"""Differential Equations and Euler's Method -- the stepping half.

Euler's method as exact fractions, its error measured against the step size, the improved
method, Runge-Kutta, and the equation whose solution ceases to exist while the method keeps
stepping.

Every figure below is read off the kit -- scripts/mathpath/labs/dekit.py -- by executing its
shipped JavaScript under node, and each preset pins the tiles it exists to show. Figures that
are worked by hand in the prose (a single step, a one-step error) are arithmetic the reader
can repeat from the formula on the page, and are marked as hand arithmetic where they appear.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "eulers-method",
        "title": "Euler's Method",
        "module": "Stepping",
        "one_line": "The next value is this value plus the rate times the step, applied over and over in exact fractions, and it is a recipe near the solution and not the solution.",
        "summary": (
            "Euler's method is the sentence &ldquo;the next value is this value plus the rate "
            "times the step&rdquo;, written as a formula and repeated. Every value it produces is "
            "an exact fraction, and every one is a little off, because each step assumes the rate "
            "stays what it was at the start of the step. The fractions are right; the answer is "
            "only as close to the true solution as the step allows."
        ),
        "key": [
            "yₙ₊₁ = yₙ + h·f(tₙ, yₙ)",
            "tₙ₊₁ = tₙ + h;  slope read at the left end",
            "y′ = y, h = 1/4:  yₙ = (5/4)ⁿ exactly",
            "y₄ = 625/256 ≈ 2.44141,  e ≈ 2.71828",
            "the error belongs to the method",
        ],
        "key_label": "One step, repeated, in exact fractions",
        "concepts_intro": (
            "Three ideas: the step itself, what it assumes, and why a column of correct "
            "fractions is still not the solution."
        ),
        "concepts": [
            ("A step moves along the slope you are standing on",
             "At the point `(tₙ, yₙ)` the equation gives a slope, `f(tₙ, yₙ)`. Euler's method "
             "walks along that slope for a time `h`: the value rises by `h` times the slope, "
             "and `t` advances by `h`. Then it reads a new slope at the new point and does it "
             "again. Nothing else is involved, which is why the method needs no closed form "
             "and no cleverness, only arithmetic."),
            ("Each step assumes the rate stays what it was",
             "Inside a step the real slope changes, because it depends on `t` and on `y`, "
             "which are both moving. The method ignores that and uses the slope from the left "
             "end for the whole step. Where the rate is rising, as it is for `y′ = y` while "
             "`y` grows, the step undershoots; where it is falling, it overshoots. That "
             "assumption is the entire source of the error."),
            ("Exact fractions do not make the method exact",
             "With a rational start and a rational step, every `yₙ` is a fraction, and the lab "
             "prints it as one. That removes arithmetic error completely and leaves the "
             "method's error exactly where it was. A value such as `625/256` is a correct "
             "value of Euler's polygon and a rough value of the solution."),
        ],
        "read_title": "The method, a table of it, and what is wrong with it",
        "read_intro": "The formula, four steps on y′ = y worked out in full, the shortfall against e, an equation where the rate falls and then rises, and the difference between more steps and a smaller step.",
        "body": [
            ("p", "Euler's method is the sentence &ldquo;the next value is this value plus the rate "
                  "times the step&rdquo;, written as `yₙ₊₁ = yₙ + h·f(tₙ, yₙ)` and applied over and "
                  "over. On `y′ = y` from `y(0) = 1` with `h = 1/4` the first step is "
                  "`1 + (1/4)·1 = 5/4`, the second `5/4 + (1/4)·(5/4) = 25/16`, and after four "
                  "steps the lab prints `625/256`, which is `(5/4)⁴` exactly and is about `2.44`."),
            ("def", ("Euler's method",
                     "Given `y′ = f(t, y)`, a start `(t₀, y₀)` and a step `h`, Euler's method "
                     "produces `tₙ₊₁ = tₙ + h` and `yₙ₊₁ = yₙ + h·f(tₙ, yₙ)`. The values "
                     "`y₁, y₂, …` are joined by straight segments to form <strong>Euler's "
                     "polygon</strong>.",
                     "Each segment has the slope the equation gives at its <em>left</em> end. "
                     "The polygon is a recipe's output, and it is near the solution for "
                     "reasons the next lesson measures; it is not the solution.")),
            ("math", [
                "y′ = y,  y(0) = 1,  h = 1/4",
                "",
                "n    tₙ     yₙ         f(tₙ, yₙ) = yₙ    rule",
                "0    0      1          1                 start",
                "1    1/4    5/4        5/4               1 + (1/4)·1",
                "2    1/2    25/16      25/16             5/4 + (1/4)·(5/4)",
                "3    3/4    125/64     125/64            25/16 + (1/4)·(25/16)",
                "4    1      625/256    625/256           125/64 + (1/4)·(125/64)",
            ]),
            ("p", "Read the table. Because `f(t, y) = y`, the slope at each point is the value "
                  "itself, and each step multiplies the value by `1 + h = 5/4`. So every row is "
                  "a power of `5/4`, and `y₄ = (5/4)⁴ = 625/256`. That is a fact about the "
                  "recipe: it is the geometric sequence of Algebra's Sequences and Series, with "
                  "ratio `5/4`."),
            ("h3", "How far off it is"),
            ("p", "The true solution of `y′ = y` with `y(0) = 1` is `e^t`, and its value at "
                  "`t = 1` is `e ≈ 2.71828`, which is rounded: `e` is not a fraction, and the "
                  "lab prints it with `≈`. Beside it the lab prints `625/256 ≈ 2.44141`, also "
                  "rounded for reading, but the fraction is the exact value of the method. The "
                  "error it prints, `≈ 0.276876`, is rounded too, because it is a fraction "
                  "subtracted from an irrational number."),
            ("p", "None of that error comes from a slip in the arithmetic. Every step used the "
                  "slope at its left end, while the real slope was climbing as `y` grew, so "
                  "every step fell a little short and the shortfalls piled up. The polygon "
                  "lies below the curve for exactly that reason."),
            ("example", ("A rate that depends on t alone",
                         "Take `y′ = 2t` from `y(0) = 0` with `h = 1/4`. The slopes read at "
                         "`t = 0, 1/4, 1/2, 3/4` are `0, 1/2, 1, 3/2`, so the values are "
                         "`0, 0, 1/8, 3/8, 3/4`, and `y₄ = 3/4`. The true solution is `t²`, "
                         "which is `1` at `t = 1`, so the error is exactly `1/4`.",
                         "This is the left sum from Accumulation and the Integral: "
                         "`(1/4)·(0 + 1/2 + 1 + 3/2) = 3/4`. Euler's method on an equation "
                         "that does not mention `y` is exactly a left sum, and its shortfall "
                         "is the left sum's shortfall on a rising rate.")),
            ("h3", "A rate that falls, then rises"),
            ("p", "Now `y′ = t − y` from `y(0) = 2` with `h = 1/2`. The first slope is "
                  "`0 − 2 = −2`, so `y₁ = 2 + (1/2)·(−2) = 1`. The next slope is "
                  "`1/2 − 1 = −1/2`, so `y₂ = 1 + (1/2)·(−1/2) = 3/4`. The slope at "
                  "`(1, 3/4)` is `1/4`, so `y₃ = 3/4 + (1/2)·(1/4) = 7/8`, and the "
                  "fourth step gives `y₄ = 19/16`. The path falls and turns upward, as the "
                  "true solution `t − 1 + 3e^(−t)` does, and the true value at `t = 2` is "
                  "`1 + 3e^(−2) ≈ 1.40601`, rounded."),
            ("h3", "More steps, or a smaller step"),
            ("p", "The tempting remedy is more steps, and it needs care in what it means. "
                  "Four steps of `h = 1/4` end at `t = 1`. Eight steps of the same size end at "
                  "`t = 2`, a different place, and the error there is not comparable. What "
                  "reduces the error at `t = 1` is a smaller step with more of them: eight "
                  "steps of `h = 1/8` give `(9/8)⁸ = 43046721/16777216 ≈ 2.56578`, an error of "
                  "`≈ 0.152497`, which is better than `≈ 0.276876` and still not zero. "
                  "No step size makes the polygon the solution, and the next lesson measures "
                  "how the error falls as `h` does."),
        ],
        "lab": ("dekit", {
            "mode": "euler",
            "preset": "growth",
            "presets": [
                {"id": "growth", "label": "y' = y from (0, 1), h = 1/4, 4 steps",
                 "f": "y", "t0": 0, "y0": 1, "h": "1/4", "n": 4, "exact": "e^t",
                 "expect": {"euLast": "625/256", "euError": "≈ 0.276876"}},
                {"id": "ramp", "label": "y' = 2t from (0, 0), h = 1/4, 4 steps",
                 "f": "2t", "t0": 0, "y0": 0, "h": "1/4", "n": 4, "exact": "t^2",
                 "expect": {"euLast": "3/4", "euError": "1/4"}},
                {"id": "mixed", "label": "y' = t - y from (0, 2), h = 1/2, 4 steps",
                 "f": "t - y", "t0": 0, "y0": 2, "h": "1/2", "n": 4, "exact": "t - 1 + 3e^(-t)",
                 "expect": {"euLast": "19/16", "euError": "≈ 0.218506"}},
                {"id": "finer", "label": "y' = y from (0, 1), h = 1/8, 8 steps",
                 "f": "y", "t0": 0, "y0": 1, "h": "1/8", "n": 8, "exact": "e^t",
                 "expect": {"euLast": "43046721/16777216", "euError": "≈ 0.152497"}},
            ],
            "panel_title": "Take the steps and read the table",
            "panel_intro": (
                "Pick each preset and read the last value, which is an exact fraction, and the "
                "error, which is exact when the known solution is rational at the end and "
                "rounded otherwise. Then change the step: set h to 1/8 and the steps to 8 on "
                "the first equation, and watch the error fall without reaching zero."
            ),
        }),
        "steps_title": "Taking an Euler step by hand",
        "steps_intro": "The same five moves at every step.",
        "steps": [
            ("Write the equation, the start and the step",
             "State `f(t, y)`, the point `(t₀, y₀)` and `h`. Make `h` a fraction so every "
             "later value stays one."),
            ("Read the slope at the left end",
             "Put the current `tₙ` and `yₙ` into `f`. This is the number the whole step will "
             "use, whatever the real slope does later in the step."),
            ("Multiply by h and add",
             "`yₙ₊₁ = yₙ + h·f(tₙ, yₙ)`. Keep the result as a fraction; do not round it."),
            ("Advance t by h and repeat",
             "`tₙ₊₁ = tₙ + h`. Take the next slope from the new point, not from the old one."),
            ("Compare with a known solution if there is one",
             "The gap `|yₙ − y(tₙ)|` is the error for this step size. Say which tier it is in: "
             "exact when `y(tₙ)` is rational, rounded with `≈` when it is not."),
        ],
        "worked": {
            "title": "y′ = y from y(0) = 1, four steps of 1/4",
            "intro": [
                "Compute `y₁`, `y₂`, `y₃` and `y₄` by hand, then compare with the true value "
                "at `t = 1`.",
            ],
            "lines": [
                "f(t, y) = y,  h = 1/4,  y₀ = 1",
                "",
                "y₁ = 1 + (1/4)·1             = 5/4",
                "y₂ = 5/4 + (1/4)·(5/4)       = 25/16",
                "y₃ = 25/16 + (1/4)·(25/16)   = 125/64",
                "y₄ = 125/64 + (1/4)·(125/64) = 625/256",
                "",
                "each step multiplies by 1 + h = 5/4: y₄ = (5/4)⁴",
                "true y(1) = e ≈ 2.71828; error ≈ 0.276876 (rounded)",
            ],
            "after": [
                "Each step multiplied the value by `5/4`, because the slope equals the value "
                "and `1 + h·1 = 5/4`. The true solution grows by more than that in each "
                "quarter of a unit of `t`, since its slope keeps rising inside the step, and "
                "the polygon never catches up.",
                "For a rehearsal, take `y′ = 2y` from `y(0) = 1` with `h = 1/2`: every step "
                "multiplies by `1 + 2·(1/2) = 2`, so `y₁ = 2` and `y₂ = 4`. The true value at "
                "`t = 1` is `e² ≈ 7.38906`, rounded.",
            ],
        },
        "quiz_title": "Steps, slopes and what they give",
        "quiz": [
            {"q": "For `y′ = y` with `y(0) = 1` and `h = 1/4`, what is `y₂`?",
             "a": ["`3/2`, adding `1/4` of the first slope twice",
                   "`21/16`, adding the new slope to the old value",
                   "`25/16`, which is `5/4 + (1/4)·(5/4)`",
                   "`5/4`, because the second step adds nothing"],
             "c": 2,
             "why": "The second step uses the slope at `(1/4, 5/4)`, which is `5/4`, so "
                    "`y₂ = 5/4 + (1/4)·(5/4) = 25/16`. The value `3/2` keeps using the "
                    "first slope, `21/16` mixes the first value with the second slope, and "
                    "`5/4` is just `y₁`."},
            {"q": "On `y′ = 2t` from `(0, 0)` with `h = 1/4`, four steps give `3/4`, and the true `y(1)` is `1`. What does the gap of `1/4` show?",
             "a": ["The arithmetic slipped somewhere and should be redone",
                   "The error belongs to the method: each step used the rate at its start while the rate was rising",
                   "The lab rounds `1` down to `3/4`",
                   "The error would vanish if the fractions were carried to more digits"],
             "c": 1,
             "why": "Every value in the table is an exact fraction, so no digits are lost. The "
                    "gap exists because the rate `2t` rises through each step and the method "
                    "used its starting value. More digits change nothing, and the lab does "
                    "no rounding here."},
            {"q": "For `y′ = y` from `(0, 1)`, which change moves the final value at `t = 1` closer to `e`?",
             "a": ["Four more steps of `h = 1/4`, which end at `t = 2`",
                   "Printing `625/256` with more decimal places",
                   "Using the slope at the right end of the first step only",
                   "Eight steps of `h = 1/8`, which still end at `t = 1`"],
             "c": 3,
             "why": "A smaller step with proportionally more steps keeps the end at `t = 1` "
                    "and shrinks the assumption each step makes. Extra steps of the same size "
                    "move the end point and answer a different question, and more decimals "
                    "of the same fraction change nothing."},
            {"q": "For `y′ = t − y` from `(0, 2)` with `h = 1/2`, what is `y₁`?",
             "a": ["`1`, because the slope at the start is `−2`",
                   "`3`, because the slope at the start is `2`",
                   "`2`, because the slope at the start is `0`",
                   "`5/4`, because the slope is read at `t = 1/2` with `y = 2`"],
             "c": 0,
             "why": "The slope at `(0, 2)` is `0 − 2 = −2`, so `y₁ = 2 + (1/2)·(−2) = 1`. A "
                    "slope of `+2` is a sign slip, a slope of `0` forgets the `−y`, and "
                    "`5/4` reads the slope at the wrong end of the step, which is a different "
                    "method."},
        ],
        "mistakes": [
            ("Expecting Euler's method to give the solution, and more steps to make it exact",
             "The column `5/4, 25/16, 125/64, 625/256` is exactly Euler's polygon, and its "
             "last value is short of `e` by `≈ 0.276876`. Halving the step and doubling the "
             "steps gives `43046721/16777216`, short by `≈ 0.152497`: closer, and not "
             "there. Taking more steps of the same size does not even keep the same end point."),
            ("Calling an exact fraction the exact answer",
             "`625/256` is the exact value of the method, and the fraction being exact says "
             "nothing about the solution. The lab prints the true value separately, rounded "
             "and marked `≈`, so the two tiers stay apart."),
            ("Reading the slope at the end of the step",
             "The formula uses `f(tₙ, yₙ)`, the slope where the step begins. Using the slope "
             "at the new point means `yₙ₊₁` appears on both sides, which is a different "
             "method that needs an equation solved at every step."),
        ],
        "standard": ("Finish when you can carry out three Euler steps as exact fractions and say what the method assumes.",
                     "You should be able to compute `y₁`, `y₂` and `y₃` from `f`, a start and "
                     "a step, keep each as a fraction, compare the last with a known solution "
                     "and say whether the error is exact or rounded, and state in one sentence "
                     "what each step assumes about the rate."),
        "note": 'One step size gives one error. How the error depends on the step is the next question: a smaller step helps, and the right thing to ask is by how much. &ldquo;Euler&rsquo;s Error and the Step Size&rdquo; measures it with exact ratios.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "eulers-error-and-the-step-size",
        "title": "Euler's Error and the Step Size",
        "module": "Stepping",
        "one_line": "Measure the error at three step sizes, form the exact ratios, and read the order: halving the step roughly halves Euler's error, and on y′ = 2t exactly.",
        "summary": (
            "The error of Euler's method at a fixed end time is the accumulation of every "
            "step's small error, and it shrinks in proportion to the step. Halve `h` and the "
            "error is about halved, which the lab shows as a ratio near 2 and names first "
            "order. On one equation the ratio is exactly 2; on the others it only approaches "
            "2, and the lesson says which is which."
        ),
        "key": [
            "E(h) = |y_N − y(T)|,  N = (T − t₀)/h",
            "y′ = 2t:  E(h) = h exactly",
            "one step errs h²;  N steps total N·h² = h",
            "halve h: the ratio of errors approaches 2",
            "ratio 2 means first order",
        ],
        "key_label": "The error at a fixed time, and what its ratio says",
        "concepts_intro": (
            "Three ideas: what is being measured, where the total comes from, and how a "
            "ratio of errors names the order."
        ),
        "concepts": [
            ("The error is measured at a fixed end time",
             "To compare step sizes, fix an end time `T` and ask for `E(h) = |y_N − y(T)|`, "
             "where `N = (T − t₀)/h` steps are needed to arrive. A smaller `h` takes more "
             "steps to reach the same `T`, and that is what makes the three errors "
             "comparable. An error at the end of four steps and an error at the end of eight "
             "of the same size are errors at two different times."),
            ("The error is the accumulation of every step, not the last one",
             "Each step starts a little off and adds a little more. On `y′ = 2t` one step of "
             "size `h` from `t` misses by exactly `h²`, and there are `1/h` of them, so the "
             "error at `T = 1` is `h²·(1/h) = h`. The last step contributes one of those "
             "pieces and no more."),
            ("The ratio of successive errors names the order",
             "If the error is about `C·h`, halving `h` halves it, and `E(h)/E(h/2)` is near "
             "`2`. If it were about `C·h²` the ratio would be near `4`. The order is the "
             "power: `log₂` of the ratio. A ratio is read from two errors, and the lab forms "
             "two ratios from three, so one can check the other."),
        ],
        "read_title": "From one error to an order",
        "read_intro": "The measurement, the one equation where Euler's error is exactly h, why the total is a sum of equal pieces, two equations where the ratio only approaches 2, and a rounded case.",
        "body": [
            ("p", "The lab runs Euler's method three times on one equation, with step sizes "
                  "`h`, `h/2` and `h/4`, to the same end time `T = 1`. For each it prints the "
                  "error `E(h)` against the known solution, then the two ratios "
                  "`E(h)/E(h/2)` and `E(h/2)/E(h/4)`, and the order those ratios imply."),
            ("math", [
                "y′ = 2t,  y(0) = 0,  exact y = t²,  T = 1",
                "",
                "h       N     y_N       y(1)    E(h)",
                "1/4     4     3/4       1       1/4",
                "1/8     8     7/8       1       1/8",
                "1/16    16    15/16     1       1/16",
                "",
                "ratios  E(1/4)/E(1/8) = 2,   E(1/8)/E(1/16) = 2",
            ]),
            ("p", "On this equation the error is exactly `h`: `E(1/4) = 1/4`, `E(1/8) = 1/8`, "
                  "`E(1/16) = 1/16`. Euler's method on `y′ = 2t` is a left sum, and the left "
                  "sum of `2t` over `N` pieces from `t = 0` to `t = 1` is `h²·N·(N − 1) = 1 − h`, which "
                  "differs from `1` by exactly `h`. Both ratios are exactly `2`, the order is "
                  "`1`, and here that is not an approximation."),
            ("h3", "Where the total comes from"),
            ("p", "Look at one step. The true solution `t²` moves from `t²` to `(t + h)²`, a rise "
                  "of `2th + h²`. Euler's step rises by `h·2t`. The difference is `h²`, whatever "
                  "`t` is, so every step falls short by the same `h²`. With `N = 1/h` steps the "
                  "total is `(1/h)·h² = h`. At `h = 1/4` each of the four steps misses by "
                  "`1/16`, and the four add to `1/4`."),
            ("thm", ("Euler's method is first order",
                     "For a right-hand side with continuous first derivatives, Euler's error "
                     "at a fixed `T` is approximately `C·h` for a constant `C` that depends on "
                     "the equation and `T` but not on `h`. Halving `h` therefore halves the "
                     "error, and the ratio `E(h)/E(h/2)` approaches `2`.")),
            ("p", "The lab demonstrates the claim on chosen equations by exact ratios, and "
                  "does not prove it for every equation. On an equation where `f` also depends "
                  "on `y`, an early error is carried forward by the later steps, which changes "
                  "the constant `C` and not the power of `h`."),
            ("h3", "When the ratio only approaches 2"),
            ("p", "Take `y′ = t²`, with exact solution `t³/3`. Euler's method is again a left "
                  "sum, and the lab prints the errors `11/96`, `23/384` and `47/1536`. The "
                  "ratios are `44/23 ≈ 1.91304` and `92/47 ≈ 1.95745`, both rounded here, and "
                  "the order tile reads `≈ 0.968973`, also rounded. The ratios are close to "
                  "`2` and not equal to it."),
            ("p", "The reason can be read off the numbers. For this equation the error is "
                  "exactly `h/2 − h²/6`: at `h = 1/4` that is `1/8 − 1/96 = 11/96`. The "
                  "first term halves exactly when `h` does. The second term is four times "
                  "smaller after each halving, so it falls faster, and its effect on the ratio "
                  "fades: the ratio stays below `2` and climbs towards it as `h` falls."),
            ("example", ("An error that is itself rounded",
                         "On `y′ = y` with exact solution `e^t`, the true value `e` is not a "
                         "fraction, so the lab cannot subtract exactly. Each error is printed "
                         "rounded with `≈`, the two ratios are rounded, and the order is "
                         "rounded.",
                         "That is the exactness rule at work: Euler's values `(1 + h)ⁿ` are "
                         "exact, the true value is not, and the lab says so in every tile "
                         "where the two meet.")),
        ],
        "lab": ("dekit", {
            "mode": "order",
            "method": "euler",
            "preset": "ramp",
            "presets": [
                {"id": "ramp", "label": "y' = 2t, exact t^2, to T = 1",
                 "f": "2t", "t0": 0, "y0": 0, "T": 1, "exact": "t^2", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "1/4", "odRatio": "2, 2", "odOrder": "1"}},
                {"id": "square", "label": "y' = t^2, exact t^3/3, to T = 1",
                 "f": "t^2", "t0": 0, "y0": 0, "T": 1, "exact": "t^3/3", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "11/96", "odRatio": "44/23, 92/47", "odOrder": "≈ 0.968973"}},
                {"id": "growth", "label": "y' = y, exact e^t, to T = 1",
                 "f": "y", "t0": 0, "y0": 1, "T": 1, "exact": "e^t", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "≈ 0.276876", "odRatio": "≈ 1.81561, ≈ 1.89783", "odOrder": "≈ 0.924354"}},
            ],
            "panel_title": "Three step sizes, two ratios, one order",
            "panel_intro": (
                "Each preset runs Euler's method to T = 1 with h = 1/4, 1/8 and 1/16. Read the "
                "three errors, then the ratios, and say before you look whether the ratio will "
                "be exactly 2. Then type your own right-hand side, such as 3t^2, and a matching "
                "exact solution, t^3, and predict the first error."
            ),
        }),
        "steps_title": "Measuring an error and reading an order",
        "steps_intro": "From an equation with a known solution to a number you can state.",
        "steps": [
            ("Choose the end time and three step sizes",
             "Pick `T` and `h, h/2, h/4` so that `(T − t₀)/h` is a whole number of steps for "
             "each. Every error is then an error at the same `T`."),
            ("Run the method and subtract the true value",
             "Compute `y_N` for each step size and the gap `|y_N − y(T)|`. Keep the gap exact "
             "when the true value at `T` is rational and mark it `≈` when it is not."),
            ("Form the two ratios",
             "Divide each error by the next: `E(h)/E(h/2)` and `E(h/2)/E(h/4)`. Two ratios "
             "that agree are better evidence than one."),
            ("Read the order from the last ratio",
             "A ratio of `2` is first order, `4` second, `16` fourth. A ratio near but not "
             "equal to a power of two is read as approaching it, and the order is `log₂` of "
             "the ratio."),
        ],
        "worked": {
            "title": "Why the error on y′ = 2t is exactly h",
            "intro": [
                "Find the error of one Euler step on `y′ = 2t`, add the steps, and check the "
                "total against the lab.",
            ],
            "lines": [
                "exact y = t²;  Euler step from (t, t²):",
                "   true rise    (t + h)² − t² = 2th + h²",
                "   Euler rise   h·2t          = 2th",
                "   one step misses by h², for every t",
                "",
                "T = 1 needs N steps with N·h = 1:  E(h) = N·h² = h",
                "",
                "h = 1/4:  4·(1/16)   = 1/4",
                "h = 1/8:  8·(1/64)   = 1/8",
                "h = 1/16: 16·(1/256) = 1/16",
                "ratios:  (1/4)/(1/8) = 2,  (1/8)/(1/16) = 2",
            ],
            "after": [
                "The three errors agree with the lab. The shortfall of a single step is "
                "`h²`, a tiny number, and it is the number of steps that turns it into an "
                "error of size `h`: halving `h` quarters each piece and doubles the number of "
                "pieces, which halves the total.",
                "For a rehearsal, run `h = 1/10` by the same formula: ten steps of `1/100` "
                "give `1/10`.",
            ],
        },
        "quiz_title": "Error, ratio and order",
        "quiz": [
            {"q": "On `y′ = 2t` from `(0, 0)`, Euler's method with `h = 1/10` runs to `T = 1`. What is the error, by the formula of this lesson?",
             "a": ["`1/100`, the error of one step",
                   "`1/10`, ten steps of `1/100`",
                   "`1/20`, half of the step",
                   "`0`, because the right side is simple"],
             "c": 1,
             "why": "Each step misses by `h² = 1/100` and there are ten, so `E = 1/10 = h`. "
                    "The figure `1/100` is a single step's error, which is the mistake the "
                    "lesson names, and a simple right side does not make the method exact."},
            {"q": "The lab prints the ratios `2, 2`. What order does that name?",
             "a": ["Order 1, because `log₂ 2 = 1`",
                   "Order 2, because the ratio is `2`",
                   "Order 0, because the ratio is not larger than `2`",
                   "No order can be named from two ratios"],
             "c": 0,
             "why": "If halving `h` halves the error, the error is proportional to `h` to the "
                    "first power, and `log₂` of the ratio is `1`. Order 2 would need a ratio "
                    "of `4`, and two agreeing ratios are exactly what is needed."},
            {"q": "On `y′ = t²` the second ratio is `92/47`, not `2`. Why?",
             "a": ["The lab rounds the errors",
                   "Euler's method is second order on this equation",
                   "The error is `h/2 − h²/6`, whose second term falls faster than the first, so the ratio climbs towards `2` without equalling it",
                   "The known solution is irrational"],
             "c": 2,
             "why": "The errors `11/96`, `23/384`, `47/1536` are exact, so nothing is rounded, "
                    "and `t³/3` is rational at `T = 1`. A ratio below `2` and rising is what a "
                    "leading term `h/2` with a smaller correction gives; second order would "
                    "put the ratio near `4`."},
            {"q": "At `h = 1/4` on `y′ = 2t` the last of the four steps misses by `1/16`. What is the total error at `T = 1`?",
             "a": ["`1/16`, since the last step is the error",
                   "`1/64`",
                   "`1/2`",
                   "`1/4`, because all four steps miss by `1/16` each"],
             "c": 3,
             "why": "Every step misses by the same `h² = 1/16` and the errors add: "
                    "`4·(1/16) = 1/4`. Taking the last step's miss as the error discards "
                    "three quarters of it."},
        ],
        "mistakes": [
            ("Taking the error to be the error of the last step",
             "On `y′ = 2t` with `h = 1/4`, the last step misses by `1/16`, and the lab's "
             "error is `1/4`: four equal pieces, one from each step. The error at `T` is "
             "whatever has accumulated from the start to there, and each step's miss sits "
             "inside every later value."),
            ("Expecting every ratio to be exactly 2",
             "Only `y′ = 2t` gives `2, 2`. On `y′ = t²` the ratios are `44/23` and `92/47`, "
             "below `2` and rising, and on `y′ = y` they are rounded. The claim is that they "
             "approach `2`, and where they are exactly `2` the lesson has shown why."),
            ("Naming the order from a single error",
             "An error of `1/4` means nothing by itself, since it depends on `T`, on the "
             "equation and on the step. The order is how the error changes when the step "
             "does, and that takes at least two errors and their ratio."),
        ],
        "standard": ("Finish when you can measure Euler's error at three step sizes, form the ratios and state the order.",
                     "You should be able to run the method to a fixed `T` with `h`, `h/2` and "
                     "`h/4`, subtract the true value, divide successive errors, and say that a "
                     "ratio near `2` means first order. You should also be able to explain, "
                     "for `y′ = 2t`, why the total error is `h` and not the error of one step."),
        "note": 'First order is slow: to halve the error you must double the work. A cheap change to the step itself does better, and it uses a second slope. &ldquo;The Improved Euler Method&rdquo; shows the error quartering instead.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-improved-euler-method",
        "title": "The Improved Euler Method",
        "module": "Stepping",
        "one_line": "Take a trial Euler step, average the slopes at both ends, and the error quarters when the step halves, exactly so on y′ = t².",
        "summary": (
            "Euler's method uses the slope at the start of a step. The improved method also "
            "asks what the slope would be at the end, using a trial Euler step to get there, "
            "and moves along the average of the two. That costs two slope readings per step "
            "and changes the order: halving `h` now divides the error by about 4, and on "
            "`y′ = t²` by exactly 4."
        ),
        "key": [
            "k₁ = f(tₙ, yₙ)   slope at the start",
            "k₂ = f(tₙ + h, yₙ + h·k₁)   trial slope",
            "yₙ₊₁ = yₙ + h·(k₁ + k₂)/2",
            "y′ = t²: the step is the trapezoid rule",
            "halve h: error ÷ 4, here exactly 4",
        ],
        "key_label": "A trial step, two slopes, one average",
        "concepts_intro": (
            "Three ideas: the trial step, why averaging helps, and what the order of the "
            "method is."
        ),
        "concepts": [
            ("A trial step finds the slope at the other end",
             "Euler's method reads the slope only where the step begins. The improved method "
             "takes an ordinary Euler step first, to a trial point `(tₙ + h, yₙ + h·k₁)`, and "
             "reads the slope `k₂` there. The trial value is only a guess at where the step "
             "would end, and it is used for nothing except that slope."),
            ("The average of the two slopes is a better rate for the step",
             "The true slope changes through a step, and the start slope is too low where "
             "the rate rises and too high where it falls. The slope at the end is wrong the "
             "other way. Their average, `(k₁ + k₂)/2`, is a better stand-in for the whole "
             "step. When `f` depends on `t` alone this is exactly the trapezoid rule from "
             "Accumulation and the Integral."),
            ("The order is 2: halving the step quarters the error",
             "The error at a fixed `T` is about `C·h²`, so halving `h` divides it by "
             "`4` and the ratio of successive errors is near `4`. A ratio of `4` names order "
             "`2`. This is not a halved error: it is a different power of `h`, and for a "
             "small step it is a much smaller error."),
        ],
        "read_title": "Two slopes instead of one",
        "read_intro": "The method, one step of it by hand, the equation where it is the trapezoid rule and its error is exactly proportional to h squared, an equation where the ratio only approaches 4, and the misreading of what second order means.",
        "body": [
            ("def", ("The improved Euler method",
                     "From `(tₙ, yₙ)` with step `h`: `k₁ = f(tₙ, yₙ)`, then "
                     "`k₂ = f(tₙ + h, yₙ + h·k₁)`, then `yₙ₊₁ = yₙ + h·(k₁ + k₂)/2`.",
                     "Two slopes are read per step, so each step costs twice what an "
                     "Euler step costs. The method is also called Heun's method.")),
            ("p", "Do one step by hand on `y′ = y` from `y(0) = 1` with `h = 1/4`. The start "
                  "slope is `k₁ = 1`. The trial value is `1 + (1/4)·1 = 5/4`, so `k₂ = 5/4`. "
                  "The average slope is `(1 + 5/4)/2 = 9/8`, and `y₁ = 1 + (1/4)·(9/8) = 41/32`. "
                  "This is hand arithmetic from the formula; set `T` to `1/4` in the lab on "
                  "`y′ = y` and the first row of its table reads `41/32`. Plain Euler gave "
                  "`5/4 = 40/32` for the same step, and `e^(1/4) ≈ 1.28403`, rounded, is nearer "
                  "to `41/32 = 1.28125`."),
            ("h3", "The equation where the step is the trapezoid rule"),
            ("p", "Take `y′ = t²`. The right side does not mention `y`, so the trial value "
                  "never matters: `k₁ = tₙ²` and `k₂ = (tₙ + h)²`, and the step adds "
                  "`h·(tₙ² + (tₙ + h)²)/2`. That is the trapezoid rule on one piece. Its "
                  "error on a quadratic is exactly proportional to `h²`, because the rule's "
                  "error is `h²·(f′(b) − f′(a))/12` and for `f = t²` that is `h²·2/12 = h²/6`."),
            ("math", [
                "y′ = t²,  y(0) = 0,  exact y = t³/3,  T = 1",
                "",
                "h       E(h) = h²/6    ratio to the next",
                "1/4     1/96           4",
                "1/8     1/384          4",
                "1/16    1/1536",
            ]),
            ("p", "The lab prints exactly these errors and the ratios `4, 4`, and names the "
                  "order `2`. Compare Euler on the same equation at the same `h = 1/4`: its "
                  "error is `11/96`, eleven times larger. Switch the Method menu to Euler to "
                  "see `11/96, 23/384, 47/1536` appear in place of these."),
            ("thm", ("The improved method is second order",
                     "For a right-hand side with continuous second derivatives, the improved "
                     "method's error at a fixed `T` is approximately `C·h²`, so halving `h` "
                     "divides it by about `4`.")),
            ("p", "As with first order in the previous lesson, the lab demonstrates this on "
                  "chosen equations by exact ratios and does not prove it in general."),
            ("h3", "When the ratio is near 4 and is not 4"),
            ("p", "Change the equation to `y′ = t⁴`, with exact solution `t⁵/5`. The errors "
                  "are `53/2560`, `213/40960` and `853/655360`, and the ratios are "
                  "`848/213 ≈ 3.98122` and `3408/853 ≈ 3.99531`, both rounded here. They climb "
                  "towards `4` and are not `4`, because the trapezoid error has a smaller "
                  "term in `h⁴` as well. On a cubic the exactness comes back: the error of "
                  "the rule is `h²·(f′(b) − f′(a))/12` with no further terms, and for "
                  "`y′ = t³` that is `h²/4`, so typing `t^3` and `t^4/4` into the lab gives "
                  "`1/64, 1/256, 1/1024`, with ratio `4` twice."),
            ("example", ("Second order is not half the error",
                         "At `h = 1/4` on `y′ = t²` Euler's error is `11/96` and the improved "
                         "method's is `1/96`: eleven times smaller, not half. For an equal "
                         "number of slope readings Euler with `h = 1/8` (eight readings) has "
                         "error `23/384`, and the improved method with `h = 1/4` (four steps "
                         "of two readings, eight in all) has `1/96 = 4/384`, nearly six times "
                         "smaller.",
                         "The comparison keeps growing in the improved method's favour as the "
                         "step shrinks, because its error falls by `4` each halving and "
                         "Euler's falls by `2`.")),
            ("p", "The lab's third preset runs the improved method on `y′ = y`. The true "
                  "value is irrational, so the errors, ratios and order are all rounded, "
                  "and the lab marks them with `≈`."),
        ],
        "lab": ("dekit", {
            "mode": "order",
            "method": "heun",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "y' = t^2, exact t^3/3, to T = 1",
                 "f": "t^2", "t0": 0, "y0": 0, "T": 1, "exact": "t^3/3", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "1/96", "odRatio": "4, 4", "odOrder": "2"}},
                {"id": "quartic", "label": "y' = t^4, exact t^5/5, to T = 1",
                 "f": "t^4", "t0": 0, "y0": 0, "T": 1, "exact": "t^5/5", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "53/2560", "odRatio": "848/213, 3408/853", "odOrder": "≈ 1.99831"}},
                {"id": "growth", "label": "y' = y, exact e^t, to T = 1",
                 "f": "y", "t0": 0, "y0": 1, "T": 1, "exact": "e^t", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "≈ 0.0234261", "odRatio": "≈ 3.63727, ≈ 3.81482", "odOrder": "≈ 1.93162"}},
            ],
            "panel_title": "Check that the error quarters",
            "panel_intro": (
                "The method menu is set to the improved method. Read the errors and the "
                "ratios for each preset, and say before you look which one will give exactly 4. "
                "Then switch the menu to Euler and compare the first error with the improved "
                "method's on the same equation."
            ),
        }),
        "steps_title": "One improved step, and one check of its order",
        "steps_intro": "Two slopes, an average, and then the usual measurement.",
        "steps": [
            ("Read the start slope",
             "`k₁ = f(tₙ, yₙ)`, exactly as in Euler's method."),
            ("Take the trial step and read the slope there",
             "Move to `(tₙ + h, yₙ + h·k₁)` and compute `k₂ = f` at that point. The trial "
             "value is used only to get `k₂`."),
            ("Average the slopes and take the real step",
             "`yₙ₊₁ = yₙ + h·(k₁ + k₂)/2`. Keep it as a fraction."),
            ("Measure the error at three step sizes",
             "Run to the same `T` with `h`, `h/2`, `h/4`, subtract the true value and divide "
             "successive errors."),
            ("Read the order from the ratio",
             "A ratio of `4` is second order. State whether it is exactly `4` or only "
             "approaching it."),
        ],
        "worked": {
            "title": "The error of the improved method on y′ = t²",
            "intro": [
                "Show that the improved step on `y′ = t²` is the trapezoid rule, and that its "
                "error is exactly proportional to `h²`.",
            ],
            "lines": [
                "f depends on t only:  k₁ = t²,  k₂ = (t + h)²",
                "step adds  h·(t² + (t + h)²)/2   (trapezoid)",
                "",
                "true rise over a step: ((t + h)³ − t³)/3",
                "   = t²·h + t·h² + h³/3",
                "step rise = h·(2t² + 2th + h²)/2",
                "   = t²·h + t·h² + h³/2",
                "one step overshoots by h³/2 − h³/3 = h³/6",
                "",
                "N steps with N·h = 1:  N·h³/6 = h²/6",
                "h = 1/4: 1/96;  h = 1/8: 1/384;  h = 1/16: 1/1536",
            ],
            "after": [
                "Each step overshoots the true rise by exactly `h³/6`, the same at every "
                "`t`, because the quadratic leaves no `t` in the difference. Adding `1/h` "
                "of them gives `h²/6`, and halving `h` divides that by exactly `4`.",
                "The lab's errors `1/96`, `1/384`, `1/1536` match. The lab reports the size "
                "of the error, so the sign, an overshoot here, does not enter the ratio.",
            ],
        },
        "quiz_title": "Two slopes, one average",
        "quiz": [
            {"q": "On `y′ = t²` from `(0, 0)` with `h = 1/2`, what does the improved method give for `y₁`?",
             "a": ["`0`, since the slope at the start is `0`",
                   "`1/8`, using only the slope at the end",
                   "`1/16`, the average slope `1/8` times `h`",
                   "`1/4`, the slope at the end"],
             "c": 2,
             "why": "Here `k₁ = 0` and `k₂ = (1/2)² = 1/4`, so the average slope is `1/8` and "
                    "`y₁ = (1/2)·(1/8) = 1/16`. Zero is plain Euler's value, `1/8` multiplies "
                    "the end slope by `h` without averaging, and `1/4` is the end slope "
                    "itself."},
            {"q": "The lab prints the ratios `4, 4` for the improved method. What does that say about halving `h`?",
             "a": ["It divides the error by `4` and the method is second order",
                   "It halves the error and the method is first order",
                   "It divides the error by `2` twice",
                   "It leaves the error unchanged"],
             "c": 0,
             "why": "A ratio of `4` is `2²`, so the error is proportional to `h²`. Half the "
                    "error is a ratio of `2`, which belongs to Euler's method."},
            {"q": "At `h = 1/4` on `y′ = t²`, Euler's error is `11/96` and the improved method's is `1/96`. Which description is right?",
             "a": ["The improved error is half of Euler's",
                   "The two methods agree to two figures",
                   "The improved error is one quarter of Euler's",
                   "The improved error is one eleventh of Euler's, and it falls faster as `h` does"],
             "c": 3,
             "why": "`(11/96)/(1/96) = 11`. Second order does not mean half the error: the "
                    "gap is a factor of `11` at this step and widens as `h` falls, because "
                    "one error is divided by `4` per halving and the other by `2`."},
            {"q": "On `y′ = t⁴` the lab prints the ratios `848/213` and `3408/853`, not `4`. What is the right reading?",
             "a": ["The method is first order on this equation",
                   "The lab has a rounding fault",
                   "The ratios approach `4`: the error is near `C·h²` with a smaller correction, unlike the quadratic, where it is exact",
                   "The ratios show the order is `3`"],
             "c": 2,
             "why": "`848/213 ≈ 3.98` and `3408/853 ≈ 3.995` are close to `4` and rising. The "
                    "errors are exact fractions, so rounding is not the cause. Order `1` "
                    "would give `2`, order `3` would give `8`."},
        ],
        "mistakes": [
            ("Believing a second-order method has half the error of a first-order one",
             "Order is about how the error changes with `h`, not how large it is at one "
             "`h`. On `y′ = t²` the improved error at `h = 1/4` is `1/96` against Euler's "
             "`11/96`, eleven times smaller, and halving `h` quarters one error and halves "
             "the other."),
            ("Using the trial value as the answer",
             "The trial point `yₙ + h·k₁` is Euler's step, and it is used only to read `k₂`. "
             "The value that is kept is `yₙ + h·(k₁ + k₂)/2`. On `y′ = y` the trial value is "
             "`5/4` and the kept value is `41/32`."),
            ("Expecting the ratio to be 4 on every equation",
             "It is exactly `4` on `y′ = t²` and on a cubic, and only approaches `4` on "
             "`y′ = t⁴` and on `y′ = y`. The claim of second order is the approach, and "
             "the exactness on a quadratic is a feature of that equation."),
        ],
        "standard": ("Finish when you can take an improved Euler step and show the error quarters when the step halves.",
                     "You should be able to compute `k₁`, the trial value, `k₂` and the "
                     "step for a given equation, run the lab at three step sizes, read the "
                     "ratio of successive errors as `4`, and say on which equations it is "
                     "exactly `4` and why."),
        "note": 'Two slopes bought a power of <em>h</em>. More slopes buy more, and the classic choice uses four. &ldquo;Runge&ndash;Kutta: Four Slopes per Step&rdquo; shows the error divided by sixteen.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "runge-kutta-four-slopes-per-step",
        "title": "Runge–Kutta: Four Slopes per Step",
        "module": "Stepping",
        "one_line": "Write the four slopes of the classical method and their weights 1, 2, 2, 1, show it is exact on y′ = t³, and that on y′ = t⁴ the error ratio is exactly 16.",
        "summary": (
            "The classical Runge&ndash;Kutta method reads four slopes in each step, one at "
            "the start, two at the middle and one at the end, and combines them with weights "
            "`1, 2, 2, 1` over `6`. When the right side depends on `t` alone, this is "
            "Simpson's rule, exact on cubics. The error is fourth order: halving `h` divides "
            "it by sixteen."
        ),
        "key": [
            "k₁ = f(tₙ, yₙ)",
            "k₂ = f(tₙ + h/2, yₙ + h·k₁/2)",
            "k₃ = f(tₙ + h/2, yₙ + h·k₂/2)",
            "k₄ = f(tₙ + h, yₙ + h·k₃)",
            "yₙ₊₁ = yₙ + h·(k₁ + 2k₂ + 2k₃ + k₄)/6",
            "y′ = t⁴: halve h, error ÷ 16 exactly",
        ],
        "key_label": "Four slopes, weights 1, 2, 2, 1",
        "concepts_intro": (
            "Three ideas: the four slopes, why the weights are 1, 2, 2, 1, and what fourth "
            "order buys."
        ),
        "concepts": [
            ("Four slopes are read, one at the start, two at the middle, one at the end",
             "The first is Euler's slope. The second is read at the middle of the step, using "
             "a half step along the first. The third is read at the middle again, using a half "
             "step along the second. The fourth is read at the end, using a whole step along "
             "the third. Each later slope corrects the point at which the previous one was "
             "taken."),
            ("The weights 1, 2, 2, 1 favour the middle",
             "The step uses `(k₁ + 2k₂ + 2k₃ + k₄)/6`. The middle gets two readings and so "
             "double weight, and the weights add to `6`. When `f` depends on `t` alone, "
             "`k₂ = k₃`, and the average is `(f(start) + 4·f(middle) + f(end))/6`: Simpson's "
             "rule on one piece, which integrates every cubic exactly."),
            ("Fourth order: halving the step divides the error by sixteen",
             "The error at a fixed `T` is about `C·h⁴`, and the ratio of successive errors "
             "is near `16`. Four slopes per step cost four times what Euler's method costs, "
             "and the error falls as the fourth power of the step, which an Euler refinement "
             "at the same cost does not reach on the equations here."),
        ],
        "read_title": "Four slopes, one weighted average",
        "read_intro": "The method, one step worked in full, the equation it solves exactly, the equation where the ratio is exactly 16, and why four slopes are not four Euler steps.",
        "body": [
            ("def", ("The classical Runge–Kutta method (RK4)",
                     "From `(tₙ, yₙ)` with step `h`: `k₁ = f(tₙ, yₙ)`; `k₂ = f(tₙ + h/2, "
                     "yₙ + h·k₁/2)`; `k₃ = f(tₙ + h/2, yₙ + h·k₂/2)`; `k₄ = f(tₙ + h, "
                     "yₙ + h·k₃)`; then `yₙ₊₁ = yₙ + h·(k₁ + 2k₂ + 2k₃ + k₄)/6`.",
                     "Four slopes are read per step. The lab runs it in exact fractions, up "
                     "to 32 steps.")),
            ("p", "“Euler's Error and the Step Size” measured Euler's method at order `1`, and "
                  "“The Improved Euler Method” measured the improved method at order `2`. This "
                  "is the next rung. Take the simplest equation for seeing the weights: "
                  "`y′ = t⁴` from `y(0) = 0`, with one step of size `h = 1`. Because `f` has "
                  "no `y`, the trial values play no part."),
            ("math", [
                "y′ = t⁴,  y(0) = 0,  one step, h = 1",
                "",
                "slope   read at     value",
                "k₁      t = 0       0",
                "k₂      t = 1/2     1/16",
                "k₃      t = 1/2     1/16",
                "k₄      t = 1       1",
                "",
                "y₁ = (0 + 2/16 + 2/16 + 1)/6 = (5/4)/6 = 5/24",
            ]),
            ("p", "The true value is `y(1) = 1/5`, and `5/24 − 1/5 = 1/120`. That is hand "
                  "arithmetic, and it is the whole error of the step: `h⁵/120` for a step of "
                  "size `h` from `t = 0`. For `t⁴` the fourth derivative is constant, so every "
                  "step of size `h` misses by the same `h⁵/120`, and `1/h` steps give "
                  "`h⁴/120` from `t = 0` to `t = 1`."),
            ("h3", "Exact on a cubic"),
            ("p", "On `y′ = t³` with exact solution `t⁴/4`, the lab prints `0` for the error at "
                  "every one of the three step sizes, the ratio tile reads `—` because "
                  "there is nothing to divide, and the order tile reads `exact (error 0)`. "
                  "The step is Simpson's rule, and Simpson's rule integrates a cubic without "
                  "error, so RK4 has nothing to get wrong here."),
            ("h3", "Exactly 16 on a quartic"),
            ("p", "On `y′ = t⁴` with exact solution `t⁵/5`, the errors at `h = 1/4`, `1/8` and "
                  "`1/16` are `1/30720`, `1/491520` and `1/7864320`. Each is `h⁴/120` "
                  "exactly: `(1/4)⁴/120 = 1/30720`. The ratios are `16` and `16`, and the "
                  "order is `4`."),
            ("thm", ("Runge–Kutta is fourth order",
                     "For a right-hand side with continuous fourth derivatives, the error of "
                     "RK4 at a fixed `T` is approximately `C·h⁴`, so halving `h` divides it "
                     "by about `16`.")),
            ("p", "The lab shows the exact ratio on `y′ = t⁴`, and on `y′ = y`, where the errors are "
                  "rounded, ratios of `≈ 14.4239` and `≈ 15.1898` that climb towards sixteen; it "
                  "does not prove the order for every equation."),
            ("example", ("Four slopes are not four Euler steps",
                         "Four Euler steps of size `h/4` also read four slopes, and they "
                         "advance by only `h`, each step starting from the previous "
                         "step's inexact value. RK4's four slopes are combined into a "
                         "single advance by `h`.",
                         "Count the work on `y′ = t⁴` to `T = 1`. RK4 with `h = 1/4` takes "
                         "four steps, sixteen slope readings, and has error `1/30720`. Euler "
                         "with sixteen readings is sixteen steps of `h = 1/16`, with error "
                         "`19627/655360 ≈ 0.0299484`, rounded, which is about 920 times "
                         "larger. Switch the Method menu to Euler and read the third error to "
                         "see it.")),
            ("p", "The third preset runs the method on `y′ = y`. The true value `e` is "
                  "irrational, so every error is rounded and the observed order, `≈ 3.92503`, "
                  "is near `4` and marked `≈`."),
        ],
        "lab": ("dekit", {
            "mode": "order",
            "method": "rk4",
            "preset": "quartic",
            "presets": [
                {"id": "cubic", "label": "y' = t^3, exact t^4/4, to T = 1",
                 "f": "t^3", "t0": 0, "y0": 0, "T": 1, "exact": "t^4/4", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "0", "odRatio": "—", "odOrder": "exact (error 0)"}},
                {"id": "quartic", "label": "y' = t^4, exact t^5/5, to T = 1",
                 "f": "t^4", "t0": 0, "y0": 0, "T": 1, "exact": "t^5/5", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "1/30720", "odRatio": "16, 16", "odOrder": "4"}},
                {"id": "growth", "label": "y' = y, exact e^t, to T = 1",
                 "f": "y", "t0": 0, "y0": 1, "T": 1, "exact": "e^t", "hs": ["1/4", "1/8", "1/16"],
                 "expect": {"odE1": "≈ 7.18893e-5", "odRatio": "≈ 14.4239, ≈ 15.1898", "odOrder": "≈ 3.92503"}},
            ],
            "panel_title": "Zero error, then exactly sixteen",
            "panel_intro": (
                "The method menu is set to Runge&ndash;Kutta. On the first preset every error is "
                "zero; on the second every error is h^4/120 and the ratios are 16. Switch the "
                "menu to Euler on the second preset and compare the third error, for h = 1/16, "
                "with the Runge-Kutta error at h = 1/4: the same sixteen slope readings."
            ),
        }),
        "steps_title": "One Runge–Kutta step by hand",
        "steps_intro": "Four readings and a weighted average, in this order.",
        "steps": [
            ("Read the slope at the start",
             "`k₁ = f(tₙ, yₙ)`."),
            ("Read the slope at the middle, along k₁",
             "`k₂ = f(tₙ + h/2, yₙ + h·k₁/2)`: go half a step along `k₁` and read there."),
            ("Read the slope at the middle again, along k₂",
             "`k₃ = f(tₙ + h/2, yₙ + h·k₂/2)`: same time, a better value."),
            ("Read the slope at the end, along k₃",
             "`k₄ = f(tₙ + h, yₙ + h·k₃)`: a whole step along `k₃`."),
            ("Combine with weights 1, 2, 2, 1 over 6",
             "`yₙ₊₁ = yₙ + h·(k₁ + 2k₂ + 2k₃ + k₄)/6`. The weights add to `6`; do not "
             "divide by `4`."),
        ],
        "worked": {
            "title": "One step of size 1 on y′ = t⁴",
            "intro": [
                "Take the single step from `y(0) = 0` to `t = 1`, compare with the true "
                "value, and state the error as a power of `h`.",
            ],
            "lines": [
                "f = t⁴, no y;  y₀ = 0;  h = 1",
                "",
                "k₁ = f(0)   = 0",
                "k₂ = f(1/2) = 1/16",
                "k₃ = f(1/2) = 1/16",
                "k₄ = f(1)   = 1",
                "",
                "y₁ = 1·(0 + 2·(1/16) + 2·(1/16) + 1)/6",
                "   = (5/4)/6 = 5/24",
                "true y(1) = 1/5;  error = 5/24 − 1/5 = 1/120",
                "",
                "from t = 0 to 1 with h = 1/4:  (1/4)⁴/120 = 1/30720",
            ],
            "after": [
                "The one-step error is `1/120`, which is `h⁵/120` at `h = 1`. From `t = 0` to "
                "`t = 1` with step `h`, there are `1/h` steps, each missing by `h⁵/120`, and the "
                "total is `h⁴/120`: `1/30720` at `h = 1/4`, as the lab prints. Halving "
                "`h` divides `h⁴` by exactly sixteen.",
                "For a rehearsal, take the single step on `y′ = t³` with `h = 1`. The "
                "readings are `0, 1/8, 1/8, 1`, so `y₁ = (0 + 2/8 + 2/8 + 1)/6 = (3/2)/6 = 1/4`, "
                "which is the true value, with error zero.",
            ],
        },
        "quiz_title": "Weights, exactness and sixteen",
        "quiz": [
            {"q": "Which combination gives the Runge–Kutta step?",
             "a": ["`yₙ + h·(k₁ + k₂ + k₃ + k₄)/4`",
                   "`yₙ + h·k₄`",
                   "`yₙ + h·(k₁ + 2k₂ + 2k₃ + k₄)/6`",
                   "`yₙ + h·(k₁ + 4k₂ + k₃)/6`"],
             "c": 2,
             "why": "The weights are `1, 2, 2, 1` and they add to `6`. Equal weights over `4` "
                    "ignore that the middle is read twice, and using only the last slope drops "
                    "three of the readings. The weights `1, 4, 1` have Simpson's shape, but "
                    "put on `k₁, k₂, k₃` they never read the slope at the end of the step; "
                    "what the formula reduces to when `k₂ = k₃` is `(k₁ + 4k₂ + k₄)/6`."},
            {"q": "Why is the error exactly `0` on `y′ = t³`?",
             "a": ["The lab rounds small errors to zero",
                   "The step is Simpson's rule when `f` depends on `t` alone, and that rule integrates every cubic exactly",
                   "Any fourth-order method is exact on every equation",
                   "The right side is too simple for Euler's method to matter"],
             "c": 1,
             "why": "With no `y` in the right side, `k₂ = k₃` and the step is "
                    "`h·(f(start) + 4·f(middle) + f(end))/6`, which is Simpson's rule, "
                    "exact for polynomials up to degree three. The lab does no rounding "
                    "here, and fourth order is a rate at which the error falls, not a "
                    "promise of exactness: on `y′ = t⁴` the same method has error `h⁴/120`."},
            {"q": "On `y′ = t⁴` the error at `h = 1/4` is `1/30720`. What is it at `h = 1/8`?",
             "a": ["`1/61440`", "`1/122880`", "`1/245760`", "`1/491520`"],
             "c": 3,
             "why": "Fourth order divides the error by `2⁴ = 16` when `h` is halved, and "
                    "`30720·16 = 491520`. Dividing by `2`, `4` or `8` is the rate of a "
                    "first, second or third order method."},
            {"q": "Why is Runge–Kutta not just four Euler steps of size `h/4`?",
             "a": ["It is the same thing, written differently",
                   "RK4 reads slopes at the start, the middle twice and the end and combines them into one advance of `h`; four Euler steps advance four times from four left-end slopes",
                   "RK4 uses four times the step",
                   "Euler's method cannot be repeated"],
             "c": 1,
             "why": "Four Euler steps use four left-end slopes and move four times; RK4 reads "
                    "its slopes at trial points and combines them into one move. At sixteen "
                    "readings on `y′ = t⁴` the errors differ by a factor of about 920."},
        ],
        "mistakes": [
            ("Thinking Runge–Kutta is four Euler steps, so it costs the same as Euler with h/4 and does no better",
             "The cost is the same, four slope readings, and the error is not. On `y′ = t⁴` "
             "with sixteen readings, RK4 at `h = 1/4` has error `1/30720` and Euler at "
             "`h = 1/16` has `19627/655360`, about 920 times more. The four slopes are combined "
             "into one step, and the combination is what raises the order."),
            ("Averaging the four slopes equally",
             "The middle slope is read twice and the weights are `1, 2, 2, 1` over `6`. "
             "On the worked example the equal average gives `(0 + 1/16 + 1/16 + 1)/4 = 9/32`, "
             "against `5/24` with the right weights and `1/5` for the truth: a much larger "
             "error."),
            ("Taking fourth order to mean exact",
             "The lab prints `0` on `y′ = t³` and not on `y′ = t⁴`, where the error is "
             "`h⁴/120`. Fourth order says how fast the error falls; exactness is a property "
             "of the equation, and here it comes from the right side being a polynomial in "
             "`t` of degree three or less, which Simpson's rule integrates without error. "
             "On `y′ = y`, whose solution is no polynomial at all, the error is never zero."),
        ],
        "standard": ("Finish when you can write the four slopes and weights of RK4 and show its error ratio is 16.",
                     "You should be able to compute `k₁` to `k₄` and the step for a given "
                     "equation, state that the weights are `1, 2, 2, 1` over `6`, explain why "
                     "the method is exact on `y′ = t³`, and read the ratio `16` and the order "
                     "`4` from the lab at three step sizes on `y′ = t⁴`."),
        "note": 'Three methods, three orders, and all of them assume the solution is there to be approached. &ldquo;Blow-Up and the Interval of Existence&rdquo; shows an equation where it is not.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "blow-up-and-the-interval-of-existence",
        "title": "Blow-Up and the Interval of Existence",
        "module": "When solutions misbehave",
        "one_line": "Show that y = 1/(1 − t) solves y′ = y² and ceases to exist at t = 1, watch Euler step past it without noticing, and read the digit budget: a quadratic right side doubles the digits each step.",
        "summary": (
            "A smooth right-hand side does not guarantee a solution for all `t`. The equation "
            "`y′ = y²` has the solution `1/(1 − t)` through `(0, 1)`, which grows without "
            "bound and ceases to exist at `t = 1`. Euler's method, which only ever looks one "
            "step ahead, steps straight past that time and reports finite numbers, and the "
            "exact fractions it produces double in length at every step until the lab stops "
            "at a stated budget."
        ),
        "key": [
            "y′ = y², y(0) = 1:  y = 1/(1 − t)",
            "y has no value at t = 1; it ends there",
            "smooth f: a solution near the start only",
            "Euler steps past t = 1 without noticing",
            "digits double per step; stops after 11",
        ],
        "key_label": "A solution that ends, and a method that does not",
        "concepts_intro": (
            "Three ideas: the interval where a solution lives, what a step method cannot "
            "see, and what exact arithmetic reveals."
        ),
        "concepts": [
            ("A solution lives on an interval, and the interval can be short",
             "A solution is a function on some interval of `t`. For `y′ = y²` with "
             "`y(0) = 1` it is `1/(1 − t)` on `t < 1`: the values rise without limit as "
             "`t` approaches `1` and there is no value at `1`. The right side `y²` is "
             "a polynomial, as smooth as an expression gets, and that did not help."),
            ("A step method keeps producing numbers whether or not a solution exists",
             "Euler's recipe needs only a slope at a point, and `y²` is defined at every "
             "`y`. So the method steps through `t = 1` and beyond, and every `yₙ` it prints is "
             "a finite fraction. A number from the method past `t = 1` is not a value of "
             "any solution through the start, since that solution does not exist there."),
            ("Exact fractions expose the growth",
             "Squaring a fraction doubles the digits of its numerator and denominator, and "
             "Euler's step on `y²` squares the current value. The lengths of the denominators, "
             "`1, 2, 5, 10, 19, 38, 77, …`, roughly double at each step. The lab stops when a "
             "number passes 2000 digits and says so, rather than rounding to continue."),
        ],
        "read_title": "Where a solution ends, and what the method does there",
        "read_intro": "The solution and its check, three steps of Euler against it, the step past the end, the limit on the arithmetic, and what is known in general.",
        "body": [
            ("p", "Take `y′ = y²` with `y(0) = 1`. The candidate `y = 1/(1 − t)` has "
                  "`y′ = 1/(1 − t)²`, and `y²` is `1/(1 − t)²` as well, so the residual is "
                  "`0`: it is the check of “Checking a Proposed Solution”, which the lab "
                  "does exactly. The value at `t = 0` is `1`, so it passes through the "
                  "start. At `t = 3/4` it is `1/(1/4) = 4`; at `t = 9/10` it is `10`; as `t` "
                  "approaches `1` it grows without limit."),
            ("p", "Starting higher ends the solution sooner. For `y(0) = y₀` the solution "
                  "is `y₀/(1 − y₀·t)`, whose derivative is `y₀²/(1 − y₀·t)²`, which is "
                  "its square, so the residual is `0`; it ends at `t = 1/y₀`. From `y₀ = 2` "
                  "it ends at `t = 1/2`. The time of the end depends on the start, and "
                  "nothing in the equation announces it."),
            ("thm", ("Existence and uniqueness, near the start",
                     "If `f(t, y)` and its derivative with respect to `y` are continuous near "
                     "the start `(t₀, y₀)`, then there is exactly one solution through the "
                     "start on <em>some</em> interval around `t₀`. The theorem does not "
                     "say how long the interval is.")),
            ("p", "The example above shows why the last sentence is not a technicality: "
                  "here `f = y²` is as well behaved as a function can be, and the interval is "
                  "`t < 1`. The lab demonstrates this one case and does not prove the "
                  "theorem; the proof belongs to a course in analysis."),
            ("h3", "Euler's method against the solution"),
            ("math", [
                "y′ = y²,  y(0) = 1,  h = 1/4",
                "",
                "n    tₙ     yₙ                  y(tₙ) = 1/(1 − tₙ)",
                "0    0      1                   1",
                "1    1/4    5/4                 4/3",
                "2    1/2    105/64              2",
                "3    3/4    37905/16384         4",
            ]),
            ("p", "Three steps give `y₃ = 37905/16384 ≈ 2.31354`, rounded for reading; the "
                  "true value is `4`, and the error the lab prints is `27631/16384`. Euler "
                  "falls well behind, as it must on a rate that rises this fast, and the "
                  "polygon still looks tame."),
            ("h3", "Stepping past the end"),
            ("p", "Run five steps and `t₅ = 5/4`, which is past `t = 1`. The lab prints "
                  "`y₅ = 32213971596000663105/4611686018427387904 ≈ 6.98529`, a perfectly good "
                  "fraction, and the tile for the known solution reads `undefined at "
                  "t = 5/4`. The formula `1/(1 − t)` would give `−4` at `5/4`, and that "
                  "number is not the solution either: the solution through `(0, 1)` has "
                  "already ended, and the negative branch is a different curve. The method "
                  "never saw the end, because it never looks further than one step."),
            ("h3", "The digit budget"),
            ("p", "Write each value over a power of two. The denominators are `4`, `64`, "
                  "`16384`, then `2³⁰` and on: each is the square of the last times `4`, "
                  "so the exponent goes `2, 6, 14, 30, 62, …`. Their lengths are `1, 2, 5, 10, "
                  "19, 38, 77, …` digits, doubling. With `h = 1/4` the lab completes "
                  "eleven steps, whose largest denominator has 1233 digits (the last value "
                  "is shown rounded, `≈ 6.77729e23`, over a numerator of 1257 digits), and "
                  "stops before the twelfth, which would pass its limit of 2000 digits. The "
                  "tile reads "
                  "`stopped after step 11: digit budget`. Nothing was rounded to continue."),
            ("p", "That is a fact about the method, and a floating-point program hides it by "
                  "rounding at every step and carrying on. The numbers it would print past "
                  "`t = 1` are no more the solution than the exact ones are."),
        ],
        "lab": ("dekit", {
            "mode": "euler",
            "preset": "square",
            "presets": [
                {"id": "square", "label": "y' = y^2 from (0, 1), h = 1/4, 3 steps",
                 "f": "y^2", "t0": 0, "y0": 1, "h": "1/4", "n": 3, "exact": "1/(1 - t)",
                 "expect": {"euLast": "37905/16384", "euExact": "4", "euError": "27631/16384"}},
                {"id": "past", "label": "y' = y^2 from (0, 1), h = 1/4, 5 steps",
                 "f": "y^2", "t0": 0, "y0": 1, "h": "1/4", "n": 5, "exact": "1/(1 - t)",
                 "expect": {"euLast": "32213971596000663105/4611686018427387904", "euExact": "undefined at t = 5/4"}},
                {"id": "budget", "label": "y' = y^2 from (0, 1), h = 1/4, 16 steps",
                 "f": "y^2", "t0": 0, "y0": 1, "h": "1/4", "n": 16, "exact": "1/(1 - t)",
                 "expect": {"euStopped": "stopped after step 11: digit budget", "euDigits": "1233"}},
            ],
            "panel_title": "Step toward the end of a solution, then past it",
            "panel_intro": (
                "The first preset stops at t = 3/4, where the solution equals 4. The second "
                "runs past t = 1 and the known-solution tile says it is undefined. The third "
                "asks for sixteen steps and the lab stops at the digit budget. Change the "
                "start to 0 2 and expect the solution to end at t = 1/2."
            ),
        }),
        "steps_title": "Finding where a solution ends",
        "steps_intro": "From an equation to the largest interval you can claim.",
        "steps": [
            ("Find a closed form, if there is one, and check it",
             "Substitute it into the equation and read the residual, as in "
             "“Checking a Proposed Solution”. Without a check there is no solution to "
             "speak of."),
            ("Find where the formula fails",
             "Look for a zero of a denominator or another break. `1/(1 − t)` fails at "
             "`t = 1`. Note which side of it the start lies on."),
            ("State the interval of existence",
             "The solution through the start lives on the interval that contains the start "
             "and stops at the break: `t < 1` for the start `(0, 1)`."),
            ("Compare with the method",
             "Step Euler past the break and see that it prints finite numbers anyway. Say "
             "which of those numbers lie past the end of the solution."),
            ("Read the stop tile",
             "If the lab stops, note the step. It is the budget of the arithmetic, not "
             "the end of the solution."),
        ],
        "worked": {
            "title": "y′ = y² through (0, 1): three steps and the true values",
            "intro": [
                "Take three Euler steps of size `1/4` and compare the last with `1/(1 − t)`.",
            ],
            "lines": [
                "f = y²,  h = 1/4,  y₀ = 1",
                "",
                "y₁ = 1 + (1/4)·1         = 5/4",
                "y₂ = 5/4 + (1/4)·(25/16) = 105/64",
                "y₃ = 105/64 + (1/4)·(105/64)²",
                "   = 37905/16384  ≈ 2.31354",
                "",
                "true y(3/4) = 1/(1 − 3/4) = 4",
                "error 4 − 37905/16384 = 27631/16384",
                "",
                "denominators 4, 64, 16384:  1, 2, 5 digits",
            ],
            "after": [
                "The arithmetic is exact at every line, and Euler is still more than 1.6 "
                "short of the true value at `t = 3/4`. The solution is climbing towards "
                "infinity at `t = 1`, and every step reads a slope smaller than the slope "
                "the step is about to meet.",
                "For a rehearsal, take the start `y(0) = 2`: the solution is `2/(1 − 2t)`, "
                "it ends at `t = 1/2`, and the first Euler step with `h = 1/4` is "
                "`2 + (1/4)·4 = 3`.",
            ],
        },
        "quiz_title": "Where solutions end",
        "quiz": [
            {"q": "What is true of `y = 1/(1 − t)` as the solution of `y′ = y²` with `y(0) = 1`?",
             "a": ["It exists for every `t`, since the right side is a polynomial",
                   "It satisfies the equation only at `t = 0`",
                   "It satisfies the equation on `t < 1` and grows without limit as `t` approaches `1`",
                   "It levels off at `y = 4`"],
             "c": 2,
             "why": "The residual is zero for every `t` where the formula is defined, so it "
                    "is a solution on `t < 1`, and the values grow without limit towards `t = 1`. "
                    "A polynomial right side does not give a global solution, and `4` is just its "
                    "value at `t = 3/4`."},
            {"q": "Euler's method with `h = 1/4` prints a finite `y₅` at `t = 5/4` on `y′ = y²` from `(0, 1)`. What does that show?",
             "a": ["The solution exists at `t = 5/4` and equals the printed fraction",
                   "The recipe produces numbers whether or not a solution exists there; none of these values belongs to the solution through the start",
                   "The step `h = 1/4` is too small",
                   "The solution blows up at `t = 5/4`"],
             "c": 1,
             "why": "The solution ended at `t = 1`, so there is nothing at `5/4` for the "
                    "printed fraction to approximate. The method needs only a slope at a "
                    "point, and `y²` is defined for every `y`."},
            {"q": "A solution of `y′ = y²` starts at `y(0) = 2`. When does it cease to exist?",
             "a": ["`t = 1/2`", "`t = 1`", "`t = 2`", "It never does"],
             "c": 0,
             "why": "The solution is `2/(1 − 2t)`, which has no value when `1 − 2t = 0`, "
                    "that is at `t = 1/2`. The end at `t = 1` belongs to the start `y(0) = 1`; "
                    "a higher start ends sooner."},
            {"q": "The lab stops at step `11` with the digit budget. What does that stop mean?",
             "a": ["The solution ends at `t = 11/4`",
                   "The next step's numbers would pass 2000 digits, so the lab stops instead of rounding",
                   "Euler's method becomes unstable at step `11`",
                   "The equation has no solution after eleven steps"],
             "c": 1,
             "why": "The stop belongs to the arithmetic: a quadratic right side squares the "
                    "fraction, the digits double, and the twelfth step would pass the limit. "
                    "The solution itself ended at `t = 1`, well before step `11`, which is "
                    "`t = 11/4`."},
        ],
        "mistakes": [
            ("Expecting a smooth right-hand side to give a solution for all t",
             "The right side of `y′ = y²` is a polynomial, and the solution through `(0, 1)` "
             "is `1/(1 − t)`, which has no value at `t = 1` and grows without limit before "
             "it. What smoothness gives is a unique solution near the start, on an interval "
             "that may be short."),
            ("Reading Euler's value past the end as a value of the solution",
             "The lab prints `y₅ = 32213971596000663105/4611686018427387904 ≈ 6.98529` at "
             "`t = 5/4` and the known-solution tile says `undefined at t = 5/4`. The fraction "
             "is a correct output of the recipe and approximates nothing, because there is "
             "no solution at that time."),
            ("Reading the digit-budget stop as the place the solution ends",
             "The stop after step `11` is at `t = 11/4`, and the solution ended at `t = 1`. "
             "The stop says the exact fractions have grown too long to print, which is "
             "what squaring does to a fraction, and it would happen on a quadratic right "
             "side whether or not the solution existed."),
        ],
        "standard": ("Finish when you can show a solution ends, step Euler past it, and read the digit budget.",
                     "You should be able to check that `1/(1 − t)` solves `y′ = y²`, say "
                     "where it ceases to exist and on what interval it is the solution through "
                     "`(0, 1)`, explain why Euler's method gives finite values past that "
                     "time, and explain why the exact fractions double in length at each step."),
        "note": 'That closes the stepping. Every method here approximates, and every closed form so far was checked rather than found. The next course finds them: a family of equations that can be solved by separating the variables, starting from the chain rule run backwards. Separable Equations, Growth and Decay is where.',
    },
]
