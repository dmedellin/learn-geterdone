"""Course 4 -- Statements: Part IV of Code Complete, Chapters 14-19.

Seven lessons: straight-line code, conditionals, loops and unusual control
structures (part_a, Chapters 14-17), then table-driven methods and Chapter 19
in two halves, boolean expressions and nesting with the decision-point count
(part_b, Chapters 18-19). Page references are to the second edition
(Microsoft Press, 2004). Every snippet is written for these lessons.
"""

from . import part_a, part_b

COURSE = {
    "slug": "code-complete-statements",
    "title": "Statements",
    "level": "Intermediate",
    "summary": (
        "Part IV of the book, Chapters 14 to 19: Organizing Straight-Line Code; Using "
        "Conditionals; Controlling Loops; Unusual Control Structures; Table-Driven "
        "Methods; and General Control Issues. McConnell goes through the statements a "
        "routine is made of, from code with no branches to the nesting of many, and asks "
        "of each how to write it so that a reader can follow it. The labs count the "
        "dependencies between statements, the tests a chain of ifs makes, the passes a "
        "loop header allows, the calls a recursion makes, the comparisons a lookup "
        "table needs, the rows on which two conditions agree, and a routine's decision "
        "points and nesting."
    ),
    "blurb": (
        "Read Part IV a chapter at a time. Order a routine by its dependencies, price a "
        "chain of tests by frequency, read a loop from its header, count a recursion "
        "against its loop, look keys up on a staircase, compare two conditions row by "
        "row, and count the decision points of a routine before and after flattening it."
    ),
    "key": [
        "order statements by their dependencies",
        "put the most common case first",
        "check the first, middle and last pass",
        "return early when it reads better",
        "move the logic into tables",
        "negate each part and swap && and ||",
        "points: 1 + each if, for, while, case, &&, ||",
        "counts are reasons to look",
    ],
    "assumes_short": "Laying the Foundation and Creating High-Quality Code",
    "assumes_long": (
        "Laying the Foundation and Creating High-Quality Code, for the argument that "
        "managing complexity comes first and for what makes a good routine; Variables "
        "helps but is not required"
    ),
    "outcomes_intro": (
        "By the end you can say what each chapter of Part IV argues and do its count on a "
        "short Java routine by hand."
    ),
    "outcomes": [
        ("Order statements by their dependencies",
         "List which line reads what another line wrote, reorder straight-line code so "
         "that no dependency points backwards, and make a hidden dependency visible "
         "through parameters."),
        ("Price a chain of tests",
         "Compute the expected tests of an if-else-if chain from its cases' frequencies, "
         "as written and in order of frequency, and name the input a chain without a "
         "final else lets through."),
        ("Read a loop from its header",
         "State a loop's iterations, the last value of its index and the value the index "
         "is left holding, and find the header that never ends."),
        ("Flatten and count",
         "Rewrite nested conditions as guard clauses, count the calls of a recursion "
         "against its loop, and count a routine's decision points and deepest nesting by "
         "the chapter's rule."),
        ("Look up and compare",
         "Look a key up in a stair-step table under a stated endpoint rule with the "
         "comparisons each search makes, and decide by truth table whether two "
         "conditions are equivalent."),
    ],
    "syllabus_intro": (
        "Seven lessons follow Part IV in order, one per chapter, with Chapter 19 read in "
        "two halves: boolean expressions, then nesting and complexity."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Steve McConnell's "
        "<em>Code Complete</em>, second edition (Microsoft Press, 2004). Each lesson opens "
        "with one short quotation, sets out the chapter's argument in its own words, "
        "section by section, with its pages, and then turns to code. The code is written "
        "for these lessons, the section numbers and pages are that edition's, and none of "
        "the book's listings, tables or checklists is reproduced; read those in your copy.",
        "Count by hand first. Every lesson ends with an exercise, a short routine or a "
        "table to fix or to measure, and its answer is in one quiz item's explanation, "
        "not on the page, so that you commit to an answer before you see it. The lab can "
        "check your count afterwards.",
        "Treat each count as a reason to look. A dependency, a number of tests, a count of "
        "decision points measures one thing about the code, and the chapters say what to "
        "look at when it is high; none of them is a verdict on the routine. Where a "
        "lesson uses one of the book's guidelines, such as the bands for decision points, "
        "it says whose figure it is.",
        "The course's last lesson, Nesting and Complexity, gathers the counts of the "
        "others into one: the routine it counts has a loop, two compound conditions and, "
        "in its second version, guard clauses, and its decision points add up what the earlier "
        "lessons counted one structure at a time.",
    ],
    "not_covered": [
        "The book's language-specific advice. Visual Basic's case ranges, C++ null-statement "
        "macros, macros that spell && and || as words, and the C conventions for comparing "
        "characters and pointers with zero are named where they arise, not taught; the "
        "lessons use Java throughout.",
        "The goto in detail. Section 17.3's worked examples of error processing with and "
        "without goto, and of sharing code in an else clause, are better read in the book; "
        "Unusual Control Structures gives the arguments and the history once.",
        "The direct-access examples of Section 18.2, the insurance-rate tables and the "
        "flexible-message-format design, which are named in Table-Driven Methods and left "
        "to the book.",
        "The book's checklists for each chapter. The lessons name them and paraphrase a "
        "few points; the lists themselves are better used from your copy.",
        "Running code. The labs read code and never execute it, and the counts are of "
        "structure, not of time; a reader who wants to time a snippet runs it in their "
        "own environment.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: a dependency is a line that reads what another wrote, an expected number "
        "of tests is a frequency-weighted average, a loop's passes and a recursion's calls "
        "follow from a header and a formula, a lookup's comparisons from the table, and "
        "decision points from a rule over keywords. The frequencies and tables are "
        "illustrative; the bands for decision points are McConnell's guidance. None of "
        "the counts says whether a routine is good."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
