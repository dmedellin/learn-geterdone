"""Separable Equations, Growth and Decay."""


from . import part_a, part_b


COURSE = {
    "slug": "separable-equations-growth-and-decay",
    "title": "Separable Equations, Growth and Decay",
    "level": "Intermediate",
    "summary": (
        "The first family of equations that can be solved in closed form: those where `y` can "
        "be gathered on one side and `t` on the other, so that each side can be integrated on "
        "its own. The method is the chain rule read backwards, its answer is often an "
        "implicit relation whose branch an initial value picks, and the simplest case, "
        "`y′ = k·y`, is the exponential &mdash; with Euler's exact steps arriving as the "
        "geometric sequence they always were. Doubling time, decay and dating, cooling, "
        "mixing, and then growth that levels off and growth that is harvested."
    ),
    "blurb": (
        "One method carries this whole course: write the equation as `g(y)·y′ = h(t)`, find an "
        "antiderivative of each side, and the relation between `y` and `t` falls out with one "
        "constant in it. What the course adds to the method is care about what it produces. An "
        "answer such as `y² = t² + 4` is not yet a function; it becomes one only when an "
        "initial value picks a sign, and it stops being one where the square root runs out. "
        "The simplest equation of all, `y′ = k·y`, gets the most attention, because Euler's "
        "method on it is an exact geometric sequence the lab prints beside `e^(kt)`, and the "
        "gap between the two is the same gap the previous course measured. Every figure that "
        "is a fraction is printed as one; every value of `e^(kt)` and every `ln 2` is rounded "
        "to six figures and marked `≈`, and the lessons say so wherever one appears."
    ),
    "key": [
        "g(y)·y′ = h(t)  ⟹  ∫g dy = ∫h dt + C",
        "G(y(t)) has rate g(y)·y′: chain rule",
        "y² = t² + 4: the sign of y(0) picks y",
        "y′ = k·y  ⟹  y = y₀·e^(kt)",
        "Euler:  yₙ = y₀·(1 + kh)ⁿ, geometric",
        "T = ln 2/k   independent of the starting y₀",
        "y′ = r·y·(1 − y/K) levels off;  H* = r·K/4",
    ],
    "assumes_short": "Differential Equations and Euler's Method; the exponential and logarithm from Algebra",
    "assumes_long": (
        "Differential Equations and Euler's Method, which supplies what a solution is, how an "
        "initial value fixes one, and Euler's steps as exact fractions, and through it "
        "Accumulation and the Integral for antiderivatives and the constant of integration. "
        "From Algebra, Exponential and Logarithmic Functions for `e`, the logarithm and why `e^(kt)` "
        "doubles in a fixed time, and the geometric sequence from Sequences and Series, which "
        "Euler's method on a growth equation turns out to be"
    ),
    "outcomes_intro": (
        "By the end you can recognise a separable equation, integrate both sides exactly, and "
        "say what the answer is and where it holds. You can then use the one equation "
        "`y′ = k·(y − A)` for growth, decay, dating, cooling and mixing, and read a bounded "
        "growth law and a harvested one from their right-hand sides."
    ),
    "outcomes": [
        ("Separate, integrate, and fix the constant",
         "Recognise `g(y)·y′ = h(t)`, integrate both sides exactly, and write the implicit "
         "solution with its constant taken from an initial value &mdash; checking each "
         "antiderivative against the lab rather than trusting a sign."),
        ("Justify the method, not just run it",
         "Explain separation as the chain rule read backwards, and verify a solution by "
         "differentiating the implicit relation to get the equation back."),
        ("Solve an implicit relation for y and say where it holds",
         "Take the branch the initial value demands, and state the interval on which the "
         "explicit solution exists &mdash; including the one that ends in finite time."),
        ("Solve and run the exponential equation",
         "Solve `y′ = k·y` by separation, get Euler's `yₙ = y₀·(1 + kh)ⁿ` exactly, and read "
         "the gap between that sequence and the rounded `e^(kt)` at the same time."),
        ("Convert between a rate, a doubling time and a half-life",
         "Derive `T = ln 2/k` from `e^(kT) = 2`, state it as rounded, and find the first step "
         "at which the exact Euler sequence passes double or half."),
        ("Model a quantity that approaches a level",
         "Write cooling, mixing and logistic growth as first-order equations, find their "
         "equilibria, and compute the harvest threshold `r·K/4` above which a population "
         "collapses."),
    ],
    "syllabus_intro": (
        "The method first, in three lessons: how to separate and integrate, why that is "
        "legitimate, and what the answer means once it is an implicit relation. Then the "
        "exponential equation and its two readings, a rate and a doubling time. Decay, dating, "
        "cooling and mixing follow as one equation with a shift in it. The last part adds a "
        "bound to the growth, and then removes some of it again."
    ),
    "how_to": [
        "Write the equation in the form `g(y)·y′ = h(t)` before you integrate anything. If it "
        "will not go into that form, the method does not apply, and no amount of cleverness "
        "with the integral signs will make it. The lab refuses a `g` it cannot integrate and "
        "says which one.",
        "Check every solution by differentiating it. The lab does this with the chain rule and "
        "prints `equal` or not, and the habit is worth more than the printout: a sign lost in "
        "an antiderivative produces a perfectly smooth wrong answer that no later step will "
        "flag.",
        "Say which tier a number is in. The Euler sequence is a column of exact fractions, "
        "`e^(kt)` and `ln 2` are rounded and carry `≈`, and the difference between them is "
        "the method's error at that step size and no other. Quote the step size with the "
        "figure.",
        "Treat a model as an equation someone gave you. Every application here states its "
        "assumptions &mdash; a well-stirred tank, a constant rate constant, a population with "
        "a fixed carrying capacity &mdash; and the lab computes what follows from them; "
        "whether the assumptions hold for a real tank is not something it can tell you.",
    ],
    "not_covered": [
        "Equations that cannot be separated. `y′ = t + y` has no `g(y)·y′ = h(t)` form, and "
        "the method of the first-order linear course handles it instead. Exact equations, "
        "Bernoulli equations and substitutions that turn an equation into a separable one are "
        "techniques for finding closed forms the exact lab cannot verify, and they are left "
        "out on purpose.",
        "Integrals beyond polynomials and the two reciprocals. The lab separates `g(y)` that is "
        "a polynomial in `y`, or exactly `1/y` or `1/y^2`, and `h(t)` that is a polynomial in "
        "`t`. Partial fractions in `y`, which the full logistic solution needs, are not built "
        "here: the logistic lessons read the equation from its equilibria and from exact "
        "Euler steps instead of from a formula.",
        "Existence and uniqueness. A separable equation can have a solution that stops in "
        "finite time, and the course shows one. Why an initial value picks exactly one "
        "solution, and when it does not, is stated in words in the previous course and not "
        "proved anywhere.",
        "Modelling as a skill. The tank, the cup of coffee, the carbon sample and the "
        "population are given with their equations. Deriving such a model from measurements, "
        "fitting its constants and judging whether it fits are a statistics course's work.",
    ],
    "footer_lead": (
        "Every antiderivative, constant and Euler step on this course is an exact fraction, "
        "and every closed form is checked by differentiating it, never by evaluating it. "
        "<strong>The figures that are not rational say so</strong>: a value of `e^(kt)`, a "
        "doubling time `ln 2/k` and the error against a closed form are printed rounded to "
        "six figures and marked `≈`. A column of Euler fractions is correct arithmetic "
        "applied to an approximate method, and how close it is to the curve depends on the "
        "step size shown beside it. What none of this can do is tell you that the equation is "
        "the right one for the tank, the sample or the population you meant."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
