"""Code Improvements, lessons 5-8 -- Chapters 23-26 of Code Complete, 2nd ed.

Debugging, refactoring, and code tuning in its strategies and its techniques.
Pages are the second edition's printed pages. Every quotation is copied from
the book character for character, with its page in the comment beside the
lesson; every figure attributed to the book carries its register id from
docs/code-complete/PLAN.md section S.2. The code is written for these
lessons; none of it is the book's.
"""

from .part_a import OVERTIME, _lines

# ---------------------------------------------------------------- snippets
# PLAN D.4 `printStatement` (presets.py `extract`).
PRINT_STATEMENT = """void printStatement(Account account) {
    double balance = account.openingBalance();
    double fees = 0.0;
    for (Transaction t : account.transactions()) {
        balance = balance + t.amount();
        if (t.amount() < 0 && balance < 0) {
            fees = fees + 25.0;
        }
    }
    balance = balance - fees;
    System.out.println("Fees: " + fees);
    System.out.println("Closing balance: " + balance);
}"""

# PLAN D.4 exercise `printInvoice` (presets.py `print-invoice`): lines 2-5 in
# inv, out subtotal; lines 7-9 in subtotal and tax, out none.
PRINT_INVOICE = """void printInvoice(Invoice inv) {
    double subtotal = 0.0;
    for (Line line : inv.lines()) {
        subtotal = subtotal + line.amount();
    }
    double tax = subtotal * inv.taxRate();
    System.out.println("Subtotal: " + subtotal);
    System.out.println("Tax: " + tax);
    System.out.println("Total: " + (subtotal + tax));
}"""

# PLAN C 5.8 exercise: a loop with an invariant call, n = 1,000.
GROSS_LOOP = """for (int i = 0; i < n; i++) {
    double rate = config.taxRate();
    gross[i] = net[i] * (1 + rate);
}"""


LESSONS = [
    # ---------------------------------------------------------------- 05
    # McConnell Chapter 23, pp. 535-562. Quote: p. 562 (Key Points), 30 words.
    # Definition and role, pp. 535-536; Gould 1975, p. 537 (F20); defects as
    # opportunities, pp. 537-538; the Devil's Guide, p. 539; the scientific
    # method and its debugging form, pp. 540-541; stabilising, p. 542; tips,
    # pp. 544-548 (binary search, p. 546; code changed recently and an old
    # version, p. 547); brute force and a time limit, pp. 548-549; fixing,
    # pp. 550-554; psychological set and distance, pp. 554-556; tools, p. 556.
    {
        "slug": "debugging-as-science",
        "title": "Debugging as Science",
        "module": "Chapter 23 · Debugging",
        "one_line": "Find a defect by experiment: state a hypothesis, run the test that decides it, and halve the suspects each time.",
        "summary": (
            "Chapter 23 sets debugging out as the scientific method: stabilise the error, "
            "form a hypothesis, design the experiment that proves or disproves it, and only "
            "then fix, test the fix and look for similar defects. State a hypothesis about a "
            "failure, name the test that decides it, and count the steps a binary search "
            "takes among a thousand suspect changes."
        ),
        "key": [
            "stabilise, then hypothesise, then test",
            "each test should halve the suspects",
            "1000 suspects: 10 halvings",
            "understand the problem before the fix",
            "one change at a time",
        ],
        "key_label": "The method in five lines",
        "concepts_intro": (
            "The chapter's method rests on three ideas, the last of which the lab counts."
        ),
        "concepts": [
            ("Debugging",
             "Finding the root cause of an error that testing has detected, and correcting "
             "it. The chapter keeps it apart from testing, which only detects, and calls it a "
             "last resort for quality rather than a way to build it."),
            ("A hypothesis and its experiment",
             "A guess about the defect's cause that accounts for the data, and a test whose "
             "result would prove or disprove it. A disproved hypothesis still narrows the "
             "search."),
            ("Binary search for a defect",
             "Removing or skipping about half of the suspects, finding which half holds the "
             "defect, and repeating. Each test halves what is left, so a thousand suspects "
             "take about ten tests."),
        ],
        "read_title": "The chapter's method, then the arithmetic of halving",
        "read_intro": (
            "The lesson goes through the five sections in order and then counts the tests "
            "halving takes."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 23, p. 562.</strong> &ldquo;A systematic "
                  "approach to finding and fixing errors is critical to success. Focus your "
                  "debugging so that each test moves you a step forward. Use the Scientific "
                  "Method of Debugging.&rdquo; Read Chapter 23, pages 535 to 562, in your own "
                  "copy first."),
            # F20, p. 537.
            ("p", "A test that passed last month fails today, and a thousand changes have gone "
                  "in since. You could read the code until the defect shows itself. Chapter 23 "
                  "calls that guessing, and opens (p. 535) by saying what is at stake. "
                  "Debugging is identifying the root cause of an error and correcting it, and "
                  "on some projects it takes a large share of the time. Programmers differ "
                  "widely at it. The book reports a study by John Gould (1975) of experienced "
                  "programmers debugging a program with known defects: the three fastest took "
                  "5.0 minutes on average against the slowest three's 14.1, missed 0.7 defects "
                  "against 1.7, and made 3.0 new defects while correcting against 7.7. That is "
                  "one study's small sample, from 1975, and it is the book's evidence that "
                  "debugging is a skill rather than a talent."),
            ("p", "The chapter's foil is &ldquo;The Devil's Guide to Debugging&rdquo; (p. 539), "
                  "McConnell's description of the circle of hell where programmers find "
                  "defects by scattering print statements, change things until something "
                  "seems to work, keep no record of what they changed, and fix a wrong result "
                  "by special-casing the input that showed it. Against it, Section 23.2 "
                  "(p. 540) sets the scientific method: gather data through repeatable "
                  "experiments, form a hypothesis that accounts for it, design an experiment "
                  "to prove or disprove the hypothesis, and repeat. For a defect that becomes "
                  "five steps. Stabilise the error, so that it happens reliably. Locate it, by "
                  "gathering data, forming a hypothesis, choosing the test or the reading that "
                  "would decide it, and deciding it. Fix it. Test the fix. Look for similar "
                  "errors."),
            ("p", "Most of Section 23.2 is tips for the locating. Use all the data, and when a "
                  "fact does not fit the hypothesis, ask why rather than drop the fact. Refine "
                  "the test case until changing any part of it changes the failure. Reproduce "
                  "the error several ways, to triangulate it. A test that disproves a "
                  "hypothesis still tells you where the defect is not. And narrow the "
                  "suspicious region (p. 546): remove about half the code, see which half the "
                  "defect is in, and halve that, a binary search. Two more tips (p. 547) point "
                  "at history: a new error is usually in code that changed recently, so run "
                  "an old version, and if it works compare the two. Talk the problem through "
                  "with someone, take a break, and when quick guessing has run past a time "
                  "limit you set in advance, switch to a brute-force method that is sure to "
                  "work, such as a full review or rewriting the code."),
            ("p", "Section 23.3 (p. 550) is fixing, which the chapter calls the easy part and "
                  "therefore the error-prone one. Understand the problem, and the program, "
                  "before you fix it; confirm the diagnosis; save the original code; fix the "
                  "problem rather than the symptom, because a special case that makes one "
                  "wrong answer right leaves the cause in place; change one thing at a time; "
                  "add a unit test that exposes the defect; and look for others like it. "
                  "Section 23.4 (p. 554) is the psychology: you see what you expect to see, "
                  "and two names that look alike are a defect waiting to happen. Section 23.5 "
                  "(p. 556) surveys the tools, from file comparators and compiler warnings to "
                  "debuggers."),
            ("def", ("Binary search among suspects",
                     "Order the suspects, test the one in the middle, and keep the half that "
                     "still holds the defect. With n suspects the number of tests is at most "
                     "the smallest whole number k for which 2 to the power k is at least n.")),
            ("p", "The chapter halves regions of code. The lab halves a history of changes, "
                  "which is where the advice to check recent code and run an old version leads: "
                  "if the build from a thousand changes ago passes and today's fails, test the "
                  "build in the middle. The <code>commit-637</code> preset puts the defect in "
                  "change 637 of 1,000. The lab's table lists the intervals as each test "
                  "decides between halves: 1 to 1,000, 501 to 1,000, 501 to 750, 626 to 750, "
                  "626 to 688, 626 to 657, 626 to 641, 634 to 641, 634 to 637, 636 to 637. It "
                  "prints Steps to find it 10 and Most steps any position takes 10."),
            ("p", "The <code>commit-63</code> preset puts the defect at change 63: Steps to "
                  "find it 9, since some positions are settled one test early, and Most steps "
                  "any position takes still 10. The <code>sixty-four</code> preset has 64 "
                  "suspects with the defect in the first: 6 steps either way, because 64 is "
                  "exactly two to the sixth. On the lesson's illustration, ten tests settle a "
                  "thousand changes, where reading them one by one would take up to a thousand."),
            ("p", "Halving works only on the chapter's first step. Each test must decide "
                  "cleanly between halves, so the failure has to be stable, and the defect has "
                  "to lie in one place on the line. An intermittent failure makes a passing "
                  "test mean nothing, and that is why stabilising comes first: the count of "
                  "ten is what a stabilised error costs, not what any error does."),
            ("h3", "Exercise"),
            ("code", _lines(OVERTIME)),
            ("p", "This is <code>overtimePay</code> from “Structured Basis Testing”. Called with "
                  "an array of four employees, none of them null, and <code>count</code> 5, it "
                  "throws <code>ArrayIndexOutOfBoundsException</code>. State a hypothesis that "
                  "accounts for the failure, the test or pair of tests that would decide it, "
                  "and the line where the exception is thrown with the value of "
                  "<code>i</code> there. Then say whether the five basis tests of that lesson "
                  "would have found it."),
            ("p", "Fixing a defect changes code that works elsewhere. The next lesson, "
                  "“Refactoring Safely”, is about changing working code on purpose without "
                  "breaking it."),
        ],
        "lab": ("cckit", {
            "mode": "search",
            "view": "bisect",
            "preset": "commit-637",
            "presets": [
                {"id": "commit-637",
                 "label": "1,000 changes, the defect in change 637",
                 "n": 1000, "k": 637,
                 "expect": {"seSteps": "10", "seWorst": "10"}},
                {"id": "commit-63",
                 "label": "1,000 changes, the defect in change 63",
                 "n": 1000, "k": 63,
                 "expect": {"seSteps": "9", "seWorst": "10"}},
                {"id": "sixty-four",
                 "label": "64 suspects, the defect in the first",
                 "n": 64, "k": 1,
                 "expect": {"seSteps": "6", "seWorst": "6"}},
            ],
            "panel_title": "Halving the suspects",
            "panel_intro": (
                "n suspects are numbered 1 to n, and the defect is in suspect k. Each test "
                "decides which half of the current interval holds it, and the table lists "
                "every interval. It assumes each test decides cleanly."
            ),
        }),
        "steps_title": "Finding a defect by experiment",
        "steps_intro": "Four steps from the chapter's method, and one from your own history.",
        "steps": [
            ("Stabilise the error",
             "Find an input that makes the failure happen every time, and simplify it until "
             "changing any part of it changes the failure."),
            ("State a hypothesis",
             "Write one sentence saying what causes the failure, and check that it accounts for "
             "every fact you have, including the cases that work."),
            ("Choose the test that decides it",
             "Pick the test whose result would prove or disprove the hypothesis; when the "
             "suspects are many, pick one that removes half of them."),
            ("Fix the cause, then look for its relatives",
             "Change one thing, rerun the deciding tests, add a test that exposes the defect, "
             "and search for the same mistake elsewhere."),
            ("Count your own last bisection",
             "Take the last time you searched for a defect by halving, among commits, inputs or "
             "lines of code. Note how many steps it took, and set that against the lab's count "
             "for the same number of suspects."),
        ],
        "worked": {
            "title": "A thousand changes in ten tests",
            "intro": [
                "Take the <code>commit-637</code> preset: the build from 1,000 changes ago "
                "passes, today's fails, and the defect came in with change 637.",
            ],
            "lines": [
                "after 9 tests:  at most 1000 / 512, about 2 left",
                "after 10 tests:  at most 1000 / 1024, under 1",
                "2 to the power 9 is 512, under 1000",
                "2 to the power 10 is 1024, at least 1000",
                "most tests any position needs:  10",
            ],
            "after": [
                "Ten halvings are enough for any of the thousand positions; change 637 takes all "
                "ten, and change 63, the <code>commit-63</code> preset, takes nine.",
            ],
        },
        "quiz_title": "Hypotheses and halving",
        "quiz": [
            {"q": "<code>overtimePay</code> is called with four employees, none null, and "
                  "<code>count</code> 5, and throws <code>ArrayIndexOutOfBoundsException</code>. "
                  "Which line throws it, and with what value of <code>i</code>?",
             "a": ["Line 4, with `i == 4`", "Line 5, with `i == 4`",
                   "Line 4, with `i == 5`", "Line 9, with `i == 3`"],
             "c": 0,
             "why": "Hypothesis: the loop reads past the end of the array, because nothing ties "
                    "<code>count</code> to <code>staff.length</code>. The test that decides it: "
                    "call with four non-null employees and <code>count</code> 4, which passes, "
                    "and with <code>count</code> 5, which fails. The line is 4: with "
                    "<code>i == 4</code>, <code>i &lt; count</code> is true, so Java evaluates "
                    "<code>staff[4]</code> in the condition and throws before line 5 is "
                    "reached. The fix is <code>i &lt; count &amp;&amp; i &lt; staff.length</code>, "
                    "or dropping <code>count</code>. The five basis tests of Structured Basis "
                    "Testing never pass a <code>count</code> larger than the array, which is "
                    "Boundaries and Bad Data's point."},
            {"q": "A binary search among 1,000 suspect changes: what is the most tests any "
                  "position can take?",
             "a": ["10", "9", "500", "32"],
             "c": 0,
             "why": "Two to the ninth is 512, less than 1,000, and two to the tenth is 1,024, "
                    "at least 1,000, so ten halvings always suffice and some positions need all "
                    "ten. Nine is what change 63 happens to take; 500 is the average for "
                    "checking one change at a time; 32 is about the square root of 1,000."},
            # F20, p. 537.
            {"q": "In the study the book reports from Gould (1975), how did the three fastest "
                  "debuggers compare with the three slowest?",
             "a": ["5.0 minutes against 14.1, and 3.0 new defects made correcting against 7.7",
                   "5.0 minutes against 14.1, but 7.7 new defects made correcting against 3.0",
                   "14.1 minutes against 5.0, and 1.7 defects missed against 0.7",
                   "About the same time, and 0.7 defects missed against 1.7"],
             "c": 0,
             "why": "Page 537: the fastest three averaged 5.0 minutes, missed 0.7 defects and "
                    "made 3.0 new ones while correcting; the slowest three 14.1, 1.7 and 7.7. "
                    "The fastest were also the most accurate, which the book takes as more "
                    "evidence that quality and speed go together. It is one study's figures, "
                    "from 1975."},
            {"q": "Which is the first step of the chapter's method for finding a defect?",
             "a": ["Stabilise the error, so that it occurs reliably",
                   "Form a hypothesis about the defect", "Fix the most likely line",
                   "Look for similar errors"],
             "c": 0,
             "why": "Page 541: stabilise the error, locate its source, fix it, test the fix, "
                    "look for similar errors. The hypothesis belongs to locating, which comes "
                    "second, because a failure that does not happen reliably cannot decide a "
                    "hypothesis."},
        ],
        "mistakes": [
            ("Thinking debugging is reading the code until the defect shows itself",
             "Reading feels like progress, and a small defect sometimes does show itself. The "
             "chapter's method is experiment instead: a hypothesis, a test that would prove or "
             "disprove it, and another test when it is disproved, each chosen to narrow the "
             "search. On the lesson's illustration, ten tests, each halving the suspects, "
             "settle a thousand changes, where reading them would take up to a thousand "
             "looks."),
            ("Fixing the symptom",
             "When one input gives a wrong answer, a special case for that input makes the "
             "answer right and leaves the cause in place. The chapter calls such fixes "
             "unmaintainable: the cause produces another wrong answer tomorrow, and the "
             "special cases pile up. Understand the problem first, then change the code that "
             "causes it."),
            ("Changing two things at once",
             "Two changes made together can each look like the fix, or one can introduce a new "
             "defect that looks like the old one. The chapter's advice is one change at a time, "
             "with the deciding tests rerun after each."),
        ],
        "standard": (
            "Finish when you can state a hypothesis, the test that decides it, and the count of "
            "a binary search.",
            "For a failing input and a routine, state the hypothesis, the one test that decides "
            "it and the line; for 1,000 suspect commits and the defect at a given one, list the "
            "halving intervals and count the steps."
        ),
        "note": (
            "The lab counts halvings among numbered suspects, assuming each test decides "
            "cleanly which half holds the defect. Real bisection can fail that assumption: an "
            "intermittent failure, a defect that needs two changes together, a build that "
            "does not compile in the middle. Applying the chapter's binary search to a history "
            "of changes is the lesson's step; the chapter halves regions of code, and points "
            "to recent changes and old versions separately."
        ),
    },
    # ---------------------------------------------------------------- 06
    # McConnell Chapter 24, pp. 563-585. Quote: p. 585 (Key Points), 24 words.
    # Myth and reality of evolution, pp. 563-564; kinds of evolution and the
    # Cardinal Rule, pp. 564-565; Fowler's definition and Constantine's
    # factoring, p. 565; reasons to refactor, pp. 565-570; reasons not to,
    # p. 571; specific refactorings, pp. 571-579 (extract routine, p. 573);
    # refactoring safely, pp. 579-581 (F21, pp. 580-581); bad times, p. 582;
    # strategies, pp. 582-584.
    {
        "slug": "refactoring-safely",
        "title": "Refactoring Safely",
        "module": "Chapter 24 · Refactoring",
        "one_line": "Before you pull a block out into its own routine, count what it reads from before it and what it leaves for after it.",
        "summary": (
            "Chapter 24 argues that code changes throughout its life and that each change "
            "should improve it, and lists the warning signs, the refactorings and the "
            "precautions that make that safe. Compute the inputs and outputs of a block "
            "before extracting it into a routine, and decide whether it extracts cleanly."
        ),
        "key": [
            "change should improve internal quality",
            "refactor: same behaviour, better structure",
            "in: read in the block, set before it",
            "out: set in the block, read after it",
            "two outs: a class or two routines first",
            "small changes: review them too",
        ],
        "key_label": "Extracting a routine",
        "concepts_intro": (
            "Three ideas from the chapter: what refactoring is, what makes it safe, and the "
            "two lists a block must be measured by before it becomes a routine."
        ),
        "concepts": [
            ("Refactoring",
             "In Martin Fowler's definition, which the chapter adopts, a change to a program's "
             "internal structure that makes it easier to understand and cheaper to modify "
             "without changing what it observably does."),
            ("The Cardinal Rule of Software Evolution",
             "McConnell's name for the rule that a program's internal quality should improve "
             "as it is changed. A fix made with duct tape and superstition makes it worse."),
            ("A block's In and Out",
             "Before extracting a block into a routine, the variables it reads that were set "
             "before it become the routine's parameters, and the variables it sets that are "
             "read after it become its results."),
        ],
        "read_title": "The chapter's argument, then a block measured before it moves",
        "read_intro": (
            "The lesson reads the five sections in order and then measures one refactoring, "
            "Extract Routine, before it is made."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 24, p. 585.</strong> &ldquo;Software can "
                  "either improve or degrade as it’s changed. The Cardinal Rule of Software "
                  "Evolution is that internal quality should improve with code "
                  "evolution.&rdquo; Read Chapter 24, pages 563 to 585, in your own copy "
                  "first."),
            ("p", "You have a routine that totals an account's transactions, charges a fee for "
                  "each overdraft and prints the result, and you would like to pull the loop "
                  "out into a routine of its own. Chapter 24 starts further back (p. 563), "
                  "with a myth: that a well-run project writes its code once, tests it and "
                  "forgets it until maintenance. The reality, McConnell says, is that code "
                  "changes a great deal while it is first being written, because requirements "
                  "change during development and every requirement change reaches the code. "
                  "Section 24.1 (p. 564) draws the distinction that matters: whether a "
                  "program's quality improves or degrades as it changes. Hence the Cardinal "
                  "Rule."),
            ("p", "Section 24.2 (p. 565) names the tool. Refactoring, in Martin Fowler's "
                  "definition (1999), is a change to a program's internal structure that makes "
                  "it easier to understand and cheaper to modify without changing its "
                  "observable behaviour. The word grew, the chapter notes, out of Larry "
                  "Constantine's &ldquo;factoring&rdquo; in structured programming, the "
                  "decomposition of a program into its parts. The section then lists warning "
                  "signs, which Fowler calls smells: duplicated code, a routine that is too "
                  "long, a parameter list that is too long, and many more, which the "
                  "chapter gathers into a checklist worth reading in the book. It ends on "
                  "reasons not to refactor, and on the word's dilution: a change that fixes a "
                  "defect or adds a feature is not a refactoring, however loosely people use "
                  "the term."),
            ("p", "Section 24.3 (p. 571) is a catalogue, summarised largely from Fowler, at "
                  "five levels: data (replace a magic number with a named constant, rename a "
                  "variable), statements (return as soon as you know the answer), routines "
                  "(extract a routine, move a routine's code inline, add or remove a "
                  "parameter), classes and their interfaces, and whole systems. Extract "
                  "Routine, the one this lesson measures, is the routine-level refactoring "
                  "that removes inline code from one routine and turns it into its own."),
            # F21, pp. 580-581.
            ("p", "Section 24.4 (p. 579) is the precautions: save the code you start with, keep "
                  "each refactoring small, do them one at a time, keep a list of the steps and "
                  "a &ldquo;parking lot&rdquo; for changes that can wait, make checkpoints, "
                  "use the compiler's warnings, retest, add tests, and review. The evidence the "
                  "chapter gives for reviewing even small changes is other people's. "
                  "Programmers' first attempt at a change is wrong more than half the time "
                  "(Yourdon 1986). The chance of a bad change rises from one line changed to "
                  "five and then falls, because small changes are treated casually (Weinberg "
                  "1983). And one organisation that began reviewing one-line changes saw their "
                  "error rate fall from 55 percent to 2 (Freedman and Weinberg 1982). Some "
                  "refactorings are riskier than others: a named constant is nearly risk-free, "
                  "while a change to a routine's interface or to a boolean test is not."),
            ("p", "The chapter warns against two abuses (p. 582): calling it refactoring while "
                  "tweaking broken code until it works, which McConnell calls hacking, and "
                  "refactoring code that needs rewriting. Section 24.5 (p. 582) suggests when: "
                  "when you add a routine or a class, when you fix a defect, in the modules "
                  "everyone is afraid of and the ones with the highest complexity, and in a "
                  "maintenance setting, in the parts you touch, leaving each better than you "
                  "found it."),
            ("def", ("In and Out of a block",
                     "In: the variables the block reads whose values were set before it. They "
                     "become the extracted routine's parameters. Out: the variables the block "
                     "sets that are read after it. A Java method returns one value, so a "
                     "block with one Out extracts directly, and one with two needs another "
                     "step first.")),
            ("code", _lines(PRINT_STATEMENT)),
            ("p", "The lab reads <code>printStatement</code> and a range of its lines. The "
                  "<code>print-lines</code> preset takes lines 11 and 12, the two print "
                  "statements: In is fees and balance, Out is none, and Parameters the routine "
                  "needs is 2. They extract as <code>printTotals(fees, balance)</code>, with "
                  "nothing to return. The <code>fee-loop</code> preset takes lines 4 to 9, the "
                  "loop: In is account, balance and fees, 3 parameters, and Out is balance and "
                  "fees, both read on lines 10 to 12. Two results."),
            ("p", "The <code>from-the-top</code> preset takes lines 2 to 10, everything before "
                  "the printing: In is only account, 1 parameter, because the block sets "
                  "balance and fees itself, but Out is still balance and fees. The lab's last "
                  "tile, Read but set nowhere, lists any name the block reads that the listing "
                  "never sets, such as a field or a constant the new routine would have to "
                  "reach some other way; here it is none. On the lesson's illustration the "
                  "count says what the refactoring will cost before you start: one clean "
                  "extraction, and two that need a small class holding both totals, or two "
                  "routines, one per result."),
            ("h3", "Exercise"),
            ("code", _lines(PRINT_INVOICE)),
            ("p", "Find two blocks of <code>printInvoice</code> that extract cleanly into "
                  "routines of their own. For each, give its lines, its In and its Out, and "
                  "the call that would replace it. Then paste the routine into the lab and set "
                  "the From and To lines to check."),
            ("p", "Refactoring improves structure and leaves behaviour alone. The next lesson, "
                  "“Code-Tuning Strategies”, is about the opposite trade: changing code to run "
                  "faster, and why that should come last."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "extract",
            "code": PRINT_STATEMENT,
            "preset": "print-lines",
            "presets": [
                {"id": "print-lines",
                 "label": "Lines 11 to 12: the two print statements",
                 "from": 11, "to": 12,
                 "expect": {"coIn": "fees, balance", "coOut": "none", "coParams": "2",
                            "coOutside": "none"}},
                {"id": "fee-loop",
                 "label": "Lines 4 to 9: the loop over the transactions",
                 "from": 4, "to": 9,
                 "expect": {"coIn": "account, balance, fees", "coOut": "balance, fees",
                            "coParams": "3"}},
                {"id": "from-the-top",
                 "label": "Lines 2 to 10: everything before the printing",
                 "from": 2, "to": 10,
                 "expect": {"coIn": "account", "coOut": "balance, fees", "coParams": "1"}},
            ],
            "panel_title": "What a block reads and leaves",
            "panel_intro": (
                "Choose a range of lines. In lists what the block reads that was set before "
                "it; Out lists what it sets that is read after it. Paste a routine of your own "
                "and choose a block to see its interface before you extract it."
            ),
        }),
        "steps_title": "Measuring a block before extracting it",
        "steps_intro": "Four steps before the refactoring, and one on your own code.",
        "steps": [
            ("Mark the block",
             "Choose the lines to extract, and save the code as it is, so that you can get "
             "back to it."),
            ("List what it reads from before",
             "For each variable the block reads, find where it was last set. Those set before "
             "the block are its In, the new routine's parameters."),
            ("List what it leaves for after",
             "For each variable the block sets, look for a read after the block. Those read "
             "later are its Out, the routine's results."),
            ("Decide on the shape",
             "No Out or one Out: extract the routine, with the Out as its return value. Two or "
             "more: first make a small class that holds them, or split the block into one "
             "routine per result."),
            ("Measure a block of your own",
             "Paste a routine you would like to break up into the lab with the block you would "
             "extract, note its In and Out before you change anything, and write the new "
             "routine's signature from them."),
        ],
        "worked": {
            "title": "Two print statements",
            "intro": [
                "Take the <code>print-lines</code> preset: lines 11 and 12 of "
                "<code>printStatement</code>.",
            ],
            "lines": [
                "line 11 reads:  fees",
                "line 12 reads:  balance",
                "both last set before line 11:  in is fees, balance",
                "set in the block:  nothing",
                "out:  none",
                "call:  printTotals(fees, balance)",
            ],
            "after": [
                "Lines 11 and 12 read <code>fees</code> and <code>balance</code> and set "
                "nothing used later, so they become <code>printTotals(fees, balance)</code> "
                "with no return value.",
            ],
        },
        "quiz_title": "Refactoring and its evidence",
        "quiz": [
            {"q": "In <code>printInvoice</code>, what are the In and Out of lines 2 to 5, and "
                  "of lines 7 to 9?",
             "a": ["Lines 2–5: in inv, out subtotal. Lines 7–9: in subtotal and tax, out none",
                   "Lines 2–5: in inv and subtotal, out subtotal. Lines 7–9: in tax, out none",
                   "Lines 2–5: in inv, out subtotal and tax. Lines 7–9: in subtotal, tax and "
                   "inv, out none",
                   "Lines 2–5: in nothing, out subtotal. Lines 7–9: in subtotal and tax, out "
                   "the total"],
             "c": 0,
             "why": "Lines 2 to 5 set <code>subtotal</code> before reading it and read "
                    "<code>inv</code>, set before them; <code>subtotal</code> is read after "
                    "them. So they extract as <code>subtotalOf(inv)</code>, in "
                    "<code>inv</code>, out <code>subtotal</code>. Lines 7 to 9 read "
                    "<code>subtotal</code> and <code>tax</code> and set nothing, so they extract "
                    "as <code>printTotals(subtotal, tax)</code>, out none. <code>tax</code> is "
                    "set on line 6, outside the first block, and the total is printed, not "
                    "stored."},
            {"q": "Why does extracting the loop of <code>printStatement</code>, lines 4 to 9, "
                  "need a step first?",
             "a": ["It sets two variables that are read after it, and a Java method returns one "
                   "value",
                   "It reads three variables set before it, too many for a parameter list",
                   "It contains a loop, which Extract Routine cannot move",
                   "It reads `account`, which is a parameter of the routine"],
             "c": 0,
             "why": "Out is <code>balance</code> and <code>fees</code>, both read on lines 10 to "
                    "12, and a Java method returns one value: first make a small class that "
                    "holds both, or split the work into two routines. Three parameters are "
                    "fine, a loop extracts like any other block, and reading a parameter just "
                    "makes it a parameter of the new routine."},
            # F21, pp. 580-581.
            {"q": "What does the book report about the number of lines changed and the chance "
                  "of a bad change (Weinberg 1983)?",
             "a": ["It rises from one line to five, then falls",
                   "It rises steadily with every line changed",
                   "It falls from one line to five, then rises",
                   "It is about the same for any number of lines"],
             "c": 0,
             "why": "Figure 24-1, p. 581, after Weinberg 1983: the chance of a bad change rises "
                    "as the lines changed go from one to five, and falls after that, because "
                    "small changes are treated casually. The book adds that one organisation "
                    "that began reviewing one-line changes saw its error rate fall from 55 "
                    "percent to 2 (Freedman and Weinberg 1982)."},
            {"q": "Which change to <code>printStatement</code> is a refactoring in Fowler's "
                  "sense, as the chapter adopts it?",
             "a": ["Replacing the literal 25.0 with a named constant OVERDRAFT_FEE",
                   "Changing the fee from 25.0 to 30.0",
                   "Charging the fee only once per statement",
                   "Printing the number of overdrafts as well"],
             "c": 0,
             "why": "A refactoring changes internal structure without changing observable "
                    "behaviour. The named constant prints exactly what the literal did. A "
                    "different fee, a fee charged once, and an extra line of output each "
                    "change what the routine does, however small the change."},
        ],
        "mistakes": [
            ("Thinking Extract Routine is always safe",
             "Extract Routine is the refactoring most programmers reach for first, and its "
             "mechanics look trivial: cut the lines, paste them into a new routine, call it. "
             "It is clean when the block leaves at most one result. On the lesson's "
             "illustration the loop of <code>printStatement</code> leaves two, balance and "
             "fees, and a Java method returns one value, so the refactoring needs a small "
             "class or two routines first. The chapter counts a change to a routine's "
             "interface among the riskier refactorings."),
            ("Calling any change a refactoring",
             "The chapter objects to the word's loose use. A refactoring leaves behaviour "
             "unchanged; fixing a defect, adding a feature or tweaking broken code until it "
             "works is not one, and the last, McConnell says, is hacking."),
            ("Skipping review for small changes",
             "A one-line change feels too small to go wrong. The book reports the opposite: "
             "the chance of a bad change rises from one line to five, after Weinberg, and one "
             "organisation's error rate on one-line changes fell from 55 percent to 2 when it "
             "began reviewing them, after Freedman and Weinberg."),
        ],
        "standard": (
            "Finish when you can give a block's In and Out and say whether it extracts "
            "cleanly.",
            "For a block in a routine, list the variables it reads that were set before it "
            "(its parameters) and those it sets that are read after it (its results), and say "
            "what to do when there are two results."
        ),
        "note": (
            "The lab reads the listing and computes In and Out from where each name is set "
            "and read, in line order; it does not follow calls, so a method that changes an "
            "object it is passed is invisible to it, and a field read in the block shows only "
            "in Read but set nowhere. It never runs the code. Whether the extracted routine "
            "has a good name and one clear purpose is the chapter's question, not the count's."
        ),
    },
    # ---------------------------------------------------------------- 07
    # McConnell Chapter 25, pp. 587-608. Quote: p. 608 (Key Points), 25 words.
    # Performance and quality, the camera, p. 588; the viewpoints and
    # requirements, p. 589; hardware and code tuning defined, p. 591; the Pareto
    # principle, p. 592 (F22); old wives' tales, pp. 593-596; when to tune and
    # compiler optimisations, pp. 596-597; kinds of fat, pp. 597-603;
    # measurement and the matrix, pp. 603-604; iteration, p. 605; the approach,
    # p. 606.
    {
        "slug": "code-tuning-strategies",
        "title": "Code-Tuning Strategies",
        "module": "Chapter 25 · Code-Tuning Strategies",
        "one_line": "A program is only as much faster as the time the changed code took, so measure where the time goes before changing anything.",
        "summary": (
            "Chapter 25 sets code tuning in its place: after requirements, design, the "
            "operating system, the compiler and the hardware, and only after measuring. "
            "Compute the overall speedup a change to one routine gives, from a profile, and "
            "find the few routines that hold most of the time."
        ),
        "key": [
            "measure before you tune",
            "new total: old, minus the part, plus part / k",
            "speedup: old time over new time",
            "a few routines hold most of the time",
            "keep a change only if it measures faster",
        ],
        "key_label": "Tuning in five lines",
        "concepts_intro": (
            "The chapter is about where to spend effort on speed; the lesson keeps its "
            "definition, its principle, and the arithmetic that decides whether a change "
            "matters."
        ),
        "concepts": [
            ("Code tuning",
             "Changing correct code, at the scale of a few lines or one routine, to make it run "
             "more efficiently. The chapter separates it from changes to requirements, design "
             "or hardware, which it puts first."),
            ("The Pareto principle",
             "Here, the observation that a small part of a program accounts for most of its "
             "running time. The book reports Boehm's 20 percent of routines taking 80 percent "
             "of the time and Knuth's under 4 percent of a program taking over half."),
            ("Speedup",
             "The time before a change divided by the time after it. A routine made k times "
             "faster changes the total only by the share of the time that routine took."),
        ],
        "read_title": "The chapter's strategy, then the arithmetic of a profile",
        "read_intro": (
            "The lesson follows the six sections and then works out what speeding up one "
            "routine does to the whole program."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 25, p. 608.</strong> &ldquo;Most programs "
                  "spend most of their time in a small fraction of their code. You won’t know "
                  "which code that is until you measure it.&rdquo; Read Chapter 25, pages 587 "
                  "to 608, in your own copy first."),
            ("p", "Your program is slow, and you have a suspect: the formatting routine, with "
                  "its string building, which you have always thought wasteful. Chapter 25 asks "
                  "you first whether the code is the place to look at all. Section 25.1 "
                  "(p. 588) separates performance from code speed. McConnell's example is his "
                  "own: a camera whose software made him upload pictures one at a time, "
                  "replaced by a card reader that let him copy them all at once. He did not "
                  "care whether the reader's code was faster, because his throughput was. "
                  "Before code, the section lists six other places to look: the program's "
                  "requirements, where a performance target is often stated that nobody "
                  "needs; its design; the design of classes and routines; its dealings with "
                  "the operating system; the compiler; and the hardware. Code tuning is last."),
            # F22, p. 592.
            ("p", "Section 25.2 (p. 591) defines code tuning as changing correct code, a few "
                  "lines or a routine at a time, to run more efficiently, and admits its "
                  "appeal. Then the Pareto principle. The book reports Barry Boehm's figure, "
                  "that 20 percent of a program's routines consume 80 percent of its time "
                  "(1987), and Donald Knuth's, that less than 4 percent of a program usually "
                  "accounts for more than half of its run time (1971). Knuth found it with a "
                  "profiler that counted the lines executed, and the book draws the "
                  "consequence: measure to find the hot spots, and put your effort there. "
                  "These are their programs' figures, from 1971 and 1987; your profile is "
                  "what applies to yours."),
            ("p", "The section then takes apart four beliefs it calls old wives' tales: that "
                  "fewer lines of source run faster; that some operations are probably faster "
                  "than others, when the answer changes with every compiler and machine; that "
                  "you should optimise as you go; and that speed matters as much as "
                  "correctness. Against optimising as you go it cites Knuth's warning about "
                  "premature optimisation, and points out that nobody can tell which small "
                  "part of a program will be the bottleneck until the program works. "
                  "M. A. Jackson's rules of optimisation, which the chapter quotes in its "
                  "margin, make the point drily: the first is don't, and the second, for "
                  "experts only, is not yet. Good compilers, it adds, optimise straightforward "
                  "code better than tricky code."),
            ("p", "Section 25.3 (p. 597) names the usual sources of slowness, among them input "
                  "and output, paging, system calls, interpreted languages and errors, and "
                  "notes that the relative cost of common operations changed between the "
                  "book's editions. Section 25.4 (p. 603) insists on measurement, with a story "
                  "against himself. McConnell once rewrote a matrix-summing routine with "
                  "pointers, sure he had saved thousands of multiplications, and measured it "
                  "to enjoy the result: no improvement at all, at any size, because the "
                  "compiler was already doing the same thing. What tuning without measurement "
                  "reliably produces, he concludes, is harder code. Section 25.5 (p. 605) adds "
                  "that gains come from many changes in combination, and Section 25.6 "
                  "(p. 606) gives the approach: save a working version, measure, decide "
                  "whether the problem is design or code, tune the bottleneck, measure each "
                  "change, and revert any that does not help."),
            ("def", ("Speedup from tuning one routine",
                     "If a routine took t of a program's total time T and is made k times "
                     "faster, the new total is T minus t plus t over k, and the speedup is T "
                     "over the new total. The saving can never exceed t, however large k "
                     "is.")),
            ("p", "The lab takes a profile, routine by routine, with a factor for each: 1 for "
                  "unchanged, 10 for ten times faster. The profile is the lesson's "
                  "illustration, not the book's: parse 600 ms, compute 250, format 100, write "
                  "50. The <code>tune-format</code> preset makes format ten times faster. Time "
                  "before is 1,000 ms; Time after is 910, since 100 ms became 10; Speedup is "
                  "100/91, about 1.10; Saved is 9%. Your suspect was ten times faster and the "
                  "program 9 percent faster."),
            ("p", "The <code>tune-parse</code> preset only halves parse, the routine that takes "
                  "most of the time: Time after 700, Speedup 10/7, about 1.43, Saved 30%. The "
                  "<code>tune-the-small-ones</code> preset makes format and write each a "
                  "thousand times faster: Time after 17003/20 = 850.15, Speedup 20000/17003, "
                  "about 1.18, Saved about 15.0%, half of what halving parse gives. The last "
                  "tile, Routines reaching 4/5 of the time, reads 2 of 4 for all three: taken "
                  "largest first, parse and compute already make 850 of the 1,000 ms before "
                  "any change. That four-fifths is the lab's target, not a law; on your own "
                  "profile the count could be one routine or six."),
            ("h3", "Exercise"),
            ("math", [
                "the hot routine:  95 percent of the time",
                "everything else:  5 percent",
                "change A:  everything else 1000 times faster",
                "change B:  the hot routine twice as fast",
            ]),
            ("p", "For each change, compute the share of the total time it saves, and say which "
                  "is worth making. To check, type a two-routine profile into the lab, with "
                  "times 95 and 5 and the factors each change gives."),
            ("p", "Once a measurement has found the hot spot, the question is what to change in "
                  "it. The next lesson, “Code-Tuning Techniques”, reads the chapter of things "
                  "to try."),
        ],
        "lab": ("cckit", {
            "mode": "profile",
            "view": "speedup",
            "unit": "ms",
            "preset": "tune-format",
            "presets": [
                {"id": "tune-format",
                 "label": "Make format ten times faster",
                 "routines": "parse, 600, 1; compute, 250, 1; format, 100, 10; write, 50, 1",
                 "expect": {"pfAfter": "910", "pfSpeedup": "100/91 ≈ 1.10",
                            "pfSaved": "9/100 = 9%", "pfPareto": "2 of 4"}},
                {"id": "tune-parse",
                 "label": "Make parse twice as fast",
                 "routines": "parse, 600, 2; compute, 250, 1; format, 100, 1; write, 50, 1",
                 "expect": {"pfAfter": "700", "pfSpeedup": "10/7 ≈ 1.43",
                            "pfSaved": "3/10 = 30%", "pfPareto": "2 of 4"}},
                {"id": "tune-the-small-ones",
                 "label": "Make format and write a thousand times faster",
                 "routines": "parse, 600, 1; compute, 250, 1; format, 100, 1000; write, 50, 1000",
                 "expect": {"pfAfter": "17003/20 = 850.15", "pfSpeedup": "20000/17003 ≈ 1.18",
                            "pfPareto": "2 of 4"}},
            ],
            "panel_title": "What tuning one routine does to the whole",
            "panel_intro": (
                "Each routine has its time before the change and a factor: 1 leaves it "
                "unchanged, 10 makes it ten times faster. The lab totals the times before and "
                "after and counts how many routines, largest first, hold four-fifths of the "
                "time before. Figures: an illustrative profile, not the book's."
            ),
        }),
        "steps_title": "Deciding what to tune",
        "steps_intro": "Four steps from a profile, and one with a profile of your own.",
        "steps": [
            ("Measure first",
             "Take a profile of the program on a realistic run, and list its routines by the "
             "time each takes, largest first."),
            ("Find the few that matter",
             "Count how many routines, from the top of the list, make up most of the time. "
             "Those are the only candidates."),
            ("Work out the most a change can save",
             "For a routine taking t of the total T, made k times faster, the new total is T "
             "minus t plus t over k. Even an infinite k saves only t."),
            ("Measure the change, and keep it only if it helps",
             "Save a working version, make one change, measure again, and revert the change if "
             "the time did not fall."),
            ("Profile a program of your own",
             "Take a profile of a program of yours, type its top four routines into the lab "
             "with their times, and note how many reach four-fifths of the time and what the "
             "best single change could save."),
        ],
        "worked": {
            "title": "Ten times faster, 9 percent saved",
            "intro": [
                "Take the <code>tune-format</code> preset: parse 600 ms, compute 250, format "
                "100, write 50, and format made ten times faster.",
            ],
            "lines": [
                "before:  600 + 250 + 100 + 50 gives 1000 ms",
                "format after:  100 / 10 gives 10 ms",
                "after:  1000 - 100 + 10 gives 910 ms",
                "speedup:  1000 / 910, about 1.10",
                "saved:  90 of 1000 ms, 9 percent",
            ],
            "after": [
                "Halving parse instead, the <code>tune-parse</code> preset, saves 300 ms, more "
                "than three times as much, from a change one-fifth as large.",
            ],
        },
        "quiz_title": "Profiles and speedups",
        "quiz": [
            {"q": "A program spends 95% of its time in one routine and 5% elsewhere. What share "
                  "of the total does each change save: A, the 5% made a thousand times faster; "
                  "B, the hot routine made twice as fast?",
             "a": ["A about 5.0%, B 47.5%", "A about 99.9%, B 50%", "A 5%, B 95%",
                   "A about 0.5%, B 47.5%"],
             "c": 0,
             "why": "A: the 5 parts become 5/1000, so it saves 4.995 of 100, 999/20000, about "
                    "5.0%. B: the 95 parts become 47.5, so it saves 19/40 = 47.5%. Making the "
                    "small part a thousand times faster can never save more than the 5% it "
                    "took; halving the hot routine saves nearly ten times as much. 99.9% is the "
                    "speedup of the small part alone, and 95% would need the hot routine to "
                    "take no time at all."},
            {"q": "A routine taking 100 ms of a 1,000 ms run is made ten times faster. What is "
                  "the new total?",
             "a": ["910 ms", "900 ms", "100 ms", "990 ms"],
             "c": 0,
             "why": "1,000 − 100 + 100/10 = 910 ms. 900 forgets the 10 ms the routine still "
                    "takes, 100 divides the whole run by ten, and 990 takes 10 ms off instead "
                    "of 90."},
            # F22, p. 592.
            {"q": "What did Knuth find in his 1971 study of Fortran programs, as the book reports "
                  "it?",
             "a": ["Less than 4% of a program usually accounts for more than 50% of its run time",
                   "20% of a program's routines consume 80% of its time",
                   "Half the code accounts for half the time",
                   "Most of the time is spent in input and output"],
             "c": 0,
             "why": "Section 25.2, p. 592: Knuth (1971) found that less than four percent of a "
                    "program usually accounts for more than half its run time. The 20 and 80 "
                    "figure is Boehm's (1987), which the book reports beside it. Input and "
                    "output are among the chapter's usual sources of slowness, not Knuth's "
                    "finding."},
            {"q": "The chapter's approach to code tuning (Section 25.6) says what to do with a "
                  "change that does not make the measured time fall?",
             "a": ["Revert to the saved working version",
                   "Keep it, since a tuning change cannot hurt",
                   "Combine it with the next change and measure both together",
                   "Rewrite the routine in a lower-level language"],
             "c": 0,
             "why": "Page 606: measure each improvement one at a time, and if it does not "
                    "improve the code, revert to the version saved before. The book adds that "
                    "attempted tunings often make little or no difference or make things "
                    "worse, so keeping them costs clarity for "
                    "nothing."},
        ],
        "mistakes": [
            ("Thinking a tenfold speedup of a routine makes the program much faster",
             "A routine that runs ten times faster feels like a large win, and on its own "
             "benchmark it is one. The program gains only in proportion to the share of its "
             "time that routine took, which is why the chapter says to measure before tuning. "
             "On the lesson's illustration <code>tune-format</code> makes a routine ten times "
             "faster and the program 9 percent faster, while <code>tune-parse</code> makes the "
             "hot routine only twice as fast and saves 30 percent."),
            ("Believing fewer lines run faster",
             "The chapter's first old wives' tale. The number of lines of source says nothing "
             "reliable about the size or speed of the machine code, and its own measurements "
             "show a loop written out line by line running faster than the loop. Only a "
             "measurement says which is faster."),
            ("Tuning as you write",
             "Optimising every routine as it is written spends the effort on code that is not "
             "the bottleneck, because nobody can tell which small part of a program will be "
             "until it runs. The chapter's order is to make it correct and clear, then "
             "measure, then tune the few places the measurement points to."),
        ],
        "standard": (
            "Finish when you can compute what a change to one routine does to the whole "
            "program.",
            "For a four-routine profile and a speed factor on one routine, compute the new "
            "total, the speedup and the share saved, and how many routines reach four-fifths "
            "of the time."
        ),
        "note": (
            "The lab's profile is illustrative, and its arithmetic assumes the routines' times "
            "simply add and that speeding one up leaves the others alone; caching, input and "
            "output, and threads can each break that. It cannot measure anything: the times "
            "are what you type, and the chapter's whole point is that they must come from a "
            "measurement of your own program. The Pareto figures are Boehm's and Knuth's, from "
            "their programs."
        ),
    },
    # ---------------------------------------------------------------- 08
    # McConnell Chapter 26, pp. 609-645. Quote: p. 645 (Key Points), 28 words.
    # Anti-refactorings and things to try, pp. 609-610; logic, pp. 610-616;
    # loops, pp. 616-624 (unswitching, p. 616; minimising work inside loops,
    # p. 620; sentinels, p. 621; the busiest loop inside, p. 623, F23; strength
    # reduction, p. 623); data transformations, pp. 624-630; expressions,
    # pp. 630-639; routines, p. 639; recoding in a low-level language, p. 640;
    # the more things change, pp. 643-644.
    {
        "slug": "code-tuning-techniques",
        "title": "Code-Tuning Techniques",
        "module": "Chapter 26 · Code-Tuning Techniques",
        "one_line": "A tuning technique changes how much work the machine is asked to do, and only a measurement says whether it is faster.",
        "summary": (
            "Chapter 26 is a catalogue of things to try once a measurement has found a hot "
            "spot: in logic, loops, data, expressions and routines, each with the book's own "
            "timings in several languages. Count the loop iterations of a nest in two orders, "
            "and move work that does not change out of a loop, stating what is saved."
        ),
        "key": [
            "a catalogue of things to try",
            "nest: outer + outer × inner passes",
            "outer 100, inner 5: 600 passes",
            "invariant work moves out of the loop",
            "fewer passes is not less time",
            "measure each change",
        ],
        "key_label": "Techniques in six lines",
        "concepts_intro": (
            "The chapter is a long list; the lesson keeps what the list is, one technique the "
            "lab can count, and one the exercise asks you to make."
        ),
        "concepts": [
            ("Anti-refactoring",
             "McConnell's name for the chapter's changes: they make the code's structure worse "
             "in exchange for speed, by definition, since a change that made it better would "
             "simply be good practice."),
            ("The busiest loop inside",
             "In a nest of loops, each loop pays for its own start, test and increment every "
             "time it runs. Putting the loop with the most iterations inside means the costlier "
             "bookkeeping is paid fewer times."),
            ("Loop-invariant work",
             "A computation inside a loop whose result is the same on every pass. Computed "
             "once before the loop, it gives the same result for less work, if the computation "
             "cost anything."),
        ],
        "read_title": "The chapter's catalogue, then two loop techniques counted",
        "read_intro": (
            "The lesson goes through the seven sections briefly and then counts what two loop "
            "techniques change."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 26, p. 645.</strong> &ldquo;Results of "
                  "optimizations vary widely with different languages, compilers, and "
                  "environments. Without measuring each specific optimization, you’ll have no "
                  "idea whether it will help or hurt your program.&rdquo; Read Chapter 26, "
                  "pages 609 to 645, in your own copy first."),
            ("p", "Once a measurement has found the hot spot, what can you change in it? "
                  "Chapter 26 (p. 609) answers with a catalogue, and warns at once that it is "
                  "a list of things to try, many of which will not work in your environment. "
                  "McConnell calls the changes anti-refactorings: where Chapter 24's changes "
                  "improve a program's structure, these make it worse in exchange for speed, "
                  "by definition, since a change that improved both would simply be good "
                  "practice. Every technique comes with the book's own timings, in several "
                  "languages, and the timings are the chapter's real lesson: they disagree."),
            ("p", "Section 26.1 (p. 610) is logic: stop testing once you know the answer, which "
                  "Java's `&&` and `||` do for you by short-circuit evaluation; order tests by "
                  "how often they succeed; compare similar logic structures; replace a "
                  "complicated expression with a table lookup; and compute a value lazily, "
                  "only when it is needed. Section 26.2 (p. 616) is loops: unswitching, which "
                  "moves a decision that never changes out of the loop; jamming two loops "
                  "over the same range into one; unrolling; minimising the work inside a loop; "
                  "a sentinel value at the end of a search; the busiest loop on the inside; "
                  "and strength reduction, replacing a multiplication by the loop index with "
                  "a running addition."),
            ("p", "Section 26.3 (p. 624) transforms data: integers rather than floating point, "
                  "fewer array dimensions, fewer array references, supplementary indexes, "
                  "caching. Section 26.4 (p. 630) works on expressions: algebraic identities, "
                  "cheaper operations, values computed at compile time or in advance, "
                  "constants of the right type, common subexpressions computed once, and a "
                  "warning about slow system routines. Section 26.5 (p. 639) finds that putting "
                  "a routine's code inline saves little on modern machines, and in one of its "
                  "languages costs time. Section 26.6 (p. 640) describes recoding a hot spot in "
                  "a lower-level language, after the program is complete and profiled."),
            ("p", "Section 26.7 (p. 643) looks back over the decade between the editions. "
                  "Computers became so much faster that McConnell had to repeat most tests "
                  "far more times to measure anything, and for many programs, he says, this "
                  "level of optimisation has become irrelevant; for embedded and real-time "
                  "work it has not. The effect of any one technique, he finds, is less "
                  "predictable than it was, and his rule is that an optimisation worth making "
                  "is worth measuring, and one not worth measuring is not worth the loss of "
                  "clarity."),
            # F23, p. 623.
            ("p", "One technique the lab can count. The book's own example (p. 623) is a nest "
                  "whose outer loop runs 100 times and whose inner loop runs 5 times on each "
                  "pass: 100 outer passes and 500 inner ones, 600 in all. Swapped, it is 5 "
                  "outer and 500 inner, 505, about 16 percent fewer. The book then measured "
                  "the swap: 33 percent less time in C++, 34 in Java, 12 in PHP and 4 in "
                  "Python. Those are its measurements on its machines in 2004; the spread "
                  "between them is the point."),
            ("def", ("Loop passes",
                     "Each time a loop's body begins counts as one pass of that loop. In a nest "
                     "with sizes a outside and b inside, the outer loop makes a passes and the "
                     "inner loop a times b; the innermost body runs a times b times whichever "
                     "order the loops are in.")),
            ("p", "The lab takes the sizes of a nest from outside in. The "
                  "<code>busiest-outside</code> preset is the book's example, 100 then 5: Body "
                  "runs 500, Passes, as given 600, Passes, smallest outside 505, and Saved "
                  "19/120, about 15.8%. The <code>busiest-inside</code> preset is the swapped "
                  "order, 5 then 100: 500, 505, 505 and Saved 0%, since it is already best. "
                  "The <code>three-levels</code> preset is the lesson's own, 50, 10 and 2: the "
                  "body runs 1,000 times either way, the passes fall from 1,550 to 1,022, and "
                  "Saved is 264/775, about 34.1%. The body never runs less; only the loops' "
                  "bookkeeping does."),
            ("p", "That is all the lab can say. It counts passes, not time, and the book's own "
                  "measurements of this very change run from a third of the time saved to "
                  "almost nothing, depending on the language. In Java a just-in-time compiler "
                  "may reorder or simplify loops itself, as an optimising C++ compiler may, so "
                  "the count is a reason to try the change and measure it, and not a "
                  "prediction of what you will see."),
            ("h3", "Exercise"),
            ("code", _lines(GROSS_LOOP)),
            ("p", "With n equal to 1,000, move the work that is the same on every pass out of "
                  "the loop. Write the changed code, and state how many times the loop body "
                  "runs and how many times <code>config.taxRate()</code> is called, before and "
                  "after. Then say what would tell you whether the change made the program "
                  "faster."),
            ("p", "This ends Code Improvements, the book's Part V. The next course, System "
                  "Considerations, widens the view from the routine to the project, beginning "
                  "with “How Program Size Affects Construction”."),
        ],
        "lab": ("cckit", {
            "mode": "run",
            "view": "nested",
            "preset": "busiest-outside",
            "presets": [
                {"id": "busiest-outside",
                 "label": "The book's example: 100 outer passes, 5 inner",
                 "sizes": "100 5",
                 "expect": {"lpBody": "500", "lpIterations": "600", "lpBest": "505",
                            "lpSaved": "19/120 ≈ 15.8%"}},
                {"id": "busiest-inside",
                 "label": "Swapped: 5 outer passes, 100 inner",
                 "sizes": "5 100",
                 "expect": {"lpIterations": "505", "lpBest": "505", "lpSaved": "0 = 0%"}},
                {"id": "three-levels",
                 "label": "Three levels: 50, 10 and 2",
                 "sizes": "50 10 2",
                 "expect": {"lpBody": "1,000", "lpIterations": "1,550", "lpBest": "1,022",
                            "lpSaved": "264/775 ≈ 34.1%"}},
            ],
            "panel_title": "Loop passes in a nest",
            "panel_intro": (
                "Give each loop's iterations, outermost first. The lab counts how often the "
                "body runs, the passes of every loop in the order given, and the passes with "
                "the smallest loop outside. It counts passes, not time."
            ),
        }),
        "steps_title": "Trying a loop technique",
        "steps_intro": "Four steps on a hot loop, and one on a loop of your own.",
        "steps": [
            ("Confirm it is the hot spot",
             "Change a loop only after a measurement has shown that the program spends its "
             "time there."),
            ("Count the passes",
             "For a nest, add the passes of every loop: the outer size, plus the outer times "
             "the next, and so on. Then count them with the loops in the other orders."),
            ("Find what does not change",
             "Look for any computation inside the loop whose inputs are the same on every "
             "pass, and compute it once before the loop instead."),
            ("Measure, and keep what helps",
             "Time the loop before and after on your own compiler and machine, and revert the "
             "change if the time did not fall by enough to pay for the lost clarity."),
            ("Count a nest of your own",
             "Take one loop nest from your own code, type its sizes into the lab, note the "
             "passes saved by reordering, and move one invariant computation out of it."),
        ],
        "worked": {
            "title": "The busiest loop inside",
            "intro": [
                "Take the <code>busiest-outside</code> preset, the book's example: an outer "
                "loop of 100 and an inner loop of 5.",
            ],
            "lines": [
                "as given:  100 + 100 × 5 gives 600 passes",
                "swapped:  5 + 5 × 100 gives 505 passes",
                "body, either way:  500 runs",
                "saved:  95 of 600 passes, about 15.8 percent",
            ],
            "after": [
                "The book measured this change at 33 percent less time in C++ and 4 percent in "
                "Python: the count is the same in every language, and the time is not.",
            ],
        },
        "quiz_title": "Passes, calls and measurement",
        "quiz": [
            {"q": "In the exercise's loop, with n = 1,000, the call <code>config.taxRate()</code> "
                  "is moved before the loop. How many times does the body run, and how many "
                  "times is <code>taxRate()</code> called, after the change?",
             "a": ["Body 1,000 times; taxRate once", "Body once; taxRate once",
                   "Body 1,000 times; taxRate 1,000 times", "Body 999 times; taxRate once"],
             "c": 0,
             "why": "<code>double rate = config.taxRate();</code> moves before the loop, and the "
                    "body keeps only <code>gross[i] = net[i] * (1 + rate);</code>. The body still "
                    "runs 1,000 times; <code>taxRate()</code> is called once instead of 1,000 "
                    "times. That is a saving only if the call costs something, which only a "
                    "measurement can say, and only if it returns the same value on every pass, "
                    "which is what moving it assumes."},
            {"q": "A nest has an outer loop of 50, a middle loop of 10 and an inner loop of 2. "
                  "How many passes do the three loops make in that order?",
             "a": ["1,550", "1,000", "1,022", "62"],
             "c": 0,
             "why": "50 + 50 × 10 + 50 × 10 × 2 = 50 + 500 + 1,000 = 1,550. 1,000 is how often "
                    "the innermost body runs, 1,022 is the passes with the smallest loop "
                    "outside (2 + 20 + 1,000), and 62 adds the sizes."},
            # F23, p. 623.
            {"q": "The book measured putting the busiest loop inside on its 100 by 5 example "
                  "(p. 623). What did it find?",
             "a": ["Savings from 33% in C++ and 34% in Java to 4% in Python",
                   "About 16% in every language, as the count predicts",
                   "No saving in any language",
                   "A slowdown in Java and a saving elsewhere"],
             "c": 0,
             "why": "The count predicts about 16 percent fewer iterations; the book's "
                    "measurements were 33 percent less time in C++, 34 in Java, 12 in PHP and 4 "
                    "in Python. The book's conclusion is that you have to measure in your own "
                    "environment."},
            {"q": "Why does the chapter call its techniques anti-refactorings?",
             "a": ["They make the code's internal structure worse in exchange for speed",
                   "They change what the program does",
                   "They undo the refactorings of Chapter 24 one by one",
                   "They are refactorings that happen to run backwards in time"],
             "c": 0,
             "why": "Page 609: refactorings improve a program's internal structure; these "
                    "changes degrade it in exchange for performance, by definition, since a "
                    "change that did both would be standard practice. They are meant to leave "
                    "behaviour unchanged."},
        ],
        "mistakes": [
            ("Thinking a technique that saves 16% of iterations saves 16% of time",
             "The count is easy to make and looks like a prediction. But the lab counts loop "
             "passes, not time. The book measured this very change on its own example and "
             "found savings from about a third of the time in C++ and Java to 4 percent in "
             "Python, and the chapter's lesson is to measure each change in your own "
             "environment."),
            ("Tuning before measuring",
             "The techniques in the chapter are for hot spots a measurement has found. Applied "
             "everywhere, they make the code harder to read in places where the speed was never "
             "the problem, and Chapter 25's figures put most of the time in a small part of "
             "the program."),
            ("Moving work that is not invariant",
             "A call can be moved out of a loop only if it gives the same result on every pass "
             "and nothing depends on its being made each time. Moving a call that reads a "
             "changing value, or that has an effect of its own, changes what the loop does."),
        ],
        "standard": (
            "Finish when you can count a nest's passes in two orders and move invariant work "
            "out of a loop.",
            "For a nest with given iteration counts, compute the body runs, the total passes "
            "in each order and the share saved; for a loop with an invariant call, write the "
            "moved version and state the calls before and after."
        ),
        "note": (
            "The lab counts loop passes, not time, and treats every pass as costing the same. "
            "The book's own measurements of the same change ranged from a third of the time "
            "saved in two languages to almost nothing in another, and a modern compiler or "
            "just-in-time compiler may make the change for you, so only a measurement on your "
            "own machine says what a technique does."
        ),
    },
]
