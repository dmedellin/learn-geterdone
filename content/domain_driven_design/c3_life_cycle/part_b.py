"""The Life Cycle of a Domain Object, lessons 5-6 -- Chapter 7.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), Chapter 7, Using the Language: An Extended Example.
The book's cargo-shipping example is summarised in prose, section by section;
the labs work a theatre box office's model written for these lessons, so that
the same decisions are taken on a domain of the lesson's own. Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter and
section. Every quotation is copied from that copy and checked with quotes.py.
None of the book's listings, diagrams or example data is reproduced. The design
is docs/domain-driven-design/PLAN.md, section C, Course 3.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# 3.5 The box office's Booking root, with "book again" (written for the lesson).
BOOKING_ROOT = """public class Booking {
    private final BookingNumber number;
    private final Customer customer;         // another aggregate's root
    private final List<Ticket> tickets = new ArrayList<>();

    Booking(BookingNumber number, Customer customer) {
        this.number = number;
        this.customer = customer;
    }

    // Book again: same customer, same seats, a new performance and number.
    public Booking repeatFor(Performance next, BookingNumber newNumber) {
        Booking copy = new Booking(newNumber, customer);
        for (Ticket t : tickets) {
            copy.tickets.add(new Ticket(copy.tickets.size() + 1, next,
                    t.seat(), next.priceFor(t.seat())));
        }
        return copy;
    }
}"""


# ---------------------------------------------------------------- lab data

# 3.5: the theatre's objects, a first draft and the boundaries drawn.
_THEATRE_OBJECTS = (
    "Customer, customer, yes; Booking, booking, yes; Ticket, booking, no; "
    "Performance, performance, yes; Venue, venue, yes; Seat, venue, no"
)
_THEATRE_DRAFT_REFS = (
    "Booking, Customer; Booking, Ticket; Ticket, Performance; Ticket, Seat; "
    "Performance, Venue; Venue, Seat; Scanner, Ticket"
)
_THEATRE_REFS = (
    "Booking, Customer; Booking, Ticket; Ticket, Performance; "
    "Performance, Venue; Venue, Seat; Scanner, Booking"
)

# 3.6: the same model packaged by pattern (module) and by concept (module2).
_THEATRE_ELEMENTS = (
    "Customer, entities, customers; ContactDetails, values, customers; "
    "CustomerRepository, repositories, customers; "
    "Venue, entities, venues; Seat, entities, venues; SeatRef, values, venues; "
    "Performance, entities, programme; PerformanceRepository, repositories, programme; "
    "Booking, entities, sales; Ticket, entities, sales; Price, values, sales; "
    "BookingRepository, repositories, sales; PricingService, services, sales"
)
_THEATRE_DEPS = (
    "Customer, ContactDetails; CustomerRepository, Customer; Venue, Seat; "
    "Seat, SeatRef; Performance, Venue; PerformanceRepository, Performance; "
    "Booking, Customer; Booking, Ticket; Ticket, Performance; Ticket, SeatRef; "
    "Ticket, Price; BookingRepository, Booking; PricingService, Performance; "
    "PricingService, Price"
)
_QUOTA_ELEMENTS = (
    _THEATRE_ELEMENTS
    + "; QuotaChecker, services, sales; AgencyClient, services, sales"
)
_QUOTA_DEPS = _THEATRE_DEPS + "; QuotaChecker, Performance; QuotaChecker, AgencyClient"


LESSONS = [
    # ---------------------------------------------------------------- 05
    # Chapter 7 (PDF pp. 96-106 of the operator's copy): opening and
    # Introducing the System (pp. 96-98), Isolating the Domain (p. 98),
    # Distinguishing Entities and Value Objects (pp. 98-100), Designing
    # Associations (pp. 100-101), Aggregate Boundaries (pp. 101-102), Selecting
    # Repositories (pp. 102-103), Walking Through Scenarios (pp. 103-104),
    # Object Creation (pp. 104-106).
    # Quote: PDF p. 96 of the operator's copy, 23 words, quotes.py OK.
    # Lesson total: 23 words.
    {
        "slug": "an-extended-example",
        "title": "Using the Language: An Extended Example",
        "module": "Chapter 7 · Using the Language: An Extended Example",
        "one_line": "Part II's patterns applied one after another to one model: layers, entities and values, associations, aggregates, repositories, scenarios and creation.",
        "summary": (
            "Chapter 7 takes one model through every building block in turn. Read "
            "the order in which Evans makes the decisions on his shipping example, "
            "then take the same decisions on a theatre box office written for the "
            "lesson, and count what drawing its aggregate boundaries changes."
        ),
        "key": [
            "isolate the domain first",
            "sort entities from values",
            "give associations a direction",
            "draw boundaries round roots",
            "repositories from requirements",
            "walk scenarios to test it all",
        ],
        "key_label": "The extended example in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's in Chapter 7; "
            "the third is the Gang of Four's pattern that he uses in one scenario."
        ),
        "concepts": [
            ("Application class",
             "A class in the application layer that coordinates one function a user "
             "asks for, such as taking a booking. It asks the domain layer the "
             "questions and does not work out the answers itself."),
            ("Scenario",
             "A sample feature walked through the design to check the decisions "
             "made so far: which objects take part, which rules apply, and whether "
             "anything outside an aggregate is touched."),
            ("Prototype",
             "A design pattern from Gamma and colleagues: a new object is made by "
             "copying an existing one. On an aggregate, every part inside the "
             "boundary needs its own decision about what is copied."),
        ],
        "read_title": "The book's example in order, then the same decisions on our own",
        "read_intro": (
            "Read Chapter 7 from Introducing the System through Object Creation in "
            "your own copy first. The lesson summarises the shipping example; the "
            "lab works a different domain."
        ),
        "body": [
            ("p", "&ldquo;In the earlier examples, the patterns were mostly applied one "
                  "at a time, but on a real project you have to combine them.&rdquo; "
                  "So Evans opens Chapter 7, Using the Language: An Extended Example. "
                  "It follows an imagined team through one model, a cargo shipper's, "
                  "with three requirements: track the handling of each customer's "
                  "cargo, book cargo in advance, and invoice automatically when the "
                  "cargo reaches a certain point. He starts from a fairly mature "
                  "model and changes it only to connect it to an implementation, "
                  "leaving discovery to Part III."),
            ("p", "The decisions come in a fixed order, and the order is the lesson. "
                  "First the domain is isolated: three application classes, a "
                  "tracking query, a booking application and an incident-logging "
                  "application, act as coordinators and leave the answers to the "
                  "domain layer. Then each object is sorted. Customers, cargoes, "
                  "handling events, carrier movements and locations are entities, "
                  "each with its own identity scheme, two of them (the customer's and "
                  "the handling event's) settled by asking a domain expert; the "
                  "delivery history is an entity whose identity is borrowed from its "
                  "cargo; the delivery specification and the customer's role are "
                  "values."),
            ("p", "Next, associations get directions. The customer does not hold every "
                  "cargo it has shipped, since a query can find them; handling events "
                  "point to carrier movements and not back, because the business "
                  "tracks cargo, not ships' inventories; and one cycle, cargo to "
                  "history to events and back, is kept with its cost noted. Then "
                  "boundaries. Customer, location and carrier movement are shared "
                  "and become roots of their own; the cargo's aggregate takes in the "
                  "history and the specification; and the handling event becomes a "
                  "root too, because finding the events for a carrier movement gives "
                  "it meaning apart from the cargo. Repositories are then chosen among "
                  "the roots by the requirements: four, and none yet for "
                  "handling events."),
            ("p", "Scenarios check the result. Changing a cargo's destination means "
                  "replacing one value with another. Repeat business, a new cargo "
                  "copied from an old one by Prototype, means deciding part by part: "
                  "a fresh empty history, a copy of the map of customer roles that "
                  "still points at the same customers, and a new tracking number, so "
                  "that nothing outside the boundary is touched. Object Creation then "
                  "writes constructors that leave identity intact and factory methods "
                  "for each kind of handling event, and runs into the cycle: adding an "
                  "event means adding it to the cargo's history in the same "
                  "transaction. The next lesson reads Evans's way out."),
            ("p", "Now the same order on a model of our own, a theatre box office. "
                  "Three requirements: sell seats for a performance, change or cancel "
                  "a booking, and admit ticket holders at the door. Three application "
                  "classes coordinate them: the box office, the door scanner and the "
                  "sales report. Customers, bookings, performances and venues are "
                  "entities, the customer known by the box office's customer number "
                  "and a booking by the number printed on it. A seat is an entity "
                  "known by row and number only within its venue, and a ticket is "
                  "known only within its booking. A price and a reference to a seat "
                  "by row and number are values."),
            ("p", "Associations get directions as Evans's do. A booking knows its "
                  "customer; the customer does not hold its bookings, which a "
                  "repository query can find. A ticket knows its performance, and a "
                  "performance its venue. The `Booking` root below holds its customer "
                  "and its tickets, and its <em>book again</em> method is the "
                  "Prototype scenario on this model: a new number, the same customer "
                  "root, and new tickets for the next performance at the same seats, "
                  "priced afresh."),
            ("code", _lines(BOOKING_ROOT)),
            ("p", "The lab checks the boundaries. The preset <code>first-draft</code> "
                  "is the model before anyone drew them: the ticket holds a reference "
                  "to the seat object in the venue, and the door scanner keeps the "
                  "tickets it has scanned. Over 4 aggregates and 6 objects the lab "
                  "counts 5 references that cross a boundary, and lists 2 that reach "
                  "a non-root: ticket to seat, and scanner to ticket."),
            ("p", "The preset <code>boundaries-drawn</code> fixes both. The ticket "
                  "holds the seat as a value, row and number, and reaches the venue "
                  "through its performance; the scanner holds the booking and asks it "
                  "for its tickets during one scan. Now 4 references cross a "
                  "boundary, every one onto a root, and 0 are violations. Repositories "
                  "follow from the requirements: the box office must find customers, "
                  "performances and bookings, so three; the venue is reached from its "
                  "performance and needs none."),
            ("p", "On <code>cancel-booking</code> the lab deletes the booking: 2 "
                  "objects go, the booking and its ticket, and 1 reference is left "
                  "dangling, the scanner's. The scanner must therefore drop a "
                  "cancelled booking, which is a rule across aggregates that the "
                  "model has to state. The book-again copy, by contrast, touches "
                  "nothing outside the booking's boundary, just as Evans's "
                  "repeat-business copy did."),
            ("h3", "Exercise"),
            ("ul", [
                "Objects (object, aggregate, root): Customer, customer, yes; Order, "
                "order, yes; OrderLine, order, no; Product, product, yes; Oven, oven, "
                "yes; Tray, oven, no.",
                "References (from, to): Order, Customer; Order, OrderLine; OrderLine, "
                "Product; OrderLine, Tray; Oven, Tray; Dispatch, Order.",
            ]),
            ("p", "A bakery's orders, with the dispatch board as an outside holder. "
                  "Count the references that cross a boundary and those that reach a "
                  "non-root, say what deleting an order removes and leaves dangling, "
                  "and name the one change that would leave no violation. Check it in "
                  "the lab."),
            ("p", "The design works, but it already has one awkward transaction. The "
                  "next lesson, Refactoring the Example, Modules and a New Feature, "
                  "reads how Evans removes it and what happens when a second system "
                  "has to be joined to the first."),
        ],
        "lab": ("dddkit", {
            "mode": "aggregate",
            "view": "boundary",
            "preset": "first-draft",
            "presets": [
                {"id": "first-draft",
                 "label": "A box office before the boundaries are drawn",
                 "objects": _THEATRE_OBJECTS,
                 "refs": _THEATRE_DRAFT_REFS,
                 "expect": {"dgrAggregates": "4: customer, booking, performance, venue", "dgrObjects": "6", "dgrCrossing": "5", "dgrViolations": "2: Ticket → Seat, Scanner → Ticket", "dgrRemoves": "no delete given", "dgrDangling": "no delete given"}},
                {"id": "boundaries-drawn",
                 "label": "The same model with every crossing on a root",
                 "objects": _THEATRE_OBJECTS,
                 "refs": _THEATRE_REFS,
                 "expect": {"dgrAggregates": "4: customer, booking, performance, venue", "dgrObjects": "6", "dgrCrossing": "4", "dgrViolations": "0: none", "dgrRemoves": "no delete given", "dgrDangling": "no delete given"}},
                {"id": "cancel-booking",
                 "label": "Cancel a booking",
                 "objects": _THEATRE_OBJECTS,
                 "refs": _THEATRE_REFS,
                 "delete": "Booking",
                 "expect": {"dgrAggregates": "4: customer, booking, performance, venue", "dgrObjects": "6", "dgrCrossing": "4", "dgrViolations": "0: none", "dgrRemoves": "2: Booking, Ticket", "dgrDangling": "1: Scanner → Booking"}},
            ],
            "panel_title": "A box office's aggregates, before and after",
        }),
        "steps_title": "Taking the decisions in Evans's order",
        "steps_intro": "Five steps, the last of them on a model of your own.",
        "steps": [
            ("Isolate the domain",
             "Name the application functions and give each a coordinating class that "
             "asks the domain layer and works nothing out itself."),
            ("Sort entities from values",
             "For each object, ask whether the users care which one it is. If they "
             "do, find out from the experts how it is told apart."),
            ("Direct the associations",
             "Make each association one-way unless the business needs both, and "
             "replace a large collection by a repository query where you can."),
            ("Draw boundaries and choose repositories",
             "Make shared objects roots, gather what exists only for a root inside "
             "its boundary, and give a repository only to the roots a requirement "
             "must find."),
            ("Walk a scenario on your own model",
             "Pick a feature of a system you know and walk it through your "
             "aggregates. Count the objects outside the boundary it touches; if the "
             "count is not zero, write down which boundary you would move."),
        ],
        "worked": {
            "title": "The box office's first draft",
            "intro": [
                "Count the crossings in <code>first-draft</code>.",
            ],
            "lines": [
                "booking to ticket: inside",
                "venue to seat: inside",
                "booking to customer: a root",
                "ticket to performance: a root",
                "performance to venue: a root",
                "ticket to seat: not a root",
                "scanner to ticket: not a root",
                "5 crossings, 2 of them violations",
            ],
            "after": [
                "Holding the seat as a value removes one crossing altogether, and "
                "pointing the scanner at the booking turns the other into a crossing "
                "onto a root: 4 crossings and 0 violations in "
                "<code>boundaries-drawn</code>.",
            ],
        },
        "quiz_title": "The order of decisions, and the boundaries counted",
        "quiz": [
            {"q": "In the exercise's bakery model, how many references cross a "
                  "boundary and how many reach a non-root, and what does deleting the "
                  "order remove?",
             "a": ["4 cross, 2 reach a non-root; the order and its line go",
                   "4 cross, 1 reaches a non-root; the order and its line go",
                   "3 cross, 1 reaches a non-root; only the order goes",
                   "6 cross, 1 reaches a non-root; the order, its line and the tray go"],
             "c": 1,
             "why": "Order to OrderLine and Oven to Tray stay inside. Order to "
                    "Customer, OrderLine to Product and Dispatch to Order cross onto "
                    "roots; OrderLine to Tray crosses onto an inner object of the "
                    "oven's aggregate. That is 4 crossings, 1 violation. Deleting the "
                    "order removes Order and OrderLine, 2 objects, and leaves 1 "
                    "reference dangling, the dispatch board's. Pointing the line at "
                    "the oven, or holding the tray's number as a value, leaves no "
                    "violation."},
            {"q": "In Evans's shipping example, why does the handling event become "
                  "the root of its own aggregate rather than sit inside the cargo's?",
             "a": ["Because it is a value object",
                   "Because finding the events for a carrier movement gives handling "
                   "meaning apart from the cargo",
                   "Because the customer holds a reference to it",
                   "Because it has no identity"],
             "c": 1,
             "why": "Evans considers two queries for handling events. The one local to "
                    "a cargo's history could stay inside; the one that finds the events "
                    "for a carrier movement shows the event matters on its own, so it "
                    "is made a root. It is an entity, with an identity made of the "
                    "cargo, the time and the type."},
            {"q": "How does Evans decide which aggregate roots get a repository in "
                  "the example?",
             "a": ["Every root gets one",
                   "Only the roots stored in the database",
                   "Only the roots with automatically generated identities",
                   "From the application requirements: a root gets one if a function "
                   "must find it"],
             "c": 3,
             "why": "Of five roots, four get repositories because the booking and "
                    "logging functions must look them up; the handling event gets none "
                    "at first, since the history holds its events and nobody yet asks "
                    "what is loaded on a carrier movement. Either reason could change."},
            {"q": "In the repeat-business scenario, what happens to the customers the "
                  "old cargo referred to?",
             "a": ["They are copied, so that the new cargo has its own customers",
                   "The new cargo refers to the same customer objects, since they lie "
                   "outside its boundary",
                   "They are dropped, and the user enters them again",
                   "They are replaced by values holding the customers' names"],
             "c": 1,
             "why": "The map of roles is copied with its keys, but the customers are "
                    "entities outside the cargo's aggregate, so the copy points at the "
                    "same ones. Copying them would create false duplicates of real "
                    "customers."},
        ],
        "mistakes": [
            ("Expecting the extended example to show how the model was discovered",
             "Evans says at the start that he begins from a fairly mature model and "
             "changes it only to connect it with an implementation; discovery is "
             "Part III's subject. The chapter shows the building blocks combined, "
             "not knowledge crunching."),
            ("Giving every aggregate root a repository because it is a root",
             "Being a root makes an object eligible for a repository, not entitled to "
             "one. In the example the handling event, a root, has none until a "
             "requirement needs it; on the lesson's illustration the venue is reached "
             "from its performance and gets none."),
            ("Copying an aggregate by copying everything it refers to",
             "A Prototype copy of an aggregate copies what is inside the boundary, "
             "with a decision for each part, and keeps references to the roots "
             "outside it. The lesson's book-again method makes new tickets and keeps "
             "the same customer."),
        ],
        "standard": (
            "Finish when you can take Chapter 7's decisions on a model of your own.",
            "Given a small model, sort its objects, direct its associations, draw "
            "aggregate boundaries, count the references that reach past a root, and "
            "say which roots need repositories and why."
        ),
        "note": (
            "The lab counts references against the boundaries you draw; it cannot "
            "say whether an object should be an entity or a value, or which "
            "requirement needs a repository. Those are the decisions the chapter "
            "makes by asking the experts and walking scenarios, and the lab can "
            "only check that the result is consistent."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Chapter 7 (PDF pp. 106-114 of the operator's copy): Pause for
    # Refactoring (pp. 106-108), Modules in the Shipping Model (pp. 108-110),
    # Introducing a New Feature: Allocation Checking, Connecting the Two
    # Systems, Enhancing the Model with Fowler's Enterprise Segment,
    # Performance Tuning (pp. 110-113), A Final Look (pp. 113-114).
    # Quote: PDF p. 108 of the operator's copy, 26 words, quotes.py OK.
    # Lesson total: 26 words.
    {
        "slug": "refactoring-the-example-and-modules",
        "title": "Refactoring the Example, Modules and a New Feature",
        "module": "Chapter 7 · Using the Language: An Extended Example",
        "one_line": "A collection replaced by a query, modules that follow concepts instead of patterns, and a second system joined through a translating service.",
        "summary": (
            "The second half of Chapter 7. Read how Evans redesigns the cargo's "
            "aggregate to remove a contended transaction, why he rejects packaging "
            "by pattern, and how he joins a sales system through a translating "
            "service; then package the box office's model by pattern and by concept "
            "and count the dependencies inside and across modules."
        ),
        "key": [
            "a query can replace a collection",
            "change stays inside a boundary",
            "package by concept, not by pattern",
            "module names join the language",
            "translate at the edge of the model",
            "name a service for its job",
        ],
        "key_label": "The example's second half in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is Evans's for a module, from "
            "Chapter 5; the second is the lab's; the third is Chapter 14's, which "
            "this chapter uses ahead of its full treatment."
        ),
        "concepts": [
            ("Module",
             "A named group of model elements, a package in Java. Evans counts its "
             "name as part of the language and wants each to hold concepts that "
             "belong together."),
            ("Dependency inside or across",
             "A dependency from one element to another is inside if both are in the "
             "same module and across if not. The share inside is the lab's measure "
             "of how far a packaging keeps related elements together."),
            ("Anticorruption Layer",
             "A layer that translates between this model and another system's, so "
             "that the other system's design does not leak in. Here it is one "
             "class, named for its job, implementing a service for each function "
             "the feature needs."),
        ],
        "read_title": "The chapter's second half, then two packagings counted",
        "read_intro": (
            "Read Chapter 7 from Pause for Refactoring to A Final Look in your own "
            "copy first."
        ),
        "body": [
            ("p", "&ldquo;The packages tell a story, but it is not the story of "
                  "shipping; it is the story of what the developer was reading at "
                  "the time.&rdquo; Evans's verdict on one way of packaging his "
                  "shipping model comes in the second half of Chapter 7, which "
                  "changes a working design three times: once to remove contention, "
                  "once to package it, and once to add a feature that depends on "
                  "another system."),
            ("p", "Pause for Refactoring takes up the awkward transaction the last "
                  "lesson ended on. Recording a handling event also updates the "
                  "cargo's delivery history, so it involves the cargo's aggregate, "
                  "and it can fail or wait if someone else is editing that cargo; yet "
                  "logging an event is quick operational work that ought not to "
                  "contend. Evans replaces the history's collection with a query on a "
                  "new handling-event repository. The event is then added inside its "
                  "own aggregate alone, the history holds nothing persistent and can "
                  "be derived when asked for, and the cycle stops being hard to "
                  "maintain."),
            ("p", "He is careful about the cost. On an object database, following a "
                  "collection is probably faster than a query, and if users list "
                  "whole histories often, the collection may win; the extra query "
                  "about carrier movements has not even been asked for. What he "
                  "stresses is that both designs express the same model: because the "
                  "values, entities and aggregates were drawn, the whole change "
                  "stayed within the cargo's boundary plus one new repository, and "
                  "the handling event itself was not redesigned."),
            ("p", "Modules in the Shipping Model looks at a larger part of the model. "
                  "One packaging, by an imagined enthusiastic reader of the book, "
                  "puts entities in one module, values in another and services in a "
                  "third. Unrelated objects are crammed together, associations run "
                  "between every pair of modules, and the packages describe the book "
                  "rather than the business. Evans adds that splitting stored objects "
                  "from short-lived ones, or any other tidy scheme that ignores what "
                  "the objects mean, is the same mistake; the previous "
                  "course's Modules and Modeling Paradigms reads that pitfall "
                  "in Chapter 5. His alternative groups the model by broad concepts, "
                  "customers, shipping operations and billing, whose names tell the "
                  "company's story and join the team's language."),
            ("p", "Introducing a New Feature joins a second system. The sales "
                  "division keeps allocations, how much of each kind of cargo it will "
                  "try to book, in its own software, and wants each new booking "
                  "checked against them. Evans will not let the booking application "
                  "talk to that system's design directly. He writes one translating "
                  "class, an Anticorruption Layer in the terms of Chapter 14, that "
                  "exposes only what the booking needs, and he names it for its "
                  "responsibility, an allocation checker, rather than for the system "
                  "it talks to. The kind of cargo comes from Fowler's Enterprise "
                  "Segment, an analysis pattern, added to the model as a value."),
            ("p", "Two refinements finish it. The rule that accepts a booking, "
                  "allocated space against space booked plus the new cargo, is domain "
                  "logic and moves out of the booking application into the checker, "
                  "which also derives the segment. A cache of the segment rules beside "
                  "the checker could halve the messages to the remote system, at the "
                  "cost of keeping copied data current. A Final Look asks why the "
                  "cargo should not derive its own segment, and answers that segments "
                  "are drawn for business purposes, differently for different ones, "
                  "so the rules belong with the object that knows them."),
            ("p", "Now the box office's model, packaged two ways. By pattern: "
                  "entities, values, repositories and services. By concept: "
                  "customers, venues, programme and sales. Thirteen elements and 14 "
                  "dependencies:"),
            ("ul", [
                "customers: Customer, ContactDetails, CustomerRepository",
                "venues: Venue, Seat, SeatRef",
                "programme: Performance, PerformanceRepository",
                "sales: Booking, Ticket, Price, BookingRepository, PricingService",
                "dependencies: each class on what it holds or uses, as listed in "
                "the lab",
            ]),
            ("p", "On <code>two-packagings</code> both packagings have 4 modules. By "
                  "pattern, 5 of the 14 dependencies are inside a module and 9 cross, "
                  "a share inside of 5/14; the most coupled pair is entities and "
                  "values, with 4 dependencies between them. By concept, 9 are "
                  "inside and 5 cross, a share of 9/14, and the most coupled pair is "
                  "programme and sales, with 2. Neither packaging has a cycle between "
                  "modules."),
            ("p", "The preset <code>quota-feature</code> adds the theatre's new "
                  "feature, a ticket agency that sells part of each performance. A "
                  "`QuotaChecker` service translates between the box office's "
                  "performances and the agency's sales channels, and an "
                  "`AgencyClient` behind it handles the messages, as Evans's checker "
                  "hides its lower-level interface. With 16 dependencies, by pattern "
                  "6 are inside and 10 cross, 3/8; by concept 10 are inside and 6 "
                  "cross, 5/8, and programme and sales now share 3."),
            ("p", "What the counts show is where each packaging puts related elements, "
                  "not which packaging is right. By pattern, the dependencies follow "
                  "the book's categories, so most dependencies, 9 of the 14, run "
                  "between modules. By concept, the dependencies that cross are the "
                  "ones the business has, sales depending on the programme, and a "
                  "reader can tell the theatre's story from the module names. A "
                  "different reading of the domain could draw the concepts "
                  "differently, as Evans says of his own."),
            ("h3", "Exercise"),
            ("ul", [
                "Elements (element, by pattern, by concept): Accession, entities, "
                "collection; CollectorTrip, entities, collection; SiteRef, values, "
                "collection; GerminationTest, entities, testing; TestResult, values, "
                "testing; AccessionRepository, repositories, collection; "
                "TestScheduler, services, testing.",
                "Dependencies (from, to): Accession, CollectorTrip; Accession, "
                "SiteRef; CollectorTrip, SiteRef; GerminationTest, Accession; "
                "GerminationTest, TestResult; AccessionRepository, Accession; "
                "TestScheduler, GerminationTest; TestScheduler, AccessionRepository.",
            ]),
            ("p", "A seed bank's model, packaged both ways. For each packaging, count "
                  "the dependencies inside a module and across, and give the share "
                  "inside. Check your counts in the lab."),
            ("p", "That ends Part II. The next course, Breakthroughs and Implicit "
                  "Concepts, begins Part III with its first lesson, Breakthrough: "
                  "what happens when continuous refactoring of a model like this one "
                  "opens the way to a deeper one."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "cohesion",
            "packagings": 2,
            "names": ["by pattern", "by concept"],
            "preset": "two-packagings",
            "presets": [
                {"id": "two-packagings",
                 "label": "The box office by pattern and by concept",
                 "elements": _THEATRE_ELEMENTS,
                 "deps": _THEATRE_DEPS,
                 "expect": {"dmoModules": "4", "dmoInside": "5", "dmoAcross": "9", "dmoShare": "5/14 ≈ 35.7%", "dmoCycles": "0: none", "dmoPair": "entities and values: 4", "dmoModules2": "4", "dmoInside2": "9", "dmoAcross2": "5", "dmoShare2": "9/14 ≈ 64.3%", "dmoCycles2": "0: none", "dmoPair2": "programme and sales: 2"}},
                {"id": "quota-feature",
                 "label": "With the agency's quota checker added",
                 "elements": _QUOTA_ELEMENTS,
                 "deps": _QUOTA_DEPS,
                 "expect": {"dmoModules": "4", "dmoInside": "6", "dmoAcross": "10", "dmoShare": "3/8 = 37.5%", "dmoCycles": "0: none", "dmoPair": "entities and values: 4", "dmoModules2": "4", "dmoInside2": "10", "dmoAcross2": "6", "dmoShare2": "5/8 = 62.5%", "dmoCycles2": "0: none", "dmoPair2": "programme and sales: 3"}},
            ],
            "panel_title": "One model, packaged by pattern and by concept",
        }),
        "steps_title": "Packaging a model by its concepts",
        "steps_intro": "Four steps, the last of them on a model of your own.",
        "steps": [
            ("List the elements and their dependencies",
             "Write each class with the classes it holds or calls; a dependency runs "
             "from the user to the used."),
            ("Group by concept",
             "Put together the elements a domain expert would talk about together, "
             "and name each group with a word the experts use."),
            ("Count both packagings",
             "For each packaging, mark every dependency inside or across, and find "
             "the pair of modules with the most dependencies between them."),
            ("Do it on your own code",
             "Take one package of a system you know that is named for a technical "
             "category, such as model, dto or service. Regroup its classes by "
             "concept, count the dependencies across modules before and after, and "
             "write down the module names you chose."),
        ],
        "worked": {
            "title": "The box office by pattern",
            "intro": [
                "Count <code>two-packagings</code> by pattern.",
            ],
            "lines": [
                "inside entities: venue to seat",
                "performance to venue, booking to customer",
                "booking to ticket, ticket to performance",
                "5 inside, all among entities",
                "entities to values: 4",
                "repositories to entities: 3",
                "services: 1 to entities, 1 to values",
                "9 across, share inside 5/14",
            ],
            "after": [
                "Every dependency inside a module is between two entities, which "
                "share nothing but a category. By concept, the 9 inside dependencies "
                "are within customers, venues, programme and sales, and the 5 across "
                "are the business's own links.",
            ],
        },
        "quiz_title": "Refactoring, packaging and the translating service",
        "quiz": [
            {"q": "In the exercise's seed-bank model, how many dependencies are "
                  "inside a module by pattern, and how many by concept?",
             "a": ["6 by pattern, 2 by concept",
                   "3 by pattern, 6 by concept",
                   "2 by pattern, 6 by concept",
                   "2 by pattern, 7 by concept"],
             "c": 2,
             "why": "By pattern, only Accession to CollectorTrip and GerminationTest "
                    "to Accession join two entities; the other 6 cross, a share inside "
                    "of 2/8 = 1/4. By concept, everything stays in collection or "
                    "testing except GerminationTest to Accession and TestScheduler to "
                    "AccessionRepository, so 6 are inside and 2 cross, a share of "
                    "6/8 = 3/4."},
            {"q": "In Pause for Refactoring, what does Evans change so that a "
                  "handling event can be recorded without contending with the cargo?",
             "a": ["He locks the cargo for a shorter time",
                   "He moves the handling event inside the cargo's aggregate",
                   "He has the cargo cache its latest handling event",
                   "He replaces the delivery history's collection of events with a "
                   "query on a handling-event repository"],
             "c": 3,
             "why": "With the collection gone, adding an event touches only the "
                    "event's own aggregate, and the delivery history can be derived "
                    "whenever a question needs it. A cached last event would be one "
                    "more copy inside the cargo to keep in step, the contention the "
                    "change removes."},
            {"q": "Why does Evans name the translating class for the allocation "
                  "feature an allocation checker rather than something like an "
                  "interface to the sales system?",
             "a": ["Because the sales system's vendor requires it",
                   "Because a name for its responsibility in this model recasts the "
                   "problem in the team's own language",
                   "Because the class is a value object",
                   "Because it is generated by the sales system"],
             "c": 1,
             "why": "He defines a service for each allocation function needed and "
                    "names the class for its job in this system. A lower-level class "
                    "may still talk to the other program, hidden behind the checker, "
                    "but it does no translating."},
            {"q": "Evans compares packaging a model by the pattern each object "
                  "follows with other ways of packaging. Which comparison is his?",
             "a": ["It is sound for small models and fails only for large ones",
                   "It is the standard approach, since the patterns are the model",
                   "It makes the same mistake as separating persistent from transient "
                   "objects: a methodical scheme not grounded in what the objects mean",
                   "It is what Layered Architecture requires inside the domain layer"],
             "c": 2,
             "why": "His point is that partitioning by pattern may look like an "
                    "obvious error, but it is the same mistake as every methodical "
                    "scheme that ignores the meaning of the objects; modules should "
                    "hold cohesive concepts."},
        ],
        "mistakes": [
            ("Packaging a model by the building-block patterns because the book names them",
             "Evans's imagined enthusiastic reader does exactly that, and he says the "
             "packages then describe the book being read, not the business. Modules "
             "should follow concepts. On the lesson's illustration packaging by "
             "pattern keeps 5 of 14 dependencies inside a module, all of them "
             "between unrelated entities."),
            ("Thinking the refactored design is simply better than the original",
             "Evans weighs it: on an object database a collection is probably faster, "
             "and frequent listing of whole histories may favour it. The point he "
             "makes is that the aggregates let either choice be made within one "
             "boundary, not that the query always wins."),
            ("Letting the booking application apply the other system's rule",
             "In the first version of the feature the booking application does the "
             "comparison of allocation and bookings, and Evans moves it: enforcing a "
             "business rule is the domain's job, and the checker, which also derives "
             "the segment, is where it belongs."),
        ],
        "standard": (
            "Finish when you can count two packagings of one model.",
            "Given a model's elements, two packagings and its dependencies, state "
            "for each the dependencies inside and across, the share inside, and the "
            "most coupled pair of modules."
        ),
        "note": (
            "The lab counts dependencies inside and across the modules you state. "
            "It cannot tell a concept from a category: a packaging by concept drawn "
            "badly can score as well as a good one. Whether the module names tell "
            "the business's story is the test Evans applies, and it is a reading, "
            "not a count."
        ),
    },
]
