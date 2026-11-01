"""Course 7 -- Maintaining Model Integrity: Chapter 14.

Eight lessons in two modules: part_a reads Chapter 14 from its opening through
Bounded Context, Continuous Integration, Context Map, Shared Kernel,
Customer/Supplier Development Teams, Conformist and Anticorruption Layer;
part_b reads Separate Ways, Open Host Service, Published Language, Unifying an
Elephant, Choosing Your Model Context Strategy and Transformations. References
are to Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of
Software (Addison-Wesley, 2004), by chapter, section and pattern; PDF pages of
the operator's copy appear only in source comments. The design is
docs/domain-driven-design/PLAN.md, section C, Course 7.
"""

from . import part_a, part_b

COURSE = {
    "slug": "ddd-model-integrity",
    "title": "Maintaining Model Integrity",
    "level": "Intermediate",
    "summary": (
        "Chapter 14, Maintaining Model Integrity, the first chapter of Part IV, "
        "Strategic Design. Why one model for a whole enterprise rarely pays; how to draw "
        "the Bounded Context in which one model applies and keep it whole with Continuous "
        "Integration; how to chart every context on a Context Map; the relationships "
        "between contexts, from Shared Kernel and Customer/Supplier teams through "
        "Conformist and Anticorruption Layer to Separate Ways, Open Host Service and "
        "Published Language; how to choose among them; and how to move from one to "
        "another. Each lesson sets out the argument and counts one consequence on a small "
        "model written for it: the false cognates and duplicate concepts between "
        "glossaries, the models and translators one change reaches across a map, and the "
        "translators a network needs point to point and through one language."
    ),
    "blurb": (
        "Read Evans on keeping models consistent where they apply and honest where they "
        "meet. Find the words two teams use differently, catch a team's two halves "
        "drifting apart, trace one change across a theatre's seven contexts, compare a "
        "kernel with a supplier and a conformist with a translating layer, count "
        "translators for six theatres, unify four views of a bike, and follow a merger "
        "step by step."
    ),
    "key": [
        "one model per context, drawn explicitly",
        "merge often inside a context",
        "map every context as it really is",
        "a kernel both ways, a supplier one way",
        "conform, or translate behind a layer",
        "integrate only where it pays",
        "unifying means a new model",
        "change relationships in small steps",
    ],
    "assumes_short": "Putting the Domain Model to Work",
    "assumes_long": (
        "Putting the Domain Model to Work, for the Ubiquitous Language and Model-Driven "
        "Design, and The Building Blocks of a Model-Driven Design, for Modules and "
        "Services, which this chapter uses without redefining them; no experience of "
        "large projects is needed, and the one listing is short Java"
    ),
    "outcomes_intro": (
        "By the end you can make, on a few glossaries or a small context map, the counts "
        "this chapter makes in words, and say in the book's terms what each count shows "
        "and what it leaves to judgement."
    ),
    "outcomes": [
        ("Find the splinters between glossaries",
         "List the false cognates, duplicate concepts and terms safe to share between two "
         "or more contexts' glossaries, and say which are splinters inside one context."),
        ("Trace a change across a Context Map",
         "State which models a change in one context reaches and which translators absorb "
         "it, along each of the book's kinds of relationship."),
        ("Compare the relationship patterns",
         "Say what a Shared Kernel, Customer/Supplier teams, a Conformist and an "
         "Anticorruption Layer each make a change reach, and the agreement or code each "
         "needs."),
        ("Count translators for many contexts",
         "Compare the translators to build and to change point to point and through a "
         "Published Language, and say when Separate Ways needs none."),
        ("Plan a strategy and a transformation",
         "Weigh larger against smaller contexts in Evans's terms, and list the first steps "
         "of a merger or a legacy phase-out with what each changes on the map."),
    ],
    "syllabus_intro": (
        "Eight lessons, in the chapter's order. The first three read Bounded Context, "
        "Continuous Integration and Context Map; the next three the relationship patterns "
        "in pairs and a trio, from the most cooperative to none at all; the last two read "
        "Unifying an Elephant with Choosing Your Model Context Strategy, and "
        "Transformations."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. Each "
        "lesson names its sections and patterns, opens with at most one short quotation, "
        "and sets out the argument in its own words. Where Evans draws on others, as "
        "Facade and Adapter come from Gamma and colleagues, the lesson says so.",
        "Read the patterns as tools and the stories as arguments. Chapter 14's patterns "
        "each state a problem and a resolution; its opening story, its elephant and its "
        "Great Wall argue for them. Each lesson says which it is reading.",
        "Treat each count as a reason to look. The labs count words in glossaries, models "
        "and translators on a map, and translators in a network, on the small models the "
        "lessons state. Which relationship two contexts should have is Evans's judgement "
        "about control, cooperation and integration, and he says politics often decides "
        "it; no count here settles it.",
        "Type your own. Every lesson ends by sending you to a system you know, and the "
        "labs take whatever glossary or map you type. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's examples. The charge in the opening story, the shipping company's "
        "booking, routing and yield analysis, the insurance project, the database story "
        "and the chemistry markup are summarised in the lessons where the argument runs "
        "through them; the labs use a theatre, a school, a clinic, a library, a bakery "
        "and a bike-share of their own.",
        "The book's diagrams, including the navigation map of the integrity patterns, "
        "the translation figures and the chart of the patterns' relative demands. They "
        "are better read in the book.",
        "The full text of Saxe's poem, which the chapter prints at length; the lesson "
        "names it and tells its story.",
        "Team politics and management structure. Evans says they often decide how "
        "contexts are integrated; the lessons say so and count none of it.",
        "Distillation and large-scale structure, which the chapter's close points to. They "
        "are the next two courses.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: false cognates, duplicate concepts and safe terms by comparing the "
        "concept names in glossaries, the models and translators a change reaches by "
        "following a map's relationships under a stated rule for each kind, and "
        "translators by counting pairs. The glossaries and maps are written for these "
        "lessons; none is taken from the book. A count models the situation the lesson "
        "states; it is not a measurement of your project."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
