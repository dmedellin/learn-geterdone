"""The Enterprise Application Patterns path, as data: a read-along of Fowler's
Patterns of Enterprise Application Architecture (Addison-Wesley, 2002).

Seven courses that follow the book's eight narrative chapters, each lesson read
with the Part 2 patterns its narrative introduces. Each lesson sets out the
argument in its own words, shows the pattern in a short piece of Java written
for this Subject, and counts its trade-off on a stated situation in the lab.
The content lives here and only here; scripts/ turns it into pages. The design
is docs/enterprise-patterns/PLAN.md.
"""

from . import (
    c1_layers_and_performance,
    c2_domain_logic,
    c3_data_source,
    c4_objects_and_tables,
    c5_web_presentation,
    c6_concurrency_and_session_state,
    c7_distribution,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_layers_and_performance.COURSE,
    c2_domain_logic.COURSE,
    c3_data_source.COURSE,
    c4_objects_and_tables.COURSE,
    c5_web_presentation.COURSE,
    c6_concurrency_and_session_state.COURSE,
    c7_distribution.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

# PATH: the Course 1 author fills every field from PLAN.md §A (slug, title,
# level, level_note, speech, tagline, description, key, sequence_intro,
# why_order, prerequisites, material, footer_lead), mirroring
# content/code_complete/__init__.py field for field.
PATH = {
    "slug": "enterprise-patterns",
    "title": "Patterns of Enterprise Application Architecture, Read Along",
    "speech": "code",
    "courses": COURSES,
}
