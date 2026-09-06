"""The Discrete Mathematics path, as data.

Eight courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.
"""

from . import (
    c1_logic,
    c2_sets,
    c3_induction,
    c4_counting,
    c5_probability,
    c6_number_theory,
    c7_graphs,
    c8_algorithms,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_logic.COURSE,
    c2_sets.COURSE,
    c3_induction.COURSE,
    c4_counting.COURSE,
    c5_probability.COURSE,
    c6_number_theory.COURSE,
    c7_graphs.COURSE,
    c8_algorithms.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "discrete-math",
    "title": "Discrete Mathematics",
    "level": "Beginner → Advanced",
    "level_note": "no calculus required",
    "tagline": (
        "Logic, proof, sets, relations, functions, induction, counting, discrete probability, number theory, graphs, and algorithm analysis."
    ),
    "description": (
        "Discrete Mathematics courses with definitions, proofs, worked examples, practice questions, and interactive tools for logic, counting, number theory, graphs, and algorithms."
    ),
    "key": [
        "∀n ∈ ℕ.  P(n)          proved by induction, not by checking",
        "|A ∪ B| = |A| + |B| − |A ∩ B|",
        "C(n, k) = n! / (k!(n−k)!)",
        "gcd(a, b) = ax + by          for some integers x, y",
        "Σ deg(v) = 2|E|",
        "T(n) = 2T(n/2) + n  ⟹  T(n) = Θ(n log n)",
    ],
    "sequence_intro": (
        "Choose a course by topic. Each course lists recommended background and its lessons."
    ),
    "why_order": [
    "Logic and proof provide methods for stating and checking mathematical arguments. Sets, relations, and functions describe the objects those arguments concern.",
    "Induction and recursion connect definitions, proofs, and algorithms. Counting supports discrete probability; divisibility and modular arithmetic support number theory.",
    "Graphs represent relationships and support traversal, optimization, and structural analysis. Algorithm analysis uses counting, recurrences, and proofs to study running time and correctness."
],
    "prerequisites": [
    "School algebra, including rearranging equations and working with exponents, is useful.",
    "Logic and Proof introduces the logical notation and proof techniques used across these courses. Individual courses list more specific recommended background.",
    "No calculus or programming is required to use the interactive tools."
],
    # The hazard of learning THIS subject from interactive examples: a widget
    # that checks a claim for n = 1..40 has demonstrated nothing about n = 41,
    # and course 3 is about exactly that.
    "material": (
        "every figure is computed in your browser from the stated definition, "
        "and a worked example is not a proof."
    ),
    "footer_lead": (
        "Discrete Mathematics definitions, proofs, examples, and interactive calculations."
    ),
    "courses": COURSES,
}
