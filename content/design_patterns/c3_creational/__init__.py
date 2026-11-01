"""Course 3 -- Creational Patterns: Chapter 3.

Six lessons in two modules: part_a reads the chapter's introduction with
Abstract Factory, then Builder, Factory Method, Prototype and Singleton;
part_b reads the Discussion of Creational Patterns that closes the chapter.
References are to Gamma, Helm, Johnson and Vlissides, Design Patterns:
Elements of Reusable Object-Oriented Software (Addison-Wesley, 1995), by
chapter, section and pattern; PDF pages of the operator's copy appear only in
source comments. The design is docs/design-patterns/PLAN.md, section C,
Course 3.
"""

from . import part_a, part_b

COURSE = {
    "slug": "gof-creational",
    "title": "Creational Patterns",
    "level": "Intermediate",
    "summary": (
        "Chapter 3 of the catalog: the five creational patterns and the authors' "
        "comparison of them. Abstract Factory, Builder, Factory Method, Prototype and "
        "Singleton each take the knowledge of which class to instantiate out of the "
        "code that needs an object. Each lesson sets out the pattern's problem, "
        "participants, consequences and implementation in its own words, sketches it "
        "in Java, and counts one consequence on a small design written for it: the "
        "classes a family-based design needs and what a new family and a new kind "
        "cost, the classes a construction process and its outputs need, who sees a "
        "change made through a clone, and the instances and cost a shared resource "
        "runs up."
    ),
    "blurb": (
        "Read the authors on making objects without naming their classes. Price a map "
        "viewer's new style against a new kind of part, split a recipe book's readers "
        "from its builders, count an irrigation controller's creator classes, watch "
        "one runner's track reach every shallow clone of a playlist, count a locker "
        "registry made five times and once, and count one quiz builder three ways."
    ),
    "key": [
        "creational patterns hide the concrete class",
        "a factory object or a subclass decides",
        "every pattern trades classes for change",
        "flexibility only where it is needed",
    ],
    "assumes_short": "A Case Study: Designing a Document Editor",
    "assumes_long": (
        "A Case Study: Designing a Document Editor, where Abstract Factory first "
        "appears inside the Lexi editor, and What Design Patterns Are, for the "
        "catalog's template and the principle of programming to an interface; the "
        "code is short Java, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small design of your own, the counts these "
        "patterns' Consequences sections argue about in words, and say in the authors' "
        "terms what each count shows and what it leaves to the designer."
    ),
    "outcomes": [
        ("Price families against kinds",
         "Count the classes of an Abstract Factory design and what a new family and a "
         "new kind each add and edit, and give the authors' remedy for new kinds."),
        ("Split construction from representation",
         "Count a Builder design's directors and builders against one class per "
         "pairing, and say who hands the client its product."),
        ("Count creators and clones",
         "Count the creator classes Factory Method needs, and who sees a change made "
         "through a shallow or a deep clone under Prototype."),
        ("Count one instance, and compare the five",
         "Count instances and cost with and without a Singleton, and count one design "
         "under Factory Method, Abstract Factory and Prototype as the chapter's "
         "discussion compares them."),
    ],
    "syllabus_intro": (
        "Six lessons, in the book's order. The first reads the chapter's introduction "
        "with Abstract Factory; the next four read Builder, Factory Method, Prototype "
        "and Singleton; the sixth reads the Discussion of Creational Patterns that "
        "closes the chapter."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Erich Gamma, "
        "Richard Helm, Ralph Johnson and John Vlissides, <em>Design Patterns: Elements "
        "of Reusable Object-Oriented Software</em> (Addison-Wesley, 1995), with designs "
        "and code written for these lessons. Each lesson names its chapter, sections "
        "and pattern, opens with one short quotation, and sets out the pattern in its "
        "own words.",
        "Read the patterns as tools and the discussion as an argument. Each pattern is "
        "set out in the catalog's own order of sections, from Intent to Related "
        "Patterns; the Discussion at the end of the chapter compares them, and the last "
        "lesson reads it through.",
        "Treat each count as a reason to look. The labs count classes, clones and "
        "instances on designs written for these lessons: a map viewer, a recipe book, "
        "an irrigation controller, a playlist, a parcel locker network, a quiz builder. "
        "Whether a pattern fits depends, as the authors say throughout, on what in the "
        "design is expected to vary, and no count settles it.",
        "Use your own designs. Every lesson ends by sending you to a system you know, "
        "and the labs take whatever you type. Nothing you enter leaves your browser.",
    ],
    "not_covered": [
        "The book's running example, the maze for a computer game, with its rooms, "
        "walls and doors. It is summarised where the argument runs through it, and the "
        "labs use designs of their own.",
        "The book's C++ and Smalltalk sample code, structure diagrams and interaction "
        "diagrams. They are named by pattern and section and are better read in the "
        "book; the lessons' sketches are Java 8, written for them.",
        "The systems of the known uses, ET++, InterViews, Unidraw and the rest, beyond "
        "naming them. They were the frameworks of the early 1990s, and the lessons do "
        "not teach them.",
        "Running code. The labs read the families, parts and requests you state and "
        "never run them; the exercises ask you to count a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is counted in your browser from the small design "
        "a lesson states: classes by the formulas each lab prints under its tiles, "
        "holders of a shared part from the records given, and instances and cost by "
        "adding the stated costs over the stated requests. The designs are written for "
        "these lessons; no figure is taken from the book. A count shows one consequence "
        "of applying a pattern or not; it is not a verdict on the pattern, whose fit "
        "depends on what in the design is expected to vary."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
