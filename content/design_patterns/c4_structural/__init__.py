"""Course 4 -- Structural Patterns: Chapter 4.

Eight lessons in two modules: part_a reads the chapter introduction, Adapter,
Bridge, Composite, Decorator and Facade; part_b reads Flyweight, Proxy and the
Discussion of Structural Patterns. References are to Gamma, Helm, Johnson and
Vlissides, Design Patterns: Elements of Reusable Object-Oriented Software
(Addison-Wesley, 1995), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/design-patterns/PLAN.md, section C, Course 4.
"""

from . import part_a, part_b

COURSE = {
    "slug": "gof-structural",
    "title": "Structural Patterns",
    "level": "Intermediate",
    "summary": (
        "Chapter 4 of the catalog: the seven patterns that compose classes and objects "
        "into larger structures, Adapter, Bridge, Composite, Decorator, Facade, Flyweight "
        "and Proxy, and the chapter's closing comparison of the ones that look alike. Each "
        "lesson sets out a pattern's problem, participants, consequences and "
        "implementation issues in its own words, sketches it in Java, and counts one "
        "consequence on a small design written for it: the adapter classes a vendor's "
        "printers need, the classes a second hierarchy saves, the calls one request makes "
        "down a tree, the order a stack of wrappers runs in, the uses that cross a "
        "subsystem's boundary, the bytes sharing saves, and the cost of loading on demand."
    ),
    "blurb": (
        "Read the Gang of Four's structural patterns one by one. Count the adapters a "
        "ticket desk needs for a vendor's printers, what a museum guide's second hierarchy "
        "saves, the calls and litres down a garden's irrigation tree, a theatre seat's "
        "price through a stack of decorators, the uses a parcel locker's facade removes, "
        "the bytes a garden plan's shared plants save, and what an archive's scans cost "
        "behind proxies."
    ),
    "key": [
        "compose classes and objects into larger ones",
        "inheritance for class patterns",
        "composition for object patterns",
        "a reference and forwarding, many ways",
        "similar structures, different intents",
    ],
    "assumes_short": "Creational Patterns",
    "assumes_long": (
        "Creational Patterns, for Abstract Factory, Factory Method and Singleton, which "
        "these patterns lean on, and the Introduction's case for object composition over "
        "class inheritance; the code is short Java 8, and a reader of any C-family "
        "language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a short list of records, the counts these patterns' "
        "consequences argue about in words, and say in the authors' terms what each count "
        "shows and what it leaves to the design."
    ),
    "outcomes": [
        ("Fit an interface, or plan for two",
         "Count the adapter classes under the class and object forms, and the classes a "
         "bridge saves as both sides of a hierarchy grow, and say when each pattern is "
         "applied."),
        ("Trace a request through a structure",
         "Give the calls and the total of one request down a composite tree, and the order "
         "and result of a stack of decorators, with the classes the same options need as "
         "subclasses."),
        ("Count what a subsystem and a pool cost",
         "Count the uses that cross a subsystem's boundary with and without a facade, and "
         "the bytes a pool of flyweights saves with extrinsic state stored and computed."),
        ("Control access, and tell the look-alikes apart",
         "Count creations and cost under eager loading, virtual proxies and protection "
         "proxies, and separate Adapter, Bridge, Composite, Decorator and Proxy by intent."),
    ],
    "syllabus_intro": (
        "Eight lessons, in the book's order. The first reads the chapter's introduction "
        "with Adapter; the next six read one pattern each; the last reads the Discussion "
        "of Structural Patterns that closes the chapter."
    ),
    "how_to": [
        "Read the pattern before the lesson. This is a read-along of Gamma, Helm, Johnson "
        "and Vlissides, <em>Design Patterns: Elements of Reusable Object-Oriented "
        "Software</em> (Addison-Wesley, 1995), with designs and code written for these "
        "lessons. Each lesson names its chapter, sections and pattern, opens with one "
        "short quotation, and sets out the pattern in its own words.",
        "Read each pattern as a reference. The book's template, from Intent to Related "
        "Patterns, is the order the lessons follow; the motivating examples are "
        "summarised in a few sentences, and the C++ and Smalltalk sample code is named, "
        "not reproduced.",
        "Treat each count as one consequence. The labs count classes, uses, calls, bytes "
        "and costs on the lesson's own designs: a box office, a museum guide, a garden, a "
        "parcel locker, an archive, a map viewer. Whether a pattern fits depends on what "
        "in the design is expected to vary, which the authors weigh and no count settles.",
        "Use your own designs. Every lesson ends by sending you to code you know, and the "
        "labs take whatever you type. Nothing you enter leaves your browser.",
    ],
    "not_covered": [
        "The book's example domains and data: the drawing editor's shapes, the window "
        "systems, the equipment hierarchy, the compiler subsystem, the document editor's "
        "characters and images. They are summarised where the argument runs through them, "
        "and the labs use designs of their own.",
        "The book's structure and interaction diagrams and its C++ and Smalltalk sample "
        "code. They are named by section and are better read in the book.",
        "Running code. The labs read records and never run them; the exercises ask you to "
        "trace a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: classes as products and sums of variant counts, uses and fan-in by "
        "counting records, calls and totals by walking a tree, a stack's result by exact "
        "arithmetic, bytes from the sizes given, and costs from the requests listed. The "
        "designs are written for these lessons; no figure is taken from the book. A count "
        "shows one consequence of applying a pattern or not; it is not a verdict on the "
        "pattern."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
