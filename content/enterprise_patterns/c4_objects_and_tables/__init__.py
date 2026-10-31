"""Course 4 -- Objects and Tables: Chapter 3's second half with Chapters 11-13.

Eight lessons in three modules: part_a reads Chapter 3's The Behavioral
Problem and Mapping Relationships with Chapter 11 (Unit of Work, Identity Map,
Lazy Load) and Chapter 12's keys; part_b reads Chapter 12's embedded values and
inheritance mappings and Chapter 13's metadata patterns, with Chapter 3's
Structural Mapping Patterns and Using Metadata. The source is Fowler et al.,
Patterns of Enterprise Application Architecture (Addison-Wesley, 2002), cited
by chapter, section and pattern. The design is
docs/enterprise-patterns/PLAN.md, section C, Course 4.
"""

from . import part_a, part_b

COURSE = {
    "slug": "enterprise-patterns-objects-and-tables",
    "title": "Objects and Tables",
    "level": "Intermediate",
    "summary": (
        "The second half of Chapter 3, Mapping to Relational Databases, read with the "
        "patterns it introduces: Chapter 11, Object-Relational Behavioral Patterns; Chapter "
        "12, Object-Relational Structural Patterns; and Chapter 13, Object-Relational "
        "Metadata Mapping Patterns. Fowler's question is what a program must do to move "
        "objects in and out of tables: remember what changed, load each row once and only "
        "when needed, keep keys and write rows in an order the keys allow, store small "
        "values and whole trees without tables of their own, map a class hierarchy, and "
        "stop writing the same mapping by hand. Each lesson counts what the chapter weighs "
        "on a stated schema: the writes a commit saves, the duplicate objects a map "
        "prevents, the statements a lazy collection issues, the broken keys in an insert "
        "order, the queries a tree takes, the tables an inheritance mapping touches, and "
        "the lines two hand-written finders repeat."
    ),
    "blurb": (
        "Read how objects become rows and back. Count the writes a Unit of Work saves, the "
        "duplicates an Identity Map prevents and the statements lazy loading issues; order "
        "inserts by their foreign keys; count the queries a tree needs as rows and as one "
        "column; compare three mappings of one class hierarchy; and find the repetition "
        "that mapping by metadata removes."
    ),
    "key": [
        "remember changes, write at commit",
        "one row, one object, per session",
        "load late only what may go unused",
        "parents first, unless checks wait",
        "values embed; trees may serialize",
        "inheritance: empty columns or joins",
        "repeated mapping belongs in metadata",
    ],
    "assumes_short": "Talking to the Database",
    "assumes_long": (
        "Talking to the Database, for gateways, Active Record and Data Mapper, and "
        "Organizing Domain Logic, for the Domain Model these patterns serve; the code is "
        "short Java, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can do, on a small schema, script or listing, the counts these "
        "chapters weigh in words, and say what each count shows about a mapping and what it "
        "leaves to measurement on your own system."
    ),
    "outcomes": [
        ("Count what a commit writes",
         "List the statements a Unit of Work writes at commit for a script of loads, "
         "creations, changes and deletions, and the writes it saves against saving each "
         "change at once."),
        ("Count loads, duplicates and lazy statements",
         "Count the distinct rows and duplicate objects in a session's finds, and the "
         "statements and rows four loading strategies issue for a set of parents and "
         "children."),
        ("Order writes by their keys",
         "Write an insert order and a delete order for a schema's foreign keys, find the "
         "keys a proposed order breaks, and say when the database makes the order "
         "unnecessary."),
        ("Weigh the structural mappings",
         "Count the queries a tree takes node by node, level by level and from one column, "
         "and the tables, columns, empty columns and tables touched for a class hierarchy "
         "under single, class and concrete table inheritance."),
        ("Find the mapping that repeats",
         "Mark the lines two hand-written finders repeat exactly and in shape, and write the "
         "metadata a single finder would read instead."),
    ],
    "syllabus_intro": (
        "Eight lessons follow Chapter 3's second half, each read with the patterns it "
        "introduces: three on Chapter 11's behavioral patterns, four on Chapter 12's "
        "structural patterns, and one on Chapter 13's metadata patterns."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Martin Fowler, with "
        "David Rice, Matthew Foemmel, Edward Hieatt, Robert Mee and Randy Stafford, "
        "<em>Patterns of Enterprise Application Architecture</em> (Addison-Wesley, 2002). "
        "Each lesson names the narrative section and the patterns it reads, by chapter, "
        "section and pattern, opens with at most one short quotation, and sets out the "
        "argument in its own words. The code in every lesson is written for it; the book's "
        "own examples and listings are better read in the book.",
        "Count on the schema the lesson states. Every lesson counts statements, rows, "
        "writes or tables on a script, a schema or a hierarchy given beside the lab, by the "
        "rules stated there. The counts are the arithmetic Fowler does in words, with the "
        "numbers put back; they model the situation, not your system.",
        "Know what your tools are doing. An object-relational mapping tool does most of what "
        "this course describes for you: it keeps a unit of work and an identity map, loads "
        "lazily, orders its writes and maps your hierarchies. That is why it is worth knowing "
        "what it is doing, and what each of its defaults counts against.",
        "Take each count to a system you know. Every lesson ends by sending you to a "
        "request, a schema or a class of your own, with a count to make from a log or a "
        "listing. Nothing you type into a lab leaves your browser.",
    ],
    "not_covered": [
        "The book's long mapping examples. Each pattern in Chapters 11 to 13 has worked "
        "examples in Java or C#, some of them several pages long; the lessons point to them "
        "by pattern and do not rework them.",
        "Association Table Mapping and Dependent Mapping beyond a paragraph each. Identity Field and Foreign Keys "
        "names what each is for and leaves its mechanics to the book.",
        "The full range of Identity Field's key schemes and Lazy Load's four forms. The "
        "lessons name the choices and show one of each in code.",
        "What has changed since 2002 in object-relational mapping frameworks and document "
        "databases. One lesson, Embedded Value and Serialized LOB, sets Fowler's caution "
        "about large objects beside databases that can query inside a document column; the "
        "rest read the book as written.",
        "Running anything. The labs count from what you type and never run a query, so they "
        "cannot time a statement or a join; Fowler's advice is to measure that on your own "
        "database.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: writes from a script of changes, duplicates from a list of finds, "
        "statements and rows from parents and their children, insert orders from foreign "
        "keys, queries from a tree, tables and columns from a class hierarchy, and repeated "
        "lines from a listing. The scripts, schemas and code are written for these "
        "lessons, and figures quoted from the book are marked as the book's. A count "
        "models the situation the lesson states; it is not a measurement of your system."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
