"""The Differential Equations path, as data.

Ten courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.

The calculus is taught inside the Subject, from exact difference quotients
and sums. Every step method runs in exact fractions, every closed form is
checked by symbolic substitution, and every irrational figure is printed with
its rounding stated. The design is docs/differential-equations/PLAN.md.
"""

from . import (
    c1_rates,
    c2_accumulation,
    c3_euler,
    c4_separable,
    c5_phase_lines,
    c6_linear,
    c7_second_order,
    c8_oscillators,
    c9_systems,
    c10_laplace,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_rates.COURSE,
    c2_accumulation.COURSE,
    c3_euler.COURSE,
    c4_separable.COURSE,
    c5_phase_lines.COURSE,
    c6_linear.COURSE,
    c7_second_order.COURSE,
    c8_oscillators.COURSE,
    c9_systems.COURSE,
    c10_laplace.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "differential-equations",
    "title": "Differential Equations",
    "level": "Intermediate \u2192 Advanced",
    "level_note": "assumes the Algebra Subject; the calculus is taught inside",
    "tagline": (
        "Change described by its rate: the derivative and the integral built from exact difference quotients and sums, then the equations that say how a quantity changes and the methods that recover the quantity &mdash; slope fields, Euler's steps as exact fractions, separable and linear equations, equilibria and phase lines, oscillators and resonance, systems in the phase plane, and the Laplace transform. Ten courses and 92 lessons are available."
    ),
    "description": (
        "The Differential Equations Subject: ten courses in one order, from rates of change and the derivative and accumulation and the integral, through what a differential equation is and Euler's method, separable equations and growth, equilibria and phase lines, first- and second-order linear equations, oscillators and resonance and systems in the phase plane, to Laplace transforms. Every step method runs in exact fractions in your browser, every closed form is checked by substitution, and every rounded number says so. All ten courses and 92 lessons are available."
    ),
    "key": [
        "Δy/Δt exactly, then what it approaches: y′",
        "∫ₐᵇ f(t) dt = F(b) − F(a)",
        "yₙ₊₁ = yₙ + h·f(tₙ, yₙ)   every yₙ a fraction",
        "y′ = k·y  ⟹  y = y₀·e^(kt)",
        "f(y*) = 0, f′(y*) < 0  ⟹  stable",
        "a·r² + b·r + c = 0   roots decide the motion",
        "x′ = A·x:  τ and Δ of A pick the portrait",
        "ℒ[y′] = s·Y − y(0)   calculus becomes algebra"
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Accumulation and the Integral reverses the rules of Rates of Change and the Derivative; Differential Equations and Euler's Method uses both; Separable Equations, Growth and Decay and Equilibria, Stability and Phase Lines read first-order equations two different ways; First-Order Linear Equations needs the product rule and the integral; Second-Order Linear Equations needs the quadratic formula from Algebra and nothing new; Oscillators, Damping and Resonance, Systems and the Phase Plane and Laplace Transforms each take the second-order theory somewhere else."
    ),
    "why_order": ['The derivative comes first because a differential equation is a statement about one, and a reader who thinks `dy/dt` is a fraction will misread every equation that follows. It is taught as what exact difference quotients approach, and for polynomials as the constant term of a polynomial in `h`, so that the first course asks for no faith.', 'The integral comes second and is kept short, because the Subject needs exactly two things from it: that accumulated change is a sum that refines to a number, and that reversing the power rule recovers a function up to a constant. The constant is the whole reason an initial value is needed, and it is met here, once, before any equation.', "Euler's method comes before any closed form, because it is what a differential equation *means*: the next value is this value plus the rate times the step. Every closed form later in the Subject is checked against those exact steps, and every step method's error is measured against a closed form, so the two halves of the Subject keep each other honest.", 'First-order equations fill four courses before second-order ones because growth, equilibria and stability are where the ideas live; the second-order theory is then one quadratic equation, and oscillators, systems and the Laplace transform are three readings of its roots.'],
    "prerequisites": ['The Algebra Subject, and specifically four of its courses: Lines, Functions and Graphs (function notation, slope, what a graph is), Polynomials and Factoring (expanding `(t + h)²`, which the first course does on every page), Quadratics and Complex Numbers (the quadratic formula and `i`, which decide every second-order equation here), and Exponential and Logarithmic Functions (`e`, `ln`, and why `e^(kt)` doubles in a fixed time). Systems and Matrices helps with the phase plane and is named where it is used.', 'No calculus. Rates of Change and the Derivative starts from a difference quotient computed as a fraction and reaches the derivative without taking a limit you have to believe: for a polynomial the quotient is a polynomial in `h` and the derivative is its constant term. Accumulation and the Integral does the same for sums. If you have met calculus before you will move quickly; if you have not, those two courses are the whole of what is assumed later.', 'Fractions, and patience with them. Every Euler step on this path is an exact fraction, and after twenty steps the denominators are long. The labs do the arithmetic; what is asked of you is to read a fraction beside a decimal and know which one is the true value of the method.', 'No programming. Nothing here asks you to write code. The labs run so that you can change a step size and watch the error halve, which is the one thing a printed page cannot do.'],
    # Each path names its own hazard. This one's is that the labs are exact and
    # the method is not: a column of correct fractions is Euler's polygon.
    "material": (
        'every figure on this path is computed in your browser from the equation the lesson states, and a numerical solution is exact arithmetic applied to an approximate method &mdash; the fractions are right, and the answer is still only as close as the step allows.'
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from the equation the lesson states, in three honest tiers: every step method runs in exact fractions, and prints them; every closed-form solution is checked by substituting it into the equation symbolically and reading the residual, never by evaluating it; and every number that is genuinely irrational &mdash; a value of `e^(kt)`, a doubling time, a period &mdash; is printed with `≈` to six figures and labelled rounded. Curves that have no closed form are drawn by stepping in floating point and the legend says so; the numbers in the tiles never are. What the labs cannot do is make a numerical method into the solution: a correct fraction is a correct value of Euler's polygon, and how close that is to the curve is the question every error tile on this path answers for one step size only."
    ),
    "courses": COURSES,
}
