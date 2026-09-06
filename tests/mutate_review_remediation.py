"""Negative proofs for each second-review guard; inputs stay in memory/copies."""
import ast
import copy
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import test_review_remediation as review


def caught(label, callback, message):
    try:
        callback()
    except AssertionError as error:
        assert message in str(error), (label, str(error))
        print('CAUGHT '+label+': '+message, flush=True)
        return
    raise AssertionError('mutation escaped: '+label)


def premium_mutations():
    markup = (review.ui.SITE / 'options-trading/option-premium/index.html').read_text()
    legend = re.search(r'<div class="seg-row" aria-label="Premium components">.*?</div>', markup)[0]
    cases = [
        ('removed legend', markup.replace(legend, ''), 'persistent premium legend'),
        ('label moved inside narrow bar', markup.replace(legend, '').replace('id="premiumIntrinsicBar" style="width:0%">', 'id="premiumIntrinsicBar" style="width:0%">'+legend), 'premium labels independent'),
        ('nondecorative bars', markup.replace('class="value-stack" aria-hidden="true"', 'class="value-stack"'), 'premium bars are decorative'),
        ('runtime label overwrite', markup.replace('function renderPremium(){', 'function renderPremium(){\n document.querySelector(\'[aria-label="Premium components"]\').children[0].textContent="";'), 'premium runtime label persistence'),
        ('runtime ancestor overwrite', markup.replace('function renderPremium(){', 'function renderPremium(){\n document.querySelector(\'[aria-label="Premium components"]\').textContent="Intrinsic / Extrinsic";'), 'premium runtime label persistence'),
        ('hidden legend', markup.replace('aria-label="Premium components"', 'aria-label="Premium components" hidden'), 'premium labels persist visibly'),
        ('numeric update omitted', markup.replace("setText('premiumIntrinsic',money(m.intrinsic));", ''), 'premium runtime label persistence'),
    ]
    review.check_premium(unittest.TestCase(), markup)
    for label, broken, expected in cases:
        assert broken != markup, 'mutation anchor missing: '+label
        caught(label, lambda: review.check_premium(unittest.TestCase(), broken), expected)
    return len(cases)


def main():
    count = premium_mutations()
    if '--premium-only' not in sys.argv:
        review.TestCatalogOrderGuard().test_reordered_mislabelled_or_misdirected_cards_fail()
        print('CAUGHT 3 catalog mutations: reordered cards, wrong title, wrong destination', flush=True)
        count += 3
        contract = json.loads(review.CONTRACT.read_text())
        assert not review.content_errors(review.ui.ROOT, contract), 'run GREEN before mutations'
        for module in contract['modules']:
            missing = copy.deepcopy(contract); del missing['modules'][module]
            assert any('content inventory omission' in e for e in review.content_errors(review.ui.ROOT, missing)), module
            # Remove an actual approved clause from each source module in
            # memory; neither the contract nor the published worktree changes.
            original_read = Path.read_text
            target = review.ui.ROOT / module
            tree = ast.parse(target.read_text())
            clause = contract['modules'][module]['clauses'][0]
            nodes = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and n.value == clause]
            assert nodes, 'content mutation anchor missing: '+module
            nodes[0].value = 'Generic summary with the domain explanation removed.'
            broken = ast.unparse(tree)
            with mock.patch.object(Path, 'read_text', lambda p, *a, **kw: broken if p == target else original_read(p, *a, **kw)):
                errors = review.content_errors(review.ui.ROOT, contract)
            assert any(module+': substantive content' in e for e in errors), module
            assert any(module+': missing approved clause' in e for e in errors), module
            print('CAUGHT content omission and semantic change: '+module, flush=True)
            count += 2
        for phrase in ('Stage 1 of 4', 'START HERE', 'After the eight courses', 'Educational path', 'Open a path', 'last thing this path asks'):
            for shell in ('<p>{}</p>', '<svg aria-label="{}"></svg>', '<noscript>{}</noscript>'):
                assert review.progression_matches(shell.format(phrase)), phrase
                count += 1
            print('CAUGHT visible/accessibility/fallback taxonomy: '+phrase, flush=True)
        assert review.progression_matches('<span id="name" hidden>Open a path</span><svg aria-labelledby="name"></svg>')
        count += 1
        # A late :is override must reach the existing real published math guard.
        from mutate_course_ui import run, page_mutation, replace, output
        run('planning source owner', review.TestReviewRemediation('test_planning_copy_is_course_specific_and_source_owned'),
            output(review.ui.trading, 'normalize_course_ui', replace(
                'The Options Trade Plan lesson documents an options trade plan.',
                'The specification lesson documents a trading system.')), expected='planning source owner')
        count += 1
        with tempfile.TemporaryDirectory(prefix='learn-functional-mutation-') as tmp:
            site = Path(tmp); relative = 'algebra-foundations/absolute-value/index.html'
            target = site / relative; target.parent.mkdir(parents=True)
            target.write_text((review.ui.SITE / relative).read_text())
            with mock.patch.object(review.ui, 'SITE', site):
                run('functional math override', review.responsive.TestResponsiveUI('test_inline_math_wraps_and_blocks_scroll'),
                    page_mutation(site, relative, replace('</head>', '<style>:is(.math, .absent) { white-space: nowrap !important; }</style></head>')),
                    expected='inline math must wrap')
                count += 1
        with tempfile.TemporaryDirectory(prefix='learn-hero-mutation-') as tmp:
            site = Path(tmp); relative = 'market-structure/index.html'
            target = site / relative; target.parent.mkdir(parents=True)
            target.write_text((review.ui.SITE / relative).read_text())
            with mock.patch.object(review.ui, 'SITE', site):
                run('highlighted curriculum endpoint', review.TestReviewRemediation('test_topic_illustrations_have_no_highlighted_curricular_endpoint'),
                    page_mutation(site, relative, replace('class="hero-svg" data-illustration="topics"', 'class="hero-svg sv-tile-live" data-illustration="topics"')),
                    expected='no highlighted curricular endpoint')
                count += 1
        # Shared inventory fixtures reject dropping input kinds and losing label ownership.
        source = Path(__file__).with_name('interactive_targets.js').read_text()
        for old, new in [('input:not([type="hidden"])', 'input[type="button"]'),
                         ("new Set(['checkbox', 'radio', 'file'])", "new Set()")]:
            assert old in source
            with tempfile.TemporaryDirectory(prefix='learn-inventory-mutation-') as tmp:
                target = Path(tmp) / 'targets.js'; target.write_text(source.replace(old, new, 1))
                p = subprocess.run(['node', str(target), '--test'], capture_output=True, text=True)
                assert p.returncode == 1 and 'AssertionError' in p.stderr, 'inventory mutation escaped'
            count += 1
            print('CAUGHT interactive inventory: '+old, flush=True)
    print(f'{count}/{count} review mutations caught; worktree inputs untouched.')


if __name__ == '__main__':
    main()
