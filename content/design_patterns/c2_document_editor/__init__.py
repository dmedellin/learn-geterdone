"""Course 2 -- A Case Study: Designing a Document Editor: Chapter 2.

Seven lessons, one per design problem of the chapter's case study, Lexi:
part_a reads 2.1-2.6 (document structure and Composite, formatting and
Strategy, embellishment and Decorator, look-and-feel standards and Abstract
Factory, window systems and Bridge); part_b reads 2.7-2.9 (user operations and
Command, spelling checking and hyphenation with Iterator and Visitor, and the
summary). References are to Gamma, Helm, Johnson and Vlissides, Design
Patterns (Addison-Wesley, 1995), by chapter, section and pattern; PDF pages of
the operator's copy appear only in source comments. The design is
docs/design-patterns/PLAN.md, section C, Course 2.
"""

from . import part_a, part_b

COURSE = {
    "slug": "gof-document-editor",
    "title": "A Case Study: Designing a Document Editor",
    "level": "Intermediate",
    "summary": (
        "Chapter 2 of the book follows one design, a WYSIWYG document editor called "
        "Lexi, through seven problems, and meets eight of the catalog's patterns on the "
        "way: Composite for the document's structure, Strategy for formatting, "
        "Decorator for borders and scroll bars, Abstract Factory for look-and-feel "
        "standards, Bridge for window systems, Command for undoable operations, and "
        "Iterator and Visitor for spelling checking and hyphenation. Each lesson "
        "summarises Lexi's problem and the authors' solution, and counts one "
        "consequence on a small design of its own with the same shape: the calls an "
        "operation makes over a tree, the classes subclassing needs against "
        "composition, the order a stack of decorators runs in, what a new family or "
        "kind of product changes, and the two stacks of an undo history."
    ),
    "blurb": (
        "Read the Gang of Four's case study, one design problem at a time. Total a "
        "recipe book through one call on its root, count the classes a playlist app "
        "and a library's notices save by holding an object instead of subclassing, "
        "stack decorators on a rental charge in two orders, add a style and a kind of "
        "product to a map viewer, undo and redo an irrigation controller's commands, "
        "and send two analyses round the recipe book as visitors."
    ),
    "key": [
        "encapsulate the concept that varies",
        "a part and a group share one interface",
        "hold an object instead of subclassing",
        "each pattern makes one change cheap",
    ],
    "assumes_short": "What Design Patterns Are",
    "assumes_long": (
        "What Design Patterns Are, for the template the catalog uses and the case for "
        "composition over inheritance that this chapter keeps applying; the code is "
        "short Java, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small design of your own, the counts Chapter 2 "
        "argues from in words, and say which pattern Lexi uses for each problem, what "
        "the count shows and what it leaves to the designer."
    ),
    "outcomes": [
        ("Count an operation over a tree of parts",
         "Give the calls one operation on a composite makes and what it totals, and "
         "say what declaring the child operations safely or transparently does."),
        ("Count subclassing against composition",
         "For a structure and an algorithm, or an abstraction and its platforms, state "
         "the classes under one subclass per pairing and under two hierarchies, and "
         "what one new variant adds to each."),
        ("Trace a stack of decorators",
         "Give the order the calls run in, the result, and whether another order "
         "changes it, and count the classes against a subclass per combination."),
        ("Count what a family of factories costs",
         "State the classes under Abstract Factory and what a new family and a new "
         "kind of product each add and edit."),
        ("Step an undo history",
         "Run commands, undos and redos on a small state and give both stacks, the "
         "redos discarded and what the history keeps."),
        ("Count a visitor's changes",
         "Give the accept and visit calls over a structure and the classes a new "
         "analysis and a new kind of part each change, with Visitor and without."),
    ],
    "syllabus_intro": (
        "Seven lessons, in the chapter's order: the first reads the list of design "
        "problems with the first of them, and each of the others one section, ending "
        "with the last problem and the chapter's summary."
    ),
    "how_to": [
        "Read the section before the lesson. This is a read-along of Erich Gamma, "
        "Richard Helm, Ralph Johnson and John Vlissides, <em>Design Patterns: Elements "
        "of Reusable Object-Oriented Software</em> (Addison-Wesley, 1995), with designs "
        "and code written for these lessons. Each lesson names its section and pattern, "
        "opens with one short quotation, and sets out the argument in its own words.",
        "Read Lexi as the argument and the pattern as a preview. The chapter introduces "
        "each pattern where Lexi needs it and sends the reader to the catalog for the "
        "whole of it; so do these lessons, naming the catalog lesson in a later course "
        "that teaches each pattern in full.",
        "Treat each count as a reason to look. The labs count calls, classes, results "
        "and stacks on the lesson's own designs: a recipe book, a playlist app, an "
        "audio-guide rental, a map viewer, a library's notices, an irrigation "
        "controller. Whether a pattern fits depends on what in the design is expected "
        "to change, which the authors weigh for Lexi and no count settles.",
        "Use your own designs. Every lesson ends by sending you to code you know, and "
        "the labs take whatever you type. Nothing you enter leaves your browser.",
    ],
    "not_covered": [
        "Lexi's own classes and data as lab material: its glyphs, rows and characters, "
        "its widget sets and window systems. They are summarised where the argument "
        "runs through them, and the labs use designs of their own with the same shape.",
        "The chapter's C++ code, class and object diagrams, interaction diagrams and "
        "tables. They are named by section and are better read in the book.",
        "Each pattern in full. The chapter previews eight patterns; their structure, "
        "implementation, sample code and known uses are the catalog's, and are taught "
        "in the later courses.",
        "Running code. The labs read designs and never run them; the exercises ask you "
        "to work a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: calls by counting nodes, totals by adding exact values, classes by the "
        "formulas each lab prints, decorator results by applying each operation in "
        "order, and undo stacks by stepping the script. The designs are written for "
        "these lessons; no figure is taken from the book. A count shows one consequence "
        "of applying a pattern or not; it is not a verdict on the pattern."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
