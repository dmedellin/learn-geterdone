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

import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))

from mathpath.speech import is_rule, say, unspoken  # noqa: E402

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

    def test_markup_is_not_read(self):
        self.assertEqual(say("w(e) &le; w(g)"), "w of e is less than or equal to w of g")


_SPAN = re.compile(r"`([^`]+)`")


def _runs(node, out):
    """Every math run a generated page emits: inline `x` spans, and the lines
    of key, worked and ("math", ...) display blocks."""
    if isinstance(node, str):
        out.extend(_SPAN.findall(node))
    elif isinstance(node, dict):
        for k, v in node.items():
            if k in ("key", "lines") and isinstance(v, list) and all(isinstance(x, str) for x in v):
                out.extend(x for x in v if not is_rule(x))
            else:
                _runs(v, out)
    elif isinstance(node, (list, tuple)):
        if isinstance(node, tuple) and len(node) == 2 and node[0] == "math":
            out.extend(x for x in node[1] if not is_rule(x))
        else:
            for x in node:
                _runs(x, out)
    return out


class TestCoverage(unittest.TestCase):
    def test_every_run_is_spoken(self):
        from build_paths import GENERATED_PATHS

        for path in GENERATED_PATHS:
            residue = {}
            for run in set(_runs(path, [])):
                for ch in unspoken(say(run)):
                    residue.setdefault(ch, run)
            with self.subTest(path=path["slug"]):
                self.assertEqual(
                    residue, {},
                    "symbols with no spoken form (add them to speech.SYMBOLS, "
                    "or override the run): %r" % residue)


if __name__ == "__main__":
    unittest.main()
