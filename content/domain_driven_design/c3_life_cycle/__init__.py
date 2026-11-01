"""Course 3 -- The Life Cycle of a Domain Object: Part II, Chapters 6 and 7.

Six lessons in two modules: part_a reads Chapter 6, The Life Cycle of a Domain
Object (Aggregates, with its purchase-order example, Factories, Repositories
and Designing Objects for Relational Databases); part_b reads Chapter 7, Using
the Language: An Extended Example. References are to Eric Evans,
Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/domain-driven-design/PLAN.md, section C, Course 3.
"""

from . import part_a, part_b

COURSE = {
    "slug": "ddd-life-cycle",
    "title": "The Life Cycle of a Domain Object",
    "level": "Intermediate",
    "summary": (
        "Chapter 6, The Life Cycle of a Domain Object, and Chapter 7, Using the "
        "Language: An Extended Example, the second half of Part II. Aggregates "
        "draw a boundary round objects that change together; Factories build an "
        "aggregate whole or refuse; Repositories find the roots that already "
        "exist. Then Evans combines every building block on one model, refactors "
        "it, packages it and joins it to another system. Each lesson sets out the "
        "argument and counts one consequence on a small model written for the "
        "lesson: the references that reach past a root, what a delete removes, "
        "whether two concurrent edits keep a rule, which rule refuses a request, "
        "which roots a query selects, and the dependencies two packagings keep "
        "inside a module."
    ),
    "blurb": (
        "Read Evans's three life-cycle patterns and his extended example. Find "
        "the references that bypass a root, watch two correct edits break a "
        "class's capacity under object locks and keep it under one lock, see "
        "which rule a factory refuses with, ask a repository for the bikes due "
        "for service, draw a box office's boundaries, and package it by concept."
    ),
    "key": [
        "outsiders hold only the root",
        "lock the aggregate the rule spans",
        "build it whole, or refuse",
        "find roots as if in memory",
        "take the decisions in order",
        "package by concept, not by pattern",
    ],
    "assumes_short": "The Building Blocks of a Model-Driven Design",
    "assumes_long": (
        "The Building Blocks of a Model-Driven Design, for entities, value "
        "objects, associations and modules; the code is short Java, and a reader "
        "of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small model written down in front of you, "
        "the checks these chapters make in words, and say in the book's terms "
        "what each count shows and what it leaves to judgement."
    ),
    "outcomes": [
        ("Check references against boundaries",
         "Group objects into aggregates with roots, count the references that "
         "cross a boundary and those that reach past a root, and say what a delete "
         "removes and leaves dangling."),
        ("Run concurrent edits under two lock schemes",
         "Given a rule over an aggregate and timed edits by two users, state who "
         "commits and whether the rule holds under object locks and under one lock "
         "on the aggregate."),
        ("Say what a factory admits",
         "Write a factory's invariants as clauses, find the first one a request "
         "breaks, and say how rebuilding a stored object differs from creating one."),
        ("Ask a repository in the model's terms",
         "State a client's question as a specification over aggregate roots, list "
         "the roots it selects and why each other fails, and say which roots need "
         "a repository at all."),
        ("Take Chapter 7's decisions on your own model",
         "Isolate the domain, sort entities from values, draw boundaries, choose "
         "repositories, and package the result by concept, counting dependencies "
         "inside and across modules."),
    ],
    "syllabus_intro": (
        "Six lessons. The first four read Chapter 6: Aggregates and its rules, "
        "the pattern's example of concurrent edits, Factories, and Repositories "
        "with the chapter's section on relational databases. The last two read "
        "Chapter 7's extended example in two halves, each summarising the book's "
        "shipping model and taking the same decisions on a theatre box office "
        "written for the lessons."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of "
        "Software</em> (Addison-Wesley, 2004), with models and code written for "
        "these lessons. Each lesson names its chapter, sections and patterns, "
        "opens with at most one short quotation, and sets out the argument in its "
        "own words.",
        "Read the patterns as tools and the examples as arguments. Chapter 6's "
        "three patterns are stated as you would apply them; its purchase-order "
        "example and Chapter 7's shipping model are summarised, because the "
        "argument runs through them, and every lab works a domain of its own.",
        "Treat each count as a reason to look. The labs count references, "
        "commits, refused clauses, selected roots and dependencies on the small "
        "model a lesson states. Where to draw a boundary, which lock to take and "
        "how to package a model are Evans's judgements, made by weighing the "
        "domain, the team and the project; no count here settles one.",
        "Try your own model. Every lesson ends by sending you to a system you "
        "know, and the labs take whatever objects, rules and records you type. "
        "Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's examples as data. The purchase order with its limit, the "
        "cargo-shipping model and the brokerage account are summarised where the "
        "argument runs through them and are better read in the book; the labs use "
        "a clinic, a cookery class, a seed bank, a bike-share and a theatre box "
        "office written for these lessons.",
        "The book's diagrams and listings, including the shipping model's "
        "constructors and factory methods. The code here is written for the "
        "lessons.",
        "The design of the creation patterns themselves. Factory Method, Abstract "
        "Factory, Builder and Prototype are named where Evans names them and are "
        "left to Gamma and colleagues' Design Patterns.",
        "Locking mechanics: version counters, lock managers, waiting, retries and "
        "deadlock detection. The Enterprise Application Patterns lesson "
        "Pessimistic and Coarse-Grained Locks reads them; the lock lab models only "
        "which edits are refused.",
        "Specification as a pattern. The factory and repository labs use "
        "specifications as rules and queries; Chapter 9's account of them is read "
        "in Breakthroughs and Implicit Concepts.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a "
        "lesson states: references against the aggregate boundaries given, "
        "commits and sums from timed edits under a stated locking rule, clauses "
        "true and false from the attributes typed, and dependencies inside and "
        "across the modules named. The models and code are written for these "
        "lessons; none is the book's. A count shows one consequence of one "
        "modelling choice; it is not a verdict on the choice."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
