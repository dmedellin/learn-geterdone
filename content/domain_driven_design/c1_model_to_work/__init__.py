"""Course 1 -- Putting the Domain Model to Work: Part I, Chapters 1-3.

Five lessons in one module: part_a reads Chapter 1, Crunching Knowledge, in
two lessons; Chapter 2, Communication and the Use of Language, in two; and
Chapter 3, Binding Model and Implementation, in one. References are to Eric
Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/domain-driven-design/PLAN.md, section C, Course 1.
"""

from . import part_a

COURSE = {
    "slug": "ddd-putting-the-model-to-work",
    "title": "Putting the Domain Model to Work",
    "level": "Intermediate",
    "summary": (
        "Part I of the book, Chapters 1 to 3: Crunching Knowledge, Communication and "
        "the Use of Language, and Binding Model and Implementation. How a team of "
        "developers and domain experts digs a model out of what the experts know; "
        "why a business rule belongs in the model rather than in a guard clause; the "
        "Ubiquitous Language, one vocabulary for speech, writing and code; what "
        "diagrams and documents are for, and when one has stopped earning its keep; "
        "and Model-Driven Design, one model for analysis and code, written by "
        "modelers who program. Each lesson sets out Evans's argument and counts one "
        "consequence on a small model written for it: the translations a "
        "conversation needs, the clause that refuses a request, the stale terms in "
        "a document, the modules a change reaches."
    ),
    "blurb": (
        "Read the three chapters that set out what domain-driven design asks of a "
        "team. Count the translations between two kinds of expert and the "
        "developers, and watch a model consolidate them; turn a booking rule into "
        "an object and find the clause that refuses each request; count what a "
        "conversation costs in three vocabularies; find the stale words in a design "
        "document; and see how far a change in the model reaches when the code "
        "follows the model and when it does not."
    ),
    "key": [
        "crunch knowledge as a team, with feedback",
        "make the business rule an object",
        "speak, write and code in one language",
        "documents complement code and speech",
        "a single model for analysis and design",
        "modelers code; coders model",
    ],
    "assumes_short": "Nothing",
    "assumes_long": (
        "no earlier course; you can read a short Java class and have worked on a "
        "program someone else will change"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small model of a domain you know, the counts "
        "these chapters make in words, and say in Evans's terms what each count "
        "shows and what it leaves to judgement."
    ),
    "outcomes": [
        ("Count the translations a team pays for",
         "Lay out the names each audience gives each concept, count the pairs of "
         "names that differ, and find the name that means two things."),
        ("Make a buried rule explicit",
         "Lift a rule out of a guard clause into an object of the model whose "
         "clauses have names, and say which clause refuses a given request."),
        ("Hold a document to account",
         "Read a design document's terms against the words spoken now and the "
         "names in the code, and find the terms that have gone stale."),
        ("Bind the model to the code",
         "Map model concepts to code modules, and count the modules each model "
         "change reaches when the code follows the model and when it follows "
         "screens and jobs."),
        ("Weigh what no count settles",
         "Give Evans's reasons why the people who model must code, and why a "
         "count of a small model is not a verdict on a design."),
    ],
    "syllabus_intro": (
        "Five lessons, in the book's order. Two read Chapter 1: knowledge crunching "
        "and the five ingredients of effective modelling, then knowledge-rich "
        "design and deep models. Two read Chapter 2: the Ubiquitous Language, "
        "Modeling Out Loud and One Team, One Language, then documents, diagrams and "
        "explanatory models. The last reads Chapter 3: Model-Driven Design and "
        "Hands-On Modelers."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. "
        "Each lesson names its chapter and sections, opens with at most one short "
        "quotation, and sets out the argument in its own words. The book's examples "
        "are summarised where the argument runs through them; the labs use domains "
        "of their own.",
        "Read Part I as an argument. These chapters state three patterns, Ubiquitous "
        "Language, Model-Driven Design and Hands-On Modelers, but mostly they make a "
        "case for a way of working, and each lesson says whose case it is.",
        "Treat each count as a reason to look. The labs count translations, refused "
        "clauses, stale terms and modules touched on the small model each lesson "
        "states. Whether a team should pay a translation, keep a document or split "
        "a module is Evans's judgement and yours; no count settles it.",
        "Bring your own project. Every lesson ends by sending you to a model you "
        "know, and the labs take whatever you type. Nothing you type leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's examples as data. The printed-circuit board tool, the cargo "
        "booking and its overbooking rule, the cargo router dialogues, the shipping "
        "route diagrams and the bus rules of Chapter 3 are summarised in the "
        "lessons and better read in the book; the labs use a seed library, a "
        "clinic, a theatre box office, a bike-share and a public library.",
        "The book's diagrams, dialogues and listings. They are described, never "
        "reproduced.",
        "The building blocks. Entities, value objects, services, modules, "
        "aggregates, factories and repositories are named here and read in the next "
        "two courses.",
        "More than one model. Chapter 2 and Chapter 3 assume a single model; "
        "Bounded Context, which deals with several, is read in Maintaining Model "
        "Integrity.",
        "Running code. The labs read the glossaries, rules and module maps a lesson "
        "gives and never run a program, so they cannot tell you whether a design "
        "works; the exercises ask you to trace a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is counted in your browser from what a lesson "
        "states: translations by comparing the names each audience gives each "
        "concept, a refusal by checking a request against a rule clause by clause, "
        "stale terms by reading a document's names against speech and code, and "
        "modules touched by looking up where each changed piece of code lives. The "
        "models and code are written for these lessons. A count shows one "
        "consequence of one modelling choice on the model stated; it is not a "
        "verdict on the choice."
    ),
    "lessons": part_a.LESSONS,
}
