"""english, the English Subject's kit: every lesson's lab builds, emits ES5,
pins every preset, and carries the cleaned word lists rather than the raw NGSL.

No browser. One test runs the table lab's script under node with a stub DOM to
see the refusal of bad input, and skips when node is absent. Whether the
figures are RIGHT is scripts/labcheck.js's job on a rendered page; whether the
cleaned lists are current is scripts/wordlists/clean_verbs.py --check.

    /usr/bin/python3 -m unittest tests.test_english_kit -v
"""

import json
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))

from mathpath import labs  # noqa: E402
from mathpath.labs import english  # noqa: E402

# The same list test_argkit.py holds Philosophy's kit to.
NOT_ES5 = [
    (re.compile(r"=>"), "arrow function"),
    (re.compile(r"(^|[\s;{(])(let|const)\s"), "let/const"),
    (re.compile(r"`"), "template literal"),
    (re.compile(r"\?\."), "optional chaining"),
    (re.compile(r"\?\?"), "nullish coalescing"),
    (re.compile(r"\(\?<[=!]"), "lookbehind"),
    (re.compile(r"\b\d+n\b"), "BigInt literal"),
]

# A cfg_literal line is JSON (json.dumps), so it is ES5 by construction -- and
# it holds printed English, where "let me" and "=>" are words, not syntax.
DATA_LINE = re.compile(r"^  var [A-Z_]+ = .*;$", re.M)


# Every mode, and every cfg variant a lesson of docs/english-v2/PLAN.md ships.
FIXTURES = [(m, {"mode": m}) for m in english.MODES] + [
    ("table", {"mode": "table", "focus": "score", "show": "residue"}),
    ("questions", {"mode": "questions", "source": "wilde"}),
    ("endings", {"mode": "endings", "rule": "s", "show": "all"}),
    ("endings", {"mode": "endings", "rule": "plural", "show": "skipped"}),
    ("wordrule", {"mode": "wordrule", "list": "plurals", "rule": "r0", "show": "noplural"}),
    ("wordrule", {"mode": "wordrule", "list": "ly", "rule": "plain"}),
    ("wordrule", {"mode": "wordrule", "list": "ly", "rule": "changes", "show": "none"}),
    ("an", {"mode": "an", "rule": "sound", "source": "wilde"}),
    ("the_super", {"mode": "the_super", "rule": "most"}),
    ("time_preps", {"mode": "time_preps", "source": "austen", "show": "bare"}),
] + [("auxchain", {"mode": "auxchain", "rule": r}) for r in
     ("agree", "modal", "have", "be", "not", "boxes")] + [
    ("auxchain", {"mode": "auxchain", "rule": "have", "source": "modern"}),
    ("auxchain", {"mode": "auxchain", "rule": "be", "rules": ["be", "have"], "show": "all"}),
]


def all_courses_written():
    import importlib
    import english as package
    names = [n for n in sorted(p.name for p in (REPO_ROOT / "content" / "english").iterdir())
             if re.match(r"c\d+_", n)]
    return all(getattr(importlib.import_module("english." + n), "COURSE", None) is not None
               for n in names) and package is not None


def lessons():
    from english import PATH
    for course in PATH["courses"]:
        for lesson in course["lessons"]:
            key, cfg = lesson["lab"]
            if key == "english":
                yield course["slug"], lesson["slug"], cfg


class EveryLessonBuilds(unittest.TestCase):
    def test_every_mode_is_used_and_builds(self):
        used = set()
        for course, slug, cfg in lessons():
            with self.subTest(lesson=slug):
                lab = labs.build("english", cfg)
                used.add(cfg["mode"])
                self.assertIn("window.redrawLab", lab.script)
                self.assertTrue(lab.expect, "%s pins nothing" % slug)
        # Every mode a wired lesson uses exists; once every course of the path
        # is written (none exports COURSE = None), every mode is used.
        from mathpath.labs import english_b
        every = set(english.MODES) | set(english_b.MODES)
        self.assertLessEqual(used, every)
        if all_courses_written():
            self.assertEqual(used, every)

    def test_every_mode_is_planned_for_a_lesson(self):
        """Until the courses are wired, the manifest in docs/english-v2 is the
        list of lessons: every mode this file builds is named there."""
        manifest = json.loads((REPO_ROOT / "docs" / "english-v2" / "COURSES.json").read_text())
        planned = {lesson["lab"][1] for course in manifest for lesson in course["lessons"]}
        self.assertLessEqual(set(english.MODES), planned)

    def test_emitted_script_is_es5(self):
        for mode, cfg in FIXTURES:
            with self.subTest(mode=mode, cfg=cfg):
                code = DATA_LINE.sub("", labs.build("english", cfg).script)
                for rx, what in NOT_ES5:
                    self.assertIsNone(rx.search(code), "%s in the %s script" % (what, mode))
                self.assertNotIn("BigInt", code)

    def test_emitted_code_has_no_double_quote(self):
        """The page's one inline script holds every kit's code; a double quote
        in code (data lines are JSON and are excluded) is the landmine."""
        for mode, cfg in FIXTURES:
            with self.subTest(mode=mode, cfg=cfg):
                code = DATA_LINE.sub("", labs.build("english", cfg).script)
                self.assertNotIn('"', code)

    def test_no_network_api(self):
        for mode, cfg in FIXTURES:
            code = labs.build("english", cfg).script
            for api in ("fetch(", "XMLHttpRequest", "WebSocket", "sendBeacon", "importScripts"):
                self.assertNotIn(api, code, "%s in the %s script" % (api, mode))

    def test_every_preset_option_is_pinned(self):
        for mode, cfg in FIXTURES:
            lab = labs.build("english", cfg)
            html = lab.markup + lab.controls
            for select, options in lab.expect.items():
                with self.subTest(mode=mode, cfg=cfg, select=select):
                    menu = re.search(r'<select id="%s">(.*?)</select>' % select, html, re.S)
                    self.assertIsNotNone(menu)
                    values = re.findall(r'<option value="([^"]*)"', menu.group(1))
                    self.assertEqual(set(values), set(options))
                    for option, tiles in options.items():
                        self.assertTrue(tiles, "%s=%s pins no tile" % (select, option))
                        for tile in tiles:
                            self.assertIn('<strong id="%s">' % tile, html)

    def test_a_lesson_ships_the_preset_its_cfg_names(self):
        for mode, cfg in FIXTURES:
            key = {"endings": "rule", "wordrule": "rule", "an": "rule", "the_super": "rule",
                   "auxchain": "rule", "time_preps": "source"}.get(mode)
            if not key or key not in cfg:
                continue
            lab = labs.build("english", cfg)
            select = next(iter(lab.expect))
            with self.subTest(mode=mode, cfg=cfg):
                self.assertRegex(lab.controls, r'<select id="%s">.*?<option value="%s" selected>'
                                 % (select, re.escape(cfg[key])))

    def test_bad_cfg_is_refused(self):
        for cfg in ({"mode": "endings", "rule": "ing"}, {"mode": "wordrule", "list": "verbs"},
                    {"mode": "wordrule", "list": "ly", "show": "noplural"},
                    {"mode": "an", "source": "novel"}, {"mode": "the_super", "rule": "first"},
                    {"mode": "auxchain", "rules": ["be", "tense"]},
                    {"mode": "auxchain", "source": "novel"},
                    {"mode": "time_preps", "source": "novel"},
                    {"mode": "questions", "source": "novel"}, {"mode": "table", "focus": "both"}):
            with self.subTest(cfg=cfg):
                with self.assertRaises(ValueError):
                    labs.build("english", cfg)

    def test_tiles_use_the_shared_kpi_markup(self):
        for mode, cfg in FIXTURES:
            lab = labs.build("english", cfg)
            with self.subTest(mode=mode, cfg=cfg):
                self.assertNotIn("kpi-label", lab.markup)
                self.assertNotIn("kpi-value", lab.markup)
                # labcheck --observe reads a tile only in this exact shape.
                for tile in re.findall(r'<strong id="([^"]+)"', lab.markup):
                    self.assertRegex(lab.markup, r'<div class="kpi"><span>[^<]*</span><strong id="%s">'
                                     % tile)

    def test_table_focus_moves_the_scoring_half_up(self):
        build = labs.build("english", {"mode": "table"}).markup
        score = labs.build("english", {"mode": "table", "focus": "score"}).markup
        self.assertLess(build.index("tbGrid"), build.index("tbsTable"))
        self.assertLess(score.index("tbsTable"), score.index("tbGrid"))
        self.assertEqual(labs.build("english", {"mode": "table"}).expect,
                         labs.build("english", {"mode": "table", "focus": "score"}).expect)

    def test_irregular_and_classes_are_different_widgets(self):
        a = labs.build("english", {"mode": "irregular"})
        b = labs.build("english", {"mode": "classes"})
        self.assertNotEqual(set(a.expect), set(b.expect))
        self.assertIn("irIau", b.script)


class TheWordLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        words = REPO_ROOT / "scripts" / "wordlists"
        cls.verbs = json.loads((words / "verbrules_cases.json").read_text())
        cls.doubling = json.loads((words / "doubling_verbs.json").read_text())
        cls.irregular = json.loads(
            (REPO_ROOT / "content" / "english" / "data" / "irregular_verbs.json").read_text())

    def test_known_misspellings_and_non_verbs_are_gone(self):
        forms = {f for slot in self.verbs["cases"].values() for _b, fs in slot for f in fs}
        for bad in ("offerring", "offerred", "sufferring", "councilling", "comed", "abled"):
            self.assertNotIn(bad, forms)
        doubling = {row[0]: row for row in self.doubling["verbs"]}
        self.assertNotIn("council", doubling)
        self.assertEqual(doubling["offer"][2], 0)
        self.assertEqual(doubling["suffer"][2], 0)
        self.assertEqual(doubling["offer"][4], "offerring")

    def test_every_exclusion_has_a_reason(self):
        for name in ("verbs", "doubling"):
            excluded = getattr(self, name)["excluded"]
            self.assertTrue(excluded)
            for word, why in excluded.items():
                self.assertTrue(why.strip(), word)

    def test_no_irregular_verb_is_scored_as_regular(self):
        bases = {v["base"] for v in self.irregular["verbs"]}
        self.assertFalse(bases & set(self.verbs["stress"]))

    def test_computed_classes_match_the_data_labels(self):
        def cls(v):
            b, p, q = v["base"], v["past"], v["pp"]
            if "/" in p or "/" in q:
                return "no_class_handcoded"
            if b == p == q:
                return "all_same"
            if p == q:
                return "past_eq_pp"
            if b == q:
                return "base_eq_pp"
            if b == p:
                return "base_eq_past"
            return "all_diff_n" if q.endswith("n") else "all_diff_other"
        for v in self.irregular["verbs"]:
            self.assertEqual(cls(v), v["class"], v["base"])


class RefusesBadInput(unittest.TestCase):
    STUB = r"""
const els = {};
const mk = (id) => els[id] || (els[id] = {id, value: id === 'tbVerb' ? 'walk' : '',
  textContent: '', innerHTML: '', style: {}, addEventListener() {}});
global.document = {getElementById: mk}; global.window = global;
eval(require('fs').readFileSync(0, 'utf8'));
const out = {};
for (const v of ['123', 'running fast', 'stop']) {
  mk('tbVerb').value = v; window.redrawLab();
  out[v] = [els.tbIng.textContent, els.tbRule.textContent];
}
console.log(JSON.stringify(out));
"""

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_table_lab_refuses_rather_than_cleans(self):
        script = labs.build("english", {"mode": "table"}).script
        run = subprocess.run(["node", "-e", self.STUB], input=script, capture_output=True,
                             text=True, timeout=30, check=True)
        out = json.loads(run.stdout)
        for bad in ("123", "running fast"):
            self.assertEqual(out[bad][0], "—", bad)
            self.assertIn("not one word", out[bad][1])
        self.assertEqual(out["stop"][0], "stopping")


WORDLISTS = REPO_ROOT / "scripts" / "wordlists"
SOURCES = REPO_ROOT / "docs" / "english-v2" / "measure" / "data"


class TheDerivedDataIsCurrent(unittest.TestCase):
    """Every data file the second instalment reads is written by a committed
    script; --check rebuilds it from the pinned sources and fails on any
    difference. The sources are downloaded (docs/english-v2/measure/fetch.sh)
    and never committed, so without them the check is skipped, loudly."""

    def check(self, script, needs_sources=True):
        if needs_sources and not (SOURCES / "cmudict.dict").exists():
            self.skipTest("the pinned sources are not in %s; run fetch.sh" % SOURCES)
        run = subprocess.run([sys.executable, str(WORDLISTS / script), "--check"],
                             capture_output=True, text=True, timeout=120)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_clean_verbs(self):
        self.check("clean_verbs.py", needs_sources=False)

    def test_clean_nouns(self):
        self.check("clean_nouns.py")

    def test_clean_adjectives(self):
        self.check("clean_adjectives.py")

    def test_concordance(self):
        self.check("concordance.py")

    def test_sounds(self):
        self.check("sounds.py")

    def test_the_cmudict_notice_travels_with_the_data(self):
        notice = (WORDLISTS / "CMUDICT_LICENSE").read_text()
        self.assertIn("Carnegie Mellon University", notice)
        for name in ("verb_sounds.json", "an_sounds.json"):
            self.assertIn("CMUDICT_LICENSE", json.loads((WORDLISTS / name).read_text())["note"])

    def test_every_data_file_names_its_sources(self):
        data = REPO_ROOT / "content" / "english" / "data"
        for path in [WORDLISTS / n for n in ("plural_nouns.json", "ly_adjectives.json",
                                             "verb_sounds.json", "an_sounds.json")] + [
                data / n for n in ("long_passage.json", "wilde_questions.json",
                                   "question_concordance.json", "an_concordance.json",
                                   "superlative_concordance.json", "time_concordance.json")]:
            with self.subTest(file=path.name):
                obj = json.loads(path.read_text())
                self.assertTrue(obj["note"].strip())
                self.assertTrue(all(re.search(r"sha256 [0-9a-f]{64}$", s) for s in obj["sources"]))

    def test_the_question_lines_start_where_their_sentences_start(self):
        q = json.loads((REPO_ROOT / "content" / "english" / "data"
                        / "question_concordance.json").read_text())
        self.assertEqual(len(q["questions"]), 90)
        for line in q["questions"]:
            self.assertRegex(line, r"^[A-Za-z]", line)
            self.assertNotIn("_", line)
        self.assertIn("Your father\u2019s estate is entailed on Mr. Collins, I think?", q["questions"])


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class TheHarnessAgreesWithThePins(unittest.TestCase):
    """scripts/wordlists/english_check.js runs the shipped rule blocks on the
    shipped data. Its figures must be the ones the presets pin."""

    @classmethod
    def setUpClass(cls):
        run = subprocess.run(["node", str(WORDLISTS / "english_check.js")], capture_output=True,
                             text=True, timeout=60, check=True)
        cls.blocks, title = {}, None
        for line in run.stdout.splitlines():
            if not line.startswith("  "):
                title = line.strip()
                cls.blocks[title] = {}
            else:
                k, v = line.strip().split(" ", 1)
                cls.blocks[title][k] = v.strip()

    def agree(self, title, expect):
        got = self.blocks[title]
        for tile, text in expect.items():
            self.assertEqual(got.get(tile), text, "%s: %s" % (title, tile))

    def test_the_new_modes(self):
        names = {
            "endings": lambda o, cfg: "endings " + o,
            "the_super": lambda o, cfg: "the_super " + o,
            "time_preps": lambda o, cfg: "time_preps " + o,
            "an": lambda o, cfg: "an %s / %s" % (o, cfg.get("source", "all")),
            "auxchain": lambda o, cfg: "auxchain %s / %s" % (o, cfg.get("source", "chapter")),
            "wordrule": lambda o, cfg: "wordrule %s %s" % (cfg.get("list", "plurals"), o),
        }
        for mode, cfg in FIXTURES:
            if mode not in names:
                continue
            lab = labs.build("english", cfg)
            for select, options in lab.expect.items():
                for option, tiles in options.items():
                    with self.subTest(mode=mode, cfg=cfg, option=option):
                        self.agree(names[mode](option, cfg), tiles)

    def test_questions(self):
        for source in ("austen", "wilde"):
            lab = labs.build("english", {"mode": "questions", "source": source})
            self.agree("questions " + source, lab.expect["quPreset"]["aux"])


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class TheTokeniser(unittest.TestCase):
    def test_typographic_apostrophes_are_part_of_the_word(self):
        from mathpath.labs.english_core import SCAN_JS
        js = SCAN_JS + r"""
console.log(JSON.stringify([wordsOf('I don\u2019t know the Bennets\u2019 aunt\u2019s house'),
                            tokensOf('in 1813, at eight o\u2019clock')]));"""
        out = json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True,
                                        timeout=30, check=True).stdout)
        self.assertEqual(out[0], ["I", "don't", "know", "the", "Bennets", "aunt's", "house"])
        self.assertEqual(out[1], ["in", "1813", "at", "eight", "o'clock"])


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class TheEndingsLabRefuses(unittest.TestCase):
    STUB = r"""
const els = {};
const mk = (id) => els[id] || (els[id] = {id, value: id === 'enPreset' ? 'ed' :
  (id === 'enShow' ? 'misses' : 'walk'), textContent: '', innerHTML: '', style: {},
  addEventListener() {}});
global.document = {getElementById: mk}; global.window = global;
eval(require('fs').readFileSync(0, 'utf8'));
const out = {};
for (const v of ['', 'banana', '0', '1/0', 'A>B', 'two words', 'walk']) {
  mk('enWord').value = v; window.redrawLab(); out[v] = els.enWordSays.textContent;
}
console.log(JSON.stringify(out));
"""

    def test_a_word_off_the_list_is_refused_by_name(self):
        script = labs.build("english", {"mode": "endings"}).script
        out = json.loads(subprocess.run(["node", "-e", self.STUB], input=script,
                                        capture_output=True, text=True, timeout=30,
                                        check=True).stdout)
        self.assertEqual(out["banana"], "not on the printed list: the page cannot hear it")
        for bad in ("0", "1/0", "A>B", "two words"):
            self.assertIn("not one word", out[bad])
        self.assertIn("type a word", out[""])
        self.assertIn("walked ends in t", out["walk"])


if __name__ == "__main__":
    unittest.main()
