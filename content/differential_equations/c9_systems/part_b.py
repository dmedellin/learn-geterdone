"""Systems and the Phase Plane -- the second half (nonlinear systems).

Equilibria of a polynomial system found by hand and checked exactly, the Jacobian
that turns an equilibrium into a linear system, and three models read in the
phase plane: predator and prey, competing species and an epidemic.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py (mode
jacobian), by executing its shipped JavaScript under node, and pinned in `expect`.
The equilibrium checks, Jacobian entries, traces, determinants, eigenvalues and
thresholds are exact fractions or surds. The trajectories behind them are drawn by
stepping in floating point and the legend says so; no tile takes its value from a
drawn curve. A quadratic right-hand side doubles the digits of every Euler step, so
the lab does not step a nonlinear system exactly for long, and the lessons say so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "nonlinear-systems-and-equilibria",
        "title": "Nonlinear Systems and Their Equilibria",
        "module": "Nonlinear systems",
        "one_line": "A nonlinear system can rest at several points, and each one is found by making both rates zero at once.",
        "summary": (
            "An equilibrium of `x′ = f(x, y)`, `y′ = g(x, y)` is a point where `f` and "
            "`g` are both zero, so the arrow there vanishes and a solution that starts "
            "on it never leaves. A linear system with a non-zero determinant has one, "
            "at the origin. A nonlinear one can have none, one or several, and they are "
            "found by solving two equations together and checked by substituting both."
        ),
        "key": [
            "equilibrium:  f(x, y) = 0  and  g(x, y) = 0",
            "both at the same point, not each alone",
            "f = 0 and g = 0 are curves; they cross",
            "solve one for y, substitute into the other",
            "a bounded search can miss a point",
        ],
        "key_label": "Where both rates vanish",
        "concepts_intro": (
            "Three ideas. The first is the definition, the second is the method that "
            "finds the points, and the third is what an exact search can promise and "
            "what it cannot."
        ),
        "concepts": [
            ("An equilibrium is a zero of the arrow",
             "At a point where `f = 0` and `g = 0` the arrow is `(0, 0)`, so Euler's step "
             "adds nothing and the exact solution stays where it is. Both conditions are "
             "needed at the same point. A point where `f` is zero and `g` is not has `x` "
             "momentarily still while `y` moves, and the solution leaves it at once."),
            ("Solve the two equations together",
             "The set where `f = 0` is a curve and the set where `g = 0` is another; "
             "the equilibria are where the curves cross. By hand, solve one equation for "
             "one unknown, substitute into the other, and finish with the unknown you "
             "have left. Every root of that last equation gives one point, and each "
             "point is then checked in both equations."),
            ("A search covers only what it tried",
             "The lab can test every point of a grid of fractions exactly, and it "
             "reports what it found. That is a statement about the grid. An equilibrium "
             "with a denominator the grid never uses, or a coordinate beyond it, is not "
             "reported, and the status line says what the bounds were so the claim is "
             "never larger than the search."),
        ],
        "read_title": "Finding the points where nothing moves",
        "read_intro": "The definition, one system solved by hand, the check that rejects a near miss, and a search whose limits are stated.",
        "body": [
            ("def", ("Equilibrium of a system",
                     "A point `(x*, y*)` is an <strong>equilibrium</strong> of "
                     "`x′ = f(x, y)`, `y′ = g(x, y)` when `f(x*, y*) = 0` and "
                     "`g(x*, y*) = 0`.",
                     "The constant pair `x(t) = x*`, `y(t) = y*` is then a solution, "
                     "because both sides of both equations are zero. The curve where "
                     "`f = 0` is the <strong>x-nullcline</strong> and the curve where "
                     "`g = 0` is the <strong>y-nullcline</strong>.")),
            ("p", "A linear system `x′ = A·x` with a non-zero determinant has exactly one "
                  "equilibrium, the origin, because `A·x = 0` has only the solution "
                  "`x = 0`. Nothing like that holds once a product or a square enters. "
                  "Where the first half of the course asked what the origin does, the "
                  "first question now is how many places there are to ask it."),
            ("math", [
                "x′ = y − x²",
                "y′ = x − y",
            ]),
            ("p", "Take the system above. Its `x`-nullcline is the parabola `y = x²` and "
                  "its `y`-nullcline is the line `y = x`. Setting `g = 0` gives `y = x`; "
                  "putting that in `f = 0` gives `x − x² = 0`, which factors as "
                  "`x·(1 − x) = 0`, so `x = 0` or `x = 1`. The line then returns "
                  "`y = x`, and the two points are `(0, 0)` and `(1, 1)`."),
            ("example", ("Check both points in both equations",
                         "At `(0, 0)`: `f = 0 − 0 = 0` and `g = 0 − 0 = 0`. At `(1, 1)`: "
                         "`f = 1 − 1 = 0` and `g = 1 − 1 = 0`. Both are equilibria.",
                         "Now try `(2, 4)`, which lies on the parabola. There "
                         "`f = 4 − 4 = 0` but `g = 2 − 4 = −2`. The lab prints "
                         "`f = 0, g = −2: not an equilibrium`. The solution through "
                         "`(2, 4)` has `x` still for an instant and `y` falling at rate "
                         "`2`, so it moves on.")),
            ("h3", "What the grid search covers"),
            ("p", "Switch the search control on. The lab tests every point whose "
                  "coordinates are fractions with denominator 1, 2, 3 or 4 and "
                  "numerators between −12 and 12, exactly, and the status line names "
                  "those bounds as it reports. On the search preset only the origin is listed, and "
                  "the report is `found 2: (0, 0), (1, 1)`. It is a convenience for checking your own algebra, and "
                  "the algebra is the method."),
            ("p", "Its limit is built into the last preset. The system "
                  "`x′ = y − 5x²`, `y′ = x − y` has the equilibria `(0, 0)` and "
                  "`(1/5, 1/5)`, because `x = 5x²` gives `x = 0` or `x = 1/5`. The "
                  "denominator 5 is outside the grid, so the search reports only "
                  "the origin, while the second point passes the exact check in the "
                  "points list. A search that finds none, or one, has told you what "
                  "the grid holds and not how many there are."),
            ("p", "The same caution applies to the drawing. The arrows are shown for "
                  "orientation, and the check tile and the table come from substituting "
                  "the listed points into the equations, with no floating point anywhere "
                  "in the test. The tiles from the Jacobian down to the linearised type "
                  "belong to the next lesson; this one needs only the check."),
        ],
        "lab": ("dekit", {
            "mode": "jacobian",
            "view": "field",
            "search": "off",
            "preset": "parabola",
            "presets": [
                {"id": "parabola", "label": "y − x², x − y: both points",
                 "f": "y - x^2", "g": "x - y", "points": [[0, 0], [1, 1]], "start": None,
                 "expect": {"jbCheck": "is an equilibrium", "jbType": "saddle"}},
                {"id": "wrong", "label": "y − x², x − y: the point (2, 4)",
                 "f": "y - x^2", "g": "x - y", "points": [[2, 4], [0, 0], [1, 1]], "start": None,
                 "expect": {"jbCheck": "f = 0, g = −2: not an equilibrium"}},
                {"id": "search", "label": "y − x², x − y: switch the search on",
                 "f": "y - x^2", "g": "x - y", "points": [[0, 0]], "start": None,
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "−1"}},
                {"id": "off-grid", "label": "y − 5x², x − y: a point off the grid",
                 "f": "y - 5x^2", "g": "x - y", "points": [["1/5", "1/5"], [0, 0]], "start": None,
                 "expect": {"jbCheck": "is an equilibrium", "jbJ": "−2 1; 1 −1", "jbType": "stable node"}},
            ],
            "panel_title": "Check a point, then search",
            "panel_intro": (
                "Read the check tile for each listed point, then type a point of your "
                "own, as 1 1; 2 4, and watch the tile change. Switch the grid search "
                "on and read what it found in the status line below the figure. On the "
                "last preset, find the second equilibrium by hand before you look."),
        }),
        "steps_title": "Finding and checking the equilibria",
        "steps_intro": "Algebra first, because it finds every point; the lab second, because it tests the ones you found.",
        "steps": [
            ("Write both rates as zero",
             "Set `f(x, y) = 0` and `g(x, y) = 0`. Keep the two equations side by "
             "side; neither is solved alone."),
            ("Solve the simpler one for an unknown",
             "Choose the equation where one unknown appears to the first power. Here "
             "`x − y = 0` gives `y = x`."),
            ("Substitute into the other",
             "Replacing `y` by `x` in `y − x² = 0` gives `x − x² = 0`. Factor it: "
             "`x·(1 − x) = 0`. Every root gives a point, and none may be dropped by "
             "dividing out a factor."),
            ("Recover the other coordinate",
             "Put each root back into the equation you solved: `x = 0` gives `y = 0`, "
             "`x = 1` gives `y = 1`."),
            ("Check each point in both equations",
             "Substitute into `f` and `g`. Type the points into the lab and read the "
             "tile; a point that fails one equation is not an equilibrium."),
        ],
        "worked": {
            "title": "x′ = y − x², y′ = x − y: both equilibria and a near miss",
            "intro": [
                "The nullclines are a parabola and a line. Solve for their crossings, "
                "then test a point that lies on only one of them.",
            ],
            "lines": [
                "g = 0:  x − y = 0,  so  y = x",
                "f = 0:  y − x² = 0  becomes  x − x² = 0",
                "x·(1 − x) = 0,  so  x = 0  or  x = 1",
                "equilibria:  (0, 0)  and  (1, 1)",
                "(1, 1):  f = 1 − 1 = 0,  g = 1 − 1 = 0",
                "(2, 4):  f = 4 − 4 = 0,  g = 2 − 4 = −2",
                "(2, 4) is not an equilibrium",
            ],
            "after": [
                "The system has two equilibria, found by factoring one equation, and the "
                "lab agrees with both checks. The point `(2, 4)` is on the `x`-nullcline "
                "and not on the `y`-nullcline, and the tile prints the number that "
                "rules it out, `g = −2`.",
                "Neither equilibrium is the origin alone. The reason the origin was "
                "special for a linear system is gone, and what each of these two points "
                "does is the question of the next lesson.",
            ],
        },
        "quiz_title": "Rates, crossings and searches",
        "quiz": [
            {"q": "For `x′ = y − x²`, `y′ = x − y`, which point is an equilibrium?",
             "a": ["`(2, 4)`",
                   "`(1, 1)`",
                   "`(1, 0)`",
                   "`(0, 1)`"],
             "c": 1,
             "why": "At `(1, 1)` both `f = 1 − 1` and `g = 1 − 1` are zero. At `(2, 4)` "
                    "`f` is zero but `g = −2`. At `(1, 0)`, `f = −1`. At `(0, 1)`, `f = 1`."},
            {"q": "At `(2, 4)` the lab prints `f = 0, g = −2: not an equilibrium`. What does that say about the solution through `(2, 4)`?",
             "a": ["`y` is falling at rate `2` while `x` is momentarily still, so it moves away",
                   "It stays at `(2, 4)`, because one of the two rates is zero",
                   "It stays for an instant and then returns, because `g` is negative",
                   "It is an equilibrium of the `x` equation alone, so it counts as one"],
             "c": 0,
             "why": "The arrow at `(2, 4)` is `(0, −2)`, which is not zero, so the solution "
                    "moves. A point needs both rates to vanish; being a zero of one "
                    "equation is not enough, and a non-zero arrow gives no reason to return."},
            {"q": "How many equilibria does `x′ = x² − 1`, `y′ = y` have?",
             "a": ["`1`",
                   "`3`",
                   "`2`",
                   "`4`"],
             "c": 2,
             "why": "`y′ = 0` forces `y = 0`, and `x² − 1 = 0` gives `x = 1` or `x = −1`. The "
                    "points are `(1, 0)` and `(−1, 0)`. One would drop the root `−1`; four "
                    "would pair every root of one equation with every root of the other, "
                    "and three has no source at all."},
            {"q": "With the search on, the lab finds only `(0, 0)` for `x′ = y − 5x²`, `y′ = x − y`. What is the correct reading?",
             "a": ["`(1/5, 1/5)` is not an equilibrium, because the search did not list it",
                   "The search rounds, so it lost the point",
                   "The point `(1/5, 1/5)` is an equilibrium whose denominator `5` the grid does not use",
                   "The system has a single equilibrium"],
             "c": 2,
             "why": "`x = 5x²` gives `x = 0` or `x = 1/5`, and the exact test passes at "
                    "`(1/5, 1/5)`. The grid has denominators 1 to 4 only. The search does not round "
                    "anything. Its report is a statement about the grid it tried."},
        ],
        "mistakes": [
            ("Believing a nonlinear system has one equilibrium, at the origin",
             "The origin is the only equilibrium of a linear system with a non-zero "
             "determinant, and that habit carries over. For `x′ = y − x²`, `y′ = x − y` "
             "the origin is an equilibrium and so is `(1, 1)`, where `f = 1 − 1 = 0` "
             "and `g = 1 − 1 = 0`. A product term bends the nullclines, and bent curves "
             "cross where they like."),
            ("Checking only one of the two equations",
             "The point `(2, 4)` satisfies `y − x² = 0` and fails the other: `g = 2 − 4 = −2`. "
             "A solution of one equation is a point where one coordinate is still, and "
             "the other keeps moving it. The lab prints both numbers so the one that "
             "rules the point out is visible."),
            ("Dividing out a common factor and losing a point",
             "In `x·(1 − x) = 0` a reader who divides by `x` finds only `x = 1` and "
             "loses `(0, 0)`. Factor, and let each factor be zero in turn. The "
             "same applies to systems like `x·(3 − x − 2y)` later in this course, "
             "where each factor in a rate gives its own family of points."),
        ],
        "standard": (
            "Finish when you can find the equilibria of a polynomial system by hand and test each one exactly.",
            "You should be able to set both rates to zero, solve the pair by "
            "substitution without dropping a root, check every candidate in both "
            "equations, and say what a bounded search found and what it could not "
            "have found."),
        "note": 'Finding the points is half the work. What a solution does near each of them is the question &ldquo;Linearisation and the Jacobian&rdquo; answers.',
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "linearisation-and-the-jacobian",
        "title": "Linearisation and the Jacobian",
        "module": "Nonlinear systems",
        "one_line": "Near an equilibrium a nonlinear system looks like a linear one whose matrix is the Jacobian, except when that matrix is a centre.",
        "summary": (
            "Close to an equilibrium the curved terms are small, and the system behaves "
            "like `u′ = J·u`, where `J` is the matrix of partial derivatives of `f` and "
            "`g` at the point. Its trace and determinant give a saddle, node or spiral "
            "that the nonlinear system shares. When the classification is a centre or "
            "the determinant is zero, the Jacobian is inconclusive and the nonlinear "
            "terms decide."),
        "key": [
            "J: rows f_x f_y and g_x g_y at the point",
            "u′ = J·u,  u = (x − x*, y − y*)",
            "classify J by τ, Δ and τ² − 4Δ",
            "saddle, node, spiral: the system agrees",
            "centre or Δ = 0: inconclusive",
        ],
        "key_label": "The linear system closest to the point",
        "concepts_intro": (
            "Three ideas. The Jacobian is a matrix of rates of change, it turns a "
            "nonlinear equilibrium into a linear classification, and it is silent on "
            "exactly the cases where the linear classification has no strict sign."),
        "concepts": [
            ("The Jacobian collects the partial derivatives",
             "The partial derivative `f_x` is the derivative of `f` with respect to "
             "`x`, treating `y` as a constant: for `f = y − x²` it is `−2x`, and "
             "`f_y = 1`. The matrix with rows `f_x f_y` and `g_x g_y` is the "
             "<em>Jacobian</em>, and its entries are numbers once a point is chosen."),
            ("Near an equilibrium the system is the Jacobian system",
             "Write `u = (x − x*, y − y*)` for the displacement from the "
             "equilibrium. The rates `f` and `g` are zero at the point, and to first "
             "order they change by `f_x·(x − x*) + f_y·(y − y*)` and "
             "`g_x·(x − x*) + g_y·(y − y*)`: the tangent-line estimate of &ldquo;The "
             "Derivative at a Point and the Tangent Line&rdquo;, made once in each "
             "unknown. So `u′ = J·u` approximates the system close to the point, and "
             "its classification by trace and determinant is the one from the first "
             "half of the course."),
            ("A centre is where the approximation stops deciding",
             "The terms thrown away are smaller than the ones kept, but a centre "
             "has real part zero, so there is nothing left to be smaller than. Whether "
             "the curved terms push the orbits in, out, or leave them closed is "
             "then a different question, and the lab says so in the type tile."),
        ],
        "read_title": "From curves to a matrix, and where the matrix is not enough",
        "read_intro": "The Jacobian, two equilibria classified, the statement that licenses the method, and a system where it is silent.",
        "body": [
            ("def", ("The Jacobian at an equilibrium",
                     "For `x′ = f(x, y)`, `y′ = g(x, y)` the <strong>Jacobian</strong> at "
                     "a point is the matrix with rows `f_x f_y` and `g_x g_y`, each "
                     "partial derivative evaluated there.",
                     "The <strong>linearisation</strong> at an equilibrium is the linear "
                     "system `u′ = J·u` for the displacement `u` from the equilibrium.")),
            ("p", "For polynomials the partial derivatives are the power rule, once for "
                  "each unknown. Differentiate with respect to `x` and treat `y` as a "
                  "number; then do the reverse. On the system of the last lesson every "
                  "entry is a line or a constant."),
            ("math", [
                "f = y − x²      f_x = −2x      f_y = 1",
                "g = x − y       g_x = 1        g_y = −1",
            ]),
            ("example", ("Two equilibria, two classifications",
                         "At `(1, 1)` the rows are `−2 1` and `1 −1`. The trace is "
                         "`−3`, the determinant is `2 − 1 = 1`, and "
                         "`τ² − 4Δ = 9 − 4 = 5 > 0`. The roots are "
                         "`(−3 ± √5)/2`, both negative, so `(1, 1)` is a stable node.",
                         "At `(0, 0)` the rows are `0 1` and `1 −1`. The trace is `−1` "
                         "and the determinant is `0 − 1 = −1 < 0`, so it is a saddle. "
                         "The same system has a sink at one equilibrium and a saddle "
                         "at the other, which a linear system can never have.")),
            ("thm", ("Linearisation near an equilibrium",
                     "If no eigenvalue of `J` has real part zero, the equilibrium of the "
                     "nonlinear system is a saddle when the linear system is, and is "
                     "stable or unstable exactly as the linear system is.")),
            ("p", "The lab demonstrates this on the examples above and does not prove it: "
                  "the proof is a theorem of dynamical systems that this course states "
                  "and does not reach. What the lab does exactly is the matrix: the "
                  "entries, the trace, the determinant and the roots as fractions or "
                  "surds. Where a root is irrational, as `(−3 + √5)/2` is, the exact "
                  "form is the one to trust, and its value is rounded to `≈ −0.381966`."),
            ("h3", "When the Jacobian is not enough"),
            ("p", "Take `x′ = −y + x³`, `y′ = x + y³`. The origin is an equilibrium, "
                  "and the cubic terms have zero derivative there, so the rows of `J` "
                  "are `0 −1` and `1 0`: trace `0`, determinant `1`, roots `±i`. "
                  "The lab prints a centre and adds that the linearisation is "
                  "inconclusive."),
            ("proof", ["Let `D = x² + y²`, the squared distance from the origin, and compute how it changes along a solution.",
                       "`D′ = 2x·x′ + 2y·y′ = 2x·(−y + x³) + 2y·(x + y³) = 2x⁴ + 2y⁴`. The "
                       "cross terms `−2xy` and `+2xy` cancel, as they do for a "
                       "rotation, and the cubic terms are left.",
                       "The remaining sum is positive at every point except the "
                       "origin, so every solution moves away from it. The origin is "
                       "an unstable spiral, though the Jacobian reports a centre."]),
            ("p", "That is the whole content of the warning. Neither the trace nor the "
                  "determinant of the Jacobian was wrong; they described the best linear "
                  "approximation, and the answer needed more than a linear approximation. "
                  "The same is true when the determinant is zero and the lab prints "
                  "non-isolated equilibria."),
        ],
        "lab": ("dekit", {
            "mode": "jacobian",
            "view": "linearised",
            "search": "off",
            "preset": "parabola-origin",
            "presets": [
                {"id": "parabola-origin", "label": "y − x², x − y at (0, 0)",
                 "f": "y - x^2", "g": "x - y", "points": [[0, 0], [1, 1]], "start": None,
                 "expect": {"jbJ": "0 1; 1 −1", "jbType": "saddle", "jbEig": "(−1 ± √5)/2"}},
                {"id": "parabola-one", "label": "y − x², x − y at (1, 1)",
                 "f": "y - x^2", "g": "x - y", "points": [[1, 1], [0, 0]], "start": None,
                 "expect": {"jbJ": "−2 1; 1 −1", "jbType": "stable node", "jbEig": "(−3 ± √5)/2"}},
                {"id": "inconclusive", "label": "−y + x³, x + y³ at (0, 0)",
                 "f": "-y + x^3", "g": "x + y^3", "points": [[0, 0]], "start": None,
                 "expect": {"jbJ": "0 −1; 1 0", "jbType": "centre (linearisation inconclusive)", "jbEig": "±i"}},
            ],
            "panel_title": "Linearise at a chosen equilibrium",
            "panel_intro": (
                "The picture is the linear system built from the Jacobian, drawn about "
                "the point you select, and the tiles are exact. On the parabola "
                "presets, use the Linearise at control to move between the two points "
                "and compare the types. Then open the last preset and note what the type "
                "tile says about a centre."),
        }),
        "steps_title": "Linearising at an equilibrium",
        "steps_intro": "Partial derivatives first, then the point, then the same classification as before.",
        "steps": [
            ("Differentiate each rate in each unknown",
             "Four partial derivatives: `f_x`, `f_y`, `g_x`, `g_y`. In `f_x` treat "
             "`y` as a constant, and in `f_y` treat `x` as one. They are polynomials "
             "in `x` and `y`."),
            ("Substitute the equilibrium",
             "Evaluate all four at the point, not at the origin by habit. For "
             "`(1, 1)`, `−2x` becomes `−2`."),
            ("Compute the trace and determinant",
             "`τ = f_x + g_y` and `Δ = f_x·g_y − f_y·g_x`, exactly. At `(1, 1)` "
             "they are `−3` and `1`."),
            ("Classify as in the linear case",
             "Check `Δ` first, then `τ² − 4Δ`, then the sign of `τ`. Here "
             "`Δ > 0`, the discriminant is `5`, and `τ < 0`: a stable node."),
            ("Decide whether the verdict transfers",
             "If the result is a saddle, node or spiral, it transfers. If it is a "
             "centre, or the determinant is zero, say that the linearisation is "
             "inconclusive and look for a different argument."),
        ],
        "worked": {
            "title": "x′ = y − x², y′ = x − y: the node at (1, 1)",
            "intro": [
                "The first two presets. Linearise at `(1, 1)` and read the type, "
                "then do the origin.",
            ],
            "lines": [
                "f_x = −2x     f_y = 1     g_x = 1     g_y = −1",
                "at (1, 1):  J = rows  −2 1  and  1 −1",
                "τ = −2 + (−1) = −3",
                "Δ = (−2)(−1) − (1)(1) = 1",
                "τ² − 4Δ = 9 − 4 = 5 > 0:  λ = (−3 ± √5)/2",
                "both roots negative:  stable node",
                "at (0, 0):  τ = −1,  Δ = −1,  a saddle",
            ],
            "after": [
                "The tiles read the same exact values, `−3`, `1` and the surd form of "
                "the roots. The rounded values of the two roots are "
                "`≈ −0.381966` and `≈ −2.61803`, and both are negative, which is all the "
                "classification uses.",
                "So solutions that start close to `(1, 1)` settle on it, and almost all "
                "solutions that start close to the origin leave it, along the "
                "directions of the saddle.",
            ],
        },
        "quiz_title": "Matrix, type and trust",
        "quiz": [
            {"q": "For `f = y − x²`, `g = x − y`, which are the rows of the Jacobian at `(1, 1)`?",
             "a": ["`2 1` and `1 −1`",
                   "`−2 1` and `1 −1`",
                   "`0 1` and `1 −1`",
                   "`−2 1` and `1 1`"],
             "c": 1,
             "why": "`f_x = −2x = −2` at `x = 1`, `f_y = 1`, `g_x = 1`, `g_y = −1`. The first "
                    "choice drops the minus sign. The third is the matrix at the origin, "
                    "where `−2x = 0`. The last gets `g_y` wrong."},
            {"q": "A Jacobian has `τ = −3` and `Δ = 1`. What is the equilibrium?",
             "a": ["A stable node, because the discriminant is `5` and `τ < 0`",
                   "A saddle, because `τ` is negative",
                   "A stable spiral, because `τ < 0`",
                   "A centre, because `Δ` is positive"],
             "c": 0,
             "why": "`Δ > 0`, `τ² − 4Δ = 5 > 0` gives two real roots, and `τ < 0` makes "
                    "them negative. A saddle needs `Δ < 0`. A spiral needs a negative "
                    "discriminant. A centre needs `τ = 0`."},
            {"q": "The Jacobian of `x′ = −y + x³`, `y′ = x + y³` at the origin is a centre. What follows?",
             "a": ["The origin is a centre of the nonlinear system too",
                   "The origin is stable, because the trace is zero",
                   "The linearisation is inconclusive; here the squared distance `D = x² + y²` has `D′ = 2x⁴ + 2y⁴`, so the origin is unstable",
                   "The system has no equilibrium, because the roots are imaginary"],
             "c": 2,
             "why": "A centre is the case the Jacobian cannot decide. The squared distance "
                    "grows by `2x⁴ + 2y⁴ > 0`, so solutions leave the origin. Imaginary roots "
                    "of the Jacobian say nothing against `(0, 0)` being an equilibrium, "
                    "which it is."},
            {"q": "The Jacobian at an equilibrium has `Δ = −1`. What may you conclude about the nonlinear system?",
             "a": ["Nothing, because the nonlinear terms always change the answer",
                   "It is a stable node",
                   "It is a centre, because the nonlinear terms vanish at the point",
                   "It is a saddle there, and unstable"],
             "c": 3,
             "why": "A negative determinant means real roots of opposite signs, and none "
                    "has real part zero, so the saddle carries over. The nonlinear terms "
                    "change the answer only in the borderline cases. A node needs "
                    "`Δ > 0`, and a centre needs `τ = 0` with `Δ > 0`."},
        ],
        "mistakes": [
            ("Assuming the Jacobian's classification is always the nonlinear behaviour",
             "The Jacobian describes the best linear approximation. It carries over "
             "for a saddle, a node or a spiral, and fails on the borderline: for "
             "`x′ = −y + x³`, `y′ = x + y³` it reports a centre, while "
             "the squared distance `D = x² + y²` has `D′ = 2x⁴ + 2y⁴`, positive, so every solution spirals out. "
             "Trace and determinant were computed correctly. They were asked a question "
             "they cannot answer."),
            ("Evaluating the Jacobian at the wrong point",
             "The entries `−2x` depend on where you stand. The matrix with rows `0 1` and "
             "`1 −1` belongs to the origin; at `(1, 1)` the rows are `−2 1` and `1 −1`. "
             "Using the origin's matrix at `(1, 1)` gives `Δ = −1`, a saddle, where the "
             "truth is a stable node."),
            ("Letting y vary when differentiating with respect to x",
             "For `f = y − x²` the partial derivative `f_x` is `−2x`. A reader who "
             "substitutes `y = x` first writes `f = x − x²` and finds `1 − 2x`, which "
             "is the derivative along the line `y = x`, a different thing. Hold the other "
             "unknown fixed, differentiate, and only then substitute the point."),
        ],
        "standard": (
            "Finish when you can linearise a polynomial system at an equilibrium and say when the answer can be trusted.",
            "You should be able to compute the four partial derivatives, evaluate "
            "the Jacobian exactly at a chosen equilibrium, classify it by trace and "
            "determinant, and name the borderline case, a centre or a zero "
            "determinant, in which the classification does not transfer."),
        "note": 'The next three lessons use this method on models with a story: &ldquo;Predator and Prey&rdquo; first, because it lands in the one case the Jacobian cannot settle.',
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "predator-and-prey",
        "title": "Predator and Prey",
        "module": "Nonlinear systems",
        "one_line": "Foxes and rabbits cycle round a point instead of settling to it, and a conserved quantity, not the Jacobian, shows why.",
        "summary": (
            "The Lotka&ndash;Volterra system lets prey grow, predators die, and every "
            "meeting move one to the other. It has an equilibrium with both populations "
            "present, where the Jacobian has trace zero: a centre of the linearisation, "
            "which settles nothing. A quantity that stays constant along solutions "
            "does, and the drawn trajectory is a closed loop that matches it."),
        "key": [
            "x′ = 2x − x·y     prey",
            "y′ = −y + x·y     predators",
            "equilibria (0, 0) saddle, (1, 2) centre",
            "V = x − ln x + y − 2·ln y  is constant",
            "orbits are closed loops, not points",
        ],
        "key_label": "Two populations that chase each other",
        "concepts_intro": (
            "Three ideas. The model states its assumptions, the Jacobian gives a "
            "borderline answer, and a conserved quantity finishes the argument."),
        "concepts": [
            ("The model says who feeds on whom",
             "Let `x` be the prey and `y` the predators. Prey would grow at a rate "
             "proportional to `x` alone, predators would die at a rate proportional "
             "to `y` alone, and each meeting, which happens at a rate proportional to "
             "`x·y`, takes prey away and adds predators. With the numbers of this "
             "lesson, `x′ = 2x − x·y` and `y′ = −y + x·y`."),
            ("The interior equilibrium is a centre of the linearisation",
             "Setting `x·(2 − y) = 0` and `y·(x − 1) = 0` gives `(0, 0)` and `(1, 2)`. "
             "At `(1, 2)` the Jacobian has rows `0 −1` and `2 0`, so `τ = 0` and "
             "`Δ = 2`: roots `±i·√2`. That is the borderline case from the last "
             "lesson, and the type tile says the linearisation is inconclusive."),
            ("A conserved quantity decides it",
             "The function `V = x − ln x + y − 2·ln y` has the same value at every "
             "point of a solution. So a solution stays on one level curve of `V`, and "
             "near `(1, 2)` those level curves are closed loops. The populations then "
             "return to where they started, which neither settling nor spiralling "
             "away would do."),
        ],
        "read_title": "A system that does not settle",
        "read_intro": "The equations, both equilibria, the quantity the true solutions keep, and what the lab draws and what it cannot.",
        "body": [
            ("def", ("The Lotka&ndash;Volterra predator&ndash;prey system",
                     "<strong>Prey</strong> `x` and <strong>predators</strong> `y` obey "
                     "`x′ = α·x − β·x·y` and `y′ = −γ·y + δ·x·y`, where `α`, `β`, `γ` and "
                     "`δ` are positive constants.",
                     "The assumptions are named, not defended: prey have unlimited food "
                     "and grow without bound alone, predators starve alone, and a "
                     "meeting is as likely as the product of the two populations.")),
            ("math", [
                "x′ = 2x − x·y",
                "y′ = −y + x·y",
            ]),
            ("p", "Take `α = 2` and `β = γ = δ = 1`. The `x`-rate factors as "
                  "`x·(2 − y)` and the `y`-rate as `y·(x − 1)`. The prey grow while "
                  "there are fewer than `2` predators, and the predators grow while "
                  "there are more than `1` prey. Each nullcline is a pair of lines, "
                  "`x = 0` or `y = 2` for the first and `y = 0` or `x = 1` for the "
                  "second, and the crossings that matter are `(0, 0)` and `(1, 2)`."),
            ("example", ("Both equilibria and their Jacobians",
                         "The Jacobian has rows `2 − y, −x` and `y, x − 1`. At `(0, 0)` "
                         "the rows are `2 0` and `0 −1`: determinant `−2`, a saddle. "
                         "Prey grow along the `x`-axis and predators die along the "
                         "`y`-axis.",
                         "At `(1, 2)` the rows are `0 −1` and `2 0`: trace `0`, "
                         "determinant `2`, roots `±i·√2`. The lab prints a centre of the "
                         "linearisation, and that is all it can claim.")),
            ("thm", ("A quantity the solutions keep",
                     "Along every solution with `x > 0` and `y > 0`, "
                     "`V = x − ln x + y − 2·ln y` is constant.")),
            ("proof", ["Differentiate along a solution. The rate of `ln t` is `1/t`: that is the "
                       "claim &ldquo;The Integral of 1/t&rdquo; made in defining `ln x` as the integral "
                       "of `1/t` from `1` to `x`, and the one Separable Equations, Growth and Decay "
                       "used to integrate `1/y`. With the chain rule, applied here as a claim beyond "
                       "the polynomials it was verified on, `ln x` changes at the rate `x′/x` and "
                       "`ln y` at the rate `y′/y`.",
                       "`V′ = (1 − 1/x)·x′ + (1 − 2/y)·y′`, and substituting "
                       "`x′ = x·(2 − y)` and `y′ = y·(x − 1)` gives "
                       "`V′ = (x − 1)·(2 − y) + (y − 2)·(x − 1)`.",
                       "The two terms are negatives of each other, so `V′ = 0`. The value "
                       "of `V` never changes, and a solution is confined to a level curve."]),
            ("p", "The proof is algebra the reader has; what it does not show is that "
                  "the level curves are closed. That is a fact about the shape of "
                  "`V`, which has its smallest value at `(1, 2)` and rises on all "
                  "sides, and the lab does not prove it. It draws it. The trajectory "
                  "view steps the system in floating point from the start and the "
                  "legend says so, and the curve closes on the picture. A drawing is "
                  "evidence. The reason is the conserved quantity."),
            ("p", "Start at `(1, 2)` itself and the arrow is zero, so the point stays "
                  "for ever, and Euler's exact steps stay at `(1, 2)` too. Start "
                  "anywhere else in the first quadrant and the solution runs round "
                  "the point. Because `y′ > 0` only when `x > 1`, the predator "
                  "peak comes after the prey peak, and the loop is traversed "
                  "anticlockwise."),
        ],
        "lab": ("dekit", {
            "mode": "jacobian",
            "view": "trajectory",
            "search": "off",
            "preset": "classic",
            "presets": [
                {"id": "classic", "label": "2x − xy, −y + xy, start (1, 1)",
                 "f": "2x - x y", "g": "-y + x y", "points": [[1, 2], [0, 0]], "start": [1, 1],
                 "window": [0, 3, 0, 4],
                 "expect": {"jbCheck": "is an equilibrium", "jbTrace": "0", "jbDet": "2", "jbType": "centre (linearisation inconclusive)"}},
                {"id": "extinction", "label": "2x − xy, −y + xy at the origin",
                 "f": "2x - x y", "g": "-y + x y", "points": [[0, 0], [1, 2]], "start": [1, 1],
                 "window": [0, 3, 0, 4],
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "−2", "jbType": "saddle"}},
                {"id": "slow", "label": "x − xy/2, −y/2 + xy/4, start (1, 1)",
                 "f": "x - x y/2", "g": "-y/2 + x y/4", "points": [[2, 2], [0, 0]], "start": [1, 1],
                 "window": [0, 6, 0, 5],
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "1/2", "jbType": "centre (linearisation inconclusive)"}},
                {"id": "start-near", "label": "2x − xy, −y + xy, start (1, 2)",
                 "f": "2x - x y", "g": "-y + x y", "points": [[1, 2], [0, 0]], "start": [1, 2],
                 "window": [0, 3, 0, 4],
                 "expect": {"jbCheck": "is an equilibrium", "jbType": "centre (linearisation inconclusive)"}},
            ],
            "panel_title": "Watch a loop that does not close on a point",
            "panel_intro": (
                "The trajectory is drawn by stepping in floating point, and the short "
                "polygon with it is the first eight of Euler's exact steps at "
                "a step of 1/8. The tiles are exact and come from the listed points. "
                "Change the start to a point nearer the equilibrium and see the loop "
                "shrink; start at the equilibrium and it does not move."),
        }),
        "steps_title": "Reading a predator-prey system",
        "steps_intro": "Find the points, linearise, and when the linearisation is silent go to the conserved quantity.",
        "steps": [
            ("Factor each rate",
             "`x′ = x·(2 − y)` and `y′ = y·(x − 1)`. Each factor is a family of points "
             "where that rate is zero."),
            ("Pair the factors to find the equilibria",
             "`x = 0` with `y = 0`, and `y = 2` with `x = 1`. The other pairings give "
             "the same two points. Check each in both equations."),
            ("Linearise at each",
             "The rows `2 − y, −x` and `y, x − 1` become `2 0` and `0 −1` at the "
             "origin, a saddle, and `0 −1` and `2 0` at `(1, 2)`."),
            ("Notice the borderline",
             "`τ = 0` and `Δ = 2 > 0` at `(1, 2)`: a centre of the linearisation, which "
             "the Jacobian cannot decide."),
            ("Use the conserved quantity",
             "Show `V′ = 0` by substitution. Then read the drawn loop as agreeing with "
             "the level curves of `V`, and say that the drawing illustrates the "
             "argument rather than proving it."),
        ],
        "worked": {
            "title": "x′ = 2x − xy, y′ = −y + xy: the equilibria and the centre",
            "intro": [
                "The first preset, linearised at the interior equilibrium.",
            ],
            "lines": [
                "x′ = x·(2 − y)     y′ = y·(x − 1)",
                "equilibria:  (0, 0)  and  (1, 2)",
                "J (rows):  2 − y, −x  and  y, x − 1",
                "at (0, 0):  rows  2 0  and  0 −1,  Δ = −2:  saddle",
                "at (1, 2):  rows  0 −1  and  2 0",
                "τ = 0,  Δ = 2,  λ = ±i·√2",
                "centre of J:  inconclusive; V = x − ln x + y − 2·ln y",
            ],
            "after": [
                "The linearisation at `(1, 2)` is a centre, and the lab says so. "
                "The reason a closed loop is still the right answer is that "
                "`V′ = 0`, not that the Jacobian predicted it.",
                "The value of `V` at the start `(1, 1)` is `2`, while at the "
                "equilibrium it is `3 − 2·ln 2 ≈ 1.61371`, rounded. The start is on "
                "a bigger loop around the point, and the two never meet: the "
                "populations do not tend to `(1, 2)`.",
            ],
        },
        "quiz_title": "Equilibria, centres and loops",
        "quiz": [
            {"q": "Which is the equilibrium with both populations present for `x′ = 2x − x·y`, `y′ = −y + x·y`?",
             "a": ["`(2, 1)`",
                   "`(1, 1)`",
                   "`(1, 2)`",
                   "`(2, 2)`"],
             "c": 2,
             "why": "At `(1, 2)` both `x·(2 − y)` and `y·(x − 1)` are `0`. At `(2, 1)` the rate "
                    "`x′ = 2` is not zero, at `(1, 1)` it is `1`, and at `(2, 2)` the rate "
                    "`y′ = 2` is not zero."},
            {"q": "At `(1, 2)` the Jacobian has `τ = 0` and `Δ = 2`. What does the lab report, and what does that mean?",
             "a": ["Centre of the linearisation, inconclusive: the nonlinear terms decide",
                   "A stable spiral: the populations settle on the point",
                   "A saddle: one population always dies out",
                   "A centre of the nonlinear system, proved by the Jacobian"],
             "c": 0,
             "why": "`τ = 0` with `Δ > 0` is the borderline case. The Jacobian alone proves "
                    "neither a spiral nor a closed loop; the conserved quantity does the "
                    "proving. A saddle would need `Δ < 0`, and here `Δ = 2`."},
            {"q": "What does `V′ = 0` along a solution tell you?",
             "a": ["The populations are constant",
                   "The solution stays on one level curve of `V`, which near `(1, 2)` is a closed loop",
                   "The populations tend to `(1, 2)`",
                   "The equilibrium `(0, 0)` is stable"],
             "c": 1,
             "why": "A constant `V` keeps the solution on its level curve, so the "
                    "populations repeat; they are not constant, because the point moves "
                    "along the curve. Settling would need `V` to move towards its "
                    "minimum, and the origin is a saddle in any case."},
            {"q": "The lab draws a closed loop. What does the drawing establish?",
             "a": ["Nothing at all, because it is floating point",
                   "The result of exact Euler stepping, which is a closed loop",
                   "That the Jacobian was wrong",
                   "Evidence consistent with the conserved quantity; the proof is `V′ = 0` and the shape of `V`"],
             "c": 3,
             "why": "The curve is stepped in floating point, so it illustrates the argument "
                    "and does not prove it. It is not nothing: it agrees with the level "
                    "curves. It is not exact Euler stepping, which the lab shows "
                    "separately, and the Jacobian was not wrong, only silent."},
        ],
        "mistakes": [
            ("Expecting predators and prey to settle to constant populations",
             "The equilibrium `(1, 2)` exists, and a reader expects the populations to "
             "approach it. They do not. The start `(1, 1)` has `V = 2` and the "
             "equilibrium has `V = 3 − 2·ln 2 ≈ 1.61371`, rounded, and `V` never changes "
             "along a solution, so the start cannot reach the equilibrium. The "
             "populations go round it for ever, the roots `±i·√2` having no real "
             "part to make them decay."),
            ("Reading the drawn loop as a proof that the orbits close",
             "The trajectory is stepped in floating point. A closed-looking curve "
             "is what a correct conserved quantity predicts, and it is also what a "
             "very slow spiral would look like at this step size. The argument is "
             "`V′ = 0` together with the shape of `V`, and the picture is illustration."),
            ("Taking a centre of the Jacobian to be a centre of the model",
             "At `(1, 2)` the linearisation is a centre and so is the model, but the "
             "reasons are separate. The previous lesson's `x′ = −y + x³`, `y′ = x + y³` has "
             "the same linearisation and its orbits spiral out. What settled this "
             "system was a conserved quantity found for this system, not the Jacobian."),
        ],
        "standard": (
            "Finish when you can set up and analyse a predator-prey system.",
            "You should be able to write the Lotka–Volterra equations, find both "
            "equilibria exactly, show the interior one has trace zero, verify by "
            "substitution that the stated quantity is conserved, and say why the "
            "drawn trajectory illustrates the result without proving it."),
        "note": 'Predators take from prey. When two species instead take from the same food, the picture changes character, and &ldquo;Competing Species&rdquo; classifies all four equilibria.',
    },

    # ---------------------------------------------------------------- 09
    {
        "slug": "competing-species",
        "title": "Competing Species",
        "module": "Nonlinear systems",
        "one_line": "Two species that share food have four equilibria, and the Jacobians say whether they coexist or one wins.",
        "summary": (
            "In a competition model each species would grow logistically alone, and "
            "the other subtracts from its growth. Four equilibria matter: both extinct, "
            "either species alone, and a mixed state. The Jacobian at each sorts them, "
            "and the mixed state is a saddle when competition is strong, so the winner "
            "depends on the start, and a stable node when it is weak enough, so they "
            "coexist."),
        "key": [
            "x′ = x·(3 − x − 2y)    y′ = y·(2 − x − y)",
            "equilibria: origin, two axis points, (1, 1)",
            "classify each by its own Jacobian",
            "mixed point a saddle: no coexistence",
            "mixed point a node and stable: coexist",
        ],
        "key_label": "Four equilibria, four Jacobians",
        "concepts_intro": (
            "Three ideas. The equations come from a product of two factors, the factors "
            "give the four points, and the determinant at the mixed point decides the "
            "story."),
        "concepts": [
            ("Each rate is a factor times a factor",
             "In `x′ = x·(3 − x − 2y)` the species `x` grows logistically towards `3` "
             "when `y = 0`, and each unit of `y` costs it twice as much as a unit of "
             "itself. The rate is zero when `x = 0` or when the bracket is zero, and "
             "the same is true of `y`."),
            ("Pairing the factors gives four equilibria",
             "Either factor of the first rate with either factor of the second: "
             "`(0, 0)`, then `x = 0` with `2 − y = 0` for `(0, 2)`, then `y = 0` with "
             "`3 − x = 0` for `(3, 0)`, then both brackets zero: `x + 2y = 3` and "
             "`x + y = 2` give `(1, 1)`. Only points with both coordinates not "
             "negative are populations."),
            ("The determinant at the mixed point decides coexistence",
             "The mixed point is the only equilibrium where both species are present. "
             "If its Jacobian is a stable node or spiral, nearby starts end with both "
             "species. If the determinant is negative it is a saddle, almost every start "
             "leaves it, and one species ends alone."),
        ],
        "read_title": "Who survives when they share",
        "read_intro": "The model, the four points and four Jacobians worked out, and the version in which competition is weak enough for both to live.",
        "body": [
            ("def", ("A two-species competition model",
                     "<strong>Competing species</strong> `x` and `y` obey "
                     "`x′ = x·(r − α·x − β·y)` and `y′ = y·(s − γ·x − δ·y)`, with "
                     "positive constants.",
                     "The assumptions are named: each species grows logistically alone, "
                     "each crowds its own kind and the other kind, and nothing else "
                     "enters. This lesson uses the integer values below.")),
            ("math", [
                "x′ = x·(3 − x − 2y)",
                "y′ = y·(2 − x − y)",
            ]),
            ("p", "The two brackets are lines, `x + 2y = 3` and `x + y = 2`, and each "
                  "rate is zero on its own line or where its own species is zero. The "
                  "crossings are the four "
                  "equilibria, and one of them, `(1, 1)`, is where the lines cross. "
                  "At each the Jacobian is the same formula, with different numbers."),
            ("math", [
                "J rows:  3 − 2x − 2y, −2x  and  −y, 2 − x − 2y",
                "(0, 0):  rows  3 0  and  0 2     unstable node",
                "(3, 0):  rows  −3 −6  and  0 −1     stable node",
                "(0, 2):  rows  −1 0  and  −2 −2     stable node",
                "(1, 1):  rows  −1 −2  and  −1 −1     saddle",
            ]),
            ("example", ("The mixed point is a saddle",
                         "At `(1, 1)` the rows are `−1 −2` and `−1 −1`. The trace is "
                         "`−2` and the determinant is `1 − 2 = −1 < 0`, so it is a saddle.",
                         "A saddle has one direction that comes in and the rest go out. "
                         "A start exactly on the incoming curve settles at `(1, 1)`. "
                         "Every other start near it leaves, and ends at `(3, 0)` or "
                         "`(0, 2)`, both stable nodes. Which one depends on which side "
                         "of the incoming curve the start is on.")),
            ("p", "So in this model coexistence is an equilibrium that exists and does "
                  "not last, and the lab's tile for it reads `saddle`. The claim about "
                  "where nearby starts end is from the saddle and the two nodes, and "
                  "the trajectory view, drawn in floating point, shows one example from "
                  "the start the preset gives."),
            ("h3", "Weaker competition changes the answer"),
            ("p", "Now halve the cost of the other species: "
                  "`x′ = x·(2 − x − y/2)` and `y′ = y·(2 − y − x/2)`. The mixed "
                  "point is `(4/3, 4/3)`, since `2 − 4/3 − 2/3 = 0`. The Jacobian rows "
                  "there are `−4/3 −2/3` and `−2/3 −4/3`: trace `−8/3`, determinant "
                  "`16/9 − 4/9 = 4/3`, positive, and the roots are `−2/3` and `−2`. "
                  "A stable node: both species survive from every nearby start. "
                  "Competition is the same in kind in both models. The strength of "
                  "the cross terms decided whether the mixed point is a saddle or a sink."),
        ],
        "lab": ("dekit", {
            "mode": "jacobian",
            "view": "linearised",
            "search": "off",
            "preset": "exclusion",
            "presets": [
                {"id": "exclusion", "label": "strong competition at (1, 1)",
                 "f": "x(3 - x - 2y)", "g": "y(2 - x - y)",
                 "points": [[1, 1], [0, 0], [3, 0], [0, 2]], "start": ["11/10", "9/10"],
                 "window": [0, 4, 0, 3],
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "−1", "jbType": "saddle"}},
                {"id": "exclusion-corner", "label": "strong competition at (3, 0)",
                 "f": "x(3 - x - 2y)", "g": "y(2 - x - y)",
                 "points": [[3, 0], [0, 0], [0, 2], [1, 1]], "start": ["11/10", "9/10"],
                 "window": [0, 4, 0, 3],
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "3", "jbType": "stable node"}},
                {"id": "exclusion-other", "label": "strong competition at (0, 2)",
                 "f": "x(3 - x - 2y)", "g": "y(2 - x - y)",
                 "points": [[0, 2], [0, 0], [3, 0], [1, 1]], "start": ["9/10", "11/10"],
                 "window": [0, 4, 0, 3],
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "2", "jbType": "stable node"}},
                {"id": "coexist", "label": "weak competition at (4/3, 4/3)",
                 "f": "x(2 - x - y/2)", "g": "y(2 - y - x/2)",
                 "points": [["4/3", "4/3"], [0, 0], [2, 0], [0, 2]], "start": ["11/10", "9/10"],
                 "window": [0, 3, 0, 3],
                 "expect": {"jbCheck": "is an equilibrium", "jbDet": "4/3", "jbType": "stable node"}},
            ],
            "panel_title": "Classify all four equilibria",
            "panel_intro": (
                "Each preset lists four points and selects one. Use the Linearise at "
                "control to go through all four, and record the determinant and type "
                "of each. The tile for the selected point is exact; the portrait "
                "behind it is the linear system, drawn by stepping in floating point. "
                "Switch the view to a trajectory to see where one start ends."),
        }),
        "steps_title": "Classifying a competition model",
        "steps_intro": "Factor, pair, linearise four times, and then answer the question about the species.",
        "steps": [
            ("Factor both rates",
             "Write each as a species times a bracket: `x·(3 − x − 2y)` and "
             "`y·(2 − x − y)`. Do not multiply out."),
            ("Pair the factors",
             "Four pairings give four points: the origin, two axis points and the "
             "crossing of the brackets. Check each in both equations."),
            ("Write the Jacobian once",
             "Differentiate the products: `f_x = 3 − 2x − 2y`, `f_y = −2x`, "
             "`g_x = −y`, `g_y = 2 − x − 2y`."),
            ("Evaluate and classify at each point",
             "Substitute, then read `Δ`, the discriminant and `τ` in that order. The "
             "result at each point is a node or a saddle."),
            ("Answer the question about the species",
             "Coexistence needs the mixed point to be stable: `Δ > 0` and `τ < 0`. "
             "A saddle there means the outcome depends on the start."),
        ],
        "worked": {
            "title": "x′ = x(3 − x − 2y), y′ = y(2 − x − y): the mixed point",
            "intro": [
                "The first preset: find the mixed equilibrium from the two brackets and "
                "classify it.",
            ],
            "lines": [
                "x + 2y = 3  and  x + y = 2:  y = 1,  x = 1",
                "f_x = 3 − 2x − 2y   f_y = −2x",
                "g_x = −y            g_y = 2 − x − 2y",
                "at (1, 1):  rows  −1 −2  and  −1 −1",
                "τ = −2,   Δ = 1 − 2 = −1",
                "Δ < 0:  a saddle",
                "(3, 0) and (0, 2) are stable nodes",
            ],
            "after": [
                "The lab's tiles for the first preset confirm the point, read the "
                "determinant `−1` and name the saddle. Selecting `(3, 0)` and then "
                "`(0, 2)` in the control reads two stable nodes, and the grid search on "
                "this system reports `found 4: (0, 0), (0, 2), (1, 1), (3, 0)`.",
                "The model predicts that, from a start near `(1, 1)`, one species "
                "ends alone, and which one is the saddle's decision, not the "
                "model's luck.",
            ],
        },
        "quiz_title": "Four points and a verdict",
        "quiz": [
            {"q": "How many equilibria with non-negative coordinates does `x′ = x·(3 − x − 2y)`, `y′ = y·(2 − x − y)` have?",
             "a": ["`2`",
                   "`3`",
                   "`5`",
                   "`4`"],
             "c": 3,
             "why": "Pairing the factors gives `(0, 0)`, `(0, 2)`, `(3, 0)` and `(1, 1)`. "
                    "Two or three forget a pairing; five invents one, since two "
                    "lines cross in one point."},
            {"q": "At `(3, 0)` the Jacobian has rows `−3 −6` and `0 −1`. What is it?",
             "a": ["A saddle, because one entry is zero",
                   "A stable node with roots `−3` and `−1`",
                   "An unstable node, because `x` is large",
                   "A centre, because `y = 0`"],
             "c": 1,
             "why": "The trace is `−4` and the determinant is `3`, so the discriminant is "
                    "`16 − 12 = 4` and the roots are `−3` and `−1`. A zero entry says nothing "
                    "about the type, and the sign of the roots does."},
            {"q": "The mixed point has `Δ = −1`. What does the model predict?",
             "a": ["Both species coexist from every start",
                   "One species ends alone, whichever side of the saddle's incoming curve the start is on",
                   "Both species die out",
                   "The model makes no prediction near the point"],
             "c": 1,
             "why": "A saddle repels almost every nearby start, and the two stable nodes "
                    "at `(3, 0)` and `(0, 2)` are where they go. Coexistence needs a "
                    "stable node or spiral, and the saddle gives a prediction, not silence."},
            {"q": "In the weak-competition model the mixed point `(4/3, 4/3)` has `τ = −8/3` and `Δ = 4/3`. What follows?",
             "a": ["A stable node: nearby starts end with both species present",
                   "A saddle, because the species still compete",
                   "A centre, because the roots are rational",
                   "An unstable node, because the determinant is positive"],
             "c": 0,
             "why": "`Δ > 0` and `τ < 0` with discriminant `64/9 − 16/3 = 16/9 > 0` give "
                    "two negative roots. Competition alone does not make a saddle, "
                    "the roots are not imaginary, and a positive determinant with a "
                    "negative trace is stable."},
        ],
        "mistakes": [
            ("Thinking two competing species always drive one to extinction",
             "The strong-competition model does: its mixed point has `Δ = −1`, a "
             "saddle. A reader generalises. With the cross terms halved the mixed point "
             "`(4/3, 4/3)` has `τ = −8/3` and `Δ = 4/3`, a stable node, and both survive. "
             "Whether competition excludes depends on the numbers, and the determinant "
             "at the mixed point is where the lab shows it."),
            ("Equating an equilibrium with both species present with coexistence",
             "The point `(1, 1)` is an equilibrium of the strong-competition model, "
             "and both populations are positive there. But it is a saddle, so a "
             "population that reaches it is knocked off by any disturbance. Coexistence "
             "in the long run needs the equilibrium to be stable."),
            ("Dividing by x or y and losing the axis equilibria",
             "Dividing `x′ = 0` by `x` gives `3 − x − 2y = 0` and no more: the points "
             "`(0, 0)` and `(0, 2)` are lost, and with them both outcomes in which the "
             "first species is extinct. Both factors of each rate are zero in turn."),
        ],
        "standard": (
            "Finish when you can find and classify the equilibria of a competition model and say whether the species coexist.",
            "You should be able to factor the rates, list the four equilibria, "
            "compute the Jacobian at each, read the type from trace and "
            "determinant, and state whether the mixed point is stable and what that "
            "means for the species."),
        "note": 'One more model, and the one where the equilibria are not isolated: &ldquo;An Epidemic Model&rdquo;.',
    },

    # ---------------------------------------------------------------- 10
    {
        "slug": "an-epidemic-model",
        "title": "An Epidemic Model",
        "module": "Nonlinear systems",
        "one_line": "An outbreak grows while the susceptible fraction exceeds a threshold, peaks there, and ends with susceptibles left over.",
        "summary": (
            "The SIR model tracks the susceptible fraction `S` and the infected "
            "fraction `I`. The ratio `R₀ = β·S₀/γ` says whether an outbreak grows at "
            "first, the infected peak when `S` falls to `γ/β`, and every point with "
            "`I = 0` is an equilibrium, so the equilibria are not isolated. The "
            "epidemic ends because the infected run out, not the susceptibles."),
        "key": [
            "S′ = −β·S·I     I′ = β·S·I − γ·I",
            "R₀ = β·S₀/γ > 1:  I grows at first",
            "I peaks where S = γ/β",
            "I = 0: a line of equilibria, Δ = 0",
            "it ends with S above zero",
        ],
        "key_label": "A threshold, a peak, and a leftover",
        "concepts_intro": (
            "Three ideas. The model has two equations, the threshold is one number "
            "from them, and the equilibria are a line, not points."),
        "concepts": [
            ("Two equations track the outbreak",
             "Let `S` be the fraction who can still be infected and `I` the fraction "
             "who are infected now. Meetings between the two happen at a rate "
             "proportional to `S·I`; each moves someone from `S` to `I` at "
             "strength `β`, and the infected recover at rate `γ`. The recovered need "
             "no equation of their own, since nothing depends on them."),
            ("R₀ is the number that says whether it grows",
             "Write `I′ = I·(β·S − γ)`. The infected grow exactly when "
             "`β·S > γ`. At the start that is `R₀ = β·S₀/γ > 1`, and `I` reaches its "
             "peak when `S` has fallen to `γ/β`, because `S` only ever decreases."),
            ("Equilibria form a line",
             "Setting `I = 0` makes both rates zero for any `S`. So every point of "
             "the `S`-axis is an equilibrium, and the Jacobian there has zero "
             "determinant. The lab reports non-isolated equilibria, and the "
             "Jacobian's remaining eigenvalue says whether the point is approached "
             "or left."),
        ],
        "read_title": "How an outbreak rises, peaks and stops",
        "read_intro": "The model, the threshold worked out exactly, why the equilibria are a line, and the reason the epidemic ends.",
        "body": [
            ("def", ("The SIR model without the recovered",
                     "With <strong>S</strong> susceptible and <strong>I</strong> infected "
                     "fractions, `S′ = −β·S·I` and `I′ = β·S·I − γ·I`, with `β` "
                     "the transmission rate and `γ` the recovery rate.",
                     "The assumptions are named: a fixed population, everyone mixing "
                     "equally, immunity after recovery, no births and deaths. The "
                     "<strong>basic reproduction number</strong> at the start is "
                     "`R₀ = β·S₀/γ`.")),
            ("math", [
                "S′ = −β·S·I",
                "I′ = β·S·I − γ·I",
                "R₀ = β·S₀/γ",
            ]),
            ("p", "Take `β = 1/2`, `γ = 1/4`, and start at `S₀ = 9/10`, `I₀ = 1/10`. Then "
                  "`R₀ = (1/2)·(9/10)/(1/4) = 9/5`, greater than `1`. The factor "
                  "`β·S − γ` in `I′ = I·(β·S − γ)` is positive while "
                  "`S > γ/β = 1/2`, so `I` rises. It is zero at `S = 1/2`, and negative "
                  "after, so `I` peaks exactly when `S` reaches `1/2`. The lab "
                  "prints this as `R₀ = 9/5; I peaks at S = 1/2`."),
            ("example", ("A start below the threshold",
                         "Raise the recovery rate to `γ = 1` with the same `β` and start. "
                         "Then `R₀ = (1/2)·(9/10)/1 = 9/20 < 1`, and the peak "
                         "would be at `S = γ/β = 2`, which `S` never reaches. The "
                         "factor `β·S − γ` is negative from the start, so `I` falls "
                         "at once. The lab prints that `I` falls from the start.",
                         "The same disease with a faster recovery never takes off, "
                         "which is what the single number `R₀` is for.")),
            ("p", "Every point `(S, 0)` is an equilibrium, because both rates have a "
                  "factor `I`. At `(9/10, 0)` the Jacobian has rows `0 −9/20` and "
                  "`0 1/5`, so the determinant is zero, the trace is `1/5`, and "
                  "the roots are `0` and `1/5`. The positive root is the outbreak: "
                  "a few infected at `S = 9/10` start to grow. The lab's type tile "
                  "reads non-isolated equilibria, which here means a line, not "
                  "a point. Switch the grid search on and the status line reports "
                  "`found 65`, every one of them on the line `I = 0`: that is the "
                  "grid's own count, and the true number is infinite."),
            ("thm", ("Why the epidemic ends with susceptibles left",
                     "Along every solution, "
                     "`S + I − (γ/β)·ln S` is constant.")),
            ("proof", ["Call the quantity `W = S + I − (γ/β)·ln S` and differentiate it along a solution. The term `ln S` changes at the rate `S′/S`, which is `−β·I`, by the rate of `ln` and the chain rule exactly as &ldquo;Predator and Prey&rdquo; used them.",
                       "`W′ = S′ + I′ − (γ/β)·S′/S = −β·S·I + (β·S·I − γ·I) + γ·I`.",
                       "The terms cancel in pairs, so the quantity is constant. If `S` "
                       "tended to `0`, then `−(γ/β)·ln S` would grow without limit while "
                       "`S` and `I` stay between `0` and `1`, and the constant could "
                       "not hold. So `S` stays above zero."]),
            ("p", "That is the correct reason an epidemic ends. The infected "
                  "decline once `S` has fallen below `γ/β`, because each infected "
                  "person then passes the disease to fewer than one other before "
                  "recovering, and `I` runs down to zero. A positive fraction of the "
                  "population is never infected. The drawn trajectory in the lab "
                  "shows `S` levelling off above zero; it is floating point, and the "
                  "argument is the conserved quantity."),
        ],
        "lab": ("dekit", {
            "mode": "jacobian",
            "view": "trajectory",
            "search": "off",
            "preset": "outbreak",
            "presets": [
                {"id": "outbreak", "label": "outbreak: S0 = 9/10, I0 = 1/10",
                 "f": "-S I/2", "g": "S I/2 - I/4", "vars": ["S", "I"],
                 "points": [["9/10", 0]], "start": ["9/10", "1/10"], "extra": "sir",
                 "window": [0, 1, 0, "3/10"],
                 "expect": {"jbExtra": "R₀ = 9/5; I peaks at S = 1/2", "jbType": "non-isolated equilibria"}},
                {"id": "contained", "label": "faster recovery: S0 = 9/10, I0 = 1/10",
                 "f": "-S I/2", "g": "S I/2 - I", "vars": ["S", "I"],
                 "points": [["9/10", 0]], "start": ["9/10", "1/10"], "extra": "sir",
                 "window": [0, 1, 0, "3/10"],
                 "expect": {"jbExtra": "R₀ = 9/20; I falls from the start", "jbType": "non-isolated equilibria"}},
                {"id": "everyone-susceptible", "label": "almost everyone susceptible: S0 = 99/100",
                 "f": "-S I/2", "g": "S I/2 - I/4", "vars": ["S", "I"],
                 "points": [["99/100", 0]], "start": ["99/100", "1/100"], "extra": "sir",
                 "window": [0, 1, 0, "3/10"],
                 "expect": {"jbExtra": "R₀ = 99/50; I peaks at S = 1/2", "jbType": "non-isolated equilibria"}},
            ],
            "panel_title": "Find the threshold and the peak",
            "panel_intro": (
                "The threshold tile is computed exactly from the coefficients you "
                "type and the start. Change the start and watch R₀ move across 1. The "
                "trajectory is drawn by stepping in floating point; the peak "
                "of the infected curve should sit where S crosses the value in the "
                "tile."),
        }),
        "steps_title": "Reading an epidemic from its two equations",
        "steps_intro": "Read the coefficients, compute the threshold, and place the peak.",
        "steps": [
            ("Read β and γ off the equations",
             "From `S′ = −β·S·I` read `β` as the size of the `S·I` coefficient; from "
             "`I′ = β·S·I − γ·I` read `γ` as the size of the coefficient of `I` on its "
             "own. Here `β = 1/2` and `γ = 1/4`."),
            ("Compute R₀ from the start",
             "`R₀ = β·S₀/γ`. With `S₀ = 9/10` it is `9/5`. Compare it with `1`."),
            ("Find the peak",
             "`I′ = 0` where `S = γ/β`. If `S₀` is above it, `I` rises first and "
             "peaks there. If `S₀` is below it, `I` falls from the start."),
            ("Check the equilibria",
             "`I = 0` for any `S`. The Jacobian has determinant zero, so the lab "
             "prints non-isolated equilibria, and its positive root says an outbreak "
             "can start."),
            ("Say why it ends",
             "`I` declines after the peak because `S` is below `γ/β`, and it never "
             "needs `S` to reach zero. The quantity `S + I − (γ/β)·ln S` is "
             "constant, which keeps `S` positive."),
        ],
        "worked": {
            "title": "β = 1/2, γ = 1/4, S₀ = 9/10: threshold and peak",
            "intro": [
                "The first preset. Compute the threshold and the peak by hand, then "
                "read them from the tile.",
            ],
            "lines": [
                "β = 1/2   γ = 1/4   S₀ = 9/10",
                "R₀ = (1/2)(9/10) / (1/4) = 9/5 > 1",
                "I′ = I·(S/2 − 1/4)  is positive while S > 1/2",
                "I peaks where S = γ/β = (1/4)/(1/2) = 1/2",
                "at (9/10, 0):  rows  0 −9/20  and  0 1/5",
                "Δ = 0:  the equilibria are not isolated",
                "S + I − (1/2)·ln S is constant, so S stays above 0",
            ],
            "after": [
                "The exact tile reads `R₀ = 9/5; I peaks at S = 1/2`, as computed. "
                "When `S` is at `1/2`, half the population has not been infected, "
                "and the infection falls from there.",
                "So the outbreak ends because the infected fraction has run down "
                "while many are still susceptible. It did not end because everyone "
                "had been through it.",
            ],
        },
        "quiz_title": "Threshold, peak and ending",
        "quiz": [
            {"q": "For `S′ = −S·I/2`, `I′ = S·I/2 − I/4` and `S₀ = 9/10`, what is `R₀`?",
             "a": ["`9/20`",
                   "`9/5`",
                   "`1/2`",
                   "`9/10`"],
             "c": 1,
             "why": "`R₀ = β·S₀/γ = (1/2)(9/10)/(1/4) = 9/5`. The choice `9/20` divides by `γ = 1` "
                    "instead of `1/4`, `1/2` is the peak value of `S`, and `9/10` is `S₀` itself."},
            {"q": "At what value of `S` does `I` reach its peak in that model?",
             "a": ["`S = 0`, when everyone has been infected",
                   "`S = 9/10`, the start",
                   "`S = 9/5`, the value of `R₀`",
                   "`S = 1/2`, where `β·S = γ`"],
             "c": 3,
             "why": "`I′ = I·(β·S − γ)` changes sign at `S = γ/β = 1/2`. The infection "
                    "has not infected everyone by then, `S = 9/10` is where it starts "
                    "to grow, and `R₀` is a ratio, not a fraction of the population."},
            {"q": "With `γ = 1` the lab prints `R₀ = 9/20` and that `I` falls from the start. Why?",
             "a": ["`S` is below `γ/β = 2` from the beginning, so `β·S − γ` is negative",
                   "`I` is too small to spread",
                   "The recovered have used up the susceptibles",
                   "Euler's method has the wrong sign"],
             "c": 0,
             "why": "`β·S − γ = 9/20 − 1 < 0` at the start and stays negative as `S` falls. "
                    "The size of `I` does not matter, since `I′ = I·(β·S − γ)` keeps the "
                    "sign of the bracket. Nothing has recovered yet, and no stepping "
                    "method enters the tile."},
            {"q": "The type tile at `(9/10, 0)` reads non-isolated equilibria. What does that mean?",
             "a": ["Every point `(S, 0)` is an equilibrium, so the determinant is `0`",
                   "The equilibrium has two zero roots",
                   "The origin is the only equilibrium",
                   "The lab could not find the equilibrium"],
             "c": 0,
             "why": "Both rates have a factor `I`, so the whole `S`-axis is a line of equilibria. "
                    "The roots at `(9/10, 0)` are `0` and `1/5`, so only one is zero. "
                    "The origin is one point of the line, and the lab checked the listed point exactly."},
        ],
        "mistakes": [
            ("Believing an epidemic ends because everyone has been infected",
             "If it did, `S` would reach `0`. For `β = 1/2`, `γ = 1/4` the quantity "
             "`S + I − (1/2)·ln S` is constant, and letting `S` tend to `0` would send it to infinity. "
             "The infected peak at `S = 1/2` and fall afterwards while half the "
             "population is still susceptible: the epidemic ends because too few "
             "susceptibles remain for each infected person to replace themselves."),
            ("Reading R₀ greater than 1 as a statement about the whole outbreak",
             "`R₀ = β·S₀/γ` compares the rates at the start. It says whether `I` grows "
             "at first, not how large the peak is or how many are finally infected. "
             "With `S₀ = 99/100` instead of `9/10`, `R₀` is larger and the peak is still "
             "at `S = 1/2`: the peak's location depends on `γ/β` alone."),
            ("Expecting a single equilibrium",
             "Each point `(S, 0)` is an equilibrium, because both rates contain `I`. "
             "A reader who expects isolated points looks for one root of a "
             "quadratic. The Jacobian's determinant is zero at every such point and the "
             "classification of the linearisation is silent, which is why the "
             "peak and the endpoint are found from the equations instead."),
        ],
        "standard": (
            "Finish when you can set up an SIR model, compute its threshold and peak exactly, and explain how the epidemic ends.",
            "You should be able to read β and γ off the equations, compute R₀ for a "
            "start, place the infected peak at S = γ/β, explain why the equilibria "
            "form a line, and give the conserved-quantity reason that susceptibles "
            "are left at the end."),
        "note": 'That completes the phase plane: classification for linear systems, linearisation at equilibria, and three models read with both. The next course, Laplace Transforms, turns the same equations into algebra.',
    },
]
