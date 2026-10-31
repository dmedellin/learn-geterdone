"""The Introduction to Algorithms path, as data: a read-along of Cormen,
Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd edition (MIT
Press, 2009).

Eight courses that follow the book's Parts I to VII (Part VII in two). Each
lesson sets out a chapter's argument in its own words and runs the algorithm on
an instance written for the lesson, counting what the chapter analyses. The
content lives here and only here; scripts/ turns it into pages. The design is
docs/intro-algorithms/PLAN.md.
"""

from . import (
    c1_foundations,
    c2_sorting,
    c3_data_structures,
    c4_design_techniques,
    c5_advanced_structures,
    c6_graphs,
    c7_algebraic_topics,
    c8_strings_geometry_hardness,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_foundations.COURSE,
    c2_sorting.COURSE,
    c3_data_structures.COURSE,
    c4_design_techniques.COURSE,
    c5_advanced_structures.COURSE,
    c6_graphs.COURSE,
    c7_algebraic_topics.COURSE,
    c8_strings_geometry_hardness.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "intro-algorithms",
    "title": "Introduction to Algorithms, Read Along",
    "level": "Intermediate → Advanced",
    "level_note": "you can program, and you know induction, sums and logarithms",
    # Course 1's author completes the fields below from PLAN section A.
    "tagline": "TODO",
    "description": "TODO",
    "key": ["TODO"],
    "sequence_intro": "TODO",
    "why_order": ["TODO"],
    "prerequisites": ["TODO"],
    "material": (
        "every count on this path is produced by running the algorithm in your browser on the instance a lesson states, and a count on one instance is evidence about that instance &mdash; the bound the book proves holds for every input, and only its proof establishes that."
    ),
    "footer_lead": "TODO",
    "courses": COURSES,
}
