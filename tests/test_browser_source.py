"""Source regeneration behavior accompanying the real-browser contracts."""
import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import subprocess
import unittest
import traceback
from unittest import mock

ROOT = Path(os.environ.get('SOURCE_ROOT', Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / 'scripts'))
import build_auth_pages as auth


class SemanticFailure(AssertionError):
    """Only the explicitly checked source behavior can emit a semantic record."""


class ProtocolResult:
    def __init__(self, result):
        self.result = result
        self.emitted = set()

    def __getattr__(self, name):
        return getattr(self.result, name)

    def report(self, error):
        if error is None:
            return
        kind, value, tb = error
        if issubclass(kind, SemanticFailure):
            assertion = str(value)
            if assertion not in self.emitted:
                self.emitted.add(assertion)
                record = dict(schema='learn-semantic-v1', assertion=assertion, observed='FAIL')
            else:
                return
        else:
            record = dict(schema='learn-setup-v1', error=''.join(traceback.format_exception(kind, value, tb)))
        print(json.dumps(record), file=sys.__stdout__, flush=True)

    def addFailure(self, test, error):
        self.report(error)
        return self.result.addFailure(test, error)

    def addError(self, test, error):
        self.report(error)
        return self.result.addError(test, error)

    def addSubTest(self, test, subtest, error):
        self.report(error)
        return self.result.addSubTest(test, subtest, error)


class ProtocolTestCase(unittest.TestCase):
    def run(self, result=None):
        return super().run(ProtocolResult(result or self.defaultTestResult()))

    def semantic_equal(self, actual, expected, assertion):
        if actual != expected:
            raise SemanticFailure(assertion)


class TestAuthGenerationWrites(ProtocolTestCase):
    def test_current_auth_pages_are_not_rewritten(self):
        with tempfile.TemporaryDirectory(prefix='learn-auth-idempotence-') as tmp:
            root = Path(tmp)
            with mock.patch.object(auth, 'ROOT', root), contextlib.redirect_stdout(io.StringIO()):
                auth.main()
                files = sorted(root.rglob('*.html'))
                self.assertEqual(2, len(files), 'both source-owned auth documents must be generated')
                expected = {p: p.read_bytes() for p in files}
                original_write = Path.write_text
                with mock.patch.object(Path, 'write_text', autospec=True, side_effect=original_write) as writes:
                    auth.main()
                    self.semantic_equal(writes.call_count, 0, 'current auth pages must not be rewritten')
                for p in files:
                    p.write_text('stale output')
                auth.main()
                self.assertEqual(expected, {p: p.read_bytes() for p in files}, 'stale auth output must be restored')


class TestBrowserSelection(ProtocolTestCase):
    def test_empty_or_incompatible_selections_fail_before_launch(self):
        courses = [p for p in (ROOT / 'site').rglob('*.html')
                   if '<body data-page-kind="course">' in p.read_text()]
        self.assertEqual(25, len(courses), 'mechanically derived course capability')
        route = '/' + courses[0].relative_to(ROOT / 'site').as_posix().removesuffix('index.html')
        cases = [(['--class=targets', '--fixtures-only'], 'fixture-only requires inventory or svg'),
                 (['--class=capstone', '--fixtures-only'], 'fixture-only requires inventory or svg'),
                 (['--class=capstone', '--only=' + route], 'selected route has no capstone capability'),
                 (['--class=unknown'], 'unknown browser contract class'),
                 (['--only=/not-a-published-route/'], 'no matching browser route')]
        for args, message in cases:
            with self.subTest(args=args), tempfile.TemporaryDirectory(prefix='learn-browser-selection-') as tmp:
                result = subprocess.run(['node', str(ROOT / 'tests/browser_acceptance.js'), '--validate-selection', *args],
                                        env=dict(os.environ, BROWSER_EVIDENCE=tmp, SOURCE_ROOT=str(ROOT), TMPDIR='/tmp'),
                                        capture_output=True, text=True)
                records = []
                for line in (result.stdout+'\n'+result.stderr).splitlines():
                    try: records.append(json.loads(line))
                    except ValueError: pass
                records = [r for r in records if isinstance(r, dict)]
                self.assertEqual('', result.stderr, 'selection child runtime diagnostics')
                self.assertEqual(1, len(records), 'one exact selection record')
                setup = [r for r in records if r.get('schema') == 'learn-setup-v1']
                for record in setup:
                    print(json.dumps(record), file=sys.__stdout__, flush=True)
                self.assertFalse(setup, 'browser selection setup failure')
                selected = [r for r in records if r.get('schema') == 'learn-selection-v1']
                # A successful exact validation witnesses the disabled guard.
                # Unexpected status, missing record, or loader failure is setup.
                if result.returncode == 0 and selected == [dict(schema='learn-selection-v1', phase='validated')]:
                    self.semantic_equal(0, 1, message)
                self.assertEqual(1, result.returncode, 'selection child status')
                self.assertEqual([dict(schema='learn-selection-v1', phase='rejected', assertion=message)], selected,
                                 'selection guard must reject for its exact assertion')
