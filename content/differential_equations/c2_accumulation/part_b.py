"""Accumulation and the Integral -- the exact total and the second integral.

The antiderivative by reversing the power rule and the fundamental theorem as
the claim the refining sums supported; the constant of integration and the one
value that fixes it; the integral sign with linearity and additivity checked on
exact fractions; and the integral of 1/t, which no reversal of the power rule
reaches.

Every figure is read off the calckit modes (scripts/mathpath/labs/calckit.py)
with node scripts/labcheck.js --observe and cross-checked by hand with
Fractions. The antiderivative mode prints exact values; the riemann mode prints
the logarithm only as a rounded figure with its label, and the prose here does
the same.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-antiderivative-and-the-fundamental-theorem",
        "title": "The Antiderivative and the Fundamental Theorem",
        "module": "The exact total",
        "one_line": "An antiderivative of a rate gives the total change as its value at the right end minus its value at the left, with no pieces to add.",
        "summary": (
            "Reversing the power rule turns a polynomial rate into a function whose "
            "derivative is that rate. The total change over an interval of a quantity with that "
            "rate is then the value of that function at the right end minus its value at the left end, "
            "an exact fraction found without a single sum. The lesson states this as the "
            "claim the refining sums of the earlier lessons were supporting, shows why it "
            "is plausible, and says what the lab demonstrates and what it does not prove."
        ),
        "key": [
            "F is an antiderivative of f when F′ = f",
            "tⁿ becomes tⁿ⁺¹/(n + 1): always divide",
            "check: differentiate F and get f back",
            "total change = F(b) − F(a)",
            "the sums close in on it: stated, not proved",
        ],
        "key_label": "Reversing the power rule to total a rate",
        "concepts_intro": (
            "Three ideas: what an antiderivative is, the one test that catches a wrong "
            "one, and why its two end values give the total."
        ),
        "concepts": [
            ("An antiderivative undoes the derivative",
             "A function `F` is an antiderivative of the rate `f` when `F′ = f`. The power "
             "rule sends `tⁿ` to `n·tⁿ⁻¹`; reversing it sends `tⁿ` to `tⁿ⁺¹/(n + 1)`, "
             "one power higher and divided by the new power. For `f = t²` that is "
             "`F = t³/3`."),
            ("Differentiating the answer is the check",
             "Whatever `F` you write down, differentiate it. `(t³/3)′ = 3t²/3 = t²` passes. "
             "`(t³)′ = 3t²` does not, and it fails by exactly the factor the division "
             "was meant to remove. The check needs no lab and no sum."),
            ("The two end values of F give the total change",
             "If `F′ = f`, the total change from `a` to `b` of a quantity whose rate is "
             "`f` is `F(b) − F(a)`. For `t²` on the interval from `0` to `1` it is "
             "`1/3 − 0 = 1/3`, the number the left sums `7/32, 35/128, 155/512` were "
             "closing in on."),
        ],
        "read_title": "From a sum of pieces to two end values",
        "read_intro": "The reversal, the check, the claim, and the reason the claim is plausible.",
        "body": [
            ("p", "The earlier lessons added a rate piece by piece and compared every sum "
                  "with an exact total printed beside it. That total came from a different "
                  "method, and this lesson is the method. It runs the derivative backwards: "
                  "given the rate `f`, find a function `F` whose rate of change <em>is</em> "
                  "`f`. If you can, the total change the rate `f` produces over an interval "
                  "is read from the two ends of `F`."),
            ("def", ("Antiderivative",
                     "A function `F` is an <strong>antiderivative</strong> of `f` when "
                     "`F′ = f`. For a polynomial it is found term by term: a term `c·tⁿ` "
                     "becomes `c·tⁿ⁺¹/(n + 1)`, and a constant term `c` becomes `c·t`.",
                     "The power rule of “The Derivative as a Function” is the same "
                     "rule read from right to left.")),
            ("p", "Take the rate `t²`. Raise the power to get `t³`, divide by the new power "
                  "to get `t³/3`, and check: `(t³/3)′ = 3t²/3 = t²`. Then "
                  "`F(1) − F(0) = 1/3 − 0 = 1/3`. The sums of “Refining the Partition” "
                  "were `7/32, 35/128, 155/512`, each a little nearer a third, and none of "
                  "them equal to it."),
            ("math", [
                "t² on [0, 1]        Lₙ          Rₙ",
                "",
                "n = 4              7/32       15/32",
                "n = 8             35/128      51/128",
                "n = 16           155/512     187/512",
                "n = 32          651/2048    715/2048",
                "",
                "F(1) − F(0) = 1/3, between every pair",
            ]),
            ("h3", "Why the claim is plausible"),
            ("p", "Cut the interval into pieces. The change of `F` across one piece is "
                  "`F(t + h) − F(t)`, and those changes add up to `F(b) − F(a)` exactly, "
                  "because every interior value is added once and subtracted once. "
                  "For the ramp `2t`, with `F = t²` and four pieces of width `1/2`, the "
                  "piece changes are `1/4, 3/4, 5/4, 7/4`, and they add to `4`."),
            ("p", "The left sum charges each piece at the rate at its left end, "
                  "`0, 1, 2, 3`, so the pieces contribute `0, 1/2, 1, 3/2`, adding to the "
                  "`3` of “Total Change from a Rate”. Each of those contributions "
                  "is a flat guess at the matching change of `F`, and it is a good guess "
                  "because `F′ = f`: over a short piece, `F` changes by about its rate "
                  "times the width. Shorter pieces make each guess better. That is the "
                  "whole argument, and it is an argument, not a proof."),
            ("thm", ("The fundamental theorem, as the lab demonstrates it",
                     "If `F′ = f` on the interval from `a` to `b`, the left and right "
                     "sums of `f` approach `F(b) − F(a)` as the number of pieces grows, "
                     "and `F(b) − F(a)` is the total change, over the interval, of the "
                     "quantity whose rate is `f`.")),
            ("p", "The identity that the piece changes of `F` telescope to `F(b) − F(a)` is "
                  "algebra and holds exactly. The claim that the sums approach that number "
                  "is what the tables of the earlier lessons show for particular rates and "
                  "particular piece counts. Neither the tables nor the lab prove it for "
                  "every rate; a first analysis course does, and this Subject states it "
                  "and uses it."),
            ("p", "A constant added to `F` changes nothing here. If `G = F + 5` then "
                  "`G(b) − G(a) = (F(b) + 5) − (F(a) + 5) = F(b) − F(a)`, so the total "
                  "does not depend on which antiderivative was chosen. Where a constant "
                  "does matter is the subject of the next lesson."),
            ("example", ("A rate with three terms",
                         "The rate `3t² − 4t + 1` on the interval from `1` to `3`. Term by "
                         "term, `F = t³ − 2t² + t`, and the check `F′ = 3t² − 4t + 1` passes. "
                         "Then `F(3) = 27 − 18 + 3 = 12` and `F(1) = 1 − 2 + 1 = 0`.",
                         "The total change is `12 − 0 = 12`. The lab prints `12` on the "
                         "mixed preset, and the same value would appear however many "
                         "pieces you chose, because no pieces were used.")),
        ],
        "lab": ("calckit", {
            "mode": "antiderivative",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "Square: t² from 0 to 1",
                 "f": "t^2", "a": 0, "b": 1, "expect": {"adF": "t³/3 + C", "adDefinite": "1/3"}},
                {"id": "ramp", "label": "Ramp: 2t from 0 to 2",
                 "f": "2t", "a": 0, "b": 2, "expect": {"adF": "t² + C", "adDefinite": "4"}},
                {"id": "mixed", "label": "Mixed: 3t² − 4t + 1 from 1 to 3",
                 "f": "3t^2 - 4t + 1", "a": 1, "b": 3, "expect": {"adF": "t³ − 2t² + t + C", "adDefinite": "12"}},
            ],
            "panel_title": "Type a polynomial rate and read its antiderivative",
            "panel_intro": "The first tile is the antiderivative the reverse power rule "
                           "gives, with the constant left open. With the limits filled in, "
                           "the definite tile is F(b) − F(a) as an exact fraction. Change "
                           "the rate, predict F on paper, then compare.",
        }),
        "steps_title": "Totalling a rate by an antiderivative",
        "steps_intro": "Five moves, and the third is the one that catches a wrong answer before it is used.",
        "steps": [
            ("Write the rate as a sum of terms c·tⁿ",
             "Expand first if you must. A constant is the term with `n = 0`. Each term is "
             "handled alone and the results are added."),
            ("Raise each power by one and divide by the new power",
             "`c·tⁿ` becomes `c·tⁿ⁺¹/(n + 1)`. The division is the step that is easy to "
             "drop, because for `2t` it is invisible: `2t²/2 = t²`."),
            ("Differentiate F and compare with f",
             "Apply the power rule to your `F`. If the result is not exactly `f`, term by "
             "term, there is an error in the second move; do not go on."),
            ("Evaluate at the two ends and subtract",
             "Compute `F(b)` and `F(a)` as fractions, then `F(b) − F(a)`. Keep the order: "
             "the right end first."),
            ("Say what the number is",
             "It is the total change over the interval of the quantity whose rate is `f`. It is exact, and it is "
             "the number the sums of the earlier lessons approach, by a claim this course "
             "demonstrates and does not prove."),
        ],
        "worked": {
            "title": "The square t² from 0 to 1, without a sum",
            "intro": [
                "Find the total change the rate `t²` produces on the interval from `0` to `1` by "
                "an antiderivative, check the antiderivative, and compare the answer with "
                "the left sums.",
            ],
            "lines": [
                "f(t) = t² on [0, 1]",
                "raise the power: t³;  divide by the new power: t³/3",
                "check: (t³/3)′ = 3t²/3 = t²   passes",
                "without the division: (t³)′ = 3t²   fails",
                "F(1) − F(0) = 1/3 − 0 = 1/3",
                "left sums, n = 4, 8, 16:  7/32, 35/128, 155/512",
                "their gaps from 1/3:  11/96, 23/384, 47/1536",
            ],
            "after": [
                "One subtraction gives the number the sums were closing in on, and the gaps "
                "shrink the way “Refining the Partition” found, by a factor near two each "
                "time the pieces doubled. The antiderivative has no such gap: it is the "
                "total, not an estimate of it.",
                "For a rehearsal, take the mixed preset. The supplied first move is that "
                "the three terms become `t³`, `−2t²` and `t`. Differentiate your result "
                "to see `3t² − 4t + 1` come back, then evaluate at `3` and at `1` and "
                "subtract.",
            ],
        },
        "quiz_title": "Reversing the power rule",
        "quiz": [
            {"q": "Which function is an antiderivative of `6t²`?",
             "a": ["6t³", "3t", "2t³", "t³/2"],
             "c": 2,
             "why": "`6t²` becomes `6t³/3 = 2t³`, and `(2t³)′ = 6t²`. `6t³` forgets the "
                    "division: its derivative is `18t²`. `3t` is the antiderivative of "
                    "`3`, not of `6t²`. `t³/2` has a derivative of `3t²/2`, which is "
                    "not `6t²` either."},
            {"q": "The rate is `3t²`. What is the total change from `t = 1` to `t = 2`?",
             "a": ["7", "8", "12", "3"],
             "c": 0,
             "why": "`F = t³`, so `F(2) − F(1) = 8 − 1 = 7`. `8` is `F(2)` alone, with the "
                    "value at the left end forgotten. `12` is the rate at the right end, "
                    "`3·4`, times the width `1`, the shortcut “Total Change from a Rate” warned against. `3` is "
                    "the rate at the left end times the width."},
            {"q": "A reader claims `t³` is an antiderivative of `t²`. What settles it?",
             "a": ["Nothing: the claim cannot be tested without computing sums",
                   "Evaluating `t³` at `0` and `1` and finding `1`",
                   "Noting that `t³` is a higher power than `t²`",
                   "Differentiating `t³`: the result is `3t²`, not `t²`, so the claim fails"],
             "c": 3,
             "why": "An antiderivative is defined by its derivative, so the test is to "
                    "differentiate. `(t³)′ = 3t²`. No sums are needed. Evaluating at two "
                    "points gives a number and does not test `F′ = f`. A higher power is "
                    "what the rule produces, and the division is what makes it right."},
            {"q": "For the rate `3t² − 4t + 1` on the interval from `1` to `3` the lab prints `12`. What would it print if `F` were replaced by `F + 7`?",
             "a": ["19", "12", "5", "26"],
             "c": 1,
             "why": "`(F(3) + 7) − (F(1) + 7) = F(3) − F(1) = 12`; the added constant "
                    "cancels. `19` and `5` add or subtract `7` once, as if it did not "
                    "appear at both ends. `26` adds it twice."},
        ],
        "mistakes": [
            ("Raising the power and forgetting to divide",
             "The antiderivative of `t²` is written `t³`, because the rule seemed to say "
             "only “add one to the power”. Differentiating gives `3t²`, three times the "
             "rate. The division by the new power is half of the rule. It hides on `2t`, "
             "where `2t²/2 = t²` looks like no division at all, which is how the habit "
             "survives until the first rate that exposes it."),
            ("Thinking F(b) − F(a) depends on which constant was chosen",
             "`t³/3`, `t³/3 + 4` and `t³/3 − 100` all have derivative `t²`, and all give "
             "`1/3` between `0` and `1`, because the constant is added at both ends and "
             "subtracted once. The total belongs to the rate, not to the antiderivative "
             "picked to compute it."),
            ("Taking the demonstration for a proof",
             "The sums `7/32, 35/128, 155/512` approach `1/3` for the square, and that "
             "is all the table says. That an antiderivative gives the total for every "
             "rate is the claim; the telescoping of `F` is exact algebra, and the step "
             "from there to the sums is the part this course shows and leaves unproved."),
        ],
        "standard": ("Finish when you can find an antiderivative, check it, and use it to total a rate exactly.",
                     "You should be able to reverse the power rule on every term of a "
                     "polynomial, confirm the result by differentiating it, evaluate "
                     "`F(b) − F(a)` as an exact fraction, and say why the answer does not "
                     "depend on a constant added to `F` and why it is a claim and not a "
                     "proof that the sums approach it."),
        "note": "The antiderivative came with a constant left open, and the total ignored it. &ldquo;The Constant of Integration&rdquo; asks when the constant matters and what fixes it.",
    },

    # ---------------------------------------------------------------- 06
    {
        "slug": "the-constant-of-integration",
        "title": "The Constant of Integration",
        "module": "The exact total",
        "one_line": "A rate has a whole family of antiderivatives, each differing by a constant, and exactly one given value picks the member.",
        "summary": (
            "Every antiderivative of a rate differs from every other by a constant, so the "
            "answer to the question of which function has this rate is a family and not a "
            "function. A total change does not see the constant, but a value of the "
            "quantity itself does. One given value is a single equation for the single "
            "unknown constant, and it is exactly enough. This is the simplest differential "
            "equation with its initial value, which the next courses make harder."
        ),
        "key": [
            "F′ = f is solved by a family: F + C",
            "two antiderivatives differ by a constant",
            "y(t₀) = y₀ gives C = y₀ − F(t₀)",
            "one value, one unknown: exactly enough",
            "C is zero only if F(t₀) already equals y₀",
        ],
        "key_label": "A family of antiderivatives and the value that picks one",
        "concepts_intro": (
            "Three ideas: the family, the reason it contains every antiderivative, and the "
            "arithmetic of picking one member."
        ),
        "concepts": [
            ("The answer to F′ = f is a family",
             "`t²`, `t² + 4` and `t² − 7` all have derivative `2t`, so all are "
             "antiderivatives of `2t`. Their graphs are the same curve moved up or down. "
             "The lab draws five of them and the one member through a chosen point."),
            ("The family has every antiderivative in it",
             "If `F` and `G` both have derivative `f`, then `F − G` has derivative `0`, "
             "and a polynomial with derivative `0` is a constant. So `G = F + C` for some "
             "`C`, and writing `F + C` leaves nothing out."),
            ("One given value fixes the constant",
             "A value `y(t₀) = y₀` says `F(t₀) + C = y₀`. That is one equation, with `C` "
             "appearing once and with coefficient `1`, so `C = y₀ − F(t₀)` and there is "
             "exactly one solution."),
        ],
        "read_title": "Why +C, and how one value removes it",
        "read_intro": "The tank that gains water at a known rate, the proof that nothing is missing from the family, and the arithmetic of the constant.",
        "body": [
            ("p", "A tank gains water at `2t` litres per minute, `t` minutes after a tap "
                  "opens. The rate tells you how much water arrives; it does not tell you "
                  "how much was in the tank to begin with. A tank that held `4` litres at "
                  "the start and one that held `100` gain water identically. The total "
                  "change of the previous lesson never needed the starting amount. The "
                  "amount in the tank at a given time does."),
            ("def", ("A family and an initial value",
                     "The antiderivatives of `f` are the <strong>family</strong> "
                     "`F + C`, one for each constant `C`. An <strong>initial value</strong> "
                     "is a given pair `y(t₀) = y₀`.",
                     "The pair of conditions `y′ = f(t)` and `y(t₀) = y₀` is the simplest "
                     "differential equation there is: a rule for the rate, and one value "
                     "to start from. The rest of this Subject is that sentence with "
                     "harder rules.")),
            ("p", "Take `y′ = 2t` with `y(1) = 5`. The family is `y = t² + C`. The given "
                  "value says `1² + C = 5`, so `C = 4` and `y = t² + 4`. The lab draws "
                  "the family as parallel copies of one curve and marks the member "
                  "through the point `(1, 5)`."),
            ("math", [
                "y = t² + C, at t = 1",
                "",
                "C = −2      y(1) = −1",
                "C = 0       y(1) = 1",
                "C = 4       y(1) = 5     (the one given)",
                "C = 10      y(1) = 11",
                "",
                "every member has y′ = 2t",
            ]),
            ("h3", "Why nothing is missing, and why one value is enough"),
            ("thm", ("Two antiderivatives of a polynomial differ by a constant",
                     "If `F′ = G′` for polynomials `F` and `G`, then `F − G` is a "
                     "constant.")),
            ("proof", ["Let `D = F − G`. By the sum rule of “The Derivative as a Function”, "
                       "`D′ = F′ − G′ = 0`.",
                       "Write `D = c₀ + c₁t + c₂t² + … + c_k·tᵏ`. Its derivative is "
                       "`c₁ + 2c₂·t + … + k·c_k·tᵏ⁻¹`, and a polynomial is zero only "
                       "when every coefficient is zero. So `c₁ = 0`, `2c₂ = 0`, and so on "
                       "to `k·c_k = 0`, which forces `c₁ = c₂ = … = c_k = 0`. Only `c₀` "
                       "is left, and `D = c₀`."]),
            ("p", "That proof is for polynomials, the only rates the lab accepts. For "
                  "other functions the same statement is true and is not proved here. "
                  "One value then does the rest. Without a value the family is every "
                  "curve; with `y(1) = 5` it is one. A second value either repeats the "
                  "first or contradicts it: `t² + 4` already gives `y(2) = 8`, and asking "
                  "for `y(2) = 9` as well would need `C = 5` and `C = 4` together."),
            ("example", ("The constant is not zero because the value is zero",
                         "Take `y′ = 3t²` with `y(2) = 0`. The family is `y = t³ + C`, "
                         "and `2³ + C = 0` gives `C = −8`, so `y = t³ − 8`.",
                         "The value `0` is the height of the curve at `t = 2`, not the "
                         "constant. `C` is the difference between that height and "
                         "`F(2) = 8`.")),
            ("p", "The constant is zero when the value agrees with `F`, and that can be "
                  "arranged. The cubic preset is `t³ − t` with `y(0) = 1/2`. Here "
                  "`F = t⁴/4 − t²/2`, and `F(0) = 0`, so `C = 1/2 − 0 = 1/2` and "
                  "`y = t⁴/4 − t²/2 + 1/2`. Starting at `t = 0` makes `C` equal to the "
                  "starting value itself, which is why a reader who always starts there "
                  "can come to think `C` is simply the start."),
        ],
        "lab": ("calckit", {
            "mode": "antiderivative",
            "preset": "through-five",
            "presets": [
                {"id": "through-five", "label": "Through (1, 5): rate 2t",
                 "f": "2t", "ic": [1, 5], "expect": {"adF": "t² + C", "adC": "4"}},
                {"id": "through-zero", "label": "Through (2, 0): rate 3t²",
                 "f": "3t^2", "ic": [2, 0], "expect": {"adF": "t³ + C", "adC": "−8"}},
                {"id": "cubic", "label": "Cubic: rate t³ − t, value one half at zero",
                 "f": "t^3 - t", "ic": [0, "1/2"], "expect": {"adF": "t⁴/4 − t²/2 + C", "adC": "1/2"}},
            ],
            "panel_title": "Give a rate and one value, and read the constant",
            "panel_intro": "Type the rate, then the initial value as two numbers: the "
                           "time and the value there. The constant tile is y0 minus F at "
                           "that time. The picture shows the family and, in green, the "
                           "member through the point.",
        }),
        "steps_title": "Fixing the constant from one value",
        "steps_intro": "The only new move is the third. Do the check at the end, because it catches both kinds of slip.",
        "steps": [
            ("Find an antiderivative F of the rate",
             "Reverse the power rule on each term and check by differentiating. Leave "
             "the constant out for now."),
            ("Write the family y = F(t) + C",
             "Every solution of `y′ = f` is in it. Say so in the line, so that the `C` "
             "is not dropped by habit."),
            ("Put the given value into the family",
             "Replace `t` by `t₀` and `y` by `y₀`: `F(t₀) + C = y₀`. Evaluate `F(t₀)` as a "
             "fraction. The unknown is only `C`."),
            ("Solve for C",
             "`C = y₀ − F(t₀)`. Do not copy `y₀` into `C` unless `F(t₀)` is zero."),
            ("Check both conditions",
             "Differentiate the final `y` and compare with the rate; evaluate it at `t₀` "
             "and compare with `y₀`. A solution passes both."),
        ],
        "worked": {
            "title": "A tank with the rate 2t that holds 5 litres at t = 1",
            "intro": [
                "Find the amount `y(t)` in a tank that gains water at `2t` litres per "
                "minute and holds `5` litres at `t = 1`.",
            ],
            "lines": [
                "y′ = 2t,  y(1) = 5",
                "F(t) = t²   (check: F′ = 2t)",
                "family:  y = t² + C",
                "value:   1² + C = 5",
                "C = 5 − 1 = 4",
                "y = t² + 4",
                "check:  y′ = 2t,  y(1) = 1 + 4 = 5",
                "the tank held y(0) = 4 at the start",
            ],
            "after": [
                "One equation, one unknown. The same rate with a different value gives the "
                "same curve moved up or down, and the lab shows the move when the second "
                "number changes. The amount at `t = 0` was never given; it came out of the "
                "formula as `4`.",
                "For a rehearsal, take the through-zero preset. The supplied first move is "
                "that `F = t³`. Put `t = 2` into `t³ + C = 0`, solve, and check that your "
                "`y` has derivative `3t²` and value `0` at `t = 2`.",
            ],
        },
        "quiz_title": "A family and the value that picks one",
        "quiz": [
            {"q": "The rate is `4t` and `y(0) = 3`. Which function is the solution?",
             "a": ["4t² + 3", "2t² − 3", "2t² + 3", "2t² + 4"],
             "c": 2,
             "why": "`F = 2t²`, and `F(0) = 0`, so `C = 3 − 0 = 3`. `4t² + 3` forgets the "
                    "division by the new power. `2t² − 3` has the sign of `C` wrong. "
                    "`2t² + 4` takes `C` from the coefficient of the rate."},
            {"q": "The rate is `3t²` and `y(1) = 2`. What is `C`?",
             "a": ["0", "3", "2", "1"],
             "c": 3,
             "why": "`F = t³`, `F(1) = 1`, and `C = 2 − 1 = 1`. `C = 2` copies the given "
                    "value without subtracting `F(1)`; then `y(1)` would be `3`. `C = 0` "
                    "assumes the constant vanishes, and `y(1)` would be `1`. `C = 3` has "
                    "no source."},
            {"q": "`F` and `G` are two antiderivatives of the same polynomial `f`. What is true of `F − G`?",
             "a": ["It is a constant", "It is zero", "It equals f", "It is a polynomial of degree one"],
             "c": 0,
             "why": "The difference has derivative `0`, so it is a constant. It need not "
                    "be zero: `(t² + 4) − t² = 4`. It cannot be `f`, whose derivative is "
                    "not `0`, and a polynomial of degree one has a derivative that is a "
                    "nonzero constant."},
            {"q": "A reader is told `y′ = 2t`, `y(1) = 5` and `y(2) = 9`. What follows?",
             "a": ["C = 9/2, the average of the two",
                   "The first value gives C = 4 and the second C = 5, so no function fits both",
                   "C = 5, because the later value wins",
                   "Both are fine, because C is not unique"],
             "c": 1,
             "why": "`1 + C = 5` gives `C = 4`; `4 + C = 9` gives `C = 5`. One constant "
                    "cannot be both, and no averaging or ranking makes it so. `C` is "
                    "unique once one value is given, which is why a second value is "
                    "either redundant or inconsistent."},
        ],
        "mistakes": [
            ("Taking the constant to be zero unless told otherwise",
             "For `y′ = 2t` with `y(1) = 5` the constant is `4`, and for `y′ = 3t²` with "
             "`y(2) = 0` it is `−8`. A zero constant means the curve passes through the "
             "plain antiderivative, which happens only if `F(t₀)` is already `y₀`. "
             "The habit comes from the previous lesson, where the constant dropped out "
             "of the total and could be left out."),
            ("Copying the given value into the constant",
             "From `y(1) = 5` it is tempting to write `y = t² + 5`. At `t = 1` that "
             "gives `6`. The value is the height of the curve, the constant is the "
             "height minus `F(t₀)`, and the two agree only when `F(t₀) = 0`, as for "
             "`t₀ = 0` with the polynomials here."),
            ("Dropping the constant because the total did not need it",
             "`F(b) − F(a)` cancelled the constant, so leaving it out cost nothing. A "
             "value of the quantity does not cancel it: the tank's amount at `t = 3` "
             "is `13` with `C = 4` and `9` with `C = 0`. The rate fixes how the "
             "quantity changes; only a value fixes where it is."),
        ],
        "standard": ("Finish when you can write the family of antiderivatives and fix its constant from one value.",
                     "You should be able to find `F`, write `y = F(t) + C`, solve "
                     "`F(t₀) + C = y₀` for `C` as an exact fraction, check the result "
                     "against both the rate and the given value, and say why one value "
                     "is exactly enough while none is too few and two are redundant or "
                     "contradictory."),
        "note": "Sums, antiderivatives and constants are now all in play, and they want a compact notation. &ldquo;The Integral Sign and Its Rules&rdquo; supplies it and checks two rules for it on exact fractions.",
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "the-integral-sign-and-its-rules",
        "title": "The Integral Sign and Its Rules",
        "module": "Notation and a second integral",
        "one_line": "The integral sign names the total change a rate produces over an interval, it obeys linearity and additivity, and the integral of a product is not the product of the integrals.",
        "summary": (
            "The symbol with limits is shorthand for the total change a rate produces over an "
            "interval, and it is read aloud as that. Two rules follow from the "
            "antiderivative and are checked here by computing both sides as exact "
            "fractions: constants and sums pass through the sign, and an interval can be "
            "cut at any interior point. A third, tempting rule is false, and one example "
            "refutes it."
        ),
        "key": [
            "∫ₐᵇ f(t) dt = F(b) − F(a)",
            "t is a placeholder: any letter, same number",
            "∫(c·f + d·g) = c·∫f + d·∫g",
            "∫ₐᵐ f dt + ∫ₘᵇ f dt = ∫ₐᵇ f dt",
            "∫ f·g is not the product of ∫f and ∫g",
        ],
        "key_label": "The integral sign and the rules it obeys",
        "concepts_intro": (
            "Three ideas: how to read the symbol, the two rules that hold, and the rule "
            "that does not."
        ),
        "concepts": [
            ("The symbol is the total change, written short",
             "`∫ₐᵇ f(t) dt` is read aloud as “the integral from a to b of f of t, d t”. "
             "It is the number the sums of `f` approach, and for a polynomial it is "
             "`F(b) − F(a)`. The `dt` recalls the width `h` in rate times width, and the "
             "stretched S recalls a sum."),
            ("Constants and sums pass through the sign; intervals can be cut",
             "`∫ₐᵇ (c·f + d·g) dt = c·∫ₐᵇ f dt + d·∫ₐᵇ g dt`, and for `m` between `a` and "
             "`b`, `∫ₐᵐ f dt + ∫ₘᵇ f dt = ∫ₐᵇ f dt`. The lab computes both sides of "
             "each and says whether they are equal."),
            ("A product does not pass through",
             "`∫₀¹ t·t dt = 1/3`, but `∫₀¹ t dt` times `∫₀¹ t dt` is `1/4`. The integral "
             "of a product is not the product of the integrals."),
        ],
        "read_title": "Reading the symbol, and two rules that follow from F",
        "read_intro": "The notation, the two rules with proofs that use the antiderivative, and the rule that fails.",
        "body": [
            ("p", "The phrase “the total change the rate `f` produces from `a` to `b`” has "
                  "appeared in every lesson of this course, and a short form for it makes "
                  "the rules below possible to write. The short form is built from the sums. "
                  "A left sum is `f(t)·h` added over the pieces; the integral sign is a "
                  "stretched S for the adding, `f(t)` is the rate, `dt` stands where the "
                  "width `h` stood, and the limits `a` and `b` are the ends."),
            ("def", ("The integral from a to b",
                     "For a polynomial rate `f` with antiderivative `F`, "
                     "`∫ₐᵇ f(t) dt = F(b) − F(a)`. It is the total change from `a` to `b` "
                     "of a quantity whose rate is `f`, a number, and the number the sums "
                     "of `f` approach.",
                     "The letter `t` is a placeholder: `∫₀² 3t² dt` and `∫₀² 3s² ds` are "
                     "both `8`, and neither depends on a variable `t`.")),
            ("p", "Read aloud, `∫₀² (3t² + 2t) dt` is “the integral from 0 to 2 of "
                  "3 t squared plus 2 t, d t”, and in words it is the total change from `0` to `2` "
                  "of a quantity whose rate is `3t² + 2t`. With `F = t³ + t²`, the value is "
                  "`F(2) − F(0) = 12`."),
            ("math", [
                "∫₀² 3t² dt = 8       ∫₀² 2t dt = 4",
                "8 + 4 = 12 = ∫₀² (3t² + 2t) dt",
                "",
                "∫₀¹ (3t² + 2t) dt = 1 + 1 = 2",
                "∫₁² (3t² + 2t) dt = 7 + 3 = 10",
                "2 + 10 = 12",
            ]),
            ("thm", ("Linearity",
                     "For polynomials `f` and `g` and numbers `c` and `d`, "
                     "`∫ₐᵇ (c·f + d·g) dt = c·∫ₐᵇ f dt + d·∫ₐᵇ g dt`.")),
            ("proof", ["Let `F′ = f` and `G′ = g`. By the sum and constant rules of "
                       "“The Derivative as a Function”, `(c·F + d·G)′ = c·f + d·g`, so "
                       "`c·F + d·G` is an antiderivative of `c·f + d·g`.",
                       "The left side is therefore `(c·F(b) + d·G(b)) − (c·F(a) + d·G(a))`, "
                       "and regrouping gives `c·(F(b) − F(a)) + d·(G(b) − G(a))`, which "
                       "is the right side."]),
            ("thm", ("Additivity over adjacent intervals",
                     "For `m` between `a` and `b`, "
                     "`∫ₐᵐ f dt + ∫ₘᵇ f dt = ∫ₐᵇ f dt`.")),
            ("proof", ["The left side is `(F(m) − F(a)) + (F(b) − F(m))`. The two `F(m)` "
                       "cancel, and what is left is `F(b) − F(a)`."]),
            ("p", "Both proofs lean on `∫ₐᵇ f dt = F(b) − F(a)`, the claim of “The "
                  "Antiderivative and the Fundamental Theorem”. They are exact for the "
                  "polynomials the lab accepts, and they are only as strong as that claim. "
                  "On the scaled preset, `6·∫₀¹ t² dt − 2·∫₀¹ t dt = 6·(1/3) − 2·(1/2) = "
                  "2 − 1 = 1`, and the lab prints both sides."),
            ("h3", "The rule that fails"),
            ("example", ("The integral of a product",
                         "Put `f = g = t` on the interval from `0` to `1`. The product is "
                         "`t·t = t²`, and `∫₀¹ t² dt = 1/3`. Each factor has "
                         "`∫₀¹ t dt = 1/2`, and the product of those is `1/4`.",
                         "`1/3` is not `1/4`. The proofs above worked because "
                         "`(c·F + d·G)′ = c·f + d·g`. For a product, `(F·G)′` is "
                         "`f·G + F·g` by “The Product Rule”, not `f·g`, so `F·G` is not an "
                         "antiderivative of `f·g`. The scaled preset already runs from "
                         "`0` to `1` and its definite tile prints `1/3` for the rate `t²`; "
                         "type `t` in its place and the tile prints `1/2`.")),
        ],
        "lab": ("calckit", {
            "mode": "antiderivative",
            "preset": "linear",
            "presets": [
                {"id": "linear", "label": "Sum: 3t² and 2t from 0 to 2",
                 "f": "3t^2", "g": "2t", "coeffs": [1, 1], "a": 0, "b": 2, "expect": {"adDefinite": "8", "adLinear": "equal: 12 = 8 + 4"}},
                {"id": "scaled", "label": "Scaled: 6 times t² minus 2 times t, from 0 to 1",
                 "f": "t^2", "g": "t", "coeffs": [6, -2], "a": 0, "b": 1, "expect": {"adDefinite": "1/3", "adLinear": "equal: 1 = 2 − 1"}},
                {"id": "split", "label": "Split: 3t² + 2t from 0 to 2, cut at 1",
                 "f": "3t^2 + 2t", "a": 0, "b": 2, "split": 1, "expect": {"adDefinite": "12", "adSplit": "equal: 12 = 2 + 10"}},
            ],
            "panel_title": "Compute both sides of a rule",
            "panel_intro": "With a second rate and two coefficients the linearity tile "
                           "shows the integral of the combination beside the combination "
                           "of the integrals. With a split point the adjacent tile shows "
                           "the whole beside its two parts. Each says equal or differ.",
        }),
        "steps_title": "Using the sign and its rules",
        "steps_intro": "Read first, compute second, and use a rule only when its conditions are in front of you.",
        "steps": [
            ("Read the symbol aloud and name its parts",
             "Say “the integral from a to b of f of t, d t”. Name the rate, the "
             "two limits and the placeholder. The result will be a number."),
            ("Find an antiderivative of the whole rate",
             "Reverse the power rule term by term and check by differentiating."),
            ("Evaluate F(b) − F(a)",
             "Right end first. That is the value, as an exact fraction."),
            ("To use a rule, state what is being combined",
             "A sum or a constant multiple: pull the constants out and split the sum. An "
             "interior point `m`: compute `∫ₐᵐ f dt` and `∫ₘᵇ f dt` and add. Compute at least "
             "one by the other route as a check."),
            ("Refuse the rule that is not there",
             "If the rate is a product, multiply out and integrate the polynomial. Never "
             "multiply two integrals to get the integral of a product."),
        ],
        "worked": {
            "title": "One integral, computed whole, by linearity, and by cutting",
            "intro": [
                "Compute `∫₀² (3t² + 2t) dt` three ways and see that they agree.",
            ],
            "lines": [
                "F(t) = t³ + t²   (F′ = 3t² + 2t)",
                "whole:  F(2) − F(0) = (8 + 4) − 0 = 12",
                "linearity:  ∫₀² 3t² dt = 8,  ∫₀² 2t dt = 4",
                "            8 + 4 = 12",
                "cut at 1:  ∫₀¹ (3t² + 2t) dt = F(1) − F(0) = 2",
                "           ∫₁² (3t² + 2t) dt = F(2) − F(1) = 10",
                "           2 + 10 = 12",
            ],
            "after": [
                "Three routes, one fraction. The lab prints each of them: the linear preset "
                "shows `12 = 8 + 4` and the split preset `12 = 2 + 10`. Agreement is not "
                "luck, since the cancellations of the two proofs are exactly what happens "
                "in each subtraction.",
                "For a rehearsal, take the scaled preset. The supplied first move is that "
                "the coefficients are `6` and `−2`. Compute `∫₀¹ t² dt` and `∫₀¹ t dt` "
                "separately, combine, and then compute `∫₀¹ (6t² − 2t) dt` directly.",
            ],
        },
        "quiz_title": "Reading and using the sign",
        "quiz": [
            {"q": "What is `∫₀³ 2t dt`?",
             "a": ["6", "18", "3", "9"],
             "c": 3,
             "why": "`F = t²`, so `F(3) − F(0) = 9`. `6` is the rate at `t = 3` and not a "
                    "total. `18` is the rate at the right end times the width, `6·3`. "
                    "`3` is the width."},
            {"q": "`∫₀¹ f dt = 2` and `∫₁⁴ f dt = 5`. What is `∫₀⁴ f dt`?",
             "a": ["3", "10", "7", "7/2"],
             "c": 2,
             "why": "The intervals are adjacent and share the point `1`, so the totals "
                    "add: `2 + 5 = 7`. `3` subtracts, `10` multiplies, and `7/2` averages; "
                    "none of those is a total over the joined interval."},
            {"q": "`∫₀¹ t dt = 1/2` and `∫₀¹ t² dt = 1/3`. What is `∫₀¹ t·t dt`?",
             "a": ["1/6", "1/4", "1/3", "1/2"],
             "c": 2,
             "why": "The product `t·t` is `t²`, so the value is `1/3`. `1/6` multiplies the "
                    "two integrals given, which is the false product rule. `1/4` multiplies "
                    "`1/2` by itself, the same mistake with the right factors. `1/2` is "
                    "just `∫₀¹ t dt`."},
            {"q": "Which sentence correctly reads `∫₁⁵ g(t) dt`?",
             "a": ["g(5) − g(1)",
                   "The total change from t = 1 to t = 5 of a quantity whose rate is g",
                   "The rate g times the width 4",
                   "The sum of g(1), g(2), g(3), g(4) and g(5)"],
             "c": 1,
             "why": "The sign names a total change of the quantity whose rate is `g`. "
                    "`g(5) − g(1)` is a change of `g` itself, not of its antiderivative. "
                    "A rate times a width is one frozen piece. A sum of five values of `g` "
                    "leaves out the widths."},
        ],
        "mistakes": [
            ("Believing the integral of a product is the product of the integrals",
             "For `t·t` on the interval from `0` to `1` the integral is `1/3`, and "
             "the product of the two single integrals is `1/4`. The rules that hold "
             "are for sums and constant multiples, where `(c·F + d·G)′ = c·f + d·g`; "
             "no such identity exists for `F·G`."),
            ("Dropping the coefficients when splitting a combination",
             "`∫₀¹ (6t² − 2t) dt` is `6·(1/3) − 2·(1/2) = 1`. Writing it as "
             "`∫₀¹ t² dt − ∫₀¹ t dt` gives `1/3 − 1/2 = −1/6`. The constants come out "
             "of the sign, but they come out as multipliers and they stay."),
            ("Treating the integral as a function of t",
             "`∫₀² 3t² dt` is `8`. The `t` inside is a placeholder that disappears when "
             "the limits go in, and `∫₀² 3s² ds` is the same `8`. A reader who "
             "writes `t³` for it has stopped one step early, at `F`."),
        ],
        "standard": ("Finish when you can read the integral sign aloud and check linearity and additivity exactly.",
                     "You should be able to say `∫ₐᵇ f(t) dt` in words, evaluate it as "
                     "`F(b) − F(a)`, compute both sides of linearity with coefficients "
                     "and of additivity at an interior point and compare them, and "
                     "refute the product rule for integrals with one example."),
        "note": "Every integral so far came from reversing the power rule. &ldquo;The Integral of 1/t&rdquo; meets a rate that the power rule cannot reverse, and the sums are all there is to go on.",
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "the-integral-of-one-over-t",
        "title": "The Integral of 1/t",
        "module": "Notation and a second integral",
        "one_line": "The reverse power rule has no answer for one over t, and the exact sums bracket a number that is not a fraction, written ln x.",
        "summary": (
            "The power rule reversed divides by one more than the power, and for one over t "
            "that is a division by zero. The sums still work: left, right and trapezoid "
            "sums on the interval from 1 to 2 are exact fractions that bracket a number the "
            "lab can print only as a rounded decimal. The lesson states that the number is "
            "ln 2 and, more generally, that the integral from 1 to x of one over t is "
            "ln x, as a claim the sums support."
        ),
        "key": [
            "tⁿ → tⁿ⁺¹/(n + 1) fails for n = −1",
            "L₄ = 319/420, R₄ = 533/840 on [1, 2]",
            "ln 2 ≈ 0.693147 sits between R₄ and L₄",
            "claim: ∫₁ˣ dt/t = ln x",
            "every sum is a fraction; ln 2 is not",
        ],
        "key_label": "The one integral the power rule cannot reach",
        "concepts_intro": (
            "Three ideas: why the usual reversal fails, what the sums do instead, and "
            "what the number is called."
        ),
        "concepts": [
            ("The power rule reversed has nothing to say about 1/t",
             "`1/t` is `t⁻¹`, and the reversal would give `t⁰/0`. A division by zero is "
             "not an antiderivative. No polynomial has derivative `1/t`, because a "
             "polynomial's derivative never contains a term in `t⁻¹`."),
            ("The sums bracket a number that no fraction equals",
             "On the interval from `1` to `2` with four pieces, the left sum is "
             "`319/420 ≈ 0.759524` and the right sum is `533/840 ≈ 0.634524`. The rate "
             "falls, so the total lies between: `≈ 0.693147`, rounded."),
            ("The number is ln x, as a claim",
             "The integral from `1` to `x` of `1/t` is written `ln x`, the natural "
             "logarithm. The lab prints it rounded and labelled. That the sums approach "
             "it is demonstrated here, not proved."),
        ],
        "read_title": "A rate with no polynomial antiderivative",
        "read_intro": "The failed reversal, the exact sums, what refining them shows, and a scaling that makes the logarithm's addition rule visible.",
        "body": [
            ("p", "Every integral so far had an antiderivative from the reversed power "
                  "rule: raise the power, divide by the new one. Try it on `1/t = t⁻¹`. "
                  "The new power is `0` and the division is by `0`. Nothing is wrong with "
                  "the rate: `1/t` is a perfectly good falling rate on the interval from "
                  "`1` to `2`, and the sums of the earlier lessons apply to it unchanged. "
                  "What fails is the shortcut."),
            ("math", [
                "1/t on [1, 2],  n = 4,  h = 1/4",
                "",
                "left ends:   1    5/4   3/2   7/4",
                "rates:       1    4/5   2/3   4/7",
                "L₄ = (1/4)·(1 + 4/5 + 2/3 + 4/7) = 319/420 ≈ 0.759524",
                "R₄ = (1/4)·(4/5 + 2/3 + 4/7 + 1/2) = 533/840 ≈ 0.634524",
                "T₄ = (L₄ + R₄)/2 = 1171/1680 ≈ 0.697024",
            ]),
            ("p", "The rate falls, so by “Left and Right Sums” the total lies between "
                  "the right sum and the left sum, and the window has width "
                  "`h·(f(1) − f(2)) = (1/4)·(1/2) = 1/8`. The lab's exact-total tile prints "
                  "`≈ 0.693147 (ln 2, rounded)`. The `≈` and the word “rounded” are there "
                  "because that figure is a double-precision evaluation, printed to six "
                  "figures; the sums are exact and the total is not."),
            ("h3", "Why no refinement ends in a fraction"),
            ("p", "Refine the pieces and the left sum drops: `n = 8` gives "
                  "`52279/72072 ≈ 0.725372`, and `n = 16` gives `≈ 0.709016`. Each is a "
                  "different exact fraction, with a larger denominator, and each is above "
                  "the target by about half what the last one was. The target `ln 2` is "
                  "not a fraction. That is a known fact of mathematics and is not proved "
                  "here; what the lab shows is that no sum it can print is equal to the "
                  "target."),
            ("thm", ("The integral of 1/t",
                     "For `x > 1` the left and right sums of `1/t` on the interval from "
                     "`1` to `x` approach a number written `ln x`, the natural logarithm, "
                     "and `∫₁ˣ dt/t = ln x`.")),
            ("p", "This is a claim, supported by the brackets above and by the "
                  "presets for `x = 3` and `x = 4`, and not proved. Here `ln x` is the "
                  "natural logarithm of “Common and Natural Logarithms” in Algebra's "
                  "Exponential and Logarithmic Functions, the power to which `e` is "
                  "raised to give `x`; that accumulating `1/t` produces it is the "
                  "claim."),
            ("thm", ("Scaling leaves the sums of 1/t unchanged",
                     "For every `n`, the left sum of `1/t` on the interval from `2a` "
                     "to `2b` with `n` pieces equals the left sum on the interval from "
                     "`a` to `b` with `n` pieces.")),
            ("proof", ["On the interval from `a` to `b` a piece has left end `t` and "
                       "width `h`, contributing `(1/t)·h`. On the doubled interval the "
                       "matching piece has left end `2t` and width `2h`, contributing "
                       "`(1/(2t))·2h = (1/t)·h`.",
                       "Each piece contributes the same amount, so the two sums are "
                       "equal term by term."]),
            ("example", ("The sum for 2 to 4 is the sum for 1 to 2",
                         "Select the scaled preset: `1/t` with limits `2` and `4` and four "
                         "pieces. The left ends are `2, 5/2, 3, 7/2`, the rates "
                         "`1/2, 2/5, 1/3, 2/7`, the width `1/2`, and the sum is "
                         "`(1/2)·(1/2 + 2/5 + 1/3 + 2/7) = 319/420`, exactly the sum "
                         "for `1` to `2`.",
                         "So the total from `2` to `4` equals the total from `1` to `2`, "
                         "and by additivity the total from `1` to `4` is twice it. The "
                         "ln4 preset agrees: with six pieces, `L₆ = 223/140 ≈ 1.59286` "
                         "and `R₆ = 341/280 ≈ 1.21786`, and between them the lab's "
                         "total `≈ 1.38629`, which is `2·ln 2`, rounded.")),
            ("p", "That is the addition rule of logarithms, `ln 4 = 2·ln 2`, appearing "
                  "as an exact equality of fractions for every `n`, with only the limit "
                  "left as a claim."),
        ],
        "lab": ("calckit", {
            "mode": "riemann",
            "rule": "left",
            "preset": "ln2",
            "presets": [
                {"id": "ln2", "label": "One over t from 1 to 2, four pieces",
                 "f": "1/t", "a": 1, "b": 2, "n": 4, "expect": {"rsSum": "319/420", "rsExact": "≈ 0.693147 (ln 2, rounded)"}},
                {"id": "ln4", "label": "One over t from 1 to 4, six pieces",
                 "f": "1/t", "a": 1, "b": 4, "n": 6, "expect": {"rsSum": "223/140", "rsExact": "≈ 1.38629 (ln 4, rounded)"}},
                {"id": "ln3", "label": "One over t from 1 to 3, four pieces",
                 "f": "1/t", "a": 1, "b": 3, "n": 4, "expect": {"rsSum": "77/60", "rsExact": "≈ 1.09861 (ln 3, rounded)"}},
                {"id": "scaled", "label": "One over t from 2 to 4, four pieces",
                 "f": "1/t", "a": 2, "b": 4, "n": 4, "expect": {"rsSum": "319/420", "rsExact": "≈ 0.693147 (rounded)"}},
            ],
            "panel_title": "Sum one over t and read the rounded total",
            "panel_intro": "The sum tile is an exact fraction for the rule chosen. The "
                           "exact-total tile is a rounded decimal with its label, since "
                           "the logarithm is not a fraction. Switch the rule to right ends "
                           "and to trapezoid, raise the pieces, and watch the sums close "
                           "in on the rounded figure.",
        }),
        "steps_title": "Bracketing the integral of 1/t",
        "steps_intro": "The method is the one of the earlier lessons in this course. What changes is the last move, because the answer is a rounded number.",
        "steps": [
            ("Check the interval avoids t = 0",
             "`1/t` has no value at `0`. The lab refuses a pole inside the interval, and "
             "so should you."),
            ("Choose the pieces and list the rates as fractions",
             "`h = (b − a)/n`; the left ends; then `1/t` at each, kept as a fraction."),
            ("Form the left and right sums",
             "Add the rates, multiply by `h`. For a falling rate the left sum is the "
             "larger. Their difference is `h·(f(a) − f(b))` in size, a check on both."),
            ("State the bracket",
             "Right sum `≤` total `≤` left sum, as exact fractions."),
            ("Quote the total rounded and labelled",
             "The total is `ln(b/a)`: print it with `≈`, say it is rounded, and never "
             "write it as a fraction or as a bare decimal."),
        ],
        "worked": {
            "title": "The integral of 1/t from 1 to 2, bracketed",
            "intro": [
                "Compute the left, right and trapezoid sums of `1/t` on the interval from "
                "`1` to `2` with four pieces, and place `ln 2` among them.",
            ],
            "lines": [
                "n = 4,  h = 1/4",
                "rates at left ends:  1, 4/5, 2/3, 4/7",
                "L₄ = (1/4)·(319/105) = 319/420",
                "R₄ = L₄ − h·(f(1) − f(2)) = 319/420 − 1/8 = 533/840",
                "T₄ = (319/420 + 533/840)/2 = 1171/1680",
                "rounded: L₄ ≈ 0.759524, R₄ ≈ 0.634524, T₄ ≈ 0.697024",
                "ln 2 ≈ 0.693147, between R₄ and L₄",
            ],
            "after": [
                "The window is `1/8` wide, and the target is nearer the trapezoid sum than "
                "either end. Nothing in the sums, however fine, makes the target a "
                "fraction; the lab keeps it as a labelled decimal for that reason.",
                "For a rehearsal, take the ln3 preset, which runs from `1` to `3`. The "
                "supplied first move is that the left ends are `1, 3/2, 2, 5/2`. You "
                "should find `L₄ = 77/60` and `R₄ = 19/20`, around `ln 3 ≈ 1.09861`.",
            ],
        },
        "quiz_title": "Sums that bracket a logarithm",
        "quiz": [
            {"q": "Why does reversing the power rule give no antiderivative of `1/t`?",
             "a": ["Because 1/t is not defined for any t",
                   "Because the rule would raise t⁻¹ to t⁰ and divide by 0",
                   "Because 1/t is a falling rate",
                   "Because the sums of 1/t are not exact fractions"],
             "c": 1,
             "why": "`1/t = t⁻¹`, and the rule gives `t⁰/0`. `1/t` is defined for every "
                    "`t` except `0`. Falling rates, like `4 − t`, are integrated by the "
                    "power rule with no trouble. And the sums of `1/t` are exact "
                    "fractions, as the lab shows."},
            {"q": "On the interval from `1` to `2` with four pieces, `L₄ = 319/420` and `R₄ = 533/840`. Which statement is justified?",
             "a": ["The total is 533/840, the smaller sum",
                   "The total is 319/420, since the left sum is exact",
                   "The total is the average of the two, 1171/1680",
                   "The total lies between 533/840 and 319/420, because the rate falls"],
             "c": 3,
             "why": "A falling rate puts the total between the two sums, the right one "
                    "lower. Neither sum is the total. The average is the trapezoid sum "
                    "`T₄`, which is a third estimate, about `0.697024`, close to the "
                    "target `≈ 0.693147` and not equal to it."},
            {"q": "Which of these is a claim the lab demonstrates and does not prove?",
             "a": ["R₄ = 533/840 for 1/t on [1, 2]",
                   "L₄ is larger than R₄ for 1/t",
                   "The sums of 1/t on [1, 2] approach ln 2",
                   "R₄ = L₄ − 1/8"],
             "c": 2,
             "why": "The first, second and fourth are exact computations that can be "
                    "checked by hand, and the gap formula of “Left and Right Sums” "
                    "gives the last. That the sums approach a limit, and that the limit "
                    "is `ln 2`, goes past any table."},
            {"q": "The left sum of `1/t` on the interval from `1` to `2` with four pieces is `319/420`. What is the left sum on the interval from `2` to `4` with four pieces?",
             "a": ["319/840", "319/210", "533/840", "319/420"],
             "c": 3,
             "why": "Doubling both ends doubles the width and halves each rate, so every "
                    "piece contributes the same product and the sum is unchanged: "
                    "`319/420`. `319/840` and `319/210` halve or double it, as if only "
                    "one of the two changes had been counted. `533/840` is the right "
                    "sum on `1` to `2`."},
        ],
        "mistakes": [
            ("Applying the power rule to 1/t and writing t⁰/0",
             "The rule sends `tⁿ` to `tⁿ⁺¹/(n + 1)`, and for `n = −1` the denominator "
             "is `0`. The expression has no value, so it names no function. The honest "
             "response is the one the lab takes: sum the rate, bracket the total, and "
             "report that it is the number written `ln 2`."),
            ("Writing the rounded total as if it were exact",
             "`0.693147` is not `ln 2`; it is `ln 2` rounded to six figures, and "
             "`693147/1000000` is not `ln 2` either. The lab prints `≈ 0.693147` with "
             "the label “rounded”, and the sentence that quotes it should keep the "
             "`≈`."),
            ("Concluding that the total is a fraction because every sum is",
             "Each of `319/420`, `52279/72072` and the rest is an exact fraction, and "
             "each is a sum, not the total. A list of fractions can close in on a "
             "number that is none of them, which is what happens here; the "
             "total is the number they approach, not one of them."),
        ],
        "standard": ("Finish when you can bracket the integral of 1/t with exact sums and report it rounded and labelled.",
                     "You should be able to say why the reversed power rule fails for "
                     "`1/t`, compute the left, right and trapezoid sums of `1/t` on an "
                     "interval as exact fractions, bracket the total, quote it with `≈` "
                     "and a rounding label, and state the claim `∫₁ˣ dt/t = ln x` as a "
                     "claim."),
        "note": "That ends the calculus the Subject needs: a rate can be differentiated and totalled, and the totals are exact whenever a polynomial is involved, with `1/t` bracketed and named. The next course, Differential Equations and Euler's Method, turns the question around and asks for a quantity given only a rule for its rate.",
    },
]
