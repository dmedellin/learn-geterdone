"""Laplace Transforms -- the first half.

The transform as an exact rational function of s, linearity and the table, the
rule for the transform of a derivative, and the solution of an initial value
problem by algebra and partial fractions.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py
(mode laplace), by executing its shipped JavaScript under node, and pinned in
`expect`. The transforms, coefficients and solutions are exact; the truncated
integrals the first lesson shows are rounded and printed behind the
approximation sign, and the lesson says so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-laplace-transform",
        "title": "The Laplace Transform",
        "module": "The transform",
        "one_line": "Weight a signal by e^(−st), add up everything from t = 0 onward, and the result is a function of s that, for these signals, is a fraction.",
        "summary": (
            "The Laplace transform turns a function of time, `f(t)`, into a function of a new "
            "variable, `s`. Fix `s`, multiply the signal by `e^(−st)`, add up the area under "
            "the product from `t = 0` onward, and that is one number; doing it for every "
            "`s` gives the transform `F(s)`. For constants, powers and exponentials the result "
            "is a rational function of `s`, which the lab prints exactly. Two entries are "
            "worked out here: `ℒ[1] = 1/s` and `ℒ[e^(at)] = 1/(s − a)`."
        ),
        "key": [
            "ℒ[f](s) = ∫₀^∞ e^(−st)·f(t) dt",
            "ℒ[1] = 1/s,   s > 0",
            "ℒ[e^(at)] = 1/(s − a),   s > a",
            "ℒ[t] = 1/s²",
            "the transform is a function of s",
        ],
        "key_label": "The definition and the first entries",
        "concepts_intro": (
            "Three ideas, and the first is the one the rest of the course leans on: the "
            "transform is a whole function, not an answer."
        ),
        "concepts": [
            ("A number for each s, and so a function of s",
             "Pick a value of `s`. Multiply the signal by `e^(−st)`, which shrinks it faster the "
             "larger `s` is, and add up the area under the product from `t = 0` onward. That "
             "gives one number. Choose a different `s` and the number changes. The numbers "
             "taken together, one for each `s`, are the function `F(s)`, and that function is "
             "the transform. The signal lives in `t`; its transform lives in `s`."),
            ("The area has to be finite, and that puts a floor under s",
             "For `f = e^(2t)` the weighted signal is `e^(−(s − 2)t)`. If `s > 2` that shrinks "
             "toward zero and the area is finite. At `s = 2` it is the constant `1` forever, "
             "so the area has no end, and below `2` it grows. So `1/(s − 2)` is the transform "
             "only for `s > 2`. Every entry in the table comes with a floor of this kind, "
             "and the lab shows its integrals at a value of `s` above it."),
            ("For these signals the transform is a fraction in s",
             "Constants, powers of `t`, exponentials, sines and cosines all transform into "
             "rational functions of `s`: a polynomial over a polynomial. That is why the "
             "lab can print every transform exactly, and why the equations of the next lessons "
             "become algebra on fractions."),
        ],
        "read_title": "From the integral to the first two entries",
        "read_intro": "The definition, the two computations that give the first table entries, and the one habit of mind the rest of the course needs: the answer is a function.",
        "body": [
            ("def", ("The Laplace transform",
                     "For a function `f` defined for `t ≥ 0`, its transform is "
                     "`ℒ[f](s) = ∫₀^∞ e^(−st)·f(t) dt`, for every `s` at which the integral "
                     "has a finite value.",
                     "The integral to infinity means the integrals from `0` to `T`, as `T` "
                     "grows. The result is a function of `s`, and it is written `F(s)` when "
                     "the signal is called `f`.")),
            ("p", "The definition is an instruction, and the quickest way to see what it does "
                  "is to follow it on the simplest signal there is. Take `f = 1`. The "
                  "weighted signal is `e^(−st)`, and a function whose rate is `−s` times "
                  "itself has the antiderivative `−e^(−st)/s`, as you can check by taking "
                  "its derivative. So the integral from `0` to `T` is "
                  "`(1 − e^(−sT))/s`."),
            ("math", [
                "∫₀ᵀ e^(−st) dt = (1 − e^(−sT))/s",
                "s = 1:   1 − e^(−T)",
                "T = 1, 2, 5:   ≈ 0.632121, ≈ 0.864665, ≈ 0.993262",
            ]),
            ("p", "At `s = 1` the lab prints those three integrals in its status line. They are "
                  "rounded, which is why each carries `≈`, and they are closing in on `1`. "
                  "The reason is the term `e^(−sT)`: for positive `s` it shrinks toward zero as "
                  "`T` grows, so the integral approaches `1/s`. That is a claim the three "
                  "numbers support and the next theorem proves for every exponential."),
            ("thm", ("The first two entries",
                     "For `s > 0`, `ℒ[1] = 1/s`. For every constant `a` and every `s > a`, "
                     "`ℒ[e^(at)] = 1/(s − a)`.")),
            ("proof", ["The second statement contains the first, with `a = 0`. The weighted "
                       "signal is `e^(−st)·e^(at) = e^(−(s − a)t)`, and its antiderivative is "
                       "`−e^(−(s − a)t)/(s − a)`, because the derivative of "
                       "`e^(−kt)` is `−k·e^(−kt)` with `k = s − a`.",
                       "So the integral from `0` to `T` is `(1 − e^(−(s − a)T))/(s − a)`. When "
                       "`s > a` the exponent is negative and the term `e^(−(s − a)T)` shrinks "
                       "toward zero as `T` grows, which leaves `1/(s − a)`."]),
            ("example", ("e^(2t) at s = 3",
                         "The signal grows, and the transform exists anyway, because the "
                         "weight shrinks faster: at `s = 3` the product is `e^(−t)`, and its "
                         "integrals are the same three numbers as before.",
                         "The lab prints `1/(s − 2)`, and at `s = 3` that is `1/(3 − 2) = 1`, "
                         "which is where those integrals are heading. Take `s = 1` instead and "
                         "the formula gives `1/(1 − 2) = −1`, an impossible area for a positive "
                         "function, because the integral has no finite value there.")),
            ("h3", "The ramp"),
            ("p", "The signal `f = t` is a straight line, and the lab prints "
                  "`ℒ[t] = 1/s²`. That one is a claim here and not a computation: finding "
                  "the antiderivative of `t·e^(−st)` needs a rule this course does not "
                  "develop. What the lab can do is show the truncated integrals closing in "
                  "on the value of `1/s²`, which at `s = 1` is `1`: for `T = 1, 2, 5` they are "
                  "`≈ 0.264241`, `≈ 0.593994` and `≈ 0.959572`, rounded."),
            ("p", "Read the three entries together: `1/s`, `1/s²` and `1/(s − a)`. Each is a "
                  "fraction, each has a denominator that vanishes at one value of `s`, and "
                  "that value, `0` or `a`, is exactly the floor under `s`. The lab's second "
                  "tile lists these values under the name they carry for the rest of the "
                  "course: the poles of the fraction, the values of `s` at which its "
                  "denominator is zero. The denominators are going to matter more than "
                  "anything else in this course."),
            ("p", "One habit before the lab. When someone writes `ℒ[1] = 1/s`, the right "
                  "side is a function: at `s = 1` it is `1`, at `s = 2` it is `1/2` and at "
                  "`s = 4` it is `1/4`. The transform of one signal is never a number. The "
                  "equations of the next lessons are equations between functions of `s`, and "
                  "they are solved by algebra only because a function of `s` can be added, "
                  "multiplied and divided like a fraction."),
            ("p", "The lab keeps its two tiers apart. The transform it prints in the first "
                  "tile is an exact rational function in lowest terms. The integrals in the "
                  "status line are floating-point sums, rounded to six figures and marked "
                  "with `≈`; they are evidence for the claim, and they close in on it without "
                  "ever proving it."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "one",
            "presets": [
                {"id": "one", "label": "f = 1", "kind": "table", "f": "1",
                 "expect": {"lpF": "1/s", "lpPoles": "0"}},
                {"id": "exp", "label": "f = e^(2t)", "kind": "table", "f": "e^(2t)",
                 "expect": {"lpF": "1/(s − 2)", "lpPoles": "2"}},
                {"id": "ramp", "label": "f = t", "kind": "table", "f": "t",
                 "expect": {"lpF": "1/s²", "lpPoles": "0 (repeated)"}},
            ],
            "panel_title": "Transform a signal",
            "panel_intro": (
                "Pick a signal and read its transform in the first tile. The status line "
                "gives the truncated integrals at three upper limits, rounded, beside the "
                "value they close in on. Then type a signal of your own, such as 5 or "
                "e^(-3t), and predict the transform first."),
        }),
        "steps_title": "Transforming a signal from the definition",
        "steps_intro": "Weight, combine, integrate to T, let T grow. The last step is the one that gives the floor on s.",
        "steps": [
            ("Write the weighted signal",
             "Multiply the signal by `e^(−st)`. For `e^(at)` the product is "
             "`e^(−st)·e^(at)`."),
            ("Combine the exponentials",
             "Add the exponents: `e^(−st)·e^(at) = e^(−(s − a)t)`. Now the integrand is a "
             "single exponential with the rate `−(s − a)`."),
            ("Integrate from 0 to T",
             "The antiderivative of `e^(−kt)` is `−e^(−kt)/k`, so the integral is "
             "`(1 − e^(−kT))/k` with `k = s − a`."),
            ("Let T grow and find the floor",
             "If `k > 0` the term `e^(−kT)` shrinks toward zero and the integral approaches "
             "`1/k`. If `k ≤ 0` it does not, and the transform does not exist at that `s`."),
            ("Compare with the lab",
             "Type the signal and read the first tile. The status line shows the "
             "integrals at three limits, rounded, closing in on the value of your fraction."),
        ],
        "worked": {
            "title": "The transform of e^(2t)",
            "intro": [
                "Follow the steps for `f = e^(2t)`, so `a = 2`. The lab's second preset is this "
                "signal.",
            ],
            "lines": [
                "ℒ[e^(2t)](s) = ∫₀^∞ e^(−st)·e^(2t) dt",
                "= ∫₀^∞ e^(−(s − 2)t) dt",
                "∫₀ᵀ e^(−(s − 2)t) dt = (1 − e^(−(s − 2)T))/(s − 2)",
                "s > 2:   e^(−(s − 2)T) → 0 as T grows",
                "ℒ[e^(2t)] = 1/(s − 2)",
                "at s = 3:   1/(3 − 2) = 1",
            ],
            "after": [
                "The lab prints the same fraction. At `s = 3` it also prints the integrals "
                "from `0` to `T` for `T = 1, 2, 5`, rounded, and they are the same three "
                "numbers as for the constant at `s = 1`, because the weighted signal is "
                "`e^(−t)` in both. Each one sits a little below `1`, as "
                "`1 − e^(−T)` does.",
                "Notice what the floor did. The formula `1/(s − 2)` is a fraction, and it has "
                "a value at `s = 1`. The integral does not. The fraction is the transform "
                "only where the integral is finite, which is `s > 2`.",
            ],
        },
        "quiz_title": "Reading the definition",
        "quiz": [
            {"q": "What is `ℒ[e^(3t)]`, and where does it hold?",
             "a": ["`1/(s + 3)` for `s > −3`",
                   "`1/(s − 3)` for `s > 3`",
                   "`3/s` for `s > 0`",
                   "`1/(3s)` for `s > 0`"],
             "c": 1,
             "why": "The weighted signal is `e^(−(s − 3)t)`, so the transform is "
                    "`1/(s − 3)`, and the integral is finite only when `s − 3 > 0`. "
                    "`1/(s + 3)` is the transform of `e^(−3t)`, with the sign of the "
                    "exponent flipped. `3/s` and `1/(3s)` do not come from any "
                    "exponential: both have their pole at `0`, where `e^(3t)` has "
                    "it at `3`."},
            {"q": "For `f = 1` the transform is `1/s`. What is its value at `s = 2`?",
             "a": ["`2`, because the transform of a constant is the constant times `s`",
                   "`1`, because the transform of `1` is `1`",
                   "`1/2`",
                   "It is not a number: the transform is a function"],
             "c": 2,
             "why": "At `s = 2` the fraction `1/s` is `1/2`, and that is the area under "
                    "`e^(−2t)` from `0` onward. The transform as a whole is a function, "
                    "but its value at one `s` is a number, so the last choice mistakes the "
                    "whole for the part. The first two ignore the formula."},
            {"q": "For which `s` is the integral that defines `ℒ[e^(2t)]` finite?",
             "a": ["Every `s`, because `1/(s − 2)` is a fraction",
                   "Only `s > 2`",
                   "Only `s > 0`",
                   "Only `s < 2`"],
             "c": 1,
             "why": "The weighted signal is `e^(−(s − 2)t)`, which shrinks only when "
                    "`s − 2 > 0`. `s > 0` is the condition for the constant `1`, not for "
                    "`e^(2t)`: at `s = 1` the product `e^(t)` grows without bound. The "
                    "formula `1/(s − 2)` exists at `s = 1` as a fraction, but the "
                    "integral does not. For `s < 2` the integral is infinite."},
            {"q": "The lab prints `≈ 0.632121`, `≈ 0.864665` and `≈ 0.993262` for the integrals of `e^(−t)` up to `T = 1, 2, 5`. What do they show?",
             "a": ["That the transform at `s = 1` is exactly `0.993262`",
                   "That the integrals are rising toward `1`, the value of `ℒ[1]` at `s = 1`",
                   "That the integral is `1` once `T` reaches `2`",
                   "That the transform is a decimal and not a fraction"],
             "c": 1,
             "why": "Each integral is `1 − e^(−T)`, rounded, and these rise toward the "
                    "limit `1 = 1/s` at `s = 1`. None of them is the transform, since "
                    "none reaches `1`. The transform is the exact fraction in the first "
                    "tile, and the decimals are only evidence for it."},
        ],
        "mistakes": [
            ("Taking the transform of a signal to be a number",
             "The transform of `1` is `1/s`, and `1/s` has a different value at every `s`: "
             "`1` at `s = 1`, `1/2` at `s = 2`, `1/4` at `s = 4`. A reader who writes "
             "`ℒ[1] = 1` has evaluated at one point and thrown the rest away. The "
             "equations in later lessons are equations between functions of `s`, and "
             "solving them needs the whole function."),
            ("Using 1/(s − a) at an s where the integral does not exist",
             "For `f = e^(2t)` the fraction `1/(s − 2)` equals `−1` at `s = 1`. The integral "
             "of a positive function cannot be negative, and it is not: at `s = 1` the "
             "weighted signal is `e^(t)`, which grows, and the integral is infinite. The "
             "fraction is the transform only on the stretch `s > 2`, and the lab's integrals "
             "are taken at a value above the floor for this reason."),
            ("Flipping the sign in the denominator",
             "Writing `ℒ[e^(2t)] = 1/(s + 2)` confuses the weight `e^(−st)` with the signal. "
             "Combining gives `e^(−st)·e^(2t) = e^(−(s − 2)t)`, with `s − 2`. The test is the "
             "lab: at `s = 3` the correct fraction is `1`, the integrals head to `1`, and "
             "the sign-flipped one would give `1/5`."),
        ],
        "standard": (
            "Finish when you can write the defining integral of the Laplace transform and compute the transform of 1 and of an exponential from it.",
            "You should be able to say that the result is a function of s and not a number, "
            "state for which s each entry holds, integrate the weighted exponential from "
            "0 to T and let T grow, and read a transform off the lab as an exact "
            "fraction with the truncated integrals marked as rounded."),
        "note": 'One transform is not much use alone. The next lesson builds the short table that covers every signal this course meets, and the property &mdash; linearity &mdash; that lets a table of five entries transform sums of any size. See &ldquo;Linearity and the Table&rdquo;.',
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "linearity-and-the-table",
        "title": "Linearity and the Table",
        "module": "The transform",
        "one_line": "The transform of a sum is the sum of the transforms, constants come straight out, and five table entries then cover every signal this course uses.",
        "summary": (
            "Two facts make the transform usable. It is linear: the transform of "
            "`c·f + d·g` is `c·ℒ[f] + d·ℒ[g]`. And a table of five families &mdash; powers, "
            "exponentials, cosines, sines, and a power times an exponential &mdash; covers every "
            "signal the rest of the course uses. Together they transform a sum of terms one "
            "term at a time and combine the result into a single fraction. They do not "
            "turn a product of signals into a product of transforms."
        ),
        "key": [
            "ℒ[c·f + d·g] = c·ℒ[f] + d·ℒ[g]",
            "ℒ[tⁿ] = n!/s^(n+1)",
            "ℒ[cos(bt)] = s/(s² + b²)",
            "ℒ[sin(bt)] = b/(s² + b²)",
            "ℒ[t·e^(at)] = 1/(s − a)²",
            "ℒ[f·g] is not ℒ[f]·ℒ[g]",
        ],
        "key_label": "Linearity, the table, and the one thing that fails",
        "concepts_intro": "Three ideas: what linearity says, what the table says, and the product that the transform does not respect.",
        "concepts": [
            ("Linearity: constants out, sums apart",
             "To transform `3t² − 2e^(−t)`, transform each term separately, keep the "
             "constants `3` and `−2` where they are, and add: "
             "`3·ℒ[t²] − 2·ℒ[e^(−t)]`. This works because the transform is an integral, and "
             "an integral of a sum is the sum of the integrals, with a constant factor "
             "taken outside."),
            ("The table has five families",
             "Powers `tⁿ`, exponentials `e^(at)`, cosines `cos(bt)`, sines `sin(bt)` and a "
             "power times an exponential `t·e^(at)`. The cosine and sine entries share the "
             "denominator `s² + b²`, and the entry for `t·e^(at)` is the entry for `t` with "
             "`s` replaced by `s − a`. A signal outside these families is outside this "
             "course, apart from the switch that the last module adds."),
            ("The transform of a product is not a product of transforms",
             "Linearity is about sums and constants only. Multiplying two signals does "
             "something else to their transforms, and the shortest test is the signal "
             "`1·1`: its transform is `1/s`, while `ℒ[1]·ℒ[1]` is `1/s²`."),
        ],
        "read_title": "Linearity, then the five entries, then the product that fails",
        "read_intro": "A theorem, a proof from the integral, the table, and a worked case that shows linearity doing its job and the product refuting itself.",
        "body": [
            ("thm", ("Linearity",
                     "For signals `f` and `g` and constants `c` and `d`, at every `s` where "
                     "both transforms exist, `ℒ[c·f + d·g] = c·ℒ[f] + d·ℒ[g]`.")),
            ("proof", ["The weighted signal is `e^(−st)·(c·f + d·g) = c·e^(−st)·f + d·e^(−st)·g`.",
                       "The integral from `0` to `T` of a sum is the sum of the integrals, "
                       "and a constant factor comes outside, because the integral is a limit "
                       "of sums of the form rate times step. Let `T` grow in each term "
                       "and the right side becomes `c·ℒ[f] + d·ℒ[g]`."]),
            ("h3", "The table"),
            ("math", [
                "ℒ[1] = 1/s",
                "ℒ[tⁿ] = n!/s^(n+1)",
                "ℒ[e^(at)] = 1/(s − a)",
                "ℒ[cos(bt)] = s/(s² + b²)",
                "ℒ[sin(bt)] = b/(s² + b²)",
                "ℒ[t·e^(at)] = 1/(s − a)²",
            ]),
            ("p", "The first lesson derived `1/s` and `1/(s − a)`. The rest of the table is "
                  "stated here as claims. The lab computes every transform by exactly these "
                  "rules, so it cannot confirm them; what it offers is evidence, in its "
                  "status line, where the truncated integrals of the weighted signal close "
                  "in on the value the fraction gives at one `s`. The entry "
                  "for `tⁿ` has `n!` on top, the product `n·(n − 1)·⋯·1`, so `ℒ[t] = 1/s²`, "
                  "`ℒ[t²] = 2/s³` and `ℒ[t³] = 6/s⁴`."),
            ("p", "The last entry is worth a second look. Put `a = 0` in "
                  "`ℒ[t·e^(at)] = 1/(s − a)²` and it becomes `1/s²`, which is `ℒ[t]`. "
                  "Multiplying the signal by `e^(at)` has replaced `s` by `s − a`. The "
                  "same replacement turns `1/s` into `1/(s − a)`, the second entry, and "
                  "that pattern is the reason the table needs only these families."),
            ("example", ("A sum of two terms",
                         "Transform `f = 3t² − 2e^(−t)`. By linearity it is "
                         "`3·ℒ[t²] − 2·ℒ[e^(−t)]`. From the table, `ℒ[t²] = 2/s³` and "
                         "`ℒ[e^(−t)] = 1/(s + 1)`, because `a = −1`.",
                         "So the transform is `3·(2/s³) − 2·(1/(s + 1)) = 6/s³ − 2/(s + 1)`. "
                         "Over a common denominator `s³·(s + 1)` the numerator is "
                         "`6·(s + 1) − 2·s³ = 6s + 6 − 2s³`, and the lab prints the single "
                         "fraction in lowest terms.")),
            ("p", "Sines and cosines work the same way, with one new feature: their "
                  "denominator `s² + b²` has no real zero. For `cos(2t)` the lab prints "
                  "`s/(s² + 4)`. The poles of that fraction are the numbers where the "
                  "denominator vanishes, `±2i`, and the lab lists them in its second tile. "
                  "That frequency `2` in the signal reappears, as the square root of `4`, in "
                  "the transform."),
            ("h3", "What linearity does not cover"),
            ("p", "Linearity does not say anything about a product of two signals. Take "
                  "`f = g = 1`. The product `f·g` is `1`, and `ℒ[1] = 1/s`. The product of the "
                  "transforms is `(1/s)·(1/s) = 1/s²`, a different function. The transform "
                  "of a product is a different and harder operation, which this course "
                  "does not need."),
            ("example", ("t times e^(3t)",
                         "The signal `t·e^(3t)` is a product of `t` and `e^(3t)`. Its "
                         "transform is the table entry `1/(s − 3)²`.",
                         "The product of the two separate transforms is "
                         "`ℒ[t]·ℒ[e^(3t)] = (1/s²)·(1/(s − 3)) = 1/(s²·(s − 3))`, which has a "
                         "pole at `0` that the real transform does not. The lab's third preset "
                         "prints the correct one, and a poles tile that agrees: the only pole "
                         "is at `3`.")),
            ("p", "A table does the work of a computation, so check one entry before trusting "
                  "it. The lab does that at every keystroke: it transforms what you type "
                  "by the table and linearity and prints a reduced fraction, so a "
                  "slip in your own arithmetic shows up as a mismatch."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "mixed",
            "presets": [
                {"id": "mixed", "label": "f = 3t² − 2e^(−t)", "kind": "table", "f": "3t^2 - 2e^(-t)",
                 "expect": {"lpF": "(−2s³ + 6s + 6)/(s³(s + 1))", "lpPartial": "6/s³ − 2/(s + 1)", "lpPoles": "−1, 0 (repeated)"}},
                {"id": "cosine", "label": "f = cos(2t)", "kind": "table", "f": "cos(2t)",
                 "expect": {"lpF": "s/(s² + 4)", "lpPoles": "±2i"}},
                {"id": "shifted", "label": "f = t·e^(3t)", "kind": "table", "f": "t e^(3t)",
                 "expect": {"lpF": "1/(s − 3)²", "lpPoles": "3 (repeated)"}},
            ],
            "panel_title": "Transform a sum of table entries",
            "panel_intro": (
                "Pick a signal and read its transform in the first tile, in lowest terms. "
                "Before you pick the first preset, write the transform term by term and "
                "combine it yourself. Then type a signal of your own built from the "
                "table, such as 2 + 5sin(3t), and check your fraction."),
        }),
        "steps_title": "Transforming a signal from the table",
        "steps_intro": "Split, look up, scale, add, combine. Combine last: the table's entries are simpler uncombined.",
        "steps": [
            ("Split the signal into terms",
             "Each term must be a constant times one table family: `3t²`, `−2e^(−t)`, "
             "`5·cos(2t)`. If a term is not, it is outside the table."),
            ("Look up each family",
             "Match the term to its entry. Name `n`, `a` or `b` for each, and watch the signs: "
             "`e^(−t)` has `a = −1`."),
            ("Scale by the constants",
             "Multiply each transform by the constant in front of its term. The constant is "
             "outside the transform, not inside the fraction."),
            ("Add the transforms",
             "Write the sum with each fraction left as it is. The result is already correct."),
            ("Combine over a common denominator if you need one fraction",
             "Multiply each numerator by the factors its denominator lacks. Compare with the "
             "lab, which prints the reduced form."),
        ],
        "worked": {
            "title": "The transform of 3t² − 2e^(−t)",
            "intro": [
                "The first preset. Two terms, two table entries.",
            ],
            "lines": [
                "ℒ[3t² − 2e^(−t)] = 3·ℒ[t²] − 2·ℒ[e^(−t)]",
                "ℒ[t²] = 2!/s³ = 2/s³",
                "ℒ[e^(−t)] = 1/(s + 1)",
                "= 3·(2/s³) − 2·(1/(s + 1))",
                "= 6/s³ − 2/(s + 1)",
                "= (6·(s + 1) − 2·s³)/(s³·(s + 1))",
                "= (6s + 6 − 2s³)/(s³·(s + 1))",
            ],
            "after": [
                "The lab prints `(−2s³ + 6s + 6)/(s³(s + 1))`, which is the last line with the numerator "
                "written from the highest power down; its fourth tile keeps the term-by-term "
                "form `6/s³ − 2/(s + 1)`.",
                "A check that costs nothing: at a large `s` the `6/s³` term is tiny and the "
                "`−2/(s + 1)` term dominates, so the fraction should be close to "
                "`−2/s`. Both forms agree.",
            ],
        },
        "quiz_title": "Using the table",
        "quiz": [
            {"q": "What is `ℒ[4 + 6t²]`?",
             "a": ["`4/s + 6/s³`",
                   "`4/s + 12/s³`",
                   "`4/s + 12/s²`",
                   "`10/s³`"],
             "c": 1,
             "why": "By linearity it is `4·(1/s) + 6·(2/s³)`, and `ℒ[t²] = 2!/s³ = 2/s³`, "
                    "so the second term is `12/s³`. Dropping the `2!` gives the first "
                    "choice. `s²` in the denominator is the entry for `t`, not `t²`. "
                    "The last choice adds the constants as if the terms were one family."},
            {"q": "What is `ℒ[sin(3t)]`?",
             "a": ["`1/(s² + 9)`",
                   "`s/(s² + 9)`",
                   "`3/(s² + 3)`",
                   "`3/(s² + 9)`"],
             "c": 3,
             "why": "The entry is `b/(s² + b²)` with `b = 3`, which is `3/(s² + 9)`. "
                    "`s/(s² + 9)` is the cosine. Omitting the `3` on top loses the factor "
                    "that makes the entry correct. The denominator is `b²`, so `s² + 3` "
                    "comes from squaring wrongly."},
            {"q": "Which statement about `t·e^(2t)` is correct?",
             "a": ["Its transform is `ℒ[t]·ℒ[e^(2t)] = 1/(s²·(s − 2))`",
                   "Its transform is `1/(s + 2)²`",
                   "Its transform is `1/(s − 2)²`",
                   "Its transform is `2/(s − 2)`"],
             "c": 2,
             "why": "It is the table entry `1/(s − a)²` with `a = 2`. The product of "
                    "transforms is a different function, with a pole at `0` that the "
                    "real transform lacks. `s + 2` has the sign of `a` reversed, which is "
                    "the transform of `t·e^(−2t)`. The last choice is not any table entry."},
            {"q": "Which of these is exactly equal to `ℒ[5e^(−3t) + 2cos(t)]`?",
             "a": ["`5/(s + 3) + 2s/(s² + 1)`",
                   "`5/(s − 3) + 2s/(s² + 1)`",
                   "`5/(s + 3) + 2/(s² + 1)`",
                   "`10/((s + 3)(s² + 1))`"],
             "c": 0,
             "why": "`5e^(−3t)` has `a = −3` and gives `5/(s + 3)`; `2cos(t)` has `b = 1` and "
                    "gives `2s/(s² + 1)`. The second choice flips the sign of `a`. The "
                    "third uses the sine entry, which has no `s` on top. The last is the "
                    "product of the two transforms, which linearity does not allow."},
        ],
        "mistakes": [
            ("Taking the transform of a product to be the product of the transforms",
             "With `f = g = 1` the product is `1`, and `ℒ[1] = 1/s`, while `ℒ[1]·ℒ[1] = 1/s²`. "
             "The lab's third preset is another refutation: `t·e^(3t)` transforms to "
             "`1/(s − 3)²`, and `ℒ[t]·ℒ[e^(3t)] = 1/(s²·(s − 3))` has a pole at `0` that the real "
             "transform lacks. Linearity covers sums and constants and nothing else."),
            ("Dropping the factorial in the power entry",
             "Writing `ℒ[t²] = 1/s³` loses a factor of `2`. The first preset catches it: "
             "its term `3t²` contributes `6/s³`, and `6/s³` is `3·2/s³`. With the "
             "factorial missing the term would be `3/s³`, and the combined "
             "fraction would not match the lab's."),
            ("Reversing the sign of a in an exponential",
             "The transform of `e^(−t)` is `1/(s + 1)`, because `a = −1` and `s − a = s + 1`. "
             "Writing `1/(s − 1)` is the transform of `e^(t)`. In the first preset this "
             "turns `−2/(s + 1)` into `−2/(s − 1)` and moves the pole of the answer from "
             "`−1` to `1`; the poles tile lists `−1` and `0`, and the slip would put `1` there."),
        ],
        "standard": (
            "Finish when you can transform any sum of the five table families and write the result as one fraction.",
            "You should be able to scale each term by its constant, look up the entry with "
            "the right sign of a and the right factorial, add the fractions over a common "
            "denominator, and say why the transform of a product of signals is not the "
            "product of their transforms."),
        "note": 'The table so far transforms signals. The next lesson transforms a <em>derivative</em>, which is the step that lets the transform meet a differential equation. See &ldquo;The Transform of a Derivative&rdquo;.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "the-transform-of-a-derivative",
        "title": "The Transform of a Derivative",
        "module": "The transform",
        "one_line": "ℒ[y′] is s times Y less the starting value, and that starting value is what puts the initial conditions into the equation.",
        "summary": (
            "The transform of a derivative is the transform of the function multiplied by "
            "`s`, less the function's value at the start: `ℒ[y′] = s·Y − y(0)`. Applying it "
            "twice gives `ℒ[y″] = s²·Y − s·y(0) − y′(0)`. The rule is proved from the "
            "product rule and the fundamental theorem, and the lab checks it on a signal by "
            "transforming the derivative directly and comparing. The initial values come "
            "with the rule, which is what makes the method of the next lesson work."),
        "key": [
            "ℒ[y′] = s·Y − y(0)",
            "ℒ[y″] = s²·Y − s·y(0) − y′(0)",
            "Y means the transform of y",
            "y(0) stays: it is not optional",
        ],
        "key_label": "The derivative rules",
        "concepts_intro": "Three ideas: the rule, where the initial value comes from, and why it is easy to forget.",
        "concepts": [
            ("Differentiating in t is multiplying by s, with a correction",
             "If the transform of `y` is `Y(s)`, then the transform of `y′` is `s·Y(s)` "
             "less the value of `y` at `t = 0`. In `t`, the operation is a derivative. In "
             "`s`, it is a multiplication and a subtraction. That exchange is the whole "
             "reason the transform is useful for differential equations."),
            ("The correction is the initial value, and it comes from the lower limit",
             "The transform integrates from `t = 0`. When the product rule is integrated "
             "over that interval, the endpoint at `t = 0` leaves behind `y(0)`. The "
             "starting value is not added by hand afterward: it is part of the rule, and "
             "an equation transformed with the rule already contains it."),
            ("The slip is invisible when y(0) = 0",
             "A reader who forgets the correction and writes `ℒ[y′] = s·Y` gets the right "
             "answer for every signal that starts at zero, `sin(t)` and `t²` among them. "
             "That is why the slip survives: it fails only when the starting value is "
             "not zero, and then it is wrong by exactly that value."),
        ],
        "read_title": "The rule, its proof, and a check on three signals",
        "read_intro": "The rule for a first derivative, a proof that uses nothing beyond the product rule and the fundamental theorem, the rule for a second derivative, and the lab's check.",
        "body": [
            ("p", "Throughout, a capital letter stands for the transform of the lower-case "
                  "one: `Y(s)` is `ℒ[y]` and `F(s)` is `ℒ[f]`. The rules are stated for a "
                  "signal `y` and its derivatives, at values of `s` large enough that "
                  "the transforms exist."),
            ("thm", ("The transform of a first derivative",
                     "`ℒ[y′] = s·Y − y(0)`, for `s` large enough that the transforms exist and "
                     "`e^(−sT)·y(T)` shrinks toward zero as `T` grows.")),
            ("proof", ["The product rule gives `(e^(−st)·y)′ = −s·e^(−st)·y + e^(−st)·y′`. "
                       "Integrate both sides from `0` to `T`. The fundamental theorem says the left "
                       "side is `e^(−sT)·y(T) − y(0)`.",
                       "On the right, the first integral is `−s` times the integral that "
                       "defines `Y`, and the second is the integral that defines `ℒ[y′]`. Let "
                       "`T` grow: the term `e^(−sT)·y(T)` goes to zero, which leaves "
                       "`−y(0) = −s·Y + ℒ[y′]`. Solving for `ℒ[y′]` gives the rule."]),
            ("p", "The condition in the theorem is not decoration. It holds for every "
                  "signal in the table, at every `s` above the signal's floor, and the "
                  "lab only transforms signals from the table. The proof shows where the "
                  "initial value enters: it is the value of the left side at the lower limit."),
            ("thm", ("The transform of a second derivative",
                     "`ℒ[y″] = s²·Y − s·y(0) − y′(0)`.")),
            ("proof", ["Apply the first rule to the function `y′`: "
                       "`ℒ[y″] = s·ℒ[y′] − y′(0)`.",
                       "Then replace `ℒ[y′]` by `s·Y − y(0)`: "
                       "`ℒ[y″] = s·(s·Y − y(0)) − y′(0) = s²·Y − s·y(0) − y′(0)`."]),
            ("math", [
                "ℒ[y′]  = s·Y − y(0)",
                "ℒ[y″] = s²·Y − s·y(0) − y′(0)",
            ]),
            ("example", ("The rule on e^(2t)",
                         "Take `y = e^(2t)`, so `y′ = 2e^(2t)` and `y(0) = 1`. The "
                         "transform of `y` is `1/(s − 2)`, and the transform of `y′` is "
                         "twice that, `2/(s − 2)`, by linearity.",
                         "The rule says `s·Y − y(0) = s/(s − 2) − 1`. Over a common "
                         "denominator that is `(s − (s − 2))/(s − 2) = 2/(s − 2)`. "
                         "The two sides agree, and the lab's first preset prints "
                         "`equal`.")),
            ("p", "The same check on `y = sin(t)` and on `y = t²` also prints `equal`, and "
                  "for both of them the starting value is zero. Then the rule reads "
                  "`ℒ[y′] = s·Y`, and a reader who had forgotten the correction would "
                  "not see anything wrong. Only a signal with a non-zero start, such as "
                  "`e^(2t)`, makes the forgotten term visible: dropping it leaves "
                  "`s/(s − 2)`, which is `1` too large."),
            ("example", ("The rule on t²",
                         "For `y = t²` the transform is `2/s³`, and `y(0) = 0`. The "
                         "derivative is `2t`, whose transform is `2/s²`. The rule gives "
                         "`s·(2/s³) − 0 = 2/s²`.",
                         "Both sides are the same fraction, and the lab prints `equal`.")),
            ("p", "What the lab does and does not do. It computes `ℒ[y′]` by differentiating "
                  "the signal and transforming the result, and computes `s·Y − y(0)` "
                  "separately, as exact fractions. Showing them equal on three signals "
                  "is a demonstration; the proof above is the reason it holds for "
                  "every signal."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "exp",
            "presets": [
                {"id": "exp", "label": "f = e^(2t)", "kind": "derivative", "f": "e^(2t)",
                 "expect": {"lpF": "1/(s − 2)", "lpY": "2/(s − 2)", "lpEqual": "equal"}},
                {"id": "sine", "label": "f = sin(t)", "kind": "derivative", "f": "sin(t)",
                 "expect": {"lpF": "1/(s² + 1)", "lpY": "s/(s² + 1)", "lpEqual": "equal"}},
                {"id": "poly", "label": "f = t²", "kind": "derivative", "f": "t^2",
                 "expect": {"lpF": "2/s³", "lpY": "2/s²", "lpEqual": "equal"}},
            ],
            "panel_title": "Check the derivative rule on a signal",
            "panel_intro": (
                "The first tile is the transform of the signal; the third is the transform "
                "of its derivative, computed directly; the last says whether that equals "
                "s times the first less the starting value. Try e^(-3t) and cos(2t) too, "
                "which start at a value that is not zero, and work out the correction by hand."),
        }),
        "steps_title": "Verifying the rule on a signal",
        "steps_intro": "Transform the signal, differentiate it and transform that, then compare against the rule.",
        "steps": [
            ("Transform the signal",
             "Find `Y(s) = ℒ[y]` from the table, and record `y(0)`."),
            ("Differentiate the signal and transform the derivative",
             "Compute `y′` in `t`, then find `ℒ[y′]` from the table. This is the left-hand "
             "side of the rule."),
            ("Form s times Y less the starting value",
             "Multiply `Y` by `s`, subtract `y(0)`, and combine into one fraction. This is "
             "the right-hand side."),
            ("Compare",
             "If the two fractions are the same, the rule holds on this signal. If they "
             "differ by a constant, the starting value was left out or mis-signed."),
        ],
        "worked": {
            "title": "The transform of y′ for y = e^(2t), both ways",
            "intro": [
                "The first preset. The left side is computed straight from the derivative; "
                "the right side from the rule.",
            ],
            "lines": [
                "y = e^(2t),   y′ = 2e^(2t),   y(0) = 1",
                "ℒ[y′] = 2·ℒ[e^(2t)] = 2/(s − 2)",
                "s·Y − y(0) = s/(s − 2) − 1",
                "= (s − (s − 2))/(s − 2)",
                "= 2/(s − 2)",
                "the two fractions are equal",
            ],
            "after": [
                "The subtraction of `1` is what makes the match work. Without it the right "
                "side is `s/(s − 2)`, which is `1` more than `2/(s − 2)` at every `s`.",
                "For a second derivative the same check needs two corrections, and the "
                "next lesson uses both: `s·y(0)` and `y′(0)`.",
            ],
        },
        "quiz_title": "Writing and using the rules",
        "quiz": [
            {"q": "The equation `y′ − 3y = 0` has `y(0) = 2`. What is the transformed equation?",
             "a": ["`(s − 3)·Y = 0`",
                   "`(s − 3)·Y − 2 = 0`",
                   "`(s + 3)·Y − 2 = 0`",
                   "`s·Y − 3 = 0`"],
             "c": 1,
             "why": "`ℒ[y′] = s·Y − 2` and `ℒ[−3y] = −3·Y`, so the equation is "
                    "`s·Y − 2 − 3·Y = 0`, which is `(s − 3)·Y − 2 = 0`. The first choice "
                    "forgets the `y(0)`. The third has the wrong sign on the `3`, and the "
                    "last mixes the coefficient and the starting value."},
            {"q": "With `y(0) = 1` and `y′(0) = −2`, what is `ℒ[y″]`?",
             "a": ["`s²·Y − s + 2`",
                   "`s²·Y − s − 2`",
                   "`s²·Y + s − 2`",
                   "`s²·Y − 1 + 2`"],
             "c": 0,
             "why": "`ℒ[y″] = s²·Y − s·y(0) − y′(0) = s²·Y − s·1 − (−2) = s²·Y − s + 2`. "
                    "Subtracting a negative gives `+2`, so the second choice has the wrong "
                    "sign. The third reverses the sign of `s·y(0)`, and the last drops the "
                    "factor `s`."},
            {"q": "Which signal can be used to check `ℒ[y′] = s·Y` without any correction term, and why?",
             "a": ["`cos(t)`, because its derivative is a sine",
                   "`e^(2t)`, because its derivative is a multiple of itself",
                   "`1`, because it is constant",
                   "`sin(t)`, because its value at `t = 0` is zero"],
             "c": 3,
             "why": "The correction is `y(0)`, so it vanishes only when the signal starts at "
                    "zero, as `sin(t)` does. `cos(t)` and `e^(2t)` both start at `1`, and the "
                    "rule needs the `−1` for each. The constant `1` also starts at `1`: "
                    "its derivative is `0`, so `ℒ[y′] = 0`, while `s·(1/s) = 1`, and "
                    "the correction `−1` is what cancels it."},
            {"q": "For `y = e^(2t)` a student computes `s·Y = s/(s − 2)` and calls it `ℒ[y′]`. How far off is the answer?",
             "a": ["It is exact: the two are equal",
                   "It is too large by `y(0) = 1`, at every `s`",
                   "It is too small by `y(0) = 1`, at every `s`",
                   "It is too large by a factor of `s`"],
             "c": 1,
             "why": "The true value is `2/(s − 2) = s/(s − 2) − 1`, so `s/(s − 2)` exceeds it "
                    "by exactly `1`. It is not too small, since it has the extra positive "
                    "term. The error is an additive constant, not a factor of `s`."},
        ],
        "mistakes": [
            ("Writing the transform of y′ as s·Y and forgetting the initial value",
             "For `y = e^(2t)` the slip gives `s/(s − 2)`, but the transform of "
             "`y′ = 2e^(2t)` is `2/(s − 2)`; the two differ by `1 = y(0)` at every `s`. The "
             "slip is hard to catch because for `sin(t)` and `t²`, where `y(0) = 0`, the "
             "wrong rule and the right rule agree. Always write the correction, and check it "
             "on a signal that starts away from zero."),
            ("Subtracting y(0) from Y instead of from s·Y",
             "The rule is `s·Y − y(0)`, not `s·(Y − y(0))`. For `e^(2t)` the second gives "
             "`s·(1/(s − 2) − 1) = s·(3 − s)/(s − 2)`, which is not `2/(s − 2)`. The "
             "value `y(0)` is a constant that is subtracted, not a factor that is multiplied "
             "by `s`."),
            ("Giving the transform of y″ only one correction",
             "A second derivative needs two starting values, `y(0)` and `y′(0)`, and they "
             "enter differently: `y(0)` is multiplied by `s`. Writing "
             "`s²·Y − y(0) − y′(0)` drops that factor. Applying the first rule twice, as in "
             "the proof, is the safe way to get it: `s·(s·Y − y(0)) − y′(0)`."),
        ],
        "standard": (
            "Finish when you can write the transform of y′ and of y″ with their initial values and verify the first on a signal.",
            "You should be able to state both rules, say where the initial value comes "
            "from, transform a signal and its derivative separately, and show by exact "
            "fractions that the two sides of the rule agree; and say why the slip of leaving the "
            "initial value out is invisible when it is zero."),
        "note": 'With the derivative rules and the table in hand, an initial value problem is a line of algebra and a table read backwards. That is the next lesson, &ldquo;Solving an Initial Value Problem&rdquo;.',
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "solving-an-initial-value-problem",
        "title": "Solving an Initial Value Problem",
        "module": "Solving with it",
        "one_line": "Transform both sides, solve for Y by algebra, invert with partial fractions, and the initial values are already in the answer.",
        "summary": (
            "A constant-coefficient initial value problem is solved in four moves: transform "
            "both sides with the derivative rules, solve the resulting algebraic equation "
            "for `Y(s)`, take `Y` apart into table forms by partial fractions, and read the "
            "table backwards to get `y(t)`. The initial values enter at the first move, so "
            "no constants are fitted at the end. The lab runs the whole chain in exact "
            "fractions and substitutes the answer back into the equation."),
        "key": [
            "transform, solve for Y, invert, check",
            "y′ + a·y = q:   (s + a)·Y = y(0) + ℒ[q]",
            "(s² + b·s + c)·Y = initial terms + ℒ[q]",
            "y(0) and y′(0) go in at the first step",
        ],
        "key_label": "The four moves",
        "concepts_intro": "Three ideas: the equation turns into algebra, the initial values arrive with it, and the inverse is the table read from right to left.",
        "concepts": [
            ("The equation becomes algebra in s",
             "Transform every term of the equation. The derivative rules turn `y′` and `y″` "
             "into multiples of `Y` plus terms that are already known. What remains is "
             "`(a·s² + b·s + c)·Y = something`, where the left coefficient is the "
             "characteristic polynomial of the equation, and the right side is made "
             "of the initial values and the transform of the forcing."),
            ("The initial values arrive with the transform",
             "The corrections in the derivative rules are the initial values, so the "
             "right side already contains them. Dividing by the characteristic polynomial "
             "gives `Y(s)` as one fraction, and its inverse is the solution to this "
             "initial value problem, with no constants left to fit."),
            ("Inverting is partial fractions and the table read backwards",
             "A fraction like `(s + 3)/((s + 1)(s + 2))` is not in the table. Taking it apart "
             "into `A/(s + 1) + B/(s + 2)` gives two entries that are, and the table "
             "read from right to left returns `A·e^(−t) + B·e^(−2t)`. When the denominator has "
             "an irreducible quadratic, complete the square: `(s + 1)² + 4` is the "
             "form the sine and cosine entries have."),
        ],
        "read_title": "Four moves, on a second-order equation",
        "read_intro": "The transformed equation in general, a first-order case in full, and a second-order case with real roots and one with complex roots.",
        "body": [
            ("p", "Take the equation `a·y″ + b·y′ + c·y = q(t)` with starting values `y(0)` "
                  "and `y′(0)`. Transform each term with the rules of the previous lesson "
                  "and collect everything that multiplies `Y`."),
            ("math", [
                "a·(s²·Y − s·y(0) − y′(0)) + b·(s·Y − y(0)) + c·Y = ℒ[q]",
                "(a·s² + b·s + c)·Y = a·(s·y(0) + y′(0)) + b·y(0) + ℒ[q]",
            ]),
            ("p", "The polynomial `a·s² + b·s + c` multiplying `Y` is the characteristic "
                  "polynomial of the equation, with `s` in place of `r`. That is the first "
                  "connection to the earlier method, and the next lessons make it precise. "
                  "For a first-order equation `y′ + a·y = q` the same steps give "
                  "`(s + a)·Y = y(0) + ℒ[q]`."),
            ("example", ("A first-order case",
                         "Solve `y′ + 2y = 6` with `y(0) = 0`. The transform of the constant "
                         "`6` is `6/s`, so `(s + 2)·Y = 0 + 6/s`, and `Y = 6/(s·(s + 2))`.",
                         "Partial fractions: `6/(s·(s + 2)) = A/s + B/(s + 2)`. At `s = 0` the "
                         "factor `s + 2` is `2`, so `A = 6/2 = 3`. At `s = −2` the factor "
                         "`s` is `−2`, so `B = 6/(−2) = −3`. Then `y = 3 − 3e^(−2t)`, "
                         "which starts at `0` and settles at `3`.")),
            ("h3", "A second-order case"),
            ("p", "For `y″ + 3y′ + 2y = 0` with `y(0) = 1` and `y′(0) = 0` the right side is "
                  "`s·1 + 0 + 3·1 = s + 3`, and the left coefficient is "
                  "`s² + 3s + 2 = (s + 1)(s + 2)`. The forcing is zero, so nothing else "
                  "contributes."),
            ("math", [
                "(s² + 3s + 2)·Y = s + 3",
                "Y = (s + 3)/((s + 1)(s + 2))",
                "Y = A/(s + 1) + B/(s + 2)",
            ]),
            ("p", "To find `A`, multiply both sides by `s + 1` and set `s = −1`: "
                  "`A = (−1 + 3)/(−1 + 2) = 2`. To find `B`, multiply by `s + 2` and set "
                  "`s = −2`: `B = (−2 + 3)/(−2 + 1) = −1`. So "
                  "`Y = 2/(s + 1) − 1/(s + 2)`, and reading the table backwards "
                  "gives `y = 2e^(−t) − e^(−2t)`."),
            ("p", "This is the answer to the real-roots example in “Real Distinct Roots” "
                  "in Second-Order Linear Equations, found there by fitting two "
                  "constants from a 2×2 system. Here the starting values went in at the "
                  "first line and the constants came out of two substitutions."),
            ("h3", "When the denominator does not factor over the rationals"),
            ("p", "For `y″ + 2y′ + 5y = 0` with `y(0) = 0` and `y′(0) = 2` the right side is "
                  "`s·0 + 2 + 2·0 = 2` and the left coefficient is `s² + 2s + 5`, which has "
                  "no real roots. Complete the square: `s² + 2s + 5 = (s + 1)² + 4`. Then "
                  "`Y = 2/((s + 1)² + 4)`."),
            ("p", "The sine entry is `b/(s² + b²)`, and replacing `s` by `s + 1` multiplies the "
                  "signal by `e^(−t)`, as in the table's last entries. With `b = 2` the "
                  "numerator is already the `2` the entry needs, so "
                  "`y = e^(−t)·sin(2t)`. The lab checks this by transforming the answer back "
                  "and reading its residual in the original equation."),
            ("p", "Two limits of the lab, stated where they matter. A linear factor of the "
                  "denominator must have a rational root, so `s² − 2`, whose roots are "
                  "`±√2`, is refused with the factor named. An irreducible quadratic must "
                  "have a rational frequency, so `s² + 2`, whose inverse would carry "
                  "`cos(√2·t)`, is refused the same way rather than printed with a surd "
                  "inside a cosine. The mathematics is still fine in both cases; the lab "
                  "is limited."),
        ],
        "lab": ("dekit", {
            "mode": "laplace",
            "preset": "decay",
            "presets": [
                {"id": "decay", "label": "y″ + 3y′ + 2y = 0, y(0) = 1, y′(0) = 0", "kind": "solve",
                 "equation": "y'' + 3y' + 2y = 0", "ic": [1, 0],
                 "expect": {"lpY": "(s + 3)/((s + 1)(s + 2))", "lpPartial": "2/(s + 1) − 1/(s + 2)", "lpSolution": "2·e^(−t) − e^(−2t)", "lpCheck": "residual 0"}},
                {"id": "first-order", "label": "y′ + 2y = 6, y(0) = 0", "kind": "solve",
                 "equation": "y' + 2y = 6", "ic": [0],
                 "expect": {"lpF": "6/s", "lpY": "6/(s(s + 2))", "lpPartial": "3/s − 3/(s + 2)", "lpSolution": "3 − 3·e^(−2t)", "lpCheck": "residual 0"}},
                {"id": "damped", "label": "y″ + 2y′ + 5y = 0, y(0) = 0, y′(0) = 2", "kind": "solve",
                 "equation": "y'' + 2y' + 5y = 0", "ic": [0, 2],
                 "expect": {"lpPoles": "−1 ± 2i", "lpY": "2/((s + 1)² + 4)", "lpSolution": "e^(−t)·sin(2t)", "lpCheck": "residual 0"}},
            ],
            "panel_title": "Solve an initial value problem",
            "panel_intro": (
                "Pick an example and read the chain: Y(s), its partial fractions, the "
                "solution, and the residual of that solution in the original equation. "
                "Then type your own equation with a prime for each derivative, and its "
                "starting values in the order y(0), then y'(0)."),
        }),
        "steps_title": "Solving by transform",
        "steps_intro": "Transform, solve, decompose, invert, check. The check is the step that finds a slip in any of the others.",
        "steps": [
            ("Transform both sides",
             "Replace each derivative by its rule, with the starting values written in. "
             "Transform the forcing from the table."),
            ("Collect Y and solve",
             "Move every term that contains `Y` to the left and factor it out. Divide by the "
             "characteristic polynomial. `Y` is now a single fraction in `s`."),
            ("Decompose into table forms",
             "Factor the denominator. Write one term for each linear factor, and complete the "
             "square for a quadratic that does not factor. Find the coefficients by "
             "substituting the roots."),
            ("Read the table backwards",
             "Replace each fraction by the signal that has it as its transform, and add the "
             "signals."),
            ("Check by substitution",
             "Put the answer into the original equation and its starting values. The "
             "residual must be zero, and the answer must start where the problem says."),
        ],
        "worked": {
            "title": "y″ + 3y′ + 2y = 0 from y(0) = 1, y′(0) = 0",
            "intro": [
                "The first preset, solved by hand and then read against the lab.",
            ],
            "lines": [
                "(s²Y − s) + 3(sY − 1) + 2Y = 0",
                "(s² + 3s + 2)·Y = s + 3",
                "Y = (s + 3)/((s + 1)(s + 2))",
                "A = (−1 + 3)/(−1 + 2) = 2",
                "B = (−2 + 3)/(−2 + 1) = −1",
                "Y = 2/(s + 1) − 1/(s + 2)",
                "y = 2e^(−t) − e^(−2t)",
            ],
            "after": [
                "Check the starting values: `y(0) = 2 − 1 = 1` and "
                "`y′(0) = −2 + 2 = 0`. Check the equation: "
                "`y″ + 3y′ + 2y` has the `e^(−t)` coefficients `2 − 6 + 4 = 0` and "
                "the `e^(−2t)` coefficients `−4 + 6 − 2 = 0`. The lab reports "
                "the same residual.",
                "Notice what was not done. No general solution with two constants "
                "was written and no pair of equations for them was solved. The "
                "starting values were in the first line.",
            ],
        },
        "quiz_title": "Setting up and inverting",
        "quiz": [
            {"q": "Transforming `y′ + 2y = 6` with `y(0) = 0` gives which `Y(s)`?",
             "a": ["`6/(s + 2)`",
                   "`6/s + 2`",
                   "`6/(s·(s + 2))`",
                   "`(6/s)·(s + 2)`"],
             "c": 2,
             "why": "The transformed equation is `(s + 2)·Y = 6/s`, because the forcing `6` "
                    "transforms to `6/s`. Dividing by `s + 2` gives `6/(s·(s + 2))`. The "
                    "first choice transforms `6` as if it were the number `6`. The last "
                    "multiplies by `s + 2` where it should divide."},
            {"q": "For `y″ + 3y′ + 2y = 0` with `y(0) = 2` and `y′(0) = −1`, what is the right-hand side of `(s² + 3s + 2)·Y = …`?",
             "a": ["`2s − 1`",
                   "`2s + 5`",
                   "`s + 3`",
                   "`2s + 7`"],
             "c": 1,
             "why": "The right side is `a·(s·y(0) + y′(0)) + b·y(0) = (2s − 1) + 3·2 = 2s + 5`. "
                    "`2s − 1` leaves out the `b·y(0)` term from the first derivative. "
                    "`s + 3` belongs to the starting values `1` and `0`. The last adds `3·2` and "
                    "then `1` where the `−1` should have subtracted."},
            {"q": "What is the partial-fraction form of `6/(s·(s + 2))`?",
             "a": ["`3/s − 3/(s + 2)`",
                   "`3/s + 3/(s + 2)`",
                   "`6/s − 6/(s + 2)`",
                   "`2/s − 4/(s + 2)`"],
             "c": 0,
             "why": "At `s = 0` the coefficient is `6/2 = 3`, and at `s = −2` it is "
                    "`6/(−2) = −3`. Recombining, `3(s + 2) − 3s = 6`, as required. The "
                    "second choice has the wrong sign on the second term and recombines "
                    "to `3(2s + 2)`. The other two do not recombine to `6` either."},
            {"q": "Which signal has the transform `2/((s + 1)² + 4)`?",
             "a": ["`sin(2t)`",
                   "`e^(−t)·cos(2t)`",
                   "`e^(−t)·sin(2t)`",
                   "`2e^(−t)·sin(2t)`"],
             "c": 2,
             "why": "The sine entry with `b = 2` is `2/(s² + 4)`, and replacing `s` by `s + 1` "
                    "multiplies the signal by `e^(−t)`. `sin(2t)` alone would need `s²` in the "
                    "denominator, the cosine has `s + 1` in the numerator, and doubling the "
                    "signal doubles the numerator to `4`."},
        ],
        "mistakes": [
            ("Applying the initial conditions after inverting",
             "In the characteristic-equation method the constants are fitted at the end, and "
             "a reader carries that habit over by transforming the equation with the "
             "starting values left out. Then `(s² + 3s + 2)·Y = 0`, so `Y = 0`, and the "
             "answer is `y = 0`, which has `y(0) = 0` and not `1`. The starting values "
             "belong in the first line, inside the derivative rules, and nothing is "
             "left to fit afterward."),
            ("Dropping the b·y(0) term from the right side",
             "For `y″ + 3y′ + 2y = 0` the right side is `s + 3`, and the `3` comes from "
             "`3y′` contributing `3·y(0)`. Using `s` alone gives "
             "`Y = s/((s + 1)(s + 2)) = −1/(s + 1) + 2/(s + 2)` and "
             "`y = −e^(−t) + 2e^(−2t)`. That starts at `1` but has `y′(0) = 1 − 4 = −3`, "
             "not `0`, so the check on the second starting value fails."),
            ("Inverting the shifted sine without its exponential",
             "The shifted square means the signal decays: `y = e^(−t)·sin(2t)`. Reading "
             "the fraction as `sin(2t)` keeps the frequency and loses the decay, and "
             "the residual in `y″ + 2y′ + 5y` is `sin(2t) + 4cos(2t)`, not zero. The lab "
             "reports `residual 0` only for the form with `e^(−t)`."),
        ],
        "standard": (
            "Finish when you can solve a constant-coefficient initial value problem by transforming it, with no constants fitted at the end.",
            "You should be able to write the transformed equation with the starting "
            "values inside it, solve for Y(s), decompose it by substituting the roots, "
            "read the table backwards, and verify the answer by its two starting values "
            "and by substitution into the equation."),
        "note": 'The decomposition step carried most of the weight here, and three cases were enough for the examples. The next lesson takes it apart on its own, with repeated and irreducible factors.',
    },
]
