"""The Building Blocks of a Model-Driven Design, lessons 1-5 -- Chapter 4 and
the first half of Chapter 5.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 4, Isolating the Domain (Layered
Architecture, Relating the Layers, Architectural Frameworks, The Domain Layer
Is Where the Model Lives, The Smart UI "Anti-Pattern", Other Kinds of
Isolation); Chapter 5, A Model Expressed in Software (Associations, Entities,
Value Objects). Pages in the comments are PDF pages of the operator's copy;
the lessons cite by chapter, section and pattern. Every quotation is copied
from that copy and checked with quotes.py. The models and the Java are written
for these lessons: none of the book's listings, diagrams or example domains is
reproduced. The design is docs/domain-driven-design/PLAN.md, section C,
Course 2.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


_PANEL_INTRO = (
    "A count over the small model the lesson states. The lab counts one "
    "consequence of one modelling choice; the choice itself is weighed in the "
    "book, against the domain, the team and the project."
)


# ---------------------------------------------------------------- 01 models

# A library's lending feature, written for the lesson.
LAYERS = "ui application domain infrastructure"

LENDING_ELEMENTS = (
    "LoanScreen, ui; LendCopy, application; Member, domain; Loan, domain; "
    "Copy, domain; LoanStore, infrastructure; Mailer, infrastructure"
)
LENDING_TANGLED = (
    "LoanScreen, LendCopy; LendCopy, Member; LendCopy, Loan; LendCopy, Mailer; "
    "Loan, Copy; Loan, LoanStore; Loan, LoanScreen; LoanStore, LendCopy"
)
LENDING_CALLBACK_ELEMENTS = LENDING_ELEMENTS + (
    "; LoanListener, domain; SaveListener, infrastructure"
)
LENDING_CALLBACKS = (
    "LoanScreen, LendCopy; LendCopy, Member; LendCopy, Loan; LendCopy, Mailer; "
    "Loan, Copy; Loan, LoanStore; Loan, LoanListener; LoanScreen, LoanListener; "
    "LoanStore, SaveListener; LendCopy, SaveListener"
)

LOAN_UPWARD = """// Upward: the domain object calls the screen itself.
class Loan {
    private final LoanScreen screen;
    private boolean overdue;

    void markOverdue() {
        overdue = true;
        screen.showOverdue(this);
    }
}"""

LOAN_LISTENER = """// The domain layer declares what it will announce.
interface LoanListener {
    void loanOverdue(Loan loan);
}

class Loan {
    private final List<LoanListener> listeners = new ArrayList<>();
    private boolean overdue;

    void markOverdue() {
        overdue = true;
        for (LoanListener l : listeners) {
            l.loanOverdue(this);
        }
    }
}"""

# 01 exercise: a clinic's booking feature.
CLINIC_ELEMENTS = (
    "BookingPage, ui; BookVisit, application; Appointment, domain; "
    "Clinician, domain; SmsGateway, infrastructure; VisitTable, infrastructure"
)
CLINIC_DEPS = (
    "BookingPage, BookVisit; BookVisit, Appointment; Appointment, Clinician; "
    "BookVisit, VisitTable; Appointment, SmsGateway; SmsGateway, BookVisit; "
    "Clinician, BookingPage"
)


# ---------------------------------------------------------------- 02 models

# A bike-share's fare rule, held in each screen and then in one domain module.
SMART_ELEMENTS = (
    "ReturnScreen, return-screen; RideHistory, history-screen; "
    "MonthlyBill, bill-screen"
)
SMART_CHANGES = (
    "fare-rule, ReturnScreen; fare-rule, RideHistory; fare-rule, MonthlyBill; "
    "bill-layout, MonthlyBill; "
    "member-discount, ReturnScreen; member-discount, MonthlyBill"
)
LAYERED_ELEMENTS = (
    "ReturnScreen, return-screen; RideHistory, history-screen; "
    "MonthlyBill, bill-screen; Fare, fares; Discount, fares"
)
LAYERED_CHANGES = (
    "fare-rule, Fare; bill-layout, MonthlyBill; member-discount, Discount"
)

SMART_SCREEN = """// Smart UI: the return screen works out the fare itself.
void onReturn(RideRow ride) {
    long minutes = ride.minutes();
    long cents = 100;
    if (minutes > 30) {
        cents = cents + 50 * ((minutes - 30 + 14) / 15);
    }
    ride.setFare(cents);
    db.save(ride);
    show(cents);
}"""

FARE_CLASS = """// The same rule, once, in the domain layer.
final class Fare {
    static Fare forRide(Duration ride) {
        long minutes = ride.toMinutes();
        long cents = 100;
        if (minutes > 30) {
            cents = cents + 50 * ((minutes - 30 + 14) / 15);
        }
        return new Fare(cents);
    }
    // ...the constructor, cents() and equals are omitted here
}
// Each screen now asks: Fare.forRide(ride.duration())"""


# ---------------------------------------------------------------- 03 models

# A school timetable, written for the lesson.
TIMETABLE_BEFORE = (
    "School, Teacher, 1-n, both, no; Teacher, Course, n-n, both, no; "
    "Room, Course, 1-n, both, no; Student, Course, n-n, both, no; "
    "Student, Locker, 1-1, both, no"
)
TIMETABLE_AFTER = (
    "School, Teacher, 1-n, a-b, no; Teacher, Course, n-n, a-b, no; "
    "Room, Course, 1-n, a-b, yes; Student, Course, n-n, both, no"
)

BOTH_WAYS = """// Both ways: every change must be made twice, and kept in step.
class Teacher {
    private final Set<Course> courses = new HashSet<>();

    void assign(Course c) {
        courses.add(c);
        c.addTeacher(this);   // the other end, or the model lies
    }
}"""

QUALIFIED = """// Qualified by period: a room holds one course in a period.
class Room {
    private final Map<Period, Course> timetable = new HashMap<>();

    Course courseAt(Period p) {
        return timetable.get(p);
    }

    void book(Period p, Course c) {
        if (timetable.containsKey(p)) {
            throw new IllegalStateException("room taken in " + p);
        }
        timetable.put(p, c);
    }
}"""

# 03 exercise: a bike-share.
BIKES_BEFORE = (
    "City, Dock, 1-n, both, no; Dock, Bike, 1-n, both, no; "
    "Member, Ride, 1-n, both, no; Ride, Bike, n-1, both, no; "
    "Member, Bike, n-n, both, no"
)


# ---------------------------------------------------------------- 04 models

# A clinic's patients as two systems hold them, written for the lesson.
PATIENTS = (
    "desk-ana, P-1047, name=ana-ruiz, born=1990, town=leeds; "
    "lab-ana, P-1047, name=ana-ruiz, born=1990, town=york; "
    "other-ana, P-2210, name=ana-ruiz, born=1990, town=leeds; "
    "desk-ben, P-0533, name=ben-okafor, born=1984, town=york"
)
PATIENTS_KEYED = (
    "desk-ana, ana-ruiz.1990, name=ana-ruiz, born=1990, town=leeds; "
    "lab-ana, ana-ruiz.1990, name=ana-ruiz, born=1990, town=york; "
    "other-ana, ana-ruiz.1990, name=ana-ruiz, born=1990, town=leeds; "
    "desk-ben, ben-okafor.1984, name=ben-okafor, born=1984, town=york"
)

PATIENT = """final class Patient {
    private final PatientId id;   // issued once, never changed
    private PersonName name;
    private LocalDate born;
    private Town town;

    @Override
    public boolean equals(Object o) {
        return o instanceof Patient && ((Patient) o).id.equals(id);
    }

    @Override
    public int hashCode() {
        return id.hashCode();
    }
}"""

# 04 exercise: a library's member records.
MEMBERS = (
    "m1, L-301, name=kim-lee, joined=2019, branch=north; "
    "m2, L-301, name=kim-lee, joined=2019, branch=south; "
    "m3, L-455, name=kim-lee, joined=2019, branch=north; "
    "m4, L-455, name=kim-lee, joined=2019, branch=north"
)


# ---------------------------------------------------------------- 05 models

# A bakery's orders and their pickup slots, written for the lesson.
SLOT_HOLDERS = (
    "order-17, sat-9-11; order-18, sat-9-11; order-19, sat-9-11; "
    "order-20, sun-9-11"
)
SLOT_COPIES = (
    "order-17, sat-9-11-a; order-18, sat-9-11-b; order-19, sat-9-11-c; "
    "order-20, sun-9-11"
)

PICKUP_SLOT = """final class PickupSlot {
    private final DayOfWeek day;
    private final LocalTime from;
    private final LocalTime to;

    PickupSlot(DayOfWeek day, LocalTime from, LocalTime to) {
        this.day = day;
        this.from = from;
        this.to = to;
    }

    PickupSlot later(Duration d) {
        return new PickupSlot(day, from.plus(d), to.plus(d));
    }
    // equals and hashCode compare day, from and to
}
// To move one order: order.slot = order.slot.later(Duration.ofHours(1));"""

# 05 exercise: a school's term dates.
TERM_HOLDERS = (
    "class-7a, autumn; class-7b, autumn; class-7c, autumn; class-8a, autumn; "
    "class-8b, spring"
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 4 opening (PDF p. 36 of the operator's copy); Layered
    # Architecture (pp. 36-39), the four layers (p. 37), the pattern (p. 38),
    # the banking example (pp. 38-39); Relating the Layers (p. 39);
    # Architectural Frameworks (p. 40); The Domain Layer Is Where the Model
    # Lives (p. 40).
    # Quote: PDF p. 37 of the operator's copy, 27 words, quotes.py OK.
    # Lesson total: 27 words. Course 2's modern aside: hexagonal architecture.
    {
        "slug": "layered-architecture",
        "title": "Layered Architecture",
        "module": "Chapter 4 · Isolating the Domain",
        "one_line": "Four layers, each depending only on the ones below it, so that the code that expresses the model can be found, read and changed on its own.",
        "summary": (
            "Chapter 4 opens Part II with the condition every later pattern needs: "
            "the domain kept apart from the screens, the storage and the plumbing. "
            "Read Evans's four layers, his one rule about which way dependencies "
            "run, and how a lower layer speaks upward without breaking it; then "
            "assign a library's classes to layers and find the dependencies that "
            "run the wrong way."
        ),
        "key": [
            "user interface, application, domain",
            "and infrastructure beneath them",
            "depend only on your layer or below",
            "speak upward through callbacks",
            "a thin application layer",
            "the domain layer is the one it needs",
        ],
        "key_label": "Layered Architecture in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Chapter 4's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Layer",
             "A group of the program's elements that share one concern, such as "
             "showing things to the user or storing data. Evans's layers are the "
             "user interface, the application, the domain and the infrastructure, "
             "from the top down."),
            ("Domain layer",
             "The layer that holds the concepts of the business, the state of the "
             "business situation and the business rules. It is the one layer "
             "domain-driven design cannot do without, because it is where the "
             "model is written as code."),
            ("An upward dependency",
             "A dependency from an element in a lower layer to one in a higher "
             "layer, such as a domain object that calls a screen. The lab lists "
             "every one; a dependency that jumps down past a layer is allowed and "
             "counted separately."),
        ],
        "read_title": "The chapter's argument, then the pattern, then the count",
        "read_intro": (
            "Read the opening of Chapter 4 and its first four sections in your own "
            "copy first. The lesson reads them as an argument for isolating the "
            "domain, then counts the dependencies of a small layered design."
        ),
        "body": [
            ("p", "&ldquo;The essential principle is that any element of a layer "
                  "depends only on other elements in the same layer or on elements of "
                  "the layers &ldquo;beneath&rdquo; it.&rdquo; That is Evans in the "
                  "Layered Architecture section of Chapter 4, Isolating the Domain, "
                  "the chapter that opens Part II. This lesson reads that section and "
                  "the three after it: Relating the Layers, Architectural Frameworks, "
                  "and The Domain Layer Is Where the Model Lives. Enterprise "
                  "Application Patterns reads the same idea in its lesson Layering; "
                  "Fowler asks there how the layers divide the work and where each "
                  "runs, and Evans asks something narrower, which is what the layers "
                  "do for the model."),
            ("p", "The chapter's problem is one of proportion. The code that actually "
                  "solves the business's problem is usually a small part of a "
                  "program, though it matters far more than its size. A single user "
                  "action needs code to draw the screen, query the database, check "
                  "the input, record the choice and commit it, and only one of those "
                  "steps is about the business. When screen code and storage code are "
                  "written straight into the business objects, and business rules "
                  "into widgets and database scripts, Evans says, the domain code "
                  "becomes very hard to see or reason about: a cosmetic change to the "
                  "screen can alter a rule, changing a rule means tracing through "
                  "screens and scripts, and testing is awkward. It happens because it "
                  "is the quickest way to make something work today."),
            ("p", "His answer is the layering most of the industry already uses, in "
                  "four conceptual layers. The user interface shows information and "
                  "interprets commands, from a person or another system. The "
                  "application layer defines the jobs the software does and directs "
                  "domain objects to do them; Evans keeps it thin, with no business "
                  "rules and no state of the business, only the progress of a task. "
                  "The domain layer holds the concepts, the business situation and "
                  "the rules, and he calls it the heart of business software. The "
                  "infrastructure layer supplies generic technical help to the others: "
                  "persistence, messaging, drawing widgets."),
            ("p", "Put as a rule to apply: split a complex program by concern, let "
                  "each part lean only on what lies under it, and give the model a "
                  "layer of its own that screens, task coordination and plumbing "
                  "stay out of. Objects that need not draw or save themselves can be "
                  "about the business alone. Evans's "
                  "example is a funds transfer in online banking, which he lays out "
                  "across the layers with the rule that every credit has a matching "
                  "debit kept in the domain layer, and the screen replaceable by a "
                  "machine request without touching anything below it. He adds that "
                  "the point is not that interfaces are often replaced, but that a "
                  "clean separation keeps each layer easy to understand."),
            ("p", "Relating the Layers says how the layers talk without losing the "
                  "separation. An upper layer uses a lower one in the ordinary way, "
                  "through its public interface. When a lower layer must tell a "
                  "higher one something, beyond answering a question it was asked, "
                  "it goes through an indirect mechanism: a callback, or the Observer "
                  "pattern of Gamma and his colleagues. Model-View-Controller, from "
                  "Smalltalk in the 1970s, is the oldest of the patterns for joining "
                  "the interface to the layers beneath; any of them will do, Evans "
                  "says, so long as the domain objects can be designed without "
                  "thinking about the screens. Infrastructure mostly arrives as "
                  "services the higher layers call, and it should know nothing in "
                  "particular about the domain it serves."),
            ("p", "Architectural Frameworks is a caution. Some infrastructure asks "
                  "more of you than a call: a base class every domain object must "
                  "extend, or method signatures it dictates. The best frameworks "
                  "solve hard technical problems and leave the developer free to "
                  "express the model; the worst constrain the model or slow the work "
                  "down. Evans's advice is to use a framework selectively, for the "
                  "problems it solves well, and his example is the early practice of "
                  "making every domain object an entity bean. The section that "
                  "follows narrows the whole chapter to one requirement: "
                  "domain-driven design needs only the domain layer to exist, since "
                  "its constructs are where the model's concepts are mirrored."),
            ("p", "Now the count. The lab takes the four layers, top to bottom, a "
                  "list of elements with the layer each sits in, and the "
                  "dependencies between them written user, used. The model is a "
                  "library's lending feature: a <code>LoanScreen</code>, an "
                  "application operation <code>LendCopy</code>, the domain objects "
                  "<code>Member</code>, <code>Loan</code> and <code>Copy</code>, and "
                  "a <code>LoanStore</code> and a <code>Mailer</code> in the "
                  "infrastructure. On the preset <code>tangled</code> it counts 8 "
                  "dependencies: 5 downward, 1 within a layer and 2 upward, which it "
                  "lists as <code>Loan</code> to <code>LoanScreen</code> and "
                  "<code>LoanStore</code> to <code>LendCopy</code>. One downward "
                  "dependency, <code>LendCopy</code> to <code>Mailer</code>, skips "
                  "the domain layer; that is allowed, and the lab counts it apart."),
            ("code", _lines(LOAN_UPWARD)),
            ("p", "The first upward dependency looks like this in code. A loan that "
                  "falls overdue tells the screen directly, so the domain layer "
                  "cannot be compiled, tested or read without the screen, and every "
                  "new screen that cares about overdue loans means another field in "
                  "<code>Loan</code>. The preset <code>callbacks</code> turns both "
                  "upward dependencies round. The domain declares a "
                  "<code>LoanListener</code>, which the screen implements; the "
                  "infrastructure declares a <code>SaveListener</code>, which the "
                  "application implements. The lab now counts 10 dependencies, 7 "
                  "downward, 3 within a layer and 0 upward, with 3 skipping a layer. "
                  "There are more arrows than before and none of them points up."),
            ("code", _lines(LOAN_LISTENER)),
            ("p", "Read the counts as Evans would, as a reason to look. An upward "
                  "dependency is where a lower layer knows something it should not; "
                  "the remedy adds an interface rather than removing a connection, "
                  "and the count of all dependencies went up. The tile for layers "
                  "with no element is 0 on both presets; a project that folds the "
                  "application layer into the user interface, as Evans says some "
                  "do, would show 1 there and break no rule. The lab cannot tell whether "
                  "<code>Loan</code> belongs in the domain; it takes your word for "
                  "each element's layer, and that assignment is the design."),
            ("p", "A later view is worth knowing. Alistair Cockburn's hexagonal "
                  "architecture, published the year after the book, and the "
                  "dependency inversion it rests on, put the domain at the centre and "
                  "let the infrastructure depend on interfaces the domain declares, "
                  "so that a storage class implementing a domain interface points "
                  "inward rather than down. Evans states the rule as one direction, "
                  "downward, with callbacks for the exceptions, and the lab counts by "
                  "his rule; on it, a storage class that knows a domain class is an "
                  "upward dependency, and on the later view it is the design. The two "
                  "agree on what matters most to Evans, that the domain must not "
                  "depend on the screens or the storage."),
            ("h3", "Exercise"),
            ("ul", [
                "Layers, top to bottom: `ui`, `application`, `domain`, `infrastructure`.",
                "A clinic's elements: `BookingPage, ui; BookVisit, application; "
                "Appointment, domain; Clinician, domain; SmsGateway, infrastructure; "
                "VisitTable, infrastructure`.",
                "Its dependencies: `BookingPage, BookVisit; BookVisit, Appointment; "
                "Appointment, Clinician; BookVisit, VisitTable; Appointment, "
                "SmsGateway; SmsGateway, BookVisit; Clinician, BookingPage`.",
            ]),
            ("p", "Sort each dependency into downward, within a layer or upward, and "
                  "name the upward ones and the one that skips a layer. For each "
                  "upward dependency, say which layer would declare the interface "
                  "that turns it round. Then type the records into the lab to check "
                  "your count."),
            ("p", "Evans is fair to the road he does not take. The next lesson, The "
                  "Smart UI Anti-Pattern, reads his case for putting everything in "
                  "the screens, and why that choice excludes the rest of the book."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "layers",
            "preset": "tangled",
            "presets": [
                {"id": "tangled",
                 "label": "A library's lending feature with two dependencies pointing up",
                 "layers": LAYERS,
                 "elements": LENDING_ELEMENTS,
                 "deps": LENDING_TANGLED,
                 "expect": {"dmoDeps": "8", "dmoDown": "5", "dmoWithin": "1", "dmoUp": "2: Loan → LoanScreen, LoanStore → LendCopy", "dmoSkip": "1", "dmoEmpty": "0: none"}},
                {"id": "callbacks",
                 "label": "The same feature, with a listener in the domain and one in the infrastructure",
                 "layers": LAYERS,
                 "elements": LENDING_CALLBACK_ELEMENTS,
                 "deps": LENDING_CALLBACKS,
                 "expect": {"dmoDeps": "10", "dmoDown": "7", "dmoWithin": "3", "dmoUp": "0: none", "dmoSkip": "3"}},
            ],
            "panel_title": "Which way the dependencies run",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Checking a layering",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Assign every element a layer",
             "Write down each class with one of the four layers, by what it is "
             "responsible for: showing, directing a task, the business, or "
             "technical support."),
            ("Sort the dependencies",
             "For each dependency, compare the user's layer with the used one's: "
             "lower is downward, the same is within, higher is upward. Note the "
             "downward ones that pass over a layer."),
            ("Turn each upward one round",
             "For each upward dependency, have the lower layer declare an interface "
             "for what it announces, and let the upper element implement it. "
             "Recount: the upward figure should be 0."),
            ("Do it on your own code",
             "Take one feature of a system you know, list its classes with their "
             "layers and its imports as user, used records, and type them into the "
             "lab. Write down the upward dependencies it lists and the interface "
             "each would need."),
        ],
        "worked": {
            "title": "Eight dependencies in a lending feature",
            "intro": [
                "Sort the dependencies of <code>tangled</code>, with the layers "
                "numbered 1 (ui) to 4 (infrastructure).",
            ],
            "lines": [
                "LoanScreen 1 to LendCopy 2: downward",
                "LendCopy 2 to Member, Loan 3: downward",
                "LendCopy 2 to Mailer 4: downward, skips",
                "Loan 3 to Copy 3: within the domain",
                "Loan 3 to LoanStore 4: downward",
                "Loan 3 to LoanScreen 1: upward",
                "LoanStore 4 to LendCopy 2: upward",
                "5 downward, 1 within, 2 upward",
            ],
            "after": [
                "Each line compares two layer numbers and nothing more. Whether "
                "<code>Mailer</code> should be reached from the application or from "
                "the domain is a design question; both are downward, and Evans's "
                "rule allows either.",
            ],
        },
        "quiz_title": "Layers, directions and Evans's claims",
        "quiz": [
            {"q": "In the exercise, with the layers ui, application, domain and "
                  "infrastructure from the top, and a dependency from a lower layer "
                  "to a higher one counted as upward, which dependencies are upward?",
             "a": ["SmsGateway to BookVisit, and Clinician to BookingPage",
                   "Clinician to BookingPage only",
                   "SmsGateway to BookVisit, Clinician to BookingPage, and BookVisit "
                   "to VisitTable",
                   "None: every element depends only on elements it needs"],
             "c": 0,
             "why": "SmsGateway is in the infrastructure and BookVisit in the "
                    "application, so that one points up; Clinician is in the domain "
                    "and BookingPage in the user interface, so that one points up "
                    "too, past the application. BookVisit to VisitTable runs down from "
                    "the application to the infrastructure; it skips the domain, "
                    "which is allowed and is the one skipping dependency. The other "
                    "four, counting Appointment to Clinician within the domain, are "
                    "in order: 4 downward, 1 within, 2 upward. The domain would "
                    "declare a listener for Clinician's news, and the infrastructure "
                    "one for SmsGateway's delivery reports."},
            {"q": "In Relating the Layers, how does Evans say an object in a lower "
                  "layer should communicate upward, beyond answering a direct query?",
             "a": ["By calling the upper layer's public interface, as upper layers "
                   "call lower ones",
                   "Through an indirect mechanism such as a callback or an observer",
                   "Through the database, which every layer can read",
                   "It should not; a lower layer only ever answers queries"],
             "c": 1,
             "why": "Upper layers may call lower ones directly. Upward communication "
                    "needs another mechanism, and Evans names callbacks and the "
                    "Observer pattern. He does not forbid it outright; he routes it "
                    "through an interface, which is what the preset "
                    "<code>callbacks</code> does."},
            {"q": "According to The Domain Layer Is Where the Model Lives, how many of "
                  "the four layers does domain-driven design require to exist?",
             "a": ["All four, in Evans's order",
                   "Three: the user interface, the application and the domain",
                   "One: the domain layer",
                   "Two: the application and the domain"],
             "c": 2,
             "why": "Evans says many styles of development benefit from layering, but "
                    "domain-driven design needs just one of them to exist, the "
                    "domain layer. He notes too that some projects do not separate "
                    "the user interface from the application, and others have "
                    "several infrastructure layers."},
            {"q": "On the preset <code>tangled</code>, you delete the dependency "
                  "<code>Loan, LoanScreen</code> and change nothing else. What does "
                  "the lab report?",
             "a": ["7 dependencies, 1 upward",
                   "7 dependencies, 0 upward",
                   "8 dependencies, 1 upward",
                   "7 dependencies, 2 upward"],
             "c": 0,
             "why": "One record fewer leaves 7. Loan to LoanScreen was one of the two "
                    "upward dependencies; LoanStore to LendCopy still runs from the "
                    "infrastructure up to the application, so 1 remains."},
        ],
        "mistakes": [
            ("Thinking the layers are there so that the user interface can be swapped",
             "Evans's banking example shows the screen replaced by a machine request "
             "without touching the layers below, and he says at once that this is "
             "not why the separation matters. Projects rarely swap their interfaces; "
             "the separation keeps each layer's design easy to understand and to "
             "maintain, and above all it lets the domain layer express the model."),
            ("Putting business rules in the application layer",
             "The application layer directs the work and keeps track of a task's "
             "progress, and Evans keeps it thin: it holds no business rules and no "
             "state of the business situation. A rule such as every credit having a "
             "matching debit belongs to the domain layer, where the model lives."),
            ("Using every feature of an architectural framework",
             "Evans expects most projects to need some framework, and warns that one "
             "can constrain the model or slow development. His advice is to apply it "
             "selectively to the hard technical problems, as the move away from "
             "making every domain object an entity bean did, and so keep the "
             "business objects readable."),
        ],
        "standard": (
            "Finish when you can find the dependencies that break a layering.",
            "Given elements with layers and their dependencies, sort every dependency "
            "as downward, within or upward, and say what interface would turn each "
            "upward one round."
        ),
        "note": (
            "The lab compares the layers you give the two ends of each dependency. "
            "It cannot tell whether an element is in the right layer, whether the "
            "domain layer holds the model or only data, or whether a skipped layer "
            "is a shortcut you will regret; those are readings of the design."
        ),
    },
    # ---------------------------------------------------------------- 02
    # The Smart UI "Anti-Pattern" (PDF pp. 41-42 of the operator's copy): the
    # fork (p. 41), the situation and the pattern (p. 41), advantages (pp.
    # 41-42), disadvantages (p. 42), choosing tools and committing (p. 42),
    # solutions in between, Transaction Script (p. 42); Other Kinds of
    # Isolation (p. 43).
    # Quote: PDF p. 41 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    {
        "slug": "the-smart-ui-anti-pattern",
        "title": "The Smart UI Anti-Pattern",
        "module": "Chapter 4 · Isolating the Domain",
        "one_line": "Every rule written into the screen that needs it: quick and right for a simple project, and a road that rules out a model-driven design.",
        "summary": (
            "Evans gives the alternative to layering a fair hearing: put the business "
            "logic in the screens, one small application at a time, over a shared "
            "database. Read when he says that is the right choice and why it is a "
            "fork rather than a starting point, then count the screens a fare change "
            "touches when the rule lives in each and when it lives in one domain "
            "class."
        ),
        "key": [
            "all the logic in the user interface",
            "right for simple work that enters data",
            "rules copied into each screen",
            "no graceful path to richer behavior",
            "choose it on purpose, or not at all",
        ],
        "key_label": "The Smart UI in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Smart UI",
             "A design that writes every business rule into the user interface, "
             "splits the application into small functions each with its own screen, "
             "and shares data through a relational database. Evans calls it an "
             "anti-pattern only for domain-driven design."),
            ("Anti-pattern",
             "A pattern described in order to say when not to use it. Evans uses the "
             "word with some irony: the Smart UI is a legitimate pattern elsewhere, "
             "and he discusses it to show when the harder road is worth taking."),
            ("Module touches",
             "For each change, the number of modules holding an element the change "
             "must edit, summed over the changes. The lab also counts the changes "
             "confined to a single module."),
        ],
        "read_title": "The section's case, both sides, then the count",
        "read_intro": (
            "Read The Smart UI &ldquo;Anti-Pattern&rdquo; and Other Kinds of "
            "Isolation in your own copy first. The lesson sets out Evans's case for "
            "and against, then counts what a copied rule costs."
        ),
        "body": [
            ("p", "&ldquo;But SMART UI is an alternate, mutually exclusive fork in the "
                  "road, incompatible with the approach of domain-driven "
                  "design.&rdquo; Evans writes that in The Smart UI "
                  "&ldquo;Anti-Pattern&rdquo;, the section of Chapter 4 that follows "
                  "Layered Architecture. The separation the last lesson described is, "
                  "he says, attempted often and achieved seldom, so its opposite "
                  "deserves a section of its own. This lesson reads it, with the "
                  "short Other Kinds of Isolation that closes the chapter."),
            ("p", "He begins with the situation in which the Smart UI is right: a "
                  "project with simple functions, mostly entering and displaying "
                  "data, few business rules, and a team that is not made of "
                  "experienced object modellers. Hand that team a model-driven design "
                  "with layers, and it faces new technology and the hard business of "
                  "learning to model, while the overhead of the layers makes each "
                  "simple task slower. Evans's guess is that such a project is "
                  "cancelled before it shows what the approach could do, and that if "
                  "it does finish, it has built a simple system nobody asked to be "
                  "rich. A seasoned team would face a different trade, but not "
                  "every project is ambitious, and not every team has those skills."),
            ("p", "Evans's prescription, for those circumstances only: let each "
                  "screen be a small application that carries its own rules, keep "
                  "the shared data in a relational store, and build the screens "
                  "with whatever tools generate them fastest. Evans calls this heresy "
                  "against his own gospel, and then lists its advantages honestly. "
                  "Productivity is high at once for simple applications; developers "
                  "with little training can work this way; a prototype in users' "
                  "hands can make up for weak requirements; the small applications "
                  "are independent, so their schedules can be planned and new simple "
                  "behaviour added; relational databases and fourth-generation tools "
                  "suit it; and a maintainer can rewrite a screen they do not "
                  "understand, since its effects stay inside it."),
            ("p", "The disadvantages are as plain. Applications can be joined only "
                  "through the database. Nothing is reused and nothing abstracts the "
                  "business problem, so each rule is duplicated in every operation "
                  "that needs it. Prototyping stops paying when the lack of "
                  "abstraction leaves nothing to refactor. Complexity overwhelms the "
                  "design quickly, and the only way to grow is more simple "
                  "applications. Choose it deliberately, Evans says, and you avoid a "
                  "great deal of overhead; two common, costly mistakes are to start a "
                  "sophisticated approach the team will not see through, and to build "
                  "heavy infrastructure for a project that does not need it."),
            ("p", "What makes it a fork is that there is no migration. You leave a "
                  "Smart UI only by replacing whole applications, so a team that "
                  "chooses it should pick tools made for it, not a general-purpose "
                  "language kept in reserve; a flexible language, he warns, does not "
                  "make a flexible system and may make an expensive one. By the same "
                  "reasoning a team that means to build a model-driven design must "
                  "design that way from the first iteration, with an isolated domain layer "
                  "from its first small steps. Between the two lie designs such as "
                  "Fowler's Transaction Script, which separates the interface from "
                  "the application but builds no object model, and Evans's test for "
                  "all of them is whether the domain code is isolated well enough to "
                  "be designed as a cohesive whole."),
            ("p", "Other Kinds of Isolation looks ahead. The interface and the "
                  "infrastructure are not the only threats to a model: other "
                  "components that are not part of it, other teams with their own "
                  "models of the same domain, and the size of the model itself. "
                  "Chapter 14 answers the first two with Bounded Context and "
                  "Anticorruption Layer, and Chapter 15 answers the third with "
                  "Distillation; both are read in later courses."),
            ("p", "Now the count, on a bike-share. Its fare rule says a ride costs a "
                  "dollar, and 50 cents more for each started quarter-hour past "
                  "thirty minutes. Under a Smart UI three screens need it, the return "
                  "screen, the ride history and the monthly bill, and each works it "
                  "out for itself, as below. The lab's change view takes the "
                  "elements with their modules and a list of changes, each naming the "
                  "elements it must edit. On the preset <code>fare-in-every-screen</code> each "
                  "screen is a module, and three changes are listed: the fare rule, "
                  "the bill's layout and a member discount that the return screen "
                  "and the bill apply. It counts 6 module touches, 1 change confined "
                  "to one module, and the fare rule as the largest, at 3 modules."),
            ("code", _lines(SMART_SCREEN)),
            ("p", "The preset <code>fare-in-the-domain</code> keeps the three screens and "
                  "adds a <code>fares</code> module holding <code>Fare</code> and "
                  "<code>Discount</code>. Each screen now asks the domain for the "
                  "fare. The same three changes make 3 module touches, all 3 confined "
                  "to one module: the fare rule edits <code>Fare</code>, the discount "
                  "edits <code>Discount</code>, and the layout edits the bill alone. "
                  "The layout change costs the same in both designs, which is the "
                  "Smart UI's own advantage, that a screen's changes stay in the "
                  "screen. What it cannot do is keep a rule in one place."),
            ("code", _lines(FARE_CLASS)),
            ("p", "That is the disadvantage Evans lists, counted on the lesson's "
                  "illustration: three edits for one rule, and a fourth the day a "
                  "new screen needs fares. It is not his verdict. For a project with "
                  "three screens and two rules, three edits may be cheaper than a "
                  "domain layer the team must first learn to build, and that is the "
                  "trade the section weighs. The lab counts edits; it does not know "
                  "the team."),
            ("h3", "Exercise"),
            ("ul", [
                "A gym's Smart UI: three screens, `CheckIn`, `Booking` and "
                "`Statement`, each its own module.",
                "Changes: the off-peak hours move (`CheckIn`, `Booking`, "
                "`Statement`); the guest-pass limit changes (`CheckIn`, `Booking`); "
                "the statement's layout changes (`Statement`); a locker fee is added "
                "(`CheckIn`, `Statement`).",
                "The layered version keeps the three screens and adds a `rules` "
                "module with `Pricing` and `GuestPolicy`; the off-peak hours and the "
                "locker fee edit `Pricing`, the guest limit edits `GuestPolicy`, and "
                "the layout edits `Statement`.",
            ]),
            ("p", "For each design, count the module touches over the four changes, "
                  "the changes confined to one module, and the largest change. Then "
                  "write one sentence on what the gym's team would need to know "
                  "before choosing between them."),
            ("p", "Chapter 5 turns from the layers to what goes in the domain layer. "
                  "The next lesson, Associations, reads its first concern: the links "
                  "between objects, and how to keep them few."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "preset": "fare-in-every-screen",
            "presets": [
                {"id": "fare-in-every-screen",
                 "label": "Smart UI: each of three screens holds the fare rule",
                 "elements": SMART_ELEMENTS,
                 "changes": SMART_CHANGES,
                 "expect": {"dmoPer": "fare-rule 3, bill-layout 1, member-discount 2", "dmoTotal": "6", "dmoConfined": "1 of 3: bill-layout", "dmoLargest": "fare-rule, 3 modules"}},
                {"id": "fare-in-the-domain",
                 "label": "The same screens, with the rules in one domain module",
                 "elements": LAYERED_ELEMENTS,
                 "changes": LAYERED_CHANGES,
                 "expect": {"dmoPer": "fare-rule 1, bill-layout 1, member-discount 1", "dmoTotal": "3", "dmoConfined": "3 of 3: fare-rule, bill-layout, member-discount"}},
            ],
            "panel_title": "The places a rule change touches",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Counting what a copied rule costs",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the rules and where they live",
             "For each business rule, write down every screen or class whose code "
             "applies it."),
            ("List the changes",
             "Write the changes you expect, rule changes and screen changes alike, "
             "each with the elements it must edit."),
            ("Count the module touches",
             "For each change, count the modules holding those elements; add them "
             "up, and note the changes that stay in one module."),
            ("Do it on your own system",
             "Pick one rule in a system you know, such as a price or a limit, and "
             "find every place it is applied. Write the count down, and one sentence "
             "on whether the project is one Evans would give a Smart UI."),
        ],
        "worked": {
            "title": "Three changes, two designs",
            "intro": [
                "Count the module touches of <code>fare-in-every-screen</code> and "
                "<code>fare-in-the-domain</code>.",
            ],
            "lines": [
                "fare rule, Smart UI: three screens, 3",
                "bill layout, Smart UI: the bill, 1",
                "discount, Smart UI: return and bill, 2",
                "Smart UI: 3 + 1 + 2 makes 6, one confined",
                "domain class: Fare, bill, Discount",
                "domain class: 1 + 1 + 1 makes 3, all confined",
            ],
            "after": [
                "The screens did not get simpler to change; the rules did. Whether "
                "three edits of one rule cost more than a domain layer is the question "
                "Evans answers by the project, not by the count.",
            ],
        },
        "quiz_title": "The Smart UI, counted and argued",
        "quiz": [
            {"q": "In the exercise, counting for each change the modules it must edit, "
                  "what are the total module touches in the Smart UI design and in "
                  "the layered design?",
             "a": ["8 and 4",
                   "8 and 3",
                   "4 and 4",
                   "7 and 4"],
             "c": 0,
             "why": "Smart UI: off-peak hours 3, guest limit 2, layout 1, locker fee 2, "
                    "which is 8, with one change, the layout, confined to one module. "
                    "Layered: off-peak hours and locker fee each edit Pricing, the "
                    "guest limit edits GuestPolicy, the layout edits Statement: 1 + 1 "
                    "+ 1 + 1 = 4, all confined. Pricing and GuestPolicy are two "
                    "elements of one rules module, but the count is by change, so "
                    "two changes to the same module are still two touches. Before "
                    "choosing, the gym's team would need to know how often the rules "
                    "change and whether it can build and keep a domain layer."},
            {"q": "Which of these does Evans list among the Smart UI's advantages?",
             "a": ["Business rules are written once and reused by every screen",
                   "There is a graceful path to richer behaviour later",
                   "A maintainer can redo a screen they cannot follow, since its "
                   "effects stay inside it",
                   "Applications integrate easily with each other outside the "
                   "database"],
             "c": 2,
             "why": "Localised effects are on his list of advantages. The other three "
                    "are the reverse of his disadvantages: rules are duplicated in "
                    "each operation, there is no graceful path to richer behaviour, "
                    "and integration is difficult except through the database."},
            {"q": "A team starts a Smart UI in a general-purpose language, planning to "
                  "move to a model-driven design if the project grows. What does "
                  "Evans say about that plan?",
             "a": ["It is the recommended way to start, since every project begins "
                   "simple",
                   "It will not work: you leave a Smart UI only by replacing whole "
                   "applications, so choose tools made for it",
                   "It works if the domain layer is added before the third screen",
                   "It works if the screens are written as Transaction Scripts"],
             "c": 1,
             "why": "Evans says the only way out of a Smart UI is to replace entire "
                    "applications, so using Java does not keep the option open; he "
                    "advises tools geared to the pattern, and warns that a flexible "
                    "language does not make a flexible system. A model-driven project "
                    "must have an isolated domain layer from its first steps."},
            {"q": "On the preset <code>fare-in-the-domain</code>, a fourth change is added "
                  "that edits <code>Fare</code> and <code>ReturnScreen</code>. How "
                  "many module touches does the lab count now, and how many changes "
                  "are confined to one module?",
             "a": ["5 touches, 3 confined",
                   "4 touches, 4 confined",
                   "5 touches, 4 confined",
                   "4 touches, 3 confined"],
             "c": 0,
             "why": "Fare is in the fares module and ReturnScreen in return-screen, so "
                    "the new change touches 2 modules: 3 + 2 = 5 touches. The three "
                    "earlier changes stay confined; the new one is not, so 3 of 4."},
        ],
        "mistakes": [
            ("Taking the Smart UI for a design nobody should choose",
             "Evans calls it an anti-pattern only in the context of domain-driven "
             "design, and with tongue in cheek. For simple, data-centred applications "
             "and teams without advanced modelling skills he recommends it, lists its "
             "real advantages, and calls building heavy infrastructure for a project "
             "that does not need it a costly mistake."),
            ("Starting with a Smart UI and planning to refactor into a model later",
             "There is no migration path: a Smart UI is left by replacing whole "
             "applications. A project that will need a model-driven design has to "
             "have an isolated domain layer from its first small iteration, or it "
             "will most likely be stuck."),
            ("Thinking a Smart UI makes every change expensive",
             "Changes to one screen stay in that screen, which is one of the "
             "pattern's advantages; the lesson's layout change costs one touch in "
             "both designs. What the Smart UI multiplies is the cost of a rule that "
             "many screens apply, because each holds its own copy."),
        ],
        "standard": (
            "Finish when you can count what a copied rule costs and say when it is worth it.",
            "Given screens, rules and changes, count the module touches with the rules "
            "in each screen and in one domain module, and give Evans's conditions for "
            "choosing the Smart UI."
        ),
        "note": (
            "The lab counts edits for the changes you list. It cannot estimate how "
            "often a rule will change, what a domain layer would cost your team to "
            "build, or whether the project will grow; Evans's choice turns on those, "
            "and no count of touches settles it."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 5 opening (PDF pp. 44-45 of the operator's copy); Associations
    # (pp. 45-49): the correspondence (p. 45), the three ways (p. 45),
    # direction and the presidents (pp. 45-46), the qualifier (p. 46),
    # elimination (p. 46), the brokerage account example (pp. 47-49).
    # Quote: PDF p. 45 of the operator's copy, 22 words, quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "associations",
        "title": "Associations",
        "module": "Chapter 5 · A Model Expressed in Software",
        "one_line": "Every link the model draws is a mechanism in the code, so impose a direction, add a qualifier, and remove the links the job does not need.",
        "summary": (
            "Chapter 5 begins with the links between objects, simple to draw and "
            "costly to maintain. Read Evans's three ways of making an association "
            "tractable, and why each says something about the domain, then apply "
            "all three to a school timetable and count the directions and the many "
            "ends before and after."
        ),
        "key": [
            "each association is a mechanism",
            "impose a traversal direction",
            "add a qualifier to cut multiplicity",
            "eliminate what the job does not need",
            "keep both ways only when they mean it",
        ],
        "key_label": "Associations in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Traversal direction",
             "Which way the code can follow an association. Both ways means each "
             "object can reach the other; one way means only one can, and the other "
             "need not know the link exists."),
            ("Qualifier",
             "A value that picks one object out of the many at the far end of an "
             "association, such as a period that picks one course out of a room's "
             "many. It turns a one-to-many link into a one-to-one link for each "
             "value of the qualifier."),
            ("Many end",
             "An end of an association where one object can be linked to many. A "
             "one-to-many link has one, a many-to-many link two; the lab counts a "
             "qualified many end as a one end, so it is no longer a many end."),
        ],
        "read_title": "The section's argument, then the three moves, then the count",
        "read_intro": (
            "Read the opening of Chapter 5 and its Associations section in your own "
            "copy first. The lesson reads them as an argument about what links "
            "cost, then counts the cost on a timetable."
        ),
        "body": [
            ("p", "&ldquo;It is important to constrain relationships as much as "
                  "possible. A bidirectional association means that both objects can "
                  "be understood only together.&rdquo; That is Evans in the "
                  "Associations section of Chapter 5, A Model Expressed in Software. "
                  "The chapter's opening sets out its plan: connect the model and the "
                  "code at the level of detail, starting with associations, then the "
                  "three kinds of model element that carry the model, Entities, "
                  "Value Objects and Services, and last Modules. This lesson reads "
                  "the opening and the first section."),
            ("p", "The section starts from a correspondence. For each association the "
                  "model says can be traversed, the code needs a mechanism that "
                  "behaves the same way. A link between a customer and a sales "
                  "representative is, on one side, a relationship between two people "
                  "that the team judged relevant, and on the other, a pointer, or a "
                  "method that looks the other up in a database. A one-to-many link "
                  "may be a collection in a field, or a query that builds the objects "
                  "when asked; both carry the same model, and the design must choose "
                  "one whose behaviour matches the association."),
            ("p", "The trouble is that the world is full of many-to-many links, many "
                  "of them naturally two-way, and so are early models, while the "
                  "brainstorm is still going. Those general associations are hard to "
                  "implement and to maintain, and they say little about the "
                  "relationship. Evans gives at least three ways to make them "
                  "tractable: impose a traversal direction, add a qualifier to reduce "
                  "the multiplicity, and eliminate associations that are not "
                  "essential."),
            ("p", "His example of the first is a country and its presidents, a link "
                  "that is one-to-many and could be followed either way, though "
                  "almost nobody starts from a person and asks which country he "
                  "led. Making it one-way, from country to president, is both a "
                  "simpler design and an insight: one direction matters more, and "
                  "the person no longer depends on the far lesser idea of a "
                  "presidency. The second move comes from looking harder at the same "
                  "link. A country has one president at a time, so qualified by the "
                  "date the association is one-to-one, and the rule is now in the "
                  "model. A direction imposed on a many-to-many link, he adds, "
                  "reduces its implementation to one-to-many."),
            ("p", "Constraining associations wherever the domain allows has a second "
                  "benefit: the two-way links that remain now mean something, since "
                  "each says that both directions matter to the domain or the "
                  "application. The last move is the simplest, to remove an "
                  "association altogether when neither the job nor the meaning of "
                  "the objects needs it. Evans closes with a brokerage account, "
                  "written first as plain fields and then as database lookups, both "
                  "consistent with one model; qualifying its investments by stock "
                  "turns a set into a map, a rule that he notes would not hold for "
                  "every business, and that once found belongs in the model and the "
                  "code."),
            ("p", "Now the count, on a school timetable. The lab takes each "
                  "association as a record of its two classes, its ends "
                  "(one to one, one to many, many to one or many to many, typed "
                  "1-1, 1-n, n-1 and n-n), its direction (both, or a-b when only "
                  "the first navigates to the second) and "
                  "whether it is qualified, and a second list for the model after "
                  "the moves. The preset <code>timetable</code> starts with five "
                  "associations, all two-way: a school's teachers, teachers and "
                  "courses, a room's courses, students and courses, and a student's "
                  "locker. It counts 10 navigable directions, 2 many-to-many "
                  "associations and 6 many ends. A two-way link is two references to "
                  "keep in step, which is what the code below has to do."),
            ("code", _lines(BOTH_WAYS)),
            ("p", "The model after the moves keeps four associations. The school "
                  "reaches its teachers and a teacher reaches his or her courses, "
                  "one way each, because the timetable is printed per teacher; the "
                  "room's courses are one way and qualified by period, since a room "
                  "holds one course at a time; students and courses stay two-way, "
                  "because the school needs class lists and each student's "
                  "timetable; the locker goes, since timetabling never asks about "
                  "it. The lab counts 4 associations, 5 navigable directions, 2 "
                  "many-to-many associations and 5 many ends, and its two-way tile "
                  "falls from 5 links to 1, the one left with two references to "
                  "keep in step. The change tile gives 1 association, 5 directions, "
                  "4 two-way links and 1 many end fewer."),
            ("code", _lines(QUALIFIED)),
            ("p", "The preset <code>timetable-directions-only</code> applies the first move "
                  "alone: every association one-way except students and courses, no "
                  "qualifier, the locker kept. It counts 6 directions, against 10, "
                  "and the many ends stay at 6. So each move shows in a different "
                  "tile. The many-to-many tile does not move at all: the lab counts "
                  "the ends as declared, while Evans's point is that a one-way "
                  "many-to-many link is built as a collection on one side, like a "
                  "one-to-many link. The counts measure the implementation's burden; "
                  "the reasons for each move, that timetables are printed per "
                  "teacher and a room holds one class at a time, are facts about the "
                  "school that no count supplies."),
            ("h3", "Exercise"),
            ("ul", [
                "A bike-share, before: `City, Dock, 1-n, both, no; Dock, Bike, 1-n, "
                "both, no; Member, Ride, 1-n, both, no; Ride, Bike, n-1, both, no; "
                "Member, Bike, n-n, both, no`.",
                "The moves: city to dock one way; dock to bike one way and qualified "
                "by slot; member to ride one way; ride to bike one way; the "
                "member's favourite bikes, the many-to-many link, removed.",
            ]),
            ("p", "Write the model after the moves as records, and count by hand the "
                  "associations, navigable directions, many-to-many associations and "
                  "many ends before and after. Then give, for one of the one-way "
                  "links, the question the business would have to ask for it to need "
                  "the other direction."),
            ("p", "Links are drawn between objects, and Chapter 5 now turns to the "
                  "objects themselves. The next lesson, Entities, reads the first "
                  "kind: objects defined by who they are."),
        ],
        "lab": ("dddkit", {
            "mode": "assoc",
            "view": "simplify",
            "preset": "timetable",
            "presets": [
                {"id": "timetable",
                 "label": "A school timetable, before and after all three moves",
                 "assocs": TIMETABLE_BEFORE,
                 "after": TIMETABLE_AFTER,
                 "expect": {"dasAssocs": "5 → 4", "dasDirections": "10 → 5", "dasTwoWay": "5 → 1", "dasManyMany": "2 → 2", "dasManyEnds": "6 → 5", "dasChange": "−1 associations, −5 navigable directions, −4 two-way, 0 many-to-many, −1 many ends"}},
                {"id": "timetable-directions-only",
                 "label": "The same timetable with directions imposed and nothing else",
                 "assocs": TIMETABLE_BEFORE,
                 "after": (
                     "School, Teacher, 1-n, a-b, no; Teacher, Course, n-n, a-b, no; "
                     "Room, Course, 1-n, a-b, no; Student, Course, n-n, both, no; "
                     "Student, Locker, 1-1, a-b, no"
                 ),
                 "expect": {"dasDirections": "10 → 6", "dasManyMany": "2 → 2", "dasManyEnds": "6 → 6"}},
            ],
            "panel_title": "The references an association asks you to keep",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Simplifying a model's associations",
        "steps_intro": "Four steps, the last of them on a model of your own.",
        "steps": [
            ("Ask which way each link is followed",
             "For each association, write down the questions the application asks "
             "of it. If every question starts from the same end, make it one-way "
             "from that end."),
            ("Look for a qualifier",
             "For each many end, ask whether some value, a date, a period, a key, "
             "picks out exactly one. If it does, qualify the association by it and "
             "write the rule down."),
            ("Remove what nothing asks",
             "Strike any association that no feature traverses and that the meaning "
             "of the objects does not need. Recount directions and many ends."),
            ("Do it on your own model",
             "Take five associations from a model you know, type them into the lab "
             "with the moves you would make, and write down the directions and many "
             "ends saved, with the domain reason for each move."),
        ],
        "worked": {
            "title": "Five links, then four",
            "intro": [
                "Count the directions and many ends of <code>timetable</code> before "
                "and after.",
            ],
            "lines": [
                "before: five links, both ways, 5 * 2 makes 10",
                "many ends: 1 + 2 + 1 + 2 + 0 makes 6",
                "after: three one way, one both, 3 + 2 makes 5",
                "room to course qualified: no many end",
                "many ends after: 1 + 2 + 0 + 2 makes 5",
                "saved: 1 link, 5 directions, 1 many end",
            ],
            "after": [
                "The qualifier saved the many end and the direction saved a "
                "reference; neither saved a many-to-many link, which a direction only "
                "makes easier to build. Each move stands on a fact about the school, "
                "and the count would mislead without it.",
            ],
        },
        "quiz_title": "Associations, counted and argued",
        "quiz": [
            {"q": "In the exercise, after the five moves, how many navigable "
                  "directions and many ends does the bike-share model have, counting "
                  "2 directions for a two-way link and a qualified many end as no "
                  "longer many?",
             "a": ["4 directions and 3 many ends",
                   "4 directions and 4 many ends",
                   "5 directions and 3 many ends",
                   "8 directions and 3 many ends"],
             "c": 0,
             "why": "Four associations remain, all one-way: 4 directions, against 10 "
                    "before. Many ends: city to dock 1, dock to bike 0 once qualified "
                    "by slot, member to ride 1, ride to bike 1 (its many end is on the "
                    "ride side), which is 3, against 6 before. The many-to-many count "
                    "falls from 1 to 0 because the favourite-bikes link was removed. "
                    "A member's rides could need the other direction if the business "
                    "asked, given a ride, which member's account to charge."},
            {"q": "Why, in Evans's example of a country and its presidents, does the "
                  "one-way association reflect insight into the domain and not only a "
                  "simpler design?",
             "a": ["Because a person can never be president of two countries",
                   "Because one direction is far more meaningful, and the person "
                   "need not depend on the lesser concept of a presidency",
                   "Because the database can only index one direction",
                   "Because one-to-many links must always be one-way"],
             "c": 1,
             "why": "Evans says we seldom start from the person and ask which country "
                    "he led; the one-way link records that one direction matters more, "
                    "and keeps the person independent of the presidency. Nothing in "
                    "the section forbids two-way one-to-many links: he keeps those "
                    "the domain or application needs, and says they then carry "
                    "meaning."},
            {"q": "What, according to Evans, does imposing a direction on a "
                  "many-to-many association do to its implementation?",
             "a": ["Nothing; only a qualifier changes the implementation",
                   "It makes it one-to-one",
                   "It reduces it, in effect, to one-to-many",
                   "It removes the association"],
             "c": 2,
             "why": "A one-way many-to-many link is built as a collection on one side "
                    "only, the shape of a one-to-many link. The lab still counts its "
                    "ends as n-n, as declared; the many-to-many tile does not move on "
                    "<code>timetable-directions-only</code>, and the prose of the lesson says "
                    "why."},
        ],
        "mistakes": [
            ("Making every association two-way so that any question can be answered",
             "Two-way links are common in the world and in early models, and Evans's "
             "point is that they cost: both objects can be understood only together, "
             "and each change must be made at both ends. Keep both directions where "
             "the domain or the application needs them, and then the two-way links "
             "that remain say something."),
            ("Choosing a direction for convenience in the code",
             "The direction Evans wants is the one the domain is biased toward, found "
             "by asking which questions start from which end. A direction chosen "
             "because one table has the foreign key may be the wrong one, and the "
             "model will say something the business does not."),
            ("Treating a qualifier as an implementation trick",
             "A qualifier states a rule of the domain, such as one course in a room "
             "in a given period, and Evans asks that every such constraint be put "
             "into both the model and the code. It makes the model more precise, not "
             "only the map lookup faster, and it holds only where the rule does."),
        ],
        "standard": (
            "Finish when you can simplify a set of associations and give the reason for each move.",
            "Given a model's associations and the questions asked of it, impose "
            "directions, add qualifiers and remove links, and count the directions "
            "and many ends saved."
        ),
        "note": (
            "The lab counts directions, ends and links as you declare them. It cannot "
            "tell whether a direction matches the questions the business asks, "
            "whether a qualifier's rule is true, or whether a removed link was "
            "needed after all; each move is a claim about the domain."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Entities (a.k.a. Reference Objects) (PDF pp. 49-52 of the operator's
    # copy): the mistaken-identity story (pp. 49-50), the customer across
    # systems (p. 50), the pattern (p. 51), bank transactions and check
    # numbers (p. 51), stadium seats (p. 52); Modeling Entities (p. 52);
    # Designing the Identity Operation (pp. 53-54).
    # Quote: PDF p. 51 of the operator's copy, 12 words, quotes.py OK.
    # Lesson total: 12 words.
    {
        "slug": "entities",
        "title": "Entities",
        "module": "Chapter 5 · A Model Expressed in Software",
        "one_line": "An object that is the same thing through every change to its attributes, and must be told apart from another that looks exactly like it.",
        "summary": (
            "Evans's first kind of model element is defined not by what it holds but "
            "by a thread of identity through its life. Read why the language's own "
            "identity will not do, how to keep an entity spare, and how to choose "
            "its identifier, then compare a clinic's patient records by identity "
            "and by attributes and find where the two disagree."
        ),
        "key": [
            "defined by identity, not attributes",
            "every attribute may change",
            "two may look alike and differ",
            "the model defines what same means",
            "keep the entity spare",
            "an identifier that never changes",
        ],
        "key_label": "Entities in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Entity",
             "An object defined mainly by its identity: it stays the same thing "
             "while its attributes change, sometimes across several systems and "
             "stored forms. Evans's examples include a person, a lottery ticket and "
             "a bank transaction."),
            ("Identity operation",
             "The means a design gives for deciding whether two objects are the same "
             "entity, usually by comparing an identifier that is unique in the "
             "system and never changes."),
            ("Changed and look-alike pairs",
             "The two ways identity and attributes can disagree. A changed pair is "
             "one thing whose attributes differ between two records; a look-alike "
             "pair is two things whose attributes are the same."),
        ],
        "read_title": "The section's story and argument, then the count",
        "read_intro": (
            "Read Entities, Modeling Entities and Designing the Identity Operation "
            "in your own copy first. The lesson reads them as an argument about "
            "sameness, then compares records two ways."
        ),
        "body": [
            ("p", "&ldquo;The model must define what it means to be the same "
                  "thing.&rdquo; That is the last sentence of the pattern Entities, "
                  "also called Reference Objects, in Chapter 5. This lesson reads it "
                  "with the two sections that follow, Modeling Entities and Designing "
                  "the Identity Operation."),
            ("p", "Evans opens with a story from his own life, and it is worth reading "
                  "in the book. Sued for damage to a flat he had never seen, he was "
                  "taken for a former tenant of the same name; what saved him was an "
                  "old phone book showing two listings side by side, his and his "
                  "namesake's. People can resolve a mistaken identity with "
                  "resourcefulness. A system that confuses two people corrupts its "
                  "data."),
            ("p", "The argument is that many things are defined by identity rather "
                  "than by any attribute. A person's name, address and finances can "
                  "all change, and yet the person persists, and the question that "
                  "matters to a model is whether the application's users care that "
                  "it is the same person. A customer in a receivables system may "
                  "also live in a sales team's contact software and in an archive, "
                  "in different forms, and when the phone rings it matters whether "
                  "this is the customer with the overdue account. Two records may "
                  "need matching though their attributes differ, and two others "
                  "telling apart though their attributes agree."),
            ("p", "Put as a rule to apply: if an object matters for who it is, let "
                  "identity lead its definition, keep the class about remaining the "
                  "same thing over its life, give it a way to be told apart that "
                  "survives any change of storage or shape, and distrust any "
                  "requirement to match such objects on their fields. The identity "
                  "is an operation that never gives two objects the same answer, "
                  "often a symbol attached for the purpose, and it must "
                  "follow the distinctions the model draws. Evans warns that the "
                  "language's own identity, Java's <code>==</code>, only says two "
                  "references point at one object in memory; that means little in "
                  "most domains, and it is lost whenever an object is stored and "
                  "read back or sent across a network."),
            ("p", "Identity, he insists, is not part of the things themselves; it is "
                  "imposed on them because it is useful. Two equal deposits to one "
                  "account on one day are still two transactions, "
                  "and a cheque number is how a bank statement and a cheque register "
                  "match the same transaction entered by different people on "
                  "different days. A stadium's seats are entities when tickets are "
                  "for numbered seats, and not when the event is general admission, "
                  "where only the count of seats matters."),
            ("p", "Modeling Entities asks that the class be kept spare: the attributes "
                  "that identify the object or are commonly used to find and match "
                  "it, the behaviour essential to the concept, and the rest moved to "
                  "associated objects, other entities or the value objects of the "
                  "next lesson. Designing the Identity Operation then lists the ways "
                  "to get an identifier. Some attributes, or combinations of them, "
                  "can be guaranteed unique and serve as a key, though Evans warns "
                  "that such keys have exceptions; otherwise the system attaches an "
                  "identifier that is unique within the class and, once assigned, "
                  "never changes. It may be hidden from users, as in a contacts "
                  "program that must tell two people of the same name apart, or "
                  "given to them, as a parcel's tracking number is. Identifiers "
                  "issued outside, a national number or a phone number, can be "
                  "missing, shared or reassigned, which is why matching often ends "
                  "with a person deciding."),
            ("p", "Now the count, on a clinic whose front desk and laboratory each "
                  "hold patient records. The lab takes objects as records of a name, "
                  "an identifier and attributes, compares every pair, and reports "
                  "the pairs the same by identity, the pairs the same by attributes, "
                  "and where the two disagree. On the preset <code>patients</code> "
                  "there are four records and 6 pairs. One pair is the same by "
                  "identity, the desk's and the lab's record of patient P-1047, and "
                  "one pair is the same by attributes, the desk's Ana Ruiz and "
                  "another patient with the same name, birth year and town. They "
                  "disagree on both: the first is a changed pair, since she has "
                  "moved and only the lab knows, and the second a look-alike pair."),
            ("code", _lines(PATIENT)),
            ("p", "Equality written as above, on the identifier alone, gives the "
                  "first answer, and an equality on every field would give the "
                  "second. The preset <code>patients-keyed-by-name</code> shows what happens "
                  "when the identifier is built from the attributes people search "
                  "by, the name with the birth year. Now 3 pairs are the same by "
                  "identity, every pairing of the three records called Ana Ruiz, and "
                  "the lab lists 2 changed pairs and 0 look-alikes. It reports, "
                  "faithfully, that two different patients are one, because the "
                  "identifier says so. That is Evans's warning about attribute keys "
                  "in the lab's numbers: the count follows the identity you state, "
                  "and only the model can say whether that identity is right."),
            ("p", "So the count is a reason to look at each disagreement. A changed "
                  "pair is where attribute matching would split one patient into "
                  "two, and a look-alike pair where it would merge two into one; "
                  "both are the mistakes a clinic cannot afford, and both are "
                  "invisible to a comparison of fields. The lab does not know which "
                  "records belong to which person. You do, from the identifier, and "
                  "the identifier is only as good as the model behind it."),
            ("h3", "Exercise"),
            ("ul", [
                "A library's member records, written name, identifier, attributes: "
                "`m1, L-301, name=kim-lee, joined=2019, branch=north`; `m2, L-301, "
                "name=kim-lee, joined=2019, branch=south`; `m3, L-455, name=kim-lee, "
                "joined=2019, branch=north`; `m4, L-455, name=kim-lee, joined=2019, "
                "branch=north`.",
            ]),
            ("p", "Compare all six pairs. Count the pairs the same by identity and by "
                  "attributes, and list the changed pairs and the look-alikes. Then "
                  "say what a librarian would need to ask to know whether the "
                  "identifiers are right."),
            ("p", "Not everything deserves an identity. The next lesson, Value "
                  "Objects, reads the objects whose only interest to us is what "
                  "they are."),
        ],
        "lab": ("dddkit", {
            "mode": "identity",
            "view": "equality",
            "preset": "patients",
            "presets": [
                {"id": "patients",
                 "label": "A clinic's patient records, with issued identifiers",
                 "objects": PATIENTS,
                 "expect": {"didPairs": "6", "didIdentity": "1: (desk-ana, lab-ana)", "didAttrs": "1: (desk-ana, other-ana)", "didChanged": "1: (desk-ana, lab-ana): town", "didLookalike": "1: (desk-ana, other-ana)"}},
                {"id": "patients-keyed-by-name",
                 "label": "The same records keyed by name and birth year",
                 "objects": PATIENTS_KEYED,
                 "expect": {"didIdentity": "3: (desk-ana, lab-ana), (desk-ana, other-ana), (lab-ana, other-ana)", "didChanged": "2: (desk-ana, lab-ana): town; (lab-ana, other-ana): town", "didLookalike": "0: none"}},
            ],
            "panel_title": "Same by identity, same by attributes",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Deciding what makes two records one thing",
        "steps_intro": "Four steps, the last of them on records of your own.",
        "steps": [
            ("Ask whether users care which one",
             "For the object in question, ask whether the application's users need "
             "to know it is the same one after its attributes change. If not, it is "
             "probably not an entity."),
            ("Choose the identifier",
             "Find an attribute or combination guaranteed unique, and test it "
             "against its exceptions; failing that, assign an identifier that is "
             "unique in the system and never changes."),
            ("Compare pairs both ways",
             "For each pair of records, compare identifiers and compare attributes, "
             "and list the changed pairs and the look-alikes."),
            ("Do it on your own records",
             "Take four records of the same kind from a system you know, type them "
             "into the lab, and write down each disagreement it lists with what the "
             "system would do wrong if it matched by attributes."),
        ],
        "worked": {
            "title": "Four patients, six pairs",
            "intro": [
                "Compare the pairs of <code>patients</code>.",
            ],
            "lines": [
                "desk Ana, lab Ana: same id, town differs",
                "desk Ana, other Ana: ids differ, all alike",
                "lab Ana, other Ana: ids and town differ",
                "the three with desk Ben: all differ",
                "same by id 1, by attributes 1",
                "1 changed pair and 1 pair alike",
            ],
            "after": [
                "Two of the six pairs are where a clinic goes wrong, and neither is "
                "where identity and attributes agree. The lab finds them; why "
                "P-1047 and P-2210 are different people is a fact only the clinic "
                "holds.",
            ],
        },
        "quiz_title": "Entities, identity and Evans's claims",
        "quiz": [
            {"q": "In the exercise, comparing all six pairs of the four member "
                  "records, how many pairs are the same by identity, how many by "
                  "attributes, and how many are changed pairs and look-alikes?",
             "a": ["2 by identity, 3 by attributes; 1 changed, 2 look-alikes",
                   "2 by identity, 2 by attributes; 1 changed, 1 look-alike",
                   "2 by identity, 3 by attributes; 1 changed, 3 look-alikes",
                   "1 by identity, 3 by attributes; 1 changed, 2 look-alikes"],
             "c": 0,
             "why": "Same identifier: m1 and m2 (L-301), m3 and m4 (L-455), 2 pairs. "
                    "Same attributes: m1, m3 and m4 are alike, which gives 3 pairs. "
                    "m1 and m2 share an identifier with different branches, 1 changed "
                    "pair. m1 with m3 and m1 with m4 are alike with different "
                    "identifiers, 2 look-alikes; m3 and m4 agree on both, so they are "
                    "not a disagreement. The librarian would need to ask whether "
                    "L-455 was issued twice for one person, and whether the member "
                    "L-301 moved branch."},
            {"q": "Why does Evans say the identity operation built into an "
                  "object-oriented language, such as Java's ==, is not enough for an "
                  "entity?",
             "a": ["Because it compares attributes, which may change",
                   "Because it is too slow for large systems",
                   "Because it only compares memory locations, and a stored or "
                   "transmitted object comes back as a new instance",
                   "Because Java does not provide one"],
             "c": 2,
             "why": "The language's identity says whether two references point at one "
                    "object. Each time an object is read from a database or sent over "
                    "a network a new instance is made, and that identity is lost; the "
                    "definition of sameness has to come from the model."},
            {"q": "In Evans's stadium example, when are the seats entities?",
             "a": ["Always, since each seat has a number engraved on it",
                   "When tickets are for assigned, numbered seats",
                   "Only at general admission events",
                   "Never: seats are value objects"],
             "c": 1,
             "why": "With assigned seating the seat number identifies the seat and the "
                    "ticket names it, so seats are entities. At a general admission "
                    "event only the number of seats matters; the engraved numbers are "
                    "still there, but the software has no need to track them, and "
                    "associating tickets with seats would state a rule the event does "
                    "not have."},
            {"q": "On the preset <code>patients-keyed-by-name</code>, why does the lab report "
                  "the desk's Ana Ruiz and the other patient as the same?",
             "a": ["Because their attributes are equal",
                   "Because the lab matches by name",
                   "Because their identifiers, built from name and birth year, are "
                   "equal",
                   "It does not; it reports them as look-alikes"],
             "c": 2,
             "why": "The lab compares the identifiers it is given. Built from the name "
                    "and birth year, both records carry the same identifier, so the "
                    "pair is the same by identity; it is not a look-alike, because a "
                    "look-alike needs different identifiers. The lab's answer is "
                    "faithful to the identity stated, and the identity is wrong."},
        ],
        "mistakes": [
            ("Deciding sameness by comparing every attribute",
             "Every attribute of an entity may change while it stays the same thing, "
             "and two different things may share every attribute. Evans asks for "
             "an identification that survives any change of shape or storage, and "
             "distrusts requirements to match on fields; on the lesson's illustration, attribute matching gets both "
             "disagreeing pairs wrong."),
            ("Giving every object an identity to be safe",
             "Identity is a meaning imposed because it is useful, and the same thing "
             "in the world may or may not be an entity in a given model, as the "
             "general admission seats show. Tracking identity costs analysis and "
             "design, and the next lesson reads Evans's case against attaching it "
             "where it is not needed."),
            ("Loading the entity with every attribute and behaviour",
             "Modeling Entities asks for a spare class: the attributes that identify "
             "or match it, the behaviour essential to the concept, and little else. "
             "The rest moves to associated objects, entities or values, and the "
             "entity coordinates them."),
        ],
        "standard": (
            "Finish when you can say what makes two records one thing.",
            "Given records with identifiers and attributes, find the pairs the same "
            "by identity and by attributes, list where they disagree, and say whether "
            "the identifier follows the model's distinctions."
        ),
        "note": (
            "The lab compares identifiers and attributes exactly as typed. It cannot "
            "tell whether an identifier was issued correctly, whether a key built "
            "from attributes has exceptions, or whether two records are the same "
            "person; that is the model's definition of sameness, and often a "
            "person's judgement."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Value Objects (PDF pp. 54-56 of the operator's copy): the markers (p.
    # 54), the cost of identity (p. 55), the definition (p. 55), the address
    # sidebar (p. 55), composite values and values that reference entities
    # (p. 55), the pattern and Whole Value (p. 56); Designing Value Objects
    # (pp. 56-58): sharing, copying, Flyweight, when to allow mutability (p.
    # 57), database tuning (p. 58); Designing Associations That Involve
    # Value Objects (p. 58).
    # Quote: PDF p. 56 of the operator's copy, 25 words, quotes.py OK.
    # Lesson total: 25 words.
    {
        "slug": "value-objects",
        "title": "Value Objects",
        "module": "Chapter 5 · A Model Expressed in Software",
        "one_line": "An object we care about only for what it is, made immutable so that it can be shared, copied and passed around without anyone being surprised.",
        "summary": (
            "Evans's second kind of model element has no identity worth tracking. "
            "Read why giving everything an identity costs, what makes a value "
            "conceptually whole, and why a shared value must be immutable, then "
            "change a pickup slot that three bakery orders share and count who sees "
            "the change when the slot is mutable and when it is replaced."
        ),
        "key": [
            "no conceptual identity",
            "care about what, not which",
            "attributes that form a whole",
            "immutable: change by replacement",
            "share freely only when immutable",
            "a mutable value must not be shared",
        ],
        "key_label": "Value Objects in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the "
            "third the lab's."
        ),
        "concepts": [
            ("Value Object",
             "An object that describes some aspect of the domain and has no "
             "conceptual identity: two with the same attributes are "
             "interchangeable. Colours, amounts, names and addresses are common "
             "examples, though whether an address is one depends on the domain."),
            ("Immutable",
             "Unable to be changed once made. An immutable value is changed only by "
             "full replacement: the holder is given a new value and the old one is "
             "left as it was."),
            ("Surprised holder",
             "A holder of a shared value that sees it change through a change "
             "another holder made. The lab counts them for a mutable value, where "
             "every holder sees the change, and for an immutable one, where only the "
             "holder whose reference was replaced does."),
        ],
        "read_title": "The section's argument, then the design choices, then the count",
        "read_intro": (
            "Read Value Objects and the two sections after it in your own copy "
            "first. The lesson reads them as an argument, then counts what sharing "
            "does."
        ),
        "body": [
            ("p", "&ldquo;To protect against this, in order for an object to be shared "
                  "safely, it must be immutable: it cannot be changed except by full "
                  "replacement.&rdquo; That is Evans in Designing Value Objects, the "
                  "section after the pattern Value Objects in Chapter 5. This lesson "
                  "reads both, with Designing Associations That Involve Value "
                  "Objects. Enterprise Application Patterns reads Fowler's version in "
                  "its lesson Value Object, where the question is equality and safe "
                  "sharing in the code; Evans asks first what in the domain has no "
                  "identity, and only then how to build it."),
            ("p", "His opening image is a child drawing with markers, who cares about "
                  "a marker's colour and tip but not which of two identical markers "
                  "he holds, though he cares very much which drawings are his and "
                  "which his sister's. Since the conspicuous objects of a model are "
                  "usually entities, it is tempting to give every object an identity, "
                  "and some frameworks do. Evans counts the cost: the system must "
                  "track it all, optimisations are ruled out, defining meaningful "
                  "identities takes analysis, and an artificial identity misleads, "
                  "making every object look alike. Design, he says, is a running "
                  "fight against complexity, and special handling belongs only "
                  "where it is needed."),
            ("p", "A value object, then, describes something and has no conceptual "
                  "identity; we care what it is, not which one it is. Whether a thing "
                  "is one depends on who is asking, and Evans's address sidebar shows "
                  "it: to a mail-order firm an address is a value, to a postal "
                  "service organising rounds it is an entity in a hierarchy, and to an "
                  "electricity company it is an entity, or a value of a dwelling that "
                  "is one. Values need not be simple. They can be assembled from "
                  "other values, and can even refer to entities, as a route between "
                  "two cities does. They are often passed as parameters, often "
                  "transient, and often the attributes of entities: a person is an "
                  "entity, and the person's name is a value."),
            ("p", "Put as a rule to apply: if nobody cares which instance they "
                  "hold, only what it says, make it a value; let it carry the "
                  "meaning and operations of what it describes, never change it in "
                  "place, and give it no identity. Its parts should belong together "
                  "as one idea, Ward Cunningham's Whole Value: a street, a city and a postal code "
                  "belong together as an address, not as three fields of a person."),
            ("p", "Designing Value Objects turns that freedom into choices about "
                  "copying, sharing and immutability. Two people who share a name "
                  "are still two people, but their name objects are "
                  "interchangeable; the two people could share one, until one of "
                  "them changes name and the other's changes too. Hence the sentence "
                  "at the top of the lesson. The same danger arises when an object "
                  "hands one of its attributes to another as an argument, and the "
                  "cure is the same, immutability or a copy. Sharing can save "
                  "enormous numbers of objects, the Flyweight of Gamma and his "
                  "colleagues, though in a distributed system a copy may be cheaper "
                  "than a reference; Evans restricts sharing to where space matters, "
                  "communication is cheap and the value is strictly immutable."),
            ("p", "He allows mutable values in special cases, for performance: values "
                  "that change often, objects expensive to create or delete, "
                  "replacement that would disturb how the database clusters data, or "
                  "little sharing in the first place. The rule that goes with it is "
                  "absolute: a mutable value must not be shared. The last section "
                  "adds that a two-way association between two value objects makes "
                  "no sense, since without identity it means nothing to say that a "
                  "value refers back to the very one that refers to it; if such a link seems needed, "
                  "the object may have an identity not yet recognised."),
            ("p", "Now the count, on a bakery whose orders each hold a pickup slot. "
                  "The lab takes the holders as records of an order and the value it "
                  "holds, the value in question, the holder through which it is "
                  "changed, and whether the value is mutable. On the preset "
                  "<code>slot-shared-mutable</code> three orders hold the one slot "
                  "Saturday nine to eleven, and the customer of order 18 moves her "
                  "pickup an hour later by changing the slot in place. The lab counts "
                  "3 holders of the value, 3 that see the change, 2 surprised, orders "
                  "17 and 19, and 0 new values. Two customers have been moved "
                  "without asking."),
            ("p", "The preset <code>slot-shared-immutable</code> is the same orders with an "
                  "immutable slot, written below. Moving order 18 now builds a new "
                  "slot and gives order 18 the reference; the old one is untouched. "
                  "The lab counts 3 holders, 1 that sees the change, 0 surprised and "
                  "1 new value. The new object is the price of the safety, and the "
                  "reason Evans lists object creation among his grounds for allowing "
                  "mutability."),
            ("code", _lines(PICKUP_SLOT)),
            ("p", "The preset <code>slot-copied-mutable</code> is Evans's special case done "
                  "properly: the slot is mutable, but each order holds its own copy. "
                  "Changing order 18's copy reaches 1 holder, surprises 0 and creates "
                  "0 new values. It is safe for the reason his rule gives, that "
                  "nothing is shared, and it gives up the sharing that made values "
                  "cheap. The counts are of the lesson's illustration; which "
                  "trade-off a real bakery should take depends on how often slots "
                  "change and how many orders hold them, which the lab does not "
                  "know."),
            ("h3", "Exercise"),
            ("ul", [
                "A school's classes and the term dates each holds: `class-7a, "
                "autumn; class-7b, autumn; class-7c, autumn; class-8a, autumn; "
                "class-8b, spring`.",
                "Class 7c's trip moves its last day, and the change is made through "
                "`class-7c` to the value `autumn`.",
            ]),
            ("p", "Count, for a mutable and for an immutable value, the holders of "
                  "<code>autumn</code>, the holders that see the change, the holders "
                  "surprised and the new values made. Then say in one sentence "
                  "whether a term's dates are a value to this school at all."),
            ("p", "Some things in a domain are neither who nor what but an action. "
                  "The next lesson, Services, reads the third kind of model element."),
        ],
        "lab": ("dddkit", {
            "mode": "identity",
            "view": "sharing",
            "preset": "slot-shared-mutable",
            "presets": [
                {"id": "slot-shared-mutable",
                 "label": "Three orders share one mutable pickup slot",
                 "holders": SLOT_HOLDERS,
                 "value": "sat-9-11",
                 "change": "order-18",
                 "kind": "mutable",
                 "expect": {"didHolders": "3: order-17, order-18, order-19", "didSee": "3: order-17, order-18, order-19", "didSurprised": "2: order-17, order-19", "didNew": "0"}},
                {"id": "slot-shared-immutable",
                 "label": "The same orders sharing an immutable slot",
                 "holders": SLOT_HOLDERS,
                 "value": "sat-9-11",
                 "change": "order-18",
                 "kind": "immutable",
                 "expect": {"didSee": "1: order-18", "didSurprised": "0: none", "didNew": "1: sat-9-11′, now held by order-18"}},
                {"id": "slot-copied-mutable",
                 "label": "A mutable slot, but a copy for each order",
                 "holders": SLOT_COPIES,
                 "value": "sat-9-11-b",
                 "change": "order-18",
                 "kind": "mutable",
                 "expect": {"didHolders": "1: order-18", "didSurprised": "0: none", "didNew": "0"}},
            ],
            "panel_title": "Who sees a change to a shared value",
            "panel_intro": _PANEL_INTRO,
        }),
        "steps_title": "Making a value safe to share",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Ask whether anyone cares which one",
             "For the object in question, ask whether swapping it for an equal one "
             "would matter to anyone. If not, make it a value object."),
            ("Gather a whole",
             "Collect the attributes that belong together into one value with the "
             "behaviour of what they mean, as a slot's day and times are."),
            ("Change by replacement",
             "Make every field final and every change a method that returns a new "
             "value, and replace the holder's reference to change it."),
            ("Do it on your own code",
             "Find a small object in a system you know that several others hold, "
             "type its holders into the lab, and count the holders surprised if it "
             "were changed in place. Write down whether it is immutable today."),
        ],
        "worked": {
            "title": "One slot, three orders",
            "intro": [
                "Count <code>slot-shared-mutable</code> and <code>slot-shared-immutable</code>.",
            ],
            "lines": [
                "holders of the Saturday slot: 17, 18, 19",
                "mutable: all three see the move",
                "surprised: 17 and 19, so 2; new values 0",
                "immutable: order 18 gets its own new slot",
                "sees it: 18 only; surprised 0; new 1",
            ],
            "after": [
                "Order 20 holds another value and is never counted. The difference "
                "between 2 surprised and 0 is the whole of Evans's rule; the one new "
                "object is its price.",
            ],
        },
        "quiz_title": "Values, sharing and Evans's claims",
        "quiz": [
            {"q": "In the exercise, the change is made through class-7c to the value "
                  "autumn. What are the holders that see it and the holders surprised, "
                  "first for a mutable value and then for an immutable one?",
             "a": ["Mutable: 4 see it, 3 surprised. Immutable: 1 sees it, 0 surprised",
                   "Mutable: 5 see it, 4 surprised. Immutable: 1 sees it, 0 surprised",
                   "Mutable: 4 see it, 4 surprised. Immutable: 1 sees it, 0 surprised",
                   "Mutable: 4 see it, 3 surprised. Immutable: 4 see it, 3 surprised"],
             "c": 0,
             "why": "Four classes hold autumn; 8b holds spring and is not counted. "
                    "Mutable: all four see the change, and the three that did not make "
                    "it, 7a, 7b and 8a, are surprised. Immutable: 7c is given a new "
                    "value, 1 sees the change, 0 are surprised, and 1 new value is "
                    "made. Whether the dates are a value is the school's question: "
                    "they are if nobody cares which autumn object a class holds, "
                    "only what dates it carries."},
            {"q": "Evans allows a value object to be mutable in some cases. What rule "
                  "does he attach?",
             "a": ["It must have an identifier",
                   "It must not be shared",
                   "It must be declared final in the language",
                   "It must be stored in its own table"],
             "c": 1,
             "why": "If a value's implementation is mutable, it must not be shared; "
                    "and he adds that values should be designed immutable whenever "
                    "they can be. The preset <code>slot-copied-mutable</code> follows the "
                    "rule: each order holds its own copy, and no one is surprised. "
                    "Declaring immutability in the language, he says, helps "
                    "communicate the decision but is not essential, and it is no "
                    "condition of mutability."},
            {"q": "In Evans's address sidebar, when is an address a value object?",
             "a": ["In every system, since an address is a set of attributes",
                   "For the postal service organising delivery rounds",
                   "For a mail-order company that uses it to confirm a card and send "
                   "a parcel",
                   "Never, since an address can change"],
             "c": 2,
             "why": "To the mail-order company it does not matter that two customers "
                    "share an address, so the address is a value. To the postal "
                    "service it is an entity in a hierarchy of regions and zones, and "
                    "to the electricity company an entity too, unless the model makes "
                    "the dwelling the entity and the address its value."},
            {"q": "What does Evans say about a two-way association between two value "
                  "objects?",
             "a": ["It makes no sense, and if one seems needed the object may have an "
                   "identity not yet recognised",
                   "It is fine if both values are immutable",
                   "It is required when a value refers to an entity",
                   "It should be qualified to make it one-to-one"],
             "c": 0,
             "why": "Without identity it means nothing to say that a value refers "
                    "back to the very one that refers to it, only to an equal one. He asks "
                    "that such links be removed entirely, and if one still seems "
                    "needed, that the decision to make the object a value be "
                    "rethought."},
        ],
        "mistakes": [
            ("Giving every domain object an identity, in case it is needed",
             "Evans counts the cost of doing so: all that tracking, optimisations ruled "
             "out, analysis spent on meaningless identities, and a model in which "
             "every object looks the same. Identity belongs where the domain needs "
             "it; a value object is the positive category for everything else, with "
             "meaning and behaviour of its own."),
            ("Sharing a mutable value",
             "Sharing is safe only when the value cannot change except by "
             "replacement; otherwise a change through one holder reaches every "
             "other, as the lesson's illustration counts. Evans allows a mutable "
             "value for performance, and then forbids sharing it."),
            ("Thinking a value object must be simple",
             "Strings and numbers are values, but so is a rich object with "
             "behaviour, an assembly of other values, or a route that refers to "
             "entities. What makes a value is having no conceptual identity, not "
             "being small."),
        ],
        "standard": (
            "Finish when you can say who sees a change to a shared value.",
            "Given holders of a value, the holder that changes it and whether it is "
            "mutable, count the holders who see the change and those surprised, and "
            "say what immutability costs."
        ),
        "note": (
            "The lab follows references as stated. It cannot tell whether an object "
            "should be a value in your domain, whether a holder wanted the change it "
            "saw, or whether new objects or shared references cost more on your "
            "platform; Evans leaves that to the implementation environment."
        ),
    },
]
