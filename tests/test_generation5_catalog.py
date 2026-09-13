"""Capability-derived catalog coverage and baseline-bound audience semantics."""
import json
import os
import re
import subprocess
import unittest
from urllib.parse import urljoin

import test_course_ui as ui

BASELINE='57788539d7463f4c5cd640e2571f3c40a9630750'


def catalog_inventory(site):
    pages={}
    for file in site.rglob('*.html'):
        doc=ui.Elements(file.read_text())
        body=doc.find('body')
        pages['/'+file.relative_to(site).as_posix().removesuffix('index.html')]=(body[0]['attrs'].get('data-page-kind'),doc)
    courses={route:doc for route,(kind,doc) in pages.items() if kind=='course'}
    lessons={route for route,(kind,doc) in pages.items() if kind=='lesson'}
    links=[dict(course=route,target=urljoin(route,a['attrs'].get('href','')),href=a['attrs'].get('href',''),
                text=ui.words(a),family=a['attrs'].get('class',''))
           for route,doc in courses.items() for a in doc.find('a')
           if urljoin(route,a['attrs'].get('href','')) in lessons]
    return courses,lessons,links


def ordinal(text):
    return bool(re.match(r'^(?:Lesson\s+)?\d{1,3}(?!\d)',text,re.I))


class TestCatalogDestinations(unittest.TestCase):
    def test_every_lesson_destination_is_literal(self):
        courses,lessons,links=catalog_inventory(ui.SITE)
        self.assertEqual(25,len(courses))
        self.assertEqual(336,len(lessons))
        self.assertEqual(351,len(links))
        self.assertEqual(lessons,{a['target'] for a in links})
        self.assertEqual(set(courses),{a['course'] for a in links})
        bad=[a for a in links if ordinal(a['text'])]
        if os.environ.get('GEN5_EVIDENCE'):
            from pathlib import Path
            p=Path(os.environ['GEN5_EVIDENCE']);p.mkdir(exist_ok=True,parents=True)
            (p/'catalog-inventory.json').write_text(json.dumps(dict(courses=len(courses),lessons=len(lessons),links=links,ordinal_failures=bad),indent=2)+'\n')
        self.assertEqual([],bad,'visible Lesson destination ordinals must be absent')

    def test_anchor_family_guard_mutations(self):
        for family in ['syllabus-item','lesson-link','file-link']:
            good=f'<a class="{family}" href="./literal/">Literal lesson title</a>'
            self.assertFalse(ordinal(ui.words(ui.Elements(good).find('a')[0])))
            for prefix in ['01 ','Lesson 15 · ']:
                bad=good.replace('>Literal','>'+prefix+'Literal')
                self.assertTrue(ordinal(ui.words(ui.Elements(bad).find('a')[0])),family)


def derive_audience(course, courses):
    """The course's baseline 'Who it is for' text, read from the Git object."""
    route = 'site/' + course['slug'] + '/index.html'
    original = ui.Elements(subprocess.check_output(
        ['git', 'show', BASELINE + ':' + route], cwd=ui.ROOT, text=True,
        stderr=subprocess.DEVNULL))
    heading = next(n for n in original.find('h3') if ui.words(n) == 'Who it is for')
    parent = next(n for n in original.nodes if any(c is heading for c in n['children']))
    audience = ' '.join(ui.words(n) for n in parent['children'] if n['tag'] == 'p')
    audience = audience.replace('courses 6 and 7', 'Trading Risk Management and Backtesting and Trading Systems')
    audience = re.sub(r'\bcourse ([1-8])\b', lambda m: courses[int(m[1]) - 1]['title'], audience, flags=re.I)
    audience = audience.replace('lesson 01 starts from a bare candlestick chart', 'Market Structure Lab starts from a bare candlestick chart')
    audience = audience.replace('The later lessons stay useful', 'The lessons stay useful')
    return audience


def baseline_object_present():
    return subprocess.run(['git', 'cat-file', '-e', BALANCE_PROBE], cwd=ui.ROOT,
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


BALANCE_PROBE = BASELINE + '^{commit}'


class TestAuthoredPrerequisites(unittest.TestCase):
    """The baseline text is carried in the fixture, not read from Git.

    CI checks out at depth 1, so the baseline commit is not in the object store
    there and `git show` exits 128. Carrying the eight paragraphs in
    content_preservation.json makes the assertion run everywhere; the
    re-derivation below keeps the carried copy honest wherever the object does
    exist, so it cannot drift unnoticed into something the baseline never said.
    """

    def setUp(self):
        from pathlib import Path
        self.contract = json.loads(Path(__file__).with_name('content_preservation.json').read_text())['baseline_audience']

    def test_every_baseline_audience_qualification_survives(self):
        courses = ui.trading.trading_inventory()
        carried = self.contract['courses']
        self.assertEqual(8, len(courses))
        self.assertEqual({c['slug'] for c in courses}, set(carried))
        failures = []
        for course in courses:
            audience = carried[course['slug']]
            current = ui.Elements((ui.SITE / course['slug'] / 'index.html').read_text())
            if audience not in [ui.words(p) for p in current.find('p')]:
                failures.append(dict(course=course['slug'], required=audience))
        self.assertEqual([], failures, 'baseline audience qualifications cannot be replaced by generic prerequisites')

    def test_carried_audience_matches_the_baseline_object(self):
        if not baseline_object_present():
            self.skipTest('shallow checkout: baseline commit ' + BASELINE[:12] + ' is not in the object store')
        courses = ui.trading.trading_inventory()
        self.assertEqual(BASELINE, self.contract['baseline_sha'])
        drifted = [c['slug'] for c in courses
                   if derive_audience(c, courses) != self.contract['courses'][c['slug']]]
        self.assertEqual([], drifted, 'carried baseline audience text no longer matches the baseline commit')

    def test_technical_indicators_scope_boundary(self):
        doc=ui.Elements((ui.SITE/'technical-indicators/index.html').read_text())
        text=ui.words(doc.find('body')[0])
        self.assertNotIn('volatility, and volume indicators',text,'Technical Indicators must not advertise Volume and Order Flow scope')
        self.assertIn('volume-derived tools',text,'authored scope exclusion must survive')
        self.assertIn('Volume and Order Flow',text)
