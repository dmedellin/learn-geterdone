"""The Building Blocks of a Model-Driven Design, lessons 6-7 -- the second
half of Chapter 5.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 5, A Model Expressed in Software (Services,
Services and the Isolated Domain Layer, Granularity, Access to Services;
Modules (a.k.a. Packages), Agile Modules, The Pitfalls of
Infrastructure-Driven Packaging; Modeling Paradigms, Why the Object Paradigm
Predominates, Nonobjects in an Object World, Sticking with Model-Driven Design
When Mixing Paradigms). Pages in the comments are PDF pages of the operator's
copy; the lessons cite by chapter, section and pattern. Every quotation is
copied from that copy and checked with quotes.py. The models and the Java are
written for these lessons. The design is docs/domain-driven-design/PLAN.md,
section C, Course 2.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


_PANEL_INTRO = (
    "A count over the small model the lesson states. The lab counts one "
    "consequence of one modelling choice; the choice itself is weighed in the "
    "book, against the domain, the team and the project."
)


# ---------------------------------------------------------------- 06 models

# A theatre box office exchanging a ticket for another performance.
ON_TICKET = (
    "BoxOffice, Ticket; Ticket, Performance; Ticket, SeatPlan; "
    "Ticket, PriceList; Ticket, Refunds; Performance, SeatPlan"
)
EXCHANGE_SERVICE = (
    "BoxOffice, TicketExchange; TicketExchange, Ticket; "
    "TicketExchange, Performance; TicketExchange, SeatPlan; "
    "TicketExchange, PriceList; TicketExchange, Refunds; "
    "Ticket, Performance; Performance, SeatPlan"
)

FORCED_ON_TICKET = """// Forced onto the entity: a ticket that knows prices and refunds.
class Ticket {
    private final Buyer buyer;
    private Performance performance;
    private Seat seat;
    private final PriceList prices;   // here only for exchange
    private final Refunds refunds;    // here only for exchange

    void exchangeFor(Performance wanted, SeatChoice choice) {
        Seat next = wanted.seatPlan().reserve(choice);
        Money diff = prices.priceOf(next).minus(prices.priceOf(seat));
        refunds.settle(buyer, diff);
        performance.seatPlan().release(seat);
        performance = wanted;
        seat = next;
    }
}"""

TICKET_EXCHANGE = """// A domain service: named for the activity, in the model's terms.
public interface TicketExchange {
    Ticket exchange(Ticket held, Performance wanted, SeatChoice choice);
}

final class BoxOfficeExchange implements TicketExchange {
    private final PriceList prices;
    private final Refunds refunds;

    public Ticket exchange(Ticket held, Performance wanted, SeatChoice choice) {
        Seat seat = wanted.seatPlan().reserve(choice);
        refunds.settle(held.buyer(),
                prices.priceOf(seat).minus(held.pricePaid()));
        held.surrender();
        return Ticket.issue(held.buyer(), wanted, seat);
    }
}"""


# ---------------------------------------------------------------- 07 models

# A seed bank, packaged by technical tier (module) and by concept (module2).
SEED_ELEMENTS = (
    "AccessionLogic, logic, accessions; AccessionData, data, accessions; "
    "Passport, logic, accessions; GerminationLogic, logic, testing; "
    "GerminationData, data, testing; ShipmentLogic, logic, distribution; "
    "ShipmentData, data, distribution; Request, logic, distribution"
)
SEED_DEPS = (
    "AccessionLogic, AccessionData; Passport, AccessionData; "
    "AccessionLogic, Passport; GerminationLogic, GerminationData; "
    "ShipmentLogic, ShipmentData; Request, ShipmentData; "
    "ShipmentLogic, Request; GerminationLogic, AccessionLogic; "
    "ShipmentLogic, GerminationLogic"
)
SEED_DEPS_BACK = SEED_DEPS + "; AccessionLogic, ShipmentLogic"

GERMINATION_TEST = """package org.seedbank.testing;

import org.seedbank.accessions.*;   // the module this one depends on

public class GerminationTest {
    private final AccessionNumber accession;
    private final int sown;
    private int germinated;

    public GerminationTest(AccessionNumber accession, int sown) {
        this.accession = accession;
        this.sown = sown;
    }

    public void recordGerminated(int count) {
        germinated = count;
    }

    public Viability viability() {
        return Viability.of(germinated, sown);
    }
}"""

# 07 exercise: a bakery packaged by pattern kind and by concept.
BAKERY_ELEMENTS = (
    "Order, entities, ordering; OrderLine, entities, ordering; "
    "Quantity, values, ordering; Recipe, entities, production; "
    "BatchPlan, services, production; Oven, entities, production"
)
BAKERY_DEPS = (
    "Order, OrderLine; OrderLine, Quantity; OrderLine, Recipe; "
    "BatchPlan, Order; BatchPlan, Recipe; BatchPlan, Oven; Recipe, Quantity"
)


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Services (PDF pp. 59-60 of the operator's copy): the opening (p. 59),
    # doers and Managers (p. 59), the definition (p. 59), verbs and the
    # language (p. 60), the three characteristics and statelessness (p. 60),
    # the pattern (p. 60); Services and the Isolated Domain Layer (pp.
    # 60-61), the layered table (p. 61); Granularity (p. 61); Access to
    # Services (p. 62).
    # Quote: PDF p. 59 of the operator's copy, 6 words, quotes.py OK.
    # Lesson total: 6 words.
    {
        "slug": "services",
        "title": "Services",
        "module": "Chapter 5 · A Model Expressed in Software",
        "one_line": "An operation the domain names but no entity or value naturally owns, offered on its own, stateless, in the language of the model.",
        "summary": (
            "Evans's third kind of model element is not an object of the domain at "
            "all but something done on request. Read his three marks of a good "
            "service, how to tell domain services from application and "
            "infrastructure ones, and what a service does for granularity; then "
            "count the uses an exchange of theatre tickets drags into the ticket, "
            "and where they go when the exchange becomes a service."
        ),
        "key": [
            "some operations are not things",
            "named for an activity, a verb",
            "its interface in terms of the model",
            "stateless: any instance will do",
            "application, domain, infrastructure",
            "do not strip entities of behavior",
        ],
        "key_label": "Services in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the "
            "third the lab's, from Code Complete's counts of a design."
        ),
        "concepts": [
            ("Service",
             "An operation that stands on its own in the model, offered through an "
             "interface; it holds no state of its own, defined by what it does for a client. "
             "A domain service carries a meaning of the business; application and "
             "infrastructure services do not."),
            ("Stateless",
             "In Evans's sense, any client can use any instance of the service "
             "without regard to its history. The service may read and even change "
             "information held elsewhere; it keeps no state of its own that alters "
             "its behaviour."),
            ("Fan-in and fan-out",
             "For one class, the number of classes that use it (fan-in) and the "
             "number it uses (fan-out). The lab reports the largest of each and the "
             "share of possible pairs of classes that are connected."),
        ],
        "read_title": "The pattern, the layers it lives in, then the count",
        "read_intro": (
            "Read Services and its three subsections in your own copy first. The "
            "lesson reads the pattern as a tool, then counts what it moves."
        ),
        "body": [
            ("p", "&ldquo;Sometimes, it just isn't a thing.&rdquo; That is the first "
                  "line of the pattern Services, the last of Chapter 5's three kinds "
                  "of model element. This lesson reads it with Services and the "
                  "Isolated Domain Layer, Granularity, and Access to Services. "
                  "Enterprise Application Patterns reads Randy Stafford's Service "
                  "Layer in its lesson Service Layer, a boundary of application "
                  "operations over the domain; Evans's service is narrower in scope, can "
                  "live in any layer, and the one he cares most about is a concept "
                  "of the domain itself."),
            ("p", "Some important operations of a domain have no natural home in an "
                  "entity or a value, because they are activities rather than "
                  "things. Evans names two mistakes. The more common one is to give "
                  "up too soon on finding the right object and drift into "
                  "procedural code. The other is to force the operation onto an "
                  "object it does not fit: the object loses its clarity, the "
                  "operation can swamp it, and since such operations usually bring "
                  "several domain objects together, the host acquires dependencies "
                  "on all of them. A third shape he notes with some sympathy: the "
                  "&ldquo;doer&rdquo; with a name ending in Manager, a class with no "
                  "state and no meaning beyond the operation it hosts, which at "
                  "least spares the real objects."),
            ("p", "A service is defined purely by what it does for a client, and it "
                  "tends to be named for an activity, a verb rather than a noun. It "
                  "still has a defined responsibility, part of the model, with an "
                  "operation name from the Ubiquitous Language and parameters and "
                  "results that are domain objects. Evans asks that services be used "
                  "judiciously, never to strip entities and values of their "
                  "behaviour. A good one has three characteristics: the operation "
                  "stands for a concept of the domain that does not belong naturally "
                  "to an entity or a value; its interface is expressed through other "
                  "elements of the model; and it is stateless."),
            ("p", "Services and the Isolated Domain Layer sorts them by layer. Most "
                  "services in the literature are technical and belong in the "
                  "infrastructure, such as the interface to an e-mail system. "
                  "Application and domain services are harder to tell apart, and "
                  "Evans's test is business meaning. In his banking example, "
                  "exporting transactions to a spreadsheet is an application "
                  "service, since file formats mean nothing to banking, while a "
                  "funds transfer is a domain service, because it is a term of the "
                  "business and embeds its rules. Putting the transfer on an account "
                  "would be awkward, since it involves two accounts and some global "
                  "rules; the service itself asks the accounts to do most of the "
                  "work. Deciding that a balance has fallen below a threshold is not "
                  "a service at all; it fits the account."),
            ("p", "Granularity adds a second reason for the pattern. Medium-grained, "
                  "stateless services put significant behaviour behind a simple "
                  "interface, which is easier to reuse in a large system and cheaper "
                  "to call across a network than many fine-grained objects. Without "
                  "them the application layer coordinates the domain objects in "
                  "detail, and domain knowledge leaks up into it. The pattern "
                  "favours a simple interface over the client's control. Access to "
                  "Services is brief: how a service is reached matters less than the "
                  "decision to carve it off, and a plain object or a Singleton will "
                  "often do, with elaborate distribution frameworks kept for when "
                  "they are actually needed."),
            ("p", "Now the count, on a theatre box office where a customer exchanges a "
                  "ticket for another performance. Exchange is a word the box office "
                  "uses, and it involves the ticket held, the performance wanted, "
                  "its seat plan, the price list and the refunds. The lab here is "
                  "Code Complete's dependency count, its coupling view: each record "
                  "is one use, written user, used. On the preset "
                  "<code>exchange-on-the-ticket</code> the exchange is a method of "
                  "<code>Ticket</code>, as below. The lab counts 6 classes, 6 uses, "
                  "connected pairs 2/5 = 40% of the 15 possible, the largest fan-out "
                  "<code>Ticket</code> at 4 and the largest fan-in "
                  "<code>SeatPlan</code> at 2."),
            ("code", _lines(FORCED_ON_TICKET)),
            ("p", "The ticket now holds a price list and a refunds account for the "
                  "sake of one operation, which is the dependency Evans warns of. "
                  "The preset <code>exchange-as-a-service</code> moves the operation into "
                  "a domain service, <code>TicketExchange</code>, and the ticket "
                  "keeps only its own performance. The lab counts 7 classes, 8 uses, "
                  "connected pairs 8/21 ≈ 38.1%, the largest fan-out "
                  "<code>TicketExchange</code> at 5, and the largest fan-in "
                  "<code>Performance</code> at 2, tied with "
                  "<code>SeatPlan</code>. <code>Ticket</code>'s own fan-out, which "
                  "you can read off the records, falls from 4 to 1."),
            ("code", _lines(TICKET_EXCHANGE)),
            ("p", "Read the numbers honestly. The design with a service has more "
                  "classes and more uses, not fewer; the connections have moved, "
                  "from an entity that should be about who holds which seat to an "
                  "operation that is about exchanging. That is the trade Evans "
                  "describes, and the count shows it without judging it. The service "
                  "holds a price list and a refunds account, but nothing that "
                  "changes how it behaves from one call to the next, so it is "
                  "stateless in his sense. Whether the box office really thinks of "
                  "exchange as an activity, rather than something a ticket does, is "
                  "the question that decides it, and it is asked of the experts, "
                  "not the lab."),
            ("h3", "Exercise"),
            ("ul", [
                "Four operations in a bike-share: (a) when a ride ends, close it, have "
                "the fare worked out, charge the member and ask for a receipt to be "
                "sent; (b) choose which dock the rebalancing van should empty next, "
                "from the fill level of every dock and the network's rebalancing "
                "rules; (c) send a push notification to a phone; (d) work out a "
                "ride's fare from its length.",
            ]),
            ("p", "Sort each into an application service, a domain service, an "
                  "infrastructure service, or no service at all, and give the reason "
                  "Evans's test supplies. For the domain service, write its interface "
                  "in the model's terms."),
            ("p", "Entities, values and services are the elements; the last part of "
                  "Chapter 5 groups them. The next lesson, Modules and Modeling "
                  "Paradigms, reads how."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "coupling",
            "preset": "exchange-on-the-ticket",
            "presets": [
                {"id": "exchange-on-the-ticket",
                 "label": "Exchange forced onto the Ticket entity",
                 "edges": ON_TICKET,
                 "expect": {"dgModules": "6", "dgEdges": "6", "dgConnected": "2/5 = 40%", "dgFanOut": "Ticket 4", "dgFanIn": "SeatPlan 2"}},
                {"id": "exchange-as-a-service",
                 "label": "Exchange as a domain service, TicketExchange",
                 "edges": EXCHANGE_SERVICE,
                 "expect": {"dgModules": "7", "dgEdges": "8", "dgConnected": "8/21 ≈ 38.1%", "dgFanOut": "TicketExchange 5", "dgFanIn": "Performance 2"}},
            ],
            "panel_title": "Where an operation's dependencies go",
            "panel_intro": (
                "Each record is one use, written user, used. The lab counts the "
                "classes, the distinct uses, the possible pairs, the pairs "
                "connected in either direction and the largest fan-out and fan-in. "
                "The designs are the lesson's, and a count shows one consequence of "
                "where an operation lives, not whether it should live there."
            ),
        }),
        "steps_title": "Deciding whether an operation is a service",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Try the objects first",
             "Ask whether the operation is a natural responsibility of one entity "
             "or value. If it is, put it there; the common mistake is to give up "
             "too soon."),
            ("Apply the three marks",
             "If not, check that the operation is a domain concept, that its "
             "interface can be written in the model's terms, and that it can be "
             "stateless."),
            ("Find its layer",
             "Ask whether it means something to the business. If it embeds business "
             "rules it is a domain service; if it only coordinates or formats, an "
             "application service; if it is purely technical, infrastructure."),
            ("Do it on your own code",
             "Find a class in a system you know that holds a field only one method "
             "uses. Type its uses into the lab, then the uses with that method moved "
             "into a service, and write down the class's fan-out before and after."),
        ],
        "worked": {
            "title": "Ticket's uses, before and after",
            "intro": [
                "Count <code>Ticket</code>'s fan-out in both presets.",
            ],
            "lines": [
                "forced onto Ticket: Performance, SeatPlan",
                "then PriceList and Refunds: 4 in all",
                "as a service: Performance only, 1",
                "the other 3 now come from TicketExchange",
                "TicketExchange also uses Ticket: 5",
            ],
            "after": [
                "The uses did not disappear; they moved to the operation that needs "
                "them. Ticket can now be read as a ticket, and that is a claim about "
                "meaning, which the count supports but does not make.",
            ],
        },
        "quiz_title": "Services, their layers and Evans's claims",
        "quiz": [
            {"q": "In the exercise, by Evans's test of business meaning, how do the "
                  "four operations sort?",
             "a": ["(a) application, (b) domain, (c) infrastructure, (d) no service: "
                   "it belongs to the ride or a fare value",
                   "(a) domain, (b) domain, (c) infrastructure, (d) no service",
                   "(a) application, (b) application, (c) infrastructure, (d) domain",
                   "(a) application, (b) domain, (c) application, (d) domain"],
             "c": 0,
             "why": "Ending a ride only orders the work: it asks the ride to close, "
                    "the domain for the fare, the member's account to be charged and "
                    "the infrastructure for a receipt, and holds no rule of its own, "
                    "so it is an application service even though rules run beneath "
                    "it. Choosing the dock to empty next weighs every dock's fill "
                    "level against the network's rules; it is a term of the business "
                    "that no single dock owns, so a domain service, which might be "
                    "written <code>Dock nextToEmpty(Network network)</code>. A push "
                    "notification is technical: infrastructure. A ride's fare comes "
                    "from the ride's own length, so it fits the ride or a fare value "
                    "and needs no service, as Evans's balance threshold fits the "
                    "account."},
            {"q": "What does statelessness mean for a service in Evans's sense?",
             "a": ["It may not read or change any information outside itself",
                   "It holds no fields of any kind",
                   "Any client can use any instance without regard to its history; "
                   "it may still change global information",
                   "It must be a Singleton"],
             "c": 2,
             "why": "A service may use information accessible globally and may even "
                    "change it, which is a side effect; what it does not have is "
                    "state of its own that affects its behaviour. A Singleton is one "
                    "way Evans mentions of giving access, not a requirement, and "
                    "references to collaborators, like the price list in "
                    "<code>BoxOfficeExchange</code>, are not state in this sense."},
            {"q": "Which of these is one of Evans's three characteristics of a good "
                  "service?",
             "a": ["It is distributed through a framework such as J2EE or CORBA",
                   "Its parameters and results are other elements of the domain "
                   "model",
                   "It replaces the behaviour of the entities it uses",
                   "It is named with a noun ending in Manager"],
             "c": 1,
             "why": "The three are: the operation stands for a domain concept that "
                    "no entity or value naturally owns; its interface, parameters and "
                    "results included, is made of other model elements; and it is "
                    "stateless. Evans "
                    "warns against stripping entities of their behaviour, treats "
                    "Manager-named doers as services in disguise, and says elaborate "
                    "frameworks are often overkill."},
            {"q": "On the preset <code>exchange-as-a-service</code>, the use "
                  "<code>Ticket, Performance</code> is removed. Which class has the "
                  "largest fan-in now, by the lab's rule that a tie goes to the "
                  "alphabetically first name?",
             "a": ["Performance, 2",
                   "SeatPlan, 2",
                   "Ticket, 1",
                   "TicketExchange, 1"],
             "c": 1,
             "why": "Performance is now used only by TicketExchange, fan-in 1. SeatPlan "
                    "is still used by TicketExchange and Performance, fan-in 2, and "
                    "no other class reaches 2, so SeatPlan has the largest alone."},
        ],
        "mistakes": [
            ("Making every operation a service",
             "Evans calls the more common mistake giving up too easily on fitting "
             "behaviour into the right object, and drifting toward procedural code. "
             "Services are to be used judiciously and never allowed to strip "
             "entities and values of their behaviour; a balance check belongs to the "
             "account, not to a service."),
            ("Calling any class with Service in its name a domain service",
             "Most services are technical and belong to the infrastructure, and many "
             "others are application services that coordinate and format. A domain "
             "service carries a meaning of the business and embeds its rules, like "
             "a funds transfer; a spreadsheet export does not, whatever it is "
             "called."),
            ("Thinking a stateless service cannot change anything",
             "Statelessness, for Evans, means any client can use any instance "
             "without regard to its history. The service may read global "
             "information and change it as a side effect; it holds no state of its "
             "own that changes how it behaves."),
        ],
        "standard": (
            "Finish when you can say where an operation belongs and what moving it costs.",
            "Given an operation and the objects it uses, decide whether it is a "
            "responsibility of an object or a service, place the service in a layer, "
            "and count the uses each design gives its classes."
        ),
        "note": (
            "The lab counts uses as you list them. It cannot tell whether an "
            "operation is a concept of the domain, whether it fits an entity better "
            "than you thought, or which layer its meaning belongs to; Evans decides "
            "those by the language of the business, not by the arrows."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Modules (a.k.a. Packages) (PDF pp. 62-63 of the operator's copy):
    # cognitive overload (p. 62), coupling and cohesion of concepts (p. 62),
    # communication and the pattern (p. 63); Agile Modules (pp. 63-64), the
    # Java package example (p. 64); The Pitfalls of Infrastructure-Driven
    # Packaging (pp. 64-66), the four-tier project (p. 65), the two costs and
    # the advice (pp. 65-66); the chapter's close (p. 66); Modeling Paradigms
    # (pp. 66-69): Why the Object Paradigm Predominates (pp. 66-68),
    # Nonobjects in an Object World (p. 68), Sticking with Model-Driven Design
    # When Mixing Paradigms (pp. 68-69), the four rules of thumb (p. 69).
    # Quote: PDF p. 63 of the operator's copy, 11 words, quotes.py OK.
    # Lesson total: 11 words.
    {
        "slug": "modules-and-modeling-paradigms",
        "title": "Modules and Modeling Paradigms",
        "module": "Chapter 5 · A Model Expressed in Software",
        "one_line": "Modules chosen by the concepts they hold, named in the language, refactored with the model; and objects as the paradigm, mixed with others only with care.",
        "summary": (
            "Chapter 5 ends with the largest building block and with the paradigm "
            "the others assume. Read why Evans wants modules to tell the story of "
            "the domain, how technical packaging schemes pull a concept apart, and "
            "his rules of thumb for mixing objects with rules engines; then package "
            "a seed bank by tier and by concept and count the dependencies each "
            "keeps inside its modules."
        ),
        "key": [
            "modules are part of the model",
            "cohesive concepts, low coupling",
            "names in the Ubiquitous Language",
            "refactor modules with the model",
            "one concept, one module",
            "objects first; mix paradigms warily",
        ],
        "key_label": "Modules and paradigms in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Module",
             "A named group of model elements, a package in Java. Evans treats the "
             "choice of modules as part of the model: placing classes together tells "
             "the next developer to think about them together."),
            ("Cohesion and coupling of concepts",
             "High cohesion is a module whose elements have rich conceptual "
             "relationships; low coupling is modules that can be understood with "
             "little reference to each other. Evans applies both to ideas, not only "
             "to code."),
            ("Share inside",
             "The dependencies whose two ends are in the same module, as a share of "
             "all the dependencies. The lab gives it for each of two packagings of "
             "one model, with any cycle between modules."),
        ],
        "read_title": "Two arguments, modules and paradigms, then the count",
        "read_intro": (
            "Read Modules, its two subsections and Modeling Paradigms in your own "
            "copy first. The lesson reads modules as a pattern and paradigms as an "
            "argument, then counts one model packaged two ways."
        ),
        "body": [
            ("p", "&ldquo;If your model is telling a story, the MODULES are "
                  "chapters.&rdquo; That is Evans in Modules, also called Packages, "
                  "the last pattern of Chapter 5. This lesson reads it with Agile "
                  "Modules and The Pitfalls of Infrastructure-Driven Packaging, then "
                  "the section that closes the chapter, Modeling Paradigms."),
            ("p", "Modules are old, Evans says, and the main reason for them is not "
                  "technical but cognitive overload. They give two views of a model: "
                  "the detail inside one module without the whole, or the "
                  "relationships between modules without the detail. Everyone uses "
                  "them, and few treat them as part of the model; code is divided by "
                  "technical architecture or by who works on what, and modules chosen "
                  "early tend to stay. The familiar rule, that modules should be "
                  "loosely coupled to each other and cohesive inside, is usually explained as a "
                  "technical metric. Evans reads it as a fact about minds: a person "
                  "can think about only so many things at once, and fragments of "
                  "ideas are as hard to follow as an undivided soup."),
            ("p", "Put as a rule to apply: let each module be a chapter of the "
                  "domain's story, its concepts belonging together. Low coupling "
                  "often follows; when it does not, change the model so the "
                  "concepts separate, or find a missing concept that can anchor a "
                  "module of its own. Give the modules names that "
                  "enter the Ubiquitous Language, so that a conversation with an "
                  "expert can start from one. Thinking in concepts does not replace "
                  "the technical measures; it works at another level of the same "
                  "problem; where they conflict, Evans would take conceptual clarity, "
                  "even at the cost of more references between modules."),
            ("p", "Agile Modules is about change. Modules ought to evolve with the "
                  "model, and seldom do, because moving them means wide edits, "
                  "disrupts the team and upsets the tools; so module names often "
                  "describe a much older model than the classes do, and early "
                  "mistakes harden. His Java example notes that imports are declared "
                  "class by class, and suggests importing whole packages, which "
                  "mixes scales but states a dependency on a module and makes "
                  "renaming cheaper. A class that needs one class from a module its "
                  "own module has no conceptual reason to depend on is a sign that "
                  "something should move."),
            ("p", "The Pitfalls of Infrastructure-Driven Packaging separates the "
                  "framework rules that help from those that hurt. Keeping the "
                  "interface and infrastructure in their own packages, and the domain "
                  "in its own, enforces the layering and is useful. Splitting each "
                  "domain object into tiers, data in one object and logic in "
                  "another, each tier in its own package, is not. Evans tells of a "
                  "well-run project whose every concept was split four ways, a tier "
                  "to a package: developers avoided making modules and hardly ever "
                  "changed one, "
                  "finding everything that defined one concept took all their "
                  "attention, and what shipped was an anemic model, data access with "
                  "behaviour in a few services. His advice: use packaging to "
                  "separate the domain layer, and otherwise, unless code really is "
                  "deployed to different servers, keep all the code for one concept "
                  "in one module, if not one object."),
            ("p", "Modeling Paradigms widens the view. A model-driven design needs an "
                  "implementation technology that fits its paradigm, and objects "
                  "predominate for good reasons: they balance simplicity and "
                  "richness, people who are not programmers can follow an object "
                  "diagram, and the tools, the infrastructure and the community are "
                  "mature. Evans's own story of an ambitious early object database, "
                  "found to be using a large share of its capacity on test data "
                  "alone, shows what an immature technology can cost. Yet a domain model need not be an object "
                  "model, and some domains, intensely mathematical ones or those "
                  "ruled by global logical reasoning, fit objects badly. Mixing in a "
                  "rules engine or a workflow engine is appealing and hard; the "
                  "common failure is an application split into object storage and an "
                  "unconnected set of rules."),
            ("p", "He ends with four rules of thumb for mixing other paradigms into "
                  "an object system: do not fight the implementation paradigm, but "
                  "find concepts that fit it; lean on the Ubiquitous Language to "
                  "keep the parts from drifting apart; do not distort the model to "
                  "fit what UML can draw; and be sceptical whether the extra tool "
                  "earns its cost, since rules can often be objects. Exhaust the "
                  "dominant paradigm first. The relational database is the special "
                  "case, left to Chapter 6."),
            ("p", "Now the count, on a seed bank. Its model has three concepts, "
                  "accessions (the seed lots it holds, with their passport data), "
                  "germination testing, and distribution to people who request "
                  "seed, and its classes have been split into logic and data in "
                  "the tiered way Evans describes. The lab's cohesion view takes "
                  "each element with two module assignments, so that one model can "
                  "be packaged two ways at once: by tier, <code>logic</code> and "
                  "<code>data</code>, and by concept, <code>accessions</code>, "
                  "<code>testing</code> and <code>distribution</code>. On the preset "
                  "<code>seed-bank-two-ways</code>, with 9 dependencies, the tier packaging "
                  "keeps 4 inside its modules and sends 5 across, 4/9 inside; the "
                  "concept packaging keeps 7 inside and 2 across, 7/9. Neither has a "
                  "cycle between modules. The most coupled pair under tiers is data "
                  "and logic, with all 5 crossings."),
            ("code", _lines(GERMINATION_TEST)),
            ("p", "Every crossing in the tier packaging is one concept's logic "
                  "reaching its own data, which is Evans's point about very high "
                  "coupling between the two halves of a split object. The preset "
                  "<code>accession-knows-shipments</code> adds one dependency, an accession that "
                  "knows its shipments. The concept packaging now keeps 7 of 10 "
                  "inside and lists a cycle, accessions to distribution to testing "
                  "and back; the tier packaging keeps 5 of 10 and has none, since "
                  "logic only ever uses data. The count does not say the tiers were "
                  "better. It says the new link tangles three concepts, and Evans's "
                  "remedy is in the model: turn the link round, so that a shipment "
                  "names its accession, as the Associations lesson did with its "
                  "links, or find the concept that would hold it."),
            ("h3", "Exercise"),
            ("ul", [
                "A bakery's elements, each with two modules, by pattern kind and by "
                "concept: `Order, entities, ordering; OrderLine, entities, ordering; "
                "Quantity, values, ordering; Recipe, entities, production; BatchPlan, "
                "services, production; Oven, entities, production`.",
                "Its dependencies: `Order, OrderLine; OrderLine, Quantity; OrderLine, "
                "Recipe; BatchPlan, Order; BatchPlan, Recipe; BatchPlan, Oven; "
                "Recipe, Quantity`.",
            ]),
            ("p", "For each packaging, count the dependencies inside modules and "
                  "across them, and find any cycle between modules. Then name one "
                  "change to the model that would remove the cycle you find."),
            ("p", "This course has read the elements a model is built from. The next "
                  "course, The Life Cycle of a Domain Object, reads Chapter 6's "
                  "Aggregates, Factories and Repositories, which keep those elements "
                  "whole from creation to storage."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "cohesion",
            "packagings": 2,
            "names": ["by tier", "by concept"],
            "preset": "seed-bank-two-ways",
            "presets": [
                {"id": "seed-bank-two-ways",
                 "label": "A seed bank packaged by tier and by concept",
                 "elements": SEED_ELEMENTS,
                 "deps": SEED_DEPS,
                 "expect": {"dmoInside": "4", "dmoAcross": "5", "dmoShare": "4/9 ≈ 44.4%", "dmoCycles": "0: none", "dmoPair": "data and logic: 5", "dmoInside2": "7", "dmoAcross2": "2", "dmoShare2": "7/9 ≈ 77.8%", "dmoCycles2": "0: none"}},
                {"id": "accession-knows-shipments",
                 "label": "The same, with an accession that knows its shipments",
                 "elements": SEED_ELEMENTS,
                 "deps": SEED_DEPS_BACK,
                 "expect": {"dmoInside": "5", "dmoShare": "1/2 = 50%", "dmoCycles": "0: none", "dmoInside2": "7", "dmoAcross2": "3", "dmoShare2": "7/10 = 70%", "dmoCycles2": "1: (accessions, distribution, testing)"}},
            ],
            "panel_title": "One model, two packagings",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Packaging a model by its concepts",
        "steps_intro": "Five steps, the last of them on code of your own.",
        "steps": [
            ("Name the concepts",
             "List the few concepts the domain's experts would use to describe the "
             "model in outline, in their words."),
            ("Assign every element",
             "Put each class in the module of the concept it expresses, keeping the "
             "parts of one concept together whatever their technical role."),
            ("Count inside and across",
             "Sort each dependency as inside a module or across, and draw the "
             "module-level arrows to find any cycle."),
            ("Untangle through the model",
             "For each cycle or heavy crossing, look for a direction to impose or a "
             "missing concept, rather than moving classes until the count improves."),
            ("Do it on your own code",
             "Take one package tree you know, type its classes with their current "
             "package and the package you would choose by concept, and the imports "
             "as dependencies. Write down the share inside for each, and any cycle."),
        ],
        "worked": {
            "title": "Nine dependencies, two packagings",
            "intro": [
                "Sort the dependencies of <code>seed-bank-two-ways</code>.",
            ],
            "lines": [
                "logic to own data: 5, across tiers",
                "the same 5: inside each concept",
                "AccessionLogic to Passport: inside both",
                "ShipmentLogic to Request: inside both",
                "Germination to Accession: across concepts",
                "Shipment to Germination: across concepts",
                "tiers 4 of 9 inside; concepts 7 of 9",
            ],
            "after": [
                "The two crossings left under concepts are the model's real "
                "relationships between ideas; the five under tiers are each one "
                "concept talking to itself across a package line.",
            ],
        },
        "quiz_title": "Modules, packaging and Evans's claims",
        "quiz": [
            {"q": "In the exercise, how many of the 7 dependencies stay inside a "
                  "module under each packaging, and where is there a cycle between "
                  "modules?",
             "a": ["By kind 2, by concept 4; a cycle between ordering and production",
                   "By kind 2, by concept 4; no cycle in either",
                   "By kind 3, by concept 4; a cycle between entities and values",
                   "By kind 2, by concept 5; a cycle between ordering and production"],
             "c": 0,
             "why": "By kind, only Order to OrderLine and OrderLine to Recipe join two "
                    "entities: 2 inside, 5 across, and no cycle, since entities use "
                    "values and services use entities but nothing points back. By "
                    "concept, Order to OrderLine, OrderLine to Quantity, BatchPlan to "
                    "Recipe and BatchPlan to Oven are inside: 4; OrderLine to Recipe "
                    "runs from ordering to production, while BatchPlan to Order and "
                    "Recipe to Quantity run back, so the two modules form a cycle. "
                    "One remedy: let an order line name a product rather than a "
                    "recipe, or move Quantity into a small module both can use."},
            {"q": "What does Evans recommend in The Pitfalls of Infrastructure-Driven "
                  "Packaging?",
             "a": ["Put each technical tier of every object in its own package",
                   "Use packaging to separate the domain layer, and otherwise keep "
                   "the code for one concept in one module unless it is truly "
                   "distributed",
                   "Avoid packages in the domain layer altogether",
                   "Follow the framework's naming convention for every package"],
             "c": 1,
             "why": "Separating the domain layer from other code is the useful "
                    "framework standard. Splitting objects into tiers across packages "
                    "is the pitfall: unless code is really deployed to different "
                    "servers, keep a concept's code in one module, if not one object, "
                    "and leave the domain developers free to package the rest."},
            {"q": "When Evans finds that concept-based modules are still tightly "
                  "coupled, what does he advise?",
             "a": ["Package by technical tier instead",
                   "Merge the modules into one",
                   "Change the model so the concepts separate, or find a missing "
                   "concept that can anchor a module of its own",
                   "Accept it, since coupling is only a technical metric"],
             "c": 2,
             "why": "The pattern says to look for a change to the model, or a concept "
                    "missing from it that could be the basis of a module. He does "
                    "prefer conceptual clarity to fewer references when they truly "
                    "conflict, but that comes after the model has been worked on."},
            {"q": "Which is one of Evans's four rules of thumb for mixing other "
                  "paradigms into an object system?",
             "a": ["Model each part in whichever paradigm fits it best",
                   "Adopt a rules engine whenever the model has rules",
                   "Draw everything in UML so that both parts share one notation",
                   "Lean on the Ubiquitous Language to keep the parts from "
                   "diverging"],
             "c": 3,
             "why": "The four are: do not fight the implementation paradigm; lean on "
                    "the Ubiquitous Language; do not get hung up on UML; be "
                    "sceptical whether the tool pulls its weight. Modelling each part "
                    "in its own paradigm is the appeal he describes and then hedges, "
                    "and he asks that the dominant paradigm's options be exhausted "
                    "first."},
        ],
        "mistakes": [
            ("Treating packages as a filing system for the code",
             "Evans treats modules as part of the model: their names enter the "
             "Ubiquitous Language, and putting classes together tells the next "
             "developer to think of them together. Packaging by work assignment or "
             "technical role, then leaving it alone, lets the modules describe a "
             "model the classes have left behind."),
            ("Splitting each concept into technical tiers, a package for each",
             "Evans grants that the separation has reasons, but it pulls the code "
             "for one concept apart, spends all the dividing a reader can mentally "
             "reassemble, and on the project he describes led to an anemic model. "
             "Keep a concept's code in one module unless it is really deployed to "
             "different servers."),
            ("Concluding that objects must model everything",
             "Objects predominate for reasons Evans sets out, and he advises "
             "exhausting them before mixing paradigms. But a domain model need not be "
             "an object model, some domains fit other paradigms better, and when "
             "rules engines or other tools are used, model-driven design should be "
             "kept, not abandoned."),
        ],
        "standard": (
            "Finish when you can package a model by its concepts and read what the count shows.",
            "Given elements with two packagings and their dependencies, count the "
            "share inside and the cycles for each, and say what change to the model "
            "would untangle a crossing."
        ),
        "note": (
            "The lab counts dependencies inside and across the modules you assign. "
            "It cannot tell whether a module tells the domain's story, whether its "
            "name would mean anything to an expert, or whether a cycle is a missing "
            "concept; Evans puts conceptual clarity above the count when the two "
            "conflict."
        ),
    },
]
