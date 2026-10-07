"""The spoken form of math notation, for read-out.

Two questions, kept apart:

* coverage -- every math run the five generated paths emit comes out as words
  a voice can say, with no symbol left over to be read as its Unicode name or
  dropped as punctuation;
* correctness -- a reading that is all words can still be wrong (`¬(p ∧ q)`
  read flat as "not p and q" says the opposite). Those are pinned case by case
  below, each one a reading that was wrong once.

    python3 -m unittest tests.test_speech -v
"""

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))

from mathpath.speech import say, say_block, unspoken  # noqa: E402

READINGS = {
    # the Discrete Mathematics key column
    "∀n ∈ ℕ.  P(n)          proved by induction, not by checking":
        "for every n in the natural numbers, P of n, proved by induction, not by checking",
    "|A ∪ B| = |A| + |B| − |A ∩ B|":
        "the size of A union B, equals the size of A, plus the size of B, "
        "minus the size of A intersect B",
    "C(n, k) = n! / (k!(n−k)!)":
        "n choose k equals n factorial over the quantity k factorial "
        "times the quantity n minus k, factorial",
    "gcd(a, b) = ax + by          for some integers x, y":
        "the gcd of A and b equals A x plus b y, for some integers x, y",
    "Σ deg(v) = 2|E|":
        "the sum of the degree of v equals 2 times the size of E",
    "T(n) = 2T(n/2) + n  ⟹  T(n) = Θ(n log n)":
        "T of n equals 2 T of n over 2 plus n, implies, T of n equals theta of n log n",
    # grouping: a flat reading changes the meaning
    "¬(p ∧ q)  ≡  ¬p ∨ ¬q":
        "not the quantity p and q, is equivalent to, not p or not q",
    "-b ± √(b² - 4ac)":
        "negative b plus or minus the square root of the quantity b squared minus 4 A c",
    "3 - (6 - 3) = 0": "3 minus the quantity 6 minus 3, equals 0",
    "disk IOPS = (1 − h) × reads":
        "disk IOPS equals the quantity 1 minus h, times reads",
    "n(n + 1)/2": "n times the quantity n plus 1, over 2",
    # bars: size, absolute value, given, such that, divides
    "|x − 3| < 2": "the absolute value of x minus 3, is less than 2",
    "|−6 − 1| = 7": "the absolute value of negative 6 minus 1, equals 7",
    "P(A | B)": "P of A given B",
    "{x | x > 0}": "the set x such that x is greater than 0",
    "a ≡ b (mod m)   ⟺   m | (a − b)":
        "A is congruent to b mod m, if and only if, m divides A minus b",
    # scripts, functions, units
    "x^2 + 3x − 4 = 0": "x squared plus 3 x minus 4 equals 0",
    "log_10(x)": "log base 10 of x",
    "⌈n/k⌉ − 1": "the ceiling of n over k, minus 1",
    "λ − μ": "lambda minus mu",
    "log_3(x + 6)": "log base 3 of the quantity x plus 6",
    "√(2KDh)/2": "the square root of the quantity 2 K D h, over 2",
    "2⌊log₂ m⌋": "2 times the floor of log base 2 m",
    "Vₜ(i)": "V sub t of i",
    "all c̄ᵢⱼ ≥ 0": "all c bar sub i j is greater than or equal to 0",
    "λ = 100 000 /s": "lambda equals 100000 per second",
    "scan 1 GB/s": "scan 1 gigabytes per second",
    "ρ = a/s < 1": "rho equals A over s is less than 1",
    "= 0.864 min   50 hours": "equals 0.864 minutes, 50 hours",
    "E[N₀]": "E of N sub 0",
    "Θ(nk)": "theta of n k",
    "χ(Cₙ)": "chi of C sub n",
    # arrows depend on what surrounds them
    "¬p → ¬q": "not p implies not q",
    "f : ℝ → [0,∞)": "f, the reals to 0, infinity",
    "n = 3 → 3": "n equals 3 goes to 3",
    # words beside operators are still words
    "N = 3, R = 168 h  (one week)": "N equals 3, R equals 168 h, one week",
    "latency cap ≈ 14 s": "latency cap is approximately 14 seconds",
    "(n − 3)² = 4,           a different quantity":
        "the quantity n minus 3, squared equals 4, a different quantity",
}


class TestReadings(unittest.TestCase):
    def test_pinned_readings(self):
        for text, spoken in READINGS.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_override_wins(self):
        self.assertEqual(say("Σ deg(v)", override="the sum over v of the degree of v"),
                         "the sum over v of the degree of v")

    def test_tables_are_not_read(self):
        lines = ["speedup        100.00 / 6.00                        =  16.67×",
                 "  ─────────────────────",
                 "      1   7       10            2         3            3",
                 "x = 2 + 1 = 3"]
        self.assertEqual(say_block(lines), ["a table, shown on the page", "x equals 2 plus 1 equals 3"])

    def test_markup_is_not_read(self):
        self.assertEqual(say("w(e) &le; w(g)"), "w of e is less than or equal to w of g")


class TestCoverage(unittest.TestCase):
    """Every run on the five generated paths is spoken, and nothing is guessed."""

    @classmethod
    def setUpClass(cls):
        from speechcheck import runs, subjects, unresolved

        cls.subjects = list(subjects())
        cls.runs, cls.unresolved = staticmethod(runs), staticmethod(unresolved)

    def test_every_run_is_spoken(self):
        for path, overrides in self.subjects:
            residue = {}
            for run, _, _ in self.runs(path):
                for ch in unspoken(overrides.get(run) or say(run)):
                    residue.setdefault(ch, run)
            with self.subTest(path=path["slug"]):
                self.assertEqual(
                    residue, {},
                    "symbols with no spoken form (add them to speech.SYMBOLS, "
                    "or give the run a spoken form): %r" % residue)

    def test_spoken_forms_are_words(self):
        for path, overrides in self.subjects:
            for run, spoken in overrides.items():
                with self.subTest(path=path["slug"], run=run):
                    self.assertTrue(spoken.strip())
                    self.assertEqual(unspoken(spoken), set())

    def test_no_spoken_form_for_math_that_is_gone(self):
        """A spoken form keyed to a run the content no longer has is dead data,
        and the next edit to that line silently loses its reading."""
        for path, overrides in self.subjects:
            present = {run for run, _, _ in self.runs(path)}
            with self.subTest(path=path["slug"]):
                self.assertEqual(sorted(set(overrides) - present), [])

    def test_nothing_is_guessed(self):
        """A run whose notation is ambiguous needs a spoken form, or the content
        rewritten to the convention in content/AGENTS.md."""
        for path, overrides in self.subjects:
            todo = self.unresolved(path, overrides)
            with self.subTest(path=path["slug"]):
                self.assertEqual(
                    [item["run"] for item in todo], [],
                    "python3 scripts/speechcheck.py --list %s" % path["slug"])


if __name__ == "__main__":
    unittest.main()
