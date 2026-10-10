"""Accumulation and the Integral."""

from . import part_a, part_b


COURSE = {
    "slug": "accumulation-and-the-integral",
    "title": "Accumulation and the Integral",
    "level": "Intermediate",
    "summary": (
        "Total change as a sum of rate times step: left, right, trapezoid and midpoint sums as exact fractions, the way refining them closes in on a number, the antiderivative and the fundamental theorem as a demonstrated claim, the constant fixed by an initial value, the integral sign and its rules, and the integral of 1/t."
    ),
    "blurb": (
        "An integral is accumulated change. This course adds up a rate piece by piece in exact fractions, watches the sums close in on a number, and then shows that reversing the power rule finds that number without any sum. The one constant that reversal leaves open is the reason an equation later needs an initial value."
    ),
    "key": [
        "total change ≈ Σ (rate · width)",
        "Rₙ − Lₙ = h·(f(b) − f(a))",
        "Tₙ = (Lₙ + Rₙ)/2, Mₙ from midpoint rates",
        "∫ₐᵇ f(t) dt = F(b) − F(a)",
        "y = F(t) + C    one value fixes C",
        "∫₁ˣ dt/t = ln x    not a fraction",
    ],
    "assumes_short": "Rates of change and the derivative",
    "assumes_long": "the derivative and the power rule from Rates of Change and the Derivative, and fractions",
    "outcomes_intro": (
        "By the end you can estimate a total change from a rate with exact sums, "
        "bracket it, find it by an antiderivative, and say what each of those "
        "claims and what it only demonstrates."
    ),
    "outcomes": [
        ("Compute total change from a rate",
         "Cut an interval into equal pieces, add rate times width exactly, and state "
         "what the sum assumed about the rate inside each piece."),
        ("Bracket and refine a total",
         "Compute left and right sums, predict their gap, and double the pieces to "
         "watch the error and its exact ratio."),
        ("Compare four rules",
         "Compute trapezoid and midpoint sums, find their exact errors, and show "
         "the error quartering on a quadratic."),
        ("Find a total by antiderivative",
         "Reverse the power rule, evaluate `F(b) − F(a)` exactly, and fix the "
         "constant from one given value."),
        ("Read and use the integral sign",
         "Say `∫ₐᵇ f(t) dt` aloud, and check linearity and additivity by computing "
         "both sides exactly."),
        ("Bracket an integral that is not a fraction",
         "Sum `1/t` exactly, trap the total between the left and right sums, and "
         "quote it rounded and labelled rather than as a fraction."),
    ],
    "syllabus_intro": (
        "Adding up a rate comes first: sums, their gap, their refinement and the "
        "better rules. The exact total follows, by antiderivative and by a constant "
        "fixed from one value. The last two lessons give the notation and the one "
        "integral that no fraction equals."
    ),
    "how_to": [
        "Compute the first sum of each lesson by hand before reading the lab's "
        "figure. The sums are short, and doing one yourself makes the table a check "
        "and not a surprise.",
        "Keep what a table shows apart from what it proves. Several lessons here "
        "state a claim, demonstrate it on exact fractions, and say plainly that the "
        "demonstration is not a proof for every case.",
        "After each worked example, cover it and finish the faded rehearsal beneath "
        "it before opening the quiz. Change the rate in the lab and predict the "
        "sign of the error before you look.",
    ],
    "not_covered": [
        "The theory of the integral. There is no definition by limits of arbitrary "
        "partitions, no test for which rates have an integral, and no proof that the "
        "sums converge; the sums are shown approaching a number and the fundamental "
        "theorem is stated as the claim they support. A first analysis course is where "
        "that is done.",
        "Techniques of integration for general functions. Integration by parts, "
        "substitution, trigonometric substitution and integrating rational functions "
        "by partial fractions are left out; the Subject needs polynomials and `1/t` "
        "and nothing else.",
        "Improper integrals, integrals over infinite intervals, and areas between "
        "curves. Totals here are signed accumulations of a rate over a finite interval.",
        "Numerical integration as a subject. Adaptive step size, Simpson's rule and "
        "error estimators are not here; the four rules and their exact errors on "
        "polynomials are the whole of it.",
    ],
    "footer_lead": (
        "Every sum on this course is computed in your browser as an exact fraction, "
        "from the rate the lesson states. A sum is an estimate of a total and is "
        "labelled as one; where a total is irrational, as for the integral of `1/t`, "
        "it is printed with a rounding label and never as a bare decimal."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
