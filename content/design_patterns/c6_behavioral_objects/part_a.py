"""Behavioral Patterns II, lessons 1-5 -- Chapter 5's last five patterns.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 5, Behavioral
Patterns: Observer, State, Strategy, Template Method and Visitor. Pages in the
comments are PDF pages of the operator's copy (PDF page = printed page + 20);
the lessons cite by chapter, section and pattern. Every quotation is copied
from that copy and checked with quotes.py. The designs, records and Java are
written for these lessons: none of the book's code, diagrams or example data
is reproduced, and no lab uses the book's example domains (no spreadsheet and
bar chart, no network-connection states, no line-breaking compositors, no
document-opening framework, no syntax trees or equipment). The design is
docs/design-patterns/PLAN.md, section C, Course 6.
"""


def _lines(text):
    """A snippet or record constant as a code block's list of lines."""
    return text.split("\n")


def _records(text):
    """Records written one to a line, as the single string a lab field takes."""
    return " ".join(line.strip() for line in text.split("\n") if line.strip())


# ---------------------------------------------------------------- 6.1 Observer

# A theatre box office: three subjects, four observers, four operations. The
# re-pricing releases held seats, so it changes prices and then seats; a
# matinee adds a performance, its prices and its seats; an exchange releases
# one seat and takes another, two changes to seats.
BOX_SUBJECTS = "seats prices schedule"

BOX_OBSERVERS = """seatmap, seats, prices;
kiosk, seats, prices, schedule;
mailer, schedule;
report, seats"""

BOX_OPERATIONS = """sale, seats;
reprice, prices, seats;
matinee, schedule, prices, seats;
exchange, seats, seats"""

SEAT_PLAN_JAVA = """interface SeatObserver {
    void update(SeatPlan changed);   // pull: ask the plan what it needs
}
class SeatPlan {
    private final List<SeatObserver> observers = new ArrayList<>();
    private final Set<String> sold = new HashSet<>();

    void attach(SeatObserver o) { observers.add(o); }
    void detach(SeatObserver o) { observers.remove(o); }

    void sell(String seat) {
        sold.add(seat);         // make the state consistent first,
        notifyObservers();      // then tell every observer, every time
    }
    boolean isSold(String seat) { return sold.contains(seat); }

    private void notifyObservers() {
        for (SeatObserver o : observers) { o.update(this); }
    }
}"""

# Exercise: a garden irrigation controller.
IRRIGATION_EXERCISE = """subjects:    soil rain
observers:   valve, soil, rain; panel, soil, rain; phone, rain
operations:  dawn, soil, rain; shower, rain, rain, soil"""


# ---------------------------------------------------------------- 6.2 State

# A library copy. The event "return" is a name in the lab; in Java the method
# is giveBack, since return is a keyword.
COPY_STATES = "shelf onloan held overdue lost"
COPY_EVENTS = "lend return hold due renew expire writeoff"
COPY_TRANSITIONS = """shelf, lend, onloan;
shelf, hold, held;
onloan, return, shelf;
onloan, due, overdue;
onloan, renew, onloan;
held, lend, onloan;
held, expire, shelf;
overdue, return, shelf;
overdue, writeoff, lost"""
COPY_INPUT = "return lend renew due renew return hold lend due writeoff"

# The same copy with a repair state: damage sends a copy on the shelf or on
# loan to repair, and fix brings it back to the shelf.
REPAIR_STATES = COPY_STATES + " repair"
REPAIR_EVENTS = COPY_EVENTS + " damage fix"
REPAIR_TRANSITIONS = COPY_TRANSITIONS + """;
shelf, damage, repair;
onloan, damage, repair;
repair, fix, shelf"""
REPAIR_INPUT = "lend damage fix hold expire"

COPY_STATE_JAVA = """interface CopyState {   // an event a state ignores leaves it as it is
    default CopyState lend()     { return this; }
    default CopyState giveBack() { return this; }
    default CopyState fallDue()  { return this; }
}
enum Shelf implements CopyState { INSTANCE;
    public CopyState lend() { return OnLoan.INSTANCE; }
}
enum OnLoan implements CopyState { INSTANCE;
    public CopyState giveBack() { return Shelf.INSTANCE; }
    public CopyState fallDue()  { return Overdue.INSTANCE; }
}
// Held, Overdue and Lost are written the same way.
final class Copy {
    private CopyState state = Shelf.INSTANCE;
    void lend()     { state = state.lend(); }
    void giveBack() { state = state.giveBack(); }
    void fallDue()  { state = state.fallDue(); }
}"""

# Exercise: a museum audio guide's handset.
HANDSET_EXERCISE = """states:       docked ready playing paused   (docked is the start)
events:       lift play pause dock
transitions:  docked, lift, ready; ready, play, playing;
              playing, pause, paused; paused, play, playing;
              playing, dock, docked; paused, dock, docked;
              ready, dock, docked
input:        play lift play pause pause play dock lift"""


# ---------------------------------------------------------------- 6.3 Strategy

PRINT_BY_METHOD = """long quoteCents(Job job) {
    int sheets = job.pages() * job.copies();
    switch (job.method()) {
        case OFFSET:
            if (job.copies() < 500) { return 9000 + 4 * sheets; }
            return 9000 + 3 * sheets;
        case RISO:
            return 2500 + 2 * sheets;
        case DIGITAL:
            return 20 * sheets;
        default:
            throw new IllegalStateException("no such method");
    }
}
int daysToPrint(Job job) {
    if (job.method() == Method.OFFSET) { return 5; }
    if (job.method() == Method.RISO && job.copies() > 1000) { return 3; }
    return 1;
}"""

PRINT_METHODS = """interface PrintMethod {
    long quoteCents(int sheets, int copies);
    int daysToPrint(int copies);
}
class Offset implements PrintMethod {
    public long quoteCents(int sheets, int copies) {
        if (copies < 500) { return 9000 + 4 * sheets; }
        return 9000 + 3 * sheets;
    }
    public int daysToPrint(int copies) { return 5; }
}
class Riso implements PrintMethod {
    public long quoteCents(int sheets, int copies) { return 2500 + 2 * sheets; }
    public int daysToPrint(int copies) {
        if (copies > 1000) { return 3; }
        return 1;
    }
}
// Digital is written the same way, and tests nothing."""

QUIZ_POINTS = """// A quiz app scores an answer by the round's mode.
int points(Answer a, Mode mode) {
    if (!a.correct()) {
        return 0;
    }
    if (mode == Mode.TIMED && a.seconds() < 5) {
        return 15;
    }
    if (mode == Mode.TIMED) {
        return 10;
    }
    if (mode == Mode.STREAK) {
        return 5 * a.streak();
    }
    return 10;
}"""


# ---------------------------------------------------------------- 6.4 Template Method

TILE_STEPS = """fetch, fixed;
decode, primitive;
style, primitive;
label, hook;
shade, hook;
cache, fixed;
show, fixed"""

TILE_SUBCLASSES = """RoadTile, decode, style, label;
SatelliteTile, decode, style;
TerrainTile, decode, shade"""

TILE_SUBCLASSES_FIXED = """RoadTile, decode, style, label;
SatelliteTile, decode, style;
TerrainTile, decode, style, shade"""

MAP_TILE_JAVA = """abstract class MapTile {
    public final Image render(TileKey key) {       // the template method
        byte[] raw = fetch(key);
        Image img = style(decode(raw));
        label(img);                                // hook
        shade(img);                                // hook
        cache(key, img);
        return show(img);
    }
    protected abstract Image decode(byte[] raw);   // primitive: must be written
    protected abstract Image style(Image img);     // primitive: must be written
    protected void label(Image img) { }            // hook default: nothing
    protected void shade(Image img) { }
    private byte[] fetch(TileKey key) { return TileStore.download(key); }
    private void cache(TileKey key, Image img) { TileStore.keep(key, img); }
    private Image show(Image img) { return img; }
}"""

COFFEE_EXERCISE = """steps:       take, fixed; brew, primitive; milk, hook; serve, fixed
subclasses:  Espresso, brew; Latte, brew, milk; Cortado, milk"""


# ---------------------------------------------------------------- 6.5 Visitor

# A music playlist: folders hold tracks, podcast episodes and folders. Values
# are minutes.
PLAYLIST_NODES = """library, -, Folder, -;
morning, library, Folder, -;
run, library, Folder, -;
sunrise, morning, Track, 4.5;
news, morning, Episode, 22;
tempo, run, Track, 3.75;
climb, run, Track, 5.25;
talk, library, Episode, 31"""

PLAYLIST_JAVA = """interface PlaylistVisitor {
    void visitFolder(Folder f);
    void visitTrack(Track t);
    void visitEpisode(Episode e);
}
interface Entry { void accept(PlaylistVisitor v); }

final class Folder implements Entry {
    final List<Entry> entries = new ArrayList<>();
    public void accept(PlaylistVisitor v) {
        for (Entry e : entries) { e.accept(v); }   // the structure traverses
        v.visitFolder(this);
    }
}
final class Track implements Entry {
    final double minutes;
    Track(double minutes) { this.minutes = minutes; }
    public void accept(PlaylistVisitor v) { v.visitTrack(this); }
}
// Episode is written like Track; each visitor implements all three visits."""

MUSEUM_EXERCISE = """nodes:     museum, -, Wing, -; east, museum, Wing, -;
           vase, east, Exhibit, 1; mask, east, Exhibit, 1;
           film, museum, Screen, 1
visitors:  audio map count
adding:    a new kind of element, Shop"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 5, Observer (PDF pp. 313-323 of the operator's copy): Intent and
    # Motivation p. 313-314, Applicability p. 314, Participants and
    # Collaborations p. 315, Consequences p. 316, Implementation pp. 317-320,
    # Sample Code pp. 320-323, Known Uses and Related Patterns p. 323.
    # Quote: PDF p. 316 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    {
        "slug": "observer",
        "title": "Observer",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "One object changes and every object that depends on it hears about it, without the changing object knowing who they are.",
        "summary": (
            "Observer sets up a one-to-many dependency: when a subject changes, each of "
            "its observers is told and brings itself up to date. Read the pattern, then "
            "count the updates a box office's four operations send to four observers when "
            "every change notifies at once, and when a change manager waits for the end "
            "of each operation."
        ),
        "key": [
            "a subject knows only the Observer interface",
            "a change can reach every observer",
            "decide who calls notify",
            "push assumes; pull asks",
            "a change manager sends one per operation",
            "say which operations notify",
        ],
        "key_label": "Observer in six lines",
        "concepts_intro": (
            "Three ideas from Observer, the last of them what the lab's second scheme "
            "models."
        ),
        "concepts": [
            ("Subject and observer",
             "A subject holds state other objects depend on and keeps a list of them; an "
             "observer is any object that wants to hear when that state changes. The "
             "subject sees its observers only through one small updating interface, so it "
             "never needs their concrete classes."),
            ("Push and pull",
             "Two ends of a range for what a notification carries. Under push the subject "
             "sends details of the change, whether wanted or not; under pull it sends next "
             "to nothing, and each observer asks the subject for what it needs."),
            ("Change manager",
             "An object placed between subjects and observers that keeps the mapping "
             "between them, owns the update strategy, and does the notifying. One that "
             "waits until an operation has finished changing several subjects can send "
             "each observer a single update instead of one per change."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Observer, in Chapter 5, Behavioral Patterns, in your own copy first. "
            "The lesson reads the pattern as a tool, section by section, and then counts "
            "the updates one design sends."
        ),
        "body": [
            ("p", "&ldquo;A seemingly innocuous operation on the subject may cause a "
                  "cascade of updates to observers and their dependent objects.&rdquo; That "
                  "warning comes from the Consequences of Observer, the first of the five "
                  "patterns that close Chapter 5, Behavioral Patterns. The pattern's intent, "
                  "in other words: when one object's state changes, the objects that depend "
                  "on it should be told and should update themselves, without anyone wiring "
                  "them together by hand. The book also knows it as Dependents and as "
                  "Publish-Subscribe."),
            ("p", "The Motivation starts from a familiar problem. Split a system into "
                  "cooperating classes and you must keep related objects consistent, but "
                  "tight coupling between them would spoil their reuse. The book's example, "
                  "summarised: a user interface toolkit keeps application data apart from its "
                  "presentations, so that a table view and a chart of the same data can each "
                  "be reused alone, yet a change typed into one shows up at once in the other. "
                  "Neither view knows the other exists; both depend on the data. The Applicability's cases come down to one: some objects must keep up "
                  "with another's state, and the one that changes should not have to know "
                  "which objects they are, or how many."),
            ("p", "The participants are four. The Subject knows its observers, however "
                  "many, and offers operations to attach and detach them. The Observer "
                  "declares the updating interface. A ConcreteSubject holds the state its "
                  "observers care about and notifies them when it changes; a ConcreteObserver "
                  "keeps a reference to its subject and its own state in step with it. In "
                  "the collaboration the subject notifies, and each observer may then query "
                  "the subject to reconcile itself. Even the observer whose request caused "
                  "the change waits for the notification before updating, and notify need "
                  "not be called by the subject at all."),
            ("p", "The Consequences open with the benefit: subjects and observers vary "
                  "independently, and observers can be added without touching the subject "
                  "or each other. Three more follow. The coupling is abstract and minimal, "
                  "so a low-level subject can inform a high-level observer without breaking "
                  "the system's layers. Communication is broadcast: the notification names "
                  "no receiver, and each observer handles or ignores it. The liability is "
                  "the one the opening quotation names. Observers cannot see each other, so "
                  "none can see what a change to the subject will cost in all; loosely kept "
                  "dependencies give spurious updates that are hard to trace; and the simple "
                  "protocol says nothing about what changed, so observers may work hard to "
                  "find out."),
            ("code", _lines(SEAT_PLAN_JAVA)),
            ("p", "The sketch above is the lesson's own, in Java: a seat plan that "
                  "notifies after every sale. It uses the pull model, and it passes itself in "
                  "the update, which is how the book lets one observer watch several subjects "
                  "and tell them apart. It also changes its state before it notifies, the "
                  "self-consistency rule of the Implementation: observers query the subject "
                  "as they update, so a subclass that notifies through an inherited "
                  "operation and then changes more state has notified too early. The book's "
                  "remedy is a template method in the abstract subject that calls the "
                  "subclass's primitive operation and notifies last (Template Method, two "
                  "lessons on), and it advises documenting which operations notify."),
            ("p", "The Implementation lists nine issues; the rest, briefly. A subject can "
                  "hold its observers itself or, when subjects are many and observers few, "
                  "leave the mapping in a hash table, saving space at some cost in time. "
                  "Who triggers the update is a real choice: if the subject's state-setting "
                  "operations notify, clients cannot forget, but a run of changes sends a run "
                  "of updates; if clients notify when they are done, the needless updates go, "
                  "and a forgotten call becomes a bug. A deleted subject should tell its "
                  "observers so they hold no dangling reference. Push makes observers less "
                  "reusable, since the subject assumes what they need; pull may be "
                  "inefficient, since they must work out what changed. Observers can register "
                  "interest in particular aspects of a subject. Smalltalk, without multiple "
                  "inheritance, puts both interfaces in one class."),
            ("p", "The eighth issue is the one the lab models. When the dependencies are "
                  "complicated, a ChangeManager can map subjects to observers, define the "
                  "update strategy and do the updating. The book sketches two: a simple one "
                  "that updates every observer of each subject, and one for acyclic graphs "
                  "of dependencies that makes sure an observer of several changed subjects "
                  "gets one update. It notes that a ChangeManager is an instance of Mediator, "
                  "the last course's lesson of that name, and usually a Singleton. The "
                  "Sample Code, in C++, has a clock timer as subject and a digital and an "
                  "analog clock as observers. Known Uses begins with Smalltalk's "
                  "Model/View/Controller, and goes on to ET++, the THINK library, "
                  "InterViews, the Andrew Toolkit and Unidraw."),
            ("p", "Now the lab, on a theatre box office of the lesson's own. Its subjects "
                  "are seats, prices and the schedule. The seat map watches seats and "
                  "prices, the kiosk all three, the mailer the schedule, the nightly report "
                  "seats. Four operations change them: a sale changes seats; a re-pricing "
                  "changes prices and then seats, since it releases held seats; a new "
                  "matinee changes schedule, prices and seats; an exchange changes seats "
                  "twice. On the preset <code>box-office-direct</code> each change notifies "
                  "at once. The lab counts 8 changes and 21 updates sent, one for every "
                  "observer of the subject on each change: the seat map receives 7, the "
                  "kiosk 8, the mailer 1, the report 5. No observer goes unnotified and no "
                  "subject is unwatched, so those two tiles read <code>0: none</code>."),
            ("p", "The preset <code>box-office-managed</code> runs the same operations "
                  "through a change manager that sends one update per observer per "
                  "operation, to each observer of anything the operation changed. It sends "
                  "13: 3, 3, 4 and 3. The tile for the other scheme gives the direct figure "
                  "beside it, and the difference, 8, is the redundant updates the manager "
                  "saves. Redundant is the book's word and not a fault: the simple manager, "
                  "it says, is fine when several updates do no harm. The count says how many "
                  "updates each design sends here. It does not weigh them: a kiosk redraw "
                  "and a log line count the same."),
            ("h3", "Exercise"),
            ("code", _lines(IRRIGATION_EXERCISE)),
            ("p", "A garden irrigation controller: two subjects, three observers, two "
                  "operations, the second changing rain twice. By hand, count the changes, "
                  "the updates sent when each change notifies at once, and the updates a "
                  "change manager sends when it waits for the end of each operation. Then "
                  "type the design into the lab to check."),
            ("p", "Observer lets the dependents decide what to do about a change. The next "
                  "lesson, State, turns to an object whose own behaviour must change with "
                  "its state."),
        ],
        "lab": ("gofkit", {
            "mode": "notify",
            "view": "observer",
            "preset": "box-office-direct",
            "subjects": BOX_SUBJECTS,
            "observers": _records(BOX_OBSERVERS),
            "operations": _records(BOX_OPERATIONS),
            "presets": [
                {"id": "box-office-direct",
                 "label": "A box office: every change notifies at once",
                 "scheme": "direct",
                 "expect": {"gnoChanges": "8",
                            "gnoSent": "21",
                            "gnoOther": "managed: 13",
                            "gnoRedundant": "8",
                            "gnoPer": "seatmap 7, kiosk 8, mailer 1, report 5",
                            "gnoNever": "0: none",
                            "gnoUnobserved": "0: none"}},
                {"id": "box-office-managed",
                 "label": "The same box office through a change manager",
                 "scheme": "managed",
                 "expect": {"gnoSent": "13",
                            "gnoOther": "direct: 21",
                            "gnoRedundant": "8",
                            "gnoPer": "seatmap 4, kiosk 4, mailer 1, report 4"}},
            ],
            "panel_title": "The updates a change sends",
        }),
        "steps_title": "Counting the updates a change sends",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("List subjects and observers",
             "Write each subject, and each observer with the subjects it watches. Count "
             "each subject's observers."),
            ("List the operations",
             "For each operation a client performs, write the subjects it changes, in "
             "order, repeating a subject it changes twice."),
            ("Count both ways",
             "Direct: for each change, add the observers of the subject changed. Managed: "
             "for each operation, count the distinct observers of anything it changed. The "
             "difference is what the change manager saves."),
            ("Do it on a design of your own",
             "Pick a model in code you know with listeners or subscribers. Count the "
             "updates one busy operation sends, and say who calls notify there and whether "
             "it pushes or pulls."),
        ],
        "worked": {
            "title": "Twenty-one updates, or thirteen",
            "intro": [
                "Count the updates on <code>box-office-direct</code>, then managed.",
            ],
            "lines": [
                "observers: seats 3, prices 2, schedule 2",
                "sale: 3",
                "reprice: 2 + 3 = 5",
                "matinee: 2 + 2 + 3 = 7",
                "exchange: 3 + 3 = 6",
                "direct: 3 + 5 + 7 + 6 = 21",
                "managed: 3 + 3 + 4 + 3 = 13",
                "saved: 21 − 13 = 8",
            ],
            "after": [
                "Only the mailer's figure is the same under both schemes: it watches one "
                "subject, which one operation changes once.",
            ],
        },
        "quiz_title": "Updates, triggers and models",
        "quiz": [
            {"q": "In the exercise, how many updates are sent when each change notifies at "
                  "once, and how many through a change manager that waits for the end of "
                  "each operation?",
             "a": ["13 and 6", "10 and 6", "13 and 10", "13 and 3"],
             "c": 0,
             "why": "Soil has 2 observers and rain 3. Dawn changes soil and rain, 2 + 3 = 5; "
                    "the shower changes rain twice and soil once, 3 + 3 + 2 = 8; 13 in all. "
                    "The manager sends each observer of anything changed one update per "
                    "operation, and both operations reach all three observers: 3 + 3 = 6. "
                    "10 and 6 counts the shower's second rain change as none; 13 and 10 sends "
                    "one update per observer per subject changed; 13 and 3 manages the whole "
                    "script as if it were one operation."},
            {"q": "In the Implementation's issue on who triggers the update, what is the "
                  "drawback of making clients call notify?",
             "a": ["A run of changes sends a run of updates",
                   "A client may forget to call it",
                   "The subject must store a reference to each observer",
                   "Observers can no longer query the subject"],
             "c": 1,
             "why": "Leaving notify to clients lets them wait until a series of changes is "
                    "done, at the price of one more thing to remember. A run of updates is "
                    "the drawback of the other option, notifying from the state-setting "
                    "operations; neither option changes how observers are stored or "
                    "queried."},
            {"q": "Which update model does the book say may make observers less reusable, "
                  "and why?",
             "a": ["Pull, because observers must work out what changed",
                   "Push, because the subject assumes what its observers need",
                   "Registering for aspects, because observers must name events",
                   "Pull, because the subject passes itself in the update"],
             "c": 1,
             "why": "Under push the subject sends details chosen for the observers it "
                    "expects, an assumption that may not hold for the next observer. Pull's "
                    "cost is efficiency, not reuse: observers must find out what changed "
                    "without help."},
            {"q": "On <code>box-office-managed</code>, why does the seat map receive 4 "
                  "updates rather than 7?",
             "a": ["The manager sends it one update per subject it watches",
                   "The manager sends it one update per operation that changed seats or "
                   "prices",
                   "The manager drops the exchange, which changes nothing new",
                   "It receives one update per subject per operation"],
             "c": 1,
             "why": "All four operations change seats or prices, so the seat map receives "
                    "one update for each: 4, not one per subject, which would be 2. Directly it would receive one per change to "
                    "either subject: 1 + 2 + 2 + 2 = 7. One per subject per operation would "
                    "give 1 + 2 + 2 + 1 = 6."},
        ],
        "mistakes": [
            ("Treating a change to a subject as cheap because the subject does so little",
             "The subject only loops over a list, but every observer on it does its own "
             "work, and an observer may be a subject in turn; Consequences names the "
             "cascade and the spurious updates of ill-kept dependencies. On the lesson's "
             "illustration four operations send 21 updates; the lab counts them and cannot "
             "follow an observer that notifies others."),
            ("Notifying before the subject is consistent",
             "Observers query the subject while they update. A subclass operation that "
             "calls an inherited operation which notifies, and then changes more state, "
             "has told its observers about a state that never existed. The book's remedy is "
             "a template method that notifies last."),
            ("Reading redundant updates as a defect",
             "The updates a change manager saves are redundant in the book's sense, more "
             "than one per operation, and the book says the simple manager is fine when "
             "that does no harm. Whether 8 saved updates matter depends on what each costs, "
             "which the count does not say."),
        ],
        "standard": (
            "Finish when you can count what a change sends to its observers.",
            "Given subjects, observers and operations, count the updates sent directly "
            "and through a change manager, and name the implementation choice each "
            "figure depends on."
        ),
        "note": (
            "The lab counts updates, one each, and stops at the first observers: it does "
            "not model an observer that is also a subject, so the cascade the book warns "
            "of is something to look for in your own code, not something these figures "
            "show."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 5, State (PDF pp. 325-333 of the operator's copy): Intent and
    # Motivation p. 325-326, Applicability and Participants p. 326,
    # Collaborations and Consequences pp. 327-328, Implementation pp. 328-329,
    # Sample Code pp. 329-332, Known Uses and Related Patterns p. 333.
    # Quote: PDF p. 325 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "state",
        "title": "State",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "An object whose behaviour depends on its state hands each request to an object standing for that state, and swaps it when the state changes.",
        "summary": (
            "State gives each state of an object a class of its own, and lets the object "
            "delegate to whichever is current. Read the pattern, then trace a library "
            "copy through ten events, and count the branches one conditional needs "
            "against the classes State needs, before and after a repair state is added."
        ),
        "key": [
            "one class for every state",
            "the context delegates to its state",
            "a transition rebinds one variable",
            "stateless states can be shared",
            "say who chooses the next state",
            "tables define transitions; State, behaviour",
        ],
        "key_label": "State in six lines",
        "concepts_intro": (
            "Three ideas from State, the last of them the comparison the lab counts."
        ),
        "concepts": [
            ("Context and state object",
             "The context is the object clients use; it holds a reference to one state "
             "object and passes each state-dependent request to it. Changing state is "
             "replacing that reference with another state object."),
            ("Transition",
             "A move from one state to the next on some event. Under State it is "
             "written in a state class, or in the context when the rules are fixed; as "
             "flags and assignments it has no place of its own in the code."),
            ("Branches against classes",
             "With one conditional the code needs a branch for each transition and a "
             "default for each state that ignores the rest; with State it needs a class "
             "per state, plus the context and the abstract state. The lab counts both."),
        ],
        "read_title": "The pattern first, then the trace",
        "read_intro": (
            "Read State, in Chapter 5, Behavioral Patterns, in your own copy first. The "
            "lesson reads it section by section, then traces one machine and counts what "
            "each way of writing it needs."
        ),
        "body": [
            ("p", "&ldquo;Allow an object to alter its behavior when its internal state "
                  "changes. The object will appear to change its class.&rdquo; That is the "
                  "intent of State, the next pattern of Chapter 5, Behavioral Patterns, "
                  "also called Objects for States. The second sentence is the striking one: "
                  "a client calling the same operation on the same object gets different "
                  "behaviour, as if the object had been replaced by an instance of some "
                  "other class."),
            ("p", "The book's Motivation, summarised, is a network connection that answers "
                  "an open or a close request differently depending on whether it is "
                  "established, listening or closed. An abstract state class declares the "
                  "requests; one subclass per state implements them; the connection keeps an "
                  "instance of the current one, forwards every state-specific request to it, "
                  "and swaps it for another when the state changes. Reach for it, on the Applicability's "
                  "reading, when what an object does at run time turns on a status it "
                  "carries, and that status is tested by switch after switch through its "
                  "methods; each tested case becomes a class."),
            ("p", "Three participants. The Context is the interface clients use and holds "
                  "the current concrete state. The State declares the interface for "
                  "behaviour tied to a state. Each ConcreteState implements it for one state. "
                  "In the collaborations the context delegates; it may pass itself so the "
                  "state can reach its data; clients may configure it with states and then "
                  "never touch them; and either the context or the states may decide which "
                  "state comes next."),
            ("p", "The Consequences are three. State localizes what each state does, so a "
                  "new state is a new subclass; the alternative, data values the context's "
                  "operations test, spreads similar conditionals through every operation, "
                  "and a new state can mean editing several. The authors are fair about the "
                  "cost: more classes, less compact than one class, and worth it when there "
                  "are many states. Second, transitions become explicit, and atomic from the "
                  "context's side, one variable rebound instead of several. Third, state "
                  "objects with no fields can be shared among contexts: flyweights, in the "
                  "book's terms, with behaviour and no intrinsic state."),
            ("code", _lines(COPY_STATE_JAVA)),
            ("p", "The sketch is the lesson's own: a library copy whose states are Java "
                  "enums, so each is a single shared instance, as the book's sample makes its "
                  "states Singletons. The interface's default methods return the state "
                  "unchanged, which is how an ignored event looks here, and each state "
                  "returns its successor, so the states choose the transitions and the copy "
                  "only rebinds. The method is <code>giveBack</code> because "
                  "<code>return</code> is a Java keyword."),
            ("p", "The Implementation asks first who defines the transitions. Fixed rules "
                  "can live in the context; letting the states name their successors is "
                  "usually more flexible and easier to extend, at the price that each state "
                  "class knows at least one other. Second, a table-driven alternative from "
                  "Cargill's C++ Programming Style maps each state and input to the next "
                  "state: regular, and changed by editing data, but slower than a call, less "
                  "explicit, and awkward when a transition must do something. State models "
                  "what each state does; a table models the transitions. Third, create state "
                  "objects when entered and discard them, or create them all once; fourth, "
                  "languages such as Self can change an object's delegation at run time and "
                  "so support the pattern directly."),
            ("p", "The Sample Code is a simplified C++ connection whose states, holding no "
                  "fields, are Singletons. Known Uses names Johnson and Zweig's account of "
                  "the pattern, and the tools of interactive drawing programs, HotDraw and "
                  "Unidraw among them, where the current tool decides what a click does. "
                  "Coplien's Envelope-Letter idiom, for swapping an object's class while "
                  "the program runs, is related. Related Patterns: Flyweight, on sharing states, and "
                  "Singleton."),
            ("p", "Now the lab, on a library copy of the lesson's own: five states, shelf, "
                  "on loan, held, overdue and lost, seven events and nine transitions. On the "
                  "preset <code>library-copy</code> the copy starts on the shelf and the lab "
                  "traces ten events to a final state of lost. Two are ignored, a return "
                  "while on the shelf and a renewal while overdue; no state is never "
                  "entered; and the largest state class is on loan, with three transitions. "
                  "One conditional over the state and event needs 14 branches, a branch for "
                  "each of the 9 transitions and a default for each of the 5 states; State "
                  "needs 7 classes, the 5 states, the context and the abstract state."),
            ("p", "The preset <code>library-repair</code> adds a repair state and two "
                  "events: a copy on the shelf or on loan can be damaged, and a fix returns "
                  "it to the shelf. The conditional grows to 18 branches, three new "
                  "transitions and a default for the new state, each a case added to code "
                  "that already worked. State grows to "
                  "8 classes, one of them new; the shelf and on-loan classes each gain a "
                  "transition, and the interface two default methods. On this short input "
                  "two states, overdue and lost, are never entered, and the largest class is "
                  "now on loan, with four. The figures compare sizes; whether 8 small "
                  "classes are clearer than one 18-branch method is the book's judgement "
                  "about many states, not something the count settles."),
            ("h3", "Exercise"),
            ("code", _lines(HANDSET_EXERCISE)),
            ("p", "A museum audio guide's handset. By hand, trace the input from the start "
                  "state and give the final state and the events ignored; then count the "
                  "branches one conditional needs and the classes State needs. Then enter "
                  "the machine into the lab to check."),
            ("p", "State varies what an object does with its state. The next lesson, "
                  "Strategy, varies how an object does one thing, by handing it an "
                  "algorithm."),
        ],
        "lab": ("gofkit", {
            "mode": "machine",
            "view": "states",
            "preset": "library-copy",
            "presets": [
                {"id": "library-copy",
                 "label": "A library copy over ten events",
                 "states": COPY_STATES,
                 "events": COPY_EVENTS,
                 "transitions": _records(COPY_TRANSITIONS),
                 "input": COPY_INPUT,
                 "expect": {"gsmFinal": "lost",
                            "gsmIgnored": "2: return at shelf (1), renew at overdue (5)",
                            "gsmDefined": "9",
                            "gsmBranches": "14",
                            "gsmClasses": "7",
                            "gsmLargest": "onloan, 3 transitions",
                            "gsmNever": "0: none"}},
                {"id": "library-repair",
                 "label": "The same copy with a repair state",
                 "states": REPAIR_STATES,
                 "events": REPAIR_EVENTS,
                 "transitions": _records(REPAIR_TRANSITIONS),
                 "input": REPAIR_INPUT,
                 "expect": {"gsmFinal": "shelf",
                            "gsmIgnored": "0: none",
                            "gsmDefined": "12",
                            "gsmBranches": "18",
                            "gsmClasses": "8",
                            "gsmLargest": "onloan, 4 transitions",
                            "gsmNever": "2: overdue, lost"}},
            ],
            "panel_title": "A trace, and two ways to write it",
        }),
        "steps_title": "Tracing a state machine and sizing it",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Write the states and transitions",
             "List the states, starting state first, the events, and for each state the "
             "events it responds to and the state each leads to."),
            ("Trace an input",
             "From the start state, take each event in turn: follow its transition if the "
             "current state has one, and otherwise note the event as ignored and stay put."),
            ("Count both designs",
             "One conditional: one branch per transition plus one default per state. "
             "State: one class per state, plus the context and the abstract state."),
            ("Do it on code of your own",
             "Find a class in code you know that tests a status field in more than one "
             "method. Write its states and transitions, count both figures, and say who "
             "decides each transition now."),
        ],
        "worked": {
            "title": "Ten events from the shelf",
            "intro": [
                "Trace <code>library-copy</code> from the shelf.",
            ],
            "lines": [
                "1 return at shelf: ignored",
                "2 lend: shelf to onloan; 3 renew: onloan",
                "4 due: overdue; 5 renew at overdue: ignored",
                "6 return: shelf; 7 hold: held",
                "8 lend: onloan; 9 due: overdue",
                "10 writeoff: lost",
                "branches: 9 + 5 = 14; classes: 5 + 2 = 7",
            ],
            "after": [
                "A renewal is a transition from on loan to itself: it counts as a branch "
                "and as part of the on-loan class, though the state does not change.",
            ],
        },
        "quiz_title": "Traces, transitions and tables",
        "quiz": [
            {"q": "In the exercise, what are the final state and the events ignored, and "
                  "how many branches and classes do the two designs need?",
             "a": ["ready; 2 ignored; 11 branches against 6 classes",
                   "docked; 2 ignored; 11 branches against 6 classes",
                   "ready; 1 ignored; 11 branches against 6 classes",
                   "ready; 2 ignored; 7 branches against 4 classes"],
             "c": 0,
             "why": "From docked: play is ignored, lift goes to ready, play to playing, "
                    "pause to paused, the second pause is ignored, play goes to playing, "
                    "dock to docked, and lift to ready. Seven transitions and four states "
                    "give 7 + 4 = 11 branches; State needs 4 + 2 = 6 classes. Docked is where "
                    "the input was one event before the end; 7 and 4 leave out the defaults, "
                    "the context and the abstract state."},
            {"q": "What drawback does the book give for letting the state classes choose "
                  "their successors?",
             "a": ["The context must be edited for every new state",
                   "Transitions are no longer atomic",
                   "Each state class knows at least one other, a dependency between them",
                   "State objects can no longer be shared"],
             "c": 2,
             "why": "Decentralizing the transitions makes the logic easy to extend with new "
                    "subclasses, and ties those subclasses to each other. The context is "
                    "edited less, not more; a transition is still one rebinding; and the "
                    "book's own sample shares states that choose their successors."},
            {"q": "In the book's comparison with Cargill's tables, what does the table-driven "
                  "approach focus on?",
             "a": ["What each state does",
                   "Sharing state objects among contexts",
                   "Swapping the class of a running object",
                   "Defining the transitions between states"],
             "c": 3,
             "why": "The book sums it up as State modelling state-specific behaviour and "
                    "the table defining transitions; tables are regular and edited as data, "
                    "but make it awkward to attach actions to a transition."},
            {"q": "On <code>library-copy</code>, where do the conditional's 14 branches "
                  "come from?",
             "a": ["7 events for each of the 5 states, less those never used",
                   "One for each of the 9 transitions and a default for each of the 5 "
                   "states",
                   "One for each of the 9 transitions and the 5 events not ignored",
                   "One for each event a state responds to, and nothing for the rest"],
             "c": 1,
             "why": "The lab's rule: a branch per defined transition plus a default per "
                    "state for the events it ignores, 9 + 5 = 14. Five states by seven "
                    "events would be 35 cases, most of them defaults that one default per "
                    "state already covers; the transitions alone are 9, with no default. "
                    "The input plays no part: the branches are a count of the code, so "
                    "which events a trace happens to ignore does not change them."},
        ],
        "mistakes": [
            ("Expecting State to make the code smaller",
             "The book says the opposite: the pattern spreads behaviour over more classes "
             "and is less compact than one class, and is worth it when there are many "
             "states. On the lesson's illustration one conditional needs 14 branches and "
             "State 7 classes; the gain the book claims is where a new state's code goes, "
             "which the repair preset shows."),
            ("Keeping state as flags and assignments",
             "Then a transition is only some variables changing, possibly several, with "
             "moments in between where the object is half in one state and half in "
             "another. A state object makes the transition one rebinding, and gives it a "
             "place in the code."),
            ("Assuming the context must decide every transition",
             "The pattern leaves it open. Fixed rules can live in the context; more often "
             "the states name their successors, which is easier to extend and couples the "
             "state classes to each other."),
        ],
        "standard": (
            "Finish when you can trace a state machine and size both ways of writing it.",
            "Given states, events, transitions and an input, give the final state and "
            "the ignored events, and count the branches and the classes each design "
            "needs."
        ),
        "note": (
            "The lab counts transitions and classes, not what a state does on each event; "
            "the book's main claim for the pattern, that each state's behaviour is in one "
            "place, is about the code's shape, which a count of branches only hints at."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 5, Strategy (PDF pp. 335-343 of the operator's copy): Intent and
    # Motivation pp. 335-336, Applicability p. 336, Participants, Collaborations
    # and Consequences pp. 337-339, Implementation pp. 339-340, Sample Code pp.
    # 340-342, Known Uses and Related Patterns pp. 342-343.
    # Quote: PDF p. 338 of the operator's copy, 14 words, quotes.py OK.
    # Lesson total: 14 words.
    {
        "slug": "strategy",
        "title": "Strategy",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "A family of algorithms, each in a class of its own behind one interface, so a client can be given whichever one it needs.",
        "summary": (
            "Strategy puts each algorithm of a family behind one interface, so the object "
            "that uses them can be configured with any. Read the pattern, then count the "
            "decision points of a print shop's code that tests the printing method in "
            "every operation, against the same prices as three printing strategies."
        ),
        "key": [
            "one interface, many algorithms",
            "the client picks; the context delegates",
            "composition instead of a subclass each",
            "take the data, or pass the context",
            "only when clients care which",
        ],
        "key_label": "Strategy in five lines",
        "concepts_intro": (
            "Three ideas from Strategy, the last of them what the lab counts."
        ),
        "concepts": [
            ("Strategy and context",
             "A strategy is an object that carries out one algorithm behind an interface "
             "every algorithm of the family shares. The context is the object that holds a "
             "strategy and calls it whenever it needs that algorithm done."),
            ("Taking the data to the strategy",
             "One way to connect the two: the context passes everything the algorithm "
             "might need as arguments. The other is to pass the context itself, and let "
             "the strategy ask for what it needs."),
            ("Decision points",
             "A count of the places code can go two ways: one, plus one for each if, "
             "while, for and case, and for each conditional and and or. Tests that ask "
             "which algorithm applies are the ones a Strategy moves."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Strategy, in Chapter 5, Behavioral Patterns, in your own copy first. "
            "The lesson reads it section by section and then counts the tests one "
            "listing makes."
        ),
        "body": [
            ("p", "&ldquo;Code containing many conditional statements often indicates the "
                  "need to apply the Strategy pattern.&rdquo; The sentence ends the third of "
                  "Strategy's Consequences, in Chapter 5, Behavioral Patterns. The intent, in "
                  "the lesson's words: make each algorithm of a family an object of its own, "
                  "all behind one interface, so they can be swapped, and the code that uses "
                  "an algorithm stays the same whichever is chosen. The book's other name "
                  "for it is Policy."),
            ("p", "The Motivation, summarised, is the case of breaking text into lines, for "
                  "which there are many algorithms. Writing them all into the class that "
                  "needs them makes it bigger, keeps algorithms you may not use, and makes a "
                  "new one hard to add. So the book's text-composition class holds a "
                  "compositor object, and three compositor subclasses implement a simple "
                  "line-at-a-time method, a paragraph-wide optimizing one and one that fills "
                  "each row with a fixed number of items. It is the same pair the case study "
                  "met in Formatting, in Chapter 2. In short, the Applicability "
                  "says: reach for it when there is more than one way to do a job, the "
                  "ways can be swapped, and you would rather not see the choice written "
                  "into conditionals or the ways' private data seen by their callers."),
            ("p", "The participants are three: the Strategy, the common interface; each "
                  "ConcreteStrategy, one algorithm; and the Context, which is configured with "
                  "a concrete strategy, keeps a reference to it and may give it access to its "
                  "own data. In the collaborations the context either passes the data the "
                  "algorithm needs or passes itself so the strategy can call back. Clients "
                  "usually create a concrete strategy and hand it to the context, and from "
                  "then on deal with the context only."),
            ("p", "Four of the Consequences are benefits. A hierarchy of strategies is a "
                  "family that inheritance can factor. Strategy is an alternative to "
                  "subclassing the context for each behaviour, which would fix the algorithm "
                  "into the context and rule out changing it at run time. It removes the "
                  "conditionals that pick a behaviour, as the opening quotation says. And it "
                  "lets a client choose among implementations with different trade-offs of "
                  "time and space."),
            ("p", "Three are liabilities, and the authors put them plainly. Clients must "
                  "know how the strategies differ to choose one, so the pattern belongs where "
                  "the variation matters to clients. All strategies share one interface, so "
                  "a context may prepare arguments a simple strategy never reads. And there "
                  "are more objects, which stateless strategies shared among contexts can "
                  "reduce, as Flyweight describes. The Implementation adds the choice between "
                  "taking the data to the strategy, which keeps the two decoupled, and "
                  "passing the context, which couples them more closely; strategies as C++ "
                  "template parameters when the choice is fixed at compile time; and "
                  "optional strategies, where a context with none falls back on default "
                  "behaviour."),
            ("p", "The Sample Code is the compositor example in C++, from InterViews, where "
                  "the simple compositor ignores some of what it is passed and the fixed-row "
                  "one ignores all of it. Known Uses ranges from ET++ and InterViews to a "
                  "compiler's register allocators, a financial framework's pricing "
                  "strategies, the Booch components' memory-allocation template arguments, "
                  "a circuit-layout router and the validators of Borland's ObjectWindows, an "
                  "example of the optional kind. Strategy's Related Patterns "
                  "name only Flyweight, since stateless strategies make good flyweights. "
                  "Two neighbours: Template Method varies part "
                  "of an algorithm by inheritance, where Strategy varies the whole of it by "
                  "delegation; and Domain-Driven Design's lesson Strategy and Composite in "
                  "the Model reads the same pattern as a policy the business names."),
            ("code", _lines(PRINT_BY_METHOD)),
            ("p", "Now the lab, on a print shop of the lesson's own, above. It quotes and "
                  "schedules a job by the printing method on its ticket, and both "
                  "operations test the method. On the preset <code>print-by-method</code> "
                  "the lab counts 8 decision points: one to start, three cases, three "
                  "ifs and one conditional and. The bands beside the count are "
                  "McConnell's guidance from Code Complete, not this book's; the deepest "
                  "nesting, 1, is first reached at line 4, inside the switch. Of the "
                  "eight, five ask which method applies: the three cases and the first test "
                  "of each <code>if</code> in <code>daysToPrint</code>."),
            ("code", _lines(PRINT_METHODS)),
            ("p", "The preset <code>print-methods</code> is the same prices and times as "
                  "printing strategies, above, and a job holds one, given at the counter: "
                  "<code>method.quoteCents(sheets, copies)</code>. The count falls to 3, one "
                  "to start and two ifs, each a rule inside one method: offset's price break "
                  "at 500 copies, risograph's slower run past 1,000. The five tests of which "
                  "method applies are gone from the listing, though nesting is now 2, from "
                  "line 7, since each test sits in a method in a class. The choice is made once, "
                  "where the job is given its method, in code the lab is not shown. That is "
                  "the first liability in a sentence: someone must know the strategies to "
                  "choose one."),
            ("h3", "Exercise"),
            ("code", _lines(QUIZ_POINTS)),
            ("p", "A quiz app scores an answer by the round's mode. Count its decision "
                  "points by the lab's rule. Then sketch classic, timed and streak scoring "
                  "strategies, keeping the test of whether the answer is correct in the "
                  "context, and count the context and the strategies together. Paste each "
                  "into the lab to check."),
            ("p", "Strategy varies a whole algorithm by giving an object another one. The "
                  "next lesson, Template Method, keeps the algorithm and lets subclasses "
                  "vary some of its steps."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "bands": [5, 10],
            "book": "other",
            "preset": "print-by-method",
            "presets": [
                {"id": "print-by-method",
                 "label": "A print shop testing the method in every operation",
                 "code": PRINT_BY_METHOD,
                 "expect": {"coDecisions": "8",
                            "coBreakdown": "1 + if 3 + case 3 + && 1",
                            "coBand": "6–10",
                            "coDepth": "1",
                            "coDeepest": "line 4"}},
                {"id": "print-methods",
                 "label": "The same prices and times as printing strategies",
                 "code": PRINT_METHODS,
                 "expect": {"coDecisions": "3",
                            "coBreakdown": "1 + if 2",
                            "coBand": "0–5",
                            "coDepth": "2",
                            "coDeepest": "line 7"}},
            ],
            "panel_title": "The tests a strategy moves",
            "panel_intro": (
                "The lab counts decision points by a stated rule: one, plus one for each "
                "if, while, for and case, and for each conditional and and conditional "
                "or. The bands beside the count are McConnell's, from Code Complete; the "
                "Gang of Four give no count. The listings are the lesson's."
            ),
        }),
        "steps_title": "Moving an algorithm into strategies",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Count the decisions",
             "Count one, plus one for each `if`, `while`, `for`, `case`, `&&` and `||`. "
             "An `else` or a `default` adds nothing."),
            ("Mark the tests on the algorithm",
             "For each decision, say whether it asks which algorithm applies or applies a "
             "rule within one. Tests of the first kind, repeated across operations, are "
             "what Strategy gathers."),
            ("Write one class per algorithm",
             "Give each algorithm a class implementing every operation that varied, check "
             "each case gives what it gave before, and name the one place where a strategy "
             "is chosen."),
            ("Do it on code of your own",
             "Find a method in code you know that switches on a mode, type or flag, "
             "count its decisions before and after strategies, and say whether its clients "
             "need to know which algorithm they get."),
        ],
        "worked": {
            "title": "Eight decisions, five of them on the method",
            "intro": [
                "Count the decision points in <code>print-by-method</code>.",
            ],
            "lines": [
                "start at 1",
                "line 4: case OFFSET: +1",
                "line 5: if on the copies: +1",
                "line 7: case RISO, line 9: case DIGITAL: +2",
                "line 16: if on the method: +1",
                "line 17: if on the method, and &&: +2",
                "1 + if 3 + case 3 + && 1 = 8",
                "after: 1 + if 2 = 3",
            ],
            "after": [
                "The two tests that survive, on lines 7 and 15 of the strategies, are "
                "rules of one method each; every test of which method applies has moved to "
                "where a job is given its method.",
            ],
        },
        "quiz_title": "Strategies, contexts and their costs",
        "quiz": [
            {"q": "In the exercise, how many decision points has the listing by the lab's "
                  "rule, and how many have the context and the three scoring strategies "
                  "together, with the correctness test kept in the context?",
             "a": ["5 before, 3 after",
                   "6 before, 3 after",
                   "6 before, 2 after",
                   "7 before, 3 after"],
             "c": 1,
             "why": "One, plus four ifs, plus the && on line 6: 1 + if 4 + && 1 = 6. "
                    "After, the context keeps `if (!a.correct())`, the timed strategy keeps "
                    "its test on the seconds, and classic and streak test nothing: 1 + if 2 "
                    "= 3. 5 forgets the &&; 2 drops the correctness test the exercise keeps "
                    "in the context."},
            {"q": "Why, in the book's Consequences, may a context prepare arguments that a "
                  "strategy never uses?",
             "a": ["The client chose the wrong strategy",
                   "Strategies keep state between calls",
                   "Every strategy shares one interface, whatever its algorithm needs",
                   "The context was subclassed for each algorithm"],
             "c": 2,
             "why": "That is the communication overhead: the interface must serve the "
                    "most demanding algorithm, so simple ones are passed what they ignore. "
                    "The book's remedy, if it matters, is tighter coupling between strategy "
                    "and context."},
            {"q": "How does the book's Template Method relate to Strategy?",
             "a": ["Template methods vary part of an algorithm by inheritance; strategies "
                   "vary the whole of it by delegation",
                   "Template methods vary the whole algorithm by delegation; strategies vary "
                   "part of it by inheritance",
                   "Both vary the whole algorithm, one at compile time and one at run time",
                   "Template Method is Strategy with one concrete strategy"],
             "c": 0,
             "why": "So the Related Patterns of Template Method put it. A template method "
                    "keeps the skeleton in a parent class and lets subclasses fill in steps; "
                    "a strategy is a separate object the context delegates the whole "
                    "algorithm to."},
            {"q": "In ObjectWindows, as Known Uses describes it, what makes a Validator an "
                  "optional strategy?",
             "a": ["Fields may choose among several validators at run time",
                   "A client attaches one only to the fields that need validating",
                   "A validator may skip some of the data it is given",
                   "Validators are shared among all the fields of a dialog"],
             "c": 1,
             "why": "A data-entry field delegates validation to a validator if it has one; "
                    "the client attaches one only where validation is needed, and a field "
                    "without one carries on as it would anyway. Optional strategies are the "
                    "third issue of the Implementation."},
        ],
        "mistakes": [
            ("Reaching for Strategy wherever an algorithm could vary",
             "The book attaches a condition: clients must understand how strategies "
             "differ to pick one, so the pattern belongs where the variation is relevant "
             "to them. An algorithm that never varies in practice gains an interface, "
             "several classes and a choice someone must make, and nothing else."),
            ("Reading the falling count as the whole story",
             "On the lesson's illustration the decisions fall from 8 to 3 because the "
             "method is no longer tested in each operation. It is still chosen once, "
             "where a job is given its method, in code the lab does not see; and the "
             "strategies are more objects, which the book counts as a cost."),
            ("Shaping the interface around the first algorithm",
             "The book stresses that the compositor's interface was designed to suit every "
             "layout algorithm, since changing it for each new strategy means changing "
             "every existing one. The Strategy and Context interfaces, it says, decide how "
             "well the pattern works."),
        ],
        "standard": (
            "Finish when you can say what a Strategy moves out of a class and what it "
            "costs.",
            "Count a listing's decisions before and after strategies, name where the "
            "choice of algorithm went, and give one liability the book names."
        ),
        "note": (
            "The lab counts decisions in the listing it is given. It does not see the "
            "code that picks a strategy, or the objects a strategy adds, and it cannot "
            "say whether the clients care which algorithm they get; the book makes that "
            "the condition for using the pattern at all."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 5, Template Method (PDF pp. 345-350 of the operator's copy):
    # Intent and Motivation pp. 345-346, Applicability p. 346, Participants,
    # Collaborations and Consequences pp. 347-348, Implementation pp. 348-349,
    # Sample Code p. 349, Known Uses and Related Patterns pp. 349-350.
    # Quotes: PDF p. 345 of the operator's copy, 14 words; PDF p. 347 (the
    # book quoting Sweet's phrase), 6 words; quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "template-method",
        "title": "Template Method",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "A parent class fixes the order of an algorithm's steps and lets subclasses write some of them.",
        "summary": (
            "Template Method writes an algorithm's skeleton once in a parent class and "
            "defers chosen steps to subclasses. Read the pattern, then count, for a map "
            "viewer's three kinds of tile, the steps each subclass writes, the one it "
            "forgot, and the step bodies the template saves."
        ),
        "key": [
            "the parent fixes the order of the steps",
            "primitives must be written; hooks may be",
            "the parent calls the subclass",
            "say which operations are hooks",
            "keep the primitives few",
        ],
        "key_label": "Template Method in five lines",
        "concepts_intro": (
            "Three ideas from Template Method, the second of them what the lab sorts the "
            "steps by."
        ),
        "concepts": [
            ("Template method",
             "An operation in a parent class that runs an algorithm's steps in a fixed "
             "order, some written in the parent and some left for subclasses. It is "
             "itself not meant to be overridden."),
            ("Primitive operation and hook",
             "A primitive operation is abstract: every concrete subclass must write it. A "
             "hook has a default in the parent, often doing nothing, and a subclass "
             "overrides it only to add something at that point."),
            ("Inverted control",
             "The parent class calls the subclass's operations, not the other way round. "
             "The subclass supplies pieces; it never decides when they run."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Template Method, in Chapter 5, Behavioral Patterns, in your own copy "
            "first; it is one of the shortest patterns. The lesson reads it section by "
            "section and then counts what three subclasses write."
        ),
        "body": [
            ("p", "&ldquo;Define the skeleton of an algorithm in an operation, deferring "
                  "some steps to subclasses.&rdquo; That is the first sentence of Template "
                  "Method's intent, in Chapter 5, Behavioral Patterns. The rest says the "
                  "point: subclasses may redefine some steps, and the algorithm's structure "
                  "stays as the parent wrote it. It is the one pattern of this course with "
                  "class scope, done with inheritance rather than with objects."),
            ("p", "The book's Motivation, summarised, is an application framework whose "
                  "abstract application class opens a document by a fixed series of steps: "
                  "check that the document can be opened, create the right kind of document "
                  "object, add it to the open documents and read it in. Subclasses for a "
                  "drawing program or a spreadsheet supply the check, the creation and the "
                  "reading; one more operation, called just before the document opens, lets "
                  "them react if they care to. The Applicability gives three uses: write the "
                  "invariant part of an algorithm once; factor behaviour that subclasses "
                  "duplicate into one place, which the book calls refactoring to generalize "
                  "after Opdyke and Johnson; and control how subclasses extend a class, by "
                  "allowing it only at hooks."),
            ("p", "The participants are two: the AbstractClass declares the primitive "
                  "operations and implements the template method that calls them, along with "
                  "its own operations and other objects'; each ConcreteClass implements the "
                  "primitives. The concrete class relies on the abstract one for the steps "
                  "that do not vary."),
            ("p", "The Consequences call template methods a fundamental technique for "
                  "reuse, the way class libraries factor out common behaviour. They invert "
                  "control, the book says, by what is sometimes called the Hollywood "
                  "principle, &ldquo;Don't call us, we'll call you&rdquo;, a phrase it credits "
                  "to Richard Sweet's 1985 paper on the Mesa environment: the parent calls the "
                  "subclass. A template method may call concrete operations, the abstract "
                  "class's own useful operations, primitive operations, factory methods and "
                  "hooks, and it must make clear which operations may be overridden and which "
                  "must be. Hooks also cure a common slip. A subclass that extends an "
                  "inherited operation by overriding it and calling the parent's version can "
                  "forget the call; if the parent instead calls an empty hook from the "
                  "operation, the subclass overrides the hook and cannot forget anything."),
            ("code", _lines(MAP_TILE_JAVA)),
            ("p", "The sketch is the lesson's own: a map viewer's tile, in Java. "
                  "<code>render</code> is <code>final</code>, so no subclass can reorder "
                  "the steps; <code>decode</code> and <code>style</code> are abstract, the "
                  "primitives; <code>label</code> and <code>shade</code> do nothing unless "
                  "overridden, the hooks; and the fixed steps are private. That is the "
                  "Implementation's first issue in Java's terms, where the book's is C++ "
                  "access control: protected primitives, pure virtual where they must be "
                  "overridden, and a template method that is not virtual. The second issue "
                  "is to keep the primitives few, since each is one more operation every "
                  "subclass writer must supply; the third, naming them so they stand out, as "
                  "MacApp prefixed its with Do."),
            ("p", "The Sample Code, from NeXT's AppKit and summarised, shows a parent class "
                  "enforcing an invariant: a view's display operation sets up the drawing "
                  "state, calls a hook that subclasses override to draw, and releases the "
                  "state afterwards, so no subclass can draw without the setup. Known Uses "
                  "says template methods are in nearly every abstract class, and points to "
                  "Wirfs-Brock and colleagues. Related Patterns: template methods often call "
                  "factory methods, as the document-opening example does; and Strategy, last "
                  "lesson, varies the whole algorithm by delegation where Template Method "
                  "varies part of it by inheritance."),
            ("p", "Now the lab, on the tile above. It has seven steps: three fixed, two "
                  "primitive, two hooks. Three subclasses override some: road tiles write "
                  "decode, style and the label hook; satellite tiles decode and style; "
                  "terrain tiles decode and the shading hook. On the preset "
                  "<code>map-tiles</code> the lab lists the sequence each subclass runs, "
                  "step by step, as the base's or its own, and gives the steps each writes, "
                  "3, 2 and 2, and the hooks each overrides, 1, 0 and 1. It flags one "
                  "subclass left abstract: terrain tiles lack style, so the Java would not "
                  "compile until that primitive is written."),
            ("p", "The same preset counts the step bodies. Written whole in each subclass "
                  "the algorithm would be 21, seven steps three times. With the template it "
                  "is 12: the 5 the base writes once, its fixed steps and its two hook "
                  "defaults, and the 7 overrides. The preset <code>map-tiles-fixed</code> "
                  "gives terrain tiles their style: no subclass is left abstract, and the "
                  "count with the template rises to 13, against 21. The gap is the "
                  "duplication the Applicability's second use removes; it is not a measure "
                  "of how well the steps were chosen, which is the Implementation's "
                  "question."),
            ("h3", "Exercise"),
            ("code", _lines(COFFEE_EXERCISE)),
            ("p", "A coffee bar's order, as a template of four steps and three subclasses. "
                  "By hand, name any subclass left abstract and the primitive it lacks, and "
                  "count the step bodies written whole in each subclass against those with "
                  "the template. Then enter it into the lab to check."),
            ("p", "Template Method lets subclasses fill in an algorithm's steps. The next "
                  "lesson, Visitor, the last pattern of the catalog, lets you add whole "
                  "operations to a structure without touching its classes."),
        ],
        "lab": ("gofkit", {
            "mode": "route",
            "view": "template",
            "preset": "map-tiles",
            "steps": _records(TILE_STEPS),
            "presets": [
                {"id": "map-tiles",
                 "label": "A map viewer's three kinds of tile, one primitive missing",
                 "subclasses": _records(TILE_SUBCLASSES),
                 "expect": {"grtSteps": "7: 3 fixed, 2 primitive, 2 hooks",
                            "grtOwn": "RoadTile 3, SatelliteTile 2, TerrainTile 2",
                            "grtAbstract": "1: TerrainTile (lacks style)",
                            "grtHooks": "RoadTile 1, SatelliteTile 0, TerrainTile 1",
                            "grtBase": "5",
                            "grtWhole": "21",
                            "grtWith": "12"}},
                {"id": "map-tiles-fixed",
                 "label": "The same tiles with terrain's style written",
                 "subclasses": _records(TILE_SUBCLASSES_FIXED),
                 "expect": {"grtOwn": "RoadTile 3, SatelliteTile 2, TerrainTile 3",
                            "grtAbstract": "0: none",
                            "grtWhole": "21",
                            "grtWith": "13"}},
            ],
            "panel_title": "What each subclass writes",
        }),
        "steps_title": "Reading a template and its subclasses",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("List the steps in order",
             "Write each step of the template method, and mark it fixed, primitive (must "
             "be written by every subclass) or hook (has a default)."),
            ("List each subclass's overrides",
             "For each subclass, write the steps it overrides. Any primitive missing from "
             "the list leaves that subclass abstract."),
            ("Count the step bodies",
             "Whole in each subclass: steps times subclasses. With the template: the fixed "
             "steps and the hook defaults once, plus every override."),
            ("Do it on code of your own",
             "Find an abstract class in code you know that calls methods its subclasses "
             "write. Sort them into primitives and hooks, count what each subclass "
             "writes, and say whether any hook is really a primitive in disguise."),
        ],
        "worked": {
            "title": "Twenty-one step bodies, or twelve",
            "intro": [
                "Count the step bodies on <code>map-tiles</code>.",
            ],
            "lines": [
                "steps: 3 fixed + 2 primitive + 2 hooks = 7",
                "whole: 7 × 3 subclasses = 21",
                "base: 3 fixed + 2 hook defaults = 5",
                "overrides: 3 + 2 + 2 = 7",
                "with the template: 5 + 7 = 12",
                "TerrainTile lacks style: abstract",
            ],
            "after": [
                "The primitives are not written in the base, so they appear only among the "
                "overrides; a subclass that skips one adds nothing to the count and leaves "
                "a hole the compiler finds.",
            ],
        },
        "quiz_title": "Skeletons, primitives and hooks",
        "quiz": [
            {"q": "In the exercise, which subclass is left abstract, and how many step "
                  "bodies are written whole in each subclass against with the template?",
             "a": ["Cortado; 12 against 7",
                   "Cortado; 12 against 4",
                   "None, since every subclass overrides something; 12 against 7",
                   "Cortado; 9 against 7"],
             "c": 0,
             "why": "Cortado overrides only the milk hook and lacks brew, the one "
                    "primitive. Whole: 4 steps × 3 subclasses = 12. With the template: 2 "
                    "fixed steps and 1 hook default in the base, plus the overrides 1 + 2 + "
                    "1 = 4, so 7. Four counts the overrides alone; 9 leaves the hook out of "
                    "the whole count."},
            {"q": "What does the book mean by the Hollywood principle in Template Method?",
             "a": ["A subclass overrides an operation and then calls the parent's version",
                   "Clients call the primitive operations directly",
                   "The parent class calls the subclass's operations, not the reverse",
                   "Subclasses may override the template method itself"],
             "c": 2,
             "why": "The inverted control: the subclass supplies operations and the parent "
                    "decides when they run. Overriding and calling the parent is the habit a "
                    "hook replaces, and nobody should override the template method "
                    "itself."},
            {"q": "What distinguishes a hook from a primitive operation?",
             "a": ["A hook must be overridden; a primitive may be",
                   "A hook has a default, often empty, and may be overridden; a primitive "
                   "must be",
                   "A hook is private to the parent; a primitive is public",
                   "A hook is called by clients; a primitive by the template method"],
             "c": 1,
             "why": "The book asks template methods to say which operations are hooks, "
                    "the ones a subclass may override, and which are abstract, the ones it must override. Both are "
                    "called by the template method, and both are meant for subclasses."},
            {"q": "Why does the book advise keeping primitive operations few?",
             "a": ["Each is one more operation every subclass writer must supply",
                   "Primitive operations cannot be protected in C++",
                   "A template method may call at most a few operations",
                   "Hooks are slower than primitives"],
             "c": 0,
             "why": "Minimizing primitives is the second implementation issue: the more "
                    "operations a subclass must override to complete the algorithm, the more "
                    "tedious it is to write one. Primitives can be protected, and nothing "
                    "limits how many operations a template method calls."},
        ],
        "mistakes": [
            ("Extending an inherited operation by overriding it and calling the parent",
             "It works until a subclass forgets the call. The book's alternative is a "
             "template method in the parent that calls an empty hook at the point of "
             "extension: the subclass overrides the hook, and the parent's part always "
             "runs."),
            ("Leaving unclear which operations may be overridden",
             "A subclass writer who cannot tell a hook from a primitive, or either from a "
             "step not meant to change, will override the wrong thing. The book asks "
             "template methods to make that explicit, and suggests naming conventions to "
             "help."),
            ("Making every step a primitive for flexibility",
             "Each primitive is a method every subclass must write. On the lesson's "
             "illustration one forgotten primitive leaves a subclass abstract; the book's "
             "advice is to keep primitives as few as the algorithm allows and use hooks "
             "where a default will do."),
        ],
        "standard": (
            "Finish when you can say what a template fixes and what its subclasses write.",
            "Given a template's steps and each subclass's overrides, name any subclass "
            "left abstract, and count the step bodies with and without the template."
        ),
        "note": (
            "The lab counts steps and overrides. It cannot say whether the steps were cut "
            "in the right places, whether a hook should have been a primitive, or whether "
            "a subclass's override keeps the parent's invariant; those are the "
            "Implementation's questions, and the reader's."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 5, Visitor (PDF pp. 351-364 of the operator's copy): Intent and
    # Motivation pp. 351-353, Applicability p. 353, Participants and
    # Collaborations pp. 354-355, Consequences pp. 355-357, Implementation
    # pp. 357-359, Sample Code pp. 359-364, Known Uses and Related Patterns
    # p. 364.
    # Quote: PDF p. 351 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "visitor",
        "title": "Visitor",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "An operation over a structure of objects packed into one class of its own, so new operations can be added without changing the objects' classes.",
        "summary": (
            "Visitor moves an operation out of the classes of a structure's elements into "
            "a visitor object the elements accept. Read the pattern, then count the accept "
            "and visit calls two visitors make over a playlist, and the classes a new "
            "operation and a new kind of element each change."
        ),
        "key": [
            "one visitor per operation",
            "accept calls the visit for its class",
            "two classes choose the method",
            "new operations are cheap",
            "new element classes are dear",
            "visitors may need what elements hide",
        ],
        "key_label": "Visitor in six lines",
        "concepts_intro": (
            "Three ideas from Visitor, the last of them the trade the lab counts."
        ),
        "concepts": [
            ("Visitor",
             "An object holding one operation over a structure, with a visit method for "
             "each class of element. The elements call it; the operation's code lives in "
             "the visitor instead of being spread over the element classes."),
            ("Double dispatch",
             "Choosing the code to run by the classes of two objects instead of one. An "
             "element's accept calls the visit method for its own class, on whichever "
             "visitor it was given, so the method run depends on both."),
            ("The two kinds of addition",
             "A new operation is one new visitor class and no edits. A new kind of element "
             "is one new element class, and a new visit method in the abstract visitor and "
             "in every visitor."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Visitor, in Chapter 5, Behavioral Patterns, in your own copy first; it is "
            "the longest of the five. The lesson reads it section by section and then "
            "counts calls and classes on one structure."
        ),
        "body": [
            ("p", "&ldquo;Visitor lets you define a new operation without changing the "
                  "classes of the elements on which it operates.&rdquo; That is the second "
                  "sentence of Visitor's intent, the last pattern in the catalog. The first "
                  "says what a visitor is: an operation to be carried out on the elements of "
                  "a structure, made into an object of its own."),
            ("p", "The book's Motivation, summarised, is a compiler holding "
                  "programs as syntax trees and needing many operations over them, type "
                  "checking, code generation, optimization, pretty-printing and more, each "
                  "treating assignments, variables and expressions differently. Put every "
                  "operation in every node class and the classes become a mixture that is "
                  "hard to follow and must all be recompiled for one new operation. So each "
                  "operation goes into a visitor, which is passed to the nodes; a node "
                  "accepts it by calling the visitor's operation for its own class, passing "
                  "itself. There are then two hierarchies, the elements and the visitors, and "
                  "a new operation is a new visitor subclass. The Applicability's "
                  "cases share one shape: a stable set of element classes, each with its "
                  "own interface, and a growing list of jobs over them that you would rather "
                  "not spread through every class."),
            ("p", "The participants: the Visitor declares one visit operation per concrete "
                  "element class, and the operation's name tells the visitor which class it "
                  "has; a ConcreteVisitor implements them all, and its fields often "
                  "accumulate the result as it goes; the Element declares accept; each "
                  "ConcreteElement implements it; and the ObjectStructure can enumerate its "
                  "elements, perhaps as a Composite or a plain collection. The client makes "
                  "a concrete visitor and has the structure visited; each element calls the "
                  "visit operation for its class and passes itself."),
            ("p", "The Consequences weigh both sides. Adding an operation is easy, a new "
                  "visitor, where spreading operations over the classes would mean editing "
                  "each. Related behaviour sits together in one visitor and unrelated "
                  "behaviour apart. But adding a ConcreteElement class is hard: every visitor "
                  "gains an operation, and a default in the abstract visitor helps only "
                  "sometimes. So the key question, the book says, is which you expect to "
                  "change more often, the operations or the element classes; if the classes, "
                  "keep the operations in them. Visitors can also visit objects with no "
                  "common parent class, which an iterator cannot, and can accumulate state "
                  "that would otherwise travel as arguments or globals. The last liability is "
                  "encapsulation: visitors need public access to what elements hold."),
            ("code", _lines(PLAYLIST_JAVA)),
            ("p", "The sketch is the lesson's own, a music playlist in Java. A folder "
                  "passes the visitor to its entries and then visits itself, so here the "
                  "structure does the traversing. That is the Implementation's second issue: "
                  "traversal can belong to the structure, to an iterator or to the visitor, "
                  "the last mainly for an irregular traversal that depends on the results, at "
                  "the cost of repeating it in each visitor. The first issue is the name of "
                  "the trick, double dispatch: the method that runs depends on both classes "
                  "involved, the element's and the visitor's, where C++ and Smalltalk choose "
                  "by the receiver alone. Languages with multiple dispatch, CLOS among them, "
                  "need the pattern less."),
            ("p", "The Sample Code returns to Composite's equipment, adding pricing and "
                  "inventory visitors in C++, and then redoes Interpreter's matcher in "
                  "Smalltalk with a visitor that traverses for itself. Known Uses names "
                  "Smalltalk-80's compiler and IRIS Inventor, whose actions are visitors "
                  "dispatched through a table of visitors by node classes; the name itself "
                  "was Mark Linton's, from the Fresco toolkit. Related Patterns: Composite, "
                  "whose structures visitors traverse, and Interpreter, which a visitor can "
                  "carry out."),
            ("p", "Now the lab, on a playlist of the lesson's own: a library folder holding "
                  "a morning folder, a running folder and a talk; eight entries of three "
                  "kinds, folders, tracks and episodes; and two visitors, one totalling the "
                  "minutes and one exporting the list. On the preset "
                  "<code>playlist-operation</code> the lab counts 16 accept calls, one per "
                  "entry per visitor, and as many visit calls, shown by kind in the table. "
                  "There are 4 element classes, the abstract element and three kinds, and 3 "
                  "visitor classes. With Visitor 9 methods are written, a visit per kind per "
                  "visitor and an accept per kind; with each operation a method of the "
                  "element classes, 6. A third operation is 1 new visitor and changes "
                  "nothing, against edits to the abstract element and all three element "
                  "classes."),
            ("p", "The preset <code>playlist-kind</code> makes the other addition, a new "
                  "kind of entry, say an audiobook chapter. With Visitor it is 1 new element "
                  "class and 3 changed classes, the abstract visitor and both visitors; "
                  "with operations on the elements it is 1 new class and nothing changed. "
                  "The two presets are the book's key consideration as counts. Which "
                  "addition your playlist will see more often is not in the counts."),
            ("h3", "Exercise"),
            ("code", _lines(MUSEUM_EXERCISE)),
            ("p", "A museum's floor plan, with three visitors. By hand, count the accept "
                  "calls, the methods written with Visitor against operations on the "
                  "elements, and the classes a new Shop kind changes under each. Then enter "
                  "it into the lab to check."),
            ("p", "That ends the catalog. The next lesson, Discussion of Behavioral "
                  "Patterns, reads the chapter's closing comparison of the eleven."),
        ],
        "lab": ("gofkit", {
            "mode": "tree",
            "view": "visit",
            "preset": "playlist-operation",
            "nodes": _records(PLAYLIST_NODES),
            "visitors": "duration export",
            "presets": [
                {"id": "playlist-operation",
                 "label": "A playlist with two visitors, adding an operation",
                 "adding": "operation",
                 "expect": {"gtrAccepts": "16: 8 nodes × 2 visitors",
                            "gtrVisits": "16",
                            "gtrElements": "1 + 3 = 4 (the abstract element; Folder, Track, Episode)",
                            "gtrVisitorClasses": "1 + 2 = 3 (the abstract visitor; duration, export)",
                            "gtrMethods": "3 × 2 + 3 = 9",
                            "gtrMethodsPlain": "3 × 2 = 6",
                            "gtrAddVisitor": "1 added (the new visitor), 0 changed",
                            "gtrAddPlain": "0 added, 4 changed (the abstract element and 3 element classes)"}},
                {"id": "playlist-kind",
                 "label": "The same playlist, adding a kind of entry",
                 "adding": "kind",
                 "expect": {"gtrAddVisitor": "1 added (the new element class), 3 changed (the abstract visitor and 2 visitors)",
                            "gtrAddPlain": "1 added (the new element class), 0 changed"}},
            ],
            "panel_title": "Calls, classes and the two additions",
        }),
        "steps_title": "Counting what a visitor costs and saves",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("List the structure and the operations",
             "Write each element with its parent and kind, and name the operations you "
             "would make visitors."),
            ("Count the calls",
             "One accept call per element per visitor, and each accept makes one visit "
             "call."),
            ("Count the classes each addition changes",
             "A new operation: one new visitor, nothing changed, against every element "
             "class and their parent edited. A new kind: one new class, and the abstract "
             "visitor and every visitor edited, against nothing changed."),
            ("Do it on code of your own",
             "Find a tree or a set of related classes in code you know with several "
             "operations over it. Count both additions, and say from its history which "
             "it has seen more of."),
        ],
        "worked": {
            "title": "Sixteen accepts, nine methods",
            "intro": [
                "Count <code>playlist-operation</code> by hand.",
            ],
            "lines": [
                "entries: 8; kinds: Folder, Track, Episode",
                "accepts: 8 × 2 visitors = 16; visits: 16",
                "element classes: 1 + 3 = 4",
                "visitor classes: 1 + 2 = 3",
                "with Visitor: 3 × 2 + 3 = 9 methods",
                "on the elements: 3 × 2 = 6 methods",
                "new operation: 1 added, 0 changed",
            ],
            "after": [
                "The three extra methods are the accepts, the price of double dispatch; "
                "in return the six visit methods sit in two visitors instead of across "
                "three element classes.",
            ],
        },
        "quiz_title": "Double dispatch and the two additions",
        "quiz": [
            {"q": "In the exercise, how many accept calls are made, how many methods are "
                  "written with Visitor against operations on the elements, and how many "
                  "existing classes does the new Shop kind change with Visitor?",
             "a": ["15 calls; 12 against 9 methods; 4 changed",
                   "15 calls; 12 against 9 methods; 3 changed",
                   "5 calls; 12 against 9 methods; 4 changed",
                   "15 calls; 9 against 9 methods; 4 changed"],
             "c": 0,
             "why": "Five nodes and three visitors give 5 × 3 = 15 accepts. Three kinds, "
                    "Wing, Exhibit and Screen: 3 × 3 visits + 3 accepts = 12 methods, against "
                    "3 × 3 = 9. The new kind changes the abstract visitor and the three "
                    "visitors, 4. Three forgets the abstract visitor; 5 is one call per node, "
                    "not per node per visitor."},
            {"q": "Under Visitor, what decides which method runs when an element accepts a "
                  "visitor?",
             "a": ["Only the element's class",
                   "Only the visitor's class",
                   "The order in which the structure is traversed",
                   "Both the element's class and the visitor's class"],
             "c": 3,
             "why": "That is double dispatch: accept is chosen by the element's class, and "
                    "it calls the visit method for that class on the visitor, which is "
                    "chosen by the visitor's class. Traversal order decides when, not "
                    "which."},
            {"q": "When does the book say it is likely wiser to put the operations "
                  "in the element classes?",
             "a": ["When new operations are added often",
                   "When the element classes change often",
                   "When the elements share no common parent class",
                   "When an operation must accumulate state"],
             "c": 1,
             "why": "Each new element class means a new operation in every visitor, so a "
                    "hierarchy that keeps growing makes visitors hard to maintain. Frequent "
                    "new operations, elements with no common parent and accumulated state "
                    "are all points in Visitor's favour."},
            {"q": "Why might the traversal be put in the visitor rather than in the "
                  "structure?",
             "a": ["To avoid repeating the traversal code",
                   "To make an internal iterator double-dispatch",
                   "For an irregular traversal that depends on the operation's results",
                   "Because a composite cannot traverse itself"],
             "c": 2,
             "why": "The book gives that as the main reason, with the cost that each "
                    "visitor repeats the traversal for each composite element. A composite "
                    "commonly does traverse itself, and an internal iterator does not "
                    "double-dispatch."},
        ],
        "mistakes": [
            ("Choosing Visitor where new kinds of element keep arriving",
             "Every new element class adds an operation to the abstract visitor and to "
             "every concrete one. On the lesson's illustration a new kind changes 3 "
             "classes with Visitor and none without; the book's test is which you expect "
             "to change more often, operations or element classes."),
            ("Expecting the elements to stay fully encapsulated",
             "A visitor does its work from outside the element, so the element's interface "
             "must be rich enough for it, which often means public operations exposing "
             "state the element would otherwise keep to itself. The book lists this among "
             "the liabilities."),
            ("Taking Visitor for an iterator",
             "An iterator visits elements one after another and calls their operations, "
             "and its elements must share a parent type. A visitor carries an operation to "
             "the elements, chooses its code by their class, and can visit classes with no "
             "common parent; who traverses is a separate choice."),
        ],
        "standard": (
            "Finish when you can say what a visitor makes easy and what it makes hard.",
            "Given a structure and its operations, count the accept and visit calls and "
            "the methods written, and the classes each kind of addition changes with and "
            "without Visitor."
        ),
        "note": (
            "The lab counts calls and classes. It cannot say which kind of addition your "
            "structure will see, which is the book's whole test, or how much of an "
            "element's state a visitor will need opened up."
        ),
    },
]
