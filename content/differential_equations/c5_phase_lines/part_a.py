"""Equilibria, Stability and Phase Lines -- the first half.

Autonomous equations and the phase line, then the classification of an
equilibrium: by the sign of f on either side, and by the sign of f-prime at the
equilibrium itself.

Every figure a tile prints below was read off the built page with
`node scripts/labcheck.js --observe`, never predicted, and is pinned in the
preset's `expect`. The arithmetic written out in the prose and in the worked
examples is done by hand on exact fractions and is checkable on the page.
"""


def _p(pid, label, f, starts, h, n, window, expect):
    return {"id": pid, "label": label, "f": f, "starts": starts, "h": h, "n": n,
            "window": window, "expect": expect}


CUBIC = "y^3 - 4y^2 + 3y"

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "autonomous-equations",
        "title": "Autonomous Equations",
        "module": "Autonomous equations",
        "one_line": "When the right side has no t, the slope depends on y alone, and the constant solutions are the exact roots of f.",
        "summary": (
            "An equation is autonomous when its right-hand side mentions only the unknown, "
            "`y′ = f(y)`, and never the time. That one restriction makes the slope field "
            "identical on every vertical line, lets a solution be slid sideways into another "
            "solution, and turns the question &ldquo;where does the equation have a constant "
            "solution?&rdquo; into &ldquo;where is `f(y)` zero?&rdquo;. Those roots are the "
            "equilibria, and the lab finds them exactly."
        ),
        "key": [
            "y′ = f(y)        no t on the right",
            "f(y*) = 0  ⟹  y = y* is a solution",
            "slope at (t, y) is f(y), whatever t is",
            "slide a solution sideways: still one",
            "y′ = y² − 1:  equilibria  −1  and  1",
        ],
        "key_label": "What makes an equation autonomous, and what it hands you",
        "concepts_intro": (
            "Three ideas, in the order they depend on each other. The first is a definition "
            "and the other two follow from it by arithmetic."
        ),
        "concepts": [
            ("Autonomous means the right side has no t",
             "`y′ = y² − 1` and `y′ = 3 − y` are autonomous: how fast `y` changes depends on "
             "where `y` is and on nothing else. `y′ = t·y` and `y′ = y + t` are not, because "
             "the clock appears on the right. The word is not decoration. Everything this "
             "course does &mdash; the phase line, the classification of equilibria, the "
             "sketches &mdash; works because the clock is absent."),
            ("An equilibrium is a constant solution, for all t",
             "If `f(c) = 0`, the constant function `y = c` has `y′ = 0` and the right side "
             "`f(c) = 0`, so substituting it leaves a residual of exactly zero at every "
             "`t`. That is the same check as in &ldquo;Checking a Proposed Solution&rdquo;, "
             "and it needs no solving. The equilibria of `y′ = f(y)` are therefore the roots "
             "of `f`, found by algebra alone."),
            ("The slope field is the same on every vertical line",
             "The slope at `(t, y)` is `f(y)`, whatever `t` is. Look up one vertical line of "
             "the field and you have seen them all, and every horizontal line carries one "
             "slope from end to end. A solution slid to the right or the left by any amount "
             "therefore meets the same slopes and is again a solution."),
        ],
        "read_title": "Equations with no clock in them",
        "read_intro": "The definition, the two things it buys, and how the lab finds the equilibria exactly.",
        "body": [
            ("def", ("Autonomous equation and equilibrium",
                     "A first-order equation is <strong>autonomous</strong> when it can be "
                     "written `y′ = f(y)`: the right side is a function of `y` alone.",
                     "An <strong>equilibrium</strong> is a number `y*` with `f(y*) = 0`. "
                     "The constant function `y = y*` is then a solution on every `t`.")),
            ("p", "Whether an equation is autonomous is read off its right-hand side, and the "
                  "test is only whether `t` appears. Equations from earlier courses sort "
                  "cleanly. Exponential growth, `y′ = k·y`, is autonomous. So is logistic "
                  "growth in Separable Equations, Growth and Decay, and so is Newton's law of "
                  "cooling, `y′ = −k·(y − A)`, whose only equilibrium is the surrounding "
                  "temperature `A`. The equation `y′ = 2t` of Differential Equations and Euler's Method "
                  "is not."),
            ("h3", "Why the slope field repeats"),
            ("p", "In &ldquo;Slope Fields&rdquo; a field was drawn by evaluating `f(t, y)` at "
                  "grid points. When `f` is a function of `y` alone, the value at `(1, y)` is "
                  "the value at `(5, y)`: the column of slopes above `t = 1` is the column "
                  "above `t = 5`, and all that varies is the height. The lab therefore draws "
                  "one line, the `y` axis, and puts on it everything the field knows."),
            ("thm", ("Sliding a solution sideways",
                     "If `y(t)` solves `y′ = f(y)` and `c` is any constant, then `y(t − c)` "
                     "solves it too.")),
            ("proof", ["Put `w(t) = y(t − c)`. By the chain rule, `w′(t) = y′(t − c)`, since "
                       "the inner function `t − c` has slope 1.",
                       "And `y′(t − c) = f(y(t − c)) = f(w(t))`, because `y` satisfies the "
                       "equation at every argument, `t − c` included. So `w′ = f(w)`. The step "
                       "that fails for `y′ = t·y` is the last one: the right side would "
                       "become `(t − c)·y(t − c)`, which is not `t·w(t)`."]),
            ("h3", "Finding the equilibria"),
            ("p", "Write the right side as a polynomial in `y`, factor it if it factors, and "
                  "read off the roots. The lab does this exactly, with the rational roots "
                  "first and then the roots of what is left when that is a quadratic."),
            ("math", [
                "f(y) = y³ − 4y² + 3y",
                "     = y·(y² − 4y + 3)",
                "     = y·(y − 1)·(y − 3)",
                "",
                "equilibria:  y = 0,  y = 1,  y = 3",
            ]),
            ("p", "Not every equilibrium is a fraction. For `y′ = y² − y − 1` the lab prints "
                  "`(1 ± √5)/2`, which is exact, and in its status line the same two numbers "
                  "rounded, `≈ 1.61803` and `≈ −0.618034`. The square root is carried as a "
                  "surd for the same reason the rest of this Subject carries fractions: a "
                  "decimal equilibrium would make the check &ldquo;is `f` zero there?&rdquo; "
                  "impossible to state exactly."),
            ("h3", "An equilibrium is not a pause"),
            ("p", "A solution that is at an equilibrium at one instant is there at every "
                  "instant, before and after. Through each point there is exactly one "
                  "solution, which &ldquo;Blow-Up and the Interval of Existence&rdquo; states "
                  "in words and this course uses without proof. The constant function is "
                  "already a solution through the point `(t, y*)`, so it is the solution "
                  "through that point, and no other curve can pass through it."),
            ("example", ("An equilibrium you can find with no lab at all",
                         "Cooling is `y′ = −(1/2)·(y − 20)`, with the room at `20`. The right "
                         "side is zero exactly when `y − 20` is zero, so `y = 20` is the only "
                         "equilibrium.",
                         "Substitute: the left side of the constant `y = 20` is `0`, and the "
                         "right side is `−(1/2)·(20 − 20) = 0`. A cup that is already at room "
                         "temperature stays at room temperature at every later time, and at "
                         "every earlier one.")),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "line",
            "preset": "quad",
            "presets": [
                _p("quad", "f(y) = y² − 1", "y^2 - 1", [0], "1/4", 8, [4, -3, 3],
                   {"auEquil": "−1, 1"}),
                _p("cubic", "f(y) = y(y − 1)(y − 3), typed expanded", CUBIC, [2], "1/4", 8,
                   [4, -1, 4], {"auEquil": "0, 1, 3"}),
                _p("golden", "f(y) = y² − y − 1", "y^2 - y - 1", [0], "1/4", 8, [4, -2, 3],
                   {"auEquil": "(1 ± √5)/2"}),
            ],
            "panel_title": "Type f and read the equilibria",
            "panel_intro": "The box holds the right-hand side as a polynomial in `y`. The first "
                           "tile lists its roots exactly: fractions when it has them, a surd "
                           "when it does not, with the rounded values in the status line below. "
                           "The picture shows the same equation as arrows; the next lesson "
                           "reads them.",
        }),
        "steps_title": "Finding the equilibria of an equation",
        "steps_intro": "Four moves. The first decides whether the method applies at all.",
        "steps": [
            ("Look for the clock",
             "If `t` appears on the right side, the equation is not autonomous and nothing in "
             "this course applies to it directly. If only `y` appears, name the right side "
             "`f(y)` and carry on."),
            ("Collect `f(y)` into a polynomial and factor it",
             "Expand brackets and move everything to one side so that `f(y)` stands alone. "
             "Pull out common factors first, and keep them: a factor of `y` is a root."),
            ("Solve `f(y) = 0` exactly",
             "Rational roots as fractions, and a leftover quadratic by the quadratic formula, "
             "kept as a surd such as `(1 ± √5)/2`. Round only to report a size, and say that "
             "you rounded."),
            ("Substitute each root back as a constant",
             "For `y = c`, the left side `y′` is `0` and the right side is `f(c)`. They agree "
             "exactly when `c` is a root, which is the check and also the reason the roots "
             "are the answer."),
        ],
        "worked": {
            "title": "y′ = y² − 1: factor, solve, substitute, and read one column of slopes",
            "intro": [
                "The right side has no `t`, so the equation is autonomous, with "
                "`f(y) = y² − 1`. Factor, set to zero, then test the constants.",
            ],
            "lines": [
                "f(y) = y² − 1 = (y − 1)·(y + 1)",
                "f(y) = 0   at   y = 1   and   y = −1",
                "",
                "y = 1:    y′ = 0     and   1² − 1 = 0     residual 0",
                "y = −1:   y′ = 0     and   (−1)² − 1 = 0  residual 0",
                "",
                "slope at height y, at every t:",
                "   f(−2) = 3    f(0) = −1    f(2) = 3",
            ],
            "after": [
                "So `y = 1` and `y = −1` are solutions for all time. Every other solution "
                "has a slope that is positive above `1`, negative between `−1` and `1`, and "
                "positive below `−1` &mdash; and by uniqueness none of them ever touches "
                "either constant. Which way each one moves is the subject of the next lesson.",
                "For a rehearsal, take `y′ = y³ − y` and find its three equilibria by "
                "factoring `y·(y − 1)·(y + 1)`, then say what the slope is at `y = 2`, for "
                "`t = 0` and for `t = 100`.",
            ],
        },
        "quiz_title": "Autonomous equations and their equilibria",
        "quiz": [
            {"q": "Which of these equations is autonomous?",
             "a": ["`y′ = t − y`", "`y′ = y·(2 − y)`", "`y′ = t·(2 − y)`", "`y′ = y + t²`"],
             "c": 1,
             "why": "`y′ = y·(2 − y)` has only `y` on the right. Each of the others has a `t` "
                    "there, so its slope at a given height changes as time passes and the "
                    "slope field is not the same on every vertical line."},
            {"q": "What are all the equilibria of `y′ = y³ − y`?",
             "a": ["`0` only", "`−1` and `1` only", "`−1`, `0` and `1`", "`0` and `1` only"],
             "c": 2,
             "why": "`y³ − y = y·(y − 1)·(y + 1)`, which is zero at `−1`, `0` and `1`. "
                    "Dividing both sides by `y` to simplify, as in the first choice or the "
                    "second, throws one root away; the second choice drops `0` that way, and "
                    "the last drops `−1`."},
            {"q": "A solution of `y′ = y² − 1` has `y(2) = 1`. What is `y(0)`?",
             "a": ["`0`", "`−1`", "It cannot be found without solving the equation", "`1`"],
             "c": 3,
             "why": "`y = 1` is an equilibrium, so the constant `1` is a solution through "
                    "`(2, 1)`, and only one solution passes through any point. The solution "
                    "is `1` at every `t`, earlier ones included, and nothing had to be "
                    "solved."},
            {"q": "For `y′ = y² − 1`, how do the slopes at `(0, 3)` and `(5, 3)` compare?",
             "a": ["Equal, both `8`", "`8` and `13`", "`8` and `40`", "`0` and `8`"],
             "c": 0,
             "why": "The slope is `f(3) = 9 − 1 = 8` at both points, since `t` does not "
                    "appear. A slope that grew with `t` would need `t` in the equation."},
        ],
        "mistakes": [
            ("Thinking an equilibrium is where the solution stops changing for a while",
             "A solution that sits at an equilibrium is there for every `t`, before and "
             "after, because the constant is itself the solution through that point and "
             "solutions through one point are unique. If `y(3) = 1` in `y′ = y² − 1`, then "
             "`y(0) = 1` as well. A curve that slows down and moves off again is not at "
             "an equilibrium; it is passing near one."),
            ("Cancelling a common factor and losing an equilibrium",
             "For `y′ = y² − y`, dividing both sides by `y` gives `y′/y = y − 1`, which "
             "looks as if it has the one root `y = 1`. The factored form `y·(y − 1)` shows "
             "two, `0` and `1`, and the constant `y = 0` is a solution that the division "
             "never saw. Factor and set to zero; never cancel a factor that can be zero."),
            ("Rounding an irrational equilibrium and treating the decimal as the equilibrium",
             "For `y² − y − 1` the equilibria are `(1 ± √5)/2`. The decimal `1.618` is "
             "close, and `f(1.618)` is not zero, so the constant `y = 1.618` has a nonzero "
             "residual and is not a solution. Keep the surd for any claim of equality and "
             "write `≈` whenever a size is reported."),
        ],
        "standard": ("Finish when you can look at a first-order equation and say whether it is autonomous, and list its equilibria exactly.",
                     "You should be able to test an equation for a `t` on the right side, "
                     "factor `f(y)`, give every root as a fraction or a surd, verify each by "
                     "substitution as a constant, and explain why one vertical line of the "
                     "slope field is all the field there is."),
        "note": "The equilibria cut the `y` axis into intervals, and on each interval "
                "the equation has a definite direction. Drawing those directions is the whole "
                "of &ldquo;The Phase Line&rdquo;.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-phase-line",
        "title": "The Phase Line",
        "module": "Autonomous equations",
        "one_line": "Mark the equilibria on the y axis, test the sign of f once in each gap, and every solution's direction is drawn.",
        "summary": (
            "Between two consecutive equilibria the function `f` cannot change sign, so a "
            "single test value decides the direction of every solution that lives in that "
            "gap. Draw the equilibria on a number line, put an arrow in each gap, and the "
            "result is the phase line: the whole qualitative story of `y′ = f(y)` without "
            "solving it. The arrows carry direction only, never speed."
        ),
        "key": [
            "f > 0 on a gap  ⟹  y rises there",
            "f < 0 on a gap  ⟹  y falls there",
            "one test value per gap decides the sign",
            "arrow = direction;  |f(y)| = speed",
            "f = y³ − 4y² + 3y:  ↓ 0 ↑ 1 ↓ 3 ↑",
        ],
        "key_label": "How to draw the phase line, and what it does not say",
        "concepts_intro": (
            "Three ideas. The first is why one test value is enough; the second turns a sign "
            "into an arrow; the third says what the arrow leaves out."
        ),
        "concepts": [
            ("Between two equilibria f has one sign",
             "A polynomial changes sign only by passing through zero, and the equilibria are "
             "its zeros. On a gap between two of them, `f` is therefore positive throughout "
             "or negative throughout, and the value at a single point in the gap says which. "
             "The same holds on the two unbounded stretches at the ends, which are tested at "
             "one point beyond the outermost equilibria."),
            ("The sign of f is the direction of y",
             "Where `f(y) > 0`, the slope `y′ = f(y)` is positive and a solution there is "
             "increasing, so its arrow points towards larger `y`. Where `f(y) < 0` it points "
             "towards smaller `y`. A solution cannot leave its gap, since leaving would mean "
             "passing through an equilibrium."),
            ("An arrow gives direction, not speed",
             "The speed at height `y` is `|f(y)|`, and it changes continuously from point to "
             "point; the arrow records only the sign. Two arrows of equal size can stand for "
             "a crawl and a rush, and a long arrow on a drawing means nothing at all."),
        ],
        "read_title": "Reading the direction of every solution from one line",
        "read_intro": "The construction, done on the cubic, and then the two places a reader goes wrong with it.",
        "body": [
            ("def", ("Phase line",
                     "The <strong>phase line</strong> of `y′ = f(y)` is the `y` axis with each "
                     "equilibrium marked and an arrow drawn in every interval between and "
                     "beyond them, pointing towards larger `y` where `f > 0` and towards "
                     "smaller `y` where `f < 0`.")),
            ("p", "Take `f(y) = y³ − 4y² + 3y = y·(y − 1)·(y − 3)`, whose equilibria "
                  "`0`, `1` and `3` cut the axis into four pieces. Pick one convenient number "
                  "in each piece and evaluate. The lab uses an integer beyond each end "
                  "and the midpoint of every gap, and evaluates exactly."),
            ("math", [
                "y       −1     1/2     2     4",
                "f(y)    −8     5/8    −2    12",
                "sign     −      +      −     +",
                "arrow    ↓      ↑      ↓     ↑",
            ]),
            ("p", "Read upwards along the axis. Below `0` the arrow points down, so a solution "
                  "there falls away from `0`. On `(0, 1)` it points up, towards `1`. On "
                  "`(1, 3)` it points down, again towards `1`. Above `3` it points up and "
                  "nothing stops it. Without finding a single formula the picture says that "
                  "`y = 1` draws in solutions from both sides and that `0` and `3` push them "
                  "away."),
            ("h3", "The arrow is a sign, and only a sign"),
            ("p", "At `y = 1/2` the speed is `|f(1/2)| = 5/8`; at `y = 2` it is "
                  "`|f(2)| = 2`. A solution passing through `2` is falling `16/5` times as "
                  "fast as one passing through `1/2` is rising, and the two gaps carry arrows "
                  "of the same size. The reasons to draw a phase line are the direction and "
                  "the order of the equilibria. Speed has to be computed from `f`."),
            ("p", "One consequence is worth keeping. Close to an equilibrium `f` is close to "
                  "zero, so the speed there is small. A solution approaching `1` therefore "
                  "slows as it closes in, and the phase line's arrows, which look as if they "
                  "run all the way to `1`, are describing a limit that is never reached in "
                  "finite time."),
            ("h3", "One equilibrium, one gap on each side"),
            ("p", "With a single equilibrium there are only two arrows. For `y′ = 2 − y` the "
                  "equilibrium is `2`, the test values are `1` and `3`, and `f(1) = 1 > 0`, "
                  "`f(3) = −1 < 0`. Both arrows point at `2`."),
            ("example", ("Two arrows that cannot both be right",
                         "A drawing of the cubic's phase line has an arrow pointing up on "
                         "`(0, 1)` and another pointing up on `(1, 3)`.",
                         "The second is wrong, and the test value shows it: `f(2) = −2 < 0`. "
                         "The check is also internal. A solution rising on `(1, 3)` would "
                         "have to pass through `3`, which is an equilibrium and so cannot "
                         "be crossed.")),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "line",
            "preset": "cubic",
            "presets": [
                _p("cubic", "f(y) = y(y − 1)(y − 3), typed expanded", CUBIC, [2], "1/4", 8,
                   [4, -1, 4], {"auEquil": "0, 1, 3", "auTypes": "0 unstable; 1 stable; 3 unstable"}),
                _p("quad", "f(y) = y² − 1", "y^2 - 1", [0], "1/4", 8, [4, -3, 3],
                   {"auEquil": "−1, 1", "auTypes": "−1 stable; 1 unstable"}),
                _p("single", "f(y) = 2 − y", "2 - y", [0], "1/4", 8, [4, -1, 4],
                   {"auEquil": "2", "auTypes": "2 stable"}),
            ],
            "panel_title": "Read the arrows from the sign of f",
            "panel_intro": "The line shows each equilibrium as a dot and each gap as an "
                           "arrow. The status line lists the exact test points and the sign "
                           "of `f` at each. The second tile names what kind of equilibrium "
                           "each dot is; the next lesson explains that column, and for now it "
                           "can be checked against the arrows on either side.",
        }),
        "steps_title": "Drawing a phase line from f",
        "steps_intro": "Five moves, in this order. The sign table is the one that the arrows are copied from.",
        "steps": [
            ("Find and order the equilibria",
             "Solve `f(y) = 0` exactly and list the roots from smallest to largest. They are "
             "the dots on the line."),
            ("Choose one test value in every gap",
             "One below the smallest root, one between each consecutive pair, one above the "
             "largest. Any number inside the gap serves; pick the easiest to compute."),
            ("Evaluate `f` at each test value and keep only the sign",
             "Use exact fractions and evaluate the factored form if there is one. Only the "
             "sign matters; a value that rounds to zero is not zero."),
            ("Turn each sign into an arrow",
             "Positive: towards larger `y`. Negative: towards smaller `y`. Draw it in the "
             "gap, not at the test value."),
            ("Check that no arrow runs across an equilibrium",
             "Two neighbouring arrows may point at the same dot, away from it, or the same "
             "way past it. None may point through a dot into the next gap on its own."),
        ],
        "worked": {
            "title": "The phase line of y′ = y(y − 1)(y − 3) from four test values",
            "intro": [
                "The equilibria are `0`, `1` and `3`. Evaluate `f(y) = y³ − 4y² + 3y` at "
                "`−1`, `1/2`, `2` and `4`, one in each of the four pieces.",
            ],
            "lines": [
                "f(−1)  = −1 − 4 − 3  = −8       negative",
                "f(1/2) = 1/8 − 1 + 3/2 = 5/8    positive",
                "f(2)   = 8 − 16 + 6  = −2       negative",
                "f(4)   = 64 − 64 + 12 = 12      positive",
                "",
                "signs   −   +   −   +",
                "arrows  ↓   ↑   ↓   ↑",
            ],
            "after": [
                "Reading it back: a solution starting below `0` falls without limit; one "
                "starting in `(0, 1)` rises to `1`; one starting in `(1, 3)` falls to `1`; "
                "one starting above `3` rises without limit. The lab agrees on the middle two: "
                "from `y(0) = 2` the cubic preset reports the limit `→ 1`.",
                "For a rehearsal, draw the line for `y′ = (y + 1)·(y − 2)`. The test values "
                "`−2`, `0` and `3` give `4`, `−2` and `4`, so the arrows are up, down, up.",
            ],
        },
        "quiz_title": "Signs and arrows",
        "quiz": [
            {"q": "For `f(y) = (y + 1)·(y − 2)`, which arrows does the phase line show, from the bottom of the axis to the top?",
             "a": ["down, up, down", "up, up, up", "up, down, up", "up, down, down"],
             "c": 2,
             "why": "`f(−2) = 4`, `f(0) = −2` and `f(3) = 4` give the signs `+, −, +`, so up, "
                    "down, up. Down, up, down is the pattern of `(1 + y)·(2 − y)`, whose "
                    "leading coefficient is negative; the other two cannot occur, because the "
                    "sign changes at each simple root."},
            {"q": "For `y′ = y·(y − 1)·(y − 3)` a solution starts at `y(0) = 2`. Where does it go?",
             "a": ["Up to `3`", "Down towards `1`", "Up without limit", "It stays at `2`"],
             "c": 1,
             "why": "`f(2) = −2 < 0`, so the solution is falling, and it cannot pass through "
                    "the equilibrium `1`, so it approaches `1` from above. Staying at `2` "
                    "would need `f(2) = 0`."},
            {"q": "On the phase line of `y′ = y·(y − 1)·(y − 3)`, why is evaluating `f(2)` enough to know the direction on all of `(1, 3)`?",
             "a": ["Because `f` is evaluated at the midpoint, and the midpoint is typical",
                   "Because `f(1)` and `f(3)` are both zero, so `f(2)` is their average",
                   "Because `f′(2)` is zero",
                   "Because `f` cannot change sign inside a gap that contains no root"],
             "c": 3,
             "why": "A polynomial can only change sign at a root, and `1` and `3` are "
                    "consecutive roots. The midpoint is merely convenient, any point of the "
                    "gap would do, and `f(2) = −2` is not the average of two zeros."},
            {"q": "A phase line has a long arrow on `(0, 1)` and a short arrow on `(1, 3)`. What does this say about how fast solutions move?",
             "a": ["Solutions in `(0, 1)` move faster, in proportion to the lengths",
                   "Nothing: arrows give only the direction, and the speed is `|f(y)|`",
                   "Solutions in `(1, 3)` move faster, since a shorter arrow is more urgent",
                   "Solutions in both gaps move at the same speed"],
             "c": 1,
             "why": "The arrow encodes the sign of `f` and nothing else. Speed is `|f(y)|`, "
                    "which differs from point to point inside one gap, so no single arrow "
                    "length could describe it."},
        ],
        "mistakes": [
            ("Reading arrow length as speed",
             "On the cubic, `|f(1/2)| = 5/8` and `|f(2)| = 2`, so the solution at height "
             "`2` falls `16/5` times as fast as the one at `1/2` rises, and the two arrows "
             "are the same size. Speed is `|f(y)|` and has to be computed. What the arrow "
             "records is only which way, which is also all that is needed to know where "
             "the solution is heading."),
            ("Using the test value in place of the equilibria",
             "The dots are the roots of `f`. Putting the dots at the test values, or "
             "drawing the arrows with no dots, loses the information that decides the "
             "long-run answer: where a solution can and cannot go. List the roots first."),
            ("Testing only one gap and copying the sign to the others",
             "The signs alternate across a simple root, but not across a repeated one. "
             "The cubic's pattern `−, +, −, +` is not a rule; for `y′ = y²·(1 − y)` the "
             "signs are `+, +, −` (the next lesson). Evaluate once in every gap."),
        ],
        "standard": ("Finish when you can draw the phase line of a polynomial f from its roots and four or fewer test values, and read where a start goes.",
                     "You should be able to list the equilibria in order, evaluate `f` "
                     "exactly in every gap, turn each sign into an arrow, say which way a "
                     "solution starting anywhere moves, and explain why the arrow's length "
                     "means nothing."),
        "note": "Some dots on the line have arrows pointing into them from both sides, some "
                "have arrows pointing away, and some have one of each. Those three cases are "
                "named and sorted in &ldquo;Stable, Unstable and Semistable&rdquo;.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "stable-unstable-and-semistable",
        "title": "Stable, Unstable and Semistable",
        "module": "Classifying equilibria",
        "one_line": "An equilibrium attracts from both sides, repels from both, or attracts from one side only, and the signs of f on either side say which.",
        "summary": (
            "Look at the two arrows touching an equilibrium. If both point towards it, it is "
            "stable; if both point away, it is unstable; if one points towards and one away, "
            "it is semistable. The three cases are all there is, they are decided by the "
            "sign of `f` on each side, and semistable is a distinct case with a distinct "
            "reason &mdash; a root of `f` where `f` touches zero and turns back."
        ),
        "key": [
            "f: + then −  across y*  ⟹  stable",
            "f: − then +  across y*  ⟹  unstable",
            "same sign on both sides  ⟹  semistable",
            "y′ = y²·(1 − y):  0 semistable, 1 stable",
            "never decide by f at y* itself: f = 0",
        ],
        "key_label": "Three kinds of equilibrium, from the signs on either side",
        "concepts_intro": (
            "Three ideas. A definition by arrows, a rule that turns signs into a verdict, "
            "and the case people try to explain away."
        ),
        "concepts": [
            ("Stable, unstable and semistable are defined by the two arrows",
             "At an equilibrium `y*`, look at the arrow just below and the arrow just "
             "above. Both towards `y*`: stable, since a solution that starts near enough "
             "ends up there. Both away: unstable. One towards and one away: "
             "semistable. Nothing else can happen, as each neighbouring arrow has only two "
             "directions."),
            ("The signs of f on the two sides are the whole test",
             "Positive then negative as `y` increases through `y*` gives arrows up and then "
             "down, both towards `y*`: stable. Negative then positive: unstable. The same "
             "sign on both sides: semistable. The value of `f` at `y*` is zero and says "
             "nothing, so the signs are read next to the equilibrium, never at it."),
            ("Semistable is a case, not a hedge",
             "A double root of `f` is a place where the graph of `f` touches the axis "
             "and turns back without crossing. Neither side's sign changes, so the arrows "
             "agree in direction, and that is not a mixture of the other two cases but the "
             "single situation in which a solution below is drawn in and one above is "
             "carried off."),
        ],
        "read_title": "Three kinds of equilibrium, and the one that looks like a mistake",
        "read_intro": "The definitions, the sign rule checked on three equations, and why the semistable case matters later.",
        "body": [
            ("def", ("Stable, unstable, semistable",
                     "An equilibrium `y*` of `y′ = f(y)` is <strong>stable</strong> if the "
                     "arrows on both sides point towards it, <strong>unstable</strong> if "
                     "both point away, and <strong>semistable</strong> if one points "
                     "towards it and the other away.")),
            ("p", "The classification therefore needs only the phase line from the previous "
                  "lesson. For each dot, compare the sign of `f` just below with the sign "
                  "just above. The lab prints the verdicts for every equilibrium in "
                  "increasing order, and prints the same sign data its status line used."),
            ("math", [
                "f(y) = y³ − 4y² + 3y      signs  −  +  −  +",
                "",
                "y = 0:   − then +    arrows ↓ ↑   away on both sides   unstable",
                "y = 1:   + then −    arrows ↑ ↓   towards from both    stable",
                "y = 3:   − then +    arrows ↓ ↑   away on both sides   unstable",
            ]),
            ("p", "An unstable equilibrium is one that a real system would not stay at. The "
                  "constant solution is exactly right and a solution starting a hair "
                  "away leaves. A stable one is where solutions from a whole interval end up, "
                  "which is why it is the equilibrium that a measurement is likely to find."),
            ("h3", "A root where f touches zero"),
            ("p", "Take `f(y) = y²·(1 − y)`. The factor `y²` is positive on both sides of "
                  "`0`, and the factor `1 − y` is positive there, so `f` is positive on "
                  "both sides of `0`. Below `0` the arrow points up, towards `0`. Just above "
                  "it the arrow points up, away from `0`. The equilibrium at `1` is the "
                  "ordinary kind: `f` goes from positive to negative, and it is stable."),
            ("math", [
                "f(y) = y²·(1 − y)      test values  −1,  1/2,  2",
                "",
                "f(−1)  = 1·2 = 2         positive",
                "f(1/2) = (1/4)·(1/2) = 1/8   positive",
                "f(2)   = 4·(−1) = −4       negative",
                "",
                "y = 0:  + then +   semistable",
                "y = 1:  + then −   stable",
            ]),
            ("p", "The lab prints `f′(0) = 0` and `f′(1) = −1` for this equation, in the "
                  "slope tile. The zero at `y = 0` tempts a reader into using it as the "
                  "verdict, and the next lesson shows that it is not one: the flat slope "
                  "occurs at stable and unstable equilibria as well. The signs of `f` "
                  "decide, and they are always available."),
            ("p", "One of these was met before the word was defined. In &ldquo;Harvesting and "
                  "the Threshold&rdquo; the harvest `H = 1` left the single equilibrium `2`, "
                  "with the right side `−(y − 2)²/4`, which is negative on both sides of "
                  "`2`. A population above `2` falls to it and one below falls away from "
                  "it, and that lesson called the equilibrium semistable without yet having "
                  "the test. The same sign on both sides, negative this time, gives the "
                  "same verdict: the arrows agree in direction, down and down."),
            ("thm", ("Even and odd roots",
                     "For a polynomial `f`, an equilibrium that is a root of even multiplicity "
                     "is semistable, and one of odd multiplicity is stable or unstable "
                     "according to whether `f` passes from positive to negative or from "
                     "negative to positive.")),
            ("p", "This is stated, not proved here; it is the factor-by-factor sign argument "
                  "that the cubic and the semistable example used above. A factor "
                  "`(y − y*)` with an even power does not change sign at `y*`, and with an "
                  "odd power it does. The multiplicity is a shortcut for the sign test. The "
                  "sign test needs no theorem and is the one to trust."),
            ("h3", "The solutions near a semistable point"),
            ("p", "Start the equation `y′ = y²·(1 − y)` at `y(0) = −1`. It rises, because "
                  "`f(−1) = 2 > 0`, and it approaches `0` from below without reaching it. "
                  "Start it at `y(0) = 1/2` and it rises to `1`, leaving `0` behind for ever. "
                  "Only the first of these is drawn in by `0`, and only from below. That "
                  "asymmetry is the whole content of the word."),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "line",
            "preset": "cubic",
            "presets": [
                _p("cubic", "f(y) = y(y − 1)(y − 3), typed expanded", CUBIC, [2], "1/4", 8,
                   [4, -1, 4], {"auTypes": "0 unstable; 1 stable; 3 unstable",
                                "auSlope": "f′(0) = 3; f′(1) = −2; f′(3) = 6"}),
                _p("semi", "f(y) = y²(1 − y), typed as y² − y³", "y^2 - y^3", ["1/2"], "1/4", 8,
                   [4, -1, 2], {"auTypes": "0 semistable; 1 stable",
                                "auSlope": "f′(0) = 0; f′(1) = −1"}),
                _p("quad", "f(y) = y² − 1", "y^2 - 1", [0], "1/4", 8, [4, -3, 3],
                   {"auTypes": "−1 stable; 1 unstable", "auSlope": "f′(−1) = −2; f′(1) = 2"}),
            ],
            "panel_title": "Classify each equilibrium, then check against its arrows",
            "panel_intro": "The type tile names each equilibrium from the sign of `f` on "
                           "its two sides, and the slope tile prints `f′` at each, which the "
                           "next lesson uses. Choose the semistable preset and look at the "
                           "two arrows touching the dot at `0`: they point the same way.",
        }),
        "steps_title": "Classifying an equilibrium from the signs",
        "steps_intro": "Four moves, done for one equilibrium at a time.",
        "steps": [
            ("Find the sign of `f` just below the equilibrium",
             "Use the gap's test value, or the sign of the factored form. Write it down as "
             "a plus or a minus sign."),
            ("Find the sign of `f` just above it",
             "The same, in the next gap up. Do not skip this because the first sign "
             "looked decisive: a single side cannot separate stable from semistable."),
            ("Compare the pair",
             "`+` then `−`: stable. `−` then `+`: unstable. Equal signs: semistable. That is "
             "the whole table."),
            ("Confirm with a start on each side",
             "Pick a start in each neighbouring gap and follow the arrow. They should "
             "approach or leave the dot in the way the verdict says."),
        ],
        "worked": {
            "title": "y′ = y²·(1 − y): one equilibrium of each kind",
            "intro": [
                "The equilibria are `0` and `1`. Evaluate `f(y) = y²·(1 − y)` at the three "
                "test values the lab uses, `−1`, `1/2` and `2`.",
            ],
            "lines": [
                "f(−1)  = (−1)²·(1 − (−1)) = 1·2 = 2",
                "f(1/2) = (1/2)²·(1 − 1/2) = 1/8",
                "f(2)   = 2²·(1 − 2) = −4",
                "",
                "signs   +   +   −",
                "",
                "y = 0:   + then +   up, up      semistable",
                "y = 1:   + then −   up, down    stable",
            ],
            "after": [
                "Solutions below `0` rise to `0`; solutions just above `0` rise away from it "
                "and head for `1`. The slope tile prints `f′(0) = 0` here, and the sign test, "
                "not the derivative, is what gave the verdict. The lab prints "
                "`0 semistable; 1 stable` for this preset.",
                "For a rehearsal, factor `y²·(y − 2)` (arrows down, down, up) and say what "
                "kind of equilibrium sits at `0` and at `2`.",
            ],
        },
        "quiz_title": "Telling the three kinds apart",
        "quiz": [
            {"q": "Along an axis with an equilibrium `y*`, `f` is positive just below `y*` and positive just above. What is `y*`?",
             "a": ["Stable", "Unstable", "Semistable", "Not an equilibrium, since `f` has the same sign on both sides"],
             "c": 2,
             "why": "Both arrows point up. The one below points towards `y*` and the one "
                    "above points away, so `y*` attracts from below and repels from above: "
                    "semistable. It is still an equilibrium, because `f(y*) = 0` is all that "
                    "defines one."},
            {"q": "For `y′ = (y − 4)·(y + 2)`, what kind of equilibrium is `y = 4`?",
             "a": ["Unstable", "Stable", "Semistable", "It has no type, since `f(4) = 0`"],
             "c": 0,
             "why": "`f(3) = −5` and `f(5) = 7`: negative then positive, arrows down and up, "
                    "away from `4` on both sides. Stable would need positive then negative. "
                    "The value of `f` at `4` is zero for every equilibrium and decides "
                    "nothing."},
            {"q": "Which `f` has a semistable equilibrium at `y = 2`?",
             "a": ["`f(y) = y − 2`", "`f(y) = (y − 2)³`", "`f(y) = 2 − y`", "`f(y) = (y − 2)²`"],
             "c": 3,
             "why": "`(y − 2)²` is positive on both sides of `2`. `y − 2` and `(y − 2)³` go "
                    "from negative to positive, which is unstable, and `2 − y` goes from "
                    "positive to negative, which is stable. An odd power changes sign, so it "
                    "is the even power that gives a semistable point."},
            {"q": "For `y′ = y²·(1 − y)`, a solution starts at `y(0) = −1`. What is its long-run behaviour?",
             "a": ["It approaches `0` from below and stays below it", "It reaches `1`",
                   "It falls without limit", "It crosses `0` and then approaches `1`"],
             "c": 0,
             "why": "`f(−1) = 2 > 0`, so it rises, but `0` is an equilibrium and a solution "
                    "cannot cross one. It creeps up towards `0` from below, slowing as `f` "
                    "shrinks. The solution that goes on to `1` is the one that starts in "
                    "`(0, 1)`."},
        ],
        "mistakes": [
            ("Treating semistable as a hedge between stable and unstable",
             "It is a third, exactly-defined case. At the semistable root `0` of "
             "`y²·(1 − y)` a solution starting below rises to it and one starting just "
             "above rises away from it, so it is not &ldquo;a bit stable&rdquo;: it is "
             "stable from one side and unstable from the other, and a definite sign "
             "pattern, the same sign on both sides, produces it every time."),
            ("Classifying from one side only",
             "From below, the arrow at `0` for `y²·(1 − y)` points towards `0`, which on its "
             "own looks stable. Only the arrow above, pointing away, shows that it is not. "
             "Always read both sides before giving a verdict."),
            ("Saying a solution reaches a stable equilibrium",
             "A solution near a stable equilibrium approaches it and, because it cannot "
             "cross it and its speed `|f(y)|` goes to zero, does not arrive in finite time. "
             "&ldquo;The limit is `1`&rdquo; is the correct statement, and the lab's limit "
             "tile reads `→ 1` for that reason, not `= 1`."),
        ],
        "standard": ("Finish when you can classify every equilibrium of a polynomial equation as stable, unstable or semistable, from the signs alone.",
                     "You should be able to read the sign of `f` on either side of each "
                     "root, say which of three cases results, write down an `f` with a "
                     "semistable root, and predict from the arrows where a start just below "
                     "and just above it will go."),
        "note": "The signs always work. A number sometimes works too: the slope of "
                "`f` at the equilibrium, whose sign usually decides and sometimes "
                "does not, and which also says how quickly a solution closes in. That is "
                "&ldquo;Linearisation and the Sign of f&prime;&rdquo;.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "linearisation-and-the-sign-of-f-prime",
        "title": "Linearisation and the Sign of f′",
        "module": "Classifying equilibria",
        "one_line": "Near an equilibrium the gap obeys u′ ≈ f′(y*)·u, so the sign of f′(y*) decides the type unless it is zero.",
        "summary": (
            "Shift the equilibrium to zero with `u = y − y*` and the equation becomes "
            "`u′ = f′(y*)·u` plus terms in `u²` and higher, which are negligible for small "
            "`u`. A negative slope then means the gap closes, a positive one means it opens, "
            "and the size of the slope says at what exponential rate. A zero slope settles "
            "nothing, and the equations `y′ = y³`, `y′ = −y³` and the semistable one of "
            "the last lesson show all three outcomes."
        ),
        "key": [
            "u = y − y*  ⟹  u′ ≈ f′(y*)·u",
            "f′(y*) < 0  ⟹  stable   (u shrinks)",
            "f′(y*) > 0  ⟹  unstable (u grows)",
            "f′(y*) = 0  ⟹  undecided: use the signs",
            "y³, −y³, y²:  f′(0) = 0, three verdicts",
        ],
        "key_label": "What the slope of f at an equilibrium decides, and what it does not",
        "concepts_intro": (
            "Three ideas. A change of variable that puts the equilibrium at zero, the rule "
            "it produces, and the case where the rule says nothing."
        ),
        "concepts": [
            ("Shift the equilibrium to zero and expand",
             "Write `u = y − y*`, so that `u′ = y′ = f(y* + u)`. For a polynomial, expanding "
             "gives `f(y* + u) = f(y*) + f′(y*)·u + (terms with u² and higher)`, which is "
             "the same expansion in `h` that produced the derivative in Rates of Change and "
             "the Derivative. At an equilibrium `f(y*) = 0`, so "
             "`u′ = f′(y*)·u + (terms with u² and higher)`."),
            ("A nonzero slope settles the type, and sets the rate",
             "For small `u` the higher terms are far smaller than the first. If "
             "`f′(y*) < 0` then `u′` has the opposite sign to `u` and the gap closes, like "
             "`e^(f′(y*)·t)`; if `f′(y*) > 0` the gap opens. The number is a rate, not only "
             "a sign: slope `−2` closes the gap like `e^(−2t)`, a factor of about "
             "`0.135335` per unit of time."),
            ("A zero slope settles nothing",
             "If `f′(y*) = 0` the first term is absent and what is left is `u²` or "
             "`u³` or higher, whose sign depends on the equation. The slope of "
             "`f` at the equilibrium is not the slope of any solution, and it being flat "
             "does not mean the equilibrium is flat in any sense a classification can use. "
             "The sign test of the last lesson still works and is the method to fall back "
             "on."),
        ],
        "read_title": "Using the slope of f, and knowing when it will not do",
        "read_intro": "The expansion done exactly on one equation, the rule and its rate, and the three equations where the rule is silent.",
        "body": [
            ("p", "The sign test needs the whole phase line. The slope test needs only the "
                  "equilibrium. Of the two methods this Subject uses for stability it is the "
                  "one that carries over to systems, in &ldquo;Linearisation and the "
                  "Jacobian&rdquo; in Systems and the Phase Plane, so the reasoning is worth "
                  "seeing exactly once on an equation small enough to do by hand."),
            ("math", [
                "y′ = y² − 1       equilibrium y* = −1       f′(y) = 2y",
                "",
                "u = y + 1,   y = u − 1",
                "y² − 1 = (u − 1)² − 1 = u² − 2u",
                "",
                "u′ = −2u + u²",
            ]),
            ("p", "That is exact, with nothing dropped. The slope is `f′(−1) = −2`, the first "
                  "term, and what remains is `u²`. Take `u = 1/10`: the full right side is "
                  "`−2/10 + 1/100 = −19/100`, against `−20/100` for the first term alone. "
                  "The neglected piece is a twentieth of the first term, and it shrinks "
                  "faster than `u` does, so it matters less and less as the solution closes "
                  "in."),
            ("thm", ("The slope test",
                     "Let `y*` be an equilibrium of `y′ = f(y)`. If `f′(y*) < 0` it is stable, "
                     "and if `f′(y*) > 0` it is unstable. If `f′(y*) = 0` the test says nothing.")),
            ("p", "The lab demonstrates this on every equation it is given: it prints "
                  "`f′` at each equilibrium, exactly, beside the type found from the signs, "
                  "and they agree whenever the slope is not zero. It does not prove the "
                  "statement for every `f`. The claim has the same standing as the limit "
                  "of the quotients in the first course: shown to hold, and used."),
            ("h3", "The rate"),
            ("p", "If `u′ = −2u` exactly then `u = u₀·e^(−2t)`, and the gap at "
                  "`t = 1` is `e^(−2)`, about `0.135335` (rounded), of the gap at `t = 0`. "
                  "That is the sense in which a stable equilibrium of slope `−2` is "
                  "&ldquo;twice as strongly stable&rdquo; as one of slope `−1`: the same "
                  "gap closes like `e^(−t)` instead, a factor of about `0.367879` per unit "
                  "of time. At an unstable equilibrium of slope `2` the gap grows by "
                  "`e² ≈ 7.38906` per unit instead. Exactness belongs to the equation "
                  "above; the exponential is what it approaches for small `u`."),
            ("h3", "When the slope is zero"),
            ("p", "The cubic of the last lesson has slopes `3`, `−2` and `6` at its "
                  "three equilibria, because `f′(y) = 3y² − 8y + 3`. The lab prints "
                  "`f′(0) = 3; f′(1) = −2; f′(3) = 6`, and the verdicts it prints beside "
                  "them, unstable, stable, unstable, are those of the sign test."),
            ("p", "Three equations have slope zero at `y = 0` and no two of them behave "
                  "alike. For `y′ = y³` we have `u′ = u³`, which has the sign of `u`: the "
                  "gap opens, so `0` is unstable. For `y′ = −y³` it has the opposite sign: "
                  "the gap closes, stable. For the semistable equation of the last "
                  "lesson, `y′ = y²·(1 − y)`, near zero we have `u′ ≈ u²`, which is "
                  "positive on both sides: semistable. The slope is the same, `0`, in all "
                  "three, and the verdicts are three different ones."),
            ("example", ("A flat slope and a verdict that survives it",
                         "The lab prints `f′(0) = 0` for `y′ = −y³`. Do not read the zero as "
                         "&ldquo;no decision possible&rdquo;; read it as &ldquo;this test "
                         "has nothing to say&rdquo;.",
                         "The signs do. `f(−1) = 1 > 0` and `f(1) = −1 < 0`: positive then "
                         "negative, both arrows towards `0`, stable. Solutions do approach "
                         "`0`, though more slowly than any exponential `e^(−c·t)` would "
                         "carry them.")),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "line",
            "preset": "cubic",
            "presets": [
                _p("cubic", "f(y) = y(y − 1)(y − 3), typed expanded", CUBIC, [2], "1/4", 8,
                   [4, -1, 4], {"auSlope": "f′(0) = 3; f′(1) = −2; f′(3) = 6",
                                "auTypes": "0 unstable; 1 stable; 3 unstable"}),
                _p("flat-unstable", "f(y) = y³", "y^3", ["1/2"], "1/4", 8, [4, -2, 2],
                   {"auSlope": "f′(0) = 0", "auTypes": "0 unstable"}),
                _p("flat-stable", "f(y) = −y³", "-y^3", ["1/2"], "1/4", 8, [4, -2, 2],
                   {"auSlope": "f′(0) = 0", "auTypes": "0 stable"}),
            ],
            "panel_title": "Compare the slope tile with the type tile",
            "panel_intro": "The slope tile prints `f′` at every equilibrium, exactly. Where it "
                           "is nonzero, its sign matches the type beside it. Choose the two "
                           "flat presets: the slope tile reads the same on both, and the type "
                           "tile does not.",
        }),
        "steps_title": "Classifying an equilibrium with f′",
        "steps_intro": "Four moves. The last one is the one a reader forgets to make.",
        "steps": [
            ("Differentiate `f`",
             "Use the power rule on the polynomial, term by term. Keep the result as a "
             "polynomial in `y`."),
            ("Evaluate `f′` at the equilibrium, exactly",
             "Substitute the root: a fraction, or a surd for an irrational root. Do not "
             "evaluate at a rounded decimal, which is not the equilibrium."),
            ("Read the sign",
             "Negative: stable, and the gap closes like `e^(f′(y*)·t)`. Positive: unstable. "
             "Zero: stop and use the signs of `f` on either side."),
            ("Compare with the signs when you can",
             "On a polynomial the phase line costs one test value per gap. A slope verdict "
             "and a sign verdict that disagree mean an arithmetic slip."),
        ],
        "worked": {
            "title": "y′ = y² − 1 at y = −1: the gap closes like e^(−2t)",
            "intro": [
                "Here `f(y) = y² − 1`, so `f′(y) = 2y`. The two equilibria are `±1`. Shift "
                "each to zero and expand.",
            ],
            "lines": [
                "f′(−1) = −2    stable      f′(1) = 2     unstable",
                "",
                "u = y + 1:   u′ = −2u + u²      slope −2",
                "u = y − 1:   u′ =  2u + u²      slope  2",
                "",
                "u = 1/10 at y* = −1:",
                "   full    −2/10 + 1/100 = −19/100",
                "   linear  −2/10         = −20/100",
            ],
            "after": [
                "Near `y = −1` the gap behaves like `u₀·e^(−2t)`, which is "
                "`e^(−2) ≈ 0.135335` of itself after one unit of time (rounded). Near "
                "`y = 1` it grows instead. The sign test gives the same verdicts: "
                "`y²−1` goes from positive to negative across `−1` and from negative to "
                "positive across `1`.",
                "For a rehearsal, take `y′ = y·(4 − y)`. Its slope is `4 − 2y`, which is "
                "`4` at `0` and `−4` at `4`: unstable at `0`, stable at `4`.",
            ],
        },
        "quiz_title": "What the slope of f decides",
        "quiz": [
            {"q": "For `y′ = y·(4 − y)`, what is `f′(4)`, and what kind of equilibrium is `y = 4`?",
             "a": ["`4`, unstable", "`0`, semistable", "`−4`, stable", "`−4`, unstable"],
             "c": 2,
             "why": "`f(y) = 4y − y²`, so `f′(y) = 4 − 2y` and `f′(4) = −4`. Negative means "
                    "stable. `4` is `f′(0)`, which belongs to the unstable equilibrium at "
                    "`0`, and a slope of zero would not be semistable by itself in any "
                    "case."},
            {"q": "An equilibrium has `f′(y*) = 0`. What can be concluded about its type?",
             "a": ["It is semistable", "It is stable", "Nothing yet: look at the signs of `f` on both sides",
                   "It is unstable"],
             "c": 2,
             "why": "`y′ = y³` (unstable), `y′ = −y³` (stable) and `y′ = y²` (semistable) all "
                    "have `f′(0) = 0`. Any of the three verdicts can follow, so the slope "
                    "settles nothing and the signs have to be read."},
            {"q": "For `y′ = −y³`, the equilibrium `y = 0` has `f′(0) = 0`. What is the correct description?",
             "a": ["Stable, by the sign test", "Unstable, by the sign test",
                   "Semistable, because the slope is zero", "Not an equilibrium, because the slope is zero"],
             "c": 0,
             "why": "`f` is positive for `y < 0` and negative for `y > 0`: arrows towards `0` "
                    "on both sides. The slope being zero does not make it semistable and "
                    "does not stop it from being an equilibrium, which only needs `f(0) = 0`."},
            {"q": "Near a stable equilibrium with `f′(y*) = −2`, the gap behaves like `e^(−2t)`. By roughly what factor does it shrink in one unit of time?",
             "a": ["About `0.5`", "About `0.135335`", "About `7.38906`", "By exactly `2`"],
             "c": 1,
             "why": "`e^(−2) ≈ 0.135335`, so the gap falls to about a seventh of its size. "
                    "`7.38906` is `e²`, which is how an unstable equilibrium of slope `2` "
                    "would grow the gap. `0.5` would need a rate near `0.693` rather than `2`, and a factor of "
                    "exactly `2` points the wrong way."},
        ],
        "mistakes": [
            ("Reading f′(y*) = 0 as semistable",
             "Three equations with slope zero at `0` give three verdicts: `y′ = y³` is "
             "unstable, `y′ = −y³` is stable, and `y′ = y²` is semistable. The zero only "
             "means the first-order term has vanished and the equation has to be read "
             "at the next order, which for a polynomial is the same thing as the sign of "
             "`f` on both sides."),
            ("Mixing up f′(y*) and y′",
             "At an equilibrium `y′ = f(y*) = 0` always, since the solution is constant. "
             "The number `f′(y*)` is the slope of the graph of `f` at the equilibrium, "
             "and it measures how fast nearby solutions pull in or push out, not how "
             "fast any solution moves."),
            ("Applying the sign of f′ at a point that is not an equilibrium",
             "On the cubic, `f′(1/2) = −1/4` is negative, and `1/2` is not an "
             "equilibrium; a solution there is rising, not being drawn in. The slope "
             "test is for roots of `f` only, and a root has to be found first."),
        ],
        "standard": ("Finish when you can compute f′ exactly at each equilibrium, classify with its sign, and name the case it cannot decide.",
                     "You should be able to differentiate `f`, evaluate at each equilibrium "
                     "as a fraction or a surd, say stable or unstable from the sign, give "
                     "the rate at which the gap closes or opens, and fall back on the signs "
                     "of `f` when the slope is zero."),
        "note": "With the type of every equilibrium known, a start can be followed to its "
                "limit, which is the question of the next lesson, and the equation can be "
                "given a parameter and the equilibria watched as it moves.",
    },
]
