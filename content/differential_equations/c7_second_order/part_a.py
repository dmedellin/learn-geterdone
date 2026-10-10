"""Second-Order Linear Equations -- the first half.

Sine and cosine as each other's rates, the second-order equation and its two
constants, the characteristic equation, and the two cases of real roots.

Every figure below is read off the labs, scripts/mathpath/labs/calckit.py (mode
transcendental) and scripts/mathpath/labs/dekit.py and dekit_b.py (modes verify
and char), by executing their shipped JavaScript under node, and pinned in
`expect`. A figure that is rounded is printed with the approximation sign and
says so; everything else is an exact fraction, an exact surd or an exact
symbolic expression.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "sine-cosine-and-their-rates",
        "title": "Sine, Cosine and Their Rates",
        "module": "Sines, cosines and two constants",
        "one_line": "Read the quotients of sin and cos off a rounded table, state sin′ = cos and cos′ = −sin as the claims they demonstrate, and conclude cos″ = −cos.",
        "summary": (
            "The first second-order equation on this course is solved by two functions "
            "you already know, and the reason is a fact about their rates: the rate of "
            "`sin` is `cos`, and the rate of `cos` is `−sin`. The quotients that show it "
            "cannot be fractions, so the lab rounds them, labels them with `≈`, and "
            "prints the number they head for. Taking a rate twice then returns each "
            "function with its sign reversed, which is exactly what the next lesson's "
            "equation asks for."
        ),
        "key": [
            "sin′ t = cos t       cos′ t = −sin t",
            "cos″ t = −cos t      sin″ t = −sin t",
            "(sin h)/h  →  1   as   h → 0",
            "quotients are rounded:  ≈ 0.841471",
            "shown by the table, not proved here",
        ],
        "key_label": "Each is the other's rate, with one sign",
        "concepts_intro": (
            "Three ideas. The first two are the facts the course leans on; the third "
            "is what they give when used twice, and it is the whole reason for the "
            "lesson."
        ),
        "concepts": [
            ("A rate is what the quotients head for",
             "The quotient `(f(a + h) − f(a))/h` is the average rate over a step of "
             "width `h`. When it settles toward one number as `h` is halved again and "
             "again, that number is the rate at `a`. For `sin` and `cos` the "
             "quotients are irrational, so the lab rounds each to six significant "
             "figures and puts `≈` in front of every one; no entry in these tables "
             "is exact."),
            ("Sine and cosine are each other's rates",
             "At `a = 0` the quotients of `sin` head for `1`, which is `cos 0`. At "
             "`a = 0` the quotients of `cos` head for `0`, which is `−sin 0`, and at "
             "`a = 1` they head for a negative number. The pattern across every "
             "place tried is `sin′ = cos` and `cos′ = −sin`, with `t` measured in "
             "radians, and the lesson states it as a claim the table demonstrates."),
            ("Taking the rate twice flips the sign",
             "If `cos′ = −sin` and `sin′ = cos`, then `cos″ = (−sin)′ = −cos` and "
             "`sin″ = (cos)′ = −sin`. Each function is the negative of its own "
             "second rate. That is a differential equation in one line, "
             "`y″ = −y`, and both functions satisfy it."),
        ],
        "read_title": "What the table shows, and what two rates give",
        "read_intro": "The claim, how far a rounded table can carry it, one case where the sign is easy to lose, and the step to the second rate.",
        "body": [
            ("p", "Every earlier rate in this Subject came out as a fraction, because the "
                  "functions were polynomials and the quotient was a polynomial in `h`. "
                  "`sin` and `cos` are not polynomials, and at almost every place the "
                  "value is irrational, so no column of fractions is available. The lab "
                  "here computes the quotients in ordinary floating point, prints each "
                  "rounded to six significant figures behind `≈`, and prints the "
                  "number they head for. The honest status of that last number is the "
                  "important point, and it is stated below. The lab's fourth tile "
                  "divides the last quotient by `f(a)`; it was built for the "
                  "exponential, whose rate is a fixed multiple of its value, and for "
                  "sine and cosine it says nothing, so the first three tiles are the "
                  "ones to read."),
            ("thm", ("The rates of sine and cosine",
                     "For `t` measured in radians, the rate of `sin` at every `t` is "
                     "`cos t`, and the rate of `cos` at every `t` is `−sin t`. In "
                     "symbols: `sin′ t = cos t` and `cos′ t = −sin t`.")),
            ("p", "This is a claim, and the lab demonstrates it at the places you choose "
                  "without proving it. A table of quotients that settle toward a "
                  "number shows the pattern; it cannot show that the pattern continues "
                  "for every smaller `h`, and no table can. The course uses the claim "
                  "from here on, as every course in this Subject uses the rate of an "
                  "exponential, and says so once."),
            ("h3", "The column at zero"),
            ("p", "At `a = 0` the first sine preset starts with `h = 1`. The quotient is "
                  "`(sin 1 − sin 0)/1 = sin 1`, which is `≈ 0.841471` and has no "
                  "fraction form. Halving `h` gives `≈ 0.958851`, `≈ 0.989616` and "
                  "`≈ 0.997398`, and the lab continues to the sixth halving. The "
                  "numbers climb toward `1`, which is `cos 0`, and the gap to `1` is "
                  "cut to about a quarter each time `h` is halved. A quarter, and not "
                  "the half that the cosine table below will show, because the leading "
                  "error of a one-sided quotient is proportional to `h` times the "
                  "second rate of the function at `a`, and `sin″ 0 = −sin 0 = 0`: at "
                  "`0` that term is absent and the next one, proportional to `h²`, is "
                  "what remains."),
            ("math", [
                "h = 1       ≈ 0.841471",
                "h = 1/2     ≈ 0.958851",
                "h = 1/4     ≈ 0.989616",
                "h = 1/8     ≈ 0.997398",
                "claim: these head for cos 0 = 1",
            ]),
            ("h3", "The sign of the cosine's rate"),
            ("p", "The cosine preset at `a = 0` is the one where the sign hides. Its "
                  "quotients start at `≈ −0.459698` and shrink toward `0`, because "
                  "`cos` is at the top of its hill at `0` and is not yet falling. "
                  "That does not tell you the sign of `cos′` in general, since "
                  "`0` has no sign. The preset at `a = 1` does: its quotients are "
                  "all negative and head for `−sin 1 ≈ −0.841471`, because the "
                  "cosine is falling at `1`. A reader who remembers only that the "
                  "rate of `cos` is &ldquo;the other one&rdquo; will write `sin 1`, "
                  "and the table refutes it with a minus sign."),
            ("example", ("Reading the cosine at 1",
                         "The first quotient, `h = 1`, is `cos 2 − cos 1`, which the lab "
                         "prints rounded as `≈ −0.956449`. It is negative because "
                         "`cos` is smaller at `2` than at `1`.",
                         "The last of the seven quotients, at `h = 1/64`, is "
                         "`≈ −0.845658`. It is still moving toward the limit "
                         "`−sin 1 ≈ −0.841471`, and from the third row on the gap shrinks by about a half each time, "
                         "which is what a quotient with an error proportional to `h` does.")),
            ("p", "Radians matter. A degree is `π/180` of a radian, so a table built on "
                  "degrees would head for `cos` times `π/180` instead, and the "
                  "rates would not be each other's. Everything here, and the whole "
                  "course, measures the argument in radians."),
            ("thm", ("Second rates of sine and cosine",
                     "`cos″ t = −cos t` and `sin″ t = −sin t` for every `t`.")),
            ("proof", ["Use the two claims above. The rate of `cos` is `−sin`, so the rate "
                       "of the rate of `cos` is the rate of `−sin`, which is "
                       "`−(sin′)`, and `sin′ = cos`. Hence `cos″ = −cos`.",
                       "The same steps give `sin″ = (cos)′ = −sin`. The proof is only as "
                       "firm as the two claims it uses, which the table "
                       "demonstrates and does not prove."]),
            ("p", "Both identities say that the second rate of the function is minus the "
                  "function. Written as an equation for an unknown `y`, that is "
                  "`y″ = −y`, or `y″ + y = 0`. The next lesson substitutes into it "
                  "and finds that `cos`, `sin` and every combination of them solve it."),
        ],
        "lab": ("calckit", {
            "mode": "transcendental",
            "preset": "sin-at-zero",
            "presets": [
                {"id": "sin-at-zero", "label": "sin at 0, step 1 halved six times",
                 "kind": "sin", "a": 0, "h": 1, "halvings": 6, "expect": {"tqFirst": "≈ 0.841471", "tqLast": "≈ 0.999959", "tqLimit": "cos(0) = 1"}},
                {"id": "cos-at-zero", "label": "cos at 0, step 1 halved six times",
                 "kind": "cos", "a": 0, "h": 1, "halvings": 6, "expect": {"tqFirst": "≈ −0.459698", "tqLast": "≈ −0.00781234", "tqLimit": "−sin(0) = 0"}},
                {"id": "sin-at-one", "label": "sin at 1, step 1 halved six times",
                 "kind": "sin", "a": 1, "h": 1, "halvings": 6, "expect": {"tqLast": "≈ 0.533706", "tqLimit": "cos(1) ≈ 0.540302"}},
                {"id": "cos-at-one", "label": "cos at 1, step 1 halved six times",
                 "kind": "cos", "a": 1, "h": 1, "halvings": 6, "expect": {"tqFirst": "≈ −0.956449", "tqLast": "≈ −0.845658", "tqLimit": "−sin(1) ≈ −0.841471"}},
            ],
            "panel_title": "Quotients of sin and cos, rounded",
            "panel_intro": (
                "Pick a preset and read the first and last quotients and the number "
                "they approach. Every entry behind an approximately sign is rounded to "
                "six significant figures. Then change the place a, or the first h, "
                "and predict the number before you read it."
            ),
        }),
        "steps_title": "Reading a rounded column of quotients",
        "steps_intro": "Five moves. The last is the one that makes the lesson: a rate, used twice.",
        "steps": [
            ("Choose the function and the place",
             "Pick `sin` or `cos` and a place `a`. Write down, before reading the "
             "table, what you expect the rate to be at that place, with its sign."),
            ("Read the first and last quotients",
             "The first is the average rate over the widest step, the last over the "
             "narrowest. Both are rounded, and the tile says so with `≈`."),
            ("Check that the column is settling",
             "Each halving of `h` should move the quotient closer to a single number. "
             "If the changes are not shrinking, the table is not showing a rate."),
            ("Compare with the number the lab names",
             "The lab prints the number the quotients head for, as `cos(1) ≈ 0.540302` "
             "for example. That is the claim, rounded, and the last quotient is near "
             "it but not equal to it."),
            ("Apply the rate to the rate",
             "To get a second rate, take the rate of the result: `cos` becomes "
             "`−sin`, which becomes `−cos`. Count the minus signs as you go."),
        ],
        "worked": {
            "title": "From the sine at zero to the second rate of cosine",
            "intro": [
                "Read four quotients of `sin` at `0`, state what they head for, and "
                "use the two claims to find `cos″`.",
            ],
            "lines": [
                "(sin 1 − sin 0)/1        ≈ 0.841471",
                "(sin(1/2) − sin 0)/(1/2) ≈ 0.958851",
                "h = 1/4                  ≈ 0.989616",
                "h = 1/8                  ≈ 0.997398",
                "claim: they head for cos 0 = 1",
                "cos′ t = −sin t",
                "cos″ t = −(sin t)′ = −cos t",
            ],
            "after": [
                "Every entry in the column is rounded, and the lab labels it so; the "
                "limit `1` is stated as a claim and used from here on.",
                "The second line of the last pair does the work of the lesson: the "
                "minus sign in `cos′ = −sin` stays when the rate is taken again, so "
                "`cos″` is `−cos` and not `cos`.",
            ],
        },
        "quiz_title": "Rates of sin and cos, and the sign",
        "quiz": [
            {"q": "At `a = 0` the lab prints quotients of `cos` that begin at `≈ −0.459698` and shrink toward `0`. Which statement does this support?",
             "a": ["`cos′ 0 = 1`, because `cos 0 = 1`",
                   "`cos′ 0 = 0`, which agrees with `−sin 0`",
                   "`cos′ 0 ≈ −0.459698`, the first quotient",
                   "`cos′ 0 = −1`, because the quotients are negative"],
             "c": 1,
             "why": "The quotients head for `0`, and `−sin 0 = 0`. The value `1` is "
                    "`cos 0` itself, not its rate. The first quotient is the rate over "
                    "the widest step, `≈ −0.459698`, and is only the start of a column "
                    "that is still settling. Negative quotients do not mean the limit "
                    "is `−1`; the limit is the number the column approaches."},
            {"q": "Which pair of statements is right?",
             "a": ["`sin′ = cos` and `cos′ = sin`",
                   "`sin′ = −cos` and `cos′ = −sin`",
                   "`sin′ = cos` and `cos′ = −sin`",
                   "`sin′ = −cos` and `cos′ = sin`"],
             "c": 2,
             "why": "The cosine preset at `a = 1` has negative quotients heading for "
                    "`−sin 1 ≈ −0.841471`, so `cos′ = −sin`; the sine preset at `a = 0` "
                    "heads for `+1 = cos 0`, so `sin′ = cos`. The other pairs each get "
                    "at least one of the two signs wrong."},
            {"q": "From `sin′ = cos` and `cos′ = −sin`, what is `sin″`?",
             "a": ["`sin t`",
                   "`cos t`",
                   "`−cos t`",
                   "`−sin t`"],
             "c": 3,
             "why": "`sin″ = (sin′)′ = (cos)′ = −sin`. The answer `sin t` forgets the "
                    "sign that `cos′` carries. The answer `cos t` is the first rate, "
                    "not the second. The answer `−cos t` would apply the minus sign "
                    "to the wrong step."},
            {"q": "The lab prints the quotients of `sin` at `a = 1` ending at `≈ 0.533706`, and names the limit `cos(1) ≈ 0.540302`. What is the right reading of the last quotient?",
             "a": ["It is exactly `cos 1`, since the lab ends the column there",
                   "It is a rounded quotient for a small step, near but not equal to the claimed rate",
                   "It proves that `sin′ 1 = cos 1`",
                   "It shows that `sin′ 1` is `≈ 0.533706`, so `cos 1` is wrong"],
             "c": 1,
             "why": "The last entry is the average rate over the narrowest step, "
                    "rounded. It is near the limit and below it, and it would move "
                    "closer with another halving. It is not the limit, and a table "
                    "cannot prove the claim. The limit `cos 1` is the number the "
                    "pattern points to, not a figure the table contradicts."},
        ],
        "mistakes": [
            ("Taking the rate of cos to be sin, because it is the other one",
             "The rate of `cos` is `−sin`. At `a = 1` the cosine is falling, so every "
             "quotient is negative: the first is `≈ −0.956449` and they head for "
             "`−sin 1 ≈ −0.841471`. If `cos′` were `+sin 1 ≈ 0.841471` the column "
             "would be positive. Dropping that sign also changes the second rate: "
             "`cos″` would be `+cos`, and `cos` would not satisfy `y″ + y = 0`."),
            ("Reading the last quotient as the rate itself",
             "The last row is the average rate over the narrowest step, rounded. For "
             "`sin` at `1` it is `≈ 0.533706` while the claimed rate is "
             "`cos 1 ≈ 0.540302`. They differ because `h` is not zero, and "
             "the column would keep moving with more halvings. The table shows "
             "the pattern; the limit is a claim."),
            ("Measuring the angle in degrees",
             "The claims are for radians. In degrees the quotients of `sin` at `0` "
             "would head for `π/180 ≈ 0.0174533`, rounded, and not for `1`; the "
             "rates would no longer be each other's, and `y″ + y = 0` would not "
             "have `sin` as a solution. Every `t` in this course is in radians."),
        ],
        "standard": (
            "Finish when you can read the rate of sin or cos off a rounded table, with its sign, and use it twice.",
            "You should be able to say what the quotients of sin and cos head for at "
            "a place you choose, state sin′ = cos and cos′ = −sin as claims the "
            "table demonstrates, say which entries are rounded, and conclude that "
            "the second rate of each is the negative of the function."),
        "note": 'Next, &ldquo;The Second-Order Equation&rdquo; puts <em>cos</em> and <em>sin</em> into <em>y″ + y = 0</em>, checks that the residual is exactly zero, and asks why one starting value is not enough to pick out a single solution.',
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "the-second-order-equation",
        "title": "The Second-Order Equation",
        "module": "Sines, cosines and two constants",
        "one_line": "Verify that cos t, sin t and any combination solve y″ + y = 0 by exact substitution, and explain why two initial values are needed.",
        "summary": (
            "A second-order equation mentions the rate of the rate of the unknown. "
            "The equation `y″ + y = 0` is solved by `cos t` and by `sin t`, and by "
            "every combination `C·cos t + D·sin t`, which the lab checks by "
            "substituting and reading a residual that is exactly zero or is not. "
            "Because there are two free constants, one starting value cannot pick "
            "out one solution; the starting rate is needed as well."
        ),
        "key": [
            "y″ + y = 0:  residual = y″ + y",
            "cos t, sin t,  C·cos t + D·sin t",
            "zero for every t  ⟹  a solution",
            "y(0) = C,   y′(0) = D",
            "two constants, so two starting values",
        ],
        "key_label": "A residual that is zero for every t",
        "concepts_intro": (
            "Three ideas: what the order of an equation counts, what the residual "
            "tells you, and why two constants appear and not one."
        ),
        "concepts": [
            ("The order is the highest rate in the equation",
             "`y′ = 2t` is first order; `y″ + y = 0` is second order, because it "
             "contains `y″`, the rate of the rate. The equation is <em>linear</em> "
             "when `y`, `y′` and `y″` each appear alone and to the first power. "
             "Both equations in this lesson are linear, and the lab prints the "
             "order and says so."),
            ("A solution has a residual that is zero for every t",
             "Move everything to the left to get `y″ + y`, substitute the "
             "candidate and its two rates, and simplify. The result is the "
             "<em>residual</em>. A candidate is a solution when the residual is "
             "zero for every `t`, and not when it is zero at one value, which a "
             "wrong candidate can easily be."),
            ("A solution carries two free constants",
             "If `y` solves `y″ + y = 0` then so does `C·y`, and if `y₁` and `y₂` "
             "both solve it then so does `C·y₁ + D·y₂`. With `cos` and `sin` that "
             "gives a family with two constants. At `t = 0` the value is `C` and "
             "the rate is `D`, so a starting value fixes one of them and a "
             "starting rate fixes the other."),
        ],
        "read_title": "Checking solutions of y″ + y = 0",
        "read_intro": "The equation, the residual that decides, a short proof that combinations stay solutions, and why the family needs two starting values.",
        "body": [
            ("def", ("A second-order linear equation",
                     "An equation in an unknown function `y(t)` whose highest rate "
                     "is `y″`, in which `y`, `y′` and `y″` each appear alone and to "
                     "the first power. A <strong>solution</strong> is a function "
                     "that makes it true for every `t`.",
                     "The <strong>residual</strong> of a candidate is the left side "
                     "minus the right side after substituting the candidate and its "
                     "rates. It is zero for every `t` exactly when the candidate is "
                     "a solution.")),
            ("p", "The lab on this page uses the unknown `y`, and the equation "
                  "`y″ + y = 0`. Read `y` as the position of something that moves "
                  "along a line, `y′` as its velocity and `y″` as its acceleration, "
                  "and the equation says the acceleration is always minus the "
                  "position. Last lesson's claims already give two solutions: "
                  "`cos″ = −cos` and `sin″ = −sin`."),
            ("math", [
                "y = cos t",
                "y′ = −sin t",
                "y″ = −cos t",
                "y″ + y = −cos t + cos t = 0",
            ]),
            ("p", "That residual is exactly zero, and it is zero for every `t` because "
                  "the cancellation does not depend on `t`. The lab does the same "
                  "with the symbolic rates and prints the residual; it never "
                  "evaluates the candidate at a number to decide."),
            ("thm", ("Combinations of solutions are solutions",
                     "If `y₁` and `y₂` solve `y″ + y = 0`, then `C·y₁ + D·y₂` solves "
                     "it for every pair of constants `C` and `D`.")),
            ("proof", ["The rate of a sum is the sum of the rates, and a constant factor "
                       "comes out of a rate, so `(C·y₁ + D·y₂)″ = C·y₁″ + D·y₂″`.",
                       "Then `(C·y₁ + D·y₂)″ + (C·y₁ + D·y₂) = C·(y₁″ + y₁) + "
                       "D·(y₂″ + y₂) = C·0 + D·0 = 0`. Only the form of the equation "
                       "was used: `y″` and `y` each appear once, to the first power."]),
            ("example", ("A candidate that is almost a solution",
                         "Try `y = t·cos t`. The product rule gives "
                         "`y′ = cos t − t·sin t` and `y″ = −2·sin t − t·cos t`.",
                         "The residual is `y″ + y = −2·sin t`, which is zero at "
                         "`t = 0` and at every multiple of `π`, but not for every `t`. "
                         "The lab prints `−2·sin(t)` and the verdict &ldquo;Not a "
                         "solution&rdquo;.")),
            ("h3", "Why one starting value is not enough"),
            ("p", "For the family `y = C·cos t + D·sin t` the starting value is "
                  "`y(0) = C`, since `cos 0 = 1` and `sin 0 = 0`. The rate is "
                  "`y′ = −C·sin t + D·cos t`, so the starting rate is `y′(0) = D`. "
                  "Fixing `y(0) = 1` leaves `D` free: `cos t`, `cos t + sin t` and "
                  "`cos t − 5·sin t` all start at `1` and are different motions. "
                  "The starting rate chooses between them."),
            ("math", [
                "y = C·cos t + D·sin t",
                "y(0) = C",
                "y′(0) = D",
                "y(0) = 1 and y′(0) = −2  give  C = 1, D = −2",
            ]),
            ("p", "The lab's last preset does exactly this. It is given the family "
                  "with two constants and the starting values, and it solves for "
                  "them and prints `C = 1, D = −2`. If the candidate is not linear "
                  "in `C` and `D`, or the equation is not linear, the lab says so "
                  "and refuses."),
        ],
        "lab": ("dekit", {
            "mode": "verify",
            "preset": "cos",
            "presets": [
                {"id": "cos", "label": "y″ + y = 0 with the candidate cos(t)",
                 "equation": "y'' + y = 0", "candidate": "cos(t)", "ic": None, "expect": {"vfOrder": "2", "vfResidual": "0", "vfVerdict": "Solution"}},
                {"id": "combo", "label": "y″ + y = 0 with 3cos(t) − 2sin(t)",
                 "equation": "y'' + y = 0", "candidate": "3cos(t) - 2sin(t)", "ic": None, "expect": {"vfResidual": "0", "vfVerdict": "Solution"}},
                {"id": "not", "label": "y″ + y = 0 with the candidate t cos(t)",
                 "equation": "y'' + y = 0", "candidate": "t cos(t)", "ic": None, "expect": {"vfResidual": "−2·sin(t)", "vfVerdict": "Not a solution"}},
                {"id": "fit", "label": "y″ + y = 0 with C cos(t) + D sin(t), y(0) = 1, y′(0) = −2",
                 "equation": "y'' + y = 0", "candidate": "C cos(t) + D sin(t)", "ic": [0, 1, -2], "expect": {"vfIC": "satisfied", "vfFamily": "C = 1, D = −2"}},
            ],
            "panel_title": "Substitute a candidate into y″ + y = 0",
            "panel_intro": (
                "Choose each preset and read the residual. A residual of 0 means the "
                "candidate is a solution for every t. The last preset has two free "
                "constants and two starting values; it solves for C and D. Then type "
                "your own candidate, such as 5sin(t) or cos(2t), and predict the "
                "residual first."
            ),
        }),
        "steps_title": "Testing a candidate for y″ + y = 0",
        "steps_intro": "The same moves for every second-order equation on this course.",
        "steps": [
            ("Write the residual",
             "Put everything on the left: `y″ + y`. The zero on the right is the "
             "value the residual has to equal."),
            ("Differentiate the candidate twice",
             "Compute `y′` and then `y″`, exactly, with the product rule where "
             "`t` multiplies a sine or cosine."),
            ("Substitute and simplify",
             "Put the candidate and its two rates into the residual and collect like "
             "terms. Do not put in a number for `t`."),
            ("Read the residual",
             "If it is `0` for all `t`, the candidate is a solution. If anything "
             "with a `t` is left, it is not, whatever it does at one value."),
            ("Count the constants",
             "If the candidate is a family, count the free constants and the "
             "starting values you have. You need one starting value for each."),
        ],
        "worked": {
            "title": "Two candidates, and a pair of starting values",
            "intro": [
                "Compare `y = t·cos t` with `y = 3·cos t − 2·sin t` as candidates for "
                "`y″ + y = 0`, then fit the family to `y(0) = 1`, `y′(0) = −2`.",
            ],
            "lines": [
                "y = t·cos t",
                "y′ = cos t − t·sin t",
                "y″ = −2·sin t − t·cos t",
                "y″ + y = −2·sin t     not zero for every t",
                "y = 3·cos t − 2·sin t",
                "y″ = −3·cos t + 2·sin t = −y",
                "y″ + y = 0            a solution",
                "fit:  C = y(0) = 1,   D = y′(0) = −2",
            ],
            "after": [
                "The first residual is `−2·sin t`, which vanishes at `t = 0`. That "
                "alone proves nothing; the residual has to be zero for every `t`, "
                "and here it is not.",
                "In the second, no `t` is left after simplifying, so the "
                "residual is `0` throughout. The last line shows the starting "
                "values reading the constants off directly, because `cos` is `1` "
                "and `sin` is `0` at `t = 0`.",
            ],
        },
        "quiz_title": "Solutions, residuals and constants",
        "quiz": [
            {"q": "Which function solves `y″ + y = 0`?",
             "a": ["`cos(2t)`",
                   "`t·sin t`",
                   "`e^t`",
                   "`2·cos t + 5·sin t`"],
             "c": 3,
             "why": "The combination `2·cos t + 5·sin t` has second rate `−2·cos t − 5·sin t`, "
                    "which is minus itself. For `cos(2t)` the second rate is `−4·cos(2t)`, "
                    "so the residual is `−3·cos(2t)`. For `t·sin t` it is `2·cos t`. For "
                    "`e^t` it is `2·e^t`."},
            {"q": "How many starting values pick out exactly one solution of `y″ + y = 0`?",
             "a": ["One, the value `y(0)`, as for a first-order equation",
                   "Two, the value `y(0)` and the rate `y′(0)`",
                   "Three, adding the second rate `y″(0)`",
                   "None, since `cos` and `sin` are already fixed"],
             "c": 1,
             "why": "The family `C·cos t + D·sin t` has two constants, and `y(0) = C` "
                    "and `y′(0) = D` fix one each. One value leaves `D` free: "
                    "`cos t` and `cos t + sin t` both start at 1. A third value is "
                    "not independent, since the equation gives `y″(0) = −y(0)`. "
                    "Without starting values the whole family remains."},
            {"q": "For `y = C·cos t + D·sin t` with `y(0) = 4` and `y′(0) = −3`, which pair is right?",
             "a": ["`C = −3`, `D = 4`",
                   "`C = 4`, `D = 3`",
                   "`C = −4`, `D = 3`",
                   "`C = 4`, `D = −3`"],
             "c": 3,
             "why": "`y(0) = C` gives `C = 4` and `y′(0) = D` gives `D = −3`, because "
                    "`y′ = −C·sin t + D·cos t`. Swapping the two values gives "
                    "`C = −3`, `D = 4`. Taking `D = 3` loses the sign of the "
                    "starting rate, and `C = −4` loses the sign of the starting value."},
            {"q": "A student finds that the residual for `y = t·cos t` is `−2·sin t`, which is `0` at `t = 0`, and concludes `t·cos t` is a solution. What is wrong?",
             "a": ["Nothing; a residual of 0 at the starting time is all that is needed",
                   "The residual has to be 0 for every `t`, and `−2·sin t` is not",
                   "The residual should have been `−2·cos t`, which is not 0 at `t = 0`",
                   "A product of `t` and a cosine can never be a solution"],
             "c": 1,
             "why": "A solution makes the equation true for every `t`. `−2·sin t` is "
                    "zero at `t = 0` and at multiples of `π` and nowhere between. "
                    "The residual is `−2·sin t`, not `−2·cos t`. Whether a product "
                    "with `t` can be a solution depends on the equation: it can "
                    "be, in the lesson on repeated roots, though not for this one."},
        ],
        "mistakes": [
            ("Expecting one constant, as in a first-order equation",
             "A first-order equation like `y′ = k·y` has solutions `C·e^(kt)` with "
             "one constant, and one starting value fixes it. For `y″ + y = 0` take "
             "`y = C·cos t` and `y(0) = 1`, so `C = 1`. Then `y′(0) = 0`. A start "
             "with `y′(0) = −2` is not matched by any choice of `C`: the family has to "
             "include `D·sin t`, and then `C = 1, D = −2` fits both starting values."),
            ("Calling a candidate a solution because its residual vanishes at one t",
             "For `y = t·cos t` the residual is `−2·sin t`. It is `0` at `t = 0` and "
             "`−2·sin(1) ≈ −1.68294` at `t = 1`, where it is rounded. The equation "
             "must hold for every `t`, and the lab's verdict is &ldquo;Not a "
             "solution&rdquo; for exactly this reason."),
            ("Testing a candidate by drawing it",
             "A plot of `t·cos t` is a wave that looks a good deal like the cosine, "
             "with its amplitude growing. The eye cannot see a residual of "
             "`−2·sin t`. The lab's curve is drawn in floating point to be looked "
             "at; the residual is symbolic, and it is the residual that decides."),
        ],
        "standard": (
            "Finish when you can check any candidate against a second-order equation by substituting it, and say how many starting values it needs.",
            "You should be able to differentiate a candidate twice, simplify the "
            "residual y″ + y, state whether it is zero for every t, and fit the "
            "constants C and D of the family from y(0) and y′(0)."),
        "note": 'Guessing worked here only because the previous lesson supplied <em>cos</em> and <em>sin</em>. &ldquo;The Characteristic Equation&rdquo; replaces the guess by one substitution that works for every equation of the form <em>a·y″ + b·y′ + c·y = 0</em>.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "the-characteristic-equation",
        "title": "The Characteristic Equation",
        "module": "The characteristic equation",
        "one_line": "Substitute y = e^(rt) into a·y″ + b·y′ + c·y = 0, obtain a·r² + b·r + c = 0, and solve it exactly.",
        "summary": (
            "Guessing the solution of a second-order equation does not scale, but one "
            "guess does: `y = e^(rt)`. Its rate and the rate of its rate are "
            "multiples of itself, so the equation collapses to a quadratic in `r` "
            "after the exponential is divided out. The quadratic is called the "
            "characteristic equation, its discriminant names the kind of root, and "
            "the next three lessons turn each kind of root into a solution."
        ),
        "key": [
            "y = e^(rt),  y′ = r·e^(rt),  y″ = r²·e^(rt)",
            "(a·r² + b·r + c)·e^(rt) = 0",
            "e^(rt) is never 0,  so  a·r² + b·r + c = 0",
            "disc = b² − 4ac picks the kind of root",
            "roots: −b ± √disc, over 2a",
        ],
        "key_label": "One substitution, one quadratic",
        "concepts_intro": (
            "Three ideas: why the exponential is the guess, why the equation "
            "becomes a quadratic, and what the discriminant announces."
        ),
        "concepts": [
            ("The exponential is the function whose rates are copies of itself",
             "The rate of `e^(rt)` is `r·e^(rt)`, a number times the same function, "
             "and the rate of that is `r²·e^(rt)`. An equation that adds multiples "
             "of `y`, `y′` and `y″` therefore adds multiples of one function, and "
             "that is the only kind of guess for which the sum can collapse."),
            ("The exponential factors out, and a quadratic remains",
             "Substituting gives `a·r²·e^(rt) + b·r·e^(rt) + c·e^(rt) = 0`, which is "
             "`(a·r² + b·r + c)·e^(rt) = 0`. Because `e^(rt)` is never zero, the "
             "bracket has to be, and that is the <em>characteristic equation</em>. "
             "It is an equation in the number `r`, with no `t` in it."),
            ("The discriminant says which of three things happens",
             "`b² − 4ac` positive means two real roots, zero means one repeated root, "
             "negative means a complex pair. A positive discriminant that is not a "
             "perfect square gives roots with a surd in them, such as "
             "`(1 ± √5)/2`; the lab prints the surd and does not round it."),
        ],
        "read_title": "From the equation to its quadratic",
        "read_intro": "The substitution in full, the quadratic formula from Algebra, and the four presets that show each kind of root.",
        "body": [
            ("p", "Separable Equations, Growth and Decay met `y′ = k·y` and its solution "
                  "`e^(kt)`, and the previous course leaned on that exponential at every "
                  "step. Here the "
                  "equation is `a·y″ + b·y′ + c·y = 0`, with `a`, `b` and `c` constants "
                  "and `a` not zero, and the same function is the natural thing to try. "
                  "The only unknown is the number `r` in the exponent."),
            ("math", [
                "y = e^(rt)",
                "y′ = r·e^(rt)",
                "y″ = r²·e^(rt)",
                "a·r²·e^(rt) + b·r·e^(rt) + c·e^(rt) = 0",
                "(a·r² + b·r + c)·e^(rt) = 0",
            ]),
            ("thm", ("The characteristic equation",
                     "The function `e^(rt)` solves `a·y″ + b·y′ + c·y = 0` exactly when "
                     "`r` solves `a·r² + b·r + c = 0`.")),
            ("proof", ["From the substitution above, `e^(rt)` solves the equation exactly "
                       "when `(a·r² + b·r + c)·e^(rt)` is zero for every `t`.",
                       "The factor `e^(rt)` is positive for every `t`, so the product "
                       "is zero exactly when the bracket is. The bracket has no `t` "
                       "in it, so it is zero exactly when `r` is a root."]),
            ("p", "The rate of the exponential, `(e^(rt))′ = r·e^(rt)`, is the claim "
                  "Rates of Change and the Derivative demonstrated with rounded quotients "
                  "in &ldquo;The Exponential and Its Rate&rdquo;; the proof "
                  "above uses it and nothing else new. What is left is the algebra "
                  "of a quadratic, which is &ldquo;The Quadratic Formula&rdquo; in Algebra's "
                  "Quadratics and Complex Numbers."),
            ("math", [
                "r = (−b ± √(b² − 4ac)) / (2a)",
                "disc = b² − 4ac",
            ]),
            ("h3", "The four presets"),
            ("p", "Each preset is an equation and its quadratic. The lab prints "
                  "the discriminant, the kind of root and the roots, all exactly. "
                  "For `y″ + 3y′ + 2y = 0` the discriminant is `9 − 8 = 1`, a "
                  "perfect square, so the roots are rational. For `y″ + 4y′ + 4y = 0` "
                  "it is `16 − 16 = 0`, one root twice. For `y″ + 2y′ + 5y = 0` it "
                  "is `4 − 20 = −16`, so the roots are the complex pair `−1 ± 2i`."),
            ("example", ("A discriminant that is positive and not a square",
                         "For `y″ − y′ − y = 0` the discriminant is `1 + 4 = 5`. Both "
                         "roots are real, and they are `(1 ± √5)/2`. The lab prints "
                         "that surd exactly.",
                         "Rounded, the roots are `≈ 1.61803` and `≈ −0.618034`; the "
                         "rounded numbers are for the eye only, and the exact surd "
                         "is what the next lessons would carry into a solution.")),
            ("p", "Every equation of this form has a characteristic quadratic, and "
                  "every root of it gives one exponential solution. What is still to "
                  "decide is how to build the full set of solutions from the roots, "
                  "and that depends on the kind of root: one lesson each, starting "
                  "with two real roots."),
        ],
        "lab": ("dekit", {
            "mode": "char",
            "view": "roots",
            "preset": "distinct",
            "presets": [
                {"id": "distinct", "label": "y″ + 3y′ + 2y = 0, two real roots",
                 "a": 1, "b": 3, "c": 2, "ic": None, "expect": {"ceDisc": "1", "ceKind": "two real roots", "ceRoots": "−2, −1"}},
                {"id": "repeated", "label": "y″ + 4y′ + 4y = 0, one root twice",
                 "a": 1, "b": 4, "c": 4, "ic": None, "expect": {"ceDisc": "0", "ceKind": "one repeated root", "ceRoots": "−2 (repeated)"}},
                {"id": "complex", "label": "y″ + 2y′ + 5y = 0, a complex pair",
                 "a": 1, "b": 2, "c": 5, "ic": None, "expect": {"ceDisc": "−16", "ceKind": "complex pair", "ceRoots": "−1 ± 2i"}},
                {"id": "surd", "label": "y″ − y′ − y = 0, roots with a square root",
                 "a": 1, "b": -1, "c": -1, "ic": None, "expect": {"ceDisc": "5", "ceKind": "two real roots (irrational)", "ceRoots": "(1 ± √5)/2"}},
            ],
            "panel_title": "The characteristic quadratic of a·y″ + b·y′ + c·y = 0",
            "panel_intro": (
                "Choose a preset, or type a, b and c. The lab prints the "
                "discriminant, the kind of root and the roots exactly. Before each "
                "preset, compute b² − 4ac yourself and predict the kind."
            ),
        }),
        "steps_title": "From an equation to its roots",
        "steps_intro": "Five moves. The substitution is always the same, so the work is in the quadratic.",
        "steps": [
            ("Read a, b and c with their signs",
             "Take them from `a·y″ + b·y′ + c·y = 0`. For `y″ − y′ − y = 0` they are "
             "`1`, `−1` and `−1`; a missing term has coefficient `0`."),
            ("Write the characteristic equation",
             "Replace `y″` by `r²`, `y′` by `r` and `y` by `1`, keeping the "
             "coefficients: `a·r² + b·r + c = 0`, with a zero on the right."),
            ("Compute the discriminant",
             "`b² − 4ac`. Its sign, and whether it is a perfect square, name the "
             "kind of root before any root is found."),
            ("Apply the quadratic formula",
             "`r = (−b ± √disc)/(2a)`. Keep a surd as a surd, and a negative "
             "discriminant as an `i`."),
            ("Check one root",
             "Put it back into `a·r² + b·r + c`. It should be `0` exactly."),
        ],
        "worked": {
            "title": "y″ + 3y′ + 2y = 0 by substitution",
            "intro": [
                "Substitute `y = e^(rt)`, divide out the exponential, and solve.",
            ],
            "lines": [
                "y = e^(rt),  y′ = r·e^(rt),  y″ = r²·e^(rt)",
                "(r² + 3r + 2)·e^(rt) = 0",
                "e^(rt) is never 0, so  r² + 3r + 2 = 0",
                "disc = 9 − 8 = 1",
                "r = (−3 ± 1)/2",
                "r = −1   or   r = −2",
            ],
            "after": [
                "Each root gives a solution: `e^(−t)` and `e^(−2t)`. Check `r = −1` in "
                "the quadratic: `1 − 3 + 2 = 0`; check `r = −2`: `4 − 6 + 2 = 0`.",
                "The discriminant `1` is a perfect square, and the lab confirms "
                "the kind as two real roots. Putting the two solutions together "
                "into one answer is the work of the next lesson.",
            ],
        },
        "quiz_title": "Substituting, dividing and classifying",
        "quiz": [
            {"q": "What are the roots of the characteristic equation of `y″ − 5y′ + 6y = 0`?",
             "a": ["`−2` and `−3`",
                   "`1` and `6`",
                   "`2` and `3`",
                   "`5` and `6`"],
             "c": 2,
             "why": "The quadratic is `r² − 5r + 6 = (r − 2)(r − 3)`, so the roots are "
                    "`2` and `3`. The roots `−2` and `−3` are what you get by "
                    "reading the signs of `b` and `c` wrongly. The pair `1` and `6` "
                    "multiply to `6` but add to `7`, not `5`, and the pair `5` and "
                    "`6` are the coefficients, not the roots."},
            {"q": "In `(r² + 3r + 2)·e^(rt) = 0`, why may the factor `e^(rt)` be divided out?",
             "a": ["It equals 1 at `t = 0`, so it equals 1 always",
                   "It is never zero, so the bracket must be zero",
                   "`r` is chosen to make `e^(rt)` equal 1",
                   "Its rate equals itself, so it cancels with `y′`"],
             "c": 1,
             "why": "A product is zero only if a factor is, and `e^(rt)` is positive for "
                    "every `t`, so the bracket carries all of the zero. The factor "
                    "is `1` only at `t = 0`. Choosing `r = 0` would make it 1 always, "
                    "but then the equation would just be `c = 0`. The rate of an "
                    "exponential is `r` times itself, not itself."},
            {"q": "For `y″ − y′ − y = 0` the lab prints the discriminant `5`. What does that say?",
             "a": ["Two real roots, rational, because the discriminant is positive",
                   "One repeated root",
                   "Two real roots, irrational, `(1 ± √5)/2`",
                   "A complex pair, because `5` is not a perfect square"],
             "c": 2,
             "why": "A positive discriminant gives two real roots, and `5` is not a "
                    "perfect square, so the roots contain `√5` and are irrational. "
                    "They would be rational for `1`, `4` or `9`. A repeated root "
                    "needs the discriminant to be `0`, and a complex pair needs it "
                    "to be negative; whether it is a square only matters when it "
                    "is positive."},
            {"q": "What is the discriminant of the characteristic equation of `y″ + 9y = 0`?",
             "a": ["`36`",
                   "`−36`",
                   "`9`",
                   "`0`"],
             "c": 1,
             "why": "Here `a = 1`, `b = 0` and `c = 9`, so `b² − 4ac = 0 − 36 = −36`. "
                    "The positive `36` forgets that `4ac` is subtracted. The value `9` "
                    "is `c` alone. The value `0` is `b²`, which ignores the other "
                    "term. A negative discriminant means a complex pair, `±3i`."},
        ],
        "mistakes": [
            ("Writing the characteristic equation as a·r² + b·r + c = y",
             "The right side of the characteristic equation is zero, not `y`. For "
             "`y″ + 3y′ + 2y = 0` and `r = −1` the quadratic `r² + 3r + 2` is "
             "`0`, but `y = e^(−t)` is not `0`. Setting the quadratic equal to `y` "
             "would ask a number to equal a function of `t`, and no `r` does that "
             "for every `t`. The bracket is multiplied by `e^(rt)`, and it is "
             "the product that equals the zero on the right."),
            ("Reading the signs of b and c wrongly",
             "For `y″ − 5y′ + 6y = 0` the coefficients are `1`, `−5` and `6`, and "
             "the roots are `2` and `3`. Reading `b` as `+5` solves `r² + 5r + 6 = 0` "
             "instead and gives `−2` and `−3`. Put `−2` back into the true quadratic "
             "and it gives `(−2)² − 5·(−2) + 6 = 20`, not `0`. One root put back "
             "into the quadratic catches the slip."),
            ("Taking a positive discriminant to mean rational roots",
             "The discriminant of `y″ − y′ − y = 0` is `5`, which is positive, but "
             "the roots `(1 ± √5)/2` are irrational. Only a perfect-square "
             "discriminant gives rational roots. The lab prints the kind as "
             "&ldquo;two real roots (irrational)&rdquo; for exactly this case."),
        ],
        "standard": (
            "Finish when you can turn a·y″ + b·y′ + c·y = 0 into its quadratic and name the kind of root before you solve it.",
            "You should be able to substitute y = e^(rt), obtain a·r² + b·r + c = 0, "
            "compute the discriminant, classify the roots as two real, one repeated "
            "or a complex pair, and solve exactly, keeping a surd as a surd."),
        "note": 'The next lesson takes the first kind of root, two real roots that differ, and turns them into <em>C₁·e^(r₁t) + C₂·e^(r₂t)</em> with the constants fitted from the starting value and the starting rate.',
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "real-distinct-roots",
        "title": "Real Distinct Roots",
        "module": "The characteristic equation",
        "one_line": "Write y = C₁·e^(r₁t) + C₂·e^(r₂t), verify it exactly, and read growth or decay off the signs of the roots.",
        "summary": (
            "When the characteristic quadratic has two different real roots, each "
            "gives an exponential solution, and the general solution is a "
            "combination of the two with a constant in front of each. The two "
            "constants are fitted from the starting value and the starting rate, "
            "and the lab checks the fitted solution by substitution. Whether the "
            "motion dies away, runs off or settles is decided by the signs of the "
            "roots, before any constant is found."
        ),
        "key": [
            "r₁ ≠ r₂ real:  y = C₁·e^(r₁t) + C₂·e^(r₂t)",
            "C₁ + C₂ = y(0)",
            "r₁·C₁ + r₂·C₂ = y′(0)",
            "both roots negative:  every solution decays",
            "a positive root with C ≠ 0:  it grows",
        ],
        "key_label": "Two exponentials, two constants",
        "concepts_intro": (
            "Three ideas: the general solution has both exponentials and a "
            "constant on each, the constants come from a two-by-two fit, and the "
            "roots' signs forecast the motion."),
        "concepts": [
            ("Each root gives a solution, and the sum of multiples is the family",
             "A root `r` of `a·r² + b·r + c = 0` makes `e^(rt)` a solution. If there "
             "are two roots, `C₁·e^(r₁t) + C₂·e^(r₂t)` is a solution for every `C₁` "
             "and `C₂`, since combinations of solutions are solutions. The "
             "constants are what make it general."),
            ("The constants solve two linear equations",
             "At `t = 0` the exponentials are both `1`, so `y(0) = C₁ + C₂`, and the "
             "rate is `y′(0) = r₁·C₁ + r₂·C₂`. Two equations in two unknowns have "
             "exactly one solution whenever `r₁ ≠ r₂`, because the equations "
             "then disagree about the proportions of `C₁` and `C₂`."),
            ("The signs of the roots forecast the long run",
             "A negative root gives a term that shrinks to zero, a positive root "
             "gives a term that grows without limit, and a root of zero gives a "
             "constant. If both roots are negative every solution dies away; if "
             "one is positive, a solution grows unless the constant on that "
             "term is exactly zero."),
        ],
        "read_title": "Two exponentials and two constants",
        "read_intro": "The form, the fit, the exact check, and a case where a growing root is present and the solution decays anyway.",
        "body": [
            ("p", "The three kinds of discriminant give three shapes of answer. "
                  "A positive discriminant gives two distinct real roots `r₁` and "
                  "`r₂`, and the answer is a combination of the two exponentials. "
                  "The word &ldquo;general&rdquo; matters: the form carries both "
                  "constants, and a particular motion is picked out by giving "
                  "them values."),
            ("thm", ("The general solution for distinct real roots",
                     "If `a·r² + b·r + c = 0` has two different real roots `r₁` and `r₂`, "
                     "then every solution of `a·y″ + b·y′ + c·y = 0` has the form "
                     "`y = C₁·e^(r₁t) + C₂·e^(r₂t)`, and every such function is a solution.")),
            ("p", "That every such function is a solution is the combination rule from "
                  "&ldquo;The Second-Order Equation&rdquo; applied to two exponentials, and the "
                  "lab checks it case by case. That there are no other solutions is the "
                  "part this course states and does not prove in full; &ldquo;Superposition "
                  "and the Wronskian&rdquo; shows why two constants always suffice to fit a "
                  "starting value and rate, and that is the part you can use."),
            ("h3", "Fitting the constants"),
            ("p", "Take `y″ + 3y′ + 2y = 0`. The roots are `−1` and `−2`, so "
                  "`y = C₁·e^(−t) + C₂·e^(−2t)`. At `t = 0` the exponentials are `1`, "
                  "so `y(0) = C₁ + C₂`. The rate is `y′ = −C₁·e^(−t) − 2·C₂·e^(−2t)`, so "
                  "`y′(0) = −C₁ − 2·C₂`. With `y(0) = 1` and `y′(0) = 0` the equations "
                  "are `C₁ + C₂ = 1` and `−C₁ − 2·C₂ = 0`."),
            ("math", [
                "C₁ + C₂ = 1",
                "−C₁ − 2·C₂ = 0",
                "add:  −C₂ = 1,   C₂ = −1",
                "C₁ = 1 − C₂ = 2",
                "y = 2·e^(−t) − e^(−2t)",
            ]),
            ("p", "Checking by substitution is what makes the answer trustworthy. "
                  "From `y = 2·e^(−t) − e^(−2t)` the rates are `y′ = −2·e^(−t) + 2·e^(−2t)` "
                  "and `y″ = 2·e^(−t) − 4·e^(−2t)`. Then `y″ + 3y′ + 2y` has the "
                  "`e^(−t)` terms `2 − 6 + 4 = 0` and the `e^(−2t)` terms "
                  "`−4 + 6 − 2 = 0`. The lab prints the same residual, `0`, in its "
                  "status line, and also checks that both starting values hold."),
            ("h3", "Reading the motion from the roots"),
            ("p", "With roots `−1` and `−2` every solution is a sum of two terms that "
                  "shrink, so every solution tends to `0`. With roots `2` and `3`, as "
                  "in `y″ − 5y′ + 6y = 0`, both terms grow. With roots `−1` and `1`, "
                  "as in `y″ − y = 0`, one term shrinks and one grows, and the growing "
                  "one wins as soon as its constant is not zero."),
            ("example", ("A growing root with a zero constant",
                         "For `y″ − y = 0` with `y(0) = 1` and `y′(0) = −1`, the "
                         "equations are `C₁ + C₂ = 1` and `C₁ − C₂ = −1`. Adding gives "
                         "`2·C₁ = 0`, so `C₁ = 0` and `C₂ = 1`, and the solution is "
                         "`y = e^(−t)`, which decays.",
                         "Change the starting rate to `y′(0) = −99/100` and "
                         "`C₁ = 1/200` is not zero, so the term in `e^t` is present "
                         "and, though it starts tiny, it grows past everything. "
                         "A decaying solution here is balanced on one exact value.")),
            ("p", "That balance is why the signs forecast the motion only up to a "
                  "constant being exactly zero. For a starting value and rate chosen "
                  "from measured data that never happens, so the safe forecast is "
                  "that a positive root means growth."),
        ],
        "lab": ("dekit", {
            "mode": "char",
            "view": "solution",
            "preset": "decay",
            "presets": [
                {"id": "decay", "label": "y″ + 3y′ + 2y = 0, y(0) = 1, y′(0) = 0",
                 "a": 1, "b": 3, "c": 2, "ic": [1, 0], "expect": {"ceRoots": "−2, −1", "ceGeneral": "C₁·e^(−t) + C₂·e^(−2t)", "ceSolution": "2·e^(−t) − e^(−2t)"}},
                {"id": "mixed", "label": "y″ − y = 0, y(0) = 1, y′(0) = −1",
                 "a": 1, "b": 0, "c": -1, "ic": [1, -1], "expect": {"ceRoots": "−1, 1", "ceGeneral": "C₁·e^t + C₂·e^(−t)", "ceC": "C₁ = 0, C₂ = 1", "ceSolution": "e^(−t)"}},
                {"id": "grow", "label": "y″ − 5y′ + 6y = 0, y(0) = 0, y′(0) = 1",
                 "a": 1, "b": -5, "c": 6, "ic": [0, 1], "expect": {"ceRoots": "2, 3", "ceGeneral": "C₁·e^(3t) + C₂·e^(2t)", "ceC": "C₁ = 1, C₂ = −1", "ceSolution": "e^(3t) − e^(2t)"}},
            ],
            "panel_title": "Two real roots, and the solution fitted to a start",
            "panel_intro": (
                "Choose a preset and read the roots, the general solution, the "
                "fitted constants and the solution. The status line gives the "
                "residual, which is 0 when the solution is substituted back. "
                "Then edit the starting values and check the constants by hand."
            ),
        }),
        "steps_title": "Solving with two real roots",
        "steps_intro": "Five moves. The fit comes last, and the check after it.",
        "steps": [
            ("Find the roots",
             "Solve `a·r² + b·r + c = 0`. Confirm the discriminant is positive, so "
             "that there are two different real roots."),
            ("Write the general solution",
             "`y = C₁·e^(r₁t) + C₂·e^(r₂t)`, with a constant in front of "
             "each exponential. The lab puts the larger root first, so `C₁` goes "
             "with the larger root."),
            ("Write the two equations for the constants",
             "`C₁ + C₂ = y(0)` and `r₁·C₁ + r₂·C₂ = y′(0)`. The second comes from "
             "the rate of the general solution, taken at `t = 0`."),
            ("Solve them exactly",
             "Eliminate one constant. Keep the answers as fractions."),
            ("Substitute back",
             "Differentiate twice and put the result into the equation. The "
             "residual is `0` or something was mis-copied."),
        ],
        "worked": {
            "title": "y″ + 3y′ + 2y = 0 with y(0) = 1 and y′(0) = 0",
            "intro": [
                "Two real roots, a two-by-two fit, and a substitution as the check.",
            ],
            "lines": [
                "r² + 3r + 2 = 0,   r = −1, −2",
                "y = C₁·e^(−t) + C₂·e^(−2t)",
                "y(0):   C₁ + C₂ = 1",
                "y′(0):  −C₁ − 2·C₂ = 0",
                "C₂ = −1,   C₁ = 2",
                "y = 2·e^(−t) − e^(−2t)",
                "residual:  y″ + 3y′ + 2y = 0",
            ],
            "after": [
                "The second equation is the rate of the general solution at `t = 0`: "
                "`y′ = −C₁·e^(−t) − 2·C₂·e^(−2t)`. A wrong sign there is the "
                "most common slip, and the check at the end catches it.",
                "Both roots are negative, so the solution decays to zero; the term "
                "`−e^(−2t)` goes faster, and the `2·e^(−t)` is left.",
            ],
        },
        "quiz_title": "General solutions and long-run behaviour",
        "quiz": [
            {"q": "What is the general solution of `y″ − 5y′ + 6y = 0`?",
             "a": ["`e^(2t) + e^(3t)`",
                   "`C₁·e^(−2t) + C₂·e^(−3t)`",
                   "`C₁·e^(5t) + C₂·e^(6t)`",
                   "`C₁·e^(2t) + C₂·e^(3t)`"],
             "c": 3,
             "why": "The roots are `2` and `3`, so the general solution is "
                    "`C₁·e^(2t) + C₂·e^(3t)`. The sum with no constants has "
                    "`y(0) = 2` only, so it fits one starting value. The "
                    "negative exponents come from the wrong signs, and `5` and "
                    "`6` are the coefficients, not the roots."},
            {"q": "For `y″ + 3y′ + 2y = 0`, what happens to every solution as `t` grows?",
             "a": ["It tends to `0`, since both roots are negative",
                   "It grows without bound",
                   "It tends to the constant `C₁`",
                   "It oscillates"],
             "c": 0,
             "why": "Both `e^(−t)` and `e^(−2t)` shrink to zero, and a combination "
                    "of two terms that shrink shrinks. Growth needs a positive root, "
                    "a limit of `C₁` needs a root of `0`, and oscillation needs a "
                    "complex pair; none of these is present."},
            {"q": "For `y″ − y = 0` the choice `y(0) = 1`, `y′(0) = −99/100` gives `C₁ = 1/200`. What happens to the solution for large `t`?",
             "a": ["It decays to `0`, since the starting rate is negative",
                   "It stays close to `e^(−t)` for ever, since the start is close",
                   "It grows without bound, since the term `C₁·e^t` is present",
                   "It oscillates, since the roots are `1` and `−1`"],
             "c": 2,
             "why": "`C₁ = (y(0) + y′(0))/2 = 1/200` is not zero, and `e^t` outgrows "
                    "every multiple of `e^(−t)`. Closeness at the start does not last: "
                    "the term in `e^t` grows past the rest. A negative starting rate "
                    "does not stop it, and real roots never give oscillation."},
            {"q": "For `y″ − 5y′ + 6y = 0` with `y(0) = 0` and `y′(0) = 1`, which constants fit `y = C₁·e^(3t) + C₂·e^(2t)`?",
             "a": ["`C₁ = −1`, `C₂ = 1`",
                   "`C₁ = 0`, `C₂ = 1`",
                   "`C₁ = 1`, `C₂ = 1`",
                   "`C₁ = 1`, `C₂ = −1`"],
             "c": 3,
             "why": "`C₁ + C₂ = 0` and `3·C₁ + 2·C₂ = 1`; the first gives `C₂ = −C₁`, "
                    "so `C₁ = 1` and `C₂ = −1`, and `y = e^(3t) − e^(2t)`. Swapping "
                    "them gives `y′(0) = −1`, not `1`. Setting `C₁ = 0` breaks "
                    "the second equation, and `C₁ = C₂ = 1` has `y(0) = 2`."},
        ],
        "mistakes": [
            ("Writing the general solution as e^(r₁t) + e^(r₂t) with no constants",
             "The bare sum has `y(0) = 1 + 1 = 2` and `y′(0) = r₁ + r₂` for every "
             "equation, so it can fit one pair of starting values and no other. For "
             "`y″ + 3y′ + 2y = 0` it would give `y(0) = 2`, `y′(0) = −3`, and "
             "the start `y(0) = 1`, `y′(0) = 0` needs `C₁ = 2` and `C₂ = −1`. The "
             "constants are what make the family large enough to fit."),
            ("Dropping the sign of the root in the exponent",
             "For `y″ + 3y′ + 2y = 0` the roots are `−1` and `−2`, and the "
             "solutions are `e^(−t)` and `e^(−2t)`. Writing `e^(t)` and `e^(2t)` "
             "describes growth where the real motion decays, and fails the "
             "check: `y = e^t` gives `1 + 3 + 2 = 6`, not `0`."),
            ("Forecasting decay from one negative root",
             "In `y″ − y = 0` one root is `−1`, but the other is `1`. A solution "
             "decays only if the constant on the growing term is exactly `0`, "
             "as it is for `y(0) = 1`, `y′(0) = −1`. Any other start grows. The "
             "forecast needs both roots."),
        ],
        "standard": (
            "Finish when you can write and fit the general solution for two real roots, and forecast the long run from their signs.",
            "You should be able to write C₁·e^(r₁t) + C₂·e^(r₂t), set up and solve the "
            "two equations for the constants from y(0) and y′(0), verify the "
            "result by substituting it, and say which solutions decay, grow or settle."),
        "note": 'Two different roots gave two different exponentials. When the quadratic has one root twice there is only one exponential to be had from it, and &ldquo;Repeated Roots&rdquo; finds the second solution somewhere else.',
    },

    # ---------------------------------------------------------------- 05
    {
        "slug": "repeated-roots",
        "title": "Repeated Roots",
        "module": "The characteristic equation",
        "one_line": "Show that one root gives one solution, verify t·e^(rt) as the second by exact substitution, and fit both constants.",
        "summary": (
            "When the discriminant is zero the quadratic has one root, and `e^(rt)` is "
            "only one solution, which would leave the equation with a family of one "
            "constant. The second solution is `t·e^(rt)`, and the lab verifies it "
            "exactly, so the general solution is `(C₁ + C₂·t)·e^(rt)` and the "
            "two constants can again be fitted from a start and a rate."
        ),
        "key": [
            "disc = 0:  one root  r = −b/(2a)",
            "e^(rt) and t·e^(rt) are both solutions",
            "y = (C₁ + C₂·t)·e^(rt)",
            "y(0) = C₁",
            "y′(0) = r·C₁ + C₂",
        ],
        "key_label": "A repeated root needs a factor of t",
        "concepts_intro": (
            "Three ideas: why the usual form falls short, which second function "
            "takes its place, and how the constants are read."),
        "concepts": [
            ("One root gives only one exponential",
             "With a zero discriminant the formula returns the same root twice. "
             "`C₁·e^(rt) + C₂·e^(rt)` is `(C₁ + C₂)·e^(rt)`, which has one "
             "constant: it fits a starting value and cannot also fit a starting "
             "rate."),
            ("The second solution is t times the first",
             "The function `t·e^(rt)` has the rate `(1 + r·t)·e^(rt)` and a second "
             "rate `(2r + r²·t)·e^(rt)`. Substituted into the equation, the result "
             "is a multiple of `a·r² + b·r + c` plus a multiple of `2a·r + b`, and "
             "both are zero when `r` is the repeated root."),
            ("The constants read off simply at t = 0",
             "Because `t = 0` in `(C₁ + C₂·t)·e^(rt)` leaves `C₁`, the starting value is "
             "`y(0) = C₁`. The starting rate adds the two sources, "
             "`y′(0) = r·C₁ + C₂`, since `(C₁ + C₂·t)·e^(rt)` has the rate "
             "`(r·C₁ + C₂ + r·C₂·t)·e^(rt)`."),
        ],
        "read_title": "Where the second solution comes from",
        "read_intro": "Why a single exponential is not enough, the substitution that shows t·e^(rt) works, and a fit with both constants.",
        "body": [
            ("p", "When the discriminant `b² − 4ac` is `0`, the quadratic formula gives "
                  "`r = −b/(2a)` once. For `y″ + 4y′ + 4y = 0` the quadratic is "
                  "`r² + 4r + 4 = (r + 2)²`, and `r = −2` is its only root. "
                  "That gives `e^(−2t)`, and its multiples, a family with one "
                  "constant."),
            ("p", "A family with one constant cannot fit two starting values. The "
                  "equation `y″ + 4y′ + 4y = 0` with `y(0) = 1` and `y′(0) = 1` "
                  "needs `C = 1` from the first and, since `(C·e^(−2t))′ = −2·C·e^(−2t)`, "
                  "`−2·C = 1` from the second. The two demands disagree, and "
                  "a second solution must be found."),
            ("thm", ("The second solution for a repeated root",
                     "If `r` is the only root of `a·r² + b·r + c = 0`, then `t·e^(rt)` "
                     "is a solution of `a·y″ + b·y′ + c·y = 0`, and the general "
                     "solution is `(C₁ + C₂·t)·e^(rt)`.")),
            ("proof", ["The product rule gives `(t·e^(rt))′ = (1 + r·t)·e^(rt)` and "
                       "`(t·e^(rt))″ = (2r + r²·t)·e^(rt)`.",
                       "Substituting, `a·y″ + b·y′ + c·y` is "
                       "`[(a·r² + b·r + c)·t + (2a·r + b)]·e^(rt)`. The first bracket "
                       "is zero because `r` is a root. The second is zero because a "
                       "repeated root is `r = −b/(2a)`. So the residual is zero.",
                       "That `t·e^(rt)` is the second solution is verified here. That "
                       "these two are all the solutions is stated, and &ldquo;Superposition "
                       "and the Wronskian&rdquo; shows why they can fit any starting values."]),
            ("h3", "A concrete check"),
            ("p", "For `y″ + 4y′ + 4y = 0` and `y = t·e^(−2t)` the rates are "
                  "`y′ = (1 − 2t)·e^(−2t)` and `y″ = (4t − 4)·e^(−2t)`. Then "
                  "`y″ + 4y′ + 4y = [(4t − 4) + 4(1 − 2t) + 4t]·e^(−2t) = 0`, because "
                  "the `t` terms are `4 − 8 + 4 = 0` and the constants are "
                  "`−4 + 4 = 0`."),
            ("math", [
                "y = t·e^(−2t)",
                "y′ = (1 − 2t)·e^(−2t)",
                "y″ = (4t − 4)·e^(−2t)",
                "(4t − 4) + 4·(1 − 2t) + 4t = 0",
            ]),
            ("h3", "Fitting both constants"),
            ("p", "With `y(0) = 1` and `y′(0) = 1`, the first condition gives "
                  "`C₁ = 1`. The second is `−2·C₁ + C₂ = 1`, so `C₂ = 3`, and the "
                  "solution is `(1 + 3t)·e^(−2t)`. The factor `1 + 3t` grows, but "
                  "`e^(−2t)` shrinks faster, so the solution rises at first "
                  "and then decays, a shape that one exponential cannot make."),
            ("example", ("A root of zero, repeated",
                         "For `y″ = 0` the quadratic is `r² = 0` with `r = 0` twice, "
                         "and the general solution is `(C₁ + C₂·t)·e^(0·t) = C₁ + C₂·t`, "
                         "a straight line. That is right: a function with a zero second "
                         "rate has a constant first rate, so it is a line.",
                         "With `y(0) = 1` and `y′(0) = 2` the line is `1 + 2t`, and "
                         "the lab prints the constants `C₁ = 1, C₂ = 2`.")),
            ("p", "The repeated root is a boundary case. A tiny change in `b` makes "
                  "the discriminant positive or negative and the form of the "
                  "solution changes, though the solution itself changes only a "
                  "little. It is also the case the next course uses, as the "
                  "dividing line between motion that overshoots and motion that "
                  "does not."),
        ],
        "lab": ("dekit", {
            "mode": "char",
            "view": "solution",
            "preset": "critical",
            "presets": [
                {"id": "critical", "label": "y″ + 4y′ + 4y = 0, y(0) = 1, y′(0) = 1",
                 "a": 1, "b": 4, "c": 4, "ic": [1, 1], "expect": {"ceKind": "one repeated root", "ceGeneral": "(C₁ + C₂·t)·e^(−2t)", "ceC": "C₁ = 1, C₂ = 3"}},
                {"id": "zero-root", "label": "y″ = 0, y(0) = 1, y′(0) = 2",
                 "a": 1, "b": 0, "c": 0, "ic": [1, 2], "expect": {"ceRoots": "0 (repeated)", "ceGeneral": "C₁ + C₂·t", "ceC": "C₁ = 1, C₂ = 2"}},
                {"id": "third", "label": "9y″ + 6y′ + y = 0, y(0) = 3, y′(0) = 0",
                 "a": 9, "b": 6, "c": 1, "ic": [3, 0], "expect": {"ceRoots": "−1/3 (repeated)", "ceGeneral": "(C₁ + C₂·t)·e^(−t/3)", "ceC": "C₁ = 3, C₂ = 1"}},
            ],
            "panel_title": "One root, twice",
            "panel_intro": (
                "Choose a preset and read the kind, the general solution and the "
                "constants. The kind says the root is repeated, and the general "
                "solution has a factor of t. Then change the starting values, "
                "and check the constants by hand."
            ),
        }),
        "steps_title": "Solving with a repeated root",
        "steps_intro": "Five moves. The one that is new is the second solution.",
        "steps": [
            ("Confirm the discriminant is zero",
             "`b² − 4ac = 0`. Then the single root is `r = −b/(2a)`."),
            ("Write both solutions",
             "`e^(rt)` and `t·e^(rt)`. The second is the first with a factor of `t`."),
            ("Write the general solution",
             "`y = (C₁ + C₂·t)·e^(rt)`. The factor `C₁ + C₂·t` is a line in `t`."),
            ("Fit the constants",
             "`C₁ = y(0)` and `C₂ = y′(0) − r·C₁`. Substitute the numbers; keep "
             "the fractions."),
            ("Substitute back",
             "Differentiate twice by the product rule and check the residual. "
             "A forgotten factor of `t` fails here."),
        ],
        "worked": {
            "title": "y″ + 4y′ + 4y = 0 with y(0) = 1 and y′(0) = 1",
            "intro": [
                "One root, the second solution checked, and both constants fitted.",
            ],
            "lines": [
                "(r + 2)² = 0,   r = −2 twice",
                "y = t·e^(−2t)",
                "y′ = (1 − 2t)·e^(−2t)",
                "y″ = (4t − 4)·e^(−2t)",
                "(4t − 4) + 4(1 − 2t) + 4t = 0",
                "y(0) = C₁ = 1",
                "y′(0) = −2·C₁ + C₂ = 1,   C₂ = 3",
                "y = (1 + 3t)·e^(−2t)",
            ],
            "after": [
                "The lab prints the same solution expanded, as `3·t·e^(−2t) + e^(−2t)`. "
                "The fifth line is the exact check: the `t` terms cancel and so do "
                "the constants, and the lab's status line reports a residual of `0`.",
                "Note that `C₂` is `3` and not `1`. The starting rate is "
                "`1`, but `−2·C₁` already contributes `−2`, so the second "
                "term has to supply `3`.",
            ],
        },
        "quiz_title": "Repeated roots and the second solution",
        "quiz": [
            {"q": "What is the general solution of `y″ + 4y′ + 4y = 0`?",
             "a": ["`C₁·e^(−2t) + C₂·e^(2t)`",
                   "`(C₁ + C₂·t)·e^(2t)`",
                   "`(C₁ + C₂·t)·e^(−2t)`",
                   "`C₁·e^(−2t) + C₂·e^(−2t)`"],
             "c": 2,
             "why": "The only root is `−2`, so the solutions are `e^(−2t)` and "
                    "`t·e^(−2t)`. The first option pairs `−2` with `+2`, "
                    "which is not a root. The second has the wrong sign in the "
                    "exponent. The last is `(C₁ + C₂)·e^(−2t)`, which has "
                    "only one constant."},
            {"q": "Why does `C₁·e^(−2t) + C₂·e^(−2t)` fail as a general solution?",
             "a": ["It is not a solution of the equation",
                   "It equals `(C₁ + C₂)·e^(−2t)`, which has only one free constant",
                   "Its exponent should be positive",
                   "It cannot be differentiated twice"],
             "c": 1,
             "why": "Each term does solve the equation; the trouble is that the "
                    "sum is a single multiple of one function, so it cannot fit "
                    "both a starting value and a starting rate. The sign of the exponent "
                    "is right, and the function is easily differentiated."},
            {"q": "For `y″ + 4y′ + 4y = 0` with `y(0) = 2` and `y′(0) = −1`, which solution fits?",
             "a": ["`(2 + 3t)·e^(−2t)`",
                   "`(2 − t)·e^(−2t)`",
                   "`(2 + t)·e^(−2t)`",
                   "`(2 − 5t)·e^(−2t)`"],
             "c": 0,
             "why": "`C₁ = 2`, and `−2·C₁ + C₂ = −1` gives `C₂ = 3`, so the solution "
                    "is `(2 + 3t)·e^(−2t)`. Taking `C₂ = y′(0) = −1` forgets "
                    "that the exponential contributes `−2·C₁`. The options "
                    "`2 + t` and `2 − 5t` come from sign slips in that step."},
            {"q": "The equation `y″ = 0` has the repeated root `0`. Which function solves it with `y(0) = 1` and `y′(0) = 2`?",
             "a": ["`2 + t`",
                   "`1 + t²`",
                   "`2t`",
                   "`1 + 2t`"],
             "c": 3,
             "why": "With `r = 0` the general solution is `C₁ + C₂·t`, `C₁ = y(0) = 1` "
                    "and `C₂ = y′(0) = 2`. Swapping the values gives `2 + t`. "
                    "The function `1 + t²` has the second rate `2`, not `0`, and "
                    "`2t` has `y(0) = 0`."},
        ],
        "mistakes": [
            ("Using C·e^(rt) alone, with one initial value",
             "With one root, `y = C·e^(rt)` looks like the answer, and `y(0) = 1` "
             "fixes `C = 1`. For `y″ + 4y′ + 4y = 0` that is `e^(−2t)`, whose "
             "rate at `0` is `−2`. A start with `y′(0) = 1` is not met, and "
             "no choice of `C` does it. The second solution `t·e^(−2t)` supplies "
             "the missing freedom, giving `(1 + 3t)·e^(−2t)`."),
            ("Reading C₂ as the starting rate",
             "Since `y′(0) = r·C₁ + C₂`, the constant `C₂` is the starting rate "
             "minus `r·C₁`. For `y(0) = 1`, `y′(0) = 1` and `r = −2`, "
             "that is `C₂ = 1 − (−2)(1) = 3`. Taking `C₂ = 1` gives "
             "`(1 + t)·e^(−2t)`, whose rate at `0` is `−1`, not `1`."),
            ("Writing the second solution as another copy of e^(rt)",
             "Both roots equal `−2`, so it is tempting to write `C₁·e^(−2t) + C₂·e^(−2t)`. "
             "That is `(C₁ + C₂)·e^(−2t)`, one function with one constant, and the "
             "lab's constants for `y(0) = 1`, `y′(0) = 1` are `C₁ = 1, C₂ = 3` on "
             "`e^(−2t)` and `t·e^(−2t)`. The residual of the copy is `0`, which is "
             "why it looks right; what fails is the fit, since `e^(−2t)` has "
             "`y′(0) = −2` and not `1`."),
        ],
        "standard": (
            "Finish when you can solve an equation whose characteristic quadratic has a repeated root, and fit both constants.",
            "You should be able to recognise a zero discriminant, write "
            "(C₁ + C₂·t)·e^(rt), check t·e^(rt) by substitution, and solve "
            "C₁ = y(0) and r·C₁ + C₂ = y′(0) exactly."),
        "note": 'Real roots, distinct or repeated, give solutions that do not oscillate. When the discriminant is negative the roots are a complex pair, and the exponential and a sine and cosine appear together: that is &ldquo;Complex Roots and Oscillation&rdquo;.',
    },
]
