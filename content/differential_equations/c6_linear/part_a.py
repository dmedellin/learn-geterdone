"""First-Order Linear Equations -- the first half.

The standard form, the constant-coefficient equation and its steady state, the
integrating factor as the product rule read backwards, and the split of every
solution into a homogeneous part and one particular part.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py
(mode linear1), by executing its shipped JavaScript under node, and pinned in
`expect`. A figure that is rounded is printed with the approximation sign and
says so; everything else is an exact fraction or an exact symbolic expression.
Where the lab refuses an equation, the lesson says that it is the lab that is
limited and not the mathematics.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-standard-form",
        "title": "The Standard Form",
        "module": "The linear form",
        "one_line": "Divide by the coefficient of y′, read off p and q, and the equation is in the one shape every method on this course assumes.",
        "summary": (
            "A first-order linear equation is any equation in which the unknown and its "
            "rate each appear once, to the first power, multiplied by something that may "
            "depend on `t` however it likes. Dividing through by the coefficient of "
            "`y′` puts it in the standard form `y′ + p(t)·y = q(t)`, and everything the "
            "rest of this course does starts from reading `p` and `q` off that line. "
            "The word <em>linear</em> is about `y`, never about `t`."
        ),
        "key": [
            "y′ + p(t)·y = q(t)    y′ has coefficient 1",
            "a·y′ + b·y = c   gives   p = b/a, q = c/a",
            "linear: y and y′ appear alone, to power 1",
            "t may appear anywhere: t²·y is still linear",
            "q = 0 is homogeneous;  q ≠ 0 is forced",
        ],
        "key_label": "The shape every later method assumes",
        "concepts_intro": (
            "Three ideas, and none of them is a technique for solving anything yet. "
            "They decide which equations the techniques apply to, and what the two "
            "functions the techniques are built from are called."
        ),
        "concepts": [
            ("The standard form puts a 1 in front of y′",
             "An equation `a(t)·y′ + b(t)·y = c(t)` is divided, term by term, by `a(t)`. "
             "That gives `y′ + p(t)·y = q(t)` with `p = b/a` and `q = c/a`. The division "
             "is the only step, and it has to reach the right-hand side as well as the "
             "left. It is legitimate wherever `a(t)` is not zero, which is why "
             "`t·y′ − 2y = 0` is divided on the stretch where `t > 0` or the stretch "
             "where `t < 0`, and never across `t = 0`."),
            ("Linear is about y, and t is free",
             "The equation is linear when `y` and `y′` each appear on their own, to the "
             "first power, and are never multiplied together or put inside a function. "
             "The coefficients may be any functions of `t` at all. So `y′ = 2y + t²·y` "
             "is linear, because it is `y′ + (−2 − t²)·y = 0`, and `y′ + y² = t` is not, "
             "because of the `y²`. A term with no `y` in it is forcing, and it goes on "
             "the right."),
            ("Homogeneous means the right-hand side is zero",
             "When `q = 0` the equation is <em>homogeneous</em>: nothing pushes on it from "
             "outside, and the only thing acting on `y` is `p`. The word does not mean "
             "easy or constant. It names the equation whose solutions can be scaled, "
             "and the next lessons show that every forced equation carries its "
             "homogeneous partner inside it."),
        ],
        "read_title": "Reading an equation until you can see p and q",
        "read_intro": "The definition, the division, what the word linear rules out and what it allows, and the one property of the homogeneous case the rest of the course uses.",
        "body": [
            ("def", ("A first-order linear equation",
                     "An equation that can be written `a(t)·y′ + b(t)·y = c(t)` with "
                     "`a(t)` not identically zero. Its <strong>standard form</strong> is "
                     "`y′ + p(t)·y = q(t)`, where `p = b/a` and `q = c/a`.",
                     "It is <strong>homogeneous</strong> when `q` is zero, and "
                     "<strong>forced</strong> (or non-homogeneous) when it is not. The "
                     "function `q` is the <strong>forcing</strong>.")),
            ("p", "Standard form is a convention with a reason. The formulas on this course "
                  "&mdash; for a steady state, for an integrating factor, for a "
                  "particular solution &mdash; are all written for `y′` with coefficient 1, "
                  "and every one of them goes wrong by exactly the leftover factor if the "
                  "coefficient is something else. Dividing first is cheap. Dividing "
                  "afterwards, in the middle of a formula, is where the errors are."),
            ("math", [
                "2y′ + 6y = 4t",
                "divide every term by 2",
                "y′ + 3y = 2t",
                "p(t) = 3     q(t) = 2t     q is not 0, so forced",
            ]),
            ("h3", "What linear rules out, and what it allows"),
            ("p", "The unknown `y` and its rate `y′` each appear once, alone, to the first "
                  "power. That excludes `y²`, `y·y′`, `sin(y)` and `1/y`, and nothing "
                  "else. The factors multiplying `y` and `y′` are unrestricted: `t²`, "
                  "`1/t`, `sin(t)`, `e^t`. A term with no `y` in it is forcing and is "
                  "free to be anything."),
            ("math", [
                "y′ = 2y + t²·y        linear, p = −2 − t²",
                "y′ = t·y              linear, p = −t, homogeneous",
                "y′ + y² = t           not linear: y²",
                "y·y′ = 1              not linear: y times y′",
            ]),
            ("p", "Moving a term across the equals sign changes its sign, and that is the "
                  "commonest slip in reading `p`. The equation `y′ = 4 − 2y` has the "
                  "unknown on both sides; collecting it on the left gives `y′ + 2y = 4`, "
                  "so `p = 2` and `q = 4`, not `p = −2`. The sign matters later: a "
                  "positive constant `p` makes the solutions of the homogeneous equation "
                  "die away, and a negative one makes them grow."),
            ("thm", ("Scaling a homogeneous solution",
                     "If `y` solves `y′ + p(t)·y = 0`, then so does `C·y` for every "
                     "constant `C`.")),
            ("proof", ["The derivative of `C·y` is `C·y′`, because a constant factor "
                       "comes straight out of a derivative.",
                       "So `(C·y)′ + p·(C·y) = C·(y′ + p·y) = C·0 = 0`. Nothing about `p` "
                       "was used, only that `y` and `y′` each appear once and to the first "
                       "power. For `y′ = y²` the same step fails: `y = 1/(1 − t)` solves "
                       "it and `2·y` does not."]),
            ("example", ("A power of t in front of y′",
                         "Take `t·y′ − 2y = 0` and divide by `t`: `y′ − (2/t)·y = 0`, so "
                         "`p(t) = −2/t` and `q = 0`. It is homogeneous.",
                         "A solution is `y = t²`. Substitute: `t·(2t) − 2·t² = 0`. By the "
                         "scaling property `C·t²` is a solution for every `C`, and the lab "
                         "prints exactly that as the homogeneous solution.")),
            ("p", "The lab at the foot of the page does the division and prints several "
                  "things this lesson has not derived. Two of them matter now. "
                  "<strong>μ</strong>, the integrating factor, is the subject of the next "
                  "lesson but one; it is `e^(3t)` for `p = 3` and `1/t²` for `p = −2/t`. "
                  "<strong>y_h</strong> is the homogeneous solution, and across the three "
                  "presets it is always `C` divided by `μ`. The particular solution, the "
                  "steady state and the full solution are later lessons' business. Read "
                  "all of them as outputs for now; &ldquo;The Integrating Factor&rdquo; "
                  "explains the first two."),
            ("example", ("The equation that looks nonlinear and is not",
                         "In `y′ = 2y + t²·y` the `t²` sits beside the `y`. It is a "
                         "coefficient of `y`, not a power of `y`, so the equation is "
                         "`y′ + (−2 − t²)·y = 0` with `p(t) = −2 − t²`.",
                         "The lab refuses it, and the reason it gives is the lab's limit "
                         "and not a verdict on the equation: the lab solves a constant "
                         "`p` or one of the form `a/t`, and says that `p` is outside "
                         "them. A refusal from the lab never means the equation is not "
                         "linear unless it says so in those words.")),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "solve",
            "preset": "scaled",
            "presets": [
                {"id": "scaled", "label": "2y′ + 6y = 4t",
                 "equation": "2y' + 6y = 4t", "ic": None,
                 "expect": {"lfMu": "e^(3t)", "lfYh": "C·e^(−3t)"}},
                {"id": "power", "label": "t·y′ − 2y = 0",
                 "equation": "t y' - 2y = 0", "ic": None,
                 "expect": {"lfMu": "1/t²", "lfYh": "C·t²"}},
                {"id": "constant", "label": "y′ = 4 − 2y",
                 "equation": "y' = 4 - 2y", "ic": None,
                 "expect": {"lfMu": "e^(2t)", "lfYh": "C·e^(−2t)", "lfSteady": "2"}},
            ],
            "panel_title": "Type an equation and read its standard form",
            "panel_intro": (
                "The lab divides by the coefficient of y′, reports p and q in its status "
                "line, and prints the integrating factor and the homogeneous solution. "
                "Pick each preset, find p in the status line, and check it against the "
                "division you would do by hand. Then type your own: write the unknown "
                "with a prime, as y', and a product with a space or a star."),
        }),
        "steps_title": "Putting an equation in standard form",
        "steps_intro": "Collect, divide, read, then name it. The check at the end is the one that catches the equations that are not linear at all.",
        "steps": [
            ("Collect every term with y or y′ on the left",
             "Move the terms with no `y` in them to the right. Moving a term changes its "
             "sign, so `y′ = 4 − 2y` becomes `y′ + 2y = 4`, and the `+2` is the `p`."),
            ("Divide every term by the coefficient of y′",
             "Every term, including the right-hand side. If the coefficient is `2`, the "
             "`6y` becomes `3y` and the `4t` becomes `2t`. If it is `t`, you divide by "
             "`t` and say on which side of zero the equation lives."),
            ("Read p and q",
             "`p` is whatever now multiplies `y`; `q` is whatever is left on the right. "
             "Write both down as functions of `t`, with their signs."),
            ("Name the equation",
             "If `q` is zero it is homogeneous. If not it is forced, and the "
             "homogeneous equation with the same `p` is its partner &mdash; the one "
             "&ldquo;Homogeneous Plus Particular&rdquo; builds the solution from."),
            ("Test that it is linear at all",
             "If `y` or `y′` is squared, multiplied by the other, in a denominator or "
             "inside a sine, an exponential or a logarithm, it is not linear and none "
             "of this course applies. A `t` anywhere else does not matter."),
        ],
        "worked": {
            "title": "Dividing 2y′ + 6y = 4t, and reading the lab's answer",
            "intro": [
                "The first preset is `2y′ + 6y = 4t`. The coefficient of `y′` is `2`, so "
                "everything is divided by `2`.",
            ],
            "lines": [
                "2y′ + 6y = 4t",
                "y′ + 3y = 2t",
                "p(t) = 3      q(t) = 2t",
                "q is not zero, so forced",
                "homogeneous partner:  y′ + 3y = 0",
                "the lab:  μ = e^(3t),  y_h = C·e^(−3t)",
                "check:  y_h = C/μ,  and (e^(−3t))′ = −3·e^(−3t)",
            ],
            "after": [
                "The division changed `6y` to `3y` and `4t` to `2t` together. Leaving the "
                "right-hand side at `4t` would have described a different equation, and "
                "the lab's `μ` and `y_h` would not have noticed, because neither depends "
                "on `q` at all. That is the reason the status line reports `q` as well "
                "as `p`.",
                "For a rehearsal, read the other two presets before the lab does. The "
                "third, `y′ = 4 − 2y`, collects to `y′ + 2y = 4`; its `p` is the positive "
                "`2`, and the lab agrees with `μ = e^(2t)`. The second, `t·y′ − 2y = 0`, "
                "divides by `t` to give `p = −2/t`; predict the sign of the exponent in "
                "`μ` before you pick it, and then compare.",
            ],
        },
        "quiz_title": "Dividing, reading and refusing",
        "quiz": [
            {"q": "Put `3y′ − 6t·y = 9t` in standard form. What are `p` and `q`?",
             "a": ["`p = −6t` and `q = 9t`, because the equation is already in standard form",
                   "`p = 2t` and `q = 3t`, because the sign of the `y` term flips when it is divided",
                   "`p = −2t` and `q = 3t`, from dividing every term by 3",
                   "`p = −2t` and `q = 9t`, because only the left side needs dividing"],
             "c": 2,
             "why": "Dividing every term by 3 gives `y′ − 2t·y = 3t`, so `p = −2t` and "
                    "`q = 3t`. Leaving the equation as it stands keeps a 3 in front of "
                    "`y′`, which the standard form forbids. Dividing does not flip a "
                    "sign: `p` is `−2t` because the term on the left is `−6t·y`. "
                    "Dividing only the left side changes the equation, because "
                    "the right-hand side then no longer matches it."},
            {"q": "Which of these equations is linear?",
             "a": ["`y′ = t²·y − e^t`",
                   "`y′ + t·y² = 1`",
                   "`y′ = sin(y) + t`",
                   "`y·y′ = t`"],
             "c": 0,
             "why": "In the first, `y` appears once to the first power, multiplied by "
                    "`t²`, and `e^t` is forcing; it is `y′ − t²·y = −e^t`. The second "
                    "has `y²`, the third puts `y` inside `sin`, and the fourth "
                    "multiplies `y` by `y′`. The `t` in the first is irrelevant to "
                    "linearity, however awkward the function of `t` is."},
            {"q": "Which of these equations is homogeneous?",
             "a": ["`y′ = 4 − 2y`",
                   "`y′ + 2y = t`",
                   "`y′ + y = 1`",
                   "`2y′ = −t²·y`"],
             "c": 3,
             "why": "Homogeneous means `q = 0` once the terms with `y` are collected. "
                    "`2y′ = −t²·y` is `2y′ + t²·y = 0`, so it is. The first is "
                    "`y′ + 2y = 4` with `q = 4`, the second has `q = t`, and the third "
                    "has `q = 1`; each carries a term with no `y` in it."},
            {"q": "A student says `y′ = 2y + t²·y` is not linear because `t²` is not linear. What is the best reply?",
             "a": ["Correct, because a linear equation may only have constant coefficients",
                   "The equation is linear, because `t²` is a coefficient of `y`: it is `y′ + (−2 − t²)·y = 0`",
                   "The equation is linear but forced, because `t²` is forcing",
                   "The equation is linear only on the stretch where `t > 0`"],
             "c": 1,
             "why": "Linearity is a property of how `y` and `y′` appear. Here `y` appears "
                    "once, to the first power, with the coefficient `2 + t²`, so "
                    "`p = −2 − t²` and `q = 0`. Constant coefficients are a special case "
                    "that the lab handles, not a requirement. The `t²` multiplies `y`, so "
                    "it is not forcing and the equation is homogeneous. No division by "
                    "`t` is involved, so no stretch needs to be chosen."},
        ],
        "mistakes": [
            ("Calling y′ = 2y + t²·y nonlinear because of the t²",
             "The `t²` is a coefficient of `y`, and a coefficient may be any function of "
             "`t`. The equation is `y′ + (−2 − t²)·y = 0`: `p = −2 − t²`, `q = 0`, "
             "homogeneous. Scaling confirms it behaves linearly: if `y` is a solution then "
             "so is `5y`, since `(5y)′ − (2 + t²)·(5y) = 5·(y′ − (2 + t²)·y) = 0`. A "
             "nonlinear equation such as `y′ = y²` fails that test, and linearity in `y` "
             "is the only thing the word means."),
            ("Dividing the left side by the coefficient and leaving the right alone",
             "From `2y′ + 6y = 4t` the slip gives `y′ + 3y = 4t`. Test it with the "
             "particular solution the lab prints for the correct line, `(2/3)·t − 2/9`: "
             "substituted into the left side it gives "
             "`2/3 + 3·((2/3)·t − 2/9) = 2t`, which is `2t` and not `4t`. The slipped "
             "equation is a different equation, with a different forcing, and every "
             "solution of it would be wrong for the original."),
            ("Reading p with the sign it had before the term moved",
             "In `y′ = 4 − 2y` the `−2y` is on the right. Collecting it on the left "
             "gives `y′ + 2y = 4`, so `p = +2`. A reader who takes `p = −2` has the "
             "wrong sign in the exponent of every later formula: `μ = e^(−2t)` where "
             "the lab prints `e^(2t)`, and a solution that grows where the real one "
             "settles to `2`."),
        ],
        "standard": (
            "Finish when you can take any first-order linear equation, however its terms "
            "are arranged, and write it as y′ + p(t)·y = q(t).",
            "You should be able to collect the terms with the unknown on the left, divide "
            "every term by the coefficient of y′, name p and q with their signs, say "
            "whether the equation is homogeneous, and say why an equation with a power or "
            "product of y is not linear and an equation with a power of t is."),
        "note": 'The standard form is the form the integrating factor assumes, but the simplest equations do not need one. When <em>p</em> is a constant and <em>q</em> is a constant too, the equation has a constant solution, and everything else is a gap to it that shrinks or grows by one factor. That is the first thing to solve, in &ldquo;Constant Coefficients and the Steady State&rdquo;.',
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "constant-coefficients-and-the-steady-state",
        "title": "Constant Coefficients and the Steady State",
        "module": "The linear form",
        "one_line": "Solve y′ + a·y = b as a shifted exponential, name the steady state b/a, and set Euler's exact steps beside the closed form.",
        "summary": (
            "When both `a` and `b` are constants the equation has one constant "
            "solution, the steady state `b/a`, and every other solution is that "
            "constant plus a gap that is multiplied by the same factor in equal "
            "stretches of time. The gap shrinks to nothing without ever reaching "
            "it when `a` is positive and grows away when `a` is negative. Euler's "
            "method multiplies the gap by `1 − a·h` at each step, an exact "
            "geometric sequence beside a curve that is not."
        ),
        "key": [
            "y′ + a·y = b    steady state  y* = b/a",
            "y = b/a + (y₀ − b/a)·e^(−a·t)",
            "a > 0 pulls toward y*;  a < 0 pushes away",
            "Euler multiplies the gap by 1 − a·h",
            "the gap is never zero at a finite time",
        ],
        "key_label": "A constant plus a gap that decays",
        "concepts_intro": (
            "Three facts, each one line of algebra, and the second one is the "
            "solution. The third is what the lab shows beside it."
        ),
        "concepts": [
            ("The steady state is where the rate is zero",
             "From `y′ + a·y = b` the rate is `y′ = b − a·y`, and that is zero when "
             "`y = b/a`. So `y = b/a` is a constant solution, the only one when `a` "
             "is not zero. It is the equilibrium from Equilibria, Stability and "
             "Phase Lines, and here it can be written down without drawing a "
             "phase line."),
            ("The gap to it obeys y′ = −a·y",
             "Let `u = y − b/a`, the gap. Then `u′ = y′ = b − a·y = −a·(y − b/a) = −a·u`. "
             "The gap satisfies the equation from Separable Equations, Growth and "
             "Decay, so `u = u₀·e^(−a·t)`, and `y = b/a + (y₀ − b/a)·e^(−a·t)`. The "
             "starting value enters only as the starting gap."),
            ("Euler multiplies the gap by 1 − a·h, exactly",
             "One Euler step is `yₙ₊₁ = yₙ + h·(b − a·yₙ)`. Subtracting `b/a` from both "
             "sides gives `yₙ₊₁ − b/a = (1 − a·h)·(yₙ − b/a)`. So the gap after "
             "`n` steps is the starting gap times `(1 − a·h)ⁿ`, a geometric sequence "
             "of fractions, to be compared with the true factor `e^(−a·h)` per step, "
             "which is irrational."),
        ],
        "read_title": "A constant, a gap, and the factor that shrinks it",
        "read_intro": "The steady state, the shifted exponential and why it solves the equation, what never reaching the steady state means, the repelling case, and Euler's geometric sequence beside the closed form.",
        "body": [
            ("p", "Take `y′ + 2y = 6` with `y(0) = 0`. Before solving anything, ask where "
                  "the rate is zero: `y′ = 6 − 2y`, which is `0` at `y = 3`. If `y` ever "
                  "sat at `3` it would stay there for ever. The question the rest of the "
                  "lesson answers is what a solution does when it starts somewhere else."),
            ("def", ("Steady state",
                     "For `y′ + a·y = b` with `a ≠ 0`, the <strong>steady state</strong> is "
                     "the constant `y* = b/a`. It is the one constant solution, and it is "
                     "<strong>attracting</strong> when `a > 0`, <strong>repelling</strong> "
                     "when `a < 0`.")),
            ("thm", ("The shifted exponential",
                     "The solution of `y′ + a·y = b` with `y(0) = y₀` is "
                     "`y = b/a + (y₀ − b/a)·e^(−a·t)`.")),
            ("proof", ["Let `u = y − b/a`. Then `u′ = y′`, and from the equation "
                       "`y′ = b − a·y = −a·(y − b/a) = −a·u`.",
                       "So `u′ = −a·u`, which is the decay equation and has the solution "
                       "`u = u₀·e^(−a·t)`, a claim from Separable Equations, Growth and "
                       "Decay that is not reproved here. The starting gap is "
                       "`u₀ = y₀ − b/a`, and adding `b/a` back gives the formula."]),
            ("math", [
                "y′ + 2y = 6,   y(0) = 0",
                "steady state:  6 − 2y = 0,  so  y* = 3",
                "starting gap:  0 − 3 = −3",
                "y = 3 − 3·e^(−2t)",
            ]),
            ("h3", "The gap is never zero"),
            ("p", "The gap `3·e^(−2t)` is positive for every `t`, because an exponential "
                  "is never zero. So `y` comes closer to `3` and does not reach it at "
                  "any finite time, however long you wait. A reader who sees the curve "
                  "flatten in the drawing is looking at the gap getting smaller than a "
                  "pixel, which is not the same as the gap being zero. The claim the "
                  "lesson makes is about every finite `t`, and the formula proves it."),
            ("p", "Nor is the steady state the starting value. The solution starts at "
                  "`y(0) = 0` and the steady state is `3`; the starting value fixes the "
                  "gap and the steady state fixes where the gap is measured from. Start "
                  "at `5` instead and the gap is `+2`, giving `y = 3 + 2·e^(−2t)`, which "
                  "falls toward `3` from above and never crosses it, since the gap "
                  "never changes sign."),
            ("h3", "When a is negative the steady state repels"),
            ("p", "Take `y′ − y = 2`, so `a = −1`, `b = 2` and `y* = −2`. The solution "
                  "from `y(0) = 0` is `y = −2 + 2·e^t`: the gap is multiplied by `e^t`, "
                  "so it grows. The lab prints the steady state as `−2 (repelling)`. "
                  "Starting exactly at `−2` stays there; starting anywhere else, however "
                  "close, leaves."),
            ("h3", "Euler's steps, exactly, beside the closed form"),
            ("p", "Run Euler on `y′ + 2y = 6` from `y(0) = 0` with `h = 1/4`. The factor "
                  "`1 − a·h = 1 − 1/2 = 1/2` is an exact fraction, and so is every "
                  "value: `yₙ = 3 − 3·(1/2)ⁿ`. The closed form at the same times is "
                  "irrational, so the lab prints it rounded, to six figures, with "
                  "`≈`, in a separate column."),
            ("math", [
                "n     tₙ     yₙ (Euler, exact)    y(tₙ) (rounded)",
                "0     0      0                    0",
                "1     1/4    3/2                  ≈ 1.18041",
                "2     1/2    9/4                  ≈ 1.89636",
                "3     3/4    21/8                 ≈ 2.33061",
                "4     1      45/16                ≈ 2.59399",
            ]),
            ("p", "The fraction `45/16` is exactly `3 − 3/16`, and it is `2.8125`. The "
                  "true value is `3 − 3·e^(−2) ≈ 2.59399`, so Euler's polygon ends about "
                  "`0.218506` above the curve. Every fraction in the column is right; "
                  "none of them is the solution. Euler's gap shrinks by `1/2` per step, "
                  "and the true gap shrinks by `e^(−1/2) ≈ 0.606531` per step, which "
                  "is why the polygon runs ahead."),
            ("example", ("The same equation from above, and the repelling one",
                         "From `y(0) = 5` the gap is `+2` and Euler gives "
                         "`yₙ = 3 + 2·(1/2)ⁿ`, so `y₄ = 3 + 2/16 = 25/8`: above the steady "
                         "state at every step, as the true curve is.",
                         "For `y′ − y = 2` from `y(0) = 0` the factor is "
                         "`1 − (−1)·(1/4) = 5/4`, so `y₄ = −2 + 2·(5/4)⁴ = 369/128`. The "
                         "gap is multiplied by a number bigger than one, and the polygon "
                         "leaves the steady state exactly as the curve does.")),
            ("p", "One warning for later. The factor `1 − a·h` is positive and below "
                  "one for a small step, but it goes negative when `h > 1/a`, and its "
                  "size passes one when `h > 2/a`. At `h = 1/2` exactly, here, the "
                  "factor is `0`: the polygon lands on `3` after one step and stays "
                  "there, which the curve never does. A polygon that follows the curve "
                  "for `h = 1/4` can run away for a larger step on the same equation. "
                  "&ldquo;Stiffness: When the Step Is Too Big&rdquo; takes that up."),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "steps",
            "preset": "three",
            "presets": [
                {"id": "three", "label": "y′ + 2y = 6, y(0) = 0",
                 "equation": "y' + 2y = 6", "ic": [0, 0], "h": "1/4", "n": 4,
                 "expect": {"lfSteady": "3", "lfSolution": "y = 3 − 3·e^(−2t)", "lfLast": "45/16"}},
                {"id": "from-above", "label": "y′ + 2y = 6, y(0) = 5",
                 "equation": "y' + 2y = 6", "ic": [0, 5], "h": "1/4", "n": 4,
                 "expect": {"lfSteady": "3", "lfSolution": "y = 3 + 2·e^(−2t)", "lfLast": "25/8"}},
                {"id": "negative", "label": "y′ − y = 2, y(0) = 0",
                 "equation": "y' - y = 2", "ic": [0, 0], "h": "1/4", "n": 4,
                 "expect": {"lfSteady": "−2 (repelling)", "lfSolution": "y = −2 + 2·e^t", "lfLast": "369/128"}},
            ],
            "panel_title": "Exact Euler steps beside the shifted exponential",
            "panel_intro": (
                "The table lists Euler's values as exact fractions beside the closed "
                "form rounded to six figures. The steady-state tile is exact, the "
                "solution tile is the closed form, and the last-value tile is the "
                "final Euler fraction. Try the three presets, then change the step to "
                "1/2 and watch the factor 1 − a·h change."),
        }),
        "steps_title": "Solving y′ + a·y = b from any start",
        "steps_intro": "Find the constant, measure the gap, let the gap decay or grow, then check. Euler is one more line.",
        "steps": [
            ("Find the steady state",
             "Set the rate to zero: `b − a·y = 0`, so `y* = b/a`. Say whether it attracts "
             "(`a > 0`) or repels (`a < 0`)."),
            ("Write the starting gap",
             "`y₀ − y*`, with its sign. The sign says which side of the steady state the "
             "solution lives on for ever."),
            ("Put the gap on an exponential",
             "`y = y* + (y₀ − y*)·e^(−a·t)`. The exponent is `−a·t`: negative for an "
             "attracting steady state, positive for a repelling one."),
            ("Check the start and the equation",
             "At `t = 0` the exponential is `1`, so `y = y* + (y₀ − y*) = y₀`. Then "
             "substitute into `y′ + a·y` and read `b`."),
            ("Run Euler by one factor",
             "The gap after `n` steps is `(y₀ − y*)·(1 − a·h)ⁿ`. Add `y*` and the whole "
             "column follows, as exact fractions."),
        ],
        "worked": {
            "title": "y′ + 2y = 6 from zero: the closed form, then four steps",
            "intro": [
                "The equation is `y′ + 2y = 6` with `y(0) = 0` and step `h = 1/4`. The "
                "steady state comes first, then the gap, then the formula, then Euler "
                "as one factor.",
            ],
            "lines": [
                "steady state:  6 − 2y = 0,  so  y* = 3",
                "gap at the start:  0 − 3 = −3",
                "y = 3 − 3·e^(−2t)",
                "check at t = 0:  3 − 3 = 0, matches y(0) = 0",
                "Euler factor:  1 − 2·(1/4) = 1/2",
                "yₙ = 3 − 3·(1/2)ⁿ",
                "y₄ = 3 − 3/16 = 45/16 = 2.8125",
                "y(1) = 3 − 3·e^(−2) ≈ 2.59399",
            ],
            "after": [
                "The two numbers at the foot are different quantities and the lab prints "
                "both: `45/16` is exact arithmetic on Euler's approximation, and "
                "`2.59399` is a rounded value of the curve. The distance between them, "
                "about `0.218506`, is the error of this method at this step, and it is "
                "the only part of the table that is not exact. Halve the step and it "
                "falls, as Differential Equations and Euler's Method measured.",
                "For a rehearsal, change the start to `y(0) = 5` without running the "
                "lab. The steady state is unchanged, the gap is now `+2`, and the "
                "factor is still `1/2`. Predict `y₄` as a fraction, then pick the "
                "second preset and compare.",
            ],
        },
        "quiz_title": "Steady states, gaps and factors",
        "quiz": [
            {"q": "For `y′ + 4y = 20` with `y(0) = 0`, what does the solution do?",
             "a": ["It approaches `20`, the number on the right-hand side",
                   "It approaches `5` and is equal to `5` at no finite time",
                   "It reaches `5` at the finite time `t = 5/4`",
                   "It approaches `1/5`, the ratio `4/20`"],
             "c": 1,
             "why": "The steady state is `b/a = 20/4 = 5`, and the gap is `5·e^(−4t)`, "
                    "which is positive for every `t`. The right-hand side `20` is not "
                    "the steady state: `y = 20` gives `y′ + 4y = 80`. The ratio is "
                    "inverted in the last choice. No finite time makes an exponential "
                    "zero, so there is no `t` at which `y = 5`."},
            {"q": "For `y′ + 3y = 12` with `y(0) = 10`, which statement is true?",
             "a": ["`y` decreases past `4`, crosses it, and returns",
                   "`y` increases away from `4`",
                   "`y` decreases toward `4` and stays above it",
                   "`y` stays at `10` because `10` is the starting value"],
             "c": 2,
             "why": "The steady state is `12/3 = 4`, the gap starts at `+6`, and the gap "
                    "is `6·e^(−3t)`, which never changes sign, so `y = 4 + 6·e^(−3t)` "
                    "stays above `4` and decreases. A solution of this equation "
                    "cannot cross its steady state. It does not grow, since `a = 3` is "
                    "positive. And `y′ = 12 − 30 = −18` at the start, so it is moving."},
            {"q": "Euler's method with `h = 1/10` is applied to `y′ + 2y = 6` from `y(0) = 0`. By what factor is the gap to `3` multiplied at each step?",
             "a": ["`1/5`",
                   "`6/5`",
                   "`e^(−1/5)`",
                   "`4/5`"],
             "c": 3,
             "why": "The Euler factor is `1 − a·h = 1 − 2/10 = 4/5`, an exact fraction. "
                    "The factor `e^(−1/5)` is what the true solution multiplies the gap "
                    "by over the same time, and it is irrational, so it is not Euler's. "
                    "`1/5` is `h·a` alone, and `6/5` has the wrong sign inside the "
                    "bracket."},
            {"q": "In `y′ − 3y = −6` the solution starts at `y(0) = 2.001`. What does it do?",
             "a": ["It decays toward `2`",
                   "It oscillates around `2`",
                   "It moves away from `2`, upward",
                   "It stays at `2.001`"],
             "c": 2,
             "why": "Here `a = −3` and `b = −6`, so the steady state is `b/a = 2` and it "
                    "repels. The gap `0.001` is multiplied by `e^(3t)`, so the solution "
                    "grows away from `2` on the side it started. A solution that "
                    "starts exactly at `2` would stay, but this one does not. A "
                    "first-order linear equation does not oscillate, and `y′` at the start "
                    "is `−6 + 3·2.001 = 0.003`, not zero."},
        ],
        "mistakes": [
            ("Thinking the steady state is the starting value, or that it is reached",
             "The solution of `y′ + 2y = 6` from `y(0) = 0` starts at `0` and approaches "
             "`3`; the starting value fixes the gap, not the steady state. The gap "
             "`3·e^(−2t)` is positive at every `t`, so `y` is below `3` for ever, and "
             "Euler's gap `3·(1/2)ⁿ` is positive at every step. A curve that looks flat "
             "has a gap smaller than the drawing can show, and the gap is still there."),
            ("Reading the steady state off the right-hand side",
             "In `y′ + 2y = 6` the number `6` is the forcing, and `y = 6` gives "
             "`0 + 12 = 12`, not `6`. The steady state is `b/a = 3`, the value that makes "
             "`b − a·y` zero. The right-hand side and the steady state are equal only "
             "when `a = 1`."),
            ("Taking Euler's final fraction for the value of the solution",
             "At `t = 1` the lab prints `45/16`, which is `2.8125`, and the true "
             "value is `≈ 2.59399`. The fraction is correct arithmetic on a polygon whose "
             "gap shrinks by `1/2` per step; the curve's gap shrinks by "
             "`e^(−1/2) ≈ 0.606531`. The difference is the error of the method at this "
             "step, not a slip in the arithmetic."),
        ],
        "standard": (
            "Finish when you can solve y′ + a·y = b from any starting value, name the steady state and say whether it attracts, and compute Euler's step factor.",
            "You should be able to find b/a, write the starting gap with its sign, put the "
            "gap on e^(−a·t), check the result at t = 0 and by substitution, say why the "
            "solution never reaches the steady state in finite time, and predict "
            "Euler's value after n steps as an exact fraction from the factor "
            "1 − a·h."),
        "note": 'A constant <em>a</em> gave the exponential `e^(−a·t)` for free. When <em>p</em> depends on <em>t</em>, or when the forcing is not a constant, the gap is no longer a pure exponential. One idea handles every such case, and it is the product rule read backwards: &ldquo;The Integrating Factor&rdquo;.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "the-integrating-factor",
        "title": "The Integrating Factor",
        "module": "Integrating factors",
        "one_line": "Construct μ = e^(∫p dt), show that (μ·y)′ = μ·q is the product rule read backwards, and solve a case with μ = tᵃ entirely in fractions.",
        "summary": (
            "The left side of `y′ + p·y = q` is almost the derivative of something and "
            "not quite. Multiply by the function `μ` whose rate is `p` times itself and "
            "it becomes exactly `(μ·y)′`, the product rule read backwards, so the "
            "equation turns into `(μ·y)′ = μ·q` and can be integrated. When "
            "`p = a/t` the factor is the power `tᵃ`, and the whole solution is a "
            "calculation in fractions."
        ),
        "key": [
            "μ′ = p·μ,  so  μ = e^(∫p dt)",
            "(μ·y)′ = μ·y′ + μ′·y = μ·(y′ + p·y)",
            "y′ + p·y = q   becomes   (μ·y)′ = μ·q",
            "p = a/t:  μ = tᵃ, and every step is exact",
            "μ is e^(∫p dt), never e^(p)",
        ],
        "key_label": "Multiply by a function that makes the left side a derivative",
        "concepts_intro": (
            "Three ideas, in the order they are used: what the factor must do, what it "
            "therefore is, and what the equation becomes once it is applied."
        ),
        "concepts": [
            ("The product rule read backwards",
             "The product rule says `(μ·y)′ = μ·y′ + μ′·y`. The left side of the "
             "equation is `y′ + p·y`. Multiply it by `μ` and it is `μ·y′ + p·μ·y`. These "
             "agree exactly when `μ′ = p·μ`, so the factor is whichever function "
             "satisfies that one condition."),
            ("μ is the function whose rate is p times itself",
             "For a constant `p = a` that function is `e^(a·t)`. For `p = a/t` it is "
             "`tᵃ`, because the power rule gives `(tᵃ)′ = a·t^(a − 1) = (a/t)·tᵃ`. In "
             "general it is `e^(∫p dt)`, where `∫p dt` is one antiderivative of `p`; "
             "the exponent is the antiderivative of `p`, not `p` itself."),
            ("After multiplying, the left side is a derivative",
             "The equation becomes `(μ·y)′ = μ·q`. Integrate the right side and add "
             "a constant: `μ·y = ∫μ·q dt + C`. Then divide by `μ`, including the "
             "constant, and fit `C` to the starting value last."),
        ],
        "read_title": "Why one multiplication makes the equation integrable",
        "read_intro": "The condition on the factor, the check that proves it works, the two families of factor the lab handles, a full solution in fractions, and why the constant in the exponent does not matter.",
        "body": [
            ("p", "As it stands the left side `y′ + p·y` is not the derivative of anything "
                  "you can write down. `y′` alone is the derivative of `y`, and the "
                  "extra term `p·y` spoils it. A product `μ·y` has the derivative "
                  "`μ·y′ + μ′·y`, which has the same two-term shape; the only question is "
                  "whether a `μ` exists that makes the second term `p·μ·y`."),
            ("thm", ("The integrating factor",
                     "If `μ′ = p·μ`, then `(μ·y)′ = μ·(y′ + p·y)` for every "
                     "differentiable `y`. So `y′ + p·y = q` implies `(μ·y)′ = μ·q`.")),
            ("proof", ["The product rule, verified exactly on polynomials in Rates of "
                       "Change and the Derivative, gives `(μ·y)′ = μ·y′ + μ′·y`.",
                       "Replace `μ′` by `p·μ`: `μ·y′ + p·μ·y = μ·(y′ + p·y)`. If "
                       "`y′ + p·y = q` the right side is `μ·q`. Only the product rule and "
                       "the one condition on `μ` were used."]),
            ("p", "Two families of `p` need nothing else. For a constant `p = a`, "
                  "`μ = e^(a·t)`, since the rate of `e^(a·t)` is `a` times itself, a claim "
                  "from the earlier courses. For `p = a/t` with a whole number `a`, "
                  "`μ = tᵃ`, and the check is the power rule alone. It is exact, and the "
                  "lab prints the result without a logarithm."),
            ("math", [
                "p = 2/t,   μ = t²",
                "μ′ = 2t",
                "p·μ = (2/t)·t² = 2t",
                "equal, so μ′ = p·μ",
            ]),
            ("h3", "Why the exponent is the antiderivative of p"),
            ("p", "For the general formula `μ = e^(∫p dt)` the chain rule, verified on "
                  "polynomials in Rates of Change and the Derivative and applied here to "
                  "the exponential as a stated claim, gives "
                  "`μ′ = (∫p dt)′·e^(∫p dt) = p·μ`, which is the condition. The "
                  "exponent has to be an antiderivative of `p`. Using `p` itself fails "
                  "at once: for the constant `p = 3`, `e^p = e³` is a constant, its "
                  "rate is `0`, and `p·μ = 3·e³` is not."),
            ("p", "Which antiderivative does not matter. A different constant added to "
                  "`∫p dt` multiplies `μ` by a constant factor, such as `5` or `e⁷`, and "
                  "that factor multiplies both sides of the equation and cancels. "
                  "`μ = 5t²` works as well as `μ = t²`, and the final `y` is the same."),
            ("example", ("A case with an exponential factor and a forcing",
                         "Take `y′ + 2y = e^t`. Then `μ = e^(2t)`, and "
                         "`(e^(2t)·y)′ = e^(2t)·e^t = e^(3t)`.",
                         "Integrate: `e^(2t)·y = (1/3)·e^(3t) + C`, so "
                         "`y = (1/3)·e^t + C·e^(−2t)`. The lab prints exactly this, with "
                         "`C` left free because no starting value was given.")),
            ("p", "For `p = a/t` the same steps stay in fractions. With "
                  "`y′ + (2/t)·y = t²` and `y(1) = 1`, the factor is `t²`, "
                  "`(t²·y)′ = t⁴`, `t²·y = t⁵/5 + C`, and `y = t³/5 + C/t²`. Substituting "
                  "to check: `y′ = 3t²/5 − (2C)/t³` and `(2/t)·y = 2t²/5 + (2C)/t³`, "
                  "which add to `t²` for every `C`."),
            ("math", [
                "y′ + (2/t)·y = t²,    y(1) = 1",
                "μ = t²",
                "(t²·y)′ = t⁴",
                "t²·y = t⁵/5 + C",
                "y = t³/5 + C/t²",
                "y(1) = 1/5 + C = 1,  so  C = 4/5",
            ]),
            ("p", "The lab limits itself to the families above, and says so when it "
                  "refuses. It takes a constant `p`, or `a/t` with `a` a whole number from "
                  "`−4` to `4`; it will not integrate `tᵃ·q` when that integral has a "
                  "`ln t` in it; and for `p = a/t` it asks for a starting time other "
                  "than `0`, since the equation is not defined at `t = 0`. These are "
                  "limits of the lab, and the integrating factor itself has no such "
                  "limit."),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "solve",
            "preset": "t-squared",
            "presets": [
                {"id": "t-squared", "label": "y′ + (2/t)·y = t², y(1) = 1",
                 "equation": "y' + (2/t) y = t^2", "ic": [1, 1],
                 "expect": {"lfMu": "t²", "lfSolution": "y = t³/5 + (4/5)/t²", "lfC": "4/5"}},
                {"id": "exp", "label": "y′ + 2y = e^t",
                 "equation": "y' + 2y = e^t", "ic": None,
                 "expect": {"lfMu": "e^(2t)", "lfSolution": "y = (1/3)·e^t + C·e^(−2t)", "lfC": "—"}},
                {"id": "t-one", "label": "y′ + y/t = 1, y(1) = 2",
                 "equation": "y' + y/t = 1", "ic": [1, 2],
                 "expect": {"lfMu": "t", "lfSolution": "y = t/2 + (3/2)/t", "lfC": "3/2"}},
            ],
            "panel_title": "The factor, the solution, and the constant",
            "panel_intro": (
                "The first tile is the integrating factor μ; the solution tile is the "
                "closed form, with C fitted when an initial value is given and left "
                "free when not. For each preset, multiply by μ by hand and check that "
                "the left side is the derivative of μ·y before you read the answer."),
        }),
        "steps_title": "Solving a first-order linear equation with μ",
        "steps_intro": "Five moves: standard form, factor, multiply, integrate, divide. The check is a substitution, and it is cheap.",
        "steps": [
            ("Put it in standard form and read p",
             "`y′ + p(t)·y = q(t)`, with the signs. Everything else depends on `p` "
             "being right."),
            ("Find μ and test it",
             "Find a function with `μ′ = p·μ`: `e^(a·t)` for `p = a`, `tᵃ` for `p = a/t`. "
             "Differentiate it and compare with `p·μ` before you use it."),
            ("Multiply both sides and recognise the left",
             "Multiply the whole equation by `μ`, left and right. The left side is now "
             "`(μ·y)′`, so write it that way."),
            ("Integrate the right side and add C",
             "`μ·y = ∫μ·q dt + C`. If the integral is a power of `t`, the power rule "
             "gives it in fractions."),
            ("Divide by μ, then fit C",
             "`y = (∫μ·q dt + C)/μ`, with `C` divided as well. Put the starting value "
             "in last, solve for `C`, and check by substituting into the original."),
        ],
        "worked": {
            "title": "y′ + (2/t)·y = t² from y(1) = 1, every step a fraction",
            "intro": [
                "The equation is already in standard form, with `p = 2/t` and `q = t²`. "
                "The factor is a power, so nothing leaves the rational numbers.",
            ],
            "lines": [
                "p = 2/t, so  μ = t²   (μ′ = 2t = (2/t)·t²)",
                "multiply:  t²·y′ + 2t·y = t⁴",
                "left side is (t²·y)′,  so  (t²·y)′ = t⁴",
                "integrate:  t²·y = t⁵/5 + C",
                "divide:  y = t³/5 + C/t²",
                "y(1) = 1:  1/5 + C = 1,  so  C = 4/5",
                "y = t³/5 + (4/5)/t²",
            ],
            "after": [
                "Every line is an exact fraction, and the answer is checked by "
                "substitution: `y′ = 3t²/5 − (8/5)/t³`, `(2/t)·y = 2t²/5 + (8/5)/t³`, and "
                "the sum is `t²`. At `t = 1` the solution is `1/5 + 4/5 = 1`. Nothing "
                "here was rounded, because `μ` was a power of `t` and the integral of a "
                "power is a power.",
                "For a rehearsal, work the third preset, `y′ + y/t = 1` with `y(1) = 2`, "
                "before opening it. The factor is `t`; the integrated line is "
                "`t·y = t²/2 + C`; the starting value fixes `C`. Then compare the "
                "constant with the lab's.",
            ],
        },
        "quiz_title": "Factors, products and constants",
        "quiz": [
            {"q": "For `y′ + (2/t)·y = t²` a student uses `μ = e^(2/t)`. What goes wrong?",
             "a": ["Nothing: any function built from `p` works as an integrating factor",
                   "The factor is right, but the integral of `μ·q` must be added",
                   "`μ′` is `−(2/t²)·e^(2/t)`, not `(2/t)·μ`, so the left side is not `(μ·y)′`",
                   "The factor is right, but only after dividing both sides by `t`"],
             "c": 2,
             "why": "The factor must satisfy `μ′ = p·μ`. For `μ = e^(2/t)` the chain rule "
                    "gives `μ′ = −(2/t²)·e^(2/t)`, which is not `(2/t)·μ`: the "
                    "exponent has to be an antiderivative of `p`, which is `2·ln t` and "
                    "gives `t²`. A function of `p` is not enough, and neither added "
                    "integrals nor extra division repair a factor with the wrong rate."},
            {"q": "Which integrating factor goes with `y′ + (3/t)·y = 1`?",
             "a": ["`t³`",
                   "`e^(3/t)`",
                   "`3t`",
                   "`e^(3t)`"],
             "c": 0,
             "why": "For `p = a/t` the factor is `tᵃ`; the check is `(t³)′ = 3t² = (3/t)·t³`. "
                    "`e^(3/t)` uses `p` in the exponent and `e^(3t)` is the factor for "
                    "the constant `p = 3`. `3t` has rate `3`, but `p·μ = (3/t)·3t = 9`."},
            {"q": "For `y′ + y/t = 1` the factor is `μ = t`. What is `t·y`?",
             "a": ["`t + C`",
                   "`t² + C`",
                   "`1/t + C`",
                   "`t²/2 + C`"],
             "c": 3,
             "why": "Multiplying gives `(t·y)′ = t·1 = t`, and the integral of `t` is "
                    "`t²/2`. `t + C` forgets to multiply the right side by `μ`. "
                    "`t² + C` drops the factor `1/2` from the power rule. "
                    "`1/t + C` integrates `1/μ`."},
            {"q": "One student takes `μ = e^(2t)` for `y′ + 2y = e^t`, another takes `μ = e^(2t + 7)`. Which statement is right?",
             "a": ["Only `e^(2t)`, because the constant of integration must be zero",
                   "Both work: the extra factor `e⁷` multiplies both sides and cancels",
                   "Only `e^(2t + 7)`, because the constant of integration must be kept",
                   "Neither works, because `μ` is found by differentiating, not integrating"],
             "c": 1,
             "why": "Any antiderivative of `p` gives a valid factor, since the factor "
                    "only has to satisfy `μ′ = p·μ`, and `e^(2t + 7)` does. The extra "
                    "`e⁷` is a constant that multiplies both sides of the equation, so the "
                    "final `y` is the same. The constant is neither forbidden nor "
                    "required, and `μ` is built by integrating `p`."},
        ],
        "mistakes": [
            ("Putting p itself in the exponent instead of its antiderivative",
             "For `y′ + (2/t)·y = t²` the wrong factor `e^(2/t)` has the rate "
             "`−(2/t²)·e^(2/t)`, and `p·μ` is `(2/t)·e^(2/t)`; they differ, so "
             "`μ·y′ + p·μ·y` is not `(μ·y)′`. With `p = 3` the wrong factor is the constant "
             "`e³`, whose rate is `0` and not `3·e³`. The exponent is an "
             "antiderivative of `p`: `2·ln t` for `2/t`, which is `t²`, and `3t` for `3`."),
            ("Multiplying only the left side by μ",
             "From `(t²·y)′ = t²` the slip gives `t²·y = t³/3 + C` and `y = t/3 + C/t²`. "
             "Substitute into the original: `y′ = 1/3 − 2C/t³` and "
             "`(2/t)·y = 2/3 + 2C/t³`, which add to `1`, not `t²`. The factor multiplies "
             "the right side too, and the right side is `μ·q = t⁴`."),
            ("Adding C before dividing by μ",
             "The step gives `y = (∫μ·q dt)/μ + C`, here `y = t³/5 + C`. Substituting "
             "gives `y′ + (2/t)·y = 3t²/5 + 2t²/5 + 2C/t = t² + 2C/t`, which is `t²` only "
             "for `C = 0`. The constant belongs to the integral and is divided "
             "with it: `y = t³/5 + C/t²`."),
        ],
        "standard": (
            "Finish when you can solve y′ + p(t)·y = q(t) for p constant or a/t by building μ, multiplying, integrating and fitting the constant, and can say why the left side becomes a derivative.",
            "You should be able to find a function with μ′ = p·μ and check it by "
            "differentiating, write the equation as (μ·y)′ = μ·q, integrate the right side "
            "with a constant, divide the constant by μ as well, fit it to a starting value "
            "last, and explain why e^(p) is not a factor."),
        "note": 'The solution always came out as one piece with a free constant, and in the exponential case the piece with the constant was `C·e^(−2t)`, the same as the homogeneous solution. That is not an accident, and it gives a second way to solve these equations which needs no integrating factor at all: &ldquo;Homogeneous Plus Particular&rdquo;.',
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "homogeneous-plus-particular",
        "title": "Homogeneous Plus Particular",
        "module": "Integrating factors",
        "one_line": "Split a solution into the homogeneous part and one particular part, explain why adding them is allowed, and fit the constant last.",
        "summary": (
            "Every solution of `y′ + p·y = q` is one particular solution `y_p` plus a "
            "solution `y_h` of the homogeneous equation `y′ + p·y = 0`. Adding is "
            "allowed because the left side is linear in `y`, so the sum gives "
            "`q + 0`; and nothing is missed, because the difference of two solutions "
            "solves the homogeneous equation. The constant in `y_h` is fitted to the "
            "starting value after the two parts are added, never before."
        ),
        "key": [
            "y = y_p + y_h",
            "y_h:  y′ + p·y = 0,  so  y_h = C/μ",
            "y_p:  any one solution of y′ + p·y = q",
            "sum gives  y′ + p·y = q + 0 = q",
            "fit C last:  y(t₀) = y_p(t₀) + C/μ(t₀)",
        ],
        "key_label": "Two simpler problems, added, then one constant",
        "concepts_intro": (
            "Three ideas: the two equations, why adding their solutions is legitimate, and "
            "why one particular solution is enough."
        ),
        "concepts": [
            ("Two equations, one for each part",
             "The <em>homogeneous</em> solution `y_h` solves `y′ + p·y = 0`, the "
             "equation with the forcing removed, and carries the constant `C`. The "
             "<em>particular</em> solution `y_p` solves the forced equation "
             "`y′ + p·y = q` and carries no constant. Any one particular solution "
             "will do; the lessons that follow find them by guessing a form and "
             "matching coefficients."),
            ("Adding is allowed because the equation is linear",
             "Substitute `y_p + y_h`: the left side is "
             "`(y_p + y_h)′ + p·(y_p + y_h) = (y_p′ + p·y_p) + (y_h′ + p·y_h) = q + 0`. "
             "That works for any `p` and any `q`, and it fails for nonlinear equations: "
             "the sum of two solutions of `y′ = y²` is not a solution."),
            ("One particular solution is enough",
             "If `y` is any solution at all, then `y − y_p` solves the homogeneous "
             "equation, because `q − q = 0`. So `y − y_p = C/μ` for some `C`, and every "
             "solution has the form `y_p + C/μ`. A different `y_p` changes only the "
             "constant that the starting value will fix."),
        ],
        "read_title": "Why the general solution splits, and how to fit it",
        "read_intro": "The two parts, the proof that their sum solves the equation and that nothing else does, how a particular solution is found by a guess, and the order in which the constant is fitted.",
        "body": [
            ("def", ("Homogeneous and particular solutions",
                     "For `y′ + p(t)·y = q(t)`, a <strong>particular solution</strong> "
                     "`y_p` is any one function that satisfies it, and a "
                     "<strong>homogeneous solution</strong> `y_h` is any function that "
                     "satisfies `y′ + p(t)·y = 0`.",
                     "The <strong>general solution</strong> is `y = y_p + y_h`, where "
                     "`y_h = C/μ` carries one arbitrary constant.")),
            ("thm", ("Superposition for the forced equation",
                     "If `y_p` solves `y′ + p·y = q` and `y_h` solves "
                     "`y′ + p·y = 0`, then `y_p + y_h` solves `y′ + p·y = q`. And "
                     "if `y` is any solution, then `y − y_p` solves the "
                     "homogeneous equation.")),
            ("proof", ["The derivative of a sum is the sum of the derivatives, so "
                       "`(y_p + y_h)′ + p·(y_p + y_h) = (y_p′ + p·y_p) + (y_h′ + p·y_h) = q + 0`.",
                       "For the second claim, `(y − y_p)′ + p·(y − y_p) = (y′ + p·y) − "
                       "(y_p′ + p·y_p) = q − q = 0`. Both steps use only that `y` and `y′` "
                       "appear once and to the first power."]),
            ("p", "Take `y′ + 3y = 2t`. The homogeneous equation is `y′ + 3y = 0`, with "
                  "factor `μ = e^(3t)` from the last lesson, so `y_h = C·e^(−3t)`. A "
                  "particular solution has to be found, and a guess whose form is "
                  "borrowed from the forcing is the standard way."),
            ("h3", "Finding y_p by a guess with unknown constants"),
            ("p", "The forcing `2t` is a polynomial of degree one, so try a polynomial of "
                  "degree one, `y_p = A·t + B`. Substituting: `A + 3·(A·t + B) = 2t`, which "
                  "is `3A·t + (A + 3B) = 2t`. Matching the coefficients of `t` and of "
                  "`1` gives `3A = 2` and `A + 3B = 0`, so `A = 2/3` and `B = −2/9`."),
            ("math", [
                "y_p = (2/3)·t − 2/9",
                "y_p′ = 2/3",
                "3·y_p = 2t − 2/3",
                "y_p′ + 3·y_p = 2t",
            ]),
            ("p", "The check is the last line, and it is exact. The guess carried a "
                  "constant term `B` even though the forcing `2t` has none, for the "
                  "reason the next lesson makes into a rule: with `A·t` alone the "
                  "equations would be `3A = 2` and `A = 0`, which no `A` satisfies. "
                  "The derivative of `A·t` is a constant, and something in the guess "
                  "has to cancel it. &ldquo;Polynomial Forcing and Undetermined "
                  "Coefficients&rdquo; turns the guess into a method."),
            ("example", ("A constant forcing: the steady state is the particular solution",
                         "For `y′ + 2y = 6` try a constant, `y_p = A`. Then `0 + 2A = 6` "
                         "gives `A = 3`, which is the steady state from "
                         "&ldquo;Constant Coefficients and the Steady State&rdquo;.",
                         "The gap `(y₀ − 3)·e^(−2t)` found there is exactly the "
                         "homogeneous part, `C·e^(−2t)` with `C = y₀ − 3`. That lesson was "
                         "this one for a constant `q`.")),
            ("h3", "The constant is fitted last"),
            ("p", "Add the two parts first: `y = (2/3)·t − 2/9 + C·e^(−3t)`. Only then "
                  "put in the starting value, because the starting value is a "
                  "statement about the whole solution. With `y(0) = 1`: "
                  "`−2/9 + C = 1`, so `C = 11/9`. The `−2/9` is the value of the "
                  "particular part at `t = 0`, and it has to be subtracted before "
                  "`C` is read off."),
            ("math", [
                "y = (2/3)·t − 2/9 + C·e^(−3t)",
                "y(0) = −2/9 + C = 1",
                "C = 1 + 2/9 = 11/9",
                "y = (2/3)·t − 2/9 + (11/9)·e^(−3t)",
            ]),
            ("example", ("An exponential forcing",
                         "For `y′ + 2y = e^t` with `y(0) = 0` try `y_p = A·e^t`. Then "
                         "`A·e^t + 2A·e^t = e^t` gives `3A = 1`, so `y_p = (1/3)·e^t`.",
                         "The solution is `(1/3)·e^t + C·e^(−2t)`, and `y(0) = 1/3 + C = 0` gives "
                         "`C = −1/3`. The lab shows the three curves in its parts view: "
                         "the homogeneous part, the particular part, and their sum.")),
            ("p", "Because the two parts are separate, the lab can draw them separately. "
                  "In the parts view the homogeneous curve decays on its own, the "
                  "particular curve is the forced response the starting value "
                  "cannot change, and the solution is their sum. A different particular "
                  "solution would give a different split and the same sum."),
        ],
        "lab": ("dekit", {
            "mode": "linear1",
            "view": "parts",
            "preset": "ramp",
            "presets": [
                {"id": "ramp", "label": "y′ + 3y = 2t, y(0) = 1",
                 "equation": "y' + 3y = 2t", "ic": [0, 1],
                 "expect": {"lfYh": "C·e^(−3t)", "lfYp": "(2/3)·t − 2/9", "lfC": "11/9"}},
                {"id": "constant", "label": "y′ + 2y = 6",
                 "equation": "y' + 2y = 6", "ic": None,
                 "expect": {"lfYh": "C·e^(−2t)", "lfYp": "3", "lfSteady": "3"}},
                {"id": "exp", "label": "y′ + 2y = e^t, y(0) = 0",
                 "equation": "y' + 2y = e^t", "ic": [0, 0],
                 "expect": {"lfYh": "C·e^(−2t)", "lfYp": "(1/3)·e^t", "lfC": "−1/3"}},
            ],
            "panel_title": "Split the solution into its two parts",
            "panel_intro": (
                "Three tiles name the parts: the homogeneous solution, the particular "
                "solution and the fitted constant. The drawing shows the homogeneous "
                "part, the particular part and their sum. Change the initial value and "
                "watch which tile moves and which does not."),
        }),
        "steps_title": "Solving a forced equation in two parts",
        "steps_intro": "Solve the easy equation, find one solution of the forced one, add, and fit the constant last.",
        "steps": [
            ("Solve the homogeneous equation",
             "Set `q = 0` and use `y_h = C/μ`. For `p = 3` that is `C·e^(−3t)`."),
            ("Find one particular solution",
             "Guess a form with the same shape as `q`, with unknown constants, substitute, "
             "and match coefficients. Any single solution will do."),
            ("Check the particular solution",
             "Substitute `y_p` alone into `y′ + p·y` and read `q`. If it does not give "
             "`q`, the guess was wrong, however neat the constants look."),
            ("Add the parts and fit C last",
             "`y = y_p + C/μ`. Put in `y(t₀)`, subtract the particular part's value "
             "at `t₀`, and divide by `1/μ(t₀)`."),
            ("Check the start and the equation",
             "The finished `y` must give the starting value at `t₀` and must satisfy "
             "the original equation. Both are one line."),
        ],
        "worked": {
            "title": "y′ + 3y = 2t with y(0) = 1, in two parts",
            "intro": [
                "The homogeneous equation has the factor `e^(3t)`, so its solution is "
                "known at once. The particular solution is a degree-one polynomial.",
            ],
            "lines": [
                "y_h = C·e^(−3t)",
                "try y_p = A·t + B:   A + 3A·t + 3B = 2t",
                "t terms:  3A = 2,   so  A = 2/3",
                "constants:  A + 3B = 0,   so  B = −2/9",
                "y_p = (2/3)·t − 2/9",
                "y = (2/3)·t − 2/9 + C·e^(−3t)",
                "y(0) = −2/9 + C = 1,   so  C = 11/9",
            ],
            "after": [
                "The order matters. The constant `11/9` is not `1`, and the difference "
                "is exactly the `2/9` that the particular part contributes at `t = 0`. "
                "Reading `C` off the homogeneous part alone would have set it to `1` and "
                "made `y(0)` equal to `7/9`.",
                "For a rehearsal, take the third preset, `y′ + 2y = e^t` with "
                "`y(0) = 0`, and write down `y_h`, `y_p` and `C` before pressing the "
                "button. The particular solution is a multiple of `e^t`; find the "
                "multiple by substitution, then compute the constant from the sum.",
            ],
        },
        "quiz_title": "Parts, sums and constants",
        "quiz": [
            {"q": "For `y′ + 3y = 2t` with `y(0) = 1`, a student fits `C` in `C·e^(−3t)` to `y(0) = 1`, then adds `y_p = (2/3)·t − 2/9`. What is `y(0)` for the result?",
             "a": ["`1`",
                   "`7/9`",
                   "`11/9`",
                   "`−2/9`"],
             "c": 1,
             "why": "With `C = 1` the sum at `t = 0` is `1 + (−2/9) = 7/9`, which is not "
                    "the starting value. The particular part contributes `−2/9` at "
                    "`t = 0`, so `C` has to make up `1 + 2/9 = 11/9`, which is the "
                    "value of `C` and not of `y(0)`. And `−2/9` is the particular "
                    "part alone."},
            {"q": "If `y₁` and `y₂` both solve `y′ + 2y = 6`, what equation does `y₁ − y₂` solve?",
             "a": ["`y′ + 2y = 6`",
                   "`y′ + 2y = 0`",
                   "`y′ + 2y = 12`",
                   "`y′ + 2y = 3`"],
             "c": 1,
             "why": "The left side is linear: `(y₁ − y₂)′ + 2·(y₁ − y₂) = 6 − 6 = 0`. The "
                    "difference solves the homogeneous equation, which is why one "
                    "particular solution is enough. `6` would be the answer for a "
                    "single solution, and `12` the answer for the sum, which is not "
                    "a solution of the forced equation."},
            {"q": "For `y′ + 2y = e^t` with `y(0) = 0`, the particular solution is `(1/3)·e^t`. What is `C` in `y = (1/3)·e^t + C·e^(−2t)`?",
             "a": ["`1/3`",
                   "`0`",
                   "`1`",
                   "`−1/3`"],
             "c": 3,
             "why": "At `t = 0` the particular part is `1/3`, so `1/3 + C = 0` and "
                    "`C = −1/3`. `C = 1/3` has the wrong sign. `C = 0` would leave "
                    "`y(0) = 1/3`, and `C = 1` would leave `4/3`."},
            {"q": "Why can `y_p + y_h` be a solution of `y′ + 3y = 2t`?",
             "a": ["Both solve the same equation, so their sum does too",
                   "The equation is first order, so any two solutions add",
                   "The left side is linear in `y`: for the sum it gives `q + 0`, which is `q`",
                   "Because `C` can always be chosen to make the sum fit"],
             "c": 2,
             "why": "The left side of the equation is linear, so applied to the sum it "
                    "is the left side applied to each part: `2t + 0`. The two parts "
                    "do not solve the same equation, and the sum of two solutions "
                    "of the forced equation gives `4t`, not `2t`. Being first order "
                    "does not make solutions add, and the choice of `C` is made after "
                    "the sum is known to be a solution."},
        ],
        "mistakes": [
            ("Fitting the constant to y_h before y_p is added",
             "For `y′ + 3y = 2t` with `y(0) = 1`, the slip gives `C = 1`, the solution "
             "`e^(−3t) + (2/3)·t − 2/9`, and `y(0) = 1 − 2/9 = 7/9`. The starting value "
             "belongs to the sum. The particular part is `−2/9` at `t = 0`, so the "
             "constant has to supply `1 + 2/9 = 11/9`."),
            ("Guessing y_p = A·t with no constant term",
             "For `y′ + 3y = 2t` the guess gives `A + 3A·t = 2t`. The `t` terms need "
             "`3A = 2` and the constant terms need `A = 0`, and no `A` does both. "
             "The derivative of `A·t` is a constant, so a constant has to be allowed "
             "in the guess: `y_p = A·t + B`, as the worked example does."),
            ("Believing the particular solution is unique",
             "Take `y_p* = (2/3)·t − 2/9 + e^(−3t)`. It also solves `y′ + 3y = 2t`, "
             "because the extra term is a homogeneous solution. With this choice the "
             "constant is `2/9`, not `11/9`, and the final `y` is the same, since "
             "`2/9 + 1 = 11/9`. The lab prints one choice, and the final solution does "
             "not depend on which."),
        ],
        "standard": (
            "Finish when you can write the general solution of y′ + p·y = q as y_p + y_h, check y_p by substitution, and fit the constant after adding.",
            "You should be able to solve the homogeneous equation, find one particular "
            "solution by a guess and matched coefficients, show that the sum solves "
            "the forced equation and that the difference of two solutions solves the "
            "homogeneous one, and compute the constant from a starting value after the "
            "two parts are added."),
        "note": 'Two ways to solve the same equation are now on the table. The integrating factor always works and needs an integral; the guess needs no integral and works when the forcing has a shape that can be guessed. The next half of the course takes the guess seriously for polynomial, exponential and sinusoidal forcing, and then applies the whole of it to circuits, tanks and loans.',
    },
]
