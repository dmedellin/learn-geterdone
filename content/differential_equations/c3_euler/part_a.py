"""Differential Equations and Euler's Method -- the first half.

What a differential equation is, how a proposed solution is checked, how an initial
value picks one curve out of a family, and the equation drawn as a slope field and
read without being solved.

Every figure below is read off the kit -- scripts/mathpath/labs/dekit.py -- by
executing its shipped JavaScript under node, and each preset pins the tiles it exists
to show. Where a design note and the kit disagreed, the kit won and the lesson says
what the kit does.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "what-a-differential-equation-is",
        "title": "What a Differential Equation Is",
        "module": "What a differential equation is",
        "one_line": "An equation whose unknown is a whole function, stated through its rate of change, and answered by a function that makes the residual zero.",
        "summary": (
            "An equation in algebra asks for a number. A differential equation asks for a "
            "function: it says how fast the unknown changes and leaves you to find what the "
            "unknown is. Its order is the highest derivative it mentions, and a proposed "
            "solution is tested by substituting it and reading the residual, the left side "
            "minus the right. The first surprise is that a solvable equation usually has "
            "infinitely many answers, not one."
        ),
        "key": [
            "y′ = 2t     the unknown is the function y",
            "order = the highest derivative present",
            "residual = left side − right side",
            "residual 0 for every t: a solution",
            "y = t² and y = t² + 3 both work",
        ],
        "key_label": "A differential equation, its order, and the residual test",
        "concepts_intro": (
            "Three ideas, in the order you need them: what is being asked for, how to size the "
            "equation, and how to decide whether an answer is one."
        ),
        "concepts": [
            ("The unknown is a function, not a number",
             "In `3x + 1 = 7` the unknown is a number and there is one right value. In `y′ = 2t` "
             "the unknown is a function `y` of `t`, and the equation does not say what `y` is. "
             "It says what `y` does: at every `t`, the rate of change of `y` is `2t`. To answer "
             "it you must produce a whole function, and to check an answer you must check it at "
             "every `t` at once."),
            ("The order is the highest derivative that appears",
             "`y′ = 2t` is first order, because only the first derivative appears. `y″ + y = 0` "
             "is second order, because `y″` does. The order tells you how much extra "
             "information a single answer will need, which “Initial Value Problems” "
             "makes exact. It is read from the equation and nothing else: the powers of "
             "`y` and the other terms do not change it."),
            ("A solution is checked by substituting it and reading the residual",
             "Differentiate the candidate, put it and its derivatives into the equation, and "
             "subtract the right side from the left. That difference is the "
             "<strong>residual</strong>. If it is `0` for every `t`, the candidate is a "
             "solution. If it is anything else, it is not, and the residual says by how much "
             "and where it fails. The check is algebra on a formula, not a trial at a few "
             "values."),
        ],
        "read_title": "An equation about a rate, and what counts as an answer",
        "read_intro": "The definition, the order, the residual test on three candidates, and the first look at why there are many solutions.",
        "body": [
            ("def", ("Differential equation, order, solution",
                     "A <strong>differential equation</strong> is an equation whose unknown is a "
                     "function and which involves one or more of that function's derivatives. "
                     "Its <strong>order</strong> is the highest derivative that appears. A "
                     "<strong>solution</strong> is a function that makes the equation true for "
                     "every `t` in some interval.",
                     "The word &ldquo;every&rdquo; carries the weight. A function that fits the "
                     "equation at a few values of `t` has satisfied a few instances of it, "
                     "and no more.")),
            ("p", "Start with the smallest example. The equation `y′ = 2t` says that the rate of "
                  "change of `y` at time `t` is `2t`: zero at the start, 2 at time 1, 4 at time 2. "
                  "In Accumulation and the Integral you met this question the other way up, as "
                  "&ldquo;which function has this rate&rdquo;, and the answer was an "
                  "antiderivative. A differential equation is that question asked of a rate that "
                  "may also depend on the unknown itself, as in `y′ = y`, and then the "
                  "antiderivative alone no longer answers it."),
            ("p", "The lab below takes an equation and a candidate and does the substitution "
                  "for you, symbolically. It differentiates the candidate exactly, forms "
                  "`y′ − 2t`, simplifies, and prints the result in the tile named Residual. "
                  "Nothing is evaluated at sample points; the verdict is about every `t`."),
            ("math", [
                "equation   y′ = 2t",
                "",
                "candidate     its y′     residual y′ − 2t     verdict",
                "t²            2t         0                    a solution",
                "t² + 3        2t         0                    a solution",
                "t³            3t²        3t² − 2t             not a solution",
            ]),
            ("p", "Read the three rows. The candidate `t²` has derivative `2t`, so the residual "
                  "`2t − 2t` is `0`. The candidate `t² + 3` has the same derivative, because a "
                  "constant has rate zero, so it is a solution as well. The candidate `t³` has "
                  "derivative `3t²`, and the residual `3t² − 2t` is not zero. It does vanish at "
                  "`t = 0` and at `t = 2/3`, and that does not rescue it: a solution needs the "
                  "residual to be zero at every `t`."),
            ("h3", "One equation, many answers"),
            ("p", "That `t²` and `t² + 3` are both solutions is the first fact to absorb, and "
                  "the one the misconception below gets wrong. Adding any constant `C` to "
                  "`t²` leaves the derivative at `2t`, so `t² + C` is a solution for every "
                  "`C`. A differential equation of this kind has a whole family of solutions, "
                  "one curve for each constant, and each is the same shape shifted up or down."),
            ("example", ("The same check on a candidate that does not work",
                         "Take `y′ = 2t` and the candidate `y = 2t`. Its derivative is `2`, so "
                         "the residual is `2 − 2t`, which the lab writes as `−2t + 2`.",
                         "That is zero at `t = 1` and nowhere else. At `t = 1` the candidate "
                         "and the equation agree, and one instance of agreement is exactly what "
                         "the residual test refuses to accept. “Checking a Proposed Solution” "
                         "meets the same trap in a harder equation.")),
            ("h3", "What the lab does and does not claim"),
            ("p", "The residual tile is exact: it is the symbolic left side minus right side, "
                  "and it prints `0` only when the simplified expression is identically zero. "
                  "The curve in the plot is a drawing made with ordinary floating-point numbers, "
                  "and it is there to be looked at, not to be trusted for a digit."),
        ],
        "lab": ("dekit", {
            "mode": "verify",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "y' = 2t with the candidate t^2",
                 "equation": "y' = 2t", "candidate": "t^2", "ic": None, "expect": {"vfOrder": "1", "vfResidual": "0", "vfVerdict": "Solution"}},
                {"id": "shifted", "label": "y' = 2t with the candidate t^2 + 3",
                 "equation": "y' = 2t", "candidate": "t^2 + 3", "ic": None, "expect": {"vfOrder": "1", "vfResidual": "0", "vfVerdict": "Solution"}},
                {"id": "cube", "label": "y' = 2t with the candidate t^3",
                 "equation": "y' = 2t", "candidate": "t^3", "ic": None, "expect": {"vfOrder": "1", "vfResidual": "3t² − 2t", "vfVerdict": "Not a solution"}},
            ],
            "panel_title": "Substitute a candidate and read the residual",
            "panel_intro": (
                "Choose each preset in turn. The order tile reads the equation, the residual "
                "tile is the left side minus the right after substitution, and the verdict "
                "follows from whether that is zero for every t. Then type your own candidate "
                "for y&prime; = 2t, such as t^2 + 5 or 2t, and predict the residual before you "
                "look."
            ),
        }),
        "steps_title": "Testing a candidate against an equation",
        "steps_intro": "The same four moves for every equation on this course, in the same order.",
        "steps": [
            ("Name the unknown and read the order",
             "Find the unknown function and the highest derivative of it in the equation. "
             "That is the order, and it is all the order is."),
            ("Move everything to one side",
             "Write the equation as left side minus right side. For `y′ = 2t` that is "
             "`y′ − 2t`. The candidate will be tested against zero, so the zero has to be on "
             "the right."),
            ("Differentiate the candidate and substitute",
             "Compute every derivative the equation mentions, exactly, and put the candidate "
             "and those derivatives where `y` and its derivatives stand."),
            ("Simplify and read the residual",
             "If it simplifies to `0` for all `t`, the candidate is a solution. If any `t` "
             "remains in it, it is not, and the residual tells you what is left over."),
        ],
        "worked": {
            "title": "Two candidates for y′ = 2t",
            "intro": [
                "Test `y = t³` and `y = t² + 3` against `y′ = 2t`, with the residual taken as "
                "the derivative minus `2t`.",
            ],
            "lines": [
                "y = t³:",
                "   y′ = 3t²",
                "   residual = 3t² − 2t = t·(3t − 2)",
                "   not zero for all t, so not a solution",
                "",
                "y = t² + 3:",
                "   y′ = 2t + 0 = 2t",
                "   residual = 2t − 2t = 0",
                "   a solution",
                "",
                "y = t² + C, for any constant C:",
                "   y′ = 2t, residual 0, so a solution for every C",
            ],
            "after": [
                "The third candidate is the one to keep. The constant `3` dropped out of the "
                "derivative, and so would any other constant, which is why the equation has "
                "one solution for every `C` and not a single answer. A single curve will "
                "appear only when something fixes `C`, and “Initial Value Problems” is where "
                "that happens.",
                "The factored residual `t·(3t − 2)` shows why `t³` is no solution even though "
                "the equation holds at two points: it is zero at `t = 0` and `t = 2/3` and "
                "nonzero between and beyond them.",
            ],
        },
        "quiz_title": "Order, residual and solution",
        "quiz": [
            {"q": "What is the order of the differential equation `y″ + 3y′ = t`?",
             "a": ["1, because the equation has one unknown function",
                   "2, because the highest derivative is `y″`",
                   "3, because of the coefficient of `y′`",
                   "It depends on the value of `t`"],
             "c": 1,
             "why": "The order is the highest derivative that appears, and `y″` appears. The "
                    "number of unknown functions, the coefficients and the value of `t` have "
                    "nothing to do with it."},
            {"q": "For `y′ = 2t`, the candidate `y = t² − 5` gives which result?",
             "a": ["A solution: its derivative is `2t`, so the residual is `0`",
                   "Not a solution, because of the `−5`",
                   "A solution only at `t = 0`",
                   "Not a solution, because a solution has to be `t²` exactly"],
             "c": 0,
             "why": "The derivative of a constant is zero, so `t² − 5` has derivative `2t` and "
                    "the residual `2t − 2t` is zero for every `t`. The `−5` is allowed, and "
                    "so is every other constant, which is why `t²` is not the only answer."},
            {"q": "The candidate `y = t³` for `y′ = 2t` has residual `3t² − 2t`, which is zero at `t = 0` and at `t = 2/3`. What does that tell you?",
             "a": ["It is a solution, because the residual is zero at `t = 0`",
                   "It is a solution on the interval from 0 to 2/3",
                   "It is not a solution: the residual is zero only at isolated values, not for every `t`",
                   "Nothing yet; you have to test more values of `t`"],
             "c": 2,
             "why": "A solution needs the residual to be zero at every `t` in an interval. "
                    "Here it is `t·(3t − 2)`, which is nonzero everywhere else, so the question "
                    "is already decided. No further sample values are needed, because the "
                    "residual is a formula, not a list."},
            {"q": "How many functions satisfy `y′ = 2t`?",
             "a": ["Exactly one, `t²`",
                   "None, until a starting value is given",
                   "Two, one for each sign of `t`",
                   "One for every constant `C`: `t² + C` works each time"],
             "c": 3,
             "why": "Every `t² + C` has derivative `2t`, so each is a solution. Nothing in "
                    "the equation fixes `C`; a starting value would, and without one the "
                    "equation is already satisfied by the whole family."},
        ],
        "mistakes": [
            ("Expecting a differential equation to have a number for an answer",
             "The unknown is a function, and `y′ = 2t` is satisfied by `t²` and by `t² + 3` "
             "and by `t² − 7`, each with residual zero in the lab. There is no single value "
             "to find and no single curve. A number comes out only if you are asked for one "
             "value of a particular solution, after something has chosen which curve."),
            ("Reading the order from the exponent or the number of terms",
             "The order is the highest derivative and nothing else. `y′ = y²` is first order "
             "even though it has a square in it, and `y″ = 0` is second order even though it "
             "is short."),
            ("Testing a candidate at one value of t and stopping",
             "The residual of `t³` in `y′ = 2t` is zero at `t = 0`, so a check there passes "
             "and the candidate is wrong. The test is the simplified residual for every `t`, "
             "which is exactly what the lab prints."),
        ],
        "standard": ("Finish when you can say what a differential equation is, name its order, and decide a candidate.",
                     "You should be able to state in a sentence that the unknown is a function, "
                     "read the order of an equation from its highest derivative, substitute a "
                     "candidate and simplify the residual by hand on a first-order equation, "
                     "and decide whether it is a solution from whether that residual is zero for "
                     "every `t`. You should also be able to say why `t²` and `t² + 3` are both "
                     "answers to the same equation."),
        "note": 'This lesson tested candidates that were handed over. The next uses the same residual on harder equations, a second-order one with an exponential, one with a coefficient that depends on <em>t</em>, and one that is not linear, and learns to tell which kind it is. &ldquo;Checking a Proposed Solution&rdquo; is where.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "checking-a-proposed-solution",
        "title": "Checking a Proposed Solution",
        "module": "What a differential equation is",
        "one_line": "Substitute an exponential or a power into a second-order or variable-coefficient equation, simplify the residual, and decide, then classify the equation as linear or not.",
        "summary": (
            "The residual test is the same on every equation, and it gets more work to do as "
            "equations get harder. A second-order equation needs two derivatives of the "
            "candidate; an equation with a coefficient that depends on `t` needs that "
            "coefficient carried through; and a nonlinear equation turns out to behave "
            "differently from the others. The test decides the first two exactly, and the "
            "equation's form tells you whether a multiple of a solution is still a solution."
        ),
        "key": [
            "y″ − y′ − 2y = 0   with y = e^(2t)",
            "4e^(2t) − 2e^(2t) − 2e^(2t) = 0",
            "y = eᵗ leaves residual −2·eᵗ, never 0",
            "agreeing at one t proves nothing",
            "linear: y, y′, y″ to the first power only",
        ],
        "key_label": "The residual on a harder equation, and linear against not",
        "concepts_intro": (
            "Three ideas: carrying the substitution through more derivatives, why one "
            "matching point is not a check, and the one property that sorts equations."
        ),
        "concepts": [
            ("Each derivative the equation mentions has to be computed",
             "For `y″ − y′ − 2y = 0` the candidate `y = e^(2t)` needs `y′ = 2e^(2t)` and "
             "`y″ = 4e^(2t)`, because the derivative of `e^(kt)` is `k·e^(kt)` and a second "
             "derivative applies that twice. Put all three in and the residual is a sum of "
             "multiples of `e^(2t)` that either cancels or leaves a multiple of it behind."),
            ("A residual that is zero at one value of t does not make a solution",
             "A function can satisfy an equation at a single `t` or at a few and still fail "
             "everywhere else. Take `t·y′ = 2y` and the candidate `y = 5t`: the residual is "
             "`−5t`, which is zero at `t = 0` and nowhere else. The only verdict that "
             "counts is the simplified residual, and it is zero for every `t` or it is not."),
            ("An equation is linear when the unknown and its derivatives appear only to the first power",
             "In a <strong>linear</strong> equation `y`, `y′` and `y″` are each multiplied by "
             "something that depends on `t` alone and added up, with at most a term in `t` "
             "alone besides. `t·y′ = 2y` is linear; "
             "`y′ = y²` is not, because `y` is squared. The distinction matters at once: "
             "a constant multiple of a solution of a linear equation with zero on the right "
             "is another solution, and for a nonlinear equation it usually is not."),
        ],
        "read_title": "The same test on harder equations",
        "read_intro": "A second-order equation, a coefficient that depends on t, a nonlinear equation, and the one place the nonlinear case differs.",
        "body": [
            ("p", "Start with `y″ − y′ − 2y = 0`. It is second order, so a candidate needs two "
                  "derivatives, and it is linear, so each of `y″`, `y′` and `y` appears once "
                  "with a number in front. Try `y = e^(2t)`. Then `y′ = 2e^(2t)` and "
                  "`y″ = 4e^(2t)`, and the residual is `4e^(2t) − 2e^(2t) − 2e^(2t)`, which is "
                  "`(4 − 2 − 2)·e^(2t) = 0`. A solution."),
            ("p", "Now try `y = eᵗ`, the same shape with a different rate. Here `y′ = eᵗ` and "
                  "`y″ = eᵗ`, and the residual is `eᵗ − eᵗ − 2eᵗ = −2eᵗ`. The coefficient "
                  "`−2` is not zero and `eᵗ` is never zero, so the residual is not zero at any "
                  "`t`, and the candidate fails everywhere. The two exponentials differ only in "
                  "the number in the exponent, and the equation accepts one and rejects the "
                  "other."),
            ("math", [
                "y″ − y′ − 2y = 0",
                "",
                "candidate    y′         y″         residual         verdict",
                "e^(2t)       2e^(2t)    4e^(2t)    0                a solution",
                "eᵗ           eᵗ         eᵗ         −2·eᵗ            not a solution",
            ]),
            ("h3", "A coefficient that depends on t"),
            ("p", "The equation `t·y′ = 2y` has `t` multiplying the derivative, and the "
                  "substitution carries it along. For `y = 5t²` the derivative is `10t`, so "
                  "`t·y′ = 10t²`, and `2y = 10t²`, and the residual is `0`. The candidate "
                  "`5t²` is a solution, and so would be `t²` or `−3t²`: each is a constant "
                  "multiple of `t²`, and in a linear equation with zero on the right that is "
                  "allowed."),
            ("p", "A candidate `y = 5t` makes a good contrast. Its derivative is `5`, the "
                  "left side is `5t`, the right side is `10t`, and the residual is `−5t`. At "
                  "`t = 0` both sides are zero, so a check at that one point would pass it. "
                  "Type `5t` into the lab and read the residual: it is not zero."),
            ("h3", "A nonlinear equation"),
            ("p", "Now `y′ = y²`. Take `y = 1/(1 − t)`. By the chain rule its derivative is "
                  "`1/(1 − t)²`, and `y²` is `1/(1 − t)²` as well, so the residual is `0`. "
                  "The lab decides this one exactly, because a ratio of polynomials in `t` "
                  "can be differentiated without rounding, and it labels the equation "
                  "nonlinear because `y` is squared."),
            ("thm", ("What linear buys, stated and used",
                     "In a linear equation whose right side is `0`, a constant multiple of a "
                     "solution is a solution, and the sum of two solutions is a solution. "
                     "For a nonlinear equation neither is guaranteed.")),
            ("p", "The linear case follows from the residual being built from sums and "
                  "constant multiples; the lab demonstrates it on the presets and does not "
                  "prove it. The nonlinear case is easy to watch fail: take "
                  "`y′ = y²` and double the solution to `2/(1 − t)`. Its derivative is "
                  "`2/(1 − t)²` and its square is `4/(1 − t)²`, so the residual is "
                  "`−2/(1 − t)²`, which is never zero (the lab prints it expanded, as "
                  "`−2/(t² − 2t + 1)`). The doubling that was harmless in "
                  "the linear equation breaks this one."),
            ("p", "One limit of the lab belongs here. A ratio of polynomials in `t`, and "
                  "exponential or sine and cosine candidates in a linear equation, are "
                  "decided exactly. An exponential candidate in a nonlinear equation is not: "
                  "the lab then evaluates the residual at five values of `t` in "
                  "floating point and says so in the verdict, which reads that it checked at "
                  "five points only. That is a spot check, and it is labelled as one."),
        ],
        "lab": ("dekit", {
            "mode": "verify",
            "preset": "two-exps",
            "presets": [
                {"id": "two-exps", "label": "y'' - y' - 2y = 0 with e^(2t)",
                 "equation": "y'' - y' - 2*y = 0", "candidate": "e^(2t)", "ic": None, "expect": {"vfLinear": "Linear", "vfResidual": "0", "vfVerdict": "Solution"}},
                {"id": "wrong-exp", "label": "y'' - y' - 2y = 0 with e^t",
                 "equation": "y'' - y' - 2*y = 0", "candidate": "e^t", "ic": None, "expect": {"vfLinear": "Linear", "vfResidual": "−2·e^t", "vfVerdict": "Not a solution"}},
                {"id": "power", "label": "t y' = 2y with 5t^2",
                 "equation": "t*y' = 2*y", "candidate": "5t^2", "ic": None, "expect": {"vfLinear": "Linear", "vfResidual": "0", "vfVerdict": "Solution"}},
                {"id": "nonlinear", "label": "y' = y^2 with 1/(1 - t)",
                 "equation": "y' = y^2", "candidate": "1/(1 - t)", "ic": None, "expect": {"vfLinear": "Nonlinear", "vfResidual": "0", "vfVerdict": "Solution"}},
            ],
            "panel_title": "The residual on four equations",
            "panel_intro": (
                "Each preset names an equation and a candidate; the order, linear and residual "
                "tiles are computed from them. After the presets, keep the equation and change "
                "the candidate: e^(-t) in the second-order equation, 5t in t y&prime; = 2y, and "
                "2/(1 - t) in y&prime; = y^2, and read each residual."
            ),
        }),
        "steps_title": "Checking a candidate on a harder equation",
        "steps_intro": "The four moves of “What a Differential Equation Is”, with the extra care a harder equation needs.",
        "steps": [
            ("Write down every derivative the equation uses",
             "For a second-order equation that is `y′` and `y″` as well as `y`, each computed "
             "from the candidate before anything is substituted. Skipping this line is how "
             "the powers of two go missing from `e^(2t)`."),
            ("Substitute and keep the coefficients",
             "Put the candidate and its derivatives where `y`, `y′` and `y″` stand, "
             "including any factor of `t` in front of them, and leave the equation moved to "
             "one side so the residual is the whole left side."),
            ("Collect like terms and read the residual",
             "Group the terms that share a factor, such as every multiple of `e^(2t)`. If "
             "the coefficients sum to zero the residual is zero. If anything survives, the "
             "candidate fails, and the survivor is the residual."),
            ("Classify the equation",
             "Look at `y`, `y′` and `y″`. If each appears only to the first power, "
             "multiplied by something in `t` alone, the equation is linear. Anything such as "
             "`y²` or `y·y′` makes it nonlinear."),
        ],
        "worked": {
            "title": "Two exponentials in one second-order equation",
            "intro": [
                "Test `e^(2t)` and `eᵗ` against `y″ − y′ − 2y = 0`.",
            ],
            "lines": [
                "y = e^(2t):",
                "   y′ = 2·e^(2t)",
                "   y″ = 4·e^(2t)",
                "   residual = 4·e^(2t) − 2·e^(2t) − 2·e^(2t) = 0",
                "   a solution",
                "",
                "y = eᵗ:",
                "   y′ = eᵗ,  y″ = eᵗ",
                "   residual = eᵗ − eᵗ − 2·eᵗ = −2·eᵗ",
                "   never zero, so not a solution",
            ],
            "after": [
                "The only difference between the two is the number in the exponent, and the "
                "equation singles out `2`. In Second-Order Linear Equations this "
                "becomes a method, because the right numbers are the roots of a quadratic. "
                "For now the point is that the check is mechanical and decisive.",
                "For a rehearsal, try `e^(−t)`. Its derivatives are `−e^(−t)` and `e^(−t)`, and "
                "the residual is `e^(−t) + e^(−t) − 2e^(−t)`, which is zero. This equation "
                "has two exponentials that work, and the lab confirms it.",
            ],
        },
        "quiz_title": "Residuals, one-point checks and linearity",
        "quiz": [
            {"q": "In `y″ − y′ − 2y = 0`, the candidate `y = e^(−t)` has `y′ = −e^(−t)` and `y″ = e^(−t)`. What is the verdict?",
             "a": ["A solution: the residual is `(1 + 1 − 2)·e^(−t) = 0`",
                   "Not a solution: only `e^(2t)` was shown to work",
                   "Not a solution: `y″` would have to be negative",
                   "A solution only for `t > 0`"],
             "c": 0,
             "why": "Substituting gives `e^(−t) − (−e^(−t)) − 2e^(−t)`, which is "
                    "`e^(−t) + e^(−t) − 2e^(−t) = 0` for every `t`. Another candidate "
                    "working does not exclude this one, and the sign of `y″` is not a "
                    "condition of the equation."},
            {"q": "A student checks `y = 3t` in `t·y′ = 2y`, finds both sides equal 0 at `t = 0`, and declares it a solution. What is wrong?",
             "a": ["Nothing: the equation holds, so the candidate is a solution",
                   "The candidate must be a power of `t` with exponent 2",
                   "A candidate cannot be checked at `t = 0`",
                   "One matching point is not a check: the residual is `3t − 6t = −3t`, zero only at `t = 0`"],
             "c": 3,
             "why": "The derivative of `3t` is `3`, so the left side is `3t` and the right "
                    "side is `6t`. Their difference `−3t` is zero only at the single point "
                    "where the student looked. A solution needs the residual to vanish for "
                    "every `t`."},
            {"q": "Which of these equations is linear?",
             "a": ["`y·y′ = t`",
                   "`y′ = y²`",
                   "`t·y′ + y = t²`",
                   "`y′ = 1/y`"],
             "c": 2,
             "why": "In `t·y′ + y = t²` the unknown and its derivative each appear to the "
                    "first power, multiplied by a function of `t` alone. The product `y·y′`, "
                    "the square `y²` and the reciprocal `1/y` all combine the unknown with "
                    "itself, which is what makes an equation nonlinear."},
            {"q": "`y = 1/(1 − t)` solves `y′ = y²`. What happens to `2/(1 − t)`, which is twice that function?",
             "a": ["It is a solution too, since constant multiples are always allowed",
                   "It is not: its residual is `−2/(1 − t)²`, since the equation is nonlinear",
                   "It is a solution only for `t < 1`",
                   "It cannot be tested because it has a denominator"],
             "c": 1,
             "why": "The derivative of `2/(1 − t)` is `2/(1 − t)²` and its square is "
                    "`4/(1 − t)²`; the difference is `−2/(1 − t)²`, nonzero wherever it is "
                    "defined. Constant multiples are safe in a linear equation with zero on "
                    "the right, and this one is not linear."},
        ],
        "mistakes": [
            ("Accepting a function because it satisfies the equation at one value of t",
             "The candidate `5t` in `t·y′ = 2y` has both sides zero at `t = 0`, and its "
             "residual is `−5t`, which is zero nowhere else. A pass at a point says "
             "nothing; the whole simplified residual has to be zero."),
            ("Forgetting a derivative or its coefficient in a second-order check",
             "For `e^(2t)` the second derivative is `4e^(2t)`, not `2e^(2t)`, and the "
             "residual `4 − 2 − 2` is zero only with the 4. Write `y′` and `y″` as their own "
             "lines before substituting."),
            ("Assuming a multiple of a solution is always a solution",
             "That holds for a linear equation with zero on the right, which `y″ − y′ − 2y = 0` "
             "and `t·y′ = 2y` are. It fails for `y′ = y²`: the double of `1/(1 − t)` has "
             "residual `−2/(1 − t)²`. Classify the equation first."),
        ],
        "standard": ("Finish when you can substitute an exponential or a power into an equation and decide it.",
                     "You should be able to compute the two derivatives of `e^(kt)` or `a·tⁿ`, "
                     "substitute into a second-order or variable-coefficient equation, "
                     "simplify the residual by collecting like terms, state the verdict, and say "
                     "whether the equation is linear and what that allows."),
        "note": 'A residual of zero says a function is one solution, and the previous lesson showed there are usually many. The next one picks a single curve from the family by fixing the constants from starting values, and asks how many such values an equation needs. &ldquo;Initial Value Problems&rdquo; is where.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "initial-value-problems",
        "title": "Initial Value Problems",
        "module": "What a differential equation is",
        "one_line": "Fix the constant in a family of solutions from one initial value, state how many values a first- and a second-order equation need, and check the result.",
        "summary": (
            "A family of solutions has a constant in it, and a single curve needs the constant "
            "pinned. An initial value does that: it says the solution passes through a given "
            "point. A first-order equation has one constant and needs one value; a "
            "second-order equation has two and needs two. The constant is found by "
            "substituting the value, and the finished solution is checked by the same "
            "residual."
        ),
        "key": [
            "y′ = 2t, y(1) = 5:  1 + C = 5, C = 4",
            "y = t² + 4 is the one curve through (1, 5)",
            "first order: one constant, one value",
            "second order: two constants, two values",
            "check: the residual is still 0",
        ],
        "key_label": "Fixing a constant, and counting how many values an equation needs",
        "concepts_intro": (
            "Three ideas: what an initial value is, how many a given equation needs, and why "
            "it selects a curve and says nothing about where the solution begins."
        ),
        "concepts": [
            ("An initial value is a point the solution must pass through",
             "`y(1) = 5` says that the solution takes the value 5 at `t = 1`. Of all the "
             "curves `t² + C` it leaves exactly one, the one that goes through `(1, 5)`. The "
             "equation together with the value is an <strong>initial value problem</strong>, "
             "and it is the equation and the value that have an answer, not the equation "
             "alone."),
            ("The number of values needed is the order",
             "Undoing one derivative brings one constant, which is what you met as the "
             "constant of integration. A first-order equation therefore has a family with one "
             "constant and needs one value. A second-order equation undoes two derivatives, "
             "carries two constants, and needs two: the value of `y` and the value of `y′` at "
             "the same `t`."),
            ("The constant is found by substituting the value, then the result is checked",
             "Put the given `t` and `y` into the family and solve the resulting equation for "
             "the constant: `1² + C = 5` gives `C = 4`. The finished function is then run "
             "through the residual test as before. The value fixes the curve; it does not "
             "make a wrong family right."),
        ],
        "read_title": "One curve out of a family",
        "read_intro": "How a value selects a curve, the count of values by order, three families, and where the lab stops.",
        "body": [
            ("def", ("Initial value problem",
                     "A differential equation together with values of the unknown, and for a "
                     "second-order equation of its derivative, at one starting `t = t₀`. "
                     "For first order the problem is `y′ = f(t, y)` with `y(t₀) = y₀`.",
                     "A <strong>solution</strong> of the problem is a solution of the equation "
                     "that also takes the stated values at `t₀`.")),
            ("p", "Take `y′ = 2t` with `y(1) = 5`. The family of solutions is `y = t² + C`. The "
                  "value says that at `t = 1` the function is 5, and `t² + C` at `t = 1` is "
                  "`1 + C`, so `1 + C = 5` and `C = 4`. The solution of the problem is "
                  "`y = t² + 4`. The lab reports this as `C = 4 from y(1) = 5` and the "
                  "residual stays `0`: fixing a constant does not leave the family of "
                  "solutions, it picks a member."),
            ("math", [
                "y′ = 2t,  family  y = t² + C",
                "",
                "value        equation for C       C     the solution",
                "y(1) = 5     1 + C = 5            4     t² + 4",
                "y(0) = 0     0 + C = 0            0     t²",
                "y(2) = 1     4 + C = 1            −3    t² − 3",
            ]),
            ("h3", "Each constant comes with a value"),
            ("p", "The same procedure works for any family linear in its constants. For "
                  "`y′ = 3y` the family is `C·e^(3t)`, and `y(0) = 2` gives `C·e⁰ = 2`, so "
                  "`C = 2` and the solution is `2e^(3t)`. The value is taken at `t = 0` "
                  "because that is where the lab can evaluate an exponential exactly, "
                  "since `e⁰ = 1`: at any other `t` the value would need an irrational "
                  "number, and the lab says that it is refusing to fit there."),
            ("p", "A second-order equation has two constants, and two values give two "
                  "equations for them. Take `y″ − y′ − 2y = 0`, whose two exponentials "
                  "“Checking a Proposed Solution” verified: the family is "
                  "`C·e^(2t) + D·e^(−t)`, with derivative `2C·e^(2t) − D·e^(−t)`. At "
                  "`t = 0` both exponentials are 1, so `y(0) = C + D` and `y′(0) = 2C − D`. "
                  "The values `y(0) = 1` and `y′(0) = −2` give `C + D = 1` and `2C − D = −2`; "
                  "adding them, `3C = −1`, so `C = −1/3` and `D = 4/3`, and the lab prints "
                  "`C = −1/3, D = 4/3`. Two values, two equations, one small system."),
            ("p", "For `y″ + y = 0` the family is `C·cos(t) + D·sin(t)`, with derivative "
                  "`−C·sin(t) + D·cos(t)`. That sine and cosine are each other's rates, with "
                  "the one sign change, is taken on trust here and demonstrated in “Sine, "
                  "Cosine and Their Rates” in Second-Order Linear Equations; what this fit "
                  "needs is only their values at `t = 0`, where the cosine is 1 and the sine "
                  "is 0, so `y(0) = C` and `y′(0) = D`. The values `y(0) = 1` and "
                  "`y′(0) = −2` therefore give `C = 1` and `D = −2` at once, and the solution "
                  "is `cos(t) − 2·sin(t)`. One value would leave the other constant free."),
            ("example", ("Why one value is not enough for a second-order equation",
                         "Give the lab `y″ + y = 0` with only `y(0) = 1`. It declines to fit "
                         "anything: the constants tile shows a dash, and the banner says that "
                         "two constants need two values, `y(t₀)` and `y′(t₀)`.",
                         "By hand the situation is clear: `y(0) = 1` forces `C = 1` and says "
                         "nothing about `D`. Every function `cos(t) + D·sin(t)` is a solution that passes through "
                         "`(0, 1)`, and they differ in how steeply they pass. The second value, "
                         "the rate at the start, is the missing piece of information, and "
                         "supplying it is what selects one.")),
            ("h3", "A value selects a curve; it does not start the solution"),
            ("p", "It is tempting to read `y(1) = 5` as saying that the solution begins at "
                  "`t = 1`. It does not. The curve `t² + 4` is defined on both sides of "
                  "`t = 1`, and what the value does is identify which curve. The point "
                  "`t₀` is simply where the information is given; the solution runs "
                  "both ways from it."),
            ("p", "One fact about initial value problems is used on trust at this stage. "
                  "For the equations in this course, a starting point selects exactly one "
                  "solution. “Blow-Up and the Interval of Existence” states the condition "
                  "under which that is true and shows an equation where the solution "
                  "stops existing; the lab, here, only fits the constants."),
        ],
        "lab": ("dekit", {
            "mode": "verify",
            "preset": "first",
            "presets": [
                {"id": "first", "label": "y' = 2t, family t^2 + C, y(1) = 5",
                 "equation": "y' = 2t", "candidate": "t^2 + C", "ic": [1, 5], "expect": {"vfFamily": "C = 4 from y(1) = 5", "vfIC": "satisfied"}},
                {"id": "growth", "label": "y' = 3y, family C e^(3t), y(0) = 2",
                 "equation": "y' = 3*y", "candidate": "C e^(3t)", "ic": [0, 2], "expect": {"vfFamily": "C = 2 from y(0) = 2", "vfIC": "satisfied"}},
                {"id": "two-exps", "label": "y'' - y' - 2y = 0, family C e^(2t) + D e^(-t)",
                 "equation": "y'' - y' - 2*y = 0", "candidate": "C e^(2t) + D e^(-t)", "ic": [0, 1, -2], "expect": {"vfFamily": "C = −1/3, D = 4/3", "vfIC": "satisfied"}},
                {"id": "second", "label": "y'' + y = 0, family C cos(t) + D sin(t)",
                 "equation": "y'' + y = 0", "candidate": "C cos(t) + D sin(t)", "ic": [0, 1, -2], "expect": {"vfFamily": "C = 1, D = −2", "vfIC": "satisfied"}},
            ],
            "panel_title": "From a family to one curve",
            "panel_intro": (
                "The candidate is a family: C stands for a constant the lab will solve for, "
                "and D for a second one. The constants tile shows what the initial values "
                "force and the initial-values tile says whether the result satisfies them. "
                "Change the value in the first preset to y(1) = 0 and predict C before you read it."
            ),
        }),
        "steps_title": "Solving an initial value problem",
        "steps_intro": "Four moves, once the family of solutions is known.",
        "steps": [
            ("Write the family with its constants",
             "One constant for a first-order equation, two for a second-order one. If you "
             "cannot name the constants, you do not yet have a general solution."),
            ("Substitute the starting values",
             "Put `t₀` and `y₀` into the family, and for a second-order equation put `t₀` "
             "and `y′(t₀)` into its derivative. Each value gives one equation for the "
             "constants."),
            ("Solve for the constants",
             "One equation for one constant is arithmetic. Two equations for two constants "
             "are a small linear system: `C + D = 1` and `2C − D = −2` for the exponential "
             "pair, solved by adding them, as in Algebra's Systems and Matrices. For the sine "
             "and cosine pair the system arrives already solved, because each value at "
             "`t = 0` names one constant on its own."),
            ("Check the function that results",
             "Write the solution with the constants in place, run the residual test on it, "
             "and confirm that it takes the stated values. Both must hold."),
        ],
        "worked": {
            "title": "y′ = 2t with y(1) = 5",
            "intro": [
                "The family is `y = t² + C`; find the constant and check the answer.",
            ],
            "lines": [
                "family:       y = t² + C",
                "value:        y(1) = 5",
                "substitute:   1² + C = 5",
                "solve:        C = 4",
                "solution:     y = t² + 4",
                "",
                "check the equation: y′ = 2t, residual 2t − 2t = 0",
                "check the value:    y(1) = 1 + 4 = 5",
            ],
            "after": [
                "Two checks, and both are needed. The residual says the function solves the "
                "equation, and the value says it is the member that goes through the stated "
                "point. A function can pass either test and fail the other: `t²` solves the "
                "equation and misses the point, and `5` hits the point and solves nothing.",
                "For a rehearsal, take the same equation with `y(2) = 1`. The substitution is "
                "`4 + C = 1`, so `C = −3`, and the lab will say so.",
            ],
        },
        "quiz_title": "Constants, counts and checks",
        "quiz": [
            {"q": "For `y′ = 2t` with `y(1) = 5`, the solution is `y = t² + C`. What is `C`?",
             "a": ["`C = 5`, since 5 is the value given",
                   "`C = 6`, since `t² = 1` has to be added to 5",
                   "`C = 4`, since `1 + C = 5`",
                   "`C` cannot be found from one value"],
             "c": 2,
             "why": "At `t = 1` the family reads `1² + C`, and the value says that equals 5, "
                    "so `C = 4`. Taking `C` to be the value itself forgets that the `t²` "
                    "term contributes to it, and one value is exactly enough for one "
                    "constant."},
            {"q": "How many initial values does a second-order equation such as `y″ + y = 0` need to give a single solution?",
             "a": ["One, since there is one unknown function",
                   "Two, one for `y` and one for `y′`, at the same `t`",
                   "Two, both for `y`, at different values of `t`",
                   "Three, one per term of the equation"],
             "c": 1,
             "why": "The family has two constants, and a pair of values that pins both is "
                    "the value of `y` and of `y′` at the starting point. The notion in the "
                    "third option, two values of `y` at different points, is a different kind "
                    "of problem and not an initial value problem."},
            {"q": "A student reads `y(1) = 5` as saying the solution starts at `t = 1` and is not defined before. What corrects this?",
             "a": ["The solution `t² + 4` is defined for all `t`; the value only identifies the curve",
                   "A solution is always defined only after `t₀`",
                   "The value is taken at `t = 0` in every problem",
                   "Initial values apply to second-order equations only"],
             "c": 0,
             "why": "The function `t² + 4` is a perfectly good solution of `y′ = 2t` on the "
                    "whole line, before `t = 1` as much as after. The starting point is "
                    "where the value is stated, and nothing makes it a boundary."},
            {"q": "For `y″ + y = 0` with the family `C·cos(t) + D·sin(t)`, only `y(0) = 1` is given. What follows?",
             "a": ["`C = 1, D = 0`, taking the unstated constant to be zero",
                   "Second-order equations cannot have initial values",
                   "`C = 1` and `D` is undetermined: every `cos(t) + D·sin(t)` passes through `(0, 1)`",
                   "`C = 0, D = 1`, swapping the roles"],
             "c": 2,
             "why": "At `t = 0` the sine vanishes, so `y(0)` pins `C` and leaves `D` "
                    "completely untouched. Every member `cos(t) + D·sin(t)` passes through "
                    "`(0, 1)`, which is why a second value is needed and why guessing `D = 0` "
                    "would be inventing a condition. The lab declines to fit for this reason."},
        ],
        "mistakes": [
            ("Treating the initial value as where t starts, not as a value that selects one solution",
             "`y(1) = 5` is a point the curve passes through. The solution `t² + 4` exists on "
             "both sides of `t = 1`. What the value changes is which constant, `C = 4`, and "
             "nothing about where the solution lives."),
            ("Setting the constant equal to the given value",
             "In `y = t² + C` with `y(1) = 5` the constant is `4`, because `1² = 1` already "
             "contributes. Substitute, then solve; do not copy."),
            ("Giving a second-order equation one starting value",
             "Two constants need two values. With only `y(0) = 1` the constant `C` is `1` and "
             "`D` is undetermined, every `cos(t) + D·sin(t)` is a valid answer, and the lab "
             "declines to fit."),
        ],
        "standard": ("Finish when you can fix a constant from an initial value and say how many a given equation needs.",
                     "You should be able to write the family of solutions with its constants, "
                     "substitute a starting value to solve for the constant of a first-order "
                     "equation, solve the two equations for the constants of a second-order "
                     "one, state that the numbers needed are one and two, and run the residual "
                     "test on the result."),
        "note": 'Everything so far has been algebra on a formula we were given. The next two lessons look at the equation without any formula at all, as a field of slopes drawn over the plane, and ask what that picture lets you read. &ldquo;Slope Fields&rdquo; builds it.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "slope-fields",
        "title": "Slope Fields",
        "module": "Pictures of solutions",
        "one_line": "Compute the slope f(t, y) at a grid point exactly, draw the short segment, and find the curve where the slope is zero.",
        "summary": (
            "An equation `y′ = f(t, y)` gives a slope at every point of the plane, and that "
            "is all the information it has. Draw a short segment of that slope at each point "
            "of a grid and the equation is a picture, with no solving involved. The slope "
            "at a chosen point is a number to compute exactly, and the points where it is "
            "zero make a curve to find."
        ),
        "key": [
            "y′ = f(t, y) gives a slope at each point",
            "slope at (t, y) is f(t, y), computed exactly",
            "y′ = t − y at (2, 0): slope 2",
            "slope 0 on y = t, the nullcline",
            "a segment shows slope, not where it goes",
        ],
        "key_label": "A slope field: the equation as a grid of slopes",
        "concepts_intro": (
            "Three ideas: what the picture is made of, how one slope is computed, and the "
            "one curve worth finding straight away."
        ),
        "concepts": [
            ("The equation is a rule that assigns a slope to every point",
             "In `y′ = f(t, y)` the right side takes a point `(t, y)` and returns a number. "
             "A solution is a curve whose slope at each of its points is that number, and so "
             "the equation is a statement about slopes before it is a statement about "
             "functions. A <strong>slope field</strong> draws that statement: a short "
             "segment with slope `f(t, y)` at each point of a grid."),
            ("A slope is computed by substitution, and it is exact",
             "To find the slope at `(2, 0)` for `y′ = t − y`, put `t = 2` and `y = 0`: "
             "`2 − 0 = 2`. There is no limit and no approximation, because the slope is the "
             "value of a polynomial at a point. The lab prints it as a fraction when it "
             "is one."),
            ("The nullcline is where the slope is zero",
             "Set `f(t, y) = 0` and solve. For `y′ = t − y` that is `y = t`, a line. Along it every "
             "segment is flat, and a solution that reaches it has a horizontal tangent there. "
             "Segments above the nullcline slope one way and segments below slope the other, "
             "which is why it organises the whole picture."),
        ],
        "read_title": "Drawing an equation without solving it",
        "read_intro": "The grid, the slope at one point, the zero-slope curve, and a field in which the formula tells you a shortcut.",
        "body": [
            ("def", ("Slope field and nullcline",
                     "For the equation `y′ = f(t, y)`, the <strong>slope field</strong> is the "
                     "collection of short segments, one centred at each point of a grid, "
                     "whose slope is `f(t, y)` at that point.",
                     "The <strong>nullcline</strong> is the set of points where `f(t, y) = 0`, "
                     "the points whose segment is horizontal.")),
            ("p", "Take `y′ = t − y`. At `(2, 0)` the slope is `2 − 0 = 2`, so the segment "
                  "rises two for every one across. At `(1, 1)` it is `1 − 1 = 0`, so the "
                  "segment is flat. At `(0, 2)` it is `0 − 2 = −2`, and the segment falls "
                  "steeply. Three substitutions, three segments, and a grid of fifteen by "
                  "fifteen of them is that arithmetic repeated."),
            ("math", [
                "y′ = t − y",
                "",
                "point (t, y)     slope t − y",
                "(2, 0)           2",
                "(1, 1)           0",
                "(0, 2)           −2",
                "(3, 1)           2",
            ]),
            ("p", "The nullcline of `y′ = t − y` is found by setting the right side to zero: "
                  "`t − y = 0`, so `y = t`. Every point on that line, such as `(1, 1)` and "
                  "`(−2, −2)`, has a flat segment. The lab prints it in the tile "
                  "named Slope 0."),
            ("h3", "Fields that depend on one variable"),
            ("p", "Two special cases are worth recognising because the picture is then "
                  "regular. For `y′ = y`, the slope depends on `y` alone: at `(0, 1)` it is 1, "
                  "and it is 1 at every other point at height 1, so the segments in each "
                  "row are parallel copies. The nullcline is the line `y = 0`."),
            ("p", "For `y′ = 2t` the slope depends on `t` alone: at `(1, 2)` it is 2, and "
                  "it is 2 on the whole vertical line `t = 1`. The nullcline is the line "
                  "`t = 0`, and the lab prints it as `none in y` because no height `y` makes "
                  "the slope zero for every `t`; there is no equation to solve for `y`. "
                  "This is the equation of “What a Differential Equation Is”, and its solutions `t² + C` are "
                  "vertical shifts of one another, which is exactly what a field of identical "
                  "columns would let you see."),
            ("example", ("Reading one segment correctly",
                         "At `(2, 0)` on `y′ = t − y` the segment has slope 2.",
                         "That says a solution through `(2, 0)` is rising there at a rate "
                         "of 2. It does not say the solution goes on to `(3, 2)`: by then "
                         "the point is a different point with a different slope, `3 − 2 = 1`, "
                         "and the curve has bent. A segment is a tangent, the direction "
                         "of travel at that instant.")),
            ("p", "About the drawing: the segments and any curve are plotted with "
                  "floating-point numbers, and the legend says a solution is drawn. The slope "
                  "tile is computed exactly. If a number matters, read it from the tile."),
        ],
        "lab": ("dekit", {
            "mode": "field",
            "preset": "t-minus-y",
            "grid": "15",
            "presets": [
                {"id": "t-minus-y", "label": "y' = t - y at (1, 1)",
                 "f": "t - y", "window": [-3, 3, -3, 3], "start": [1, 1], "point": [1, 1], "expect": {"sfSlope": "0", "sfZero": "y = t"}},
                {"id": "y-only", "label": "y' = y at (0, 1)",
                 "f": "y", "window": [-3, 3, -3, 3], "start": None, "point": [0, 1], "expect": {"sfSlope": "1", "sfZero": "y = 0"}},
                {"id": "t-only", "label": "y' = 2t at (1, 2)",
                 "f": "2t", "window": [-3, 3, -3, 3], "start": None, "point": [1, 2], "expect": {"sfSlope": "2", "sfZero": "none in y"}},
            ],
            "panel_title": "A slope field, one exact slope, and the nullcline",
            "panel_intro": (
                "The segments are drawn at the grid points; the slope tile is the exact value of "
                "f at the point you type. Pick each preset, find the slope by hand first, and "
                "then compare. Change the point in the first preset to (2, 0) and expect a slope "
                "of 2."
            ),
        }),
        "steps_title": "Building the picture of an equation",
        "steps_intro": "From a right-hand side to a field you can read.",
        "steps": [
            ("Choose a window and a grid",
             "Decide the range of `t` and of `y` to show, and a grid of points inside it. A "
             "finer grid shows more detail and the same information."),
            ("Compute the slope at a point by substituting",
             "Put the `t` and `y` of the point into `f`. Do it exactly, as a fraction if "
             "need be, and write the number beside the point."),
            ("Draw the segment through the point",
             "A segment with that slope: rise `m` for a run of 1. Flat for `0`, rising for "
             "a positive number, falling for a negative one."),
            ("Find where the slope is zero",
             "Set `f(t, y) = 0` and solve for `y` where you can. That curve separates "
             "rising segments from falling ones, and it is the first thing to mark."),
        ],
        "worked": {
            "title": "y′ = t − y at three points, and its nullcline",
            "intro": [
                "Compute the slopes at `(2, 0)`, `(1, 1)` and `(0, 2)`, then find where the slope "
                "is zero.",
            ],
            "lines": [
                "f(t, y) = t − y",
                "",
                "(2, 0):   2 − 0 =  2     rising",
                "(1, 1):   1 − 1 =  0     flat",
                "(0, 2):   0 − 2 = −2     falling",
                "",
                "slope 0:  t − y = 0,  so y = t",
                "above the line, y > t:  t − y is negative, falling",
                "below the line, y < t:  t − y is positive, rising",
            ],
            "after": [
                "The three points straddle the line `y = t`: `(2, 0)` is below it with a "
                "positive slope, `(0, 2)` is above it with a negative slope, and `(1, 1)` is on "
                "it with slope zero. Every solution crosses that line horizontally, which is "
                "a statement about the whole family and was read from a single "
                "equation, `t − y = 0`.",
                "For a rehearsal, work out the slope at `(3, 1)` yourself, then look at "
                "the preset: `3 − 1 = 2`.",
            ],
        },
        "quiz_title": "Slopes, segments and the nullcline",
        "quiz": [
            {"q": "For `y′ = t − y`, what is the slope of the field at `(3, 1)`?",
             "a": ["2", "4", "−2", "3"],
             "c": 0,
             "why": "Substitute `t = 3` and `y = 1`: `3 − 1 = 2`. The value `4` adds the "
                    "coordinates, `−2` swaps the order, and `3` forgets the `y` term."},
            {"q": "Which point lies on the nullcline of `y′ = t − y`?",
             "a": ["`(0, 1)`", "`(4, 3)`", "`(−2, −2)`", "`(1, 0)`"],
             "c": 2,
             "why": "The nullcline is `y = t`, where `t − y = 0`. Of the points listed only "
                    "`(−2, −2)` has equal coordinates; the others give slopes `−1`, `1` and `1`."},
            {"q": "At `(2, 0)` the slope field of `y′ = t − y` has slope 2. What does that tell you about the solution through `(2, 0)`?",
             "a": ["It next passes through `(3, 2)`",
                   "Its tangent at that point has slope 2",
                   "It stays at slope 2 for all later `t`",
                   "It reaches `y = 2` at `t = 2`"],
             "c": 1,
             "why": "A segment is the direction of the curve at the point itself. A "
                    "tangent of slope 2 does not carry the curve to `(3, 2)`, because the "
                    "slope changes as the curve moves, and the field has a different value at "
                    "every later point."},
            {"q": "For `y′ = 2t` the lab prints `none in y` for the nullcline. Why?",
             "a": ["The slope is never zero",
                   "The slope is zero only at `t = 0`, and no height `y` changes that; there is nothing to solve for `y`",
                   "The slope is zero for every `y`",
                   "The equation has no solutions"],
             "c": 1,
             "why": "The right side `2t` does not contain `y`, so setting it to zero gives "
                    "`t = 0`, a vertical line, not a curve `y = …`. The slope is zero on that "
                    "line and the equation has solutions, so the other options are wrong."},
        ],
        "mistakes": [
            ("Reading a segment as where the solution goes next, rather than its slope there",
             "The segment at `(2, 0)` on `y′ = t − y` has slope 2 and it is a tangent. The "
             "slope at the next point of the curve is a different number from the field, "
             "so the curve bends, and joining segments end to end is Euler's method, "
             "which the stepping half of this course shows is only approximate."),
            ("Confusing the slope with the value of y",
             "The number the field gives at `(1, 1)` is `0`, the slope, and the point is at "
             "height 1. A flat segment at a high point and a steep segment at a low point "
             "are both normal."),
            ("Expecting the nullcline to be a solution",
             "Where `f = 0` the segments are flat, but a solution that touches the line "
             "`y = t` carries on and leaves it, because the slope changes with the point. "
             "A horizontal solution needs `f = 0` along the whole line `y = c` for every "
             "`t`; that is a stronger condition."),
        ],
        "standard": ("Finish when you can compute a slope at a point exactly, draw its segment, and find the nullcline.",
                     "You should be able to substitute a point into `f(t, y)` and write the "
                     "slope as a fraction or integer, sketch the segment for a positive, "
                     "negative or zero slope, solve `f(t, y) = 0` for the nullcline of a "
                     "right side that is linear in `y`, and say what a segment shows and what "
                     "it does not."),
        "note": 'The picture is drawn. The next lesson reads it: which curves are solutions that stay put, where solutions head, and what can never happen, and also what the picture can only suggest. &ldquo;Reading a Slope Field&rdquo; does it.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "reading-a-slope-field",
        "title": "Reading a Slope Field",
        "module": "Pictures of solutions",
        "one_line": "Read horizontal solutions, long-run behaviour and where solutions cannot cross off a slope field, and say which of those the field settles and which it only suggests.",
        "summary": (
            "A slope field can be read at three levels of confidence. Some things follow from "
            "the arithmetic of the slope: a horizontal solution, the direction of travel on "
            "each side of it, and the fact that two solutions cannot cross. Some things the "
            "picture only suggests: where a curve is heading in the long run, and whether "
            "it leaves the window because it grows large or because it ends. Reading well "
            "means keeping the two apart."
        ),
        "key": [
            "y′ = y·(1 − y): slope 0 on y = 0, y = 1",
            "between 0 and 1 rising;  outside, falling",
            "two solutions cannot cross: one slope",
            "settled: the sign of the slope, y = c",
            "only suggested: the far future",
        ],
        "key_label": "What a slope field settles, and what it only suggests",
        "concepts_intro": (
            "Three kinds of reading, from the surest to the least sure."
        ),
        "concepts": [
            ("A horizontal solution is a line y = c where f is zero for every t",
             "If `f(t, c) = 0` for all `t`, the constant function `y = c` has derivative "
             "zero and the equation says its slope should be zero, so it is a solution. For "
             "`y′ = y·(1 − y)` the right side vanishes at `y = 0` and at `y = 1`, and both "
             "lines are solutions. This is settled by arithmetic, and the lab lists them."),
            ("Solutions do not cross, and here they do not touch",
             "At a point the field has one slope, so two solutions through the same point "
             "with different slopes are impossible: that much the arithmetic settles. A curve "
             "that reached a horizontal solution would arrive flat, with the same slope `0`, "
             "and ruling that out takes one more fact: through a given point there is exactly "
             "one solution. This course states it, uses it and does not prove it; it holds "
             "for every polynomial right side, so a curve that starts between two horizontal "
             "solutions stays between them."),
            ("The long-run behaviour is suggested by the picture, not proved by it",
             "Where a curve is heading as `t` grows is something you see, and the sign of the "
             "slope supports it, but the field does not prove a limit. A curve between "
             "`y = 0` and `y = 1` is rising and cannot reach `1`; that it approaches `1` "
             "is what the picture suggests and Equilibria, Stability and Phase Lines "
             "establishes."),
        ],
        "read_title": "Three things to read, and how much each is worth",
        "read_intro": "The horizontal solutions, the sign of the slope between them, the no-crossing rule, and two fields where reading further would be a mistake.",
        "body": [
            ("p", "Start with `y′ = y·(1 − y)`. The right side is a product, and a product is "
                  "zero when either factor is. So the slope is `0` exactly where `y = 0` or "
                  "`y = 1`, at every `t`: both lines are horizontal solutions, and "
                  "the lab lists them in the tile named Horizontal solutions."),
            ("p", "Between the lines and outside them the sign of the slope is fixed. For "
                  "`y` between 0 and 1 both factors `y` and `1 − y` are positive, so the "
                  "slope is positive and the segments rise. For `y` above 1 the factor `1 − y` "
                  "is negative and the slope is negative. For `y` below 0 the factor `y` is "
                  "negative and `1 − y` is positive, so the slope is negative again."),
            ("math", [
                "y′ = y·(1 − y)",
                "",
                "range of y     sign of y     sign of 1 − y     slope",
                "y < 0          −             +                 falling",
                "y = 0          0             +                 0",
                "0 < y < 1      +             +                 rising",
                "y = 1          +             0                 0",
                "y > 1          +             −                 falling",
            ]),
            ("h3", "Why curves do not cross, and what that gives"),
            ("p", "A solution that starts at `y = 1/2` rises, because the slope there is "
                  "positive. Could it reach `y = 1`? Not by crossing at an angle: the field "
                  "gives one slope at each point, and two curves through one point with two "
                  "slopes cannot both be solutions. But a curve that reached `y = 1` would "
                  "arrive flat, since the slope there is `0` by the equation, and the "
                  "one-slope argument has nothing to say against that. What rules it out is "
                  "the uniqueness claim: through a given point there is exactly one solution, "
                  "and the horizontal line is already it. For a polynomial right side the "
                  "claim holds, and with it a solution that starts below `1` stays below it "
                  "for ever, and the same argument keeps it above `0`."),
            ("thm", ("The no-crossing claim",
                     "Two different solutions of `y′ = f(t, y)` never cross at an angle, "
                     "because they would need two slopes at one point. For the equations of "
                     "this course they never touch either: through each point there is "
                     "exactly one solution, which is the uniqueness statement of “Blow-Up and "
                     "the Interval of Existence”.")),
            ("p", "The first sentence is settled by the arithmetic of the slope, and the lab "
                  "demonstrates it. The second is a claim this course states, uses and does "
                  "not prove; it is what makes a horizontal solution a wall and not merely a "
                  "line of flat segments. For the rest of this course, take both as the "
                  "working rule."),
            ("h3", "A field where the curve approaches a line"),
            ("p", "In the second preset the equation is `y′ = t − y` and the drawn solution "
                  "starts at `(0, 2)`. The line `y = t − 1` is itself a solution: its "
                  "derivative is `1`, and `t − (t − 1) = 1`, so the residual is zero, by the "
                  "test of “What a Differential Equation Is”. The drawn curve bends towards that line. "
                  "That is what the picture suggests; First-Order Linear Equations "
                  "is where the claim is established."),
            ("example", ("A curve that leaves the window",
                         "Take `y′ = y²` with the solution through `(0, 1)`, and look at the "
                         "third preset. The drawn curve climbs, steeper and steeper, and "
                         "leaves the window before `t = 1`.",
                         "What the field supports: the slope `y²` is never negative, so the "
                         "curve never falls, and it grows steeper as `y` grows. What it does "
                         "not settle is whether the curve is merely large at the window's edge "
                         "or has stopped existing there. “Blow-Up and the Interval of "
                         "Existence” answers that.")),
            ("p", "Hold that distinction in the examples that follow. The arithmetic of the "
                  "slope settles the horizontal solutions, the sign on each side and the "
                  "no-crossing rule. The look of the picture suggests the far future, and "
                  "the drawn curve is a floating-point drawing that says so in the legend."),
        ],
        "lab": ("dekit", {
            "mode": "field",
            "preset": "logistic",
            "grid": "15",
            "presets": [
                {"id": "logistic", "label": "y' = y(1 - y), start (0, 1/2)",
                 "f": "y*(1 - y)", "window": [-1, 5, -1, 2], "start": [0, "1/2"], "point": [0, "1/2"], "expect": {"sfEquil": "y = 0, y = 1", "sfSlope": "1/4"}},
                {"id": "t-minus-y", "label": "y' = t - y, start (0, 2)",
                 "f": "t - y", "window": [-1, 5, -2, 4], "start": [0, 2], "point": [0, 2], "expect": {"sfEquil": "none", "sfSlope": "−2"}},
                {"id": "square", "label": "y' = y^2, start (0, 1)",
                 "f": "y^2", "window": [-1, 2, -2, 4], "start": [0, 1], "point": [0, 1], "expect": {"sfEquil": "y = 0", "sfSlope": "1"}},
            ],
            "panel_title": "Horizontal solutions, signs and a drawn curve",
            "panel_intro": (
                "The tile for horizontal solutions is exact; the curve is drawn by stepping "
                "in floating point and the legend says so. For each preset write down what the "
                "field settles before you look at the curve, then what the curve suggests."
            ),
        }),
        "steps_title": "Reading a field you have been given",
        "steps_intro": "Settled things first, suggested things last, and the line between them written down.",
        "steps": [
            ("Find the horizontal solutions",
             "Solve `f(t, c) = 0` for all `t`. When `f` has no `t`, these are the roots of "
             "`f` in `y`. Mark each line `y = c`."),
            ("Read the sign of the slope in each region",
             "Between and beyond the horizontal solutions, decide whether `f` is "
             "positive or negative, by testing one point or by signs of factors. That is "
             "the direction of travel in the region."),
            ("Apply the no-crossing rule",
             "A solution that starts in a region between two horizontal solutions stays in "
             "it: one slope per point forbids a crossing, and the uniqueness claim forbids a "
             "touch. State what that bounds."),
            ("Sketch the long-run behaviour and label it a suggestion",
             "Draw where the curves seem to head, and write beside it that this is read "
             "from the picture and not proved by it. Do not state a limit as a fact."),
        ],
        "worked": {
            "title": "y′ = y·(1 − y), start at y = 1/2",
            "intro": [
                "Read the field of `y′ = y·(1 − y)` and say what happens to a solution that "
                "starts at `y = 1/2`.",
            ],
            "lines": [
                "slope = 0 when y·(1 − y) = 0:  y = 0 or y = 1",
                "",
                "y < 0:      y negative, 1 − y positive:  slope negative",
                "0 < y < 1:  both factors positive:  slope positive",
                "y > 1:      y positive, 1 − y negative:  slope negative",
                "",
                "start y = 1/2:  slope = (1/2)·(1/2) = 1/4, rising",
                "reaching y = 1 would put two solutions through one point",
                "falling to y = 0 would do the same",
            ],
            "after": [
                "What the arithmetic settled: the two horizontal solutions and the direction "
                "of travel in each region. What the uniqueness claim adds: the curve from "
                "`1/2` stays strictly between `0` and `1`, because meeting either line would "
                "put two solutions through one point. What the picture only suggests is that "
                "the curve climbs towards `1`. Rising and bounded above does not by itself "
                "fix where it ends, and the picture shows it levelling off without proving it.",
                "For a rehearsal, take a start at `y = 2`. The slope there is `2·(1 − 2) = −2`, "
                "so the curve falls, and by the same argument it stays above `1`.",
            ],
        },
        "quiz_title": "Settled and suggested",
        "quiz": [
            {"q": "Two curves in a sketch of `y′ = t − y` cross at `(2, 0)` with different slopes. What is wrong?",
             "a": ["Nothing: solutions cross wherever the slope is large",
                   "Nothing: solutions cross at points on the nullcline",
                   "The field has one slope at `(2, 0)`, so two curves with different slopes cannot both be solutions",
                   "Curves must cross at least once per unit of `t`"],
             "c": 2,
             "why": "The slope at `(2, 0)` is `2 − 0 = 2`. A solution through that point must "
                    "have slope 2 there, and two curves crossing at an angle would have two "
                    "different slopes. Neither the steepness nor the nullcline has any bearing."},
            {"q": "For `y′ = y·(1 − y)`, a solution starts at `y = 3`. Which statement do the sign of the slope and the no-crossing rule settle?",
             "a": ["It reaches `y = 1` at some finite `t`",
                   "It levels off at exactly `y = 1` after a finite time",
                   "It crosses below `y = 0`",
                   "It falls at the start and stays above `y = 1`"],
             "c": 3,
             "why": "At `y = 3` the slope is `3·(1 − 3) = −6`, so it falls; and it cannot reach "
                    "the horizontal solution `y = 1`, because through each point there is one "
                    "solution and the line is already it. Reaching `1`, levelling at `1` in "
                    "finite time, or crossing `0` all require meeting a horizontal solution."},
            {"q": "On `y′ = y²`, the drawn solution through `(0, 1)` leaves the window before `t = 1`. Which conclusion does the arithmetic of the slope settle?",
             "a": ["The solution ceases to exist at `t = 1`",
                   "The solution is a straight line",
                   "The curve rises more and more steeply, and the slope is never negative",
                   "The curve crosses `y = 0`"],
             "c": 2,
             "why": "The slope `y²` is never negative, and it grows as `y` grows, so the "
                    "curve climbs ever more steeply. That the solution ceases to exist at "
                    "`t = 1` happens to be true, and “Blow-Up and the Interval of Existence” "
                    "shows it with a formula and a check; nothing in the sign of the slope, "
                    "or in a drawing that goes off the edge, settles it. It is not a line, and "
                    "it cannot cross the horizontal solution `y = 0`."},
            {"q": "What are the horizontal solutions of `y′ = y²`?",
             "a": ["`y = 0` only", "`y = 1` only", "`y = 0` and `y = 1`", "None"],
             "c": 0,
             "why": "The right side `y²` is zero only at `y = 0`, so that line is the only "
                    "horizontal solution. At `y = 1` the slope is `1`, not zero, so the "
                    "curve through `(0, 1)` is not horizontal."},
        ],
        "mistakes": [
            ("Letting solution curves cross",
             "At each point the field has a single slope, so two solutions through the same "
             "point with different slopes cannot both exist; and for the equations here two "
             "solutions through one point are the same solution, so a curve cannot even "
             "touch a horizontal one. On `y′ = y·(1 − y)` that is why a curve from `1/2` can "
             "never reach `1` or `0`; a sketch with a crossing has an error in it."),
            ("Stating a limit as something the picture proved",
             "The curve from `1/2` seems to level off at `1`, and the field supports that, "
             "but a drawing is a floating-point curve and shows a tendency. Say that the "
             "far future is suggested, and write what has been settled separately."),
            ("Treating a curve that leaves the window as one that blows up",
             "On `y′ = y²` the curve through `(0, 1)` leaves the window, and it could have "
             "merely become large. The field cannot tell the two apart, and the next lessons "
             "show how a formula or a step method answers."),
        ],
        "standard": ("Finish when you can list what a slope field settles, and what it only suggests, for an equation you are given.",
                     "You should be able to find the horizontal solutions of an equation with no "
                     "`t` in it, read the sign of the slope in each region, apply the "
                     "no-crossing rule to bound a solution, and state which of your conclusions "
                     "come from the arithmetic and which only from the look of a drawn curve."),
        "note": 'Segments end to end give a path, and the question of how good a path is leads to a method. The stepping half of this course starts from the slope at the start and moves along it by a step, again and again, in exact fractions. &ldquo;Euler&rsquo;s Method&rdquo; is where.',
    },
]
