"""The Design Patterns path, as data: a read-along of Erich Gamma, Richard
Helm, Ralph Johnson and John Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995).

Six courses that follow the book's six chapters: the introduction, the
document-editor case study, and the catalog's creational, structural and
behavioral patterns, one lesson per pattern. Each lesson sets out the
pattern's problem and consequences in its own words, sketches it in Java, and
counts one consequence of applying it on a small design written for the
lesson. The content lives here and only here; scripts/ turns it into pages.
The design is docs/design-patterns/PLAN.md.
"""

from . import (
    c1_introduction,
    c2_document_editor,
    c3_creational,
    c4_structural,
    c5_behavioral_requests,
    c6_behavioral_objects,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_introduction.COURSE,
    c2_document_editor.COURSE,
    c3_creational.COURSE,
    c4_structural.COURSE,
    c5_behavioral_requests.COURSE,
    c6_behavioral_objects.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

# Course 1's author completes this from docs/design-patterns/PLAN.md section A,
# field for field as content/domain_driven_design/__init__.py.
PATH = {
    "slug": "design-patterns",
    "title": "Design Patterns, Read Along",
    "level": "Intermediate",
    "level_note": "you can read a short Java class and know what an interface and a subclass are",
    # Backtick runs, key lines and worked lines are read by the code dialect
    # (speech.say_code), as on Code Complete, Enterprise Patterns and
    # Domain-Driven Design.
    "speech": "code",
    "tagline": (
        "Gamma, Helm, Johnson and Vlissides&rsquo;s <em>Design Patterns</em>, read chapter by chapter and pattern by pattern &mdash; and each pattern&rsquo;s consequences counted on a small design: the classes a design&rsquo;s variations need, the calls one operation makes on a tree of parts, the updates a change sends, the undo and redo stacks after a sequence of commands, the objects created and shared. Six courses and 40 lessons are available."
    ),
    "description": (
        "The Design Patterns Subject: a read-along of the 1995 book by Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, the &ldquo;Gang of Four&rdquo;, in its own order, from the introduction&rsquo;s account of what a pattern is and its principles of reusable design, through the case study of a document editor, to the catalog&rsquo;s twenty-three creational, structural and behavioral patterns, one lesson each, and the conclusion. Each lesson sets out a pattern&rsquo;s problem, participants and consequences in its own words, sketches it in a few lines of Java, and counts one consequence of applying it on a small design written for the lesson &mdash; the classes a new product family adds, the handler that takes each request, the redundant updates a change manager saves &mdash; and ends with a design to work by hand. All six courses and 40 lessons are available."
    ),
    "key": [
        "name, problem, solution, consequences",
        "program to an interface, not to a class",
        "favor composition over inheritance",
        "encapsulate the concept that varies",
        "count classes, calls, updates and undos",
        "a count shows a consequence, not a verdict",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else, and the order is the book&rsquo;s. The first course&rsquo;s vocabulary &mdash; the four elements of a pattern, purpose and scope, programming to an interface, composition over inheritance, the causes of redesign &mdash; is used in every lesson after it. The case study shows eight patterns arising from one design&rsquo;s problems before the catalog states them, and the catalog then takes the patterns one by one, in its three chapters."
    ),
    "why_order": [
        "The order is the authors&rsquo;. What Design Patterns Are reads Chapter 1: what a pattern is, how the catalog is described and organised, how patterns solve design problems, and how to select and use one. A Case Study: Designing a Document Editor reads Chapter 2, where eight patterns arise from the problems of building one editor. Creational Patterns, Structural Patterns and the two courses of Behavioral Patterns read the catalog, Chapters 3 to 5, one lesson per pattern and one for each chapter&rsquo;s discussion; the last course ends with Chapter 6, the authors&rsquo; conclusion.",
        "Chapter 1 comes first because every pattern is argued in its terms. A pattern&rsquo;s consequences are a claim about interfaces, inheritance, composition and change, and a reader who meets Decorator before the case for composition over inheritance reads it as a trick rather than as an answer to a cause of redesign.",
        "The case study comes before the catalog because it shows why. The authors present Composite, Strategy, Decorator, Abstract Factory, Bridge, Command, Iterator and Visitor as answers to problems in one design, so that the catalog&rsquo;s formal entries for them are read as solutions already seen at work.",
        "The catalog courses can be read separately once the first course is read, and the book means them to be looked up as well as read through. Chapter 5 holds eleven patterns, more than one course&rsquo;s worth, so it is split after Memento, in the book&rsquo;s alphabetical order; the second half takes the chapter&rsquo;s discussion and the conclusion.",
    ],
    "prerequisites": [
        "You can read a short Java class and know what an interface and a subclass are. Every sketch is Java 8, at most twenty lines, using classes, interfaces, fields, `if`, loops, `List` and `Map`. The book&rsquo;s own code is C++ and Smalltalk; a reader who knows C#, Kotlin or TypeScript reads the sketches without trouble.",
        "You have changed a program after it was written, yours or someone else&rsquo;s. The book&rsquo;s argument is about designs that can take change without being redesigned, and it lands best on a reader who has had to make one.",
        "No other Subject. <em>Code Complete, Read Along</em> teaches the inheritance and coupling heuristics Chapter 1 leans on, <em>Enterprise Application Patterns, Read Along</em> uses Gang of Four patterns throughout, and <em>Domain-Driven Design, Read Along</em> reads Strategy and Composite as concepts in a domain; the lessons here name them where the books meet. The arithmetic is counting, sums and products, and the labs do it.",
        "A copy of the book is strongly recommended. The book is in copyright, so a lesson states each section&rsquo;s argument and each pattern in its own words, points to the chapter, section and pattern by name, and quotes at most a sentence or two. The book&rsquo;s examples are summarised where the argument runs through them; the designs and code in the lessons are written for them, in domains of their own.",
        "Some program of your own, or one you know. Every lesson&rsquo;s last step sends you to a design you work on, with a count to make.",
    ],
    # Each path names its own hazard. This one's is that a count of a small
    # design is not a verdict on a pattern, whose fit depends on what in the
    # design is expected to vary (PLAN section A).
    "material": (
        "every figure on this path is counted in your browser from the small design a lesson states &mdash; its classes, objects, requests, events and changes &mdash; and a count shows one consequence of applying a pattern or not; it is not a verdict on the pattern, whose fit depends on what in the design is expected to vary."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is counted in your browser from what the lesson states: a class count is the product or sum its rules give for the variations listed, an update count is one per observer for each change made, an undo stack is the commands the script ran and did not undo. The designs and code are written for this course; the labs read them and never run them, and nothing you type is sent anywhere. What the labs cannot do is choose a pattern &mdash; the authors weigh each against what in a design is expected to vary, and warn against applying one where its flexibility is not needed, and so must you."
    ),
    "courses": COURSES,
}
