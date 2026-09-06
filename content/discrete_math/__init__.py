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
        'The mathematics of things you can count, list and check: statements that are true or false, sets and the relations between them, proof by induction, counting without enumerating, probability over finite outcomes, the arithmetic of remainders, graphs, and the analysis of the algorithms that run on all of it. Eight courses and 106 lessons are available.'
    ),
    "description": (
        'The Discrete Mathematics Subject offers eight courses covering propositional logic and proof, sets, relations and functions, induction and recursion, combinatorics, discrete probability, number theory and cryptography, graphs and trees, and the analysis of algorithms. All eight courses and 106 lessons are available. Every lesson is one self-contained page whose figures are computed in your browser.'
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
        'Induction and Recursion proves things about the sets described in Sets, Relations, and Functions. Discrete Probability uses the outcome-counting techniques of Combinatorics and Counting. Algorithms and Complexity analyses structures described in Graphs and Trees.'
    ),
    "why_order": ['Logic provides the precision needed to state a claim as true or false. A reader who has not settled what `∀x ∃y P(x, y)` means can silently misread theorems throughout these courses.', 'Sets, relations and functions provide the vocabulary. Equivalence relations, bijections and partial orders recur across these courses; their definitions are developed in Sets, Relations, and Functions.', 'Induction is a proof technique used throughout this Subject. Counting arguments, recurrence solutions, graph theorems and algorithm correctness are all induction wearing different clothes.', 'Counting, probability and number theory apply that machinery to three specific worlds, and graphs give it an object to act on. Algorithms and Complexity uses recurrences from Induction and Recursion, counting from Combinatorics and Counting, and graphs from Graphs and Trees.'],
    "prerequisites": ['School algebra, and nothing beyond it. You need to be comfortable rearranging an equation, working with exponents, and reading summation notation &mdash; the lessons that use `Σ` explain it where it appears.', 'No calculus. Nothing in this Subject takes a limit, a derivative or an integral. Where a growth rate is compared to another, it is compared by an explicit constant and threshold rather than by a limit.', 'No programming. Algorithms and Complexity reads pseudocode and Number Theory and Cryptography walks through algorithms step by step, but nothing asks you to write or run code. The labs execute in your browser so that you can watch an algorithm rather than implement it.', 'Patience with definitions. The single largest difficulty in this subject is that its words are used precisely: <em>or</em> is inclusive, <em>some</em> means at least one, and a <em>graph</em> is not a plot. Every one of those is stated where it first matters.'],
    # The hazard of learning THIS subject from interactive examples: a widget
    # that checks a claim for n = 1..40 has demonstrated nothing about n = 41,
    # and course 3 is about exactly that.
    "material": (
        "every figure is computed in your browser from the stated definition, "
        "and a worked example is not a proof."
    ),
    "footer_lead": (
        '<strong>Educational course material.</strong> Every figure in this Subject is computed in your browser from the definition the lesson states &mdash; the counting is done in exact integer arithmetic and the probabilities as exact fractions, so the numbers are not approximations. What the labs cannot do is prove anything: checking a statement for the cases on screen is evidence about those cases and nothing more, which is the subject of Induction and Recursion.'
    ),
    "courses": COURSES,
}
