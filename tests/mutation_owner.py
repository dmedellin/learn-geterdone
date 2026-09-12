"""Responsive Linux subreaper owning exactly one mutation export/profile root.

Descendant identities use kernel parentage and start times, including children
of non-main threads. Directory cleanup is descriptor-relative and bounded;
replacements, symlinks and diagnostic failures fail closed.
"""
import ctypes
import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import tempfile
import time
import traceback


def identity(pid):
    try:
        fields = Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()
        return {'pid': pid, 'start': fields[19], 'state': fields[0], 'ppid': int(fields[1])}
    except (FileNotFoundError, ProcessLookupError):
        return None


def descendants():
    found, todo = {}, [os.getpid()]
    while todo:
        pid = todo.pop()
        try:
            tasks = list(Path(f'/proc/{pid}/task').iterdir())
        except (FileNotFoundError, ProcessLookupError):
            continue
        for task in tasks:
            try:
                children = (task/'children').read_text().split()
            except (FileNotFoundError, ProcessLookupError):
                continue
            for child in map(int, children):
                row = identity(child)
                if row and child not in found:
                    found[child] = row
                    todo.append(child)
    return found


def error_data(error):
    return {'name': type(error).__name__, 'message': str(error),
            'errno': getattr(error, 'errno', None), 'filename': getattr(error, 'filename', None),
            'traceback': ''.join(traceback.format_exception(error))}


def signal_owned(row, sig):
    current = identity(row['pid'])
    if current and current['start'] == row['start']:
        try:
            os.kill(row['pid'], sig)
        except ProcessLookupError:
            pass


def own(path, owned):
    # Record ownership before subsequent initialization can fail.
    info = path.lstat()
    row = {'path': str(path), 'device': info.st_dev, 'inode': info.st_ino, 'removed': False}
    owned.append(row)
    if not stat.S_ISDIR(info.st_mode):
        raise RuntimeError('owned path is not a directory: '+str(path))


def remove_owned(row, deadline):
    target = Path(row['path'])
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    def check_time():
        if time.monotonic() > deadline:
            raise TimeoutError('owned directory cleanup timeout')
    def matches(info):
        return (info.st_dev, info.st_ino) == (row['device'], row['inode'])
    def empty(fd):
        for name in os.listdir(fd):
            check_time()
            info = os.stat(name, dir_fd=fd, follow_symlinks=False)
            if stat.S_ISDIR(info.st_mode):
                sub = os.open(name, flags, dir_fd=fd)
                try:
                    opened = os.fstat(sub)
                    if (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino):
                        raise RuntimeError('owned descendant identity changed')
                    if opened.st_dev != row['device']:
                        raise RuntimeError('refusing mounted directory in owned root')
                    empty(sub)
                finally:
                    os.close(sub)
                os.rmdir(name, dir_fd=fd)
            else:
                os.unlink(name, dir_fd=fd)  # unlink symlinks; never follow them
    parent = os.open(target.parent, flags)
    try:
        info = os.stat(target.name, dir_fd=parent, follow_symlinks=False)
        if not stat.S_ISDIR(info.st_mode) or not matches(info):
            raise RuntimeError('owned directory identity changed: '+str(target))
        fd = os.open(target.name, flags, dir_fd=parent)
        try:
            if not matches(os.fstat(fd)):
                raise RuntimeError('owned directory identity changed: '+str(target))
            check_time()
            empty(fd)
        finally:
            os.close(fd)
        if not matches(os.stat(target.name, dir_fd=parent, follow_symlinks=False)):
            raise RuntimeError('owned directory identity changed: '+str(target))
        os.rmdir(target.name, dir_fd=parent)
        row['removed'] = not os.path.lexists(target)
        if not row['removed']:
            raise RuntimeError('owned directory remains: '+str(target))
    finally:
        os.close(parent)


def main():
    requested_signals, owned = [], []
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda number, frame: requested_signals.append(number))
    root = Path(__file__).resolve().parents[1]
    out = None
    worker = None
    proof = {'schema': 'learn-ownership-v1', 'supervisor': identity(os.getpid()),
             'signals': requested_signals, 'directories': owned, 'children': [],
             'reaped': [], 'remaining_children': [], 'errors': [],
             'worker': {'command': [*sys.argv[1:2], str(root/'tests/mutate_browser_ui.js'), *sys.argv[2:]],
                        'status': None, 'signal': None, 'error': None}}
    exit_code = 1
    try:
        candidate = Path(os.environ['BROWSER_EVIDENCE']).resolve()
        if candidate == root or candidate.is_relative_to(root):
            raise ValueError('external evidence directory required')
        out = candidate
        out.mkdir(parents=True, exist_ok=True)
        # Establish adoption before creating anything or starting a worker.
        if ctypes.CDLL(None, use_errno=True).prctl(36, 1, 0, 0, 0):
            raise OSError(ctypes.get_errno(), 'cannot establish child ownership')
        export = out/'disposable-export'
        export.mkdir()  # never adopt a preexisting path, including a symlink
        own(export, owned)
        profiles = Path(tempfile.mkdtemp(prefix='lm-', dir='/tmp'))
        own(profiles, owned)
        if not requested_signals:
            try:
                worker = subprocess.Popen(proof['worker']['command'], env=dict(os.environ,
                    LEARN_MUTATION_WORKER='1', LEARN_PROFILE_ROOT=str(profiles), TMPDIR='/tmp',
                    SOURCE_ROOT=str(root), BROWSER_EVIDENCE=str(out)))
                proof['worker']['identity'] = identity(worker.pid)
            except BaseException as error:
                proof['worker']['error'] = error_data(error)
                raise
            while worker.poll() is None and not requested_signals:
                time.sleep(.025)
            code = worker.returncode
            if code is not None:
                proof['worker'].update(returncode=code, status=code if code >= 0 else None,
                                       signal=signal.Signals(-code).name if code < 0 else None)
                exit_code = code if code >= 0 else 128-code
    except BaseException as error:
        proof['errors'].append(error_data(error))
    finally:
        deadline = time.monotonic()+15
        seen = {}
        try:
            while True:
                children = descendants()
                seen.update({(r['pid'], r['start']): r for r in children.values()})
                # Freeze parents first to stop forks, then kill only identities
                # still belonging to this supervisor (never global name matches).
                for sig in (signal.SIGSTOP, signal.SIGKILL):
                    for row in children.values():
                        signal_owned(row, sig)
                while True:
                    try:
                        pid, status = os.waitpid(-1, os.WNOHANG)
                        if not pid:
                            break
                        proof['reaped'].append({'pid': pid, 'wait_status': status,
                                                'returncode': os.waitstatus_to_exitcode(status)})
                    except ChildProcessError:
                        break
                if not descendants():
                    break
                if time.monotonic() > deadline:
                    raise TimeoutError('owned child cleanup timeout')
                time.sleep(.02)
        except BaseException as error:
            proof['errors'].append(error_data(error))
        proof['children'] = list(seen.values())
        proof['remaining_children'] = list(descendants().values())
        if worker and proof['worker']['status'] is None and proof['worker']['signal'] is None:
            reaped = next((r for r in proof['reaped'] if r['pid'] == worker.pid), None)
            code = reaped['returncode'] if reaped else worker.poll()
            if code is not None:
                worker.returncode = code
                proof['worker'].update(returncode=code, status=code if code >= 0 else None,
                                       signal=signal.Signals(-code).name if code < 0 else None)
        for row in reversed(owned):
            try:
                if proof['remaining_children']:
                    raise RuntimeError('cannot clean directories while descendants remain')
                remove_owned(row, time.monotonic()+15)
            except BaseException as error:
                row['error'] = error_data(error)
                proof['errors'].append(row['error'])
        if requested_signals:
            exit_code = 128+requested_signals[0]
        if proof['errors'] or proof['remaining_children'] or any(not row['removed'] for row in owned):
            exit_code = 1
        proof['exit_code'] = exit_code
        try:
            if out is None:
                raise RuntimeError('no safe external diagnostic destination')
            (out/'ownership-cleanup.json').write_text(json.dumps(proof, indent=2)+'\n')
        except BaseException as error:
            exit_code = proof['exit_code'] = 1
            proof['errors'].append(error_data(error))
            print(json.dumps({'schema': 'learn-setup-v1', 'error': error_data(error)}), file=sys.stderr, flush=True)
        print(json.dumps({'ownership_cleanup': proof}), flush=True)
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
