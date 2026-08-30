"""Rational and Radical Expressions."""

from . import part_a, part_b

COURSE = {
    "slug": "rational-and-radical-expressions",
    "title": "Rational and Radical Expressions",
    "level": "Intermediate",
    "summary": (
        "Algebraic fractions and roots: domains and the values that break them, simplifying and operating on rational expressions, complex fractions, rational equations and the extraneous solutions they produce, asymptotes, radical arithmetic and radical equations."
    ),
    "blurb": (
        "What happens when a variable lands in a denominator or under a root. Both put values out of bounds, both create solutions that are not solutions, and both need the domain written down before the algebra starts."
    ),
    "key": [
        "a/b · c/d = ac/bd        a/b ÷ c/d = a/b · d/c",
        "x = 2 makes (x² − 4)/(x − 2) undefined, not 4",
        "squaring both sides can INVENT a solution",
        "degree of top vs bottom  ⟹  the horizontal asymptote",
    ],
    "assumes_short": "Courses 1–4",
    "assumes_long": "factoring, domain inequalities, and function notation",
    "outcomes_intro": (
        "By the end you can handle an expression with a variable in a denominator or under a root without losing the values that were never allowed."
    ),
    "outcomes": [
        ("State the domain first",
         "Find every value that makes a denominator zero or an even-index radicand negative, and record the resulting restrictions before simplifying rather than after."),
        ("Simplify and combine exact expressions",
         "Cancel only common FACTORS, build a least common denominator, reduce a complex fraction two ways, extract perfect powers, combine like radicals and rationalize the numerical denominators taught here."),
        ("Solve and then check",
         "Clear denominators or square both sides, solve, and test every candidate against the original &mdash; because both moves can create solutions that are not ones."),
        ("Read domains and graphs",
         "Locate rational-function asymptotes and holes from factored form, then solve an even-root inequality and use its boundaries and range to sketch a radical function."),
    ],
    "syllabus_intro": (
        "Lessons 1 to 7 are rational expressions, equations and graphs; lessons 8 to 12 are radicals, from simplification to radical functions."
    ),
    "how_to": [
        "Factor everything before you do anything else. Every technique in the first half is stated in terms of factors, and none of them applies to a sum.",
        "Write the excluded values down at the top of the page, before you start. They are not recoverable from your simplified answer &mdash; that is the whole point of lesson 1.",
        "After each complete example, cover its answer and do the faded rehearsal before the quiz. The first strategic move is supplied; the remaining algebra, restrictions and original-expression check are yours. In lessons 6 and 11 that check is part of the method, because a legal step can create an extraneous candidate.",
    ],
    "not_covered": [
        "Partial fractions, which are a technique for integration and belong to calculus.",
        "Oblique and curvilinear asymptotes beyond a brief mention where long division makes one visible.",
        "Radicals of complex numbers, and roots of negative numbers generally. Course 6 introduces `i`; here `sqrt(-4)` is outside the domain and is treated as such.",
    ],
    "footer_lead": (
        "Domains, asymptotes and holes on this course are computed from the factored form in exact arithmetic, and every solution a lab reports has been substituted back into the ORIGINAL equation in front of you. An extraneous root is shown failing that check rather than quietly dropped."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
