"""The Domain-Driven Design path, as data: a read-along of Eric Evans's
Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004).

Nine courses that follow the book's four parts and seventeen chapters, one
lesson per pattern or group of sections. Each lesson sets out the chapter's
argument in its own words, states the pattern as a reader would apply it, and
counts one consequence of the modelling choice on a small model written for the
lesson. The content lives here and only here; scripts/ turns it into pages. The
design is docs/domain-driven-design/PLAN.md.
"""

from . import (
    c1_model_to_work,
    c2_building_blocks,
    c3_life_cycle,
    c4_implicit_concepts,
    c5_supple_design,
    c6_patterns_and_refactoring,
    c7_model_integrity,
    c8_distillation,
    c9_large_scale_structure,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_model_to_work.COURSE,
    c2_building_blocks.COURSE,
    c3_life_cycle.COURSE,
    c4_implicit_concepts.COURSE,
    c5_supple_design.COURSE,
    c6_patterns_and_refactoring.COURSE,
    c7_model_integrity.COURSE,
    c8_distillation.COURSE,
    c9_large_scale_structure.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

# Course 1's author completes this from docs/domain-driven-design/PLAN.md §A,
# field for field as content/enterprise_patterns/__init__.py.
PATH = {
    "slug": "domain-driven-design",
    "title": "Domain-Driven Design, Read Along",
    "level": "Intermediate",
    "level_note": "you can read a short Java class and have worked on a program someone else will change",
    # Backtick runs, key lines and worked lines are read by the code dialect
    # (speech.say_code), as on Code Complete and Enterprise Patterns.
    "speech": "code",
    "tagline": (
        "Eric Evans&rsquo;s <em>Domain-Driven Design</em>, read chapter by chapter and pattern by pattern &mdash; and each modelling choice&rsquo;s consequence counted on a small model: translations a conversation needs, references that bypass a root, edits that break an invariant, modules a change touches, translators a context map costs, effort spent on the core. Nine courses and 53 lessons are available."
    ),
    "description": (
        "The Domain-Driven Design Subject: a read-along of Eric Evans&rsquo;s 2004 book in its own order, from crunching knowledge and the Ubiquitous Language through the building blocks of a model-driven design, the life cycle of a domain object, the refactoring toward deeper insight and supple design, to the strategic design of Part IV: bounded contexts, distillation and large-scale structure. Each lesson sets out a chapter&rsquo;s argument, states the pattern as a reader would apply it, and counts one consequence of the choice on a small model written for the lesson &mdash; the names two audiences give one concept, the candidates a specification refuses, the downstream models an upstream change reaches &mdash; and ends with a model to work by hand. All nine courses and 53 lessons are available."
    ),
    "key": [
        "a single model and language, in the code",
        "translations: pairs of names that differ",
        "outside references go to the root only",
        "a specification admits or names a clause",
        "a change reaches what its relation passes",
        "a count shows a consequence, not a verdict",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else, and the order is the book&rsquo;s. The first course&rsquo;s three ideas &mdash; knowledge crunching, the Ubiquitous Language and Model-Driven Design &mdash; are used in every lesson after it. The building blocks of Part II are the vocabulary Part III refactors with, and Part IV&rsquo;s strategic design is about many models, each built from those blocks."
    ),
    "why_order": [
        "The order is Evans&rsquo;s, and it runs from one model outward. Putting the Domain Model to Work sets out why a team crunches knowledge into a model, speaks it as one language and binds it to the code. The Building Blocks and The Life Cycle of a Domain Object give the parts a model-driven design is built from: layers, entities, value objects, services, modules, aggregates, factories and repositories, with Evans&rsquo;s extended example. Breakthroughs and Implicit Concepts, Supple Design and the course on analysis patterns, design patterns and refactoring are Part III&rsquo;s refactoring toward deeper insight. Maintaining Model Integrity, Distillation and Large-Scale Structure are Part IV&rsquo;s strategic design.",
        "Part I comes first because every later pattern is judged by it. An Entity or a Repository is worth having, in Evans&rsquo;s argument, when it lets the code say what the model says; a reader who meets the building blocks before the Ubiquitous Language reads them as a catalogue of classes.",
        "Part IV comes last because it is about more than one model. Bounded Context, Context Map and the relationships between teams need the reader to know what one model is, and Distillation needs the reader to have seen how a model grows.",
        "The courses can be read separately once the first is read. Maintaining Model Integrity assumes the first course and enough of the second to know what an entity and a module are; Distillation and Large-Scale Structure assume the first and Maintaining Model Integrity.",
    ],
    "prerequisites": [
        "You can read a short Java class. Every snippet is Java 8, at most twenty lines, using classes, interfaces, fields, `if`, loops, `List` and `Map`. A reader who knows C#, Kotlin or TypeScript reads it without trouble.",
        "You have worked on a program someone else will change, or that you changed after someone else wrote it. Evans&rsquo;s argument is about what a design says to the next person who reads it, and it lands best on a reader who has been that person.",
        "No other Subject. <em>Enterprise Application Patterns, Read Along</em> is the closest neighbour: it teaches Layered Architecture, Value Object, Service Layer, Repository and Domain Model from Fowler&rsquo;s side, and the lessons here name it where the two books meet. The arithmetic is counting, sums and shares, and the labs do it.",
        "A copy of the book is strongly recommended. The book is in copyright, so a lesson states each chapter&rsquo;s argument in its own words, points to the chapter, section and pattern by name, and quotes at most a sentence or two. The book&rsquo;s examples are summarised where the argument runs through them; the models and code in the lessons are written for them, in domains of their own.",
        "Some project of your own, or one you know. Every lesson&rsquo;s last step sends you to a model you work on, with a count to make.",
    ],
    # Each path names its own hazard. This one's is that a count of a small
    # model is not a verdict on a modelling choice, which Evans weighs against
    # the domain, the team and the project (PLAN section A).
    "material": (
        "every figure on this path is counted in your browser from the small model a lesson states &mdash; its terms, objects, references, edits, modules and contexts &mdash; and a count shows one consequence of one modelling choice; it is not a verdict on the choice, which depends on the domain, the team and the project."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is counted in your browser from what the lesson states: a translation count is a count over the glossary it lists, a violation is a reference it draws to an object that is not a root, a reach is a walk along the relationships of the context map it gives. The models and code are written for this course; the labs read them and never run them, and nothing you type is sent anywhere. What the labs cannot do is choose a design &mdash; Evans weighs each choice against the domain, the team and the project, and so must you."
    ),
    "courses": COURSES,
}
