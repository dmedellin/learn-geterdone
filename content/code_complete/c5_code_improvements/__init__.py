"""Course 5 -- Code Improvements: Part V of Code Complete, Chapters 20-26.

Eight lessons: the quality landscape (Chapter 20), collaborative construction
(21), developer testing in two halves (22), debugging (23), refactoring (24),
and code tuning's strategies (25) and techniques (26). part_a holds Chapters
20-22, part_b Chapters 23-26 (PLAN E.1). Page references are to the second
edition (Microsoft Press, 2004).
"""

from . import part_a, part_b

COURSE = {
    "slug": "code-complete-code-improvements",
    "title": "Code Improvements",
    "level": "Intermediate",
    "summary": (
        "Part V of the book, Chapters 20 to 26: The Software-Quality Landscape; "
        "Collaborative Construction; Developer Testing; Debugging; Refactoring; Code-Tuning "
        "Strategies; and Code-Tuning Techniques. McConnell surveys how defects are found and "
        "what each technique finds, argues for reviews beside tests, sets out how to choose "
        "tests, how to find and fix a defect by experiment, how to change working code "
        "safely, and when and how to make it faster. The labs multiply removal rates, cost a "
        "pipeline of reviews and tests, count basis tests and boundary tests, halve a set of "
        "suspects, measure a block before extracting it, and work out what tuning one "
        "routine or one loop nest changes."
    ),
    "blurb": (
        "Read Part V a chapter at a time. Combine removal rates, read a routine as an "
        "inspector, count the tests a routine needs and the boundaries a check gets wrong, "
        "bisect a thousand changes, measure a block before it moves, and work out what a "
        "faster routine does to the whole program."
    ),
    "key": [
        "left: start × every miss rate",
        "basis tests: 1 plus each decision",
        "test a boundary below, on and above",
        "each debugging test halves the suspects",
        "in: set before, read in the block",
        "speedup: old time over new time",
        "a count is a reason to look",
    ],
    "assumes_short": "Statements",
    "assumes_long": (
        "the courses Creating High-Quality Code and Statements, in particular the "
        "decision-point count of Nesting and Complexity; you can read a short Java routine"
    ),
    "outcomes_intro": (
        "By the end you can say what Part V argues, chapter by chapter, and do each "
        "chapter's count or arithmetic by hand."
    ),
    "outcomes": [
        ("Combine defect-removal stages",
         "Compute the defects a sequence of stages finds and leaves from each stage's rate, "
         "and the hours per defect found when each stage has a cost, and state what the "
         "product assumes."),
        ("Inspect a routine",
         "Read a short routine against its specification as an inspector prepares, and list "
         "each defect with its line and the kind of checklist question that finds it."),
        ("Choose tests by count and by boundary",
         "Count a routine's basis test cases and give one input for each, and list a range's "
         "six boundary tests and name the ones a check gets wrong."),
        ("Locate a defect by experiment",
         "State a hypothesis about a failure, the test that decides it and the line, and "
         "count the steps a binary search takes among n suspects."),
        ("Measure a change before making it",
         "Give a block's inputs and outputs before extracting it into a routine, compute "
         "what tuning one routine does to a profile's total, and count the passes of a loop "
         "nest in two orders."),
    ],
    "syllabus_intro": (
        "Eight lessons follow the book's fifth Part in order. Chapter 22, on developer "
        "testing, is split in two: structured basis testing, then boundaries, bad data and "
        "the rest of the chapter."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Steve McConnell's "
        "<em>Code Complete</em>, second edition (Microsoft Press, 2004). Each lesson opens "
        "with one short quotation, then sets out the chapter's argument in its own words, "
        "section by section, and names the pages; the section numbers and pages are that "
        "edition's. The code in the lessons is written for them, and none of the book's "
        "listings, tables or checklists is reproduced.",
        "Treat the defect-removal figures as averages. The detection rates, the hours per "
        "defect and the distribution of errors are averages from many organisations' "
        "projects, mostly before 2004, which the book quotes from Capers Jones and others. "
        "Every lesson and lab that uses them says whose they are, and your own defect "
        "records are what would test them.",
        "Use the labs on code of your own. Four labs read Java: they count basis tests, "
        "the inputs and outputs of a block, and the boundaries of a check. Each lesson's "
        "last step sends you to a routine, a review, a bisection or a profile of yours.",
        "Read every count as a reason to look. A basis count is the fewest tests, not "
        "enough tests; a speedup in loop passes is not a speedup in time. The chapters "
        "say the same of their own numbers, and the last two insist on measurement.",
    ],
    "not_covered": [
        "Independent and system testing as disciplines. Chapter 22 is about the testing a "
        "developer does, and so are the lessons; beta tests, performance tests and the work "
        "of a test team are named, not taught.",
        "The book's checklists and its catalogue of refactorings and tuning techniques. "
        "The lessons name them and paraphrase a few points; the lists and the timing tables "
        "are the book's and are better read in your copy.",
        "Debugging tools in detail. Section 23.5's survey of comparators, compiler warnings, "
        "debuggers and profilers is summarised in a sentence; tools have changed since 2004 "
        "and the method has not.",
        "Language-specific tuning. The book times its techniques in C++, Java, Visual Basic, "
        "PHP and Python; the lessons report a few of those timings as the book's and teach "
        "only what the chapter says about all of them, that each change must be measured.",
        "What has happened to testing since 2004. Test-driven development is stated once, "
        "in Structured Basis Testing, as a continuation of the book's test-first advice; "
        "continuous integration, mutation testing and modern review tools are not taught.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a removal rate is a product of the stages' misses, a basis count is one plus the "
        "decisions a stated rule finds, a bisection is a count of halvings, and a speedup is "
        "a ratio of totals. The rates and hours are the book's reports of other people's "
        "averages, marked with their source; the profiles and loop sizes are illustrative. "
        "The labs read code and never run it, and nothing you paste is sent anywhere."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
