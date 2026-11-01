"""Maintaining Model Integrity, lessons 1-5 -- Chapter 14, to Anticorruption Layer.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), Chapter 14, Maintaining Model Integrity: the opening,
Bounded Context, Continuous Integration, Context Map, Relationships Between
Bounded Contexts, Shared Kernel, Customer/Supplier Development Teams,
Conformist and Anticorruption Layer. Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter, section and pattern. Every
quotation is copied from that copy and checked with quotes.py. The glossaries,
maps and code are written for these lessons (a theatre, a school, a clinic, a
library, a bakery); none of the book's examples, diagrams or listings is
reproduced. The design is docs/domain-driven-design/PLAN.md, section C,
Course 7.
"""


def _lines(text):
    """A constant as a code block's list of lines."""
    return text.split("\n")


def _rows(text):
    """Records 'a, b, c; d, e, f' as one line per record, for a code block."""
    return [r.strip() + ";" for r in text.split(";")]


MODULE = "Chapter 14 · Maintaining Model Integrity"


# ---------------------------------------------------------------- glossaries

# 7.1 Bounded Context: a theatre's Box Office and its Venue Operations team.
TWO_TEAMS = (
    "boxoffice, seat, sellable-place; "
    "boxoffice, performance, dated-showing; "
    "boxoffice, patron, ticket-buyer; "
    "boxoffice, hold, unsold-reserve; "
    "boxoffice, order, ticket-sale; "
    "venue, seat, physical-chair; "
    "venue, performance, dated-showing; "
    "venue, guest, ticket-buyer; "
    "venue, hold, out-of-service; "
    "venue, usher-shift, staff-rota"
)

RENAMED = (
    "boxoffice, seat, sellable-place; "
    "boxoffice, performance, dated-showing; "
    "boxoffice, patron, ticket-buyer; "
    "boxoffice, hold, unsold-reserve; "
    "boxoffice, order, ticket-sale; "
    "venue, chair, physical-chair; "
    "venue, performance, dated-showing; "
    "venue, guest, ticket-buyer; "
    "venue, block, out-of-service; "
    "venue, usher-shift, staff-rota"
)

SCHOOL = (
    "timetable, period, teaching-slot; "
    "timetable, room, teaching-space; "
    "timetable, set, student-group; "
    "timetable, teacher, staff-member; "
    "exams, period, exam-window; "
    "exams, room, teaching-space; "
    "exams, set, paper-batch; "
    "exams, staff, staff-member; "
    "exams, group, student-group; "
    "exams, sitting, exam-session"
)

# 7.2 Continuous Integration: two halves of one Box Office team.
DRIFTED = (
    "web, patron, ticket-buyer; "
    "web, basket, unpaid-order; "
    "web, concession, discounted-price; "
    "web, order, ticket-sale; "
    "web, performance, dated-showing; "
    "till, customer, ticket-buyer; "
    "till, concession, snack-sale; "
    "till, order, ticket-sale; "
    "till, performance, dated-showing; "
    "till, reduced-rate, discounted-price"
)

MERGED = (
    "web, patron, ticket-buyer; "
    "web, basket, unpaid-order; "
    "web, concession, discounted-price; "
    "web, order, ticket-sale; "
    "web, performance, dated-showing; "
    "till, patron, ticket-buyer; "
    "till, kiosk-sale, snack-sale; "
    "till, order, ticket-sale; "
    "till, performance, dated-showing; "
    "till, concession, discounted-price"
)

CLINIC = (
    "booking, appointment, booked-slot; "
    "booking, patient, registered-person; "
    "booking, clinician, care-provider; "
    "booking, referral, incoming-request; "
    "booking, slot, free-time; "
    "records, appointment, booked-slot; "
    "records, patient, registered-person; "
    "records, provider, care-provider; "
    "records, referral, outgoing-letter; "
    "records, episode, course-of-care"
)


# ---------------------------------------------------------------- maps

# 7.3 Context Map: the theatre's seven contexts.
THEATRE_CONTEXTS = "programming venue boxoffice marketing finance payments resellers"
THEATRE_RELS = (
    "programming, venue, shared-kernel; "
    "programming, boxoffice, customer-supplier; "
    "boxoffice, marketing, conformist; "
    "boxoffice, finance, acl; "
    "payments, boxoffice, acl; "
    "boxoffice, resellers, ohs"
)

LIBRARY_CONTEXTS = "catalogue lending members events supplier-feed fines-legacy"
LIBRARY_RELS = (
    "catalogue, lending, customer-supplier; "
    "members, lending, shared-kernel; "
    "lending, events, conformist; "
    "supplier-feed, catalogue, acl; "
    "fines-legacy, lending, acl"
)

# 7.4 Shared Kernel and Customer/Supplier.
KERNEL_CONTEXTS = "programming venue boxoffice cafe"
KERNEL_RELS = (
    "programming, venue, shared-kernel; "
    "programming, boxoffice, customer-supplier; "
    "boxoffice, cafe, customer-supplier"
)
KERNEL_RELS_WIDER = (
    "programming, venue, shared-kernel; "
    "programming, boxoffice, shared-kernel; "
    "boxoffice, cafe, customer-supplier"
)

# 7.5 Conformist and Anticorruption Layer.
LEGACY_CONTEXTS = "members-legacy boxoffice marketing finance"
LEGACY_CONFORM = (
    "members-legacy, boxoffice, conformist; "
    "boxoffice, marketing, conformist; "
    "boxoffice, finance, customer-supplier"
)
LEGACY_ACL = (
    "members-legacy, boxoffice, acl; "
    "boxoffice, marketing, conformist; "
    "boxoffice, finance, customer-supplier"
)

BAKERY_CONTEXTS = "till-vendor orders baking-plan accounts"
BAKERY_CONFORM = (
    "till-vendor, orders, conformist; "
    "orders, baking-plan, conformist; "
    "orders, accounts, acl"
)

ACL_JAVA = """// In the Box Office context: the service its own model asks for.
interface MembershipCheck {
    Optional<Discount> discountFor(PatronId patron);
}

// The adapter answers it by asking the old system's facade.
class LegacyMembershipAdapter implements MembershipCheck {
    private final LegacyMembersFacade facade;      // the old model's terms
    private final MembershipTranslator translator; // holds no state

    LegacyMembershipAdapter(LegacyMembersFacade f, MembershipTranslator t) {
        this.facade = f;
        this.translator = t;
    }

    public Optional<Discount> discountFor(PatronId patron) {
        LegacyMemberRow row = facade.findByCardNo(translator.cardNo(patron));
        return translator.discount(row);
    }
}"""


_COGNATES_INTRO = (
    "Each record is a context, a term used there, and the concept the term stands "
    "for, written as a short name. The lab compares the concept names exactly; it "
    "does not read definitions, so two names for one concept are two concepts to it "
    "until you write them alike. The glossaries are the lesson's."
)

_MAP_INTRO = (
    "Each relationship is an upstream context, a downstream context and one of the "
    "book's kinds. The lab follows a change in one context's model along the edges "
    "whose kind carries it: a Shared Kernel both ways, Conformist and "
    "Customer/Supplier downstream. An Anticorruption Layer or an Open Host Service "
    "stops it at a translator. The map is the lesson's."
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 14, opening (PDF pp. 205-206 of the operator's copy); Bounded
    # Context (pp. 207-209), with its sidebar on Modules (p. 208) and its
    # example (p. 209); Recognizing Splinters Within a Bounded Context (p. 210).
    # Quote: PDF p. 208 of the operator's copy, 27 words, quotes.py OK.
    # Lesson total: 27 words.
    {
        "slug": "bounded-context",
        "title": "Bounded Context",
        "module": MODULE,
        "one_line": "Say where a model applies, keep it consistent inside that line, and expect translation across it.",
        "summary": (
            "Chapter 14 opens by giving up on one model for a whole enterprise and asks "
            "instead where each model applies. Read Evans's case for drawing that line "
            "explicitly, and his two symptoms of models mixed without one, duplicate "
            "concepts and false cognates; then count both in two teams' glossaries."
        ),
        "key": [
            "a model means something only in a context",
            "one enterprise-wide model rarely pays",
            "draw the line: team, code, schema",
            "consistent inside, translated across",
            "duplicate concept: one idea, two names",
            "false cognate: one name, two ideas",
        ],
        "key_label": "Bounded Context in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's premise, the other "
            "two are the symptoms of its section on splinters."
        ),
        "concepts": [
            ("Unification",
             "Evans's word for a model's internal consistency: every term means one thing "
             "and no two rules contradict. A model without it, he says, means nothing."),
            ("Bounded Context",
             "The explicit limit within which one model applies and is kept unified, "
             "drawn in terms of a team, the parts of the application that use the model, "
             "and the code and schema it lives in."),
            ("Duplicate concept and false cognate",
             "A duplicate concept is one idea held by two model elements under two names. "
             "A false cognate is one name that two people use for two different ideas, "
             "each believing the other means the same."),
        ],
        "read_title": "The chapter's premise first, then the pattern, then the count",
        "read_intro": (
            "Read the opening of Chapter 14, the Bounded Context pattern and Recognizing "
            "Splinters in your own copy first. The lesson reads the opening as an argument "
            "and the pattern as a tool, and then counts two teams' words."
        ),
        "body": [
            ("p", "&ldquo;The model context is whatever set of conditions must apply in "
                  "order to be able to say that the terms in a model have a specific "
                  "meaning.&rdquo; That is Evans's definition, inside the Bounded Context "
                  "pattern that begins Chapter 14, Maintaining Model Integrity, the first "
                  "chapter of Part IV, Strategic Design. This lesson reads the chapter's "
                  "opening, the pattern and its section Recognizing Splinters Within a "
                  "Bounded Context."),
            ("p", "The chapter starts with a story. Two teams building parts of one new "
                  "system each needed a class for a charge. The second found the first "
                  "team's class, added the field it lacked, renamed its own idea to fit an "
                  "attribute that was already there, and moved on. Days later the first "
                  "team's module was showing records nobody had entered and crashing in a "
                  "monthly tax report: one team had meant a charge to a customer and the "
                  "other a payment to a supplier. Their repair was two classes with two "
                  "names, after which, Evans notes, they carried on exactly as before."),
            ("p", "From the story he draws the chapter's premise. The most basic thing a "
                  "model needs is internal consistency, which he calls unification. One "
                  "unified model across a whole enterprise would be ideal, and on a large "
                  "system it costs more than it is worth. He lists what goes wrong when a "
                  "project tries anyway: too many legacy replacements attempted at once; "
                  "coordination that outgrows the team; specialised applications forced "
                  "onto a model that does not serve them; and a model swollen with options "
                  "to satisfy everyone. Models also part company for political and "
                  "organisational reasons that no technical decision removes. So the "
                  "question is not how to have one model, but how to choose on purpose "
                  "which parts stay unified and how the rest relate to them."),
            ("p", "Bounded Context is the first answer, and it reads as a tool. Every large "
                  "project has several models in play, and when code built on two of them "
                  "is combined without anyone noticing, the software becomes unreliable and "
                  "the team's talk confused; the trouble, Evans insists, begins in how the "
                  "teams are organised, not in the code. So: state where a model applies, "
                  "and draw that line in three sorts of terms together, the team that owns "
                  "it, the parts of the application that use it, and the code base and "
                  "database schema that embody it. Within the line, hold the model strictly "
                  "consistent; beyond it, do not be pulled about by other models' concerns. "
                  "Integration across the line will need translation, and once the line is "
                  "drawn that translation can be designed rather than discovered."),
            ("p", "A sidebar separates the pattern from Chapter 5's Modules. Two models' "
                  "objects nearly always sit in different Modules, and the separate name "
                  "spaces help, but Modules also divide up a single model. Inside one "
                  "context their separate name spaces can even hide the fragmentation the "
                  "pattern exists to catch. Evans's example then draws the line for a "
                  "booking application at a shipping company, deciding team by team and "
                  "artefact by artefact what is inside it; the most useful result, he says, "
                  "is seeing that a neighbouring team has been sharing objects casually "
                  "with no agreed relationship at all."),
            ("p", "Recognizing Splinters names the two ways a mixed model goes wrong. A "
                  "duplicate concept is one idea held by two elements: each change must be "
                  "made twice, in practice is not, and the copies drift into different rules "
                  "and data. A false cognate is one term two people use for different "
                  "things, each sure the other means the same. Evans calls false cognates "
                  "less common and more damaging, and the opening story's charge is his "
                  "example. The early warning of both, he says, is confused language, "
                  "before any interface fails to fit."),
            ("p", "Now the count. The lab reads glossaries: each record is a context, a "
                  "term used there, and the concept it stands for. The lesson's two "
                  "contexts are a theatre's Box Office, which sells seats for "
                  "performances, and its Venue Operations team, which runs the building. "
                  "On the preset <code>two-teams</code> the lab counts 2 contexts and 7 "
                  "distinct terms, 3 of them used in both. Of those 3, 2 are false "
                  "cognates, `seat` and `hold`, and 1 is safe to share, `performance`, "
                  "used alike in both. It also finds 1 duplicate concept: the person who "
                  "buys a ticket is a `patron` to the box office and a `guest` to the "
                  "venue."),
            ("code", _rows(TWO_TEAMS)),
            ("p", "Read the counts as Evans reads his symptoms. A box office seat is a place "
                  "in one performance that can be sold; a venue seat is a chair with a row "
                  "and a number, which can break. A box office hold keeps seats back from "
                  "sale; a venue hold takes a broken chair out of use. If the two teams "
                  "shared one `Seat` class, each would add what it needed, and one evening "
                  "the box office would sell a chair the venue had taken out: the opening "
                  "story again, with seats. The duplicate is milder. Two names for one "
                  "person is a translation, and across a boundary a translation is "
                  "allowed."),
            ("p", "The preset <code>renamed</code> does what the story's teams did: the "
                  "venue now says `chair` and `block`. The lab finds 0 false cognates, 1 "
                  "shared term and 1 safe to share, and the duplicate is still there, 1, "
                  "since nothing about a boundary requires two contexts to name a patron "
                  "alike. What renaming did not do is Evans's complaint about the story's "
                  "ending: no line was drawn and no process set up to catch the next "
                  "divergence. The lab counts words; it cannot tell whether anyone has "
                  "written down where the Box Office model stops."),
            ("h3", "Exercise"),
            ("code", _rows(SCHOOL)),
            ("p", "A school's timetabling team and its exams office, each with its own "
                  "glossary. Find the terms both use, say which of them are false cognates "
                  "and which are safe to share, and list the duplicate concepts with their "
                  "two names. Then paste the records into the lab to check your count."),
            ("p", "A boundary is drawn once; keeping the model inside it whole is daily "
                  "work. The next lesson, Continuous Integration, reads Evans's process for "
                  "that."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "cognates",
            "preset": "two-teams",
            "presets": [
                {"id": "two-teams",
                 "label": "Box Office and Venue Operations, each with its own words",
                 "contexts": TWO_TEAMS,
                 "expect": {"dlnContexts": "2: boxoffice, venue", "dlnTerms": "7", "dlnShared": "3: seat, performance, hold", "dlnFalse": "2: seat (boxoffice: sellable-place, venue: physical-chair); hold (boxoffice: unsold-reserve, venue: out-of-service)", "dlnDuplicate": "1: ticket-buyer: patron (boxoffice), guest (venue)", "dlnSafe": "1: performance"}},
                {"id": "renamed",
                 "label": "The venue renames seat and hold",
                 "contexts": RENAMED,
                 "expect": {"dlnContexts": "2: boxoffice, venue", "dlnTerms": "9", "dlnShared": "1: performance", "dlnFalse": "0: none", "dlnDuplicate": "1: ticket-buyer: patron (boxoffice), guest (venue)", "dlnSafe": "1: performance"}},
            ],
            "panel_title": "Two teams' glossaries, side by side",
            "panel_intro": _COGNATES_INTRO,
        }),
        "steps_title": "Finding the splinters between two glossaries",
        "steps_intro": "Four steps, the last of them on a project of your own.",
        "steps": [
            ("Write each team's glossary",
             "For each context, list the terms its people use and give each the concept it "
             "stands for in a short name, as the lab's records do."),
            ("Compare the shared terms",
             "For each term that appears in more than one context, compare the concepts. "
             "The same concept everywhere is safe to share; any difference is a false "
             "cognate."),
            ("Find the concepts with two names",
             "For each concept, list the terms that name it. More than one is a duplicate "
             "concept: inside one context a splinter, across a boundary a translation."),
            ("Do it on your own project",
             "Take two teams or two services you know that share a word such as account, "
             "order or user. Write a few records for each, count the false cognates, and "
             "say in one sentence where the boundary between them lies."),
        ],
        "worked": {
            "title": "Two teams, seven terms",
            "intro": [
                "Count the preset <code>two-teams</code> by hand.",
            ],
            "lines": [
                "terms: seat, performance, patron, hold,",
                "order, guest, usher-shift: 7",
                "in both contexts: seat, performance, hold",
                "seat: sellable-place, physical-chair",
                "hold: unsold-reserve, out-of-service",
                "performance: dated-showing in both",
                "ticket-buyer: patron and guest",
            ],
            "after": [
                "Two false cognates, one safe term and one duplicate concept. Which of them "
                "matters is a reading of the domain: the false cognates would break a shared "
                "class, while the duplicate only asks for a translation at the boundary.",
            ],
        },
        "quiz_title": "Contexts, cognates and Evans's claims",
        "quiz": [
            {"q": "In the exercise (the school's timetable and exams glossaries), how many "
                  "false cognates and how many duplicate concepts are there?",
             "a": ["1 false cognate, 2 duplicate concepts",
                   "2 false cognates, 1 duplicate concept",
                   "2 false cognates, 2 duplicate concepts",
                   "3 false cognates, 2 duplicate concepts"],
             "c": 2,
             "why": "Three terms appear in both: `period`, `room` and `set`. `period` is a "
                    "teaching-slot in one and an exam-window in the other, and `set` a "
                    "student-group against a paper-batch: 2 false cognates. `room` means "
                    "teaching-space in both, so it is safe to share, not a third. The "
                    "duplicates are staff-member (`teacher` and `staff`) and student-group "
                    "(`set` in the timetable, `group` in exams): 2. The second is easy to "
                    "miss because one of its names is also a false cognate."},
            {"q": "Which of the two symptoms in Recognizing Splinters does Evans call less "
                  "common but more harmful?",
             "a": ["Duplicate concepts",
                   "Unexpected behaviour at run time",
                   "Interfaces that do not match",
                   "False cognates"],
             "c": 3,
             "why": "False cognates: two people use one term for two things and each "
                    "believes they agree, as the two teams did with the charge. Interfaces "
                    "that do not match and unexpected behaviour are signs he lists, the "
                    "first the most obvious, but the two categories of problem are duplicate "
                    "concepts and false cognates."},
            {"q": "According to the sidebar in the Bounded Context pattern, why are Modules "
                  "not enough to separate two models?",
             "a": ["Modules cannot give two models separate name spaces",
                   "Modules also divide one model, and their name spaces can hide a splinter",
                   "Modules belong to the infrastructure layer, not the domain",
                   "Evans recommends one Module for each Bounded Context"],
             "c": 1,
             "why": "Modules do give separate name spaces, which two contexts need, but they "
                    "also organise the elements of a single model, so they say nothing about "
                    "an intention to separate models; inside one context their name spaces "
                    "can make accidental fragmentation harder to see."},
            {"q": "In the pattern, which three things does Evans name as the terms in which "
                  "to set a context's boundary?",
             "a": ["Who owns the model, which parts of the application use it, and the "
                   "code and schema it lives in",
                   "Layers, Modules and Aggregates",
                   "Subdomains, user communities and deployment units",
                   "The Ubiquitous Language, the code and the tests"],
             "c": 0,
             "why": "The pattern names three: how the teams are organised, which parts of "
                    "the application use the model, and the forms it takes in code bases "
                    "and database schemas. Layers, Modules and Aggregates organise a model "
                    "inside a context; they do not bound one."},
        ],
        "mistakes": [
            ("Setting out to give the whole enterprise one model",
             "It sounds like the end of all translation. Evans judges total unification of a "
             "large system neither feasible nor cost-effective, and lists the risks of "
             "attempting it: too many replacements at once, coordination the project cannot "
             "carry, applications forced onto a model that does not fit them, and a model "
             "full of options. His goal is a chosen set of unified models with known "
             "relationships, which on the lesson's illustration means two glossaries with "
             "their false cognates found, not one glossary forced on both teams."),
            ("Taking a Bounded Context for a Module or a package",
             "The pattern's sidebar keeps them apart. Separate models usually do sit in "
             "separate Modules, but a Module also divides one model and says nothing about "
             "an intention to keep models apart; a context is drawn around teams, usage and "
             "schemas as well as code."),
            ("Thinking that renaming a class repairs a splinter",
             "Renaming, as the story's teams did with their two charges, removes one false "
             "cognate. It draws no boundary and sets up no process, and the next divergence "
             "arrives the same way. On the preset <code>renamed</code> the lab shows the "
             "words are fixed; it cannot show that anything else is."),
        ],
        "standard": (
            "Finish when you can find the splinters between two glossaries.",
            "Given two contexts' glossaries, name the shared terms, the false cognates and "
            "the duplicate concepts, and say which would break a shared class."
        ),
        "note": (
            "The lab compares concept names as you write them, so it finds the splinters "
            "your records already state. Deciding that two definitions are one concept, "
            "or that a term in your code has drifted, is the knowledge crunching the "
            "glossary comes from, and where a boundary should lie is a judgement about "
            "teams and integration that no count of words settles."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Continuous Integration (PDF pp. 211-212 of the operator's copy).
    # Quote: PDF p. 211 of the operator's copy, 23 words, quotes.py OK.
    # Lesson total: 23 words.
    {
        "slug": "continuous-integration",
        "title": "Continuous Integration",
        "module": MODULE,
        "one_line": "Inside one context, merge the code and the language often enough that a splinter is caught while it is small.",
        "summary": (
            "A Bounded Context does not stay unified by being drawn. Read Evans's account "
            "of how a model fragments among the people who share it, and his two levels "
            "of Continuous Integration, of concepts and of code; then watch two halves of "
            "one team drift apart and count what a merge must settle."
        ),
        "key": [
            "a shared model tends to fragment",
            "three or four people are enough",
            "integrate the concepts by talking",
            "integrate the code: build, test, merge",
            "a short life for unmerged changes",
            "needed only inside one context",
        ],
        "key_label": "Continuous Integration in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the section's problem, the second "
            "and third its two levels."
        ),
        "concepts": [
            ("Fragmentation",
             "The tendency of a model shared by several people to break into inconsistent "
             "pieces: one changes an object for a purpose its author did not intend, another "
             "builds a near copy of a concept that already exists."),
            ("Integration of concepts",
             "Keeping a shared understanding of the changing model by constant talk, above "
             "all by exercising the Ubiquitous Language in every discussion of the model and "
             "the application."),
            ("Integration of the implementation",
             "A merge, build and test process that is reproducible, runs automated tests, "
             "and sets a small upper limit on how long a change may stay unmerged."),
        ],
        "read_title": "The section's problem first, then the process, then the count",
        "read_intro": (
            "Read Continuous Integration in Chapter 14 in your own copy first. It is a short "
            "pattern; the lesson reads it as a tool and then counts what a team's two halves "
            "have let drift."
        ),
        "body": [
            ("p", "Continuous Integration, Evans writes, means that &ldquo;all work within "
                  "the context is being merged and made consistent frequently enough that "
                  "when splinters happen they are caught and corrected quickly.&rdquo; The "
                  "pattern follows Bounded Context in Chapter 14, and this lesson reads it "
                  "whole."),
            ("p", "Its problem is the one the last lesson left. Once a context is drawn, the "
                  "people working inside it pull its model apart, and the larger the team "
                  "the worse it gets; Evans says three or four people can already run into "
                  "serious trouble. Cutting the system into ever smaller contexts is no "
                  "cure, because past a point it throws away integration worth having."),
            ("p", "He describes three ways a careful developer splinters a model. One does "
                  "not fully grasp what a colleague's object was for, and changes it so it "
                  "no longer serves that purpose. One does not know a concept already exists "
                  "elsewhere in the model, and writes an inexact second version. One knows "
                  "it exists but is afraid that touching it will break something, and "
                  "writes the second version anyway. The last is the one a safety net "
                  "addresses: a developer who can run the tests is less afraid to change "
                  "the original."),
            ("p", "This, he says, is where Extreme Programming comes into its own, since so "
                  "many of its practices aim at keeping a design coherent while many people "
                  "change it; but some process of Continuous Integration is essential with "
                  "or without it. The process works at two levels, as everything in "
                  "domain-driven design does. Concepts are integrated by constant talk, and "
                  "most of all by hammering out the Ubiquitous Language. The implementation "
                  "is integrated by a systematic merge, build and test, which in effective "
                  "processes is reproducible step by step, runs automated test suites, and "
                  "puts a fairly small limit on how long a change can stay unmerged; most "
                  "agile projects, he notes, merge at least daily."),
            ("p", "The two levels help each other. In a Model-Driven Design the shared "
                  "concepts make the code easier to merge, and the merged, tested code proves "
                  "the model consistent and exposes its splinters early. The pattern, then: "
                  "merge all the code and the other artefacts often, with automated tests "
                  "that flag fragmentation quickly, and exercise the language relentlessly "
                  "as the concepts change in different people's heads. And keep the job no "
                  "bigger than it must be. Continuous Integration is needed only inside one "
                  "context, for any context larger than a two-person task; relations with "
                  "neighbouring contexts can move at a slower pace."),
            ("p", "Now the count. The lab is the last lesson's, but the two contexts in its "
                  "records are the two halves of one team inside one Bounded Context: the "
                  "Box Office's web shop pair and its counter till pair, who stopped talking "
                  "for a month. Inside one context, every term both halves use should be "
                  "safe to share, and no concept should have two names. On the preset "
                  "<code>drifted</code> the lab counts 7 terms, 3 of them used by both "
                  "halves; 1 is a false cognate, `concession`, and 2 are safe to share. It "
                  "finds 2 duplicate concepts: the ticket buyer is a `patron` on the web and "
                  "a `customer` at the till, and the reduced price is a `concession` on the "
                  "web and a `reduced-rate` at the till."),
            ("code", _rows(DRIFTED)),
            ("p", "`concession` is the instructive one. In a theatre it means a reduced "
                  "ticket price for students and pensioners, and it also means the counter "
                  "that sells drinks and ice cream, and each half of the team has taken one "
                  "meaning. Across a boundary that would be a translation to design; inside "
                  "one context it is a splinter, and the first sign of it, as Evans says, is "
                  "two people talking past each other, long before a report adds snacks to "
                  "discounted tickets."),
            ("p", "The preset <code>merged</code> is the glossary after one afternoon of "
                  "hammering out the language: both halves say `patron` and `concession` for "
                  "the reduced price, and the counter's sales become `kiosk-sale`. The lab "
                  "counts 6 terms, 4 shared and all 4 safe to share, 0 false cognates and 0 "
                  "duplicate concepts. That is the target inside one context. Notice who "
                  "gave way: the till half gave up `customer`, `reduced-rate` and its "
                  "snack sense of `concession`, now `kiosk-sale`; the web half nothing. Who gives way is a conversation, "
                  "not a count."),
            ("h3", "Exercise"),
            ("code", _rows(CLINIC)),
            ("p", "A clinic's booking pair and its records pair, both inside one Bounded "
                  "Context, after a month apart. Find what the next merge must settle: the "
                  "false cognates, the duplicate concepts, and the terms already safe to "
                  "share. Then propose one renaming for each problem and check the result "
                  "in the lab."),
            ("p", "Inside a context the work is merging; between contexts it is mapping. The "
                  "next lesson, Context Map, draws all the contexts of a project and the "
                  "relationships between them."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "cognates",
            "preset": "drifted",
            "presets": [
                {"id": "drifted",
                 "label": "Two halves of the Box Office team after a month apart",
                 "contexts": DRIFTED,
                 "expect": {"dlnContexts": "2: web, till", "dlnTerms": "7", "dlnShared": "3: concession, order, performance", "dlnFalse": "1: concession (web: discounted-price, till: snack-sale)", "dlnDuplicate": "2: ticket-buyer: patron (web), customer (till); discounted-price: concession (web), reduced-rate (till)", "dlnSafe": "2: order, performance"}},
                {"id": "merged",
                 "label": "The same glossary after the language is hammered out",
                 "contexts": MERGED,
                 "expect": {"dlnContexts": "2: web, till", "dlnTerms": "6", "dlnShared": "4: patron, concession, order, performance", "dlnFalse": "0: none", "dlnDuplicate": "0: none", "dlnSafe": "4: patron, concession, order, performance"}},
            ],
            "panel_title": "Two halves of one context, drifting",
            "panel_intro": (
                "Each record is a half of one team, a term it uses, and the concept the term "
                "stands for. Inside one Bounded Context the target is no false cognates and "
                "no duplicate concepts; the lab counts how far the halves are from it. The "
                "glossaries are the lesson's."
            ),
        }),
        "steps_title": "Checking one context for splinters",
        "steps_intro": "Four steps, the last of them on a team of your own.",
        "steps": [
            ("Collect each half's words",
             "Write the terms each part of the team uses in code and in talk, with the "
             "concept each stands for."),
            ("Mark every disagreement",
             "A shared term with two concepts is a false cognate; a concept with two terms is "
             "a duplicate. Inside one context, both are splinters."),
            ("Settle each one in the language",
             "For each splinter, agree one term for one concept and rename the other use, "
             "in the code as well as the talk, and re-count."),
            ("Do it on your own team",
             "Take the last week's merge requests in a code base you share. Note any class or "
             "field that two people named differently for one idea, or alike for two, and "
             "count them."),
        ],
        "worked": {
            "title": "The halves that drifted",
            "intro": [
                "Count the preset <code>drifted</code> by hand.",
            ],
            "lines": [
                "in both halves: concession, order, performance",
                "concession: discounted-price, snack-sale",
                "order, performance: alike, safe",
                "ticket-buyer: patron and customer",
                "discounted-price: concession, reduced-rate",
                "1 false cognate, 2 duplicates",
            ],
            "after": [
                "Three splinters for one merge to settle. The lab counts them; it cannot say "
                "which half's word should win, which is the conversation Evans means by "
                "exercising the language.",
            ],
        },
        "quiz_title": "Integration inside a context",
        "quiz": [
            {"q": "In the exercise (the clinic's booking and records pairs), what must the "
                  "next merge settle?",
             "a": ["1 false cognate and 1 duplicate concept; 2 terms are already safe",
                   "2 false cognates and 1 duplicate concept; 1 term is safe",
                   "1 false cognate and 2 duplicate concepts; 2 terms are safe",
                   "Nothing: the halves are in one context, so their terms agree"],
             "c": 0,
             "why": "Three terms are used by both: `appointment`, `patient` and `referral`. "
                    "`referral` is an incoming-request to booking and an outgoing-letter to "
                    "records, the 1 false cognate; the other two mean the same in both and "
                    "are safe. The 1 duplicate is care-provider, named `clinician` and "
                    "`provider`. Being in one context is what makes these splinters, not "
                    "what prevents them."},
            {"q": "At which two levels does Evans say Continuous Integration operates?",
             "a": ["Within a team and between teams",
                   "Daily builds and weekly kernel merges",
                   "The integration of model concepts and the integration of the "
                   "implementation",
                   "Unit tests and acceptance tests"],
             "c": 2,
             "why": "Concepts, by constant communication and the Ubiquitous Language; and "
                    "the implementation, by a systematic merge, build and test. Weekly "
                    "merges belong to the Shared Kernel, and between teams is the subject "
                    "of the Context Map, not of this pattern."},
            {"q": "Where, according to the pattern, is Continuous Integration essential?",
             "a": ["Across every context on the project, at the same pace",
                   "Only within a Bounded Context",
                   "Only on projects using Extreme Programming",
                   "Only where a Shared Kernel exists"],
             "c": 1,
             "why": "Evans limits it to one context, for any context bigger than a "
                    "two-person task; design issues with neighbouring contexts, translation "
                    "included, need not move at that pace. He says some such process is "
                    "essential whether or not XP is used."},
            {"q": "Which of these is not among the characteristics Evans gives for "
                  "effective integration of the implementation?",
             "a": ["A step-by-step, reproducible merge and build",
                   "Automated test suites",
                   "A fairly short limit on how long a change may stay unmerged",
                   "A single developer who owns each class"],
             "c": 3,
             "why": "The three he lists are a reproducible merge and build, automated tests, "
                    "and a reasonably small limit on how long a change stays unmerged. "
                    "Single ownership of classes is not among them, and the fear of touching "
                    "another person's code is one of the ways he says models splinter."},
        ],
        "mistakes": [
            ("Thinking a team inside one context stays consistent without effort",
             "Being in one Bounded Context is a decision about what should be consistent, "
             "not a guarantee that it is. Evans says even three or four people can fragment "
             "a model, by changing an object for a purpose its author did not intend or by "
             "duplicating a concept they did not know or dared not touch. On the lesson's "
             "illustration two halves of one team produce three splinters in a month."),
            ("Treating Continuous Integration as a build server alone",
             "Merging and testing the code is one level. The other is conceptual: constant "
             "exercise of the Ubiquitous Language, which Evans notes is seldom written into "
             "the process. A green build does not show that two halves of a team mean "
             "different things by `concession`; a conversation does."),
            ("Running Continuous Integration across every context",
             "The pattern applies inside a context. Relations with neighbouring contexts, "
             "translation included, need not move at the same pace, and trying to make "
             "them do so makes the job bigger than it must be."),
        ],
        "standard": (
            "Finish when you can say what a merge inside one context must settle.",
            "Given two halves of a team's glossary, list the false cognates and duplicate "
            "concepts a merge must settle, and propose a renaming that clears them."
        ),
        "note": (
            "The lab sees only the words you record. It cannot see a class changed for a "
            "purpose its author did not intend, or a test that would have caught it, and "
            "it cannot say how often a team should merge; Evans leaves the frequency to the "
            "pace of change."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Context Map (PDF pp. 213-219 of the operator's copy), with its example
    # (pp. 214-218), Testing at the Context Boundaries (p. 218) and Organizing
    # and Documenting Context Maps (pp. 218-219).
    # Quote: PDF p. 213 of the operator's copy, 8 words, quotes.py OK.
    # Lesson total: 8 words.
    {
        "slug": "context-map",
        "title": "Context Map",
        "module": MODULE,
        "one_line": "Name every model on the project, say how each touches the others, and describe things as they are.",
        "summary": (
            "One Bounded Context gives no view of the others. Read Evans's Context Map: "
            "every model named, every point of contact described, the terrain mapped as it "
            "is, and tests at the boundaries; then follow one change across a theatre's "
            "seven contexts and count what it reaches."
        ),
        "key": [
            "name every context, and use the names",
            "describe each point of contact",
            "map the terrain as it is today",
            "change the map after the reality",
            "test hardest at the boundaries",
            "a translator stops what a model passes on",
        ],
        "key_label": "Context Map in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the pattern's, the second the "
            "chapter's vocabulary for direction, the third the lab's."
        ),
        "concepts": [
            ("Context Map",
             "A shared description of every model in play on a project, each in its named "
             "Bounded Context, with the points of contact between them and the nature of "
             "each. Its form is free: a diagram, a list, or talk, if everyone shares it."),
            ("Upstream and downstream",
             "The direction of dependence between two contexts. The downstream one depends on "
             "the upstream one's model or output; the upstream one does not depend back."),
            ("What a change reaches",
             "The contexts whose models must change when one context's model changes, "
             "followed along each relationship by the rule its kind implies, and the "
             "translators that absorb the change instead."),
        ],
        "read_title": "The pattern first, then its example, then the count",
        "read_intro": (
            "Read Context Map, Testing at the Context Boundaries and Organizing and "
            "Documenting Context Maps in your own copy first. The lesson reads the pattern "
            "as a tool and then traces one change across a map."
        ),
        "body": [
            ("p", "&ldquo;Map the existing terrain. Take up transformations later.&rdquo; "
                  "That is the last line of the Context Map pattern's statement in Chapter 14. This "
                  "lesson reads the pattern, its example, and the two short sections after "
                  "it, Testing at the Context Boundaries and Organizing and Documenting "
                  "Context Maps."),
            ("p", "The problem: a single Bounded Context still gives no global view. People "
                  "on other teams do not know where its edges are and blur them without "
                  "meaning to, and where two contexts must connect they tend to bleed into "
                  "each other. Reusing code across a boundary is a hazard, Evans says; "
                  "functionality and data should cross it through a translation. He places "
                  "the map where project management and design overlap, because the "
                  "boundaries follow the teams: people who work closely share a model, and "
                  "people who do not talk, even on one team or at opposite ends of one "
                  "building, drift into separate ones."),
            ("p", "The pattern, as a tool. List every model the project really uses, "
                  "counting the unstated models inside subsystems that are not "
                  "object-oriented, and define the context of each. Give each context a name, and let those names enter the "
                  "Ubiquitous Language. Set out where the models touch, with the translation "
                  "explicit and any sharing marked. And describe the situation as it stands. "
                  "The map takes whatever form the team will share, diagram or text or talk; "
                  "it must name every context and make every contact clear. Where a "
                  "relationship does not match one of the chapter's patterns, do not force "
                  "it; describe what is there."),
            ("p", "Two warnings follow. Where you find a splinter, a model entangled and "
                  "inconsistent, mark it on the map as unknown country and finish the rest "
                  "first; until every piece of work sits in some context with explicit "
                  "relationships, fix only outright contradictions, and resist the urge to "
                  "reorganise wholesale. And once the map is clear and you change teams or "
                  "design, change the map only after the reality has changed."),
            ("p", "Evans's example is a routing feature in a booking system, where the team "
                  "doing the route-finding needed a quite different model, built for fast "
                  "network algorithms. He yielded, and the two became separate contexts "
                  "joined by one translator object, which both teams maintain together and "
                  "which should be easy to unit-test. Testing at the Context Boundaries "
                  "draws the moral: contact points deserve the most tests, because "
                  "translation is subtle and communication thinnest there. Organizing and "
                  "Documenting has only two points, that contexts have names in the "
                  "language and that everyone knows where the boundaries lie, and asks you "
                  "to say the model's name, not a colleague's, when you talk about a change."),
            ("p", "Now the count. The lab reads a map: the contexts, and for each "
                  "relationship its upstream, its downstream and its kind, one of the "
                  "book's. Then it follows a change in one context's model. A Shared Kernel "
                  "carries the change both ways, since both teams own the kernel; a "
                  "Conformist or a Customer/Supplier relationship carries it downstream, "
                  "since the downstream model is built on the upstream's; an "
                  "Anticorruption Layer or an Open Host Service stops it at a translator, "
                  "which must change instead. The next three lessons read those patterns; "
                  "here they are the map's legend."),
            ("code", _rows(THEATRE_RELS)),
            ("p", "The map is a theatre's seven contexts: programming, which plans the "
                  "season; the venue; the box office; marketing; finance; an outside "
                  "payments provider; and the agencies that resell tickets. On the preset "
                  "<code>change-programming</code> the season planners change their model of "
                  "a performance. The lab counts 6 relationships. The change reaches the "
                  "venue through the Shared Kernel, the box office through Customer/Supplier, "
                  "and marketing through the box office, which it conforms to: 3 models that "
                  "must change. It stops at 2 translators, finance's layer and the "
                  "box office's host service for the resellers. The lab counts 4 contexts "
                  "reached, the three changed models and finance, whose layer changes "
                  "though its model does not, and 2 untouched, payments and the resellers, "
                  "whose side of the open protocol stays as it was."),
            ("p", "The preset <code>change-payments</code> changes the outside provider "
                  "instead. Its only edge is the box office's Anticorruption Layer, so the "
                  "lab finds 0 models that must change, 1 translator to update, 1 context "
                  "reached, the box office through its layer, and 5 untouched. That is the map doing "
                  "what Evans asks of it: before "
                  "anyone touches code, the team can say, in the language, that a change to "
                  "the Programming model means changing the Venue, Box Office and Marketing "
                  "models and two translators, and that a change at Payments means one translator."),
            ("h3", "Exercise"),
            ("code", _rows(LIBRARY_RELS)),
            ("p", "A public library's map: the catalogue, lending, members, events, a "
                  "supplier's feed of new titles and an old fines system. The catalogue team "
                  "changes its model of a title. By the lab's rules, find the models that "
                  "must change, the translators to update and the contexts untouched. Watch "
                  "the Shared Kernel's direction. Then load the map into the lab with "
                  "`catalogue` as the changed context."),
            ("p", "The map's legend has seven kinds. The next lesson, Shared Kernel and "
                  "Customer/Supplier Teams, reads the two most cooperative."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "map",
            "preset": "change-programming",
            "presets": [
                {"id": "change-programming",
                 "label": "The season planners change their model of a performance",
                 "contexts": THEATRE_CONTEXTS,
                 "rels": THEATRE_RELS,
                 "changed": "programming",
                 "expect": {"dcxRels": "6", "dcxModels": "3: venue, boxoffice, marketing", "dcxTranslators": "2: finance’s ACL from boxoffice, boxoffice’s protocol", "dcxReached": "4: venue, boxoffice, marketing, finance", "dcxUntouched": "2: payments, resellers"}},
                {"id": "change-payments",
                 "label": "The outside payments provider changes its model",
                 "contexts": THEATRE_CONTEXTS,
                 "rels": THEATRE_RELS,
                 "changed": "payments",
                 "expect": {"dcxRels": "6", "dcxModels": "0: none", "dcxTranslators": "1: boxoffice’s ACL from payments", "dcxReached": "1: boxoffice", "dcxUntouched": "5: programming, venue, marketing, finance, resellers"}},
            ],
            "panel_title": "What one change reaches across a map",
            "panel_intro": _MAP_INTRO,
        }),
        "steps_title": "Tracing a change across a map",
        "steps_intro": "Four steps, the last of them on a map of your own.",
        "steps": [
            ("Name every context",
             "List every model in play, including the legacy and outside systems and any "
             "subsystem that is not object-oriented, and give each a name the team will say."),
            ("Mark each relationship",
             "For each point of contact, write which side is upstream and which of the "
             "chapter's kinds it is, or describe it plainly if it fits none."),
            ("Follow the change",
             "From the changed context, cross every Shared Kernel in either direction and "
             "every Conformist or Customer/Supplier edge downstream; stop at each "
             "Anticorruption Layer or Open Host Service and note its translator."),
            ("Do it on your own system",
             "Draw the contexts your team's code talks to, mark each edge, and pick one "
             "upstream change from last quarter. Count the models and translators it "
             "reached, and compare with what actually had to change."),
        ],
        "worked": {
            "title": "The season planners' change",
            "intro": [
                "Trace <code>change-programming</code> by hand.",
            ],
            "lines": [
                "programming to venue: kernel, venue changes",
                "programming to boxoffice: supplier, changes",
                "boxoffice to marketing: conformist, changes",
                "boxoffice to finance: layer, translator",
                "boxoffice to resellers: host, translator",
                "payments: upstream only, untouched",
            ],
            "after": [
                "Three models and two translators. The count assumes the change crosses "
                "every edge its kind allows; on a real map a small change may touch only part "
                "of a kernel, which the lab cannot know.",
            ],
        },
        "quiz_title": "Maps, boundaries and Evans's advice",
        "quiz": [
            {"q": "In the exercise (the library's map, with the catalogue's model changed), "
                  "which models must change by the lab's rules?",
             "a": ["Lending only",
                   "Lending and events",
                   "Lending, events and members",
                   "Lending, events, members and the supplier's feed"],
             "c": 2,
             "why": "Customer/Supplier carries the change from the catalogue to lending; the "
                    "Conformist edge carries it on to events; and the Shared Kernel between "
                    "members and lending carries it both ways, so members changes too, though "
                    "members is the kernel's upstream side. That is 3 models and 0 "
                    "translators: the two Anticorruption Layers are on edges into the "
                    "catalogue and lending from the supplier feed and the fines system, "
                    "which are upstream and untouched."},
            {"q": "What does Evans advise when the map reveals a splinter, a model entangled "
                  "and inconsistent?",
             "a": ["Mark it on the map, finish describing everything, and until the map is "
                   "clear change only outright contradictions",
                   "Stop mapping and repair the splinter before going on",
                   "Split it at once into two Bounded Contexts",
                   "Reorganise the teams around it before drawing the rest"],
             "c": 0,
             "why": "He says to mark the confusion on the map and finish describing "
                    "everything first; until every piece of work sits in a context with "
                    "explicit relationships, change only outright contradictions, and do "
                    "not let repair turn into wholesale reorganisation."},
            {"q": "What form does the pattern require a Context Map to take?",
             "a": ["A UML package diagram",
                   "A table of every package in each context",
                   "A diagram kept in the code repository",
                   "Any form, provided it is shared, names every context and makes the "
                   "points of contact clear"],
             "c": 3,
             "why": "Evans says the map need not be documented in any particular form. He "
                    "likes informal diagrams, others prefer text, and sometimes discussion "
                    "is enough; whatever the form, everyone must share it, every context must "
                    "have a clear name, and the contacts and their nature must be clear."},
            {"q": "On the preset <code>change-programming</code>, the box office's "
                  "relationship to marketing is changed from conformist to acl. What does "
                  "the lab report?",
             "a": ["3 models must change and 2 translators update, as before",
                   "2 models must change, venue and box office, and 3 translators update",
                   "1 model must change, the venue, and 3 translators update",
                   "2 models must change and 2 translators update"],
             "c": 1,
             "why": "Marketing now translates what the box office gives it, so its model is "
                    "spared and its translator must change instead: the venue and the box "
                    "office are still reached, through the kernel and Customer/Supplier, "
                    "and the translators are finance's, the resellers' and marketing's."},
        ],
        "mistakes": [
            ("Drawing the map you want instead of the one you have",
             "A map of the intended organisation looks more useful. Evans insists the map "
             "describe the situation as it stands, relationships that fit no pattern "
             "included, with transformations taken up later and the map changed only after "
             "the reality has. On the lesson's illustration the counts are of the theatre's "
             "map as drawn; a map of the hoped-for relationships would count a change the "
             "teams will not actually see."),
            ("Naming contexts after people or teams",
             "It is how talk naturally goes: George's team is changing its stuff. Organizing "
             "and Documenting asks for the model's name instead, so that the names enter the "
             "Ubiquitous Language and the sentence says which translator must change."),
            ("Reusing code across a boundary to save a translation",
             "Evans calls reuse between contexts a hazard. Functionality and data should "
             "cross through a translation, which the map makes explicit and which the "
             "boundary tests watch; a shared class across the line is how the chapter's "
             "opening story began."),
        ],
        "standard": (
            "Finish when you can trace a change across a context map.",
            "Given a map of contexts and relationships, state which models a change in one "
            "context reaches, which translators absorb it, and which contexts it leaves alone."
        ),
        "note": (
            "The lab assumes a change crosses every edge its kind allows. It cannot tell a "
            "change inside a Shared Kernel from one outside it, or whether a downstream "
            "context uses the part that changed. Nor does it count a downstream's own "
            "layer when that downstream's model changes: the box office's layer for "
            "payments may need its box-office side rewritten. And it cannot draw the map: "
            "finding the contexts and their real relationships is the work the pattern "
            "asks for."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Relationships Between Bounded Contexts (PDF p. 219 of the operator's copy);
    # Shared Kernel (p. 220); Customer/Supplier Development Teams (pp. 221-223),
    # with its example (pp. 222-223).
    # Quote: PDF p. 220 of the operator's copy, 17 words, quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "shared-kernel-and-customer-supplier",
        "title": "Shared Kernel and Customer/Supplier Teams",
        "module": MODULE,
        "one_line": "Share a small, agreed part of the model both ways, or let one team serve another, with tests both can run.",
        "summary": (
            "The chapter's relationship patterns begin with the two most cooperative. Read "
            "Evans's Shared Kernel, a part of the model two teams hold in common and change only "
            "together, and his Customer/Supplier Development Teams, where the downstream "
            "team is a customer with acceptance tests; then count which contexts one change "
            "must reach under each."
        ),
        "key": [
            "a kernel: shared, changed by agreement",
            "both teams' tests pass on every change",
            "kernel merges less often than daily",
            "upstream serves, downstream is customer",
            "acceptance tests in the upstream suite",
            "a kernel is two-way; a supplier, one-way",
        ],
        "key_label": "Two cooperative patterns in six lines",
        "concepts_intro": (
            "Three terms carry the lesson: the section's two patterns and the test that "
            "holds the second together."
        ),
        "concepts": [
            ("Shared Kernel",
             "A part of the domain model, with the code and schema behind it, that two "
             "teams hold in common by explicit agreement. It is changed only after consulting the other team, and "
             "both teams' tests must pass on it."),
            ("Customer/Supplier Development Teams",
             "Two teams whose contexts depend one way, related as a customer and its "
             "supplier: the downstream team joins the upstream team's planning as a "
             "customer, and its needs are negotiated and scheduled."),
            ("Acceptance tests at the interface",
             "Automated tests, written by the downstream team with the upstream one, of the "
             "interface the downstream team relies on, run in the upstream team's own suite "
             "so a breaking change is seen before it ships."),
        ],
        "read_title": "The section's spectrum first, then the two patterns, then the count",
        "read_intro": (
            "Read Relationships Between Bounded Contexts, Shared Kernel and Customer/Supplier "
            "Development Teams in your own copy first. The lesson reads both patterns as "
            "tools and then counts what a change reaches under each."
        ),
        "body": [
            ("p", "&ldquo;This explicitly shared stuff has special status, and shouldn't be "
                  "changed without consultation with the other team.&rdquo; That is from "
                  "Shared Kernel, the first of the relationship patterns in Chapter 14. This "
                  "lesson reads the short introduction Relationships Between Bounded "
                  "Contexts, then Shared Kernel and Customer/Supplier Development Teams."),
            ("p", "The introduction says what the patterns are for. They are targets to "
                  "move a relationship toward and vocabulary to describe one that exists, "
                  "and a real relationship that comes close to one can be named after it, "
                  "with its differences noted. Evans names the variables that decide among "
                  "them: how much control you have over the other model, how the teams "
                  "cooperate, and how deeply features and data must be integrated. The "
                  "patterns then run from the most cooperative to the least."),
            ("p", "Shared Kernel starts where functional integration is limited and "
                  "Continuous Integration costs more than it returns, especially when the "
                  "team is too big or lacks the skill or the political organisation to "
                  "integrate continuously. Teams that simply race ahead on closely related "
                  "applications can end up paying more for translation and retrofits than "
                  "integration would have cost. Evans's middle way borrows from shared "
                  "infrastructure: choose a part of the domain model, with the code and "
                  "schema behind it, that two teams hold in common by explicit agreement. "
                  "That part changes only after "
                  "consultation; it is integrated less often than each team's own code, "
                  "perhaps weekly where the teams merge daily; and at each integration both "
                  "teams' tests must pass. The kernel aims to reduce duplication, not end "
                  "it, as one context would."),
            ("p", "Customer/Supplier Development Teams covers a different shape: one "
                  "subsystem feeds another, the downstream one gives little back, and every "
                  "dependency runs one way. Such pairs fall naturally into two contexts, "
                  "often with different skills, tools and users, and translation is simpler "
                  "for running in one direction. The danger is political. An upstream team "
                  "that downstream can veto is cramped, or afraid of breaking it; a "
                  "downstream team at the mercy of upstream priorities is helpless."),
            ("p", "The remedy is to make the relationship formal. In planning, the downstream "
                  "team plays customer to the upstream team, its needs negotiated and "
                  "budgeted so that everyone knows what is promised and when; on an Extreme "
                  "Programming project the planning game already has the place for it. The "
                  "two teams write automated acceptance tests of the interface downstream "
                  "relies on, and the upstream team runs them in its own suite, which frees "
                  "it to change without fear. Evans marks two elements as crucial: the "
                  "customer's needs come first, not a poor relation's begging, and the tests "
                  "exist. His example, a yield-analysis team taking data from a booking "
                  "system, works because both project managers report to one person; such "
                  "teams succeed, he says, when they share management or really are "
                  "customer and supplier."),
            ("p", "Now the count, on the theatre's season planning, venue, box office and "
                  "café. Programming and the venue share a kernel, the calendar of "
                  "performances and spaces. The box office is programming's customer, and "
                  "the café, which forecasts its stock from ticket sales, is the box "
                  "office's. On the preset <code>change-programming</code> the lab counts 3 "
                  "relationships and finds 3 models that must change, venue, box office and "
                  "café, with 0 translators and 0 contexts untouched."),
            ("code", _rows(KERNEL_RELS)),
            ("p", "The other two presets show the two directions. On "
                  "<code>change-venue</code> the venue team changes the kernel, and the "
                  "change reaches programming, the kernel's other owner, and from there "
                  "the box office and the café: again 3 models. That is why a kernel is "
                  "changed only by agreement; neither side is upstream of the other. On "
                  "<code>change-cafe</code> the café changes its own forecasting model, and "
                  "the lab finds 0 models to change and 3 contexts untouched: a customer's "
                  "change does not travel up to its supplier."),
            ("p", "Read those zeros and threes carefully. The lab says what is connected, "
                  "not what breaks. Under Customer/Supplier the box office still must "
                  "change when programming does; what the pattern adds is that the change "
                  "was negotiated in planning and the acceptance tests catch it before it "
                  "reaches the box office's users. A count of reached models is the same "
                  "with tests or without; the surprise is what the tests remove."),
            ("h3", "Exercise"),
            ("code", _rows(KERNEL_RELS_WIDER)),
            ("p", "Suppose programming and the box office also agreed to share a kernel, the "
                  "map above. The box office changes its model of a sale. By the lab's "
                  "rules, find the models that must change on this map, and then on the "
                  "original map, where programming supplies the box office. Say in a "
                  "sentence what the wider kernel costs the box office team."),
            ("p", "Both patterns need a willing partner upstream. The next lesson, Conformist "
                  "and Anticorruption Layer, reads what a downstream team can do without one."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "map",
            "preset": "change-programming",
            "presets": [
                {"id": "change-programming",
                 "label": "Programming changes the season calendar",
                 "contexts": KERNEL_CONTEXTS,
                 "rels": KERNEL_RELS,
                 "changed": "programming",
                 "expect": {"dcxRels": "3", "dcxModels": "3: venue, boxoffice, cafe", "dcxTranslators": "0: none", "dcxReached": "3: venue, boxoffice, cafe", "dcxUntouched": "0: none"}},
                {"id": "change-venue",
                 "label": "The venue team changes the shared kernel",
                 "contexts": KERNEL_CONTEXTS,
                 "rels": KERNEL_RELS,
                 "changed": "venue",
                 "expect": {"dcxRels": "3", "dcxModels": "3: programming, boxoffice, cafe", "dcxTranslators": "0: none", "dcxReached": "3: programming, boxoffice, cafe", "dcxUntouched": "0: none"}},
                {"id": "change-cafe",
                 "label": "The café changes its own forecasting model",
                 "contexts": KERNEL_CONTEXTS,
                 "rels": KERNEL_RELS,
                 "changed": "cafe",
                 "expect": {"dcxRels": "3", "dcxModels": "0: none", "dcxTranslators": "0: none", "dcxReached": "0: none", "dcxUntouched": "3: programming, venue, boxoffice"}},
            ],
            "panel_title": "A kernel and two suppliers",
            "panel_intro": _MAP_INTRO,
        }),
        "steps_title": "Choosing between a kernel and a supplier",
        "steps_intro": "Four steps, the last of them on two teams you know.",
        "steps": [
            ("Find the direction of dependence",
             "For the two contexts, ask whether either uses the other's model or output, and "
             "whether the dependence runs one way or both."),
            ("Name what would be shared",
             "If both depend on one part of the model, write down that part: the classes, the "
             "tables, the tests. The smaller it is, the cheaper a kernel."),
            ("Write down the agreement",
             "For a kernel, how changes are agreed and how often both teams' tests run on it; "
             "for a supplier, how the customer's needs enter planning and which acceptance "
             "tests the upstream suite runs."),
            ("Do it on two teams you know",
             "Pick two teams where one consumes the other's data. Say which pattern their "
             "relationship comes closest to, list the tests that would guard it, and count "
             "how many of those exist today."),
        ],
        "worked": {
            "title": "A change in the kernel",
            "intro": [
                "Trace <code>change-venue</code> by hand.",
            ],
            "lines": [
                "venue to programming: kernel, both ways",
                "programming to boxoffice: supplier",
                "boxoffice to cafe: supplier",
                "models reached: 3, translators 0",
            ],
            "after": [
                "A kernel has two owners, and neither side is upstream of the other, so a change by either reaches the "
                "other, and everything the other supplies. The lab assumes the change is "
                "inside the kernel; a change to the venue's own part would stay at home.",
            ],
        },
        "quiz_title": "Kernels, suppliers and their tests",
        "quiz": [
            {"q": "In the exercise, the box office changes its model. How many models must "
                  "change on the wider-kernel map, and how many on the original map?",
             "a": ["1 on both maps: only the café",
                   "3 on the wider-kernel map, 1 on the original map",
                   "2 on the wider-kernel map, 1 on the original map",
                   "3 on both maps"],
             "c": 1,
             "why": "On the wider map the kernel carries the change from the box office to "
                    "programming, the other kernel carries it to the venue, and "
                    "Customer/Supplier carries it to the café: 3. On the original map "
                    "programming is the box office's supplier, and a change downstream does "
                    "not travel up, so only the café is reached: 1. The wider kernel makes "
                    "every box office change a matter for two more teams."},
            {"q": "How often does Evans suggest a Shared Kernel be integrated?",
             "a": ["Continuously, like each team's own code",
                   "Never: each team keeps its own copy for good",
                   "Only at releases",
                   "Frequently, but somewhat less often than each team's Continuous "
                   "Integration, for example weekly where the teams merge daily"],
             "c": 3,
             "why": "The teams usually change separate copies of the kernel and merge at "
                    "intervals, less often than their own integration: his example is a weekly "
                    "kernel merge on teams that integrate daily. He adds that the teams "
                    "should talk about changes as soon as possible, whatever the schedule."},
            {"q": "Which two elements does Evans call crucial to Customer/Supplier "
                  "Development Teams?",
             "a": ["The customer's needs come first in negotiation, and an automated "
                   "acceptance test suite lets each team work without watching the other",
                   "A shared code base and a shared database",
                   "A veto for the downstream team over upstream changes, and weekly merges",
                   "A translator owned jointly by both teams"],
             "c": 0,
             "why": "The relationship must be truly that of customer and supplier, with the "
                    "customer's needs paramount, and there must be automated tests of the "
                    "interface. A downstream veto is one of the ways he says the upstream "
                    "team gets cramped."},
            {"q": "Under what conditions does Evans expect Customer/Supplier teams to work best?",
             "a": ["When the two teams use the same tools and language",
                   "When the upstream team has many small customers",
                   "When both teams work under the same management, or are in different "
                   "companies that really hold those roles",
                   "When the downstream team can rewrite the upstream code"],
             "c": 2,
             "why": "Shared management gives the teams shared goals, and a real commercial "
                    "relationship gives the supplier a reason to serve. A supplier with "
                    "many small customers is one of the situations that, in the next "
                    "pattern, leaves the downstream team on its own."},
        ],
        "mistakes": [
            ("Putting as much as possible into the Shared Kernel",
             "Sharing more seems to save more translation. The kernel cannot be changed as "
             "freely as the rest of the design: every change needs consultation and both "
             "teams' tests. Evans chooses a carefully selected subset and aims to reduce "
             "duplication, not to remove it. On the lesson's illustration widening the kernel "
             "to the box office takes a box office change from 1 model reached to 3."),
            ("Thinking acceptance tests stop the downstream team from having to change",
             "The tests do not change what is connected; the box office is reached by a "
             "programming change with tests or without. They make the change visible to the "
             "upstream team before it ships, and any change to the tests calls for talking to "
             "the other team, because it means the interface is changing."),
            ("Expecting Customer/Supplier to work between any two teams",
             "Evans ties its success to shared management or a real commercial relationship. "
             "Where the upstream team has no reason to serve, the next lesson's patterns "
             "apply instead."),
        ],
        "standard": (
            "Finish when you can say what a kernel and a supplier each make a change reach.",
            "Given a small map with a Shared Kernel and Customer/Supplier edges, state the "
            "models a change in each context reaches, and the agreement each edge needs."
        ),
        "note": (
            "The lab counts connections. It cannot see whether the teams consult before a "
            "kernel change, whether the acceptance tests exist, or whether two project "
            "managers report to one person, and those, in Evans's account, decide whether "
            "the patterns work."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Conformist (PDF pp. 224-225 of the operator's copy), with its sidebar
    # Following Isn't Always Bad (p. 225); Anticorruption Layer (pp. 226-230),
    # Designing the Interface (p. 227), Implementing (pp. 227-229), its example
    # (p. 229) and A Cautionary Tale (pp. 229-230). Facade and Adapter are from
    # Gamma et al. (p. 227).
    # Quote: PDF p. 225 of the operator's copy, 17 words, quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "conformist-and-anticorruption-layer",
        "title": "Conformist and Anticorruption Layer",
        "module": MODULE,
        "one_line": "Without a willing upstream team, adopt its model wholesale, or wall your own off behind a translating layer.",
        "summary": (
            "When the upstream team has no reason to serve you, Evans offers two paths. "
            "Read his Conformist, which gives up an independent model to remove translation, "
            "and his Anticorruption Layer, which keeps one behind facades, adapters and "
            "translators; then count the models one upstream change reaches under each."
        ),
        "key": [
            "no willing upstream: you are on your own",
            "conform: adopt its model, drop translation",
            "following can drag you to a better design",
            "a layer keeps your model in your terms",
            "facade, adapter, translator",
            "every wall has a cost",
        ],
        "key_label": "The two downstream paths in six lines",
        "concepts_intro": (
            "Three terms carry the lesson: the two patterns, and the three parts Evans builds "
            "the second from."
        ),
        "concepts": [
            ("Conformist",
             "A downstream context that adopts the upstream team's model as it is, so that no "
             "translation is needed, at the price of the downstream team's freedom to model "
             "its own way."),
            ("Anticorruption Layer",
             "An isolating layer that gives the downstream context the other system's "
             "functions in the downstream model's own terms, reaches that system by the "
             "interface it already has, and translates both ways."),
            ("Facade, adapter and translator",
             "The layer's parts. A facade simplifies the other system's interface in that "
             "system's own model; an adapter makes the requests one of your services needs; "
             "a translator, holding no state, converts the objects and data."),
        ],
        "read_title": "The downstream team's choice first, then each path, then the count",
        "read_intro": (
            "Read Conformist and Anticorruption Layer, with A Cautionary Tale, in your own "
            "copy first. The lesson reads both as tools and then counts what one upstream "
            "change does to each."
        ),
        "body": [
            ("p", "&ldquo;It is very unappealing emotionally, which is why we choose it less "
                  "often than we probably should.&rdquo; That is Evans on Conformist, in "
                  "Chapter 14. This lesson reads Conformist and Anticorruption Layer, the two "
                  "patterns for a downstream team that cannot count on the upstream one."),
            ("p", "Conformist begins where Customer/Supplier fails. When the two teams are "
                  "not directed from one place, because they are far apart in a large "
                  "company, or the shared manager does not care, or the supplier has many "
                  "small customers, or is changing direction, or has gone out of business, "
                  "the downstream team is on its own. Promises from upstream will not be "
                  "kept, and plans built on them will wait. Evans gives three paths. "
                  "Abandon the upstream, which is Separate Ways, two lessons on. If the "
                  "dependency must stay and the upstream design is hard to work with, build "
                  "your own model and a translation layer. If its quality is tolerable and "
                  "its style compatible, give up an independent model and conform."),
            ("p", "As a tool, then: follow the upstream model closely and drop translation "
                  "altogether. It cramps the downstream design and probably does not give the "
                  "ideal model for the application, but integration becomes far simpler, and "
                  "the two teams share a language, which helps when the supplier holds all "
                  "the power. The dependence deepens, and the application is limited to what "
                  "the upstream model can do, plus purely additive extensions. A sidebar, "
                  "Following Isn't Always Bad, makes the positive case for an off-the-shelf "
                  "component with a large interface: if it is worth having, its design holds "
                  "crunched knowledge, perhaps more than yours, and conforming can pull your "
                  "design upward. Conformist resembles a Shared Kernel in shape; the "
                  "difference is that the other team is not collaborating."),
            ("p", "Anticorruption Layer is the defensive end of the range. A new system with a "
                  "large interface to another can find its model gradually bent to match the "
                  "other's, piece by piece; legacy models are usually weak, and even a good "
                  "one does not fit the new project's needs. Avoiding all integration is no "
                  "answer, since reuse of existing systems is valuable. The trap is believing "
                  "that only plain values cross between systems, and that a plain value "
                  "means the same on both sides; meaning lives in how the data is associated, and a "
                  "low-level interface leaves your system interpreting someone else's "
                  "data in someone else's terms. So: build an isolating layer that offers "
                  "your context the other system's functions in your own model's terms, "
                  "reaches the other system by the interface it already has, needing little "
                  "or no change there, and translates in both directions."),
            ("p", "The layer is not a messaging mechanism; it translates concepts and "
                  "actions. Its interface is usually a set of Services, each with a coherent "
                  "job in your model. Evans builds it from Facades and Adapters, both from "
                  "Gamma and his colleagues' Design Patterns, and translators. The facade "
                  "simplifies the other system's interface and stays in that system's "
                  "model; the adapter, used a little loosely, he admits, makes the requests "
                  "a service needs; the translator converts objects and data and holds no "
                  "state. The layer can be two-way, can carry an audit trail, and can even "
                  "join two contexts of your own."),
            ("code", _lines(ACL_JAVA)),
            ("p", "Above, a sketch of one service in such a layer, written for the lesson. "
                  "The box office asks its own question, whether a patron has a discount; "
                  "the adapter asks the old membership system's facade for a row by card "
                  "number; the translator turns the patron into a card number and the row "
                  "into a `Discount`. Nothing outside this class names `LegacyMemberRow`. "
                  "Evans closes the pattern with A Cautionary Tale, the Great Wall: it kept "
                  "a civilisation distinct and helped bankrupt a dynasty. Isolation has costs "
                  "as well as benefits, and integration of any kind is always expensive."),
            ("p", "Now the count, on the theatre's box office downstream of an old membership "
                  "database, with marketing conforming to the box office and finance its "
                  "customer. On the preset <code>conform</code> the box office conforms to "
                  "the old system, and the membership team changes its model: the lab finds "
                  "3 models that must change, box office, marketing and finance, and 0 "
                  "translators. On the preset <code>acl</code> the box office sits behind an "
                  "Anticorruption Layer instead: 0 models that must change, 1 translator "
                  "to update, the box office's, and 2 contexts untouched, marketing and "
                  "finance."),
            ("code", _rows(LEGACY_ACL)),
            ("p", "Three to nought is not a verdict. The layer is code the box office team "
                  "writes and keeps, for every change on the other side, and the lab's 1 "
                  "translator may be a day's work or a month's. The conforming team writes "
                  "no translator, and its 3 models change because the box office takes the "
                  "old model as it is, and marketing and finance build on the box office's."
                  " There is nothing to adapt. Which is cheaper depends on how large the "
                  "interface is, how often the upstream model changes and how good it is, "
                  "the questions Evans asks."),
            ("h3", "Exercise"),
            ("code", _rows(BAKERY_CONFORM)),
            ("p", "A bakery's order system conforms to the till software it bought, the "
                  "baking plan conforms to the orders, and accounts translates orders "
                  "through its own layer. The till vendor changes its model. By the lab's "
                  "rules, find the models that must change and the translators to update; "
                  "then do it again with the first relationship made an acl. Check both in "
                  "the lab with `till-vendor` as the changed context."),
            ("p", "Both paths keep an integration. The next lesson, Separate Ways, Open Host "
                  "Service and Published Language, reads the choice to have none, and two "
                  "ways to make one cheaper for many."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "map",
            "preset": "conform",
            "presets": [
                {"id": "conform",
                 "label": "The box office conforms to the old membership system",
                 "contexts": LEGACY_CONTEXTS,
                 "rels": LEGACY_CONFORM,
                 "changed": "members-legacy",
                 "expect": {"dcxRels": "3", "dcxModels": "3: boxoffice, marketing, finance", "dcxTranslators": "0: none", "dcxReached": "3: boxoffice, marketing, finance", "dcxUntouched": "0: none"}},
                {"id": "acl",
                 "label": "The box office keeps its model behind an Anticorruption Layer",
                 "contexts": LEGACY_CONTEXTS,
                 "rels": LEGACY_ACL,
                 "changed": "members-legacy",
                 "expect": {"dcxRels": "3", "dcxModels": "0: none", "dcxTranslators": "1: boxoffice’s ACL from members-legacy", "dcxReached": "1: boxoffice", "dcxUntouched": "2: marketing, finance"}},
            ],
            "panel_title": "One upstream change, conformed to or translated",
            "panel_intro": _MAP_INTRO,
        }),
        "steps_title": "Choosing a downstream path",
        "steps_intro": "Five steps, the last of them on a system you depend on.",
        "steps": [
            ("Check the upstream team's motive",
             "Ask whether anything makes the upstream team serve you: shared management, a "
             "contract, your importance to it. If nothing does, Customer/Supplier is not "
             "available."),
            ("Ask whether you need it at all",
             "Weigh dropping the dependency, honestly, without assuming the upstream will "
             "change for you."),
            ("Judge its model and the interface",
             "A tolerable model with a compatible style and a large interface points to "
             "conforming; a poor model, or a small interface, to translating."),
            ("Sketch the layer if you translate",
             "Name the services your model wants, the facade over the other system, the "
             "adapter for each service and the translators between them."),
            ("Do it on a system you depend on",
             "Pick an outside API your code calls. Count the places its types appear outside "
             "the code that calls it, and say whether your design conforms to it or "
             "translates it."),
        ],
        "worked": {
            "title": "The membership change, conformed to",
            "intro": [
                "Trace <code>conform</code> by hand.",
            ],
            "lines": [
                "legacy to boxoffice: conformist, changes",
                "boxoffice to marketing: conformist, changes",
                "boxoffice to finance: supplier, changes",
                "models reached: 3, translators: 0",
            ],
            "after": [
                "Under <code>acl</code> the first edge stops the change at the box office's "
                "translator, and nothing beyond it moves. The lab counts what is reached; "
                "what the translator costs to keep is the trade the chapter weighs.",
            ],
        },
        "quiz_title": "Conforming, translating and Evans's reasons",
        "quiz": [
            {"q": "In the exercise (the bakery, with the till vendor's model changed), what "
                  "does the lab report with the first relationship conformist, and with it "
                  "an acl?",
             "a": ["Conformist: 2 models, 1 translator; acl: 0 models, 1 translator",
                   "Conformist: 3 models, 0 translators; acl: 0 models, 1 translator",
                   "Conformist: 2 models, 0 translators; acl: 0 models, 2 translators",
                   "Conformist: 2 models, 1 translator; acl: 1 model, 1 translator"],
             "c": 0,
             "why": "Conforming carries the change to orders and from orders to the baking "
                    "plan, 2 models; accounts translates orders through its own layer, so "
                    "its translator must change, 1. With an acl on the first edge, orders' "
                    "translator absorbs the change and nothing past it moves: 0 models and 1 "
                    "translator, a different one."},
            {"q": "Which situation does Evans's sidebar Following Isn't Always Bad describe?",
             "a": ["Conforming to a legacy system you are about to replace",
                   "Conforming only through an adapter that changes the model",
                   "Conforming to a team that refuses to cooperate, as a punishment",
                   "Conforming to an off-the-shelf component with a large interface, whose "
                   "design may know more than yours"],
             "c": 3,
             "why": "For a bought component with a large interface he says you should "
                    "typically conform: if the component is worth having it holds crunched "
                    "knowledge, and following it may drag you into a better design. Adapters "
                    "for small format changes are allowed, but the model should be the same."},
            {"q": "In Evans's design, which part of an Anticorruption Layer belongs to the "
                  "other system's Bounded Context?",
             "a": ["The translator",
                   "The adapter",
                   "The facade",
                   "The services that form the layer's interface"],
             "c": 2,
             "why": "The facade simplifies the other system's interface and is written "
                    "strictly in that system's model, so it belongs to that system's context. "
                    "The services speak your model, the adapters make requests for them, and "
                    "the translators convert between the two."},
            {"q": "What is the moral Evans draws from A Cautionary Tale, the Great Wall?",
             "a": ["Walls always fail in the end",
                   "Isolation has costs to weigh against its benefits; there is a time to "
                   "revise the model to fit foreign ones",
                   "A layer must be impenetrable to be worth building",
                   "Legacy systems should be replaced at once rather than walled off"],
             "c": 1,
             "why": "The Wall let a culture define itself and was expensive enough to help "
                    "bankrupt a dynasty. Evans's point is balance: weigh the benefits of "
                    "isolation against its costs, and sometimes make measured changes to the "
                    "model so it fits others more smoothly. Replacing everything at once is "
                    "something he warns against."},
        ],
        "mistakes": [
            ("Treating Conformist as surrender, always to be avoided",
             "It feels like giving up on design. Evans says the reluctance is emotional and "
             "the pattern is chosen less often than it should be: it removes translation, "
             "gives the teams one language, and, for a good component with a large interface, "
             "can pull a design upward. Its costs are real, limits on what the application "
             "can do and a deeper dependence. On the lesson's illustration the conforming "
             "teams change three models and write no translator; that is a trade, not a loss."),
            ("Mistaking an Anticorruption Layer for the transport between systems",
             "Evans separates them: the communication link can sit anywhere, between your "
             "system and the layer's services or between the adapter and the facade, and "
             "that placement has no bearing on the layer's job, which is translating concepts "
             "and actions from one model to the other."),
            ("Passing the other system's primitive data straight through",
             "Plain values look safe because they seem to mean the same everywhere. Evans says "
             "that assumption is usually wrong: meaning lives in how the data is associated, "
             "and a low-level interface leaves your model interpreting the other one's. In "
             "the lesson's sketch only the translator sees `LegacyMemberRow`."),
        ],
        "standard": (
            "Finish when you can say what conforming and translating each make a change reach.",
            "Given an upstream change and a downstream path, state the models and translators "
            "it reaches under Conformist and under an Anticorruption Layer, and the parts the "
            "layer would need."
        ),
        "note": (
            "The lab counts one translator as one, whether it is ten lines or ten thousand, "
            "and it cannot judge the upstream model's quality, the size of the interface or "
            "the team's appetite for the work, which are what Evans's choice between the two "
            "paths turns on."
        ),
    },
]
