"""Statements, lessons 1-4 -- Chapters 14 to 17 of Code Complete, 2nd ed.

Straight-line code, conditionals, loops and the unusual control structures.
Every page is a printed page of the second edition (Microsoft Press, 2004);
the comment above each lesson gives its pages and the page of its opening
quotation, which was checked character for character against the text. The
Java snippets are written for these lessons; none is the book's. Each snippet
is one constant, used both by the lesson's code block and by the lab preset
that counts it, so the line numbers the prose names are the lab's.
"""

# ---------------------------------------------------------------- snippets

# Organizing Straight-Line Code. PLAN §D.4 <code>total-first</code>, <code>in-order</code>, <code>hidden</code>.
TOTAL_FIRST = """double shippingQuote(Parcel parcel) {
    double total = base + surcharge + insurance;
    double base = parcel.baseRate();
    double surcharge = parcel.fuelSurcharge();
    double insurance = parcel.insuranceFee();
    return total;
}"""

IN_ORDER = """double shippingQuote(Parcel parcel) {
    double base = parcel.baseRate();
    double surcharge = parcel.fuelSurcharge();
    double insurance = parcel.insuranceFee();
    double total = base + surcharge + insurance;
    return total;
}"""

# The exercise's listing and the <code>hidden</code> preset: one constant, one block.
HIDDEN = """void printQuote(Quote quote) {
    quote.loadRates();
    quote.addSurcharges();
    quote.addInsurance();
    quote.print();
}"""

# Using Conditionals: the lesson's chain (written for it) and the exercise.
CLASSIFY = """String classify(int status) {
    int hundreds = status / 100;
    if (hundreds == 5) {
        return "server error";
    } else if (hundreds == 4) {
        return "client error";
    } else if (hundreds == 3) {
        return "redirect";
    } else if (hundreds == 2) {
        return "success";
    }
    return "unexpected";
}"""

ROUTE = """void route(Request req) {
    String method = req.method();
    if (method.equals("GET")) {
        read(req);
    } else if (method.equals("POST")) {
        create(req);
    } else if (method.equals("PUT")) {
        replace(req);
    } else if (method.equals("DELETE")) {
        remove(req);
    }
}"""

# Controlling Loops: the lesson's off-by-one and the exercise's header.
HOURLY = """int[] hourly = new int[10];
for (int i = 0; i <= 10; i++) {
    hourly[i] = countVisits(i);
}"""

BY_THREES = """for (int i = 10; i > 0; i -= 3) {
    System.out.println(i);
}"""

# Unusual Control Structures: Fibonacci two ways, and the exercise
# (PLAN §D.4 refundAmount, nested).
FIB_RECURSIVE = """long fibonacci(int n) {
    if (n < 2) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}"""

FIB_LOOP = """long fibonacci(int n) {
    if (n < 2) {
        return n;
    }
    long older = 0;
    long newer = 1;
    for (int i = 2; i <= n; i++) {
        long next = older + newer;
        older = newer;
        newer = next;
    }
    return newer;
}"""

REFUND_NESTED = """double refundAmount(Order order) {
    double refund = 0.0;
    if (order.isPaid()) {
        if (order.daysSinceDelivery() <= 30) {
            refund = order.total();
        }
    }
    return refund;
}"""


def _lines(snippet):
    return snippet.split("\n")


LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapter 14, §§14.1-14.2, pp. 347-353. Opening quotation:
    # Key Points, p. 353 (10 words). The order-dependency guidelines,
    # pp. 348-350; the long-name remark, p. 349; comments as a fallback and
    # housekeeping variables, p. 350; the Principle of Proximity, top-to-bottom
    # reading and grouping, pp. 351-353. Data-flow anomaly names: §22.3.
    {
        "slug": "organizing-straight-line-code",
        "title": "Organizing Straight-Line Code",
        "module": "Chapter 14 · Straight-Line Code",
        "one_line": "When statements must run in a certain order, Chapter 14 asks you to make the order visible in the code itself: in names, in parameters, and only as a last resort in comments.",
        "summary": (
            "Chapter 14 is about code with no branches at all, and its one hard idea is "
            "the dependency: a statement that must come after another because it reads "
            "what the other wrote. Count the dependencies in a parcel quote with the lab, "
            "find the three values summed before they exist, and see why four calls that "
            "pass nothing show the lab no order at all."
        ),
        "key": [
            "order statements by their dependencies",
            "i → j: line j reads what line i wrote",
            "make the order visible in names and data",
            "pass the data, and the order shows",
            "no dependency: keep related lines together",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "Chapter 14 has two sections, one for statements whose order matters and one "
            "for statements whose order does not. Three ideas carry both."
        ),
        "concepts": [
            ("Order dependency",
             "One statement depends on another when it reads a value the other wrote, so "
             "it has to run after it. Straight-line code is correct only if every "
             "dependency points forward, from an earlier line to a later one."),
            ("Hidden dependency",
             "A dependency the code does not show. Calls that pass nothing and return "
             "nothing can still depend on each other through the data of the object they "
             "share, and neither the reader nor the compiler can see it."),
            ("The Principle of Proximity",
             "Keep related actions together. When the order of some statements does not "
             "matter, McConnell's rule for choosing one is to put the statements that work "
             "on the same data next to each other, so the code reads from top to bottom."),
        ],
        "read_title": "The chapter's argument first, then the parcel quote",
        "read_intro": (
            "The lesson sets out what Chapter 14 argues, section by section, and then "
            "counts the dependencies in three short listings with the lab."
        ),
        "body": [
            ("p", "<strong>Chapter 14, p. 353.</strong> &ldquo;The strongest principle for "
                  "organizing straight-line code is ordering dependencies.&rdquo; The "
                  "sentence is the first of the chapter's key points. Read Chapter 14, "
                  "pp. 347&ndash;353, in your own copy before going on; it is seven pages, "
                  "and the lesson follows it in order."),
            ("p", "You have probably met a routine that worked until someone tidied it: "
                  "two calls that looked independent were swapped, and a total came out "
                  "wrong, or zero. Chapter 14 is about that kind of code, statements with "
                  "no branches and no loops, run one after another, and its argument is "
                  "that the order of such statements is a fact about the program that "
                  "should be visible in the code, not something a reader has to know."),
            ("p", "Section 14.1 (p. 347) begins with statements whose order counts, and "
                  "McConnell's word for what makes it count is dependency: the second "
                  "statement needs what the first produced. Sometimes the routine names "
                  "make that plain, sometimes only knowledge of the domain does, and "
                  "sometimes it is hidden altogether, as in a run of calls that take no "
                  "parameters and work on data their class shares. His first guideline is "
                  "to organize the code so that dependencies are obvious: if one routine "
                  "quietly initializes data the others use, move the initialization into "
                  "a routine of its own whose name says it comes first. His second is to "
                  "name routines so that dependencies are obvious, even at the cost of a "
                  "long name. A name that lists everything a routine does is not the "
                  "trouble, he remarks; the routine that does all of it is."),
            ("p", "The third guideline is the one the lab can see. Pass the data between "
                  "the routines as parameters, and better still have each return what the "
                  "next one takes, and the order is written into the calls themselves "
                  "(pp. 349&ndash;350). Data can show the opposite too: routines that "
                  "share nothing announce that their order does not matter. Only when the "
                  "code itself cannot be improved does McConnell turn to comments that "
                  "document the dependency, and for critical code to status variables or "
                  "assertions that check it, a technique he weighs against the new "
                  "variables and new error checks it brings."),
            ("p", "Section 14.2 (p. 351) takes statements whose order does not matter. "
                  "There the guiding rule is the Principle of Proximity: keep related "
                  "actions together, so that the code reads from top to bottom and a "
                  "reader following one variable does not have to search the whole "
                  "routine. McConnell's test is to draw a box round each group of related "
                  "statements on a printed listing. Boxes that nest are fine; boxes that "
                  "overlap mean the code should be reorganized, and a group with no ties "
                  "to its neighbours may be a routine waiting to be extracted. The "
                  "measure behind it, how long a variable stays live, is the one Scope, "
                  "Span and Live Time counted."),
            ("p", "Now the code. The lab's <em>dataflow</em> view reads a Java listing top "
                  "to bottom and records, for every variable, the lines that set it and "
                  "the lines that read it; a parameter is set on the routine's first line. "
                  "From those it prints the <strong>dependencies (line → line)</strong>: a "
                  "pair i → j whenever line j reads a variable whose latest earlier set is "
                  "on line i. It also counts <strong>anomalies</strong>, the names of which "
                  "come from the data-flow testing of Section 22.3: a variable "
                  "<strong>used before set</strong>, one <strong>set twice</strong> with no "
                  "read between, and one <strong>set, never used</strong>. Here is the "
                  "lesson's parcel quote in the order a hurried writer might put it, the "
                  "<code>total-first</code> preset:"),
            ("code", {"lines": _lines(TOTAL_FIRST), "marked": [2]}),
            ("p", "The lab finds 6 anomalies. Line 2 reads `base`, `surcharge` and "
                  "`insurance` before anything has set them, so all three are used before "
                  "set at line 2, and each is then set on lines 3, 4 and 5 and never read "
                  "again, which is three more. Its dependencies are 1→3, 1→4, 1→5, 2→6: "
                  "lines 3 to 5 read the parameter `parcel`, and line 6 returns the "
                  "`total` that line 2 wrote. Nothing links line 2 to the three lines it "
                  "needs, because in this order they come after it. Here `javac` agrees "
                  "with the lab and refuses to compile the routine, with &ldquo;cannot find "
                  "symbol&rdquo; at line 2, and it can refuse because the names make the "
                  "dependency visible. Now the same statements in the order their "
                  "dependencies set, the <code>in-order</code> preset:"),
            ("code", _lines(IN_ORDER)),
            ("p", "Here the lab finds 0 anomalies, nothing set twice and nothing set but "
                  "never used, and the dependencies 1→2, 1→3, 1→4, 2→5, 3→5, 4→5, 5→6. "
                  "Every arrow points down the page, and that is what ordering "
                  "dependencies means in the count: no line reads anything a later line "
                  "writes. The third preset, <code>hidden</code>, is the listing in the "
                  "exercise below: four calls on one `Quote` object, each taking nothing "
                  "and returning nothing. The lab prints 1→2, 1→3, 1→4, 1→5, which says "
                  "only that every call reads the parameter `quote`, and 0 anomalies. The "
                  "routine compiles with its four calls in any order. Whatever "
                  "`loadRates` leaves inside the object for `addSurcharges` to use, the "
                  "lab cannot see it, and from this code you cannot either."),
            ("h3", "Exercise"),
            ("code", _lines(HIDDEN)),
            ("p", "Rewrite `printQuote` so that the order is in the parameters, as "
                  "Section 14.1 recommends: `loadRates` returns a `Rates`, which you keep "
                  "in a new local variable; `addSurcharges` and `addInsurance` each take "
                  "the `Rates` the call before returned and return a new one, kept in "
                  "its own variable; and `print` takes the last of them. Keep the routine "
                  "to five lines. Then list, by the lab's rule, every dependency i → j in "
                  "your version, and name the chain of arrows that now carries the "
                  "order. You can paste your version into the lab afterwards to check "
                  "the list."),
            ("p", "Statements in sequence are the simplest kind of control. The next "
                  "lesson, Using Conditionals, adds the first decision, and asks what the "
                  "order of a chain of tests costs."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dataflow",
            "preset": "total-first",
            "presets": [
                {"id": "total-first",
                 "label": "Total summed first (the lesson's parcel quote, out of order)",
                 "code": TOTAL_FIRST,
                 "expect": {"coAnomalies": "6", "coUsedBeforeSet": "base (line 2), surcharge (line 2), insurance (line 2)", "coDeps": "1→3, 1→4, 1→5, 2→6"}},
                {"id": "in-order",
                 "label": "The same statements in dependency order",
                 "code": IN_ORDER,
                 "expect": {"coAnomalies": "0", "coDeps": "1→2, 1→3, 1→4, 2→5, 3→5, 4→5, 5→6"}},
                {"id": "hidden",
                 "label": "Four calls that pass nothing (the exercise's listing)",
                 "code": HIDDEN,
                 "expect": {"coAnomalies": "0", "coDeps": "1→2, 1→3, 1→4, 1→5"}},
            ],
            "panel_title": "Which line reads what another wrote",
            "panel_intro": (
                "The lab records every set and read of every variable, line by line, and "
                "prints each dependency i → j where line j reads what line i last wrote. "
                "It reads variables only: what a call leaves inside an object is invisible "
                "to it, as it is to a reader of the code."
            ),
        }),
        "steps_title": "Finding the order a routine depends on",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("Mark what each line writes",
             "For every line, note the variable it sets, if any. A parameter is set on the "
             "routine's first line."),
            ("Mark what each line reads",
             "Note every variable each line uses on its right-hand side, in a condition or "
             "as an argument."),
            ("Draw the arrows",
             "For each variable a line reads, draw an arrow from the line that last set it. "
             "A read with no earlier set is a value used before it exists."),
            ("Look for an arrow that points up",
             "An arrow from a later line to an earlier one is an order the code gets "
             "wrong. A pair of calls with no arrow between them is either free to move or "
             "a dependency the code hides; decide which, and make it visible."),
            ("Do it on your own code",
             "Paste a routine of your own whose calls must run in a certain order into the "
             "lab, note the arrows it prints, and write one sentence naming the dependency "
             "that the arrows do not show and how you know it is there."),
        ],
        "worked": {
            "title": "Reading the arrows in the in-order listing",
            "intro": [
                "Take the in-order listing and find, for each line, the line whose value it "
                "reads.",
            ],
            "lines": [
                "line 1 sets parcel; lines 2, 3 and 4 read it",
                "line 2 sets base; line 5 reads it: 2→5",
                "lines 3 and 4 likewise: 3→5 and 4→5",
                "line 5 sets total; line 6 returns it: 5→6",
                "every arrow points down the page",
            ],
            "after": [
                "Line 5 depends on lines 2, 3 and 4, and on nothing else: it never reads "
                "`parcel` itself. That is the order Section 14.1 asks to see, and here the "
                "names alone show it.",
            ],
        },
        "quiz_title": "Dependencies in the parcel quote",
        "quiz": [
            {"q": "Line j depends on line i when it reads a variable whose latest earlier "
                  "set is on line i. In the in-order listing, which lines does line 5 "
                  "depend on?",
             "a": ["Lines 2, 3 and 4", "Lines 1, 2, 3 and 4", "Line 4 only", "Line 1 only"],
             "c": 0,
             "why": "Line 5 reads `base`, `surcharge` and `insurance`, set on lines 2, 3 "
                    "and 4. It does not read `parcel`, so there is no arrow 1→5; and it "
                    "reads three variables, not only the one set just before it."},
            {"q": "You rewrote `printQuote` so that `loadRates` returns a `Rates`, each of "
                  "the next two calls takes the previous call's result and returns a new "
                  "one, and `print` takes the last. By the same rule, which dependencies "
                  "does your version have?",
             "a": ["1→2, 1→3, 1→4, 1→5",
                   "1→2, 1→3, 1→4, 1→5, 2→3, 3→4, 4→5",
                   "2→3, 3→4, 4→5",
                   "1→2, 2→3, 3→4, 4→5"],
             "c": 1,
             "why": "The lab gives 1→2, 1→3, 1→4, 1→5, 2→3, 3→4, 4→5. Every call still "
                    "reads the parameter `quote`, set on line 1, so the four arrows from "
                    "line 1 stay; the new arrows 2→3, 3→4 and 4→5 are the chain that "
                    "carries the order, now in the parameters, which is Section 14.1's "
                    "remedy and the reason the lab can see it. The first option is the "
                    "routine before the rewrite."},
            {"q": "Which of the lesson's three listings does `javac` refuse to compile?",
             "a": ["None of them: all three are legal Java",
                   "<code>hidden</code>, because its calls pass nothing",
                   "<code>total-first</code>, because line 2 uses names not yet declared",
                   "<code>in-order</code>, because `total` is set and returned at once"],
             "c": 2,
             "why": "Line 2 of <code>total-first</code> names `base`, `surcharge` and `insurance` "
                    "before their declarations, and `javac` reports &ldquo;cannot find "
                    "symbol&rdquo;. The <code>hidden</code> routine compiles with its calls in any "
                    "order, which is exactly why its dependency is hidden, and <code>in-order</code> "
                    "is correct."},
            {"q": "For statements whose order does not matter, what does Section 14.2 "
                  "tell you to do?",
             "a": ["Order them by how often they run",
                   "Keep related statements together, so the code reads from top to bottom",
                   "Declare every variable at the top of the routine first",
                   "Sort them alphabetically by the variable they set"],
             "c": 1,
             "why": "The section's guiding rule is the Principle of Proximity, keeping "
                    "related actions together (p. 351). Ordering by frequency is Chapter "
                    "15's advice for chains of tests and `case` statements; alphabetical "
                    "order is one of its options for `case` labels of equal importance; "
                    "and declaring everything at the top is what Chapter 10 argues "
                    "against."},
        ],
        "mistakes": [
            ("Thinking that if the code compiles, its order is right",
             "The compiler sees the dependencies the names show and no others. It rejects "
             "<code>total-first</code>, because line 2 names three variables that do not "
             "yet exist, but it accepts the four calls of <code>hidden</code> in every one "
             "of their 24 orders, because they pass nothing. On the lesson's "
             "illustration the lab is in the same position: 1→2, 1→3, 1→4, 1→5 and no "
             "arrow between the calls. Section 14.1's argument is that the order should "
             "be put where both can see it, in names and in parameters."),
            ("Reaching for a comment first",
             "A comment saying which call must come first is McConnell's fallback, not his "
             "remedy. He asks you first to write code without order dependencies, second "
             "to write code that makes them obvious, and only then, if the code itself "
             "cannot be improved, to document them (p. 350)."),
            ("Treating a status flag as a free safety net",
             "A variable such as a flag set by the initializing routine and checked by "
             "the others can enforce a critical order, and the book offers it for code "
             "critical enough to need it. It also says what it costs: new variables, new "
             "initialization code and new error checks, each a new place for a mistake, "
             "to be weighed against the benefit."),
        ],
        "standard": (
            "Finish when you can list a routine's order dependencies and reorder it so none points backwards.",
            "For six statements, list each dependency as i → j, where line j reads what "
            "line i last wrote, and reorder the statements so that no dependency points "
            "backwards, by hand."
        ),
        "note": (
            "The lab reads variables and nothing else. A dependency carried by the fields "
            "of an object, a file or a database is invisible to it, which is the point of "
            "the <code>hidden</code> preset and the limit of the count. It reads the lines "
            "top to bottom and does not follow branches or loops, so for code that has "
            "them its arrows are an approximation. Whether a given order is the one the "
            "program needs is a question about the program, which the arrows only help "
            "you ask."
        ),
    },
    # ---------------------------------------------------------------- 02
    # McConnell Chapter 15, §§15.1-15.2, pp. 355-366. Opening quotation:
    # Key Points, p. 366 (21 words). Plain if statements, pp. 355-358; chains,
    # pp. 358-360 (most common first, all cases covered); case statements,
    # pp. 361-365 (ordering, phony variables, the default clause, falling
    # through). The frequencies are the lesson's illustration, not the book's.
    {
        "slug": "using-conditionals",
        "title": "Using Conditionals",
        "module": "Chapter 15 · Conditionals",
        "one_line": "The order of the tests in an if-else-if chain does not change its answer, but it changes what the chain costs and what a reader meets first, and the chain's last else is where the unexpected case should be caught.",
        "summary": (
            "Chapter 15 sets out how to write if statements, chains of them and case "
            "statements: the normal path first, the most common case first, and a final "
            "else or default that traps the cases nobody planned for. Compute how many "
            "tests a chain makes on average from the frequencies of its cases, see what "
            "reordering saves and where it saves nothing, and find the request a chain "
            "without a final else lets through."
        ),
        "key": [
            "write the normal path first",
            "put the most common case first",
            "expected tests: position × share, summed",
            "the last else catches what you missed",
            "reorder only exclusive tests",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "Chapter 15 is short and practical. Three ideas carry the lesson's arithmetic "
            "and its exercise."
        ),
        "concepts": [
            ("The nominal path",
             "The path through a routine that is normally taken. McConnell asks for it to "
             "be written first and to be easy to find, with the unusual and error cases "
             "after it rather than mixed through it."),
            ("Expected tests",
             "In an if-else-if chain the case tested first costs one test, the second "
             "two, and so on. Weight each case's cost by how often it occurs and divide "
             "by the total, and you have the average number of tests the chain makes."),
            ("The error trap",
             "A final else in a chain, or a default clause in a case statement, that "
             "catches every value no earlier branch handled and reports it, so that a "
             "case nobody planned for is noticed instead of passing silently."),
        ],
        "read_title": "The chapter's argument first, then the cost of a chain",
        "read_intro": (
            "The lesson goes through Chapter 15's two sections, then computes what a "
            "chain's order costs on an illustrative classifier, and ends with a router."
        ),
        "body": [
            ("p", "<strong>Chapter 15, p. 366.</strong> &ldquo;To trap errors, use the "
                  "default clause in a case statement or the last else in a chain of "
                  "if-then-else statements.&rdquo; It is one of the chapter's four key "
                  "points. Read Chapter 15, pp. 355&ndash;366, in your own copy first."),
            ("p", "Chapter 15 asks a plain question: given a decision, how should the "
                  "statement that makes it be laid out? Section 15.1 (p. 355) begins with "
                  "the plain `if`. Write the nominal path first and the unusual cases "
                  "after it. Branch correctly on equality, because writing `>` where `>=` "
                  "was meant is the conditional's own off-by-one error. Put the normal "
                  "case after the `if` rather than after the `else`; McConnell shows a "
                  "routine whose error cases sit sometimes in the `if` clause and "
                  "sometimes in the `else`, and the same routine rewritten so that the "
                  "normal path runs straight down and the errors collect at the bottom. "
                  "Do not leave an `if` clause empty in order to act in the `else`; negate "
                  "the test instead. Consider whether an `if` needs an `else`, test the "
                  "`else` too, and check that the two clauses have not been reversed."),
            ("p", "Chains of if-then-else tests get guidelines of their own "
                  "(pp. 358&ndash;360). Replace a complicated test with a call to a "
                  "well-named boolean function. Put the most common cases first, for two "
                  "reasons the chapter gives in this order: a reader finds the usual case "
                  "without wading through the exceptions, and the code makes fewer tests "
                  "to reach it. Make sure all cases are covered, with a final `else` that "
                  "reports the case you did not plan for in a message meant for the "
                  "programmer rather than the user. And where the language has a `case` "
                  "statement that fits, use it instead of the chain."),
            ("p", "Section 15.2 (p. 361) is the `case` statement. Order the cases "
                  "alphabetically or numerically when they matter equally, with the normal "
                  "case first when there is one, or by frequency. Keep each case's action "
                  "short, calling a routine when it is not. Do not invent a variable just "
                  "to be able to switch on it: the chapter's example switches on the first "
                  "letter of a typed command, and so accepts any word that begins with "
                  "the right letter. Use the default clause for a legitimate default or "
                  "to detect errors, never to hold the last real case. And in the "
                  "C family, Java included, every case must end explicitly, or control "
                  "drops into the next. Of a deliberate fall-through McConnell says it is "
                  "useful &ldquo;about as often as you find someone who would rather have "
                  "a used Pontiac Aztek than a new Corvette&rdquo; (p. 365), and where "
                  "one is written it must be commented."),
            ("p", "Now a chain to count. The lesson's classifier sorts HTTP status codes "
                  "into their classes by the hundreds digit. The four tests are mutually "
                  "exclusive, so any order gives the same answers, and the final `return` "
                  "is the error trap the quotation asks for:"),
            ("code", _lines(CLASSIFY)),
            ("p", "The lab's <em>chain</em> view takes the cases in the chain's order with "
                  "a frequency for each. Reaching the first condition costs one test, the "
                  "second two, and a final `else` costs as many tests as there are "
                  "conditions before it. It prints the <strong>expected tests as "
                  "written</strong>, the frequency-weighted average; the <strong>expected "
                  "tests, best order</strong>, with the conditions sorted from most to "
                  "least frequent and any `else` kept last; and the <strong>saved per "
                  "case</strong>, the difference. The frequencies here are illustrative: "
                  "5% server errors, 10% client errors, 15% redirects and 70% successes, "
                  "the kind of mix a log might show. In the <code>as-written</code> "
                  "preset, the classifier's order, the chain makes 7/2 = 3.50 tests per "
                  "status on average, because the most common answer is tested last; "
                  "in the best order it makes 3/2 = 1.50, and 2 tests per status are "
                  "saved."),
            ("p", "The other two presets move the final `else`. In "
                  "<code>common-first</code> success is tested first and server errors "
                  "fall to the `else`: 29/20 = 1.45 tests as written and in the best "
                  "order, 0 saved, because the order is already the best. In "
                  "<code>else-is-common</code> the three error and redirect classes are "
                  "tested and success is left to the `else`. That costs 14/5 = 2.80 tests, "
                  "and the best reordering of the three conditions brings it only to "
                  "13/5 = 2.60, saving 1/5 = 0.20, because 70% of the cases still pass "
                  "all three tests on the way to the `else`. The cure there is not "
                  "reordering but testing the common case by name. On a classifier the "
                  "difference is a few comparisons, and the chapter's first reason, the "
                  "reader who looks for the usual case, is usually the stronger."),
            ("h3", "Exercise"),
            ("p", "(a) A request router tests `DELETE`, then `POST`, then `GET`, and "
                  "its logs show 5% of requests are `DELETE`, 15% `POST` and 80% `GET`. "
                  "How many tests does it make per request on average, and how many with "
                  "the tests in order of frequency? (b) Here is a router written as a "
                  "chain:"),
            ("code", _lines(ROUTE)),
            ("p", "Name a request that no branch of `route` handles, say what happens to "
                  "it, and write the change that would trap it as Section 15.1 asks. Work "
                  "both parts by hand; you can type the frequencies of part (a) into the "
                  "lab afterwards to check them."),
            ("p", "A chain decides once. The next lesson, Controlling Loops, takes the "
                  "statement that decides again on every pass."),
        ],
        "lab": ("cckit", {
            "mode": "search",
            "view": "chain",
            "preset": "as-written",
            "presets": [
                {"id": "as-written",
                 "label": "As written: server error, client error, redirect, success (illustrative frequencies)",
                 "cases": "server error, 5; client error, 10; redirect, 15; success, 70",
                 "expect": {"seExpected": "7/2 = 3.50", "seBest": "3/2 = 1.50", "seSaved": "2"}},
                {"id": "common-first",
                 "label": "Success first, server errors to the final else",
                 "cases": "success, 70; redirect, 15; client error, 10; else, 5",
                 "expect": {"seExpected": "29/20 = 1.45", "seBest": "29/20 = 1.45", "seSaved": "0"}},
                {"id": "else-is-common",
                 "label": "Success left to the final else",
                 "cases": "server error, 5; client error, 10; redirect, 15; else, 70",
                 "expect": {"seExpected": "14/5 = 2.80", "seBest": "13/5 = 2.60", "seSaved": "1/5 = 0.20"}},
            ],
            "panel_title": "What a chain's order costs",
            "panel_intro": (
                "Each case is charged the tests it takes to reach it, weighted by its "
                "frequency. The frequencies are the lesson's illustration. Reordering is "
                "valid only when the conditions are mutually exclusive, which the lab "
                "cannot check."
            ),
        }),
        "steps_title": "Computing what a chain's order costs",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("List the cases in the chain's order",
             "Write each condition with its frequency, from a log if you have one. A final "
             "else is the last case."),
            ("Charge each case its tests",
             "The first condition costs one test, the second two, and so on; the final "
             "else costs as many as there are conditions."),
            ("Weight and divide",
             "Multiply each case's tests by its frequency, add, and divide by the total "
             "frequency. That is the expected number of tests."),
            ("Reorder, if the tests are exclusive",
             "Sort the conditions from most to least frequent and compute again. Check "
             "first that no condition relies on an earlier one having failed, or the "
             "reordered chain gives different answers."),
            ("Do it on your own code",
             "Type an if-else-if chain from your own code into the lab, with frequencies "
             "from a log or a guess, note the expected tests as written and in the best "
             "order, and write one sentence saying which the frequencies came from."),
        ],
        "worked": {
            "title": "The classifier as written",
            "intro": [
                "Take the as-written preset: server error 5, client error 10, redirect 15, "
                "success 70, in that order, with no final else.",
            ],
            "lines": [
                "server error: 1 test × 5 gives 5",
                "client error: 2 tests × 10 gives 20",
                "redirect: 3 tests × 15 gives 45",
                "success: 4 tests × 70 gives 280",
                "(5 + 20 + 45 + 280) / 100 gives 3.5 tests",
                "success first: (70 + 30 + 30 + 20) / 100 gives 1.5",
            ],
            "after": [
                "Reordering saves two tests per status on average, and the answer for every "
                "status code is the same in both orders, because the four tests are "
                "mutually exclusive.",
            ],
        },
        "quiz_title": "Chains, their cost and their last else",
        "quiz": [
            {"q": "A router tests `DELETE` (5% of requests), then `POST` (15%), then "
                  "`GET` (80%). Charging one test for each condition reached, how many "
                  "tests does it make per request on average, and how many with the "
                  "tests in order of frequency?",
             "a": ["11/4 = 2.75 as written; 5/4 = 1.25 in order of frequency",
                   "2 as written; 2 in order of frequency",
                   "11/4 = 2.75 as written; 11/4 = 2.75 in order of frequency",
                   "3 as written; 1 in order of frequency"],
             "c": 0,
             "why": "As written: (1·5 + 2·15 + 3·80)/100 = 275/100 = 11/4 = 2.75 tests. "
                    "With `GET` first: (1·80 + 2·15 + 3·5)/100 = 125/100 = 5/4 = 1.25. "
                    "The plain average of 1, 2 and 3 is 2, which ignores the frequencies; "
                    "3 and 1 are the costs of `GET` alone in each order."},
            {"q": "In the exercise's `route`, what happens to a request whose method is "
                  "`PATCH`?",
             "a": ["Java throws an exception, because no branch matched",
                   "It passes every test, and `route` returns having done nothing",
                   "It is handled by the last branch, the `DELETE` one",
                   "`javac` rejects the chain, because it has no final `else`"],
             "c": 1,
             "why": "Any method the chain does not name, `PATCH`, `HEAD`, or a misspelling "
                    "such as a lower-case `get`, fails all four tests and falls through "
                    "silently: Java neither complains nor throws. A final `else` that "
                    "rejects the request and reports it is Section 15.1's error trap, "
                    "and the chapter's key point quoted at the head of the lesson."},
            {"q": "In <code>else-is-common</code> (server error 5, client error 10, redirect 15, "
                  "else 70), why does the best reordering save only 1/5 = 0.20 tests per "
                  "case?",
             "a": ["Because the lab charges the final else no tests",
                   "Because the three conditions are not mutually exclusive",
                   "Because 70% of the cases are in the final else, which costs all three "
                   "tests in any order of the conditions",
                   "Because reordering never saves more than one test"],
             "c": 2,
             "why": "The else costs three tests, one for each condition before it, "
                    "whatever their order, and it carries 70% of the cases; reordering the "
                    "other 30% saves little. In <code>as-written</code> reordering saves 2 tests, so "
                    "the last option is false, and the conditions here are exclusive."},
            {"q": "Section 15.2 says the default clause of a case statement should be used "
                  "for a legitimate default or for what else?",
             "a": ["To detect errors, with a diagnostic message",
                   "To hold the most common case, saving a test",
                   "To hold the last remaining real case, saving a label",
                   "Nothing: a case statement is clearer without one"],
             "c": 0,
             "why": "The chapter says to use the default clause to detect errors when it is "
                    "not a legitimate default (p. 363), and calls coding the last real case "
                    "as the default a mistake that loses documentation and breaks down "
                    "under modification."},
        ],
        "mistakes": [
            ("Thinking the order of mutually exclusive tests does not matter",
             "It does not matter to the result: each status code gets the same class in any "
             "order. It matters to the cost and to the reader, and Chapter 15 weighs both. "
             "On the lesson's illustration the classifier as written makes 7/2 = 3.50 "
             "tests per status and 3/2 = 1.50 with success first; and a reader looking "
             "for the usual case finds it at the top instead of the bottom."),
            ("Treating a chain as complete because it handles every case you thought of",
             "The final else is for the cases you did not think of. A router that names "
             "four methods handles four; every other request passes all four tests and "
             "is dropped without a word, which is what Section 15.1's final else, with "
             "its message for the programmer, is there to prevent."),
            ("Reordering a chain whose tests depend on each other",
             "A chain of range tests such as `status >= 500`, then `status >= 400`, gives "
             "the right answer only in that order, because each test assumes the ones "
             "before it failed. Reorder it by frequency and a server error is classed as "
             "a client error. The lab's arithmetic assumes the tests are mutually "
             "exclusive, and it cannot check that; the classifier tests "
             "`hundreds == 5` and so on for that reason."),
        ],
        "standard": (
            "Finish when you can compute what a chain's order costs and find what it lets through.",
            "Given a chain's cases in order with their frequencies, compute the expected "
            "number of tests, and the expected number with the cases in order of "
            "frequency; and for a chain, name an input that no branch catches, by hand."
        ),
        "note": (
            "The lab counts tests and treats every test as costing the same, where a "
            "string comparison costs more than an integer one; it does not time anything. "
            "The frequencies are the lesson's illustration, and yours should come from a "
            "log. The lab cannot tell whether your conditions are mutually exclusive, "
            "and it cannot measure the cost the chapter puts first, which is the "
            "reader's."
        ),
    },
    # ---------------------------------------------------------------- 03
    # McConnell Chapter 16, §§16.1-16.4, pp. 367-389. Opening quotation:
    # Key Points, p. 389 (20 words). Kinds of loop, pp. 367-372; controlling
    # the loop, pp. 373-385 (entering, the middle, exit; the loop index's final
    # value, p. 377; endpoints, p. 381; loop-index scope, pp. 383-384;
    # length and nesting, p. 385); inside out, pp. 385-387; loops and arrays,
    # pp. 387-388.
    # F13, p. 385: loops of one screen or page, rarely over 15 or 20 lines;
    # nesting limited to three levels (Yourdon 1986a).
    {
        "slug": "controlling-loops",
        "title": "Controlling Loops",
        "module": "Chapter 16 · Loops",
        "one_line": "A loop's header decides how many times it runs, the last value its index takes and the value the index is left holding, and Chapter 16 asks you to work all three out before the loop runs.",
        "summary": (
            "Chapter 16 chooses the kind of loop, controls its entry, body and exit, and "
            "limits its length and nesting. Compute from a header alone how many times a "
            "loop runs, the last value of its index in the body and the value it would "
            "hold afterwards, and find the header that never ends."
        ),
        "key": [
            "choose the loop by its test and its count",
            "treat the loop body as a black box",
            "check the first, a middle and the last pass",
            "do not rely on the index after the loop",
            "keep loops short; nest three levels at most",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "Three ideas from Chapter 16 carry the lesson: one about where a loop tests, "
            "one about where it goes wrong, and one about what it leaves behind."
        ),
        "concepts": [
            ("Where the loop tests",
             "A loop can test whether it has finished at the beginning, in the middle or "
             "at the end. That decides whether its body runs at least once, and with the "
             "loop's flexibility it decides which kind of loop to use."),
            ("The off-by-one error",
             "A loop that runs once too often or once too few times, usually because `<=` "
             "was written where `<` was meant or the other way round. It is also called a "
             "fencepost error: ten sections of fence need eleven posts."),
            ("The index's final value",
             "The value a loop index holds once the loop is over. It is one step past the "
             "last value used in the body, it differs between languages and between a "
             "normal and an early exit, and the chapter says not to write code that "
             "depends on it."),
        ],
        "read_title": "The chapter's argument first, then the header",
        "read_intro": (
            "The lesson goes through Chapter 16's four sections, then reads four loop "
            "headers with the lab, and ends with one for you."
        ),
        "body": [
            ("p", "<strong>Chapter 16, p. 389.</strong> &ldquo;Think through the loop "
                  "carefully to verify that it operates normally under each case and "
                  "terminates under all possible conditions.&rdquo; It is the last of the "
                  "chapter's key points. Read Chapter 16, pp. 367&ndash;389, in your own "
                  "copy first."),
            ("p", "You have probably written a loop that ran once too often: the array "
                  "had ten entries, the loop asked for eleven, and the program stopped "
                  "with an exception on a line that looked right. Chapter 16 opens by "
                  "calling loops one of the most complex parts of programming, and spends "
                  "its pages on keeping them simple enough that such mistakes show."),
            ("p", "Section 16.1 (p. 367) sorts loops into counted loops, continuously "
                  "evaluated loops, endless loops and iterator loops, and then by two "
                  "properties: how flexible the loop is, and whether it tests for "
                  "completion at the beginning, the middle or the end, which decides "
                  "whether the body runs at least once. Use a `while` loop when you do not "
                  "know in advance how many times it will run, and a `for` loop when you "
                  "do. Prefer `for` when it fits, because all of its control sits in the "
                  "header; but keep the header for statements that control the loop, and "
                  "do not cram a `while` loop's housekeeping into it."),
            ("p", "Section 16.2 (p. 373) begins with a list of what goes wrong with loops, "
                  "from missing initialization to a wrong termination, and two practices "
                  "against it: minimize the number of things that affect the loop, and "
                  "treat its inside like a routine, a black box whose controlling "
                  "conditions can be read without looking in. Enter the loop from one "
                  "place, with its initialization directly before it; write an infinite "
                  "loop as `while (true)`; brace the body, keep it non-empty, keep its "
                  "housekeeping together and give it one job. On the way out, make sure "
                  "the loop ends, make the ending obvious, and do not alter a `for` loop's "
                  "index to stop it early: use a `while` loop instead."),
            ("p", "Two of the section's guidelines are the lesson's subject. Check the "
                  "endpoints: run through the first pass, a pass in the middle and the "
                  "last pass in your head, and with a calculator if the body computes "
                  "something (p. 381). And avoid code that depends on the index's value "
                  "after the loop (p. 377): it varies from language to language and "
                  "between a normal ending and an early one, and the next reader will have "
                  "to stop and work it out, so save what you need in a variable inside "
                  "the loop. In Java an index declared in the `for` header does not exist "
                  "after the loop at all; the book reports three C++ compilers giving "
                  "three different answers on the same point (p. 384), which is a reason "
                  "not to rely on the language to settle it."),
            ("p", "The section ends with length and nesting. Make a loop short enough to "
                  "see all at once; the book reports an expert limit of one page, and "
                  "adds that a programmer who values simple code will rarely write a loop "
                  "longer than 15 or 20 lines. Limit nesting to three levels, after a "
                  "finding Yourdon reports, that the ability to understand a loop falls "
                  "sharply beyond three (p. 385). These are guidelines from other "
                  "people's experience, collected before 2004; your own code reviews can "
                  "test them. Section 16.3 (p. 385) then shows how to build a hard loop "
                  "from the inside out: write one case with literals, put a loop round "
                  "it, replace the literals, and repeat. Section 16.4 (p. 387) notes that "
                  "loops and arrays usually correspond, though some languages, APL and "
                  "later Fortran among them, operate on whole arrays with no loop at "
                  "all; in Java the loop is required."),
            ("p", "Now the header. The lab's <em>loop</em> view reads the loop "
                  "`for (int i = start; i cmp bound; i += step)`, where `cmp` is typed as "
                  "one of `lt`, `le`, `ne`, `gt` or `ge` for `<`, `<=`, `!=`, `>` and "
                  "`>=`, and computes from those four values alone, in closed form, "
                  "without running anything. It prints the <strong>iterations</strong>, "
                  "the <strong>last value of i in the body</strong>, and <strong>i after "
                  "the loop, if declared before it</strong>: the value an index declared "
                  "outside the loop would be left holding, which is the value p. 377 "
                  "advises against using. Here is a loop with the classic mistake:"),
            ("code", _lines(HOURLY)),
            ("p", "The <code>fencepost</code> preset is its header: start 0, `le`, bound "
                  "10, step 1. The lab prints 11 iterations, a last value of 10 and 11 "
                  "after the loop. The array has ten entries, numbered 0 to 9, so the "
                  "eleventh pass asks for `hourly[10]` and Java throws an "
                  "`ArrayIndexOutOfBoundsException`. The <code>half-open</code> preset is "
                  "the fix, `<` in place of `<=`: 10 iterations, last value 9, and 10 "
                  "after. Changing one character changed all three figures, not only the "
                  "last pass."),
            ("p", "The <code>counting-down</code> preset runs from 10 down to and "
                  "including 0, `ge` with a step of −1: 11 iterations, a last value of 0, "
                  "and −1 after the loop, one step past in the direction of travel. The "
                  "<code>skips-the-bound</code> preset is start 0, `ne`, bound 9, step 2, "
                  "and the lab prints &ldquo;never ends&rdquo;: `i` takes only even values, "
                  "9 is odd, and even when `i` passes the top of Java's `int` and wraps "
                  "round to the bottom it stays even, so `i != 9` never becomes false. "
                  "This is the case the opening quotation asks you to think through, a "
                  "loop that terminates under some conditions and not others; with `<` "
                  "in the test it would have stopped after 5 passes."),
            ("h3", "Exercise"),
            ("code", _lines(BY_THREES)),
            ("p", "From the header alone, state how many times the body runs, the last "
                  "value it prints, and the value an `i` declared before the loop would "
                  "hold after it. Then type the header into the lab as start 10, `gt`, "
                  "bound 0, step −3 to check."),
            ("p", "Loops and conditionals are the ordinary structures. The next lesson, "
                  "Unusual Control Structures, takes the ones Chapter 17 calls unusual: "
                  "early returns, recursion and the `goto`."),
        ],
        "lab": ("cckit", {
            "mode": "run",
            "view": "loop",
            "preset": "fencepost",
            "presets": [
                {"id": "fencepost",
                 "label": "0 to 10, at most 10 (the lesson's hourly loop)",
                 "start": 0, "cmp": "le", "bound": 10, "step": 1,
                 "expect": {"lpIterations": "11", "lpLast": "10", "lpAfter": "11"}},
                {"id": "half-open",
                 "label": "0 to 10, below 10",
                 "start": 0, "cmp": "lt", "bound": 10, "step": 1,
                 "expect": {"lpIterations": "10", "lpLast": "9", "lpAfter": "10"}},
                {"id": "counting-down",
                 "label": "10 down to 0, at least 0",
                 "start": 10, "cmp": "ge", "bound": 0, "step": -1,
                 "expect": {"lpIterations": "11", "lpLast": "0", "lpAfter": "−1"}},
                {"id": "skips-the-bound",
                 "label": "0 by twos, while not 9",
                 "start": 0, "cmp": "ne", "bound": 9, "step": 2,
                 "expect": {"lpIterations": "never ends"}},
            ],
            "panel_title": "What a loop header decides",
            "panel_intro": (
                "The lab reads one header, for (int i = start; i cmp bound; i += step), "
                "over Java's int, and computes the run in closed form. The body is not "
                "read: a body that changes i or breaks out early is outside the count."
            ),
        }),
        "steps_title": "Reading a loop from its header",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("Write the first values",
             "Start at the header's first value and apply the step two or three times, so "
             "you see the direction and the spacing."),
            ("Find the last value the test accepts",
             "Walk to the bound: the last value of i for which the test is still true is "
             "the last value in the body. If no value ever makes the test false, the loop "
             "never ends."),
            ("Count the values",
             "The number of values from the first to the last, in steps of the step, is "
             "the number of iterations."),
            ("Take one more step",
             "One step past the last value is where the test first fails, and that is "
             "what an index declared before the loop is left holding."),
            ("Do it on your own code",
             "Type four loop headers from your own code into the lab, note the "
             "iterations, the last value and the value after for each, and mark any "
             "header whose figures differ from what you would have said."),
        ],
        "worked": {
            "title": "Zero to ten, inclusive",
            "intro": [
                "Take the fencepost header, for (int i = 0; i <= 10; i++).",
            ],
            "lines": [
                "values of i in the body: 0, 1, 2, … 10",
                "count: 10 - 0 + 1 gives 11 passes",
                "last value in the body: 10",
                "the test first fails at i == 11",
                "so an i declared before the loop holds 11",
            ],
            "after": [
                "The loop runs 11 times, one more than the 10 its bound suggests, and the "
                "index ends one step past its last value in the body. Written with < it "
                "runs 10 times and ends at 10.",
            ],
        },
        "quiz_title": "Counts, last values and loops that never end",
        "quiz": [
            {"q": "For `for (int i = 10; i > 0; i -= 3)`, how many times does the body "
                  "run, what is the last value of `i` in it, and what would an `i` "
                  "declared before the loop hold afterwards?",
             "a": ["4 times; last value 1; −2 after",
                   "3 times; last value 4; 1 after",
                   "4 times; last value 1; 1 after",
                   "4 times; last value −2; −2 after"],
             "c": 0,
             "why": "The body runs 4 times, for 10, 7, 4 and 1. The next value, 1 − 3 = −2, "
                    "fails `i > 0`, so −2 is what an `i` declared before the loop holds "
                    "afterwards. Stopping at 4 drops the pass for 1, and giving 1 for the "
                    "value after mistakes the last value in the body for the index's "
                    "final value."},
            {"q": "How many times does `for (int i = 0; i <= 10; i++)` run?",
             "a": ["10", "11", "9", "12"],
             "c": 1,
             "why": "It runs for every whole number from 0 to 10 inclusive: 10 − 0 + 1 = 11. "
                    "With `<` it would run 10 times, which is the off-by-one the lesson's "
                    "`hourly` loop makes in the other direction."},
            {"q": "Which of these headers never ends?",
             "a": ["`for (int i = 0; i != 10; i += 2)`",
                   "`for (int i = 9; i > 0; i -= 2)`",
                   "`for (int i = 0; i != 9; i += 2)`",
                   "`for (int i = 0; i < 9; i += 2)`"],
             "c": 2,
             "why": "Counting up by twos from 0 gives only even values, and 9 is odd, so "
                    "`i != 9` is never false; wrapping past the top of `int` keeps `i` "
                    "even. The `!= 10` loop reaches 10 after 5 passes, the loop down from "
                    "9 runs for 9, 7, 5, 3 and 1, and `< 9` runs for 0, 2, 4, 6 and 8."},
            {"q": "What does Section 16.2 advise about the value of a loop index once "
                  "the loop is over?",
             "a": ["Rely on it, since it is always one step past the last value",
                   "Declare the index before the loop so that the value is kept",
                   "Reset it to zero so that it cannot be misused",
                   "Avoid code that depends on it, and save any value you need inside "
                   "the loop"],
             "c": 3,
             "why": "The book calls depending on the index's final value bad form, because "
                    "the value varies between languages and implementations and between a "
                    "normal and an early exit, and advises assigning the value you need "
                    "to a variable inside the loop (p. 377)."},
        ],
        "mistakes": [
            ("Thinking <= and < differ by one only at the end",
             "They differ in the count, the last value and the value after. On the "
             "lesson's header, `<= 10` gives 11 iterations, a last value of 10 and 11 "
             "after; `< 10` gives 10, 9 and 10. And with `!=` the difference can be "
             "between a loop that stops and one that never does: counting up by twos "
             "from 0, `i != 9` never becomes false. That is why the chapter asks you to "
             "check the first, a middle and the last pass."),
            ("Thinking the index after the loop is the last value it had in the body",
             "The index is left one step past it, because the loop ends at the first value "
             "the test rejects. The fencepost loop's last value in the body is 10 and an "
             "index declared outside it holds 11; the counting-down loop's last value is "
             "0 and the index holds −1. Section 16.2 advises not relying on either."),
            ("Stopping a for loop by setting its index",
             "Setting `i` to the bound inside the body to end the loop early is what the "
             "book calls monkeying with the loop index (p. 377). The header no longer "
             "says when the loop ends, and a reader has to look inside. A `while` loop, "
             "whose condition holds the whole exit, is the chapter's alternative."),
        ],
        "standard": (
            "Finish when you can read a loop's run from its header.",
            "For four loop headers, state the iterations, the last value of the index in "
            "the body and the value it would hold after the loop, and say which header "
            "never ends, without the lab."
        ),
        "note": (
            "The lab computes from the header alone. A body that changes the index, "
            "breaks out or throws is outside its count, and so is any loop that is not a "
            "for loop over an int. The length and nesting limits come from the book's "
            "reading of other people's experience and are guidelines, not properties of "
            "a loop the lab could check."
        ),
    },
    # ---------------------------------------------------------------- 04
    # McConnell Chapter 17, §§17.1-17.4, pp. 391-410. Opening quotation:
    # Key Points, p. 410 (22 words). Multiple returns and guard clauses,
    # pp. 391-393; recursion, pp. 393-398 (tips, pp. 396-397; factorials and
    # Fibonacci, pp. 397-398, "I'd hire someone else", p. 397); goto,
    # pp. 398-408 (Dijkstra 1968 and Knuth 1974, pp. 398-399; Shneiderman and
    # Sheil, p. 399; the summary of guidelines, pp. 407-408); perspective,
    # p. 408. Fowler 1999 on guard clauses, p. 408. This course's §F.4 aside
    # (the goto history) is the late p before the last.
    {
        "slug": "unusual-control-structures",
        "title": "Unusual Control Structures",
        "module": "Chapter 17 · Unusual Control Structures",
        "one_line": "Early returns, recursion and the goto each make some code clearer and other code harder to follow, and Chapter 17 asks you to use each where it helps and to know what it costs.",
        "summary": (
            "Chapter 17 takes the control structures that sit between leading-edge and "
            "discredited: returns from the middle of a routine, guard clauses, recursion "
            "and the goto. Count the calls a recursive Fibonacci makes against the passes "
            "of its loop, and flatten a nested routine with guard clauses."
        ),
        "key": [
            "return early when it reads better",
            "guard clauses clear the nominal path",
            "make sure recursion stops",
            "no recursion for Fibonacci",
            "recursive Fibonacci: 2·F(n + 1) - 1 calls",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "Chapter 17 has three structures and a perspective on all of them. The lesson "
            "uses three ideas."
        ),
        "concepts": [
            ("Guard clause",
             "A test at the top of a routine that returns at once when an error or "
             "special case holds, so that the rest of the routine, the nominal path, runs "
             "unindented instead of inside a stack of nested ifs."),
            ("Recursion",
             "A routine that solves part of a problem itself and calls itself on the "
             "smaller pieces. It needs a case that does not call itself, or it never "
             "stops."),
            ("goto",
             "An unconditional jump to a label. Java reserves the word and has no goto "
             "statement; C, C++ and Visual Basic have one. Chapter 17 sets out the case "
             "against it and the case for its careful use."),
        ],
        "read_title": "The chapter's argument first, then the calls",
        "read_intro": (
            "The lesson goes through Chapter 17's four sections, counts the calls of a "
            "recursive routine with the lab, and ends with a routine to flatten."
        ),
        "body": [
            ("p", "<strong>Chapter 17, p. 410.</strong> &ldquo;Multiple returns can "
                  "enhance a routine&rsquo;s readability and maintainability, and they "
                  "help prevent deeply nested logic. They should, nevertheless, be used "
                  "carefully.&rdquo; It is the first of the chapter's key points. Read "
                  "Chapter 17, pp. 391&ndash;410, in your own copy first."),
            ("p", "Which control structures are safe to use, and when? Chapter 17 opens "
                  "by placing its three structures somewhere between the leading edge and "
                  "the discredited, and sometimes in both camps at once: useful, with "
                  "care, in the languages that offer them. Section 17.1 (p. 391) is returns from the "
                  "middle of a routine. Use a return when it makes the routine easier to "
                  "read, as when the answer is known and nothing is left to clean up. Use "
                  "guard clauses, early returns that check the error cases first, to "
                  "simplify complicated error processing: otherwise the nominal path ends "
                  "up indented inside every check. McConnell is careful about the gain. "
                  "Once each guard clause has to set an error status before it returns, "
                  "the code before the nominal path grows, and his verdict is that the "
                  "guard version is still the more readable and maintainable, though "
                  "only by a small margin (p. 393). And minimize the number of returns, because a "
                  "reader at the bottom of a routine may not know it can return above."),
            ("p", "Section 17.2 (p. 393) is recursion, which McConnell says is not useful "
                  "often but gives elegant solutions when used judiciously, as in a "
                  "sorting routine or a search through a maze. His tips: make sure the "
                  "recursion stops, with a test that takes a path without a recursive "
                  "call; use a safety counter where no such test is simple; keep the "
                  "recursion within one routine; and watch the stack. Then a warning: do "
                  "not use recursion for factorials or Fibonacci numbers, the textbook "
                  "examples, where it is slower, less predictable in memory and harder to "
                  "read than a loop. A programmer of his who did, he says, would be "
                  "replaced (p. 397). His conclusion is not that recursion is to be "
                  "avoided but that it is more powerful than those examples suggest, and "
                  "that its alternatives, iteration and an explicit stack, should be "
                  "considered before it is chosen."),
            ("p", "Section 17.3 (p. 398) is the `goto`, and it gives both sides. Against "
                  "it: code with `goto`s is harder to format, to analyse and to optimize; "
                  "it is rarely the fastest or smallest; and once a few are allowed, more "
                  "follow. For it: careful use in particular cases, to avoid duplicating "
                  "code or to release resources in one place, and the book's report that "
                  "decades of research failed to show the `goto` harmful (p. 399). McConnell's own position is that in a modern "
                  "language almost every `goto` can be replaced, easily or with effort, "
                  "and that in the rare case where one is the right solution it should "
                  "be documented and used. Section 17.4 (p. 408) closes the chapter "
                  "with a perspective: the field has advanced largely by restricting what "
                  "programmers may do, and he views unusual control structures with "
                  "strong skepticism."),
            ("p", "Now the counting. The lab's <em>recursion</em> view takes a routine, "
                  "`factorial` or `fibonacci`, and an `n`, and prints four figures: "
                  "<strong>calls</strong>, how many times the recursive version is "
                  "called; <strong>deepest call</strong>, how many calls are open at once "
                  "at the deepest point; <strong>value</strong>, the answer; and "
                  "<strong>iterations of a loop</strong>, how many passes the loop "
                  "version makes. Here are the two versions of Fibonacci it models, "
                  "written for this lesson. First the recursive one:"),
            ("code", _lines(FIB_RECURSIVE)),
            ("p", "And the loop:"),
            ("code", _lines(FIB_LOOP)),
            ("p", "The <code>factorial-10</code> preset is the mild case: 10 calls, 10 "
                  "deep, value 3,628,800, against 9 passes of a loop. Recursion there "
                  "costs little in calls, and the book's objection is to clarity, speed "
                  "and memory. The <code>fibonacci-30</code> preset is the reason for the "
                  "warning: 2,692,537 calls, never more than 30 deep, for the value "
                  "832,040, which the loop reaches in 29 passes. Each call above the base "
                  "case makes two more, and the two halves recompute the same smaller "
                  "values again and again. The <code>fibonacci-40</code> preset makes "
                  "331,160,281 calls for the value 102,334,155, against 39 passes. The "
                  "depth was never the problem; the number of calls was."),
            ("h3", "Exercise"),
            ("code", _lines(REFUND_NESTED)),
            ("p", "Rewrite `refundAmount` with guard clauses, so that the nominal case, "
                  "returning the order's total, comes last and unindented. Then count the "
                  "decision points before and after, as 1 plus one for each `if`, `for`, "
                  "`while`, `case`, `&&` and `||`, and the deepest nesting of a "
                  "statement, counting a statement directly in the routine's body as "
                  "depth 0 and each pair of braces it sits inside below the routine's "
                  "own as one more. Nesting and Complexity counts both with the lab on a "
                  "larger routine; you can paste your two versions into its lab to check."),
            ("p", "The history behind Section 17.3 is a story with people in it, and this "
                  "course tells it once. In March 1968 Edsger Dijkstra's letter &ldquo;Go "
                  "To Statement Considered Harmful&rdquo; appeared in <em>Communications "
                  "of the ACM</em>, observing that the quality of code fell as the number "
                  "of its `goto`s rose. In 1974 Donald Knuth answered with "
                  "&ldquo;Structured Programming with go to Statements&rdquo;, which "
                  "showed cases where a `goto` made code slower and larger and a few "
                  "where it made a real gain. The book reports both, and that by the "
                  "time it was written many languages, Java among them, had no `goto` at "
                  "all. Since then the jump has survived mostly in disguise. Java gives "
                  "its uses names, a labelled `break`, an early `return`, `finally` for "
                  "cleanup; large C programs still use a forward `goto` to a single "
                  "cleanup label, the very case the book's argument for the `goto` "
                  "describes; and the dispute McConnell said had moved to multiple "
                  "returns, loop exits and exceptions (p. 398) is still argued in those "
                  "terms. Whether those structures are the `goto` tamed or the `goto` "
                  "back by another name is a question this lesson leaves with you."),
            ("p", "Every structure so far has been written as code. The next lesson, "
                  "Table-Driven Methods, moves some of the logic out of the code and into "
                  "data."),
        ],
        "lab": ("cckit", {
            "mode": "run",
            "view": "recursion",
            "preset": "fibonacci-30",
            "presets": [
                {"id": "factorial-10",
                 "label": "factorial(10)",
                 "fn": "factorial", "n": 10,
                 "expect": {"lpCalls": "10", "lpDepth": "10", "lpValue": "3,628,800", "lpLoop": "9"}},
                {"id": "fibonacci-30",
                 "label": "fibonacci(30), the lesson's routine",
                 "fn": "fibonacci", "n": 30,
                 "expect": {"lpCalls": "2,692,537", "lpDepth": "30", "lpValue": "832,040", "lpLoop": "29"}},
                {"id": "fibonacci-40",
                 "label": "fibonacci(40)",
                 "fn": "fibonacci", "n": 40,
                 "expect": {"lpCalls": "331,160,281", "lpValue": "102,334,155", "lpLoop": "39"}},
            ],
            "panel_title": "Recursion against its loop",
            "panel_intro": (
                "The lab counts the calls the recursive version makes, its deepest chain "
                "of open calls, the value, and the passes the loop version makes. It counts; "
                "it does not time anything or measure the stack."
            ),
        }),
        "steps_title": "Flattening a routine and counting a recursion",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("Find the nominal path",
             "In a routine with nested ifs, find the statement that does the routine's "
             "real work, and the conditions it sits inside."),
            ("Turn each condition into a guard",
             "For each enclosing condition, write its negation as an if at the top that "
             "returns what the routine returns when the condition fails."),
            ("Count what changed",
             "Count the decision points and the deepest nesting before and after. Guard "
             "clauses move the tests; they do not remove them."),
            ("Count a recursion",
             "For a recursive routine, count the calls for a small n by drawing the tree "
             "of calls, and compare them with the passes of the loop that does the same "
             "work."),
            ("Do it on your own code",
             "Take one routine of your own with an if nested inside another, rewrite it "
             "with guard clauses, and write down its decision points and deepest nesting "
             "before and after."),
        ],
        "worked": {
            "title": "The calls fibonacci(30) makes",
            "intro": [
                "Count the calls of the lesson's recursive fibonacci, whose base case "
                "returns n when n is below 2.",
            ],
            "lines": [
                "calls(0) and calls(1) are 1 each",
                "calls(n) is 1 + calls(n - 1) + calls(n - 2)",
                "so calls(n) is 2 · F(n + 1) - 1",
                "F(31) is 1346269",
                "calls(30): 2 · 1346269 - 1 gives 2692537",
                "the loop: i from 2 to 30, 29 passes",
            ],
            "after": [
                "The recursive version makes 2,692,537 calls for an answer the loop reaches "
                "in 29 additions. The definition of the Fibonacci numbers is recursive; "
                "the computation does not have to be.",
            ],
        },
        "quiz_title": "Guard clauses and recursion",
        "quiz": [
            {"q": "You rewrote `refundAmount` with guard clauses. Counting decision points "
                  "as 1 plus one for each `if`, `for`, `while`, `case`, `&&` and `||`, and "
                  "depth with a statement directly in the routine's body at 0, what "
                  "changes?",
             "a": ["Decision points fall from 3 to 1; the deepest nesting from 2 to 0",
                   "Decision points stay at 3; the deepest nesting falls from 2 to 1",
                   "Decision points rise from 3 to 4, for the extra return; nesting falls "
                   "from 2 to 1",
                   "Decision points stay at 3; the deepest nesting stays at 2"],
             "c": 1,
             "why": "The guard-clause version returns `0.0` early when the order is not "
                    "paid and when more than 30 days have passed since delivery, then "
                    "returns `order.total()`. Both versions have two `if`s, so 1 + 2 = 3 "
                    "decision points before and after; a `return` is not a decision. The "
                    "deepest statement was at depth 2, inside two `if`s, and is now at "
                    "depth 1, inside one. Nesting and Complexity counts the same "
                    "transformation again on a larger routine."},
            {"q": "How many calls does the lesson's recursive `fibonacci` make for n = 30?",
             "a": ["30", "832,040", "1,346,269", "2,692,537"],
             "c": 3,
             "why": "Calls follow calls(n) = 1 + calls(n − 1) + calls(n − 2), which "
                    "gives 2·F(n + 1) − 1 = 2·1,346,269 − 1 = 2,692,537. 30 is the depth, "
                    "832,040 the value F(30), and 1,346,269 is F(31) before doubling."},
            {"q": "What does Section 17.2 say about using recursion to compute factorials "
                  "or Fibonacci numbers?",
             "a": ["Don't: a loop is faster, more predictable and easier to read",
                   "Use it, because the definitions are recursive",
                   "Use it only with a safety counter",
                   "Use it only in languages without loops"],
             "c": 0,
             "why": "The book calls them silly textbook examples and says not to use "
                    "recursion for them (p. 397). Safety counters are its tip for "
                    "recursion that has no simple stopping test, which these have."},
            {"q": "Which of these is one of the arguments for the `goto` that Section 17.3 "
                  "reports?",
             "a": ["A `goto` always makes code faster",
                   "Dijkstra recommended it for loops",
                   "A well-placed `goto` can remove duplicated code",
                   "Java's designers included it"],
             "c": 2,
             "why": "The case for the `goto` is its careful use in particular cases, such "
                    "as avoiding duplicate code or releasing resources in one place "
                    "(p. 399). The book says `goto` code is rarely the fastest, "
                    "Dijkstra's letter argued against it, and Java has no `goto`."},
        ],
        "mistakes": [
            ("Thinking recursion is the natural way to compute Fibonacci numbers",
             "The definition is recursive, but the computation need not be, and the book "
             "says not to make it so. On the lesson's routine the recursive version makes "
             "2,692,537 calls for fibonacci(30), recomputing the same smaller values over "
             "and over, where a loop makes 29 passes. The lab illustrates what Section "
             "17.2 argues: the recursive version is slower and harder to follow than the "
             "iterative one."),
            ("Insisting on exactly one return per routine",
             "A single exit is a rule some programmers take from structured programming. "
             "Chapter 17 does not hold to it: use a return when it makes the routine "
             "easier to read, use guard clauses to keep the nominal path clear, and keep "
             "the number of returns small, because a reader can miss one."),
            ("Taking the warning as a rule against recursion",
             "The warning is about two textbook examples. The same section calls "
             "recursion a powerful tool that gives elegant solutions when used "
             "judiciously, as in a sort or a maze search, where the alternative would be "
             "much more complicated, and asks only that you consider iteration before "
             "you choose it."),
        ],
        "standard": (
            "Finish when you can flatten a nested routine with guard clauses and compare a recursion with its loop.",
            "For a routine with two nested ifs and a single return, write the guard-clause "
            "version and say what changes in its nesting and what does not in its "
            "decision points; for naive recursive Fibonacci at n, state the calls, "
            "2·F(n + 1) − 1, and the loop's iterations, by hand."
        ),
        "note": (
            "The lab counts calls and passes; it does not time either version, and it does "
            "not model the stack, so how deep a recursion a Java program can go before "
            "it fails is outside it. Its two routines are the lesson's, and the value "
            "fits a Java `long` for every n it accepts. Nothing in it speaks to the "
            "`goto`, where the chapter's argument is about code in general and has to be "
            "weighed, not counted."
        ),
    },
]
