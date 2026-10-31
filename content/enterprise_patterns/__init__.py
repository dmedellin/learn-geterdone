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

PATH = {
    "slug": "enterprise-patterns",
    "title": "Patterns of Enterprise Application Architecture, Read Along",
    "level": "Intermediate",
    "level_note": "you can read a short Java class and know what a table, a row and a SQL query are",
    # Backtick runs, key lines and worked lines are read by the code dialect
    # (speech.say_code), as on Code Complete.
    "speech": "code",
    "tagline": (
        "Martin Fowler&rsquo;s <em>Patterns of Enterprise Application Architecture</em>, read narrative by narrative with the patterns each one introduces &mdash; and each pattern&rsquo;s trade-off counted on a stated situation: round trips, SQL statements, writes saved, tables touched, conflicts refused, pennies lost. Seven courses and 44 lessons are available."
    ),
    "description": (
        "The Enterprise Application Patterns Subject: a read-along of the 2002 book that follows its eight narrative chapters and reads each with the patterns it introduces. Seven courses take the reader from layering and domain logic through the database, object-relational mapping, web presentation, concurrency and session state to distribution. Each lesson sets out a chapter&rsquo;s argument, shows the pattern in a short piece of Java, and counts its trade-off in the lab &mdash; the statements a lazy collection issues, the writes a unit of work saves, the remote calls a facade removes &mdash; and ends with a situation to work by hand. All seven courses and 44 lessons are available."
    ),
    "key": [
        "fine-grained time = n·(latency + work)",
        "coarse-grained time = m·latency + n·work",
        "lazy load = 1 + one query per parent used",
        "unit of work: one write per object, at commit",
        "stateless objects = users·service/think",
        "a count models the situation, not your system",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. The layers and the performance terms of the first course are used everywhere. The domain-logic choice of the second decides which data-source patterns the third and fourth use. Web presentation, concurrency and distribution then build on a system that already has all three layers."
    ),
    "why_order": [
        "The order is the narratives&rsquo;, and it runs from the outside in and out again. Layers and Performance sets out what an enterprise application is, the vocabulary of performance, and the three layers. Organizing Domain Logic chooses how the middle layer is built. Talking to the Database and Objects and Tables connect it to the database. Web Presentation puts a front on it. Concurrency and Session State let many people use it at once. Distribution and Putting It Together decides what, if anything, runs on another machine, and closes with the book&rsquo;s own summary.",
        "Domain logic comes before the database because Fowler&rsquo;s choice of data-source pattern depends on the domain pattern chosen. A Table Module wants a Table Data Gateway; a rich Domain Model wants a Data Mapper. A reader who meets the mappers before the domain patterns cannot see why there are four of them.",
        "Each pattern is read where the narrative introduces it, not in Part 2&rsquo;s order. Unit of Work is read with Chapter 3&rsquo;s behavioral problem, not after all the data-source patterns, so that the reader meets the problem first.",
        "The courses can be read separately. Web Presentation assumes only the first course. Concurrency and Session State assumes the first and enough of the database courses to know what a row and a commit are.",
    ],
    "prerequisites": [
        "You can read a short Java class. Every snippet is Java 8, at most twenty lines, using classes, interfaces, fields, `if`, loops, `List` and `Map`. Where a snippet uses JDBC (`Connection`, `PreparedStatement`, `ResultSet`), the lesson says in a sentence what each call does. A reader who knows C#, Kotlin or TypeScript reads it without trouble.",
        "You know what a relational table, a row, a primary key and a `SELECT` are. You do not need to write SQL beyond a one-table query; the lessons that need a join show it.",
        "No other Subject. <em>Code Complete, Read Along</em> is a good companion, and its decision-point and duplication counts are reused here, but every rule is restated where it is used. The arithmetic is products, sums and shares, and the labs do it.",
        "A copy of the book is strongly recommended. The book is in copyright, so a lesson states each chapter&rsquo;s argument in its own words, points to the chapter, section and pattern by name, and quotes at most a sentence or two. The code is written for these lessons, and none of the book&rsquo;s listings is reproduced. The book&rsquo;s own examples, worked in full in Part 2, are better read in the book.",
        "Some system of your own, or one you know. Every lesson&rsquo;s last step sends you to a design you work on, with a count to make.",
    ],
    # Each path names its own hazard. This one's is Fowler's rule that advice
    # about performance is not a fact until it is measured on your configuration
    # (Introduction, Thinking About Performance; PDF p. 27 of the operator's copy).
    "material": (
        "every figure on this path is computed in your browser from the situation a lesson states &mdash; its rows, calls, sessions and timings &mdash; and a count models that situation; it is not a measurement of your system, which only measuring your own configuration can give."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: a round-trip time is a product of the calls and the latency the lesson gives, a write count is a count over the script of changes it lists, a table count is a count over the hierarchy it draws. The code is written for this course; the labs read it and never run it, and nothing you type is sent anywhere. Figures the book gives are marked as the book&rsquo;s illustrations. What the labs cannot do is measure your system &mdash; Fowler&rsquo;s advice is to measure it yourself."
    ),
    "courses": COURSES,
}
