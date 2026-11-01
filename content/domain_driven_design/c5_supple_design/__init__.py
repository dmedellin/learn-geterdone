"""Course 5 -- Supple Design: Chapter 10.

Seven lessons in two modules: part_a reads the chapter's opening and its first
five patterns (Intention-Revealing Interfaces, Side-Effect-Free Functions,
Assertions, Conceptual Contours, Standalone Classes with Closure of
Operations); part_b reads Declarative Design with Extending Specifications in a
Declarative Style, and Angles of Attack. References are to Eric Evans,
Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), by chapter, section and pattern; PDF pages of the
operator's copy appear only in source comments. The design is
docs/domain-driven-design/PLAN.md, section C, Course 5.
"""

from . import part_a, part_b

COURSE = {
    "slug": "ddd-supple-design",
    "title": "Supple Design",
    "level": "Intermediate",
    "summary": (
        "Chapter 10 of Part III, Supple Design: the patterns Evans offers for a design "
        "that developers can understand, combine and change with confidence. "
        "Intention-Revealing Interfaces, Side-Effect-Free Functions and Assertions make "
        "each element say what it means and do only what it says; Conceptual Contours, "
        "Standalone Classes and Closure of Operations decide where the elements divide "
        "and what they depend on; Declarative Design and Angles of Attack show where the "
        "style leads and where to begin. Each lesson sets out the argument, states the "
        "pattern as a reader would apply it, and counts one consequence on a small model "
        "written for the lesson: the names a routine declares, the holders a shared "
        "value surprises, the clause an outcome breaks, the modules a change request "
        "touches, the classes a change reaches, the candidates that separate two rules, "
        "and the dependencies a carved-off subdomain straightens."
    ),
    "blurb": (
        "Read Evans's patterns for a supple design. Read a routine's names against what "
        "they reveal, count who sees a change made through a shared value, check an "
        "outcome against its post-condition, find where change requests land under two "
        "divisions of one model, follow a change through a tangled and a standalone "
        "design, ask whether one rule subsumes another, and carve a subdomain off a "
        "tangled model."
    ),
    "key": [
        "name the effect and purpose, not the means",
        "logic in functions; commands kept simple",
        "state post-conditions and invariants",
        "divide along the domain's contours",
        "cut every dependency not basic to a concept",
        "combine rules declaratively",
        "carve off a subdomain; use a formalism",
    ],
    "assumes_short": "Breakthroughs and Implicit Concepts",
    "assumes_long": (
        "Breakthroughs and Implicit Concepts, for making implicit concepts explicit and "
        "for the Specification pattern, and The Building Blocks of a Model-Driven Design, "
        "for entities and value objects; the code is short Java 8, and a reader of any "
        "C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a short listing or a small model, the counts this "
        "chapter makes in words, and say in Evans's terms what each count shows and what "
        "it leaves to judgement."
    ),
    "outcomes": [
        ("Read an interface as its client",
         "List the names a routine declares, mark the short ones, and rename an operation "
         "and its arguments to state effect and purpose in the domain's words."),
        ("Make consequences predictable",
         "Split an operation into a function and a simple command, count the holders a "
         "change to a shared value reaches, and check an outcome against a post-condition "
         "and an invariant."),
        ("Divide a design along its contours",
         "Count the modules each change request touches under two divisions, and say what "
         "a spreading change suggests about the model."),
        ("Reduce what a class depends on",
         "List a class's dependencies directly and in all, find the standalone classes, and "
         "tell a closed operation from one that is halfway."),
        ("Combine and compare rules",
         "Decide whether one specification subsumes another, find a separating candidate, "
         "and count a model's dependencies before and after a subdomain is carved off."),
    ],
    "syllabus_intro": (
        "Seven lessons, in the chapter's order. The first three make each element "
        "readable and safe to use: Intention-Revealing Interfaces, Side-Effect-Free "
        "Functions and Assertions. The next two decide how elements divide and connect: "
        "Conceptual Contours, then Standalone Classes with Closure of Operations. The last "
        "two read Declarative Design, with the extended Specification, and Angles of "
        "Attack, with its Shares Math example."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of Software</em> "
        "(Addison-Wesley, 2004), with models and code written for these lessons. Each "
        "lesson names its sections and patterns, opens with at most one short quotation, "
        "and sets out the argument in its own words. Where Evans draws on another author, "
        "as he does on Kent Beck, Bertrand Meyer, Martin Fowler and Ward Cunningham, the "
        "lesson says so.",
        "Read the patterns as tools and the chapter as an argument. Evans offers these "
        "patterns as ones that tend to make a design supple where they fit, not as a "
        "formula, and he says he has never seen a large program supple throughout. Each "
        "lesson states the pattern as you would apply it and the limits he puts on it.",
        "Treat each count as a reason to look. The labs count one consequence of one "
        "modelling choice on the model the lesson states: names, holders, clauses, module "
        "touches, classes reached, candidates and dependencies. Whether a name reveals "
        "intention, or a division follows the domain's contours, is a reading of the "
        "domain, and no count here settles it.",
        "Bring your own model. Every lesson ends by sending you to a system you know, and "
        "the labs take whatever you type or paste. Nothing you enter leaves your browser.",
    ],
    "not_covered": [
        "The book's paint-mixing example, which runs through the first patterns, and its "
        "accruals, warehouse and syndicated loan examples. They are summarised where the "
        "argument runs through them and better read in the book; the lessons' models use "
        "domains of their own.",
        "The book's listings and diagrams, including the composite specification and the "
        "Share Pie classes. The lessons' Java is written for them.",
        "Chapter 15's treatment of subdomains and cohesive mechanisms, which Angles of "
        "Attack points to. It is read in the course Distillation.",
        "Running code. The labs read names, records and rules and never run a program, so "
        "they cannot tell you whether an operation really has no side effect or meets its "
        "post-condition; the exercises ask you to check a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: declared names by the rule beside the listing, holders and changes from "
        "the records given, clauses by evaluating the stated specification on each "
        "candidate, module touches and dependencies by counting the records against the "
        "packagings given, and classes reached by following the dependencies listed. The "
        "models and code are written for these lessons. A count shows one consequence of "
        "one modelling choice; it is not a verdict on the choice, which depends on the "
        "domain, the team and the project."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
