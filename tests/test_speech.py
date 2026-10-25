"""The spoken form of math notation, for read-out.

Two questions, kept apart:

* coverage -- every math run the six generated paths emit comes out as words
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
        "T of n equals 2 T of the quantity n over 2, plus n, implies, "
        "T of n equals theta of n times log n",
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
    "all c̄ᵢⱼ ≥ 0": "all c bar sub i j is at least 0",
    "λ = 100 000 /s": "lambda equals 100000 per second",
    "scan 1 GB/s": "scan 1 gigabytes per second",
    "ρ = a/s < 1": "rho equals A over s is less than 1",
    "= 0.864 min   50 hours": "equals 0.864 minutes, 50 hours",
    "E[N₀]": "E of N sub 0",
    "Θ(nk)": "theta of n k",
    "χ(Cₙ)": "chi of C sub n",
    # reported by the per-subject spoken-form passes
    "log_b(M·N)": "log base b of the quantity M times N",
    "2^{h+1} − 1": "2 to the power the quantity h plus 1, minus 1",
    "Σ_{i=1}^{n} (2i − 1)²": "the sum from i equals 1 to n of the quantity 2 i minus 1, squared",
    "Σ_g P(g)": "the sum over g of P of g",
    "a + ar + ar² + ⋯ + arⁿ": "A plus A r plus A r squared, and so on, plus A r to the power n",
    "Θ(n ln n)": "theta of n times the natural log of n",
    "3 x 41 = 123": "3 times 41 equals 123",
    "ax² + bx + c": "A x squared plus b x plus c",
    "p⁻¹(25)": "p inverse of 25",
    "|S*|": "the size of S star",
    "f(2x + 6)": "f of the quantity 2 x plus 6",
    "[-2, inf)": "negative 2, infinity",
    # from the blind sample after the spoken-form passes
    "|ℕ| = |ℤ|": "the size of the natural numbers, equals the size of the integers",
    "|h_L − h_R| ≤ 1": "the absolute value of h sub L minus h sub R, is at most 1",
    "aₙ = (n + 1)2ⁿ": "A sub n equals the quantity n plus 1, times 2 to the power n",
    "D(i, j−1) + 1        insert the j-th character":
        "D of i and j minus 1 plus 1, insert the j-th character",
    "P(job past 120 ms)": "P of job past 120 milliseconds",
    "Ā = U \\ A = {x ∈ U : x ∉ A}": "A bar equals U minus A equals the set x in U such that x not in A",
    "5^0 = 1                  log_5(1) = 0": "5 to the power 0 equals 1, log base 5 of 1 equals 0",
    "× 2 = 39 813 120 000 bytes/day": "times 2 equals 39813120000 bytes per day",
    "(1 − λΔ)^(t/Δ) → e^(−λt)           as Δ → 0":
        "the quantity 1 minus lambda delta, to the power the quantity t over delta, goes to "
        "e to the power the quantity negative lambda t, as delta goes to 0",
    "λ = 1200 / s        μ = 1000 / s": "lambda equals 1200 per second, mu equals 1000 per second",
    "4 −2 6 | 18": "4 negative 2 6, 18",
    "3 | 12": "3 divides 12",
    "6x³y   / 6x³y  =   1        <-- write the 1":
        "6 x cubed y, over 6 x cubed y, equals, 1, write the 1",
    "x ∈ (A ∪ B)‾": "x in the complement of the quantity A union B",
    "on one 30-character text": "on one 30-character text",
    "n-1": "n minus 1",
    "n objects, k boxes, n > k   ⟹   some box has ≥ 2":
        "n objects, k boxes, n is greater than k, implies, some box has at least 2",
    "n ≥ 2": "n is at least 2",
    "≤": "less-than-or-equal",
    "&ge;": "greater-than-or-equal",
    "0 ≤ r < d": "0 is at most r is less than d",
    "□p → p": "necessarily p implies p",
    "◇p": "possibly p",
    "A ≻ B": "A is preferred to B",
    # arrows depend on what surrounds them
    "¬p → ¬q": "not p implies not q",
    "f : ℝ → [0,∞)": "f, the reals to 0, infinity",
    "n = 3 → 3": "n equals 3 goes to 3",
    # words beside operators are still words
    "N = 3, R = 168 h  (one week)": "N equals 3, R equals 168 h, one week",
    "latency cap ≈ 14 s": "latency cap is approximately 14 seconds",
    "(n − 3)² = 4,           a different quantity":
        "the quantity n minus 3, squared equals 4, a different quantity",
    # Differential Equations (docs/differential-equations/PLAN.md section D.5)
    "ℒ[f]": "the Laplace transform of f",
    "ℒ[y′] = s·Y(s) − y(0)":
        "the Laplace transform of y prime equals s times Y of s minus y of 0",
    "tr(J)": "the trace of J",
    "y‴ − y": "y triple prime minus y",
    "∫ₐᵇ f(t) dt": "the integral from A to b of f of t d t",
    "∫₁ˣ dt/t": "the integral from 1 to x of d t over t",
    "(1/T)∫N(t) dt": "1 over T the integral of N of t d t",
    # a letter applied to time or to a number is a call, not a product
    "y(0) = 1": "y of 0 equals 1",
    "x(t)": "x of t",
    "y(tₙ)": "y of t sub n",
    "y(t + h)": "y of the quantity t plus h",
    "u(t − c)": "u of the quantity t minus c",
    # ...but a fraction keeps "the quantity": "y of 1 over 2" is also y(1)/2
    "y(1/2)": "y of the quantity 1 over 2",
    "f(3/2) = 9/4": "f of the quantity 3 over 2, equals 9 over 4",
    "f(−1) = −3": "f of negative 1 equals negative 3",
    # ...and the shapes that stay products
    "y(y − 2)": "y times the quantity y minus 2",
    "3x(-2)²": "3 x times the quantity negative 2, squared",
    "c(9/10)n": "c times the quantity 9 over 10, times n",
    "2y(0)": "2 y times 0",
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
        lines = ["  2        2      0    98.01%",
                 "  ─────────────────────",
                 "      1   7       10            2         3            3",
                 "x = 2 + 1 = 3"]
        self.assertEqual(say_block(lines), ["a table, shown on the page", "x equals 2 plus 1 equals 3"])
        # one calculation laid out in columns is read, not skipped
        self.assertEqual(say_block(["speedup        100.00 / 6.00          =  16.67×"]),
                         ["speedup, 100.00 over 6.00, equals, 16.67 times"])
        # a blank spacer or a lone rule between formulas is silence, not a table
        self.assertEqual(say_block(["x = 1", "", "  ─────", "y = 2"]), ["x equals 1", "y equals 2"])

    def test_time_calls_are_settled(self):
        """`y(0)` and `x(t)` read as calls, so they are not guesses; a bracket
        holding the calling letter, a subscript's bracket, and a coefficient
        glued to the letter are still flagged."""
        from mathpath.speech import ambiguous
        for run in ("y(0)", "x(t) = x + t·d", "y(tₙ)", "u(t − c)", "y(−1/2)"):
            with self.subTest(run=run):
                self.assertEqual(ambiguous(run), [])
        for run in ("y(t + y)", "w_a(t + p_a)", "t(the rest)", "μ(t)", "2y(0)", "c(9/10)²n"):
            with self.subTest(run=run):
                self.assertEqual(ambiguous(run), ["letter-call"])

    def test_markup_is_not_read(self):
        self.assertEqual(say("w(e) &le; w(g)"), "w of e is at most w of g")


class TestCapitalForms(unittest.TestCase):
    """Rules added for the Capital read-along; each also pins what it must NOT
    touch, because every rule here is global to all Subjects."""

    def test_grouped_thousands_are_one_number(self):
        cases = {
            "10,000": "10000",
            "1,000·3 + 3,000·4": "1000 times 3 plus 3000 times 4",
            "dominance: 1,001,000 > 1,000,000": "dominance, 1001000 is greater than 1000000",
            "990 / 50,940 = 11/566": "990 over 50940 equals 11 over 566",
            # a list is not a number: no group may continue or run into one
            "60,72,90,120,180,360": "60, 72, 90, 120, 180, 360",
            "(1, 2)": "1, 2",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_pounds_follow_the_amount(self):
        cases = {
            "£1,062": "1062 pounds",
            "E[winnings] = 3.5 − 2 = £1.50": "E of winnings equals 3.5 minus 2 equals 1.50 pounds",
            "−£10": "negative 10 pounds",
            "hours in £1": "hours in 1 pound",
            "£": "pounds",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_shillings_and_pence(self):
        cases = {
            "3s 6d": "3 shillings 6 pence",
            "100 × 1s 6d =": "100 times 1 shilling 6 pence equals",
            "24 · 1½d = 48 · ¾d = 3s":
                "24 times 1 and a half pence equals 48 times three farthings equals 3 shillings",
            "a halfpenny: ½d": "a halfpenny, a halfpenny",
            "10 hours:  36d / 10 = 3 3/5 d an hour":
                "10 hours, 36 pence over 10 equals 3 and 3 over 5 pence an hour",
            "12 · 6d = 72d = 6s": "12 times 6 pence equals 72 pence equals 6 shillings",
            "10s / 144 = 120d / 144 = 5/6 d a piece":
                "10 shillings over 144 equals 120 pence over 144 equals 5 over 6 of a penny a piece",
            "£24,883 4s": "24883 pounds 4 shillings",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_s_and_d_alone_are_not_money(self):
        """Surplus value, seconds, days and distances keep their readings."""
        cases = {
            "400c + 100v + 100s": "400 c plus 100 v plus 100 s",
            "40 · 3s = 120s": "40 times 3 s equals 120 s",
            "36d / 12": "36 d over 12",
            "two nines, and 1 d 11 h 51 min 9.58 s":
                "two nines, and 1 d 11 h 51 minutes 9.58 seconds",
            "RTT_min = 2d / (⅔c)": "RTT sub min equals 2 d over two thirds c",
            "25q + 10d": "25 q plus 10 d",
            "s / v": "s over v",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_departments(self):
        cases = {
            "I(v + s) = IIc": "Department one's v plus s, equals Department two's c",
            "IIc": "Department two's c",
            "Ic is replaced within Department I":
                "Department one's c is replaced within Department one",
            "within II: IIv + IIs = 1000":
                "within Department two, Department two's v plus Department two's s equals 1000",
            "revenue:  I(1000 + 1000) + II(500 + 500) = 3000":
                "revenue, Department one's 1000 plus 1000, plus Department two's 500 plus 500, equals 3000",
            "I:  4000c + 1000v + 1000s = 6000":
                "Department one, 4000 c plus 1000 v plus 1000 s equals 6000",
            "unsold:  100 of Department I's product": "unsold, 100 of Department one's product",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_roman_letters_elsewhere_are_letters(self):
        cases = {
            "DR II: successive capitals": "DR II, successive capitals",
            "II / (I + II)": "II over the quantity I plus II",
            "Is −2 ∈ A?": "I s negative 2 in A ?",
            "(I - gP)v = r": "the quantity I minus g P, times v equals r",
            "I(X; Y)": "I of X, Y",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)

    def test_short_words_are_words(self):
        cases = {
            "due = 500": "due equals 500",
            "out − in": "out minus in",
            "use = 3": "use equals 3",
            "gap = bound − incumbent": "gap equals bound minus incumbent",
            "straggler tax = 4.33×": "straggler tax equals 4.33 times",
            "x = net + tax": "x equals net plus tax",
            "cap = fixed issue + gold": "cap equals fixed issue plus gold",
            # still products when a number or a power touches them
            "4tax": "4 t A x",
            "ax + by": "A x plus b y",
        }
        for text, spoken in cases.items():
            with self.subTest(text=text):
                self.assertEqual(say(text), spoken)


class TestMathBlockPayload(unittest.TestCase):
    def test_a_string_payload_is_refused(self):
        """("math", "x = 1") would iterate the string and render one character
        per line; three Capital lessons shipped like that."""
        from mathpath import render
        with self.assertRaises(TypeError):
            render._block("math", "x = 1")
        with self.assertRaises(TypeError):
            render._mathblock("x = 1")
        self.assertIn('data-say="x equals 1"', render._block("math", ["x = 1"]))


class TestProseIslands(unittest.TestCase):
    """Math written into prose without backticks still reaches the voice as words."""

    def test_islands(self):
        from mathpath.speech import islands
        cases = {
            "For a nonzero series, compare |r| with 1 before any formula": ["|r|"],
            "Finish when |r| &lt; 1 is a question about rⁿ and S∞ is.": ["|r| &lt; 1", "rⁿ", "S∞"],
            "Factoring x² + bx + c": ["x² + bx + c"],
            "the same definition &ldquo;λ, μ and ρ&rdquo; gives": ["λ, μ", "ρ"],
            "A plain sentence with no math, not even a 2.": [],
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual([text[a:b] for a, b in islands(text)], expected)

    def test_render_marks_them_and_keeps_the_text(self):
        from mathpath import render
        out = render.inline("compare |r| with 1, then `rⁿ`")
        self.assertEqual(out, 'compare <span data-say="the absolute value of r">|r|</span> with 1, '
                              'then <span class="math" data-say="r to the power n">rⁿ</span>')


class TestReaderScript(unittest.TestCase):
    def test_parses_in_every_supported_browser(self):
        """The reader shares one <script> element with the theme, quiz, lab and
        progress code: syntax an older Safari cannot parse kills all of them."""
        from mathpath.readout import READOUT_JS
        for construct in ("(?<", "=>", "?.", "??", "`", "const ", "let "):
            self.assertNotIn(construct, READOUT_JS)

    def test_no_double_quotes(self):
        """The trading pages' copy contract lexes their scripts for string
        literals, and an earlier script on those pages holds an unmatched `"`.
        A double quote here would pair with it and swallow everything between."""
        from mathpath.readout import READOUT_JS
        self.assertNotIn('"', READOUT_JS)


# Program text, read by speech.say_code. Each of the first five was measured
# wrong under the mathematical rules before the dialect existed
# (docs/code-complete/PLAN.md section H.1): `!done` lost its negation and read
# the opposite of the page.
CODE_READINGS = {
    "a && b": "A and b",
    "a || b": "A or b",
    "!done": "not done",
    "int[] a = new int[n];": "array of int A is set to new int array of length n",
    "double[] prices = new double[n];": "array of double prices is set to new double array of length n",
    "x = -1.0;": "x is set to minus 1.0",
    "r = total % size;": "r is set to total mod size",
    "x = a - b;": "x is set to A minus b",
    "System.out.print(x);": "print x",
    "boolean isDomestic = MAX_RETRIES > 0;": "boolean is domestic is set to max retries is greater than 0",
    "public static void main(String[] args) {": "public static void main of array of string args",
    "final char sep = ',';": "final char sep is set to the character comma",
    "x != y": "x is not equal to y",
    "x == y": "x equals y",
    "if (!done && count < max) {": "if not done and count is less than max",
    "for (int i = 0; i < n; i++) {": "for int i is set to 0, i is less than n, i is incremented",
    "total += values[i];": "total is increased by values at index i",
    "count -= 2;": "count is decreased by 2",
    "i--;": "i is decremented",
    "--i;": "decrement i",
    "x = y++ + ++z;": "x is set to y is incremented plus increment z",
    "} else {": "else",
    "return !(a && b);": "return not, open bracket, A and b, close bracket",
    "return !a || !b;": "return not A or not b",
    "List<String> names = new ArrayList<>();": "list of string names is set to new array list",
    "Map<String, List<Integer>> byName;": "map of string and list of integer by name",
    "isDone = MAX_SIZE >= HTTPServer.count();":
        "is done is set to max size is at least HTTP server dot count",
    "System.out.println(\"Total: \" + total);": "print line Total plus total",
    "s = \"\";": "s is set to the empty string",
    "char c = 'a';": "char c is set to the character a",
    "double r = (double) a / b;": "double r is set to cast to double A divided by b",
    "for (String s : names) {": "for string s in names",
    "y = x > 0 ? x : -x;": "y is set to x is greater than 0, if so, x, otherwise, minus x",
    "x = (a + b) * c; // the sum first": "x is set to, open bracket, A plus b, close bracket, "
                                       "times c, comment, the sum first",
    "a &amp;&amp; b": "A and b",
}


class TestCodeDialect(unittest.TestCase):
    """speech.say_code: program text read as program text."""

    def test_pinned_readings(self):
        from mathpath.speech import say_code
        for text, spoken in CODE_READINGS.items():
            with self.subTest(text=text):
                self.assertEqual(say_code(text), spoken)
                self.assertEqual(unspoken(spoken), set())

    def test_the_global_rules_are_unchanged(self):
        """`!` is a factorial and `=` an equation everywhere the dialect is not
        asked for; Operations Research writes `||` as scheduling notation. The
        dialect is a second reader, never a change to the first."""
        self.assertEqual(say("n!"), "n factorial")
        self.assertEqual(say("x = 1"), "x equals 1")
        self.assertEqual(say("!done"), "done")
        self.assertEqual(say("a && b"), "A and and b")
        from mathpath.speech import say_code
        self.assertEqual(say_code("x = 1"), "x is set to 1")
        self.assertEqual(say_code("x = 1", override="x becomes one"), "x becomes one")

    def test_braces_and_semicolons_are_silent(self):
        from mathpath.speech import say_code
        for line in ("{", "}", ";", "};", "  }  "):
            with self.subTest(line=line):
                self.assertEqual(say_code(line), "")

    def test_a_block_skips_blank_lines_and_reads_no_table(self):
        from mathpath.speech import say_code_block
        lines = ["int a    = 1;", "", "int bb   = 22;", "int ccc  = 333;", "}"]
        # each line announced by its number; the blank line and the lone brace
        # say nothing, so their numbers are not announced either
        self.assertEqual(say_code_block(lines),
                         ["line 1, int A is set to 1", "line 3, int bb is set to 22",
                          "line 4, int ccc is set to 333"])
        self.assertEqual(say_code_block(lines, marked={3}),
                         ["line 1, int A is set to 1", "line 3, flagged, int bb is set to 22",
                          "line 4, int ccc is set to 333"])

    def test_keywords_are_words(self):
        """A three-letter keyword at the head of a line is a word, never letters."""
        from mathpath.speech import JAVA_KEYWORDS, say_code
        for word in ("int", "for", "new", "void", "char", "boolean", "static", "final"):
            with self.subTest(word=word):
                self.assertIn(word, JAVA_KEYWORDS)
                self.assertEqual(say_code(word), word)

    def test_dialect_comes_only_from_the_path(self):
        from mathpath.speech import CODE_DIALECT, dialect_of
        self.assertIsNone(dialect_of({"slug": "algebra"}))
        self.assertEqual(dialect_of({"slug": "cc", "speech": "code"}), CODE_DIALECT)
        with self.assertRaises(ValueError):
            dialect_of({"slug": "cc", "speech": "java"})


def _code_path():
    """A copy of a real Subject marked "speech": "code", with a code block,
    prose runs, and code in its key and worked lines, as the Code Complete
    lessons will be written."""
    import copy
    from discrete_math import PATH
    path = copy.deepcopy(PATH)
    path["speech"] = "code"
    course = path["courses"][0]
    lesson = course["lessons"][0]
    lesson["key"] = ["if (!done && i < n)", "List<String> names", "a || b"]
    lesson["worked"]["lines"] = ["count += 1;", "return !(a && b);"]
    lesson["body"].insert(1, ("code", CODE_BLOCK))
    lesson["body"].insert(2, ("p", "So `!done && ready` holds, `List<String>` is a type, `a || b`."))
    return path, course, lesson


CODE_BLOCK = [
    "// generics and && must show as written",
    "List<String> names = new ArrayList<>();",
    "if (!done && names.size() > 0) {",
    "",
    "    names.add(\"a < b\");",
    "}",
]


def _render(path, course, lesson):
    from mathpath import render
    return render.lesson_page(path=path, course=course, lesson=lesson, index=0,
                              prev_lesson=None, next_lesson=course["lessons"][1])


class TestCodeBlock(unittest.TestCase):
    """The `code` body block (render._codeblock)."""

    def test_a_string_payload_is_refused(self):
        from mathpath import render
        with self.assertRaises(TypeError):
            render._block("code", "x = 1;")
        with self.assertRaises(TypeError):
            render._block("code", ["x = 1;", 2])

    def test_limits(self):
        from mathpath import render
        for bad in (["x;"] * 31, ["x" * 81], ["\tx = 1;"], ["a &lt; b"], ["a\nb"], []):
            with self.subTest(bad=bad[:2]):
                self.assertTrue(render.code_block_problems(bad))
                with self.assertRaises(ValueError):
                    render._block("code", bad)
        self.assertEqual(render.code_block_problems(["x;"] * 30 + []), [])
        self.assertEqual(render.code_block_problems(["x" * 80]), [])

    def test_markup_escapes_and_numbers_by_css(self):
        from mathpath import render
        out = render._block("code", CODE_BLOCK)
        self.assertTrue(out.startswith('<pre class="codeblock" data-say="'))
        self.assertIn("<code>", out)
        self.assertIn('<span class="cl">List&lt;String&gt; names = new ArrayList&lt;&gt;();</span>', out)
        self.assertIn('<span class="cl">if (!done &amp;&amp; names.size() &gt; 0) {</span>', out)
        self.assertIn('<span class="cl">    names.add(&quot;a &lt; b&quot;);</span>', out)
        self.assertIn('<span class="cl"></span>', out)  # a blank line keeps its number
        # one span per line, newline-separated, and no number in the text:
        # copying the listing copies the code alone
        body = re.search(r"<code>(.*)</code>", out, re.S).group(1)
        self.assertEqual(re.sub(r"<[^>]+>", "", body).split("\n"),
                         [__import__("html").escape(l) for l in CODE_BLOCK])
        self.assertNotRegex(body, r">\s*\d+\s*<")

    def test_spoken_in_the_code_dialect_on_every_subject(self):
        from mathpath import render
        out = render._block("code", CODE_BLOCK)
        spoken = __import__("html").unescape(re.search(r'data-say="([^"]*)"', out).group(1))
        self.assertEqual(spoken, "line 1, comment, generics and must show as written. "
                                 "line 2, list of string names is set to new array list. "
                                 "line 3, if not done and names dot size is greater than 0. "
                                 "line 5, names dot add of a b")

    def test_marked_lines(self):
        """A flagged line: a gutter glyph and a hidden word, never colour
        alone; both are generated content, so a copy is still the code."""
        from mathpath import render, theme
        out = render._block("code", {"lines": CODE_BLOCK, "marked": [3]})
        self.assertIn('<span class="cl flag">if (!done &amp;&amp; names.size() &gt; 0) {</span>', out)
        self.assertEqual(out.count('"cl flag"'), 1)
        self.assertIn("line 3, flagged, if not done", out)
        rule = re.search(r"\.codeblock \.flag::before \{([^}]*)\}", theme.CODE_CSS).group(1)
        self.assertIn('/ "flagged, line " counter(code-line);', rule)  # the hidden word
        self.assertIn("25B6", rule)                                     # the glyph
        self.assertIn("font-weight: 700", rule)                         # not colour alone
        self.assertEqual(render.code_lines({"lines": CODE_BLOCK, "marked": [3]}), CODE_BLOCK)
        for bad in ({"lines": CODE_BLOCK, "marked": [7]}, {"lines": CODE_BLOCK, "marked": "3"},
                    {"lines": CODE_BLOCK, "flag": [1]}, {"marked": [1]}):
            with self.subTest(bad=bad.get("marked")):
                self.assertTrue(render.code_block_problems(bad))
                with self.assertRaises((TypeError, ValueError)):
                    render._block("code", bad)

    def test_styles_ship_only_with_a_code_block(self):
        from mathpath import theme
        path, course, lesson = _code_path()
        with_code = _render(path, course, lesson)
        self.assertEqual(with_code.count(theme.CODE_CSS), 1)
        self.assertIn('aria-label="Code listing"', with_code)
        lesson["body"] = [b for b in lesson["body"] if b[0] != "code"]
        self.assertNotIn(".codeblock", _render(path, course, lesson))

    def test_listen_reads_a_code_block_and_announces_any_other_pre(self):
        from mathpath.readout import READOUT_JS
        self.assertIn("el.matches('pre:not([data-say])')", READOUT_JS)
        self.assertIn("table,pre,", READOUT_JS)  # a <pre> is still a block Listen visits


class TestCodeDialectRendering(unittest.TestCase):
    """On a "speech": "code" Subject every run, key line and worked line is
    program text; on every other Subject nothing changes."""

    def test_runs_key_and_worked_lines_use_the_dialect(self):
        import html as h
        path, course, lesson = _code_path()
        page = _render(path, course, lesson)
        said = [h.unescape(x) for x in re.findall(r'data-say="([^"]*)"', page)]
        self.assertIn("not done and ready", said)
        self.assertIn("list of string", said)
        self.assertIn("A or b", said)
        self.assertIn("if not done and i is less than n. list of string names. A or b", said)
        self.assertIn("count is increased by 1. return not, open bracket, A and b, close bracket", said)
        # shown exactly as written, not opened as a tag
        self.assertIn(">!done &amp;&amp; ready</span>", page)
        self.assertIn(">List&lt;String&gt;</span>", page)

    def test_no_code_run_reaches_plain_say(self):
        """On a code Subject, a run holding `&&`, `||` or a prefix `!` read by
        the mathematical rules is a failure: it is how `!done` read "done"."""
        from mathpath import render, speech
        code_op = re.compile(r"&&|&amp;&amp;|\|\||(?<![\w)\]!=<>])!(?!=)")
        real, leaked = speech.say, []

        def watched(text, **kw):
            if code_op.search(text):
                leaked.append(text)
            return real(text, **kw)

        render._say_in.cache_clear()
        speech.say = watched
        try:
            _render(*_code_path())
            self.assertEqual(leaked, [])
            # the watch is not inert: the same content on a math Subject does
            # reach plain say
            path, course, lesson = _code_path()
            del path["speech"]
            render._say_in.cache_clear()
            _render(path, course, lesson)
            self.assertIn("!done && ready", leaked)
        finally:
            speech.say = real
            render._say_in.cache_clear()

    def test_an_unknown_dialect_is_refused(self):
        path, course, lesson = _code_path()
        path["speech"] = "java"
        with self.assertRaises(ValueError):
            _render(path, course, lesson)


def _prose_islands(path):
    """Every math island in a Subject's prose: the runs written without
    backticks that render._prose gives a spoken form (speech.islands), read
    from the same strings and split on tags the same way."""
    from mathpath.speech import islands
    tag, span = re.compile(r"(<[^>]+>)"), re.compile(r"`[^`]*`")

    def strings(node):
        if isinstance(node, str):
            yield node
        elif isinstance(node, dict):
            for key, value in node.items():
                if key not in ("key", "lines"):
                    yield from strings(value)
        elif isinstance(node, (list, tuple)):
            if not (isinstance(node, tuple) and len(node) == 2 and node[0] in ("math", "code")):
                for item in node:
                    yield from strings(item)

    found = set()
    for text in strings(path):
        for piece in tag.split(span.sub(" ", text)):
            if not piece.startswith("<"):
                for start, end in islands(piece):
                    found.add(piece[start:end])
    return found


def _sound_islands(path):
    """Every sound or stress-mark island in a Subject's prose (speech.islands)."""
    from mathpath.speech import _IPA, _STRESS
    return {island for island in _prose_islands(path)
            if _IPA.search(island) or _STRESS.match(island)}


class TestCoverage(unittest.TestCase):
    """Every run on the six generated paths is spoken, and nothing is guessed."""

    @classmethod
    def setUpClass(cls):
        from speechcheck import code_lines, reading, runs, subjects, unresolved

        cls.subjects = list(subjects())
        cls.runs, cls.unresolved = staticmethod(runs), staticmethod(unresolved)
        cls.code_lines, cls.reading = staticmethod(code_lines), staticmethod(reading)

    def test_every_run_is_spoken(self):
        for path, overrides in self.subjects:
            residue = {}
            for run, _, _ in self.runs(path):
                for ch in unspoken(self.reading(path, run, overrides)):
                    residue.setdefault(ch, run)
            with self.subTest(path=path["slug"]):
                self.assertEqual(
                    residue, {},
                    "symbols with no spoken form (add them to speech.SYMBOLS, "
                    "or give the run a spoken form): %r" % residue)

    def test_every_code_line_is_spoken(self):
        """A `code` block is read by say_code on every Subject."""
        from mathpath.speech import say_code
        for path, overrides in self.subjects:
            residue = {}
            for line, _ in self.code_lines(path):
                for ch in unspoken(overrides.get(line) or say_code(line)):
                    residue.setdefault(ch, line)
            with self.subTest(path=path["slug"]):
                self.assertEqual(residue, {}, "code with no spoken form: %r" % residue)

    def test_the_coverage_checks_use_the_subjects_reader(self):
        from speechcheck import reader, reading, unresolved
        from mathpath.speech import say_code
        path, _, _ = _code_path()
        self.assertIs(reader(path), say_code)
        self.assertEqual(reading(path, "!done", {}), "not done")
        self.assertEqual(reading(path, "!done", {"!done": "not yet done"}), "not yet done")
        self.assertEqual(unresolved(path, {}), [])  # f(x) is a call in code, not a guess
        path.pop("speech")
        self.assertIs(reader(path), say)

    def test_spoken_forms_are_words(self):
        for path, overrides in self.subjects:
            for run, spoken in overrides.items():
                with self.subTest(path=path["slug"], run=run):
                    self.assertTrue(spoken.strip())
                    self.assertEqual(unspoken(spoken), set())

    def test_no_spoken_form_for_math_that_is_gone(self):
        """A spoken form keyed to a run the content no longer has is dead data,
        and the next edit to that line silently loses its reading. A prose
        island counts as present: render._prose speaks it with its spoken
        form (Phenomenology's `ho_se` and `_a_e` are read that way)."""
        for path, overrides in self.subjects:
            present = {run for run, _, _ in self.runs(path)} | _prose_islands(path) \
                | {line for line, _ in self.code_lines(path)}
            with self.subTest(path=path["slug"]):
                self.assertEqual(sorted(set(overrides) - present), [])

    def test_one_reading_per_run(self):
        """The page renderer merges every subject's spoken forms, so a run
        written in two subjects must not be given two readings."""
        seen, clashes = {}, []
        for path, overrides in self.subjects:
            for run, spoken in overrides.items():
                if run in seen and seen[run][1] != spoken:
                    clashes.append((run, seen[run][0], path["slug"]))
                seen.setdefault(run, (path["slug"], spoken))
        self.assertEqual(clashes, [])

    def test_no_spoken_form_for_a_bare_tuple(self):
        """Spoken forms are shared by every Subject, and a bare tuple means
        different things in different places: `(a, b)` is a pair in a
        relation and an open interval in Algebra. Calling it "the pair a, b"
        everywhere misreads the interval, so a tuple keeps the rules' reading."""
        tuple_run = re.compile(r"\(\s*[^(),]+\s*(,\s*[^(),]+\s*)+\)")
        for path, overrides in self.subjects:
            with self.subTest(path=path["slug"]):
                self.assertEqual([run for run in overrides if tuple_run.fullmatch(run)], [])

    def test_no_spoken_form_for_a_lone_symbol(self):
        """A single symbol's reading belongs to speech.SYMBOLS, which every
        Subject shares. Philosophy once keyed `□` to its epistemic gloss for
        one lesson, which would have read the necessity of every modal lesson
        as knowledge."""
        for path, overrides in self.subjects:
            with self.subTest(path=path["slug"]):
                self.assertEqual([run for run in overrides if len(run.strip()) == 1], [])

    def test_every_sound_in_prose_is_spoken(self):
        """A pronunciation spelling (<dfn>tə</dfn>) or a stress pattern (s.S.)
        written into prose becomes an island at build time, but the rules have
        no words for it: a voice would read it letter by letter. Each needs a
        spoken form in its Subject's file."""
        for path, overrides in self.subjects:
            with self.subTest(path=path["slug"]):
                self.assertEqual(sorted(i for i in _sound_islands(path) if i not in overrides), [])

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
