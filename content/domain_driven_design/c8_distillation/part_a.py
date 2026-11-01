"""Distillation, lessons 1-5 -- Chapter 15 of Evans's Domain-Driven Design.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), Chapter 15, Distillation: Core Domain, Generic
Subdomains, Domain Vision Statement, Highlighted Core, Cohesive Mechanisms,
Segregated Core and Abstract Core, with the sections between them. Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter,
section and pattern. Every quotation is copied from that copy and checked with
quotes.py. The projects, classes, weeks and code are written for these lessons:
none of the book's examples, figures or tables is reproduced, and none of its
example domains is used as lab data. The design is
docs/domain-driven-design/PLAN.md, section C, Course 8.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- lab data

# The bike-share project of lessons 1 and 2: eight parts, 100 developer-weeks,
# three strongest developers. Each record is part, kind, weeks, strong.
BIKES_DRIFTED = (
    "rebalancing, core, 16, 0; "
    "demand-forecast, core, 8, 0; "
    "payments, generic, 18, 1; "
    "login, generic, 10, 1; "
    "map-tiles, generic, 12, 1; "
    "rider-accounts, supporting, 14, 0; "
    "dock-repairs, supporting, 14, 0; "
    "messaging, generic, 8, 0"
)

BIKES_CORE_FIRST = (
    "rebalancing, core, 30, 2; "
    "demand-forecast, core, 16, 1; "
    "payments, generic, 12, 0; "
    "login, generic, 6, 0; "
    "map-tiles, generic, 6, 0; "
    "rider-accounts, supporting, 14, 0; "
    "dock-repairs, supporting, 10, 0; "
    "messaging, generic, 6, 0"
)

# Lesson 2: the drifted project with an option on each generic part.
BIKES_ALL_BUILT = (
    "rebalancing, core, 16, 0; "
    "demand-forecast, core, 8, 0; "
    "payments, generic, 18, 1, build; "
    "login, generic, 10, 1, build; "
    "map-tiles, generic, 12, 1, build; "
    "rider-accounts, supporting, 14, 0; "
    "dock-repairs, supporting, 14, 0; "
    "messaging, generic, 8, 0, build"
)

BIKES_BOUGHT = (
    "rebalancing, core, 16, 0; "
    "demand-forecast, core, 8, 0; "
    "payments, generic, 18, 0, buy; "
    "payments_fit, supporting, 3, 1; "
    "login, generic, 10, 0, outsource; "
    "map-tiles, generic, 12, 0, buy; "
    "map_fit, supporting, 1, 1; "
    "rider-accounts, supporting, 14, 0; "
    "dock-repairs, supporting, 14, 0; "
    "messaging, generic, 8, 1, build"
)

BIKES_FREED_TO_CORE = (
    "rebalancing, core, 40, 2; "
    "demand-forecast, core, 20, 1; "
    "payments, generic, 18, 0, buy; "
    "payments_fit, supporting, 3, 0; "
    "login, generic, 10, 0, outsource; "
    "map-tiles, generic, 12, 0, buy; "
    "map_fit, supporting, 1, 0; "
    "rider-accounts, supporting, 14, 0; "
    "dock-repairs, supporting, 14, 0; "
    "messaging, generic, 8, 0, build"
)

# Lesson 3: the bike-share model's twelve classes, with the weeks spent on
# each so far, flagged two ways.
CLASSES_NARROW = (
    "DemandForecast, core, 6, 1; "
    "RebalancingPlan, core, 6, 1; "
    "Move, core, 2, 0; "
    "Station, supporting, 4, 0; "
    "Dock, supporting, 3, 0; "
    "Bike, supporting, 2, 0; "
    "VanRun, supporting, 4, 1; "
    "Trip, supporting, 4, 0; "
    "Fare, supporting, 2, 0; "
    "RepairTicket, supporting, 2, 0; "
    "Rider, generic, 3, 0; "
    "Payment, generic, 2, 0"
)

CLASSES_BROAD = (
    "DemandForecast, core, 6, 1; "
    "RebalancingPlan, core, 6, 1; "
    "Move, core, 2, 0; "
    "Station, core, 4, 0; "
    "Dock, core, 3, 0; "
    "Bike, core, 2, 0; "
    "VanRun, core, 4, 1; "
    "Trip, supporting, 4, 0; "
    "Fare, supporting, 2, 0; "
    "RepairTicket, supporting, 2, 0; "
    "Rider, generic, 3, 0; "
    "Payment, generic, 2, 0"
)

# Lesson 4: a school timetable. Each record is element, module with the
# mechanism tangled into the domain classes, module with it separated.
TIMETABLE_ELEMENTS = (
    "Lesson, timetable, timetable; "
    "Timetable.place, timetable, timetable; "
    "Timetable.clashes, timetable, timetable; "
    "Teacher.canTake, staff, staff; "
    "Room.canHold, rooms, rooms; "
    "overlaps, timetable, intervals; "
    "merge, staff, intervals; "
    "gaps, staff, intervals; "
    "span, rooms, intervals"
)

TIMETABLE_CHANGES = (
    "minutes-not-periods, overlaps; minutes-not-periods, merge; "
    "minutes-not-periods, gaps; minutes-not-periods, span; "
    "touching-periods-ok, overlaps; "
    "five-a-day, Teacher.canTake; "
    "cleaning-gap, Room.canHold; cleaning-gap, gaps"
)

# Lesson 5: the bike-share model's classes and dependencies (from, to), packaged
# by history (module) and with the core segregated (module2).
BIKE_MODEL_ELEMENTS = (
    "Station, stations, stations; "
    "Dock, stations, stations; "
    "DemandForecast, stations, rebalancing; "
    "Bike, fleet, fleet; "
    "RepairTicket, fleet, fleet; "
    "Move, fleet, rebalancing; "
    "RebalancingPlan, ops, rebalancing; "
    "VanRun, ops, fleet; "
    "Rider, riders, riders; "
    "Trip, riders, riders; "
    "Fare, riders, riders; "
    "Payment, riders, riders"
)

BIKE_MODEL_DEPS = (
    "Dock, Station; Bike, Dock; Trip, Bike; Trip, Rider; Trip, Station; "
    "Fare, Trip; Payment, Fare; Payment, Rider; "
    "DemandForecast, Trip; DemandForecast, Station; "
    "RebalancingPlan, DemandForecast; RebalancingPlan, Move; "
    "Move, Station; Move, Bike; VanRun, Move; RepairTicket, Bike; "
    "RebalancingPlan, RepairTicket; Station, DemandForecast"
)

# The same model remodelled around an abstract core: two interfaces, Place and
# DemandSource, carry the interactions the specialised modules had with each other.
# Packaged with each interface beside its implementer (module), and with both in
# the core module (module2).
ABSTRACT_ELEMENTS = (
    "Place, stations, rebalancing; DemandSource, riders, rebalancing; "
    "DemandForecast, rebalancing, rebalancing; "
    "RebalancingPlan, rebalancing, rebalancing; Move, rebalancing, rebalancing; "
    "Station, stations, stations; Dock, stations, stations; "
    "Bike, fleet, fleet; RepairTicket, fleet, fleet; VanRun, fleet, fleet; "
    "Rider, riders, riders; Trip, riders, riders; Fare, riders, riders; "
    "Payment, riders, riders"
)

ABSTRACT_DEPS = (
    "Dock, Station; Station, Place; Bike, Place; Trip, Bike; Trip, Rider; "
    "Trip, Place; Trip, DemandSource; Fare, Trip; Payment, Fare; Payment, Rider; "
    "DemandForecast, DemandSource; DemandForecast, Place; "
    "RebalancingPlan, DemandForecast; RebalancingPlan, Move; Move, Place; "
    "VanRun, Move; RepairTicket, Bike"
)


# ---------------------------------------------------------------- snippets

# 8.4 Cohesive Mechanisms: the clash rule stated through the mechanism's interface.
CLASH_RULE = """// In the timetable package: the rule, in the school's own terms.
boolean clashes(Lesson a, Lesson b) {
    boolean shared = a.teacher().equals(b.teacher())
            || a.room().equals(b.room())
            || a.group().equals(b.group());
    return shared && a.slot().overlaps(b.slot());
}

// In the intervals package: the arithmetic, knowing nothing of schools.
final class Interval {
    private final int start;   // minutes after midnight
    private final int end;     // exclusive
    Interval(int start, int end) { this.start = start; this.end = end; }
    boolean overlaps(Interval other) {
        return start < other.end && other.start < end;
    }
    int minutes() { return end - start; }
}"""

# 8.5 Abstract Core: the two interfaces and the value at the centre of the core.
ABSTRACT_CORE = """// In the rebalancing module: the abstract core.
interface Place {
    String name();
    int bikesAvailable();
    int docksFree();
}

interface DemandSource {
    int departures(Place place, int hour);
    int arrivals(Place place, int hour);
}

final class Move {
    final Place from;
    final Place to;
    final int bikes;
    Move(Place from, Place to, int bikes) {
        this.from = from; this.to = to; this.bikes = bikes;
    }
}"""


_EFFORT_INTRO = (
    "A count over the small model the lesson states. Each record is one part of a "
    "project: its kind, the developer-weeks it takes, and how many of the team's "
    "strongest developers work on it. The lab adds the weeks and the developers by "
    "kind. Which part is the core is the team's choice, which the book weighs; the "
    "lab only counts what that choice does to the shares."
)

_CHANGE_INTRO = (
    "A count over the small model the lesson states. Each element sits in one module "
    "under each packaging, and each change touches the elements listed for it. The "
    "lab counts the modules each change reaches. It cannot see how easily a module "
    "reads, which is most of what the book claims for a separated mechanism."
)

_COHESION_INTRO = (
    "A count over the small model the lesson states. Each dependency runs from one "
    "class to another; the lab places both ends in their modules and counts those "
    "inside a module, those across, and the cycles between modules. Whether a module "
    "means something in the domain is the book's question, and the lab cannot ask it."
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 15, opening (PDF p. 247 of the operator's copy); Core Domain
    # (pp. 248-250); Choosing the Core (p. 250); Who Does the Work? (pp. 250-251);
    # An Escalation of Distillations (p. 251).
    # Quote: PDF p. 249 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "core-domain",
        "title": "Core Domain",
        "module": "Chapter 15 · Distillation",
        "one_line": "The part of the model that sets the system apart and justifies building it, kept small, kept visible, and given the team's best people.",
        "summary": (
            "Chapter 15 opens Evans's second strategic principle, distillation, with the "
            "pattern everything else in it serves: the Core Domain. Read his case that "
            "the most valuable part of a model is the one most easily neglected, how a "
            "team chooses it and who should build it, and then count where a bike-share "
            "team's weeks and strongest developers go."
        ),
        "key": [
            "the core is what makes it worth building",
            "boil the model down and keep the core small",
            "put the strongest developers on the core",
            "the team chooses the core, and revises it",
            "the core can rarely be bought",
        ],
        "key_label": "Core Domain in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Distillation",
             "Separating a mixture to keep its most valuable part. For Evans a model is "
             "already a distillation of what the experts know; Chapter 15 steps back and "
             "distils the model as a whole, telling the part that matters most apart "
             "from the parts that support it."),
            ("Core Domain",
             "The part of the model that is distinctive and central to what the "
             "application is for: the reason to build the software rather than buy it. "
             "Everything else in the model supports it, however necessary it is."),
            ("Strongest developers",
             "In the lab, the `strong` column: how many of the team's most capable "
             "developers work on a part. Who counts as strongest is the team's own "
             "judgement; the lab only adds the numbers you give it."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 15 and the Core Domain pattern with the three "
            "sections after it in your own copy first. The lesson sets out the argument, "
            "then counts where one team's effort goes."
        ),
        "body": [
            ("p", "&ldquo;The planning process must drive resources to the most crucial "
                  "points in the model and design.&rdquo; Evans writes it in the Core Domain "
                  "pattern, the first of Chapter 15, Distillation, and the rest of the "
                  "chapter is a set of ways to make those points easy to find. This lesson "
                  "reads the chapter's opening, the pattern, and three short sections after "
                  "it: Choosing the Core, Who Does the Work? and An Escalation of "
                  "Distillations. Read them in your own copy first."),
            ("p", "The chapter starts from a limit of Layered Architecture. Layers keep the "
                  "domain apart from the technical code that keeps a computer running, "
                  "but in a big system the domain by itself can still be too complex to "
                  "manage. Distillation, Evans says, separates a mixture so that its essence "
                  "can be drawn off, and a model is already a distillation of knowledge. "
                  "Here he takes the strategic view and distils the model as a whole. Done "
                  "well, it gives the whole team a grasp of the overall design, a core small "
                  "enough to enter the Ubiquitous Language, a guide for refactoring, a focus "
                  "for work where the value is, and a basis for deciding what to outsource, "
                  "what to buy and who works on what."),
            ("p", "The Core Domain pattern names two costs of losing sight of the core. The "
                  "first belongs to any design that is hard to understand: people get lost "
                  "outside their own corner, so they specialise; knowledge stops moving; "
                  "behaviour gets written twice because nobody knew it existed. The second "
                  "is particular to distillation. Not every part of a design can be equally "
                  "refined, so priorities are set whether or not anyone sets them, and "
                  "Evans observes that scarce skilled developers drift towards "
                  "infrastructure and towards problems that are neatly defined and need no "
                  "special knowledge of the business. Those look interesting and travel well "
                  "on a CV. The specialised core is then often built by less experienced "
                  "hands, feature by feature from a database schema, and the application "
                  "never does anything compelling however good its plumbing is."),
            ("p", "His story is from a project to build a system for syndicated loans. The "
                  "strong developers were busy with database mapping and messaging, and the "
                  "one experienced object designer who worked on the domain built an elegant, "
                  "general way to attach comments to long-lived objects, which went into "
                  "production and was useful. It was also peripheral. Meanwhile the loan "
                  "module, the reason for the system, was being tangled by a developer out "
                  "of his depth, and the project nearly did not recover."),
            ("p", "So the pattern, as you would apply it: decide which part of the model is "
                  "the core, make it easy for anyone to see, and keep it as small as you can. "
                  "Staff it with your best developers and hire with it in mind, aim its "
                  "effort at deepening the model and making the design supple, and ask of "
                  "every other investment what it does for the core. "
                  "Evans adds that the hard decision makes several easy ones. Make the core "
                  "distinctive and the rest as generic as you practically can; if anything "
                  "is to be kept secret, it is the core; and when time allows only one of "
                  "two good refactorings, choose the one that does more for the core."),
            ("p", "Choosing the Core warns that the answer depends on where you stand. Many "
                  "applications need a plain model of money, but for software that trades "
                  "currencies a richer money model is the core, and even there some of it "
                  "is generic. One application's core is another's supporting component. "
                  "Within one project, and usually one company, a consistent core can be "
                  "agreed, and the agreement should change with the iterations: objects "
                  "that look central at the start can turn out to play supporting roles."),
            ("p", "Who Does the Work? names the circle that keeps the strongest developers "
                  "away. They seldom know the domain, so they are given supporting work, so "
                  "they never learn it. Evans's remedy is a team of strong developers who "
                  "mean to stay and to become holders of domain knowledge, paired with "
                  "domain experts who know the business deeply. A short-term outside "
                  "designer takes the knowledge away when the contract ends, though a "
                  "mentor who teaches design is valuable. Nor can the core usually be "
                  "bought: industry model frameworks have so far disappointed, except as "
                  "Published Languages for exchanging data. If a framework constrains your "
                  "core, he says, either you are giving up an asset and should back off, or "
                  "the area is less central than you thought and the core should be redrawn, "
                  "or you have no special needs and should look at buying software to integrate "
                  "with your own."),
            ("p", "An Escalation of Distillations then orders the chapter's other techniques "
                  "by how far each changes the design. A Domain Vision Statement costs "
                  "little; a Highlighted Core helps decisions without changing the code; "
                  "separating Generic Subdomains and Cohesive Mechanisms takes refactoring "
                  "and repackaging; a Segregated Core makes the core visible in the code "
                  "itself; and an Abstract Core, the most ambitious, reorganises the model "
                  "around its most fundamental concepts. This course reads them in roughly "
                  "that order."),
            ("p", "Now the count, on a project written for the lesson: a city bike-share, "
                  "whose distinctive problem is rebalancing, forecasting where riders will "
                  "want bikes and planning van runs to move them there. Its eight parts "
                  "are listed with a kind, the developer-weeks spent, and how many of the "
                  "team's three strongest developers work on each. The preset "
                  "<code>as-it-drifted</code> is the team as it arranged itself: of 100 "
                  "weeks, 24 are on the two core parts, rebalancing and the demand forecast, "
                  "48 on the four generic ones, payments, login, map tiles and "
                  "messaging, and the other 28 on the two supporting parts. None of the three strongest developers is on the core; one "
                  "each is on payments, login and map tiles."),
            ("p", "The figures are the shape Evans describes, not a judgement of it: on the "
                  "lesson's illustration, the parts that are easiest to define without "
                  "knowing about bikes have taken half the weeks and all of the strongest "
                  "people. The preset <code>core-first</code> is the same eight parts after "
                  "a planning decision: 46 of the 100 weeks are on the core and 30 on "
                  "generic parts, and all three strongest developers work on rebalancing "
                  "and the forecast. The lab cannot tell you that rebalancing is the core. "
                  "That is the choice the section on Choosing the Core leaves to the team, "
                  "and the lab only counts what the choice does once it is made."),
            ("h3", "Exercise"),
            ("ul", [
                "A clinic's booking system, whose team agrees that triage scheduling, "
                "booking the most urgent patients first with a suitable clinician, is the "
                "core.",
                "Parts (part, kind, weeks, strongest developers): triage-scheduling, core, "
                "10, 0; patient-records, supporting, 14, 0; billing, generic, 15, 2; login, "
                "generic, 6, 1; reminders, generic, 5, 0.",
            ]),
            ("p", "By hand, find the total weeks, the share of them on the core, the share "
                  "on generic parts, and how many of the strongest developers are on the "
                  "core out of how many in all. Then type the parts into the lab to check "
                  "your figures."),
            ("p", "Knowing where the core is says nothing yet about what to do with the "
                  "rest. The next lesson, Generic Subdomains, reads Evans's four ways of "
                  "getting the parts you would rather not build."),
        ],
        "lab": ("dddkit", {
            "mode": "distill",
            "view": "effort",
            "preset": "as-it-drifted",
            "presets": [
                {"id": "as-it-drifted",
                 "label": "The bike-share team as it arranged itself",
                 "parts": BIKES_DRIFTED,
                 "expect": {"ddsWeeks": "100", "ddsCore": "6/25 = 24%", "ddsSupporting": "7/25 = 28%",
                            "ddsGeneric": "12/25 = 48%", "ddsStrong": "0 of 3, 0 = 0%"}},
                {"id": "core-first",
                 "label": "The same parts after planning put the core first",
                 "parts": BIKES_CORE_FIRST,
                 "expect": {"ddsWeeks": "100", "ddsCore": "23/50 = 46%", "ddsGeneric": "3/10 = 30%",
                            "ddsStrong": "3 of 3, 1 = 100%"}},
            ],
            "panel_title": "Where a team's weeks and strongest developers go",
            "panel_intro": _EFFORT_INTRO,
        }),
        "steps_title": "Finding where the effort goes",
        "steps_intro": "Four steps, the last of them on a project of your own.",
        "steps": [
            ("Name the core",
             "Write one sentence saying what makes the system worth building rather than "
             "buying, and mark the parts that sentence is about as core."),
            ("Sort the rest",
             "Mark each other part generic if many unrelated businesses would need it in "
             "much the same form, and supporting otherwise."),
            ("Add the weeks and the people",
             "Total the developer-weeks by kind, divide the core's by the whole, and "
             "count the strongest developers on core parts against all of them."),
            ("Do it on your own project",
             "List the parts of a system you work on with their kind, rough weeks and "
             "strongest developers, type them into the lab, and write down the share of "
             "weeks and of strongest developers on what you called the core."),
        ],
        "worked": {
            "title": "The bike-share as it drifted",
            "intro": [
                "Find the shares in <code>as-it-drifted</code>.",
            ],
            "lines": [
                "core: rebalancing 16 + forecast 8, so 24",
                "generic: 18 + 10 + 12 + 8, so 48",
                "supporting: 14 + 14, so 28",
                "total: 24 + 48 + 28, so 100 weeks",
                "core share 24 of 100, generic 48 of 100",
                "strongest on core: 0 of 3 in all",
            ],
            "after": [
                "Every figure follows from the table once the kinds are written in. "
                "Writing them in is the hard part, and it is the part Evans gives to the "
                "team: rebalancing is the core here because the lesson says what the "
                "bike-share is for.",
            ],
        },
        "quiz_title": "The core, who builds it, and Evans's claims",
        "quiz": [
            {"q": "In the exercise, what share of the clinic's weeks is on the core, and how "
                  "many of the strongest developers work there?",
             "a": ["10 of 50 weeks, a fifth, and 0 of the 3 strongest developers",
                   "10 of 40 weeks, a quarter, and 0 of the 3 strongest developers",
                   "10 of 50 weeks, a fifth, and 2 of the 3 strongest developers",
                   "24 of 50 weeks, about half, and 0 of the 3 strongest developers"],
             "c": 0,
             "why": "The weeks are 10 + 14 + 15 + 6 + 5 = 50, of which triage scheduling's "
                    "10 are core: a fifth. The generic parts, billing, login and reminders, "
                    "take 15 + 6 + 5 = 26 weeks, 52 per cent. The strongest developers are "
                    "2 on billing and 1 on login, 3 in all, and none on the core. Leaving "
                    "out patient records gives 40; the 2 belong to billing; 24 adds the "
                    "core to patient records, which is supporting."},
            {"q": "According to the Core Domain pattern, where do scarce, highly skilled "
                  "developers tend to go if nobody plans otherwise?",
             "a": ["To the core, because it is the hardest part",
                   "To user interfaces, which users see first",
                   "To technical infrastructure and to neatly defined problems that need no "
                   "special domain knowledge",
                   "To whichever part was started first"],
             "c": 2,
             "why": "Evans says they gravitate to infrastructure and to problems that can be "
                    "understood without specialised domain knowledge, which look interesting "
                    "and build transferable skills. The core then tends to be built by less "
                    "skilled developers, which is the syndrome his loan-system story shows."},
            {"q": "Who Does the Work? names three likely possibilities when a framework "
                  "constrains your core more than by sparing you its generic parts. Which "
                  "is not one of them?",
             "a": ["You are losing an essential asset, and should back off the framework",
                   "The area is less pivotal than you thought, and the core should be redrawn",
                   "You have no special needs, and should consider buying software",
                   "The framework is immature, and you should wait for its next version"],
             "c": 3,
             "why": "The three are losing an asset, redrawing the core's boundary, and buying "
                    "because there are no special needs. Evans does say more workable "
                    "frameworks may come as the field advances, but he gives no advice to "
                    "wait; his conclusion is a stable team building a rich model, with no "
                    "shortcuts."},
            {"q": "On <code>as-it-drifted</code>, the team moves one strongest developer "
                  "from payments to rebalancing and changes no weeks. What changes in the "
                  "lab?",
             "a": ["The core's share of weeks rises above 24 of 100",
                   "Strongest developers on the core goes from 0 of 3 to 1 of 3; the shares "
                   "of weeks stay the same",
                   "The generic share falls, since payments has fewer people",
                   "Nothing: the lab counts weeks, not people"],
             "c": 1,
             "why": "The weeks column is unchanged, so 24 of 100 on the core and 48 of 100 "
                    "on generic parts stay as they were. The strong column moves 1 from a "
                    "generic part to a core part, so the count on the core becomes 1 of 3. "
                    "Weeks and people are counted separately because the chapter cares about "
                    "both."},
        ],
        "mistakes": [
            ("Taking the core to be the hardest or most essential-looking part",
             "Evans grants that every part of a large system is complicated and necessary "
             "to success; that is the problem the pattern starts from. The core is the part "
             "that is distinctive and central to what the application is for. Payments, "
             "login and a database mapping layer can be hard and indispensable and still "
             "not be it, which is why skilled developers can spend a project on them while "
             "the core is neglected. On the lesson's illustration the generic parts take 48 "
             "of 100 weeks and every strongest developer."),
            ("Expecting to buy the core as an industry framework",
             "Who Does the Work? says the core is unlikely to be purchasable: the industry "
             "model frameworks Evans names have not been compelling except as Published "
             "Languages, and the greatest value of custom software is total control of the "
             "core. A framework that spares you generic work is welcome; one that constrains "
             "the core means one of his three possibilities."),
            ("Fixing the core at the start of the project",
             "Choosing the Core says the identification should evolve through iterations, "
             "and that what looks central at first may turn out to be supporting. It also "
             "depends on the application: a money model is generic in most systems and core "
             "in one that trades currencies. What should be consistent is the team's shared "
             "answer at any one time, not the answer for ever."),
        ],
        "standard": (
            "Finish when you can say where a team's effort goes relative to its core.",
            "Given a project's parts with kind, weeks and strongest developers, state the "
            "share of weeks on the core and on generic parts and the strongest developers "
            "on the core, and give Evans's reason the two tend to drift apart."
        ),
        "note": (
            "The lab adds weeks and developers. It cannot say which part is the core, "
            "whether a developer is strong, or whether the weeks were well spent; those are "
            "the team's judgements, and Evans expects the first of them to change as the "
            "project learns."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Generic Subdomains (PDF pp. 252-254 of the operator's copy): the four
    # options (pp. 252-254); A Tale of Two Time Zones (pp. 254-256); Generic
    # Doesn't Mean Reusable (p. 256); Project Risk Management (p. 256).
    # Quote: PDF p. 252 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "generic-subdomains",
        "title": "Generic Subdomains",
        "module": "Chapter 15 · Distillation",
        "one_line": "The parts of the model many businesses would need, factored into modules of their own and bought, adopted, outsourced or built with less of the team's best effort.",
        "summary": (
            "The first distillation that changes the design: find the subdomains that are "
            "not why the project exists, separate them, and decide how to get each one. "
            "Read Evans's four options with their advantages and drawbacks, why generic "
            "does not mean reusable, and why the first system should not be built on a "
            "generic part; then count the weeks a decision to buy frees."
        ),
        "key": [
            "generic: needed by many businesses",
            "factor it into a module of its own",
            "keep your own specialties out of it",
            "buy, publish, outsource or build",
            "generic does not mean designed for reuse",
            "build the first system on the core",
        ],
        "key_label": "Generic Subdomains in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Generic Subdomain",
             "A cohesive part of the model that is genuinely part of the domain but "
             "abstracts concepts a great many businesses need: an organisation's "
             "structure, an accounting ledger, a calendar. It is essential to the system "
             "and is not what the project is for."),
            ("The four options",
             "Evans's ways of getting a generic subdomain: an off-the-shelf solution "
             "bought or taken from open source; a published design or model, adopted; an "
             "outsourced implementation; and an in-house implementation. A published model "
             "combines with either of the last two."),
            ("Weeks freed",
             "In the lab, the developer-weeks of the generic parts still built in house: "
             "the weeks a decision to buy or outsource each of them would take off the "
             "team's own list. A part marked `buy` or `outsource` no longer counts in the "
             "team's weeks. A published model still has to be built, in house or outside, "
             "so mark such a part `build` or `outsource`, whatever the tile's label says."),
        ],
        "read_title": "The pattern, its options, then the count",
        "read_intro": (
            "Read Generic Subdomains, its four options, the time-zone story and the two "
            "short sections after it in your own copy first. The lesson sets out the "
            "pattern as a tool, then counts what each option does to the team's weeks."
        ),
        "body": [
            ("p", "&ldquo;There is a part of your model that you would like to take for "
                  "granted.&rdquo; That is how Evans introduces Generic Subdomains, the next "
                  "pattern of Chapter 15. This lesson reads the pattern with its four "
                  "options, the story of two projects and their time zones, and two short "
                  "sections after it, Generic Doesn't Mean Reusable and Project Risk "
                  "Management. Read them in your own copy first."),
            ("p", "The problem is clutter. Some parts of a model add complexity without "
                  "carrying any special knowledge: principles everybody knows, or details "
                  "from specialties that support the project without being its focus. "
                  "However generic, they are needed for the system to work, and mixed in "
                  "with the core they make it harder to see. Evans's examples are an "
                  "organisation chart, which shipping, banking and manufacturing all need "
                  "in some form, and the receivables and expense ledgers a generic "
                  "accounting model could handle. He has watched two projects put their "
                  "best developers on dates and times with time zones for weeks."),
            ("p", "The pattern, as you would apply it: find the subdomains that support the "
                  "project without being its point, and give each a generic model in a "
                  "Module of its own that holds nothing peculiar to your business. Then "
                  "rank their work below the core's, keep the core's developers elsewhere, "
                  "because they would learn little of the business there, and check whether "
                  "a package or a published model would serve before you build."),
            ("p", "Then the four options, each with its costs. An off-the-shelf solution "
                  "means less code and maintenance carried by someone else, usually by "
                  "code more mature than yours; but it still has to be evaluated and "
                  "understood, its quality cannot be assumed, it may be overbuilt, it may "
                  "sit in a Bounded Context of its own and refer awkwardly to your Entities, "
                  "and it can bring platform dependencies. Evans finds such solutions worth "
                  "investigating and usually not worth the trouble, though he has seen "
                  "elaborate workflow engines and a deeply integrated error log succeed. A "
                  "published design or model is more mature than a home-grown one and comes "
                  "documented, though it may fit badly or be more than you need; where a "
                  "field has a rigorous formal model, as accounting and physics do, use it, "
                  "and implement only the consistent subset you need. Fowler's "
                  "<em>Analysis Patterns</em>, read in this Subject's sixth course, is the "
                  "kind of source he means."),
            ("p", "An outsourced implementation keeps the core team on the core and adds "
                  "capacity without spreading knowledge of the core thin, and handing the "
                  "work outside forces an interface-oriented, generic design. It still costs "
                  "the core team time to explain the interface and the standards, bringing "
                  "the code back in has an overhead, and its quality may be better or worse "
                  "than your own; Evans recommends requiring unit tests and, better, "
                  "specifying the acceptance tests yourself. An in-house implementation "
                  "integrates easily, does exactly what you want, and can be given to "
                  "temporary contractors; its costs are maintenance, training and a time "
                  "estimate that is easy to get wrong. Generic subdomains, he adds, are the "
                  "right place for outside design expertise and the place where "
                  "confidentiality matters least."),
            ("p", "The time-zone story is two projects that spent their best developers' "
                  "weeks on time zones. On a shipping scheduler the need was proven and the "
                  "core was mature, no adequate package existed, and the work went to a "
                  "strong programmer on a short contract, who adapted a public-domain "
                  "implementation. On an insurance claims system a long-term junior "
                  "developer, later joined by a senior one, built a fully general time-zone "
                  "model before any requirement was known, and the core went undeveloped. "
                  "Both did one thing right: they kept the time-zone model out of the "
                  "core."),
            ("p", "Generic Doesn't Mean Reusable corrects a natural reading. Evans has said "
                  "generic, not reusable, on purpose: if you build the subdomain yourself, "
                  "do not design that code for reuse, because the point of distillation is "
                  "to put as much effort as you can into the core and only what is needed "
                  "into the rest. Model reuse, through a published model, is often the "
                  "better kind. Implement only the part you need, but stay strictly inside "
                  "the generic concept: anything specific to your industry makes the "
                  "subdomain harder to extend, and belongs in the core or in a specialised "
                  "subdomain of its own, which is worth more than the generic one. Project "
                  "Risk Management then asks what an early end-to-end system should be "
                  "made of. Building it on a generic part is tempting because such parts "
                  "are easy to analyse, but unless the team's skills are proven and "
                  "the domain well known, the first cut should rest on part of the core, "
                  "even a small one, since that is where the risk is."),
            ("p", "Now the count, on the bike-share of the last lesson. The preset "
                  "<code>all-built</code> is the drifted team with an option written on "
                  "each generic part, all of them `build`: 100 weeks, 24 on the core and 48 "
                  "on generic parts, four generic parts built in house, and 48 weeks a "
                  "decision to buy or outsource could free. The preset "
                  "<code>buy-and-outsource</code> buys payments and map tiles, outsources "
                  "login, and keeps messaging in house. Buying is not free, so it adds two "
                  "supporting parts, `payments_fit` and `map_fit`, for the 3 and 1 weeks of "
                  "evaluating and integrating the packages. The team's own weeks fall to 64, "
                  "of which 24 are core, three eighths; the 8 weeks of messaging are the "
                  "only generic weeks left, and the only ones still to free."),
            ("p", "That preset also shows what buying does not do. The strongest developers "
                  "are on the two integrations and on messaging: still 0 of 3 on the core, "
                  "because no decision about people was made. The preset "
                  "<code>freed-to-core</code> makes it: the 36 weeks the purchases saved go "
                  "to rebalancing and the forecast, and so do the three strongest "
                  "developers, so the core holds 60 of the team's 100 weeks and 3 of 3 of "
                  "the strongest. Which option suits a part is Evans's list of advantages "
                  "and drawbacks weighed against your own case; the lab counts only the "
                  "weeks each choice takes off the team's list."),
            ("h3", "Exercise"),
            ("ul", [
                "The clinic from the last lesson: triage-scheduling, core, 10 weeks; "
                "patient-records, supporting, 14; billing, generic, 15; login, generic, 6; "
                "reminders, generic, 5.",
                "The team buys billing, adding a supporting part billing-fit of 1 week; "
                "outsources login; and builds reminders.",
            ]),
            ("p", "By hand, find the team's own weeks after these decisions, the share of "
                  "them on the core, the generic parts still built in house, and the weeks "
                  "a further decision could free. Then type the parts, with an option on "
                  "each generic one, into the lab."),
            ("p", "A generic subdomain leaves the core in plainer view, but only for those "
                  "who already know what it is. The next lesson, Domain Vision Statement "
                  "and Highlighted Core, reads two cheap ways of telling everyone."),
        ],
        "lab": ("dddkit", {
            "mode": "distill",
            "view": "effort",
            "preset": "all-built",
            "presets": [
                {"id": "all-built",
                 "label": "The drifted bike-share, every generic part built in house",
                 "parts": BIKES_ALL_BUILT,
                 "expect": {"ddsWeeks": "100", "ddsCore": "6/25 = 24%", "ddsGeneric": "12/25 = 48%",
                            "ddsBuilt": "4: payments, login, map-tiles, messaging", "ddsFree": "48"}},
                {"id": "buy-and-outsource",
                 "label": "Payments and map tiles bought, login outsourced",
                 "parts": BIKES_BOUGHT,
                 "expect": {"ddsWeeks": "64", "ddsCore": "3/8 = 37.5%", "ddsGeneric": "1/8 = 12.5%",
                            "ddsStrong": "0 of 3, 0 = 0%", "ddsBuilt": "1: messaging", "ddsFree": "8"}},
                {"id": "freed-to-core",
                 "label": "The weeks saved and the strongest developers moved to the core",
                 "parts": BIKES_FREED_TO_CORE,
                 "expect": {"ddsWeeks": "100", "ddsCore": "3/5 = 60%", "ddsStrong": "3 of 3, 1 = 100%",
                            "ddsFree": "8"}},
            ],
            "panel_title": "The weeks a decision about a generic part frees",
            "panel_intro": _EFFORT_INTRO,
        }),
        "steps_title": "Deciding how to get a generic part",
        "steps_intro": "Four steps, the last of them on a project of your own.",
        "steps": [
            ("Check that it is generic",
             "Say which other kinds of business would need the part in much the same "
             "form; if the answer is none, it is supporting or core, not generic."),
            ("Strip out your specialty",
             "List anything in the part that only your industry would recognise, and "
             "move it to the core or to a specialised subdomain."),
            ("Weigh the four options",
             "For each of buying, adopting a published model, outsourcing and building, "
             "write the one advantage and the one drawback Evans names that matter most "
             "for this part, and choose."),
            ("Do it on your own project",
             "Take the generic parts of a system you know, write an option on each in the "
             "lab, add a supporting part for any integration a purchase needs, and write "
             "down the weeks the decisions free and where those weeks and people go."),
        ],
        "worked": {
            "title": "Buying payments and map tiles",
            "intro": [
                "Find the team's weeks in <code>buy-and-outsource</code>.",
            ],
            "lines": [
                "not counted: payments 18, login 10, maps 12",
                "core: 16 + 8, so 24",
                "supporting: 3 + 1 + 14 + 14, so 32",
                "generic still built: messaging 8",
                "the team: 24 + 32 + 8, so 64 weeks",
                "core share 24 of 64, three eighths",
            ],
            "after": [
                "The purchases took 40 weeks off the list and the integrations put 4 back. "
                "The core's share rose only because the total fell; its own weeks did not "
                "move until a separate decision moved them.",
            ],
        },
        "quiz_title": "Generic subdomains and their options",
        "quiz": [
            {"q": "Which of these does Evans give as a drawback of an outsourced "
                  "implementation of a generic subdomain?",
             "a": ["It forces an interface-oriented design",
                   "It requires no time from the core team",
                   "Transferring ownership back inside has a significant overhead, because "
                   "the code has to be understood",
                   "It keeps the subdomain generic, because the specification is passed "
                   "outside"],
             "c": 2,
             "why": "The cost of bringing the code back in is one of the drawbacks he lists, "
                    "with the core team's time and the varying quality. Forcing an "
                    "interface-oriented design and keeping the subdomain generic are "
                    "advantages, and he says it still requires the core team's time."},
            {"q": "In the exercise, what are the team's own weeks, the core's share, and the "
                  "weeks a further decision could free?",
             "a": ["50 weeks; a fifth; 26 weeks",
                   "30 weeks; a third; 5 weeks",
                   "29 weeks; 10 of 29; 5 weeks",
                   "30 weeks; a third; 0 weeks"],
             "c": 1,
             "why": "Billing's 15 and login's 6 leave the team's list; billing-fit's 1 joins "
                    "it. The team's weeks are 10 + 14 + 1 + 5 = 30, a third of them on "
                    "triage scheduling. Reminders is the one generic part still built in "
                    "house, so its 5 weeks are what a further decision could free. 50 is the "
                    "total before the decisions; 29 forgets billing-fit; 0 forgets that "
                    "reminders is still built."},
            {"q": "Generic Doesn't Mean Reusable: you are building a generic subdomain in "
                  "house. What does Evans advise about the reusability of its code?",
             "a": ["Design it for reuse, since other projects will need it",
                   "Do not concern yourself with it; build only the part you need, but keep "
                   "strictly within the generic concept",
                   "Make it reusable only if it is outsourced",
                   "Put the industry-specific parts in it, so that it is complete"],
             "c": 1,
             "why": "Designing for reuse would spend effort the core should have. He still "
                    "insists on keeping out industry-specific elements, which belong in the "
                    "core or a specialised subdomain and would make the generic one hard to "
                    "extend."},
            {"q": "According to Project Risk Management, what should a first end-to-end "
                  "system be built on, unless the team's skills are proven and the domain "
                  "well known?",
             "a": ["A generic subdomain, since it is easiest to analyse",
                   "The technical architecture alone, with no domain logic",
                   "The part with the most users",
                   "A part of the core domain, even a small one"],
             "c": 3,
             "why": "An end-to-end system reduces risk only as far as it is an early version "
                    "of the hard parts, and the core is risky because it often turns "
                    "out harder than expected and the project fails without it. A generic part "
                    "is the tempting choice the section warns against."},
        ],
        "mistakes": [
            ("Taking generic to mean designed for reuse",
             "Evans chose the word generic and not reusable deliberately. Code built in "
             "house for a generic subdomain should do only what this business needs, "
             "because effort spent generalising it is effort the core does not get. The "
             "reuse he values more is of models, as when a team adopts a published one. "
             "What he does insist on is purity: nothing industry-specific in the generic "
             "module."),
            ("Giving the generic part to the strongest developers because it is hard and "
             "well defined",
             "Evans's two time-zone projects both spent strong developers on a generic "
             "problem. The one that did it well had proven the need, had a mature core and "
             "used a strong programmer on a short contract; the other used long-term "
             "developers who should have been learning insurance, before any requirement "
             "was known. On the lesson's illustration, buying parts frees weeks but leaves "
             "the strongest developers at 0 of 3 on the core until people are moved too."),
            ("Starting a project with the generic parts to reduce risk",
             "Project Risk Management says the opposite: unless the team has proven skills "
             "and knows the domain well, the first-cut system should be built on part of "
             "the core, because that is where the unforeseen complexity and the missing "
             "knowledge are. A generic part is easier to analyse, which is why it tempts."),
        ],
        "standard": (
            "Finish when you can choose how to get a generic part and say what it frees.",
            "Given a project's parts, state which are generic, give one advantage and one "
            "drawback of each of the four options, and count the team's weeks and the "
            "weeks still to free after a set of decisions."
        ),
        "note": (
            "The lab takes bought and outsourced parts off the team's weeks and counts "
            "only the integration you add back. It knows nothing of a package's quality, "
            "its fit or its licence, which are most of Evans's list of drawbacks, and it "
            "cannot say whether a part is generic: that is the team's reading of its domain."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Domain Vision Statement (PDF pp. 257-258 of the operator's copy);
    # Highlighted Core (p. 258); The Distillation Document (p. 259); The Flagged
    # Core (pp. 259-260); The Distillation Document as Process Tool (p. 260).
    # Quote: PDF p. 258 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "domain-vision-statement-and-highlighted-core",
        "title": "Domain Vision Statement and Highlighted Core",
        "module": "Chapter 15 · Distillation",
        "one_line": "A page that says what the core is for, and a mark on the model that shows which elements are in it, both cheap and neither changing the code.",
        "summary": (
            "Two distillations that change only documents: a short Domain Vision Statement "
            "of the core's value, and a Highlighted Core, as a distillation document or as "
            "flags in the model itself. Read why Evans thinks both are worth their small "
            "cost, what each must leave out, and how the distillation document tells a "
            "team which changes need consulting on; then count the share of a model a "
            "newcomer must read."
        ),
        "key": [
            "one narrow page on what the core is worth",
            "about the model, not the screens or servers",
            "show everyone which elements are core",
            "a distillation document: a few sparse pages",
            "or flag the core where the model lives",
            "a change to the document means: consult",
        ],
        "key_label": "The two patterns in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's patterns, the "
            "third the lab's count."
        ),
        "concepts": [
            ("Domain Vision Statement",
             "About a page describing the Core Domain and what it is worth to the "
             "business. It leaves out whatever does not distinguish this model from others, "
             "shows how the model balances the interests it serves, and is revised as the "
             "team learns."),
            ("Highlighted Core",
             "Any means of making it effortless to see which model elements are in the "
             "core. Evans gives two: a distillation document of a few sparse pages on the "
             "core's elements and their main interactions, and a flagged core, marks on "
             "the elements themselves wherever the model is kept."),
            ("The newcomer's share",
             "In the lab, the classes flagged core against all the classes of the model, "
             "and the weeks spent on them against all the weeks: how much of the model a "
             "new member must read to know what the system is for."),
        ],
        "read_title": "Two light patterns, then the count",
        "read_intro": (
            "Read Domain Vision Statement, Highlighted Core and the three sections after "
            "it in your own copy first. The lesson sets out both patterns as tools, then "
            "counts what flagging the core narrowly or broadly asks of a newcomer."
        ),
        "body": [
            ("p", "&ldquo;The mental labor of constantly filtering the model to identify the "
                  "key parts absorbs concentration better spent on design thinking&rdquo;, "
                  "Evans writes in Highlighted Core, and it requires knowing the whole model. "
                  "Most of Chapter 15's techniques change the model and the code; this "
                  "lesson reads the two that change only a document, Domain Vision "
                  "Statement and Highlighted Core, with The Distillation Document, The "
                  "Flagged Core and The Distillation Document as Process Tool. Read them in "
                  "your own copy first."),
            ("p", "Domain Vision Statement answers two needs that arrive before any deep "
                  "model does. At the start of a project there is no model yet, but its "
                  "development already needs a direction; later, people need the value of "
                  "the system explained without studying the model; and the critical "
                  "concepts may span several Bounded Contexts, which no single model can "
                  "show together. Many teams write a vision document for management, Evans "
                  "notes, and it is usually forgotten once the funding arrives. His version "
                  "keeps that form but is about the domain model and the value it brings, "
                  "and it is meant to be used throughout by managers and developers alike."),
            ("p", "So the pattern: about a page on the core and its worth to the business, "
                  "leaving out whatever any similar model would also say, showing how "
                  "competing interests are weighed, narrow in scope, drafted at the start "
                  "and rewritten as understanding grows. The book sets two sample statements beside lists of things "
                  "that are important but do not belong in one. For a bike-share, a "
                  "sentence that does belong would say that the model forecasts each "
                  "station's demand by hour and plans the fewest van moves that keep bikes "
                  "where riders will want them. One that does not, however true, would say "
                  "that the app must load in under two seconds, or that riders sign in with "
                  "a phone number. Those are requirements, not the model's value."),
            ("p", "A vision statement names the core in broad terms and leaves each reader to "
                  "decide which elements it means, and different people, or one person on "
                  "different days, will not pick the same ones. Highlighted Core is the "
                  "remedy. Restructuring the code is the ideal way to show the core, Evans "
                  "says, but it is not always possible in the short term, and it is hard to do "
                  "without exactly the shared view the team lacks. Marking the core says "
                  "something about the model without having to belong to it, and any technique that lets "
                  "everyone see it will do."),
            ("p", "The first technique is the distillation document: a short document, a "
                  "handful of pages (Evans says three to seven, sparse), on the core and how "
                  "its elements work together. It can be a list of the essential objects, diagrams "
                  "of them, a walk through their interactions, or prose, and it is an entry "
                  "point that sends the reader to the code, not a complete design document. "
                  "It carries the usual risks of a separate document: it may go stale, go "
                  "unread, or add one more source of information to a complex picture. "
                  "Being minimalist limits all three, because the central abstractions "
                  "change more slowly than the detail. Write it for the nontechnical "
                  "members of the team too."),
            ("p", "The second is the flagged core. Evans's story: given a two-hundred-page "
                  "industry model on his first day with an insurer, and with management "
                  "unwilling to see it cut, he worked through it with a business analyst, "
                  "marked the few sections that held the essential concepts, and gave the "
                  "team a way through the model that showed the core and what supported it. "
                  "A new prototype built from that view soon showed some of what was required. The technique does not "
                  "depend on paper: a stereotype on a diagram, a structured comment in the "
                  "code or a tool in the development environment will do, provided a "
                  "developer can tell at a glance whether an element is core."),
            ("p", "The Distillation Document as Process Tool turns the document into a rule "
                  "for coordination. On a team where any pair may change any code, some "
                  "changes still need consultation, and in the domain layer it is not "
                  "always obvious which. If a change would force the distillation document "
                  "to change, it alters the core's elements, their relationships or the "
                  "core's boundary: consult first, then tell the whole team and send round "
                  "the new document. A change outside the core, or below the document's "
                  "level of detail, can be made without either."),
            ("p", "Now the count, on the bike-share model's twelve classes, each with the "
                  "weeks spent on it so far. The preset <code>flagged-narrowly</code> flags "
                  "the three classes the vision statement's sentence is about: "
                  "`DemandForecast`, `RebalancingPlan` and `Move`. A newcomer reads 3 of the "
                  "12 classes first, a quarter of the model; they carry 14 of the 40 weeks "
                  "spent, and two of the three strongest developers work on them. The lab "
                  "prints the weeks; the classes you count from its table."),
            ("p", "The preset <code>flagged-broadly</code> is the same model with every "
                  "class to do with stations and vans flagged too: `Station`, `Dock`, `Bike` "
                  "and `VanRun`. Now the core is 7 of the 12 classes and 27 of the 40 "
                  "weeks, more than half the model, and the flag tells a newcomer little "
                  "that the class list did not. On the lesson's illustration, a broad flag "
                  "costs the reading it was meant to save. Whether a station belongs in the "
                  "core is the team's call; Evans's advice in the chapter is to keep the "
                  "core small."),
            ("h3", "Exercise"),
            ("ul", [
                "The clinic's model, with the core flagged in its distillation document: "
                "`UrgencyScore`, `TriageRule` and `Booking`. Its other classes are "
                "`Patient`, `Clinician`, `Slot`, `Room`, `Invoice` and `Reminder`.",
                "Five proposed changes and the classes each touches: (a) reminders by text "
                "message, `Reminder`; (b) a new triage rule for chest pain, `TriageRule`; "
                "(c) invoices in two currencies, `Invoice`; (d) a booking may now hold two "
                "clinicians, `Booking` and `Clinician`; (e) rooms get a cleaning flag, "
                "`Room`. Changes (b) and (d) each alter what the distillation document says "
                "about the core's elements or their relationships; the others do not.",
            ]),
            ("p", "By hand, find the share of the model's classes a newcomer reads first, "
                  "and which of the five changes call for consultation under the process "
                  "rule. Then type the classes into the lab with the core flagged and 1 week "
                  "each, so that the share on the core counts classes."),
            ("p", "Both patterns guide the team without changing the code. The next lesson, "
                  "Cohesive Mechanisms, begins the techniques that change the code itself, "
                  "with a computation that has swamped the model around it."),
        ],
        "lab": ("dddkit", {
            "mode": "distill",
            "view": "effort",
            "preset": "flagged-narrowly",
            "presets": [
                {"id": "flagged-narrowly",
                 "label": "The bike-share's classes, three flagged core",
                 "parts": CLASSES_NARROW,
                 "expect": {"ddsWeeks": "40", "ddsCore": "7/20 = 35%", "ddsStrong": "2 of 3, 2/3 ≈ 66.7%"}},
                {"id": "flagged-broadly",
                 "label": "The same classes, seven flagged core",
                 "parts": CLASSES_BROAD,
                 "expect": {"ddsWeeks": "40", "ddsCore": "27/40 = 67.5%", "ddsStrong": "3 of 3, 1 = 100%"}},
            ],
            "panel_title": "The share of a model flagged core",
            "panel_intro": (
                "A count over the small model the lesson states. Each record is one class "
                "of the model, flagged core, supporting or generic, with the "
                "developer-weeks spent on it and the strongest developers who work on it. "
                "The lab adds them by flag; which classes deserve the core flag is the "
                "team's judgement, which the book weighs. The last two tiles count generic "
                "classes and mean nothing here."
            ),
        }),
        "steps_title": "Making the core visible",
        "steps_intro": "Four steps, the last of them on a model of your own.",
        "steps": [
            ("Write the vision statement",
             "Write a few sentences on what the model does that others do not, and "
             "strike any sentence about screens, servers, response times or sign-in."),
            ("Flag the elements it names",
             "Mark as core only the classes the statement's sentences are about, and "
             "count them against all the classes."),
            ("Write the rule for consulting",
             "List the core's elements and their main interactions on one page, and "
             "agree that a change which would alter that page is discussed first."),
            ("Do it on your own model",
             "Flag the core classes of a system you know, type them into the lab, and "
             "write down the share of classes and of weeks a newcomer would read first."),
        ],
        "worked": {
            "title": "Flagging the bike-share narrowly",
            "intro": [
                "Find the newcomer's share in <code>flagged-narrowly</code>.",
            ],
            "lines": [
                "core classes: forecast, plan, move: 3",
                "all classes: 12, so 3 of 12, a quarter",
                "core weeks: 6 + 6 + 2, so 14",
                "all weeks: 14 + 21 + 5, so 40",
                "core share of weeks: 14 of 40",
                "strongest on core: 2 of 3",
            ],
            "after": [
                "The supporting classes take 4 + 3 + 2 + 4 + 4 + 2 + 2 = 21 weeks and the "
                "two generic ones 5. The three flagged classes are the ones the vision "
                "statement's sentence names; the flag only makes that reading the same for "
                "everyone.",
            ],
        },
        "quiz_title": "Vision statements, flags and the process rule",
        "quiz": [
            {"q": "In the exercise, what share of the clinic's classes does a newcomer read "
                  "first, and which changes call for consultation?",
             "a": ["3 of 9, a third; changes (b) and (d)",
                   "3 of 9, a third; change (b) only",
                   "3 of 6, a half; changes (b) and (d)",
                   "3 of 9, a third; every change, since all touch the model"],
             "c": 0,
             "why": "Three flagged classes of nine in all is a third; 3 of 6 compares the "
                    "core with the rest instead of the whole. Change (b) touches "
                    "`TriageRule` and (d) touches `Booking`, both flagged, and both alter "
                    "what the distillation document says, so each needs consulting on; (d) "
                    "also touches `Clinician`, which does not make it any less a core "
                    "change. Changes (a), (c) and (e) touch only unflagged classes, leave the "
                    "document as it is, and can be made without consultation."},
            {"q": "A Domain Vision Statement describes the core domain and its value and leaves "
                  "out what does not set the model apart. Which of these belongs in one for "
                  "the bike-share?",
             "a": ["The app must load in under two seconds",
                   "Riders sign in with a phone number",
                   "The model forecasts each station's hourly demand and plans the fewest "
                   "van moves that keep bikes where riders will want them",
                   "The system runs on two servers in separate data centres"],
             "c": 2,
             "why": "The statement is about the core domain and the value it brings, and "
                    "leaves out what does not set this model apart. The other three are real "
                    "requirements of the kind the book's samples list as important but not "
                    "part of a vision statement: speed, sign-in and hosting."},
            {"q": "How long does Evans say a distillation document should be?",
             "a": ["About one page, like the vision statement",
                   "Three to seven sparse pages",
                   "As long as needed to describe the whole design",
                   "One page for each core class"],
             "c": 1,
             "why": "The Distillation Document asks for a very brief document of three to "
                    "seven sparse pages on the core and its main interactions: an entry "
                    "point, not a complete design document. About one page is the length of "
                    "the Domain Vision Statement."},
            {"q": "In <code>flagged-broadly</code>, the team unflags `Bike` and `Dock` "
                  "again and changes nothing else. What share of the classes and of the "
                  "weeks is now core?",
             "a": ["5 of 12 classes and 22 of 40 weeks",
                   "7 of 12 classes and 27 of 40 weeks",
                   "5 of 12 classes and 27 of 40 weeks",
                   "5 of 10 classes and 22 of 35 weeks"],
             "c": 0,
             "why": "Removing two of the seven flags leaves 5 core classes out of the same 12. "
                    "`Dock` and `Bike` carried 3 and 2 weeks, so the core's 27 weeks become "
                    "22 of the unchanged 40. Unflagging a class moves it to supporting; it "
                    "does not leave the model, so the totals stay at 12 and 40."},
        ],
        "mistakes": [
            ("Writing the vision statement as a list of features and technology",
             "A vision document for management often lists screens, platforms and response "
             "times. Evans's Domain Vision Statement is modelled on such documents but is "
             "about the domain model and the value it brings to the business, and it "
             "leaves out whatever does not distinguish this model from others. The book's "
             "samples set requirements like those beside the statements as important "
             "but not part of them."),
            ("Expecting a distillation document to describe the whole design",
             "It is a minimalist entry point of three to seven sparse pages on the core's "
             "elements and their main interactions, which sends the reader to the code for "
             "detail. Evans names the usual risks of separate documents, going stale, going "
             "unread and adding to the complexity, and says the way to limit all three is to "
             "stay away from detail."),
            ("Thinking the core can only be shown by restructuring the code",
             "Restructuring is the ideal, Evans says, but not always practical at first, and "
             "hard without the shared view it is meant to provide. Highlighting is a "
             "reflection on the model, and any technique will do: his flagged core was a "
             "highlighter and page tabs on a purchased model. On the lesson's illustration "
             "a narrow flag puts a newcomer's first reading at 3 of 12 classes without one "
             "line of code moving."),
        ],
        "standard": (
            "Finish when you can make a model's core visible without changing its code.",
            "Given a project, write the sentences of its vision statement and strike those "
            "that do not belong, flag its core classes and state their share, and say which "
            "of a list of changes call for consultation."
        ),
        "note": (
            "The lab adds classes and weeks by the flags you set. It cannot read a vision "
            "statement, so it cannot tell whether the flags match it, and it cannot tell "
            "whether a document is being read; Evans's risks for separate documents are "
            "about people, not counts."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Cohesive Mechanisms (PDF pp. 261-262 of the operator's copy); A Mechanism in
    # an Organization Chart (pp. 261-262); Generic Subdomain Versus Cohesive
    # Mechanism (p. 262); When a Mechanism Is Part of the Core Domain
    # (pp. 262-263); Full Circle (p. 263).
    # Quote: PDF p. 261 of the operator's copy, 13 words, quotes.py OK.
    # Lesson total: 13 words.
    {
        "slug": "cohesive-mechanisms",
        "title": "Cohesive Mechanisms",
        "module": "Chapter 15 · Distillation",
        "one_line": "A computation complicated enough to swamp the model, moved into a small framework of its own behind an interface that says what it does.",
        "summary": (
            "When the methods that compute an answer bury the methods that state the "
            "problem, Evans separates the coherent part of the computation into a "
            "lightweight framework with an intention-revealing interface. Read the "
            "pattern, how it differs from a Generic Subdomain and when a mechanism belongs "
            "in the core, then count the modules a change to a school timetable's "
            "arithmetic and a change to its rules each touch."
        ),
        "key": [
            "the how has swamped the what",
            "first seek a model that makes it simple",
            "a coherent computation, not a calculator",
            "behind an interface that says what it does",
            "the model states; the mechanism solves",
            "in the core only if it is the value",
        ],
        "key_label": "Cohesive Mechanisms in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's pattern, the second "
            "Chapter 10's, the third the lab's."
        ),
        "concepts": [
            ("Cohesive Mechanism",
             "The coherent part of a computation, moved out of the model into a small "
             "framework of its own that the model reaches through operations named for "
             "what they answer, so that the domain's classes state the fact, rule or problem and "
             "the framework works out the answer."),
            ("Intention-Revealing Interface",
             "From Chapter 10: names of classes and operations that say what they do and "
             "what they are for, not how, so that a client can use them without reading "
             "their code. A mechanism is useful to the core only through such an interface."),
            ("Module touches",
             "In the lab, the number of different modules holding the elements a change "
             "touches, added over all the changes. A change confined to one module touches "
             "one."),
        ],
        "read_title": "The pattern and its limits, then the count",
        "read_intro": (
            "Read Cohesive Mechanisms and the sections after it, to the end of the second "
            "organisation-chart example, in your own copy first. The lesson sets out the "
            "pattern as a tool, then counts the modules two kinds of change reach."
        ),
        "body": [
            ("p", "&ldquo;This proliferation of procedures is a symptom of a problem in the "
                  "model.&rdquo; Evans means the methods that pile up when a computation "
                  "grows complicated enough to bloat a design, until the methods that work "
                  "out an answer hide the methods that say what the problem is. This lesson "
                  "reads Cohesive Mechanisms, its organisation-chart example, Generic "
                  "Subdomain Versus Cohesive Mechanism, When a Mechanism Is Part of the "
                  "Core Domain, and the example that brings the organisation chart full "
                  "circle. Read them in your own copy first."),
            ("p", "Encapsulating an algorithm behind a method with an intention-revealing "
                  "name is ordinary object design, and it separates what is computed from "
                  "how. The pattern starts where that runs out: a computation so large that "
                  "the how swamps the what. Evans's first remedy is not the pattern. It is "
                  "to refactor toward a deeper model in which the computation becomes "
                  "simple. Only sometimes does a part of the mechanism turn out to be "
                  "coherent in its own right, and he is careful to say that it will not "
                  "cover all the messy computation, and that he does not mean a catch-all "
                  "calculator. Extracting the coherent part should make what remains "
                  "easier to follow."),
            ("p", "The pattern, as you would apply it: give the coherent part of the "
                  "computation a small framework of its own, look first for a known "
                  "formalism or a textbook family of algorithms that already covers it, and "
                  "let the model reach it only through operations named for what they "
                  "answer. The domain classes then say what the problem is, and the "
                  "framework works out the answer, and the mechanism takes a supporting role, leaving the core "
                  "smaller and more declarative. Recognising a standard formalism brings a "
                  "studied set of concepts other developers know or can look up. Often you "
                  "must still build something new; keep it narrowly about the computation, "
                  "with the expressive model kept out."),
            ("p", "His example is an organisation chart whose questions, who in this chain "
                  "of command may approve this, who in this department can handle that, "
                  "turned out to be mostly about walking branches of a tree. A subcontractor "
                  "built a small graph-traversal framework, in standard graph vocabulary and "
                  "covering only the subset the project needed, and the organisation model "
                  "could then simply say that people are nodes and their relationships "
                  "edges. Evans names two costs of leaving the traversal inside the model: "
                  "it would have tied the model to one way of solving the problem, and, "
                  "worse, it would have muddied the model. A framework for building and "
                  "combining Specifications is another example he gives."),
            ("p", "Generic Subdomain Versus Cohesive Mechanism draws the line between two "
                  "patterns that both unburden the core. A generic subdomain is an "
                  "expressive model of part of the domain, only less central; a cohesive "
                  "mechanism represents no part of the domain, it solves a hard "
                  "computational problem that the expressive models pose. Evans admits the "
                  "line is often blurred at first unless the computation is a published "
                  "formalism, and that further refactoring may push it either way. When a "
                  "Mechanism Is Part of the Core Domain gives the exception: a proprietary "
                  "algorithm that is itself part of the software's value, like the "
                  "risk-rating algorithms on a project of his at an investment bank. Even then, "
                  "deeper analysis might make the rules explicit and leave a solver behind "
                  "them, a step he leaves to a cost-benefit judgement."),
            ("p", "Full Circle is Evans being fair to his own advice. A year later other "
                  "developers folded the graph framework back into the organisation's "
                  "Entities, judging the extra objects and package not worth it, while "
                  "keeping the declarative interface and the encapsulation. Such circles "
                  "are common, he says, and they do not return to where they started: the "
                  "result is usually a deeper model that keeps the virtues of the "
                  "intermediate stage."),
            ("p", "Now the code, on a domain written for the lesson: a school timetable. Its "
                  "rule is that two lessons clash if they share a teacher, a room or a "
                  "class of pupils and their times overlap. Below, the rule is stated in the "
                  "timetable's own terms, and the arithmetic of time intervals sits in a "
                  "small `intervals` package that knows nothing of schools. Interval "
                  "arithmetic is a documented formalism, the kind of thing the pattern "
                  "tells you to watch for."),
            ("code", _lines(CLASH_RULE)),
            ("p", "The lab places nine elements of the timetable in modules twice. In the "
                  "tangled packaging the interval helpers live where they were first "
                  "needed: `overlaps` in `timetable`, `merge` and `gaps` in `staff`, `span` "
                  "in `rooms`. In the separated packaging the four sit together in "
                  "`intervals`. The preset <code>four-changes</code> applies four changes. "
                  "Storing times in minutes instead of periods touches all four helpers: 3 "
                  "modules tangled, 1 separated. Letting periods that only meet not clash "
                  "touches `overlaps` alone, 1 module either way, and so does capping a "
                  "teacher at five periods a day, a rule change. A ten-minute cleaning gap "
                  "between laboratory lessons touches the room rule and `gaps`: 2 modules "
                  "either way."),
            ("p", "So, on the lesson's illustration, 7 module touches tangled and 5 "
                  "separated; 2 of the 4 changes confined to one module tangled, and 3 "
                  "separated. The largest change tangled is the move to minutes, at 3 "
                  "modules; separated it is the cleaning gap, at 2. The change to the arithmetic is the one the separation "
                  "confines. The rule changes stay where the rules are, and a rule that "
                  "needs a new capability of the mechanism reaches into it whichever way the "
                  "code is packaged. The count is narrower than Evans's claim, which is "
                  "about reading: in the separated design `clashes` says what a clash is, "
                  "and nobody has to read interval arithmetic to learn it."),
            ("h3", "Exercise"),
            ("ul", [
                "Two more changes to the timetable. (a) Teachers see their free periods "
                "only if a gap is at least 30 minutes: it touches `gaps` and "
                "`Teacher.canTake`. (b) Interval ends become inclusive instead of "
                "exclusive: it touches `overlaps`, `span` and `gaps`.",
            ]),
            ("p", "By hand, using the two packagings above, find the modules each change "
                  "touches tangled and separated, and the total module touches for the two "
                  "changes under each. Then replace the lab's changes with these two and check."),
            ("p", "A mechanism moves one kind of complexity out of the core. The next lesson, "
                  "Segregated Core, Abstract Core and Refactoring Targets, moves the core "
                  "itself."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "packagings": 2,
            "names": ["tangled", "separated"],
            "preset": "four-changes",
            "presets": [
                {"id": "four-changes",
                 "label": "Four changes, with the interval arithmetic tangled and separated",
                 "elements": TIMETABLE_ELEMENTS,
                 "changes": TIMETABLE_CHANGES,
                 "expect": {"dmoTotal": "7", "dmoTotal2": "5",
                            "dmoConfined": "2 of 4: touching-periods-ok, five-a-day",
                            "dmoConfined2": "3 of 4: minutes-not-periods, touching-periods-ok, five-a-day",
                            "dmoLargest": "minutes-not-periods, 3 modules",
                            "dmoLargest2": "cleaning-gap, 2 modules"}},
            ],
            "panel_title": "The modules a change to the arithmetic and to a rule touch",
            "panel_intro": _CHANGE_INTRO,
        }),
        "steps_title": "Separating a mechanism",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Find the swamped rule",
             "In a class whose purpose you cannot see at a glance, mark the methods that "
             "state a domain rule and the methods that only compute."),
            ("Look for a formalism",
             "Ask whether the computing methods are a known kind of computation, such as "
             "intervals, graphs, units or constraint solving, and name it."),
            ("Write the interface first",
             "Write the few operations the rule needs, named for what they answer, and "
             "rewrite the rule in terms of them before moving any code."),
            ("Do it on your own code",
             "Take a domain class of your own that holds a computation, list its elements "
             "and two packagings in the lab, add one change to the computation and one to a "
             "rule, and write down the modules each touches."),
        ],
        "worked": {
            "title": "Times in minutes, not periods",
            "intro": [
                "Find the modules the change reaches in <code>four-changes</code>.",
            ],
            "lines": [
                "it touches overlaps, merge, gaps, span",
                "tangled: timetable, staff, staff, rooms",
                "distinct modules tangled: 3",
                "separated: all four in intervals",
                "distinct modules separated: 1",
                "modules of the rules: not touched",
            ],
            "after": [
                "Each module is counted once however many of its elements a change touches, "
                "which is why `merge` and `gaps` in `staff` make one touch, not two.",
            ],
        },
        "quiz_title": "Mechanisms, subdomains and the count",
        "quiz": [
            {"q": "What is Evans's first remedy when a computation's methods swamp the "
                  "methods that express the problem?",
             "a": ["Move all the computing methods into a utility class",
                   "Refactor toward a model that makes the computation simple",
                   "Buy an off-the-shelf mechanism",
                   "Put the computation in a service of the application layer"],
             "c": 1,
             "why": "He reads the growing pile of procedures as a sign that the model is "
                    "wrong, and the first solution to seek is a deeper model in which the "
                    "mechanism is simple. Only when a coherent part of the computation "
                    "emerges does he separate it, and he rules out a catch-all calculator."},
            {"q": "In the exercise, how many module touches do the two changes make "
                  "tangled, and how many separated?",
             "a": ["3 tangled, 3 separated",
                   "5 tangled, 2 separated",
                   "4 tangled, 2 separated",
                   "4 tangled, 3 separated"],
             "c": 3,
             "why": "(a) touches `gaps` and `Teacher.canTake`, both in `staff` when tangled: "
                    "1 module; separated they are in `intervals` and `staff`: 2. (b) touches "
                    "`overlaps`, `span` and `gaps`, in `timetable`, `rooms` and `staff` "
                    "tangled: 3; all in `intervals` separated: 1. Totals 4 and 3. Counting "
                    "each element instead of each module gives 5 tangled; forgetting that "
                    "(a) reaches `staff` when separated gives 2."},
            {"q": "Generic Subdomain Versus Cohesive Mechanism: what is the difference "
                  "Evans draws?",
             "a": ["A generic subdomain is bought; a mechanism is built",
                   "A generic subdomain is an expressive model of part of the domain; a "
                   "mechanism represents no domain and solves a computational problem the "
                   "models pose",
                   "A mechanism is always part of the core; a generic subdomain never is",
                   "There is none; the two names are for the same pattern"],
             "c": 1,
             "why": "Both unburden the core, but a generic subdomain is a less central model "
                    "of the domain, while a mechanism solves what the models state. Either "
                    "can be bought or built, and a mechanism is part of the core only in "
                    "the exception he names."},
            {"q": "When does Evans count a mechanism as part of the Core Domain?",
             "a": ["When it is the most complex code in the system",
                   "When it uses a published formalism",
                   "When the core calls it more than any other module does",
                   "When the mechanism is proprietary and is itself a large part of "
                   "what the software is worth"],
             "c": 3,
             "why": "You almost always want mechanisms out of the core; the exception is a "
                    "proprietary, highly specialised algorithm that is part of what the "
                    "software is worth, such as a particularly effective scheduling "
                    "algorithm or the risk-rating algorithms he mentions. A published "
                    "formalism points elsewhere, towards a supporting framework."},
        ],
        "mistakes": [
            ("Treating a cohesive mechanism as a home for every computation",
             "Evans says plainly that he does not mean a catch-all calculator, and that the "
             "coherent part will not cover all the messy computation. A utility class full "
             "of unrelated helpers is not a mechanism. His first remedy is a deeper model "
             "that makes the computation simple; a mechanism is what to do when some part of "
             "the computation proves coherent in its own right. On the lesson's illustration only the four interval "
             "helpers move, and the rules stay where they were."),
            ("Confusing a cohesive mechanism with a generic subdomain",
             "Both take weight off the core, but a generic subdomain is a model of part of "
             "the domain, like an organisation's structure, while a mechanism models no "
             "domain at all and works out what the models pose, like graph traversal. Evans "
             "grants the line is often unclear at first and that refactoring may push a "
             "part either way."),
            ("Assuming a mechanism must always be kept out of the core, and stay separated "
             "for good",
             "A proprietary algorithm that is part of the software's value belongs in the "
             "core, Evans says. And his Full Circle example shows a separated framework "
             "folded back into the Entities a year later, with its declarative interface "
             "and encapsulation kept; he calls such circles common and usually a step to a "
             "deeper model."),
        ],
        "standard": (
            "Finish when you can separate a mechanism and say what the separation changes.",
            "Given a domain class holding a computation, write the interface a mechanism "
            "would offer, and count the modules a change to the computation and a change "
            "to a rule each touch, tangled and separated."
        ),
        "note": (
            "The lab counts modules touched. Evans's case for a mechanism is mostly about "
            "how the model reads, which no count of modules shows; and the lab cannot tell "
            "whether a computation is coherent enough to separate, which he leaves to the "
            "modeller's insight."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Distilling to a Declarative Style (PDF p. 263 of the operator's copy);
    # Segregated Core (pp. 264-265); The Costs of Creating a Segregated Core
    # (pp. 264-265); Evolving Team Decision (p. 265); the cargo example
    # (pp. 265-269); Abstract Core (pp. 270-271); Deep Models Distill (p. 271);
    # Choosing Refactoring Targets (p. 271).
    # Quotes: PDF p. 264 of the operator's copy, 15 words, quotes.py OK; PDF
    # p. 270, 6 words, quotes.py OK. Lesson total: 21 words.
    {
        "slug": "segregated-and-abstract-core",
        "title": "Segregated Core, Abstract Core and Refactoring Targets",
        "module": "Chapter 15 · Distillation",
        "one_line": "The core's classes pulled into a module of their own, then its fundamental concepts made abstract so the other modules depend on it and not on each other.",
        "summary": (
            "The last and heaviest distillations: refactor the core's classes out of the "
            "mass of supporting code into their own module, and, further, factor the "
            "core's fundamental concepts into abstract types that carry most of the "
            "interaction between modules. Read Evans's steps, the costs he names, and "
            "where he would start refactoring a tangled system; then count the "
            "dependencies across the core's boundary in a model packaged three ways."
        ),
        "key": [
            "pull the core into its own module",
            "leave the rest where it is, for now",
            "it can break a module that was cohesive",
            "the whole team moves to it together",
            "abstract types carry the interactions",
            "refactor the core first",
        ],
        "key_label": "The two cores in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's patterns, the "
            "third the lab's count."
        ),
        "concepts": [
            ("Segregated Core",
             "The model refactored so that the core's concepts sit in a module of their "
             "own, with the cohesion inside it strengthened and its coupling to other code "
             "reduced, even where that means separating elements that were tightly "
             "coupled."),
            ("Abstract Core",
             "The model's deepest concepts made into abstract types through which most of "
             "the traffic between the main parts flows, kept in a module of their own, "
             "with the detailed classes left in modules by subdomain, depending on it "
             "rather than on each other."),
            ("Dependencies across the core's boundary",
             "In the lab, read from its list of dependencies: those with one end in the "
             "core's module and the other outside it, in either direction: in the lab's "
             "table, the core module's row, out to others plus in from others. The lab itself "
             "counts dependencies inside and across all modules, and the cycles between "
             "modules."),
        ],
        "read_title": "Two patterns and a strategy, then the count",
        "read_intro": (
            "Read Chapter 15 from Distilling to a Declarative Style to the end in your own "
            "copy first. The lesson sets out both patterns as tools, Evans's costs and his "
            "advice on where to start, then counts one model packaged three ways."
        ),
        "body": [
            ("p", "&ldquo;What is done with the undifferentiated mass left behind is "
                  "important, but not as important.&rdquo; Evans says it of the code left "
                  "over when the core is pulled out of a model, and it sets the priority of "
                  "Segregated Core. This lesson reads the end of Chapter 15: Distilling to a "
                  "Declarative Style, Segregated Core with its costs and the team decision "
                  "it needs, Abstract Core, Deep Models Distill and Choosing Refactoring "
                  "Targets. Read them in your own copy first."),
            ("p", "Distilling to a Declarative Style links this chapter to Chapter 10. The "
                  "value of distillation is seeing what you are doing, and parts of the "
                  "core can be written declaratively when the supporting design gives them a "
                  "small language for stating the core's concepts and rules while hiding how "
                  "they are computed or enforced. Mechanisms with intention-revealing "
                  "interfaces, assertions and side-effect-free functions let the core make "
                  "meaningful statements; the larger payoff comes when the core itself "
                  "becomes such a language. Even then, Evans says, not everything outside "
                  "the core will find a good home, which is where the next pattern begins."),
            ("p", "Segregated Core starts from entanglement: elements that serve the core "
                  "partly and support it partly, core elements tightly coupled to generic "
                  "ones, a core whose cohesion is weak or invisible. Factoring out generic "
                  "subdomains clears some of this, but it is hard work and leaves the core "
                  "tangled in the residue. So work from the other direction: pull the core's "
                  "concepts away from everything that only helps them, vague helpers "
                  "included, so that the core hangs together more tightly and leans less on "
                  "the rest, and push what is generic or supporting into other classes and "
                  "packages, even when that pulls apart classes that were closely tied. The residue can stay roughly where it was, or go into packages "
                  "named for its prominent classes, and be sorted out later."),
            ("p", "Evans gives the steps as roughly these. Identify a core subdomain, "
                  "perhaps from the distillation document; collect its classes in a new "
                  "module whose name says what unites them; cut out the data and "
                  "behaviour that do not express that concept and put them in other "
                  "packages, without agonising over where, while making the references from "
                  "the core outward explicit; simplify the new module's relationships with "
                  "the others, an objective that never quite ends; and repeat with the next "
                  "core subdomain."),
            ("p", "He is plain about the costs. Segregation can leave the links with "
                  "closely coupled non-core classes murkier, and it can break up a "
                  "module that was nicely cohesive in another way; he counts both as worth "
                  "paying for a clearer core. It is also a lot of work that can pull "
                  "developers into changes all over the system, so the time for it is when a "
                  "large, critical Bounded Context has its essential model hidden under "
                  "supporting capability. And the whole team must move together, under one "
                  "definition of the core that is not frozen, with insights shared and acted "
                  "on jointly rather than by one pair alone. The book's worked example "
                  "segregates the core of a cargo-shipping model and shows the small model "
                  "changes that segregation tends to surface."),
            ("p", "Abstract Core addresses what segregation can leave. Breaking a model into "
                  "modules by subdomain is the usual way to make it manageable, but where the "
                  "subdomains interact heavily, either many references cross the modules or "
                  "the interaction is made indirect and obscure. &ldquo;Consider slicing "
                  "horizontally rather than vertically.&rdquo; If most of the interaction "
                  "can be expressed through polymorphic interfaces, and those interfaces are "
                  "fundamental concepts of the domain rather than a technical trick, factor "
                  "them into a core module of their own; the specialised modules then "
                  "reference that core and not each other. Evans warns that this is not "
                  "mechanical: moving every frequently referenced class into one module "
                  "makes a meaningless mess, and the real thing needs deep understanding and "
                  "usually considerable redesign. Deep Models Distill adds that distillation "
                  "also means refining the core itself toward a deep model and supple "
                  "design, where a breakthrough can change a whole project."),
            ("p", "Choosing Refactoring Targets closes the chapter. Evans rejects the two "
                  "answers the XP community tends to give to where a tangled system's refactoring should start: "
                  "anywhere, since it all needs doing, which works only for teams of top "
                  "programmers; and wherever it hurts, which treats symptoms and avoids the "
                  "worst tangles. His alternative: when pain drives the work, check whether "
                  "its root is in the core or in the core's relationship to a supporting "
                  "element, and if it is, fix that first; when you are free to choose, "
                  "improve the factoring of the core and its segregation, and purify "
                  "supporting subdomains until they are generic."),
            ("p", "Now the count, on the bike-share model's twelve classes and eighteen "
                  "dependencies. The preset <code>mixed-and-segregated</code> packages them "
                  "twice. As history left them, in `stations`, `fleet`, `ops` and `riders`, "
                  "9 dependencies fall inside a module and 9 across, and `stations`, "
                  "`fleet` and `riders` lie on one cycle of module dependencies. "
                  "Segregated, with `DemandForecast`, `RebalancingPlan` and `Move` in a "
                  "`rebalancing` module, 8 fall inside and 10 across. Seven of the 18 cross "
                  "the core's boundary, and the cycles now pass through the core: "
                  "`Station` still depends on `DemandForecast`, which depends on `Station`. "
                  "The share inside went down, from a half to four ninths, which is the "
                  "cost Evans names: the forecast had been comfortable in `stations`. The "
                  "lab's most coupled pair says the same: before, `fleet` and `ops` with 3 "
                  "dependencies between them; after, `fleet` and `rebalancing` tie with "
                  "`rebalancing` and `stations` at 3, both pairs now through the core."),
            ("p", "What segregation did is put the core's own relationships in one place, so "
                  "that the seven references crossing its boundary are explicit and can be "
                  "worked on, which is his fourth step. The preset <code>abstract-core</code> "
                  "is that work done, and it is a redesign, not a repackaging: two "
                  "interfaces, `Place` and `DemandSource`, shown below, carry the core's "
                  "interactions; `Station` implements one and `Trip` the other; the plan no "
                  "longer reads repair tickets, and a move carries a number of bikes between "
                  "places. The preset packages the new model twice, to show what Evans means "
                  "by slicing horizontally. Sliced vertically, each interface sits with the "
                  "class that implements it, `Place` in `stations` and `DemandSource` in "
                  "`riders`: of 17 dependencies, 10 fall inside a module and 7 across, and "
                  "`fleet`, `rebalancing` and `riders` lie on a cycle."),
            ("p", "Sliced horizontally, with both interfaces in the `rebalancing` module, 11 "
                  "fall inside and 6 across, and there is no cycle between modules. Five "
                  "dependencies cross the core's boundary, and every one of them points into "
                  "it: the stations, the fleet and the riders depend on the core and the core "
                  "on none of them. That is the shape the pattern describes, specialised "
                  "modules referring to the abstract core rather than to each other, though "
                  "`Trip` still refers to `Bike` in another specialised module. The interfaces earned "
                  "their place because places and demand are what rebalancing is about; "
                  "the lab would have counted the same for any two interfaces."),
            ("code", _lines(ABSTRACT_CORE)),
            ("h3", "Exercise"),
            ("ul", [
                "A seed bank's model, whose core is deciding when stored seed must be grown "
                "again. Classes: `Accession`, `GerminationTest`, `ViabilityForecast`, "
                "`RegenerationPlan`, `Donor`, `Shipment`.",
                "Dependencies (from, to): GerminationTest, Accession; ViabilityForecast, "
                "GerminationTest; RegenerationPlan, ViabilityForecast; RegenerationPlan, "
                "Accession; Accession, Donor; Shipment, Accession; Accession, "
                "ViabilityForecast.",
                "Packaging A: `stock` holds Accession, GerminationTest and "
                "ViabilityForecast; `ops` holds RegenerationPlan, Shipment and Donor. "
                "Packaging B: `viability` holds GerminationTest, ViabilityForecast and "
                "RegenerationPlan; `stock` holds Accession and Donor; `dispatch` holds "
                "Shipment. `viability` is the core's module.",
            ]),
            ("p", "By hand, find the dependencies inside and across modules in each "
                  "packaging, the dependencies across the core's boundary in packaging B, and "
                  "any cycle between B's modules. Then type both packagings into the lab."),
            ("p", "Distillation sorts a model by what matters most. The next course, "
                  "Large-Scale Structure and Strategy, reads Evans's third strategic "
                  "principle, after context and distillation: an order that lets a whole system be understood in terms of "
                  "its role in the parts."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "cohesion",
            "packagings": 2,
            "names": ["first packaging", "second packaging"],
            "preset": "mixed-and-segregated",
            "presets": [
                {"id": "mixed-and-segregated",
                 "label": "The bike-share model as history packaged it, and with the core segregated",
                 "elements": BIKE_MODEL_ELEMENTS,
                 "deps": BIKE_MODEL_DEPS,
                 "expect": {"dmoInside": "9", "dmoAcross": "9", "dmoShare": "1/2 = 50%",
                            "dmoCycles": "1: (fleet, riders, stations)", "dmoPair": "fleet and ops: 3",
                            "dmoInside2": "8", "dmoAcross2": "10", "dmoShare2": "4/9 ≈ 44.4%",
                            "dmoCycles2": "1: (fleet, rebalancing, riders, stations)"}},
                {"id": "abstract-core",
                 "label": "The model redesigned around an abstract core, sliced vertically and horizontally",
                 "elements": ABSTRACT_ELEMENTS,
                 "deps": ABSTRACT_DEPS,
                 "expect": {"dmoInside": "10", "dmoAcross": "7", "dmoCycles": "1: (fleet, rebalancing, riders)",
                            "dmoInside2": "11", "dmoAcross2": "6", "dmoShare2": "11/17 ≈ 64.7%",
                            "dmoCycles2": "0: none"}},
            ],
            "panel_title": "Dependencies inside, across, and across the core",
            "panel_intro": _COHESION_INTRO,
        }),
        "steps_title": "Segregating a core",
        "steps_intro": "Five steps, Evans's own in outline, the last on a model of your own.",
        "steps": [
            ("Pick one core subdomain",
             "Take the core's elements from the distillation document or the flags, and "
             "choose the most closely related few."),
            ("Move them into a named module",
             "Create a module whose name says what unites them, and move the "
             "classes as they are."),
            ("Cut out what is not the concept",
             "From each moved class, take out the data and behaviour that do not express "
             "the core concept, and put them in classes outside the module."),
            ("List the boundary",
             "Write down every dependency that crosses the new module's boundary, in both "
             "directions, and look for an abstraction that would make the outward ones "
             "point inward."),
            ("Do it on your own model",
             "Type a system's classes and dependencies into the lab with two packagings, "
             "before and after segregating its core, and write down the dependencies "
             "inside, across and across the core's boundary."),
        ],
        "worked": {
            "title": "The segregated packaging",
            "intro": [
                "Count the dependencies in <code>mixed-and-segregated</code>, segregated.",
            ],
            "lines": [
                "riders inside: 4; stations inside: 1",
                "fleet inside: 1; core inside: 2",
                "inside: 4 + 1 + 1 + 2, so 8; across: 10",
                "out of the core: 5 dependencies",
                "into the core: VanRun, Station: 2",
                "across the core boundary: 5 + 2, so 7",
            ],
            "after": [
                "Out of the core run the forecast to `Trip` and to `Station`, the move to "
                "`Station` and to `Bike`, and the plan to `RepairTicket`; into it run "
                "`VanRun` to `Move` and `Station` to `DemandForecast`. The last of these "
                "closes the cycle between `stations` and `rebalancing`.",
            ],
        },
        "quiz_title": "Segregated and abstract cores",
        "quiz": [
            {"q": "In the exercise, how many dependencies fall inside a module and across "
                  "modules in packaging B, how many cross the core's boundary, and is there "
                  "a cycle?",
             "a": ["3 inside, 4 across; 3 across the core's boundary; a cycle between "
                   "viability and stock",
                   "3 inside, 4 across; 4 across the core's boundary; no cycle",
                   "4 inside, 3 across; 3 across the core's boundary; a cycle between "
                   "viability and stock",
                   "3 inside, 4 across; 3 across the core's boundary; no cycle"],
             "c": 0,
             "why": "Inside B: ViabilityForecast to GerminationTest and RegenerationPlan to "
                    "ViabilityForecast in `viability`, Accession to Donor in `stock`: 3. "
                    "Across: GerminationTest to Accession, RegenerationPlan to Accession, "
                    "Shipment to Accession and Accession to ViabilityForecast: 4. Of those, "
                    "all but Shipment to Accession touch `viability`: 3. GerminationTest to "
                    "Accession runs from `viability` to `stock` and Accession to "
                    "ViabilityForecast runs back, so the two modules form a cycle. Packaging "
                    "A also has 3 inside and 4 across; removing Accession's dependency on "
                    "the forecast would break B's cycle."},
            {"q": "Which cost of a Segregated Core does Evans name and judge worth paying?",
             "a": ["It always lowers the number of dependencies in the model",
                   "It may break up a module that was cohesive in another way, for the sake "
                   "of the core's cohesion",
                   "It requires buying a framework",
                   "It forces the core to depend on no other module"],
             "c": 1,
             "why": "He says segregation can sacrifice a nicely cohesive module, and can leave "
                    "the links to closely coupled non-core classes murkier, and "
                    "that both are outweighed by a clearer core. On the lesson's "
                    "illustration the share of dependencies inside a module fell from 9 of "
                    "18 to 8 of 18, because the forecast left `stations`."},
            {"q": "What does Evans say happens if you build an Abstract Core by moving every "
                  "class frequently referenced across modules into one module?",
             "a": ["A good first approximation, to be refined later",
                   "A Segregated Core",
                   "The likely result is a meaningless mess; the real thing needs deep "
                   "understanding and usually considerable redesign",
                   "A Generic Subdomain"],
             "c": 2,
             "why": "The process is not mechanical, he says: the abstractions must be "
                    "fundamental concepts of the domain, found by refactoring toward deeper "
                    "insight. The lesson's abstract core needed two new interfaces and "
                    "changed dependencies, not only a move."},
            {"q": "Choosing Refactoring Targets: in a pain-driven refactoring, what does "
                  "Evans tell you to check first?",
             "a": ["Whether the root of the pain involves the core, or the core's "
                   "relationship to a supporting element; if so, fix that first",
                   "Which module has the most dependencies",
                   "Whether the code has tests",
                   "Which change is smallest"],
             "c": 0,
             "why": "He rejects both starting anywhere and refactoring only where it hurts, "
                    "and offers instead: when pain drives the work, look for a root in the "
                    "core or its relationship to support and bite the bullet there; when "
                    "free to choose, improve the core's factoring and its segregation, and "
                    "purify supporting subdomains until they are generic."},
        ],
        "mistakes": [
            ("Expecting a Segregated Core to make every module more cohesive",
             "Evans says the opposite can happen: segregation may break up a module that "
             "was cohesive in another way, and may leave the links to closely coupled "
             "non-core classes murkier, and he judges the cost worth paying for the "
             "core's sake. It is also a lot of work across the whole system. On the "
             "lesson's illustration the share of dependencies inside a module fell from "
             "9 of 18 to 8 of 18 when the core was segregated."),
            ("Building an Abstract Core by moving the most-referenced classes",
             "Evans warns that doing it mechanically, by moving whatever is often referenced "
             "across modules, gives a meaningless mess. The abstractions must be fundamental "
             "concepts of the domain whose polymorphic interfaces carry most of the "
             "interaction; finding them is refactoring toward deeper insight and usually "
             "needs considerable redesign."),
            ("Refactoring everywhere at once, or only where it hurts",
             "Choosing Refactoring Targets rejects both: the first is impractical except for "
             "teams of top programmers, and the second picks at the edges and avoids the "
             "worst tangles. Evans's rule is to look for the core in the root of the pain, "
             "and when free, to work on the core's factoring and segregation and on "
             "purifying supporting subdomains until they are generic."),
        ],
        "standard": (
            "Finish when you can segregate a core and count what it does to the boundary.",
            "Given a model's classes and dependencies in two packagings, count the "
            "dependencies inside and across modules and across the core's boundary, name "
            "any cycle, and give two costs Evans names for a Segregated Core."
        ),
        "note": (
            "The lab counts where dependencies fall. It cannot tell a module named for a "
            "domain concept from one named for a technical layer, which is what Evans asks "
            "of a Segregated Core, and it cannot tell a fundamental abstraction from a "
            "merely popular class, which is the whole difficulty of an Abstract Core."
        ),
    },
]
