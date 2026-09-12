"""Real signals at owned-export and active-browser boundaries.

Assertions record residue before teardown. Test cleanup is never passing
product evidence; it only prevents a RED fixture leaking into another run.
"""
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time
import unittest
import sys

ROOT = Path(__file__).resolve().parents[1]


def alive(pid):
    try:
        return Path(f'/proc/{pid}/stat').read_text().split(') ')[1][0] != 'Z'
    except FileNotFoundError:
        return False


class TestSignalOwnership(unittest.TestCase):
    def test_signals_at_copy_and_browser_boundaries(self):
        records = []
        for boundary in ['post-copy', 'active-browser']:
            for sig in [signal.SIGTERM, signal.SIGINT]:
                with self.subTest(boundary=boundary, signal=sig.name):
                    with tempfile.TemporaryDirectory(prefix='learn-gen5-signals-', dir='/tmp') as tmp:
                        root = Path(tmp)
                        out = root / 'diagnostics'
                        out.mkdir()
                        sentinel = out / 'unrelated-sentinel'
                        sentinel.write_text('must survive')
                        hook = root / 'boundary.cjs'
                        # Pause exactly after the export is copied, before the
                        # preflight child starts. Signals target the main PID.
                        hook.write_text("const fs=require('node:fs'),path=require('node:path');const mkdir=fs.mkdirSync;fs.mkdirSync=function(p,...a){const r=mkdir.call(this,p,...a);if(process.env.TEST_BOUNDARY==='post-copy'&&path.basename(String(p))==='target-preflight'){fs.writeFileSync(path.join(process.env.BROWSER_EVIDENCE,'boundary-ready'),'ready');Atomics.wait(new Int32Array(new SharedArrayBuffer(4)),0,0,60000)}return r};")
                        logpath = out / 'outer.log'
                        with logpath.open('w') as log:
                            child = subprocess.Popen(['node', str(ROOT/'tests/mutate_browser_ui.js'), '--case=runtime-named-process'],
                                cwd=ROOT, env=dict(os.environ, TMPDIR='/tmp', BROWSER_EVIDENCE=str(out),
                                    TEST_BOUNDARY=boundary, NODE_OPTIONS='--require='+str(hook)),
                                stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                            browsers = []
                            try:
                                deadline = time.monotonic()+40
                                while time.monotonic()<deadline and child.poll() is None:
                                    browsers = [json.loads(p.read_text()) for p in out.rglob('*-process.json')]
                                    ready = (out/'boundary-ready').exists() if boundary=='post-copy' else any(Path(b['profile'],'DevToolsActivePort').exists() for b in browsers)
                                    if ready: break
                                    time.sleep(.02)
                                self.assertTrue(ready, 'real ownership boundary must be reached')
                                child.send_signal(sig)
                                time.sleep(.002)
                                if child.poll() is None: child.send_signal(sig)
                                child.wait(timeout=20)
                                time.sleep(.2)
                                export = out/'disposable-export'
                                row = dict(boundary=boundary, signal=sig.name, exit=child.returncode,
                                    export_exists=export.exists(), owned_files=sum(p.is_file() for p in export.rglob('*')),
                                    browsers_alive=[b['pid'] for b in browsers if alive(b['pid'])],
                                    profiles_remaining=[b['profile'] for b in browsers if Path(b['profile']).exists()],
                                    diagnostics_retained=logpath.exists(), sentinel=sentinel.read_text())
                                records.append(row)
                                if os.environ.get('GEN5_EVIDENCE'):
                                    dest=Path(os.environ['GEN5_EVIDENCE']); dest.mkdir(exist_ok=True,parents=True)
                                    (dest/'signal-observations.json').write_text(json.dumps(records,indent=2)+'\n')
                                    (dest/f'{boundary}-{sig.name}.log').write_bytes(logpath.read_bytes())
                                self.assertEqual(128+sig, row['exit'], 'main must forward the signal and retain its exit semantics')
                                self.assertFalse(row['export_exists'], 'owned export survives main signal exit')
                                self.assertEqual([],row['browsers_alive'],'owned browser survives main signal exit')
                                self.assertEqual([],row['profiles_remaining'],'owned profile survives main signal exit')
                                self.assertEqual('must survive',row['sentinel'])
                                proof=json.loads((out/'ownership-cleanup.json').read_text())
                                self.assertEqual([],proof['remaining_children'],'all adopted children must be reaped')
                                self.assertEqual([],proof['errors'],'cleanup cannot silently degrade')
                            except BaseException as error:
                                failure=dict(boundary=boundary,signal=sig.name,error=repr(error),
                                    export_exists=(out/'disposable-export').exists(),
                                    owned_files=sum(p.is_file() for p in (out/'disposable-export').rglob('*')),
                                    browsers=browsers,exit=child.poll())
                                if os.environ.get('GEN5_EVIDENCE'):
                                    dest=Path(os.environ['GEN5_EVIDENCE']);dest.mkdir(parents=True,exist_ok=True)
                                    (dest/f'{boundary}-{sig.name}-failure-before-teardown.json').write_text(json.dumps(failure,indent=2)+'\n')
                                raise
                            finally:
                                if child.poll() is None:
                                    # A failed forwarding guard must not leak the
                                    # real owner: notify its exact child PID only
                                    # after recording the failed product boundary.
                                    children=Path(f'/proc/{child.pid}/task/{child.pid}/children')
                                    if children.exists():
                                        for pid in map(int,children.read_text().split()):
                                            try:os.kill(pid,signal.SIGTERM)
                                            except ProcessLookupError:pass
                                    try:child.wait(timeout=20)
                                    except subprocess.TimeoutExpired:child.kill();child.wait()
                                # Only after the assertions/evidence above.
                                try: os.killpg(child.pid, signal.SIGKILL)
                                except ProcessLookupError: pass
                                for b in browsers:
                                    try: os.killpg(b['pid'], signal.SIGKILL)
                                    except ProcessLookupError: pass
                                    if Path(b['profile']).is_relative_to(out): shutil.rmtree(b['profile'],ignore_errors=True)

    def test_initialization_and_cleanup_fail_closed(self):
        for failure in ['before-ownership','after-ownership','preexisting-export','cleanup-failure']:
            with self.subTest(failure=failure), tempfile.TemporaryDirectory(prefix='learn-owner-failure-',dir='/tmp') as tmp:
                root=Path(tmp);out=root/'diagnostics';out.mkdir()
                sentinel=root/'unrelated';sentinel.write_text('unchanged')
                if failure=='preexisting-export':
                    (out/'disposable-export').mkdir();(out/'disposable-export'/'sentinel').write_text('not owned')
                # Run the actual supervisor in a fresh process, injecting at
                # explicit ownership boundaries. Never clean before assertions.
                program="""
import sys,os,subprocess,shutil
from pathlib import Path
sys.path.insert(0,sys.argv[1]);import mutation_owner
case=sys.argv[2];out=Path(os.environ['BROWSER_EVIDENCE'])
def fail(*a,**k): raise OSError('INJECTED '+case)
if case=='before-ownership':
 original=Path.mkdir
 def mkdir(p,*a,**k):
  if p.name=='disposable-export': fail()
  return original(p,*a,**k)
 Path.mkdir=mkdir
elif case=='after-ownership': subprocess.Popen=fail
elif case=='cleanup-failure':
 original=mutation_owner.remove_owned
 def remove(row,*a,**k):
  if Path(row['path']).name=='disposable-export': fail()
  return original(row,*a,**k)
 mutation_owner.remove_owned=remove
 subprocess.Popen=fail
sys.argv=['mutation_owner.py','node']
sys.exit(mutation_owner.main())
"""
                run=subprocess.run(['/usr/bin/python3','-c',program,str(ROOT/'tests'),failure],env=dict(os.environ,BROWSER_EVIDENCE=str(out),TMPDIR='/tmp'),capture_output=True,text=True)
                proof=json.loads((out/'ownership-cleanup.json').read_text())
                record=dict(case=failure,exit=run.returncode,proof=proof,output=run.stdout+run.stderr,export_exists=(out/'disposable-export').exists())
                if os.environ.get('GEN5_EVIDENCE'):
                    dest=Path(os.environ['GEN5_EVIDENCE']);dest.mkdir(exist_ok=True,parents=True)
                    (dest/(failure+'.json')).write_text(json.dumps(record,indent=2)+'\n')
                self.assertEqual(1,run.returncode,'ownership failures must fail closed')
                self.assertTrue(proof['errors'],'failure diagnostics must be retained')
                self.assertEqual([],proof['remaining_children'])
                self.assertEqual(failure in ['preexisting-export','cleanup-failure'],record['export_exists'])
                self.assertEqual('unchanged',sentinel.read_text())
                if failure=='preexisting-export':self.assertEqual('not owned',(out/'disposable-export'/'sentinel').read_text())

    def test_worker_and_directory_failure_matrix(self):
        cases = ['success', 'worker-nonzero', 'worker-signal', 'double-fork', 'thread-fork',
                 'preflight-exception', 'loop-exception', 'subreaper-init', 'profile-init',
                 'spawn-error', 'preexisting-symlink', 'identity-swap', 'internal-symlink',
                 'cleanup-timeout', 'diagnostic-write']
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory(prefix='lcd-', dir='/tmp') as tmp:
                root = Path(tmp); out = root/'evidence'; out.mkdir()
                sentinel = root/'unrelated'; sentinel.mkdir(); (sentinel/'bytes').write_bytes(b'untouched\x00\xff')
                program = r'''
import os,sys,subprocess,tempfile,time,signal,threading
from pathlib import Path
sys.path.insert(0,sys.argv[1]);import mutation_owner as owner
case=sys.argv[2];out=Path(os.environ['BROWSER_EVIDENCE']);sentinel=out.parent/'unrelated'
original=subprocess.Popen
worker=out/'worker.py'
worker.write_text("""import os,signal,time,sys,threading
from pathlib import Path
out=Path(os.environ['BROWSER_EVIDENCE']);case=sys.argv[1]
(out/'disposable-export'/'owned').write_bytes(b'owned')
if case in ('preflight-exception','loop-exception'):raise RuntimeError('INJECTED '+case)
if case=='worker-signal':os.kill(os.getpid(),signal.SIGTERM)
if case in ('double-fork','thread-fork'):
 def fork():
  if os.fork()==0:
   os.setsid()
   if os.fork()>0:os._exit(0)
   (out/'escaped.pid').write_text(str(os.getpid()))
   signal.signal(signal.SIGTERM,signal.SIG_IGN)
   for i in range(8):
    if os.fork()==0:
     while True:time.sleep(.01)
    time.sleep(.005)
   while True:time.sleep(.01)
 if case=='thread-fork':
  t=threading.Thread(target=fork);t.start();t.join()
 else:fork()
 while not (out/'escaped.pid').exists():time.sleep(.01)
sys.exit(7 if case=='worker-nonzero' else 0)
""")
def popen(*a,**kw):
 if case=='spawn-error':raise FileNotFoundError(2,'INJECTED spawn','missing-worker')
 if case=='identity-swap':
  (out/'disposable-export').rename(out/'moved-owned')
  (out/'disposable-export').mkdir();(out/'disposable-export'/'foreign').write_bytes(b'foreign')
 if case=='internal-symlink':(out/'disposable-export'/'link').symlink_to(sentinel,target_is_directory=True)
 return original(['/usr/bin/python3',str(worker),case],**kw)
subprocess.Popen=popen
if case=='subreaper-init':
 def fail(*a,**kw):raise OSError('INJECTED initialization')
 owner.ctypes.CDLL=fail
if case=='profile-init':
 def fail(*a,**kw):raise OSError('INJECTED profile initialization')
 tempfile.mkdtemp=fail
if case=='preexisting-symlink':(out/'disposable-export').symlink_to(sentinel,target_is_directory=True)
if case=='cleanup-timeout':
 original_remove=owner.remove_owned
 def remove(row,deadline):return original_remove(row,0)
 owner.remove_owned=remove
if case=='diagnostic-write':
 write=Path.write_text
 def reject(p,*a,**kw):
  if p.name=='ownership-cleanup.json':raise OSError('INJECTED diagnostic write')
  return write(p,*a,**kw)
 Path.write_text=reject
sys.argv=['mutation_owner.py','node'];sys.exit(owner.main())
'''
                started = time.monotonic()
                run = subprocess.run(['/usr/bin/python3', '-c', program, str(ROOT/'tests'), case],
                    env=dict(os.environ, BROWSER_EVIDENCE=str(out), TMPDIR='/tmp'), capture_output=True, text=True, timeout=25)
                proof = next(json.loads(line)['ownership_cleanup'] for line in run.stdout.splitlines()
                             if line.startswith('{"ownership_cleanup":'))
                escaped = int((out/'escaped.pid').read_text()) if (out/'escaped.pid').exists() else None
                row = dict(case=case, argv=run.args, exit=run.returncode, seconds=time.monotonic()-started,
                           stdout=run.stdout, stderr=run.stderr, proof=proof,
                           export_exists=os.path.lexists(out/'disposable-export'),
                           escaped_exists=escaped is not None and Path(f'/proc/{escaped}').exists(),
                           sentinel=(sentinel/'bytes').read_bytes().hex())
                if os.environ.get('GEN5_EVIDENCE'):
                    dest=Path(os.environ['GEN5_EVIDENCE']);dest.mkdir(parents=True,exist_ok=True)
                    (dest/(case+'.json')).write_text(json.dumps(row,indent=2)+'\n')
                try:
                    expected = 7 if case=='worker-nonzero' else 143 if case=='worker-signal' else 0 if case in ['success','double-fork','thread-fork','internal-symlink'] else 1
                    self.assertEqual(expected, run.returncode, 'worker and supervisor exits must remain distinct')
                    self.assertEqual([], proof['remaining_children'], 'all descendants must be reaped')
                    self.assertFalse(row['escaped_exists'], 'double-fork/setsid descendant escaped ownership')
                    self.assertEqual(b'untouched\x00\xff'.hex(), row['sentinel'])
                    self.assertEqual(case in ['preexisting-symlink','identity-swap','cleanup-timeout'],row['export_exists'])
                    if case=='spawn-error':
                        self.assertEqual(2,proof['worker']['error']['errno'])
                        self.assertEqual('missing-worker',proof['worker']['error']['filename'])
                    if case=='worker-signal':
                        self.assertEqual('SIGTERM',proof['worker']['signal']);self.assertIsNone(proof['worker']['status'])
                    if case=='worker-nonzero':self.assertEqual(7,proof['worker']['status'])
                    if case=='identity-swap':self.assertEqual(b'foreign',(out/'disposable-export'/'foreign').read_bytes())
                    if case=='diagnostic-write':
                        self.assertFalse((out/'ownership-cleanup.json').exists());self.assertIn('INJECTED diagnostic write',run.stderr)
                    for directory in proof['directories']:
                        if case not in ['identity-swap','cleanup-timeout']:
                            self.assertFalse(Path(directory['path']).exists(),'owned profile/export residue')
                finally:
                    # Evidence and assertions above precede fixture-only cleanup.
                    if escaped and Path(f'/proc/{escaped}').exists():
                        try:os.kill(escaped,signal.SIGKILL)
                        except ProcessLookupError:pass
                    for directory in proof['directories']:
                        path=Path(directory['path'])
                        if path.exists() and not path.is_symlink() and (path.stat().st_dev,path.stat().st_ino)==(directory['device'],directory['inode']):
                            shutil.rmtree(path)

    def test_real_preflight_exception_and_browser_death(self):
        for boundary in ['post-copy-exception','browser-death']:
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory(prefix='lcf-',dir='/tmp') as tmp:
                root=Path(tmp);out=root/'evidence';out.mkdir()
                sentinel=out/'unrelated';sentinel.write_bytes(b'external diagnostics\x00')
                hook=root/'hook.cjs'
                hook.write_text("const fs=require('node:fs'),path=require('node:path'),mkdir=fs.mkdirSync;fs.mkdirSync=function(p,...a){const v=mkdir.call(this,p,...a);if(process.env.TEST_BOUNDARY==='post-copy-exception'&&path.basename(String(p))==='target-preflight')throw Error('INJECTED real post-copy preflight failure');return v;};")
                with (out/'command.log').open('w') as log:
                    command=['node',str(ROOT/'tests/mutate_browser_ui.js'),'--case=runtime-named-process']
                    child=subprocess.Popen(command,env=dict(os.environ,TMPDIR='/tmp',BROWSER_EVIDENCE=str(out),
                        TEST_BOUNDARY=boundary,NODE_OPTIONS='--require='+str(hook)),stdout=log,stderr=subprocess.STDOUT)
                    browsers=[];started=time.monotonic()
                    try:
                        if boundary=='browser-death':
                            deadline=time.monotonic()+30;ready=False
                            while child.poll() is None and time.monotonic()<deadline:
                                for p in out.rglob('*-process.json'):
                                    try:
                                        row=json.loads(p.read_text())
                                        if Path(row['profile'],'DevToolsActivePort').exists():browsers=[row];ready=True;break
                                    except ValueError:pass
                                if ready:break
                                time.sleep(.02)
                            self.assertTrue(ready,'real browser must be active before injecting death')
                            os.kill(browsers[0]['pid'],signal.SIGKILL)
                        child.wait(timeout=85)
                        proof=json.loads((out/'ownership-cleanup.json').read_text())
                        row=dict(boundary=boundary,argv=command,exit=child.returncode,seconds=time.monotonic()-started,
                                 proof=proof,export_exists=(out/'disposable-export').exists(),
                                 browser_residue=[b for b in browsers if Path(f"/proc/{b['pid']}").exists() or Path(b['profile']).exists()],
                                 sentinel=sentinel.read_bytes().hex(),log=(out/'command.log').read_text())
                        if os.environ.get('GEN5_EVIDENCE'):
                            dest=Path(os.environ['GEN5_EVIDENCE']);dest.mkdir(parents=True,exist_ok=True)
                            (dest/(boundary+'.json')).write_text(json.dumps(row,indent=2)+'\n')
                        self.assertEqual(1,child.returncode,'setup/browser failure cannot produce aggregate success')
                        self.assertFalse(row['export_exists']);self.assertFalse(row['browser_residue'])
                        self.assertEqual([],proof['remaining_children']);self.assertEqual([],proof['errors'])
                        self.assertEqual(b'external diagnostics\x00'.hex(),row['sentinel'])
                    finally:
                        if child.poll() is None:
                            child.send_signal(signal.SIGTERM);child.wait(timeout=20)
