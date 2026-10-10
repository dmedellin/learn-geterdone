"""First-Order Linear Equations -- the second half (forcing and stiffness).

Polynomial forcing, exponential and sinusoidal forcing (with the resonant case),
circuits, tanks and loans as one equation, and the step size at which Euler's
method stops following a decay.

Every figure below is read off the lab (dekit, modes linear1 and stiff) by
executing its shipped JavaScript under node, and pinned in `expect`. A figure
that is rounded is printed with the approximation sign and says so; everything
else is an exact fraction or an exact symbolic expression.

Three figures are NOT printed by a lab tile and are labelled in the prose as
rounded values the reader computes from the closed form: the payoff time
`20·ln 6 ≈ 35.8352` (linear1 has no logarithm tile), the balance `≈ 73.2071`
after 17 years (a rounded entry of the lab's Euler table when the step is one
year), and `256/5764801`, which the lab prints when the scheme select of the
stiffness lab is switched to backward.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    {
        "slug": "polynomial-forcing",
        "title": "Polynomial Forcing and Undetermined Coefficients",
        "module": "Forcing",
        "one_line": "Guess a polynomial of the forcing's degree with every lower term, match coefficients from the top down, and solve the exact system.",
        "summary": (
            "When the forcing is a polynomial, a particular solution is a polynomial of "
            "the same degree, with a coefficient for every power down to the constant. "
            "Substituting it and matching the coefficient of each power of `t` gives a "
            "triangular system of linear equations whose solution is a column of exact "
            "fractions. The guess needs its lower terms because a derivative moves each "
            "power down one place, and the power it lands on must be matched too."
        ),
        "key": [
            "y′ + a·y = polynomial of degree n",
            "guess  cₙ·tⁿ + ⋯ + c₁·t + c₀   (all powers)",
            "match tⁿ first:  a·cₙ = coefficient in q",
            "then  a·cₖ + (k+1)·cₖ₊₁ = coefficient of tᵏ",
            "a ≠ 0 gives exactly one such solution",
        ],
        "key_label": "A guess with a coefficient for every power",
        "concepts_intro": (
            "Three ideas. The first says what to guess, the second says why the "
            "guess always works, and the third says what the guess is for once the "
            "constant has been fitted."
        ),
        "concepts": [
            ("The guess has the forcing's degree and every lower power",
             "Differentiating a polynomial lowers its degree by one and multiplying by "
             "`a` keeps it, so for `a ≠ 0` the left side of `y′ + a·y = q` has the same "
             "degree as `y`. To produce a forcing of degree `n` the guess therefore has "
             "degree `n`. It needs every power from `tⁿ` down to the constant, because "
             "the derivative of each term lands on the next power down, and that power "
             "has an equation of its own to satisfy."),
            ("Matching coefficients is a triangular system",
             "Substitute the guess and collect by powers of `t`. The coefficient of "
             "`tᵏ` on the left is `a·cₖ + (k+1)·cₖ₊₁`, and it must equal the "
             "coefficient of `tᵏ` in the forcing. The top equation has one unknown, "
             "`a·cₙ`, and every equation below it brings in one new unknown beside "
             "one already found. Dividing by `a` at each line gives exact fractions "
             "all the way down."),
            ("The particular solution is what the solution ends up following",
             "The general solution is `y_p + C·e^(−a·t)`. For `a > 0` the exponential "
             "dies away and the solution follows the polynomial `y_p`, which keeps "
             "moving: there is no steady state when the forcing keeps changing. For "
             "`a < 0` the exponential grows, and `y_p` is the one solution that "
             "never picks it up."),
        ],
        "read_title": "Guessing a polynomial and matching it power by power",
        "read_intro": "A first failed guess, the method, a worked system, why the system always has an answer, and what changes when the sign of a does.",
        "body": [
            ("p", "Take `y′ + y = t²`. The simplest guess is the forcing itself, "
                  "`y = t²`. Its derivative is `2t`, so the left side is `2t + t²`, "
                  "and the equation wants `t²`. The guess is wrong by exactly the "
                  "leftover `2t`, and that leftover is the whole lesson: the derivative "
                  "creates a power of `t` that the forcing does not have, and something "
                  "in the guess has to cancel it."),
            ("def", ("Undetermined coefficients",
                     "To find a particular solution, write down a function with the "
                     "<em>shape</em> of the forcing and unknown constants in place of "
                     "its coefficients, substitute it into the left side, and match "
                     "the coefficients of like terms on both sides.",
                     "Every unknown is then fixed by an exact linear equation, and "
                     "the finished guess is checked by substituting it back.")),
            ("h3", "Substituting a full quadratic"),
            ("p", "The forcing `t²` has degree two, so the guess is "
                  "`y_p = c₂·t² + c₁·t + c₀`: the `A` and `B` of &ldquo;Homogeneous Plus "
                  "Particular&rdquo;, renamed by the power each one multiplies so that "
                  "the pattern can be written for any degree. Its derivative is "
                  "`2c₂·t + c₁`. Adding "
                  "the two and collecting by powers of `t` gives the left side, and "
                  "the right side is `t²` with no `t` and no constant."),
            ("math", [
                "y_p = c₂·t² + c₁·t + c₀",
                "y_p′ = 2c₂·t + c₁",
                "y_p′ + y_p = c₂·t² + (2c₂ + c₁)·t + (c₁ + c₀)",
                "t²:   c₂ = 1",
                "t:    2c₂ + c₁ = 0,   so   c₁ = −2",
                "1:    c₁ + c₀ = 0,   so   c₀ = 2",
            ]),
            ("p", "So `y_p = t² − 2t + 2`. The check is exact and takes one line: "
                  "`y_p′ = 2t − 2`, and adding `y_p` gives `t²` with nothing left "
                  "over. The `2t` that spoiled the first guess is cancelled by the "
                  "`−2t` in the second power, and the `−2` that produces is "
                  "cancelled by the constant."),
            ("thm", ("One polynomial solution",
                     "If `a ≠ 0` and `q` is a polynomial of degree `n`, then "
                     "`y′ + a·y = q` has exactly one polynomial solution, and its "
                     "degree is `n`.")),
            ("proof", ["Write `y = cₙ·tⁿ + ⋯ + c₀` with `cₙ₊₁ = 0`. The coefficient of "
                       "`tᵏ` in `y′ + a·y` is `a·cₖ + (k+1)·cₖ₊₁`, and it must equal the "
                       "coefficient of `tᵏ` in `q`. For `k = n` this fixes `cₙ`, because "
                       "`a ≠ 0`; each lower `k` then fixes `cₖ` from the one above. "
                       "There is no choice at any line, so there is exactly one "
                       "solution.",
                       "Another polynomial solution would differ from this one by a "
                       "solution of `y′ + a·y = 0`, which is `C·e^(−a·t)`. That is a "
                       "polynomial only when `C = 0`, so there is no other."]),
            ("h3", "A negative a changes the signs and nothing else"),
            ("p", "Take `y′ − 2y = 4t`, so `a = −2`. The forcing has degree one, "
                  "and the guess is `c₁·t + c₀`. Then `c₁ − 2c₁·t − 2c₀ = 4t`: the "
                  "`t` terms give `−2c₁ = 4`, so `c₁ = −2`, and the constants give "
                  "`c₁ − 2c₀ = 0`, so `c₀ = −1`. The particular solution is "
                  "`−2t − 1`."),
            ("example", ("Why the sign of a matters here",
                         "The general solution is `−2t − 1 + C·e^(2t)`. The "
                         "exponential grows, so every solution except the one with "
                         "`C = 0` runs away exponentially, and the polynomial "
                         "`−2t − 1` is the single solution that does not.",
                         "Reading `a` as `+2` instead gives the equations `2c₁ = 4` "
                         "and `c₁ + 2c₀ = 0`, so `c₁ = 2` and `c₀ = −1`; substituting "
                         "`2t − 1` into the real left side `y′ − 2y` leaves "
                         "`2 − 2·(2t − 1) = 4 − 4t`, with the wrong sign on `t` and a "
                         "constant the forcing does not have. The residual announces "
                         "the slip at once.")),
            ("p", "A higher power follows the same pattern at greater length. For "
                  "`y′ + y = t³` the system is `c₃ = 1`, `3c₃ + c₂ = 0`, "
                  "`2c₂ + c₁ = 0` and `c₁ + c₀ = 0`, and the lab prints "
                  "`t³ − 3t² + 6t − 6`. Each coefficient is minus the one before it "
                  "times the exponent of that earlier power: `−3·1`, `−2·(−3)`, "
                  "`−1·6`."),
            ("p", "The case `a = 0` is not this method. The equation is then "
                  "`y′ = q`, which is the antiderivative of Accumulation and the "
                  "Integral, and the answer has degree one more than the forcing. "
                  "Everything above assumed the term `a·y` is there to keep the degree."),
            ("p", "The lab's parts view draws the homogeneous curve, the particular "
                  "curve and their sum. For the first preset the initial value "
                  "`y(0) = 0` is fitted after the two parts are added, as always: "
                  "`2 + C = 0`, so `C = −2`."),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "parts",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "y′ + y = t², y(0) = 0",
                 "equation": "y' + y = t^2", "ic": [0, 0],
                 "expect": {"lfYp": "t² − 2t + 2", "lfC": "−2"}},
                {"id": "line", "label": "y′ − 2y = 4t",
                 "equation": "y' - 2y = 4t", "ic": None,
                 "expect": {"lfYp": "−2t − 1"}},
                {"id": "cubic", "label": "y′ + y = t³",
                 "equation": "y' + y = t^3", "ic": None,
                 "expect": {"lfYp": "t³ − 3t² + 6t − 6"}},
            ],
            "panel_title": "Match the polynomial, then read it off",
            "panel_intro": (
                "The particular-solution tile prints the polynomial with its exact "
                "coefficients, and the status line shows p and q. For each preset, "
                "write the guess and the matching equations by hand, solve them, and "
                "compare with the tile. Then type a forcing of your own, such as "
                "t^2 + 1, and predict the coefficients."),
        }),
        "steps_title": "Finding a polynomial particular solution",
        "steps_intro": "Read the degree, write a guess with all its powers, substitute, match from the top, and check before fitting anything.",
        "steps": [
            ("Put the equation in standard form and read the degree",
             "Divide by the coefficient of `y′`. Then `a` is the coefficient of `y` and "
             "`n` is the degree of the forcing. If `a` is zero the method does not "
             "apply and the answer is an antiderivative."),
            ("Write a guess with every power from n down to 0",
             "`cₙ·tⁿ + ⋯ + c₁·t + c₀`, with a separate unknown for each power, "
             "including any power the forcing is missing."),
            ("Substitute and collect by powers of t",
             "Differentiate the guess, add `a` times the guess, and gather the "
             "coefficient of `tⁿ`, then `tⁿ⁻¹`, down to the constant."),
            ("Match from the top down",
             "Set each collected coefficient equal to the forcing's. The top equation "
             "gives `cₙ = (coefficient)/a`; every later one has a single new unknown."),
            ("Check y_p alone, then fit C last",
             "Substitute `y_p` into `y′ + a·y` and read `q`. Only then write "
             "`y = y_p + C·e^(−a·t)` and use the initial value, subtracting `y_p(t₀)` "
             "before reading `C`."),
        ],
        "worked": {
            "title": "y′ + y = t² by a full quadratic guess",
            "intro": [
                "The forcing has degree two and `a = 1`, so the guess is a quadratic "
                "with three unknowns. The three matching equations are solved from "
                "the top.",
            ],
            "lines": [
                "guess:  y_p = c₂·t² + c₁·t + c₀",
                "y_p′ + y_p = c₂·t² + (2c₂ + c₁)·t + (c₁ + c₀)",
                "t²:  c₂ = 1",
                "t:   2c₂ + c₁ = 0,   so   c₁ = −2",
                "1:   c₁ + c₀ = 0,   so   c₀ = 2",
                "y_p = t² − 2t + 2",
                "check:  (2t − 2) + (t² − 2t + 2) = t²",
                "fit y(0) = 0:  2 + C = 0,   so   C = −2",
            ],
            "after": [
                "The three equations were solved without dividing by anything "
                "awkward, because `a = 1`. With `a = 3` the first line would read "
                "`3c₂ = 1`, and the whole column would be thirds, ninths and "
                "twenty-sevenths; the structure is the same.",
                "For a rehearsal, take the second preset, `y′ − 2y = 4t`. Write the "
                "two-term guess, the two equations, and the answer before you press "
                "the button, then check it by substituting into the left side.",
            ],
        },
        "quiz_title": "Forms, equations and constants",
        "quiz": [
            {"q": "For `y′ + 2y = 5t³`, which family is the smallest one guaranteed to contain a particular solution?",
             "a": ["`c·t³`, one term with the forcing's power",
                   "`c₃·t³ + c₂·t²`, the top two powers",
                   "`c₃·t³ + c₂·t² + c₁·t + c₀`, every power up to 3",
                   "`c₄·t⁴ + c₃·t³ + c₂·t² + c₁·t + c₀`, one degree more"],
             "c": 2,
             "why": "The derivative of each term feeds the power below it, so the "
                    "guess needs every power from `t³` to the constant. One term or two "
                    "leave a power with nothing to match it, and the equations "
                    "contradict each other. The quartic family does contain the answer "
                    "with `c₄ = 0`, but it is larger than it needs to be: the top "
                    "equation `2c₄ = 0` shows the extra term was never required."},
            {"q": "Substituting `c₂·t² + c₁·t + c₀` into `y′ + y = t²` and matching powers of `t`, which equations result?",
             "a": ["`c₂ = 1`, `2c₂ + c₁ = 0`, `c₁ + c₀ = 0`",
                   "`c₂ = 1`, `c₁ = 0`, `c₀ = 0`",
                   "`c₂ = 1`, `2c₂ = c₁`, `c₁ = c₀`",
                   "`c₂ = 1`, `2c₂ + c₁ = 1`, `c₁ + c₀ = 1`"],
             "c": 0,
             "why": "The coefficient of `t` on the left is `2c₂` from the derivative "
                    "plus `c₁` from the term itself, and the forcing has no `t`, so "
                    "the sum is zero. The second choice drops the derivative's "
                    "contribution. The third has the right terms on the wrong sides, "
                    "which gives `c₁ = 2`, `c₀ = 2` and a residual of `4t + 4`. The fourth treats "
                    "the missing `t` and constant of the forcing as ones."},
            {"q": "Which function is a particular solution of `y′ − 2y = 4t`?",
             "a": ["`2t + 1`",
                   "`−2t − 1`",
                   "`−2t + 1`",
                   "`−2t`"],
             "c": 1,
             "why": "For `−2t − 1` the derivative is `−2` and `−2y` is `4t + 2`, "
                    "so the sum is `4t`. For `2t + 1` the sum is `2 − 4t − 2 = −4t`. For "
                    "`−2t + 1` it is `−2 + 4t − 2 = 4t − 4`, and for `−2t` it is "
                    "`−2 + 4t`. In each case the constant or the sign is off by "
                    "exactly the amount the residual shows."},
            {"q": "For `y′ + y = t²` the particular solution is `t² − 2t + 2`. With `y(0) = 0`, what is `C` in `y = y_p + C·e^(−t)`?",
             "a": ["`2`",
                   "`0`",
                   "`1`",
                   "`−2`"],
             "c": 3,
             "why": "At `t = 0` the particular part is `2`, so `2 + C = 0` and "
                    "`C = −2`. The choice `C = 2` has the wrong sign. `C = 0` would "
                    "leave `y(0) = 2`, and `C = 1` would leave `3`; the constant has to "
                    "cancel the particular part's value, not repeat it."},
        ],
        "mistakes": [
            ("Guessing c·t² alone for the forcing t²",
             "For `y′ + y = t²` the guess `y = c·t²` gives `2c·t + c·t²`. The `t²` "
             "terms need `c = 1` and the `t` terms need `2c = 0`, and no `c` does both: "
             "with `c = 1` the residual is exactly `2t`. The derivative produces a "
             "power the forcing does not have, so the guess needs a `t` term and a "
             "constant to cancel it, as the worked example shows."),
            ("Expecting the solution to settle to a constant",
             "A steady state exists when the forcing is a constant. Under `t²` the "
             "forcing keeps changing, and the solution `t² − 2t + 2 + C·e^(−t)` follows "
             "the parabola `t² − 2t + 2`, which does not stop. The exponential part "
             "dies away; what is left is the particular solution, moving. A "
             "polynomial forcing gives a polynomial long-run behaviour."),
            ("Using the wrong sign for a in the matching equations",
             "In `y′ − 2y = 4t` the coefficient of `y` is `−2`. Taking it as `+2` gives "
             "`2c₁ = 4` and `c₁ + 2c₀ = 0`, so `c₁ = 2` and `c₀ = −1`, and `2t − 1` "
             "leaves `2 − 2·(2t − 1) = 4 − 4t` when substituted into `y′ − 2y`: the "
             "`t` term has the wrong sign and a constant is left over. With `a = −2` "
             "the equations are `−2c₁ = 4` and `c₁ − 2c₀ = 0`, giving `−2t − 1`. The "
             "sign is fixed in the standard form, before any guess is made."),
        ],
        "standard": (
            "Finish when you can find a polynomial particular solution of y′ + a·y = q for any polynomial q, and fit the constant afterwards.",
            "You should be able to choose a guess of the forcing's degree with every "
            "lower power, substitute it, write the matching equations from the top "
            "power down, solve them as exact fractions, check the result by "
            "substituting it, and fit the constant after adding the homogeneous "
            "part."),
        "note": 'A polynomial is one of the shapes a derivative leaves alone: it comes back as a polynomial. So are exponentials and the pair of sine and cosine, and &ldquo;Exponential and Sinusoidal Forcing&rdquo; makes the same guess-and-match move for them. One of those has a trap the polynomial does not, which is the case where the guess is already a solution of the homogeneous equation.',
    },

    # ---------------------------------------------------------------- 06
    {
        "slug": "exponential-and-sinusoidal-forcing",
        "title": "Exponential and Sinusoidal Forcing",
        "module": "Forcing",
        "one_line": "Fit A·e^(bt) and A·cos(ωt) + B·sin(ωt) particular solutions with exact coefficients, and multiply by t when the forcing matches the homogeneous solution.",
        "summary": (
            "An exponential forcing is met by an exponential with the same exponent, "
            "a sine or cosine forcing by a combination of both with the same "
            "frequency, and the coefficients are fixed by matching. The sine and "
            "cosine always travel together, because each is the other's derivative. "
            "The one trap is a forcing `e^(−a·t)` that is itself a solution of the "
            "homogeneous equation; the left side then gives zero, and the guess "
            "needs a factor of `t`."
        ),
        "key": [
            "forcing e^(bt):   try A·e^(bt),  A = 1/(a + b)",
            "forcing cos(ωt): try A·cos(ωt) + B·sin(ωt)",
            "cos(ωt) terms, sin(ωt) terms: two equations",
            "b = −a is resonant: try A·t·e^(bt)",
            "a ≠ 0:  the sinusoid never resonates",
        ],
        "key_label": "Three forms of guess, and the one trap",
        "concepts_intro": (
            "Three ideas. Two of them say what to guess; the third says when the "
            "guess collapses and what to do."
        ),
        "concepts": [
            ("An exponential comes back as itself",
             "The derivative of `e^(bt)` is `b·e^(bt)`, so the left side of "
             "`y′ + a·y` applied to `A·e^(bt)` is `(b + a)·A·e^(bt)`. For forcing "
             "`e^(bt)` that gives `A = 1/(a + b)`, and it is exact whenever "
             "`a + b ≠ 0`. The sum, not the difference, is what appears."),
            ("Sine and cosine come back as each other",
             "The derivative of `cos(ωt)` is `−ω·sin(ωt)` and of `sin(ωt)` is "
             "`ω·cos(ωt)`, so a guess with only a cosine produces a sine on the "
             "left that nothing on the right can match. The guess carries both, "
             "`A·cos(ωt) + B·sin(ωt)`, and matching the cosine terms and the sine "
             "terms gives two equations in two unknowns."),
            ("Resonance is a guess the left side annihilates",
             "If the forcing is `e^(−a·t)`, the guess `A·e^(−a·t)` is a solution of the "
             "homogeneous equation, so the left side gives `0` and can never equal "
             "the forcing. The remedy is one more factor of `t`: "
             "`A·t·e^(−a·t)`, whose derivative contributes the term that survives."),
        ],
        "read_title": "Three guesses, the equations they give, and the case that fails",
        "read_intro": "An exponential forcing and its proof, a cosine forcing and its two equations, the general result for a sinusoid, and the resonant case with its factor of t.",
        "body": [
            ("p", "Start with `y′ + 2y = e^t`. Try `y_p = A·e^t`: the derivative is "
                  "`A·e^t`, so the left side is `A·e^t + 2A·e^t = 3A·e^t`, and "
                  "matching `e^t` gives `3A = 1`. The particular solution is "
                  "`(1/3)·e^t`. Nothing needed to be solved: one equation, one "
                  "unknown, and the unknown multiplies the forcing's own shape."),
            ("thm", ("Exponential forcing",
                     "If `a + b ≠ 0`, then `y_p = e^(bt)/(a + b)` is a particular "
                     "solution of `y′ + a·y = e^(bt)`.")),
            ("proof", ["The derivative of `e^(bt)/(a + b)` is `b·e^(bt)/(a + b)`.",
                       "Adding `a` times the function gives "
                       "`(b + a)·e^(bt)/(a + b) = e^(bt)`. The division by `a + b` is "
                       "the only step that needs the condition, and it is exactly "
                       "the condition under which the formula has an answer."]),
            ("h3", "A cosine needs a sine"),
            ("p", "Two facts about sine and cosine are used from here on, and they are "
                  "stated rather than derived: the rate of `sin(t)` is `cos(t)`, and the "
                  "rate of `cos(t)` is `−sin(t)`, so that `cos(ωt)` has rate "
                  "`−ω·sin(ωt)` and `sin(ωt)` has rate `ω·cos(ωt)`. The next course "
                  "opens with them, in &ldquo;Sine, Cosine and Their Rates&rdquo;, where "
                  "their quotients are computed and the claim is demonstrated; here they "
                  "are the claim the matching rests on."),
            ("p", "For `y′ + 2y = cos(t)` the guess `A·cos(t)` alone gives "
                  "`−A·sin(t) + 2A·cos(t)`. The sine term needs `−A = 0` and the "
                  "cosine term needs `2A = 1`, which contradict each other. The "
                  "derivative of the cosine is a sine, so the guess has to contain "
                  "one."),
            ("math", [
                "y_p = A·cos(t) + B·sin(t)",
                "y_p′ = −A·sin(t) + B·cos(t)",
                "y_p′ + 2y_p = (2A + B)·cos(t) + (2B − A)·sin(t)",
                "cos(t) terms:   2A + B = 1",
                "sin(t) terms:   2B − A = 0",
                "A = 2B,   so   5B = 1:   B = 1/5,   A = 2/5",
            ]),
            ("p", "The particular solution is `(2/5)·cos(t) + (1/5)·sin(t)`, and the "
                  "forcing had no sine in it at all. The check is exact: "
                  "`2·(2/5) + 1/5 = 1` for the cosine and `2·(1/5) − 2/5 = 0` for the "
                  "sine. The sine appears because the unknown's rate depends on its "
                  "own value, so the response lags the forcing."),
            ("thm", ("Sinusoidal forcing",
                     "For `a ≠ 0`, a particular solution of `y′ + a·y = cos(ωt)` is "
                     "`A·cos(ωt) + B·sin(ωt)` with `A = a/(a² + ω²)` and "
                     "`B = ω/(a² + ω²)`.")),
            ("proof", ["Matching gives `a·A + ω·B = 1` for the cosine and "
                       "`a·B − ω·A = 0` for the sine. The second equation says "
                       "`A = a·B/ω`, and putting that into the first gives "
                       "`B·(a²/ω + ω) = 1`, so `B = ω/(a² + ω²)` and then "
                       "`A = a/(a² + ω²)`.",
                       "The denominator `a² + ω²` is positive whenever `a ≠ 0`, so the "
                       "system always has an answer. A sinusoid forcing cannot be "
                       "resonant for a real nonzero `a`: the guess never collapses. "
                       "With `a = 2` and `ω = 1` the formulas give `2/5` and `1/5`."]),
            ("h3", "When the forcing is already a solution"),
            ("p", "Take `y′ + 2y = e^(−2t)`. The homogeneous solutions are "
                  "`C·e^(−2t)`, so the forcing is one of them. The guess "
                  "`A·e^(−2t)` gives `−2A·e^(−2t) + 2A·e^(−2t) = 0`, which no "
                  "choice of `A` turns into `e^(−2t)`. The formula "
                  "`1/(a + b)` fails too, since `a + b = 2 − 2 = 0`."),
            ("math", [
                "y_p = A·t·e^(−2t)",
                "y_p′ = A·e^(−2t) − 2A·t·e^(−2t)",
                "y_p′ + 2y_p = A·e^(−2t)",
                "A = 1,   y_p = t·e^(−2t)",
            ]),
            ("example", ("The factor of t is a repair, not a growth",
                         "The general solution is `(t + C)·e^(−2t)`. With "
                         "`y(0) = 1` the constant is `C = 1`, and the solution "
                         "`(t + 1)·e^(−2t)` still goes to zero, because the "
                         "exponential falls faster than `t` rises.",
                         "The `t` is there so that the derivative can leave "
                         "behind a term the left side does not cancel. It is a "
                         "device for finding a solution, and it says nothing about "
                         "whether the solution grows.")),
            ("p", "That leaves three shapes of guess for three shapes of forcing, "
                  "and one test before substituting: does the forcing appear in the "
                  "homogeneous solution `C·e^(−a·t)`? If it does, multiply by `t`. "
                  "The lab's third preset is exactly this case, and its particular-"
                  "solution tile prints the factor of `t`."),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "parts",
            "preset": "cosine",
            "presets": [
                {"id": "cosine", "label": "y′ + 2y = cos(t), y(0) = 0",
                 "equation": "y' + 2y = cos(t)", "ic": [0, 0],
                 "expect": {"lfYp": "(2/5)·cos(t) + (1/5)·sin(t)", "lfSolution": "y = (2/5)·cos(t) + (1/5)·sin(t) − (2/5)·e^(−2t)"}},
                {"id": "exp", "label": "y′ + 2y = e^t, y(0) = 1",
                 "equation": "y' + 2y = e^t", "ic": [0, 1],
                 "expect": {"lfYp": "(1/3)·e^t", "lfC": "2/3"}},
                {"id": "resonant", "label": "y′ + 2y = e^(−2t), y(0) = 1",
                 "equation": "y' + 2y = e^(-2t)", "ic": [0, 1],
                 "expect": {"lfYp": "t·e^(−2t)", "lfSolution": "y = t·e^(−2t) + e^(−2t)"}},
            ],
            "panel_title": "Fit the form, then read the coefficients",
            "panel_intro": (
                "Each preset has a different shape of forcing. Write the guess for "
                "it, say whether it needs a factor of t, and solve the matching "
                "equations by hand; then compare with the particular-solution tile "
                "and the solution tile. Try cos(2t) or e^(3t) as forcing of your "
                "own, and predict the coefficients first."),
        }),
        "steps_title": "Choosing the form and fitting the coefficients",
        "steps_intro": "Read the shape of the forcing, test it against the homogeneous solution, write the guess, match, and check before fitting the constant.",
        "steps": [
            ("Read the forcing's shape",
             "A polynomial, an exponential `e^(bt)`, or a sine or cosine of "
             "`ω·t`. Each has a standard guess with the same exponent or frequency."),
            ("Test it against the homogeneous solution",
             "The homogeneous solution is `C·e^(−a·t)`. If the forcing is "
             "`e^(−a·t)` itself, the guess gets a factor of `t`. A sinusoid "
             "never fails this test when `a ≠ 0`."),
            ("Write the guess with unknown coefficients",
             "`A·e^(bt)`, or `A·cos(ωt) + B·sin(ωt)`, or "
             "`A·t·e^(bt)` in the resonant case. Always both a sine and a "
             "cosine, even if the forcing has only one."),
            ("Substitute and match like terms",
             "Collect the cosine terms and the sine terms separately, or the "
             "coefficient of the one exponential, and set each equal to the "
             "forcing's. Solve the resulting equations exactly."),
            ("Check y_p alone, then fit C last",
             "Substitute `y_p` into `y′ + a·y` and read the forcing back. Then "
             "add `C·e^(−a·t)` and use the initial value with `y_p(t₀)` already "
             "subtracted."),
        ],
        "worked": {
            "title": "y′ + 2y = cos(t) with a cosine and a sine in the guess",
            "intro": [
                "The forcing is a cosine and `a = 2`, so the guess carries both a "
                "cosine and a sine. Matching gives two equations in two unknowns.",
            ],
            "lines": [
                "guess:  y_p = A·cos(t) + B·sin(t)",
                "y_p′ + 2y_p = (2A + B)·cos(t) + (2B − A)·sin(t)",
                "cos(t) terms:  2A + B = 1",
                "sin(t) terms:  2B − A = 0",
                "A = 2B,   so   5B = 1:   B = 1/5,   A = 2/5",
                "y_p = (2/5)·cos(t) + (1/5)·sin(t)",
                "check cos(t):  2·(2/5) + 1/5 = 1",
                "check sin(t):  2·(1/5) − 2/5 = 0",
                "fit y(0) = 0:  2/5 + C = 0,   so   C = −2/5",
            ],
            "after": [
                "The solution is the sum of the oscillating particular part and the "
                "decaying homogeneous part `−(2/5)·e^(−2t)`. The exponential is never "
                "zero, but it is soon smaller than the drawing can show, and what is "
                "left is the particular part: a steady oscillation at the frequency "
                "of the forcing, which no starting value can change.",
                "For a rehearsal, take the third preset, `y′ + 2y = e^(−2t)`. Check "
                "whether the forcing matches the homogeneous solution before writing "
                "any guess, then find the coefficient of `t·e^(−2t)` and the "
                "constant from `y(0) = 1`.",
            ],
        },
        "quiz_title": "Forms, coefficients and the resonant case",
        "quiz": [
            {"q": "Which guess is right for `y′ + 3y = sin(2t)`?",
             "a": ["`A·sin(2t)`",
                   "`A·cos(2t) + B·sin(2t)`",
                   "`A·t·sin(2t)`",
                   "`A·e^(2t)`"],
             "c": 1,
             "why": "The derivative of a sine is a cosine, so both appear in the "
                    "guess. `A·sin(2t)` alone leaves `2A·cos(2t)` with nothing to "
                    "match. The factor of `t` is for resonance, and a sinusoid "
                    "cannot be resonant here because `a² + ω² = 13` is not zero. "
                    "An exponential has the wrong shape altogether."},
            {"q": "For `y′ + 4y = e^(2t)`, what is `A` in `y_p = A·e^(2t)`?",
             "a": ["`1/2`",
                   "`1/4`",
                   "`6`",
                   "`1/6`"],
             "c": 3,
             "why": "The left side gives `(2 + 4)·A·e^(2t) = 6A·e^(2t)`, so `A = 1/6`. "
                    "The choice `1/2` comes from `4 − 2`, with the wrong sign for the "
                    "exponent. `1/4` ignores the derivative. `6` is the coefficient "
                    "the left side produces, not the one that makes it equal the "
                    "forcing."},
            {"q": "For which forcing is `y′ + 3y = q(t)` in the resonant case?",
             "a": ["`q = e^(−3t)`",
                   "`q = e^(3t)`",
                   "`q = cos(3t)`",
                   "`q = e^(−t)`"],
             "c": 0,
             "why": "Resonance needs the forcing to be a homogeneous solution, "
                    "and those are `C·e^(−3t)`. The forcing `e^(3t)` gives "
                    "`a + b = 6`, `e^(−t)` gives `a + b = 2`, and `cos(3t)` gives "
                    "`a² + ω² = 18`; none of the three is zero, so each has an "
                    "ordinary particular solution."},
            {"q": "Why does `A·e^(−2t)` fail as a guess for `y′ + 2y = e^(−2t)`?",
             "a": ["Because the exponent is negative",
                   "Because the left side would give `4A·e^(−2t)`, which is too large",
                   "Because the equation needs a sine to go with it",
                   "Because it solves `y′ + 2y = 0`, so the left side gives zero"],
             "c": 3,
             "why": "`A·e^(−2t)` is a homogeneous solution: its derivative is "
                    "`−2A·e^(−2t)` and adding `2A·e^(−2t)` leaves zero. A left side "
                    "that is always zero cannot equal `e^(−2t)`. A negative exponent "
                    "is no obstacle in itself, since `e^(−3t)` forcing would work "
                    "with `a = 2`. The left side does not give `4A`, and a sine is "
                    "for sinusoids."},
        ],
        "mistakes": [
            ("Guessing A·cos(t) alone for a cosine forcing",
             "For `y′ + 2y = cos(t)` the guess `A·cos(t)` gives "
             "`−A·sin(t) + 2A·cos(t)`. The cosine terms need `2A = 1` and the sine "
             "terms need `−A = 0`, and no `A` does both: with `A = 1/2` the residual "
             "is `−(1/2)·sin(t)`. The derivative of a cosine is a sine, so the "
             "guess has to hold both."),
            ("Using 1/(a − b) instead of 1/(a + b)",
             "For `y′ + 2y = e^t` the slip gives `A = 1/(2 − 1) = 1`. Substituting "
             "`e^t` gives `e^t + 2e^t = 3e^t`, which is three times the forcing. "
             "The derivative contributes `+b` and the term `a·y` contributes "
             "`+a`, so they add: `A = 1/3`, as the lab prints."),
            ("Concluding there is no solution when the guess gives zero",
             "For `y′ + 2y = e^(−2t)` the guess `A·e^(−2t)` gives zero. That says "
             "the guess was wrong, not that the equation cannot be solved. The "
             "function `t·e^(−2t)` has derivative "
             "`e^(−2t) − 2t·e^(−2t)`, and adding `2t·e^(−2t)` leaves exactly "
             "`e^(−2t)`: the residual is zero, and a solution exists."),
        ],
        "standard": (
            "Finish when you can write and fit the particular solution of y′ + a·y = q for an exponential or a sinusoidal q, including the resonant case.",
            "You should be able to choose the guess from the shape of the forcing, "
            "decide by comparing with the homogeneous solution whether it needs a "
            "factor of t, write the matching equations for the cosine and sine "
            "terms or for the single exponential, solve them as exact fractions, "
            "and check the result by substitution."),
        "note": 'With polynomials, exponentials and sinusoids the method now covers every forcing that the lab accepts. What to do with it is the next lesson, and the equations are not abstract ones: a capacitor charging, a tank being flushed and a loan being repaid are each the same equation with their own letters, and the constant forcing makes the particular solution the steady state.',
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "circuits-tanks-and-loans",
        "title": "Circuits, Tanks and Loans",
        "module": "Forcing",
        "one_line": "Write three situations as one equation y′ + a·y = b, read the steady state in each, and compute when a loan balance reaches zero.",
        "summary": (
            "A capacitor charging through a resistor, salt flowing through a "
            "well-mixed tank and a balance growing with interest while it is paid "
            "down are the same equation with different letters. In each, the steady "
            "state is `b/a`, and the sign of `a` decides whether it attracts or "
            "repels. The loan has a negative `a`, which is why the naive payoff "
            "time of balance divided by payment is wrong."
        ),
        "key": [
            "rate of change = gain − loss",
            "collect:  y′ + a·y = b,  steady state b/a",
            "capacitor, tank:  a > 0, steady state pulls",
            "loan:  interest is a gain, a < 0, it repels",
            "payoff:  closed form = 0, then take ln",
        ],
        "key_label": "Three situations, one equation",
        "concepts_intro": (
            "Three ideas: how a situation is turned into the equation, what the "
            "steady state means in each, and why the loan behaves differently."
        ),
        "concepts": [
            ("Write the rate as what comes in minus what goes out",
             "Each equation starts as a sentence: the rate of change of the unknown "
             "is a gain minus a loss. A tank gains salt at a fixed rate and loses "
             "it in proportion to how much is there. A loan gains interest in "
             "proportion to the balance and loses a fixed payment. Collect the "
             "terms in `y` on the left and the equation is `y′ + a·y = b`, with "
             "`a` taking its sign from what is on the right."),
            ("The steady state is where gain equals loss",
             "At `y = b/a` the rate is zero: the tank loses salt exactly as fast as "
             "it gains it, the capacitor draws no current, and the balance grows "
             "by interest exactly as fast as the payment removes it. The steady "
             "state is the particular solution for a constant forcing, from "
             "&ldquo;Homogeneous Plus Particular&rdquo;."),
            ("A negative a turns the steady state around",
             "For the tank and the capacitor, loss is in proportion to the "
             "unknown and `a` is positive, so every solution is pulled toward the "
             "steady state. For the loan the proportional term is a <em>gain</em>, "
             "so `a` is negative, and the steady state is where the balance "
             "stalls: start below it and the balance falls, start above it and "
             "the balance grows for ever."),
        ],
        "read_title": "Three situations, one equation, one question each",
        "read_intro": "The three models with their numbers, the steady state in each, the loan in detail and the payoff time it gives, and the naive answer it corrects.",
        "body": [
            ("p", "All three situations on this page have the same skeleton. There is "
                  "an unknown quantity, a constant source and a loss or gain "
                  "proportional to the unknown. Once the equation is written as "
                  "`y′ + a·y = b` the solution and its steady state follow from "
                  "&ldquo;Constant Coefficients and the Steady State&rdquo; with no new idea."),
            ("math", [
                "situation     unknown     a        b      steady state b/a",
                "capacitor     q           2        5      5/2",
                "tank          y           1/20     10     200",
                "loan          B           −1/20    −6     120",
            ]),
            ("h3", "The capacitor"),
            ("p", "A capacitor with capacitance `C` is charged through a resistor `R` "
                  "from a source of voltage `V`. The charge `q` satisfies "
                  "`R·q′ + q/C = V`. With `R = 1`, `C = 1/2` and `V = 5` in consistent "
                  "units, dividing by `R` gives `q′ + 2q = 5`. The steady state "
                  "is `C·V = 5/2`, the charge at which the capacitor's voltage "
                  "equals the source's. From an empty capacitor "
                  "the charge approaches `5/2` and is below it at every finite time."),
            ("h3", "The tank"),
            ("p", "A tank holds `20` litres of well-mixed brine. Brine at `10` units of "
                  "salt per litre flows in at one litre per minute, and the mixture "
                  "flows out at the same rate. The salt `y` gains `10` per minute "
                  "and loses `y/20` per minute, since a twentieth of the tank leaves "
                  "each minute. So `y′ = 10 − y/20`, which is `y′ + y/20 = 10`. The "
                  "steady state is `200`, the inflow concentration times the volume."),
            ("h3", "The loan"),
            ("p", "A balance of `100` earns interest at `5%` a year, charged "
                  "continuously, and is repaid at `6` a year. The balance gains "
                  "`B/20` and loses `6`, so `B′ = B/20 − 6`. Moving the `B` term to the "
                  "left <em>changes its sign</em>: `B′ − B/20 = −6`, so "
                  "`a = −1/20` and `b = −6`. The steady state is "
                  "`b/a = (−6)/(−1/20) = 120`."),
            ("p", "That number has a meaning. At a balance of `120` the interest is "
                  "`120/20 = 6` a year, exactly the payment, so the balance neither "
                  "falls nor grows. It is a knife edge, not a destination: "
                  "`a < 0` makes it repelling. The loan starts at `100`, below "
                  "it, so the gap is `−20` and grows."),
            ("math", [
                "B = 120 + (100 − 120)·e^(t/20)",
                "B = 120 − 20·e^(t/20)",
                "B = 0:   e^(t/20) = 6",
                "t = 20·ln 6 ≈ 35.8352 years",
            ]),
            ("p", "The payoff time is where the balance is zero. It needs a natural "
                  "logarithm, `ln 6 ≈ 1.79176`, which is irrational, so the "
                  "figure `≈ 35.8352` is rounded. The lab does not print a payoff "
                  "time; it prints the closed form, and the number is yours to compute "
                  "from it. You can check the sign change in the lab's Euler view "
                  "with a step of one year and at least `36` steps: the rounded "
                  "closed-form column falls through zero between year `35` and year "
                  "`36`."),
            ("p", "Compare the naive estimate. A balance of `100` repaid at `6` a "
                  "year would take `100/6 ≈ 16.6667` years if no interest were charged. "
                  "At year `17` the closed form gives `120 − 20·e^(17/20) ≈ 73.2071`, "
                  "rounded: more than seventy are still owed. The real payoff "
                  "is more than twice as long, because the balance gains interest "
                  "all the way down."),
            ("example", ("The same loan starting just above the steady state",
                         "Start the same loan at `B(0) = 130` instead. The gap to "
                         "`120` is `+10`, so `B = 120 + 10·e^(t/20)`, and the "
                         "balance grows without limit: the interest on `130` is "
                         "`6.5` a year and the payment is only `6`.",
                         "The knife edge is exactly `B = 120`. A payment of `6` a year "
                         "pays off a loan of `100` but not a loan of `130`, and "
                         "the equation says so at once through the sign of the gap.")),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "solve",
            "preset": "rc",
            "presets": [
                {"id": "rc", "label": "q′ + 2q = 5, q(0) = 0",
                 "equation": "q' + 2q = 5", "ic": [0, 0],
                 "expect": {"lfSteady": "5/2", "lfSolution": "q = 5/2 − (5/2)·e^(−2t)"}},
                {"id": "tank", "label": "y′ + y/20 = 10, y(0) = 0",
                 "equation": "y' + y/20 = 10", "ic": [0, 0],
                 "expect": {"lfSteady": "200", "lfSolution": "y = 200 − 200·e^(−t/20)"}},
                {"id": "loan", "label": "B′ − B/20 = −6, B(0) = 100",
                 "equation": "B' - B/20 = -6", "ic": [0, 100],
                 "expect": {"lfSteady": "120 (repelling)", "lfSolution": "B = 120 − 20·e^(t/20)"}},
                {"id": "above", "label": "B′ − B/20 = −6, B(0) = 130",
                 "equation": "B' - B/20 = -6", "ic": [0, 130],
                 "expect": {"lfSteady": "120 (repelling)", "lfSolution": "B = 120 + 10·e^(t/20)"}},
            ],
            "panel_title": "One equation, three situations",
            "panel_intro": (
                "Each preset is one of the situations, with its steady state and "
                "closed form in the tiles. Say what the unknown is, what comes in "
                "and what goes out, and whether the steady state attracts, then "
                "compare. The loan presets differ only in the starting balance. "
                "Switch the view to Euler's steps with a step of 1 and the step "
                "count raised to 36 or more to read the rounded balance year by year."),
        }),
        "steps_title": "From a situation to a steady state",
        "steps_intro": "Name the unknown, write gain and loss, collect into standard form with the signs checked, and read the steady state before solving.",
        "steps": [
            ("Name the unknown and the rate",
             "A charge, an amount of salt or a balance, and its rate of change "
             "per unit of time. Fix the unit of time once."),
            ("Write the rate as gain minus loss",
             "`y′ = (what comes in) − (what goes out)`. A flow in proportion to "
             "the unknown carries the unknown; a fixed flow does not."),
            ("Collect into y′ + a·y = b",
             "Move every term in `y` to the left and change its sign as it crosses. "
             "A proportional gain, like interest, becomes a negative `a`."),
            ("Read the steady state b/a and its direction",
             "`a > 0` attracts and `a < 0` repels. Say what the number means in "
             "the situation: a charge, an amount of salt, a balance."),
            ("Solve, then answer the question asked",
             "Write `y = b/a + (y₀ − b/a)·e^(−a·t)`. For a payoff, set it to "
             "zero and take a logarithm; the answer is irrational and printed "
             "rounded."),
        ],
        "worked": {
            "title": "How long a loan of 100 takes at 5% with 6 paid a year",
            "intro": [
                "The balance gains `B/20` a year in interest and loses `6` in payments. "
                "The equation is written, the steady state read, and the balance set "
                "to zero.",
            ],
            "lines": [
                "B′ = B/20 − 6,   B(0) = 100",
                "B′ − B/20 = −6:   a = −1/20,   b = −6",
                "steady state:  B* = b/a = 120   (repelling)",
                "gap at the start:  100 − 120 = −20",
                "B = 120 − 20·e^(t/20)",
                "B = 0:   e^(t/20) = 6",
                "t = 20·ln 6 ≈ 35.8352 years",
                "naive estimate:  100/6 ≈ 16.6667 years",
            ],
            "after": [
                "The payoff time is more than twice the naive estimate. The naive "
                "estimate assumes each payment of `6` takes `6` off the balance. "
                "It does not: interest of about `5` a year on a balance near `100` "
                "puts most of that back, so the balance falls by only about `1` a "
                "year at first.",
                "For a rehearsal, run the tank. Write `y′ = 10 − y/20`, collect it "
                "to `y′ + y/20 = 10`, read the steady state before the lab does, "
                "and check that it is `200` and attracting.",
            ],
        },
        "quiz_title": "Models, steady states and payoffs",
        "quiz": [
            {"q": "A tank satisfies `y′ + y/20 = 10`. What is the steady-state amount?",
             "a": ["`10`",
                   "`1/2`",
                   "`200`",
                   "`20`"],
             "c": 2,
             "why": "The steady state is `b/a = 10/(1/20) = 200`. The forcing `10` is "
                    "not the steady state, since `y = 10` gives a rate of `9.5`. "
                    "The value `1/2` is `10·a`, not `b/a`. And `20` is the volume, "
                    "which is the factor between `200` and the inflow concentration "
                    "`10`."},
            {"q": "The loan `B′ − B/20 = −6` starts at `B(0) = 130`. What does the balance do?",
             "a": ["It falls to zero in about 36 years",
                   "It grows without limit",
                   "It settles at `120`",
                   "It stays at `130`"],
             "c": 1,
             "why": "The steady state `120` repels, because `a = −1/20` is negative, "
                    "and `130` is above it. The gap `+10` is multiplied by `e^(t/20)`, "
                    "so `B = 120 + 10·e^(t/20)` grows. Settling at `120` would be "
                    "the behaviour of an attracting steady state. Staying at `130` "
                    "would need a rate of zero, and the rate is `6.5 − 6 = 0.5`. The "
                    "36 years is the answer for a start of `100`."},
            {"q": "A tank of 50 litres has brine of 3 units per litre flowing in at 2 litres per minute, with the same flow out. What is the steady-state amount of salt?",
             "a": ["`6`",
                   "`75`",
                   "`25`",
                   "`150`"],
             "c": 3,
             "why": "The equation is `y′ = 3·2 − (2/50)·y`, so `a = 1/25`, `b = 6` "
                    "and `b/a = 150`, which is the concentration `3` times the volume "
                    "`50`. The value `6` is the inflow of salt per minute. `25` is "
                    "`1/a`, the time scale, and `75` is half the steady state."},
            {"q": "Why is `100/6` years wrong for a loan of 100 at 5% repaid at 6 a year?",
             "a": ["The balance gains interest while it is repaid, so each payment removes less than 6 from it",
                   "The steady state of the loan is 100",
                   "A loan can never be repaid",
                   "The exponential makes the time shorter than `100/6`"],
             "c": 0,
             "why": "The balance falls by the payment minus the interest it earns, "
                    "which is `6 − B/20`, and that is less than `6`. The steady state "
                    "is `120`, not `100`. The loan can be repaid, because `100` is below "
                    "the steady state. And the actual time, `20·ln 6 ≈ 35.8352` years, "
                    "is longer than `100/6`, not shorter."},
        ],
        "mistakes": [
            ("Taking 100/6 as the payoff time",
             "A balance of `100` repaid at `6` a year is not paid off in "
             "`100/6 ≈ 16.6667` years. At year `17` the closed form still gives "
             "`≈ 73.2071`, rounded, and the balance reaches zero only at "
             "`20·ln 6 ≈ 35.8352` years. The estimate ignores the interest that "
             "is charged on the way down."),
            ("Reading the steady state of a loan as where the balance ends up",
             "The steady state `120` repels, because `a = −1/20`. Starting at `100` "
             "the balance moves away from `120`, downward, and through zero; "
             "starting at `130` it moves away upward. A solution settles at the "
             "steady state only when `a` is positive, as for the tank and the "
             "capacitor."),
            ("Moving the interest term without changing its sign",
             "From `B′ = B/20 − 6` the slip gives `B′ + B/20 = −6`, so `a = +1/20` "
             "and the steady state `−120`, attracting. That is a different loan: from "
             "`100` its balance is `−120 + 220·e^(−t/20)`, which falls through zero "
             "at `20·ln(11/6) ≈ 12.1227` years, sooner than even the no-interest "
             "estimate, and then keeps falling toward `−120`. Interest cannot clear a "
             "loan faster than paying with no interest at all, and that impossibility "
             "is the sign that a term crossed the equals sign with its sign unchanged. "
             "Collecting the terms carefully gives `B′ − B/20 = −6`."),
        ],
        "standard": (
            "Finish when you can write a charging capacitor, a flowing tank or a loan as y′ + a·y = b, name the steady state, and find a payoff time.",
            "You should be able to write the rate as gain minus loss, collect it into "
            "standard form with the signs checked, read the steady state b/a and "
            "say whether it attracts or repels, write the closed form, and find "
            "when a loan balance reaches zero by setting the closed form to zero, "
            "giving the answer rounded."),
        "note": 'The steady state in these models is the particular solution for a constant forcing. What the models do not show is how the equation behaves when it is solved by a computer, one step at a time. The last lesson of the course returns to Euler&rsquo;s method on the simplest decay, where the step size alone decides whether the answer follows the curve or leaves it.',
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "stiffness-when-the-step-is-too-big",
        "title": "Stiffness: When the Step Is Too Big",
        "module": "Stiffness",
        "one_line": "Show Euler's factor 1 − a·h on y′ = −a·y, derive the bound h < 2/a for decay, and show that the backward factor decays at every step size.",
        "summary": (
            "On `y′ = −a·y` one Euler step multiplies the value by the exact "
            "factor `1 − a·h`, and the whole column is a geometric sequence in that "
            "factor. The steps decay only when the factor lies between `−1` and `1`, "
            "which is `h < 2/a`. A larger step makes the exact fractions grow while "
            "the true solution falls to nearly zero. The backward step divides by "
            "`1 + a·h` instead, and that factor lies between `0` and `1` for every "
            "step size."
        ),
        "key": [
            "Euler on y′ = −a·y:  yₙ = y₀·(1 − a·h)ⁿ",
            "decays smoothly when h < 1/a",
            "wobbles but decays when 1/a < h < 2/a",
            "grows when h > 2/a",
            "backward: yₙ₊₁ = yₙ/(1 + a·h), always decays",
        ],
        "key_label": "The factor that decides whether Euler decays",
        "concepts_intro": (
            "Three ideas: the factor, the bound it gives, and the different step "
            "that has no bound."
        ),
        "concepts": [
            ("One Euler step multiplies by one number",
             "For `y′ = −a·y` the step is `yₙ₊₁ = yₙ + h·(−a·yₙ) = (1 − a·h)·yₙ`. "
             "The factor `1 − a·h` is the same at every step, so "
             "`yₙ = y₀·(1 − a·h)ⁿ` exactly: a geometric sequence of fractions, "
             "whatever the size of `a` or `h`."),
            ("The steps decay only if the factor's size is below one",
             "A geometric sequence goes to zero exactly when the size of its "
             "factor is less than `1`. The condition `|1 − a·h| < 1` means "
             "`−1 < 1 − a·h < 1`, which is `0 < a·h < 2`, and so `h < 2/a`. "
             "The true solution decays for every `h`, so the bound belongs to "
             "the method alone."),
            ("The backward step divides instead",
             "Backward Euler evaluates the rate at the new point: "
             "`yₙ₊₁ = yₙ + h·(−a·yₙ₊₁)`. Solving for `yₙ₊₁` gives "
             "`yₙ₊₁ = yₙ/(1 + a·h)`. For `a > 0` and `h > 0` the denominator "
             "exceeds `1`, so the factor lies strictly between `0` and `1` "
             "at every step size."),
        ],
        "read_title": "The factor, its bound, and a step that has none",
        "read_intro": "Euler's factor, what each range of the step does, the bound with its proof, the lab's three steps on one decay, and the backward alternative with its limits.",
        "body": [
            ("p", "Take `y′ = −5y` with `y(0) = 1`. The true solution is "
                  "`e^(−5t)`, which falls toward zero quickly. The question for "
                  "this lesson is whether Euler's polygon falls with it, and "
                  "the answer depends on the step alone."),
            ("math", [
                "yₙ₊₁ = yₙ + h·(−5·yₙ) = (1 − 5h)·yₙ",
                "yₙ = (1 − 5h)ⁿ",
            ]),
            ("p", "Everything is carried by the factor `ρ = 1 − a·h`, an exact "
                  "fraction. Its sign says whether successive values change sign, "
                  "and its size says whether they shrink."),
            ("thm", ("The step bound for decay",
                     "Forward Euler on `y′ = −a·y` with `a > 0` goes to zero for "
                     "every starting value exactly when `0 < h < 2/a`.")),
            ("proof", ["Euler gives `yₙ = y₀·ρⁿ` with `ρ = 1 − a·h`. A geometric "
                       "sequence goes to zero for every start when `|ρ| < 1`, and "
                       "does not when `|ρ| ≥ 1`.",
                       "Now `|1 − a·h| < 1` means `−1 < 1 − a·h < 1`. Subtracting "
                       "`1` and changing signs gives `0 < a·h < 2`, which is "
                       "`0 < h < 2/a`. At `h = 2/a` the factor is exactly `−1` and "
                       "the values alternate forever without shrinking."]),
            ("h3", "Three steps on one decay"),
            ("p", "For `a = 5` the bound is `2/5`, and a second marker, `1/a = 1/5`, "
                  "is where the factor changes sign. Below `1/5` the factor is "
                  "positive and the steps decay smoothly. Between `1/5` and "
                  "`2/5` it is negative: the values alternate in sign and still "
                  "shrink. Above `2/5` they alternate and grow."),
            ("math", [
                "h      factor   what the steps do        y₈ (exact)",
                "1/10   1/2      decays                   1/256",
                "1/4    −1/4     oscillates and decays    1/65536",
                "1/2    −3/2     oscillates and grows     6561/256",
            ]),
            ("p", "The last row is the preset the lab opens with. With `h = 1/2` "
                  "and eight steps the polygon reaches `t = 4`, where it holds "
                  "`(3/2)⁸ = 6561/256`, which is about `25.6289`, rounded. The "
                  "true value is `e^(−20) ≈ 2.06115·10⁻⁹`, also rounded, and the "
                  "tile writes it as `2.06115e-9`. Every "
                  "fraction in the column is correct arithmetic; the method has "
                  "turned a decay into a growth."),
            ("h3", "Small is relative to 2/a"),
            ("p", "A step of `1/2` looks small, and for a slow decay such as "
                  "`y′ = −y` it is: the bound there is `2`. The bound shrinks as "
                  "`a` grows, so a quickly decaying component forces a small "
                  "step even after it has stopped mattering to the answer. "
                  "That is what the word <em>stiff</em> names here: the step "
                  "is capped by the fastest decay in the problem, not by the "
                  "accuracy one wants."),
            ("h3", "The backward step has no bound"),
            ("p", "The backward factor `1/(1 + a·h)` is between `0` and `1` "
                  "whatever `h` is. For `a = 5` and `h = 1/2` it is "
                  "`1/(1 + 5/2) = 2/7`, so the steps decay, where the forward "
                  "factor was `−3/2`. Stable does not mean accurate: the true "
                  "factor over one step is `e^(−5/2) ≈ 0.082085`, rounded, and "
                  "`2/7 ≈ 0.285714` is more than three times as large. After eight steps the backward "
                  "column holds `(2/7)⁸ = 256/5764801`, still far above the true "
                  "value, but it has not blown up."),
            ("example", ("What the backward method costs",
                         "For `y′ = −a·y` the backward step is solved by one "
                         "division, because the equation is linear in `y`. For a "
                         "nonlinear right-hand side the new value appears on both "
                         "sides inside the function, and finding it takes an "
                         "equation to be solved at every step.",
                         "That cost is the price of the bound's disappearing. This "
                         "course shows the one linear case; the general theory is "
                         "not part of it.")),
        ],
        "lab": ("dekit", {
            "mode": "stiff",
            "scheme": "forward",
            "preset": "grows",
            "presets": [
                {"id": "grows", "label": "a = 5, h = 1/2",
                 "a": "5", "y0": "1", "h": "1/2", "n": 8,
                 "expect": {"skFactor": "−3/2", "skVerdict": "oscillates and grows", "skLimit": "h < 2/5", "skLast": "6561/256", "skTrue": "≈ 2.06115e-9", "skBackward": "2/7"}},
                {"id": "wobbles", "label": "a = 5, h = 1/4",
                 "a": "5", "y0": "1", "h": "1/4", "n": 8,
                 "expect": {"skFactor": "−1/4", "skVerdict": "oscillates and decays", "skLimit": "h < 2/5", "skLast": "1/65536", "skBackward": "4/9"}},
                {"id": "fine", "label": "a = 5, h = 1/10",
                 "a": "5", "y0": "1", "h": "1/10", "n": 8,
                 "expect": {"skFactor": "1/2", "skVerdict": "decays", "skLimit": "h < 2/5", "skLast": "1/256", "skBackward": "2/3"}},
            ],
            "panel_title": "The same decay at three step sizes",
            "panel_intro": (
                "Each preset steps y' = -5y from 1 with a different h. The factor "
                "tile is exact, the verdict follows from it, and the limit tile "
                "gives the bound 2/a. Switch the scheme to backward to see the "
                "other factor, then try a larger decay rate with the step held "
                "fixed."),
        }),
        "steps_title": "Deciding whether a step size is safe",
        "steps_intro": "Compute the factor, read its size and sign, compare the step with the bound, and only then trust the column.",
        "steps": [
            ("Write the equation as y′ = −a·y",
             "Read `a`, which is positive for a decay. For an equation with a "
             "forcing, the gap to the steady state obeys this equation, so `a` "
             "is the same."),
            ("Compute the forward factor 1 − a·h",
             "An exact fraction. Then `yₙ = y₀·(1 − a·h)ⁿ`, and every value "
             "in the Euler column is a power of the factor."),
            ("Read its sign and size",
             "Between `0` and `1`: smooth decay. Between `−1` and `0`: "
             "alternating and decaying. Exactly `−1`: alternating without "
             "shrinking. Below `−1`: alternating and growing."),
            ("Compare h with 2/a",
             "The steps decay exactly when `h < 2/a`. If the step is larger, "
             "shrink it, or change the method."),
            ("Compute the backward factor if the bound is too tight",
             "`1/(1 + a·h)`, between `0` and `1` for every `h`. It decays, but "
             "how closely it follows the true decay is a separate question."),
        ],
        "worked": {
            "title": "Euler on y′ = −5y with a step of 1/2",
            "intro": [
                "The decay rate is `a = 5` and the step is `h = 1/2`, so the "
                "bound is `2/5` and the step exceeds it. The forward factor "
                "and the backward factor are both exact.",
            ],
            "lines": [
                "forward factor:  1 − 5·(1/2) = −3/2",
                "bound:  h < 2/5,   but  h = 1/2",
                "y₈ = (−3/2)⁸ = 6561/256 ≈ 25.6289",
                "true  y(4) = e^(−20) ≈ 2.06115·10⁻⁹",
                "backward factor:  1/(1 + 5/2) = 2/7",
            ],
            "after": [
                "The polygon does not merely lose accuracy. It reverses its "
                "behaviour: a quantity that decays to nearly zero is described as "
                "one that grows and changes sign at every step. A smaller error "
                "per step would not have prevented this, because the factor "
                "amplifies whatever error there is.",
                "For a rehearsal, take the second preset. The step `1/4` is "
                "above `1/5` and below `2/5`. Predict the factor, the verdict "
                "and `y₈` before pressing the button, then read the backward "
                "factor as well.",
            ],
        },
        "quiz_title": "Factors, bounds and the backward step",
        "quiz": [
            {"q": "What does forward Euler do on `y′ = −10y` with `h = 1/4`?",
             "a": ["It decays smoothly",
                   "It oscillates and decays",
                   "It oscillates and grows",
                   "It grows without changing sign"],
             "c": 2,
             "why": "The factor is `1 − 10/4 = −3/2`. It is negative, so the values "
                    "alternate in sign, and its size is above `1`, so they grow. The "
                    "bound is `2/10 = 1/5`, and `1/4` is above it. Smooth decay "
                    "needs a factor between `0` and `1`, and growth with one sign "
                    "needs a factor above `1`, which `1 − a·h` cannot be for "
                    "`a > 0`."},
            {"q": "For `y′ = −8y`, which values of `h` make the forward steps go to zero?",
             "a": ["Exactly the `h` with `0 < h < 1/4`",
                   "Exactly the `h` with `0 < h < 1/8`",
                   "Every `h > 0`",
                   "Exactly the `h` with `0 < h < 4`"],
             "c": 0,
             "why": "The bound is `2/a = 2/8 = 1/4`. The values `1/8 < h < 1/4` give a "
                    "negative factor above `−1`, which still decays, so `1/8` is "
                    "where the wobble begins and not where the decay ends. The "
                    "backward method decays for every `h`, but this is the forward "
                    "method. And `4` is `a/2`, the bound turned upside down."},
            {"q": "On `y′ = −5y` with `h = 2`, the forward factor is `−9`. What is the backward factor?",
             "a": ["`−1/9`",
                   "`1/9`",
                   "`11`",
                   "`1/11`"],
             "c": 3,
             "why": "The backward factor is `1/(1 + a·h) = 1/(1 + 10) = 1/11`. It is "
                    "positive and below `1`. The forward factor is `1 − 10 = −9`; "
                    "`−1/9` and `1/9` are the reciprocals of that, which is not what "
                    "the backward step computes. The number `11` is the "
                    "denominator, not the factor."},
            {"q": "A student says that `h = 1/2` is small, so Euler's answer for `y′ = −5y` will be close to the truth. What refutes this?",
             "a": ["The true solution is too large for Euler's method to follow",
                   "The factor is `−3/2`, so every step multiplies the error by a number larger than `1` in size",
                   "The step `1/2` is not a fraction Euler's method accepts",
                   "Euler's method is always wrong by a fixed amount"],
             "c": 1,
             "why": "With factor `−3/2` the values grow in size by `3/2` per step and "
                    "alternate in sign, while the true solution falls. How small "
                    "`1/2` looks next to `1` is irrelevant; it is above `2/5`. "
                    "The true solution is small, not large. Euler accepts any "
                    "positive rational step, and its error is not a fixed amount: "
                    "it depends on the step."},
        ],
        "mistakes": [
            ("Thinking any small step will do",
             "The step `h = 1/2` is small next to `1`, and it makes Euler fail on "
             "`y′ = −5y`: the factor is `−3/2`, and the column grows to "
             "`6561/256` while the true value falls to `≈ 2.06115·10⁻⁹`. What "
             "counts as small is `h < 2/a`, which depends on the equation. Lowering "
             "the error made in a single step does not help when the factor "
             "multiplies the error that is already there."),
            ("Treating the backward method as the accurate one",
             "The backward factor `2/7` decays for `h = 1/2`, but the true factor "
             "for that step is `≈ 0.082085`. After eight steps the backward "
             "column holds `256/5764801`, still far above the true value. "
             "Backward Euler removes the bound; it does not remove the error."),
            ("Taking any sign change as the method failing",
             "With `h = 1/4` the factor is `−1/4`: the values alternate in sign, "
             "and they decay all the same, to `1/65536` after eight steps. The "
             "failure is the factor's size passing `1`, which happens at `2/a`, "
             "not the sign changing, which happens at `1/a`. The wobble is "
             "inaccurate, but it is not unstable."),
        ],
        "standard": (
            "Finish when you can compute Euler's factor for a decay, say what the steps do, and state the largest step that decays.",
            "You should be able to write the forward factor 1 − a·h as an exact "
            "fraction, classify the behaviour from its sign and size, derive the "
            "bound h < 2/a, compute the backward factor 1/(1 + a·h), and say "
            "why a small step size alone does not guarantee a faithful answer."),
        "note": 'That is the end of the first-order equations. Everything so far has been one unknown and its rate; the next course adds a second derivative, and the single exponential factor becomes a pair of them whose exponents are roots of a quadratic equation from Algebra.',
    },
]
