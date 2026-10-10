"""Separable Equations, Growth and Decay -- the first half.

The method (separate, integrate, fix the constant), the reason it is legitimate
(the chain rule read backwards), what an implicit answer means and where it
holds, and then the simplest separable equation of all, y' = k*y, with Euler's
exact steps beside e^(kt) and the doubling time that falls out of it.

Every figure below that a tile prints was read off the built page with
scripts/labcheck.js --observe and pinned in `expect`; the arithmetic in the
prose that is not a tile (a power such as (9/8)^5) was computed with
fractions.Fraction. Where this file and PLAN.md section C disagree the lab won,
and the disagreement is reported with the lesson, not copied.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "separable-equations",
        "title": "Separable Equations",
        "module": "Separating variables",
        "one_line": "Gather every y with y′ on one side and every t on the other, integrate each side, and let the initial value fix the one constant.",
        "summary": (
            "Some first-order equations can be written so that the left side is a function of "
            "`y` times `y′` and the right side is a function of `t` alone. For those, each side "
            "has an antiderivative of its own, the two are set equal with a single constant, and "
            "an initial value fixes that constant exactly. The lab does the integration in exact "
            "fractions and prints the implicit relation between `y` and `t`. The one thing to "
            "watch is what &ldquo;separate&rdquo; means: `y′` stays with the `y`, not with the "
            "`t`."
        ),
        "key": [
            "g(y)·y′ = h(t)   the separable form",
            "G′ = g, H′ = h  ⟹  G(y) = H(t) + C",
            "C = G(y₀) − H(t₀)   from y(t₀) = y₀",
            "y·y′ = t, y(0) = 2  ⟹  y² = t² + 4",
        ],
        "key_label": "The method in four lines",
        "concepts_intro": (
            "Three ideas, in the order you use them. The first is a test, the second is the "
            "integration, and the third is the only place an initial value enters."
        ),
        "concepts": [
            ("A function of y times y′ equals a function of t, and y′ stays with the y",
             "An equation is <strong>separable</strong> when it can be written with a function "
             "of `y` multiplying `y′` on one side and a function of `t` alone on the other. "
             "`y′ = t/y` becomes `y·y′ = t` by multiplying through by `y`. Nothing is moved "
             "across the equals sign and left behind: the factor `y′` travels with the `y` it "
             "multiplies, and that is what the next lesson shows to be the whole point."),
            ("Each side has an antiderivative, and there is one constant",
             "Call an antiderivative of `g` by the name `G` and one of `h` by `H`. The relation "
             "`G(y) = H(t) + C` holds along a solution. Each side could carry its own "
             "constant, but their difference is a single number, so one `C` is enough, and "
             "writing it on the right is only a habit."),
            ("The initial value fixes C, and exactly",
             "If the solution passes through `(t₀, y₀)` then `C = G(y₀) − H(t₀)`. With the "
             "antiderivatives in exact fractions, `C` is an exact fraction too, and the lab "
             "prints it. Before the constant is fixed the answer is a whole family of curves; "
             "after, it is one."),
        ],
        "read_title": "From an equation to a relation between y and t",
        "read_intro": "The definition, the four moves, two more equations through the same moves, and one equation the moves cannot reach.",
        "body": [
            ("def", ("A separable equation",
                     "A first-order equation that can be written `g(y)·y′ = h(t)`, where `g` is "
                     "a function of `y` only and `h` is a function of `t` only.",
                     "An <strong>antiderivative</strong> of `g` is a function `G` with "
                     "`G′ = g`, as in Accumulation and the Integral. The lab accepts a `g` that "
                     "is a polynomial in `y`, or exactly `1/y` or `1/y^2`, and an `h` that is a "
                     "polynomial in `t`.")),
            ("p", "Take `y′ = t/y`. Multiply both sides by `y` and the equation reads "
                  "`y·y′ = t`: the left side is `g(y) = y` times `y′`, and the right side is "
                  "`h(t) = t`. The antiderivatives are `G(y) = y²/2` and `H(t) = t²/2`, so "
                  "along any solution `y²/2 = t²/2 + C`. That is a relation between `y` and "
                  "`t`, not yet a formula for `y`, and &ldquo;Implicit and Explicit Solutions&rdquo; is about what "
                  "to do with it."),
            ("math", [
                "y·y′ = t",
                "",
                "  G(y) = y²/2           H(t) = t²/2",
                "",
                "  y²/2 = t²/2 + C",
                "",
                "  y(0) = 2:   2²/2 = 0²/2 + C",
                "              C = 2",
                "",
                "  y²/2 = t²/2 + 2",
                "  y² = t² + 4",
            ]),
            ("h3", "The four moves"),
            ("ol", [
                "Write the equation as `g(y)·y′ = h(t)`. If you cannot, stop; this method does "
                "not apply.",
                "Find `G` with `G′ = g` and `H` with `H′ = h`.",
                "Write `G(y) = H(t) + C`.",
                "Put in the initial value and solve for `C`.",
            ]),
            ("p", "The lab does moves two to four. Its first tile shows `G(y)`, its second "
                  "`H(t)`, its third the constant, and the fourth the relation with the "
                  "constant in it, scaled so that the leading coefficient on the `y` side is "
                  "1. Its first preset is the equation above, and the tiles print "
                  "`y²/2`, `t²/2`, `2` and `y² = t² + 4`."),
            ("example", ("A reciprocal on the left",
                         "`y′ = t·y²` separates as `(1/y²)·y′ = t`, so `g(y) = 1/y²`, "
                         "`G(y) = −1/y` (the rate of `−1/y` is `1/y²`, from &ldquo;The "
                         "Derivative of 1/t&rdquo;) and `H(t) = t²/2`. With `y(0) = 1` the constant is "
                         "`C = −1/1 − 0 = −1`, and the relation is `−1/y = t²/2 − 1`; the lab also prints the explicit form "
                         "`y = 2/(2 − t²)`.",
                         "The division by `y²` is only allowed where `y ≠ 0`. The constant "
                         "function `y = 0` also satisfies `y′ = t·y²`, and the separated form "
                         "cannot produce it. An initial value of 1 never goes near it, so "
                         "nothing is lost here, but the method has no way to hand back a "
                         "solution it divided away.")),
            ("example", ("A polynomial in y on the left",
                         "`3y²·y′ = 2t + 1` has `G(y) = y³` and `H(t) = t² + t`. With "
                         "`y(0) = 1` the constant is `C = 1³ − 0 = 1`, so `y³ = t² + t + 1`.",
                         "Here the relation can be solved for `y` as a cube root, which is a "
                         "formula. The lab marks it as implicit anyway, and &ldquo;Implicit and Explicit Solutions&rdquo; says "
                         "when an explicit form exists.")),
            ("h3", "What the method cannot do"),
            ("p", "`y′ = t + y` has no separated form. The right side is a sum, and a sum of a "
                  "function of `t` and a function of `y` cannot be written as `h(t)` over "
                  "`g(y)` for any such pair. Nothing in the lab will rescue it, and a later "
                  "course solves it by another method. `y′ = t² + y²` fails for the same "
                  "reason."),
        ],
        "lab": ("dekit", {
            "mode": "separable",
            "view": "solve",
            "preset": "circle",
            "presets": [
                {"id": "circle", "label": "y·y′ = t, y(0) = 2",
                 "g": "y", "h": "t", "ic": [0, 2],
                 "expect": {"spG": "y²/2", "spC": "2", "spImplicit": "y² = t² + 4"}},
                {"id": "recip", "label": "(1/y²)·y′ = t, y(0) = 1",
                 "g": "1/y^2", "h": "t", "ic": [0, 1],
                 "expect": {"spG": "−1/y", "spC": "−1", "spImplicit": "−1/y = t²/2 − 1"}},
                {"id": "poly", "label": "3y²·y′ = 2t + 1, y(0) = 1",
                 "g": "3y^2", "h": "2t + 1", "ic": [0, 1],
                 "expect": {"spG": "y³", "spC": "1", "spImplicit": "y³ = t² + t + 1"}},
            ],
            "panel_title": "Integrate both sides, then fix the constant",
            "panel_intro": (
                "Type g(y) and h(t) and an initial value, or pick a preset. The tiles show the "
                "two antiderivatives, the constant taken from the initial value, and the "
                "relation between y and t. Change the initial value on the first preset to "
                "y(0) = 3 and the constant becomes 9/2."
            ),
        }),
        "steps_title": "Solving one separable equation",
        "steps_intro": "Four moves. The first is the one that decides whether the rest apply.",
        "steps": [
            ("Multiply or divide until every y is with y′",
             "Get the equation to `g(y)·y′ = h(t)`. Write down any value of `y` you divided by "
             "zero at, because a constant solution there is not recovered by the later steps."),
            ("Integrate each side by itself",
             "`G` from `g` with respect to `y`, `H` from `h` with respect to `t`. Differentiate "
             "each answer once in your head; a lost sign here survives to the end."),
            ("Write one relation with one constant",
             "`G(y) = H(t) + C`. Put the constant on the `t` side, and do not add a second one "
             "to the `y` side."),
            ("Fix C from the initial value",
             "`C = G(y₀) − H(t₀)`, in that order. Substitute the point back into the relation "
             "to confirm it holds."),
        ],
        "worked": {
            "title": "y·y′ = t with y(0) = 2, start to finish",
            "intro": [
                "The equation is already separated, with `g(y) = y` and `h(t) = t`. Every figure "
                "below is exact, and the lab's first preset prints the same four results."
            ],
            "lines": [
                "G(y) = y²/2            H(t) = t²/2",
                "",
                "y²/2 = t²/2 + C",
                "",
                "t = 0, y = 2:   4/2 = 0 + C    so C = 2",
                "",
                "y²/2 = t²/2 + 2",
                "y² = t² + 4",
                "",
                "check the point:  2² = 0² + 4   yes",
            ],
            "after": [
                "The relation is what the method delivers. It is not yet a function: for each "
                "`t` it allows two values of `y`, one positive and one negative, and the "
                "initial value `y(0) = 2` is what will pick between them. That choice, and "
                "where it can be made, is the work of &ldquo;Implicit and Explicit Solutions&rdquo;.",
                "Before that, there is a question the method has so far dodged: why is it "
                "allowed to integrate `y·y′` as though it were an ordinary function of one "
                "variable? The next lesson answers it, and the answer is the chain rule.",
            ],
        },
        "quiz_title": "Separable or not, and what the constant is",
        "quiz": [
            {"q": "Which of these equations can be written in the form `g(y)·y′ = h(t)`?",
             "a": ["`y′ = t + y`", "`y′ = t² + y²`", "`y′ = t·y²`", "`y′ = t − y`"],
             "c": 2,
             "why": "`y′ = t·y²` becomes `(1/y²)·y′ = t` wherever `y ≠ 0`. The other three have a "
                    "sum of a function of `t` and a function of `y` on the right, and a sum of "
                    "two such functions is not a product of one function of `t` and one of `y`, "
                    "so no rearrangement separates them."},
            {"q": "For `y·y′ = t` with `y(0) = 2`, the relation is `y²/2 = t²/2 + C`. What is `C`?",
             "a": ["0", "2", "4", "1/2"],
             "c": 1,
             "why": "`C = G(y₀) − H(t₀) = 2²/2 − 0²/2 = 2`. The value 4 is the constant in the "
                    "scaled relation `y² = t² + 4`, which is a different equation; 0 would "
                    "come from forgetting the `y` side, and 1/2 from nothing."},
            {"q": "For `(1/y²)·y′ = t` with `y(0) = 1`, what does the constant come to?",
             "a": ["−1", "1", "0", "1/2"],
             "c": 0,
             "why": "`G(y) = −1/y` and `H(t) = t²/2`, so `C = G(1) − H(0) = −1 − 0 = −1`. "
                    "Taking `G(1) = 1` drops the sign of the antiderivative of `1/y²`, which is "
                    "the usual slip."},
            {"q": "Someone solves `y′ = t/y` by writing `y = t²/(2y) + C`, integrating `t/y` as if `y` were a constant. What is wrong?",
             "a": ["`y` changes with `t`, so `t/y` is not a function of `t` alone and cannot be integrated that way",
                   "`t/y` has no antiderivative",
                   "Nothing: the answer is right once `C` is found",
                   "They should have integrated with respect to `y` on both sides"],
             "c": 0,
             "why": "While `t` varies, `y` varies with it, so `t/y` cannot be integrated with "
                    "`y` held fixed. The separated form `y·y′ = t` removes the problem by putting "
                    "every `y` on one side. Integrating both sides with respect to `y` mixes up "
                    "which variable depends on which, and the answer is not right: "
                    "differentiating it gives a different equation."},
        ],
        "mistakes": [
            ("Moving the y across and leaving y′ behind",
             "The mistaken model is that &ldquo;separating&rdquo; means getting `y` to the other "
             "side of the equals sign, then integrating each side with respect to `t` with `y` "
             "treated as a constant. From `y′ = t/y` it produces `y = t²/(2y) + C`, and with "
             "`y(0) = 2` that gives `y² = t²/2 + 2y`. Differentiate it: `2y·y′ = t + 2y′`, so "
             "`y′ = t/(2y − 2)`, not `t/y`. The two agree at the starting point, where "
             "`t = 0` makes both slopes zero, which is why the error survives a check there "
             "and fails one step later. The correct move keeps `y′` with the `y`: "
             "`y·y′ = t`."),
            ("Getting C with the subtraction the wrong way round",
             "`C = G(y₀) − H(t₀)`, because the relation is `G(y) = H(t) + C`. Computing "
             "`H(t₀) − G(y₀)` flips the sign of `C`, and the relation then fails at the very "
             "point it was built from. Put `(t₀, y₀)` back in; it takes a line and catches this "
             "every time."),
            ("Dividing by g(y) and forgetting where it is zero",
             "Dividing `y′ = t·y²` by `y²` assumes `y ≠ 0`. The constant function `y = 0` solves "
             "the original equation and is absent from the separated one. When an initial value "
             "does not touch the zero it does not matter; when it does, the method gives no "
             "answer at all, and you check the zero by substitution."),
        ],
        "standard": ("Finish when you can take a separable equation and an initial value to its relation without help.",
                     "You should be able to say whether an equation separates, integrate each "
                     "side exactly, write one relation with one constant, take the constant "
                     "from the initial value in the right order, and name the value of `y` "
                     "you divided by."),
        "note": 'The method has been run, not yet justified. Why is it legitimate to integrate `y·y′` with respect to `t` as though it were an antiderivative of something? &ldquo;Why Separation Works&rdquo; answers with the chain rule, and checks each relation here by differentiating it.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "why-separation-works",
        "title": "Why Separation Works",
        "module": "Separating variables",
        "one_line": "Integrating g(y)·y′ with respect to t is legitimate because the chain rule says G(y(t)) has exactly that derivative.",
        "summary": (
            "The method of &ldquo;Separable Equations&rdquo; integrates `y·y′` as though it were the derivative of "
            "something, and it is: of `y²/2`, by the chain rule. Read backwards, the chain rule "
            "is the whole justification. Differentiating the implicit relation gives the "
            "equation back, which is also how a solution is checked. The lab's check view "
            "performs that differentiation exactly, line by line, and prints whether the result "
            "equals the right-hand side."
        ),
        "key": [
            "G(y(t)) has rate g(y)·y′   chain rule",
            "G(y) = H(t) + C   differentiated gives",
            "g(y)·y′ = h(t)   the equation back",
            "dy/dt is one symbol for y′, not a fraction",
        ],
        "key_label": "Why the method is a theorem and not a trick",
        "concepts_intro": (
            "Three ideas. The first is the chain rule from an earlier course; the second turns "
            "it round; the third says what the shorthand with the differentials is and is not."
        ),
        "concepts": [
            ("The chain rule gives the derivative of G(y(t))",
             "If `G′ = g` and `y` is a function of `t`, then `G(y(t))` has the derivative "
             "`g(y)·y′`. For `G(y) = y²/2` that is `y·y′`. The factor `y′` is not decoration: "
             "it is the rate at which the inside function moves, and it is why the `y′` stays "
             "with the `y`."),
            ("Reading it backwards integrates the left side",
             "The left side `g(y)·y′`, viewed as a function of `t`, is the derivative of "
             "`G(y(t))`. The right side `h(t)` is the derivative of `H(t)`. Two functions with "
             "equal derivatives on an interval differ by a constant, which is the `C`."),
            ("The differentials are shorthand, not quantities",
             "`∫g dy = ∫h dt` is a convenient way to write the result. In this course `dy/dt` "
             "means `y′`, one symbol, and nothing is cancelled to get from the equation to "
             "the relation. The chain rule is what is being used, and it holds whether or not "
             "you ever write a differential."),
        ],
        "read_title": "The method as a consequence of the chain rule",
        "read_intro": "The chain rule once more, the statement that justifies the method with its proof, and three relations checked by differentiating them.",
        "body": [
            ("p", "&ldquo;The Chain Rule&rdquo; in Rates of Change and the Derivative was checked exactly on "
                  "polynomials: if `u = y(t)` and `F` is a function of `u`, the rate of "
                  "`F(y(t))` is `F′(y)` times `y′`. Here `F` is an antiderivative `G`, so "
                  "`G′ = g`, and the rate is `g(y)·y′`. Nothing about `y` is assumed beyond "
                  "having a derivative."),
            ("thm", ("Separation",
                     "Suppose `G′ = g` and `H′ = h`, and `y` is differentiable on an interval. "
                     "Then `g(y)·y′ = h(t)` on that interval exactly when "
                     "`G(y(t)) − H(t)` is constant on it.")),
            ("proof", ["By the chain rule, the rate of `G(y(t)) − H(t)` is `g(y)·y′ − h(t)`.",
                       "That is zero for every `t` in the interval exactly when the equation "
                       "holds. A function whose rate is zero on an interval does not change on "
                       "it &mdash; the fact behind the constant of integration in Accumulation "
                       "and the Integral &mdash; so `G(y(t)) − H(t) = C`, one number."]),
            ("p", "So the relation `G(y) = H(t) + C` is not a heuristic. Along a solution it "
                  "holds with some constant, and the proof also runs the other way: a "
                  "differentiable `y` that satisfies the relation satisfies the equation, "
                  "wherever `g(y)` makes sense. That second direction is what a check uses."),
            ("h3", "Checking by differentiating the relation"),
            ("p", "Take the relation `y² = t² + 4`. Differentiate both sides with respect to `t`, "
                  "remembering that `y` depends on `t`: the left side gives `2y·y′` by the "
                  "chain rule, the right side gives `2t`. So `2y·y′ = 2t`, which is "
                  "`y·y′ = t`, the equation we started with."),
            ("math", [
                "y²/2 = t²/2 + 2",
                "",
                "  d/dt of the left side:    y·y′",
                "  d/dt of the right side:   t",
                "",
                "  y·y′ = t     the equation again",
                "",
                "explicit form  y = √(t² + 4):",
                "",
                "  y′ = t/√(t² + 4)",
                "  y·y′ = √(t² + 4)·t/√(t² + 4) = t",
            ]),
            ("p", "The explicit form is checked the same way, with one more use of the chain "
                  "rule for the square root. The check view of the lab does the differentiation "
                  "with exact fractions: it shows `G′ = g`, `H′ = h`, and, where the relation "
                  "can be solved for `y`, the composite `G(y(t))` differentiated. The tile "
                  "reads `equal` when the result is the equation and a dash when there is nothing "
                  "to compare."),
            ("example", ("The reciprocal preset",
                         "For `(1/y²)·y′ = t` the relation is `−1/y = t²/2 − 1`. The derivative "
                         "of `−1/y` with respect to `t` is `y′/y²`, by the chain rule, and the "
                         "derivative of `t²/2 − 1` is `t`. So `y′/y² = t`, which is "
                         "`(1/y²)·y′ = t`.")),
            ("example", ("The cube preset",
                         "For `3y²·y′ = 2t + 1` the relation is `y³ = t² + t + 1`. The derivative "
                         "of `y³` is `3y²·y′` and the derivative of the right side is `2t + 1`, "
                         "so the equation comes straight back. The lab does not solve this "
                         "relation for `y`, which would take a cube root, and the check does "
                         "not need it to.")),
            ("p", "Whenever a lesson in this course reports a solution, this is the test: "
                  "differentiate it and compare. It catches a lost sign, a missing factor of "
                  "`y′` and a wrong constant, and it needs no knowledge of how the answer was "
                  "found."),
        ],
        "lab": ("dekit", {
            "mode": "separable",
            "view": "check",
            "preset": "circle",
            "presets": [
                {"id": "circle", "label": "y·y′ = t, y(0) = 2",
                 "g": "y", "h": "t", "ic": [0, 2],
                 "expect": {"spCheck": "equal", "spImplicit": "y² = t² + 4"}},
                {"id": "recip", "label": "(1/y²)·y′ = t, y(0) = 1",
                 "g": "1/y^2", "h": "t", "ic": [0, 1],
                 "expect": {"spCheck": "equal", "spImplicit": "−1/y = t²/2 − 1"}},
                {"id": "poly", "label": "3y²·y′ = 2t + 1, y(0) = 1",
                 "g": "3y^2", "h": "2t + 1", "ic": [0, 1],
                 "expect": {"spCheck": "equal", "spImplicit": "y³ = t² + t + 1"}},
            ],
            "panel_title": "Differentiate the answer and get the equation back",
            "panel_intro": (
                "The table lists the differentiation, step by step, and the Chain-rule check "
                "tile says equal when the derivative of the relation is the equation. Pick "
                "each preset and read the rows. The view is set to the check; the select "
                "beside the tiles switches back to the solution."
            ),
        }),
        "steps_title": "Checking a solution by differentiating it",
        "steps_intro": "Four moves, and none of them needs to know how the answer was found.",
        "steps": [
            ("Differentiate the left side with respect to t",
             "Every `y` is a function of `t`, so each term picks up a factor `y′` from the "
             "chain rule: `y²` becomes `2y·y′` and `1/y` becomes `−y′/y²`."),
            ("Differentiate the right side",
             "It is a function of `t` alone, so this is an ordinary derivative, and the "
             "constant disappears."),
            ("Compare with the original equation",
             "Equal after rearranging means the relation is consistent with the equation. "
             "Unequal means a sign or a factor was lost, and the difference tells you which."),
            ("Check the starting point",
             "Substitute `(t₀, y₀)` into the relation. The derivative check says nothing about "
             "the constant, and this is the line that catches a wrong `C`."),
        ],
        "worked": {
            "title": "Differentiating the relation y² = t² + 4 and its positive branch",
            "intro": [
                "The solution of `y·y′ = t` through `y(0) = 2` from &ldquo;Separable Equations&rdquo;, checked "
                "both as a relation and as a formula. The first line is the one the lab's "
                "table prints for the first preset."
            ],
            "lines": [
                "relation   y² = t² + 4",
                "  d/dt:    2y·y′ = 2t",
                "  so       y·y′ = t           the equation",
                "",
                "formula    y = √(t² + 4)",
                "  y′ = t/√(t² + 4)",
                "  y·y′ = √(t² + 4)·t/√(t² + 4) = t",
                "",
                "point      y(0) = √4 = 2       as required",
            ],
            "after": [
                "Two checks, two different jobs. The derivative check confirms that the "
                "relation's rate is the equation's rate; the point check confirms the constant. "
                "Either one alone leaves room for a wrong answer, and together they leave "
                "none.",
                "The same relation also holds for `y = −√(t² + 4)`, which has the same square "
                "and the opposite sign. Both pass the derivative check, and only one passes the "
                "point check for a given initial value. That is the subject of the next "
                "lesson.",
            ],
        },
        "quiz_title": "Where the y′ comes from",
        "quiz": [
            {"q": "If `y` is a function of `t`, what is the derivative of `y³` with respect to `t`?",
             "a": ["`3y²`", "`3t²`", "`3y²·y′`", "`y³·y′`"],
             "c": 2,
             "why": "By the chain rule the outer rate `3y²` is multiplied by the inner rate "
                    "`y′`. Without the factor `y′` the answer would be the derivative with "
                    "respect to `y`, which is a different question."},
            {"q": "Differentiating `y³ = t² + t + 1` with respect to `t` gives which equation?",
             "a": ["`3y²·y′ = 2t + 1`", "`3y² = 2t + 1`", "`y′ = 2t + 1`", "`3y²·y′ = t² + t`"],
             "c": 0,
             "why": "The left side gives `3y²·y′` by the chain rule and the right side gives "
                    "`2t + 1`. Dropping `y′` is the commonest slip; and the constant `1` "
                    "differentiates to nothing, so it does not become `t² + t`."},
            {"q": "What is the best account of `dy/dt` in this course?",
             "a": ["A fraction of two small quantities, which is why the differentials can be cancelled",
                   "One symbol for the derivative `y′`; the shorthand `∫g dy = ∫h dt` records which variable each integral is taken with respect to",
                   "A decimal that the lab rounds",
                   "The change in `y` over the whole interval"],
             "c": 1,
             "why": "The derivative is what the difference quotients approach, one number at "
                    "each `t`. The method rests on the chain rule, which holds with no talk of "
                    "cancelling. The change over an interval is `Δy`, a different thing, and "
                    "the lab never rounds a derivative."},
            {"q": "Both `y = √(t² + 4)` and `y = −√(t² + 4)` pass the derivative check for `y·y′ = t`. What does the check say about `y(0) = 2`?",
             "a": ["Nothing; it does not involve the initial value",
                   "It rules out the negative one",
                   "It rules out the positive one",
                   "It shows that the equation has no solution"],
             "c": 0,
             "why": "The derivative check tests the equation only. The initial value is tested "
                    "by substituting the point, which the derivative never sees. Both signs "
                    "satisfy the equation; only the positive one passes through `(0, 2)`."},
        ],
        "mistakes": [
            ("Thinking dy and dt were cancelled, so the method is a trick",
             "The mistaken model is that `dy/dt` is a fraction, multiplied by the differential of "
             "`t` to leave the differential of `y`, and the whole method is an algebraic sleight that happens to work. It "
             "works for a reason: `y·y′` is the derivative of `y²/2`, and the lab's check "
             "view differentiates the answer and gets `y·y′ = t` back with exact fractions. "
             "The notation `∫g dy = ∫h dt` is a record of that fact. The test of whether you "
             "have the idea is whether you can differentiate your own answer and find the "
             "factor `y′` in it."),
            ("Dropping the factor y′ when differentiating",
             "Writing the derivative of `y²` as `2y` treats `y` as the variable. It is the "
             "variable only when you differentiate with respect to `y`. With respect to `t`, "
             "the inside function moves at rate `y′`, and the factor is there. Without it the "
             "check shows a mismatch for every preset."),
            ("Treating the derivative check as a check of the constant",
             "The constant differentiates to zero, so a wrong `C` passes every derivative "
             "check. A solution is verified by two tests: the derivative gives the equation "
             "back, and the initial point satisfies the relation."),
        ],
        "standard": ("Finish when you can differentiate an implicit relation and show that the equation comes back.",
                     "You should be able to state the chain rule for `G(y(t))`, say why it "
                     "justifies integrating `g(y)·y′`, differentiate a relation in `y` and `t` "
                     "with the factor `y′` in the right places, and explain why the derivative "
                     "check cannot catch a wrong constant."),
        "note": 'A relation such as `y² = t² + 4` is the middle of a solution, not its end. &ldquo;Implicit and Explicit Solutions&rdquo; takes it the rest of the way: solving for `y`, choosing the branch the initial value demands, and saying on which interval the answer exists.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "implicit-and-explicit-solutions",
        "title": "Implicit and Explicit Solutions",
        "module": "Separating variables",
        "one_line": "Solve the relation for y where a quadratic allows it, take the branch the initial value demands, and state where the answer exists.",
        "summary": (
            "`y² = t² + 4` is a relation, and the function it gives depends on which sign of the "
            "square root the initial value selects. The lab solves the relation for `y` when it "
            "is linear or quadratic in `y`, or a reciprocal, prints the branch through the "
            "starting point, and states the interval of `t` on which that branch exists. One of "
            "the presets exists for all `t`, one on an open interval with both ends excluded, and "
            "one ends at a finite `t` where the solution blows up."
        ),
        "key": [
            "y² = t² + 4 gives two functions, ±√(t² + 4)",
            "y(0) = −2 picks the lower branch",
            "y² = 1 − t²  ⟹  y = √(1 − t²), −1 < t < 1",
            "−1/y = t − 1  ⟹  y = 1/(1 − t), t < 1",
        ],
        "key_label": "A relation, a branch and a domain",
        "concepts_intro": (
            "Three ideas, one for each thing the lab prints after the relation: the formula, "
            "the sign, and the interval."
        ),
        "concepts": [
            ("A relation is not yet a function",
             "`y² = t² + 4` allows two values of `y` for each `t`. Each choice of a sign, "
             "continued across all the `t` where it makes sense, is a function, and both are "
             "solutions of `y·y′ = t`. The relation names the pair, and only an initial value "
             "names one of them."),
            ("The initial value picks the branch by its sign",
             "A solution passes through `(t₀, y₀)`. The positive root is above the axis and the "
             "negative root below it, so `y₀ > 0` selects the positive root and `y₀ < 0` the "
             "negative one. The branch you did not choose is still a solution, but not of "
             "this initial value problem."),
            ("The solution exists on an interval, which can be small",
             "The explicit formula is defined where the square root has a non-negative "
             "radicand and where a denominator is not zero. The solution is then the piece of "
             "that set that contains `t₀`. It may be all `t`, a bounded open interval, or a "
             "half-line that ends where the solution runs off to infinity."),
        ],
        "read_title": "From the relation to the function, and where it lives",
        "read_intro": "Solving for y, choosing the branch, reading off the interval, and three presets that differ in what the interval turns out to be.",
        "body": [
            ("p", "Take the relation `y² = t² + 4`. As an equation in `y` it is a quadratic with "
                  "no linear term, so `y = ±√(t² + 4)`. The lab handles a relation that is "
                  "linear in `y`, or quadratic in `y` with coefficients that are polynomials in "
                  "`t`, by the quadratic formula, and the reciprocal form `−1/y = H(t) + C` by "
                  "inverting. Anything else it reports as implicit only, and says so."),
            ("math", [
                "y² = t² + 4",
                "",
                "  y = √(t² + 4)       above the axis, y > 0",
                "  y = −√(t² + 4)      below the axis, y < 0",
                "",
                "  y(0) = 2    selects  y = √(t² + 4)",
                "  y(0) = −2   selects  y = −√(t² + 4)",
            ]),
            ("p", "The radicand `t² + 4` is positive for every `t`, so both branches exist "
                  "everywhere and never reach `y = 0`. That matters: the branch through "
                  "`(0, 2)` never gets to the axis, and no solution of `y′ = t/y` can cross "
                  "it, because at `y = 0` the equation gives no slope to follow. The lab's "
                  "first preset prints `y = −√(t² + 4)` and `all t`."),
            ("h3", "A domain with two ends"),
            ("p", "Now change the right side to `−t`: `y·y′ = −t` with `y(0) = 1`. Then "
                  "`y²/2 = −t²/2 + C`, and `C = 1/2`, so `y² = 1 − t²`. The branch through "
                  "`(0, 1)` is `y = √(1 − t²)`, and it exists only where `1 − t² ≥ 0`. The "
                  "lab prints the domain as `−1 < t < 1`, with both ends excluded."),
            ("p", "The ends are excluded because the solution is a function that satisfies the "
                  "differential equation, and at `t = ±1` the value is `y = 0`, where "
                  "`y′ = −t/y` has no value. The solution reaches the axis there and cannot be "
                  "continued as a solution past it; the formula survives at the ends, the "
                  "equation does not."),
            ("h3", "A domain with one end"),
            ("p", "For `(1/y²)·y′ = 1` with `y(0) = 1` the relation is `−1/y = t − 1`, and "
                  "inverting gives `y = 1/(1 − t)`. The formula is defined for every `t` except "
                  "`t = 1`, but the solution through `(0, 1)` is only the branch on the side "
                  "of `t = 1` that contains `t = 0`, which is `t < 1`. As `t` approaches 1 "
                  "from below, `y` grows without bound. This is the blow-up met in "
                  "&ldquo;Blow-Up and the Interval of Existence&rdquo;, now with a formula "
                  "attached."),
            ("example", ("Reading the interval from the formula",
                         "`y = 1/(1 − t)` is also defined for `t > 1`, where it is negative. "
                         "That piece is a solution of the equation, but it is not a "
                         "continuation of the one through `(0, 1)`: the two are separated by "
                         "the point where the formula has no value. A solution is a function "
                         "on one interval, and the interval is the piece that holds the "
                         "initial `t`.")),
            ("p", "The lab prints three tiles for this: the relation, the explicit solution "
                  "and the domain. When a relation cannot be solved for `y` the explicit tile "
                  "reads `implicit only`, and the domain is not given. That is the honest "
                  "answer for cubics and beyond: the relation is the solution, and it can "
                  "still be differentiated and checked."),
        ],
        "lab": ("dekit", {
            "mode": "separable",
            "view": "solve",
            "preset": "lower",
            "presets": [
                {"id": "lower", "label": "y·y′ = t, y(0) = −2",
                 "g": "y", "h": "t", "ic": [0, -2],
                 "expect": {"spExplicit": "y = −√(t² + 4)", "spDomain": "all t"}},
                {"id": "arc", "label": "y·y′ = −t, y(0) = 1",
                 "g": "y", "h": "-t", "ic": [0, 1],
                 "expect": {"spExplicit": "y = √(1 − t²)", "spDomain": "−1 < t < 1"}},
                {"id": "blow", "label": "(1/y²)·y′ = 1, y(0) = 1",
                 "g": "1/y^2", "h": "1", "ic": [0, 1],
                 "expect": {"spExplicit": "y = 1/(1 − t)", "spDomain": "t < 1"}},
            ],
            "panel_title": "Which branch, and on what interval",
            "panel_intro": (
                "Pick a preset and read the explicit tile and the domain tile. On the first "
                "preset change the initial value from y(0) = -2 to y(0) = 2 and watch only the "
                "sign of the formula change. On the second, change it to y(0) = 2 and compare "
                "the interval with the one it printed before."
            ),
        }),
        "steps_title": "From a relation to a solution on an interval",
        "steps_intro": "Four moves after the relation is written. The third and fourth are the ones that are usually skipped.",
        "steps": [
            ("Solve for y if the relation allows it",
             "Linear in `y`: one function. Quadratic in `y`: the quadratic formula gives "
             "two. If neither, say implicit only, and stop here."),
            ("Choose the branch with the initial value",
             "Compare the sign of `y₀` with the signs of the two roots at `t₀`. Exactly one "
             "matches. If `y₀` is zero the two roots coincide, neither branch is "
             "differentiable there, and `y′ = h(t)/g(y)` has no slope to give; the lab "
             "reports implicit only."),
            ("Find where the formula is defined",
             "A square root needs a non-negative radicand; a denominator must not be zero. "
             "Write the set of `t` where both hold."),
            ("Keep the piece that contains t₀",
             "A solution lives on one interval. State it with its ends open or closed as the "
             "equation dictates, and say what happens at an open end."),
        ],
        "worked": {
            "title": "y·y′ = t with y(0) = −2",
            "intro": [
                "The same equation as before, with the starting value on the other side of "
                "the axis. The relation is unchanged, and the branch and the interval are what "
                "the initial value decides."
            ],
            "lines": [
                "y²/2 = t²/2 + C       C = (−2)²/2 − 0 = 2",
                "y² = t² + 4",
                "",
                "y = √(t² + 4)    or    y = −√(t² + 4)",
                "",
                "y(0) = −2 < 0   so   y = −√(t² + 4)",
                "t² + 4 > 0 for every t, so the domain is all t",
                "",
                "check:  −√4 = −2     as required",
            ],
            "after": [
                "The positive branch is a perfectly good solution of the equation. It simply "
                "never passes through `(0, −2)`, and since no solution of `y′ = t/y` can "
                "cross the axis, a start below it stays below it for every `t`.",
                "Try the second preset next and compare the domain: the formula `√(1 − t²)` is "
                "defined on a closed interval, but the solution is defined only on the open one, "
                "because at each end the slope `−t/y` has no value. The domain tile prints "
                "`−1 < t < 1`.",
            ],
        },
        "quiz_title": "Branch and interval",
        "quiz": [
            {"q": "For `y·y′ = t` with `y(0) = −2`, which formula is the solution?",
             "a": ["`y = √(t² + 4)`", "`y = −√(t² + 4)`", "`y = ±√(t² + 4)`", "`y = t²/2 − 2`"],
             "c": 1,
             "why": "The relation `y² = t² + 4` gives both signs, and the initial value picks "
                    "the one with `y(0) = −2`, which is the negative root. The plus-or-minus "
                    "form is the relation, not a function. The last formula has the wrong "
                    "derivative: it gives `y′ = t`, not `t/y`."},
            {"q": "The relation `y² = 1 − t²` with `y(0) = 1` gives `y = √(1 − t²)`. On which `t` is this a solution?",
             "a": ["`−1 < t < 1`", "Every real `t`", "`−1 ≤ t ≤ 1`", "`t ≥ 0`"],
             "c": 0,
             "why": "The formula needs `1 − t² ≥ 0`, which is `−1 ≤ t ≤ 1`, but at `t = ±1` the "
                    "value of `y` is zero and `y′ = −t/y` has no value, so the ends are not "
                    "included in the interval on which the equation holds. `t ≥ 0` has no "
                    "reason behind it, and every real `t` would put a negative number under "
                    "the root."},
            {"q": "`y = 1/(1 − t)` is defined for every `t` except `t = 1`. For the solution of `(1/y²)·y′ = 1` through `y(0) = 1`, what is the interval of existence?",
             "a": ["`t > 1`", "All `t` except `1`", "`t ≤ 1`", "`t < 1`"],
             "c": 3,
             "why": "A solution is a function on one interval containing the initial `t = 0`, "
                    "and the formula breaks at `t = 1`. The piece to the left of 1 contains "
                    "0; the piece to the right is a different solution. `t ≤ 1` would include "
                    "a point where the formula has no value."},
            {"q": "A student reads `y² = t² + 4` and writes `y = √(t² + 4)` for the initial value `y(0) = −2`. What does checking the point show?",
             "a": ["It passes, because squares are positive", "It passes, because the relation is satisfied",
                   "It fails: the formula gives `y(0) = 2`, not `−2`", "It cannot be checked without a derivative"],
             "c": 2,
             "why": "The relation is satisfied by `(0, −2)`, but the formula `y = √(t² + 4)` "
                    "is the positive root and gives `y(0) = 2`. Substituting the initial "
                    "point into the formula, not the relation, is the check that catches "
                    "the wrong branch."},
        ],
        "mistakes": [
            ("Reading y² = t² + 4 as the positive root alone",
             "The mistaken model is that the square root is the inverse of the square, so "
             "taking it recovers `y`. It recovers `|y|`. Whether `y` is the positive or the "
             "negative root is information the relation does not carry, and the initial value "
             "does: `y(0) = −2` gives `y = −√(t² + 4)`, and the formula "
             "`√(t² + 4)` has the value `2` at `t = 0`, not `−2`. The lab's first preset "
             "prints the negative branch for this reason."),
            ("Stating the domain of the formula instead of the solution",
             "`√(1 − t²)` is defined on `−1 ≤ t ≤ 1`, but the solution of `y·y′ = −t` is "
             "defined only on `−1 < t < 1`, because the equation has no slope where "
             "`y = 0`. And `1/(1 − t)` is defined on two pieces, of which only one contains "
             "the initial `t`. The domain of a solution is a statement about the equation "
             "and the starting point, not about the algebra."),
            ("Switching branches across a zero of the radicand",
             "At a point where `y = 0` the two branches meet, and a curve that looks "
             "continuous can be drawn from one to the other. It is not a solution there: "
             "each branch arrives with an infinite slope, and the equation, which needs "
             "`g(y)·y′` to equal `h(t)` at the join, does not hold. A solution stays on "
             "the branch it started on."),
        ],
        "standard": ("Finish when you can go from an implicit relation and an initial value to an explicit solution and its interval.",
                     "You should be able to solve a quadratic relation for `y`, pick the "
                     "branch by the sign of the initial value, find where the radicand or "
                     "denominator stops the formula, and state the interval of existence "
                     "with its ends correctly open."),
        "note": 'With the method, its justification and its answer fully in hand, the next lesson applies them to the simplest separable equation there is, `y′ = k·y`, whose solution is the exponential. &ldquo;Exponential Growth&rdquo; also runs Euler\'s method on it, and the exact fractions turn out to be a geometric sequence.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "exponential-growth",
        "title": "Exponential Growth",
        "module": "Exponential change",
        "one_line": "The equation whose rate is proportional to its size separates to y₀·e^(kt), and Euler's method on it is the geometric sequence y₀·(1 + kh)ⁿ in exact fractions.",
        "summary": (
            "The equation `y′ = k·y` says a quantity changes at a rate proportional to its "
            "size, and separation solves it: `y = y₀·e^(kt)`. Euler's method on the same "
            "equation multiplies by the same factor `1 + kh` at every step, so its output is "
            "the geometric sequence `y₀·(1 + kh)ⁿ`, an exact fraction at every step. The lab "
            "prints that fraction beside `e^(kt)`, which is rounded, and the gap between them "
            "shrinks as the step does."
        ),
        "key": [
            "y′ = k·y  ⟹  y = y₀·e^(kt)",
            "Euler: yₙ₊₁ = (1 + kh)·yₙ",
            "so yₙ = y₀·(1 + kh)ⁿ   geometric, ratio 1 + kh",
            "y′ = y, h = 1/4, n = 4:  625/256 ≈ 2.44141",
            "the true value at t = 1 is e ≈ 2.71828",
        ],
        "key_label": "One equation, two answers, and how far apart they are",
        "concepts_intro": (
            "Three ideas: the equation and its exact solution, the method's solution, and the "
            "distance between the two."
        ),
        "concepts": [
            ("The rate is proportional to the size",
             "`y′ = k·y` with `k` a constant. The bigger the quantity, the faster it changes, "
             "in the same proportion. For `k > 0` that is growth, for `k < 0` decay, and the "
             "number `k` has the units of one over time. Nothing in the equation says the "
             "growth is fast; a small `k` is slow, and the solution is still exponential."),
            ("Separation gives y₀·e^(kt), exactly",
             "Writing the equation as `(1/y)·y′ = k` and integrating gives `ln(|y|) = kt + C`, "
             "and with `y(0) = y₀` the solution is `y = y₀·e^(kt)`. The value `e^(kt)` is "
             "irrational for rational `kt ≠ 0`, so every figure from the closed form on this "
             "page is rounded and carries `≈`."),
            ("Euler multiplies by a fixed factor each step",
             "One Euler step is `yₙ₊₁ = yₙ + h·k·yₙ = (1 + kh)·yₙ`. The factor does not depend "
             "on `n`. So `yₙ = y₀·(1 + kh)ⁿ`, which is a geometric sequence with ratio "
             "`1 + kh`, and for rational `k`, `h` and `y₀` every term is an exact fraction."),
        ],
        "read_title": "The same equation solved twice",
        "read_intro": "Separation first, then Euler's steps, then the two side by side, with the lab's numbers for step sizes one quarter and one sixteenth.",
        "body": [
            ("def", ("Exponential growth and decay",
                     "A quantity `y(t)` obeys <strong>exponential growth</strong> when "
                     "`y′ = k·y` for a constant `k > 0`, and <strong>exponential decay</strong> "
                     "when `k < 0`. The number `k` is the <strong>rate constant</strong>.",
                     "The name describes the form of the solution, not its speed: "
                     "`y₀·e^(kt)` is exponential for every `k ≠ 0`, however small.")),
            ("thm", ("The exponential solution",
                     "The solution of `y′ = k·y` with `y(0) = y₀` is `y = y₀·e^(kt)`.")),
            ("proof", ["Take `y₀ > 0`; for `y₀ < 0` the same lines run with `|y|`, and "
                       "`y₀ = 0` gives the constant solution `y = 0`, which the formula "
                       "covers as well. While `y > 0`, "
                       "the equation separates as `(1/y)·y′ = k`, so `ln y = kt + C` by the "
                       "method of &ldquo;Separable Equations&rdquo;, with `1/y` integrated to `ln y` as in "
                       "&ldquo;The Integral of 1/t&rdquo;.",
                       "At `t = 0` that says `C = ln y₀`, so `ln y − ln y₀ = kt`, which is "
                       "`y = y₀·e^(kt)`. The check is the rate of `e^(kt)` from &ldquo;The "
                       "Exponential and Its Rate&rdquo;: the rate of `y₀·e^(kt)` is `k·y₀·e^(kt)`, which is `k·y`."]),
            ("p", "That is a solution in closed form, and it is what every figure on this page "
                  "will be compared with. It is also the only kind of statement here that is "
                  "not an exact fraction: `e^(kt)` has no finite fraction, so the lab prints it "
                  "rounded to six figures and marks it `≈`."),
            ("h3", "What Euler's method does to it"),
            ("p", "Take `y′ = y`, `y(0) = 1`, `h = 1/4`. The first step is `1 + (1/4)·1 = 5/4`. "
                  "The second is `5/4 + (1/4)·(5/4) = 25/16`, which is `(5/4)²`. Every step "
                  "multiplies by `5/4`, because the rate is the value itself, and "
                  "so after four steps, at `t = 1`, the lab prints `625/256`, which is "
                  "`(5/4)⁴` exactly."),
            ("math", [
                "y′ = k·y,   step h",
                "",
                "  yₙ₊₁ = yₙ + h·(k·yₙ) = (1 + kh)·yₙ",
                "",
                "  y₁ = (1 + kh)·y₀",
                "  y₂ = (1 + kh)²·y₀",
                "  yₙ = (1 + kh)ⁿ·y₀",
                "",
                "k = 1,  y₀ = 1,  h = 1/4:   factor 5/4",
                "  y₄ = (5/4)⁴ = 625/256",
            ]),
            ("p", "This is the geometric sequence of &ldquo;Geometric Sequences and Series&rdquo; in "
                  "Algebra's Sequences and Series: each term is the previous one times a "
                  "fixed ratio, here `1 + kh`. Euler's method on a growth equation is that "
                  "sequence under another name. The ratio is a rational number, so nothing in "
                  "it is rounded."),
            ("h3", "Beside the true value"),
            ("p", "The value `625/256` is about `2.44141`; the closed form at `t = 1` is "
                  "`e ≈ 2.71828`, rounded. The lab's error tile prints the difference as "
                  "`≈ 0.276876`. That is not because any step was computed wrongly: each step "
                  "assumed the rate stayed at its starting value across the step, while the real rate "
                  "kept climbing. The exact sequence is always below the curve for growth."),
            ("math", [
                "y′ = y,  y(0) = 1,  t = 1,  h = 1/n,  yₙ = (1 + 1/n)ⁿ",
                "",
                "  n = 1:    y₁ = 2",
                "  n = 2:    y₂ = 9/4            = 2.25",
                "  n = 4:    y₄ = 625/256        ≈ 2.44141",
                "  n = 16:   y₁₆ = (17/16)¹⁶     ≈ 2.63793",
                "",
                "  the true value:  e ≈ 2.71828",
            ]),
            ("p", "As the step shrinks the sequence climbs towards `e`, which is the sequence "
                  "met in &ldquo;The Number e&rdquo; in Algebra's Exponential and Logarithmic Functions, "
                  "built here directly from a differential equation. That the values approach "
                  "`e` is a claim the table suggests and does not prove; &ldquo;Euler's Error and the Step "
                  "Size&rdquo; in the previous course measured how fast, and found the error "
                  "roughly halving each time the step does."),
        ],
        "lab": ("dekit", {
            "mode": "growth",
            "preset": "unit",
            "presets": [
                {"id": "unit", "label": "y′ = y, y(0) = 1, h = 1/4, 4 steps",
                 "k": 1, "y0": 1, "A": 0, "h": "1/4", "n": 4, "target": None,
                 "expect": {"grFactor": "5/4", "grLast": "625/256", "grTrue": "≈ 2.71828"}},
                {"id": "half", "label": "y′ = y/2, y(0) = 2, h = 1/4, 8 steps",
                 "k": "1/2", "y0": 2, "A": 0, "h": "1/4", "n": 8, "target": None,
                 "expect": {"grFactor": "9/8", "grLast": "43046721/8388608", "grTrue": "≈ 5.43656"}},
                {"id": "fine", "label": "y′ = y, y(0) = 1, h = 1/16, 16 steps",
                 "k": 1, "y0": 1, "A": 0, "h": "1/16", "n": 16, "target": None,
                 "expect": {"grFactor": "17/16", "grLast": "48661191875666868481/18446744073709551616",
                            "grTrue": "≈ 2.71828"}},
            ],
            "panel_title": "Euler's steps as a geometric sequence, beside e^(kt)",
            "panel_intro": (
                "Each row of the table is one step: the exact yₙ, and the closed form rounded "
                "beside it. The factor tile is 1 + kh, and the last tile pair is the exact end "
                "value and the rounded true one. Compare the first and third presets: the same "
                "equation and the same end time, with the step cut by four."
            ),
        }),
        "steps_title": "Solving the growth equation two ways",
        "steps_intro": "Do both, and compare them. Either one alone leaves you with a number and no idea how far to trust it.",
        "steps": [
            ("Read off k",
             "Write the equation as `y′ = k·y` and identify `k` with its sign. If the right "
             "side is `−3y`, then `k = −3`, and the quantity decays."),
            ("Solve by separation",
             "`(1/y)·y′ = k`, `ln(|y|) = kt + C`, and `y = y₀·e^(kt)` from the initial value. "
             "Check by differentiating: the rate of `e^(kt)` is `k·e^(kt)`."),
            ("Find Euler's factor",
             "`1 + kh`, a fraction when `k` and `h` are. Write it down before any steps; the "
             "whole table is its powers."),
            ("Write yₙ and compare",
             "`yₙ = y₀·(1 + kh)ⁿ` against `y₀·e^(k·nh)`. The difference is the method's "
             "error at this step size, and it is of the sign the factor dictates."),
            ("Shrink the step and repeat",
             "Halve `h`, double `n`, and watch the error fall. That it falls is the reason "
             "Euler's method is useful, and how fast is the reason the later lessons exist."),
        ],
        "worked": {
            "title": "y′ = y from y(0) = 1, with h = 1/4",
            "intro": [
                "The factor is `1 + 1·(1/4) = 5/4` and the end time is `t = 4·(1/4) = 1`. "
                "Every number below is exact until the last line, which is the closed form "
                "and says so."
            ],
            "lines": [
                "factor      1 + kh = 1 + 1/4 = 5/4",
                "",
                "y₀ = 1",
                "y₁ = 5/4",
                "y₂ = 25/16",
                "y₃ = 125/64",
                "y₄ = 625/256          ≈ 2.44141",
                "",
                "closed form  e^1       ≈ 2.71828   (rounded)",
                "error                  ≈ 0.276876",
            ],
            "after": [
                "Every step is the one before multiplied by `5/4`, and there is no other "
                "arithmetic in the column. The sequence is geometric, and the error is "
                "the whole of what is wrong with it.",
                "Now run the third preset: the step is `1/16`, there are 16 steps, and the "
                "end value is `(17/16)¹⁶`, about `2.63793`. The end time is still `t = 1`, and "
                "the sequence has moved most of the way to `e ≈ 2.71828`. The second preset "
                "has a different rate and start (`k = 1/2`, `y₀ = 2`), and its factor is `9/8`.",
            ],
        },
        "quiz_title": "Rates, factors and sequences",
        "quiz": [
            {"q": "Euler's method is applied to `y′ = 3y` with step `h = 1/10`. What is the factor each step multiplies by?",
             "a": ["3/10", "31/30", "13/10", "4"],
             "c": 2,
             "why": "The factor is `1 + kh = 1 + 3·(1/10) = 13/10`. The value `3/10` is `k·h` "
                    "alone, which would be the increase and not the new value; `31/30` "
                    "divides by `k` instead of multiplying; and `4` adds `k` to 1 without "
                    "the step."},
            {"q": "In the second preset the factor is `9/8` and `y₀ = 2`. What is `y₂`, exactly?",
             "a": ["9/4", "81/64", "11/4", "81/32"],
             "c": 3,
             "why": "`y₂ = 2·(9/8)² = 2·81/64 = 81/32`. The value `9/4` is `y₁`; `81/64` forgets "
                    "the starting value `2`; and `11/4` adds instead of multiplying."},
            {"q": "The sequence `1, 5/4, 25/16, 125/64, …` is Euler's output for `y′ = y` with `h = 1/4`. What kind of sequence is it?",
             "a": ["Geometric, with ratio `5/4`", "Arithmetic, with difference `1/4`",
                   "Neither, because the terms are fractions", "Geometric, with ratio `1/4`"],
             "c": 0,
             "why": "Each term is the previous one times `5/4`, which is the definition of a "
                    "geometric sequence. The differences are `1/4, 5/16, 25/64, …`, which are "
                    "not constant, and fractions are allowed as terms."},
            {"q": "A cell culture obeys `y′ = (1/100)·y`. Is this exponential growth?",
             "a": ["No, because it grows slowly", "Yes: the solution is `y₀·e^(t/100)`, and exponential names the form, not the speed",
                   "Only after `t` exceeds 100", "No, because `k` must be larger than 1"],
             "c": 1,
             "why": "The form of the solution decides it: a constant `k > 0` gives "
                    "`y₀·e^(kt)` however small `k` is. In the lab with step `1/4` it multiplies "
                    "by `401/400` per step, a genuine geometric sequence with a ratio close "
                    "to 1."},
        ],
        "mistakes": [
            ("Thinking exponential means fast, and that a geometric sequence is something else",
             "The mistaken model is that &ldquo;exponential&rdquo; is a word for rapid growth, "
             "and that the geometric sequences of Algebra and the exponential functions of "
             "calculus are two topics. Neither holds. `y′ = (1/100)·y` is exponential: the lab "
             "with `h = 1/4` gives a factor of `401/400`, a ratio close to 1, and still a "
             "geometric sequence. Euler's method turns every `y′ = k·y` into exactly that "
             "sequence, with ratio `1 + kh`. What distinguishes exponential growth is that the "
             "rate is proportional to the size, not that it is large."),
            ("Reading yₙ as the solution at tₙ",
             "The lab's `625/256` is a correct value of Euler's method at `t = 1`, and the "
             "solution there is `e ≈ 2.71828`. The first is exact arithmetic applied to an "
             "approximate method; the second is the quantity the equation describes. They "
             "differ by about `0.276876` at this step size, and by a different amount at "
             "another."),
            ("Forgetting the 1 in the factor",
             "Euler adds the change to the old value, so the factor is `1 + kh`, not `k·h`. "
             "With `kh = 1/4` the wrong factor `1/4` would make the sequence shrink to zero "
             "for a growth equation. A quick check: for `k > 0` the factor must exceed 1."),
        ],
        "standard": ("Finish when you can solve the growth equation by separation and by Euler's method and say how far apart the answers are.",
                     "You should be able to write the exact solution `y₀·e^(kt)`, compute "
                     "Euler's factor `1 + kh` as a fraction, write `yₙ` as a power of it, "
                     "recognise the sequence as geometric, and report the rounded error "
                     "with the step size beside it."),
        "note": 'The equation `y′ = k·y` has a clock hidden in it: the time for the quantity to double does not depend on how much there is. &ldquo;Doubling Time and Half-Life&rdquo; derives that time and finds the first Euler step at which the exact sequence passes double.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "doubling-time-and-half-life",
        "title": "Doubling Time and Half-Life",
        "module": "Exponential change",
        "one_line": "T = ln 2/k comes from e^(kT) = 2, it does not depend on the amount you start with, and the exact Euler sequence passes double at a step the lab names.",
        "summary": (
            "Every solution of `y′ = k·y` doubles in the same time, `T = ln 2/k`, whatever its "
            "starting amount, and a decaying one halves in `ln 2/|k|`. The time is irrational, "
            "so the lab prints it rounded. The exact Euler sequence passes the target at a "
            "particular step, and the lab prints that step and its time as exact values: they "
            "sit on the grid of steps, not at the true time."
        ),
        "key": [
            "e^(kT) = 2  ⟹  T = ln 2/k",
            "ln 2 ≈ 0.693147   (rounded)",
            "T does not depend on y₀",
            "k = 1/2:  T ≈ 1.38629;  k = 1/10:  T ≈ 6.93147",
            "Euler passes 2 at a grid step, not at T",
        ],
        "key_label": "The doubling time, derived and read",
        "concepts_intro": (
            "Three ideas: the derivation, the independence from the start, and the difference "
            "between the true time and the step on which the exact sequence crosses."
        ),
        "concepts": [
            ("T comes from one equation",
             "The solution `y₀·e^(kt)` has doubled when `e^(kT) = 2`. Taking the natural logarithm of both sides "
             "gives `kT = ln 2`, so `T = ln 2/k`. For `k < 0` the quantity halves when "
             "`e^(kT) = 1/2`, and `T = ln 2/|k|`. The number `ln 2` is irrational: "
             "`≈ 0.693147` to six figures."),
            ("The start drops out",
             "The amount at time `t + T` is `y₀·e^(k·(t + T)) = y₀·e^(kt)·e^(kT) = 2·y(t)`. "
             "Whatever `y(t)` is, doubling it takes `T`. A culture of a thousand and a "
             "culture of a million, with the same `k`, have the same doubling time."),
            ("Euler crosses on the grid",
             "The exact sequence `y₀·(1 + kh)ⁿ` exists only at multiples of `h`. The first step "
             "`n` with `yₙ` at least double the start is an exact statement about the sequence, "
             "and the lab prints it with its time. For growth it is never earlier than `T`, "
             "and how much later it falls depends on the step: within a step for a fine one, "
             "more than a step for a coarse one."),
        ],
        "read_title": "The time to double, and the step that first gets there",
        "read_intro": "The derivation, the independence from the start, and the exact crossing step of the sequence from “Exponential Growth”.",
        "body": [
            ("p", "Take `y′ = (1/2)·y`, so `k = 1/2`. The solution is `y₀·e^(t/2)`, and it "
                  "doubles when `e^(T/2) = 2`, which is `T/2 = ln 2` and `T = 2·ln 2`. The "
                  "lab prints this as `ln 2/(1/2)` and then `≈ 1.38629`, rounded; the "
                  "irrational factor is `ln 2 ≈ 0.693147`."),
            ("math", [
                "y = y₀·e^(kt)",
                "",
                "  doubled when   y = 2·y₀",
                "  e^(kT) = 2",
                "  kT = ln 2",
                "  T = ln 2/k",
                "",
                "k = 1/2:    T = 2·ln 2     ≈ 1.38629",
                "k = 1/10:   T = 10·ln 2    ≈ 6.93147",
                "k = −1/2:   half-life 2·ln 2    ≈ 1.38629",
            ]),
            ("p", "A bigger rate constant gives a shorter doubling time, and the product "
                  "`k·T = ln 2` is the same for every equation of this kind. A useful "
                  "consequence: `T ≈ 0.693/k`, so a rate of `k = 0.07` per year, about seven "
                  "percent, doubles in about ten years. That is rounded, and the lab prints "
                  "it as rounded whenever it appears."),
            ("h3", "The start drops out"),
            ("p", "Begin with `y₀ = 1` and the target `2`, and again with `y₀ = 8` and the "
                  "target `4` and `k = −1/2`: the lab prints the same time, `≈ 1.38629`, because "
                  "`k` is the only thing the formula uses. Change the start to `5` and the "
                  "target to `10` on the first preset to see the same step and the same time "
                  "again. The amount scales the whole curve and moves nowhere along the time "
                  "axis."),
            ("h3", "Where the exact sequence crosses"),
            ("p", "With `k = 1/2` and `h = 1/4` the factor is `9/8`. The terms "
                  "`(9/8)⁵ = 59049/32768 ≈ 1.80203` and `(9/8)⁶ = 531441/262144 ≈ 2.02729` "
                  "straddle `2`, so the exact sequence first reaches double at step 6, which is "
                  "`t = 6·(1/4) = 3/2`. The lab prints `step 6 (t = 3/2)`."),
            ("math", [
                "k = 1/2, h = 1/4, factor 9/8, y₀ = 1, target 2",
                "",
                "  step 5   (9/8)⁵ = 59049/32768   ≈ 1.80203   below 2",
                "  step 6   (9/8)⁶ = 531441/262144 ≈ 2.02729   at or above 2",
                "",
                "  first step past the target:  step 6, t = 3/2",
                "  true doubling time:          T ≈ 1.38629",
            ]),
            ("p", "The true curve passes `2` at `T ≈ 1.38629`, between steps 5 and 6. For "
                  "growth the exact Euler sequence lies below the curve, so it cannot cross "
                  "earlier than the curve does: the crossing step is at or after the first "
                  "grid point past `T`, and here it is that grid point. It need not be. A "
                  "coarser step leaves the sequence further below the curve, and in the "
                  "third preset the crossing comes a whole step after the grid point that "
                  "follows `T`."),
            ("example", ("A coarse step, a late crossing",
                         "For `k = 1/10` and `h = 1` the factor is `11/10`. The terms "
                         "`(11/10)⁷ = 19487171/10000000 ≈ 1.94872` and `(11/10)⁸ ≈ 2.14359` "
                         "straddle 2, so the lab prints `step 8 (t = 8)`. The true doubling "
                         "time is `T ≈ 6.93147`, so at `t = 7` the closed form column already "
                         "reads `≈ 2.01375`, while the exact sequence at step 7 is still "
                         "below 2: it is late by a whole step.")),
        ],
        "lab": ("dekit", {
            "mode": "growth",
            "preset": "double",
            "presets": [
                {"id": "double", "label": "k = 1/2, y(0) = 1, h = 1/4, target 2",
                 "k": "1/2", "y0": 1, "A": 0, "h": "1/4", "n": 8, "target": 2,
                 "expect": {"grT": "≈ 1.38629", "grHit": "step 6 (t = 3/2)"}},
                {"id": "halve", "label": "k = −1/2, y(0) = 8, h = 1/4, target 4",
                 "k": "-1/2", "y0": 8, "A": 0, "h": "1/4", "n": 8, "target": 4,
                 "expect": {"grT": "≈ 1.38629", "grHit": "step 6 (t = 3/2)"}},
                {"id": "slow", "label": "k = 1/10, y(0) = 1, h = 1, target 2",
                 "k": "1/10", "y0": 1, "A": 0, "h": 1, "n": 16, "target": 2,
                 "expect": {"grT": "≈ 6.93147", "grHit": "step 8 (t = 8)"}},
            ],
            "panel_title": "The doubling time, and the first step past the target",
            "panel_intro": (
                "The doubling-or-halving tile is ln 2 over the size of k, rounded. The step "
                "tile is the first exact Euler value at or past the target in the direction "
                "of travel, with its time. Change the start and the target together on the "
                "first preset and see that only the table's numbers move."
            ),
        }),
        "steps_title": "Finding a doubling time or a half-life",
        "steps_intro": "Five moves, and the last one is the one that stops a coarse step being mistaken for the answer.",
        "steps": [
            ("Identify k and its sign",
             "Positive means doubling, negative means halving. The time uses `|k|` only."),
            ("Set the quantity equal to its target",
             "`y₀·e^(kT) = 2·y₀` for doubling, `y₀·e^(kT) = y₀/2` for halving. The `y₀` "
             "cancels, and that is why the answer does not depend on it."),
            ("Take the logarithm",
             "`kT = ln 2`, so `T = ln 2/|k|`. Quote it rounded and marked `≈`, since "
             "`ln 2` is irrational."),
            ("Find the crossing step of the exact sequence",
             "Compute `(1 + kh)ⁿ` for increasing `n` until it passes 2 (or falls to 1/2). "
             "The first such `n` and the time `n·h` are exact."),
            ("Compare the two times",
             "The grid time is at least `T` for growth, with the gap set by `h`. Report the "
             "step size alongside it."),
        ],
        "worked": {
            "title": "k = 1/2, h = 1/4, target 2",
            "intro": [
                "The true time first, rounded, and then the exact sequence's crossing, which "
                "is exact."
            ],
            "lines": [
                "T = ln 2/(1/2) = 2·ln 2        ≈ 1.38629   (rounded)",
                "",
                "factor    1 + (1/2)(1/4) = 9/8",
                "(9/8)⁵ = 59049/32768           ≈ 1.80203   below 2",
                "(9/8)⁶ = 531441/262144         ≈ 2.02729   at or above 2",
                "",
                "first step past 2:  step 6,  t = 6/4 = 3/2",
                "gap to the true T:  3/2 − T ≈ 0.113706",
            ],
            "after": [
                "Euler underestimates growth, so it is late by the part of a step it needs "
                "to make up. Here that is part of a quarter-step, and with the step "
                "equal to 1 in the third preset it is more than a whole one. Neither is wrong "
                "arithmetic; the first is the exact sequence and the second is the "
                "true curve, and they are different objects.",
                "The decay preset runs the same arithmetic downward: the factor is `7/8` and "
                "the exact sequence from 8 first reaches 4 or below at step 6, the same "
                "step, though not for the same reason. For decay the factor `7/8` is below "
                "`e^(−1/8)`, so the sequence falls faster than the curve and could cross "
                "early; here both cross between steps 5 and 6. Its time is the half-life, "
                "which equals the doubling time for the opposite rate.",
            ],
        },
        "quiz_title": "Doubling, halving and the grid",
        "quiz": [
            {"q": "For `y′ = (1/10)·y`, the doubling time is `ln 2/k`. What does the lab print?",
             "a": ["≈ 0.0693147", "≈ 6.93147", "≈ 10", "≈ 20"],
             "c": 1,
             "why": "`ln 2/(1/10) = 10·ln 2 ≈ 6.93147`. The value `0.0693147` multiplies by "
                    "`k` instead of dividing; 10 is `1/k`, which is the time constant and not "
                    "the doubling time; and 20 would be two doublings of nothing in particular."},
            {"q": "A culture of 500 cells doubles in 3 hours. Under the same conditions, how long does a culture of 5000 cells take to double?",
             "a": ["30 hours", "0.3 hours", "3 hours", "6 hours"],
             "c": 2,
             "why": "The doubling time is `ln 2/k`, and `k` is the same, so the time is the "
                    "same. The start only scales the curve. A larger start reaches larger "
                    "numbers sooner in absolute terms but does not double faster."},
            {"q": "With factor `11/10` and `y₀ = 1`, at which step does the exact Euler sequence first reach 2 or more?",
             "a": ["Step 8", "Step 7", "Step 10", "Step 6.93"],
             "c": 0,
             "why": "`(11/10)⁷ ≈ 1.94872` is below 2 and `(11/10)⁸ ≈ 2.14359` is above. Step 7 "
                    "is where the true curve is already past 2 but the sequence is not, which "
                    "is the trap; steps are whole numbers, so 6.93 is not a step."},
            {"q": "How do the doubling time for `k = 1/2` and the half-life for `k = −1/2` compare?",
             "a": ["The half-life is half as long", "The doubling time is twice the half-life",
                   "They cannot be compared", "They are equal"],
             "c": 3,
             "why": "Both are `ln 2/|k|`, which is `ln 2/(1/2) ≈ 1.38629`. Only the sign of `k` "
                    "differs between growth and decay, and the time uses its size."},
        ],
        "mistakes": [
            ("Believing the doubling time depends on the starting amount",
             "The mistaken model is that a larger amount takes longer to double, because "
             "there is more to double, or shorter, because it is growing faster in absolute "
             "terms. Neither is right. At `t + T` the amount is `y₀·e^(kt)·e^(kT) = 2·y(t)`, "
             "so every amount doubles in `T = ln 2/k`. The lab's first two presets start "
             "from 1 and from 8 and print the same `≈ 1.38629`, and the formula has no "
             "place to put the start."),
            ("Getting T upside down",
             "Writing `T = k/ln 2`, or `T = ln 2·k`, reverses the sensible direction: a faster "
             "rate must shorten the time. The check is that `k·T = ln 2` for every equation of "
             "this kind, a constant, so doubling `k` halves `T`. With `k = 1/10` the lab "
             "prints `≈ 6.93147`; with `k = 1/2`, `≈ 1.38629`, about five times shorter."),
            ("Reading the crossing step as the doubling time",
             "The tile `step 6 (t = 3/2)` is exact, and it is a statement about the Euler "
             "sequence on its grid. The doubling time of the equation is `≈ 1.38629`. They "
             "agree to within one step, and the lab prints both so that the gap is visible "
             "rather than assumed away."),
        ],
        "standard": ("Finish when you can derive the doubling time, quote it rounded, and find the crossing step of the exact sequence.",
                     "You should be able to turn a rate constant into a doubling time or a "
                     "half-life, explain why the starting amount does not enter, compute "
                     "powers of the Euler factor until one passes the target, and say how "
                     "the grid time and the true time differ."),
        "note": 'Decay is the same equation with a negative rate, and it brings the first honest application: how old is a sample that has lost three quarters of its carbon? &ldquo;Radioactive Decay and Dating&rdquo; converts a half-life to a rate and back.',
    },
]
