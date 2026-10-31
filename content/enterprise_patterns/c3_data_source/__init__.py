"""Course 3 -- Talking to the Database: Chapter 3's first half and Chapter 10.

Six lessons in two modules, all in part_a: four read Chapter 10, Data Source
Architectural Patterns, with the narrative of Chapter 3 that introduces each
pattern and the Chapter 18 base patterns behind them (Gateway, Mapper); two
read Chapter 3, Mapping to Relational Databases (Building the Mapping,
Database Connections, Some Miscellaneous Points) with Chapter 18's Registry.
The source is Fowler et al., Patterns of Enterprise Application Architecture
(Addison-Wesley, 2002), cited by chapter, section and pattern; PDF pages of
the operator's copy are in source comments only. The design is
docs/enterprise-patterns/PLAN.md, section C, Course 3.
"""

from . import part_a

COURSE = {
    "slug": "enterprise-patterns-data-source",
    "title": "Talking to the Database",
    "level": "Intermediate",
    "summary": (
        "Chapter 3, Mapping to Relational Databases, in its first half (Architectural "
        "Patterns, Reading in Data, Building the Mapping, Database Connections and Some "
        "Miscellaneous Points), read with Chapter 10, Data Source Architectural Patterns, "
        "and three of Chapter 18's Base Patterns: Gateway, Mapper and Registry. Fowler "
        "offers four ways for the domain to talk to the database, Table Data Gateway, Row "
        "Data Gateway, Active Record and Data Mapper, and says the choice follows from how "
        "the domain logic is built. Each lesson sets out the narrative's argument and the "
        "pattern it introduces, shows the pattern in a short piece of Java, and counts "
        "what it costs or saves on a stated situation: the classes a column rename is "
        "edited in, the time of fifty keyed finds against one broad query, the routines "
        "that make a row object an Active Record, what a change to the database library "
        "reaches with and without a mapper, the lines two mappings repeat, and the waits "
        "a batch of statements removes."
    ),
    "blurb": (
        "Read the four data-source patterns where Chapter 3 introduces them. Count where "
        "a schema change is edited with and without a gateway, time keyed finds against "
        "one broad query, tell an Active Record from a Row Data Gateway by its routines, "
        "trace what a database change reaches through a mapper, find what two mappings "
        "repeat, and work out what batching saves."
    ),
    "key": [
        "keep the SQL out of the domain logic",
        "a gateway holds a table's SQL",
        "domain logic makes it an Active Record",
        "a mapper keeps both sides ignorant",
        "each statement pays the latency",
        "a batch removes waits, not work",
    ],
    "assumes_short": "Organizing Domain Logic",
    "assumes_long": (
        "Layers and Performance, for the three layers and the vocabulary of latency, and "
        "Organizing Domain Logic, for Transaction Script, Table Module and Domain Model, "
        "since the choice of data-source pattern follows from that choice; and enough SQL "
        "to read a one-table SELECT"
    ),
    "outcomes_intro": (
        "By the end you can say, for a design you know, which of the four data-source "
        "patterns it uses, and count on a stated situation what that choice makes a "
        "change, a query or a save cost."
    ),
    "outcomes": [
        ("Say where a schema change is edited",
         "List the classes that hold SQL against a table, which are the classes a column "
         "rename is edited in, and count them again once the SQL is behind a gateway."),
        ("Time the ways of reading rows",
         "Compute the time of keyed finds, one broad query and finds in batches from a "
         "latency and a cost a row, and say which way the chapter's rule of thumb points "
         "and when the figures reverse it."),
        ("Tell the four patterns apart",
         "Sort a row object's routines into database access and domain logic, say whether "
         "it is a Row Data Gateway or an Active Record, and say what a Data Mapper changes "
         "about who depends on whom."),
        ("Find what a second source repeats",
         "Mark the conversions that two mappings of one kind of data repeat, and write the "
         "logical record and the shared step that would hold them once."),
        ("Work out what batching saves",
         "From a latency, a cost a statement and the statements of a save, compute the time "
         "one at a time and in batches, and the share of the first spent waiting."),
    ],
    "syllabus_intro": (
        "Six lessons follow Chapter 3 in the book's order and pull each Chapter 10 pattern "
        "forward to the narrative that introduces it: four on the architectural patterns "
        "(gateways, Row Data Gateway with Reading in Data, Active Record, Data Mapper), "
        "then Building the Mapping, then Database Connections with Registry."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Martin Fowler, with "
        "David Rice, Matthew Foemmel, Edward Hieatt, Robert Mee and Randy Stafford, "
        "<em>Patterns of Enterprise Application Architecture</em> (Addison-Wesley, 2002), "
        "with code written for these lessons. Each lesson names the chapter, section and "
        "pattern it reads, opens with at most one short quotation, and sets out the "
        "argument in its own words. The book's own examples, in C# and Java, are worked in "
        "full in Part 2 and are better read there; none of its listings is reproduced.",
        "Expect a count in every lesson. Each one counts what a design makes a change, a "
        "query or a round trip cost: the classes a rename is edited in, the statements a "
        "page issues, the classes a change reaches, the lines two mappings repeat. The "
        "database is yours to imagine, because the labs run none: they read the "
        "dependencies, the code or the timings the lesson states and do the arithmetic.",
        "Know what the last lesson counts. Database Connections and Registry counts only "
        "batching, one point of Some Miscellaneous Points; connections, pooling and "
        "Registry are read without a count, since what they decide is where an object "
        "lives, not how many of anything there are.",
        "Treat each count as a reason to look. A latency of 5 ms is the lesson's figure, "
        "not your network's, and Fowler's own advice in Reading in Data is to profile your "
        "application with your own database and data. Every lesson ends by sending you to "
        "a system you know, with a count to make there.",
    ],
    "not_covered": [
        "SQL tuning and stored procedures. Fowler names them where they bear on a pattern "
        "(stored procedures organised as a Table Data Gateway, indexes and clustering as "
        "the database administrator's business), and the lessons name them there; they "
        "are not taught.",
        "The structural and behavioral mapping patterns. Unit of Work, Identity Map, Lazy "
        "Load, the inheritance mappings and the rest of Chapter 3's second half are the "
        "next course's; this one names them where a Data Mapper needs them.",
        "Platform specifics: ADO.NET data sets and readers, JDBC beyond the four calls the "
        "snippets use, and the connection pools of particular servers.",
        "The book's code examples. They are the book's, and each lesson points to its "
        "pattern's examples by name.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: the classes a change reaches by following the dependencies it lists, "
        "fields, routines and repeated lines by the rules beside each listing, and query "
        "and save times as products of the statements and the timings it gives. The code "
        "is written for these lessons, and the labs read it without running it; figures "
        "from the book are marked as the book's illustrations. No lab measures a "
        "database."
    ),
    "lessons": part_a.LESSONS,
}
