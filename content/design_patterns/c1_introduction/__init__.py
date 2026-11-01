"""Course 1 -- What Design Patterns Are: Chapter 1, Introduction.

Six lessons on the book's first chapter: what a design pattern is and the
patterns inside Smalltalk MVC (1.1-1.2); how the catalog is described and
organised (1.3-1.5); the four parts of 1.6, How Design Patterns Solve Design
Problems, in three lessons (objects and interfaces; inheritance and
composition; designing for change); and how to select and use a pattern
(1.7-1.8). References are to Gamma, Helm, Johnson and Vlissides, Design
Patterns (Addison-Wesley, 1995), by chapter and section; PDF pages of the
operator's copy appear only in source comments. The design is
docs/design-patterns/PLAN.md, section C, Course 1.
"""

from . import part_a, part_b

COURSE = {
    "slug": "gof-introduction",
    "title": "What Design Patterns Are",
    "level": "Intermediate",
    "summary": (
        "Chapter 1 of the book, the Introduction, read section by section. What a design pattern is "
        "and the four elements every pattern has; the patterns inside Smalltalk's "
        "Model/View/Controller; the template each pattern is written in and the "
        "classification by purpose and scope; the book's two principles, program to an "
        "interface and favor composition over inheritance; the eight common causes of "
        "redesign; and how to select and apply a pattern, and when not to. Each lesson "
        "counts one consequence on a small design written for it: the updates a model "
        "sends, the patterns a specification selects, a client's dependencies, the "
        "classes a design's variations need, the modules a change reaches, and the "
        "changes worth a pattern."
    ),
    "blurb": (
        "Read the Gang of Four's introduction: what a pattern is, how the catalog is "
        "organised, and the principles every later chapter leans on. Count the updates "
        "a bike-share dock sends its views, select patterns by purpose and scope, count "
        "a parcel locker's dependencies on classes and on one interface, count a music "
        "player's classes by subclassing and by composition, count the modules an "
        "irrigation controller's changes reach, and select a bakery's changes worth a "
        "pattern."
    ),
    "key": [
        "name, problem, solution, consequences",
        "program to an interface, not to a class",
        "favor composition over inheritance",
        "each pattern lets one aspect vary",
        "apply a pattern only where it is needed",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no earlier course; you can read a short Java class and know what an interface "
        "and a subclass are"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small design written down in front of you, the "
        "counts Chapter 1 argues about in words, and say in the authors' terms what each "
        "count shows and what it leaves to the designer."
    ),
    "outcomes": [
        ("Say what a pattern is",
         "Give the four essential elements of a pattern, read MVC as Observer, Composite "
         "and Strategy, and count the updates one model sends its views."),
        ("Find your way in the catalog",
         "Say what each section of the template is for, give a pattern's purpose and "
         "scope, and select patterns from a list by a specification on both."),
        ("Program to an interface",
         "Tell a class from a type, count a client's dependencies on concrete classes "
         "and on an interface, and say what a new variant reaches in each."),
        ("Weigh inheritance against composition",
         "Count the classes a design's variations need as subclasses and as composed "
         "hierarchies, and give the costs the authors name on both sides."),
        ("Design for change",
         "Name the eight causes of redesign and their patterns, and count the modules "
         "each change reaches before and after a varying thing is encapsulated."),
        ("Select a pattern, and hold back",
         "Select the changes worth a pattern with a rule for what should vary, follow "
         "the steps of applying one, and give the chapter's reason for restraint."),
    ],
    "syllabus_intro": (
        "Six lessons, in the chapter's order. The first two read Sections 1.1 to 1.5; "
        "the middle three read the long Section 1.6 in three parts; the last reads "
        "Sections 1.7 and 1.8, which close the chapter."
    ),
    "how_to": [
        "Read the section before the lesson. This is a read-along of Gamma, Helm, "
        "Johnson and Vlissides, <em>Design Patterns: Elements of Reusable "
        "Object-Oriented Software</em> (Addison-Wesley, 1995), with designs and code "
        "written for these lessons. Each lesson names its chapter and sections, opens "
        "with one short quotation, and sets out the argument in its own words.",
        "Read the code as a sketch. The book's sample code is C++ and Smalltalk; the "
        "sketches here are Java 8, written for each lesson and never more than twenty "
        "lines, and none of them is the book's code with the names changed.",
        "Treat each count as a reason to look. The labs count updates, dependencies, "
        "classes and modules touched on the lesson's own designs: a bike-share dock, a "
        "parcel locker, a music player, a garden irrigation controller, a bakery. "
        "Whether a pattern fits is weighed in the book against what in the design is "
        "expected to vary, and no count settles it.",
        "Use your own designs. Every lesson ends by sending you to a program you know, "
        "and the labs take whatever you type. Nothing you enter leaves your browser.",
    ],
    "not_covered": [
        "The book's examples as data. The spreadsheet and charts of the MVC "
        "illustration, the window and rectangle of the delegation example and the "
        "frameworks the authors cite are summarised where the argument runs through "
        "them; the labs use designs of their own.",
        "The book's diagrams, tables and code. Table 1.1, Table 1.2 and Figure 1.1 are "
        "described in words and are better read in the book; the OMT notation is "
        "explained only as far as a lesson needs it.",
        "The Preface, the Foreword and the Guide to Readers, and the appendices. They "
        "are pointed to; the glossary of Appendix A is worth keeping open.",
        "The patterns themselves. Chapter 1 names most of them; each is read in full, "
        "with its own lesson, in the courses that follow.",
        "Running code. The labs read the records a lesson gives and never run a "
        "program, so they cannot tell you whether a design works.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: updates by counting each change once for every observer of what "
        "changed, selections by evaluating a specification on typed attributes, "
        "dependencies by counting the uses listed, classes by the products and sums "
        "the rules state, and modules touched by counting the distinct modules each "
        "change lists. The designs and code are written for these lessons; no figure "
        "is taken from the book. A count shows one consequence of applying a pattern "
        "or not; it is not a verdict on the pattern."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
