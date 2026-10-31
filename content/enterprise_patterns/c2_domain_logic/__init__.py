"""Course 2 -- Organizing Domain Logic: Chapters 2 and 9, with Chapter 18's
Record Set, Value Object, Money and Special Case.

Seven lessons in two modules: part_a reads Chapter 2 with Chapter 9's
Transaction Script, Domain Model, Table Module and Randy Stafford's Service
Layer; part_b reads three of Chapter 18's base patterns. References are to
Fowler et al., Patterns of Enterprise Application Architecture
(Addison-Wesley, 2002), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/enterprise-patterns/PLAN.md, section C, Course 2.
"""

from . import part_a, part_b

COURSE = {
    "slug": "enterprise-patterns-domain-logic",
    "title": "Organizing Domain Logic",
    "level": "Intermediate",
    "summary": (
        "Chapter 2, Organizing Domain Logic, and Chapter 9, Domain Logic Patterns, "
        "with four of Chapter 18's Base Patterns: Record Set, Value Object, Money and "
        "Special Case. The three ways to organise the middle layer, Transaction "
        "Script, Domain Model and Table Module; how Fowler chooses between them; "
        "Randy Stafford's Service Layer over them; and the small objects a domain "
        "layer is made of. Each lesson sets out the argument, shows the pattern in a "
        "short piece of Java written for the lesson, and counts what the pattern "
        "changes: the lines two scripts or two clients repeat, the decisions a type "
        "switch or a null check spends, the objects each organisation holds, the "
        "public fields that let a value be changed under its owner, and the pennies "
        "a rounding rule loses."
    ),
    "blurb": (
        "Read Fowler's three ways of organising domain logic and the patterns that "
        "sit beside them. Find the rule two scripts copy, see where a type switch's "
        "decisions go in a Domain Model, count objects a row against objects a table, "
        "move two clients' transactions into one service, close the fields that make "
        "a value unsafe to share, split five cents without losing one, and replace a "
        "null with a guest."
    ),
    "key": [
        "a script per action, or objects per thing",
        "a table module: one object a table",
        "no measure of domain complexity",
        "domain logic and application logic differ",
        "a value is equal by its fields",
        "split money with an allocator",
        "return a special case, not null",
    ],
    "assumes_short": "Layers and Performance",
    "assumes_long": (
        "Layers and Performance, for the three layers and where domain logic sits "
        "among them; the code is short Java, and a reader of any C-family language "
        "can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a short listing or a list of tables, the counts "
        "these chapters make in words, and say in the book's terms what each count "
        "shows and what it leaves to judgement."
    ),
    "outcomes": [
        ("Find what scripts and clients repeat",
         "Mark the lines two Transaction Scripts or two kinds of client repeat, and "
         "write the subroutine or the service operation both would call."),
        ("Move a type switch into a Domain Model",
         "Count a routine's decision points, and say which class each branch moves to "
         "when each kind carries its own rule, without changing what it computes."),
        ("Compare the domain patterns' objects",
         "State how many objects a Domain Model and a Table Module hold for the same "
         "tables, and give Fowler's reasons for choosing, which no count settles."),
        ("Separate application logic from domain logic",
         "Sort a use case's response into Stafford's two kinds of business logic, and "
         "say when a Service Layer is worth having."),
        ("Build the small objects safely",
         "Check a class for value equality and immutability, split an amount by ratios "
         "under several rounding rules, and remove a caller's null checks with a "
         "Special Case."),
    ],
    "syllabus_intro": (
        "Seven lessons. The first four read Chapter 2 with Chapter 9's patterns, in "
        "the narrative's order: Transaction Script, Domain Model, Table Module with "
        "Making a Choice, and Service Layer. The last three read the Chapter 18 "
        "patterns a domain layer is built from: Value Object, Money and Special "
        "Case."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Martin Fowler, "
        "with David Rice, Matthew Foemmel, Edward Hieatt, Robert Mee and Randy "
        "Stafford, <em>Patterns of Enterprise Application Architecture</em> "
        "(Addison-Wesley, 2002), with code written for these lessons. Each lesson "
        "names its chapter, sections and patterns, opens with at most one short "
        "quotation, and sets out the argument in its own words. Where a pattern is a "
        "contributor's, as Service Layer is Randy Stafford's, the lesson says so.",
        "Read the narrative as an argument and the patterns as tools. Chapter 2 is "
        "Fowler's case for how to organise domain logic; Chapters 9 and 18 are "
        "patterns to look up. Each lesson says which it is reading.",
        "Treat each count as a reason to look. The labs count what each organisation "
        "costs in code on the listing or tables the lesson gives: repeated lines, "
        "decision points, objects, public fields, pennies. The choice between the "
        "three domain patterns is Fowler's judgement, and he says plainly that no "
        "one can measure the quantity it turns on; no count here settles it.",
        "Paste your own code. Every lesson ends by sending you to a system you know, "
        "and the labs take whatever you paste or type. Nothing you paste leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's revenue recognition example. Fowler works it in full through "
        "Transaction Script, Domain Model, Table Module and Service Layer, and it is "
        "pointed to here, not reworked: the lessons' code uses domains of its own.",
        "The book's listings, sketches and the other Part 2 examples, including the "
        "Money class by Matt Foemmel and Fowler and the null employee of Special Case. "
        "They are named in the lessons and better read in the book.",
        "Platform specifics of 2002: entity beans, ADO.NET data sets, EJB session "
        "beans for a Service Layer. Named where the book names them; not taught.",
        "How the domain layer is connected to the database. Active Record and Data "
        "Mapper are named here and read in the next course, Talking to the Database.",
        "Running code. The labs read code and records and never run them, so they "
        "cannot tell you whether a routine is correct; the exercises ask you to trace "
        "a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: repeated blocks by matching statement lines, decision points by "
        "a stated rule, objects by adding row counts, public fields by the rules "
        "beside each listing, and shares of an amount by exact arithmetic on the "
        "ratios given. The code is written for these lessons; the one figure taken "
        "from the book, Matt Foemmel's five cents, is marked as the book's "
        "illustration. A count models the situation the lesson states; it is not a "
        "measurement of your system."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
