"""Large-Scale Structure and Strategy, lessons 1-5 -- Chapters 16 and 17.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 16, Large-Scale Structure (Evolving Order,
System Metaphor, Responsibility Layers, Knowledge Level, Pluggable Component
Framework and the sections that follow it) and Chapter 17, Bringing the
Strategy Together, as far as Assessment First. Pages in the comments are PDF
pages of the operator's copy; the lessons cite by chapter, section and pattern.
Every quotation is copied from that copy and checked with quotes.py. The
models in the labs are written for these lessons (a bike-share, a theatre box
office, a library, a museum group, a bakery chain, a seed bank, a clinic);
none of the book's example domains, figures or data is reproduced. The design
is docs/domain-driven-design/PLAN.md, section C, Course 9.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- models

# 9.1 Evolving Order: one bike-share model under two packagings. module is the
# structure fixed up front (one package a screen); module2 the one that grew.
BIKES_ELEMENTS = (
    "Bike, rent-screen, fleet; Rider, rent-screen, riding; Fare, rent-screen, pricing; "
    "Dock, return-screen, fleet; Trip, return-screen, riding; Tariff, return-screen, pricing; "
    "Station, admin-screen, fleet; Membership, admin-screen, riding"
)
BIKES_CHANGES = (
    "weekend-tariff, Fare; weekend-tariff, Tariff; "
    "dock-sensor, Dock; dock-sensor, Station; "
    "family-plan, Membership; family-plan, Rider; "
    "ride-time-cap, Trip; ride-time-cap, Fare"
)
BIKES_CHANGES_PLUS = BIKES_CHANGES + (
    "; rebalancing-credit, Station; rebalancing-credit, Trip; "
    "rebalancing-credit, Tariff; rebalancing-credit, Rider"
)

# 9.2 Responsibility Layers: a theatre box office, layers top to bottom.
THEATRE_LAYERS = "decision policy operations potential"
THEATRE_ELEMENTS = (
    "Auditorium, potential; Seat, potential; Usher, potential; "
    "Performance, operations; Booking, operations; Ticket, operations; "
    "ConcessionRule, policy; PricingAdvisor, decision"
)
THEATRE_DEPS_FIRST = (
    "Seat, Auditorium; Performance, Auditorium; Performance, Usher; "
    "Booking, Performance; Booking, Ticket; Ticket, Seat; Booking, ConcessionRule; "
    "Auditorium, Performance; ConcessionRule, Ticket; "
    "PricingAdvisor, Booking; PricingAdvisor, ConcessionRule"
)
THEATRE_DEPS_REFACTORED = (
    "Seat, Auditorium; Performance, Auditorium; Performance, Usher; "
    "Booking, Performance; Booking, Ticket; Ticket, Seat; ConcessionRule, Booking; "
    "ConcessionRule, Ticket; "
    "PricingAdvisor, Booking; PricingAdvisor, ConcessionRule"
)

BOOKING_ASKS_POLICY = """// Operations: one booking of seats for one performance.
class Booking {
    private final Performance performance;
    private final List<Ticket> tickets = new ArrayList<>();
    private final ConcessionRule concessions;   // a Policy object

    long priceCents() {
        long total = 0;
        for (Ticket t : tickets) {
            total += concessions.priceCents(t); // operations asks policy
        }
        return total;
    }
}"""

POLICY_READS_BOOKING = """// Policy: the rule reads the booking; the booking never names the rule.
class ConcessionRule {
    long priceCents(Booking booking) {
        long total = 0;
        for (Ticket t : booking.tickets()) {
            total += priceCents(t);
        }
        return total;
    }

    long priceCents(Ticket t) {
        return t.isConcession() ? t.faceCents() / 2 : t.faceCents();
    }
}"""

# 9.3 Knowledge Level: a library's borrower categories, as subclasses and as
# knowledge-level objects configured by a superuser.
LIBRARY_SUBCLASS_ELEMENTS = (
    "Borrower, borrowers; StudentBorrower, borrowers; StaffBorrower, borrowers; "
    "VisitorBorrower, borrowers; AlumniBorrower, borrowers; "
    "RegistrationForm, accounts; FineCalculator, fines"
)
LIBRARY_SUBCLASS_CHANGES = (
    "add-visitor, VisitorBorrower; add-visitor, RegistrationForm; add-visitor, FineCalculator; "
    "add-alumni, AlumniBorrower; add-alumni, RegistrationForm; "
    "longer-staff-loans, StaffBorrower; "
    "exam-amnesty, FineCalculator; exam-amnesty, StudentBorrower"
)
LIBRARY_KNOWLEDGE_ELEMENTS = (
    "Borrower, operations; Loan, operations; "
    "BorrowerCategory, knowledge; FinePolicy, knowledge; "
    "CategoryTable, configuration; RegistrationForm, accounts"
)
LIBRARY_KNOWLEDGE_CHANGES = (
    "add-visitor, CategoryTable; add-alumni, CategoryTable; "
    "longer-staff-loans, CategoryTable; "
    "exam-amnesty, FinePolicy; exam-amnesty, BorrowerCategory; exam-amnesty, CategoryTable"
)

BORROWER_CATEGORY = """// Knowledge level: what one kind of borrower may do.
// Instances are rows a superuser edits; the class rarely changes.
class BorrowerCategory {
    private final String name;
    private final int loanDays;
    private final FinePolicy fines;

    int loanDays() { return loanDays; }
    FinePolicy fines() { return fines; }
}

// Operations level: a real borrower, constrained by its category.
class Borrower {
    private BorrowerCategory category;

    LocalDate dueDate(LocalDate borrowed) {
        return borrowed.plusDays(category.loanDays());
    }
}"""


_CHANGE_INTRO = (
    "A count over the small model the lesson states. Each element is assigned to a "
    "module, and each change lists the elements it touches; the lab counts the modules "
    "each change reaches. The packagings and changes are the lesson's, not the book's."
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 16, opening (PDF pp. 272-274 of the operator's copy), Evolving
    # Order (pp. 274-276), System Metaphor and The "Naive Metaphor" (pp. 276-277).
    # Quote: PDF p. 275 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "evolving-order-and-system-metaphor",
        "title": "Evolving Order and System Metaphor",
        "module": "Chapter 16 · Large-Scale Structure",
        "one_line": "A structure for the whole system that grows with the system instead of being fixed before anyone understood it, and a metaphor as its loosest form.",
        "summary": (
            "Chapter 16 asks how a model too large to hold in one head can still be "
            "understood as a whole. Read Evans's case for a large-scale structure, his "
            "warning against fixing one up front, and his qualified case for a System "
            "Metaphor; then count how far four changes to a bike-share reach under a "
            "packaging decided early and one that grew with the changes."
        ),
        "key": [
            "a structure lets you see the whole",
            "fixed up front, it becomes a straitjacket",
            "let the structure evolve with the system",
            "a poor fit costs more than no structure",
            "a metaphor is the loosest structure",
            "drop a metaphor that misleads",
        ],
        "key_label": "Evolving Order in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Large-scale structure",
             "A small set of high-level rules, roles or concepts that applies across a "
             "whole system, so that a developer can say what part a piece plays without "
             "knowing its details. It shapes the design but usually does not appear in "
             "it as a class or a package."),
            ("Evolving Order",
             "Evans's pattern for how such a structure should be found: let it grow and "
             "change with the application, even into a different kind of structure, "
             "instead of deciding it before the domain is understood."),
            ("Modules touched by a change",
             "For one change, the number of distinct modules holding an element the "
             "change edits. The lab adds these up across a list of changes and counts "
             "the changes that stay inside one module."),
        ],
        "read_title": "The chapter's problem, then two patterns, then the count",
        "read_intro": (
            "Read the opening of Chapter 16, Evolving Order and System Metaphor in your "
            "own copy first. The lesson reads the opening as the chapter's problem and "
            "the two patterns as Evans's first answers to it, and then counts one "
            "consequence of fixing a structure early."
        ),
        "body": [
            ("p", "&ldquo;The problem is not the existence of guiding rules, but rather the "
                  "rigidity and source of those rules.&rdquo; The sentence is from Evolving "
                  "Order, the first pattern of Chapter 16, Large-Scale Structure. This lesson "
                  "reads the chapter's opening, that pattern, and System Metaphor. Read them "
                  "in your own copy first."),
            ("p", "The chapter opens on a team building a simulator of a satellite "
                  "communications network. They had broken a hard model into many sensible "
                  "modules, and the modules had multiplied until nobody could say where a "
                  "new class belonged. Their way out was not another package but a story "
                  "about the system as a whole, a stack of conceptual layers from the "
                  "physical links upward, which they refined while refactoring the code to "
                  "fit it. Evans uses the story to name what was missing: not a class, but a "
                  "structure for the model as a whole."),
            ("p", "His argument for needing one runs through the strategic tools you have "
                  "already met. Modules cut a design into pieces of a manageable size, but "
                  "there may be a great many of them, and they need not be designed alike. "
                  "Bounded Contexts keep models from corrupting one another but do not by "
                  "themselves show the whole. Distillation picks out the Core Domain, yet "
                  "the supporting parts still have to be understood in relation to it. On a "
                  "project of any size people work apart, and without some shared rules "
                  "they solve the same problem in different ways, become specialists who "
                  "cannot help one another, and lose sight of how the parts fit."),
            ("p", "A large-scale structure, in Evans's terms, is a language for discussing "
                  "the system in broad strokes: rules or roles that span the design and let "
                  "anyone say what a part is for without reading its details. It may live in one "
                  "Bounded Context but usually spans several. It is mostly not drawn in UML "
                  "and does not need to be; it explains the model rather than appearing in "
                  "it. And he is plain that a small team with a model of modest size may "
                  "need nothing more than well-named modules, some distillation and "
                  "informal coordination."),
            ("p", "Evolving Order is the pattern for how the structure arrives. Evans sets "
                  "two failures against each other. A design free-for-all produces a system "
                  "no one can understand as a whole. An architecture imposed up front, "
                  "especially one that reaches into the domain layer, freezes decisions "
                  "made before the domain was understood, and as requirements change it "
                  "fights the developers: they simplify the application to fit it, or route "
                  "around it until there is no structure at all. His resolution is the "
                  "quotation's: keep guiding rules, but let them grow from the application "
                  "and change with it, perhaps into a different kind of structure "
                  "altogether, and leave detailed modelling decisions to the people who "
                  "have the detailed knowledge."),
            ("p", "He does not pretend the choice is free. A structure favours the "
                  "manageability of the whole over the best shape of each part, so some "
                  "parts will be expressed less naturally than they could be. A structure "
                  "that really fits pays that back: it rules out many options at once, "
                  "gives shortcuts to decisions that would otherwise be argued object by "
                  "object, and helps different people reach consistent answers. It must "
                  "leave teams in different contexts room for their local models, and it "
                  "must bend around parts nobody controls, such as an external or legacy "
                  "system."),
            ("p", "Two more qualifications close the pattern. A Context Map is always "
                  "needed; a large-scale structure is not, worth imposing only when one is found "
                  "that clarifies the system without forcing unnatural constraints; because "
                  "a structure that fits badly is worse than none, Evans advises a minimal "
                  "set aimed at the problems that have actually appeared. A structure may "
                  "tolerate a few exceptions if they are marked, but when they become "
                  "numerous the structure should be changed or dropped. He then offers four "
                  "structures he has seen emerge on projects, not as a catalogue but as "
                  "starting points: this lesson's metaphor, and the three that follow."),
            ("p", "System Metaphor comes from Extreme Programming, where it is one of the "
                  "core practices, and Evans credits Ward Cunningham's firewall with making "
                  "it click for him. The firewall picture made a whole product category easy "
                  "to grasp, yet its power cuts both ways: it suggested a barrier at the "
                  "edge and so said nothing about threats from inside. A metaphor, Evans "
                  "says, is a loose structure that sits comfortably with objects, and "
                  "because it is only an analogy, models in several contexts can map to it "
                  "approximately. The risk is that a persuasive analogy carries in features "
                  "the problem does not have, and he notes that few projects have found a "
                  "really useful one."),
            ("p", "So the pattern is conditional. Evans would take up a metaphor only when "
                  "one has turned up that the team finds compelling and that points its "
                  "thinking somewhere productive. Then it shapes the design and enters the "
                  "Ubiquitous Language, and because no analogy is exact it stays under "
                  "review, to be abandoned once it misleads. A "
                  "sidebar disposes of the XP community's &ldquo;naive metaphor&rdquo;, the "
                  "domain model itself: a model refined through many rounds of knowledge "
                  "crunching is anything but naive, and Evans would retire the term. Among "
                  "the twelve XP practices, he says, a Ubiquitous Language can play the "
                  "metaphor's role."),
            ("p", "Now the count. The lab holds one small bike-share model of eight "
                  "elements under two packagings. The first was fixed before the domain was "
                  "understood, one package for each screen of the app: "
                  "<code>rent-screen</code>, <code>return-screen</code> and "
                  "<code>admin-screen</code>. The second grew as the team learned which "
                  "things change together: <code>fleet</code> for bikes, docks and "
                  "stations, <code>riding</code> for riders, memberships and trips, and "
                  "<code>pricing</code> for fares and tariffs. Four changes arrive, each "
                  "touching two elements."),
            ("ul", [
                "By screen: rent-screen holds Bike, Rider, Fare; return-screen holds Dock, "
                "Trip, Tariff; admin-screen holds Station, Membership.",
                "Grown: fleet holds Bike, Dock, Station; riding holds Rider, Membership, "
                "Trip; pricing holds Fare, Tariff.",
                "Changes: weekend-tariff touches Fare and Tariff; dock-sensor touches Dock "
                "and Station; family-plan touches Membership and Rider; ride-time-cap "
                "touches Trip and Fare.",
            ]),
            ("p", "On the preset <code>screens-against-grown</code> the screen packaging "
                  "gives 4 changes, 2 modules for every one of them, 8 module touches in "
                  "all, and 0 changes confined to one module. The grown packaging gives 5 "
                  "touches: three changes stay in one module, and ride-time-cap, the "
                  "largest, reaches 2, <code>riding</code> and <code>pricing</code>. The "
                  "count is not a verdict on screens as packages. It shows one consequence "
                  "of deciding the structure before the changes were known: the screens "
                  "were a guess about what would vary, and the changes did not vary that "
                  "way."),
            ("p", "The preset <code>a-change-neither-fits</code> adds a fifth change, "
                  "rebalancing-credit, which pays riders who return a bike to an emptying "
                  "station and touches Station, Trip, Tariff and Rider. It reaches 3 "
                  "modules under both packagings, so the totals become 11 against 8 and "
                  "the largest change is the new one under each. The grown structure was "
                  "found from the first four changes and does not help with a kind of "
                  "change it never saw. That is the case Evolving Order is written for: "
                  "the structure is a current best reading of the domain, and a new kind "
                  "of requirement is a reason to look at it again."),
            ("h3", "Exercise"),
            ("ul", [
                "A seed bank, packaged by department up front: intake holds SeedLot and "
                "Donor; storage holds VaultShelf and GerminationTest; outreach holds "
                "Request and Packet.",
                "The same elements, packaged as the team learned: viability holds SeedLot "
                "and GerminationTest; holdings holds VaultShelf and Packet; members holds "
                "Donor and Request.",
                "Changes: retest-interval touches GerminationTest and SeedLot; "
                "member-quota touches Request and Donor; packet-size touches Packet, "
                "VaultShelf and Request.",
            ]),
            ("p", "By hand, find the modules each change touches under each packaging, the "
                  "total module touches, and the changes confined to one module. Then type "
                  "the model into the lab to check, the department packaging in the "
                  "column the lab labels by screen and the learned one in the column "
                  "labelled as it grew, and say in a sentence what the "
                  "department packaging assumed about how the seed bank would change."),
            ("p", "A structure that grows with the system still has to be some particular "
                  "structure. The next lesson, Responsibility Layers, reads the one Evans "
                  "develops at greatest length: layers cut along the domain's own strata."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "packagings": 2,
            "names": ["by screen", "as it grew"],
            "preset": "screens-against-grown",
            "presets": [
                {"id": "screens-against-grown",
                 "label": "A bike-share packaged by screen up front, and as it grew",
                 "elements": BIKES_ELEMENTS,
                 "changes": BIKES_CHANGES,
                 "expect": {"dmoChanges": "4",
                            "dmoTotal": "8",
                            "dmoConfined": "0 of 4",
                            "dmoLargest": "weekend-tariff, 2 modules",
                            "dmoTotal2": "5",
                            "dmoConfined2": "3 of 4: weekend-tariff, dock-sensor, family-plan",
                            "dmoLargest2": "ride-time-cap, 2 modules"}},
                {"id": "a-change-neither-fits",
                 "label": "The same, with a fifth change that cuts across both",
                 "elements": BIKES_ELEMENTS,
                 "changes": BIKES_CHANGES_PLUS,
                 "expect": {"dmoChanges": "5",
                            "dmoTotal": "11",
                            "dmoLargest": "rebalancing-credit, 3 modules",
                            "dmoTotal2": "8",
                            "dmoLargest2": "rebalancing-credit, 3 modules"}},
            ],
            "panel_title": "How far each change reaches under two packagings",
            "panel_intro": _CHANGE_INTRO,
        }),
        "steps_title": "Reading a packaging against its changes",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Write each packaging as a table",
             "List every element once with the module it sits in, one column a "
             "packaging, so that both can be read against the same changes."),
            ("Mark each change's modules",
             "For each change, look up the module of every element it touches and count "
             "the distinct modules. A change that touches two elements in one module "
             "counts one."),
            ("Add up, and look at the largest",
             "Sum the touches for each packaging, count the changes confined to one "
             "module, and read the largest change: it is the one the structure fits "
             "worst."),
            ("Do it on your own system",
             "Take the last five changes merged into a system you know. Write down the "
             "packages each touched, total the touches, and say in one sentence what "
             "kind of change the current packaging seems to expect."),
        ],
        "worked": {
            "title": "Four changes against the screen packaging",
            "intro": [
                "Count the module touches of <code>screens-against-grown</code> under the "
                "screen packaging, by hand.",
            ],
            "lines": [
                "weekend-tariff: rent-screen, return-screen",
                "dock-sensor: return-screen, admin-screen",
                "family-plan: admin-screen, rent-screen",
                "ride-time-cap: return-screen, rent-screen",
                "4 changes, 2 modules each: 8 touches",
                "none of the four stays in one module",
            ],
            "after": [
                "Under the grown packaging the same four give 1, 1, 1 and 2, which is 5. "
                "The difference measures only how well each packaging anticipated these "
                "four changes; a fifth of another kind can erase it, as the second preset "
                "shows.",
            ],
        },
        "quiz_title": "Structure, its evolution, and the metaphor",
        "quiz": [
            {"q": "In the exercise, what are the total module touches under the department "
                  "packaging and under the packaging the team learned, and how many changes "
                  "does each confine to one module?",
             "a": ["6 and 4; department confines 0, learned confines 2",
                   "6 and 4; department confines 0, learned confines 1",
                   "7 and 4; department confines 0, learned confines 2",
                   "6 and 5; department confines 1, learned confines 2"],
             "c": 0,
             "why": "By department, retest-interval reaches storage and intake, "
                    "member-quota outreach and intake, and packet-size outreach and storage "
                    "(Packet and Request are both in outreach): 2 + 2 + 2 is 6, none "
                    "confined. As learned, retest-interval stays in viability and "
                    "member-quota in members, while packet-size reaches holdings and "
                    "members: 1 + 1 + 2 is 4, two confined. Counting packet-size's three "
                    "elements as three modules gives the 7; it touches two outreach "
                    "elements, which count once. The department packaging assumed each "
                    "department's work would change on its own, and these changes cross "
                    "departments."},
            {"q": "In Evolving Order, what does Evans name as the problem with architectures "
                  "imposed on the domain layer?",
             "a": ["That any guiding rules at all limit what developers can do",
                   "The rigidity and source of the rules, fixed before the domain was understood",
                   "That they are drawn in UML, which cannot show a large-scale structure",
                   "That they are confined to a single Bounded Context"],
             "c": 1,
             "why": "He keeps guiding rules: a structure that fits pushes development in a "
                    "helpful direction. The trouble is rules that cannot change and that "
                    "come from somewhere other than the application being built. That most "
                    "structures are not shown in UML is a separate remark, and a structure "
                    "may live in one context or span several."},
            {"q": "How does Evans compare a large-scale structure with a Context Map?",
             "a": ["Both are required on every project of any size",
                   "The structure is required and the map is optional",
                   "The map is required; the structure is optional, imposed when one fits",
                   "They are the same artefact drawn at two levels of detail"],
             "c": 2,
             "why": "Evolving Order contrasts the two: the map is always needed, while a "
                    "large-scale structure is optional, to be imposed when costs and benefits favour it "
                    "and a fitting structure has been found; a system simple enough to "
                    "understand through its modules does not need one."},
            {"q": "On the preset <code>a-change-neither-fits</code>, how many modules does "
                  "rebalancing-credit reach under each packaging?",
             "a": ["3 by screen and 2 grown",
                   "4 by screen and 3 grown",
                   "3 under both",
                   "2 under both"],
             "c": 2,
             "why": "Station, Trip, Tariff and Rider are in admin-screen, return-screen, "
                    "return-screen and rent-screen: 3 distinct modules. Grown, they are in "
                    "fleet, riding, pricing and riding: 3 again. Four elements is not four "
                    "modules when two share one."},
        ],
        "mistakes": [
            ("Thinking Evolving Order means having no structure until late in the project",
             "Evans argues against a design free-for-all as firmly as against a "
             "straitjacket; the problem he names is the rigidity and source of the rules, "
             "not their existence. Refactoring Toward a Fitting Structure suggests starting "
             "early with something loose, a metaphor or a couple of layers, and changing it "
             "as understanding grows. On the lesson's illustration the grown packaging is "
             "itself a structure; what evolves is which one."),
            ("Adopting a System Metaphor because every project should have one",
             "Evans says few projects have found a really useful metaphor, that people "
             "have pushed the idea where it does harm, and that no project strictly "
             "needs a large-scale structure. The pattern is for the case where a "
             "compelling analogy has already turned up, and it tells the team to abandon "
             "the analogy once it misleads."),
            ("Reading a lower touch count as proof that one packaging is better",
             "The lab counts how far the lesson's changes reach under each packaging. A "
             "different list of changes gives different figures, and the second preset "
             "shows one change that both packagings handle equally badly. Evans chooses "
             "a structure by whether it clarifies the domain for the people working in "
             "it, which no count of four changes settles."),
        ],
        "standard": (
            "Finish when you can read a packaging against the changes it meets.",
            "Given two packagings of the same elements and a list of changes, state the "
            "modules each change touches, the totals, and the changes confined to one "
            "module, and say what each packaging assumed."
        ),
        "note": (
            "The lab counts modules touched by the changes you give it. It cannot say "
            "whether a structure tells a true story about the domain, whether a metaphor "
            "illuminates or misleads, or when a structure has acquired too many "
            "exceptions; Evans leaves those to the team's judgement, revisited as the "
            "system grows."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 16, Responsibility Layers (PDF pp. 277-285 of the operator's copy),
    # including the shipping example (pp. 279-285, summarised only) and Choosing
    # Appropriate Layers (pp. 285-288).
    # Quote: PDF p. 285 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "responsibility-layers",
        "title": "Responsibility Layers",
        "module": "Chapter 16 · Large-Scale Structure",
        "one_line": "Broad layers of responsibility cut along the domain's own strata, each depending only on the layers beneath it.",
        "summary": (
            "Responsibility Layers joins two ideas, layering and responsibility-driven "
            "design, at the scale of the whole model. Read Evans's case for layers that "
            "tell the domain's story, the five he has seen recur, and his advice on "
            "choosing them; then classify a theatre box office's dependencies against "
            "four layers and find the two that run upward."
        ),
        "key": [
            "layers cut along the domain's strata",
            "each layer uses only the layers below",
            "potential, operations, decision support",
            "policy and commitment where they fit",
            "an upward dependency breaks the story",
            "four or five layers at most",
        ],
        "key_label": "Responsibility Layers in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Responsibility layer",
             "A broad responsibility, such as what the business could do or what it is "
             "doing now, cast as a layer. Every object, aggregate and module is factored "
             "to sit inside one of them."),
            ("Relaxed layering",
             "The variant of the layering pattern Evans prefers here: a layer may use any "
             "layer below it, not only the one directly beneath. Only dependencies that "
             "run upward break it."),
            ("Upward dependency",
             "A dependency from an element in one layer to an element in a higher layer. "
             "The lab lists each one; a dependency that skips over a layer on its way down "
             "is counted separately and is allowed."),
        ],
        "read_title": "The pattern, the layers Evans has seen, then the count",
        "read_intro": (
            "Read Responsibility Layers and Choosing Appropriate Layers in your own copy "
            "first. The lesson reads the pattern as a tool, summarises the book's long "
            "example, and then classifies every dependency of a small model of its own."
        ),
        "body": [
            ("p", "&ldquo;Choosing a large-scale structure is less a technical decision than "
                  "a business modeling decision.&rdquo; That line is from Choosing "
                  "Appropriate Layers, at the end of the second pattern of Chapter 16, "
                  "Responsibility Layers. Read the pattern and that section in your own "
                  "copy first."),
            ("p", "Evans starts from objects. Throughout the book each object has a narrow "
                  "set of related responsibilities, but when every one of them is "
                  "handcrafted there is no way to reason about large regions of the model "
                  "at once. In some domains a deep understanding reveals a natural "
                  "stratification: some concepts sit against a background of others that "
                  "change independently, at a different rate and for different reasons. "
                  "Layering is the established way to exploit that, and the chapter "
                  "contrasts it with the layering that sorts itself out when you draw a "
                  "module dependency diagram, which eases tracing but says little about "
                  "the model."),
            ("p", "The pattern unites the two ideas. Name a few broad responsibilities the "
                  "domain itself shows, far wider than any object's, and refactor until "
                  "every object, aggregate and module belongs to exactly one of them. "
                  "Members of a layer may use the layers beneath and know nothing of those "
                  "above. Evans prefers the relaxed variant, Buschmann and his co-authors' "
                  "Relaxed Layered System, in which a layer may reach any lower layer, not "
                  "only the next. The layers should tell the story of the system's "
                  "purpose. This is a different cut from the Layered Architecture of "
                  "Chapter 4, which separates user interface, application, domain and "
                  "infrastructure; Responsibility Layers divides the domain layer itself."),
            ("p", "The book's example is long, and only its shape is summarised here. "
                  "Evans takes the shipping model of earlier chapters and has its team "
                  "notice that schedules can be discussed without the cargo they carry, "
                  "but not the other way round. They name two layers, then a third for "
                  "the routing service once they see it helps decide rather than records "
                  "what is. One attribute turns out to be a policy hiding in a capability "
                  "object, and moving it out makes the model clearer. Then a new "
                  "regulation arrives, and the first design that occurs to them would make "
                  "an operational object depend on a decision-support service; they choose "
                  "another that respects the layers. Evans is careful to say the second "
                  "design is not simply better. Consistency across a team is worth modest "
                  "trade-offs, and if the structure keeps forcing awkward choices, "
                  "Evolving Order says to revise it."),
            ("p", "Choosing Appropriate Layers gives three things to look for and preserve "
                  "as layers are split, merged and redefined. Storytelling: the layers "
                  "should bring out the business's priorities, which is the point of the "
                  "quotation. Conceptual dependency: upper-layer concepts should have "
                  "meaning against the lower ones, while lower ones make sense alone. And "
                  "conceptual contours: where objects change at different rates or for "
                  "different reasons, a layer boundary should run along that shearing "
                  "line."),
            ("p", "Then come five layers Evans has seen recur in enterprise systems, "
                  "offered as examples rather than a template. Potential asks what the "
                  "business could do: its resources, people and contracts. Operations asks "
                  "what it is doing, and like Potential records reality as it is; an "
                  "operational object may refer to potential ones, never the reverse. "
                  "Decision Support asks what should be done, analysing the layers "
                  "beneath. Policy holds rules and goals that constrain the other layers, "
                  "sometimes passed into a lower method, sometimes as a Strategy. "
                  "Commitment, which comes to the fore where capacity depends on current "
                  "business, as in finance or insurance, records what has been promised."),
            ("p", "He ends on restraint. Keep the layering simple: beyond four, or "
                  "possibly five, layers stop telling a story, and the complexity they "
                  "were meant to tame returns in another form. The five layers fit a range "
                  "of enterprise systems, but a domain unlike those may need layers of its "
                  "own, and forcing it into these would do harm. Start somewhere, he says, "
                  "and let the order evolve."),
            ("p", "Now the count. The lab holds a theatre box office in four layers, top to "
                  "bottom <code>decision</code>, <code>policy</code>, "
                  "<code>operations</code> and <code>potential</code>, with eight elements: "
                  "Auditorium, Seat and Usher are potential; Performance, Booking and "
                  "Ticket are operations; ConcessionRule is policy; PricingAdvisor is "
                  "decision support. The first version has eleven dependencies, and among "
                  "them a booking that holds its concession rule, like this:"),
            ("code", _lines(BOOKING_ASKS_POLICY)),
            ("p", "On the preset <code>as-first-written</code> the lab counts 11 "
                  "dependencies: 6 downward, 3 within a layer (Seat on Auditorium, Booking "
                  "on Performance and on Ticket) and 2 upward, listed as Booking on ConcessionRule and "
                  "Auditorium on Performance, the second because each auditorium kept a "
                  "list of its performances. One downward dependency, PricingAdvisor on "
                  "Booking, skips over the policy layer, which relaxed layering allows; "
                  "the lab counts it, 1, and does not list it as a fault. No layer is "
                  "empty: the tile for layers with no element reads none, and a layer the "
                  "story names but nothing fills would be worth asking about."),
            ("p", "The preset <code>refactored</code> turns the first upward dependency "
                  "round, as below: the rule reads the booking, and the booking never "
                  "names the rule. The auditorium's list goes, replaced by asking a "
                  "repository for an auditorium's performances. The lab then counts 10 "
                  "dependencies, 7 downward, 3 within and 0 upward, with the same one "
                  "skip. Whether the policy should own the price at all is a modelling "
                  "question the count does not answer; what it shows is that every "
                  "remaining dependency now runs in the direction the layers' story "
                  "says."),
            ("code", _lines(POLICY_READS_BOOKING)),
            ("h3", "Exercise"),
            ("ul", [
                "A clinic in the same four layers: Clinician and Room are potential; "
                "Appointment and Visit are operations; BookingLimit is policy; "
                "ScheduleOptimizer is decision.",
                "Dependencies, written dependent first: Appointment on Clinician; "
                "Appointment on Room; Visit on Appointment; Clinician on Appointment; "
                "BookingLimit on Appointment; ScheduleOptimizer on Room; Appointment on "
                "BookingLimit.",
            ]),
            ("p", "By hand, sort the seven dependencies into downward, within a layer and "
                  "upward, name the upward ones, and count the downward ones that skip a "
                  "layer. Then type the model into the lab and compare."),
            ("p", "Layers order what a system does. The next lesson, Knowledge Level, reads "
                  "a structure that looks like a layer and is not one: objects whose job is "
                  "to say how other objects may behave."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "layers",
            "preset": "as-first-written",
            "presets": [
                {"id": "as-first-written",
                 "label": "A theatre box office as first written",
                 "layers": THEATRE_LAYERS,
                 "elements": THEATRE_ELEMENTS,
                 "deps": THEATRE_DEPS_FIRST,
                 "expect": {"dmoDeps": "11",
                            "dmoDown": "6",
                            "dmoWithin": "3",
                            "dmoUp": "2: Booking → ConcessionRule, Auditorium → Performance",
                            "dmoSkip": "1",
                            "dmoEmpty": "0: none"}},
                {"id": "refactored",
                 "label": "The same, with the two upward dependencies removed",
                 "layers": THEATRE_LAYERS,
                 "elements": THEATRE_ELEMENTS,
                 "deps": THEATRE_DEPS_REFACTORED,
                 "expect": {"dmoDeps": "10",
                            "dmoDown": "7",
                            "dmoWithin": "3",
                            "dmoUp": "0: none",
                            "dmoSkip": "1"}},
            ],
            "panel_title": "Which dependencies run against the layers",
            "panel_intro": (
                "A count over the small model the lesson states. Layers are listed top to "
                "bottom; each element sits in one, and each dependency is written dependent "
                "first. The layers and the model are the lesson's, not the book's."
            ),
        }),
        "steps_title": "Checking a model against its layers",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Write the layers and their members",
             "List the layers top to bottom and put every element in exactly one. An "
             "element you cannot place is a question about the layers, not a mistake in "
             "the list."),
            ("Classify each dependency",
             "For each dependency, compare the layer of the dependent with the layer of "
             "the one it uses: higher to lower is downward, the same is within, lower to "
             "higher is upward."),
            ("Decide what each upward one means",
             "For every upward dependency, say whether the dependency can be turned round, "
             "replaced by a query, or is evidence that an element sits in the wrong layer "
             "or that the layers need revising."),
            ("Do it on your own system",
             "Pick four broad responsibilities in a system you know, assign ten of its "
             "classes to them, list the dependencies among those ten, and count the "
             "upward ones."),
        ],
        "worked": {
            "title": "Eleven dependencies in the box office",
            "intro": [
                "Classify the dependencies of <code>as-first-written</code> by hand.",
            ],
            "lines": [
                "within potential: Seat on Auditorium",
                "within operations: Booking on Performance, Ticket",
                "down: Performance on Auditorium and Usher",
                "down: Ticket on Seat; rule on Ticket",
                "down: PricingAdvisor on Booking and rule",
                "up: Booking on rule; Auditorium on Performance",
            ],
            "after": [
                "That is 3 within, 6 downward and 2 upward. Of the six downward, only "
                "PricingAdvisor on Booking passes over a layer, from decision to operations "
                "across policy, which the relaxed variant allows.",
            ],
        },
        "quiz_title": "Layers, their order and the book's claims",
        "quiz": [
            {"q": "In the exercise, with layers decision, policy, operations and potential "
                  "from the top, how many of the seven dependencies run upward, and how many "
                  "downward ones skip a layer?",
             "a": ["2 upward; 1 skips",
                   "1 upward; 1 skips",
                   "2 upward; 2 skip",
                   "3 upward; 1 skips"],
             "c": 0,
             "why": "Clinician on Appointment runs from potential up to operations, and "
                    "Appointment on BookingLimit from operations up to policy: 2 upward. "
                    "Downward are Appointment on Clinician, Appointment on Room, "
                    "BookingLimit on Appointment and ScheduleOptimizer on Room, 4, and only "
                    "the last passes over a layer (it passes over two, policy and "
                    "operations, and is one skipping dependency). Visit on Appointment is "
                    "within operations. BookingLimit on Appointment is the policy reading "
                    "operations, which is downward."},
            {"q": "According to Choosing Appropriate Layers, what should the concepts of a "
                  "lower layer be like?",
             "a": ["Meaningful standing alone, without the layers above",
                   "Defined in terms of the layer immediately above",
                   "Changed at the same rate as the layers above",
                   "Implemented in a separate Bounded Context"],
             "c": 0,
             "why": "Conceptual dependency: upper-layer concepts take their meaning against "
                    "the lower layers, and lower ones should make sense alone. Different "
                    "rates of change are a reason to put a boundary between layers, not "
                    "something to equalise, and a layer such as Decision Support may "
                    "become a separate context but need not."},
            {"q": "Which of these is Evans's advice on the number of layers?",
             "a": ["Always use exactly the five he describes",
                   "As many as the domain has strata, however many",
                   "Keep it simple: more than four or five is unwieldy",
                   "Two, Potential and Operations, in every enterprise system"],
             "c": 2,
             "why": "He says more than four, perhaps five, layers grow unwieldy and that "
                    "the structure must be ruthlessly distilled. The five are examples that "
                    "recur in enterprise systems, and a domain unlike them may need layers "
                    "of its own; Potential and Operations alone cover many logistics "
                    "systems but not all."},
            {"q": "On the preset <code>as-first-written</code>, which dependency does the lab "
                  "count as skipping a layer?",
             "a": ["Booking on ConcessionRule",
                   "PricingAdvisor on ConcessionRule",
                   "Performance on Usher",
                   "PricingAdvisor on Booking"],
             "c": 3,
             "why": "PricingAdvisor is in decision and Booking in operations, so the "
                    "dependency passes over policy. PricingAdvisor on ConcessionRule goes to "
                    "the layer directly below, Performance on Usher goes from operations to "
                    "potential directly below it, and Booking on ConcessionRule runs "
                    "upward."},
        ],
        "mistakes": [
            ("Taking Responsibility Layers for the user interface, application, domain and infrastructure layers",
             "Those are Chapter 4's Layered Architecture, which isolates the domain from "
             "everything else in the program. Responsibility Layers divides the domain "
             "layer itself, by broad responsibilities in the business such as what could be "
             "done and what is being done, and the choice of them is, in the quotation's "
             "words, a business modelling decision."),
            ("Treating Evans's five layers as a template every system should fill",
             "Choosing Appropriate Layers offers Potential, Operations, Decision Support, "
             "Policy and Commitment as layers seen in a range of enterprise systems, warns "
             "that forcing a different domain into them would be counterproductive, and "
             "says a domain unlike these may need layers of its own. Evans's advice is to "
             "start somewhere and let the order evolve."),
            ("Counting a dependency that skips a layer as a violation",
             "Evans adopts the relaxed variant of layering, in which a layer may use any "
             "layer below it. Only dependencies that run upward break the structure. The "
             "lab counts skipping dependencies so that you can see them, and lists only "
             "the upward ones as faults."),
        ],
        "standard": (
            "Finish when you can check a model against its responsibility layers.",
            "Given layers, an assignment of elements and a list of dependencies, sort "
            "every dependency into downward, within or upward, name the upward ones, and "
            "count the downward ones that skip a layer."
        ),
        "note": (
            "The lab checks dependencies against the layers you give it. It cannot say "
            "whether those layers tell the domain's story, whether an element belongs in "
            "the layer you put it in, or which of two designs that both respect the "
            "layers is better; Evans treats those as modelling decisions made with domain "
            "experts."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 16, Knowledge Level (PDF pp. 288-294 of the operator's copy),
    # including the payroll and pension example (pp. 289-294, summarised only).
    # Quote: Fowler's definition as Evans quotes it, PDF p. 288 of the
    # operator's copy, 13 words, quotes.py OK. Lesson total: 13 words.
    {
        "slug": "knowledge-level",
        "title": "Knowledge Level",
        "module": "Chapter 16 · Large-Scale Structure",
        "one_line": "A set of ordinary domain objects that describes and constrains how another set may behave, so that a superuser can reconfigure the rules without new code.",
        "summary": (
            "Knowledge Level, a pattern Evans takes from Martin Fowler's Analysis "
            "Patterns, separates the objects that say what kinds of thing are allowed "
            "from the objects that are those things. Read why it untangles "
            "configurable models, how it differs from a layer, and Evans's warnings "
            "about using it; then count the modules four new requirements reach in a "
            "library written with a subclass per borrower category and with a "
            "knowledge level."
        ),
        "key": [
            "objects that describe other objects",
            "rules a superuser can reconfigure",
            "a knowledge level and an operations level",
            "dependencies run both ways: not a layer",
            "built of ordinary domain objects",
            "use it sparingly, where change is crucial",
        ],
        "key_label": "Knowledge Level in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Fowler's, as Evans uses "
            "them (Buschmann's names for them are meta level and base level); the third "
            "is the lab's."
        ),
        "concepts": [
            ("Knowledge level",
             "Objects that describe how other objects may behave: the kinds of thing "
             "the business recognises, and the rules each kind brings. A user with the "
             "right to do so changes them as the business's policies change."),
            ("Operations level",
             "The objects that record what is actually happening, each constrained by "
             "the knowledge-level object it points to. Evans compares the pair to the "
             "base level and meta level of the Reflection pattern."),
            ("A change landing in configuration",
             "In the lab, a change that touches only the data a superuser edits. It "
             "still counts as a module touched; the prose says what the count cannot, "
             "that no code was written."),
        ],
        "read_title": "The pattern, its costs, then the count",
        "read_intro": (
            "Read Knowledge Level in your own copy first. The lesson reads the pattern "
            "as a tool, summarises the book's two-part example, and then counts where "
            "four new requirements land in two designs of the same library."
        ),
        "body": [
            ("p", "A knowledge level is &ldquo;a group of objects that describes how another "
                  "group of objects should behave.&rdquo; Evans opens the third pattern of "
                  "Chapter 16 with that definition, quoted from Martin Fowler's paper on "
                  "accountability. Read the pattern in your own copy first."),
            ("p", "The pattern is Fowler's. It appears in his Analysis Patterns, first in "
                  "modelling accountability in organisations and later in posting rules for "
                  "accounting, and it never has a chapter there, because unlike his other "
                  "patterns it does not model a domain; it structures a model. Evans brings "
                  "it into this chapter for software whose behaviour must be configurable, "
                  "where the roles and relationships among entities have to change when the "
                  "system is installed, or even while it runs."),
            ("p", "The problem is easy to recognise. Organisations arrange their people in "
                  "different ways: one has departments under directors, another units "
                  "under managers, a third reports along two lines at once. An application "
                  "that assumes one arrangement fails the rest, and Evans traces what "
                  "follows: users bend data-entry fields to meanings they were not built "
                  "for, the application's behaviour misfires, features get switched off, "
                  "and years later anyone replacing the system finds that its fields mean "
                  "different things to different users."),
            ("p", "The book works the pattern on an employer's pay and retirement-plan "
                  "model, which is summarised here only. A rule that one class of employee "
                  "must have a particular plan leads the team to an explicit employee-type "
                  "object, which only a superuser may edit. The next morning a developer "
                  "notices that the restricted objects already form a knowledge level, and "
                  "seeing them that way lets a colleague spot a second concept hidden in "
                  "the type and factor it out."),
            ("p", "The general argument sits between two failures. A static model forces "
                  "workarounds; a fully flexible one, allowing any relationship, is hard "
                  "to use and cannot enforce the organisation's own rules. Adding options "
                  "to the operational objects makes them unwieldy: they gain references to "
                  "types to cover many cases, attributes that mean different things in "
                  "different situations, and classes that differ only in how they may be "
                  "assembled. Inside such a model, Evans says, is another model about the "
                  "model. A knowledge level separates it out and makes its constraints "
                  "explicit."),
            ("p", "He relates it to Reflection, as Buschmann and his co-authors describe it "
                  "in Pattern-Oriented Software Architecture: a base level that does the "
                  "work and a meta level that describes the software's structure. Two "
                  "differences matter. A knowledge level is about the business, not the "
                  "language, so it is built from ordinary objects, never from the "
                  "language's reflection tools. And it does not aim at full generality: "
                  "like a Specification beside a general predicate, a narrow set of "
                  "constraints says more about what the designer meant. It is not called a "
                  "layer, because dependencies run both ways between the levels, which is "
                  "also why it is not a special case of the Policy layer of the previous "
                  "lesson."),
            ("p", "The warnings are as strong as the pattern. Evans calls Reflection and "
                  "knowledge levels intoxicating and says to use them sparingly. The "
                  "indirection brings back some of the obscurity it removes; if the "
                  "knowledge level grows complex, the people who configure it need a "
                  "programmer's skills, and a meta-level programmer's at that, and their "
                  "mistakes make the application behave wrongly. Data migration does not "
                  "vanish, since operations-level objects must be dealt with when the "
                  "knowledge level changes. And the design must hold up for every "
                  "configuration a user might later choose. Applied where customisation is "
                  "crucial, he concludes, it solves problems that are very hard to solve "
                  "any other way; and like the other structures it is optional and can sit "
                  "alongside them."),
            ("p", "Now the count. A library lends to students, staff and the public, and "
                  "each category has its own loan period and fines. Written with a "
                  "subclass per category, a new category is a new class, a new case in the "
                  "registration form, and a new branch in the fine calculator where its "
                  "fines differ. Written with a knowledge level, each category is a "
                  "<code>BorrowerCategory</code> object held in a table a superuser edits, "
                  "and every borrower points to one:"),
            ("code", _lines(BORROWER_CATEGORY)),
            ("p", "Four requirements arrive: a visitor category with its own fines, an "
                  "alumni category with the public's fines, longer loans for staff, and an "
                  "amnesty on students' fines during exams. On the preset "
                  "<code>subclass-per-category</code> they touch 3, 2, 1 and 2 modules, 8 "
                  "in all; 1 change stays in one module, and the largest is add-visitor, "
                  "which reaches <code>borrowers</code>, <code>accounts</code> and "
                  "<code>fines</code>. On the preset <code>knowledge-level</code> the first "
                  "three each touch only the category table in "
                  "<code>configuration</code>, 1 module apiece, with no code written."),
            ("p", "The fourth is the instructive one. An exam-time amnesty is a kind of rule "
                  "the fine policy was never built to express, so it reaches "
                  "<code>knowledge</code>, where FinePolicy and BorrowerCategory must learn "
                  "about dates, and <code>configuration</code>, where the amnesty is set "
                  "up: 2 modules, the largest, and 5 touches in all with 3 changes "
                  "confined. The subclass design also needed 2 modules for this change, so "
                  "the knowledge level does not make the amnesty harder. It just does not "
                  "make it easier: a new kind of rule is still new code, now in the "
                  "knowledge level itself. Evans's warnings cover what the count leaves "
                  "out: the superuser who must now configure amnesties correctly, the "
                  "loans already out when the rule changes, and a design that must hold up "
                  "for any configuration users later choose."),
            ("h3", "Exercise"),
            ("ul", [
                "A gym, written with a subclass per kind of class: Session, Yoga, Spin and "
                "Swim are in booking; Reminder is in notices; StudioPlanner is in rooms.",
                "Changes to it: add-pilates touches Pilates (a new class in booking), "
                "Reminder and StudioPlanner; longer-spin touches Spin and StudioPlanner; "
                "swim-reminder-days touches Swim and Reminder; follow-up-booking, which "
                "books the next session automatically, touches Session and Yoga.",
                "The same gym with a knowledge level: Session is in operations, "
                "SessionType in knowledge, TypeTable in configuration. add-pilates, "
                "longer-spin and swim-reminder-days each touch TypeTable; "
                "follow-up-booking touches SessionType, Session and TypeTable.",
            ]),
            ("p", "By hand, find the modules each change touches in each design, the total "
                  "touches, and the changes confined to one module, and say which change "
                  "the knowledge level makes harder. Then type both designs into the lab "
                  "to check."),
            ("p", "A knowledge level lets users reconfigure a model; the last structure of "
                  "the chapter lets whole applications be assembled from parts. The next "
                  "lesson, Pluggable Component Framework, reads it with the sections on how "
                  "restrictive a structure should be."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "preset": "subclass-per-category",
            "presets": [
                {"id": "subclass-per-category",
                 "label": "A library with a subclass per borrower category",
                 "elements": LIBRARY_SUBCLASS_ELEMENTS,
                 "changes": LIBRARY_SUBCLASS_CHANGES,
                 "expect": {"dmoPer": "add-visitor 3, add-alumni 2, longer-staff-loans 1, exam-amnesty 2",
                            "dmoTotal": "8",
                            "dmoConfined": "1 of 4: longer-staff-loans",
                            "dmoLargest": "add-visitor, 3 modules"}},
                {"id": "knowledge-level",
                 "label": "The same library with a knowledge level",
                 "elements": LIBRARY_KNOWLEDGE_ELEMENTS,
                 "changes": LIBRARY_KNOWLEDGE_CHANGES,
                 "expect": {"dmoPer": "add-visitor 1, add-alumni 1, longer-staff-loans 1, exam-amnesty 2",
                            "dmoTotal": "5",
                            "dmoConfined": "3 of 4: add-visitor, add-alumni, longer-staff-loans",
                            "dmoLargest": "exam-amnesty, 2 modules"}},
            ],
            "panel_title": "Where four new requirements land",
            "panel_intro": _CHANGE_INTRO,
        }),
        "steps_title": "Finding where a requirement lands",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Separate the two levels",
             "List the objects that say what kinds of thing exist and what each may do, "
             "and the objects that record what is happening. The first group is the "
             "knowledge level, whether or not anyone has called it that."),
            ("Trace each requirement",
             "For each requirement, write the elements it touches in each design and the "
             "modules they sit in, counting a change to configuration data as a module "
             "touched."),
            ("Find the change it was not built for",
             "Look for a requirement that adds a new kind of rule rather than a new value "
             "of an existing one. It is the requirement a knowledge level does not absorb."),
            ("Do it on your own system",
             "Find a type code or a family of subclasses in a system you know that users "
             "keep asking to extend. List three recent requests, count the modules each "
             "touched, and say which would have been configuration under a knowledge "
             "level."),
        ],
        "worked": {
            "title": "Four requirements against the subclasses",
            "intro": [
                "Count the module touches of <code>subclass-per-category</code> by hand.",
            ],
            "lines": [
                "add-visitor: borrowers, accounts, fines",
                "add-alumni: borrowers, accounts",
                "longer-staff-loans: borrowers",
                "exam-amnesty: fines, borrowers",
                "3 + 2 + 1 + 2 is 8 touches",
                "only longer-staff-loans is confined",
            ],
            "after": [
                "With the knowledge level the same four give 1, 1, 1 and 2, which is 5. "
                "The three ones are rows a superuser edits; the two is new code in the "
                "knowledge level itself.",
            ],
        },
        "quiz_title": "Levels, layers and the book's warnings",
        "quiz": [
            {"q": "In the gym exercise, what are the total module touches with subclasses "
                  "and with a knowledge level, and how many modules does follow-up-booking "
                  "reach in each?",
             "a": ["8 and 6; follow-up-booking reaches 1, then 3",
                   "8 and 6; follow-up-booking reaches 2, then 3",
                   "9 and 6; follow-up-booking reaches 1, then 3",
                   "8 and 4; follow-up-booking reaches 1, then 1"],
             "c": 0,
             "why": "With subclasses, add-pilates reaches booking, notices and rooms (3), "
                    "longer-spin booking and rooms (2), swim-reminder-days booking and "
                    "notices (2), and follow-up-booking only booking, since Session and "
                    "Yoga are both there (1): 8. With the knowledge level the first three "
                    "touch only configuration (1 each), and follow-up-booking reaches "
                    "knowledge, operations and configuration (3): 6. Follow-up booking is a "
                    "new kind of rule, and the knowledge level makes it harder."},
            {"q": "Why, according to Evans, is the pattern not called a knowledge layer?",
             "a": ["Because it is always a separate Bounded Context",
                   "Because dependencies run in both directions between the two levels",
                   "Because it holds no behaviour, only data",
                   "Because it must be built with the language's reflection tools"],
             "c": 1,
             "why": "Like Reflection it involves mutual dependencies, whereas a lower layer "
                    "is independent of the layers above. The knowledge level is built from "
                    "ordinary objects with behaviour, Evans says explicitly not from the "
                    "language's reflection facilities, and nothing makes it a separate "
                    "context."},
            {"q": "Which of these is among the costs Evans names for a knowledge level?",
             "a": ["It removes the need for data migration, which hides errors",
                   "It forbids the use of Specification in the same model",
                   "Whoever configures it may need a meta-level programmer's skills",
                   "It can only be applied after a Pluggable Component Framework"],
             "c": 2,
             "why": "If the knowledge level becomes complex, the users or superuser who "
                    "configure it end up needing programming skill, and their mistakes make "
                    "the application misbehave. Evans says migration problems do not "
                    "completely disappear, the opposite of the first option, and he "
                    "compares the pattern to Specification rather than forbidding it."},
            {"q": "On the preset <code>knowledge-level</code>, which change is the largest, "
                  "and how many modules does it reach?",
             "a": ["add-visitor, 3",
                   "add-visitor, 1",
                   "longer-staff-loans, 1",
                   "exam-amnesty, 2"],
             "c": 3,
             "why": "exam-amnesty touches FinePolicy and BorrowerCategory, both in knowledge, "
                    "and CategoryTable in configuration: 2 modules. The other three touch "
                    "only the category table, 1 each. add-visitor's 3 is its figure under "
                    "the subclass design."},
        ],
        "mistakes": [
            ("Implementing a knowledge level with the language's reflection facilities",
             "Evans is explicit that the language's meta-objects describe the language's "
             "own constructs, and that a knowledge level must be built of ordinary "
             "domain objects. What it borrows from Reflection is the split into two "
             "levels, applied to the business."),
            ("Making the knowledge level as general as possible",
             "The pattern deliberately does not aim at full generality. Evans compares it "
             "to a Specification, which says more than a general predicate: a narrow set "
             "of constraints communicates the designer's intent, while a fully flexible "
             "model cannot enforce the organisation's own rules. On the lesson's "
             "illustration, a level general enough to express any rule would make every "
             "configuration a programming task."),
            ("Believing a knowledge level makes every future change mere configuration",
             "It absorbs the changes its designer foresaw. A new kind of rule reaches into "
             "the knowledge level itself, as the exam amnesty does on the lesson's "
             "illustration, and Evans warns that the design must hold up for every "
             "configuration users may later choose and that existing operational objects "
             "still need migrating when the knowledge changes."),
        ],
        "standard": (
            "Finish when you can say where a requirement lands in each design.",
            "Given a model with subclasses and the same model with a knowledge level, "
            "count the modules each requirement touches in each, and name the requirement "
            "a knowledge level does not absorb."
        ),
        "note": (
            "The lab counts modules touched, and a row in a configuration table counts the "
            "same as a new class. It cannot weigh what Evans weighs: the indirection a "
            "reader must follow, the skill a superuser needs, or the migration of objects "
            "created under the old rules."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 16, Pluggable Component Framework (PDF pp. 294-298 of the
    # operator's copy), with the SEMATECH CIM example and the quilt (pp. 296-298,
    # summarised only); How Restrictive Should a Structure Be? (pp. 298-299);
    # Refactoring Toward a Fitting Structure, Minimalism, Communication and
    # Self-Discipline, Restructuring Yields Supple Design, Distillation Lightens
    # the Load (pp. 299-300).
    # Quote: PDF p. 299 of the operator's copy, 17 words, quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "pluggable-component-framework",
        "title": "Pluggable Component Framework and Fitting Structure",
        "module": "Chapter 16 · Large-Scale Structure",
        "one_line": "Components that plug into an abstract core through one set of interfaces, the most restrictive structure in the chapter, and how to refactor toward a structure that fits.",
        "summary": (
            "The last structure of Chapter 16 lets independently built components work "
            "together through an Abstract Core, at the price of freezing that core. "
            "Read the pattern and its downsides, then the chapter's closing sections on "
            "how restrictive a structure should be and how to refactor toward one; then "
            "count the translators a group of applications needs pairwise and through "
            "one framework interface."
        ),
        "key": [
            "an abstract core of interfaces",
            "components plug in; apps use the core",
            "one translator each, not one a pair",
            "a change to the core reaches everyone",
            "not the first structure, nor the second",
            "keep any structure minimal",
        ],
        "key_label": "Pluggable components in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is from Chapter 15, the second the "
            "pattern's, the third the lab's."
        ),
        "concepts": [
            ("Abstract Core",
             "Chapter 15's distillation of the Core Domain into abstract interfaces and "
             "the interactions between them, with the specialised implementations kept "
             "elsewhere."),
            ("Pluggable Component Framework",
             "A structure in which every component is written against the Abstract "
             "Core's interfaces and every application reaches components only through "
             "them, so that one component can replace another."),
            ("Translator",
             "In the lab, one piece of code that converts between one context's model and "
             "another's, or between a context and the shared interface. Pairwise "
             "integration needs one for every pair; a framework needs one a component."),
        ],
        "read_title": "The pattern, the chapter's closing sections, then the count",
        "read_intro": (
            "Read Pluggable Component Framework and the five sections after it to the end "
            "of Chapter 16 in your own copy first. The lesson reads the pattern as a tool "
            "and the closing sections as Evans's argument about structure in general."
        ),
        "body": [
            ("p", "&ldquo;The most important contribution of the large-scale structure is "
                  "conceptual coherence, and giving insight into the domain.&rdquo; That is "
                  "from How Restrictive Should a Structure Be?, which follows the last "
                  "structure of Chapter 16, Pluggable Component Framework. This lesson reads "
                  "the pattern and the chapter's closing sections. Read them in your own "
                  "copy first."),
            ("p", "This structure belongs to a mature model. Evans says it usually comes "
                  "into play only after a few applications have been built in the same "
                  "domain. The problem it answers is many applications, designed "
                  "independently on the same abstractions, that must work together: "
                  "translating between all their Bounded Contexts limits integration, a "
                  "Shared Kernel is impractical between teams that are not close, and "
                  "duplication raises the cost of everything."),
            ("p", "The pattern, in the lesson's words: make the Abstract Core's interfaces "
                  "and their interactions the only contract, so that one component can be "
                  "swapped for any other that honours it, and an application can work "
                  "with any component without knowing which one it has. The hub is an Abstract Core inside a Shared Kernel, while "
                  "behind each component's interface there may be a different context. "
                  "Components may also share a context, or a kernel of their own, and the "
                  "plug-in interface may be a Published Language. Technical frameworks that "
                  "support the idea are secondary; the pattern is a way of organising "
                  "responsibilities and can be applied inside one Java program."),
            ("p", "Evans is frank about the downsides. The pattern is very hard to apply, "
                  "needing precise interfaces and a model deep enough to put the necessary "
                  "behaviour in the core. Applications are limited: one whose idea of the "
                  "Core Domain differs sharply will find the structure in the way. "
                  "And the core cannot change without changing the protocol of every "
                  "component, so refactoring toward deeper insight in the core more or less "
                  "stops. He points to Fayad and Johnson's survey of such frameworks, calls "
                  "their success mixed, and says this should be neither the first "
                  "large-scale structure a project applies nor the second."),
            ("p", "His example is the SEMATECH CIM Framework for semiconductor factories, "
                  "summarised here only: an industry consortium defined abstract interfaces "
                  "for the domain's basic concepts and a protocol for using them, so that a "
                  "vendor's new machine plugs into any application that keeps to the "
                  "interfaces. The chapter's opening image belongs here too. The AIDS "
                  "Memorial Quilt gathered tens of thousands of panels made by people "
                  "working apart, held together by a few rules about each panel's purpose, "
                  "size and durability."),
            ("p", "How Restrictive Should a Structure Be? sets the four patterns on a line, "
                  "from the loose metaphor to the restrictive framework, and notes that even "
                  "one pattern can be tightened, for instance by fixing how layers "
                  "communicate, such as lower layers announcing events that higher layers "
                  "listen for, so that no dependency runs upward. A tighter structure is "
                  "more uniform, easier to interpret and, if it fits, pushes developers "
                  "toward good designs; it also takes away flexibility they may need, "
                  "especially across contexts built with different technologies. So Evans "
                  "advises resisting the urge to build frameworks around a structure, and "
                  "asks that every structural rule make development easier, which is the "
                  "point of the quotation."),
            ("p", "Refactoring Toward a Fitting Structure answers the charge that "
                  "large-scale structure is waterfall design returning: a useful structure "
                  "can only come from deep understanding, and the practical route to that "
                  "is iterative development, so the structure must be refactored into the "
                  "code as it is found. Four sections say how to keep that affordable. "
                  "Minimalism: deal only with the gravest concerns and settle everything "
                  "else as it comes up; start loose. Communication and Self-Discipline: the whole team must know the "
                  "structure through the Ubiquitous Language, because the structure is "
                  "rarely explicit in the code and no functional test depends on it, so "
                  "without discipline it decays."),
            ("p", "Restructuring Yields Supple Design reports something Evans says he "
                  "cannot fully explain: a design that has had a structure is easier to "
                  "restructure than one that never had one, even into a different kind, "
                  "and one that has had two is easier still. His image, a leather jacket "
                  "that loosens with wear, is the chapter's one light moment. Distillation "
                  "Lightens the Load adds that taking mechanisms and Generic Subdomains out "
                  "of the core leaves less to restructure, and that a generic subdomain "
                  "can be placed to fit the structure simply, within one layer or owned by "
                  "one component."),
            ("p", "Now the count. A museum group runs six applications, collections, "
                  "exhibitions, outward loans, conservation, ticketing and the shop, that "
                  "all need the same few concepts: an object, where it is, and its "
                  "condition. Integrated pairwise, every pair that exchanges data needs a "
                  "translator; plugged into one framework, each application needs one "
                  "translator to and from the core's interfaces. On the preset "
                  "<code>six-pairwise</code>, with each translator working both ways, the "
                  "lab counts 15 translators to build, one for each of the six applications' "
                  "fifteen pairs, and 5 to change when one application's model changes. "
                  "On <code>six-plugged</code>, the scheme the lab calls published, it counts 6 to build and 1 to change. Each "
                  "preset also prints the other scheme's figures and two ratios, pairwise "
                  "over framework: 5/2 ≈ 2.5× to build and 5× to change."),
            ("p", "Pairwise cost grows with the square of the number of applications, the "
                  "framework's in proportion to it. The presets "
                  "<code>twelve-pairwise</code> and <code>twelve-plugged</code> give 66 "
                  "against 12 to build, and 11 against 1 to change, ratios of 11/2 ≈ 5.5× "
                  "and 11×. What the lab does not "
                  "count is Evans's main downside. A change to the core interfaces "
                  "themselves reaches every component at once, 12 of 12, which is why the "
                  "core stops evolving; and the count assumes a model deep enough to write "
                  "the core in the first place, which is the reason he puts this structure "
                  "late."),
            ("h3", "Exercise"),
            ("p", "A group of nine applications must all exchange data. By hand, find the "
                  "translators to build pairwise when each works both ways, and when each "
                  "works in one direction only; the translators to change in each case when "
                  "one application's model changes; the figures through one framework "
                  "interface; and the components a change to the framework's interface "
                  "reaches. Then set the lab to nine to check the figures it counts."),
            ("p", "That ends Chapter 16's four structures. The next lesson, Bringing the "
                  "Strategy Together, reads Chapter 17, where structure, contexts and "
                  "distillation meet on one project."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "protocol",
            "directed": "no",
            "preset": "six-pairwise",
            "presets": [
                {"id": "six-pairwise",
                 "label": "Six museum applications, each pair with a two-way translator",
                 "contexts": "6", "scheme": "pairwise",
                 "expect": {"dcxBuild": "15",
                            "dcxChange": "5",
                            "dcxBuildRatio": "5/2 ≈ 2.5×",
                            "dcxChangeRatio": "5×"}},
                {"id": "six-plugged",
                 "label": "The same six plugged into one framework interface",
                 "contexts": "6", "scheme": "published",
                 "expect": {"dcxBuild": "6",
                            "dcxChange": "1",
                            "dcxOther": "pairwise: 15 to build, 5 to change"}},
                {"id": "twelve-pairwise",
                 "label": "Twelve applications, pairwise",
                 "contexts": "12", "scheme": "pairwise",
                 "expect": {"dcxBuild": "66",
                            "dcxChange": "11",
                            "dcxBuildRatio": "11/2 ≈ 5.5×",
                            "dcxChangeRatio": "11×"}},
                {"id": "twelve-plugged",
                 "label": "Twelve applications through one framework interface",
                 "contexts": "12", "scheme": "published",
                 "expect": {"dcxBuild": "12",
                            "dcxChange": "1"}},
            ],
            "panel_title": "Translators pairwise and through one framework",
            "panel_intro": (
                "A count over the small model the lesson states: n applications that all "
                "exchange data, integrated pair by pair or each through one shared "
                "interface. The applications are the lesson's, not the book's."
            ),
        }),
        "steps_title": "Counting what integration costs",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Count the parties",
             "Write down n, the number of applications or components that must exchange "
             "data, and whether each translator works both ways or one."),
            ("Count pairwise",
             "Two-way translators number n·(n − 1)/2 and one-way ones n·(n − 1). A change "
             "to one application reaches n − 1 two-way translators, or 2·(n − 1) one-way "
             "ones."),
            ("Count through a framework",
             "One translator a component, n in all, and one to change when a component's "
             "own model changes; but a change to the shared interface reaches all n."),
            ("Do it on your own system",
             "Count the systems your team's application exchanges data with and the "
             "integrations among them, and say which interface a change would have to "
             "reach every one of them through."),
        ],
        "worked": {
            "title": "Six applications, both ways",
            "intro": [
                "Work <code>six-pairwise</code> and <code>six-plugged</code> by hand.",
            ],
            "lines": [
                "pairs of six: 6·5/2 = 15 translators",
                "one app changes: its 5 translators",
                "framework: 6 translators, one each",
                "one app changes: its 1 translator",
                "the interface changes: all 6",
            ],
            "after": [
                "The framework wins on every count but the last, and the last is the one "
                "Evans weighs most: it is why he says the core's refinement stops.",
            ],
        },
        "quiz_title": "Frameworks, restriction and refactoring",
        "quiz": [
            {"q": "In the exercise, with nine applications, how many two-way translators "
                  "does pairwise integration need, how many one-way ones, and how many "
                  "components does a change to the framework's interface reach?",
             "a": ["36 two-way, 72 one-way, and 9 components",
                   "36 two-way, 72 one-way, and 1 component",
                   "45 two-way, 90 one-way, and 9 components",
                   "72 two-way, 36 one-way, and 9 components"],
             "c": 0,
             "why": "Two-way: 9·8/2 = 36; one-way: 9·8 = 72. One application's change "
                    "reaches 8 two-way translators or 16 one-way ones pairwise, and 1 "
                    "through the framework, which needs 9 translators in all. A change to "
                    "the framework interface reaches all 9 components. The 45 is 10·9/2, "
                    "counting a tenth party."},
            {"q": "When does Evans say a Pluggable Component Framework should be applied?",
             "a": ["As the first structure, to fix the protocol before teams diverge",
                   "Not as the first large-scale structure, nor the second",
                   "Whenever more than two teams share a Bounded Context",
                   "Only within a single Java program"],
             "c": 1,
             "why": "It needs a mature, deep model, usually after several applications in "
                    "the domain, and he says it should not be the first structure applied "
                    "nor the second. That it can be applied within one Java program is a "
                    "remark that it needs no technical framework, not a limit."},
            {"q": "What, according to Communication and Self-Discipline, makes a large-scale "
                  "structure tend to decay?",
             "a": ["Its rules are enforced by the compiler and break the build",
                   "It is written down in UML, which falls out of date",
                   "Its link to the code is rarely explicit, and no functional test checks it",
                   "It is owned by a separate architecture team"],
             "c": 2,
             "why": "Because the structure's relation to the code is rarely explicit and no "
                    "functional test depends on it, only consistent adherence by everyone, "
                    "through the Ubiquitous Language, keeps it. Most structures are not in "
                    "UML at all, and nothing enforces them automatically."},
            {"q": "What does Evans report in Restructuring Yields Supple Design?",
             "a": ["A structured design is usually easier to transform than one without, even into another kind",
                   "Moving to a different kind of structure means starting the model again",
                   "A design that has had two structures is the hardest to change",
                   "Restructuring is cheap because the structure appears in the code"],
             "c": 0,
             "why": "He observes that designs with a large-scale structure are easier to "
                    "transform, even from metaphor to layers, and that one with two earlier "
                    "structures is easier still, which he says he cannot fully explain. "
                    "He also says each change of structure means a lot of refactoring."},
        ],
        "mistakes": [
            ("Reaching for a pluggable framework at the start of a project",
             "Evans puts it last among the structures for a reason: it needs a model deep "
             "and distilled enough to write the Abstract Core, it usually follows several "
             "applications in the domain, and once in place it freezes the core. He says "
             "it should be neither the first structure applied nor the second."),
            ("Equating the pattern with a technical plug-in platform",
             "Technical frameworks that support it are, he says, a secondary issue, needed "
             "only to solve a real technical problem such as distribution. The pattern is "
             "a conceptual organisation of responsibilities around an Abstract Core and "
             "can be applied within one program."),
            ("Assuming a more restrictive structure is always the safer one",
             "A tighter structure brings uniformity and, when it fits, good designs; it "
             "also removes flexibility developers need, especially across contexts in "
             "different technologies. Evans warns against regimenting a structure into a "
             "framework and asks that every rule make development easier. On the lesson's "
             "illustration, the framework's low counts all assume a core that never has "
             "to change."),
        ],
        "standard": (
            "Finish when you can count what pairwise and framework integration cost.",
            "Given n parties, state the translators to build and to change pairwise, one "
            "way and two ways, and through one framework interface, and the parties a "
            "change to that interface reaches."
        ),
        "note": (
            "The lab counts translators for parties that all exchange data. It cannot say "
            "whether your model is mature enough to write an Abstract Core, how often the "
            "core will need to change, or whether a looser structure would serve; those "
            "are the judgements Evans says should come late."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 17, opening (PDF p. 301 of the operator's copy), Combining
    # Large-Scale Structures and Bounded Contexts (pp. 301-304), Combining
    # Large-Scale Structures and Distillation (p. 304), Assessment First (p. 305).
    # Quote: PDF p. 305 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "bringing-the-strategy-together",
        "title": "Bringing the Strategy Together",
        "module": "Chapter 17 · Bringing the Strategy Together",
        "one_line": "Contexts, distillation and large-scale structure as complements on one project, and an assessment of the present situation before any strategy is chosen.",
        "summary": (
            "Chapter 17 asks how the strategic tools of the last three chapters work on "
            "one project. Read how a structure can sit inside one context or organise "
            "the whole map, how it and distillation explain each other, and the six "
            "questions Evans asks first; then count a bakery chain's effort across its "
            "contexts before and after an assessment."
        ),
        "key": [
            "context, distillation and structure",
            "complements, not substitutes",
            "a structure inside a context or across all",
            "a structure can itself be part of the core",
            "assess the present situation first",
            "refine the answers as you learn",
        ],
        "key_label": "Bringing it together in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Strategic design",
             "The book's name for the decisions that apply across a whole project: which "
             "contexts there are and how they relate, which part is the Core Domain, and "
             "what large-scale structure, if any, organises it all."),
            ("Assessment First",
             "Evans's starting point for strategic design: six questions about the map, "
             "the language, the core, the technology and the team, answered as well as "
             "they can be now and refined later."),
            ("Share of effort on the core",
             "In the lab, the developer-weeks spent on parts marked core divided by the "
             "weeks spent on everything built in house, beside the count of the team's "
             "strongest developers working there."),
        ],
        "read_title": "Three combinations, six questions, then the count",
        "read_intro": (
            "Read Chapter 17 from its opening to the end of Assessment First in your own "
            "copy first. The lesson reads the sections as Evans's argument for using the "
            "three strategic principles together, and then counts one thing an "
            "assessment might change."
        ),
        "body": [
            ("p", "&ldquo;You know less about this project right now than you ever will in "
                  "the future.&rdquo; The sentence is from Assessment First, in Chapter 17, "
                  "Bringing the Strategy Together. This lesson reads the chapter up to "
                  "that section. Read it in your own copy first."),
            ("p", "The chapter opens with the questions a team faces once it has met all "
                  "three strategic principles: how a structure coexists with a Context "
                  "Map, where the building blocks fit, and what to do first. Evans's first "
                  "answer is that none of the three, context, distillation or large-scale "
                  "structure, is an alternative to the others. They complement one another and "
                  "interact in many ways."),
            ("p", "Combining Large-Scale Structures and Bounded Contexts. Chapter 16 "
                  "showed Responsibility Layers inside a single context, which keeps the "
                  "explanation simple and is a common way to use them; a structure held "
                  "within one context raises how much complexity a single unified model "
                  "can carry. But on many "
                  "projects the harder problem is how separate contexts fit together, and "
                  "then the structure can organise the Context Map itself, its vocabulary "
                  "applying across the project. A legacy system that ignores your layers "
                  "need not defeat them: say which layers its services fall in, which "
                  "describes its scope and role concisely, and if it is reached through a "
                  "facade, design each of the facade's services to sit in one layer. A "
                  "team may use the same layers inside its own context as across the map."),
            ("p", "Since each context is its own name space, different contexts could use "
                  "different structures, and the map yet another. Evans allows it, and "
                  "warns that going far down that road erodes what a structure is for: a "
                  "set of concepts the whole project shares."),
            ("p", "Combining Large-Scale Structures and Distillation. The two help each "
                  "other. A structure can show how the modules of the Core Domain relate to "
                  "one another and to the Generic Subdomains. And a structure can itself be "
                  "part of the core: a layering into potential, operations, policy and "
                  "decision support may be an insight fundamental to the business, "
                  "especially useful where a project is split into so many contexts that "
                  "the core's own objects mean nothing across most of it."),
            ("p", "Assessment First is a short list, and here it is in paraphrase. Before "
                  "choosing a strategy, find out where the project stands:"),
            ("ol", [
                "Draw a Context Map, and see whether a consistent one can be drawn or some "
                "relationships are unclear.",
                "Listen to how language is used: is there a Ubiquitous Language, and is it "
                "rich enough to help development?",
                "Ask what matters most: has the Core Domain been named, does a Domain "
                "Vision Statement exist, and could you write one?",
                "Ask whether the project's technology helps a Model-Driven Design or works "
                "against it.",
                "Ask whether the developers have the technical skill the work needs.",
                "Ask whether they know the domain, and whether it interests them.",
            ]),
            ("p", "Evans expects imperfect answers, which is where the quotation comes in, "
                  "and says that first answers already show what most urgently needs "
                  "doing. The map, the vision statement and whatever else the team has "
                  "made should then be refined as the situation changes and insight "
                  "grows."),
            ("p", "Now the count, for the third question. A bakery chain's system is six "
                  "contexts on its map. Bake planning, which turns orders and forecasts "
                  "into each shop's overnight bake, is what distinguishes the chain: the "
                  "core. Shop orders and wholesale accounts support it. Payments, the staff "
                  "rota and the ledger export are generic. The table gives each part's "
                  "kind, its developer-weeks this quarter, and how many of the team's four "
                  "strongest developers work on it; a generic part also says whether it is "
                  "built or bought."),
            ("ul", [
                "bake-planning: core, 20 weeks, 1 strong developer",
                "shop-orders: supporting, 14 weeks, 0",
                "wholesale-accounts: supporting, 10 weeks, 0",
                "payments: generic, 18 weeks, 2, built in house",
                "staff-rota: generic, 12 weeks, 1, built in house",
                "ledger-export: generic, 6 weeks, 0, bought",
            ]),
            ("p", "On the preset <code>as-found</code> the lab counts 74 weeks built in "
                  "house, since only built parts count; 20 of them on the core, 10/37 ≈ "
                  "27.0% of the effort, 24 on supporting parts, 12/37 ≈ 32.4%, and 30 on "
                  "generic parts, 15/37 ≈ 40.5%. One of the four strongest "
                  "developers is on the core and three are on generic parts; 2 generic "
                  "parts are built in house, and buying or adopting a published model for "
                  "them would free 30 weeks. These are the figures the Core Domain and "
                  "Generic Subdomains lessons of the previous course asked about, now "
                  "taken as part of an assessment."),
            ("p", "The preset <code>after-assessment</code> shows one possible response: "
                  "payments and the rota are bought, the core gets 30 weeks and three of "
                  "the strongest developers, and shop orders gets the fourth. The lab "
                  "counts 54 weeks built, 5/9 ≈ 55.6% of them on the core, 4/9 on "
                  "supporting parts, none on generic parts, and 3 of the 4 strongest on "
                  "the core. The counts say where effort went. "
                  "Whether the bought payment system fits the chain, and whether bake "
                  "planning really is what sets it apart, are the questions the assessment "
                  "asks people, not tables."),
            ("h3", "Exercise"),
            ("ul", [
                "viability-forecast: core, 12 weeks, 1 strong developer",
                "member-requests: supporting, 8 weeks, 1",
                "label-printing: generic, 6 weeks, 1, built in house",
                "email-notices: generic, 4 weeks, 0, built in house",
                "accounting: generic, 10 weeks, 0, bought",
            ]),
            ("p", "A seed bank's system, by the lab's rule that only built parts count. By "
                  "hand, find the weeks built in house, the share on the core and on generic "
                  "parts, the strongest developers on the core out of all of them, and the "
                  "weeks that buying the generic parts built in house would free. Then type "
                  "the table into the lab to check."),
            ("p", "An assessment says what is; someone still has to decide what to do. The "
                  "last lesson, Who Sets the Strategy, and a Conclusion, reads who that "
                  "should be, and how the book ends."),
        ],
        "lab": ("dddkit", {
            "mode": "distill",
            "view": "effort",
            "preset": "as-found",
            "presets": [
                {"id": "as-found",
                 "label": "A bakery chain's effort as found",
                 "parts": (
                     "bake-planning, core, 20, 1; shop-orders, supporting, 14, 0; "
                     "wholesale-accounts, supporting, 10, 0; "
                     "payments, generic, 18, 2, build; staff-rota, generic, 12, 1, build; "
                     "ledger-export, generic, 6, 0, buy"
                 ),
                 "expect": {"ddsWeeks": "74",
                            "ddsCore": "10/37 ≈ 27.0%",
                            "ddsSupporting": "12/37 ≈ 32.4%",
                            "ddsGeneric": "15/37 ≈ 40.5%",
                            "ddsStrong": "1 of 4, 1/4 = 25%",
                            "ddsBuilt": "2: payments, staff-rota",
                            "ddsFree": "30"}},
                {"id": "after-assessment",
                 "label": "The same chain after an assessment",
                 "parts": (
                     "bake-planning, core, 30, 3; shop-orders, supporting, 14, 1; "
                     "wholesale-accounts, supporting, 10, 0; "
                     "payments, generic, 18, 0, buy; staff-rota, generic, 12, 0, buy; "
                     "ledger-export, generic, 6, 0, buy"
                 ),
                 "expect": {"ddsWeeks": "54",
                            "ddsCore": "5/9 ≈ 55.6%",
                            "ddsGeneric": "0 = 0%",
                            "ddsStrong": "3 of 4, 3/4 = 75%",
                            "ddsBuilt": "0: none",
                            "ddsFree": "0"}},
            ],
            "panel_title": "Where a team's effort goes, across its contexts",
            "panel_intro": (
                "A count over the small model the lesson states. Each part is one context "
                "on the map, with its kind, its developer-weeks and the strongest "
                "developers on it; a generic part bought or published costs no weeks. The "
                "parts and figures are the lesson's, not the book's."
            ),
        }),
        "steps_title": "Starting from an assessment",
        "steps_intro": "Four steps, the last of them on your own project.",
        "steps": [
            ("Draw the map before anything else",
             "Name every context and its relationships; mark those you cannot classify. "
             "An unclear relationship is the first finding of the assessment."),
            ("Mark the kind of each part",
             "Label each context core, supporting or generic, and say in one sentence why "
             "the core one distinguishes the system."),
            ("Count where effort goes",
             "Total the weeks built in house, the share on the core and on generic parts, "
             "and where the strongest developers are."),
            ("Do it on your own project",
             "Answer Evans's six questions for a project you work on, one line each, and "
             "add the share of last month's effort that went to its core."),
        ],
        "worked": {
            "title": "The bakery chain as found",
            "intro": [
                "Work <code>as-found</code> by hand.",
            ],
            "lines": [
                "built: 20 + 14 + 10 + 18 + 12 = 74",
                "ledger-export is bought: not counted",
                "core: 20/74 = 10/37",
                "generic built: 18 + 12 = 30, 15/37",
                "strongest on core: 1 of 4",
                "buying both generic parts frees 30",
            ],
            "after": [
                "Three of the four strongest developers are on parts the chain could buy. "
                "That is a finding for the assessment, not yet a decision: a bought "
                "payment system must still be integrated and may not fit.",
            ],
        },
        "quiz_title": "Combining the principles, and assessing first",
        "quiz": [
            {"q": "In the seed bank exercise, by the lab's rule, what share of the weeks "
                  "built in house goes to the core, and how many weeks would buying the "
                  "generic parts built in house free?",
             "a": ["2/5 on the core; 10 weeks freed",
                   "2/5 on the core; 20 weeks freed",
                   "3/10 on the core; 10 weeks freed",
                   "3/10 on the core; 20 weeks freed"],
             "c": 0,
             "why": "Built in house: 12 + 8 + 6 + 4 = 30 weeks; accounting is bought and not "
                    "counted. The core has 12 of them, 12/30 = 2/5, and generic parts built "
                    "in house have 6 + 4 = 10, a third, so buying them frees 10. Counting "
                    "accounting too gives 40 weeks and 3/10, or 20 freed, which is the lab's "
                    "rule broken. One of the three strongest developers is on the core."},
            {"q": "How does Chapter 17 describe the relation between context, distillation "
                  "and large-scale structure?",
             "a": ["Alternatives: a project chooses one of the three",
                   "A sequence: contexts first, then distillation, then structure, never overlapping",
                   "Complements that interact, not substitutes for one another",
                   "Structure replaces the Context Map once it is in place"],
             "c": 2,
             "why": "Evans calls them complementary and says they interact in many ways: a "
                    "structure can live within a context or organise the map, and it can "
                    "explain or even be part of the core. Evolving Order had already said "
                    "the map is not optional and the structure is."},
            {"q": "Suppose a legacy system's organisation does not fit your Responsibility "
                  "Layers. What does Chapter 17 suggest?",
             "a": ["Give up the layers for the whole project",
                   "Rewrite the legacy system to follow the layers first",
                   "Acknowledge its place: say which layers its services fall in, and fit each facade service to one layer",
                   "Leave it off the Context Map"],
             "c": 2,
             "why": "You need not give up the layers; you acknowledge where the legacy "
                    "actually sits. Saying it fits within particular layers describes its "
                    "scope and role, and if it is reached through a facade, each of the "
                    "facade's services can be designed to fit one layer."},
            {"q": "Which of these is one of the six questions of Assessment First?",
             "a": ["How many layers should the large-scale structure have?",
                   "Are the developers knowledgeable about the domain, and interested in it?",
                   "Which framework should the architecture team build?",
                   "How many translators will the Context Map need?"],
             "c": 1,
             "why": "The six concern the Context Map, the use of language, the Core Domain "
                    "and vision statement, whether the technology works for a Model-Driven "
                    "Design, the developers' technical skill, and their knowledge of and "
                    "interest in the domain. Choosing a structure comes after the "
                    "assessment."},
        ],
        "mistakes": [
            ("Choosing between contexts, distillation and structure as if they were rival approaches",
             "Evans says plainly they are not substitutes: they complement one another. A "
             "structure can organise the Context Map, a context can keep its own local "
             "structure, and a layering can be part of the Core Domain's insight. A "
             "project usually needs all three in some measure, a Context Map always."),
            ("Designing the strategy before assessing the present",
             "Assessment First puts six questions before any strategic choice, about the "
             "map, the language, the core, the technology and the team. Their first "
             "answers are expected to be imperfect and to be refined, but they already "
             "show what most urgently needs doing."),
            ("Using a different structure in every context and calling it a strategy",
             "Since each context is its own name space it is possible, and Evans allows "
             "it, but he warns that going far down that path erodes a structure's value "
             "as concepts the whole project shares."),
        ],
        "standard": (
            "Finish when you can assess where a project's effort goes.",
            "Given a project's parts with their kind, weeks and strongest developers, "
            "state the weeks built in house, the shares on the core and on generic parts, "
            "and the weeks buying would free, and name two of Evans's six questions the "
            "table does not answer."
        ),
        "note": (
            "The lab counts effort across the parts you list. It answers part of one of "
            "Evans's six questions. Whether the map is consistent, whether the language "
            "is rich, whether the technology helps and whether the team knows the domain "
            "are found by looking and asking, and the counts are only as good as the "
            "kinds you assigned."
        ),
    },
]
