"""Second-Order Linear Equations."""

from . import part_a, part_b

COURSE = {
    "slug": "second-order-linear-equations",
    "title": "Second-Order Linear Equations",
    "level": "Advanced",
    "summary": (
        "The equation `a·y″ + b·y′ + c·y = 0` and the single idea that solves it: try "
        "`y = e^(rt)`, and the equation becomes the quadratic `a·r² + b·r + c = 0`. The "
        "course starts from sine and cosine as each other's rates, shows why a "
        "second-order equation has two constants, solves the three kinds of root "
        "(real and distinct, repeated, complex), fits the constants from `y(0)` and "
        "`y′(0)`, and ends by rewriting the equation as a system and stepping an "
        "oscillator with Euler's method."
    ),
    "blurb": (
        "A mass on a spring, a pendulum at small angles and a circuit with an inductor "
        "all obey the same equation: the rate of the rate of the unknown, a multiple of "
        "its rate, and a multiple of the unknown itself add up to zero. Separable "
        "Equations, Growth and Decay solved `y′ = k·y` with `e^(kt)`; this course tries "
        "the same exponential on the second-order equation and finds that it works, "
        "provided `r` is a root of a quadratic. The quadratic is the one from Algebra, "
        "and its three possible "
        "discriminants give three shapes of solution: two exponentials, an exponential "
        "with a factor of `t`, and an exponential multiplied by a cosine and a sine. "
        "Every closed form is checked by substituting it into the equation, and the "
        "two constants are fitted from the starting value and the starting rate. The "
        "last two lessons look at the same equation from outside, as a pair of "
        "first-order equations whose matrix carries the quadratic inside its trace and "
        "determinant, and show Euler's method pushing a circle's worth of motion "
        "steadily outward."
    ),
    "key": [
        "a·y″ + b·y′ + c·y = 0    two constants",
        "y = e^(rt)  ⟹  a·r² + b·r + c = 0",
        "two real roots: C₁·e^(r₁t) + C₂·e^(r₂t)",
        "one root twice: (C₁ + C₂·t)·e^(rt)",
        "α ± βi:  e^(αt)·(C₁·cos(βt) + C₂·sin(βt))",
        "y(0) and y′(0) fix C₁ and C₂",
        "x′ = v,  v′ = −(c/a)·x − (b/a)·v",
        "Euler on x′ = v, v′ = −x:  × (1 + h²)",
    ],
    "assumes_short": "First-Order Linear Equations",
    "assumes_long": (
        "the previous course, First-Order Linear Equations, for the habit of checking a "
        "solution by substituting it, together with Separable Equations, Growth and "
        "Decay for the exponential solution of `y′ = k·y`, Differential Equations and "
        "Euler's Method for Euler's steps as exact fractions, the product rule from "
        "Rates of Change and the Derivative, and the quadratic formula and complex "
        "numbers from Algebra's Quadratics and Complex Numbers"
    ),
    "outcomes_intro": (
        "By the end you can turn a second-order linear equation with constant "
        "coefficients into its characteristic quadratic, solve it for every kind of "
        "root, fit both constants from starting values, check each answer exactly, and "
        "say what changes when the same equation is written as a system."
    ),
    "outcomes": [
        ("Read the rates of sine and cosine from a rounded table",
         "State `sin′ = cos` and `cos′ = −sin` as the claims the quotients "
         "demonstrate, and conclude that the rate of the rate of `cos` is `−cos`."),
        ("Verify a candidate solution of a second-order equation",
         "Differentiate it twice, substitute, and read the residual; say why a "
         "combination `C·cos t + D·sin t` needs two initial values."),
        ("Derive and solve the characteristic equation",
         "Substitute `y = e^(rt)` into `a·y″ + b·y′ + c·y = 0`, obtain "
         "`a·r² + b·r + c = 0`, and solve it exactly, with the discriminant naming "
         "the kind of root."),
        ("Write the general solution for each kind of root",
         "Use two exponentials for distinct real roots, `(C₁ + C₂·t)·e^(rt)` for a "
         "repeated root and a damped cosine and sine for a complex pair, and read "
         "growth, decay or oscillation off the roots."),
        ("Fit the constants and say when the fit is guaranteed",
         "Solve the two-by-two system from `y(0)` and `y′(0)` exactly, and use the "
         "Wronskian at `0` to say when two solutions can fit any starting values."),
        ("Rewrite the equation as a system and step it",
         "Set `x′ = v`, find the trace and determinant that reproduce the "
         "characteristic equation, and compute the exact growth of Euler's method "
         "on `x′ = v, v′ = −x`."),
    ],
    "syllabus_intro": (
        "The course opens with the two functions that make the simplest second-order "
        "equation true, then asks why there are two constants. The characteristic "
        "equation is the centre: one derivation, then the three kinds of root in turn. "
        "Fitting the constants and the Wronskian say how far the answers can be "
        "trusted, and the last two lessons change the point of view from one "
        "equation to a system."
    ),
    "how_to": [
        "Substitute before you trust. Every closed form on this course is checked by "
        "differentiating it twice and putting it into the equation, and the lab prints "
        "the residual, which is exactly zero or it is not. A wrong sign in an exponent "
        "or a missing factor of `t` shows up there at once and does not show up in a "
        "plot.",
        "Do the quadratic by hand first. Read `a`, `b` and `c`, compute `b² − 4ac`, "
        "and say which kind of root to expect before you pick a preset. The lab then "
        "confirms or corrects you, and the discriminant is the one number that decides "
        "which of three forms the solution has.",
        "Fit the constants last, from two numbers. A second-order equation has two "
        "arbitrary constants, and the starting value alone leaves one of them free. "
        "Keep `y(0)` and `y′(0)` apart: the second is the rate of the unknown at the "
        "start, and not the derivative of the first number.",
        "Say which figures are exact. Roots, constants and residuals are exact "
        "fractions or surds. A value of `sin 1`, `cos 1` or `e^(−2)` is irrational, and "
        "is printed rounded, with `≈`, and said to be rounded.",
    ],
    "not_covered": [
        "Equations with a forcing term. This course solves the homogeneous equation "
        "`a·y″ + b·y′ + c·y = 0`; a right-hand side that is not zero belongs to "
        "Oscillators, Damping and Resonance. Variation of parameters, the general "
        "tool when a guess does not work, is named here and not taught.",
        "Variable coefficients. If `a`, `b` or `c` depends on `t`, as in the "
        "Euler&ndash;Cauchy equation `t²·y″ + b·t·y′ + c·y = 0`, then `e^(rt)` is no "
        "longer a solution and the method does not apply. Series solutions and special "
        "functions such as Bessel's are a different subject and are not here.",
        "Proofs of existence and uniqueness. The course uses the fact that two initial "
        "values fix exactly one solution, and the Wronskian lesson shows why for "
        "the cases it builds; it does not prove the general theorem.",
        "Irrational constants. The lab fits the two constants only when the roots are "
        "rational or the complex pair has rational parts, and it refuses the "
        "rest with the reason. That is a limit of the arithmetic, and the method itself "
        "works for any roots.",
        "Equations of third order and higher. The same substitution gives a cubic or "
        "worse characteristic equation, and the Subject stays with second order and "
        "with two-by-two systems, where the trace and determinant are complete.",
    ],
    "footer_lead": (
        "Every root, discriminant, constant, Wronskian and residual on this course is an "
        "exact fraction or an exact symbolic expression, and each solution is checked "
        "by substituting it into the equation. The quotients of `sin` and `cos` and "
        "the values of `e^(rt)` are irrational, so they are printed rounded to six "
        "figures with `≈` and labelled. Euler's columns are exact arithmetic applied "
        "to an approximate method: the fractions are right, and each is only as close "
        "to the true motion as the step allows."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
