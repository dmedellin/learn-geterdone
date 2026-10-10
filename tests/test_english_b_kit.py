"""english_b, the second half of the English Subject's kit: every mode builds
under every cfg a lesson can give it, emits ES5 with no double-quote character,
pins every option of every preset menu, and carries derived facts rather than
the dictionaries they came from.

No browser. Whether the pinned figures are RIGHT is scripts/labcheck.js's job
on a rendered page; whether the data files are current is
scripts/wordlists/b_sounds.py --check and b_concordance.py --check, run here
when the downloaded sources are present.

    /usr/bin/python3 -m unittest tests.test_english_b_kit -v
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
from mathpath.labs import english_b  # noqa: E402

MODES = {"compare", "phrasal", "letters", "stress", "contractions", "linking", "coverage"}

# Every cfg a lesson in docs/english-v2/PLAN.md section C gives these modes,
# plus each mode bare and each redraw-only choice a lesson could ship.
CFGS = [
    {"mode": "compare"}, {"mode": "compare", "rule": "B"},
    {"mode": "compare", "source": "wilde", "show": "aside"},
    {"mode": "compare", "source": "modern", "rule": "B", "show": "all"},
    {"mode": "phrasal"}, {"mode": "phrasal", "rule": "freq"},
    {"mode": "phrasal", "rule": "freq", "source": "wilde"},
    {"mode": "letters"},
    {"mode": "letters", "rules": ["softc", "softg"]},
    {"mode": "letters", "rules": ["magic", "magic_r"]},
    {"mode": "letters", "rules": ["ie", "ie_ee"]},
    {"mode": "letters", "rules": ["gh", "kn_wr_mb", "h", "ough"], "show": "aside"},
    {"mode": "letters", "rules": ["tion", "sion", "ture", "cial"]},
    {"mode": "stress"},
    {"mode": "stress", "rules": ["nouns2", "verbs2", "adj2", "pairs"]},
    {"mode": "stress", "rules": ["tion", "ic", "ical", "ity", "ate", "ize", "ee"]},
    {"mode": "stress", "rules": ["ly", "ness", "ment", "er", "ful", "able"]},
    {"mode": "stress", "rules": ["schwa"], "show": "all"},
    {"mode": "contractions"}, {"mode": "contractions", "source": "austen"},
    {"mode": "contractions", "source": "modern"},
    {"mode": "linking"}, {"mode": "linking", "rule": "vv"}, {"mode": "linking", "rule": "same"},
    {"mode": "coverage"}, {"mode": "coverage", "show": "top"},
    {"mode": "coverage", "show": "family"}, {"mode": "coverage", "text": "own"},
]

NOT_ES5 = [
    (re.compile(r"=>"), "arrow function"),
    (re.compile(r"(^|[\s;{(])(let|const)\s"), "let/const"),
    (re.compile(r"`"), "template literal"),
    (re.compile(r"\?\."), "optional chaining"),
    (re.compile(r"\?\?"), "nullish coalescing"),
    (re.compile(r"\(\?<[=!]"), "lookbehind"),
    (re.compile(r"\b\d+n\b"), "BigInt literal"),
]
# The data lines english_b._lit writes, by name: stripped before the ES5 scan
# because they hold printed English, where "let me" is words, not syntax.
DATA_NAMES = ("CP_DATA", "PH_DATA", "LT_DATA", "ST_DATA", "MODERN", "CO_TEXTS", "LK_SOUNDS",
              "LK_TEXT", "CV_HEADS", "CV_IRR", "CV_TEXTS")
DATA_LINE = re.compile(r"^  var (?:%s) = .*;$" % "|".join(DATA_NAMES), re.M)
# The site's copy guards read "course 1" or "lesson 2 of 5" anywhere in a page
# as a curricular number, inline data included (tests/test_course_ui.py).
ORDINAL = re.compile(r"(?i)\bcourse\s+\d|\bcourses\s+\d+\s+(?:and|to|through)\s+\d+|\blesson\s+\d+\s+of\s+\d+")


def build(cfg):
    return labs.build("english", cfg)


class EveryModeBuilds(unittest.TestCase):
    def test_the_seven_modes_are_served(self):
        self.assertEqual(set(english_b.MODES), MODES)
        self.assertEqual({c["mode"] for c in CFGS}, MODES)

    def test_every_cfg_builds_and_redraws(self):
        for cfg in CFGS:
            with self.subTest(cfg=cfg):
                lab = build(cfg)
                self.assertIn("window.redrawLab", lab.script)
                self.assertTrue(lab.expect)

    def test_a_bad_cfg_is_refused(self):
        for cfg in ({"mode": "compare", "rule": "C"}, {"mode": "letters", "rules": ["nope"]},
                    {"mode": "coverage", "text": "novel"}, {"mode": "phrasal", "source": "modern"}):
            with self.subTest(cfg=cfg):
                with self.assertRaises(ValueError):
                    build(cfg)


class TheScriptContract(unittest.TestCase):
    def test_es5_only(self):
        for cfg in CFGS:
            code = DATA_LINE.sub("", build(cfg).script)
            for rx, what in NOT_ES5:
                with self.subTest(cfg=cfg, construct=what):
                    self.assertIsNone(rx.search(code))

    def test_no_double_quote_anywhere_in_the_script(self):
        for cfg in CFGS:
            with self.subTest(cfg=cfg):
                self.assertNotIn('"', build(cfg).script)

    def test_data_lines_are_single_line_literals(self):
        for cfg in CFGS:
            script = build(cfg).script
            for line in script.splitlines():
                name = re.match(r"^  var ([A-Z_]+) = ", line)
                if name and name.group(1) in DATA_NAMES:
                    with self.subTest(cfg=cfg, line=line[:40]):
                        self.assertTrue(DATA_LINE.match(line))
                        self.assertNotIn("</", line)

    def test_no_curricular_number_in_the_script(self):
        for cfg in CFGS:
            with self.subTest(cfg=cfg):
                self.assertIsNone(ORDINAL.search(build(cfg).script))

    def test_no_network(self):
        for cfg in CFGS:
            script = build(cfg).script
            for api in ("fetch(", "XMLHttpRequest", "WebSocket", "sendBeacon", "import("):
                with self.subTest(cfg=cfg, api=api):
                    self.assertNotIn(api, script)

    def test_the_literal_writer_round_trips(self):
        value = {"a": ["it’s", "say \"no\"", "</script>", "back\\slash", "line\nbreak"],
                 "n": [1, 2.5, None, True]}
        if shutil.which("node"):
            out = subprocess.run(["node", "-e", "var x = %s; console.log(JSON.stringify(x));"
                                  % english_b._js(value)], capture_output=True, text=True,
                                 check=True, timeout=30)
            self.assertEqual(json.loads(out.stdout), value)
        self.assertNotIn('"', english_b._js(value))
        self.assertNotIn("</", english_b._js(value))


class EveryPresetIsPinned(unittest.TestCase):
    def test_every_option_of_every_declared_menu_pins_a_tile(self):
        for cfg in CFGS:
            lab = build(cfg)
            html = lab.markup + lab.controls
            for select, options in lab.expect.items():
                with self.subTest(cfg=cfg, select=select):
                    menu = re.search(r'<select id="%s">(.*?)</select>' % select, html, re.S)
                    self.assertIsNotNone(menu)
                    values = re.findall(r'<option value="([^"]*)"', menu.group(1))
                    self.assertEqual(set(values), set(options))
                    for option, tiles in options.items():
                        self.assertTrue(tiles, "%s=%s pins no tile" % (select, option))
                        for tile in tiles:
                            self.assertIn('<strong id="%s">' % tile, html)

    def test_the_preset_menu_is_named_xx_preset(self):
        for cfg in CFGS:
            lab = build(cfg)
            with self.subTest(cfg=cfg):
                self.assertTrue(any(s.endswith("Preset") for s in lab.expect))

    def test_a_restricted_menu_shows_only_its_rules(self):
        lab = build({"mode": "letters", "rules": ["tion", "sion"]})
        menu = re.search(r'<select id="ltPreset">(.*?)</select>', lab.controls, re.S).group(1)
        self.assertEqual(re.findall(r'<option value="([^"]*)"', menu), ["tion", "sion"])
        self.assertNotIn("softc", lab.script.split("LT_DATA = ", 1)[1].split(";\n", 1)[0])

    def test_the_shipped_choice_is_selected(self):
        lab = build({"mode": "compare", "source": "wilde", "rule": "B"})
        self.assertIn('<option value="wilde" selected="selected">', lab.controls)
        self.assertIn('<option value="B" selected="selected">', lab.controls)
        self.assertEqual(lab.expect["cpPreset"]["wilde"], lab.expect["cpRule"]["B"])


class TheData(unittest.TestCase):
    CMU_MODES = ({"mode": "compare"}, {"mode": "letters"}, {"mode": "stress"}, {"mode": "linking"})

    def test_cmudict_notice_travels_with_its_facts(self):
        notice = (REPO_ROOT / "scripts" / "wordlists" / "b_CMUDICT_LICENSE").read_text()
        self.assertIn("Carnegie Mellon University", notice)
        for cfg in self.CMU_MODES:
            with self.subTest(cfg=cfg):
                self.assertIn("Copyright (C) 1993-2015 Carnegie Mellon University", build(cfg).markup)
        for name in ("b_letters.json", "b_stress.json", "b_passage_sounds.json"):
            note = json.loads((REPO_ROOT / "scripts" / "wordlists" / name).read_text())["note"]
            self.assertIn("b_CMUDICT_LICENSE", note, name)

    def test_no_dictionary_symbols_or_moby_tags_are_shipped_as_lists(self):
        letters = json.loads((REPO_ROOT / "scripts" / "wordlists" / "b_letters.json").read_text())
        for rule, d in letters["rules"].items():
            for row in d["rows"]:
                with self.subTest(rule=rule, row=row):
                    self.assertFalse(any(re.fullmatch(r"[A-Z]{1,2}[0-2]?", str(x)) for x in row))
        for cfg in CFGS:
            self.assertNotIn("mobypos", build(cfg).script)

    def test_every_set_aside_has_a_reason(self):
        for name in ("b_letters.json", "b_stress.json"):
            for rule, d in json.loads((REPO_ROOT / "scripts" / "wordlists" / name).read_text())["rules"].items():
                for why, words in d["aside"].items():
                    with self.subTest(file=name, rule=rule):
                        self.assertTrue(why.strip())
                        self.assertTrue(words)

    def test_the_excerpt_is_the_planned_cut(self):
        d = json.loads((REPO_ROOT / "content" / "english" / "data" / "b_wilde_excerpt.json").read_text())
        self.assertTrue(d["text"].startswith("CECILY. Oh, I merely came back to water the roses."))
        self.assertTrue(d["text"].endswith("if I may speak candidly—"))
        self.assertEqual(d["words"], 1975)

    @unittest.skipUnless((REPO_ROOT / "docs" / "english-v2" / "measure" / "data" / "cmudict.dict").exists(),
                         "the downloaded sources are absent (docs/english-v2/measure/fetch.sh)")
    def test_the_data_files_are_current(self):
        for script in ("b_sounds.py", "b_concordance.py"):
            with self.subTest(script=script):
                run = subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "wordlists" / script),
                                      "--check"], capture_output=True, text=True, timeout=300,
                                     cwd=str(REPO_ROOT / "scripts" / "wordlists"))
                self.assertEqual(run.returncode, 0, run.stdout + run.stderr)


class RefusesBadInput(unittest.TestCase):
    STUB = r"""
var els = {};
function mk(id) {
  if (!els[id]) els[id] = {id: id, value: '', textContent: '', innerHTML: '', style: {},
                           addEventListener: function () {}};
  return els[id];
}
global.document = {getElementById: mk}; global.window = global;
var src = require('fs').readFileSync(0, 'utf8');
mk('cvPreset').value = 'own'; mk('cvShow').value = 'bands';
eval(src);
var out = {};
['', 'banana', '0', '-1', '1/0', 'A>B', 'one two three'].forEach(function (v) {
  mk('cvOwn').value = v; window.redrawLab();
  out[v] = [els.cvB3.textContent, els.cvN.textContent, els.cvLimit.textContent];
});
var long = []; for (var i = 0; i < 60; i++) long.push('the cat sat on the mat');
mk('cvOwn').value = long.join(' '); window.redrawLab();
out.long = [els.cvB3.textContent, els.cvN.textContent];
console.log(JSON.stringify(out));
"""

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_coverage_refuses_a_short_text(self):
        script = build({"mode": "coverage", "text": "own"}).script
        run = subprocess.run(["node", "-e", self.STUB], input=script, capture_output=True,
                             text=True, timeout=60, check=True)
        out = json.loads(run.stdout)
        for bad in ("", "banana", "0", "-1", "1/0", "A>B", "one two three"):
            self.assertEqual(out[bad][0], "—", bad)
            self.assertEqual(out[bad][1], "—", bad)
            self.assertIn("fifty words", out[bad][2])
        self.assertEqual(out["long"][1], "360")
        self.assertRegex(out["long"][0], r"^\d+\.\d%$")


if __name__ == "__main__":
    unittest.main()
