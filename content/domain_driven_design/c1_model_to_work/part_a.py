"""Putting the Domain Model to Work, lessons 1-5 -- Part I, Chapters 1-3.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 1, Crunching Knowledge; Chapter 2,
Communication and the Use of Language; Chapter 3, Binding Model and
Implementation. Pages in the comments are PDF pages of the operator's copy;
the lessons cite by chapter, section and pattern. Every quotation is copied
from that copy and checked with quotes.py. The models and code are written for
these lessons: none of the book's listings, diagrams, dialogues or example
domains is reproduced. Each glossary, rule and module map is one constant
below, used both by the lesson's code block and by the lab preset that counts
it, so the figures the prose names are the lab's. The design is
docs/domain-driven-design/PLAN.md, section C, Course 1.
"""


def _lines(text):
    """A constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- models

# 1.1 Crunching Knowledge: a seed library. One record a concept: the concept,
# then the curators', the growers' and the developers' name for it.
SEEDS_FIRST = """accession, accession, lot, batch;
germination_test, germ_test, sprout_count, test_run;
viability, viability, strike_rate, pass_rate;
regeneration, regeneration, grow_out, replant;
variety, variety, variety, variety;
donor, donor, saver, supplier;
packet, packet, packet, batch;
isolation_distance, isolation_distance, isolation, spacing;"""

SEEDS_CRUNCHED = """accession, accession, accession, accession;
germination_test, germination_test, germination_test, germination_test;
viability, viability, viability, viability;
regeneration, regeneration, grow_out, regeneration;
variety, variety, variety, variety;
donor, donor, donor, donor;
packet, packet, packet, packet;"""

SEEDS_EXERCISE = """withdrawal, withdrawal, packet, withdrawal;
return, return, give_back, deposit;
member, member, member, patron;
packet, packet, packet, packet;"""

# 1.2 Knowledge-Rich Design: a clinic's evening session. The rule buried in a
# booking method, and the same rule as an object of the model.
BURIED_RULE = """// The clinic's rule, buried in the method that books.
Booking book(Session s, Request r) {
    int load = s.bookedMinutes() + r.minutes();
    if (r.minutes() > 30 || load > 195
            || (!r.isUrgent() && r.noticeDays() < 1)) {
        return Booking.refused();
    }
    return s.add(r);
}"""

EXPLICIT_RULE = """// The same rule as an object of the model, a method a clause.
class EveningSessionPolicy {
    boolean fitsStandardSlot(Request r) {
        return r.minutes() <= 30;
    }
    boolean withinAllowance(Session s, Request r) {
        return s.bookedMinutes() + r.minutes() <= 195;
    }
    boolean hasStanding(Request r) {
        return r.isUrgent() || r.noticeDays() >= 1;
    }
    boolean admits(Session s, Request r) {
        return fitsStandardSlot(r) && withinAllowance(s, r)
            && hasStanding(r);
    }
}"""

CLINIC_SPEC = "minutes <= 30 and load <= 195 and (urgent = yes or notice >= 1)"

CLINIC_EXERCISE = "request_d, minutes=30, load=196, urgent=no, notice=2"

# 1.3 Ubiquitous Language: a theatre box office. The concept, then the
# experts', the developers' and the code's name for it.
BOX_OFFICE_TWO = """production, show, production, production;
performance, show, performance, slot;
hold, hold, temp_block, seat_lock;
booking, booking, reservation, order;
comp, comp, free_ticket, zero_price_order;
release, release, unblock, seat_unlock;"""

BOX_OFFICE_ONE = """production, production, production, production;
performance, performance, performance, performance;
hold, hold, hold, hold;
booking, booking, booking, order;
comp, comp, comp, comp;
release, release, release, release;"""

BOX_OFFICE_EXERCISE = """subscription, subscription, season_pass, season_pass;
exchange, exchange, rebooking, exchange;
standby, standby, waitlist, standby;
seat, seat, seat, seat;"""

# 1.4 Documents and Explanatory Models: a bike-share. The concept, then the
# design document's term, the word spoken in the team now, and the code's name.
BIKES_OLD_DOC = """station, station, station, station;
dock, dock, dock, dock;
trip, rental, ride, ride;
rebalancing, redistribution, rebalancing, rebalancing;
membership, subscription, membership, membership;
day_pass, -, day_pass, day_pass;
morning_peak, morning_peak, morning_peak, -;"""

BIKES_NEW_DOC = """station, station, station, station;
dock, dock, dock, dock;
trip, ride, ride, ride;
rebalancing, rebalancing, rebalancing, rebalancing;
membership, membership, membership, membership;
day_pass, day_pass, day_pass, day_pass;
morning_peak, morning_peak, morning_peak, -;"""

BIKES_EXERCISE = """fault_report, fault_ticket, fault_report, fault_report;
repair, repair, repair, repair;
e_bike, electric_bike, e_bike, e_bike;
battery_swap, charging, battery_swap, swap;"""

# 1.5 Model-Driven Design: a public library's lending. Each piece of code,
# then its module when the code follows the model's concepts, then its module
# in a design that follows screens and jobs.
LENDING_ELEMENTS = """loan.due_date, loans, checkout_screen;
loan.renewal, loans, renewal_screen;
loan.overdue, loans, nightly_job;
hold.queue, holds, holds_screen;
hold.expiry, holds, nightly_job;
hold.notice, holds, mailer_script;
fine.daily_rate, fines, nightly_job;
fine.cap, fines, checkout_screen;
fine.waiver, fines, desk_screen;"""

LENDING_DRIFTED = LENDING_ELEMENTS.replace(
    "fine.cap, fines, checkout_screen;", "fine.cap, loans, checkout_screen;")

LENDING_CHANGES = """loan_period, loan.due_date;
loan_period, loan.overdue;
hold_pickup_window, hold.expiry;
hold_pickup_window, hold.notice;
fine_cap_per_item, fine.daily_rate;
fine_cap_per_item, fine.cap;
fine_cap_per_item, fine.waiver;
renew_with_hold, loan.renewal;
renew_with_hold, hold.queue;"""

LENDING_EXERCISE = """student_loans, loan.due_date;
student_loans, fine.daily_rate;
student_loans, loan.renewal;"""


_LANG_INTRO = (
    "A count over the small model the lesson states. Here it is a glossary: one "
    "record a concept, with the name each audience gives it, and a dash where an "
    "audience has none. The lab "
    "counts a translation for each pair of audiences whose names for a concept "
    "differ. The count is one consequence of one choice of words; the choice is "
    "weighed in the book, against the domain, the team and the project."
)

_SPEC_INTRO = (
    "A count over the small model the lesson states. Here it is a rule and a request. "
    "The lab reads the "
    "rule as clauses joined by and, or and not, checks the request against each "
    "clause in the order written, and says whether the rule is satisfied and which "
    "clauses are false. Nothing typed is run as a program. Whether the rule is the "
    "right rule is the clinic's question, not the lab's."
)

_CHANGE_INTRO = (
    "A count over the small model the lesson states. Here it is a module map: each "
    "piece of code with its "
    "module in two packagings, and each change with the pieces it touches. The lab "
    "counts the modules each change reaches in each packaging. It counts one "
    "consequence of one way of packaging the code; the choice is weighed in the "
    "book, against the domain, the team and the project."
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 1, opening story (PDF pp. 2-6 of the operator's copy),
    # Ingredients of Effective Modeling (p. 6), Knowledge Crunching (p. 7),
    # Continuous Learning (p. 8).
    # Quote: PDF p. 7 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    {
        "slug": "crunching-knowledge",
        "title": "Crunching Knowledge",
        "module": "Chapter 1 · Crunching Knowledge",
        "one_line": "Developers and domain experts digging a model out of what the experts know, together, with the code feeding back into the talk.",
        "summary": (
            "Chapter 1 opens with a story of a developer who knew nothing of the domain "
            "and a model that grew out of his conversations with its experts. Read "
            "Evans's five ingredients of effective modelling, his case that knowledge "
            "crunching is a team's work with feedback, and his warning that projects "
            "leak knowledge; then count the translations between two kinds of expert "
            "and the developers, before a model and after it."
        ),
        "key": [
            "a team crunches, led by developers",
            "bind the model to the code early",
            "speak a language based on the model",
            "keep concepts that earn their place",
            "feedback has to flow both ways",
            "translations: names that differ, a pair",
        ],
        "key_label": "Crunching knowledge in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Chapter 1's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Domain expert",
             "Someone who knows the business the software serves, as a curator knows a "
             "seed collection or a nurse a clinic's sessions. The expert need know "
             "nothing about software; the developers need to learn enough of the "
             "domain to model it."),
            ("Knowledge crunching",
             "Evans's name for turning a flood of facts into a small set of concepts "
             "that makes sense of them: trying one way of organising the domain after "
             "another, with the experts, and keeping what the software needs."),
            ("A translation",
             "In the lab, a pair of audiences that use different names for one "
             "concept. Each such pair is a place where a conversation has to stop and "
             "say what a word means in the other vocabulary."),
        ],
        "read_title": "The chapter's story and argument first, then the count",
        "read_intro": (
            "Read Chapter 1 up to Knowledge-Rich Design in your own copy first. The "
            "lesson reads it as an argument, with the story as its evidence, and then "
            "counts what a shared model saves in one domain of its own."
        ),
        "body": [
            ("p", "&ldquo;Knowledge crunching is not a solitary activity. A team of "
                  "developers and domain experts collaborate, typically led by "
                  "developers.&rdquo; That sentence, from the section Knowledge "
                  "Crunching, is the claim this lesson reads. It covers the start of "
                  "Chapter 1 of Evans's book: the opening story, Ingredients of "
                  "Effective Modeling, Knowledge Crunching and Continuous Learning. "
                  "Read them in your own copy first."),
            ("p", "The chapter opens with a story. Evans was to build a tool for "
                  "engineers who design printed-circuit boards, and he knew nothing "
                  "about electronics. Asking the engineers what the software should do "
                  "got him designs for reading, sorting and annotating text files, "
                  "which would not give them the leap they wanted. What did help was "
                  "talking through what they needed while he sketched informal "
                  "diagrams, being corrected, and correcting their terms in turn. Over "
                  "some days of this the two sides built a model together; Evans then "
                  "wrote a small prototype with no user interface and no storage, only "
                  "the behaviour, and the experts could now see what the model meant "
                  "and argue with it."),
            ("p", "He draws five ingredients from it, which this lesson puts in its "
                  "own words. Bind the model to the implementation early, and keep "
                  "the link through every iteration. Cultivate a language based on "
                  "the model, so that anyone on the team can make a sentence from its "
                  "terms and be understood without a gloss. Make the model rich in "
                  "knowledge: objects with behaviour and rules, not a data schema. "
                  "Distil it, adding concepts as they prove useful and, just as "
                  "important, dropping those that do not. And brainstorm and "
                  "experiment, letting talk and sketches test many variations quickly, "
                  "since an awkward model is often heard before it is seen."),
            ("p", "The section Knowledge Crunching names the activity. Evans compares "
                  "a modeller to a financial analyst sifting figures for the few that "
                  "matter: many organising ideas are tried and dropped until a small "
                  "set of abstract concepts makes sense of the detail. The raw "
                  "material is in the experts' heads, in the users of an old system, "
                  "in the team's experience, in documents and in a great deal of "
                  "talk, and early prototypes feed back into it. His point is that it "
                  "is done by the developers and the experts together, not by one "
                  "side for the other."),
            ("p", "He sets it against three ways of working that fail to crunch. In "
                  "the old waterfall method, experts talk to analysts and analysts "
                  "hand an abstraction to programmers; nothing comes back, so what is "
                  "learned flows one way and does not build up. In an iterative "
                  "project that does not abstract, developers build what the experts "
                  "describe, feature by feature; refactoring can keep the code clean, "
                  "but the team learns what the application does and not the "
                  "principles behind it. And where good programmers abstract on their "
                  "own, without the experts, the concepts come out naive. Crunching "
                  "together changes both sides: developers learn the business, and "
                  "experts sharpen what they know into essentials."),
            ("p", "Continuous Learning adds the condition that makes this a habit "
                  "rather than a phase. At the start a team never knows enough, and "
                  "what it knows leaks: people move on, teams are reorganised, work is "
                  "outsourced so that code arrives and knowledge does not. Evans then "
                  "admits that the feature his circuit-board story turned on was "
                  "later dropped altogether, and the parts of the model that served it "
                  "went with it. The early work still mattered, he argues, because it "
                  "started the crunching, the shared language and the feedback "
                  "through code that everything after it used."),
            ("p", "Now a domain of the lesson's own: a seed library that lends packets "
                  "of seed and asks borrowers to return seed they grew. Three "
                  "audiences talk about it: the curators who run the collection, the "
                  "growers who regenerate stock in the garden, and the developers. "
                  "Each record below is one concept, then the curators', the growers' "
                  "and the developers' word for it, as the first meetings would have "
                  "found them. The lab counts a translation for each of the three "
                  "pairs of audiences whose names for a concept differ."),
            ("code", _lines(SEEDS_FIRST)),
            ("p", "On the preset <code>first-meetings</code> the lab finds 8 concepts, "
                  "only 1 named alike by every audience (variety), and 20 "
                  "translations: three for each of the six concepts on which all "
                  "three words differ, and two for the packet, where only the "
                  "developers differ. It also finds an ambiguous name, a word one "
                  "audience uses for two concepts: the developers' batch means both an "
                  "accession and a packet. Every audience has a name for every "
                  "concept here, so the tile for names missing is empty. Twenty is not "
                  "a cost the lab can price; it is the number of places a "
                  "conversation in this team has to stop and gloss a word."),
            ("p", "The preset <code>after-crunching</code> is the same domain some "
                  "weeks later. The model has done what Evans says his did: it "
                  "consolidated synonyms, so lot, batch and accession are one term, "
                  "and it excluded a fact the library's software does not need, the "
                  "isolation distance between plots, which the growers still know and "
                  "use in the garden. The lab finds 7 concepts, 6 named alike, no "
                  "ambiguous name, and 2 translations, both on regeneration, which the "
                  "growers still call a grow-out. Whether that last word should be "
                  "taken into the model or left as the growers' dialect is a judgement "
                  "the count does not make."),
            ("h3", "Exercise"),
            ("code", _lines(SEEDS_EXERCISE)),
            ("p", "Four more concepts from the seed library's lending desk, with the "
                  "curators', the volunteers' and the code's names in that order. By "
                  "the lab's rule, a translation for each pair of audiences whose "
                  "names for a concept differ, count the translations by hand, and "
                  "find the name one audience uses for two concepts. Then set the "
                  "lab's Audiences to curators volunteers code and type the records "
                  "in to check your count."),
            ("p", "A model consolidates the words a team speaks. The next lesson, "
                  "Knowledge-Rich Design and Deep Models, reads what else it must "
                  "carry: the rules of the business, made explicit."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "glossary",
            "audiences": "curators growers developers",
            "preset": "first-meetings",
            "presets": [
                {"id": "first-meetings",
                 "label": "The seed library's first meetings: three vocabularies",
                 "audiences": "curators growers developers",
                 "terms": SEEDS_FIRST,
                 "expect": {"dlnConcepts": "8", "dlnAlike": "1: variety", "dlnTranslations": "20",
                            "dlnMissing": "0: none",
                            "dlnAmbiguous": "1: batch (developers: accession, packet)"}},
                {"id": "after-crunching",
                 "label": "Some weeks later, with a model the three share",
                 "audiences": "curators growers developers",
                 "terms": SEEDS_CRUNCHED,
                 "expect": {"dlnConcepts": "7", "dlnTranslations": "2", "dlnAmbiguous": "0: none",
                            "dlnAlike": "6: accession, germination_test, viability, variety, donor, packet"}},
            ],
            "panel_title": "The translations three vocabularies need",
            "panel_intro": _LANG_INTRO,
        }),
        "steps_title": "Counting the translations a team pays for",
        "steps_intro": "Four steps, the last of them on a domain of your own.",
        "steps": [
            ("List the concepts, not the words",
             "Write one line for each thing the team talks about, named by what it is, "
             "before deciding whose word to use for it."),
            ("Write down each audience's word",
             "For each concept, write the name each audience actually uses in meetings "
             "and in the code, with a dash where an audience has none."),
            ("Count the pairs that differ",
             "For each concept, compare every pair of audiences and count one "
             "translation for each pair whose names differ; then look for a name that "
             "one audience uses for two concepts."),
            ("Do it on your own domain",
             "Take five concepts from a system you work on, write the experts', the "
             "developers' and the code's names for each, and count the translations. "
             "Write the figure down, and name the one word you would change first."),
        ],
        "worked": {
            "title": "Twenty translations in the first meetings",
            "intro": [
                "Count the translations in <code>first-meetings</code>, three pairs a "
                "concept.",
            ],
            "lines": [
                "accession: lot, batch, all differ: 3",
                "germination test: all three differ: 3",
                "viability: all three differ: 3",
                "regeneration: all three differ: 3",
                "variety: all three alike: 0",
                "donor: saver, supplier, all differ: 3",
                "packet: only the developers differ: 2",
                "isolation distance: all differ: 3",
                "total: 3 + 3 + 3 + 3 + 0 + 3 + 2 + 3 makes 20",
            ],
            "after": [
                "Each figure is the number of pairs that must translate, and the packet "
                "shows why it is a count of pairs: curators and growers agree, so only "
                "the two pairs that include the developers differ. The developers' "
                "batch, used for two concepts, is the kind of collision Evans and the "
                "engineers ironed out as they sketched together.",
            ],
        },
        "quiz_title": "Crunching, its failures, and the count",
        "quiz": [
            {"q": "In the exercise, how many translations does the lab count (one for "
                  "each pair of audiences whose names for a concept differ), and which "
                  "name means two things?",
             "a": ["6, and none",
                   "7, and the volunteers' packet",
                   "12, and the volunteers' packet",
                   "7, and the code's withdrawal"],
             "c": 1,
             "why": "Withdrawal: the volunteers' packet differs from both others, which "
                    "agree: 2. Return: return, give-back and deposit all differ: 3. "
                    "Member: only the code's patron differs: 2. Packet: all alike: 0. "
                    "That is 2 + 3 + 2 + 0 = 7. Twelve is every pair of every concept, "
                    "differing or not. The volunteers say packet for the withdrawal and "
                    "for the packet itself, so their packet is ambiguous; the code's "
                    "withdrawal names one concept only."},
            {"q": "Why, in the section Knowledge Crunching, does the old waterfall "
                  "method fail to crunch knowledge?",
             "a": ["The analysts do not talk to the business experts",
                   "It has no feedback: what is learned flows one way and does not "
                   "accumulate",
                   "Its programmers refactor too little",
                   "It produces no model at all"],
             "c": 1,
             "why": "The analysts do talk to the experts and do build a model; what the "
                    "method lacks is any path back from the programmers or from early "
                    "software to the analysts. Refactoring without abstraction is the "
                    "failing Evans gives to a different kind of project, the iterative "
                    "one that only builds features."},
            {"q": "Evans says the model in his circuit-board story excluded hundreds of "
                  "facts the engineers understood. Why does he count that among its "
                  "strengths?",
             "a": ["The facts were wrong, and the model corrected them",
                   "The facts were not directly relevant to the problems being solved, "
                   "and leaving them out let a newcomer grasp the model quickly",
                   "The engineers did not want them in the software",
                   "Every excluded fact was moved into a separate document"],
             "c": 1,
             "why": "The facts were true, and the engineers went on using them; they "
                    "were simply not what the tool needed. Distilling, the fourth "
                    "ingredient, drops concepts that do not prove useful, which is why a "
                    "developer could read the model's diagrams in minutes. The lab's "
                    "after-crunching preset drops the isolation distance for the same "
                    "reason."},
            {"q": "On the preset <code>after-crunching</code>, the growers adopt the "
                  "word regeneration. How many translations does the lab then count?",
             "a": ["2", "1", "0", "6"],
             "c": 2,
             "why": "The two translations left were both on regeneration, between the "
                    "growers' grow-out and the other two audiences. Once all three say "
                    "regeneration, every concept is named alike by every audience and "
                    "the count is 0. Six is the number of concepts named alike before "
                    "the change, not a count of translations."},
        ],
        "mistakes": [
            ("Thinking knowledge crunching is the analysts' job, finished before the coding starts",
             "Evans's claim is the reverse: developers and experts crunch together, "
             "typically led by developers, and early versions of the software feed "
             "back into what they think. The waterfall hand-off fails, he argues, "
             "because nothing comes back from the programmers to the analysts, so the "
             "knowledge flows one way and does not build up. On the lesson's "
             "illustration the translations fall because all three audiences took "
             "part, not because one wrote a glossary for the others."),
            ("Thinking short iterations and frequent demos are enough",
             "They are not, in Chapter 1. A project can show the experts a feature, "
             "ask what to do next, and keep its code clean by refactoring, and still "
             "learn only what the application should do, never the principles behind "
             "it. Evans grants that such a project can ship working software, but says "
             "new features will never fall out of old ones as corollaries."),
            ("Expecting the model to hold everything the experts know",
             "The circuit-board model left out hundreds of facts the engineers "
             "understood, and Evans counts that as a strength: distilling drops "
             "concepts that are not useful or central. The seed library's model drops "
             "the isolation distance, which the growers still use. A model is "
             "selective by design; what it keeps is a choice about the software's "
             "problems."),
        ],
        "standard": (
            "Finish when you can count the translations a team's vocabularies need.",
            "Given the names several audiences use for a domain's concepts, count the "
            "translations, find the ambiguous name, and say which change to the shared "
            "words would remove the most."
        ),
        "note": (
            "The lab counts pairs of names that differ. It cannot tell a harmless "
            "dialect from a real disagreement about what a concept is, and it cannot "
            "say whether a concept belongs in the model at all; those are what the "
            "crunching decides, with the experts in the room."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 1, Knowledge-Rich Design (PDF p. 8 of the operator's copy),
    # Example: Extracting a Hidden Concept (pp. 9-10), Deep Models (p. 11).
    # Quote: PDF p. 8 of the operator's copy, 23 words, quotes.py OK.
    # Lesson total: 23 words.
    {
        "slug": "knowledge-rich-design-and-deep-models",
        "title": "Knowledge-Rich Design and Deep Models",
        "module": "Chapter 1 · Crunching Knowledge",
        "one_line": "A business rule made an object of the model, named and readable, instead of a condition hidden in the method that uses it.",
        "summary": (
            "The last two sections of Chapter 1: a model must carry the business's "
            "rules as well as its things, and the most useful models lie below the "
            "surface. Read Evans's example of a rule hidden in a guard clause and "
            "lifted into a policy, then check a clinic's booking requests against the "
            "same kind of rule, clause by clause."
        ),
        "key": [
            "rules are as central as things",
            "a guard clause hides a policy",
            "name the rule as a model object",
            "a request fails on a named clause",
            "deep models lie below the surface",
        ],
        "key_label": "Knowledge-rich design in five lines",
        "concepts_intro": (
            "Three terms. The first is Evans's, the second the Gang of Four's as he "
            "uses it, the third the lab's."
        ),
        "concepts": [
            ("Knowledge-rich design",
             "A design whose objects carry the business's activities and rules, not only "
             "its nouns. Evans contrasts it with modelling by finding the nouns in a "
             "description and making each one a class of data."),
            ("Policy",
             "Another name for the Strategy design pattern: an object that holds a rule "
             "so that the code using the rule can stay the same if the rule is "
             "replaced. Evans uses it here for its meaning, a rule of the business, "
             "rather than for the substitution."),
            ("Specification, in the lab",
             "A rule written as clauses, each an attribute compared with a value, joined "
             "by and, or and not. Chapter 9 makes Specification a pattern; here it is "
             "only the lab's way of reading the clinic's rule."),
        ],
        "read_title": "The chapter's argument first, then the rule, then the check",
        "read_intro": (
            "Read Knowledge-Rich Design, its example and Deep Models in your own copy "
            "first. The lesson then writes one clinic's booking rule twice and checks "
            "three requests against it."
        ),
        "body": [
            ("p", "&ldquo;Business activities and rules are as central to a domain as "
                  "are the entities involved; any domain will have various categories "
                  "of concepts.&rdquo; Evans writes this at the start of Knowledge-Rich "
                  "Design, the section after Continuous Learning in Chapter 1. This "
                  "lesson reads it, the example that follows it, Extracting a Hidden "
                  "Concept, and the chapter's last section, Deep Models."),
            ("p", "The argument begins by going past the advice to find the nouns. A "
                  "domain's rules matter as much as its things, and they are where "
                  "crunching gets hard, because the rules may contradict each other. "
                  "Experts, Evans observes, are rarely aware how much they reconcile "
                  "and fill in with common sense as they work; software cannot do "
                  "that. Crunching with the developers is how the rules get stated, "
                  "completed, reconciled, or put out of scope, and the code is then "
                  "refactored to express what was found."),
            ("p", "His example is a booking application from shipping. The business "
                  "deliberately accepts more bookings than a voyage can carry, because "
                  "some always cancel, and the requirements carry the rule as one "
                  "short line. The first code puts it as a guard clause in the method "
                  "that makes a booking, a comparison against capacity times a factor. "
                  "Evans makes two objections: no business expert could read that code "
                  "to check the rule, even with help, and a developer who is not a "
                  "business person would struggle to connect the requirement to it. "
                  "He moves the rule into its own policy class, which the booking "
                  "method asks."),
            ("p", "He names the class after the Strategy pattern of Gamma, Helm, "
                  "Johnson and Vlissides, while noting that Strategy is usually "
                  "chosen so that rules can be swapped, which this application does "
                  "not need. The rule fits the meaning of a policy, and in "
                  "domain-driven design that is as good a reason (Chapter 12 returns "
                  "to it). The gain is in understanding: to get there, everyone has "
                  "had to see the rule as a distinct business rule rather than an "
                  "obscure calculation, and the code can now be shown to an expert. "
                  "He adds at once that he does not recommend such care for every "
                  "detail of a domain; Chapter 15, Distillation, says where to spend "
                  "it."),
            ("p", "Deep Models carries the point further. Useful models seldom lie on "
                  "the surface: early elements are dropped or seen differently, and "
                  "subtler abstractions appear that no one would have proposed at the "
                  "start. On the shipping project behind the example, the team's "
                  "model of cargo and itineraries worked, but the experts were "
                  "unsatisfied; months later the team saw that the business thought "
                  "of shipping as a chain of handovers of responsibility, from "
                  "one party to the next, governed by documents such as the bill of lading. The "
                  "itinerary stayed, but the model changed deeply. Crunching, Evans "
                  "ends, is exploration, and you cannot know where it will end."),
            ("p", "Now a rule of the lesson's own. A clinic runs an evening session "
                  "of 180 minutes, and because a few patients never arrive it lets "
                  "bookings run to 195. It admits a request when the appointment fits "
                  "a standard slot of at most 30 minutes, the session's booked "
                  "minutes with this request stay within 195, and the patient is "
                  "urgent or gave at least a day's notice. The first version buries "
                  "all of that in the booking method."),
            ("code", _lines(BURIED_RULE)),
            ("p", "The second gives the rule a home and its clauses names. "
                  "`EveningSessionPolicy` is a class the clinic's staff could be "
                  "walked through, with `fitsStandardSlot`, `withinAllowance` and "
                  "`hasStanding` saying in the clinic's terms what the conditions "
                  "above say in arithmetic. The booking method would call `admits`, "
                  "and the rule would be found by its name."),
            ("code", _lines(EXPLICIT_RULE)),
            ("p", "The lab reads the same rule as four clauses: `minutes <= 30`, "
                  "`load <= 195`, urgent = yes and `notice >= 1`, where load is "
                  "the session's booked minutes with the request added. On the preset "
                  "<code>routine-booking</code>, a 15-minute request with 3 days' "
                  "notice into a session that would hold 150 minutes, the rule is "
                  "satisfied; 3 of the 4 clauses are true, and the false one, "
                  "urgent = yes, does not matter, because its partner in the or "
                  "holds. The lab still lists it as the first false clause, which is "
                  "a reminder that a false clause refuses only where the rule needs "
                  "it."),
            ("p", "On <code>over-allowance</code>, an urgent 20-minute request that "
                  "would take the session to 205, the rule is not satisfied; the first "
                  "false clause is `load <= 195`, and the false clauses are that one "
                  "and `notice >= 1`, which the urgency covers. On "
                  "<code>long-same-day</code>, a 45-minute request with no notice "
                  "from a patient who is not urgent, with the session at 190, three "
                  "clauses are false: `minutes <= 30` first, then both halves of the "
                  "or. The buried version gives the same answers, but each refusal "
                  "is one compound condition coming out true, with nothing to say "
                  "which part did it; the policy says which part of the "
                  "rule refused, in words the clinic uses."),
            ("h3", "Exercise"),
            ("code", [CLINIC_EXERCISE]),
            ("p", "One more request: 30 minutes, into a session that would then hold "
                  "196 minutes, from a patient who is not urgent and gave 2 days' "
                  "notice. By hand, take the four clauses in order, say whether the "
                  "rule admits the request, and name the first false clause. Then "
                  "type the record into the lab's candidates, with request_d as the "
                  "candidate to validate, to check."),
            ("p", "A rule with a name can be spoken. The next lesson, The Ubiquitous "
                  "Language, reads Chapter 2's case that the model's names should be "
                  "the words the whole team speaks."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "validate",
            "spec": CLINIC_SPEC,
            "preset": "routine-booking",
            "presets": [
                {"id": "routine-booking",
                 "label": "15 minutes, 3 days' notice, session at 150",
                 "spec": CLINIC_SPEC,
                 "candidates": "request_a, minutes=15, load=150, urgent=no, notice=3",
                 "candidate": "request_a",
                 "expect": {"dspSatisfied": "yes", "dspTrue": "3 of 4",
                            "dspFirstFalse": "clause 3, urgent = yes: urgent is no",
                            "dspFalse": "1: urgent = yes"}},
                {"id": "over-allowance",
                 "label": "Urgent, 20 minutes, session would reach 205",
                 "spec": CLINIC_SPEC,
                 "candidates": "request_b, minutes=20, load=205, urgent=yes, notice=0",
                 "candidate": "request_b",
                 "expect": {"dspSatisfied": "no", "dspTrue": "2 of 4",
                            "dspFirstFalse": "clause 2, load <= 195: load is 205",
                            "dspFalse": "2: load <= 195, notice >= 1"}},
                {"id": "long-same-day",
                 "label": "45 minutes, no notice, not urgent, session at 190",
                 "spec": CLINIC_SPEC,
                 "candidates": "request_c, minutes=45, load=190, urgent=no, notice=0",
                 "candidate": "request_c",
                 "expect": {"dspSatisfied": "no", "dspTrue": "1 of 4",
                            "dspFirstFalse": "clause 1, minutes <= 30: minutes is 45",
                            "dspFalse": "3: minutes <= 30, urgent = yes, notice >= 1"}},
            ],
            "panel_title": "The clinic's rule, clause by clause",
            "panel_intro": _SPEC_INTRO,
        }),
        "steps_title": "Lifting a buried rule into the model",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Find the condition that is a rule",
             "Look in an application method for a test that refuses or allows "
             "something for a business reason, not a technical one."),
            ("Say it in the experts' words",
             "Write the rule as a sentence an expert would agree to, and split it at "
             "each and and or into clauses."),
            ("Give the rule and its clauses names",
             "Make the rule a class of the model named for what it is, with one method "
             "a clause, and have the original method ask it."),
            ("Do it on your own code",
             "Find one business rule written as a guard clause in a system you know. "
             "Write it as named clauses, and for one real case say which clause "
             "decides it."),
        ],
        "worked": {
            "title": "The request that runs over",
            "intro": [
                "Check <code>over-allowance</code> against the rule, clause by clause.",
            ],
            "lines": [
                "minutes <= 30: 20 <= 30, true",
                "load <= 195: 205 <= 195, false",
                "urgent: yes, so true",
                "notice >= 1: 0 >= 1, false",
                "the or: true, since the patient is urgent",
                "the rule: true and false and true, so false",
                "first false clause: load <= 195",
            ],
            "after": [
                "Two clauses are false, but only one refuses: the notice clause is "
                "covered by the urgency. That difference is what the buried condition "
                "hides and the named policy shows, and it is why Evans wants an expert "
                "able to read the rule.",
            ],
        },
        "quiz_title": "Hidden rules, policies and the clinic's requests",
        "quiz": [
            {"q": "In the exercise (30 minutes, load 196, not urgent, 2 days' notice), "
                  "does the clinic's rule admit the request, and which is the first "
                  "false clause?",
             "a": ["Admitted; no clause is false",
                   "Refused; the first false clause is minutes <= 30",
                   "Refused; the first false clause is load <= 195",
                   "Refused; the first false clause is urgent = yes"],
             "c": 2,
             "why": "30 <= 30 is true, so the slot clause holds at its boundary. 196 <= "
                    "195 is false, and it is the second clause in order, so it is the "
                    "first false one, and the rule is refused. urgent = yes is also "
                    "false, but it comes after load <= 195, and the or still holds "
                    "because 2 >= 1."},
            {"q": "What were Evans's two objections to the booking rule written as a "
                  "guard clause in the booking method?",
             "a": ["It ran too slowly, and it could not be tested",
                   "A business expert could not read it to check the rule, and a "
                   "technical person who was not a business person would find it hard "
                   "to connect the requirement to the code",
                   "It mixed two unrelated rules, and it ignored cancellations",
                   "It used a double for a capacity, and it returned a magic number"],
             "c": 1,
             "why": "Both objections are about knowledge, not mechanics: the rule was "
                    "unreadable to the people who own it and hard to trace to its "
                    "requirement. Evans does mention that Layered Architecture, in "
                    "Chapter 4, would move the rule into a domain object, but he sets "
                    "that aside to make the point about explicitness."},
            {"q": "Why does Evans call the extracted class a policy, after the Strategy "
                  "pattern, though the application never swaps one rule for another?",
             "a": ["Because Strategy is the only pattern that can hold a rule",
                   "Because the concept fits the meaning of a policy, which in "
                   "domain-driven design is reason enough",
                   "Because the rule will certainly be replaced later",
                   "Because Gamma and colleagues require it for business rules"],
             "c": 1,
             "why": "Evans says plainly that substituting rules, the usual motive for "
                    "Strategy, is not needed here as far as anyone knows. He uses the "
                    "name because the thing being captured is, in the business's own "
                    "terms, a policy; Chapter 12 develops the point."},
            {"q": "On the preset <code>routine-booking</code>, the lab lists urgent = "
                  "yes as the first false clause, yet the rule is satisfied. Why?",
             "a": ["The lab has made an error",
                   "The clause is false, but it sits in an or whose other side, "
                   "notice >= 1, is true",
                   "A false clause never matters once two clauses are true",
                   "The lab skips clauses after the first false one"],
             "c": 1,
             "why": "The rule is minutes and load and (urgent or notice). 15 <= 30, "
                    "150 <= 195 and 3 >= 1 are true, so the or is true though urgent = "
                    "yes is false, and the whole rule holds. It is not a matter of "
                    "counting true clauses: on over-allowance two of four are true and "
                    "the rule fails on one."},
        ],
        "mistakes": [
            ("Thinking a rule is in the model because it is in the code",
             "The guard clause in Evans's booking method was in the code, and it "
             "enforced the rule, but nothing in the design said a rule was there: no "
             "expert could read it and no developer could trace it to the requirement. "
             "Knowledge-Rich Design asks for the rule to be an element of the model, "
             "named as the business names it. The clinic's rule has the same answers "
             "both ways on the lesson's illustration; only the policy says which "
             "clause refused."),
            ("Making every condition a policy object",
             "Evans says directly that he does not recommend so elaborate a design for "
             "every detail of a domain, and points to Chapter 15 for how to choose "
             "where to spend it. A policy earns its class when the rule matters to the "
             "business and the people who own it need to see it."),
            ("Reading the Strategy name as a promise of interchangeable rules",
             "Strategy is usually chosen so that rules can be swapped, and Evans notes "
             "that this application does not need that. He chose the name for its "
             "meaning: the concept is a policy. A reader who builds a family of "
             "interchangeable rules because of the name has added something the domain "
             "did not ask for."),
        ],
        "standard": (
            "Finish when you can lift a buried rule into the model and check a case against it.",
            "Given a business rule written as one condition, write it as named clauses, "
            "and for a given request say whether it is admitted and which clause comes "
            "first among the false ones."
        ),
        "note": (
            "The lab checks a request against the rule as written. It cannot tell "
            "whether the rule is the clinic's real rule, whether two of its clauses "
            "contradict the experts, or whether a deeper model would state it another "
            "way; Evans's shipping project took months to find its deeper view."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 2, opening (PDF p. 12 of the operator's copy), Ubiquitous Language
    # (pp. 12-14), Example: Working Out a Cargo Router (pp. 14-16), Modeling Out
    # Loud (p. 17), One Team, One Language (pp. 18-19).
    # Quotes: PDF p. 13, 8 words; PDF p. 14, 14 words; quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "ubiquitous-language",
        "title": "The Ubiquitous Language",
        "module": "Chapter 2 · Communication and the Use of Language",
        "one_line": "The model's vocabulary used by the whole team, in speech, in writing and in the code, so that nothing has to be translated.",
        "summary": (
            "Chapter 2's first pattern and its two addenda: a language built on the "
            "model and used everywhere, the habit of trying models out loud, and the "
            "rule that the line between languages must never fall between the experts "
            "and the developers. Count what a box office's three vocabularies cost a "
            "conversation, and what is left when the team speaks one."
        ),
        "key": [
            "translation blunts communication",
            "build the language on the model",
            "speech, writing and code alike",
            "a new word is a change to the model",
            "say the model out loud to test it",
            "no language line between the roles",
        ],
        "key_label": "The Ubiquitous Language in six lines",
        "concepts_intro": (
            "Three terms. The first is the pattern's name, the second the chapter's "
            "word for what it removes, the third the lab's."
        ),
        "concepts": [
            ("Ubiquitous Language",
             "The team's one vocabulary, built on the model: the names of its classes "
             "and main operations, its explicit rules, its large-scale principles and "
             "the patterns the team applies. Ubiquitous means it is used everywhere, by "
             "everyone, including in the code."),
            ("A fractured language",
             "Evans's picture of a project without one: experts speaking their jargon, "
             "developers speaking design, the code naming things a third way, and a "
             "few bilingual people translating, inexactly, between them."),
            ("An ambiguous name",
             "In the lab, a word one audience uses for two concepts. It is the hardest "
             "translation to notice, because the speaker hears no difference."),
        ],
        "read_title": "The pattern first, then the dialogues, then the count",
        "read_intro": (
            "Read Chapter 2 up to Documents and Diagrams in your own copy first. The "
            "lesson reads the pattern as a tool and its two addenda as practice, then "
            "counts the translations in one box office."
        ),
        "body": [
            ("p", "&ldquo;Translation blunts communication and makes knowledge "
                  "crunching anemic.&rdquo; The sentence sits in the middle of the "
                  "pattern Ubiquitous Language, the first section of Chapter 2, "
                  "Communication and the Use of Language. This lesson reads the "
                  "pattern, its example, and the two sections that extend it, "
                  "Modeling Out Loud and One Team, One Language."),
            ("p", "The problem Evans sets out is a divide. Experts know little of "
                  "software jargon and speak their own field's, often in several "
                  "flavours; developers describe the system in functional terms, or "
                  "invent abstractions the experts never hear. So everyone "
                  "translates: developers for experts, experts for other experts, "
                  "developers for each other. A few people become bilingual, and "
                  "they turn into bottlenecks whose translations are inexact. The "
                  "worse cost is what translation hides: people using one word for "
                  "different things without noticing, which surfaces later as "
                  "software whose parts do not fit."),
            ("p", "The pattern's answer is to build the team's language on the "
                  "model and use it without exception: in conversation, "
                  "in writing, in diagrams and in the code, with the names of classes "
                  "and their main operations as its vocabulary and the model's "
                  "relationships as its grammar. When a word is awkward, the team "
                  "tries alternatives out loud, and when it settles on one the "
                  "code takes the new word too. The boxed statement "
                  "includes the point the lab will lean on: &ldquo;Recognize that a "
                  "change in the UBIQUITOUS LANGUAGE is a change to the model.&rdquo;"),
            ("p", "Evans admits the plan sounds circular. At first the model is not "
                  "good enough to be a language: it lacks the richness of the "
                  "experts' jargon and the subtler concepts hidden in the developers' "
                  "code. But the jargons cannot be used as they are, since they carry "
                  "ambiguities and contradictions, and it is the insistence on "
                  "speaking the model that drags its weaknesses into the open. Gaps "
                  "get new words, the new words change the model, and the model "
                  "changes the code."),
            ("p", "The chapter's example is a pair of dialogues, written to run in "
                  "parallel, between a user and a developer about rerouting a cargo "
                  "when its customs point changes. In the first the developer talks "
                  "in database rows, flags and procedures; in the second both talk "
                  "about a route specification and the itinerary that must satisfy "
                  "it. The second is shorter and says more of what the user means, "
                  "and Evans adds that a real first dialogue would have been longer "
                  "still. Read both; the difference is in the nouns."),
            ("p", "Modeling Out Loud adds a habit. People are good at spoken "
                  "language, and an awkward model is often easier to hear than to "
                  "see, so Evans asks the team to describe scenarios aloud in the "
                  "model's terms and look for shorter ways to say them, then carry "
                  "the better phrasing back to the diagrams and the code. One Team, "
                  "One Language adds a limit. Developers often keep the model from "
                  "the experts as too abstract for them; Evans answers that if "
                  "capable experts cannot follow the model, the model is wrong. "
                  "Technical and business dialects may extend the language, but they "
                  "should not be rival vocabularies for the same domain."),
            ("p", "Now a domain of the lesson's own: a theatre's box office. Each "
                  "record is a concept, then the box-office experts' word, the "
                  "developers' word and the code's name. The lab ignores letter case, "
                  "so a class named Hold and the spoken hold are one name."),
            ("code", _lines(BOX_OFFICE_TWO)),
            ("p", "On the preset <code>two-languages</code> the lab finds 6 concepts, "
                  "none named alike by all three audiences, and 17 translations: three "
                  "for every concept except the production, where developers and code "
                  "agree and only the experts' show differs, for two. The ambiguous "
                  "name is the experts' show, used for the production that runs all "
                  "season and for the one performance on Tuesday evening. That is the "
                  "translation no one notices in the room: the experts hear no "
                  "difference, and a developer told that a show is sold out has to "
                  "guess which."),
            ("p", "The preset <code>one-language</code> is the team after it has "
                  "taken the model's words for its own, the experts included: they "
                  "say production and performance now, because the split turned out "
                  "to matter to them too. The lab finds 5 of the 6 concepts named "
                  "alike, no ambiguous name, and 2 translations, both on booking, "
                  "where the code still has a class called order. By the pattern "
                  "those two are not a matter of taste: the word changed, so the "
                  "model changed, and the class is to be renamed."),
            ("h3", "Exercise"),
            ("code", _lines(BOX_OFFICE_EXERCISE)),
            ("p", "Four more concepts from the box office, with the experts', the "
                  "developers' and the code's names in that order. By the lab's rule, "
                  "count the translations by hand, and say which audience the code "
                  "agrees with on each concept. Then type them into the lab."),
            ("p", "The language lives in speech and code. The next lesson, Documents, "
                  "Diagrams and Explanatory Models, reads what Chapter 2 says about "
                  "the other places it is written down."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "glossary",
            "audiences": "experts developers code",
            "preset": "two-languages",
            "presets": [
                {"id": "two-languages",
                 "label": "The box office with three vocabularies",
                 "audiences": "experts developers code",
                 "terms": BOX_OFFICE_TWO,
                 "expect": {"dlnConcepts": "6", "dlnAlike": "0: none", "dlnTranslations": "17",
                            "dlnAmbiguous": "1: show (experts: production, performance)"}},
                {"id": "one-language",
                 "label": "One language, with one class still to rename",
                 "audiences": "experts developers code",
                 "terms": BOX_OFFICE_ONE,
                 "expect": {"dlnAlike": "5: production, performance, hold, comp, release",
                            "dlnTranslations": "2", "dlnAmbiguous": "0: none"}},
            ],
            "panel_title": "What a conversation in the box office translates",
            "panel_intro": _LANG_INTRO,
        }),
        "steps_title": "Finding where a team translates",
        "steps_intro": "Four steps, the last of them on a project of your own.",
        "steps": [
            ("Listen for the experts' words",
             "Write down the nouns and verbs the experts use for one scenario, as they "
             "say them, without correcting them."),
            ("Read the code's names beside them",
             "For each concept, find the class or method that stands for it and write "
             "its name next to the experts' word and the developers'."),
            ("Count, then look for the double meaning",
             "Count the pairs that differ for each concept, then look for a word one "
             "audience uses for two concepts; say aloud a sentence that uses it both "
             "ways."),
            ("Do it on your own project",
             "Take one scenario from a system you work on and count the translations "
             "between its experts, its developers and its code. Name one class you "
             "would rename and the word you would rename it to."),
        ],
        "worked": {
            "title": "Seventeen translations at the box office",
            "intro": [
                "Count the translations in <code>two-languages</code>.",
            ],
            "lines": [
                "production: only the experts differ: 2",
                "performance: show, performance, slot: 3",
                "hold: hold, temp block, seat lock: 3",
                "booking: three different words: 3",
                "comp: three different words: 3",
                "release: three different words: 3",
                "total: 2 + 3 + 3 + 3 + 3 + 3 makes 17",
                "ambiguous: show, for two of the concepts",
            ],
            "after": [
                "The count does not see that the experts' show is two translations "
                "in disguise: it is one word in one column, matched against two "
                "different words in the others. That double use is the schism Evans "
                "warns translation hides.",
            ],
        },
        "quiz_title": "One language, its cost and its changes",
        "quiz": [
            {"q": "In the exercise, how many translations does the lab count, one for "
                  "each pair of audiences whose names for a concept differ?",
             "a": ["5", "6", "7", "8"],
             "c": 1,
             "why": "Subscription: developers and code agree on `season_pass`, so only "
                    "the two pairs with the experts differ: 2. Exchange: experts and "
                    "code agree, the developers' rebooking differs: 2. Standby: experts "
                    "and code agree, the developers' waitlist differs: 2. Seat: all "
                    "alike, 0. That is 6. Seven counts standby as three, as if all its "
                    "words differed."},
            {"q": "According to the pattern Ubiquitous Language, what should a team do "
                  "when it settles on a better word for a concept?",
             "a": ["Add the new word to the glossary beside the old one",
                   "Treat it as a change to the model, and change the code's names "
                   "along with the talk",
                   "Use it in speech but keep the code's names stable",
                   "Ask the bilingual members to translate it"],
             "c": 1,
             "why": "The pattern's statement asks the team to carry a new word "
                    "into the code's names at once, and to treat a change in the "
                    "language as a change to the model. "
                    "Keeping two words is the translation the pattern removes."},
            {"q": "In One Team, One Language, what does Evans conclude when capable "
                  "domain experts cannot understand the model?",
             "a": ["The experts need training in objects",
                   "Something is wrong with the model",
                   "The developers should keep a separate model for the experts",
                   "Requirements should be collected only in the experts' terms"],
             "c": 1,
             "why": "He lists the usual reasons for shielding the experts, too abstract, "
                    "they don't understand objects, collect requirements in their "
                    "terms, and dismisses them; a domain expert can think deeply about "
                    "the field, so a model such an expert cannot follow is at fault."},
            {"q": "On the preset <code>one-language</code>, the code's class order is "
                  "renamed booking. What does the lab then count?",
             "a": ["0 translations, 6 concepts named alike",
                   "1 translation, 5 concepts named alike",
                   "2 translations, 6 concepts named alike",
                   "0 translations, 5 concepts named alike"],
             "c": 0,
             "why": "The only translations left were the two pairs with the code on "
                    "booking. With the class renamed, all three audiences say booking, "
                    "so every one of the 6 concepts is named alike and no pair differs. "
                    "A rename removes both of that concept's translations at once, not "
                    "one."},
        ],
        "mistakes": [
            ("Keeping two vocabularies and a bilingual teammate to translate between them",
             "It works for a while, and Evans describes it fairly: a few people become "
             "bilingual. They also become bottlenecks, their translations are inexact, "
             "and the translation hides the moments when two people use one word for "
             "different things. On the lesson's illustration the experts' show is two "
             "concepts, and no one translating it would notice."),
            ("Treating a rename as cosmetic",
             "In the pattern a change in the language is a change to the model, so a "
             "class that keeps the old name is a part of the model that has not "
             "changed. The box office's order class is the one place where speech and "
             "code still disagree, and the lab's two remaining translations are the "
             "cost of leaving it."),
            ("Shielding the experts from the model as too abstract for them",
             "One Team, One Language answers each usual reason in turn. If the "
             "abstractions are too abstract for the experts, how does the team know "
             "they are sound? A capable expert can think deeply about the field, and a "
             "model such a person cannot follow is wrong. Lower-level users may need "
             "more concrete words, but the line between languages should never run "
             "between experts and developers."),
        ],
        "standard": (
            "Finish when you can count what a team's vocabularies cost and find the hidden double meaning.",
            "Given three audiences' names for a domain's concepts, count the "
            "translations, name the ambiguous word and its two concepts, and say which "
            "rename in the code would remove the most."
        ),
        "note": (
            "The lab compares names as words. It cannot hear whether a sentence in the "
            "language flows or jars, which is the test Modeling Out Loud relies on, "
            "and it cannot tell when two concepts should become one; that is a change "
            "to the model, made by the team."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 2, Documents and Diagrams (PDF pp. 19-20 of the operator's copy),
    # Written Design Documents (pp. 20-22), Executable Bedrock (p. 22),
    # Explanatory Models (pp. 22-24).
    # Quotes: PDF p. 20, 9 words; PDF p. 21, 12 words; quotes.py OK.
    # Lesson total: 21 words.
    {
        "slug": "documents-and-explanatory-models",
        "title": "Documents, Diagrams and Explanatory Models",
        "module": "Chapter 2 · Communication and the Use of Language",
        "one_line": "Diagrams that anchor a conversation, documents that say what the code cannot, and the test that a document still speaks the team's language.",
        "summary": (
            "The second half of Chapter 2: what diagrams are good for and what they "
            "cannot say, two guidelines for a written design document, the case for "
            "and against letting the code be the only document, and explanatory "
            "models kept apart from the one that drives the code. Read a bike-share's "
            "design document against the words its team speaks and the names in its "
            "code, and find the stale terms."
        ),
        "key": [
            "the model is not the diagram",
            "small diagrams anchor talk",
            "documents complement code and speech",
            "a document must work for a living",
            "test it against the spoken language",
            "explanatory models stay out of code",
        ],
        "key_label": "Documents and diagrams in six lines",
        "concepts_intro": (
            "Three terms. The first two are Chapter 2's, the third the lab's."
        ),
        "concepts": [
            ("A design document",
             "Writing that explains the model's concepts, helps a reader find a way "
             "through the code, and shows how the model is meant to be used. Evans "
             "prescribes no set of documents, only two tests for any one."),
            ("Explanatory model",
             "A picture or description of the domain made to teach it, not to drive "
             "the code: a timeline, a map, the experts' own sketch. It may cover more "
             "than the software needs, and is best not drawn in UML."),
            ("A stale term",
             "In this lesson, a document's word for a concept where the team's speech and "
             "the code agree on another. The document was right once, and the "
             "language moved on without it."),
        ],
        "read_title": "The chapter's guidelines first, then the document, then the count",
        "read_intro": (
            "Read Chapter 2 from Documents and Diagrams to its end in your own copy "
            "first. The lesson sets out the two guidelines and then holds one design "
            "document to them."
        ),
        "body": [
            ("p", "&ldquo;Always remember that the model is not the diagram.&rdquo; "
                  "Evans writes it at the close of Documents and Diagrams, in the "
                  "second half of Chapter 2. This lesson reads that section, Written "
                  "Design Documents with its two guidelines, Executable Bedrock, and "
                  "Explanatory Models."),
            ("p", "Evans draws constantly in meetings, mostly class diagrams and "
                  "object interactions, and he gives diagrams their due: UML is good "
                  "at relationships and fair at interactions. A sketch of a handful of "
                  "objects, three to five, at the centre of the question keeps a discussion focused "
                  "and puts everyone on the same names, and it changes as fast as the "
                  "talk does. The trouble starts when a diagram tries to hold the "
                  "whole model. It becomes too complete to read, and still leaves "
                  "out half the story: what the concepts mean and what the objects "
                  "are for, which no box and line can state. He has seen no attempt "
                  "to generate code from UML that helped."),
            ("p", "So he turns the usual arrangement inside out. Rather than a "
                  "diagram annotated with text, he writes text illustrated with a "
                  "few small, simplified diagrams of the parts that matter, and lets "
                  "the code hold the detail, since well-written Java says as much as "
                  "UML in its own way. The diagrams in his book are of that kind: "
                  "skeletons of ideas, not specifications."),
            ("p", "Written Design Documents grants that a team of any size needs "
                  "some writing that holds still, and that writing tends to fall "
                  "behind the code and the language. Its first guideline is that "
                  "documents should complement code and speech. Evans states the "
                  "Extreme Programming position fairly: running code does not lie, "
                  "comments and documents drift, and relying on code keeps it clean. "
                  "But code can bury a reader in detail, its behaviour is exact "
                  "without being obvious, and developers are not the only readers. "
                  "&ldquo;A document shouldn't try to do what the code already does "
                  "well.&rdquo; It should give meaning, the large structure and the "
                  "core."),
            ("p", "The second guideline, Documents Should Work for a Living and Stay "
                  "Current, comes with a test, and the test is the language. Is the "
                  "document written in the words the team speaks now, and in the "
                  "words of the code? If its terms never turn up in conversation or "
                  "in the code, it is not doing its job. If the language moves on "
                  "and the document does not, it could be archived as history: left in "
                  "use it may confuse, and if it plays no important part, keeping it "
                  "current by willpower is wasted effort."),
            ("p", "Executable Bedrock returns to the code-only position and qualifies "
                  "it. The behaviour of code cannot be argued with, but its message "
                  "can be wrong: a method's name can be vague, misleading or out of "
                  "date, and only discipline keeps code saying what it does. Still, "
                  "code is closer to the ground than any other document, and it must "
                  "use the same language as the requirements and the team."),
            ("p", "Explanatory Models ends the chapter. One model should drive the "
                  "code, the design and the talk, but other models can teach the "
                  "domain, and may range wider than the code's model, which must be "
                  "pared to what the software needs. They are better not drawn as "
                  "object models, so no one mistakes them for the design. Evans's "
                  "example sets a class diagram of a shipping route beside a "
                  "picture of the same route as a sequence of handling, storage and "
                  "transport, which does not match the classes in detail, and which, "
                  "read beside the class diagram, makes both easier to follow."),
            ("p", "Now a domain of the lesson's own: a city bike-share, whose design "
                  "document was written at launch a year ago. Each record is a "
                  "concept, then the document's term, the word the team speaks now, "
                  "and the code's name, with a dash where one of them has no name."),
            ("code", _lines(BIKES_OLD_DOC)),
            ("p", "On the preset <code>last-years-document</code> the lab finds 7 "
                  "concepts, 2 named alike by all three, and the translations fall "
                  "where the document parts company: rental for a ride, "
                  "redistribution for rebalancing, subscription for a membership, "
                  "two translations each, 6 in all, where speech and code agree and "
                  "the document alone differs. Those three are the stale terms. The tile "
                  "for names missing shows two different gaps. The document has no "
                  "word for the day pass, a product added after launch, so it cannot "
                  "help anyone with it. The code has no name for the morning peak, "
                  "and should not: the flow of riders downhill before nine is an "
                  "explanatory model the team uses to reason about rebalancing, not a "
                  "class."),
            ("p", "The preset <code>revised-document</code> is the document after a "
                  "morning's work: the three stale terms replaced and a paragraph on "
                  "the day pass added. The lab finds 6 concepts named alike and no "
                  "translation between document, speech and code on any concept all "
                  "three name; the only gap left is the code's, on the morning peak, "
                  "by design. Whether the document was worth that morning is Evans's "
                  "second guideline, and the count cannot answer it."),
            ("h3", "Exercise"),
            ("code", _lines(BIKES_EXERCISE)),
            ("p", "Four concepts from the bike-share's repair workshop, with the "
                  "document's term, the spoken word and the code's name in that "
                  "order. By hand, count the translations, and name the stale "
                  "document terms: those where speech and code agree and the "
                  "document differs. Say what is different about the battery swap."),
            ("p", "A document is tested against the code. The next lesson, "
                  "Model-Driven Design and Hands-On Modelers, reads Chapter 3's case "
                  "that the code must be the model."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "glossary",
            "audiences": "document speech code",
            "preset": "last-years-document",
            "presets": [
                {"id": "last-years-document",
                 "label": "The design document written at launch",
                 "audiences": "document speech code",
                 "terms": BIKES_OLD_DOC,
                 "expect": {"dlnConcepts": "7", "dlnAlike": "2: station, dock", "dlnTranslations": "6",
                            "dlnMissing": "2: day_pass (document); morning_peak (code)"}},
                {"id": "revised-document",
                 "label": "The same document, brought up to date",
                 "audiences": "document speech code",
                 "terms": BIKES_NEW_DOC,
                 "expect": {"dlnTranslations": "0", "dlnMissing": "1: morning_peak (code)",
                            "dlnAlike": "6: station, dock, trip, rebalancing, membership, day_pass"}},
            ],
            "panel_title": "A design document against speech and code",
            "panel_intro": _LANG_INTRO,
        }),
        "steps_title": "Holding a document to the language",
        "steps_intro": "Four steps, the last of them on a document you know.",
        "steps": [
            ("List the document's terms",
             "Write down each concept the document defines or names, with the term it "
             "uses."),
            ("Set speech and code beside them",
             "For each, write the word the team says now and the name in the code, "
             "with a dash where either has none."),
            ("Mark the stale and the missing",
             "Mark each term where speech and code agree against the document, each "
             "concept the document cannot name, and each the code has no name for and "
             "should not."),
            ("Do it on a document you know",
             "Take a design document or wiki page from a project you work on, list "
             "five of its terms, and count the stale ones. Decide whether to update "
             "it or archive it, and write down why."),
        ],
        "worked": {
            "title": "Three stale terms in last year's document",
            "intro": [
                "Read <code>last-years-document</code> row by row.",
            ],
            "lines": [
                "station and dock: all three alike",
                "trip: document rental, others ride: stale",
                "rebalancing: document redistribution: stale",
                "membership: document subscription: stale",
                "day pass: no document term: missing",
                "morning peak: no class: explanatory",
                "stale terms: 3, each 2 translations",
            ],
            "after": [
                "The two gaps look alike in the table and mean opposite things. The "
                "document's gap is a failure of the second guideline: the language "
                "moved and the document did not. The code's gap is the chapter's "
                "advice followed: an explanatory model kept out of the design.",
            ],
        },
        "quiz_title": "Diagrams, documents and the stale term",
        "quiz": [
            {"q": "In the exercise, which document terms are stale, the speech and the "
                  "code agreeing against the document?",
             "a": ["`fault_ticket` and `electric_bike`",
                   "`fault_ticket`, `electric_bike` and `charging`",
                   "`charging` only",
                   "`electric_bike` only"],
             "c": 0,
             "why": "For the fault report and the e-bike, speech and code agree and "
                    "the document alone differs, so `fault_ticket` and `electric_bike` are "
                    "stale, 2 translations each. The battery swap is different: "
                    "`charging`, `battery_swap` and `swap` all differ, 3 translations, so the "
                    "code lags the spoken word as well and renaming the document alone "
                    "would not settle it. Repair is alike everywhere. The total is "
                    "2 + 0 + 2 + 3 = 7."},
            {"q": "What, according to Documents and Diagrams, can a UML diagram not "
                  "convey?",
             "a": ["The relationships between objects",
                   "The names of the objects",
                   "What the concepts mean and the purpose each object serves",
                   "Interactions between objects"],
             "c": 2,
             "why": "Evans rates UML well for showing how objects relate and "
                    "passably for showing how they interact, and a sketch puts everyone on the same names. What "
                    "it cannot state is the meaning of the concepts and the purpose of "
                    "the objects, which falls to text and talk."},
            {"q": "In Written Design Documents, what does Evans advise for a document "
                  "the language has left behind and that plays no important role?",
             "a": ["Update it by discipline, so that it never misleads",
                   "Delete it at once",
                   "Retire it to an archive: in use it misleads, and upkeep "
                   "without a role is wasted",
                   "Generate it from the code"],
             "c": 2,
             "why": "Evans's advice is that such a document may be put away as "
                    "history, since one kept in use can mislead its readers, and that "
                    "maintaining a document with no real part to play by effort of "
                    "will is a waste. He does not say to delete it."},
            {"q": "In Executable Bedrock, what does Evans grant the code-only position, "
                  "and what does he hold against it?",
             "a": ["Code's behaviour is inescapable, but its names and organisation can "
                   "still mislead",
                   "Code never misleads, so no other document is needed",
                   "Code is always obvious, but it is too long to read",
                   "Tests are rigorous, so method names do not matter"],
             "c": 0,
             "why": "He grants that what code does cannot be argued with and that "
                    "a test's checks are exact; but a method's name may be vague, "
                    "wrong or stale beside its body, and only discipline keeps the "
                    "names and layout of the code telling the truth."},
        ],
        "mistakes": [
            ("Taking the diagram for the model",
             "The diagram exists to communicate and explain the model, Evans says, and "
             "the code holds the detail. A diagram that tries to show every object is "
             "too complete to read and still cannot say what the concepts mean. The "
             "bike-share's morning peak is a picture the team reasons with that is "
             "deliberately not in the code at all."),
            ("Keeping every document current by discipline",
             "Evans's second guideline is that a document must work for a living. If "
             "its terms never reach the team's talk or code, it is not working; if the "
             "language moves on without it, it can be archived as history. Keeping a "
             "document current by willpower when it plays no real part, he says, "
             "wastes effort. On the lesson's illustration the stale terms are the "
             "signal to decide, not an order to rewrite."),
            ("Concluding that the code is the only document a team needs",
             "Evans states the Extreme Programming position at its strength and then "
             "qualifies it: code's behaviour is exact without being obvious, it can "
             "bury a reader in detail, its names can mislead, and developers are not "
             "its only readers. Documents should do what code does not do well: give "
             "meaning, show the large structure, point to the core."),
        ],
        "standard": (
            "Finish when you can hold a design document to the team's language.",
            "Given a document's terms, the words spoken now and the code's names, count "
            "the translations, name the stale terms and the gaps, and say which gap is "
            "a fault and which is by design."
        ),
        "note": (
            "The lab finds where a document's words differ from speech and code. It "
            "cannot say whether the document is read, whether it explains anything "
            "the code does not, or whether it is worth the upkeep; that is Evans's "
            "test, and only the team can apply it."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 3, opening (PDF p. 25 of the operator's copy), Model-Driven Design
    # (pp. 26-28), Modeling Paradigms and Tool Support (pp. 28-33), Letting the
    # Bones Show (p. 33), Hands-On Modelers (pp. 34-35).
    # Quotes: PDF p. 27, 20 words; PDF p. 35, 9 words; quotes.py OK.
    # Lesson total: 29 words.
    {
        "slug": "model-driven-design-and-hands-on-modelers",
        "title": "Model-Driven Design and Hands-On Modelers",
        "module": "Chapter 3 · Binding Model and Implementation",
        "one_line": "One model for analysis and for the code, mapped so literally that changing the code can change the model, and modelled by people who code.",
        "summary": (
            "Chapter 3: why a model on paper that the code does not follow is of little "
            "use, the pattern Model-Driven Design that binds them, the tools that make "
            "the binding possible, what happens when the user is shown a different "
            "model, and why the modeller must code. Map a library's lending code to "
            "modules two ways and count how far each change in the model reaches."
        ),
        "key": [
            "a single model for analysis and design",
            "the code expresses the model",
            "change the code: change the model",
            "object languages make the map literal",
            "show users the model, not an illusion",
            "modelers code; coders model",
        ],
        "key_label": "Model-Driven Design in six lines",
        "concepts_intro": (
            "Three terms. The first two are the chapter's patterns, the third the "
            "lab's."
        ),
        "concepts": [
            ("Analysis model",
             "A model of the domain made to understand it, with no thought for the part "
             "it will play in software, and usually handed to other people to design "
             "from. Evans's argument is against keeping one apart from the design."),
            ("Model-Driven Design",
             "The pattern of one model serving both analysis and design: part of the "
             "code is the model, readably, and the model is reshaped until it can "
             "be."),
            ("Modules a change reaches",
             "In the lab, the number of distinct modules holding the pieces of code a "
             "change to the model touches. One module means the change stays where the "
             "concept lives."),
        ],
        "read_title": "The chapter's argument first, then the patterns, then the count",
        "read_intro": (
            "Read Chapter 3 in your own copy first. The lesson reads its opening "
            "stories as evidence, the two patterns as tools, and then counts what "
            "binding the code to the model does to one library's changes."
        ),
        "body": [
            ("p", "&ldquo;MODEL-DRIVEN DESIGN discards the dichotomy of analysis model "
                  "and design to search out a single model that serves both "
                  "purposes.&rdquo; That is the pattern Model-Driven Design, the heart "
                  "of Chapter 3, Binding Model and Implementation. This lesson reads "
                  "the chapter whole: its opening, Model-Driven Design, Modeling "
                  "Paradigms and Tool Support, Letting the Bones Show, and Hands-On "
                  "Modelers."),
            ("p", "The chapter opens with two projects. On the first, analysts and "
                  "experts had spent months on a detailed model, printed across a "
                  "wall; it captured real knowledge, but its tangle of associations "
                  "gave no units the developers could store and change safely, so "
                  "they concluded that a conceptual model could not be the basis of "
                  "their design and built an ad hoc one. The second project was "
                  "rewriting an old program that had never had a model at all. The "
                  "two ended in much the same place: working, bloated software whose "
                  "code said little about what the system was for."),
            ("p", "Evans's diagnosis is the analysis model. Many methods ask for one, "
                  "made to understand the domain without regard to software, and "
                  "then a design loosely related to it. Much of what the analysis "
                  "learned is lost when coding begins; the analysis misses things "
                  "only implementation reveals, so it is soon abandoned; and keeping "
                  "a complex mapping between it and the design current is, in "
                  "practice, impossible. Software without a concept at its "
                  "foundation does useful things without explaining them."),
            ("p", "The pattern binds the two. Some part of the code is written to be "
                  "the model, class for concept, so that anyone can see which is "
                  "which; when the model resists that, the model is reworked as well "
                  "as the code, and deepened as it goes; and one model has to carry "
                  "both jobs and the team's language too. When a model cannot be implemented "
                  "practically, or does not express the domain's key concepts, the "
                  "team looks for another. Because the code now expresses the "
                  "model, editing the code can amount to editing the model, and the "
                  "rest of the project's work has to follow such an edit."),
            ("p", "Modeling Paradigms and Tool Support says the binding needs a "
                  "language that can express the model's constructs directly. Object "
                  "languages can, and so can Prolog for a model of rules and facts; a "
                  "procedural language such as C has no modelling paradigm to match, "
                  "although Fortran suits a domain that is mathematics. The example "
                  "is the circuit-board domain again: engineers who wanted rules "
                  "applied to whole buses of nets had written scripts that sorted and "
                  "pattern-matched the tool's files, inferring the bus without ever "
                  "naming it. Evans's model makes the bus an object that carries "
                  "rules, and the rest becomes nearly trivial and testable unit by "
                  "unit."),
            ("p", "Letting the Bones Show turns to the user. A browser's bookmarks, "
                  "presented as a list of names but stored as files, reject or "
                  "silently alter names a file system will not accept, and the user "
                  "is left asking which file is meant. Evans's remedy is a single "
                  "model: either show the user that bookmarks are files, or store "
                  "them so that they follow the rules of what they name. Hands-On "
                  "Modelers then tells his own story: kept from coding by a "
                  "management that thought modellers should model, he saw a sound "
                  "model lose its intent in the hand-off and its feedback arrive "
                  "months late, until the developers built without it. "
                  "&ldquo;Programmers are modelers, whether anyone likes it or "
                  "not.&rdquo; From this the pattern follows: whoever helps shape the model "
                  "also works in the code, and whoever works in the code learns to "
                  "make it say what the model says."),
            ("p", "Now a domain of the lesson's own: a public library's lending. Nine "
                  "pieces of code each carry part of the model: a loan's due date, "
                  "renewal and overdue rule; a hold's queue, expiry and notice; a "
                  "fine's daily rate, cap and waiver. Each record gives a piece, its "
                  "module when the code follows the model (loans, holds, fines), and "
                  "its module in a design built screen by screen and job by job, as "
                  "a team working from a separate analysis model might have built "
                  "it."),
            ("code", _lines(LENDING_ELEMENTS)),
            ("p", "Four changes to the model touch the code: a shorter loan period, "
                  "a pickup window for holds, a cap on fines per item, and a rule "
                  "that a loan cannot be renewed while someone holds the item. On "
                  "the preset <code>lending-changes</code>, with the code following "
                  "the model, the changes reach 1, 1, 1 and 2 modules, 5 module "
                  "touches in all, 3 changes confined to one module, and the largest "
                  "is the renewal rule, at 2. With the code following screens and "
                  "jobs, they reach 2, 2, 3 and 2, 9 touches in all, none confined to "
                  "one module, and the largest is the fine cap, spread over the "
                  "nightly job, the checkout screen and the desk screen."),
            ("p", "Two things keep that count honest. The renewal rule joins two "
                  "concepts, loans and holds, and reaches two modules either way; "
                  "following the model does not make a change local when the model "
                  "says it is not. And the preset <code>model-drifts</code> shows "
                  "what Hands-On Modelers warns of: a developer who did not see that "
                  "changing code changes the model has put the fine cap into the "
                  "loans code to save a call. The fine-cap change now reaches 2 "
                  "modules, and the total rises from 5 to 6. The model is weaker by "
                  "one misplaced piece, and nothing in the code says so."),
            ("h3", "Exercise"),
            ("code", _lines(LENDING_EXERCISE)),
            ("p", "A fifth change: student loans, with their own due date, their own "
                  "daily fine and their own renewal limit, touching the three pieces "
                  "listed. Using the module map above, count by hand the modules the "
                  "change reaches when the code follows the model and when it follows "
                  "screens and jobs. Then put the records in place of the lab's changes."),
            ("p", "This closes Part I. The next course, The Building Blocks of a "
                  "Model-Driven Design, begins with Layered Architecture, the first "
                  "of the patterns that let the code express the model."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "packagings": 2,
            "names": ["by concept", "by screen and job"],
            "preset": "lending-changes",
            "presets": [
                {"id": "lending-changes",
                 "label": "Four model changes, code by concept against code by screen",
                 "elements": LENDING_ELEMENTS,
                 "changes": LENDING_CHANGES,
                 "expect": {"dmoTotal": "5", "dmoTotal2": "9",
                            "dmoPer": "loan_period 1, hold_pickup_window 1, fine_cap_per_item 1, renew_with_hold 2",
                            "dmoPer2": "loan_period 2, hold_pickup_window 2, fine_cap_per_item 3, renew_with_hold 2",
                            "dmoConfined": "3 of 4: loan_period, hold_pickup_window, fine_cap_per_item",
                            "dmoConfined2": "0 of 4",
                            "dmoLargest": "renew_with_hold, 2 modules",
                            "dmoLargest2": "fine_cap_per_item, 3 modules"}},
                {"id": "model-drifts",
                 "label": "The same, with the fine cap moved into the loans code",
                 "elements": LENDING_DRIFTED,
                 "changes": LENDING_CHANGES,
                 "expect": {"dmoTotal": "6", "dmoTotal2": "9",
                            "dmoPer": "loan_period 1, hold_pickup_window 1, fine_cap_per_item 2, renew_with_hold 2",
                            "dmoConfined": "2 of 4: loan_period, hold_pickup_window"}},
            ],
            "panel_title": "How far a change in the model reaches",
            "panel_intro": _CHANGE_INTRO,
        }),
        "steps_title": "Mapping the model to the code",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("List the model's pieces in the code",
             "For each concept of the model, list the pieces of code that carry its "
             "rules and data."),
            ("Write down where each piece lives",
             "Give each piece its module, package or file, as the code is organised "
             "now."),
            ("Trace recent changes through the map",
             "For each of a few recent changes to what the experts asked for, list the "
             "pieces it touched and count the modules they are in."),
            ("Do it on your own code",
             "Take three changes from a system you work on, count the modules each "
             "reached, and say for the one that reached the most whether the code or "
             "the model divided the concept."),
        ],
        "worked": {
            "title": "Five touches by concept, nine by screen",
            "intro": [
                "Count the modules each change reaches in <code>lending-changes</code>.",
            ],
            "lines": [
                "loan period: 1 by concept, 2 by screen",
                "hold pickup window: 1 by concept, 2 by screen",
                "fine cap per item: 1 by concept, 3 by screen",
                "renew with hold: 2 by concept, 2 by screen",
                "total touches: 5 by concept, 9 by screen",
                "confined to one module: 3 by concept, 0 by screen",
            ],
            "after": [
                "The nightly job appears in three of the four changes on the right, "
                "because it holds a piece of every concept. That is the shape Evans "
                "finds in the scripts that inferred a bus from a sort of net names: the "
                "concept the engineers think in is in none of the code, only implied "
                "by where things happen to sit.",
            ],
        },
        "quiz_title": "One model, its tools and its modelers",
        "quiz": [
            {"q": "In the exercise (student loans touching `loan.due_date`, "
                  "`fine.daily_rate` and `loan.renewal`), how many modules does the change "
                  "reach with the code by concept, and with the code by screen and job?",
             "a": ["2 and 3", "3 and 3", "1 and 3", "2 and 2"],
             "c": 0,
             "why": "By concept, `loan.due_date` and `loan.renewal` are in loans and "
                    "`fine.daily_rate` in fines: 2 modules. By screen and job, they are in "
                    "the checkout screen, the renewal screen and the nightly job: 3. "
                    "The change joins two concepts, so even the model-driven packaging "
                    "cannot keep it in one module."},
            {"q": "Why, in Chapter 3's account, is a pure analysis model usually "
                  "abandoned soon after coding starts?",
             "a": ["Analysts are not skilled enough to build one",
                   "It is made without design in mind, misses what only implementation "
                   "reveals, and keeping a mapping to the design current is not "
                   "worth the cost",
                   "Object languages cannot express it",
                   "The experts reject it"],
             "c": 1,
             "why": "Evans grants the analysts care and skill; his opening story's model "
                    "was the result of extensive collaboration with experts. The "
                    "failure is structural: an up-front model goes deep on the wrong "
                    "subjects, discoveries come during implementation, and the mapping "
                    "between two loosely connected models is not cost-effective to "
                    "maintain."},
            {"q": "In Letting the Bones Show, what does Evans recommend for a feature "
                  "whose user-facing model differs from the implementation's?",
             "a": ["Hide the implementation behind a friendlier model",
                   "Keep one model: show the user the implementation's, or change the "
                   "implementation to follow the user's",
                   "Document both models for the user",
                   "Let the user choose which model to see"],
             "c": 1,
             "why": "Of the bookmarks stored as files, he offers both remedies: expose "
                    "the fact that they are files, or store them another way so that "
                    "they obey their own rules. Either gives one model. An illusion "
                    "over a different model, he says, confuses unless it is perfect."},
            {"q": "On the preset <code>model-drifts</code>, which figure changes from "
                  "<code>lending-changes</code>, with the code following the model?",
             "a": ["The renewal rule now reaches 3 modules",
                   "The fine-cap change reaches 2 modules, and the total rises from 5 "
                   "to 6",
                   "No figure changes, since `fine.cap` is still a fine",
                   "The loan period change reaches 2 modules"],
             "c": 1,
             "why": "Only `fine.cap` moved, from fines to loans, so only the change that "
                    "touches it is affected: `fine.daily_rate` and `fine.waiver` are still "
                    "in fines, so the fine cap now reaches fines and loans, 2 instead of "
                    "1, and the total goes from 5 to 6. The loan period change touches "
                    "`loan.due_date` and `loan.overdue`, both still in loans."},
        ],
        "mistakes": [
            ("Keeping the analysis model apart so that implementation cannot muddy it",
             "That is the reason methods give for it, and Evans states it fairly. His "
             "answer is that a pure analysis model fails even at understanding, "
             "because crucial discoveries come during implementation, and that it is "
             "abandoned soon after coding starts, with much of its ground covered "
             "again. Model-Driven Design asks for one model that works as analysis "
             "and as design; on the lesson's illustration the code that follows its "
             "model keeps three of four changes in one module."),
            ("Treating modelling as a senior role that should not touch the code",
             "Hands-On Modelers is Evans's own case against it: forbidden to program, "
             "he watched a sound model lose its intent in the hand-off and its "
             "feedback arrive too late, until the developers built without it. The "
             "pattern does not abolish specialised roles; it says that modelling and "
             "coding cannot be handed to different people: the modeller works in the "
             "code, and the programmer makes the code carry the model."),
            ("Giving users a friendlier model than the one underneath",
             "Letting the Bones Show argues that an illusion of another model confuses "
             "users unless it is perfect, as the bookmarks stored as files show when a "
             "name breaks a file-system rule. A single model, shown to the user or "
             "changed to fit the user's, is Evans's remedy."),
        ],
        "standard": (
            "Finish when you can map a model to its code and trace a change through the map.",
            "Given the pieces of code that carry a model, their modules in two "
            "packagings, and the pieces a change touches, count the modules the change "
            "reaches in each and say which packaging follows the model."
        ),
        "note": (
            "The lab counts modules a change reaches on the map it is given. It cannot "
            "tell whether the map follows the model or only claims to, whether a "
            "module's name matches the concept inside it, or what a change costs in "
            "a module it reaches; Evans's test is whether the code says what the model "
            "says."
        ),
    },
]
