"""Behavioral Patterns II, lessons 6-7 -- Chapter 5's discussion and Chapter 6.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995): Discussion of Behavioral
Patterns, which closes Chapter 5 (Encapsulating Variation, Objects as
Arguments, Should Communication be Encapsulated or Distributed?, Decoupling
Senders and Receivers, Summary), and Chapter 6, Conclusion (6.1 What to Expect
from Design Patterns, 6.2 A Brief History, 6.3 The Pattern Community, 6.4 An
Invitation, 6.5 A Parting Thought). Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter and section. Every quotation is
copied from that copy and checked with quotes.py. The designs and records are
written for these lessons. The design is docs/design-patterns/PLAN.md,
section C, Course 6.
"""

from .part_a import _lines, _records


# ---------------------------------------------------------------- 6.6 records

# A ticket desk's devices, which must coordinate: the till, the ticket
# printer, the barcode scanner, the customer display and the queue screen.
DESK_FIVE = "till printer scanner display queue"
DESK_EIGHT = DESK_FIVE + " door alarm phone"

GARDEN_EXERCISE = """colleagues:  sensor valve pump panel phone timer weather
designs:     each talks to each other directly, both ways;
             each talks only to one mediator"""


# ---------------------------------------------------------------- 6.7 records

# A bakery's till system after an expansionary phase: each kind of discount
# was added as a subclass of Order, and the till, the receipt and the daily
# report each test the order's class.
BAKERY_BEFORE = """Order, orders;
StaffOrder, orders;
StudentOrder, orders;
Till, till;
Receipt, printing;
DailyReport, reports;
LoyaltyCard, loyalty"""

BAKERY_BEFORE_CHANGES = """senior-discount, Order;
senior-discount, Till;
senior-discount, Receipt;
senior-discount, DailyReport;
staff-cap, StaffOrder;
staff-cap, Receipt;
loyalty-stamps, LoyaltyCard;
loyalty-stamps, StaffOrder;
loyalty-stamps, StudentOrder;
receipt-logo, Receipt"""

# After a consolidation that makes discounts strategies an order is given.
BAKERY_AFTER = """Order, orders;
Discount, pricing;
StaffDiscount, pricing;
StudentDiscount, pricing;
Till, till;
Receipt, printing;
DailyReport, reports;
LoyaltyCard, loyalty"""

BAKERY_AFTER_CHANGES = """senior-discount, Discount;
senior-discount, Till;
staff-cap, StaffDiscount;
loyalty-stamps, LoyaltyCard;
loyalty-stamps, Discount;
receipt-logo, Receipt"""

DISCOUNT_JAVA = """// After the consolidation: an order is given a discount instead of being one.
interface Discount {
    long offCents(long total);
}
final class StaffDiscount implements Discount {
    public long offCents(long total) { return Math.min(total / 5, 500); }
}
final class StudentDiscount implements Discount {
    public long offCents(long total) { return total / 10; }
}
final class Order {
    private final Discount discount;     // was: class StaffOrder extends Order
    private long totalCents;
    Order(Discount discount) { this.discount = discount; }
    long dueCents() { return totalCents - discount.offCents(totalCents); }
}"""

CONTROLLER_EXERCISE = """// before: elements, as element, module
Controller, control; Panel, ui; Scheduler, schedule; Alarm, alerts
// before: changes, as change, element
frost-mode, Controller; frost-mode, Panel; frost-mode, Scheduler;
holiday-mode, Controller; holiday-mode, Scheduler; alarm-sound, Alarm
// after: the same four, and the modes as State classes in their own module
Controller, control; Panel, ui; Scheduler, schedule; Alarm, alerts;
ModeState, modes
// after: changes
frost-mode, ModeState; frost-mode, Panel; holiday-mode, ModeState;
alarm-sound, Alarm"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Chapter 5, Discussion of Behavioral Patterns (PDF pp. 365-369 of the
    # operator's copy): Encapsulating Variation p. 365, Objects as Arguments
    # pp. 365-366, Should Communication be Encapsulated or Distributed? p. 366,
    # Decoupling Senders and Receivers pp. 366-368, Summary p. 369.
    # Quote: PDF p. 366 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "behavioral-discussion",
        "title": "Discussion of Behavioral Patterns",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "What each behavioral pattern wraps up, which ones travel as arguments, and four ways of keeping a sender apart from its receiver.",
        "summary": (
            "The chapter closes by comparing its eleven patterns: what each encapsulates, "
            "which objects are passed as arguments, Observer against Mediator, and four "
            "ways to decouple senders from receivers. Read it, then count the connections "
            "a ticket desk's devices need when each talks to each, against one mediator."
        ),
        "key": [
            "name the aspect that varies, then wrap it",
            "some objects travel as arguments",
            "Observer distributes; Mediator centralizes",
            "reuse against an easy flow to follow",
            "four ways to decouple a sender",
            "patterns are used together",
        ],
        "key_label": "The discussion in six lines",
        "concepts_intro": (
            "Three ideas from the discussion, the last of them what the lab counts."
        ),
        "concepts": [
            ("Encapsulating variation",
             "Finding the aspect of a program likely to change and giving it an object of "
             "its own, which the rest of the program works with. Many behavioral patterns "
             "are named after that object: a strategy, a state, a mediator, an iterator."),
            ("Distributed or encapsulated communication",
             "Under Observer no single object keeps a constraint: subjects and observers "
             "cooperate to keep it. Under Mediator one object holds the constraint, and "
             "the others talk only to it."),
            ("Connections",
             "In the lab, a link one colleague must hold to another and keep in step with "
             "it. Pairwise, n colleagues need one for each pair; through a mediator, one "
             "each. The lab's tiles say contexts and translators: read them as colleagues "
             "and connections."),
        ],
        "read_title": "The discussion first, then the count",
        "read_intro": (
            "Read Discussion of Behavioral Patterns, at the end of Chapter 5, in your own "
            "copy first; it is a few pages. The lesson reads it as an argument, part by "
            "part, and then counts one comparison it makes."
        ),
        "body": [
            ("p", "&ldquo;We've found it easier to make reusable Observers and Subjects than "
                  "to make reusable Mediators.&rdquo; That is the authors weighing two of "
                  "their own patterns, in Discussion of Behavioral Patterns, the pages that "
                  "close Chapter 5. The discussion has four parts and a summary; it reads the "
                  "eleven patterns of the chapter, the six of the last course and the five of "
                  "this one, side by side."),
            ("p", "Encapsulating Variation is the first theme. When some aspect of a program "
                  "changes often, many behavioral patterns give it an object, which the "
                  "rest of the program uses wherever it depends on that aspect, and the "
                  "pattern takes the object's name: a strategy wraps an algorithm, a state "
                  "the behaviour that depends on a state, a mediator the protocol between "
                  "objects, an iterator the way an aggregate is traversed. Most of these "
                  "patterns involve a new object and the existing ones that use it, and without the pattern the new one's code would be inside "
                  "the old. A footnote adds that Abstract Factory, Builder, Prototype, "
                  "Decorator and Bridge share the theme. Chain of Responsibility is the "
                  "exception: it works over any number of objects that may already exist, "
                  "and its communication is open-ended rather than fixed between classes."),
            ("p", "Objects as Arguments is the second. A visitor is always an argument, to "
                  "the accept operation of what it visits, and never part of those objects, "
                  "though without the pattern its code would be spread through them. Command "
                  "and Memento make tokens, passed around and used later: a command stands "
                  "for a request and a memento for an object's state at one moment. They "
                  "differ in one respect. Executing a command is polymorphic; a memento's "
                  "interface is so narrow that it is passed only as a value."),
            ("p", "The third part asks whether communication should be encapsulated or "
                  "distributed, and calls Mediator and Observer competitors. Observer "
                  "distributes it: no single object holds the constraint, subjects and "
                  "observers maintain it together, and the pattern of communication is how "
                  "they happen to be connected, sometimes with one subject's observer being "
                  "another's subject. Mediator puts the constraint in the mediator. The "
                  "authors find Observer gives finer-grained classes that are easier to "
                  "reuse, as the opening quotation says; and they find the flow of "
                  "communication easier to follow through a mediator, since observers are "
                  "usually connected just after they are made and the connections are hard "
                  "to see later. Smalltalk's observers are more reusable still, so a "
                  "Smalltalk programmer often picks Observer where one writing C++ would "
                  "pick Mediator."),
            ("p", "Decoupling Senders and Receivers is the fourth. Objects that refer to each "
                  "other directly depend on each other, and four patterns loosen that, each "
                  "differently. Command puts the binding of sender to receiver in an object, "
                  "so a sender can work with different receivers; it nominally needs a "
                  "subclass per connection. Observer's binding is looser, since a subject "
                  "can have many observers, their number changing at run time, and it suits data "
                  "dependencies best. Mediator has colleagues refer to each other only "
                  "through it, which can reduce subclassing, but its fixed interface may "
                  "force a home-made dispatching scheme that weakens type safety. Chain of "
                  "Responsibility passes a request along possible receivers and shares that "
                  "drawback; it suits a chain the structure already has, and is easy to "
                  "change."),
            ("p", "The Summary says the behavioral patterns mostly reinforce one another: a "
                  "handler in a chain probably uses a template method, the chain may carry "
                  "commands, an interpreter may keep its parsing contexts as states, and a "
                  "visitor may act on what an iterator reaches. They work with the other "
                  "patterns too, and the book imagines a Composite with visitors, a chain to "
                  "parents, decorators, observers, states, a builder that made it, and other parts of the system treating it as a prototype. Well-designed systems, the authors say, are full of "
                  "patterns, whether or not their designers thought in those terms."),
            ("p", "Now the lab, on one comparison from the third part, at the scale of a "
                  "ticket desk of the lesson's own: five devices, the till, the ticket "
                  "printer, the scanner, the customer display and the queue screen, which "
                  "must keep each other informed. The lab's view comes from another kit, so "
                  "its tiles say contexts and translators; read them as colleagues and "
                  "connections. On the preset <code>desk-pairwise</code>, where each device "
                  "talks to each other directly, both ways, the lab counts 5 colleagues and "
                  "10 connections to build, one per pair, and 4 to change when one device's "
                  "interface changes. The tile for the other design gives the mediator's "
                  "figures, and the ratios compare the two."),
            ("p", "The preset <code>desk-mediator</code> routes every device through one "
                  "mediator, the scheme the lab calls published: 5 connections to build, one per device, and 1 to change. The "
                  "preset <code>desk-eight</code> adds a door, an alarm and a phone: pairwise "
                  "28 to build and 7 to change, against 8 and 1. Two cautions keep these "
                  "figures honest. Observer is not the pairwise extreme, since a subject "
                  "links only to its own observers, so the counts bound the comparison rather "
                  "than settle it. And the one connection that changes under the mediator "
                  "sits inside the mediator, which absorbs every such change; that is how it "
                  "grows into the monolith Mediator warns of. The authors' two measures, "
                  "reuse and a flow easy to follow, are not counted at all."),
            ("h3", "Exercise"),
            ("code", _lines(GARDEN_EXERCISE)),
            ("p", "A garden controller's seven devices. By hand, count the connections to "
                  "build and to change in each design. Then type the colleagues into the lab "
                  "and switch the scheme between pairwise and published to check."),
            ("p", "That ends Chapter 5 and the catalog. The next lesson, What to Expect from "
                  "Design Patterns, reads Chapter 6, the authors' conclusion to the book."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "protocol",
            "preset": "desk-pairwise",
            "presets": [
                {"id": "desk-pairwise",
                 "label": "A ticket desk's five devices, each talking to each",
                 "contexts": DESK_FIVE,
                 "scheme": "pairwise",
                 "expect": {"dcxN": "5",
                            "dcxBuild": "10",
                            "dcxChange": "4",
                            "dcxOther": "published: 5 to build, 1 to change",
                            "dcxBuildRatio": "2×",
                            "dcxChangeRatio": "4×"}},
                {"id": "desk-mediator",
                 "label": "The same five through one mediator",
                 "contexts": DESK_FIVE,
                 "scheme": "published",
                 "expect": {"dcxBuild": "5",
                            "dcxChange": "1",
                            "dcxOther": "pairwise: 10 to build, 4 to change"}},
                {"id": "desk-eight",
                 "label": "Eight devices, each talking to each",
                 "contexts": DESK_EIGHT,
                 "scheme": "pairwise",
                 "expect": {"dcxN": "8",
                            "dcxBuild": "28",
                            "dcxChange": "7",
                            "dcxOther": "published: 8 to build, 1 to change",
                            "dcxBuildRatio": "7/2 ≈ 3.5×",
                            "dcxChangeRatio": "7×"}},
            ],
            "panel_title": "Connections, distributed or centralized",
            "panel_intro": (
                "Read the tiles' contexts as colleagues and their translators as "
                "connections; the published scheme is one mediator that every colleague "
                "talks to. The designs are the lesson's."
            ),
        }),
        "steps_title": "Comparing two ways to connect colleagues",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the colleagues",
             "List the objects that must keep each other informed, and count them: n."),
            ("Count the pairwise design",
             "Each pair needs a connection: n·(n − 1)/2 to build. When one colleague "
             "changes, its n − 1 connections change."),
            ("Count the mediated design",
             "Each colleague connects to the mediator: n to build, 1 to change, and that "
             "one inside the mediator."),
            ("Do it on a design of your own",
             "Pick a screen or a device in code you know whose parts notify each other. "
             "Count both designs, and say which of the book's two measures, reuse or a "
             "flow you can follow, matters more there."),
        ],
        "worked": {
            "title": "Ten connections, or five",
            "intro": [
                "Count <code>desk-pairwise</code> and <code>desk-mediator</code>.",
            ],
            "lines": [
                "five devices: n = 5",
                "pairwise: 5 · 4 / 2 = 10 to build",
                "one device changes: 5 − 1 = 4",
                "mediator: 5 to build, 1 to change",
                "eight devices: 8 · 7 / 2 = 28, 7 to change",
            ],
            "after": [
                "The pairwise figure grows with the square of the devices and the mediated "
                "one in step with them, which is why the gap widens from 2 times to 3.5 "
                "times between five and eight.",
            ],
        },
        "quiz_title": "Encapsulation, arguments and decoupling",
        "quiz": [
            {"q": "In the exercise, how many connections are built and changed with each "
                  "device talking to each, and with one mediator?",
             "a": ["21 and 6, against 7 and 1",
                   "42 and 6, against 7 and 1",
                   "21 and 7, against 7 and 1",
                   "21 and 6, against 8 and 1"],
             "c": 0,
             "why": "Seven devices: 7 · 6 / 2 = 21 pairs, and a device that changes has 6 "
                    "connections. Through a mediator, one each, 7, and 1 to change. 42 counts "
                    "each pair twice, as one-way links; 7 to change counts the device itself; "
                    "8 counts the mediator as a colleague."},
            {"q": "What do the authors conclude when they compare Observer and Mediator?",
             "a": ["Mediators are easier to reuse, and observers easier to follow",
                   "Mediator wins on both reuse and understanding",
                   "Observers and subjects are easier to reuse; the flow is easier to follow "
                   "in a mediator",
                   "The two are interchangeable in every language"],
             "c": 2,
             "why": "They find Observer's finer-grained classes easier to reuse, and "
                    "Mediator's centralized flow easier to understand. They add that "
                    "Smalltalk tips the balance toward Observer, so the choice is not the "
                    "same in every language."},
            {"q": "Which pattern does the discussion call best for decoupling objects that "
                  "have data dependencies between them?",
             "a": ["Command", "Observer", "Mediator", "Chain of Responsibility"],
             "c": 1,
             "why": "Its subject and observer interfaces are designed for communicating "
                    "changes. Command binds a sender to a receiver through an object; "
                    "Mediator routes requests between colleagues; Chain of Responsibility "
                    "suits a chain the structure already has."},
            {"q": "Which two patterns does the discussion say may need a home-made "
                  "dispatching scheme, at a cost in type safety?",
             "a": ["Command and Observer",
                   "Observer and Mediator",
                   "Command and Chain of Responsibility",
                   "Mediator and Chain of Responsibility"],
             "c": 3,
             "why": "Both route requests through a fixed interface, a mediator's or a "
                    "handler's, so an open-ended set of requests must be encoded and "
                    "decoded by hand. Command's request is an object with one execute "
                    "operation, and Observer's interface is made for change notices."},
        ],
        "mistakes": [
            ("Expecting a winner between Observer and Mediator",
             "The authors give each a strength the other lacks, reuse for Observer and a "
             "flow easy to follow for Mediator, and say the language tips the balance. On "
             "the lesson's illustration the lab counts connections, which neither of their "
             "two measures is."),
            ("Thinking every behavioral pattern splits a new object from the ones that use it",
             "Most do, and are named for the new object. Chain of Responsibility works "
             "instead over any number of objects that may already exist, with "
             "communication left open-ended; and Visitor, Command and Memento wrap an "
             "operation, a request or a state in objects that travel as arguments rather "
             "than being kept by their users."),
            ("Treating decoupling as free",
             "Each of the four ways costs something: Command a subclass per connection, "
             "Observer connections that are hard to see, Mediator and Chain of "
             "Responsibility type safety when they dispatch by hand. The discussion "
             "states each trade-off beside the benefit."),
        ],
        "standard": (
            "Finish when you can say what each behavioral pattern encapsulates or "
            "decouples, and at what cost.",
            "Count the connections a set of colleagues needs pairwise and through a "
            "mediator, and give the authors' two measures for choosing between Observer "
            "and Mediator."
        ),
        "note": (
            "The lab counts connections at the two extremes. It cannot count reuse or how "
            "easy a flow is to follow, the measures the authors actually use, and it does "
            "not model an Observer design, whose connections depend on who observes whom."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Chapter 6, Conclusion (PDF pp. 371-378 of the operator's copy): opening
    # p. 371; 6.1 What to Expect from Design Patterns pp. 371-375 (A Common
    # Design Vocabulary p. 372, A Documentation and Learning Aid pp. 372-373,
    # An Adjunct to Existing Methods p. 373, A Target for Refactoring pp.
    # 373-375); 6.2 A Brief History p. 375; 6.3 The Pattern Community pp.
    # 376-378; 6.4 An Invitation p. 378; 6.5 A Parting Thought p. 378.
    # Quote: PDF p. 375 of the operator's copy, 8 words, quotes.py OK.
    # Lesson total: 8 words.
    {
        "slug": "conclusion",
        "title": "What to Expect from Design Patterns",
        "module": "Chapter 6 · Conclusion",
        "one_line": "The authors' own account of what a catalog of patterns is for: a vocabulary, a way to read systems, a missing piece of design methods, and a target for refactoring.",
        "summary": (
            "Chapter 6 says what the authors expect patterns to do for a designer, tells "
            "the catalog's history, places it beside Christopher Alexander's work, and "
            "invites the reader in. Read it, then count the modules a bakery's change "
            "requests reach before and after a consolidation that makes its discounts a "
            "Strategy."
        ),
        "key": [
            "names make designs easier to discuss",
            "the why, not only the what",
            "prototype, expand, consolidate",
            "black-box reuse replaces white-box",
            "patterns are targets for refactoring",
            "a collection, not a pattern language",
            "be a critical consumer",
        ],
        "key_label": "Chapter 6 in seven lines",
        "concepts_intro": (
            "Three ideas from Chapter 6, the last of them what the lab counts."
        ),
        "concepts": [
            ("Design vocabulary",
             "Pattern names used as words between designers, so that a design can be "
             "described, documented and argued about at a level above classes and "
             "notation."),
            ("The refactoring life cycle",
             "Brian Foote's three phases of object-oriented software: prototyping, where "
             "classes mirror the problem and reuse is by inheritance; expansion, where new "
             "requirements pile on classes; and consolidation, where the software is "
             "reorganized, often into composed objects."),
            ("Modules a change touches",
             "For one change request, the number of distinct modules holding the classes "
             "it alters. A variation spread through a design sends a change to several; "
             "the same variation behind one pattern sends it to fewer."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Chapter 6, Conclusion, in your own copy first; it is short. The lesson "
            "reads it as an argument, section by section, and then counts what one "
            "consolidation changes."
        ),
        "body": [
            ("p", "&ldquo;Design patterns thus provide targets for your refactorings.&rdquo; "
                  "The sentence closes A Target for Refactoring, in Chapter 6, Conclusion. "
                  "The chapter opens by stating the case against the book: it offers no new "
                  "algorithm or technique, no rigorous method and no theory of design, only "
                  "existing designs written down. The authors' reply is that cataloguing "
                  "gives the techniques standard names and definitions, that what is not "
                  "studied cannot be improved, and that the book is a start, which they hope "
                  "will set others documenting what practitioners know."),
            ("p", "Section 6.1 gives four things to expect. A Common Design Vocabulary: "
                  "research on expert programmers, which the book cites, found knowledge held "
                  "in larger structures than syntax, and patterns name such structures, so "
                  "designers can talk above the level of notation and code; you will hear "
                  "yourself proposing an Observer here or a Strategy there. A Documentation "
                  "and Learning Aid: much of what makes a large system's inheritance hard to "
                  "follow is patterns the reader does not recognise, and naming the patterns "
                  "a design uses saves the next reader from reverse-engineering them. The "
                  "authors admit to using their patterns in arguably naive ways, to name "
                  "classes, to teach, and to describe a design as the sequence of patterns "
                  "applied."),
            ("p", "An Adjunct to Existing Methods: design methods supply notations and "
                  "rules but, the authors argue, have not captured the experience of expert "
                  "designers, and patterns are the missing piece. They show how to use "
                  "objects, inheritance and polymorphism to parameterize a system by an "
                  "algorithm, a behaviour, a state or the kind of objects it creates, and "
                  "they record why a design is as it is, with Applicability, Consequences and "
                  "Implementation as guides to the decisions. They are especially useful in getting from "
                  "an analysis model to an implementation model, which is never as smooth as "
                  "promised, and a full method would need other kinds too: analysis, user "
                  "interface and performance-tuning patterns."),
            ("p", "A Target for Refactoring tells the life cycle Brian Foote described. In "
                  "the prototyping phase software is built fast, until it meets its first "
                  "requirements; its class hierarchies mirror the problem domain and reuse is "
                  "white-box, by inheritance. In the expansionary phase new requirements add "
                  "classes and operations until the hierarchies reflect many domains and the "
                  "software grows stiff. In the consolidating phase it is refactored: classes "
                  "split into special and general parts, operations move up and down, "
                  "interfaces are rationalized, frameworks emerge, and composition replaces "
                  "inheritance, black-box reuse in place of white-box. Expansion and "
                  "consolidation repeat. The patterns, the authors say, capture many of the "
                  "structures refactoring produces: used early, they spare later "
                  "refactorings, and found late, they show what to refactor toward."),
            ("p", "6.2, A Brief History, is the catalog's story. It began in Erich Gamma's "
                  "doctoral thesis, which held about half the patterns; Richard Helm joined "
                  "him by OOPSLA '91, John Vlissides soon after, and Ralph Johnson by OOPSLA "
                  "'92. A 90-page paper for ECOOP '93 was plainly too long, so they sent a "
                  "summary, which was accepted, and decided on a book. Wrapper became "
                  "Decorator, Glue became Facade, Solitaire Singleton and Walker Visitor. "
                  "Their main lesson was that spotting a pattern is easy and describing one "
                  "so that newcomers see why it matters is hard, so the patterns grew from "
                  "under two pages each to over ten, with examples, sample code, trade-offs "
                  "and, increasingly, the problem each solves."),
            ("p", "6.3, The Pattern Community, sets the book beside Christopher Alexander's "
                  "work on buildings. Both observe existing systems, use a template, write in "
                  "natural language with many examples and give reasons. But building is "
                  "thousands of years old and software young; Alexander orders his patterns "
                  "and the authors do not; his stress the problem and theirs the solution; "
                  "and he claims his generate whole buildings, while they claim no such thing "
                  "for programs. Their catalog, they say, is a collection of related patterns "
                  "and not a pattern language, and a complete one for software is unlikely. "
                  "They trace the community from Bruce Anderson's OOPSLA '91 workshop to the "
                  "first Pattern Languages of Programs conference in 1994, and name Knuth, "
                  "Graphics Gems, Coplien, Kent Beck and Peter Coad among its forerunners and "
                  "members."),
            ("p", "6.4, An Invitation, asks three things: use patterns and build your "
                  "vocabulary; be a critical consumer, since patterns make their authors' "
                  "trade-offs explicit and so open to argument, and send the authors your "
                  "objections; and write down the patterns you use, with someone else to "
                  "help you improve them. 6.5, A Parting Thought, ends on a passage "
                  "from Alexander, which the book quotes, contrasting a building that "
                  "only strings patterns together with one where many overlap in the same "
                  "space and the building gains its depth from that density."),
            ("p", "Now the lab, on the life cycle at small scale: a bakery's till system "
                  "after its expansionary phase, of the lesson's own. Each kind of discount "
                  "was added as a subclass of the order, and the till, the receipt and the "
                  "daily report each test the order's class. On the preset "
                  "<code>bakery-expansion</code> the lab takes 7 classes in 5 modules and 4 "
                  "change requests and counts the modules each touches: a senior discount 4, "
                  "a cap on the staff discount 2, loyalty stamps on discounted orders 2, a "
                  "new logo on the receipt 1. That is 9 module touches, 1 change confined to "
                  "one module, and the largest change the senior discount, at 4."),
            ("code", _lines(DISCOUNT_JAVA)),
            ("p", "The preset <code>bakery-consolidated</code> is the same system after a "
                  "consolidation that turns the discounts into a Strategy, above: an order "
                  "is given a discount object from a pricing module, by composition, instead "
                  "of being a subclass. A senior discount is now a new class beside the "
                  "others in pricing, which the lab records as a touch on the family it "
                  "joins, plus the till's list of discounts: 2. The staff cap is 1, loyalty "
                  "stamps 2 and the logo 1, for 6 touches, 2 changes confined to one module, "
                  "and a largest change of 2, the senior discount tied with loyalty stamps "
                  "and shown first. Those are the figures for these four requests only. The "
                  "book's point is that the pattern gave the refactoring a target; whether "
                  "this one was worth doing depends on which requests come next."),
            ("h3", "Exercise"),
            ("code", _lines(CONTROLLER_EXERCISE)),
            ("p", "A garden irrigation controller, before and after its modes become State "
                  "classes in a module of their own. By hand, give the modules each change "
                  "touches in each design, the total and the changes confined to one module. "
                  "Then enter both designs into the lab to check."),
            ("p", "That ends the book, and this Subject. The authors' invitation is the "
                  "next step: look for the patterns in code you know and write them down. "
                  "Two Subjects in this library carry the patterns further, Domain-Driven "
                  "Design, Read Along, on patterns as concepts in a model, and Patterns of "
                  "Enterprise Application Architecture, Read Along, on patterns at the scale "
                  "of whole applications."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "preset": "bakery-expansion",
            "presets": [
                {"id": "bakery-expansion",
                 "label": "A bakery's discounts as subclasses of the order",
                 "elements": _records(BAKERY_BEFORE),
                 "changes": _records(BAKERY_BEFORE_CHANGES),
                 "expect": {"dmoChanges": "4",
                            "dmoPer": "senior-discount 4, staff-cap 2, loyalty-stamps 2, receipt-logo 1",
                            "dmoTotal": "9",
                            "dmoConfined": "1 of 4: receipt-logo",
                            "dmoLargest": "senior-discount, 4 modules"}},
                {"id": "bakery-consolidated",
                 "label": "The same system with discounts as a Strategy",
                 "elements": _records(BAKERY_AFTER),
                 "changes": _records(BAKERY_AFTER_CHANGES),
                 "expect": {"dmoPer": "senior-discount 2, staff-cap 1, loyalty-stamps 2, receipt-logo 1",
                            "dmoTotal": "6",
                            "dmoConfined": "2 of 4: staff-cap, receipt-logo",
                            "dmoLargest": "senior-discount, 2 modules"}},
            ],
            "panel_title": "The modules each change request reaches",
            "panel_intro": (
                "The lab counts one consequence of consolidating a design into a "
                "pattern: the modules each change request reaches before and after; "
                "whether the consolidation is worth its indirection is weighed in the "
                "book, against what in the design is expected to vary."
            ),
        }),
        "steps_title": "Counting what a consolidation changes",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the classes and modules",
             "Write each class with its module, before the consolidation and after it, "
             "including the classes the pattern adds."),
            ("List the change requests",
             "For each request the system has had or expects, write the classes it alters "
             "in each design. Use the same requests for both."),
            ("Count the modules",
             "For each request, count the distinct modules among its classes; add them for "
             "the total, and count the requests that stay in one module."),
            ("Do it on a system of your own",
             "Pick a part of a system you know that has grown by subclassing. Name the "
             "pattern a consolidation would aim at, and count the modules your last three "
             "changes there touched before and as they would after."),
        ],
        "worked": {
            "title": "Four requests, before the consolidation",
            "intro": [
                "Count the modules each request touches on <code>bakery-expansion</code>.",
            ],
            "lines": [
                "senior-discount: orders, till, printing, reports: 4",
                "staff-cap: orders, printing: 2",
                "loyalty-stamps: loyalty, orders: 2",
                "receipt-logo: printing: 1",
                "total: 4 + 2 + 2 + 1 = 9; confined: 1",
                "after: 2 + 1 + 2 + 1 = 6; confined: 2",
            ],
            "after": [
                "The two requests about discounts fall furthest; the logo was never about "
                "discounts and stays at one module in both designs.",
            ],
        },
        "quiz_title": "Vocabulary, life cycle and history",
        "quiz": [
            {"q": "In the exercise, what are the total module touches and the changes "
                  "confined to one module, before and after the modes become State classes?",
             "a": ["before 6 and 1; after 4 and 2",
                   "before 6 and 1; after 3 and 3",
                   "before 5 and 1; after 4 and 2",
                   "before 6 and 0; after 4 and 2"],
             "c": 0,
             "why": "Before: frost-mode touches control, ui and schedule, 3; holiday-mode "
                    "control and schedule, 2; alarm-sound alerts, 1: a total of 6, with only "
                    "the alarm confined. After: frost-mode touches modes and ui, 2, since the "
                    "panel must still show it; holiday-mode modes, 1; alarm-sound 1: a total "
                    "of 4, two of them confined."},
            {"q": "In Foote's life cycle as the chapter tells it, in which phase does "
                  "black-box reuse replace white-box reuse?",
             "a": ["Prototyping", "Expansionary", "Consolidating",
                   "None: each phase keeps the reuse it began with"],
             "c": 2,
             "why": "Consolidation reorganizes the software, often decomposing objects and "
                    "composing them instead of inheriting, so black-box reuse replaces the "
                    "white-box reuse of the prototyping phase. The expansionary phase is "
                    "where requirements pile on classes until the design stiffens."},
            {"q": "Which of these is a difference the authors draw between their patterns "
                  "and Alexander's?",
             "a": ["Alexander writes in natural language; they use a formal one",
                   "Alexander gives an order for using his patterns; they give none",
                   "They claim their patterns generate complete programs",
                   "Alexander has no template for describing a pattern"],
             "c": 1,
             "why": "They list four differences: the age of the field, the order Alexander "
                    "gives, his stress on problems against their detail on solutions, and "
                    "his claim to generate whole buildings, which they do not make for "
                    "programs. Both use natural language and both have templates."},
            {"q": "Which renaming does A Brief History record?",
             "a": ["Glue became Mediator",
                   "Solitaire became Flyweight",
                   "Walker became Visitor",
                   "Wrapper became Proxy"],
             "c": 2,
             "why": "The four it names are Wrapper to Decorator, Glue to Facade, Solitaire "
                    "to Singleton and Walker to Visitor."},
        ],
        "mistakes": [
            ("Taking the catalog for a method that generates designs",
             "The authors say plainly that it is a collection of related patterns, not a "
             "pattern language, that they do not claim it generates whole programs, and "
             "that a complete pattern language for software is unlikely. Patterns help a "
             "designer decide; they do not decide."),
            ("Applying patterns up front to avoid ever refactoring",
             "The chapter calls the cycle of expansion and consolidation unavoidable. "
             "Patterns used early make a design robust to the changes a requirements "
             "analysis says are likely; found later, they show what to refactor toward. On "
             "the lesson's illustration the lab counts four requests, not the ones that "
             "come next."),
            ("Accepting the catalog uncritically",
             "The Invitation asks the opposite: because a pattern states its trade-offs, "
             "it can be argued with, and the authors want to hear where theirs fall "
             "short. Read every Consequences section that way."),
        ],
        "standard": (
            "Finish when you can say what the authors expect patterns to do, and what "
            "they do not claim.",
            "Count the modules each change touches before and after a consolidation that "
            "introduces one pattern, and place it in Foote's life cycle."
        ),
        "note": (
            "The lab counts modules over the requests listed. It cannot say which requests "
            "are coming, or whether a consolidation was worth its cost; the chapter's "
            "advice, to design for the changes that are likely, depends on knowing them."
        ),
    },
]
