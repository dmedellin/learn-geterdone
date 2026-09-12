"""Polynomials and Factoring."""

from . import part_a, part_b

COURSE = {
    "slug": "polynomials-and-factoring",
    "title": "Polynomials and Factoring",
    "level": "Intermediate",
    "summary": (
        "Polynomial arithmetic and the reverse of it: degree and standard form, "
        "the four operations, special products, the standard integer-coefficient "
        "factoring techniques, long and synthetic division, the remainder and "
        "factor theorems, rational roots and polynomial graphs."
    ),
    "blurb": (
        (
        'Multiply out, then learn to go back. The factored form is the one that answers questions &mdash; where a graph crosses, when a product is zero &mdash; and this course is about producing it reliably rather than by inspection.'
    )
    ),
    "key": [
        "(a + b)(a − b) = a² − b²",
        "(a ± b)² = a² ± 2ab + b²",
        "f(c) = 0   ⟺   (x − c) is a factor",
        "root p/q  ⟹  p | a₀  and  q | aₙ",
    ],
    "assumes_short": "Expressions and functions",
    "assumes_long": "exponents, distribution, function notation",
    "outcomes_intro": (
        "By the end you can carry out polynomial arithmetic, factor the standard "
        "integer-coefficient forms over the rationals, and state exactly what a "
        "completed search has and has not ruled out."
    ),
    "outcomes": [
        ("Operate on polynomials",
         "Add, subtract and multiply polynomials of any degree, and recognise the special products on sight rather than expanding them."),
        ("Choose the right factoring technique",
         "Work down a decision list &mdash; common factor, then term count, then pattern "
         "or finite pair search &mdash; and expand the result to verify it."),
        ("Divide polynomials",
         "Carry out long division, use synthetic division where it applies, and read the remainder as a function value."),
        ("Find every rational root",
         "For an integer-coefficient polynomial, generate every candidate from the "
         "constant and leading coefficients, test the list, and distinguish no rational "
         "root from no root at all."),
    ],
    "syllabus_intro": (
        'Definitions, addition, subtraction, multiplication and special products describe polynomials and their operations. Removing the greatest common factor is the first move in a factorisation; grouping, trinomial methods and special forms are branches chosen by term count and pattern. Division and root-finding connect the factors to graph sketches.'
    ),
    "how_to": ["Always look for a common factor first. The lab's decision list starts there because skipping it is what turns a one-line problem into an unfactorable-looking mess.", 'Expand your factored answer to check it. Checking a factorisation by expansion is faster than producing it.', 'After each complete example, cover the answer and do the faded rehearsal on paper. The first decision is supplied; the remaining algebra and the expansion or substitution check are yours before you answer the quiz.'],
    "not_covered": [
        (
            "Factoring quadratics with irrational or complex coefficients. Quadratics and "
            "Complex Numbers teaches the discriminant, the quadratic formula and `i`; this "
            "course stops after proving that no rational factor exists."
        ),
        "A complete factorisation algorithm for arbitrary polynomials of degree 4 or "
        "more. No rational root rules out rational linear factors, but a quartic may "
        "still split into two quadratics.",
        "Numerical root-finding and polynomial interpolation. An irrational root may be "
        "named exactly when its form is already known, but it is not approximated here.",
    ],
    "footer_lead": (
        "Every pair or rational-root search on this course is carried out in exact "
        "arithmetic: the candidate list is generated and each candidate is tested where "
        "you can see it. A negative result is stated only at the scope the search proves "
        "&mdash; no rational linear factor is not the same claim as no factor of any kind."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
