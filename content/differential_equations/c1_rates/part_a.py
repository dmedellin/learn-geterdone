"""Rates of Change and the Derivative -- the first half.

The average rate as an exact difference quotient, the quotient of a polynomial
as a polynomial in the step, what a column of halving steps heads for, the
derivative at a point with its tangent line, the derivative of 1/t, and the
derivative as a function.

Every figure below is read off the calckit labs -- scripts/mathpath/labs/
calckit.py -- with scripts/labcheck.js --observe and pinned in each preset's
expect, rather than asserted here. The derivative is never taken as a limit
anyone has to believe: for a polynomial it is the constant term of the
quotient, and elsewhere it is a column of exact fractions and a stated claim.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "average-rate-of-change",
        "title": "Average Rate of Change",
        "module": "Average rates",
        "one_line": "The average rate over a step is a difference divided by the step, an exact fraction that is the slope of a secant.",
        "summary": (
            "How fast something changed between two moments is a subtraction followed by a "
            "division: the change in the output over the change in the input. Done exactly it "
            "is a fraction, and it is the slope of the straight line through two points of the "
            "graph. What the fraction depends on is the step `h` as well as the place, and "
            "that dependence is the whole subject of this course."
        ),
        "key": [
            "rate = (f(a + h) − f(a))/h",
            "change in output, over change in input",
            "the slope of the secant through two points",
            "a line: the same rate for every h",
            "t² at 1: the rate is 2 + h",
        ],
        "key_label": "The average rate of change over [a, a + h]",
        "concepts_intro": (
            "Three ideas. The first is the formula, the second is the picture, and the third is "
            "the one the rest of the course is built on."
        ),
        "concepts": [
            ("The rate is a difference over a difference",
             "Between `t = a` and `t = a + h` the input changes by `h` and the output changes by "
             "`f(a + h) − f(a)`. The average rate is the second divided by the first. Both "
             "parts matter: the subtraction says how much the output moved, and the division "
             "says how much input it took to move it, which is what makes it a rate."),
            ("It is the slope of a secant",
             "Plot the points `(a, f(a))` and `(a + h, f(a + h))`. The straight line through "
             "them is a secant, and its slope is rise over run, which is exactly the quotient. "
             "So an average rate is a slope you could draw, and every fact about slopes from "
             "Algebra applies to it."),
            ("The rate depends on the step, not only on the place",
             "For a line the rate is the same whatever `h` is, which is what makes a line a "
             "line. For a curve it is not: a different `h` is a different secant with a "
             "different slope. A single point does not yet have a rate, only a family of them, "
             "one for each step. The next lessons ask what that family looks like."),
        ],
        "read_title": "A change in the output, divided by the change in the input",
        "read_intro": "The definition, a first computation, the picture it draws, and the case where the step does not matter.",
        "body": [
            ("def", ("Average rate of change",
                     "For a function `f`, a starting input `a` and a step `h ≠ 0`, the "
                     "<strong>average rate of change</strong> of `f` over `[a, a + h]` is "
                     "`(f(a + h) − f(a))/h`.",
                     "It is also called a <strong>difference quotient</strong>: a difference "
                     "in the numerator, divided by the step `h`.")),
            ("p", "The lab takes the function as text and the place and step as exact numbers "
                  "and prints the quotient as a fraction. Nothing is rounded: `f(a + h)` is "
                  "found by substituting a fraction into the function, and the subtraction "
                  "and division are done on fractions."),
            ("p", "Take `f(t) = t²` and start at `a = 1`. With `h = 1` the input goes from 1 "
                  "to 2 and the output from 1 to 4, so the rate is `(4 − 1)/1 = 3`. Halve the "
                  "step to `h = 1/2`: the output at `3/2` is `9/4`, the change is `9/4 − 1 = "
                  "5/4`, and dividing by `1/2` gives `5/2`. A third halving gives `9/4`."),
            ("math", [
                "f(t) = t²,  a = 1",
                "",
                "   h       f(1 + h)     f(1 + h) − 1     rate",
                "   1         4              3             3",
                "   1/2      9/4            5/4           5/2",
                "   1/4     25/16           9/16          9/4",
            ]),
            ("p", "The rates are not the same: 3, then `5/2`, then `9/4`. The function did not "
                  "change; the step did. Each number is the slope of a different secant "
                  "through the same point `(1, 1)`."),
            ("h3", "The pattern is already visible"),
            ("p", "Look at the three rates as `2 + 1`, `2 + 1/2`, `2 + 1/4`. Each is 2 plus "
                  "the step. That is not a coincidence of these three numbers; it can be "
                  "derived. The output at `1 + h` is `(1 + h)² = 1 + 2h + h²`, so the change "
                  "is `2h + h²`, and dividing by `h` gives `2 + h`. For this function at this "
                  "point the slope of the secant through `(1, 1)` and `(1 + h, (1 + h)²)` is "
                  "`2 + h`, for every nonzero `h`."),
            ("example", ("A cubic, at a bigger step",
                         "Let `f(t) = t³ − t` and start at `a = 2`. Then `f(2) = 6`, and with "
                         "`h = 1` the output at 3 is 24, so the rate is `(24 − 6)/1 = 18`.",
                         "With `h = 1/2` the output at `5/2` is `105/8`; the change is "
                         "`105/8 − 6 = 57/8`, and dividing by `1/2` gives `57/4`. The rate "
                         "fell from 18 to `57/4`, which is 14.25, as the step halved. The lab "
                         "continues the column and prints the last row as a single fraction.")),
            ("h3", "When the step does not matter"),
            ("p", "Try `f(t) = 3t + 1` at `a = 5`. The output at 5 is 16, and at `5 + h` it is "
                  "`16 + 3h`, so the change is `3h` and the quotient is 3. It is 3 for "
                  "`h = 1`, for `h = 1/2`, for every step the lab can take. A function whose "
                  "average rate does not depend on the step is exactly a line, and the rate is "
                  "its slope. A curve is the opposite case: its rate depends on the step, and "
                  "so its secants have different slopes."),
            ("p", "That is what makes the next question worth asking. If a curve has no single "
                  "rate over a step, is there a rate at a single place? The answer takes the "
                  "next several lessons, and every one of them starts from the quotient on "
                  "this page."),
        ],
        "lab": ("calckit", {
            "mode": "quotient",
            "show_limit": False,
            "preset": "square",
            "presets": [
                {"id": "square", "label": "t² at 1, four halvings", "f": "t^2", "a": 1, "h": 1,
                 "halvings": 4, "expect": {'qtFirst': '3', 'qtLast': '33/16'}},
                {"id": "cubic", "label": "t³ − t at 2, four halvings", "f": "t^3 - t", "a": 2, "h": 1,
                 "halvings": 4, "expect": {'qtFirst': '18', 'qtLast': '2913/256'}},
                {"id": "line", "label": "3t + 1 at 5, every rate is the slope", "f": "3t + 1", "a": 5, "h": 1,
                 "halvings": 4, "expect": {'qtFirst': '3', 'qtLast': '3'}},
            ],
            "panel_title": "The rate over a step, as an exact fraction",
            "panel_intro": "Type a function of t, a starting place and a step. Each row halves the "
                           "step and prints the change in the output divided by the step, as a "
                           "fraction. The red line is the secant for the smallest step. Try the "
                           "line preset and watch every rate stay the same.",
        }),
        "steps_title": "Computing an average rate by hand",
        "steps_intro": "Four moves, always in this order, so that the division is never forgotten.",
        "steps": [
            ("Evaluate at both ends",
             "Find `f(a)` and `f(a + h)` as exact numbers. Substitute the fraction for `t` and "
             "square, cube or multiply it out; leave nothing as a decimal."),
            ("Subtract, output end minus output start",
             "`f(a + h) − f(a)` is the change. Its sign is the direction: positive means the "
             "output rose, negative that it fell."),
            ("Divide by the step",
             "The step is `h`, the change in the input. A step of `1/2` is divided by as "
             "`1/2`, which doubles the change. This is the move that turns a change into a "
             "rate, and the one that is easiest to leave out."),
            ("Read it as a slope",
             "The fraction you have is the slope of the secant through `(a, f(a))` and "
             "`(a + h, f(a + h))`. If the answer does not look like a slope you could draw, "
             "recheck the evaluation."),
        ],
        "worked": {
            "title": "t² at 1, over three steps",
            "intro": [
                "The function is `f(t) = t²` and the start is `a = 1`, so `f(1) = 1`. Three "
                "steps, each halving the last, each done with fractions.",
            ],
            "lines": [
                "h = 1:    f(2) = 4          (4 − 1)/1 = 3",
                "h = 1/2:  f(3/2) = 9/4      (9/4 − 1)/(1/2) = (5/4)·2 = 5/2",
                "h = 1/4:  f(5/4) = 25/16    (25/16 − 1)/(1/4) = (9/16)·4 = 9/4",
                "",
                "in general: ((1 + h)² − 1)/h = (2h + h²)/h = 2 + h",
            ],
            "after": [
                "The three rates, 3 and `5/2` and `9/4`, are 2 plus the step in each case, "
                "and the general line says why. The slope of the secant through `(1, 1)` and "
                "`(1 + h, (1 + h)²)` is `2 + h`.",
                "For a rehearsal, take `f(t) = t²` at `a = 2`. Work out the rate for "
                "`h = 1` by hand, then the general quotient `((2 + h)² − 4)/h`, and compare "
                "it with what the lab prints for the same function.",
            ],
        },
        "quiz_title": "Rates, steps and secants",
        "quiz": [
            {"q": "For `f(t) = t²`, what is the average rate of change over `[1, 3]`?",
             "a": ["2", "4", "8", "9/2"],
             "c": 1,
             "why": "The change is `f(3) − f(1) = 9 − 1 = 8` and the step is `2`, so the rate is "
                    "`8/2 = 4`. The answer 8 is the change with the division forgotten, and "
                    "`9/2` divides `f(3)` by the step without subtracting `f(1)`. The answer 2 "
                    "is the step itself."},
            {"q": "What is the average rate of `f(t) = 3t + 1` over `[5, 5 + h]`?",
             "a": ["3 for every nonzero h", "3 + h", "(16 + 3h)/h", "3 only when h = 1"],
             "c": 0,
             "why": "The output at `5 + h` is `16 + 3h`, so the change is `3h`, and dividing "
                    "by `h` gives 3, whatever `h` is. The slope of a line is its rate over "
                    "every step. The answer `3 + h` belongs to a curve, and `(16 + 3h)/h` is "
                    "`f(5 + h)/h`, which has no subtraction in it."},
            {"q": "For `f(t) = t²` at `a = 1`, which step gives the average rate `9/4`?",
             "a": ["h = 1/2", "h = 1", "h = 1/8", "h = 1/4"],
             "c": 3,
             "why": "The rate is `2 + h`, so `2 + h = 9/4` gives `h = 1/4`. A step of `1/2` "
                    "gives `5/2`, a step of 1 gives 3, and a step of `1/8` gives `17/8`."},
            {"q": "On the graph of `f`, the average rate over `[a, a + h]` is the slope of which line?",
             "a": ["The line through `(a, f(a))` and `(a + h, f(a + h))`",
                   "The line through the origin and `(a + h, f(a + h))`",
                   "The horizontal line at height `f(a)`",
                   "The line that touches the graph at only one point"],
             "c": 0,
             "why": "Rise over run between those two points is the quotient. The line through the "
                    "origin has slope `f(a + h)/(a + h)`, a different quantity, and the horizontal "
                    "line has slope 0. A line touching at one point is a tangent, which is a "
                    "later lesson, and a secant meets the graph at both of its points."},
        ],
        "mistakes": [
            ("Dividing nothing, or dividing the wrong thing",
             "The average rate is not `f(a + h)/h`, and it is not `f(a + h) − f(a)` with the "
             "division left out. For `t²` at 1 with `h = 1/2` the first gives `(9/4)/(1/2) = "
             "9/2` and the second gives `5/4`; the rate is `5/2`. The two errors are "
             "different, and neither is a slope: the subtraction takes out the starting value "
             "and the division by `h` makes the number a rate."),
            ("Treating the rate as a property of the function alone",
             "For a curve there is no single average rate. `t²` at 1 has the rate 3 over a step "
             "of 1, and `5/2` over a step of `1/2`. Always say which interval the rate belongs "
             "to, and expect that changing the step changes the answer."),
            ("Reading a negative rate as an error",
             "A negative quotient means the output fell over the interval. The sign is "
             "information, and a function that drops has negative secant slopes just as a "
             "falling line has a negative slope."),
        ],
        "standard": ("Finish when you can compute the average rate of change of a function over a stated interval as an exact fraction and say which line has that slope.",
                     "You should be able to evaluate `f(a)` and `f(a + h)` as fractions, "
                     "subtract and divide without dropping the division, draw or describe the "
                     "secant, and say what changes when `h` does."),
        "note": "A table of rates for halving steps shows something: the numbers are not "
                "scattered. For `t²` at 1 they are 2 plus the step each time. The next lesson "
                "does the algebra that makes this a rule for every polynomial, in "
                "&ldquo;The Difference Quotient as a Polynomial in h&rdquo;.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-quotient-as-a-polynomial-in-h",
        "title": "The Difference Quotient as a Polynomial in h",
        "module": "Average rates",
        "one_line": "For a polynomial the quotient simplifies to another polynomial in h, and the part that does not contain h is the number the next lessons call the rate at the place.",
        "summary": (
            "When the function is a polynomial, the difference quotient can be simplified by "
            "algebra alone. Expand `p(t + h)`, subtract `p(t)`, and every surviving term has a "
            "factor `h`, so dividing by `h` leaves a polynomial in `h`. Its constant term, the "
            "part that does not contain `h`, is what the next lessons call the rate at `t`. "
            "No limit is taken; the cancelling is exact."
        ),
        "key": [
            "(p(t + h) − p(t))/h, expanded and cancelled",
            "every term of the numerator has a factor h",
            "what is left is a polynomial in h",
            "t²: 2t + h     t³: 3t² + 3t·h + h²",
            "its h-free part: 2t, 3t²",
        ],
        "key_label": "The quotient of a polynomial, simplified",
        "concepts_intro": (
            "Three ideas: why the `h` cancels, what is left, and the order of operations "
            "that stops it going wrong."
        ),
        "concepts": [
            ("The numerator always has a factor of h",
             "When you expand `p(t + h)`, the terms that contain no `h` add up to exactly "
             "`p(t)`: that is what it means to put `h = 0`. Subtracting `p(t)` removes them, "
             "so every term left has at least one `h`. That is why the division by `h` "
             "always comes out even for a polynomial, with nothing left over."),
            ("What remains is a polynomial in h",
             "After the division the result is a sum of terms in `h`, with coefficients that "
             "depend on `t`. For `t²` it is `2t + h`. For `t³` it is `3t² + 3t·h + h²`. The "
             "step has not been made small, and nothing has been dropped: this is an exact "
             "rewriting of the same quotient."),
            ("Cancel first, then read off the part without h",
             "The part that does not contain `h` is the constant term. It is `2t` for `t²` and "
             "`3t²` for `t³`. It is the value the quotient takes when `h` is replaced by 0 "
             "in the simplified form, which is safe because the division is already done. "
             "Doing it in the other order is dividing zero by zero."),
        ],
        "read_title": "Expand, subtract, divide, read",
        "read_intro": "One polynomial worked through completely, then the same moves on a quartic, and the order of operations that matters.",
        "body": [
            ("p", "&ldquo;Average Rate of Change&rdquo; found that the rate of `t²` at 1 was `2 + h`. That was one place. "
                  "Do the same computation at a general `t` and the answer is a formula in "
                  "`t` and `h` together."),
            ("math", [
                "p(t) = t²",
                "",
                "p(t + h) = t² + 2th + h²",
                "p(t + h) − p(t) = 2th + h²",
                "(p(t + h) − p(t))/h = 2t + h",
            ]),
            ("p", "At `t = 1` this is `2 + h`, the result of the previous lesson, and at "
                  "`t = 2` it is `4 + h`. One expansion has done every place at once. The "
                  "terms of `p(t + h)` that have no `h` are `t²` alone, which the subtraction "
                  "removes; every term that survives has an `h`, and the division by `h` "
                  "takes one of them away."),
            ("def", ("The quotient as a polynomial in h",
                     "For a polynomial `p`, the expression `(p(t + h) − p(t))/h`, after the "
                     "expansion, subtraction and cancellation, is a polynomial in `h` whose "
                     "coefficients are polynomials in `t`.",
                     "Its <strong>constant term</strong> is the coefficient of `h` to the "
                     "power 0: the part of the quotient that does not contain `h`.")),
            ("h3", "The cube"),
            ("p", "For `p(t) = t³` the expansion is `(t + h)³ = t³ + 3t²h + 3th² + h³`. "
                  "Subtracting `t³` removes the first term, and what is left is "
                  "`3t²h + 3th² + h³`. Each term has a factor `h`, and dividing by `h` "
                  "gives `3t² + 3th + h²`."),
            ("math", [
                "p(t) = t³",
                "",
                "p(t + h) − p(t) = 3t²h + 3th² + h³",
                "divide by h:       3t² + 3th + h²",
                "the part without h:  3t²",
            ]),
            ("p", "The constant term is `3t²`. The terms that contain `h` are `3th` and `h²`; "
                  "they are the part of the rate that depends on how big the step is, and the "
                  "constant term is the part that does not."),
            ("example", ("A quartic with two terms",
                         "Let `p(t) = t⁴ − 2t²`. The first term contributes "
                         "`4t³h + 6t²h² + 4th³ + h⁴` to the numerator, and the second "
                         "contributes `−2·(2th + h²)`, which is `−4th − 2h²`.",
                         "Dividing the whole numerator by `h` gives `4t³ + 6t²h + 4th² + h³ "
                         "− 4t − 2h`. The lab groups it by powers of `h`: the constant term "
                         "is `4t³ − 4t`, and the remaining terms all contain `h`.")),
            ("h3", "Why the order matters"),
            ("p", "The tempting shortcut is to put `h = 0` into the quotient straight away. "
                  "The numerator becomes `p(t) − p(t) = 0` and the denominator becomes 0, so "
                  "the quotient is `0/0`, which has no value. The simplified form is "
                  "different: after the `h` has been cancelled out of the numerator, "
                  "`2t + h` is a perfectly good polynomial and has a value at `h = 0`. The "
                  "step is allowed only after the cancelling, because the cancelling is what "
                  "removed the zero from the denominator."),
            ("p", "Read this way, the constant term is not a limit that has to be believed. "
                  "It is a coefficient, found by the same expanding and collecting that "
                  "Algebra's Polynomials and Factoring does. What it means as a rate, and "
                  "why it is the right thing to call the rate at `t`, is the question for the "
                  "next lesson."),
        ],
        "lab": ("calckit", {
            "mode": "hpoly",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "t² gives 2t + h", "kind": "single", "f": "t^2", "g": None,
                 "a": None, "expect": {'hpQ': '2t + h', 'hpConst': '2t'}},
                {"id": "cube", "label": "t³ gives 3t² + 3th + h²", "kind": "single", "f": "t^3", "g": None,
                 "a": None, "expect": {'hpQ': '3t² + 3th + h²', 'hpConst': '3t²'}},
                {"id": "quartic", "label": "t⁴ − 2t², two terms", "kind": "single", "f": "t^4 - 2t^2", "g": None,
                 "a": None, "expect": {'hpQ': '4t³ − 4t + 6t²h − 2h + 4th² + h³', 'hpConst': '4t³ − 4t'}},
            ],
            "panel_title": "The quotient as a polynomial in h",
            "panel_intro": "Type a polynomial in t. The lab expands p(t + h) − p(t), divides by "
                           "h exactly, and prints the quotient grouped by powers of h. The "
                           "constant term is the part with no h. Leave the place empty to keep "
                           "t symbolic.",
        }),
        "steps_title": "Simplifying a quotient",
        "steps_intro": "Four moves. The order is the point: the division comes before any step is made small.",
        "steps": [
            ("Expand p(t + h)",
             "Replace every `t` by `t + h` and multiply out. For a power use the binomial "
             "pattern: `(t + h)³` has coefficients 1, 3, 3, 1."),
            ("Subtract p(t)",
             "The terms with no `h` cancel, since they sum to `p(t)`. Check that every term "
             "left has an `h`; if one does not, the expansion has an error."),
            ("Divide each term by h",
             "Do it term by term. Each `h` becomes 1, each `h²` becomes `h`, and so on. The "
             "result is a polynomial in `h`."),
            ("Read off the constant term",
             "Collect the terms that contain no `h`. That coefficient, a polynomial in `t`, is "
             "the part of the rate that does not depend on the step."),
        ],
        "worked": {
            "title": "The cube, term by term",
            "intro": [
                "The polynomial is `p(t) = t³`. The expansion is the binomial pattern, and "
                "each line is exact.",
            ],
            "lines": [
                "p(t + h) = t³ + 3t²h + 3th² + h³",
                "p(t + h) − p(t) = 3t²h + 3th² + h³",
                "divide by h:  3t² + 3th + h²",
                "",
                "constant term in h:  3t²",
                "check at t = 1, h = 1/4:  3 + 3/4 + 1/16 = 61/16",
            ],
            "after": [
                "The check at the end agrees with the quotient computed the long way. The "
                "output at `5/4` is `125/64`, the change from `t³ = 1` is `61/64`, and dividing "
                "by `1/4` gives `61/16`.",
                "For a rehearsal, repeat this for `p(t) = t⁴`, whose expansion has the "
                "coefficients 1, 4, 6, 4, 1. The constant term is `4t³`. The pattern across "
                "`t²`, `t³` and `t⁴` is that the constant term is the exponent times the "
                "power one lower, and the lesson on the derivative as a function uses it.",
            ],
        },
        "quiz_title": "Cancelling the h",
        "quiz": [
            {"q": "What is the simplified difference quotient of `p(t) = t²`?",
             "a": ["2t", "2t + h", "t + h", "2th + h²"],
             "c": 1,
             "why": "`(t + h)² − t² = 2th + h²`, and dividing by `h` gives `2t + h`. The "
                    "expression `2th + h²` is the numerator before the division, `2t` is the "
                    "part of the answer with no `h`, and `t + h` has the wrong coefficient."},
            {"q": "In `3t² + 3th + h²`, which part is the constant term in h?",
             "a": ["3t² + 3th", "h²", "3t²", "3th + h²"],
             "c": 2,
             "why": "The constant term is the part with no `h`: `3t²`. The other terms, `3th` "
                    "and `h²`, each contain `h` and change when the step does."},
            {"q": "Why is it wrong to put `h = 0` into `(p(t + h) − p(t))/h` before simplifying?",
             "a": ["It gives p(t) divided by 0",
                   "It gives the right answer but takes longer",
                   "It makes the polynomial constant",
                   "It gives 0 divided by 0, which has no value"],
             "c": 3,
             "why": "At `h = 0` the numerator is `p(t) − p(t) = 0` and the denominator is 0, so "
                    "the quotient is `0/0`. The simplified form has no division, which is why "
                    "it can be evaluated at `h = 0`. The first choice would be a different "
                    "mistake, and the last two are not what happens."},
        ],
        "mistakes": [
            ("Setting h to zero before dividing",
             "The quotient `(p(t + h) − p(t))/h` is undefined at `h = 0`: both the numerator "
             "and the denominator are zero. The constant term is found by cancelling an `h` "
             "from the numerator first, and then reading the result. For `t²`, putting "
             "`h = 0` in the quotient gives `0/0`, and putting it in `2t + h` gives `2t`."),
            ("Dropping terms because h is small",
             "Nothing in this lesson drops a term. `3t² + 3th + h²` is exactly equal to the "
             "quotient for every `h`, and `3th` and `h²` are part of it. They are not the "
             "constant term, and that is all that distinguishes them."),
            ("Forgetting a term of the expansion",
             "The most common slip is `(t + h)³ = t³ + h³`. The middle terms `3t²h` and "
             "`3th²` are what make the answer `3t²` and not 0. Check by putting in numbers: "
             "`(1 + 1)³ = 8`, not `1 + 1 = 2`."),
        ],
        "standard": ("Finish when you can expand a polynomial's difference quotient, cancel the h, and name its constant term.",
                     "You should be able to expand `p(t + h)`, subtract `p(t)`, divide by `h` "
                     "and write the result as a polynomial in `h`, say why the division comes "
                     "out even, and say why the order of the steps is not optional."),
        "note": "The constant term is a number once a place is chosen: `2` at `t = 1` for "
                "`t²`. Whether that number is the rate at the place, in the sense of a "
                "column of average rates heading somewhere, is checked next in &ldquo;What "
                "the Quotients Approach&rdquo;.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "what-the-quotients-approach",
        "title": "What the Quotients Approach",
        "module": "The derivative at a point",
        "one_line": "Halve the step and the exact quotients head for one number; the lesson states that as a claim, and the table is its evidence.",
        "summary": (
            "A column of exact quotients for halving steps gets closer to one number, and the "
            "gap to it shrinks with the step. That number is what the rate at the place "
            "means. The claim is about every step, not the rows on the page, and no row of a "
            "table is ever equal to the number it heads for. For a polynomial the claim is "
            "backed by the algebra of the previous lesson."
        ),
        "key": [
            "halve h: 3, 5/2, 9/4, 17/8, 33/16 …",
            "the gap to 2 is 1, 1/2, 1/4, 1/8 …",
            "the quotients approach 2",
            "no row equals 2; the claim covers every h",
            "t² at 1: quotient 2 + h, gap exactly h",
        ],
        "key_label": "What a column of quotients heads for",
        "concepts_intro": (
            "Three ideas: the column, the gap, and what the word “approach” does and does "
            "not say."
        ),
        "concepts": [
            ("The column of quotients",
             "Fix a function and a place `a`. Start with a step `h`, then halve it again and "
             "again, and write the exact quotient for each. For `t²` at 1 the column is 3, "
             "`5/2`, `9/4`, `17/8`, `33/16`, `65/32`, `129/64`. The lab prints each as a "
             "fraction, so there is no rounding to blame for what the column does."),
            ("The gap shrinks",
             "Subtract the number the column heads for from each row, and look at the size. "
             "Here the number is 2, and the gaps are `1, 1/2, 1/4, 1/8, …`: each is exactly "
             "the step, because the quotient is `2 + h`. As the step is halved the gap is "
             "halved, and it can be made smaller than any bound you name by halving enough "
             "times."),
            ("“Approach” is a claim about every step",
             "The statement “the quotients approach 2” says that for every positive "
             "bound there is a step below which every quotient is within the bound of 2. "
             "A table of seven rows cannot say that. It shows seven cases and the pattern "
             "behind them; the claim is about all of them. Nor is any row equal to 2: the "
             "gap is `h`, never zero."),
        ],
        "read_title": "A column of fractions, a number, and a claim",
        "read_intro": "The table, the gap, the claim stated carefully, and the polynomial case where the claim is also algebra.",
        "body": [
            ("p", "Take `f(t) = t²` at `a = 1` and halve the step from `h = 1` six times. "
                  "The lab computes each quotient exactly."),
            ("math", [
                "f(t) = t²,  a = 1",
                "",
                "   h       quotient     gap to 2",
                "   1          3            1",
                "   1/2       5/2          1/2",
                "   1/4       9/4          1/4",
                "   1/8      17/8          1/8",
                "   1/16     33/16         1/16",
                "   1/32     65/32         1/32",
                "   1/64    129/64         1/64",
            ]),
            ("p", "The quotients fall, 3 down to `129/64`, which is 2.015625 exactly. "
                  "The gap column is the step column, exactly: the quotient is `2 + h`, as "
                  "the previous lesson found by algebra, so subtracting 2 leaves `h`."),
            ("thm", ("What the quotients approach",
                     "For `f(t) = t²` at `a = 1`, the exact quotients `(f(1 + h) − f(1))/h` "
                     "<em>approach</em> 2 as `h → 0`: name any positive bound, and there is "
                     "a step below which every quotient is within that bound of 2. When the "
                     "quotients of a function at a place approach one number in this sense, "
                     "that number is the rate of the function at the place. The lab's tile "
                     "labels it `f′(a)`, and the next lesson takes it as the definition of "
                     "the derivative.",)),
            ("p", "The word “approach” has a precise sense, and it is not “reach”. "
                  "No row of the table equals 2. The last row is `129/64`, and the next "
                  "would be `257/128`; there is always a row after it and always a gap. "
                  "What the claim says is that the gap can be made as small as desired by "
                  "taking the step small enough, and that is a statement about every "
                  "step, not about the seven that happen to be printed."),
            ("h3", "Evidence and proof are different things"),
            ("p", "For this function the claim has a proof, and it is the algebra of the "
                  "last lesson. The quotient is `2 + h` for every nonzero `h`, so the gap to "
                  "2 is `h` in absolute value, which is less than any bound once `h` is. "
                  "The table illustrates that; the algebra is what establishes it. For "
                  "a function whose quotient does not simplify, the table is the evidence "
                  "and the lesson states the claim, and later lessons say so where it "
                  "applies."),
            ("example", ("The cube at 1",
                         "For `f(t) = t³` at `a = 1` the quotient is `3 + 3h + h²`, from the "
                         "expansion of `(1 + h)³`. At `h = 1` it is 7, and at `h = 1/64` it "
                         "is `12481/4096`.",
                         "The gap to 3 is `3h + h²`, which for `h = 1/64` is `193/4096`. "
                         "Halving the step slightly more than halves the gap, because of the "
                         "`h²` term, so the lab's gap column falls by a bit more than half "
                         "each time. The column heads for 3.")),
            ("example", ("A flat place",
                         "For `f(t) = t²` at `a = 0` the quotient is `((0 + h)² − 0)/h = h`. "
                         "The column is `1, 1/2, 1/4, …`, and it heads for 0.",
                         "The rate at 0 is 0, which is what the graph of `t²` looks like "
                         "there: the bottom of the bowl, neither rising nor falling. Here "
                         "the gap to the limit is the quotient itself.")),
            ("p", "Written with an arrow, the claim for the first example is "
                  "`(f(1 + h) − f(1))/h → 2` as `h → 0`. The arrow reads as “goes to”, and "
                  "it carries all the care of the paragraphs above. The next lesson gives "
                  "the number its name at a point, and attaches a line to it."),
        ],
        "lab": ("calckit", {
            "mode": "quotient",
            "show_limit": True,
            "preset": "square",
            "presets": [
                {"id": "square", "label": "t² at 1, six halvings", "f": "t^2", "a": 1, "h": 1,
                 "halvings": 6, "expect": {'qtLast': '129/64', 'qtGap': '1/64', 'qtLimit': '2'}},
                {"id": "cube", "label": "t³ at 1, six halvings", "f": "t^3", "a": 1, "h": 1,
                 "halvings": 6, "expect": {'qtLast': '12481/4096', 'qtGap': '193/4096', 'qtLimit': '3'}},
                {"id": "flat", "label": "t² at 0, every quotient is h", "f": "t^2", "a": 0, "h": 1,
                 "halvings": 6, "expect": {'qtLast': '1/64', 'qtGap': '1/64', 'qtLimit': '0'}},
            ],
            "panel_title": "Halve the step and watch the gap",
            "panel_intro": "Each row halves the step. The last tile shows the number the column "
                           "heads for, and the gap tile is the distance from the last row to it. "
                           "Raise the number of halvings and the gap shrinks without ever "
                           "reaching zero. The green line is the tangent.",
        }),
        "steps_title": "Reading a column of quotients",
        "steps_intro": "Four questions, asked of a table before it is trusted.",
        "steps": [
            ("Write the quotient for each step",
             "Halve the step each time and compute the exact quotient, as a fraction. Keep "
             "every row; a pattern can only be seen in a column."),
            ("Guess the number it heads for",
             "Look at where the fractions are settling. For `3, 5/2, 9/4, 17/8` it is 2. If "
             "you cannot see it, simplify the quotient by algebra first."),
            ("Compute the gaps",
             "Subtract the guess from each row. If the gaps shrink with the step, the guess "
             "is consistent with the table."),
            ("State the claim, and say what backs it",
             "Say that the quotients approach the number as `h → 0`. Then say whether "
             "algebra backs the claim, as it does for a polynomial, or whether the table is "
             "the only evidence."),
        ],
        "worked": {
            "title": "The gaps for t² at 1",
            "intro": [
                "The quotient is `2 + h`, so the gap to 2 is exactly the step. Seven rows, "
                "every one a fraction.",
            ],
            "lines": [
                "h = 1:     3        gap 1",
                "h = 1/2:   5/2      gap 1/2",
                "h = 1/4:   9/4      gap 1/4",
                "h = 1/8:   17/8     gap 1/8",
                "h = 1/16:  33/16    gap 1/16",
                "h = 1/32:  65/32    gap 1/32",
                "h = 1/64:  129/64   gap 1/64",
            ],
            "after": [
                "Each gap is half the one above it, and none is zero. The table shows seven "
                "rows, and the claim is about every `h`, including the ones the table "
                "never reaches.",
                "For a rehearsal, repeat this for `t²` at 2, where the quotient is `4 + h`. "
                "Write the gaps to 4 before you look, then check them in the lab.",
            ],
        },
        "quiz_title": "Approaching, not reaching",
        "quiz": [
            {"q": "For `t²` at 1 the quotients are `2 + h`. What does “the quotients approach 2” claim?",
             "a": ["Some row of the table is exactly 2",
                   "The last row of the table is as close to 2 as any quotient can be",
                   "Taking the step small enough puts the quotient as near 2 as you choose",
                   "The quotient is 2 when h is 0"],
             "c": 2,
             "why": "The claim is about every step: the gap `h` can be made smaller than any "
                    "bound by taking `h` smaller. No row is 2, since the gap is `h` and never "
                    "zero. The last row is not the nearest possible, since a smaller step "
                    "gives a nearer quotient. At `h = 0` the quotient is `0/0`, and has no "
                    "value."},
            {"q": "For `t³` at 1 the quotient is `3 + 3h + h²`. What number do the quotients approach?",
             "a": ["1", "3", "7", "12481/4096"],
             "c": 1,
             "why": "As `h` shrinks, `3h + h²` shrinks, and the quotient heads for 3. The value "
                    "7 is the first row, at `h = 1`, and `12481/4096` is the row for "
                    "`h = 1/64`, which is above 3 and is not the number approached. The "
                    "value 1 is `f(1)`."},
            {"q": "For `t²` at 0 the quotient is `h`. What does the column heading for 0 tell you about the graph at 0?",
             "a": ["It is neither rising nor falling there",
                   "It is rising steeply",
                   "It is falling",
                   "It has a gap in it"],
             "c": 0,
             "why": "A rate of 0 means the secant slopes level off to zero, which is the "
                    "bottom of the bowl. A steep rise would mean a large positive number, and "
                    "a fall a negative one. The graph of `t²` is unbroken."},
            {"q": "A table of seven quotients for halving steps heads for 2. Which statement is the claim about every step, and not just a fact about the rows?",
             "a": ["The seventh quotient is 129/64",
                   "Some quotient is exactly 2",
                   "The gap in the seventh row is 1/64",
                   "The quotients get within any bound of 2 once the step is small enough"],
             "c": 3,
             "why": "The first and third are facts about one particular row, and the second "
                    "is false, since the gap is `h` and never zero. Only the last is about "
                    "every step."},
        ],
        "mistakes": [
            ("Thinking the limit is the last row, or is reached at some step",
             "The last entry of a table is the quotient for the smallest step the table "
             "tried, not the number the column heads for. For `t²` at 1 the last row is "
             "`129/64`, the number approached is 2, and the gap `1/64` is not zero. A "
             "smaller step gives a nearer row, and no step gives 2 itself."),
            ("Reading a pattern in a few rows as a proof",
             "Seven fractions heading for 2 are evidence. For `t²` the algebra turns the "
             "evidence into a proof, because the quotient is exactly `2 + h`. For a function "
             "with no such simplification, the table remains evidence, and a lesson that "
             "relies on it should say so."),
            ("Expecting the gap to halve every time",
             "The gap halves for `t²` at 1 because the quotient is `2 + h`. For `t³` at 1 the "
             "gap is `3h + h²`, which falls to slightly less than half each time. How the gap "
             "shrinks depends on the function; that it shrinks is the claim."),
        ],
        "standard": ("Finish when you can produce the column of exact quotients for halving steps, state the number they approach, and say in one sentence what that claims and what the table shows.",
                     "You should be able to write the exact quotient for a polynomial at a "
                     "place, list the first several rows, compute the gaps, and say that "
                     "the claim covers every step while the table covers only the rows "
                     "shown."),
        "note": "The number the quotients approach at one place gets its definition next, "
                "and it comes with a line: "
                "&ldquo;The Derivative at a Point and the Tangent Line&rdquo;.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-derivative-at-a-point",
        "title": "The Derivative at a Point and the Tangent Line",
        "module": "The derivative at a point",
        "one_line": "The derivative at a point is the number the quotients approach, and the tangent line it defines estimates nearby values with an error you can write down exactly.",
        "summary": (
            "The number a column of quotients approaches at `a` is the derivative `f′(a)`. "
            "The line through `(a, f(a))` with that slope is the tangent line, "
            "`y = f(a) + f′(a)·(t − a)`. It is not a line that touches once and says "
            "nothing about the rest: it is the best straight-line estimate near `a`, and "
            "its error at `a + h` is a fraction the lab prints exactly."
        ),
        "key": [
            "f′(a) = what the quotients approach",
            "tangent: y = f(a) + f′(a)·(t − a)",
            "estimate at a + h: f(a) + f′(a)·h",
            "error = f(a + h) − estimate, exactly",
            "t² at 2, h = 1/10: error 1/100 = h²",
        ],
        "key_label": "The derivative at a point and its tangent line",
        "concepts_intro": (
            "Three ideas: the name for the number, the line it builds, and how far the line "
            "can be trusted."
        ),
        "concepts": [
            ("The derivative at a is the number the quotients approach",
             "Write `f′(a)` for it, read “f prime of a”. It is a single number for each "
             "place `a`, not a family. For `t²` at 2 the quotient is `4 + h`, the column "
             "heads for 4, and `f′(2) = 4`. That is a claim, as before, and for a "
             "polynomial it is backed by the constant term of the simplified quotient."),
            ("The tangent line is the line with that slope through the point",
             "It passes through `(a, f(a))` with slope `f′(a)`, so its equation is "
             "`y = f(a) + f′(a)·(t − a)`. For `t²` at 2 that is `y = 4 + 4·(t − 2) = 4t − 4`. "
             "It is the limit of the secant lines as the step shrinks, which is why its "
             "slope is the derivative."),
            ("Near a, the line estimates the function, and the error is computable",
             "At `t = a + h` the line gives `f(a) + f′(a)·h`, while the function gives "
             "`f(a + h)`. Their difference is the error of the linear approximation. For a "
             "polynomial it is an exact fraction, and it shrinks faster than `h` does, "
             "which is what makes the line useful."),
        ],
        "read_title": "A number, a line, and the error of using it",
        "read_intro": "The definition, the tangent line for a parabola, the exact error, and why “touches once” is the wrong picture.",
        "body": [
            ("def", ("The derivative at a point",
                     "The <strong>derivative</strong> of `f` at `a` is the number the "
                     "difference quotients `(f(a + h) − f(a))/h` approach as `h → 0`. It is "
                     "written `f′(a)`.",
                     "The <strong>tangent line</strong> to the graph of `f` at `a` is the line "
                     "through `(a, f(a))` with slope `f′(a)`: "
                     "`y = f(a) + f′(a)·(t − a)`.")),
            ("p", "Take `f(t) = t²` and `a = 2`. The quotient is `((2 + h)² − 4)/h = 4 + h`, "
                  "so the derivative is `f′(2) = 4`, the constant term. The point on the "
                  "graph is `(2, 4)`, and the tangent line is `y = 4 + 4·(t − 2)`, which "
                  "simplifies to `y = 4t − 4`."),
            ("h3", "Using the line to estimate"),
            ("p", "Move a tenth to the right, to `t = 21/10`. The line gives "
                  "`4·(21/10) − 4 = 22/5`, which is `440/100`. The function gives "
                  "`(21/10)² = 441/100`. The estimate is short by `1/100`."),
            ("math", [
                "f(t) = t²,  a = 2,  h = 1/10",
                "",
                "   f(2) = 4          f′(2) = 4",
                "   line at 21/10:    4 + 4·(1/10) = 22/5 = 440/100",
                "   function at 21/10:    441/100",
                "   error:                  1/100",
            ]),
            ("p", "The error is exactly `1/100`, which is `h²`. That is no accident for "
                  "this function. The function at `a + h` is `4 + 4h + h²` and the line is "
                  "`4 + 4h`, so the difference is the `h²` term that the line leaves out. "
                  "Halve the step to `1/20` and the error is `1/400`: a quarter of it, not a "
                  "half. The estimate gets better faster than the step gets smaller."),
            ("example", ("A cube at 1",
                         "For `f(t) = t³` at `a = 1` the quotient is `3 + 3h + h²`, so "
                         "`f′(1) = 3` and the tangent line is `y = 1 + 3·(t − 1) = 3t − 2`.",
                         "At `h = 1/10` the line gives `13/10` and the function gives "
                         "`1331/1000`. The error is `31/1000`, which is "
                         "`3h² + h³`: the terms of the expansion that the line leaves "
                         "out.")),
            ("example", ("A function that is not a polynomial",
                         "For `f(t) = 1/t` at `a = 1` the lab reports a slope of −1, "
                         "which the next lesson derives. The tangent line is "
                         "`y = 1 − (t − 1) = −t + 2`.",
                         "At `h = 1/2` the line gives `1/2` and the function gives `2/3`, "
                         "so the error is `1/6`. The line is too low here because `1/t` "
                         "bends upward away from its tangent.")),
            ("h3", "Touching is the wrong picture"),
            ("p", "A tangent is often described as a line that touches the graph at one "
                  "point. That is true of a circle and misleading here. The tangent line to "
                  "`t²` at 2 meets the parabola at `(2, 4)` and nowhere else, but that is "
                  "not what defines it. It is defined by the slope, and its usefulness is "
                  "in the nearby values it estimates: `22/5` against `441/100`, off by "
                  "`1/100`, at a point a tenth of a unit away."),
            ("p", "The error is always printed exactly in the lab, and for a "
                  "polynomial it is made of the terms of `f(a + h)` that contain `h²` or "
                  "more. That is why the estimate improves faster than the step shrinks, "
                  "and it is the whole reason a derivative is useful."),
        ],
        "lab": ("calckit", {
            "mode": "tangent",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "t² at 2, step 1/10", "f": "t^2", "a": 2, "h": "1/10", "expect": {'tgSlope': '4', 'tgLine': 'y = 4t − 4', 'tgApprox': '22/5', 'tgTrue': '441/100', 'tgError': '1/100'}},
                {"id": "cube", "label": "t³ at 1, step 1/10", "f": "t^3", "a": 1, "h": "1/10", "expect": {'tgSlope': '3', 'tgLine': 'y = 3t − 2', 'tgApprox': '13/10', 'tgTrue': '1331/1000', 'tgError': '31/1000'}},
                {"id": "recip", "label": "1/t at 1, step 1/2", "f": "1/t", "a": 1, "h": "1/2", "expect": {'tgSlope': '−1', 'tgLine': 'y = −t + 2', 'tgApprox': '1/2', 'tgTrue': '2/3', 'tgError': '1/6'}},
            ],
            "panel_title": "The tangent line and its exact error",
            "panel_intro": "Type a function, a place and a step. The lab prints the slope, the "
                           "tangent line, what the line estimates at a + h, the true value and "
                           "the error, all as exact fractions. Shrink the step and watch the "
                           "error fall faster than the step.",
        }),
        "steps_title": "From a quotient to a tangent line",
        "steps_intro": "Five moves. The first three find the derivative, the last two use it.",
        "steps": [
            ("Simplify the quotient at the place",
             "Expand and cancel the `h`, as in the polynomial lesson, with `a` in the place "
             "of `t`."),
            ("Read off the constant term",
             "It is `f′(a)`, the number the quotients approach."),
            ("Write the line",
             "`y = f(a) + f′(a)·(t − a)`: the point `(a, f(a))` and the slope `f′(a)`."),
            ("Estimate at a + h",
             "The line gives `f(a) + f′(a)·h`. Compute it as a single fraction."),
            ("Subtract to find the error",
             "True value minus estimate: `f(a + h) − (f(a) + f′(a)·h)`. A positive error "
             "means the line lies below the function there."),
        ],
        "worked": {
            "title": "t² at 2, a tenth to the right",
            "intro": [
                "The function is `f(t) = t²`, the place is `a = 2` and the step is "
                "`h = 1/10`. Each number is an exact fraction.",
            ],
            "lines": [
                "f(2) = 4",
                "quotient: ((2 + h)² − 4)/h = 4 + h,  so f′(2) = 4",
                "tangent line: y = 4 + 4·(t − 2) = 4t − 4",
                "",
                "line at 21/10:      4·(21/10) − 4 = 22/5 = 440/100",
                "function at 21/10:  (21/10)² = 441/100",
                "error:              441/100 − 440/100 = 1/100 = h²",
            ],
            "after": [
                "The line is a good estimate: it is within one part in 441 of the true value. "
                "The error is the `h²` term that the line leaves out.",
                "For a rehearsal, find the tangent to `t²` at 3 and use it at "
                "`t = 31/10`. The slope is 6, the estimate is `9 + 6/10 = 48/5`, and the "
                "error should again be `h²`.",
            ],
        },
        "quiz_title": "Slope, line and error",
        "quiz": [
            {"q": "For `f(t) = t²` at `a = 2`, what is the tangent line?",
             "a": ["y = 4t − 4", "y = 2t", "y = 4t + 4", "y = 4"],
             "c": 0,
             "why": "The slope is `f′(2) = 4` and the line passes through `(2, 4)`, so "
                    "`y = 4 + 4·(t − 2) = 4t − 4`. The line `y = 4t + 4` has the right slope "
                    "and passes through `(2, 12)`, and `y = 4` is horizontal. The line "
                    "`y = 2t` has the wrong slope."},
            {"q": "The tangent to `t²` at 2 estimates the value at `t = 21/10` as `22/5`. The true value is `441/100`. What is the error?",
             "a": ["1/100", "1/10", "1/5", "0"],
             "c": 0,
             "why": "`22/5 = 440/100`, and `441/100 − 440/100 = 1/100`. The step is `1/10`, and "
                    "the error is the square of it, so `1/10` is the step itself and not the "
                    "error."},
            {"q": "The step is halved from `1/10` to `1/20` in the tangent estimate of `t²` at 2. What happens to the error?",
             "a": ["It is halved, to 1/200",
                   "It is divided by four, to 1/400",
                   "It stays at 1/100",
                   "It doubles"],
             "c": 1,
             "why": "The error is `h²`, so a step of `1/20` gives `1/400`. Dividing by two "
                    "would be right if the error were proportional to `h`, which it is not."},
            {"q": "Which statement about the tangent line to `t²` at 2 is correct?",
             "a": ["It has slope equal to the average rate over every step",
                   "It is useless away from the single point where it touches",
                   "Its slope is the number the quotients at 2 approach",
                   "It lies exactly on the parabola near 2"],
             "c": 2,
             "why": "That is the definition. The average rate over a step `h` is `4 + h`, which "
                    "equals the slope only at `h = 0`. The line estimates well near 2, as "
                    "the error `h²` shows, and it is not on the parabola except at "
                    "`(2, 4)`."},
        ],
        "mistakes": [
            ("Thinking the tangent “touches at one point only”, so it says nothing about nearby values",
             "The tangent to `t²` at 2 meets the parabola only at `(2, 4)`, and yet at "
             "`t = 21/10` it estimates `22/5` against the true `441/100`, an error of "
             "`1/100`. Touching once is not the definition; the slope is, and the line is "
             "valuable because the error falls as `h²` while the step falls as `h`."),
            ("Using the tangent far from its point",
             "The error is exact and it grows: at `h = 1` the error for `t²` at 2 is 1, and at "
             "`h = 10` it is 100. The line is an estimate near `a`, and the error formula "
             "says how near."),
            ("Confusing the derivative with a value of the function",
             "`f′(2)` is the slope, 4, and `f(2)` is the height, also 4 here only by "
             "coincidence. For `t³` at 1 the slope is 3 and the height is 1. The tangent line "
             "uses both: the height as the starting point and the slope as the rate."),
        ],
        "standard": ("Finish when you can find f′(a) for a polynomial, write the tangent line, and compute the exact error of the estimate at a + h.",
                     "You should be able to simplify the quotient at a place, read the "
                     "derivative off as the constant term, write the line, evaluate it at "
                     "`a + h`, and subtract from the true value to get a fraction."),
        "note": "Every derivative so far came from a quotient that simplifies to a "
                "polynomial in `h`. One function does not do that, and it is worth "
                "doing by hand: &ldquo;The Derivative of 1/t&rdquo;.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-derivative-of-one-over-t",
        "title": "The Derivative of 1/t",
        "module": "The derivative at a point",
        "one_line": "The quotient of 1/t is found by combining two fractions, it simplifies to the exact fraction −1/(a(a + h)), and the derivative is −1/a².",
        "summary": (
            "`1/t` is not a polynomial, so its quotient cannot be expanded. It can still be "
            "simplified exactly, by putting `1/(a + h) − 1/a` over a common denominator. "
            "The `h` cancels, leaving `−1/(a(a + h))`, and as `h` shrinks the denominator "
            "heads for `a²`, so the derivative is `−1/a²`."
        ),
        "key": [
            "1/(a + h) − 1/a = −h/(a(a + h))",
            "the quotient: −1/(a(a + h))",
            "a = 2 gives −1/6, −1/5, −2/9, −4/17 → −1/4",
            "f′(a) = −1/a²",
            "negative, because 1/t falls",
        ],
        "key_label": "The derivative of 1/t",
        "concepts_intro": (
            "Three ideas: combining the fractions, cancelling, and reading the number off "
            "a formula and a column together."
        ),
        "concepts": [
            ("Put the difference over a common denominator",
             "`1/(a + h) − 1/a` is a subtraction of fractions, and a common denominator is "
             "`a(a + h)`. The numerator becomes `a − (a + h) = −h`, so the difference is "
             "`−h/(a(a + h))`. The `h` has been exposed as a factor of the numerator, which "
             "is the same event as in the polynomial case."),
            ("Cancel the h, and the quotient is a fraction in h",
             "Dividing by `h` leaves `−1/(a(a + h))`. This is not a polynomial in `h`, but "
             "it is exact, and it has a value at `h = 0` because the zero has been "
             "cancelled out of the denominator. The column of quotients is this fraction "
             "evaluated at `h = 1, 1/2, 1/4, …`."),
            ("The number it approaches is −1/a²",
             "As `h` shrinks, `a + h` heads for `a`, so the denominator `a(a + h)` heads for "
             "`a²` and the quotient for `−1/a²`. The column in the lab and the formula "
             "agree: at `a = 2` the column heads for `−1/4`. The sign is negative because "
             "`1/t` falls as `t` rises."),
        ],
        "read_title": "Two fractions, one subtraction, one cancelled h",
        "read_intro": "The algebra once in general, the column that confirms it, and why the answer cannot be positive or a logarithm.",
        "body": [
            ("p", "The function is `f(t) = 1/t`, so `f(a + h) = 1/(a + h)`. The quotient has "
                  "a fraction inside a fraction, and the way through is to subtract the two "
                  "fractions first."),
            ("math", [
                "f(a + h) − f(a) = 1/(a + h) − 1/a",
                "                = (a − (a + h)) / (a·(a + h))",
                "                = −h / (a·(a + h))",
                "",
                "divide by h:   −1 / (a·(a + h))",
            ]),
            ("p", "The `h` in the numerator is the whole point, as in the polynomial lesson: "
                  "once it is divided out, the quotient has no zero in its denominator. At "
                  "`a = 2` and `h = 1/4` the quotient is `−1/(2·(9/4)) = −2/9`, and the long "
                  "way gives the same: `1/(9/4) − 1/2 = 4/9 − 1/2 = −1/18`, and "
                  "dividing by `1/4` gives `−2/9`."),
            ("math", [
                "f(t) = 1/t,  a = 2",
                "",
                "   h       quotient −1/(2·(2 + h))",
                "   1             −1/6",
                "   1/2           −1/5",
                "   1/4           −2/9",
                "   1/8           −4/17",
                "   1/16          −8/33",
                "   1/32          −16/65",
            ]),
            ("p", "The column heads for `−1/4`. Each entry is `−1/(2·(2 + h))`, and the "
                  "denominator `2·(2 + h)` heads for `4`. The gaps from `−1/4` shrink as "
                  "the step does, and, as before, no row reaches `−1/4`."),
            ("thm", ("The derivative of 1/t",
                     "For every place `a ≠ 0`, the quotients of `f(t) = 1/t` are "
                     "`−1/(a(a + h))`, and they approach `−1/a²` as `h → 0`: "
                     "`f′(a) = −1/a²`.",)),
            ("proof", ["The quotient was derived exactly above, by algebra. What is left is "
                       "the claim that `−1/(a(a + h))` approaches `−1/a²` as `h` shrinks.",
                       "The denominator `a(a + h) = a² + a·h`, which differs from `a²` by "
                       "`a·h`, and that can be made as small as you like by taking `h` small. "
                       "So the quotient is as near `−1/a²` as you choose, and the lab's "
                       "column, which shows several steps, illustrates it. The "
                       "approach is the same claim as for a polynomial, and here it is "
                       "read off a formula instead of a constant term."]),
            ("h3", "Two other values of a"),
            ("p", "At `a = 1` the quotient is `−1/(1 + h)`, so the column is "
                  "`−1/2, −2/3, −4/5, −8/9, …`, and it heads for `−1`. At `a = 1/2` the "
                  "quotient is `−1/((1/2)·(1/2 + h))`, the column starts at `−4/3` and heads "
                  "for `−4`. Both agree with `−1/a²`: at `a = 1/2`, `a² = 1/4` and "
                  "`−1/(1/4) = −4`. The rate is steeper where `t` is smaller, which fits "
                  "the graph of `1/t`, falling fast near 0 and flattening out for large `t`."),
            ("p", "The tangent line from the last lesson uses this. At `a = 1` the slope is "
                  "`−1`, the point is `(1, 1)`, and the line is `y = −t + 2`."),
        ],
        "lab": ("calckit", {
            "mode": "quotient",
            "show_limit": True,
            "preset": "two",
            "presets": [
                {"id": "two", "label": "1/t at 2, five halvings", "f": "1/t", "a": 2, "h": 1,
                 "halvings": 5, "expect": {'qtFirst': '−1/6', 'qtLast': '−16/65', 'qtLimit': '−1/4'}},
                {"id": "one", "label": "1/t at 1, five halvings", "f": "1/t", "a": 1, "h": 1,
                 "halvings": 5, "expect": {'qtFirst': '−1/2', 'qtLast': '−32/33', 'qtLimit': '−1'}},
                {"id": "half", "label": "1/t at 1/2, five halvings", "f": "1/t", "a": "1/2", "h": 1,
                 "halvings": 5, "expect": {'qtFirst': '−4/3', 'qtLast': '−64/17', 'qtLimit': '−4'}},
            ],
            "panel_title": "The quotients of 1/t, exactly",
            "panel_intro": "The function is a rational function, so every quotient is a fraction. "
                           "Change the place and compare the number the column heads for with "
                           "minus one over the place squared. The place must not be zero.",
        }),
        "steps_title": "Differentiating 1/t by hand",
        "steps_intro": "The same four moves as the polynomial case, with fractions in place of an expansion.",
        "steps": [
            ("Write f(a + h) − f(a) as two fractions",
             "`1/(a + h) − 1/a`. Do not divide by `h` yet."),
            ("Combine over a common denominator",
             "The common denominator is `a(a + h)`. The numerator is `a − (a + h) = −h`."),
            ("Divide by h and cancel",
             "The `h` in the numerator cancels the `h` in the divisor, leaving "
             "`−1/(a(a + h))`."),
            ("Let the step shrink in the formula",
             "The denominator `a(a + h)` heads for `a²`, so the quotient heads for "
             "`−1/a²`. Check with a column: the fractions should agree."),
        ],
        "worked": {
            "title": "1/t at 2, one step by hand",
            "intro": [
                "The place is `a = 2` and the step is `h = 1/4`, so `a + h = 9/4`. Both "
                "routes are shown.",
            ],
            "lines": [
                "the long way:",
                "  1/(9/4) = 4/9",
                "  4/9 − 1/2 = 8/18 − 9/18 = −1/18",
                "  (−1/18)/(1/4) = −4/18 = −2/9",
                "",
                "the formula:  −1/(a·(a + h)) = −1/(2·(9/4)) = −2/9",
                "",
                "as h gets small,  a·(a + h) → 4,   quotient → −1/4",
            ],
            "after": [
                "Both routes give `−2/9`. The lab's column for `a = 2` has this value in "
                "its third row, and the rows after it head for `−1/4`, which is "
                "`−1/a²` at `a = 2`.",
                "For a rehearsal, find the derivative of `1/t` at `a = 3` from the formula, "
                "and check that the quotient at `h = 1` is `−1/12`.",
            ],
        },
        "quiz_title": "Fractions and the derivative of 1/t",
        "quiz": [
            {"q": "What is `1/(a + h) − 1/a` as a single fraction?",
             "a": ["−h/(a·(a + h))", "h/(a·(a + h))", "−h/a", "1/((a + h) − a)"],
             "c": 0,
             "why": "The common denominator is `a(a + h)` and the numerator is "
                    "`a − (a + h) = −h`. The positive version has the numerator the wrong way "
                    "round, `−h/a` has dropped a factor from the denominator, and "
                    "`1/((a + h) − a)` subtracts the denominators, which is not how "
                    "fractions are subtracted."},
            {"q": "What is the derivative of `1/t` at `a = 2`?",
             "a": ["1/4", "−1/2", "−1/4", "−1/6"],
             "c": 2,
             "why": "`f′(a) = −1/a²`, which at `a = 2` is `−1/4`. The value `−1/6` is the "
                    "quotient at `h = 1`, a step of the column and not where it heads. "
                    "Without the sign it would be the slope of a rising function."},
            {"q": "Why must the derivative of `1/t` at `a = 1` be negative?",
             "a": ["Because 1 is a small number",
                   "Because 1/t takes smaller values as t grows, so every secant slopes down",
                   "Because the formula has a minus sign in it, whatever the function does",
                   "Because the quotient is a fraction"],
             "c": 1,
             "why": "At 1 the function is 1, and at 2 it is `1/2`, so the average rate over "
                    "any step to the right is negative, and so is the number they approach. "
                    "The minus sign in the formula is a consequence, not a reason."},
            {"q": "The quotient for `1/t` at `a = 1/2` with `h = 1` is `−4/3`. What number does the column of halving steps head for?",
             "a": ["−1", "−4", "−1/4", "4"],
             "c": 1,
             "why": "`f′(1/2) = −1/(1/2)² = −4`. The value `−1` is the derivative at 1 and `−1/4` "
                    "is the derivative at 2. A positive 4 would need the function to be "
                    "rising."},
        ],
        "mistakes": [
            ("Taking the derivative of 1/t to be 1 or ln t",
             "At `a = 1` the quotients of `1/t` are `−1/2, −2/3, −4/5, …`, every one "
             "negative, because `1/t` falls from 1 to `1/2` as `t` goes from 1 to 2. "
             "No positive number can be where they head, so the derivative is not 1, "
             "and `ln t` rises, so its slope would be positive too. It is −1 at `a = 1`, "
             "and `−1/a²` in general."),
            ("Applying a polynomial rule to a fraction",
             "`1/t` is not `t` to a positive power, so the expansion of "
             "the polynomial lesson does not apply. The cancelling is of a different "
             "kind: the `h` appears when the two fractions are combined. Skipping the "
             "combination leaves a fraction over `h` with no visible factor to cancel."),
            ("Forgetting that a cannot be zero",
             "`1/t` has no value at 0, so there is no quotient and no derivative there, and "
             "`−1/a²` is undefined at `a = 0`. The lab refuses a place of 0, or a place "
             "where `a + h` lands on 0, instead of printing something."),
        ],
        "standard": ("Finish when you can derive the quotient of 1/t by combining fractions and state its derivative at a place.",
                     "You should be able to write `1/(a + h) − 1/a` as one fraction, cancel "
                     "the `h`, evaluate the result at a given step, and say what the column "
                     "of such quotients approaches."),
        "note": "Two kinds of function now have a derivative at every place: a polynomial "
                "and `1/t`. The next lesson stops computing one place at a time and treats "
                "the derivative as a function of its own, in &ldquo;The Derivative as a "
                "Function&rdquo;.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-derivative-as-a-function",
        "title": "The Derivative as a Function",
        "module": "The derivative as a function",
        "one_line": "Differentiate a polynomial term by term with the power rule, and read where its graph rises and falls from the sign of the result.",
        "summary": (
            "Each place has its own derivative, so the derivative is itself a function "
            "of `t`. For a polynomial it is found by the power rule: each term "
            "`c·tⁿ` becomes `n·c·tⁿ⁻¹`, and a constant term disappears. Where the "
            "result is positive the graph rises, where it is negative the graph falls, and "
            "where it is zero the graph is momentarily level."
        ),
        "key": [
            "(c·tⁿ)′ = n·c·tⁿ⁻¹",
            "a constant has derivative 0",
            "(p + q)′ = p′ + q′",
            "p′ > 0: rising    p′ < 0: falling",
            "t³ − 6t² + 9t has p′ = 3t² − 12t + 9",
        ],
        "key_label": "The derivative as a function, by the power rule",
        "concepts_intro": (
            "Three ideas: the rule, why it is allowed, and what the sign says about the "
            "graph."
        ),
        "concepts": [
            ("The derivative is a function of t",
             "Compute `f′(a)` for every `a` and you get a new function, `f′(t)`. For `t²` the "
             "constant term of the quotient is `2t`, so `(t²)′ = 2t`. For `t³` it is "
             "`3t²`. These are the same constant terms found in the polynomial lesson, "
             "now read as formulas."),
            ("The power rule: bring the exponent down",
             "The pattern is that `t²` has derivative `2t`, `t³` has `3t²` and `t⁴` has "
             "`4t³`: the derivative of `tⁿ` is `n·tⁿ⁻¹`. The reason is the expansion "
             "`(t + h)ⁿ = tⁿ + n·tⁿ⁻¹·h + (terms with h²)`, so the quotient is `n·tⁿ⁻¹` "
             "plus terms that each contain `h`. A constant `c` multiplies through, "
             "and a constant term has quotient `(c − c)/h = 0`."),
            ("The sign of p′ is the direction of the graph",
             "A positive derivative at `t` means the secant slopes there are positive, "
             "so the graph is rising. A negative one means it is falling. Where `p′` "
             "is zero the tangent is horizontal. Solving `p′ = 0` and testing the sign on "
             "each side of a zero reads the whole shape of the graph."),
        ],
        "read_title": "A rule, a reason, and a graph read from a sign",
        "read_intro": "The power rule with its proof, the sum and constant rules, one cubic read completely, and the three errors the rule invites.",
        "body": [
            ("thm", ("The power rule",
                     "For a whole number `n ≥ 1`, the derivative of `tⁿ` is `n·tⁿ⁻¹`. For a "
                     "constant `c`, the derivative of `c` is 0.",)),
            ("proof", ["Expand `(t + h)ⁿ` by multiplying `n` copies of `t + h` together. "
                       "Taking `t` from every copy gives `tⁿ`; taking `h` from one copy and "
                       "`t` from the other `n − 1` can be done in `n` ways, which gives "
                       "`n·tⁿ⁻¹·h`; every other choice takes `h` from at least two copies, "
                       "so every later term contains `h²`. For `n = 3` this is the "
                       "`t³ + 3t²h + 3th² + h³` of the polynomial lesson.",
                       "Subtracting `tⁿ` and dividing by `h` leaves `n·tⁿ⁻¹` plus terms that "
                       "each still contain `h`, so the constant term in `h` is `n·tⁿ⁻¹`. For "
                       "a constant `c` the numerator `c − c` is 0, so the quotient is "
                       "`(c − c)/h = 0` for every `h`."]),
            ("p", "Two more facts let the rule handle a whole polynomial. The quotient of a "
                  "sum is the sum of the quotients, because subtraction and division "
                  "distribute over a sum, so `(p + q)′ = p′ + q′`. And a constant factor "
                  "comes through unchanged: `(c·p)′ = c·p′`. Together they give "
                  "the rule for `c·tⁿ`: `n·c·tⁿ⁻¹`, term by term."),
            ("example", ("A cubic, term by term",
                         "`p(t) = t³ − 6t² + 9t`. The three terms give `3t²`, `−12t` and `9`, "
                         "so `p′(t) = 3t² − 12t + 9`.",
                         "Factor it: `3t² − 12t + 9 = 3(t² − 4t + 3) = 3(t − 1)(t − 3)`. The "
                         "zeros are at `t = 1` and `t = 3`.")),
            ("h3", "Reading the graph from the sign"),
            ("p", "The product `3(t − 1)(t − 3)` is positive when both brackets have the same "
                  "sign and negative when they differ. Test one point in each region: "
                  "at `t = 0` it is `3·(−1)·(−3) = 9`, positive; at `t = 2` it is "
                  "`3·1·(−1) = −3`, negative; at `t = 4` it is `3·3·1 = 9`, positive."),
            ("math", [
                "p′(t) = 3(t − 1)(t − 3)",
                "",
                "   t < 1         p′ > 0     rising",
                "   1 < t < 3     p′ < 0     falling",
                "   t > 3         p′ > 0     rising",
            ]),
            ("p", "That is what the graph of `t³ − 6t² + 9t` does: it rises to `t = 1`, where "
                  "`p = 4`, falls to `t = 3`, where `p = 0`, and rises again. The derivative "
                  "has told us the shape without plotting a point. The lab prints the "
                  "derivative, its rational zeros and the intervals of rising and falling."),
            ("h3", "Three errors the rule invites"),
            ("ul", ["Forgetting the coefficient: the derivative of `t³` is `3t²`, not `t²`.",
                    "Treating a constant as if it had a rate: the derivative of 5 is 0, not "
                    "1, and the derivative of `t + 5` is 1.",
                    "Differentiating the factors of a product separately: that is not "
                    "this rule, and a later lesson shows why not. Expand first."]),
        ],
        "lab": ("calckit", {
            "mode": "derivative",
            "order": 1,
            "preset": "hill",
            "presets": [
                {"id": "hill", "label": "t³ − 6t² + 9t, rises and falls", "f": "t^3 - 6t^2 + 9t",
                 "expect": {'dvDeriv': '3t² − 12t + 9', 'dvZeros': '1, 3', 'dvIntervals': 'rising t < 1; falling 1 < t < 3; rising t > 3'}},
                {"id": "bowl", "label": "t² − 4t, one turn", "f": "t^2 - 4t", "expect": {'dvDeriv': '2t − 4', 'dvZeros': '2', 'dvIntervals': 'falling t < 2; rising t > 2'}},
                {"id": "wave", "label": "t⁴ − 2t², two dips and a hump", "f": "t^4 - 2t^2", "expect": {'dvDeriv': '4t³ − 4t', 'dvZeros': '−1, 0, 1', 'dvIntervals': 'falling t < −1; rising −1 < t < 0; falling 0 < t < 1; rising t > 1'}},
            ],
            "panel_title": "Differentiate a polynomial and read its sign",
            "panel_intro": "Type a polynomial in t. The lab applies the power rule term by term, "
                           "finds the rational zeros of the derivative, and lists where the "
                           "polynomial rises and falls. The plot shows the polynomial and its "
                           "derivative together; the derivative crosses zero where the graph "
                           "turns.",
        }),
        "steps_title": "Differentiating and reading a polynomial",
        "steps_intro": "Five moves. The first two are mechanical, and the rest read the answer.",
        "steps": [
            ("Differentiate each term",
             "`c·tⁿ` becomes `n·c·tⁿ⁻¹`. A constant term goes. Do not skip the coefficient."),
            ("Add the results",
             "The derivative of the sum is the sum of the derivatives. Write it in order of "
             "descending powers."),
            ("Solve p′ = 0",
             "Factor, or use the quadratic formula for a quadratic. The zeros are where the "
             "tangent is horizontal."),
            ("Test the sign between the zeros",
             "Pick one point in each region and evaluate `p′`. Positive means rising, "
             "negative means falling."),
            ("Check against the plot",
             "The graph should turn at each zero where the sign changes. If it does "
             "not, recheck the coefficient of each term."),
        ],
        "worked": {
            "title": "A cubic, from rule to graph",
            "intro": [
                "The polynomial is `p(t) = t³ − 6t² + 9t`. The derivative, the factoring and "
                "the signs are each exact.",
            ],
            "lines": [
                "p(t)  = t³ − 6t² + 9t",
                "p′(t) = 3t² − 12t + 9 = 3(t − 1)(t − 3)",
                "",
                "zeros:   t = 1,  t = 3",
                "t = 0:   p′ =  9    rising",
                "t = 2:   p′ = −3    falling",
                "t = 4:   p′ =  9    rising",
                "",
                "p(1) = 4,   p(3) = 0",
            ],
            "after": [
                "The graph rises to a height of 4 at `t = 1`, falls to 0 at `t = 3`, and "
                "rises for ever after. Neither height was found by plotting.",
                "For a rehearsal, differentiate `t² − 4t`. The derivative is `2t − 4`, the "
                "zero is at 2, and the graph falls before it and rises after, which is a "
                "bowl.",
            ],
        },
        "quiz_title": "The power rule and the sign",
        "quiz": [
            {"q": "What is the derivative of `p(t) = t⁴ − 2t²`?",
             "a": ["4t³ − 2t", "t³ − 2t", "4t³ − 4t", "4t³ − 4t + 1"],
             "c": 2,
             "why": "The first term gives `4t³` and the second gives `2·2t = 4t`, so "
                    "`p′ = 4t³ − 4t`. The answer `4t³ − 2t` forgets the coefficient 2 on the second "
                    "term, `t³ − 2t` forgets the exponent on both, and the final `+ 1` would be "
                    "the derivative of a constant term, which this polynomial has not got; "
                    "a constant's derivative is 0 in any case."},
            {"q": "What is the derivative of the constant function `f(t) = 5`?",
             "a": ["5", "1", "0", "t"],
             "c": 2,
             "why": "Every quotient is `(5 − 5)/h = 0`, so the number they approach is 0. A "
                    "constant does not change, and its rate is zero."},
            {"q": "For `p(t) = t³ − 6t² + 9t`, what does the graph do between `t = 1` and `t = 3`?",
             "a": ["It rises", "It falls", "It is level", "It jumps"],
             "c": 1,
             "why": "`p′ = 3(t − 1)(t − 3)`, and at `t = 2` it is `−3`, which is negative, "
                    "so the graph falls on that whole stretch. It rises on either side."},
            {"q": "The derivative of `t² − 4t` is `2t − 4`. Where is the tangent line horizontal?",
             "a": ["t = 2", "t = 4", "t = 0", "t = −2"],
             "c": 0,
             "why": "A horizontal tangent has slope 0, so `2t − 4 = 0` gives `t = 2`. At `t = 4` "
                    "the slope is 4, and at `t = 0` it is `−4`."},
        ],
        "mistakes": [
            ("Writing the derivative of tⁿ as tⁿ⁻¹, or the derivative of a constant as 1",
             "The exponent comes down as a coefficient: the derivative of `t³` is `3t²`, not `t²`. The "
             "polynomial lesson found `3t²` as the constant term of the cube's quotient, and "
             "`t²` would give a slope of 1 at `t = 1` where the quotients head for 3. A "
             "constant is the other slip: every quotient of `f(t) = 5` is `(5 − 5)/h = 0`, so its "
             "derivative is 0, not 1."),
            ("Reading p′ > 0 as “p is positive”",
             "The sign of `p′` is the direction of the graph, not its height. "
             "For `t² − 4t` at `t = 3`, `p′ = 2` is positive, so the graph is rising, "
             "while `p = −3` is negative, so the graph is below the axis. The two signs "
             "answer different questions, and the derivative answers only the first."),
            ("Dropping the sign check once the zeros are found",
             "A zero of `p′` is a place where the tangent is level. It does not say whether "
             "the graph rises or falls on either side. The signs have to be tested "
             "between the zeros, and the next lesson shows a zero where the sign does not change."),
        ],
        "standard": ("Finish when you can differentiate a polynomial term by term and say from the sign of the result where the graph rises and falls.",
                     "You should be able to apply the power rule to every term, factor the "
                     "result where it factors, solve for the zeros, test one point in each "
                     "region, and state the intervals of rising and falling."),
        "note": "Where the derivative is zero is where the graph can turn, and not every "
                "zero is a turn. The rest of the course treats those zeros, starting in "
                "&ldquo;Where the Rate Is Zero&rdquo;, then the rules for products and "
                "compositions, the second derivative and the exponential.",
    },
]
