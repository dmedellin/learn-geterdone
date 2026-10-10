"""Separable Equations, Growth and Decay -- the second half.

Decay and dating, cooling, mixing, and then the two bounded-growth lessons:
logistic growth and the harvested logistic. The first three run the same
`growth` mode as the lessons before them, because Newton's law and the tank are
y' = k*(y - A) with A the level the quantity approaches; the last two run the
`autonomous` mode, because the logistic equation is not of that form and is read
from its equilibria and from exact Euler steps rather than from a formula.

Every tile pinned in `expect` was read off the built page with
scripts/labcheck.js --observe. Arithmetic in the prose that is not a tile was
computed with fractions.Fraction; a value of e^(kt) or ln 2 is rounded and
carries the approximation sign wherever it appears. Where this file and PLAN.md
section C disagree the lab won, and the disagreement is reported with the
lesson, not copied.
"""


def _p(pid, label, f, starts, h, n, window, expect):
    return {"id": pid, "label": label, "f": f, "starts": starts, "h": h, "n": n,
            "window": window, "expect": expect}


LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "radioactive-decay-and-dating",
        "title": "Radioactive Decay and Dating",
        "module": "Exponential change",
        "one_line": "Decay is the growth equation with a negative rate, a half-life converts to a rate and back through ln 2, and the fraction of a sample that is left says how many half-lives have passed.",
        "summary": (
            "A radioactive sample loses atoms at a rate proportional to the number it has, "
            "which is the decay equation `y′ = −k·y` with `k > 0`. Its half-life `T` and its "
            "rate are tied by `k·T = ln 2`, so each converts to the other, rounded because "
            "`ln 2` is irrational. A sample that has a quarter of its original amount left has "
            "been through two half-lives, and the lab prints both that age and the first "
            "step at which the exact Euler sequence has fallen that far."
        ),
        "key": [
            "y′ = −k·y,  k > 0  ⟹  y = y₀·e^(−kt)",
            "half-life T:  k·T = ln 2",
            "ln 2 ≈ 0.693147   (rounded)",
            "a quarter left:  two half-lives, age 2T",
            "k = 3/25000:  T ≈ 5776.23 years",
        ],
        "key_label": "Decay, half-life and age",
        "concepts_intro": (
            "Three ideas: what the sign convention is, how a half-life and a rate are the same "
            "information, and how a remaining fraction becomes an age."
        ),
        "concepts": [
            ("Decay is the growth equation with a minus sign",
             "Write `y′ = −k·y` with `k > 0`, so that `k` is the size of the rate and the "
             "minus sign carries the direction. The solution is `y₀·e^(−kt)` by the same "
             "separation as before. The lab takes the signed number, so the rate "
             "`k = 3/25000` of this lesson is typed as `−3/25000`."),
            ("A half-life and a rate are one fact",
             "The sample has halved when `e^(−kT) = 1/2`, which is `k·T = ln 2`. Give either "
             "`T` or `k` and the other follows: `T = ln 2/k` and `k = ln 2/T`. Because "
             "`ln 2` is irrational, a conversion from a measured half-life produces a rounded "
             "rate, and a rational rate produces a rounded half-life."),
            ("The fraction that is left counts half-lives",
             "After `m` half-lives a fraction `1/2` multiplied `m` times is left. So a quarter "
             "means `m = 2` and an eighth means `m = 3`. A fraction that is not a power of "
             "`1/2` falls between two of them, and its age needs a logarithm."),
        ],
        "read_title": "From a half-life to a rate, and from what is left to an age",
        "read_intro": "The sign convention, the two conversions, and an age worked from a quarter of the original amount, with the lab's exact steps beside the rounded half-life.",
        "body": [
            ("p", "Carbon dating rests on one observation: a radioactive atom has the same "
                  "chance of decaying in any given year, whatever its age, so the number of "
                  "atoms that decay in a year is proportional to the number still there. "
                  "That is a rate proportional to the size, the equation of &ldquo;Exponential "
                  "Growth&rdquo; with the direction reversed."),
            ("def", ("Radioactive decay",
                     "A quantity <strong>decays</strong> at rate constant `k > 0` when "
                     "`y′ = −k·y`. Its <strong>half-life</strong> `T` is the time in which "
                     "any amount falls to half.",
                     "The sign is written outside `k` so that `k` can be read as a size. In "
                     "the lab the rate box holds the signed coefficient, `−k`.")),
            ("p", "The solution is `y = y₀·e^(−kt)`, by the same separation. It has halved "
                  "when `e^(−kT) = 1/2`, and taking the natural logarithm of both sides gives "
                  "`−kT = −ln 2`. That is the same relation as the doubling time of the "
                  "previous lesson, with the same independence from the start."),
            ("math", [
                "y′ = −k·y,   y = y₀·e^(−kt)",
                "",
                "  halved when   e^(−kT) = 1/2",
                "  k·T = ln 2",
                "",
                "  T = ln 2/k          k = ln 2/T",
                "",
                "k = 3/25000 per year:",
                "  T = (25000/3)·ln 2   ≈ 5776.23 years   (rounded)",
            ]),
            ("h3", "Which rate the lab uses"),
            ("p", "A measured half-life for carbon-14 is commonly quoted as about 5730 years. "
                  "Turning it into a rate gives `ln 2/5730`, which is irrational, and Euler's "
                  "factor would then be rounded. The lab instead uses the fraction "
                  "`k = 3/25000` per year, which is `0.00012`: a rate that keeps every Euler "
                  "step exact, and a half-life that prints as `≈ 5776.23`, close to the "
                  "measured one and not equal to it. That difference is the cost of choosing "
                  "a rational rate, and it is stated here so that the lab's age is not read as "
                  "a measurement."),
            ("h3", "From what is left to an age"),
            ("p", "If a fraction `f` of the original is left, then `e^(−kt) = f`, and the "
                  "age is `t = ln(1/f)/k`. For the fractions that are powers of one half "
                  "this needs no new calculation, because each halving costs one `T`."),
            ("math", [
                "  time since start     fraction left",
                "",
                "      0                    1",
                "      T                    1/2",
                "      2T                   1/4",
                "      3T                   1/8",
                "",
                "  a sample with 15% left lies between 2T and 3T,",
                "  since 1/8 < 15% < 1/4",
            ]),
            ("p", "The last line is a check that needs no logarithm: it brackets the age "
                  "before any rounded figure is computed, and a rounded answer outside the "
                  "bracket is wrong."),
            ("h3", "The exact sequence beside it"),
            ("p", "With a step of one century the Euler factor is `1 − 100·(3/25000) = 247/250`, "
                  "an exact fraction, and the sequence `(247/250)ⁿ` is geometric as before. The "
                  "lab prints the first step at which it has fallen to one half or below. The "
                  "step is a whole number of centuries, so it lands near the half-life "
                  "`≈ 5776.23` on the grid and not on it."),
            ("example", ("A quarter left",
                         "Switch the lab to the second preset, whose target is `1/4` and "
                         "whose step is 200 years. The half-life tile still reads "
                         "`≈ 5776.23`, because that tile depends on the rate and not on the "
                         "target. The age of a sample with a quarter left is twice it, "
                         "`≈ 11552.5` years, a figure the reader computes from the tile "
                         "and the lab does not print. The step tile gives the grid's "
                         "version of the same crossing: `step 58 (t = 11600)`, which is "
                         "within one 200-year step of `≈ 11552.5`.")),
            ("p", "The third preset is the same arithmetic with round numbers: a rate of "
                  "`1/4` per unit time, a start of 100 and a target of 50. The factor is "
                  "`3/4`; `(3/4)² = 9/16` is still above one half and `(3/4)³ = 27/64` is "
                  "below it, so the lab prints `step 3 (t = 3)` while the half-life tile "
                  "reads `≈ 2.77259`, which is `4·ln 2`, rounded."),
            ("p", "What dating assumes should be said as plainly as what it computes. It "
                  "assumes the sample began with a known amount, that nothing entered or "
                  "left it except by decay, and that the rate constant has not changed. The "
                  "lab computes what follows from those assumptions; whether they hold for a "
                  "particular sample is not something it can tell you."),
        ],
        "lab": ("dekit", {
            "mode": "growth",
            "preset": "carbon",
            "presets": [
                {"id": "carbon", "label": "k = −3/25000 per year, y(0) = 1, h = 100, target 1/2",
                 "k": "-3/25000", "y0": 1, "A": 0, "h": 100, "n": 64, "target": "1/2",
                 "expect": {"grFactor": "247/250", "grT": "≈ 5776.23", "grHit": "step 58 (t = 5800)"}},
                {"id": "quarter", "label": "k = −3/25000 per year, y(0) = 1, h = 200, target 1/4",
                 "k": "-3/25000", "y0": 1, "A": 0, "h": 200, "n": 64, "target": "1/4",
                 "expect": {"grFactor": "122/125", "grT": "≈ 5776.23", "grHit": "step 58 (t = 11600)"}},
                {"id": "fast", "label": "k = −1/4, y(0) = 100, h = 1, target 50",
                 "k": "-1/4", "y0": 100, "A": 0, "h": 1, "n": 8, "target": 50,
                 "expect": {"grFactor": "3/4", "grT": "≈ 2.77259", "grHit": "step 3 (t = 3)"}},
            ],
            "panel_title": "A decay rate, its half-life, and the step that crosses",
            "panel_intro": (
                "The rate box holds the signed coefficient, so a decay rate is typed with its "
                "minus sign. The factor tile is the exact Euler multiplier 1 + kh. The "
                "half-life tile is ln 2 over the size of k, rounded; the step tile is the "
                "first exact value at or below the target. Move the target to 1/8 on the "
                "first preset and watch only the step and its time change."
            ),
        }),
        "steps_title": "Dating a sample",
        "steps_intro": "Five moves. The bracket in the third is the one that catches an arithmetic slip before it is reported.",
        "steps": [
            ("Write the rate with its sign",
             "Decay is `y′ = −k·y` with `k > 0`. If you are given a half-life `T`, the rate is "
             "`k = ln 2/T`, rounded; if you are given `k`, the half-life is `T = ln 2/k`."),
            ("Turn the measurement into a fraction",
             "Divide what is left now by what was there at the start. A quarter is `1/4`, "
             "fifteen percent is `15/100`."),
            ("Bracket the age in half-lives",
             "Find the powers of `1/2` on either side of the fraction. A quarter is exactly two "
             "half-lives; fifteen percent lies between two and three."),
            ("Compute the age",
             "For a power of one half the age is the number of half-lives times `T`. For any "
             "other fraction it is `ln(1/f)/k`, rounded and marked `≈`."),
            ("State what was assumed",
             "Name the rate constant, the starting amount and the closed system. The age is "
             "exactly as good as those three."),
        ],
        "worked": {
            "title": "A sample with a quarter of its carbon left",
            "intro": [
                "The rate is the lab's `k = 3/25000` per year. The exact lines are fractions, "
                "and the lines with a logarithm in them are rounded and say so."
            ],
            "lines": [
                "y′ = −k·y,   k = 3/25000 per year",
                "half-life   T = ln 2/k = (25000/3)·ln 2",
                "                     ≈ 5776.23 years   (rounded)",
                "",
                "a quarter left = (1/2)·(1/2): two half-lives",
                "age         2T = (50000/3)·ln 2",
                "                     ≈ 11552.5 years   (rounded)",
                "",
                "Euler, h = 200:  factor 1 − 600/25000 = 122/125",
            ],
            "after": [
                "The exact sequence `(122/125)ⁿ` is a geometric sequence that never reaches "
                "zero, and the lab prints the first step at which it is at or below `1/4`. That "
                "step is a whole number of 200-year steps, so it sits within one step of the "
                "true age and is not the true age.",
                "Had the sample held fifteen percent, the bracket from the table says its age "
                "lies between `2T` and `3T`, which is between `≈ 11552.5` and `≈ 17328.7` years. "
                "A computed age outside that range would be a slip.",
            ],
        },
        "quiz_title": "Half-lives and ages",
        "quiz": [
            {"q": "A sample has been through three half-lives. What fraction of the original amount remains?",
             "a": ["None: it has all decayed", "`1/6`", "`1/8`", "`1/3`"],
             "c": 2,
             "why": "Each half-life halves what is there, so three of them leave "
                    "`(1/2)·(1/2)·(1/2) = 1/8`. The decay is a multiplication by one half "
                    "at each stage, so it never reaches nothing; `1/6` and `1/3` come from "
                    "dividing or subtracting by the number of half-lives instead."},
            {"q": "A sample has a quarter of its original amount and its half-life is 5000 years. How old is it?",
             "a": ["2500 years", "10000 years", "20000 years", "15000 years"],
             "c": 1,
             "why": "A quarter is two halvings, so the age is `2·5000 = 10000` years. "
                    "The value 2500 divides by two, 15000 is three half-lives, and 20000 "
                    "multiplies by four, which is the reciprocal of the fraction left and "
                    "not the count of halvings."},
            {"q": "Which equation has a half-life of `ln 2/3`?",
             "a": ["`y′ = −y/3`", "`y′ = 3y`", "`y′ = −(ln 2)·y`", "`y′ = −3y`"],
             "c": 3,
             "why": "A half-life of `ln 2/k` needs `k = 3` and a decaying quantity, "
                    "so `y′ = −3y`. The equation `y′ = 3y` has doubling time `ln 2/3`, but "
                    "it grows. The first choice has half-life `3·ln 2`, and the third has "
                    "half-life exactly 1."},
            {"q": "The lab's first preset prints the half-life `≈ 5776.23` and a step with a time of 5800 years. Which of these is the half-life of the equation?",
             "a": ["`≈ 5776.23` years", "5800 years", "58 years", "`247/250` years"],
             "c": 0,
             "why": "The half-life is `ln 2/k`, rounded. The time 5800 is a multiple of the "
                    "100-year step: the first grid time at which the exact sequence is at or "
                    "below one half. The number 58 is the step count and `247/250` is the "
                    "Euler factor per step."},
        ],
        "mistakes": [
            ("Believing that after two half-lives nothing is left",
             "The mistaken model is that a half-life is half the sample's life, so two of "
             "them use it all up. A half-life halves what is there, and half of a half is a "
             "quarter, not zero: after two the fraction is `1/4`, after three `1/8`. The "
             "exact Euler sequence shows the same thing with fractions, since `(247/250)ⁿ` is a "
             "positive number for every `n`; the lab's second preset passes `1/4` and the "
             "sequence goes on."),
            ("Typing a decay rate with the wrong sign",
             "In the equation the rate is written `y′ = −k·y` with `k > 0`, and the lab "
             "wants the signed coefficient, `−3/25000`. Typing the positive `3/25000` there "
             "is a growth equation: the table rises, and the half-life tile, which uses "
             "the size of the rate, reads exactly as before and hides the mistake. If a "
             "decay preset grows, look at the sign first."),
            ("Taking 1/k for the half-life",
             "The number `1/k` is `25000/3`, about 8333 years, and it is the time for the amount "
             "to fall to `1/e` of what it was. The half-life carries the factor `ln 2`, so "
             "`T = ln 2/k ≈ 5776.23`, which is shorter by that factor. The check is that "
             "`k·T` must equal `ln 2`, not 1."),
        ],
        "standard": ("Finish when you can convert a half-life to a rate and back and date a sample from the fraction left.",
                     "You should be able to write decay as `y′ = −k·y`, derive "
                     "`k·T = ln 2`, convert in both directions with the result marked "
                     "rounded, bracket an age between two half-lives, and say what the "
                     "dating assumes."),
        "note": "Decay toward zero is one case of a more general shape: a quantity that moves toward a level that is not zero. &ldquo;Newton's Law of Cooling&rdquo; puts a shift into the same equation, and a substitution turns it back into the decay of this lesson.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "newtons-law-of-cooling",
        "title": "Newton's Law of Cooling",
        "module": "Exponential change",
        "one_line": "An object changes at a rate proportional to the gap between its temperature and its surroundings, so the gap decays exponentially and the temperature levels off at the surroundings' value.",
        "summary": (
            "Newton's law says `y′ = −k·(y − A)`: the object changes at a rate proportional "
            "to how far it is from the surrounding temperature `A`. Substituting `u = y − A` "
            "turns it into the pure decay `u′ = −k·u`, so the gap shrinks geometrically in "
            "Euler's method and exponentially in the solution, and the temperature settles at "
            "`A`. The rate is large while the gap is large and small near the end, which is "
            "not a constant rate of cooling."
        ),
        "key": [
            "y′ = −k·(y − A),  k > 0",
            "u = y − A  ⟹  u′ = −k·u",
            "y = A + (y₀ − A)·e^(−kt)",
            "Euler: the gap is multiplied by 1 − kh",
            "coffee: y₄ = 725/16;  true ≈ 49.4304",
        ],
        "key_label": "Cooling is decay of the gap",
        "concepts_intro": (
            "Three ideas: what the rate is proportional to, the substitution that reduces the "
            "equation to one already solved, and where the temperature ends up."
        ),
        "concepts": [
            ("The rate follows the gap",
             "The object changes fastest when it is far from the surroundings and slowly when "
             "it is near them. The equation `y′ = −k·(y − A)` has a negative rate while "
             "`y > A` and a positive one while `y < A`, so it covers cooling and warming "
             "alike."),
            ("One substitution gives decay",
             "Put `u = y − A`. Since `A` is a constant, `u′ = y′`, and the equation becomes "
             "`u′ = −k·u`: the decay of the previous lesson, for the gap. So "
             "`u = u₀·e^(−kt)` and `y = A + (y₀ − A)·e^(−kt)`."),
            ("The temperature approaches A and does not reach it",
             "The gap `u₀·e^(−kt)` is never zero. The value `A` is an equilibrium: start "
             "there and `y′ = 0`. Start anywhere else and the temperature moves towards `A` "
             "forever and arrives at no time."),
        ],
        "read_title": "A cup of coffee, step by step",
        "read_intro": "The law, the substitution, the coffee's first four steps in exact fractions beside the closed form, and a cold cup warming by the same equation.",
        "body": [
            ("p", "A cup of coffee at 100 degrees stands in a room at 20 degrees. Newton's "
                  "observation was that it loses heat at a rate proportional to how much "
                  "hotter it is than the room. Write `y` for its temperature and take the "
                  "constant of proportionality to be `k = 1/4` per minute."),
            ("def", ("Newton's law of cooling",
                     "A body at temperature `y` in surroundings at the constant temperature "
                     "`A` obeys `y′ = −k·(y − A)` for a constant `k > 0`.",
                     "It assumes the surroundings stay at `A` and the body has one "
                     "temperature throughout. The lab computes what follows from those "
                     "assumptions; it does not check them for a real cup.")),
            ("math", [
                "y′ = −(1/4)·(y − 20),   y(0) = 100",
                "",
                "  u = y − 20      u(0) = 80",
                "  u′ = y′ = −(1/4)·u",
                "  u = 80·e^(−t/4)",
                "",
                "  y = 20 + 80·e^(−t/4)",
            ]),
            ("p", "The check is by differentiating: the rate of `20 + 80·e^(−t/4)` is "
                  "`−20·e^(−t/4)`, and `−(1/4)·(y − 20) = −(1/4)·80·e^(−t/4)`, the same. "
                  "The temperature at time `t` is a rounded number, since `e^(−t/4)` is "
                  "irrational for `t ≠ 0`, which is why a check by differentiating is the "
                  "right check and an evaluation is not."),
            ("h3", "The rate is not constant"),
            ("p", "Run Euler's method with a step of one minute. The first step uses the "
                  "starting rate `−(1/4)·(100 − 20) = −20`, so `y₁ = 80`. The gap is now 60 "
                  "and the rate `−15`, so `y₂ = 65`. Then the gap is 45 and the rate is "
                  "`−45/4`, so `y₃ = 215/4`. The rate changes at every step because the gap "
                  "does."),
            ("math", [
                "  step n     gap yₙ − 20     rate −(1/4)·(yₙ − 20)",
                "",
                "    0           80              −20",
                "    1           60              −15",
                "    2           45              −45/4",
                "    3           135/4           −135/16",
                "",
                "  each gap is the one before times 3/4 = 1 − kh",
            ]),
            ("p", "The gap is multiplied by `1 − kh = 1 − 1/4 = 3/4` at every step (the lab's "
                  "factor tile, which takes the signed rate `−1/4`, writes the same number as "
                  "`1 + kh`), so "
                  "`yₙ = 20 + 80·(3/4)ⁿ`. At `n = 4` that is `20 + 80·81/256 = 725/16`, which "
                  "is `45.3125`, and the lab prints it exactly. The closed form at "
                  "`t = 4` is `20 + 80·e^(−1)`, which the lab prints rounded: `≈ 49.4304`. "
                  "The two differ because a step of one minute assumes the rate stays put for "
                  "the whole minute, while the true rate keeps falling. The lab's error tile "
                  "prints the gap as `≈ 4.11786`, rounded, and it is the method's error at "
                  "this step size and no other."),
            ("h3", "The same equation warms a cold cup"),
            ("p", "A cup at 5 degrees in a room at 20 has a gap of `5 − 20 = −15`, a negative "
                  "gap, and the rate `−k·(−15)` is positive. Nothing else changes. With "
                  "`k = 1/2` and a step of 1 the factor is `1/2`, so the gap is cut in half "
                  "at every step: `−15, −15/2, −15/4, …`. The temperatures `5, 25/2, 65/4, "
                  "145/8, 305/16, …` climb towards 20 and none of them passes it; the lab's "
                  "closed form at the fourth step is `≈ 17.97`, rounded. The third preset "
                  "is a drink at 25 degrees in a fridge at 4: the gap is 21, the factor is "
                  "`9/10`, and the steady-state tile reads 4."),
            ("example", ("How long until the gap halves",
                         "The gap follows `u₀·e^(−kt)`, so it halves in `ln 2/k`, the "
                         "half-life of the previous lesson. For `k = 1/4` that is "
                         "`4·ln 2 ≈ 2.77259` minutes, and then the coffee is at "
                         "`20 + 40 = 60` degrees. With the target set to 60, the lab prints "
                         "the first step of the exact sequence at or below 60: "
                         "`step 3 (t = 3)`, where the sequence is at `215/4 = 53.75`, "
                         "having been at 65 one step earlier.")),
        ],
        "lab": ("dekit", {
            "mode": "growth",
            "preset": "coffee",
            "presets": [
                {"id": "coffee", "label": "k = −1/4, y(0) = 100, A = 20, h = 1, target 60",
                 "k": "-1/4", "y0": 100, "A": 20, "h": 1, "n": 4, "target": 60,
                 "expect": {"grFactor": "3/4", "grLast": "725/16", "grTrue": "≈ 49.4304", "grSteady": "20", "grT": "≈ 2.77259", "grHit": "step 3 (t = 3)"}},
                {"id": "warming", "label": "k = −1/2, y(0) = 5, A = 20, h = 1",
                 "k": "-1/2", "y0": 5, "A": 20, "h": 1, "n": 4, "target": None,
                 "expect": {"grFactor": "1/2", "grLast": "305/16", "grTrue": "≈ 17.97", "grSteady": "20"}},
                {"id": "fridge", "label": "k = −1/10, y(0) = 25, A = 4, h = 1",
                 "k": "-1/10", "y0": 25, "A": 4, "h": 1, "n": 8, "target": None,
                 "expect": {"grFactor": "9/10", "grLast": "1303981141/100000000", "grTrue": "≈ 13.4359", "grSteady": "4"}},
            ],
            "panel_title": "Cool toward the surroundings, or warm toward them",
            "panel_intro": (
                "A is the temperature of the surroundings, and the steady-state tile prints it. "
                "The factor tile multiplies the gap y − A at every step, not the temperature. "
                "The half-life tile is the time for the gap to halve, rounded. Set the start "
                "equal to A on any preset and nothing moves."
            ),
        }),
        "steps_title": "Solving a cooling problem",
        "steps_intro": "Five moves, and the substitution in the second is the one that reduces a new equation to an old one.",
        "steps": [
            ("Name the surroundings and the rate",
             "Read `A` and `k` off the equation `y′ = −k·(y − A)`. The lab takes the signed "
             "coefficient, `−k`."),
            ("Substitute the gap",
             "`u = y − A` gives `u′ = −k·u` with `u₀ = y₀ − A`. The sign of `u₀` says whether "
             "the object cools (positive) or warms (negative)."),
            ("Solve the decay",
             "`u = u₀·e^(−kt)`, so `y = A + (y₀ − A)·e^(−kt)`. Check it by differentiating."),
            ("Run Euler on the gap",
             "The factor `1 − kh` multiplies the gap each step, so `yₙ = A + (y₀ − A)·(1 − kh)ⁿ`, "
             "an exact fraction."),
            ("State both numbers with their tier",
             "The Euler value is exact, the closed form is rounded and marked `≈`, and the "
             "step size goes beside the pair."),
        ],
        "worked": {
            "title": "The coffee, four steps of one minute",
            "intro": [
                "The equation is `y′ = −(1/4)·(y − 20)` with `y(0) = 100` and `h = 1`. "
                "Everything is exact until the closed-form line."
            ],
            "lines": [
                "factor      1 − kh = 1 − 1/4 = 3/4  (on the gap)",
                "gap         u₀ = 100 − 20 = 80",
                "",
                "yₙ = 20 + 80·(3/4)ⁿ",
                "y₁ = 20 + 60 = 80",
                "y₂ = 20 + 45 = 65",
                "y₃ = 20 + 135/4 = 215/4",
                "y₄ = 20 + 80·81/256 = 725/16 = 45.3125",
                "",
                "closed form  20 + 80·e^(−1)   ≈ 49.4304   (rounded)",
            ],
            "after": [
                "Euler is below the curve here, by the amount the lab's error tile prints. "
                "The reason is the one in the table above: each step took the rate at the "
                "start of the minute, and the real rate falls during it, so the real "
                "coffee had cooled less than the sequence says.",
                "The steady state is 20. In the closed form the term `80·e^(−t/4)` goes to zero "
                "without reaching it, and in the exact sequence `80·(3/4)ⁿ` is positive for every "
                "`n`.",
            ],
        },
        "quiz_title": "Rate, gap and steady state",
        "quiz": [
            {"q": "The coffee is at 100 degrees in a 20-degree room, and `k = 1/4`. What is `y′` at the start?",
             "a": ["`−25`", "`−5`", "`−80`", "`−20`"],
             "c": 3,
             "why": "`y′ = −(1/4)·(100 − 20) = −20`. The value `−25` uses the temperature, "
                    "100, instead of the gap; `−5` uses the room temperature, 20; and `−80` "
                    "is the gap itself with the rate constant left out."},
            {"q": "A cup at 5 degrees stands in a room at 20 degrees, `k = 1/2`. What happens?",
             "a": ["It warms towards 20 and never exceeds it", "It warms past 20 because its rate is positive",
                   "It stays at 5", "It cools below 5"],
             "c": 0,
             "why": "The gap is `−15`, so the rate `−(1/2)·(−15)` is positive and the cup "
                    "warms; the gap then shrinks as `−15·e^(−t/2)`, which is never zero, so "
                    "the temperature stays below 20. Positive rate does not mean unbounded: "
                    "the rate itself shrinks as the gap does."},
            {"q": "With `u = y − A`, which equation does `u` satisfy when `y′ = −k·(y − A)`?",
             "a": ["`u′ = −k·u − k·A`", "`u′ = −k·(u + A)`", "`u′ = −k·u`", "`u′ = −k·u + A`"],
             "c": 2,
             "why": "`A` is constant, so `u′ = y′ = −k·(y − A) = −k·u`. The other three "
                    "put `A` back into an equation that has already absorbed it."},
            {"q": "In the coffee preset the factor is `3/4`. What does each Euler step multiply by `3/4`?",
             "a": ["The temperature `y`", "The gap `y − 20`", "The rate constant `k`", "The room temperature"],
             "c": 1,
             "why": "The exact formula is `yₙ = 20 + 80·(3/4)ⁿ`: it is the gap that is "
                    "multiplied. Multiplying the temperature itself would send it towards 0, "
                    "below the room's 20, where the equation says it can never go."},
        ],
        "mistakes": [
            ("Believing a hot object cools at a constant rate",
             "The mistaken model is that the coffee loses the same number of degrees every "
             "minute. The equation says the loss is proportional to the gap, and the gap "
             "shrinks: the rates in the table are `−20, −15, −45/4, −135/16`, each three "
             "quarters of the one before. A constant rate of 20 per minute would have the "
             "coffee at 20 degrees after four minutes and below it after that, which Newton's "
             "law forbids."),
            ("Applying the decay factor to the temperature instead of the gap",
             "Writing `yₙ = 100·(3/4)ⁿ` treats the temperature as the decaying quantity. It "
             "heads for 0, not for 20: at `n = 4` it gives `2025/64`, about `31.6`, which is "
             "under the lab's `725/16`, and it keeps falling past the room temperature. Only "
             "the gap `y − 20` decays; the temperature is that decaying gap added to the "
             "steady level."),
            ("Treating warming as a separate law",
             "A cold cup in a warm room needs no new equation. The gap `y − A` is negative, "
             "the rate `−k·(y − A)` is positive, and the same formula "
             "`A + (y₀ − A)·e^(−kt)` gives a rising curve. The lab's second preset is "
             "the same code with a start below `A`."),
        ],
        "standard": ("Finish when you can write Newton's law, reduce it to decay by a substitution, and quote its Euler and closed-form values with their tiers.",
                     "You should be able to read the surroundings and the rate off the "
                     "equation, substitute `u = y − A`, write `yₙ` as `A` plus a power of "
                     "the factor, name the steady state, and explain why the rate is not "
                     "constant."),
        "note": "The cup of coffee exchanges heat with the room; a tank exchanges salt with a stream. &ldquo;Mixing Problems&rdquo; sets up the same shifted equation from a balance of what comes in and what goes out.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "mixing-problems",
        "title": "Mixing Problems",
        "module": "Shifted and bounded growth",
        "one_line": "For a well-stirred tank the amount of salt changes at the rate in minus the rate out, which is the shifted decay equation whose steady state is the inflow concentration times the volume, approached and never reached.",
        "summary": (
            "A tank holds a well-stirred solution, with a stream flowing in at one "
            "concentration and the same volume flowing out. The amount of salt `y` then "
            "obeys `y′ = (rate in) − (rate out)·y/V`, which is `y′ = −k·(y − A)` with the "
            "steady amount `A` equal to the inflow concentration times the volume. The lab "
            "gives the exact Euler column and the rounded closed form, and shows that the "
            "tank approaches `A` in the manner of a cooling cup and does not get there."
        ),
        "key": [
            "y′ = (rate in) − (rate out)·y/V",
            "= −k·(y − A),  k = flow/V",
            "steady amount A = (inflow concentration)·V",
            "y = A + (y₀ − A)·e^(−kt)",
            "y′ = 10 − y/20:  A = 200, factor 19/20",
        ],
        "key_label": "A balance of what enters and what leaves",
        "concepts_intro": (
            "Three ideas: the balance that gives the equation, the steady amount it points at, "
            "and why the tank never gets there."
        ),
        "concepts": [
            ("Rate in minus rate out",
             "The salt in a tank changes by what the inflow brings minus what the outflow "
             "carries away. The inflow brings `(flow)·(concentration)` grams per minute. The "
             "outflow carries the same flow times the tank's current concentration `y/V`, so "
             "what leaves depends on how much is already there."),
            ("The steady amount is where the two rates are equal",
             "Setting rate in equal to rate out gives the amount at which `y′ = 0`. For "
             "equal flows that is the inflow concentration times the volume, `A = c·V`. "
             "Writing the equation as `y′ = −(flow/V)·(y − A)` puts it in the form of the "
             "last lesson."),
            ("Approached, never reached",
             "The gap `y − A` is multiplied by `1 − kh` at every Euler step and shrinks like "
             "`e^(−kt)` in the solution. Neither is ever zero, so the tank's concentration "
             "gets as close to the inflow concentration as you like and stays under it."),
        ],
        "read_title": "A tank with salt water running through it",
        "read_intro": "The balance written once in general and once for a tank of one hundred litres, the steady amount, and the exact steps beside the closed form.",
        "body": [
            ("p", "A tank holds 100 litres of water. Salt water at 2 grams per litre runs in at "
                  "5 litres per minute, and well-stirred solution runs out at the same 5 "
                  "litres per minute, so the volume stays at 100. Let `y` be the grams of salt "
                  "in the tank. The question the equation answers is how `y` changes."),
            ("def", ("A well-stirred tank",
                     "A tank of constant volume `V` with a stream of concentration `c` flowing "
                     "in at the flow rate `r`, and the same flow `r` leaving. The "
                     "<strong>well-stirred</strong> assumption is that the concentration "
                     "inside is `y/V` everywhere at once.",
                     "The balance is `y′ = r·c − r·y/V`: grams in per minute, minus grams out "
                     "per minute.")),
            ("math", [
                "in:    r·c     = 5 × 2        = 10 grams per minute",
                "out:   r·y/V   = 5 × y/100    = y/20 grams per minute",
                "",
                "  y′ = 10 − y/20",
                "     = −(1/20)·(y − 200)",
            ]),
            ("p", "The second line is the first rewritten by taking out `−1/20`: "
                  "`10 − y/20 = −(1/20)·(y − 200)`. It is Newton's law with "
                  "`k = 1/20` and a steady amount `A = 200` grams, and it is the equation of "
                  "&ldquo;Newton's Law of Cooling&rdquo; with the salt's gap `y − 200` in the place "
                  "of the coffee's gap `y − 20`. The steady amount is where the rates balance: "
                  "`10 = y/20` at `y = 200`, which is `c·V = 2·100`."),
            ("h3", "Solving it, and stepping it"),
            ("p", "With the tank starting as pure water, `y(0) = 0`, the solution is "
                  "`y = 200 + (0 − 200)·e^(−t/20) = 200·(1 − e^(−t/20))`. The lab steps it "
                  "with `h = 1` minute. The factor is `1 − 1/20 = 19/20`, and the first two "
                  "steps are `y₁ = 200·(1 − 19/20) = 10` and "
                  "`y₂ = 200·(1 − 361/400) = 39/2`. After ten steps the exact value is a "
                  "fraction with a long denominator, which the lab prints in full "
                  "beside `≈ 78.6939`, the rounded closed form at `t = 10`."),
            ("math", [
                "  n      yₙ = 200·(1 − (19/20)ⁿ)",
                "",
                "  0      0",
                "  1      10",
                "  2      39/2",
                "  3      1141/40",
                "",
                "  closed form at t = 10:  200·(1 − e^(−1/2)) ≈ 78.6939",
            ]),
            ("h3", "Never reaching the inflow concentration"),
            ("p", "The tank's concentration is `y/V`, which starts at 0 and has the inflow's "
                  "concentration 2 as its limit. Does it get there? The gap "
                  "`200·e^(−t/20)` is positive at every time, so `y` is under 200 at every time, "
                  "and the exact sequence has the same property, because `(19/20)ⁿ` is "
                  "positive for every `n`. The gap halves every `ln 2/(1/20) ≈ 13.8629` "
                  "minutes, which is quick, and still never zero."),
            ("example", ("A tank being flushed",
                         "Fill the tank with 50 grams of salt and run pure water through it at "
                         "10 litres per minute into 100 litres: `y′ = −y/10`, steady amount 0. "
                         "The factor with `h = 1` is `9/10`, so the exact amounts are "
                         "`50, 45, 81/2, 729/20, …`. They fall towards 0 and no step is 0. "
                         "The third preset is a tank that already holds 100 grams and is fed "
                         "by a stream whose steady amount is 300: `y′ = 6 − y/50`, which is "
                         "5 litres per minute at 1.2 grams per litre into 250 litres. It "
                         "rises towards 300 and stays under it.")),
            ("p", "What the equation assumes is part of the problem. The volume does not "
                  "change; the tank is perfectly mixed; the inflow concentration is "
                  "constant. If the outflow differed from the inflow the volume would "
                  "change, and `V` would become a function of time in the equation. That is "
                  "a different problem and not one this course solves."),
        ],
        "lab": ("dekit", {
            "mode": "growth",
            "preset": "tank",
            "presets": [
                {"id": "tank", "label": "y′ = 10 − y/20, y(0) = 0, h = 1",
                 "k": "-1/20", "y0": 0, "A": 200, "h": 1, "n": 10, "target": None,
                 "expect": {"grFactor": "19/20", "grLast": "4108933742199/51200000000", "grTrue": "≈ 78.6939", "grSteady": "200", "grT": "≈ 13.8629"}},
                {"id": "flush", "label": "y′ = −y/10, y(0) = 50, h = 1",
                 "k": "-1/10", "y0": 50, "A": 0, "h": 1, "n": 10, "target": None,
                 "expect": {"grFactor": "9/10", "grLast": "3486784401/200000000", "grTrue": "≈ 18.394", "grSteady": "0"}},
                {"id": "salt", "label": "y′ = 6 − y/50, y(0) = 100, h = 1",
                 "k": "-1/50", "y0": 100, "A": 300, "h": 1, "n": 10, "target": None,
                 "expect": {"grFactor": "49/50", "grLast": "66692108702387999/488281250000000", "grTrue": "≈ 136.254", "grSteady": "300"}},
            ],
            "panel_title": "Rate in minus rate out, as a shifted decay",
            "panel_intro": (
                "The rate box holds minus the flow over the volume, and the shift box holds "
                "the steady amount. The steady-state tile prints it. The last-value tile is "
                "the exact amount after the steps, a fraction that may be long, and the "
                "closed-form tile is the rounded one. Change the start on any preset and the "
                "steady-state tile does not move."
            ),
        }),
        "steps_title": "Setting up and solving a mixing problem",
        "steps_intro": "Five moves. The balance in the first two is where a mixing problem is won or lost.",
        "steps": [
            ("Write the rate in",
             "Flow times inflow concentration, in grams per minute. Check the units before "
             "anything else."),
            ("Write the rate out",
             "Flow times the tank's current concentration, `r·y/V`. It contains `y`, which is "
             "what makes the equation differential."),
            ("Rewrite as a shifted decay",
             "Factor out the coefficient of `y`: `y′ = −(r/V)·(y − A)` with `A = c·V`. "
             "Read `k` and `A` off it."),
            ("Solve and step",
             "`y = A + (y₀ − A)·e^(−kt)` rounded, and `yₙ = A + (y₀ − A)·(1 − kh)ⁿ` exact. "
             "Check the closed form by differentiating."),
            ("Say what was assumed",
             "Constant volume, perfect stirring, a constant inflow. The steady amount "
             "is approached and not reached."),
        ],
        "worked": {
            "title": "A hundred litres, 2 grams per litre in",
            "intro": [
                "Flow 5 litres per minute both ways, inflow 2 grams per litre, volume 100 "
                "litres, an empty start. Exact until the closed-form line."
            ],
            "lines": [
                "in:   5 × 2 = 10 grams per minute",
                "out:  5 × y/100 = y/20 grams per minute",
                "y′ = 10 − y/20 = −(1/20)·(y − 200)",
                "steady amount  A = 2 × 100 = 200 grams",
                "",
                "Euler, h = 1:   factor 1 − 1/20 = 19/20",
                "y₁ = 200·(1 − 19/20)     = 10",
                "y₂ = 200·(1 − 361/400)   = 39/2",
                "",
                "closed form  200·(1 − e^(−t/20))",
                "at t = 10:   ≈ 78.6939   (rounded)",
            ],
            "after": [
                "The gap to 200 is 200 grams at the start, and it is multiplied by `19/20` at "
                "every step. It halves, in the solution, every `≈ 13.8629` minutes, the "
                "half-life tile of this lab.",
                "The concentration in the tank is `y/100`, and the inflow's concentration of 2 is "
                "its limit. The tank is below that limit at every time, in the exact "
                "sequence and in the closed form.",
            ],
        },
        "quiz_title": "Balance, steady amount and limit",
        "quiz": [
            {"q": "A 200-litre tank has a stream of 4 litres per minute at 3 grams per litre flowing in, and 4 litres per minute flowing out. What is the steady amount of salt?",
             "a": ["12 grams", "600 grams", "150 grams", "67 grams"],
             "c": 1,
             "why": "The steady amount is the inflow concentration times the volume, "
                    "`3·200 = 600` grams. The value 12 is the rate in, in grams per minute, "
                    "which is a different unit; 150 divides 600 by 4; and 67 divides the "
                    "volume by the concentration."},
            {"q": "Which equation describes that tank?",
             "a": ["`y′ = 12 − 4y`", "`y′ = 3 − y/50`", "`y′ = 12 + y/50`", "`y′ = 12 − y/50`"],
             "c": 3,
             "why": "In is `4·3 = 12` grams per minute and out is `4·y/200 = y/50`. The "
                    "first drops the volume from the outflow; the second uses the "
                    "concentration where a rate in grams is needed; the third adds the "
                    "outflow instead of subtracting it."},
            {"q": "In the first preset the tank starts as pure water. Does the amount of salt ever equal 200 grams?",
             "a": ["No: the gap `200·e^(−t/20)` is positive at every time", "Yes, at `t = 20`",
                   "Yes, at `t = 10·ln 2`", "Yes, after a long enough time"],
             "c": 0,
             "why": "The solution is `200·(1 − e^(−t/20))`, which is below 200 for every "
                    "`t` because the exponential is never 0. A long time brings it as close "
                    "to 200 as you like, which is different from equal to it; at `t = 20` it "
                    "has only gone `1 − e^(−1)` of the way."},
            {"q": "In the flush preset the factor is `9/10` and the start is 50. What is `y₂` exactly?",
             "a": ["45", "40", "`81/2`", "`81/10`"],
             "c": 2,
             "why": "`y₂ = 50·(9/10)² = 50·81/100 = 81/2`. The value 45 is `y₁`; 40 "
                    "subtracts 10 twice, as if the loss were constant; and `81/10` forgets "
                    "that the start is 50 and not 10."},
        ],
        "mistakes": [
            ("Believing the tank reaches the inflow concentration in finite time",
             "The mistaken model is that the tank fills up to the inflow's concentration "
             "and then stays there, like a glass that is full. The gap `y − 200` is "
             "multiplied by `19/20` at every step and by `e^(−t/20)` in the solution, and "
             "neither is ever zero, because a power of a positive fraction is positive. The "
             "lab's last-value tile after ten steps is a fraction less than 200, and the table "
             "is under 200 at every row."),
            ("Leaving the tank's own concentration out of the outflow",
             "Writing the rate out as a constant 5 grams per minute, the flow with the "
             "wrong unit, and not as the flow times the concentration `y/100`, makes "
             "`y′ = 10 − 5 = 5` constant. Then `y = 5t`, which passes 200 "
             "at `t = 40` and keeps going. But the outflow carries salt in proportion to how "
             "salty the tank is: it takes nothing from a tank that holds no salt and 10 "
             "grams per minute, equal to the inflow, from one that holds 200."),
            ("Reading the steady amount as a rate",
             "The steady amount is 200 grams, not 10. The 10 is the rate in, in grams per "
             "minute, and it is the same quantity as the rate out when `y = 200`. The "
             "difference in units is the check: an amount in grams is `c·V`, a rate in grams "
             "per minute is `r·c`."),
        ],
        "standard": ("Finish when you can set up the balance for a well-stirred tank, find its steady amount, and report the exact and rounded values with their tiers.",
                     "You should be able to write rate in minus rate out, rewrite it "
                     "as `−k·(y − A)`, read `A` as the inflow concentration times the "
                     "volume, step it exactly, state the closed form, and say that the "
                     "steady amount is approached and not reached."),
        "note": "Every equation so far has had one steady level that attracts: the quantity moves toward it from either side. &ldquo;Logistic Growth&rdquo; builds an equation with two steady levels, one that repels and one that attracts, from the observation that no population can grow exponentially for ever.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "logistic-growth",
        "title": "Logistic Growth",
        "module": "Shifted and bounded growth",
        "one_line": "Logistic growth multiplies the growth rate by a factor that falls to zero at the carrying capacity K, so the equation has equilibria at 0 and K and grows fastest at K/2.",
        "summary": (
            "A population cannot grow exponentially for ever. The logistic equation "
            "`y′ = r·y·(1 − y/K)` multiplies the exponential rate `r·y` by a factor that is "
            "near 1 for a small population and falls to 0 at the carrying capacity `K`. Its "
            "equilibria are `0` and `K`, the first repelling and the second attracting; the "
            "growth rate is largest at `K/2`; and Euler's exact steps show a column of "
            "fractions whose digits double at every step, so the lab prints them until a stated "
            "budget and then says so."
        ),
        "key": [
            "y′ = r·y·(1 − y/K)",
            "equilibria  y = 0  and  y = K",
            "r = 1, K = 4:  f(y) = y·(1 − y/4)",
            "f′(y) = 1 − y/2 = 0 at y = 2 = K/2",
            "steps from 1:  11/8,  935/512, …",
        ],
        "key_label": "Growth that levels off",
        "concepts_intro": (
            "Three ideas: the factor that bounds the growth, the two equilibria and which way "
            "the rest of the line moves, and where the growth is fastest."
        ),
        "concepts": [
            ("Exponential growth times a bounding factor",
             "The logistic equation is `y′ = r·y·(1 − y/K)`. For `y` small compared with `K` "
             "the factor `1 − y/K` is near 1 and the equation is nearly `y′ = r·y`. As `y` "
             "approaches `K` the factor falls to 0 and so does the rate."),
            ("Two equilibria, and the direction between them",
             "The right side is zero at `y = 0` and at `y = K`. Between them it is positive, "
             "so a population there grows; above `K` it is negative, so a population "
             "there shrinks. Starts anywhere above 0 move towards `K`, and a start "
             "just above 0 moves away from 0: the first equilibrium repels and the "
             "second attracts."),
            ("The growth is fastest at half the capacity",
             "The rate `f(y) = r·y·(1 − y/K)` has `f′(y) = r·(1 − 2y/K)`, which is zero at "
             "`y = K/2`. There `f` is largest, `r·K/4`, and the curve `y(t)` is steepest. "
             "Before that the curve bends upwards and afterwards downwards."),
        ],
        "read_title": "A population that levels off",
        "read_intro": "The equation, its equilibria read from the sign of the right side, the point of fastest growth from the rate of that rate, and exact Euler steps with the lab's stated limit.",
        "body": [
            ("p", "Exponential growth is the right description of a small population with "
                  "room and food, and it is wrong for a large one, because it has no "
                  "limit on how big the population can become. Something has to slow the "
                  "growth as the population fills its surroundings. The simplest "
                  "correction multiplies the exponential rate by a factor that drops to "
                  "zero at a ceiling."),
            ("def", ("The logistic equation",
                     "With a growth rate `r > 0` and a <strong>carrying capacity</strong> "
                     "`K > 0`, the logistic equation is `y′ = r·y·(1 − y/K)`.",
                     "The carrying capacity is the level at which the growth rate is zero. It "
                     "is a number the model is given, not one it derives.")),
            ("p", "Take `r = 1` and `K = 4`, so that `f(y) = y·(1 − y/4)`. Expanded, "
                  "that is `y − y²/4`: the exponential term `y` and a correction "
                  "that grows with the square of `y`. Here is the rate at several populations."),
            ("math", [
                "  y       f(y) = y·(1 − y/4)",
                "",
                "  0       0",
                "  1       3/4",
                "  2       1",
                "  3       3/4",
                "  4       0",
                "  5       −5/4",
            ]),
            ("p", "The rate rises from 0, peaks at `y = 2` with `f = 1`, and falls to 0 at 4. "
                  "Above 4 it is negative, so a population above the capacity shrinks "
                  "back to it. An exponential at `y = 3` would be growing at 3, and the "
                  "logistic is growing at `3/4`: the same equation with a quarter of the rate."),
            ("h3", "Which way the line moves"),
            ("p", "An equilibrium is a value where `f(y) = 0`, so that a population placed "
                  "there does not change. Here those are `0` and `4`. Between 0 and 4 the "
                  "rate is positive and above 4 negative, so every start above 0 heads for "
                  "4. The lab labels this `0 unstable; 4 stable`, in words the next "
                  "course defines carefully: nearby starts move away from 0 and towards 4."),
            ("h3", "Where the growth is fastest"),
            ("p", "The rate `f(y)` is largest where its own rate of change is zero. "
                  "Here `f′(y) = 1 − y/2`, which is zero at `y = 2`, half of the capacity. "
                  "For the curve `y(t)` this is the steepest point, and the chain rule "
                  "shows it is also where the curve changes from bending up to bending "
                  "down, because `y″ = f′(y)·y′`. The lab's inflection tile prints "
                  "`y = 2`."),
            ("h3", "Exact steps, and the lab's limit"),
            ("p", "Start at `y(0) = 1` with `h = 1/2`. The first step is "
                  "`1 + (1/2)·(3/4) = 11/8`, a little under the `3/2` that exponential growth "
                  "would give. The second is `935/512`, which is about `1.82617`. The right "
                  "side is quadratic, so the numerator and denominator roughly double their "
                  "number of digits at every step. The lab prints exact steps until a "
                  "number has more than 2000 digits and then stops, and says "
                  "that it has: from this start it prints `11 exact steps, then digit "
                  "budget`. It does not round to carry on."),
            ("math", [
                "y′ = y·(1 − y/4),  y(0) = 1,  h = 1/2",
                "",
                "  y₁ = 1 + (1/2)·(3/4)             = 11/8",
                "  y₂ = 11/8 + (1/2)·(231/256)      = 935/512",
                "",
                "  digits roughly double at each step",
            ]),
            ("p", "The population cannot be followed further as exact fractions, "
                  "and nothing in the equation stopped. The stopping is the lab's, "
                  "and it is the honest alternative to hiding the growth in the digits by "
                  "rounding at every step."),
            ("example", ("Above the capacity",
                         "Start at 6. Then `f(6) = 6·(1 − 3/2) = −3`, so the first step is "
                         "`6 + (1/2)·(−3) = 9/2`: the population falls towards 4, "
                         "and the lab prints a limit of `→ 4`. The third preset is the same "
                         "kind of equation with `K = 10`, whose steepest point is at 5.")),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "steps",
            "preset": "four",
            "presets": [
                _p("four", "y′ = y·(1 − y/4), start 1, h = 1/2", "y(1 - y/4)", [1], "1/2", 12,
                   [6, 0, 5], {"auEquil": "0, 4", "auTypes": "0 unstable; 4 stable", "auInflect": "y = 2",
                    "auSteps": "11 exact steps, then digit budget"}),
                _p("above", "y′ = y·(1 − y/4), start 6, h = 1/2", "y(1 - y/4)", [6], "1/2", 12,
                   [6, 0, 7], {"auEquil": "0, 4", "auLimit": "→ 4"}),
                _p("small", "y′ = y·(1 − y/10), start 1/2, h = 1/2", "y(1 - y/10)", ["1/2"], "1/2", 12,
                   [6, 0, 11], {"auEquil": "0, 10", "auTypes": "0 unstable; 10 stable", "auInflect": "y = 5"}),
            ],
            "panel_title": "The equilibria of a logistic equation and its first steps",
            "panel_intro": (
                "The first tile lists where the right side is zero, the second says what kind "
                "of equilibrium each is, and the inflection tile is where the right side is "
                "largest. The picture shows the exact Euler polygon from each start, with "
                "the equilibria as horizontal lines. The steps tile says when the exact "
                "column stopped on the digit budget."
            ),
        }),
        "steps_title": "Reading a logistic equation",
        "steps_intro": "Five moves, done before any step is computed.",
        "steps": [
            ("Identify r and K",
             "Write the right side as `r·y·(1 − y/K)`. The factor that vanishes gives `K`; "
             "the coefficient of `y` near 0 gives `r`."),
            ("Find the equilibria",
             "Solve `f(y) = 0`: `y = 0` and `y = K`."),
            ("Read the direction between them",
             "Evaluate `f` at one point in each region. Positive means `y` rises, negative "
             "that it falls. Mark which equilibria are approached."),
            ("Locate the steepest point",
             "Solve `f′(y) = 0`: `y = K/2`, where `f = r·K/4`."),
            ("Step it and note the limit",
             "Compute a few exact steps from the starting value and compare each "
             "with what exponential growth would have given. Report where the lab stopped."),
        ],
        "worked": {
            "title": "The logistic equation with K = 4, from y(0) = 1",
            "intro": [
                "The equilibria and the steepest point come from the right side alone. The two "
                "Euler steps are exact fractions, with `h = 1/2`."
            ],
            "lines": [
                "f(y) = y·(1 − y/4) = y − y²/4",
                "f(y) = 0  at  y = 0  and  y = 4",
                "f′(y) = 1 − y/2 = 0  at  y = 2 = K/2",
                "",
                "f(1)    = 1·(3/4)          = 3/4",
                "y₁      = 1 + (1/2)·(3/4)  = 11/8",
                "f(11/8) = (11/8)·(21/32)   = 231/256",
                "y₂      = 11/8 + (1/2)·(231/256) = 935/512",
            ],
            "after": [
                "The rate at the start is `3/4`, and the exponential would have used 1. The "
                "difference is the factor `1 − y/4`, which has already cost a quarter of "
                "the growth at `y = 1`. The steps rise towards 4 and the lab's picture "
                "shows them flattening as they near it.",
                "The value `935/512 ≈ 1.82617` is rounded only to say how big it is; the "
                "lab prints the fraction. The next steps double the digits again until the "
                "budget, and the equilibria and the steepest point do not depend on any "
                "of them.",
            ],
        },
        "quiz_title": "Equilibria, direction and the steepest point",
        "quiz": [
            {"q": "What are the equilibria of `y′ = y·(1 − y/10)`?",
             "a": ["`1` and `10`", "`0` only", "`0` and `10`", "`0` and `5`"],
             "c": 2,
             "why": "The right side is zero when `y = 0` or `1 − y/10 = 0`, that is "
                    "`y = 10`. The value 5 is where the rate is largest, not zero, and 1 is "
                    "the coefficient inside the bracket and not a root."},
            {"q": "In the first preset a population starts at 6, above the capacity of 4. What does the equation do to it?",
             "a": ["It falls towards 4 and does not go below it", "It keeps growing, as 6 is already past the limit",
                   "It stays at 6", "It falls to 0"],
             "c": 0,
             "why": "`f(6) = 6·(1 − 3/2) = −3` is negative, so the population falls, and as "
                    "it nears 4 the rate shrinks to 0. It cannot cross 4, which is an "
                    "equilibrium, and it is not at an equilibrium at 6."},
            {"q": "For `y′ = y·(1 − y/10)` at which population is the growth rate largest?",
             "a": ["`y = 10`", "`y = 5`", "`y = 0`", "`y = 1`"],
             "c": 1,
             "why": "`f′(y) = 1 − y/5` is zero at `y = 5`, half the capacity. At `y = 10` "
                    "and `y = 0` the rate is zero, the flattest the curve gets, and at 1 the "
                    "factor `1 − y/10` has hardly started to act."},
            {"q": "What does the logistic equation look like when `y` is very small compared with `K`?",
             "a": ["Constant growth, `y′ = r·K`", "No growth, `y′ = 0`", "Decay, `y′ = −r·y`",
                   "Almost exponential growth, `y′ ≈ r·y`"],
             "c": 3,
             "why": "When `y/K` is near 0 the factor `1 − y/K` is near 1, and the equation is "
                    "nearly `y′ = r·y`. The bounding only acts when the population is a "
                    "good fraction of the capacity."},
        ],
        "mistakes": [
            ("Thinking the logistic curve is exponential growth that stops at K",
             "The mistaken model is an exponential that runs until it hits `K` and is then "
             "switched off. The equation has no switch. The factor `1 − y/K` acts at every "
             "population, trimming the rate smoothly: at `y = 1` the rate is `3/4` and not 1, "
             "at `y = 3` it is `3/4` and not 3. And a switch could not bring a population "
             "above `K` back down, which the equation does, with `f(5) = −5/4`."),
            ("Putting the steepest point at K",
             "At `y = K` the rate is zero, which is the flattest the curve gets, not the "
             "steepest. The rate is largest where `f′(y) = 0`, which for this family is "
             "`y = K/2`: `y = 2` for `K = 4`, as the inflection tile prints, with "
             "`f(2) = 1` against `f(3) = 3/4`."),
            ("Reading the lab's stop as the population's",
             "The exact column stops after eleven steps with a message about the digit "
             "budget. That is the lab refusing to keep writing numbers with thousands of "
             "digits, not the solution leaving off. The equilibria, their kinds and the "
             "steepest point come from the right side and are exact whether or not any "
             "step is printed."),
        ],
        "standard": ("Finish when you can find the equilibria of a logistic equation, say which way the rest of the line moves, and locate its steepest growth.",
                     "You should be able to write `y′ = r·y·(1 − y/K)`, solve "
                     "`f(y) = 0`, read the direction from the sign of `f` in each "
                     "region, solve `f′(y) = 0` for the steepest point, compute an exact "
                     "Euler step, and say what the lab does when the digits run out."),
        "note": "A logistic population has a ceiling, and a harvest takes some of it away at a steady rate. &ldquo;Harvesting and the Threshold&rdquo; subtracts a constant from the equation and finds the rate beyond which the population cannot survive.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "harvesting-and-the-threshold",
        "title": "Harvesting and the Threshold",
        "module": "Shifted and bounded growth",
        "one_line": "Subtracting a constant harvest H from the logistic equation moves its equilibria together until, at H = r·K/4, they meet and vanish, and above that rate every start collapses.",
        "summary": (
            "A population harvested at a constant rate `H` obeys `y′ = r·y·(1 − y/K) − H`. "
            "The equilibria are the roots of a quadratic. Below the threshold `H* = r·K/4` "
            "there are two, a lower one that repels and an upper one that attracts; at the "
            "threshold they merge into one; above it there are none and every start falls. "
            "A population that looks sustainable at a given harvest can therefore collapse "
            "from a small dip."
        ),
        "key": [
            "y′ = r·y·(1 − y/K) − H",
            "r = 1, K = 4:  y² − 4y + 4H = 0",
            "H below 1: two;  H = 1: one;  H above 1: none",
            "H* = r·K/4,  the peak of the growth rate",
            "below the lower equilibrium: collapse",
        ],
        "key_label": "How much a population can give up",
        "concepts_intro": (
            "Three ideas: what a constant harvest does to the rate, how the quadratic counts "
            "the equilibria, and where the threshold comes from."
        ),
        "concepts": [
            ("A harvest lowers the whole rate by H",
             "Taking `H` per unit time makes the rate of change `f(y) − H`, where "
             "`f(y) = r·y·(1 − y/K)` is the natural growth. The population grows where the "
             "natural growth exceeds the harvest and shrinks where it does not."),
            ("The equilibria solve a quadratic",
             "Setting `f(y) − H = 0` gives, for `r = 1` and `K = 4`, "
             "`y² − 4y + 4H = 0`. Its discriminant is `16 − 16·H`, so two roots exist for "
             "`H < 1`, one for `H = 1`, none for `H > 1`."),
            ("The threshold is the most the growth ever gives",
             "The natural growth `f` is largest at `y = K/2`, where it is `r·K/4`. A harvest "
             "above that is more than the population can replace at any size, and a harvest "
             "at exactly that leaves a single, fragile equilibrium."),
        ],
        "read_title": "Two equilibria, one, and none",
        "read_intro": "The harvested equation, the quadratic that counts its equilibria, three harvests of increasing size, and the threshold read off the peak of the growth.",
        "body": [
            ("p", "Take the logistic population of the previous lesson, with `r = 1` and "
                  "`K = 4`, and remove a fixed amount `H` of it in every unit of time. Fishing "
                  "and logging are the usual pictures. Left alone the population grows "
                  "to 4. The question is how large `H` can be before it no longer does."),
            ("def", ("The harvested logistic equation",
                     "With a constant harvest rate `H ≥ 0`, the equation is "
                     "`y′ = r·y·(1 − y/K) − H`.",
                     "The harvest is taken at the same rate whatever the population is. This "
                     "is an assumption about the fishery, and the lab computes what follows "
                     "from it.")),
            ("math", [
                "r = 1, K = 4:",
                "",
                "  y′ = y·(1 − y/4) − H",
                "     = −y²/4 + y − H",
                "",
                "  equilibria:   y² − 4y + 4H = 0",
                "  discriminant: 16 − 16·H = 16·(1 − H)",
            ]),
            ("p", "The discriminant decides the count. For `H < 1` it is positive and there "
                  "are two real roots, for `H = 1` it is zero and there is one, and for "
                  "`H > 1` it is negative and there are none. The three presets are one of "
                  "each."),
            ("math", [
                "  H = 3/4:   y² − 4y + 3 = (y − 1)(y − 3)    y = 1, 3",
                "  H = 1:     y² − 4y + 4 = (y − 2)²          y = 2",
                "  H = 5/4:   y² − 4y + 5,  16 − 20 < 0       none",
            ]),
            ("h3", "A harvest of three quarters"),
            ("p", "The right side is `−(y − 1)·(y − 3)/4`, which is negative below 1, positive "
                  "between 1 and 3, and negative above 3. So a population between 1 and 3 "
                  "grows to 3, a population above 3 falls to 3, and a population below 1 "
                  "falls further. The lab prints `1 unstable; 3 stable`. The harvest has "
                  "not removed the attracting equilibrium; it has moved it from 4 down to 3, "
                  "and it has created a repelling one at 1. The slope tile agrees: "
                  "`f′(1) = 1/2` is positive, so nearby populations move away from 1, and "
                  "`f′(3) = −1/2` is negative, so they move towards 3."),
            ("p", "The repelling equilibrium is the dangerous one. At `y = 1` the natural growth "
                  "is exactly `3/4`, the harvest, so nothing changes. At `y = 9/10` the natural "
                  "growth is `279/400`, which is less than `300/400`, so the population shrinks, "
                  "and the less there is the less growth to pay for the harvest. A harvest "
                  "that the population can replace today may not be one it can replace after "
                  "a bad year."),
            ("h3", "At the threshold, and beyond"),
            ("p", "At `H = 1` the right side is `−(y − 2)²/4`, which is never positive. A "
                  "population above 2 falls back to 2 and settles. A population below 2 "
                  "falls away, and so does one that dips just under it. The equilibrium is "
                  "attracting from one side only, and the lab calls it semistable. At "
                  "`H = 5/4` the right side is negative for every `y` and every start "
                  "falls."),
            ("p", "The threshold has a general form. The natural growth `r·y·(1 − y/K)` has "
                  "its peak at `y = K/2`, where it equals `r·K/4`. For a harvest above that "
                  "peak the right side is negative at every `y`; for one below it the line "
                  "`H` crosses the growth curve twice. So `H* = r·K/4`, which is "
                  "`1·4/4 = 1` here."),
            ("example", ("A population that falls below zero",
                         "In the third preset the limit tile reads `→ −∞`: every start falls "
                         "without bound, and passes zero on the way, since the equation does "
                         "not know a population cannot be negative. Read a negative value "
                         "as the population having already gone: the model says the stock "
                         "is exhausted, and stops describing anything.")),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "line",
            "preset": "light",
            "presets": [
                _p("light", "H = 3/4: y′ = y·(1 − y/4) − 3/4", "y(1 - y/4) - 3/4", [2], "1/4", 8,
                   [6, 0, 5], {"auEquil": "1, 3", "auTypes": "1 unstable; 3 stable",
                    "auSlope": "f′(1) = 1/2; f′(3) = −1/2"}),
                _p("critical", "H = 1: y′ = y·(1 − y/4) − 1", "y(1 - y/4) - 1", [3], "1/4", 8,
                   [6, 0, 5], {"auEquil": "2", "auTypes": "2 semistable", "auLimit": "→ 2"}),
                _p("heavy", "H = 5/4: y′ = y·(1 − y/4) − 5/4", "y(1 - y/4) - 5/4", [2], "1/4", 8,
                   [6, -2, 5], {"auEquil": "none", "auLimit": "→ −∞"}),
            ],
            "panel_title": "How many equilibria a harvest leaves",
            "panel_intro": (
                "The phase line shows each equilibrium as a dot and each gap between them as "
                "an arrow. The first tile lists the equilibria, the second says which "
                "attract and which repel, and the limit tile says where the first start "
                "ends up. Edit the box to try another harvest: the threshold is where the "
                "number of equilibria changes."
            ),
        }),
        "steps_title": "Finding what a harvest does",
        "steps_intro": "Five moves, and the threshold is the fourth.",
        "steps": [
            ("Write the natural growth and the harvest",
             "`f(y) = r·y·(1 − y/K)` and the constant `H`. The equation is `y′ = f(y) − H`."),
            ("Find the equilibria",
             "Solve `f(y) = H`. For `r = 1`, `K = 4` that is `y² − 4y + 4H = 0`; use "
             "its discriminant first to count the roots."),
            ("Read the direction in each region",
             "Evaluate `f(y) − H` at a point in each region between roots. The lower one "
             "repels and the upper one attracts."),
            ("Find the threshold",
             "The peak of `f` is `r·K/4`, at `y = K/2`. A harvest at or above it leaves no "
             "attracting equilibrium."),
            ("Test with a dip",
             "Take a start a little below the lower equilibrium and compute `f(y) − H` "
             "there. If it is negative, a small loss becomes a collapse."),
        ],
        "worked": {
            "title": "r = 1, K = 4, three harvests",
            "intro": [
                "The equilibria come from the quadratic, and every figure is an exact fraction."
            ],
            "lines": [
                "y′ = y·(1 − y/4) − H",
                "equilibria:  y² − 4y + 4H = 0",
                "",
                "H = 3/4:  (y − 1)(y − 3)       y = 1, 3",
                "H = 1:    (y − 2)²             y = 2",
                "H = 5/4:  16 − 20 < 0          none",
                "",
                "threshold  H* = r·K/4 = 1·4/4 = 1",
                "f(9/10) − 3/4 = 279/400 − 300/400 = −21/400",
            ],
            "after": [
                "The last line is the check on the lower equilibrium: just below 1 the "
                "right side is negative, so the population keeps falling. As `H` rises "
                "from 3/4 to 1 the two equilibria, 1 and 3, move together and meet at 2; "
                "at any larger harvest nothing is left to hold the population.",
                "The upper equilibrium is 3 at the first harvest, 2 at the second, and "
                "absent at the third. It does not fade away smoothly: it goes from 2 to "
                "nothing the moment `H` passes `H* = 1`.",
            ],
        },
        "quiz_title": "Counting equilibria and finding the threshold",
        "quiz": [
            {"q": "For `r = 1`, `K = 4` and `H = 1/2`, how many equilibria does `y′ = y·(1 − y/4) − H` have?",
             "a": ["None", "One", "Two", "Three"],
             "c": 2,
             "why": "The discriminant `16 − 16·H = 8` is positive, so there are two real "
                    "roots, which are irrational but still two. One root needs `H = 1` and "
                    "none needs `H > 1`; a quadratic never has three."},
            {"q": "A population has `r = 2` and `K = 10`. What is the threshold harvest `H*`?",
             "a": ["`20`", "`2.5`", "`10`", "`5`"],
             "c": 3,
             "why": "`H* = r·K/4 = 2·10/4 = 5`. The value 20 is `r·K`, which is four times the "
                    "peak; 10 is the carrying capacity, which is a population and not a rate; "
                    "and 2.5 divides by 8."},
            {"q": "With `H = 3/4` (the first preset) a population starts at `1/2`. What does it do?",
             "a": ["It falls, because the harvest is more than the growth there", "It grows to 3",
                   "It stays at `1/2`", "It grows to 4"],
             "c": 0,
             "why": "`f(1/2) − 3/4 = 7/16 − 12/16 = −5/16`, which is negative, and `1/2` is below "
                    "the repelling equilibrium at 1. The equilibria are 1 and 3 and the "
                    "capacity of 4 is no longer one."},
            {"q": "At the threshold `H = 1` a population starts just above 2. What happens?",
             "a": ["It rises to 4", "It falls and settles at 2", "It stays where it started",
                   "It falls to 0"],
             "c": 1,
             "why": "The right side is `−(y − 2)²/4`, negative for `y ≠ 2`, so the population "
                    "falls, and the rate shrinks to 0 as it nears 2. A start just below 2 "
                    "would fall away from 2 for good, which is why the equilibrium is "
                    "called semistable."},
        ],
        "mistakes": [
            ("Believing that any harvest below the natural growth rate is sustainable",
             "The mistaken model is that if the population is growing faster than it is "
             "harvested, the harvest is safe. At `y = 1` with `H = 3/4` the growth "
             "exactly matches the harvest, and the equilibrium there repels: at `y = 9/10` "
             "the growth `279/400` is under the harvest `300/400`, and the population "
             "falls and keeps falling. A harvest below the peak of the growth is sustainable "
             "only for starts above the lower equilibrium."),
            ("Expecting the population to shrink gradually as the harvest grows",
             "The stable level does come down with `H`: 4 for no harvest, 3 for `H = 3/4`, "
             "2 for `H = 1`. But at `H = 1` it meets the repelling equilibrium, past that "
             "both are gone, and for `H = 5/4` there is nothing left to settle on. There "
             "is no small stable population at a slightly larger harvest, so a small increase "
             "in `H` past `H*` turns a stable stock into a collapse."),
            ("Treating the negative values as a population",
             "In the heavy preset the limit is `→ −∞`, so the solution passes below zero. A negative number of fish is "
             "not a quantity, and the equation, which knows nothing of the physical "
             "problem, carries on past it. The honest reading is that the stock is gone "
             "when `y` reaches 0, and everything after that point is outside the model."),
        ],
        "standard": ("Finish when you can find the equilibria of a harvested logistic equation, classify them, and compute the threshold harvest.",
                     "You should be able to write `y′ = f(y) − H`, reduce it to a "
                     "quadratic, count its roots from the discriminant, read which "
                     "repel and which attract, derive `H* = r·K/4` from the peak of "
                     "the growth, and test a start just below the lower equilibrium."),
        "note": "That finishes the course. Every model in it was one first-order equation with its equilibria read from its right side; the next course takes that reading as its subject and draws the phase line for any equation of the form `y′ = f(y)`.",
    },
]
