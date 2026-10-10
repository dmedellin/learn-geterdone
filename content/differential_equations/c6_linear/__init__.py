"""First-Order Linear Equations."""

from . import part_a, part_b

COURSE = {
    "slug": "first-order-linear-equations",
    "title": "First-Order Linear Equations",
    "level": "Advanced",
    "summary": (
        "The equation `y′ + p(t)·y = q(t)` and the three ideas that solve it: a steady "
        "state that a gap decays toward, an integrating factor that turns the left side "
        "into a derivative, and a solution split into a homogeneous part and one particular "
        "part. Then forcing by polynomials, exponentials and sinusoids, circuits, tanks "
        "and loans as one equation, and the step size at which Euler's method stops "
        "following a decay."
    ),
    "blurb": (
        "One equation does a great deal of work. A tank filling, a capacitor charging, a "
        "loan being repaid and a cooling cup of coffee are all `y′ + a·y = b` with different "
        "letters, and every one of them is a constant plus a gap that shrinks by a fixed "
        "factor in equal times. This course solves that equation three ways: as a shifted "
        "exponential, by multiplying through by an integrating factor that makes the left "
        "side a derivative, and as a homogeneous solution plus one particular solution "
        "found by a guess whose coefficients are matched exactly. The cases that are "
        "exact throughout are the ones with `p` constant or `a/t`, where the factor is an "
        "exponential or a power of `t`. The last lesson turns to the method rather than the "
        "equation: Euler's factor `1 − a·h` is an exact fraction, and it leaves the "
        "interval from `−1` to `1` at a step size you can compute."
    ),
    "key": [
        "y′ + p(t)·y = q(t)    p and q read off first",
        "y′ + a·y = b:  steady state y* = b/a",
        "μ = e^(∫p dt),   (μ·y)′ = μ·q",
        "y = y_p + y_h    fit C last",
        "undetermined coefficients: exact matching",
        "Euler on y′ = −a·y:  factor 1 − a·h",
        "stable only while h < 2/a",
    ],
    "assumes_short": "Equilibria, Stability and Phase Lines",
    "assumes_long": (
        "the previous course, Equilibria, Stability and Phase Lines, for the idea that a constant "
        "solution can attract or repel, together with Separable Equations, Growth and Decay "
        "for `y′ = k·y` and its exponential solution, Differential Equations and Euler's Method "
        "for Euler's steps as exact fractions, the product rule from Rates of Change and the "
        "Derivative, and antiderivatives of powers from Accumulation and the Integral"
    ),
    "outcomes_intro": (
        "By the end you can put a first-order linear equation in standard form, solve it "
        "by whichever of the three methods suits it, fit the constant from a starting "
        "value, check every answer by substitution, and say at what step size Euler's "
        "method stops following a decay."
    ),
    "outcomes": [
        ("Write an equation in standard form and read p and q",
         "Divide every term by the coefficient of `y′`, name `p` and `q` with their signs, "
         "say whether the equation is homogeneous, and say why `t²·y` is linear and "
         "`y²` is not."),
        ("Solve y′ + a·y = b and name the steady state",
         "Find `b/a`, write the starting gap, put it on `e^(−at)`, say whether the "
         "steady state attracts, and compare Euler's exact steps with the closed form."),
        ("Build and use an integrating factor",
         "Construct `μ` with `μ′ = p·μ`, show that the left side becomes `(μ·y)′`, "
         "and solve a case with `μ = tᵃ` entirely in fractions."),
        ("Split a solution into homogeneous and particular parts",
         "Find one particular solution by a guess with matched coefficients, add the "
         "homogeneous solution, and fit the constant after the sum."),
        ("Fit particular solutions to polynomial, exponential and sinusoidal forcing",
         "Choose the form from the forcing, match coefficients exactly, and handle the "
         "resonant case where the forcing matches the homogeneous solution."),
        ("Bound the step size at which Euler's method fails",
         "Compute the factor `1 − a·h`, derive `h < 2/a` for decay, and show that the "
         "backward factor decays at every step size."),
    ],
    "syllabus_intro": (
        "The form first, because every method assumes it, then the constant-coefficient "
        "case, which needs nothing more than a shifted exponential. The integrating "
        "factor and the split into homogeneous and particular parts are two solutions of "
        "one equation, and the forcing lessons make the second of them a method. "
        "Applications come next, and the course ends with the step size, where the "
        "exact arithmetic of the labs exposes what a decimal would hide."
    ),
    "how_to": [
        "Read the standard form before doing anything else. Every formula on this course "
        "is written for `y′` with coefficient 1, and the commonest error is a formula "
        "applied to an equation that has not been divided yet. The lab states `p` and `q` "
        "in its status line so that you can compare them with your own.",
        "Check every solution by substituting it into the equation, not by comparing it "
        "with a picture. The check is one derivative and one addition, it is exact, and "
        "it catches a wrong sign in the exponent or a constant divided by the wrong "
        "factor, which a plot of a decaying curve does not.",
        "Fit the constant last. In every method here the general solution has the "
        "constant in it, and the starting value is a statement about the whole "
        "solution. Putting it in before the particular part is added is the error "
        "the course names more than once.",
        "Say which figures are exact. The fractions in the Euler columns are exact "
        "arithmetic on an approximate method, and a value of `e^(−2)` is rounded and "
        "printed with `≈`. The two sit side by side in the labs on purpose.",
    ],
    "not_covered": [
        "Variation of parameters as a general tool. The integrating factor is the "
        "first-order version and is complete here; the second-order version is named "
        "in Second-Order Linear Equations as the method that works when a guess does not.",
        "Equations whose coefficient `p(t)` is not a constant or `a/t`. The integrating "
        "factor `e^(∫p dt)` exists for any continuous `p`, and the lessons state it in "
        "general, but the labs solve only the two families whose factor is exact, and "
        "the course does not teach integrals that need a logarithm to print.",
        "Nonlinear equations that can be turned linear by a substitution, such as "
        "Bernoulli and Riccati equations. They are techniques for finding closed forms "
        "that the exact checks of this Subject cannot verify.",
        "Existence and uniqueness. A linear equation with continuous `p` and `q` has "
        "exactly one solution through each starting point on an interval where they "
        "are continuous; the course uses this and does not prove it.",
        "Stiffness as a numerical-analysis topic. The last lesson shows one exact factor, "
        "its bound, and the backward method's answer to it. Stability regions, "
        "implicit Runge&ndash;Kutta methods and adaptive step sizes are not here.",
    ],
    "footer_lead": (
        "Every steady state, integrating factor, constant of integration, particular "
        "coefficient and Euler value on this course is an exact fraction or an exact "
        "symbolic expression, and the lessons check each solution by substituting it "
        "into the equation. A value of a closed form such as `e^(−2)` is irrational, and is "
        "printed rounded to six figures with `≈` and labelled. The Euler columns are "
        "exact arithmetic applied to an approximate method: the fractions are right, "
        "and each is only as close to the curve as the step allows."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
