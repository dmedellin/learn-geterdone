"""Course 6 -- Analysis Patterns, Design Patterns and Refactoring: Chapters 11-13.

Four lessons in one module: two read Chapter 11, Applying Analysis Patterns,
with Martin Fowler's accounting models and Posting Rules as Evans summarises
them; one reads Chapter 12, Relating Design Patterns to the Model (Strategy,
Composite, Why Not Flyweight?); one reads Chapter 13, Refactoring Toward
Deeper Insight. References are to Evans, Domain-Driven Design (Addison-Wesley,
2004), by chapter, section and pattern; PDF pages of the operator's copy
appear only in source comments. The design is docs/domain-driven-design/PLAN.md,
section C, Course 6.
"""

from . import part_a

COURSE = {
    "slug": "ddd-patterns-and-refactoring",
    "title": "Analysis Patterns, Design Patterns and Refactoring",
    "level": "Intermediate",
    "summary": (
        "The three short chapters that close Part III. Chapter 11, Applying Analysis "
        "Patterns, works two examples through Martin Fowler's accounts, entries and "
        "posting rules; Chapter 12, Relating Design Patterns to the Model, reads "
        "Strategy and Composite as concepts in the domain and Flyweight as a pattern "
        "that is not; Chapter 13, Refactoring Toward Deeper Insight, gathers Part III "
        "into an account of when and how a model changes. Each lesson sets out the "
        "argument and counts one consequence on a small model written for it: the "
        "balances and the transactions that do not balance, the entries rules derive, "
        "the decisions a policy moves, and the modules a change request reaches."
    ),
    "blurb": (
        "Read Evans on borrowing models and patterns, and on when to change a model. "
        "Post a week's entries and find the two slips the grand total hides, let rules "
        "derive a levy and watch the cents round, count the decisions a pricing policy "
        "takes out of every method, and count the modules a clinic's change requests "
        "reach before and after its cancellation rule becomes a concept."
    ),
    "key": [
        "an analysis pattern is a starting model",
        "keep the concept a borrowed term names",
        "a domain pattern names a domain concept",
        "refactor on insight, not only smells",
    ],
    "assumes_short": "Supple Design",
    "assumes_long": (
        "Supple Design, for side-effect-free functions, assertions and the supple "
        "design Chapter 13 keeps returning to, and the building blocks of Part II; the "
        "code is short Java, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a short list of records or a short listing, the "
        "counts these chapters argue about in words, and say in Evans's terms what each "
        "count shows and what it leaves to the team and its experts."
    ),
    "outcomes": [
        ("Post entries and check the transactions",
         "Give each account's balance from its entries, name the transactions that do "
         "not net to zero, and say when Fowler's conservation rule applies."),
        ("Fire posting rules by hand",
         "Derive the entries a set of rules posts, with their rounding, and name the "
         "firing mode and the point that starts it."),
        ("Read a design pattern on two levels",
         "Count the decisions a Strategy moves out of a routine, and say what concept "
         "Strategy or Composite names in the domain, and why Flyweight names none."),
        ("Count what a deeper model changes",
         "Count the modules each change request touches before and after a concept is "
         "made explicit, and give Evans's reasons for refactoring and his limits on it."),
    ],
    "syllabus_intro": (
        "Four lessons, in the book's order. The first two read Chapter 11's two "
        "examples and its closing section; the third reads Chapter 12; the fourth reads "
        "Chapter 13, which looks back over all of Part III."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. Each "
        "lesson names its chapter, sections and patterns, opens with one short "
        "quotation, and sets out the argument in its own words. Chapter 11's accounting "
        "patterns are Martin Fowler's, from <em>Analysis Patterns</em> (1997), and "
        "Chapter 12's are from <em>Design Patterns</em> by Gamma, Helm, Johnson and "
        "Vlissides; the lessons say so where they use them.",
        "Read the examples as arguments and the patterns as tools. Evans makes his case "
        "through teams who borrow a pattern and then depart from it; the lessons "
        "summarise those stories in a few sentences and keep their point.",
        "Treat each count as a reason to look. The labs count balances, derived "
        "entries, decision points and modules touched on the lesson's own records and "
        "code: a theatre box office, a bike-share, a clinic. Whether a pattern fits, or "
        "a refactoring is worth it, is a judgement Evans leaves to the team and its "
        "domain experts, and no count settles it.",
        "Use your own records and code. Every lesson ends by sending you to a system "
        "you know, and the labs take whatever you type or paste. Nothing you enter "
        "leaves your browser.",
    ],
    "not_covered": [
        "The book's examples' domains and data: the interest-bearing loans of Chapter "
        "11, the routing and shipment routes of Chapter 12. They are summarised where "
        "the argument runs through them, and the labs use domains of their own.",
        "The book's class and sequence diagrams and the developers' dialogues. They are "
        "named by figure and section and are better read in the book.",
        "Fowler's Analysis Patterns itself, beyond the accounting models Evans "
        "summarises. The lessons do not teach its other chapters.",
        "Running code. The labs read records and listings and never run them; the "
        "exercises ask you to trace a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: balances by adding exact amounts, derived entries by multiplying and "
        "rounding to the cent by the stated rule, decision points by a stated rule, and "
        "modules touched by counting the distinct modules each change lists. The "
        "records and code are written for these lessons; no figure is taken from the "
        "book. A count shows one consequence of one modelling choice; it is not a "
        "verdict on the choice."
    ),
    "lessons": part_a.LESSONS,
}
