"""Actual source-test and browser-driver failure boundaries, in subprocesses."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def classify(run, expected):
    child = subprocess.run(['node', '-e',
        "const fs=require('node:fs'),p=require('./tests/mutation_protocol');const i=JSON.parse(fs.readFileSync(0,'utf8'));console.log(JSON.stringify(p.diagnose(i.run,{expected:i.expected})));"],
        cwd=ROOT, input=json.dumps(dict(run=dict(status=run.returncode if run.returncode>=0 else None,
            signal=None if run.returncode>=0 else 'SIGTERM',stdout=run.stdout,stderr=run.stderr),expected=expected)),
        capture_output=True, text=True, check=True)
    return json.loads(child.stdout)


def evidence(name, run, result):
    if os.environ.get('GEN5_EVIDENCE'):
        dest=Path(os.environ['GEN5_EVIDENCE']);dest.mkdir(parents=True,exist_ok=True)
        (dest/(name+'.json')).write_text(json.dumps(dict(argv=run.args,exit=run.returncode,
            stdout=run.stdout,stderr=run.stderr,classification=result),indent=2)+'\n')


class TestSourceProtocol(unittest.TestCase):
    def test_auth_setup_teardown_and_semantic_boundaries(self):
        program = r'''
import sys,unittest,os
from pathlib import Path
sys.path.insert(0,sys.argv[1]);import test_browser_source as source
case=sys.argv[2];klass=source.TestAuthGenerationWrites
original=source.auth.main;calls=0
def fail(*a,**k):raise OSError('INJECTED '+case)
def main():
 global calls
 calls+=1
 if case=={1:'initial-build',2:'current-build',3:'stale-build'}.get(calls):fail()
 original()
 if calls==2 and case in ('semantic','semantic-then-teardown','semantic-then-cleanup'):
  # Exercise the real patched writer-count assertion, not a fabricated record.
  for p in source.auth.ROOT.rglob('*.html'):p.write_text(p.read_text())
source.auth.main=main
if case=='setUp':klass.setUp=fail
if case in ('tearDown','semantic-then-teardown'):klass.tearDown=fail
if case in ('cleanup','semantic-then-cleanup'):
 def setUp(self):self.addCleanup(fail)
 klass.setUp=setUp
if case=='stale-write':
 write=Path.write_text
 def rejected(p,data,*a,**k):
  if data=='stale output':fail()
  return write(p,data,*a,**k)
 Path.write_text=rejected
suite=unittest.defaultTestLoader.loadTestsFromTestCase(klass)
result=unittest.TextTestRunner(verbosity=2).run(suite);sys.exit(not result.wasSuccessful())
'''
        expected='current auth pages must not be rewritten'
        for case in ['initial-build','current-build','stale-build','stale-write','setUp','tearDown','cleanup',
                     'semantic','semantic-then-teardown','semantic-then-cleanup']:
            with self.subTest(case=case):
                run=subprocess.run(['/usr/bin/python3','-c',program,str(ROOT/'tests'),case],
                    env=dict(os.environ,TMPDIR='/tmp',SOURCE_ROOT=str(ROOT)),capture_output=True,text=True,timeout=30)
                result=classify(run,expected);evidence('auth-'+case,run,result)
                self.assertEqual(1,run.returncode)
                self.assertEqual(case=='semantic',result['caught'],case)
                if case!='semantic':self.assertTrue(result['setupRecords'],'real setup/teardown must be structured')
                if case.startswith('semantic'):self.assertTrue(result['semanticRecords'],'intended real assertion must execute')

    def test_selection_subprocess_boundaries(self):
        program=r'''
import os,sys,subprocess,unittest,json
sys.path.insert(0,sys.argv[1]);import test_browser_source as source
case=sys.argv[2];klass=source.TestBrowserSelection
original=subprocess.run
expected='fixture-only requires inventory or svg'
def run(args,**kw):
 assert kw['env']['TMPDIR']=='/tmp','actual inner TMPDIR boundary'
 assert kw['env']['SOURCE_ROOT']==str(source.ROOT),'actual inner source boundary'
 assert kw['env']['BROWSER_EVIDENCE'].startswith('/tmp/'),'actual inner diagnostic boundary'
 if case=='spawn':raise FileNotFoundError('INJECTED selection spawn')
 if case=='signal':return subprocess.CompletedProcess(args,-15,'','')
 if case=='empty':return subprocess.CompletedProcess(args,1,'','')
 if case=='wrapper':return subprocess.CompletedProcess(args,1,'',"AssertionError: '"+expected+"' not found in 'Error: Chrome launch timeout'")
 if case=='tainted-validation':return subprocess.CompletedProcess(args,0,json.dumps(dict(schema='learn-selection-v1',phase='validated'))+'\n','TypeError: late runtime failure')
 return original(args,**kw)
subprocess.run=run
def fail(*a,**k):raise OSError('INJECTED '+case)
if case=='setUp':klass.setUp=fail
if case=='tearDown':klass.tearDown=fail
if case=='cleanup':
 def setUp(self):self.addCleanup(fail)
 klass.setUp=setUp
result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(klass));sys.exit(not result.wasSuccessful())
'''
        for case in ['green','spawn','signal','empty','wrapper','tainted-validation','setUp','tearDown','cleanup']:
            with self.subTest(case=case):
                run=subprocess.run(['/usr/bin/python3','-c',program,str(ROOT/'tests'),case],
                    env=dict(os.environ,TMPDIR='/tmp',SOURCE_ROOT=str(ROOT)),capture_output=True,text=True,timeout=30)
                result=classify(run,'fixture-only requires inventory or svg');evidence('selection-'+case,run,result)
                self.assertEqual(0 if case=='green' else 1,run.returncode)
                self.assertFalse(result['caught'])
                if case!='green':self.assertTrue(result['setupRecords'])

    def test_browser_driver_setup_cannot_launder_semantics(self):
        for group in ['inventory','targets','svg','capstone','theme','contract','contrast']:
            for order in ['before','after']:
                with self.subTest(group=group,order=order), tempfile.TemporaryDirectory(prefix='lpd-',dir='/tmp') as tmp:
                    root=Path(tmp);hook=root/'hook.cjs';out=root/'out';out.mkdir()
                    hook.write_text("""const Module=require('node:module'),load=Module._load;
Module._load=function(name,...args){const value=load.call(this,name,...args);if(name==='./browser_cdp')return {...value,launch:async()=>{
const p=require(process.env.SOURCE_ROOT+'/tests/mutation_protocol');
if(process.env.TEST_ORDER==='before')p.semantic('planted expected assertion',{});
p.setup(new Error('planted setup anchor failure'));
if(process.env.TEST_ORDER==='after')p.semantic('planted expected assertion',{});
throw new Error('planted browser launch failure');}};return value;};
""")
                    driver='browser_contract_fixtures.js' if group=='contract' else 'browser_contrast.js' if group=='contrast' else 'browser_acceptance.js'
                    args=[] if group=='contract' else ['--capstones'] if group=='contrast' else ['--class='+group]
                    run=subprocess.run(['node',str(ROOT/'tests'/driver),*args],env=dict(os.environ,
                        TMPDIR='/tmp',SOURCE_ROOT=str(ROOT),BROWSER_EVIDENCE=str(out),TEST_ORDER=order,
                        NODE_OPTIONS='--require='+str(hook)),capture_output=True,text=True,timeout=30)
                    result=classify(run,'planted expected assertion');evidence('driver-'+group+'-'+order,run,result)
                    self.assertEqual(1,run.returncode)
                    self.assertFalse(result['caught'])
                    self.assertTrue(result['semanticRecords'],'fixture must reach the real driver launch boundary')
                    self.assertTrue(result['setupRecords'],'driver setup errors must remain structured')

    def test_explicit_cdp_evaluation_deadline_remains_fatal(self):
        with tempfile.TemporaryDirectory(prefix='lcd-budget-',dir='/tmp') as tmp:
            program=r'''
const assert=require('node:assert/strict'),{launch}=require('./tests/browser_cdp');
(async()=>{const c=await launch({dir:process.env.BROWSER_EVIDENCE,name:'deadline',base:'http://127.0.0.1:1'});
try{
 assert.equal(await c.evaluate('6*7'),42);
 let failure;
 try{await c.evaluate('new Promise(r=>setTimeout(()=>r("late"),250))',50);}catch(e){failure=e;}
 assert.match(String(failure),/CDP timeout Runtime.evaluate/,'the supplied finite deadline must be enforced');
 await assert.rejects(c.evaluate('42',Infinity),/invalid bounded CDP/);
 console.log(JSON.stringify({schema:'learn-budget-fixture-v1',pass:true}));
}finally{await c.close();}})().catch(e=>{console.error(e.stack);process.exitCode=1});
'''
            run=subprocess.run(['node','-e',program],cwd=ROOT,env=dict(os.environ,TMPDIR='/tmp',
                SOURCE_ROOT=str(ROOT),BROWSER_EVIDENCE=tmp),capture_output=True,text=True,timeout=60)
            result=classify(run,'CDP timeout Runtime.evaluate');evidence('cdp-deadline',run,result)
            self.assertEqual(0,run.returncode,run.stdout+run.stderr)
            self.assertFalse(result['caught'],'expected timeout is a fixture observation, never a semantic catch')

    def test_late_browser_exit_cannot_count_as_semantics(self):
        program=r'''
const {launch,sleep}=require('./tests/browser_cdp'),p=require('./tests/mutation_protocol');
(async()=>{const c=await launch({dir:process.env.BROWSER_EVIDENCE,name:'late-browser',base:'http://127.0.0.1:1'});
p.semantic('intended assertion',{});
if(process.env.TEST_SIGNAL){process.kill(c.processRecord.pid,process.env.TEST_SIGNAL);for(let i=0;i<30;i++){await sleep(100);try{process.kill(c.processRecord.pid,0);}catch{break;}}}
await c.close();process.exitCode=1;
})().catch(e=>{p.setup(e);process.exitCode=1});
'''
        for sig in ['', 'SIGTERM', 'SIGKILL']:
            with self.subTest(signal=sig), tempfile.TemporaryDirectory(prefix='lcd-late-',dir='/tmp') as tmp:
                run=subprocess.run(['node','-e',program],cwd=ROOT,env=dict(os.environ,TMPDIR='/tmp',
                    SOURCE_ROOT=str(ROOT),BROWSER_EVIDENCE=tmp,TEST_SIGNAL=sig),capture_output=True,text=True,timeout=60)
                result=classify(run,'intended assertion');evidence('late-browser-'+(sig or 'normal'),run,result)
                self.assertEqual(1,run.returncode)
                self.assertEqual(not sig,result['caught'],'late browser failure must taint the semantic record')
                self.assertEqual(1,len(result['semanticRecords']))
                self.assertEqual(bool(sig),bool(result['setupRecords']))
                proof=json.loads((Path(tmp)/'late-browser-cleanup.json').read_text())
                if sig=='SIGKILL':self.assertEqual(sig,proof['signalCode'])
                if sig:self.assertTrue(proof['prematureExit'],'unsolicited browser exit must remain distinct from graceful close')
                self.assertFalse(proof['pidAlive']);self.assertFalse(proof['profileExists'])

    def test_chrome_spawn_and_nonzero_diagnostics_survive_cleanup(self):
        program=r'''
const Module=require('node:module'),load=Module._load;
Module._load=function(name,...a){const m=load.call(this,name,...a);if(name==='node:child_process')return {...m,spawn:(command,args,options)=>command==='/usr/bin/google-chrome'?process.env.TEST_FAILURE==='spawn'?m.spawn('/tmp/lcd-missing-chrome-'+process.pid,args,options):m.spawn('/usr/bin/python3',['-c','raise SystemExit(7)'],options):m.spawn(command,args,options)};return m;};
const {launch}=require('./tests/browser_cdp'),p=require('./tests/mutation_protocol');
launch({dir:process.env.BROWSER_EVIDENCE,name:'chrome-failure',base:'http://127.0.0.1:1'}).then(()=>{throw Error('fixture must fail launch');}).catch(e=>{p.setup(e);process.exitCode=1;});
'''
        for failure in ['spawn','nonzero']:
            with self.subTest(failure=failure), tempfile.TemporaryDirectory(prefix='lcd-spawn-',dir='/tmp') as tmp:
                run=subprocess.run(['node','-e',program],cwd=ROOT,env=dict(os.environ,TMPDIR='/tmp',
                    SOURCE_ROOT=str(ROOT),BROWSER_EVIDENCE=tmp,TEST_FAILURE=failure),capture_output=True,text=True,timeout=60)
                result=classify(run,'intended assertion');evidence('chrome-'+failure,run,result)
                self.assertEqual(1,run.returncode);self.assertFalse(result['caught']);self.assertTrue(result['setupRecords'])
                proof=json.loads((Path(tmp)/'chrome-failure-cleanup.json').read_text())
                self.assertFalse(proof['pidAlive']);self.assertFalse(proof['profileExists'])
                if failure=='spawn':
                    self.assertEqual('ENOENT',proof['error']['code'])
                    self.assertEqual('ENOENT',result['setupRecords'][0]['errorData']['code'])
                    self.assertIn('Chrome cleanup:',result['setupRecords'][0]['error'])
                else:
                    self.assertEqual(7,proof['exitCode'])
                    self.assertEqual(7,result['setupRecords'][0]['errorData']['status'])

    def test_mutation_anchor_failure_is_structured_setup(self):
        # Execute the actual runner's case loop without the expensive preflight.
        # This fixture selects one deliberately absent mutation anchor; no driver
        # is allowed to execute, and no synthetic output supplies a semantic catch.
        program=r'''
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const protocol=require('./tests/mutation_protocol'),OUT=process.env.BROWSER_EVIDENCE;
const file=path.join(OUT,'owned-source');fs.writeFileSync(file,'original bytes');
const source=fs.readFileSync('./tests/mutate_browser_ui.js','utf8');
const code=source.slice(source.indexOf('const summary=[];'),source.indexOf(" assert.equal(summary.length,selected.length"));
assert(code.includes('for(const c of selected)'),'real nonempty case loop');
const selected=[{name:'anchor-fixture',file,group:'source',expected:'intended assertion',change(){throw Error('mutation anchor absent: intended assertion');}}];
const context={fs,path,assert,protocol,OUT,selected,console,commandFor:()=>({command:'node',args:[],driver:'fixture'}),execute(){throw Error('driver must not execute after failed setup');}};
assert.throws(()=>vm.runInNewContext(code,context),/mutation escaped or failed for an unrelated reason/);
const result=JSON.parse(fs.readFileSync(path.join(OUT,'anchor-fixture/result.json')));
assert.equal(fs.readFileSync(file,'utf8'),'original bytes');assert.equal(result.caught,false);assert.equal(result.status,null);
assert(result.setupRecords.length,'anchor failure must be structured setup');
assert.equal(result.setupRecords[0].stage,'mutation-setup','anchor failure must be setup');
assert.match(result.error.message,/mutation anchor absent/,'original exception must survive');
assert(fs.readFileSync(path.join(OUT,'anchor-fixture/command.log'),'utf8').includes('learn-setup-v1'),'setup log must survive');
'''
        with tempfile.TemporaryDirectory(prefix='lcd-anchor-',dir='/tmp') as tmp:
            run=subprocess.run(['node','-e',program],cwd=ROOT,env=dict(os.environ,TMPDIR='/tmp',
                SOURCE_ROOT=str(ROOT),BROWSER_EVIDENCE=tmp),capture_output=True,text=True,timeout=60)
            result=classify(run,'intended assertion');evidence('mutation-anchor',run,result)
            self.assertEqual(0,run.returncode,run.stdout+run.stderr)
