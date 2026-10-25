"""The Code Complete path, as data: a read-along of McConnell's Code Complete, 2nd ed.

Seven courses following the book's seven Parts. Each lesson sets out a
chapter's argument in its own words and applies it to short Java snippets
written for this Subject; the labs count what the chapter tells you to count.
The content lives here and only here; scripts/ turns it into pages. The design
is docs/code-complete/PLAN.md.
"""

from . import (
    c1_foundation,
    c2_high_quality_code,
    c3_variables,
    c4_statements,
    c5_code_improvements,
    c6_system_considerations,
    c7_craftsmanship,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_foundation.COURSE,
    c2_high_quality_code.COURSE,
    c3_variables.COURSE,
    c4_statements.COURSE,
    c5_code_improvements.COURSE,
    c6_system_considerations.COURSE,
    c7_craftsmanship.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "code-complete",
    "title": "Code Complete, Read Along",
    "level": "Beginner → Intermediate",
    "level_note": "you can read a short routine in Java, C# or C++; the arithmetic is counting",
    # Backtick runs, key lines and worked lines are read by the code dialect
    # (speech.say_code): `&&` is "and", `!done` is "not done".
    "speech": "code",
    "tagline": (
        "Steve McConnell&rsquo;s <em>Code Complete</em>, read chapter by chapter from the foundations of construction to the habits of the craft &mdash; with each chapter&rsquo;s guidance measured on short pieces of code: decision points, live times, basis tests, defect-removal rates and the cost of a late fix. Seven courses and 41 lessons are available."
    ),
    "description": (
        "The Code Complete Subject: a read-along of the second edition (2004) in its own order, seven courses that follow the book&rsquo;s seven Parts. Each lesson sets out a chapter&rsquo;s argument and then applies it to code &mdash; counting the decision points in a routine, the lines a variable stays live, the test cases a routine needs, the defects a set of practices leaves behind, the stubs an integration order needs &mdash; and ends with a piece of code to fix or to measure. All seven courses and 41 lessons are available."
    ),
    "key": [
        "points = 1 + each if, for, while, case, &&, ||",
        "span = lines between two references",
        "live time = last line − first line + 1",
        "paths in a team of n = n·(n − 1)/2",
        "left = N·(1 − e₁)·(1 − e₂)·…",
        "speedup = old time / new time",
        "a count is a reason to look, not a verdict",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Creating High-Quality Code uses the prerequisites and the cost of a late fix from Laying the Foundation; Variables and Statements apply the complexity argument line by line; Code Improvements measures the code they produce; System Considerations and Software Craftsmanship widen the view to the project and the programmer."
    ),
    "why_order": [
        "The order is the book's, and it runs from outside the code inwards and out again. Laying the Foundation says what construction is and what must be settled before it starts; Creating High-Quality Code builds classes and routines; Variables and Statements go down to the line; Code Improvements tests, inspects, debugs, refactors and tunes what was built; System Considerations widens the view to the project; Software Craftsmanship closes on layout, documentation and the programmer.",
        "Design comes before variables and statements because the book's one organising idea, that managing complexity is software's primary technical imperative, is argued in Chapter 5 and used in every later chapter. A reader who meets the decision-point count before the argument for it sees a metric; a reader who meets it after sees the argument applied.",
        "Quality comes after construction because its chapters measure the code the earlier ones taught you to write: the basis tests of Structured Basis Testing are counted on the same routines whose decision points Nesting and Complexity counted.",
        "The Parts can be read separately. Variables and Statements assume only the first two courses; System Considerations can be read by a lead who has read Laying the Foundation; Software Craftsmanship's lessons stand alone.",
    ],
    "prerequisites": [
        "You can read a short routine in a C-family language. Every snippet is Java, kept under twenty lines, and uses nothing past what a first course teaches: if, loops, methods, arrays, a class with fields. A reader who knows C#, C++, JavaScript or Python reads it without trouble; where Java behaves in a way another language does not (integer overflow, integer division, switch fall-through), the lesson says so.",
        "No other Subject. Boolean algebra is taught where the book uses it, in Boolean Expressions; Logic and Proof, a course in Discrete Mathematics, goes further and is optional. The arithmetic is counting, a product and a share; the labs do it, and what is asked of you is to say what each count is evidence of.",
        "A copy of the book is strongly recommended. The book is in copyright, so a lesson states each chapter's argument in its own words, points to the section by number and page, and quotes at most a sentence or two. The code is written for these lessons; none of the book's listings or checklists is reproduced, and the book's own versions are better read in the book.",
        "Some code of your own. Every code lab takes a routine you paste in, and the most useful thing a lesson can do is send you back to your own work with a number to look at.",
    ],
    # Each path names its own hazard. This one's is that a count over code is
    # a reason to look, not a verdict.
    "material": (
        "every figure on this path is computed in your browser from the code or the quantities a lesson states, and a count over code is a reason to look at it, not a verdict on it &mdash; the rates and costs quoted from the book are averages from other people&rsquo;s projects, which your own records can test and the lab cannot."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: a decision-point count is one plus the branches a stated rule finds, a live time is a difference of line numbers, a combined removal rate is a product of the stages&rsquo; misses. The code is written for this course; the labs read it and never run it, and nothing you paste is sent anywhere. Figures quoted from the book are marked with their source. What the labs cannot do is tell you whether a routine is good &mdash; a count says where to look."
    ),
    "courses": COURSES,
}
