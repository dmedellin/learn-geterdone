"""Course 6 -- System Considerations: Part VI of Code Complete, Chapters 27-30.

Four lessons, one per chapter: program size, managing construction,
integration and programming tools. The labs are the kit's family 2 and 3
views: the arithmetic of the book's size and effort tables, and the stubs,
drivers and rebuilds a stated dependency list implies. See
docs/code-complete/PLAN.md, section C, Course 6.
"""

from . import part_a

COURSE = {
    "slug": "code-complete-system-considerations",
    "title": "System Considerations",
    "level": "Intermediate",
    "summary": (
        "Part VI of <em>Code Complete</em>, Chapters 27 to 30: How Program Size Affects "
        "Construction; Managing Construction; Integration; and Programming Tools. The view "
        "widens from the routine to the project. Count the communication paths in a team and "
        "the defects and staff-years the book's tables give for a size, multiply a nominal "
        "estimate by the book's effort factors, count the stubs and drivers an integration "
        "order needs, and find what a build tool rebuilds when one file changes."
    ),
    "blurb": (
        "Read the four chapters on the project around the code. Count how communication grows "
        "with a team, work the book's size and effort tables into ranges, count the "
        "scaffolding an integration order costs, and trace a change through a build."
    ),
    "key": [
        "paths among n people: n·(n − 1)/2",
        "defects = size in KLOC × errors per KLOC",
        "effort = nominal × each factor",
        "stub: called before it is integrated",
        "driver: integrated before any caller",
        "a build redoes what depends on the change",
        "the rates are averages from other projects",
    ],
    "assumes_short": "Laying the Foundation",
    "assumes_long": (
        "Laying the Foundation, for the kinds of project and the cost of a late fix; the "
        "courses on classes, statements and testing help but are not needed, and the arithmetic "
        "is a product, a quotient and a count"
    ),
    "outcomes_intro": (
        "By the end you can do the arithmetic each chapter does with its figures, and say what "
        "the result is evidence of and what it is not."
    ),
    "outcomes": [
        ("Count a team's communication paths",
         "Compute the paths among n people as n·(n − 1)/2, and say how they grow when a team "
         "doubles."),
        ("Work the book's size tables into ranges",
         "For a size in thousands of lines, choose the rows of Tables 27-1 and 27-2, compute the "
         "range of defects and staff-years they give, and the ratio of the range's ends."),
        ("Adjust an estimate by effort factors",
         "Turn the book's percentages from Table 28-1 into multipliers, multiply them into a "
         "nominal estimate, and state the range the factors span."),
        ("Count the scaffolding of an integration order",
         "From a list of who calls whom and an order, list the components that need a stub and "
         "those that need a driver."),
        ("Trace a change through a build",
         "From a make-style list of targets and prerequisites, list what a change to one file "
         "rebuilds, directly and in all."),
    ],
    "syllabus_intro": (
        "Four lessons, one per chapter, in the book's order: how size changes a project, how "
        "construction is managed and estimated, the order in which a system is put together, "
        "and the tools that do part of the work."
    ),
    "how_to": [
        "This course is for anyone who works on a team, or will. It reads McConnell's "
        "<em>Code Complete</em>, 2nd edition (Microsoft Press, 2004), Part VI, with code and "
        "build lists written for these lessons; section numbers and pages are that edition's. "
        "Read each chapter in your own copy first: every lesson names the sections it covers "
        "and the pages they start on.",
        "Most of the figures here are the book's quotations of industry averages: Jones on "
        "defect density, Boehm's Cocomo II on effort factors, Putnam and others on productivity. "
        "Each is marked with its source the first time it appears. They are averages over other "
        "people's projects, mostly from before 2004, and your own records are the test of them.",
        "The labs do arithmetic you could do by hand, on figures the lesson states. Change the "
        "inputs to your own team, size or build and look at what moves; a range that is an order "
        "of magnitude wide is the honest result, not a failure of the lab.",
        "Each lesson ends with an exercise and a last step that sends you to your own team, "
        "estimate, call graph or build. Do the exercise by hand before you check it in the lab.",
    ],
    "not_covered": [
        "Estimation as a discipline. Chapter 28 points to whole books on it, among them "
        "McConnell's own later work; the lesson does only the chapter's arithmetic with Table "
        "28-1, and does not teach Cocomo II's size equation.",
        "The book's tables and checklists. Table 27-1, Table 27-2 and Table 28-1 are used a few "
        "figures at a time, with their sources; the configuration-management, integration and "
        "tools checklists are named and not reproduced.",
        "Version-control and build practice since 2004: distributed version control, pull "
        "requests, build systems that cache by content, and continuous delivery. Programming "
        "Tools says in one paragraph where today's practice differs; the course does not teach "
        "it.",
        "Process methodologies. Scrum, Extreme Programming and the rest are named where the book "
        "names them, in Chapter 27's pages on methodology and size; none is taught.",
        "Named products. Chapter 30 surveys kinds of tools rather than brands, and so does the "
        "lesson; make and ant are named because the book names them.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "communication paths as n·(n − 1)/2, a defect range as a size times the book's densities, "
        "an adjusted estimate as a product of multipliers, stubs and drivers by walking an order "
        "through a call list, and a rebuild by following a dependency list. The densities, "
        "productivities and effort factors are the book's quotations of other people's averages, "
        "marked with their sources; the lab cannot say what your project will see."
    ),
    "lessons": part_a.LESSONS,
}
