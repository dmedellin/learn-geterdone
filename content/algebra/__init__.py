"""The Algebra path, as data.

Nine courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.
"""

from . import (
    c1_foundations,
    c2_equations,
    c3_functions,
    c4_polynomials,
    c5_rational,
    c6_quadratics,
    c7_exponentials,
    c8_systems,
    c9_sequences,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_foundations.COURSE,
    c2_equations.COURSE,
    c3_functions.COURSE,
    c4_polynomials.COURSE,
    c5_rational.COURSE,
    c6_quadratics.COURSE,
    c7_exponentials.COURSE,
    c8_systems.COURSE,
    c9_sequences.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "algebra",
    "title": "Algebra",
    "level": "Beginner → Advanced",
    "level_note": "arithmetic with fractions and negative numbers",
    "tagline": (
        "Expressions, equations, functions, polynomials, rational and radical expressions, quadratics, complex numbers, exponentials, logarithms, systems, matrices, sequences, and series."
    ),
    "description": (
        "Algebra courses with explanations, worked examples, practice questions, and interactive tools for expressions, equations, functions, systems, matrices, sequences, and series."
    ),
    "key": [
        "a(b + c) = ab + ac              the law behind almost every rearrangement",
        "x = (−b ± √(b² − 4ac)) / 2a",
        "f(c) = 0   ⟺   (x − c) is a factor of f",
        "log_b(x) = y   ⟺   b^y = x",
        "aₙ = a₁r^(n−1)                  Sₙ = a₁(1 − rⁿ)/(1 − r)",
    ],
    "sequence_intro": (
        "Choose a course by topic. Each course lists recommended background and its lessons."
    ),
    "why_order": [
    "Expressions and equations describe quantities and relationships. Function notation and graphs connect those relationships to their inputs and outputs.",
    "Factoring supports rational expressions, quadratics, and polynomial graphs. Exponentials and logarithms describe constant-ratio change and its inverse.",
    "Systems and matrices describe simultaneous constraints. Sequences and series describe indexed terms and their sums."
],
    "prerequisites": [
    "Arithmetic with fractions and negative numbers is useful throughout these courses.",
    "Foundations of Algebra introduces variables and algebraic notation. Individual courses list more specific recommended background.",
    "The interactive tools require no programming. Calculus and trigonometry are not required."
],
    # The hazard of learning THIS subject from interactive examples is not the
    # same one. Algebra's characteristic error is the invented law -- cancelling
    # a term rather than a factor, log(M + N), (a + b)^2 = a^2 + b^2 -- and each
    # of those gives the right answer on SOME example. Watching a step work is
    # therefore not evidence that the step is a rule.
    "material": (
        "every figure is computed in your browser from the stated definition, "
        "and a step that gives the right answer here is not thereby a valid rule."
    ),
    "footer_lead": (
        "Algebra explanations, worked examples, practice questions, and interactive calculations."
    ),
    "courses": COURSES,
}
