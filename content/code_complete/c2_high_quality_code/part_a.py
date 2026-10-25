"""Creating High-Quality Code, lessons 1-4 -- Chapters 5 and 6.

McConnell, Code Complete, 2nd ed. (Microsoft Press, 2004): Chapter 5, Design
in Construction (pp. 73-123), and Chapter 6, Working Classes (pp. 125-160).
Every quotation is copied from the operator's copy with its printed page in
the comment beside the lesson; every figure attributed to the book carries
its PLAN section S.2 id. The code is written for these lessons: none of the
book's listings is reproduced. Each snippet is one constant below, used both
by the lesson's code block and by the lab preset that counts it, so the line
numbers the prose names are the lab's.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# Abstract Data Types and Interfaces: presets public-fields, private-fields,
# kitchen-sink (PLAN section D.4 and presets.py, verbatim).
PUBLIC_FIELDS = """public class Employee {
    public String name;
    public String address;
    public String phone;
    public int salaryCents;
    public int vacationDays;

    public Employee(String name) {
        this.name = name;
    }

    public int monthlyPayCents() {
        return salaryCents / 12;
    }
}"""

PRIVATE_FIELDS = """public class Employee {
    private String name;
    private Address address;
    private PhoneNumber phone;
    private Money salary;
    private int vacationDays;
    public Employee(String name, Money salary) {
        this.name = name;
        this.salary = salary;
    }
    public String name() {
        return name;
    }
    public Money monthlyPay() {
        return salary.dividedBy(12);
    }
    private boolean isEligibleForBonus() {
        return vacationDays < 5;
    }
}"""

KITCHEN_SINK = """public abstract class Kiosk {
    public String location;
    public Printer printer;
    private int ticketsIssued;
    private int refundsToday;
    private Forecast forecast;
    private String forecastCity;
    private Writer auditLog;
    private int auditLines;
    private boolean maintenanceMode;

    public abstract Ticket issueTicket(Fare fare);
    public abstract void refundTicket(Ticket ticket);
    public abstract Forecast fetchForecast(String city);
    public abstract void showForecast();
    public abstract void openAuditLog();
    public abstract void closeAuditLog();
}"""

# Exercise snippets (not presets: the exercise is the reader's).
POINT_EXERCISE = """public class Point {
    public double x;
    public double y;
    private String label;

    public double distanceTo(Point other) {
        double dx = x - other.x;
        double dy = y - other.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
}"""

DATE_EXERCISE = """// in Billing
LocalDate dueDate(Invoice inv) {
    String s = inv.dueText();
    return LocalDate.of(Integer.parseInt(s.substring(0, 4)),
            Integer.parseInt(s.substring(4, 6)),
            Integer.parseInt(s.substring(6, 8)));
}
// in Shipping
LocalDate shipDate(Parcel p) {
    String s = p.shippedText();
    return LocalDate.of(Integer.parseInt(s.substring(0, 4)),
            Integer.parseInt(s.substring(4, 6)),
            Integer.parseInt(s.substring(6, 8)));
}
// in Members
LocalDate joinDate(Member m) {
    String s = m.joinedText();
    return LocalDate.of(Integer.parseInt(s.substring(0, 4)),
            Integer.parseInt(s.substring(4, 6)),
            Integer.parseInt(s.substring(6, 8)));
}"""

SQUARE_EXERCISE = """class Rectangle {
    private int width;
    private int height;
    void setWidth(int w) { width = w; }
    void setHeight(int h) { height = h; }
    int area() { return width * height; }
}

class Square extends Rectangle {
    void setWidth(int w) {
        super.setWidth(w);
        super.setHeight(w);
    }
    void setHeight(int h) {
        super.setWidth(h);
        super.setHeight(h);
    }
}"""

_FIVE = ("ui", "orders", "billing", "stock", "db")
_EVERYTHING_TALKS = "; ".join("%s, %s" % (a, b) for a in _FIVE for b in _FIVE if a != b)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapter 5, sections 5.1-5.2, pp. 73-86.
    # Quote: p. 123 (Key Points), 17 words, cc_quotes.py OK. Brooks's essay is
    # named by its own title, No Silver Bullet, not quoted. Lesson total: 17 words.
    # Wicked problems after Rittel and Webber 1973 (p. 74); Tacoma Narrows
    # (pp. 74-75); accidental and essential difficulties after Brooks 1987
    # (pp. 77-78); the primary technical imperative (p. 78); Dijkstra 1972
    # and 1989 (pp. 78-79); two prongs (p. 79); desirable characteristics
    # (pp. 80-81); levels of design and the hoses (pp. 82-85).
    {
        "slug": "design-challenges-and-complexity",
        "title": "Design Challenges and Complexity",
        "module": "Chapter 5 · Design in Construction",
        "one_line": "Design is a wicked, sloppy, heuristic activity whose first job is to keep how much of a program anyone must hold in mind at once small.",
        "summary": (
            "Chapter 5 opens by saying why design is hard and what it is for: design is a "
            "wicked problem, sloppy and heuristic, and its primary technical imperative is "
            "managing complexity. Count the modules of a small design, the pairs that could "
            "interact and the pairs that do, and the largest fan-in, and see what one layering "
            "decision changes."
        ),
        "key": [
            "design is sloppy, heuristic, emergent",
            "first imperative: manage complexity",
            "pairs of n modules: n * (n - 1) / 2",
            "connected pairs: used either way, once",
            "fan in: how many modules use this one",
            "fan out: how many this one uses",
        ],
        "key_label": "Sections 5.1 and 5.2 in six lines",
        "concepts_intro": (
            "Three ideas carry the first half of the chapter. Each has a name the rest of the "
            "book takes for granted."
        ),
        "concepts": [
            ("A wicked problem",
             "A problem that can be clearly defined only by solving it, or part of it. The "
             "book takes the term from Rittel and Webber (1973) and applies it to design: you "
             "often learn what the problem was by building something that fails to solve it."),
            ("Essential and accidental difficulty",
             "Brooks's distinction (1987), which the chapter follows. Accidental difficulties "
             "come from the tools, such as clumsy syntax or batch computers, and have largely "
             "been removed. Essential difficulties come from the problem itself, an intricate "
             "set of interlocking details that must be exactly right."),
            ("Coupling, fan-in and fan-out",
             "Coupling is how tightly two parts of a program are connected. A module's fan-in "
             "is the number of modules that use it; its fan-out is the number it uses. The "
             "chapter asks for loose coupling, high fan-in at the utility level and low to "
             "medium fan-out."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 5.1 and 5.2, pages 73 to 86, in your own copy first. The lesson "
            "sets out the argument in its own words, section by section, and then counts the "
            "connections in three versions of one small design."
        ),
        "body": [
            ("p", "&ldquo;Software’s Primary Technical Imperative is managing complexity. "
                  "This is greatly aided by a design focus on simplicity.&rdquo; That is the "
                  "first of Chapter 5's key points (p. 123), and the whole of Creating "
                  "High-Quality Code is built on it. This lesson reads sections 5.1 and 5.2, "
                  "pages 73 to 86: why design is hard, and what the chapter means by "
                  "complexity. Read them in your own copy first."),
            ("p", "The chapter's first question is what design is, and its answer is a list "
                  "of difficulties. Design, McConnell says, is a wicked problem, in the sense "
                  "Rittel and Webber gave the word in 1973: one you can define clearly only by "
                  "solving it, or part of it, so that you solve it once to learn what it was and "
                  "again to solve it properly. His example is the first Tacoma Narrows bridge, "
                  "strong enough for its load and shaken apart by the wind in 1940, because "
                  "nobody had known that aerodynamics mattered that much until the bridge "
                  "showed them. School exercises, he notes, are rarely wicked; professional "
                  "work usually is."),
            ("p", "The rest of section 5.1 follows from that. Design is sloppy, full of false "
                  "steps, even when its result is tidy, and it is hard to know when it is good "
                  "enough. It is about trade-offs and priorities, and about restrictions, which "
                  "force simplifications that improve the result. It is nondeterministic: three "
                  "people sent away to design one program can come back with three acceptable "
                  "designs. So its techniques are heuristics, rules of thumb that sometimes work, "
                  "and design is emergent: it evolves through reviews, discussion and the "
                  "experience of writing and revising the code."),
            ("p", "Section 5.2 asks what all this difficulty is made of, and answers with "
                  "Fred Brooks's essay <em>No Silver Bullet</em> (1987). Brooks "
                  "divided software's difficulties, after Aristotle, into the accidental and "
                  "the essential. Assembly language, batch computers and tools that did not "
                  "work together were accidental, and were largely dealt with decades ago. "
                  "What remains is essential: working out an intricate, interlocking set of "
                  "concepts that must be exactly right and that meet a disorderly world. The "
                  "root of both kinds, McConnell concludes, is complexity, and when projects "
                  "fail for technical reasons the reason is often that nobody any longer "
                  "understands what a change in one place will do elsewhere."),
            ("p", "Hence the imperative. Citing Dijkstra, the chapter says no one's skull is "
                  "big enough to hold a modern program, so a design should let you focus "
                  "safely on one part at a time. It proposes two prongs: keep the essential "
                  "complexity anyone must deal with at one time to a minimum, and keep "
                  "accidental complexity from spreading. Its list of a design's desirable "
                  "internal characteristics follows, and three of them are counts: loose "
                  "coupling, high fan-in (many classes using a given utility class) and low "
                  "to medium fan-out (a class using only a few others). Stratification, "
                  "leanness and ease of maintenance are on the same list."),
            ("p", "The section ends with the levels of design, from the whole system through "
                  "subsystems and classes down to the inside of a routine. At the subsystem "
                  "level McConnell imagines six subsystems in which every one talks to every "
                  "other, and offers his own image for what that costs: think of each line "
                  "between subsystems as a hose with water in it, and of how wet you get "
                  "pulling one subsystem out to use elsewhere. His advice is to allow "
                  "communication on a need-to-know basis, restricting it early, and to keep "
                  "the subsystem diagram free of cycles."),
            ("p", "Now the count. The lab reads a design as records `user, used`, one per "
                  "dependency, and counts. Its tiles are the number of modules, the distinct "
                  "uses, the possible pairs of modules, the pairs connected in either "
                  "direction as a share of the possible ones, and the largest fan-out and "
                  "fan-in, with a tie going to the alphabetically first name and the banner "
                  "naming every tied module. The preset <code>everything-talks</code> has five "
                  "modules, `ui`, `orders`, `billing`, `stock` and `db`, each using every "
                  "other: 20 uses, 10 possible pairs, and all 10 connected, 1 = 100%. The "
                  "largest fan-in prints as billing 4, but all five modules tie at 4; this is "
                  "the hoses picture in miniature."),
            ("p", "The preset <code>layered</code> redraws the same five modules in layers: "
                  "`ui` uses `orders` and `billing`, each of those uses `stock` and `db`, and "
                  "`stock` uses `db`. That is 7 uses touching 7 of the 10 pairs, 7/10 = 70%. "
                  "The largest fan-in is db 3, and the largest fan-out billing 2, tied with "
                  "`ui` and `orders`. In <code>strict-layers</code> each module talks only to "
                  "modules below it, and to fewer of them: `ui` to `orders` and `billing`, `orders` to `stock`, `stock` "
                  "and `billing` to `db`. Five uses, half the pairs, 1/2 = 50%, and the "
                  "largest fan-in falls to db 2."),
            ("p", "What do the counts show? Not that one design is good. They show how many "
                  "pairs of modules a change could pass between directly, and which module "
                  "everything leans on. In <code>layered</code>, `db` has the highest fan-in, "
                  "and that is what the chapter hopes for at the bottom of a design: a "
                  "utility many modules use. A reader who opens `ui` in "
                  "<code>strict-layers</code> needs to know two modules to understand it, "
                  "where in <code>everything-talks</code> they need four. A count is a "
                  "reason to look, and here it tells you where."),
            ("h3", "Exercise"),
            ("ul", [
                "Six modules, `ui`, `api`, `orders`, `billing`, `stock` and `db`, in a "
                "design where every module uses every other.",
                "The same six, layered: `ui, api; api, orders; api, billing; orders, stock; "
                "billing, stock; stock, db`.",
            ]),
            ("p", "For each design, find by hand the possible pairs, the uses, the pairs "
                  "connected as a share of the possible ones, and the module with the largest "
                  "fan-in. Then say in one sentence what the layering changed. You can check "
                  "your counts afterwards by typing the records into the lab."),
            ("p", "Design, the chapter says, is heuristic. The next lesson, Design Heuristics "
                  "and Information Hiding, reads the heuristics it offers, and the one it "
                  "calls particularly valuable."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "coupling",
            "preset": "everything-talks",
            "presets": [
                {"id": "everything-talks",
                 "label": "Everything talks: five modules, each using every other (illustrative)",
                 "edges": _EVERYTHING_TALKS,
                 "expect": {"dgEdges": "20", "dgConnected": "1 = 100%", "dgFanIn": "billing 4"}},
                {"id": "layered",
                 "label": "Layered: ui over orders and billing, over stock and db",
                 "edges": "ui, orders; ui, billing; orders, stock; billing, stock; "
                          "orders, db; billing, db; stock, db",
                 "expect": {"dgEdges": "7", "dgConnected": "7/10 = 70%", "dgFanIn": "db 3"}},
                {"id": "strict-layers",
                 "label": "Strict layers: each module uses fewer modules, all below it",
                 "edges": "ui, orders; orders, stock; stock, db; ui, billing; billing, db",
                 "expect": {"dgEdges": "5", "dgConnected": "1/2 = 50%", "dgFanIn": "db 2"}},
            ],
            "panel_title": "Count the connections in a design",
            "panel_intro": (
                "Each record is one dependency, written user, used. The lab counts the "
                "modules, the distinct uses, the possible pairs, the pairs connected in "
                "either direction and the largest fan-out and fan-in. The designs are "
                "illustrative, and the counts are a reason to look, not a verdict."
            ),
        }),
        "steps_title": "Counting a design's connections",
        "steps_intro": "Five steps, the last of them on a design of your own.",
        "steps": [
            ("List the modules",
             "Write down every module the dependencies name, once each. Their number is n."),
            ("Count the possible pairs",
             "Each module can be paired with each of the n − 1 others, and each pair is "
             "counted twice that way, so there are n·(n − 1)/2 possible pairs."),
            ("Count the connected pairs",
             "Mark each pair that has a dependency in either direction, counting a pair "
             "once even when each module uses the other. Divide by the possible pairs for "
             "the share."),
            ("Find the largest fan-in and fan-out",
             "For each module, count the modules that use it (fan-in) and the modules it "
             "uses (fan-out), and note the largest of each and every module tied for it."),
            ("Do it on your own code",
             "Take one package of your own, list who imports whom as `a, b` records, and "
             "paste them into the lab. Note the share of pairs connected and the module with "
             "the largest fan-in, and write one sentence on a dependency you would remove."),
        ],
        "worked": {
            "title": "Five modules, three ways",
            "intro": [
                "Take the five modules of the lab's presets and count the pairs, then the "
                "connections in the layered design.",
            ],
            "lines": [
                "possible pairs: 5 * 4 / 2, which is 10",
                "everything talks: 20 uses, all 10 pairs",
                "layered: 7 uses, each joins its own pair",
                "layered: 7 of 10 pairs connected, 70 per cent",
                "db is used by orders, billing and stock: 3",
                "strict layers: 5 uses, 5 of 10 pairs",
            ],
            "after": [
                "Layering removed thirteen of the twenty uses and three of the ten pairs, "
                "and made `db` the module most others lean on. Whether the remaining "
                "dependencies are the right ones is a design question the count does not "
                "answer; it tells you which ones to ask it about.",
            ],
        },
        "quiz_title": "Connections and the chapter's claims",
        "quiz": [
            {"q": "Count the exercise's layered design: six modules and the six dependencies "
                  "`ui, api; api, orders; api, billing; orders, stock; billing, stock; "
                  "stock, db`. How many pairs are connected, and which module has the "
                  "largest fan-in?",
             "a": ["6 of 15 pairs, 40%; stock, with fan-in 2",
                   "6 of 30 pairs, 20%; stock, with fan-in 2",
                   "6 of 15 pairs, 40%; api, with fan-in 2",
                   "5 of 15 pairs, 33.3%; stock, with fan-in 2"],
             "c": 0,
             "why": "Six modules give 6 × 5 / 2 = 15 possible pairs. When every module uses "
                    "every other there are 30 uses and all 15 pairs are connected. Layered, the "
                    "6 uses join 6 different pairs, 6/15 = 2/5 = 40%, and `stock` is used by "
                    "`orders` and `billing`, a fan-in of 2. Thirty is the number of uses when "
                    "all talk, not the number of pairs. `api` uses two modules: that is its "
                    "fan-out; only `ui` uses it. Six records join six pairs: count the records before "
                    "the pairs."},
            {"q": "In a design, `a` uses `b` and `c`, `d` uses `c`, and `e` uses `c`. Which "
                  "module has the largest fan-in, and what is it?",
             "a": ["`a`, 2", "`c`, 4", "`c`, 3", "`e`, 1"],
             "c": 2,
             "why": "Fan-in counts the modules that use a module: `a`, `d` and `e` use `c`, "
                    "so it is 3. `a` has the largest fan-out, 2. Four would count `c` itself "
                    "or a use twice."},
            {"q": "Which of these does section 5.1 claim about design?",
             "a": ["A design is complete before coding begins once the requirements are stable",
                   "There is usually one correct design for a given specification",
                   "Design is emergent: it evolves through reviews, discussion and writing "
                   "and revising the code",
                   "A good design process is as tidy as the design it produces"],
             "c": 2,
             "why": "Section 5.1 calls design emergent, sloppy and nondeterministic: three "
                    "designers can return three acceptable designs, the process is untidy "
                    "even when the result is tidy, and design goes on while the code is "
                    "written and revised."},
            {"q": "Module `p` uses `q`, and `q` uses `p`. How many uses does the lab count, "
                  "and how many connected pairs?",
             "a": ["1 use, 1 pair", "2 uses, 2 pairs", "2 uses, 1 pair", "1 use, 2 pairs"],
             "c": 2,
             "why": "Each record is a use, so there are 2. A pair is connected if there is a "
                    "use in either direction, and it is counted once: `p` and `q` make 1 pair."},
        ],
        "mistakes": [
            ("Thinking design is a phase that ends when coding begins",
             "On this view the design is finished, then built. Section 5.1 says otherwise: "
             "design is a wicked problem, understood only by partly solving it, and it is "
             "sloppy, heuristic and emergent, evolving through reviews, discussion and the "
             "experience of writing and revising the code. Much of it is done during "
             "construction, at the level of classes and routines. The lab's three presets "
             "illustrate the point on the lesson's own example: one set of five modules, its "
             "layering redrawn three times, each a design decision."),
            ("Taking fewer connections for a better design",
             "The share of connected pairs falls from 100% to 50% across the presets, and "
             "it is tempting to read the lowest as the best. The chapter does not ask for "
             "the fewest connections; it asks for loose coupling and for high fan-in at the "
             "bottom of a design, where many modules use one utility. In "
             "<code>layered</code>, `db` with fan-in 3 is that utility. The count shows "
             "where the connections are; whether each is needed is a design question."),
            ("Expecting good design to remove complexity",
             "Brooks's distinction says some difficulty belongs to the problem: the "
             "details that must be exactly right, and the world they meet. Design cannot "
             "remove that. What the chapter asks of it is narrower: keep the essential "
             "complexity anyone must face at one time to a minimum, and stop accidental "
             "complexity from spreading."),
        ],
        "standard": (
            "Finish when you can count a design's connections by hand.",
            "For five or six modules and their dependencies, compute the possible pairs, the "
            "pairs connected as a share, and the largest fan-in, and say what a layering "
            "changes in those figures."
        ),
        "note": (
            "The lab counts the dependencies you state; it cannot find them in code, and it "
            "counts a pair joined by one call the same as a pair joined by forty. It does not "
            "say whether a design is good. Chapter 5 says complexity is the thing to manage, "
            "and these counts are one view of it: how many places a change could reach "
            "directly, and which module carries the most weight."
        ),
    },
    # ---------------------------------------------------------------- 02
    # McConnell Chapter 5, sections 5.3-5.5, pp. 87-123.
    # Quote: p. 123 (Key Points), 17 words, cc_quotes.py OK; the inner marks
    # are the book's, printed as lsquo/rsquo.
    # Brooks's line, as the book quotes it (Brooks 1995): p. 92, 10 words,
    # cc_quotes.py OK. Lesson total: 27 words.
    # Parnas 1972 and Boehm 1987 (p. 92); secrets and the right to privacy
    # (pp. 92-93); the ID example (pp. 93-94); two categories of secrets
    # (p. 94); barriers (pp. 95-96); likely change (pp. 97-99); section 5.4
    # (pp. 110-118); section 5.5 (pp. 118-119), with enough design and the
    # two positions always wrong on p. 119.
    {
        "slug": "design-heuristics-and-information-hiding",
        "title": "Design Heuristics and Information Hiding",
        "module": "Chapter 5 · Design in Construction",
        "one_line": "Of the chapter's design heuristics, information hiding is the one it singles out: decide what each module keeps secret, and let only that module know it.",
        "summary": (
            "Sections 5.3 to 5.5 give the heuristics design works by, the practices that "
            "apply them and a word on methodologies. Name the secret one detail of a design "
            "should be, count the modules whose code knows it with the detail exposed and "
            "hidden, and tell the modules that must be edited from the modules a change "
            "reaches."
        ),
        "key": [
            "ask what each module should hide",
            "a secret: a decision likely to change",
            "secrets hide complexity or change",
            "direct: modules that know the secret",
            "reached: everything that depends on it",
        ],
        "key_label": "Sections 5.3 to 5.5 in five lines",
        "concepts_intro": (
            "Three terms run through section 5.3. The chapter treats each as a heuristic, a "
            "question worth asking, rather than a rule."
        ),
        "concepts": [
            ("Abstraction",
             "The ability to engage with a concept while safely ignoring its details. A "
             "class interface is an abstraction of the implementation behind it."),
            ("Encapsulation",
             "The enforcer behind abstraction: not only may you ignore the details, you are "
             "prevented from looking at them. The chapter calls it the stronger of the two."),
            ("Information hiding",
             "Each module is characterised by the design decisions it hides from all the "
             "others, its secrets. A secret might be an area likely to change, a file format "
             "or how a data type is implemented."),
        ],
        "read_title": "The heuristics first, then one secret counted",
        "read_intro": (
            "Read sections 5.3 to 5.5, pages 87 to 123, in your own copy first; the "
            "heuristics take most of it. The lesson sets out the argument, then counts who "
            "knows one file format in two versions of a design."
        ),
        "body": [
            ("p", "&ldquo;Information hiding is a particularly valuable concept. Asking "
                  "&lsquo;What should I hide?&rsquo; settles many difficult design "
                  "issues.&rdquo; That is one of Chapter 5's key points (p. 123), and this "
                  "lesson reads the sections behind it: 5.3 on the heuristics, 5.4 on design "
                  "practices and 5.5 on methodologies, pages 87 to 123. Read them in your own "
                  "copy first."),
            ("p", "If design is heuristic, as the first lesson read, the next question is "
                  "which heuristics. Section 5.3 gives a list: find real-world objects; form consistent abstractions; "
                  "encapsulate implementation details; inherit when that simplifies the "
                  "design; hide secrets; identify areas likely to change; keep coupling "
                  "loose; look for common design patterns. A shorter list follows, from "
                  "strong cohesion and hierarchies to binding time, central points of "
                  "control, brute force and drawing a diagram."),
            ("p", "One heuristic gets several pages, and its history is a story with people "
                  "in it. David Parnas introduced information hiding in a 1972 paper on the "
                  "criteria for dividing a system into modules. Fred Brooks, in the first "
                  "edition of <em>The Mythical Man-Month</em>, argued against it; in the "
                  "twentieth-anniversary edition he took it back, and the book quotes him: "
                  "&ldquo;Parnas was right, and I was wrong about information hiding&rdquo; "
                  "(Brooks 1995). The book adds that Barry Boehm found it powerful for "
                  "eliminating rework, especially where requirements change."),
            ("p", "The idea is that each class, package or routine is characterised by the "
                  "design decisions it hides from all the others. McConnell's example is an "
                  "object id made by incrementing a global counter wherever an object is "
                  "created. That spreads one decision, how ids are made, through every "
                  "creation site; a single routine that hands out the next id keeps it in one "
                  "place, and so can change it in one place. Secrets, the chapter says, fall "
                  "into two kinds: hiding complexity, so you need not think about it, and "
                  "hiding sources of change, so that a change stays local."),
            ("p", "The section also lists what gets in the way: information spread through "
                  "the system, such as one literal repeated everywhere; circular "
                  "dependencies; avoiding class data from a fear of global data; and the "
                  "worry that indirection costs speed, which it calls premature. Then come "
                  "areas likely to change, with three steps: identify the items likely to "
                  "change, separate each into its own class, and isolate it behind an "
                  "interface that does not change with it. Business rules, hardware "
                  "dependencies, input and output, status variables and data-size "
                  "constraints are on its list of the usual suspects."),
            ("p", "Section 5.4 turns from heuristics to practice: iterate; divide and "
                  "conquer; work top down and bottom up, which it says are complementary "
                  "rather than rival; build experimental prototypes; design with others, "
                  "formally or informally; and capture the design cheaply, in comments, "
                  "on a wiki, in photographs of a whiteboard. Section 5.5, on "
                  "methodologies, comes back to how much design is enough: a judgement "
                  "call, it says, but two amounts are wrong every time, designing every "
                  "last detail and designing nothing at all, and dogmatic adherence to any "
                  "one method hurts."),
            ("p", "Now the count. The lab reads a design as records `dependent, dependency` "
                  "and a module that changes, and prints two tiles: the modules that depend "
                  "on it directly, and every module the change reaches by following the "
                  "dependencies back, with each one's distance in the table. In "
                  "<code>exposed</code>, five modules, `invoice`, `report`, `export`, "
                  "`audit` and `backup`, each read a CSV file format themselves, and `ui` "
                  "uses `report`. Change the format, `csvformat`, and the lab prints 5: "
                  "audit, backup, export, invoice, report directly, and 6 reached, `ui` "
                  "included."),
            ("p", "In <code>hidden</code> the format is a secret of one module, `store`, and "
                  "the five use `store`. Now the change reaches 1 module directly, store, "
                  "and 7 in all: audit, backup, export, invoice, report, store and ui. The "
                  "total went up by one, because `store` is new. What fell is the number of "
                  "modules whose code knows the format, from 5 to 1, and that is the number "
                  "the chapter cares about: those are the modules you would have to edit. "
                  "The second tile counts something else, everything that depends on the "
                  "format at any distance, which is what a build tool would recompile; "
                  "Programming Tools, later in this path, uses it that way."),
            ("p", "The lab cannot see whether `store` keeps its secret. If its interface "
                  "hands back the raw line and lets each caller split it on commas, the "
                  "records say one module depends on the format while five still know it. "
                  "That is the question the chapter puts to every interface: what does this "
                  "module hide, and does its interface give the secret away?"),
            ("h3", "Exercise"),
            ("code", _lines(DATE_EXERCISE)),
            ("p", "Three routines in three classes read a date stored as text. Name the "
                  "secret all three know, say which one routine should know it and what it "
                  "would be called, and count the routines that would have to change if the "
                  "stored format became <code>yyyy-MM-dd</code>, first as written and then with the "
                  "secret hidden. You can check the count afterwards in the lab, as records "
                  "with the format as the module that changes."),
            ("p", "A class is where most secrets are kept. The next lesson, Abstract Data "
                  "Types and Interfaces, reads Chapter 6 on what a class's interface should "
                  "present."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "exposed",
            "presets": [
                {"id": "exposed",
                 "label": "Exposed: five modules read the CSV format themselves (illustrative)",
                 "edges": "invoice, csvformat; report, csvformat; export, csvformat; "
                          "audit, csvformat; backup, csvformat; ui, report",
                 "changed": "csvformat",
                 "expect": {"dgDirect": "5: audit, backup, export, invoice, report"}},
                {"id": "hidden",
                 "label": "Hidden: only store knows the format, and the five use store",
                 "edges": "store, csvformat; invoice, store; report, store; export, store; "
                          "audit, store; backup, store; ui, report",
                 "changed": "csvformat",
                 "expect": {"dgDirect": "1: store",
                            "dgAffected": "7: audit, backup, export, invoice, report, store, ui"}},
            ],
            "panel_title": "Who knows the secret, and who is reached",
            "panel_intro": (
                "Each record is one dependency, written dependent, dependency. Name the "
                "module that changes. The lab lists the modules that depend on it directly, "
                "the ones whose code knows it, and every module the change reaches by "
                "following the dependencies back. The designs are illustrative."
            ),
        }),
        "steps_title": "Finding a secret and who knows it",
        "steps_intro": "Four steps, the last of them on your own code.",
        "steps": [
            ("Name the decision",
             "Say in a few words which design decision might change: a file format, a table's "
             "columns, how an id is made. That decision is the candidate secret."),
            ("List who knows it",
             "List every module whose own code depends on the decision, the ones you would "
             "have to edit if it changed. That is the direct count."),
            ("Choose its keeper",
             "Choose the one module that should know it, give it an interface that does not "
             "mention the decision, and redraw the dependencies so that the others use the "
             "keeper."),
            ("Do it on your own code",
             "Pick one detail several modules of yours know, a file format, a table's columns "
             "or a URL scheme. Type the modules that know it as `a, b` records into the lab "
             "with the detail as the module that changes, note the direct count, and write "
             "the name of the module that should keep it."),
        ],
        "worked": {
            "title": "One file format, exposed and hidden",
            "intro": [
                "Five modules parse the CSV format themselves, and `ui` uses `report`. Then "
                "the format moves behind `store`.",
            ],
            "lines": [
                "exposed, direct: invoice, report, export, audit, backup",
                "exposed, reached: those 5 and ui, 6",
                "hidden, direct: store only, 1",
                "hidden, reached: store, the 5, and ui, 7",
                "modules to edit when the format changes: 5, then 1",
            ],
            "after": [
                "Hiding the format added a module and so a dependency, and a build would "
                "reach one more module than before. It cut the modules whose code must "
                "change from five to one, which is the effect the chapter claims for "
                "information hiding.",
            ],
        },
        "quiz_title": "Secrets, and who knows them",
        "quiz": [
            {"q": "In the exercise, three routines take dates apart with `substring`. If the "
                  "stored format becomes <code>yyyy-MM-dd</code>, how many routines change as written, "
                  "and how many once the secret is hidden?",
             "a": ["3 as written, 3 hidden", "3 as written, 1 hidden",
                   "1 as written, 1 hidden", "3 as written, 0 hidden"],
             "c": 1,
             "why": "The secret is the <code>yyyyMMdd</code> layout: which characters hold the year, the "
                    "month and the day. As written all three routines know it, so all 3 "
                    "change. Hidden in one routine, say `parseDate(String text)`, which the "
                    "three call, only that 1 changes. It is not 0: the knowledge has to live "
                    "somewhere, and the point is that it lives in one place."},
            {"q": "Records `x, fmt; a, x; b, x; c, a`, and `fmt` changes. What do the two "
                  "tiles print?",
             "a": ["1 direct, 4 reached", "1 direct, 1 reached",
                   "3 direct, 4 reached", "1 direct, 3 reached"],
             "c": 0,
             "why": "Only `x` depends on `fmt` directly. Following the dependencies back, `a` "
                    "and `b` use `x`, and `c` uses `a`, so 4 modules are reached: x, a, b and "
                    "c. Three reached leaves out `x` itself; three direct counts modules that "
                    "only reach `fmt` through `x`."},
            {"q": "According to section 5.5, which two amounts of design are wrong every "
                  "time?",
             "a": ["Designing before the requirements are final, and designing after coding "
                   "starts",
                   "Designing every last detail, and designing nothing at all",
                   "Designing without a formal notation, and designing alone",
                   "Prototyping, and designing top down"],
             "c": 1,
             "why": "How much design is enough is a judgement call, the section says, but the "
                    "two extremes are always wrong: designing every last detail before "
                    "coding, and doing no design at all. It recommends prototyping, "
                    "collaboration and both top-down and bottom-up work."},
            {"q": "Into which two kinds does section 5.3 divide the secrets a module hides?",
             "a": ["Data and routines",
                   "Hiding complexity, and hiding sources of change",
                   "Hiding from users, and hiding from other programmers",
                   "Hiding data, and hiding routines"],
             "c": 1,
             "why": "The two categories are hiding complexity, so that your mind need not deal "
                    "with it unless you are working on it, and hiding sources of change, so "
                    "that a change has local effects."},
        ],
        "mistakes": [
            ("Thinking information hiding means fewer dependencies",
             "It sounds as if hiding should shrink the graph. On the lesson's illustration "
             "it does the opposite: in <code>hidden</code> the change reaches 7 modules, one "
             "more than the 6 in <code>exposed</code>, because the keeper `store` is new. "
             "What falls is the number of modules whose code knows the format, from 5 to 1. "
             "Section 5.3 measures information hiding by what a change makes you edit, and "
             "the two tiles count two different things."),
            ("Skipping the hiding for speed",
             "The worry is that calling through an extra routine or class costs time. "
             "Section 5.3 names it as a barrier and calls it premature: until you can measure "
             "the program and find the slow spots, the best preparation for tuning is a "
             "modular design, in which a slow class can be rewritten without touching the "
             "rest."),
            ("Equating private fields with a hidden secret",
             "Declaring the fields private hides the variables. It hides the decision only "
             "if the interface does too. A `store` that returns the raw CSV line and leaves "
             "callers to split it has private fields and a public secret: every caller still "
             "knows the format. The chapter's question is what the module hides, not which "
             "keywords it uses."),
        ],
        "standard": (
            "Finish when you can name a design's secret and who should keep it.",
            "Given a dependency list, name the secret, list the modules whose code knows it, "
            "and name the one module that should, and say how many modules a change of the "
            "secret would make you edit before and after."
        ),
        "note": (
            "The lab follows the dependencies you type and cannot read code, so it cannot "
            "tell whether a keeper's interface really hides its secret: that is the question "
            "the chapter leaves to you. The two designs are the lesson's illustration. The "
            "historical claims, Parnas's paper and Brooks's change of mind, are the book's "
            "report of them."
        ),
    },
    # ---------------------------------------------------------------- 03
    # McConnell Chapter 6, sections 6.1-6.2, pp. 125-142.
    # Quote: p. 160 (Key Points), 15 words, cc_quotes.py OK.
    # ADTs and their benefits (pp. 126-129); a class as an ADT plus
    # inheritance and polymorphism (p. 133); good abstraction (pp. 133-138);
    # good encapsulation, the Point after Riel (pp. 139-142).
    # F6, pp. 143-144: consider decomposing above about seven data members
    # (Miller 1956; Riel 1996).
    {
        "slug": "abstract-data-types-and-interfaces",
        "title": "Abstract Data Types and Interfaces",
        "module": "Chapter 6 · Working Classes",
        "one_line": "A class should implement one abstract data type, and its public interface should present that one abstraction and hide everything else.",
        "summary": (
            "Sections 6.1 and 6.2 build a class from the abstract data type and ask what a "
            "good interface presents. Count a class's fields, its public data and its "
            "routines by visibility in three versions of one design, and group public "
            "routines by the abstraction each serves."
        ),
        "key": [
            "one class, one abstract data type",
            "a consistent level of abstraction",
            "no public data",
            "consider splitting past about 7 fields",
            "public fields: public and not final",
        ],
        "key_label": "Sections 6.1 and 6.2 in five lines",
        "concepts_intro": (
            "The chapter builds its account of a class out of one older idea, and two tests "
            "of an interface."
        ),
        "concepts": [
            ("Abstract data type",
             "A collection of data and the operations on it, used through those operations "
             "alone. The chapter's point is that it lets a program work with fonts, cells or "
             "passengers, not with arrays and flags."),
            ("A consistent abstraction",
             "Every public routine of a class should serve the one abstraction the class "
             "implements. A class whose interface serves several is several classes "
             "sharing a name."),
            ("Encapsulation",
             "Keeping a class's implementation out of reach, not merely out of view. The "
             "chapter's rules include no public data, no implementation details in the "
             "interface, and no assumptions about how callers use the class."),
        ],
        "read_title": "The chapter's argument first, then three classes counted",
        "read_intro": (
            "Read sections 6.1 and 6.2, pages 125 to 142, in your own copy first. The lesson "
            "sets out the argument and then counts what three versions of a class expose."
        ),
        "body": [
            ("p", "&ldquo;Class interfaces should provide a consistent abstraction. Many "
                  "problems arise from violating this single principle.&rdquo; That is one of "
                  "Chapter 6's key points (p. 160). This lesson reads sections 6.1 and 6.2, "
                  "pages 125 to 142, on the abstract data type and on good class interfaces. "
                  "Read them in your own copy first."),
            ("p", "You have probably met a class like the first one below: an `Employee` "
                  "whose fields are all public, because every caller needed one of them "
                  "once, and it was quicker to open them than to ask what the callers were "
                  "doing. Chapter 6 is about why that class becomes hard to change, and its "
                  "answer starts with an idea older than classes."),
            ("p", "An abstract data type, section 6.1 says, is a collection of data and the "
                  "operations that work on it. McConnell's running example is a font. "
                  "Without one, code all over the program sets a size field to 16, leaving "
                  "the reader to guess whether that is pixels or points, and turns bold on "
                  "with a bit mask. With one, it calls a font's own routine. The benefits he "
                  "lists follow from that: implementation details hidden, the effect of a "
                  "change limited, an interface that says what it means, code that is more "
                  "obviously correct, and a program that works with real-world entities "
                  "rather than low-level ones. One way to think of a class, he says, is "
                  "as an abstract data type plus inheritance and polymorphism."),
            ("p", "Section 6.2 asks what makes a class interface good, and its first answer "
                  "is abstraction: each class should implement one abstract data type and no "
                  "more, and its public routines should belong together. Its examples include "
                  "a class whose public routines run a command stack, format reports, print "
                  "them and initialise global data, and an employee list that inherits its "
                  "routines from a list container and so presents two abstractions at two "
                  "levels. It adds that an interface erodes under maintenance, one convenient "
                  "routine at a time, and that each new public routine should be asked "
                  "whether it fits the abstraction already there."),
            ("p", "Its second answer is encapsulation, which it calls the stronger concept: "
                  "abstraction lets you ignore the details, encapsulation stops you looking. "
                  "Minimise accessibility; expose no member data; keep implementation details "
                  "out of the interface; make no assumptions about the class's users; and be "
                  "very wary of what it calls semantic violations, callers who rely on how "
                  "the class happens to work rather than on what its interface promises. In "
                  "section 6.3 the book adds a figure, after Miller and Riel: consider "
                  "decomposing a class that has more than about seven data members."),
            ("p", "Now the count. The lab reads a class and prints four tiles: the fields, "
                  "the public fields that are not final, the routines (constructors "
                  "included), and the public routines. In <code>public-fields</code>, the "
                  "class below, all five fields are public: 5 fields, 5 public, 2 routines, 2 "
                  "public. Every caller can read and write `salaryCents`, so a change to how "
                  "pay is stored reaches every caller that touches it."),
            ("code", _lines(PUBLIC_FIELDS)),
            ("p", "In <code>private-fields</code> the same data is private, typed by what it "
                  "means rather than how it is stored, with a constructor, two public "
                  "readers and one private helper: 5 fields, 0 public, 4 routines, 3 public. "
                  "The interface says what an employee is for: its name and its monthly pay. "
                  "How the salary is kept is the class's secret."),
            ("code", _lines(PRIVATE_FIELDS)),
            ("p", "The third preset, <code>kitchen-sink</code>, is an abstract `Kiosk` with "
                  "9 fields, 2 of them public, and 6 routines, all 6 public. Nine is past the "
                  "book's about seven, a reason to look rather than a verdict, and the two "
                  "public fields break the no-public-data rule outright. But the counts "
                  "cannot answer the chapter's main question, whether those six routines "
                  "present one abstraction. Read their names and decide; the exercise asks "
                  "you to."),
            ("code", _lines(KITCHEN_SINK)),
            ("h3", "Exercise"),
            ("code", _lines(POINT_EXERCISE)),
            ("p", "First, for this `Point`, give the fields, the public fields and what a "
                  "caller would need if they were made private. Second, take "
                  "<code>kitchen-sink</code>'s six public routines and group them by the "
                  "abstraction each serves: how many classes are in there, and which "
                  "routines go in each? You can paste `Point` into the lab afterwards to "
                  "check the counts; the grouping is yours."),
            ("p", "An interface is half of a class. The next lesson, Inheritance, "
                  "Containment and Members, reads the rest of Chapter 6, on how a class is "
                  "built inside and when one class should extend another."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "class",
            "preset": "public-fields",
            "presets": [
                {"id": "public-fields",
                 "label": "An Employee with five public fields",
                 "code": PUBLIC_FIELDS,
                 "expect": {"coFields": "5", "coPublicFields": "5", "coPublicRoutines": "2"}},
                {"id": "private-fields",
                 "label": "The same data private, with two public readers",
                 "code": PRIVATE_FIELDS,
                 "expect": {"coFields": "5", "coPublicFields": "0", "coPublicRoutines": "3"}},
                {"id": "kitchen-sink",
                 "label": "A kiosk class with six public routines",
                 "code": KITCHEN_SINK,
                 "expect": {"coFields": "9", "coPublicFields": "2", "coPublicRoutines": "6"}},
            ],
            "panel_title": "Count what a class exposes",
            "panel_intro": (
                "Paste a Java class. The lab counts its fields, its public fields that are "
                "not final, its routines with constructors included, and its public "
                "routines. Whether the public routines present one abstraction is the "
                "question the counts leave to you."
            ),
        }),
        "steps_title": "Reading a class's interface",
        "steps_intro": "Five steps, the last of them on a class of your own.",
        "steps": [
            ("Count the fields",
             "List the class's fields and mark the public ones that are not final. A public "
             "constant is part of an interface; a public variable is the class's data in "
             "every caller's hands."),
            ("Count the routines by visibility",
             "List the routines, constructors included, and mark the public ones. They are "
             "the interface."),
            ("Name each public routine's abstraction",
             "Beside each public routine, write in two or three words what it is about. "
             "Routines with the same words belong together."),
            ("Group them",
             "Group the public routines by those words. More than one group means more than "
             "one abstraction in one class."),
            ("Do it on your own code",
             "Paste the largest class you maintain into the lab and note its four counts. "
             "Then group its public routines by the abstraction each serves, and write down "
             "how many groups you found."),
        ],
        "worked": {
            "title": "Five public fields",
            "intro": [
                "Count <code>public-fields</code> and say what its interface exposes.",
            ],
            "lines": [
                "fields: name, address, phone, salaryCents, vacationDays",
                "public and not final: all 5",
                "routines: the constructor and monthlyPayCents, 2",
                "public routines: 2",
                "callers that touch salaryCents depend on its type",
            ],
            "after": [
                "Any caller may set `salaryCents` to anything, and any change to how pay is "
                "stored, cents in an `int` today, a `Money` tomorrow, reaches every caller "
                "that reads it. Making the fields private and adding the readers callers "
                "actually need is the change <code>private-fields</code> shows.",
            ],
        },
        "quiz_title": "Interfaces, counted and read",
        "quiz": [
            {"q": "In the exercise's `Point`, how many fields and public fields are there, and "
                  "what does a caller need once `x` and `y` are private?",
             "a": ["3 fields, 2 public; a reader for each, or whatever the callers do with them",
                   "3 fields, 3 public; nothing, since `label` is already private",
                   "2 fields, 2 public; a reader for each",
                   "3 fields, 2 public; nothing, since `distanceTo` already reads them"],
             "c": 0,
             "why": "`Point` declares `x`, `y` and `label`, and `x` and `y` are public: 3 and "
                    "2. Made private, a caller needs `x()` and `y()`, or better whatever the "
                    "callers actually do with them. The kiosk's routines serve three "
                    "abstractions: tickets (`issueTicket`, `refundTicket`), the weather "
                    "forecast (`fetchForecast`, `showForecast`) and an audit log "
                    "(`openAuditLog`, `closeAuditLog`), so three classes. That is by the names "
                    "alone; a reader who keeps the audit log with the tickets has made a "
                    "design decision, not a counting error."},
            {"q": "A class declares `public static final int MAX = 10;`, `public String name;` "
                  "and `private int age;`. What do the lab's first two tiles print?",
             "a": ["3 fields, 2 public", "3 fields, 1 public",
                   "2 fields, 1 public", "1 field, 1 public"],
             "c": 1,
             "why": "All three are fields. The public-fields tile counts public fields that "
                    "are not final, so `MAX`, a constant, is not counted and `name` is: 1."},
            {"q": "Section 6.2 finds a class implementing more than one abstract data type. "
                  "What does it say to do?",
             "a": ["Make every field private and add accessors",
                   "Reorganise it into classes that each implement one well-defined "
                   "abstract data type",
                   "Inherit the second abstraction from a library class",
                   "Document which routines belong to which abstraction"],
             "c": 1,
             "why": "Each class should implement one and only one abstract data type; a class "
                    "implementing more, or none you can name, should be reorganised. Inheriting "
                    "from a container is the section's own example of mixing two abstractions, "
                    "and accessors do not join two abstractions into one."},
            {"q": "Above about how many data members does the book suggest considering "
                  "whether a class should be split?",
             "a": ["Three", "Seven", "Twelve", "Twenty"],
             "c": 1,
             "why": "About seven, section 6.3 (pp. 143–144), after Miller's 1956 paper on how "
                    "many items people can hold in mind and Riel's 1996 book. The book allows "
                    "the high end of seven plus or minus two for simple fields and the low end "
                    "for complex objects."},
        ],
        "mistakes": [
            ("Thinking a getter and setter for every field makes a good interface",
             "The book does credit accessors with something: after Riel, it says a `Point` "
             "with get and set routines encapsulates its representation, where public `x`, "
             "`y` and `z` do not. But its test of an interface is the abstraction it presents, "
             "and section 6.2 applies that test to the public routines as a whole. The "
             "lesson's <code>kitchen-sink</code> has six public routines; adding accessors "
             "for its nine fields would not make them one abstraction, and the exercise asks "
             "how many there are."),
            ("Taking private for hidden",
             "Private fields stop callers reading the data. They do not stop callers relying "
             "on how the class happens to behave: skipping an initialisation because another "
             "routine is known to do it, or using a constant because it happens to equal "
             "another. Section 6.2 calls these semantic violations of encapsulation, and "
             "says that a caller who reads the implementation to learn how to use a class is "
             "programming through its interface, not to it."),
            ("Treating a class as a bag of data with routines",
             "A class with whatever fields and routines were convenient is what section 6.1 "
             "calls a class in name only, a carrying case for loosely related data. The "
             "abstract data type is what makes it a class: data used only through operations "
             "that describe it in the problem's own terms."),
        ],
        "standard": (
            "Finish when you can read a class's interface and count what it exposes.",
            "For a class listing, state the field count, the public non-constant fields and "
            "the routines a caller can reach, and name the abstractions its public routines "
            "serve."
        ),
        "note": (
            "The lab counts declarations by the rules under its listing; it does not judge "
            "them, and it cannot tell whether public routines belong together, which is the "
            "chapter's main question. The classes are the lesson's own. The figure of about "
            "seven data members is the book's guideline, drawn from Miller's work on short-term "
            "memory, not a measured threshold."
        ),
    },
    # ---------------------------------------------------------------- 04
    # McConnell Chapter 6, sections 6.3-6.6, pp. 143-160.
    # Quote: p. 160 (Key Points), 13 words, cc_quotes.py OK; inner marks as
    # lsquo/rsquo.
    # Bloch's line as the book quotes it: p. 144, 8 words, cc_quotes.py OK.
    # "grossly optimistic": p. 147, 2 words. Lesson total: 23 words.
    # Containment (p. 143); inheritance and LSP (pp. 144-145, Liskov 1988;
    # Hunt and Thomas 2000); depth (p. 147); multiple inheritance as a chain
    # saw (pp. 148-149); the summary (p. 149); members, Demeter and
    # constructors (pp. 150-152); reasons to create a class (pp. 152-155);
    # classes to avoid (p. 155); sections 6.5 and 6.6 (pp. 156-157).
    # F7, p. 147: Riel 1996's six levels; McConnell: two or three; Basili,
    # Briand and Melo 1996.
    {
        "slug": "inheritance-containment-and-members",
        "title": "Inheritance, Containment and Members",
        "module": "Chapter 6 · Working Classes",
        "one_line": "Contain before you inherit; inherit only for a true “is a” that a caller cannot tell apart, and keep the hierarchy shallow.",
        "summary": (
            "Sections 6.3 to 6.6 cover how a class is built inside: containment, inheritance "
            "and its rules, members, constructors, and the reasons to create a class at all. "
            "Compute the depth of an inheritance hierarchy, read it against the book's "
            "guidance, and say whether a subclass can stand in for its parent."
        ),
        "key": [
            "has a: containment, the workhorse",
            "is a: inheritance, with care",
            "a subclass must stand in for its parent",
            "depth: levels from the root, root is 1",
            "most people manage two or three levels",
        ],
        "key_label": "Sections 6.3 to 6.6 in five lines",
        "concepts_intro": (
            "Two relationships and one principle carry section 6.3. The rest of the chapter "
            "is guidance on members and on when a class is worth having."
        ),
        "concepts": [
            ("Containment",
             "A class that holds another as a field: an employee has a name, has an "
             "address. The book calls it the workhorse technique of object-oriented "
             "programming."),
            ("Inheritance",
             "A class that is a more specialised version of another: it inherits the "
             "parent's interface, and perhaps its implementation, and must keep the "
             "parent's promises."),
            ("Substitution",
             "The Liskov substitution principle (Liskov 1988): a subclass should be usable "
             "through its parent's interface without the caller knowing the difference."),
        ],
        "read_title": "The chapter's rules first, then a hierarchy measured",
        "read_intro": (
            "Read sections 6.3 to 6.6, pages 143 to 160, in your own copy first. The lesson "
            "sets out the argument, then measures two hierarchies and leaves a subclass for "
            "you to test."
        ),
        "body": [
            ("p", "&ldquo;Containment is usually preferable to inheritance unless you’re "
                  "modeling an &lsquo;is a&rsquo; relationship.&rdquo; That is one of "
                  "Chapter 6's key points (p. 160). This lesson reads sections 6.3 to 6.6, "
                  "pages 143 to 160: how a class is built inside, and when a class is worth "
                  "creating at all. Read them in your own copy first."),
            ("p", "Once a class has an interface, the chapter asks how to build what is "
                  "behind it, and it starts with the plainest answer. Containment, a class "
                  "holding another as a field, is the workhorse; more is written about "
                  "inheritance, it says, because inheritance is trickier and more "
                  "error-prone, not because it is better. Private inheritance to get at a "
                  "contained class's protected members is a last resort, a C++ device; Java has no private inheritance, so "
                  "the question does not arise there."),
            ("p", "Inheritance means &ldquo;is a&rdquo;: the new class is a more specialised "
                  "version of the old, and must keep the contract the old one sets. The book "
                  "quotes Joshua Bloch: &ldquo;Design and document for inheritance, or "
                  "prohibit it.&rdquo; In Java the prohibition is `final`. Then comes the "
                  "principle with a person behind it. In a 1988 paper Barbara Liskov argued "
                  "that one class should inherit from another only if it truly is a more "
                  "specific version of it, and the book gives Hunt and Thomas's summary: a "
                  "subclass must be usable through its parent's interface without the "
                  "caller knowing the difference. Its example is an account whose interest "
                  "routine returns a rate with the opposite sign from its parent's; every "
                  "caller would have to know which kind it held."),
            ("p", "More rules follow. Move common interface, data and behaviour as high as "
                  "abstraction allows; be suspicious of a base class with one derived "
                  "class, and of an override that does nothing; and keep hierarchies "
                  "shallow. Riel, the book reports, suggests a limit of six levels; "
                  "McConnell calls that &ldquo;grossly optimistic&rdquo; and says most "
                  "people have trouble juggling more than two or three, and that deep trees "
                  "have been significantly associated with higher fault rates (Basili, "
                  "Briand and Melo 1996). If inheritance is a chain saw, he adds, multiple "
                  "inheritance is a 1950s chain saw with no blade guard. The section's "
                  "summary is a heavy bias against inheritance: contain when classes share "
                  "only data; inherit when they share behaviour, or when the base class "
                  "should control the interface."),
            ("p", "The section ends with members and constructors: keep the number of "
                  "routines in a class small; minimise the routines a class calls and the "
                  "classes it uses; follow the Law of Demeter (Lieberherr and Holland), "
                  "under which an object may call routines on the objects it holds but not "
                  "on the objects those return; initialise all member data in every "
                  "constructor; and prefer deep copies to shallow ones until shown otherwise."),
            ("p", "Section 6.4 asks why to create a class at all. Modelling real-world and "
                  "abstract objects are reasons, but the single most important one, it says, "
                  "is to reduce complexity; others are to isolate complexity, hide "
                  "implementation details, limit the effects of change and make central "
                  "points of control. It warns against god classes that know and do "
                  "everything, classes with data and no behaviour, and classes named after "
                  "verbs. Section 6.5 is on language-specific issues, which these lessons "
                  "leave to the book, and 6.6 on packages, which Java has as a feature."),
            ("p", "Now the count. The lab reads a hierarchy as `child, parent` records and "
                  "prints its depth, with a root at level 1, the deepest class (the "
                  "alphabetically first, when several tie, with the banner naming every "
                  "one), the number of classes and the number of leaves, classes nothing "
                  "extends. The preset <code>shallow</code> has `Circle`, `Square` and "
                  "`Triangle` under `Shape`: depth 2, deepest Circle (tied with the other "
                  "two), 4 classes and 3 leaves."),
            ("p", "The preset <code>deep</code> is a chain of accounts: `Record`, `Account`, "
                  "`DepositAccount`, `SavingsAccount`, `BonusSavings`, "
                  "`HolidayBonusSavings` and `ChristmasHolidaySavings`, with "
                  "`CheckingAccount` beside `SavingsAccount`. The lab prints depth 7, deepest "
                  "ChristmasHolidaySavings, 8 classes and 2 leaves. Read 7 against "
                  "McConnell's two or three, not against Riel's six. What it measures is how "
                  "many classes a reader must open to know what one call on a "
                  "`ChristmasHolidaySavings` does, when any of the six above may have "
                  "defined or overridden it."),
            ("p", "The depth is the part of this section a count can reach. Substitution is "
                  "not: the lab cannot tell whether a subclass keeps its parent's promises, "
                  "because that depends on what a caller expects, not on the shape of the "
                  "tree. To test a subclass, name a caller of the parent, write down what "
                  "it expects, and run the subclass through it by hand."),
            ("h3", "Exercise"),
            ("p", "First, the hierarchy `Dog, Mammal; Cat, Mammal; Mammal, Animal; Animal, "
                  "LivingThing; Puppy, Dog`. Second, this `Square`, which extends "
                  "`Rectangle` and overrides both setters so that each sets both sides:"),
            ("code", _lines(SQUARE_EXERCISE)),
            ("p", "For the hierarchy, give its depth and its deepest class. For `Square`, say "
                  "whether it can stand in for `Rectangle`, naming a caller of `Rectangle` "
                  "it would break and what that caller gets. You can type the hierarchy into "
                  "the lab afterwards to check the depth."),
            ("p", "Classes are made of routines. The next lesson, Reasons to Create a "
                  "Routine, begins Chapter 7, on what a good routine is for."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "tree",
            "preset": "shallow",
            "presets": [
                {"id": "shallow",
                 "label": "Shallow: three shapes under Shape (illustrative)",
                 "edges": "Circle, Shape; Square, Shape; Triangle, Shape",
                 "expect": {"dgDepth": "2", "dgDeepest": "Circle"}},
                {"id": "deep",
                 "label": "Deep: a chain of account classes (illustrative)",
                 "edges": "Account, Record; DepositAccount, Account; "
                          "SavingsAccount, DepositAccount; BonusSavings, SavingsAccount; "
                          "HolidayBonusSavings, BonusSavings; "
                          "ChristmasHolidaySavings, HolidayBonusSavings; "
                          "CheckingAccount, DepositAccount",
                 "expect": {"dgDepth": "7", "dgDeepest": "ChristmasHolidaySavings"}},
            ],
            "panel_title": "Measure an inheritance hierarchy",
            "panel_intro": (
                "Each record is one class and the class it extends, written child, parent. "
                "The lab prints the depth with a root at level 1, the deepest class, the "
                "classes and the leaves. It cannot tell whether a subclass can stand in for "
                "its parent; that is a question about callers."
            ),
        }),
        "steps_title": "Measuring a hierarchy and testing a subclass",
        "steps_intro": "Five steps, the last of them on your own code.",
        "steps": [
            ("Find the roots",
             "A root is a class that extends nothing in the list. It is at level 1."),
            ("Number the levels",
             "Each class is one level below its parent. The depth is the largest level, and "
             "the deepest class is the one at it."),
            ("Name a caller of the parent",
             "Pick a piece of code that uses the parent through its interface, and write "
             "down exactly what it expects: a value, a state after a call, an exception "
             "or none."),
            ("Run the subclass through it",
             "Trace the caller with the subclass in the parent's place. If it gets anything "
             "other than what it expected, the subclass does not substitute."),
            ("Do it on your own code",
             "Take one inheritance chain from your own code, type it into the lab as "
             "child, parent records and note the depth. For its deepest class, write down "
             "one caller of its parent it could break, and what that caller would get."),
        ],
        "worked": {
            "title": "Seven levels of accounts",
            "intro": [
                "Number the levels of <code>deep</code> from its root, `Record`.",
            ],
            "lines": [
                "Record 1, Account 2, DepositAccount 3",
                "SavingsAccount 4, CheckingAccount 4",
                "BonusSavings 5, HolidayBonusSavings 6",
                "ChristmasHolidaySavings 7: the depth",
                "classes 8; leaves CheckingAccount and the last, 2",
            ],
            "after": [
                "Seven levels is more than twice the two or three McConnell says most people "
                "can manage. The count does not say the design is wrong; it says that to "
                "know what a call on the deepest class does, a reader may have to look in "
                "seven places.",
            ],
        },
        "quiz_title": "Hierarchies and substitution",
        "quiz": [
            {"q": "In the exercise, what is the depth of `Dog, Mammal; Cat, Mammal; Mammal, "
                  "Animal; Animal, LivingThing; Puppy, Dog`, and can the `Square` stand in "
                  "for `Rectangle`?",
             "a": ["Depth 5 at `Puppy`; no, a caller expecting an area of 20 gets 25",
                   "Depth 4 at `Puppy`; no, a caller expecting an area of 20 gets 25",
                   "Depth 5 at `Puppy`; yes, its area is always width times height",
                   "Depth 5 at `LivingThing`; no, a caller expecting an area of 20 gets 25"],
             "c": 0,
             "why": "`LivingThing` is the root at level 1, then `Animal` 2, `Mammal` 3, `Dog` "
                    "4 and `Puppy` 5. A caller of `Rectangle` that sets the width to 4, then "
                    "the height to 5, expects an area of 20; the `Square` sets both sides to "
                    "5 on the second call and returns 25, so it does not substitute. A "
                    "`Square` that overrode only `setWidth` would pass this caller, because "
                    "the height set last wins, which is why the exercise overrides both. "
                    "`LivingThing` is the root, not the deepest class."},
            {"q": "The hierarchy `C, B; B, A; D, A; E, D; F, E`, with a root at level 1. What "
                  "are its depth and deepest class?",
             "a": ["3, `F`", "4, `F`", "5, `F`", "4, `C`"],
             "c": 1,
             "why": "`A` is the root, 1; `B` and `D` are 2; `C` and `E` are 3; `F` is 4. `C` "
                    "is a leaf at level 3, not the deepest; 5 would count an edge as a level."},
            {"q": "How many levels of inheritance does McConnell say most people have "
                  "trouble going beyond?",
             "a": ["Two or three", "Six", "Seven, plus or minus two", "Ten"],
             "c": 0,
             "why": "Section 6.3 (p. 147): Riel suggests six levels, and McConnell calls that "
                    "grossly optimistic; in his experience most people have trouble juggling "
                    "more than two or three. Seven plus or minus two, he says, is better "
                    "applied to the number of subclasses of a base class."},
            {"q": "Several classes share common data but not behaviour. What does section "
                  "6.3's summary recommend?",
             "a": ["Derive them all from a common base class that holds the data",
                   "Create a common object the classes can contain",
                   "Use multiple inheritance",
                   "Copy the data into each class"],
             "c": 1,
             "why": "Shared data without shared behaviour calls for containment: a common "
                    "object each class holds. Inheritance is for shared behaviour, or for "
                    "shared data and behaviour together."},
        ],
        "mistakes": [
            ("Treating inheritance as the main way to reuse code",
             "Inheritance does let a subclass reuse its parent's code, and that is why it "
             "is reached for. Section 6.3 says containment is the workhorse and inheritance "
             "the trickier tool, to be used for an &ldquo;is a&rdquo; relationship that keeps "
             "the parent's contract, with a heavy bias against it otherwise. Reuse without "
             "&ldquo;is a&rdquo; is what containment is for. The depth tile counts one of "
             "inheritance's costs: in <code>deep</code>, seven classes to read for one call."),
            ("Thinking a subclass that compiles can stand in for its parent",
             "The compiler checks that a subclass has the parent's routines, not that they "
             "mean the same thing. Substitution is about meaning: the book's account whose "
             "interest routine returns a rate with the opposite sign compiles, and still "
             "breaks every caller that relied on the parent's behaviour."),
            ("Allowing deep hierarchies because each level is small",
             "Each class in a chain may be simple, and the chain still hard to follow, "
             "because a call can be defined or overridden at any level above. The book "
             "reports Riel's six levels and calls them grossly optimistic, puts most people's "
             "limit at two or three, and cites a study associating deep trees with higher "
             "fault rates."),
        ],
        "standard": (
            "Finish when you can measure a hierarchy and test a subclass.",
            "For a hierarchy given as child, parent pairs, state its depth and deepest "
            "class; for a stated subclass, say whether it can stand in for its parent, "
            "naming a caller it would break and what that caller gets."
        ),
        "note": (
            "The lab measures the shape of a hierarchy you type; it cannot read a subclass's "
            "code or tell whether it keeps its parent's promises, which is what substitution "
            "is about. The hierarchies are illustrative. The figures on depth are the book's "
            "guidance and its report of Riel and of one study, not limits the lab enforces."
        ),
    },
]
