"""calckit builds every mode with the presets docs/differential-equations/PLAN.md section C sketches.

Fast and browserless. Every fixture is built through labs.build("calckit", cfg)
and the markup and script are checked for the controls, tiles and wiring D.2
names, for ES5, and for the absence of a double quote in everything de_core
and calckit add to a page. The arithmetic is checked by running the shipped
JavaScript blocks under node (skipped when node is absent): the de_core cases
D.1 asks for first, and figures from section C's worked lines, each worked by
hand. The `expect` figures below were read off rendered fixture pages with
`node scripts/labcheck.js --observe` and checked by hand against section C;
FIXTURES is importable, so a fixture page can be rendered and gated by
labcheck.js --expect.
"""

import os
import re
import shutil
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from mathpath import labs  # noqa: E402
from mathpath.labs import calckit, de_core  # noqa: E402


def _p(pid, expect=None, **fields):
    out = {"id": pid, "label": pid.replace("-", " ")}
    out.update(fields)
    out["expect"] = expect or {}
    return out


# (section C lesson, cfg). One entry per lesson that uses calckit.
FIXTURES = [
    ("1.1", {"mode": "quotient", "show_limit": False, "presets": [
        _p("square", {"qtFirst": "3", "qtLast": "33/16"}, f="t^2", a=1, h=1, halvings=4),
        _p("cubic", {"qtFirst": "18", "qtLast": "2913/256"}, f="t^3 - t", a=2, h=1, halvings=4),
        _p("line", {"qtFirst": "3", "qtLast": "3"}, f="3t + 1", a=5, h=1, halvings=4)]}),
    ("1.2", {"mode": "hpoly", "presets": [
        _p("square", {"hpQ": "2t + h", "hpConst": "2t"}, kind="single", f="t^2", g=None, a=None),
        _p("cube", {"hpQ": "3t² + 3th + h²", "hpConst": "3t²"}, kind="single", f="t^3", g=None, a=None),
        _p("quartic", {"hpQ": "4t³ − 4t + 6t²h − 2h + 4th² + h³", "hpConst": "4t³ − 4t"},
           kind="single", f="t^4 - 2t^2", g=None, a=None)]}),
    ("1.3", {"mode": "quotient", "presets": [
        _p("square", {"qtLast": "129/64", "qtGap": "1/64", "qtLimit": "2"}, f="t^2", a=1, h=1, halvings=6),
        _p("cube", {"qtLast": "12481/4096", "qtGap": "193/4096", "qtLimit": "3"}, f="t^3", a=1, h=1, halvings=6),
        _p("flat", {"qtLast": "1/64", "qtGap": "1/64", "qtLimit": "0"}, f="t^2", a=0, h=1, halvings=6)]}),
    ("1.4", {"mode": "tangent", "presets": [
        _p("square", {"tgSlope": "4", "tgLine": "y = 4t − 4", "tgError": "1/100"}, f="t^2", a=2, h="1/10"),
        _p("cube", {"tgSlope": "3", "tgLine": "y = 3t − 2", "tgError": "31/1000"}, f="t^3", a=1, h="1/10"),
        _p("recip", {"tgSlope": "−1", "tgLine": "y = −t + 2", "tgApprox": "1/2", "tgTrue": "2/3",
                     "tgError": "1/6"}, f="1/t", a=1, h="1/2")]}),
    ("1.5", {"mode": "quotient", "presets": [
        _p("two", {"qtFirst": "−1/6", "qtLast": "−16/65", "qtLimit": "−1/4"}, f="1/t", a=2, h=1, halvings=5),
        _p("one", {"qtFirst": "−1/2", "qtLast": "−32/33", "qtLimit": "−1"}, f="1/t", a=1, h=1, halvings=5),
        _p("half", {"qtFirst": "−4/3", "qtLast": "−64/17", "qtLimit": "−4"}, f="1/t", a="1/2", h=1, halvings=5)]}),
    ("1.6", {"mode": "derivative", "order": 1, "presets": [
        _p("hill", {"dvDeriv": "3t² − 12t + 9", "dvZeros": "1, 3"}, f="t^3 - 6t^2 + 9t"),
        _p("bowl", {"dvDeriv": "2t − 4", "dvZeros": "2"}, f="t^2 - 4t"),
        _p("wave", {"dvDeriv": "4t³ − 4t", "dvZeros": "−1, 0, 1"}, f="t^4 - 2t^2")]}),
    ("1.7", {"mode": "derivative", "order": 1, "presets": [
        _p("two-turns", {"dvZeros": "−1, 2", "dvIntervals": "rising t < −1; falling −1 < t < 2; rising t > 2"},
           f="2t^3 - 3t^2 - 12t + 1"),
        _p("flat-step", {"dvZeros": "0 (no sign change)", "dvIntervals": "rising t < 0; rising t > 0"}, f="t^3"),
        _p("none", {"dvZeros": "none rational", "dvIntervals": "rising for every t"}, f="t^3 + t")]}),
    ("1.8", {"mode": "hpoly", "presets": [
        _p("basic", {"hpConst": "3t² + 2t", "hpRule": "f′g + fg′ = 3t² + 2t; f′g′ = 2t", "hpEqual": "equal"},
           kind="product", f="t^2", g="t + 1", a=None),
        _p("wrong-rule", {"hpRule": "f′g + fg′ = 3t² + 2t; f′g′ = 2t", "hpEqual": "equal", "hpAt": "353/64"},
           kind="product", f="t^2", g="t + 1", a=1),
        _p("cubic", {"hpConst": "5t⁴ + 3t² − 2", "hpRule": "f′g + fg′ = 5t⁴ + 3t² − 2; f′g′ = 6t³ − 2t",
                     "hpEqual": "equal"}, kind="product", f="t^3 - t", g="t^2 + 2", a=None)]}),
    ("1.9", {"mode": "hpoly", "presets": [
        _p("stretch", {"hpConst": "18t + 6", "hpRule": "18t + 6", "hpEqual": "equal"},
           kind="compose", f="t^2", g="3t + 1", a=None),
        _p("power", {"hpConst": "6t⁵ + 12t³ + 6t", "hpRule": "6t⁵ + 12t³ + 6t", "hpEqual": "equal"},
           kind="compose", f="t^3", g="t^2 + 1", a=None),
        _p("shift", {"hpConst": "2t − 8", "hpRule": "2t − 8", "hpEqual": "equal"},
           kind="compose", f="t^2", g="t - 4", a=None)]}),
    ("1.10", {"mode": "derivative", "order": 2, "presets": [
        _p("s-curve", {"dvSecond": "6t − 6", "dvInflect": "t = 1"}, f="t^3 - 3t^2", window=[-1, 3]),
        _p("quartic", {"dvSecond": "12t² − 12", "dvInflect": "t = −1, 1"}, f="t^4 - 6t^2"),
        _p("parabola", {"dvSecond": "2", "dvInflect": "none"}, f="t^2")]}),
    ("1.11", {"mode": "transcendental", "presets": [
        _p("two", {"tqFirst": "1", "tqLimit": "ln 2 ≈ 0.693147", "tqRatio": "≈ 0.696914"},
           kind="exp", b=2, a=0, h=1, halvings=6),
        _p("three", {"tqFirst": "2", "tqLimit": "ln 3 ≈ 1.09861", "tqRatio": "≈ 1.1081"},
           kind="exp", b=3, a=0, h=1, halvings=6),
        _p("e", {"tqFirst": "≈ 1.71828", "tqLimit": "ln e = 1", "tqRatio": "≈ 1.00785"},
           kind="exp", b="e", a=0, h=1, halvings=6)]}),
    ("2.1", {"mode": "riemann", "rule": "left", "presets": [
        _p("ramp", {"rsSum": "3", "rsExact": "4"}, f="2t", a=0, b=2, n=4),
        _p("speed", {"rsSum": "8", "rsExact": "12"}, f="t^2 + 1", a=0, b=3, n=3),
        _p("constant", {"rsSum": "12", "rsExact": "12"}, f="3", a=1, b=5, n=4)]}),
    ("2.2", {"mode": "riemann", "rule": "left", "presets": [
        _p("ramp", {"rsSum": "3", "rsGap": "2"}, f="2t", a=0, b=2, n=4),
        _p("square", {"rsSum": "7/32", "rsGap": "1/4"}, f="t^2", a=0, b=1, n=4),
        _p("falling", {"rsSum": "13/2", "rsGap": "−1"}, f="4 - t", a=0, b=2, n=4)]}),
    ("2.3", {"mode": "riemann", "rule": "left", "presets": [
        _p("square", {"rsSum": "7/32", "rsError": "−11/96", "rsRatio": "44/23"}, f="t^2", a=0, b=1, n=4),
        _p("cubic", {"rsSum": "9/4", "rsError": "−7/4", "rsRatio": "28/15"}, f="t^3", a=0, b=2, n=4),
        _p("ramp", {"rsSum": "3", "rsError": "−1", "rsRatio": "2"}, f="2t", a=0, b=2, n=4)]}),
    # `mid` is the midpoint instance, but rsRule is redraw-only and ships `trap`,
    # so its expectation pins what the page prints under `trap` (rule 6); the
    # midpoint figures (21/64, error −1/192) belong in the lesson prose.
    ("2.4", {"mode": "riemann", "rule": "trap", "presets": [
        _p("trap", {"rsSum": "11/32", "rsError": "1/96", "rsRatio": "4"}, f="t^2", a=0, b=1, n=4),
        _p("mid", {"rsSum": "11/32", "rsError": "1/96", "rsRatio": "4"}, f="t^2", a=0, b=1, n=4),
        _p("quartic", {"rsSum": "113/512", "rsError": "53/2560", "rsRatio": "848/213"}, f="t^4", a=0, b=1, n=4)]}),
    ("2.5", {"mode": "antiderivative", "presets": [
        _p("square", {"adF": "t³/3 + C", "adDefinite": "1/3"}, f="t^2", a=0, b=1),
        _p("ramp", {"adF": "t² + C", "adDefinite": "4"}, f="2t", a=0, b=2),
        _p("mixed", {"adF": "t³ − 2t² + t + C", "adDefinite": "12"}, f="3t^2 - 4t + 1", a=1, b=3)]}),
    ("2.6", {"mode": "antiderivative", "presets": [
        _p("through-five", {"adF": "t² + C", "adC": "4"}, f="2t", ic=[1, 5]),
        _p("through-zero", {"adF": "t³ + C", "adC": "−8"}, f="3t^2", ic=[2, 0]),
        _p("cubic", {"adF": "t⁴/4 − t²/2 + C", "adC": "1/2"}, f="t^3 - t", ic=[0, "1/2"])]}),
    ("2.7", {"mode": "antiderivative", "presets": [
        _p("linear", {"adDefinite": "8", "adLinear": "equal: 12 = 8 + 4"},
           f="3t^2", g="2t", coeffs=[1, 1], a=0, b=2),
        _p("scaled", {"adDefinite": "1/3", "adLinear": "equal: 1 = 2 − 1"},
           f="t^2", g="t", coeffs=[6, -2], a=0, b=1),
        _p("split", {"adDefinite": "12", "adSplit": "equal: 12 = 2 + 10"}, f="3t^2 + 2t", a=0, b=2, split=1)]}),
    ("2.8", {"mode": "riemann", "rule": "left", "presets": [
        _p("ln2", {"rsSum": "319/420", "rsExact": "≈ 0.693147 (ln 2, rounded)"}, f="1/t", a=1, b=2, n=4),
        _p("ln4", {"rsSum": "223/140", "rsExact": "≈ 1.38629 (ln 4, rounded)"}, f="1/t", a=1, b=4, n=6),
        _p("ln3", {"rsSum": "77/60", "rsExact": "≈ 1.09861 (ln 3, rounded)"}, f="1/t", a=1, b=3, n=4)]}),
    ("7.1", {"mode": "transcendental", "presets": [
        _p("sin-at-zero", {"tqLast": "≈ 0.999959", "tqLimit": "cos(0) = 1"}, kind="sin", a=0, h=1, halvings=6),
        _p("cos-at-zero", {"tqLast": "≈ −0.00781234", "tqLimit": "−sin(0) = 0"}, kind="cos", a=0, h=1, halvings=6),
        _p("sin-at-one", {"tqLast": "≈ 0.533706", "tqLimit": "cos(1) ≈ 0.540302"}, kind="sin", a=1, h=1, halvings=6)]}),
]

TILES = {
    "quotient": ("qtPreset", ["qtFirst", "qtLast"], "qtStatus"),
    "hpoly": ("hpPreset", ["hpQ", "hpConst", "hpRule", "hpEqual", "hpAt"], "hpStatus"),
    "tangent": ("tgPreset", ["tgValue", "tgSlope", "tgApprox", "tgTrue", "tgError", "tgLine"], "tgStatus"),
    "derivative": ("dvPreset", ["dvDeriv", "dvSecond", "dvZeros", "dvIntervals", "dvInflect"], "dvStatus"),
    "transcendental": ("tqPreset", ["tqFirst", "tqLast", "tqLimit", "tqRatio"], "tqStatus"),
    "riemann": ("rsPreset", ["rsSum", "rsSumDec", "rsExact", "rsError", "rsGap", "rsRatio"], "rsStatus"),
    "antiderivative": ("adPreset", ["adF", "adC", "adDefinite", "adLinear", "adSplit"], "adStatus"),
}

# ES5: one inline <script> carries every lab and the quiz, so a construct an
# older parser rejects kills the page. BigInt literals are allowed, as
# RATIONAL_JS uses them.
NOT_ES5 = [
    (re.compile(r"=>"), "arrow function"),
    (re.compile(r"(^|[\s;{(])(let|const)\s"), "let/const"),
    (re.compile(r"\bclass\s+[A-Za-z_$][\w$]*\s*(extends\b|\{)"), "class"),
    (re.compile(r"`"), "template literal"),
    (re.compile(r"\?\."), "optional chaining"),
    (re.compile(r"\?\?"), "nullish coalescing"),
    (re.compile(r"\(\?<[=!]"), "lookbehind"),
    (re.compile(r"\.\.\.[A-Za-z_\[]"), "spread"),
    (re.compile(r"\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon|importScripts)\b"), "network"),
]


def build(cfg, **extra):
    return labs.build("calckit", dict(cfg, **extra))


def own_script(script):
    """What de_core and calckit add to a page: the script with algebra_core's
    blocks, which predate the no-double-quote rule, taken out."""
    for block in de_core.ALGEBRA_BLOCKS:
        script = script.replace(block, "")
    return script


class EveryLessonBuilds(unittest.TestCase):
    def test_every_mode_is_covered(self):
        self.assertEqual({cfg["mode"] for _, cfg in FIXTURES}, set(calckit.MODES))

    def test_every_section_c_lesson(self):
        for key, cfg in FIXTURES:
            mode = cfg["mode"]
            with self.subTest(lesson=key, mode=mode):
                lab = build(cfg)
                select, tiles, status = TILES[mode]
                html = lab.markup + lab.controls
                self.assertIn('id="%s"' % select, html)
                for tile in tiles:
                    self.assertIn('<strong id="%s">' % tile, html)
                self.assertIn('id="%s"' % status, html)
                for p in cfg["presets"]:
                    self.assertIn('<option value="%s"' % p["id"], html)
                self.assertEqual(set(lab.expect), {select})
                self.assertEqual(set(lab.expect[select]), {p["id"] for p in cfg["presets"]})
                for p in cfg["presets"]:
                    for tile in p["expect"]:
                        self.assertIn('<strong id="%s">' % tile, html, "%s pins a tile the page lacks" % p["id"])
                self.assertIn("window.redrawLab = redraw", lab.script)
                self.assertIn("DE_refuse(", lab.script)
                ids = re.findall(r'\bid="([^"]+)"', html)
                self.assertEqual(sorted({i for i in ids if ids.count(i) > 1}), [])

    def test_script_is_es5_apart_from_bigint(self):
        blocks = [de_core.SHOW_JS, de_core.MPOLY_JS, de_core.RF_JS, de_core.EP_JS, de_core.STEP_JS,
                  de_core.DRAW_JS, calckit.CK_JS] + list(calckit.MODE_JS.values())
        # algebra_core's comments quote names in backticks; its code is ES5
        blocks += [own_script(build(cfg).script) for _, cfg in FIXTURES]
        for i, js in enumerate(blocks):
            for rx, what in NOT_ES5:
                self.assertIsNone(rx.search(js), "%s in block %d" % (what, i))

    def test_no_double_quote_in_what_de_core_and_calckit_add(self):
        for block in [de_core.SHOW_JS, de_core.MPOLY_JS, de_core.RF_JS, de_core.EP_JS, de_core.STEP_JS,
                      de_core.DRAW_JS, calckit.CK_JS] + list(calckit.MODE_JS.values()):
            self.assertNotIn('"', block)
        for key, cfg in FIXTURES:
            with self.subTest(lesson=key):
                self.assertNotIn('"', own_script(build(cfg).script))

    def test_each_preset_can_be_shipped(self):
        for key, cfg in FIXTURES:
            for p in cfg["presets"]:
                with self.subTest(lesson=key, preset=p["id"]):
                    lab = build(cfg, preset=p["id"])
                    self.assertIn('<option value="%s" selected>' % p["id"], lab.controls)

    def test_no_shipped_value_holds_markup_characters(self):
        for key, cfg in FIXTURES:
            lab = build(cfg)
            for value in re.findall(r'<input [^>]*value="([^"]*)"', lab.controls):
                with self.subTest(lesson=key, value=value):
                    self.assertFalse(set(value) & set("<>&"), value)

    def test_per_mode_assembly(self):
        """A page carries the de_core blocks its mode names, and no other mode's code."""
        names = {"quotient": "qtCompute", "hpoly": "hpCompute", "tangent": "tgCompute",
                 "derivative": "dvCompute", "transcendental": "tqCompute", "riemann": "rsCompute",
                 "antiderivative": "adCompute"}
        for key, cfg in FIXTURES:
            script = build(cfg).script
            with self.subTest(lesson=key):
                for mode, fn in names.items():
                    (self.assertIn if mode == cfg["mode"] else self.assertNotIn)("function %s(" % fn, script)
                self.assertNotIn("function EPparse(", script)
                self.assertNotIn("function DE_euler(", script)
        self.assertNotIn("function RFpartial(", build(dict(FIXTURES)["1.2"]).script)   # hpoly: MPOLY only

    def test_show_limit_false_omits_the_limit(self):
        by = dict(FIXTURES)
        lab = build(by["1.1"])
        self.assertNotIn('id="qtLimit"', lab.controls)
        self.assertNotIn('id="qtGap"', lab.controls)
        self.assertIn('id="qtLimit"', build(by["1.3"]).controls)

    def test_redraw_only_defaults_come_from_cfg(self):
        by = dict(FIXTURES)
        self.assertIn('<option value="2" selected>', build(by["1.10"]).controls)
        self.assertIn('<option value="trap" selected>', build(by["2.4"]).controls)
        self.assertIn('<option value="left" selected>', build(by["2.8"]).controls)


class Refusals(unittest.TestCase):
    def bad(self, cfg, needle):
        with self.assertRaises(ValueError) as ctx:
            labs.build("calckit", cfg)
        self.assertIn(needle, str(ctx.exception))

    def test_unknown_mode(self):
        self.bad({"mode": "integral", "presets": [_p("x", f="t")]}, "unknown mode")

    def test_unknown_preset(self):
        self.bad(dict(FIXTURES[0][1], preset="nope"), "no preset 'nope'")

    def test_malformed_instances_name_the_preset(self):
        self.bad({"mode": "quotient", "presets": [_p("neg", f="t^2", a=1, h=-1, halvings=2)]}, "'neg'")
        self.bad({"mode": "quotient", "presets": [_p("many", f="t^2", a=1, h=1, halvings=13)]}, "'many'")
        self.bad({"mode": "quotient", "presets": [_p("word", f="sin(x)", a=1, h=1, halvings=2)]}, "'word'")
        self.bad({"mode": "hpoly", "presets": [_p("g", kind="product", f="t", g=None)]}, "'g'")
        self.bad({"mode": "riemann", "presets": [_p("back", f="t", a=2, b=1, n=4)]}, "'back'")
        self.bad({"mode": "antiderivative", "presets": [_p("half", f="t", a=0)]}, "'half'")
        self.bad({"mode": "transcendental", "presets": [_p("kind", kind="tan", a=0, h=1, halvings=1)]}, "'kind'")
        self.bad({"mode": "derivative", "order": 1, "presets": [_p("o", f="t", order=2)]}, "'o'")

    def test_bad_redraw_only_values(self):
        self.bad(dict(dict(FIXTURES)["2.1"], rule="simpson"), "rule")
        self.bad(dict(dict(FIXTURES)["1.6"], order=3), "order")

    def test_missing_expect_is_not_a_build_error(self):
        build({"mode": "tangent", "presets": [{"id": "x", "label": "x", "f": "t^2", "a": 1, "h": 1}]})


# ---------------------------------------------------------------------------
# The arithmetic, by running the shipped blocks.
# ---------------------------------------------------------------------------

ARITH = r"""
var out = [];
function eq(label, got, want) { if (String(got) !== String(want)) out.push(label + ': got ' + got + ', want ' + want); }
function Q(s) { return DE_rat(s); }
/* D.1's five first cases */
eq('EPderiv t e^-2t', EPtext(EPderiv(EPparse('t e^(-2t)'))), '−2·t·e^(−2t) + e^(−2t)');
eq('EPlaplace t e^3t', RFtext(EPlaplace(EPparse('t e^(3t)')), 's', true), '1/(s − 3)²');
eq('RFpartial 1/(s(s+1)^2)', RFpartialText(RFpartial(RFparse('1/(s*(s+1)^2)', 's')), 's'), '1/s − 1/(s + 1) − 1/(s + 1)²');
var rk = DE_rk4(MPparse('t^3', ['t', 'y']), R0, R0, Q('1/4'), 4);
eq('DE_rk4 t^3 error', DE_q(Rsub(rk.rows[4].y, Q('1/4'))), '0');
var bu = DE_euler(MPparse('y^2', ['t', 'y']), R0, R1, Q('1/4'), 64);
eq('DE_euler y^2 budget', bu.steps + ' ' + bu.stopped, '11 true');
/* the printers */
eq('DE_q', DE_q(Q('-3/4')), '−3/4');
eq('DE_dec', [DE_dec(Math.LN2), DE_dec(2.5), DE_dec(2.06115e-9), DE_dec(-0.4596976941), DE_dec(NaN)].join('|'),
   '≈ 0.693147|≈ 2.5|≈ 2.06115e-9|≈ −0.459698|—');
var q1 = quadroots(R1, R(-1n), R(-1n)), q2 = quadroots(R1, R(2n), R(5n)), q3 = quadroots(R1, R0, R(4n));
eq('DE_root', [DE_root(q1.p, q1.s, false), DE_root(q2.p, q2.s, true), DE_root(q3.p, q3.s, true),
   DE_root(null, Rsurd(Q('5/2')), false), DE_root(null, Rsurd(R(24n)), false)].join('|'),
   '(1 ± √5)/2|−1 ± 2i|±2i|√10/2|2√6');
eq('DE_ptext', DE_ptext(Pintegral([R(1n), R(-4n), R(3n)])) + '|' + DE_ptext(Pintegral([R0, R0, R1])), 't³ − 2t² + t|t³/3');
eq('MPtext by h', MPtext(MPdivVar(MPsub(MPsubst(MPparse('t^3', ['t', 'h']), 't', MPparse('t + h', ['t', 'h'])),
   MPparse('t^3', ['t', 'h'])), 'h'), { by: 'h' }), '3t² + 3th + h²');
eq('MPeval', DE_q(MPeval(MPparse('t^2 - y', ['t', 'y']), { t: Q('1/2'), y: R(1n) })), '−3/4');
var msg = ''; try { MPparse('sin(t) + y', ['t', 'y']); } catch (e) { msg = e.message; }
eq('MPparse refusal', msg, 'this lab steps polynomial right-hand sides exactly; sin(t) is not one');
eq('EPtext', EPtext(EPparse('2e^(-t) - e^(-2t)')) + '|' + EPtext(EPparse('(2/3)t - 2/9')),
   '2·e^(−t) − e^(−2t)|(2/3)·t − 2/9');
var y = EPparse('t cos(t)');
eq('residual t cos t', EPtext(EPadd(EPderiv(EPderiv(y)), y)), '−2·sin(t)');
var fam = EPfamily('C cos(t) + D sin(t)');
eq('EPfamily', EPtext(fam.C) + '|' + EPtext(fam.D) + '|' + EPzero(fam.base), 'cos(t)|sin(t)|true');
eq('EPfromPartial', EPtext(EPfromPartial(RFpartial(RFparse('(s+3)/((s+1)*(s+2))', 's'))).ep), '2·e^(−t) − e^(−2t)');
eq('EPfromPartial quad', EPtext(EPfromPartial(RFpartial(RFparse('(s+1)/((s+1)^2+4)', 's'))).ep), 'e^(−t)·cos(2t)');
eq('EPevalExact', DE_q(EPevalExact(EPparse('2e^(-t) - e^(-2t)'), R0)) + '|' + EPevalExact(EPparse('e^t'), R1), '1|null');
eq('DE_euler y', DE_q(DE_euler(MPparse('y', ['t', 'y']), R0, R1, Q('1/4'), 4).rows[4].y), '625/256');
var sys = DE_eulerSys(MPparse('-y', ['x', 'y']), MPparse('x', ['x', 'y']), R0, R1, R0, Q('1/4'), 2);
eq('DE_eulerSys', DE_q(sys.rows[2].x) + ',' + DE_q(sys.rows[2].y), '15/16,1/2');
/* calckit, against section C's worked lines */
var qt = qtCompute('t^2', '1', '1', 2);
eq('qt t^2', qt.rows.map(function (r) { return DE_q(r.q); }).join(', '), '3, 5/2, 9/4');
var qt2 = qtCompute('1/t', '2', '1/4', 0);
eq('qt 1/t', DE_q(qt2.rows[0].q) + ' ' + DE_q(qt2.limit), '−2/9 −1/4');
var hp = hpCompute('single', 't^3', '', '');
eq('hp t^3', MPtext(hp.q.Q, { by: 'h' }) + ' | ' + DE_ptext(hp.q.C), '3t² + 3th + h² | 3t²');
var hc = hpCompute('compose', 't^2', '3t + 1', '');
eq('hp chain', DE_ptext(hc.rule) + ' ' + hc.equal, '18t + 6 true');
var tg = tgCompute('t^2', '2', '1/10');
eq('tg', DE_ptext(tg.line) + ' ' + DE_q(tg.approx) + ' ' + DE_q(tg.tru) + ' ' + DE_q(tg.error), '4t − 4 22/5 441/100 1/100');
var dv = dvCompute('t^3 - 6t^2 + 9t');
eq('dv', DE_ptext(dv.d1) + ' | ' + dv.zeros + ' | ' + dv.intervals, '3t² − 12t + 9 | 1, 3 | rising t < 1; falling 1 < t < 3; rising t > 3');
eq('dv flat', dvCompute('t^3').intervals, 'rising t < 0; rising t > 0');
eq('dv inflect', dvCompute('t^3 - 3t^2').inflect + ' ' + DE_q(Peval(dvCompute('t^3 - 3t^2').d1, R1)), 't = 1 −3');
var tq = tqCompute('exp', '2', '0', '1', 1);
eq('tq 2^t', tqShow(tq.rows[0]) + ' ' + tqShow(tq.rows[1]), '1 ≈ 0.828427');
eq('tq sin', tqShow(tqCompute('sin', '', '0', '1', 3).rows[3]), '≈ 0.997398');
var rs = rsCompute('t^2', '0', '1', 4, 'left');
eq('rs left', DE_q(rs.s1.left) + ' ' + DE_q(rs.s1.right) + ' ' + DE_q(rs.s2.sum) + ' ' + rs.errText + ' ' + rs.ratio,
   '7/32 15/32 35/128 −11/96 44/23');
eq('rs trap', rsCompute('t^2', '0', '1', 4, 'trap').s2.sum.n + '/' + rsCompute('t^2', '0', '1', 4, 'trap').s2.sum.d, '43/128');
eq('rs mid', DE_q(rsCompute('t^2', '0', '1', 4, 'mid').s1.sum) + ' ' + rsCompute('t^2', '0', '1', 4, 'mid').errText, '21/64 −1/192');
var ln = rsCompute('1/t', '1', '2', 4, 'trap');
eq('rs 1/t', DE_q(ln.s1.left) + ' ' + DE_q(ln.s1.right) + ' ' + DE_q(ln.s1.sum) + ' ' + ln.exText,
   '319/420 533/840 1171/1680 ≈ 0.693147 (ln 2, rounded)');
var pole = ''; try { rsCompute('1/t', '-1', '1', 4, 'left'); } catch (e) { pole = e.message; }
eq('rs pole', pole.indexOf('pole at t = 0') >= 0, true);
var ad = adCompute('3t^2 + 2t', false, '', '', '', '0', '2', '1');
eq('ad split', ad.split, 'equal: 12 = 2 + 10');
eq('ad ic', DE_q(adCompute('2t', false, '', '', '1 5', '', '', '').C), '4');
eq('RFtext factored', RFtext(RFparse('(s+3)/(s^2+3s+2)', 's'), 's', true), '(s + 3)/((s + 1)(s + 2))');
var lin = ''; try { EPfamily('C C t'); } catch (e) { lin = e.message; }
eq('EPfamily linear', lin, 'the candidate is not linear in C and D');
eq('dv even zero', dvCompute('t^3').zeros, '0 (no sign change)');
eq('ad split from 1', adCompute('3t^2', false, '', '', '', '1', '3', '2').split, 'equal: 26 = 7 + 19');
console.log(out.length ? out.join('\n') : 'OK');
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class Arithmetic(unittest.TestCase):
    def test_shipped_blocks_compute_the_worked_figures(self):
        src = de_core.script("SURD", "MPOLY", "RF", "EP", "STEP", "DRAW",
                             extra=calckit.CK_JS + "".join(calckit.MODE_JS.values()))
        run = subprocess.run(["node", "-e", src + ARITH], capture_output=True, text=True, timeout=60)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(run.stdout.strip(), "OK")


# A page's own script, run against a stub document: every control at the value
# the markup ships for that preset, then each pinned tile read back. This is
# the per-page arithmetic gate in a fraction of a second; scripts/labcheck.js
# --expect on rendered fixture pages is the full one (sweep included).
PAGE_RUNNER = r"""
var vm = require('vm');
var jobs = JSON.parse(require('fs').readFileSync(0, 'utf8')), fails = [];
function El(id, value) {
  this.id = id; this.value = value === undefined ? '' : value; this.textContent = ''; this.innerHTML = '';
  this.style = {}; this.attrs = {};
}
El.prototype.addEventListener = function () {};
El.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
El.prototype.getAttribute = function (k) { return k in this.attrs ? this.attrs[k] : null; };
El.prototype.appendChild = function (c) { return c; };
El.prototype.remove = function () {};
jobs.forEach(function (job) {
  var els = {};
  Object.keys(job.values).forEach(function (id) { els[id] = new El(id, job.values[id]); });
  var doc = {
    getElementById: function (id) { return els[id] || null; },
    createElementNS: function () { return new El(''); },
    createElement: function () { return new El(''); }
  };
  var box = { document: doc, Math: Math, console: console };
  box.window = box;
  try {
    vm.runInNewContext(job.script, box, { timeout: 10000 });
  } catch (e) { fails.push(job.name + ': ' + e.message); return; }
  Object.keys(job.expect).forEach(function (tile) {
    var got = els[tile] ? els[tile].textContent : '(no tile)';
    if (got !== job.expect[tile]) fails.push(job.name + ' #' + tile + ': got ' + got + ', want ' + job.expect[tile]);
  });
  if (/Refused/.test(els[job.status].innerHTML)) fails.push(job.name + ': ' + els[job.status].innerHTML);
});
console.log(fails.length ? fails.join('\n') : 'OK');
"""


def _values(html):
    out = {}
    for m in re.finditer(r'<(input|select|div|strong|span|svg|label)\b([^>]*)>', html):
        idm = re.search(r'\bid="([^"]+)"', m.group(2))
        if idm:
            val = re.search(r'\bvalue="([^"]*)"', m.group(2))
            out[idm.group(1)] = val.group(1) if (val and m.group(1) == "input") else ""
    for m in re.finditer(r'<select id="([^"]+)">(.*?)</select>', html):
        chosen = re.search(r'<option value="([^"]*)" selected>', m.group(2)) or re.search(r'<option value="([^"]*)"', m.group(2))
        out[m.group(1)] = chosen.group(1) if chosen else ""
    return out


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class EveryPresetPrintsItsFigures(unittest.TestCase):
    def test_each_page_script_prints_the_pinned_tiles(self):
        import json
        jobs = []
        for key, cfg in FIXTURES:
            for p in cfg["presets"]:
                lab = build(cfg, preset=p["id"])
                jobs.append({"name": "%s %s/%s" % (key, cfg["mode"], p["id"]), "script": lab.script,
                             "values": _values(lab.markup + lab.controls), "expect": p["expect"],
                             "status": TILES[cfg["mode"]][2]})
        run = subprocess.run(["node", "-e", PAGE_RUNNER], input=json.dumps(jobs), capture_output=True,
                             text=True, timeout=120)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(run.stdout.strip(), "OK")


if __name__ == "__main__":
    unittest.main()
