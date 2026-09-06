"""Source regeneration behavior accompanying the real-browser contracts."""
import contextlib
import io
import os
from pathlib import Path
import sys
import tempfile
import subprocess
import unittest
from unittest import mock

ROOT = Path(os.environ.get('SOURCE_ROOT', Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / 'scripts'))
import build_auth_pages as auth


class TestAuthGenerationWrites(unittest.TestCase):
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
                    self.assertEqual(0, writes.call_count, 'current auth pages must not be rewritten')
                for p in files:
                    p.write_text('stale output')
                auth.main()
                self.assertEqual(expected, {p: p.read_bytes() for p in files}, 'stale auth output must be restored')


class TestBrowserSelection(unittest.TestCase):
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
                result = subprocess.run(['node', str(ROOT / 'tests/browser_acceptance.js'), *args],
                                        env=dict(os.environ, BROWSER_EVIDENCE=tmp, SOURCE_ROOT=str(ROOT)),
                                        capture_output=True, text=True)
                self.assertEqual(1, result.returncode, 'empty browser selection must fail')
                self.assertIn(message, result.stdout + result.stderr)
