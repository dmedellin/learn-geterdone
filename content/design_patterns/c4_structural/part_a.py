"""Structural Patterns, lessons 1-5 -- Chapter 4: the introduction, Adapter,
Bridge, Composite, Decorator and Facade.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 4. Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter,
section and pattern. Every quotation is copied from that copy and checked with
quotes.py. The designs, records and Java are written for these lessons: none
of the book's code, diagrams or example data is reproduced, and no lab uses
the book's example domains. The design is docs/design-patterns/PLAN.md,
section C, Course 4.
"""


def _lines(text):
    """A snippet or record constant as a code block's list of lines."""
    return text.split("\n")


def _records(text):
    """Records written one to a line, as the single string a lab field takes."""
    return " ".join(line.strip() for line in text.split("\n") if line.strip())


MODULE = "Chapter 4 · Structural Patterns"


# ---------------------------------------------------------------- 4.1 Adapter

# A box office's ticket desk prints through a vendor's label-printer library:
# LabelJet and two subclasses. Records are user, used (a use, an extends or an
# implements).
CLASS_ADAPTERS = """TicketDesk, TicketPrinter;
JetAdapter, TicketPrinter;
JetAdapter, LabelJet;
WideJetAdapter, TicketPrinter;
WideJetAdapter, LabelJetWide;
UsbJetAdapter, TicketPrinter;
UsbJetAdapter, LabelJetUsb;
LabelJetWide, LabelJet;
LabelJetUsb, LabelJet"""

OBJECT_ADAPTER = """TicketDesk, TicketPrinter;
JetAdapter, TicketPrinter;
JetAdapter, LabelJet;
LabelJetWide, LabelJet;
LabelJetUsb, LabelJet"""

TARGET_JAVA = """// The Target: the interface the ticket desk was written against.
interface TicketPrinter {
    void print(Ticket t);
}

// An object adapter: it holds a LabelJet, the vendor's class or any subclass.
final class JetAdapter implements TicketPrinter {
    private final LabelJet jet;
    JetAdapter(LabelJet jet) { this.jet = jet; }

    public void print(Ticket t) {
        jet.feed(LabelJet.STOCK_58MM);
        jet.writeLine(t.show() + "  " + t.seat());
        jet.cut();
    }
}"""

CLASS_ADAPTER_JAVA = """// A class adapter: it is a LabelJet, so it adapts that one class.
final class JetClassAdapter extends LabelJet implements TicketPrinter {
    public void print(Ticket t) {
        feed(STOCK_58MM);
        writeLine(t.show() + "  " + t.seat());
        cut();
    }

    @Override
    protected void beep() { }   // overriding the adaptee is one line
}"""


# ---------------------------------------------------------------- 4.2 Bridge

GUIDES_THREE = "guide, tour, highlights, family; player, handset, phone, kiosk"
GUIDES_FIVE = "guide, tour, highlights, family; player, handset, phone, kiosk, web, watch"

BRIDGE_JAVA = """// The Abstraction: what a guide does, in terms of a player's primitives.
abstract class Guide {
    protected final Player player;            // the bridge
    Guide(Player player) { this.player = player; }
    abstract void arriveAt(Stop stop);
}
final class HighlightsGuide extends Guide {
    HighlightsGuide(Player player) { super(player); }
    void arriveAt(Stop stop) {
        if (stop.isHighlight()) {
            player.showTitle(stop.title());
            player.playClip(stop.shortClip());
        }
    }
}
// The Implementor: a few primitives every device supplies.
interface Player {
    void playClip(String clipId);
    void showTitle(String text);
}"""

NOTICES_EXERCISE = """notice, ready, reminder, returned, overdue;
channel, sms, email, app"""


# ---------------------------------------------------------------- 4.3 Composite

# A garden's irrigation, as zones and emitters; values are litres per minute.
GARDEN = """garden, -, Zone, -;
front, garden, Zone, -;
back, garden, Zone, -;
rose-drip, front, Emitter, 2.5;
hedge-drip, front, Emitter, 4;
lawn-spray, back, Emitter, 12.5;
beds, back, Zone, -;
herb-drip, beds, Emitter, 1.5;
veg-drip, beds, Emitter, 3.25;
tap, garden, Emitter, 6"""

COMPOSITE_JAVA = """// The Component: every part of the system answers one question.
interface Watering {
    BigDecimal litresPerMinute();
}

final class Emitter implements Watering {             // a Leaf
    private final BigDecimal flow;
    Emitter(BigDecimal flow) { this.flow = flow; }
    public BigDecimal litresPerMinute() { return flow; }
}

final class Zone implements Watering {                // a Composite
    private final List<Watering> parts = new ArrayList<>();
    void add(Watering part) { parts.add(part); }   // declared here only: safe
    public BigDecimal litresPerMinute() {
        BigDecimal sum = BigDecimal.ZERO;
        for (Watering p : parts) { sum = sum.add(p.litresPerMinute()); }
        return sum;
    }
}"""

TRANSPARENT_JAVA = """// The transparent choice: add is declared on every component.
interface Watering {
    BigDecimal litresPerMinute();
    default void add(Watering part) {
        throw new UnsupportedOperationException("an emitter has no parts");
    }
}"""

VAN_EXERCISE = """order, -, Crate, -;
breads, order, Crate, -;
cakes, order, Crate, -;
rye, breads, Bake, 4.2;
spelt, breads, Bake, 3.8;
torte, cakes, Bake, 18;
cookies, order, Bake, 6.5"""


# ---------------------------------------------------------------- 4.4 Decorator

DECORATOR_JAVA = """interface Price {                                    // the Component
    BigDecimal amount();
}
final class SeatPrice implements Price {             // the ConcreteComponent
    private final BigDecimal base;
    SeatPrice(BigDecimal base) { this.base = base; }
    public BigDecimal amount() { return base; }
}
abstract class PriceDecorator implements Price {     // the Decorator
    protected final Price inner;
    PriceDecorator(Price inner) { this.inner = inner; }
}
final class MemberDiscount extends PriceDecorator {
    MemberDiscount(Price inner) { super(inner); }
    public BigDecimal amount() {
        return inner.amount().multiply(new BigDecimal("0.9"));
    }
}
// new Insurance(new MemberDiscount(new BookingFee(new SeatPrice(stalls))))"""

CIRCLE_EXERCISE = """core:   circle, 24
layers: fee, add, 2.50; member, times, 0.9"""


# ---------------------------------------------------------------- 4.5 Facade

# A parcel locker's subsystem (LockerBank, DoorController, PinGenerator,
# SmsGateway, Ledger) and its three clients.
LOCKERS_DIRECT = """CourierApp, LockerBank;
CourierApp, DoorController;
CourierApp, PinGenerator;
CourierApp, SmsGateway;
CustomerKiosk, LockerBank;
CustomerKiosk, DoorController;
CustomerKiosk, PinGenerator;
SupportDesk, LockerBank;
SupportDesk, DoorController;
SupportDesk, Ledger;
DoorController, LockerBank;
LockerBank, Ledger"""

LOCKERS_FACADE = """CourierApp, Lockers;
CustomerKiosk, Lockers;
SupportDesk, Lockers;
SupportDesk, Ledger;
Lockers, LockerBank;
Lockers, DoorController;
Lockers, PinGenerator;
Lockers, SmsGateway;
DoorController, LockerBank;
LockerBank, Ledger"""

FACADE_JAVA = """// The Facade: one entry point for what most clients want to do.
final class Lockers {
    private final LockerBank bank;
    private final DoorController doors;
    private final PinGenerator pins;
    private final SmsGateway sms;
    Lockers(LockerBank bank, DoorController doors,
            PinGenerator pins, SmsGateway sms) {
        this.bank = bank; this.doors = doors;
        this.pins = pins; this.sms = sms;
    }
    // A courier drops a parcel: find a locker, open it, text the PIN.
    Locker deposit(Parcel p) {
        Locker free = bank.freeLockerFor(p.size());
        doors.open(free);
        String pin = pins.issue(free, p);
        sms.send(p.phone(), "Locker " + free.number() + ", PIN " + pin);
        return free;
    }
}"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 4 introduction (PDF pp. 157-158 of the operator's copy) and
    # Adapter (pp. 159-170): Intent and Motivation p. 159, Applicability p. 160,
    # Participants p. 161, Consequences and the other issues pp. 162-163,
    # Implementation pp. 163-165, Known Uses pp. 168-169, Related Patterns
    # pp. 169-170.
    # Quote: PDF p. 157 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "adapter",
        "title": "Adapter",
        "module": MODULE,
        "one_line": "A class that gives an existing class the interface its clients expect, by inheriting from it or by holding one.",
        "summary": (
            "Chapter 4 opens with what structural patterns have in common, then catalogs "
            "Adapter, which makes a class you cannot change answer to the interface your "
            "code already uses. Read the chapter introduction and the pattern, then count "
            "the classes and uses a box office's ticket desk needs to print through a "
            "vendor's three printer classes, with class adapters and with one object "
            "adapter."
        ),
        "key": [
            "structural: composing classes and objects",
            "fit an existing class to your interface",
            "class adapter: inherit the adaptee",
            "object adapter: hold the adaptee",
            "one class adapter per adaptee class",
            "one object adapter for the whole family",
            "a class adapter can override the adaptee",
        ],
        "key_label": "Adapter in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson: the pattern's two forms, and the roles it names."
        ),
        "concepts": [
            ("Target, Adaptee and Adapter",
             "The Target is the interface the client was written against. The Adaptee is "
             "an existing class whose interface does not match it. The Adapter is the new "
             "class that implements the Target and carries out each request by calling "
             "the Adaptee."),
            ("Class adapter",
             "An adapter that inherits from the adaptee and implements the target. It is "
             "one object, with no extra reference to follow, and it can override the "
             "adaptee's methods; but it is tied to that one concrete class, so each "
             "subclass to be adapted needs an adapter of its own."),
            ("Object adapter",
             "An adapter that holds an adaptee and forwards to it. One adapter serves the "
             "adaptee class and every subclass of it, and can add behaviour to them all at "
             "once; changing how the adaptee itself behaves now takes a subclass of the "
             "adaptee for the adapter to hold."),
        ],
        "read_title": "The chapter's opening, then the pattern, then the count",
        "read_intro": (
            "Read the introduction to Chapter 4 and the Adapter pattern in your own copy "
            "first. The lesson sets out what the introduction says the structural patterns "
            "share, reads Adapter section by section, and then counts two adapter designs."
        ),
        "body": [
            ("p", "&ldquo;Structural patterns are concerned with how classes and objects are "
                  "composed to form larger structures.&rdquo; So Chapter 4 begins, and its "
                  "first page sorts the seven patterns that follow by the mechanism each "
                  "relies on. Structural <em>class</em> patterns use inheritance to put "
                  "interfaces or implementations together; multiple inheritance is the first "
                  "example, and the class form of Adapter the second. Structural <em>object</em> patterns put objects "
                  "together instead, and gain something inheritance cannot give: the "
                  "composition can be changed while the program runs. Composite, Proxy, "
                  "Flyweight, Facade, Bridge and Decorator are each given a sentence or two, "
                  "and the authors promise to compare the ones that look alike at the end of "
                  "the chapter. This course reads the seven in the book's order and ends with "
                  "that comparison."),
            ("p", "Adapter's problem is a mismatch. You have code written against one "
                  "interface and a class, often from a library you did not write, that does "
                  "the work but answers to different names and arguments. Editing the "
                  "library is rarely an option, and even with its source it would be the "
                  "wrong move: a general-purpose class should not take on one application's "
                  "vocabulary. The pattern's answer is a small class in between. Its intent, "
                  "in the lesson's words: turn a class's interface into the one its clients "
                  "expect, so that classes that could not work together now can. The book "
                  "also calls it Wrapper."),
            ("p", "The Motivation section works this through a drawing editor that wants to "
                  "reuse a toolkit's text-editing view as one of its shapes; the view has the "
                  "editing and none of the shape operations. An adapter class supplies the "
                  "shape interface by calling the view, and it also supplies what the view "
                  "never had, here an object for dragging the shape about, which is the "
                  "first hint that an adapter may do more than rename. Applicability names "
                  "three cases: an existing class whose interface does not match; a class "
                  "you want to be reusable with classes nobody has written yet; and, for the "
                  "object form only, several existing subclasses that would be tedious to "
                  "adapt one by one."),
            ("p", "The participants are the Target, the Client that uses it, the Adaptee and "
                  "the Adapter; the collaboration is one sentence long: the client calls the "
                  "adapter, and the adapter calls the adaptee. Everything interesting is in "
                  "the Consequences, which the authors write as a comparison. A class adapter "
                  "commits to one concrete adaptee class, so it cannot cover that class and "
                  "its subclasses together; in exchange it can override the adaptee's "
                  "behaviour, being a subclass of it, and it adds no second object to reach "
                  "through. An object adapter is the reverse: one adapter works with the "
                  "adaptee and all its subclasses, and can add a feature to all of them at "
                  "once, but overriding the adaptee now means writing a subclass of the "
                  "adaptee and pointing the adapter at that."),
            ("code", _lines(TARGET_JAVA)),
            ("p", "In Java the class form is a class that extends the adaptee and implements "
                  "the target interface; the book's C++ gets the same effect by inheriting "
                  "the target publicly and the adaptee privately, so the adapter is a "
                  "subtype of the first and not of the second. The object form is the "
                  "wrapper above. The sketch below is the class form of the same adapter, "
                  "with the one thing it does more easily."),
            ("code", _lines(CLASS_ADAPTER_JAVA)),
            ("p", "Three further issues fill out the pattern. How much adapting an adapter "
                  "does ranges from renaming operations to supplying a whole set the adaptee "
                  "lacks. A <em>pluggable</em> adapter builds the adaptation into a reusable "
                  "class so that it can work with classes it knows nothing about: the "
                  "authors' example is a widget that draws any tree, whether its nodes answer "
                  "for their children under one name or another, and the Implementation "
                  "section gives three ways to build it, all starting from the smallest "
                  "interface that will do (abstract operations a subclass fills in, a "
                  "delegate object, or, in Smalltalk, blocks passed in). A <em>two-way</em> "
                  "adapter conforms to both interfaces, so that two clients can each see the "
                  "object as their own; the book's case joins a graphical editor framework "
                  "to a constraint solver, each with its own variable class. Known Uses "
                  "include an object adapter in InterViews that lets a structured graphic sit "
                  "in a dialog, and Smalltalk's pluggable adapters; the C++ Sample Code shows "
                  "both forms for the text shape and is not reproduced here."),
            ("p", "Now the lab, on a design of the lesson's own. A box office's ticket desk "
                  "prints through <code>TicketPrinter</code>; the printers come from a vendor "
                  "library, <code>LabelJet</code>, with two subclasses for a wide carriage "
                  "and a USB model. Each record is one use, written user, used, and an "
                  "<code>extends</code> or <code>implements</code> counts as a use. On the "
                  "preset <code>class-adapters</code> each vendor class gets its own class "
                  "adapter: the lab counts 8 modules (here, classes) and 9 distinct uses, so "
                  "9 of the 28 possible pairs are connected, about 32.1%. The largest fan-in "
                  "is <code>TicketPrinter</code>, used by 4; the largest fan-out is 2, a tie "
                  "among the three adapters, which the lab breaks alphabetically, naming "
                  "<code>JetAdapter</code>."),
            ("p", "On the preset <code>object-adapter</code> one <code>JetAdapter</code> holds "
                  "a <code>LabelJet</code>, and the desk can be handed any of the three "
                  "printers. The lab counts 6 classes and 5 uses, 5 of 15 pairs, which the lab "
                  "reduces to 1/3 (about 33.3%), and the largest fan-in moves to <code>LabelJet</code>, used by 3: "
                  "its two subclasses and the adapter. The difference in classes is the "
                  "adapters themselves, three against one, and it grows by one class "
                  "adapter for every vendor subclass you need. What the count does not show "
                  "is the other column of the trade-off: the class adapter overrode "
                  "<code>beep</code> in one line, and the object adapter would need a fourth "
                  "vendor subclass to do the same. Which matters more depends on whether the "
                  "vendor's family will grow or whether you need to change how its printers "
                  "behave."),
            ("h3", "Exercise"),
            ("p", "The vendor ships a fourth printer, <code>LabelJetColour</code>, another "
                  "subclass of <code>LabelJet</code>, and the desk must be able to use it. "
                  "By hand, give the number of classes and the number of distinct uses under "
                  "each design once it is supported, then type the records into the lab to "
                  "check."),
            ("p", "Adapter makes two existing interfaces meet. The next lesson, Bridge, keeps "
                  "an abstraction and its implementations apart from the start, with a "
                  "structure that looks much the same."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "coupling",
            "preset": "class-adapters",
            "presets": [
                {"id": "class-adapters",
                 "label": "A ticket desk and three vendor printers, one class adapter each",
                 "edges": _records(CLASS_ADAPTERS),
                 "expect": {"dgModules": "8", "dgEdges": "9", "dgPairs": "28", "dgConnected": "9/28 ≈ 32.1%", "dgFanOut": "JetAdapter 2", "dgFanIn": "TicketPrinter 4"}},
                {"id": "object-adapter",
                 "label": "The same desk and printers, one object adapter",
                 "edges": _records(OBJECT_ADAPTER),
                 "expect": {"dgModules": "6", "dgEdges": "5", "dgPairs": "15", "dgConnected": "1/3 ≈ 33.3%", "dgFanOut": "JetAdapter 2", "dgFanIn": "LabelJet 3"}},
            ],
            "panel_title": "Classes and uses under two adapter designs",
            "panel_intro": (
                "Each record is one use, written user, used; an extends or an implements "
                "counts as a use, and each name is a class. The lab counts the classes, "
                "the distinct uses, the pairs connected either way, and the largest "
                "fan-out and fan-in. The design is the lesson's, and a count shows one "
                "consequence of choosing a class or an object adapter, not which to choose."
            ),
        }),
        "steps_title": "Fitting a class to an interface",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the three roles",
             "Write down the Target the client uses, the Adaptee whose interface does not "
             "match, and the requests that must be translated. A request the adaptee "
             "cannot serve at all is one the adapter writes from scratch."),
            ("Count the adaptee classes",
             "List the adaptee class and every subclass the client may be handed. A class "
             "adapter is needed for each; one object adapter serves them all."),
            ("Check what you need to override",
             "If the adaptee's own behaviour must change, a class adapter can override it "
             "directly; an object adapter needs a subclass of the adaptee to hold."),
            ("Do it on a design of your own",
             "Take a library class your code wraps today and write its classes and uses as "
             "records. Count the adapter classes under each form, and say which of the two "
             "consequences, more subclasses to cover or behaviour to override, your design "
             "is more likely to meet."),
        ],
        "worked": {
            "title": "Three printers, two designs",
            "intro": [
                "Count the classes in <code>class-adapters</code> and <code>object-adapter</code>.",
            ],
            "lines": [
                "desk, target and vendor classes: 1 + 1 + 3 = 5",
                "class adapters: one per vendor class, 3",
                "class adapter design: 5 + 3 = 8 classes",
                "object adapter: JetAdapter holds any LabelJet, 1",
                "object adapter design: 5 + 1 = 6 classes",
                "uses: 1 + 3 × 2 + 2 = 9 against 1 + 2 + 2 = 5",
            ],
            "after": [
                "Each class adapter brings two uses, the target it implements and the vendor "
                "class it extends; the object adapter brings the same two once. The two "
                "vendor subclasses' uses of their parent are there in both designs.",
            ],
        },
        "quiz_title": "Class adapters, object adapters and the counts",
        "quiz": [
            {"q": "In the exercise, with <code>LabelJetColour</code> supported, how many "
                  "classes and distinct uses does each design have?",
             "a": ["class adapters 10 classes, 12 uses; object adapter 7 classes, 6 uses",
                   "class adapters 9 classes, 11 uses; object adapter 7 classes, 6 uses",
                   "class adapters 10 classes, 12 uses; object adapter 8 classes, 7 uses",
                   "class adapters 10 classes, 11 uses; object adapter 7 classes, 5 uses"],
             "c": 0,
             "why": "Under class adapters there are the desk, the target, four vendor classes "
                    "and four adapters, 10 classes; the uses are the desk's 1, two for each "
                    "adapter (8) and the three vendor subclasses' uses of LabelJet (3), 12. "
                    "Under the object adapter the new printer is one more class and one more "
                    "use of LabelJet: 7 classes and 6 uses. No adapter is added, because the "
                    "one JetAdapter already holds any LabelJet."},
            {"q": "Which consequence do the authors give for a class adapter and not for an "
                  "object adapter?",
             "a": ["It works with the adaptee and all of its subclasses",
                   "It can add a feature to every adaptee at once",
                   "It can override some of the adaptee's behaviour, being its subclass",
                   "It changes the adaptee's interface without changing its class"],
             "c": 2,
             "why": "A class adapter is a subclass of the adaptee, so it can override the "
                    "adaptee's methods, and it adds no extra object. Working with all the "
                    "subclasses and adding a feature to them all at once are the object "
                    "adapter's benefits. Every adapter, of either form, leaves the adaptee's "
                    "class untouched; that is not what distinguishes them."},
            {"q": "On the preset <code>class-adapters</code>, why does the lab name "
                  "<code>JetAdapter</code> as the largest fan-out?",
             "a": ["It uses more classes than any other adapter",
                   "It is the only class adapter that extends LabelJet itself",
                   "It is used by the ticket desk",
                   "Three adapters tie at 2 and the lab breaks the tie alphabetically"],
             "c": 3,
             "why": "Each of the three class adapters uses exactly two classes, the target it "
                    "implements and the vendor class it extends. The lab names the "
                    "alphabetically first of the tied names and lists the others in its "
                    "banner. The desk uses the TicketPrinter interface, not any adapter."},
            {"q": "What is a two-way adapter for, in the authors' account?",
             "a": ["Letting two different clients each see one object through their own interface",
                   "Covering an adaptee class and every subclass with one adapter",
                   "Converting requests in one direction and replies in the other",
                   "Building interface adaptation into a reusable widget"],
             "c": 0,
             "why": "An adapter answers to the target's interface, not the adaptee's, so it "
                    "cannot be used wherever the adaptee could. A two-way adapter conforms to "
                    "both, which helps when two clients need to view one object differently. "
                    "Covering the subclasses is the object adapter's benefit, and adaptation "
                    "built into a reusable class is the pluggable adapter."},
        ],
        "mistakes": [
            ("Treating the class and object forms as interchangeable",
             "They make opposite trade-offs. The class form is tied to one concrete adaptee "
             "and can override it; the object form covers a whole family of adaptee classes "
             "and makes overriding harder. On the lesson's illustration the lab shows the "
             "first half as a count, three adapters against one; the second half is a line "
             "of code the count does not see."),
            ("Expecting an adapter only to rename operations",
             "The authors place adapters on a range, from renaming to supplying a whole set "
             "of operations the adaptee lacks; their motivating adapter adds a dragging "
             "operation the reused class never had. How much work it does depends on how far "
             "apart the two interfaces are."),
            ("Changing the library class to fit your code",
             "Even with its source, a general-purpose class should not take on one "
             "application's interface. The adapter keeps that application's vocabulary on "
             "the application's side, and the library stays usable by everyone else."),
        ],
        "standard": (
            "Finish when you can count the adapters a design needs under each form.",
            "Given a target, an adaptee hierarchy and the classes the client may be handed, "
            "state the classes and uses under class adapters and under one object adapter, "
            "and name the consequence each form gives up."
        ),
        "note": (
            "The lab counts classes and uses. It cannot tell whether the vendor's family "
            "will grow, whether you will need to change how its classes behave, or whether "
            "an adapter is needed at all rather than a change on your own side; those decide "
            "between the forms, and the authors set them side by side for that reason."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Bridge (PDF pp. 171-181 of the operator's copy): Intent and Motivation
    # pp. 171-172, Applicability p. 173, Participants and Consequences p. 174,
    # Implementation pp. 175-176, Known Uses p. 180, Related Patterns p. 181.
    # Quote: PDF p. 171 of the operator's copy, 13 words (the Intent), quotes.py OK.
    # Lesson total: 13 words.
    {
        "slug": "bridge",
        "title": "Bridge",
        "module": MODULE,
        "one_line": "An abstraction and its implementation kept in two class hierarchies joined by a reference, so that each can grow without multiplying the other.",
        "summary": (
            "Bridge separates what an object offers its clients from the platform-specific "
            "code that carries it out, so that the two can be extended on their own. Read "
            "the pattern, then count the classes a museum audio guide needs with one "
            "subclass for every kind of guide on every player, and with a guide hierarchy "
            "holding a player, and what one new player adds to each."
        ),
        "key": [
            "abstraction and implementation, apart",
            "two hierarchies joined by a reference",
            "subclass per pair: a product of counts",
            "two hierarchies: a sum of counts",
            "a new player: one class, not one per guide",
            "the implementor offers primitives",
            "designed in up front, not fitted later",
        ],
        "key_label": "Bridge in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson: the two sides the pattern separates, and the "
            "structure it replaces."
        ),
        "concepts": [
            ("Abstraction and RefinedAbstraction",
             "The interface clients use, which holds a reference to an implementor and "
             "carries out its operations through it; refined abstractions are its "
             "subclasses, extending what it offers. Here, the kinds of guide."),
            ("Implementor and ConcreteImplementor",
             "The interface for the implementation classes, usually a few primitive "
             "operations that the abstraction builds its higher-level ones from; it need "
             "not match the abstraction's interface. Its concrete classes are one per "
             "platform. Here, the players."),
            ("Proliferation of classes",
             "What a single hierarchy produces when a class varies in two ways: one subclass "
             "for every pairing, so every new kind on one side means a class for each "
             "variant on the other. Rumbaugh's name for such a hierarchy, which the book "
             "cites, is nested generalizations."),
        ],
        "read_title": "The pattern, section by section, then the count",
        "read_intro": (
            "Read Bridge in your own copy first. The lesson summarises its window-system "
            "example, reads the consequences and implementation issues, and then counts "
            "the classes of a design of its own."
        ),
        "body": [
            ("p", "&ldquo;Decouple an abstraction from its implementation so that the two can "
                  "vary independently.&rdquo; That is Bridge's intent, as the book states it, "
                  "and the pattern is also known as Handle/Body. The usual way to give an "
                  "abstraction several implementations is inheritance: an abstract class for "
                  "the interface, a concrete subclass for each way of carrying it out. The "
                  "authors' objection is that inheritance fixes the pairing for good, so "
                  "abstraction and implementation can no longer be changed, extended or "
                  "reused apart."),
            ("p", "The Motivation section makes the point with a portable window class in a "
                  "user interface toolkit, implemented for two window systems. Add a "
                  "specialised kind of window and you need a subclass of it for each "
                  "system; add a third system and every kind of window needs one more "
                  "subclass. Worse, a client that creates a window must name a "
                  "system-specific class, so the client is tied to the platform too. The "
                  "pattern's answer is two hierarchies, one for the kinds of window and one "
                  "for the platform implementations, with every window operation written in "
                  "terms of the implementation's interface. The reference from one to the "
                  "other is the bridge."),
            ("p", "Applicability lists six cases: you want no permanent binding between "
                  "abstraction and implementation, perhaps because the implementation is "
                  "chosen at run time; both sides should be extensible by subclassing; "
                  "a change of implementation should leave client code untouched, not even "
                  "rebuilt; in C++, clients should see nothing of the representation; the "
                  "class hierarchy is already proliferating; or several objects should share "
                  "one implementation, invisibly to their clients, as in Coplien's string "
                  "class sharing its representation. The participants are the Abstraction, "
                  "RefinedAbstraction, Implementor and ConcreteImplementor, and they "
                  "collaborate in one way: whatever a client asks of the abstraction, the "
                  "abstraction passes on to the implementor it holds."),
            ("code", _lines(BRIDGE_JAVA)),
            ("p", "The Consequences are three. Interface and implementation are decoupled: "
                  "an implementation can be chosen while the program runs, even swapped, and "
                  "changing an implementation class no longer forces the abstraction and its "
                  "clients to be recompiled, which matters for binary compatibility between "
                  "library versions and encourages layering. Each hierarchy can be extended "
                  "on its own. And details such as shared implementor objects and their "
                  "reference counts can be hidden from clients."),
            ("p", "The Implementation section takes up four issues. With only one "
                  "implementation an abstract Implementor is unnecessary, though the "
                  "separation still protects clients from changes; Carolan's name for it is "
                  "the Cheshire Cat. Someone must create the right implementor: the "
                  "abstraction can choose from its constructor's arguments (a collection "
                  "might pick a linked list when small and a hash table when large), start "
                  "with a default and switch as usage grows, or ask another object, such as "
                  "an Abstract Factory, which keeps it from knowing any implementor class at "
                  "all. Implementors can be shared, with Coplien's Handle/Body reference "
                  "counting. And multiple inheritance cannot make a true Bridge in C++, "
                  "because inheritance binds the pair statically. The Known Uses are ET++'s "
                  "window ports, libg++'s set classes (a degenerate bridge with no abstract "
                  "implementor) and NeXT's image classes, whose image can hold several "
                  "representations at once."),
            ("p", "Now the lab, on a museum audio guide, not the book's windows. Three kinds "
                  "of guide (a full tour, the highlights, a family trail) run on three "
                  "players (a rental handset, the visitor's phone, a gallery kiosk). Each "
                  "record is one aspect that varies, then its variants. On the preset "
                  "<code>three-by-three</code> there are 3 × 3 = 9 pairings. One subclass "
                  "per pairing, under one abstract guide, is 9 + 1 = 10 classes. The bridge "
                  "is (3 + 1) + (3 + 1) = 8: an abstract class and three concrete ones on "
                  "each side, and the lab's ratio of the two counts is 10/8, which it prints as 5/4, "
                  "about 1.3. Each guide holds 1 reference, to its player."),
            ("p", "The difference that matters is in the last two tiles. A fourth player, a "
                  "web page say, adds 3 classes under subclassing (10 → 13), one for each "
                  "kind of guide, and 1 class under the bridge (8 → 9); neither design edits "
                  "an existing class for it. The preset <code>five-players</code> grows the "
                  "player side to five, and asks what one new kind of guide costs: 3 × 5 = "
                  "15 pairings, 16 classes against (3 + 1) + (5 + 1) = 10, a ratio of 1.6, "
                  "and a new guide adds 5 subclasses (16 → 21) against 1 (10 → 11). The "
                  "subclass count is the product of the variant counts and the bridge's is "
                  "their sum, so the gap widens as either side grows. The lab counts the "
                  "flattest possible single hierarchy; the book's own picture of the "
                  "proliferation has intermediate classes too, which only adds to it."),
            ("p", "None of that says the museum should build a bridge. With one player "
                  "planned and no second in sight, the separate Implementor is the "
                  "degenerate case the authors describe, worth it only if clients must be "
                  "shielded from changes. The count shows what happens if both sides grow; "
                  "whether they will is the design question."),
            ("h3", "Exercise"),
            ("code", _lines(NOTICES_EXERCISE)),
            ("p", "A parcel locker sends four kinds of notice through three channels. By "
                  "hand, give the classes under one subclass per pairing and under a bridge "
                  "of notices holding a channel, and the classes a fourth channel adds to "
                  "each. Type the records into the lab, with the channel as the aspect that "
                  "gains a variant, to check."),
            ("p", "Bridge and Adapter both forward to another object; the Discussion of "
                  "Structural Patterns, at the end of this course, sets them side by side. "
                  "The next lesson, Composite, turns from two hierarchies to one recursive "
                  "structure."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "explosion",
            "preset": "three-by-three",
            "presets": [
                {"id": "three-by-three",
                 "label": "Three kinds of guide on three players; a fourth player arrives",
                 "aspects": GUIDES_THREE,
                 "added": "player",
                 "expect": {"gclCombos": "3 × 3 = 9", "gclSubclass": "9 + 1 = 10", "gclCompose": "(3 + 1) + (3 + 1) = 8", "gclRatio": "5/4 ≈ 1.3×", "gclRefs": "1: player", "gclAddSubclass": "3 (10 → 13)", "gclAddCompose": "1 (8 → 9)"}},
                {"id": "five-players",
                 "label": "The same guides on five players; a fourth kind of guide arrives",
                 "aspects": GUIDES_FIVE,
                 "added": "guide",
                 "expect": {"gclCombos": "3 × 5 = 15", "gclSubclass": "15 + 1 = 16", "gclCompose": "(3 + 1) + (5 + 1) = 10", "gclRatio": "8/5 ≈ 1.6×", "gclRefs": "1: player", "gclAddSubclass": "5 (16 → 21)", "gclAddCompose": "1 (10 → 11)"}},
            ],
            "panel_title": "Classes with one subclass per pairing, and with a bridge",
        }),
        "steps_title": "Deciding whether a hierarchy wants a bridge",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Find the two ways the class varies",
             "Write down what clients see varying (the kinds of abstraction) and what the "
             "platform or mechanism varies (the implementations). If only one of them varies, "
             "there is nothing to bridge."),
            ("Count both designs",
             "Multiply the variant counts and add one for the subclass-per-pairing design; "
             "add the variant counts and one abstract class per side for the bridge."),
            ("Write the implementor's primitives",
             "List the few operations every implementation must supply, and check that each "
             "abstraction's operations can be written from them alone."),
            ("Do it on a design of your own",
             "Take a class in your code that has grown subclasses for two concerns at once "
             "and write its aspects as records. Count the classes now and after one new "
             "variant on each side, and say which side you expect to grow."),
        ],
        "worked": {
            "title": "One more player",
            "intro": [
                "Count what a fourth player adds on <code>three-by-three</code>.",
            ],
            "lines": [
                "guides × players: 3 × 3 = 9",
                "a subclass per guide and player: 9 + 1 = 10",
                "guide and player hierarchies: (3 + 1) + (3 + 1) = 8",
                "new player, subclassing: 3 guides, 10 → 13",
                "new player, bridge: 1 class, 8 → 9",
            ],
            "after": [
                "Under subclassing the new player is paid for once per kind of guide; under "
                "the bridge it is one ConcreteImplementor, and every guide can use it at "
                "once.",
            ],
        },
        "quiz_title": "Bridge's counts and the authors' claims",
        "quiz": [
            {"q": "In the exercise, four notices and three channels: how many classes under "
                  "one subclass per pairing and under a bridge, and what does a fourth "
                  "channel add to each?",
             "a": ["13 and 9; a fourth channel adds 4 and 1",
                   "12 and 7; a fourth channel adds 4 and 1",
                   "13 and 9; a fourth channel adds 3 and 1",
                   "13 and 8; a fourth channel adds 4 and 2"],
             "c": 0,
             "why": "There are 4 × 3 = 12 pairings, so 12 + 1 = 13 classes with one abstract "
                    "base. The bridge has (4 + 1) + (3 + 1) = 9: an abstract notice and four "
                    "kinds, an abstract channel and three channels. A fourth channel needs one "
                    "subclass per notice under subclassing, 4 (13 → 17), and one channel class "
                    "under the bridge (9 → 10)."},
            {"q": "On <code>five-players</code>, a fourth kind of guide is added. What does it "
                  "add under each design?",
             "a": ["5 classes under subclassing, 1 under the bridge",
                   "3 classes under subclassing, 1 under the bridge",
                   "5 classes under subclassing, 6 under the bridge",
                   "1 class under each design"],
             "c": 0,
             "why": "Under subclassing the new guide needs one class per player, and there are "
                    "five players: 16 → 21. Under the bridge it is one RefinedAbstraction that "
                    "works with every player through the Player interface: 10 → 11. Three is "
                    "the number of guides, which is what a new player would cost."},
            {"q": "Which of these is one of Bridge's consequences, as the authors list them?",
             "a": ["It converts an existing class's interface to the one clients expect",
                   "Changing an implementation class need not force the abstraction and its "
                   "clients to be recompiled",
                   "It reduces the number of objects at run time",
                   "It lets an abstraction add responsibilities to one object at a time"],
             "c": 1,
             "why": "Decoupling interface and implementation means clients no longer need "
                    "rebuilding when an implementation class changes, which the authors note matters for binary "
                    "compatibility between library versions. Converting an interface is "
                    "Adapter's intent and adding responsibilities object by object is "
                    "Decorator's; a bridge adds an implementor object rather than removing "
                    "any."},
            {"q": "According to the Implementation section, what is the case with only one "
                  "implementation?",
             "a": ["Not a Bridge, since nothing varies",
                   "A Bridge that must still declare an abstract Implementor",
                   "A degenerate Bridge, still useful to keep clients from recompiling when "
                   "the implementation changes",
                   "An Adapter, since the implementation already existed"],
             "c": 2,
             "why": "With one implementation an abstract Implementor class is unnecessary, and "
                    "the authors call the result a degenerate case of the pattern; the "
                    "separation still keeps a change in the implementation from reaching "
                    "clients. Carolan's term for it is the Cheshire Cat."},
        ],
        "mistakes": [
            ("Reading Bridge as Adapter under another name",
             "Both put a reference to another object behind an interface, and the Related "
             "Patterns section says the structures are similar. Bridge is designed in up "
             "front so that an abstraction and its implementations can both grow; Adapter is "
             "fitted later to make two existing interfaces meet. On the lesson's illustration "
             "the lab counts what a bridge buys when both sides grow; an adapter answers a "
             "different question."),
            ("Making the implementor mirror the abstraction",
             "The Implementor's interface need not match the Abstraction's, and the authors "
             "expect it to be smaller: primitives that every platform can supply, from which "
             "the abstraction builds its higher-level operations. Copying the abstraction's "
             "operations into it pushes the abstraction's logic into every implementation."),
            ("Building a bridge for a hierarchy that varies one way",
             "If there is one implementation and none in prospect, the separation buys only "
             "insulation from recompiling, which the authors grant as the degenerate case. "
             "The lab's counts are equal or worse for a bridge when one side has a single "
             "variant; it is growth on both sides that the pattern pays for."),
        ],
        "standard": (
            "Finish when you can count a hierarchy's classes with and without a bridge.",
            "Given the variants on each side, state the classes under one subclass per "
            "pairing and under two hierarchies, what one new variant on either side adds, "
            "and the consequences the authors claim for the separation."
        ),
        "note": (
            "The lab counts classes as products and sums. It cannot tell you whether both "
            "sides of your design will grow, or whether the implementation must be chosen at "
            "run time; those are the questions Applicability asks, and they decide whether "
            "the second hierarchy is worth having."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Composite (PDF pp. 183-193 of the operator's copy): Intent and Motivation
    # pp. 183-184, Applicability p. 184, Participants and Collaborations p. 185,
    # Consequences and Implementation pp. 186-190, Known Uses pp. 192-193,
    # Related Patterns p. 193.
    # Quote: PDF p. 183 of the operator's copy, 11 words (from the Intent),
    # quotes.py OK. Lesson total: 11 words.
    {
        "slug": "composite",
        "title": "Composite",
        "module": MODULE,
        "one_line": "Parts and wholes behind one interface, so that a client asks a single part and a whole made of parts the same question.",
        "summary": (
            "Composite builds a tree of objects in which a container and the things it "
            "contains share one interface. Read the pattern, including its trade-off between "
            "safety and transparency in declaring the child operations, then send one "
            "request down a garden's irrigation zones and count the calls, the total flow, "
            "and what happens when an emitter is asked to take a child."
        ),
        "key": [
            "parts and wholes, one interface",
            "a composite forwards to its children",
            "one call per node in the tree",
            "the total is the sum of the leaves",
            "add on the composite only: safe",
            "add on every component: transparent",
            "easy to add kinds, hard to restrict them",
        ],
        "key_label": "Composite in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson: the roles, and the choice the authors spend "
            "longest on."
        ),
        "concepts": [
            ("Component, Leaf and Composite",
             "The Component declares the interface every object in the tree answers to. A "
             "Leaf has no children and does the work itself; a Composite stores children and "
             "usually carries out a request by forwarding it to each of them, perhaps doing "
             "something before or after."),
            ("Safety",
             "Declaring the child operations, such as add and remove, only on the Composite "
             "class. Asking a leaf to add a child is then caught by the compiler, but leaves "
             "and composites no longer share one interface."),
            ("Transparency",
             "Declaring the child operations on the Component, so that every object in the "
             "tree can be treated alike. A leaf asked to add a child then compiles, and must "
             "ignore the request or fail at run time. The book's pattern leans this way."),
        ],
        "read_title": "The pattern, section by section, then the count",
        "read_intro": (
            "Read Composite in your own copy first. The lesson summarises its graphics "
            "example, reads the consequences and the nine implementation issues, and then "
            "counts the calls one request makes down a tree of its own."
        ),
        "body": [
            ("p", "&ldquo;Composite lets clients treat individual objects and compositions of "
                  "objects uniformly.&rdquo; That is the second half of the pattern's "
                  "intent; the first says what it builds, a tree of objects standing for a "
                  "part&ndash;whole hierarchy. You met it in this path's case study, Design "
                  "Problems and Document Structure, where the editor's page is built this "
                  "way; here it is the catalog entry. <em>Domain-Driven Design</em>'s lesson "
                  "Strategy and Composite in the Model reads the same pattern as a concept in "
                  "a domain; this lesson reads it as the authors wrote it."),
            ("p", "The Motivation is a drawing program in which users group simple shapes "
                  "into larger ones and group those again. With separate classes for the "
                  "simple shapes and for the containers, every piece of code that handles "
                  "them must tell the two apart, though the user hardly ever does. The "
                  "pattern removes the distinction with one abstract class that stands for "
                  "both: it declares the drawing operations and the operations for managing "
                  "children, the simple shapes implement drawing directly, and the container "
                  "class, a picture, draws by asking each child to draw. A picture can hold "
                  "pictures, so the structure nests as deep as the user likes. Applicability "
                  "is brief: use it for part&ndash;whole hierarchies, when code that uses the "
                  "structure should handle one part and a group of parts alike."),
            ("p", "Four consequences follow. Wherever the client expects a simple object it "
                  "can be given a composite one. The client becomes simpler, with no "
                  "type-testing code over the classes in the tree. New kinds of leaf or "
                  "composite work with existing structures and clients unchanged. And the "
                  "liability: the design can become too general, because the type system can "
                  "no longer stop a composite from holding a kind of component it should "
                  "not; that check moves to run time."),
            ("code", _lines(COMPOSITE_JAVA)),
            ("p", "The Implementation section raises nine issues, and the fourth is the one "
                  "the authors dwell on: where to declare the child operations. Declare "
                  "<code>add</code> and <code>remove</code> on the Component and you gain "
                  "transparency, since every node can be handled alike, at the cost of "
                  "safety, since a client can ask a leaf for something meaningless. Declare "
                  "them on the Composite alone, as the sketch above does, and the compiler "
                  "catches the mistake, but leaves and composites now have different "
                  "interfaces, and a client holding a component may need to find out whether "
                  "it is a composite before adding to it. The authors say they have favoured "
                  "transparency in the pattern, and suggest that a default "
                  "<code>add</code> fail, by raising an exception, rather than quietly do "
                  "nothing, since adding to a leaf probably means a bug."),
            ("code", _lines(TRANSPARENT_JAVA)),
            ("p", "The other issues, briefly. A child can keep an explicit reference to its "
                  "parent, which makes moving up and deleting easier, provided the invariant "
                  "is kept that a composite's children name it as their parent (changing the "
                  "parent only in <code>add</code> and <code>remove</code> keeps it). Sharing "
                  "components is hard when each has one parent; Flyweight is the way round "
                  "it. The Component interface should be as large as can be made meaningful "
                  "for both kinds, which pulls against the rule that a class should offer only "
                  "what its subclasses can use. Keeping the child list in the Component costs "
                  "space in every leaf. Children may need an order, and Iterator helps. A "
                  "composite may cache results about its children, such as a bounding box, "
                  "and must then be told when a change below invalidates the cache. Without "
                  "garbage collection the composite should delete its children. And the "
                  "structure holding the children is a matter of efficiency. Known Uses begin "
                  "with Smalltalk's original view class, which was component and composite at "
                  "once, and run through user interface toolkits, a compiler's parse trees and "
                  "a financial portfolio of assets."),
            ("p", "Now the lab, on a garden's irrigation system rather than the book's "
                  "examples. Zones hold emitters and other zones; each emitter's value is "
                  "its flow in litres per minute. Each record is node, parent, kind, value, "
                  "with <code>-</code> as the root's parent and as a composite's value. On "
                  "the preset <code>garden-safe</code> the lab counts 10 nodes: 6 leaves, 4 "
                  "composites, and a depth of 3, down from the garden through the back zone "
                  "and the beds to the herb drip. One request for the flow makes 10 calls: 1 "
                  "from the client and 9 forwarded by composites, one call per node. The "
                  "total is 29.75 litres per minute, and the table gives each zone's "
                  "subtotal: front 6.5, back 17.25, beds 4.75."),
            ("p", "The same preset asks two nodes to add a child: <code>tap</code>, an "
                  "emitter, and <code>beds</code>, a zone. The zone does. The emitter's "
                  "request is refused by the compiler, because under the safe declaration "
                  "<code>add</code> exists only on <code>Zone</code>. On the preset "
                  "<code>garden-transparent</code> the same request compiles, and the lab "
                  "says the emitter must ignore it or fail at run time. Nothing else changes: "
                  "the calls and the total are the same under either declaration, which is "
                  "the point. The choice is about when a meaningless request is caught, not "
                  "about what the tree computes."),
            ("h3", "Exercise"),
            ("code", _lines(VAN_EXERCISE)),
            ("p", "A bakery's delivery: crates hold bakes and other crates, and each bake's "
                  "value is its weight in kilograms. By hand, give the leaves, the "
                  "composites, the depth, the calls one request for the weight makes, and "
                  "the total weight. Then type the records into the lab to check."),
            ("p", "A composite holds many children and adds them up. The next lesson, "
                  "Decorator, holds exactly one and adds to it."),
        ],
        "lab": ("gofkit", {
            "mode": "tree",
            "view": "compose",
            "preset": "garden-safe",
            "presets": [
                {"id": "garden-safe",
                 "label": "A garden's zones and emitters; add declared on zones only",
                 "nodes": _records(GARDEN),
                 "asks": "tap beds",
                 "declare": "safe",
                 "expect": {"gtrNodes": "10", "gtrLeaves": "6", "gtrComposites": "4", "gtrDepth": "3", "gtrCalls": "10: 1 from the client + 9 forwarded by composites", "gtrTotal": "29.75", "gtrAskLeaves": "1: tap (refused by the compiler: add is declared only on composites)", "gtrAskTaken": "1: beds"}},
                {"id": "garden-transparent",
                 "label": "The same garden; add declared on every component",
                 "nodes": _records(GARDEN),
                 "asks": "tap beds",
                 "declare": "transparent",
                 "expect": {"gtrNodes": "10", "gtrLeaves": "6", "gtrComposites": "4", "gtrDepth": "3", "gtrCalls": "10: 1 from the client + 9 forwarded by composites", "gtrTotal": "29.75", "gtrAskLeaves": "1: tap (accepted by the interface: each ignores it or fails at run time)", "gtrAskTaken": "1: beds"}},
            ],
            "panel_title": "One request over a tree of parts",
        }),
        "steps_title": "Reading a tree the way the pattern does",
        "steps_intro": "Four steps, the last of them on a structure of your own.",
        "steps": [
            ("Sort the nodes",
             "Mark each node a leaf, with a value, or a composite, with children. A kind of "
             "node is one or the other, never both."),
            ("Count the calls",
             "One request to the root reaches every node once: the client's call and one "
             "call from each composite to each child. The calls equal the nodes."),
            ("Add up from the leaves",
             "The total is the sum of the leaf values; each composite's subtotal is the sum "
             "of the leaves below it."),
            ("Do it on a structure of your own",
             "Take a part&ndash;whole structure in your code (a menu, a bill of quantities, "
             "a folder tree) and write it as records. Count the calls and the total, and "
             "decide whether a leaf asked to add a child should fail at compile time or at "
             "run time in your design."),
        ],
        "worked": {
            "title": "One request down the garden",
            "intro": [
                "Count the calls and the total on <code>garden-safe</code>.",
            ],
            "lines": [
                "garden nodes: 4 zones + 6 emitters = 10",
                "garden calls: 1 from the client + 9 forwarded = 10",
                "front: 2.5 + 4 = 6.5",
                "beds: 1.5 + 3.25 = 4.75",
                "back: 12.5 + 4.75 = 17.25",
                "garden: 6.5 + 17.25 + 6 = 29.75",
            ],
            "after": [
                "Each zone's subtotal is computed once, by the zone, from its children's "
                "answers; the client asked one question of one object.",
            ],
        },
        "quiz_title": "Calls, totals and the child operations",
        "quiz": [
            {"q": "In the exercise, the bakery's delivery: what are the calls one request "
                  "makes, the depth, and the total weight?",
             "a": ["7 calls, depth 2, 32.5 kg", "6 calls, depth 2, 32.5 kg",
                   "7 calls, depth 3, 32.5 kg", "7 calls, depth 2, 26 kg"],
             "c": 0,
             "why": "There are 7 nodes, 3 crates and 4 bakes, and one request reaches each "
                    "once: the client's call and 6 forwarded, 7 in all. The longest path is "
                    "order, breads, rye: 2 edges. The total is 4.2 + 3.8 + 18 + 6.5 = 32.5. "
                    "Six is the forwarded calls without the client's; 26 leaves out the "
                    "cookies packed straight into the order."},
            {"q": "On <code>garden-transparent</code>, <code>tap</code> is asked to add a "
                  "child. What does the lab report?",
             "a": ["The compiler refuses it, because add is declared only on Zone",
                   "The request compiles, and the emitter must ignore it or fail at run time",
                   "The tap becomes a zone and the tree gains a level",
                   "The total flow changes, because the tap now has a child"],
             "c": 1,
             "why": "Under the transparent declaration every component has add, so the call "
                    "compiles, and a leaf can only ignore it or fail, which the authors "
                    "prefer. The compiler refusal is the safe declaration's outcome. The lab "
                    "never adds the child, so the tree and its total are unchanged."},
            {"q": "Which consequence of Composite do the authors count as a liability?",
             "a": ["Clients need type tests to tell leaves from composites",
                   "New kinds of component force changes to existing clients",
                   "The type system can no longer restrict which components a composite holds",
                   "A request reaches some leaves more than once"],
             "c": 2,
             "why": "Making it easy to add components makes it hard to restrict them: a "
                    "composite that should hold only certain kinds must check at run time. The "
                    "pattern removes type tests from clients and lets new kinds work "
                    "unchanged, and each node in a tree has one parent, so a request reaches "
                    "it once."},
            {"q": "Why do the authors suggest a default add on the Component should fail "
                  "rather than do nothing?",
             "a": ["Because doing nothing would not compile",
                   "Because adding to a leaf probably means a bug, and silence hides it",
                   "Because leaves must then delete the argument",
                   "Because a composite cannot otherwise find its parent"],
             "c": 1,
             "why": "An empty add is legal, but it quietly swallows what is most likely a "
                    "mistake; raising an exception reports it. Deleting the argument is the "
                    "option the authors note clients might not expect, and parent references "
                    "are a separate issue."},
        ],
        "mistakes": [
            ("Thinking the declaration of add changes what the tree computes",
             "Safety and transparency decide when a meaningless request to a leaf is caught, "
             "at compile time or at run time. On the lesson's illustration the calls and the "
             "total are the same under both, 10 calls and 29.75; only the outcome of asking "
             "the emitter differs."),
            ("Letting the client test which kind of node it holds",
             "The pattern exists to remove that code. If the client branches on leaf or "
             "composite for an ordinary request, the operation belongs in the Component "
             "interface, with each class answering it in its own way."),
            ("Caching a composite's result without telling it of changes",
             "The authors allow a composite to cache what it learns about its children, and "
             "attach a condition: a change below must invalidate the caches above, which is "
             "easiest when children know their parents."),
        ],
        "standard": (
            "Finish when you can trace one request down a tree of parts.",
            "Given a tree as records, state its leaves, composites, depth, the calls one "
            "request makes and the total, and say what a leaf asked to add a child does "
            "under each declaration."
        ),
        "note": (
            "The lab counts calls and adds exact values over the tree you state. It cannot "
            "tell you whether your clients really can ignore the difference between a part "
            "and a whole, or whether your composites need restricting, which the pattern "
            "makes harder; those are what Applicability and the Consequences weigh."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Decorator (PDF pp. 195-204 of the operator's copy): Intent and Motivation
    # pp. 195-196, Applicability and Participants p. 197, Consequences p. 198,
    # Implementation pp. 199-200, Known Uses pp. 202-204, Related Patterns p. 204.
    # Quote: PDF p. 195 of the operator's copy, 10 words (from the Intent),
    # quotes.py OK. Lesson total: 10 words.
    {
        "slug": "decorator",
        "title": "Decorator",
        "module": MODULE,
        "one_line": "An object that wraps another of the same interface, forwards to it and adds one responsibility, so that options are stacked at run time instead of subclassed.",
        "summary": (
            "Decorator adds responsibilities to one object at a time by wrapping it in "
            "objects of the same interface. Read the pattern, its liabilities included, then "
            "stack a booking fee, a member discount and insurance on a theatre seat's price, "
            "read the order the wrappers run in and what the stack returns, and count the "
            "classes the same options need as subclasses."
        ),
        "key": [
            "wrap, forward, and add one thing",
            "same interface as the component",
            "stacked at run time, per object",
            "the outer wrapper runs first",
            "the order can change the result",
            "subclasses: 2ⁿ; decorators: n + 3",
            "a decorated object is not the original",
        ],
        "key_label": "Decorator in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson: the roles, and the two ways the authors contrast "
            "for changing an object."
        ),
        "concepts": [
            ("Component, ConcreteComponent and Decorator",
             "The Component is the interface; the ConcreteComponent is the object being "
             "decorated. A Decorator holds a component, conforms to the same interface, and "
             "forwards each request, doing its own work before or after; ConcreteDecorators "
             "are its subclasses, one per responsibility."),
            ("Transparent enclosure",
             "A wrapper whose interface matches what it wraps, so a client cannot tell a "
             "decorated object from a plain one. That is what lets decorators nest: a "
             "decorator can wrap another decorator, as many deep as needed."),
            ("Skin and guts",
             "The authors' contrast between changing an object from outside, with decorators "
             "(its skin), and changing it from inside, by giving it a strategy object to "
             "delegate to (its guts). The second suits a component too heavy to wrap in "
             "quantity."),
        ],
        "read_title": "The pattern, section by section, then the count",
        "read_intro": (
            "Read Decorator in your own copy first. The lesson summarises its user interface "
            "example, reads the four consequences and the implementation issues, and then "
            "counts a stack of decorators of its own."
        ),
        "body": [
            ("p", "&ldquo;Decorators provide a flexible alternative to subclassing for "
                  "extending functionality.&rdquo; That is the second sentence of the "
                  "pattern's intent; the first says it attaches responsibilities to an "
                  "object at run time. Like Adapter, it is also called Wrapper. You met it "
                  "in the case study's lesson Embellishing the User Interface, where it "
                  "puts borders round the page; here it is the catalog entry."),
            ("p", "The Motivation asks how to give one user interface component a border, or "
                  "scrolling, without giving it to every object of the class. Inheriting a "
                  "border decides statically, for every instance, and the client has no say. "
                  "The pattern instead encloses the component in another object, the "
                  "decorator, that adds the border. Because the decorator has the "
                  "component's interface, its clients do not see it, and because they do not "
                  "see it, decorators can be nested: the book's example wraps a text view in "
                  "a scrolling decorator and that in a border. A decorator may also offer "
                  "operations of its own, for clients that know it is there. Applicability "
                  "names three cases: adding responsibilities to individual objects without "
                  "affecting others; responsibilities that can be withdrawn; and extension by "
                  "subclassing that is impractical, because the independent options would "
                  "need a subclass for every combination, or because the class cannot be "
                  "subclassed."),
            ("p", "The authors count two benefits and two liabilities. It is more flexible "
                  "than static inheritance: responsibilities are attached and detached at run "
                  "time, they mix and match, and the same one can be added twice (a double "
                  "border is two border decorators), where inheritance would need a class "
                  "for each combination. It avoids classes high in the hierarchy loaded with "
                  "every feature anyone might want: you pay for the features you attach. "
                  "Against that, a decorator and its component are not the same object, so "
                  "code that relies on object identity will be surprised. And a design "
                  "built this way consists of lots of little objects that look alike and "
                  "differ only in how they are connected; easy to customise for whoever "
                  "understands it, hard to learn and to debug."),
            ("code", _lines(DECORATOR_JAVA)),
            ("p", "The Implementation section has four issues. Every decorator must conform to "
                  "the component's interface, so in C++ they share a base class. With only "
                  "one responsibility to add, the abstract Decorator can be dropped and its "
                  "forwarding merged into the one concrete decorator. The common Component "
                  "class must stay light, an interface rather than a store of data, or the "
                  "decorators become too heavy to use in numbers. And, the skin against the "
                  "guts: when the component is heavyweight, give it a list of strategy "
                  "objects instead, as MacApp and Bedrock did with their "
                  "&ldquo;adorners&rdquo; on views. Then the component knows about its "
                  "extensions, which a decorated component never does, but each strategy "
                  "can have a small interface of its own. Known Uses include toolkit "
                  "embellishments, a debugging wrapper that logs layout requests, and the "
                  "ET++ streams, where compression and conversion to seven-bit ASCII are "
                  "decorators on a file stream."),
            ("p", "Now the lab, on a theatre box office's prices. The component is a stalls "
                  "seat at 32. Three decorators wrap it, innermost first: a booking fee that "
                  "adds 2.50, a member discount that multiplies by 0.9, and insurance that "
                  "adds 1.75. Each record is decorator, operation, amount. On the preset "
                  "<code>fee-member-insurance</code> the call order is the stack's shape: "
                  "the request goes in through insurance, the member discount and the fee, "
                  "reaches the seat, and the answers come back out the other way. The "
                  "result is ((32 + 2.50) × 0.9) + 1.75 = 32.8. With the decorators in the "
                  "reverse order the lab gives 32.875, so here the order changes the result: "
                  "a discount applied after the fee discounts the fee too."),
            ("p", "The last three tiles count classes. Three on-or-off options as subclasses "
                  "need a class for every combination: 2³ = 8, the plain seat and seven "
                  "decorated versions of it. With Decorator the design has 3 + 3 = 6: the "
                  "interface, the concrete component, the abstract decorator and three "
                  "decorators. A fourth option doubles the first count, adding 8, and adds 1 "
                  "to the second. The preset <code>two-adds</code> keeps only the fee and "
                  "insurance: 36.25 in either order, because two additions commute, and 4 "
                  "classes against 5, so with two options the subclasses are actually fewer. "
                  "The subclass count assumes each combination is wanted; it is the "
                  "combinations, not the options, that make the explosion."),
            ("p", "What the count leaves out is the cost on the other side. Three decorators "
                  "on one seat are four objects where a subclass would be one, a debugger "
                  "shows all four, and a check that this price is that seat's price by "
                  "identity fails. Those are the authors' two liabilities, and they grow "
                  "with the stack."),
            ("h3", "Exercise"),
            ("code", _lines(CIRCLE_EXERCISE)),
            ("p", "A circle seat at 24 with a fee and a member discount. By hand, give the "
                  "result with the decorators in the order given and in the reverse order, "
                  "and the classes as subclasses and with Decorator. Then type the records "
                  "into the lab to check."),
            ("p", "Decorator keeps an object's interface and adds to it. The next lesson, "
                  "Facade, does the opposite for a whole subsystem: a new, smaller interface "
                  "in front of many classes."),
        ],
        "lab": ("gofkit", {
            "mode": "route",
            "view": "wrap",
            "preset": "fee-member-insurance",
            "presets": [
                {"id": "fee-member-insurance",
                 "label": "A stalls seat with a booking fee, a member discount and insurance",
                 "core": "stalls, 32",
                 "layers": "fee, add, 2.50; member, times, 0.9; insurance, add, 1.75",
                 "expect": {"grtLayers": "3", "grtCalls": "in: insurance, member, fee; core: stalls; out: fee, member, insurance", "grtResult": "32.8", "grtOther": "32.875", "grtMatters": "yes", "grtSubclass": "8 (the component + 7 combinations)", "grtDecorator": "6 (interface, component, abstract decorator + 3)", "grtAddOne": "subclassing +8, Decorator +1"}},
                {"id": "two-adds",
                 "label": "The same seat with only the fee and insurance",
                 "core": "stalls, 32",
                 "layers": "fee, add, 2.50; insurance, add, 1.75",
                 "expect": {"grtLayers": "2", "grtCalls": "in: insurance, fee; core: stalls; out: fee, insurance", "grtResult": "36.25", "grtOther": "36.25", "grtMatters": "no", "grtSubclass": "4 (the component + 3 combinations)", "grtDecorator": "5 (interface, component, abstract decorator + 2)", "grtAddOne": "subclassing +4, Decorator +1"}},
            ],
            "panel_title": "A component in a stack of decorators",
        }),
        "steps_title": "Reading a stack of decorators",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Write the stack innermost first",
             "Start from the component and list each decorator in the order it was wrapped "
             "round the last. The outermost is the one the client holds."),
            ("Trace the call in and out",
             "The request enters through the outermost decorator and reaches the component "
             "last; each decorator's own work happens on the way in or the way out."),
            ("Compute the result both ways",
             "Apply the operations from the inside out, then in the reverse order. If the "
             "results differ, the order of wrapping is part of the design."),
            ("Do it on a design of your own",
             "Take a class in your code with optional features (logging, caching, retries, "
             "formatting) and write them as decorators over one component. Count the classes "
             "as subclasses and as decorators, and say whether any feature depends on "
             "running before another."),
        ],
        "worked": {
            "title": "The seat's price, from the inside out",
            "intro": [
                "Compute the result on <code>fee-member-insurance</code>, then reverse it.",
            ],
            "lines": [
                "seat: 32",
                "fee: 32 + 2.50 = 34.50",
                "member: 34.50 × 0.9 = 31.05",
                "insurance: 31.05 + 1.75 = 32.80",
                "reversed: (32 + 1.75) × 0.9 + 2.50 = 32.875",
            ],
            "after": [
                "The client asked the insurance decorator for an amount, and the answer was "
                "built on the way back out. Swap the order and the discount no longer "
                "applies to the fee.",
            ],
        },
        "quiz_title": "Call order, results and class counts",
        "quiz": [
            {"q": "In the exercise, a circle seat at 24 with a fee of 2.50 and a member "
                  "discount of 0.9 (innermost first): what are the two results, and the "
                  "classes as subclasses and with Decorator?",
             "a": ["23.85 and 24.1; 4 against 5", "23.85 and 24.1; 3 against 5",
                   "24.1 and 23.85; 4 against 5", "23.85 and 23.85; 4 against 4"],
             "c": 0,
             "why": "In the order given, the fee is applied first: (24 + 2.50) × 0.9 = 23.85. "
                    "Reversed, the discount comes first: 24 × 0.9 + 2.50 = 24.1. Two options "
                    "as subclasses need 2² = 4 classes, the plain seat and three combinations; "
                    "with Decorator there are 2 + 3 = 5: interface, component, abstract "
                    "decorator and two decorators."},
            {"q": "On <code>fee-member-insurance</code>, which object receives the client's "
                  "request first?",
             "a": ["The stalls seat, the component", "The booking fee, the innermost decorator",
                   "The member discount, in the middle", "Insurance, the outermost decorator"],
             "c": 3,
             "why": "The client holds the outermost wrapper, insurance, which forwards to the "
                    "member discount, which forwards to the fee, which forwards to the seat. "
                    "The seat answers first, but it is reached last; the fee is applied "
                    "first because it is innermost, which is why it is listed first."},
            {"q": "Why does <code>two-adds</code> give the same result in either order?",
             "a": ["Because the lab ignores the order of add decorators",
                   "Because two additions give the same sum in either order",
                   "Because a stack of two decorators cannot be reordered",
                   "Because insurance is applied to the base price only"],
             "c": 1,
             "why": "32 + 2.50 + 1.75 and 32 + 1.75 + 2.50 are both 36.25: addition "
                    "commutes. The lab does reorder them, and with a multiplication in the "
                    "stack, as on the first preset, the result changes."},
            {"q": "Which is one of the two liabilities the authors give for Decorator?",
             "a": ["Responsibilities cannot be removed once attached",
                   "Every combination of options needs its own class",
                   "A decorator and the object it wraps are two objects, so identity "
                   "checks mislead",
                   "Decorators must know the concrete class they wrap"],
             "c": 2,
             "why": "The two liabilities are that a decorator and its component are not "
                    "identical, and that the design is made of many little look-alike objects "
                    "that are hard to learn and debug. Withdrawing a responsibility is one of "
                    "Decorator's uses; a class per combination is the subclassing it avoids; "
                    "and a decorator needs only the component's interface."},
        ],
        "mistakes": [
            ("Assuming the order of the decorators does not matter",
             "Each decorator works on what the one inside it returns, so any two that do not "
             "commute give different results in different orders. On the lesson's "
             "illustration, a discount wrapped outside the booking fee gives 32.8, and the "
             "reverse 32.875; two additions alone give the same either way."),
            ("Counting only the classes and not the objects",
             "Decorator trades classes for objects. Three options are six classes instead of "
             "eight, but every decorated seat is a chain of objects, and the authors name the "
             "result, lots of little objects, as a liability for anyone learning or "
             "debugging the system."),
            ("Decorating a heavyweight component",
             "Every decorator carries the component's whole interface. When that interface is "
             "large, the authors point to changing the guts instead: a strategy object the "
             "component delegates to, with a small interface of its own."),
        ],
        "standard": (
            "Finish when you can trace a stack of decorators and count its classes.",
            "Given a component and its decorators innermost first, state the call order, the "
            "result, whether the order changes it, and the classes as subclasses and with "
            "Decorator, and name the pattern's two liabilities."
        ),
        "note": (
            "The lab computes a stack's result and counts classes. It cannot count the cost "
            "of the objects themselves, the debugging and identity troubles the authors "
            "warn of, or tell whether your options are really independent; and it assumes "
            "every combination of options would otherwise need its own subclass."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Facade (PDF pp. 205-213 of the operator's copy): Intent and Motivation
    # p. 205, Applicability p. 206, Participants, Collaborations and
    # Consequences pp. 207-208, Implementation p. 208, Known Uses pp. 211-213,
    # Related Patterns p. 213.
    # Quote: PDF p. 205 of the operator's copy, 12 words (from the Intent),
    # quotes.py OK. Lesson total: 12 words.
    {
        "slug": "facade",
        "title": "Facade",
        "module": MODULE,
        "one_line": "One class in front of a subsystem that offers the common requests in a simpler interface and passes each to the classes that do the work.",
        "summary": (
            "Facade gives a subsystem one higher-level entry point, without hiding the "
            "classes behind it from clients that need them. Read the pattern, then count "
            "the uses between a parcel locker's three client applications and its "
            "subsystem, first going straight to the subsystem's classes and then through a "
            "facade."
        ),
        "key": [
            "one simpler interface to a subsystem",
            "clients send requests to the facade",
            "the facade forwards to the classes",
            "fewer uses across the boundary",
            "subsystem classes know nothing of it",
            "direct use is still allowed",
        ],
        "key_label": "Facade in six lines",
        "concepts_intro": (
            "Three terms carry the lesson: the roles, and the two kinds of subsystem "
            "interface the authors distinguish."
        ),
        "concepts": [
            ("Facade and subsystem classes",
             "The Facade knows which subsystem classes handle a request and passes it to "
             "them, doing a little translation of its own where needed. The subsystem "
             "classes do the work and keep no reference to the facade."),
            ("Weak coupling",
             "Few dependencies between a subsystem and its clients, so that the subsystem's "
             "classes can change without changing the clients. A facade reduces the uses "
             "that cross the subsystem's boundary to the facade itself."),
            ("Public and private subsystem interface",
             "Like a class, a subsystem has a public interface, the classes any client may "
             "use, and a private one, for those who extend it. The facade belongs to the "
             "public interface but is seldom the whole of it."),
        ],
        "read_title": "The pattern, section by section, then the count",
        "read_intro": (
            "Read Facade in your own copy first. The lesson summarises its compiler example, "
            "reads the consequences and the two implementation issues, and then counts "
            "the uses of a subsystem with and without a facade."
        ),
        "body": [
            ("p", "&ldquo;Provide a unified interface to a set of interfaces in a "
                  "subsystem.&rdquo; That is the first sentence of Facade's intent; the "
                  "second says the facade works a level above those interfaces, so the "
                  "subsystem is simpler to work with. Its argument starts from the observation that "
                  "dividing a system into subsystems reduces complexity, and that a common "
                  "aim is then to have subsystems talk to and rely on each other as "
                  "little as possible."),
            ("p", "The Motivation is a programming environment's compiler subsystem: a "
                  "scanner, a parser, the classes for the parse tree, a bytecode stream and a "
                  "builder. A few specialised tools need those classes directly; most clients "
                  "only want their code compiled. So the subsystem also offers a compiler "
                  "class that does the common thing in one call and holds the rest together, "
                  "without hiding the classes from the tools that want them. Applicability "
                  "gives three cases: a simple default view of a subsystem that has grown "
                  "complicated (patterns themselves tend to produce more and smaller classes, "
                  "the authors note, which makes a subsystem more reusable and harder to "
                  "use); many dependencies between clients and a subsystem's implementation "
                  "classes; and layering, with a facade as each layer's entry point."),
            ("p", "The participants are the Facade and the subsystem classes; the subsystem "
                  "classes do the actual work and know nothing of the facade. Clients that "
                  "use the facade need not touch the subsystem's objects at all. The "
                  "Consequences are three benefits. The facade shields clients from the "
                  "subsystem's components, so they deal with fewer objects. It promotes weak "
                  "coupling: the subsystem's own classes are often tightly bound together, "
                  "and a facade lets them change without the clients noticing, can remove "
                  "complex or circular dependencies, and cuts the rebuilding that a minor "
                  "edit to a central subsystem would otherwise trigger. And it does not "
                  "stop applications from using the subsystem's classes when they need to, so "
                  "each client can trade simplicity for the full set of options."),
            ("code", _lines(FACADE_JAVA)),
            ("p", "Two implementation issues follow. Coupling can be reduced further by making "
                  "the facade abstract, with a concrete facade for each implementation of the "
                  "subsystem, or by configuring one facade with different subsystem objects. "
                  "And a subsystem, like a class, has a public interface and a private one; "
                  "making some subsystem classes private would help, but in 1995 few "
                  "object-oriented languages could, and the authors note that the C++ "
                  "committee had just added namespaces. The Sample Code builds the "
                  "compiler facade in C++ and ends by weighing a parameter for the code "
                  "generator, sensible if there is more than one target, against "
                  "parameterizing every participant, which adds flexibility but works "
                  "against the facade's purpose of simplifying the common case. Known Uses are the Smalltalk compiler that "
                  "inspired the example, ET++'s browsing tools behind one class, and the "
                  "Choices operating system, whose virtual memory framework has a facade. "
                  "Related Patterns contrast it with Mediator, whose colleagues talk to it, "
                  "where subsystem classes do not know a facade exists, and note that a "
                  "facade is often a Singleton."),
            ("p", "Now the lab, on a parcel locker rather than the book's compiler. The "
                  "subsystem has five classes: <code>LockerBank</code>, "
                  "<code>DoorController</code>, <code>PinGenerator</code>, "
                  "<code>SmsGateway</code> and <code>Ledger</code>. Three applications use "
                  "it: a courier's app, the kiosk at the lockers and the support desk. Each "
                  "record is one use, user then used. On the preset <code>direct</code> "
                  "every client reaches into the subsystem for what it needs: the lab counts "
                  "8 classes and 12 distinct uses, so 12 of the 28 possible pairs are "
                  "connected, 3/7 or about 42.9%. The courier app has the largest fan-out, 4, and "
                  "<code>LockerBank</code> the largest fan-in, 4. Ten of the twelve uses "
                  "cross from a client into the subsystem; the other two are the "
                  "subsystem's own."),
            ("p", "On the preset <code>through-facade</code> a <code>Lockers</code> class "
                  "stands in front. The courier app and the kiosk use only "
                  "<code>Lockers</code>; the support desk uses it too, and still reads "
                  "<code>Ledger</code> directly, because the pattern does not forbid that. "
                  "The lab counts 9 classes, one more, and 10 uses, 10 of 36 pairs (5/18) or "
                  "about 27.8%. The largest fan-out is now the facade's, 4, and so is the largest "
                  "fan-in, 3: every client uses it. Count the uses that cross the boundary "
                  "yourself from the records: four, three to the facade and the desk's one "
                  "to the ledger, where there were ten. The subsystem's classes can now "
                  "change behind <code>Lockers</code>, and only the desk's one direct use "
                  "goes with them."),
            ("p", "The lab's figures are of the design as written. The facade concentrates "
                  "the fan-out in one class, which is the point and also a thing to watch: "
                  "a facade that takes on every client's special case grows into the "
                  "subsystem's whole interface again, which is the trade-off the Sample Code ends on."),
            ("h3", "Exercise"),
            ("p", "The support desk is changed to read the ledger through "
                  "<code>Lockers</code> as well, so the facade uses all five subsystem "
                  "classes. By hand, give the classes, the distinct uses, the uses that "
                  "cross from a client into the subsystem, and the facade's fan-out. Edit "
                  "the preset's records in the lab to check."),
            ("p", "Facade puts one object in front of many. The next lesson, Flyweight, goes "
                  "the other way, making very many objects affordable by sharing a few."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "coupling",
            "preset": "direct",
            "presets": [
                {"id": "direct",
                 "label": "Three clients using the locker subsystem's classes directly",
                 "edges": _records(LOCKERS_DIRECT),
                 "expect": {"dgModules": "8", "dgEdges": "12", "dgPairs": "28", "dgConnected": "3/7 ≈ 42.9%", "dgFanOut": "CourierApp 4", "dgFanIn": "LockerBank 4"}},
                {"id": "through-facade",
                 "label": "The same clients through a Lockers facade; the desk still reads the ledger",
                 "edges": _records(LOCKERS_FACADE),
                 "expect": {"dgModules": "9", "dgEdges": "10", "dgPairs": "36", "dgConnected": "5/18 ≈ 27.8%", "dgFanOut": "Lockers 4", "dgFanIn": "Lockers 3"}},
            ],
            "panel_title": "Uses across a subsystem's boundary, with and without a facade",
            "panel_intro": (
                "Each record is one use, written user, used, and each name is a class. The "
                "lab counts the classes, the distinct uses, the pairs connected either way, "
                "and the largest fan-out and fan-in. The design is the lesson's, and a "
                "count shows one consequence of putting a facade in front of a subsystem, "
                "not whether the subsystem needs one."
            ),
        }),
        "steps_title": "Measuring what a facade changes",
        "steps_intro": "Four steps, the last of them on a subsystem of your own.",
        "steps": [
            ("Draw the boundary",
             "List the subsystem's classes and the clients outside it. A facade belongs "
             "inside the boundary, with the classes it fronts."),
            ("Count the uses that cross it",
             "Count every use from a client to a class inside, before and after the facade. "
             "Leave the subsystem's own uses out: a facade does not change them."),
            ("Keep the direct uses that are needed",
             "Mark the clients that need something the facade does not offer. They may keep "
             "using the subsystem's classes; the pattern allows it."),
            ("Do it on a subsystem of your own",
             "Take a package your code reaches into from several places and write its uses as "
             "records. Count the uses that cross its boundary, then sketch the facade's few "
             "operations and count again."),
        ],
        "worked": {
            "title": "Uses across the locker subsystem's boundary",
            "intro": [
                "Count the client uses on <code>direct</code> and <code>through-facade</code>.",
            ],
            "lines": [
                "direct: courier 4 + kiosk 3 + desk 3 = 10",
                "uses inside the subsystem: 2",
                "uses in the direct design: 10 + 2 = 12",
                "facade: 3 clients → Lockers, desk → Ledger: 4",
                "uses from the facade: 4; inside: 2",
                "uses in the facade design: 4 + 4 + 2 = 10",
            ],
            "after": [
                "The uses that cross the boundary fall from ten to four. The facade's own "
                "four uses are inside it, and the two between the subsystem's classes are "
                "unchanged.",
            ],
        },
        "quiz_title": "Uses, boundaries and the authors' claims",
        "quiz": [
            {"q": "In the exercise, with the desk reading the ledger through Lockers, what "
                  "are the classes, distinct uses, uses crossing into the subsystem, and the "
                  "facade's fan-out?",
             "a": ["9 classes, 10 uses, 3 crossing, fan-out 5",
                   "9 classes, 10 uses, 4 crossing, fan-out 5",
                   "8 classes, 9 uses, 3 crossing, fan-out 5",
                   "9 classes, 11 uses, 3 crossing, fan-out 4"],
             "c": 0,
             "why": "The classes are unchanged at 9. The desk's use of Ledger becomes the "
                    "facade's, so the uses are the three clients' uses of Lockers, the "
                    "facade's five, and the subsystem's two: 10. Three cross the boundary, all "
                    "to the facade, and Lockers now uses five classes."},
            {"q": "On <code>through-facade</code>, why does the support desk still use "
                  "<code>Ledger</code>?",
             "a": ["Because the lab cannot remove a use",
                   "Because the facade must not use the ledger",
                   "Because the pattern does not prevent clients from using subsystem "
                   "classes they need",
                   "Because the ledger is outside the subsystem"],
             "c": 2,
             "why": "The authors list it as a consequence: a facade does not stop "
                    "applications from using subsystem classes when they need to, so clients "
                    "can trade simplicity for the full set of options. Ledger is one of the five "
                    "subsystem classes, and the exercise shows the facade can use it too."},
            {"q": "How do the authors distinguish Facade from Mediator?",
             "a": ["A facade centralises communication between colleague objects",
                   "Subsystem classes do not know the facade exists, while a mediator's "
                   "colleagues communicate with it",
                   "A mediator offers a simpler interface to a subsystem",
                   "A facade must be abstract, a mediator concrete"],
             "c": 1,
             "why": "Mediator abstracts arbitrary communication between colleagues, who know "
                    "it and talk to it instead of to each other, and it often adds behaviour "
                    "of its own. A facade only abstracts the interface to the subsystem's "
                    "objects, adds no new functionality, and the subsystem classes keep no "
                    "reference to it. An abstract facade is an implementation option, not a "
                    "rule."},
            {"q": "On <code>direct</code>, which class has the largest fan-in?",
             "a": ["LockerBank, used by 4", "DoorController, used by 3",
                   "CourierApp, using 4", "Ledger, used by 2"],
             "c": 0,
             "why": "LockerBank is used by the courier app, the kiosk, the support desk and "
                    "DoorController: 4. DoorController is used by the three clients, 3. The "
                    "courier app's 4 is a fan-out, the classes it uses, not the ones that use "
                    "it."},
        ],
        "mistakes": [
            ("Thinking a facade hides the subsystem",
             "The authors say plainly that it does not prevent clients from using the "
             "subsystem's classes. It offers a simpler default for most clients, and those "
             "who need more look past it. On the lesson's illustration the support desk "
             "keeps its one direct use, and the count shows it."),
            ("Expecting a facade to remove the subsystem's own coupling",
             "A facade changes the uses that cross the boundary, not the ones inside. The "
             "subsystem's classes may still be strongly bound together; the facade lets them "
             "change without the clients noticing."),
            ("Giving the facade every option the subsystem has",
             "A parameter or two can earn its place, as the code generator does in the "
             "authors' Sample Code; parameterizing every participant, they note, detracts "
             "from the facade's purpose, which is to make the common case simple. A client "
             "that needs the options can use the subsystem's classes directly."),
        ],
        "standard": (
            "Finish when you can count a subsystem's uses with and without a facade.",
            "Given clients and a subsystem as records, state the classes, the distinct uses, "
            "the uses crossing the boundary and the largest fan-out and fan-in, before and "
            "after a facade, and say what the facade does not prevent."
        ),
        "note": (
            "The lab counts uses in the design you state. It cannot tell you which requests "
            "most clients share, which is what a facade should offer, or whether a client's "
            "direct use is a need or a habit; the boundary and the facade's few operations "
            "are design decisions."
        ),
    },
]
