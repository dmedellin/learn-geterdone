"""Behavioral Patterns I, lessons 1-5 -- Chapter 5's introduction, Chain of
Responsibility, Command, Interpreter, Iterator and Mediator.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 5, Behavioral
Patterns. Pages in the comments are PDF pages of the operator's copy; the
lessons cite by chapter, section and pattern. Every quotation is copied from
that copy and checked with quotes.py. The designs, records and Java are
written for these lessons: none of the book's code, diagrams or example data
is reproduced, and no lab uses the book's examples (help handlers, menu
items, regular or Boolean expression grammars, lists of employees, the font
dialog). The design is docs/design-patterns/PLAN.md, section C, Course 5.
"""


def _lines(text):
    """A snippet or record constant as a code block's list of lines."""
    return text.split("\n")


def _records(text):
    """Records written one to a line, as the single string a lab field takes."""
    return " ".join(line.strip() for line in text.split("\n") if line.strip())


# ---------------------------------------------------------------- 5.1 designs

# A public library's help desk. Each handler names the topics it takes, in
# chain order: the self-service kiosk renews loans; the desk renews, places
# holds and takes fines; the librarian places holds, arranges inter-library
# loans and deals with lost items.
LIBRARY_CHAIN = """kiosk, renew;
desk, renew, hold, fine;
librarian, hold, ill, lost"""

LIBRARY_CHAIN_MANAGER = LIBRARY_CHAIN + """;
manager, all"""

LIBRARY_CHAIN_DESK_FIRST = """desk, renew, hold, fine;
kiosk, renew;
librarian, hold, ill, lost"""

LIBRARY_REQUESTS = "renew hold fine ill renew donate lost hold donate"

# Exercise: a bakery's order line.
BAKERY_EXERCISE = """// handlers, in chain order
counter, small;
baker, small, custom, large;
owner, custom, wholesale
// requests, in the order sent
large custom wholesale small refund custom"""

DESK_HANDLER_JAVA = """abstract class DeskHandler {
    private final DeskHandler next;     // null at the end of the chain
    DeskHandler(DeskHandler next) { this.next = next; }
    // The default passes the request on; a subclass overrides it.
    String handle(Request r) {
        if (next != null) {
            return next.handle(r);
        }
        return "unhandled: " + r.topic();   // fell off the end
    }
}
final class Kiosk extends DeskHandler {
    Kiosk(DeskHandler next) { super(next); }
    @Override String handle(Request r) {
        if (r.topic().equals("renew")) {
            return "kiosk renewed " + r.itemId();
        }
        return super.handle(r);
    }
}"""

LIBRARY_WIRING_JAVA = """// The client builds the chain and sends every request to its head.
DeskHandler librarian = new Librarian(null);
DeskHandler desk = new Desk(librarian);
DeskHandler head = new Kiosk(desk);

String reply = head.handle(new Request("hold", "B-2291"));"""


# ---------------------------------------------------------------- 5.2 designs

# A ferry's booking desk: free car spaces and foot-passenger places on one sailing.
BOX_STATE = "cars, 30; foot, 120"

BOX_COMMANDS = """car, add, cars, -1;
group, add, foot, -6;
storm, set, foot, 0;
reset, set, cars, 30"""

BOX_SCRIPT = "car car group undo undo storm redo undo undo undo redo"

BOX_SCRIPT_BACK = "car car group undo undo redo redo"

THERMOSTAT_EXERCISE = """// state, as cell, value
target, 20
// commands, as command, op, cell, amount
warm, add, target, 1;
eco, set, target, 16
// the script
warm warm eco undo warm redo undo"""

COMMANDS_JAVA = """interface Command {
    void execute();
    void undo();
}
final class TakePlaces implements Command {
    private final Deck deck;            // the receiver
    private final int places;
    TakePlaces(Deck d, int places) { this.deck = d; this.places = places; }
    public void execute() { deck.take(places); }
    public void undo()    { deck.give(places); }
}
final class CloseDeck implements Command {
    private final Deck deck;
    private int wasFree;                // what execute replaced, kept for undo
    CloseDeck(Deck d) { this.deck = d; }
    public void execute() { wasFree = deck.free(); deck.setFree(0); }
    public void undo()    { deck.setFree(wasFree); }
}"""

MACRO_JAVA = """// A macro runs its parts in order and undoes them in reverse order.
final class Macro implements Command {
    private final List<Command> parts;
    Macro(List<Command> parts) { this.parts = new ArrayList<>(parts); }
    public void execute() {
        for (Command c : parts) { c.execute(); }
    }
    public void undo() {
        for (int i = parts.size() - 1; i >= 0; i--) { parts.get(i).undo(); }
    }
}
// The invoker: a key on the booking desk, given its command by the client.
final class DeskKey {
    private Command command;
    void assign(Command c) { command = c; }
    void press() { command.execute(); }
}"""


# ---------------------------------------------------------------- 5.3 designs

# A print shop's price for a job, as a sentence in the lesson's own small
# arithmetic language. per_page is the cost of one printed page.
PRINT_EXPR = "setup + copies * (pages * per_page + binding)"
PRINT_CONTEXT = "setup, 12; copies, 20; pages, 48; per_page, 0.05; binding, 1.5; rush, 25"
PRINT_CONTEXT_MORE = "setup, 12; copies, 50; pages, 48; per_page, 0.05; binding, 1.5"

# A quiz app's score: a quarter of a mark off for each wrong answer.
QUIZ_EXPR = "(right - wrong / 4) / questions * 100"
QUIZ_CONTEXT = "right, 18; wrong, 3; questions, 20"

GRAMMAR = """expression ::= term { ( '+' | '-' ) term }
term       ::= factor { ( '*' | '/' ) factor }
factor     ::= number | name | '-' factor | '(' expression ')'"""

MUSEUM_EXERCISE = """// the expression
fee * (adults + children / 2) - discount
// the context, as name, value
fee, 8; adults, 3; children, 4; discount, 5"""

EXPR_JAVA = """interface Expr {
    BigDecimal interpret(Map<String, BigDecimal> context);
}
final class Var implements Expr {                       // a terminal
    private final String name;
    Var(String name) { this.name = name; }
    public BigDecimal interpret(Map<String, BigDecimal> c) {
        return c.get(name);
    }
}
final class Add implements Expr {                       // a nonterminal
    private final Expr left, right;
    Add(Expr left, Expr right) { this.left = left; this.right = right; }
    public BigDecimal interpret(Map<String, BigDecimal> c) {
        return left.interpret(c).add(right.interpret(c));
    }
}
// Num is a terminal like Var; Sub, Mul, Div and Neg follow Add's shape."""

PRINT_TREE_JAVA = """// The client builds the print job's tree (no parser) and interprets it.
Expr price = new Add(new Var("setup"),
        new Mul(new Var("copies"),
                new Add(new Mul(new Var("pages"), new Var("per_page")),
                        new Var("binding"))));

BigDecimal total = price.interpret(jobContext);   // 90 for the first job"""


# ---------------------------------------------------------------- 5.4 designs

# A quiz app's question bank: sections hold questions and other sections; a
# question's value is its marks.
QUIZ_TREE = """quiz, -, Section, -;
warmup, quiz, Section, -;
q1, warmup, Question, 1;
q2, warmup, Question, 2;
main, quiz, Section, -;
q3, main, Question, 3;
bonus, main, Section, -;
q4, bonus, Question, 5;
q5, main, Question, 2;
q6, quiz, Question, 1"""

ROUND_LIST = """round, -, Section, -;
a1, round, Question, 1;
a2, round, Question, 1;
a3, round, Question, 1;
a4, round, Question, 1"""

CATALOGUE_EXERCISE = """// node, parent, kind, value
catalogue, -, Shelf, -;
fiction, catalogue, Shelf, -;
f1, fiction, Book, 1;
f2, fiction, Book, 1;
science, catalogue, Shelf, -;
s1, science, Book, 1;
maps, catalogue, Book, 1"""

PREORDER_JAVA = """// An external iterator: the client asks for each node in turn.
final class PreOrder implements Iterator<Part> {
    private final Deque<Part> pending = new ArrayDeque<>();

    PreOrder(Part root) { pending.push(root); }

    public boolean hasNext() { return !pending.isEmpty(); }

    public Part next() {
        if (pending.isEmpty()) { throw new NoSuchElementException(); }
        Part p = pending.pop();
        List<Part> kids = p.children();
        for (int i = kids.size() - 1; i >= 0; i--) {
            pending.push(kids.get(i));        // the first child ends on top
        }
        return p;
    }
}"""

ITERATOR_USE_JAVA = """// External: the client drives the loop and may stop or compare.
for (Iterator<Part> it = new PreOrder(quiz); it.hasNext(); ) {
    Part p = it.next();
    if (p.name().equals("q4")) { break; }
}

// Internal: the client hands the aggregate an operation.
quiz.forEachInPreOrder(p -> print(p.name()));"""


# ---------------------------------------------------------------- 5.5 designs

# A bakery's online order form for a celebration cake: five fields whose
# behaviour depends on one another (a flavour sets the earliest pickup day and
# the price; a pickup tomorrow adds a rush fee; a long message needs a larger
# size).
FORM_FIELDS = "size flavour pickup message price"
FORM_FIELDS_BIGGER = "size flavour pickup message price candles box allergens"

MEDIATOR_JAVA = """interface OrderForm {                 // the Mediator
    void changed(Field source);
}
abstract class Field {                  // a Colleague: knows only the form
    private final OrderForm form;
    Field(OrderForm form) { this.form = form; }
    protected void changed() { form.changed(this); }
}
final class CakeOrderForm implements OrderForm {   // the ConcreteMediator
    private Flavour flavour; private Pickup pickup; private Price price;
    // ... create() makes the fields and keeps a reference to each
    public void changed(Field source) {
        if (source == flavour) {
            pickup.setEarliestDay(flavour.chosen().leadDays());
            price.setBase(flavour.chosen().cost());
        } else if (source == pickup) {
            price.setRushFee(pickup.daysAhead() < 2);
        }
    }
}"""

STUDIO_EXERCISE = """// a recording studio's mixing desk: seven controls
// that all affect one another
fader mute solo pan eq send meter"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 5, introduction (PDF pp. 241-242 of the operator's copy) and
    # Chain of Responsibility (pp. 243-252).
    # Quote: PDF p. 243 of the operator's copy, the Intent's first sentence,
    # 22 words, quotes.py OK. Lesson total: 22 words.
    {
        "slug": "chain-of-responsibility",
        "title": "Chain of Responsibility",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "A request passed along a line of candidate handlers until one takes it, so the sender never needs to know which object will.",
        "summary": (
            "Chapter 5 opens with what behavioral patterns are, and its first pattern "
            "sends a request along a chain of objects that might handle it. Read how "
            "the chain decouples the sender from the receiver and what it costs, then "
            "send a library help desk's requests down a chain of handlers and count "
            "who takes each, how often each is passed on, and which fall off the end."
        ),
        "key": [
            "the sender knows only the head of the chain",
            "each handler takes it or passes it on",
            "a request has an implicit receiver",
            "order decides who takes a request",
            "receipt is not guaranteed",
            "a last handler that takes all guarantees it",
        ],
        "key_label": "Chain of Responsibility in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's own division "
            "of its patterns; the other two are the pattern's."
        ),
        "concepts": [
            ("Behavioral pattern",
             "A pattern about algorithms and about which object is responsible for "
             "what, and so about how objects communicate. Class patterns of this kind "
             "spread behaviour over a hierarchy by inheritance (Template Method, "
             "Interpreter); object patterns spread it over objects joined by "
             "composition (the other nine)."),
            ("Implicit receiver",
             "The object that will in the end deal with a request, unknown to the "
             "object that sends it. The sender holds a reference to the first handler "
             "only, and which handler takes the request is settled as it travels."),
            ("Successor",
             "The next handler on the chain, the one a handler passes a request to "
             "when it does not take it itself. The link may be a field added for the "
             "purpose or a reference the design already has, such as a part's "
             "parent."),
        ],
        "read_title": "The chapter's opening, then the pattern, then the count",
        "read_intro": (
            "Read the two-page introduction to Chapter 5 and the whole of Chain of "
            "Responsibility in your own copy first. The lesson reads the introduction "
            "as a map of the chapter and the pattern as a tool, and then counts a "
            "chain."
        ),
        "body": [
            ("p", "&ldquo;Avoid coupling the sender of a request to its receiver by giving "
                  "more than one object a chance to handle the request.&rdquo; That is the "
                  "first sentence of Chain of Responsibility's Intent, the pattern that opens "
                  "the catalog's Chapter 5, Behavioral Patterns. This lesson reads the "
                  "chapter's short introduction and then the pattern, section by section. "
                  "Read both in your own copy first; the book's own samples, here as "
                  "everywhere, are in C++ and Smalltalk, and the sketches below are Java "
                  "written for the lesson."),
            ("p", "The introduction says what the chapter's eleven patterns share. They are "
                  "about algorithms and the division of responsibility between objects, and "
                  "so about the way objects talk to each other: control flow that is hard to "
                  "follow when the program runs is described instead as a pattern of "
                  "connections. Two of them are class patterns, which use inheritance: "
                  "Template Method, an algorithm written once with steps a subclass fills "
                  "in, and Interpreter, which turns the rules of a language into classes. The rest are object "
                  "patterns. Mediator puts one object between peers that would otherwise "
                  "know each other; Chain of Responsibility loosens the coupling further; "
                  "Observer keeps dependents informed of a change; and Strategy, Command, "
                  "State, Visitor and Iterator each wrap a piece of behaviour in an object "
                  "and delegate to it. The chapter runs in alphabetical order, and this "
                  "course reads its first six patterns."),
            ("p", "The pattern's motivating example is context-sensitive help in a user "
                  "interface. A user clicks on some part of a window for help; if that part "
                  "has none of its own, the help should come from whatever encloses it, and "
                  "so on outwards to the application. The button that receives the click "
                  "cannot know which object will answer. So every candidate shares one "
                  "interface for handling the request and knows its successor, and the "
                  "request moves outwards from the most specific candidate until one of them "
                  "deals with it."),
            ("p", "Stated as you would apply it: a Handler declares the operation that "
                  "handles a request and, usually, holds the link to the next handler; each "
                  "ConcreteHandler takes the requests it is responsible for and passes every "
                  "other one to its successor; the Client sends the request to a handler on "
                  "the chain, normally the first, and knows no more than that. The default "
                  "implementation in the Handler simply forwards, so a subclass with no "
                  "interest in a request need not mention it."),
            ("code", _lines(DESK_HANDLER_JAVA)),
            ("p", "The authors give three situations for the pattern: several objects could "
                  "deal with a request, none is known in advance, and the right one should "
                  "be found without the sender choosing; the sender should not have to name "
                  "the receiver at all; and the candidates should be assembled while the "
                  "program runs. The second sketch shows that last point: the chain is three "
                  "constructor calls, and a different chain is three different ones."),
            ("code", _lines(LIBRARY_WIRING_JAVA)),
            ("p", "The consequences cut both ways, and the book states both. Coupling is "
                  "reduced: the sender and the receiver know nothing of each other, and a "
                  "handler keeps one reference, to its successor, instead of references to "
                  "every candidate. Responsibilities can be added or moved by changing the "
                  "chain while the program runs. The liability is that receipt is not "
                  "guaranteed: with no explicit receiver, a request can reach the end of "
                  "the chain unhandled, and a chain built wrongly drops requests it was "
                  "meant to serve."),
            ("p", "Among the implementation issues, two matter most here. The successor "
                  "links can be new fields, as in the sketch, or existing references, such "
                  "as a part's parent in a Composite, which saves space when the existing "
                  "structure is the chain you want. And requests can be represented three "
                  "ways: as a fixed operation per kind of request, which is safe but closed; "
                  "as one operation taking a request code, which is open-ended but needs "
                  "conditional dispatch and parameters packed by hand; or as request "
                  "objects, one class per kind, that carry their own parameters. The "
                  "book's Sample Code builds the help example with a help-topic handler "
                  "class; its Known Uses are the event handlers of several 1990s class "
                  "libraries (NeXT's AppKit calls the class Responder) and graphical "
                  "update in ET++. Its Related Patterns section names Composite, whose "
                  "parent links often form the chain."),
            ("p", "Now the lab, on a public library's help desk. The preset "
                  "<code>library</code> has three handlers in chain order: a self-service "
                  "kiosk that renews loans; the desk, which renews, places holds and takes "
                  "fines; and a librarian, who places holds, arranges inter-library loans "
                  "(<code>ill</code>) and deals with lost items. Nine requests are sent to "
                  "the kiosk. The lab reports 7 of 9 handled: the kiosk takes 2, the desk "
                  "3 and the librarian 2, so the desk is the busiest handler. Requests are "
                  "passed on 11 times in all, a request taken by the k-th handler having "
                  "been passed k − 1 times. Two requests, the donations at positions 6 and "
                  "9, are taken by nobody: each is passed on twice and falls off the end. "
                  "That is the liability in a number."),
            ("p", "The preset <code>library-manager</code> adds a manager who takes "
                  "everything (<code>all</code>) at the end of the chain. Now 9 of 9 are "
                  "handled and nothing is unhandled; the two donations each travel three "
                  "hops to reach the manager, so the hops rise to 13. A catch-all handler "
                  "is one answer to the guarantee the pattern does not give. The preset "
                  "<code>library-desk-first</code> keeps the first three handlers and puts "
                  "the desk ahead of the kiosk. The kiosk now takes nothing, because every "
                  "renewal stops at the desk, which takes 5; the hops fall to 8. The order "
                  "of the chain decides who does the work, and the sender cannot see it."),
            ("h3", "Exercise"),
            ("code", _lines(BAKERY_EXERCISE)),
            ("p", "A bakery's order line, in the lab's form. By hand, trace each of the six "
                  "requests from the counter onwards: who takes it and how many times it was "
                  "passed on. Give the total hops, the handled count and the unhandled "
                  "requests, then type the records into the lab to check. Then move the "
                  "owner to the front and say which handler loses work."),
            ("p", "A request here is only a topic word. The next lesson, Command, makes the "
                  "request itself an object that can be stored, queued and undone."),
        ],
        "lab": ("gofkit", {
            "mode": "route",
            "view": "chain",
            "requests": LIBRARY_REQUESTS,
            "preset": "library",
            "presets": [
                {"id": "library",
                 "label": "A library help desk: kiosk, desk, librarian",
                 "handlers": _records(LIBRARY_CHAIN),
                 "expect": {"grtRequests": "9", "grtHandled": "7 of 9", "grtHops": "11",
                            "grtUnhandled": "2: donate (6), donate (9)",
                            "grtPer": "kiosk 2, desk 3, librarian 2",
                            "grtBusiest": "desk, 3 requests"}},
                {"id": "library-manager",
                 "label": "The same chain with a manager who takes everything",
                 "handlers": _records(LIBRARY_CHAIN_MANAGER),
                 "expect": {"grtHandled": "9 of 9", "grtHops": "13",
                            "grtUnhandled": "0: none",
                            "grtPer": "kiosk 2, desk 3, librarian 2, manager 2",
                            "grtBusiest": "desk, 3 requests"}},
                {"id": "library-desk-first",
                 "label": "The desk moved ahead of the kiosk",
                 "handlers": _records(LIBRARY_CHAIN_DESK_FIRST),
                 "expect": {"grtHandled": "7 of 9", "grtHops": "8",
                            "grtPer": "desk 5, kiosk 0, librarian 2",
                            "grtBusiest": "desk, 5 requests"}},
            ],
            "panel_title": "Requests down a chain of handlers",
        }),
        "steps_title": "Tracing a chain by hand",
        "steps_intro": "Four steps, the last of them on a chain of your own.",
        "steps": [
            ("Write the chain in order",
             "List the handlers from the head of the chain to its end, each with the "
             "kinds of request it takes. A handler that takes everything goes last, or "
             "nothing after it is ever reached."),
            ("Walk each request",
             "Start every request at the head. At each handler, ask whether it takes "
             "that kind; if not, pass it on and count one hop. A request taken by the "
             "k-th handler has made k − 1 hops."),
            ("Mark what falls off the end",
             "A request no handler takes has been passed on by every handler but the "
             "last and is then dropped. List each one with its position; that list is "
             "what the pattern does not guarantee."),
            ("Do it on a chain of your own",
             "Take a chain you know: servlet filters, middleware in a web framework, an "
             "escalation rota, a logger hierarchy. Write its handlers in order with what "
             "each takes, send it five requests, and say which request reaches the end "
             "and what the system does then."),
        ],
        "worked": {
            "title": "Nine requests at the library desk",
            "intro": [
                "Trace the preset <code>library</code>: kiosk, desk, librarian.",
            ],
            "lines": [
                "renew, twice: the kiosk takes it, 0 hops",
                "hold, twice: the desk takes it, 1 hop",
                "fine: the desk takes it, 1 hop",
                "ill: two passes, the librarian takes it, 2 hops",
                "lost: the librarian takes it, 2 hops",
                "donate, twice: 2 hops, then off the end",
                "hops: 0 + 0 + 1 + 1 + 1 + 2 + 2 + 2 + 2, so 11",
                "handled 7 of 9; the desk takes 3",
            ],
            "after": [
                "The lab's figures are these. A catch-all at the end turns the two "
                "donations into two handled requests of three hops each, which is the "
                "preset <code>library-manager</code>'s 13.",
            ],
        },
        "quiz_title": "Chains, hops and the pattern's trade-offs",
        "quiz": [
            {"q": "In the exercise, counting one hop each time a handler passes a request "
                  "on, and an unhandled request as passed on by every handler but the last, "
                  "what are the total hops and the unhandled requests?",
             "a": ["7 hops; refund (5) is unhandled",
                   "5 hops; refund (5) is unhandled",
                   "8 hops; refund (5) is unhandled",
                   "7 hops; nothing is unhandled"],
             "c": 0,
             "why": "large goes counter to baker, 1 hop; custom 1; wholesale passes the "
                    "counter and the baker, 2; small is taken at once, 0; refund is passed "
                    "on by the counter and the baker and falls off the end, 2; the last "
                    "custom 1. That is 1 + 1 + 2 + 0 + 2 + 1 = 7, with 5 of 6 handled. Five "
                    "leaves out the unhandled request's hops; eight counts its fall off the "
                    "end as a third. With the owner first, the owner takes both customs and "
                    "the baker loses two of its three requests."},
            {"q": "On the preset <code>library-desk-first</code>, why does the kiosk take "
                  "no requests at all?",
             "a": ["The kiosk takes no kind of request in that chain",
                   "The desk, now ahead of it, also takes renewals, so none reach the kiosk",
                   "A chain may not have two handlers that take the same kind",
                   "Requests start at the last handler, and the librarian takes them"],
             "c": 1,
             "why": "The kiosk still takes renewals, but a request stops at the first "
                    "handler that takes it, and the desk now comes first and renews too. "
                    "Two handlers may share a kind (the desk and librarian both take holds); "
                    "the chain's order decides which of them does."},
            {"q": "Which of these is a liability of Chain of Responsibility that the authors "
                  "list in its Consequences?",
             "a": ["The sender must hold a reference to every candidate receiver",
                   "The chain cannot be changed once the program is running",
                   "A request can reach the end of the chain without being handled",
                   "Every handler must handle every kind of request"],
             "c": 2,
             "why": "Receipt isn't guaranteed: with no explicit receiver, a request may pass "
                    "every handler and be dropped, and a badly assembled chain loses requests "
                    "it was meant to serve. The "
                    "other three contradict the pattern: the sender knows only one handler, "
                    "the chain can be rearranged while the program runs, and a handler forwards what it "
                    "does not take."},
            {"q": "In Implementation, what do the authors say a single handler operation "
                  "taking a request code buys, and at what price?",
             "a": ["Safety and convenience, at the price of a fixed set of requests",
                   "An open-ended set of requests, at the price of conditional dispatch and "
                   "parameters packed by hand",
                   "Type-safe parameters, at the price of one subclass per request",
                   "Automatic forwarding, at the price of Smalltalk's doesNotUnderstand"],
             "c": 1,
             "why": "A request code lets sender and receiver agree on any set of requests, "
                    "but the handler must switch on the code and parameters lose their "
                    "types. The first answer describes a hard-coded operation per request; "
                    "the third, request objects; the fourth, the Smalltalk forwarding "
                    "technique, a separate issue."},
        ],
        "mistakes": [
            ("Assuming every request sent down a chain gets handled",
             "The authors list it as a liability: the request has no explicit receiver, "
             "so nothing guarantees one takes it, and a misconfigured chain drops "
             "requests silently. On the lesson's illustration two donations are passed "
             "on twice and then lost; a handler that takes everything at the end is one "
             "way to make receipt certain, and deciding what it should do is a design "
             "question the count does not answer."),
            ("Putting the catch-all handler anywhere but last",
             "A handler that takes every request stops every request, so any handler "
             "after it is never reached. Put a general handler at the end of the chain, "
             "the way the book's help example ends with the application."),
            ("Reading the chain as the sender's choice",
             "The sender picks only where the request starts. Which handler takes it "
             "depends on the order of the chain, which can change at run time: moving "
             "the desk ahead of the kiosk takes all the renewals from the kiosk, with no "
             "change to any sender."),
        ],
        "standard": (
            "Finish when you can trace requests down a chain and say what it costs.",
            "Given a chain and a stream of requests, name the handler that takes each, "
            "total the hops, list the unhandled requests, and state the pattern's two "
            "benefits and its liability in the authors' terms."
        ),
        "note": (
            "The lab counts hops and handlers on the chain stated. It cannot tell "
            "whether a request should have a known receiver after all, what an "
            "unhandled request ought to do, or whether a chain is the right shape for "
            "your handlers; those are the judgements the pattern's Applicability asks "
            "you to make."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Command (PDF pp. 253-262 of the operator's copy).
    # Quote: PDF p. 255 of the operator's copy, Applicability, 7 words,
    # quotes.py OK. Lesson total: 7 words.
    {
        "slug": "command",
        "title": "Command",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "A request turned into an object, so it can be handed around, queued, logged, and undone and redone from a history.",
        "summary": (
            "Command wraps a request in an object with an execute operation, so the "
            "object that triggers it need not know what it does. Read the pattern's "
            "participants, its uses and the work undo takes, then run a ferry "
            "booking desk's commands, undos and redos, and count the two "
            "stacks, the state, and the redo history a new command throws away."
        ),
        "key": [
            "a request becomes an object",
            "the invoker knows only execute",
            "the receiver knows how to do it",
            "undo pops one stack, pushes the other",
            "any new command clears the redo stack",
            "a command may need its own copy",
        ],
        "key_label": "Command in six lines",
        "concepts_intro": "Three terms from the pattern carry the lesson.",
        "concepts": [
            ("Receiver",
             "The object that knows how to carry out the work, such as the deck of "
             "a ferry whose free places change. Any class can be a receiver; a command holds a "
             "reference to it and calls it."),
            ("Invoker",
             "The object that asks a command to execute: a button, a menu item, a "
             "scheduler, a history. It knows the Command interface and nothing about "
             "what any particular command does or to whom."),
            ("History list",
             "The record of executed commands that makes multi-level undo and redo "
             "possible. Undo walks it backwards, reversing each command; redo walks it "
             "forwards, executing each again. Its length limits how far back you can go."),
        ],
        "read_title": "The pattern first, then the undo it makes possible, then the count",
        "read_intro": (
            "Read Command in your own copy first, all of it. The lesson reads the "
            "pattern as a tool, then turns to undo and redo and counts a history."
        ),
        "body": [
            ("p", "&ldquo;Commands are an object-oriented replacement for callbacks.&rdquo; "
                  "The sentence is from Command's Applicability, and it is the quickest way "
                  "into the pattern: where a procedural program registers a function to be "
                  "called later, Command registers an object. This lesson reads the "
                  "pattern section by section. Read it in your own copy first."),
            ("p", "The motivation is a toolkit's problem. Buttons and menus must do "
                  "something when chosen, yet the toolkit's authors cannot know what, or to "
                  "which object: only the application that uses the toolkit knows. So the "
                  "request itself becomes an object. An abstract Command declares an "
                  "execute operation; each concrete subclass stores a receiver and a "
                  "particular action on it. The book's menu items each hold a command, "
                  "commands such as paste and open do different work behind the same "
                  "interface, and a macro command runs a sequence of other commands and "
                  "has no receiver of its own."),
            ("p", "The participants, as you would apply them: the Command declares the "
                  "interface; a ConcreteCommand binds a Receiver to an action and "
                  "implements execute by calling the receiver; the Client creates the "
                  "concrete command and gives it its receiver; the Invoker holds the "
                  "command and calls execute when the time comes. The invoker and the "
                  "receiver never meet. A menu and a toolbar button can share one command "
                  "object, and the command can be swapped while the program runs."),
            ("code", _lines(COMMANDS_JAVA)),
            ("p", "The authors list five uses. A command lets you configure an object with "
                  "what it should do, as the desk key below is configured. A command made "
                  "now can run later, wait in a queue, or travel to another process. With "
                  "a second operation that reverses the first, it can be undone. Written "
                  "to disk and read back, a log of commands can be replayed after a crash. "
                  "And a system's large operations can be composed of small ones, the way "
                  "transactions are. Undo is where the pattern's details are, and it is "
                  "what the lab counts: a history keeps two stacks, pushing each executed "
                  "command on the first, moving it to the second when it is undone, and "
                  "back when it is redone."),
            ("code", _lines(MACRO_JAVA)),
            ("p", "The consequences are short in the book: the invoker is decoupled from "
                  "the receiver; commands are objects like any other and can be extended "
                  "and handled as such; they can be put together into composite commands, "
                  "an instance of Composite; and a new command is a new class that changes "
                  "no existing one. The costs are in the Implementation section. How much "
                  "a command should know is a range: at one end it only binds a receiver "
                  "to an action, at the other it does all the work itself, and in between "
                  "it finds its receiver when it runs. To be undone, a command may need to "
                  "keep the receiver, the arguments, and whatever values in the receiver "
                  "execute replaces, as <code>CloseDeck</code> keeps "
                  "<code>wasFree</code>. The macro shows the composite case: it has no "
                  "receiver of its own, and it must undo its parts in the reverse of the "
                  "order it ran them."),
            ("p", "Two further issues bite in practice. A command whose state varies "
                  "between runs, like <code>CloseDeck</code>, must be copied before it "
                  "goes on the history list, or the next run of the same object overwrites "
                  "the value an earlier undo needs; such a command acts as a Prototype. "
                  "And repeated execute and undo can accumulate errors until the state "
                  "drifts from where it started, which the authors call hysteresis; storing "
                  "more in the command, through a Memento, is their remedy. The Sample "
                  "Code builds open, paste, a C++ template for simple commands, and the "
                  "macro command; the Known Uses run from Lieberman's 1985 paper and "
                  "MacApp's undoable operations to InterViews and Unidraw. Related "
                  "Patterns: Composite for macros, Memento for undo state, Prototype for "
                  "copied commands. Course 2's User Operations lesson met the same pattern "
                  "in Lexi; this one reads the pattern itself."),
            ("p", "Now the lab, on a ferry's booking desk with 30 free car spaces and 120 "
                  "foot-passenger places on one sailing. Four commands: <code>car</code> "
                  "takes 1 car space, <code>group</code> takes 6 foot places, "
                  "<code>storm</code> sets the foot places to 0 and <code>reset</code> sets "
                  "the car spaces back to 30. On the preset <code>ferry</code> the script "
                  "runs two <code>car</code>s and a <code>group</code>, undoes two of them, "
                  "and then runs <code>storm</code>. That new command discards the 2 entries "
                  "on the redo stack, so the redo straight after it is refused. Three undos "
                  "follow, the last refused with nothing left to undo, and a final redo "
                  "re-runs <code>car</code>. The lab ends with cars 29 and foot 120, an undo "
                  "stack of 1 (<code>car</code>), a redo stack of 1 (<code>storm</code>), one "
                  "undo and one redo refused, and 2 entries discarded."),
            ("p", "The preset <code>ferry-back</code> runs the same three commands, undoes "
                  "two and redoes both, with no new command in between. Nothing is "
                  "discarded and nothing refused: the state returns to cars 28, foot 114, "
                  "with all 3 commands on the undo stack and the redo stack empty. Both "
                  "presets also show what the history holds. Under the inverse scheme an "
                  "<code>add</code> is undone by subtracting and stores nothing, while a "
                  "<code>set</code> keeps the one value it replaced: 1 value at the end of "
                  "<code>ferry</code>, none on <code>ferry-back</code>. The tile under the "
                  "other scheme gives full snapshots for comparison, the subject "
                  "of the lesson Memento."),
            ("h3", "Exercise"),
            ("code", _lines(THERMOSTAT_EXERCISE)),
            ("p", "A thermostat with two commands. By hand, step through the seven entries "
                  "of the script, writing the target and both stacks after each, and note "
                  "where the redo history is discarded and which entry is refused. Then "
                  "type it into the lab to check, and say what the redo would have done "
                  "had the <code>warm</code> after the undo not run."),
            ("p", "A command here changes one number. The next lesson, Interpreter, turns "
                  "to a whole small language whose sentences are trees of objects."),
        ],
        "lab": ("gofkit", {
            "mode": "history",
            "view": "undo",
            "state": BOX_STATE,
            "commands": _records(BOX_COMMANDS),
            "preset": "ferry",
            "presets": [
                {"id": "ferry",
                 "label": "A ferry booking desk: a new command after two undos",
                 "script": BOX_SCRIPT,
                 "expect": {"ghiFinal": "cars 29, foot 120", "ghiUndo": "1: car",
                            "ghiRedo": "1: storm", "ghiRefused": "undo 1, redo 1",
                            "ghiDiscarded": "2", "ghiStored": "1",
                            "ghiOther": "snapshot: 4"}},
                {"id": "ferry-back",
                 "label": "The same commands undone and redone, nothing new",
                 "script": BOX_SCRIPT_BACK,
                 "expect": {"ghiFinal": "cars 28, foot 114",
                            "ghiUndo": "3: car, car, group", "ghiRedo": "0: none",
                            "ghiRefused": "undo 0, redo 0", "ghiDiscarded": "0",
                            "ghiStored": "0", "ghiOther": "snapshot: 6"}},
            ],
            "panel_title": "Commands, undo and redo on a small state",
        }),
        "steps_title": "Running a history by hand",
        "steps_intro": "Four steps, the last of them on an application of your own.",
        "steps": [
            ("Write the state and the commands",
             "Write each cell's starting value, and each command with what it does to "
             "which cell. For a command that sets a value, note that undo needs the value "
             "it replaced."),
            ("Keep two stacks",
             "Executing a command pushes it on the undo stack. Undo pops the top, "
             "reverses it and pushes it on the redo stack; redo pops the redo stack, "
             "executes again and pushes back. An undo or redo on an empty stack does "
             "nothing."),
            ("Clear the redo stack on a new command",
             "When a command is executed after some undos, the redo stack is emptied: "
             "the undone commands belonged to a future that will not happen now. Count "
             "what is discarded."),
            ("Do it on an application of your own",
             "Pick an editor or tool you use. Make three changes, undo two, make a new "
             "change, and try to redo. Say what the redo did, and whether that "
             "application keeps a branching history or discards the redo stack."),
        ],
        "worked": {
            "title": "The ferry script, step by step",
            "intro": [
                "Trace the preset <code>ferry</code> from cars 30, foot 120.",
            ],
            "lines": [
                "car, car: cars 29, then 28",
                "group: foot 114; undo stack car, car, group",
                "undo, undo: foot 120, cars 29; redo stack group, car",
                "storm: foot 0; the 2 redo entries are discarded",
                "redo: refused, nothing to redo",
                "undo, undo: foot 120, cars 30; redo stack storm, car",
                "undo: refused, nothing to undo",
                "redo: cars 29; undo stack car, redo stack storm",
            ],
            "after": [
                "The final state is cars 29, foot 120. The history holds one "
                "<code>add</code> and one <code>set</code>; only the <code>set</code> "
                "needs a stored value, so the inverse scheme keeps 1.",
            ],
        },
        "quiz_title": "Commands, stacks and the pattern's details",
        "quiz": [
            {"q": "In the exercise, what is the final target, and what are the undo and "
                  "redo stacks, bottom to top?",
             "a": ["22; undo: warm, warm; redo: warm",
                   "23; undo: warm, warm, warm; redo: none",
                   "23; undo: warm, warm, warm; redo: eco",
                   "16; undo: warm, warm, eco; redo: warm"],
             "c": 0,
             "why": "warm, warm: 22. eco: 16. undo: 22, redo stack eco. warm: 23, and the "
                    "new command discards eco. redo: refused, the stack is empty. undo: 22, "
                    "undo stack warm, warm, redo stack warm. The second answer stops before "
                    "the last undo; the third keeps eco on the redo stack, as if a new "
                    "command did not clear it, so the redo sets 16 and the last undo "
                    "takes it back to 23; the fourth leaves eco in force. Had the "
                    "warm after the undo not run, the redo would have re-run eco and set "
                    "the target to 16."},
            {"q": "On the preset <code>ferry</code>, how many redo entries does "
                  "<code>storm</code> discard?",
             "a": ["0: redo entries are kept until a redo uses them",
                   "1: only the last undone command",
                   "2: group and car, both undone just before",
                   "3: every command run so far"],
             "c": 2,
             "why": "The two undos before it moved group and then car onto the redo stack. "
                    "Executing a new command empties that stack, so both are discarded, and "
                    "the redo straight after is refused. The first car stays on the undo "
                    "stack; it was never undone."},
            {"q": "Why, according to Implementation, may an undoable command have to be "
                  "copied before it is put on the history list?",
             "a": ["Because a history list can hold only one reference to each class",
                   "Because the same command object will run again later, and state it "
                   "keeps for undo would be overwritten",
                   "Because a command's receiver is deleted after it executes",
                   "Because copying is the only way to support redo"],
             "c": 1,
             "why": "A menu item reuses its command object. If execute stores something "
                    "that varies, such as the value it replaced, the next execution "
                    "overwrites it, so a copy goes on the list; a command that keeps no "
                    "varying state need not be copied, and only a reference is stored. Such "
                    "copied commands act as prototypes."},
            {"q": "What do the authors mean by hysteresis in an undo mechanism?",
             "a": ["A redo stack that grows longer than the undo stack",
                   "Errors that build up over repeated execution and undoing, so the state "
                   "drifts from its original values",
                   "The delay between queuing a command and executing it",
                   "Two invokers executing the same command at once"],
             "c": 1,
             "why": "Hysteresis is the accumulation of errors as commands are executed, "
                    "undone and executed again, until the state no longer matches where it "
                    "began. The remedy they give is to store more in the command, through "
                    "Memento, so the exact earlier state can be restored."},
        ],
        "mistakes": [
            ("Keeping the redo stack after a new command",
             "Once you undo and then do something new, the undone commands describe "
             "changes made to a state that no longer exists; redoing them would apply "
             "them to the wrong state. The usual history list, the one the book "
             "describes and the lab counts, empties the redo stack on every new command. "
             "On the lesson's illustration <code>storm</code> discards two entries and "
             "the next redo is refused."),
            ("Putting the same command object on the history twice",
             "A command that remembers what it replaced, like <code>CloseDeck</code>, "
             "overwrites that memory each time it runs. If one instance is pushed twice, "
             "undoing the earlier run restores the wrong value. The authors' answer is to "
             "copy such a command before it goes on the list."),
            ("Thinking an undo needs a full copy of the state",
             "A command can undo itself from much less: an addition by subtracting, a "
             "set from the one value it replaced. Full snapshots are an alternative "
             "with its own costs, which the lesson Memento counts; the authors suggest "
             "them where reversing is not exact."),
        ],
        "standard": (
            "Finish when you can run a history of commands by hand.",
            "Given a state, a set of commands and a script, give the state and both "
            "stacks after every step, the refused undos and redos and the discarded "
            "redo entries, and name the participants of the pattern in a design you "
            "know."
        ),
        "note": (
            "The lab runs commands on whole numbers whose undo is exact. It cannot show "
            "hysteresis, macro commands, a command queue or a log replayed after a "
            "crash, and it does not say which of the pattern's uses your design needs."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Interpreter (PDF pp. 263-275 of the operator's copy).
    # Quote: PDF p. 275 of the operator's copy, Known Uses, 24 words,
    # quotes.py OK. Lesson total: 24 words.
    {
        "slug": "interpreter",
        "title": "Interpreter",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "A class for each rule of a small language, so that a sentence is a tree of objects and interpreting it is one call on the root.",
        "summary": (
            "Interpreter represents each rule of a simple grammar as a class, so a "
            "sentence becomes an abstract syntax tree that evaluates itself. Read when "
            "the pattern fits and when a grammar outgrows it, then interpret sentences "
            "of a small arithmetic language in a context and count the nodes by class, "
            "the interpret calls and the tree's depth."
        ),
        "key": [
            "one class for each grammar rule",
            "a sentence is a tree of objects",
            "terminals end the recursion",
            "the context holds what is global",
            "one interpret call per node",
            "parsing is left to someone else",
        ],
        "key_label": "Interpreter in six lines",
        "concepts_intro": "Three terms carry the lesson, all of them the pattern's.",
        "concepts": [
            ("Abstract syntax tree",
             "A sentence of the language held as a tree of objects: each operator a node "
             "whose children are its operands, each number or name a leaf. Brackets and "
             "spacing in the written sentence leave no node; the tree's shape records "
             "what they meant."),
            ("Terminal and nonterminal expression",
             "A TerminalExpression stands for a symbol that is not broken down further, "
             "here a number or a name, and interprets itself directly. A "
             "NonterminalExpression stands for a rule built from other symbols, here an "
             "operator, and interprets itself by interpreting its children."),
            ("Context",
             "Information global to the interpretation, passed to every node: here the "
             "value of each name. The same tree interpreted in another context gives "
             "another result."),
        ],
        "read_title": "The pattern first, then a small language, then the count",
        "read_intro": (
            "Read Interpreter in your own copy first, including its Sample Code's "
            "closing remarks. The lesson reads the pattern as a tool, defines a small "
            "language of its own, and counts its trees."
        ),
        "body": [
            ("p", "&ldquo;But the Interpreter pattern should be reserved for those cases in "
                  "which you want to think of the class hierarchy as defining a "
                  "language.&rdquo; The authors write that near the end of Interpreter, after "
                  "conceding that almost any operation spread over a Composite could be "
                  "called an interpreter. It is the pattern's boundary, and a good place to "
                  "start. This lesson reads the pattern section by section; read it in "
                  "your own copy first."),
            ("p", "The motivation: when the same sort of problem keeps coming back, "
                  "describing each case in a small language and evaluating the "
                  "descriptions can beat writing a fresh algorithm each time. The book's example is matching strings "
                  "against patterns, with a grammar of five classes for regular "
                  "expressions, one per rule, and an interpret operation on each that "
                  "matches the next part of the input. This lesson uses a language of its "
                  "own instead: arithmetic over named values, enough to price a print job "
                  "or score a quiz."),
            ("code", _lines(GRAMMAR)),
            ("p", "The pattern, stated as you would apply it. An AbstractExpression declares "
                  "the interpret operation. A TerminalExpression implements it for a symbol "
                  "that is not decomposed, such as a number or a name; a "
                  "NonterminalExpression class exists for each rule built from other "
                  "symbols, holds an AbstractExpression for each, and implements interpret "
                  "by interpreting them. A Context carries what every node may need. The "
                  "Client builds the sentence's tree, or is given it, sets up the context "
                  "and calls interpret on the root; each nonterminal then calls its "
                  "children, and the terminals end the recursion."),
            ("code", _lines(EXPR_JAVA)),
            ("p", "In the authors' view the pattern suits a simple grammar, and a program "
                  "where speed is not the first concern. Its benefits are that the grammar is easy to "
                  "change and extend, since each rule is a class that can be subclassed, "
                  "and easy to implement, since the node classes are alike and could be "
                  "generated; and that a new way of interpreting, such as printing or "
                  "type-checking a sentence, is one more operation on the classes. Its "
                  "liability is that a complex grammar is hard to maintain: at least one "
                  "class per rule makes a large hierarchy, and for such grammars they point "
                  "to parser and compiler generators. Efficient interpreters usually "
                  "translate the tree into another form first, as regular expressions are "
                  "turned into state machines, though the translator can itself be an "
                  "Interpreter."),
            ("code", _lines(PRINT_TREE_JAVA)),
            ("p", "Three implementation issues. The pattern does not say how the tree is "
                  "built: a table-driven parser, a hand-written recursive-descent parser or "
                  "the client itself can do it, as in the sketch. If new ways to interpret "
                  "keep arriving, put them in a Visitor rather than on every node class. "
                  "And a terminal that appears many times, such as a variable, can be "
                  "shared as a Flyweight, since it keeps no position in the tree. The "
                  "Sample Code gives a Smalltalk regular-expression matcher and a C++ "
                  "evaluator of Boolean expressions with an operation that replaces a "
                  "variable by an expression; Known Uses are compilers written in "
                  "object-oriented languages, a file-format description tool and a "
                  "constraint-solving toolkit. Related Patterns: Composite, of which the "
                  "tree is an instance; Flyweight; Iterator, to traverse the tree; and "
                  "Visitor."),
            ("p", "Now the lab, which parses the language above and builds the tree with its "
                  "own classes, Number, Variable, Add, Subtract, Multiply, Divide and "
                  "Negate. On the preset <code>print-job</code> the price of a job is "
                  "<code>setup + copies * (pages * per_page + binding)</code>, with setup 12, "
                  "20 copies of 48 pages at 0.05 a page and 1.5 for binding. The lab finds "
                  "9 nodes: Variable 5, Add 2, Multiply 2, so 3 of the 7 classes are used. "
                  "Interpreting the root makes 9 interpret calls, 1 from the client and 8 "
                  "from nodes to their operands, and the tree is 4 deep, the path down "
                  "through the brackets to <code>pages</code>. The value is 90. The context "
                  "also gives <code>rush</code>, which the sentence never uses, and the "
                  "lab lists it."),
            ("p", "The preset <code>print-job-more</code> keeps the sentence and changes only "
                  "the context, to 50 copies. The tree is the same 9 nodes and 9 calls; the "
                  "value becomes 207. That is the division of labour the pattern makes: the "
                  "tree is the sentence, built once, and the context is what it is "
                  "interpreted against. The preset <code>quiz-score</code> is a different "
                  "sentence, <code>(right - wrong / 4) / questions * 100</code>, with 18 "
                  "right, 3 wrong and 20 questions. It has 9 nodes again, Number 2, "
                  "Variable 3, Subtract 1, Multiply 1, Divide 2, and its value is 345/4 = "
                  "86.25; operators group from the left, so the last step multiplies the "
                  "quotient by 100. Set <code>questions</code> to 0 and the lab refuses, "
                  "naming the division by zero."),
            ("h3", "Exercise"),
            ("code", _lines(MUSEUM_EXERCISE)),
            ("p", "A museum's ticket price: children pay half. By hand, draw the tree, give "
                  "its nodes by class, its depth and the number of interpret calls, and "
                  "interpret it in the context given. Then type it into the lab to check, "
                  "and write the Java that builds the same tree, as the print job's is "
                  "built above."),
            ("p", "The interpreter walks its tree by recursion. The next lesson, Iterator, "
                  "takes the walk itself out of the structure and puts it in an object of "
                  "its own."),
        ],
        "lab": ("gofkit", {
            "mode": "expr",
            "view": "interpret",
            "preset": "print-job",
            "presets": [
                {"id": "print-job",
                 "label": "A print shop's price for one job",
                 "expr": PRINT_EXPR, "context": PRINT_CONTEXT,
                 "expect": {"gexValue": "90", "gexNodes": "9",
                            "gexByClass": "Variable 5, Add 2, Multiply 2",
                            "gexClasses": "3 of the 7",
                            "gexCalls": "9: 1 from the client + 8 from nodes to their operands",
                            "gexDepth": "4",
                            "gexVars": "5: setup, copies, pages, per_page, binding",
                            "gexUnused": "1: rush"}},
                {"id": "print-job-more",
                 "label": "The same sentence in another context: 50 copies",
                 "expr": PRINT_EXPR, "context": PRINT_CONTEXT_MORE,
                 "expect": {"gexValue": "207", "gexNodes": "9",
                            "gexCalls": "9: 1 from the client + 8 from nodes to their operands",
                            "gexUnused": "0: none"}},
                {"id": "quiz-score",
                 "label": "A quiz score with a penalty for wrong answers",
                 "expr": QUIZ_EXPR, "context": QUIZ_CONTEXT,
                 "expect": {"gexValue": "345/4 = 86.25", "gexNodes": "9",
                            "gexByClass": "Number 2, Variable 3, Subtract 1, Multiply 1, Divide 2",
                            "gexClasses": "5 of the 7", "gexDepth": "4",
                            "gexVars": "3: right, wrong, questions"}},
            ],
            "panel_title": "A sentence as a tree, interpreted in a context",
        }),
        "steps_title": "Interpreting a sentence by hand",
        "steps_intro": "Four steps, the last of them on a language of your own.",
        "steps": [
            ("Write the grammar",
             "One rule per line, from the start symbol down to the terminals. Each rule "
             "built from other symbols will be a nonterminal class; each symbol that is "
             "not broken down will be a terminal class."),
            ("Build the tree",
             "Apply precedence and grouping: the operator applied last is the root, "
             "and each operand is a subtree. Brackets decide the shape and then "
             "disappear. Count the nodes by class and the depth."),
            ("Interpret from the leaves",
             "Give each leaf its value from the context, then each operator its result "
             "from its children's, up to the root. Each node is interpreted exactly "
             "once."),
            ("Do it on a language of your own",
             "Find a small language in a system you know: a search filter, a pricing "
             "rule, a permission expression. Write its grammar in three to six rules, "
             "count the classes the pattern would need, and say whether a parser "
             "generator would serve it better."),
        ],
        "worked": {
            "title": "The quiz score, from the leaves up",
            "intro": [
                "Interpret <code>quiz-score</code> with 18 right, 3 wrong, 20 questions.",
            ],
            "lines": [
                "wrong / 4 gives 3/4",
                "right - 3/4 is 18 - 3/4, giving 69/4",
                "69/4 / questions gives 69/80",
                "69/80 * 100 gives 345/4, or 86.25",
                "nodes: 3 variables, 2 numbers, 4 operators: 9",
                "depth: multiply, divide, subtract, divide, wrong: 4",
            ],
            "after": [
                "Each of the 9 nodes is interpreted once, so there are 9 calls, 1 from "
                "the client on the root and 8 from operators to their operands.",
            ],
        },
        "quiz_title": "Trees, contexts and the pattern's limits",
        "quiz": [
            {"q": "In the exercise, with standard precedence and no node for brackets, what "
                  "is the value, and how many nodes does the tree have?",
             "a": ["35, with 9 nodes", "35, with 10 nodes", "23, with 9 nodes",
                   "51, with 9 nodes"],
             "c": 0,
             "why": "children / 2 is 2; adults + 2 is 5; fee * 5 is 40; 40 - discount is 35. "
                    "The nodes are fee, adults, children, the number 2 and discount, and "
                    "Subtract, Multiply, Add and Divide: 9 (Number 1, Variable 4, Add 1, "
                    "Subtract 1, Multiply 1, Divide 1), with depth 4 and 9 interpret calls. "
                    "Ten counts the brackets as a node; 23 halves fee * (adults + children); "
                    "51 charges the children full price, 8 * 7 - 5."},
            {"q": "Going from the preset <code>print-job</code> to "
                  "<code>print-job-more</code>, only the context changes, from 20 copies to "
                  "50. What changes in the lab?",
             "a": ["The value and the number of nodes",
                   "Only the value, from 90 to 207; the tree keeps its 9 nodes",
                   "Nothing: the context is read when the tree is built",
                   "The depth, since more copies make a deeper tree"],
             "c": 1,
             "why": "The tree is the sentence and does not depend on the values; the context "
                    "is passed to it when it is interpreted. 12 + 50 * (48 * 0.05 + 1.5) = 12 "
                    "+ 50 * 3.9 = 207."},
            {"q": "Which liability of Interpreter do the authors name in its "
                  "Consequences?",
             "a": ["The grammar is hard to extend, because rules cannot be subclassed",
                   "A new way of interpreting sentences needs a new grammar",
                   "Grammars with many rules are hard to maintain, at a class or more per "
                   "rule",
                   "The pattern only works with a parser generator"],
             "c": 2,
             "why": "Complex grammars are hard to maintain because each rule needs a "
                    "class of its own, sometimes more; for such grammars the authors point to "
                    "parser or compiler generators instead. Extending a grammar by "
                    "subclassing and adding new interpretations are listed as benefits, and "
                    "the pattern is silent on parsing."},
            {"q": "What does the Interpreter pattern say about turning a written sentence "
                  "into its abstract syntax tree?",
             "a": ["The interpret operation parses its own input",
                   "Nothing: the tree may come from a table-driven parser, a hand-written "
                   "parser or the client",
                   "The tree must be built by a recursive-descent parser",
                   "Each terminal class parses the characters that make it up"],
             "c": 1,
             "why": "The first implementation issue says the pattern leaves parsing "
                    "to others. The client builds the tree or is given it; the book's Smalltalk "
                    "sample even uses the Smalltalk compiler as its parser, and the lesson's "
                    "sketch builds the tree by hand."},
        ],
        "mistakes": [
            ("Calling every operation over a tree an interpreter",
             "Any operation spread over a Composite looks like an interpreter, and the "
             "authors admit as much; they reserve the name for hierarchies you think of "
             "as a language. Totalling a hamper's items is Composite; evaluating a "
             "pricing rule written in a grammar is Interpreter. On the lesson's "
             "illustration the lab counts the nodes either way; whether the hierarchy is "
             "a language is your reading, not the count's."),
            ("Expecting the pattern to parse",
             "Interpreter starts from the tree. How the written sentence becomes a tree "
             "is a separate problem the pattern leaves open, to a parser or to the "
             "client."),
            ("Growing a large grammar one class at a time",
             "The pattern's cost is at least a class per rule. For a language of many "
             "rules, or one that must run fast, the authors point to parser and compiler "
             "generators, or to translating the tree into another form."),
        ],
        "standard": (
            "Finish when you can build and interpret a sentence's tree by hand.",
            "Given a small grammar, a sentence and a context, draw the tree, count its "
            "nodes by class, its depth and its interpret calls, give its value, and say "
            "when the authors would use a parser generator instead."
        ),
        "note": (
            "The lab interprets arithmetic only, with its own seven classes. It cannot "
            "weigh a real grammar's size, measure an interpreter's speed, or tell "
            "whether your hierarchy is a language; the authors leave that to how you "
            "think of it."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Iterator (PDF pp. 277-291 of the operator's copy).
    # Quote: PDF p. 277 of the operator's copy, Motivation, 27 words,
    # quotes.py OK. Lesson total: 27 words.
    {
        "slug": "iterator",
        "title": "Iterator",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "An object that walks an aggregate's elements one at a time, so the aggregate need not expose how it stores them and can be walked in more than one order.",
        "summary": (
            "Iterator moves the job of walking a collection out of the collection and "
            "into an object of its own. Read who controls the iteration, who defines "
            "the traversal and what makes an iterator robust, then walk a quiz app's "
            "question bank in pre-order, post-order and level-order and find one "
            "question's place in each."
        ),
        "key": [
            "walk it without seeing inside",
            "the iterator keeps the position",
            "several walks can be in progress",
            "one tree, more than one order",
            "external: the client drives",
            "internal: the iterator drives",
        ],
        "key_label": "Iterator in six lines",
        "concepts_intro": "Three terms carry the lesson, all of them from the pattern.",
        "concepts": [
            ("Aggregate",
             "An object that holds other objects, such as a list, a set or a tree, and "
             "can be asked for an iterator over them. A ConcreteAggregate returns the "
             "iterator class that knows its representation."),
            ("External and internal iterator",
             "With an external iterator the client asks for each element in turn and "
             "decides when to stop. With an internal iterator the client hands over an "
             "operation and the iterator applies it to every element. Booch called them "
             "active and passive."),
            ("Traversal order",
             "The order in which an iterator visits a structure's elements. On a tree, "
             "pre-order visits a node before its children, post-order after them, and "
             "level-order visits every node at one depth before going deeper."),
        ],
        "read_title": "The pattern first, then its variants, then the count",
        "read_intro": (
            "Read Iterator in your own copy first; its Implementation section is long "
            "and worth all of it. The lesson reads the pattern as a tool and counts "
            "three traversals of one tree."
        ),
        "body": [
            ("p", "&ldquo;The key idea in this pattern is to take the responsibility for "
                  "access and traversal out of the list object and put it into an iterator "
                  "object.&rdquo; That sentence from Iterator's Motivation is the whole "
                  "pattern; the rest of the section is about the choices it opens. This "
                  "lesson reads the pattern section by section. Read it in your own copy "
                  "first."),
            ("p", "The motivation is a list. It should let you reach its elements without "
                  "showing how it keeps them, and you may want to walk it in different "
                  "ways, or twice at once, without adding an operation to the list for "
                  "every kind of walk. So an iterator object keeps track of the current "
                  "element and offers operations to start, advance, test for the end and "
                  "read the current item. Then the authors go a step further: if clients "
                  "should not depend on which kind of list they hold, both the lists and "
                  "the iterators need abstract classes, and each list creates its own "
                  "iterator through a factory method, which connects the two hierarchies."),
            ("p", "The participants, as you would apply them. An Iterator defines the "
                  "interface for reaching and walking elements; a ConcreteIterator "
                  "implements it and keeps the position in the walk; an Aggregate defines "
                  "the operation that creates an iterator; a ConcreteAggregate returns the "
                  "right ConcreteIterator. The pattern applies when clients should get at "
                  "what an aggregate holds without learning how it holds it, when one "
                  "aggregate must be walked in several ways or by several walks at once, "
                  "and when different kinds of aggregate should be walked through one "
                  "interface, which the book calls polymorphic iteration."),
            ("code", _lines(PREORDER_JAVA)),
            ("p", "Three consequences, all benefits: the walk can vary, since replacing the "
                  "iterator changes the order and a subclass can add a new one; the "
                  "aggregate's own interface stays small; and more than one walk can be "
                  "under way at once, since each iterator keeps its own state. The "
                  "sketch is one such walk. Swap its stack for a queue, taking from the "
                  "front and adding the children at the back in order, and the same class "
                  "shape gives level-order."),
            ("p", "The implementation issues are where the judgement lies. Who controls the "
                  "iteration? An external iterator is more flexible (comparing two "
                  "collections element by element is easy with one and, the authors say, "
                  "practically impossible with an internal one), while an internal "
                  "iterator is easier to use because it writes the loop for you. Who "
                  "defines the traversal? If the aggregate does and the iterator only "
                  "marks the position, the iterator is called a cursor; if the iterator "
                  "does, different walks are easy, but it may need the aggregate's private "
                  "members. How robust is it? Changing an aggregate while it is being "
                  "walked can visit an element twice or miss one; a robust iterator copes "
                  "with insertions and removals without copying the aggregate, usually "
                  "because the aggregate knows its iterators and adjusts them."),
            ("code", _lines(ITERATOR_USE_JAVA)),
            ("p", "Here the book shows its date. It calls internal iterators weak in C++, "
                  "which in 1995 had no anonymous functions or closures, and its sample "
                  "builds one by subclassing. Java 8's lambdas make the internal form the "
                  "short one, as the second half of the sketch shows. The standard Java "
                  "collections answer the robustness question differently again: most of "
                  "their iterators detect a change made behind their back and throw, "
                  "rather than adjusting. The remaining issues are extra operations such "
                  "as previous, the cost of polymorphic iterators in C++ and a Proxy that "
                  "frees them, privileged access, iterators for composites, which must "
                  "keep a path through the tree, and a null iterator that is always done, "
                  "handy at a tree's leaves. The Sample Code builds list iterators "
                  "forwards and backwards and an internal traverser; Known Uses include "
                  "Smalltalk's collection methods and streams. Related Patterns: "
                  "Composite, Factory Method and Memento."),
            ("p", "Now the lab, on a quiz app's question bank: a quiz of sections, sections "
                  "holding questions and other sections. On the preset <code>quiz</code>, "
                  "10 nodes, the three orders are: pre-order quiz, warmup, q1, q2, main, "
                  "q3, bonus, q4, q5, q6; post-order q1, q2, warmup, q3, q4, bonus, q5, "
                  "main, q6, quiz; level-order quiz, warmup, main, q6, q1, q2, q3, bonus, "
                  "q5, q4. The bonus question q4, the deepest node, is 8th in pre-order, "
                  "5th in post-order and last, 10th, in level-order. Pre-order suits "
                  "printing the quiz as a contents page, post-order totalling marks from "
                  "the bottom up, level-order showing the top level first."),
            ("p", "The preset <code>round</code> is a single section of four questions, a "
                  "list rather than a tree. There pre-order and level-order coincide, "
                  "round, a1, a2, a3, a4, and post-order differs only in putting the "
                  "section last; finding a3 gives positions 4, 3 and 4 of 5. The orders "
                  "part company only when the structure has depth, which is why the book "
                  "says composites often need more than one kind of iterator."),
            ("h3", "Exercise"),
            ("code", _lines(CATALOGUE_EXERCISE)),
            ("p", "A library catalogue of shelves and books. By hand, write its pre-order, "
                  "post-order and level-order, and the position of s1 in each. Then type "
                  "the records into the lab to check, and say which order the sketch's "
                  "stack produces and what you would change for each of the other two."),
            ("p", "An iterator walks a structure on behalf of a client. The next lesson, "
                  "Mediator, is about objects that would otherwise all talk to each other "
                  "directly."),
        ],
        "lab": ("gofkit", {
            "mode": "tree",
            "view": "traverse",
            "preset": "quiz",
            "presets": [
                {"id": "quiz",
                 "label": "A quiz app's question bank, finding the bonus question",
                 "nodes": _records(QUIZ_TREE), "find": "q4",
                 "expect": {"gtrNodes": "10",
                            "gtrPre": "quiz, warmup, q1, q2, main, q3, bonus, q4, q5, q6",
                            "gtrPost": "q1, q2, warmup, q3, q4, bonus, q5, main, q6, quiz",
                            "gtrLevel": "quiz, warmup, main, q6, q1, q2, q3, bonus, q5, q4",
                            "gtrFind": "pre-order 8, post-order 5, level-order 10 (of 10)"}},
                {"id": "round",
                 "label": "One round of four questions: a list, not a tree",
                 "nodes": _records(ROUND_LIST), "find": "a3",
                 "expect": {"gtrNodes": "5",
                            "gtrPre": "round, a1, a2, a3, a4",
                            "gtrPost": "a1, a2, a3, a4, round",
                            "gtrLevel": "round, a1, a2, a3, a4",
                            "gtrFind": "pre-order 4, post-order 3, level-order 4 (of 5)"}},
            ],
            "panel_title": "One structure, three traversals",
        }),
        "steps_title": "Walking a tree by hand",
        "steps_intro": "Four steps, the last of them on a structure of your own.",
        "steps": [
            ("Draw the tree with its children in order",
             "Write each node under its parent, children left to right in the order "
             "given. The order of children is part of the structure; change it and every "
             "traversal changes."),
            ("Write pre-order and post-order",
             "Pre-order: write a node, then walk each child's subtree in turn. "
             "Post-order: walk each child's subtree, then write the node. Both go deep "
             "before they go across."),
            ("Write level-order",
             "Write the root, then every node at depth 1 left to right, then depth 2, "
             "and so on. It goes across before it goes deep, and needs a queue where the "
             "other two need a stack."),
            ("Do it on a structure of your own",
             "Take a nested structure you work with: a folder tree, a menu, an "
             "organisation chart. Write it as records, get its three orders, and say "
             "which order your code needs and whether that code walks it with an "
             "external or an internal iterator."),
        ],
        "worked": {
            "title": "Three orders over the question bank",
            "intro": [
                "Walk the preset <code>quiz</code>; quiz holds warmup, main and q6.",
            ],
            "lines": [
                "pre: quiz, warmup, q1, q2, main, q3, bonus, q4, q5, q6",
                "post: q1, q2, warmup, q3, q4, bonus, q5, main, q6, quiz",
                "depth 1: warmup, main, q6",
                "depth 2: q1, q2, q3, bonus, q5",
                "depth 3: q4",
                "q4: eighth, fifth and tenth of 10",
            ],
            "after": [
                "Level-order is the root followed by the three depth lists in turn. The "
                "lab's positions count from 1.",
            ],
        },
        "quiz_title": "Orders, control and robustness",
        "quiz": [
            {"q": "In the exercise, which of these is the level-order of the catalogue?",
             "a": ["catalogue, fiction, f1, f2, science, s1, maps",
                   "f1, f2, fiction, s1, science, maps, catalogue",
                   "catalogue, fiction, science, maps, f1, f2, s1",
                   "catalogue, maps, science, fiction, s1, f2, f1"],
             "c": 2,
             "why": "Level-order takes the root, then its children fiction, science and maps "
                    "in record order, then the next depth, f1, f2 and s1. The first answer "
                    "is pre-order and the second post-order, both real orders of this tree "
                    "but not this one; the fourth takes each level right to left. s1 is "
                    "6th in pre-order, 4th in post-order and 7th in level-order. The "
                    "sketch's stack gives pre-order."},
            {"q": "On the preset <code>quiz</code>, where is q4 in pre-order, post-order "
                  "and level-order?",
             "a": ["8th, 5th and 10th", "8th, 4th and 10th", "7th, 5th and 9th",
                   "10th, 5th and 8th"],
             "c": 0,
             "why": "Pre-order reaches q4 after quiz, warmup, q1, q2, main, q3 and bonus, so "
                    "8th. Post-order writes q1, q2, warmup and q3 first, then q4, so 5th. "
                    "q4 is the only node at depth 3, so level-order puts it last, 10th of 10."},
            {"q": "Which task do the authors say is easy with an external iterator and "
                  "practically impossible with an internal one?",
             "a": ["Applying one operation to every element",
                   "Comparing two collections for equality",
                   "Walking a list from front to back",
                   "Freeing the iterator when it is done"],
             "c": 1,
             "why": "Comparing two collections needs both walks advanced in step, which "
                    "only a client in control of each iterator can do. Applying one "
                    "operation to every element is what an internal iterator does best."},
            {"q": "What makes an iterator robust, in the book's sense?",
             "a": ["It copies the aggregate first and walks the copy",
                   "It throws an exception if the aggregate changes during the walk",
                   "It copes with insertions and removals during the walk, without copying "
                   "the aggregate",
                   "It can walk the aggregate both forwards and backwards"],
             "c": 2,
             "why": "A robust iterator keeps working when elements are added or removed, "
                    "and does so without a copy, usually because the aggregate adjusts the "
                    "iterators it has made. Copying is the simple answer the authors call "
                    "too expensive in general; throwing, as most Java collection iterators "
                    "do, detects the change rather than coping with it."},
        ],
        "mistakes": [
            ("Thinking a tree has one natural order",
             "Pre-order, post-order and level-order are all complete walks of the same "
             "tree, and the authors make it a consequence of the pattern that the walk "
             "can vary by changing the iterator. On the lesson's illustration the bonus "
             "question is 8th, 5th or 10th depending on the iterator; which order is "
             "right depends on what the walk is for."),
            ("Changing an aggregate while walking it",
             "Adding or removing elements mid-walk can visit one twice or skip one. A "
             "robust iterator is designed for it; most iterators are not, and Java's "
             "standard ones throw when they detect it."),
            ("Putting every traversal on the aggregate's interface",
             "An operation on the list for each kind of walk bloats it and still allows "
             "only one walk at a time. The pattern puts each traversal in its own "
             "iterator class, created by the aggregate."),
        ],
        "standard": (
            "Finish when you can walk a tree in three orders by hand.",
            "Given a tree as records, write its pre-order, post-order and level-order "
            "and a node's place in each, and say who controls the iteration and who "
            "defines the traversal in an iterator you use."
        ),
        "note": (
            "The lab lists the orders of a tree stated with its children in order. It "
            "cannot show a robust iterator, a walk interrupted by a change, or the cost "
            "of keeping a path through a deep composite; those are the Implementation "
            "section's questions."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Mediator (PDF pp. 293-302 of the operator's copy).
    # Quote: PDF p. 297 of the operator's copy, Consequences, 12 words,
    # quotes.py OK. Lesson total: 12 words.
    {
        "slug": "mediator",
        "title": "Mediator",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "One object that holds how a group of objects interact, so that each knows only it and not the others.",
        "summary": (
            "Mediator puts the rules of a group's interaction in one object, so the "
            "members, its colleagues, refer to it instead of to each other. Read its "
            "five consequences, the last of them a warning, then count the connections "
            "a cake order form's fields need when each knows every other and when each "
            "knows only the form, and how many change when one field does."
        ),
        "key": [
            "colleagues know only the mediator",
            "many to many becomes one to many",
            "the interaction lives in one class",
            "n·(n − 1)/2 links against n",
            "n − 1 changed against 1",
            "the mediator can grow into a monolith",
        ],
        "key_label": "Mediator in six lines",
        "concepts_intro": "Three terms carry the lesson, all of them the pattern's.",
        "concepts": [
            ("Colleague",
             "One of the objects whose behaviour depends on the others, such as a field "
             "on a form. Each colleague knows its mediator and tells it when something "
             "of interest happens, where it would otherwise have told another colleague "
             "directly."),
            ("Mediator",
             "The object that knows the colleagues and coordinates them. A "
             "ConcreteMediator implements the cooperation; an abstract Mediator is "
             "needed only if colleagues must work with more than one kind."),
            ("Connection",
             "A two-way link by which two objects can ask each other for something, "
             "counted once per pair. Pairwise, every pair that interacts needs one; through a mediator, each "
             "colleague needs one, to the mediator."),
        ],
        "read_title": "The pattern first, then its warning, then the count",
        "read_intro": (
            "Read Mediator in your own copy first. The lesson reads the pattern as a "
            "tool, weighs its consequences, and counts connections on a form of its "
            "own."
        ),
        "body": [
            ("p", "&ldquo;The Mediator pattern trades complexity of interaction for "
                  "complexity in the mediator.&rdquo; The sentence is the fifth of "
                  "Mediator's consequences, and the lesson keeps it in view from the start, "
                  "because the pattern's benefits are easy to count and its cost is not. "
                  "This lesson reads the pattern section by section; read it in your own "
                  "copy first."),
            ("p", "The motivation begins with a tension in object-oriented design. "
                  "Spreading behaviour over many objects helps reuse, but the objects end up "
                  "connected to each other, in the worst case each to every other, and "
                  "then none can work without the rest and the system behaves as if it "
                  "were one piece. The book's example is a dialog box whose widgets depend "
                  "on one another: a button enabled only when a field has text, a list "
                  "whose selection fills the field. Rather than subclassing every widget "
                  "for every dialog, one director object knows the widgets and coordinates "
                  "them, and each widget knows only the director."),
            ("p", "The participants, as you would apply them. The Mediator defines the "
                  "interface colleagues use to talk to it; a ConcreteMediator implements "
                  "the cooperation and knows its colleagues; a Colleague holds a "
                  "reference to its mediator only, and goes to it wherever it would have "
                  "gone to a fellow colleague. The authors give three situations: objects whose dealings with "
                  "one another are clearly defined but tangled; an object that is hard to "
                  "use elsewhere because it is wired to so many others; and behaviour shared "
                  "among several classes that you want to change without a subclass of "
                  "each."),
            ("code", _lines(MEDIATOR_JAVA)),
            ("p", "The five consequences, benefits first. The mediator limits subclassing: "
                  "the behaviour that would be spread over the colleagues is in one place, "
                  "so changing it means subclassing the mediator alone, and the colleague "
                  "classes are reused as they are. It decouples colleagues, which can then "
                  "vary independently of the mediator. It simplifies object protocols, "
                  "replacing many-to-many interaction by one-to-many. It abstracts how "
                  "objects cooperate, making the interaction a thing you can look at by "
                  "itself. And it centralizes control, which is the warning: the mediator "
                  "can become more complex than any colleague, a monolith that is hard to "
                  "maintain. The book's own sample admits that its director's change "
                  "handler grows with the dialog."),
            ("p", "Two implementation issues. An abstract Mediator class can be left out "
                  "when colleagues only ever work with one mediator. And colleagues must "
                  "tell the mediator when something happens: either the mediator observes "
                  "them, through Observer, or it offers a notification operation to which "
                  "a colleague passes itself, as the sketch's <code>changed</code> does. "
                  "The Sample Code builds the dialog's director; the Known Uses are "
                  "dialog directors in ET++ and the THINK class library, the view manager "
                  "of Smalltalk/V for Windows, Observer's change manager and a "
                  "connectivity solver in Unidraw. Related Patterns: Facade, which differs "
                  "because its protocol runs one way, the facade calling the subsystem and "
                  "never the reverse, where a mediator's runs in every direction; and "
                  "Observer, as the means of notification. The lesson Discussion of "
                  "Behavioral Patterns, in the next course, sets Mediator against Observer "
                  "at length."),
            ("p", "The lab is the context view of the Domain-Driven Design kit, used here "
                  "for the same count: its contexts are this lesson's colleagues and its "
                  "translators are connections. Its pairwise scheme is the worst case the "
                  "authors name, every colleague connected to every other; its published "
                  "scheme, one shared language each context translates to, is the "
                  "mediator, one connection per colleague. On the preset "
                  "<code>cake-form</code>, a bakery's order form with five fields (size, "
                  "flavour, pickup, message and price) connected pairwise, there are 10 "
                  "connections to build, n·(n − 1)/2, and 4 to change when one field's "
                  "interface changes, one for each other field."),
            ("p", "The preset <code>cake-form-mediated</code> puts the same five fields "
                  "behind one form object: 5 connections to build and 1 to change, so "
                  "pairwise needs 2× as many to build and 4× as many to change. The preset "
                  "<code>cake-form-bigger</code> adds candles, a box and allergens, eight "
                  "fields pairwise: 28 to build and 7 to change, against 8 and 1, ratios "
                  "of 7/2 = 3.5× and 7×. The gap grows with every colleague, which is the "
                  "pattern's case in a number. What the count leaves out is the other "
                  "side of the trade: the mediator's own <code>changed</code> method grows "
                  "with the interactions it now holds, and no tile measures that."),
            ("h3", "Exercise"),
            ("code", _lines(STUDIO_EXERCISE)),
            ("p", "A recording studio's mixing desk, seven controls that affect one "
                  "another. By hand, give the connections to build and to change when one "
                  "control changes, pairwise and through a mediator. Then type the seven "
                  "names into the lab under each scheme to check, and list two "
                  "interactions you would expect the mediator's method to have to "
                  "handle."),
            ("p", "A mediator holds the logic of an interaction. The next lesson, Memento, "
                  "is about holding an object's state outside it without exposing what "
                  "that state is."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "protocol",
            "directed": "no",
            "preset": "cake-form",
            "presets": [
                {"id": "cake-form",
                 "label": "Five order-form fields, each connected to every other",
                 "contexts": FORM_FIELDS, "scheme": "pairwise",
                 "expect": {"dcxN": "5", "dcxBuild": "10", "dcxChange": "4",
                            "dcxOther": "published: 5 to build, 1 to change",
                            "dcxBuildRatio": "2×", "dcxChangeRatio": "4×"}},
                {"id": "cake-form-mediated",
                 "label": "The same five fields, each connected only to the form",
                 "contexts": FORM_FIELDS, "scheme": "published",
                 "expect": {"dcxN": "5", "dcxBuild": "5", "dcxChange": "1",
                            "dcxOther": "pairwise: 10 to build, 4 to change"}},
                {"id": "cake-form-bigger",
                 "label": "Eight fields, each connected to every other",
                 "contexts": FORM_FIELDS_BIGGER, "scheme": "pairwise",
                 "expect": {"dcxN": "8", "dcxBuild": "28", "dcxChange": "7",
                            "dcxOther": "published: 8 to build, 1 to change",
                            "dcxBuildRatio": "7/2 ≈ 3.5×", "dcxChangeRatio": "7×"}},
            ],
            "panel_title": "Colleagues connected pairwise and through a mediator",
            "panel_intro": (
                "The colleagues all interact. Read each context as a colleague and each "
                "translator as a connection. Pairwise, every pair of colleagues has its own "
                "connection; under the published scheme, read here as the mediator, each "
                "colleague has one connection, to the mediator. The lab counts the "
                "connections to build and those to change when one colleague's interface "
                "changes. It does not count the work inside the mediator."
            ),
        }),
        "steps_title": "Counting a group's connections",
        "steps_intro": "Four steps, the last of them on a group of your own.",
        "steps": [
            ("List the colleagues",
             "Write down every object whose behaviour depends on another in the group. "
             "Count them: that is n."),
            ("Count the pairwise connections",
             "If every colleague may affect every other, there are n·(n − 1)/2 pairs to "
             "connect, and a change to one colleague's interface reaches the n − 1 "
             "others. Real groups may connect fewer pairs; the count is the worst case."),
            ("Count the mediated connections",
             "Through a mediator there are n connections, one per colleague, and a "
             "change to one colleague reaches 1, the mediator. Then list the rules the "
             "mediator now holds."),
            ("Do it on a group of your own",
             "Take a form, a screen or a set of services in a system you know where the "
             "parts react to each other. Count the colleagues and the pairs that "
             "actually interact, and say which object, if any, already acts as their "
             "mediator."),
        ],
        "worked": {
            "title": "Five fields, then eight",
            "intro": [
                "Count <code>cake-form</code> and <code>cake-form-bigger</code> by hand.",
            ],
            "lines": [
                "pairwise, 5 fields: 5 × 4 / 2, so 10 to build",
                "one field changes: 5 − 1, so 4 connections",
                "mediated, 5 fields: 5 to build, 1 to change",
                "pairwise, 8 fields: 8 × 7 / 2, so 28; 7 to change",
                "mediated, 8 fields: 8 to build, 1 to change",
                "ratios for 8 fields: 28 / 8, or 3.5, and 7",
            ],
            "after": [
                "Pairwise grows with the square of the colleagues, mediated with their "
                "number. The mediator's own size is not in these lines.",
            ],
        },
        "quiz_title": "Connections and the pattern's consequences",
        "quiz": [
            {"q": "In the exercise, with seven controls, counting one two-way connection "
                  "per pair, how many connections are there to build and to change when "
                  "one changes, pairwise and through a mediator?",
             "a": ["Pairwise 21 and 6; mediated 7 and 1",
                   "Pairwise 42 and 6; mediated 7 and 1",
                   "Pairwise 21 and 7; mediated 7 and 7",
                   "Pairwise 49 and 7; mediated 8 and 1"],
             "c": 0,
             "why": "Seven controls make 7 × 6 / 2 = 21 pairs, and a change to one reaches "
                    "the other 6; through a mediator there are 7 connections and a change "
                    "reaches 1. Forty-two counts each pair from both ends, as one-way "
                    "references would; 49 counts each control as connected to itself."},
            {"q": "Which consequence of Mediator do the authors give as a drawback?",
             "a": ["Colleague classes can no longer be reused",
                   "Every colleague must be subclassed for each new interaction",
                   "The mediator can become a monolith that is hard to maintain",
                   "Many-to-many interactions replace one-to-many ones"],
             "c": 2,
             "why": "Centralizing control moves the complexity of the interaction into the "
                    "mediator, which can become more complex than any colleague. The other "
                    "three invert benefits the authors list: colleagues are reused as they "
                    "are, only the mediator is subclassed, and one-to-many replaces "
                    "many-to-many."},
            {"q": "According to Related Patterns, how does Facade differ from Mediator?",
             "a": ["A facade knows its subsystem's classes; a mediator does not know its "
                   "colleagues",
                   "A facade's protocol runs one way, from the facade to the subsystem; a "
                   "mediator's runs in every direction",
                   "A facade is always a singleton; a mediator never is",
                   "A facade coordinates peers; a mediator simplifies an interface"],
             "c": 1,
             "why": "A facade makes requests of the subsystem's classes, which do not call "
                    "it back; colleagues and their mediator call each other. A mediator does "
                    "know its colleagues, and the fourth answer swaps the two patterns' "
                    "purposes."},
            {"q": "Going from five to ten colleagues, all interacting, and counting one "
                  "two-way connection per pair, how many pairwise connections are there "
                  "to build?",
             "a": ["20", "45", "50", "90"],
             "c": 1,
             "why": "Ten colleagues make 10 × 9 / 2 = 45 pairs, against 10 through a "
                    "mediator. Twenty doubles five's 10, as if the count grew in proportion; "
                    "90 counts each pair from both ends; 50 is 10 × 5."},
        ],
        "mistakes": [
            ("Counting only the connections saved",
             "The authors give the cost as plainly as the benefit: the mediator takes on "
             "the complexity the colleagues shed and can become a monolith. On the "
             "lesson's illustration eight fields need 8 connections instead of 28, and "
             "every rule those 28 carried is now in one method; whether that method "
             "stays manageable is the question the count cannot answer."),
            ("Treating a facade as a mediator",
             "Both stand between a client and several objects, but a facade's protocol "
             "is one-way and its subsystem does not know it exists. A mediator's "
             "colleagues know it and call it, and it calls them back."),
            ("Assuming every colleague talks to every other",
             "The pairwise count is the worst case the motivation describes. A real "
             "group may connect only some pairs, and the saving then is smaller; count "
             "the pairs that actually interact before deciding."),
        ],
        "standard": (
            "Finish when you can count a group's connections both ways and weigh them.",
            "Given n colleagues, give the connections to build and to change pairwise "
            "and through a mediator, and state the pattern's five consequences, "
            "including the one that warns against it."
        ),
        "note": (
            "The lab counts connections in the worst case, every colleague linked to "
            "every other, and borrows a kit whose words are contexts and translators. "
            "It cannot measure the mediator's own complexity, which is the pattern's "
            "stated cost, or tell how many pairs in your group really interact."
        ),
    },
]
