"""Laplace Transforms."""

from . import part_a, part_b

COURSE = {
    "slug": "laplace-transforms",
    "title": "Laplace Transforms",
    "level": "Advanced",
    "summary": (
        "A transform that turns a constant-coefficient differential equation into algebra. "
        "The signal `f(t)` becomes a rational function `F(s)`, a derivative becomes "
        "multiplication by `s` less an initial value, and an initial value problem becomes a "
        "fraction to solve and a table to read backwards. Then partial fractions with exact "
        "coefficients, the poles of a transfer function and what they say about stability, "
        "switched forcing, and one equation solved by two methods, with a third for first "
        "order, that must all agree."
    ),
    "blurb": (
        "Every differential equation so far has been solved in the time domain: guess a form, "
        "match coefficients, then fit the constants to the starting values. The Laplace "
        "transform moves the whole problem to a different variable, `s`, where `y′` becomes "
        "`s·Y − y(0)` and `y″` becomes `s²·Y − s·y(0) − y′(0)`. The equation turns into "
        "`(a·s² + b·s + c)·Y = something`, a line of algebra, and the starting values are "
        "already inside it. What is left is a rational function to take apart into the pieces "
        "of a short table. This course builds the table, proves the derivative rule from the "
        "product rule, solves initial value problems end to end, and then reads what the poles "
        "of the answer say about the long run. Every transform and every coefficient in the "
        "labs is an exact fraction, and every answer is checked by substituting it back."
    ),
    "key": [
        "ℒ[f](s) = ∫₀^∞ e^(−st)·f(t) dt",
        "ℒ[e^(at)] = 1/(s − a)",
        "ℒ[y′] = s·Y − y(0)",
        "(a·s² + b·s + c)·Y = initial terms + ℒ[q]",
        "partial fractions, then the table backwards",
        "poles = characteristic roots",
        "ℒ[u(t − c)·f(t − c)] = e^(−cs)·F(s)",
    ],
    "assumes_short": "Systems and the Phase Plane",
    "assumes_long": (
        "the previous course, Systems and the Phase Plane, for the habit of reading "
        "eigenvalues and roots as the numbers that decide long-run behaviour, together with "
        "Second-Order Linear Equations for the characteristic equation and the fitting of "
        "constants, Accumulation and the Integral for the integral as accumulated change, "
        "and Algebra's Rational and Radical Expressions for adding and reducing "
        "fractions; partial fractions are not assumed, since that course leaves them "
        "out, and are built here from scratch"
    ),
    "outcomes_intro": (
        "By the end you can transform a signal built from powers, exponentials and "
        "sinusoids, solve a constant-coefficient initial value problem by algebra, invert "
        "the answer by partial fractions, and check it by substitution."
    ),
    "outcomes": [
        ("State the transform and compute the first entries of the table",
         "Write the defining integral, compute `ℒ[1]` and `ℒ[e^(at)]` from truncated "
         "integrals, and say for which `s` each result holds."),
        ("Transform a signal with linearity and the table",
         "Split a signal into table entries, scale and add their transforms, and combine the "
         "result into one fraction in lowest terms."),
        ("Apply the derivative rule",
         "Write `ℒ[y′]` and `ℒ[y″]` with their initial values, and verify the rule on a "
         "signal by transforming its derivative directly."),
        ("Solve an initial value problem by algebra",
         "Transform both sides, solve for `Y(s)`, invert through partial fractions and verify "
         "the result by substitution."),
        ("Decompose a rational function exactly",
         "Handle linear, repeated and irreducible quadratic factors and invert each piece."),
        ("Read stability and switched forcing from the transform",
         "Identify poles with characteristic roots, state the stability criterion, and "
         "solve an equation whose forcing switches on at a stated time."),
    ],
    "syllabus_intro": (
        "The transform first, because everything else is a use of it: its definition, "
        "its table and its rule for derivatives. Solving comes next, as one procedure and "
        "then as the two pieces of it that need care, the partial fractions and the poles. "
        "The course ends with forcing that switches on at a time, and with one equation "
        "solved by two methods that have to agree."
    ),
    "how_to": [
        "Keep the two variables apart. A signal lives in `t`, its transform lives in `s`, "
        "and a figure belongs to one of them. The labs print the transform as a fraction in "
        "`s` and the solution as a sum of exponentials in `t`, and the status line says "
        "which is which.",
        "Check every answer by substitution. The lab reports the residual of its solution in "
        "the original equation, and `residual 0` is the claim that the algebra and the "
        "inversion were both right. Do the same check by hand on one preset in each lesson.",
        "Do the algebra before reading the lab. The transformed equation, `Y(s)` and the "
        "partial fractions are all short enough to write out, and a lab that agrees with "
        "your line is worth more than one you copied from.",
        "Say which figures are exact. The transforms, the coefficients and the poles are exact "
        "fractions or exact surd-free roots. The truncated integrals that the first lesson "
        "shows are rounded and printed with `≈`, because they are evidence for a claim and "
        "not the claim.",
    ],
    "not_covered": [
        "The Dirac delta, which needs distributions, and the convolution theorem. Both are "
        "standard in a full treatment of the transform; here the forcing is a polynomial, an "
        "exponential, a sinusoid or a switch, and the response to an impulse is not "
        "needed.",
        "Transforms of periodic functions, the inversion integral and the region of "
        "convergence as a theory. The lessons state the half-line of `s` where each integral "
        "converges and use it; they do not develop the complex analysis that explains it.",
        "Irrational frequencies. A denominator such as `s² + 2` has the pole pair `±i√2`, and "
        "its inverse has `cos(√2·t)` in it. The lab refuses that case and names the factor "
        "rather than print a surd inside a cosine.",
        "Systems of equations by transform. The previous course solves them with "
        "eigenvalues and eigenvectors, and the transform here is applied to a single "
        "equation of first or second order.",
        "Equations with variable coefficients, where the transform gives a differential "
        "equation in `s` and not an algebraic one. The method works because the "
        "coefficients are constant.",
    ],
    "footer_lead": (
        "Every transform, partial-fraction coefficient, pole and constant on this course is an "
        "exact fraction or an exact root, and each solution is checked by substituting it into "
        "the original equation and reading the residual. The only rounded figures are the "
        "truncated integrals in the first lesson and any value of an exponential, and each is "
        "printed with `≈`. A numerical solution is exact arithmetic applied to an approximate "
        "method; the transform solutions here are different in kind, since they are closed "
        "forms, and they are checked as closed forms."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
