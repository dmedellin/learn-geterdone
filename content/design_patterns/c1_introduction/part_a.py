"""What Design Patterns Are, lessons 1-5 -- Chapter 1, Introduction.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 1: 1.1 What Is a
Design Pattern?, 1.2 Design Patterns in Smalltalk MVC, 1.3 Describing Design
Patterns, 1.4 The Catalog of Design Patterns, 1.5 Organizing the Catalog, and
1.6 How Design Patterns Solve Design Problems, read in three lessons. Lesson 6,
on 1.7 and 1.8, is in part_b.py. Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter, section and pattern. Every
quotation is copied from that copy and checked with quotes.py. The designs,
records and Java sketches are written for these lessons: none of the book's
code, diagrams, tables or example data is reproduced, and no lab uses the
book's example domains. The design is docs/design-patterns/PLAN.md, section C,
Course 1.
"""


def _lines(text):
    """A snippet or record constant as a code block's list of lines."""
    return text.split("\n")


def _records(text):
    """Records written one to a line, as the single string a lab field takes."""
    return " ".join(line.strip() for line in text.split("\n") if line.strip())


# ---------------------------------------------------------------- 1.1 design

# A bike-share dock as the model, with three views of it: the screen at the
# dock, the city map in the rider's app, and the operator's ledger. A swap is a
# rider returning one bike and taking another, so it changes the dock twice.
DOCK_VIEWS = """kiosk, dock;
map, dock;
ledger, dock"""

DOCK_FOUR_VIEWS = DOCK_VIEWS + """;
alerts, dock"""

DOCK_OPERATIONS = """rent, dock;
dropoff, dock;
swap, dock, dock;
repair, dock"""

DOCK_JAVA = """// The dock knows its views only as DockView; it names no screen.
interface DockView {
    void update(Dock dock);
}

final class Dock {
    private final List<DockView> views = new ArrayList<>();
    private int bikes;

    void attach(DockView view) { views.add(view); }
    void rent()    { bikes--; changed(); }
    void dropoff() { bikes++; changed(); }
    int bikes()    { return bikes; }

    private void changed() {
        for (DockView view : views) {
            view.update(this);   // one update per view, per change
        }
    }
}"""

QUIZ_BOARD_EXERCISE = """subjects:   board
observers:  podium, board; table, board; host, board; phone, board
operations: q1, board; q2, board; bonus, board, board, board; reset, board"""


# ---------------------------------------------------------------- 1.2 catalog

# Eight of the catalog's twenty-three patterns, each with the purpose and scope
# the lesson's prose gives it (1.5). Not the book's table: a selection, as
# records the reader can check against the prose.
EIGHT_PATTERNS = """factory-method, purpose=creational, scope=class;
abstract-factory, purpose=creational, scope=object;
singleton, purpose=creational, scope=object;
composite, purpose=structural, scope=object;
decorator, purpose=structural, scope=object;
template-method, purpose=behavioral, scope=class;
observer, purpose=behavioral, scope=object;
strategy, purpose=behavioral, scope=object"""

TEMPLATE_HEADINGS = """Pattern Name and Classification
Intent
Also Known As
Motivation
Applicability
Structure
Participants
Collaborations
Consequences
Implementation
Sample Code
Known Uses
Related Patterns"""

FOUR_MORE_EXERCISE = """builder, purpose=creational, scope=object;
bridge, purpose=structural, scope=object;
interpreter, purpose=behavioral, scope=class;
iterator, purpose=behavioral, scope=object
specification: scope = class or purpose = structural"""


# ---------------------------------------------------------------- 1.3 design

# A parcel locker tells a customer a parcel has arrived, by text, e-mail or a
# push message. Written user, used.
LOCKER_CONCRETE = """LockerApp, SmsSender;
LockerApp, EmailSender;
LockerApp, PushSender"""

LOCKER_INTERFACE = """LockerApp, Notifier;
SmsSender, Notifier;
EmailSender, Notifier;
PushSender, Notifier"""

LOCKER_CONCRETE_POST = LOCKER_CONCRETE + """;
LockerApp, PostSender"""

LOCKER_INTERFACE_POST = LOCKER_INTERFACE + """;
PostSender, Notifier"""

LOCKER_CONCRETE_JAVA = """// The locker names every sender it might use.
final class LockerApp {
    private final SmsSender sms = new SmsSender();
    private final EmailSender email = new EmailSender();
    private final PushSender push = new PushSender();

    void parcelArrived(Customer c, String box) {
        String text = "Your parcel is in box " + box;
        if (c.prefers() == Channel.SMS) {
            sms.text(c.phone(), text);
        } else if (c.prefers() == Channel.EMAIL) {
            email.mail(c.address(), "Parcel", text);
        } else {
            push.send(c.deviceId(), text);
        }
    }
}"""

LOCKER_INTERFACE_JAVA = """// The locker commits only to a type: anything that can send a notice.
interface Notifier {
    void send(Customer c, String text);
}

final class LockerApp {
    private final Notifier notifier;

    LockerApp(Notifier notifier) {   // the caller chooses the class
        this.notifier = notifier;
    }

    void parcelArrived(Customer c, String box) {
        notifier.send(c, "Your parcel is in box " + box);
    }
}"""

TILE_VIEWER_EXERCISE = """// before: user, used
TileView, OsmSource; TileView, SatelliteSource;
TileView, CacheSource; TileView, CanvasRenderer
// after: the three sources behind one interface
TileView, TileSource; TileView, CanvasRenderer;
OsmSource, TileSource; SatelliteSource, TileSource;
CacheSource, TileSource"""


# ---------------------------------------------------------------- 1.4 design

# A music player varies in where its tracks come from and in the order it plays
# them; the second preset adds the output it plays to.
PLAYER_TWO = """source, local, stream, radio, podcast;
order, inorder, shuffle, repeat"""

PLAYER_THREE = PLAYER_TWO + """;
output, speaker, headphones"""

PLAYER_JAVA = """// A player is composed of a source and an order, each behind an interface.
final class Player {
    private final TrackSource source;
    private PlayOrder order;

    Player(TrackSource source, PlayOrder order) {
        this.source = source;
        this.order = order;
    }

    void setOrder(PlayOrder order) {   // changed while the player runs
        this.order = order;
    }

    Track next() {
        return order.next(source.tracks());   // delegated, not inherited
    }
}"""

IRRIGATION_EXERCISE = """trigger, timer, moisture, weather;
zone, lawn, beds, pots;
valve, solenoid, drip"""


# ---------------------------------------------------------------- 1.5 design

# A garden irrigation controller that reads a commercial weather service. In
# the first design four classes call the service's web interface themselves;
# in the second one class, behind an interface of the controller's own, does.
GARDEN_ELEMENTS = """Scheduler, scheduling;
RainDelay, scheduling;
FrostAlert, alerts;
WeeklyReport, reports;
ValveDriver, hardware"""

GARDEN_CHANGES_SPREAD = """new-provider, Scheduler;
new-provider, RainDelay;
new-provider, FrostAlert;
new-provider, WeeklyReport;
hourly-forecast, Scheduler;
hourly-forecast, RainDelay;
hourly-forecast, FrostAlert;
frost-threshold, FrostAlert;
new-valve, ValveDriver"""

GARDEN_ELEMENTS_ENCAPSULATED = GARDEN_ELEMENTS + """;
WeatherSource, weather;
HttpWeather, weather"""

GARDEN_CHANGES_ENCAPSULATED = """new-provider, HttpWeather;
hourly-forecast, WeatherSource;
hourly-forecast, HttpWeather;
hourly-forecast, Scheduler;
hourly-forecast, RainDelay;
hourly-forecast, FrostAlert;
frost-threshold, FrostAlert;
new-valve, ValveDriver"""

WEATHER_JAVA = """// The controller's own word for what it needs from any weather service.
interface WeatherSource {
    Forecast tomorrow(Location where);
}

// The one class that knows the vendor's web interface and its units.
final class HttpWeather implements WeatherSource {
    private final HttpClient client;
    private final String apiKey;

    HttpWeather(HttpClient client, String apiKey) {
        this.client = client;
        this.apiKey = apiKey;
    }

    public Forecast tomorrow(Location where) {
        VendorReply reply = client.get(where, apiKey);
        return new Forecast(reply.rainMm(), reply.lowCelsius());
    }
}"""

FRAMEWORK_JAVA = """// A framework owns the main loop; the application supplies the hooks.
abstract class GardenJob {
    final void runAt(Instant now) {   // written once, in the framework
        if (shouldRun(now)) {
            work(now);
            log(now);
        }
    }
    protected abstract boolean shouldRun(Instant now);
    protected abstract void work(Instant now);
    private void log(Instant now) { /* the framework's record */ }
}"""

VENDING_EXERCISE = """// before: change, class (module in brackets)
card-payments: Keypad [ui], Display [ui], CoinBox [payment]
new-coin:      CoinBox [payment], Display [ui]
restock-alert: Stock [inventory]
// after: payment behind a Payment interface, CardReader added
card-payments: CardReader [payment], Display [ui]
new-coin:      CoinBox [payment]
restock-alert: Stock [inventory]"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 1 opening (PDF pp. 21-22 of the operator's copy), 1.1 What Is a
    # Design Pattern? (pp. 22-24), 1.2 Design Patterns in Smalltalk MVC
    # (pp. 24-26).
    # Quote: PDF p. 23 of the operator's copy, 25 words, quotes.py OK; the
    # word "Inheritance" as a would-be pattern name, PDF p. 24, 1 word, OK.
    # Lesson total: 26 words.
    {
        "slug": "what-is-a-design-pattern",
        "title": "What Is a Design Pattern?",
        "module": "Chapter 1 · Introduction",
        "one_line": "A named, recurring arrangement of classes and objects that solves a general design problem in a context, together with what it costs.",
        "summary": (
            "The opening of Chapter 1 asks what experienced object-oriented designers "
            "know that newcomers do not, and answers with patterns. Read the authors' "
            "definition, the four elements every pattern has, and their reading of "
            "Smalltalk's Model/View/Controller as three patterns at once; then count the "
            "updates one model sends to its views as it changes."
        ),
        "key": [
            "experts reuse solutions that worked",
            "name, problem, solution, consequences",
            "classes and objects, not walls and doors",
            "MVC: Observer, Composite and Strategy",
            "one update per view for each change",
            "adding a view leaves the model unchanged",
        ],
        "key_label": "Design patterns in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's own; the "
            "third is the Smalltalk design the authors read as an example."
        ),
        "concepts": [
            ("Design pattern",
             "A description of communicating classes and objects, tailored to a design "
             "problem that recurs, in the setting where it arises. It names the arrangement, says "
             "which classes and instances take part and what each is responsible for, "
             "and says when it applies and what it costs. It is smaller than an "
             "application's architecture and larger than a reusable class such as a "
             "list."),
            ("The four essential elements",
             "A name, which gives designers a word for the whole idea; the problem, "
             "which says when the pattern applies; the solution, an abstract "
             "arrangement of elements and their collaborations rather than one concrete "
             "design; and the consequences, the trade-offs of applying it, often of "
             "space, time, flexibility or portability."),
            ("Model/View/Controller",
             "The Smalltalk-80 way of building user interfaces from three kinds of "
             "object: the model holds the application's data, a view presents it, and "
             "a controller decides how the interface responds to input. The authors "
             "find Observer, Composite and Strategy inside it."),
        ],
        "read_title": "The authors' question first, then the definition, then the count",
        "read_intro": (
            "Read the opening of Chapter 1 and Sections 1.1 and 1.2 in your own copy "
            "first. The lesson reads them as an argument about what a pattern is, then "
            "counts one consequence of the first pattern MVC contains."
        ),
        "body": [
            ("p", "&ldquo;A design pattern names, abstracts, and identifies the key "
                  "aspects of a common design structure that make it useful for creating "
                  "a reusable object-oriented design.&rdquo; Gamma, Helm, Johnson and "
                  "Vlissides write that in Section 1.1 of <em>Design Patterns</em>, the "
                  "1995 book often called the Gang of Four's after its four authors. This "
                  "lesson reads the opening of Chapter 1, Introduction, and Sections 1.1, "
                  "What Is a Design Pattern?, and 1.2, Design Patterns in Smalltalk MVC. "
                  "Read them in your own copy first."),
            ("p", "The chapter starts from a puzzle. Reusable object-oriented design is "
                  "hard, and experienced designers say they rarely get it right at the "
                  "first attempt; yet they do produce good designs, while newcomers, "
                  "faced with too many options, fall back on habits from other kinds of "
                  "programming. The authors' answer is that experts do not start every "
                  "problem from nothing. They reuse arrangements that worked before, so the "
                  "same shapes of classes and communicating objects turn up in system "
                  "after system. The book's aim is to write those shapes down, each "
                  "named, explained and evaluated, so a designer can apply one without "
                  "discovering it again. None is new, the authors stress: every design in "
                  "the catalog had been used more than once in different systems, and "
                  "most had lived only in folklore or inside successful programs."),
            ("p", "They borrow the idea from the architect Christopher Alexander, whose "
                  "patterns describe a problem that keeps recurring and the core of a "
                  "solution that can serve countless times, each building of it "
                  "different from the last. Alexander meant buildings and towns; the authors keep "
                  "the shape of his definition and change the material, from walls and "
                  "doors to objects and interfaces. In both, the pattern pairs a recurring "
                  "problem, in its setting, with the heart of its answer. They also fix the level they mean. A linked list "
                  "or a hash table, coded once as a class and reused as it stands, is too "
                  "small to be a design pattern; the design of a whole application for one "
                  "domain is too large. The patterns of the book sit between."),
            ("p", "Every pattern, the section says, has four essential elements. The "
                  "<strong>name</strong> is a handle: a word or two that lets designers "
                  "talk, write and think about a design at a higher level, and finding good "
                  "ones was, the authors admit, among the hardest parts of the work. The "
                  "<strong>problem</strong> says when to apply the pattern, sometimes with "
                  "conditions that must hold first. The <strong>solution</strong> gives the "
                  "elements, their relationships, responsibilities and collaborations, as "
                  "an abstract arrangement, a template that fits many situations, not a "
                  "particular implementation. The <strong>consequences</strong> are the "
                  "results and trade-offs, which designers often leave unspoken and which "
                  "the authors insist are what you need to choose between designs. Every "
                  "lesson after this one is built around those four."),
            ("p", "The section ends on the choice of language. The patterns assume what "
                  "Smalltalk and C++ offered in the early 1990s, and the authors note that "
                  "this choice shapes the catalog: in a procedural language, "
                  "&ldquo;Inheritance&rdquo; might have been a pattern, and a language "
                  "with multi-methods needs Visitor less. The book's own sample code is "
                  "C++ and, sometimes, Smalltalk. The sketches in these lessons are Java "
                  "8, written for each lesson, never more than twenty lines; Java did not "
                  "exist when the book was written, and where its features change a "
                  "pattern's cost the lesson says so."),
            ("p", "Section 1.2 shows what the authors mean by reading a familiar design. "
                  "In Smalltalk-80's Model/View/Controller, a model holds the data, each "
                  "view presents it, and the model and its views are joined by a "
                  "subscribe and notify protocol: whenever the model's data changes, it "
                  "tells the views that depend on it, and each updates itself. The book's "
                  "illustration is one set of figures shown three ways at once. Read "
                  "narrowly, that is a way to separate views from models. Read generally, "
                  "it is a way to let a change to one object reach any number of others "
                  "without the changed object knowing what they are, and that general "
                  "design is the pattern Observer."),
            ("p", "The same section finds two more. Views can nest, a panel of buttons "
                  "being a view made of views, and a composite view is used wherever a "
                  "single view would be: treating a group like one of its members is "
                  "Composite. And a view hands its response to input to a controller "
                  "object, which can be replaced, even while the program runs, to change "
                  "how the view reacts without changing how it looks: an object standing "
                  "for an algorithm is Strategy. MVC uses others in passing, Factory Method "
                  "for a view's default controller and Decorator for scrolling, but the "
                  "authors name those three as its main relationships."),
            ("code", _lines(DOCK_JAVA)),
            ("p", "That sketch is the subscribe and notify protocol on a design of this "
                  "lesson's own: a bike-share dock as the model, with three views, the "
                  "screen at the dock, the city map in a rider's app, and the operator's "
                  "ledger. The dock calls <code>update</code> on every attached view each "
                  "time its count of bikes changes. On the preset <code>three-views</code> "
                  "four operations run, a rental, a drop-off, a swap and a repair, and the "
                  "swap changes the dock twice, so the lab counts 5 changes and 15 updates "
                  "sent: each of kiosk, map and ledger receives 5. Observers never "
                  "notified and subjects no one observes both read <code>0: none</code>, "
                  "since every view watches the dock."),
            ("p", "Two tiles look ahead to the Observer lesson in Behavioral Patterns II. "
                  "Under the other scheme, a change manager that collects an operation's "
                  "changes and sends each view one update for the whole operation, the "
                  "lab counts 12 updates, and the tile for redundant updates reads 3: the "
                  "swap's second round. The preset <code>fourth-view</code> attaches an "
                  "alerts view and changes nothing else. Updates rise to 20 and the "
                  "change manager's figure to 16, and the class <code>Dock</code> is not "
                  "edited at all. That is the claim of Section 1.2 in a number: new views "
                  "can be made for a model without rewriting it, and what each new view "
                  "costs is one more update for every change."),
            ("h3", "Exercise"),
            ("code", _lines(QUIZ_BOARD_EXERCISE)),
            ("p", "A quiz app's scoreboard as the model, with four views: the podium "
                  "screen, the league table, the host's console and each player's phone. "
                  "By hand, count the changes, the updates sent directly, and the updates "
                  "a change manager would send, one per view per operation. Then type the "
                  "records into the lab to check, and say which operation the redundant "
                  "updates come from."),
            ("p", "A pattern is written down in a fixed form, and the catalog is "
                  "organised in a way the rest of the book relies on. The next lesson, "
                  "Describing and Organizing the Catalog, reads Sections 1.3 to 1.5."),
        ],
        "lab": ("gofkit", {
            "mode": "notify",
            "view": "observer",
            "subjects": "dock",
            "operations": _records(DOCK_OPERATIONS),
            "preset": "three-views",
            "presets": [
                {"id": "three-views",
                 "label": "A bike-share dock with three views: kiosk, map, ledger",
                 "observers": _records(DOCK_VIEWS),
                 "expect": {"gnoChanges": "5", "gnoSent": "15",
                            "gnoOther": "managed: 12", "gnoRedundant": "3",
                            "gnoPer": "kiosk 5, map 5, ledger 5",
                            "gnoNever": "0: none", "gnoUnobserved": "0: none"}},
                {"id": "fourth-view",
                 "label": "The same dock with a fourth view attached: alerts",
                 "observers": _records(DOCK_FOUR_VIEWS),
                 "expect": {"gnoChanges": "5", "gnoSent": "20",
                            "gnoOther": "managed: 16", "gnoRedundant": "4",
                            "gnoPer": "kiosk 5, map 5, ledger 5, alerts 5"}},
            ],
            "panel_title": "The updates one model sends to its views",
        }),
        "steps_title": "Reading a design as a pattern",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the objects and their roles",
             "List the objects in the design and say what each is for: which one holds "
             "the data, which ones present or react to it."),
            ("Find the general problem",
             "For each relationship, ask what more general problem it solves once the "
             "particular objects are forgotten: one change reaching many, a group "
             "standing in for a member, an algorithm that can be swapped."),
            ("Count what the arrangement does",
             "For the Observer relationship, count the changes each operation makes and "
             "multiply by the observers of what changed. That is the number of updates "
             "sent."),
            ("Do it on a design of your own",
             "Pick a screen or report in a program you know that shows data kept "
             "elsewhere. Name its model and its views, count the updates one ordinary "
             "operation causes, and say what you would have to edit to add one more "
             "view."),
        ],
        "worked": {
            "title": "Updates from the dock",
            "intro": [
                "Count the updates on the preset <code>three-views</code>.",
            ],
            "lines": [
                "rent, dropoff and repair change the dock once",
                "the swap changes the dock twice",
                "dock changes in all: 5",
                "views of the dock: kiosk, map and ledger",
                "direct: 5 changes × 3 views gives 15 updates",
                "managed: 4 operations × 3 views gives 12",
                "the 3 saved are the second round of the swap",
            ],
            "after": [
                "Each view hears about every change, and the dock never learns what the "
                "views do with it. Attaching a fourth view adds 5 updates and no line to "
                "the dock.",
            ],
        },
        "quiz_title": "Patterns, their elements and MVC",
        "quiz": [
            {"q": "In the exercise, how many updates does the scoreboard send directly, "
                  "and how many would a change manager send?",
             "a": ["24 directly; 16 with a change manager",
                   "16 directly; 24 with a change manager",
                   "24 directly; 6 with a change manager",
                   "6 directly; 4 with a change manager"],
             "c": 0,
             "why": "The operations change the board 1 + 1 + 3 + 1 = 6 times, and four "
                    "views watch it, so 6 × 4 = 24 updates go out directly. A change "
                    "manager sends one update per view per operation: 4 × 4 = 16. The "
                    "8 redundant updates are the bonus round's second and third changes. "
                    "6 and 4 are the counts of changes and operations, not of updates."},
            {"q": "On the preset <code>three-views</code>, how many updates does the swap "
                  "alone send directly?",
             "a": ["2", "3", "6", "15"],
             "c": 2,
             "why": "The swap changes the dock twice, and each change reaches all three "
                    "views: 2 × 3 = 6. Three is what one change sends, 2 is the number of "
                    "changes, and 15 is the total for all four operations."},
            {"q": "Which pattern do the authors find in the relationship between a view "
                  "and its controller?",
             "a": ["Observer", "Composite", "Strategy", "Decorator"],
             "c": 2,
             "why": "A view delegates its response to input to a controller object that "
                    "can be replaced, which is Strategy. Observer is the model and its "
                    "views; Composite is views nested in views; Decorator is what MVC "
                    "uses to add scrolling to a view."},
            {"q": "Which of these is not one of the four essential elements of a pattern "
                  "in Section 1.1?",
             "a": ["The pattern name", "The problem", "The consequences",
                   "The sample code"],
             "c": 3,
             "why": "The four elements are the name, the problem, the solution and the "
                    "consequences. Sample code is one section of the template the "
                    "catalog uses to describe each pattern, read in the next lesson; the "
                    "solution itself is abstract, not a particular implementation."},
        ],
        "mistakes": [
            ("Taking a pattern for a class you can reuse as it stands",
             "The authors set the level explicitly: a linked list or a hash table, coded "
             "once and reused as is, is not what they mean by a design pattern. A "
             "pattern's solution is an abstract arrangement of roles that has to be "
             "implemented again in each design, with names of that design's own; on the "
             "lesson's illustration, <code>Dock</code> and <code>DockView</code> are "
             "Observer, but no library class called Observer appears."),
            ("Reading MVC as a single pattern",
             "Section 1.2 finds at least three in it: Observer between the model and its "
             "views, Composite in nested views, and Strategy between a view and its "
             "controller, with Factory Method and Decorator in smaller roles. The point "
             "of the section is that a familiar design is several patterns working "
             "together."),
            ("Treating the consequences as an optional extra",
             "The consequences are one of the four essential elements. The authors call "
             "them critical for weighing one design against another and note that they "
             "are often left unsaid; a pattern described without its costs is missing "
             "the part you need to decide whether to use it."),
        ],
        "standard": (
            "Finish when you can name a pattern's four elements and count an Observer's updates.",
            "Given a model, its views and a list of operations, state the changes and "
            "the updates sent, say which patterns the authors find in MVC and where, and "
            "give the four elements every pattern in the catalog has."
        ),
        "note": (
            "The lab counts updates on the dock the lesson states. It cannot say whether "
            "a design needs Observer at all, or whether its views would be better off "
            "asking the model when they need to; the authors leave that to each "
            "pattern's consequences, weighed against what in the design is expected to "
            "change."
        ),
    },
    # ---------------------------------------------------------------- 02
    # 1.3 Describing Design Patterns (PDF pp. 26-28 of the operator's copy), 1.4
    # The Catalog of Design Patterns (pp. 28-29), 1.5 Organizing the Catalog
    # (pp. 29-31; Table 1.1 p. 30, Figure 1.1 p. 32).
    # Quote: PDF p. 26 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "describing-and-organizing-the-catalog",
        "title": "Describing and Organizing the Catalog",
        "module": "Chapter 1 · Introduction",
        "one_line": "Every pattern in the catalog is written in the same thirteen sections, and classified by what it does and whether it works on classes or on objects.",
        "summary": (
            "Sections 1.3 to 1.5 set out the template every pattern in the catalog "
            "follows, list the twenty-three patterns with their intents, and classify "
            "them by purpose and scope. Read what each section of the template is for, "
            "then give eight patterns their purpose and scope and let a specification "
            "select from them."
        ),
        "key": [
            "every pattern in thirteen sections",
            "intent: what it does and why",
            "purpose: creational, structural, behavioral",
            "scope: class or object",
            "class relations are fixed at compile time",
            "some go together; some are alternatives",
        ],
        "key_label": "The catalog in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, all the authors': the template from Section "
            "1.3 and the two criteria from Section 1.5."
        ),
        "concepts": [
            ("The template",
             "The fixed sequence of sections in which every pattern of the catalog is "
             "written, from its name and intent through its motivation, applicability, "
             "structure, participants, collaborations, consequences and implementation "
             "to sample code, known uses and related patterns. The uniform order makes "
             "patterns easier to compare and to look things up in."),
            ("Purpose",
             "What a pattern does. A creational pattern concerns how objects are made; "
             "a structural one, how classes or objects are put together; a behavioral "
             "one, how classes or objects interact and share out responsibility."),
            ("Scope",
             "Whether a pattern is mainly about classes or about objects. Class patterns "
             "work through inheritance, so their relationships are fixed when the "
             "program is compiled; object patterns work through references between "
             "objects, which can change while it runs. Most patterns have object scope."),
        ],
        "read_title": "The template, the catalog, then a selection by purpose and scope",
        "read_intro": (
            "Read Sections 1.3, 1.4 and 1.5 in your own copy first. The lesson reads the "
            "template as a reader's guide to every later chapter, and the classification "
            "as a tool, which the lab uses to select."
        ),
        "body": [
            ("p", "&ldquo;The template lends a uniform structure to the information, making "
                  "design patterns easier to learn, compare, and use.&rdquo; That is the "
                  "authors' reason, in Section 1.3, Describing Design Patterns, for "
                  "writing all twenty-three patterns the same way. This lesson reads 1.3, "
                  "1.4, The Catalog of Design Patterns, and 1.5, Organizing the Catalog. "
                  "Read them in your own copy first."),
            ("p", "A diagram, Section 1.3 argues, is not enough to describe a pattern. It "
                  "shows the classes and objects a design ended with, but not the "
                  "choices made on the way, the options turned down and what each cost, and those are "
                  "what someone reusing the design needs; concrete examples are needed too, "
                  "to see the design at work. So each pattern is written in a fixed set of "
                  "sections, listed here by their headings, which are the book's own."),
            ("code", _lines(TEMPLATE_HEADINGS)),
            ("p", "Read as a guide, the sections fall into four groups. The name, its "
                  "classification, the <strong>Intent</strong> and any other names say "
                  "what the pattern is and the problem it addresses, in a sentence or two. "
                  "<strong>Motivation</strong> and <strong>Applicability</strong> say when "
                  "to use it: a scenario first, then the situations, and the poor designs "
                  "it can repair. <strong>Structure</strong>, "
                  "<strong>Participants</strong> and <strong>Collaborations</strong> say "
                  "what it is: the classes, drawn in a notation based on OMT, with their "
                  "responsibilities and how they work together. "
                  "<strong>Consequences</strong>, <strong>Implementation</strong>, "
                  "<strong>Sample Code</strong>, <strong>Known Uses</strong> and "
                  "<strong>Related Patterns</strong> say what using it involves: its "
                  "trade-offs, the pitfalls and techniques of building it, code in C++ or "
                  "Smalltalk, at least two uses in real systems from different domains, "
                  "and its neighbours in the catalog. The pattern lessons of this path "
                  "follow the same order in their own words."),
            ("p", "Section 1.4 is the catalog's table of contents: the twenty-three "
                  "pattern names in alphabetical order, each with its intent, from "
                  "Abstract Factory to Visitor. It is worth reading through once, quickly, "
                  "now; you will come back to it. From here on, every pattern is named with the page "
                  "it starts on in parentheses, a convention the authors say they follow "
                  "throughout the book."),
            ("p", "Section 1.5 classifies the patterns by two criteria. "
                  "<strong>Purpose</strong> is what a pattern does: creational patterns "
                  "are about making objects, structural ones about composing classes or "
                  "objects, and behavioral ones about how they interact and divide the "
                  "work. <strong>Scope</strong> is whether a pattern is mainly about "
                  "relationships between classes and their subclasses, set by inheritance "
                  "and so fixed at compile time, or about relationships between objects, "
                  "which can change at run time. Almost every pattern uses inheritance "
                  "somewhere, the authors note, so only those whose point is a class "
                  "relationship are called class patterns, and most of the catalog has "
                  "object scope."),
            ("p", "Crossing the two criteria says something about each group. A creational "
                  "class pattern leaves part of the making of an object to a subclass, as "
                  "Factory Method does; a creational object pattern leaves it to another "
                  "object, as Abstract Factory and Singleton do. Structural class patterns "
                  "combine classes by inheritance, while structural object patterns such "
                  "as Composite and Decorator assemble objects. Behavioral class patterns "
                  "use inheritance to lay out an algorithm and its flow of control, "
                  "Template Method and Interpreter among them; behavioral object patterns "
                  "such as Observer and Strategy describe objects that cooperate on a "
                  "task none of them could do alone. Those eight are the lab's "
                  "candidates, with the purpose and scope this paragraph gives each."),
            ("p", "The section adds other ways to group them. Some patterns are used "
                  "together: Composite with Iterator or with Visitor. Some are "
                  "alternatives: Prototype often instead of Abstract Factory. Some produce "
                  "similar diagrams for different intents, as Composite and Decorator do. "
                  "And the Related Patterns sections refer to one another, which the "
                  "book draws as a figure, Figure 1.1, a map of the whole catalog worth "
                  "looking at in your copy. Having several ways to see the catalog, the "
                  "authors say, deepens your sense of what each pattern does and when."),
            ("p", "Now the lab. The preset <code>class-scope</code> asks for "
                  "<code>scope = class</code> and selects 2 of the 8 candidates, "
                  "factory-method and template-method; the other 6 fail on that one "
                  "clause, each with <code>scope is object</code>. The preset "
                  "<code>behavioral-objects</code> asks for <code>purpose = behavioral and "
                  "scope = object</code> and selects observer and strategy. Its failing "
                  "list shows the clause that rejects each of the other six: the purpose "
                  "clause for the three creational and two structural patterns, the scope "
                  "clause for template-method, which is behavioral but a class pattern."),
            ("p", "The preset <code>creational-or-class</code> joins the clauses with "
                  "<code>or</code>, <code>purpose = creational or scope = class</code>, "
                  "and selects 4: the three creational patterns and template-method. Section "
                  "1.7 later suggests narrowing a search with this classification. A "
                  "selection is only as good as the attributes typed "
                  "in: the lab checks the specification against the records, and the "
                  "records against nothing."),
            ("h3", "Exercise"),
            ("code", _lines(FOUR_MORE_EXERCISE)),
            ("p", "Four more patterns, with the purpose and scope Section 1.5 gives them: "
                  "Builder and Bridge have object scope, Interpreter is the other "
                  "behavioral class pattern, and Iterator a behavioral object pattern. "
                  "By hand, say which of the four the specification selects, and for each "
                  "of the others which clause it fails. Then add them to the candidates in "
                  "the lab and check."),
            ("p", "The template and the classification say how the catalog is written. "
                  "Section 1.6 says what the patterns are for, beginning with objects "
                  "themselves. The next lesson is Objects, Interfaces and "
                  "Implementations."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "select",
            "candidates": _records(EIGHT_PATTERNS),
            "preset": "class-scope",
            "presets": [
                {"id": "class-scope",
                 "label": "Eight patterns: those with class scope",
                 "spec": "scope = class",
                 "expect": {"dspCandidates": "8",
                            "dspSatisfying": "2: factory-method, template-method"}},
                {"id": "behavioral-objects",
                 "label": "Eight patterns: behavioral, with object scope",
                 "spec": "purpose = behavioral and scope = object",
                 "expect": {"dspSatisfying": "2: observer, strategy"}},
                {"id": "creational-or-class",
                 "label": "Eight patterns: creational, or with class scope",
                 "spec": "purpose = creational or scope = class",
                 "expect": {"dspSatisfying": "4: factory-method, abstract-factory, "
                                             "singleton, template-method"}},
            ],
            "panel_title": "Patterns selected by purpose and scope",
            "panel_intro": (
                "The lab counts one consequence of a classification; what the "
                "attributes should be is the book's, and is checked against the "
                "lesson's prose, not by the lab."
            ),
        }),
        "steps_title": "Finding your way in the catalog",
        "steps_intro": "Four steps, the last of them on a problem of your own.",
        "steps": [
            ("Read the intent first",
             "For any pattern, read its Intent and Applicability before its Structure. "
             "They say whether the rest is worth reading for the problem in front of "
             "you."),
            ("Place it by purpose",
             "Ask whether the problem is about making objects, composing them, or how "
             "they interact. That picks one of the catalog's three chapters."),
            ("Place it by scope",
             "Ask whether the relationship you need is fixed when the code is compiled "
             "or must change while it runs. Class patterns give the first, object "
             "patterns the second."),
            ("Do it on a problem of your own",
             "Take a design problem from your own work, write its purpose and scope as "
             "two attributes, select the candidates from the catalog's list that match, "
             "and read their intents in Section 1.4."),
        ],
        "worked": {
            "title": "Selecting behavioral object patterns",
            "intro": [
                "Evaluate <code>purpose = behavioral and scope = object</code> on the eight "
                "candidates.",
            ],
            "lines": [
                "Factory Method: creational, fails on purpose",
                "Abstract Factory, Singleton: creational, fail",
                "Composite, Decorator: structural, fail",
                "Template Method: behavioral, but class scope",
                "Observer, Strategy: behavioral objects, selected",
                "selected: 2 of the 8 patterns",
            ],
            "after": [
                "For clauses joined only by <code>and</code>, the clause that rejects a "
                "candidate is the first one it fails, read from the left. Template Method "
                "passes the purpose clause and fails on scope.",
            ],
        },
        "quiz_title": "The template, purpose and scope",
        "quiz": [
            {"q": "In the exercise, which of the four patterns does <code>scope = class or "
                  "purpose = structural</code> select?",
             "a": ["interpreter only",
                   "bridge and interpreter",
                   "builder and bridge",
                   "interpreter and iterator"],
             "c": 1,
             "why": "Interpreter is a class pattern, so the first clause holds; Bridge is "
                    "structural, so the second does. Builder is creational with object "
                    "scope and Iterator behavioral with object scope, so both clauses fail "
                    "for each. Interpreter alone misses that an or needs only one true "
                    "clause."},
            {"q": "Which section of the template is about building the pattern: its "
                  "traps and the techniques that help?",
             "a": ["Consequences", "Applicability", "Implementation", "Collaborations"],
             "c": 2,
             "why": "Implementation is about building the pattern, including issues of "
                    "particular languages. Consequences gives the trade-offs and results "
                    "of using it, Applicability the situations it fits, Collaborations how "
                    "the participants work together."},
            {"q": "How does Section 1.5 draw the line between class and object scope?",
             "a": ["Class patterns create classes; object patterns create objects",
                   "Class patterns use inheritance; object patterns never do",
                   "Class patterns are about relationships fixed at compile time through "
                   "inheritance; object patterns about relationships that can change at "
                   "run time",
                   "Class patterns are about one class; object patterns about many"],
             "c": 2,
             "why": "Scope is whether a pattern's point is a relationship between classes "
                    "and subclasses, fixed when compiled, or between objects, changeable "
                    "while running. The authors note that nearly every pattern inherits "
                    "somewhere, object patterns included; and creation is a matter of "
                    "purpose, not scope."},
            {"q": "Which pair does Section 1.5 give as patterns that are alternatives to "
                  "each other?",
             "a": ["Composite and Iterator",
                   "Composite and Decorator",
                   "Prototype and Abstract Factory",
                   "Observer and Strategy"],
             "c": 2,
             "why": "Section 1.5 names Prototype as a frequent substitute for Abstract "
                    "Factory. Composite is "
                    "often used together with Iterator (or Visitor), and Composite and "
                    "Decorator have similar structure diagrams for different intents."},
        ],
        "mistakes": [
            ("Reading only the structure diagram",
             "Section 1.3 says a diagram records only where a design ended up, not the "
             "decisions and trade-offs behind it. A pattern read from its Structure alone "
             "loses Applicability and Consequences, which say whether it fits at all; "
             "Section 1.8 tells you to read those two first."),
            ("Thinking object patterns do not use inheritance",
             "Scope says what a pattern is mainly about, not whether it inherits. The "
             "authors note that almost every pattern uses inheritance somewhere; "
             "Observer and Strategy have abstract classes with subclasses, and are still "
             "object patterns because their point is objects linked at run time."),
            ("Treating the classification as the only map",
             "Purpose and scope are one way to organise the catalog. The authors give "
             "others in the same section: patterns used together, patterns that are "
             "alternatives, patterns with similar structure, and the cross-references "
             "of Figure 1.1. Each shows something the table does not."),
        ],
        "standard": (
            "Finish when you can say what each template section is for and classify a pattern.",
            "Given a pattern's description, state its purpose and scope with the reason "
            "for each, say which sections of the template to read first and why, and "
            "select from a list of patterns by a specification on the two criteria."
        ),
        "note": (
            "The lab selects from the attributes typed in and checks them against "
            "nothing. Whether a pattern's purpose and scope are what the records say is "
            "a matter of reading its chapter, and Section 1.5 itself places Adapter in "
            "both scopes, which a single attribute cannot hold."
        ),
    },
    # ---------------------------------------------------------------- 03
    # 1.6 How Design Patterns Solve Design Problems: Finding Appropriate Objects,
    # Determining Object Granularity, Specifying Object Interfaces, Specifying
    # Object Implementations, Class versus Interface Inheritance, Programming to
    # an Interface, not an Implementation (PDF pp. 31-38 of the operator's copy).
    # Quote: PDF p. 38 of the operator's copy, 7 + 21 = 28 words, quotes.py OK.
    # Lesson total: 28 words.
    {
        "slug": "objects-interfaces-and-implementations",
        "title": "Objects, Interfaces and Implementations",
        "module": "Chapter 1 · Introduction",
        "one_line": "An object is known only through its interface, so a client written against a type rather than a class can be given any object of that type.",
        "summary": (
            "The first half of Section 1.6 says how patterns help find objects, size "
            "them, define their interfaces and implement them, and arrives at the first "
            "principle of the book: program to an interface, not an implementation. Read "
            "the argument, then count a client's dependencies when it names three "
            "concrete classes and when it names one interface, and see what a fourth "
            "class reaches in each."
        ),
        "key": [
            "requests are the only way in",
            "an interface is a set of signatures",
            "a type names an interface",
            "the class is how; the type is what",
            "the request picks the operation at run time",
            "program to an interface, not to a class",
        ],
        "key_label": "Interfaces in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, each defined in the section in its own "
            "words; they are the vocabulary of every pattern that follows."
        ),
        "concepts": [
            ("Interface and type",
             "An operation's signature is its name, its parameters and its result; an "
             "object's interface is the set of all its signatures, the requests it "
             "accepts. A type is a name for an interface. One object can have several "
             "types, very different objects can share one, and a subtype's interface "
             "contains its supertype's."),
            ("Dynamic binding and polymorphism",
             "Dynamic binding is the choice, made when the program runs, of which "
             "object's operation answers a request. It lets one object stand in for "
             "another with the same interface, which is polymorphism: the client "
             "assumes only that the object supports the interface."),
            ("Class versus interface inheritance",
             "An object's class says how it is implemented; its type says only which "
             "requests it answers. Class inheritance shares code and representation; "
             "interface inheritance, or subtyping, says when one object can stand in "
             "place of another. Many languages run the two together."),
        ],
        "read_title": "The section's argument first, then the principle, then the count",
        "read_intro": (
            "Read the first part of Section 1.6, up to and including Programming to an "
            "Interface, not an Implementation, in your own copy first. The lesson reads "
            "it as an argument that ends in a principle, and then counts dependencies."
        ),
        "body": [
            ("p", "&ldquo;Program to an interface, not an implementation.&rdquo; The "
                  "authors set that on a line of its own in Section 1.6, How Design "
                  "Patterns Solve Design Problems, and explain it at once: &ldquo;Don't "
                  "declare variables to be instances of particular concrete classes. "
                  "Instead, commit only to an interface defined by an abstract "
                  "class.&rdquo; This lesson reads the section from its start to that "
                  "principle. Read it in your own copy first."),
            ("p", "Section 1.6 is a list of everyday design problems and the ways "
                  "patterns help with each. The first is finding the objects. An object "
                  "packages data with the operations on it, and a client can only send it "
                  "requests; that restriction is what keeps its state encapsulated. "
                  "Deciding what the objects should be is the hard part, the authors "
                  "say, because encapsulation, granularity, dependency, flexibility, "
                  "performance and reuse all pull in different directions, and methods "
                  "disagree: underline the nouns, follow responsibilities, or model the "
                  "real world. Many classes do come from analysis, but a design that only "
                  "copies today's world is not ready for tomorrow's, and some of the "
                  "most useful objects have no counterpart in it: an algorithm made an "
                  "object (Strategy), each state of something made an object (State), "
                  "found late, as a design is made flexible."),
            ("p", "The second is granularity: objects can be as small as a character or "
                  "as large as a subsystem. Patterns help here as well. Facade makes a "
                  "whole subsystem one object, and Flyweight supports very many tiny "
                  "ones; Abstract Factory and Builder produce objects whose only job is to "
                  "make other objects, and Visitor and Command objects whose only job is "
                  "to carry out a request on something else."),
            ("p", "Then interfaces. Each operation has a signature, and the set of an "
                  "object's signatures is its interface, every request it will accept. A "
                  "type is a name for an interface, so an object that accepts every "
                  "request named in a type has that type, and a subtype's interface "
                  "includes its supertype's. Objects are known only through their "
                  "interfaces, which say nothing about how the requests are carried out. "
                  "Which operation runs depends on the request and on the object that "
                  "receives it, decided when the program runs: that is dynamic binding, "
                  "and the freedom it gives to swap one object for another of the same "
                  "type is polymorphism. Patterns often say what belongs in an interface "
                  "(Memento's two, one narrow and one privileged) and how interfaces must "
                  "relate (a Decorator's and a Proxy's match the object they wrap)."),
            ("p", "Then implementations. A class defines an object's data and "
                  "operations; a subclass inherits both and may override; an abstract "
                  "class exists mainly to define an interface for its subclasses and "
                  "cannot be instantiated. The section's key distinction follows. An "
                  "object's class is how it is built; its type is only what it can be "
                  "asked. Class inheritance reuses code and representation; interface "
                  "inheritance says what may stand in for what. C++ and Eiffel use "
                  "one mechanism for both, and Smalltalk's inheritance is of "
                  "implementation only, since its variables have no declared types. Java, "
                  "which came later, gives interface inheritance a keyword of its own, "
                  "<code>interface</code>, which is why the sketches here use it where the "
                  "book has a pure abstract class."),
            ("p", "That distinction is what the principle rests on. Inheritance is a "
                  "quick way to define a new kind of object from an old one, but its "
                  "other use matters as much: when every subclass of an abstract class "
                  "keeps its interface, all of them are subtypes, and clients can use "
                  "any of them. Clients that deal with objects only through such an "
                  "interface need not know the objects' types or the classes that "
                  "implement them, and the implementation dependencies between parts of "
                  "a system shrink accordingly. Concrete classes still have to be "
                  "instantiated somewhere, the authors add; the creational patterns are "
                  "ways of doing it without the rest of the code naming them."),
            ("code", _lines(LOCKER_CONCRETE_JAVA)),
            ("p", "That is a parcel locker's app, written to three implementations: it "
                  "names a text sender, a mail sender and a push sender, and chooses "
                  "among them itself. The preset <code>concrete-senders</code> writes its "
                  "dependencies as records, user then used. The lab counts 4 classes, 3 "
                  "distinct uses and 6 possible pairs, of which 3 are connected, printed reduced as <code>1/2 = 50%</code>. The largest "
                  "fan-out, the most classes one class uses, is <code>LockerApp 3</code>. "
                  "The largest fan-in, the most users one class has, is a tie at 1 among "
                  "the three senders, broken alphabetically to EmailSender, and the banner "
                  "names the others."),
            ("code", _lines(LOCKER_INTERFACE_JAVA)),
            ("p", "Written to an interface, the app depends on one type, "
                  "<code>Notifier</code>, and each sender implements it. The preset "
                  "<code>one-interface</code> has 5 classes and 4 uses, connecting 4 of its "
                  "10 pairs (<code>2/5 = 40%</code>), and the figures turn round: the largest fan-in is <code>Notifier 4</code>, and no class "
                  "uses more than one other, so the largest fan-out is a tie at 1. The two "
                  "presets with a postal sender added show what a new variant reaches. "
                  "With concrete senders, <code>LockerApp</code> gains a use and its "
                  "fan-out becomes 4: the client is edited. Through the interface, the new "
                  "use runs from <code>PostSender</code> to <code>Notifier</code>, and "
                  "the app is untouched. The lab leaves out the line that creates a "
                  "<code>PostSender</code> and hands it to the app; that line is what "
                  "the creational patterns of course 3 are about."),
            ("h3", "Exercise"),
            ("code", _lines(TILE_VIEWER_EXERCISE)),
            ("p", "A map viewer's tile view, before and after its three tile sources are "
                  "put behind one interface. By hand, give the fan-out of "
                  "<code>TileView</code> and the fan-in of each used class in both "
                  "designs, and the number of distinct uses. Then type the records into "
                  "the lab to check, and say which class a fourth tile source would make "
                  "you edit in each."),
            ("p", "Programming to an interface is the first of the section's two "
                  "principles. The second is about how to reuse an implementation once "
                  "you have one. The next lesson is Inheritance Versus Composition."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "coupling",
            "preset": "concrete-senders",
            "presets": [
                {"id": "concrete-senders",
                 "label": "A locker app that names three concrete senders",
                 "edges": _records(LOCKER_CONCRETE),
                 "expect": {"dgModules": "4", "dgEdges": "3",
                            "dgPairs": "6", "dgConnected": "1/2 = 50%", "dgFanOut": "LockerApp 3",
                            "dgFanIn": "EmailSender 1"}},
                {"id": "one-interface",
                 "label": "The same app written to one interface, Notifier",
                 "edges": _records(LOCKER_INTERFACE),
                 "expect": {"dgModules": "5", "dgEdges": "4",
                            "dgPairs": "10", "dgConnected": "2/5 = 40%",
                            "dgFanOut": "EmailSender 1", "dgFanIn": "Notifier 4"}},
                {"id": "concrete-plus-post",
                 "label": "Concrete senders, with a postal sender added",
                 "edges": _records(LOCKER_CONCRETE_POST),
                 "expect": {"dgModules": "5", "dgEdges": "4",
                            "dgFanOut": "LockerApp 4", "dgFanIn": "EmailSender 1"}},
                {"id": "interface-plus-post",
                 "label": "The interface, with a postal sender added",
                 "edges": _records(LOCKER_INTERFACE_POST),
                 "expect": {"dgModules": "6", "dgEdges": "5",
                            "dgFanOut": "EmailSender 1", "dgFanIn": "Notifier 5"}},
            ],
            "panel_title": "A client's dependencies on classes and on an interface",
            "panel_intro": (
                "Each record is one use, written user, used. The lab counts the "
                "classes, the distinct uses, the possible pairs, the pairs connected "
                "in either direction, and the largest fan-out and fan-in. The designs "
                "are the lesson's, and a count shows one consequence of programming to "
                "an interface or not, not whether a design needs one."
            ),
        }),
        "steps_title": "Finding where a client commits to a class",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("List what the client uses",
             "Write one record for each class or interface the client names in a field, "
             "parameter, local variable or constructor call."),
            ("Mark the concrete ones",
             "Mark each used name that is a concrete class rather than an interface or "
             "abstract class. Those are the client's commitments to an implementation."),
            ("Add a variant on paper",
             "Add one more implementation of the thing that varies, and write down "
             "which existing classes gain a record. If the client is one of them, it "
             "must be edited for every new variant."),
            ("Do it on code of your own",
             "Pick a class in your own code that chooses among several implementations "
             "with an <code>if</code> or a <code>switch</code>. Count its fan-out, then "
             "count it again with the choices behind one interface, and say where the "
             "concrete classes would be created instead."),
        ],
        "worked": {
            "title": "A fourth sender, two ways",
            "intro": [
                "Compare <code>concrete-plus-post</code> with <code>interface-plus-post</code>.",
            ],
            "lines": [
                "concrete: LockerApp uses Sms, Email, Push",
                "add PostSender: LockerApp gains a use",
                "LockerApp fan out: 3 → 4, so it is edited",
                "interface: every sender uses Notifier",
                "add PostSender: PostSender → Notifier",
                "LockerApp fan out stays 1; Notifier fan in 5",
            ],
            "after": [
                "Under the interface, the new class depends on the type, and nothing that "
                "already exists depends on the new class. Whatever creates the "
                "<code>PostSender</code> still names it, which is the creational patterns' "
                "problem.",
            ],
        },
        "quiz_title": "Interfaces, types and dependencies",
        "quiz": [
            {"q": "In the exercise, what is the fan-out of <code>TileView</code> before and "
                  "after, and the fan-in of <code>TileSource</code> after?",
             "a": ["4 before, 2 after; TileSource fan-in 3",
                   "4 before, 1 after; TileSource fan-in 3",
                   "3 before, 2 after; TileSource fan-in 4",
                   "4 before, 2 after; TileSource fan-in 4"],
             "c": 3,
             "why": "Before, TileView uses three sources and the renderer: 4. After, it "
                    "uses TileSource and CanvasRenderer: 2, since the renderer was never "
                    "put behind the interface. TileSource is used by the three sources, "
                    "which implement it, and by TileView, which calls it, so its fan-in is "
                    "4; a fan-in of 3 forgets the client."},
            {"q": "On the two presets with a postal sender added, which existing class "
                  "gains a dependency?",
             "a": ["LockerApp in both designs",
                   "LockerApp with concrete senders; none through the interface",
                   "Notifier in both designs",
                   "None in either design"],
             "c": 1,
             "why": "With concrete senders the app must name PostSender, so its fan-out "
                    "goes from 3 to 4. Through the interface the only new record is "
                    "PostSender, Notifier: a use from the new class. Notifier gains a "
                    "user, but it does not depend on anything new and is not edited."},
            {"q": "What does Section 1.6 call the choice, made while the program runs, "
                  "of which object's operation answers a request?",
             "a": ["Polymorphism", "Dynamic binding", "Interface inheritance",
                   "Encapsulation"],
             "c": 1,
             "why": "That association is dynamic binding. Polymorphism is the "
                    "substitutability it makes possible; interface inheritance is "
                    "subtyping; encapsulation is the object's state being reachable only "
                    "through its operations."},
            {"q": "In the authors' account, what does inheritance mean in Smalltalk?",
             "a": ["Implementation inheritance only",
                   "Interface inheritance only",
                   "Both interface and implementation inheritance, as in C++",
                   "Nothing: Smalltalk has no inheritance"],
             "c": 0,
             "why": "Smalltalk variables have no declared types, so any object that "
                    "supports the requests sent to it can be assigned; inheritance there "
                    "shares implementation only. In C++ and Eiffel it means both."},
        ],
        "mistakes": [
            ("Taking an object's class and its type for the same thing",
             "Section 1.6 separates them: the class says how an object is implemented, "
             "the type only which requests it answers. A single object may carry several "
             "types, and unrelated classes may share a type; on the lesson's "
             "illustration, three unrelated sender classes all have the type "
             "<code>Notifier</code>."),
            ("Expecting the real world to supply every object",
             "The authors grant that many classes come from analysis, but warn that a "
             "design which only models today's world may not suit tomorrow's. Some of the "
             "objects that make a design flexible, an algorithm or a state made into an "
             "object, have no counterpart in the world and appear only as the design is "
             "worked."),
            ("Thinking an interface removes concrete classes from the program",
             "Concrete classes must be instantiated somewhere, as the section says "
             "itself. Programming to an interface moves the naming of them out of the "
             "clients; the creational patterns say where it goes."),
        ],
        "standard": (
            "Finish when you can tell a class from a type and count a client's commitments.",
            "Given a client and the classes it uses, state its fan-out and which uses "
            "are of concrete classes, say what a new implementation reaches with and "
            "without an interface, and define signature, interface, type, dynamic "
            "binding and polymorphism."
        ),
        "note": (
            "The lab counts uses on the records it is given. It cannot see who creates "
            "the objects, whether a variant will ever be added, or whether an interface "
            "with one implementation earns its place; the authors' principle is a "
            "default, and each pattern's consequences say when it pays."
        ),
    },
    # ---------------------------------------------------------------- 04
    # 1.6: Putting Reuse Mechanisms to Work (Inheritance versus Composition,
    # Delegation, Inheritance versus Parameterized Types) and Relating Run-Time
    # and Compile-Time Structures (PDF pp. 38-43 of the operator's copy).
    # Quote: PDF p. 40 of the operator's copy, 6 + 22 = 28 words, quotes.py OK.
    # Lesson total: 28 words.
    {
        "slug": "inheritance-versus-composition",
        "title": "Inheritance Versus Composition",
        "module": "Chapter 1 · Introduction",
        "one_line": "Reuse by subclassing is fixed when the code is compiled and exposes the parent; reuse by composing objects can change while it runs, at the cost of more objects.",
        "summary": (
            "The second part of Section 1.6 weighs the two ways to reuse what a class "
            "does, inheriting from it or holding an instance of it, and states the "
            "book's second principle: favor object composition over class inheritance. "
            "Read the argument, then count the classes a design needs when every "
            "combination of its variations is a subclass and when each variation is its "
            "own hierarchy."
        ),
        "key": [
            "inheritance: white box, fixed at compile time",
            "composition: black box, set at run time",
            "favor composition over inheritance",
            "delegation: forward and pass yourself",
            "subclass per combination: a product",
            "hierarchy per aspect: a sum",
        ],
        "key_label": "Reuse in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's names for "
            "kinds of reuse; the third is its distinction between two run-time "
            "relationships."
        ),
        "concepts": [
            ("White-box and black-box reuse",
             "Reuse by subclassing is white-box: the parent's internals are often "
             "visible to the subclass. Reuse by composing objects is black-box: each "
             "object is used only through its interface, and its insides stay hidden."),
            ("Delegation",
             "Composition made as strong as inheritance: an object handles a request by "
             "passing it to another object, its delegate, and passes itself along so "
             "the delegate can refer back to it, as an inherited operation can refer to "
             "<code>this</code>."),
            ("Aggregation and acquaintance",
             "Aggregation means one object owns another and they share a lifetime. "
             "Acquaintance means one object merely knows another and may send it "
             "requests. Both are usually written as a reference, so the difference "
             "lies in intent and shows at run time more than in the code."),
        ],
        "read_title": "The section's argument first, then the principle, then the count",
        "read_intro": (
            "Read Putting Reuse Mechanisms to Work and Relating Run-Time and "
            "Compile-Time Structures, in Section 1.6, in your own copy first. The lesson "
            "reads them as an argument, then counts one consequence of the choice the "
            "argument is about."
        ),
        "body": [
            ("p", "&ldquo;Favor object composition over class inheritance.&rdquo; That is "
                  "the second principle of Section 1.6, and the authors give their reason "
                  "plainly: in their experience &ldquo;designers overuse inheritance as a "
                  "reuse technique, and designs are often made more reusable (and simpler) "
                  "by depending more on object composition.&rdquo; This lesson reads "
                  "Putting Reuse Mechanisms to Work, with its parts on delegation and "
                  "parameterized types, and Relating Run-Time and Compile-Time "
                  "Structures. Read them in your own copy first."),
            ("p", "There are two common ways to reuse what a class does. You can inherit "
                  "from it, so the new class is defined in terms of the old one's "
                  "implementation, which the authors call white-box reuse because the "
                  "parent's insides are often visible to the child. Or you can hold an "
                  "object of it and send it requests, building larger behaviour out of "
                  "objects with well-defined interfaces, which is black-box reuse."),
            ("p", "Inheritance has real advantages, the section says: the language "
                  "supports it directly, it is easy to use, and overriding some "
                  "operations can change what the inherited ones do. Its disadvantages "
                  "are two. What a class inherits cannot be swapped while the program "
                  "runs. And, the worse of the two, a parent often fixes part of its "
                  "children's representation, so a subclass is bound to its parent's "
                  "implementation and must change when that changes, the sense of the "
                  "saying that inheritance breaks encapsulation. One remedy is to inherit "
                  "only from abstract classes, which carry little or no implementation."),
            ("p", "Composition is set up while the program runs, by objects getting "
                  "references to other objects. It asks for interfaces designed with "
                  "care, but in return no encapsulation is broken, any object can be "
                  "replaced by another of the same type, and there are far fewer "
                  "implementation dependencies. It also keeps classes small and each on "
                  "one task. Its cost, which the authors state in the same paragraph, is "
                  "more objects, if fewer classes, and behaviour that lives in how those "
                  "objects are connected rather than in one place you can read. They do "
                  "not set the two against each other in the end: the components on hand "
                  "are never quite enough, inheritance makes new ones easy to write, and "
                  "the two work together."),
            ("p", "Delegation is the strong form of composition. The receiving object "
                  "forwards a request to a delegate and passes itself along, so the "
                  "delegate can refer back to it, the way an inherited operation refers to "
                  "<code>this</code> in C++ or <code>self</code> in Smalltalk. The book's "
                  "example is a window that, instead of being a subclass of rectangle, "
                  "holds a rectangle and forwards its area to it, so it can become a "
                  "circle while the program runs by swapping that object. The price, the "
                  "authors say, is that software so dynamic and so parameterized is harder "
                  "to understand, and some run time; delegation is a good choice only when "
                  "it removes more complexity than it adds, and works best in the stylized "
                  "forms that patterns give it, as State, Strategy and Visitor do."),
            ("p", "Parameterized types, C++ templates or Ada and Eiffel generics, are a "
                  "third way. The section's example is a sort that compares elements: the "
                  "comparison could be an operation a subclass supplies, which is Template "
                  "Method; an object passed to the sort, which is Strategy; or a template "
                  "parameter. Composition can change at run time but costs indirection; "
                  "inheritance gives defaults that subclasses override; parameterized "
                  "types change the types a class uses, and neither of the last two "
                  "changes at run time. Java gained generics in 2004, nine years after the "
                  "book, and its <code>Comparator</code> is the Strategy form of the "
                  "example."),
            ("p", "The last part contrasts a program's two structures. The code is frozen "
                  "when compiled, classes in fixed inheritance relationships; the running "
                  "program is a changing network of objects. Aggregation, one object "
                  "owning another with the same lifetime, and acquaintance, one object "
                  "merely knowing another, are usually written the same way, as a "
                  "reference, and differ in intent; acquaintances are made and unmade more "
                  "often and are harder to see in the source. So, the authors conclude, "
                  "the code will not show everything about how a system runs, and "
                  "patterns with object scope, Composite, Decorator, Observer, Chain of "
                  "Responsibility, are often what make the run-time structure "
                  "readable."),
            ("code", _lines(PLAYER_JAVA)),
            ("p", "Now the count, on a music player of the lesson's own. It varies in two "
                  "ways: where tracks come from (a local library, a stream, a radio "
                  "station, a podcast feed) and the order they play in (in order, "
                  "shuffled, repeated). The preset <code>two-aspects</code> makes every "
                  "combination a subclass of one abstract player: 4 × 3 = 12 "
                  "combinations and 13 classes. With one hierarchy per aspect, an "
                  "abstract class and a concrete class per variant joined by "
                  "composition as in the sketch, it needs (4 + 1) + (3 + 1) = 9, a ratio "
                  "of 13/9 ≈ 1.4×. The lab treats the first aspect as the one a client "
                  "holds, so each source object holds 1 reference, to an order; the "
                  "sketch keeps both references in a small <code>Player</code>, one "
                  "class the count leaves out. A "
                  "new order, say one that plays by mood, adds 4 classes as subclasses, "
                  "one per source, against 1 class with composition."),
            ("p", "The preset <code>three-aspects</code> adds the output, a speaker or "
                  "headphones. Combinations double to 24 and subclassing needs 25 "
                  "classes, while composition needs 12; the ratio grows to 25/12 ≈ 2.1×, "
                  "each source holds 2 references, and a new order now adds 8 subclasses "
                  "against 1. That growth by multiplication is what the section's list "
                  "of causes of redesign, in the next lesson, calls an explosion of "
                  "classes. It is one consequence. The count does not show the cost the "
                  "authors put beside it, that the composed player's behaviour is spread "
                  "over three objects; <em>Code Complete, Read Along</em> weighs the same "
                  "choice from the other side in Inheritance, Containment and Members."),
            ("h3", "Exercise"),
            ("code", _lines(IRRIGATION_EXERCISE)),
            ("p", "A garden irrigation controller varies in what triggers watering, which "
                  "zone it waters and which kind of valve it drives. By hand, count the "
                  "combinations, the classes as one subclass per combination, and the "
                  "classes as one hierarchy per aspect, and the classes a new trigger adds "
                  "under each. Then type the aspects into the lab to check."),
            ("p", "Inheritance and composition are mechanisms. Section 1.6 ends on what "
                  "they are for: building a system that can take the changes it will "
                  "meet. The next lesson is Designing for Change."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "explosion",
            "preset": "two-aspects",
            "presets": [
                {"id": "two-aspects",
                 "label": "A music player: four sources and three orders",
                 "aspects": _records(PLAYER_TWO),
                 "added": "order",
                 "expect": {"gclCombos": "4 × 3 = 12", "gclSubclass": "12 + 1 = 13",
                            "gclCompose": "(4 + 1) + (3 + 1) = 9",
                            "gclRatio": "13/9 ≈ 1.4×", "gclRefs": "1: order",
                            "gclAddSubclass": "4 (13 → 17)",
                            "gclAddCompose": "1 (9 → 10)"}},
                {"id": "three-aspects",
                 "label": "The same player, with two outputs as well",
                 "aspects": _records(PLAYER_THREE),
                 "added": "order",
                 "expect": {"gclCombos": "4 × 3 × 2 = 24", "gclSubclass": "24 + 1 = 25",
                            "gclCompose": "(4 + 1) + (3 + 1) + (2 + 1) = 12",
                            "gclRatio": "25/12 ≈ 2.1×", "gclRefs": "2: order, output",
                            "gclAddSubclass": "4 × 2 = 8 (25 → 33)",
                            "gclAddCompose": "1 (12 → 13)"}},
            ],
            "panel_title": "Classes as one subclass per combination and as one hierarchy per aspect",
        }),
        "steps_title": "Counting the classes a design's variations need",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("List the aspects that vary",
             "Write each independent way the design varies, with its variants. Two "
             "aspects are independent when any variant of one can go with any variant "
             "of the other."),
            ("Count both designs",
             "Multiply the variant counts and add 1 for one subclass per combination; "
             "add the variant counts and one abstract class per aspect for composition."),
            ("Add a variant",
             "Add one variant to one aspect. Under subclassing it adds the product of "
             "the other aspects' counts; under composition it adds one class."),
            ("Do it on a design of your own",
             "Find a class hierarchy in your own code whose subclass names join two "
             "words, such as a format and a destination. Count its aspects and variants, "
             "count both designs, and say what the composed version would make harder "
             "to read."),
        ],
        "worked": {
            "title": "Three aspects of a player",
            "intro": [
                "Count the classes on the preset <code>three-aspects</code>.",
            ],
            "lines": [
                "sources 4, orders 3, outputs 2",
                "combinations: 4 × 3 × 2 gives 24",
                "a subclass for each, plus a base: 25",
                "one hierarchy each: 5 + 4 + 3 gives 12",
                "a mood order as subclasses: 4 × 2 gives 8 more",
                "a mood order by composition: 1 more",
            ],
            "after": [
                "Subclassing grows with the product of the counts and composition with "
                "their sum. Neither design edits an existing class to add the mood order; "
                "the difference is how many new ones it takes.",
            ],
        },
        "quiz_title": "Inheritance, composition and delegation",
        "quiz": [
            {"q": "In the exercise, how many classes does the controller need under each "
                  "design, and how many does a new trigger add under each?",
             "a": ["19 and 11; a new trigger adds 6 and 1",
                   "18 and 11; a new trigger adds 6 and 1",
                   "19 and 8; a new trigger adds 6 and 1",
                   "19 and 11; a new trigger adds 9 and 1"],
             "c": 0,
             "why": "There are 3 × 3 × 2 = 18 combinations, so 19 classes with the base; "
                    "composition needs (3 + 1) + (3 + 1) + (2 + 1) = 11. A new trigger "
                    "goes with every zone and valve, 3 × 2 = 6 subclasses, against 1 "
                    "class. 18 forgets the base, 8 forgets the abstract classes, and 9 "
                    "multiplies the wrong aspects."},
            {"q": "On the preset <code>three-aspects</code>, how many classes does one "
                  "new order add when every combination is a subclass?",
             "a": ["12", "8", "6", "1"],
             "c": 1,
             "why": "A new order goes with each of 4 sources and 2 outputs: 4 × 2 = 8, "
                    "taking 25 classes to 33. 12 is the product of sources and orders, 6 "
                    "the product of orders and outputs, and 1 is what composition adds."},
            {"q": "What disadvantage of delegation do the authors name?",
             "a": ["What it delegates cannot change while the program runs",
                   "It breaks encapsulation by exposing the delegate's internals",
                   "Software this dynamic and parameterized is harder to follow",
                   "It needs multiple inheritance"],
             "c": 2,
             "why": "Because so much is decided by which objects are connected at run "
                    "time, the design is harder to follow than one fixed in code, and there "
                    "is some run-time cost. Being "
                    "fixed at compile time and breaking encapsulation are inheritance's "
                    "disadvantages; multiple inheritance is what mixin classes need."},
            {"q": "How does Section 1.6 tell aggregation from acquaintance?",
             "a": ["Aggregation is a reference; acquaintance is a copy",
                   "Aggregation means owning, with a shared lifetime; acquaintance means "
                   "only knowing of",
                   "Aggregation is fixed at compile time; acquaintance only at run time",
                   "Acquaintance is the stronger of the two"],
             "c": 1,
             "why": "An aggregate owns its part and they have the same lifetime; "
                    "acquainted objects only know each other and may send requests. Both "
                    "are usually written as references, which is why the difference is one "
                    "of intent; acquaintance is the weaker, looser relationship."},
        ],
        "mistakes": [
            ("Reading the principle as never inherit",
             "The authors say favor, not replace. They point out that the set of "
             "components on hand is never rich enough, that inheritance makes new "
             "components easy to write, and that inheritance and composition work "
             "together; and they state composition's own costs, more objects and "
             "behaviour spread across their connections."),
            ("Thinking the case against inheritance is the class count",
             "The count is the lesson's illustration. The section's reasons are that an "
             "inherited implementation cannot change at run time and that a subclass is "
             "bound to its parent's representation, so a change in the parent forces "
             "changes in the child. A design with few subclasses can still suffer "
             "both."),
            ("Expecting the code to show owning and knowing",
             "Aggregation and acquaintance are usually written the same way, as a "
             "reference, and the authors say the distinction is one of intent that the "
             "compile-time structure may hide. The run-time structure has to be designed "
             "and documented; patterns help make it visible."),
        ],
        "standard": (
            "Finish when you can count classes both ways and state the trade-offs in the book's terms.",
            "Given the aspects a design varies in, state the classes under each design "
            "and what a new variant adds, give inheritance's two disadvantages and "
            "composition's cost, and say what delegation adds to composition."
        ),
        "note": (
            "The lab counts classes, and only classes. It cannot weigh the cost the "
            "authors set beside composition, behaviour spread over several objects and "
            "harder to follow, nor say whether the aspects really vary independently; "
            "both decide whether the smaller count is worth having."
        ),
    },
    # ---------------------------------------------------------------- 05
    # 1.6: Designing for Change (the eight causes of redesign, PDF pp. 43-45 of
    # the operator's copy), Application Programs, Toolkits, Frameworks
    # (pp. 45-48).
    # Quote: PDF p. 44 of the operator's copy, 26 words, quotes.py OK; its
    # words "particular" (1) and "particular kind of change" (4) quoted again
    # in the body, OK. Lesson total: 31 words.
    {
        "slug": "designing-for-change",
        "title": "Designing for Change",
        "module": "Chapter 1 · Introduction",
        "one_line": "Most redesign has a few common causes, and each pattern guards against one or more of them by letting one aspect of a system change on its own.",
        "summary": (
            "The last part of Section 1.6 lists eight common causes of redesign, each "
            "with the patterns that address it, and asks how much flexibility "
            "application programs, toolkits and frameworks each need. Read the argument, "
            "then count the modules each change request reaches when a varying thing is "
            "spread through a design and when it is behind one interface."
        ),
        "key": [
            "anticipate change, or redesign later",
            "each pattern lets one aspect vary",
            "eight common causes of redesign",
            "a toolkit is called; a framework calls",
            "an interface confines changes behind it",
            "a change to the interface still spreads",
        ],
        "key_label": "Designing for change in six lines",
        "concepts_intro": (
            "Three terms carry the lesson, all from the section: the idea that "
            "organises its list, and two of its three kinds of software."
        ),
        "concepts": [
            ("Cause of redesign",
             "A common way a design ties itself to something that later changes: naming "
             "a class when creating an object, relying on one particular operation or "
             "platform, knowing how another object is stored, depending on an "
             "algorithm, tight coupling, extending by subclassing, or needing to alter "
             "a class that cannot conveniently be altered."),
            ("Toolkit",
             "A set of related, reusable, general-purpose classes, such as collections "
             "or a stream library, that an application calls. It imposes no design on "
             "the application and is reuse of code, the object-oriented counterpart of "
             "a subroutine library."),
            ("Framework and inversion of control",
             "A set of cooperating classes that form a reusable design for one kind of "
             "software. The application subclasses its abstract classes, and the "
             "framework's code calls the application's: the application keeps the "
             "hooks and the framework keeps the loop, the reverse of using a toolkit."),
        ],
        "read_title": "The section's argument first, then the causes, then the count",
        "read_intro": (
            "Read Designing for Change, with its parts on application programs, "
            "toolkits and frameworks, in your own copy first. The lesson reads the list "
            "of causes as a tool and the rest as an argument about how much flexibility "
            "each kind of software needs."
        ),
        "body": [
            ("p", "&ldquo;Each design pattern lets some aspect of system structure vary "
                  "independently of other aspects, thereby making a system more robust to "
                  "a particular kind of change.&rdquo; The authors write that in Designing "
                  "for Change, the last part of Section 1.6. This lesson reads it, with "
                  "its discussion of application programs, toolkits and frameworks. Read "
                  "them in your own copy first."),
            ("p", "The argument begins with reuse. Getting the most out of a design, the "
                  "authors say, depends on anticipating new requirements and changes to "
                  "old ones, and on building so the system can evolve with them; a design "
                  "that ignores change risks major redesign later, with classes redefined "
                  "and reimplemented, clients modified and everything tested again. "
                  "Patterns help by making a system able to change in specific ways. The "
                  "word that matters in the opening quotation is "
                  "&ldquo;particular&rdquo;: a pattern protects against one kind of "
                  "change, not against change."),
            ("p", "Then the list, eight common causes of redesign, read here as a tool. "
                  "One: creating an object by naming its class, which commits the code to "
                  "an implementation; create objects indirectly, with Abstract Factory, "
                  "Factory Method or Prototype. Two: depending on one particular "
                  "operation to satisfy a request; Chain of Responsibility and Command "
                  "avoid hard-coding it. Three: depending on a hardware or software "
                  "platform, which makes porting and even keeping up to date harder; "
                  "Abstract Factory and Bridge limit it. Four: clients that know how an "
                  "object is stored, laid out, found or built, and must "
                  "change with it; Abstract Factory, Bridge, Memento and Proxy hide "
                  "that."),
            ("p", "Five: depending on an algorithm that will be extended, optimised or "
                  "replaced; isolate it with Builder, Iterator, Strategy, Template Method "
                  "or Visitor. Six: tight coupling, classes that cannot be understood, "
                  "changed or reused apart, until the system is one dense mass; abstract "
                  "coupling and layering loosen it, in Abstract Factory, Bridge, Chain of "
                  "Responsibility, Command, Facade, Mediator and Observer. Seven: "
                  "extending by subclassing, which needs a deep understanding of the "
                  "parent and can multiply classes, the count of the last lesson; Bridge, "
                  "Chain of Responsibility, Composite, Decorator, Observer and Strategy "
                  "let you add one subclass and compose it instead, though heavy "
                  "composition is harder to understand. Eight: a class you cannot "
                  "conveniently alter, because you lack its source or a change would "
                  "ripple through its subclasses; Adapter, Decorator and Visitor work "
                  "around it."),
            ("p", "How much of this flexibility matters, the section continues, depends on "
                  "what you are building. In an application program, a document editor "
                  "for instance, the priorities are internal reuse, maintainability and "
                  "extension, and patterns that reduce dependencies serve all three. A "
                  "toolkit, a library of general classes like collections, is called by "
                  "applications it cannot foresee, so it must avoid assumptions that "
                  "would limit where it can be used; designing one is arguably harder than "
                  "designing an application, the authors say."),
            ("p", "A framework is hardest of all. It is a reusable design for one kind of "
                  "software, graphical editors or compilers, say, and an application "
                  "customises it by subclassing its abstract classes. It fixes the "
                  "architecture, the classes and their responsibilities, how they "
                  "collaborate and who has control, and that inverts the usual "
                  "relationship: with a toolkit your code is in charge and calls the "
                  "library; with a framework the framework's code is in charge and calls "
                  "yours. Applications built on one are quicker to write and alike in "
                  "structure, at the cost of some freedom, and they are exposed to every "
                  "change in its interfaces, so loose coupling matters most here. Mature "
                  "frameworks, the authors observe, usually contain several patterns, and "
                  "documenting a framework by its patterns makes it easier to learn."),
            ("code", _lines(FRAMEWORK_JAVA)),
            ("p", "Patterns and frameworks differ in three ways, the section ends. Patterns "
                  "are more abstract: a framework is code you can run and reuse "
                  "directly, while a pattern has to be implemented each time, and comes "
                  "with its intent and trade-offs. Patterns are smaller: a framework "
                  "contains several, never the reverse. And patterns are less "
                  "specialised: a framework serves one application domain, while the "
                  "catalog's patterns fit nearly any."),
            ("code", _lines(WEATHER_JAVA)),
            ("p", "Now the count, on a garden irrigation controller that reads a "
                  "commercial weather service. In the preset <code>spread</code>, four "
                  "classes in three modules call the service's web interface themselves, "
                  "which is causes three and four at once. Four change requests are "
                  "listed with the classes each touches. The lab counts modules touched "
                  "per change: new-provider 3, hourly-forecast 2, frost-threshold 1, "
                  "new-valve 1, for 7 module touches in all; 2 of the 4 changes stay "
                  "inside one module, and the largest is new-provider, 3 modules."),
            ("p", "In the preset <code>encapsulated</code> the controller has a "
                  "<code>WeatherSource</code> interface of its own, and one class, "
                  "<code>HttpWeather</code>, in a new weather module, knows the vendor. "
                  "Changing vendors now touches 1 module, so 3 of the 4 changes are "
                  "confined and the total falls to 6. But hourly-forecast changes what the "
                  "interface itself offers, and reaches the weather module and every module "
                  "whose classes use the new forecast, scheduling and alerts: 3 modules, one more than before; it is now the largest change. "
                  "That is the opening quotation's &ldquo;particular kind of "
                  "change&rdquo; in a number: the interface makes the design robust to a "
                  "new vendor, not to a new kind of forecast."),
            ("h3", "Exercise"),
            ("code", _lines(VENDING_EXERCISE)),
            ("p", "A vending machine before and after its payment is put behind an "
                  "interface, with each change's classes and their modules in brackets. "
                  "By hand, count the modules each change touches in both designs, the "
                  "total, and the changes confined to one module. Then type the elements "
                  "and changes into the lab to check, and say which cause of redesign the "
                  "interface addresses."),
            ("p", "The causes of redesign are one of the ways Section 1.7 suggests for "
                  "finding a pattern. The last lesson of the course, Selecting and Using a "
                  "Design Pattern, reads all six ways, the steps of applying one, and "
                  "the authors' warning about when not to."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "preset": "spread",
            "presets": [
                {"id": "spread",
                 "label": "An irrigation controller: the weather service called from four classes",
                 "elements": _records(GARDEN_ELEMENTS),
                 "changes": _records(GARDEN_CHANGES_SPREAD),
                 "expect": {"dmoChanges": "4",
                            "dmoPer": "new-provider 3, hourly-forecast 2, "
                                      "frost-threshold 1, new-valve 1",
                            "dmoTotal": "7",
                            "dmoConfined": "2 of 4: frost-threshold, new-valve",
                            "dmoLargest": "new-provider, 3 modules"}},
                {"id": "encapsulated",
                 "label": "The same controller with the service behind WeatherSource",
                 "elements": _records(GARDEN_ELEMENTS_ENCAPSULATED),
                 "changes": _records(GARDEN_CHANGES_ENCAPSULATED),
                 "expect": {"dmoPer": "new-provider 1, hourly-forecast 3, "
                                      "frost-threshold 1, new-valve 1",
                            "dmoTotal": "6",
                            "dmoConfined": "3 of 4: new-provider, frost-threshold, "
                                           "new-valve",
                            "dmoLargest": "hourly-forecast, 3 modules"}},
            ],
            "panel_title": "The modules each change request reaches",
            "panel_intro": (
                "The lab counts one consequence of where a varying thing lives; whether "
                "it should be encapsulated is weighed in the book, against what in the "
                "design is expected to vary."
            ),
        }),
        "steps_title": "Counting what a change reaches",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the classes and modules",
             "Write each class with its module, in the design as it is and with the "
             "interface you are considering, including any class the interface adds."),
            ("List the changes you expect",
             "For each change request the system has had or is likely to have, write "
             "the classes it alters in each design. Use the same requests for both."),
            ("Count the modules and name the cause",
             "Count the distinct modules each request reaches. For the largest, name "
             "the cause of redesign behind it and the patterns the section lists for "
             "that cause."),
            ("Do it on a system of your own",
             "Pick an outside service or library your code calls from more than one "
             "place. Count the modules your last change to how you use it touched, and "
             "say which change an interface of your own would confine and which it "
             "would not."),
        ],
        "worked": {
            "title": "The weather service, spread and encapsulated",
            "intro": [
                "Count module touches on <code>spread</code> and <code>encapsulated</code>.",
            ],
            "lines": [
                "spread, new provider: scheduling, alerts, reports",
                "spread, hourly forecast: scheduling, alerts",
                "spread: 3 + 2 + 1 + 1 gives 7 module touches",
                "encapsulated, new provider: weather only",
                "encapsulated, hourly forecast: weather, scheduling, alerts",
                "encapsulated: 1 + 3 + 1 + 1 gives 6 module touches",
            ],
            "after": [
                "A module counts once per change however many of its classes the change "
                "lists. The interface confines the vendor change and spreads the change to "
                "the interface itself one module further.",
            ],
        },
        "quiz_title": "Causes of redesign and kinds of software",
        "quiz": [
            {"q": "In the exercise, how many module touches are there before and after, and "
                  "how many changes stay inside one module after?",
             "a": ["5 before, 4 after; 2 of 3 confined after",
                   "6 before, 4 after; 2 of 3 confined after",
                   "5 before, 3 after; 3 of 3 confined after",
                   "5 before, 4 after; 1 of 3 confined after"],
             "c": 0,
             "why": "Before: card-payments reaches ui and payment (2), new-coin payment "
                    "and ui (2), restock-alert inventory (1), 5 in all. After: "
                    "card-payments still reaches payment and ui (2), new-coin only "
                    "payment (1), restock-alert 1, so 4, with new-coin and restock-alert "
                    "confined. Six counts Keypad and Display as two touches of ui; a "
                    "module counts once per change."},
            {"q": "Which patterns does Section 1.6 list for the cause of redesign "
                  "that comes from naming a class when creating an object?",
             "a": ["Abstract Factory, Factory Method, Prototype",
                   "Abstract Factory, Bridge",
                   "Adapter, Decorator, Visitor",
                   "Strategy, Template Method, Visitor"],
             "c": 0,
             "why": "Creating objects indirectly is what Abstract Factory, Factory Method "
                    "and Prototype are for. Abstract Factory and Bridge are listed for "
                    "platform dependence; Adapter, Decorator and Visitor for classes that "
                    "cannot conveniently be altered; Strategy, Template Method and Visitor "
                    "appear among the patterns for algorithmic dependencies."},
            {"q": "On the preset <code>encapsulated</code>, why does hourly-forecast reach "
                  "3 modules, one more than before?",
             "a": ["Because the weather module was added and every change now passes "
                   "through it",
                   "Because it changes the WeatherSource interface itself, so the weather "
                   "module changes along with every module that uses the new forecast",
                   "Because the lab counts each class it touches separately",
                   "Because the vendor's service was replaced"],
             "c": 1,
             "why": "The interface hides how the forecast is fetched, not what a forecast "
                    "is. A change to what the interface offers reaches WeatherSource, "
                    "HttpWeather and the three classes in scheduling and alerts that use the "
                    "new forecast; WeeklyReport also uses the interface but not the hourly "
                    "forecast, so reports is untouched. "
                    "Frost-threshold and new-valve never pass through the weather module, "
                    "and the lab counts each module once per change."},
            {"q": "What does inversion of control mean in the section on frameworks?",
             "a": ["The application calls the framework's classes, as it would a "
                   "library's",
                   "The framework is written in terms of interfaces, not classes",
                   "The framework's code runs the program and calls the operations you write",
                   "Control of the framework passes to its users' community"],
             "c": 2,
             "why": "With a toolkit your code is in charge and calls what it reuses; with "
                    "a framework the framework's code is in charge and calls operations you supply, "
                    "with the names and calling conventions it sets. The first option "
                    "describes a toolkit."},
        ],
        "mistakes": [
            ("Expecting a pattern to make a design robust to every change",
             "The authors say each pattern lets some aspect vary independently and so "
             "guards against a particular kind of change. On the lesson's illustration "
             "the interface confines a change of vendor and makes a change to the "
             "forecast itself reach one module more."),
            ("Treating frameworks and patterns as the same thing",
             "The section gives three differences: patterns are more abstract, since "
             "only examples of them can be written as code; they are smaller, since a "
             "framework contains several; and they are less specialised, since a "
             "framework belongs to one domain."),
            ("Giving every kind of software the same amount of flexibility",
             "The authors say how crucial flexibility is depends on what you build: an "
             "application program needs internal reuse and maintainability, a toolkit "
             "must avoid assumptions about the applications that call it, and a "
             "framework, which fixes their architecture, needs the most."),
        ],
        "standard": (
            "Finish when you can name the causes of redesign and count what a change reaches.",
            "Given a design's classes, modules and change requests, state the modules "
            "each change touches before and after a varying thing is encapsulated, name "
            "the cause of redesign involved and its patterns, and say what separates a "
            "toolkit, a framework and a pattern."
        ),
        "note": (
            "The lab counts the modules each listed change touches. It cannot say which "
            "changes will come, and the encapsulated design is only better if the vendor "
            "is likelier to change than the forecast; anticipating that is the designer's "
            "work, as the section says."
        ),
    },
]
