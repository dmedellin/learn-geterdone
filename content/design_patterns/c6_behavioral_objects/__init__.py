"""Course 6 -- Behavioral Patterns II: Notification, State and Algorithms, and the Conclusion.

Seven lessons in two modules: part_a reads the last five patterns of Chapter
5, Behavioral Patterns (Observer, State, Strategy, Template Method, Visitor);
part_b reads the chapter's Discussion of Behavioral Patterns and Chapter 6,
Conclusion. References are to Gamma, Helm, Johnson and Vlissides, Design
Patterns: Elements of Reusable Object-Oriented Software (Addison-Wesley,
1995), by chapter, section and pattern; PDF pages of the operator's copy
appear only in source comments. The design is docs/design-patterns/PLAN.md,
section C, Course 6.
"""

from . import part_a, part_b

COURSE = {
    "slug": "gof-behavioral-objects",
    "title": "Behavioral Patterns II: Notification, State and Algorithms, and the Conclusion",
    "level": "Intermediate",
    "summary": (
        "The second half of Chapter 5, Behavioral Patterns, and the book's short "
        "Chapter 6. Observer keeps dependents informed of a change; State gives each "
        "state of an object a class; Strategy puts each algorithm of a family behind "
        "one interface; Template Method fixes an algorithm's steps and lets subclasses "
        "fill some in; Visitor moves operations out of a structure's classes. The "
        "chapter's discussion compares all eleven behavioral patterns, and the "
        "Conclusion says what the authors expect patterns to do. Each lesson counts one "
        "consequence on a small design written for it: the updates a change sends, a "
        "state machine's trace and size, the decisions a strategy moves, the step bodies "
        "a template saves, the classes each kind of addition changes, the connections "
        "colleagues need, and the modules a change request reaches."
    ),
    "blurb": (
        "Read the last five patterns of the catalog and the authors' conclusion. Count "
        "a box office's updates with and without a change manager, trace a library copy "
        "and size it as one conditional or as State classes, watch a print shop's "
        "decisions move into strategies, find the primitive a map tile forgot, count "
        "what a new kind of playlist entry costs a visitor, and count the modules a "
        "bakery's requests reach before and after a consolidation."
    ),
    "key": [
        "a subject knows only its observers' interface",
        "one class for every state",
        "one interface, many algorithms",
        "the parent fixes the order of the steps",
        "new operations cheap, new elements dear",
        "patterns are targets for refactoring",
    ],
    "assumes_short": "Behavioral Patterns I",
    "assumes_long": (
        "Behavioral Patterns I: Requests, Languages and Traversal, for Chapter 5's "
        "introduction and its first six patterns, Mediator and Command above all, which "
        "the discussion compares with these; and the introduction's case for composition "
        "over inheritance. The code is short Java, and a reader of any C-family language "
        "can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a short design written down in front of you, the "
        "counts these patterns' Consequences argue about in words, and say in the "
        "authors' terms what each count shows and what it leaves to the designer."
    ),
    "outcomes": [
        ("Count what a change sends",
         "Count the updates subjects send their observers directly and through a change "
         "manager, and name who triggers them and whether they push or pull."),
        ("Trace and size a state machine",
         "Trace a machine over a sequence of events, and count the branches one "
         "conditional needs against the classes State needs."),
        ("Move an algorithm into strategies or a template",
         "Count the decisions a Strategy takes out of a listing and the step bodies a "
         "template method saves, and name the primitive a subclass has not written."),
        ("Weigh Visitor's two additions",
         "Count the accept and visit calls over a structure, and the classes a new "
         "operation and a new kind of element each change with and without Visitor."),
        ("Read the chapter's comparisons and the Conclusion",
         "Say what each behavioral pattern encapsulates or decouples, count connections "
         "distributed and centralized, and place a consolidation in Foote's life cycle."),
    ],
    "syllabus_intro": (
        "Seven lessons, in the book's order. The first five read the last five patterns "
        "of Chapter 5, alphabetical as the book has them; the sixth reads the chapter's "
        "Discussion of Behavioral Patterns; the seventh reads Chapter 6, which closes "
        "the book and this Subject."
    ),
    "how_to": [
        "Read the pattern before the lesson. This is a read-along of Gamma, Helm, "
        "Johnson and Vlissides, <em>Design Patterns: Elements of Reusable "
        "Object-Oriented Software</em> (Addison-Wesley, 1995), with designs and code "
        "written for these lessons. Each lesson names its chapter, section or pattern, "
        "opens with one short quotation, and sets out the argument in its own words.",
        "Read the patterns as tools and the discussions as arguments. Each pattern "
        "lesson goes through the book's sections in order, from Intent to Related "
        "Patterns, summarises the motivating example in a few sentences, and names the "
        "sample code and known uses without reproducing them. The book's code is C++ "
        "and Smalltalk; the sketches here are Java 8.",
        "Treat each count as a reason to look. The labs count updates, branches, "
        "decisions, step bodies, calls, connections and modules on the lesson's own "
        "designs: a box office, a library copy, a print shop, a map viewer, a playlist, a "
        "ticket desk, a bakery. Whether a pattern fits depends, as the authors say "
        "throughout, on what in the design is expected to vary, and no count settles "
        "it.",
        "Use your own code. Every lesson ends by sending you to a design you know, and "
        "the labs take whatever you type or paste. Nothing you enter leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's example domains and data: the spreadsheet and chart, the network "
        "connection's states, the line-breaking compositors, the document framework, "
        "the syntax trees and the equipment. They are summarised where the argument "
        "runs through them, and the labs use designs of their own.",
        "The book's sample code, structure diagrams and interaction diagrams. They are "
        "named by section and are better read in the book.",
        "Appendix A, the Glossary, B, the Guide to Notation, and C, the Foundation "
        "Classes, and the Bibliography. The lessons point to them where a term needs "
        "one.",
        "Running code. The labs read designs and listings and never run them; the "
        "exercises ask you to count a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: updates by counting the observers of each change, traces by following "
        "the stated transitions, decision points by a stated rule, step bodies, calls "
        "and classes by stated formulas, connections by counting pairs, and modules "
        "touched by counting the distinct modules each change lists. The designs and "
        "code are written for these lessons; no figure is taken from the book. A count "
        "shows one consequence of applying a pattern or not; it is not a verdict on the "
        "pattern."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
