"""Visitor-boundary regressions independent of the generator's implementation."""
import os
import json
import re
from pathlib import Path
import tempfile
import unittest

import visitor_copy as copy


SITE = Path(os.environ.get('SITE_ROOT') or Path(__file__).resolve().parents[1] / 'site')


def algebra_semantic_errors(site, contract):
    """Check complete authored clauses as blocks, including their qualifications.

    The fixture carries baseline-derived copy; no Git object is needed. Exact
    block comparison rejects an inverted prerequisite even when it contains the
    original words. Browser visibility remains a separate acceptance check.
    """
    import test_course_ui as ui
    errors = []
    for slug, course in contract['algebra_semantic_copy']['courses'].items():
        file = site / slug / 'index.html'
        if not file.is_file():
            errors.append(slug + ': missing Course home')
            continue
        doc = ui.Elements(file.read_text())
        children = {id(c) for n in doc.nodes for c in n['children']}
        blocks = set()

        def visit(node, hidden=False):
            attrs = node['attrs']
            hidden = hidden or node['tag'] in ('script', 'style', 'template', 'noscript') or 'hidden' in attrs or bool(
                re.search(r'(?:display\s*:\s*none|visibility\s*:\s*hidden)', attrs.get('style', '')))
            if not hidden:
                blocks.add((node['tag'], ui.words(node)))
            for child in node['children']:
                visit(child, hidden)

        for node in doc.nodes:
            if id(node) not in children:
                visit(node)
        for clause in course['clauses']:
            if (clause['tag'], clause['expected']) not in blocks:
                errors.append(slug + ': missing or altered ' + clause['field'] + ': ' + clause['expected'])
    return errors


class TestPublicCopy(unittest.TestCase):
    def test_shared_surface_inventory_has_no_ordinal_references(self):
        pages, records = copy.scan(SITE)
        owners = {route for route, page in pages.items()
                  if page.family in ('library', 'subject')}
        self.assertEqual(sum(page.family == 'library' for page in pages.values()), 1)
        self.assertEqual(sum(page.family == 'subject' for page in pages.values()), 3)
        records = [r for r in records if r['route'] in owners]
        self.assertGreater(len(records), 100, 'shared visitor sweep cannot be empty')
        self.assertFalse([f for r in records for f in copy.findings(r)],
                         'shared library/Subject copy must use titles and topic relationships')

    def test_indirect_curricular_reference_mutations(self):
        for text in (
                'The smoothing every later tool is built on.',
                'Five positions assembled from the parts above, one lesson each.'):
            with self.subTest(text=text):
                doc = copy.Document('<body data-page-kind="course"><p>' + text + '</p></body>')
                self.assertIn('implicit-curricular-order',
                              [f['rule'] for r in doc.records for f in copy.findings(r)])
        for text in ('Pricing topics above a long-call payoff diagram.',
                     'Factor out the common term before applying another factoring method.'):
            doc = copy.Document('<body data-page-kind="course"><p>' + text + '</p></body>')
            self.assertFalse([f for r in doc.records for f in copy.findings(r)])

    def test_shared_surface_gate_mutations_on_owned_copies(self):
        from unittest import mock
        owners = []
        for file in SITE.rglob('*.html'):
            if copy.Document(file.read_text()).family in ('library', 'subject'):
                owners.append(file.relative_to(SITE))
        self.assertEqual(len(owners), 4, 'shared mutation sweep must cover all owners')
        with tempfile.TemporaryDirectory(prefix='shared-copy-', dir='/tmp') as tmp:
            site = Path(tmp)
            for relative in owners:
                target = site / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((SITE / relative).read_bytes())
            with mock.patch(__name__ + '.SITE', site):
                self.test_shared_surface_inventory_has_no_ordinal_references()
                for relative in owners:
                    with self.subTest(owner=str(relative)):
                        file = site / relative
                        original = file.read_bytes()
                        self.assertIn(b'</main>', original)
                        try:
                            file.write_bytes(original.replace(b'</main>', b'<p>Start here: the next lesson is Lesson 2.</p></main>', 1))
                            with self.assertRaisesRegex(AssertionError, 'shared library/Subject copy'):
                                self.test_shared_surface_inventory_has_no_ordinal_references()
                        finally:
                            file.write_bytes(original)
                        self.assertEqual(file.read_bytes(), original)
                        self.test_shared_surface_inventory_has_no_ordinal_references()

    def test_generated_lab_dynamic_strings_use_titles(self):
        import test_course_ui as ui
        routes = {'/' + relative.removesuffix('index.html') for relative, _html in ui.build_paths.pages()}
        self.assertGreater(len(routes), 200, 'generated owner inventory must not be empty')
        subject = os.environ.get('AB_SUBJECT')
        if subject:
            owners = [p for p in ui.build_paths.GENERATED_PATHS if p['slug'] == subject]
            self.assertEqual(len(owners), 1, 'focused subject must have a generated owner')
            prefixes = tuple('/' + c['slug'] + '/' for c in owners[0]['courses'])
            routes = {r for r in routes if r.startswith(prefixes)}
            self.assertGreater(len(routes), len(prefixes), 'subject must include Lessons')
        focus = os.environ.get('AB_COURSE')
        if focus:
            self.assertIn('/' + focus + '/', routes)
            routes = {r for r in routes if r.startswith('/' + focus + '/')}
            self.assertGreater(len(routes), 1, 'Course must include Lessons')
        _pages, records = copy.scan(SITE)
        records = [r for r in records if r['route'] in routes and r['boundary'] == 'dynamic-string']
        self.assertGreater(len(records), 1000)
        failures = [f for r in records for f in copy.findings(r)]
        self.assertFalse(failures, 'generated lab dynamic copy must use titles:\n' + '\n'.join(
            r['route'] + ': ' + r['text'] for r in failures[:30]))

    def test_rendered_inventory_has_no_ordinal_references(self):
        pages, records = copy.scan(SITE)
        self.assertEqual(369, len(pages), 'visitor inventory must include every family')
        self.assertEqual(25, sum(p.family == 'course' for p in pages.values()))
        self.assertEqual(336, sum(p.family == 'lesson' for p in pages.values()))
        self.assertGreater(len(records), 45000)
        focus = os.environ.get('AB_COURSE')
        if focus:
            self.assertIn('/' + focus + '/', pages)
            records = [r for r in records if r['route'].startswith('/' + focus + '/')]
            self.assertGreater(len(records), 100)
        boundary = os.environ.get('AB_BOUNDARY')
        if boundary:
            records = [r for r in records if r['boundary'] == boundary]
            self.assertGreater(len(records), 10, 'a focused boundary cannot cover nothing')
        failures = [f for r in records for f in copy.findings(r)]
        self.assertFalse(failures, 'public ordinal/navigation copy:\n' + '\n'.join(
            f"{r['route']} {r['boundary']}: {r['text']}" for r in failures[:30]))

    def test_boundary_mutations_are_detected_in_every_page_family(self):
        payloads = {
            'range prose': '<p>Lessons 1 to 3 establish the model (01–03).</p>',
            'dependency': '<p>The next lesson uses the result of lesson 6.</p>',
            'capstone': '<h2>Lesson 16 exports a risk plan</h2>',
            'aria': '<svg aria-label="Lessons 01 to 03 show conditioning"></svg>',
            'quiz feedback': '<button data-why="Lesson 6 explains the risk">Answer</button>',
            'title': '<button title="Next lesson">Open</button>',
            'alt': '<img alt="Lesson 2">',
            'value': '<input value="Lesson 3">',
            'placeholder': '<input placeholder="Lesson 4">',
            'metadata': '<meta name="description" content="Lessons 1 to 3">',
            'social': '<meta property="og:description" content="Course 2">',
            'twitter': '<meta name="twitter:description" content="Lesson 4">',
            'dynamic': '<script>output.textContent="Lesson 6";</script>',
            'dynamic interpolation': '<script>output.textContent=`Lesson ${number}`;</script>',
            'dynamic concatenation': '<script>output.textContent="Lesson " + number;</script>',
            'search': '<script>const SEARCH=[{description:"Course 3 uses lesson 2"}];</script>',
            'structured': '<script type="application/ld+json">{"description":"Lesson 6"}</script>',
            'vocabulary': '<nav>Open a path. START HERE. Course progression.</nav>',
            **{word: '<nav>' + word + '</nav>' for word in ('Path', 'Track', 'Module', 'Progression', 'Stage')},
            'noscript': '<noscript><p>The final lesson exports a plan.</p></noscript>',
        }
        for family in ('library', 'subject', 'course', 'lesson', 'progress', 'auth', 'supplemental', 'slides'):
            for label, payload in payloads.items():
                with self.subTest(family=family, boundary=label):
                    doc = copy.Document(f'<body data-page-kind="{family}">{payload}</body>')
                    self.assertTrue([f for r in doc.records for f in copy.findings(r)], label)

    def test_numbered_link_mutations_use_destination_capabilities(self):
        with tempfile.TemporaryDirectory(prefix='copy-mutation-', dir='/tmp') as tmp:
            site = Path(tmp)
            (site / 'arbitrary').mkdir()
            (site / 'arbitrary' / 'index.html').write_text('<body data-page-kind="lesson"><h1>Literal title</h1></body>')
            for family in ('syllabus-item', 'lesson-link', 'file-link'):
                for prefix in ('01 ', 'Lesson 02 · '):
                    (site / 'index.html').write_text(f'<body data-page-kind="course"><a class="{family}" href="./arbitrary/">{prefix}Literal title</a></body>')
                    _pages, records = copy.scan(site)
                    self.assertIn('numbered-link', [f['rule'] for r in records for f in copy.findings(r)])
            (site / 'index.html').write_text('<body data-page-kind="course"><a href="./arbitrary/">Literal title</a></body>')
            _pages, records = copy.scan(site)
            self.assertFalse([f for r in records for f in copy.findings(r)])

    def test_legitimate_instructional_numbers_are_not_catalog_ordinals(self):
        controls = (
            'A graph path visits adjacent vertices; the shortest path has minimum weight.',
            'Arithmetic and geometric sequences have different rules.',
            'At each algorithmic stage, compare the current node with its neighbours.',
            'This Course contains 14 lessons.',
            'There are 25 Courses in three Subjects.',
            'The expression (3 − 1) equals 2.',
            'The expression (3 - 1) = 2.',
            'Take each edge in order if it joins two components',
            'Read the pair in order',
            'The Conditional Probability Lesson uses a restricted sample space.',
        )
        for text in controls:
            with self.subTest(text=text):
                doc = copy.Document('<body data-page-kind="lesson"><p>' + text + '</p></body>')
                self.assertFalse([f for r in doc.records for f in copy.findings(r)])
                mutant = copy.Document('<body data-page-kind="lesson"><p>' + text + ' The next lesson uses Lesson 6.</p></body>')
                self.assertTrue([f for r in mutant.records for f in copy.findings(r)], 'domain language cannot excuse ordinal dependencies')

    def test_implicit_order_mutations_and_domain_controls(self):
        payloads = (
            'The first half of this course concerns fractions.',
            'Every technique in the first half requires factoring.',
            'Complex numbers are defined later in the course.',
            'After this lesson, these answers are available.',
            'Every radical from here on uses this notation.',
            'Every later solution set uses intervals.',
            'Every method later on produces these lines.',
            'Every notation you meet later relies on this.',
            'Nothing so far defines a fractional exponent.',
            'Among the formulas available so far, roots restrict the domain.',
            'The named Course later supplies the equation method.',
            'The formula for computing one entry comes next.',
        )
        controls = {
            'The second half of the definition requires a positive root.':
                'Two clauses in a mathematical definition, not Course order.',
            'The second half of a row is the first half reversed.':
                "Pascal triangle symmetry describes array entries.",
            'Each earlier number system was extended to solve an equation.':
                'Mathematical number-system extensions, not curricular order.',
            'An earlier arithmetic step was wrong; check the original equation.':
                'A procedural verification rule for one calculation.',
            'The first term and every later term equal zero.':
                'Indices of a mathematical sequence, not Lessons.',
        }
        with tempfile.TemporaryDirectory(prefix='algebra-copy-controls-', dir='/tmp') as tmp:
            root = Path(tmp)
            file = root / 'index.html'
            for family in ('library', 'subject', 'course', 'lesson', 'progress', 'auth', 'supplemental', 'slides'):
                for text in payloads:
                    with self.subTest(family=family, text=text):
                        file.write_text(f'<body data-page-kind="{family}"><p>{text}</p></body>')
                        pages, records = copy.scan(root)
                        self.assertEqual(len(pages), 1)
                        self.assertIn('implicit-curricular-order', [f['rule'] for r in records for f in copy.findings(r)])
            for text, reason in controls.items():
                with self.subTest(domain_reason=reason):
                    file.write_text(f'<body data-page-kind="lesson"><p>{text}</p></body>')
                    _, records = copy.scan(root)
                    self.assertFalse([f for r in records for f in copy.findings(r)])

    def test_named_course_order_uses_rendered_titles(self):
        with tempfile.TemporaryDirectory(prefix='named-copy-controls-', dir='/tmp') as tmp:
            root = Path(tmp)
            owner = root / 'arbitrary-owner'
            owner.mkdir()
            (owner / 'index.html').write_text('<body data-page-kind="course"><h1>Vector Methods</h1></body>')
            file = root / 'index.html'
            for verb in ('began', 'begins', 'started', 'starts', 'ended', 'ends'):
                file.write_text(f'<body data-page-kind="lesson"><p>Vector Methods {verb} with elimination.</p></body>')
                _, records = copy.scan(root)
                self.assertIn('named-course-sequencing', [f['rule'] for r in records for f in copy.findings(r)])
            file.write_text('<body data-page-kind="lesson"><p>The sequence starts with zero. Vector Methods explains elimination.</p></body>')
            _, records = copy.scan(root)
            self.assertFalse([f for r in records for f in copy.findings(r)], 'sequence terms are mathematical objects; a named explanation is a topic relationship')


class TestAlgebraSemanticCopy(unittest.TestCase):
    def contract(self):
        return json.loads(Path(__file__).with_name('content_preservation.json').read_text())

    def test_baseline_clauses_survive_in_all_algebra_course_homes(self):
        import test_course_ui as ui
        contract = self.contract()
        self.assertEqual(contract['base'], '57788539d7463f4c5cd640e2571f3c40a9630750')
        owner = next(p for p in ui.build_paths.GENERATED_PATHS if p['slug'] == 'algebra')
        courses = contract['algebra_semantic_copy']['courses']
        self.assertEqual(set(courses), {c['slug'] for c in owner['courses']})
        self.assertEqual(len(courses), 9)
        for slug, course in courses.items():
            fields = {c['field'] for c in course['clauses']}
            self.assertTrue({'title', 'blurb', 'assumes_long', 'syllabus_intro', 'footer_lead'} <= fields, slug)
            self.assertGreater(sum(f.startswith('not_covered.') for f in fields), 1, slug)
            self.assertGreater(sum(f.startswith('how_to.') for f in fields), 1, slug)
        self.assertEqual([], algebra_semantic_errors(SITE, contract))

    def test_semantic_mutations_on_owned_course_copies(self):
        import shutil
        import test_course_ui as ui
        contract = self.contract()
        count = 0
        with tempfile.TemporaryDirectory(prefix='algebra-semantic-mutation-', dir='/tmp') as tmp:
            site = Path(tmp)
            for slug, course in contract['algebra_semantic_copy']['courses'].items():
                (site / slug).mkdir()
                shutil.copyfile(SITE / slug / 'index.html', site / slug / 'index.html')
            self.assertEqual([], algebra_semantic_errors(site, contract), 'unmodified owned copy must pass before mutations')
            for slug, course in contract['algebra_semantic_copy']['courses'].items():
                file = site / slug / 'index.html'
                original = file.read_text()
                targets = {c['field']: c for c in course['clauses']}
                cases = [('generic substitution', 'blurb'), ('dropped prerequisite', 'assumes_long'),
                         ('inverted prerequisite', 'assumes_long'), ('missing exclusion', 'not_covered.0'),
                         ('deleted rationale', course['rationale_field']), ('hidden prerequisite', 'assumes_long')]
                for label, field in cases:
                    with self.subTest(course=slug, mutation=label):
                        matches = [m for m in re.finditer(r'<p\b[^>]*>.*?</p>', original, re.S)
                                   if ui.words(ui.Elements(m[0]).find('p')[0]) == targets[field]['expected']]
                        self.assertEqual(len(matches), 1, 'owned mutation must find one real paragraph: ' + field)
                        match = matches[0]
                        if label == 'generic substitution':
                            replacement = '<p>Explore useful ideas and practise your skills.</p>'
                        elif label == 'inverted prerequisite':
                            replacement = '<p>No knowledge of ' + targets[field]['expected'] + ' is needed.</p>'
                        elif label == 'deleted rationale':
                            reason = course['rationale_text']
                            self.assertIn(reason, match[0], 'rationale anchor must be real source text')
                            replacement = match[0].replace(reason, '')
                        elif label == 'hidden prerequisite':
                            replacement = '<div hidden>' + match[0] + '</div>'
                        else:
                            replacement = ''
                        file.write_text(original[:match.start()] + replacement + original[match.end():])
                        errors = algebra_semantic_errors(site, contract)
                        self.assertTrue(any(e.startswith(slug + ': missing or altered ' + field + ':') for e in errors), errors)
                        file.write_text(original)
                        self.assertEqual([], algebra_semantic_errors(site, contract), 'restore must recover the same contract')
                        count += 1
        self.assertEqual(count, 54, 'five semantic families and a hidden-clause mutation on every Algebra Course')


def discrete_semantic_errors(site, contract):
    """Apply the same complete-block check to the baseline-derived A/B3 scope."""
    return algebra_semantic_errors(site, {
        'algebra_semantic_copy': contract['discrete_semantic_copy'],
    })


def authored_semantic_errors(site, contract, only=None):
    semantic = contract['authored_semantic_copy']
    pages = semantic['pages']
    if only is not None:
        pages = {key: pages[key] for key in only}
    errors = algebra_semantic_errors(site, {'algebra_semantic_copy': {'courses': pages}})
    for key, page in pages.items():
        file = site / key / 'index.html'
        if not file.is_file():
            continue
        doc = copy.Document(file.read_text())
        records = {(r['boundary'], r['text']) for r in doc.records}
        if any(r['boundary'] == 'dynamic-template-source' for r in page['source_records']):
            # Compare the complete nested template, including its expressions.
            # The historical regex record included JavaScript after its end.
            import subprocess
            templates = subprocess.run(
                ['node', str(Path(__file__).with_name('javascript_templates.js'))],
                input=file.read_text(), text=True, capture_output=True, check=True)
            records.update(('dynamic-template-source', copy.words(r['text']))
                           for r in json.loads(templates.stdout))
        for record in page['source_records']:
            if (record['boundary'], record['text']) not in records:
                errors.append(key + ': missing or altered ' + record['boundary'] + ': ' + record['text'])
    if only is None:
        for relative, expected in semantic['assets'].items():
            file = site / relative
            if not file.is_file() or json.loads(file.read_text()) != expected:
                errors.append(relative + ': altered published JSON contract')
    return errors


class TestAuthoredSemanticCopy(unittest.TestCase):
    def contract(self):
        return json.loads(Path(__file__).with_name('content_preservation.json').read_text())

    def test_portable_contract_covers_all_courses_and_shared_surfaces(self):
        import test_course_ui as ui
        contract = self.contract()
        semantic = contract['authored_semantic_copy']
        self.assertEqual(semantic['baseline_sha'], '57788539d7463f4c5cd640e2571f3c40a9630750')
        trading = ui.trading.trading_inventory()
        self.assertEqual(len(trading), 8)
        self.assertEqual(set(semantic['courses']), {c['slug'] for c in trading})
        expected = {'', 'paths/trading', 'paths/discrete-math', 'paths/algebra',
                    'sets-relations-functions'}
        for course in trading:
            expected.add(course['slug'])
            expected.update(course['slug'] + '/' + lesson['slug'] for lesson in course['lessons'])
        self.assertEqual(set(semantic['pages']), expected, 'authored semantic owner omission')
        self.assertEqual(len(expected), 131)
        all_courses = (set(semantic['courses']) | {'sets-relations-functions'} |
                       set(contract['algebra_semantic_copy']['courses']) |
                       set(contract['discrete_semantic_copy']['courses']))
        registered = {c['slug'] for p in ui.build_paths.GENERATED_PATHS for c in p['courses']}
        registered.update(c['slug'] for c in trading)
        self.assertEqual(all_courses, registered)
        self.assertEqual(len(all_courses), 25)
        self.assertGreater(sum(len(p['clauses']) for p in semantic['pages'].values()), 5000)
        self.assertGreater(sum(len(p['source_records']) for p in semantic['pages'].values()), 2000)
        self.assertEqual([], authored_semantic_errors(SITE, contract))

    def test_authored_semantic_mutations_on_owned_copies(self):
        import html
        import shutil
        import test_course_ui as ui
        contract = self.contract()
        semantic = contract['authored_semantic_copy']
        cases = semantic['mutations']
        self.assertEqual(len(cases), 48)
        self.assertEqual({c['course'] for c in cases}, set(semantic['courses']))
        for course in semantic['courses']:
            self.assertEqual({c['kind'] for c in cases if c['course'] == course}, {
                'generic substitution', 'dropped dependency', 'inverted dependency',
                'missing safety boundary', 'deleted rationale', 'weakened financial disclaimer'})
        with tempfile.TemporaryDirectory(prefix='authored-semantic-', dir='/tmp') as tmp:
            site = Path(tmp)
            owners = {case['page'] for case in cases}
            for key in owners:
                file = site / key / 'index.html'
                file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(SITE / key / 'index.html', file)
            self.assertEqual([], authored_semantic_errors(site, contract, owners))
            count = 0
            for case in cases:
                with self.subTest(course=case['course'], mutation=case['kind']):
                    key = case['page']
                    file = site / key / 'index.html'
                    original = file.read_bytes()
                    source = original.decode()
                    target = next(c for c in semantic['pages'][key]['clauses']
                                  if c['field'] == case['field'])
                    matches = [m for m in re.finditer(r'<p\b[^>]*>.*?</p>', source, re.S)
                               if ui.words(ui.Elements(m[0]).find('p')[0]) == target['expected']]
                    self.assertTrue(matches, 'mutation requires a real paragraph anchor')
                    if case['kind'] == 'deleted rationale':
                        self.assertIn(case['remove'], target['expected'])
                        replacement = target['expected'].replace(case['remove'], '')
                    else:
                        replacement = case['replacement']
                    self.assertNotEqual(replacement, target['expected'])
                    mutant = source
                    for match in reversed(matches):
                        paragraph = '<p>' + html.escape(replacement) + '</p>' if replacement else ''
                        mutant = mutant[:match.start()] + paragraph + mutant[match.end():]
                    try:
                        file.write_text(mutant)
                        errors = authored_semantic_errors(site, contract, [key])
                        self.assertTrue(any(e.startswith(key + ': missing or altered ' + case['field'] + ':')
                                            for e in errors), errors)
                        count += 1
                    finally:
                        file.write_bytes(original)
                    self.assertEqual(file.read_bytes(), original)
                    self.assertEqual([], authored_semantic_errors(site, contract, [key]))
            self.assertEqual(count, 48, 'all anchored semantic mutations must be caught')


class TestDiscreteSemanticCopy(unittest.TestCase):
    # This is the bounded A/B3 semantic contract, not a scanner exception.
    COURSES = {
        'logic-and-proof', 'induction-and-recursion', 'combinatorics-and-counting',
        'discrete-probability', 'number-theory-and-cryptography', 'graphs-and-trees',
        'algorithms-and-complexity',
    }

    def contract(self):
        return json.loads(Path(__file__).with_name('content_preservation.json').read_text())

    def test_baseline_clauses_survive_in_scoped_discrete_course_homes(self):
        import test_course_ui as ui
        contract = self.contract()
        self.assertEqual(contract['base'], '57788539d7463f4c5cd640e2571f3c40a9630750')
        semantic = contract['discrete_semantic_copy']
        self.assertEqual(semantic['baseline_sha'], contract['base'])
        courses = semantic['courses']
        self.assertEqual(set(courses), self.COURSES)
        owner = next(p for p in ui.build_paths.GENERATED_PATHS if p['slug'] == 'discrete-math')
        self.assertTrue(self.COURSES <= {c['slug'] for c in owner['courses']})
        for slug, course in courses.items():
            fields = {c['field'] for c in course['clauses']}
            self.assertEqual(len(fields), len(course['clauses']), slug + ': unique clause fields')
            self.assertTrue({'title', 'blurb', 'assumes_long', 'syllabus_intro', 'footer_lead'} <= fields, slug)
            self.assertGreater(sum(f.startswith('not_covered.') for f in fields), 1, slug)
            self.assertGreater(sum(f.startswith('how_to.') for f in fields), 1, slug)
            self.assertIn(course['rationale_field'], fields)
        self.assertEqual([], discrete_semantic_errors(SITE, contract))

    def test_semantic_mutations_on_owned_discrete_course_copies(self):
        import shutil
        import test_course_ui as ui
        contract = self.contract()
        courses = contract['discrete_semantic_copy']['courses']
        self.assertEqual(set(courses), self.COURSES, 'mutation scope cannot silently shrink')
        count = 0
        with tempfile.TemporaryDirectory(prefix='discrete-semantic-mutation-', dir='/tmp') as tmp:
            site = Path(tmp)
            for slug in courses:
                (site / slug).mkdir()
                shutil.copyfile(SITE / slug / 'index.html', site / slug / 'index.html')
            self.assertEqual([], discrete_semantic_errors(site, contract), 'clean owned copies must pass')
            for slug, course in courses.items():
                file = site / slug / 'index.html'
                original = file.read_text()
                targets = {c['field']: c for c in course['clauses']}
                cases = [('generic substitution', 'blurb'), ('dropped prerequisite', 'assumes_long'),
                         ('inverted prerequisite', 'assumes_long'), ('missing exclusion', 'not_covered.0'),
                         ('deleted rationale', course['rationale_field']), ('hidden prerequisite', 'assumes_long')]
                for label, field in cases:
                    with self.subTest(course=slug, mutation=label):
                        matches = [m for m in re.finditer(r'<p\b[^>]*>.*?</p>', original, re.S)
                                   if ui.words(ui.Elements(m[0]).find('p')[0]) == targets[field]['expected']]
                        self.assertEqual(len(matches), 1, 'mutation needs one actual paragraph: ' + field)
                        match = matches[0]
                        if label == 'generic substitution':
                            replacement = '<p>Explore useful ideas and practise your skills.</p>'
                        elif label == 'inverted prerequisite':
                            replacement = '<p>' + course['inverted_prerequisite'] + '</p>'
                        elif label == 'deleted rationale':
                            reason = course['rationale_text']
                            self.assertIn(reason, match[0], 'rationale must exist before mutation')
                            replacement = match[0].replace(reason, '')
                        elif label == 'hidden prerequisite':
                            replacement = '<div hidden>' + match[0] + '</div>'
                        else:
                            replacement = ''
                        file.write_text(original[:match.start()] + replacement + original[match.end():])
                        errors = discrete_semantic_errors(site, contract)
                        self.assertTrue(any(e.startswith(slug + ': missing or altered ' + field + ':')
                                            for e in errors), errors)
                        file.write_text(original)
                        self.assertEqual([], discrete_semantic_errors(site, contract), 'restoration must pass')
                        count += 1
        self.assertEqual(count, 42, 'five semantic families and one visibility mutation for seven Courses')


class TestNestedTemplatePreservation(unittest.TestCase):
    def test_complete_template_survives_wrapper_and_rejects_semantic_mutations(self):
        import shutil
        key = 'backtesting-and-trading-systems/signal-timing-look-ahead-bias-and-data-leakage'
        contract = json.loads(Path(__file__).with_name('content_preservation.json').read_text())
        targets = [r for r in contract['authored_semantic_copy']['pages'][key]['source_records']
                   if r['boundary'] == 'dynamic-template-source']
        self.assertEqual(len(targets), 1, 'complete nested template contract is non-vacuous')
        with tempfile.TemporaryDirectory(prefix='learn-template-') as temporary:
            site = Path(temporary) / 'site'
            file = site / key / 'index.html'
            file.parent.mkdir(parents=True)
            shutil.copyfile(SITE / key / 'index.html', file)
            original = file.read_bytes()
            self.assertEqual([], authored_semantic_errors(site, contract, only=[key]))
            for before, after in [('Difference: ${pct(stats.returnPct,1)}', 'Changed: ${pct(stats.returnPct,1)}'),
                                  ('${pct(inflation,1)} points.</pre>', '${pct(inflation,2)} points.</pre>'),
                                  ('points.</pre>`', '</pre>`')]:
                with self.subTest(mutation=after):
                    text = original.decode()
                    self.assertEqual(text.count(before), 1, 'mutation owns one real template fragment')
                    file.write_text(text.replace(before, after))
                    errors = authored_semantic_errors(site, contract, only=[key])
                    self.assertTrue(any(e.startswith(key + ': missing or altered dynamic-template-source:') for e in errors), errors)
                    file.write_bytes(original)
                    self.assertEqual(file.read_bytes(), original)
                    self.assertEqual([], authored_semantic_errors(site, contract, only=[key]))
