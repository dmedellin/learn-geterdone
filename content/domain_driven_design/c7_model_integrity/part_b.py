"""Maintaining Model Integrity, lessons 6-8 -- Chapter 14, from Separate Ways.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), Chapter 14, Maintaining Model Integrity: Separate Ways,
Open Host Service, Published Language, Unifying an Elephant, Choosing Your
Model Context Strategy and Transformations. Pages in the comments are PDF pages
of the operator's copy; the lessons cite by chapter, section and pattern. Every
quotation is copied from that copy and checked with quotes.py. The networks,
glossaries and maps are written for these lessons (a touring network of
theatres, a bike-share, a bakery, a theatre's box office); none of the book's
examples, diagrams or listings is reproduced. The design is
docs/domain-driven-design/PLAN.md, section C, Course 7.
"""

from .part_a import MODULE, _COGNATES_INTRO, _MAP_INTRO, _rows


# 7.7 Unifying an Elephant: four views of one bicycle in a bike-share.
FOUR_VIEWS = (
    "maintenance, bike, serviceable-asset; "
    "maintenance, station, docking-site; "
    "maintenance, fault, defect-report; "
    "maintenance, trip, test-ride; "
    "rebalancing, bike, movable-unit; "
    "rebalancing, station, docking-site; "
    "rebalancing, trip, van-run; "
    "rebalancing, fill, docked-count; "
    "billing, bike, vehicle-class; "
    "billing, station, docking-site; "
    "billing, trip, paid-ride; "
    "billing, fault, damage-charge; "
    "app, bike, map-pin; "
    "app, station, docking-site; "
    "app, ride, paid-ride; "
    "app, dock-count, docked-count"
)

DEEPER_MODEL = (
    "maintenance, bicycle, bicycle; "
    "maintenance, station, docking-site; "
    "maintenance, defect, defect-report; "
    "maintenance, test-ride, test-ride; "
    "rebalancing, bicycle, bicycle; "
    "rebalancing, station, docking-site; "
    "rebalancing, van-run, van-run; "
    "rebalancing, docked, docked-count; "
    "billing, bicycle, bicycle; "
    "billing, station, docking-site; "
    "billing, ride, paid-ride; "
    "billing, damage-charge, damage-charge; "
    "billing, price-band, vehicle-class; "
    "app, bicycle, bicycle; "
    "app, station, docking-site; "
    "app, ride, paid-ride; "
    "app, docked, docked-count"
)

BAKERY_VIEWS = (
    "shop, order, customer-request; "
    "shop, cake, product-line; "
    "shop, slot, collection-time; "
    "kitchen, order, bake-ticket; "
    "kitchen, cake, batch-item; "
    "kitchen, slot, oven-time; "
    "delivery, order, customer-request; "
    "delivery, drop, delivery-stop; "
    "delivery, slot, delivery-window; "
    "accounts, sale, customer-request; "
    "accounts, cake, product-line"
)

# 7.8 Transformations: Separate Ways to Shared Kernel at a box office.
MERGE_CONTEXTS = "boxoffice membership marketing finance"
MERGE_BEFORE = (
    "boxoffice, membership, separate-ways; "
    "boxoffice, marketing, conformist; "
    "membership, marketing, acl; "
    "boxoffice, finance, acl"
)
MERGE_AFTER = (
    "boxoffice, membership, shared-kernel; "
    "boxoffice, marketing, conformist; "
    "membership, marketing, acl; "
    "boxoffice, finance, acl"
)
MERGED_CONTEXTS = "tickets marketing finance"
MERGED_ONE = (
    "tickets, marketing, conformist; "
    "tickets, finance, acl"
)


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Separate Ways (PDF pp. 230-231 of the operator's copy), with its example
    # (p. 231); Open Host Service (pp. 231-232); Published Language (pp. 232-234),
    # with the DB2 and Btrieve story (p. 233) and the CML example (pp. 233-234,
    # Murray-Rust et al. 1995). Course 7's one modern aside: today's interchange
    # schema languages, in the body's late paragraph.
    # Quote: PDF p. 230 of the operator's copy, 9 words, quotes.py OK.
    # Lesson total: 9 words.
    {
        "slug": "separate-ways-open-host-and-published-language",
        "title": "Separate Ways, Open Host Service and Published Language",
        "module": MODULE,
        "one_line": "Integrate nothing where nothing needs it; where many need you, offer one protocol, ideally in a documented shared language.",
        "summary": (
            "Every integration costs something. Read Evans's Separate Ways, a context with "
            "no connection to the others, and his two patterns for a context many others "
            "need: an Open Host Service with one protocol for all, and a Published Language "
            "for that protocol to speak; then count translators point to point and through "
            "one language."
        ),
        "key": [
            "integration always costs something",
            "no shared logic, no shared data",
            "separate ways forecloses some options",
            "many clients: open one protocol",
            "one team's oddity: a one-off translator",
            "publish: documented, readily available",
            "keep the language apart from the model",
        ],
        "key_label": "Three patterns in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson, one for each of the section's patterns."
        ),
        "concepts": [
            ("Separate Ways",
             "A Bounded Context cut loose from all the others: no shared logic, little or "
             "no data passed through translation, and its developers free to solve its "
             "narrow problem as simply as they can."),
            ("Open Host Service",
             "One interface of Services that a subsystem in demand offers to every context "
             "that integrates with it, grown for common needs, while a lone team's unusual "
             "needs get a translator of their own."),
            ("Published Language",
             "A shared language, documented well, in which the systems can state the "
             "domain information they exchange, used as their common medium, each translating into it "
             "and out of it."),
        ],
        "read_title": "The case against integrating first, then the two ways to scale it",
        "read_intro": (
            "Read Separate Ways, Open Host Service and Published Language in your own copy "
            "first. The lesson reads all three as tools and then counts translators for a "
            "network of contexts."
        ),
        "body": [
            ("p", "&ldquo;Integration is always expensive. Sometimes the benefit is "
                  "small.&rdquo; Evans sets those two sentences at the head of Separate Ways, "
                  "in Chapter 14. This lesson reads that pattern and the two after it, Open "
                  "Host Service and Published Language."),
            ("p", "Separate Ways puts the case for no integration at all. Besides the cost of "
                  "coordinating teams, integration forces compromise: a simple model made for "
                  "one need gives way to a more abstract one that handles every situation; a "
                  "technology that would make some feature easy is hard to fit in; a team may "
                  "be hard to work with. If two parts of a system do not call on each other's "
                  "functions, do not act on objects both touch, and do not share data while "
                  "they run, integrating them, even through translation, may bring nothing. "
                  "Two features meeting in one use case is no proof that they "
                  "need integrating. So cut the context loose and let its developers solve its "
                  "narrow problem as simply as they can; the user interface or "
                  "middleware can still put the features side by side."),
            ("p", "His example is an insurance project that had stalled after a year of "
                  "analysis and infrastructure. A week of ruthless scoping found features "
                  "that integration added little to; they were delivered almost at once as "
                  "small, unconnected applications launched from one menu, and when the main "
                  "project stalled again, those small applications were all it left behind. "
                  "Evans is fair to the cost. Going separate ways closes off options, models "
                  "grown apart are hard to merge, and if integration is needed later the "
                  "translation may be complex."),
            ("p", "Open Host Service turns to the opposite problem: a context many others "
                  "need. A translation layer for each outside component is the cheap answer "
                  "for one-off integrations, but a subsystem in demand that customises a "
                  "translator for every client is soon doing the same work again and again, "
                  "with more to keep and more to worry about at each change. If the "
                  "subsystem is coherent, it can be described as a set of Services that "
                  "cover what the others commonly need. So: describe the subsystem as "
                  "Services behind one protocol any integrating team may use; grow it for "
                  "common needs, and serve one team's unusual needs with its own "
                  "translator, keeping what everyone shares simple. It is harder "
                  "to design a protocol many teams can use, and it pays only with a coherent "
                  "set of Services and many integrations. Its cost: every client is coupled "
                  "to the host's dialect."),
            ("p", "Published Language answers that cost. A domain model built for its own "
                  "users carries features that only complicate exchange, and a model used as "
                  "the exchange medium freezes, since it must stay stable for everyone who "
                  "speaks it. Between businesses, adopting another's model is unrealistic. "
                  "So: take a shared, well-documented language able to carry the "
                  "domain information needed, and make it the common medium, translating into and out of it. "
                  "Publishing, in Evans's sense, means only that the language is available to "
                  "everyone who might use it and documented well enough that independent "
                  "readings are compatible."),
            ("p", "The language need not be new. Evans tells of letting a client's product run "
                  "on a lighter database as well as its original one, by building his "
                  "component on the "
                  "client's own undocumented persistence abstractions. It worked, but "
                  "working out what they required took much effort, the component could not "
                  "be reused elsewhere, and the client's model was more entrenched than "
                  "before; supporting the documented subset of the original database's "
                  "interface would have been better, because that interface was already a "
                  "Published Language. His other example is the Chemical Markup Language, "
                  "an XML dialect for exchanging chemical structures, after Murray-Rust and "
                  "colleagues, which made tools worth writing that one database alone never "
                  "justified."),
            ("p", "Now the count. The lab takes a number of contexts that must all exchange "
                  "information and a scheme. Point to point, every pair needs its own "
                  "translation: n·(n − 1)/2 two-way translators, or n·(n − 1) one-way ones, "
                  "and a change in one context's model touches every translator it is part "
                  "of, n − 1 two-way or 2·(n − 1) one-way. Through a Published Language each "
                  "context needs one translator, to and from the language: n in all, and 1 "
                  "to change when one context's model changes, as long as the language "
                  "itself holds still."),
            ("p", "The lesson's network is six theatres sharing a touring production's "
                  "bookings. On the preset <code>pairwise</code> the lab counts 15 two-way "
                  "translators to build and 5 to change when one theatre's model changes, "
                  "and its other-scheme tile gives the published figures beside them. On "
                  "<code>published</code> it counts 6 to build and 1 to change. The two "
                  "ratio tiles divide pairwise by published: 5/2 as many to build, 5 times "
                  "as many to change. Counted one way, by hand, each figure doubles, "
                  "30 and 10 against 12 and 2, and the ratios stay the same; this lab "
                  "counts two-way translators only. The gap grows with the square of n, which is "
                  "Evans's reason for a protocol when there are many integrations and not "
                  "when there are two: with n = 2, point to point needs 1 two-way "
                  "translator and a published language 2."),
            ("p", "The count leaves out the language itself. Designing one that six theatres "
                  "accept is the hard part Evans describes, and changing it reaches every "
                  "context at once, which is why he asks for a stable one. A note on the "
                  "years since: the XML schemas the chapter points to have been "
                  "joined by JSON Schema, Protocol Buffers and API description formats, "
                  "and many teams now publish their service contracts in them. The "
                  "pattern's demand is the same as it was, documentation good enough that "
                  "independent readers agree, and no schema language meets it on its own."),
            ("h3", "Exercise"),
            ("p", "A regional network of ten venues must all share bookings. Count the "
                  "two-way translators point to point and through a Published Language, and "
                  "the translators each scheme must change when one venue's model changes. "
                  "Then say which of three features a box office is planning could go its "
                  "separate way: a printed programme shop that shares no data with ticket "
                  "sales; seat maps that ticket sales read while selling; a staff rota that "
                  "takes nothing from the box office. Check the counts in the lab with n = "
                  "10."),
            ("p", "Six patterns and a map give a vocabulary for any one boundary. The next "
                  "lesson, Unifying an Elephant and Choosing a Strategy, asks how to choose "
                  "among them for a whole project."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "protocol",
            "directed": "no",
            "preset": "pairwise",
            "presets": [
                {"id": "pairwise",
                 "label": "Six theatres, a two-way translator for every pair",
                 "contexts": "6", "scheme": "pairwise",
                 "expect": {"dcxN": "6", "dcxBuild": "15", "dcxChange": "5", "dcxOther": "published: 6 to build, 1 to change", "dcxBuildRatio": "5/2 ≈ 2.5×", "dcxChangeRatio": "5×"}},
                {"id": "published",
                 "label": "Six theatres through one Published Language",
                 "contexts": "6", "scheme": "published",
                 "expect": {"dcxN": "6", "dcxBuild": "6", "dcxChange": "1", "dcxOther": "pairwise: 15 to build, 5 to change", "dcxBuildRatio": "5/2 ≈ 2.5×", "dcxChangeRatio": "5×"}},
            ],
            "panel_title": "Translators point to point and through one language",
            "panel_intro": (
                "The contexts all exchange information. Point to point, each pair has its own "
                "translator, one two-way or two one-way; through a Published Language, each "
                "context has one translator to and from the language. The lab counts the "
                "translators to build and those to change when one context's model changes. "
                "It does not count the work of designing the language."
            ),
        }),
        "steps_title": "Deciding how far to integrate",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Test the need for integration",
             "For two features, ask whether either calls the other's functions, acts on "
             "objects both touch, or shares data while it runs. If none holds, consider "
             "Separate Ways."),
            ("Count the clients",
             "For a context others need, count the contexts that integrate with it and how "
             "much of what they need is common to them."),
            ("Count the translators",
             "With n contexts, compare n·(n − 1)/2 translators point to point with n through "
             "one language, and n − 1 changed per model change with 1."),
            ("Do it on a system of your own",
             "List the services that call one service you know. Count its client-specific "
             "adapters, say whether a published contract would replace them, and name one "
             "feature that could have gone its separate way."),
        ],
        "worked": {
            "title": "Six theatres, two schemes",
            "intro": [
                "Count the two presets by hand, with n = 6, and the one-way figures beside "
                "them, which the lab does not show.",
            ],
            "lines": [
                "pairs: 6 × 5 / 2 = 15 two-way",
                "one-way: 6 × 5 = 30",
                "published: one each, 6",
                "one theatre changes, pairwise: 5",
                "one theatre changes, one-way: 10",
                "one theatre changes, published: 1",
            ],
            "after": [
                "Point to point grows with n squared, a published language with n. The count "
                "takes the language as given; designing it, and keeping it stable, is the "
                "cost the pattern warns of.",
            ],
        },
        "quiz_title": "Separate ways, hosts and languages",
        "quiz": [
            {"q": "In the exercise (ten venues), how many two-way translators does each "
                  "scheme build, and how many must change when one venue's model changes?",
             "a": ["Pairwise 100 and 10; published 10 and 1",
                   "Pairwise 90 and 18; published 10 and 1",
                   "Pairwise 45 and 9; published 10 and 10",
                   "Pairwise 45 and 9; published 10 and 1"],
             "c": 3,
             "why": "Ten venues make 10 × 9 / 2 = 45 pairs, and one venue is in 9 of them. "
                    "Through a language each venue has one translator, 10 in all, and only "
                    "the changed venue's own translator changes: 1. 90 and 18 are the one-way "
                    "counts. Of the three features, the programme shop and the staff rota "
                    "could go their separate ways; seat maps that ticket sales read while "
                    "selling share data in operation and could not."},
            {"q": "When does Evans say an Open Host Service pays off?",
             "a": ["Whenever a subsystem has at least one client",
                   "When what the subsystem offers forms a coherent set of "
                   "Services and there are a significant number of integrations",
                   "Only when an industry-standard language exists",
                   "When every client team has the same peculiar needs"],
             "c": 1,
             "why": "A protocol clean enough for many teams is harder to design, so it pays "
                    "only with a coherent set of Services and many integrations. A single "
                    "team's peculiar needs get a one-off translator instead, to keep the "
                    "protocol simple."},
            {"q": "What does Evans mean by publishing a language?",
             "a": ["Making it an international standard",
                   "Selling it as a product",
                   "Making it readily available to those who might use it, and documented "
                   "well enough that independent interpretations are compatible",
                   "Using the host's internal domain model as the exchange format"],
             "c": 2,
             "why": "He says he simply means availability to the interested community and "
                    "documentation good enough for independent readings to agree. Using a "
                    "host's own model as the medium is what freezes that model, the problem "
                    "the pattern answers."},
            {"q": "Which cost of Separate Ways does Evans name?",
             "a": ["It forecloses some options: models developed in isolation are hard to "
                   "merge, and later integration may need complex translation",
                   "It requires a Shared Kernel later",
                   "It cannot be combined with a shared user interface",
                   "It doubles the size of every team"],
             "c": 0,
             "why": "Taking separate ways forecloses options, since merging isolated models "
                    "is hard and translation layers may be needed after all. He allows the "
                    "features to be organised together in middleware or the user interface."},
        ],
        "mistakes": [
            ("Integrating everything that appears in one use case",
             "Features that a user meets together seem to belong together. Evans answers that "
             "sharing a use case is no proof they need integrating: if they do not "
             "call each other, touch shared objects or share data in operation, a common "
             "menu may be all they need. On the lesson's illustration the programme shop and "
             "the staff rota are such features."),
            ("Exposing the host's domain model as its open protocol",
             "It saves designing a second vocabulary. But a model used as the exchange medium "
             "must stay stable for every client and so cannot change freely, which is the "
             "problem Published Language names; Evans's advice on the transformation to a "
             "Published Language is to keep the interchange language and the host's model "
             "apart."),
            ("Widening the shared protocol for each client's special case",
             "The pattern extends the protocol for new integration needs, but a single team's "
             "idiosyncratic needs go to a one-off translator, so that the protocol everyone "
             "shares stays simple and coherent."),
        ],
        "standard": (
            "Finish when you can compare translators point to point and through one language.",
            "Given n contexts that must exchange information, state the translators each "
            "scheme builds and changes, and say when Separate Ways would build none."
        ),
        "note": (
            "The lab's counts are combinatorics on n. It cannot weigh what a translator "
            "costs against what the language costs to design and keep stable, or say "
            "whether two features need integrating at all, which is the judgement Separate "
            "Ways asks for."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Unifying an Elephant (PDF pp. 234-237 of the operator's copy), after
    # John Godfrey Saxe's poem; Choosing Your Model Context Strategy
    # (pp. 237-242): Team Decision or Higher, Putting Ourselves in Context,
    # Transforming Boundaries, the External Systems, the System Under Design,
    # Catering to Special Needs, Deployment, The Trade-off, When Your Project Is
    # Already Under Way.
    # Quote: PDF p. 236 of the operator's copy, 10 words, quotes.py OK.
    # Lesson total: 10 words.
    {
        "slug": "unifying-an-elephant",
        "title": "Unifying an Elephant and Choosing a Strategy",
        "module": MODULE,
        "one_line": "Partial models of one thing need not agree to be useful; unifying them means building a new one, and choosing how far to go is a trade.",
        "summary": (
            "Evans's blind men each model a different part of one elephant. Read what it "
            "takes to unify their models, and his guidelines for choosing contexts and "
            "relationships for a whole project; then count the overlaps and conflicts in "
            "four teams' glossaries of one bicycle."
        ),
        "key": [
            "partial models can still cooperate",
            "knowing you disagree is most of it",
            "unifying means a new model",
            "first a crude whole, then a deeper one",
            "map what is, then choose changes",
            "larger: smoother; smaller: cheaper",
            "the trade: independence or integration",
        ],
        "key_label": "Unifying and choosing in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the elephant's, the third the "
            "strategy section's."
        ),
        "concepts": [
            ("Partial models",
             "Models of one thing built by people who each see a part of it. They may never "
             "agree, and still cooperate on the little they share, once they know they do "
             "not agree."),
            ("Part-whole and deeper unification",
             "The two stages of joining partial models. First relate the parts into a crude "
             "whole; later, driven by new needs or insight, replace it with a deeper model "
             "whose new concepts drop what was incidental or wrong in each part."),
            ("The system under design",
             "The part of the software your team is actually changing, where you can declare "
             "contexts and choose relationships, as against the external systems you can "
             "only conform to, translate or leave alone."),
        ],
        "read_title": "The fable first, then the guidelines, then the count",
        "read_intro": (
            "Read Unifying an Elephant and Choosing Your Model Context Strategy in your own "
            "copy first. The lesson reads the fable as an argument and the guidelines as a "
            "checklist, then counts four partial glossaries."
        ),
        "body": [
            ("p", "&ldquo;Unifying multiple models almost always means creating a new "
                  "model.&rdquo; That is the turn in Unifying an Elephant, in Chapter 14. "
                  "This lesson reads that section and the long one after it, Choosing Your "
                  "Model Context Strategy."),
            ("p", "The section opens with John Godfrey Saxe's poem The Blind Men and the "
                  "Elephant, after a story in the Udana: six blind men each touch one part "
                  "of an elephant and declare it a wall, a snake, a tree, a rope. Evans's "
                  "reading is generous to them. If they need no integration, it does not "
                  "matter that their models disagree; if they need some, they gain most "
                  "simply by recognising that they disagree, so that they stop talking at "
                  "cross purposes. With separate contexts drawn, they can agree on the one "
                  "thing they all care about, perhaps where the elephant is."),
            ("p", "As they need to share more, a single context is worth more, and harder to "
                  "reach. None will give up his model for another's, since the man holding "
                  "the tail knows it is no tree; hence the quotation. The first stage is "
                  "part and whole: relate the pieces, and get a crude elephant, a wall on "
                  "four trees with a snake and a rope at the ends. It is incoherent, but it "
                  "may serve. A new requirement or a new insight, the elephant walking, "
                  "say, forces a deeper model, with an animal and its parts in clear "
                  "relationships. The harder case is two people describing the same part "
                  "differently, a snake against a fire hose, where neither model survives "
                  "and a new abstraction must keep what is apt in each. Unification, he says, "
                  "depends on minimalism: lacking a feature is better than carrying a wrong "
                  "one."),
            ("p", "Choosing Your Model Context Strategy starts from the current map and "
                  "offers guidelines for changing it. The decisions are the team's, or "
                  "higher: on the merits they trade the value of teams acting independently "
                  "against the value of rich integration, and in practice politics often "
                  "decides. Your own context biases your map, which is fine if you know it. "
                  "Evans lists the forces. Larger contexts give smoother flow between user "
                  "tasks, one coherent model instead of two and a mapping, no difficult "
                  "translation, and a shared language. Smaller ones mean less communication "
                  "overhead, easier Continuous Integration, no call for abstract models whose "
                  "skills are scarce, and room for specialised jargons."),
            ("p", "He starts with the easy decisions. External systems are outside your "
                  "contexts, though they may only weakly be contexts themselves, so check "
                  "that their models are really unified. Toward them, consider Separate Ways "
                  "first, then choose between Conformist, wholeheartedly, for a peripheral "
                  "extension with a large interface, and an Anticorruption Layer otherwise. "
                  "Within the system under design, one context may do for a team of fewer "
                  "than ten on closely related work; a larger team can break off independent "
                  "parts, each under ten, with a Shared Kernel or, for one-way dependence, "
                  "Customer/Supplier teams; clashing mindsets may go their separate ways with "
                  "a jointly kept translation layer. Generally there is one team to a "
                  "context."),
            ("p", "Distinct models can serve specialised groups' jargons, at the price of "
                  "lost shared language, integration overhead and duplicated effort; the "
                  "biggest risk, he warns, is that this becomes an excuse for any parochial "
                  "model. Deployment feeds back into boundaries too: a translation layer lets "
                  "one context be updated alone, a kernel ties both releases together. The "
                  "trade, in sum, is independence against smoother communication. And on a "
                  "project already under way, first map the contexts as they really are, "
                  "tighten integration inside them, gather stray translation code into the "
                  "layers, name the contexts, and only then change boundaries, in small "
                  "pieces."),
            ("p", "Now the count. The lab is the one from Bounded Context, with four contexts: "
                  "a bike-share's maintenance workshop, its van crews who rebalance bikes "
                  "between stations, billing, and the rider app. Each has its own model of a "
                  "bike. On the preset <code>four-views</code> the lab counts 4 contexts and "
                  "7 terms, 4 of them shared. 3 are false cognates: `bike`, with four "
                  "meanings, `trip`, with three, and `fault`, with two. 1 term is safe to "
                  "share, `station`, and there are 2 duplicate concepts, the paid ride "
                  "(`trip` and `ride`) and the count of docked bikes (`fill` and "
                  "`dock-count`)."),
            ("code", _rows(FOUR_VIEWS)),
            ("p", "This is the elephant. To the workshop a bike is an asset to be serviced; "
                  "to the van crews a unit to move; to billing a class with a price; to the "
                  "app a pin on a map. None of them is wrong, and none will give way. The "
                  "one safe term, `station`, is the elephant's location: if all they need is "
                  "to agree where bikes are, translating that one concept is enough, and the "
                  "false cognates can stay behind their boundaries."),
            ("p", "The preset <code>deeper-model</code> is what unifying would mean: a new "
                  "concept, `bicycle`, that every context uses alike, with each partial view "
                  "kept as a term of its own, `test-ride`, `van-run`, `price-band`, and the "
                  "duplicates given one name each. The lab counts 9 terms, 4 shared, all 4 "
                  "safe to share, 0 false cognates and 0 duplicate concepts. It is a new "
                  "model, as the quotation says; no team's old `bike` survived. Whether the "
                  "four teams need it, or only need to agree on stations, is the strategy "
                  "question, and the count does not answer it."),
            ("h3", "Exercise"),
            ("code", _rows(BAKERY_VIEWS)),
            ("p", "A bakery's shop, kitchen, delivery round and accounts, four partial "
                  "models of an order. Find the shared terms, the false cognates and the "
                  "duplicate concepts, and say which term, if any, is safe to share. Then "
                  "name the one concept a minimal integration would translate, and check "
                  "your count in the lab."),
            ("p", "A strategy chosen is not fixed. The last lesson of the chapter, "
                  "Transformations, reads how to move a relationship from one pattern to "
                  "another, step by step."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "cognates",
            "preset": "four-views",
            "presets": [
                {"id": "four-views",
                 "label": "Four teams' partial models of a bike",
                 "contexts": FOUR_VIEWS,
                 "expect": {"dlnContexts": "4: maintenance, rebalancing, billing, app", "dlnTerms": "7", "dlnShared": "4: bike, station, fault, trip", "dlnFalse": "3: bike (maintenance: serviceable-asset, rebalancing: movable-unit, billing: vehicle-class, app: map-pin); fault (maintenance: defect-report, billing: damage-charge); trip (maintenance: test-ride, rebalancing: van-run, billing: paid-ride)", "dlnDuplicate": "2: docked-count: fill (rebalancing), dock-count (app); paid-ride: trip (billing), ride (app)", "dlnSafe": "1: station"}},
                {"id": "deeper-model",
                 "label": "A deeper model: one bicycle, each view a term of its own",
                 "contexts": DEEPER_MODEL,
                 "expect": {"dlnContexts": "4: maintenance, rebalancing, billing, app", "dlnTerms": "9", "dlnShared": "4: bicycle, station, docked, ride", "dlnFalse": "0: none", "dlnDuplicate": "0: none", "dlnSafe": "4: bicycle, station, docked, ride"}},
            ],
            "panel_title": "Four partial models of one thing",
            "panel_intro": _COGNATES_INTRO,
        }),
        "steps_title": "Choosing how far to unify",
        "steps_intro": "Five steps, the last of them on a project of your own.",
        "steps": [
            ("Write each partial model",
             "For each context, list its terms for the shared thing and the concepts they "
             "stand for."),
            ("Find what they really share",
             "Mark the terms safe to share. If integration needs only those, translate them "
             "and stop."),
            ("Weigh the forces",
             "For a larger context, list the user tasks that would flow better and the "
             "translations that would go; for smaller ones, the communication saved and the "
             "jargons kept."),
            ("Sketch the new model if you unify",
             "Name the new concept that replaces the clashing ones, keep each partial view as "
             "a term of its own, and drop any feature none of the parts can justify."),
            ("Do it on your own project",
             "Pick one entity that three systems you know each model, such as a customer or "
             "a product. Write their glossaries, count the false cognates, and say whether "
             "the systems need a deeper model or only one agreed concept."),
        ],
        "worked": {
            "title": "Four views of a bike",
            "intro": [
                "Count <code>four-views</code> by hand.",
            ],
            "lines": [
                "bike: four contexts, four meanings",
                "trip: three contexts, three meanings",
                "fault: maintenance and billing, differ",
                "station: docking-site in all four, safe",
                "paid-ride: trip and ride",
                "docked-count: fill and dock-count",
            ],
            "after": [
                "Three false cognates, one safe term, two duplicates. The safe term is the "
                "minimal integration; the false cognates are what a deeper model would have "
                "to replace.",
            ],
        },
        "quiz_title": "Elephants and strategy",
        "quiz": [
            {"q": "In the exercise (the bakery's four views of an order), how many false "
                  "cognates are there, and how many terms are safe to share?",
             "a": ["2 false cognates, 1 safe term",
                   "3 false cognates, 0 safe terms",
                   "3 false cognates, 1 safe term",
                   "1 false cognate, 2 safe terms"],
             "c": 1,
             "why": "Three terms are shared: `order` (a customer-request to the shop and "
                    "delivery, a bake-ticket to the kitchen), `cake` (a product-line to the "
                    "shop and accounts, a batch-item to the kitchen) and `slot` (collection, "
                    "oven and delivery times). Each has at least two meanings, so all 3 are "
                    "false cognates and 0 are safe. The 1 duplicate is the customer-request, "
                    "an `order` in the shop and delivery and a `sale` in accounts; it is "
                    "the concept a minimal integration would translate."},
            {"q": "What does Evans say the blind men gain if they need some integration but "
                  "not a unified model?",
             "a": ["A lot from merely recognising that they do not agree",
                   "Nothing until they agree on what an elephant is",
                   "A Shared Kernel of the elephant's parts",
                   "A Published Language for elephants"],
             "c": 0,
             "why": "They need not agree on what an elephant is; recognising that they "
                    "disagree stops them talking at cross purposes, and separate contexts let "
                    "them agree on the little they share, such as the elephant's location."},
            {"q": "Which of these does Evans list as a force favouring smaller Bounded "
                  "Contexts?",
             "a": ["Flow between user tasks is smoother",
                   "One coherent model is easier to understand than two plus mappings",
                   "Smaller teams and code bases make Continuous Integration easier",
                   "A shared language fosters clear communication"],
             "c": 2,
             "why": "Easier Continuous Integration is on the smaller list, with reduced "
                    "communication overhead, less need for scarce abstract-modelling skills, "
                    "and room for specialised jargons. The other three are on his list "
                    "favouring larger contexts."},
            {"q": "For a project already under way, what does Evans say to do first?",
             "a": ["Redraw the contexts by the guidelines for a new project",
                   "Replace the legacy systems",
                   "Merge every context into a Shared Kernel",
                   "Define the Bounded Contexts as things are now, reflecting the teams' true "
                   "practice"],
             "c": 3,
             "why": "The map must reflect how the teams really work, not the ideal "
                    "organisation; then tighten integration within the contexts, gather "
                    "stray translation into the layers and name the contexts, before "
                    "changing boundaries in small pieces."},
        ],
        "mistakes": [
            ("Thinking unification means one team's model wins",
             "It looks like the quickest merger: pick the best model and convert the others. "
             "Evans says none of the partial modellers will accept another's model, since it "
             "contradicts what each knows, and that unifying almost always means a new "
             "model, first a crude whole and later a deeper one. On the lesson's "
             "illustration the deeper model replaces every team's `bike` with a `bicycle` "
             "none of them had."),
            ("Treating specialised jargons as always worth a context of their own",
             "Distinct models can keep a group's precise terminology, and Evans allows it; "
             "but he names the costs, lost shared language, integration overhead and "
             "duplicated effort, and warns that the biggest risk is a justification for any "
             "quirky, parochial model. The value of the jargon must be weighed."),
            ("Planning on a deep model to resolve the conflicts",
             "A deep model that unifies two dialects sometimes emerges, Evans says, but late, "
             "after much knowledge crunching, if at all. It cannot be scheduled; when it "
             "comes, change the strategy and refactor."),
        ],
        "standard": (
            "Finish when you can say what unifying partial models would take.",
            "Given several contexts' glossaries of one thing, find the safe terms, false "
            "cognates and duplicates, and say what minimal integration and a deeper model "
            "would each need."
        ),
        "note": (
            "The lab counts disagreements in the words written down. It cannot invent the "
            "deeper model, which comes from knowledge crunching, and it cannot weigh "
            "independence against integration or the politics Evans says often decide; the "
            "counts only show how far apart the partial models are."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Transformations (PDF pp. 242-246 of the operator's copy): Merging Contexts,
    # Separate Ways to Shared Kernel (pp. 242-243); Shared Kernel to Continuous
    # Integration (pp. 243-244); Phasing Out a Legacy System (pp. 244-245); Open
    # Host Service to Published Language (p. 245); the chapter's close (pp. 245-246).
    # Quote: PDF p. 242 of the operator's copy, 22 words, quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "transformations",
        "title": "Transformations",
        "module": MODULE,
        "one_line": "Move a relationship along the range from separate ways to one context in small steps, each with its process and its tests.",
        "summary": (
            "Decisions about contexts are not final. Read Evans's game plans for four hard "
            "changes, merging separate contexts into a Shared Kernel, a kernel into one "
            "context, phasing out a legacy system, and an Open Host Service into a Published "
            "Language; then count what one change reaches on a map before and after a merger."
        ),
        "key": [
            "splitting is easy; merging is hard",
            "too big for one iteration: plan steps",
            "to merge, go through a Shared Kernel",
            "start small, generic, already translated",
            "prepare the people before the code",
            "retire legacy one iteration at a time",
            "keep the language apart from the host",
        ],
        "key_label": "Transformations in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson, each the name of one of the section's game plans."
        ),
        "concepts": [
            ("Merging contexts",
             "Moving two contexts toward one model, first from Separate Ways to a small Shared "
             "Kernel grown subdomain by subdomain, and then, if wanted, from the kernel to one "
             "context under Continuous Integration."),
            ("Phasing out a legacy system",
             "Moving the legacy system's functions into the newer systems one iteration at a "
             "time, adding to the Anticorruption Layer as needed and removing what is no "
             "longer used once each step is running."),
            ("Open Host Service to Published Language",
             "Replacing a growing set of ad hoc protocols with a formal language: an industry "
             "standard if one exists, or one based on the host's sharpened core, published to "
             "everyone in the collaboration."),
        ],
        "read_title": "The game plans first, then the count before and after",
        "read_intro": (
            "Read Transformations, to the end of Chapter 14, in your own copy first. The "
            "lesson reads the four game plans as checklists and then counts one change on a "
            "map before and after a merger."
        ),
        "body": [
            ("p", "&ldquo;These transformations are usually much too big to be taken in a "
                  "single refactoring or possibly even in a single project iteration.&rdquo; "
                  "That is from the opening of Transformations, the last section of Chapter "
                  "14. This lesson reads its four game plans and the chapter's close."),
            ("p", "Decisions about contexts can be revisited and often must be. Breaking a "
                  "context up is fairly easy, Evans says; merging contexts or changing their "
                  "relationship is hard. So each game plan is a series of manageable steps, "
                  "and he presents them as guidelines to adapt, not procedures."),
            ("p", "Merging from Separate Ways to a Shared Kernel comes first, prompted by "
                  "translation that costs too much or duplication that is too plain. Even if "
                  "the goal is one context, go through a kernel. Check that each context is "
                  "unified inside before unifying them with each other. Set up the process "
                  "before any shared code: how code is shared, how modules are named, at "
                  "least weekly integration, and a test suite, which, being empty, is easy "
                  "to pass at first. Choose a small subdomain duplicated in both, generic "
                  "rather than core, ideally one already translated, so the translation is "
                  "proven and thins as you go. A group of two to four developers from both "
                  "teams works out its model in detail, synonyms included, with a basic set "
                  "of tests; others implement it; each team integrates; translations no "
                  "longer needed are removed. Then repeat with more."),
            ("p", "For the merge itself there are three approaches: adopt one context's model "
                  "wholesale, take pieces from each with care not to make a jumble, or find a "
                  "new model deeper than both. Two cautions follow. Defer merging parts "
                  "tailored to different users' jargons until a deep model can replace "
                  "both. And consider the alternative of moving whole subdomains into the "
                  "favoured context without sharing anything, which removes redundancy with "
                  "no integration overhead but keeps Separate Ways' trade-offs meanwhile."),
            ("p", "From Shared Kernel to Continuous Integration is a change of people and "
                  "language as much as of code. Put each team's integration practices in "
                  "place and make them alike; circulate people between the teams; distil "
                  "each model, which is Chapter 15's subject; then merge the core domains "
                  "into the kernel, quickly once begun, since that phase is costly and "
                  "error-prone, choosing again between one model, a new one, or a deeper "
                  "one that keeps both specialised powers. Raise the integration frequency "
                  "to daily and then continuous, until one team, or two sharing one code "
                  "base, is left."),
            ("p", "Phasing Out a Legacy System takes a common case: an old system in daily "
                  "use, newer systems talking to it through an Anticorruption Layer. Decide "
                  "the testing strategy first; some organisations run old and new in "
                  "parallel. Each iteration, pick functions that one iteration can move, the "
                  "layer's needed additions, implement and deploy; once running, remove the "
                  "parts of the layer no longer needed and, where practical, the unused "
                  "legacy modules. The layer will shrink and swell as you go; other things "
                  "equal, move first what makes it smaller. Open Host Service to Published "
                  "Language, the last plan, uses an industry standard if one exists, or else "
                  "sharpens the host's core domain into an interchange language, publishes "
                  "it, builds translators and switches over; the language must be stable, so "
                  "keep it apart from the host's model."),
            ("p", "The chapter ends with a warning. Contexts are sometimes used for a problem "
                  "they do not solve: a large model that seems too complex to grasp gets cut "
                  "into pieces, and integration is lost. If a large context meets real "
                  "integration needs and is feasible apart from its complexity, look first "
                  "at the next two chapters' tools, distillation and large-scale structure."),
            ("p", "Now the count, on a theatre box office and the membership scheme that "
                  "went its separate way years ago, with marketing conforming to the box "
                  "office and translating membership's data through a layer, and finance "
                  "translating the box office's. The box office changes its model of a "
                  "sale. On the preset <code>before</code> the lab counts 4 relationships, 1 "
                  "model that must change, marketing, 1 translator to update, finance's, "
                  "and 1 context untouched, membership. On <code>after</code>, with the first step of "
                  "the merger taken and the separate ways made a Shared Kernel, the same "
                  "change reaches 2 models, membership and marketing, and 2 translators, "
                  "finance's and marketing's layer for membership, and leaves 0 untouched."),
            ("code", _rows(MERGE_AFTER)),
            ("p", "The merger makes a change reach further, and that is not a defect in it. "
                  "A kernel is a promise to change together, and Evans's deployment remark "
                  "says the same: a kernel ties two contexts' releases, where separate ways "
                  "leave each free. What the count does not show is what the merger bought: "
                  "the duplicated membership concepts the box office kept, and the "
                  "translation the two teams no longer need. Each step of the game plan is "
                  "a choice of which of those to pay."),
            ("h3", "Exercise"),
            ("code", _rows(MERGED_ONE)),
            ("p", "Suppose the plan runs to its end: the kernel grows until box office and "
                  "membership are one context, `tickets`, under Continuous Integration, and "
                  "marketing's layer for membership is no longer needed. The map is above. "
                  "When `tickets` changes, find the models that must change and the "
                  "translators to update, and compare with <code>before</code> and "
                  "<code>after</code>. Then check it in the lab."),
            ("p", "Chapter 14 ends by pointing past itself, and so does this course. The next "
                  "course, Distillation, reads Chapter 15: how to find the Core Domain of a "
                  "large model and give it the attention it deserves."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "map",
            "preset": "before",
            "presets": [
                {"id": "before",
                 "label": "Before: box office and membership go separate ways",
                 "contexts": MERGE_CONTEXTS,
                 "rels": MERGE_BEFORE,
                 "changed": "boxoffice",
                 "expect": {"dcxRels": "4", "dcxModels": "1: marketing", "dcxTranslators": "1: finance’s ACL from boxoffice", "dcxReached": "2: marketing, finance", "dcxUntouched": "1: membership"}},
                {"id": "after",
                 "label": "After the first step: a small Shared Kernel",
                 "contexts": MERGE_CONTEXTS,
                 "rels": MERGE_AFTER,
                 "changed": "boxoffice",
                 "expect": {"dcxRels": "4", "dcxModels": "2: membership, marketing", "dcxTranslators": "2: marketing’s ACL from membership, finance’s ACL from boxoffice", "dcxReached": "3: membership, marketing, finance", "dcxUntouched": "0: none"}},
            ],
            "panel_title": "One map before and after a transformation",
            "panel_intro": _MAP_INTRO,
        }),
        "steps_title": "Planning a transformation",
        "steps_intro": "Five steps, the last of them on a boundary you would change.",
        "steps": [
            ("Map the boundary as it is",
             "Draw the two contexts and every relationship they have, and check that each is "
             "unified inside before joining them."),
            ("Set up the process first",
             "Decide how code is shared and named, how often the kernel is integrated, and "
             "start its test suite before any shared code exists."),
            ("Pick the first subdomain",
             "Choose something small, duplicated in both, not in the core, and ideally "
             "already translated."),
            ("Count before and after",
             "Trace one likely change on the map before the step and after it, and write "
             "down what it reaches and which translations the step removes."),
            ("Do it on a boundary you would change",
             "Pick two services you know that duplicate one concept. Name the first "
             "subdomain you would share, the tests it needs, and the translation it would "
             "let you delete."),
        ],
        "worked": {
            "title": "The box office change, after the first step",
            "intro": [
                "Trace <code>after</code> by hand.",
            ],
            "lines": [
                "boxoffice to membership: kernel, changes",
                "boxoffice to marketing: conformist, changes",
                "membership to marketing: layer, translator",
                "boxoffice to finance: layer, translator",
                "models reached: 2, translators: 2",
            ],
            "after": [
                "Before the step, the separate-ways edge carried nothing, so membership and "
                "its layer stayed still. The kernel buys shared concepts with shared changes.",
            ],
        },
        "quiz_title": "Transformations and their steps",
        "quiz": [
            {"q": "In the exercise (box office and membership merged into `tickets`), what "
                  "does a change to `tickets` reach?",
             "a": ["1 model and 1 translator, as before the merger",
                   "2 models and 2 translators, as after the first step",
                   "1 model and 2 translators",
                   "0 models and 1 translator"],
             "c": 0,
             "why": "Marketing conforms to `tickets`, so its model changes: 1. Finance "
                    "translates through its layer: 1 translator. Membership's layer to "
                    "marketing is gone with membership. The reach is back to where it was "
                    "before the merger, but now with one model where there were two, and "
                    "the duplication and one translation removed."},
            {"q": "In Evans's plan for merging Separate Ways into a Shared Kernel, which "
                  "subdomain should the teams start with?",
             "a": ["The Core Domain, since it matters most",
                   "Whatever the larger team owns",
                   "Something small, duplicated in both contexts, not in the Core Domain, "
                   "ideally already being translated",
                   "The subdomain with the most specialised jargon"],
             "c": 2,
             "why": "The first merger sets up the process, so it should be simple and "
                    "relatively generic; one already translated starts from a proven "
                    "translation. The core comes later, once the process has firmed up and "
                    "the teams are confident, and subdomains tailored to different jargons "
                    "are deferred until a deep model can replace both."},
            {"q": "In Phasing Out a Legacy System, which functions does Evans say to migrate "
                  "first, all else being equal?",
             "a": ["The most-used functions",
                   "Those the legacy team wants to drop",
                   "The newest functions",
                   "Those that lead to smaller Anticorruption Layers"],
             "c": 3,
             "why": "The layer shrinks and swells as functions move, and other things equal "
                    "you should move first what makes it smaller, though he grants other "
                    "factors are likely to dominate."},
            {"q": "Why does Evans warn against breaking up a large context because its model "
                  "seems too complex?",
             "a": ["Because splitting contexts is technically impossible",
                   "Because the fragmentation loses integration, and distillation and "
                   "large-scale structure may make the model tractable instead",
                   "Because smaller contexts always need a Shared Kernel",
                   "Because the Context Map cannot show more than one context"],
             "c": 1,
             "why": "Contexts solve logical inconsistency, not complexity. If a large context "
                    "meets real integration needs and is feasible apart from its complexity, "
                    "he points to the next two chapters before that sacrifice; breaking up "
                    "contexts is, he says, the easy transformation, not an impossible one."},
        ],
        "mistakes": [
            ("Merging two contexts in one step",
             "A single sweeping merge looks quicker than a series of small ones. Evans says "
             "these transformations are usually too big for one refactoring or one iteration, "
             "and even a full merger should pass through a Shared Kernel grown subdomain by "
             "subdomain, with its process and tests set up first. On the lesson's "
             "illustration the first step alone doubles what a box office change reaches, "
             "which is the coordination each step adds."),
            ("Starting the kernel with the Core Domain",
             "The core matters most, so it seems the place to begin. The first merger "
             "establishes the process, and Evans picks something simple, generic and "
             "preferably already translated; the core is merged later, once the people and "
             "processes are ready."),
            ("Expecting the Anticorruption Layer to shrink steadily as legacy goes",
             "It alternately shrinks and swells as functions move, Evans says, and some "
             "awkward translations may have to be tolerated on the way; moving first what "
             "makes it smaller is a preference, not a guarantee."),
        ],
        "standard": (
            "Finish when you can plan a transformation and count its effect.",
            "Given a map and a transformation, list its first steps in Evans's order and "
            "state what one change reaches before and after."
        ),
        "note": (
            "The lab compares one change on two maps. It does not count the duplication or "
            "translation a merger removes, the training and circulation of people Evans "
            "puts first, or the weeks a step takes, and it cannot say when a transformation "
            "is worth beginning."
        ),
    },
]
