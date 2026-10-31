"""Layers and Performance, lessons 1-5 -- the Preface, the Introduction,
Chapter 1, and two base patterns from Chapter 18.

Fowler et al., Patterns of Enterprise Application Architecture
(Addison-Wesley, 2002): the Preface; the Introduction (Architecture,
Enterprise Applications, Kinds of Enterprise Application, Thinking About
Performance, Patterns); Chapter 1, Layering; and Chapter 18, Layer Supertype
and Separated Interface. The lessons cite the book by chapter, section and
pattern; the PDF pages in the comments are the operator's copy's, which has no
printed page numbers. Every quotation is copied from that copy and checked
with ea_quotes.py; every figure attributed to the book carries its PLAN
section S.2 id. The code is written for these lessons: none of the book's
listings or example domains is used. Each snippet is one constant below,
verbatim from docs/enterprise-patterns/presets.py, used by the lesson's code
block and, for a cckit code lab, by the preset that counts it.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# Enterprise Applications: presets due-day and due-day-plain; LATE_FEE is the
# exercise (PLAN section D.4, verbatim).
DUE_DAY = """\
// Days from the start of the invoice month until payment is due.
int dueDay(Customer c, int invoiceDay) {
    int day = invoiceDay + 30;
    if (c.isGovernment()) {
        day = day + 15;
    }
    if (c.region() == Region.NORTH && c.years() > 5) {
        day = day + 10;
    }
    if (c.isRetail() || c.isOnline()) {
        if (invoiceDay > 25) {
            day = day + 5;
        }
    }
    if (day > 60 && !c.isGovernment()) {
        day = 60;
    }
    return day;
}"""

DUE_DAY_PLAIN = """\
// Days from the start of the invoice month until payment is due.
int dueDay(Customer c, int invoiceDay) {
    return invoiceDay + 30;
}"""

LATE_FEE = """\
// Fee in cents for a late payment, with the agreed exceptions.
long lateFee(Account a, int daysLate) {
    long fee = 0;
    if (daysLate > 10) {
        fee = 500;
    }
    if (daysLate > 30 || a.isFlagged()) {
        fee = 2500;
    }
    if (a.isCharity() && daysLate < 60) {
        fee = 0;
    }
    if (a.isNew() && a.payments() == 0) {
        fee = fee / 2;
    }
    return fee;
}"""

# Thinking About Performance: read in the body; no lab figures.
RESPONSE_TIME = """\
// Times one request. Run it at each load you care about.
long responseMillis(Service service, Request request) {
    long start = System.nanoTime();
    service.handle(request);
    return (System.nanoTime() - start) / 1000000;
}"""

# Capacity and Scalability: read in the body; the loop pzNeed does.
SERVERS_NEEDED = """\
// Servers needed for a target load, from two measured rates.
int serversNeeded(int firstTps, int extraTps, int targetTps) {
    if (extraTps <= 0 && firstTps < targetTps) {
        throw new IllegalArgumentException("more servers add nothing");
    }
    int servers = 1;
    int tps = firstTps;
    while (tps < targetTps) {
        servers = servers + 1;
        tps = tps + extraTps;
    }
    return servers;
}"""

# Layering: presets rising-twice and rising-once; OVERDUE_TWICE is the exercise.
RISING_TWICE = """\
// Web page: show a product, red if sales rose more than 10%.
void showProduct(Product p, Page page) {
    long before = p.salesLastMonth();
    long now = p.salesThisMonth();
    boolean rising = now * 100 > before * 110;
    page.write(p.name(), now, rising);
}

// Command line: the same report, for a script.
void printProduct(Product p, PrintStream out) {
    long before = p.salesLastMonth();
    long now = p.salesThisMonth();
    boolean rising = now * 100 > before * 110;
    out.println(p.name() + " " + now + (rising ? " *" : ""));
}"""

RISING_ONCE = """\
// Domain layer: the rule, in one place.
boolean isRising(Product p) {
    return p.salesThisMonth() * 100 > p.salesLastMonth() * 110;
}

// Presentation: the web page and the command line both ask.
void showProduct(Product p, Page page) {
    page.write(p.name(), p.salesThisMonth(), isRising(p));
}

void printProduct(Product p, PrintStream out) {
    String mark = isRising(p) ? " *" : "";
    out.println(p.name() + " " + p.salesThisMonth() + mark);
}"""

OVERDUE_TWICE = """\
// Report screen
void showInvoice(Invoice inv, Page page) {
    int days = inv.daysOpen();
    boolean overdue = days > 30 && !inv.isDisputed();
    page.write(inv.number(), overdue);
}

// Nightly export
void exportInvoice(Invoice inv, Writer csv) throws IOException {
    int days = inv.daysOpen();
    boolean overdue = days > 30 && !inv.isDisputed();
    csv.write(inv.number() + "," + overdue + "\\n");
}"""

# Layer Supertype and Separated Interface: read in the body; the lab counts
# the dependencies the prose states.
SEPARATED_FINDER = """\
// Domain package: the interface the domain needs.
interface OrderFinder {
    Order find(long id);
}

// Domain package: Order uses only the interface.
class Order {
    private static OrderFinder finder;
    static void setFinder(OrderFinder f) { finder = f; }
    static Order load(long id) { return finder.find(id); }
}

// Mapper package: the implementation, which knows the SQL.
class OrderMapper implements OrderFinder {
    public Order find(long id) {
        // SELECT ... FROM orders WHERE id = ?
        return new Order();
    }
}"""


_COMPLEXITY_INTRO = (
    "The lab counts decision points by a stated rule: one, plus one for each if, while, "
    "for and case, and each conditional and or conditional or. The bands beside the count are McConnell's, from Code "
    "Complete; Fowler gives no count. The listings are the lesson's, and the agreements "
    "in them are invented."
)

_A_AND_B = "a, 10, 500; a, 20, 500; b, 10, 200; b, 20, 2000"
_SWORDFISH_AND_CAMEL = "swordfish, 1, 20; swordfish, 2, 35; camel, 1, 40; camel, 2, 50"


LESSONS = [
    # ---------------------------------------------------------------- 1.1
    # Preface (PDF pp. 15-20 of the operator's copy) and Introduction
    # (pp. 21-31): Architecture p. 22, Enterprise Applications pp. 23-24,
    # Kinds of Enterprise Application pp. 25-26, Patterns pp. 29-31.
    # Quote: PDF p. 24 of the operator's copy, 18 words, ea_quotes.py OK.
    # "half baked" (Fowler's phrase, PDF p. 29 of the operator's copy), 2 words,
    # ea_quotes.py OK. Lesson total: 20 words. Alexander's definition is
    # paraphrased, not quoted.
    # F1, PDF p. 23 of the operator's copy: over 1 GB, tens of millions of records.
    # F2, PDF p. 25 of the operator's copy: no more than a hundred or so users.
    {
        "slug": "enterprise-applications",
        "title": "Enterprise Applications",
        "module": "Introduction",
        "one_line": "An enterprise application is known by its data, its many users and screens, the systems around it, and business rules that follow no principle.",
        "summary": (
            "The Preface and the Introduction's first sections: how the book is meant to be "
            "read, what Fowler means by architecture, what makes an application an enterprise "
            "application, the three kinds he contrasts, and what a pattern is. Count the "
            "decision points in a business rule written for the lesson, and see that each "
            "one comes from an agreement rather than from logic."
        ),
        "key": [
            "narratives: read through; patterns: look up",
            "enterprise: persistent, shared, integrated",
            "business rules: agreed, not derived",
            "points: 1 + each if, for, while, case, &&, ||",
            "a pattern: advice found in practice",
            "the example is not the pattern",
        ],
        "key_label": "The Preface and Introduction in six lines",
        "concepts_intro": (
            "Three words carry the opening of the book. Every later chapter takes them for "
            "granted."
        ),
        "concepts": [
            ("Enterprise application",
             "Fowler gives no precise definition, only marks: persistent data that outlives "
             "the programs and machines that made it, a lot of it, used by many people at "
             "once through many screens, joined to other systems that disagree about what "
             "the data means. Payroll, patient records and foreign exchange trading are "
             "enterprise applications; compilers, games and elevator controllers are not."),
            ("Business logic",
             "The rules of the business the application carries out: what is charged, when, "
             "to whom, and with which exceptions. Fowler's point is that they are given to "
             "you, agreed one case at a time, and follow no principle you could derive them "
             "from."),
            ("Pattern",
             "In Christopher Alexander's sense, which the Introduction starts from, a problem "
             "that keeps recurring and the core of a solution that can be applied again and "
             "again, each time a little differently. Fowler adds that a pattern is a piece of "
             "advice, found by watching what works in practice, and that it always has to be "
             "finished off in your own project."),
        ],
        "read_title": "The book's opening, then the count",
        "read_intro": (
            "Read the Preface and the Introduction's sections Architecture, Enterprise "
            "Applications, Kinds of Enterprise Application and Patterns in your own copy "
            "first. The lesson sets out their argument in its own words and then counts the "
            "special cases in one business rule."
        ),
        "body": [
            ("p", "&ldquo;I find this a curious term because there are few things that are "
                  "less logical than business logic.&rdquo; Fowler writes that of the phrase "
                  "<em>business logic</em> in the Introduction's section Enterprise "
                  "Applications, and the sentence holds the whole book's starting point: the "
                  "hard part of these systems is not clever algorithms but a great deal of "
                  "shared data and a great many rules nobody can simplify. This lesson reads "
                  "the Preface and the Introduction's first sections. Read them in your own "
                  "copy first."),
            ("p", "The Preface begins with a project. In the spring of 1999 Fowler flew to "
                  "Chicago to consult for ThoughtWorks on a back-end leasing system, the kind "
                  "that handles everything after a lease is signed: billing, upgrades, chasing "
                  "late payers, early returns. Leasing deals, he says, vary without end, "
                  "because small variations win business, and every such victory adds "
                  "complexity. The domain model had to be stored in a relational database, "
                  "given a user interface, opened to remote applications and joined to other "
                  "packages, all on J2EE, which nobody yet had real experience of. The book is "
                  "written for that situation. It has two parts: narrative chapters to read "
                  "from start to finish, and patterns to dip into as a reference. This "
                  "read-along takes them together, each narrative with the patterns it "
                  "introduces."),
            ("p", "The section Architecture is short and wary. Fowler calls the word one that "
                  "mostly signals importance, and admits, with a smiley, that he is pragmatic "
                  "enough to use it anyway. People agree on little, he says, except two "
                  "elements: how a system is divided into its parts at the top, and the "
                  "decisions that would be hard to reverse. Following a posting of Ralph Johnson's, "
                  "he adds that architecture is subjective, a shared understanding among a "
                  "project's expert developers, so that something found easy to change stops "
                  "being architectural. The architectural pattern he likes most is layers, and "
                  "the book is about how an enterprise application is divided into them."),
            ("p", "Enterprise Applications gives the marks of the kind. The data is persistent, "
                  "kept for years, outliving hardware, operating systems and compilers, and "
                  "migrated whenever the application is replaced. There is a lot of it: a "
                  "moderate system, Fowler says, holds over 1 GB in tens of millions of "
                  "records, so managing it is a major part of the work. Many people use it at "
                  "once, through many screens, and there is batch processing that is easy to "
                  "forget. And it lives among other systems built at different times with "
                  "different technologies, which disagree even about what a customer is. Then "
                  "come the rules: given to you, changeable only by political effort, full of "
                  "strange conditions that interact. His example is a salesman who agreed to "
                  "move one customer's payment to win the business; a few thousand such "
                  "one-off cases add up to what he calls business illogic."),
            ("p", "Kinds of Enterprise Application then refuses a single answer. Fowler sets "
                  "out three points on a large plane: an online retailer with a very high "
                  "number of users and fairly simple logic, which must above all scale; a "
                  "leasing system with few users, no more than a hundred or so at a time, but "
                  "complicated and arbitrary rules, a richer interface and a large schema; and "
                  "a small company's expense tracker, simple in every way except that it must "
                  "be built quickly and may grow. Each has different difficulties, so no one "
                  "architecture suits all three. He has, he says, alarm bells that ring when "
                  "someone says always do this, and much of his book is about choosing between "
                  "alternatives."),
            ("p", "Patterns closes the opening. Fowler starts from Christopher Alexander's "
                  "definition, a recurring problem and the core of its solution, a core that "
                  "can be reused endlessly and never comes out in quite the same form, "
                  "and adds his own: a pattern is a piece of advice, rooted in practice, "
                  "discovered rather than invented, and its value to an experienced designer "
                  "is the shared vocabulary it gives. Every pattern in Part 2 has the same "
                  "parts: a name, an intent and a sketch, a motivating problem, How It Works, "
                  "When to Use It, further reading and examples. He insists that the example "
                  "is not the pattern; patterns are, in his phrase, &ldquo;half baked,&rdquo; and you finish "
                  "them in your own project."),
            ("code", _lines(DUE_DAY)),
            ("p", "Here is a business rule written for the lesson, a due date with four "
                  "agreements in it: government customers get fifteen more days, long-standing "
                  "northern customers ten, retail or online customers invoiced late in the "
                  "month five, and nobody but government waits past day 60. The agreements are "
                  "invented; they stand for the kind Fowler describes. The lab counts decision "
                  "points by a rule stated beside it: one, plus one for each `if`, `while`, "
                  "`for`, `case`, `&&` and `||`. On the preset <code>due-day</code> it counts "
                  "9, and its breakdown prints how: 1 + if 5 + && 2 + || 1. The `!` on line "
                  "15 adds nothing; it negates a condition and makes no new branch."),
            ("p", "The lab prints three more tiles. The band, 6–10, places the count between "
                  "McConnell's thresholds from <em>Code Complete</em>; Fowler gives no count "
                  "and no threshold, so the band is another author's guidance, not this "
                  "book's. The deepest nesting is 2, first reached at line 12, the statement "
                  "inside the `if` on line 11, which is inside the `if` on line 10. The preset "
                  "<code>due-day-plain</code> is the same routine with every agreement taken "
                  "out: 1 decision point, breakdown 1, band 0–5, nesting 0, line 3. The eight "
                  "points between the two listings are the agreements, and none of them could "
                  "have been derived from the plain rule. That is what the count shows: not "
                  "that the routine is badly written, but how much of it a reader has to learn "
                  "case by case."),
            ("h3", "Exercise"),
            ("code", _lines(LATE_FEE)),
            ("p", "Count the decision points in this late fee by the same rule, writing the "
                  "breakdown as the lab does, and name the agreement each `if` encodes. Then "
                  "paste the routine into the lab and compare."),
            ("p", "Fowler warns that advice about performance is not a fact until it is "
                  "measured. The next lesson, Thinking About Performance, reads the words he "
                  "uses for what is measured."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "bands": [5, 10],
            "book": "other",
            "preset": "due-day",
            "presets": [
                {"id": "due-day",
                 "label": "A due date with four agreements in it (illustrative)",
                 "code": DUE_DAY,
                 "expect": {"coDecisions": "9", "coBreakdown": "1 + if 5 + && 2 + || 1"}},
                {"id": "due-day-plain",
                 "label": "The same due date with every agreement taken out",
                 "code": DUE_DAY_PLAIN,
                 "expect": {"coDecisions": "1", "coBreakdown": "1"}},
            ],
            "panel_title": "The special cases in a business rule",
            "panel_intro": _COMPLEXITY_INTRO,
        }),
        "steps_title": "Counting a rule's special cases",
        "steps_intro": "Four steps, the last of them on a rule from a system you know.",
        "steps": [
            ("List the cases",
             "Read the routine and write down each condition under which it does something "
             "different, in the order the code tests them."),
            ("Count by the stated rule",
             "Start at one and add one for each `if`, `while`, `for`, `case`, `&&` and `||`. "
             "A `!`, a comparison and an `else` add nothing. Write the breakdown, kind by kind."),
            ("Name the agreement behind each",
             "For each decision point, say in a phrase which agreement it carries out, and "
             "mark any you cannot name: those are the ones to ask about."),
            ("Do it on a rule of your own",
             "Take one rule in a system you know that someone outside engineering agreed. "
             "Write its exceptions as a list and count them, then paste the code into the lab "
             "and set its count beside your list."),
        ],
        "worked": {
            "title": "Nine decision points in a due date",
            "intro": [
                "Count the preset <code>due-day</code> by the rule, kind by kind.",
            ],
            "lines": [
                "start at 1",
                "if: lines 4, 7, 10, 11 and 15, so 5",
                "&&: lines 7 and 15, so 2",
                "||: line 10, so 1",
                "1 + 5 + 2 + 1 is 9 decision points",
                "without the agreements: 1",
            ],
            "after": [
                "Every point past the first comes from an agreement someone made, and the "
                "plain routine shows what is left when they are taken out. The count does not "
                "say the agreements are wrong; it says how many a reader must learn.",
            ],
        },
        "quiz_title": "Enterprise applications and their rules",
        "quiz": [
            {"q": "Count the exercise's lateFee by the rule: one, plus one for each `if`, "
                  "`while`, `for`, `case`, `&&` and `||`. How many decision points does it have?",
             "a": ["7", "8", "5", "10"],
             "c": 1,
             "why": "8: 1 + if 4 + && 2 + || 1. The four `if`s carry the agreements: a fee "
                    "after ten days late; a larger fee after thirty days or for a flagged "
                    "account (the `||`); no fee for a charity under sixty days (an `&&`); half "
                    "the fee for a new account with no payments (the other `&&`). Seven forgets "
                    "the starting one, five counts only the `if`s and the one, and ten counts "
                    "the comparisons `==` and `<`, which make no branch of their own."},
            {"q": "Which of these does the Introduction give as marks of an enterprise "
                  "application?",
             "a": ["A large code base worked on by many developers",
                   "Hard multithreading problems and integration with hardware",
                   "Persistent data used by many people at once and shared with other systems",
                   "A rich-client user interface"],
             "c": 2,
             "why": "Enterprise Applications names persistent data, a lot of it, concurrent "
                    "access, many screens and integration with other systems. It says that not "
                    "all enterprise applications are large, that they mostly lack the "
                    "multithreading and hardware problems of telecoms software, and that many "
                    "use a Web presentation rather than a rich client."},
            {"q": "On the Introduction's account, why can business logic not be simplified "
                  "by finding its principle?",
             "a": ["Because it is usually written in the presentation layer",
                   "Because its rules were agreed one case at a time, often to win business, "
                   "and follow from no principle",
                   "Because there is too much data for any principle to cover",
                   "Because business people write the code themselves"],
             "c": 1,
             "why": "Fowler's point is that business rules are given to you and changeable "
                    "only with political effort; a salesman's one-off agreement to win a deal "
                    "is his example, and a few thousand of them make the illogic. Where the "
                    "logic sits, and how much data there is, are other questions."},
            {"q": "The lab prints the band 6–10 beside the count of 9 for <code>due-day</code>. Whose "
                  "thresholds are those bands?",
             "a": ["Fowler's, from the Introduction",
                   "McConnell's, from Code Complete",
                   "The lesson's own, chosen for this course",
                   "Alexander's, from A Pattern Language"],
             "c": 1,
             "why": "The bands are McConnell's guidance in <em>Code Complete</em>, which the "
                    "lab reuses. Fowler gives no count of decision points and no threshold; "
                    "the panel and the banner both say whose the bands are."},
        ],
        "mistakes": [
            ("Thinking business logic is logic, so the special cases will go",
             "On this view, find the principle behind the rules and the special cases "
             "disappear. Fowler's point in Enterprise Applications is that they do not: the "
             "rules were agreed one negotiation at a time, often to win business, and the "
             "program has to carry them as they are, knowing only that they will change. On "
             "the lesson's illustration, eight of the due date's nine decision points come "
             "from agreements nobody could derive from the plain rule."),
            ("Taking an enterprise application to be a big one",
             "Fowler says plainly that not all enterprise applications are large, and Kinds "
             "of Enterprise Application gives a small company's expense tracker as one of its "
             "three examples. What makes an application enterprise is persistent, shared, "
             "integrated data and the rules over it, not its size; he adds that small "
             "systems, taken together, matter a great deal to a business."),
            ("Copying a pattern's example as the pattern",
             "The Introduction insists that the example is not the pattern. Each example is "
             "kept simple to show one idea, leaves out error handling and much else, and is "
             "not meant to be used as it stands. A pattern is unfinished, as Fowler puts it: "
             "you finish it in your own project, and it never comes out quite the same twice."),
        ],
        "standard": (
            "Finish when you can list a business rule's special cases and count its decision points.",
            "Given a routine that encodes a business rule, list each special case it carries "
            "and count its decision points by the stated rule, one plus each `if`, `while`, "
            "`for`, `case`, `&&` and `||`, with the breakdown by kind."
        ),
        "note": (
            "The lab counts decision points in the listing; it cannot tell which came from an "
            "agreement and which from a slip, and it cannot say whether an agreement still "
            "holds. Fowler gives no count at all, and the bands are another book's. What the "
            "chapter asks of you is to organise these rules as well as you can, because the "
            "only certain thing about them is that they will change."
        ),
    },
    # ---------------------------------------------------------------- 1.2
    # Introduction, Thinking About Performance, first half (PDF p. 27 of the
    # operator's copy; load, load sensitivity and the illustration, p. 28).
    # Quote: PDF p. 27 of the operator's copy, 16 words, ea_quotes.py OK; the
    # apostrophe is the copy's. Lesson total: 16 words.
    # F3, PDF p. 28 of the operator's copy: A 0.5 s from 10 to 20 users; B 0.2 s
    # at 10 rising to 2 s at 20. The presets give them in ms.
    {
        "slug": "performance-terms",
        "title": "Thinking About Performance",
        "module": "Introduction",
        "one_line": "Fowler's words for performance, response time, responsiveness, latency, throughput, load and load sensitivity, and his rule that no advice about it is a fact until you measure.",
        "summary": (
            "The first half of the Introduction's section Thinking About Performance: "
            "Fowler's caution that performance advice must be measured on your own "
            "configuration, and the terms he uses in the rest of the book. Compute load "
            "sensitivity from the book's illustration of two systems measured at two loads, "
            "and see which is faster depends on the load."
        ),
        "key": [
            "measure before and after, on your setup",
            "response time: processing a request",
            "responsiveness: acknowledging it",
            "latency: the least time for any response",
            "change a user: rise in ms / rise in users",
            "ratio: last time / first time",
        ],
        "key_label": "Thinking About Performance, first half",
        "concepts_intro": (
            "Fowler defines his terms because, he says, they are used inconsistently. Three "
            "of them do most of the work in this lesson."
        ),
        "concepts": [
            ("Response time and responsiveness",
             "Response time is how long the system takes to process a request from outside, "
             "a button press or an API call. Responsiveness is how quickly it acknowledges "
             "the request. A progress bar during a file copy improves responsiveness and "
             "leaves response time as it was."),
            ("Latency and throughput",
             "Latency is the least time any response takes, even when there is no work to do; "
             "it is the big cost of a remote call, and an application developer can rarely "
             "reduce it. Throughput is how much is done in a given time, bytes a second or, "
             "for enterprise applications, transactions a second."),
            ("Load and load sensitivity",
             "Load is how much stress the system is under, such as how many users are "
             "connected, and it is the context of another measurement: a response time is "
             "at some load. Load sensitivity is how the response time varies with the load. "
             "A system that degrades more is more load sensitive."),
        ],
        "read_title": "The section's caution first, then its terms",
        "read_intro": (
            "Read the Introduction's section Thinking About Performance as far as load "
            "sensitivity in your own copy first. The lesson sets out the caution and the "
            "terms, then works the book's illustration of load sensitivity in the lab."
        ),
        "body": [
            ("p", "&ldquo;any advice about performance should not be treated as fact until "
                  "it's measured on your configuration.&rdquo; Fowler gives that as the reason "
                  "performance is hard to write about, early in the Introduction's section "
                  "Thinking About Performance, and the rest of the book holds itself to it. "
                  "This lesson reads the first half of the section, the caution and the terms. "
                  "Read it in your own copy first."),
            ("p", "The caution comes first. Many architectural decisions are about "
                  "performance, Fowler says, and for most performance problems he would rather "
                  "get the system running, instrument it and optimise by measurement. Some "
                  "architectural decisions are hard to fix later, though, and people worry "
                  "about them early whether or not they can be fixed. So he gives a few "
                  "guidelines, minimising remote calls among them, and asks you to verify each "
                  "one on your application, to measure before and after every optimisation, "
                  "and to redo the work when the configuration changes: a new virtual machine, "
                  "database or piece of hardware can turn an old optimisation into a cost. He "
                  "has seen designs adopted or rejected on performance grounds that fell "
                  "apart once someone measured the system as it was really set up."),
            ("p", "Then the terms, in his order. Response time is the time to process a request "
                  "from outside. Responsiveness is how quickly the request is acknowledged; if "
                  "the system says nothing until it is done, the two are the same. Latency is "
                  "the minimum time for any response at all, and Fowler makes the point with a "
                  "program asked to do nothing and report when it has finished: on his laptop "
                  "the answer is instant, on a remote machine it may take seconds, and that "
                  "wait is why remote calls should be few. Throughput is how much is done in a "
                  "given time; transactions a second is the usual measure, though it depends "
                  "on the transaction, so he advises picking a common set of them. By "
                  "performance he means whichever of throughput and response time counts for "
                  "more in your case, and he prefers to name the one meant."),
            ("p", "Load is how much stress the system is under, for example how many users "
                  "are connected, and it is usually the context of another figure: a response "
                  "time is at some load. Load sensitivity is how the response time varies with "
                  "the load. Fowler's illustration is two systems. System A answers in 0.5 "
                  "seconds from 10 users through 20; system B answers in 0.2 seconds at 10 "
                  "users and 2 seconds at 20. A is the less load sensitive; B, he says, "
                  "degrades more. The figures are the book's illustration, not a measurement "
                  "of any real system."),
            ("code", _lines(RESPONSE_TIME)),
            ("p", "The snippet, written for the lesson, is the measurement all of this rests "
                  "on: it reads the clock, handles one request and returns the elapsed "
                  "milliseconds. `System.nanoTime()` is a clock for intervals, not the time of "
                  "day, and the division by `1000000` turns nanoseconds into milliseconds. Its "
                  "comment is the point Fowler makes: a figure from it is a response time at "
                  "the load the system was under when it ran, and means nothing without that "
                  "load beside it."),
            ("p", "The lab takes measurements as records `system, users, ms`. The preset "
                  "<code>system-a-and-b</code> enters the book's illustration in milliseconds "
                  "and asks for 15 users. Its first tile is the change in response time a "
                  "user, the rise from the first measurement to the last over the rise in "
                  "users: a 0 ms a user; b 180 ms a user, since B rises 1,800 ms over 10 users. "
                  "The second is the ratio of the last response time to the first: a 1×; b "
                  "10×. The third reads each system at 15 users on a straight line between its "
                  "two measurements: a 500 ms; b 1,100 ms. That line is the lab's assumption, "
                  "not the book's; Fowler gives only the two ends, and the banner says so."),
            ("p", "The preset <code>at-ten-users</code> reads the same measurements at 10 "
                  "users: a 500 ms; b 200 ms. At 10 users B is the faster system; at 15, on the "
                  "lab's line, A is, by 600 ms. On that line the two meet a little below 12 "
                  "users, where 200 + 180 a user for each user over 10 reaches 500. So neither "
                  "system is faster; each is faster at some load, and the one figure that "
                  "decides between them is the load you expect. That is why Fowler keeps "
                  "response time and load sensitivity apart."),
            ("h3", "Exercise"),
            ("ul", [
                "System north: 400 ms at 5 users, and 1,400 ms at 25 users.",
                "System south: 900 ms at 5 users, and 1,000 ms at 25 users.",
            ]),
            ("p", "By hand, find each system's change in response time a user and its ratio "
                  "of last to first, then read each at 20 users on a straight line between its "
                  "measurements, saying that the figure is interpolated. Say which system is "
                  "faster at 20 users and which at 5. Check your figures in the lab afterwards "
                  "by typing the records `north, 5, 400; north, 25, 1400; south, 5, 900; south, "
                  "25, 1000`."),
            ("p", "Load sensitivity is one of several words Fowler says are used loosely; "
                  "scalability is the worst. The next lesson, Capacity and Scalability, reads "
                  "the rest of the section and his Swordfish and Camel."),
        ],
        "lab": ("eakit", {
            "mode": "perf",
            "view": "load",
            "points": _A_AND_B,
            "preset": "system-a-and-b",
            "presets": [
                {"id": "system-a-and-b",
                 "label": "Systems A and B, read at 15 users (the book's illustration)",
                 "users": "15",
                 "expect": {"pzPerUser": "a 0 ms a user; b 180 ms a user",
                            "pzRatio": "a 1×; b 10×",
                            "pzAt": "a 500 ms; b 1,100 ms"}},
                {"id": "at-ten-users",
                 "label": "The same systems, read at 10 users",
                 "users": "10",
                 "expect": {"pzPerUser": "a 0 ms a user; b 180 ms a user",
                            "pzRatio": "a 1×; b 10×",
                            "pzAt": "a 500 ms; b 200 ms"}},
            ],
            "panel_title": "Load sensitivity from two measurements",
            "panel_intro": (
                "Each record is one measurement: a system, a number of users and a response "
                "time in milliseconds. The lab computes each system's change a user, its "
                "ratio of last to first, and a reading at the load you give on a straight "
                "line between measurements."
            ),
            "source": (
                "systems A and B are the book's illustration in the Introduction, Thinking "
                "About Performance, given in ms; the load to read them at is the lesson's"
            ),
        }),
        "steps_title": "Reading load sensitivity",
        "steps_intro": "Four steps, the last of them on a figure of your own.",
        "steps": [
            ("Sort each system's measurements",
             "Group the measurements by system and put each group in order of load, fewest "
             "users first."),
            ("Compute the change and the ratio",
             "For each system, divide the rise in response time by the rise in users for the "
             "change a user, and divide the last response time by the first for the ratio."),
            ("Read between measurements, and say so",
             "For a load between two measurements, take the lower one's time and add the "
             "change a user for each user above it. Write that the figure is interpolated, "
             "and never extend the line past the last measurement."),
            ("Do it on a figure of your own",
             "Take one response time you have measured and the load you measured it at. "
             "Write which of Fowler's terms the figure is, and the load at which you have no "
             "figure at all."),
        ],
        "worked": {
            "title": "How much system B degrades",
            "intro": [
                "Take the preset <code>system-a-and-b</code>: B answers in 200 ms at 10 users "
                "and 2,000 ms at 20; A in 500 ms at both. The figures below are in "
                "milliseconds.",
            ],
            "lines": [
                "B rises 2000 - 200, which is 1800",
                "over 20 - 10, which is 10 users",
                "change a user: 1800 / 10 is 180",
                "ratio: 2000 / 200 is 10 times",
                "A: 0 a user, and 500 / 500 is 1",
                "B at 15 users: 200 + 5 * 180 is 1100",
            ],
            "after": [
                "B's figures are the book's; the 1,100 ms at 15 users is the lab's straight "
                "line, which no one measured. A real system B might be well above or below it, "
                "and Fowler's advice is to measure at the load you care about.",
            ],
        },
        "quiz_title": "The terms of performance",
        "quiz": [
            {"q": "Work the exercise: north 400 ms at 5 users and 1,400 ms at 25; south 900 "
                  "ms at 5 and 1,000 ms at 25. On a straight line between the measurements, "
                  "what is each at 20 users, and which is faster there?",
             "a": ["north 1,150 ms, south 975 ms: south is faster at 20 users",
                   "north 1,400 ms, south 1,000 ms: south is faster at 20 users",
                   "north 900 ms, south 950 ms: north is faster at 20 users",
                   "north 1,150 ms, south 975 ms: north is faster at 20 users"],
             "c": 0,
             "why": "North rises 1,000 ms over 20 users, 50 ms a user, a ratio of 1,400/400 = "
                    "3.5×; at 20 users it is 400 + 15 × 50 = 1,150 ms. South rises 100 ms over "
                    "20 users, 5 ms a user, a ratio of 1,000/900 ≈ 1.1×; at 20 it is 900 + 15 "
                    "× 5 = 975 ms. South is faster at 20 users and north at 5. Both figures at "
                    "20 are interpolated. The 1,400 and 1,000 are the 25-user measurements, "
                    "and 900 and 950 are the readings at 15 users."},
            {"q": "Which of Fowler's terms names how quickly a system acknowledges a "
                  "request, as opposed to processing it?",
             "a": ["Response time", "Latency", "Responsiveness", "Throughput"],
             "c": 2,
             "why": "Responsiveness is about acknowledging a request; response time is the "
                    "time to process it. A progress bar improves the first and leaves the "
                    "second alone. Latency is the least time any response takes, and "
                    "throughput how much is done in a given time."},
            {"q": "On the book's illustration (A: 500 ms from 10 to 20 users; B: 200 ms at "
                  "10 users, 2,000 ms at 20), which statement is true, reading between the "
                  "measurements on a straight line?",
             "a": ["B is faster at every load from 10 to 20 users, because it is faster at 10",
                   "A is faster at every load from 10 to 20 users, because it degrades less",
                   "B is faster at 10 users and A is faster at 15",
                   "The two are equally fast at 15 users"],
             "c": 2,
             "why": "At 10 users B answers in 200 ms against A's 500. At 15 the line gives B "
                    "1,100 ms against A's 500. The two meet a little below 12 users. Lower at "
                    "one load does not mean lower at every load, which is why Fowler "
                    "separates response time from load sensitivity."},
            {"q": "What does Fowler say a significant change of configuration, such as a new "
                  "virtual machine or database, does to what you know about performance?",
             "a": ["Nothing, if the optimisations were measured when they were made",
                   "It may invalidate it, so the optimisations must be redone and checked",
                   "It improves it, since newer versions are faster",
                   "It affects throughput but never response time"],
             "c": 1,
             "why": "His corollary is that a significant change of configuration may "
                    "invalidate any facts about performance: you redo the optimisations and "
                    "check they still help, and an old one may now hurt."},
        ],
        "mistakes": [
            ("Thinking the faster system at one load is faster at every load",
             "On this view the system with the lower response time at one load is the "
             "faster system. Fowler's illustration says otherwise: B answers sooner at 10 "
             "users and degrades so much that A answers sooner from about 12 users up. Which "
             "is better depends on the load, which is why he separates response time from "
             "load sensitivity. On the book's figures, read on the lab's line, B is 300 ms "
             "faster at 10 users and 600 ms slower at 15."),
            ("Treating responsiveness and response time as one thing",
             "Fowler distinguishes them. A system that shows a progress bar at once is "
             "responsive while its response time is long, and he notes that users can be "
             "frustrated by a system with low responsiveness even when its response time is "
             "good. Only when the system says nothing until it has finished are the two the "
             "same."),
            ("Taking a performance tip as a fact",
             "The section's first rule is that advice about performance is not a fact until "
             "it is measured on your configuration, and that includes the book's own advice "
             "and the lab's. The lab's straight line between two measurements is an "
             "assumption; a real system can bend anywhere between them. Measure at the load "
             "you care about, before and after any change."),
        ],
        "standard": (
            "Finish when you can compute load sensitivity from two measurements and say which system is faster at which load.",
            "Given response times at two loads for two systems, compute each system's change "
            "a user and its ratio, and the response time between them by straight-line "
            "interpolation, stating that it is interpolation."
        ),
        "note": (
            "The lab does arithmetic on the measurements you type; it measures nothing, and "
            "its reading between two measurements is a straight line that no real system is "
            "obliged to follow. Fowler's illustration has no units of cost or hardware "
            "attached, and a figure from your own system means something only with its load "
            "and its configuration beside it."
        ),
    },
    # ---------------------------------------------------------------- 1.3
    # Introduction, Thinking About Performance, second half (PDF p. 28 of the
    # operator's copy).
    # Quote: PDF p. 28 of the operator's copy, 12 words, ea_quotes.py OK.
    # Lesson total: 12 words.
    # F4, PDF p. 28 of the operator's copy: 30 tps on two CPUs against 40 on four.
    # F5, PDF p. 28 of the operator's copy: Swordfish 20 and Camel 40 tps on one
    # server, 35 and 50 on two, then 15 and 10 a server; Camel more efficient
    # below five servers.
    {
        "slug": "capacity-and-scalability",
        "title": "Capacity and Scalability",
        "module": "Introduction",
        "one_line": "Efficiency, capacity and scalability are three different things, and Fowler's Swordfish and Camel show that the system with more capacity need not scale better.",
        "summary": (
            "The second half of the Introduction's section Thinking About Performance: "
            "efficiency, capacity, and scalability up and out, with Fowler's Swordfish and "
            "Camel and his case for building for hardware scalability. Project two systems' "
            "throughput from the book's figures, find where they cross, and count the "
            "servers a target needs."
        ),
        "key": [
            "efficiency: performance / resources",
            "capacity: the most effective throughput",
            "scalability: what more hardware adds",
            "up: a bigger server; out: more servers",
            "gain: rise in tps / servers added",
            "at n: last tps + gain * (n - last n)",
        ],
        "key_label": "Thinking About Performance, second half",
        "concepts_intro": (
            "Fowler's point is that these three are different, and that a design decision "
            "can improve one while it worsens another."
        ),
        "concepts": [
            ("Efficiency",
             "Performance divided by resources. In the book's example 30 transactions a "
             "second on two CPUs is more efficient than 40 on four identical CPUs: 15 a CPU "
             "against 10."),
            ("Capacity",
             "The most effective throughput or load the system can take, either an absolute "
             "maximum or the point at which performance falls below what is acceptable."),
            ("Scalability, vertical and horizontal",
             "How adding resources, usually hardware, changes performance. A scalable system "
             "gives a commensurate gain, such as twice the throughput for twice the servers. "
             "Vertical scalability, scaling up, adds power to one server; horizontal "
             "scalability, scaling out, adds servers."),
        ],
        "read_title": "The section's terms first, then the projection",
        "read_intro": (
            "Read the rest of the Introduction's section Thinking About Performance, from "
            "efficiency to the end, in your own copy first. The lesson sets out the terms and "
            "Fowler's argument, then projects his Swordfish and Camel in the lab."
        ),
        "body": [
            ("p", "&ldquo;Scalability is a measure of how adding resources (usually hardware) "
                  "affects performance.&rdquo; That is Fowler's definition in the second half "
                  "of the Introduction's section Thinking About Performance, the term he "
                  "says is used in many different senses. This lesson reads the rest of the "
                  "section: efficiency, capacity, scalability, and the illustration he argues "
                  "from. Read it in your own copy first."),
            ("p", "The three terms come in order. Efficiency is performance divided by "
                  "resources, and Fowler's example is that 30 transactions a second on two CPUs "
                  "is more efficient than 40 on four identical CPUs. Capacity is the most "
                  "effective throughput or load, which may be an absolute maximum or the point "
                  "at which performance falls below an acceptable threshold. Scalability is "
                  "the measure of what more hardware adds, and a scalable system gives a "
                  "commensurate improvement, twice the servers for twice the throughput. "
                  "Scaling up, or vertical scalability, adds power to one server, such as more "
                  "memory; scaling out, or horizontal scalability, adds servers."),
            ("p", "Then the illustration. Two systems, Swordfish and Camel, run on one server: "
                  "Swordfish handles 20 transactions a second and Camel 40. Which performs "
                  "better, and which scales better? Fowler says the second question cannot be "
                  "answered from these figures, and the first only partly: Camel is the more "
                  "efficient on a single server. Add a server, and Swordfish handles 35 and "
                  "Camel 50. Keep adding, and Swordfish gains 15 a server and Camel 10. So "
                  "Swordfish has the better horizontal scalability, though Camel is the more "
                  "efficient below five servers. The figures are the book's illustration; "
                  "Fowler poses the two systems as a supposition, to make the point."),
            ("p", "His conclusion is practical. It often makes sense, he argues, to build for "
                  "hardware scalability rather than for capacity or even efficiency, because "
                  "scalability keeps more performance in reserve for when it is wanted, and "
                  "is often the easier thing to build. Designers do complicated things to raise "
                  "capacity on one platform when more hardware would be cheaper; if Camel cost "
                  "as much more as a couple of servers, Swordfish would be cheaper even at 40 "
                  "transactions a second. He admits that he grumbles too whenever he "
                  "must upgrade his laptop for the latest version of Word, and still holds that "
                  "hardware usually costs less than the programmers it would take to do "
                  "without it, as long as the system can make use of it."),
            ("code", _lines(SERVERS_NEEDED)),
            ("p", "The snippet, written for the lesson, is the count the lab's servers-needed "
                  "tile does: start with one server at its measured throughput, and add a "
                  "server and its gain until the target is met. The guard on lines 3 to 5 is "
                  "there because a system that gains nothing from another server, and has not "
                  "yet reached the target, would keep the loop on lines 8 to 11 running for "
                  "ever. Like the lab, the loop assumes that every server past the measured "
                  "ones adds the same amount."),
            ("p", "The lab takes measurements as records `system, servers, tps`. The preset "
                  "<code>swordfish-and-camel</code> enters the book's figures, a target of 40 "
                  "and a projection at 5 servers. The first tile is efficiency, throughput a "
                  "server at the first measurement: swordfish 20 a server; camel 40 a server. "
                  "The second is the gain a server between the measurements: swordfish 15; "
                  "camel 10. The third is where the two projections meet or cross: 5 servers "
                  "(both 80). The fourth is the fewest servers that reach the target: "
                  "swordfish 3; camel 1. The fifth projects each at 5 servers: swordfish 80; "
                  "camel 80. Past the last measurement the lab carries on at the measured "
                  "rate, which is the book's own assumption when it says what further servers "
                  "add, and nothing more."),
            ("p", "The preset <code>need-120</code> asks for 120 transactions a second and a "
                  "projection at 10 servers: swordfish 8; camel 9 servers needed, and at 10 "
                  "servers swordfish 155 against camel's 130. At 40 a second Camel needs one "
                  "server to Swordfish's three; at 120 the order has turned round. That is "
                  "Fowler's argument in two figures: the higher capacity on one server says "
                  "nothing about what the next servers add, and the system that wins depends "
                  "on how far you expect to grow."),
            ("h3", "Exercise"),
            ("ul", [
                "System heron: 30 tps on 1 server, and 54 tps on 3 servers.",
                "System stork: 45 tps on 1 server, and 57 tps on 3 servers.",
            ]),
            ("p", "Assume each carries on at its measured gain. By hand, find each system's "
                  "gain a server, the server count at which heron first matches or passes "
                  "stork, the servers each needs for 60 tps, and each one's throughput at 6 "
                  "servers. Then check your figures in the lab with the records `heron, 1, 30; "
                  "heron, 3, 54; stork, 1, 45; stork, 3, 57`."),
            ("p", "The Introduction ends here, and the narratives begin. The next lesson, "
                  "Layering, reads Chapter 1, the architecture the rest of the book is built "
                  "on."),
        ],
        "lab": ("eakit", {
            "mode": "perf",
            "view": "scale",
            "unit": "server",
            "points": _SWORDFISH_AND_CAMEL,
            "preset": "swordfish-and-camel",
            "presets": [
                {"id": "swordfish-and-camel",
                 "label": "Swordfish and Camel, 40 tps needed (the book's illustration)",
                 "need": "40",
                 "at": "5",
                 "expect": {"pzMarginal": "swordfish 15; camel 10",
                            "pzCrossover": "5 servers (both 80)",
                            "pzNeed": "swordfish 3; camel 1"}},
                {"id": "need-120",
                 "label": "The same two systems, 120 tps needed",
                 "need": "120",
                 "at": "10",
                 "expect": {"pzMarginal": "swordfish 15; camel 10",
                            "pzCrossover": "5 servers (both 80)",
                            "pzNeed": "swordfish 8; camel 9"}},
            ],
            "panel_title": "Throughput as servers are added",
            "panel_intro": (
                "Each record is one measurement: a system, a number of servers and its "
                "throughput in transactions a second. The lab computes each system's "
                "throughput a server, its gain a server, where two systems' projections meet, "
                "the servers a target needs, and a projection at the count you give."
            ),
            "source": (
                "Swordfish and Camel are the book's illustration in the Introduction, "
                "Thinking About Performance; the targets are the lesson's"
            ),
        }),
        "steps_title": "Projecting throughput",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Compute efficiency at the first measurement",
             "Divide each system's throughput at its first measurement by its servers. That "
             "is efficiency, throughput a unit of resource."),
            ("Compute the gain a server",
             "Divide the rise in throughput between the two measurements by the servers "
             "added. Say that you are assuming each further server adds the same."),
            ("Project, compare and count",
             "Add the gain once for each server past the last measurement. Find the first "
             "count at which the two systems are equal or change places, and the fewest "
             "servers that reach the target."),
            ("Do it on a system of your own",
             "Take the last time your team scaled a system, by hardware or by code. Write "
             "whether it was scaling up, scaling out, or a gain in efficiency instead, and "
             "the figure that justified it."),
        ],
        "worked": {
            "title": "Where Swordfish catches Camel",
            "intro": [
                "Take the preset <code>swordfish-and-camel</code>: Swordfish 20 then 35, Camel "
                "40 then 50, on one and two servers.",
            ],
            "lines": [
                "swordfish gains 35 - 20, which is 15",
                "camel gains 50 - 40, which is 10",
                "swordfish at n: 20 + 15 * (n - 1)",
                "camel at n: 40 + 10 * (n - 1)",
                "equal when 5 * (n - 1) is 20: n is 5",
                "both give 80 a second on 5 servers",
            ],
            "after": [
                "Below five servers Camel is ahead, and above five Swordfish is. Both lines "
                "are the book's figures carried on at a constant gain, which is what Fowler "
                "assumes when he says what further servers add; a real system's gain usually "
                "changes as it grows, and only measuring shows how.",
            ],
        },
        "quiz_title": "Efficiency, capacity and scalability",
        "quiz": [
            {"q": "Work the exercise: heron 30 tps on 1 server and 54 on 3; stork 45 on 1 and "
                  "57 on 3, each carrying on at its measured gain. What does each gain a "
                  "server, and at what server count does heron first pass stork?",
             "a": ["heron 24, stork 12; at 3 servers",
                   "heron 12, stork 6; at 3 servers",
                   "heron 12, stork 6; at 4 servers",
                   "heron 12, stork 6; at 5 servers"],
             "c": 2,
             "why": "Heron rises 24 over 2 servers, 12 a server; stork rises 12 over 2, 6 a "
                    "server. At 3 servers heron has 54 and stork 57; at 4, heron 66 and stork "
                    "63, so heron passes at 4. Both need 4 servers for 60 tps (66 and 63; on 3 "
                    "they have 54 and 57). At 6 servers heron gives 90 and stork 75. Twenty-four "
                    "and twelve are the rises over two servers, not the gain a server."},
            {"q": "By Fowler's definition of efficiency, which is more efficient: 30 tps on "
                  "two CPUs, or 40 tps on four identical CPUs?",
             "a": ["40 tps on four CPUs, because its throughput is higher",
                   "30 tps on two CPUs: 15 a CPU against 10",
                   "They are equally efficient",
                   "40 tps on four CPUs: 10 a CPU against 15"],
             "c": 1,
             "why": "Efficiency is performance divided by resources: 30/2 = 15 a CPU against "
                    "40/4 = 10. This is the book's own example. The higher throughput is the "
                    "less efficient system."},
            {"q": "Carry the book's Swordfish (20, then 15 a server) and Camel (40, then 10 a "
                  "server) on at those gains. How many servers does each need for 120 tps?",
             "a": ["swordfish 8; camel 9",
                   "swordfish 7; camel 9",
                   "swordfish 8; camel 8",
                   "swordfish 7; camel 8"],
             "c": 0,
             "why": "Swordfish gives 20 + 15 × 6 = 110 on 7 servers and 125 on 8; Camel gives "
                    "40 + 10 × 7 = 110 on 8 and 120 on 9. Seven and eight are each one server "
                    "short."},
            {"q": "In Fowler's terms, which of these is scaling out?",
             "a": ["Adding memory to the one server the system runs on",
                   "Rewriting the code so that one server handles more",
                   "Adding more servers",
                   "Raising the system's capacity on its present server"],
             "c": 2,
             "why": "Scaling out, horizontal scalability, means adding servers. Adding power "
                    "to one server is scaling up. Rewriting the code changes efficiency or "
                    "capacity, not what more hardware adds."},
        ],
        "mistakes": [
            ("Thinking the system with more capacity scales better",
             "On this view, the system that does more on one server is the one to grow. "
             "Swordfish and Camel are Fowler's counterexample. On his figures Camel has twice "
             "the capacity on one server, 40 against 20, and Swordfish catches it at five "
             "servers, because it gains 15 a server to Camel's 10. Capacity says what one "
             "configuration does; scalability says what more hardware adds."),
            ("Taking efficiency for throughput",
             "Efficiency is throughput, or another measure of performance, divided by "
             "resources. In the book's example 30 tps on two CPUs, 15 a CPU, is more efficient "
             "than 40 tps on four, 10 a CPU, though 40 is the higher throughput. Camel is the "
             "more efficient on one server, and that alone does not make it the better "
             "choice."),
            ("Reading a projection as a measurement",
             "The lab, like the book's illustration, carries each system on at the gain "
             "between two measurements. That is an assumption: real systems can gain less "
             "with each server as they share a database or a network, and the crossover can "
             "move or vanish. The projection tells you what the two measurements imply, and "
             "the next measurement tells you whether it holds."),
        ],
        "standard": (
            "Finish when you can project two systems' throughput, find where they cross, and count the servers a target needs.",
            "Given two systems' throughput measured at two server counts and a constant gain "
            "a server between and after them, compute each one's gain, the crossover and the "
            "servers needed for a target."
        ),
        "note": (
            "The lab projects in straight lines from two measurements; it cannot know where a "
            "real system stops scaling, and it knows nothing of what a server or a "
            "programmer costs, which is where Fowler's argument ends. His figures are an "
            "illustration, and the decision he describes needs your own measurements and "
            "your own prices."
        ),
    },
    # ---------------------------------------------------------------- 1.4
    # Chapter 1, Layering (PDF pp. 33-38 of the operator's copy): benefits and
    # downsides p. 33; The Evolution of Layers in Enterprise Applications p. 34;
    # The Three Principal Layers pp. 35-36; Choosing Where to Run Your Layers
    # pp. 37-38.
    # Quote: PDF p. 36 of the operator's copy, 12 words, ea_quotes.py OK.
    # Lesson total: 12 words. Alan Knight's comment (p. 36) is paraphrased.
    # F6, PDF p. 36 of the operator's copy: sales up over 10 percent, coloured red.
    # F7, PDF p. 38 of the operator's copy: complexity boosters, after Jens
    # Coldewey, among them more than 100 transactions per second.
    # The course's one modern aside (PLAN section F.3) is the second-last p.
    {
        "slug": "layering",
        "title": "Layering",
        "module": "Chapter 1 · Layering",
        "one_line": "Presentation, domain and data source, with one rule about which way the dependencies run, and Fowler's test for logic that has leaked into the page.",
        "summary": (
            "Chapter 1: what layers buy and what they cost, how enterprise applications came "
            "to have three of them, what belongs in presentation, domain and data source, "
            "and where each layer should run. Find the domain logic in two presentations by "
            "the lines a second one forces you to copy, and move it into the domain."
        ),
        "key": [
            "presentation, domain, data source",
            "domain never depends on presentation",
            "test: add a second presentation",
            "what you copy is domain logic",
            "a layer is not a tier",
            "keep it in one process if you can",
        ],
        "key_label": "Chapter 1 in six lines",
        "concepts_intro": (
            "Chapter 1 uses three ideas that every later chapter assumes. The first is the "
            "distinction most often blurred."
        ),
        "concepts": [
            ("Layer and tier",
             "A layer is a logical division of the software; a tier usually means a physical "
             "one, a separate machine. Fowler uses layer to stress that the layers need not "
             "run on different machines: with a local database all three can run on one "
             "laptop and still be three layers."),
            ("The three principal layers",
             "Presentation handles the interaction with the user or another program: it "
             "displays information and turns commands into actions. Data source talks to "
             "the systems that do work for the application, above all the database. Domain "
             "logic, also called business logic, is the work the application exists to do."),
            ("The dependency rule",
             "The domain and data source never depend on the presentation: no call runs from "
             "them into presentation code. That makes it easy to put a different "
             "presentation on the same foundation and to change the presentation without "
             "consequences further down."),
        ],
        "read_title": "The chapter's argument first, then the copied lines",
        "read_intro": (
            "Read Chapter 1, Layering, in your own copy first, all five of its sections. The "
            "lesson sets out its argument in its own words, then counts the lines a second "
            "presentation forces you to copy."
        ),
        "body": [
            ("p", "&ldquo;The domain and data source should never be dependent on the "
                  "presentation.&rdquo; That is the one fixed rule in Chapter 1, Layering, in "
                  "its section The Three Principal Layers, and the rest of the book keeps it. "
                  "This lesson reads the whole chapter: what layers are for, how enterprise "
                  "applications came to have three, what belongs in each, and where each "
                  "should run. Read it in your own copy first."),
            ("p", "Fowler's case for layers starts outside enterprise software, with network "
                  "protocols: FTP on TCP on IP on ethernet. A higher layer uses the services of "
                  "the one below and the lower is unaware of the higher. The benefits he lists "
                  "follow: you can understand one layer without much knowledge of the others, "
                  "replace a layer with another that offers the same services, minimise the "
                  "dependencies between layers, standardise a layer, and build many higher "
                  "services on one lower one. The costs are two. Layers do not encapsulate "
                  "everything, so a new field that must be shown and stored ripples through "
                  "every layer between; and extra layers can harm performance, though a layer "
                  "that hides a function can also be optimised. The hardest part, he says, is "
                  "deciding what the layers are and what each is responsible for."),
            ("p", "The Evolution of Layers is a short history. Batch programs had none. The "
                  "client–server tools of the 1990s, VB, Powerbuilder and Delphi among them, "
                  "made two layers easy, with widgets that knew SQL, and worked well while the "
                  "job was showing and updating rows. Domain logic was the trouble: written into "
                  "the screens, it was awkward and easily duplicated, so a simple change meant "
                  "hunting through many screens; written as stored procedures, it was poorly "
                  "structured and tied to one vendor. The object community's answer was a "
                  "third layer for the domain, and it made little headway until the Web, when "
                  "every application whose logic lived in a rich client had to be rewritten to "
                  "get a browser front end, while a well-layered one needed only a new "
                  "presentation."),
            ("p", "The Three Principal Layers names them, after Brown and his colleagues: "
                  "presentation, domain and data source. Presentation is how the user, or a "
                  "program, interacts with the software; data source is the communication with "
                  "databases, messaging systems and other packages that do work for you; domain "
                  "is the work itself, calculation, validation and choosing which data source "
                  "logic to run. Fowler notes that the presentation often reads the data "
                  "source directly, which is less tidy and, in his experience, the better choice in practice. "
                  "He contrasts his scheme with Alistair Cockburn's Hexagonal Architecture, "
                  "which treats everything outside as one kind of interface, and keeps the "
                  "asymmetry because a service you offer and a service you use are different. "
                  "Separate the layers as the system needs, he advises, by subroutine, class "
                  "or package, but separate them."),
            ("p", "Then the test. People find it hard, he says, to tell domain logic from other "
                  "logic, and his informal check is to imagine adding a radically different "
                  "presentation, such as a command line to a Web application: whatever you "
                  "would have to duplicate is domain logic that has leaked into the "
                  "presentation. His example is a product list in which every product whose "
                  "sales rose by more than 10 percent on the month before was coloured red, "
                  "with the comparison done in the page. The domain should have a method that "
                  "says whether sales are improving; the page asks it and chooses how to "
                  "highlight. He will not be dogmatic about it: a reviewer, Alan Knight, "
                  "wondered whether the rule in the page began a slide into disorder or was a "
                  "sensible shortcut only a purist would mind, and Fowler's answer is that it "
                  "is both."),
            ("p", "Choosing Where to Run Your Layers turns to machines. Running everything on "
                  "servers is the simplest choice, because there is one place to upgrade and "
                  "fix; the case for the client is responsiveness or working while "
                  "disconnected. The data source runs on servers, the presentation wherever the "
                  "kind of interface puts it, and Fowler, writing in 2002, favours a Web front "
                  "end wherever it will serve and a rich client only where it must. Domain logic is best kept on the server; if a "
                  "little must run on the client too, isolate it in a module that depends on "
                  "nothing else. Keep the code in one process if you can, because separate "
                  "processes cost performance and complexity. The chapter ends with the "
                  "complexity boosters, Jens Coldewey's name for distribution, explicit "
                  "multithreading, paradigm chasms such as objects and tables, multiplatform "
                  "work and extreme performance requirements, which the book puts at more than "
                  "100 transactions a second. Each has a cost, in building and in maintenance."),
            ("code", _lines(RISING_TWICE)),
            ("p", "Here is the book's red-product rule in code written for the lesson: a Web "
                  "page and a command-line report, each deciding for itself whether sales "
                  "rose by more than 10 percent. `now * 100 > before * 110` is that test in "
                  "whole numbers. The lab finds identical lines, two or more in a row, after "
                  "collapsing white space. On the preset <code>rising-twice</code> it reports "
                  "1 repeated block, 6 lines in all the copies, and where: lines 3–5 and lines "
                  "11–13. Lines 6 and 14 differ, because each presentation shows the result "
                  "in its own way. The 10 percent rule is the book's illustration; the code is "
                  "the lesson's."),
            ("code", _lines(RISING_ONCE)),
            ("p", "The preset <code>rising-once</code> is the same two presentations after the "
                  "rule has moved into the domain as `isRising`. The lab reports 0 repeated "
                  "blocks, 0 lines, and where: none. The two presentations still differ, one "
                  "passes a flag to the page and the other appends a star, and that is the "
                  "split Fowler describes: the domain decides whether there is something to "
                  "highlight, and each presentation decides how. On the lesson's illustration "
                  "the copied lines are three, and the count is a way of finding them, not a "
                  "verdict on how bad they were."),
            ("p", "One later view belongs here. Much presentation is now built in the browser, "
                  "running as a program on the client and talking to the server through an "
                  "API, and some applications run domain rules on both sides so that a form "
                  "can answer at once. Those who build this way argue that the browser is now "
                  "a capable client that updates itself, which removes much of the deployment "
                  "cost that made Fowler favour the server. His chapter still frames the "
                  "choice: a rule that runs in both places is the split he says sounds like the "
                  "worst of both worlds, workable when it sits in a module that depends on "
                  "nothing else, and "
                  "an API is a second presentation, so his test applies to it."),
            ("h3", "Exercise"),
            ("code", _lines(OVERDUE_TWICE)),
            ("p", "Mark the lines that a second presentation has forced to be copied, counting "
                  "only identical lines at least two in a row, as the lab does. Then write the "
                  "domain method, on the class it belongs to, that both routines would call "
                  "instead. Paste the listing into the lab to check your marking."),
            ("p", "A domain that must call a mapper below it, without depending on it, needs a "
                  "small pattern. The next lesson, Layer Supertype and Separated Interface, "
                  "reads two base patterns from Chapter 18."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dupes",
            "min_run": 2,
            "preset": "rising-twice",
            "presets": [
                {"id": "rising-twice",
                 "label": "The sales rule in the page and in the command line",
                 "code": RISING_TWICE,
                 "expect": {"coDupBlocks": "1", "coDupLines": "6",
                            "coDupWhere": "lines 3–5 and lines 11–13"}},
                {"id": "rising-once",
                 "label": "The rule moved into the domain, and both presentations asking",
                 "code": RISING_ONCE,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
            ],
            "panel_title": "What a second presentation copies",
            "panel_intro": (
                "The lab finds lines that are identical after white space is collapsed, at "
                "least two in a row, and reports each repeated block and where its copies "
                "are. The 10 percent rule is the book's illustration; the listings are the "
                "lesson's."
            ),
        }),
        "steps_title": "Finding domain logic in a presentation",
        "steps_intro": "Four steps, the last of them on a screen you know.",
        "steps": [
            ("Imagine the second presentation",
             "Take a screen and imagine offering the same data another way: a command line, "
             "a report, an API. Write the second presentation, or sketch it."),
            ("Mark what you had to copy",
             "Mark every line the second presentation repeats from the first. Those lines are "
             "domain logic that has leaked into the presentation."),
            ("Move the rule into the domain",
             "Write one domain method that does what the copied lines did and returns the "
             "answer. Each presentation calls it and keeps only how the answer is shown."),
            ("Do it on a screen you know",
             "Take one screen in a system you know. List each line of it that would be "
             "repeated if the same data were offered through an API, and count them."),
        ],
        "worked": {
            "title": "Three lines in two copies",
            "intro": [
                "Compare the two routines of the preset <code>rising-twice</code> line by line.",
            ],
            "lines": [
                "line 3 matches line 11: before",
                "line 4 matches line 12: now",
                "line 5 matches line 13: rising",
                "lines 6 and 14 differ",
                "one block of 3 lines, in 2 copies",
                "lines in all the copies: 3 * 2 is 6",
            ],
            "after": [
                "The block that repeats is exactly the rule Fowler says belongs in the domain; "
                "the lines that differ are what each presentation does with the answer. That "
                "is his test made visible: the copy marks the leak.",
            ],
        },
        "quiz_title": "Layers and the rule between them",
        "quiz": [
            {"q": "Mark the exercise as the lab does, counting identical lines at least two "
                  "in a row. Which lines repeat, and where does the rule they hold belong?",
             "a": ["lines 3–5 and 10–12; in a method on the report screen",
                   "lines 3–4 and 10–11; in a method boolean isOverdue() on Invoice",
                   "lines 4 and 11 only; in a method boolean isOverdue() on Invoice",
                   "none: the two routines write to different outputs"],
             "c": 1,
             "why": "Lines 3–4 and 10–11 are identical: one block of 2 lines in 2 copies, 4 "
                    "lines in all. Lines 5 and 12 differ, because one writes to the page and "
                    "the other to the file, so the block stops at 4 and 11; and line 3 matches "
                    "line 10, so the block starts there. The rule, more than 30 days open and "
                    "not disputed, becomes `boolean isOverdue()` on `Invoice`, in the domain, "
                    "and both routines call it."},
            {"q": "Fowler runs all three layers on one laptop with a local database. How many "
                  "layers is that, and on how many machines?",
             "a": ["Three layers on one machine",
                   "One layer, since it is one machine",
                   "Three layers, so three tiers and three machines",
                   "Two layers, since the database is local"],
             "c": 0,
             "why": "A layer is a logical division and a tier usually a physical one. Fowler "
                    "says plainly that with a local database he can run all three layers on a "
                    "single laptop, and they are still three distinct layers."},
            {"q": "Which dependency does Chapter 1's rule forbid?",
             "a": ["The presentation reading the data source directly",
                   "The presentation calling the domain",
                   "The domain calling the presentation",
                   "The domain calling the data source"],
             "c": 2,
             "why": "The rule is that the domain and data source never depend on the "
                    "presentation. Fowler says the presentation often reads the data source "
                    "directly, less tidy but, he finds, better in practice; the presentation calling the "
                    "domain is the normal direction; and the domain's relation to the data "
                    "source depends on the data-source patterns chosen."},
            {"q": "Which of these is among the complexity boosters that close Chapter 1, in "
                  "Jens Coldewey's phrase?",
             "a": ["Layering", "Explicit multithreading", "A Web presentation",
                   "A command-line interface"],
             "c": 1,
             "why": "The boosters are distribution, explicit multithreading, paradigm chasms "
                    "such as objects against tables, multiplatform development and extreme "
                    "performance requirements, more than 100 transactions a second in the "
                    "book. Layering is the chapter's recommendation, and a Web presentation "
                    "Fowler's preferred one."},
        ],
        "mistakes": [
            ("Thinking layers are tiers, so three layers need three machines",
             "Fowler separates the logical layers from where they run. Choosing Where to Run "
             "Your Layers is a separate decision, and its advice is to keep the code in one "
             "process where you can. The separation is worth having on one machine, because "
             "what it buys, understanding and replacing one layer without the others, has "
             "nothing to do with the hardware."),
            ("Thinking the rule is harmless in the page while there is one page",
             "Fowler's test is to imagine a second presentation, such as a command line: "
             "everything it would duplicate is domain logic. On the lesson's illustration "
             "that is three lines, copied into the second routine, and a change to the 10 "
             "percent would have to be made twice. Fowler does not call the first copy a "
             "disaster; with Alan Knight he finds it both sensible and the start of a slide, and "
             "the test tells you which side you are on."),
            ("Thinking the presentation must never touch the data source",
             "The chapter's rule runs the other way: the domain and data source must not "
             "depend on the presentation. Fowler says the presentation more often reads the "
             "data source directly than not, which is less tidy and, he finds, works better in "
             "practice. A layered design forbids calls into the presentation, not every call "
             "that skips a layer."),
        ],
        "standard": (
            "Finish when you can find domain logic in a presentation by what a second presentation would copy.",
            "Given two presentations of the same data, mark the lines that are domain logic "
            "and write the domain method that replaces them."
        ),
        "note": (
            "The lab finds identical lines; a rule copied with a variable renamed, or written "
            "a second way, is not found, and a line repeated by chance is. Fowler's test is "
            "about meaning, not text: whatever a second presentation would make you "
            "duplicate, in any form, is domain logic. The count is a quick way to see the "
            "plainest case."
        ),
    },
    # ---------------------------------------------------------------- 1.5
    # Chapter 18, Base Patterns: Layer Supertype (PDF p. 420 of the operator's
    # copy) and Separated Interface (pp. 421-423).
    # Quote: PDF p. 421 of the operator's copy, 15 words, ea_quotes.py OK.
    # Lesson total: 15 words. No figure from the book.
    {
        "slug": "layer-supertype-and-separated-interface",
        "title": "Layer Supertype and Separated Interface",
        "module": "Chapter 18 · Base Patterns",
        "one_line": "Two small base patterns: a superclass for what every object in a layer shares, and an interface in one package implemented in another, so a dependency can be reversed.",
        "summary": (
            "Two base patterns from Chapter 18 that layering needs: Layer Supertype, a "
            "superclass for every object in a layer, and Separated Interface, an interface "
            "defined in one package and implemented in another. Count what a change to the "
            "database library reaches before and after the domain stops depending on its "
            "mapper."
        ),
        "key": [
            "supertype: what every object in a layer shares",
            "interface here, implementation there",
            "the implementation depends on the interface",
            "use it to break a dependency",
            "something else wires the two together",
            "reached: dependents, theirs, and so on",
        ],
        "key_label": "Two base patterns in six lines",
        "concepts_intro": (
            "Both patterns are short, and both are read as tools to look up. Three ideas "
            "carry them."
        ),
        "concepts": [
            ("Layer Supertype",
             "A superclass for all the objects in one layer, holding what they all share and "
             "would otherwise duplicate. Fowler's example is the handling of an object's ID "
             "in a superclass of every domain object. A layer with more than one kind of "
             "object can have more than one."),
            ("Separated Interface",
             "An interface defined in one package and implemented in another. Because an "
             "implementation depends on its interface and not the other way round, the "
             "package that uses the interface knows nothing of the implementation."),
            ("The direction of a dependency",
             "Which package must be compiled, read and changed with which. A change to a "
             "package can reach every package that depends on it, directly or through "
             "others; reversing one dependency can put a whole layer out of reach."),
        ],
        "read_title": "The two patterns first, then the ripple",
        "read_intro": (
            "Read Chapter 18's Layer Supertype and Separated Interface in your own copy "
            "first. The lesson sets out each pattern in its own words, then follows a change "
            "to a database library through two designs."
        ),
        "body": [
            ("p", "&ldquo;use Separated Interface to define an interface in one package but "
                  "implement it in another.&rdquo; Fowler's advice comes at the opening of the "
                  "pattern, for the moment when one package must call another that the design "
                  "says it may not depend on. This lesson reads it, with the pattern before it "
                  "in Chapter 18, Layer Supertype. They are base patterns, more general than "
                  "the rest, and the narratives lean on both. Read them in your own copy first."),
            ("p", "Layer Supertype is, as Fowler says, a small idea and so a short pattern. "
                  "When every object in a layer needs the same methods, put "
                  "them in a superclass for the layer: a domain object superclass for every "
                  "domain object, holding the storage and handling of its ID, say, and a mapper "
                  "superclass for every mapper, which can rely on the domain one. A layer with "
                  "more than one kind of object may want more than one supertype. When to Use "
                  "It is one line: when the objects in a layer have common features, and "
                  "Fowler says he often does it without thinking."),
            ("p", "Separated Interface begins with packages. You improve a design by reducing "
                  "the coupling between its parts, and a good way to do that is to group "
                  "classes into packages and control which may depend on which, as Chapter 1's "
                  "rule does for the presentation. Sometimes a class must call something the "
                  "rules put out of its reach. Then define an interface in the calling "
                  "package and implement it in the other. It works because an implementation "
                  "depends on its interface and not the reverse, so the caller sees only the "
                  "interface, and the implementation's package now depends on the caller's."),
            ("p", "How It Works settles three questions. Where does the interface go? In the "
                  "client's package if there is one client package, so that the client's "
                  "developers define what they need; in a third package if there are several "
                  "clients, or if the implementers own the definition. What kind of interface? "
                  "Java's `interface` is the obvious choice, though an abstract class can carry "
                  "optional common behaviour. Who creates the implementation, since the "
                  "client may not know its class? A factory, itself behind a Separated "
                  "Interface and bound by Plugin, a pattern Course 7 reads; or, more simply, a "
                  "package that knows both and wires them together when the application "
                  "starts."),
            ("p", "When to Use It gives the occasions: a framework that must call application "
                  "code, a layer that must call one it should not see, such as domain code "
                  "calling a Data Mapper, and code that must call another team's work without "
                  "depending on its API. Fowler also says when not to bother. Some developers "
                  "write a separate interface for every class, which he thinks excessive; for "
                  "applications he recommends one only to break a dependency or to allow "
                  "several independent implementations, and notes that separating them later "
                  "is a simple refactoring. Enforcing dependency rules strictly, by a check at "
                  "build time, is less needed in a small system and, he says, well worth the "
                  "discipline in a big one."),
            ("code", _lines(SEPARATED_FINDER)),
            ("p", "The snippet, written for the lesson, is the domain calling a mapper without "
                  "depending on it. `OrderFinder`, lines 2–4, is the interface, in the domain "
                  "package. `Order`, lines 7–11, holds only an `OrderFinder` and loads through "
                  "it. `OrderMapper`, lines 14–19, is in the mapper package, knows the SQL, "
                  "and implements the interface, so the dependency runs from the mapper to "
                  "the domain. Something must still call `Order.setFinder` with a mapper when "
                  "the application starts: Fowler's simpler alternative, a package that knows "
                  "both. The static field is the lesson's shortcut, chosen to keep the listing "
                  "short."),
            ("p", "The lab reads dependencies as records `dependent, dependency` and a class "
                  "that changes, and prints two tiles: the classes that depend on it directly, "
                  "and every class the change reaches, following dependents of dependents. It "
                  "never lists the changed class itself. On the preset "
                  "<code>mapper-in-domain</code>, `order` uses `mapper` and `mapper` uses "
                  "`order`, the cycle a domain that calls its mapper makes, and `jdbc` "
                  "changes: depend on it directly, 1: mapper; reached in all, 3: mapper, "
                  "order, screen. The lab follows the cycle without going round it twice."),
            ("p", "On the preset <code>separated</code>, `order` uses `finder`, the interface "
                  "in its own package, `mapper` uses `finder` and `order`, and `main` uses "
                  "`mapper` to wire it. The same change to `jdbc` gives 1: mapper directly and "
                  "2: main, mapper in all. No domain class is reached. The count does not say "
                  "the second design is better; it says what the stated dependencies let a "
                  "database change touch, and in the second they stop at the mapper and the "
                  "code that wires it."),
            ("h3", "Exercise"),
            ("ul", [
                "Dependencies: `report, invoice; invoice, pdfwriter; pdfwriter, fontlib`, "
                "written dependent first.",
                "The class that changes: `fontlib`.",
            ]),
            ("p", "List by hand what the change reaches, directly and in all. Then put a "
                  "Separated Interface where it would keep `invoice` out of reach: name the "
                  "interface and its package, rewrite the dependency it reverses, add the "
                  "class that wires the two, and list again what the change reaches. Check "
                  "both lists in the lab."),
            ("p", "The base is laid: the layers, the rule between them, and the means to keep "
                  "it. The next course, Organizing Domain Logic, opens with Transaction "
                  "Script, the first of three ways to build the middle layer."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "mapper-in-domain",
            "presets": [
                {"id": "mapper-in-domain",
                 "label": "The domain calls its mapper, and the mapper the domain",
                 "edges": "screen, order; order, mapper; mapper, order; mapper, jdbc",
                 "changed": "jdbc",
                 "expect": {"dgDirect": "1: mapper",
                            "dgAffected": "3: mapper, order, screen"}},
                {"id": "separated",
                 "label": "A Separated Interface: the domain uses a finder, main wires the mapper",
                 "edges": "screen, order; order, finder; mapper, finder; mapper, order; "
                          "mapper, jdbc; main, mapper",
                 "changed": "jdbc",
                 "expect": {"dgDirect": "1: mapper", "dgAffected": "2: main, mapper"}},
            ],
            "panel_title": "What a database change reaches",
            "panel_intro": (
                "Each record is one dependency, written dependent, dependency. Name the class "
                "that changes; the lab lists what depends on it directly and everything the "
                "change reaches. The designs are the lesson's."
            ),
        }),
        "steps_title": "Following a change, and reversing a dependency",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Write the dependencies down",
             "Write each dependency as a record, the class that depends first and the class "
             "it depends on second."),
            ("Follow the change backwards",
             "From the changed class, list every class that depends on it, then every class "
             "that depends on those, until no new class appears."),
            ("Reverse one edge with an interface",
             "Put an interface in the calling class's package, make the lower class "
             "implement it, and add the class that wires the implementation in at startup. "
             "Rewrite the records and follow the change again."),
            ("Do it on code of your own",
             "Take one place in your code where a domain class imports something from a "
             "lower layer. Draw the edge, write the interface that would reverse it, and "
             "count what a change below reaches before and after."),
        ],
        "worked": {
            "title": "A database change that stops at the mapper",
            "intro": [
                "Take the preset <code>separated</code> and follow a change to `jdbc` backwards.",
            ],
            "lines": [
                "jdbc is used by mapper: direct, 1",
                "mapper is used by main: reached",
                "main is used by nothing: stop",
                "order uses finder, never mapper",
                "reached in all: main, mapper, so 2",
            ],
            "after": [
                "Before the interface the same change reached `order` through the cycle and "
                "`screen` through `order`. The edge that was removed, `order` on `mapper`, is "
                "the one the pattern reverses: the mapper now depends on the domain, and the "
                "domain on nothing below it.",
            ],
        },
        "quiz_title": "Separated Interface and what a change reaches",
        "quiz": [
            {"q": "In the exercise, `fontlib` changes. What does it reach before the "
                  "interface, and what after an interface InvoiceRenderer in the invoice "
                  "package, implemented by pdfwriter and wired by main?",
             "a": ["before 1: pdfwriter; after 1: pdfwriter",
                   "before 4: fontlib, invoice, pdfwriter, report; after 3: fontlib, main, pdfwriter",
                   "before 3: invoice, pdfwriter, report; after 3: invoice, main, pdfwriter",
                   "before 3: invoice, pdfwriter, report; after 2: main, pdfwriter"],
             "c": 3,
             "why": "Before: `pdfwriter` depends on `fontlib` directly (1: pdfwriter), "
                    "`invoice` on `pdfwriter` and `report` on `invoice`, so 3: invoice, "
                    "pdfwriter, report. With `InvoiceRenderer` in the invoice package, the "
                    "edge `invoice, pdfwriter` becomes `pdfwriter, invoice`, and `main, "
                    "pdfwriter` wires it: the change reaches `pdfwriter` and `main`, 2: main, "
                    "pdfwriter, and neither `invoice` nor `report`. The changed class itself "
                    "is never in the list, and the direct dependents are only the first step."},
            {"q": "For application code, when does Separated Interface's When to Use It "
                  "recommend a separate interface?",
             "a": ["Only when there are already two implementations",
                   "To break a dependency, or to allow several independent implementations",
                   "For every class, so that any class can be replaced",
                   "Only in framework code, never in an application"],
             "c": 1,
             "why": "Fowler recommends a separate interface for applications only to break a "
                    "dependency or to have multiple independent implementations. He calls an "
                    "interface for every class excessive, and his first example of use is a "
                    "framework calling application code, but not the only one."},
            {"q": "Where does the pattern suggest putting the interface when all its clients "
                  "are in one package?",
             "a": ["In the implementation's package",
                   "In a third package, always",
                   "In the client's package",
                   "In the package that wires them together"],
             "c": 2,
             "why": "With one client package, Fowler says, the interface may as well "
                    "live with the client, whose developers define what they need. A "
                    "third package suits several clients, or implementers who own the "
                    "definition. In the implementation's package it would reverse nothing."},
        ],
        "mistakes": [
            ("Thinking an interface is worth having only with two implementations",
             "On this view an interface earns its place by being implemented more than once. "
             "Separated Interface usually has one implementation; its point is the direction "
             "of the dependency, which Fowler argues from packages and the rules between "
             "them, not from substitution. In the lesson's illustration one interface and one "
             "mapper take every domain class out of reach of a database change."),
            ("Thinking a Layer Supertype is a class that does everything",
             "A Layer Supertype holds only what every object in its layer shares, so that it "
             "is not repeated in each; Fowler's example is the handling of an ID. Behaviour "
             "only some objects need belongs in those objects, or in a second supertype for "
             "that kind of object, as the pattern allows."),
            ("Thinking a Separated Interface removes every dependency between the packages",
             "It reverses one. The implementation still depends on the interface and on the "
             "domain's classes: in the preset <code>separated</code>, `mapper` depends on "
             "`order`, so a change to `order` would reach the mapper. And something must "
             "still know both to wire them, `main` here, or a Plugin. What the pattern "
             "removes is the domain's dependency on the layer below."),
        ],
        "standard": (
            "Finish when you can list what a change reaches and redraw the design with a Separated Interface.",
            "Given dependencies with a cycle through the domain, redraw them with a Separated "
            "Interface and list what a change to the database layer reaches in each."
        ),
        "note": (
            "The lab follows the dependencies you state; it cannot find them in code, and it "
            "counts a dependency on one method the same as one on a whole class. It also "
            "assumes that every change ripples to every dependent, when a change behind an "
            "unchanged interface reaches none. Whether a dependency is worth reversing is "
            "Fowler's question of when to bother, which no count settles."
        ),
    },
]
