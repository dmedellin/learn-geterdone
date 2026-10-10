"""Equilibria, Stability and Phase Lines."""

from . import part_a, part_b


COURSE = {
    "slug": "equilibria-stability-and-phase-lines",
    "title": "Equilibria, Stability and Phase Lines",
    "level": "Intermediate → Advanced",
    "summary": (
        "When an equation has no clock in it, the long-run answer can be read off without "
        "solving anything. Find the roots of `f`, test its sign between them, and the phase "
        "line says where every solution goes; classify each equilibrium by the signs or by "
        "the slope `f′`; follow the equilibria as a parameter moves until two of them meet "
        "and vanish; and sketch the solution curves, with the inflection level computed."
    ),
    "blurb": (
        "The last course solved equations: it separated the variables and integrated. This "
        "one asks a different question of the same first-order equations, and it is often the "
        "more useful one. For `y′ = f(y)` nobody needs a formula to say that a solution "
        "starting at 2 settles at 1, or climbs without limit, or that a small change in a "
        "parameter makes two equilibria collide and disappear. All of it comes from the sign "
        "of `f`, which a browser can evaluate exactly, and from one derivative. The lab "
        "keeps the exact side exact: equilibria are fractions or surds, the slope at each is "
        "an exact number, and the only things that are drawn rather than computed are the "
        "solution curves, which the legend says are stepped in floating point. The method is "
        "approximate, the classification is not."
    ),
    "key": [
        "y′ = f(y):  no t on the right",
        "f(y*) = 0   y* is a constant solution",
        "f: + to −  stable;   − to +  unstable",
        "f′(y*) < 0  stable",
        "f′(y*) > 0  unstable;  f′(y*) = 0  undecided",
        "y′ = f(y, a):  equilibria move and meet",
        "y″ = f′(y)·f(y):  bends where f′ = 0",
    ],
    "assumes_short": "Separable Equations, Growth and Decay",
    "assumes_long": (
        "separable equations, growth and decay: the solution of `y′ = k·y`, the logistic "
        "equation with its two equilibria, and harvesting with its threshold, which this "
        "course reads again from the sign of `f` instead of from a formula. Behind that sit "
        "differential equations and Euler's method, from which the slope field and the exact "
        "Euler steps are used on every page, and the derivative of a polynomial from Rates "
        "of Change and the Derivative, which is all the calculus the slope test needs"
    ),
    "outcomes_intro": (
        "By the end you can take a first-order equation with no `t` in it, decide where "
        "its solutions go from any start without solving it, say how stable each equilibrium "
        "is and why, and predict what happens to the equilibria when a parameter moves."
    ),
    "outcomes": [
        ("Recognise an autonomous equation and find its equilibria exactly",
         "The test is whether `t` appears on the right; the equilibria are the roots of "
         "`f`, as fractions or surds, each checked by substituting the constant solution."),
        ("Draw the phase line from the sign of `f`",
         "The equilibria in order, one exact test value in every gap, and an arrow in each, "
         "with the direction of every solution read off it."),
        ("Classify each equilibrium as stable, unstable or semistable",
         "From the signs on either side of the root, and again from the sign of `f′` at "
         "it, with the case `f′ = 0` named as the one the second method cannot decide."),
        ("State the long-run behaviour of a solution from its start",
         "The limit of a solution from any starting value as an equilibrium or `±∞`, "
         "with the claim checked against exact Euler steps."),
        ("Follow the equilibria as a parameter changes",
         "Where two of them meet, the value of the parameter at which they do, and the "
         "fork and exchange shapes read off a bifurcation diagram."),
        ("Sketch solution curves from the phase line alone",
         "Horizontal at the equilibria, monotone between them, and bending where `f′(y)` is "
         "zero, with the sketch checked against curves the lab draws."),
    ],
    "syllabus_intro": (
        "The course goes from the equation to the picture and then to the things the "
        "picture can do. Autonomous equations and the phase line come first, because "
        "everything after is read from them. Classifying equilibria comes second, by "
        "signs and then by a derivative, and ends with the limit of a solution found "
        "without solving. The third part adds a parameter, and the last uses the phase "
        "line to draw the curves the earlier courses could only compute point by point."
    ),
    "how_to": [
        "Read the sign of `f` before reaching for a formula. In every lesson the first "
        "move is the same: find the roots, test between them, draw the arrows. The "
        "answers that follow are usually available at that point, and a formula for the "
        "solution, where one exists, adds detail and not direction.",
        "Say whether an answer came from the signs or from `f′`. The signs always decide; "
        "the slope decides unless it is zero, and also supplies a rate. A verdict from "
        "the slope with no check against the signs is a verdict that cannot be told from a "
        "slip.",
        "Treat a limit as a claim about a phase line, not about a table. The exact Euler "
        "steps on these pages are an approximate method applied exactly, and a column of "
        "them that climbs is evidence for `→ +∞`, not proof. What the phase line "
        "gives is the reason.",
        "Keep exact and rounded apart. An equilibrium like `(1 ± √5)/2` is exact; "
        "`≈ 1.61803` is its rounding. Write the first when you mean equality, and the "
        "second only when you are reporting a size.",
    ],
    "not_covered": [
        "Proofs of existence and uniqueness. That one solution passes through each point is "
        "used throughout, because it is why a solution can approach an equilibrium and "
        "never cross it; it is stated in words in Differential Equations and Euler's "
        "Method and is not proved here.",
        "The proof that the sign of `f′` decides stability. The slope test is demonstrated "
        "on every equation the lab is given, by printing `f′` at each equilibrium beside "
        "the type found from the signs, and derived exactly on one equation by hand. Showing "
        "that the neglected terms cannot overturn it, for every `f`, is a task for a "
        "first course in analysis.",
        "Bifurcation theory beyond one parameter. The saddle-node, transcritical and "
        "pitchfork shapes are read from the equilibria the lab computes; normal forms, "
        "imperfect bifurcations, hysteresis loops and the Hopf bifurcation, which needs "
        "two variables, are not here. Systems and the Phase Plane takes the step to two "
        "variables.",
        "Right-hand sides that are not polynomials. The lab refuses `sin(y)` or `1/y` "
        "rather than round its way through them, because its equilibria and signs are exact. "
        "The method carries over unchanged, with roots found by other means.",
        "Equations that depend on time. A forced equation, `y′ = f(y) + g(t)`, has no phase "
        "line, because the arrows would move; First-Order Linear Equations treats the "
        "linear case, and the general case is a different subject.",
        "<strong>What this course states and does not prove.</strong> That the sign of "
        "`f′(y*)` settles stability when it is nonzero. Every figure on the course "
        "is computed from the equation without it, so the unproved statement carries no "
        "number, and the sign test, which needs no theorem, is available alongside it "
        "on every page.",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every equilibrium, sign, slope and "
        "classification on this course is exact: roots are fractions or surds, `f` is "
        "evaluated at exact test points, and `f′` is an exact number at each root. "
        "The exact Euler steps beside them are exact arithmetic applied to an approximate "
        "method &mdash; each fraction is right, and the polygon is still only as close to "
        "a solution as the step allows. Where a number is irrational it is printed with "
        "`≈` and called rounded. The solution curves in the last lesson are drawn by "
        "stepping in floating point, the legend says so, and nothing in a tile comes from "
        "them. One result is stated and not proved, and says so: that the sign of `f′` "
        "decides stability when it is nonzero. What none of this can do is tell you "
        "whether the equation you wrote down is the system you meant."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
