"""Visitor UI contracts; content, URL identities and completion are independent."""

import re
import os
import json
import sys
import contextlib
import io
import shutil
import tempfile
import subprocess
import unittest
from unittest import mock
from types import SimpleNamespace
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(os.environ.get("SITE_ROOT") or ROOT / "site")
sys.path.insert(0, str(ROOT / "scripts"))
import build_paths
from mathpath import chrome
from mathpath import progress
import add_progress_marks as trading


class Elements(HTMLParser):
    """Small semantic reader used by assertions, with no markup rewriting."""

    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        for ancestor in self.stack:
            ancestor["text"] += " "
        node = {"tag": tag, "attrs": dict(attrs), "text": "", "children": []}
        self.nodes.append(node)
        if self.stack:
            self.stack[-1]["children"].append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                for ancestor in self.stack:
                    ancestor["text"] += " "
                break

    def handle_data(self, data):
        if any(n["tag"] in ("script", "style") for n in self.stack):
            return
        for node in self.stack:
            node["text"] += data

    def find(self, tag=None, **attrs):
        return [n for n in self.nodes if (tag is None or n["tag"] == tag)
                and all(n["attrs"].get(k) == v for k, v in attrs.items())]


def words(node):
    return " ".join(node["text"].split())


class TestPublishedUI(unittest.TestCase):
    def test_every_page_family_exposes_the_shared_contract(self):
        from test_site_invariants import ALL_COURSES, PATH_PAGES, REQUIRED_PAGES
        families = [("/", "library"), ("/progress/", "progress")]
        families += [(url, "subject") for url in PATH_PAGES]
        families += [(url, "course") for _title, url, _lessons in ALL_COURSES]
        families += [(url + lesson + "/", "lesson") for _title, url, lessons in ALL_COURSES for lesson in lessons]
        self.assertEqual({"library": 1, "subject": 3, "course": 25, "lesson": 336, "progress": 1},
                         {kind: sum(k == kind for _u, k in families) for _url, kind in families})
        required = {"library": ["hero", "subject-list", "course-search"],
                    "subject": ["breadcrumbs", "hero", "metadata", "overview", "course-list", "background"],
                    "course": ["breadcrumbs", "hero", "metadata", "overview", "lesson-list", "background", "course-navigation"],
                    "lesson": ["breadcrumbs", "hero", "progress", "lesson-navigation", "feedback"],
                    "progress": ["breadcrumbs", "hero", "metadata", "course-list"]}
        failures = []
        for url, kind in families:
            doc = Elements((SITE / REQUIRED_PAGES[url]).read_text())
            missing = [name for name in ["masthead", *required[kind], "footer"] if len(doc.find(**{"data-ui": name})) != 1]
            if doc.find("body")[0]["attrs"].get("data-page-kind") != kind:
                missing.append("body kind " + kind)
            if len(doc.find("main",id="main")) != 1 or len(doc.find("h1")) != 1:
                missing.append("one main#main and h1")
            if kind.capitalize().lower() not in words(doc.find("title")[0]).lower().split():
                missing.append("literal page kind in title")
            if kind == "course":
                crumb = doc.find("nav", **{"data-ui":"breadcrumbs"})[0]
                labels = [words(n) for n in crumb["children"] if n["attrs"].get("aria-hidden") != "true"]
                if "| Course | " + labels[1] + " |" not in words(doc.find("title")[0]):
                    missing.append("subject context in course title")
            if len(doc.find("a",**{"class":"skip-link","href":"#main"})) != 1:
                missing.append("skip link")
            order=[n["attrs"].get("data-ui") for n in doc.nodes if n["attrs"].get("data-ui") in required[kind]]
            if not missing and order != required[kind]:
                missing.append("region order: " + repr(order))
            if missing:
                failures.append(url + ": " + ", ".join(missing))
        self.assertEqual([],failures,"page-family UI contract failures:\n" + "\n".join(failures[:30]))


class TestVisitorTaxonomy(unittest.TestCase):
    ORDINAL = re.compile(r"(?i)\bcourse\s+\d|\bcourses\s+\d+\s+(?:and|to|through)\s+\d+|\blesson\s+\d+\s+of\s+\d+|\b(?:first|last|next) course\b")
    TAXONOMY = re.compile(r"(?i)\blearning paths?\b|\b(?:Trading|Algebra|Discrete Mathematics) paths?\b|front[- ]to[- ]back|\b(?:curricular|learning) (?:spine|roadmap|journey)\b|\b(?:start|begin) (?:with |at )?(?:course|lesson) 0?1\b")

    def test_generated_cross_references_use_titles_and_topics(self):
        copy=json.dumps(ui_data := build_paths.GENERATED_PATHS)
        awkward = re.search(r"Functions's|Inequalities's|Trees's|Polynomials and Factoring factoring|next two courses|two courses away|course was arranged around|whole course has been building toward|toolkit the course promised|course ends where|That closes the course", copy)
        self.assertIsNone(awkward, "course references must be factual and use readable titles")
        algebra=next(p for p in ui_data if p["slug"]=="algebra")
        exponentials=next(c for c in algebra["courses"] if c["slug"]=="exponential-and-logarithmic-functions")
        note=exponentials["lessons"][-1]["note"]
        self.assertIn("Sequences and Series",note,"the follow-up on constant-ratio sequences must name the sequences course")
        self.assertNotIn("Systems and Matrices",note)
        self.assertIn("constant ratio between successive terms",note,"describe the sequence topic directly")

    def test_visible_copy_separates_adjacent_elements(self):
        doc=Elements('<body><span>Library</span><p>Course 3</p><p>Execution paths and mathematical sequences.</p></body>')
        copy=words(doc.find("body")[0])
        self.assertTrue(self.ORDINAL.search(copy),"a forbidden identity at an element boundary must be detected")
        self.assertFalse(self.TAXONOMY.search("Execution paths and mathematical sequences."))
        self.assertFalse(self.ORDINAL.search("Courses 8 Lessons 118"), "catalog totals are counts, not numbered identities")

    def test_published_copy_uses_subjects_and_course_titles(self):
        from test_site_invariants import ALL_COURSES, PATH_PAGES, REQUIRED_PAGES
        urls = ["/", "/progress/", *PATH_PAGES]
        urls += [url for _t, url, _l in ALL_COURSES]
        urls += [url + lesson + "/" for _t, url, lessons in ALL_COURSES for lesson in lessons]
        failures=[]
        for url in urls:
            doc=Elements((SITE / REQUIRED_PAGES[url]).read_text())
            body_copy=words(doc.find("body")[0])
            # Teaching prose can discuss execution paths, graph paths and
            # mathematical sequences. Broad taxonomy patterns apply to the UI;
            # explicit numbered course identities remain forbidden in prose.
            kind=doc.find("body")[0]["attrs"].get("data-page-kind")
            shell_names={"masthead","breadcrumbs","page-kind","progress","lesson-navigation","feedback","footer"}
            shell_nodes=[n for n in doc.nodes if n["attrs"].get("data-ui") in shell_names]
            copy=" ".join(words(n) for n in shell_nodes) if kind=="lesson" else body_copy
            copy+=" "+words(doc.find("title")[0])
            copy+=" "+" ".join(n["attrs"].get("content","") for n in doc.find("meta")
                if n["attrs"].get("name",n["attrs"].get("property","")) in ("description","og:title","og:description","twitter:title","twitter:description"))
            accessible_nodes=doc.nodes if kind!="lesson" else shell_nodes
            copy+=" "+" ".join(v for n in accessible_nodes for k,v in n["attrs"].items()
                              if k in ("aria-label","aria-description","alt","title","placeholder") and v)
            found=sorted({m[0] for pattern,scope in ((self.ORDINAL,body_copy+" "+copy),(self.TAXONOMY,copy)) for m in pattern.finditer(scope)})
            if found:failures.append(url+": "+repr(found))
        self.assertEqual(366,len(urls),"taxonomy sweep must cover every requested page")
        self.assertEqual([],failures,"visitor taxonomy failures:\n"+"\n".join(failures[:45]))


class TestGeneratedLessonUI(unittest.TestCase):
    def test_lesson_hierarchy(self):
        checked = 0
        for subject in build_paths.GENERATED_PATHS:
            for course in subject["courses"]:
                lesson = course["lessons"][0]
                doc = Elements(build_paths.render.lesson_page(
                    path=subject, course=course, lesson=lesson, index=0,
                    prev_lesson=None, next_lesson=course["lessons"][1]))
                with self.subTest(course=course["title"]):
                    crumb = doc.find("nav", **{"aria-label": "Breadcrumb"})[0]
                    labels = [words(n) for n in crumb["children"]
                              if n["attrs"].get("aria-hidden") != "true"]
                    self.assertEqual(["Learn library", subject["title"], course["title"], lesson["title"]], labels,
                                     "lesson breadcrumb must include its subject and unnumbered names")
                    self.assertEqual("Lesson", words(doc.find(**{"data-ui": "page-kind"})[0]))
                    checked += 1
        self.assertEqual(17, checked, "hierarchy sweep must cover every generated course")

    def test_understanding_and_terminal_navigation(self):
        subject = build_paths.GENERATED_PATHS[0]
        course = subject["courses"][0]
        lesson = course["lessons"][-1]
        markup = build_paths.render.lesson_page(path=subject, course=course, lesson=lesson,
            index=len(course["lessons"]) - 1, prev_lesson=course["lessons"][-2], next_lesson=None)
        doc = Elements(markup)
        self.assertIn("Check your understanding", [words(n) for n in doc.find("h3")])
        terminal = doc.find("a", **{"class": "lesson-link next"})[0]
        self.assertEqual("Course overview", words(terminal["children"][0]))
        self.assertNotIn("rel", terminal["attrs"])
        self.assertEqual("../", terminal["attrs"]["href"])
        self.assertIn(build_paths.render.inline(lesson["standard"][1]), markup,
                      "renaming the heading must preserve the pedagogical criterion")


class TestSharedMasthead(unittest.TestCase):
    def test_navigation_and_control_order(self):
        doc = Elements(chrome.topbar(up="../../"))
        header = doc.find("header")[0]
        self.assertEqual("masthead", header["attrs"].get("data-ui"))
        brand, nav, actions = header["children"]
        self.assertEqual("Learn", words(brand))
        self.assertEqual("../../", brand["attrs"].get("href"))
        self.assertEqual(["Subjects", "Courses", "Progress"], [words(n) for n in nav["children"]])
        self.assertEqual(["../../#paths", "../../#courses", "../../progress/"],
                         [n["attrs"].get("href") for n in nav["children"]])
        self.assertEqual(["signinLink", "themeToggle"], [n["attrs"].get("id") for n in actions["children"]])
        self.assertEqual("Toggle light and dark theme", actions["children"][1]["attrs"].get("aria-label"))


class TestLibraryUI(unittest.TestCase):
    def test_library_browses_subjects_and_search_reports_subject_names(self):
        markup = (SITE / "index.html").read_text()
        doc = Elements(markup)
        self.assertEqual("library", doc.find("body")[0]["attrs"].get("data-page-kind"))
        self.assertEqual("Learn library", words(doc.find("h1")[0]))
        self.assertIn("Subjects", [words(n) for n in doc.find("h2")])
        self.assertNotRegex(words(doc.find("main")[0]), r"(?i)\b(?:learning )?paths\b|\d+ subjects|take.*courses in order|\bcourse \d")
        # Execute the shipped result renderer. Source-only scans miss JS-created copy.
        code = r'''
const fs = require('fs'), vm = require('vm'), assert = require('assert');
const source = fs.readFileSync(process.argv[1], 'utf8');
function el(tag) { return {tag, children: [], own: '', appendChild(n){this.children.push(n);},
  set textContent(v){this.own = v;}, get textContent(){return this.own + this.children.map(n=>n.textContent).join('');}}; }
const context = {document:{createElement:el,createTextNode(s){const n=el('text');n.textContent=s;return n;}},
  highlighted(s){const n=el('text');n.textContent=s;return n;}};
vm.createContext(context);
for (const name of ['metaItem','resultItem','emptyState']) {
  const a=source.indexOf('function '+name+'('), b=source.indexOf('\n      function ',a+1);
  assert(a>=0 && b>a, name+' source missing');
  vm.runInContext(source.slice(a,b).replace(/\/\*[\s\S]*?\*\//g,''),context);
}
const result=context.resultItem({title:'Logic and Proof',href:'./logic-and-proof/',path:'Discrete Mathematics',position:'Course 1',lessons:14,description:'Logic'},'');
assert.deepStrictEqual(result.children[1].children.map(n=>n.textContent),['Discrete Mathematics','14 lessons']);
assert(!/\bpath\b/i.test(context.emptyState('missing').textContent));
const inventory=/var COURSES = (\[[\s\S]*?\n      \]);/.exec(source);
assert(inventory,'course search inventory missing');
const courses=vm.runInNewContext(inventory[1]);
assert.equal(courses.length,25,'search must cover every published course');
for(const c of courses) assert(!/\b(?:the|this|learning|Trading|Algebra|Discrete Mathematics) path\b|\bcourse\s+\d/i.test(context.resultItem(c,'').textContent),c.title+' has curricular search copy');
assert.deepStrictEqual(JSON.parse(JSON.stringify(courses.map(c=>[c.path,c.title,c.href,c.lessons]))),EXPECTED_INVENTORY);
console.log('library search: subject names, factual lesson counts, neutral empty state');
'''
        import build_auth_pages
        expected = [[subject["title"],course["title"],"./"+course["slug"]+"/",len(course["lessons"])]
                    for subject in build_auth_pages.library_inventory() for course in subject["courses"]]
        code = code.replace("EXPECTED_INVENTORY",json.dumps(expected))
        result = subprocess.run(["node", "-e", code, str(SITE / "index.html")], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


class TestMarkLabels(unittest.TestCase):
    def test_course_marks_have_readable_state(self):
        for script in (progress.COURSE_JS, trading.COURSE_JS):
            code = r'''
const vm=require('vm'), assert=require('assert');
let on=true, listener; const state={textContent:''};
const item={getAttribute(){return 'c/l';},querySelector(){return state;},classList:{toggle(){}}};
const context={document:{getElementById(){return {};},querySelectorAll(){return [item];}},
 window:{learnProgress:{done(){return on;}},addEventListener(name,f){listener=f;}}};
vm.runInNewContext(SCRIPT,context);
assert.equal(state.textContent,'Marked complete');
on=false;listener();assert.equal(state.textContent,'Not marked');
'''.replace("SCRIPT", json.dumps(script))
            result = subprocess.run(["node", "-e", code],capture_output=True,text=True)
            self.assertEqual(0,result.returncode,result.stderr)


class TestTradingIntakeUI(unittest.TestCase):
    def test_intake_breadcrumb_and_terminal_return(self):
        import intake_course
        lesson=SimpleNamespace(title="Options Contract Fundamentals",ordinal="01",slug="options-contract-fundamentals")
        ctx={"lesson":lesson,"course_title":"Options Trading","lessons":[lesson],"index":0}
        doc=Elements(intake_course.build_breadcrumb(ctx))
        breadcrumb=doc.find("nav")[0]
        self.assertEqual(["Learn library","Trading","Options Trading",lesson.title],
            [words(n) for n in breadcrumb["children"] if n["attrs"].get("aria-hidden") != "true"])
        terminal=Elements(intake_course.build_pager(ctx)).find("a")[0]
        self.assertEqual("Course overview",words(terminal["children"][0]))
        self.assertNotIn("rel",terminal["attrs"])


class TestGeneratedCatalogUI(unittest.TestCase):
    def test_subject_catalog_has_unnumbered_courses(self):
        checked = 0
        for subject in build_paths.GENERATED_PATHS:
            doc = Elements(build_paths.render.path_page(subject))
            self.assertEqual("Subject", words(doc.find(**{"data-ui": "page-kind"})[0])
                             if doc.find(**{"data-ui": "page-kind"}) else None)
            self.assertEqual([c["title"] for c in subject["courses"]],
                [words(n["children"][0]["children"][0]) for n in doc.find("a", **{"class": "spine-item"})])
            self.assertFalse(doc.find(**{"class": "spine-num"}), "subject cards must not number courses")
            self.assertIn("Recommended background", [words(n) for n in doc.find("h2")])
            actions = doc.find(**{"data-ui": "primary-actions"})[0]
            self.assertEqual("View courses", words(actions["children"][0]))
            self.assertEqual("#courses", actions["children"][0]["attrs"]["href"])
            self.assertNotRegex(words(doc.find("body")[0]),
                r"(?i)\blearning path\b|\bthe path\b|\bthis path\b|\bpath &middot;|\bcourse\s+\d|in (?:a )?fixed order|why this order|front to back")
            checked += 1
        self.assertEqual(2, checked)

    def test_course_overview_has_factual_identity_and_optional_navigation(self):
        checked = 0
        for subject in build_paths.GENERATED_PATHS:
            for i, course in enumerate(subject["courses"]):
                checked += 1
                doc = Elements(build_paths.render.course_home(course=course, index=i,
                    courses=subject["courses"], path=subject))
                with self.subTest(course=course["title"]):
                    self.assertEqual("Course", words(doc.find(**{"data-ui": "page-kind"})[0])
                                     if doc.find(**{"data-ui": "page-kind"}) else None)
                    crumb = doc.find("nav", **{"aria-label": "Breadcrumb"})[0]
                    self.assertEqual(["Learn library", subject["title"], course["title"]],
                        [words(n) for n in crumb["children"] if n["attrs"].get("aria-hidden") != "true"])
                    self.assertIn("Recommended background", [words(n) for n in doc.find("h2")])
                    actions = doc.find(**{"data-ui": "primary-actions"})[0]
                    self.assertEqual("#syllabus", actions["children"][0]["attrs"]["href"])
                    self.assertEqual("View lessons", words(actions["children"][0]))
                    labels = [words(n) for n in doc.find("dt")]
                    self.assertEqual(["Subject", "Lessons", "Format"], labels)
                    if i == len(subject["courses"]) - 1:
                        terminal = doc.find("a", **{"class": "path-move next"})[0]
                        self.assertEqual("All %s courses" % subject["title"], words(terminal))
                        self.assertNotIn("rel", terminal["attrs"])
                    self.assertFalse(re.search(r"\bcourse\s+\d|lessons? in (?:a )?fixed order", words(doc.find("body")[0]), re.I),
                                     "course identity and overview must not prescribe course order")
        self.assertEqual(17, checked)


class TestTradingNormalization(unittest.TestCase):
    def test_legacy_shells_preserve_domain_copy_and_hero_controls(self):
        course={"slug":"example-course","title":"Example Course","lessons":[{"slug":"example-lesson","title":"Example Lesson"}]}
        lesson=course["lessons"][0]
        visual='<div class="hero-visual"><svg viewBox="0 0 100 100" aria-label="Execution path"><path d="M0 0L100 100" /></svg></div>'
        content='<section class="section" id="lab"><h2>Keep the trading path explicit</h2><p>The execution path processes orders one at a time.</p><button id="labAction" type="button">Run</button></section>'
        authored='<script>var sentinel = "Keep the trading path explicit";</script>'
        for compact in (False,True):
            reset='<button class="icon-btn" id="resetBtn" type="button" aria-label="Reset lab">Reset</button>' if compact else ''
            header='<header class="topbar"><a class="brand" href="../">Old course identity</a>'+reset+chrome.THEME_TOGGLE+'</header>'
            crumb='<nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Learn library</a></nav>'
            hero='<section class="hero"><div><span class="eyebrow">Course 1</span><h1>Example Lesson</h1><p>Inspect an execution path.</p><div class="hero-actions"><button id="openLab" type="button">Open lab</button></div></div>'+visual+'</section>'
            start='<main class="shell">' if compact else '<div class="shell">'
            middle='' if compact else '<main id="main">'
            end='</main>' if compact else '</main></div>'
            source='<!doctype html><html><head><title>Example</title><style>:root { --panel2: #123; --line2: #345; } body { color: black; }</style></head><body>'+start+header+crumb+middle+hero+content+'<nav class="lesson-nav" aria-label="Lesson navigation"></nav><footer><p>Example course.</p></footer>'+end+authored+'</body></html>'
            if not compact:
                source=source.replace('<nav class="lesson-nav"', '\n    <div class="progress-bar">\n      <button id="progressToggle" type="button">Mark this lesson complete</button>\n    </div>\n<nav class="lesson-nav"')
            source=source.replace('</style>', '\n</style>').replace('<nav class="lesson-nav"', '\n<nav class="lesson-nav"')
            result=trading.prepare_lesson(source,'example-course/example-lesson/index.html',course,lesson,[course]*8)
            self.assertIn(content,result,"instructional domain copy must survive a first pass on a legacy shell")
            self.assertIn(visual,result,"hero diagrams and their accessible names must survive")
            self.assertIn(authored,result,"authored scripts must survive")
            self.assertEqual(source.count('id="resetBtn"'),result.count('id="resetBtn"'))
            self.assertEqual(1,result.count('id="openLab"'))
            self.assertEqual(result,trading.prepare_lesson(result,'example-course/example-lesson/index.html',course,lesson,[course]*8))

    def test_published_trading_names_are_literal(self):
        courses=trading.trading_inventory()
        failures=[]
        for course in courses:
            for lesson in course["lessons"]:
                relative=course["slug"]+"/"+lesson["slug"]+"/index.html"
                doc=Elements((SITE/relative).read_text())
                expected=lesson["title"]+" | Lesson | "+course["title"]+" | Trading | Learn · geterdone.io"
                if words(doc.find("title")[0]) != expected:
                    failures.append(relative+": escaped lesson title")
                if words(doc.find("footer")[0]).count(course["title"]) > 1:
                    failures.append(relative+": repeated footer course identity")
        self.assertEqual(118,sum(len(c["lessons"]) for c in courses))
        self.assertEqual([],failures,"literal Trading identities:\n"+"\n".join(failures[:10]))

    def test_legacy_palette_and_hero_controls_support_shared_styles(self):
        from test_site_invariants import stylesheet, css_rules, css_variables, light_paths
        courses=trading.trading_inventory()
        for course in courses:
            relative=course["slug"]+"/"+course["lessons"][0]["slug"]+"/index.html"
            rendered=trading.ensure_css((trading.SITE/relative).read_text())
            css=stylesheet(rendered)
            rules=css_rules(css)
            declared={k for _ctx,_selector,declarations in rules for k in css_variables(declarations)}
            with self.subTest(course=course["title"]):
                self.assertEqual({"toggle":1,"media":1},{k:len(v) for k,v in light_paths(rendered).items()},
                                 "palette aliases must preserve one declaration for each light-theme path")
                self.assertTrue({"--panel-2","--line-strong","--on-accent"} <= declared,
                                "shared surface, border and accent ink tokens must resolve on legacy palettes")
                reset=[decl for ctx,selector,decl in rules if not ctx and '[data-ui="primary-actions"] .icon-btn' in selector]
                self.assertTrue(any(re.search(r"min-height:\s*44px",decl) and re.search(r"min-width:\s*44px",decl) for decl in reset),
                                "hero reset controls need a practical 44px touch target")
        self.assertEqual(8,len(courses))

    def test_trading_lesson_state_is_inside_the_card_content(self):
        source='<article class="lesson-card"><div class="lesson-body"><a class="lesson-link" href="./example/">Example</a><p>Factual description.</p></div></article><p class="course-progress" id="courseProgress"></p>'
        source=source.replace('</article>', '\n    <span class="lesson-state">Not marked</span>\n    \n</article>')
        result=trading.ensure_course_hooks(source,"sample",[{"slug":"example","title":"Example"}])
        body=Elements(result).find("div",**{"class":"lesson-body"})[0]
        self.assertIn("Not marked",words(body),"completion state belongs in the padded lesson card content")
        self.assertNotRegex(result,r"(?m)^[ \t]+$","moving a completion label must not leave whitespace-only lines")
        self.assertEqual(result,trading.ensure_course_hooks(result,"sample",[{"slug":"example","title":"Example"}]))

    def test_authored_inventory_names_are_decoded_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            site=Path(tmp)
            (site / "example").mkdir()
            (site / "example/index.html").write_text('<article class="lesson-card"><a class="lesson-link" href="./ranges/">Ranges &amp; Breakouts</a></article>')
            with mock.patch.object(trading, "SITE", site):
                lessons=trading.course_lessons("example")
            self.assertEqual([{"slug":"ranges", "title":"Ranges & Breakouts"}], lessons,
                             "inventory titles must be decoded before chrome escapes them")
            crumb=Elements(chrome.crumbs([(lessons[0]["title"],None)]))
            self.assertEqual("Ranges & Breakouts", words(crumb.find("nav")[0]))

    def test_normalized_catalog_prose_remains_authored(self):
        courses=trading.trading_inventory()
        course=courses[0]
        for relative, normalize in [
                (course["slug"]+"/index.html", lambda text: trading.normalize_course_ui(text,course,courses,0)),
                (trading.PATH_PAGE, lambda text: trading.normalize_subject_ui(text,courses))]:
            text=(trading.SITE/relative).read_text()
            hero=trading.element(text,"section",cls="hero")
            region=text[hero["start"]:hero["end"]]
            region=trading.replace_element(region,trading.element(region,"p"),'<p>Authored factual overview retained on later runs.</p>')
            revised=trading.replace_element(text,hero,region)
            self.assertIn('<p>Authored factual overview retained on later runs.</p>',normalize(revised),
                          "the UI migration must leave subsequent authored catalog edits authoritative")

    def test_incomplete_inventory_is_rejected_before_transformation(self):
        inventory=trading.trading_inventory()
        with mock.patch.object(trading,"trading_inventory",return_value=inventory[:-1]), \
             mock.patch.object(trading,"normalize_lesson_ui",side_effect=AssertionError("transformation began with an incomplete inventory")):
            with self.assertRaisesRegex(ValueError,"inventory"):
                trading.main()

    def test_course_and_subject_catalog_contract(self):
        inventory = trading.trading_inventory()
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / "site"
            for course in inventory:
                shutil.copytree(trading.SITE / course["slug"], site / course["slug"])
            shutil.copytree(trading.SITE / "paths/trading", site / "paths/trading")
            shutil.copy2(trading.SITE / "index.html", site / "index.html")
            with mock.patch.object(trading, "SITE", site), contextlib.redirect_stdout(io.StringIO()):
                trading.main()
                self.assertEqual(inventory, trading.trading_inventory(), "catalog normalization must preserve inventory and order")
            for relative, kind in [(Path(c["slug"]) / "index.html", "course") for c in inventory] + [(Path(trading.PATH_PAGE), "subject")]:
                doc = Elements((site / relative).read_text())
                with self.subTest(page=str(relative)):
                    self.assertEqual(kind, doc.find("body")[0]["attrs"].get("data-page-kind"))
                    self.assertEqual(kind.capitalize(), words(doc.find(**{"data-ui": "page-kind"})[0]))
                    self.assertIn("Recommended background", [words(n) for n in doc.find("h2")])
                    self.assertTrue(doc.find(**{"data-ui": "overview"}))
                    self.assertTrue(doc.find(**{"data-ui": "lesson-list" if kind == "course" else "course-list"}))
                    self.assertFalse([n for n in doc.find(**{"class": "course-ord"})
                                      if re.search(r"(?i)course\s+\d", words(n))], "course number badges must be removed")
                    self.assertNotRegex(words(doc.find("main")[0]),
                        r"(?i)\bcourse\s+\d|\btrading path\b|\blearning path\b|\bthe path\b|in order,|lessons, in order|start at (?:lesson )?01|start at lesson")

    def test_failed_preflight_writes_nothing(self):
        inventory = trading.trading_inventory()
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / "site"
            for course in inventory:
                shutil.copytree(trading.SITE / course["slug"], site / course["slug"])
            shutil.copytree(trading.SITE / "paths/trading", site / "paths/trading")
            shutil.copy2(trading.SITE / "index.html", site / "index.html")
            course = inventory[-1]
            target = site / course["slug"] / course["lessons"][-1]["slug"] / "index.html"
            target.write_text(target.read_text().replace('<section class="hero"', '<section class="unknown-hero"'))
            # Force an early repair even when the checked-in pages are normalized.
            early = site / inventory[0]["slug"] / inventory[0]["lessons"][0]["slug"] / "index.html"
            early.write_text(early.read_text().replace('data-ui="masthead"','data-ui="broken-masthead"'))
            before = {p.relative_to(site): p.read_bytes() for p in site.rglob("*.html")}
            with mock.patch.object(trading, "SITE", site), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(ValueError, "hero"):
                    trading.main()
            changed = [str(p.relative_to(site)) for p in site.rglob("*.html")
                       if before[p.relative_to(site)] != p.read_bytes()]
            self.assertEqual([], changed, "failed preflight must leave every earlier page untouched")

    def test_lesson_shell_preserves_instruction_and_is_idempotent(self):
        inventory = trading.trading_inventory()
        self.assertEqual((8, 118), (len(inventory), sum(len(c["lessons"]) for c in inventory)))
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / "site"
            for course in inventory:
                shutil.copytree(trading.SITE / course["slug"], site / course["slug"])
            shutil.copytree(trading.SITE / "paths/trading", site / "paths/trading")
            shutil.copy2(trading.SITE / "index.html", site / "index.html")
            before = {p.relative_to(site): p.read_text() for p in site.rglob("*.html")}
            with mock.patch.object(trading, "SITE", site), contextlib.redirect_stdout(io.StringIO()):
                trading.main()
                once = {p.relative_to(site): p.read_text() for p in site.rglob("*.html")}
                trading.main()
            self.assertEqual(once, {p.relative_to(site): p.read_text() for p in site.rglob("*.html")},
                             "a second normalization pass must change no bytes")
            checked = 0
            for course in inventory:
                for lesson in course["lessons"]:
                    checked += 1
                    relative = Path(course["slug"]) / lesson["slug"] / "index.html"
                    original, result = before[relative], once[relative]
                    doc = Elements(result)
                    with self.subTest(page=str(relative)):
                        self.assertEqual("lesson", doc.find("body")[0]["attrs"].get("data-page-kind"))
                        self.assertEqual(1, len(doc.find("main", id="main")))
                        self.assertEqual(1, len(doc.find("a", **{"class": "skip-link", "href": "#main"})))
                        crumb = doc.find("nav", **{"aria-label": "Breadcrumb"})[0]
                        self.assertEqual(["Learn library", "Trading", course["title"], lesson["title"]],
                            [words(n) for n in crumb["children"] if n["attrs"].get("aria-hidden") != "true"])
                        self.assertEqual(1, len(doc.find("header", **{"data-ui": "masthead"})))
                        self.assertEqual("Lesson", words(doc.find(**{"data-ui": "page-kind"})[0]))
                        self.assertEqual(original.count('id="resetBtn"'), result.count('id="resetBtn"'))
                        # Exact source spans: teaching after the hero, before completion markup.
                        def instruction(s):
                            start = re.search(r'<section\b[^>]*class="section"', s).start()
                            return s[start:s.index('<div class="progress-bar"')].replace('</main>', '').strip()
                        self.assertEqual(instruction(original), instruction(result), "instructional markup changed")
                        scripts = lambda s: re.findall(r'<script(?:\s+[^>]*)?>.*?</script>', s, re.S)
                        authored = lambda s: [v for v in scripts(s) if 'data-progress-marks' not in v]
                        self.assertEqual(authored(original), authored(result), "authored lab or theme script changed")
            self.assertEqual(118, checked)


if __name__ == "__main__":
    unittest.main()
