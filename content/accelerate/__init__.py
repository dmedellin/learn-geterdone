"""The Accelerate path, as data: a read-along of Nicole Forsgren, Jez Humble
and Gene Kim's Accelerate: The Science of Lean Software and DevOps (IT
Revolution, 2018).

Eight courses that follow the book's three parts, sixteen chapters,
conclusion and appendices, one lesson per section or group of sections. Each
lesson sets out what the research found and how it was measured, and
recomputes one kind of figure the researchers computed on a small sample
written for the lesson. The content lives here and only here; scripts/ turns
it into pages. The design is docs/accelerate/PLAN.md.
"""

from . import (
    c1_measuring_performance,
    c2_culture,
    c3_technical_practices,
    c4_lean_management,
    c5_people,
    c6_the_science,
    c7_surveys_and_data,
    c8_transformation,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_measuring_performance.COURSE,
    c2_culture.COURSE,
    c3_technical_practices.COURSE,
    c4_lean_management.COURSE,
    c5_people.COURSE,
    c6_the_science.COURSE,
    c7_surveys_and_data.COURSE,
    c8_transformation.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

# Course 1's author completes this from docs/accelerate/PLAN.md section A,
# field for field as content/domain_driven_design/__init__.py.
PATH = {
    "slug": "accelerate",
    "title": "Accelerate, Read Along",
    "level": "Introductory",
    "level_note": "you have worked on, with or near a team that builds and runs software",
    # Backtick runs, key lines and worked lines are read by the code dialect
    # (speech.say_code), as on the other software read-alongs.
    "speech": "code",
    "material": (
        "every figure on this path is computed in your browser from the small sample a lesson states &mdash; its log, its answers, its teams &mdash; and shows what one measure says about that sample; it is not a finding about any team or organization, and a correlation in it is not a cause."
    ),
    "courses": COURSES,
}
