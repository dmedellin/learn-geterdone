"""Course 4 -- Breakthroughs and Implicit Concepts: Part III, Chapters 8 and 9.

Five lessons in one module: part_a reads Chapter 8, Breakthrough, and Chapter
9, Making Implicit Concepts Explicit, in the book's order: the story of a
breakthrough and the decision to take it; the five ways of digging out a
missing concept; explicit constraints and processes as domain objects; the
Specification pattern; and its three uses. References are to Eric Evans,
Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/domain-driven-design/PLAN.md, section C, Course 4.
"""

from . import part_a

COURSE = {
    "slug": "ddd-implicit-concepts",
    "title": "Breakthroughs and Implicit Concepts",
    "level": "Intermediate",
    "summary": (
        "Part III of the book, Refactoring Toward Deeper Insight, begins with two "
        "chapters on how a model gets deeper. Chapter 8, Breakthrough, is a story: "
        "months of small refactorings, then a sudden change of model, and the hard "
        "decision to make it under a deadline. Chapter 9, Making Implicit Concepts "
        "Explicit, is the method behind the story: where to look for a concept the "
        "model is missing, how to model the less obvious kinds of concept, "
        "constraints and processes, and the Specification pattern, which Evans "
        "developed with Martin Fowler. Each lesson sets out the argument and counts "
        "one consequence on a small model written for the lesson: the cents a "
        "rounding rule loses, the experts' terms the code cannot name, the decisions "
        "a constraint moves out of its host, and the candidates a specification "
        "admits or refuses, clause by clause."
    ),
    "blurb": (
        "Read Evans's story of a breakthrough and the method that leads to one. "
        "Split a bill by two kinds of share without losing a cent, find the "
        "librarians' words that name no class, move a theatre's sales limit out of "
        "the method that sells seats, and check seed lots against a specification "
        "for validation, for selection and for building to order."
    ),
    "key": [
        "a breakthrough is an event, not a technique",
        "listen for words the design lacks",
        "give a constraint a name and a home",
        "model a process the experts talk about",
        "a specification: a rule as a value object",
        "validate, select, build to order: one rule",
    ],
    "assumes_short": "The Life Cycle of a Domain Object",
    "assumes_long": (
        "The Life Cycle of a Domain Object, for Aggregates, Factories and "
        "Repositories, and The Building Blocks of a Model-Driven Design, for "
        "Entities, Value Objects and Services; the code is short Java, and a reader "
        "of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small model written down in front of you, the "
        "counts these chapters make in words, and say in the book's terms what each "
        "count shows and what it leaves to judgement."
    ),
    "outcomes": [
        ("Say what a breakthrough is and what it costs",
         "Retell Evans's story in its stages, name the questions a team should answer "
         "before taking a breakthrough under pressure, and show on a split bill what "
         "an explicit share concept makes exact."),
        ("Dig out a missing concept",
         "Name the five places Evans looks for one, and on a glossary of three "
         "audiences find the terms the experts use that the code cannot name."),
        ("Make a constraint or a process explicit",
         "Factor a rule out of the method it lives in, count where its decisions go, "
         "and apply Evans's test for which processes belong in the model."),
        ("Write a rule as a Specification",
         "State a rule as a predicate-like value object, and check one candidate "
         "against it clause by clause."),
        ("Apply one Specification three ways",
         "Use the same rule to validate an object, to select from a collection and "
         "to state what a generator must build, and say what each use costs to "
         "implement."),
    ],
    "syllabus_intro": (
        "Five lessons. The first reads Chapter 8 whole. The other four read Chapter "
        "9 in the book's order: Digging Out Concepts, How to Model Less Obvious "
        "Kinds of Concepts with its constraints and processes, the Specification "
        "pattern, and Applying and Implementing Specification."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. "
        "Each lesson names its chapter, sections and patterns, opens with at most "
        "one short quotation, and sets out the argument in its own words. Where the "
        "book draws on another author, as Specification was developed with Martin "
        "Fowler, the lesson says so.",
        "Read Chapter 8 as a story and Chapter 9 as a method. The breakthrough is an "
        "account of one project, told so that you recognise the shape when it "
        "happens to you; the ways of finding concepts and the Specification pattern "
        "are tools to pick up. Each lesson says which it is reading.",
        "Treat each count as a reason to look. The labs count one consequence of "
        "one modelling choice on the model the lesson states: cents, missing names, "
        "decision points, clauses. Whether a concept belongs in the model is "
        "Evans's question for the domain, the team and the project, and no count "
        "here settles it.",
        "Bring your own model. Every lesson ends by sending you to a system you "
        "know, and the labs take whatever you type. Nothing you type leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's examples. Chapter 8's loan syndication story and Chapter 9's "
        "shipping itinerary, interest accruals, overbooking policy, delinquent "
        "invoices and chemical warehouse are summarised in the lessons and read in "
        "the book; the labs use domains of their own.",
        "The book's diagrams, dialogues and code listings. They are named where the "
        "argument runs through them, never redrawn or retyped.",
        "Combining specifications with and, or and not as objects, and subsumption. "
        "Chapter 9 points ahead to them; they are read in the next course, Supple "
        "Design, in Declarative Design.",
        "Strategy as a domain pattern. Chapter 9 names it for processes with more "
        "than one way to run; it is read in Analysis Patterns, Design Patterns and Refactoring, with Chapter 12.",
        "Running code. The labs read code and records and never run them, so they "
        "cannot tell you whether a rule is right for the business; that is a "
        "conversation with the people who know it.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: shares of an amount by exact arithmetic on the ratios given, "
        "missing and differing names by comparing a glossary's columns, decision "
        "points by a stated rule, and a specification's verdict clause by clause on "
        "the candidates typed. The models and code are written for these lessons; "
        "none of the book's figures is used. A count shows one consequence of one "
        "modelling choice on the model stated; it is not a verdict on the choice."
    ),
    "lessons": part_a.LESSONS,
}
