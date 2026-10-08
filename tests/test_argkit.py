"""argkit, the Philosophy argument kit: every mode builds with every preset
docs/philosophy/PLAN.md section C sketches.

No browser and no node: this builds each lesson's lab through labs.build and
checks the markup and the script came out, that every preset reached the menu
and the expectation table, and that the build-time refusals raise. Whether the
figures are RIGHT is scripts/labcheck.js's job on a rendered page.

    /usr/bin/python3 -m unittest tests.test_argkit -v
"""

import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from mathpath import labs  # noqa: E402
from mathpath.labs import argkit  # noqa: E402


def P(pid, **fields):
    fields.setdefault("label", pid.replace("-", " "))
    fields["id"] = pid
    return fields


def case(name, values, verdict):
    return {"name": name, "values": values, "verdict": verdict}


# Every argkit lesson in PLAN.md section C, as (mode, cfg). Instances follow the
# sketch; where the sketch names a preset without its instance, the instance
# here is a plausible one an author might write.
LESSONS = {
    # Course 1
    "1.1": ("validity", {"show": "all", "presets": [
        P("bare", premises=["p", "q"], conclusion="p"),
        P("leap", premises=["p"], conclusion="q"),
        P("padding", premises=["p", "q", "r"], conclusion="p")]}),
    "1.2": ("validity", {"presets": [
        P("same", premises=["p"], conclusion="p"),
        P("other", premises=["q"], conclusion="p"),
        P("both", premises=["p", "q"], conclusion="q")]}),
    "1.5": ("validity", {"presets": [
        P("mp", premises=["p -> q", "p"], conclusion="q"),
        P("mt", premises=["p -> q", "~q"], conclusion="~p"),
        P("ac", premises=["p -> q", "q"], conclusion="p"),
        P("da", premises=["p -> q", "~p"], conclusion="~q")]}),
    "1.7": ("consistency", {"presets": [
        P("triad", sentences=["p -> q", "p", "~q"]),
        P("four", sentences=["p -> q", "q -> r", "p", "~r"]),
        P("fine", sentences=["p | q", "~p", "q -> r"])]}),
    "1.8": ("syllogism", {"import": "boolean", "presets": [
        P("convert-e", premises=["No S are P"], conclusion="No P are S"),
        P("convert-a", premises=["All S are P"], conclusion="All P are S"),
        P("contrapose-a", premises=["All S are P"], conclusion="All non-P are non-S"),
        P("convert-o", premises=["Some S are not P"], conclusion="Some P are not S")]}),
    "1.9": ("syllogism", {"import": "boolean", "presets": [
        P("subalt", premises=["All S are P"], conclusion="Some S are P"),
        P("contradictory", premises=["All S are P"], conclusion="Some S are not P"),
        P("converse-accidens", premises=["All S are P"], conclusion="Some P are S"),
        P("unicorns", premises=["All unicorns are white"], conclusion="Some unicorns are white")]}),
    "1.10": ("syllogism", {"presets": [
        P("barbara", premises=["All M are P", "All S are M"], conclusion="All S are P"),
        P("darii", premises=["All M are P", "Some S are M"], conclusion="Some S are P"),
        P("ferio", premises=["No M are P", "Some S are M"], conclusion="Some S are not P"),
        P("undistributed", premises=["All P are M", "All S are M"], conclusion="All S are P"),
        P("illicit-major", premises=["All M are P", "No S are M"], conclusion="No S are P")]}),
    "1.12": ("validity", {"presets": [
        P("hs", premises=["p -> q", "q -> r"], conclusion="p -> r"),
        P("ds", premises=["p | q", "~p"], conclusion="q"),
        P("cd", premises=["p -> r", "q -> s", "p | q"], conclusion="r | s"),
        P("affirm-disjunct", premises=["p | q", "p"], conclusion="~q"),
        P("da", premises=["p -> q", "~p"], conclusion="~q")]}),
    # Course 2
    "2.1": ("analysis", {"search": "off", "presets": [
        P("jtb", conditions=["J", "T", "B"], target="knows", definition="J & T & B", cases=[
            case("ordinary perception", [1, 1, 1], 1), case("lucky guess", [0, 1, 1], 0),
            case("confident error", [1, 0, 1], 0), case("unbelieved truth", [1, 1, 0], 0)])]}),
    "2.2": ("analysis", {"search": "pairs", "preset": "lemma", "presets": [
        P("gettier", conditions=["J", "T", "B"], definition="J & T & B", cases=[
            case("ordinary perception", [1, 1, 1], 1), case("Smith's coins", [1, 1, 1], 0),
            case("stopped clock", [1, 1, 1], 0), case("lucky guess", [0, 1, 1], 0)]),
        P("lemma", conditions=["J", "T", "B", "L"], definition="J & T & B & ~L", cases=[
            case("ordinary perception", [1, 1, 1, 0], 1), case("Smith's coins", [1, 1, 1, 1], 0),
            case("lucky guess", [0, 1, 1, 0], 0), case("fake barns", [1, 1, 1, 0], 0)])]}),
    "2.3": ("analysis", {"search": "pairs", "presets": [
        P("reliabilist", conditions=["R", "E", "T", "B"], definition="R & T & B", cases=[
            case("perception", [1, 1, 1, 1], 1), case("Norman", [1, 0, 1, 1], 0),
            case("envatted twin", [0, 1, 0, 1], 1), case("lucky testimony", [0, 1, 1, 1], 0)]),
        P("evidentialist", conditions=["R", "E", "T", "B"], definition="E & T & B", cases=[
            case("perception", [1, 1, 1, 1], 1), case("Norman", [1, 0, 1, 1], 0),
            case("envatted twin", [0, 1, 0, 1], 1), case("lucky testimony", [0, 1, 1, 1], 0)])]}),
    "2.4": ("validity", {"presets": [
        P("closure", premises=["h -> b", "~b"], conclusion="~h"),
        P("moore", premises=["h", "h -> b"], conclusion="b"),
        P("deny-closure", premises=["~b"], conclusion="~h")]}),
    "2.5": ("consistency", {"presets": [
        P("agrippa", sentences=["j", "j -> n", "n -> (c | f | i)", "~c", "~f", "~i"]),
        P("foundationalist", sentences=["j", "j -> n", "n -> (c | f | i)", "~c", "~i"])]}),
    # Course 3
    "3.6": ("consistency", {"presets": [
        P("duhem", sentences=["h", "a", "b", "(h & a & b) -> e", "~e"]),
        P("neptune", sentences=["h", "b", "(h & a & b) -> e", "~e"])]}),
    "3.7": ("analysis", {"search": "pairs", "presets": [
        P("diners", conditions=["A", "B", "C", "D", "E"], target="sick", definition="C", cases=[
            case("Ann", [1, 0, 1, 0, 1], 1), case("Bob", [0, 1, 1, 0, 0], 1),
            case("Cy", [1, 1, 0, 1, 0], 0), case("Di", [0, 0, 1, 1, 1], 1),
            case("Ed", [1, 0, 0, 0, 1], 0)]),
        P("two-causes", conditions=["A", "B", "C"], target="sick", definition="A", cases=[
            case("1", [1, 0, 0], 1), case("2", [0, 1, 0], 1), case("3", [0, 0, 1], 0),
            case("4", [1, 1, 1], 1), case("5", [0, 0, 0], 0)])]}),
    "3.9": ("structural", {"presets": [
        P("match", equations={"F": "S & O"}, exogenous={"S": 1, "O": 1}, cause="S", effect="F"),
        P("oxygen", equations={"F": "S & O"}, exogenous={"S": 1, "O": 1}, cause="O", effect="F"),
        P("chain", equations={"B": "A", "C": "B"}, exogenous={"A": 1}, cause="A", effect="C")]}),
    "3.10": ("structural", {"presets": [
        P("preemption", equations={"SH": "ST", "BH": "BT & ~SH", "shattered": "SH | BH"},
          exogenous={"ST": 1, "BT": 1}, cause="ST", effect="shattered"),
        P("overdetermination", equations={"SH": "ST", "BH": "BT", "shattered": "SH | BH"},
          exogenous={"ST": 1, "BT": 1}, cause="ST", effect="shattered"),
        P("trumping", equations={"MO": "M", "SO": "S & ~M", "march": "MO | SO"},
          exogenous={"M": 1, "S": 1}, cause="M", effect="march")]}),
    # Course 6
    "6.1": ("validity", {"presets": [
        P("hume", premises=["p", "q"], conclusion="o"),
        P("bridged", premises=["p", "q", "(p & q) -> o"], conclusion="o"),
        P("searle", premises=["u", "u -> m", "m -> o"], conclusion="o")]}),
    "6.2": ("analysis", {"search": "pairs", "presets": [
        P("hedonism", conditions=["P", "D", "A"], target="good", definition="P", cases=[
            case("a good life", [1, 1, 1], 1), case("experience machine", [1, 1, 0], 0),
            case("deceived life", [1, 0, 0], 0), case("hard-won project", [0, 1, 1], 1)]),
        P("desire", conditions=["P", "D", "A"], target="good", definition="D", cases=[
            case("a good life", [1, 1, 1], 1), case("experience machine", [1, 1, 0], 0),
            case("satisfied sadist", [1, 1, 1], 0), case("hard-won project", [0, 1, 1], 1)])]}),
    "6.8": ("structural", {"presets": [
        P("switch", equations={"divert": "pull", "hit": "divert", "five": "divert | stop"},
          exogenous={"pull": 1, "stop": 0}, cause="hit", effect="five"),
        P("loop", equations={"divert": "pull", "hit": "divert", "five": "divert & hit"},
          exogenous={"pull": 1}, cause="hit", effect="five"),
        P("bomber", equations={"bomb": "order", "civ": "bomb", "end": "bomb & civ"},
          exogenous={"order": 1}, cause="civ", effect="end")]}),
    "6.9": ("structural", {"presets": [
        P("lifeguard", equations={"R": "L & W", "D": "~R"}, exogenous={"L": 1, "W": 0},
          cause="W", effect="D"),
        P("two-rescuers", equations={"R": "W1 | W2", "D": "~R"}, exogenous={"W1": 0, "W2": 0},
          cause="W1", effect="D"),
        P("shallow-pond", equations={"R": "W", "D": "~R"}, exogenous={"W": 0}, cause="W", effect="D")]}),
    "6.10": ("consistency", {"presets": [
        P("dilemma", sentences=["op", "oq", "(op & oq) -> opq", "opq -> cpq", "~cpq"]),
        P("drop-agglomeration", sentences=["op", "oq", "opq -> cpq", "~cpq"]),
        P("drop-can", sentences=["op", "oq", "(op & oq) -> opq", "~cpq"])]}),
    "6.11": ("validity", {"presets": [
        P("function", premises=["f -> g", "r"], conclusion="g"),
        P("function-bridged", premises=["f -> g", "r", "r -> f"], conclusion="g"),
        P("enthymeme", premises=["r -> f"], conclusion="g")]}),
    "6.12": ("sorites", {"treatment": "classical", "presets": [
        P("weeks", start=40, end=0, cutoff=24, predicate="is too early to matter"),
        P("cents", start=10000, end=0, cutoff=4999, predicate="is a fair price"),
        P("grains", start=10000, end=0, cutoff=100, range=[50, 200], predicate="is a heap")]}),
    # Course 8
    "8.1": ("kripke", {"at": 1, "presets": [
        P("two-worlds", n=2, access=[[1, 2]], valuation={"p": [2]}, formula="[]p"),
        P("blind", n=2, access=[], valuation={"p": [2]}, formula="<>p"),
        P("self", n=2, access=[[1, 1], [1, 2], [2, 2]], valuation={"p": [2]}, formula="[]p")]}),
    "8.2": ("kripke", {"presets": [
        P("reflexive", n=3, access=[[1, 1], [2, 2], [3, 3], [1, 2], [2, 3]], valuation={"p": [1, 2]}, formula="[]p -> p"),
        P("s4", n=3, access=[[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [1, 3]], valuation={"p": [1, 2]}, formula="[]p -> p"),
        P("s5", n=3, access=[[1, 1], [2, 2], [3, 3], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]],
          valuation={"p": [1, 2]}, formula="[]p -> p"),
        P("serial-only", n=3, access=[[1, 2], [2, 3], [3, 1]], valuation={"p": [2]}, formula="[]p -> p")]}),
    "8.3": ("kripke", {"presets": [
        P("wide", n=3, access=[[1, 2], [1, 3]], valuation={"p": [2]}, formula="[](p | ~p)"),
        P("narrow", n=3, access=[[1, 2], [1, 3]], valuation={"p": [2]}, formula="[]p | []~p"),
        P("determined", n=3, access=[[1, 2], [1, 3]], valuation={"p": [2, 3]}, formula="[]p | []~p")]}),
    "8.4": ("kripke", {"presets": [
        P("s5", n=3, access=[[1, 1], [1, 2], [2, 1], [2, 2], [3, 3]], valuation={"G": [1, 2]},
          formula="<>[]G -> []G"),
        P("no-symmetry", n=2, access=[[1, 1], [1, 2], [2, 2]], valuation={"G": [2]}, formula="<>[]G -> []G"),
        P("b-axiom", n=2, access=[[1, 1], [1, 2], [2, 1], [2, 2]], valuation={"G": [2]}, formula="<>[]G -> []G")]}),
    "8.5": ("kripke", {"reading": "epistemic", "presets": [
        P("known-father", label="I know my father is here", n=2, access=[[1, 1], [1, 2]],
          valuation={"f": [1, 2], "m": [1]}, formula="[]f"),
        P("known-masked", label="I know the masked man is here", n=2, access=[[1, 1], [1, 2]],
          valuation={"f": [1, 2], "m": [1]}, formula="[]m"),
        P("same-man", label="the father is the masked man", n=2, access=[[1, 1], [1, 2]],
          valuation={"f": [1, 2], "m": [1]}, formula="f <-> m"),
        P("extensional", n=1, access=[[1, 1]], valuation={"f": [1], "m": [1]}, formula="[]f <-> []m")]}),
    "8.6": ("sorites", {"treatment": "classical", "presets": [
        P("planks", start=1000, end=0, predicate="is the ship of Theseus"),
        P("cutoff-half", start=1000, end=0, cutoff=500, predicate="is the ship of Theseus"),
        P("degrees", start=1000, end=0, predicate="is the ship of Theseus")]}),
    "8.8": ("consistency", {"presets": [
        P("fission", sentences=["ca", "cb", "ca -> ia", "cb -> ib", "~(ia & ib)"]),
        P("no-branching", sentences=["ca", "cb", "(ca & ~cb) -> ia", "(cb & ~ca) -> ib", "~(ia & ib)"]),
        P("parfit", sentences=["ca", "cb", "~(ia & ib)"])]}),
    "8.9": ("consistency", {"presets": [
        P("triad", sentences=["d", "f", "d -> ~f"]),
        P("compatibilist", sentences=["d", "f", "f <-> a", "d -> ~o"]),
        P("libertarian", sentences=["~d", "f", "d -> ~f"])]}),
    "8.10": ("kripke", {"presets": [
        P("transfer", n=3, access=[[1, 2], [2, 3], [1, 3]], valuation={"p": [2, 3], "q": [3]},
          formula="([]p & [](p -> q)) -> []q"),
        P("premise-one", n=3, access=[[1, 2], [1, 3]], valuation={"p": [1, 2, 3]}, formula="[]p"),
        P("premise-two", n=3, access=[[1, 2], [1, 3]], valuation={"p": [1, 2, 3], "q": [1, 2, 3]},
          formula="[](p -> q)")]}),
    "8.11": ("structural", {"presets": [
        P("frankfurt", equations={"B": "~D", "A": "D | B"}, exogenous={"D": 1}, cause="D", effect="A"),
        P("no-intervener", equations={"A": "D"}, exogenous={"D": 1}, cause="D", effect="A"),
        P("intervener-acts", equations={"B": "~D", "A": "D | B"}, exogenous={"D": 0}, cause="D", effect="A")]}),
    "8.12": ("consistency", {"presets": [
        P("mackie", sentences=["o", "k", "g", "e", "(o & k & g) -> ~e"]),
        P("free-will-defence", sentences=["o", "k", "g", "e", "(o & k & g) -> ~u"]),
        P("evidential", sentences=["o", "k", "g", "e", "u", "(o & k & g) -> ~u"])]}),
    # Course 9
    "9.1": ("kripke", {"presets": [
        P("zombie", n=2, access=[[1, 1], [1, 2]], valuation={"p": [1, 2], "c": [1]}, formula="[](p <-> c)"),
        P("no-zombie-world", n=1, access=[[1, 1]], valuation={"p": [1], "c": [1]}, formula="[](p <-> c)")]}),
    "9.5": ("validity", {"presets": [
        P("mary", premises=["a -> ~n", "n"], conclusion="~a"),
        P("ability-reply", premises=["a -> ~n", "k"], conclusion="~a"),
        P("equivocation", premises=["a -> ~n1", "n2"], conclusion="~a")]}),
    "9.6": ("semantics", {"presets": [
        P("orbits", domain=["a", "b", "c"], predicates={"Planet": ["a", "b"], "Orbits": [["a", "b"], ["b", "c"]]},
          sentence="Ax (Planet(x) -> Ey Orbits(x, y))"),
        P("everyone-loves", domain=["a", "b", "c"], predicates={"Loves": ["ab", "bc", "ca"]},
          sentence="Ax Ey Loves(x, y)"),
        P("no-witness", domain=["a", "b", "c"], predicates={"Planet": ["a", "b"], "Orbits": [["a", "b"]]},
          sentence="Ax (Planet(x) -> Ey Orbits(x, y))")]}),
    "9.7": ("semantics", {"presets": [
        P("hesperus", domain=["a", "b"], names={"h": "a", "p": "a"}, predicates={}, sentence="h = p"),
        P("distinct", domain=["a", "b"], names={"h": "a", "p": "b"}, predicates={}, sentence="h = p"),
        P("twin-earth", domain=["a", "b"], names={"w": "a"}, predicates={"Water": ["a"]}, sentence="Water(w)"),
        P("twin-earth-2", domain=["a", "b"], names={"w": "a"}, predicates={"Water": ["b"]}, sentence="Water(w)")]}),
    "9.8": ("semantics", {"presets": [
        P("king", domain=["a", "b", "c"], predicates={"King": [], "Bald": ["a", "b"]},
          sentence="[the x: King(x)] Bald(x)"),
        P("author", domain=["a", "b", "c"], predicates={"Author": ["b"], "Bald": ["b"]},
          sentence="[the x: Author(x)] Bald(x)"),
        P("two-kings", domain=["a", "b", "c"], predicates={"King": ["a", "c"], "Bald": ["a", "c"]},
          sentence="[the x: King(x)] Bald(x)")]}),
    "9.9": ("semantics", {"presets": [
        P("wide", domain=["a", "b"], predicates={"King": [], "Bald": ["a"]}, sentence="~[the x: King(x)] Bald(x)"),
        P("narrow", domain=["a", "b"], predicates={"King": [], "Bald": ["a"]}, sentence="[the x: King(x)] ~Bald(x)"),
        P("loves", domain=["a", "b"], predicates={"Loves": ["ab", "ba"]}, sentence="Ax Ey Loves(x, y)"),
        P("loves-one", domain=["a", "b"], predicates={"Loves": ["ab", "ba"]}, sentence="Ey Ax Loves(x, y)")]}),
    "9.10": ("sorites", {"treatment": "degrees", "presets": [
        P("heap", start=10000, end=0, predicate="is a heap"),
        P("heap-cutoff", start=10000, end=0, cutoff=50, predicate="is a heap"),
        P("heap-range", start=10000, end=0, range=[50, 200], predicate="is a heap")]}),
    # Course 10
    "10.1": ("semantics", {"presets": [
        P("barber", domain=["a", "b", "c"], predicates={"Shaves": ["ba", "bc"]},
          sentence="Ax (Shaves(b, x) <-> ~Shaves(x, x))"),
        P("barber-two", domain=["a", "b", "c"], predicates={"Shaves": ["ba", "bb", "bc"]},
          sentence="Ax (Shaves(b, x) <-> ~Shaves(x, x))"),
        P("honest-barber", domain=["a", "b", "c"], predicates={"Shaves": ["ba", "bc"]},
          sentence="Ax (~(x = b) -> (Shaves(b, x) <-> ~Shaves(x, x)))")]}),
    "10.9": ("kripke", {"reading": "epistemic", "presets": [
        P("moore-true", n=2, access=[[1, 1], [1, 2]], valuation={"p": [1]}, formula="p & ~[]p"),
        P("moore-believed", n=2, access=[[1, 1], [1, 2], [2, 2]], valuation={"p": [1]}, formula="[](p & ~[]p)"),
        P("not-reflexive", n=2, access=[[1, 2]], valuation={"p": [1]}, formula="[](p & ~[]p)")]}),
}

TILES = {
    "validity": ("vaPreset", ["vaRows", "vaCounter", "vaVerdict", "vaForm"], "vaStatus"),
    "consistency": ("coPreset", ["coModels", "coVerdict", "coMis", "coWitness"], "coStatus"),
    "syllogism": ("syPreset", ["syVerdict", "syForm", "syModels", "syCounter"], "syStatus"),
    "sorites": ("soPreset", ["soSteps", "soCond", "soConc"], "soStatus"),
    "kripke": ("krPreset", ["krValue", "krWorlds", "krFrame", "krAxioms"], "krStatus"),
    "semantics": ("sePreset", ["seValue", "seWitness", "seDesc", "seSat"], "seStatus"),
    "analysis": ("anPreset", ["anAgree", "anFail", "anVerdict", "anCands"], "anStatus"),
    "structural": ("stPreset", ["stActual", "stButFor", "stHP", "stKind"], "stStatus"),
}

# ES5: one inline <script> carries every lab and the quiz, so a construct an
# older parser rejects kills the page. BigInt literals come from RATIONAL_JS,
# shared with every exact kit, and are allowed.
NOT_ES5 = [
    (re.compile(r"=>"), "arrow function"),
    (re.compile(r"(^|[\s;{(])(let|const)\s"), "let/const"),
    (re.compile(r"`"), "template literal"),
    (re.compile(r"\?\."), "optional chaining"),
    (re.compile(r"\?\?"), "nullish coalescing"),
    (re.compile(r"\(\?<[=!]"), "lookbehind"),
]


def build(mode, cfg):
    return labs.build("argkit", dict(cfg, mode=mode))


class EveryLessonBuilds(unittest.TestCase):
    def test_every_section_c_lesson(self):
        self.assertEqual(set(m for m, _ in LESSONS.values()), set(argkit.MODES))
        for key, (mode, cfg) in LESSONS.items():
            with self.subTest(lesson=key, mode=mode):
                lab = build(mode, cfg)
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
                self.assertIn("window.redrawLab = redraw", lab.script)
                self.assertIn("akRefuse(", lab.script)
                for rx, what in NOT_ES5:
                    self.assertIsNone(rx.search(lab.script), "%s in the %s script" % (what, mode))

    def test_each_preset_can_be_shipped(self):
        for key, (mode, cfg) in LESSONS.items():
            for p in cfg["presets"]:
                with self.subTest(lesson=key, preset=p["id"]):
                    lab = build(mode, dict(cfg, preset=p["id"]))
                    self.assertIn('<option value="%s" selected>' % p["id"], lab.controls)

    def test_no_shipped_value_holds_markup_characters(self):
        # labcheck.js reads a control's starting value without decoding entities
        for key, (mode, cfg) in LESSONS.items():
            lab = build(mode, cfg)
            for value in re.findall(r'<input [^>]*value="([^"]*)"', lab.controls):
                with self.subTest(lesson=key, value=value):
                    self.assertFalse(set(value) & set("<>&"), value)

    def test_per_mode_assembly(self):
        rational = "function Rtext"
        for mode in argkit.MODES:
            key = next(k for k, (m, _) in LESSONS.items() if m == mode)
            script = build(mode, LESSONS[key][1]).script
            self.assertEqual(rational in script, mode == "sorites", mode)
            self.assertEqual("function akParse" in script,
                             mode in ("validity", "consistency", "kripke", "analysis", "structural"), mode)

    def test_redraw_only_defaults_come_from_cfg(self):
        lab = build(*LESSONS["9.10"])
        self.assertIn('<option value="degrees" selected>', lab.controls)
        lab = build(*LESSONS["2.2"])
        self.assertIn('<option value="pairs" selected>', lab.controls)
        self.assertIn('<option value="lemma" selected>', lab.controls)
        lab = build(*LESSONS["8.5"])
        self.assertIn('<option value="epistemic" selected>', lab.controls)


class BuildTimeRefusals(unittest.TestCase):
    def bad(self, mode, preset, match):
        with self.assertRaisesRegex(ValueError, match):
            build(mode, {"presets": [dict(preset, id="broken", label="broken")]})

    def test_unknown_mode_raises(self):
        with self.assertRaisesRegex(ValueError, "unknown mode"):
            labs.build("argkit", {"mode": "nope", "presets": []})

    def test_unknown_preset_raises(self):
        with self.assertRaisesRegex(ValueError, "no preset"):
            build("validity", dict(LESSONS["1.1"][1], preset="missing"))

    def test_malformed_instances_name_the_preset(self):
        self.bad("validity", {"premises": ["a", "b", "c", "d", "e", "f", "g"], "conclusion": "a"}, "broken")
        self.bad("validity", {"premises": ["a & b & c & d", "e"], "conclusion": "f -> g"}, "6 sentence letters")
        self.bad("consistency", {"sentences": ["p"] * 9}, "at most 8")
        self.bad("syllogism", {"premises": ["All A are B", "All C are D"], "conclusion": "All A are D"}, "3 terms")
        self.bad("syllogism", {"premises": ["Most A are B"], "conclusion": "All A are B"}, "categorical")
        self.bad("sorites", {"start": 10, "end": 10}, "end < start")
        self.bad("sorites", {"start": 10, "end": 0, "cutoff": 0}, "cutoff")
        self.bad("kripke", {"n": 7, "formula": "p"}, "1 to 6")
        self.bad("kripke", {"n": 2, "access": [[1, 3]], "formula": "p"}, "worlds 1..n")
        self.bad("kripke", {"n": 2, "formula": "a & b & c & d & e"}, "4 atoms")
        self.bad("semantics", {"domain": list("abcdefg"), "sentence": "Ax F(x)"}, "domain")
        self.bad("analysis", {"conditions": ["J"], "definition": "J",
                              "cases": [case("x", [1, 0], 1)]}, "row of 1 values")
        self.bad("analysis", {"conditions": ["J"], "definition": "J",
                              "cases": [case(str(i), [1], 1) for i in range(11)]}, "1 to 10")
        self.bad("analysis", {"conditions": ["J"], "definition": "K",
                              "cases": [case("x", [1], 1)]}, "not conditions")
        self.bad("structural", {"equations": {"A": "B", "B": "A"}, "exogenous": {},
                                "cause": "A", "effect": "B"}, "cycle")
        self.bad("structural", {"equations": {"A": "Z"}, "exogenous": {"X": 1},
                                "cause": "X", "effect": "A"}, "undefined")
        self.bad("structural", {"equations": {"A": "X"}, "exogenous": {"X": 1},
                                "cause": "X", "effect": "X"}, "two different")

    def test_bad_redraw_only_values_raise(self):
        with self.assertRaisesRegex(ValueError, "treatment"):
            build("sorites", dict(LESSONS["6.12"][1], treatment="fuzzy"))
        with self.assertRaisesRegex(ValueError, "at"):
            build("kripke", dict(LESSONS["8.1"][1], at=3))


if __name__ == "__main__":
    unittest.main()
