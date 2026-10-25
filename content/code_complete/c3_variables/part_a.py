"""Variables, lessons 1-6 -- Part III of Code Complete, Chapters 10-13.

Every quotation is copied from the second edition (Microsoft Press, 2004),
printed pagination; the comment beside each lesson gives its pages, and each
quotation was checked against the text. Every snippet is written for its
lesson and is one constant below, used both by the lesson's code block and by
the lab preset that counts it, so the line numbers the prose names are the
lab's. Figures attributed to the book carry their PLAN.md S.2 id and page.
"""

# ---------------------------------------------------------------- snippets

# Lesson 1, Declaring and Initializing Variables (presets.py init-bad,
# init-good, init-twice).
COUNT_UNSET = "\n".join([
    "double averagePrice(double[] prices) {",
    "    int count;",
    "    double total = 0.0;",
    "    for (int i = 0; i < prices.length; i++) {",
    "        total = total + prices[i];",
    "        count = count + 1;",
    "    }",
    "    return total / count;",
    "}",
])

INITIALIZED = "\n".join([
    "double averagePrice(double[] prices) {",
    "    double total = 0.0;",
    "    int count = 0;",
    "    for (int i = 0; i < prices.length; i++) {",
    "        total = total + prices[i];",
    "        count = count + 1;",
    "    }",
    "    return total / count;",
    "}",
])

SET_TWICE = "\n".join([
    "double averagePrice(double[] prices) {",
    "    double total = 0.0;",
    "    int count = 0;",
    "    total = prices[0];",
    "    count = prices.length;",
    "    double average = total / count;",
    "    return total / count;",
    "}",
])

# The exercise: the lab reports nothing; javac rejects line 6.
INITIALS_EXERCISE = "\n".join([
    "String initials(String first, String last) {",
    "    String result;",
    "    if (first.length() > 0) {",
    "        result = first.substring(0, 1);",
    "    }",
    "    result = result + last.substring(0, 1);",
    "    return result;",
    "}",
])

# Lesson 2, Scope, Span and Live Time (PLAN D.4 auditShipments).
DECLARED_AT_TOP = "\n".join([
    "void auditShipments(Shipment[] shipments, int limitKg) {",
    "    int scanned = 0;",
    "    int heaviestKg = 0;",
    "    int overLimit = 0;",
    "    printTitle();",
    "    printLegend();",
    "    for (Shipment s : shipments) {",
    "        s.verify();",
    "        scanned = scanned + 1;",
    "    }",
    "    printCount(scanned);",
    "    for (Shipment s : shipments) {",
    "        heaviestKg = Math.max(heaviestKg, s.weightKg());",
    "        if (s.weightKg() > limitKg) {",
    "            overLimit = overLimit + 1;",
    "        }",
    "    }",
    "    printSummary(heaviestKg, overLimit);",
    "}",
])

DECLARED_NEAR_USE = "\n".join([
    "void auditShipments(Shipment[] shipments, int limitKg) {",
    "    printTitle();",
    "    printLegend();",
    "    int scanned = 0;",
    "    for (Shipment s : shipments) {",
    "        s.verify();",
    "        scanned = scanned + 1;",
    "    }",
    "    printCount(scanned);",
    "    int heaviestKg = 0;",
    "    int overLimit = 0;",
    "    for (Shipment s : shipments) {",
    "        heaviestKg = Math.max(heaviestKg, s.weightKg());",
    "        if (s.weightKg() > limitKg) {",
    "            overLimit = overLimit + 1;",
    "        }",
    "    }",
    "    printSummary(heaviestKg, overLimit);",
    "}",
])

# The exercise: total on 2, 9, 12 and count on 3, 10, 12; moved below the
# four print calls, to lines 6 and 7.
REPORT_SALES_EXERCISE = "\n".join([
    "void reportSales(Sale[] sales) {",
    "    double total = 0.0;",
    "    int count = 0;",
    "    printHeader();",
    "    printDate();",
    "    printColumns();",
    "    printRule();",
    "    for (Sale sale : sales) {",
    "        total = total + sale.amount();",
    "        count = count + 1;",
    "    }",
    "    printTotals(total, count);",
    "}",
])

# Lesson 3, The Power of Variable Names (presets.py names-short, names-long).
SHORT_NAMES = "\n".join([
    "double calc(double[] a, int n, double r) {",
    "    double t = 0.0;",
    "    for (int i = 0; i < n; i++) {",
    "        double x = a[i] * r;",
    "        t = t + x;",
    "    }",
    "    double tmp = t / n;",
    "    return tmp;",
    "}",
])

PROBLEM_NAMES = "\n".join([
    "double averageNetPrice(double[] grossPrices, int priceCount, double netFactor) {",
    "    double netTotal = 0.0;",
    "    for (int i = 0; i < priceCount; i++) {",
    "        double netPrice = grossPrices[i] * netFactor;",
    "        netTotal = netTotal + netPrice;",
    "    }",
    "    double averageNet = netTotal / priceCount;",
    "    return averageNet;",
    "}",
])

# The exercise: five names of one letter, average 1.
INTEREST_EXERCISE = "\n".join([
    "double f(double p, int n, double r) {",
    "    double m = p * r / 12;",
    "    double t = 0.0;",
    "    for (int i = 0; i < n; i++) {",
    "        t = t + m;",
    "    }",
    "    return t;",
    "}",
])

# Lesson 4, Integers and Floating Point: two listings in the body; the lab
# takes numbers, not code.
MS_PER_YEAR = "\n".join([
    "int msPerYear = 365 * 24 * 60 * 60 * 1000;",
    "System.out.println(msPerYear);",
])

OVERFLOW_EXERCISE = "\n".join([
    "int total = 0;",
    "for (int i = 0; i < 1000; i++) {",
    "    total += 3000000;",
    "}",
    "System.out.println(total);",
])

# Lesson 5, Named Constants and Other Types (presets.py magic, named).
MAGIC = "\n".join([
    "double monthlyPayment(double principal, int years) {",
    "    double rate = 0.0725 / 12;",
    "    int months = years * 12;",
    "    if (months > 360) {",
    "        months = 360;",
    "    }",
    "    double factor = Math.pow(1 + rate, months);",
    "    return principal * rate * factor / (factor - 1);",
    "}",
])

NAMED = "\n".join([
    "static final double ANNUAL_RATE = 0.0725;",
    "static final int MONTHS_PER_YEAR = 12;",
    "static final int MAX_TERM_MONTHS = 360;",
    "",
    "double monthlyPayment(double principal, int years) {",
    "    double rate = ANNUAL_RATE / MONTHS_PER_YEAR;",
    "    int months = Math.min(years * MONTHS_PER_YEAR, MAX_TERM_MONTHS);",
    "    double factor = Math.pow(1 + rate, months);",
    "    return principal * rate * factor / (factor - 1);",
    "}",
])

# The exercise: 38.5, 3 and 900, three magic numbers, three distinct.
WATCH_EXERCISE = "\n".join([
    "void watchWard(Patient[] ward) {",
    "    while (true) {",
    "        for (Patient patient : ward) {",
    "            if (patient.temperature() > 38.5) {",
    "                raiseAlert(patient, 3);",
    "            }",
    "        }",
    "        sleepSeconds(900);",
    "    }",
    "}",
])

# Lesson 6, Structures, Pointers and Global Data: an access routine, in the
# body only (the lab takes records, not code).
ACCESS_ROUTINE = "\n".join([
    "class CurrentRecord {",
    "    private static Record current;",
    "",
    "    static Record get() {",
    "        return current;",
    "    }",
    "",
    "    static void set(Record next) {",
    "        current = next;",
    "    }",
    "}",
])

GLOBAL_USES = (
    "readInput, w, current; validate, r, current; validate, w, errors; "
    "report, r, errors; report, r, current; reset, w, errors; reset, w, current; "
    "addLine, r, current; addLine, rw, total; printTotals, r, total"
)


def lines(snippet):
    """A snippet constant as the line list a code block takes."""
    return snippet.split("\n")


LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapter 10, sections 10.1-10.3, pp. 237-243. Quotation:
    # p. 258 (Key Points), 24 words. Anomaly names: section 22.3, pp. 509-510.
    # Card, Church and Agresti 1986 on unreferenced variables: p. 257.
    {
        "slug": "declaring-and-initializing-variables",
        "title": "Declaring and Initializing Variables",
        "module": "Chapter 10 · Using Variables",
        "one_line": "Most initialisation errors are a variable holding a value you did not expect, and reading a routine line by line for a read before a set, a set twice and a set never used finds the commonest of them.",
        "summary": (
            "Chapter 10 opens Part III with the variable itself: how it is declared and how it "
            "gets its first value. McConnell traces initialisation errors to a value you did "
            "not expect and asks for each variable to be initialised where it is declared, or "
            "close to its first use. Read three versions of a short routine top to bottom, find "
            "the variable read before it is set, the values set twice and thrown away and the "
            "result never used, and say which of them Java's compiler catches."
        ),
        "key": [
            "initialise each variable where it is declared",
            "or as close to its first use as you can",
            "used before set: read with no set above",
            "set twice: two sets with no read between",
            "set, never used: nothing reads the last set",
            "javac rejects any local read before set",
        ],
        "key_label": "Initialisation in six lines",
        "concepts_intro": (
            "Sections 10.1 to 10.3 are short, and the third carries the weight: it says where "
            "initialisation errors come from and how to keep them out."
        ),
        "concepts": [
            ("An unexpected initial value",
             "McConnell's diagnosis of every initialisation error. A variable was never given a "
             "value, or was given one that has since gone stale, or had only part of itself set, "
             "and the code reads it as if it held what you meant."),
            ("The Principle of Proximity",
             "Keep related actions together. Applied to variables it means declaring and "
             "initialising each one close to where it is first used, so that the line that gives "
             "it a value and the lines that rely on that value can be read together."),
            ("A data-flow anomaly",
             "A suspicious order of what happens to a variable, read along the code: used before "
             "anything set it, set twice with no use between, or set and then never used. Section "
             "22.3 names the patterns; finding one is a reason to look, not proof of a bug."),
        ],
        "read_title": "The chapter's opening sections, then three versions of one routine",
        "read_intro": (
            "The lesson sets out what Sections 10.1 to 10.3 argue, then reads one short routine "
            "three ways: with a counter never initialised, with it initialised, and with values "
            "set and thrown away."
        ),
        "body": [
            ("p", "&ldquo;Data initialization is prone to errors, so use the initialization "
                  "techniques described in this chapter to avoid the problems caused by "
                  "unexpected initial values.&rdquo; That is the first of the Key Points with "
                  "which Chapter 10, General Issues in Using Variables, closes on page 258. This "
                  "lesson reads the chapter's first three sections, pages 237 to 243; read them in "
                  "your own copy first. The rest of the chapter, from Section 10.4 on scope, is the "
                  "next lesson."),
            ("p", "Section 10.1 begins with a self-test: a list of data-type terms to score "
                  "yourself against, with a scoring table and a short reading list. Three of the "
                  "terms are made up, and the scoring table has a word for the reader who claims "
                  "to know all of them. The point under the joke is the section's own: you cannot "
                  "use data well without knowing which kinds of data there are."),
            ("p", "Section 10.2 is about declarations. Some languages declare a variable for you "
                  "the first time you use it, and McConnell counts implicit declaration among the "
                  "most dangerous features a language can have: type `acctNo` where you "
                  "meant `acctNum` and you have a second variable, silently initialised, "
                  "and a bug. In a language that requires declarations the "
                  "same slip takes two mistakes, a wrong name and a declaration to match it. "
                  "Java is such a language, so this half of the advice is "
                  "done for you; for the others the section says to turn implicit declarations off "
                  "where the compiler allows it, to declare everything anyway, to adopt naming "
                  "conventions for suffixes such as `Num` and `No`, and to "
                  "read the compiler's list of the variables each routine uses."),
            ("p", "Section 10.3 is the heart of the lesson. Improper initialisation, McConnell "
                  "says, is among the richest sources of error in programming, and every "
                  "case comes down to a variable holding an initial value you did not expect: it "
                  "was never assigned, so it holds whatever was there; or its value is out of date; "
                  "or part of it was assigned and part was not. His guidelines follow from that. "
                  "Initialise each variable as it is declared, which he calls cheap insurance. "
                  "Where you cannot, initialise it close to where it is first used, not in a block "
                  "of initialisations at the top: a loop is later built around the code, the "
                  "initialisation is left outside it, and the second pass starts with the first "
                  "pass's value. That is his Principle of Proximity, keeping related actions "
                  "together. Use `final` for anything that should not change once set. "
                  "Pay special attention to counters and accumulators, which are easy to forget "
                  "to reset before their next use. Check input parameters before you use them, and read your "
                  "compiler's warnings."),
            ("def", ("Three data-flow anomalies",
                     "Chapter 22, in Section 22.3 on data-flow testing (pages 509 and 510), "
                     "names the patterns of what happens to a variable that deserve suspicion. "
                     "This lesson's lab looks for three of them in a local variable: entered and "
                     "used, a read with no set before it; defined and defined again, a set "
                     "followed by another set with no read between; and defined and exited, a set "
                     "that nothing reads.")),
            ("p", "Now the code. Here is a routine that averages an array of prices, written "
                  "with its counter declared and never given a value. It is the "
                  "<code>count-unset</code> preset in the lab below."),
            ("code", {"lines": lines(COUNT_UNSET), "marked": [6]}),
            ("p", "Read it the way the lab does, top to bottom. Line 2 declares "
                  "`count` and gives it no value. Line 6 reads `count` to add "
                  "one to it, and nothing above line 6 has set it. The lab reports one anomaly, "
                  "<code>count (line 6)</code> under Used before set, and marks the line in its "
                  "listing. Java's compiler agrees and goes further: it refuses to compile the "
                  "routine, with the message that `count` might not have been "
                  "initialised. The <code>initialized</code> preset is the same routine with "
                  "`int count = 0;` beside `total`, and the lab reports no "
                  "anomaly at all."),
            ("code", lines(INITIALIZED)),
            ("p", "The <code>set-twice</code> preset is the case Java's compiler lets through. "
                  "Someone has replaced the loop with two assignments and kept the old "
                  "initialisations, and added a variable for the average and then returned the "
                  "expression instead."),
            ("code", {"lines": lines(SET_TWICE), "marked": [4, 5, 6]}),
            ("p", "The lab counts three anomalies. Under Set twice it lists <code>total (lines 2, "
                  "4), count (lines 3, 5)</code>: each was given a value that was overwritten before "
                  "anything read it. Under Set, never used it lists <code>average (line 6)</code>. "
                  "The routine compiles and runs, and it returns the first price divided by the "
                  "number of prices, which is not an average. The lab's last tile, Dependencies, "
                  "lists each line that reads a value next to the line that last set it, "
                  "<code>4&rarr;6</code> meaning that line 6 reads what line 4 wrote; in this "
                  "preset nothing reads line 2 or line 3, which is what Set twice was saying."),
            ("p", "So what does Java's compiler catch? A local variable read before it is "
                  "definitely assigned, on any path through the routine, and that check is "
                  "stronger than this lab's, because the lab reads lines in order and never "
                  "follows a branch. A C or C++ compiler accepts the same mistake, perhaps with a "
                  "warning, and the program reads whatever was in memory. What Java's compiler "
                  "does not question is a value set and thrown away, a variable set and never "
                  "used, or a field: `int count;` declared in a class rather than a "
                  "routine starts at 0 and is read without complaint. That is still an initial "
                  "value nobody chose."),
            ("h3", "Exercise"),
            ("code", lines(INITIALS_EXERCISE)),
            ("p", "This routine builds a person's initials. Read it top to bottom and list every "
                  "anomaly the lab would report, with its line. Then say whether "
                  "`javac` accepts it, and if not, on which path a line reads a "
                  "variable nothing has set. Write your answer down before you paste the routine "
                  "into the lab to check the first half; the quiz has the rest."),
            ("p", "The values a variable holds are one half of Chapter 10. The other half is how "
                  "far apart its uses lie and how long it stays live, which is the next lesson, "
                  "&ldquo;Scope, Span and Live Time&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dataflow",
            "preset": "count-unset",
            "presets": [
                {"id": "count-unset", "label": "A counter never initialised",
                 "code": COUNT_UNSET,
                 "expect": {"coAnomalies": "1", "coUsedBeforeSet": "count (line 6)"}},
                {"id": "initialized", "label": "The counter initialised beside the total",
                 "code": INITIALIZED,
                 "expect": {"coAnomalies": "0", "coUsedBeforeSet": "none", "coSetTwice": "none"}},
                {"id": "set-twice", "label": "Values set twice, and an average never used",
                 "code": SET_TWICE,
                 "expect": {"coAnomalies": "3",
                            "coSetTwice": "total (lines 2, 4), count (lines 3, 5)",
                            "coUnused": "average (line 6)"}},
            ],
            "panel_title": "Reading a routine for data-flow anomalies",
            "panel_intro": (
                "The lab reads the listing line by line and records, for every variable, each "
                "line that sets it and each line that reads it. It reports a read with no set "
                "above it, a set followed by another set with no read between, and a set nothing "
                "reads. It does not follow branches, so it can miss what Java's compiler finds."
            ),
        }),
        "steps_title": "Reading a routine for anomalies",
        "steps_intro": "Five steps; the last is yours.",
        "steps": [
            ("Number the lines",
             "Count every line from 1, the header included, so that each set and each read has "
             "an address you can write down."),
            ("Track each variable",
             "For each variable, list in order the lines that set it (a declaration with a "
             "value, an assignment, a parameter on the header's line) and the lines that read it. "
             "An assignment like `count = count + 1` reads first and then sets."),
            ("Flag the three patterns",
             "A read with no earlier set; a set followed by another set with no read between; a "
             "set with nothing after it. Write each with its variable and line."),
            ("Ask what the compiler does",
             "For each flag, say whether Java's compiler rejects it (a local read before it is "
             "definitely assigned) or accepts it (everything else), and look along every path "
             "through an `if`, which the line-by-line reading does not."),
            ("Read a routine of your own",
             "Paste a routine of your own into the lab and note each anomaly it reports. Compile "
             "the routine and write beside each anomaly whether the compiler rejected it, warned "
             "about it or said nothing."),
        ],
        "worked": {
            "title": "The counter nobody set",
            "intro": [
                "Take the <code>count-unset</code> preset and follow `total` and "
                "`count` down the listing, set by set and read by read.",
            ],
            "lines": [
                "line 2: int count; declares it and sets nothing",
                "line 3: total set to 0.0",
                "line 5: total read, then set",
                "line 6: count read, then set; nothing set it above",
                "line 8: total and count read",
                "anomalies: 1, count used before set on line 6",
            ],
            "after": [
                "One anomaly, and it is the one Java's compiler rejects. Give `count` "
                "a value where it is declared and the lab finds none; the routine is then "
                "correct for any array with at least one price.",
            ],
        },
        "quiz_title": "Initial values",
        "quiz": [
            {"q": "In the exercise's `initials` routine, what does a top-to-bottom "
                  "reading report, and what does `javac` do with the routine?",
             "a": ["Nothing; javac rejects it, because when the if is false line 6 reads result "
                   "before anything sets it",
                   "result used before set on line 6; javac rejects it",
                   "Nothing; javac accepts it, because line 4 sets result",
                   "result set twice, on lines 4 and 6; javac accepts it"],
             "c": 0,
             "why": "Read in order, line 4 sets `result` before line 6 reads it, so "
                    "the lab reports no anomaly; and line 6 reads `result` before "
                    "setting it, so lines 4 and 6 are not two sets with no read between. But on "
                    "the path where `first.length() > 0` is false, line 4 never "
                    "runs and line 6 reads an unset variable. Java's compiler follows both paths "
                    "and rejects the routine (&ldquo;variable result might not have been "
                    "initialized&rdquo;); a C or C++ compiler accepts its equivalent. The lab "
                    "reads top to bottom and so misses it."},
            {"q": "Of the three presets, <code>count-unset</code>, <code>initialized</code> and "
                  "<code>set-twice</code>, which does Java's compiler refuse to compile?",
             "a": ["count-unset only", "set-twice only", "count-unset and set-twice",
                   "None of them"],
             "c": 0,
             "why": "Only <code>count-unset</code> reads a local before it is definitely "
                    "assigned. <code>set-twice</code> compiles: overwriting a value and leaving a "
                    "variable unused are legal Java, though the routine returns the first price "
                    "over the count, which is why the lab reports three anomalies there."},
            {"q": "A local variable is set, then set again with no use between. Which of Section "
                  "22.3's patterns is that?",
             "a": ["Defined-defined", "Entered-used", "Defined-exited", "Used-defined"],
             "c": 0,
             "why": "Defined then defined again is the pattern McConnell calls wasteful and "
                    "error-prone even if not wrong (p. 509). Entered-used is a read before any "
                    "set; defined-exited is a set nothing reads; used-defined is a read followed "
                    "by a set, which is suspicious only if nothing set the variable before the "
                    "read."},
            {"q": "A class declares the field `int hits;` and a method reads it before "
                  "anything assigns it. What happens in Java?",
             "a": ["It compiles, and the read gives 0",
                   "The compiler rejects it, as it does a local",
                   "It compiles, and the read gives whatever was in memory",
                   "It compiles, and the read throws an exception"],
             "c": 0,
             "why": "A field starts at its type's default, 0 for an `int`, and the "
                    "compiler's definite-assignment check applies to locals, not fields. Reading "
                    "leftover memory is C's behaviour for an uninitialised local, not Java's for "
                    "anything."},
        ],
        "mistakes": [
            ("Thinking that if it compiles, every variable holds the value you meant",
             "Java's compiler does reject a local variable read before it is definitely "
             "assigned, on any path, and that is a real check, stronger than this lesson's lab. "
             "But <code>set-twice</code> compiles and throws away two initial values, returning "
             "the first price over the count; and a field declared `int count;` starts "
             "at 0 and is read without a word from the compiler. McConnell's diagnosis is an "
             "initial value you did not expect, and a compiler can only rule out some of the ways "
             "of getting one."),
            ("Initialising everything in a block at the top",
             "It looks orderly, and Section 10.3 argues against it. A block of initialisations "
             "far from the code that uses them suggests that every variable is used throughout "
             "the routine, and when a loop is later built around part of the code, the "
             "initialisation stays outside it. McConnell asks for each variable to be initialised "
             "where it is declared, close to its first use."),
            ("Treating an unused variable as harmless",
             "It does nothing at run time, but Section 10.8 asks you to make sure every declared "
             "variable is used, and the book cites Card, Church and Agresti (1986), who found "
             "unreferenced variables correlated with higher fault rates. An unused variable is "
             "often the sign of code that was meant to use it and does not."),
        ],
        "standard": (
            "Finish when you can find a routine's data-flow anomalies by reading it.",
            "For a short routine, list every variable read before it is set, set twice with no "
            "use between, or set and never used, each with its line, and say which of them Java's "
            "compiler rejects."
        ),
        "note": (
            "The lab reads the lines in order and never follows a branch or a loop; Java's "
            "compiler checks every path, so for locals it is "
            "stronger than the lab, and the exercise is a case only the compiler sees. The lab "
            "also cannot see a value that has gone stale, a field's default, or a variable that "
            "is set correctly and holds the wrong thing."
        ),
    },
    # ---------------------------------------------------------------- 02
    # McConnell Chapter 10, sections 10.4-10.8, pp. 244-258. Quotation:
    # p. 258 (Key Points), 24 words. Span and live time: section 10.4,
    # pp. 245-248.
    # F10, pp. 245-248 (span, live time, the book's 54 against 7).
    {
        "slug": "scope-span-and-live-time",
        "title": "Scope, Span and Live Time",
        "module": "Chapter 10 · Using Variables",
        "one_line": "Keeping each variable's references close together and its life short shrinks the code a reader has to hold in mind, and the book measures both with line numbers.",
        "summary": (
            "The second half of Chapter 10 asks how widely a variable is known and how long it "
            "is in play. McConnell measures the distance between a variable's references, its "
            "span, and the stretch from first reference to last, its live time, and asks for "
            "both to be kept small. Compute both for a routine that declares its variables at "
            "the top, move each declaration to the loop that uses it, and compute them again."
        ),
        "key": [
            "span: lines strictly between two references",
            "live time: last line - first line + 1",
            "declare each variable just before its use",
            "start with the smallest scope that works",
            "one variable, one purpose",
        ],
        "key_label": "Scope in five lines",
        "concepts_intro": (
            "Section 10.4 gives the chapter's two measures, and Sections 10.5 to 10.8 add four "
            "shorter points about a variable's life and purpose."
        ),
        "concepts": [
            ("Scope",
             "How widely a variable is known: within one block, one routine, one class, one "
             "package or the whole program. McConnell's advice is to start with the smallest "
             "scope that works and widen it only when you must."),
            ("Span",
             "The number of lines between two consecutive references to a variable. A variable "
             "referenced on lines 3, 13 and 18 has spans of 9 and 4; its average span is the "
             "mean of its spans."),
            ("Live time",
             "The stretch from a variable's first reference to its last, both lines included: "
             "last minus first plus one. It does not care how often the variable is used in "
             "between, only how long a reader has to keep it in mind."),
        ],
        "read_title": "Section 10.4's two measures, then one routine measured twice",
        "read_intro": (
            "The lesson sets out Section 10.4 and the four sections after it, then measures a "
            "routine before and after its declarations are moved."
        ),
        "body": [
            ("p", "&ldquo;Minimize the scope of each variable. Keep references to a variable "
                  "close together. Keep it local to a routine or class. Avoid global data.&rdquo; "
                  "That is the second of Chapter 10's Key Points, on page 258. This lesson reads "
                  "Sections 10.4 to 10.8, pages 244 to 258; read them in your own copy first."),
            ("p", "Section 10.4 begins with a variable's celebrity: how many places know it. In "
                  "Java a variable can be known to a block, a routine, a class or a whole package, "
                  "and the section's argument is that the less of the program that knows a "
                  "variable, the less of it you need to read to understand that variable. The "
                  "code between two references to a variable is what McConnell calls a &ldquo;window of "
                  "vulnerability&rdquo;: new code can be added there that changes the variable by "
                  "mistake, and a reader can forget what it holds."),
            ("p", "He then makes the idea measurable. A variable's span is the number of lines "
                  "between two consecutive references to it, and its average span is the mean of "
                  "those; its live time is the number of lines from its first reference to its "
                  "last, both included. The two differ: a variable used on every line from 1 to 25 "
                  "has spans of 0 and a live time of 25, and one used only on lines 1 and 25 has a "
                  "span of 23 and the same live time. The section's own example measures a listing "
                  "whose three variables are initialised at the top and averages a live time of "
                  "about 54 lines; with the initialisations moved down beside their loops, the "
                  "average is about 7. McConnell is candid that no one has found the number that "
                  "separates a good live time from a bad one, and he takes it "
                  "that smaller is better."),
            ("p", "The section's guidelines follow. Initialise a loop's variables just before "
                  "the loop, not at the top of the routine. Do not give a variable its value until "
                  "just before the value is used. Group the statements that work on the same "
                  "variables. Break a group out into a routine of its own, where its variables "
                  "cannot live long. And begin with the most restricted visibility, widening it "
                  "only when you must, because it is much harder to make a global variable local "
                  "than the reverse. He frames the disagreement fairly: programmers who make "
                  "variables global value convenience in writing, and those who keep them local "
                  "value being able to understand one routine at a time; his own conclusion is "
                  "that a program is read more than it is written."),
            ("p", "The four shorter sections each add a point. Section 10.5, on persistence, "
                  "warns against assuming a variable lasts longer than it does, and compares it to "
                  "the milk in your refrigerator, which is supposed to keep for a week. Section "
                  "10.6, on binding time, asks when a variable is tied to its value, from coding "
                  "time with a literal, through compile time with a named constant, to the moment "
                  "of use, and notes that later binding buys flexibility at the price of "
                  "complexity. Section 10.7 matches kinds of data to control structures: "
                  "sequential data to a sequence of statements, selective data to an "
                  "`if` or a `case`, iterative data to a loop. Section 10.8 "
                  "asks for each variable to have exactly one purpose, and not, for instance, to be "
                  "a page count that means an error when it is &minus;1."),
            ("p", "You have probably written a routine like `auditShipments`: three "
                  "declarations at the top, set to zero, and then the work, a screen further down. "
                  "It is the <code>declared-at-top</code> preset in the lab below."),
            ("code", lines(DECLARED_AT_TOP)),
            ("p", "Count it for `heaviestKg`: declared on line 3, used on lines 13 and "
                  "18, so its spans are 9 and 4, and it is live for 18 &minus; 3 + 1 = 16 lines, "
                  "nine of which come before it is first used. `scanned` is on lines 2, "
                  "9 and 11, spans 6 and 1, live time 10; `overLimit` on lines 4, 15 and "
                  "18, spans 10 and 2, live time 15. With the three variables in its "
                  "<em>Variables</em> box, the lab prints the average span over all six spans, "
                  "16/3 &asymp; 5.33, the average live time, 41/3 &asymp; 13.67, and the longest "
                  "live time, <code>heaviestKg: 16</code>. The <code>declared-near-use</code> "
                  "preset moves each declaration down to the loop that uses it and changes no "
                  "other statement."),
            ("code", lines(DECLARED_NEAR_USE)),
            ("p", "Now `scanned` is on lines 4, 7 and 9, `heaviestKg` on "
                  "10, 13 and 18, and `overLimit` on 11, 15 and 18. The average span "
                  "falls to 7/3 &asymp; 2.33 and the average live time to 23/3 &asymp; 7.67, and "
                  "the longest is <code>heaviestKg: 9</code>. Nothing about what the program does "
                  "is different; what is different is how much of it you have to hold in your head "
                  "at once, which is the complexity Chapter 5 said was the thing to manage. Notice "
                  "too that each loop's `s` is declared in its own loop header, so Java "
                  "already gives it the smallest scope there is."),
            ("p", "Two differences between the lab and the book are worth knowing. The book "
                  "counts statements, and the lab counts listing lines, blank lines and lines of "
                  "braces included, so the lab's numbers run a little higher than a statement "
                  "count would. And the book averages the spans of one variable; the lab's single "
                  "average over several variables pools all their spans, which is the lab's own "
                  "extension of the measure. Either way the figure tells you where to look, not "
                  "what to do."),
            ("h3", "Exercise"),
            ("code", lines(REPORT_SALES_EXERCISE)),
            ("p", "For `total` and `count`, write down every span, the "
                  "average span over the four spans and each live time. Then move both "
                  "declarations below the four `print` calls, so that they become lines "
                  "6 and 7, and compute the same figures again. You can check both versions in the "
                  "lab afterwards, with `total count` in its Variables box."),
            ("p", "A variable that stays live for few lines is easy to follow only if its name "
                  "says what it holds. The next lesson, &ldquo;The Power of Variable Names&rdquo;, "
                  "reads Chapter 11."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "span",
            "vars": "scanned heaviestKg overLimit",
            "preset": "declared-at-top",
            "presets": [
                {"id": "declared-at-top", "label": "Declared at the top",
                 "code": DECLARED_AT_TOP,
                 "expect": {"coAvgSpan": "16/3 ≈ 5.33", "coAvgLive": "41/3 ≈ 13.67",
                            "coLongest": "heaviestKg: 16"}},
                {"id": "declared-near-use", "label": "Declared near their use",
                 "code": DECLARED_NEAR_USE,
                 "expect": {"coAvgSpan": "7/3 ≈ 2.33", "coAvgLive": "23/3 ≈ 7.67",
                            "coLongest": "heaviestKg: 9"}},
            ],
            "panel_title": "Span and live time",
            "panel_intro": (
                "The lab finds every line on which each named variable appears, computes the "
                "spans between consecutive references and each live time, and averages them. "
                "Leave the Variables box empty to measure every variable the routine sets."
            ),
        }),
        "steps_title": "Measuring span and live time",
        "steps_intro": "Four steps; the last is yours.",
        "steps": [
            ("List each variable's lines",
             "Number every line from 1 and write down, for each variable, the lines on which it "
             "appears, its declaration included."),
            ("Compute the spans",
             "For each pair of consecutive lines, the span is the later minus the earlier minus "
             "one: the lines strictly between. Average them for the variable, or over all the "
             "variables, as the lab does."),
            ("Compute the live times",
             "For each variable, its last line minus its first line plus one. Note which is "
             "longest and how many of its lines come before the first real use."),
            ("Shorten a live time of your own",
             "Paste a routine of your own into the lab with the Variables box empty, find the "
             "variable with the longest live time, move its declaration down to just before its "
             "first use, and note how far its live time falls."),
        ],
        "worked": {
            "title": "heaviestKg, declared at the top",
            "intro": [
                "In <code>declared-at-top</code>, `heaviestKg` appears on lines 3, 13 "
                "and 18.",
            ],
            "lines": [
                "references: lines 3, 13, 18",
                "spans: 13 - 3 - 1 is 9, and 18 - 13 - 1 is 4",
                "average span: 13/2, about 6.5",
                "live time: 18 - 3 + 1 is 16",
                "declared near use, on line 10: 18 - 10 + 1 is 9",
            ],
            "after": [
                "Moving the declaration cuts seven lines from its live time, all of them lines on "
                "which `heaviestKg` held 0 and did nothing.",
            ],
        },
        "quiz_title": "Spans and live times",
        "quiz": [
            {"q": "In the exercise's `reportSales`, what are the average span over "
                  "`total` and `count` and their live times, before and after "
                  "the declarations move to lines 6 and 7?",
             "a": ["3.75 and live times 11 and 10 before; 1.75 and 7 and 6 after",
                   "3.75 and live times 10 and 9 before; 1.75 and 6 and 5 after",
                   "4.75 and live times 11 and 10 before; 2.75 and 7 and 6 after",
                   "3.75 and live times 11 and 10 before; 3.75 and 7 and 6 after"],
             "c": 0,
             "why": "Before, `total` is on lines 2, 9 and 12 (spans 6 and 2) and "
                    "`count` on 3, 10 and 12 (spans 6 and 1): 15/4 = 3.75, live times "
                    "12 &minus; 2 + 1 = 11 and 12 &minus; 3 + 1 = 10. After, `total` is "
                    "on 6, 9 and 12 (spans 2 and 2) and `count` on 7, 10 and 12 (spans 2 "
                    "and 1): 7/4 = 1.75, live times 7 and 6. Leaving out the + 1 gives 10 and 9; "
                    "counting a span as the plain difference of line numbers gives 4.75; and the "
                    "spans do change when a declaration moves."},
            {"q": "A variable is referenced only on line 1 and line 25. What are its span and "
                  "live time, as Section 10.4 counts them?",
             "a": ["Span 23, live time 25", "Span 24, live time 24", "Span 23, live time 24",
                   "Span 0, live time 25"],
             "c": 0,
             "why": "Twenty-three lines lie strictly between lines 1 and 25, and the live time "
                    "counts both ends: 25 &minus; 1 + 1 = 25. These are the book's own figures "
                    "(p. 246). A span of 0 would need a reference on every line between."},
            {"q": "In <code>declared-at-top</code> the lab's average span is 16/3. What has it "
                  "averaged?",
             "a": ["Six spans, two for each of the three variables",
                   "Three spans, one for each variable",
                   "The three live times",
                   "The two spans of heaviestKg"],
             "c": 0,
             "why": "Each variable appears on three lines and so has two spans: 6 and 1, 9 and 4, "
                    "10 and 2, which total 32, and 32/6 = 16/3. Pooling all the spans is the lab's "
                    "extension of the book's per-variable average; the live times average 41/3."},
            {"q": "Section 10.6 lists the times at which a variable can be bound to its value. "
                  "Which of these binds latest?",
             "a": ["Reading the value each time a window is drawn",
                   "A named constant",
                   "A literal typed into the code",
                   "Reading the value from a properties file when the program loads"],
             "c": 0,
             "why": "The section's order runs from coding time (a literal), through compile time "
                    "(a named constant) and load time (a file read at start-up), to object "
                    "creation and finally just in time, each time the value is used. Later "
                    "binding is more flexible and, the section adds, more complex."},
        ],
        "mistakes": [
            ("Declaring every variable at the top so it is easy to find",
             "It is a common habit and has a real reason: one place to look. The chapter's "
             "measure says what it costs. Every line between a declaration and the variable's "
             "first use is a line on which it is live and doing nothing; on the lesson's "
             "illustration the average live time is 41/3, about 13.7 lines, against 23/3, about "
             "7.7, for the same statements with each declaration moved down beside its loop."),
            ("Taking span and live time for the same measure",
             "A variable used on every line from 1 to 25 has spans of 0 and a live time of 25; "
             "one used only on lines 1 and 25 has a span of 23 and the same live time. Span says "
             "how far apart the references are; live time says how long the variable is in play. "
             "Section 10.4 asks for both to be small."),
            ("Reusing a temporary variable for a second job",
             "It saves a declaration and costs a reader. Section 10.8 asks for one purpose per "
             "variable: a `temp` used for two unrelated values makes them look "
             "related, and a count that means an error when it is &minus;1 is, in the book's "
             "words for it, an integer &ldquo;moonlighting as a boolean&rdquo;."),
        ],
        "standard": (
            "Finish when you can compute spans and live times by hand.",
            "Given the lines on which two variables are referenced, compute every span, the "
            "average span and each live time, and say which declaration to move to shrink them."
        ),
        "note": (
            "The lab counts listing lines where the book counts statements, and its pooled "
            "average over several variables is its own extension of the book's per-variable "
            "measure. It reads names, not meanings: a variable reused for two purposes is one "
            "name to the lab, and a short live time says nothing about whether the variable's "
            "scope is wider than it needs to be."
        ),
    },
    # ---------------------------------------------------------------- 03
    # McConnell Chapter 11, sections 11.1-11.7, pp. 259-289. Quotation:
    # p. 289 (Key Points), 23 words.
    # F11, p. 262 (name length, Gorla, Benander and Benander 1990).
    {
        "slug": "the-power-of-variable-names",
        "title": "The Power of Variable Names",
        "module": "Chapter 11 · Variable Names",
        "one_line": "A variable's name should state in words what the variable stands for in the problem, at a length that serves the reader, and the book reports a study in which debugging was easiest when names averaged ten to sixteen characters.",
        "summary": (
            "Chapter 11 argues that a variable and its name are, for a reader, the same thing. "
            "McConnell asks for names that describe the problem rather than the computing, for "
            "conventions that settle the small decisions once, and for short names only where "
            "the scope is short. Average the length of a routine's names, see which fall below "
            "eight characters, and rename them for what they stand for."
        ),
        "key": [
            "say what the variable stands for, in words",
            "name the problem, not the solution",
            "best in the study: names of 10 to 16",
            "short names for short scopes only",
            "names are for the reader, not the writer",
        ],
        "key_label": "Names in five lines",
        "concepts_intro": (
            "Chapter 11 is long and practical; three of its ideas carry the rest."
        ),
        "concepts": [
            ("A full and accurate description",
             "McConnell's most important rule: state in words what the variable represents, "
             "and that statement is often the best name. `linesPerPage` needs no "
             "deciphering; `lpp` does."),
            ("Problem orientation",
             "A good name says what, not how: what the value means in the problem the program "
             "solves, not which computing device holds it. `employeeData` is about the "
             "problem; `inputRec` is about the program."),
            ("A naming convention",
             "A set of decisions about names made once for a whole program or team: how to "
             "tell a constant from a variable, where a qualifier such as `Total` goes, "
             "which abbreviations are allowed. The chapter's claim is that having one matters more "
             "than which one it is."),
        ],
        "read_title": "Chapter 11 section by section, then one routine named twice",
        "read_intro": (
            "The lesson goes through the chapter's seven sections, then measures the names of "
            "one routine written two ways."
        ),
        "body": [
            ("p", "&ldquo;Code is read far more times than it is written. Be sure that the names "
                  "you choose favor read-time convenience over write-time convenience.&rdquo; "
                  "That is one of the Key Points of Chapter 11, The Power of Variable Names, on "
                  "page 289. This lesson reads the whole chapter, pages 259 to 289; read it in "
                  "your own copy first."),
            ("p", "Section 11.1 starts from the claim that a variable is, to a reader, its name, "
                  "so choose the name with care. The most important consideration is that the "
                  "name fully and accurately describe what the variable represents, and the "
                  "technique is to say it in words: the number of seats in a stadium, the current "
                  "date. A good name speaks to the problem rather than the solution, what rather "
                  "than how. The section adds two conventions: put a computed-value qualifier such "
                  "as `Total`, `Max` or `Average` at the end of a "
                  "name, so that `revenueTotal` and `expenseTotal` read alike; "
                  "and use opposites precisely, `first` with `last`, "
                  "`min` with `max`."),
            ("p", "On length the section reports a study. Gorla, Benander and Benander (1990), "
                  "as the book cites them, found the effort to debug a program lowest when its "
                  "variable names averaged 10 to 16 characters, and programs whose names averaged "
                  "8 to 20 almost as easy to debug. McConnell is careful with it: the finding does "
                  "not say that every name should be that long, only that if you see many shorter "
                  "names in your code, check that they are as clear as they need to be. The figure "
                  "is an average over the programs those researchers studied, and your own code "
                  "can be checked against it but is not bound by it. Short names have their place: "
                  "`i` in a three-line loop tells the reader that it is a scratch value "
                  "that matters nowhere else, and the shorter the scope, the shorter a name can "
                  "be."),
            ("p", "Section 11.2 takes particular kinds of data in turn. Loop indexes may be "
                  "`i`, `j` and `k` in a short loop, but a nested "
                  "loop is clearer with names like `teamIndex`, which also prevent "
                  "index cross-talk, writing `i` where you meant `j`. A "
                  "status variable should never be called `flag`. A variable called "
                  "`temp` is often a sign that its writer has not yet understood what it "
                  "holds. A boolean should have a name that is plainly true or false, such as "
                  "`done` or `found`, and a positive one: "
                  "`notFound` negated is hard to read. A constant should be named for "
                  "what it stands for, not for its value."),
            ("p", "Sections 11.3 and 11.4 argue for conventions. They let you make one decision "
                  "for a whole program instead of many small ones, carry knowledge between "
                  "projects, and stop the same thing being called `pointTotal` here and "
                  "`totalPoints` there; McConnell's point is that a convention's power "
                  "comes from its existing, more than from its particular choices. Section 11.5 "
                  "describes standardized prefixes, of which the Hungarian convention once "
                  "widely used in Windows programming is the best known: short codes for a "
                  "program's own types combined with prefixes for a variable's role, such as a "
                  "count or an index. The section notes that the Hungarian convention is no longer "
                  "in widespread use, holds that the idea of terse, precise prefixes still has "
                  "value, and warns that a prefix is no substitute for a meaningful name."),
            ("p", "Section 11.6 calls the habit of short names a remnant of an earlier age, when "
                  "languages limited names to a few characters, and gives guidelines for "
                  "abbreviating when you must: consistently, pronounceably, never by dropping a "
                  "single letter. Section 11.7 lists names to avoid: names with similar meanings, "
                  "names a letter apart, numerals, misspellings, and names that differ only in "
                  "capitals. It includes names that sound alike, and McConnell's example is "
                  "Extreme Programming's Goal Donor and Gold Owner, with a spoken exchange about "
                  "them that is worth reading in the book."),
            ("p", "Now the code. Here is a routine named for its arithmetic. It is the "
                  "<code>short-names</code> preset in the lab below, which counts names shorter "
                  "than eight characters, the lower end of the range the study found almost as "
                  "good."),
            ("code", lines(SHORT_NAMES)),
            ("p", "The lab finds seven declared names: the parameters `a`, "
                  "`n` and `r`, the locals `t`, `x` "
                  "and `tmp`, and the loop index `i`, which it lists and "
                  "leaves out of the average, as Section 11.2 allows. The other six total eight "
                  "characters, so the mean length is 8/6 = 4/3 &asymp; 1.33, and all six are shorter "
                  "than the minimum: <code>a, n, r, t, x, tmp</code>. Nothing in the routine says "
                  "what it computes. The <code>problem-names</code> preset is the same routine "
                  "named for its problem."),
            ("code", lines(PROBLEM_NAMES)),
            ("p", "The lab again finds seven names, with `i` again listed and not "
                  "counted. The six counted names total 56 characters, a mean of 28/3 &asymp; 9.33, "
                  "and none is shorter than eight. The routine now says what it is for: an average "
                  "net price, from gross prices and a net factor. The study's figure is an average "
                  "over a whole program and the lab's list of short names is its own reading of it, "
                  "name by name; a list of short names is a list of names to look at, and "
                  "`i` in a short loop is the kind you will look at and keep."),
            ("h3", "Exercise"),
            ("code", lines(INTEREST_EXERCISE)),
            ("p", "This routine computes the simple interest on a loan. List its declared names "
                  "with their lengths and compute the mean length, leaving out the loop index and "
                  "the routine's own name, as the lab does. Then rename the routine and every "
                  "short name for what it stands for, compute the mean again and say which names "
                  "are still under eight characters. Paste your version into the lab to check "
                  "it."),
            ("p", "Names tell a reader what a value means; types decide what values it can hold. "
                  "The next lesson, &ldquo;Integers and Floating Point&rdquo;, reads the first "
                  "half of Chapter 12."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "names",
            "min": 8,
            "preset": "short-names",
            "presets": [
                {"id": "short-names", "label": "Named for the arithmetic",
                 "code": SHORT_NAMES,
                 "expect": {"coNames": "7", "coAvgLen": "4/3 ≈ 1.33",
                            "coShort": "a, n, r, t, x, tmp"}},
                {"id": "problem-names", "label": "Named for the problem",
                 "code": PROBLEM_NAMES,
                 "expect": {"coNames": "7", "coAvgLen": "28/3 ≈ 9.33", "coShort": "none"}},
            ],
            "panel_title": "The length of a routine's names",
            "panel_intro": (
                "The lab lists the routine's parameters and declared variables, leaves loop "
                "indexes out of the count, averages the length of the rest and lists those "
                "shorter than this lesson's minimum of eight characters. It measures length only; "
                "whether a name describes the problem is for you to judge."
            ),
        }),
        "steps_title": "Measuring and renaming",
        "steps_intro": "Four steps; the last is yours.",
        "steps": [
            ("List the declared names",
             "Write down every parameter and declared variable with its length in characters, "
             "and mark the loop indexes, which you leave out of the average."),
            ("Average the rest",
             "Add the lengths of the names you count and divide by how many there are. Compare "
             "the mean with the range the study found, 10 to 16 characters, and note which names "
             "fall under eight."),
            ("Rename for the problem",
             "For each short name, say in words what the variable stands for in the problem, "
             "and make that the name, shortening only where the words are needlessly long."),
            ("Rename a routine of your own",
             "Paste a routine of your own into the lab, note its mean name length and the names "
             "it lists as short, rename those for the problem, and paste it again to see the new "
             "mean."),
        ],
        "worked": {
            "title": "The names of averageNetPrice",
            "intro": [
                "In <code>problem-names</code>, the counted names are the three parameters and "
                "three locals; the loop index is left out.",
            ],
            "lines": [
                "grossPrices 11, priceCount 10, netFactor 9",
                "netTotal 8, netPrice 8, averageNet 10",
                "total: 11 + 10 + 9 + 8 + 8 + 10 gives 56",
                "mean: 56 / 6 is 28/3, about 9.33",
                "under eight characters: none",
            ],
            "after": [
                "The mean is inside the range the study found almost as good, 8 to 20, and just "
                "below the one it found best. That is a reason to look at the shortest names, "
                "not to lengthen them.",
            ],
        },
        "quiz_title": "Names and their lengths",
        "quiz": [
            {"q": "In the exercise's routine, leaving out the loop index and the routine's own "
                  "name, what is the mean name length, and what is it after renaming the "
                  "routine <code>simpleInterest(double principal, int months, double "
                  "annualRate)</code> with locals `monthlyInterest` and "
                  "`totalInterest`?",
             "a": ["1, then 53/5 = 10.6, with only months under eight",
                   "1, then 53/5 = 10.6, with no name under eight",
                   "1, then 54/6 = 9, counting the loop index i",
                   "1, then 67/6, about 11.17, counting the routine's name"],
             "c": 0,
             "why": "Before, the five counted names `p`, `n`, "
                    "`r`, `m` and `t` are one character each: "
                    "5/5 = 1. After, `principal` 9, `months` 6, "
                    "`annualRate` 10, `monthlyInterest` 15 and "
                    "`totalInterest` 13 total 53: 53/5 = 10.6, and "
                    "`months`, at six characters, is the one name under eight. "
                    "Counting `i` gives 54/6 = 9, and counting "
                    "`simpleInterest`, 14 characters, gives 67/6."},
            {"q": "What did the study the book reports on name length find?",
             "a": ["Debugging effort was lowest when names averaged 10 to 16 characters, and "
                   "almost as low at 8 to 20",
                   "Every name should be at least 10 characters long",
                   "The longer a program's names, the easier it was to debug",
                   "Debugging effort was lowest when names averaged 8 to 20 characters, and "
                   "almost as low at 10 to 16"],
             "c": 0,
             "why": "Gorla, Benander and Benander (1990), as the book reports them on page 262: "
                    "lowest at a 10 to 16 character average, almost as low at 8 to 20. It is an "
                    "average over a program, not a rule for each name, and it is a range, not a "
                    "direction; the other two options turn it into one, and the last swaps the "
                    "ranges."},
            {"q": "Under Section 11.1's convention for computed-value qualifiers, which set of "
                  "names is consistent?",
             "a": ["revenueTotal, expenseTotal, revenueAverage",
                   "totalRevenue, expenseTotal, revenueAverage",
                   "totalRevenue, totalExpense, averageRevenue",
                   "revenueTotal, totalExpense, averageRevenue"],
             "c": 0,
             "why": "The section puts a qualifier such as `Total` or "
                    "`Average` at the end, so the part of the name that carries its "
                    "meaning comes first. The third option is consistent, but with the opposite "
                    "convention; the second and fourth mix the two."},
            {"q": "Section 11.2 discusses loop indexes. When does it advise a name longer than "
                  "`i`?",
             "a": ["When the loops are nested, or the index is used outside the loop",
                   "Always: a single letter is never acceptable",
                   "Only when the loop runs more than ten times",
                   "Never: i, j and k are the established names"],
             "c": 0,
             "why": "The section accepts `i`, `j` and `k` for "
                    "simple loops and asks for descriptive names when a loop is nested or long, "
                    "or when the value is needed after the loop, as with a record count. How many "
                    "times a loop runs is not its criterion."},
        ],
        "mistakes": [
            ("Thinking that longer names are always better",
             "The study the book reports found a range, not a direction: debugging was easiest "
             "when names averaged 10 to 16 characters and almost as easy at 8 to 20, and Section "
             "11.1's own examples of names that are too long run past thirty characters. The "
             "chapter keeps short names where the scope is short, `i` in a simple loop "
             "above all, because there the shortness itself tells the reader the value matters "
             "nowhere else."),
            ("Letting a prefix stand in for a name",
             "Section 11.5 warns of exactly this: a standardized prefix such as one for an index "
             "into an array of paragraphs says what kind of thing a variable is, and it is "
             "tempting to stop there. McConnell asks you to add the descriptive part as well, so "
             "that the name says which index it is."),
            ("Abbreviating to save the reader time",
             "An abbreviation saves the writer a few keystrokes and costs every reader the "
             "decoding. Section 11.6 asks for abbreviations that are standard, consistent and "
             "pronounceable, and argues that over a program's life its names are read far "
             "more often than they are typed."),
        ],
        "standard": (
            "Finish when you can measure and rename a routine's names.",
            "For a routine, list its declared names with their lengths, compute the mean "
            "without loop indexes, and propose a name for each one under eight characters that "
            "says what it stands for in the problem."
        ),
        "note": (
            "The lab measures length and cannot tell whether a name describes the problem: "
            "`someDataValue` passes it. On prefixes the book and later practice differ. "
            "Section 11.5 holds that terse standardized prefixes add precision, as with the "
            "distinctions between first, last, limit and maximum, and can catch type mistakes a "
            "compiler cannot. Many teams now drop type prefixes, because an editor shows a "
            "variable's type and scope on demand and Java's own conventions use none, while "
            "others keep a few prefixes for role or scope. The lesson does not settle it."
        ),
    },
    # ---------------------------------------------------------------- 04
    # McConnell Chapter 12, sections 12.1-12.3, pp. 291-296 (and the top of
    # p. 297). Quotation: p. 295, 29 words (body text; a margin epigraph sits
    # beside it). The 0.1-ten-times example:
    # pp. 295-296.
    # F12, p. 292 (only 0 and 1 in a program's body).
    {
        "slug": "integers-and-floating-point",
        "title": "Integers and Floating Point",
        "module": "Chapter 12 · Fundamental Data Types",
        "one_line": "Java's int and long overflow silently, integer division truncates, and a double holds the nearest binary fraction rather than a decimal one, so arithmetic that is right on paper can be wrong in code.",
        "summary": (
            "The first half of Chapter 12 is about numbers: magic numbers, division by zero and "
            "conversions, then integers, which divide and overflow in ways arithmetic does not, "
            "and floating-point numbers, which cannot hold most decimal fractions exactly. Have "
            "the lab do Java's int, long and double arithmetic beside the exact result, and see "
            "where they part."
        ),
        "key": [
            "an int holds -2147483648 to 2147483647",
            "past either end it wraps, with no error",
            "integer division drops the remainder",
            "doubles hold the nearest binary fraction",
            "count money in whole cents",
        ],
        "key_label": "Numbers in five lines",
        "concepts_intro": (
            "Sections 12.1 to 12.3 are a list of guidelines; three facts about Java underlie "
            "them."
        ),
        "concepts": [
            ("Integer overflow",
             "A Java `int` is 32 bits and holds −2,147,483,648 to 2,147,483,647. A "
             "sum or product past either end wraps around to the other, silently. A "
             "`long` holds 64 bits and wraps much further out."),
            ("Integer division",
             "Dividing one integer by another drops the remainder: `7 / 2` is 3 in "
             "Java, truncated toward zero. Multiply before you divide where you can."),
            ("Binary floating point",
             "A `double` stores the nearest fraction whose denominator is a power of "
             "two. Most decimal fractions, 0.1 among them, have no such form, so the stored value "
             "is close and not equal, and the small errors add up."),
        ],
        "read_title": "Sections 12.1 to 12.3, then Java's arithmetic beside the exact",
        "read_intro": (
            "The lesson sets out the three sections, then has the lab do Java's arithmetic on "
            "six cases and compare each with the exact result."
        ),
        "body": [
            ("p", "&ldquo;Floating-point numbers that should be equal are not always equal. The "
                  "main problem is that two different paths to the same number don’t always lead "
                  "to the same number.&rdquo; That is from Section 12.3, on page 295 of Chapter "
                  "12, Fundamental Data Types. This lesson reads Sections 12.1 to 12.3, pages 291 "
                  "to 297; read them in your own copy first. The rest of the chapter is the next "
                  "lesson."),
            ("p", "Section 12.1 gives guidelines for numbers in general. Avoid magic numbers, "
                  "literals that appear in the middle of the code without explanation, because "
                  "named constants make changes more reliable, changes easier and the code more "
                  "readable; the section's rule of thumb is that the only literals in a program's "
                  "body should be 0 and 1, which the next lesson takes up. Anticipate division by "
                  "zero wherever a denominator could be 0. Make type conversions obvious, avoid "
                  "comparing values of mixed types, and pay attention to your compiler's warnings, "
                  "which, McConnell says, top programmers fix rather than ignore."),
            ("p", "Section 12.2 is about integers. Integer division does not give the fraction: "
                  "7 divided by 10 is 0, so ten times seven-tenths is 0 where arithmetic says 7, "
                  "and the remedy is to reorder the expression so that the division comes last. "
                  "Integer overflow is the other danger. The section's method is to think through "
                  "each term of an expression, imagine the largest value it can take, and check "
                  "that the result fits, allowing for the program's growth; and to remember that "
                  "an intermediate result can overflow even when the final one would fit, as the "
                  "section's own Java example shows when a product of two millions divided by a "
                  "million prints a small negative number."),
            ("def", ("Wrapping",
                     "Java's `int` and `long` are fixed-width, two's "
                     "complement integers. When a result passes the largest value, Java keeps the "
                     "low 32 or 64 bits and carries on: one more than 2,147,483,647 is "
                     "−2,147,483,648, with no error and no warning. A C compiler may do the same "
                     "or something stranger, because signed overflow is undefined there; a Python "
                     "integer grows instead and never overflows.")),
            ("p", "Section 12.3 is about floating point. Many decimal fractions cannot be "
                  "represented exactly in binary, so adding numbers of very different sizes can "
                  "lose the small one, and two values that should be equal often are not: the "
                  "section's example is 0.1 added ten times, which does not equal 1.0. Compare "
                  "floating-point values within a tolerance instead of with "
                  "`==`. For rounding errors, use a type with more precision, a "
                  "decimal type, or integers counting the smallest unit, such as cents, behind a "
                  "class that hides the representation. In Java the decimal type is "
                  "`BigDecimal`."),
            ("p", "Now the lab. You give it a type, a starting value, an operation, an operand "
                  "and a number of times, and it does what Java would, printing the result as "
                  "`System.out.println` would print it, under Java prints. Beside it is "
                  "the exact result, under Exact arithmetic, a tile saying whether the two are the "
                  "same, and the value Java actually stored, in full. It simulates Java's types exactly rather "
                  "than running Java."),
            ("p", "The <code>int-max-plus-one</code> preset adds 1 to 2147483647, the largest "
                  "`int`. Java prints <code>-2147483648</code>; the exact sum is "
                  "2,147,483,648; they are not the same. The <code>square-overflow</code> preset "
                  "multiplies 46341 by itself: the exact product is 2,147,488,281, just past the "
                  "largest `int`, and Java prints <code>-2147479015</code>. The "
                  "<code>long-square</code> preset does the same multiplication in a "
                  "`long` and prints <code>2147488281</code>, the same as the exact "
                  "value. The <code>int-division</code> preset divides 7 by 2: Java prints "
                  "`3`, against an exact 7/2 = 3.50."),
            ("p", "The <code>tenth-ten-times</code> preset is the book's own example from page "
                  "295: start at 0 and add 0.1 ten times in a `double`. Java prints "
                  "<code>0.9999999999999999</code>, the exact sum is 1, and they are not the same. "
                  "The stored value is shown in full as 9007199254740991/9007199254740992, one "
                  "part in about nine quadrillion short of 1. The <code>cents</code> preset is "
                  "the chapter's remedy: count in whole cents, add 10 cents ten times in an "
                  "`int`, and Java prints `100`, exactly."),
            ("p", "Overflow in an intermediate result is easy to write without noticing. Here is "
                  "a line that computes the milliseconds in a year."),
            ("code", lines(MS_PER_YEAR)),
            ("p", "Java multiplies left to right in `int`. The first four factors give "
                  "31,536,000 seconds, which fits; multiplying by 1000 gives 31,536,000,000, which "
                  "does not, and the line prints <code>1471228928</code>. You can see it in the "
                  "lab by multiplying 31536000 by 1000 as an `int`. The fix is to "
                  "declare `msPerYear` as a `long` and write the last factor "
                  "as <code>1000L</code>, so that the multiplication that overflows is done in "
                  "`long`."),
            ("h3", "Exercise"),
            ("code", lines(OVERFLOW_EXERCISE)),
            ("p", "Without the lab, say whether `total` overflows, in which "
                  "direction it wraps, and how to fix the code; you need not work out the wrapped "
                  "value by hand. Then check in the lab: type `int`, start 0, "
                  "operation +, operand 3000000, 1000 times."),
            ("p", "Rooting out the literals in this lesson's snippets is the subject of the next "
                  "lesson, &ldquo;Named Constants and Other Types&rdquo;, which reads the rest of "
                  "Chapter 12."),
        ],
        "lab": ("cckit", {
            "mode": "run",
            "view": "arith",
            "preset": "int-max-plus-one",
            "presets": [
                {"id": "int-max-plus-one", "label": "The largest int, plus 1",
                 "type": "int", "start": "2147483647", "op": "+", "operand": "1",
                 "expect": {"nuJava": "-2147483648", "nuEqual": "no"}},
                {"id": "square-overflow", "label": "46341 squared, as an int",
                 "type": "int", "start": "46341", "op": "*", "operand": "46341",
                 "expect": {"nuJava": "-2147479015", "nuEqual": "no"}},
                {"id": "long-square", "label": "46341 squared, as a long",
                 "type": "long", "start": "46341", "op": "*", "operand": "46341",
                 "expect": {"nuJava": "2147488281", "nuEqual": "yes"}},
                {"id": "int-division", "label": "7 / 2, as ints",
                 "type": "int", "start": "7", "op": "/", "operand": "2",
                 "expect": {"nuJava": "3", "nuEqual": "no"}},
                {"id": "tenth-ten-times",
                 "label": "0.1 added ten times, as a double (the book's example, p. 295)",
                 "type": "double", "start": "0", "op": "+", "operand": "0.1", "times": 10,
                 "expect": {"nuJava": "0.9999999999999999", "nuEqual": "no"}},
                {"id": "cents", "label": "10 cents added ten times, as an int",
                 "type": "int", "start": "0", "op": "+", "operand": "10", "times": 10,
                 "expect": {"nuJava": "100", "nuEqual": "yes"}},
            ],
            "panel_title": "Java's arithmetic beside the exact result",
            "panel_intro": (
                "The lab repeats one operation on a starting value, as Java would in the type "
                "you choose, and prints what Java would print beside the exact result. It "
                "simulates int and long wrapping and double rounding exactly; it does not run "
                "Java."
            ),
        }),
        "steps_title": "Checking an expression's range",
        "steps_intro": "Four steps; the last is yours.",
        "steps": [
            ("Find each term's largest value",
             "For every variable in the expression, write down the largest value it can "
             "plausibly take, allowing for the program's growth, as Section 12.2 asks."),
            ("Compute the largest result, and every step to it",
             "Multiply or add those largest values in the order Java evaluates them, and note "
             "the largest intermediate result as well as the final one."),
            ("Compare with the type's limit",
             "An `int` holds 2,147,483,647 and a `long` about 9.2 × "
             "10<sup>18</sup>. Anything past the limit wraps; choose a wider type, or write a "
             "`long` literal so the step that overflows is done in "
             "`long`."),
            ("Check a counter of your own",
             "Pick one counter, sum or product in your own code, write down its largest "
             "plausible value, and put that value into the lab in its declared type to see "
             "whether Java prints it unchanged."),
        ],
        "worked": {
            "title": "46341 squared",
            "intro": [
                "The <code>square-overflow</code> preset multiplies 46341 by itself as an "
                "`int`.",
            ],
            "lines": [
                "exact: 46341 * 46341 is 2147488281",
                "2 to the power 31 is 2147483648",
                "so the product is 2147483648 + 4633",
                "past 2147483647 an int wraps down by 4294967296",
                "2147488281 - 4294967296 is -2147479015",
            ],
            "after": [
                "The product is only 4,633 past what an `int` can hold, and it comes "
                "out as a large negative number. In a `long` the same product fits "
                "and prints exactly.",
            ],
        },
        "quiz_title": "Java's numbers",
        "quiz": [
            {"q": "The exercise adds 3000000 to an `int` total a thousand times. What "
                  "does it print, and what fixes it?",
             "a": ["-1294967296; declare total as a long",
                   "3000000000; nothing needs fixing",
                   "It throws an ArithmeticException; catch the exception",
                   "2147483647; Java stops at the largest int"],
             "c": 0,
             "why": "The exact total, 3,000,000,000, is larger than "
                    "`Integer.MAX_VALUE`, 2,147,483,647, so the `int` wraps "
                    "past the top to a negative number: Java prints <code>-1294967296</code>. "
                    "Java neither throws on integer overflow nor stops at the limit. Declared "
                    "`long`, the total prints <code>3000000000</code>."},
            {"q": "Which of these `int` expressions overflows in Java?",
             "a": ["46341 * 46341", "46340 * 46340", "65535 * 32768", "1000000 + 2000000000"],
             "c": 0,
             "why": "46341² is 2,147,488,281, past 2,147,483,647. The others fit: 46340² is "
                    "2,147,395,600, 65535 × 32768 is 2,147,450,880, and the sum is "
                    "2,001,000,000."},
            {"q": "In a `double`, 0.1 is added ten times to 0.0 and the result is "
                  "compared with 1.0 using `==`. What happens?",
             "a": ["The comparison is false; the sum prints as 0.9999999999999999",
                   "The comparison is true",
                   "The comparison is false; the sum prints as 1.0000000000000002",
                   "The comparison is false, because 1.0 cannot be stored exactly"],
             "c": 0,
             "why": "This is the book's example (pp. 295–296): the sum is "
                    "0.9999999999999999, so `==` is false. The error is in 0.1, "
                    "which has no exact binary form; 1.0 is stored exactly."},
            {"q": "What does Java give for `7 / 2` when both are `int`?",
             "a": ["3", "3.5", "4", "3.0"],
             "c": 0,
             "why": "Integer division drops the remainder, truncating toward zero: 3, an "
                    "`int`. 3.5 needs a floating-point operand, 4 would be rounding, "
                    "and 3.0 is a `double`."},
        ],
        "mistakes": [
            ("Believing that a double holds 0.1",
             "It holds the nearest binary fraction, which is a little more than 0.1, and the lab "
             "prints the stored value exactly. Ten of them add up to 0.9999999999999999, not 1, "
             "which is the book's own example on page 295. Counting money in whole cents, as the "
             "<code>cents</code> preset does, is the remedy Section 12.3 gives, and "
             "`BigDecimal` is Java's decimal type."),
            ("Expecting Java to stop on integer overflow",
             "It does not. An `int` or `long` past its limit wraps to the "
             "other end with no exception and no warning; only integer division by zero throws. "
             "Section 12.2's method is to think through each term's largest value before the "
             "code runs."),
            ("Expecting integer division to round",
             "It truncates: `7 / 2` is 3, and Section 12.2 points out that ten times "
             "seven-tenths is 0 in integer arithmetic, because seven-tenths is 0 before the "
             "multiplication happens. Reorder the expression so that the division comes last."),
        ],
        "standard": (
            "Finish when you can predict where Java's arithmetic parts from the exact result.",
            "For an `int` sum or product, say whether it overflows and in which "
            "direction, and name the fix, a `long` or a `long` literal; for "
            "a decimal fraction added ten times as a `double`, say whether the result "
            "equals the exact one and why."
        ),
        "note": (
            "The lab repeats one operation on one value; it does not evaluate a whole "
            "expression, mix types, or follow Java's promotion rules, so the "
            "`msPerYear` case has to be split into steps by hand. It prints doubles as "
            "JDK 19 and later print them, and it cannot say whether an error of one part in "
            "nine quadrillion matters in your program: that depends on what you do with the "
            "value."
        ),
    },
    # ---------------------------------------------------------------- 05
    # McConnell Chapter 12, sections 12.4-12.9, pp. 297-318. Quotation:
    # p. 309, 22 words. "Safe" literals: pp. 308-309. The 0-and-1 rule:
    # Java's enumerated types: margin note, p. 307.
    # F12, p. 292 (only 0 and 1 in a program's body).
    {
        "slug": "named-constants-and-other-types",
        "title": "Named Constants and Other Types",
        "module": "Chapter 12 · Fundamental Data Types",
        "one_line": "A literal in the body of a routine hides what it means and where else it must change, so the book asks for a named constant for every literal but 0 and 1, even the safe ones.",
        "summary": (
            "The second half of Chapter 12 runs through characters and strings, booleans, "
            "enumerated types, named constants, arrays and types of your own. Its sharpest "
            "advice is about literals: give each a name, even when you are sure it will never "
            "change. List a routine's magic numbers with their lines and replace them with "
            "constants."
        ),
        "key": [
            "magic number: an unnamed literal",
            "only 0 and 1 belong in the body",
            "even safe literals get names",
            "one constant, one place to change it",
            "name what it stands for, not its value",
        ],
        "key_label": "Constants in five lines",
        "concepts_intro": (
            "Six short sections, and one idea runs through most of them: say what a value means "
            "in the code itself."
        ),
        "concepts": [
            ("A magic number",
             "A literal such as `360` or `0.0725` that appears in the "
             "middle of the code with nothing to say what it is. Strings and characters can be "
             "magic too."),
            ("A named constant",
             "A name bound to a value that cannot change once set; in Java a <code>static "
             "final</code> field. It says what the value means and gives it a single point of "
             "control: change it once and every use follows."),
            ("An enumerated type",
             "A type whose values are a fixed list of names, such as the months of the year, "
             "instead of numbers that stand for them. In Java it is an `enum`."),
        ],
        "read_title": "Sections 12.4 to 12.9, then one routine with and without constants",
        "read_intro": (
            "The lesson sets out the six sections, then lists the literals in a mortgage "
            "calculation and replaces them."
        ),
        "body": [
            ("p", "&ldquo;Even if you think a literal is safe, use named constants instead. Be a "
                  "fanatic about rooting out literals in your code.&rdquo; That is from Section "
                  "12.7, on page 309. This lesson reads Sections 12.4 to 12.9, pages 297 to 318; "
                  "read them in your own copy first."),
            ("p", "Section 12.4, on characters and strings, begins where the previous lesson's "
                  "section on numbers did: avoid magic characters and strings. A literal string "
                  "may need to change, may need translating, takes space, and says nothing about "
                  "why it is there; a constant called `ESCAPE` is clearer than the "
                  "character code it stands for. The rest of the section is about off-by-one "
                  "errors in substrings and, for C, Unicode and safe string routines; in Java "
                  "every string is Unicode."),
            ("p", "Section 12.5 uses boolean variables to document a program: assign each part "
                  "of a complicated test to a boolean whose name says what it checks, and the "
                  "`if` reads as a sentence. Section 12.6 recommends enumerated types "
                  "over schemes in which 1 stands for red and 2 for green, for readability, for "
                  "parameters whose meaning is otherwise a guess, and for checking that a value is "
                  "one of the allowed ones. Its margin note says that Java has no enumerated types "
                  "as the book is written and probably will by the time it is read; Java 5 added "
                  "`enum` the same year."),
            ("p", "Section 12.7 is the lesson's centre. A named constant parameterises a "
                  "program, putting something that might change where it can be changed once; "
                  "McConnell calls this single-point control. Use named constants in declarations, "
                  "such as the length of an array. Avoid literals even when they seem safe: a loop "
                  "to 12 is probably over months, but the section asks whether you would bet on "
                  "it, and a constant removes the doubt. Use each constant consistently, because a "
                  "constant in one place and the same literal in another is a change waiting to "
                  "be missed. Section 12.1's rule of thumb, that the only literals in a "
                  "program's body should be 0 and 1, is the measure this lesson's lab applies."),
            ("p", "This is where many readers part company with McConnell, over the "
                  "`2` in a midpoint or the `100` in a percentage. The "
                  "chapter's position is plain: name even the safe ones, and search your code for "
                  "the digits 2 to 9 to make sure none has slipped in. The lab follows the book "
                  "and counts every literal but 0 and 1."),
            ("p", "Section 12.8 is about arrays: keep every index within bounds, consider a "
                  "container accessed in sequence instead, check the first and last elements, and "
                  "watch for index cross-talk in nested loops. Section 12.9 recommends creating "
                  "your own types, with C's `typedef` as its main example, so that "
                  "changing a representation is one edit; in Java the same idea is a small class, "
                  "which Chapter 6's lessons covered."),
            ("p", "Now the code. Here is a routine that computes a monthly mortgage payment. It "
                  "is the <code>magic</code> preset in the lab below."),
            ("code", {"lines": lines(MAGIC), "marked": [2, 3, 4, 5]}),
            ("p", "The lab counts a numeric literal other than 0 and 1 on any line that does not "
                  "declare a `final`. It finds five magic numbers, three of them "
                  "distinct, and lists each with its lines: <code>0.0725 (line 2), 12 (lines 2, 3), "
                  "360 (lines 4, 5)</code>. The two 12s mean the same thing, months in a year, and "
                  "the two 360s mean the longest term in months; change the term in one place and "
                  "you have to remember the other. The single `0.0725` is not repeated, "
                  "and still does not say that it is an annual interest rate. The "
                  "`1`s in `1 + rate` and `factor - 1` are part of "
                  "the formula and are not counted."),
            ("code", lines(NAMED)),
            ("p", "The <code>named</code> preset declares the three constants as <code>static "
                  "final</code> fields at the top, and the lab finds no magic number. "
                  "`0.0725 / 12` has become `ANNUAL_RATE / MONTHS_PER_YEAR`, "
                  "and the cap on the term is now one line with `Math.min`. What the "
                  "lab cannot see is whether a name is good: `TWELVE` would satisfy it "
                  "as well as `MONTHS_PER_YEAR`, and Chapter 11 asked for a constant to "
                  "be named for what it stands for, not for its value."),
            ("h3", "Exercise"),
            ("code", lines(WATCH_EXERCISE)),
            ("p", "This loop watches the patients on a ward. List every magic number in it with "
                  "its line, say how many are distinct, and write a `static final` "
                  "declaration with a name for each. Paste your version into the lab to check "
                  "that it finds none."),
            ("p", "Chapter 12 ends with types you make yourself. Chapter 13 turns to the unusual "
                  "ones, and to global data, in the course's last lesson, &ldquo;Structures, "
                  "Pointers and Global Data&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "literals",
            "preset": "magic",
            "presets": [
                {"id": "magic", "label": "Magic numbers in a mortgage payment",
                 "code": MAGIC,
                 "expect": {"coMagic": "5", "coDistinct": "3",
                            "coMagicList": "0.0725 (line 2), 12 (lines 2, 3), 360 (lines 4, 5)"}},
                {"id": "named", "label": "The same with named constants",
                 "code": NAMED,
                 "expect": {"coMagic": "0", "coMagicList": "none"}},
            ],
            "panel_title": "Magic numbers",
            "panel_intro": (
                "The lab lists every numeric literal other than 0 and 1 outside a final "
                "declaration, with the lines it appears on, and counts them and the distinct "
                "values. It does not count strings or characters, and it cannot judge a "
                "constant's name."
            ),
        }),
        "steps_title": "Rooting out literals",
        "steps_intro": "Four steps; the last is yours.",
        "steps": [
            ("List the literals",
             "Go through the routine and write down every numeric literal other than 0 and 1, "
             "with the line it is on. Note strings and characters as well; the lab does not."),
            ("Group them by meaning",
             "Two literals with the same value and the same meaning are one constant; the same "
             "value with two meanings is two constants."),
            ("Name and declare each",
             "Write a `static final` declaration for each, named for what it stands "
             "for in the problem, and replace every use."),
            ("Declare constants in your own code",
             "Paste a routine of your own into the lab, declare a named constant for each "
             "literal it lists, replace the literals, and paste it again until the lab finds "
             "none or you can say why a literal should stay."),
        ],
        "worked": {
            "title": "Naming the rate",
            "intro": [
                "In <code>magic</code>, line 2 holds two of the five literals.",
            ],
            "lines": [
                "line 2: double rate = 0.0725 / 12;",
                "0.0725 is the annual rate: ANNUAL_RATE",
                "12 is months per year: MONTHS_PER_YEAR",
                "line 2 becomes: ANNUAL_RATE / MONTHS_PER_YEAR",
                "line 3 uses MONTHS_PER_YEAR too",
            ],
            "after": [
                "One constant now carries both 12s, and a reader of line 2 no longer has to "
                "guess that the routine works in monthly terms.",
            ],
        },
        "quiz_title": "Literals and constants",
        "quiz": [
            {"q": "How many magic numbers does the exercise's `watchWard` contain, "
                  "counting as the lab does, and how many are distinct?",
             "a": ["3 magic numbers, 3 distinct: 38.5, 3 and 900",
                   "2: 3 and 900, because 38.5 is not a whole number",
                   "3 magic numbers, 2 distinct, because 3 and 900 are both settings",
                   "None, because each literal is used once"],
             "c": 0,
             "why": "`38.5` on line 4, `3` on line 5 and `900` "
                    "on line 8: three literals, three values, three meanings, which might be "
                    "`FEVER_CELSIUS`, `URGENT_PRIORITY` and "
                    "`CHECK_INTERVAL_SECONDS`. A decimal literal is a magic number as "
                    "much as a whole one; distinct means distinct values; and a literal used once "
                    "is still counted, as Section 12.7 asks."},
            {"q": "Section 12.1 gives a rule of thumb for the literals that may appear in a "
                  "program's body. Which are they?",
             "a": ["0 and 1", "None at all", "0, 1 and 2", "Any literal used only once"],
             "c": 0,
             "why": "The book's rule of thumb (p. 292): the only literals in a program's body "
                    "should be 0 and 1, which start loops and increment counters. Every other "
                    "literal should be replaced with something more descriptive."},
            {"q": "The longest term changes from 360 months to 480. How many lines must change "
                  "in <code>magic</code>, and how many in <code>named</code>?",
             "a": ["2 and 1", "1 and 1", "2 and 2", "3 and 1"],
             "c": 0,
             "why": "In <code>magic</code>, 360 is on lines 4 and 5; in <code>named</code> it is "
                    "only in the declaration of `MAX_TERM_MONTHS`. That single point of "
                    "control is one of Section 12.7's two reasons for constants."},
            {"q": "Section 12.7 asks for a named constant even for the 12 in a loop over the "
                  "months of a year, which will never change. What reason does it give?",
             "a": ["If the code leaves any doubt about its purpose, the name removes it",
                   "The number of months may change",
                   "A constant makes the loop run faster",
                   "Java will not compile a loop bound written as a literal"],
             "c": 0,
             "why": "The section grants that the number of months is not going to change and "
                    "asks for the constant for readability: a reader should not have to bet that "
                    "12 means months (pp. 308–309). Constants cost nothing at run time, and a "
                    "literal loop bound is legal Java."},
        ],
        "mistakes": [
            ("Thinking that a literal used only once is harmless",
             "The chapter gives two reasons for constants, readability and a single point of "
             "change, and asks for them even for literals you think are safe. In "
             "<code>magic</code>, `12` appearing twice with one meaning is the case "
             "the lab's list makes obvious; the single `0.0725` is not repeated, and "
             "it still does not say that it is an annual rate. On the lesson's illustration, "
             "naming all three costs three lines and removes every guess."),
            ("Naming a constant after its value",
             "`TWELVE` passes the lab and tells a reader nothing the literal did "
             "not. Chapter 11 asks for a constant to be named for the abstract thing it "
             "represents, so that the name is still true when the value changes."),
            ("Overlooking magic strings and characters",
             "Section 12.4 applies the same reasoning to literal strings and characters: they "
             "may change, may need translating, and say nothing about why they are there. The "
             "lab counts only numbers, so a message or a code character in quotes is for you to "
             "find."),
        ],
        "standard": (
            "Finish when you can list a routine's magic numbers and replace them.",
            "For a routine, list every literal other than 0 and 1 with its lines, group them by "
            "meaning, and write the named constant declarations that replace them."
        ),
        "note": (
            "The lab counts numeric literals by the book's rule of thumb and nothing else: it "
            "does not count strings or characters, it ignores 0 and 1 even where they encode a "
            "meaning, and it cannot tell whether a constant's name says what it stands for. "
            "Whether every 2 deserves a name is a point on which practice varies; the book's "
            "answer is yes."
        ),
    },
    # ---------------------------------------------------------------- 06
    # McConnell Chapter 13, sections 13.1-13.3, pp. 319-344. Quotation:
    # p. 344 (Key Points), 24 words. Named constants as global data: p. 338.
    # Side effects: p. 336. Advantages of access routines: pp. 339-340.
    {
        "slug": "structures-pointers-and-global-data",
        "title": "Structures, Pointers and Global Data",
        "module": "Chapter 13 · Unusual Data Types",
        "one_line": "Global data couples every routine that writes it to every routine that touches it, and access routines do not remove that coupling but put each global's representation behind one name.",
        "summary": (
            "Chapter 13 covers three kinds of data a modern program uses less often: structures, "
            "pointers and global data. Its longest argument is about globals, which McConnell "
            "says are rarely the best way to program, and about the access routines he "
            "recommends in their place. Count the routines a set of globals couples and "
            "the places that touch them directly, then add access routines and see which count "
            "moves."
        ),
        "key": [
            "readers are coupled to every writer",
            "make data local first, global last",
            "one access routine for each global",
            "access routines move the coupling",
            "they do not remove it",
        ],
        "key_label": "Global data in five lines",
        "concepts_intro": (
            "Chapter 13's three sections are uneven; the third is the one that applies to every "
            "language."
        ),
        "concepts": [
            ("Global data",
             "A variable any part of the program can read or write. In Java that is a "
             "`public static` field that is not `final`, or a singleton "
             "with public state; a class's private field shared by all its routines is class "
             "data, not global data."),
            ("Coupling through a global",
             "Two routines are coupled through a global when one of them writes it and the "
             "other reads or writes it: neither can be understood, tested or changed without "
             "the other in mind."),
            ("An access routine",
             "A routine through which all code reaches a piece of data, which is itself hidden. "
             "It puts the data's representation in one place, and gives a place to check every "
             "change."),
        ],
        "read_title": "Chapter 13 section by section, then six routines and three globals",
        "read_intro": (
            "The lesson sets out the three sections, then counts what a set of globals couples "
            "before and after access routines are added."
        ),
        "body": [
            ("p", "&ldquo;If you can’t avoid global variables, work with them through access "
                  "routines. Access routines give you everything that global variables give you, "
                  "and more.&rdquo; That is the last of Chapter 13's Key Points, on page 344. This "
                  "lesson reads the whole chapter, Unusual Data Types, pages 319 to 344; read it "
                  "in your own copy first."),
            ("p", "Section 13.1 is about structures, data built from other data, which in Java "
                  "is a class with public fields and no routines. McConnell would usually rather "
                  "you wrote a class, but gives reasons a structure still helps: it shows which "
                  "data belongs together, as an employee's name and address do and a supervisor's "
                  "title does not; it lets you copy or pass a group of values as one; it shortens "
                  "parameter lists; and it means that adding or removing a field changes only the "
                  "code that cares about that field."),
            ("p", "Section 13.2 is about pointers, which McConnell calls one of the most "
                  "error-prone areas of programming. Java has no pointer type, and most of the "
                  "section's detail is for C and C++; the course does not teach it. Its general "
                  "advice carries over. A pointer error's symptoms are usually unrelated to its "
                  "cause, so the strategy is to avoid installing such errors and to detect them "
                  "soon after; and the first technique is to isolate pointer operations in a few "
                  "routines, so that there are few places to get them wrong. That is the same "
                  "move Section 13.3 makes for global data."),
            ("p", "Section 13.3 opens with what experienced programmers agree on: global data is "
                  "riskier than local data, and access to data from several routines is useful. "
                  "The problems it lists are inadvertent changes, where one routine changes a "
                  "global another assumed was untouched, which the book calls a side effect; "
                  "aliasing, where a global passed as a parameter is changed under two names; "
                  "code that more than one thread runs; code that cannot be reused without its "
                  "globals; initialisation order between files in C++; and above all the damage "
                  "to modularity, because you can no longer understand one routine at a time."),
            ("p", "The section is fair to the other side. Some purists, it says, would forbid "
                  "global data, but a database and a configuration file are global data, and so "
                  "are named constants, though they are not global variables. Used with "
                  "discipline, globals serve for values that apply to the whole program, to "
                  "emulate named constants and enumerated types in a language without them, for "
                  "data so common it would be in every parameter list, and to eliminate tramp "
                  "data passed through routines that do not use it. Even so, make each variable "
                  "local first, class data next, and global only as a last resort."),
            ("p", "Its answer to the globals you keep is access routines. Hide the data in a "
                  "class, make it `static` so there is one copy, write routines to read "
                  "and change it, and require every other piece of code to use them. The section "
                  "lists what that buys: centralised control, so a change of representation "
                  "stays inside the class; a place to check every change, such as a stack "
                  "overflow; information hiding; and a level of abstraction, so that a test reads "
                  "as whether the page is full instead of as a comparison of a line count. Do not "
                  "pour every global into one class, and do not disguise global data as one "
                  "enormous object passed to every routine. Here is a minimal access routine for "
                  "one global."),
            ("code", lines(ACCESS_ROUTINE)),
            ("p", "Now the count. The lab takes a list of records, one for each time a routine "
                  "reads (`r`), writes (`w`) or does both "
                  "(`rw`) to a global. The <code>globals</code> preset has six "
                  "routines and three globals: `readInput` and `reset` "
                  "write `current`, and `validate`, `report` and "
                  "`addLine` read it; `validate` and `reset` "
                  "write `errors`, and `report` reads it; "
                  "`addLine` reads and writes `total`, and "
                  "`printTotals` reads it. The lab counts 3 globals and 6 routines, "
                  "and 9 of the 15 possible pairs of routines coupled through them. The most "
                  "shared global is <code>current, 5 routines</code>; 10 places touch a global "
                  "directly; and Who writes each global lists <code>current: readInput, reset; "
                  "errors: reset, validate; total: addLine</code>."),
            ("p", "Where do the nine pairs come from? `current` alone couples seven: "
                  "its two writers with each other, and each writer with each of its three "
                  "readers. `errors` adds `validate` with "
                  "`report`, the other pairs it couples being among those already "
                  "counted, and `total` adds `addLine` with "
                  "`printTotals`. Notice `report`, which only reads: it is "
                  "coupled to `readInput`, `reset` and "
                  "`validate`, because what it prints depends on what they wrote."),
            ("p", "The <code>access-routines</code> preset keeps every record and gives each "
                  "global an owner: `current` behind `currentRecord`, "
                  "`errors` behind `errorLog` and `total` behind "
                  "`runningTotal`. The coupled pairs stay at 9, because the six routines "
                  "still share the same data. What changes is that the places touching a global's "
                  "representation fall from 10 to 3, one per global, and Who writes each global "
                  "now names only the owners. That is what Section 13.3 claims for access "
                  "routines, centralised control, and no more."),
            ("h3", "Exercise"),
            ("ul", ["`load` writes `config`",
                    "`render` reads `config`",
                    "`save` reads `config`",
                    "`render` writes `cache`",
                    "`save` reads `cache`"]),
            ("p", "These five records describe a small program. Count the globals, the routines "
                  "and the coupled pairs of routines, and the places that touch a global "
                  "directly; then say how many places touch a global directly once each global "
                  "has an access routine, and whether the coupled pairs change. Type the records "
                  "into the lab to check, in the form <code>load, w, config</code>, separated by "
                  "semicolons."),
            ("p", "That ends Part III. The next course, Statements, goes from the variable to "
                  "the line of code, beginning with &ldquo;Organizing Straight-Line Code&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "shared",
            "uses": GLOBAL_USES,
            "preset": "globals",
            "presets": [
                {"id": "globals", "label": "Six routines sharing three globals",
                 "expect": {"dgGlobals": "3", "dgRoutines": "6", "dgCoupled": "9",
                            "dgMostShared": "current, 5 routines", "dgDirectAccess": "10",
                            "dgWriters": "current: readInput, reset; errors: reset, validate; "
                                         "total: addLine"}},
                {"id": "access-routines", "label": "The same, with an access routine for each",
                 "owners": "current=currentRecord; errors=errorLog; total=runningTotal",
                 "expect": {"dgCoupled": "9", "dgDirectAccess": "3",
                            "dgWriters": "current: currentRecord; errors: errorLog; "
                                         "total: runningTotal"}},
            ],
            "panel_title": "What global data couples",
            "panel_intro": (
                "Each record says that a routine reads (r), writes (w) or reads and writes (rw) a "
                "global. The lab counts the pairs of routines coupled through a global, one of "
                "them writing it, and the places that touch each global directly; give owners to "
                "put a global behind an access routine."
            ),
        }),
        "steps_title": "Counting what a global couples",
        "steps_intro": "Four steps; the last is yours.",
        "steps": [
            ("List the uses",
             "For each global, write down every routine that reads it and every routine that "
             "writes it."),
            ("Count the coupled pairs",
             "Two routines are coupled when they share a global and at least one of them writes "
             "it. Count each pair once, however many globals it shares."),
            ("Count the direct touches",
             "Count the places that read or write each global's representation. With an access "
             "routine for a global, that becomes one place, and the coupled pairs stay as they "
             "were."),
            ("Map a global of your own",
             "Pick one global variable, singleton or static field in your own code, list every "
             "routine that reads or writes it as records in the lab, and note how many pairs it "
             "couples and how many places would change if its representation did."),
        ],
        "worked": {
            "title": "The nine coupled pairs",
            "intro": [
                "In <code>globals</code>, count the pairs global by global, skipping a pair "
                "already counted.",
            ],
            "lines": [
                "current: writers readInput, reset",
                "readers validate, report, addLine",
                "1 pair of writers + 2 * 3 writer and reader pairs: 7",
                "errors: adds validate with report: 8",
                "total: adds addLine with printTotals: 9",
                "possible pairs of 6 routines: 6 * 5 / 2, so 15",
            ],
            "after": [
                "Pairs that share only a read are not coupled: `validate` and "
                "`report` both read `current`, and are coupled only "
                "because `validate` writes `errors`, which "
                "`report` reads.",
            ],
        },
        "quiz_title": "Globals and access routines",
        "quiz": [
            {"q": "For the exercise's five records, what are the counts, and what do access "
                  "routines change?",
             "a": ["2 globals, 3 routines, 3 of 3 pairs coupled; 5 direct touches, 2 with an "
                   "access routine for each",
                   "2 globals, 3 routines, 2 of 3 pairs coupled, because render and save only "
                   "read config; 5 direct touches, 2 with access routines",
                   "2 globals, 3 routines, 3 of 3 pairs coupled; 5 direct touches, and with "
                   "access routines no pair is coupled",
                   "2 globals, 3 routines, 3 of 3 pairs coupled; 5 direct touches, still 5 with "
                   "access routines"],
             "c": 0,
             "why": "`load` writes `config`, which `render` and "
                    "`save` read: two pairs. `render` writes "
                    "`cache`, which `save` reads: the third pair, so all 3 "
                    "pairs of the 3 routines are coupled. Five records touch a global directly; "
                    "with an access routine for each global, 2 places do. The coupling stays at "
                    "3, because the routines still share the data."},
            {"q": "In the <code>globals</code> preset, which pair of routines is not coupled?",
             "a": ["report and printTotals", "validate and report", "readInput and addLine",
                   "reset and validate"],
             "c": 0,
             "why": "`report` reads `current` and `errors`; "
                    "`printTotals` reads only `total`; they share nothing. "
                    "`validate` writes `errors`, which `report` "
                    "reads; `readInput` writes `current`, which "
                    "`addLine` reads; `reset` and `validate` both "
                    "write `errors`."},
            {"q": "Adding access routines in <code>access-routines</code> changes which of the "
                  "lab's counts?",
             "a": ["Places touching a global fall from 10 to 3; coupled pairs stay at 9",
                   "Both fall: coupled pairs to 3 and places to 3",
                   "Coupled pairs fall to 0; places stay at 10",
                   "Neither changes"],
             "c": 0,
             "why": "The six routines still read and write the same data through the access "
                    "routines, so the 9 coupled pairs remain. What moves is the representation: "
                    "each global is touched directly in one place, its owner. That centralised "
                    "control is the advantage Section 13.3 claims."},
            {"q": "A table of tax rates is loaded once at start-up and only read afterwards by "
                  "four routines. Counting coupling as the lab does, after start-up, how many "
                  "pairs does it couple?",
             "a": ["None, since no routine writes it",
                   "6, every pair of the four readers",
                   "4, one for each reader",
                   "3, each reader with the next"],
             "c": 0,
             "why": "Coupling needs a writer, and once loaded the table has none: it behaves as a "
                    "named constant, which Section 13.3 counts as global data but not a global "
                    "variable (p. 338). Four readers make 6 pairs, but readers alone are not "
                    "coupled."},
        ],
        "mistakes": [
            ("Thinking global data is fine as long as a routine only reads it",
             "A routine that only reads a global is coupled to every routine that writes it: "
             "in <code>globals</code>, `report` writes nothing and is coupled to "
             "`readInput`, `reset` and `validate`, because "
             "what it prints depends on what they wrote. Section 13.3's first problem is just "
             "this, a value changed somewhere you assumed it was not. Data that no routine writes "
             "after start-up is another matter: it is a named constant, which the section accepts."),
            ("Thinking access routines remove the coupling",
             "They do not. In <code>access-routines</code> the coupled pairs stay at 9, because "
             "the six routines still share the same data, through the routines instead of "
             "directly. What changes is that each global's representation is touched in one "
             "place instead of ten, which is what Section 13.3 claims for them: centralised "
             "control, a place to check changes, and a level of abstraction."),
            ("Hiding global data in one big object",
             "Gathering everything into one object and passing it to every routine satisfies "
             "the letter of a rule against global variables. Section 13.3 calls it "
             "overhead with none of the benefits of encapsulation: every routine can still "
             "reach everything. If you use global data, it asks you to use it openly."),
        ],
        "standard": (
            "Finish when you can count what a set of globals couples.",
            "For a table of routines and the globals each reads and writes, count the coupled "
            "pairs (two routines that share a global one of them writes) and the places that "
            "touch each global directly, and say what access routines change and what they do "
            "not."
        ),
        "note": (
            "The lab counts coupling from a list you give it; it cannot read code to find the "
            "globals, and it treats every write as the same, whether it is a careful update "
            "through a checked routine or a stray assignment. It also cannot see when the "
            "accesses happen, so it says nothing about threads or initialisation order, two of "
            "the problems Section 13.3 lists."
        ),
    },
]
