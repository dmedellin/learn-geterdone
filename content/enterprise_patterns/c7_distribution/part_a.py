"""Distribution and Putting It Together, lessons 1-5.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002): Chapter 7, Distribution Strategies; Chapter 15, Distribution Patterns
(Remote Facade, Data Transfer Object); Chapter 8, Putting It All Together; and
Chapter 18's Plugin (David Rice and Matt Foemmel) and Service Stub (Rice).
Every quotation is copied from the operator's copy, character for character,
with its PDF page in the comment beside the lesson; every figure attributed to
the book carries its PLAN section S.2 id. The code is written for these
lessons: none of the book's listings is reproduced, and none of its example
domains is used. Each snippet is one constant below, copied from
docs/enterprise-patterns/presets.py, used by the lesson's code block.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# 7.1 (body; 6 lines).
REMOTE_CUSTOMER = """\
// Each call on this interface crosses the network.
interface RemoteCustomer extends Remote {
    String name() throws RemoteException;
    String city() throws RemoteException;
    long creditCents() throws RemoteException;
}"""

# 7.2 (body; 16 lines).
CUSTOMER_FACADE = """\
// One remote call does the work of several local ones.
class CustomerFacade {
    private final CustomerRepository customers;

    CustomerFacade(CustomerRepository customers) {
        this.customers = customers;
    }

    void moveHouse(long id, String street, String city, String code) {
        Customer c = customers.find(id);
        c.address().setStreet(street);
        c.address().setCity(city);
        c.address().setPostcode(code);
        customers.save(c);
    }
}"""

# 7.3 (body; 8 lines).
ORDER_DTO = """\
// Everything the order screen shows, in one serializable bundle.
class OrderDto implements Serializable {
    long id;
    String customerName;
    String status;
    long totalCents;
    List<String> lineSummaries = new ArrayList<String>();
}"""

# 7.4 (body; 11 lines).
PLACE_ORDER_STACK = """\
// One request through every layer: the service runs the domain
// logic inside a unit of work, and the mappers do the SQL.
String placeOrder(String cartId) throws SQLException {
    UnitOfWork uow = new UnitOfWork();
    Cart cart = carts.find(cartId);
    Order order = cart.checkOut();
    uow.markNew(order);
    uow.markChanged(cart);
    uow.commit(mapper);
    return "Order " + order.number() + " placed";
}"""

# 7.5 (body; 20 lines).
ADDRESS_STUB = """\
// The interface the signup depends on, and a stub for its tests.
interface AddressCheck {
    boolean deliverable(String postcode);
}
class AddressCheckStub implements AddressCheck {
    public boolean deliverable(String postcode) {
        return !postcode.startsWith("ZZ");
    }
}

// The plugin: one switch on the environment, read once at startup.
class AddressChecks {
    static AddressCheck forEnvironment(String environment) {
        switch (environment) {
            case "test": return new AddressCheckStub();
            case "live": return new PostOfficeCheck();
            default: throw new IllegalArgumentException(environment);
        }
    }
}"""

_BY_CLASS_CALLS = "screen, order, 20; order, customer, 10; order, product, 30; order, pricing, 15"
_STACK_CALLS = ("browser, page, 1; page, service, 2; service, domain, 40; "
                "domain, mapper, 25; mapper, database, 6")
_ORDER_FIELDS = ("id, 8, yes; customerName, 40, yes; status, 10, yes; "
                 "totalCents, 8, yes; lines, 2000, yes; notes, 4000, no")


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 7, Distribution Strategies, PDF pp. 92-99 of the operator's copy:
    # The Allure of Distributed Objects (p. 93), Remote and Local Interfaces
    # (p. 95), Where You Have to Distribute (p. 97), Working with the
    # Distribution Boundary (p. 98), Interfaces for Distribution (p. 99).
    # Quote: PDF p. 95 of the operator's copy, 15 words, ea_quotes.py OK.
    # "fight like a cornered rat": PDF p. 97 of the operator's copy, 5 words,
    # ea_quotes.py OK. Lesson total: 20 words.
    {
        "slug": "distribution-strategies",
        "title": "Distribution Strategies",
        "module": "Chapter 7 · Distribution Strategies",
        "one_line": "Fowler's First Law of Distributed Object Design, and the arithmetic behind it: a call to another process costs orders of magnitude more than a call within one.",
        "summary": (
            "Chapter 7 sets out why putting each kind of object on its own machine fails: a "
            "remote call is orders of magnitude slower than a local one, so a remote "
            "interface must be coarse-grained and a local one fine-grained, and one class "
            "cannot be both. Price one design's calls with its classes spread by class and "
            "with all of them in one process."
        ),
        "key": [
            "a remote call: orders of magnitude slower",
            "a remote interface must be coarse-grained",
            "a local interface is best fine-grained",
            "first law: do not distribute your objects",
            "spread load by clustering, not by class",
            "count the calls that cross a node",
        ],
        "key_label": "Chapter 7 in six lines",
        "concepts_intro": (
            "Three ideas carry the chapter. The rest of the course is built on the second."
        ),
        "concepts": [
            ("Distribution by class",
             "Putting each kind of object, such as customers, orders and products, in its own "
             "component on its own processing node, so that a busy component can be given "
             "more machines. It is the design the chapter opens with, and argues against."),
            ("Fine-grained and coarse-grained interfaces",
             "A fine-grained interface has many small methods, one getter or setter for each "
             "thing. A coarse-grained interface does a lot in one call, such as reading or "
             "updating all of an address at once. The first suits calls within a process, the "
             "second calls between processes."),
            ("Clustering",
             "Running several copies of the whole application, every class in one process, "
             "on several nodes. Each copy makes only local calls, so it can keep the "
             "fine-grained interfaces, and the load is spread by adding copies."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Chapter 7, Distribution Strategies, in your own copy first. It is short, "
            "and it is an argument to read through. The lesson sets it out section by "
            "section and then prices one design's calls on one node and on five."
        ),
        "body": [
            # PDF p. 95 of the operator's copy.
            ("p", "&ldquo;Hence, we get to my First Law of Distributed Object Design: Don't "
                  "distribute your objects!&rdquo; That is the turn of Chapter 7, "
                  "Distribution Strategies, and this lesson reads the whole chapter: the "
                  "design Fowler argues against, the fact the argument rests on, and the "
                  "places where, the law notwithstanding, you will have to distribute. Read "
                  "it in your own copy first; it is an argument, not a catalogue."),
            ("p", "The chapter opens, in The Allure of Distributed Objects, with a design "
                  "Fowler says he used to be shown two or three times a year. An ordering "
                  "system is drawn as separate remote objects for customers, orders, products "
                  "and deliveries, each a component that can be put on its own processing "
                  "node. The reason given is performance: if one component gets busy, give it "
                  "more boxes. The vendors' promise behind it is transparency, that an object "
                  "can call another without knowing whether the callee is in its own process "
                  "or on another machine. Transparency is valuable, Fowler grants, but "
                  "performance is not usually one of the things it makes transparent, and the "
                  "design will usually slow the system badly, or make it harder to build and "
                  "deploy, and usually both."),
            ("p", "Remote and Local Interfaces gives the reason. A procedure call within a "
                  "process is very fast; a call between two processes is orders of magnitude "
                  "slower, and another machine adds an order or two more. So the interface "
                  "of an object used remotely must differ from one used locally. Locally, "
                  "fine-grained is best: an address class with separate methods to get and "
                  "set the city, the state and the rest, small pieces that can be combined "
                  "and overridden. Remotely you want the city, state and postcode in one call, "
                  "an interface designed to minimise calls rather than for flexibility. "
                  "Middleware may run a local call at local speed, but that does not "
                  "escape the point: any object that may be used remotely needs the "
                  "awkward coarse-grained interface, so you want as few inter-process "
                  "collaborations as you can get. Distribute by class and you get many remote "
                  "calls, coarse interfaces on every class, and, into the bargain, a system "
                  "that is hard to change."),
            ("p", "Hence the law, and its alternative. To use several processors, Fowler "
                  "says, put all the classes in a single process and run copies of that "
                  "process on the various nodes. That is clustering: every call inside a copy "
                  "is local, every class keeps its fine-grained interface, and the load is "
                  "spread by the number of copies, not by the class of object."),
            # PDF p. 97 of the operator's copy.
            ("p", "Where You Have to Distribute is the concession. There are limits to "
                  "clustering, and Fowler's advice is to &ldquo;fight like a cornered "
                  "rat&rdquo; to remove as many process boundaries as you can, knowing you "
                  "will not remove them all. He names five. Client and server: the desktop "
                  "and the shared data are different machines. The application server and "
                  "the database, unless everything runs inside the database as stored "
                  "procedures; SQL, he notes, is designed as a remote interface, so the cost "
                  "can usually be kept down. The web server and the application server, "
                  "which are best in one process when all else is equal. A vendor's package, "
                  "which runs in its own process. And, rarely, a genuine reason to split the "
                  "application server's own software, which he advises avoiding at almost "
                  "any price."),
            ("p", "The last two sections look ahead to the rest of the course. Working with "
                  "the Distribution Boundary says to keep fine-grained objects inside the "
                  "process and put coarse-grained objects at the boundary, whose only job is "
                  "to be a remote interface to them: Remote Facade, with Data Transfer Object "
                  "to carry the data. Interfaces for Distribution weighs XML over HTTP "
                  "against a platform's own remote call: XML carries a lot of structured data "
                  "in one round trip and crosses platforms and firewalls, but adds a burden "
                  "to each call, so Fowler would use XML web services only when a more direct "
                  "approach is not possible. He adds that he increasingly prefers "
                  "asynchronous messaging to the synchronous calls the book assumes, and "
                  "leaves its patterns to another book."),
            ("code", _lines(REMOTE_CUSTOMER)),
            ("p", "The snippet is the chapter's mistake in six lines: a fine-grained "
                  "interface made remote. `RemoteCustomer` extends Java's `Remote`, so each of "
                  "its three methods, on lines 3 to 5, is a call across the network that may "
                  "throw `RemoteException`. A screen that shows a customer's name, city and "
                  "credit makes three round trips where one would do. Locally the same three "
                  "getters would be exactly right."),
            ("p", "Now the count. The lab reads the design as records `caller, callee, "
                  "count`, the number of times one class calls another for one piece of work, "
                  "and a list of nodes written `class=node`; a class not listed runs on node "
                  "`main`. A call is remote when its two classes are on different nodes. The "
                  "tiles are every call, the remote calls, the time (each remote call at the "
                  "remote cost and each local call at the local cost, in microseconds), the "
                  "remote calls' share of that time, the time with every class on one node, "
                  "and the ratio of the two times."),
            ("p", "The preset <code>by-class</code> is the opening design, with a screen "
                  "calling an order 20 times and the order calling a customer 10 times, a "
                  "product 30 and a pricing object 15, each of the four on its own node. A "
                  "remote call costs 1,000 µs and a local one 1 µs, an illustrative ratio "
                  "standing in for Fowler's orders of magnitude. All 75 calls cross a node, "
                  "so the time is 75,000 µs, all of it remote (1 = 100%), against 75 µs on "
                  "one node: 1,000×. The preset <code>one-process</code> has no nodes: 0 "
                  "remote calls, 75 µs, 1×. A cluster is many copies of "
                  "<code>one-process</code>, each answering its own requests at that price."),
            ("p", "What the counts show is the chapter's arithmetic, not your network. On "
                  "the lesson's illustration the distributed design is a thousand times "
                  "slower for the same work, because the ratio was set at a thousand; on "
                  "your own machines the ratio is whatever you measure, and Fowler's point "
                  "survives any ratio much above one. Change one class's node and watch "
                  "which calls stop crossing: that is the decision the chapter wants you to "
                  "make deliberately."),
            ("h3", "Exercise"),
            ("ul", [
                "Calls: `web, cart, 12; cart, stock, 8; cart, tax, 8; tax, rates, 16`.",
                "Nodes: `web` on a front node; `tax` and `rates` on a back node; `cart` and "
                "`stock` on `main`.",
                "A remote call costs 800 µs and a local one 2 µs.",
            ]),
            ("p", "Find by hand the calls, the remote calls, the total time, the remote share "
                  "and the time on one node, and say which pair of classes keeps its calls "
                  "local although both are away from `main`. You can check your figures "
                  "afterwards by typing the records into the lab."),
            ("p", "Where a boundary cannot be removed, Fowler puts a coarse-grained object on "
                  "it. The next lesson, Remote Facade, reads that pattern and counts what it "
                  "saves."),
        ],
        "lab": ("eakit", {
            "mode": "remote",
            "view": "boundary",
            "preset": "by-class",
            "calls": _BY_CLASS_CALLS,
            "remoteUs": "1000",
            "localUs": "1",
            "presets": [
                {"id": "by-class",
                 "label": "By class: order, customer, product and pricing each on its own node (illustrative)",
                 "nodes": "order=orders; customer=customers; product=catalog; pricing=pricing",
                 "expect": {"rrRemote": "75", "rrTime": "75,000", "rrRatio": "1,000×"}},
                {"id": "one-process",
                 "label": "One process: every class on one node, as in each copy of a cluster",
                 "nodes": "",
                 "expect": {"rrRemote": "0", "rrTime": "75", "rrRatio": "1×"}},
            ],
            "panel_title": "Price a design's calls across nodes",
            "panel_intro": (
                "Each record is one pair of classes and how many times the first calls the "
                "second; each node assignment puts a class on a named node. The times are "
                "the lesson's, in microseconds, and the ratio of a remote call to a local one "
                "is the lesson's illustration of Fowler's orders of magnitude, not a "
                "measurement."
            ),
        }),
        "steps_title": "Pricing a design's calls across nodes",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the calls and the nodes",
             "Write each pair of classes that call each other with the number of calls for "
             "one piece of work, and the node each class runs on."),
            ("Mark each call remote or local",
             "A call is remote when its caller and callee are on different nodes, local when "
             "they share one, wherever that node is."),
            ("Price both deployments",
             "Multiply the remote calls by the remote cost and the local calls by the local "
             "cost, and add. Then price every call at the local cost, for one node, and "
             "divide the first time by the second."),
            ("Do it on a system you know",
             "Take one service boundary in a system you know and one user action that "
             "crosses it. Count the calls that cross the boundary, write the figure, and say "
             "in one sentence which of them could stay inside one process."),
        ],
        "worked": {
            "title": "Four classes on four nodes",
            "intro": [
                "Take the preset <code>by-class</code> and price it, then price the same calls "
                "in one process.",
            ],
            "lines": [
                "calls: 20 + 10 + 30 + 15, which is 75",
                "every pair is on two nodes: 75 remote",
                "time: 75 calls at 1,000 µs, 75,000 µs",
                "one node: 75 calls at 1 µs, 75 µs",
                "ratio: 75,000 over 75, which is 1,000",
            ],
            "after": [
                "Every call in this design crosses a node, so the design pays the remote "
                "price on all of them: 75 ms of waiting against 75 µs of work. That the ratio "
                "equals the cost ratio is a sign that nothing in the design stayed local.",
            ],
        },
        "quiz_title": "Remote calls and the chapter's claims",
        "quiz": [
            {"q": "Price the exercise: calls `web, cart, 12; cart, stock, 8; cart, tax, 8; "
                  "tax, rates, 16`, with `web` on a front node, `tax` and `rates` on a back "
                  "node, a remote call at 800 µs and a local one at 2 µs. How many calls are "
                  "remote, and what is the total time?",
             "a": ["20 remote, 16,048 µs",
                   "36 remote, 28,816 µs",
                   "12 remote, 9,664 µs",
                   "44 remote, 35,200 µs"],
             "c": 0,
             "why": "There are 44 calls. The 12 from `web` to `cart` cross from the front "
                    "node to `main`, and the 8 from `cart` to `tax` cross from `main` to the "
                    "back node: 20 remote. `cart` and `stock` share `main`, and `tax` and "
                    "`rates` share the back node, so `tax, rates` stays local although both "
                    "are away from `main`. The time is 20 × 800 + 24 × 2 = 16,048 µs, the "
                    "remote share 16,000/16,048 = 1,000/1,003 ≈ 99.7%, against 44 × 2 = 88 µs "
                    "on one node, 2,006/11 ≈ 182.4×. Counting `tax, rates` as remote gives "
                    "36; counting only the front node's calls gives 12."},
            {"q": "In the preset by-class, the customer class is moved onto the orders node "
                  "(`customer=orders`), and nothing else changes. How many of the 75 calls "
                  "are now remote?",
             "a": ["55", "65", "10", "75"],
             "c": 1,
             "why": "Only the 10 calls from `order` to `customer` become local, since both "
                    "classes are now on `orders`. The screen's 20 calls to the order, and the "
                    "order's 30 to the product and 15 to pricing, still cross a node: 65 "
                    "remote, 65,010 µs. Ten is the number that became local, not the number "
                    "left remote."},
            {"q": "How does Chapter 7 say to use several processors, instead of putting each "
                  "kind of object on its own node?",
             "a": ["Give each busy component more boxes and balance the load across them",
                   "Put every class in one process and run copies of that process on the "
                   "nodes",
                   "Give every remotable class a coarse-grained interface",
                   "Rely on the middleware's transparency to make remote calls local"],
             "c": 1,
             "why": "That is clustering (Remote and Local Interfaces): each copy makes local "
                    "calls and keeps fine-grained interfaces. More boxes for a busy component "
                    "is the opening design's own reason. Coarse interfaces on every class "
                    "still leave too many remote calls, the chapter says, and transparency "
                    "does not extend to performance."},
            {"q": "Which of these is not one of the boundaries Where You Have to Distribute "
                  "names?",
             "a": ["Between a client on the desktop and the shared data on a server",
                   "Between the application server and the database",
                   "Between the web server and the application server",
                   "Between the order and customer classes, so that each can be scaled "
                   "separately"],
             "c": 3,
             "why": "The section names client and server, application server and database, "
                    "web server and application server, a vendor's package, and, rarely, a "
                    "genuine need to split the application server's software. Splitting "
                    "classes so that each can be scaled is the design the chapter opens with "
                    "and argues against."},
        ],
        "mistakes": [
            ("Thinking that distributing by class spreads the load",
             "The opening design gives each kind of object its own node so that a busy one "
             "can be given more boxes. What it spreads is the calls' cost: every call "
             "between those objects now pays the remote price, orders of magnitude above the "
             "local one. On the lesson's illustration, <code>by-class</code> takes 75,000 µs "
             "for the work <code>one-process</code> does in 75. Fowler's alternative, "
             "clustering, spreads the load by running copies of the whole application, with "
             "every call still local."),
            ("Treating a remote call as a slower local call",
             "If speed were the only difference, a slow interface could be used remotely "
             "and a fast one locally with the same methods. The chapter says the difference "
             "also changes the interface: a local object is best fine-grained, a remote one "
             "must be coarse-grained, and an object that might ever be remote has to pay for "
             "the coarse-grained programming model. That is why one class cannot serve "
             "both."),
            ("Trusting transparent middleware to remove the cost",
             "Vendors say a local call through their middleware runs at local speed and "
             "you pay only for the remote calls you make. Fowler grants that this is to some "
             "extent true, and says it misses the point: you still have to decide, for every "
             "pair of objects, which interface they use, and an object that may be remote "
             "needs the coarse one. Transparency hides where the callee is, not what the "
             "call costs."),
        ],
        "standard": (
            "Finish when you can price a deployment's calls by hand.",
            "Given calls between classes and the node each class is on, compute the remote "
            "calls, the total time and the ratio to the time on one node, and say which "
            "calls a move of one class would make local."
        ),
        "note": (
            "The lab prices every remote call at one cost and every local call at another, "
            "and both are the lesson's. Real remote calls vary with marshalling, security "
            "checks and the distance between machines, and a call that carries a megabyte "
            "costs more than one that carries a number; the lab counts calls, not bytes, "
            "until the Data Transfer Object lesson. What it shows is how many calls a "
            "deployment makes cross a node, which is what the First Law is about."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 15, Remote Facade, PDF pp. 352-362 of the operator's copy (How It
    # Works pp. 352-354, When to Use It p. 355; the example, pp. 355-362, is
    # pointed to, not used).
    # Quote: PDF p. 355 of the operator's copy, 13 words, ea_quotes.py OK.
    # "Remote Facade has no domain logic.": PDF p. 354 of the operator's copy,
    # 6 words, ea_quotes.py OK. Lesson total: 19 words.
    {
        "slug": "remote-facade",
        "title": "Remote Facade",
        "module": "Chapter 15 · Distribution Patterns",
        "one_line": "A thin, coarse-grained object on the process boundary that turns one remote call into the several local calls the fine-grained objects behind it need.",
        "summary": (
            "Remote Facade puts a coarse-grained interface over a web of fine-grained "
            "objects, so that a remote client makes one call where it would have made "
            "several, while the objects behind it keep their small methods for local use. "
            "Compute the time fine-grained calls take across a network against the "
            "facade's coarse calls, and see how the saving depends on the latency."
        ),
        "key": [
            "one remote call, many local calls behind",
            "the facade translates; it holds no logic",
            "fine time: calls times latency plus work",
            "coarse time: trips times latency, plus work",
            "the facade removes waits, not work",
        ],
        "key_label": "Remote Facade in five lines",
        "concepts_intro": (
            "Three terms from the pattern. The second is the one Fowler insists on."
        ),
        "concepts": [
            ("Remote Facade",
             "A coarse-grained object at the process boundary over many fine-grained "
             "objects. None of the fine-grained objects has a remote interface; the facade "
             "translates each coarse call into the calls on them, and does nothing more."),
            ("No domain logic",
             "Fowler's description of the facade: it holds no domain logic. Validation, "
             "computation and workflow stay in the fine-grained objects, or in a separate "
             "Transaction Script that is not remote, so that the whole application can run "
             "locally without the facade."),
            ("Bulk accessor",
             "One getter or setter that reads or writes a group of values at once, such as "
             "a whole address, where the fine-grained object has one accessor for each value. "
             "A facade's methods are usually bulk accessors and commands, shaped for one "
             "client's screens."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Chapter 15's Remote Facade in your own copy first, up to the end of When "
            "to Use It; the example that follows is worth reading in the book. The lesson "
            "sets out how the pattern works and then counts what one facade saves on two "
            "networks."
        ),
        "body": [
            # PDF p. 355 of the operator's copy.
            ("p", "&ldquo;Use Remote Facade whenever you need remote access to a "
                  "fine-grained object model.&rdquo; The previous lesson ended at the "
                  "boundaries you cannot remove; this one reads the pattern Fowler puts on "
                  "them, in Chapter 15, Distribution Patterns. It is a pattern, to be looked "
                  "up and used, and the lesson reads it as a tool: what it is, what it must "
                  "not hold, and when it pays."),
            ("p", "The problem is the one Chapter 7 set. An object model works best with "
                  "small objects and small methods, which gives control, substitution and "
                  "names that reveal intent, and means many calls between objects. Between "
                  "processes each call is expensive: data has to be marshalled, security may "
                  "be checked, packets routed, and across the globe the speed of light starts "
                  "to matter. Any object meant to be used remotely therefore needs a "
                  "coarse-grained interface, and that affects the whole object structure: you "
                  "update an order and its lines in one call, and give up the clear intent of "
                  "small methods."),
            ("p", "Remote Facade keeps both. It is a coarse-grained facade over a web of "
                  "fine-grained objects; none of those objects has a remote interface, and "
                  "the facade contains no domain logic. All it does is translate. In the "
                  "simplest case it replaces an address's getters and setters with one bulk "
                  "getter and one bulk setter, which call the real object's accessors and do "
                  "nothing more, so that validation and computation stay on the address. More "
                  "often one facade has many methods, each passing on data from several "
                  "objects, and Fowler prefers few facades with many methods each, perhaps "
                  "one for a moderate application, where others make one per use case. A "
                  "facade is designed for one client's usage, typically a family of screens, "
                  "and two of its methods may do much the same thing underneath, because the "
                  "client thinks of them as different commands."),
            # PDF p. 354 of the operator's copy.
            ("p", "Three further points from How It Works. A facade can be stateless, and "
                  "pooled, or stateful, which makes Server Session State easy and may not "
                  "scale to thousands of users. Its methods are the natural place for "
                  "security and for transactions: start one, do the work, commit before the "
                  "call returns. And it must stay thin. Fowler asks you to repeat a "
                  "sentence three times, and it is worth repeating here once: "
                  "&ldquo;Remote Facade has no domain logic.&rdquo; Workflow goes in the "
                  "fine-grained objects or in a Transaction Script that is not remote, and "
                  "the application should still run, whole, in one process with no facade "
                  "at all. That is also how he tells it apart from the Session Facade of "
                  "Alur, Crupi and Malks, which as usually described holds workflow logic, and "
                  "from Stafford's Service Layer, in Fowler's book, which need not be remote "
                  "and may sit under a facade."),
            ("p", "When to Use It answers the quotation's question. The commonest use is "
                  "between a presentation and a Domain Model in different processes, such "
                  "as a desktop client and a server model, or a servlet and an object model "
                  "when the web and application servers are separate. The cost of a call "
                  "between processes on the same machine is large enough to need it too. "
                  "Within one process it is not needed, and it is not usually used with a "
                  "Transaction Script, which is coarse-grained already. It implies "
                  "synchronous calls, and Fowler notes that asynchronous messaging can do "
                  "better, outside the book's scope."),
            ("code", _lines(CUSTOMER_FACADE)),
            ("p", "The snippet is one facade method. A remote client calls `moveHouse` "
                  "(lines 9 to 15) once, with the new street, city and postcode. Inside the "
                  "server's process the facade makes five local calls: it finds the "
                  "customer, sets the three parts of the address one by one, and saves. "
                  "Nothing in it decides anything. If a postcode must be checked against its "
                  "city, that rule belongs to the address, where the local code that uses "
                  "`setPostcode` gets it too."),
            ("p", "Now the count. The lab reads records `operation, fine`: each record is "
                  "one coarse-grained call that does the work of that many fine-grained "
                  "ones. With the latency of a round trip and the work in each fine-grained "
                  "call, it gives the round trips each way, the time of the fine-grained "
                  "calls (each pays a latency and its work), the time of the coarse calls "
                  "(one latency each, plus all the work), the share of the fine-grained time "
                  "spent waiting, and the ratio of the two times. It assumes the work is the "
                  "same either way."),
            ("p", "The preset <code>move-house</code> has two facade methods, "
                  "`moveHouse`, which does the work of 5 fine-grained calls, and "
                  "`showCustomer`, a bulk getter in place of 6, at a latency of 20 ms and "
                  "0.5 ms of work a call. The fine-grained client makes 11 round trips, "
                  "451/2 = 225.50 ms, 40/41 ≈ 97.6% of it waiting; the facade makes 2, "
                  "91/2 = 45.50 ms, and the speed-up is 451/91 ≈ 5.0×."),
            ("p", "The preset <code>on-a-fast-network</code> cuts the latency to 1 ms. Now "
                  "the fine-grained calls take 33/2 = 16.50 ms, 2/3 ≈ 66.7% of it waiting, "
                  "against 15/2 = 7.50 ms through the facade: 11/5 ≈ 2.2×. The facade removes "
                  "waits, not work, so it saves most where the waits are most of the time. "
                  "On the lesson's illustration even a fast network leaves two thirds of the "
                  "fine-grained time in waiting, which is Fowler's point about processes on "
                  "one machine."),
            ("h3", "Exercise"),
            ("ul", [
                "A trip-booking service whose facade has three methods: `bookTrip`, doing the "
                "work of 8 fine-grained calls; `cancelTrip`, of 3; and `showTrip`, of 9.",
                "A latency of 15 ms a round trip, and 1 ms of work in each fine-grained call.",
            ]),
            ("p", "Find by hand the round trips each way, the time of the fine-grained calls "
                  "and of the facade's calls, the speed-up, and the share of the "
                  "fine-grained time spent waiting."),
            ("p", "A coarse call has to carry its data in one piece. The next lesson, Data "
                  "Transfer Object, reads the object that carries it and weighs what it "
                  "sends."),
        ],
        "lab": ("eakit", {
            "mode": "remote",
            "view": "calls",
            "preset": "move-house",
            "ops": "moveHouse, 5; showCustomer, 6",
            "workMs": "0.5",
            "presets": [
                {"id": "move-house",
                 "label": "moveHouse and showCustomer at 20 ms a round trip (illustrative)",
                 "latencyMs": "20",
                 "expect": {"rrFineMs": "451/2 = 225.50", "rrCoarseMs": "91/2 = 45.50",
                            "rrSpeedup": "451/91 ≈ 5.0×"}},
                {"id": "on-a-fast-network",
                 "label": "The same facade at 1 ms a round trip (illustrative)",
                 "latencyMs": "1",
                 "expect": {"rrFineMs": "33/2 = 16.50", "rrCoarseMs": "15/2 = 7.50",
                            "rrSpeedup": "11/5 ≈ 2.2×"}},
            ],
            "panel_title": "What a Remote Facade saves",
            "panel_intro": (
                "Each record is one facade method and the number of fine-grained calls it "
                "does the work of. A fine-grained call pays a round trip and its work; a "
                "facade call pays one round trip, and the work of all the calls behind it."
            ),
            "source": "illustrative, the lesson's own; none is the book's",
        }),
        "steps_title": "Counting what a facade saves",
        "steps_intro": "Four steps, the last of them on a screen of your own.",
        "steps": [
            ("Count the round trips",
             "Add up the fine-grained calls each facade method replaces: that is the "
             "fine-grained client's round trips. The facade's are the number of its "
             "methods called."),
            ("Price the fine-grained calls",
             "Each pays one latency and its own work: multiply the calls by the sum of the "
             "two."),
            ("Price the facade's calls",
             "Each facade call pays one latency; the work of every fine-grained call is still "
             "done, inside the server. Add the two, and divide the first time by this one."),
            ("Do it on a screen you know",
             "Take one screen in a system you know that calls a remote API. Count the calls "
             "it makes to draw itself, write the figure, and say in one sentence which of "
             "them one facade method could replace."),
        ],
        "worked": {
            "title": "Two facade methods at 20 ms",
            "intro": [
                "Take the preset <code>move-house</code>: 5 and 6 fine-grained calls, 20 ms "
                "latency, 0.5 ms work.",
            ],
            "lines": [
                "fine-grained: 11 trips at 20.5 ms",
                "fine-grained time: 225.5 ms",
                "facade: 2 trips at 20 ms, which is 40 ms",
                "facade work: 11 calls at 0.5 ms, 5.5 ms",
                "facade time: 45.5 ms",
                "speed-up: 225.5 over 45.5, about 5 times",
            ],
            "after": [
                "The work, 5.5 ms, is the same on both sides. Everything the facade saves is "
                "the nine round trips it did not make, 180 ms of waiting.",
            ],
        },
        "quiz_title": "Facades, round trips and the pattern's rules",
        "quiz": [
            {"q": "Count the exercise: a facade with `bookTrip` (8 fine-grained calls), "
                  "`cancelTrip` (3) and `showTrip` (9), a latency of 15 ms and 1 ms of work a "
                  "fine-grained call. What are the two times?",
             "a": ["320 ms fine-grained, 65 ms through the facade, about 4.9× faster",
                   "320 ms fine-grained, 45 ms through the facade, about 7.1× faster",
                   "300 ms fine-grained, 65 ms through the facade, about 4.6× faster",
                   "20 ms fine-grained, 3 ms through the facade, about 6.7× faster"],
             "c": 0,
             "why": "There are 20 fine-grained calls against 3 facade calls. The fine-grained "
                    "time is 20 × (15 + 1) = 320 ms, 15/16 ≈ 93.8% of it waiting; the facade's "
                    "is 3 × 15 + 20 × 1 = 65 ms, and 320/65 = 64/13 ≈ 4.9×. Leaving out the "
                    "work the facade still does gives 45 ms; leaving it out of the "
                    "fine-grained time gives 300; 20 and 3 are the round trips, not times."},
            {"q": "A facade method has to check that a booking's dates do not overlap "
                  "another booking. Where does the pattern say that rule belongs?",
             "a": ["In the facade method, since that is where the client's call arrives",
                   "In the fine-grained objects, or in a Transaction Script that is not "
                   "remote",
                   "In the Data Transfer Object the facade returns",
                   "In the client, so that the facade stays thin"],
             "c": 1,
             "why": "Remote Facade has no domain logic: if workflow or coordination is "
                    "needed, Fowler puts it in the fine-grained objects or a separate "
                    "nonremotable Transaction Script, so the application can run locally "
                    "without the facade. A transfer object carries data and has no behaviour, "
                    "and moving the rule to the client only puts the logic on the other side "
                    "of the wire."},
            {"q": "A single facade method replaces 5 fine-grained calls. The latency is 20 ms "
                  "and the work in each call is 0. What is the speed-up?",
             "a": ["1×", "4×", "5×", "25×"],
             "c": 2,
             "why": "Fine-grained: 5 × 20 = 100 ms. Facade: one round trip, 20 ms, and no "
                    "work. 100/20 = 5×. With no work the speed-up is just the number of "
                    "round trips saved over one; work would bring it down."},
            {"q": "Which of these does When to Use It say needs no Remote Facade?",
             "a": ["A desktop client calling a domain model on a server",
                   "A servlet calling an object model in a separate application server",
                   "A CGI script calling a Domain Model in the same web server process",
                   "Two processes on the same machine"],
             "c": 2,
             "why": "Within a single process no conversion is needed, and Fowler names a CGI "
                    "script and a Domain Model in one web server as such a case. Two "
                    "processes on one machine still need a coarse-grained interface: the "
                    "section says the cost of an inter-process call on the same box is large "
                    "enough."},
        ],
        "mistakes": [
            ("Putting the business logic in the facade",
             "The facade is where the remote call arrives, so it looks like the place to "
             "decide things. Fowler calls this one of the biggest mistakes he sees: the "
             "facade is a thin layer that translates coarse calls into fine-grained ones, and "
             "the logic stays in the objects behind it. In the snippet, `moveHouse` sets "
             "the address and saves; any rule about addresses is the address's. Logic in "
             "the facade cannot be used by local code without going through it, and the "
             "whole application can no longer run without the facade."),
            ("Making the domain objects coarse-grained so they can be called remotely",
             "It removes the round trips, and gives up what the fine-grained model was for: "
             "small objects and methods that can be combined, overridden and read. The facade "
             "exists so that you do not have to choose. Local code keeps the fine-grained "
             "objects, and only the boundary gets the coarse interface, where it is obvious "
             "that a call is remote."),
            ("Thinking a facade matters only between machines",
             "On the lesson's illustration the facade saves least at the lowest latency, and "
             "it is tempting to drop it when the processes share a box. When to Use It says "
             "the cost of a call between processes on the same machine is large enough to "
             "need a coarse-grained interface regardless of where the processes live. The "
             "line Fowler draws is the process, not the machine."),
        ],
        "standard": (
            "Finish when you can price a facade's saving by hand.",
            "Given facade methods and the fine-grained calls each replaces, a latency and a "
            "work time, compute the time of the fine-grained calls and of the facade's, and "
            "the speed-up."
        ),
        "note": (
            "The lab assumes the work is the same either way and that each call pays one "
            "fixed latency. A real facade call carries more data than a fine-grained one, so "
            "it takes longer to send, and the next lesson's lab puts that back. The lab "
            "cannot tell whether a facade holds domain logic; that is read in the code."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 15, Data Transfer Object, PDF pp. 363-372 of the operator's copy
    # (How It Works pp. 363-366, When to Use It p. 366; the examples are pointed
    # to, not used). Chapter 6, Session State, PDF p. 90 (F20).
    # Quote: PDF p. 363 of the operator's copy, 26 words, ea_quotes.py OK; "its"
    # for "it's" is the book's, as printed. Lesson total: 26 words.
    {
        "slug": "data-transfer-object",
        "title": "Data Transfer Object",
        "module": "Chapter 15 · Distribution Patterns",
        "one_line": "An object with no behaviour that carries everything one call needs across a process boundary, built from the domain by an assembler.",
        "summary": (
            "A Data Transfer Object bundles the data for a call, from several domain "
            "objects, into one serializable object, so that a remote client asks once. "
            "Compute the time of one getter call per field against one object carrying every "
            "field, the bytes it sends that the screen never shows, and how many bytes the "
            "saved round trips could have carried."
        ),
        "key": [
            "one call carries all the data it needs",
            "shaped for the screen, not the domain",
            "an assembler builds it from the domain",
            "a getter each: calls times latency",
            "send too much rather than call twice",
            "extra bytes against saved round trips",
        ],
        "key_label": "Data Transfer Object in six lines",
        "concepts_intro": (
            "Three terms from the pattern. The third keeps the other two apart."
        ),
        "concepts": [
            ("Data Transfer Object",
             "An object that carries the data for one remote call: fields, getters and "
             "setters, no behaviour. It is serializable, it holds only simple values and other "
             "transfer objects, and its class is present on both sides of the wire."),
            ("Serialization",
             "Turning an object into bytes to send, and back on arrival. The book weighs "
             "binary forms, compact but fragile when the class changes, against text forms "
             "such as XML, easy to read and more tolerant of change but larger and slower."),
            ("Assembler",
             "A separate object on the server that builds a transfer object from the domain "
             "objects and updates the domain from one, so that neither depends on the other. "
             "The book calls it an example of Mapper."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Chapter 15's Data Transfer Object in your own copy first, to the end of "
            "When to Use It. The lesson sets out how it works and then weighs one transfer "
            "object against a getter a field, in two encodings."
        ),
        "body": [
            # PDF p. 363 of the operator's copy; "its" for "it's" as printed.
            ("p", "&ldquo;Due to the latency costs of remote calls, its better to err on the "
                  "side of sending too much data than have to make multiple calls.&rdquo; The "
                  "sentence is from How It Works in Chapter 15's Data Transfer Object, and it "
                  "is the pattern's argument in one line. A Remote Facade needs coarse "
                  "methods; this lesson reads the coarse object those methods take and "
                  "return."),
            ("p", "Each call to a remote interface is expensive, so each call has to carry "
                  "more data. Many parameters would do it for an update, awkwardly, but Java "
                  "returns only one value. So the pattern makes one object to hold all the "
                  "data for the call. It must be serializable to cross the connection, and "
                  "an assembler on the server usually moves data between it and the domain "
                  "objects. Fowler admits it is the kind of object you were brought up not to write, "
                  "a bag of fields and accessors, whose whole value is that it moves many "
                  "pieces of information in one call."),
            ("p", "What goes in it is decided by the client, not the domain. A transfer "
                  "object usually carries more than the remote object asked for, data from "
                  "the order, the customer, the lines and the delivery, everything the client "
                  "will want for a while. Domain objects themselves usually cannot be sent: "
                  "they are tied into a web of references that is hard to serialize, and you "
                  "would not want the domain classes on the client. So the fields are "
                  "primitives, strings, dates and other transfer objects, arranged as a simple "
                  "hierarchy. Transfer objects are often shaped for one web page or screen; "
                  "whether to have one for a whole interaction or one per request, and one for "
                  "request and response or two, Fowler says has no blanket rule. A Record "
                  "Set is the transfer object for a SQL database, and suits Table Module."),
            # F20, PDF p. 90 of the operator's copy.
            ("p", "Serializing the Data Transfer Object weighs the forms. Use the platform's "
                  "built-in serialization when there is one. Text forms such as XML are easy "
                  "to read and to generate, but need more bandwidth for the same data, XML "
                  "especially, and can be markedly slower. Binary forms are fragile: a change "
                  "as small as adding an optional field can break an out-of-date client, "
                  "where XML can be written to tolerate it. Chapter 6, Session State, gives "
                  "the book's illustration of the size: one application's session data, sent "
                  "as XML, came to about a megabyte, which one of Fowler's team likened to "
                  "three Shakespeare plays."),
            ("p", "Assembling a Data Transfer Object from Domain Objects keeps the two "
                  "apart. The transfer object is deployed on both sides of the wire, so it "
                  "must not depend on the domain; and the domain should not depend on it, "
                  "because its shape changes with the interface. A separate assembler builds "
                  "one from the other. When to Use It is brief: whenever several items of "
                  "data must cross between two processes in one call, and in particular to "
                  "hide an XML document behind an explicit interface. One naming note: much "
                  "of the J2EE world called this pattern a value object, which in this book "
                  "is something else, the small immutable object read in the Value Object "
                  "lesson of the second course."),
            ("code", _lines(ORDER_DTO)),
            ("p", "The snippet is a transfer object shaped for one screen. Lines 3 to 7 hold "
                  "what the order screen shows: the order's id, the customer's name, the "
                  "status, the total and a summary of each line, gathered from at least three "
                  "domain objects by an assembler the snippet leaves out. It has no "
                  "behaviour, and nothing in it refers to a domain class, so the client can "
                  "hold the class without the domain."),
            ("p", "Now the count. The lab reads records `field, bytes, needed`, one per "
                  "field the server could send, with a latency, a bandwidth in bytes a "
                  "millisecond and an encoding factor, the encoded size over the raw bytes. "
                  "It compares two designs. The getter design makes one call for each field "
                  "the screen needs; the transfer object is one call carrying every field. "
                  "The tiles are the getter calls, the time of the getters (a latency each "
                  "and their bytes at the bandwidth), the bytes in the transfer object, its "
                  "time (one latency and all its bytes), the bytes it carries that the "
                  "screen does not need, and the bytes the saved round trips could have "
                  "carried: one fewer than the getter calls, times the latency, times the "
                  "bandwidth. The model sends data at a steady rate after a fixed latency, "
                  "and the panel says real networks are lumpier."),
            ("p", "The preset <code>order-screen</code> is the snippet's screen, with a "
                  "4,000-byte `notes` field the screen does not show, as if the assembler had "
                  "copied the whole order: the err-on-the-side-of-too-much case. At 20 ms "
                  "and 1,000 bytes a millisecond, five getters take 51,033/500 ≈ 102.07 ms; "
                  "one transfer object of 6,066 bytes takes 13,033/500 ≈ 26.07 ms, though "
                  "4,000 of its bytes are never shown. The four round trips it saved could "
                  "have carried 80,000 bytes, twenty times the waste."),
            ("p", "The preset <code>as-xml</code> sends the same fields at three times their "
                  "raw size, the lesson's stand-in for a text encoding; the factor is "
                  "illustrative, not the book's. The getters now take 53,099/500 ≈ 106.20 ms "
                  "and the transfer object, 18,198 bytes with 12,000 of them unneeded, "
                  "19,099/500 ≈ 38.20 ms. The encoding costs the transfer object far more "
                  "than the getters, because it sends more bytes, and it is still the faster "
                  "design here. Whether it stays faster depends on how many bytes it wastes "
                  "against what the saved trips could have carried, and the exercise is a "
                  "case to test that."),
            ("h3", "Exercise"),
            ("ul", [
                "A profile screen that shows a member's `name` (30 bytes) and `email` (40 "
                "bytes). The server also holds a `photo` of 60,000 bytes and a `history` of "
                "9,000 bytes, which the screen does not show.",
                "A latency of 10 ms, 2,000 bytes a millisecond, and an encoding factor of 1.",
            ]),
            ("p", "Find by hand the time of one getter for each field the screen needs, the "
                  "time of one transfer object carrying all four fields, and the time of one "
                  "carrying only the two the screen shows, and say which is fastest and why "
                  "the quotation's advice does not settle it."),
            ("p", "With a facade and its transfer objects the boundary is designed. The next "
                  "lesson, Putting It All Together, reads Fowler's summary of the whole book, "
                  "and prices one request through every layer under three deployments."),
        ],
        "lab": ("eakit", {
            "mode": "remote",
            "view": "payload",
            "preset": "order-screen",
            "fields": _ORDER_FIELDS,
            "latencyMs": "20",
            "bytesPerMs": "1000",
            "presets": [
                {"id": "order-screen",
                 "label": "The order screen, with the notes it does not show (illustrative)",
                 "factor": "1",
                 "expect": {"rrGetterMs": "51,033/500 ≈ 102.07", "rrDtoMs": "13,033/500 ≈ 26.07",
                            "rrExtraBytes": "4,000"}},
                {"id": "as-xml",
                 "label": "The same fields, encoded at three times their size (illustrative)",
                 "factor": "3",
                 "expect": {"rrGetterMs": "53,099/500 ≈ 106.20", "rrDtoMs": "19,099/500 ≈ 38.20",
                            "rrExtraBytes": "12,000"}},
            ],
            "panel_title": "One getter a field, or one transfer object",
            "panel_intro": (
                "Each record is one field the server could send, its size in bytes and "
                "whether the screen needs it. The getter design makes one call for each needed "
                "field; the transfer object is one call carrying every field. The factor is "
                "the lesson's stand-in for an encoding's size against the raw bytes."
            ),
            "source": "illustrative, the lesson's own; none is the book's",
        }),
        "steps_title": "Weighing a transfer object",
        "steps_intro": "Four steps, the last of them on an API response of your own.",
        "steps": [
            ("Price the getters",
             "Count the fields the screen needs: one call each, one latency each, and their "
             "bytes, encoded, at the bandwidth."),
            ("Price the transfer object",
             "One latency, and every field it carries, encoded, at the bandwidth. Note the "
             "bytes the screen does not need."),
            ("Weigh the waste against the trips",
             "The round trips the transfer object saved are one fewer than the getters. "
             "Multiply them by the latency and the bandwidth for the bytes they could have "
             "carried, and compare that with the unneeded bytes."),
            ("Do it on a response you know",
             "Take one API response in a system you know. Weigh it in bytes, count the fields "
             "its client actually uses, write both figures, and say in one sentence whether "
             "a smaller response or fewer calls would save more."),
        ],
        "worked": {
            "title": "The order screen at 20 ms",
            "intro": [
                "Take the preset <code>order-screen</code>: five needed fields of 2,066 bytes, "
                "and notes of 4,000 bytes.",
            ],
            "lines": [
                "getters: 5 trips at 20 ms, 100 ms",
                "getters: 2,066 bytes at 1,000 a ms",
                "getter time: about 102.07 ms",
                "one object: 1 trip, 20 ms",
                "one object: 6,066 bytes at 1,000 a ms",
                "object time: about 26.07 ms",
            ],
            "after": [
                "The transfer object sends 4,000 bytes nobody sees and is still four times "
                "faster, because those bytes cost 4 ms and the four round trips it saved "
                "cost 80. That is the quotation in figures, on the lesson's illustration.",
            ],
        },
        "quiz_title": "Transfer objects, bytes and round trips",
        "quiz": [
            {"q": "Work the exercise: `name` 30 bytes and `email` 40, needed; `photo` 60,000 "
                  "and `history` 9,000, not needed; 10 ms latency, 2,000 bytes a millisecond, "
                  "factor 1. Which is faster, two getters or one transfer object carrying all "
                  "four fields?",
             "a": ["The two getters: 4,007/200 ≈ 20.04 ms against 8,907/200 ≈ 44.54 ms",
                   "The transfer object: 2,007/200 ≈ 10.04 ms against 4,007/200 ≈ 20.04 ms",
                   "The transfer object: 8,907/200 ≈ 44.54 ms against 69 ms for the getters",
                   "Neither: both take 20 ms, one latency each way"],
             "c": 0,
             "why": "Two getters cost 2 × 10 ms plus 70 bytes at 2,000 a ms, 4,007/200 ≈ "
                    "20.04 ms. One transfer object of 69,070 bytes costs 10 ms plus 34.535 ms, "
                    "8,907/200 ≈ 44.54 ms: here it is slower, because it carries 69,000 "
                    "unneeded bytes, more than the 20,000 the one saved round trip could have "
                    "carried. A transfer object shaped for the screen, with no photo and no "
                    "history, takes 2,007/200 ≈ 10.04 ms, the fastest of the three: that is "
                    "the second option's figure, which is not the object that carries all "
                    "four fields."},
            {"q": "Why does the pattern say you usually cannot send the domain objects "
                  "themselves across the boundary?",
             "a": ["Because Java objects cannot be serialized",
                   "Because they are tied into a web of references that is hard to "
                   "serialize, and the client should not need the domain classes",
                   "Because a transfer object is faster to build than a domain object",
                   "Because domain objects have no getters"],
             "c": 1,
             "why": "How It Works gives both reasons: a domain model is a complex web, "
                    "difficult if not impossible to serialize, and sending it would mean "
                    "copying the domain classes to the other side. Java serializes simple "
                    "objects without trouble, which is why transfer objects are kept simple."},
            {"q": "Which object, in the pattern, depends on both the domain objects and the "
                  "transfer object?",
             "a": ["The transfer object", "The domain object", "The assembler",
                   "The remote client"],
             "c": 2,
             "why": "The transfer object must not depend on the domain, because it is "
                    "deployed on both sides; the domain should not depend on it, because its "
                    "shape changes with the interface. The assembler, an example of Mapper, "
                    "knows both and moves data between them."},
            {"q": "A screen needs three fields. The latency is 10 ms and the bandwidth 500 "
                  "bytes a millisecond. How many bytes could the round trips saved by one "
                  "transfer object have carried?",
             "a": ["5,000", "10,000", "15,000", "1,500"],
             "c": 1,
             "why": "Three getters against one transfer object save two round trips. Each is "
                    "10 ms, at 500 bytes a millisecond: 2 × 10 × 500 = 10,000 bytes. Counting "
                    "three saved trips gives 15,000; one gives 5,000."},
        ],
        "mistakes": [
            ("Fetching each value only when the screen asks for it",
             "It looks economical: no byte crosses the wire unless it is shown. On the "
             "lesson's illustration it is five calls and 51,033/500 ≈ 102.07 ms, against "
             "13,033/500 ≈ 26.07 ms for one transfer object that also carries 4,000 bytes the "
             "screen never shows. The quotation gives the reason: a round trip costs more "
             "than the bytes most fields add, so Fowler would rather send too much than call "
             "again. The advice has a limit, which the exercise finds."),
            ("Taking a transfer object for a domain object with getters",
             "Both have fields and accessors, but a transfer object has no behaviour and is "
             "shaped by the call, often by one screen, gathering data from several domain "
             "objects. It must not refer to the domain, so that it can live on both sides of "
             "the wire. An assembler builds it; it does not build itself from the domain."),
            ("Choosing the encoding by size alone",
             "A binary form is smaller and faster, and the as-xml preset shows what three "
             "times the bytes costs. The book adds the other side: binary serialization is "
             "fragile, and a change as small as an optional field can break an out-of-date "
             "client, where XML can be written to tolerate changes. Size is one of the "
             "trade-offs, not the whole of it."),
        ],
        "standard": (
            "Finish when you can weigh a transfer object by hand.",
            "Given fields with sizes and whether the screen needs them, a latency, a "
            "bandwidth and an encoding factor, compute the getters' time and the transfer "
            "object's, the unneeded bytes it sends, and the bytes one saved round trip would "
            "have carried."
        ),
        "note": (
            "The lab models a network as a fixed latency and a steady rate, and an encoding "
            "as one factor on every byte; real networks send in packets and windows, and real "
            "encodings cost time to build and parse as well as to send. It cannot weigh the "
            "fragility of a binary form or the cost of keeping both sides' classes in step, "
            "which the book counts as part of the choice."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 8, Putting It All Together, PDF pp. 100-106 of the operator's
    # copy: Starting with the Domain Layer (p. 101), Down to the Data Source
    # Layer (pp. 102-103), The Presentation Layer (p. 103), Some
    # Technology-Specific Advice (pp. 104-106); Other Layering Schemes (pp.
    # 107-109).
    # Quote: PDF p. 100 of the operator's copy, 17 words, ea_quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "putting-it-all-together",
        "title": "Putting It All Together",
        "module": "Chapter 8 · Putting It All Together",
        "one_line": "Fowler's summary of the book: the domain-logic choice first, the data source and presentation it leads to, the platforms of 2002, and the other layering schemes mapped onto the patterns.",
        "summary": (
            "Chapter 8 sweeps the narratives together: choose the domain logic first, let it "
            "choose the data-source patterns, then the presentation, and keep everything in "
            "one process if you can. It closes by mapping five other layering schemes onto "
            "the patterns. Price one request's calls through every layer under three "
            "deployments."
        ),
        "key": [
            "choose the domain logic first",
            "the domain choice picks the data source",
            "one process if you can; a facade if not",
            "the platform advice is dated, by Fowler",
            "advice prods thinking; it is no recipe",
        ],
        "key_label": "Chapter 8 in five lines",
        "concepts_intro": (
            "Three ideas organise the chapter. None of them is new; that is the chapter's "
            "point."
        ),
        "concepts": [
            ("The central decision",
             "Fowler's name for the choice among Transaction Script, Table Module and Domain "
             "Model. The complexity of the domain logic drives it most, the difficulty of the "
             "database connection next, and the decisions below are shaped by it."),
            ("Mediating layers",
             "Layers that other schemes put between the three basic ones, such as a "
             "controller between presentation and domain or a data-mapping layer between "
             "domain and data source. Fowler treats them as patterns, Application Controller "
             "and Data Mapper, useful some of the time."),
            ("A deployment",
             "Which node each layer runs on. The same layers can run in one process or be "
             "split at the browser, the database, the service or the domain, and each "
             "split adds remote calls."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Chapter 8 in your own copy first, from its opening to the end of Other "
            "Layering Schemes. It is advice, and Fowler says how to read it. The lesson sets "
            "it out section by section and then prices one request under three deployments."
        ),
        "body": [
            # PDF p. 100 of the operator's copy.
            ("p", "&ldquo;Use this advice to prod your thinking, but don't use it as a "
                  "replacement for your thinking.&rdquo; Fowler writes that near the start of "
                  "Chapter 8, Putting It All Together, after borrowing Frodo's warning that "
                  "the Elves will say both no and yes. He even wonders whether the chapter "
                  "was needed, since it repeats earlier advice; he keeps it to put the "
                  "discussion in context, and reminds you that you know your own project "
                  "far better than he can. Read the chapter in your own copy first."),
            ("p", "He also says your decisions are not cast in stone. Architectural "
                  "refactoring is hard and its full costs are unknown, but it is possible, "
                  "and he recommends three practices that make it easier to change your mind: "
                  "continuous integration, test-driven development and refactoring. You will "
                  "need to change it, he adds, unless you are luckier or more skilful than "
                  "anyone he has met."),
            ("p", "Starting with the Domain Layer repeats Chapter 2, with a second force "
                  "added. The strongest force is still the complexity of the domain logic, "
                  "which nobody can yet measure; the second is the difficulty of the "
                  "connection to the database. Transaction Script is the simplest and is "
                  "easy to build on a relational database, but it handles complex logic "
                  "badly and invites duplication. Domain Model handles really complex logic "
                  "better than anything, Fowler says, but is hard to learn and hard to map to "
                  "tables. Table Module sits between them and fits a relational database, and "
                  "tools that work with Record Sets, very well. He calls this the central "
                  "decision, and lets it shape the rest."),
            # F22, PDF p. 102 of the operator's copy.
            ("p", "Down to the Data Source Layer follows each choice. A Transaction Script "
                  "takes a Row Data Gateway or a Table Data Gateway, with Optimistic Offline "
                  "Lock when one request loads data for editing and a later one saves it. A "
                  "Table Module takes a Table Data Gateway. A Domain Model that is fairly "
                  "simple, the book's illustration is a couple of dozen classes close to the "
                  "database, can use Active Record; a more complex one needs Data Mapper, "
                  "ideally with a mapping tool, and then most of the object-relational "
                  "patterns, Unit of Work above all."),
            ("p", "The Presentation Layer prefers an HTML browser to a rich client where you "
                  "can get away with it, with Model View Controller underneath, Page "
                  "Controller for a document-oriented site and Front Controller for complex "
                  "navigation, and Template View or Transform View as the team's skills "
                  "decide, with Two Step View for several looks. Then the sentence this "
                  "course turns on: run everything in one process if you can, and if you "
                  "cannot, wrap the domain layer in a Remote Facade and talk to the web "
                  "server with Data Transfer Objects."),
            # F23, PDF p. 104 of the operator's copy.
            ("p", "Some Technology-Specific Advice applies all this to Java and .NET, and "
                  "Fowler dates it himself: he is writing in early 2002, and technologies "
                  "change faster than patterns. For J2EE he says you do not need Enterprise "
                  "Java Beans to build a good application, wraps a Domain Model in session "
                  "beans acting as Remote Facades, and keeps entity beans local, since they "
                  "need fine-grained interfaces. For .NET, Table Module is the default, and "
                  "there is no real reason to split web server and domain into separate "
                  "processes. Stored procedures are an optimisation for clear performance "
                  "problems, not an architectural principle. Web services are for integrating "
                  "applications, not for building one: expose parts of an application as "
                  "Remote Facades, and remember the First Law."),
            ("p", "Other Layering Schemes compares the three layers with five others. The "
                  "Brown model adds two mediating layers, which Fowler reads as Application "
                  "Controller and Data Mapper. Core J2EE, after Alur, Crupi and Malks, splits "
                  "the presentation into the part on the client and the part on the server. "
                  "Microsoft DNA, after Kirtland, passes record sets up through every layer, "
                  "which Fowler reads as a Record Set acting as a Data Transfer Object over "
                  "Table Modules. Marinescu and Nilsson split the domain into a services layer "
                  "over a domain layer, which is Stafford's Service Layer over a Domain Model; "
                  "Fowler finds that split occasionally useful, and says designers he respects "
                  "disagree. Every mediating layer, to him, is an optional extra, added when "
                  "one of the three gets too complex."),
            ("code", _lines(PLACE_ORDER_STACK)),
            ("p", "The snippet is one request through the layers Fowler recommends for a "
                  "complex domain: a service method that opens a Unit of Work (line 4), "
                  "finds the cart through a mapper (line 5), lets the domain check it out "
                  "(line 6), registers the new order and the changed cart (lines 7 and 8), "
                  "and commits, the mappers writing the SQL (line 9). Every one of those "
                  "calls is cheap if the layers share a process. The lab asks what they cost "
                  "if they do not."),
            ("p", "The lab is the boundary view of the first lesson, with layers in place of "
                  "classes. One request makes 1 call from the browser to the page, 2 from "
                  "the page to the service, 40 from the service to the domain, 25 from the "
                  "domain to the mappers and 6 from the mappers to the database, 74 in all, "
                  "at 2,000 µs a remote call and 1 µs a local one. The preset "
                  "<code>web-and-database</code> puts the browser and the database on their "
                  "own nodes, the two boundaries Chapter 7 says you cannot avoid: 7 remote "
                  "calls, 14,067 µs, 14,067/74 ≈ 190.1× the time on one node."),
            ("p", "The preset <code>service-split-off</code> moves the service, domain and "
                  "mappers to an application node, a boundary above the Service Layer: 9 "
                  "remote calls, 18,065 µs. The preset <code>domain-split-off</code> leaves "
                  "the service with the page and moves the domain and mappers, a boundary "
                  "under the Service Layer: 47 remote calls, 94,027 µs. On the lesson's "
                  "illustration the first adds 2 remote calls to the unavoidable seven and "
                  "the second adds 40, which is why, when Fowler must split, he puts the "
                  "facade on the coarse side. The lab prices every remote hop alike, the "
                  "browser's and the database's; the panel says so."),
            ("h3", "Exercise"),
            ("ul", [
                "Calls for one screen of a phone app: `app, facade, 3; facade, domain, 30; "
                "domain, mapper, 20; mapper, db, 4`.",
                "Nodes: `app` on the phone; the facade, domain, mappers and database on the "
                "server's node, so that the only slow hop is the phone's.",
                "A remote call costs 50,000 µs and a local one 1 µs.",
            ]),
            ("p", "Find by hand the calls, the remote calls and the total time, the ratio to "
                  "one node, and the time if one Remote Facade method served the whole "
                  "screen in a single call, with the work behind it unchanged."),
            ("p", "Two of Chapter 18's base patterns let a system like this be wired "
                  "differently for its tests than for production. The next lesson, Plugin "
                  "and Service Stub, reads them."),
        ],
        "lab": ("eakit", {
            "mode": "remote",
            "view": "boundary",
            "preset": "web-and-database",
            "calls": _STACK_CALLS,
            "remoteUs": "2000",
            "localUs": "1",
            "presets": [
                {"id": "web-and-database",
                 "label": "Only the browser and the database apart (illustrative)",
                 "nodes": "browser=client; database=db",
                 "expect": {"rrRemote": "7", "rrTime": "14,067"}},
                {"id": "service-split-off",
                 "label": "The service, domain and mappers on an application node",
                 "nodes": "browser=client; service=app; domain=app; mapper=app; database=db",
                 "expect": {"rrRemote": "9", "rrTime": "18,065"}},
                {"id": "domain-split-off",
                 "label": "The domain and mappers apart from the page and the service",
                 "nodes": "browser=client; domain=app; mapper=app; database=db",
                 "expect": {"rrRemote": "47", "rrTime": "94,027"}},
            ],
            "panel_title": "One request under three deployments",
            "panel_intro": (
                "Each record is one pair of layers and how many times the first calls the "
                "second for one request; each node assignment puts a layer on a named node. "
                "One remote cost prices every hop alike, the browser's and the database's as "
                "well as any boundary between layers. The times are the lesson's, in "
                "microseconds."
            ),
        }),
        "steps_title": "Pricing a deployment of the layers",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Write the calls for one request",
             "List each pair of layers that call each other for one request, and how many "
             "times, from the browser down to the database."),
            ("Place the layers on nodes",
             "Mark the nodes you cannot avoid first, the client and the database, then any "
             "boundary between layers you are considering."),
            ("Price each deployment",
             "Count the calls that cross a node, price them and the local calls, and compare "
             "each deployment with the unavoidable one."),
            ("Do it on a system you know",
             "Write the layers of one system you know with the node each runs on. Count the "
             "calls that cross a node for one request, write the figure, and say in one "
             "sentence which boundary you would remove first."),
        ],
        "worked": {
            "title": "The two boundaries you cannot avoid",
            "intro": [
                "Take the preset <code>web-and-database</code>: the browser on a client node, "
                "the database on its own, everything else on one.",
            ],
            "lines": [
                "calls: 1 + 2 + 40 + 25 + 6, which is 74",
                "remote: browser to page 1, mappers to db 6",
                "remote: 7 calls at 2,000 µs, 14,000 µs",
                "local: 67 calls at 1 µs, 67 µs",
                "time: 14,067 µs",
            ],
            "after": [
                "Almost all the time is in seven calls, and none of them can be removed by "
                "rearranging the layers. Any further split can only add to it; the question "
                "is how much, and the two other presets answer it.",
            ],
        },
        "quiz_title": "Deployments and the chapter's advice",
        "quiz": [
            {"q": "Price the exercise: `app, facade, 3; facade, domain, 30; domain, mapper, "
                  "20; mapper, db, 4`, with only `app` on the phone, at 50,000 µs a remote "
                  "call and 1 µs a local one. How many calls are remote, and what is the time?",
             "a": ["3 remote, 150,054 µs",
                   "7 remote, 350,050 µs",
                   "57 remote, 2,850,000 µs",
                   "3 remote, 150,000 µs"],
             "c": 0,
             "why": "There are 57 calls, and only the 3 from the phone to the facade cross a "
                    "node, since the database shares the server's node. The time is 3 × "
                    "50,000 + 54 × 1 = 150,054 µs, almost all of it the three phone calls, "
                    "against 57 µs on one node (50,018/19 ≈ 2,632.5×). One Remote Facade "
                    "method for the screen would make it one call, about 50,054 µs. Counting "
                    "the database hop as remote gives 7; leaving out the 54 local calls gives "
                    "150,000."},
            {"q": "Down to the Data Source Layer: for a fairly simple Domain Model, the "
                  "book's illustration being a couple of dozen classes close to the database, "
                  "which pattern does Chapter 8 say makes sense?",
             "a": ["Active Record",
                   "Data Mapper, with a mapping tool",
                   "Table Module",
                   "Remote Facade"],
             "c": 0,
             "why": "The chapter says Active Record makes sense for such a model, with a "
                    "gateway if you want to decouple a little. Data Mapper is for more "
                    "complicated models. Table Module is a domain-logic pattern, not a data "
                    "source, and Remote Facade is for distribution."},
            {"q": "In the lab's three deployments, the boundary moves from above the Service "
                  "Layer (between the page and the service) to under it (between the service "
                  "and the domain). How many remote calls does the request make in each?",
             "a": ["9 and 47", "2 and 40", "7 and 47", "9 and 40"],
             "c": 0,
             "why": "Both keep the browser's 1 call and the mappers' 6 remote. Above the "
                    "Service Layer adds the page's 2 calls to the service: 9. Under it adds "
                    "the service's 40 calls to the domain: 47. Two and forty are what each "
                    "boundary adds, not the totals."},
            {"q": "Other Layering Schemes maps Marinescu's services layer, which sits above "
                  "his domain layer, onto which pattern?",
             "a": ["Application Controller", "Service Layer", "Data Mapper",
                   "Remote Facade"],
             "c": 1,
             "why": "Fowler reads Marinescu's services layer, and Nilsson's application "
                    "layer, as Service Layer over a Domain Model. Marinescu's application "
                    "layer, a split of the presentation, is the one he reads as Application "
                    "Controller."},
        ],
        "mistakes": [
            ("Reading the chapter as a decision procedure",
             "The chapter does go step by step, domain first, then data source, then "
             "presentation, and it is tempting to follow it like a flowchart. Fowler says "
             "otherwise in the quotation, warns that advice can do harm, and reminds you "
             "that you know your own project better than he can. The order is a way "
             "of thinking about the decisions, and the decisions remain yours."),
            ("Taking the technology advice for the chapter's point",
             "Some Technology-Specific Advice is the most concrete section, with entity "
             "beans, data sets and web services. Fowler dates it himself, to early 2002, "
             "and says technologies change much faster than the patterns. The patterns, and "
             "the forces that choose between them, are the point; the platform section "
             "shows them applied once."),
            ("Thinking the other layering schemes contradict the three layers",
             "Brown's five layers, Core J2EE's five and Nilsson's seven look like rivals. "
             "Fowler maps each onto his three, reading the extra layers as patterns the "
             "reader has met: Application Controller and Data Mapper as mediating layers, "
             "Service Layer as a split of the domain, Record Set as a transfer object. He "
             "treats them as optional extras, added when a layer gets too complex."),
        ],
        "standard": (
            "Finish when you can price a deployment of the layers by hand.",
            "Given the calls between layers for one request and the node each layer runs on, "
            "compute the remote calls and the time for each deployment, and say which "
            "boundaries Chapter 7 says you cannot avoid."
        ),
        "note": (
            "What has happened to distribution since 2002, services and then microservices, "
            "is argued largely in Chapter 7's vocabulary: coarse-grained interfaces at the "
            "boundary, transfer objects on the wire, a facade in front of each service. Some "
            "of it is argued against the First Law, on the ground that separate deployment, "
            "ownership and scaling of parts of a system can be worth the remote calls; others "
            "hold that the law still applies and the calls still cost what the chapter says. "
            "The lab cannot settle that: it prices calls, not the organisational reasons for "
            "a boundary, and it prices every hop alike."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 18, Plugin, by David Rice and Matt Foemmel, PDF pp. 441-444 of the
    # operator's copy; Service Stub, by David Rice, pp. 445-448. Separated
    # Interface is read in the first course.
    # Quote: PDF p. 446 of the operator's copy, 18 words, ea_quotes.py OK; the
    # words are David Rice's, in his pattern. Lesson total: 18 words.
    {
        "slug": "plugin-and-service-stub",
        "title": "Plugin and Service Stub",
        "module": "Chapter 18 · Base Patterns",
        "one_line": "Choose an interface's implementation in one place at configuration time, and give the tests a small, fast stand-in for a service they should not depend on.",
        "summary": (
            "Rice and Foemmel's Plugin links a Separated Interface to its implementation "
            "during configuration rather than compilation, in one place; Rice's Service Stub "
            "is the simplest implementation that lets development and tests go on without a "
            "slow or unavailable service. List what a change to a network library reaches "
            "with a direct dependency, and with an interface, a stub and a plugin."
        ),
        "key": [
            "plugin: link at configuration, not build",
            "one place chooses each implementation",
            "a stub stands in for a service in tests",
            "keep the stub as simple as possible",
            "a stub tests the caller, not the service",
        ],
        "key_label": "Plugin and Service Stub in five lines",
        "concepts_intro": (
            "Two patterns, and the interface they both rest on, from the first course."
        ),
        "concepts": [
            ("Separated Interface",
             "An interface declared apart from its implementation, so that the code that uses "
             "it depends on the interface alone. Read in the first course; both patterns here "
             "build on it."),
            ("Plugin",
             "By David Rice and Matt Foemmel: a factory that links each Separated Interface to "
             "its implementation from instructions stated at one external point and read at "
             "run time, so that a new configuration needs no rebuild."),
            ("Service Stub",
             "By David Rice: a local, fast, in-memory stand-in for a service the system "
             "depends on, such as a credit check, used during development and testing and "
             "kept as simple as possible."),
        ],
        "read_title": "The two patterns first, then the count",
        "read_intro": (
            "Read Chapter 18's Plugin and Service Stub in your own copy first, to the end of "
            "each When to Use It. The lesson sets out both and then lists what a change to a "
            "network library reaches in two designs of one signup."
        ),
        "body": [
            # PDF p. 446 of the operator's copy; David Rice's words.
            ("p", "&ldquo;Use Service Stub whenever you find that dependence on a particular "
                  "service is hindering your development and testing.&rdquo; The words are "
                  "David Rice's, in his Service Stub, one of Chapter 18's Base Patterns. "
                  "This lesson reads it with Plugin, which Rice wrote with Matt Foemmel, "
                  "because each needs the other: a stub is no use unless something chooses "
                  "it for the tests and the real service for production."),
            ("p", "Plugin starts from Separated Interface, where code running in several "
                  "environments needs a different implementation in each: an in-memory "
                  "counter for unit tests and a database sequence in production, say. The "
                  "usual answer is a factory method with a conditional on the environment, "
                  "and once there are a few such factories, Rice and Foemmel say, you have a "
                  "mess: a new deployment configuration means editing conditionals in "
                  "several factories, rebuilding and redeploying. The configuration belongs in "
                  "one place, and changing it should not mean building again."),
            ("p", "So the Plugin factory states its linking instructions at a single, "
                  "external point, such as a text file mapping each interface to an "
                  "implementation, and links them at run time. It works best with reflection, "
                  "because the factory can then build an implementation without depending on "
                  "it at compile time. Without reflection a central point of configuration is "
                  "still worth having, with a conditional in the factory for each "
                  "implementation, and the authors suggest putting that factory in its own "
                  "package so that layer dependencies can still be checked. Use it whenever "
                  "behaviour needs different implementations in different runtime "
                  "environments."),
            ("p", "Service Stub starts from the services an enterprise system leans on and "
                  "does not control, such as credit scoring and pricing engines. Their "
                  "features arrive unpredictably, and being remote they can be slow and "
                  "unreliable. Developers wait, or hack around them, and worse, tests cannot "
                  "run, which Rice says breaks the development process. A stand-in that runs "
                  "locally, fast and in memory fixes that."),
            ("p", "The steps are the two earlier patterns. Define access to the service with "
                  "a Gateway, and make the Gateway a Separated Interface, not a class, so "
                  "that one implementation calls the real service and another is the stub. "
                  "Load the right one with a Plugin. Then keep the stub as simple as possible, "
                  "a few lines, since a complicated stub defeats the point; a stub that tests can "
                  "configure may need a setup method on the interface, which Rice accepts for "
                  "the sake of the tests. He notes that many practitioners of Extreme "
                  "Programming call this a Mock Object, and that he kept Service Stub because "
                  "the name is older."),
            ("code", _lines(ADDRESS_STUB)),
            ("p", "The snippet has all three parts. Lines 2 to 4 are the Separated "
                  "Interface the signup depends on: is this postcode deliverable? Lines 5 to "
                  "9 are the stub, which says yes to every postcode except those beginning "
                  "`ZZ`, so a test can ask for either answer. Lines 12 to 20 are the plugin "
                  "in its simplest form, one `switch` on the environment's name, read once "
                  "at startup: the stub for `test`, the real post office check for `live`. "
                  "It is the one place that knows both implementations."),
            ("p", "Now the count. The lab reads records `dependent, dependency` and the name "
                  "of the class that changes, and walks the dependencies backwards from it. "
                  "Its tiles list what depends on the changed class directly and everything "
                  "the change reaches, the changed class itself left out. In the preset "
                  "<code>real-service</code> the signup calls `postoffice`, which uses the "
                  "`network` library, and the signup's test calls the signup. Change "
                  "`network` and it reaches 1 directly, `postoffice`, and 3 in all, "
                  "`postoffice, signup, signuptest`: the test depends on the network."),
            ("p", "The preset <code>plugin-and-stub</code> is the snippet's design. The "
                  "signup depends on `addresscheck`; `postofficecheck` and "
                  "`addresscheckstub` implement it; the test uses the signup and the stub; "
                  "and `main`, the startup code that calls the plugin and hands the result to "
                  "the signup, depends on `postofficecheck`. Change `network` and it reaches "
                  "1 directly, `postofficecheck`, and 2 in all, `main, postofficecheck`. "
                  "Neither the signup nor its test is reached."),
            ("p", "That depends on who calls the switch. If the signup called "
                  "`AddressChecks.forEnvironment` itself, it would depend on the plugin, "
                  "which names `PostOfficeCheck`; add `signup, main` to the records and a "
                  "change to `network` reaches 4 again, `main, postofficecheck, signup, "
                  "signuptest`. That is the compile-time dependency Rice and Foemmel's "
                  "reflection removes, and one reason to read the configuration at one point "
                  "at the edge of the system, as the lesson's `main` does, not inside the "
                  "code that uses the interface."),
            ("h3", "Exercise"),
            ("ul", [
                "An invoice priced from an exchange-rate feed: `invoice, ratesfeed; "
                "ratesfeed, http; invoicetest, invoice`, with `http` changed.",
                "The same invoice redesigned: an interface `rates`, implemented by "
                "`httprates`, which uses `http`, and by `ratesstub`; the invoice and its test "
                "as in the snippet's design; `main` wiring `httprates`.",
            ]),
            ("p", "For each design, list by hand what depends on `http` directly and "
                  "everything a change to it reaches, and say in one sentence whether the "
                  "invoice's test still depends on the network. Write the second design's "
                  "records first."),
            ("p", "That ends the Subject where it began. Plugin and Service Stub both rest "
                  "on the Separated Interface of the first course's Layer Supertype and "
                  "Separated Interface, and the First Law of this course's first lesson is "
                  "one more case of what the first course said about layers: decide where "
                  "the boundaries are, and keep them few."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "real-service",
            "changed": "network",
            "presets": [
                {"id": "real-service",
                 "label": "The signup calls the post office directly (illustrative)",
                 "edges": "signup, postoffice; postoffice, network; signuptest, signup",
                 "expect": {"dgDirect": "1: postoffice",
                            "dgAffected": "3: postoffice, signup, signuptest"}},
                {"id": "plugin-and-stub",
                 "label": "An AddressCheck interface, a stub, and main choosing the real one",
                 "edges": "signup, addresscheck; postofficecheck, addresscheck; "
                          "postofficecheck, network; addresscheckstub, addresscheck; "
                          "signuptest, signup; signuptest, addresscheckstub; "
                          "main, postofficecheck",
                 "expect": {"dgDirect": "1: postofficecheck",
                            "dgAffected": "2: main, postofficecheck"}},
            ],
            "panel_title": "What a change to the network reaches",
            "panel_intro": (
                "Each record is one dependency, written dependent, dependency. Name the "
                "class that changes; the lab lists what depends on it directly and "
                "everything the change reaches. The designs are the lesson's, and the tests "
                "are listed as classes like any other."
            ),
        }),
        "steps_title": "Keeping a test off the network",
        "steps_intro": "Four steps, the last of them on a test of your own.",
        "steps": [
            ("List the dependencies, tests included",
             "Write each class and what it uses, as dependent, dependency, and include each "
             "test as a class that uses what it tests."),
            ("Walk back from the change",
             "From the network library, list what uses it directly, then what uses those, "
             "until nothing new is reached. Check whether a test is on the list."),
            ("Redesign with an interface, a stub and a plugin",
             "Put a Separated Interface in front of the service, give it a real "
             "implementation and a stub, let the test use the stub, let one startup class "
             "choose the real one, and walk back again."),
            ("Do it on a test you know",
             "Take one test in a system you know that calls a real external service. Write "
             "the interface that would let it use a stub, in a few lines, and list what a "
             "change to the service's client library would then reach."),
        ],
        "worked": {
            "title": "The signup with a stub",
            "intro": [
                "Take the preset <code>plugin-and-stub</code> and walk back from `network`.",
            ],
            "lines": [
                "uses network: postofficecheck",
                "uses postofficecheck: main",
                "uses main: nothing",
                "reached: main, postofficecheck",
                "signuptest uses signup and the stub",
                "neither of those reaches network",
            ],
            "after": [
                "The test depends on `signup` and `addresscheckstub`, and both depend only on "
                "the interface. A change to the network reaches the startup code that chose "
                "the real check, and nothing the tests run.",
            ],
        },
        "quiz_title": "Stubs, plugins and what a change reaches",
        "quiz": [
            {"q": "Work the exercise. With `invoice, ratesfeed; ratesfeed, http; "
                  "invoicetest, invoice`, a change to `http` reaches what? And in the "
                  "redesign with `rates`, `httprates`, `ratesstub` and `main` wiring "
                  "`httprates`?",
             "a": ["3: invoice, invoicetest, ratesfeed; then 2: httprates, main",
                   "3: invoice, invoicetest, ratesfeed; then 3: httprates, invoicetest, main",
                   "2: invoice, ratesfeed; then 1: httprates",
                   "1: ratesfeed; then 1: httprates"],
             "c": 0,
             "why": "Before, `http` is used directly by `ratesfeed` only, and the change "
                    "reaches 3: `invoice, invoicetest, ratesfeed`, so the test depends on the "
                    "network. After, the records are `invoice, rates; httprates, rates; "
                    "httprates, http; ratesstub, rates; invoicetest, invoice; invoicetest, "
                    "ratesstub; main, httprates`: `http` is used directly by `httprates` and "
                    "reaches \"2: httprates, main\", and the test is no longer reached. The "
                    "last option gives only the direct dependents."},
            {"q": "What does a Service Stub let a test check?",
             "a": ["That the real service returns correct answers",
                   "The code that uses the service, without the service",
                   "That the network is available",
                   "The service's performance under load"],
             "c": 1,
             "why": "A stub stands in for the service, so a test that uses it checks the "
                    "caller's behaviour for the answers the stub gives. Whether the real "
                    "service answers correctly, or at all, needs tests of its own against "
                    "the service."},
            {"q": "How does Service Stub say the stub, rather than the real service, is put "
                  "in place for the tests?",
             "a": ["By subclassing the real service class and overriding its methods",
                   "By a conditional on the environment in each class that calls the "
                   "service",
                   "Through a Plugin, behind a Gateway defined as a Separated Interface",
                   "By pointing the real service's client at a test address"],
             "c": 2,
             "why": "Rice's How It Works: define access with a Gateway that is a Separated "
                    "Interface, with the real implementation and the stub behind it, and load "
                    "the right one with a Plugin. A conditional in each calling class is the "
                    "scattered configuration Plugin was written to remove."},
            {"q": "In the preset plugin-and-stub, the signup calls the plugin itself, so the "
                  "record `signup, main` is added. What does a change to `network` reach now?",
             "a": ["2: main, postofficecheck",
                   "3: main, postofficecheck, signup",
                   "4: main, postofficecheck, signup, signuptest",
                   "5: addresscheck, main, postofficecheck, signup, signuptest"],
             "c": 2,
             "why": "`network` reaches `postofficecheck`, then `main`, which the signup now "
                    "uses, then the signup, then its test: 4. Stopping at the signup forgets "
                    "that the test uses it. `addresscheck` is not reached: it is used by the "
                    "others and uses nothing that changed."},
        ],
        "mistakes": [
            ("Thinking a stub tests the service",
             "A test that passes against the stub says nothing about the post office: the "
             "stub answers yes to every postcode not beginning `ZZ`, whatever the real "
             "service would say. What it tests is the code that uses the service, without "
             "it, which is what Rice wrote it for. The service, and the class that calls it, "
             "need tests of their own."),
            ("Thinking a plugin needs a framework",
             "The book's example reads a properties file and builds classes by reflection, "
             "and it is easy to conclude that Plugin means a configuration framework. Rice "
             "and Foemmel ask for less: one place, stated outside the code that uses the "
             "interface and read at configuration time, that chooses the implementation for "
             "the environment. Without reflection that can be a conditional, and the "
             "snippet does it with one `switch`."),
            ("Making the stub faithful to the service",
             "A stub that reproduces the service's rules seems more useful the more it "
             "copies. Rice says the opposite: keep it as simple as possible, because "
             "a complicated stub defeats the point of having one. A few lines that give the answers the tests "
             "need, such as one postcode prefix that is refused, are the pattern; a second "
             "implementation of the service is another thing to test and keep in step."),
        ],
        "standard": (
            "Finish when you can list what a change to a service reaches, with and without "
            "a stub.",
            "Given dependencies including tests, list what a change to the network library "
            "reaches with a direct dependency and with a Separated Interface, a Service Stub "
            "and a Plugin, and say whether the tests are reached."
        ),
        "note": (
            "The lab walks the dependencies you type; it cannot find them in code, and it "
            "cannot tell whether the stub's answers resemble the service's. It also counts a "
            "test reached or not, when what matters to Rice is whether the test can run "
            "without the service: a design where the test is not reached can still fail "
            "because the stub's setup is wrong, and only running the tests shows that."
        ),
    },
]
