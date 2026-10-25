"""Creating High-Quality Code, lessons 5-9 -- Chapters 7, 8 and 9.

McConnell, Code Complete, 2nd ed. (Microsoft Press, 2004): Chapter 7,
High-Quality Routines (pp. 161-186); Chapter 8, Defensive Programming
(pp. 187-213); Chapter 9, The Pseudocode Programming Process (pp. 215-234).
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

# Reasons to Create a Routine: presets copied, extracted, two-names
# (presets.py dupes-copied, dupes-routine, dupes-label, verbatim).
COPIED = """void printLabels(Order order) {
    Address a = order.shipTo();
    System.out.println(a.name());
    System.out.println(a.street());
    System.out.println(a.city() + " " + a.postcode());
    a = order.billTo();
    System.out.println(a.name());
    System.out.println(a.street());
    System.out.println(a.city() + " " + a.postcode());
}"""

EXTRACTED = """void printLabels(Order order) {
    printAddress(order.shipTo());
    printAddress(order.billTo());
}

void printAddress(Address a) {
    System.out.println(a.name());
    System.out.println(a.street());
    System.out.println(a.city() + " " + a.postcode());
}"""

TWO_NAMES = """void printLabels(Order order) {
    Address ship = order.shipTo();
    System.out.println(ship.name());
    System.out.println(ship.street());
    System.out.println(ship.city() + " " + ship.postcode());
    Address bill = order.billTo();
    System.out.println(bill.name());
    System.out.println(bill.street());
    System.out.println(bill.city() + " " + bill.postcode());
}"""

# Exercise (b), PLAN section D.4 printSummary, verbatim.
PRINT_SUMMARY_EXERCISE = """void printSummary(Totals totals) {
    double amount = totals.sales();
    String label = "Sales";
    System.out.print(label + ": ");
    System.out.println(String.format("%,.2f", amount));
    amount = totals.refunds();
    label = "Refunds";
    System.out.print(label + ": ");
    System.out.println(String.format("%,.2f", amount));
}"""

# Routine Length and Parameters: presets nine-parameters, parameter-objects
# (presets.py size-params, size-object, verbatim).
NINE_PARAMETERS = """// Prints one line of an invoice.
void printInvoiceLine(String sku, String description, int quantity,
        int unitPriceCents, int discountPercent, boolean taxable,
        int taxRatePermille, String currency, boolean showSku) {
    int gross = quantity * unitPriceCents;
    int net = gross - gross * discountPercent / 100;
    int tax = taxable ? net * taxRatePermille / 1000 : 0;
    String label = showSku ? sku + " " + description : description;
    System.out.println(label + " " + (net + tax) + " " + currency);
}"""

PARAMETER_OBJECTS = """// Prints one line of an invoice.
void printInvoiceLine(InvoiceLine line, TaxRule tax, Format format) {
    int net = line.netCents();
    int total = net + tax.on(net, line.isTaxable());
    System.out.println(format.label(line) + " " + format.money(total));
}"""

SCHEDULE_EXERCISE = """void schedule(String name, int year, int month, int day,
        int hour, int minute, int durationMinutes, String room) {
    // ...
}"""

SCORE_EXERCISE = """// A score is valid from 0 to 100.
boolean isValidScore(int score) {
    return score >= 0 || score <= 100;
}"""

# The Pseudocode Programming Process: presets free-slot and complete
# (PLAN section D.4 free-slot; complete adds line 15).
FREE_SLOT = """// Returns the index of the first free slot, or -1 if the table is full.
int findFreeSlot(Slot[] table) {
    // start at the slot after the one used last
    int start = (lastUsed + 1) % table.length;
    // look at each slot once, wrapping around the end
    for (int step = 0; step < table.length; step++) {
        int i = (start + step) % table.length;
        // if the slot is free, remember it and return it
        if (table[i].isFree()) {
            lastUsed = i;
            return i;
        }
    }
    // if no slot is free, log the overflow
    // return -1
    return -1;
}"""

COMPLETE = """// Returns the index of the first free slot, or -1 if the table is full.
int findFreeSlot(Slot[] table) {
    // start at the slot after the one used last
    int start = (lastUsed + 1) % table.length;
    // look at each slot once, wrapping around the end
    for (int step = 0; step < table.length; step++) {
        int i = (start + step) % table.length;
        // if the slot is free, remember it and return it
        if (table[i].isFree()) {
            lastUsed = i;
            return i;
        }
    }
    // if no slot is free, log the overflow
    log.warn("table full");
    // return -1
    return -1;
}"""

# Exercise, PLAN section D.4 expireSessions, verbatim.
EXPIRE_SESSIONS_EXERCISE = """// Moves every expired session to the archive.
void expireSessions(List<Session> sessions, Clock clock) {
    // read the current time once
    long now = clock.millis();
    // for each session older than the limit
    for (Session s : sessions) {
        if (now - s.lastSeen() > LIMIT) {
            // move it to the archive
            archive.add(s);
            // remove it from the live list
        }
    }
}"""


LESSONS = [
    # ---------------------------------------------------------------- 05
    # McConnell Chapter 7, sections 7.1-7.3, pp. 161-172.
    # Quote: p. 186 (Key Points), 20 words, cc_quotes.py OK; "illogical
    # cohesion", p. 170, 2 words. Lesson total: 22 words.
    # The low-quality routine (pp. 161-163, named, not reproduced); the
    # routine as the greatest invention, and the undergraduate textbook
    # (p. 163); valid reasons (pp. 164-167); operations that seem too simple
    # (pp. 166-167); cohesion after Stevens, Myers and Constantine 1974
    # (pp. 168-171); "illogical cohesion" (p. 170); good routine names
    # (pp. 171-172).
    {
        "slug": "reasons-to-create-a-routine",
        "title": "Reasons to Create a Routine",
        "module": "Chapter 7 · High-Quality Routines",
        "one_line": "The first reason to create a routine is to reduce complexity, not to avoid repetition, and a good routine does one thing, which its name says.",
        "summary": (
            "Sections 7.1 to 7.3 give the reasons for creating a routine, the kinds of "
            "cohesion a routine can have, and what a good name says. Name a routine's "
            "cohesion by the chapter's kinds, and find the repeated lines a routine would "
            "replace, with the lab's limit in view: it cannot see a copy whose names "
            "changed."
        ),
        "key": [
            "first reason: reduce complexity",
            "cohesion: how closely its parts relate",
            "aim for functional cohesion",
            "a name says everything it does",
            "the lab matches text, not meaning",
        ],
        "key_label": "Sections 7.1 to 7.3 in five lines",
        "concepts_intro": (
            "Three ideas organise the first half of Chapter 7. The second is older than the "
            "book, and the book keeps its terms."
        ),
        "concepts": [
            ("A valid reason",
             "The chapter lists the reasons a block of code deserves a routine of its own. "
             "Avoiding duplication is one; the most important is reducing complexity, by "
             "putting a detail behind a name so that you can stop thinking about it."),
            ("Cohesion",
             "How closely the operations inside a routine are related. A routine with "
             "functional cohesion does one thing; the chapter's other kinds, from "
             "sequential to coincidental, describe looser ties."),
            ("A complete name",
             "A routine's name should describe everything it does, its outputs and side "
             "effects included. A name that cannot do that without becoming long and silly "
             "points at a routine that does too much."),
        ],
        "read_title": "The chapter's argument first, then a repeated block",
        "read_intro": (
            "Read sections 7.1 to 7.3, pages 161 to 172, in your own copy first. The lesson "
            "sets out the argument and then turns to a label printer in three versions."
        ),
        "body": [
            ("p", "&ldquo;You can classify routines into various kinds of cohesion, but you "
                  "can make most routines functionally cohesive, which is best.&rdquo; That is "
                  "one of Chapter 7's key points (p. 186). This lesson reads sections 7.1 to "
                  "7.3, pages 161 to 172: why routines are created, how closely their parts "
                  "should be related, and what their names should say. Read them in your own "
                  "copy first."),
            ("p", "Chapter 7 opens with a deliberately bad routine and a list of what is "
                  "wrong with it, worth reading in the book. It then asks why routines exist "
                  "at all, and answers against its author's own education. As an "
                  "undergraduate, McConnell says, he thought the main reason for a routine "
                  "was to avoid duplicate code, because his textbook said so and said little "
                  "else; the chapter is his fuller answer. The routine, he says, is the "
                  "single greatest invention in computer science after the computer itself."),
            ("p", "Section 7.1's list starts with the reason it calls the single most "
                  "important: to reduce complexity, by hiding information so that you need "
                  "not think about it. Then come introducing an intermediate, understandable "
                  "abstraction (a well-named call in place of eight lines of loop), avoiding "
                  "duplicate code, supporting subclassing, hiding sequences, improving "
                  "portability, simplifying complicated boolean tests and improving "
                  "performance, with the class reasons of Chapter 6 added. Making every "
                  "routine small is not on the list. Nor is any operation too simple: the "
                  "chapter's example is a one-line unit conversion, repeated in a dozen "
                  "places, that later needed a check for division by zero, and could get it "
                  "once because it had become a routine."),
            ("p", "Section 7.2 takes cohesion from Wayne Stevens, Glenford Myers and Larry "
                  "Constantine's paper of 1974, and keeps it as the workhorse heuristic at the "
                  "level of a single routine. Functional cohesion, one operation, is the "
                  "strongest. Sequential cohesion is steps that must run in order and pass "
                  "data from one to the next without making up a complete function; "
                  "communicational is operations that use the same data and are otherwise "
                  "unrelated; temporal is operations grouped because they happen at the same "
                  "time, acceptable when the routine only calls the others. Procedural, "
                  "logical and coincidental are the unacceptable kinds. Logical cohesion, "
                  "operations picked by a flag passed in, is the one McConnell suggests "
                  "renaming &ldquo;illogical cohesion&rdquo;, with an exception for an event "
                  "handler that only dispatches. Learn the ideas, he adds, not the terms."),
            ("p", "Section 7.3 is on names. A routine's name should describe everything the "
                  "routine does; the cure for a long, silly name is not a vaguer one but a "
                  "routine without side effects. Avoid verbs like handle, process and deal "
                  "with, which say only that something happens."),
            ("p", "Now the count. One reason on section 7.1's list is visible to a machine: "
                  "duplicated code. The lab compares statement lines as text, with spacing "
                  "collapsed, and reports each block of at least two lines that appears more "
                  "than once: the number of repeated blocks, the lines in all the copies, and "
                  "where they are, with the copies flagged in the listing. In "
                  "<code>copied</code>, below, one variable `a` holds first the shipping "
                  "address and then the billing address, and lines 3 to 5 equal lines 7 to "
                  "9: 1 repeated block, 6 lines in its copies, at lines 3–5 and lines 7–9."),
            ("code", _lines(COPIED)),
            ("p", "In <code>extracted</code> the three lines have become `printAddress`, "
                  "called twice, and the lab finds 0 repeated blocks. The routine also has a "
                  "name, which says what the three lines were for, and that is section 7.1's "
                  "second reason as much as its third."),
            ("code", _lines(EXTRACTED)),
            ("p", "The last preset, <code>two-names</code>, is the copied printer written "
                  "with two variables, `ship` and `bill`. The lab reports 0 repeated blocks. "
                  "The copy is still there; the text differs, and the lab matches text. The "
                  "lab cannot see this copy; you can. A count of duplicated lines is a lower "
                  "bound, and a reason to look further."),
            ("code", _lines(TWO_NAMES)),
            ("h3", "Exercise"),
            ("p", "First, name the cohesion of each of these six routines, by section 7.2's "
                  "kinds, and rewrite the weakest as separate routines:"),
            ("ol", [
                "returns the sales tax on an amount;",
                "works out a parcel's volume and then, from that volume, its box size, and returns both;",
                "from an order's list of items, adds up the total weight and, separately, "
                "counts the distinct suppliers;",
                "at the end of each night, archives the day's orders, empties the shopping baskets and rotates the logs;",
                "prints a shipping label and then writes a line to the dispatch log, in the "
                "order the warehouse procedure lists them, with nothing passed between the two;",
                "formats an invoice, a receipt or a refund note, depending on a flag passed in.",
            ]),
            ("code", _lines(PRINT_SUMMARY_EXERCISE)),
            ("p", "Second, in `printSummary` above, mark the repeated block by hand and write "
                  "the header of the routine that would replace it. Paste it into the lab "
                  "afterwards to check the lines you marked."),
            ("p", "Section 7.4 asks how long a routine can be, and 7.5 how many parameters it "
                  "should take. The next lesson, Routine Length and Parameters, reads both."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dupes",
            "min_run": 2,
            "preset": "copied",
            "presets": [
                {"id": "copied",
                 "label": "A label printer with its address lines copied",
                 "code": COPIED,
                 "expect": {"coDupBlocks": "1", "coDupLines": "6"}},
                {"id": "extracted",
                 "label": "The printer calling printAddress twice",
                 "code": EXTRACTED,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0"}},
                {"id": "two-names",
                 "label": "The copied printer with two variable names",
                 "code": TWO_NAMES,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0"}},
            ],
            "panel_title": "Find the repeated blocks",
            "panel_intro": (
                "Paste a Java routine or two. The lab compares statement lines as text, with "
                "spacing collapsed, and reports each block of two or more lines that appears "
                "more than once. A copy whose variable names differ is not the same text, so "
                "the lab cannot see it."
            ),
        }),
        "steps_title": "Reading a routine for its cohesion and its copies",
        "steps_intro": "Five steps, the last of them on a routine of your own.",
        "steps": [
            ("Say what the routine does",
             "Write one sentence that says everything the routine does. If the sentence "
             "needs an and, note what it joins."),
            ("Name its cohesion",
             "One operation is functional. Steps passing data along are sequential; "
             "operations sharing data and nothing else are communicational; operations "
             "grouped by when they run are temporal; a flag choosing among operations is "
             "logical."),
            ("Look for repeated blocks",
             "Find runs of two or more lines that appear twice. Look also for runs that "
             "differ only in the names of their variables, which a text match will miss."),
            ("Write the replacing routine's header",
             "Give the repeated block a name that says what it is for, and take as "
             "parameters exactly what the copies differ in."),
            ("Do it on your own code",
             "Take the longest routine you maintain, name its cohesion in one word, and "
             "paste it into the lab. Note any repeated block it finds, and write the header "
             "of the routine that would replace it, or one sentence on why there is none."),
        ],
        "worked": {
            "title": "Three address lines, twice",
            "intro": [
                "Read <code>copied</code> and do what the lab does, then write the routine.",
            ],
            "lines": [
                "line 3: System.out.println(a.name());",
                "line 7: System.out.println(a.name());",
                "lines 3 to 5 equal lines 7 to 9: one block",
                "two copies of 3 lines: 6 lines",
                "void printAddress(Address a)",
            ],
            "after": [
                "The two copies differ in nothing, because the same variable `a` holds both "
                "addresses in turn. The routine takes that variable as its parameter, and "
                "the printer becomes two calls. In <code>two-names</code> the same "
                "extraction applies, and only a reader can see it.",
            ],
        },
        "quiz_title": "Cohesion and copies",
        "quiz": [
            {"q": "Name the cohesion of the exercise's six routines, in order.",
             "a": ["Functional, sequential, communicational, temporal, procedural, logical",
                   "Functional, communicational, sequential, temporal, procedural, logical",
                   "Functional, sequential, communicational, procedural, temporal, logical",
                   "Functional, sequential, communicational, temporal, procedural, "
                   "coincidental"],
             "c": 0,
             "why": "The tax is one operation: functional. The volume feeds the box size and both are "
                    "returned: sequential; it would be functional if it returned the box size "
                    "alone. Weight and supplier count share only the item list: "
                    "communicational. The nightly jobs are grouped by when they run: temporal. The "
                    "label and the log line are ordered only by the warehouse procedure and share no data: "
                    "procedural. The flag picks among three unrelated jobs: logical, the "
                    "weakest here, and it becomes three routines, `formatInvoice`, "
                    "`formatReceipt` and `formatRefundNote`, with no flag. Coincidental "
                    "cohesion has no tie at all; here a flag passed in picks the operation, "
                    "which is what makes it logical (p. 170)."},
            {"q": "Paste the exercise's `printSummary` into the lab. What does it report?",
             "a": ["1 block, 6 lines: lines 3–5 and lines 7–9",
                   "1 block, 4 lines: lines 4–5 and lines 8–9",
                   "1 block, 8 lines: lines 2–5 and lines 6–9",
                   "No repeated block, because the amounts differ"],
             "c": 1,
             "why": "Lines 4–5 and 8–9 are the same text, 2 lines in each of 2 copies, 4 lines. "
                    "Lines 2–3 and 6–7 differ, since one declares and the other assigns. A "
                    "routine `printMoney(String label, double amount)` replaces the block, "
                    "and `printSummary` becomes two calls."},
            {"q": "Which reason does section 7.1 call the single most important reason to "
                  "create a routine?",
             "a": ["To avoid duplicate code", "To reduce complexity",
                   "To improve performance", "To support subclassing"],
             "c": 1,
             "why": "Reducing complexity comes first: hide information so you need not think "
                    "about it. Avoiding duplicate code is, the section says, the most popular "
                    "reason, not the most important."},
            {"q": "Two three-line blocks in a routine differ only in that one uses `ship` "
                  "where the other uses `bill`. What does the lab's duplicate count report "
                  "for them?",
             "a": ["One block, six lines", "One block, three lines",
                   "No repeated block", "Two blocks, six lines"],
             "c": 2,
             "why": "The lab compares the lines as text, and `ship.name()` is not the same "
                    "text as `bill.name()`, so it finds nothing. That is "
                    "<code>two-names</code>: the copy is real, and only a reader sees it."},
        ],
        "mistakes": [
            ("Thinking code that is not repeated needs no routine",
             "If routines exist to avoid duplication, a block used once can stay where it "
             "is. Section 7.1 puts reducing complexity first and introducing an "
             "understandable abstraction second, and neither depends on repetition; its "
             "cohesion scale in 7.2 has nothing to do with it either. On the lesson's "
             "illustration, <code>extracted</code> would be the better routine even if the "
             "order had only one address, because `printAddress` names what three lines do."),
            ("Leaving a two-line operation inline because it is simple",
             "A routine for two or three lines can look like overkill. The chapter's example "
             "is a one-line conversion repeated a dozen times that later needed a guard "
             "against division by zero: as a routine it changed in one place. Small "
             "operations tend to grow."),
            ("Keeping a name short by leaving out a side effect",
             "A routine that computes totals and also opens a file is not described by a "
             "name about totals. Section 7.3 asks for a name that describes everything the "
             "routine does, and when that name would be long and silly, the cure is to "
             "remove the side effect, not to shorten the name."),
        ],
        "standard": (
            "Finish when you can name a routine's cohesion and the routine its copies need.",
            "For six one-line routine descriptions, name each one's cohesion and rewrite the "
            "weakest as separate routines; in a listing, mark the repeated block and write "
            "the header of the routine that replaces it."
        ),
        "note": (
            "The lab finds only one of section 7.1's reasons, repetition, and only when the "
            "copies are the same text: a copy with renamed variables, or the same logic "
            "written two ways, is invisible to it. Cohesion it cannot measure at all; that "
            "is a reading of what a routine's operations have to do with each other."
        ),
    },
    # ---------------------------------------------------------------- 06
    # McConnell Chapter 7, sections 7.4-7.7, pp. 173-186.
    # Quote: p. 186 (Key Points), 23 words, cc_quotes.py OK.
    # The Pilgrims (p. 173); the studies of routine length (pp. 173-174);
    # parameters (pp. 174-180); functions and procedures (pp. 181-182);
    # macros and inline routines (pp. 182-185).
    # F8, pp. 173-174: allow growth to 100-200 lines (non-comment, non-blank);
    # care past 200 (Basili and Perricone 1984 and others).
    # F9, p. 178: limit parameters to about seven (Miller 1956).
    # The course's one modern aside (PLAN section F.4) is this lesson's note.
    {
        "slug": "routine-length-and-parameters",
        "title": "Routine Length and Parameters",
        "module": "Chapter 7 · High-Quality Routines",
        "one_line": "Let complexity, not a line limit, decide a routine's length; keep its parameters to about seven, grouped by the abstraction they serve; and let a function return only the value its name describes.",
        "summary": (
            "Sections 7.4 to 7.7 ask how long a routine can be, how to use its parameters, "
            "when a routine should be a function, and what to make of macros. Count a "
            "routine's lines and parameters, regroup parameters that travel together into "
            "objects, and read both counts against the book's figures."
        ),
        "key": [
            "grow to 100 or 200 lines if need be",
            "a line: not blank, not a comment",
            "parameters: about seven at most",
            "group what travels together",
            "a function returns what its name says",
        ],
        "key_label": "Sections 7.4 to 7.7 in five lines",
        "concepts_intro": (
            "The second half of Chapter 7 turns on three questions a routine's author answers "
            "every time."
        ),
        "concepts": [
            ("A line of code",
             "For the book's figures on length, a line is a non-comment, non-blank line of "
             "source. The lab's code-lines tile counts exactly that, so a line holding only "
             "a brace counts."),
            ("A parameter object",
             "An object that carries values which always travel together, passed as one "
             "parameter. The chapter's test is the routine's abstraction: pass what the "
             "routine is about."),
            ("Function and procedure",
             "A function returns a value; a procedure does not. The chapter asks that a "
             "function's main purpose be to return the value its name describes."),
        ],
        "read_title": "The chapter's argument first, then a header that shrinks",
        "read_intro": (
            "Read sections 7.4 to 7.7, pages 173 to 186, in your own copy first. The lesson "
            "sets out the argument and then counts one routine before and after its "
            "parameters are grouped."
        ),
        "body": [
            ("p", "&ldquo;Functions should be used only when the primary purpose of the "
                  "function is to return the specific value described by the function’s "
                  "name.&rdquo; That is one of Chapter 7's key points (p. 186). This lesson "
                  "reads sections 7.4 to 7.7, pages 173 to 186, on routine length, "
                  "parameters, functions and macros. Read them in your own copy first."),
            ("p", "You have probably called a routine like the first one below with its "
                  "arguments in the wrong order: nine of them, three `int`s in a row, and a "
                  "compiler that is satisfied as long as the types line up. The second half "
                  "of Chapter 7 is about the shape of a routine from the outside, its length "
                  "and its parameters, and it begins with McConnell's own joke: the Pilgrims, "
                  "he says, argued about the best maximum length for a routine all the way "
                  "across the Atlantic, and never settled it."),
            ("p", "Section 7.4 reviews the studies, which the book cites from Basili and "
                  "Perricone (1984) to Jones (1986a), and most do not say what you might "
                  "expect: several found larger routines no more error-prone per line than "
                  "small ones, and some found them cheaper to develop; one, at IBM, found "
                  "routines over 500 lines the most error-prone. The book's conclusion is "
                  "that a routine with a complex algorithm may be allowed to grow "
                  "organically up to 100 to 200 lines, a line being one that is neither a "
                  "comment nor blank, and that past about 200 you should be careful: none "
                  "of the studies that favoured longer routines distinguished sizes beyond "
                  "200, and somewhere past it a routine becomes hard to understand. Length should follow from cohesion, nesting, the number of "
                  "variables and decision points, not from a limit imposed for its own sake."),
            ("p", "Section 7.5 is the longest, because interfaces between routines are, it "
                  "says, among the most error-prone parts of a program. Put parameters in "
                  "input, modify, output order, and keep the order consistent across "
                  "routines; use every parameter; put status or error variables last; do "
                  "not use a parameter as a working variable; document what you assume of "
                  "each. Limit their number to about seven, after Miller's 1956 paper on how "
                  "much people can keep track of at once. And pass what the routine's "
                  "abstraction needs: whether to pass an object or three of its fields is "
                  "settled by what the routine is about, not by a rule. Java has no "
                  "<em>in</em> or <em>out</em> keywords; `final` on a parameter stops it "
                  "being reassigned, but not an object it refers to being changed."),
            ("p", "Section 7.6 draws the line between functions and procedures. Purists, "
                  "the section says, would have a function take only input and return one "
                  "value through its name, as `sin` or `screenHeight` do. A routine that does something and returns "
                  "a status is common, and the book accepts it if used consistently, while "
                  "preferring a procedure with an explicit status variable. Its rule is the "
                  "key point above. Section 7.7, on macros and inline routines, is about C "
                  "and C++ and is left to the book."),
            ("p", "Now the count. The lab's size view prints seven tiles: all lines; code "
                  "lines, those neither blank nor comment, which is the book's line, so "
                  "braces count; statement lines, the code lines that are more than a brace; "
                  "comment lines; blank lines; the parameters of the routine's header; and "
                  "comment lines per statement line. The preset "
                  "<code>nine-parameters</code>, below, gives 10 lines, 9 code lines, 8 "
                  "statement lines, 1 comment, 0 blank, 9 parameters and a density of "
                  "1/8 = 12.5%."),
            ("code", _lines(NINE_PARAMETERS)),
            ("p", "Seven of its nine parameters describe the invoice line or its tax: "
                  "`sku`, `description`, `quantity`, `unitPriceCents`, `discountPercent`, "
                  "`taxable` and `taxRatePermille`. In <code>parameter-objects</code> they "
                  "become an `InvoiceLine` and a `TaxRule`, and the currency and the SKU "
                  "switch become a `Format`: 6 lines, 5 code lines, 4 statement lines, 1 "
                  "comment, 0 blank, 3 parameters, and a density of 1/4 = 25%. The density "
                  "doubled with no comment added: the statement lines it divides by fell."),
            ("code", _lines(PARAMETER_OBJECTS)),
            ("p", "What do the counts show? Nine is past the book's about seven, and three "
                  "is not; but the lab counts parameters, not abstractions, and would print 3 "
                  "just as happily for three grab-bag objects. The grouping is right here "
                  "because each object is something the routine is about. As for length, "
                  "both versions are far below the 100 to 200 lines the book allows, and "
                  "nothing in section 7.4 asks you to split either for length alone."),
            ("h3", "Exercise"),
            ("code", _lines(SCHEDULE_EXERCISE)),
            ("p", "Count this header's parameters, find the ones that travel together, and "
                  "write a header with fewer parameters that keeps what `schedule` is "
                  "about. Use a type from the Java library if one fits. You can paste the "
                  "header into the lab afterwards to check the parameter count."),
            ("p", "A routine's parameters are where bad data arrives. The next lesson, "
                  "Assertions and Error Handling, begins Chapter 8, on what a routine should "
                  "do about it."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "size",
            "preset": "nine-parameters",
            "presets": [
                {"id": "nine-parameters",
                 "label": "An invoice-line printer with nine parameters",
                 "code": NINE_PARAMETERS,
                 "expect": {"coParams": "9", "coCode": "9", "coStatements": "8",
                            "coDensity": "1/8 = 12.5%"}},
                {"id": "parameter-objects",
                 "label": "The same printer taking three objects",
                 "code": PARAMETER_OBJECTS,
                 "expect": {"coParams": "3", "coCode": "5", "coStatements": "4",
                            "coDensity": "1/4 = 25%"}},
            ],
            "panel_title": "Count a routine's lines and parameters",
            "panel_intro": (
                "Paste a Java routine. Code lines are lines that are neither blank nor a "
                "comment, the book's line; statement lines leave out lines that hold only a "
                "brace. The parameters are counted from the routine's header. A count is a "
                "reason to look at the header, not a verdict on it."
            ),
        }),
        "steps_title": "Counting a routine and regrouping its parameters",
        "steps_intro": "Five steps, the last of them on a routine of your own.",
        "steps": [
            ("Count the lines the book counts",
             "Count the lines that are neither blank nor a comment. Read the figure against "
             "the book's 100 to 200, not against a screen."),
            ("Count the parameters",
             "Count the header's parameters. Past about seven, look at them as a group."),
            ("Find what travels together",
             "Mark the parameters that describe one thing: a date and a time, a line and its "
             "price, a position and a size. Each group is a candidate object."),
            ("Check the abstraction",
             "For each group, ask whether the routine is about that thing. If it is, pass "
             "the object; if the values only happen to come from one object, pass them."),
            ("Do it on your own code",
             "Find the routine in your own code with the most parameters, paste it into the "
             "lab and note the count. Write the header it would have with its travelling "
             "parameters grouped, and name the object each group belongs in."),
        ],
        "worked": {
            "title": "Nine parameters become three",
            "intro": [
                "Group the parameters of <code>nine-parameters</code> by what they describe.",
            ],
            "lines": [
                "the line: sku, description, quantity",
                "its price: unitPriceCents, discountPercent",
                "its tax: taxable, taxRatePermille",
                "the output: currency, showSku",
                "InvoiceLine line, TaxRule tax, Format format",
                "parameters: 9 before, 3 after",
            ],
            "after": [
                "The seven values that describe the line and its tax go into two objects, and "
                "the two that describe the output into a third. The arithmetic moved into "
                "the objects' own routines, which is why the body shrank from 8 statement "
                "lines to 4.",
            ],
        },
        "quiz_title": "Length, parameters and functions",
        "quiz": [
            {"q": "How many parameters has the exercise's `schedule`, and how many once the "
                  "five fields that name a moment, `year` to `minute`, become one "
                  "`LocalDateTime`?",
             "a": ["8, then 4", "8, then 6", "7, then 4", "8, then 1"],
             "c": 0,
             "why": "`name`, `year`, `month`, `day`, `hour`, `minute`, `durationMinutes` and "
                    "`room` are 8. The five fields from `year` to `minute` are one moment, "
                    "a `LocalDateTime`, so the header becomes `schedule(String name, "
                    "LocalDateTime start, int durationMinutes, String room)`: 4. `durationMinutes` "
                    "could become a `Duration` as well; the header would still have four "
                    "parameters. One parameter would be a grab-bag holding the name and room "
                    "as well."},
            {"q": "In <code>nine-parameters</code>, the lab prints 9 code lines and 8 "
                  "statement lines. What is the one line in the first count and not the "
                  "second?",
             "a": ["The comment on line 1", "The closing brace on line 10",
                   "The second line of the header", "None: the tiles count the same lines"],
             "c": 1,
             "why": "Code lines are the lines that are neither blank nor a comment, the "
                    "book's line, so the comment is in neither count and the closing brace "
                    "is a code line. Statement lines leave out a line holding only a brace."},
            {"q": "What length does section 7.4 say a routine may be allowed to grow to, if "
                  "a complex algorithm calls for it?",
             "a": ["One screen, about 50 lines", "100 to 200 lines",
                   "About 500 lines", "No limit at all"],
             "c": 1,
             "why": "Up to 100 to 200 lines, a line being neither a comment nor blank "
                    "(pp. 173–174), with care past 200, because none of the studies that "
                    "found longer routines cheaper or less error-prone distinguished sizes "
                    "beyond it. One screen is the traditional "
                    "figure the section reports and does not adopt."},
            {"q": "A routine named `totalPrice` returns the order's total and also marks the "
                  "order as priced. By section 7.6, what should change?",
             "a": ["Nothing, if the caller reads the code",
                   "Rename it `totalPriceAndMark`",
                   "Separate the marking from the function, so that `totalPrice` only "
                   "returns the value its name describes",
                   "Make it return a status instead"],
             "c": 2,
             "why": "A function's primary purpose should be to return the value its name "
                    "describes. Marking the order is a second job, which belongs in a "
                    "procedure of its own; renaming it only records the problem."},
        ],
        "mistakes": [
            ("Letting a function change state on the way",
             "The thought is that a routine which returns a value may as well do some work "
             "too, and the caller can read the code to find out. Section 7.6 is firm that a "
             "function's main purpose is to return the value its name describes. A call "
             "that reads like a value, `total = totalPrice(order)`, gives no sign that it also "
             "changes the order, and a reader who has to open every function to learn what "
             "it does has lost what the routine was for."),
            ("Bundling any parameters to get under seven",
             "Three objects instead of nine values satisfies the count whatever is in the "
             "objects. Section 7.5's test is the routine's abstraction: group values the "
             "routine is about, and pass separately values that only happen to come from "
             "one place. A grab-bag object hides the coupling it was meant to reduce."),
            ("Reusing a parameter as a working variable",
             "Overwriting a parameter saves a declaration and leaves a name that no longer "
             "means what it says: by the end of the routine it holds a computed value, not "
             "the input. Section 7.5 says to copy it into a local variable with a name of "
             "its own."),
        ],
        "standard": (
            "Finish when you can count a routine's interface and regroup it.",
            "For a routine header and body, state its code lines and its parameter count, "
            "and propose a header with fewer parameters that keeps the routine's abstraction."
        ),
        "note": (
            "The lab counts lines and parameters; whether a grouping matches the routine's "
            "abstraction is for you to say. The book's figure for length, up to 100 to 200 "
            "lines, rests on studies of the 1980s and early 1990s that it reviews in section "
            "7.4. Since the book, a school of thought has argued that most routines should be "
            "only a few lines long, and that length alone is a reason to extract a routine: "
            "small routines, it holds, are easier to name, test and reuse. The book's position "
            "is that length should follow from complexity, and that the evidence it reviewed "
            "did not find routines of 100 to 200 lines more error-prone than shorter ones. "
            "The two are stated here side by "
            "side; this course does not settle between them, and your own records of where "
            "defects were found can test either."
        ),
    },
    # ---------------------------------------------------------------- 07
    # McConnell Chapter 8, sections 8.1-8.3, pp. 187-197.
    # Quote: p. 213 (Key Points), 19 words, cc_quotes.py OK; "Garbage in,
    # garbage out", p. 188, 4 words. Lesson total: 23 words.
    # Defensive driving (p. 187); garbage in (p. 188); assertions and the
    # rule (pp. 189-191); executable code in assertions, pre- and
    # postconditions, assert and handle (pp. 191-193); error-handling
    # techniques (pp. 194-196); robustness and correctness (p. 197);
    # high-level implications (p. 197).
    {
        "slug": "assertions-and-error-handling",
        "title": "Assertions and Error Handling",
        "module": "Chapter 8 · Defensive Programming",
        "one_line": "Handle the errors you expect, assert the ones that can never happen, and check an input check against its specification at the boundaries.",
        "summary": (
            "Sections 8.1 to 8.3 cover protecting a program from invalid input, assertions, "
            "and the ways of handling an error. Compare an input check with its "
            "specification over every integer, find where it is wrong, and see how a slip "
            "between `&&` and `||` makes a check never fire or always fire."
        ),
        "key": [
            "expected errors: handle them",
            "impossible conditions: assert them",
            "test each end, inside and outside",
            "inside a range: join both ends with &&",
            "how to handle bad input is design",
        ],
        "key_label": "Sections 8.1 to 8.3 in five lines",
        "concepts_intro": (
            "Section 8.2 gives the rule that settles most of the chapter. It needs three "
            "terms."
        ),
        "concepts": [
            ("Error handling",
             "Code that deals with conditions the programmer expects to occur, rarely "
             "perhaps: bad input from a user, a file or another system. It runs in the "
             "program that ships."),
            ("Assertion",
             "Code that lets a program check itself as it runs, stating a condition that "
             "should never be false if the program is right. A failing assertion means a "
             "bug in the code, and assertions are usually compiled out of the program "
             "that ships."),
            ("Boundary test",
             "A test at the edge of a valid range: each end, the value just inside it and "
             "the value just outside. Most mistakes in a range check show at the ends."),
        ],
        "read_title": "The chapter's rule first, then a check tested",
        "read_intro": (
            "Read sections 8.1 to 8.3, pages 187 to 197, in your own copy first. The lesson "
            "sets out the argument and then tests three versions of one input check."
        ),
        "body": [
            ("p", "&ldquo;The decision about how to handle bad inputs is a key error-handling "
                  "decision and a key high-level design decision.&rdquo; That is one of "
                  "Chapter 8's key points (p. 213). This lesson reads sections 8.1 to 8.3, "
                  "pages 187 to 197, on invalid input, assertions and the techniques of "
                  "error handling. Read them in your own copy first."),
            ("p", "What does it mean to program defensively? The chapter's answer is an "
                  "analogy with defensive driving: assume you cannot be sure what other "
                  "drivers will do, and arrange not to be hurt even when it is their fault. "
                  "A routine passed bad data should not be hurt by it, even when the data is "
                  "another routine's fault. &ldquo;Garbage in, garbage out&rdquo;, section 8.1 "
                  "says, is not good enough for production software; a good program never "
                  "puts garbage out. It names three ways to handle garbage in: check the "
                  "values of all data from external sources, check the values of a "
                  "routine's input parameters, and decide how to handle bad inputs. It adds "
                  "that the best defence is not inserting errors in the first place."),
            ("p", "Section 8.2 introduces the assertion, and with it the rule that settles "
                  "most of the chapter (p. 191): use error-handling code for conditions you "
                  "expect to occur, and assertions for conditions that should never occur. "
                  "Error handling checks for bad input; an assertion checks for a bug, and "
                  "when one fires the fix is to change the source and release a new version. "
                  "The section's other guidelines: keep executable code out of assertions, "
                  "since they may be compiled out; use them to state preconditions and "
                  "postconditions, after Meyer's design by contract; and in very large, "
                  "long-lived systems, assert and then handle the error anyway. In Java an "
                  "`assert` statement does nothing unless the program runs with assertions "
                  "enabled, which is the switch <code>-ea</code>; the rule above is why that is safe."),
            ("p", "Section 8.3 lists what to do with an error you expect: return a neutral "
                  "value, substitute the next valid piece of data, return the previous "
                  "answer, substitute the closest legal value, log a warning, return an "
                  "error code, call a central error-handling routine, display a message, "
                  "handle it locally, or shut down. Which is right depends on the program: a "
                  "video game can paint a neutral colour, a machine that treats patients "
                  "should stop. That is the choice between robustness, always doing "
                  "something, and correctness, never returning an inaccurate result. "
                  "Because the choice shapes the whole program, the section ends where the "
                  "key point does: decide it at the level of the architecture, and follow it "
                  "everywhere."),
            ("p", "Now the count. The most common defence against external data is a range "
                  "check, and the most common slip in writing one is the connective. The "
                  "lab's range view takes a check on one integer variable, the valid range, "
                  "and what a true check means, valid or invalid. Here a month is valid from "
                  "1 to 12 and the check flags an invalid one. The lab prints where the check "
                  "and the range disagree, the boundary tests (each end, one inside and one "
                  "outside), and the tests that expose a difference. The preset "
                  "<code>correct</code>, `month < 1 || month > 12`, disagrees nowhere: none; "
                  "boundary tests 0, 1, 2, 11, 12, 13; none exposed."),
            ("p", "In <code>never-fires</code> the connective is `&&`: `month < 1 && month > "
                  "12`. No integer is both below 1 and above 12, so the check is never true "
                  "and every invalid month passes. The lab prints 0 and below, 13 and above "
                  "as the disagreement, and the boundary tests 0 and 13 expose it. In "
                  "<code>always-fires</code>, `month >= 1 || month <= 12`, every integer "
                  "satisfies one side or the other, so every month is flagged invalid: the "
                  "check and the range disagree on 1 to 12, and the tests 1, 2, 11 and 12 "
                  "expose it."),
            ("p", "Neither mistake needs an unusual value to show: the six boundary tests "
                  "catch both. That is the argument for testing at the ends, which Developer "
                  "Testing, later in this path, makes properly. What the lab cannot tell you "
                  "is whether this check should be error handling or an assertion. That "
                  "depends on where `month` comes from, which is the question the next "
                  "lesson's barricade answers."),
            ("h3", "Exercise"),
            ("code", _lines(SCORE_EXERCISE)),
            ("p", "A score is valid from 0 to 100, and this check returns true for a valid "
                  "one. By hand, from its comparisons and its connective, find the integers "
                  "on which it is wrong, the boundary tests that would expose it, and the "
                  "fix. You can check your answer afterwards by typing the condition, the "
                  "range and what a true check means into the lab."),
            ("p", "Where should such checks go, and which values need them? The next lesson, "
                  "Exceptions and Barricades, reads the rest of Chapter 8."),
        ],
        "lab": ("cckit", {
            "mode": "cond",
            "view": "range",
            "means": "invalid",
            "lo": 1,
            "hi": 12,
            "preset": "correct",
            "presets": [
                {"id": "correct",
                 "label": "Correct: below 1 or above 12, joined by or",
                 "cond": "month < 1 || month > 12",
                 "expect": {"cdDisagree": "none", "cdExposed": "none"}},
                {"id": "never-fires",
                 "label": "Never fires: and where or was meant",
                 "cond": "month < 1 && month > 12",
                 "expect": {"cdDisagree": "0 and below, 13 and above", "cdExposed": "0, 13"}},
                {"id": "always-fires",
                 "label": "Always fires: the valid test joined by or",
                 "cond": "month >= 1 || month <= 12",
                 "expect": {"cdDisagree": "1 to 12", "cdExposed": "1, 2, 11, 12"}},
            ],
            "panel_title": "Test an input check against its range",
            "panel_intro": (
                "Type a check on one integer variable, the valid range, and whether a true "
                "check means the value is valid or invalid. The lab finds every integer on "
                "which the check and the range disagree, and runs the boundary tests: each "
                "end, one inside and one outside."
            ),
        }),
        "steps_title": "Checking an input check",
        "steps_intro": "Five steps, the last of them on a check of your own.",
        "steps": [
            ("Write down the specification",
             "State the valid range, low and high, and whether the check is meant to be "
             "true for a valid value or an invalid one."),
            ("Read the connective",
             "A check that a value is inside a range joins its two ends with `&&`; a check "
             "that it is outside joins them with `||`. The other connective makes the check "
             "never or always true."),
            ("Run the boundary tests",
             "Try each end of the range, the value just inside each end and the value just "
             "outside it. Six values catch a wrong connective and an off-by-one at either end."),
            ("Decide how the error is handled",
             "If the value comes from outside the program, the check needs error handling; "
             "if it can be wrong only through a bug, an assertion."),
            ("Do it on your own code",
             "Take one input check from your own code and its documented range, and type the "
             "condition, the range and what a true check means into the lab. Note where it "
             "disagrees, if anywhere, and write down which boundary test exposes it."),
        ],
        "worked": {
            "title": "A check that never fires",
            "intro": [
                "Test <code>never-fires</code>, `month < 1 && month > 12`, meant to flag an "
                "invalid month.",
            ],
            "lines": [
                "month 0: 0 < 1 is true, 0 > 12 is false: false",
                "month 13: 13 < 1 is false, 13 > 12 is true: false",
                "no integer is below 1 and above 12",
                "the check is always false",
                "invalid months 0 and 13 pass: disagreement",
            ],
            "after": [
                "Each comparison is right on its own; the connective joins two conditions "
                "that cannot both hold. With `||` in its place the check flags 0 and below "
                "and 13 and above, which is <code>correct</code>.",
            ],
        },
        "quiz_title": "Checks, assertions and the rule",
        "quiz": [
            {"q": "In the exercise, `score >= 0 || score <= 100` is meant to be true for a "
                  "valid score, 0 to 100. Where is it wrong, and what is the fix?",
             "a": ["Nowhere; it is correct as written",
                   "On −1 and below and 101 and above; the tests −1 and 101 expose it; the "
                   "connective should be `&&`",
                   "On 101 and above only; the test 101 exposes it; `<=` should be `<`",
                   "On 0 to 100; the tests 0 and 100 expose it; the connective should be `&&`"],
             "c": 1,
             "why": "Every `int` is at least 0 or at most 100, so the check is always true. "
                    "It therefore agrees on 0 to 100 and wrongly accepts −1 and below and 101 "
                    "and above; the boundary tests −1 and 101 expose it. Joined by `&&`, a "
                    "value must satisfy both comparisons, which is the range."},
            {"q": "A routine reads a quantity from a file a customer uploaded. By section "
                  "8.2's rule, how should it treat a quantity of −5?",
             "a": ["With an assertion, since a negative quantity should never happen",
                   "With error-handling code, since bad data in an uploaded file is to be "
                   "expected",
                   "Not at all, since the file is the customer's responsibility",
                   "With an assertion, and remove it from production"],
             "c": 1,
             "why": "Error handling is for conditions you expect to occur, and data from an "
                    "external source can be bad; an assertion is for a condition that can "
                    "only be false if the program has a bug."},
            {"q": "A quantity is valid from 1 to 99, and the check `qty > 0 && qty < 99` is "
                  "meant to be true for a valid one. On which integers is it wrong?",
             "a": ["0", "99", "100", "None"],
             "c": 1,
             "why": "`qty > 0` is right for the low end. `qty < 99` rejects 99, which is "
                    "valid, so the check is wrong on 99 alone; 100 is correctly rejected. "
                    "The boundary test 99 exposes it."},
            {"q": "In section 8.3's terms, what does correctness mean?",
             "a": ["Always doing something that keeps the program running",
                   "Never returning an inaccurate result, even if that means returning none",
                   "Handling every error locally",
                   "Asserting every precondition"],
             "c": 1,
             "why": "Correctness means never returning an inaccurate result; robustness "
                    "means always trying to keep going, even at the cost of an inaccurate "
                    "result. Safety-critical programs, the section says, favour the first; "
                    "consumer programs often the second."},
        ],
        "mistakes": [
            ("Using an assertion to handle bad input",
             "An assertion looks like a check, so it is tempting to write one for a user's "
             "entry or a field in a file. Section 8.2 draws the line: input from outside is "
             "a condition you expect to occur, and gets error handling; an assertion "
             "states what can never happen if the program is right, and may be compiled "
             "out. In Java it is off unless the program runs with <code>-ea</code>, so an assertion "
             "on user input usually checks nothing at all."),
            ("Leaving error handling to each routine",
             "Each routine could pick whatever response suits it locally. Section 8.3 says "
             "the choice, robustness or correctness, a neutral value or a shutdown, affects "
             "whether the program meets its requirements, and should be made once, at the "
             "level of the architecture, and followed consistently. That is the key point "
             "this lesson opens with."),
            ("Testing only values far from the ends",
             "A check that flags 0 and 50 can still be wrong at an end. Type "
             "`month < 1 || month > 13` into the lab: it flags 0 and 50 correctly, lets 13 "
             "through, and only the boundary test 13 shows it. The boundary tests exist to "
             "try exactly the values next to each end."),
        ],
        "standard": (
            "Finish when you can find where a range check is wrong by hand.",
            "Given a valid interval and a check, name the integers the check gets wrong, "
            "from its comparisons and its connective, and the boundary tests that expose "
            "them."
        ),
        "note": (
            "The lab evaluates a condition on one integer and cannot see where the value "
            "comes from, so it cannot say whether the check should be error handling or an "
            "assertion; that is section 8.2's rule applied to your design. The month and "
            "the checks are the lesson's illustration."
        ),
    },
    # ---------------------------------------------------------------- 08
    # McConnell Chapter 8, sections 8.4-8.8, pp. 198-213.
    # Quote: p. 205, 24 words, cc_quotes.py OK; "Dog Breath", p. 210, 2 words.
    # Lesson total: 26 words.
    # Exceptions (pp. 198-203); barricades, Figure 8-2 named only, the
    # operating room, converting input (pp. 203-204); barricades and
    # assertions (p. 205); debugging aids and offensive programming, after
    # Howard and LeBlanc 2003 (pp. 205-209); production code, Mars
    # Pathfinder after March 1999, "Dog Breath" (pp. 209-210); section 8.8
    # (p. 210).
    {
        "slug": "exceptions-and-barricades",
        "title": "Exceptions and Barricades",
        "module": "Chapter 8 · Defensive Programming",
        "one_line": "Validate data where it crosses into the program and assert it inside: the barricade decides which checks are error handling and which are assertions.",
        "summary": (
            "Sections 8.4 to 8.8 cover exceptions, the barricade, debugging aids and how much "
            "defensive code to keep. Classify each value in a design by where it comes from, "
            "say what the barricade rule asks of it, and count the values that break the "
            "rule."
        ),
        "key": [
            "outside the barricade: validate",
            "inside the barricade: assert",
            "bad data inside: a bug, not bad input",
            "throw at the right level of abstraction",
            "too much defence is a defect source",
        ],
        "key_label": "Sections 8.4 to 8.8 in five lines",
        "concepts_intro": (
            "The second half of Chapter 8 adds one mechanism and one design idea, and closes "
            "on how much of either to keep."
        ),
        "concepts": [
            ("Exception",
             "A way for code that cannot handle an error to pass it up to code that can. "
             "Its benefit, the chapter says, is that an error signalled this way cannot be "
             "ignored."),
            ("Barricade",
             "A set of interfaces chosen as the boundary of a safe area. Code at the boundary "
             "validates and sanitises what crosses it; code inside may assume the data is "
             "clean."),
            ("Offensive programming",
             "Making errors impossible to overlook during development, so that they can be "
             "handled gently in production: the book takes the term from Howard and LeBlanc "
             "(2003)."),
        ],
        "read_title": "The chapter's argument first, then a boundary classified",
        "read_intro": (
            "Read sections 8.4 to 8.8, pages 198 to 213, in your own copy first. The lesson "
            "sets out the argument and then applies the barricade rule to six values of an "
            "order system."
        ),
        "body": [
            ("p", "&ldquo;Routines inside the barricade should use assertions, because the "
                  "data passed to them is supposed to be sanitized before it’s passed across "
                  "the barricade.&rdquo; That sentence is from section 8.5 (p. 205), and it "
                  "is the rule this lesson applies. The lesson reads sections 8.4 to 8.8, "
                  "pages 198 to 213. Read them in your own copy first."),
            ("p", "The previous lesson ended on a question: which checks are error handling "
                  "and which are assertions? Before it answers, the chapter adds a mechanism. "
                  "Section 8.4 is on exceptions, which let code that does not know what to "
                  "do about an error throw it to code up the calling chain that might. Their "
                  "great benefit, it says, is that an error cannot be silently ignored; their "
                  "cost is that callers must know what a routine may throw, which weakens "
                  "encapsulation. Java goes further than most languages here: a checked "
                  "exception must be declared, and caught or passed on, or the code does not "
                  "compile."),
            ("p", "The section's guidelines follow from that trade. Throw only for conditions "
                  "that are truly exceptional, and do not use an exception to pass the buck "
                  "on an error you could handle locally. Throw at the level of abstraction of "
                  "the routine's interface: the book's example is an employee class whose "
                  "tax-id routine lets an end-of-file exception escape, which tells every "
                  "caller how employees are stored. Put the facts that led to the exception "
                  "in its message; do not write an empty `catch` block, or if one is truly "
                  "right, say why; standardise how the project uses exceptions; and consider "
                  "the alternatives, since a language having exceptions is not a reason to "
                  "use them."),
            ("p", "Section 8.5 is the barricade. Like the watertight compartments of a hull or "
                  "a building's firewalls, it confines damage: choose certain interfaces as "
                  "the boundary of a safe area, make the code there check and clean whatever "
                  "crosses it, and let the code inside assume the data is good. The book "
                  "draws it in Figure 8-2, with the validation classes between the external "
                  "sources and the internal classes, and compares it to an operating room: "
                  "everything is sterilised before it goes in. Convert input to its proper "
                  "type as it arrives. The same idea works for one class, whose public "
                  "routines check and whose private ones assume. And it makes section 8.2's "
                  "rule clean-cut: outside, error handling; inside, assertions; bad data "
                  "found inside is an error in the program, not in the data."),
            ("p", "Sections 8.6 to 8.8 turn to development and production. Do not let the "
                  "production version's limits bind the development version: give it "
                  "debugging aids, introduce them early, and program offensively, making "
                  "asserts abort and failures loud so that they are fixed, then plan to "
                  "remove the aids without editing the code by hand. In production, keep the "
                  "checks for important errors and drop the trivial ones, take out what "
                  "crashes hard, and keep what lets a program fail gracefully; engineers on "
                  "the Mars Pathfinder, the book reports, diagnosed a fault after landing "
                  "with debug code they had left in. Make the messages you leave in "
                  "friendly; McConnell's own once called a user &ldquo;Dog Breath&rdquo;. And "
                  "be defensive about defensive programming: code that checks everything "
                  "everywhere is fat and slow, and its own checks can be wrong."),
            ("p", "Now the count. The lab's barricade view takes records `value, side, "
                  "handling`: where each value comes from, `outside` or `inside`, and what the "
                  "design does with it, `validate`, `assert` or `none`. It prints the number "
                  "of values and four lists that the rule picks out: outside and unchecked, "
                  "outside and only asserted, inside and unchecked, and inside and "
                  "validated. The preset <code>mixed</code> has six values and prints 6, "
                  "then 1: uploadName, 1: feedPrice, 1: customerId and 0: none."),
            ("p", "Take them in turn. `uploadName` arrives from outside and nobody checks it. "
                  "`feedPrice` comes from a supplier's real-time feed, also outside, and is "
                  "only asserted: with assertions off it passes unchecked, and with them on a "
                  "bad price stops the program instead of being handled. `customerId` is "
                  "inside and unchecked, where the rule asks for an assertion to state what "
                  "the barricade promised. In <code>barricaded</code> the three outside "
                  "values are validated and the three inside asserted, and all four lists "
                  "print 0: none. In <code>checks-everywhere</code> all six are validated, "
                  "and the last list prints 3: lineTotal, customerId, taxDue."),
            ("p", "The counts are the rule applied to the records, not a verdict. Section 8.2 "
                  "itself allows a large, long-lived system to assert a condition and handle "
                  "it anyway, so an entry in the last list can be a choice. What the lab "
                  "cannot do is decide which side a value is on: that is the design "
                  "decision, and the exercise is about it."),
            ("h3", "Exercise"),
            ("ol", [
                "a quantity typed into a form;",
                "a file name from an upload;",
                "a price from a supplier's feed;",
                "a line total the routine computed itself;",
                "an index into the routine's own array;",
                "a customer id passed in from the order class, which validated it;",
                "a tax rate read from a configuration file;",
                "a discount the pricing class computed after validation;",
                "a date parsed from an e-mail.",
            ]),
            ("p", "These are nine values in an order system. Mark each <em>validate</em>, "
                  "<em>assert</em> or <em>neither</em> by the barricade rule, give the reason "
                  "for each, and say which one is open to argument and why. You can type "
                  "your classification into the lab afterwards as records."),
            ("p", "Chapter 9 turns from what a routine defends against to how a routine is "
                  "written. The next lesson is The Pseudocode Programming Process."),
        ],
        "lab": ("cckit", {
            "mode": "cond",
            "view": "barricade",
            "preset": "mixed",
            "presets": [
                {"id": "mixed",
                 "label": "Mixed: some values on the wrong side of the rule (illustrative)",
                 "values": "quantityField, outside, validate; uploadName, outside, none; "
                           "feedPrice, outside, assert; lineTotal, inside, assert; "
                           "customerId, inside, none; taxDue, inside, assert",
                 "expect": {"cdOutsideUnchecked": "1: uploadName",
                            "cdOutsideAsserted": "1: feedPrice",
                            "cdInsideUnchecked": "1: customerId",
                            "cdInsideValidated": "0: none"}},
                {"id": "barricaded",
                 "label": "Barricaded: outside validated, inside asserted",
                 "values": "quantityField, outside, validate; uploadName, outside, validate; "
                           "feedPrice, outside, validate; lineTotal, inside, assert; "
                           "customerId, inside, assert; taxDue, inside, assert",
                 "expect": {"cdOutsideUnchecked": "0: none",
                            "cdOutsideAsserted": "0: none",
                            "cdInsideUnchecked": "0: none",
                            "cdInsideValidated": "0: none"}},
                {"id": "checks-everywhere",
                 "label": "Checks everywhere: every value validated",
                 "values": "quantityField, outside, validate; uploadName, outside, validate; "
                           "feedPrice, outside, validate; lineTotal, inside, validate; "
                           "customerId, inside, validate; taxDue, inside, validate",
                 "expect": {"cdOutsideUnchecked": "0: none",
                            "cdOutsideAsserted": "0: none",
                            "cdInsideUnchecked": "0: none",
                            "cdInsideValidated": "3: lineTotal, customerId, taxDue"}},
            ],
            "panel_title": "Apply the barricade rule",
            "panel_intro": (
                "Each record is a value, the side of the barricade it comes from, and what the "
                "design does with it. The lab lists the values the chapter's rule picks out: "
                "outside values left unchecked or only asserted, inside values left unchecked "
                "or validated. The rule is section 8.5's, and the lists are not a verdict."
            ),
        }),
        "steps_title": "Placing a barricade",
        "steps_intro": "Five steps, the last of them on a boundary in your own system.",
        "steps": [
            ("Draw the boundary",
             "Decide which interfaces are the barricade: the routines that receive data from "
             "users, files, networks or other systems."),
            ("Place each value",
             "For each value, ask where it was last outside the program's control. If it "
             "crossed the boundary without being checked, it is outside."),
            ("Apply the rule",
             "Outside values get error handling at the boundary; inside values get "
             "assertions, which state what the barricade promised."),
            ("Read the exceptions as choices",
             "Where you assert and handle, or validate inside, write down why. Section 8.8 "
             "allows judgement, and a reason is what makes it judgement."),
            ("Do it on your own code",
             "Pick one boundary in your own system, an API handler or a file reader, and "
             "type the values that cross it into the lab as value, side, handling records. "
             "Note every value the four lists name, and write one sentence on the one you "
             "would change first."),
        ],
        "worked": {
            "title": "A price from a feed, only asserted",
            "intro": [
                "In <code>mixed</code>, `feedPrice` is a price that arrives from a "
                "supplier's real-time feed and is checked only by an assertion.",
            ],
            "lines": [
                "feedPrice: from a feed, so outside",
                "outside values get error handling",
                "it has only an assertion",
                "assertions off: a bad price passes",
                "assertions on: a bad price stops the program",
            ],
            "after": [
                "Either way the bad price is not handled: it is let through or treated as a "
                "bug in the program. A feed sends bad data from time to time, which is what "
                "error handling at the barricade is for.",
            ],
        },
        "quiz_title": "Barricades and exceptions",
        "quiz": [
            {"q": "In the exercise's nine values, how many does the barricade rule mark "
                  "<em>validate</em>, and which is the one to argue about?",
             "a": ["Five; the tax rate from the configuration file",
                   "Four; the date parsed from the e-mail",
                   "Five; the customer id from the order class",
                   "Six; the discount the pricing class computed"],
             "c": 0,
             "why": "Validate the form quantity, the upload's file name, the feed price, the "
                    "configuration tax rate and the e-mailed date, five values from outside. "
                    "Assert the computed line total, the array index, the customer id the "
                    "order class validated and the discount computed after validation, four "
                    "inside. The tax rate is the one to argue about: the team writes the "
                    "configuration, but it is read from outside the program, and section "
                    "8.1 treats a file as an external source. Nothing here is neither: the "
                    "array index never crossed the barricade, but section 8.2 still asks for a "
                    "precondition on it, which is what an assertion is for."},
            {"q": "A routine inside the barricade finds a negative quantity. By section 8.5, "
                  "what has gone wrong?",
             "a": ["The user typed a bad value, which the routine should handle",
                   "Nothing; inside routines must check everything again",
                   "There is an error in the program, not in the data",
                   "The data should have been asserted at the boundary"],
             "c": 2,
             "why": "Data inside the barricade is supposed to have been sanitised, so bad data "
                    "there means the program let it through or made it: a bug. The boundary "
                    "validates; it does not assert."},
            {"q": "Records `a, outside, assert; b, inside, validate; c, outside, none`. What "
                  "do the lab's four lists print, in order: outside unchecked, outside only "
                  "asserted, inside unchecked, inside validated?",
             "a": ["1: c; 1: a; 0: none; 1: b",
                   "1: a; 1: c; 0: none; 1: b",
                   "2: a, c; 0: none; 0: none; 1: b",
                   "1: c; 1: a; 1: b; 0: none"],
             "c": 0,
             "why": "`c` is outside with no handling, `a` outside with only an assertion, "
                    "nothing is inside and unchecked, and `b` is inside and validated. An "
                    "assertion is not nothing, so `a` is not unchecked."},
            {"q": "An `Employee` routine that returns a tax id lets an end-of-file exception "
                  "from its file reader escape to callers. What does section 8.4 say is "
                  "wrong?",
             "a": ["Nothing, as long as the exception is documented",
                   "The exception is at the wrong level of abstraction, and exposes how "
                   "employees are stored",
                   "Exceptions should never leave a routine",
                   "It should be an empty `catch` block instead"],
             "c": 1,
             "why": "Exceptions are part of a routine's interface, and an end-of-file exception "
                    "tells callers the data comes from a file. The section's advice is to throw "
                    "an exception at the class's own level, an employee-data exception, and "
                    "never to swallow it in an empty `catch`."},
        ],
        "mistakes": [
            ("Thinking defensive programming means checking everything everywhere",
             "If checks are good, more checks should be better. The lesson's "
             "<code>checks-everywhere</code> is that design: every value validated, inside "
             "the barricade as well as at it. Section 8.5 puts the checks at the barricade and "
             "assertions inside, and section 8.8 warns that too much defensive code makes a "
             "program fat and slow and is itself a source of defects."),
            ("Leaving an empty catch block in code that works",
             "An empty `catch` keeps the program running, which can look like robustness. "
             "Section 8.4 reads it the other way: either the code in the `try` is wrong to "
             "raise the exception or the `catch` is wrong to ignore it. Find which, and if an "
             "empty block really is right, say why in it."),
            ("Stripping every debugging aid from production",
             "Assertions and debug checks belong to development, so they might all come "
             "out. Section 8.7 keeps some: checks for important errors, code that lets the "
             "program fail gracefully, and logging for support. The book's example is the "
             "Mars Pathfinder, diagnosed after landing with debug code left in by design."),
        ],
        "standard": (
            "Finish when you can place a value relative to a barricade and say why.",
            "For nine values, mark each validate, assert or neither by the barricade rule, "
            "and give the reason for each."
        ),
        "note": (
            "The lab applies section 8.5's rule to the sides and handling you type; it cannot "
            "decide which side of the barricade a value is on, which is the design decision "
            "the chapter is about, and section 8.8 leaves room for judgement it cannot "
            "model. The order system's values are the lesson's illustration."
        ),
    },
    # ---------------------------------------------------------------- 09
    # McConnell Chapter 9, sections 9.1-9.4, pp. 215-234.
    # Quote: p. 234 (Key Points), 28 words, cc_quotes.py OK; "Just One More
    # Compile", p. 231, 4 words. Lesson total: 32 words.
    # Steps for classes and routines (pp. 216-217); pseudocode for pros and
    # its benefits (pp. 218-220); the PPP: design, code, check, clean up,
    # repeat (pp. 220-232); compiling late (pp. 230-231); alternatives, and
    # forgetting part of a routine (pp. 232-233).
    {
        "slug": "the-pseudocode-programming-process",
        "title": "The Pseudocode Programming Process",
        "module": "Chapter 9 · The Pseudocode Programming Process",
        "one_line": "Write a routine first as English comments at the level of intent, then fill in code beneath each, so that every step's code is where you can see it.",
        "summary": (
            "Chapter 9 sets out the steps for building classes and routines and McConnell's "
            "preferred way of building a routine: design it in pseudocode, turn the "
            "pseudocode into comments, write the code beneath each, and check it. Check that "
            "every pseudocode comment in a routine has the code it promised, and that the "
            "code is right for the language."
        ),
        "key": [
            "pseudocode: English, at the level of intent",
            "each line becomes a comment",
            "fill in the code under each comment",
            "a step with nothing under it: look",
            "check it before you compile it",
        ],
        "key_label": "Chapter 9 in five lines",
        "concepts_intro": (
            "The chapter's process needs three terms, and the book defines them more "
            "narrowly than everyday use does."
        ),
        "concepts": [
            ("Pseudocode",
             "An informal, English-like description of what a routine will do. The chapter "
             "asks for precise English at the level of intent, with no syntax from the target "
             "language."),
            ("The Pseudocode Programming Process",
             "Design a routine in pseudocode, refine it until coding is nearly mechanical, "
             "turn each line into a comment, fill in the code beneath each, then check and "
             "clean up."),
            ("A step",
             "One pseudocode line, kept as a comment, with the code that carries it out "
             "beneath. A step with no code beneath it is a promise the routine does not keep."),
        ],
        "read_title": "The process first, then a routine checked against its steps",
        "read_intro": (
            "Read Chapter 9, pages 215 to 234, in your own copy first. The lesson sets out "
            "the process and then checks one routine's steps against its code."
        ),
        "body": [
            ("p", "&ldquo;The Pseudocode Programming Process is a useful tool for detailed "
                  "design and makes coding easy. Pseudocode translates directly into "
                  "comments, ensuring that the comments are accurate and useful.&rdquo; That "
                  "is one of Chapter 9's key points (p. 234). This lesson reads the whole "
                  "chapter, pages 215 to 234. Read it in your own copy first."),
            ("p", "You may know the feeling of finishing a routine, seeing it compile and "
                  "pass the tests you thought of, and finding a week later that one thing it "
                  "was meant to do it never does: the branch you meant to write and did not. "
                  "Chapter 9 claims a way of working that makes that rare, and it says so: "
                  "forgetting to write part of a routine, it says, hardly ever happens if you "
                  "use the process."),
            ("p", "Section 9.1 places the process. A class is built by designing it as a "
                  "whole, constructing each routine, and reviewing and testing the class, and "
                  "the steps loop back on each other; a routine is built by designing it, "
                  "checking the design, coding it and checking the code. Section 9.2 says "
                  "what good pseudocode is: precise English statements; no syntax from the "
                  "programming language; written at the level of intent, saying what the "
                  "approach means rather than how it will be coded; and low enough that "
                  "writing the code from it is nearly automatic. Its benefits, the chapter "
                  "says, are easier reviews, refinement in small steps, cheaper changes, and "
                  "comments that cost nothing extra and stay accurate."),
            ("p", "Section 9.3 is the process itself, worked on an error-reporting routine in "
                  "the book. Design the routine: check the prerequisites, state what it hides, "
                  "its inputs and outputs and its pre- and postconditions, name it, decide how "
                  "to test it, look for it in the libraries, think about errors and "
                  "efficiency, then write the pseudocode from a header comment down, check "
                  "it, and try several versions. Code it: write the declaration, then the "
                  "first and last lines, turn the pseudocode into comments, and fill in the "
                  "code beneath each. If one comment grows too much code, make it a routine "
                  "of its own, or apply the process to it again."),
            ("p", "Then check the code: execute each path in your head, and know why each "
                  "line works, because, the chapter says, nothing is right just because it "
                  "seems to work. It recommends compiling only when you believe the routine "
                  "is right, warning against the &ldquo;Just One More Compile&rdquo; habit, "
                  "then stepping through the code in a debugger and testing it. Clean up: "
                  "check the interface, the variables, the logic, the layout and whether the "
                  "comments are still accurate, and remove any made redundant. Repeat as "
                  "needed. Section 9.4 names the alternatives: test-first development (Beck "
                  "2003), refactoring (Fowler 1999), design by contract (Meyer 1997), and "
                  "hacking."),
            ("p", "Now the count. The lab's pseudocode view reads a routine written this way "
                  "and treats each comment inside its body as a step. It prints the steps, "
                  "the statement lines in the body, the steps with no code beneath them "
                  "(flagged in the listing), and the most code under any one step. The preset "
                  "<code>free-slot</code>, below, has 5 steps and 7 statement lines; the most "
                  "code under one step is 3 lines, under line 8; and one step is empty, "
                  "line 14. A step's code runs to the next comment, so a loop header and "
                  "an `if` belong to the step above them."),
            ("code", {"lines": _lines(FREE_SLOT), "marked": [14]}),
            ("p", "Line 14 says that if no slot is free the routine logs the overflow, and "
                  "nothing under it does: a full table is reported to nobody. The process kept "
                  "the promise in plain sight, which is why the lab can find it. There is a "
                  "second point in the listing. Line 15, &ldquo;return -1&rdquo;, is "
                  "pseudocode at the level of the language, not of intent, which section 9.2 "
                  "says to avoid; at the level of intent it would say that the routine reports "
                  "that no slot was found. In <code>complete</code>, below, a call to "
                  "`log.warn` sits under the step, and the lab prints 5 steps, 8 statement "
                  "lines and no empty step."),
            ("code", {"lines": _lines(COMPLETE), "marked": [15]}),
            ("p", "What the lab cannot check is whether the code under a step does what the "
                  "step says, or whether it is right for the language. That is the check the "
                  "process asks of you, and the exercise is one where the obvious line of "
                  "code is the wrong one."),
            ("h3", "Exercise"),
            ("code", _lines(EXPIRE_SESSIONS_EXERCISE)),
            ("p", "Find the step with no code beneath it and say what the routine fails to do "
                  "because of it. Then write the obvious one-line fix and say whether it is "
                  "right in Java, and if it is not, what the step needs instead. You can paste "
                  "the routine into the lab afterwards to check the step count."),
            ("p", "That ends Creating High-Quality Code. The next course, Variables, begins "
                  "with Declaring and Initializing Variables, on Chapter 10."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "ppp",
            "preset": "free-slot",
            "presets": [
                {"id": "free-slot",
                 "label": "Find a free slot, with one step left empty",
                 "code": FREE_SLOT,
                 "expect": {"coSteps": "5", "coEmpty": "line 14"}},
                {"id": "complete",
                 "label": "The same routine with the overflow logged",
                 "code": COMPLETE,
                 "expect": {"coSteps": "5", "coEmpty": "none"}},
            ],
            "panel_title": "Check a routine against its pseudocode",
            "panel_intro": (
                "Paste a Java routine written with its pseudocode kept as comments. The lab "
                "treats each comment inside the body as a step, counts the statement lines, "
                "and flags each step with no code beneath it. Whether the code does what its "
                "step says is for you to check."
            ),
        }),
        "steps_title": "Building a routine from pseudocode",
        "steps_intro": "Five steps, the last of them on a routine you are about to write.",
        "steps": [
            ("Write the header comment",
             "State in one or two sentences what the routine does. If that is hard to write, "
             "the routine's role is not yet clear."),
            ("Write the steps in English",
             "Write the routine as pseudocode at the level of intent: what each step "
             "achieves, with no syntax from the language."),
            ("Turn the steps into comments",
             "Write the declaration and the braces, put each pseudocode line inside as a "
             "comment, and fill in the code beneath each."),
            ("Check each step against its code",
             "For every comment, confirm the code beneath it does what it says and is right "
             "for the language. A comment with nothing beneath it is a step not done."),
            ("Do it on your own code",
             "Before writing your next routine, write it as about five pseudocode comments. "
             "Fill in the code beneath them, paste the routine into the lab, and note the "
             "step count and any empty step it flags."),
        ],
        "worked": {
            "title": "Five steps and one gap",
            "intro": [
                "Read <code>free-slot</code> step by step and count the code beneath each.",
            ],
            "lines": [
                "line 3, start after the last used: one line",
                "line 5, look at each slot once: two lines",
                "line 8, if free, remember and return: three lines",
                "line 14, log the overflow: nothing",
                "line 15, return minus one: one line",
                "steps 5, statement lines 7, empty: line 14",
            ],
            "after": [
                "The gap is visible because the step was written down before the code. "
                "Without the comment on line 14, the routine would simply be one that does "
                "not log, and nothing on the page would say it was meant to.",
            ],
        },
        "quiz_title": "Steps and their code",
        "quiz": [
            {"q": "In the exercise's `expireSessions`, which step is empty, and is "
                  "`sessions.remove(s);` inside the loop the right fix in Java?",
             "a": ["Line 8 is empty; yes, add `archive.add(s);` beneath it",
                   "Line 10 is empty; yes, `sessions.remove(s);` beneath it is correct",
                   "Line 10 is empty; no, removing from the list inside its enhanced `for` "
                   "breaks the iteration, so the step needs an explicit `Iterator`",
                   "No step is empty; the routine is correct"],
             "c": 2,
             "why": "The routine has 4 steps, and line 10, remove it from the live list, has "
                    "no code, so expired sessions stay live. Calling `sessions.remove(s)` "
                    "inside the enhanced `for` changes the list behind its iterator: on an "
                    "`ArrayList` the next pass throws `ConcurrentModificationException`, and "
                    "when the removed element was second to last the loop silently ends and "
                    "skips the last one instead. The step needs a loop over an explicit "
                    "`Iterator`, calling `it.remove()`, or a loop over a copy. Writing the "
                    "step down first is what shows it needs a different loop. Line 8 has "
                    "its code, `archive.add(s)` on line 9."},
            {"q": "Which of these is pseudocode at the level of intent, as section 9.2 asks?",
             "a": ["`if (table[i].isFree())`",
                   "set i to (start + step) mod length",
                   "look at each slot once, wrapping around the end",
                   "return -1"],
             "c": 2,
             "why": "Intent says what the step achieves. The first is Java; the second is the "
                    "code in words; return -1 is at the level of the language, as the lesson's "
                    "line 15 is."},
            {"q": "A routine has the comments `// read the order`, `// price each line` and "
                  "`// total the lines`, and code under the first and the third only. What "
                  "does the lab report?",
             "a": ["3 steps, no empty step", "3 steps, 1 empty step",
                   "2 steps, no empty step", "3 steps, 2 empty steps"],
             "c": 1,
             "why": "Each comment in the body is a step: 3. The second has no code beneath it "
                    "before the next comment, so it is empty: 1."},
            {"q": "When does section 9.3 recommend compiling a routine written by the process?",
             "a": ["After every line, to catch errors early",
                   "Once you are convinced the routine is right, after checking it yourself",
                   "Only after the routine has been tested",
                   "Never before a code review"],
             "c": 1,
             "why": "The chapter advises compiling late, after reviewing the routine, because "
                    "compiling early starts a cycle of "
                    "hasty changes. Testing comes after compiling, in a debugger and with the "
                    "planned test cases."},
        ],
        "mistakes": [
            ("Treating pseudocode as a draft to delete once the code works",
             "If pseudocode is scaffolding, it goes when the building stands. The process "
             "keeps it as the routine's comments, which is why its comments are accurate and "
             "why a step with nothing beneath it is a defect a reader can see. On the lesson's "
             "illustration, delete the comments from <code>free-slot</code> and the missing "
             "log is no longer missing from anything: the routine just does not log."),
            ("Writing pseudocode in the language's own terms",
             "Pseudocode full of brackets and calls looks precise. Section 9.2 says it sinks "
             "to the level of the code and loses what design at a higher level was for; it "
             "also makes poor comments, since it repeats the code. Write what each step "
             "achieves, as line 3 of <code>free-slot</code> does, not how, as line 15 does."),
            ("Trusting a routine because it compiles and seems to work",
             "Section 9.3 is blunt: nothing is right just because it seems to work, and if "
             "you do not know why it works, it probably does not. Check each step against its "
             "code by hand before compiling, and know why each line is there."),
        ],
        "standard": (
            "Finish when you can check a routine against its pseudocode.",
            "For a routine written by the process, list its steps, find any step with no "
            "code beneath it, and name the code that is missing and whether it is right for "
            "the language."
        ),
        "note": (
            "The lab counts comments and the code lines beneath them; it cannot tell whether "
            "the code does what its step says, or whether it is valid Java, which is the "
            "check the process asks of you. The routines are the lesson's own. McConnell "
            "calls the process his favourite, and names test-first development, refactoring "
            "and design by contract as alternatives or supplements; the lesson does not "
            "rank them."
        ),
    },
]
