"""Laplace Transforms -- the second half.

Partial fractions with exact coefficients, the transfer function and its poles,
the unit step and switched forcing, and one equation solved by three routes
that have to agree.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py
(mode laplace), by executing its shipped JavaScript under node, and pinned in
`expect`. The transforms, coefficients, poles and solutions are exact; the few
values of an exponential quoted in the prose are rounded and printed behind
the approximation sign.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    {
        "slug": "partial-fractions-exactly",
        "title": "Partial Fractions, Exactly",
        "module": "Solving with it",
        "one_line": "A fraction in s is taken apart into one term for every power of every factor, and each term is a table entry read backwards.",
        "summary": (
            "The answer to a transformed equation is a fraction in `s` that is not in the table, "
            "and partial fractions is how it gets there. Each distinct linear factor gets a "
            "term, a factor repeated `m` times gets `m` terms, and an irreducible quadratic gets "
            "a numerator `B·s + C`. The coefficients are exact fractions found by substituting "
            "roots and comparing powers of `s`, and each term then inverts through the table."),
        "key": [
            "F = A/s + B/(s + 1) + C/(s + 1)²",
            "(s − a)^m: one term for each power 1 to m",
            "quadratic factor: (B·s + C)/quadratic",
            "s² + 2s + 5 = (s + 1)² + 4",
            "1/(s − a)² inverts to t·e^(at)",
        ],
        "key_label": "One term for every power of every factor",
        "concepts_intro": "Three ideas: the shape of the answer is fixed before any arithmetic, repeated factors need every power, and a quadratic needs a two-part numerator.",
        "concepts": [
            ("The shape is fixed by the denominator",
             "Factor the denominator first. Every distinct linear factor `s − a` contributes "
             "`A/(s − a)`. Every irreducible quadratic contributes `(B·s + C)` over that "
             "quadratic. Only then do the coefficients get computed, and the work is finding "
             "numbers for a form already written down."),
            ("A repeated factor contributes every power up to its multiplicity",
             "If `(s + 1)²` divides the denominator, the form has both `B/(s + 1)` and "
             "`C/(s + 1)²`. Leaving out the first power removes a coefficient the numerator "
             "needs, and the equations for the others then have no solution."),
            ("Each term is a table entry",
             "`1/(s − a)` is the transform of `e^(at)`, `1/(s − a)²` of `t·e^(at)`, and a "
             "quadratic written as `(s + 1)² + 4` has the cosine and sine entries shifted by "
             "`e^(−t)`. Finding the coefficients is the arithmetic; inverting is reading the "
             "table from right to left."),
        ],
        "read_title": "Three kinds of factor, and how each one inverts",
        "read_intro": "The form for each kind of factor, the two ways of finding coefficients, and the inverse of each term.",
        "body": [
            ("p", "The previous lesson ended with fractions such as "
                  "`(s + 3)/((s + 1)(s + 2))` and handled them with one trick: multiply by a "
                  "factor and set `s` to its root. That trick covers one case. This lesson "
                  "takes the cases in order of difficulty, starting from the rule that decides "
                  "which terms to write."),
            ("def", ("The partial-fraction form",
                     "Let `F` be a fraction in `s` whose numerator has lower degree than its "
                     "denominator. Each factor `(s − a)^m` of the denominator contributes the "
                     "`m` terms `A₁/(s − a) + A₂/(s − a)² + ⋯ + Aₘ/(s − a)^m`, and each "
                     "irreducible quadratic factor `q` contributes `(B·s + C)/q`.",
                     "Here `A₁, …, Aₘ`, `B` and `C` are the numbers to find. The lab refuses "
                     "a fraction whose numerator is not lower in degree, because the table "
                     "has no entry for a polynomial in `s`.")),
            ("h3", "Distinct linear factors: substitute the root"),
            ("p", "For `(s + 3)/((s + 1)(s + 2))` the form is `A/(s + 1) + B/(s + 2)`. Multiply "
                  "both sides by the whole denominator, so that `s + 3 = A·(s + 2) + B·(s + 1)`. "
                  "This is an identity in `s`, which holds at every value. At `s = −1` the "
                  "term with `B` vanishes and `2 = A`. At `s = −2` the term with `A` vanishes "
                  "and `1 = −B`. The lab prints `2/(s + 1) − 1/(s + 2)`, the same coefficients "
                  "the previous lesson found."),
            ("h3", "A repeated factor: every power is needed"),
            ("p", "For `1/(s·(s + 1)²)` the form has three terms, and the worked example below "
                  "finds them. The reason the middle one cannot be dropped is arithmetic. "
                  "Suppose the form were only `A/s + C/(s + 1)²`. Multiplying out gives "
                  "`1 = A·(s + 1)² + C·s`. The `s²` coefficient on the right is `A`, "
                  "which must be `0` to match the left side; yet at `s = 0` the identity "
                  "gives `A = 1`. The two demands contradict each other, so no such `A` and "
                  "`C` exist. The term `B/(s + 1)` supplies the missing `s²`."),
            ("p", "Substituting roots finds only some coefficients: `s = 0` gives `A` and "
                  "`s = −1` gives `C`, but no value of `s` isolates `B`. The remaining "
                  "coefficient comes from comparing the powers of `s` on both sides of the "
                  "identity, here the `s²` terms, which gives `0 = A + B`."),
            ("h3", "An irreducible quadratic: a two-part numerator"),
            ("p", "For `1/(s·(s² + 2s + 5))` the quadratic has no real roots, since "
                  "`2² − 4·5 = −16` is negative. The form is `A/s + (B·s + C)/(s² + 2s + 5)`. "
                  "At `s = 0` the identity `1 = A·(s² + 2s + 5) + (B·s + C)·s` gives "
                  "`1 = 5A`, so `A = 1/5`. The `s²` terms give `0 = A + B`, so `B = −1/5`, "
                  "and the `s` terms give `0 = 2A + C`, so `C = −2/5`."),
            ("p", "Completing the square, `s² + 2s + 5 = (s + 1)² + 4`, shows how this "
                  "inverts. Write the numerator `s + 2` as `(s + 1) + 1`. The part "
                  "with `s + 1` over `(s + 1)² + 4` is the cosine entry shifted by `e^(−t)`. "
                  "The leftover `1` over `(s + 1)² + 4` is half of the sine entry, since "
                  "that entry has `2` on top. With the factor `−1/5` in front, the inverse is "
                  "`1/5 − (1/5)·e^(−t)·cos(2t) − (1/10)·e^(−t)·sin(2t)`, which is what the lab "
                  "prints, with the fraction written as `(1/5)/s − (s/5 + 2/5)/((s + 1)² + 4)`."),
            ("math", [
                "(s + 2)/((s + 1)² + 4) = (s + 1)/((s + 1)² + 4) + (1/2)·2/((s + 1)² + 4)",
            ]),
            ("p", "The lab does not trust any of this arithmetic. After it finds the "
                  "coefficients and writes the inverse, it transforms the inverse back and "
                  "compares the result with the original fraction exactly. If they differ it "
                  "reports an error and prints no answer; for the three presets they agree. "
                  "A decomposition is unique, so a set of coefficients that reproduces the "
                  "fraction is the set."),
            ("p", "Two limits of the lab, named here because they decide what you can type. "
                  "A quadratic factor whose frequency is irrational, such as `s² + 2`, is "
                  "refused with the factor named, since its inverse would hold `cos(√2·t)`. "
                  "And an irreducible factor of degree three or more is refused. Neither "
                  "makes the method wrong; they bound what the lab prints."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "two-linear",
            "presets": [
                {"id": "two-linear", "label": "(s + 3)/(s² + 3s + 2)", "kind": "partial",
                 "F": "(s + 3)/(s^2 + 3s + 2)", "expect": {"lpPoles": "−2, −1", "lpPartial": "2/(s + 1) − 1/(s + 2)", "lpSolution": "2·e^(−t) − e^(−2t)"}},
                {"id": "repeated", "label": "1/(s(s + 1)²)", "kind": "partial",
                 "F": "1/(s (s + 1)^2)", "expect": {"lpPoles": "−1 (repeated), 0", "lpPartial": "1/s − 1/(s + 1) − 1/(s + 1)²", "lpSolution": "1 − t·e^(−t) − e^(−t)"}},
                {"id": "quadratic", "label": "1/(s(s² + 2s + 5))", "kind": "partial",
                 "F": "1/(s (s^2 + 2s + 5))", "expect": {"lpPoles": "0, −1 ± 2i", "lpPartial": "(1/5)/s − (s/5 + 2/5)/((s + 1)² + 4)", "lpSolution": "1/5 − (1/5)·e^(−t)·cos(2t) − (1/10)·e^(−t)·sin(2t)"}},
            ],
            "panel_title": "Take a fraction apart",
            "panel_intro": (
                "Pick a fraction and read its partial fractions and its inverse. Before you "
                "do, write the form the denominator demands and count the unknowns. Then type "
                "your own fraction, such as 1/(s^2 (s + 2)), and predict the number of "
                "terms."),
        }),
        "steps_title": "Decomposing and inverting",
        "steps_intro": "Factor, write the form, find the numbers, invert each term, transform back. The form comes before any arithmetic.",
        "steps": [
            ("Check the degrees",
             "The numerator must have lower degree than the denominator. If it does not, "
             "divide first; the polynomial part is not a table entry."),
            ("Factor the denominator and write the form",
             "One term for each power of each linear factor, from the first up to its "
             "multiplicity, and a numerator `B·s + C` over each irreducible quadratic."),
            ("Clear the denominators",
             "Multiply through by the whole denominator. The result is an identity between "
             "polynomials in `s`."),
            ("Find the numbers",
             "Substitute each root to isolate one coefficient. Compare powers of `s` for "
             "whatever is left."),
            ("Invert and check",
             "Replace each term by its table entry, completing the square for a quadratic. "
             "Substitute one value of `s` into both sides as a spot check."),
        ],
        "worked": {
            "title": "The repeated factor, taken apart and inverted",
            "intro": [
                "The second preset. The form has three terms because `s` appears once and "
                "`s + 1` twice.",
            ],
            "lines": [
                "1/(s·(s + 1)²) = A/s + B/(s + 1) + C/(s + 1)²",
                "1 = A·(s + 1)² + B·s·(s + 1) + C·s",
                "s = 0:   1 = A,   so A = 1",
                "s = −1:   1 = −C,   so C = −1",
                "s² terms:   0 = A + B,   so B = −1",
                "F = 1/s − 1/(s + 1) − 1/(s + 1)²",
                "f = 1 − e^(−t) − t·e^(−t)",
            ],
            "after": [
                "Spot-check at `s = 1`: the left side is `1/(1·4) = 1/4`, and the right side "
                "is `1 − 1/2 − 1/4 = 1/4`. The lab prints the same three terms and the same "
                "inverse.",
                "The `t·e^(−t)` is what the repeated factor buys. A single factor `s + 1` "
                "would give only `e^(−t)`; the square gives that and the same exponential "
                "multiplied by `t`.",
            ],
        },
        "quiz_title": "Writing the form and inverting",
        "quiz": [
            {"q": "Which is the partial-fraction form of `1/(s·(s + 1)²)`?",
             "a": ["`A/s + B/(s + 1)²`",
                   "`A/s + B/(s + 1) + C/(s + 1)²`",
                   "`A/s + B/(s + 1) + C/(s + 1)³`",
                   "`A/s + B/(s + 1) + C/(s + 2)`"],
             "c": 1,
             "why": "The factor `s` appears once and `s + 1` twice, so the terms are `A/s`, "
                    "`B/(s + 1)` and `C/(s + 1)²`. The first choice drops the first power of "
                    "`s + 1`, and the contradiction above shows no coefficients then exist. "
                    "The third runs past the multiplicity: `(s + 1)³` does not divide the "
                    "denominator, so the powers stop at `2`. The last invents a factor "
                    "`s + 2` that is not in the denominator."},
            {"q": "What is the inverse transform of `1/(s + 1)²`?",
             "a": ["`e^(−t)`",
                   "`e^(−2t)`",
                   "`t²·e^(−t)`",
                   "`t·e^(−t)`"],
             "c": 3,
             "why": "The table entry is `ℒ[t·e^(at)] = 1/(s − a)²`, and `a = −1` here. "
                    "`e^(−t)` has transform `1/(s + 1)` with no square. `e^(−2t)` has its "
                    "pole at `−2`, and `t²·e^(−t)` has `2/(s + 1)³`."},
            {"q": "For `1/(s·(s² + 2s + 5))`, which numerator goes over the quadratic?",
             "a": ["A single constant `B`, since the quadratic is one factor",
                   "`B·s²`",
                   "`B·s + C`",
                   "`B·s + C + D`"],
             "c": 2,
             "why": "A quadratic factor can hold a numerator of degree one, so it needs two "
                    "unknowns, `B` and `C`. A constant alone cannot produce the `s` term that "
                    "the identity needs. `B·s²` has degree two, the same as the "
                    "denominator, which makes the term improper. `C + D` is one unknown "
                    "written twice."},
            {"q": "In `1/(s·(s + 1)²) = A/s + B/(s + 1) + C/(s + 1)²` you have found `A = 1` and `C = −1`. What gives `B`?",
             "a": ["Setting `s = −1` again",
                   "`A + B + C = 1`, the numerator, so `B = 1`",
                   "Comparing the `s²` terms of the cleared identity, `0 = A + B`",
                   "`B = 0`, because it has no root of its own"],
             "c": 2,
             "why": "Clearing denominators gives `1 = A·(s + 1)² + B·s·(s + 1) + C·s`, whose "
                    "`s²` coefficient is `A + B` on the right and `0` on the left, so "
                    "`B = −1`. Setting `s = −1` kills `B` and returns `C`. The coefficients do "
                    "not add to the numerator: at `s = 1` the identity reads "
                    "`1 = 4A + 2B + C`, not `A + B + C`. `B = 0` would leave "
                    "the form without the term that the contradiction showed was needed."},
        ],
        "mistakes": [
            ("A repeated factor needs only the highest power",
             "Writing `1/(s·(s + 1)²) = A/s + C/(s + 1)²` looks complete, because "
             "`(s + 1)²` is the factor. Clearing denominators gives `1 = A·(s + 1)² + C·s`. "
             "Setting `s = 0` gives `A = 1`, which puts a term `s²` on the right that the "
             "left side does not have. Adding `B/(s + 1)` is what makes the `s²` terms "
             "cancel, and with it `B = −1`."),
            ("A bare constant over an irreducible quadratic",
             "Writing `A/s + B/(s² + 2s + 5)` has too few unknowns. Clearing denominators "
             "gives `1 = A·(s² + 2s + 5) + B·s`, whose `s²` coefficient is `A` and must be "
             "`0`, while `s = 0` gives `A = 1/5`. The numerator `B·s + C` supplies the extra "
             "unknown that settles it, with `B = −1/5` and `C = −2/5`."),
            ("Inverting the shifted numerator as a pure cosine",
             "The numerator `s + 2` is not `s + 1`, so the fraction is not just the shifted "
             "cosine entry. Splitting it gives `(s + 1) + 1`: the first part is the cosine "
             "with `e^(−t)`, and the leftover `1` is half the sine entry, whose numerator is "
             "`2`. Dropping the leftover loses the `(1/10)·e^(−t)·sin(2t)` term in the "
             "lab's answer."),
        ],
        "standard": (
            "Finish when you can decompose a fraction with linear, repeated and irreducible quadratic factors into table forms and invert it.",
            "You should be able to write the form from the factored denominator, find "
            "each coefficient as an exact fraction by substituting roots and comparing "
            "powers, complete the square for a quadratic, and invert every term."),
        "note": 'With the decomposition in hand, the next question is what the denominator itself says about the answer before any decomposing is done. See &ldquo;The Transfer Function and Its Poles&rdquo;.',
    },

    # ---------------------------------------------------------------- 06
    {
        "slug": "the-transfer-function-and-its-poles",
        "title": "The Transfer Function and Its Poles",
        "module": "Solving with it",
        "one_line": "From rest, the response is a fixed fraction times the transform of the forcing, and the long run is read from where that fraction's denominator vanishes.",
        "summary": (
            "With zero starting values the transformed equation is `Y = H(s)·ℒ[q]`, where "
            "`H(s) = 1/(a·s² + b·s + c)` depends on the equation and not on the forcing. "
            "The values of `s` where `H` has a zero denominator are its poles, and they are "
            "the characteristic roots. A pole with negative real part contributes a term "
            "that dies out; a pole with positive real part contributes one that grows "
            "without bound. That is the stability criterion."),
        "key": [
            "from rest:   Y = H(s)·ℒ[q]",
            "H(s) = 1/(a·s² + b·s + c)",
            "poles of H = characteristic roots",
            "pole p gives a term built on e^(pt)",
            "stable when every pole has real part < 0",
        ],
        "key_label": "The transfer function and the criterion",
        "concepts_intro": "Three ideas: the equation and the forcing separate in the transform, the poles are roots you already know how to find, and the sign of a real part decides the long run.",
        "concepts": [
            ("The transform separates the system from the forcing",
             "With `y(0) = 0` and `y′(0) = 0` the initial terms vanish and "
             "`(a·s² + b·s + c)·Y = ℒ[q]`. So `Y` is `H(s)` times `ℒ[q]`. The factor `H` is "
             "built from the left side alone, so it describes the system, and the second "
             "factor describes what is done to it."),
            ("The poles are the characteristic roots",
             "A pole is a value of `s` at which a fraction has a zero denominator. The "
             "denominator of `H` is the characteristic polynomial with `s` in place of `r`, "
             "so its zeros are exactly the characteristic roots found earlier in the Subject. "
             "Nothing new is computed; the roots are read from the denominator."),
            ("Real parts decide, imaginary parts oscillate",
             "A real pole `p` contributes a term built on `e^(pt)`, and a complex pair "
             "`α ± βi` contributes terms built on `e^(αt)` times a cosine or a sine of "
             "`βt`. In both cases the term dies out when the real part is negative and "
             "grows when it is positive. The imaginary part only sets the frequency."),
        ],
        "read_title": "Poles and the long run, on three equations",
        "read_intro": "The transfer function, three equations from rest, and the criterion that sorts them.",
        "body": [
            ("p", "Take `a·y″ + b·y′ + c·y = q(t)` with `y(0) = 0` and `y′(0) = 0`. The "
                  "transformed equation of the previous lesson loses its starting terms, "
                  "and what is left is one product."),
            ("math", [
                "(a·s² + b·s + c)·Y = ℒ[q]",
                "Y = H(s)·ℒ[q],   H(s) = 1/(a·s² + b·s + c)",
            ]),
            ("def", ("The transfer function and its poles",
                     "The fraction `H(s) = 1/(a·s² + b·s + c)` is the transfer function of "
                     "the equation. Its poles are the values of `s` at which "
                     "`a·s² + b·s + c = 0`.",
                     "These are the characteristic roots of “The Characteristic Equation” "
                     "in Second-Order Linear Equations, with `s` as the unknown.")),
            ("p", "The first equation is `y″ + 3y′ + 2y = 1` from rest. The transform of the "
                  "forcing `1` is `1/s`, so `Y = 1/(s·(s² + 3s + 2))`, and the denominator "
                  "factors as `s·(s + 1)·(s + 2)`. The transfer function has the poles "
                  "`−2` and `−1`. Substituting roots gives the coefficients, and "
                  "`Y = (1/2)/s − 1/(s + 1) + (1/2)/(s + 2)`."),
            ("p", "Inverting term by term gives `y = 1/2 − e^(−t) + (1/2)·e^(−2t)`. Each "
                  "pole became one term. The poles `−1` and `−2` of `H` became the two "
                  "exponentials that die out, and the pole at `0` came from the forcing, not "
                  "from the equation: it is the constant `1/2` that the solution settles at. "
                  "The poles of `H` decide whether the transient dies; the poles of `ℒ[q]` decide "
                  "what the response settles into."),
            ("thm", ("The stability criterion",
                     "Let `H` be the transfer function of a constant-coefficient equation. "
                     "Every term built on a pole of `H` tends to zero as `t` grows, whatever "
                     "the forcing and the starting values, if and only if every pole of `H` "
                     "has negative real part. One pole with positive real part gives a term "
                     "that grows without bound.")),
            ("proof", ["A real pole `p` contributes a multiple of `e^(pt)`, and a complex "
                       "pair `α ± βi` a multiple of `e^(αt)` times a cosine or a sine. A "
                       "repeated pole adds a factor `t`, as in the previous lesson.",
                       "The exponential `e^(pt)` shrinks to zero when `p < 0` and grows "
                       "without bound when `p > 0`; the same holds for `e^(αt)`, and the "
                       "sine and cosine only stay between `−1` and `1`. So the sign of the "
                       "real part decides."]),
            ("h3", "A complex pair: oscillation with a decay rate"),
            ("p", "For `y″ + 2y′ + 5y = 5` from rest, `H` has the denominator "
                  "`s² + 2s + 5 = (s + 1)² + 4`. The poles are `−1 ± 2i`. The real part "
                  "`−1` is negative, so the transient dies, and the imaginary part `2` is the "
                  "frequency. With the forcing `5/s` the solution is "
                  "`y = 1 − e^(−t)·cos(2t) − (1/2)·e^(−t)·sin(2t)`, which oscillates about "
                  "`1` with an envelope shrinking like `e^(−t)`."),
            ("h3", "A pole on the right"),
            ("p", "For `y″ − y′ − 2y = 2` from rest, the denominator is "
                  "`s² − s − 2 = (s − 2)(s + 1)`, and the poles are `2` and `−1`. The pole "
                  "`2` has positive real part. Its term is `(1/3)·e^(2t)`, and the "
                  "full solution is `y = −1 + (1/3)·e^(2t) + (2/3)·e^(−t)`; the lab prints "
                  "the same three terms with the growing one first. It starts at "
                  "`0`, as it must, and then the exponential takes over. At `t = 5` the "
                  "factor `e^(10)` is `≈ 22026.5`, rounded, and every further unit of "
                  "time multiplies the term by `e²`, which is `≈ 7.38906`, rounded."),
            ("p", "One edge of the criterion is worth stating. A pole exactly on the "
                  "imaginary axis, such as the pair `±2i` of `y″ + 4y = 0`, has real part "
                  "`0`. It gives a term that neither shrinks nor grows, so the criterion "
                  "as stated, with its strict inequality, does not call that equation "
                  "stable."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "stable",
            "presets": [
                {"id": "stable", "label": "y″ + 3y′ + 2y = 1, from rest", "kind": "solve",
                 "equation": "y'' + 3y' + 2y = 1", "ic": [0, 0], "expect": {"lpPoles": "−2, −1", "lpSolution": "1/2 − e^(−t) + (1/2)·e^(−2t)", "lpCheck": "residual 0"}},
                {"id": "oscillatory", "label": "y″ + 2y′ + 5y = 5, from rest", "kind": "solve",
                 "equation": "y'' + 2y' + 5y = 5", "ic": [0, 0], "expect": {"lpPoles": "−1 ± 2i", "lpSolution": "1 − e^(−t)·cos(2t) − (1/2)·e^(−t)·sin(2t)", "lpCheck": "residual 0"}},
                {"id": "unstable", "label": "y″ − y′ − 2y = 2, from rest", "kind": "solve",
                 "equation": "y'' - y' - 2y = 2", "ic": [0, 0], "expect": {"lpPoles": "−1, 2", "lpSolution": "(1/3)·e^(2t) − 1 + (2/3)·e^(−t)", "lpCheck": "residual 0"}},
            ],
            "panel_title": "Read the poles, then the response",
            "panel_intro": (
                "Pick an equation and read the poles in the second tile before the solution. "
                "Predict which terms die out and which grow, then compare with the solution "
                "tile. Then type your own equation, with the starting values left at 0, 0, "
                "and change the sign of the middle coefficient."),
        }),
        "steps_title": "Reading stability from the equation",
        "steps_intro": "No decomposition is needed to classify the long run. The denominator of the transfer function is enough.",
        "steps": [
            ("Write the transfer function",
             "Replace `y″`, `y′` and `y` in the left side by `s²`, `s` and `1` to get "
             "`a·s² + b·s + c`. The transfer function is its reciprocal."),
            ("Find the poles",
             "Solve `a·s² + b·s + c = 0`. Factor it, or use the quadratic formula for a "
             "complex pair."),
            ("Read the real parts",
             "Write down the real part of each pole. Any positive one means growth. If "
             "all are negative, the transient dies."),
            ("Separate the forcing's poles",
             "Transform the forcing. Its poles appear in `Y` but not in `H`, and they give "
             "the steady state the response settles into."),
            ("Confirm with the solution",
             "Decompose, invert, and check that each term has the behaviour its pole "
             "predicted."),
        ],
        "worked": {
            "title": "y″ + 3y′ + 2y = 1 from rest",
            "intro": [
                "The first preset: the poles, then the solution, then the long run.",
            ],
            "lines": [
                "(s² + 3s + 2)·Y = 1/s",
                "Y = 1/(s·(s + 1)·(s + 2))",
                "poles of H:   −1 and −2",
                "A = 1/((1)(2)) = 1/2   (at s = 0)",
                "B = 1/((−1)(1)) = −1   (at s = −1)",
                "C = 1/((−2)(−1)) = 1/2   (at s = −2)",
                "y = 1/2 − e^(−t) + (1/2)·e^(−2t)",
            ],
            "after": [
                "Both poles of `H` are negative, so both exponentials die out and `y` "
                "settles at `1/2`. That is also the value the equation gives when `y″` "
                "and `y′` are zero: `2y = 1`.",
                "Change the middle coefficient to make `s² − s − 2` and the pole `2` "
                "appears, which is the third preset. The only difference in the arithmetic "
                "is one sign; the difference in the long run is bounded against unbounded.",
            ],
        },
        "quiz_title": "Poles and the long run",
        "quiz": [
            {"q": "What are the poles of the transfer function for `y″ + 3y′ + 2y = 1`?",
             "a": ["`0`, `−1` and `−2`",
                   "`−3` and `−2`",
                   "`−1` and `−2`",
                   "`1` and `2`"],
             "c": 2,
             "why": "The transfer function has the denominator `s² + 3s + 2 = (s + 1)(s + 2)`, "
                    "so its poles are `−1` and `−2`. The pole at `0` belongs to the "
                    "forcing `1/s`, and `Y` has it but `H` does not. `1` and `2` are the "
                    "constants in the factors, with the wrong sign. `−3` is a coefficient, "
                    "not a root."},
            {"q": "The poles of an equation are `−3 ± 4i`. What does the response do?",
             "a": ["It oscillates with an envelope that shrinks like `e^(−3t)`",
                   "It oscillates with an envelope that grows like `e^(4t)`",
                   "It grows without oscillating, because of the `i`",
                   "It oscillates with a constant amplitude"],
             "c": 0,
             "why": "The real part `−3` sets the envelope `e^(−3t)`, which shrinks, and the "
                    "imaginary part `4` sets the frequency. The second choice reads the "
                    "imaginary part as a growth rate. The third takes `i` to mean growth; "
                    "it means oscillation. A constant amplitude needs real part `0`."},
            {"q": "For `y″ − y′ − 2y = 2` from rest, the pole `2` gives the term `(1/3)·e^(2t)`. What is true of the response?",
             "a": ["It is larger than for a stable equation but stays bounded",
                   "It grows without bound, since `e^(2t)` does",
                   "It settles at `−1`, the constant term",
                   "It oscillates, since the roots are of opposite sign"],
             "c": 1,
             "why": "The term `(1/3)·e^(2t)` has no upper limit, and nothing in the response "
                    "cancels it, so `y` grows without bound. `−1` is the steady-state "
                    "constant the equation would give, but the response never settles "
                    "there. Opposite-sign real roots give exponentials, not oscillation."},
            {"q": "The equation `y″ + 4y = 0` has the poles `±2i`. What does the criterion say, and what do the solutions do?",
             "a": ["Stable; the solutions die out, since the real part is not positive",
                   "Stable; the solutions stay bounded, which is what the criterion asks",
                   "Not stable; the solutions grow without bound",
                   "Not stable; the solutions neither shrink nor grow, since the real part is `0` and not negative"],
             "c": 3,
             "why": "The criterion asks for negative real part, and `0` is not negative, so "
                    "the equation is not called stable; its solutions are cosines and sines "
                    "of `2t`, which neither shrink nor grow. The first choice has the sign "
                    "test wrong. The second judges by boundedness, which is a different test "
                    "from the criterion. The third is false: nothing in a cosine grows."},
        ],
        "mistakes": [
            ("A pole on the right just makes the response larger",
             "The unstable preset has the term `(1/3)·e^(2t)`. At `t = 5` it is "
             "`≈ 7342.16`, rounded, and every further unit of time multiplies it by `e²`, "
             "which is `≈ 7.38906`, rounded. A positive real part is not a bigger bounded response; the response has "
             "no bound at all. The check is the term itself: an exponential with a "
             "positive exponent has no ceiling."),
            ("Reading stability from the pole of the forcing",
             "In `Y = 1/(s·(s + 1)·(s + 2))` there is a pole at `0`, and it is tempting to "
             "call the equation marginal because of it. That pole comes from the forcing "
             "`1/s`. It sets the constant `1/2` that the response settles to. Stability is "
             "a property of the poles of `H`, here `−1` and `−2`, and both are negative."),
            ("Calling −1 ± 2i unstable because of the i",
             "The imaginary part gives oscillation, not growth. The real part of "
             "`−1 ± 2i` is `−1`, and the response is `1 − e^(−t)·cos(2t) − (1/2)·e^(−t)·sin(2t)`, "
             "whose oscillation is multiplied by `e^(−t)` and shrinks. Only the real "
             "part enters the criterion."),
        ],
        "standard": (
            "Finish when you can write the transfer function of a second-order equation, find its poles and state from their real parts whether the response dies out.",
            "You should be able to say which poles belong to the equation and which to the "
            "forcing, read a complex pair as a decay rate and a frequency, and confirm "
            "the prediction against the lab's solution."),
        "note": 'Every forcing so far has been on from the start. The next lesson switches it on at a chosen time, which the transform handles with one new factor. See &ldquo;The Unit Step and Switched Forcing&rdquo;.',
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "the-unit-step-and-switched-forcing",
        "title": "The Unit Step and Switched Forcing",
        "module": "Switched forcing and a comparison",
        "one_line": "A forcing that switches on at t = c transforms to e^(−cs) times an ordinary fraction, and the solution is that fraction's inverse, shifted to start at c.",
        "summary": (
            "The unit step `u(t − c)` is `0` before `t = c` and `1` from then on. Multiplying "
            "a signal by it switches the signal on at `c`, and the transform of the "
            "switched-on, shifted signal is `e^(−cs)·F(s)`. To solve an equation with a "
            "switched forcing, invert the ordinary fraction as before, then replace "
            "`t` by `t − c` and multiply by the step. The solution is written in pieces, "
            "one for each stretch of time."),
        "key": [
            "u(t − c) = 0 for t < c,  1 for t ≥ c",
            "ℒ[u(t − c)·f(t − c)] = e^(−cs)·F(s)",
            "ℒ[u(t − c)] = e^(−cs)/s",
            "invert F, then shift by c",
            "nothing happens before the switch",
        ],
        "key_label": "The step and the shift rule",
        "concepts_intro": "Three ideas: what a step is, what the shift rule does to a transform, and why an effect cannot come before its cause.",
        "concepts": [
            ("The unit step is a switch",
             "The function `u(t − c)` is `0` for every `t` before `c` and `1` for every `t` "
             "from `c` on. Multiplying a signal by it blanks the signal before `c`. Two "
             "steps with a minus sign between them, `u(t − 1) − u(t − 3)`, give a pulse "
             "that is on from `1` up to `3`."),
            ("The exponential factor carries the shift",
             "If `f` has the transform `F(s)`, the copy of `f` that starts at `c` has the "
             "transform `e^(−cs)·F(s)`. The fraction `F` is exactly what it was, and the "
             "delay sits entirely in the factor `e^(−cs)`. Inverting reverses it: remove "
             "the factor, invert the fraction, shift."),
            ("The response cannot start before the switch",
             "The solution on `t < c` depends only on what the equation and the forcing "
             "were doing on `t < c`. Before the switch the forcing is the old one, so the "
             "solution is the old one. Whatever happens after `c` is invisible there."),
        ],
        "read_title": "From a switch to a two-piece solution",
        "read_intro": "The shift rule, a proof of it, and three equations: a switch-on, a pulse, and a second-order case.",
        "body": [
            ("def", ("The unit step",
                     "For a constant `c ≥ 0`, `u(t − c) = 0` when `t < c` and `u(t − c) = 1` "
                     "when `t ≥ c`.",
                     "The product `u(t − c)·f(t − c)` is the signal `f` shifted to the right "
                     "by `c`: it is `0` up to `t = c`, and from there it repeats `f` as it "
                     "was from `t = 0`.")),
            ("thm", ("The shift rule",
                     "If `ℒ[f] = F(s)`, then for every `c > 0`, "
                     "`ℒ[u(t − c)·f(t − c)] = e^(−cs)·F(s)`.")),
            ("proof", ["The signal is zero before `c`, so the integral starts at `t = c` and "
                       "contains `f(t − c)`. Write `t = c + τ`. Then `e^(−st) = e^(−cs)·e^(−sτ)`, "
                       "and `τ` runs from `0` onward. Renaming the variable this way is a "
                       "shift of the time axis, and all it uses is that sliding a graph along "
                       "the axis does not change the area under it.",
                       "The constant `e^(−cs)` comes outside the integral, and what is left "
                       "is the integral of `e^(−sτ)·f(τ)` from `0` onward, which is `F(s)`. So "
                       "the result is `e^(−cs)·F(s)`."]),
            ("p", "Putting `f = 1` gives the case that matters most for forcing: "
                  "`ℒ[u(t − c)] = e^(−cs)/s`. So the equation `y′ + y = u(t − 2)` transforms to "
                  "`(s + 1)·Y = e^(−2s)/s`, and `Y = e^(−2s)/(s·(s + 1))`. The factor "
                  "`e^(−2s)` is a passenger. Partial fractions are done on "
                  "`1/(s·(s + 1)) = 1/s − 1/(s + 1)`, giving `f = 1 − e^(−t)`, and then the "
                  "shift is applied once, at the end."),
            ("example", ("A pulse",
                         "Take `y′ + y = u(t − 1) − u(t − 3)` from `y(0) = 0`. The forcing is "
                         "on from `t = 1` up to `t = 3`. The transform is "
                         "`Y = (e^(−s) − e^(−3s))/(s·(s + 1))`, which is the same fraction "
                         "`1/s − 1/(s + 1)` times two different delays.",
                         "The solution has three stretches. Before `t = 1` nothing has "
                         "happened and `y = 0`. From `1` to `3` it is the charging curve "
                         "`1 − e^(−(t − 1))`. From `3` on, the second delay subtracts a "
                         "copy that starts at `3`, which leaves "
                         "`e^(−(t − 3)) − e^(−(t − 1))`: the output decays, since the forcing "
                         "is off again. The two pieces meet at `t = 3`, where both are "
                         "`1 − e^(−2)`.")),
            ("h3", "Second order"),
            ("p", "For `y″ + 4y = u(t − 1)` from rest, the transform is "
                  "`(s² + 4)·Y = e^(−s)/s`. The fraction `1/(s·(s² + 4))` decomposes as "
                  "`(1/4)/s − (1/4)·s/(s² + 4)`: `A = 1/4` at `s = 0`, and the `s²` "
                  "terms give `B = −1/4`. Its inverse is `(1/4)·(1 − cos(2t))`, and the "
                  "shift gives the solution `(1/4)·(1 − cos(2(t − 1)))` from `t = 1` on. "
                  "It sits at `0` until the switch and then oscillates between `0` and "
                  "`1/2`, with its first minimum exactly at the switch."),
            ("p", "A limit of the lab, stated where it applies. The shift `c` must be a "
                  "positive rational number. The equation `y″ + y = u(t − π)` is a "
                  "common textbook example, but `π` is not rational and the lab does "
                  "not take it. The method is the same; only the typed input is "
                  "restricted."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "switch-on",
            "presets": [
                {"id": "switch-on", "label": "y′ + y = u(t − 2), y(0) = 0", "kind": "step",
                 "equation": "y' + y = u(t - 2)", "ic": [0], "expect": {"lpY": "e^(−2s)/(s(s + 1))", "lpSolution": "0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2", "lpCheck": "residual 0"}},
                {"id": "pulse", "label": "y′ + y = u(t − 1) − u(t − 3), y(0) = 0", "kind": "step",
                 "equation": "y' + y = u(t - 1) - u(t - 3)", "ic": [0], "expect": {"lpY": "e^(−s)/(s(s + 1)) − e^(−3s)/(s(s + 1))", "lpSolution": "0 for t < 1; 1 − e^(−(t − 1)) for 1 ≤ t < 3; −e^(−(t − 1)) + e^(−(t − 3)) for t ≥ 3", "lpCheck": "residual 0"}},
                {"id": "second-order", "label": "y″ + 4y = u(t − 1), from rest", "kind": "step",
                 "equation": "y'' + 4y = u(t - 1)", "ic": [0, 0], "expect": {"lpY": "e^(−s)/(s(s² + 4))", "lpSolution": "0 for t < 1; 1/4 − (1/4)·cos(2(t − 1)) for t ≥ 1", "lpCheck": "residual 0"}},
            ],
            "panel_title": "Switch a forcing on",
            "panel_intro": (
                "Pick an equation and read Y(s) with its exponential factor, then the "
                "solution in pieces. The plot shows the response in time. Then type your own "
                "switch, such as u(t - 3), and predict the first time the solution is "
                "not zero."),
        }),
        "steps_title": "Solving with a switch",
        "steps_intro": "Transform with the delay in the factor, invert the fraction, shift, and write the pieces.",
        "steps": [
            ("Transform the switched forcing",
             "Replace each `u(t − c)` by `e^(−cs)/s`. Keep the factors `e^(−cs)` as they "
             "are."),
            ("Solve for Y",
             "Divide by the characteristic polynomial. `Y` is a sum of terms "
             "`e^(−cs)·F(s)` with ordinary fractions `F`."),
            ("Invert each fraction",
             "Decompose each `F` and read the table backwards. Do not touch the factor "
             "`e^(−cs)` yet."),
            ("Shift",
             "For each term, replace `t` by `t − c` and multiply by `u(t − c)`."),
            ("Write the pieces and check",
             "List the solution on each stretch of time. It must be `0` where nothing has "
             "yet happened, and each piece must meet the next."),
        ],
        "worked": {
            "title": "y′ + y = u(t − 2) from y(0) = 0",
            "intro": [
                "The first preset: the forcing switches on at `t = 2`.",
            ],
            "lines": [
                "(s + 1)·Y = e^(−2s)/s",
                "Y = e^(−2s)·1/(s·(s + 1))",
                "1/(s·(s + 1)) = 1/s − 1/(s + 1)",
                "f = 1 − e^(−t)",
                "y = u(t − 2)·(1 − e^(−(t − 2)))",
                "t < 2:   y = 0",
                "t ≥ 2:   y = 1 − e^(−(t − 2))",
            ],
            "after": [
                "Nothing happens until `t = 2`, and then the charging curve starts from `0` "
                "as if time began at the switch. The pieces meet: at `t = 2` the second "
                "piece is `1 − e⁰ = 0`. The lab prints the same two pieces.",
                "Compare with the pulse preset on the stretch from `1` to `3`: there the "
                "solution is `1 − e^(−(t − 1))`, the same curve with the switch at `1`. The "
                "switch-off at `3` has no effect before `t = 3`.",
            ],
        },
        "quiz_title": "Steps and shifts",
        "quiz": [
            {"q": "What is `ℒ[u(t − 2)]`?",
             "a": ["`1/(s − 2)`",
                   "`e^(−2s)/s`",
                   "`e^(2s)/s`",
                   "`2/s`"],
             "c": 1,
             "why": "The shift rule with `f = 1` and `c = 2` gives `e^(−2s)·(1/s)`. "
                    "`1/(s − 2)` is the transform of `e^(2t)`, which grows. The delay "
                    "carries a negative exponent, so `e^(2s)/s` has the wrong sign. `2/s` is "
                    "the transform of the constant `2`."},
            {"q": "For `Y = e^(−3s)/(s + 1)`, what is `y(t)`?",
             "a": ["`e^(−t)` for all `t`",
                   "`e^(−t)` for `t ≥ 3`, and `0` before",
                   "`e^(−(t + 3))` for `t ≥ 0`",
                   "`e^(−(t − 3))` for `t ≥ 3`, and `0` before"],
             "c": 3,
             "why": "The fraction `1/(s + 1)` inverts to `e^(−t)`, and the factor `e^(−3s)` "
                    "shifts it: replace `t` by `t − 3` and switch on at `3`. The first "
                    "choice ignores the factor. The second switches on at `3` but forgets to "
                    "shift, so the curve would jump to `e^(−3)` instead of starting at `1`. "
                    "The third shifts in the wrong direction."},
            {"q": "In `y′ + y = u(t − 1) − u(t − 3)` from `y(0) = 0`, what is `y` at `t = 1/2`?",
             "a": ["`1 − e^(−1/2)`, since the forcing is about to begin",
                   "`1 − e^(−2)`, the value at `t = 3`",
                   "`0`, since the forcing is not on yet",
                   "It cannot be found without solving past `t = 3`"],
             "c": 2,
             "why": "Before `t = 1` the forcing is `0` and the starting value is `0`, so "
                    "`y` stays `0`. A response does not anticipate a switch. The "
                    "second and fourth choices let the later switch-off reach back in time. "
                    "The first lets the switch-on do so."},
            {"q": "For `y″ + 4y = u(t − 1)` from rest, which describes the solution?",
             "a": ["`(1/4)(1 − cos(2t))` for all `t ≥ 0`",
                   "`(1/4)(1 − cos(2(t − 1)))` for `t ≥ 1`, and `0` before",
                   "`(1/4)(1 − cos(2t))` for `t ≥ 1`, and `0` before",
                   "`cos(2(t − 1))` for `t ≥ 1`, and `0` before"],
             "c": 1,
             "why": "The unshifted response is `(1/4)(1 − cos(2t))`, and the switch "
                    "replaces `t` by `t − 1` and delays the start to `1`. The first choice "
                    "has the response from the start, ignoring the switch. The third switches "
                    "on at `1` but leaves `t` unshifted, so it would start at "
                    "`(1/4)(1 − cos(2))`, not `0`. The last drops the constant `1/4`."},
        ],
        "mistakes": [
            ("The solution before t = c is affected by what happens after",
             "Reading the pulse as one forcing that is on for a while, a reader expects "
             "`y` to start moving before `t = 1`, or to depend on the switch-off at `3`. "
             "It does not. On `t < 1` the equation is `y′ + y = 0` with `y(0) = 0`, so "
             "`y = 0`. On `1 ≤ t < 3` the solution is the same `1 − e^(−(t − 1))` whether the "
             "pulse ends at `3` or at `30`."),
            ("Shifting the step but not the signal",
             "Writing the answer to the first preset as `u(t − 2)·(1 − e^(−t))` keeps the "
             "switch and drops the shift. At `t = 2` that is `1 − e^(−2)`, "
             "`≈ 0.864665`, rounded, so the answer jumps from `0` to nearly `1` at the "
             "switch. The correct piece starts at `1 − e⁰ = 0`. The factor "
             "`u(t − c)` and the replacement of `t` by `t − c` go together."),
            ("Leaving out the step",
             "The expression `1 − e^(−(t − 2))` by itself is a perfectly good function, but "
             "at `t = 0` it is `1 − e²`, `≈ −6.38906`, rounded, which is not the "
             "starting value `0`. Without the factor `u(t − 2)` the formula describes "
             "a solution that was on all along."),
        ],
        "standard": (
            "Finish when you can solve a first- or second-order equation whose forcing switches on at a rational time and write the solution in pieces.",
            "You should be able to transform a unit step, factor the delay out of Y, "
            "invert the remaining fraction, apply the shift, and check that the "
            "pieces start from zero and meet at the switch."),
        "note": 'One more comparison remains, which is the point of the whole course: the transform is not a rival to the earlier methods. See &ldquo;Three Methods, One Equation&rdquo;.',
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "three-methods-one-equation",
        "title": "Three Methods, One Equation",
        "module": "Switched forcing and a comparison",
        "one_line": "Undetermined coefficients, the Laplace transform and, for a first-order equation, the integrating factor all return the same function, and substitution is the referee.",
        "summary": (
            "One forced initial value problem solved two ways, and a first-order one "
            "solved a third. Undetermined coefficients guesses a particular solution, adds "
            "the homogeneous one and fits two constants. The Laplace transform puts the "
            "starting values in at the first line and ends with a table read backwards. The "
            "two give the same function, and the reason is that an initial value problem "
            "has one solution. Each method has a kind of problem it is best at."),
        "key": [
            "y_p + y_h, then fit two constants",
            "transform, solve for Y, invert",
            "the answers agree: the solution is unique",
            "residual 0 settles any doubt",
            "switched forcing favours the transform",
        ],
        "key_label": "Two routes and one referee",
        "concepts_intro": "Three ideas: each method's route, why the answers must agree, and how to choose.",
        "concepts": [
            ("Undetermined coefficients goes through a general solution",
             "Guess a particular solution `y_p` with the shape of the forcing, add the "
             "homogeneous solution `y_h` with two unknown constants, and fit the constants "
             "to the starting values with a 2×2 system. The constants are found last."),
            ("The transform puts the starting values in first",
             "Transform both sides, with `y(0)` and `y′(0)` inside the derivative rules, and "
             "solve for `Y`. Partial fractions and the table finish the job. No "
             "general solution is written and no system for constants is solved."),
            ("They must agree, and substitution shows it",
             "Two solutions of the same initial value problem differ by a solution of the "
             "homogeneous equation that starts at zero, and that is zero. So the routes "
             "return the same function. The lab's `residual 0` is the test on any single "
             "answer, starting values included."),
        ],
        "read_title": "One equation, solved twice and then a third time",
        "read_intro": "The constant-force equation by both second-order routes, a proof that they agree, the first-order case by a third route, and when to choose which.",
        "body": [
            ("p", "Take `y″ + 3y′ + 2y = 4` with `y(0) = 0` and `y′(0) = 0`. The forcing "
                  "is constant, so the first route guesses a constant. If `y_p = K`, then "
                  "`y_p′ = 0` and `y_p″ = 0`, and the equation reads `2K = 4`, so "
                  "`y_p = 2`. The homogeneous equation has the characteristic roots "
                  "`−1` and `−2`, so `y_h = C₁·e^(−t) + C₂·e^(−2t)`. The general solution is "
                  "`y = 2 + C₁·e^(−t) + C₂·e^(−2t)`."),
            ("p", "Fitting the constants takes two equations. From `y(0) = 0`: "
                  "`2 + C₁ + C₂ = 0`, so `C₁ + C₂ = −2`. From `y′(0) = 0`, with "
                  "`y′ = −C₁·e^(−t) − 2C₂·e^(−2t)`: `−C₁ − 2C₂ = 0`. Adding the two equations "
                  "gives `−C₂ = −2`, so `C₂ = 2` and `C₁ = −4`."),
            ("p", "The second route starts at the same equation. Transforming gives "
                  "`(s² + 3s + 2)·Y = 4/s`, so `Y = 4/(s·(s + 1)·(s + 2))`. The roots give "
                  "the coefficients: `4/(1·2) = 2` at `s = 0`, `4/((−1)·1) = −4` at `s = −1`, "
                  "and `4/((−2)·(−1)) = 2` at `s = −2`. So "
                  "`Y = 2/s − 4/(s + 1) + 2/(s + 2)`, and the table backwards gives "
                  "`y = 2 − 4·e^(−t) + 2·e^(−2t)`."),
            ("math", [
                "undetermined coefficients:   y = 2 − 4e^(−t) + 2e^(−2t)",
                "Laplace transform:   y = 2 − 4e^(−t) + 2e^(−2t)",
            ]),
            ("p", "The same function from two directions. The lab prints this solution and "
                  "its residual in the original equation and starting values, `residual 0`, "
                  "so the check does not rest on reading two lines and judging them alike."),
            ("thm", ("The routes agree",
                     "If `y₁` and `y₂` both satisfy `y″ + 3y′ + 2y = 4` with `y(0) = 0` and "
                     "`y′(0) = 0`, then `y₁ = y₂`.")),
            ("proof", ["Let `d = y₁ − y₂`. Because the equation is linear, the `4` cancels and "
                       "`d` satisfies the homogeneous equation, with `d(0) = 0` and "
                       "`d′(0) = 0`.",
                       "So `d = C₁·e^(−t) + C₂·e^(−2t)`, and the starting values give "
                       "`C₁ + C₂ = 0` and `−C₁ − 2C₂ = 0`. Adding them gives `−C₂ = 0`, so "
                       "`C₂ = 0` and `C₁ = 0`. The other kinds of root end the same way, "
                       "because the 2×2 system for the constants has a nonzero "
                       "determinant, the Wronskian at `0` of “Superposition and the "
                       "Wronskian” in Second-Order Linear Equations."]),
            ("h3", "A third route for a first-order equation"),
            ("p", "The equation `y′ + 2y = e^t` with `y(0) = 0` has a third route, "
                  "the integrating factor. With `μ = e^(2t)` the left side times `μ` is "
                  "`(e^(2t)·y)′`, and the right side is `e^(3t)`. So "
                  "`e^(2t)·y = e^(3t)/3 + C`, and `y(0) = 0` gives `C = −1/3`. The result is "
                  "`y = e^t/3 − e^(−2t)/3`."),
            ("p", "The transform gives `(s + 2)·Y = 1/(s − 1)`, so `Y = 1/((s − 1)(s + 2))`. "
                  "At `s = 1` the coefficient is `1/3`, and at `s = −2` it is `−1/3`. "
                  "Undetermined coefficients guesses `A·e^t`: `A + 2A = 1`, so "
                  "`A = 1/3`, and the starting value gives the constant `−1/3`. All three "
                  "return `e^t/3 − e^(−2t)/3`."),
            ("p", "For the cosine-force preset, `y″ + 4y = 3cos(t)` from rest, undetermined "
                  "coefficients guesses `A·cos(t)`: `−A + 4A = 3`, so `A = 1`, and the "
                  "starting values give `C₁ = −1` and `C₂ = 0`. The transform gives "
                  "`Y = 3s/((s² + 1)(s² + 4)) = s/(s² + 1) − s/(s² + 4)`. Both give "
                  "`y = cos(t) − cos(2t)`."),
            ("h3", "When to choose which"),
            ("ul", [
                "Undetermined coefficients is shortest when the forcing is one of the "
                "shapes it guesses, and when what you want is the long-run response, the "
                "particular solution itself.",
                "The transform is shortest when the forcing switches on or off, since the "
                "step is one factor, and when the starting values are not zero, since "
                "they go in at the first line.",
                "The integrating factor needs a first-order equation, and then works for "
                "any forcing that can be integrated against `μ`.",
                "Substitution is not a method but a referee. Whichever route is used, put "
                "the answer in the equation and its starting values.",
            ]),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "constant-force",
            "presets": [
                {"id": "constant-force", "label": "y″ + 3y′ + 2y = 4, from rest", "kind": "solve",
                 "equation": "y'' + 3y' + 2y = 4", "ic": [0, 0], "expect": {"lpPartial": "2/s − 4/(s + 1) + 2/(s + 2)", "lpSolution": "2 − 4·e^(−t) + 2·e^(−2t)", "lpCheck": "residual 0"}},
                {"id": "cosine-force", "label": "y″ + 4y = 3cos(t), from rest", "kind": "solve",
                 "equation": "y'' + 4y = 3cos(t)", "ic": [0, 0], "expect": {"lpPartial": "s/(s² + 1) − s/(s² + 4)", "lpSolution": "cos(t) − cos(2t)", "lpCheck": "residual 0"}},
                {"id": "exp-force", "label": "y′ + 2y = e^t, y(0) = 0", "kind": "solve",
                 "equation": "y' + 2y = e^t", "ic": [0], "expect": {"lpPartial": "(1/3)/(s − 1) − (1/3)/(s + 2)", "lpSolution": "(1/3)·e^t − (1/3)·e^(−2t)", "lpCheck": "residual 0"}},
            ],
            "panel_title": "Check a solution against the equation",
            "panel_intro": (
                "Pick an equation, solve it by the other route on paper, and compare with the "
                "solution tile. The last tile substitutes the lab's answer back into the "
                "equation and its starting values. Then change the forcing or a starting "
                "value and see which parts of the answer move."),
        }),
        "steps_title": "Solving one equation twice",
        "steps_intro": "Do both routes, compare, and let substitution decide any disagreement.",
        "steps": [
            ("Solve by undetermined coefficients",
             "Guess `y_p` with the forcing's shape, solve for its coefficient, add `y_h` "
             "with two constants."),
            ("Fit the constants",
             "Put `y(0)` and `y′(0)` into the general solution and its derivative, and solve "
             "the 2×2 system."),
            ("Solve by transform",
             "Transform both sides with the starting values inside, solve for `Y`, "
             "decompose and invert."),
            ("Compare",
             "Match the two functions term by term. A mismatch is an arithmetic slip "
             "in one route."),
            ("Substitute",
             "Put the suspect answer into the equation and the starting values. The "
             "residual must be zero."),
        ],
        "worked": {
            "title": "y″ + 3y′ + 2y = 4 from rest, two ways",
            "intro": [
                "The first preset: the constants fitted on one side and the fractions on "
                "the other.",
            ],
            "lines": [
                "y_p = 2   (2K = 4)",
                "y = 2 + C₁·e^(−t) + C₂·e^(−2t)",
                "C₁ + C₂ = −2,   −C₁ − 2C₂ = 0",
                "C₂ = 2,   C₁ = −4",
                "Y = 4/(s·(s + 1)·(s + 2))",
                "= 2/s − 4/(s + 1) + 2/(s + 2)",
                "y = 2 − 4e^(−t) + 2e^(−2t)",
            ],
            "after": [
                "Both lines end at the same function. Check the starting values once: "
                "`y(0) = 2 − 4 + 2 = 0` and `y′(0) = 4 − 4 = 0`. The lab reports "
                "`residual 0` for the equation.",
                "The two routes differ in where the work falls. The first found the "
                "constants last, from a 2×2 system. The second found them as the "
                "coefficients of the fractions, and the starting values never needed a "
                "separate step.",
            ],
        },
        "quiz_title": "Comparing the routes",
        "quiz": [
            {"q": "The undetermined-coefficients route and the transform route give different functions for the same initial value problem. What follows?",
             "a": ["Both are valid, since the problem has two solutions",
                   "The methods are different theories and disagree here",
                   "One of the routes has an arithmetic error, since the solution is unique",
                   "The forcing is outside both methods"],
             "c": 2,
             "why": "Two solutions of the same initial value problem differ by a solution of "
                    "the homogeneous equation that starts at zero, and that is zero. So a "
                    "mismatch is a slip in one route. The first two deny uniqueness, and "
                    "the last has no basis when both routes handled the same forcing."},
            {"q": "For `y″ + 3y′ + 2y = 4`, the particular solution is `y_p = 2`. Why?",
             "a": ["It is the value at `t = 0`",
                   "It is the average of the roots",
                   "A constant solves `2K = 4` once its derivatives vanish",
                   "It makes `y(0) = 0`"],
             "c": 2,
             "why": "For a constant `K` the derivatives are `0`, so the equation reduces to "
                    "`2K = 4`. The starting value `y(0) = 0` is met only after the "
                    "homogeneous part is added, so `y_p` alone does not do it. The roots "
                    "are `−1` and `−2`, and nothing here averages them."},
            {"q": "Which problem favours the transform most clearly?",
             "a": ["`y′ + 2y = 6` with `y(0) = 0`, where the guess is a constant",
                   "An equation whose forcing switches off at `t = 4`",
                   "`y′ + 2y = 0` with `y(0) = 3`",
                   "An equation with the variable coefficient `t·y`"],
             "c": 1,
             "why": "A switch is one factor `e^(−4s)` in the transform, while the other route "
                    "must fit the solution across the switch by matching pieces. The first "
                    "problem is as short by guessing a constant, and the third is "
                    "`y = 3e^(−2t)` at sight. The last has a variable coefficient, which is "
                    "outside the transform of this course."},
            {"q": "For `y′ + 2y = e^t` with `y(0) = 0`, what is the solution?",
             "a": ["`e^t/3 + e^(−2t)/3`",
                   "`e^t − e^(−2t)`",
                   "`e^t/2 − e^(−2t)/2`",
                   "`e^t/3 − e^(−2t)/3`"],
             "c": 3,
             "why": "Undetermined coefficients gives `A = 1/3` and the constant `−1/3` from "
                    "`y(0) = 0`. The first choice has `y(0) = 2/3`. The second starts at `0` "
                    "but gives `y′ + 2y = 3e^t`, three times too much. The third also "
                    "starts at `0` and gives `y′ + 2y = (3/2)·e^t`."},
        ],
        "mistakes": [
            ("The three methods are three theories that may disagree",
             "A reader who gets `2 − 4e^(−t) + 2e^(−2t)` from one route and "
             "`2 − 2e^(−t) + 2e^(−2t)` from the other may conclude that the methods "
             "give different answers. The second has `y(0) = 2` and not `0`, so it is "
             "wrong on its face. The routes are one theory run in different orders, "
             "and the uniqueness result says they cannot disagree."),
            ("Applying the starting values to y_p alone",
             "Requiring the particular solution itself to start at `0` is wrong, since `y_p = 2` starts at `2`. The conditions "
             "belong to the whole of `y_p + y_h`, which is why the constants `C₁` and "
             "`C₂` are fitted after the two are added. Fitting them to `y_h` alone gives "
             "`C₁ = C₂ = 0` and the answer `y = 2`, which starts at `2`."),
            ("Transforming the forcing as if it were a number",
             "In `(s² + 3s + 2)·Y = 4/s` the right side is `4/s`, not `4`. Using `4` "
             "gives `Y = 4/((s + 1)(s + 2))` and the solution `4e^(−t) − 4e^(−2t)`, which "
             "starts at `0` but has `y′(0) = −4 + 8 = 4`, not `0`. A constant forcing "
             "has the transform `c/s`, and the pole at `0` is the particular solution."),
        ],
        "standard": (
            "Finish when you can solve one forced initial value problem by undetermined coefficients and by the transform, check that the answers agree, and say which method suits a given problem.",
            "You should be able to fit the constants from a 2×2 system, decompose "
            "the transform of the answer, compare the two results term by term, and "
            "verify the answer by substitution."),
        "note": 'That closes the transform: the table, the derivative rule, the poles and the switch. The same problems are solved elsewhere by other means, and the answer is the same function.',
    },
]
