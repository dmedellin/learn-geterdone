"""Equilibria, Stability and Phase Lines -- the second half.

Long-run behaviour read from the phase line, then a parameter: the equilibria
of a family, the diagram that stacks their phase lines, and the sketches the
phase line allows.

Every figure a tile prints below was read off the built page with
`node scripts/labcheck.js --observe`, never predicted, and is pinned in the
preset's `expect`. The arithmetic written out in the prose and in the worked
examples is done by hand on exact fractions and is checkable on the page.
"""


def _p(pid, label, f, starts, h, n, window, expect):
    return {"id": pid, "label": label, "f": f, "starts": starts, "h": h, "n": n,
            "window": window, "expect": expect}


def _b(pid, label, f, a, rng, expect):
    return {"id": pid, "label": label, "f": f, "a": a, "range": rng, "expect": expect}


CUBIC = "y^3 - 4y^2 + 3y"

LESSONS = [
    # ---------------------------------------------------------------- 05
    {
        "slug": "long-run-behaviour-without-solving",
        "title": "Long-Run Behaviour Without Solving",
        "module": "Classifying equilibria",
        "one_line": "A solution cannot leave its gap and moves one way inside it, so its limit is the equilibrium its arrow points to, or infinity.",
        "summary": (
            "A solution of `y′ = f(y)` cannot cross an equilibrium, because the equilibrium "
            "is itself a solution, and inside a gap `f` has one sign, so it moves in one "
            "direction only. A solution that moves one way inside a gap has to settle at the "
            "equilibrium at the end its arrow points to, or grow without bound if that end "
            "has no equilibrium. The limit from any start can be stated from the phase "
            "line, and the exact Euler steps are a check on that claim and not a proof of it."
        ),
        "key": [
            "a solution never crosses an equilibrium",
            "inside a gap f has one sign: y is monotone",
            "limit = the equilibrium its arrow points to",
            "arrow to an open end:  y → +∞  or  −∞",
            "a start at y* stays at y* for every t",
        ],
        "key_label": "How to read a limit off the phase line",
        "concepts_intro": (
            "Three ideas, each resting on the one before. The first keeps a solution in its "
            "gap, the second gives it a direction, and the third says where that direction "
            "ends."
        ),
        "concepts": [
            ("A solution stays in the gap it starts in",
             "Every equilibrium is a constant solution, and through each point there passes "
             "only one solution. A solution that began between two equilibria would have to "
             "touch one of them to leave, which would put two solutions through the same "
             "point. So it never does: its height stays strictly between the two, for as "
             "long as it exists."),
            ("Inside a gap it moves one way",
             "Between consecutive equilibria `f` has one sign, so `y′ = f(y)` has one sign "
             "along the whole solution. The solution is always rising or always falling, "
             "and it never turns round. The arrow the phase line draws in that gap is the "
             "direction for every solution that lives there."),
            ("A solution that moves one way ends at a limit the line names",
             "A solution that keeps rising inside a gap either runs into its upper "
             "equilibrium, never reaching it, or has no upper equilibrium and rises past "
             "every height. The first is a limit that is a number, the second is `+∞`. "
             "A limit short of the equilibrium is not possible, since there the slope would "
             "still be bounded away from zero and the solution would carry on."),
        ],
        "read_title": "Where a solution goes, from the signs alone",
        "read_intro": "The statement, one equation read from every start, and two places where the exact steps and the line can seem to disagree.",
        "body": [
            ("p", "A limit is a statement about what a solution does as `t` grows. Write "
                  "`y → 1` when `y(t)` gets and stays as close to `1` as you like, and "
                  "`y → +∞` when it rises past every height. Neither says the solution ever "
                  "arrives. The phase line of the last two lessons gives both, for every "
                  "start at once."),
            ("thm", ("The limit of a solution",
                     "Let `y` solve `y′ = f(y)` with `f` a polynomial. If `y(0)` lies in a gap "
                     "between two equilibria, or beyond the outermost one, then `y` stays in "
                     "that gap and is monotone, and as `t` grows, for as long as the solution "
                     "exists, it approaches the equilibrium at the end its arrow points to, or "
                     "goes to `+∞` or `−∞` if that end has no equilibrium. If `y(0)` is an "
                     "equilibrium, `y` stays there.")),
            ("p", "The lab demonstrates this on every equation it is given, by printing the "
                  "limit the phase line predicts beside exact Euler steps that move the same "
                  "way. It does not prove it for every polynomial. The argument has the "
                  "three concepts above as its pieces; the one that is stated and not "
                  "proved is the last, that a solution which rises inside a gap cannot "
                  "stop short of the equilibrium above it."),
            ("h3", "One equation, three starts"),
            ("p", "Take `y′ = (y − 1)·(y − 3)`, which the lab's box holds expanded as "
                  "`y² − 4y + 3`. Its equilibria are `1` and `3`. The slopes are `f′(y) = 2y − 4`, so "
                  "`f′(1) = −2` and `f′(3) = 2`: `1` is stable and `3` is unstable, by the "
                  "slope test of the last lesson. The signs of `f` at the test values `0`, "
                  "`2` and `4` are `+`, `−` and `+`, giving arrows up, down, up."),
            ("math", [
                "start    gap          arrow   limit",
                "0        below 1      up      → 1",
                "2        (1, 3)       down    → 1",
                "4        above 3      up      → +∞",
            ]),
            ("p", "Starts `0` and `2` are on opposite sides of `1` and end at the same "
                  "place, because `1` is stable and both arrows point at it. The start at "
                  "`4` is above the unstable equilibrium, nothing lies above it, and the "
                  "solution rises without limit. The exact Euler steps from `4` with "
                  "`h = 1/4` are `4 + (1/4)·3 = 19/4`, then `409/64`, and the lab's table "
                  "climbs from there. For this quadratic the climb is faster than any "
                  "exponential and ends at a finite time, as &ldquo;Blow-Up and the Interval "
                  "of Existence&rdquo; found for `y′ = y²`; `y → +∞` is the correct statement of "
                  "where it is going."),
            ("h3", "A column of steps is evidence, not proof"),
            ("p", "Exact Euler steps are exact arithmetic applied to an approximate method, "
                  "and the phase line is what says why they move as they do. With `h = 1/4` "
                  "the steps from `2` run `2, 7/4, 97/64, …`, falling and staying above `1`, "
                  "as the arrow says. A step that is too large can disagree. On the same "
                  "equation from `5/2` with `h = 1` the steps are `5/2`, `7/4`, `13/16` and "
                  "`313/256`: the third is below `1` and the fourth is above it again, "
                  "so the column rocks about the equilibrium. No solution does that. The "
                  "polygon stepped over `1`, which a solution cannot do, and the error is "
                  "the step size and not the equation. One limit of the lab belongs here too: a "
                  "quadratic right-hand side doubles the digits of every fraction at each "
                  "step, so the lab stops after `11` exact steps and says so, and a cubic "
                  "stops after `7`, where it could only go on by rounding."),
            ("example", ("A start exactly on the unstable equilibrium",
                         "For `y′ = (y − 1)·(y − 3)` start at `y(0) = 3`. The lab's limit tile "
                         "reads `at equilibrium`, and every exact Euler step is `3`, since "
                         "`f(3) = 0` adds nothing.",
                         "A start at `3` and a start just below it are not close in "
                         "the long run. The first stays at `3` for ever; the second is in the "
                         "gap `(1, 3)`, where the arrow points down, and goes to `1`. A start "
                         "just above `3` goes to `+∞`. Unstable means that nearby starts leave, "
                         "and it does not mean that they all leave the same way.")),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "steps",
            "preset": "two",
            "presets": [
                _p("two", "f(y) = (y − 1)(y − 3), typed expanded", "y^2 - 4y + 3", [0, 2, 4], "1/4", 12,
                   [3, -1, 6], {"auLimit": "→ 1", "auSteps": "11 exact steps, then digit budget"}),
                _p("climb", "The same f, starting from the top", "y^2 - 4y + 3", [4, 2, 0], "1/4", 12,
                   [3, -1, 6], {"auLimit": "→ +∞"}),
                _p("cubic", "f(y) = y(y − 1)(y − 3), typed expanded", CUBIC, ["1/2", 2, "7/2"], "1/4", 12,
                   [3, -1, 6], {"auLimit": "→ 1", "auSteps": "7 exact steps, then digit budget"}),
                _p("quad", "f(y) = y² − 1", "y^2 - 1", [-2, 0, 2], "1/4", 12, [3, -3, 4], {"auLimit": "→ −1"}),
            ],
            "panel_title": "Read the limit, then watch the steps agree",
            "panel_intro": "The limit tile names where the first start goes, from the phase "
                           "line, and the step tile says how many exact steps were taken. "
                           "The table lists every start. The picture draws the exact polygons "
                           "against the equilibria as horizontal lines. Reorder the starts "
                           "in the box to put a different one first.",
        }),
        "steps_title": "Finding the limit of a start from the phase line",
        "steps_intro": "Five moves. The first four need no arithmetic beyond one sign per gap.",
        "steps": [
            ("Find the equilibria and put them in order",
             "Solve `f(y) = 0` exactly and list the roots from smallest to largest. They are "
             "the only heights a solution can approach."),
            ("Place the start",
             "Say which gap `y(0)` is in, or that it is an equilibrium. A start that is "
             "exactly an equilibrium stays there and has no more to say."),
            ("Read the arrow in that gap",
             "Take the sign of `f` at a test value in the gap, as in the phase line. Up "
             "means larger `y`, down means smaller."),
            ("Name the limit",
             "Follow the arrow to the end of the gap. If there is an equilibrium there, "
             "that is the limit, written `→ y*`. If the gap runs on without end, the "
             "limit is `→ +∞` or `→ −∞`."),
            ("Check against the exact steps",
             "Take a few exact Euler steps with a small `h`. They should move the way "
             "the arrow says and stay inside the gap. A column that disagrees points to a "
             "step too large or a slip in a sign, and the phase line is what to trust."),
        ],
        "worked": {
            "title": "y′ = (y − 1)(y − 3) from 0, 2 and 4",
            "intro": [
                "The equilibria are `1` and `3`, and `f′(y) = 2y − 4` gives slopes `−2` and "
                "`2`. Evaluate `f` at the three starts, which are also test values, and "
                "read each limit.",
            ],
            "lines": [
                "f′(1) = −2 stable       f′(3) = 2 unstable",
                "",
                "f(0) = 3    f(2) = −1    f(4) = 3",
                "",
                "y(0) = 0:  gap below 1,  up    → 1",
                "y(0) = 2:  gap (1, 3),   down  → 1",
                "y(0) = 4:  gap above 3,  up    → +∞",
                "",
                "Euler, h = 1/4, from 4:  4, 19/4, 409/64, …",
            ],
            "after": [
                "Two of the three starts end at the same equilibrium and the third does not "
                "end anywhere. The lab agrees: the first start `0` reads `→ 1`, and "
                "choosing the climb preset puts `4` first so that the tile reads `→ +∞`. "
                "The first Euler step is `4 + (1/4)·3 = 19/4` and the second is "
                "`19/4 + (1/4)·(105/16) = 409/64`, the numbers the table prints.",
                "For a rehearsal, take `y′ = y·(4 − y)` and starts `−1`, `2` and `5`. The "
                "values `f(−1) = −5`, `f(2) = 4` and `f(5) = −5` give `→ −∞`, `→ 4` and `→ 4`.",
            ],
        },
        "quiz_title": "Where a solution goes",
        "quiz": [
            {"q": "For `y′ = (y − 1)·(y − 3)`, a solution has `y(0) = 5/2`. What does it do as `t` grows?",
             "a": ["It approaches `3`", "It rocks about `2`", "It approaches `1`", "It falls through `1` and on without limit"],
             "c": 2,
             "why": "`f(5/2) = −3/4 < 0`, so it falls, and it stays inside `(1, 3)`. It "
                    "approaches `1`. It cannot approach `3`, which would need it to rise, and "
                    "it cannot rock or pass through `1`, an equilibrium and so a solution "
                    "that no other solution crosses."},
            {"q": "For `y′ = y·(4 − y)`, which start has the limit `−∞`?",
             "a": ["`y(0) = −1`", "`y(0) = 0`", "`y(0) = 2`", "`y(0) = 5`"],
             "c": 0,
             "why": "`f(−1) = −5 < 0` and nothing lies below `0`, so it falls without "
                    "limit. A start at `0` is an equilibrium and stays there, `y(0) = 2` "
                    "rises to `4`, and `y(0) = 5` falls to `4`, since `f(5) = −5`."},
            {"q": "For `y′ = (y − 1)·(y − 3)` and `y(0) = 1`, which is correct?",
             "a": ["The solution rises to `3`", "The solution falls to `−∞`", "The solution moves to the nearest unstable equilibrium", "The solution is `1` at every `t`"],
             "c": 3,
             "why": "`1` is an equilibrium, so the constant `y = 1` is the solution through "
                    "`(0, 1)`. Stable or not, a start on an equilibrium stays on it. The "
                    "other choices move it, and a solution through an equilibrium cannot "
                    "move."},
            {"q": "The exact Euler steps from `5/2` with `h = 1` on `y′ = (y − 1)·(y − 3)` are `5/2, 7/4, 13/16, 313/256`. What does this show?",
             "a": ["The solution crosses `1` and then crosses back", "The step is too large: the polygon stepped over an equilibrium that no solution crosses",
                   "The equation has an equilibrium at `13/16`", "The limit of the solution is `−∞`"],
             "c": 1,
             "why": "The third value is below `1` and the fourth above it, but the solution "
                    "stays above `1` and falls to it. The disagreement comes from stepping "
                    "`h = 1` where `h = 1/4` does not cross. `13/16` is not a root of "
                    "`f`, and nothing about the equation sends the limit to `−∞`."},
        ],
        "mistakes": [
            ("Thinking a solution between two equilibria may oscillate between them",
             "The equilibria are solutions, and a solution cannot cross another, so a "
             "solution between them stays between them. Inside the gap `f` has one "
             "sign, so it only rises or only falls. A column of Euler steps that rocks, "
             "like `5/2, 7/4, 13/16, 313/256` for `h = 1`, is the polygon overshooting "
             "an equilibrium, and a smaller step does not do it."),
            ("Saying an unstable equilibrium sends everything to infinity",
             "Unstable means that starts near it leave it, not that they all go to "
             "`±∞`. For `y′ = (y − 1)·(y − 3)`, a start just below `3` goes down to the "
             "stable equilibrium at `1`, and only a start above `3` goes to `+∞`. The limit "
             "has to be read from the arrow in the start's own gap."),
            ("Reading a limit from a column of steps alone",
             "Twelve steps that climb are twelve numbers. They are evidence that the "
             "arrow points up, and the arrow, which comes from the sign of `f`, is the "
             "reason. From `2` the steps `2, 7/4, 97/64, …` stay above `1`, as they "
             "must, and no finite column reaches `1`: the limit statement is about what "
             "happens as `t` grows, which no table holds."),
        ],
        "standard": ("Finish when you can state the limit of a solution from any starting value using only the phase line, and say when it is infinite.",
                     "You should be able to find and order the equilibria, place a start in "
                     "its gap, read the arrow, give the limit as an equilibrium or as "
                     "`+∞` or `−∞`, say what happens to a start exactly on an equilibrium, "
                     "and explain a rocking column of Euler steps as a step that was too "
                     "large."),
        "note": "So far the equation has been fixed. Put a number `a` in it and the "
                "equilibria move, and the long-run behaviour with them. That is the subject of "
                "&ldquo;One-Parameter Families&rdquo;.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "one-parameter-families",
        "title": "One-Parameter Families",
        "module": "Parameters",
        "one_line": "Put a number a in the equation and the equilibria move; where two of them meet, the behaviour changes all at once.",
        "summary": (
            "An equation `y′ = f(y, a)` with a parameter `a` is a different autonomous "
            "equation for every value of `a`, and its equilibria are the roots of "
            "`f(y, a)` in `y`, which move as `a` does. Two of them meet where `f` and its slope in "
            "`y` are zero together, and at that value of `a` the count of equilibria "
            "changes. The lab finds the value exactly, and shows that a small change in "
            "`a` can change the long-run behaviour completely."
        ),
        "key": [
            "y′ = f(y, a):  a different line for each a",
            "equilibria = roots of f in y; they move",
            "two meet where f = 0 and f′ = 0 together",
            "y′ = a + y²:  two,  one,  none",
            "a small change in a can change everything",
        ],
        "key_label": "How a parameter moves the equilibria, and where they meet",
        "concepts_intro": (
            "Three ideas. A parameter makes a family of phase lines, the equilibria in it "
            "are roots that move, and two roots meeting is a test with two equations."
        ),
        "concepts": [
            ("A parameter makes a family of equations",
             "In `y′ = a + y²` the letter `a` is fixed for the whole solution and chosen "
             "before it begins. Each value of `a` gives an ordinary autonomous equation "
             "with its own equilibria and its own phase line. The lab holds `a` in a box, "
             "and everything else on the page is the phase line of that one equation."),
            ("The equilibria are roots that move",
             "The equilibria of `y′ = a + y²` are the roots of `y² + a`, which are `±√(−a)` "
             "when `a` is negative. As `a` climbs from `−4` towards `0` they close from "
             "`±2` towards `0`. The phase line keeps its shape while the number of roots "
             "stays the same, and can change it only at a value of `a` where that number "
             "changes."),
            ("Two equilibria meet where f and its slope are zero",
             "Two roots coming together form a double root: `f(y, a) = (y − r)²·g(y)` near "
             "it, which is zero at `r` and has slope zero there too. So the value of `a` "
             "at which two equilibria meet is found by solving `f = 0` and `f′ = 0` together, "
             "with `f′` the slope in `y` and `a` held fixed."),
        ],
        "read_title": "Following the equilibria as a changes",
        "read_intro": "One family read at four values of the parameter, the test that finds the value where it changes, and why that change is not small.",
        "body": [
            ("def", ("Critical value of a",
                     "For a family `y′ = f(y, a)`, a <strong>critical value</strong> of the "
                     "parameter is a value of `a` at which two equilibria meet, so that the "
                     "number of equilibria is different on the two sides of it.")),
            ("p", "The family is `y′ = a + y²`. At each value of `a` the right side is a "
                  "quadratic in `y` that is zero where `y² = −a`, and the slope in `y` is "
                  "`f′(y) = 2y`. Read it at four values."),
            ("math", [
                "a       equilibria    types",
                "−4      −2, 2         −2 stable;  2 unstable",
                "−1      −1, 1         −1 stable;  1 unstable",
                "0       0             semistable",
                "1       none          —",
            ]),
            ("p", "At `a = −4` the slopes are `f′(−2) = −4` and `f′(2) = 4`, so `−2` is stable "
                  "and `2` is unstable, by the slope test. The pair closes up as `a` rises: "
                  "`±2`, then `±1`, then one equilibrium at `0`, then none. For `a = 1`, "
                  "`1 + y²` is positive for every `y`, so every solution rises."),
            ("h3", "The value where they meet"),
            ("p", "Solve both equations. The slope `f′(y) = 2y` is zero only at `y = 0`. The "
                  "right side at `y = 0` is `a`, and that is zero only at `a = 0`. So "
                  "`a = 0` is the one critical value of this family, and the lab's "
                  "critical-value tile reads `a = 0`."),
            ("p", "At `a = 0` the equation is `y′ = y²`, which is positive on both sides of "
                  "`0`: the equilibrium is the semistable one of &ldquo;Stable, Unstable and "
                  "Semistable&rdquo;, the last equilibrium before the pair disappears. It is "
                  "one double root, and the lab counts it once."),
            ("example", ("Finding a critical value of a different family",
                         "Take `y′ = y² − 2y + a`. The slope in `y` is `2y − 2`, zero at "
                         "`y = 1`. There `f(1, a) = 1 − 2 + a = a − 1`, which is zero when "
                         "`a = 1`.",
                         "Check on both sides. At `a = 0` the right side is `y·(y − 2)`, with "
                         "equilibria `0` and `2`. At `a = 1` it is `(y − 1)²`, one equilibrium. "
                         "At `a = 2` it is `(y − 1)² + 1`, which is never zero. Type the right "
                         "side into the box and move `a` to see the same three counts.")),
            ("p", "This test was run once before, without its name. In &ldquo;Harvesting and "
                  "the Threshold&rdquo; the family was `y′ = y·(1 − y/4) − H`, with the "
                  "harvest `H` as the parameter: the equilibria `1` and `3` at `H = 3/4` "
                  "moved together and met at `2` when `H = 1`, and at any larger harvest "
                  "there were none. The two equations find that value. The slope in `y` is "
                  "`1 − y/2`, zero at `y = 2`, and `f(2, H) = 1 − H`, zero at `H = 1`, which "
                  "is the threshold `r·K/4` that lesson read off the peak of the growth. "
                  "Type the harvested right side into the box, with `a` in place of `H`: "
                  "at `a = 3/4` the tiles print `1, 3` and `1 unstable; 3 stable`, at "
                  "`a = 1` they print `2 semistable`, and the critical value reads `a = 1`."),
            ("h3", "Small changes in a are not small changes in the answer"),
            ("p", "Take `y′ = a + y²` with `y(0) = 0`. At `a = −1/100` the equilibria are "
                  "`±1/10`, because `(1/10)² = 1/100`. The start `0` lies between them, "
                  "where `f(0) = −1/100 < 0`, so the solution falls to `−1/10` and stops "
                  "there for good."),
            ("p", "At `a = 1/100` there are no equilibria. Now `y′ = 1/100 + y²` is at least "
                  "`1/100` for every `y`, so the solution rises for ever and, because the right "
                  "side grows with `y²`, without bound. Two values of `a` that are `1/50` apart "
                  "give a solution that settles and a solution that does not. And between "
                  "`a = −1/100` and `a = 0` each equilibrium moved by `1/10` while `a` moved "
                  "by `1/100`, ten times as far as the parameter did: near a critical value "
                  "a square root is steep."),
        ],
        "lab": ("dekit", {
            "mode": "bifurcate",
            "preset": "saddle-node",
            "presets": [
                _b("saddle-node", "y′ = a + y², with a = −4", "a + y^2", "-4", [-4, 1], {"bfEquil": "−2, 2", "bfCount": "2 equilibria", "bfCritical": "a = 0"}),
                _b("at-zero", "y′ = a + y², with a = 0", "a + y^2", "0", [-4, 1], {"bfEquil": "0", "bfTypes": "0 semistable", "bfCount": "1 equilibrium"}),
                _b("gone", "y′ = a + y², with a = 1", "a + y^2", "1", [-4, 1], {"bfEquil": "none", "bfCount": "no equilibria"}),
            ],
            "panel_title": "Move a and watch the equilibria meet",
            "panel_intro": "The box holds `f(y, a)` as a polynomial in `y` and `a`, and a second "
                           "box holds the value of `a`. The tiles list the equilibria at that "
                           "`a`, how many there are, and the critical values of `a` in the "
                           "range, found exactly. The picture draws every equilibrium "
                           "against `a`, from floating-point roots, with the chosen `a` "
                           "marked; the next lesson reads it.",
        }),
        "steps_title": "Tracking the equilibria of a family",
        "steps_intro": "Five moves. The third is the one that gives the answer; the others check it.",
        "steps": [
            ("Fix a value of `a` and solve",
             "Substitute the number, then find the roots of `f(y, a)` in `y` exactly, as in the "
             "first lesson of this course. This is an ordinary phase line."),
            ("Repeat at several values of `a`",
             "Pick values spread across the range and record the count and the "
             "types each time. A change in the count is a sign that a critical value lies "
             "between two of your values."),
            ("Solve `f = 0` and `f′ = 0` together",
             "Differentiate in `y` with `a` held fixed. Find the `y` that makes `f′` zero, "
             "put it into `f`, and solve for `a`. For a quadratic this is the same as "
             "setting its discriminant to zero."),
            ("Test one value of `a` on each side",
             "At the critical value itself there is one double root. On the two sides the "
             "counts differ, and a pair that has gone has gone from one side only."),
            ("State the answer for every range of `a`",
             "Say how many equilibria there are for `a` below, at and above each critical "
             "value, and what they are."),
        ],
        "worked": {
            "title": "y′ = a + y²: the equilibria at four values of a",
            "intro": [
                "The right side is `y² + a`, with slope `2y` in `y`. Solve at each `a`, then "
                "solve `f = 0` and `f′ = 0` together to find where the pair meets.",
            ],
            "lines": [
                "a = −4:  y² = 4     y = −2, 2     f′ = −4, 4",
                "a = −1:  y² = 1     y = −1, 1",
                "a = 0:   y² = 0     y = 0         f′(0) = 0",
                "a = 1:   y² = −1    none",
                "",
                "f′ = 2y = 0  at  y = 0",
                "f(0, a) = a = 0  at  a = 0",
            ],
            "after": [
                "The equilibria are `±√(−a)` for negative `a`: `±2` at `a = −4` and `±1` at "
                "`a = −1`. They meet at `0` when `a = 0` and are gone for positive `a`. The "
                "lab's three presets print `−2, 2`, then `0`, then `none`, with the critical "
                "value `a = 0`.",
                "For a rehearsal, find the critical value of `y′ = y² − 4y + a`. The slope "
                "`2y − 4` is zero at `y = 2`, and `f(2, a) = 4 − 8 + a = a − 4`, so `a = 4`.",
            ],
        },
        "quiz_title": "Following the equilibria",
        "quiz": [
            {"q": "How many equilibria does `y′ = a + y²` have when `a = −9`?",
             "a": ["None", "Two, `−3` and `3`", "One", "Two, `−9` and `9`"],
             "c": 1,
             "why": "`y² − 9 = 0` gives `y = ±3`. There are two, and both are exact. "
                    "`±9` solves `y² = 81`, the equation for `a = −81`, and the family has no "
                    "equilibria only for positive `a`."},
            {"q": "For `y′ = y² − 2y + a`, at which value of `a` do the two equilibria meet?",
             "a": ["`a = 0`", "`a = −1`", "`a = 2`", "`a = 1`"],
             "c": 3,
             "why": "The slope `2y − 2` is zero at `y = 1`, and `f(1, a) = a − 1` is zero at "
                    "`a = 1`. At `a = 0` the equilibria are `0` and `2`, which have not met. "
                    "At `a = 2` there are none."},
            {"q": "In `y′ = a + y²`, what kind of equilibrium is `y = 0` at `a = 0`?",
             "a": ["Semistable", "Stable", "Unstable", "There is no equilibrium at `a = 0`"],
             "c": 0,
             "why": "The right side is `y²`, positive on both sides of `0`, so a solution below "
                    "rises to it and one above rises away. That is semistable. It is an "
                    "equilibrium, since `f(0) = 0`, and the single one at that `a`."},
            {"q": "For `y′ = a + y²` with `y(0) = 0`, which value of `a` gives a solution that rises without bound?",
             "a": ["`a = −1/100`", "`a = 0`", "`a = 1/100`", "`a = −4`"],
             "c": 2,
             "why": "At `a = 1/100` there are no equilibria and the slope is at least `1/100`. "
                    "At `a = −1/100` and `a = −4` the start `0` lies between two equilibria "
                    "and falls to the lower one. At `a = 0` the start is on the equilibrium "
                    "and stays there."},
        ],
        "mistakes": [
            ("Assuming a small change in a makes a small change in the behaviour",
             "The family `y′ = a + y²` has equilibria `±1/10` at `a = −1/100` and none at "
             "`a = 1/100`. From `y(0) = 0` the first solution settles at `−1/10` and the second "
             "rises without bound. The equilibria also moved ten times as far as `a` did. "
             "Near a critical value the count changes, and the behaviour with it."),
            ("Finding the critical value from f = 0 alone",
             "One equation in the two unknowns `y` and `a` has a whole curve of solutions: "
             "`f = a + y²` is zero at `(y, a) = (2, −4)`, and `2` is an equilibrium at "
             "`a = −4` that has not met anything, since `f′(2) = 4`. The meeting needs the "
             "second equation, `f′ = 0`, which singles out `y = 0` and so `a = 0`."),
            ("Counting the equilibrium at the critical value as two, or as none",
             "At `a = 0` the two equilibria `±√(−a)` have become the single double root "
             "`0`, and the lab's count tile reads `1 equilibrium`. It is not a pair "
             "lying on top of one another and it is not absent: `y = 0` is a constant "
             "solution, and it is semistable."),
        ],
        "standard": ("Finish when you can list the equilibria of a family at a given value of the parameter, and find the value where two of them meet.",
                     "You should be able to substitute a value of `a` and solve, tabulate the "
                     "equilibria across the range, solve `f = 0` and `f′ = 0` together to "
                     "get the critical value, and say how many equilibria there are on "
                     "each side of it."),
        "note": "The table of equilibria against `a` has a picture, and the picture is the "
                "most compact way to see a whole family at once. Drawing it, and naming the shapes "
                "it takes, is &ldquo;Bifurcation Diagrams&rdquo;.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "bifurcation-diagrams",
        "title": "Bifurcation Diagrams",
        "module": "Parameters",
        "one_line": "Plot every equilibrium against a, solid where stable and dashed where unstable, and the fork and the exchange are read straight off.",
        "summary": (
            "A bifurcation diagram puts the parameter `a` along the horizontal axis and the "
            "equilibria up the vertical one, so that each vertical slice is a phase line. "
            "Stable branches are drawn solid and unstable ones dashed. Three shapes cover the "
            "families here: two branches that meet and vanish, two that cross and swap "
            "stability, and one that forks into three. The critical values and the types are "
            "exact; the curves are drawn from floating-point roots."
        ),
        "key": [
            "across: a;  up: the equilibria y*",
            "solid = stable;  dashed = unstable",
            "a + y²:  two branches meet and vanish",
            "a·y − y²:  branches cross, swap stability",
            "a·y − y³:  one branch forks into three",
        ],
        "key_label": "Reading a bifurcation diagram, and the three shapes it shows",
        "concepts_intro": (
            "Three ideas. A diagram is phase lines side by side, the line style carries the "
            "stability, and the shape at a critical value has a name."
        ),
        "concepts": [
            ("A diagram is a stack of phase lines",
             "Cut the diagram with a vertical line at one value of `a` and the points where it "
             "crosses the branches are the equilibria of that equation. Sweep the line from "
             "left to right and the phase line changes as it goes. The horizontal axis is the "
             "parameter, not time, and no branch is a solution plotted against `t`."),
            ("Solid and dashed are the sign of f′",
             "At a point on a branch, `f′(y*, a)` is the slope that classified the equilibrium "
             "in &ldquo;Linearisation and the Sign of f&prime;&rdquo;. Negative is stable and drawn solid; "
             "positive is unstable and drawn dashed. A branch changes style at a point where "
             "its slope passes through zero, which is where it meets another branch."),
            ("Three shapes carry the whole story here",
             "In a <em>saddle-node</em> two branches of opposite type meet and vanish. In a "
             "<em>transcritical</em> shape two branches cross and exchange stability. In a "
             "<em>pitchfork</em> one branch changes type and two new branches of the other "
             "type spring from it. The shape at a critical value is a fact about the "
             "equation, and each one can be found by solving for the equilibria."),
        ],
        "read_title": "A fork, a crossing, and a count that goes both ways",
        "read_intro": "The pitchfork family worked fully, then the crossing, then the comparison with the last lesson that corrects a common impression.",
        "body": [
            ("p", "Take `y′ = a·y − y³ = y·(a − y²)`. The equilibria are `0` for every `a`, and "
                  "`±√a` when `a` is positive. The slope in `y` is `f′(y) = a − 3y²`, so at the "
                  "equilibria it is `f′(0) = a`, and at the other two "
                  "`f′(±√a) = a − 3a = −2a`."),
            ("math", [
                "a       equilibria    types",
                "−1      0             0 stable",
                "0       0             slope 0: use the signs",
                "4       −2, 0, 2      −2 stable;  0 unstable;  2 stable",
            ]),
            ("p", "For negative `a` the slope `f′(0) = a` is negative and `0` is stable, the "
                  "only equilibrium. For positive `a` it is positive, so `0` is unstable, and "
                  "the pair `±√a` has appeared, each with slope `−2a < 0`, stable. At "
                  "`a = 4` that is `±2` with slope `−8`, and `0` with slope `4`. The diagram "
                  "is a solid line along `a < 0`, then a dashed line along `a > 0` with "
                  "two solid arms leaving it: a fork opening to the right."),
            ("h3", "A crossing instead of a fork"),
            ("p", "For `y′ = a·y − y² = y·(a − y)` the equilibria are `0` and `a`, for every "
                  "`a`. The slope is `a − 2y`, so `f′(0) = a` and `f′(a) = −a`. At `a = 2` that "
                  "is `0` unstable and `2` stable; at `a = −2` it is `0` stable and `−2` "
                  "unstable. The two branches pass through each other at `a = 0` and trade "
                  "stability there."),
            ("p", "The count behaves differently from the last lesson's family. At `a = 2` "
                  "there are two equilibria, at `a = 0` one, at `a = −2` two again. No "
                  "equilibrium vanishes: one passes through the other. This is what separates "
                  "a transcritical shape from a saddle-node."),
            ("h3", "The count can go down, and can go up"),
            ("p", "Compare the three families as `a` rises through `0`. In `a + y²` the count "
                  "falls from two to none. In `a·y − y³` it rises from one to three. In "
                  "`a·y − y²` it is two on both sides. Nothing in the idea of a parameter makes "
                  "the number of equilibria grow or shrink; the shape of `f` does."),
            ("example", ("Reading one slice of the pitchfork",
                         "Put the chosen `a` at `4` and look at the vertical line through it. It "
                         "crosses the diagram at three heights, `−2`, `0` and `2`. The two "
                         "outer crossings are on solid branches and the middle one is on a dashed "
                         "branch.",
                         "The phase line at that slice has arrows up, down, up, down, and the "
                         "tile prints `−2 stable; 0 unstable; 2 stable`. A solution "
                         "starting above `0` goes to `2`, and one below goes to `−2`. At "
                         "`a = −1` the line crosses once, at `0`, and every solution goes there.")),
        ],
        "lab": ("dekit", {
            "mode": "bifurcate",
            "preset": "pitchfork",
            "presets": [
                _b("pitchfork", "y′ = a·y − y³, with a = 4", "a y - y^3", "4", [-2, 4], {"bfEquil": "−2, 0, 2", "bfTypes": "−2 stable; 0 unstable; 2 stable", "bfCritical": "a = 0"}),
                _b("pitchfork-before", "y′ = a·y − y³, with a = −1", "a y - y^3", "-1", [-2, 4], {"bfEquil": "0", "bfTypes": "0 stable"}),
                _b("transcritical", "y′ = a·y − y², with a = 2", "a y - y^2", "2", [-2, 4], {"bfEquil": "0, 2", "bfTypes": "0 unstable; 2 stable", "bfCritical": "a = 0"}),
            ],
            "panel_title": "Read the branches, solid and dashed",
            "panel_intro": "The picture draws each equilibrium against `a`, solid where it is "
                           "stable and dashed where it is unstable, with a vertical line at the "
                           "chosen `a`. The tiles give the same slice exactly: the equilibria, "
                           "their types, the count and the critical value. Change `a` in the "
                           "box and watch the line move across the fork.",
        }),
        "steps_title": "Drawing and reading a bifurcation diagram",
        "steps_intro": "Five moves. The first four produce the diagram, and the last names it.",
        "steps": [
            ("Factor `f(y, a)` to get the equilibria as functions of `a`",
             "For `a·y − y³` the factors are `y` and `a − y²`, so the branches are `y = 0` "
             "and `y = ±√a`, the second pair existing for `a ≥ 0`."),
            ("Find the critical values",
             "Solve `f = 0` and `f′ = 0` together, as in the last lesson. These are the "
             "values of `a` where branches meet and the diagram can change its form."),
            ("Classify one slice on each side of every critical value",
             "Choose a value of `a` between critical values, find the equilibria and read "
             "`f′` at each. Negative is stable and solid, positive is unstable and dashed."),
            ("Join the points into branches",
             "Follow each equilibrium as `a` moves, keeping the style it has. A change of "
             "style on one branch happens at a critical value only."),
            ("Name the shape at each critical value",
             "Two branches meeting and vanishing: saddle-node. Two crossing and swapping "
             "style: transcritical. One splitting into three: pitchfork."),
        ],
        "worked": {
            "title": "y′ = a·y − y³ at a = 4 and at a = −1",
            "intro": [
                "Here `f(y) = y·(a − y²)` and `f′(y) = a − 3y²`. Read the slice at each of the "
                "two presets and then name the shape at `a = 0`.",
            ],
            "lines": [
                "a = 4:   y·(4 − y²) = y·(2 − y)·(2 + y)",
                "         equilibria −2, 0, 2",
                "         f′ = 4 − 3y²:  f′(0) = 4,  f′(±2) = −8",
                "         −2 stable;  0 unstable;  2 stable",
                "",
                "a = −1:  y·(−1 − y²) = −y·(1 + y²)",
                "         equilibrium 0 only,  f′(0) = −1,  stable",
            ],
            "after": [
                "Along the diagram `0` goes from stable at `a = −1` to unstable at `a = 4`, "
                "and the pair `±2` is present at `a = 4` and absent at `a = −1`: the shape "
                "is a fork, opening at the critical value `a = 0`, where "
                "`f′(0) = a` passes through zero. The lab prints `−2, 0, 2` and "
                "`0 stable` for these two presets, with the critical value `a = 0`.",
                "For a rehearsal, take the crossing `y′ = a·y − y²` at `a = −2`. The "
                "equilibria are `0` and `−2` and the slopes `f′(0) = −2` and "
                "`f′(−2) = 2`: `0` stable and `−2` unstable, the reverse of `a = 2`.",
            ],
        },
        "quiz_title": "Reading the diagram",
        "quiz": [
            {"q": "On a bifurcation diagram, what does a dashed branch mean?",
             "a": ["The equilibria along it are stable", "The equilibria along it are semistable", "The curve is only a guide and is not made of equilibria", "The equilibria along it are unstable"],
             "c": 3,
             "why": "Dashed marks a positive slope `f′`, which is unstable. Solid is stable. "
                    "Every point on a dashed branch is still an equilibrium, so the branch "
                    "is made of constant solutions, and a semistable point is one point "
                    "and not a branch."},
            {"q": "For `y′ = a·y − y³` with `a = 9`, which description is correct?",
             "a": ["Three equilibria: `−3` and `3` stable, `0` unstable", "Three equilibria: `0` stable, `−3` and `3` unstable", "One equilibrium, `0`, stable", "Three equilibria, all stable"],
             "c": 0,
             "why": "`f′ = 9 − 3y²` gives `f′(0) = 9`, unstable, and `f′(±3) = 9 − 27 = −18`, "
                    "stable. The second choice has the types reversed, the third is the "
                    "picture for negative `a`, and `0` has a positive slope."},
            {"q": "In `y′ = a·y − y²`, what happens to the equilibrium `y = 0` as `a` rises from `−2` to `2`?",
             "a": ["It stays stable", "It splits into three", "It goes from stable to unstable, trading stability with the equilibrium at `y = a`", "It disappears at `a = 0`"],
             "c": 2,
             "why": "`f′(0) = a`, negative then positive, so `0` is stable and then unstable, "
                    "while `f′(a) = −a` goes the other way. At `a = 0` they coincide at `0`, "
                    "and `0` is an equilibrium for every `a`, so it does not disappear."},
            {"q": "As `a` rises through `0`, which statement is true of the three families of these two lessons?",
             "a": ["All three gain equilibria", "`a + y²` loses two equilibria and `a·y − y³` gains two", "All three lose equilibria", "`a·y − y²` gains one equilibrium"],
             "c": 1,
             "why": "`a + y²` goes from two to none, and `a·y − y³` from one to three. "
                    "`a·y − y²` has two on both sides, so it gains none. The count follows "
                    "the shape of `f`, in both directions."},
        ],
        "mistakes": [
            ("Thinking the number of equilibria can only go up as a parameter increases",
             "In `y′ = a + y²` the lab prints `2 equilibria` at `a = −4` and `no equilibria` "
             "at `a = 1`, so raising `a` removed them. In `y′ = a·y − y³` raising `a` "
             "through `0` adds two. In `y′ = a·y − y²` the count is two on both sides "
             "of `0`. Which happens depends on the equation, not on the direction of "
             "the parameter."),
            ("Reading a branch of the diagram as a solution plotted against time",
             "The horizontal axis is the parameter `a`, which is fixed for each solution. "
             "A branch records where the equilibria of one equation sit for each choice of "
             "`a`, and a solution of any one equation is a single point on the vertical "
             "slice, or a path along it. Nothing in the diagram moves with `t`."),
            ("Treating a dashed branch as not a solution",
             "Every point on a dashed branch is an equilibrium and so a constant "
             "solution; at `a = 4` the constant `y = 0` solves `y′ = 4y − y³` exactly. "
             "Dashed means unstable: a solution that starts exactly there stays, and "
             "one that starts anywhere nearby leaves."),
        ],
        "standard": ("Finish when you can read stable and unstable branches off a bifurcation diagram and name the fork and the crossing.",
                     "You should be able to take a vertical slice and list the equilibria with "
                     "their types, tell solid from dashed by the sign of `f′`, find the "
                     "critical value, and name a saddle-node, transcritical or pitchfork shape "
                     "from how the branches meet."),
        "note": "With the phase line, the types, the limits and the way they depend on a "
                "parameter in hand, the last thing the phase line can give is a picture "
                "of the solutions themselves. That is &ldquo;Sketching Solutions from the "
                "Phase Line&rdquo;.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "sketching-solutions-from-the-phase-line",
        "title": "Sketching Solutions from the Phase Line",
        "module": "Sketching",
        "one_line": "Horizontal at the equilibria, monotone between them, and bending only where f′(y) is zero: a solution can be drawn without a formula.",
        "summary": (
            "In the `t`–`y` plane the equilibria are horizontal lines that no solution "
            "crosses, and between them each solution rises or falls as the phase line says. "
            "Differentiating `y′ = f(y)` once more gives `y″ = f′(y)·f(y)`, which fixes the "
            "bend, so a solution has an inflection exactly where it crosses a level at "
            "which `f′` changes sign. The lab computes those levels exactly and draws the "
            "curves for comparison."
        ),
        "key": [
            "y″ = f′(y)·y′ = f′(y)·f(y)",
            "horizontal at y*, monotone in each gap",
            "y″ > 0 where f′ and f have the same sign",
            "inflection at a level where f′ changes sign",
            "curves never cross; slide one: another",
        ],
        "key_label": "What a sketch must show, and how the bends are found",
        "concepts_intro": (
            "Three ideas. The phase line fixes the outline, one more derivative fixes the "
            "bends, and the bends sit at levels and not at times."
        ),
        "concepts": [
            ("The phase line fixes the outline",
             "Draw each equilibrium as a horizontal line across the plane. Between two of them "
             "every solution is monotone, rising or falling as the arrow says, never touching "
             "either line, and levelling off towards a stable equilibrium. Close to an "
             "unstable one it leaves slowly and then speeds up."),
            ("The second derivative is f′ times f",
             "Differentiate `y′ = f(y)` by the chain rule: `y″ = f′(y)·y′`, and `y′` is `f(y)`, so "
             "`y″ = f′(y)·f(y)`. It is positive, concave up, where `f′` and `f` have the same "
             "sign, and negative, concave down, where their signs differ. Both are "
             "functions of `y` alone."),
            ("The bend changes at a level, not at a time",
             "A solution can only change its bend where `y″` changes sign. At an "
             "equilibrium `f` is zero but the solution is a straight line, so that is no bend. "
             "Elsewhere it is where `f′` is zero and changes sign: a height `y`, the same "
             "for every solution that crosses it, reached at a time that differs from solution "
             "to solution."),
        ],
        "read_title": "Drawing the curves the phase line allows",
        "read_intro": "The second derivative worked out, one equation sketched in full, and the cases where the inflection cannot be placed exactly.",
        "body": [
            ("thm", ("The second derivative of a solution",
                     "If `y` solves `y′ = f(y)`, with `f` a polynomial, then "
                     "`y″ = f′(y)·f(y)`.")),
            ("proof", ["Differentiate both sides of `y′ = f(y)` with respect to `t`. On the "
                       "left that gives `y″`. On the right the chain rule gives "
                       "`f′(y)·y′`, the slope of `f` at the height `y` times the rate at "
                       "which `y` is changing.",
                       "Replace `y′` by `f(y)` in that product, which the equation allows at "
                       "every `t`. The result is `y″ = f′(y)·f(y)`, a function of `y` alone."]),
            ("p", "Take `y′ = (y − 1)·(y − 3)`. Then `f′(y) = 2y − 4`, and "
                  "`y″ = (2y − 4)·(y − 1)·(y − 3)`. It is zero at `y = 1` and `y = 3`, "
                  "which are equilibria, and at `y = 2`, which is not."),
            ("math", [
                "gap        f′     f     y″      shape",
                "y < 1      −      +     −       concave down",
                "1 < y < 2  −      −     +       concave up",
                "2 < y < 3  +      −     −       concave down",
                "y > 3      +      +     +       concave up",
            ]),
            ("p", "A solution from `y(0) = 5/2` is in the gap `(1, 3)`, with `f(5/2) = −3/4`, "
                  "so it falls. Above `2` it is concave down, `y″ = (1)·(−3/4) = −3/4` at "
                  "the start. It crosses the level `2` and from there it is concave up, "
                  "`y″ = 3/4` at `y = 3/2` where `f′ = −1` and `f = −3/4`, flattening out "
                  "towards `1`. The inflection is at the level `y = 2`."),
            ("h3", "Why the steepest place is the inflection"),
            ("p", "In the gap `(1, 3)` the speed `|f(y)|` is `1` at `y = 2` and less everywhere "
                  "else, so the curve is steepest as it crosses `2`. A curve that is steepest "
                  "at a point has no change of slope there, which is `y″ = 0`. The "
                  "inflection and the maximum speed are the same level."),
            ("h3", "What a sketch must show"),
            ("ul", ["Each equilibrium as a horizontal line, solutions never crossing it.",
                    "In each gap, curves that rise or fall as the arrow says, monotone, "
                    "levelling off towards a stable equilibrium.",
                    "Each inflection level as a guide, with the bend flipping where "
                    "a curve crosses it.",
                    "Any curve slid left or right as another curve of the same equation."]),
            ("example", ("A logistic S-curve from the phase line",
                         "Take `y′ = y·(1 − y/4)`, so `f(y) = y − y²/4` and `f′(y) = 1 − y/2`, "
                         "zero at `y = 2`, half of the equilibrium `4`. The slopes at "
                         "`y = 1/2, 1, 2, 3` are `7/16, 3/4, 1, 3/4`, and `0` at `y = 4`.",
                         "From `y(0) = 1` the curve rises, concave up until it crosses `2`, steepest "
                         "there, then concave down, levelling off at `4`. From `y(0) = 6` it falls to "
                         "`4`, concave up all the way, with no inflection, since `f′ < 0` and "
                         "`f < 0` above `4`. &ldquo;Logistic Growth&rdquo; in Separable Equations, "
                         "Growth and Decay found the same level `K/2` as the point of fastest "
                         "growth and printed `y = 2` in the same tile; the phase line now says "
                         "why the fastest point and the change of bend are one level.")),
            ("p", "The cubic of the earlier lessons has `f′(y) = 3y² − 8y + 3`, whose roots "
                  "are `(4 ± √7)/3`, exactly, and `≈ 0.451416` and `≈ 2.21525` rounded. The "
                  "inflection levels are real and irrational. The lab places only the rational ones, "
                  "so its inflection tile reads `none rational` there; the sketch "
                  "still has two bends, at heights that are not fractions."),
        ],
        "lab": ("dekit", {
            "mode": "autonomous",
            "view": "curves",
            "preset": "two",
            "presets": [
                _p("two", "f(y) = (y − 1)(y − 3), typed expanded", "y^2 - 4y + 3", [0, "3/2", "5/2", 4], "1/4", 8,
                   [4, -1, 5], {"auEquil": "1, 3", "auInflect": "y = 2"}),
                _p("logistic", "f(y) = y(1 − y/4)", "y(1 - y/4)", ["1/2", 1, 6], "1/4", 8,
                   [8, -1, 7], {"auEquil": "0, 4", "auInflect": "y = 2"}),
                _p("cubic", "f(y) = y(y − 1)(y − 3), typed expanded", CUBIC, ["1/2", "5/2", "7/2"], "1/4", 8,
                   [3, -1, 5], {"auEquil": "0, 1, 3", "auInflect": "none rational"}),
            ],
            "panel_title": "Compare the sketch with the drawn curves",
            "panel_intro": "The picture shows the curves, drawn by stepping in floating point, "
                           "against the equilibria as horizontal lines; the legend says "
                           "which is which. The inflection tile is exact. Sketch first from "
                           "the phase line, then compare, and note where each curve changes "
                           "its bend.",
        }),
        "steps_title": "Sketching solution curves from f",
        "steps_intro": "Five moves, each using something computed earlier in the course.",
        "steps": [
            ("Draw the equilibria as horizontal lines",
             "Find them exactly and draw them across the `t`–`y` plane, labelled stable or "
             "unstable. No curve will cross any of them."),
            ("Sketch the monotone curves in each gap",
             "Use the arrow of the gap: up or down, levelling off at a stable end, "
             "leaving an unstable end slowly. A gap with no equilibrium at an end has "
             "curves that run off the page."),
            ("Compute `f′` and find where it is zero",
             "Differentiate, solve `f′(y) = 0` exactly, and keep the roots at which `f′` "
             "changes sign and `f` is not zero. Each is the level of an inflection."),
            ("Read the bend in every strip",
             "Between the lines, `y″ = f′·f` is positive where the signs agree and negative "
             "where they differ. Draw each curve concave up or down accordingly, flipping "
             "where it crosses an inflection level."),
            ("Compare with the drawn curves",
             "Check the arrows, the levelling off and the level of each flip against the "
             "lab. A curve that crosses an equilibrium, or has a bend at the wrong "
             "level, has a slip in a sign."),
        ],
        "worked": {
            "title": "y′ = (y − 1)(y − 3): the curve from y(0) = 5/2",
            "intro": [
                "Here `f′(y) = 2y − 4`, so `y″ = (2y − 4)·f(y)`. Find the level of the "
                "bend, then read the shape of the solution on each side of it.",
            ],
            "lines": [
                "y″ = f′(y)·f(y) = (2y − 4)·(y − 1)·(y − 3)",
                "f′(y) = 0  at  y = 2",
                "",
                "y = 5/2:  f = −3/4,  f′ = 1    y″ = −3/4   down",
                "y = 3/2:  f = −3/4,  f′ = −1   y″ = 3/4    up",
                "",
                "from 5/2: falls, concave down to y = 2,",
                "then concave up, levelling off at 1",
            ],
            "after": [
                "The curve is monotone, falling, and never reaches `1` or goes below it. "
                "It changes bend at the level `y = 2`, where it is steepest: the "
                "lab's inflection tile reads `y = 2`, and the start `5/2` is drawn crossing that "
                "level. The start `3/2` is already below it, and its curve is concave up throughout.",
                "For a rehearsal, take the start `y(0) = 4` on the same equation. "
                "`f(4) = 3` and `f′(4) = 4`, so `y″ = 12 > 0`: rising and concave up, with no "
                "inflection, running off the page.",
            ],
        },
        "quiz_title": "From the phase line to the curve",
        "quiz": [
            {"q": "For `y′ = y·(1 − y/4)`, at which level do the curves change their bend?",
             "a": ["`y = 2`", "`y = 4`", "`y = 1`", "`y = 0`"],
             "c": 0,
             "why": "`f′(y) = 1 − y/2` is zero at `y = 2`, and it changes sign there. `0` and "
                    "`4` are equilibria, where the curve is a horizontal line and "
                    "not a bend, and `y = 1` is just a height with no special slope."},
            {"q": "For `y′ = (y − 1)·(y − 3)` and `y(0) = 4`, the solution is",
             "a": ["Falling and concave up", "Rising and concave down", "Rising and concave up", "Falling and concave down"],
             "c": 2,
             "why": "`f(4) = 3 > 0`, so it rises, and `y″ = f′(4)·f(4) = 4·3 = 12 > 0`, so "
                    "it is concave up. The other three choices each get at least one of "
                    "the two signs wrong."},
            {"q": "The equilibria of an equation are `1` and `3`. Which of these curves cannot be a solution?",
             "a": ["One rising from `0` and levelling off at `1`", "One that crosses the line `y = 3`", "One falling from `5/2` towards `1`", "One that is another solution moved `2` to the right"],
             "c": 1,
             "why": "`y = 3` is a solution, and through each point passes only one, so no "
                    "other solution crosses it. The others are allowed: a rise from "
                    "`0` is in the gap below `1`, a fall from `5/2` is in `(1, 3)`, and "
                    "moving a solution sideways gives another solution."},
            {"q": "A solution of `y′ = (y − 1)·(y − 3)` passes through `y = 2` at some time. What is `y″` there?",
             "a": ["`−1`", "`1`", "Undefined", "`0`"],
             "c": 3,
             "why": "`y″ = f′(2)·f(2) = 0·(−1) = 0`, since `f′(y) = 2y − 4` is zero at "
                    "`y = 2`. It is defined, because `f` is a polynomial, and the value `−1` "
                    "is `f(2)`, the slope, and not the second derivative."},
        ],
        "mistakes": [
            ("Sketching a curve between two equilibria as a straight line or a parabola",
             "For `y′ = y·(1 − y/4)` the slopes at `y = 1/2, 1, 2, 3, 4` are "
             "`7/16, 3/4, 1, 3/4, 0`. A straight line has one slope throughout, and a "
             "parabola cannot level off at both ends. The curve is an S: slope rising to "
             "`1` at `y = 2` and falling to `0` at `y = 4`. The shape comes from `f`, and "
             "each equation draws its own."),
            ("Marking the equilibria as inflections",
             "At an equilibrium `f = 0`, so `f′·f = 0` and `y″ = 0` there. That is a "
             "horizontal straight line, which has no bend, and the solutions near it "
             "are the ones that bend. An inflection needs `f′` to change sign at a level "
             "where `f` is not zero, as at `y = 2` for the quadratic."),
            ("Putting the inflection at a time instead of a level",
             "The bend changes where a solution crosses `y = 2`, and two solutions of the "
             "same equation reach `2` at different times: starting at `1/2` and at `1` on "
             "the logistic equation, the first gets there later. The level is the same "
             "for both, which is why the lab reports `y = 2` and no time."),
        ],
        "standard": ("Finish when you can sketch solution curves from the phase line alone, with the inflection level computed.",
                     "You should be able to draw the equilibria as horizontal lines, sketch "
                     "monotone curves in each gap, work out `y″ = f′(y)·f(y)`, solve `f′(y) = 0` "
                     "for the levels of the bends, and check the sketch against the "
                     "drawn curves."),
        "note": "That completes first-order equations with no `t` in them: the phase line "
                "names the equilibria and their types, gives every limit, follows them as a "
                "parameter moves, and draws the curves. The next course takes the "
                "equations that do have `t` in them, but are linear, and solves them in closed "
                "form.",
    },
]
