"""Second-Order Linear Equations -- the second half.

Complex roots and oscillation, fitting the two constants from the starting value
and rate, superposition and the Wronskian, the equation rewritten as a system,
and Euler's method on the oscillator.

Every figure below is read off the labs, scripts/mathpath/labs/dekit_b.py (modes
char and phase), by executing their shipped JavaScript under node, and pinned in
`expect`. A figure that is rounded is printed with the approximation sign and
says so; everything else is an exact fraction, an exact surd or an exact
symbolic expression.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "complex-roots-and-oscillation",
        "title": "Complex Roots and Oscillation",
        "module": "The characteristic equation",
        "one_line": "Turn the roots α ± βi into e^(αt)·(C₁·cos(βt) + C₂·sin(βt)), verify it exactly, and read the oscillation speed and the decay rate off the root.",
        "summary": (
            "When the discriminant is negative the characteristic quadratic has a "
            "complex pair `α ± βi`, and the solutions of the equation are real "
            "functions all the same: an exponential `e^(αt)` multiplied by a cosine "
            "and a sine of `βt`. The real part `α` decides whether the oscillation "
            "shrinks, stays level or grows, and `β` decides how fast it turns. The "
            "lab fits the two constants and checks the result by substitution."
        ),
        "key": [
            "disc negative:  roots  α ± βi,  β positive",
            "y = e^(αt)·(C₁·cos(βt) + C₂·sin(βt))",
            "α negative shrinks,  α = 0 keeps its size",
            "α positive grows;  one turn takes 2π/β",
            "y(0) = C₁,   y′(0) = α·C₁ + β·C₂",
            "the roots are complex, the solution is real",
        ],
        "key_label": "The real part of the root is the envelope",
        "concepts_intro": (
            "Three ideas: what a complex root hands over, why the answer is still a "
            "real function, and what the two parts of the root mean for the motion."
        ),
        "concepts": [
            ("A complex pair is two real numbers",
             "The quadratic formula gives `r = (−b ± √(b² − 4ac))/(2a)`, and when the "
             "discriminant is negative the square root is `β` times `i` for a real "
             "`β`. The two roots are then `α + βi` and `α − βi`, with the real part "
             "`α = −b/(2a)` in both. Only two real numbers, `α` and `β`, are needed "
             "to write the solution."),
            ("The solutions are an exponential times a cosine and a sine",
             "Both `e^(αt)·cos(βt)` and `e^(αt)·sin(βt)` satisfy "
             "`a·y″ + b·y′ + c·y = 0`, and the lab checks each by substitution "
             "with no `i` in sight. The general solution has a constant on each. "
             "It is real whenever the constants are real."),
            ("The real part is the envelope and the imaginary part is the speed",
             "The factor `e^(αt)` multiplies everything: it shrinks the oscillation "
             "when `α` is negative, leaves its size alone when `α` is zero and "
             "grows it when `α` is positive. The cosine and sine turn once "
             "every `2π/β` units of `t`, so a larger `β` is a faster oscillation."),
        ],
        "read_title": "Roots that are not real, and solutions that are",
        "read_intro": "The form of the answer, a proof that it works with algebra the reader has, a hand check, and the three shapes the real part can give.",
        "body": [
            ("p", "Take `y″ + 2y′ + 5y = 0`. The discriminant is `4 − 20 = −16`, so "
                  "the roots are `(−2 ± 4i)/2 = −1 ± 2i`. There is no real number "
                  "that solves the characteristic quadratic, and it is tempting to "
                  "conclude that no real function solves the equation. The "
                  "conclusion does not follow: the roots are numbers that satisfy "
                  "a quadratic, and the solutions are functions of `t` built from "
                  "them."),
            ("p", "The reason a cosine and a sine appear is that an exponential with an "
                  "imaginary exponent is a cosine plus `i` times a sine. This course "
                  "does not use that identity, because the answer can be checked "
                  "directly, which is the standard throughout: a candidate is a "
                  "solution when its residual is zero."),
            ("thm", ("The solutions for a complex pair",
                     "If `a·r² + b·r + c = 0` has the roots `α ± βi` with `α` and `β` "
                     "real and `β` not zero, then `e^(αt)·cos(βt)` and "
                     "`e^(αt)·sin(βt)` both solve `a·y″ + b·y′ + c·y = 0`, and the "
                     "general solution is `e^(αt)·(C₁·cos(βt) + C₂·sin(βt))`.")),
            ("proof", ["Take `y = e^(αt)·cos(βt)`. The product rule, with the chain rule "
                       "supplying the factor `β` in front of the sine, gives "
                       "`y′ = e^(αt)·(α·cos(βt) − β·sin(βt))` and "
                       "`y″ = e^(αt)·((α² − β²)·cos(βt) − 2·α·β·sin(βt))`. "
                       "Then `a·y″ + b·y′ + c·y` equals `e^(αt)` times "
                       "`(a·(α² − β²) + b·α + c)·cos(βt) − β·(2a·α + b)·sin(βt)`.",
                       "The root pair has real part `α = −b/(2a)`, so `2a·α + b = 0` and "
                       "the sine term vanishes. It also has product `α² + β² = c/a`, "
                       "since `(α + βi)·(α − βi) = α² + β²`. With `b = −2a·α` the "
                       "cosine bracket is `a·α² − a·β² − 2a·α² + c = c − a·(α² + β²)`, "
                       "which is `0`.",
                       "The sine case is the same computation with the roles of the two "
                       "terms exchanged. That these two functions are all the "
                       "solutions is stated here and not proved; &ldquo;Superposition and "
                       "the Wronskian&rdquo; shows why they can fit any starting value and rate."]),
            ("h3", "A check by hand"),
            ("p", "For `y″ + 2y′ + 5y = 0` the roots give `α = −1` and `β = 2`. Take "
                  "the sine solution `y = e^(−t)·sin(2t)`. Its rates, by the product "
                  "rule, are below, and the cosine terms and the sine terms of the "
                  "residual each cancel exactly."),
            ("math", [
                "y = e^(−t)·sin(2t)",
                "y′ = e^(−t)·(2·cos(2t) − sin(2t))",
                "y″ = e^(−t)·(−4·cos(2t) − 3·sin(2t))",
                "cosine terms of y″ + 2y′ + 5y:  −4 + 2·2 + 0 = 0",
                "sine terms of y″ + 2y′ + 5y:    −3 + 2·(−1) + 5 = 0",
            ]),
            ("h3", "Reading the motion from the root"),
            ("p", "The same equation has the envelope `e^(−t)` and turns at speed `2`, "
                  "so one full turn takes `π` units of `t`. The lab's three presets "
                  "have three different real parts. The first, `α = −1`, shrinks. "
                  "The second is `y″ + 4y = 0`, with `α = 0`: it neither shrinks "
                  "nor grows and keeps its size for ever. The third has `α = 1` "
                  "and grows."),
            ("example", ("A growing oscillation",
                         "For `y″ − 2y′ + 2y = 0` the discriminant is `4 − 8 = −4` and "
                         "the roots are `1 ± i`, so `α = 1` and `β = 1`. The general "
                         "solution is `e^t·(C₁·cos t + C₂·sin t)`.",
                         "With `y(0) = 1` and `y′(0) = 0` the first condition gives "
                         "`C₁ = 1` and the second is `α·C₁ + β·C₂ = 1 + C₂ = 0`, so "
                         "`C₂ = −1`. The solution turns once every `2π` and its size "
                         "multiplies by `e` each time `t` increases by `1`.")),
            ("p", "That last sentence is the whole content of the real part. A spring "
                  "that loses energy to friction is described by a solution with "
                  "a negative `α`, and one that is driven harder at every swing has "
                  "a positive `α`. The next course measures both."),
        ],
        "lab": ("dekit", {
            "mode": "char",
            "view": "solution",
            "preset": "damped",
            "presets": [
                {"id": "damped", "label": "y″ + 2y′ + 5y = 0, y(0) = 0, y′(0) = 2",
                 "a": 1, "b": 2, "c": 5, "ic": [0, 2], "expect": {"ceRoots": "−1 ± 2i", "ceGeneral": "e^(−t)·(C₁·cos(2t) + C₂·sin(2t))", "ceSolution": "e^(−t)·sin(2t)"}},
                {"id": "pure", "label": "y″ + 4y = 0, y(0) = 3, y′(0) = −4",
                 "a": 1, "b": 0, "c": 4, "ic": [3, -4], "expect": {"ceRoots": "±2i", "ceGeneral": "C₁·cos(2t) + C₂·sin(2t)", "ceSolution": "3·cos(2t) − 2·sin(2t)"}},
                {"id": "growing", "label": "y″ − 2y′ + 2y = 0, y(0) = 1, y′(0) = 0",
                 "a": 1, "b": -2, "c": 2, "ic": [1, 0], "expect": {"ceRoots": "1 ± i", "ceGeneral": "e^t·(C₁·cos(t) + C₂·sin(t))", "ceC": "C₁ = 1, C₂ = −1", "ceSolution": "e^t·cos(t) − e^t·sin(t)"}},
            ],
            "panel_title": "A complex pair, and the real solution it gives",
            "panel_intro": (
                "Choose a preset and read the roots, the general solution and the "
                "fitted solution. The status line gives the residual, which is 0 when "
                "the solution is substituted back. Then change b and watch the real "
                "part of the root move from negative through zero to positive."
            ),
        }),
        "steps_title": "Solving with a complex pair",
        "steps_intro": "Five moves. The first three are about the root, and the last two are the fit and the check.",
        "steps": [
            ("Confirm the discriminant is negative",
             "`b² − 4ac < 0`. Then there is no real root, and the roots come as a pair."),
            ("Read α and β off the roots",
             "`α = −b/(2a)` is the real part and `β` is the positive number in "
             "front of `i`. For `−1 ± 2i` they are `−1` and `2`."),
            ("Write the general solution",
             "`e^(αt)·(C₁·cos(βt) + C₂·sin(βt))`. Keep the exponential factor; it "
             "is what the real part contributes."),
            ("Fit the constants",
             "`C₁ = y(0)`, and `α·C₁ + β·C₂ = y′(0)` gives `C₂`. The division by "
             "`β` is the step most often skipped."),
            ("Substitute back",
             "Differentiate twice by the product rule and read the residual. A "
             "missing factor of `e^(αt)` fails here at once."),
        ],
        "worked": {
            "title": "y″ + 2y′ + 5y = 0 with y(0) = 0 and y′(0) = 2",
            "intro": [
                "A complex pair, the general real solution, and a two-condition fit.",
            ],
            "lines": [
                "disc = 4 − 20 = −16,   r = −1 ± 2i",
                "α = −1,   β = 2",
                "y = e^(−t)·(C₁·cos(2t) + C₂·sin(2t))",
                "y(0) = C₁ = 0",
                "y′(0) = −C₁ + 2·C₂ = 2,   C₂ = 1",
                "y = e^(−t)·sin(2t)",
                "residual y″ + 2y′ + 5y = 0",
            ],
            "after": [
                "The fourth line is the first condition, since `cos 0 = 1` and "
                "`sin 0 = 0`. The fifth is the rate of the general solution at "
                "`t = 0`, which picks up `α·C₁` from the exponential and `β·C₂` "
                "from the sine.",
                "The solution starts at `0`, rises, and turns back as the factor "
                "`e^(−t)` shrinks the swing. The lab prints the residual `0` in its "
                "status line, so the answer is exact and not an approximation.",
            ],
        },
        "quiz_title": "Complex pairs, real solutions",
        "quiz": [
            {"q": "The characteristic equation of an equation has the roots `−3 ± 4i`. What is the general solution?",
             "a": ["`C₁·cos(4t) + C₂·sin(4t)`",
                   "`e^(4t)·(C₁·cos(3t) + C₂·sin(3t))`",
                   "`e^(−3t)·(C₁·cos(4t) + C₂·sin(4t))`",
                   "`C₁·e^(−3t) + C₂·e^(4t)`"],
             "c": 2,
             "why": "The real part `−3` goes into the exponential and the imaginary part "
                    "`4` into the cosine and sine. The first answer leaves out the "
                    "exponential. The second swaps the two parts. The last treats "
                    "`−3` and `4` as two real roots, which they are not."},
            {"q": "For `y″ + 4y = 0` the roots are `±2i`. How does a solution behave as `t` grows?",
             "a": ["It decays to `0`, since the roots are not real",
                   "It grows without bound, since `2` is positive",
                   "It tends to a constant",
                   "It keeps oscillating at the same size"],
             "c": 3,
             "why": "The real part is `α = 0`, so the envelope `e^(0·t) = 1` neither "
                    "shrinks nor grows. A decay needs a negative real part and growth "
                    "a positive one. The imaginary part `2` sets the speed, not the "
                    "size, and a pure oscillation does not settle to a constant."},
            {"q": "For `y″ + 2y′ + 5y = 0` with `y(0) = 1` and `y′(0) = 0`, which constants fit `e^(−t)·(C₁·cos(2t) + C₂·sin(2t))`?",
             "a": ["`C₁ = 1`, `C₂ = 0`",
                   "`C₁ = 1`, `C₂ = 1/2`",
                   "`C₁ = 1`, `C₂ = −1/2`",
                   "`C₁ = 1`, `C₂ = 2`"],
             "c": 1,
             "why": "`C₁ = y(0) = 1`, and `y′(0) = −C₁ + 2·C₂ = 0` gives `C₂ = 1/2`. Taking "
                    "`C₂ = y′(0) = 0` forgets that the exponential contributes "
                    "`−C₁`. The value `−1/2` has the sign of that contribution "
                    "reversed, and `2` multiplies by `β` instead of dividing by it."},
            {"q": "Which equation has solutions that oscillate and grow in size?",
             "a": ["`y″ − 2y′ + 2y = 0`",
                   "`y″ + 2y′ + 2y = 0`",
                   "`y″ + 4y = 0`",
                   "`y″ − 3y′ + 2y = 0`"],
             "c": 0,
             "why": "The first has the roots `1 ± i`, a positive real part and a "
                    "nonzero imaginary part. The second has `−1 ± i`, which "
                    "oscillates and shrinks. The third has `±2i`, which oscillates at "
                    "a constant size. The last has the real roots `1` and `2`, "
                    "which grow without oscillating."},
        ],
        "mistakes": [
            ("Concluding that a complex root means the equation has no real solution",
             "The roots `−1 ± 2i` are numbers that satisfy the quadratic, not values "
             "of the unknown. The function `e^(−t)·sin(2t)` is real for every real "
             "`t`, starts at `y(0) = 0` and has rate `y′(0) = 2`, and the lab "
             "reports a residual of exactly `0` for it. The imaginary part of the "
             "root becomes the speed of a cosine and a sine, and no `i` appears in "
             "the solution."),
            ("Dropping the exponential and keeping only the cosine and sine",
             "For `−1 ± 2i` it is tempting to write `C₁·cos(2t) + C₂·sin(2t)`. "
             "Substituting `cos(2t)` into `y″ + 2y′ + 5y` gives "
             "`−4·cos(2t) − 4·sin(2t) + 5·cos(2t) = cos(2t) − 4·sin(2t)`, which is "
             "not zero. Only for a root with real part `0` is the exponential "
             "factor `1` and safe to leave out."),
            ("Reading C₂ as the starting rate",
             "Since `y′(0) = α·C₁ + β·C₂`, the constant `C₂` is "
             "`(y′(0) − α·C₁)/β`. For `y(0) = 1`, `y′(0) = 0` and the root "
             "`−1 ± 2i` that is `(0 + 1)/2 = 1/2`. Taking `C₂ = y′(0) = 0` gives "
             "`e^(−t)·cos(2t)`, whose rate at `0` is `−1`, not `0`."),
        ],
        "standard": (
            "Finish when you can solve an equation whose characteristic quadratic has complex roots, fit both constants, and read the motion off the roots.",
            "You should be able to compute a negative discriminant, read α and β "
            "from the roots, write e^(αt)·(C₁·cos(βt) + C₂·sin(βt)), fit C₁ and C₂ "
            "from y(0) and y′(0), and say whether the oscillation shrinks, stays "
            "level or grows."),
        "note": 'Every kind of root has now been turned into a solution. &ldquo;Fitting the Initial Conditions&rdquo; collects the three fits into one picture, a pair of linear equations for the constants, and says when the lab will and will not solve them.',
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "fitting-the-initial-conditions",
        "title": "Fitting the Initial Conditions",
        "module": "Fitting the constants",
        "one_line": "Set up the two linear equations for C₁ and C₂ from y(0) and y′(0), solve them exactly, and say when the lab declines and why that is a limit of its arithmetic and not of the method.",
        "summary": (
            "Whatever kind of root the equation has, the starting value and the starting "
            "rate give two linear equations for the two constants, because at "
            "`t = 0` every exponential is `1`, `cos` is `1` and `sin` is `0`. The "
            "equations differ only in a few entries, and they are solved by "
            "elimination with exact fractions. When the roots are irrational the "
            "constants would be surds, and the lab declines to fit them and says so."
        ),
        "key": [
            "real roots:  C₁ + C₂ = y(0)",
            "and  r₁·C₁ + r₂·C₂ = y′(0)",
            "repeated:  C₁ = y(0),  r·C₁ + C₂ = y′(0)",
            "complex:  C₁ = y(0),  α·C₁ + β·C₂ = y′(0)",
            "y′(0) is the starting rate, not 0",
            "irrational roots: the lab prints a dash",
        ],
        "key_label": "Two numbers in, two equations out",
        "concepts_intro": (
            "Three ideas: each starting number is one equation, the three kinds of "
            "root change only a few entries of the pair, and a dash from the lab "
            "has a specific meaning."
        ),
        "concepts": [
            ("Each starting number is one equation in C₁ and C₂",
             "The general solution is a formula in `t`, `C₁` and `C₂`. Putting "
             "`t = 0` in it gives `y(0)`, and putting `t = 0` in its rate gives "
             "`y′(0)`. Each is a linear expression in `C₁` and `C₂`, so two starting "
             "numbers give two linear equations in two unknowns."),
            ("At t = 0 the exponential is 1, cosine is 1 and sine is 0",
             "That is why the pair is short. For two real roots the first equation "
             "is `C₁ + C₂ = y(0)`; for a repeated root it is `C₁ = y(0)`; for a "
             "complex pair it is again `C₁ = y(0)`. The second equation carries "
             "the roots, because the rate of `e^(rt)` at `0` is `r`."),
            ("A dash means the lab declined, not that no fit exists",
             "When the roots contain a square root the constants do too, and the "
             "lab fits only rational constants. It prints a dash and gives the "
             "reason in its status line. The two equations still have an exact "
             "solution; it is a number the lab does not print."),
        ],
        "read_title": "The two equations, and what the lab will solve",
        "read_intro": "The pair for each kind of root, a general solution of the real case by elimination, a complex fit, and the case the lab declines.",
        "body": [
            ("p", "Every earlier lesson on this course ended by fitting two constants, "
                  "and each did it in one line. This lesson shows that the lines are "
                  "one computation. The unknowns are `C₁` and `C₂`, the data are the "
                  "starting value `y(0)` and the starting rate `y′(0)`, and the "
                  "equations come from putting `t = 0` in the general solution and "
                  "in its rate."),
            ("math", [
                "real roots r₁, r₂:    C₁ + C₂ = y(0)",
                "                      r₁·C₁ + r₂·C₂ = y′(0)",
                "repeated root r:      C₁ = y(0)",
                "                      r·C₁ + C₂ = y′(0)",
                "complex α ± βi:       C₁ = y(0)",
                "                      α·C₁ + β·C₂ = y′(0)",
            ]),
            ("p", "Read the second line of each pair as &ldquo;the rate at the start&rdquo;. For "
                  "two exponentials it adds the roots in proportion to the constants. "
                  "For the repeated root, the product rule on `(C₁ + C₂·t)·e^(rt)` at "
                  "`t = 0` gives `r·C₁ + C₂`. For the complex pair, the product rule "
                  "on the exponential and the cosine and sine at `t = 0` gives "
                  "`α·C₁ + β·C₂`."),
            ("h3", "Eliminating, once, for two real roots"),
            ("p", "Multiply the first equation by `r₂` and subtract it from the "
                  "second, then multiply the first by `r₁` and subtract the "
                  "second from it. The unknowns separate."),
            ("math", [
                "(r₁ − r₂)·C₁ = y′(0) − r₂·y(0)",
                "(r₁ − r₂)·C₂ = r₁·y(0) − y′(0)",
            ]),
            ("p", "The factor `r₁ − r₂` is why the roots have to differ. If they are "
                  "different it is not zero and may be divided out, so there is "
                  "exactly one pair `C₁, C₂` for every starting value and rate. If "
                  "they are equal the two exponentials are one function, and the "
                  "repeated-root form takes over."),
            ("example", ("The lab's first preset",
                         "For `y″ + 3y′ + 2y = 0` the roots are `r₁ = −1` and `r₂ = −2`, "
                         "so `r₁ − r₂ = 1`. With `y(0) = 0` and `y′(0) = 1`, the first "
                         "formula gives `C₁ = (1 − 0)/1 = 1` and the second "
                         "`C₂ = (0 − 1)/1 = −1`.",
                         "The solution is `e^(−t) − e^(−2t)`. It starts at `0` and "
                         "is positive afterwards, with a starting rate of `1`: the "
                         "rate at the start is not the rate of the number `0`.")),
            ("h3", "A complex fit"),
            ("p", "For `y″ + 2y′ + 5y = 0` the roots are `−1 ± 2i`, so the pair is "
                  "`C₁ = y(0)` and `−C₁ + 2·C₂ = y′(0)`. Take `y(0) = 2` and "
                  "`y′(0) = 0`. Then `C₁ = 2` and `−2 + 2·C₂ = 0`, so `C₂ = 1`, and "
                  "the solution is `e^(−t)·(2·cos(2t) + sin(2t))`. Its rate at `0` is "
                  "zero because two effects cancel exactly: the exponential "
                  "pulls it down by `2` and the sine pushes it up by `2`. The "
                  "rate is not zero because `y(0)` happens to be a constant."),
            ("h3", "When the lab declines"),
            ("p", "For `y″ − y′ − y = 0` the roots are `(1 ± √5)/2`. The two "
                  "equations are exactly as above, and they have a solution; by "
                  "hand it is `C₁ = (5 − √5)/10` and `C₂ = (5 + √5)/10` for "
                  "`y(0) = 1` and `y′(0) = 0`, and the first equation checks, "
                  "since the two add to `1`. The constants contain `√5`, though, and "
                  "the lab fits rational constants only. It prints a dash in the "
                  "constants tile and the solution tile and says in its status line "
                  "that the roots are irrational."),
            ("p", "That is a limit of the arithmetic. The lab differentiates and "
                  "substitutes solutions whose exponents and constants are fractions, "
                  "which it can do without rounding; a surd in an exponent or a "
                  "constant would have to be rounded, and then the residual would be "
                  "a rounded number instead of a zero. A complex pair whose `β` is a "
                  "surd is declined for the same reason, as in `y″ + 3y = 0` with the "
                  "roots `±√3·i`, and the status line names the irrational frequency. "
                  "The method is the same for any roots, and a solution with "
                  "irrational constants is a perfectly good one."),
        ],
        "lab": ("dekit", {
            "mode": "char",
            "view": "solution",
            "preset": "decay",
            "presets": [
                {"id": "decay", "label": "y″ + 3y′ + 2y = 0, y(0) = 0, y′(0) = 1",
                 "a": 1, "b": 3, "c": 2, "ic": [0, 1], "expect": {"ceC": "C₁ = 1, C₂ = −1", "ceSolution": "e^(−t) − e^(−2t)"}},
                {"id": "damped", "label": "y″ + 2y′ + 5y = 0, y(0) = 2, y′(0) = 0",
                 "a": 1, "b": 2, "c": 5, "ic": [2, 0], "expect": {"ceC": "C₁ = 2, C₂ = 1", "ceSolution": "2·e^(−t)·cos(2t) + e^(−t)·sin(2t)"}},
                {"id": "surd", "label": "y″ − y′ − y = 0, y(0) = 1, y′(0) = 0",
                 "a": 1, "b": -1, "c": -1, "ic": [1, 0], "expect": {"ceC": "—", "ceSolution": "—"}},
            ],
            "panel_title": "Fit the constants from the start",
            "panel_intro": (
                "Choose a preset and read the constants and the fitted solution. "
                "Write the two equations on paper first and solve them. The third "
                "preset has irrational roots, so the lab declines to fit it and "
                "says why. Then type your own starting values."
            ),
        }),
        "steps_title": "Fitting two constants from a start",
        "steps_intro": "Five moves, the same for every kind of root.",
        "steps": [
            ("Write the general solution for the kind of root",
             "Two exponentials, `(C₁ + C₂·t)·e^(rt)`, or `e^(αt)` with a cosine "
             "and sine. The lab names the kind."),
            ("Put t = 0 in it",
             "That gives the first equation. The exponentials become `1`, the "
             "cosine `1` and the sine `0`."),
            ("Put t = 0 in its rate",
             "Differentiate once, by the product rule where `t` or an exponential "
             "multiplies something. This gives the second equation, which equals "
             "`y′(0)`."),
            ("Solve by elimination",
             "Keep the fractions exact. Check that the number you divide by is "
             "not zero."),
            ("Check both starting values and the residual",
             "Put `t = 0` into the answer and into its rate, and read the status "
             "line of the lab for the residual."),
        ],
        "worked": {
            "title": "y″ + 2y′ + 5y = 0 with y(0) = 2 and y′(0) = 0",
            "intro": [
                "A complex pair, the pair of equations, and the answer checked at the start.",
            ],
            "lines": [
                "r = −1 ± 2i,   α = −1,   β = 2",
                "y = e^(−t)·(C₁·cos(2t) + C₂·sin(2t))",
                "y(0) = C₁ = 2",
                "y′(0) = −C₁ + 2·C₂ = 0",
                "−2 + 2·C₂ = 0,   C₂ = 1",
                "y = e^(−t)·(2·cos(2t) + sin(2t))",
                "check:  y′(0) = −2 + 2·1 = 0",
            ],
            "after": [
                "The fourth line is the rate of the general solution at `t = 0`. A "
                "wrong sign on the `−C₁` shows up in the last line as a starting "
                "rate that is not `0`.",
                "The lab prints the same solution expanded, as "
                "`2·e^(−t)·cos(2t) + e^(−t)·sin(2t)`. The status line also reports "
                "the residual of the whole solution, "
                "which is exactly `0`; the check on the last line covers the "
                "starting values, and the residual covers the equation.",
            ],
        },
        "quiz_title": "Setting up and solving the pair",
        "quiz": [
            {"q": "For `y″ + 3y′ + 2y = 0` with `y(0) = 0` and `y′(0) = 1`, the lab fits `C₁·e^(−t) + C₂·e^(−2t)`. Which constants does it print?",
             "a": ["`C₁ = −1`, `C₂ = 1`",
                   "`C₁ = 1`, `C₂ = −1`",
                   "`C₁ = 0`, `C₂ = 1`",
                   "`C₁ = 1`, `C₂ = 0`"],
             "c": 1,
             "why": "`C₁ + C₂ = 0` and `−C₁ − 2·C₂ = 1`; adding gives `−C₂ = 1`, so "
                    "`C₂ = −1` and `C₁ = 1`. The pair `−1, 1` puts the constants on "
                    "the wrong exponentials, and its rate at `0` is `−1`. The last "
                    "two do not satisfy `C₁ + C₂ = 0`."},
            {"q": "The repeated root of `y″ + 6y′ + 9y = 0` is `−3`. With `y(0) = 1` and `y′(0) = 0`, which solution fits?",
             "a": ["`(1 + 0·t)·e^(−3t)`",
                   "`(1 − 3t)·e^(−3t)`",
                   "`(1 + t)·e^(−3t)`",
                   "`(1 + 3t)·e^(−3t)`"],
             "c": 3,
             "why": "`C₁ = 1`, and `−3·C₁ + C₂ = 0` gives `C₂ = 3`. Taking `C₂ = y′(0) = 0` "
                    "ignores the exponential's contribution of `−3`. The value `−3` "
                    "has the sign reversed, and `1` is the starting value, not the "
                    "constant."},
            {"q": "For `y″ + 2y′ + 5y = 0` with `y(0) = 0` and `y′(0) = 4`, which value of `C₂` fits `e^(−t)·(C₁·cos(2t) + C₂·sin(2t))`?",
             "a": ["`2`",
                   "`4`",
                   "`1`",
                   "`−2`"],
             "c": 0,
             "why": "`C₁ = 0`, so `y′(0) = −C₁ + 2·C₂ = 2·C₂ = 4` and `C₂ = 2`. Writing "
                    "`C₂ = 4` forgets the factor `β = 2`. The value `1` divides "
                    "the starting rate by `4` instead of by `2`, and `−2` has a "
                    "sign error."},
            {"q": "For `y″ − y′ − y = 0` the lab shows a dash for the constants. What does it mean?",
             "a": ["No solution fits those starting values",
                   "The equation is not linear",
                   "The roots are irrational, so the constants would be surds, which the lab does not fit",
                   "The starting values contradict each other"],
             "c": 2,
             "why": "The roots are `(1 ± √5)/2`, so the constants contain `√5` and the "
                    "lab, which fits rational constants only, declines and says so. "
                    "A fit does exist, since the two roots differ. The equation is "
                    "linear, and two starting numbers can never contradict one "
                    "another here."},
        ],
        "mistakes": [
            ("Finding y′(0) by differentiating the number y(0)",
             "The starting rate is a second piece of data, and it is not computed from "
             "the first. A constant has rate zero, so `y(0) = 0` would suggest "
             "`y′(0) = 0` and the zero solution. The first preset has `y(0) = 0` and "
             "`y′(0) = 1`, and its solution `e^(−t) − e^(−2t)` starts at `0` and "
             "rises at rate `1`. Every question of this kind needs both numbers."),
            ("Putting the constants on the wrong roots",
             "The lab writes the larger root first, so in "
             "`C₁·e^(−t) + C₂·e^(−2t)` the constant `C₁` goes with `−1`. Reading it "
             "the other way gives `−e^(−t) + e^(−2t)` for the first preset, whose "
             "rate at `0` is `1 − 2 = −1`, not `1`. Name the root beside each "
             "constant before solving."),
            ("Taking a dash for a failure of the method",
             "The dash means that the constants contain a surd and the lab only "
             "fits rational ones. For `y″ − y′ − y = 0` they are "
             "`(5 − √5)/10` and `(5 + √5)/10`, and they add to `1` as the first "
             "equation requires. The method works for any roots, and an exact "
             "fit by hand is the way to see it."),
        ],
        "standard": (
            "Finish when you can write and solve the two equations for the constants for any kind of root, and say what a dash from the lab means.",
            "You should be able to set t = 0 in the general solution and in its "
            "rate, solve the resulting pair exactly, check both starting values, "
            "and say why irrational roots make the lab decline."),
        "note": 'The fit is guaranteed for the three forms in this course. &ldquo;Superposition and the Wronskian&rdquo; asks the general question: for which pairs of solutions is a fit always possible, and what number says so?',
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "superposition-and-the-wronskian",
        "title": "Superposition and the Wronskian",
        "module": "Fitting the constants",
        "one_line": "Show that a combination of solutions is a solution, compute the Wronskian at 0 exactly, and say what a nonzero value guarantees about fitting starting values.",
        "summary": (
            "If two functions solve `a·y″ + b·y′ + c·y = 0` then so does every "
            "combination of them, which is why the family has constants at all. "
            "Whether the combinations can fit any starting value and rate is "
            "decided by one number, the Wronskian of the two solutions at `t = 0`: "
            "when it is not zero, every start can be fitted, and when it is zero, "
            "some cannot."
        ),
        "key": [
            "y₁, y₂ solve it  ⟹  C₁·y₁ + C₂·y₂ does",
            "W = y₁·y₂′ − y₁′·y₂",
            "W(0) ≠ 0: every y(0), y′(0) can be fitted",
            "W(0) = 0: some starts cannot",
            "the sign of W(0) means nothing",
        ],
        "key_label": "One number says whether the fit always works",
        "concepts_intro": (
            "Three ideas: why combinations of solutions are solutions, why two "
            "solutions may still not be enough, and the number that tells the "
            "difference."
        ),
        "concepts": [
            ("Combinations of solutions are solutions",
             "The equation is linear with zero on the right: `y″`, `y′` and `y` each "
             "appear alone and to the first power. So the left side of a sum is "
             "the sum of the left sides, and a constant multiple is carried "
             "through. If the left side is zero for `y₁` and for `y₂` it is zero "
             "for `C₁·y₁ + C₂·y₂`."),
            ("Two solutions can still fit too little",
             "The functions `e^(−t)` and `2·e^(−t)` both solve "
             "`y″ + 3y′ + 2y = 0`, yet their combinations are all multiples of "
             "`e^(−t)`, a family with one real constant in it. Its starting rate "
             "is always `−1` times its starting value, so a start with "
             "`y(0) = 1` and `y′(0) = 0` is out of reach."),
            ("The Wronskian at 0 is the determinant of the fitting equations",
             "The pair of equations for `C₁` and `C₂` has the coefficients "
             "`y₁(0), y₂(0)` and `y₁′(0), y₂′(0)`. Their determinant is "
             "`y₁(0)·y₂′(0) − y₁′(0)·y₂(0)`, which is the Wronskian "
             "`W = y₁·y₂′ − y₁′·y₂` evaluated at `0`. Not zero means exactly one "
             "fit for every start."),
        ],
        "read_title": "Combining solutions, and the number that checks the fit",
        "read_intro": "The superposition rule and its proof, a pair of solutions that is not enough, the Wronskian, and the four lab presets.",
        "body": [
            ("thm", ("Superposition",
                     "If `y₁` and `y₂` solve `a·y″ + b·y′ + c·y = 0`, then "
                     "`C₁·y₁ + C₂·y₂` solves it for every pair of constants `C₁` and "
                     "`C₂`.")),
            ("proof", ["The rate of a sum is the sum of the rates, and a constant factor "
                       "comes out of a rate, so for `y = C₁·y₁ + C₂·y₂` the combination "
                       "`a·y″ + b·y′ + c·y` splits into "
                       "`C₁·(a·y₁″ + b·y₁′ + c·y₁) + C₂·(a·y₂″ + b·y₂′ + c·y₂)`.",
                       "Each bracket is zero because `y₁` and `y₂` are solutions, so the "
                       "whole is `C₁·0 + C₂·0 = 0`. The proof used two things: that "
                       "the equation is linear, and that its right side is zero."]),
            ("p", "The second condition matters. The equation `y″ + y = 1` is linear, "
                  "and `y = 1` solves it, since `y″ = 0` and `0 + 1 = 1`. The "
                  "double `y = 2` does not: `0 + 2 = 2`, not `1`. Superposition "
                  "belongs to equations whose right side is zero."),
            ("h3", "Two solutions are not always enough"),
            ("p", "Take `y₁ = e^(−t)` and `y₂ = 2·e^(−t)` for `y″ + 3y′ + 2y = 0`. Both "
                  "are solutions, and so is every combination "
                  "`C₁·y₁ + C₂·y₂ = (C₁ + 2·C₂)·e^(−t)`. The starting value is "
                  "`y(0) = C₁ + 2·C₂` and the starting rate is "
                  "`y′(0) = −C₁ − 2·C₂`, which is minus the first. The start "
                  "`y(0) = 1`, `y′(0) = 0` would need `C₁ + 2·C₂` to be `1` and "
                  "`0` together."),
            ("def", ("The Wronskian",
                     "For two functions `y₁` and `y₂`, the <strong>Wronskian</strong> is "
                     "`W(t) = y₁(t)·y₂′(t) − y₁′(t)·y₂(t)`. Its value at `t = 0` is the "
                     "determinant of the coefficients of the pair of equations that "
                     "fit `C₁` and `C₂`.")),
            ("p", "For the pair above, `y₁(0) = 1`, `y₂(0) = 2`, `y₁′(0) = −1` and "
                  "`y₂′(0) = −2`. The determinant is `1·(−2) − 2·(−1) = 0`, "
                  "and the Wronskian is zero for every `t`, because the second "
                  "function is a multiple of the first."),
            ("thm", ("What a nonzero Wronskian guarantees",
                     "If `y₁` and `y₂` solve `a·y″ + b·y′ + c·y = 0` and "
                     "`W(0) ≠ 0`, then for every `y(0)` and `y′(0)` there is exactly "
                     "one pair `C₁, C₂` with `C₁·y₁ + C₂·y₂` starting there.")),
            ("proof", ["The equations are `C₁·y₁(0) + C₂·y₂(0) = y(0)` and "
                       "`C₁·y₁′(0) + C₂·y₂′(0) = y′(0)`. Multiply the first by `y₂′(0)` "
                       "and the second by `y₂(0)` and subtract, and the `C₂` terms "
                       "cancel: `W(0)·C₁ = y₂′(0)·y(0) − y₂(0)·y′(0)`.",
                       "In the same way `W(0)·C₂ = y₁(0)·y′(0) − y₁′(0)·y(0)`. If "
                       "`W(0)` is not zero both can be divided by it, which gives "
                       "one pair of constants and no other. That the combination is "
                       "then <em>the</em> solution with that start is the fact that two "
                       "starting values fix one solution, which the course uses "
                       "and does not prove."]),
            ("h3", "The four presets"),
            ("p", "The lab's four presets give the pair of solutions that the roots "
                  "determine and print `W(0)`. For `y″ + 3y′ + 2y = 0` the pair is "
                  "`e^(−t)` and `e^(−2t)`, and the worked example below computes "
                  "it. For `y″ + 4y = 0` the pair is `cos(2t)` and `sin(2t)`, "
                  "and `W` is `2` for every `t`. For `y″ + 4y′ + 4y = 0` the pair is "
                  "`e^(−2t)` and `t·e^(−2t)`, and `W = e^(−4t)`, which is `1` at "
                  "`0`."),
            ("p", "For two exponentials `W(0)` is the second root minus the first, "
                  "with the larger root first, and a repeated root would make it "
                  "zero: that is why the repeated case needed the second function "
                  "`t·e^(rt)`. For a complex pair `W(0)` is `β`. The fourth preset, "
                  "`y″ − y′ − y = 0`, has the roots `(1 ± √5)/2`, which differ by "
                  "`√5`, and the lab prints `−√5` as an exact surd, not a rounded "
                  "number; the sign is the order of the two roots. In "
                  "all three computed cases `W(t) = W(0)·e^(−(b/a)·t)`, so a "
                  "Wronskian that starts nonzero never reaches zero; this is stated "
                  "as a pattern, not proved."),
            ("p", "The sign of `W(0)` carries no information. Swapping the roles of "
                  "`y₁` and `y₂` reverses it, and what the guarantee needs is only "
                  "that it is not zero."),
        ],
        "lab": ("dekit", {
            "mode": "char",
            "view": "wronskian",
            "preset": "decay",
            "presets": [
                {"id": "decay", "label": "y″ + 3y′ + 2y = 0, e^(−t) and e^(−2t)",
                 "a": 1, "b": 3, "c": 2, "ic": None, "expect": {"ceW": "−1"}},
                {"id": "pure", "label": "y″ + 4y = 0, cos(2t) and sin(2t)",
                 "a": 1, "b": 0, "c": 4, "ic": None, "expect": {"ceW": "2"}},
                {"id": "repeated", "label": "y″ + 4y′ + 4y = 0, e^(−2t) and t·e^(−2t)",
                 "a": 1, "b": 4, "c": 4, "ic": None, "expect": {"ceW": "1"}},
                {"id": "surd", "label": "y″ − y′ − y = 0, roots with a square root",
                 "a": 1, "b": -1, "c": -1, "ic": None, "expect": {"ceW": "−√5"}},
            ],
            "panel_title": "The Wronskian of the two solutions at 0",
            "panel_intro": (
                "Choose a preset and read the Wronskian at 0 beside the plot of "
                "the two solutions. Compute y₁·y₂′ − y₁′·y₂ at 0 by hand first. "
                "Then type an equation whose discriminant is 0 and watch the "
                "two solutions stay different."
            ),
        }),
        "steps_title": "Checking that two solutions are enough",
        "steps_intro": "Five moves. The determinant is the only new computation.",
        "steps": [
            ("Write the two solutions",
             "From the roots: two exponentials, or `e^(rt)` and `t·e^(rt)`, or "
             "`e^(αt)` with cosine and with sine."),
            ("Differentiate each once",
             "You need `y₁′` and `y₂′`, and the product rule where a factor of "
             "`t` or an exponential is multiplied."),
            ("Form y₁·y₂′ − y₁′·y₂",
             "Keep the order: first function times the rate of the second, "
             "minus the rate of the first times the second."),
            ("Put in t = 0",
             "Exponentials become `1`, cosines `1`, sines `0`, and `t` becomes `0`."),
            ("Read the verdict",
             "Not zero: every start can be fitted, by exactly one pair. Zero: "
             "find the relation between `y(0)` and `y′(0)` that the pair can reach."),
        ],
        "worked": {
            "title": "e^(−t) and e^(−2t) for y″ + 3y′ + 2y = 0",
            "intro": [
                "The Wronskian of the two exponentials, and the determinant it equals.",
            ],
            "lines": [
                "y₁ = e^(−t)         y₂ = e^(−2t)",
                "y₁′ = −e^(−t)       y₂′ = −2·e^(−2t)",
                "y₁·y₂′ = −2·e^(−3t)",
                "y₁′·y₂ = −e^(−3t)",
                "W = −2·e^(−3t) + e^(−3t) = −e^(−3t)",
                "W(0) = −1,   not zero",
                "C₁ + C₂ = y(0),   −C₁ − 2·C₂ = y′(0)",
                "determinant:  1·(−2) − 1·(−1) = −1",
            ],
            "after": [
                "The determinant of the pair of equations is `−1`, the same as "
                "`W(0)`, so the pair has exactly one solution for every right side. "
                "Adding the two equations gives `C₂ = −(y(0) + y′(0))`, then "
                "`C₁ = 2·y(0) + y′(0)`; for `y(0) = 1` and `y′(0) = 0` that is "
                "`C₁ = 2`, `C₂ = −1`.",
                "The value is negative, and nothing turns on that: with the two "
                "functions in the other order it would be `+1`.",
            ],
        },
        "quiz_title": "Superposition and the guarantee",
        "quiz": [
            {"q": "`y₁` and `y₂` both solve `y″ − y = 0`. Which function must also solve it?",
             "a": ["`y₁·y₂`",
                   "`3·y₁ − 2·y₂`",
                   "`y₁²`",
                   "`y₁ + 1`"],
             "c": 1,
             "why": "A combination with constant coefficients keeps the residual at "
                    "zero. The product fails: `e^t·e^(−t) = 1` and `1″ − 1 = −1`. The "
                    "square is not a combination, and `y₁ + 1` has the residual "
                    "`−1`, because the constant is not a solution."},
            {"q": "For `y₁ = cos(3t)` and `y₂ = sin(3t)`, what is `W(0)`?",
             "a": ["`1`",
                   "`0`",
                   "`3`",
                   "`−3`"],
             "c": 2,
             "why": "`W = cos(3t)·3·cos(3t) − (−3·sin(3t))·sin(3t) = 3`. The value "
                    "`1` forgets the factor from the chain rule, and `0` would "
                    "mean the two functions are multiples of each other, which they "
                    "are not. `−3` is the other order's value."},
            {"q": "Each function below solves `y″ + 3y′ + 2y = 0`. Which pair cannot fit the start `y(0) = 1`, `y′(0) = 0`?",
             "a": ["`e^(−t)` and `e^(−2t)`",
                   "`e^(−t)` and `e^(−t) + e^(−2t)`",
                   "`2·e^(−t)` and `−e^(−2t)`",
                   "`e^(−t)` and `5·e^(−t)`"],
             "c": 3,
             "why": "The last pair is a function and a multiple of it, so its "
                    "Wronskian is zero, and its combinations always have "
                    "`y′(0) = −y(0)`. The first pair has `W(0) = −1`. The second "
                    "has `W = −e^(−3t)` as well, and the third has `W = 2·e^(−3t)`; "
                    "neither is zero."},
            {"q": "The lab prints `W(0) = 1` for `y₁ = e^(−2t)` and `y₂ = t·e^(−2t)` in `y″ + 4y′ + 4y = 0`. What follows?",
             "a": ["Every starting value and rate can be fitted by exactly one pair of constants",
                   "Only starts with `y′(0) = −2·y(0)` can be fitted",
                   "The two functions are not solutions",
                   "Both constants are equal to `1`"],
             "c": 0,
             "why": "A nonzero Wronskian at `0` is the guarantee. The second statement "
                    "describes what a zero Wronskian would give. The functions are "
                    "solutions, as &ldquo;Repeated Roots&rdquo; verified, and the "
                    "constants depend on the start, not on `W`."},
        ],
        "mistakes": [
            ("Believing that any two solutions can fit any starting values",
             "The functions `e^(−t)` and `2·e^(−t)` both solve `y″ + 3y′ + 2y = 0`, "
             "but every combination has `y′(0) = −y(0)`, so the start `y(0) = 1`, "
             "`y′(0) = 0` has no fit. Their Wronskian is `1·(−2) − 2·(−1) = 0`. "
             "The pair has to have a nonzero Wronskian for the guarantee to hold."),
            ("Combining solutions by multiplying them or adding a constant",
             "Superposition is for sums with constant multiples. For "
             "`y″ + 3y′ + 2y = 0` the product of the two solutions is `e^(−3t)`, "
             "and its residual is `9·e^(−3t) − 9·e^(−3t) + 2·e^(−3t) = 2·e^(−3t)`, "
             "which is not zero. Neither a product nor a shift stays "
             "a solution."),
            ("Reading meaning into the sign of the Wronskian",
             "The first preset has `W(0) = −1` and the repeated-root preset has "
             "`W(0) = 1`, and that tells you nothing about the fit. Swapping which "
             "function is called `y₁` reverses the sign. Only whether the value is "
             "zero matters."),
        ],
        "standard": (
            "Finish when you can prove superposition, compute W(0) for a pair of solutions, and say what it guarantees.",
            "You should be able to show that a combination of solutions is a "
            "solution, compute y₁·y₂′ − y₁′·y₂ at t = 0 exactly, say that a "
            "nonzero value means every starting value and rate can be fitted, and "
            "give a pair for which it cannot."),
        "note": 'The course so far has solved one equation at a time. &ldquo;From Second Order to a System&rdquo; changes the point of view: the same equation written as two first-order equations, whose matrix carries the characteristic quadratic inside its trace and determinant.',
    },

    # ---------------------------------------------------------------- 09
    {
        "slug": "from-second-order-to-a-system",
        "title": "From Second Order to a System",
        "module": "The systems view",
        "one_line": "Rewrite a·x″ + b·x′ + c·x = 0 as x′ = v and v′ = −(c/a)·x − (b/a)·v, and show that the matrix's trace and determinant reproduce the characteristic equation.",
        "summary": (
            "Naming the rate `v = x′` turns one equation of second order into two "
            "of first order, `x′ = v` and `v′ = −(c/a)·x − (b/a)·v`. The grid of "
            "four numbers on the right has a trace `−b/a` and a determinant `c/a`, "
            "and the quadratic built from them is the characteristic equation "
            "divided by `a`. The same roots appear, so the same motion does."
        ),
        "key": [
            "v = x′,   x′ = v",
            "v′ = −(c/a)·x − (b/a)·v",
            "trace τ = −b/a,   determinant Δ = c/a",
            "λ² − τ·λ + Δ = 0  is  r² + (b/a)·r + c/a = 0",
            "the same roots, the same motion",
        ],
        "key_label": "A system has the same roots as its equation",
        "concepts_intro": (
            "Three ideas: the new unknown, what its equation looks like as a matrix, "
            "and why nothing about the motion is new."
        ),
        "concepts": [
            ("Name the rate as a second unknown",
             "Write `v` for `x′`. Then `x′ = v` is true by the choice of name, and "
             "`v′ = x″` can be replaced using the original equation. The result is "
             "a pair of first-order equations in the two unknowns `x` and `v`, "
             "which a later course studies in the plane of `(x, v)`."),
            ("The coefficients form a matrix with a trace and a determinant",
             "The right-hand sides are `0·x + 1·v` and `−(c/a)·x − (b/a)·v`, so the "
             "four coefficients form a grid, the matrix `A`. Its trace is the sum "
             "of the diagonal entries, `0 + (−b/a) = −b/a`, and its determinant is "
             "`0·(−b/a) − 1·(−c/a) = c/a`."),
            ("The motion is the same",
             "Given the start `x(0)` and the start `v(0) = x′(0)` the system and "
             "the equation have the same solution: the first component of the "
             "system is the function the equation asks for, and the second is its "
             "rate. The two initial values of the equation are the two components "
             "of the system's starting point."),
        ],
        "read_title": "One equation, two unknowns, one matrix",
        "read_intro": "The substitution, the matrix and its trace and determinant, a check that the system and the equation agree, and what the lab's last tile names.",
        "body": [
            ("p", "From here the unknown is called `x`, because the system treats "
                  "position and velocity as a pair, and the equation under study is "
                  "`a·x″ + b·x′ + c·x = 0` with `a` not zero. Divide by `a`, and "
                  "solve for the second rate."),
            ("math", [
                "x″ = −(c/a)·x − (b/a)·x′",
                "v = x′",
                "x′ = v",
                "v′ = −(c/a)·x − (b/a)·v",
            ]),
            ("p", "The first line is the original equation, solved for its highest "
                  "rate. The last two lines are a system of two first-order "
                  "equations; the second is the first line with `v` written in "
                  "place of `x′`. Nothing has been lost, since `v` is the rate "
                  "of `x` by definition. The system is written as a matrix with one "
                  "row for each equation; the words trace and determinant are those "
                  "of Algebra's Systems and Matrices, and the two formulas in the "
                  "claim below are all this lesson needs of them."),
            ("math", [
                "A =   0       1",
                "     −c/a    −b/a",
            ]),
            ("thm", ("The matrix carries the characteristic equation",
                     "The matrix `A` has trace `τ = −b/a` and determinant `Δ = c/a`, "
                     "and the equation `λ² − τ·λ + Δ = 0` is the characteristic "
                     "equation `a·r² + b·r + c = 0` divided by `a`.")),
            ("proof", ["The trace is `0 + (−b/a)` and the determinant is "
                       "`0·(−b/a) − 1·(−c/a)`, which are `−b/a` and `c/a`.",
                       "Then `λ² − τ·λ + Δ = λ² + (b/a)·λ + c/a`. Multiplying by `a` "
                       "gives `a·λ² + b·λ + c`, which is the characteristic "
                       "quadratic with `λ` in place of `r`. The eigenvalues of `A`, "
                       "the numbers a later course defines as the roots of this "
                       "quadratic, are the roots `r` of the equation."]),
            ("h3", "The system and the equation agree"),
            ("p", "The first preset is `x″ + 3x′ + 2x = 0`, and the solution of "
                  "the equation from the earlier lesson with `x(0) = 1` and "
                  "`x′(0) = 0` is `x = 2·e^(−t) − e^(−2t)`. Its rate is "
                  "`v = −2·e^(−t) + 2·e^(−2t)`. Both equations of the system hold "
                  "exactly."),
            ("math", [
                "x′ = −2·e^(−t) + 2·e^(−2t) = v",
                "v′ = 2·e^(−t) − 4·e^(−2t)",
                "−2x − 3v = −4·e^(−t) + 2·e^(−2t) + 6·e^(−t) − 6·e^(−2t)",
                "         = 2·e^(−t) − 4·e^(−2t) = v′",
            ]),
            ("p", "The pair `(x, v)` is a solution of the system, and its first "
                  "component is the solution of the equation. The pair also starts "
                  "at `(x(0), v(0)) = (1, 0)`, which is the two initial values of "
                  "the equation written as a point."),
            ("h3", "The three presets"),
            ("p", "The lab takes the matrix as its input and prints the trace, the "
                  "determinant, the eigenvalues and a name for the picture the "
                  "system makes in the plane. The matrix for `x″ + 3x′ + 2x = 0` "
                  "has `τ = −3` and `Δ = 2`, and its eigenvalues are `−2` and `−1`. "
                  "The matrix for `x″ + 4x = 0` has `τ = 0` and `Δ = 4`, "
                  "eigenvalues `±2i`. The matrix for `x″ + 2x′ + 5x = 0` has "
                  "`τ = −2` and `Δ = 5`, eigenvalues `−1 ± 2i`. These are the "
                  "roots from the earlier lessons, one for one."),
            ("p", "The name the lab gives the picture follows the roots: negative "
                  "real roots, imaginary roots and complex roots with a negative real "
                  "part are named a stable node, a centre and a stable spiral. What the "
                  "names mean is the subject of Systems and the Phase Plane; "
                  "here they are a label on roots already understood."),
            ("p", "The lab prints six more tiles that belong to that course: "
                  "eigenvectors, a general solution written with them, the constants "
                  "fitted to the start, and two Euler tiles that the next lesson "
                  "reads. One of them is worth a look now. For the first preset the "
                  "constants tile says `C₁ = −1, C₂ = 2`, while &ldquo;Real Distinct "
                  "Roots&rdquo; fitted `C₁ = 2, C₂ = −1` to the same start. The two labs "
                  "number the roots in opposite orders, this one from the smaller "
                  "eigenvalue up, so here `C₁ = −1` goes with `e^(−2t)`, and the "
                  "first component is `2·e^(−t) − e^(−2t)` either way."),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "field",
            "preset": "decay",
            "presets": [
                {"id": "decay", "label": "x″ + 3x′ + 2x = 0, start (1, 0)",
                 "A": [[0, 1], [-2, -3]], "start": [1, 0], "h": "1/4", "n": 8, "expect": {"ppTrace": "−3", "ppDet": "2", "ppEig": "−2, −1", "ppType": "stable node"}},
                {"id": "pure", "label": "x″ + 4x = 0, start (1, 0)",
                 "A": [[0, 1], [-4, 0]], "start": [1, 0], "h": "1/4", "n": 8, "expect": {"ppTrace": "0", "ppDet": "4", "ppEig": "±2i", "ppType": "centre"}},
                {"id": "damped", "label": "x″ + 2x′ + 5x = 0, start (0, 2)",
                 "A": [[0, 1], [-5, -2]], "start": [0, 2], "h": "1/4", "n": 8, "expect": {"ppTrace": "−2", "ppDet": "5", "ppEig": "−1 ± 2i", "ppType": "stable spiral"}},
            ],
            "panel_title": "The matrix of a second-order equation",
            "panel_intro": (
                "Choose a preset and read the trace, the determinant and the "
                "eigenvalues. Compare the eigenvalues with the roots of the "
                "characteristic equation you computed from the same coefficients. "
                "Then type a matrix of the form 0 1; -c -b for your own equation."
            ),
        }),
        "steps_title": "Writing a second-order equation as a system",
        "steps_intro": "Five moves. The one that is easy to skip is the division by a.",
        "steps": [
            ("Divide by the leading coefficient",
             "Solve for the highest rate: `x″ = −(c/a)·x − (b/a)·x′`. The rate "
             "`x″` must stand alone, with coefficient `1`."),
            ("Name the rate",
             "Write `v = x′`, and `x′ = v` is the first equation of the system."),
            ("Substitute v into the second",
             "The second equation is `v′ = −(c/a)·x − (b/a)·v`. Its coefficients "
             "of `x` and `v` are the bottom row of the matrix."),
            ("Read the trace and the determinant",
             "`τ = −b/a` and `Δ = c/a`. They are the sum of the diagonal "
             "entries and the diagonal product minus the cross product."),
            ("Compare λ² − τ·λ + Δ with the characteristic equation",
             "They are the same quadratic up to the factor `a`. Compute the roots "
             "once and check them against the lab's eigenvalue tile."),
        ],
        "worked": {
            "title": "x″ + 3x′ + 2x = 0 as a system",
            "intro": [
                "From the equation to the matrix, and from the matrix back to the quadratic.",
            ],
            "lines": [
                "v = x′,   so   x′ = v",
                "x″ = −2x − 3x′,   so   v′ = −2x − 3v",
                "A =   0    1",
                "     −2   −3",
                "τ = 0 + (−3) = −3",
                "Δ = 0·(−3) − 1·(−2) = 2",
                "λ² − τ·λ + Δ = λ² + 3λ + 2 = 0",
                "λ = −1 or λ = −2,  the roots of r² + 3r + 2 = 0",
            ],
            "after": [
                "Here `a = 1`, so dividing by `a` changes nothing. With "
                "`2x″ + 8x′ + 6x = 0`, the bottom row would be `−3` and `−4`, "
                "not `−6` and `−8`.",
                "The roots are those of the earlier lessons, and so are the "
                "solutions: the first component of every solution of the system "
                "is a solution of the equation.",
            ],
        },
        "quiz_title": "From the equation to the matrix",
        "quiz": [
            {"q": "For `2x″ + 8x′ + 6x = 0`, with `v = x′`, what is `v′`?",
             "a": ["`−6x − 8v`",
                   "`−3x + 4v`",
                   "`−3x − 4v`",
                   "`−8x − 6v`"],
             "c": 2,
             "why": "Dividing by `2` gives `x″ = −3x − 4x′`, so `v′ = −3x − 4v`. The "
                    "first option skips the division. The second has the sign of "
                    "the damping term wrong, and the last swaps the two "
                    "coefficients."},
            {"q": "What are the trace and determinant of the matrix for `x″ + 4x = 0`?",
             "a": ["`τ = 0`, `Δ = 4`",
                   "`τ = 4`, `Δ = 0`",
                   "`τ = 0`, `Δ = −4`",
                   "`τ = −4`, `Δ = 1`"],
             "c": 0,
             "why": "The matrix has rows `0, 1` and `−4, 0`. The trace is `0 + 0 = 0` and "
                    "the determinant is `0·0 − 1·(−4) = 4`. The second option "
                    "swaps them, the third drops the sign in the cross product, "
                    "and the fourth reads the coefficients of another equation."},
            {"q": "The lab prints the eigenvalues `−1 ± 2i` for the matrix of `x″ + 2x′ + 5x = 0`. How do they relate to the equation?",
             "a": ["They are a different set of numbers that describes the system only",
                   "They are the roots of the equation's characteristic quadratic",
                   "They are the starting values `x(0)` and `v(0)`",
                   "They are the coefficients `b` and `c`"],
             "c": 1,
             "why": "The characteristic quadratic is `r² + 2r + 5 = 0`, with roots "
                    "`−1 ± 2i`, the same numbers. The eigenvalues are not "
                    "starting values, which are a separate input, and the "
                    "coefficients `2` and `5` are not the roots."},
            {"q": "A solution of the system for `x″ + 3x′ + 2x = 0` has `x = e^(−t)`. What is `v`?",
             "a": ["`e^(−t)`",
                   "`−2·e^(−2t)`",
                   "`e^(−2t)`",
                   "`−e^(−t)`"],
             "c": 3,
             "why": "`v` is the rate of `x`, so `v = (e^(−t))′ = −e^(−t)`. Then "
                    "`v′ = e^(−t)` equals `−2x − 3v = −2e^(−t) + 3e^(−t)`, and the "
                    "second equation holds. The other options are rates of "
                    "the wrong function or have no rate taken."},
        ],
        "mistakes": [
            ("Thinking the system has different solutions from the equation",
             "The system is the equation in other clothes. The first component "
             "of `(x, v) = (2·e^(−t) − e^(−2t), −2·e^(−t) + 2·e^(−2t))` is the "
             "equation's solution for `x(0) = 1` and `x′(0) = 0`, and the second "
             "is its rate. Both equations of the system hold exactly, and the "
             "start `(1, 0)` is the pair of initial values. Nothing new has been "
             "solved, and nothing is lost."),
            ("Forgetting to divide by a",
             "For `2x″ + 8x′ + 6x = 0` the bottom row is `−3, −4`. Using `−6, −8` "
             "gives the trace `−8` and determinant `6`, so the quadratic "
             "`λ² + 8λ + 6 = 0` with the irrational roots `−4 ± √10`, which are "
             "not the roots `−1` and `−3` of `2r² + 8r + 6 = 0`. The check "
             "against the characteristic equation catches the slip."),
            ("Swapping the two entries of the bottom row",
             "The entry under `x` is `−c/a` and under `v` is `−b/a`. For "
             "`x″ + 3x′ + 2x = 0` swapping them gives `−3, −2`, with trace `−2` "
             "and determinant `3`, a complex pair, and the lab would name it a "
             "spiral, though the equation has real roots `−1` and `−2`. The "
             "eigenvalue tile is the check."),
        ],
        "standard": (
            "Finish when you can turn a second-order equation into a pair of first-order equations and show the roots are unchanged.",
            "You should be able to divide by the leading coefficient, name v = x′, "
            "write the matrix, compute its trace and determinant, and show that "
            "λ² − τ·λ + Δ = 0 is the characteristic equation divided by a."),
        "note": 'One more thing can be done with the system that cannot be done with the equation: step it. &ldquo;Euler on an Oscillator&rdquo; applies Euler\'s method to <em>x′ = v, v′ = −x</em> and finds the exact amount by which the method spirals outward at every step.',
    },

    # ---------------------------------------------------------------- 10
    {
        "slug": "euler-on-an-oscillator",
        "title": "Euler on an Oscillator",
        "module": "The systems view",
        "one_line": "Step x′ = v, v′ = −x with Euler's method, show that every step multiplies x² + v² by exactly 1 + h², and compute the growth over a whole run.",
        "summary": (
            "The oscillator `x′ = v, v′ = −x` has solutions that move on a circle, "
            "and `x² + v²` never changes. Euler's method applied to it does not "
            "keep that quantity: each step multiplies `x² + v²` by exactly "
            "`1 + h²`, so the polygon spirals outward. The fractions the lab "
            "prints are exact, and they show an exactly wrong answer."
        ),
        "key": [
            "x′ = v,  v′ = −x:  x² + v² stays 1",
            "xₙ₊₁ = xₙ + h·vₙ",
            "vₙ₊₁ = vₙ − h·xₙ",
            "xₙ₊₁² + vₙ₊₁² = (1 + h²)·(xₙ² + vₙ²)",
            "h = 1/4:  17/16 per step, exactly",
            "exact fractions, and still off the circle",
        ],
        "key_label": "Each step gains the factor 1 + h²",
        "concepts_intro": (
            "Three ideas: what the equation conserves, what one Euler step does "
            "to it, and why exact fractions do not repair it."
        ),
        "concepts": [
            ("The true solution stays on a circle",
             "For `x′ = v` and `v′ = −x` the rate of `x² + v²` is "
             "`2x·x′ + 2v·v′ = 2x·v − 2v·x = 0`. So `x² + v²` is constant along a "
             "solution: from the start `(1, 0)` the solution is `(cos t, −sin t)` "
             "and stays on the circle of radius `1`."),
            ("An Euler step multiplies x² + v² by 1 + h²",
             "One step replaces `(x, v)` by `(x + h·v, v − h·x)`. Squaring and "
             "adding, the cross terms `2h·x·v` and `−2h·x·v` cancel and what is "
             "left is `(1 + h²)·(x² + v²)`. The factor is greater than `1` for "
             "every positive `h`."),
            ("The error is the method's, not the arithmetic's",
             "The lab prints every point as an exact fraction. The growth by "
             "`1 + h²` is not a rounding effect: it is the exact value of the "
             "recipe. A smaller step makes the factor closer to `1`, and the "
             "factor never reaches it."),
        ],
        "read_title": "Why Euler's polygon leaves the circle",
        "read_intro": "The conserved quantity, a proof that a step multiplies it by 1 + h², the first two steps by hand, and the three step sizes the lab compares.",
        "body": [
            ("p", "The oscillator `x″ + x = 0` written as a system is `x′ = v`, "
                  "`v′ = −x`. Its solutions from `(1, 0)` are `x = cos t` and "
                  "`v = −sin t`, so that `x² + v² = cos² t + sin² t = 1` at every "
                  "`t`. The quantity can be shown to be constant without the "
                  "solutions at all: its rate is `2x·v + 2v·(−x) = 0`. That is what "
                  "the equation conserves."),
            ("p", "Euler's method steps the system by the recipe "
                  "`xₙ₊₁ = xₙ + h·vₙ` and `vₙ₊₁ = vₙ − h·xₙ`, with both formulas using "
                  "the old values. Differential Equations and Euler's Method ran the "
                  "same recipe on a "
                  "single equation; here it runs on a pair, and the lab prints the "
                  "pair at every step as exact fractions."),
            ("thm", ("Euler's growth on the oscillator",
                     "For the Euler step `xₙ₊₁ = xₙ + h·vₙ`, `vₙ₊₁ = vₙ − h·xₙ`, "
                     "`xₙ₊₁² + vₙ₊₁² = (1 + h²)·(xₙ² + vₙ²)` for every `xₙ` and "
                     "`vₙ`.")),
            ("proof", ["Expand both squares: "
                       "`(xₙ + h·vₙ)² = xₙ² + 2h·xₙ·vₙ + h²·vₙ²` and "
                       "`(vₙ − h·xₙ)² = vₙ² − 2h·xₙ·vₙ + h²·xₙ²`.",
                       "Adding, the middle terms cancel, and what remains is "
                       "`xₙ² + vₙ² + h²·(xₙ² + vₙ²) = (1 + h²)·(xₙ² + vₙ²)`. The "
                       "argument is algebra and holds for any starting point."]),
            ("h3", "The first two steps by hand"),
            ("p", "Start at `(1, 0)` with `h = 1/4`. The first step gives "
                  "`x₁ = 1 + (1/4)·0 = 1` and `v₁ = 0 − (1/4)·1 = −1/4`, so "
                  "`x₁² + v₁² = 1 + 1/16 = 17/16`. The second gives "
                  "`x₂ = 1 + (1/4)(−1/4) = 15/16` and "
                  "`v₂ = −1/4 − (1/4)·1 = −1/2`, so "
                  "`x₂² + v₂² = 225/256 + 64/256 = 289/256`, which is `(17/16)²`."),
            ("math", [
                "n      xₙ        vₙ       xₙ² + vₙ²",
                "0       1         0           1",
                "1       1       −1/4        17/16",
                "2     15/16     −1/2       289/256",
            ]),
            ("p", "Every step multiplies the last column by `17/16`, and the "
                  "point is outside the circle after the first step. The "
                  "polygon the lab draws spirals out of the circle the true "
                  "solution stays on, which the lab draws behind it in floating "
                  "point and labels as drawn. The lab names the origin of the "
                  "true system a centre, a point with closed circles round it, "
                  "and a polygon that does not close is exactly what Euler's "
                  "method makes of one."),
            ("h3", "Three step sizes, one end time"),
            ("p", "The three presets run to the same time, `t = 6`: "
                  "`h = 1/2` for `12` steps, `h = 1/4` for `24` and `h = 1/8` for "
                  "`48`. The lab prints the ratio of the last radius squared to the "
                  "one before: `5/4`, `17/16` and `65/64`, each `1 + h²` exactly. "
                  "The total gain is that factor to the power of the number of "
                  "steps, so it falls as `h` falls, and it never reaches `1`."),
            ("example", ("The total growth at t = 6",
                         "With `h = 1/4` the radius squared after `24` steps is "
                         "`(17/16)²⁴`, which is `≈ 4.28444`, rounded. With "
                         "`h = 1/8` it is `(65/64)⁴⁸ ≈ 2.10476`, also rounded, and with "
                         "`h = 1/2` it is `(5/4)¹² ≈ 14.5519`.",
                         "The natural logarithm of the total gain, which is the growth "
                         "rate in an exponent, falls from `≈ 2.67772` to `≈ 1.45499` to "
                         "`≈ 0.744201`, all rounded: it roughly halves each time `h` "
                         "does, the behaviour of a method whose error is proportional "
                         "to `h`. A smaller step slows the growth and cannot remove "
                         "it.")),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "exact",
            "preset": "quarter",
            "presets": [
                {"id": "quarter", "label": "x′ = v, v′ = −x, start (1, 0), h = 1/4, 24 steps",
                 "A": [[0, 1], [-1, 0]], "start": [1, 0], "h": "1/4", "n": 24, "expect": {"ppRatio": "17/16", "ppLast": "(535788072480961/281474976710656, 7152073883955/8796093022208)", "ppType": "centre"}},
                {"id": "eighth", "label": "x′ = v, v′ = −x, start (1, 0), h = 1/8, 48 steps",
                 "A": [[0, 1], [-1, 0]], "start": [1, 0], "h": "1/8", "n": 48, "expect": {"ppRatio": "65/64", "ppLast": "(30770093621683264155841585501049700833306113/22300745198530623141535718272648361505980416, 78104246420400163827731200592088894513603/174224571863520493293247799005065324265472)", "ppType": "centre"}},
                {"id": "coarse", "label": "x′ = v, v′ = −x, start (1, 0), h = 1/2, 12 steps",
                 "A": [[0, 1], [-1, 0]], "start": [1, 0], "h": "1/2", "n": 12, "expect": {"ppRatio": "5/4", "ppLast": "(11753/4096, 1287/512)", "ppType": "centre"}},
            ],
            "panel_title": "Euler's steps on the oscillator, exactly",
            "panel_intro": (
                "Choose a preset and read the ratio of the last radius squared "
                "to the one before, and the last point. The ratio is 1 + h² for "
                "every step. Then change h or the number of steps, and predict "
                "the ratio before you read it."
            ),
        }),
        "steps_title": "Measuring Euler's growth on the oscillator",
        "steps_intro": "Five moves. The factor is known before any step is taken.",
        "steps": [
            ("Write the system",
             "`x′ = v` and `v′ = −x`. For the true solution `x² + v²` is "
             "constant, so the target is a circle."),
            ("Predict the factor",
             "Each step multiplies `x² + v²` by `1 + h²`. Compute it from the "
             "step size before reading the lab."),
            ("Take two steps by hand",
             "Use the old values in both formulas. Check that the second "
             "radius squared is the square of the factor."),
            ("Read the ratio tile",
             "The lab's ratio is the last radius squared over the one before. It "
             "should equal the factor you predicted exactly."),
            ("Compound it to the end time",
             "The total gain over `n` steps is the factor to the power `n`. "
             "Compare two step sizes that end at the same `t`."),
        ],
        "worked": {
            "title": "h = 1/4 from (1, 0)",
            "intro": [
                "Two Euler steps by hand, then the factor for the whole run.",
            ],
            "lines": [
                "first:   x = 1 + (1/4)·0 = 1",
                "         v = 0 − (1/4)·1 = −1/4",
                "radius² = 1 + 1/16 = 17/16",
                "second:  x = 1 + (1/4)(−1/4) = 15/16",
                "         v = −1/4 − (1/4)·1 = −1/2",
                "radius² = 225/256 + 64/256 = 289/256 = (17/16)²",
                "factor per step = 1 + h² = 17/16",
                "after 24 steps:  (17/16)²⁴",
            ],
            "after": [
                "Each line uses the old point, so the second step starts from "
                "`(1, −1/4)` and not from a mixture of old and new values. The "
                "last column of the table in the lesson shows the factor again.",
                "The true solution has radius squared `1` at every time. The "
                "polygon's value is exactly `17/16` after the first step, "
                "and this is the method, not the arithmetic.",
            ],
        },
        "quiz_title": "Euler's gain on the oscillator",
        "quiz": [
            {"q": "With `h = 1/2`, starting at `(1, 0)`, what is `x² + v²` after one Euler step?",
             "a": ["`1`",
                   "`3/4`",
                   "`5/4`",
                   "`1/4`"],
             "c": 2,
             "why": "The step gives `(1, −1/2)`, and `1 + 1/4 = 5/4 = 1 + h²`. The "
                    "value `1` is what the true solution keeps. The value `3/4` "
                    "would be `1 − h²`, a factor the proof does not give, and "
                    "`1/4` is `v²` alone."},
            {"q": "With `h = 1/4`, what is `x² + v²` after three steps from `(1, 0)`?",
             "a": ["`(17/16)³`",
                   "`3·(17/16)`",
                   "`1 + 3/16`",
                   "`(1/16)³`"],
             "c": 0,
             "why": "Each step multiplies by `17/16`, so three steps multiply by "
                    "`(17/16)³`. Three times `17/16` adds the factors where they "
                    "should compound, and `1 + 3/16` adds the excesses and drops "
                    "the products of them. `(1/16)³` raises the excess and not the "
                    "factor."},
            {"q": "Both runs end at `t = 6`: `h = 1/4` with `24` steps and `h = 1/8` with `48` steps. How do the final radii squared compare?",
             "a": ["They are equal, because the end time is the same",
                   "The run with `h = 1/8` is larger, because it takes more steps",
                   "The run with `h = 1/8` is exactly twice as large",
                   "The run with `h = 1/8` is smaller, because its factor per step is smaller"],
             "c": 3,
             "why": "`(65/64)⁴⁸` is smaller than `(17/16)²⁴`, `≈ 2.10476` against "
                    "`≈ 4.28444`, both rounded. The step count is larger but each factor "
                    "`1 + h²` is much closer to `1`. The two cannot be equal, since "
                    "neither is `1`, and the gain is not doubled."},
            {"q": "Which statement about Euler's method on `x′ = v`, `v′ = −x` from `(1, 0)` is true for every `h > 0`?",
             "a": ["For small enough `h` the points stay on the unit circle",
                   "Every point after the first is outside the unit circle and the radius keeps growing",
                   "The points spiral inward because of rounding",
                   "The points are on the circle only when `h = 1/4`"],
             "c": 1,
             "why": "The radius squared after `n` steps is `(1 + h²)ⁿ`, which is greater "
                    "than `1` for every `n ≥ 1` and grows with `n`. No positive step "
                    "makes the factor `1`. The arithmetic is exact, so rounding "
                    "plays no part."},
        ],
        "mistakes": [
            ("Assuming Euler's method conserves what the equation conserves",
             "The equation keeps `x² + v²` at `1`. The first Euler step from "
             "`(1, 0)` with `h = 1/4` is `(1, −1/4)`, with `x² + v² = 17/16`, and "
             "the second gives `289/256 = (17/16)²`. The method does not know "
             "about the conservation law, and each step moves along the tangent, "
             "which lies outside the circle."),
            ("Treating the factor 1 + h² as negligible because it is close to 1",
             "The factor `17/16` is only `1/16` more than `1`, but it "
             "compounds: `(17/16)²⁴ ≈ 4.28444`, rounded, so the radius at `t = 6` is "
             "`≈ 2.06989` times what it should be. A smaller step lowers the total "
             "(`≈ 2.10476` for `h = 1/8`), and never removes it."),
            ("Blaming the growth on rounding, or trusting exact fractions as the solution",
             "The lab's arithmetic is exact: `17/16` is not a rounded `1.0625`, "
             "and `289/256` is exactly its square. The growth is in the recipe. A "
             "column of exact fractions is exact arithmetic applied to an "
             "approximate method, and the fractions are right while the point is "
             "still not on the true circle."),
        ],
        "standard": (
            "Finish when you can step x′ = v, v′ = −x with Euler's method, prove the factor 1 + h² and compound it over a run.",
            "You should be able to take Euler steps on a pair of equations with "
            "old values on the right, show that x² + v² is multiplied by 1 + h² "
            "per step, read the ratio from the lab, and compare two step sizes "
            "that end at the same time."),
        "note": 'This ends the course. The next, Oscillators, Damping and Resonance, takes the same equation with friction and a push, and asks how the roots <em>α ± βi</em> move as the damping changes.',
    },
]
