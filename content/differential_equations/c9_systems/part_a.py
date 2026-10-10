"""Systems and the Phase Plane -- the first half.

Linear systems in the plane: the system as a field of arrows, the straight-line
solutions and the eigenvectors that give them, the general solution and the
constants that fit it to a start, the saddles, nodes, spirals and centres, and
the criterion for stability of the origin.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py (mode
phase), by executing its shipped JavaScript under node, and pinned in `expect`.
The traces, determinants, eigenvalues, eigenvectors and fitted constants are
exact fractions or surds; the curves behind them are drawn by stepping in
floating point and the legend says so. Euler's steps are exact arithmetic
applied to an approximate method, and the lessons say where that matters.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "systems-of-two-equations",
        "title": "Systems of Two Equations",
        "module": "Linear systems",
        "one_line": "A pair of equations sends every point of a plane an arrow, and a solution is a curve that follows the arrows.",
        "summary": (
            "Two quantities that change together are described by a system such as "
            "`x′ = a·x + b·y`, `y′ = c·x + d·y`. At each point `(x, y)` it names a "
            "direction and a speed, and Euler's method steps both quantities at once. A "
            "solution is a curve `(x(t), y(t))` in the phase plane, and the plane has no "
            "axis for time: time is how far along the curve you have gone."
        ),
        "key": [
            "x′ = a·x + b·y,   y′ = c·x + d·y",
            "the arrow at (x, y) is (a·x + b·y, c·x + d·y)",
            "a solution is a curve (x(t), y(t))",
            "the phase plane has no t axis",
            "Euler: new point = point + h·arrow",
        ],
        "key_label": "A system is an arrow at every point",
        "concepts_intro": (
            "Three ideas, and the first one decides how to read every picture on this "
            "course. The other two are the arithmetic that fills the picture in."
        ),
        "concepts": [
            ("A system gives every point an arrow",
             "The right-hand sides `a·x + b·y` and `c·x + d·y` are functions of the "
             "point `(x, y)`, and nothing else. At `(1, 1)` the system `x′ = x`, "
             "`y′ = −y` names the arrow `(1, −1)`: `x` is growing at rate `1` and `y` "
             "is shrinking at rate `1`. The collection of all those arrows is a vector "
             "field, and the system is a rule for drawing it."),
            ("A solution is a curve that follows the arrows",
             "A pair of functions `x(t)` and `y(t)` solves the system when, at every "
             "`t`, the velocity `(x′, y′)` is the arrow at the point `(x(t), y(t))`. "
             "Plot the points `(x(t), y(t))` as `t` runs and you get a curve in the "
             "plane that is tangent to the field everywhere it goes. That plane, with "
             "the unknowns for axes, is the phase plane."),
            ("Euler steps both unknowns at once",
             "From the point `(x, y)` with step `h` the next point is `(x + h·x′, "
             "y + h·y′)`, each rate read from the arrow at the old point. Both "
             "coordinates move before either rate is read again. With rational "
             "coefficients every step is a pair of fractions, and the lab prints them "
             "exactly."),
        ],
        "read_title": "From one equation to two, and from a graph to a path",
        "read_intro": "The definition, the first system worked out, what the phase plane leaves out, and the one exact fact that shows Euler's polygon is only a recipe.",
        "body": [
            ("def", ("A linear system in the plane",
                     "Two equations `x′ = a·x + b·y` and `y′ = c·x + d·y`, where `a`, "
                     "`b`, `c` and `d` are numbers. Written with a matrix it is "
                     "`x′ = A·x`, where `x` is the pair `(x, y)` and `A` has the rows "
                     "`a b` and `c d`.",
                     "A <strong>solution</strong> is a pair of functions `x(t)`, `y(t)` "
                     "that satisfy both equations. The <strong>phase plane</strong> is "
                     "the plane with the unknowns `x` and `y` as its axes, and the "
                     "<strong>orbit</strong> of a solution is the curve it traces.")),
            ("p", "One equation `y′ = f(t, y)` gave a field of slopes on a plane with "
                  "time across the bottom. A system has two unknowns and no time on "
                  "either axis, and the field is a field of arrows instead. The "
                  "equations here have no `t` on the right-hand side, so the arrow at a "
                  "point is the same whenever the solution gets there. That is why "
                  "the picture can leave time out: two solutions that meet the same "
                  "point leave it in the same direction."),
            ("math", [
                "x′ = x",
                "y′ = −y",
                "at (1, 1) the arrow is (1, −1)",
                "at (2, 1) the arrow is (2, −1)",
                "at (0, 3) the arrow is (0, −3)",
            ]),
            ("h3", "A curve in the plane is not a graph against time"),
            ("p", "The commonest misreading is to treat the horizontal axis as time. In "
                  "the phase plane the horizontal axis is `x`. A solution that starts "
                  "at `(1, 1)` and reaches `(5/4, 3/4)` has moved right and down in "
                  "space, and the picture does not say when. To recover the timing you "
                  "go back to the formulas, or to the step count, because time is "
                  "carried by the step and not by an axis."),
            ("example", ("Three steps of x′ = x, y′ = −y",
                         "Start at `(1, 1)` with `h = 1/4`. The arrow at `(1, 1)` is "
                         "`(1, −1)`, so the first step lands at `(1 + 1/4, 1 − 1/4)`, "
                         "which is `(5/4, 3/4)`.",
                         "The arrow there is `(5/4, −3/4)`, giving `(5/4 + 5/16, "
                         "3/4 − 3/16)`, which is `(25/16, 9/16)`. A third step gives "
                         "`(125/64, 27/64)`. The curve heads along the `x` direction "
                         "away from the origin while `y` dies away, which is the "
                         "picture of a saddle.")),
            ("math", [
                "step          x           y",
                "  0           1           1",
                "  1          5/4         3/4",
                "  2         25/16        9/16",
                "  3        125/64       27/64",
            ]),
            ("p", "The first preset in the lab is this system, and it is set to eight "
                  "steps rather than three, so the point it prints is the eighth. "
                  "Drag the step control down to three and the third row above appears "
                  "in the last-point tile. Notice that the arithmetic was the same one-line "
                  "rule each time: `x` is multiplied by `1 + h` and `y` by `1 − h`."),
            ("thm", ("A quantity the true solution keeps",
                     "Every solution of `x′ = x`, `y′ = −y` keeps the product `x·y` "
                     "constant.")),
            ("proof", ["By the product rule `(x·y)′ = x′·y + x·y′`.",
                       "Substituting the equations gives `x·y − x·y = 0`, so the product "
                       "never changes. The solution through `(1, 1)` therefore lies on "
                       "the curve `x·y = 1`. The Euler points above do not: "
                       "`(125/64)·(27/64) = 3375/4096`, which is `(15/16)³`. Each step "
                       "multiplies the product by `(1 + h)·(1 − h) = 15/16`, so the "
                       "polygon slips inside the curve."]),
            ("p", "That is the difference between the method and the solution, shown with "
                  "two fractions. Each Euler step is computed exactly, and the polygon "
                  "is still not the curve. Sixteen steps of `h = 1/16` would stay much "
                  "closer, and the lab lets you try. What it cannot do is make the product "
                  "exactly one."),
            ("example", ("A system that goes round",
                         "Take `x′ = y`, `y′ = −x` from `(1, 0)`. The arrow at "
                         "`(1, 0)` is `(0, −1)`, so with `h = 1/4` the first step goes "
                         "to `(1, −1/4)`.",
                         "The true solutions here are circles about the origin, and "
                         "the squared distance from the origin is `1` at the start. After "
                         "the step it is `1 + 1/16 = 17/16`. The lab prints that "
                         "ratio, and it is the same at every step: Euler's polygon on a "
                         "rotation spirals outwards by an exact factor of `1 + h²`, "
                         "because each step moves along the tangent, and a tangent "
                         "always leaves the circle. &ldquo;Euler on an Oscillator&rdquo; proved "
                         "that factor for `x′ = v`, `v′ = −x`; this is the same system with "
                         "`y` written for `v`, seen in the phase plane.")),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "field",
            "preset": "saddle",
            "presets": [
                {"id": "saddle", "label": "x′ = x, y′ = −y",
                 "A": [[1, 0], [0, -1]], "start": [1, 1], "h": "1/4", "n": 8,
                 "expect": {"ppTrace": "0", "ppDet": "−1", "ppLast": "(390625/65536, 6561/65536)"}},
                {"id": "rotate", "label": "x′ = y, y′ = −x",
                 "A": [[0, 1], [-1, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppTrace": "0", "ppDet": "1", "ppRatio": "17/16", "ppLast": "(−31679/65536, −2415/2048)"}},
                {"id": "decay", "label": "x′ = −x, y′ = −2y",
                 "A": [[-1, 0], [0, -2]], "start": [2, 2], "h": "1/4", "n": 8,
                 "expect": {"ppTrace": "−3", "ppDet": "2", "ppLast": "(6561/32768, 1/128)"}},
            ],
            "panel_title": "Read a system as a field of arrows",
            "panel_intro": (
                "Pick a preset and look at the field, then switch the view to the exact "
                "Euler steps and compare the polygon with the curve drawn behind it. The "
                "tiles are exact. Change the step count to three on the first preset and "
                "check the last point against the table above. Then type your own matrix "
                "by rows, as 0 1; -2 -3, which means x′ = y and y′ = −2x − 3y."),
        }),
        "steps_title": "Stepping a system and reading what it does",
        "steps_intro": "Read the arrow, take the step on both coordinates, and then ask what the path is doing in the plane.",
        "steps": [
            ("Write the system as an arrow",
             "At the point `(x, y)` the arrow is `(a·x + b·y, c·x + d·y)`. For `x′ = x`, "
             "`y′ = −y` it is `(x, −y)`, so at `(2, 1)` it is `(2, −1)`."),
            ("Multiply the arrow by the step",
             "With `h = 1/4` the arrow `(2, −1)` becomes the displacement `(1/2, −1/4)`. "
             "Both components are scaled by the same `h`."),
            ("Add the displacement to the point",
             "The new point is `(2 + 1/2, 1 − 1/4)`, which is `(5/2, 3/4)`. Read the next "
             "arrow from this new point and repeat."),
            ("Describe the path, not the graph",
             "Say where the point is heading in the plane: away from the origin along "
             "one axis and toward it along the other, round and round, or in toward "
             "the origin. Do not say how `x` varies with `t` unless you also say that you "
             "have left the phase plane."),
            ("Ask what is conserved or lost",
             "Where the true solution keeps a quantity (the product `x·y`, or the "
             "squared distance on a rotation), compute that quantity at the Euler point "
             "and compare. The gap is the method's error, and it is exact."),
        ],
        "worked": {
            "title": "x′ = x, y′ = −y from (1, 1), h = 1/4",
            "intro": [
                "The system is the first preset. The arrow at each point is `(x, −y)`, and "
                "the step multiplies `x` by `1 + h = 5/4` and `y` by `1 − h = 3/4`.",
            ],
            "lines": [
                "arrow at (1, 1):  (1, −1)",
                "step 1:  (1 + 1/4, 1 − 1/4) = (5/4, 3/4)",
                "step 2:  (5/4 · 5/4, 3/4 · 3/4) = (25/16, 9/16)",
                "step 3:  (125/64, 27/64)",
                "x grows by 5/4 each step, y shrinks by 3/4",
                "trace = 1 + (−1) = 0     determinant = −1",
                "the curve leaves along the x-axis: a saddle",
            ],
            "after": [
                "The path heads away from the origin along the `x`-axis while its `y` "
                "dies away, and no start on the `y`-axis ever leaves it. That mixture of "
                "going in along one direction and out along another is what a saddle is, "
                "and the trace and determinant tiles, `0` and `−1`, are the first look at "
                "the two numbers the rest of this course sorts by.",
                "The product of the steps' coordinates is `3375/4096`, not `1`, so this "
                "polygon is inside the true curve `x·y = 1`. That is not a slip in the "
                "arithmetic. It is what one step size does to a curve that bends.",
            ],
        },
        "quiz_title": "Arrows, curves and steps",
        "quiz": [
            {"q": "For `x′ = x`, `y′ = −y`, which description of the solution through `(1, 1)` is right?",
             "a": ["It moves away from the origin in `x` while `y` shrinks, along the curve `x·y = 1`",
                   "It moves up and to the right, because `x′` is positive",
                   "It stays at `(1, 1)`, because the start is a single point",
                   "It moves horizontally, because `y′ = −y` does not involve `x`"],
             "c": 0,
             "why": "At `(1, 1)` the arrow is `(1, −1)`: `x` is growing and `y` is falling, "
                    "and the product `x·y` stays `1`. Moving up and to the right "
                    "forgets that `y′ = −y` is negative there. Nothing sits still at "
                    "`(1, 1)`, because the arrow there is not zero. And the second "
                    "equation having no `x` in it means `y` decays on its own, not that "
                    "the path is horizontal."},
            {"q": "For `x′ = −x`, `y′ = −2y` from `(2, 2)` with `h = 1/4`, where does the first Euler step land?",
             "a": ["`(3/2, 3/2)`",
                   "`(5/2, 3)`",
                   "`(3/2, 1)`",
                   "`(7/4, 3/2)`"],
             "c": 2,
             "why": "The arrow at `(2, 2)` is `(−2, −4)`, so the displacement is `(−1/2, −1)` "
                    "and the point is `(3/2, 1)`. The first choice uses the same rate for "
                    "both unknowns. The second moves in the wrong direction. The last "
                    "subtracts `h` times the coefficient and forgets to multiply by the "
                    "coordinate."},
            {"q": "What are the axes of the phase plane?",
             "a": ["`x` across and time up, as for a single equation",
                   "`x` against `y`, with time carried by the position along the curve",
                   "`x′` against `y′`, because the plane is the plane of the rates",
                   "`t` across and the pair `(x, y)` up"],
             "c": 1,
             "why": "The unknowns are the axes, and time is how far along the curve the "
                    "solution has gone. A plot of `x` against time is a different "
                    "picture, taken from the same solution. The plane of the rates is "
                    "the arrow's own coordinates, not where the solution sits."},
            {"q": "On `x′ = y`, `y′ = −x` the lab reports the ratio `17/16` for the squared distance from the origin. What does it mean?",
             "a": ["The true solution moves out from the origin by `17/16` every `t = 1/4`",
                   "The true solution is a spiral in this system",
                   "Euler's polygon is farther from the origin after each step, by a factor of `17/16` in squared distance",
                   "The matrix has trace `17/16`"],
             "c": 2,
             "why": "The true solutions of this system are circles, so their distance "
                    "from the origin never changes. The factor `1 + h² = 17/16` belongs "
                    "to the step, and it is why the polygon spirals out. It has nothing "
                    "to do with the trace, which is `0`."},
        ],
        "mistakes": [
            ("Reading the phase plane as x plotted against time",
             "A reader who takes the horizontal axis for time sees the path from "
             "`(1, 1)` to `(5/4, 3/4)` as `x` rising and `y` being a second graph. "
             "The axes are `x` and `y`: the point moved right and down in space. Two "
             "different solutions can cross the same vertical line at different "
             "moments, and the plane does not show when. The refutation is the "
             "table above, where every row has a step number beside it and none of them "
             "is an axis."),
            ("Multiplying h by the coefficient but not by the coordinate",
             "The step is `h` times the arrow, and the arrow is `(a·x + b·y, c·x + d·y)`, "
             "not the coefficients alone. From `(2, 1)` with `x′ = x`, the displacement "
             "is `(1/4)·2 = 1/2`, not `1/4`. Using the coefficient alone moves `x` "
             "from `2` to `9/4`, the same displacement wherever the point is, and "
             "the orbit would never speed up as it moves away."),
            ("Treating Euler's polygon as the solution",
             "The points `(5/4, 3/4)`, `(25/16, 9/16)` and `(125/64, 27/64)` are exact, and "
             "they are not on the curve `x·y = 1`: their product is `15/16` after one "
             "step and `3375/4096` after three. The solution keeps the product at `1` "
             "for every `t`. The polygon is a recipe that is near the curve for "
             "reasons the error lessons measure."),
        ],
        "standard": (
            "Finish when you can take a system x′ = a·x + b·y, y′ = c·x + d·y and a start, and describe where it goes.",
            "You should be able to name the arrow at a point, take an Euler step on both "
            "unknowns as exact fractions, say that the orbit is a curve in the plane with "
            "no time axis, and say what quantity the true solution keeps that the "
            "polygon does not."),
        "note": 'A system can be solved once the directions in which it moves in a straight line are known. Finding them is a question about the matrix alone, and the next lesson, &ldquo;Straight-Line Solutions and Eigenvectors&rdquo;, answers it.',
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "straight-line-solutions-and-eigenvectors",
        "title": "Straight-Line Solutions and Eigenvectors",
        "module": "Linear systems",
        "one_line": "Some directions are only stretched by the matrix, and along each of them the system solves itself.",
        "summary": (
            "An eigenvector of `A` is a direction that the matrix does not turn: `A·v` is "
            "a multiple `λ·v` of `v`. The multipliers `λ` are the roots of "
            "`λ² − τ·λ + Δ = 0`, where `τ` is the trace and `Δ` the determinant. For each "
            "such pair, `e^(λt)·v` is a solution that travels along a straight line "
            "through the origin."
        ),
        "key": [
            "A·v = λ·v    v is a direction, not a point",
            "λ² − τ·λ + Δ = 0",
            "τ = a + d     Δ = a·d − b·c",
            "(A − λ·I)·v = 0    solve for v",
            "x(t) = e^(λt)·v  solves  x′ = A·x",
        ],
        "key_label": "The directions a matrix only stretches",
        "concepts_intro": (
            "Three ideas. The first names what to look for, the second says how to find "
            "the multipliers, and the third says why the effort pays: each pair gives a "
            "solution you can write down."
        ),
        "concepts": [
            ("An eigenvector is a direction",
             "A non-zero vector `v` is an <em>eigenvector</em> of `A` when `A·v = λ·v` "
             "for some number `λ`, called its <em>eigenvalue</em>. Multiplying by `A` "
             "may stretch, shrink or flip `v`, but it leaves it on the same line "
             "through the origin. Every non-zero multiple of `v` is an eigenvector for the "
             "same `λ`, so `(1, 1)` and `(2, 2)` are one answer written twice."),
            ("The eigenvalues solve a quadratic",
             "`A·v = λ·v` says `(A − λ·I)·v = 0`, and a non-zero `v` can satisfy that only "
             "when the determinant of `A − λ·I` is zero. Expanding it gives "
             "`λ² − τ·λ + Δ = 0` with `τ = a + d` and `Δ = a·d − b·c`. Two exact "
             "numbers decide the multipliers, and the quadratic formula finishes the job."),
            ("An eigenvector gives a straight-line solution",
             "If `A·v = λ·v` then `x(t) = e^(λt)·v` solves `x′ = A·x`. The point never "
             "leaves the line through `v`: it slides along it, away from the origin if "
             "`λ` is positive and toward it if `λ` is negative."),
        ],
        "read_title": "Finding the directions, and why they solve the system",
        "read_intro": "The definition, the quadratic, a full example in fractions, the solution it produces, and what happens when the roots are not rational.",
        "body": [
            ("def", ("Eigenvalue and eigenvector",
                     "For a matrix `A`, a number `λ` is an <strong>eigenvalue</strong> and a "
                     "non-zero vector `v` an <strong>eigenvector</strong> when "
                     "`A·v = λ·v`.",
                     "Every non-zero multiple of an eigenvector is an eigenvector with "
                     "the same eigenvalue, so what is determined is a <strong>direction</strong>, "
                     "not a point. The lab prints the smallest whole-number vector with "
                     "its first non-zero entry positive, so a diagonal matrix gets "
                     "`(0, 1)` and `(1, 0)`.")),
            ("thm", ("Where the eigenvalues come from",
                     "The eigenvalues of `A`, with rows `a b` and `c d`, are the "
                     "roots of `λ² − τ·λ + Δ = 0`, where `τ = a + d` is the trace and "
                     "`Δ = a·d − b·c` the determinant.")),
            ("proof", ["`A·v = λ·v` is `(A − λ·I)·v = 0`, which has a non-zero solution "
                       "`v` exactly when `A − λ·I` has determinant zero, the fact about "
                       "two-by-two systems from Algebra's Systems and Matrices.",
                       "That determinant is `(a − λ)·(d − λ) − b·c`. Multiplying out "
                       "gives `λ² − (a + d)·λ + (a·d − b·c)`, which is "
                       "`λ² − τ·λ + Δ`. The two roots add to `τ` and multiply to `Δ`."]),
            ("example", ("A symmetric matrix",
                         "Take `A` with rows `2 1` and `1 2`. Then `τ = 4` and `Δ = 3`, "
                         "so `λ² − 4λ + 3 = 0`, which factors as `(λ − 1)·(λ − 3)`. "
                         "The eigenvalues are `1` and `3`.",
                         "For `λ = 1`, `(A − I)·v = 0` is the pair `v₁ + v₂ = 0` and "
                         "`v₁ + v₂ = 0`, one equation twice, so `v = (1, −1)`. For `λ = 3` "
                         "it is `−v₁ + v₂ = 0`, so `v = (1, 1)`.")),
            ("p", "The two equations are always the same equation, up to a multiple, "
                  "when `λ` is an eigenvalue. That is the quadratic's doing: the "
                  "determinant being zero means the two rows of `A − λ·I` are "
                  "parallel. So solving for `v` takes one equation, and any non-zero "
                  "solution of it will do."),
            ("math", [
                "A:  rows  2 1  and  1 2",
                "τ = 4,  Δ = 3,   λ² − 4λ + 3 = 0",
                "λ = 1:  (A − I)·v = 0    v₁ + v₂ = 0    v = (1, −1)",
                "λ = 3:  (A − 3I)·v = 0   −v₁ + v₂ = 0   v = (1, 1)",
            ]),
            ("thm", ("A straight-line solution",
                     "If `A·v = λ·v`, then `x(t) = e^(λt)·v` solves `x′ = A·x`.")),
            ("proof", ["Differentiate: `x′ = λ·e^(λt)·v`, because `v` is constant.",
                       "The other side is `A·x = e^(λt)·A·v = e^(λt)·λ·v`. They are equal "
                       "at every `t`. Each coordinate of `x` is a multiple of "
                       "the same exponential, so the point stays on the line through "
                       "`v`."]),
            ("p", "For the symmetric matrix the straight-line solutions are "
                  "`e^(t)·(1, −1)` and `e^(3t)·(1, 1)`. Check the second directly: "
                  "both coordinates are `e^(3t)`, so `x′ = 3e^(3t)`, and the "
                  "first equation says `x′ = 2x + y = 3e^(3t)`. They agree. Both "
                  "solutions move away from the origin, the second faster, because both "
                  "eigenvalues are positive."),
            ("h3", "Roots that are not rational"),
            ("p", "The quadratic does not always factor. For the matrix with rows "
                  "`1 1` and `1 0`, `τ = 1` and `Δ = −1`, so `λ² − λ − 1 = 0` and "
                  "`λ = (1 ± √5)/2`. The eigenvalues are exact surds, and the "
                  "lab prints them as such. Their eigenvectors exist, but have "
                  "irrational entries, and the lab prints a dash for the vectors rather than "
                  "a rounded guess. That is a limit of the lab, not of the "
                  "mathematics: the straight-line solutions are there to be found."),
            ("example", ("A direction written two ways",
                         "A student finds `(2, 2)` for the first matrix and the "
                         "lab prints `(1, 1)`. Test `(2, 2)`: `A·(2, 2) = (6, 6) = 3·(2, 2)`. "
                         "It is an eigenvector with eigenvalue `3`.",
                         "The two answers describe one line, the diagonal. The lab "
                         "reports the primitive vector because a direction has no "
                         "preferred length.")),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "field",
            "preset": "symmetric",
            "presets": [
                {"id": "symmetric", "label": "rows 2 1 and 1 2",
                 "A": [[2, 1], [1, 2]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppEig": "1, 3", "ppVectors": "(1, −1), (1, 1)"}},
                {"id": "saddle", "label": "rows 1 2 and 3 0",
                 "A": [[1, 2], [3, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppEig": "−2, 3", "ppVectors": "(2, −3), (1, 1)"}},
                {"id": "surd", "label": "rows 1 1 and 1 0",
                 "A": [[1, 1], [1, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppEig": "(1 ± √5)/2", "ppVectors": "—"}},
            ],
            "panel_title": "Find the eigenlines",
            "panel_intro": (
                "The field view draws the eigenlines through the origin when the "
                "eigenvalues are rational. Read the eigenvalue and eigenvector tiles "
                "against your own quadratic, and check that the arrows along each "
                "line point along it. The third preset has surd eigenvalues, so its "
                "vector tile is a dash."),
        }),
        "steps_title": "Finding the straight-line solutions",
        "steps_intro": "Trace and determinant first, then the roots, then one equation per root.",
        "steps": [
            ("Compute the trace and the determinant",
             "`τ = a + d` and `Δ = a·d − b·c`. For rows `1 2` and `3 0` they are `τ = 1` "
             "and `Δ = 0 − 6 = −6`."),
            ("Solve λ² − τ·λ + Δ = 0",
             "Here `λ² − λ − 6 = (λ − 3)·(λ + 2)`, so `λ = 3` and `λ = −2`. If it does not "
             "factor, use the formula and keep the surd."),
            ("Solve (A − λ·I)·v = 0 for each λ",
             "For `λ = 3` the first row is `−2·v₁ + 2·v₂ = 0`, so `v₁ = v₂` and `v = (1, 1)`. "
             "For `λ = −2` it is `3·v₁ + 2·v₂ = 0`, so `v = (2, −3)`. One row is enough."),
            ("Check one equation of the system",
             "Test `A·v = λ·v` on the vector you found: `A·(2, −3) = (1·2 + 2·(−3), "
             "3·2 + 0) = (−4, 6) = −2·(2, −3)`. It is an eigenvector for `−2`."),
            ("Write the solutions",
             "`e^(3t)·(1, 1)` and `e^(−2t)·(2, −3)`. The first runs out along the "
             "diagonal and the second runs in along a steeper line. Any non-zero "
             "multiple is as good."),
        ],
        "worked": {
            "title": "Rows 2 1 and 1 2: from the matrix to the diagonal solution",
            "intro": [
                "The first preset. Find the eigenvalues, the directions and the "
                "solution along the diagonal.",
            ],
            "lines": [
                "A:  rows  2 1  and  1 2,   trace 4,  determinant 3",
                "λ² − 4λ + 3 = 0,   (λ − 1)(λ − 3) = 0",
                "λ = 1 and λ = 3",
                "λ = 1:  v₁ + v₂ = 0,   v = (1, −1)",
                "λ = 3:  −v₁ + v₂ = 0,  v = (1, 1)",
                "along the diagonal:  x(t) = e^(3t)·(1, 1)",
                "check:  x′ = 3e^(3t),  2x + y = 3e^(3t)",
            ],
            "after": [
                "The lab prints the eigenvalues `1, 3` and the vectors `(1, −1), (1, 1)`, "
                "which is the same list written in the same order. Only the direction of "
                "a vector matters. Any other multiple, such as `(−1, 1)` or `(5, −5)`, "
                "is the same eigenvector for the purpose of the solution.",
                "The two eigenlines cut the plane into four regions, and a start "
                "in any region stays in it, because a solution cannot cross an "
                "eigenline: on the line it never leaves, so off it, it cannot "
                "arrive. The next lesson adds the two solutions together and gets "
                "all the rest.",
            ],
        },
        "quiz_title": "Directions, quadratics and checks",
        "quiz": [
            {"q": "A matrix has trace `5` and determinant `6`. What are its eigenvalues?",
             "a": ["`5` and `6`",
                   "`1` and `6`",
                   "`2` and `3`",
                   "`−2` and `−3`"],
             "c": 2,
             "why": "The quadratic is `λ² − 5λ + 6 = (λ − 2)·(λ − 3)`, so the roots are "
                    "`2` and `3`: they add to the trace and multiply to the determinant. "
                    "`5` and `6` are the coefficients, not the roots. `1` and `6` add to "
                    "`7`. `−2` and `−3` have the right product and the wrong sum."},
            {"q": "For the matrix with rows `2 1` and `1 2`, a student gives `(2, 2)` as the eigenvector for `λ = 3` and the lab prints `(1, 1)`. Which is right?",
             "a": ["Both are right, because they point along the same line",
                   "Only `(1, 1)`, because eigenvectors must have whole-number entries of smallest size",
                   "Only `(2, 2)`, because it has the bigger eigenvalue",
                   "Neither, because an eigenvector must have length `1`"],
             "c": 0,
             "why": "`A·(2, 2) = (6, 6) = 3·(2, 2)`, so `(2, 2)` is an eigenvector with "
                    "the same eigenvalue. An eigenvector is a direction, so any non-zero "
                    "multiple is the same answer. The lab prints the smallest "
                    "whole-number representative for convenience, not because the "
                    "others are wrong. Length plays no part."},
            {"q": "For rows `1 2` and `3 0` the eigenvalues are `3` and `−2`. Which is the straight-line solution that moves toward the origin?",
             "a": ["`e^(3t)·(1, 1)`",
                   "`e^(−2t)·(2, −3)`",
                   "`e^(−2t)·(1, 1)`",
                   "`e^(3t)·(2, −3)`"],
             "c": 1,
             "why": "A negative eigenvalue gives an exponential that shrinks, and `(2, −3)` "
                    "is the eigenvector that goes with `−2`. `e^(3t)` grows. The other two "
                    "pair an eigenvalue with the wrong eigenvector: `A·(1, 1) = (3, 3)`, "
                    "so `(1, 1)` belongs to `3`, not to `−2`."},
            {"q": "Why does a solution that starts on an eigenline never leave it?",
             "a": ["Because the field is zero on the line",
                   "Because the solution is `e^(λt)·v`, a scalar multiple of `v` at every `t`",
                   "Because eigenlines are always the axes",
                   "Because the eigenvalue is always positive"],
             "c": 1,
             "why": "The solution is a changing multiple of one fixed vector, so its "
                    "position is always on the line through `v`. The field is not zero "
                    "there: it points along the line, with length `|λ|` times the "
                    "distance. Eigenlines are the axes only for a diagonal matrix, and "
                    "negative eigenvalues work in the same way."},
        ],
        "mistakes": [
            ("Treating an eigenvector as a point",
             "A reader who finds `(2, 2)` and the lab shows `(1, 1)` concludes that one of them is "
             "wrong, because they are different points. They are the same direction: "
             "`A·(2, 2) = (6, 6) = 3·(2, 2)` and `A·(1, 1) = (3, 3) = 3·(1, 1)`. An eigenvector "
             "names a line through the origin, and the line has infinitely many points on it, all "
             "equally valid. Only the eigenvalue, `3`, is a single number."),
            ("Pairing a vector with the wrong eigenvalue",
             "With rows `1 2` and `3 0`, the vector `(2, −3)` goes with `−2`, not `3`. The "
             "test is the multiplication: `A·(2, −3) = (−4, 6) = −2·(2, −3)`. Swapped, "
             "the solution `e^(3t)·(2, −3)` fails the substitution, since its derivative "
             "is `3·e^(3t)·(2, −3)` while `A·x = −2·e^(3t)·(2, −3)`."),
            ("Solving for the eigenvector from the characteristic equation alone",
             "The quadratic gives only the eigenvalues. Each still needs its own equation "
             "`(A − λ·I)·v = 0`, solved separately. For `λ = 1` and `λ = 3` of the symmetric "
             "matrix that gave `v₁ + v₂ = 0` and `−v₁ + v₂ = 0`, which have different solutions, "
             "and no amount of staring at `λ² − 4λ + 3` produces either."),
        ],
        "standard": (
            "Finish when you can take a two-by-two matrix and write down the solutions that stay on straight lines.",
            "You should be able to compute the trace and determinant, solve the "
            "quadratic exactly, find one eigenvector per eigenvalue from a single "
            "equation, check it by multiplying, and write the straight-line "
            "solution e^(λt)·v."),
        "note": 'One straight-line solution is a thin slice of the picture. The sum of the two is the whole of it, and fitting that sum to a start is the work of &ldquo;The General Solution of a Linear System&rdquo;.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "the-general-solution-of-a-linear-system",
        "title": "The General Solution of a Linear System",
        "module": "Linear systems",
        "one_line": "Add the two straight-line solutions with constants, fit the constants to a start, and see which term wins.",
        "summary": (
            "When the matrix has two distinct real eigenvalues, every solution is "
            "`C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂`. The constants come from a two-by-two "
            "system at `t = 0`, and the exponents decide which term the curve follows "
            "as `t` grows. A start that is on neither eigenline picks up both."
        ),
        "key": [
            "x = C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂",
            "at t = 0:  C₁·v₁ + C₂·v₂ = start",
            "solve a 2 by 2 system for C₁, C₂",
            "t → ∞: the larger λ wins",
            "t → −∞: the smaller λ wins",
        ],
        "key_label": "Two solutions, two constants",
        "concepts_intro": (
            "Three ideas. A sum of solutions is a solution, the constants are fixed by "
            "where you start, and the exponents say where you end up."
        ),
        "concepts": [
            ("A sum of solutions is a solution",
             "If `x₁` and `x₂` solve `x′ = A·x`, so does `C₁·x₁ + C₂·x₂` for any "
             "numbers `C₁` and `C₂`, because both sides of the equation are linear in `x`. "
             "With the two straight-line solutions this gives a two-parameter family, "
             "and when the eigenvectors point in different directions the family "
             "contains a solution through every point."),
            ("The start fixes the constants",
             "At `t = 0` every exponential is `1`, so the general solution is "
             "`C₁·v₁ + C₂·v₂`. Setting that equal to the start `(x₀, y₀)` is a pair of "
             "linear equations in `C₁` and `C₂`. The eigenvectors are the columns of "
             "its matrix, and a pair of different directions makes it solvable "
             "exactly."),
            ("The larger exponent wins",
             "As `t` grows, `e^(λ₁t)` and `e^(λ₂t)` separate, and the term with the "
             "larger eigenvalue dwarfs the other. The curve bends to run parallel to "
             "that eigenline. Running time backwards swaps the roles: the term with the "
             "smaller eigenvalue wins as `t → −∞`."),
        ],
        "read_title": "Superposition, the constants, and the long run",
        "read_intro": "Why the sum is a solution, how to fit it in fractions, what each term does, and the place the lab stops.",
        "body": [
            ("thm", ("Superposition",
                     "If `x₁` and `x₂` solve `x′ = A·x`, then so does "
                     "`C₁·x₁ + C₂·x₂` for every pair of constants.")),
            ("proof", ["The derivative of the sum is `C₁·x₁′ + C₂·x₂′`, because constants "
                       "come out of derivatives.",
                       "Each `xᵢ′` equals `A·xᵢ`, so the derivative is "
                       "`C₁·A·x₁ + C₂·A·x₂ = A·(C₁·x₁ + C₂·x₂)`. That is `A` times the sum, "
                       "which is the equation again."]),
            ("def", ("The general solution",
                     "For distinct real eigenvalues `λ₁`, `λ₂` with eigenvectors "
                     "`v₁`, `v₂`, the <strong>general solution</strong> of `x′ = A·x` is "
                     "`x(t) = C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂`.",
                     "The constants `C₁` and `C₂` are fixed by a start, and the solution "
                     "through a given start is unique. The lab prints the formula "
                     "with the eigenvectors substituted in.")),
            ("example", ("Fitting a start in fractions",
                         "For rows `2 1` and `1 2` the eigenpairs are `(1, (1, −1))` and "
                         "`(3, (1, 1))`. To start at `(1, 0)` solve "
                         "`C₁·(1, −1) + C₂·(1, 1) = (1, 0)`.",
                         "That is `C₁ + C₂ = 1` and `−C₁ + C₂ = 0`. Adding gives "
                         "`2C₂ = 1`, so `C₂ = 1/2` and `C₁ = 1/2`. The solution is "
                         "`(1/2)·e^(t)·(1, −1) + (1/2)·e^(3t)·(1, 1)`.")),
            ("math", [
                "x(t) = (e^(t) + e^(3t))/2",
                "y(t) = (e^(3t) − e^(t))/2",
                "t = 0:   (1/2 + 1/2, 1/2 − 1/2) = (1, 0)",
                "x′ = (e^(t) + 3e^(3t))/2",
                "2x + y = (2e^(t) + 2e^(3t) + e^(3t) − e^(t))/2 = x′",
            ]),
            ("p", "The check is exact, and it is the one to keep doing. The start "
                  "matches at `t = 0`, and the first equation holds at every `t`, "
                  "because the two sides simplify to the same expression. Doing "
                  "only the first check would miss a wrong exponent; doing only "
                  "the second would miss a wrong constant."),
            ("h3", "Which term wins"),
            ("p", "In the solution above the exponent `3` beats the exponent `1`. For "
                  "large `t` the first term is a thin correction on the second, so the "
                  "curve points almost exactly along `(1, 1)`; its distance from the "
                  "diagonal, which the first term sets, still grows with `e^(t)`, only "
                  "far more slowly than the curve itself runs out. Going the other "
                  "way, toward negative `t`, both terms shrink and the first is the "
                  "bigger, so the curve comes out of the origin tangent to the line "
                  "through `(1, −1)`. That is the shape of every node: orbits hug the "
                  "slow eigenline at the origin and run parallel to the fast one far "
                  "away. A saddle is different, because its exponents have opposite "
                  "signs: there the orbit closes in on one eigenline as `t → ∞` and on "
                  "the other as `t → −∞`, which the second preset shows."),
            ("p", "A start on an eigenline has the other constant zero and never bends. "
                  "A start on neither has both. For the second preset, with rows "
                  "`1 2` and `3 0` and the eigenpairs `(−2, (2, −3))` and "
                  "`(3, (1, 1))`, the start `(3, 0)` lies on neither line, and "
                  "`2C₁ + C₂ = 3`, `−3C₁ + C₂ = 0` gives `C₁ = 3/5` and `C₂ = 9/5`. "
                  "The nearer eigenline to `(3, 0)` is the diagonal, and the solution "
                  "is still not the diagonal solution: the constant `C₁` is not zero."),
            ("example", ("Both terms decaying",
                         "For rows `−1 0` and `0 −2` the eigenvalues are `−1` and `−2` "
                         "with the axes as eigenvectors. From `(2, 2)` the constants "
                         "are `2` and `2`, and the solution is `(2e^(−t), 2e^(−2t))`.",
                         "Both terms die away. The one with exponent `−1` dies more "
                         "slowly, so it wins at the end, and the orbit comes into the origin "
                         "tangent to the `x`-axis.")),
            ("p", "The lab fits the constants only when its arithmetic stays rational. "
                  "For eigenvalues that are surds the constants would carry square roots "
                  "inside the formula, and the lab prints a dash rather than a "
                  "rounded guess. When the eigenvalues are complex or repeated "
                  "the general solution has a different shape, and the next lesson shows "
                  "what the picture does in each case."),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "solution",
            "preset": "symmetric",
            "presets": [
                {"id": "symmetric", "label": "rows 2 1 and 1 2, start (1, 0)",
                 "A": [[2, 1], [1, 2]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppGeneral": "C₁·e^t·(1, −1) + C₂·e^(3t)·(1, 1)", "ppC": "C₁ = 1/2, C₂ = 1/2"}},
                {"id": "saddle", "label": "rows 1 2 and 3 0, start (3, 0)",
                 "A": [[1, 2], [3, 0]], "start": [3, 0], "h": "1/4", "n": 8,
                 "expect": {"ppGeneral": "C₁·e^(−2t)·(2, −3) + C₂·e^(3t)·(1, 1)", "ppC": "C₁ = 3/5, C₂ = 9/5"}},
                {"id": "node", "label": "rows −1 0 and 0 −2, start (2, 2)",
                 "A": [[-1, 0], [0, -2]], "start": [2, 2], "h": "1/4", "n": 8,
                 "expect": {"ppGeneral": "C₁·e^(−2t)·(0, 1) + C₂·e^(−t)·(1, 0)", "ppC": "C₁ = 2, C₂ = 2"}},
            ],
            "panel_title": "Fit the constants to a start",
            "panel_intro": (
                "The solution view draws curves from several starts and the orbit "
                "through yours. Read the general solution and the constants in the "
                "tiles, and rebuild the constants by hand from the start. Then change "
                "the start to a point on an eigenline and watch one constant go to "
                "zero."),
        }),
        "steps_title": "Fitting the general solution",
        "steps_intro": "Eigenpairs first, the system for the constants second, and the long run last.",
        "steps": [
            ("Find the eigenpairs",
             "Solve `λ² − τ·λ + Δ = 0` and one equation `(A − λ·I)·v = 0` for each root. "
             "Keep the order, and keep each vector with its own eigenvalue."),
            ("Write the general solution",
             "`C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂`. Do not put in the start yet."),
            ("Set t = 0 and equate to the start",
             "Every exponential is `1`, so `C₁·v₁ + C₂·v₂ = (x₀, y₀)`. That is two "
             "equations, one for each coordinate."),
            ("Solve for the constants exactly",
             "Eliminate one constant and solve for the other, in fractions. Substitute "
             "back into both equations to check the start is matched."),
            ("Read the long run",
             "Compare the exponents. The term with the larger eigenvalue wins as "
             "`t → ∞` and the smaller as `t → −∞`. A constant that is zero removes "
             "its term altogether."),
        ],
        "worked": {
            "title": "Rows 2 1 and 1 2 from the start (1, 0)",
            "intro": [
                "The first preset. The eigenpairs from the last lesson are "
                "`λ = 1` with `(1, −1)` and `λ = 3` with `(1, 1)`.",
            ],
            "lines": [
                "x = C₁·e^(t)·(1, −1) + C₂·e^(3t)·(1, 1)",
                "t = 0:   C₁·(1, −1) + C₂·(1, 1) = (1, 0)",
                "C₁ + C₂ = 1",
                "−C₁ + C₂ = 0",
                "adding:  2·C₂ = 1,   C₂ = 1/2,   C₁ = 1/2",
                "x = (1/2)e^(t)(1, −1) + (1/2)e^(3t)(1, 1)",
                "large t:  the e^(3t) term wins, towards (1, 1)",
            ],
            "after": [
                "The lab prints the constants as `C₁ = 1/2, C₂ = 1/2`, and the formula in the "
                "general-solution tile has the same two terms. The start `(1, 0)` is "
                "on neither eigenline, which is why both constants are non-zero.",
                "For large `t` the diagonal term is far the larger, and the orbit "
                "runs out almost along the line through `(1, 1)`. It reaches that "
                "direction only in the limit. At every finite `t` the "
                "small term is still bending the orbit away from the line.",
            ],
        },
        "quiz_title": "Constants, sums and the long run",
        "quiz": [
            {"q": "For rows `2 1` and `1 2` with eigenpairs `(1, (1, −1))` and `(3, (1, 1))`, a start of `(3, 1)` gives which constants?",
             "a": ["`C₁ = 2`, `C₂ = 1`",
                   "`C₁ = 3`, `C₂ = 1`",
                   "`C₁ = 1`, `C₂ = 2`",
                   "`C₁ = 1/2`, `C₂ = 1/2`"],
             "c": 2,
             "why": "`C₁ + C₂ = 3` and `−C₁ + C₂ = 1` give `C₂ = 2` and `C₁ = 1`. Check: "
                    "`1·(1, −1) + 2·(1, 1) = (3, 1)`. The first choice swaps them. The "
                    "second reads the constants off the coordinates, which would be right "
                    "only if the eigenvectors were the axes. The last is the answer for "
                    "the start `(1, 0)`."},
            {"q": "As `t → ∞` on the solution `(1/2)e^(t)·(1, −1) + (1/2)e^(3t)·(1, 1)`, what direction does the curve approach?",
             "a": ["The direction `(1, −1)`, because its exponent is smaller",
                   "The direction `(1, 1)`, because its exponent is larger",
                   "The origin, because both exponentials are positive",
                   "The `x`-axis, because the start is on it"],
             "c": 1,
             "why": "The `e^(3t)` term outgrows the `e^(t)` term, so the curve lines up with "
                    "`(1, 1)`. The smaller exponent matters as `t → −∞`. Positive "
                    "exponents grow, so the curve leaves the origin and does not approach it. "
                    "The start being on an axis does not tie the orbit to it."},
            {"q": "For rows `1 2` and `3 0` and the start `(3, 0)`, the diagonal `(1, 1)` is the nearest eigenline. Which is true of the solution?",
             "a": ["It stays on the diagonal, because that line is nearest",
                   "It is `e^(3t)·(1, 1)`, since only that term grows",
                   "It has `C₁ = 3/5` and `C₂ = 9/5`, so it is on neither eigenline",
                   "It has `C₁ = 0`, because `(3, 0)` has a zero coordinate"],
             "c": 2,
             "why": "`2C₁ + C₂ = 3` and `−3C₁ + C₂ = 0` give `C₁ = 3/5` and `C₂ = 9/5`. "
                    "Both are non-zero, so both terms are present. Nearness is not "
                    "membership: only a start exactly on the line has the other constant "
                    "zero. A zero coordinate does not make a constant zero either."},
            {"q": "Which start gives a solution of rows `1 2` and `3 0` that stays on one straight line?",
             "a": ["`(3, 0)`",
                   "`(1, 0)`",
                   "`(1, −1)`",
                   "`(4, −6)`"],
             "c": 3,
             "why": "`(4, −6)` is twice `(2, −3)`, so it lies on the eigenline for `−2` and "
                    "the solution is `2e^(−2t)·(2, −3)`, which stays on the line. "
                    "`(3, 0)` and `(1, 0)` lie on neither eigenline. `(1, −1)` "
                    "is not a multiple of `(2, −3)` or of `(1, 1)`."},
        ],
        "mistakes": [
            ("Taking the solution through a point to be the nearest eigenvector solution",
             "For rows `1 2` and `3 0` the point `(3, 0)` is closer to the diagonal than "
             "to the line through `(2, −3)`, and a reader concludes the solution is "
             "`e^(3t)·(1, 1)`. That solution passes through `(1, 1)`, not through `(3, 0)`. "
             "Solving `2C₁ + C₂ = 3`, `−3C₁ + C₂ = 0` gives `C₁ = 3/5`, `C₂ = 9/5`: both "
             "terms are present, and the orbit curves from the line through `(2, −3)` "
             "toward the diagonal."),
            ("Putting the start into the solution before the constants are separate",
             "Writing `C·(e^(t)(1, −1) + e^(3t)(1, 1))` with a single constant gives only a "
             "one-parameter family, and no choice of `C` passes through both `(1, 0)` "
             "and `(1, 1)`. The general solution has one constant for each eigenvector, "
             "because the start has two coordinates to match."),
            ("Mixing up which exponent wins at which end",
             "The larger eigenvalue wins as `t → ∞` and the smaller as `t → −∞`. With "
             "eigenvalues `1` and `3` the diagonal wins at the far end of the future and "
             "`(1, −1)` wins at the far end of the past, since `e^(t)` is larger than "
             "`e^(3t)` when `t` is negative. Reading the same rule backwards swaps the two "
             "directions."),
        ],
        "standard": (
            "Finish when you can write the general solution of a system with two real eigenvalues and fit it to any start.",
            "You should be able to write C₁·e^(λ₁t)·v₁ + C₂·e^(λ₂t)·v₂, set t = 0, solve "
            "for the constants in exact fractions, check both the start and the "
            "equation, and say which term dominates at each end of time."),
        "note": 'The general solution assumes two real eigenvalues. When the trace and determinant give complex roots, repeated roots or a zero root, the picture changes character, and sorting those cases is the work of &ldquo;Saddles, Nodes, Spirals and Centres&rdquo;.',
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "saddles-nodes-spirals-and-centres",
        "title": "Saddles, Nodes, Spirals and Centres",
        "module": "Linear systems",
        "one_line": "The trace and determinant of the matrix sort every linear system in the plane into five pictures.",
        "summary": (
            "The eigenvalues of a two-by-two matrix are decided by its trace `τ` and "
            "determinant `Δ`, and so is the picture. A negative determinant gives a "
            "saddle. A positive one gives a node when `τ² − 4Δ` is positive, a spiral "
            "when it is negative, and a centre when the trace is also zero. The "
            "borderline cases are degenerate."),
        "key": [
            "Δ < 0:   saddle",
            "Δ > 0, τ² − 4Δ > 0:   node",
            "Δ > 0, τ² − 4Δ < 0, τ ≠ 0:   spiral",
            "Δ > 0, τ = 0:   centre",
            "τ² − 4Δ = 0:   degenerate or star node",
        ],
        "key_label": "Two numbers pick the picture",
        "concepts_intro": (
            "Three ideas. The roots multiply to the determinant, the discriminant says "
            "whether they are real, and the sign of the real part says which way "
            "the orbits go."
        ),
        "concepts": [
            ("The determinant is the product of the roots",
             "The roots of `λ² − τ·λ + Δ = 0` add to `τ` and multiply to `Δ`. A negative "
             "product means one positive root and one negative, so the system "
             "has a growing direction and a shrinking one: a saddle. A positive "
             "product means the roots share a sign, or are a complex pair."),
            ("The discriminant separates real from complex",
             "The roots are real when `τ² − 4Δ ≥ 0` and a complex pair when it is "
             "negative. For `Δ > 0` that is the line between a node, where "
             "orbits bend but never wind round the origin, and a spiral, where they turn "
             "around the origin as they go."),
            ("The real part decides in or out",
             "A complex pair has the form `α ± β·i`, and `α = τ/2`. The orbit turns "
             "around the origin at a rate set by `β` and spirals out when `α > 0`, in "
             "when `α < 0`. With `τ = 0` there is no growth or decay, and the orbit "
             "closes: a centre."),
        ],
        "read_title": "Five pictures from two numbers",
        "read_intro": "The classification and its short proof, the table of regions, one example in full, and the borderline cases the table does not settle.",
        "body": [
            ("thm", ("The trace–determinant classification",
                     "For `x′ = A·x` with trace `τ` and determinant `Δ`, the origin is "
                     "a saddle if `Δ < 0`. If `Δ > 0` it is a node when `τ² − 4Δ > 0`, a "
                     "spiral when `τ² − 4Δ < 0` and `τ ≠ 0`, and a centre when "
                     "`τ = 0`.")),
            ("proof", ["The roots add to `τ` and multiply to `Δ`. If `Δ < 0`, the product is "
                       "negative, so the roots are real and opposite in sign: a saddle.",
                       "If `Δ > 0` and `τ² − 4Δ > 0` the roots are real and have the same "
                       "sign, which is the sign of `τ`: a node. If `τ² − 4Δ < 0` the roots "
                       "are `τ/2 ± i·√(4Δ − τ²)/2`, a complex pair whose real part is `τ/2`: "
                       "a spiral if that is not zero. If `τ = 0` and `Δ > 0` the roots "
                       "are the purely imaginary `±i·√Δ`, and the real solutions are "
                       "cosines and sines of the same angle: closed curves around "
                       "the origin."]),
            ("math", [
                "Δ < 0                              saddle",
                "Δ > 0,  τ² − 4Δ > 0                node (stable if τ < 0)",
                "Δ > 0,  τ² − 4Δ < 0,  τ ≠ 0        spiral (stable if τ < 0)",
                "Δ > 0,  τ = 0                      centre",
                "Δ > 0,  τ² − 4Δ = 0                degenerate or star node",
            ]),
            ("p", "The classification is the whole of the story for a linear system in "
                  "the plane. Two exact numbers, computed from four entries, sort "
                  "every matrix with non-zero determinant. The dividing line between "
                  "nodes and spirals is the parabola `Δ = τ²/4` in the plane whose "
                  "axes are `τ` and `Δ`, and the lab prints `τ² − 4Δ` as its own tile so "
                  "that the side of the parabola is a number and not an impression."),
            ("example", ("A spiral",
                         "Take the matrix with rows `1 2` and `−2 1`. Then `τ = 2` and "
                         "`Δ = 1 + 4 = 5`, and `τ² − 4Δ = 4 − 20 = −16`. The "
                         "discriminant is negative, so the roots are complex: "
                         "`λ = 1 ± 2i`.",
                         "The real part `1` is positive, so orbits turn around the origin "
                         "and spiral out: an unstable spiral. The lab prints the roots as "
                         "`1 ± 2i` and calls the origin an unstable spiral.")),
            ("h3", "The other pictures"),
            ("p", "For rows `1 2` and `3 0`, `Δ = −6 < 0`, so the origin is a saddle with "
                  "eigenvalues `−2` and `3`. For rows `−1 0` and `0 −2`, `τ = −3` and "
                  "`Δ = 2`, so `τ² − 4Δ = 1 > 0` and the roots are real and "
                  "negative: a stable node, where every orbit comes into the origin. "
                  "For rows `0 2` and `−2 0`, `τ = 0` and `Δ = 4`, so `τ² − 4Δ = −16` "
                  "and `λ = ±2i`: a centre, with closed orbits."),
            ("p", "On the parabola itself, `τ² − 4Δ = 0` and there is one repeated root. "
                  "The matrix with rows `−1 1` and `0 −1` has `τ = −2`, `Δ = 1` and "
                  "the repeated root `−1`. It has only one eigenline, and orbits "
                  "bend round it as they come in: a degenerate node. A matrix that is "
                  "a multiple of the identity also has a repeated root, with every "
                  "direction an eigenvector, and is a star node instead."),
            ("p", "The line `Δ = 0` is not in the table. There one root is zero and the "
                  "origin is not an isolated equilibrium, which the next lesson "
                  "treats along with the stability criterion."),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "field",
            "preset": "spiral",
            "presets": [
                {"id": "saddle", "label": "saddle: rows 1 2 and 3 0",
                 "A": [[1, 2], [3, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "saddle", "ppDisc": "25"}},
                {"id": "node", "label": "node: rows −1 0 and 0 −2",
                 "A": [[-1, 0], [0, -2]], "start": [2, 2], "h": "1/4", "n": 8,
                 "expect": {"ppType": "stable node", "ppDisc": "1"}},
                {"id": "spiral", "label": "spiral: rows 1 2 and −2 1",
                 "A": [[1, 2], [-2, 1]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "unstable spiral", "ppDisc": "−16"}},
                {"id": "centre", "label": "centre: rows 0 2 and −2 0",
                 "A": [[0, 2], [-2, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "centre", "ppDisc": "−16"}},
                {"id": "degenerate", "label": "degenerate: rows −1 1 and 0 −1",
                 "A": [[-1, 1], [0, -1]], "start": [1, 1], "h": "1/4", "n": 8,
                 "expect": {"ppType": "degenerate node", "ppDisc": "0"}},
            ],
            "panel_title": "Sort five matrices by trace and determinant",
            "panel_intro": (
                "For each preset, compute the trace, the determinant and the "
                "discriminant by hand and name the type before you read the tiles. Then "
                "use the solution view to see the curves behind the name. Try "
                "changing one entry of the spiral matrix and watch which side of the "
                "parabola you land on."),
        }),
        "steps_title": "Classifying a matrix in three numbers",
        "steps_intro": "Determinant first, because it can finish the job at once; then the discriminant; then the trace.",
        "steps": [
            ("Compute τ and Δ",
             "`τ = a + d` and `Δ = a·d − b·c`, exactly. For rows `1 2` and `−2 1` they are "
             "`2` and `5`."),
            ("Check the sign of Δ",
             "If `Δ < 0` stop: it is a saddle. The roots have opposite signs, "
             "whatever else is true. If `Δ = 0` the origin is not isolated."),
            ("Compute τ² − 4Δ",
             "This is the discriminant. Here `4 − 20 = −16`. Positive means real roots, "
             "negative means a complex pair, zero means a repeated root."),
            ("Look at the trace",
             "For real roots the sign of `τ` is the sign of both: stable if negative. "
             "For a complex pair, `τ/2` is the real part. With `τ = 0` and `Δ > 0` the "
             "origin is a centre."),
            ("Confirm with the roots",
             "Solve the quadratic and check the type against them: `1 ± 2i` for this "
             "matrix has a positive real part, so the spiral is unstable."),
        ],
        "worked": {
            "title": "Rows 1 2 and −2 1: an unstable spiral",
            "intro": [
                "The spiral preset. Four numbers, three of them computed, and then "
                "the roots.",
            ],
            "lines": [
                "A:  rows  1 2  and  −2 1",
                "τ = 1 + 1 = 2",
                "Δ = 1·1 − 2·(−2) = 5",
                "τ² − 4Δ = 4 − 20 = −16 < 0:  complex roots",
                "λ² − 2λ + 5 = 0,   λ = 1 ± 2i",
                "real part 1 > 0:  orbits turn and move out",
                "unstable spiral",
            ],
            "after": [
                "The discriminant tile reads `−16` and the eigenvalue tile reads "
                "`1 ± 2i`. The determinant is positive, which rules out a saddle, "
                "and the trace is not zero, which rules out a centre.",
                "Change the sign of the `1`s on the diagonal and the real part becomes "
                "`−1`; the discriminant is still `−16`, and the same picture runs in "
                "the other direction, as a stable spiral.",
            ],
        },
        "quiz_title": "Reading the type from two numbers",
        "quiz": [
            {"q": "A matrix has `τ = −4` and `Δ = 3`. What is the origin?",
             "a": ["A stable spiral",
                   "A saddle",
                   "A centre",
                   "A stable node"],
             "c": 3,
             "why": "`τ² − 4Δ = 16 − 12 = 4 > 0`, so the roots are real; `Δ > 0` makes "
                    "them the same sign, and `τ < 0` makes that sign negative. The roots "
                    "are `−1` and `−3`. A spiral needs a negative discriminant, a saddle "
                    "needs `Δ < 0`, and a centre needs `τ = 0`."},
            {"q": "Which matrix has a centre at the origin?",
             "a": ["Rows `1 2` and `−2 1`",
                   "Rows `0 2` and `−2 0`",
                   "Rows `0 1` and `1 0`",
                   "Rows `−1 0` and `0 −1`"],
             "c": 1,
             "why": "Rows `0 2` and `−2 0` have `τ = 0` and `Δ = 4`, so the roots are `±2i`. "
                    "The first matrix has `τ = 2`, a spiral. Rows `0 1` and `1 0` have "
                    "`Δ = −1`, a saddle. The last has `τ = −2`, `Δ = 1` and a zero "
                    "discriminant: a star node."},
            {"q": "A matrix has `Δ = −6`. A student says the origin is stable because the determinant is negative. What is the best reply?",
             "a": ["Correct, since negative numbers shrink things",
                   "The origin is a node, but of unknown stability",
                   "A negative determinant means roots of opposite sign, so it is a saddle, and a saddle is not stable",
                   "A negative determinant means complex roots, so it is a spiral"],
             "c": 2,
             "why": "The roots multiply to `Δ`, so a negative product means one positive "
                    "and one negative root. The positive one makes most orbits leave. "
                    "It is not a node, and complex roots have a positive product "
                    "(`α² + β²`), never a negative one."},
            {"q": "For rows `−1 1` and `0 −1`, which statement is correct?",
             "a": ["Its discriminant is `0`, so the root `−1` is repeated, and it has one eigenline",
                   "Its discriminant is negative, so it is a spiral",
                   "Its trace is `0`, so it is a centre",
                   "Its determinant is `0`, so the origin is not isolated"],
             "c": 0,
             "why": "`τ = −2` and `Δ = 1`, so `τ² − 4Δ = 0`: a repeated root `−1`. "
                    "Only the direction `(1, 0)` is an eigenvector, which is what "
                    "makes the node degenerate. The trace is not zero and the "
                    "determinant is not zero."},
        ],
        "mistakes": [
            ("Thinking a negative determinant means the origin is stable",
             "The word negative suggests decay, but the determinant is the product of "
             "the two eigenvalues. With rows `1 2` and `3 0`, `Δ = −6` and the "
             "eigenvalues are `−2` and `3`: one shrinks and one grows. A start on the "
             "line through `(2, −3)` does decay, and every other start is pulled out "
             "along the diagonal. A stable origin needs both eigenvalues to decay, "
             "which needs `Δ > 0`."),
            ("Calling every pair of complex roots a centre",
             "A centre needs a purely imaginary pair, `τ = 0`. For rows `1 2` and `−2 1` the "
             "roots `1 ± 2i` are also complex, and the orbits turn, but the real part "
             "`1` makes them move steadily outward. Turning is the imaginary part, "
             "and in or out is the real part; both are needed."),
            ("Using the sign of the trace without checking the discriminant",
             "A negative trace does not on its own mean decay in every direction. With "
             "`τ = −1` and `Δ = −2` the roots are `1` and `−2`, a saddle, so the sign of "
             "`τ` must be read after `Δ`. The determinant is checked first for exactly this "
             "reason."),
        ],
        "standard": (
            "Finish when you can classify the origin of any linear system in the plane from three exact numbers.",
            "You should be able to compute τ, Δ and τ² − 4Δ, name the type among "
            "saddle, node, spiral, centre and the borderline cases, and give the "
            "roots that justify it."),
        "note": 'A name for the picture is half of the answer. The other half is whether solutions end up at the origin or leave it, and that is the criterion of &ldquo;Stability of the Origin&rdquo;.',
    },

    # ---------------------------------------------------------------- 05
    {
        "slug": "stability-of-the-origin",
        "title": "Stability of the Origin",
        "module": "Linear systems",
        "one_line": "The origin attracts every start exactly when the trace is negative and the determinant positive.",
        "summary": (
            "The origin of `x′ = A·x` is asymptotically stable when every solution "
            "tends to it, and that happens exactly when `τ < 0` and `Δ > 0`, which is the "
            "same as every eigenvalue having a negative real part. The borderline "
            "cases, a centre and a zero determinant, are stable without attracting or "
            "not isolated."),
        "key": [
            "stable exactly when  Δ > 0  and  τ < 0",
            "same as:  real parts of both λ negative",
            "τ = 0, Δ > 0:  centre, neutral",
            "Δ = 0:  a zero root, not isolated",
            "one negative root is not enough",
        ],
        "key_label": "Both roots must decay",
        "concepts_intro": (
            "Three ideas. Stability has degrees, the criterion needs both numbers, and "
            "the borderline cases are where the criterion stops deciding."),
        "concepts": [
            ("Stability has three degrees",
             "The origin is <em>asymptotically stable</em> when every solution tends "
             "to it, <em>stable</em> when solutions that start close stay close, and "
             "<em>unstable</em> when some solution leaves any neighbourhood. A centre "
             "is stable without being asymptotically stable: orbits stay close and "
             "do not settle."),
            ("The criterion needs both numbers",
             "The origin is asymptotically stable exactly when `τ < 0` and `Δ > 0`. The "
             "determinant rules out saddles and a zero root; the trace then decides "
             "between in and out. Neither number alone is enough."),
            ("It is about the real parts of the eigenvalues",
             "The condition is equivalent to every eigenvalue having a negative "
             "real part. Real roots must both be negative, and a complex pair "
             "`α ± β·i` needs `α < 0`. The trace is twice the real part for a complex "
             "pair, and the sum of the roots otherwise, which is why it gives the same "
             "answer."),
        ],
        "read_title": "The criterion, its proof, and the cases it does not settle",
        "read_intro": "The three degrees, the criterion with its short proof, the borderline cases and what Euler's steps do near them.",
        "body": [
            ("def", ("Stability of the origin",
                     "The origin is <strong>asymptotically stable</strong> when every "
                     "solution tends to it as `t → ∞`. It is <strong>stable</strong> when "
                     "every solution that starts near it stays near it. It is "
                     "<strong>unstable</strong> when some solution that starts "
                     "arbitrarily near it does not.",
                     "Asymptotic stability implies stability. A centre is stable and not "
                     "asymptotically stable.")),
            ("thm", ("The stability criterion",
                     "The origin of `x′ = A·x` is asymptotically stable exactly when "
                     "`τ < 0` and `Δ > 0`.")),
            ("proof", ["Suppose the roots are real. Their product is `Δ > 0`, so they have the "
                       "same sign, and their sum is `τ < 0`, so that sign is negative. "
                       "Every term of the general solution then decays.",
                       "Suppose the roots are `α ± β·i`. The real solutions are "
                       "multiples of `e^(αt)` times cosines and sines, as in &ldquo;Complex "
                       "Roots and Oscillation&rdquo;, and `α = τ/2 < 0`, so they decay.",
                       "Conversely, if `Δ < 0` there is a positive root. If `Δ > 0` and "
                       "`τ > 0` the real parts or the common sign are positive. In each "
                       "case some solution does not tend to the origin. The borderline "
                       "cases `τ = 0` and `Δ = 0` are treated below."]),
            ("example", ("A stable spiral",
                         "The matrix with rows `−1 2` and `−2 −1` has `τ = −2` and "
                         "`Δ = 1 + 4 = 5`. Both conditions hold. The discriminant is "
                         "`4 − 20 = −16`, so `λ = −1 ± 2i`.",
                         "Both roots have real part `−1`, so every solution carries a "
                         "factor `e^(−t)` and tends to the origin, turning as it goes. "
                         "It is a stable spiral. Compare the spiral in the last lesson: "
                         "the signs of the diagonal flipped, and the picture is the same "
                         "unwound.")),
            ("h3", "The borderline cases"),
            ("p", "At `τ = 0` with `Δ > 0` the roots are `±i·√Δ`, with real part zero. "
                  "Nothing grows and nothing decays; orbits are closed curves. For rows "
                  "`0 2` and `−2 0` they are circles, since "
                  "`(x² + y²)′ = 2x·(2y) + 2y·(−2x) = 0`. The origin is stable, because a "
                  "start near it stays near it, and it is not asymptotically stable, "
                  "because no orbit tends to it. The criterion says &ldquo;not asymptotically "
                  "stable&rdquo;, and does not say &ldquo;unstable&rdquo;."),
            ("p", "At `Δ = 0` one root is zero. The matrix with rows `−1 1` and `1 −1` "
                  "has `τ = −2`, `Δ = 0` and roots `0` and `−2`. The vector `(1, 1)` is "
                  "sent to zero, so every point of that line is an equilibrium: the "
                  "origin is not isolated. Every orbit comes in to the line from the side, "
                  "along the direction `(1, −1)`, and settles on it, but not at the "
                  "origin: the start `(1, 0)` has constants `1/2` and `1/2`, and ends "
                  "at `(1/2, 1/2)`. The lab calls this non-isolated equilibria."),
            ("p", "Euler's polygon follows its own arithmetic and can disagree with "
                  "the classification. On the centre, with `h = 1/4` the squared "
                  "distance from the origin is multiplied at each step by "
                  "`1 + 4·h² = 5/4`, which is the lab's ratio. The true orbit is a "
                  "circle and the polygon spirals out. The classification is a statement "
                  "about the equation. The polygon is a method applied to it, and the "
                  "gap between them is exactly the one the material clause names."),
            ("example", ("A saddle and the one stable line",
                         "For rows `1 2` and `3 0` the eigenvalues are `−2` and `3`. One of "
                         "them is negative, and the solution `e^(−2t)·(2, −3)` does tend "
                         "to the origin.",
                         "That is a single line of starts out of the whole plane. Any "
                         "start with a component along `(1, 1)` carries an `e^(3t)` term "
                         "that grows without limit. So one negative eigenvalue does not "
                         "make the origin stable: every eigenvalue has to be negative, "
                         "which `Δ < 0` rules out.")),
        ],
        "lab": ("dekit", {
            "mode": "phase",
            "view": "field",
            "preset": "stable-spiral",
            "presets": [
                {"id": "stable-spiral", "label": "stable spiral: rows −1 2 and −2 −1",
                 "A": [[-1, 2], [-2, -1]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "stable spiral", "ppTrace": "−2", "ppDet": "5"}},
                {"id": "centre", "label": "centre: rows 0 2 and −2 0",
                 "A": [[0, 2], [-2, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "centre", "ppTrace": "0", "ppDet": "4", "ppRatio": "5/4"}},
                {"id": "unstable-node", "label": "unstable node: rows 2 1 and 1 2",
                 "A": [[2, 1], [1, 2]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "unstable node", "ppTrace": "4", "ppDet": "3"}},
                {"id": "saddle", "label": "saddle: rows 1 2 and 3 0",
                 "A": [[1, 2], [3, 0]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "saddle", "ppTrace": "1", "ppDet": "−6"}},
                {"id": "line", "label": "zero determinant: rows −1 1 and 1 −1",
                 "A": [[-1, 1], [1, -1]], "start": [1, 0], "h": "1/4", "n": 8,
                 "expect": {"ppType": "non-isolated equilibria", "ppTrace": "−2", "ppDet": "0", "ppC": "C₁ = 1/2, C₂ = 1/2"}},
            ],
            "panel_title": "Apply the criterion",
            "panel_intro": (
                "Check the sign of the trace and of the determinant on each preset "
                "before you read the type tile. Then flip the signs of a matrix's "
                "entries and watch the criterion fail: the same picture runs the "
                "other way. On the centre, compare the Euler ratio with the circle "
                "behind it."),
        }),
        "steps_title": "Deciding stability from the matrix",
        "steps_intro": "Two signs, in order, with the borderline cases handled before the verdict.",
        "steps": [
            ("Compute τ and Δ",
             "Exactly, from the four entries. For rows `−1 2` and `−2 −1` they are `−2` and `5`."),
            ("Check Δ",
             "`Δ < 0` is a saddle and not stable. `Δ = 0` means a zero root and a line of "
             "equilibria. Only `Δ > 0` leaves the question open."),
            ("Check τ when Δ > 0",
             "`τ < 0` is asymptotically stable. `τ > 0` is unstable. `τ = 0` is a centre, "
             "which is stable and not asymptotically stable."),
            ("Confirm with the real parts",
             "Solve the quadratic. For real roots check both signs; for a complex "
             "pair read `τ/2`. `−1 ± 2i` has real part `−1`."),
            ("State the verdict in words",
             "Say which of the three degrees applies and why, naming the borderline case if "
             "that is the one in play."),
        ],
        "worked": {
            "title": "Rows −1 2 and −2 −1: a stable spiral",
            "intro": [
                "The first preset. Apply the criterion and confirm it with the roots.",
            ],
            "lines": [
                "A:  rows  −1 2  and  −2 −1",
                "τ = −1 + (−1) = −2 < 0",
                "Δ = (−1)(−1) − (2)(−2) = 5 > 0",
                "τ² − 4Δ = 4 − 20 = −16:  complex roots",
                "λ = −1 ± 2i,   real part −1 < 0",
                "every solution carries e^(−t):  it decays",
                "stable spiral",
            ],
            "after": [
                "Both signs pass, and the roots agree: the real part is `−1`. The lab "
                "tiles read `−2`, `5` and `stable spiral`.",
                "Change the sign of the trace and the same picture unwinds. The matrix "
                "with rows `1 −2` and `2 1` has `τ = 2` and the same discriminant, so "
                "the roots are `1 ± 2i` and the orbits turn outward. Stability is "
                "decided by the sign of the real part alone, and the trace carries it.",
            ],
        },
        "quiz_title": "Signs, roots and borderlines",
        "quiz": [
            {"q": "Which matrix has an asymptotically stable origin?",
             "a": ["Rows `1 2` and `3 0`",
                   "Rows `0 2` and `−2 0`",
                   "Rows `−1 2` and `−2 −1`",
                   "Rows `2 1` and `1 2`"],
             "c": 2,
             "why": "Rows `−1 2` and `−2 −1` have `τ = −2 < 0` and `Δ = 5 > 0`. The first has "
                    "`Δ = −6`, a saddle. The second has `τ = 0`, a centre, stable but not "
                    "asymptotically. The last has `τ = 4 > 0`, an unstable node."},
            {"q": "A matrix has eigenvalues `−3` and `+1`. Which is right?",
             "a": ["Stable, because one eigenvalue is negative and decays",
                   "Unstable, because the determinant is `−3`, so it is a saddle",
                   "Stable, because the trace `−2` is negative",
                   "Not stable or unstable, because the roots disagree"],
             "c": 1,
             "why": "The determinant is the product `−3`, and a saddle is unstable. The "
                    "`+1` direction grows from any start with a component on it. A negative "
                    "trace is necessary for stability but not sufficient, and the "
                    "roots disagreeing is exactly what makes it unstable."},
            {"q": "For rows `0 2` and `−2 0`, what is the correct description?",
             "a": ["Asymptotically stable, because the trace is not positive",
                   "Unstable, because orbits do not tend to the origin",
                   "Stable but not asymptotically stable: orbits are circles around the origin",
                   "Not an equilibrium, because the determinant is positive"],
             "c": 2,
             "why": "`τ = 0`, `Δ = 4`, roots `±2i`; the squared distance `x² + y²` is constant "
                    "along solutions. Nearby starts stay nearby (stable) and none tend to "
                    "the origin (not asymptotically). An orbit not tending to the origin "
                    "does not make it unstable. The origin is an equilibrium of every "
                    "linear system, since `A·0 = 0`."},
            {"q": "On the centre, the lab reports an Euler ratio of `5/4` for `h = 1/4`. What should you conclude?",
             "a": ["The origin of the system is unstable",
                   "The polygon's squared distance grows by `5/4` per step although the true orbit is a circle",
                   "The determinant is `5/4`",
                   "The true solution spirals out by `5/4` per unit of time"],
             "c": 1,
             "why": "The true squared distance is constant, since `(x² + y²)′ = 0`. The "
                    "factor `1 + 4h² = 5/4` belongs to the step size. Stability is a "
                    "property of the equation, not of the method. The determinant of "
                    "this matrix is `4`."},
        ],
        "mistakes": [
            ("Believing one negative eigenvalue makes the origin stable",
             "For rows `1 2` and `3 0` the eigenvalues are `−2` and `3`, and the solution "
             "`e^(−2t)·(2, −3)` really does tend to the origin. But the start `(1, 1)` gives "
             "`e^(3t)·(1, 1)`, which grows, and any start with a component along it does "
             "the same. Stability needs every eigenvalue to decay. Equivalently "
             "`Δ > 0`: here `Δ = −6`, and the criterion fails at the first check."),
            ("Reading a centre as unstable because orbits never reach the origin",
             "On rows `0 2` and `−2 0` no orbit tends to the origin, and a reader who "
             "defines stable as tends to concludes the origin is unstable. But a start at "
             "distance `1/10` stays at distance `1/10` for ever, since "
             "`x² + y²` is constant. Stable means nearby starts stay nearby, and a "
             "centre is the standard case where that holds without attraction."),
            ("Trusting Euler's polygon over the classification",
             "At `h = 1/4` the polygon on the centre has squared distance multiplied by "
             "`5/4` per step, which looks like instability. The ratio is exact, and it "
             "is a fact about the method: the equation's solutions are circles. A "
             "smaller step lowers the ratio towards `1`, and no step brings it to `1`. "
             "The verdict on the origin comes from the trace and the determinant."),
        ],
        "standard": (
            "Finish when you can decide the stability of the origin of a linear system from its trace and determinant, borderline cases included.",
            "You should be able to state the criterion, apply it in order (Δ first, "
            "then τ), name the centre as stable and not asymptotically stable, "
            "recognise a zero determinant as non-isolated equilibria, and connect "
            "the result to the signs of the real parts of the eigenvalues."),
        "note": 'The classification and the criterion are complete for linear systems. Real models are rarely linear, and what a classification says about a nonlinear equation near an equilibrium is the question the next half of the course takes up, starting with &ldquo;Nonlinear Systems and Their Equilibria&rdquo;.',
    },
]
