"""Course 5 -- Behavioral Patterns I: Requests, Languages and Traversal.

Chapter 5's introduction and its first six patterns, in the book's
alphabetical order: Chain of Responsibility, Command, Interpreter, Iterator,
Mediator and Memento. Lessons 1-5 are in part_a, lesson 6 in part_b.
References are to Gamma, Helm, Johnson and Vlissides, Design Patterns:
Elements of Reusable Object-Oriented Software (Addison-Wesley, 1995), by
chapter, section and pattern; PDF pages of the operator's copy appear only in
source comments. The design is docs/design-patterns/PLAN.md, section C,
Course 5.
"""

from . import part_a, part_b

COURSE = {
    "slug": "gof-behavioral-requests",
    "title": "Behavioral Patterns I: Requests, Languages and Traversal",
    "level": "Intermediate",
    "summary": (
        "The first half of Chapter 5, Behavioral Patterns: its introduction and the "
        "six patterns from Chain of Responsibility to Memento. They are about how "
        "objects pass requests and share the work: a request handed along a chain, a "
        "request made into an object that can be undone, a small language as a tree "
        "of classes, a walk through a structure kept in an object of its own, a group "
        "coordinated through one object, and state saved without being exposed. Each "
        "lesson sets out the pattern and its consequences and counts one of them on a "
        "small design written for it: hops along a chain, undo and redo stacks, the "
        "nodes of a sentence's tree, traversal orders, connections, and the values a "
        "history keeps."
    ),
    "blurb": (
        "Read the Gang of Four on six behavioral patterns. Send a library's requests "
        "down a chain, undo and redo a ferry booking desk's commands, interpret a "
        "print shop's prices as a tree, walk a quiz in three orders, count a cake "
        "order form's connections with and without a mediator, and weigh snapshots "
        "against inverse operations."
    ),
    "key": [
        "behavioral patterns divide the work",
        "a request can travel or be an object",
        "a language can be a hierarchy of classes",
        "a walk can live outside the structure",
        "an interaction can live in one object",
        "state can be saved without exposing it",
    ],
    "assumes_short": "Structural Patterns",
    "assumes_long": (
        "Structural Patterns, for Composite, Flyweight, Facade and Proxy, which these "
        "patterns lean on, and Creational Patterns for Factory Method and Prototype; "
        "the code is short Java 8, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small design written down in front of you, the "
        "counts these patterns' Consequences sections argue about in words, and say in "
        "the authors' terms what each count shows and what it leaves to the design."
    ),
    "outcomes": [
        ("Trace a chain of handlers",
         "Name the handler that takes each request, total the hops, list what falls "
         "off the end, and say why a chain's order matters."),
        ("Run a command history",
         "Give the state and the undo and redo stacks after every step of a script, "
         "with the redo entries a new command discards."),
        ("Interpret a sentence as a tree",
         "Build a small language's syntax tree, count its nodes by class and its "
         "interpret calls, and give its value in a context."),
        ("Walk a structure in three orders",
         "Write a tree's pre-order, post-order and level-order and a node's place in "
         "each, and say who controls the iteration."),
        ("Weigh a mediator and a memento",
         "Count a group's connections pairwise and through a mediator, and the values "
         "a history keeps as snapshots and as inverses, and give each pattern's cost."),
    ],
    "syllabus_intro": (
        "Six lessons, in the book's order. The first also reads the chapter's "
        "introduction; each of the others reads one pattern, all of its sections."
    ),
    "how_to": [
        "Read the pattern before the lesson. This is a read-along of Gamma, Helm, "
        "Johnson and Vlissides, <em>Design Patterns: Elements of Reusable "
        "Object-Oriented Software</em> (Addison-Wesley, 1995), with designs and code "
        "written for these lessons. Each lesson names its chapter and sections, opens "
        "with one short quotation, and sets out the pattern in its own words: intent, "
        "motivation, applicability, participants, consequences and implementation, "
        "with the book's sample code and known uses named.",
        "Read the motivating examples as arguments and the patterns as tools. The "
        "book's examples are user-interface help, menus, regular expressions, lists, "
        "dialog boxes and a constraint solver; the lessons summarise each in a few "
        "sentences and keep its point, and the sketches are Java 8 where the book's are "
        "C++ and Smalltalk.",
        "Treat each count as a reason to look. The labs count hops, stacks, nodes, "
        "orders, connections and stored values on the lesson's own designs: a library "
        "help desk, a ferry booking desk, a print shop, a quiz app, a "
        "bakery's order form, a map viewer. Whether a pattern fits depends on what in "
        "the design is expected to vary, and the authors leave that judgement to you.",
        "Use your own designs. Every lesson ends by sending you to a system you know, "
        "and the labs take whatever you type. Nothing you enter leaves your browser.",
    ],
    "not_covered": [
        "The chapter's other five patterns, Observer, State, Strategy, Template Method "
        "and Visitor, and its Discussion of Behavioral Patterns. They are the next "
        "course's.",
        "The book's sample code, structure and interaction diagrams. They are named by "
        "section and are better read in the book.",
        "The book's example domains as lab data: help handlers, menu items, regular and "
        "Boolean expression grammars, employee lists, the font dialog and the "
        "constraint solver. The labs use designs of their own.",
        "Running code. The labs read records and expressions and never run a program; "
        "the exercises ask you to trace each by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: hops by walking each request down the chain stated, stacks and stored "
        "values by running the script stated, an expression's value in exact fractions, "
        "traversal orders from the records in order, and connections by the formulas "
        "the lab prints. The designs are written for these lessons; no figure is taken "
        "from the book. A count shows one consequence of applying a pattern or not; it "
        "is not a verdict on the pattern."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
