"""Course 1 -- Layers and Performance: the Preface, the Introduction and
Chapter 1 of Fowler et al., Patterns of Enterprise Application Architecture
(Addison-Wesley, 2002), with two base patterns from Chapter 18.

Five lessons, one part file: what an enterprise application is, the words
for performance and for scaling, the three layers, and the two small
patterns that keep the layers' dependency rule. The course has the least
pattern of any, because it sets up the vocabulary the patterns are argued in.
The design is docs/enterprise-patterns/PLAN.md, section C, Course 1.
"""

from . import part_a

COURSE = {
    "slug": "enterprise-patterns-layers-and-performance",
    "title": "Layers and Performance",
    "level": "Intermediate",
    "summary": (
        "The Preface; the Introduction, with its sections Architecture, Enterprise "
        "Applications, Kinds of Enterprise Application, Thinking About Performance and "
        "Patterns; Chapter 1, Layering; and from Chapter 18, Base Patterns, Layer "
        "Supertype and Separated Interface. Fowler says what an enterprise application "
        "is and why its rules resist simplification, defines the words he uses for "
        "performance and scalability, sets out the three layers and the one rule between "
        "them, and gives the two small patterns that keep that rule. The labs count the "
        "special cases in a business rule, compute load sensitivity and project "
        "throughput from the book's own illustrations, find the lines a second "
        "presentation copies, and follow a database change through two designs."
    ),
    "blurb": (
        "Read the Introduction and Chapter 1 with two base patterns. Count a business "
        "rule's special cases, compute load sensitivity and project throughput from the "
        "book's illustrations, find domain logic in a presentation by what a second one "
        "copies, and see what a change below reaches before and after a dependency is "
        "reversed."
    ),
    "key": [
        "enterprise: persistent, shared, integrated",
        "measure on your own configuration",
        "load sensitivity: time against load",
        "scalability: what more hardware adds",
        "presentation, domain, data source",
        "domain never depends on presentation",
        "an interface here can reverse a dependency",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no earlier course; you can read a short Java class and know what a table, a row "
        "and a query are"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small situation or a short listing, the counts "
        "these chapters argue from, and say in Fowler's terms what each shows and what it "
        "leaves to measurement."
    ),
    "outcomes": [
        ("Recognise an enterprise application and its rules",
         "Name the marks Fowler gives an enterprise application, and count the special "
         "cases a business rule carries, naming the agreement behind each."),
        ("Use the words for performance precisely",
         "Tell response time from responsiveness and latency, and compute a system's load "
         "sensitivity from two measurements, saying where a figure is interpolated."),
        ("Separate capacity, efficiency and scalability",
         "Compute efficiency and the gain a server from measurements, find where two "
         "systems' projections cross, and count the servers a target needs."),
        ("Find domain logic in a presentation",
         "Apply Fowler's test of a second presentation to two routines, mark the lines it "
         "copies, and write the domain method that replaces them."),
        ("Reverse a dependency with an interface",
         "List what a change reaches through a set of dependencies, and redraw them with a "
         "Separated Interface so that the domain is out of its reach."),
    ],
    "syllabus_intro": (
        "Five lessons follow the opening of the book in its own order: three on the "
        "Introduction, one on Chapter 1, and one on two base patterns from Chapter 18 that "
        "the layers need."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Fowler et al., "
        "<em>Patterns of Enterprise Application Architecture</em> (Addison-Wesley, 2002), "
        "with code written for these lessons. Each lesson names the chapter, sections and "
        "patterns it reads, opens with at most one short quotation, and sets out the "
        "argument in its own words; the book's examples and listings are better read in "
        "the book.",
        "Expect the least pattern of any course. The Introduction and Chapter 1 set up the "
        "vocabulary the rest of the book argues in: what an enterprise application is, "
        "response time, load, scalability, and the three layers. Only the last lesson reads "
        "patterns, and they are two of the smallest.",
        "Read each figure for what it is. Two labs do arithmetic on the book's own "
        "illustrations, which Fowler supposes in order to make a point, and say so; the other three "
        "count something in a listing or a set of dependencies written for the lesson. No "
        "figure here is a measurement, and Fowler's first rule about performance is that "
        "only your own measurement is one.",
        "Bring a system of your own. Every lesson ends by sending you to a rule, a "
        "response time, a screen or a dependency in software you know, with a count to "
        "make. Nothing you type into a lab leaves your browser.",
    ],
    "not_covered": [
        "The Introduction's discussion of what architecture is. Its two common elements "
        "and Ralph Johnson's view are named in the first lesson, not taught as a topic.",
        "The book's listings, sketches and tables, Table 1.1 among them. They are named "
        "and paraphrased, not reproduced.",
        "Disconnected operation and the synchronising of a client's data, which Fowler "
        "himself puts outside the book's scope in Choosing Where to Run Your Layers.",
        "Other layering schemes. Chapter 8 compares Fowler's three layers with those of "
        "other authors, and Course 7 reads it once every pattern the schemes name has been "
        "met.",
        "What has changed since 2002 in where presentation runs. One lesson, Layering, "
        "sets the chapter beside presentation built in the browser; the rest read the book "
        "as written.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "decision points by the rule printed beside the listing, load sensitivity and "
        "projected throughput by arithmetic on the measurements given, copied lines by "
        "matching text, and what a change reaches by following the dependencies listed. "
        "The book's illustrations are marked as the book's; the code and the designs are "
        "written for these lessons. None of it is a measurement of your system."
    ),
    "lessons": part_a.LESSONS,
}
