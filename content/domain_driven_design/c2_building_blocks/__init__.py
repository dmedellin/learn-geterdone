"""Course 2 -- The Building Blocks of a Model-Driven Design: Chapters 4 and 5.

Seven lessons in two modules: part_a reads Chapter 4, Isolating the Domain
(Layered Architecture and the Smart UI "Anti-Pattern"), and the first three
patterns of Chapter 5, A Model Expressed in Software (Associations, Entities,
Value Objects); part_b reads the rest of Chapter 5 (Services, Modules and
Modeling Paradigms). References are to Eric Evans, Domain-Driven Design:
Tackling Complexity in the Heart of Software (Addison-Wesley, 2004), by
chapter, section and pattern; PDF pages of the operator's copy appear only in
source comments. The design is docs/domain-driven-design/PLAN.md, section C,
Course 2.
"""

from . import part_a, part_b

COURSE = {
    "slug": "ddd-building-blocks",
    "title": "The Building Blocks of a Model-Driven Design",
    "level": "Intermediate",
    "summary": (
        "Chapter 4, Isolating the Domain, and Chapter 5, A Model Expressed in "
        "Software: the opening of Part II, where Evans turns from why a model "
        "should drive the code to the elements the code is built from. Layered "
        "Architecture and the Smart UI that is its honest alternative; then "
        "associations, Entities, Value Objects, Services and Modules, with a "
        "short look at modeling paradigms other than objects. Each lesson sets "
        "out the argument, shows the pattern in a few lines of Java written for "
        "the lesson, and counts one consequence of the choice on a small model of "
        "its own: the dependencies that run up a layering, the places a rule "
        "change touches, the references an association asks you to keep "
        "consistent, the pairs that identity and attributes disagree about, the "
        "holders surprised by a change to a shared value, the uses an operation "
        "drags into an entity, and the dependencies a packaging keeps inside its "
        "modules."
    ),
    "blurb": (
        "Read the chapters where Evans names the building blocks. Find the "
        "dependencies that run up a layering, count the screens a copied rule "
        "makes you edit, simplify a tangle of associations, tell the same patient "
        "from one who only looks alike, see who is surprised when a shared value "
        "changes, move an awkward operation into a service, and package one model "
        "two ways."
    ),
    "key": [
        "isolate the domain in its own layer",
        "Smart UI: a fork, not a halfway house",
        "constrain every association you can",
        "an entity is who, not what",
        "a value is what, and is not changed",
        "a service is an operation, not a thing",
        "modules are part of the model",
    ],
    "assumes_short": "Putting the Domain Model to Work",
    "assumes_long": (
        "Putting the Domain Model to Work, for the Ubiquitous Language and "
        "Model-Driven Design that these building blocks serve; the code is short "
        "Java, and a reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small model written down in front of you, "
        "the counts these chapters make in words, and say in Evans's terms what "
        "each count shows and what it leaves to judgement."
    ),
    "outcomes": [
        ("Check a layering",
         "Assign classes to Evans's four layers, find every dependency that runs "
         "upward, and say how a callback or an observer would turn it round."),
        ("Weigh Smart UI fairly",
         "Count the places a rule change touches when the rule lives in each screen "
         "and when it lives in one domain object, and give Evans's case for when "
         "the Smart UI is still the right choice."),
        ("Constrain associations",
         "Impose a direction, add a qualifier and remove an inessential "
         "association, and count the navigable directions and many ends before "
         "and after."),
        ("Tell entities from values",
         "Say for a pair of objects whether they are the same by identity, by "
         "attributes or both, and predict who sees a change to a shared value "
         "when it is mutable and when it is replaced."),
        ("Place services and modules",
         "Sort operations into application, domain and infrastructure services, "
         "and package one model by concept and by technical tier, counting the "
         "dependencies each keeps inside a module."),
    ],
    "syllabus_intro": (
        "Seven lessons in the book's order. The first two read Chapter 4: Layered "
        "Architecture, and the Smart UI with the other kinds of isolation. The "
        "last five read Chapter 5: Associations, Entities, Value Objects, "
        "Services, and Modules with Modeling Paradigms."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Eric Evans, "
        "<em>Domain-Driven Design: Tackling Complexity in the Heart of "
        "Software</em> (Addison-Wesley, 2004), with models and code written for "
        "these lessons. Each lesson names its chapter, sections and patterns, opens "
        "with at most one short quotation, and sets out the argument in its own "
        "words.",
        "Read each pattern as a tool and its section as an argument. Evans states a "
        "problem, argues it through an example, and then says what to do; each "
        "lesson summarises his example in a few sentences and works its lab on a "
        "different model of its own, a library, a clinic, a bakery or a seed bank.",
        "Treat each count as a reason to look. The labs count one consequence of a "
        "modelling choice on the small model a lesson states: dependencies, places "
        "touched, references, pairs, holders, uses. Whether the choice is right is "
        "Evans's judgement, weighed against the domain, the team and the project; "
        "no count here settles it.",
        "Bring your own model. Every lesson ends by sending you to a system you "
        "know, and the labs take whatever records you type. Nothing you type "
        "leaves your browser.",
    ],
    "not_covered": [
        "The book's examples: the online banking transfer, the presidents, the "
        "brokerage account, the stadium seats, the house plans and the others. "
        "They are summarised where the argument runs through them and are better "
        "read in the book; the labs use domains of their own.",
        "The book's diagrams and code listings. The Java in these lessons is "
        "written for them.",
        "Aggregates, Factories and Repositories, the patterns that manage an "
        "object's life cycle. They are Chapter 6, read in the next course, The "
        "Life Cycle of a Domain Object.",
        "How to map these objects to tables, which Enterprise Application "
        "Patterns teaches pattern by pattern. Where a lesson meets one of its "
        "patterns it names the lesson there once.",
        "Running code. The labs count records you type and never run them, so "
        "they cannot tell you whether a design works; the exercises ask you to "
        "trace a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is counted in your browser from the small "
        "model a lesson states: dependencies by the layers or modules each end is "
        "assigned to, places touched by the elements each change lists, "
        "references by the direction declared on each association, sameness by "
        "comparing identifiers and attributes as typed, and holders by who points "
        "at which value. The models are written for these lessons, and none is "
        "taken from the book. A count shows one consequence of one modelling "
        "choice; it is not a verdict on the choice."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
