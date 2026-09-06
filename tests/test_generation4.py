"""Neutral document links and full-lifecycle mutation ownership."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from urllib.parse import urljoin

import test_course_ui as ui


def navigation_errors(markup, route, titles):
    doc = ui.Elements(markup)
    navs = doc.find('nav', **{'data-ui': 'lesson-navigation'})
    if len(navs) != 1:
        return ['exactly one nonempty Course and lesson links region required']
    nav = navs[0]
    errors = []
    if nav['attrs'].get('aria-label') != 'Course and lesson links':
        errors.append('neutral accessible navigation name required')
    links = nav['children']
    if not links:
        errors.append('nonempty document links required')
    for link in links:
        target = titles.get(urljoin(route, link['attrs'].get('href', '')))
        if not target:
            errors.append('published Course or Lesson destination required')
            continue
        kind, title = target
        if ui.words(link) != kind + ' ' + title:
            errors.append('neutral literal document label required: ' + ui.words(link))
        for key in ('aria-label', 'title', 'aria-description'):
            if key in link['attrs'] and link['attrs'][key] != kind + ' ' + title:
                errors.append('neutral accessible document label required')
    return errors


class TestNeutralLessonLinks(unittest.TestCase):
    def test_intake_neighbors_are_literal_and_guarded(self):
        import intake_course
        from types import SimpleNamespace
        lessons = [SimpleNamespace(slug=slug, ordinal=str(i + 1), title=title)
                   for i, (slug, title) in enumerate([('a', 'One & two'), ('b', 'Another title'), ('c', 'Final literal title')])]
        titles = {'/c/': ('Course', 'Example Course'), **{'/c/' + item.slug + '/': ('Lesson', item.title) for item in lessons}}
        for index, lesson in enumerate(lessons):
            ctx = dict(lessons=lessons, index=index, course_title='Example Course')
            markup = intake_course.build_pager(ctx)
            self.assertEqual([], navigation_errors(markup, '/c/' + lesson.slug + '/', titles))
            broken = markup.replace('<span>Lesson</span>', '<span>Next lesson</span>')
            self.assertNotEqual(markup, broken)
            self.assertTrue(navigation_errors(broken, '/c/' + lesson.slug + '/', titles), 'intake navigation mutation')

    def test_all_336_lessons_use_literal_taxonomic_links(self):
        from test_site_invariants import ALL_COURSES
        titles, lessons = {}, {}
        for _, home, slugs in ALL_COURSES:
            for route in [home, *(home + slug + '/' for slug in slugs)]:
                markup = (ui.SITE / route.lstrip('/') / 'index.html').read_text()
                doc = ui.Elements(markup)
                kind = 'Course' if route == home else 'Lesson'
                self.assertEqual(1, len(doc.find('h1')), route)
                title = ui.words(doc.find('title')[0]).split(' | ' + kind + ' | ')[0]
                self.assertTrue(title, 'literal published document title')
                titles[route] = kind, title
                if kind == 'Lesson':
                    lessons[route] = markup
        self.assertEqual(25, len(ALL_COURSES))
        self.assertEqual(336, len(lessons), 'non-vacuous complete Lesson inventory')
        failures = {route: errors for route, markup in lessons.items()
                    if (errors := navigation_errors(markup, route, titles))}
        self.assertEqual({}, failures, 'neutral Lesson links across the complete corpus')

    def test_navigation_guard_mutations(self):
        good = '<nav data-ui="lesson-navigation" aria-label="Course and lesson links"><a href="../b/"><span>Lesson</span><strong>Literal &amp; title</strong></a></nav>'
        titles = {'/c/b/': ('Lesson', 'Literal & title')}
        self.assertEqual([], navigation_errors(good, '/c/a/', titles))
        for text in ['Previous lesson', 'Next lesson', 'Step', '→ Lesson', 'Lesson 03 ·', 'Start here']:
            bad = good.replace('<span>Lesson</span>', '<span>' + text + '</span>')
            self.assertTrue(any('neutral literal document label' in e for e in navigation_errors(bad, '/c/a/', titles)), text)
        for bad in [good.replace('Course and lesson links', 'Lesson navigation'), good.replace('<a href=', '<a aria-label="Next lesson" href='), good.replace('<strong>Literal &amp; title</strong>', '<strong>03 · Literal &amp; title</strong>'), good.replace('data-ui="lesson-navigation"', '')]:
            self.assertTrue(navigation_errors(bad, '/c/a/', titles), bad)
        self.assertTrue(navigation_errors('<nav data-ui="lesson-navigation" aria-label="Course and lesson links"></nav>', '/c/a/', titles))


class TestMutationLifecycle(unittest.TestCase):
    def test_preflight_failure_removes_owned_export(self):
        # Inject at the existing preflight boundary: the entire copy already
        # exists. This is a real setup error, and cleanup is the assertion.
        evidence = Path(os.environ.get('GEN4_EVIDENCE', tempfile.gettempdir()))
        with tempfile.TemporaryDirectory(prefix='lifecycle-', dir=evidence) as tmp:
            root = Path(tmp)
            hook = root / 'failure.cjs'
            hook.write_text("const fs=require('node:fs'),path=require('node:path');const mkdir=fs.mkdirSync;fs.mkdirSync=function(p,...args){if(path.basename(String(p))==='target-preflight')throw Error('INJECTED after disposable copy');return mkdir.call(this,p,...args)};")
            out = root / 'evidence'
            run = subprocess.run(['node', str(ui.ROOT / 'tests/mutate_browser_ui.js')], env=dict(os.environ, BROWSER_EVIDENCE=str(out), NODE_OPTIONS='--require=' + str(hook)), capture_output=True, text=True)
            # Persist diagnostic logs outside the owned export, even on RED.
            if os.environ.get('GEN4_EVIDENCE'):
                (evidence / 'lifecycle-injected-output.log').write_text(run.stdout + run.stderr)
            self.assertEqual(1, run.returncode)
            self.assertIn('INJECTED after disposable copy', run.stdout + run.stderr)
            residue = list((out / 'disposable-export').rglob('*'))
            self.assertFalse((out / 'disposable-export').exists(), 'owned disposable export leaked after setup failure: %d entries' % len(residue))

    def test_scroller_transform_is_idempotent_and_ignores_script_strings(self):
        from mathpath import chrome
        script = '<script>const sample=\'<div class="table-wrap">\';</script>'
        markup = '<div class="mathblock">x + y</div><div class="table-wrap" tabindex="0" aria-label="Journal"></div>' + script
        result = chrome.name_horizontal_scrollers(markup)
        self.assertIn('role="region" aria-label="Mathematical notation"', result)
        self.assertIn('aria-label="Journal"', result)
        self.assertIn(script, result)
        self.assertEqual(result, chrome.name_horizontal_scrollers(result))


class TestCapstonePaletteSource(unittest.TestCase):
    def test_both_authored_layouts_refresh_from_palette_owner(self):
        from mathpath import capstone
        pages = [p for p in ui.SITE.rglob('*.html') if re.search(r'<body data-page-kind="(?:slides|supplemental)"', p.read_text())]
        self.assertEqual(2, len(pages))
        for page in pages:
            text = page.read_text()
            self.assertIn(capstone.PALETTE, text, 'source-owned capstone palette')
            self.assertEqual(text, capstone.normalize_palette(text), 'capstone palette idempotence')
            self.assertEqual(2, text.count(capstone.LIGHT), 'both light paths use source tokens')
            broken = text.replace(capstone.LIGHT, capstone.LIGHT.replace('#08616e', '#98f5ff'))
            self.assertNotEqual(text, broken)
            self.assertEqual(text, capstone.normalize_palette(broken), 'source restores both light paths')


if __name__ == '__main__':
    unittest.main()
