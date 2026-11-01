"""Course 8 -- Distillation: Chapter 15 of Evans's Domain-Driven Design.

Five lessons in one module, in the chapter's order: Core Domain with
Choosing the Core, Who Does the Work? and An Escalation of Distillations;
Generic Subdomains with its four options, Generic Doesn't Mean Reusable and
Project Risk Management; Domain Vision Statement and Highlighted Core with the
distillation document; Cohesive Mechanisms; and Segregated Core with Abstract
Core, Deep Models Distill and Choosing Refactoring Targets. References are to
Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/domain-driven-design/PLAN.md, section C, Course 8.
"""

from . import part_a

COURSE = {
    "slug": "ddd-distillation",
    "title": "Distillation",
    "level": "Intermediate",
    "summary": (
        "Chapter 15 of Evans's Domain-Driven Design, Distillation: how a team finds "
        "the part of its model that makes the software worth building, and keeps it "
        "in view. The Core Domain and who should work on it; Generic Subdomains and "
        "the four ways to get one; the Domain Vision Statement and the Highlighted "
        "Core; Cohesive Mechanisms; and the Segregated and Abstract Cores. Each "
        "lesson sets out the chapter's argument and counts one consequence of a "
        "distillation choice on a small model written for the lesson: the share of "
        "effort and of the strongest developers on the core, the weeks a decision to "
        "buy would free, the share of a model a newcomer must read, the modules a "
        "change touches, and the dependencies that cross the core's boundary."
    ),
    "blurb": (
        "Read Evans on finding and protecting the heart of a model. Count where a "
        "bike-share team's weeks and strongest developers go, free weeks by buying "
        "what is generic, flag the core so a newcomer reads a quarter of the model, "
        "move a timetable's interval arithmetic behind one interface, and pull the "
        "core's classes into a module of their own."
    ),
    "key": [
        "the core is what makes it worth building",
        "put the strongest developers on the core",
        "generic: buy, publish, outsource or build",
        "a page that says what the core is for",
        "flag the core so anyone can see it",
        "a mechanism answers what the model asks",
        "the core in a module of its own",
    ],
    "assumes_short": "Maintaining Model Integrity",
    "assumes_long": (
        "Maintaining Model Integrity, for Bounded Contexts and Published Languages, and "
        "the earlier courses' Modules, Intention-Revealing Interfaces and Declarative "
        "Design; the code is short Java, and a reader of any C-family language can "
        "follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a list of a project's parts or a model's classes, "
        "the counts Chapter 15 makes in words, and say in the book's terms what each "
        "count shows and what it leaves to the team's judgement."
    ),
    "outcomes": [
        ("Find where a team's effort goes",
         "Given a project's parts with their kind, weeks and strongest developers, state "
         "the share of the weeks and of the strongest developers on the Core Domain."),
        ("Weigh the four options for a generic part",
         "Give Evans's advantages and drawbacks of buying, adopting a published model, "
         "outsourcing and building in house, and count the weeks each decision frees."),
        ("Make the core visible",
         "Say what belongs in a Domain Vision Statement and a distillation document, "
         "flag a model's core classes, and say which changes call for consultation."),
        ("Separate a mechanism from the model",
         "Move a computation behind an intention-revealing interface, and count the "
         "modules a change to the computation and a change to a rule each touch."),
        ("Segregate and abstract the core",
         "Count the dependencies inside and across modules, and across the core's "
         "boundary, for a model packaged three ways, and give the costs Evans names."),
    ],
    "syllabus_intro": (
        "Five lessons, in the chapter's order and in Evans's escalation of "
        "distillations: from the choice of the core, through the techniques that "
        "change only documents, to those that repackage and then remodel the code."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. Each "
        "lesson names its sections and patterns, opens with at most one short "
        "quotation, and sets out the argument in its own words.",
        "Read the patterns as tools and the stories as evidence. Evans argues Chapter "
        "15 largely from projects he took part in; each lesson summarises the story "
        "its argument runs through, and works its lab on a domain of its own: a "
        "bike-share, a clinic, a school timetable and a seed bank.",
        "Treat each count as a reason to look. The labs count weeks, developers, "
        "classes, modules and dependencies on the small model each lesson states. "
        "What the core is, and whether a distillation is worth its cost, are the "
        "team's judgements, which Evans says evolve with the project; no count here "
        "settles them.",
        "Type your own project. Every lesson ends by sending you to a system you know, "
        "and the labs take whatever parts, classes and dependencies you type. Nothing "
        "you type leaves your browser.",
    ],
    "not_covered": [
        "The book's examples: the syndicated-loan project, the two time-zone projects, "
        "the insurance consortium's model, the organisation chart's graph framework and "
        "the cargo-shipping model that is segregated in Segregated Core. They are "
        "summarised where the argument runs through them and better read in the book.",
        "The book's figures and tables, including the navigation map of the chapter's "
        "patterns and the two sample vision statements. They are pointed to, not "
        "redrawn.",
        "Large-scale structure, which Evans treats as the third strategic principle, "
        "after context and distillation. It is the next course, Large-Scale Structure and "
        "Strategy.",
        "Running code. The labs count what a lesson's table states and never build "
        "or run the software it describes.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: shares of effort by adding developer-weeks, developers by counting "
        "them, modules touched by reading which module holds each element a change "
        "touches, and dependencies by comparing the modules at each end. The projects, "
        "classes and weeks are written for these lessons; none is the book's. A count "
        "models the situation the lesson states; it is not a measurement of your "
        "project, and it is not a verdict on a distillation."
    ),
    "lessons": part_a.LESSONS,
}
