"""Sequences and Series."""


from . import part_a, part_b


COURSE = {
    "slug": "sequences-and-series",
    "title": "Sequences and Series",
    "level": "Intermediate → Advanced",
    "summary": (
        "Ordered lists and the sums of their terms: recursive and closed forms, sigma notation, arithmetic and geometric families, partial sums, infinite geometric series and when they converge, repeating decimals, annuities, Pascal's triangle and the binomial theorem."
    ),
    "blurb": (
        "A sequence is a function whose input is a position. Arithmetic and geometric "
        "families make that idea calculable: both have closed forms for a term and a "
        "finite sum, some geometric sums have a limit, and the same indexed notation "
        "leads to Pascal's triangle and binomial expansion."
    ),
    "key": [
        "aₙ = a₁ + (n − 1)d          aₙ = a₁rⁿ⁻¹",
        "Sₙ = n(a₁ + aₙ)/2           Sₙ = a₁(1 − rⁿ)/(1 − r)",
        "S∞ = a₁/(1 − r)      a₁ ≠ 0 needs |r| < 1; the zero series sums to 0",
        "(a + b)ⁿ = Σ C(n,k) aⁿ⁻ᵏ bᵏ",
    ],
    "assumes_short": "Courses 1\u20137",
    "assumes_long": "exponents, functions, and exact fractions",
    "outcomes_intro": (
        "By the end you can generate and classify sequences, compute finite and infinite "
        "geometric sums under their conditions, apply them to decimals and payments, "
        "and construct the coefficients and terms of a binomial expansion."
    ),
    "outcomes": [
        ("Generate, classify and sum sequences",
         "Run an explicit or recursive definition, re-index a finite sum, distinguish "
         "arithmetic from geometric data, and derive the appropriate term and finite-sum formula."),
        ("Decide and apply geometric convergence",
         "Use the sequence of partial sums and `|r| < 1` under the nonzero-first-term "
         "condition, quantify the remaining gap, and convert a repeating decimal to an exact fraction."),
        ("Value a stream of payments",
         "Place every ordinary-annuity payment on one timeline, then compute and check "
         "its accumulated value, present value or perpetuity value with rate and period in the same units."),
        ("Construct and use binomial coefficients",
         "Build and check a row of Pascal's triangle, expand a signed binomial power, "
         "and isolate a requested term by solving its exponent equation for an admissible `k`."),
    ],
    "syllabus_intro": (
        "Lessons 1 and 2 generate sequences and encode finite sums. Lessons 3 to 5 "
        "classify the two standard families and recover or telescope partial sums. "
        "Lessons 6 to 8 decide geometric convergence and apply it to decimals and "
        "payment streams; lessons 9 to 11 construct and use binomial coefficients."
    ),
    "how_to": [
        "After studying each complete worked example, cover it and finish the faded "
        "rehearsal beneath it before opening the quiz. The first strategic decision is "
        "supplied; the remaining terms, algebra and independent check are yours.",
        "Add the first several terms by hand before using a sum formula. The sequence "
        "labs compare a direct construction with the relevant closed form, while the "
        "Pascal and binomial labs make their own independent checks visible.",
        "Take the `|r| < 1` condition seriously in lesson 6. The formula returns a number for `r = 2` as happily as for `r = 1/2`, and that number is meaningless.",
        "Build Pascal's triangle by hand once, at least to row 6. Lesson 10 is much easier for anyone who has seen the coefficients appear before being given a formula for computing one directly.",
    ],
    "not_covered": [
        "Convergence tests for series in general. Only the geometric case is settled here, and it is settled completely; the rest belongs to calculus.",
        "Sequences of functions, power series and Taylor series.",
        "Mathematical induction as a proof technique. Several formulas on this course are proved by other means and stated as proved by induction elsewhere; the Discrete Mathematics path devotes a course to it.",
    ],
    "footer_lead": (
        "Every sum on this course is computed twice &mdash; once by adding the terms up and once by the closed form &mdash; and both are printed, so the formula arrives as something checked rather than something asserted. Terms and sums are exact fractions; where an infinite sum exists the lab shows the partial sums approaching it rather than jumping to the answer."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
