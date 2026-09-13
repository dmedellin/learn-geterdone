"""Second review: domain preservation and the complete visitor text boundary.

These source/semantic checks do not establish browser geometry. The content
contract covers every generated module, including modules needing no repair.
"""
import ast
import hashlib
import inspect
import json
import re
import subprocess
import unittest
from types import SimpleNamespace
from unittest import mock
from html.parser import HTMLParser
from pathlib import Path

import test_course_ui as ui
import test_responsive_ui as responsive

CONTRACT = Path(__file__).with_name('content_preservation.json')
AST_DUMP_OPTIONS = {'include_attributes': False}
if 'show_empty' in inspect.signature(ast.dump).parameters:
    AST_DUMP_OPTIONS['show_empty'] = True


def content_fingerprint(source):
    # Python 3.13+ can omit empty fields; 3.11/3.12 always emitted them.
    return hashlib.sha256(ast.dump(ast.parse(source), **AST_DUMP_OPTIONS).encode()).hexdigest()


def content_errors(root, contract):
    expected = contract['modules']
    # Cover all source modules, a superset of changed modules; no Git-history or
    # shallow-checkout dependency can silently switch off omission detection.
    actual = {p.relative_to(root).as_posix()
              for subject in ui.build_paths.GENERATED_PATHS
              for p in (root / 'content' / subject['slug'].replace('-', '_')).rglob('*.py')}
    errors = []
    if actual != set(expected):
        errors.append('content inventory omission: ' + repr(sorted(actual ^ set(expected))))
    for name in sorted(actual & set(expected)):
        source = (root / name).read_text()
        tree = ast.parse(source)
        digest = content_fingerprint(source)
        if digest != expected[name]['expected_ast_sha256']:
            errors.append(name + ': substantive content contract differs')
        strings = {n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)}
        for clause in expected[name]['clauses']:
            if clause not in strings:
                errors.append(name + ': missing approved clause: ' + clause)
    return errors


class VisitorText(HTMLParser):
    """Text and accessibility attributes, including no-script alternatives.

    Comments, script/style bodies, identifiers and URL attributes never enter
    the text stream. Hidden content is excluded; aria-hidden alone does not hide
    visually rendered text. Browser CSS-dependent visibility remains external.
    """
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.stack, self.text, self.accessible, self.references = [], [], [], []
        self.family = None
        self.feed(markup)
        if self.references:
            doc = ui.Elements(markup)
            for reference in self.references:
                for node in doc.find(id=reference):
                    self.accessible.append(ui.words(node))
                    self.accessible.append(node['attrs'].get('aria-label', ''))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'body':
            self.family = attrs.get('data-page-kind')
        hidden = (any(h for _, h in self.stack) or tag in ('script', 'style', 'template')
                  or 'hidden' in attrs or bool(re.search(r'(?:display\s*:\s*none|visibility\s*:\s*hidden)', attrs.get('style', ''))))
        self.text.append(' ')
        if not hidden:
            for name in ('aria-labelledby', 'aria-describedby'):
                self.references.extend(attrs.get(name, '').split())
            self.accessible.extend(attrs[k] for k in ('aria-label', 'aria-description', 'alt', 'title', 'placeholder') if attrs.get(k))
            if tag == 'meta' and attrs.get('name', attrs.get('property')) in ('description', 'og:title', 'og:description', 'twitter:title', 'twitter:description'):
                self.accessible.append(attrs.get('content', ''))
        if tag not in self.VOID:
            self.stack.append((tag, hidden))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        self.text.append(' ')

    def handle_data(self, data):
        if not any(hidden for _, hidden in self.stack):
            self.text.append(data)

    def copy(self):
        return ' '.join((''.join(self.text) + ' ' + ' '.join(self.accessible)).split())


PROGRESSION = {
    'stage badge': r'\bstage\s+\d+\s+of\s+\d+\b',
    'start label': r'\bstart here\b',
    'course prerequisite': r'\bafter the eight courses\b',
    'educational path': r'\beducational path\b',
    'open path': r'\bopen a path\b',
    'terminal curriculum': r'\blast thing this path asks\b',
    'curriculum illustration': r'\b(?:course stages|numbered (?:course )?waypoints|course stage tiles)\b|rising path from lesson|stages of the course|the end of the path',
    'public path identity': r'\b(?:trading|algebra|discrete mathematics|learning) path\b',
    'fallback taxonomy': r'\bthe path position\b|\bpaths, what each one holds\b|\bmethod this path teaches\b',
}


def progression_matches(markup):
    visitor = VisitorText(markup)
    copy = visitor.copy()
    # These two execution-workflow clauses are reviewed domain exceptions.
    copy = copy.replace('Keep the trading path explicit', '').replace('normal trading path is unreliable', '')
    patterns = dict(PROGRESSION)
    if visitor.family not in (None, 'library', 'subject'):
        # Naming a sibling Subject in teaching prose is the only thing telling a
        # reader the target is on another Subject at all, and it survives any
        # renumbering; tests/visitor_copy.py allows it everywhere except the
        # library and Subject pages, which name themselves. Generic framing --
        # 'learning path' -- stays forbidden on every family, and a fragment
        # with no page family is still held to the whole rule.
        patterns['public path identity'] = r'\blearning path\b'
    return [(name, m.group()) for name, pattern in patterns.items() for m in re.finditer(pattern, copy, re.I)]


class TestReviewRemediation(unittest.TestCase):
    def test_content_fingerprint_keeps_empty_fields_across_python_versions(self):
        self.assertEqual('abe172bc9dc58744d5ec90e963f971f5a7451d0387dc9f767a4f2ffcde5ef820',
                         content_fingerprint('items = []\nconsume()\n'),
                         'portable AST fingerprint must retain empty fields')

    def test_all_generated_content_is_preserved(self):
        contract = json.loads(CONTRACT.read_text())
        self.assertEqual(53, len(contract['modules']))
        errors = content_errors(ui.ROOT, contract)
        self.assertEqual([], errors, '\n'.join(errors))

    def test_complete_visitor_boundary_is_neutral(self):
        pages = sorted(ui.SITE.rglob('*.html'))
        self.assertEqual(369, len(pages), 'include capstones and no-script alternatives')
        failures = [(p.relative_to(ui.SITE).as_posix(), progression_matches(p.read_text())) for p in pages]
        self.assertEqual([], [(p, m) for p, m in failures if m], 'visitor progression/taxonomy')

    def test_planning_copy_is_course_specific_and_source_owned(self):
        courses = ui.trading.trading_inventory()
        for slug, sentence in (
            ('options-trading', 'The Options Trade Plan lesson documents an options trade plan.'),
            ('trading-risk-management', 'The Trading Risk Plan lesson documents a risk plan.')):
            course = next(c for c in courses if c['slug'] == slug)
            page = (ui.SITE / slug / 'index.html').read_text()
            self.assertIn(sentence, VisitorText(page).copy(), 'course-specific planning copy')
            # A fresh legacy sentence and the already-emitted bad sentence must
            # both be repaired by the owner, including its normalized fast path.
            for original in ('The last lesson is not a quiz you pass and close.',
                             'The specification lesson documents a trading system.'):
                repaired = ui.trading.normalize_course_ui(page.replace(sentence, original), course, courses, courses.index(course))
                self.assertIn(sentence, VisitorText(repaired).copy(), 'planning source owner must repair legacy and current copy')
                self.assertEqual(repaired, ui.trading.normalize_course_ui(repaired, course, courses, courses.index(course)))

    def test_topic_illustrations_have_no_highlighted_curricular_endpoint(self):
        for slug in ('market-structure', 'trade-setup-execution', 'options-trading', 'technical-indicators'):
            markup = (ui.SITE / slug / 'index.html').read_text()
            hero = ui.trading.element(markup, 'section', cls='hero')
            doc = ui.Elements(markup[hero['start']:hero['end']])
            svg = doc.find('svg')[0]
            self.assertEqual('topics', svg['attrs'].get('data-illustration'), slug+': neutral topic illustration')
            self.assertNotRegex(ui.words(svg), r'\b(?:0[1-7]|START HERE)\b', 'hero topics must not encode a numbered route')
            self.assertFalse(any('sv-tile-live' in n['attrs'].get('class', '').split() for n in doc.nodes), 'no highlighted curricular endpoint')

    def test_legacy_hero_normalization_preserves_domain_and_is_neutral(self):
        courses = ui.trading.trading_inventory()
        fixtures = json.loads(Path(__file__).with_name('legacy_course_heroes.json').read_text())['drawings']
        self.assertEqual({c['slug'] for c in courses}, set(fixtures), 'legacy fixture coverage')
        for index, course in enumerate(courses):
            path = course['slug']+'/index.html'
            fixture = fixtures[course['slug']]
            self.assertEqual(fixture['sha256'], hashlib.sha256(fixture['svg'].encode()).hexdigest(), 'immutable fixture bytes')
            current = (ui.SITE / path).read_text()
            baseline = ui.trading.replace_element(current, ui.trading.element(current, 'svg', cls='hero-svg'), fixture['svg'])
            normalized = ui.trading.normalize_course_ui(baseline, course, courses, index)
            normalized = ui.trading.normalize_taxonomy_copy(normalized, courses)
            self.assertEqual([], progression_matches(normalized), course['slug']+': legacy hero normalization')
            repeated = ui.trading.normalize_course_ui(normalized, course, courses, index)
            self.assertEqual(normalized, ui.trading.normalize_taxonomy_copy(repeated, courses), 'legacy source ownership/idempotence')

    def test_domain_exceptions_and_text_boundaries(self):
        allowed = 'Graph paths, shortest paths, filesystem paths, URL paths, execution paths, price paths, Monte Carlo paths, algorithmic steps, algebraic steps. Lessons 01–05. Previous Lesson 01. Next Lesson 03.'
        self.assertEqual([], progression_matches('<p>' + allowed + '</p>'))
        self.assertEqual([], progression_matches('<script>"Open a path"</script><style>/* START HERE */</style><!-- Stage 1 of 4 --><i class="path" data-path="trading"></i>'))
        for phrase in ('Stage <b>1 of 4</b>', 'START HERE', 'After the eight courses', 'Educational path', 'Open a path', 'last thing this path asks'):
            self.assertTrue(progression_matches('<p>' + phrase + '</p>'), phrase)
            self.assertTrue(progression_matches('<svg aria-label="' + re.sub('<[^>]+>', '', phrase) + '"></svg>'), phrase)
        self.assertTrue(progression_matches('<noscript>Open a path</noscript>'))
        self.assertTrue(progression_matches('<span id="name" hidden>Open a path</span><svg aria-labelledby="name"></svg>'), 'hidden referenced accessible name')
        # A sibling Subject named in teaching prose is allowed off the pages
        # that name themselves; generic framing is forbidden on all of them.
        prose = '<body data-page-kind="%s"><p>Induction is on the Discrete Mathematics path.</p></body>'
        for kind in ('course', 'lesson'):
            self.assertEqual([], progression_matches(prose % kind), kind)
        for kind in ('library', 'subject'):
            self.assertEqual([('public path identity', 'Discrete Mathematics path')],
                             progression_matches(prose % kind), kind)
        for kind in ('course', 'lesson', 'library', 'subject'):
            self.assertTrue(progression_matches('<body data-page-kind="%s"><p>Follow the learning path.</p></body>' % kind), kind)


class TestFunctionalSelectors(unittest.TestCase):
    def test_functional_matching_and_specificity(self):
        doc = ui.Elements('<main class="parent"><span id="value" class="math"></span></main>')
        chain = responsive.ancestry(doc, doc.find('span')[0])
        cases = [
            (':is(.math) {white-space:nowrap!important}', 'nowrap'),
            (':is(.absent, .parent > .math) {white-space:nowrap}', 'nowrap'),
            (':not(:is(.absent, .other)) {white-space:nowrap}', 'nowrap'),
            (':where(#value) {white-space:nowrap} .math {white-space:normal}', 'normal'),
            (':is(.math, #absent) {white-space:nowrap} .math {white-space:normal}', 'nowrap'),
            (':not(:hover) {white-space:nowrap} .math {white-space:normal}', 'normal'),
        ]
        for css, expected in cases:
            with self.subTest(css=css):
                self.assertEqual(expected, responsive.effective(css, chain, 320).get('white-space'), 'functional selector cascade')


class TestCatalogOrderGuard(unittest.TestCase):
    A = '<a data-course="alpha" href="../../alpha/"><strong>Alpha</strong></a>'
    B = '<a data-course="beta" href="../../beta/"><strong>Beta</strong></a>'

    def check_catalog(self, intro, cards):
        import test_site_invariants as invariants
        markup = '<p>'+intro+'</p><section data-ui="course-list">'+cards+'</section>'
        paths = [('Example', '/paths/example/', [('Alpha', '/alpha/', []), ('Beta', '/beta/', [])], 2, [])]
        case = invariants.TestPathPage()
        with mock.patch.object(invariants, 'PATHS', paths), mock.patch.object(case, 'path_document', return_value=SimpleNamespace(text=markup)):
            case.test_subject_catalog_preserves_authored_display_order()

    def test_overview_mentions_do_not_define_catalog_order(self):
        self.check_catalog('Beta uses the definitions in Alpha.', self.A+self.B)

    def test_reordered_mislabelled_or_misdirected_cards_fail(self):
        for cards in (self.B+self.A, self.A+self.B.replace('>Beta<', '>Other<'),
                      self.A+self.B.replace('../../beta/', '../../alpha/')):
            with self.assertRaisesRegex(AssertionError, 'catalog'):
                self.check_catalog('Alpha Beta', cards)


def check_premium(case, markup):
    doc = ui.Elements(markup)
    legends = doc.find(**{'aria-label': 'Premium components'})
    case.assertEqual(1, len(legends), 'persistent premium legend')
    legend = legends[0]
    labels = [n for n in legend['children'] if 'legend-item' in n['attrs'].get('class', '').split()]
    case.assertEqual(['Intrinsic', 'Extrinsic'], [ui.words(n) for n in labels], 'persistent premium labels')
    for label in labels:
        chain = responsive.ancestry(doc, label)
        case.assertFalse(any(dict(a).get('id') in ('premiumIntrinsicBar', 'premiumExtrinsicBar', 'premiumIntrinsic', 'premiumExtrinsic') for _, a in chain), 'premium labels independent of dynamic bars and values')
        for tag, items in chain:
            attrs = dict(items)
            case.assertNotIn(attrs.get('id'), ('premiumIntrinsicBar', 'premiumExtrinsicBar', 'premiumIntrinsic', 'premiumExtrinsic'), 'premium labels independent of dynamic bars and values')
            case.assertNotIn('hidden', attrs, 'premium labels persist visibly')
            case.assertNotEqual('true', attrs.get('aria-hidden'), 'premium labels accessible')
        for width in (320, 390, 768, 1024, 1440):
            for depth in range(1, len(chain)+1):
                style = responsive.effective(responsive.stylesheet(markup), chain[:depth], width)
                case.assertNotEqual('none', style.get('display'), 'premium labels persist visibly')
                case.assertNotIn(style.get('visibility'), ('hidden', 'collapse'), 'premium labels persist visibly')
    for component in ('Intrinsic', 'Extrinsic'):
        bar = doc.find(id='premium'+component+'Bar')[0]
        case.assertEqual('', ui.words(bar), 'premium bars are decorative')
        case.assertTrue(any(dict(a).get('aria-hidden') == 'true' for _, a in responsive.ancestry(doc, bar)), 'premium bars are decorative')
        value = doc.find(id='premium'+component)[0]
        case.assertNotIn(legend, value['children'], 'separate premium numeric values')
    function = re.search(r'function renderPremium\(\)\{.*?\n\}', markup, re.S)
    case.assertIsNotNone(function, 'execute the shipped premium UI function')
    result = subprocess.run(['node', str(Path(__file__).with_name('premium_labels.js'))],
                            input=json.dumps({'root': doc.find('body')[0], 'function': function[0]}),
                            text=True, capture_output=True)
    case.assertEqual(0, result.returncode, 'premium runtime label persistence: '+result.stderr)


class TestPremiumLabels(unittest.TestCase):
    def test_persistent_labels_and_separate_updates(self):
        check_premium(self, (ui.SITE / 'options-trading/option-premium/index.html').read_text())


def native_name(doc, node):
    attrs = node['attrs']
    if attrs.get('aria-labelledby'):
        names = [ui.words(n) for identity in attrs['aria-labelledby'].split() for n in doc.find(id=identity)]
        if any(names):
            return ' '.join(names).strip()
    if attrs.get('aria-label', '').strip():
        return attrs['aria-label'].strip()
    labels = doc.find('label', **{'for': attrs['id']}) if attrs.get('id') else []
    responsive.ancestry(doc, node)
    parent = doc.parents.get(id(node))
    while parent:
        if parent['tag'] == 'label':
            labels.append(parent)
        parent = doc.parents.get(id(parent))
    return ' '.join(ui.words(n) for n in labels).strip()


class TestInteractiveInventory(unittest.TestCase):
    def test_empty_and_dangling_names_are_rejected(self):
        for markup in ('<label><input type="checkbox"></label>', '<input aria-labelledby="missing">',
                       '<label for="value"></label><input id="value">'):
            doc = ui.Elements(markup)
            self.assertFalse(native_name(doc, doc.find('input')[0]), 'empty or dangling input name')
        doc = ui.Elements('<span id="name" hidden>Show edges</span><input type="checkbox" aria-labelledby="name">')
        self.assertEqual('Show edges', native_name(doc, doc.find('input')[0]))

    def test_browser_inventory_contract(self):
        owner = Path(__file__).with_name('interactive_targets.js')
        self.assertTrue(owner.exists(), 'complete interactive target inventory owner is required')
        result = subprocess.run(['node', str(owner), '--test'], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, 'interactive target owners: '+result.stderr)
        self.assertIn('inventory ownership fixtures passed', result.stdout)

    def test_native_input_inventory_has_names_and_label_owners(self):
        kinds, wrapped = {}, 0
        for page in sorted(ui.SITE.rglob('*.html')):
            doc = ui.Elements(page.read_text())
            for node in doc.find('input') + doc.find('textarea') + doc.find('select'):
                attrs = node['attrs']; kind = attrs.get('type', 'text') if node['tag'] == 'input' else node['tag']
                if kind == 'hidden': continue
                kinds[kind] = kinds.get(kind, 0) + 1
                chain = responsive.ancestry(doc, node)
                wrap = any(tag == 'label' for tag, _ in chain[:-1])
                wrapped += wrap
                self.assertTrue(native_name(doc, node),
                                str(page.relative_to(ui.SITE)) + ': native input must expose a named target')
        for kind in ('range', 'number', 'text', 'checkbox', 'search', 'file', 'date', 'textarea', 'select'):
            self.assertGreater(kinds.get(kind, 0), 0, 'inventory must include '+kind)
        self.assertGreater(wrapped, 40, 'label-wrapped targets must be inventoried')


if __name__ == '__main__':
    unittest.main()
