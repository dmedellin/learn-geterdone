"""Differential Equations and Euler's Method."""


from . import part_a, part_b


COURSE = {
    "slug": "differential-equations-and-eulers-method",
    "title": "Differential Equations and Euler's Method",
    "level": "Intermediate",
    "summary": (
        "What an equation about a rate is, and the one way to answer it that needs nothing but "
        "arithmetic: take the rate where you are, step along it, and repeat. A proposed solution "
        "is checked by substituting it and reading the residual, an initial value picks one "
        "curve out of a family, a slope field draws the equation before anything is solved, and "
        "then Euler's method, the improved method and Runge&ndash;Kutta turn the equation into "
        "columns of exact fractions whose error is measured rather than guessed at."
    ),
    "blurb": (
        "A differential equation does not hand over a number or a formula. It states how a "
        "quantity changes, and the first job is to learn what counts as an answer: a function, "
        "usually a whole family of them, which is accepted or rejected by one substitution and "
        "one residual that either is zero for every `t` or is not. The second job is to "
        "see the equation without solving it, as a field of short segments, and to read off "
        "what the field settles and what it only suggests. The third is to compute. Euler's "
        "method is the sentence &ldquo;the next value is this value plus the rate times the "
        "step&rdquo;, applied in exact fractions, and the error against a known solution is "
        "exact too, so the course can show &mdash; with the ratio of two errors, not with a "
        "claim &mdash; that halving the step halves Euler's error, quarters the improved "
        "method's, and divides Runge&ndash;Kutta's by sixteen. It closes on the place all of "
        "this fails: a solution that ceases to exist, which a method keeps stepping past "
        "without noticing."
    ),
    "key": [
        "y′ = f(t, y)   the rate, stated",
        "residual = left − right;  0 for all t",
        "y(t₀) = y₀   one value picks one curve",
        "slope field: slope f(t, y) drawn at (t, y)",
        "yₙ₊₁ = yₙ + h·f(tₙ, yₙ)   exact fractions",
        "halve h: Euler error ÷ 2, improved ÷ 4",
        "RK4 error ÷ 16;  y′ = y² ends at t = 1",
    ],
    "assumes_short": "Accumulation and the Integral",
    "assumes_long": (
        "accumulation and the integral, and through it rates of change and the derivative: the "
        "difference quotient and what it approaches, the derivative of a polynomial and of "
        "1/t, the product and chain rules on polynomials, the antiderivative and the constant "
        "that comes with it, and a sum of rate times step as total change. The constant of "
        "integration is the whole reason an initial value is needed here, and the left sum is "
        "exactly Euler's method on the simplest equation, so both are leaned on: the constant "
        "from the first lesson, the left sum from “Euler's Method” on. From algebra, the "
        "exponential function and the number e, and the habit of checking an answer by "
        "substituting it back"
    ),
    "outcomes_intro": (
        "By the end you can say what a differential equation asks for, decide whether a "
        "proposed function answers it, draw and read its slope field, and carry out each of "
        "the three step methods by hand and in the lab, with the error stated and the "
        "failure of the method named."
    ),
    "outcomes": [
        ("Check a proposed solution by substitution",
         "Differentiate the candidate, put it in the equation, simplify the residual "
         "symbolically and decide: zero for every `t` is a solution, anything else is "
         "not, and a function that satisfies the equation at one value of `t` has "
         "shown nothing. Equations are named by order and sorted as linear or not."),
        ("Fix the constant from an initial value",
         "State how many initial values an equation needs &mdash; one for a first-order "
         "equation, two for a second-order one &mdash; solve for the constants in a family "
         "of solutions, and check that the result still has residual zero."),
        ("Draw and read a slope field",
         "Compute the slope at a grid point exactly, draw the segment, find the curve where "
         "the slope is zero, and say which conclusions the field settles (horizontal "
         "solutions, the direction of travel, that curves cannot cross) and which it only "
         "suggests."),
        ("Step an equation forward as exact fractions",
         "Carry out Euler's method by hand for several steps, read the table, and say what "
         "the method assumes inside each step; the fractions are right and the answer is "
         "still only as close as the step allows."),
        ("Measure an error and name the order of a method",
         "Compute the error at three step sizes, form the exact ratios and read the order: "
         "Euler's method is first order, the improved method second, Runge&ndash;Kutta "
         "fourth, each shown by a ratio that is exactly 2, 4 or 16 on a chosen equation."),
        ("Recognise a solution that ceases to exist",
         "Show that `y = 1/(1 − t)` solves `y′ = y²` and ends "
         "at `t = 1`, watch Euler's method step past it, and read the digit budget "
         "that stops an exact computation whose fractions double in length."),
    ],
    "syllabus_intro": (
        "The object first: what an equation about a rate is, how a proposed solution is "
        "tested, and how an initial value picks one curve from the family. Then the equation "
        "as a picture, a slope field read without solving anything. Then the computing, in "
        "order of cost and of accuracy &mdash; Euler's method, its error against the step "
        "size, the improved method and Runge&ndash;Kutta &mdash; and last the equation whose "
        "solution does not last, which is where a method that only ever looks one step "
        "ahead is least trustworthy."
    ),
    "how_to": [
        "Check before you trust. Every closed form on this course is tested by substituting "
        "it and reading the residual, and the lab does that symbolically, so the verdict is "
        "a fact about every `t` and not about the five you happened to try. Make the "
        "same habit yours: a candidate that works at one value of `t`, or for one "
        "choice of the constant, has not been checked.",
        "Say which tier a number is in. A fraction such as `625/256` is exactly what "
        "Euler's method produces and is exactly `(5/4)⁴`; the value of the "
        "true solution is often irrational and is printed as approximate, to six figures, "
        "and labelled rounded. "
        "Keep the two apart in your own working, because the gap between them is the error "
        "the course measures.",
        "Treat the method as a recipe and not as the answer. A step method assumes the "
        "rate stays what it was at the start of the step; nothing computed from it is the "
        "solution, only a value near it for a reason the error lessons can quantify. When "
        "a lab reports an error it is the error for that step size alone.",
        "Read the pictures for what they settle. A slope field gives the slope at each "
        "point exactly and the long-run behaviour only suggestively. Write down which of "
        "your conclusions came from the sign of the slope and which from the look of the "
        "curve, and trust them accordingly.",
    ],
    "not_covered": [
        "Existence and uniqueness proofs. “Blow-Up and the Interval of Existence” states in words "
        "what makes a solution through a given point exist and be the only one, and "
        "shows the equation that breaks the global version; the proof, the Lipschitz "
        "condition and the examples with more than one solution through a point are a "
        "course in analysis and are not here.",
        "Numerical analysis as a subject. Adaptive step size, error estimators, "
        "multistep methods, implicit Runge&ndash;Kutta and the theory of A-stability are "
        "all absent. The course shows the order of a method by exact ratios on chosen "
        "equations and stops; the one exact factor that explains why a method fails on a "
        "decaying equation comes in First-Order Linear Equations.",
        "Floating-point stepping as a computed result. Where an equation has no closed "
        "form the slope fields draw a curve by stepping in floating point, and the legend "
        "says it is drawn; nothing in a tile comes from it. A reader who wants a "
        "nonlinear equation's numbers is told the honest truth: stepping a quadratic "
        "right-hand side in exact fractions reaches the digit budget in about eleven "
        "steps, and floating point hides that by rounding at every step.",
        "Methods for finding closed forms of general equations. Exact equations, "
        "Bernoulli and Riccati equations and substitutions are not here; the equations "
        "whose solutions can be checked exactly are the ones the course uses, and the "
        "next courses teach the families that can actually be solved by hand.",
        "<strong>The claims this course states and does not prove.</strong> That the "
        "errors of the three methods shrink at the orders shown, which the exact ratios "
        "demonstrate on chosen equations and do not establish for every equation, and "
        "that a smooth right-hand side gives exactly one solution through a point near "
        "the start. Every figure printed is exact or labelled; neither claim is "
        "load-bearing for a number on the page.",
    ],
    "footer_lead": (
        "Every residual, slope, Euler step and error on this course is an exact fraction "
        "or a symbolic expression computed in your browser from the equation the lesson "
        "states, and a candidate solution is accepted only by substituting it and finding "
        "the residual zero for every `t`. <strong>The one quantity that is not "
        "rational says so</strong>: the true value of a solution at a step, such as `e ≈ 2.71828`, "
        "is printed to six figures, marked as approximate and labelled rounded, beside the exact "
        "fraction a method produced. Curves with no closed form are drawn by stepping in "
        "floating point and the legend says so; the numbers in the tiles never are. What "
        "none of this can do is turn a step method into the solution: a column of "
        "correct fractions is exact arithmetic applied to an approximate method, and how "
        "close it lies to the curve is the question each error tile answers for one step "
        "size only."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
