"""Course 2 -- Creating High-Quality Code: Part II of Code Complete, Chapters 5-9.

Nine lessons in five modules: part_a reads Chapters 5 and 6 (design and
classes), part_b Chapters 7, 8 and 9 (routines, defensive programming and the
Pseudocode Programming Process). Page references are to McConnell, Code
Complete, 2nd ed. (Microsoft Press, 2004). The design is
docs/code-complete/PLAN.md, section C, Course 2.
"""

from . import part_a, part_b

COURSE = {
    "slug": "code-complete-high-quality-code",
    "title": "Creating High-Quality Code",
    "level": "Beginner",
    "summary": (
        "Part II of the book, Chapters 5 to 9: Design in Construction; Working Classes; "
        "High-Quality Routines; Defensive Programming; and The Pseudocode Programming "
        "Process. McConnell's one idea runs through all five: managing complexity is "
        "software's primary technical imperative. Each lesson sets out a chapter's "
        "argument, section by section, and then counts what the chapter says to count on "
        "a design, a class or a routine written for the lesson: connected pairs and fan-in, "
        "who knows a secret, fields and public routines, the depth of a hierarchy, repeated "
        "blocks, lines and parameters, where an input check is wrong, which values cross a "
        "barricade unchecked, and which pseudocode steps have no code beneath them."
    ),
    "blurb": (
        "Read Part II a half-chapter at a time, from design to the routine. Count the "
        "connections in a design and who knows its secrets, measure a class's interface "
        "and an inheritance chain, find a routine's repeated block and regroup its "
        "parameters, test an input check at its boundaries, place values on either side of "
        "a barricade, and check a routine against its own pseudocode."
    ),
    "key": [
        "manage complexity first",
        "ask what each module should hide",
        "one class, one abstraction",
        "contain before you inherit",
        "a routine does one thing, named fully",
        "handle expected errors, assert the rest",
        "write the steps first, then the code",
    ],
    "assumes_short": "Laying the Foundation",
    "assumes_long": (
        "Laying the Foundation, for what construction is and why a late fix costs more; "
        "the code is short Java, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can do, on a small design, class or routine, the counts these "
        "chapters ask for, and say in the chapters' terms what each count shows and what it "
        "leaves to you."
    ),
    "outcomes": [
        ("Count a design's connections and secrets",
         "Compute the possible and connected pairs and the largest fan-in of a set of "
         "modules, name a design's secret, and count the modules whose code knows it with "
         "the secret exposed and hidden."),
        ("Read a class's interface and hierarchy",
         "Count a class's fields, public data and public routines, group its routines by "
         "the abstraction each serves, compute an inheritance hierarchy's depth, and say "
         "whether a subclass can stand in for its parent."),
        ("Judge a routine's purpose and shape",
         "Name a routine's cohesion by Chapter 7's kinds, find a repeated block and write "
         "the routine that replaces it, and count a routine's lines and parameters against "
         "the book's figures."),
        ("Place a check where it belongs",
         "Find where an input check is wrong from its comparisons and connective, and "
         "decide by the barricade rule whether a value gets error handling or an "
         "assertion."),
        ("Check a routine against its pseudocode",
         "List the steps of a routine written by the Pseudocode Programming Process, find a "
         "step with no code beneath it, and say whether the obvious fix is right in Java."),
    ],
    "syllabus_intro": (
        "Nine lessons follow Part II in the book's order: two on Chapter 5, design; two on "
        "Chapter 6, classes; two on Chapter 7, routines; two on Chapter 8, defensive "
        "programming; and one on Chapter 9, the Pseudocode Programming Process."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Steve McConnell's "
        "<em>Code Complete</em>, 2nd edition (Microsoft Press, 2004), Part II. Each lesson "
        "names its sections and pages, opens with at most one short quotation, and sets "
        "out the argument in its own words; the book's own examples, listings and "
        "checklists are better read in the book. The code in every lesson is written for "
        "it, and section numbers are that edition's.",
        "Hold one idea throughout. Chapter 5 argues that managing complexity is "
        "software's primary technical imperative (p. 78), and the rest of Part II applies "
        "it to classes, routines and checks. Every count in this course is a way of seeing "
        "complexity: how many places a change can reach, how much a reader must hold in "
        "mind, how many promises a routine has not yet kept.",
        "Treat each count as a reason to look. The labs read the code or the structure "
        "you give them and count by the rules stated beside them. A count of nine fields "
        "or seven levels does not make a class bad; it tells you where to read. Each lab "
        "also names what it cannot see, and that is usually where the chapter's real "
        "question lies.",
        "Paste your own code. Every lesson ends by sending you to a design, class or "
        "routine of your own, and the labs take whatever you paste or type. Nothing you "
        "paste leaves your browser.",
    ],
    "not_covered": [
        "The book's listings, tables and checklists. They are the book's, and they are "
        "named in the lessons, not reproduced: the chapter-end checklists in particular "
        "are worth reading in the book as you finish each lesson.",
        "Language-specific sections. Section 6.5's notes on C++, Java and Visual Basic "
        "classes and section 7.7's macros and inline routines are named and left to the "
        "book, because the lessons use one language, Java.",
        "Design methods as whole systems. Section 5.5 comments on popular methodologies, "
        "and the design patterns of section 5.3 have books of their own; the lessons "
        "name them where the chapter does.",
        "What has changed since 2004 in exception handling, assertions and design "
        "practice. One lesson, Routine Length and Parameters, sets the book's figures on "
        "routine length beside a later view; the rest read the book as written.",
        "Running code. The labs read code and never run it, so they cannot tell you "
        "whether a routine is correct; the exercises ask you to trace a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: pairs and fan-in from dependency records, who knows a secret by following "
        "them, fields and routines by the rules beside each listing, a hierarchy's depth by "
        "counting levels, repeated blocks by matching lines, where a check is wrong by "
        "evaluating it at every boundary, and empty steps by reading the comments. The "
        "code and the designs are written for these lessons; figures quoted from the book "
        "are marked as the book's. A count says where to look, not what you will find."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
