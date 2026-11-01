"""Course 9 -- Large-Scale Structure and Strategy: Chapters 16 and 17 and the
Conclusion.

Six lessons in two modules: part_a reads Chapter 16's four large-scale
structures (Evolving Order with System Metaphor, Responsibility Layers,
Knowledge Level, Pluggable Component Framework with the chapter's closing
sections) and the first half of Chapter 17; part_b reads the rest of Chapter 17
and the Conclusion. References are to Eric Evans, Domain-Driven Design:
Tackling Complexity in the Heart of Software (Addison-Wesley, 2004), by
chapter, section and pattern; PDF pages of the operator's copy appear only in
source comments. The design is docs/domain-driven-design/PLAN.md, section C,
Course 9.
"""

from . import part_a, part_b

COURSE = {
    "slug": "ddd-large-scale-structure",
    "title": "Large-Scale Structure and Strategy",
    "level": "Intermediate",
    "summary": (
        "Chapter 16, Large-Scale Structure, Chapter 17, Bringing the Strategy "
        "Together, and the book's Conclusion. How a model too large to hold in one "
        "head can still be understood as a whole: a structure that evolves with the "
        "system, a System Metaphor, Responsibility Layers, a Knowledge Level and a "
        "Pluggable Component Framework; how structure, contexts and distillation "
        "combine on one project; who should set the strategy; and how the book's "
        "projects fared years later. Each lesson sets out Evans's argument and "
        "counts one consequence on a small model written for the lesson: the modules "
        "a change reaches under two packagings, the dependencies that run against "
        "the layers, the translators pairwise and through one framework, the share "
        "of a team's effort on its core, and how far one change travels across a "
        "context map."
    ),
    "blurb": (
        "Read Evans's last strategic chapters and his Conclusion. Count how far "
        "changes reach under a structure fixed early and one that grew, find the "
        "dependencies that run up a set of responsibility layers, see where new "
        "requirements land with a knowledge level, count translators pairwise and "
        "through a framework, assess where a team's effort goes, and follow one "
        "change across a context map."
    ),
    "key": [
        "let the structure evolve",
        "layers cut along the domain's strata",
        "a knowledge level describes the rest",
        "plug components into an abstract core",
        "assess first, then choose a strategy",
        "strategy grows from application work",
    ],
    "assumes_short": "Distillation",
    "assumes_long": (
        "Distillation and Maintaining Model Integrity, for the Core Domain, Generic "
        "Subdomains, the Abstract Core, Bounded Contexts and the Context Map's kinds "
        "of relationship; the code is short Java, and a reader of any C-family "
        "language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small model, the counts these chapters make in "
        "words, and say in the book's terms what each count shows and what it leaves "
        "to judgement."
    ),
    "outcomes": [
        ("Read a structure against its changes",
         "Count the modules each change reaches under two packagings, and say what a "
         "structure fixed early assumed about the domain."),
        ("Check a model against responsibility layers",
         "Sort every dependency into downward, within and upward against a set of "
         "layers, and say what each upward one asks of the model."),
        ("Place a knowledge level",
         "Separate the objects that describe kinds from those that record events, and "
         "find the requirement a knowledge level does not absorb."),
        ("Count the cost of integration",
         "State the translators pairwise and through one framework interface, and the "
         "reach of a change to that interface."),
        ("Assess a project and read its map",
         "Answer Evans's six questions, count where effort goes, follow one change "
         "across a context map, and name the six essentials for deciding strategy."),
    ],
    "syllabus_intro": (
        "Six lessons. The first four read Chapter 16 in its order: Evolving Order with "
        "System Metaphor, Responsibility Layers, Knowledge Level, and Pluggable "
        "Component Framework with the chapter's sections on fitting a structure. The "
        "last two read Chapter 17, the second of them with the book's Conclusion."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. Each "
        "lesson names its chapter, sections and patterns, opens with at most one short "
        "quotation, and sets out the argument in its own words. Where a pattern is "
        "another author's, as Knowledge Level is Martin Fowler's, the lesson says so.",
        "Read the structures as options, not requirements. Evans says a large-scale "
        "structure is optional, that an ill-fitting one is worse than none, and that "
        "each should evolve with the system; every lesson keeps his conditions beside "
        "the pattern.",
        "Treat each count as a reason to look. The labs count one consequence of one "
        "choice on the small model the lesson states: modules touched, dependencies "
        "against the layers, translators, shares of effort, the reach of a change. "
        "Whether a structure fits the domain is the team's judgement, and no count "
        "here settles it.",
        "Bring your own system. Every lesson ends by sending you to a project you know, "
        "and the labs take whatever model you type. Nothing you type leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's examples: the satellite simulator, the layered shipping model, the "
        "payroll and pension model, the SEMATECH CIM Framework and the projects of the "
        "Epilogues. They are summarised where the argument runs through them, and the "
        "labs use domains of their own.",
        "The book's diagrams, including the figures of conceptual dependencies and "
        "shearing points, and its quoted panel instructions and passage from The Oregon "
        "Experiment. They are named in the lessons and better read in the book.",
        "Rules engines, event mechanisms and the technical frameworks the chapters "
        "mention in passing. Named where the book names them; not taught.",
        "The Appendix, Glossary and References. Pointed to, not taught.",
        "Running code. The labs count over the models you state and never run "
        "anything, so they cannot tell you whether a structure, a layer or a framework "
        "fits your domain.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small model "
        "a lesson states: modules touched by adding the distinct modules each change "
        "reaches, dependencies classified by the layers given, translators by counting "
        "pairs, shares of effort by exact fractions of the weeks given, and the reach "
        "of a change by following the kinds of relationship on the map. The models are "
        "written for these lessons, and none of the book's example data is used. A "
        "count shows one consequence of one modelling choice; it is not a verdict on "
        "the choice."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
