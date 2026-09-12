"""The authored deck's renewable accessibility regions must survive maintenance."""
import importlib.util
import os
from pathlib import Path
import unittest

ROOT = Path(os.environ.get('SOURCE_ROOT', Path(__file__).resolve().parents[1]))
SITE = Path(os.environ.get('SITE_ROOT', ROOT / 'site'))
spec = importlib.util.spec_from_file_location('deck_capstone', ROOT / 'scripts/mathpath/capstone.py')
capstone = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capstone)


class TestDeckNormalization(unittest.TestCase):
    def setUp(self):
        self.source = (SITE / 'paths/trading/iren-analysis-2026-08-16/slides/index.html').read_text()

    def test_authored_deck_is_current(self):
        self.assertEqual(capstone.normalize_deck_accessibility(self.source), self.source)

    def test_repairs_all_owned_regions(self):
        damaged = self.source.replace(' tabindex="0" role="region"', ' tabindex="-1" role="region"')
        damaged = damaged.replace('aria-label="Slide 1 of 16: Backtests &amp; Current Analysis"', 'aria-label="missing"')
        damaged = damaged.replace('.deck { min-width:0; min-height:0; height:100%; overflow:visible; }', '.deck { min-width:0; min-height:0; height:100%; overflow:hidden; }')
        damaged = damaged.replace("if(e.key==='ArrowRight')", "if(e.key==='PageDown'||e.key==='ArrowRight')")
        self.assertNotEqual(damaged, self.source)
        self.assertEqual(capstone.normalize_deck_accessibility(damaged), self.source, 'renewable deck accessibility must be restored exactly')

    def test_missing_layout_is_not_silently_skipped(self):
        damaged = self.source.replace('<style data-deck-layout>', '<style data-missing-layout>')
        with self.assertRaisesRegex(AssertionError, 'authored deck screen layout missing'):
            capstone.normalize_deck_accessibility(damaged)
