"""Supple Design, lessons 1-5 -- Chapter 10.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004), Chapter 10, Supple Design: the chapter's opening,
Intention-Revealing Interfaces, Side-Effect-Free Functions, Assertions,
Conceptual Contours, Standalone Classes and Closure of Operations. Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter,
section and pattern. Every quotation is copied from that copy and checked with
quotes.py. The code and the lab models are written for these lessons: none of
the book's listings, diagrams or example domains is reproduced (the book's
paint-mixing and loan examples are summarised in prose only). The design is
docs/domain-driven-design/PLAN.md, section C, Course 5.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


MODULE = "Chapter 10 · Supple Design"

_DDD_INTRO = (
    "A count over the small model the lesson states. The lab counts one consequence "
    "of one modelling choice; the choice itself is weighed in the book, against the "
    "domain, the team and the project."
)


# ---------------------------------------------------------------- snippets

# 5.1 Intention-Revealing Interfaces: presets means-names, intention-names, long-means.
MEANS_NAMES = """// In the box office: what does this tell a client?
boolean scan(int[] row, int k) {
    int run = 0;
    for (int i = 0; i < row.length; i++) {
        if (row[i] == 0) {
            run++;
        } else {
            run = 0;
        }
        if (run >= k) {
            return true;
        }
    }
    return false;
}"""

INTENTION_NAMES = """// In SeatRow: can a party of this size sit side by side?
boolean canSeatTogether(int partySize) {
    int freeInARow = 0;
    for (Seat seat : seatsInOrder()) {
        if (seat.isFree()) {
            freeInARow++;
        } else {
            freeInARow = 0;
        }
        if (freeInARow >= partySize) {
            return true;
        }
    }
    return false;
}"""

LONG_MEANS = """// Long names, every one of them about the mechanism.
boolean scanArrayForZeroRun(int[] seatFlags, int requiredRunLength) {
    int currentZeroRun = 0;
    for (int index = 0; index < seatFlags.length; index++) {
        if (seatFlags[index] == 0) {
            currentZeroRun++;
        } else {
            currentZeroRun = 0;
        }
        if (currentZeroRun >= requiredRunLength) {
            return true;
        }
    }
    return false;
}"""

SEAT_TEST = """// Written first, from the client's side of the interface.
SeatRow row = SeatRow.parse("free free sold free free free");
assertTrue(row.canSeatTogether(3));
assertFalse(row.canSeatTogether(4));"""

REFUND_EXERCISE = """// In Booking: what is returned, and when?
long amt(int d) {
    long base = priceCents();
    if (d >= 14) {
        return base;
    }
    long tmp = base / 2;
    if (d < 2) {
        tmp = 0;
    }
    return tmp;
}"""


# 5.2 Side-Effect-Free Functions: body code only; the lab is the sharing model.
DOSE_TWO_WAYS = """// A dose that changes in place: every holder of it sees the change.
class MutableDose {
    private int milligrams;
    MutableDose(int milligrams) { this.milligrams = milligrams; }
    void scaleBy(int factor) { milligrams = milligrams * factor; }
    int milligrams() { return milligrams; }
}

// A dose as a value: the function returns a new one and changes nothing.
final class Dose {
    private final int milligrams;
    Dose(int milligrams) { this.milligrams = milligrams; }
    Dose times(int factor) { return new Dose(milligrams * factor); }
    int milligrams() { return milligrams; }
}"""

PRESCRIPTION_COMMAND = """// In Prescription, an entity: before, one method did both jobs.
MutableDose doubleAndReport() {
    dose.scaleBy(2);
    return dose;
}

// After: a query that computes, and a command that only replaces.
Dose doubled() { return dose.times(2); }
void changeDoseTo(Dose newDose) { dose = newDose; }"""

WINDOW_EXERCISE = """Window morning = new Window(8, 10);
Window noon = new Window(12, 13);
Order a = new Order(morning);
Order b = new Order(morning);
Order c = new Order(noon);
Order d = new Order(morning);
Order e = new Order(noon);
b.window().extendBy(1);   // Window is mutable: changed in place"""


# 5.3 Assertions: body code only; the lab checks the stated state as a specification.
DOCK_ASSERTIONS = """// In Dock, an entity. After a.sendBikesTo(b, n):
//   a holds n bikes fewer than before, and b holds n more;
//   so the two docks together hold as many bikes as before.
// Invariant of every Dock: 0 <= bikes() and bikes() <= capacity().
// Precondition: n <= bikes() and n <= b.spaces().
void sendBikesTo(Dock other, int n) {
    bikes = bikes - n;
    other.receive(n);
}"""

DOCK_TEST = """// The test sets up the precondition, acts, and checks the state.
Dock a = new Dock(12, 8);   // capacity 12, holding 8
Dock b = new Dock(10, 5);   // capacity 10, holding 5
a.sendBikesTo(b, 3);
assertEquals(5, a.bikes());
assertEquals(8, b.bikes());"""

DOCK_STATES = [
    ["kept", "removed=3", "added=3", "fromBikes=5", "toSpaces=2"],
    ["overfull", "removed=3", "added=3", "fromBikes=5", "toSpaces=-1"],
    ["oneSided", "removed=0", "added=3", "fromBikes=8", "toSpaces=2"],
]

DOCK_SPEC = "removed = 3 and added = 3 and fromBikes >= 0 and toSpaces >= 0"

VAULT_EXERCISE ="""// After vault.withdraw(80), from 100 packets, reorder level 30:
// post-condition:  taken = 80 and left = 20
// invariant:       left >= 30 or reorder = yes
state A:  taken=80  left=20   reorder=yes
state B:  taken=80  left=20   reorder=no
state C:  taken=80  left=100  reorder=no"""


# 5.4 Conceptual Contours: the timetable model, as data for the lab and prose.
TIMETABLE_ELEMENTS = [
    # element, packaging by step, packaging by concept
    ["roomCapacityRule", "checks", "rooms"],
    ["roomEquipmentRule", "checks", "rooms"],
    ["teacherHoursRule", "checks", "teachers"],
    ["teacherFreeDayRule", "checks", "teachers"],
    ["clashCheckRoom", "clashes", "rooms"],
    ["clashCheckTeacher", "clashes", "teachers"],
    ["printRoomView", "printing", "rooms"],
    ["printTeacherView", "printing", "teachers"],
    ["periodLengthRule", "periods", "periods"],
]

CHANGES_TERM = [
    ["scienceLabs", "roomEquipmentRule"], ["scienceLabs", "clashCheckRoom"],
    ["scienceLabs", "printRoomView"],
    ["partTimeTeachers", "teacherHoursRule"], ["partTimeTeachers", "teacherFreeDayRule"],
    ["partTimeTeachers", "clashCheckTeacher"], ["partTimeTeachers", "printTeacherView"],
    ["shortFridays", "periodLengthRule"], ["shortFridays", "clashCheckRoom"],
    ["shortFridays", "clashCheckTeacher"],
    ["largeType", "printRoomView"], ["largeType", "printTeacherView"],
]

CHANGES_CONCEPTS = CHANGES_TERM[:7]

CHANGES_ACROSS = CHANGES_TERM[7:]

TIMETABLE_EXERCISE = """examWeeks touches     clashCheckRoom, printRoomView, periodLengthRule
teacherCover touches  teacherFreeDayRule, clashCheckTeacher, printTeacherView"""


# 5.5 Standalone Classes and Closure of Operations: presets tangled-dock,
# standalone-dock, standalone-fare; exercise.
TANGLED_FARE = """// The fare rule reaches into four other concepts, one of them hidden.
class FareCalculator {
    long fareCents(Ride ride, Rider rider, Membership plan) {
        long cents = 100 + 15 * ride.minutes();
        if (ride.start().zone() != ride.end().zone()) {
            cents = cents + 50;
        }
        if (plan.isActiveFor(rider)) {
            cents = cents - cents / 4;
        }
        return cents;
    }
}"""

STANDALONE_FARE = """// Fare knows nothing but long and int; plus is closed under Fare.
final class Fare {
    private final long cents;
    Fare(long cents) { this.cents = cents; }
    Fare plus(Fare other) { return new Fare(cents + other.cents); }
    Fare lessPercent(int percent) {
        return new Fare(cents - cents * percent / 100);
    }
    long cents() { return cents; }
}

// Tariff states the rule over plain numbers and answers with a Fare.
final class Tariff {
    Fare forRide(int minutes, int zonesCrossed) {
        return new Fare(100 + 15L * minutes + 50L * zonesCrossed);
    }
}"""

TANGLED_EDGES = [
    ["Ride", "Bike"], ["Ride", "Dock"], ["Ride", "Rider"],
    ["Membership", "Rider"],
    ["FareCalculator", "Ride"], ["FareCalculator", "Rider"],
    ["FareCalculator", "Membership"], ["FareCalculator", "Dock"],
    ["Invoice", "FareCalculator"], ["Invoice", "Rider"],
]

STANDALONE_EDGES = [
    ["Ride", "Bike"], ["Ride", "Dock"], ["Ride", "Rider"],
    ["Membership", "Rider"],
    ["Tariff", "Fare"],
    ["Billing", "Ride"], ["Billing", "Membership"], ["Billing", "Tariff"],
    ["Invoice", "Fare"], ["Invoice", "Rider"],
]

LIBRARY_EXERCISE = """Loan    depends on  Book, Member, DueDate
Fine    depends on  Loan, Money
Notice  depends on  Fine, Member
Book, Member, DueDate and Money depend on no class of the model"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 10, opening (PDF pp. 147-148 of the operator's copy) and
    # Intention-Revealing Interfaces (pp. 149-152): Beck's selector (p. 150),
    # the paint example (pp. 150-151), subdomains behind such interfaces (p. 151).
    # Quote: PDF p. 150 of the operator's copy, 22 words, quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "intention-revealing-interfaces",
        "title": "Intention-Revealing Interfaces",
        "module": MODULE,
        "one_line": "Name every class, operation and argument for what it does and why, so that a client never has to read how.",
        "summary": (
            "Chapter 10 asks what kind of design a developer will want to work with, "
            "and answers with a set of patterns that make a design supple. The first is "
            "about names. Read Evans's case that encapsulation is lost when a client "
            "has to read the implementation, then list the names one routine declares "
            "and read each against what it tells a client."
        ),
        "key": [
            "a design must serve its developers too",
            "name the effect and purpose, not the means",
            "type, method and argument names together",
            "use the words of the Ubiquitous Language",
            "write the client's test first",
            "a long name can still name the means",
        ],
        "key_label": "Intention-Revealing Interfaces in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's, the third the lab's."
        ),
        "concepts": [
            ("Supple design",
             "Evans's name for a design that is a pleasure to change: its elements say "
             "what they mean, combine predictably, and bend at the points where the "
             "domain itself varies. He presents it as the complement of a deep model."),
            ("Intention-Revealing Interface",
             "An interface whose type names, operation names and argument names state "
             "what each element does and what it is for, in the team's language, without "
             "saying how. Evans builds it on Kent Beck's Intention-Revealing Selector."),
            ("A declared name",
             "A routine's parameters and local variables, in the order they appear. The "
             "lab lists them with their lengths and marks those shorter than the lesson's "
             "minimum; a variable declared in a loop's header is listed and not counted."),
        ],
        "read_title": "The chapter's question, the pattern, then one routine's names",
        "read_intro": (
            "Read the opening of Chapter 10 and the section Intention-Revealing "
            "Interfaces in your own copy first. The lesson reads the opening as an "
            "argument and the pattern as a tool, then reads the names of one routine."
        ),
        "body": [
            ("p", "&ldquo;Name classes and operations to describe their effect and "
                  "purpose, without reference to the means by which they do what they "
                  "promise.&rdquo; That is the first sentence of the pattern Evans calls "
                  "Intention-Revealing Interfaces, the first of the patterns in Chapter 10, "
                  "Supple Design. This lesson reads the chapter's opening and that "
                  "section. Read both in your own copy first."),
            ("p", "The chapter opens with a reader the book has so far left aside: the "
                  "developer. Software exists for its users, Evans says, but before it can "
                  "serve them it has to serve the people who build and keep changing it. "
                  "When a design with complicated behaviour is hard to read, developers "
                  "stop trusting their predictions of what a change will do; they copy "
                  "code rather than reuse it, avoid touching what works, and the system "
                  "hits a ceiling on how rich its behaviour can become. He calls the "
                  "alternative a supple design, one that invites change, and he sets it "
                  "beside the previous chapters: digging out implicit concepts gives the "
                  "raw material, and supple design shapes it."),
            ("p", "He is careful about what supple does not mean. Much over-engineering, "
                  "he notes, has been excused as flexibility, and layers of abstraction "
                  "usually get in the way; the designs that really help the people who "
                  "work with them tend to be simple, which is not the same as easy. A "
                  "design serves two roles, often played by one person: the client "
                  "developer who uses the domain objects, and the developer who changes "
                  "them. He admits he has never seen a large program that is supple "
                  "throughout, and offers the chapter's patterns as ones that tend to help "
                  "where they fit, not as a formula."),
            ("p", "Intention-Revealing Interfaces starts from encapsulation. An object's "
                  "value is that a client can use it without knowing the fine print of its "
                  "calculation. If the interface does not tell the client what it needs to "
                  "know, the client reads the internals anyway and the value is gone. "
                  "Worse, a second developer who infers an operation's purpose from its "
                  "code may infer one it serves only by accident; the code goes on "
                  "working, and the two developers are now working against each other."),
            ("p", "As a tool, then: every public element of a design is part of its "
                  "interface, and each name is a chance to say what the design intends. "
                  "Type names, method names and argument names together make the "
                  "interface. Name them for effect and purpose, in the words of the "
                  "Ubiquitous Language, and keep the mechanism behind them. Say what rule "
                  "holds and what event happens; leave how to the code. "
                  "Evans adds a working habit: write a test of the behaviour before you "
                  "write it, so that you are forced to think as its client."),
            ("p", "The book's example is a program for a paint shop whose single domain "
                  "class has a method whose name gives no hint of its effect. Evans writes "
                  "a test as a client would want to read it, finds the verb the domain "
                  "uses for what the method does, and renames it. He notes that the new "
                  "name does not say everything about the effect; that waits for the "
                  "Assertions lesson. He adds that whole subdomains can be carved off "
                  "behind such interfaces, which Chapter 15 takes up."),
            ("p", "Now a routine written for this lesson, from a theatre box office. It "
                  "answers whether a party can sit side by side in a row. The lab lists "
                  "the names it declares and marks those shorter than the lesson's minimum "
                  "of 5 characters. On the preset <code>means-names</code> it finds 4 "
                  "declared names, of which 3 are counted, since the loop index `i` is "
                  "listed and not counted: `row`, `k` and `run`, with a mean length of "
                  "7/3, about 2.33, and all three short. The method name, `scan`, is not "
                  "in the lab's list at all, and it names what the code does to an array, "
                  "not what the box office asks."),
            ("code", _lines(MEANS_NAMES)),
            ("p", "The preset <code>intention-names</code> is the same calculation as a "
                  "method of `SeatRow`, named for the question a clerk would ask. The lab "
                  "lists 3 declared names and counts 2, `partySize` and `freeInARow`, with "
                  "a mean length of 19/2, 9.50, and marks none as short; `seat`, declared "
                  "in the loop's header, is listed and not counted. The method name is "
                  "again outside the lab's list, and again it is the name that matters "
                  "most: `canSeatTogether` is what the box office asks."),
            ("code", _lines(INTENTION_NAMES)),
            ("p", "The preset <code>long-means</code> shows the limit of the count. It "
                  "lists 4 names, counts 3, marks none as short, and its mean length, "
                  "40/3, about 13.33, is the longest of the three. Yet "
                  "`scanArrayForZeroRun`, `seatFlags` and `currentZeroRun` all describe "
                  "the mechanism: an array, zeros, a run. A client still has to know that a "
                  "zero means a free seat. On the lab's figures this listing and "
                  "<code>intention-names</code> look alike, and only one of them reveals "
                  "its intention. Length is what the lab can count; whether a name states "
                  "effect and purpose is a reading of the name against the domain. Evans's "
                  "habit makes that reading concrete: the test below was written before "
                  "the method, and it reads as the box office speaks."),
            ("code", _lines(SEAT_TEST)),
            ("h3", "Exercise"),
            ("code", _lines(REFUND_EXERCISE)),
            ("p", "A method of `Booking` from the same box office. First, by the lab's "
                  "rule with a minimum of 5, list the declared names it counts and the "
                  "ones it marks as short. Then cover the body, say in one sentence what "
                  "the method promises, and give it a method name and an argument name "
                  "that say so. Paste the listing into the lab to check the first part; "
                  "the second the lab cannot check."),
            ("p", "A name tells a client what an operation is for, but not what it changes. "
                  "The next lesson, Side-Effect-Free Functions, makes the consequences of "
                  "calling an operation predictable."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "names",
            "min": 5,
            "preset": "means-names",
            "presets": [
                {"id": "means-names",
                 "label": "Names for the mechanism: scan, row, k, run",
                 "code": MEANS_NAMES,
                 "expect": {"coNames": "4", "coAvgLen": "7/3 ≈ 2.33",
                            "coShort": "row, k, run"}},
                {"id": "intention-names",
                 "label": "Names for the question: canSeatTogether",
                 "code": INTENTION_NAMES,
                 "expect": {"coNames": "3", "coAvgLen": "19/2 = 9.50", "coShort": "none"}},
                {"id": "long-means",
                 "label": "Long names, still about the mechanism",
                 "code": LONG_MEANS,
                 "expect": {"coNames": "4", "coAvgLen": "40/3 ≈ 13.33", "coShort": "none"}},
            ],
            "panel_title": "The names one routine declares",
            "panel_intro": (
                "The lab lists a routine's parameters and local names with their "
                "lengths and marks those shorter than the lesson's minimum of 5. It "
                "counts length, which is the one property of a name a count can see; "
                "whether a name reveals intention is read against the domain's words. "
                "The listings are the lesson's."
            ),
        }),
        "steps_title": "Reading an interface as its client",
        "steps_intro": "Five steps, the last of them on code of your own.",
        "steps": [
            ("Read the call, not the body",
             "Write down what a client sees: the type, the method name, each argument's "
             "type and name, and the return type."),
            ("Say what it promises",
             "From those names alone, write one sentence on what the operation does and "
             "what it is for. Where you cannot, the interface is hiding its intention."),
            ("Mark the names of means",
             "Mark every name that describes a mechanism (an array, a flag, a loop, a "
             "scan) rather than a concept the domain's experts would use."),
            ("Count, then read",
             "Run the lab for the names shorter than the minimum, and read each listed "
             "name against the Ubiquitous Language: short and exact, or short and vague."),
            ("Do it on your own code",
             "Pick one public method in a system you know, write a test for it as its "
             "client would want to read it, and rename the method and its arguments until "
             "the test reads as the domain's experts speak. Note how many names changed."),
        ],
        "worked": {
            "title": "Four names in a scan",
            "intro": [
                "List the declared names of <code>means-names</code> by the lab's rule, "
                "with a minimum of 5.",
            ],
            "lines": [
                "line 2: parameters row (3) and k (1)",
                "line 3: local run (3)",
                "line 4: loop index i, listed, not counted",
                "declared 4; counted 3",
                "mean length (3 + 1 + 3)/3 = 7/3",
                "shorter than 5: row, k, run",
            ],
            "after": [
                "The count says three names are short. Reading them says more: `k` is the "
                "party size, `run` the free seats found so far, and a zero in `row` a free "
                "seat. None of that is on the interface, so a client must read the body, "
                "which is the loss Evans describes.",
            ],
        },
        "quiz_title": "Names, intentions and Evans's claims",
        "quiz": [
            {"q": "In the exercise, by the lab's rule with a minimum of 5, which names "
                  "does the lab count, which does it mark as short, and what would a "
                  "revealing signature say?",
             "a": ["d, base and tmp, all three short; say refundCents(int daysBeforeShow)",
                   "d and tmp short, base not; say calculateAmount(int days)",
                   "amt, d, base and tmp, all four short; say getAmt(int d)",
                   "d, base and tmp, only d short; say refundCents(int days)"],
             "c": 0,
             "why": "The declared names are the parameter `d` and the locals `base` and "
                    "`tmp`; the method name `amt` is not a declared name. All three are "
                    "shorter than 5 (`base` has 4 letters). The body returns the full "
                    "price 14 or more days before the performance, nothing under 2 days, "
                    "and half otherwise, so the method promises a refund in cents for a "
                    "number of days before the show: `refundCents(int daysBeforeShow)`, "
                    "with locals such as `fullPrice` and `refund`. `calculateAmount` "
                    "names the means (a calculation) and not the effect."},
            {"q": "According to the section Intention-Revealing Interfaces, which names "
                  "together make up a design's interface?",
             "a": ["Method names only; types and arguments are implementation",
                   "Type names, method names and argument names",
                   "Class names and the comments above each public method",
                   "The names of private fields, which the methods reveal"],
             "c": 1,
             "why": "Evans says all the public elements of a design make up its interface, "
                    "and that type, method and argument names combine to form an "
                    "Intention-Revealing Interface. Comments and private fields are not "
                    "part of what he names."},
            {"q": "On the preset <code>long-means</code>, how many names does the lab mark "
                  "as short, and what does that show?",
             "a": ["3: long names are as opaque as short ones",
                   "1: only the loop index is short",
                   "0: and the names still describe an array, zeros and a run",
                   "0: so the interface reveals its intention"],
             "c": 2,
             "why": "None of `seatFlags`, `requiredRunLength` and `currentZeroRun` is "
                    "shorter than 5, and `index` is a loop index, listed and not counted. "
                    "The lab measures length; the names still describe the mechanism, so "
                    "the count cannot say the interface reveals intention."},
            {"q": "Why does Evans advise writing a test of a behaviour before creating it?",
             "a": ["To force the developer's thinking into the client developer's mode",
                   "To prove the implementation correct before it is written",
                   "To raise the test coverage of the domain layer",
                   "To document how the method does what it promises"],
             "c": 0,
             "why": "The pattern's statement says the test comes first so that you think as "
                    "the client developer does, the point of view from which "
                    "names are read. A test cannot prove a method correct, and documenting "
                    "the means is what the pattern says to leave out."},
        ],
        "mistakes": [
            ("Taking a long, descriptive name for an intention-revealing one",
             "A name reveals intention when it states the effect and purpose in the domain's "
             "words. `scanArrayForZeroRun` is long and describes the mechanism; `seat` is "
             "short and names the concept exactly. The lab counts length, which is why, on "
             "the lesson's illustration, it passes every name in <code>long-means</code>, "
             "whose mean length is the longest of the three; the reading against the domain "
             "is the reader's."),
            ("Making a design supple by adding layers of abstraction",
             "Evans warns that much over-engineering has been justified as flexibility, and "
             "that excessive abstraction and indirection get in the way. The designs he "
             "admires are simple, though not easy to make. A revealing name hides the means "
             "behind one clear element; it does not add an interface for its own sake."),
            ("Expecting a good name to say everything about an operation",
             "Evans says of his own renamed method that the name does not tell a reader "
             "everything about its effect. A name says what an operation is for; what it "
             "changes, and what it guarantees, are the work of the next two patterns, "
             "Side-Effect-Free Functions and Assertions."),
        ],
        "standard": (
            "Finish when you can say what an operation promises from its interface alone.",
            "Given a routine, list the names it declares and mark the short ones by the "
            "lab's rule, then rename the operation and its arguments to state its effect "
            "and purpose in the domain's words."
        ),
        "note": (
            "The lab reads one routine's parameters and local names and counts their "
            "length. It does not read the method name or the type names, and it cannot "
            "tell a name for the effect from a name for the means; that is a reading "
            "against the Ubiquitous Language, which only the team can make."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 10, Side-Effect-Free Functions (PDF pp. 152-155 of the operator's
    # copy): commands and queries (p. 152), Meyer 1988 and Fowler 1999 (p. 152),
    # the pattern (p. 153), the paint example (pp. 153-155).
    # Quote: PDF p. 153 of the operator's copy, 22 words, quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "side-effect-free-functions",
        "title": "Side-Effect-Free Functions",
        "module": MODULE,
        "one_line": "Put the logic in operations that return a result and change nothing, keep the commands that change state small, and let value objects carry the calculations.",
        "summary": (
            "Evans divides operations into commands, which change the system, and "
            "queries, which only answer. Read why he wants as much logic as possible in "
            "functions, and why he moves calculations into immutable value objects, then "
            "count who sees a change made through a shared value, mutable and immutable."
        ),
        "key": [
            "queries answer; commands change state",
            "a function: a result and no side effect",
            "keep commands simple, no domain data back",
            "move calculations into value objects",
            "a new value instead of a changed one",
        ],
        "key_label": "Side-Effect-Free Functions in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's, the third the lab's."
        ),
        "concepts": [
            ("Side effect",
             "In Evans's narrowed sense, a change to what the system holds that later "
             "operations will feel. He keeps the computing term, not the everyday sense "
             "of an unintended result, and explains why the two meet in complex systems."),
            ("Side-Effect-Free Function",
             "An operation that returns a result and causes no observable change. It "
             "returns the same answer each time, can be nested to any depth and is easy to "
             "test. Evans pairs it with commands kept separate and simple."),
            ("A surprised holder",
             "In the lab, an object that holds the shared value and sees it change, though "
             "the change was made through some other holder. A mutable shared value "
             "surprises every other holder; replacing an immutable one surprises none."),
        ],
        "read_title": "The argument, the pattern, then a shared value",
        "read_intro": (
            "Read the section Side-Effect-Free Functions in Chapter 10 first. The lesson "
            "reads its argument, states the pattern as a tool, and then counts the "
            "holders of one shared value."
        ),
        "body": [
            ("p", "&ldquo;Place as much of the logic of the program as possible into "
                  "functions, operations that return results with no observable side "
                  "effects.&rdquo; That is the first sentence of the pattern "
                  "Side-Effect-Free Functions, the second in Chapter 10. Read the section "
                  "in your own copy first."),
            ("p", "Evans starts with a division. Queries get information from the system, "
                  "perhaps by reading a variable, perhaps by computing from it. Commands, "
                  "also called modifiers, change the system. In computing a side effect is "
                  "any effect on state, and he narrows it further to a change that will "
                  "affect operations that come later. He asks why a word for unintended "
                  "consequences was taken for intended changes, and suggests an answer: "
                  "operations call operations, which call others, and a client cannot "
                  "foresee what the second and third tiers do. Their effects become side "
                  "effects in the everyday sense too."),
            ("p", "The cost is predictability. Once rules and calculations combine, the "
                  "developer calling an operation has to understand its implementation and "
                  "everything it delegates to, and the abstraction of its interface is "
                  "worth little. Functions avoid this: called again, a function returns the "
                  "same value; it can call other functions at any depth without worry; and "
                  "it is far easier to test. Evans concludes that functions lower risk."),
            ("p", "Commands cannot be avoided, so he offers two mitigations. First, keep "
                  "commands and queries in separate operations, after Bertrand Meyer: a "
                  "method that changes state returns no domain data and is as simple as it "
                  "can be, and every calculation happens in methods with no observable "
                  "effect. Second, look for a model in which nothing existing needs to "
                  "change at all, and answer with a new Value Object holding the result. A "
                  "value can be made in answer to a question, handed on and forgotten, "
                  "which an Entity cannot, since its life cycle is closely controlled."),
            ("p", "The pattern, as a tool: put the logic in functions; keep commands very "
                  "simple and returning no domain information; and where a concept fits the "
                  "responsibility, move complex logic into a value object. Evans sets the "
                  "order. Splitting an operation that both calculates and changes state is "
                  "a refactoring from Fowler's <em>Refactoring</em> (1999), and it applies "
                  "to entities. After it, consider a second refactoring that moves the "
                  "calculation into a value, which often removes the side effect "
                  "altogether. In the book's paint example he makes colour an explicit "
                  "immutable value, named for how paint mixes rather than how light does, "
                  "and mixing returns a new colour; the entity's command shrinks to a few "
                  "lines."),
            ("p", "The Value Objects lesson in the course The Building Blocks of a "
                  "Model-Driven Design counted the holders of one shared value. Here the "
                  "same count shows what a function buys. The code below is a clinic's "
                  "dose, written two ways: as a class that changes in place, and as a "
                  "value whose operation returns a new dose."),
            ("code", _lines(DOSE_TWO_WAYS)),
            ("p", "In the lab, four prescriptions hold doses: `rxAnna`, `rxBen` and "
                  "`rxCara` share one value, `fiveMg`, and `rxDev` holds `tenMg`. The "
                  "doctor doubles Ben's dose. On the preset <code>mutable-dose</code> the "
                  "change is made through `rxBen` with `scaleBy`, in place: 3 holders of "
                  "`fiveMg`, 3 see the change, 2 are surprised (Anna and Cara, whose doses "
                  "doubled though nobody changed their prescriptions), and 0 new values are "
                  "created."),
            ("p", "On the preset <code>immutable-dose</code> Ben's prescription is given "
                  "`fiveMg.times(2)` instead: 3 holders of `fiveMg`, 1 sees the change, "
                  "0 are surprised, and 1 new value is created, which the lab calls "
                  "`fiveMg′` and shows held by `rxBen`. Nothing that existed "
                  "before was changed; Ben's prescription now refers to a different value. "
                  "The figures are the model's, and the model is the lesson's: in a real "
                  "clinic the surprise in the first preset is a patient given twice the "
                  "dose."),
            ("code", _lines(PRESCRIPTION_COMMAND)),
            ("p", "The second listing is Evans's order of work on the entity. "
                  "`doubleAndReport` changed the dose and returned it, a command and a "
                  "query in one. Split, `doubled` is a function that can be called as often "
                  "as you like, to show the doctor what the new dose would be, and "
                  "`changeDoseTo` is a command of one line that returns nothing."),
            ("h3", "Exercise"),
            ("code", _lines(WINDOW_EXERCISE)),
            ("p", "Five bakery orders hold pickup windows, and order `b`'s window is "
                  "extended in place. Find the holders of the changed value, how many see "
                  "the change and how many are surprised. Then rewrite the last line so "
                  "that `Window` is immutable and `b` alone is given an extended window, "
                  "and give the same three figures and the number of new values. Type both "
                  "into the lab to check, separating the holders with semicolons: "
                  "`a, morning; b, morning; c, noon; …`."),
            ("p", "A function changes nothing, but some commands must remain, and their "
                  "effects still have to be understood. The next lesson, Assertions, "
                  "states them."),
        ],
        "lab": ("dddkit", {
            "mode": "identity",
            "view": "sharing",
            "preset": "mutable-dose",
            "presets": [
                {"id": "mutable-dose",
                 "label": "Ben's dose doubled in place: a mutable value",
                 "holders": [["rxAnna", "fiveMg"], ["rxBen", "fiveMg"],
                             ["rxCara", "fiveMg"], ["rxDev", "tenMg"]],
                 "value": "fiveMg", "change": "rxBen", "kind": "mutable",
                 "expect": {"didHolders": "3: rxAnna, rxBen, rxCara",
                            "didSee": "3: rxAnna, rxBen, rxCara",
                            "didSurprised": "2: rxAnna, rxCara", "didNew": "0"}},
                {"id": "immutable-dose",
                 "label": "Ben given a new value: an immutable dose",
                 "holders": [["rxAnna", "fiveMg"], ["rxBen", "fiveMg"],
                             ["rxCara", "fiveMg"], ["rxDev", "tenMg"]],
                 "value": "fiveMg", "change": "rxBen", "kind": "immutable",
                 "expect": {"didHolders": "3: rxAnna, rxBen, rxCara", "didSee": "1: rxBen",
                            "didSurprised": "0: none",
                            "didNew": "1: fiveMg′, now held by rxBen"}},
            ],
            "panel_title": "Who sees a change made through a shared value",
            "panel_intro": _DDD_INTRO,
        }),
        "steps_title": "Separating what changes from what computes",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Sort the operations",
             "Mark each public operation of a class as a query (it only answers) or a "
             "command (it changes state). Mark any that does both."),
            ("Split the ones that do both",
             "Write each mixed operation as a query that computes the answer and a command "
             "that applies it and returns nothing."),
            ("Look for the value",
             "Ask whether the calculation belongs to a concept of its own that could be an "
             "immutable value, and move it there as a function returning a new value."),
            ("Do it on your own code",
             "Find a shared object in a system you know that more than one holder refers "
             "to, and count the holders that would see a change made through one of them. "
             "Say whether the object should be a value."),
        ],
        "worked": {
            "title": "Three prescriptions, one dose",
            "intro": [
                "Count <code>mutable-dose</code> and <code>immutable-dose</code> by hand.",
            ],
            "lines": [
                "holders of fiveMg: rxAnna, rxBen, rxCara",
                "rxDev holds tenMg: not a holder",
                "mutable: all 3 see the doubled dose",
                "surprised: 3 − 1 = 2, Anna and Cara",
                "immutable: rxBen alone gets a new value",
                "sees 1, surprised 0, new values 1",
            ],
            "after": [
                "The two designs differ by one line of code and by two surprised holders. "
                "Which is right depends on what a dose means in the domain: a quantity, "
                "which is a value, and which Evans would compute with a function.",
            ],
        },
        "quiz_title": "Commands, functions and shared values",
        "quiz": [
            {"q": "In the exercise, how many orders hold the changed window, how many see "
                  "the change and how many are surprised; and with an immutable Window "
                  "given to b alone?",
             "a": ["3 hold it, 3 see it, 2 surprised; then 1 sees it, 0 surprised, 1 new value",
                   "5 hold a window, 5 see it, 4 surprised; then 1, 0 and 1",
                   "3 hold it, 1 sees it, 0 surprised; then 3 see it, 2 surprised",
                   "3 hold it, 3 see it, 3 surprised; then 1, 0 and 0 new values"],
             "c": 0,
             "why": "Orders `a`, `b` and `d` hold `morning`; `c` and `e` hold `noon`, which "
                    "is not changed. In place, all three holders of `morning` see the "
                    "extension, and two of them, `a` and `d`, did not make it. With an "
                    "immutable Window the last line becomes something like "
                    "`b.changeWindowTo(b.window().extendedBy(1))`: one new value, seen by "
                    "`b` alone, and nobody surprised. `b` made the change, so it is never "
                    "surprised."},
            {"q": "How does Evans narrow the meaning of side effect for his purposes?",
             "a": ["An unintended consequence of an operation",
                   "Any write to the database",
                   "Any change of state that later operations will be affected by",
                   "Any output an operation sends to the user"],
             "c": 2,
             "why": "He notes that standard English means an unintended consequence and "
                    "computer science any effect on state, and narrows it to a change in "
                    "state that will affect future operations. A database write or an "
                    "output is one kind of change, not his definition."},
            {"q": "What order of refactoring does the section recommend for an operation "
                  "that both calculates and changes state?",
             "a": ["First move the calculation into a value object, then split the method",
                   "First separate the modifier from the query, then consider moving the "
                   "calculation into a value object",
                   "Make the entity immutable, so that it has no commands",
                   "Only separate the query from the modifier; values are not involved"],
             "c": 1,
             "why": "Evans cites Fowler's refactoring for splitting an operation that mixes "
                    "calculation with state change, notes that this applies to entities, "
                    "and then suggests a second refactoring that moves the calculation into "
                    "a value object. An entity keeps its commands."},
            {"q": "On the preset <code>mutable-dose</code>, why is rxDev not counted as "
                  "surprised?",
             "a": ["It made the change",
                   "It holds tenMg, a different value, so the change does not reach it",
                   "Its dose is immutable",
                   "It was created after the change"],
             "c": 1,
             "why": "Only holders of `fiveMg` can see a change made to `fiveMg`; `rxDev` "
                    "refers to `tenMg`. The change was made through `rxBen`, and every "
                    "dose in the preset has the same kind."},
        ],
        "mistakes": [
            ("Believing a design can be made of functions alone",
             "Evans says plainly that commands cannot be avoided in most systems. His "
             "pattern puts as much logic as possible into functions and keeps the commands "
             "that remain separate, simple and returning no domain data; it does not "
             "abolish them."),
            ("Thinking that separating commands from queries is the whole pattern",
             "The separation is the first of two moves, and Evans says it applies to "
             "entities. The second is to move the calculation into a value object, which "
             "often removes the side effect entirely, because a new value is derived "
             "rather than existing state changed. On the lesson's illustration that second "
             "move takes the surprised holders from 2 to 0."),
            ("Making entities immutable too",
             "A value can be made in answer to a question and forgotten; an entity's life "
             "cycle matters in the domain and is carefully regulated, so a new one cannot "
             "simply be conjured up as a result. The prescription keeps its identity and "
             "one simple command; its dose is the value."),
        ],
        "standard": (
            "Finish when you can split an operation into a function and a simple command.",
            "Given a class and a shared object, sort its operations into commands and "
            "queries, rewrite a mixed one as both, and count the holders a change reaches "
            "when the shared object is mutable and when it is a replaced value."
        ),
        "note": (
            "The lab counts which holders of one value see one change, under the two "
            "kinds the lesson states. It does not read code, so it cannot tell whether an "
            "operation really has no side effect, and it cannot say whether a concept is "
            "a value or an entity in the domain; that is the modelling judgement Evans "
            "asks for."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 10, Assertions (PDF pp. 156-159 of the operator's copy): commands
    # that invoke commands (p. 156), Meyer 1988 and design by contract (p. 156),
    # the pattern (p. 156), people and predicates (p. 157), the paint example
    # (pp. 157-159); Declarative Design's opening on handwritten code (p. 166).
    # Quote: PDF p. 156 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "assertions",
        "title": "Assertions",
        "module": MODULE,
        "one_line": "State what an operation guarantees and what is always true of an object, so that a client can use a command without tracing it.",
        "summary": (
            "Functions leave a residue of commands whose effects a client must still "
            "understand. Read Evans's case for stating post-conditions and invariants, "
            "after Meyer's design by contract, then check the state an operation leaves "
            "against its assertions, clause by clause."
        ),
        "key": [
            "a post-condition: what a call guarantees",
            "a precondition: when the guarantee holds",
            "an invariant: true after every operation",
            "assertions describe state, not procedure",
            "no language support: write unit tests",
            "an odd assertion may hide a concept",
        ],
        "key_label": "Assertions in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, all from the design-by-contract school that "
            "Evans draws on."
        ),
        "concepts": [
            ("Post-condition",
             "A statement of the outcome an operation guarantees: the state it leaves "
             "behind, including its side effects. If you trust it, Evans says, you need not "
             "read how the method works."),
            ("Precondition",
             "A condition that must hold before the call for the post-condition to be "
             "guaranteed; Evans compares it to the fine print of a contract. A call that "
             "breaks it is owed nothing."),
            ("Invariant",
             "A statement about an object's state that is true at the end of every "
             "operation. Evans adds that invariants can be declared for a whole Aggregate, "
             "where they define its integrity rules."),
        ],
        "read_title": "The argument, the pattern, then the state a command leaves",
        "read_intro": (
            "Read the section Assertions in Chapter 10 first. The lesson reads the "
            "argument, states the pattern as a tool, and then checks the state one "
            "command leaves against what it promises."
        ),
        "body": [
            ("p", "&ldquo;If you trust the guarantee of a post-condition, you don't have to "
                  "worry about how a method works.&rdquo; That sentence is from the section "
                  "Assertions, the third pattern of Chapter 10. Read it in your own copy "
                  "first."),
            ("p", "Side-Effect-Free Functions cut the problem down, Evans says, but leave "
                  "commands on the entities, and anyone calling them has to understand "
                  "their consequences. A command with no complex computation can be read by "
                  "inspection. But in a design built from smaller parts, a command calls "
                  "other commands, and the caller must understand each of them, which "
                  "defeats encapsulation. And since an interface does not restrict side "
                  "effects, two classes implementing it can change different things, which "
                  "defeats the point of abstraction and polymorphism. When effects are "
                  "defined only by the code, the only way to understand the program is to "
                  "trace execution along its branches."),
            ("p", "Intention-revealing names help, but informal hints are not always "
                  "enough. Evans turns to the design-by-contract school, described in "
                  "Bertrand Meyer's book of 1988. A post-condition describes the "
                  "guaranteed outcome of a call, side effects included; a precondition is "
                  "what must hold for that guarantee; a class invariant is true of an "
                  "object whenever any operation finishes, and an invariant can cover a whole "
                  "Aggregate. All of them describe state rather than procedure, which is "
                  "why they are easier to analyse, and the effects of delegation are "
                  "already folded into them."),
            ("p", "As a tool: state the post-conditions of operations and the invariants of "
                  "classes and aggregates. Where the language cannot express them, check "
                  "them with automated tests, and record them wherever the team's process "
                  "keeps such things. Because assertions are about "
                  "state, the tests are easy to write: set up the preconditions, run the "
                  "operation, check the post-conditions. Evans adds a caution about "
                  "people: any consistent set of assertions would serve a compiler, but "
                  "developers extrapolate from the concepts of the model, so seek a model "
                  "whose assertions they could have guessed."),
            ("p", "The book's example returns to paint. Mixing one paint into another adds "
                  "the second's volume to the first and leaves the second unchanged, a "
                  "post-condition that does not fit anyone's idea of paint. The obvious fix, "
                  "emptying the second paint, turns out to break a requirement the original "
                  "designers knew about. Rather than document the odd post-condition, Evans "
                  "takes the awkwardness as a sign of a missing concept and splits the "
                  "class, so that the one remaining command does something any reader would "
                  "expect and the assertions become common sense."),
            ("p", "Now a command written for this lesson, from a bike-share scheme that "
                  "moves bikes between docks to rebalance them. The comment states its "
                  "post-condition, the class invariant and the precondition, and the test "
                  "after it does what Evans describes: precondition, call, post-condition."),
            ("code", _lines(DOCK_ASSERTIONS)),
            ("code", _lines(DOCK_TEST)),
            ("p", "The lab checks a stated state against the assertions written as one "
                  "specification. Each candidate is the state after `a.sendBikesTo(b, 3)`: "
                  "`removed` and `added` are the bikes taken from `a` and given to `b`, "
                  "`fromBikes` is what `a` holds after, and `toSpaces` is the room left in "
                  "`b`. The specification below is the post-condition, then the two "
                  "invariants that could break. On the preset <code>transfer-kept</code> "
                  "every clause holds, 4 of 4, and the specification is satisfied."),
            ("code", _lines(DOCK_SPEC)),
            ("p", "On the preset <code>transfer-overfull</code>, `b` started with only 2 "
                  "spaces. The post-condition's two clauses hold, but `toSpaces` is −1, and "
                  "the first false clause is `toSpaces >= 0`, the only entry in the lab's "
                  "list of every false clause: the invariant is broken. The "
                  "operation did what it promised, and the caller broke the precondition "
                  "that `n` fit in `b`. That is the fine print doing its work: it says whose "
                  "fault the broken invariant is."),
            ("p", "On the preset <code>transfer-one-sided</code>, an implementation forgot "
                  "the first line and never took the bikes out of `a`. Its `removed` is 0, "
                  "the first false clause is `removed = 3`, and the other three clauses "
                  "hold. Bikes have been created out of nothing, and only the stated "
                  "post-condition notices; nothing in the method's name would have."),
            ("h3", "Exercise"),
            ("code", _lines(VAULT_EXERCISE)),
            ("p", "A seed bank's vault holds 100 packets of a variety and must be flagged "
                  "for reordering whenever fewer than 30 are left. For each state after "
                  "`withdraw(80)`, say whether the assertions hold and, if not, the first "
                  "clause in the written order that is false. Then type the three states "
                  "into the lab as candidates to check, one record each, separated by "
                  "semicolons: `A, taken=80, left=20, reorder=yes; B, …`."),
            ("p", "With names, functions and assertions, each element is readable and safe "
                  "to use. The next lesson, Conceptual Contours, asks how a design should be "
                  "divided into elements in the first place."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "validate",
            "spec": DOCK_SPEC,
            "candidates": DOCK_STATES,
            "preset": "transfer-kept",
            "presets": [
                {"id": "transfer-kept",
                 "label": "Three bikes moved, both docks within bounds",
                 "candidate": "kept",
                 "expect": {"dspSatisfied": "yes", "dspTrue": "4 of 4",
                            "dspFirstFalse": "none: every clause is true", "dspFalse": "0: none"}},
                {"id": "transfer-overfull",
                 "label": "Three bikes into a dock with room for two",
                 "candidate": "overfull",
                 "expect": {"dspSatisfied": "no", "dspTrue": "3 of 4",
                            "dspFirstFalse": "clause 4, toSpaces >= 0: toSpaces is −1",
                            "dspFalse": "1: toSpaces >= 0"}},
                {"id": "transfer-one-sided",
                 "label": "An implementation that never removes the bikes",
                 "candidate": "oneSided",
                 "expect": {"dspSatisfied": "no", "dspTrue": "3 of 4",
                            "dspFirstFalse": "clause 1, removed = 3: removed is 0",
                            "dspFalse": "1: removed = 3"}},
            ],
            "panel_title": "The state a command leaves, against its assertions",
            "panel_intro": _DDD_INTRO,
        }),
        "steps_title": "Stating what a command guarantees",
        "steps_intro": "Five steps, the last of them on code of your own.",
        "steps": [
            ("Name the state",
             "List the quantities a command changes and the ones it must not, on the "
             "receiver and on any argument."),
            ("Write the post-condition",
             "State, without saying how, what each of those quantities is after the call "
             "in terms of what it was before."),
            ("Write the invariants and the precondition",
             "State what must be true of every object of the class after any operation, "
             "and what the caller must ensure for the post-condition to hold."),
            ("Turn them into a test",
             "Set up the precondition, make the call, and assert each clause; check the "
             "state a faulty implementation would leave, clause by clause, in the lab."),
            ("Do it on your own code",
             "Pick a command in a system you know that changes two objects. Write its "
             "post-condition and one invariant as a test, and note whether the assertion "
             "reads as common sense or needs explaining. If it needs explaining, say what "
             "concept might be missing."),
        ],
        "worked": {
            "title": "Three bikes, two docks",
            "intro": [
                "Check <code>transfer-overfull</code> clause by clause, in the written order.",
            ],
            "lines": [
                "removed = 3: removed is 3, true",
                "added = 3: added is 3, true",
                "fromBikes >= 0: 5, true",
                "toSpaces >= 0: −1, false",
                "3 of 4 clauses true",
                "first false clause: toSpaces >= 0",
            ],
            "after": [
                "The post-condition holds and an invariant does not, so the fault is "
                "outside the method: the call broke the precondition that three bikes fit "
                "in `b`. Stating the precondition is what lets you say so without reading "
                "the code.",
            ],
        },
        "quiz_title": "Post-conditions, preconditions and invariants",
        "quiz": [
            {"q": "In the exercise, which states satisfy the assertions, and what is the "
                  "first false clause, in the written order, of each that does not?",
             "a": ["A only; B fails at left >= 30, C at left = 20",
                   "A and B; C fails at left = 20",
                   "A only; B fails at reorder = yes, C at taken = 80",
                   "A and C; B fails at left >= 30"],
             "c": 0,
             "why": "The written order is `taken = 80`, `left = 20`, `left >= 30`, "
                    "`reorder = yes`. A satisfies all: it is below 30 and flagged. B keeps "
                    "the post-condition but is below 30 and not flagged; the first false "
                    "clause is `left >= 30`, and the invariant fails because both sides of "
                    "its `or` are false. C never took the packets out: `taken = 80` holds "
                    "and `left = 20` is false, the first false clause. Its 100 packets "
                    "would satisfy the invariant, which is why a post-condition is needed "
                    "beside it."},
            {"q": "On the preset <code>transfer-overfull</code>, the post-condition holds "
                  "and an invariant fails. Given the assertions in the listing's comment, "
                  "what does that show?",
             "a": ["The method is wrong: it should refuse the call",
                   "The caller broke the precondition that the bikes fit in the other dock",
                   "The invariant is wrong: a dock may hold more than its capacity",
                   "The lab cannot tell; a post-condition says nothing about invariants"],
             "c": 1,
             "why": "The method did what its post-condition promises. The precondition, "
                    "`n <= b.spaces()`, was not met, and a call that breaks a precondition "
                    "is owed no guarantee. A method might also check its precondition, but "
                    "the assertions as stated put the fault on the caller."},
            {"q": "How does the section describe preconditions?",
             "a": ["The guaranteed outcome of calling a method",
                   "What holds of an object whenever any of its operations finishes",
                   "Like the fine print of a contract: what must hold for the post-condition "
                   "to be guaranteed",
                   "The procedure a method follows, written as comments"],
             "c": 2,
             "why": "Evans gives the three kinds in turn: post-conditions are the guaranteed "
                    "outcome, preconditions the fine print that must be satisfied for that "
                    "guarantee, and class invariants what holds at the end of any "
                    "operation. All three describe state, not procedure."},
            {"q": "What does Evans advise when assertions cannot be coded directly in the "
                  "programming language?",
             "a": ["Leave them out, since unchecked assertions mislead",
                   "Write automated unit tests for them",
                   "Switch to a language that supports them",
                   "Replace them with intention-revealing names"],
             "c": 1,
             "why": "The pattern says to check assertions the language cannot state with "
                    "automated unit tests, and to record them in the project's documents "
                    "where its process allows. He calls them a powerful way of thinking "
                    "about design even without language support."},
        ],
        "mistakes": [
            ("Thinking assertions need a language that checks them",
             "Evans wrote when few object languages supported assertions, and says they are "
             "still a powerful way to think about a design. Where they cannot be coded, "
             "unit tests stand in: the setup puts the preconditions in place and the test "
             "checks the post-conditions after the call. The lesson's dock test is one."),
            ("Fixing an awkward post-condition by making the code match intuition",
             "In the paint example the intuitive fix broke a requirement the original "
             "designers had kept. Evans neither forces the fix nor settles for documenting "
             "the oddity; he reads the awkwardness as a sign of a missing concept and finds "
             "a model in which the assertions make sense. Sometimes, he grants, the odd "
             "post-condition documented is the best answer."),
            ("Reading satisfied assertions as proof that an operation is correct",
             "Assertions say only what they say. Evans opens Declarative Design by noting "
             "that handwritten code can still have side effects that no assertion "
             "excluded. On the lesson's illustration, a transfer that also cleared a "
             "dock's maintenance flag would satisfy all four clauses."),
        ],
        "standard": (
            "Finish when you can state a command's guarantee and check a state against it.",
            "Given a command, write its post-condition, a class invariant and its "
            "precondition, and say for a stated result which clause, if any, fails first."
        ),
        "note": (
            "The lab checks one stated state against one stated set of clauses. It does "
            "not run the operation, so it cannot find a state the code might leave that "
            "nobody wrote down, and it cannot say whether the assertions are the right "
            "ones for the domain, which is the question Evans's paint example turns on."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 10, Conceptual Contours (PDF pp. 159-163 of the operator's copy):
    # granularity (p. 159), consistency of domains (p. 159), cohesion and
    # coupling of concepts (p. 159), Whole Value (p. 159 footnote), the pattern
    # (p. 160), the accruals example (pp. 160-163).
    # Quotes: PDF p. 160, 22 words, and PDF p. 159, 8 words; quotes.py OK.
    # Lesson total: 30 words.
    {
        "slug": "conceptual-contours",
        "title": "Conceptual Contours",
        "module": MODULE,
        "one_line": "Divide operations, classes and aggregates where the domain itself divides, and read where changes land as a test of the fit.",
        "summary": (
            "No rule of size, small or large or uniform, tells you how to divide a design. "
            "Read Evans's case for following the domain's own divisions, found by "
            "watching where change falls, then count the modules each change request "
            "touches under two divisions of one school timetable."
        ),
        "key": [
            "no rule of size divides a design",
            "follow the divisions in the domain",
            "watch the axes of change and stability",
            "local changes indicate a fit",
            "a sweeping change says: learn more",
        ],
        "key_label": "Conceptual Contours in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is Evans's, the second Ward "
            "Cunningham's as Evans cites it, the third the lab's."
        ),
        "concepts": [
            ("Conceptual Contour",
             "A line along which the domain itself divides, so that a design cut there "
             "keeps related things together and changes mostly in one place. Evans says "
             "the contours emerge as code is adapted to new concepts and requirements."),
            ("Whole Value",
             "Ward Cunningham's pattern, which Evans cites: each object should be one "
             "complete concept. Evans puts it beside his own rule that an operation with a "
             "coherent meaning in the domain should be one operation, not split into steps."),
            ("A module touch",
             "In the lab, one module that one change request reaches: a change that "
             "touches elements in three modules makes three touches. The lab adds them "
             "over the requests and reports the changes confined to one module."),
        ],
        "read_title": "The argument, the pattern, then two divisions of one model",
        "read_intro": (
            "Read the section Conceptual Contours in Chapter 10 first. The lesson reads "
            "the argument, states the pattern as a tool, and then counts where change "
            "requests land under two divisions of one model."
        ),
        "body": [
            ("p", "&ldquo;When successive refactoring tends to be localized, not shaking "
                  "multiple broad concepts of the model, it is an indicator of model "
                  "fit.&rdquo; That is from the section Conceptual Contours, the fourth "
                  "pattern of Chapter 10. Read it in your own copy first."),
            ("p", "Evans begins with three habits: chopping functionality fine so that it "
                  "can be recombined, lumping it large to hide complexity, and keeping "
                  "every class and operation to one scale. He calls all three "
                  "oversimplifications, though each answers a real problem. A monolith "
                  "duplicates what it embeds, hides what a client cares about, and mixes "
                  "concepts until none is clear. Breaking things into tiny pieces makes the "
                  "client assemble them, and a concept can vanish in the cutting: "
                  "&ldquo;Half of a uranium atom is not uranium.&rdquo; What matters is "
                  "not only the size of the grain but the direction it runs in."),
            ("p", "No cookbook rule works, he says, but most domains have a deep logical "
                  "consistency, or they would not work as fields of knowledge. Because of "
                  "it, a model that fits one part of a domain is likely to fit parts "
                  "discovered later; when it does not, you refactor toward deeper insight. "
                  "That is why, in his account, repeated refactoring leads to suppleness: "
                  "the contours appear as the code is adapted to concepts and requirements "
                  "newly understood."),
            ("p", "High cohesion and low coupling, he goes on, are principles for concepts "
                  "and not only for code, and to keep them from turning mechanical he asks a question at "
                  "each decision: is this an expedient that suits the present code, or does "
                  "it follow a contour of the domain? If adding two objects means something "
                  "in the domain, implement it as one operation. Each object should be one "
                  "complete concept, Cunningham's Whole Value. And where the users have no "
                  "interest in detail, keep it together: in the paint example customers mix "
                  "whole paints and never single pigments, so pigments are not offered as "
                  "separate parts."),
            ("p", "The pattern, as a tool: divide the design into cohesive units where you "
                  "sense the domain divides; over several rounds of refactoring, notice what "
                  "keeps changing together and what stays put, and look for the domain lines "
                  "that explain it. Evans "
                  "is frank that this is hard to do up front and seldom comes from purely "
                  "technical refactoring. When a new requirement forces sweeping change in "
                  "how objects and methods are divided, he reads it as a message that the "
                  "team's understanding of the domain needs refining."),
            ("p", "His example, The Contours of Accruals, returns to the loan model "
                  "refactored in Chapter 9. Schedules that had been worked out by case logic "
                  "became a family of classes, and payments that had been kept apart were "
                  "brought together. When an unforeseen requirement for early and late "
                  "payments arrived, it connected to the single payment class without "
                  "duplication. Evans stresses that this was not because the developer "
                  "foresaw it, nor because the design could take any change, but because it "
                  "had been aligned with the domain's concepts."),
            ("p", "The lab's model is a school timetable written for this lesson. Nine "
                  "elements (rules, clash checks and printed views) are divided two ways. "
                  "By processing step: `checks` holds the four room and teacher rules, "
                  "`clashes` the two clash checks, `printing` the two views, and `periods` "
                  "the period length. By concept: `rooms` holds everything about rooms, "
                  "`teachers` everything about teachers, and `periods` the period length. "
                  "Four change requests arrive in a term: science labs, part-time teachers, "
                  "shorter Friday periods and large-type printouts."),
            ("p", "On the preset <code>term-requests</code>, the division by step takes 9 "
                  "module touches over the four changes and confines 1 change to one "
                  "module: science labs touch 3 modules, part-time teachers 3, short "
                  "Fridays 2, large type 1. The division by concept takes 7 touches and "
                  "confines 2: science labs 1, part-time teachers 1, short Fridays 3 and "
                  "large type 2. The lab also names the largest change under each: "
                  "science labs at 3 modules by step, the first given of the two that tie "
                  "there, and short Fridays at 3 by concept."),
            ("p", "The two other presets split that term. On "
                  "<code>rooms-and-teachers</code>, the two changes about one concept each, "
                  "the step division takes 6 touches and the concept division 2. On "
                  "<code>cross-cutting</code>, short Fridays and large type, the step "
                  "division takes 3 and the concept division 5. Neither division is local "
                  "for every change. Which one follows the contours is a question about "
                  "which changes keep arriving, which is why Evans says to watch them over "
                  "successive refactorings rather than choose from one list. If short "
                  "Fridays kept recurring, the concept division would be telling the team "
                  "that time is a concept it has not yet modelled."),
            ("h3", "Exercise"),
            ("code", _lines(TIMETABLE_EXERCISE)),
            ("p", "Two more requests for the same timetable. For each division, by step and "
                  "by concept, give the modules each request touches, the total of module "
                  "touches and the number of requests confined to one module. Then enter "
                  "them in the lab as changes to check, one record for each element a "
                  "request touches, separated by semicolons: `examWeeks, clashCheckRoom; "
                  "examWeeks, printRoomView; …`."),
            ("p", "A design cut along the contours still leaves each class depending on "
                  "others. The next lesson, Standalone Classes and Closure of Operations, "
                  "counts those dependencies."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "packagings": 2,
            "names": ["by step", "by concept"],
            "elements": TIMETABLE_ELEMENTS,
            "preset": "term-requests",
            "presets": [
                {"id": "term-requests",
                 "label": "One term's four requests, under both divisions",
                 "changes": CHANGES_TERM,
                 "expect": {"dmoChanges": "4",
                            "dmoPer": "scienceLabs 3, partTimeTeachers 3, shortFridays 2, largeType 1",
                            "dmoTotal": "9", "dmoConfined": "1 of 4: largeType",
                            "dmoLargest": "scienceLabs, 3 modules",
                            "dmoPer2": "scienceLabs 1, partTimeTeachers 1, shortFridays 3, largeType 2",
                            "dmoTotal2": "7", "dmoConfined2": "2 of 4: scienceLabs, partTimeTeachers",
                            "dmoLargest2": "shortFridays, 3 modules"}},
                {"id": "rooms-and-teachers",
                 "label": "The two requests about one concept each",
                 "changes": CHANGES_CONCEPTS,
                 "expect": {"dmoTotal": "6", "dmoConfined": "0 of 2", "dmoTotal2": "2",
                            "dmoConfined2": "2 of 2: scienceLabs, partTimeTeachers"}},
                {"id": "cross-cutting",
                 "label": "The two requests that cut across rooms and teachers",
                 "changes": CHANGES_ACROSS,
                 "expect": {"dmoTotal": "3", "dmoConfined": "1 of 2: largeType", "dmoTotal2": "5",
                            "dmoConfined2": "0 of 2"}},
            ],
            "panel_title": "The modules each change request touches",
            "panel_intro": _DDD_INTRO,
        }),
        "steps_title": "Reading where change falls",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("List the elements and their homes",
             "Write each element of the design beside the module it is in, under each "
             "division you are comparing."),
            ("Trace the requests",
             "For each change request, list the elements it touches, then the distinct "
             "modules those elements are in."),
            ("Read the pattern of change",
             "Mark the requests that stay in one module and those that spread, and ask "
             "what concept the spreading ones have in common."),
            ("Do it on your own design",
             "Take the last five changes to a system you know, count the modules each "
             "touched, and name the one concept that, made a module of its own, would "
             "have kept the most of them local."),
        ],
        "worked": {
            "title": "Short Fridays, both ways",
            "intro": [
                "Count the touches of one request, shortFridays, under each division.",
            ],
            "lines": [
                "touches periodLengthRule, clashCheckRoom,",
                "and clashCheckTeacher",
                "by step: periods, clashes, clashes",
                "distinct modules: 2",
                "by concept: periods, rooms, teachers",
                "distinct modules: 3",
            ],
            "after": [
                "The division by concept, local for the room and teacher requests, spreads "
                "this one across three modules. Evans would read that as a question about "
                "the model, whether time is a concept still hidden in two clash checks, "
                "and not as a score against the division.",
            ],
        },
        "quiz_title": "Contours, change and Evans's claims",
        "quiz": [
            {"q": "In the exercise, what are the module touches in total and the requests "
                  "confined to one module, for the division by step and for the division "
                  "by concept?",
             "a": ["By step 6 touches and 0 confined; by concept 3 touches and 1 confined",
                   "By step 5 touches and 1 confined; by concept 3 touches and 1 confined",
                   "By step 6 touches and 0 confined; by concept 4 touches and 0 confined",
                   "By step 3 touches and 2 confined; by concept 6 touches and 0 confined"],
             "c": 0,
             "why": "By step, exam weeks touch `clashes`, `printing` and `periods` (3), "
                    "and teacher cover touches `checks`, `clashes` and `printing` (3): 6, "
                    "none in one module. By concept, exam weeks touch `rooms` and "
                    "`periods` (2), and teacher cover only `teachers` (1): 3, with one "
                    "request confined."},
            {"q": "On the preset <code>term-requests</code>, how many module touches does "
                  "each division take?",
             "a": ["By step 9, by concept 7",
                   "By step 7, by concept 9",
                   "By step 12, by concept 12",
                   "By step 4, by concept 4"],
             "c": 0,
             "why": "By step: 3 + 3 + 2 + 1 = 9. By concept: 1 + 1 + 3 + 2 = 7. Twelve is "
                    "the number of element touches, the same under both divisions, since "
                    "the requests touch the same elements; four is the number of requests."},
            {"q": "What does Evans say it means when a new requirement forces sweeping "
                  "changes to how the objects and methods are divided?",
             "a": ["That the design should have been made more general up front",
                   "That the classes are too finely divided",
                   "That the team's understanding of the domain needs refining",
                   "That the requirement lies outside the Bounded Context"],
             "c": 2,
             "why": "He calls such a requirement a message that understanding of the "
                    "domain needs refinement, and an opportunity to deepen the model. He "
                    "argues against designing for every conceivable change up front, and "
                    "against any fixed rule of granularity."},
            {"q": "In The Contours of Accruals, why does Evans say the unanticipated "
                  "payment rules fitted the new model easily?",
             "a": ["The developer had anticipated that change",
                   "The design was versatile enough for any conceivable change",
                   "The previous refactoring had aligned the design with the domain's concepts",
                   "The payment classes had been split so that each could change alone"],
             "c": 2,
             "why": "Evans rules out the first two explicitly and gives the third. The "
                    "fourth is the reverse of the example: payments that had been kept "
                    "separate were lumped into one class, which is why the new rules "
                    "connected to it without duplication."},
        ],
        "mistakes": [
            ("Looking for a rule of size: small classes, large ones, or one scale for all",
             "Evans names all three habits and calls each an oversimplification that does "
             "not work as a general rule, though each answers a real problem. What counts "
             "is where the grain runs, and that is read from the domain, not from a size."),
            ("Expecting to find the contours before writing the design",
             "Evans says a simple set of interfaces that follow the contours is typically "
             "an outcome of refactoring and hard to produce up front, and that it emerges "
             "from refactoring toward deeper insight rather than technical refactoring. "
             "The axes of change are observed over successive changes."),
            ("Reading a lower total of module touches as proof that a division fits",
             "The total depends on which requests are listed. On the lesson's "
             "illustration the division by concept takes fewer touches over the term's "
             "four requests and more over the two that cut across it. A spreading change "
             "is, for Evans, a prompt to deepen the model, not a verdict on the division."),
        ],
        "standard": (
            "Finish when you can count where change requests land under two divisions.",
            "Given elements in two divisions and a list of change requests, give the "
            "modules each request touches, the totals and the requests confined to one "
            "module, and name the concept a spreading request shares."
        ),
        "note": (
            "The lab counts modules touched by the requests the lesson lists. It cannot "
            "foresee the requests that will come, and it cannot tell whether a division "
            "follows the domain's contours; Evans says that is learnt over successive "
            "refactorings and by touching base with the domain, not computed."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 10, Standalone Classes (PDF pp. 163-164 of the operator's copy) and
    # Closure of Operations (pp. 164-166): the snowball of dependencies (p. 163),
    # implicit concepts and primitives (pp. 163-164), the pattern (p. 164), the
    # Math Forum epigraph (p. 164), closure (p. 165), entities (p. 165), halfway
    # (p. 165), selecting from collections (pp. 165-166), the summary (p. 166).
    # Quote: PDF p. 164 of the operator's copy, 13 words, quotes.py OK.
    # Lesson total: 13 words.
    {
        "slug": "standalone-classes-and-closure",
        "title": "Standalone Classes and Closure of Operations",
        "module": MODULE,
        "one_line": "Cut every dependency that is not basic to a concept, factor intricate computations into classes that stand alone, and let operations return the type they take.",
        "summary": (
            "Every association, argument type and return type is one more concept a reader "
            "has to hold in mind. Read Evans's case for classes that can be understood "
            "alone and for operations closed under their own type, then follow a change "
            "through the dependencies of a bike-share fare, tangled and standalone."
        ),
        "key": [
            "each dependency adds a concept to hold",
            "hidden concepts count as much as explicit",
            "remove what is not basic to the concept",
            "intricate computation, standalone class",
            "closure: returns the type it takes",
            "rich interfaces, not bare primitives",
        ],
        "key_label": "Standalone Classes and Closure in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's, the third the lab's."
        ),
        "concepts": [
            ("Standalone Class",
             "A class with no dependencies beyond primitives and basic library types, which "
             "can be studied, understood and tested by itself. Evans calls it an extreme of "
             "low coupling."),
            ("Closure of Operations",
             "An operation whose return type is the type of its arguments, the receiver "
             "counted as one of them, as adding two whole numbers gives a whole number. It "
             "offers a rich interface without bringing in another concept."),
            ("Reached by a change",
             "In the lab, a class that depends, directly or through others, on the class "
             "that changes. The lab lists the direct dependents and every class reached, "
             "with each one's distance in edges."),
        ],
        "read_title": "Two patterns, then a change followed through the dependencies",
        "read_intro": (
            "Read the sections Standalone Classes and Closure of Operations in Chapter 10 "
            "first. The lesson reads both, then follows one change through two designs of "
            "the same fare."
        ),
        "body": [
            ("p", "&ldquo;Every dependency is suspect until proven basic to the concept "
                  "behind the object.&rdquo; That is from the section Standalone Classes, the "
                  "fifth pattern of Chapter 10, which this lesson reads with the sixth, "
                  "Closure of Operations. Read both in your own copy first."),
            ("p", "Evans counts the cost of a dependency in what a reader must think about. "
                  "Every association is one, and so is the type of every argument and every "
                  "return value. With one dependency you think about two classes and their "
                  "relationship; with two, about three classes, two relationships and "
                  "whatever relates the other two; and the things depended on have "
                  "dependencies of their own. Modules and Aggregates exist partly to limit "
                  "this web, but even inside a module, he says, the difficulty grows "
                  "quickly with each dependency added."),
            ("p", "Implicit concepts count as much as explicit references. A few basics, "
                  "such as Java's primitives, strings and collections, are always in mind and "
                  "add nothing. But what a primitive stands for is another matter: in the "
                  "paint example, three public integers were a colour, and making colour an "
                  "explicit class did not add a concept, it showed one that was already "
                  "there. A collection's size, by contrast, is just a count, and implies "
                  "nothing new."),
            ("p", "As a tool: scrutinise each association and operation, and remove every "
                  "dependency that is not essential; where you can, go all the way to a "
                  "class that stands alone. Evans qualifies this at once. Dependencies inside "
                  "one module do less harm than those outside it, two concepts that really "
                  "are tightly coupled may be clearer with several operations between them, "
                  "and the goal is to remove what is inessential, not everything. Move the "
                  "hardest computations into classes that stand alone, for instance value "
                  "objects that the more connected classes hold. And do not dumb a model down by "
                  "reducing everything to primitives."),
            ("p", "Closure of Operations is his answer to that last point. The section opens "
                  "with a definition of closure from the Math Forum at Drexel University: the "
                  "real numbers are closed under multiplication, since multiplying two of "
                  "them never leaves the set. Where it fits, give an operation a result "
                  "of the same type as its arguments, counting the receiver as an "
                  "argument when its state is used. Such an operation gives a high-level "
                  "interface without depending on any other concept, and closed operations "
                  "are easy to chain. Evans's examples are a transformation from one XML "
                  "document to another and, in the book's own code, the mixing of two "
                  "colours."),
            ("p", "He adds three refinements. Closure is mostly a property of value objects: "
                  "an entity is seldom the result of a computation, though asking an "
                  "employee for a supervisor returns an employee. Closure can hold for "
                  "an abstract type, with arguments of different concrete classes. And an operation that gets halfway, its "
                  "argument or its result of another type, keeps most of the benefit when "
                  "that type is a primitive or a basic library class. His example of the "
                  "last is selection from a collection: in Java an iterator brings in a "
                  "mechanism the problem does not need, while Smalltalk's select takes a "
                  "block, a basic type, and returns a collection that can be filtered "
                  "again."),
            ("p", "Now a fare for a bike-share scheme, written for this lesson. In the "
                  "tangled design one class computes it from a ride, a rider and a "
                  "membership, and reaches through the ride to the docks it started and "
                  "ended at, a dependency on `Dock` that appears in no signature. On the "
                  "preset <code>tangled-dock</code> the lab follows a change to `Dock`: "
                  "2 classes depend on it directly, `FareCalculator` and `Ride`, and 3 are "
                  "reached in all, with `Invoice` at distance 2."),
            ("code", _lines(TANGLED_FARE)),
            ("p", "In the standalone design the arithmetic lives in `Fare`, which depends on "
                  "nothing but `long` and `int`, and `Tariff` states the rule over plain "
                  "numbers and answers with a `Fare`. A `Billing` service does the "
                  "connecting: it reads the ride and the membership and asks the tariff. On "
                  "the preset <code>standalone-dock</code> the same change to `Dock` reaches "
                  "1 class directly, `Ride`, and 2 in all, `Ride` and `Billing`. The fare "
                  "rule is out of reach. On <code>standalone-fare</code> a change to `Fare` "
                  "itself reaches 2 classes directly, `Invoice` and `Tariff`, and 3 in all, "
                  "with `Billing` at distance 2: the holders of a value depend on it, and it "
                  "depends on none of them."),
            ("code", _lines(STANDALONE_FARE)),
            ("p", "Read the converse of the ripple too. To understand `FareCalculator` you "
                  "must hold `Ride`, `Rider`, `Membership` and `Dock` in mind, and `Bike` "
                  "through `Ride`: 5 concepts. To understand `Tariff` you need `Fare`; to "
                  "understand `Fare`, nothing. `plus` is closed under `Fare`, so it adds no "
                  "concept beyond the class itself, which is why the model lists no edge for "
                  "it. `lessPercent` is halfway, taking an "
                  "`int`, which costs a reader almost nothing."),
            ("h3", "Exercise"),
            ("code", _lines(LIBRARY_EXERCISE)),
            ("p", "A library's model, written for this exercise. Give every class `Notice` "
                  "depends on, directly and in all, and name the classes that are "
                  "standalone in this model. Then, in the lab, enter the edges, one record "
                  "for each dependency, separated by semicolons (`Loan, Book; Loan, Member; "
                  "…`), and a change to `DueDate`, and give the classes it reaches in all."),
            ("p", "These five patterns make elements readable, predictable and loosely "
                  "coupled. The next lesson, Declarative Design, asks how far that can go "
                  "toward a program that is its own specification."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "tangled-dock",
            "presets": [
                {"id": "tangled-dock",
                 "label": "Tangled: a change to Dock, with the fare rule in FareCalculator",
                 "edges": TANGLED_EDGES, "changed": "Dock",
                 "expect": {"dgDirect": "2: FareCalculator, Ride",
                            "dgAffected": "3: FareCalculator, Invoice, Ride"}},
                {"id": "standalone-dock",
                 "label": "Standalone: the same change, with the rule in Tariff and Fare",
                 "edges": STANDALONE_EDGES, "changed": "Dock",
                 "expect": {"dgDirect": "1: Ride", "dgAffected": "2: Billing, Ride"}},
                {"id": "standalone-fare",
                 "label": "Standalone: a change to Fare itself",
                 "edges": STANDALONE_EDGES, "changed": "Fare",
                 "expect": {"dgDirect": "2: Invoice, Tariff",
                            "dgAffected": "3: Billing, Invoice, Tariff"}},
            ],
            "panel_title": "The classes a change reaches",
            "panel_intro": (
                "Each record is a dependent class and the class it depends on. The lab "
                "follows a change backwards along the records to every class that depends "
                "on the changed one, directly or through others. The models are the "
                "lesson's."
            ),
        }),
        "steps_title": "Counting what a class asks you to hold in mind",
        "steps_intro": "Five steps, the last of them on code of your own.",
        "steps": [
            ("List the dependencies",
             "For one class, write every type it names: fields, arguments, return values, "
             "and the types reached through calls such as `ride.start()`."),
            ("Strike the basics",
             "Strike primitives and basic library types, unless they stand for a domain "
             "concept, as three integers once stood for a colour."),
            ("Question each one left",
             "For each remaining dependency, say whether it is basic to the class's "
             "concept. If not, say where the computation that needs it could go."),
            ("Look for closure",
             "Mark each operation whose arguments and result are of the class's own type, "
             "and each that is halfway, with a primitive on one side."),
            ("Do it on your own code",
             "Pick the class in a system you know that holds its most intricate "
             "calculation. Count the concepts it depends on in all, and write the "
             "signature of a standalone value class that could take the calculation over."),
        ],
        "worked": {
            "title": "A change to Dock, tangled",
            "intro": [
                "Follow <code>tangled-dock</code> backwards along the records by hand.",
            ],
            "lines": [
                "Ride depends on Dock: distance 1",
                "FareCalculator depends on Dock: distance 1",
                "Invoice depends on FareCalculator: 2",
                "Membership depends on Rider only",
                "direct: FareCalculator, Ride",
                "in all: FareCalculator, Invoice, Ride",
            ],
            "after": [
                "The fare rule is reached by a change to the docks, though no signature "
                "of `FareCalculator` mentions a dock. That is the implicit dependency Evans "
                "counts as heavily as an explicit one, and the one the standalone design "
                "removes.",
            ],
        },
        "quiz_title": "Dependencies, standalone classes and closure",
        "quiz": [
            {"q": "In the exercise, which classes does Notice depend on in all, which are "
                  "standalone, and which does a change to DueDate reach?",
             "a": ["In all Fine, Member, Loan, Money, Book, DueDate; standalone Book, Member, "
                   "DueDate, Money; DueDate reaches Loan, Fine, Notice",
                   "In all Fine, Member; standalone Book, DueDate, Money; DueDate reaches Loan",
                   "In all Fine, Member, Loan, Money; standalone Money only; DueDate reaches "
                   "Loan, Fine",
                   "In all Fine, Member, Loan, Book, DueDate; standalone Book, Member; DueDate "
                   "reaches Loan, Fine, Notice"],
             "c": 0,
             "why": "`Notice` depends directly on `Fine` and `Member`; through `Fine` on "
                    "`Loan` and `Money`; through `Loan` on `Book` and `DueDate` (and "
                    "`Member` again): six classes. The four that depend on no class of the "
                    "model are standalone in it. A change to `DueDate` reaches `Loan` at "
                    "distance 1, `Fine` at 2 and `Notice` at 3."},
            {"q": "Which of these operations is closed in Evans's sense?",
             "a": ["Fare lessPercent(int percent), in Fare",
                   "Fare forRide(int minutes, int zonesCrossed), in Tariff",
                   "Fare plus(Fare other), in Fare",
                   "long cents(), in Fare"],
             "c": 2,
             "why": "`plus` takes a Fare, uses the receiving Fare's state, and returns a "
                    "Fare. `lessPercent` is halfway, with an `int` argument; `cents` returns "
                    "a primitive; and `forRide` belongs to `Tariff`, takes integers and "
                    "returns a Fare, so neither its arguments nor its receiver are of the "
                    "result's type."},
            {"q": "On the preset <code>tangled-dock</code>, how many classes does the change "
                  "to Dock reach in all?",
             "a": ["2: FareCalculator and Ride",
                   "3: FareCalculator, Invoice and Ride",
                   "4: FareCalculator, Invoice, Membership and Ride",
                   "5: every class but Dock"],
             "c": 1,
             "why": "`Ride` and `FareCalculator` depend on `Dock` directly, and `Invoice` "
                    "depends on `FareCalculator`. `Membership` depends only on `Rider`, and "
                    "`Bike` and `Rider` depend on nothing, so the change does not reach them."},
            {"q": "What does Evans say about Closure of Operations and entities?",
             "a": ["Closure applies only to entities, whose identity is stable",
                   "An entity cannot have a closed operation",
                   "Closed operations exist on entities, but entities are seldom the result "
                   "of a computation, so look for closure mostly in value objects",
                   "An entity becomes a value object once its operations are closed"],
             "c": 2,
             "why": "He gives the example of asking an employee for a supervisor, which "
                    "returns an employee, so closed operations on entities exist. But since "
                    "an entity's life cycle matters in the domain, a new one cannot be "
                    "conjured up to answer a question, and he points the reader to value "
                    "objects."},
        ],
        "mistakes": [
            ("Making a class standalone by stripping its interface to primitives",
             "Evans warns against dumbing a model down by reducing everything to "
             "primitives, and offers Closure of Operations as a way to keep a rich "
             "interface while adding no dependency. `Fare plus(Fare)` is richer than "
             "`long plus(long)` and costs a reader nothing more."),
            ("Counting only the types in a class's signatures",
             "Implicit concepts count as much as explicit references, Evans says, whether "
             "they are recognised or not. On the lesson's illustration, `FareCalculator` "
             "names no dock, yet it reaches the docks through the ride, and a change to "
             "`Dock` reaches it. An integer that stands for a domain concept is a "
             "dependency on that concept."),
            ("Aiming at zero dependencies for every class",
             "The goal is to remove the inessential ones. Dependencies within a module do "
             "less harm, and when two concepts really are tightly coupled, several "
             "operations between them can make the relationship clearer. A standalone "
             "class is the extreme, worth reaching for the most intricate computations."),
        ],
        "standard": (
            "Finish when you can count what a class depends on and find a closed operation.",
            "Given a model's dependencies, list a class's dependencies directly and in all, "
            "name the standalone classes and the classes a change reaches, and say which "
            "operations are closed and which are halfway."
        ),
        "note": (
            "The lab follows the records the lesson states. It cannot find a dependency "
            "nobody wrote down, such as the dock reached through a ride or the concept "
            "hidden in an integer, and it cannot say which dependencies are basic to a "
            "concept; that scrutiny is what Evans asks of the designer."
        ),
    },
]
