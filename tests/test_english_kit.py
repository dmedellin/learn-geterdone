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
        self.assertEqual(used, set(english.MODES))

    def test_emitted_script_is_es5(self):
        for mode in english.MODES:
            with self.subTest(mode=mode):
                code = DATA_LINE.sub("", labs.build("english", {"mode": mode}).script)
                for rx, what in NOT_ES5:
                    self.assertIsNone(rx.search(code), "%s in the %s script" % (what, mode))
                self.assertNotIn("BigInt", code)

    def test_every_preset_option_is_pinned(self):
        for mode in english.MODES:
            lab = labs.build("english", {"mode": mode})
            html = lab.markup + lab.controls
            for select, options in lab.expect.items():
                with self.subTest(mode=mode, select=select):
                    menu = re.search(r'<select id="%s">(.*?)</select>' % select, html, re.S)
                    self.assertIsNotNone(menu)
                    values = re.findall(r'<option value="([^"]*)"', menu.group(1))
                    self.assertEqual(set(values), set(options))
                    for option, tiles in options.items():
                        self.assertTrue(tiles, "%s=%s pins no tile" % (select, option))
                        for tile in tiles:
                            self.assertIn('<strong id="%s">' % tile, html)

    def test_tiles_use_the_shared_kpi_markup(self):
        for mode in english.MODES:
            lab = labs.build("english", {"mode": mode})
            with self.subTest(mode=mode):
                self.assertNotIn("kpi-label", lab.markup)
                self.assertNotIn("kpi-value", lab.markup)

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


if __name__ == "__main__":
    unittest.main()
