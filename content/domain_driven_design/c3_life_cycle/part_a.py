"""The Life Cycle of a Domain Object, lessons 1-4 -- Chapter 6.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), Chapter 6, The Life Cycle of a Domain Object: the
Aggregates pattern with its purchase-order example, Factories and
Repositories, with Designing Objects for Relational Databases. Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter,
section and pattern. Every quotation is copied from that copy and checked with
quotes.py. The models and the code are written for these lessons: none of the
book's listings, diagrams or example data is reproduced, and no lab uses one of
the book's example domains. Each snippet is one constant below. The design is
docs/domain-driven-design/PLAN.md, section C, Course 3.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# 3.1 Aggregates: the clinic's Patient root (written for the lesson).
PATIENT_ROOT = """// The patient is the root: allergies are reached only through it.
public class Patient {
    private final PatientId id;
    private final List<Allergy> allergies = new ArrayList<>();
    private EmergencyContact contact;

    public void recordAllergy(String substance, Severity severity) {
        if (hasAllergyTo(substance)) {
            throw new IllegalStateException("already recorded");
        }
        allergies.add(new Allergy(allergies.size() + 1, substance, severity));
    }

    public boolean hasAllergyTo(String substance) {
        return allergies.stream().anyMatch(a -> a.isTo(substance));
    }

    public List<Allergy> allergies() {
        return Collections.unmodifiableList(allergies);
    }
}"""

# 3.2 Aggregate invariants: the cookery class root (written for the lesson).
COOKERY_CLASS = """// One class session; the parties booked into it are inside its boundary.
public class CookeryClass {
    private final ClassId id;
    private final int places;
    private final Map<PartyName, Integer> parties = new HashMap<>();

    public void resize(PartyName party, int people) {
        int others = taken() - parties.getOrDefault(party, 0);
        if (others + people > places) {
            throw new IllegalArgumentException("over " + places + " places");
        }
        parties.put(party, people);
    }

    int taken() {
        return parties.values().stream().mapToInt(Integer::intValue).sum();
    }
}"""

# 3.3 Factories: the seed bank's accession factory (written for the lesson).
ACCESSION_FACTORY = """public class AccessionFactory {
    private final AccessionNumbers numbers;   // issues new numbers

    public Accession newAccession(SeedSample sample, GerminationTest test) {
        if (sample.seeds() < 400) {
            throw new AccessionRefused("fewer than 400 seeds");
        }
        if (test.percent() < 70) {
            throw new AccessionRefused("germination under 70 percent");
        }
        if (sample.moisturePercent() > 8) {
            throw new AccessionRefused("too damp to store");
        }
        if (!sample.originKnown()) {
            throw new AccessionRefused("origin not recorded");
        }
        return new Accession(numbers.next(), sample, test);
    }
}"""

ACCESSION_RECONSTITUTE = """// Rebuilding a stored lot: its number comes in, and nothing is refused.
public Accession reconstitute(AccessionRow row) {
    Accession lot = new Accession(new AccessionNumber(row.number()),
            row.sample(), row.test());
    if (row.sample().seeds() < 400) {
        lot.flagForRegeneration();   // stored before the rule: repair it
    }
    return lot;
}"""

# 3.4 Repositories: the bike-share's repository (written for the lesson).
BIKE_REPOSITORY = """public interface BikeRepository {
    Optional<Bike> withNumber(BikeNumber number);
    List<Bike> satisfying(BikeSpecification spec);
    int countSatisfying(BikeSpecification spec);
    void add(Bike bike);
    void remove(Bike bike);
}

// The workshop's question: docked, and either worn or reported faulty.
public class DueForService implements BikeSpecification {
    public boolean isSatisfiedBy(Bike b) {
        return b.isDocked() && (b.kilometres() >= 800 || b.openFaults() >= 1);
    }
}"""


# ---------------------------------------------------------------- lab data

# 3.1: the clinic model, written for the lesson.
_CLINIC_OBJECTS = (
    "Patient, patient, yes; Allergy, patient, no; Contact, patient, no; "
    "Appointment, appointment, yes; Note, appointment, no; Doctor, doctor, yes"
)
_CLINIC_REFS = (
    "Patient, Allergy; Patient, Contact; Appointment, Patient; "
    "Appointment, Doctor; Appointment, Note; Note, Doctor; Reception, Appointment"
)
_CLINIC_SHORTCUT_REFS = _CLINIC_REFS + "; Pharmacy, Allergy; Note, Allergy"

# 3.2: the cookery school's Saturday class, written for the lesson.
_CLASS_ITEMS = "walsh, 4; okafor, 3; lin, 2"
_CLASS_EDITS = "1, pat, okafor, 5; 2, sam, lin, 4; 4, pat, okafor, 6"
_CLASS_SAME_PARTY = "1, pat, okafor, 5; 2, sam, okafor, 4; 4, pat, okafor, 6"

# 3.3: the seed bank's accession rule and three requests, written for the lesson.
_LOTS = (
    "sound-lot, seeds=1200, germination=88, moisture=6, origin=known; "
    "damp-lot, seeds=900, germination=81, moisture=11, origin=known; "
    "small-lot, seeds=150, germination=92, moisture=7, origin=unknown"
)
_ACCESSION_SPEC = "seeds >= 400 and germination >= 70 and moisture <= 8 and origin = known"

# 3.4: the bike-share's fleet, written for the lesson.
_FLEET = (
    "b101, status=docked, km=950, faults=0; b102, status=docked, km=300, faults=2; "
    "b103, status=riding, km=1200, faults=1; b104, status=docked, km=420, faults=0; "
    "b105, status=docked, km=799, faults=0"
)
_DUE_FOR_SERVICE = "status = docked and (km >= 800 or faults >= 1)"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 6, opening (PDF pp. 70-71 of the operator's copy); Aggregates
    # (pp. 71-74): the deletion and concurrency problems (pp. 71-72), root,
    # boundary and local identity, Siegel's footnote (p. 72), the car and its
    # tires (pp. 72-73), invariants within and across aggregates (p. 73), the
    # rules and the boxed statement (pp. 73-74).
    # Quote: PDF p. 72 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "aggregates",
        "title": "Aggregates",
        "module": "Chapter 6 · The Life Cycle of a Domain Object",
        "one_line": "A cluster of objects changed as one unit, with one root that the outside world may hold and a boundary that says where the cluster stops.",
        "summary": (
            "Chapter 6 opens the life cycle of a domain object with the pattern "
            "the rest of the chapter stands on. Read Evans's case for drawing a "
            "boundary round a group of objects, the rules that make the boundary "
            "real, and then count, on a clinic's model, the references that cross "
            "a boundary, the ones that reach past a root, and what a delete takes "
            "with it."
        ),
        "key": [
            "a cluster changed as one unit",
            "one root entity, one boundary",
            "outside objects hold only the root",
            "insiders have local identity",
            "a delete takes the whole cluster",
            "rules across clusters may lag",
        ],
        "key_label": "Aggregates in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, all of them Evans's, from the Aggregates "
            "pattern in Chapter 6."
        ),
        "concepts": [
            ("Aggregate",
             "Objects bound together so that any change to their data is made to "
             "the group as a whole. It has a root and a boundary, and its rules are "
             "kept for the group, not object by object."),
            ("Root",
             "The one entity in an aggregate that has identity across the whole "
             "system and that objects outside may keep a reference to. Everything "
             "else inside is reached by starting at the root."),
            ("Boundary",
             "The line that says which objects belong to the aggregate. Entities "
             "inside it other than the root need identity only among their "
             "neighbours, because nothing outside can name them on their own."),
        ],
        "read_title": "The chapter's problem, the pattern, then the count",
        "read_intro": (
            "Read the opening of Chapter 6 and the Aggregates pattern, up to the "
            "purchase-order example, in your own copy first. The next lesson reads "
            "that example."
        ),
        "body": [
            ("p", "&ldquo;Put another way, how do we know where an object made up of "
                  "other objects begins and ends?&rdquo; Evans asks it in the middle "
                  "of the Aggregates pattern, the first of three in Chapter 6, The "
                  "Life Cycle of a Domain Object. The chapter's opening sorts objects "
                  "into the short-lived ones a constructor makes and the garbage "
                  "collector takes, which need no help, and the long-lived ones that "
                  "are stored, changed under rules and tied to many others. For those "
                  "he names two dangers: losing integrity over the object's life, and "
                  "burying the model under the machinery of managing that life. "
                  "Aggregates answer the first; Factories and Repositories, the next "
                  "two lessons' patterns, answer the second."),
            ("p", "The problem is a web with no edges. After the moves of the previous "
                  "course's Associations lesson, a typical model is still densely "
                  "connected, and Evans's small case is a delete. Remove a person from "
                  "the database and the name and birth date plainly go too; but the "
                  "address may be shared with others in the same house. Delete it and "
                  "their references dangle; keep it and stale addresses pile up. A "
                  "garbage collector might tidy the second case, he grants, but that "
                  "is a technical fix for what is really a gap in the model: nobody "
                  "has said what the person owns."),
            ("p", "Concurrency makes the gap expensive. Many users change many objects "
                  "at once, and some rules apply to a group of objects rather than to "
                  "one. Lock too little and two changes together can break such a "
                  "rule; lock too much and users block each other for nothing. "
                  "Database locks and tests can be arranged case by case, but Evans "
                  "calls those ad hoc fixes a distraction from the model. His claim "
                  "is that the scope of a change is a modelling question, and that a "
                  "good answer often needs domain knowledge such as how often "
                  "different kinds of object change."),
            ("p", "The pattern is a discipline he credits, in a footnote, to David "
                  "Siegel, who used it on projects in the 1990s without publishing "
                  "it. An aggregate is a cluster with a root and a boundary. The root "
                  "is a single entity, the only member outsiders may keep a reference "
                  "to; members may refer to one another freely. His illustration is a "
                  "repair shop's car, identified worldwide by its vehicle number, "
                  "whose tires are tracked for wear but never looked up on their own: "
                  "the car is the root and the tires sit inside its boundary. An "
                  "engine block with its own serial number, tracked apart from any "
                  "car, might instead be the root of an aggregate of its own."),
            ("p", "Then the rules, in the book's order and the lesson's words:"),
            ("ul", [
                "The root has identity across the system and is finally responsible "
                "for checking the aggregate's invariants. Other entities inside need "
                "identity only within the aggregate.",
                "Nothing outside may keep a reference to an inner object. The root may "
                "lend one out for the length of an operation, and may hand out a copy "
                "of a value object, which then has no tie to the aggregate.",
                "So only roots can be fetched straight from the database; everything "
                "else is reached by traversal from a root.",
                "Objects inside may refer to the roots of other aggregates.",
                "Deleting the root takes everything inside the boundary with it.",
                "After any committed change inside, all of the aggregate's rules are "
                "true.",
            ]),
            ("p", "An invariant, here, is a consistency rule that must be true whenever "
                  "data changes. Evans divides them by the boundary. A rule inside an "
                  "aggregate is enforced as each transaction completes. A rule that "
                  "spans aggregates is allowed to be out of date for a while, and is "
                  "brought back into line by events, a batch run or some other update "
                  "within an agreed time. Choosing the boundary is choosing which rules "
                  "get the first, strict treatment."),
            ("p", "In code the rules show as what the root does and does not expose. "
                  "The clinic's `Patient` below owns its allergies: a new one is "
                  "recorded through `recordAllergy`, which checks the patient's own "
                  "rule that a substance is recorded once, and the list goes out "
                  "read-only, for the caller to read and let go. If `Allergy` itself "
                  "had setters, a caller could still change one behind the root's "
                  "back; Evans's rule is about references held, and the code has to "
                  "make it hard to break."),
            ("code", _lines(PATIENT_ROOT)),
            ("p", "Now the count. The preset <code>clinic</code> states the clinic's "
                  "model as three aggregates: a patient with an allergy list and an "
                  "emergency contact, an appointment with its consultation note, and "
                  "a doctor. Seven references are listed, one of them from the "
                  "reception desk, an outside holder that is not an object of the "
                  "model. The lab counts 3 aggregates and 6 objects, 4 references "
                  "that cross a boundary (appointment to patient, appointment to "
                  "doctor, note to doctor, reception to appointment) and 0 that "
                  "reach a non-root. A note that names its doctor is allowed: an "
                  "object inside may hold another aggregate's root."),
            ("p", "The preset <code>shortcuts</code> adds two references a busy "
                  "programmer might add: the pharmacy system keeps a list of the "
                  "allergies it has checked, and the note points straight at the "
                  "allergy it discusses. Now 6 references cross a boundary, and the "
                  "lab lists 2 as violations, both into the patient's aggregate past "
                  "its root. Each is a place where the allergy could change, or be "
                  "removed, without the patient knowing, which is the blindsiding "
                  "the pattern exists to prevent."),
            ("p", "Deletes follow the boundary. On <code>delete-patient</code> the lab "
                  "removes 3 objects, the patient, the allergy and the contact, and "
                  "reports 1 reference left dangling: the appointment's reference to "
                  "the patient. That is not a failure of the pattern; it is the rule "
                  "that spans aggregates, which the model must handle in its own way, "
                  "by refusing the delete while appointments exist or by closing them "
                  "first. On <code>delete-allergy</code> the lab refuses: an allergy is "
                  "not a root, and it is removed through the patient or not at all."),
            ("h3", "Exercise"),
            ("ul", [
                "Objects (object, aggregate, root): Member, member, yes; Card, member, "
                "no; Hold, member, no; Loan, loan, yes; Renewal, loan, no; Copy, copy, "
                "yes.",
                "References (from, to): Loan, Member; Loan, Copy; Loan, Renewal; "
                "Member, Card; Member, Hold; Hold, Copy; Desk, Card; Overdues, "
                "Renewal.",
            ]),
            ("p", "A library's model, with two outside holders, the issue desk and the "
                  "overdues report. Count the references that cross a boundary and the "
                  "ones that reach a non-root, then say what deleting the member "
                  "removes and how many references it would leave dangling. Type the "
                  "model into the lab to check."),
            ("p", "The rules say where a cluster stops; they do not yet show why a "
                  "lock on the cluster matters. The next lesson, Aggregate Invariants "
                  "and Concurrent Change, reads the chapter's own example of two "
                  "users who each keep a rule and together break it."),
        ],
        "lab": ("dddkit", {
            "mode": "aggregate",
            "view": "boundary",
            "preset": "clinic",
            "presets": [
                {"id": "clinic",
                 "label": "A clinic: patient, appointment and doctor",
                 "objects": _CLINIC_OBJECTS,
                 "refs": _CLINIC_REFS,
                 "expect": {"dgrAggregates": "3: patient, appointment, doctor", "dgrObjects": "6", "dgrCrossing": "4", "dgrViolations": "0: none", "dgrRemoves": "no delete given", "dgrDangling": "no delete given"}},
                {"id": "shortcuts",
                 "label": "The same model with two shortcuts to an allergy",
                 "objects": _CLINIC_OBJECTS,
                 "refs": _CLINIC_SHORTCUT_REFS,
                 "expect": {"dgrAggregates": "3: patient, appointment, doctor", "dgrObjects": "6", "dgrCrossing": "6", "dgrViolations": "2: Pharmacy → Allergy, Note → Allergy", "dgrRemoves": "no delete given", "dgrDangling": "no delete given"}},
                {"id": "delete-patient",
                 "label": "Delete a patient",
                 "objects": _CLINIC_OBJECTS,
                 "refs": _CLINIC_REFS,
                 "delete": "Patient",
                 "expect": {"dgrAggregates": "3: patient, appointment, doctor", "dgrObjects": "6", "dgrCrossing": "4", "dgrViolations": "0: none", "dgrRemoves": "3: Patient, Allergy, Contact", "dgrDangling": "1: Appointment → Patient"}},
                {"id": "delete-allergy",
                 "label": "Delete one allergy directly",
                 "objects": _CLINIC_OBJECTS,
                 "refs": _CLINIC_REFS,
                 "delete": "Allergy",
                 "expect": {"dgrAggregates": "3: patient, appointment, doctor", "dgrObjects": "6", "dgrCrossing": "4", "dgrViolations": "0: none", "dgrRemoves": "refused: Allergy is not the root of patient; delete it through Patient", "dgrDangling": "none: the delete is refused"}},
            ],
            "panel_title": "Roots, boundaries and the references that cross them",
        }),
        "steps_title": "Drawing a boundary and checking it",
        "steps_intro": "Four steps, the last of them on a model of your own.",
        "steps": [
            ("Group the objects",
             "Put together the objects that are created, changed and deleted with "
             "one another, and that share a rule which must hold after every change."),
            ("Choose the root",
             "In each group pick the one entity that the rest of the system needs to "
             "find and name. Everything else in the group is reached through it."),
            ("Check every reference",
             "For each reference that crosses a boundary, ask whether it lands on a "
             "root. One that lands inside is a violation: route it through the root, "
             "hold a copied value instead, or move the boundary."),
            ("Do it on your own model",
             "Take five to eight classes from a system you know, write them as "
             "aggregates with roots, list their references, and count the ones that "
             "reach past a root. Write the count down with the one you would remove "
             "first."),
        ],
        "worked": {
            "title": "The clinic with two shortcuts",
            "intro": [
                "Count the crossings and the violations in <code>shortcuts</code>.",
            ],
            "lines": [
                "patient to allergy, contact: inside",
                "appointment to note: inside",
                "appointment to patient, doctor: roots",
                "note to doctor: a root, allowed",
                "reception to appointment: a root",
                "pharmacy to allergy: not a root",
                "note to allergy: not a root",
                "6 crossings, 2 of them violations",
            ],
            "after": [
                "Both violations land in the patient's aggregate. Removing them leaves "
                "the four crossings of <code>clinic</code>, every one on a root. What "
                "the pharmacy should hold instead, the patient or a copied list of "
                "substances, is a design choice the count does not make.",
            ],
        },
        "quiz_title": "Roots, boundaries and Evans's rules",
        "quiz": [
            {"q": "In the exercise's library model, how many references cross a "
                  "boundary, and how many of them reach an object that is not a root?",
             "a": ["5 cross, 2 reach a non-root",
                   "4 cross, 2 reach a non-root",
                   "5 cross, 3 reach a non-root",
                   "8 cross, 2 reach a non-root"],
             "c": 0,
             "why": "Loan to Renewal, Member to Card and Member to Hold stay inside "
                    "their aggregates. Loan to Member, Loan to Copy and Hold to Copy "
                    "cross onto roots, which is allowed; Desk to Card and Overdues to "
                    "Renewal cross onto inner objects. That is 5 crossings, 2 of them "
                    "violations. Deleting the member removes Member, Card and Hold, 3 "
                    "objects, and leaves 2 references dangling: Loan to Member and "
                    "Desk to Card. Hold to Copy goes with the hold, since it starts "
                    "inside the deleted aggregate."},
            {"q": "By Evans's rules, may an object inside one aggregate hold a "
                  "reference to the root of another?",
             "a": ["No: only outside objects that belong to no aggregate may",
                   "Yes: objects within an aggregate can hold references to other roots",
                   "Only for the length of one operation",
                   "Only if the two roots are in the same module"],
             "c": 1,
             "why": "The rules allow it explicitly; that is why the note's reference "
                    "to its doctor is not a violation. The transient rule, for one "
                    "operation only, is the one for references to inner objects that a "
                    "root lends out."},
            {"q": "Evans divides invariants by the aggregate boundary. Which "
                  "statement is his?",
             "a": ["Every invariant must hold at the end of every transaction",
                   "Invariants belong to the database, not the aggregate",
                   "Rules inside an aggregate may lag; rules that span aggregates are "
                   "enforced at once",
                   "Rules inside an aggregate are enforced as each transaction "
                   "completes; rules that span aggregates may lag and be brought up "
                   "to date by other means"],
             "c": 3,
             "why": "Rules across aggregates are not expected to be current at every "
                    "moment; events, batch runs or other updates resolve them within a "
                    "specified time. Within an aggregate, the rules hold when each "
                    "transaction is done. The first option is what a team without "
                    "boundaries ends up trying to do."},
            {"q": "On <code>delete-patient</code>, why does the lab report a "
                  "dangling reference although the patient's whole aggregate is "
                  "removed?",
             "a": ["Because the allergy was not deleted with the patient",
                   "Because the note refers to the doctor",
                   "Because the appointment, in another aggregate, still refers to "
                   "the patient",
                   "Because reception refers to the patient's contact"],
             "c": 2,
             "why": "The delete removes all 3 objects inside the boundary, the allergy "
                    "and the contact included. The appointment's reference to the "
                    "patient crosses into the deleted aggregate from outside, so it is "
                    "the one left dangling. Reception refers to the appointment, not "
                    "to the contact, and the note's doctor is untouched."},
        ],
        "mistakes": [
            ("Taking an aggregate for a group of objects that are stored together",
             "Evans's aggregate is defined by change, not storage: a unit for data "
             "changes, with a root that guards its invariants and a boundary that "
             "outsiders may not reach past. Objects may be stored in one table or "
             "many either way. What makes the cluster an aggregate is that the "
             "rules inside it hold after every committed change and that the only "
             "way in is through the root."),
            ("Thinking that no object inside an aggregate may refer outward",
             "Inner objects may refer to the roots of other aggregates; the rule is "
             "only that nothing outside holds an inner object. On the lesson's "
             "illustration the note's reference to its doctor is allowed, and the "
             "lab does not count it as a violation."),
            ("Expecting the boundary to make every rule hold at once",
             "Evans says plainly that rules spanning aggregates will not be current "
             "at all times, and are settled by events, batches or other updates. The "
             "dangling reference after a patient's delete is such a rule: the "
             "boundary tells you what the delete removes, and the model must still "
             "say what happens to the appointment."),
        ],
        "standard": (
            "Finish when you can check a model's references against its boundaries.",
            "Given objects grouped into aggregates and a list of references, count "
            "the crossings, name each that reaches past a root, and state what a "
            "delete of a root removes and leaves dangling."
        ),
        "note": (
            "The lab checks references against the boundaries you state. It cannot "
            "say where the boundaries should be: that, Evans argues, takes knowledge "
            "of the domain, such as which rules must hold together and which objects "
            "change often. Nor does it see a reference smuggled through a getter "
            "that a caller keeps; it sees only the references you list."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 6, Aggregates (PDF pp. 71-78 of the operator's copy): the
    # contention problem (p. 72), the purchase-order example: line locking
    # (pp. 74-75), the broken limit and the PO lock (p. 76), part locking and
    # deadlock, the three business facts (p. 77), the price copied into the
    # item and the daily queue (p. 78).
    # Quote: PDF p. 72 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "aggregate-invariants-and-locking",
        "title": "Aggregate Invariants and Concurrent Change",
        "module": "Chapter 6 · The Life Cycle of a Domain Object",
        "one_line": "Locking single objects lets two correct edits break a rule that spans the group; locking the aggregate keeps the rule, at a price in waiting.",
        "summary": (
            "The Aggregates pattern's own example: two users edit different parts "
            "of one order, each keeps the order's limit, and together they break "
            "it. Read how Evans moves from object locks to a lock on the whole "
            "aggregate and then to a better model, and run concurrent edits to a "
            "class booking under both schemes."
        ),
        "key": [
            "each edit can keep the rule",
            "two together can break it",
            "lock the aggregate, not the item",
            "a coarser lock costs waiting",
            "loosen ties where contention is high",
            "copy what need not stay current",
        ],
        "key_label": "Invariants and locks in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is Evans's; the other two are "
            "the lab's names for the two locking schemes the example compares."
        ),
        "concepts": [
            ("Invariant",
             "A consistency rule that must hold whenever the data changes. The "
             "lesson's is a sum: the places taken by the parties in a class may not "
             "exceed the places it has."),
            ("Object lock",
             "A scheme that locks only the object a user is editing. Two users "
             "editing different objects never wait for each other, and never see "
             "each other's edit before they commit."),
            ("Aggregate lock",
             "A scheme that locks the whole aggregate, through its root, as soon as "
             "one user begins to edit anything inside it. A second user who tries "
             "to edit the same aggregate is refused until the first is done."),
        ],
        "read_title": "The example's argument, then the two schemes counted",
        "read_intro": (
            "Read the Aggregates pattern's example, from the purchase-order model "
            "to the price copied into each line, in your own copy first."
        ),
        "body": [
            ("p", "&ldquo;We need to find a model that leaves high-contention points "
                  "looser and strict invariants tighter.&rdquo; Evans sets this as the "
                  "goal before the Aggregates pattern's rules, and the pattern's "
                  "extended example shows what it means. This lesson reads that "
                  "example, in which every step is a reasonable locking scheme and "
                  "every step but the last goes wrong."),
            ("p", "The example is a purchase order broken into line items, each for a "
                  "quantity of a catalogue part, under one rule: the items' total may "
                  "not pass the order's approval limit. The first scheme locks only "
                  "the object a user starts to edit. Two buyers then change two "
                  "different lines of the same order; each checks the total against "
                  "the limit in their own copy and is within it; neither line is "
                  "locked by the other; both commit, and the stored order is over its "
                  "limit with no one aware. Locking the whole order would have refused "
                  "the second save."),
            ("p", "Evans then pushes further. A part's price can change too, which "
                  "would break the rule from another direction, so he tries locking "
                  "the parts as well, and the users begin to wait on one another "
                  "over popular parts and finally deadlock. The way out is not a "
                  "cleverer lock but more knowledge of the business: parts appear in "
                  "many orders, parts change less often than orders, and a price "
                  "change need not reach orders already placed. So the price is "
                  "copied into each line when it is added, the line no longer "
                  "depends on the part's current price, and the order and its lines "
                  "become one aggregate whose limit can be enforced."),
            ("p", "Two things are worth noticing in that last step. The rule that "
                  "stays strict, the limit, is now wholly inside one boundary. The "
                  "rule that was loosened, keeping old orders in step with new "
                  "prices, did not vanish; Evans suggests a daily list of items with "
                  "outdated prices for users to update or let stand. And the "
                  "ownership matches the business, since an order and its lines are "
                  "created and deleted together while parts come and go on their own."),
            ("p", "The Enterprise Application Patterns lesson Pessimistic and "
                  "Coarse-Grained Locks reads the mechanism of a lock on a group, with "
                  "its version counters and shared locks. Evans's emphasis is "
                  "earlier: which objects form the group is a decision about the "
                  "model, and once the aggregate is drawn the lock follows it."),
            ("p", "The lab's instance is a cookery school's Saturday class with 12 "
                  "places, booked by three parties: the Walshes with 4, the Okafors "
                  "with 3 and the Lins with 2, 9 places in all. The class is the "
                  "root, and its `resize` method checks the rule in memory. Two staff "
                  "members, Pat and Sam, each read the class at minute 0. Pat makes "
                  "the Okafors 5 at minute 1 and 6 at minute 4, and Sam makes the "
                  "Lins 4 at minute 2. In Pat's copy the sum is 12; in Sam's it is "
                  "11. Each passes the check."),
            ("code", _lines(COOKERY_CLASS)),
            ("p", "On <code>object-locks</code> Pat locks the Okafors' line and Sam "
                  "the Lins', so neither waits: 2 users commit and 0 are refused. The "
                  "final values are 4, 6 and 4, and the lab reports a final sum of 14 "
                  "against a limit of 12, so the invariant does not hold. Neither user "
                  "did anything wrong, and the root's check ran both times, each time "
                  "on a copy that did not contain the other edit. The last tile, edits "
                  "lost, counts committed values that a later commit overwrote: 0, "
                  "because the two changed different parties."),
            ("p", "On <code>aggregate-lock</code> Pat's first edit at minute 1 takes "
                  "the whole class. Sam's edit at minute 2 is refused, so 1 user "
                  "commits and 1 is refused, and Sam's edit is discarded until Sam "
                  "reads the class again. The final values are 4, 6 and 2, the sum is 12, "
                  "and the invariant holds. The price is the refusal itself: Sam was "
                  "changing a different party and still had to wait."),
            ("p", "The preset <code>same-party</code> is the case object locks do "
                  "catch. Both staff edit the Okafors, so under object locks the second "
                  "to edit is refused on the same line: Pat alone commits and the sum "
                  "stays at 12. Object locks protect a rule about one object; the trouble starts when the rule is about the "
                  "sum of several."),
            ("h3", "Exercise"),
            ("ul", [
                "A guided walk with a limit of 15 walkers. Parties: ana 6, ben 5, "
                "cho 2.",
                "Edits (minute, user, party, new size): 1, kim, cho, 3; 2, lee, ben, "
                "6; 3, kim, cho, 4.",
            ]),
            ("p", "Each user reads at minute 0 and commits at their last minute. Work "
                  "out, under object locks and then under an aggregate lock, who "
                  "commits, the final sizes, the final sum, and whether the limit "
                  "holds. Then set the scheme in the lab and check both."),
            ("p", "An aggregate tells you what must be consistent; something still has "
                  "to build one consistent in the first place. The next lesson, "
                  "Factories, reads the chapter's answer."),
        ],
        "lab": ("dddkit", {
            "mode": "aggregate",
            "view": "lock",
            "preset": "object-locks",
            "presets": [
                {"id": "object-locks",
                 "label": "Pat and Sam edit different parties, object locks",
                 "items": _CLASS_ITEMS, "limit": 12, "edits": _CLASS_EDITS,
                 "scheme": "object",
                 "expect": {"dgrCommitted": "2: pat, sam", "dgrRefused": "0: none", "dgrFinal": "walsh = 4, okafor = 6, lin = 4", "dgrSum": "14", "dgrHolds": "no: sum 14 over limit 12", "dgrLost": "0: none"}},
                {"id": "aggregate-lock",
                 "label": "The same edits, one lock on the class",
                 "items": _CLASS_ITEMS, "limit": 12, "edits": _CLASS_EDITS,
                 "scheme": "aggregate",
                 "expect": {"dgrCommitted": "1: pat", "dgrRefused": "1: sam (the aggregate held by pat at minute 2)", "dgrFinal": "walsh = 4, okafor = 6, lin = 2", "dgrSum": "12", "dgrHolds": "yes: sum 12 within limit 12", "dgrLost": "0: none"}},
                {"id": "same-party",
                 "label": "Both edit the same party, object locks",
                 "items": _CLASS_ITEMS, "limit": 12, "edits": _CLASS_SAME_PARTY,
                 "scheme": "object",
                 "expect": {"dgrCommitted": "1: pat", "dgrRefused": "1: sam (okafor held by pat at minute 2)", "dgrFinal": "walsh = 4, okafor = 6, lin = 2", "dgrSum": "12", "dgrHolds": "yes: sum 12 within limit 12", "dgrLost": "0: none"}},
            ],
            "panel_title": "Two users, one class, two locking schemes",
        }),
        "steps_title": "Running concurrent edits by hand",
        "steps_intro": "Four steps, the last of them on a rule of your own.",
        "steps": [
            ("Give each user a copy",
             "Write down what each user reads at the start. Every check that user "
             "makes is against that copy plus their own edits, not the others'."),
            ("Apply the locking scheme",
             "Under object locks, refuse a user only on an object another user is "
             "already editing. Under an aggregate lock, the first user to edit "
             "anything holds the whole aggregate, and every other editor is refused."),
            ("Combine what commits",
             "Apply every committed edit to the stored values, then check the "
             "invariant on the result, not on any one user's copy."),
            ("Do it on your own rule",
             "Find a rule in a system you know that sums or compares several "
             "records, such as a budget or a capacity. Write two edits that each keep "
             "it and together break it, and say which object the lock should be on."),
        ],
        "worked": {
            "title": "Object locks on the Saturday class",
            "intro": [
                "Run <code>object-locks</code> by hand.",
            ],
            "lines": [
                "stored: walsh 4, okafor 3, lin 2",
                "Pat's copy: okafor 6, sum 12, passes",
                "Sam's copy: lin 4, sum 11, passes",
                "different lines: no one waits",
                "both commit: walsh 4, okafor 6, lin 4",
                "sum 14 against 12: broken",
            ],
            "after": [
                "Each check was correct for the copy it saw. The scheme, not the code, "
                "let the two copies be combined unchecked. With one lock on the class, "
                "Sam's edit is refused at minute 2 and the stored sum stays at 12.",
            ],
        },
        "quiz_title": "Locks, invariants and the example's model",
        "quiz": [
            {"q": "In the exercise's guided walk under an aggregate lock, who commits, "
                  "what is the final sum, and does the limit of 15 hold?",
             "a": ["Kim commits; the sum is 15; it holds",
                   "Both commit; the sum is 16; it is broken",
                   "Lee commits; the sum is 14; it holds",
                   "Kim commits; the sum is 13; it holds"],
             "c": 0,
             "why": "Kim edits first, at minute 1, and holds the walk until committing "
                    "at minute 3; Lee's edit at minute 2 is refused. The final sizes are "
                    "ana 6, ben 5, cho 4, a sum of 15, which is within a limit of 15. "
                    "Under object locks Kim and Lee edit different parties, both "
                    "commit, and the sum is 6 + 6 + 4 = 16, over the limit. A sum of 13 "
                    "is the walk before any edit."},
            {"q": "In Evans's purchase-order example, what change to the model lets "
                  "the order's limit be enforced without locking every part?",
             "a": ["Locking each part as well as the order",
                   "Making each line item the root of its own aggregate",
                   "Removing the approval limit from the order",
                   "Copying the part's price into the line item when it is added"],
             "c": 3,
             "why": "With the price copied, the lines no longer depend on the part's "
                    "current price, so the order and its lines form one aggregate and "
                    "the parts stay outside it. Locking the parts too is the step that "
                    "led to contention and deadlock."},
            {"q": "On <code>object-locks</code>, the root's `resize` check ran for both "
                  "Pat and Sam. Why did the stored class still end over its limit?",
             "a": ["The check has an off-by-one error",
                   "Each check ran on a copy that lacked the other user's edit",
                   "Sam's edit overwrote Pat's",
                   "The lab does not run the check"],
             "c": 1,
             "why": "Pat's copy summed to 12 and Sam's to 11, both within 12. Neither "
                    "copy held the other's change, and object locks on different lines "
                    "let both commit, so the stored sum is 14. Nothing was overwritten: "
                    "they edited different parties."},
            {"q": "Which of these is one of the business facts Evans uses to redesign "
                  "the example?",
             "a": ["Orders change less often than parts",
                   "A price change must reach every order at once",
                   "Parts are used in many orders, and change less often than orders",
                   "Each part belongs to exactly one order"],
             "c": 2,
             "why": "His three facts are that parts are in many orders (high "
                    "contention), that parts change less often than orders, and that a "
                    "price change need not reach existing orders. The first and second "
                    "options reverse two of them; the last contradicts the first."},
        ],
        "mistakes": [
            ("Believing that if every edit checks the rule, the rule is safe",
             "In the example each user's check passes and the stored order still "
             "breaks the limit, because each check sees only that user's copy. The "
             "rule spans several objects, so it is only as safe as the scope of the "
             "lock. On the lesson's illustration, two passing checks under object "
             "locks give a stored sum of 14 against 12."),
            ("Concluding that the safest design locks everything the rule touches",
             "Evans tries exactly that, locking the parts as well as the order, and "
             "it ends in contention and deadlock. His answer is to change the model, "
             "copying the price so the parts fall outside the boundary, not to widen "
             "the lock."),
            ("Treating an aggregate lock as free",
             "Evans says a lock on the whole order may suit work spread across many "
             "small orders and become cumbersome when many people edit lines of one "
             "large order. On the lesson's illustration Sam is refused although Sam "
             "was changing a different party."),
        ],
        "standard": (
            "Finish when you can run concurrent edits under both schemes.",
            "Given an aggregate's values, a sum limit and timed edits, state who "
            "commits, the final values and sum, and whether the invariant holds, "
            "under object locks and under an aggregate lock."
        ),
        "note": (
            "The lab's model of locking is the example's simplest one: each user "
            "reads at the start, locks on first edit and commits at the end. It "
            "does not model waiting, retries, version checks or deadlock, and it "
            "cannot weigh refused edits against broken rules. That weighing is the "
            "business knowledge Evans asks for."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 6, Factories (PDF pp. 79-86 of the operator's copy): the engine
    # and its assemblers (p. 79), the client's problem and the boxed statement
    # (p. 80), the two requirements and Gamma et al. (p. 81), Choosing
    # Factories and Their Sites (pp. 81-82), When a Constructor Is All You Need
    # (pp. 82-83), Designing the Interface (pp. 83-84), Where Does Invariant
    # Logic Go? (p. 84), Entity Factories Versus Value Object Factories (p. 84),
    # Reconstituting Stored Objects (pp. 84-86).
    # Quote: PDF p. 80 of the operator's copy, 23 words, quotes.py OK.
    # Lesson total: 23 words.
    {
        "slug": "factories",
        "title": "Factories",
        "module": "Chapter 6 · The Life Cycle of a Domain Object",
        "one_line": "Creation moved out of both the object and its client into something whose one job is to build a whole, consistent aggregate or refuse.",
        "summary": (
            "The second pattern of Chapter 6 deals with the start of an object's "
            "life. Read why Evans keeps complex creation out of both the product "
            "and the client, his two requirements for a good factory, where to put "
            "one, and how rebuilding a stored object differs; then send requests "
            "to a seed bank's factory and see which it admits and which rule "
            "refuses the rest."
        ),
        "key": [
            "assembly is a job of its own",
            "the client should not know the parts",
            "each creation is atomic",
            "a factory refuses what is invalid",
            "return the abstract type",
            "rebuilding keeps the old identity",
        ],
        "key_label": "Factories in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, all of them from the Factories pattern "
            "in Chapter 6."
        ),
        "concepts": [
            ("Factory",
             "An element of the design whose one job is building other objects. It "
             "need not stand for anything in the domain, but it belongs to the "
             "domain layer, and it hides how a complex object or aggregate is put "
             "together."),
            ("Atomic creation",
             "Creation in one step that hands back a complete product with every "
             "invariant satisfied, or hands back nothing. A factory that cannot "
             "build a valid product throws or otherwise makes an improper result "
             "impossible."),
            ("Reconstitution",
             "Evans's word for rebuilding a stored or transmitted object as a live "
             "one. It is the middle of the object's life, not a new birth, so the "
             "object keeps its old identity."),
        ],
        "read_title": "The pattern's argument, then the rule counted",
        "read_intro": (
            "Read the Factories pattern, through Reconstituting Stored Objects, in "
            "your own copy first."
        ),
        "body": [
            ("p", "&ldquo;Complex object creation is a responsibility of the domain "
                  "layer, yet that task does not belong to the objects that express "
                  "the model.&rdquo; That sentence, from the Factories pattern in "
                  "Chapter 6, holds the whole problem: creation has to live somewhere, "
                  "and the two obvious homes are both wrong."),
            ("p", "The first wrong home is the object itself. Evans's picture is a car "
                  "engine: nobody designs a block that grabs its own pistons, and the "
                  "mechanic or robot that assembles it is not with you when you "
                  "drive. Assembling a compound object is a different job from the "
                  "one it does once built, and combining the two makes an awkward "
                  "class. The second wrong home is the client. A client that "
                  "assembles must know the product's internal structure and some of "
                  "its rules, and even a constructor call ties it to concrete "
                  "classes, so the product cannot be refactored without changing the "
                  "client. If the client is in the application layer, domain "
                  "knowledge has leaked out of the domain layer altogether."),
            ("p", "So he adds an element that is not an entity, value or service, and "
                  "says plainly that this departs from the previous chapter: it "
                  "corresponds to nothing in the model, yet it is the domain layer's "
                  "work. Stated as the reader would apply it, the pattern says: when "
                  "building an object or a whole aggregate is complicated, or would "
                  "expose its insides, make building it the job of a separate "
                  "element; let clients ask that element for what they want in their "
                  "own terms, never naming the classes it puts together; and have it "
                  "hand back each aggregate complete, its rules already checked."),
            ("p", "Two requirements follow. Each creation method is atomic and "
                  "produces only a consistent product: for an entity, the whole "
                  "aggregate with its invariants met, perhaps with optional parts "
                  "still to add; for an immutable value, every attribute in its final "
                  "state; and a request that cannot be met raises an exception or "
                  "otherwise cannot return something improper. And the factory "
                  "returns the abstract type wanted rather than the concrete class "
                  "built. For Factory Method, Abstract Factory and Builder, the "
                  "detailed patterns of construction, Evans points to Gamma and "
                  "colleagues' Design Patterns."),
            ("p", "Where to put one follows from what it hides. A factory method on an "
                  "aggregate's root adds elements inside it while the root keeps the "
                  "aggregate whole. A factory method on an object closely involved in "
                  "spawning another, though it will not own the product, keeps that "
                  "object's data and rules where they are; the book's case is a "
                  "brokerage account that creates trade orders. With no natural host, "
                  "a standalone factory or service builds the whole aggregate and "
                  "returns its root. And sometimes a constructor is all you need: "
                  "when the class is the type, with no interesting hierarchy, the "
                  "client cares which implementation it gets, every attribute is "
                  "available, and construction is simple. Even then the constructor "
                  "must be atomic and leave the object valid."),
            ("p", "On the interface, Evans asks for one call that carries everything a "
                  "complete product needs, a decision about what happens on failure "
                  "(an exception or a null, chosen once as a team standard), and "
                  "parameters chosen with care, since a factory is coupled to its "
                  "arguments, more tightly the more it picks them apart. On "
                  "invariants, the factory may delegate checking to the product, "
                  "which is often best, but a rule that can only matter at creation, "
                  "such as one on an entity's identity, can sit in the factory and "
                  "keep the product simpler. Entity factories take the essentials and "
                  "let details come later; value factories need the full description, "
                  "because the product is immutable."),
            ("p", "The seed bank's factory below creates a new accession, a stored lot "
                  "of seed, with its germination test inside the aggregate. It issues "
                  "the accession number itself and refuses a lot that would make a "
                  "poor store: fewer than 400 seeds, germination under 70 percent, "
                  "moisture over 8 percent, or an unknown origin. The lab states the "
                  "same four rules as one specification, `seeds >= 400 and "
                  "germination >= 70 and moisture <= 8 and origin = known`, and checks "
                  "a request against it clause by clause, in the order written, as the "
                  "factory's tests run."),
            ("code", _lines(ACCESSION_FACTORY)),
            ("p", "On <code>sound-lot</code>, 1,200 seeds at 88 percent germination "
                  "and 6 percent moisture with a known origin, all 4 clauses are true "
                  "and the factory admits it. On <code>damp-lot</code>, 900 seeds at "
                  "81 percent, but 11 percent moisture, 3 clauses are true and the "
                  "first false one is `moisture <= 8`: the factory refuses with too "
                  "damp to store. On <code>small-lot</code>, 150 seeds from an "
                  "unknown origin at 92 percent and 7 percent moisture, 2 clauses are "
                  "false, `seeds >= 400` and `origin = known`, and the first is the "
                  "seed count, the message a caller of this factory would see."),
            ("p", "Reconstitution is where the rule changes. Rebuilding a stored "
                  "object, Evans says, differs from creating one in two ways: an "
                  "entity's identifying attributes come in as arguments, since a new "
                  "number would break the object's continuity, and a violated "
                  "invariant cannot simply be refused, because the object already "
                  "exists. Suppose the bank raised its minimum to 400 seeds last year: "
                  "a stored lot of 300 is still a lot. The method below takes its "
                  "number from the row and flags the lot for regrowing instead of "
                  "throwing."),
            ("code", _lines(ACCESSION_RECONSTITUTE)),
            ("h3", "Exercise"),
            ("p", "A request arrives with seeds=450, germination=69, moisture=9 and "
                  "origin=known. By the specification above, checked clause by clause "
                  "in the order written, say how many clauses are false, which one the "
                  "factory reports first, and what the reconstitution method would do "
                  "with a stored lot of the same figures. To check the first two, add "
                  "the request to the lab's candidates as a record named `request`, "
                  "with the four attributes as cells, and set the candidate to "
                  "`request`."),
            ("p", "A factory begins an object's life. The next lesson, Repositories "
                  "and Relational Databases, reads the pattern for its middle and "
                  "end: finding an object that already exists."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "validate",
            "spec": _ACCESSION_SPEC,
            "candidates": _LOTS,
            "preset": "sound-lot",
            "presets": [
                {"id": "sound-lot",
                 "label": "A sound lot: 1,200 seeds, 88 percent, dry, known origin",
                 "candidate": "sound-lot",
                 "expect": {"dspSatisfied": "yes", "dspTrue": "4 of 4", "dspFirstFalse": "none: every clause is true", "dspFalse": "0: none"}},
                {"id": "damp-lot",
                 "label": "A damp lot: 11 percent moisture",
                 "candidate": "damp-lot",
                 "expect": {"dspSatisfied": "no", "dspTrue": "3 of 4", "dspFirstFalse": "clause 3, moisture <= 8: moisture is 11", "dspFalse": "1: moisture <= 8"}},
                {"id": "small-lot",
                 "label": "A small lot of unknown origin",
                 "candidate": "small-lot",
                 "expect": {"dspSatisfied": "no", "dspTrue": "2 of 4", "dspFirstFalse": "clause 1, seeds >= 400: seeds is 150", "dspFalse": "2: seeds >= 400, origin = known"}},
            ],
            "panel_title": "What the accession factory admits, and which rule refuses",
        }),
        "steps_title": "Designing a factory's refusal",
        "steps_intro": "Four steps, the last of them on an object of your own.",
        "steps": [
            ("List the invariants",
             "Write every rule a new product must satisfy, including those on the "
             "inner objects of its aggregate, as clauses you could test one by one."),
            ("Put them in the order a caller needs",
             "Order the checks so the first refusal is the most useful message, and "
             "decide once whether a refusal throws or returns nothing."),
            ("Separate creation from rebuilding",
             "For the same product, say which rules a reconstitution method must "
             "repair or flag rather than refuse, and which identifying attributes it "
             "takes as arguments."),
            ("Do it on your own object",
             "Find an object in a system you know whose callers assemble it by "
             "setting fields after construction. Write the one factory call that "
             "would build it whole, with the clauses it would check, and count how "
             "many callers it would replace."),
        ],
        "worked": {
            "title": "The small lot, clause by clause",
            "intro": [
                "Check <code>small-lot</code> against the specification.",
            ],
            "lines": [
                "seeds >= 400: 150, false",
                "germination >= 70: 92, true",
                "moisture <= 8: 7, true",
                "origin = known: unknown, false",
                "2 clauses false, 2 true",
                "first false: seeds >= 400",
                "refused: fewer than 400 seeds",
            ],
            "after": [
                "The factory stops at its first failed test, so its caller hears only "
                "about the seed count. The lab lists every false clause, which is what "
                "a caller fixing the request needs; whether the factory should report "
                "all of them is a choice about its interface.",
            ],
        },
        "quiz_title": "Creation, refusal and Evans's requirements",
        "quiz": [
            {"q": "In the exercise, a request with seeds=450, germination=69, "
                  "moisture=9 and origin=known is checked against the specification "
                  "in the order written. How many clauses are false, and which is "
                  "reported first?",
             "a": ["1 false; germination >= 70",
                   "2 false; moisture <= 8",
                   "3 false; seeds >= 400",
                   "2 false; germination >= 70"],
             "c": 3,
             "why": "450 seeds passes `seeds >= 400`. Germination of 69 fails `>= 70` "
                    "and moisture of 9 fails `<= 8`; a known origin passes. Two clauses "
                    "are false, and germination comes first in the order written, so "
                    "the factory refuses with germination under 70 percent. The "
                    "reconstitution method would not refuse a stored lot with these "
                    "figures: it takes the lot's number from the row, and its only "
                    "check is on seeds, which 450 passes, so the lot is rebuilt as it "
                    "is."},
            {"q": "Which are Evans's two basic requirements for any good factory?",
             "a": ["Each creation method is atomic and enforces the product's "
                   "invariants; and it is abstracted to the type wanted, not the "
                   "concrete class",
                   "It is a standalone class, and it caches its products",
                   "It assigns every product a new identity, and it stores the product",
                   "It sets every optional attribute, and it never throws"],
             "c": 0,
             "why": "Those are the two numbered requirements. A factory method on a "
                    "root is not standalone; a reconstituting factory must not assign a "
                    "new identity; storing is the repository's job; and an entity "
                    "factory may leave optional parts to be added later."},
            {"q": "When does Evans say a bare public constructor is the better choice?",
             "a": ["Whenever the product is an entity",
                   "When the class is the type, the client cares about the "
                   "implementation, all attributes are available and construction is "
                   "simple",
                   "When the product is the root of an aggregate",
                   "Never: a factory is always preferable"],
             "c": 1,
             "why": "Those are his circumstances in When a Constructor Is All You "
                    "Need, with the condition that the constructor is still atomic. "
                    "An aggregate assembled from many parts wants a factory, "
                    "and he says factories are generally underused, but not that they "
                    "always win."},
            {"q": "How does a factory that reconstitutes a stored entity differ from "
                  "one that creates a new one, by Evans's account?",
             "a": ["It assigns a new tracking number and refuses any violation",
                   "It skips every invariant, since the object was valid once",
                   "It takes the identifying attributes as input, and needs a more "
                   "flexible response than refusal to a broken invariant",
                   "It is always the repository itself"],
             "c": 2,
             "why": "A new number would break continuity with the object's earlier "
                    "life, and an object that already exists cannot be wished away, so "
                    "some strategy for repairing it is needed. Ignoring the violation "
                    "is not an option he allows, and he keeps factory and repository "
                    "separate in the domain view."},
        ],
        "mistakes": [
            ("Thinking a factory must stand for something in the domain",
             "Evans says the opposite in so many words: factories are design elements "
             "that correspond to nothing in the model, and they are still the domain "
             "layer's responsibility. Opening an account may be a milestone the "
             "experts talk about, but usually creation is a need of the "
             "implementation, and the factory keeps it out of the objects that do "
             "express the model."),
            ("Believing a factory may hand back a half-built object to be finished later",
             "Each creation is atomic: the product comes out consistent or not at all. "
             "An entity factory may leave optional parts for later, but only those no "
             "invariant requires. On the lesson's illustration the accession factory "
             "refuses the damp lot outright rather than returning it to be dried."),
            ("Expecting a reconstituted object to pass the creation rules",
             "A stored object already exists, so a rule broken since it was stored "
             "has to be repaired, not refused. The lesson's reconstitution method "
             "flags a lot below the new minimum instead of throwing, which a factory "
             "for new lots must not do."),
        ],
        "standard": (
            "Finish when you can say what a factory admits and why it refuses.",
            "Given a factory's invariants as a specification and a request, state "
            "each clause's truth, the first that fails, and how a reconstituting "
            "factory would treat the same figures."
        ),
        "note": (
            "The lab checks a request against the rules you write; it cannot say "
            "whether those are the right rules, or whether the factory belongs on a "
            "root, on a spawning object or on its own. It treats the specification "
            "as a list of clauses in order, which is how this factory's tests run, "
            "and says nothing about reconstitution, which needs a repair the model "
            "has to decide."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 6, Repositories (PDF pp. 86-93 of the operator's copy): three ways
    # to a reference and the creation-and-traversal team (pp. 86-87), the
    # problem restated and the boxed statement (pp. 88-89), the advantages
    # (p. 89), Querying a Repository with Specification-based queries and Mee
    # and Hieatt (pp. 89-90), Kyle Brown's story (pp. 90-91), Implementing a
    # Repository (pp. 91-92), Working Within Your Frameworks (p. 92), The
    # Relationship with Factories and find-or-create (pp. 92-93); Designing
    # Objects for Relational Databases (pp. 94-95).
    # Quote: PDF p. 86 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "repositories",
        "title": "Repositories and Relational Databases",
        "module": "Chapter 6 · The Life Cycle of a Domain Object",
        "one_line": "An object that lets a client treat the stored roots of one type as a collection in memory, asked in the model's terms for the ones it wants.",
        "summary": (
            "The third pattern of Chapter 6 deals with the middle and end of an "
            "object's life. Read why Evans wants a starting point for traversal "
            "that does not drag the client into query code, what a repository "
            "promises, how it relates to factories and to the relational database "
            "underneath, and then ask a bike-share's repository for the bikes that "
            "satisfy a specification."
        ),
        "key": [
            "a starting point for traversal",
            "only roots that need finding",
            "a collection in memory, in effect",
            "queries in the model's terms",
            "the client, not it, commits",
            "factories make, repositories find",
            "keep tables close to the model",
        ],
        "key_label": "Repositories in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's, from Chapter 6; "
            "the third is Chapter 9's, used here as the repository's query."
        ),
        "concepts": [
            ("Repository",
             "An object that stands for all the stored objects of one type as if "
             "they were a collection in memory. Clients add, remove and ask for "
             "objects through it, and it hides the database and the mapping behind "
             "it."),
            ("Global access",
             "Being reachable by a search on attributes rather than by following a "
             "reference from another object. Evans reserves it for the aggregate "
             "roots that are not convenient to reach any other way."),
            ("Specification",
             "An object stating a condition that another object either satisfies or "
             "does not. A repository can take one as its query, so a client says what "
             "it wants without saying how to find it."),
        ],
        "read_title": "The pattern's argument, then a query counted",
        "read_intro": (
            "Read the Repositories pattern and Designing Objects for Relational "
            "Databases in your own copy first."
        ),
        "body": [
            ("p", "&ldquo;To do anything with an object, you have to hold a reference "
                  "to it. How do you get that reference?&rdquo; Evans counts three "
                  "ways in the Repositories pattern of Chapter 6. You can create the "
                  "object; you can traverse an association from an object you hold; "
                  "or you can search the database by attributes and rebuild what you "
                  "find. He tells of a team that tried to manage with the first two "
                  "alone, on an object database, and built the very tangle the last "
                  "chapters warned against before giving up on it."),
            ("p", "The third way is necessary and dangerous. A search can reach any "
                  "object, so not everything has to be linked to everything. But a "
                  "client that writes its own queries, gets rows back and feeds them "
                  "to constructors is thinking about the technology, not the domain, "
                  "and is tempted to grab exactly the data it wants, past the "
                  "aggregates and past encapsulation. Rules drift into query code, "
                  "and the entities become containers of data. Evans narrows the "
                  "problem: transient values need no search; objects easy to reach "
                  "by traversal need none; and no object inside an aggregate may be "
                  "fetched except through its root. A value found by global search, "
                  "he adds, may be an entity whose identity nobody has noticed."),
            ("p", "The pattern, as the reader would apply it: when clients must look "
                  "up objects of some type by their attributes, give that type one "
                  "object that clients can treat as if it simply held every such "
                  "object in memory. Clients put objects in and take them out through "
                  "it, and ask it for the ones matching a condition, getting whole "
                  "objects back; it alone talks to the store. Only aggregate roots get "
                  "one, and only those that clients cannot reach by following "
                  "references. Its advantages, in his "
                  "list: a simple model for clients, persistence decoupled from the "
                  "domain, design decisions about access made visible, and an "
                  "in-memory stand-in for tests."),
            ("p", "Querying a Repository describes a range. The easiest repository "
                  "has hard-coded queries: by identity, by an attribute, by a range of "
                  "dates, and summary queries such as a count or a total. Where there "
                  "is a lot of querying, a framework can accept a Specification "
                  "instead, which Chapter 9 develops; Evans calls this elegant and "
                  "warns it may be a modest framework or prohibitively hard, pointing "
                  "to Rob Mee and Edward Hieatt's discussion in Fowler's book. Even "
                  "then, hard-coded queries should remain possible."),
            ("p", "Encapsulation does not excuse ignorance. Client code can ignore "
                  "how a repository works, Evans says, but its developers cannot: "
                  "Kyle Brown's story is of a system that ran out of memory after "
                  "hours in production because a summary was computed by fetching "
                  "every object in the plant. In implementing one, abstract the type, "
                  "use the freedom to cache or change strategy, and leave the commit "
                  "to the client, which knows where the unit of work begins and ends. "
                  "Work with your framework rather than against it, and look for "
                  "affinities; his example is J2EE's entity beans and the EJB Home, "
                  "with the warning that dressing the EJB Home up as a repository "
                  "could cause problems of its own."),
            ("p", "Factories and repositories meet at reconstitution. Technically a "
                  "repository that rebuilds objects from rows is creating them, but "
                  "Evans keeps the roles apart in the domain view: one creates what "
                  "did not exist, the other finds what already does, and a repository "
                  "may delegate the rebuilding to a factory. He advises against a combined "
                  "find-or-create, since the difference between a new object and an "
                  "existing one usually matters in the domain."),
            ("p", "The Enterprise Application Patterns lesson Metadata Mapping, Query "
                  "Object and Repository reads the same pattern from the database "
                  "side, as a layer over the mapping. Evans's emphasis is on what "
                  "the repository's interface says about the model: which roots can "
                  "be found at all, and in what terms."),
            ("p", "Designing Objects for Relational Databases closes the chapter. "
                  "When the schema exists to store this system's objects, keep the "
                  "tables close to the model, even at some cost to the model's "
                  "richness or to normalization: a row holds an object, perhaps with "
                  "its aggregate's inner parts, and a foreign key becomes a reference "
                  "to another entity, with names that match. Keep other processes out "
                  "of such a store, since they can break the objects' invariants. A "
                  "legacy schema means two models in one system, which Chapter 14 "
                  "takes up; and a schema deliberately separate from the model can be "
                  "a sound choice, if it is chosen and not drifted into."),
            ("p", "The bike-share's repository below answers the workshop's question "
                  "with a specification: a bike is due for service if it is docked "
                  "and has either done 800 kilometres since its last service or has "
                  "an open fault report. Docks belong to a station's aggregate and "
                  "get no repository of their own."),
            ("code", _lines(BIKE_REPOSITORY)),
            ("p", "On <code>fleet</code> the lab holds five bikes, the roots the "
                  "repository contains, and asks `status = docked and (km >= 800 or "
                  "faults >= 1)`. It selects 2: b101, docked at 950 kilometres, and "
                  "b102, docked at 300 with 2 faults. Of the 3 that fail, b103 fails "
                  "first on `status = docked`, being out on a ride; b104 and b105 fail "
                  "first on `km >= 800`, at 420 and at 799, with no faults to rescue "
                  "them. The preset <code>worn-only</code> asks the hard-coded query a "
                  "simpler repository might offer, `status = docked and km >= 800`, "
                  "and selects only b101: b102's faults no longer count."),
            ("h3", "Exercise"),
            ("p", "Three more bikes: b201 with status=docked, km=800, faults=0; b202 "
                  "with status=repair, km=50, faults=3; b203 with status=docked, "
                  "km=640, faults=0. Say which the specification `status = docked and "
                  "(km >= 800 or faults >= 1)` selects and, for each of the others, "
                  "the first clause in the order written that is false. Type them into "
                  "the lab to check."),
            ("p", "That ends Chapter 6's patterns. The next lesson, Using the "
                  "Language: An Extended Example, reads Chapter 7, where Evans uses "
                  "them all together on one model."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "select",
            "candidates": _FLEET,
            "preset": "fleet",
            "presets": [
                {"id": "fleet",
                 "label": "Five bikes, asked which are due for service",
                 "spec": _DUE_FOR_SERVICE,
                 "expect": {"dspCandidates": "5", "dspSatisfying": "2: b101, b102", "dspFailing": "3: b103 (status = docked: status is riding); b104 (km >= 800: km is 420); b105 (km >= 800: km is 799)"}},
                {"id": "worn-only",
                 "label": "The same bikes, a hard-coded query on distance only",
                 "spec": "status = docked and km >= 800",
                 "expect": {"dspCandidates": "5", "dspSatisfying": "1: b101", "dspFailing": "4: b102 (km >= 800: km is 300); b103 (status = docked: status is riding); b104 (km >= 800: km is 420); b105 (km >= 800: km is 799)"}},
            ],
            "panel_title": "The roots a repository returns for a specification",
        }),
        "steps_title": "Asking a repository in the model's terms",
        "steps_intro": "Four steps, the last of them on a repository of your own.",
        "steps": [
            ("Decide which roots need finding",
             "List the aggregate roots that a client must reach by search, and give "
             "every other object a path by traversal from one of them."),
            ("State the question as a condition",
             "Write the client's request as clauses on the root's attributes, "
             "combined with and, or and not, in the experts' terms."),
            ("Check each candidate",
             "For each root, evaluate the clauses in the order written; it is "
             "selected if the whole condition holds, and otherwise note the first "
             "clause that is false."),
            ("Do it on your own repository",
             "Find a query in a system you know that a client builds itself in SQL "
             "or a query language. Rewrite it as one repository method in the "
             "model's terms, and count how many places that build the same query "
             "it would replace."),
        ],
        "worked": {
            "title": "Five bikes and one specification",
            "intro": [
                "Run <code>fleet</code> by hand.",
            ],
            "lines": [
                "b101: docked, 950 km: selected",
                "b102: docked, 2 faults: selected",
                "b103: riding: fails status = docked",
                "b104: 420 km, no fault: fails km",
                "b105: 799 km, no fault: fails km",
                "2 selected out of 5",
            ],
            "after": [
                "b105 misses by one kilometre, which is the rule as written, not a "
                "judgement about the bike. The repository's client never sees how "
                "the five were fetched, only the two that satisfy the specification.",
            ],
        },
        "quiz_title": "Queries, roots and Evans's repository",
        "quiz": [
            {"q": "In the exercise, which bikes does `status = docked and (km >= 800 "
                  "or faults >= 1)` select, and why does each other bike fail?",
             "a": ["b201 only; b202 fails on status = docked, b203 on km >= 800",
                   "b201 and b202; b203 fails on km >= 800",
                   "None; b201 fails on km >= 800 since 800 is not over 800",
                   "b201 only; b202 fails on faults >= 1, b203 on km >= 800"],
             "c": 0,
             "why": "b201 is docked at exactly 800, and `>=` includes 800, so it is "
                    "selected. b202 has 3 faults but is in repair, so the first clause, "
                    "`status = docked`, is false. b203 is docked with 640 kilometres "
                    "and no fault, so `km >= 800` is the first false clause, and "
                    "`faults >= 1` is false too."},
            {"q": "For which objects does Evans say a repository should be provided?",
             "a": ["For every class that is stored",
                   "For every entity, root or not",
                   "For value objects only, since entities are found by traversal",
                   "For the aggregate roots that actually need direct access"],
             "c": 3,
             "why": "Objects inside an aggregate are reached only through their root, "
                    "and objects convenient to reach by traversal need no search. A "
                    "value found by global search may be an entity whose identity has "
                    "not been recognised."},
            {"q": "Who should commit the transaction when a repository inserts an "
                  "object, by Evans's advice in Implementing a Repository?",
             "a": ["The repository, immediately after saving",
                   "The client, which has the context to start and commit the unit of "
                   "work",
                   "The factory that built the object",
                   "The database's trigger"],
             "c": 1,
             "why": "He grants the temptation to commit after saving and advises "
                    "against it: the repository inserts and deletes but ordinarily "
                    "commits nothing, which keeps transaction management simpler."},
            {"q": "Why does Evans advise against a find-or-create operation that "
                  "combines repository and factory?",
             "a": ["It is at best a minor convenience, and the difference between a "
                   "new object and an existing one usually matters in the domain",
                   "It is too slow on relational databases",
                   "Factories cannot create entities",
                   "Repositories may not return new objects to tests"],
             "c": 0,
             "why": "He calls it a minor convenience at best, notes that many cases "
                    "vanish once entities and values are told apart, and says a "
                    "framework that hides the difference muddles the situation."},
        ],
        "mistakes": [
            ("Giving every stored class a repository",
             "Evans limits repositories to the aggregate roots that need direct "
             "access. Inner objects are reached through their root, and objects "
             "easy to reach by traversal need no search. On the lesson's "
             "illustration the docks belong to a station's aggregate and have no "
             "repository of their own."),
            ("Thinking a repository's client need not understand what it costs",
             "The client code is decoupled from the implementation; its developers are "
             "not. Kyle Brown's story, in Client Code Ignores Repository "
             "Implementation, is of a summary that loaded every object into memory "
             "and kept running out of memory in production."),
            ("Treating a repository as a factory because it builds objects from rows",
             "Technically it does create instances, and Evans says so; but in the "
             "domain view a rebuilt object is the same object in the middle of its "
             "life. New objects come from factories and existing ones from "
             "repositories, and the repository may hand the rebuilding to a factory."),
        ],
        "standard": (
            "Finish when you can say what a repository returns for a specification.",
            "Given a set of roots with their attributes and a specification, list "
            "the roots it selects and the first false clause for each of the rest."
        ),
        "note": (
            "The lab evaluates a specification over the roots you list, as an "
            "in-memory repository would. It knows nothing of the database, the "
            "mapping or the cost of a query, which Evans says the developer must "
            "still understand, and it cannot say which roots deserve a repository "
            "at all."
        ),
    },
]
