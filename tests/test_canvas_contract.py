"""Source closure for the authored canvas text layer; browser proofs are separate."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestCanvasSourceContract(unittest.TestCase):
    def run_node(self, script, *args, evidence=None):
        environment = dict(os.environ, SOURCE_ROOT=str(ROOT), TMPDIR='/tmp')
        if evidence is not None:
            environment['GEN5_EVIDENCE'] = str(evidence)
        run = subprocess.run(['node', str(ROOT / script), *map(str, args)], cwd=ROOT,
                             env=environment, capture_output=True, text=True, timeout=90)
        if os.environ.get('GEN5_EVIDENCE'):
            out = Path(os.environ['GEN5_EVIDENCE'])
            out.mkdir(parents=True, exist_ok=True)
            (out / (Path(script).stem + '-source-check.json')).write_text(json.dumps({
                'argv': run.args, 'cwd': str(ROOT), 'exit': run.returncode,
                'stdout': run.stdout, 'stderr': run.stderr}, indent=2) + '\n')
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        return run

    def test_all_published_sources_have_bound_text(self):
        run = self.run_node('scripts/canvas_sources.js', ROOT)
        result = json.loads(run.stdout)
        self.assertEqual(result['htmlRoutes'], 369)
        self.assertEqual(result['canvasRoutes'], 66)
        self.assertEqual(result['canvases'], 71)
        self.assertEqual(result['contractOccurrences'], 269)
        self.assertEqual(result['nativeProductOccurrences'], 0)
        self.assertEqual(result['unbound'], 0)
        self.assertEqual(result['errors'], [])

    def test_lexical_and_implementation_guard_canaries(self):
        for script in ('canvas_lexer_fixtures.js', 'canvas_property_fixtures.js',
                       'canvas_surface_fixtures.js', 'canvas_interpolation_fixtures.js',
                       'canvas_captured_state_fixtures.js', 'canvas_closure_fixtures.js',
                       'canvas_implementation_fixtures.js', 'javascript_template_fixtures.js',
                       'canvas_interval_fixtures.js', 'canvas_initial_fixtures.js',
                       'canvas_enclosing_state_fixtures.js', 'canvas_html_source_fixtures.js',
                       'canvas_html_maintenance_fixtures.js', 'canvas_schema_fixtures.js',
                       'canvas_constant_range_fixtures.js', 'canvas_coverage_fixtures.js'):
            with self.subTest(script=script):
                self.run_node('tests/' + script)

    def test_empty_owned_source_inventory_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix='lci-', dir='/tmp') as temporary:
            self.run_node('tests/canvas_inventory_fixtures.js', evidence=temporary)
            result = json.loads((Path(temporary) / 'empty-inventory-observation.json').read_text())
            self.assertEqual(result['removed'], 269)
            self.assertEqual(result['result']['contractOccurrences'], 0)
            cleanup = json.loads((Path(temporary) / 'empty-inventory-cleanup.json').read_text())
            self.assertTrue(cleanup['before']['exists'])
            self.assertFalse(cleanup['existsAfter'])
