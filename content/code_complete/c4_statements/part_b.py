"""Statements, lessons 5-7 -- Chapters 18 and 19 of Code Complete, 2nd ed.

Table-driven methods, boolean expressions, and deep nesting with the
decision-point count that closes the course. Pages are the second edition's
(Microsoft Press, 2004); each opening quotation was checked character for
character against the text. The Java snippets are written for these lessons
(the shipping-cost pair and discountPercent are PLAN §D.4's); each is one
constant, used by the lesson's code block and, where a code lab counts it, by
the preset.
"""

# ---------------------------------------------------------------- snippets

# Table-Driven Methods: the late-fee table as code (the lab's instance), and
# the exercise's shipping table.
LATE_FEE = """static final int[] DAYS_BELOW = {7, 14, 30, 60, 365};
static final int[] FEE = {0, 2, 5, 10, 20};

int lateFee(int daysOverdue) {
    for (int step = 0; step < DAYS_BELOW.length; step++) {
        if (daysOverdue < DAYS_BELOW[step]) {
            return FEE[step];
        }
    }
    return FEE[FEE.length - 1];
}"""

SHIP_RATES = """// the top of each weight step in kilograms, and its price
static final int[] STEP_KG = {1, 5, 20, 70};
static final int[] PRICE = {5, 9, 15, 40};"""

# Boolean Expressions: a loop whose guard and inner test are one condition
# written two ways, and the exercise.
DRAIN = """void drain(Queue queue) {
    boolean done = false;
    boolean error = false;
    while (!(done || error)) {
        done = queue.isEmpty();
        error = queue.hasFailed();
        if (!done && !error) {
            queue.processNext();
        }
    }
}"""

OWNER_TEST = """if (!(isAdmin || !isOwner)) {
    showOwnerTools();
}"""

# Nesting and Complexity. PLAN §D.4 <code>nested-shipping</code> (22 lines: the nesting
# is the lesson), <code>guard-clauses</code>, and the exercise `discountPercent`.
NESTED_SHIPPING = """double shippingCost(Order order) {
    double cost = 0.0;
    if (order != null) {
        if (order.weight() > 0) {
            if (order.isDomestic()) {
                if (order.weight() < 2 && !order.isExpress()) {
                    cost = 5.0;
                } else {
                    cost = 9.0 + order.weight();
                }
            } else {
                for (Item item : order.items()) {
                    if (item.isRestricted() || item.weight() > 30) {
                        return -1.0;
                    }
                }
                cost = 25.0 + 2 * order.weight();
            }
        }
    }
    return cost;
}"""

GUARD_CLAUSES = """double shippingCost(Order order) {
    if (order == null || order.weight() <= 0) {
        return 0.0;
    }
    if (!order.isDomestic()) {
        return internationalCost(order);
    }
    if (order.weight() < 2 && !order.isExpress()) {
        return 5.0;
    }
    return 9.0 + order.weight();
}"""

DISCOUNT = """int discountPercent(Customer c, Order o) {
    int pct = 0;
    if (c.isMember()) {
        pct = 5;
    }
    if (o.total() > 100 || c.years() > 3) {
        pct = pct + 5;
    }
    for (Coupon k : o.coupons()) {
        if (k.isValid() && !k.isUsed()) {
            pct = pct + k.percent();
        }
    }
    return pct;
}"""


def _lines(snippet):
    return snippet.split("\n")


LESSONS = [
    # ---------------------------------------------------------------- 05
    # McConnell Chapter 18, §§18.1-18.5, pp. 411-430. Opening quotation:
    # Key Points, p. 430 (27 words). General considerations, pp. 411-413
    # (the two issues: how to look up, what to store); direct access,
    # pp. 413-424 (days in a month, insurance rates, the flexible message
    # format, fudging lookup keys); indexed access, pp. 425-426; stair-step,
    # pp. 426-429 (endpoints, quasi-binary search, indexed instead, its own
    # routine); other examples, p. 429. The late-fee and shipping tables are
    # the lesson's (PLAN §R, MF-1), not the book's grading table.
    {
        "slug": "table-driven-methods",
        "title": "Table-Driven Methods",
        "module": "Chapter 18 · Table-Driven Methods",
        "one_line": "A lookup table moves a program's knowledge out of its if statements and into data, and the logic that remains, how a key finds its entry, is where a table's mistakes are made.",
        "summary": (
            "Chapter 18 sets out how to replace complicated logic with a table: what to "
            "store, and how to look an entry up, by direct, indexed or stair-step access. "
            "Look keys up in a stair-step table of late fees, count the comparisons a "
            "linear scan and a binary search make, and see the same key get two fees "
            "under two endpoint rules."
        ),
        "key": [
            "put the knowledge into the data",
            "direct, indexed or staircase access",
            "a step stores the top of its range",
            "endpoint: below the bound, or at or below",
            "long tables: search by halving",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "Chapter 18 asks two questions of every table, and names three answers to the "
            "first. The lesson uses three ideas."
        ),
        "concepts": [
            ("Table-driven method",
             "A scheme that looks information up in a table instead of working it out "
             "with if and case statements. The knowledge the tests held is stored as data, "
             "and the code that remains finds the entry."),
            ("Stair-step access",
             "A table whose entries each cover a range of keys. It stores the upper end of "
             "each range, and a key belongs to the first step whose upper end it does not "
             "pass."),
            ("The endpoint rule",
             "Whether a key equal to a step's upper end belongs to that step or the next: "
             "below the bound, or at or below it. Two tables with the same numbers and "
             "different rules give different answers at every boundary."),
        ],
        "read_title": "The chapter's argument first, then the staircase",
        "read_intro": (
            "The lesson goes through Chapter 18's five sections, looks keys up in a "
            "staircase of late fees with the lab, and ends with a table of shipping "
            "rates."
        ),
        "body": [
            ("p", "<strong>Chapter 18, p. 430.</strong> &ldquo;One key consideration in "
                  "using a table is deciding how to access the table. You can access "
                  "tables by using direct access, indexed access, or stair-step "
                  "access.&rdquo; It is the second of the chapter's three key points. "
                  "Read Chapter 18, pp. 411&ndash;430, in your own copy first."),
            ("p", "When should a chain of tests become a table? Section 18.1 (p. 411) "
                  "answers that almost anything you can select with logic statements you "
                  "can select with a table instead; in simple cases the logic is easier, "
                  "and as the logic grows the table becomes more attractive. A routine "
                  "that classifies characters with a long chain of comparisons can be "
                  "replaced by one array lookup indexed by the character, and the program's "
                  "knowledge then sits in its data instead of its tests. Every table "
                  "raises two questions: how to look an entry up, and what to store in "
                  "it, which may be data or, in some languages, a routine to run."),
            ("p", "Section 18.2 (p. 413) is direct access, where the key leads straight "
                  "to the entry: days in a month by the month's number, insurance rates "
                  "by age and other factors. Its long example, a program that prints "
                  "messages in many formats, is McConnell's case that a table can be "
                  "simpler than an object-oriented design with a class per format, and "
                  "his introduction points readers to it as an example of an "
                  "object-oriented design that is not better merely because it is "
                  "object-oriented. Where a key does not fit the table directly, the "
                  "section offers ways of fudging it: duplicate entries so that it does, "
                  "or transform the key, and in either case put the transformation in a "
                  "routine of its own. Section 18.3 (p. 425) is indexed access: a large, "
                  "mostly empty index maps the key to a position in a smaller main table, "
                  "which saves space when the main entries are large and lets one table "
                  "be reached by several indexes."),
            ("p", "Section 18.4 (p. 426) is stair-step access, for entries that hold for "
                  "ranges of keys rather than single values. Store the upper end of each "
                  "range and search for the first one the key falls under. The section's "
                  "subtleties are the lesson's subject: watch the endpoints, being careful "
                  "not to mistake `<` for `<=`, and make sure keys at the top fall into "
                  "the top range; for a long table consider a binary search, which he "
                  "calls quasi-binary because it finds a category rather than a value; "
                  "consider an indexed table instead when speed matters more than space; "
                  "and put the lookup in a routine of its own. Section 18.5 (p. 429) "
                  "lists where else in the book tables appear."),
            ("p", "Now a staircase. The lesson's library charges a late fee by the days "
                  "a book is overdue: nothing under 7 days, 2 under 14, 5 under 30, 10 "
                  "under 60 and 20 under 365. As code it is two arrays and a loop:"),
            ("code", _lines(LATE_FEE)),
            ("p", "The lab's <em>stairs</em> view takes the same table as records of "
                  "upper bound and value, a key, and a rule: <code>below</code>, the key "
                  "belongs to the first step whose bound it is below, as the loop's `<` "
                  "says, or <code>atmost</code>, at or below it. It prints the "
                  "<strong>value</strong> and two counts. <strong>Tests, linear "
                  "search</strong> is how many steps the loop compares the key with, from "
                  "the first, before one passes. <strong>Tests, binary search</strong> is "
                  "how many probes a search makes that tests the middle step, keeps the "
                  "half where the answer must lie, and stops when one step is left. In "
                  "the <code>days-20</code> preset a book 20 days overdue pays 5, after "
                  "3 linear tests, and the binary search finds it in 2."),
            ("p", "The two <code>days-60</code> presets look up the same key in the same "
                  "table. In <code>days-60-below</code>, 60 is not below 60, so the book "
                  "falls to the last step and pays 20, after 5 linear tests and 3 binary "
                  "probes. In <code>days-60-atmost</code>, 60 is at or below 60 and pays "
                  "10, after 4 tests and 3 probes. The table holds no logic, but the "
                  "endpoint rule does, and it is a decision about the library's policy "
                  "that the code has to state. The <code>brackets</code> preset is a "
                  "staircase of sixteen tax brackets, 1,000 wide, from 0% rising by 5% "
                  "to 75%. An income of 14,500 falls in the fifteenth, at 70%, after 15 "
                  "linear tests; the binary search takes 4, as it does for any key in a "
                  "sixteen-step table. That is the long table the chapter has in mind for "
                  "a binary search. On a short one it can lose: a book 5 days overdue "
                  "needs 1 linear test and 3 binary probes."),
            ("h3", "Exercise"),
            ("code", _lines(SHIP_RATES)),
            ("p", "A parcel weighs 5 kg. Using the two arrays as a stair-step table, what "
                  "does it cost, and how many comparisons do a linear search and the "
                  "lab's binary search make, if a parcel belongs to the first step whose "
                  "top it is below; and what if it belongs to the first step whose top it "
                  "is at or below? Work it by hand, then check both in the lab, and say "
                  "what the two arrays leave unstated."),
            ("p", "A table replaced the tests; the conditions inside tests remain. The "
                  "next lesson, Boolean Expressions, goes into them."),
        ],
        "lab": ("cckit", {
            "mode": "search",
            "view": "stairs",
            "steps": "7, 0; 14, 2; 30, 5; 60, 10; 365, 20",
            "preset": "days-20",
            "presets": [
                {"id": "days-20",
                 "label": "20 days overdue, below (the lesson's late-fee table)",
                 "key": 20, "rule": "below",
                 "expect": {"seValue": "5", "seLinear": "3", "seBinary": "2"}},
                {"id": "days-60-below",
                 "label": "60 days overdue, below",
                 "key": 60, "rule": "below",
                 "expect": {"seValue": "20", "seLinear": "5", "seBinary": "3"}},
                {"id": "days-60-atmost",
                 "label": "60 days overdue, at or below",
                 "key": 60, "rule": "atmost",
                 "expect": {"seValue": "10", "seLinear": "4", "seBinary": "3"}},
                {"id": "brackets",
                 "label": "Sixteen tax brackets, an income of 14,500 (illustrative)",
                 "steps": "; ".join("%d, %d%%" % (1000 * (i + 1), 5 * i) for i in range(16)),
                 "key": 14500, "rule": "below",
                 "expect": {"seValue": "70%", "seLinear": "15", "seBinary": "4"}},
            ],
            "panel_title": "A key on the staircase",
            "panel_intro": (
                "Each step is an upper bound and a value. The lab finds the key's step by "
                "a linear scan from the first step and by a binary search, and counts the "
                "comparisons each makes. The tables are the lesson's illustrations."
            ),
        }),
        "steps_title": "Looking a key up on a staircase",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("State the endpoint rule",
             "Decide, and write down, whether a key equal to a step's upper bound belongs "
             "to that step or the next."),
            ("Scan from the bottom",
             "Compare the key with each upper bound from the first, counting comparisons, "
             "until one passes. Its value is the answer."),
            ("Search by halving",
             "Probe the middle step; if the key passes it, the answer is that step or "
             "below, otherwise above. Repeat on the half that is left, counting probes, "
             "until one step remains."),
            ("Check the boundaries",
             "Look up a key equal to each upper bound, and one past the top, under the "
             "rule you stated. Those are where a table and its code disagree."),
            ("Do it on your own code",
             "Find one lookup in your own code written as a chain of ifs, write the table "
             "that would replace it with its endpoint rule stated, and type the table and "
             "one boundary key into the lab."),
        ],
        "worked": {
            "title": "Twenty days overdue",
            "intro": [
                "Take the days-20 preset: steps 7, 14, 30, 60 and 365, a key of 20, the "
                "rule below.",
            ],
            "lines": [
                "linear: 20 < 7 fails, 20 < 14 fails, 20 < 30 holds",
                "fee 5, after 3 tests",
                "binary: probe step 3 (30): 20 < 30, keep 1 to 3",
                "probe step 2 (14): fails, keep step 3",
                "one step left: fee 5, after 2 probes",
            ],
            "after": [
                "Both searches find the third step and the fee of 5. The binary search "
                "saves one comparison here and would lose two for a key of 5; on the "
                "sixteen-step table it saves eleven.",
            ],
        },
        "quiz_title": "Steps, endpoints and searches",
        "quiz": [
            {"q": "With the exercise's table (tops 1, 5, 20 and 70 kg; prices 5, 9, 15 "
                  "and 40), what does a 5 kg parcel cost, and how many comparisons do a "
                  "linear search and the lab's binary search make, under each endpoint "
                  "rule?",
             "a": ["Below: 15 (3 linear, 2 binary); at or below: 9 (2 linear, 3 binary)",
                   "Below: 9 (2 linear, 2 binary); at or below: 15 (3 linear, 3 binary)",
                   "15 under both rules (3 linear, 2 binary)",
                   "Below: 15 (3 linear, 3 binary); at or below: 9 (2 linear, 2 binary)"],
             "c": 0,
             "why": "Under below, 5 is not below 1 or 5 and is below 20, so it costs 15 "
                    "after 3 linear comparisons; the binary search probes 20 (passes) and "
                    "5 (fails): 2. Under at or below, 5 is at or below 5, so it costs 9 "
                    "after 2 linear comparisons; the binary search probes 20, 5 and 1: 3. "
                    "Which rule the business means is a question for the business, and "
                    "the table must say."},
            {"q": "In the late-fee table (bounds 7, 14, 30, 60, 365; fees 0, 2, 5, 10, "
                  "20), what does a book exactly 14 days overdue pay under the rule "
                  "below?",
             "a": ["0", "2", "5", "10"],
             "c": 2,
             "why": "14 is not below 7 and not below 14, and it is below 30, so it falls "
                    "in the third step: 5. Under at or below it would pay 2, which is the "
                    "endpoint rule at work."},
            {"q": "A stair-step table has 16 steps. How many probes does the lab's binary "
                  "search make for a key in it?",
             "a": ["16", "8", "5", "4"],
             "c": 3,
             "why": "Each probe halves what is left: 16, 8, 4, 2, 1. Four probes leave one "
                    "step, whatever the key. A linear scan takes anywhere from 1 to 16 "
                    "comparisons; for the brackets preset's 14,500 it takes 15."},
            {"q": "Which three ways of looking an entry up does Chapter 18 name?",
             "a": ["Direct access, indexed access and stair-step access",
                   "Linear search, binary search and hashing",
                   "Arrays, lists and maps",
                   "Direct access, sequential access and random access"],
             "c": 0,
             "why": "Section 18.1 lists direct access, indexed access and stair-step "
                    "access, each given a section of its own (pp. 412&ndash;429). Linear "
                    "and binary search are two ways of doing the stair-step lookup."},
        ],
        "mistakes": [
            ("Thinking a table is just a faster if chain",
             "Speed is one of the chapter's reasons, and not the main one. Its case is that "
             "a table moves the program's knowledge from the logic into data, where it is "
             "easier to read and to change. The logic that remains is the lookup, and the "
             "two days-60 presets show where it sits: the same key in the same table pays "
             "20 under below and 10 under at or below. On the lesson's illustration, the "
             "decision that the if chain spread across its tests is now one rule."),
            ("Assuming a binary search always beats a linear one",
             "On the late-fee table a key of 20 takes 3 linear tests and 2 binary probes, "
             "but a key of 5 takes 1 linear test and 3 probes. A binary search pays off on "
             "a long table, such as the sixteen tax brackets, which is the case Section "
             "18.4 has in mind."),
            ("Expecting a stair-step table to hold every key",
             "That is a direct-access table. A staircase stores one upper bound per range, "
             "which is why it suits keys that are not whole numbers or not evenly spaced, "
             "and why its endpoints need the care the chapter asks for."),
        ],
        "standard": (
            "Finish when you can look a key up in a stair-step table and count both searches.",
            "For a five-step table and a key, state the value and the comparisons a linear "
            "scan and a binary search make, and say which endpoint rule the table uses, "
            "by hand."
        ),
        "note": (
            "The lab counts comparisons, not time, and its binary search always runs until "
            "one step is left; a search that stops on an exact match could take fewer. A "
            "key past the last bound is reported as above the table, where the lesson's "
            "code returns the top fee instead. Which endpoint rule a business means is "
            "not something the lab or the code can know."
        ),
    },
    # ---------------------------------------------------------------- 06
    # McConnell Chapter 19, §§19.1-19.3, pp. 431-444. Opening quotation:
    # Key Points, p. 460 (14 words). True and false, pp. 431-433; simplifying
    # complicated expressions, pp. 433-435; forming them positively and
    # DeMorgan's theorems (Table 19-1, named, not reproduced), pp. 435-436;
    # parentheses, pp. 437-438; evaluation and short circuits, pp. 438-440;
    # number-line order, pp. 440-441; comparisons to 0, pp. 441-442; common
    # problems, pp. 442-443; compound statements, p. 443; null statements,
    # pp. 444-445.
    {
        "slug": "boolean-expressions",
        "title": "Boolean Expressions",
        "module": "Chapter 19 · General Control Issues",
        "one_line": "Two conditions mean the same only if they agree on every row of their truth table, and DeMorgan's theorems are the rule for negating one without changing what it means.",
        "summary": (
            "The first half of Chapter 19 is about the conditions that control every "
            "decision: true and false, positive forms, DeMorgan's theorems, parentheses "
            "and short-circuit evaluation. Decide by truth table whether two conditions "
            "agree on every row, and see the half-applied DeMorgan that disagrees on two."
        ),
        "key": [
            "test true and false, not 1 and 0",
            "name a complicated test",
            "state conditions positively",
            "!(a || b) is !a && !b",
            "negate each part and swap && and ||",
            "equivalent: the same on every row",
        ],
        "key_label": "The first half of the chapter in six lines",
        "concepts_intro": (
            "Sections 19.1 to 19.3 are a set of guidelines. Three ideas carry the lesson's "
            "lab."
        ),
        "concepts": [
            ("Truth table",
             "Every combination of true and false for a condition's variables, one row "
             "each, with the condition's value on each row. Two variables give four "
             "rows; two conditions are equivalent when their values agree on all of "
             "them."),
            ("DeMorgan's theorems",
             "The rules for moving a negation across an and or an or: not (a or b) is "
             "(not a) and (not b), and not (a and b) is (not a) or (not b). McConnell's "
             "recipe: negate each operand, switch the ands and ors, and negate the whole."),
            ("Short-circuit evaluation",
             "Evaluating only as much of a condition as decides it. In Java, `&&` stops at "
             "the first false operand and `||` at the first true one, so a test on the "
             "left can protect the expression on its right."),
        ],
        "read_title": "The chapter's argument first, then the truth table",
        "read_intro": (
            "The lesson goes through Sections 19.1 to 19.3, compares conditions row by "
            "row with the lab, and ends with one negated condition to rewrite."
        ),
        "body": [
            ("p", "<strong>Chapter 19, p. 460.</strong> &ldquo;Making boolean expressions "
                  "simple and readable contributes substantially to the quality of your "
                  "code.&rdquo; It is the first of the chapter's key points. Read "
                  "Sections 19.1 to 19.3, pp. 431&ndash;445, in your own copy first; "
                  "Nesting and Complexity reads the rest of the chapter."),
            ("p", "How should a condition be written? Section 19.1 (p. 431) starts from "
                  "the observation that every control structure except plain sequence "
                  "depends on one. Use `true` and `false` rather than 1 and 0, which a "
                  "reader cannot tell from a count. Compare boolean values implicitly, "
                  "writing `while (!done)` rather than comparing `done` with `false`. "
                  "Break a long test into intermediate boolean variables with good "
                  "names, or move it into a boolean function whose name says what the "
                  "test is for, which McConnell prefers to a comment because code is "
                  "read and kept up to date more reliably than comments are. And where "
                  "several variables combine, consider a decision table, the subject of "
                  "Table-Driven Methods."),
            ("p", "Form expressions positively. The section opens that guideline with a "
                  "line of Homer Simpson's built entirely of negatives, and makes the "
                  "point that most people struggle with more than one. Turn a negative "
                  "test into a positive one by swapping the `if` and `else` clauses, or "
                  "choose a variable name whose truth runs the other way. And use "
                  "DeMorgan's theorems to remove a negation from a compound test: negate "
                  "each operand, switch the ands and ors, and negate the whole "
                  "expression. Table 19-1 lists the eight forms for two operands; it is "
                  "worth reading in the book. A margin note adds that writing tests "
                  "positively can conflict with Chapter 15's advice to put the normal "
                  "case after the `if`, and leaves the choice to you."),
            ("p", "The rest of the section is about evaluation. Parenthesize to make the "
                  "meaning plain rather than relying on precedence; extra parentheses cost "
                  "nothing, and the section gives a counting trick for checking that they "
                  "balance. Know how your language evaluates: Java's `&&` and `||` short-"
                  "circuit, so `count > 0 && total / count > limit` never divides by "
                  "zero, while its `&` and `|` evaluate both sides; McConnell suggests "
                  "nested tests where a reader might not know the rule. Write numeric "
                  "comparisons in number-line order, smallest on the left; compare "
                  "numbers with 0 explicitly and boolean values implicitly; and in Java "
                  "use `a.equals(b)` where `a == b` would compare references. Section "
                  "19.2 (p. 443) asks for braces written in pairs and used around every "
                  "conditional body, and Section 19.3 (p. 444) for null statements made "
                  "obvious, or avoided by a loop with a body."),
            ("p", "Now a condition written two ways. In this routine, written for the "
                  "lesson, the loop's guard on line 4 and the test on line 7 ask the same "
                  "question, once negated as a group and once part by part:"),
            ("code", _lines(DRAIN)),
            ("p", "The lab's <em>truth</em> view takes two conditions, A and B, over "
                  "boolean variables and writes every row. It prints the "
                  "<strong>variables</strong>, the <strong>rows</strong>, the "
                  "<strong>rows where A is true</strong> and <strong>where B is "
                  "true</strong>, whether the two are <strong>equivalent</strong>, and "
                  "the <strong>first row that differs</strong>. The "
                  "<code>demorgan</code> preset compares line 4's `!(done || error)` with "
                  "line 7's `!done && !error`: 2 variables, 4 rows, each true on 1 row, "
                  "equivalent yes, no row differs. The <code>half-demorgan</code> preset "
                  "compares `!(done || error)` with `!done || !error`, which negates each "
                  "part and forgets to switch the operator. That one is true on 3 rows, "
                  "and the lab prints &ldquo;no, on 2 of 4 rows&rdquo;, the first being "
                  "done = T, error = F: the queue is empty, nothing failed, and the "
                  "half-applied version would still try to process the next item."),
            ("p", "Two more presets show DeMorgan used to simplify. The "
                  "<code>redundant</code> preset compares `(found && valid) || (found && "
                  "!valid)` with plain `found`: equivalent, true on 2 of 4 rows each, "
                  "because whatever `valid` is, one of the two halves holds whenever "
                  "`found` does. The <code>double-negative</code> preset compares "
                  "`!(!ready || !loaded)` with `ready && loaded`: equivalent, and the "
                  "positive form is the one Section 19.1 asks you to write."),
            ("h3", "Exercise"),
            ("code", _lines(OWNER_TEST)),
            ("p", "Rewrite the condition with no negated group, by DeMorgan's theorems, "
                  "and check your version by writing the four rows of `isAdmin` and "
                  "`isOwner` for both. Then type both conditions into the lab as A and B "
                  "to check."),
            ("p", "A condition can be simplified on its own; a routine full of them "
                  "nests. The next lesson, Nesting and Complexity, reads the rest of "
                  "Chapter 19 and closes the course with its count."),
        ],
        "lab": ("cckit", {
            "mode": "cond",
            "view": "truth",
            "preset": "demorgan",
            "presets": [
                {"id": "demorgan",
                 "label": "Line 4 against line 7 of drain",
                 "a": "!(done || error)", "b": "!done && !error",
                 "expect": {"cdTrueA": "1", "cdTrueB": "1", "cdEquivalent": "yes", "cdFirstDiff": "none"}},
                {"id": "half-demorgan",
                 "label": "Each part negated, the operator kept",
                 "a": "!(done || error)", "b": "!done || !error",
                 "expect": {"cdTrueB": "3", "cdEquivalent": "no, on 2 of 4 rows", "cdFirstDiff": "done = T, error = F"}},
                {"id": "redundant",
                 "label": "A redundant test",
                 "a": "(found && valid) || (found && !valid)", "b": "found",
                 "expect": {"cdEquivalent": "yes", "cdFirstDiff": "none"}},
                {"id": "double-negative",
                 "label": "A double negative",
                 "a": "!(!ready || !loaded)", "b": "ready && loaded",
                 "expect": {"cdEquivalent": "yes", "cdFirstDiff": "none"}},
            ],
            "panel_title": "Two conditions, row by row",
            "panel_intro": (
                "The lab writes every row of true and false for the variables of A and B, "
                "evaluates both on each, and reports where they differ. It parses the "
                "conditions itself and never runs them."
            ),
        }),
        "steps_title": "Testing two conditions for equivalence",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("List the variables",
             "Write every boolean variable in either condition. With n of them there are "
             "2 to the power n rows; two variables give four."),
            ("Write the rows",
             "Write every combination of true and false, true first, the first variable "
             "changing slowest."),
            ("Evaluate both on every row",
             "Work out each condition's value on each row, inner parentheses first, a "
             "negation before an and, an and before an or."),
            ("Compare",
             "If the two agree on every row, they are equivalent and either may replace "
             "the other; if not, the first row that differs is a case one of them gets "
             "wrong."),
            ("Do it on your own code",
             "Find one negated compound condition in your own code, rewrite it in a "
             "positive form by DeMorgan's theorems, and type the original and the "
             "rewrite into the lab as A and B to confirm they agree on every row."),
        ],
        "worked": {
            "title": "Three conditions on four rows",
            "intro": [
                "Let A be !(done || error), B be !done && !error and C be !done || !error. "
                "Evaluate each on the four rows of done and error.",
            ],
            "lines": [
                "done true, error true: A false, B false, C false",
                "done true, error false: A false, B false, C true",
                "done false, error true: A false, B false, C true",
                "done false, error false: A true, B true, C true",
            ],
            "after": [
                "A and B agree on every row: each is true only when both variables are "
                "false. C is also true when exactly one of them is, so it differs from A "
                "on two rows.",
            ],
        },
        "quiz_title": "Truth tables and DeMorgan",
        "quiz": [
            {"q": "Which condition is equivalent to `!(isAdmin || !isOwner)`?",
             "a": ["`!isAdmin || isOwner`",
                   "`!isAdmin && isOwner`",
                   "`!isAdmin && !isOwner`",
                   "`isAdmin && !isOwner`"],
             "c": 1,
             "why": "Negate each operand and switch the operator: `!isAdmin && isOwner`, "
                    "and the lab confirms equivalence on all 4 rows. `!isAdmin || isOwner` "
                    "kept the `||` and is wrong when both are true; `!isAdmin && !isOwner` "
                    "left the second operand un-negated and is wrong for a non-admin owner; "
                    "`isAdmin && !isOwner` is true on a row where the original is false."},
            {"q": "On which rows do `!(done || error)` and `!done || !error` disagree?",
             "a": ["Only done = F, error = F",
                   "Only done = T, error = T",
                   "On none: they are equivalent",
                   "done = T, error = F and done = F, error = T"],
             "c": 3,
             "why": "`!(done || error)` is true only when both are false; `!done || !error` "
                    "is true whenever at least one is false. They disagree on the two rows "
                    "where exactly one is true, and the lab prints &ldquo;no, on 2 of 4 "
                    "rows&rdquo;."},
            {"q": "`count` and `total` are `int`s. Which of these never divides by zero "
                  "when `count` is 0?",
             "a": ["`total / count > limit && count > 0`",
                   "`count > 0 & total / count > limit`",
                   "`count > 0 && total / count > limit`",
                   "`count != 0 | total / count > limit`"],
             "c": 2,
             "why": "`&&` evaluates its right side only when its left side is true, so the "
                    "division is skipped when `count` is 0. Putting the test second does "
                    "not help, because the division comes first; and Java's `&` and `|` "
                    "always evaluate both sides (p. 439)."},
            {"q": "How does Section 19.1 tell you to apply DeMorgan's theorems to an and "
                  "or an or and a pair of operands?",
             "a": ["Negate each operand and keep the operator",
                   "Negate each operand, switch the ands and ors, and negate the whole "
                   "expression",
                   "Switch the ands and ors and leave the operands alone",
                   "Negate the whole expression and leave the rest"],
             "c": 1,
             "why": "All three steps are needed (p. 436). Negating the operands alone is "
                    "the half-demorgan preset, which is wrong on 2 of 4 rows; the other two "
                    "change the meaning on at least two rows as well."},
        ],
        "mistakes": [
            ("Negating a condition by negating each part",
             "That is the half-demorgan preset: `!done || !error` in place of "
             "`!(done || error)`. It is true on 3 rows where the original is true on 1, "
             "and wrong on the 2 rows where exactly one variable is true. DeMorgan's "
             "theorems need the operator switched as well, `||` to `&&`, which is the "
             "difference between line 4 of drain and the half-applied version."),
            ("Treating parentheses as something only the compiler needs",
             "Section 19.1 asks for parentheses for the reader's sake: a reader should not "
             "have to remember precedence, especially one who moves between languages, "
             "and the extra characters cost nothing. Fully parenthesizing logical "
             "expressions is the habit it recommends."),
            ("Treating Java's & and && as interchangeable",
             "On boolean operands both compute the same value, but `&` always evaluates "
             "both sides and `&&` stops when the left side is false. A guard such as "
             "`count > 0` protects the expression after it only with `&&` (p. 439)."),
        ],
        "standard": (
            "Finish when you can test two conditions for equivalence by truth table.",
            "For two conditions over two variables, write the four rows and say whether "
            "the conditions are equivalent; and apply DeMorgan's theorems to "
            "!(a || b), by hand."
        ),
        "note": (
            "The lab treats each variable as free to be true or false. In a program two "
            "variables may be tied, so that some rows cannot happen, and two conditions "
            "that differ only on such rows behave the same there; the lab cannot know "
            "that. It does not evaluate calls or comparisons, short-circuit order or side "
            "effects, and it cannot judge which of two equivalent forms reads better, "
            "which is the chapter's real question."
        ),
    },
    # ---------------------------------------------------------------- 07
    # McConnell Chapter 19, §§19.4-19.6, pp. 445-460. Opening quotation:
    # Key Points, p. 460 (15 words). Taming deep nesting and its techniques,
    # pp. 445-454; structured programming, Dijkstra 1969, Böhm and Jacopini
    # 1966, pp. 454-456; control structures and complexity, McCabe 1976,
    # the decision-point count and its bands, pp. 456-458; "moving part of a
    # routine into another" does not reduce overall complexity, p. 458;
    # other measures, p. 459.
    # F14, p. 458: 1 + if, while, repeat, for, and, or + each case; 0-5
    # probably fine, 6-10 start to think about simplifying, 10+ break part out.
    # F15, p. 445: few people understand more than three levels of nested
    # ifs (Yourdon 1986a, after Chomsky and Weinberg); many recommend no more
    # than three or four (Myers 1976, Marca 1981, Ledgard and Tauer 1987a).
    {
        "slug": "nesting-and-complexity",
        "title": "Nesting and Complexity",
        "module": "Chapter 19 · General Control Issues",
        "one_line": "Counting a routine's decision points and its deepest nesting tells you where to look, and flattening it moves the decisions without removing them.",
        "summary": (
            "The second half of Chapter 19 takes deep nesting, the structured-programming "
            "idea that any control flow can be built from sequence, selection and "
            "iteration, and McCabe's count of decision points. Count a shipping-cost "
            "routine nested five deep, flatten it with guard clauses, and see what falls "
            "and what only moves."
        ),
        "key": [
            "few readers follow three nested ifs",
            "points: 1 + each if, for, while, case, &&, ||",
            "0–5 fine; 6–10 think; 10+ split",
            "a count says where to look",
            "moving code moves its decision points",
        ],
        "key_label": "The second half of the chapter in five lines",
        "concepts_intro": (
            "Sections 19.4 to 19.6 measure what earlier lessons described. The lesson uses "
            "three ideas, and gathers the course's counts into one."
        ),
        "concepts": [
            ("Nesting depth",
             "How many control structures a statement sits inside. The lab counts the "
             "braces around a statement below the routine's own, so a statement directly "
             "in the routine's body is at depth 0 and the body of three nested ifs is at "
             "depth 3."),
            ("Decision points",
             "McConnell's count, after McCabe: 1 for the straight path through a routine, "
             "plus 1 for each if, while, for, and and or, and 1 for each case. It "
             "measures how many paths the control flow has, not how good the routine is."),
            ("Structured programming",
             "The idea that a program should use only constructs with one entry and one "
             "exit, and the result, credited to Böhm and Jacopini, that sequence, "
             "selection and iteration are enough to build any control flow."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "The lesson goes through Sections 19.4 to 19.6, counts a routine before and "
            "after flattening it, and ends with one for you to count."
        ),
        "body": [
            ("p", "<strong>Chapter 19, p. 460.</strong> &ldquo;Deep nesting makes a "
                  "routine hard to understand. Fortunately, you can avoid it relatively "
                  "easily.&rdquo; It is the second of the chapter's key points. Read "
                  "Sections 19.4 to 19.6, pp. 445&ndash;460, in your own copy first."),
            ("p", "Open the routine you have maintained that you least like to open, and "
                  "you will probably find closing braces stacked down the right-hand side "
                  "and a statement somewhere in the middle that runs only when five "
                  "conditions hold. Section 19.4 (p. 445) calls excessive nesting one of "
                  "the chief culprits in confusing code, and reports the evidence for a "
                  "limit as others' findings: studies by Noam Chomsky and Gerald Weinberg, "
                  "as Yourdon reports them, suggest that few people can understand more "
                  "than three levels of nested `if`s, and many researchers, Myers, Marca, "
                  "and Ledgard and Tauer among them, recommend no more than three or four. "
                  "These are other people's observations, made before 2004; your own "
                  "code reviews can test them."),
            ("p", "The section's remedies are a list. Retest part of a condition instead "
                  "of nesting another `if`; use a block that can be broken out of; "
                  "convert a nested `if` to a chain of if-then-else tests or to a "
                  "`case` statement; factor deeply nested code into a routine of its own; "
                  "replace a case-by-case dispatch with objects and polymorphism; or "
                  "redesign the code. Its summary adds techniques from other chapters: a "
                  "status variable, exceptions, and the guard clauses of Unusual Control "
                  "Structures. Deep nesting, the section concludes, is a warning that the "
                  "code needs another look, and you should have a good reason if you "
                  "leave it."),
            ("p", "Section 19.5 (p. 454) steps back to structured programming. The book "
                  "traces the term to a paper Edsger Dijkstra presented in 1969, and notes "
                  "that it was soon applied to every activity in software, down to "
                  "&ldquo;structured goofing off&rdquo;. Its core is that a program should use only one-in, "
                  "one-out constructs, and its thesis, credited to Böhm and Jacopini in "
                  "1966, is that sequence, selection and iteration are enough to build "
                  "any control flow. McConnell's view is that `break`, `continue`, "
                  "`return` and exceptions deserve a critical eye for that reason. "
                  "Section 19.6 (p. 456) then argues that control structures are a large "
                  "part of a program's complexity, measured as the number of things a "
                  "reader must hold in mind at once, and presents Tom McCabe's 1976 "
                  "measure."),
            ("p", "The book's rule, Table 19-2 (p. 458): start with 1 for the straight "
                  "path through the routine; add 1 for each `if`, `while`, `repeat`, "
                  "`for`, `and` and `or`, &ldquo;or their equivalents&rdquo;; add 1 for each case of a "
                  "`case` statement. It reads the result in three bands: 0 to 5, the "
                  "routine is probably fine; 6 to 10, start to think about simplifying "
                  "it; 10 and more, break part of it into another routine. These are "
                  "McConnell's guidance, built on McCabe's measure, not a grade, and he "
                  "says so: the limit of 10 is a warning flag rather than a rule, and a "
                  "long `case` statement may be better left whole. He adds a point the "
                  "lesson's lab will show: moving part of a routine into another does "
                  "not reduce the program's overall complexity, it moves the decision "
                  "points, though it does reduce how much you must hold at one time."),
            ("p", "Now the count. The lab's <em>complexity</em> view applies the rule to "
                  "Java: 1, plus one for each `if`, `while`, `for`, `case`, `&&` and "
                  "`||`; `else`, `default` and the `?:` operator add nothing, the last by "
                  "the kit's choice. It prints the <strong>decision points</strong>, the "
                  "<strong>breakdown</strong> by keyword, the <strong>band</strong> "
                  "(putting 10 in 6&ndash;10, where the book's bands overlap), the "
                  "<strong>deepest nesting</strong> by the depth rule above, and the "
                  "<strong>first line at that depth</strong>. Here is the "
                  "<code>nested-shipping</code> preset, twenty-two lines written for the "
                  "lesson:"),
            ("code", {"lines": _lines(NESTED_SHIPPING), "marked": [14]}),
            ("p", "The lab counts 9 decision points, broken down as 1 + if 5 + for 1 + && "
                  "1 + || 1, in the band 6&ndash;10, and a deepest nesting of 5, first "
                  "reached on line 14, the `return -1.0;` inside the restricted-item "
                  "check. That return is an error sentinel, a technique Chapter 8 lists "
                  "with its costs. The count is a reason to look, and looking shows the "
                  "domestic rules buried four levels down. Here is the "
                  "<code>guard-clauses</code> preset, the same rules with the error cases "
                  "returned first and the international branch moved into a routine of "
                  "its own:"),
            ("code", _lines(GUARD_CLAUSES)),
            ("p", "The lab counts 6, as 1 + if 3 + && 1 + || 1, still in 6&ndash;10, and a "
                  "deepest nesting of 1, first on line 3. The nesting a reader holds at "
                  "once fell from 5 to 1. The decision points fell from 9 to 6 for a "
                  "different reason: the `for`, its `if` and its `||` moved into "
                  "`internationalCost`, where they are still to be read. That is the "
                  "book's own point on p. 458, and the lab shows it on the lesson's "
                  "routine: the program's decisions were moved, not removed. Whether 6 "
                  "is worth simplifying further is your judgement; the band says only "
                  "where McConnell would start to think about it."),
            ("h3", "Exercise"),
            ("code", _lines(DISCOUNT)),
            ("p", "Count the decision points of `discountPercent` by the rule, with their "
                  "breakdown by keyword, and the deepest nesting, by hand. Then paste the "
                  "routine into the lab to check."),
            ("p", "That ends the course, and the book's Part IV. The next course, Code "
                  "Improvements, begins with The Software-Quality Landscape, which asks "
                  "how much of the code these lessons produce a team's testing and "
                  "reviews can be expected to make right."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "preset": "nested-shipping",
            "presets": [
                {"id": "nested-shipping",
                 "label": "Shipping cost, nested five deep (the lesson's routine)",
                 "code": NESTED_SHIPPING,
                 "expect": {"coDecisions": "9", "coBreakdown": "1 + if 5 + for 1 + && 1 + || 1", "coBand": "6–10", "coDepth": "5", "coDeepest": "line 14"}},
                {"id": "guard-clauses",
                 "label": "The same rules as guard clauses",
                 "code": GUARD_CLAUSES,
                 "expect": {"coDecisions": "6", "coBreakdown": "1 + if 3 + && 1 + || 1", "coBand": "6–10", "coDepth": "1", "coDeepest": "line 3"}},
            ],
            "panel_title": "Decision points and nesting",
            "panel_intro": (
                "The lab counts decision points by the chapter's rule as applied to Java, "
                "and the depth of each statement by its braces. The bands are McConnell's "
                "guidance for where to look, not a grade."
            ),
        }),
        "steps_title": "Counting decision points and depth",
        "steps_intro": "Five steps, the last of which is yours.",
        "steps": [
            ("Start at one",
             "Every routine has one straight path through it, and the count starts with "
             "it."),
            ("Add the keywords",
             "Add one for each if, while, for and case, and one for each && and || in "
             "their conditions. An else, a default and a return add nothing."),
            ("Find the deepest statement",
             "For each statement, count the braces it sits inside below the routine's "
             "own. The largest is the routine's deepest nesting."),
            ("Read the count, then the code",
             "Place the count in the chapter's bands, then go to the deepest statement and "
             "the conditions over it, and ask which technique of Section 19.4 would bring "
             "it up."),
            ("Do it on your own code",
             "Paste your most-nested routine into the lab, note its decision points, "
             "breakdown and deepest nesting, and write one sentence saying which of "
             "Section 19.4's techniques you would try first and why."),
        ],
        "worked": {
            "title": "Counting the nested shipping routine",
            "intro": [
                "Count nested-shipping by the rule, keyword by keyword.",
            ],
            "lines": [
                "start: 1",
                "if on lines 3, 4, 5, 6 and 13: 5",
                "for on line 12: 1",
                "&& on line 6 and || on line 13: 2",
                "total: 1 + 5 + 1 + 2 gives 9",
                "deepest: line 14, inside 5 levels",
            ],
            "after": [
                "Nine decision points, in the band 6–10, and a statement five levels deep. "
                "Neither figure says the routine is wrong; both say where to read it first.",
            ],
        },
        "quiz_title": "Decision points, depth and what moves",
        "quiz": [
            {"q": "Counting 1 plus one for each `if`, `while`, `for`, `case`, `&&` and "
                  "`||`, and depth with a statement directly in the routine's body at 0, "
                  "how many decision points does `discountPercent` have, and how deep is "
                  "its deepest statement?",
             "a": ["6 (if 3 + for 1 + && 1 + || 1), depth 2",
                   "7 (1 + if 3 + for 1 + && 1 + || 1), depth 2",
                   "5 (1 + if 3 + for 1), depth 2",
                   "7 (1 + if 3 + for 1 + && 1 + || 1), depth 3"],
             "c": 1,
             "why": "7 decision points: 1 + if 3 + for 1 + && 1 + || 1, with the `||` on "
                    "line 6 and the `&&` on line 10; depth 2, for `pct = pct + "
                    "k.percent();` on line 11, inside the `for` and its `if`. Leaving out "
                    "the starting 1 gives 6, leaving out the operators 5, and counting the "
                    "routine's own braces gives depth 3."},
            {"q": "Why do the decision points fall from 9 in <code>nested-shipping</code> to 6 in "
                  "<code>guard-clauses</code>?",
             "a": ["Guard clauses count less than nested ifs",
                   "The kit does not count a condition that returns",
                   "Flattening removed three conditions from the program",
                   "A `for`, an `if` and an `||` moved into `internationalCost`, where "
                   "they still are"],
             "c": 3,
             "why": "The international branch, with its loop, its test and its `||`, moved "
                    "into `internationalCost`; the program still makes those decisions. "
                    "Every `if` counts one whether or not it returns, and the guard "
                    "clauses' own `if`s are all counted: 1 + if 3 + && 1 + || 1. Moving "
                    "part of a routine into another moves its decision points (p. 458)."},
            {"q": "By the chapter's bands, after McCabe (p. 458), what does McConnell "
                  "suggest for a routine with 8 decision points?",
             "a": ["Start to think about ways to simplify it",
                   "It is probably fine as it is",
                   "Break part of it into a second routine",
                   "Rewrite it before it is used"],
             "c": 0,
             "why": "8 falls in 6 to 10, where the book says to start to think about "
                    "simplifying; 0 to 5 is probably fine, and 10 and more is where it "
                    "suggests breaking part out (F14, Table 19-2). The book calls the limit "
                    "a warning flag, not a rule, and no band says to rewrite."},
            {"q": "Section 19.5 reports Böhm and Jacopini's thesis that any control flow "
                  "can be built from which three constructs?",
             "a": ["Sequence, selection and iteration",
                   "Sequence, goto and recursion",
                   "If, case and return",
                   "Selection, iteration and exceptions"],
             "c": 0,
             "why": "The core thesis of structured programming, credited to Böhm and "
                    "Jacopini 1966, is that sequence, selection and iteration suffice "
                    "(p. 456). `goto` is what structured programming set out to replace."},
        ],
        "mistakes": [
            ("Thinking that flattening the code reduces its complexity",
             "It reduces the nesting a reader holds at once: on the lesson's routine, from 5 "
             "levels to 1. The decision points fall from 9 to 6 only because three of "
             "them, a `for`, an `if` and an `||`, moved into `internationalCost`, where "
             "they are still to be read. McConnell says so himself: moving part of a "
             "routine into another does not reduce the program's overall complexity, it "
             "reduces what you must juggle at one time (p. 458)."),
            ("Thinking a count of 11 means the routine is bad",
             "The bands are the book's guidance for where to look, after McCabe, and the "
             "book calls 10 a warning flag, not an absolute limit; it names a long case "
             "statement as something it may be foolish to break up. A count measures the "
             "paths through a routine. Whether they are too many is a judgement made by "
             "reading it."),
            ("Thinking guard clauses are the only cure for deep nesting",
             "Section 19.4 lists retesting part of a condition, a break block, converting "
             "to if-then-else or case, factoring code into a routine, polymorphism and "
             "redesign, and points elsewhere to status variables, exceptions and guard "
             "clauses. Which fits depends on why the code is nested."),
        ],
        "standard": (
            "Finish when you can count a routine's decision points and nesting by hand.",
            "For a routine of 15 to 22 lines, state the decision points with their "
            "breakdown by keyword and the deepest nesting, by the rule as the lesson "
            "states it, by hand."
        ),
        "note": (
            "The lab reads keywords and braces; it never runs the code. It does not count "
            "`?:`, which the book's rule might count as an equivalent of `if`, and it cannot "
            "tell whether the routine a branch moved into is easier to read than the "
            "branch was. The bands are McConnell's guidance after McCabe's measure, drawn "
            "from other people's projects; your own defect records are the test of "
            "whether they fit your code."
        ),
    },
]
