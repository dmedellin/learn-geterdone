"""Dynamic Programming and Optimal Substructure, lessons 01-06 - the recurrence, the memo, the fill order, the grid."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "where-the-greedy-choice-fails",
        "title": "Where the Greedy Choice Fails",
        "module": "A table, an order, a recurrence",
        "one_line": "Run the fewest-coins recurrence on a coin system where taking the largest coin first is already wrong, and count all three routes to the answer.",
        "summary": (
            "Greedy Algorithms and Matroids proved a rule correct by exchange wherever the "
            "structure allowed it. Change the coins to 1, 3 and 4 and the largest-first rule "
            "returns three coins for an amount of six where two suffice. What replaces the rule "
            "is not a better rule: it is a recurrence that tries every first coin and keeps the "
            "best, and everything on this course is the cost of evaluating one."
        ),
        "key": [
            "f(0) = 0        f(a) = 1 + min over coins c ≤ a of f(a − c)",
            "",
            "coins 1, 3, 4 and an amount of 6",
            "  largest coin first    4 + 1 + 1     three coins",
            "  the recurrence        3 + 3         two coins",
            "",
            "one failing instance refutes a rule; a hundred passing ones refute nothing",
        ],
        "key_label": "One recurrence, and the six-unit instance the greedy rule gets wrong",
        "concepts_intro": (
            "One hard idea: optimal substructure, which is the property that licenses the "
            "recurrence and is a proof obligation rather than a hope. The other two are about "
            "what a failing instance does and does not establish."
        ),
        "concepts": [
            ("A greedy rule commits to a first choice; a recurrence does not",
             "Largest-first takes the 4, and is then solving for 2 with nothing better than a "
             "1 available: `4 + 1 + 1`, three coins, and it never reconsiders. The recurrence "
             "asks `f(6) = 1 + min(f(5), f(3), f(2))`, which is every legal first coin at once, "
             "and `f(3) = 1` gives `f(6) = 2`. The difference is not cleverness. It is that one "
             "of them discards the alternatives before it knows what they cost."),
            ("Optimal substructure is what licenses the recurrence",
             "If some fewest-coin way of making `a` begins with coin `c`, then what remains is "
             "a fewest-coin way of making `a − c` &mdash; because a cheaper way of making "
             "`a − c` could be substituted in and would give a cheaper way of making `a`, "
             "contradicting the first. That substitution argument is the whole justification "
             "for reading `f(a)` off smaller values of `f`, and a problem without it cannot be "
             "written as a recurrence over subproblems at all."),
            ("A failing instance refutes a rule; passing instances establish nothing",
             "Six units from 1, 3 and 4 settles the question of whether largest-first is "
             "correct for every coin system: it is not, and one counterexample is enough. Now "
             "switch the lab to 1, 2 and 5 and the same rule is optimal at every amount you "
             "will type. That is a fact about that coin system, established by trial for the "
             "amounts you tried, and it is not a proof about the system, let alone about the "
             "rule."),
        ],
        "read_title": "The recurrence, the property it needs, and what the counterexample settles",
        "read_intro": "The problem, the instance where greed fails, the substitution argument, and the three routes the lab runs.",
        "body": [
            ("def", ("The fewest-coins problem",
                     "Given a set of coin denominations and an amount `a`, find the smallest "
                     "number of coins, each denomination usable any number of times, that add "
                     "to exactly `a`. If no multiset of the coins adds to `a` the answer is "
                     "that the amount cannot be made, which is a result and not a failure.")),
            ("p", "Two things are being separated here, and conflating them is the reason this "
                  "lesson comes first. A <strong>rule</strong> says what to do next: take the "
                  "largest coin that fits. A <strong>recurrence</strong> says what the answer "
                  "is in terms of smaller answers, and commits to nothing. Greedy Algorithms "
                  "and Matroids is about the conditions under which a rule can be proved "
                  "correct; this course is about what to do when it cannot."),
            ("example", ("Six units from 1, 3 and 4",
                         "Largest-first takes 4, leaving 2, then 1, leaving 1, then 1: "
                         "`4 + 1 + 1`, three coins. The lab reports the answer as 2 and the "
                         "coins it uses as `3 + 3`, re-added on the panel to 6. Both are legal "
                         "ways to pay. Only one of them is fewest, and the rule does not find "
                         "it on this input.")),
            ("p", "Notice how little it took. The coin system is three denominations and the "
                  "amount is six; nothing here is adversarially large. A reader who has just "
                  "spent a course proving greedy rules correct by exchange should read this as "
                  "the boundary being drawn rather than as a trick, because the exchange "
                  "argument that works for the fractional problem really does fail here, and "
                  "the lesson after next is where that failure is made explicit on a second "
                  "problem."),
            ("def", ("Optimal substructure",
                     "A problem has <strong>optimal substructure</strong> when an optimal "
                     "solution to it contains, as a part, an optimal solution to a smaller "
                     "instance of the same problem. The phrase names a proof obligation: you "
                     "show that a better solution to the part could be cut in, which is what "
                     "makes the recurrence a statement about optima rather than about some "
                     "solutions.")),
            ("thm", ("The coin recurrence is correct",
                     "Let `f(a)` be the fewest coins that add to `a`, with `f(0) = 0` and "
                     "`f(a)` undefined when no multiset adds to `a`. Then for every `a &gt; 0` "
                     "that can be made, `f(a) = 1 + min of f(a − c)` over all coins `c ≤ a` "
                     "for which `a − c` can be made.")),
            ("proof", ("Both directions. Any multiset of coins adding to `a` has a first coin "
                       "`c`, and removing it leaves a multiset adding to `a − c` with one "
                       "fewer coin; so `f(a) ≥ 1 + f(a − c)` for that `c`, and therefore "
                       "`f(a) ≥ 1 + min of f(a − c)`.",
                       "For the other direction, take the `c` attaining the minimum and a "
                       "cheapest multiset for `a − c`; adding one `c` to it gives a multiset "
                       "adding to `a` of size `1 + f(a − c)`, so `f(a) ≤ 1 + min of f(a − c)`. "
                       "The two inequalities give equality, and the substitution in the second "
                       "half is the optimal-substructure argument doing its work.")),
            ("h3", "What the rule needed, and the recurrence does not"),
            ("p", "The exchange argument behind a greedy rule needs more than optimal "
                  "substructure: it needs the <em>greedy choice property</em>, that some "
                  "optimal solution agrees with the rule on the first step. With coins 1, 3 "
                  "and 4 at an amount of six there is no optimal solution containing a 4, so "
                  "that property is simply false, and the exchange has nothing to exchange "
                  "into. Optimal substructure survives untouched &mdash; which is precisely "
                  "why the recurrence still works when the rule does not."),
            ("p", "This is the split the Subject's ordering is built on. Greedy needs both "
                  "properties and pays `O(n log n)`; dynamic programming needs only the first "
                  "and pays for it in table cells. Neither is stronger than the other; they "
                  "assume different things, and the assumption is the thing to check."),
            ("h3", "Three routes, and three costs that are not the point until they agree"),
            ("p", "The lab runs the same definition three ways: as a recursion with no memory, "
                  "as the same recursion writing each answer down the first time, and as a "
                  "table filled bottom-up. On this instance the three answers are all 2, and "
                  "the costs are 24 calls, 14 calls, and 28 cells. The panel prints the ratio "
                  "as an exact fraction &mdash; `12/7`, about 1.7 times fewer calls &mdash; "
                  "and says explicitly that the comparison is worth nothing unless the answers "
                  "match, which is why they are checked before they are counted."),
            ("p", "Read those three numbers carefully, because they do not say what a reader "
                  "expects. The table fills 28 cells; the memo-free recursion makes 24 calls. "
                  "On this input the exponential method does <em>less</em> work than the "
                  "polynomial one. The proved bounds are unchanged &mdash; the table is "
                  "`Θ(nk)` cells for `n` denominations and amount `k`, and the plain recursion "
                  "is exponential in `k` &mdash; and the next lesson moves the amount to "
                  "eighteen, where the same two routes cost 22 089 calls and 76 cells. A count "
                  "at one size cannot order two growth rates, and this page is the smallest "
                  "instance on the course where it visibly gets the order wrong."),
        ],
        "lab": ("dpkit", {
            "mode": "memo",
            "preset": "awkward",
            "panel_title": "Choose a coin system that defeats the greedy rule",
            "panel_intro": "The panel loads coins 1, 3 and 4 at an amount of six, where "
                           "largest-first pays three coins and two are enough. Switch to 1, 2 "
                           "and 5 and the rule becomes optimal at every amount you try, which "
                           "is worth doing precisely because it proves nothing.",
        }),
        "steps_title": "Deciding whether a rule is available before reaching for a table",
        "steps_intro": "The recurrence is cheap to write and expensive to evaluate, so it is worth one honest attempt to avoid it.",
        "steps": [
            ("State the recurrence before you state a rule",
             "Write what the answer is in terms of smaller answers, with every legal first "
             "choice in the minimum. That expression is correct or it is not, independently of "
             "how you intend to evaluate it, and it is the thing the rest of the work has to "
             "agree with."),
            ("Discharge optimal substructure by substitution",
             "Assume an optimal solution whose part is not optimal, cut the better part in, "
             "and derive a contradiction. If the substitution does not go through &mdash; "
             "because the part interacts with the rest &mdash; the recurrence is not licensed "
             "and no amount of filling a table will repair it."),
            ("Try to break the greedy rule, not to confirm it",
             "Spend the effort on a counterexample. Small denominations that are not multiples "
             "of one another are where they live: 1, 3, 4 breaks largest-first at six, and 1, "
             "3, 4 is the smallest system this library knows of that does. Confirmations cost "
             "the same and buy nothing."),
            ("Count all three routes on your own input",
             "Run the recursion, the memo and the table on the instance you actually have. The "
             "ordering between them changes with size, and the only way to know which is "
             "cheaper at your size is the counter, not the complexity class."),
            ("Make the answers agree before comparing the costs",
             "Three costs are interesting only when the three answers are one answer. The lab "
             "prints a verdict for that first and says so in the banner; a cost comparison "
             "between a right method and a wrong one is not a comparison."),
        ],
        "worked": {
            "title": "The table for coins 1, 3, 4 at an amount of six",
            "intro": [
                "One row per coin type added to the system, one column per amount from zero "
                "up. Each row answers the same question the row above it answered, with one "
                "more denomination available. A dot is an amount that cannot be made with the "
                "coins so far.",
            ],
            "lines": [
                "amount            0    1    2    3    4    5    6",
                "",
                "no coins          0    ·    ·    ·    ·    ·    ·",
                "with 1            0    1    2    3    4    5    6",
                "with 1, 3         0    1    2    1    2    3    2",
                "with 1, 3, 4      0    1    2    1    1    2    2",
                "",
                "the last cell reads two others:",
                "  skip the 4:   the cell above it, which is 2",
                "  take a 4:     the cell two columns left in its OWN row, plus one,",
                "                which is 2 + 1 = 3",
                "so the answer is 2, and the coins are 3 + 3",
                "",
                "largest coin first would have paid   4 + 1 + 1   =   three coins",
            ],
            "after": [
                "The row for 1, 3 already contains the answer: `f(3) = 1`, so `f(6) = 2` by "
                "taking two threes, and adding the 4 to the system changes nothing at the "
                "amount asked about. That is worth noticing, because the greedy rule's whole "
                "mistake was to use the 4 &mdash; the denomination that turns out to be "
                "irrelevant at six is the one it reaches for first.",
                "Move the highlighted cell along the range control and the lab repaints the "
                "cells that cell read, in amber. That list is not a description of the "
                "recurrence written out beside it; it is recorded by the reads the recurrence "
                "itself performed, so it cannot disagree with what the code did. Two cells for "
                "every cell in the bottom row, here.",
                "For a faded rehearsal, keep the coins and set the amount to 11 before running "
                "it. The supplied first move: largest-first pays `4 + 4 + 3`, which is three "
                "coins. Decide whether the recurrence can do better, then check &mdash; and "
                "notice that being right about this one tells you nothing about twelve.",
            ],
        },
        "quiz_title": "Rules, recurrences, and what one instance settles",
        "quiz": [
            {"q": "With coins 1, 3 and 4, largest-first pays three coins for an amount of six and the recurrence finds two. What has been established?",
             "a": ["That largest-first is not correct for every coin system",
                   "That largest-first is wrong whenever the amount is six",
                   "That no greedy rule can be correct for any coin system",
                   "That dynamic programming is faster than greedy on this input"],
             "c": 0,
             "why": "A single counterexample refutes a universal claim and nothing more. It "
                    "says nothing about other amounts &mdash; largest-first is optimal at five "
                    "and at seven in this same system &mdash; and nothing about other rules or "
                    "other systems. It is also not a claim about cost: on this instance the "
                    "memo-free recursion makes 24 calls where the table fills 28 cells."},
            {"q": "Which property does the recurrence `f(a) = 1 + min of f(a − c)` need in order to be correct?",
             "a": ["The greedy choice property: some optimum starts with the largest coin",
                   "Optimal substructure: an optimal solution contains an optimal solution to the remaining amount",
                   "That the denominations are multiples of one another",
                   "That every amount below `a` can be made"],
             "c": 1,
             "why": "Optimal substructure is exactly what the proof's second half uses: a "
                    "cheaper way of making `a − c` could be substituted in. The greedy choice "
                    "property is the extra thing a rule needs and this instance does not have. "
                    "Neither divisibility nor reachability of every smaller amount is required "
                    "&mdash; the coins 4 and 7 make most small amounts impossible and the "
                    "recurrence still answers correctly."},
            {"q": "Switching the lab to coins 1, 2 and 5, largest-first returns the fewest coins at every amount you try. What does that establish about that coin system?",
             "a": ["That largest-first is optimal for that system, since no counterexample exists",
                   "That the recurrence is unnecessary for that system",
                   "Nothing on its own: those are the amounts you tried, and a rule is proved from its structure",
                   "That 1, 2 and 5 are pairwise coprime, which is what makes greed work"],
             "c": 2,
             "why": "The asymmetry is the lesson. A violation settles the question outright; "
                    "agreement on a finite set of amounts is evidence about those amounts. "
                    "Largest-first genuinely is optimal for 1, 2 and 5, but that is a theorem "
                    "about that system's structure, not something the lab established. The "
                    "coprimality answer is also false as stated: 1, 3 and 4 are pairwise "
                    "coprime and the rule fails on them."},
            {"q": "On this instance the memo-free recursion makes 24 calls and the table fills 28 cells. Which conclusion is supported?",
             "a": ["The memo-free recursion has the better growth rate",
                   "The table is the wrong method for the fewest-coins problem",
                   "The two methods are within a constant factor of each other",
                   "Neither method's growth is settled by this: it is one amount, and the ordering reverses as the amount grows"],
             "c": 3,
             "why": "A count is evidence about the input it was taken on. The table is `Θ(nk)` "
                    "and the plain recursion is exponential in the amount, and at an amount of "
                    "eighteen the same two routes cost 76 cells and 22 089 calls. A constant "
                    "factor is a claim about all sizes and cannot be read off one, either."},
        ],
        "mistakes": [
            ("Reading a greedy failure as a verdict on greedy",
             "The failure here is of one rule on one coin system. Greedy Algorithms and "
             "Matroids proves several rules correct, and the matroid theorem says exactly when "
             "the pattern is available. What this instance shows is that availability has to "
             "be checked per problem, not that the technique is unsound."),
            ("Treating optimal substructure as obvious",
             "It is a property that genuinely fails: the longest <em>simple</em> path between "
             "two vertices does not decompose this way, because the two halves can be optimal "
             "separately and share a vertex, and the join is then not a simple path at all. "
             "The substitution argument is what distinguishes the cases, and skipping it is "
             "how a confident recurrence for a problem that has no recurrence gets written."),
            ("Taking the smaller count at one size for the better method",
             "The panel prints 24 calls against 28 cells and the exponential route wins. A "
             "reader who stops there has measured a case and stated a class. Move the amount "
             "and the two numbers cross; the bound is what says which side of the crossing you "
             "are eventually on, and the counter is what says which side you are on now."),
        ],
        "standard": ("Finish when you can say what a counterexample to a rule does and does not settle.",
                     "You should be able to write the recurrence for a problem, discharge "
                     "optimal substructure by substitution, name the extra property a greedy "
                     "rule would need, and read a cost comparison without turning it into a "
                     "statement about growth."),
        "note": ("The recurrence is correct and, run as written, it is unusable: the next "
                 "lesson moves the amount from six to eighteen and watches the same code make "
                 "22 089 calls to answer a question with eighteen distinct parts to it."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "overlapping-subproblems-and-the-memo",
        "title": "Overlapping Subproblems and the Memo",
        "module": "A table, an order, a recurrence",
        "one_line": "Count the calls the same recursion makes with and without a memo, and find the number of distinct subproblems that explains the gap.",
        "summary": (
            "The recurrence from the previous lesson is correct and, evaluated as written, "
            "makes 22 089 calls to answer a question about an amount of eighteen. With a memo "
            "it makes 50. The ratio is not a speed-up trick: it is the count of distinct "
            "subproblems, eighteen of them, against the number of times a memo-free recursion "
            "asks the same questions over again."
        ),
        "key": [
            "coins 1, 2, 5 and an amount of 18",
            "  no memo          22 089 calls",
            "  with a memo           50 calls      18 distinct subproblems",
            "  the table             76 cells      no recursion at all",
            "",
            "22089/50 = 441.8 times fewer, and all three answer 5",
            "",
            "overlapping subproblems: the recursion tree has few DISTINCT nodes",
        ],
        "key_label": "Three routes to one answer, and the count that explains the gap",
        "concepts_intro": (
            "The hard idea is that the memo's saving is predicted, not discovered: it is the "
            "recursion tree's node count against the number of distinct arguments, and both "
            "are on the panel."
        ),
        "concepts": [
            ("Overlapping subproblems is a property of the recursion, not of the code",
             "`f(18)` asks for `f(17)`, `f(16)` and `f(13)`; `f(17)` asks for `f(16)` again. "
             "The recursion tree has thousands of nodes and eighteen distinct arguments, "
             "because the argument is a single number between 1 and 18. A recursion whose "
             "arguments are all distinct &mdash; merge sort's halves, say &mdash; has nothing "
             "for a memo to save, which is why divide and conquer is not this."),
            ("A memo turns the tree into the graph it always was",
             "Writing each answer down the first time makes every later request for the same "
             "argument a lookup. The measured calls fall from 22 089 to 50, and 50 is not "
             "mysterious: the memo holds eighteen entries and each is computed once from at "
             "most three sub-calls. The panel prints the ratio as the exact fraction "
             "`22089/50`, because a decimal there would be a number that is merely close."),
            ("The table is the same computation with the recursion removed",
             "Filling bottom-up visits every (denomination, amount) pair in a fixed order, "
             "which is 76 cells for three denominations and an amount of eighteen, and it "
             "never calls itself. It does strictly more work than the memo &mdash; 76 cells "
             "against 18 memo entries &mdash; because it computes answers the recursion never "
             "asked for. What it buys is a fixed order, which is the subject of the next "
             "lesson and the thing that can be got wrong."),
        ],
        "read_title": "Why the same recursion costs three different amounts",
        "read_intro": "Overlapping subproblems defined, the call counts measured, the arithmetic that predicts them, and the bound none of the counts establishes.",
        "body": [
            ("def", ("Overlapping subproblems",
                     "A recursive formulation has <strong>overlapping subproblems</strong> "
                     "when the set of distinct arguments it is ever called with is much "
                     "smaller than the number of calls it makes. The two numbers are both "
                     "countable by running it, and their ratio is what a memo can save.")),
            ("p", "This is the second of the two properties a dynamic program needs, and it is "
                  "the one about cost rather than about correctness. Optimal substructure says "
                  "the recurrence is right. Overlapping subproblems says evaluating it "
                  "naively is wasteful and that there is a specific, countable amount of waste "
                  "to remove. A problem with the first and not the second is a divide-and-"
                  "conquer problem, and a memo on it stores entries nothing ever reads."),
            ("example", ("Eighteen from 1, 2 and 5, counted three ways",
                         "The lab loads this instance. The memo-free recursion answers 5 after "
                         "22 089 calls. The same recursion with a memo answers 5 after 50 "
                         "calls, and reports that it stored eighteen distinct subproblems. The "
                         "table answers 5 after filling 76 cells and making 106 reads, with no "
                         "recursion at all. Three routes, one answer, three costs a factor of "
                         "hundreds apart.")),
            ("p", "Fifty is worth deriving rather than accepting. The memoised function is "
                  "entered once per distinct argument that is genuinely computed &mdash; "
                  "eighteen of them, plus the base case &mdash; and each such call makes one "
                  "sub-call per denomination that fits. Every one of those sub-calls is itself "
                  "a call. So the total is one call to start with, plus one call for every "
                  "edge leaving a computed amount &mdash; and the amounts 1 through 18 have "
                  "out-degrees 1, then 2 three times, then 3 fourteen times, which is 49. "
                  "One and 49 is 50. Nothing about that figure is a property of the memo as "
                  "a technique; it is the size of the dependency graph."),
            ("h3", "The two numbers the panel separates, and why"),
            ("p", "The memo stores eighteen entries; the table fills 76 cells. Those count "
                  "different things. The memo's key is the remaining amount alone, because the "
                  "recursion may use any denomination at any step; the table's cell is a "
                  "(denomination-prefix, amount) pair, because it is filled in an order and "
                  "each row makes one more denomination available. Four rows by nineteen "
                  "columns is 76. Both are correct formulations of the same problem with "
                  "different state, and the choice of state is the design decision this "
                  "course keeps returning to."),
            ("thm", ("The memoised recursion and the table compute the same function",
                     "For every amount `a` reachable from the coin set, the value the "
                     "memoised recursion returns for `a` equals the value in the table's last "
                     "row at column `a`, and both equal `f(a)`.")),
            ("proof", ("By strong induction on `a`. Both agree at `a = 0`, where each is 0. "
                       "Suppose both compute `f` correctly at every amount below `a`. The "
                       "memoised recursion evaluates `1 + min of f(a − c)` over the "
                       "denominations that fit, using stored values that are correct by "
                       "hypothesis, so it returns `f(a)` by the theorem of the previous "
                       "lesson.",
                       "The table's last row at column `a` takes the minimum over the same set "
                       "of options, reached as a row of cells rather than as a set of calls: "
                       "the cell for denomination prefix `i` and amount `a` is the better of "
                       "the cell above it and one more than the cell `c` columns to its left "
                       "in its own row. Unfolding that row from left to right gives exactly "
                       "the same minimum. Both therefore equal `f(a)`, and the memo's smaller "
                       "entry count is a difference of state, not of answer.")),
            ("h3", "What 441.8 times fewer does and does not say"),
            ("p", "The panel prints `22089/50` and its decimal to one place, and the exact "
                  "fraction is there because the ratio is a count divided by a count and "
                  "rounding it would misrepresent two integers as one estimate. It is a "
                  "measurement on one amount with one coin system. The proved statement is "
                  "different in kind: the table is `Θ(nk)` for `n` denominations and amount "
                  "`k`, and the memo-free recursion's call count grows exponentially in `k` "
                  "because the recursion tree branches at least twice at every level whenever "
                  "two denominations fit."),
            ("p", "The two statements diverge in a way this page can show you. At an amount of "
                  "six with coins 1, 3 and 4 &mdash; the previous lesson's instance &mdash; "
                  "the memo-free recursion makes 24 calls and the table fills 28 cells, so the "
                  "exponential method is ahead. At eighteen with 1, 2 and 5 the same two "
                  "routes cost 22 089 and 76. Nothing changed about either bound between those "
                  "two runs. What changed is which side of the crossing the input sits on, and "
                  "no count on either side of it is a statement about the other."),
            ("p", "The plot beside the grid makes the shape visible: call counts against the "
                  "amount, on a logarithmic axis, with a dashed reference curve. It stops at "
                  "sixteen whatever the amount is set to, because the unmemoised arm is re-run "
                  "at every point on every redraw and plotting further would cost a few "
                  "million calls for a picture that has already made its point. The figure "
                  "above the plot is the full amount."),
        ],
        "lab": ("dpkit", {
            "mode": "memo",
            "preset": "canonical",
            "panel_title": "Set the coins and the amount, and watch the three counters",
            "panel_intro": "Three pieces of code, not three descriptions of one. The panel "
                           "checks that they agree on the answer before it reports what each "
                           "cost, and says so in red if they ever do not. Raising the amount "
                           "by one roughly doubles the leftmost number and adds four to the "
                           "rightmost.",
        }),
        "steps_title": "Deciding whether a memo is worth adding",
        "steps_intro": "Both inputs to that decision are countable before any code is rewritten.",
        "steps": [
            ("Count the distinct arguments the recursion can be called with",
             "Not the calls &mdash; the arguments. Here it is the remaining amount, so there "
             "are `k + 1` of them. If that count is comparable to the number of calls, there "
             "is nothing to save and a memo is overhead."),
            ("Count the calls, by running it",
             "Put a counter in the function and run it on the instance you have. The ratio of "
             "the two counts is the saving available, and it is a measurement on that input "
             "rather than a property of the problem."),
            ("Choose the state, and know what you have chosen",
             "The memo keys on the amount alone; the table keys on the amount and how many "
             "denominations are in play. Both are correct. The first has eighteen entries and "
             "the second has 76 cells, and that difference is a design decision you are making "
             "whether or not you notice it."),
            ("Check that the memoised and unmemoised answers agree before trusting either",
             "A memo keyed on too little state returns a stored answer to a different "
             "question, and it does so silently and quickly. The only cheap defence is to run "
             "both on a small instance and compare, which is what the panel does on every "
             "keystroke."),
        ],
        "worked": {
            "title": "Where 22 089 calls go, and where 50 of them go",
            "intro": [
                "The recursion is entered once per call, not once per distinct amount. Counting "
                "the top three levels of the unmemoised tree shows the duplication starting "
                "immediately.",
            ],
            "lines": [
                "f(18)  asks for  f(17)   f(16)   f(13)",
                "f(17)  asks for  f(16)   f(15)   f(12)",
                "f(16)  asks for  f(15)   f(14)   f(11)",
                "f(13)  asks for  f(12)   f(11)   f(8)",
                "",
                "f(16) has already been asked for twice at depth two,",
                "f(15) twice, f(12) twice, f(11) twice   -   and the tree",
                "is only three levels deep",
                "",
                "totals on the panel, for coins 1, 2, 5 and an amount of 18",
                "",
                "  no memo        22 089 calls",
                "  with a memo        50 calls,  18 distinct subproblems stored",
                "  the table          76 cells,  106 reads",
                "",
                "  ratio  22089/50  =  441.8 times fewer calls",
                "  answer         5  from all three routes:  5 + 5 + 5 + 2 + 1",
            ],
            "after": [
                "The duplication is not an artefact of a badly written recursion. It is "
                "structural: the argument is one number, so any two paths down the tree that "
                "have spent the same total reach the same subproblem, and there are many such "
                "pairs. A memo is the observation that the tree was a directed acyclic graph "
                "with eighteen interior nodes all along.",
                "The reconstruction on the panel is a separate claim and is checked "
                "separately: the coins it reports are re-added, and the count of them is "
                "compared with the answer. `5 + 5 + 5 + 2 + 1` is five coins adding to "
                "eighteen, and the panel says so rather than asserting that a reconstruction "
                "walked back correctly. Two lessons from here that check becomes the whole "
                "point of a page.",
                "For a faded rehearsal, set the coins to 4 and 7 and the amount to 17. The "
                "supplied first move: 17 is odd and 4 is even, so any solution uses an odd "
                "number of 7s, which means one or three of them, leaving 10 or a negative "
                "amount. Decide what the panel will print before you look, and note that the "
                "answer is a result and not an error.",
            ],
        },
        "quiz_title": "Calls, entries, cells, and what each one counts",
        "quiz": [
            {"q": "The memo holds eighteen entries and the table fills 76 cells for the same instance. What accounts for the difference?",
             "a": ["The table is a less efficient formulation of the same computation",
                   "The two use different state: the memo keys on the amount, the table on the amount and how many denominations are in play",
                   "The table stores the reconstruction as well as the value",
                   "The memo skips amounts that cannot be made"],
             "c": 1,
             "why": "Four rows by nineteen columns is 76, and the rows are the denomination "
                    "prefixes. Both formulations are correct; they differ in what a "
                    "subproblem is taken to be. The table does not store the reconstruction "
                    "separately &mdash; it records which cell each cell came from &mdash; and "
                    "the memo stores unreachable amounts too, as the 4-and-7 instance shows."},
            {"q": "A recursion is called 22 089 times with 18 distinct arguments. What does adding a memo change about the answer?",
             "a": ["Nothing: the answer is the same and only the cost changes",
                   "It becomes exact, where the unmemoised version was approximate",
                   "It becomes correct for larger amounts, where the unmemoised version overflows",
                   "It becomes the optimum rather than a local optimum"],
             "c": 0,
             "why": "A memo is a cache on a pure function of its argument. The panel checks "
                    "this on every redraw rather than assuming it, and prints a red verdict if "
                    "the three routes ever disagree. Neither version is approximate, neither "
                    "overflows at these sizes, and neither is a local search."},
            {"q": "Which of these recursive formulations has nothing for a memo to save?",
             "a": ["The fewest coins for an amount, over a fixed coin set",
                   "The edit distance between two strings, on prefixes of each",
                   "Merge sort on an array, recursing on the two halves",
                   "The fewest coins, where the recursion may use any denomination at any step"],
             "c": 2,
             "why": "Merge sort's recursive calls all have distinct arguments &mdash; the "
                    "subarrays are disjoint &mdash; so no argument is ever repeated and a memo "
                    "would store entries nothing reads. That is what makes it divide and "
                    "conquer rather than dynamic programming. The other three all revisit "
                    "arguments; the first and fourth are the same formulation described twice."},
        ],
        "mistakes": [
            ("Calling the memo an optimisation and stopping there",
             "It is an optimisation, and describing it that way hides the number that makes it "
             "work. The saving is the ratio of calls to distinct arguments, and both are "
             "countable in advance. A reader who cannot say roughly what a memo will save "
             "before adding one cannot tell the case where it saves nothing."),
            ("Keying the memo on too little state",
             "The memo here keys on the remaining amount because nothing else affects the "
             "answer. Add a constraint &mdash; at most two of each coin, say &mdash; and the "
             "amount alone is no longer enough, but the code still runs and still returns "
             "quickly. It returns a stored answer to a different question, and only comparing "
             "it with an unmemoised run on a small input will tell you."),
            ("Reading `22089/50` as a property of memoisation",
             "It is one instance. Change the amount to six and the ratio is `18/7`; change the "
             "coin system and it moves again. The exact fraction is printed because the ratio "
             "is two integers, not because the number generalises."),
        ],
        "standard": ("Finish when you can predict a memo's saving from two counts before you add it.",
                     "You should be able to count the distinct arguments a recursion can take, "
                     "count its calls by running it, explain the gap between the memo's entries "
                     "and the table's cells as a choice of state, and name a recursion for "
                     "which a memo would be pure overhead."),
        "note": ("Both routes so far have let the recursion decide what order to compute things "
                 "in. The table does not: an order is chosen in advance, and the next lesson is "
                 "about a table that finishes, prints a number, and is wrong because that order "
                 "was chosen badly."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-fill-order-is-part-of-the-algorithm",
        "title": "The Fill Order Is Part of the Algorithm",
        "module": "A table, an order, a recurrence",
        "one_line": "Fill the matrix-chain table row by row instead of by interval length, and read the cheaper, wrong answer it finishes with.",
        "summary": (
            "A dynamic program is three things: a table, a recurrence, and an order to fill it "
            "in. The recurrence is the part nobody gets wrong. Fill the matrix-chain table by "
            "interval length and it reports 15 125 multiplications, which every one of the 42 "
            "bracketings confirms. Fill the same recurrence row by row and it reports 9 000. "
            "Nothing crashes, nothing is empty, and the smaller number is the wrong one."
        ),
        "key": [
            "cost(i, j) = min over k of  cost(i, k) + cost(k+1, j) + p(i)·p(k+1)·p(j+1)",
            "",
            "dimensions 30 35 15 5 10 20 25, which is six matrices",
            "  filled by interval length    15 125     and 42 bracketings agree",
            "  filled row by row             9 000     and 35 reads hit unwritten cells",
            "",
            "an unwritten cell reads as nothing, and nothing plus a number is a number",
        ],
        "key_label": "One recurrence, two orders, and the order that answers without crashing",
        "concepts_intro": (
            "The hard idea is that reading a cell too early is not an error condition. It is a "
            "silent substitution of zero, and the table finishes looking exactly like a table "
            "that worked."
        ),
        "concepts": [
            ("A cell covers an interval and reads two shorter ones",
             "The cell for the interval from `i` to `j` asks, for each split point `k` inside "
             "it, what the two halves cost and what joining them costs, and keeps the best. "
             "Both halves are strictly shorter intervals. So every cell depends on cells "
             "nearer the diagonal, and an order that reaches a cell before both of its halves "
             "exist is reading something that has not been computed."),
            ("An unwritten cell is not an error; it is a zero in disguise",
             "The table filler returns nothing for a cell that has not been written yet, and "
             "adding nothing to a number in this language gives the number. So a recurrence "
             "that reads too early does not raise, does not print a blank and does not leave a "
             "gap. It computes a smaller total from a missing half and stores it, and every "
             "cell that later reads <em>that</em> cell inherits the error without noticing."),
            ("The wrong order is cheaper-looking, which is what makes it dangerous",
             "Row-major reports 9 000 against the correct 15 125. A reader checking the "
             "arithmetic of one cell would find it consistent, and a reader who expected the "
             "optimum to be small would be encouraged. The only cheap defence is a second "
             "route: the lab enumerates all 42 bracketings and reports the smallest, and it is "
             "15 125. The order that is wrong is the one that disagrees with the enumeration."),
        ],
        "read_title": "The recurrence, the two orders, and the reads that land on nothing",
        "read_intro": "What the chain problem asks, why the order is forced, what happens when it is not respected, and the count that catches it.",
        "body": [
            ("def", ("The matrix-chain problem",
                     "A chain of `n` matrices is given by `n + 1` dimensions: "
                     "`p(0), p(1), …, p(n)`, where matrix `i` is `p(i−1)` by `p(i)`. "
                     "Multiplying a `p` by `q` matrix with a `q` by `r` matrix costs `p·q·r` "
                     "scalar multiplications. The problem is to choose the bracketing &mdash; "
                     "not the order of the matrices, which is fixed &mdash; that minimises the "
                     "total.")),
            ("p", "Seven numbers describe six matrices. The lab loads "
                  "`30 35 15 5 10 20 25`, so the first matrix is 30 by 35, the second is 35 by "
                  "15, and so on. The product is the same matrix whatever the bracketing, "
                  "because matrix multiplication is associative; only the cost of computing it "
                  "changes, and on this chain it changes by a factor of nearly four between "
                  "the best and worst bracketings."),
            ("thm", ("The chain recurrence",
                     "Let `cost(i, j)` be the fewest scalar multiplications needed to multiply "
                     "matrices `i` through `j`, with `cost(i, i) = 0`. Then for `i &lt; j`, "
                     "`cost(i, j)` is the minimum over split points `k` with `i ≤ k &lt; j` of "
                     "`cost(i, k) + cost(k+1, j) + p(i)·p(k+1)·p(j+1)`.")),
            ("proof", ("Any bracketing of matrices `i` through `j` has a last multiplication, "
                       "which joins a bracketed product of `i` through `k` with a bracketed "
                       "product of `k+1` through `j` for some `k`. Those two products have "
                       "dimensions determined by `i`, `k` and `j` alone, so the cost of the "
                       "join is `p(i)·p(k+1)·p(j+1)` whatever the two halves did internally.",
                       "If either half were bracketed more cheaply, substituting it in would "
                       "bracket the whole more cheaply, so each half of an optimal bracketing "
                       "is itself optimal &mdash; optimal substructure, discharged. Taking the "
                       "minimum over the `j − i` possible values of `k` therefore gives the "
                       "optimum, and the recurrence is exact.")),
            ("h3", "The order the recurrence forces, and the order a reader writes"),
            ("p", "`cost(i, j)` reads `cost(i, k)` and `cost(k+1, j)`, and both of those cover "
                  "shorter intervals than `i` to `j`. So the cells have to be filled in "
                  "increasing order of `j − i`: all the zero-length intervals, then all the "
                  "length-one intervals, and so on. That is a diagonal-by-diagonal sweep, and "
                  "it fills 21 cells of the 36 in a six-by-six table, because only the upper "
                  "triangle means anything."),
            ("p", "The order a reader writes, because it is the order every other table in "
                  "this course is filled in, is row by row. Row-major visits `(0,0)`, `(0,1)`, "
                  "`(0,2)` and so on across the whole first row before it has filled a single "
                  "cell of the second. But `(0,2)` needs `(1,2)`, which is in the second row. "
                  "It reads it anyway."),
            ("example", ("The cell where row-major goes wrong, in full",
                         "Correct: `cost(0,2) = min(cost(0,0) + cost(1,2) + 30·35·5, "
                         "cost(0,1) + cost(2,2) + 30·15·5)` = `min(0 + 2625 + 5250, "
                         "15750 + 0 + 2250)` = `7875`. Row-major: when it reaches `(0,2)`, the "
                         "cell `(1,2)` has not been written, so the first option evaluates to "
                         "`0 + 0 + 5250 = 5250`, which is smaller than 18 000, and 5250 is "
                         "stored. The table now contains a number that no bracketing of those "
                         "three matrices achieves.")),
            ("p", "The damage propagates. Every later cell that reads `(0,2)` reads 5250, and "
                  "the final answer in the corner comes out 9 000. Thirty-five reads over the "
                  "whole fill land on cells that have not been written, and the lab counts "
                  "them and paints them red. Fill by interval length and that count is zero."),
            ("h3", "Why the wrong table does more work and still finishes"),
            ("p", "Row-major writes all 36 cells; by-length writes 21. So the wrong order is "
                  "not a shortcut &mdash; it does more work, produces a fuller-looking table, "
                  "and reports a number two-fifths below the truth. Both orders make the same "
                  "70 reads, because the recurrence is the same recurrence; what differs is "
                  "whether the read finds anything."),
            ("p", "The measured counts here are 15 125 and 9 000 on one chain of six matrices, "
                  "and 42 bracketings agreeing with the first of them. The proved bound is a "
                  "different statement: the table has `Θ(n²)` meaningful cells and each takes "
                  "`O(n)` work, so filling it is `Θ(n³)`, against `Catalan(n−1)` bracketings "
                  "for the enumeration &mdash; 42 at six matrices, 132 at seven, 1 430 at "
                  "nine. The enumeration is the only reason we know 15 125 is right, and it is "
                  "also the thing that stops being runnable first."),
        ],
        "lab": ("dpkit", {
            "mode": "chain",
            "preset": "clrs",
            "panel_title": "Choose the dimensions and the order to fill in",
            "panel_intro": "Two drawings of the same table: the order you chose, and row by "
                           "row for comparison. Cells read before they were written are "
                           "painted red, and the count of them is on the panel. The "
                           "enumeration beside it has no table in it at all.",
        }),
        "steps_title": "Choosing a fill order, and proving you chose it correctly",
        "steps_intro": "The order is derived from the recurrence's reads, not from how the table looks on the page.",
        "steps": [
            ("Write down, for one cell, exactly which cells it reads",
             "Not the shape of the dependency &mdash; the list. For the chain it is "
             "`(i, k)` and `(k+1, j)` for every split `k`, which is two cells per split and "
             "`j − i` splits. The lab records that list from the reads the recurrence actually "
             "performed, so it can be compared with yours."),
            ("Find an order in which every cell's reads come earlier",
             "Sort the cells by whatever quantity the dependencies decrease: interval length "
             "here, remaining amount in the coin table, prefix length in the string tables. "
             "That quantity is the thing the recurrence recurses on, and the order is always "
             "increasing in it."),
            ("Run the order you rejected as well",
             "A wrong order produces a complete table and a plausible number, so the way to "
             "see it is to run it. The lab keeps both on screen; away from the lab, fill the "
             "table twice and compare the corners."),
            ("Check the corner against something with no table in it",
             "Enumerate every bracketing while the chain is short enough &mdash; 42 at six "
             "matrices, 132 at seven, 429 at eight, which is the cap. If the two disagree, the "
             "table is wrong and the order is the first thing to suspect."),
            ("Count the reads that landed on nothing",
             "Zero is the only acceptable number, and it is a check you can make once rather "
             "than a property you have to argue about. Any positive count means the order is "
             "wrong even if the answer happened to come out right."),
        ],
        "worked": {
            "title": "The same table, filled two ways",
            "intro": [
                "Rows and columns are matrices one to six; the cell in row i and column j is "
                "the cost of multiplying matrices i through j. Only the upper triangle carries "
                "meaning. The by-length fill leaves the lower triangle untouched; the row-major "
                "fill writes zeros into it and reads them.",
            ],
            "lines": [
                "by interval length, shortest first",
                "",
                "         A1     A2     A3     A4     A5     A6",
                "  A1      0  15750   7875   9375  11875  15125",
                "  A2      ·      0   2625   4375   7125  10500",
                "  A3      ·      ·      0    750   2500   5375",
                "  A4      ·      ·      ·      0   1000   3500",
                "  A5      ·      ·      ·      ·      0   5000",
                "  A6      ·      ·      ·      ·      ·      0",
                "",
                "row by row, left to right",
                "",
                "         A1     A2     A3     A4     A5     A6",
                "  A1      0  15750   5250   6750   8250   9000",
                "  A2      0      0   2625   4375   6125   7000",
                "  A3      0      0      0    750   1500   1875",
                "  A4      0      0      0      0   1000   1250",
                "  A5      0      0      0      0      0   5000",
                "  A6      0      0      0      0      0      0",
                "",
                "enumerating all 42 bracketings:   best 15125,   worst 58000",
                "the optimum is   ((A1(A2A3))((A4A5)A6))   and re-costing that",
                "tree from the dimensions alone gives 15125 again",
            ],
            "after": [
                "Compare the two tables cell by cell and the divergence starts at `(A1, A3)`: "
                "7875 against 5250. Everything to its left agrees, because those cells read "
                "only the diagonal, which both orders have already written. Everything to its "
                "right is contaminated, and the corner is 9 000 instead of 15 125.",
                "The second table's lower triangle is not empty, it is zeros, and those zeros "
                "are what the first row read. That is the mechanism in one sentence: the "
                "recurrence asked for a cell, the table had no value for it, and the "
                "arithmetic treated the absence as nothing rather than refusing. Any new "
                "recurrence written against this table filler has to know that, because a "
                "recurrence that reads too early will not tell you.",
                "For a faded rehearsal, switch the dimensions to `10 10 10 10 10` before you "
                "run it. The supplied first move: every matrix is 10 by 10, so every "
                "multiplication costs 1 000 and the total is three multiplications whatever "
                "the bracketing. Predict what by-length reports, predict what row-major "
                "reports, and check both &mdash; the answers are 3 000 and 1 000, and the "
                "enumeration of all five bracketings says the first.",
            ],
        },
        "quiz_title": "Orders, reads, and the number that looks better",
        "quiz": [
            {"q": "Filled row by row, the chain table reports 9 000 where the correct answer is 15 125. Why does it not crash or leave a blank?",
             "a": ["Because the recurrence catches the missing cell and substitutes a default",
                   "Because an unwritten cell reads as nothing, and nothing plus a number is that number",
                   "Because row-major happens to fill the cells in dependency order for this chain",
                   "Because the table is initialised to the correct values on the diagonal only"],
             "c": 1,
             "why": "The table filler returns nothing for a cell that is outside the table and "
                    "for one inside it that has not been written, and the arithmetic then "
                    "treats the absence as zero. Nothing catches it and nothing substitutes a "
                    "default. Row-major is definitely not in dependency order here: 35 reads "
                    "land on unwritten cells."},
            {"q": "Which fact tells you the by-length answer is the right one, rather than merely the larger one?",
             "a": ["It is larger, and an optimum over costs is a minimum, so the larger of two candidate minima is the safer one",
                   "It fills fewer cells, so it does less work",
                   "Enumerating all 42 bracketings and re-costing the best one gives 15 125",
                   "It makes zero reads on unwritten cells"],
             "c": 2,
             "why": "The enumeration has no table in it, so it cannot share the table's "
                    "mistake, and re-costing the reconstructed tree from the dimensions is a "
                    "third computation again. Zero early reads is good evidence and is the "
                    "right thing to check, but it is a statement about the fill rather than "
                    "about the answer; a recurrence can be wrong with a perfect order. Being "
                    "larger is not evidence of anything."},
            {"q": "How many cells does each order write, on six matrices?",
             "a": ["By length writes 21 and row-major writes 36: the wrong order does more work",
                   "By length writes 36 and row-major writes 21: the wrong order takes a shortcut",
                   "Both write 21; they differ only in the sequence",
                   "Both write 36; the lower triangle is meaningless in either"],
             "c": 0,
             "why": "By-length visits only the upper triangle, which is 21 cells of the 36; "
                    "row-major visits all of them and writes zeros below the diagonal. The "
                    "wrong order is not a shortcut. It produces a fuller table, a smaller "
                    "number, and more work, which is a combination worth remembering."},
            {"q": "A different chain is filled row by row and the corner happens to match the enumeration. What follows?",
             "a": ["The order is correct for that shape of table",
                   "Nothing about the order: it is one chain, and the early reads are still there to be counted",
                   "Row-major is correct whenever the dimensions are increasing",
                   "The recurrence must have been rewritten to read only leftward"],
             "c": 1,
             "why": "The lab's `10 100 5 50` instance is exactly this case: both orders report "
                    "7 500 and row-major still makes four reads on unwritten cells. An answer "
                    "that comes out right through a fill that reads nothing is a coincidence "
                    "of the numbers, and the count of early reads is what distinguishes it "
                    "from a correct fill."},
        ],
        "mistakes": [
            ("Treating the fill order as a presentation detail",
             "It is a third of the algorithm. The table and the recurrence are the parts a "
             "reader writes down and checks; the order is the part that is usually left "
             "implicit in the loop nesting, and it is the part this table gets wrong while "
             "looking finished. Write the order down beside the recurrence."),
            ("Expecting a wrong order to fail loudly",
             "It cannot. An unwritten cell reads as nothing, nothing behaves as zero in a sum, "
             "and a minimum over options one of which is spuriously small returns the spurious "
             "one. Every symptom of the bug &mdash; a complete table, a plausible number, "
             "consistent arithmetic within each cell &mdash; is a symptom of the code working."),
            ("Checking the recurrence and concluding the table is right",
             "The recurrence was right in both runs on this page. What differed was when the "
             "cells it names were available. A cell-by-cell audit of the arithmetic will pass "
             "on the row-major table, because each cell is a correct evaluation of the "
             "recurrence against the values that were there at the time."),
        ],
        "standard": ("Finish when you can derive the fill order from the recurrence's reads and prove it with a count.",
                     "You should be able to list the cells one cell reads, order the table by "
                     "the quantity the recurrence decreases, run the order you rejected, and "
                     "check the corner against an enumeration that has no table in it."),
        "note": ("The enumeration that settled this page is also the thing the table exists to "
                 "avoid, and the two cross: 42 bracketings at six matrices against 21 cells. "
                 "The next lesson runs both on seven matrices and reads the reconstruction back "
                 "out of the table as a bracketing rather than as a number."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "every-bracketing-and-the-one-the-table-found",
        "title": "Every Bracketing, and the One the Table Found",
        "module": "A table, an order, a recurrence",
        "one_line": "Enumerate all 132 bracketings of seven matrices, read the table's answer back as a tree, and re-cost that tree from the dimensions alone.",
        "summary": (
            "A table returns a number. A bracketing is an object, and getting the object back "
            "means following the split point each cell recorded. Those are two different "
            "claims and they are checked separately here: the number against every one of the "
            "132 bracketings of seven matrices, and the tree against the dimensions it was "
            "supposedly built from."
        ),
        "key": [
            "bracketings of n matrices = Catalan(n−1)",
            "  n = 4:    5        n = 6:   42        n = 8:   429",
            "  n = 5:   14        n = 7:  132        n = 9:  1430",
            "",
            "dimensions 5 10 3 12 5 50 6 4, seven matrices",
            "  the table                      2052       28 cells",
            "  all 132 bracketings, best      2052       worst 14060",
            "  the tree, re-costed            2052       ((A1A2)(((A3A4)(A5A6))A7))",
        ],
        "key_label": "Three computations of one number, and the object the third one needs",
        "concepts_intro": (
            "The hard idea is that a reconstruction is a separate claim from the value, and it "
            "fails in a way the value cannot: it can return a plausible object that costs "
            "something else entirely."
        ),
        "concepts": [
            ("The table stores a split point, and that is what the object is made of",
             "Each cell records not only its value but which `k` attained the minimum. Reading "
             "the answer back means starting at the whole interval, taking its split, and "
             "recursing on the two halves &mdash; which produces a binary tree over the "
             "matrices, and that tree printed with brackets is the bracketing. The value came "
             "from a minimum; the object comes from a pointer, and they can disagree."),
            ("Re-costing the object is a third computation, not a restatement",
             "Given the tree and the dimensions, the cost can be worked out from scratch: each "
             "internal node costs the product of three dimensions determined by the span of "
             "its two children, and the total is the sum over nodes. Nothing in that "
             "calculation looks at the table. When the table says 2052 and the re-costed tree "
             "says 2052, two independent computations have agreed."),
            ("The enumeration is the only route that is obviously right, and the first to die",
             "Listing every bracketing needs no recurrence and no order, so it cannot share a "
             "mistake with the table. It is also `Catalan(n−1)`, which is 132 at seven "
             "matrices, 429 at eight, and past a hundred million by nineteen. The lab refuses "
             "above eight. That is the shape of the whole subject: the check you trust most is "
             "the one you can least afford."),
        ],
        "read_title": "Counting the bracketings, and getting one of them back",
        "read_intro": "Where Catalan numbers come from here, how the reconstruction walks, what re-costing proves, and what the two counts say about each other.",
        "body": [
            ("def", ("A bracketing, as a binary tree",
                     "A <strong>bracketing</strong> of matrices `1` through `n` is a binary "
                     "tree whose leaves are the matrices in order and whose internal nodes are "
                     "multiplications. Its cost is the sum, over internal nodes, of "
                     "`p·q·r` where the left child spans dimensions `p` by `q` and the right "
                     "child `q` by `r`.")),
            ("thm", ("The number of bracketings",
                     "The number of bracketings of `n` matrices is the Catalan number "
                     "`C(n−1)`, where `C(0) = 1` and `C(m) = sum over i of C(i)·C(m−1−i)` for "
                     "`i` from 0 to `m−1`.")),
            ("proof", ("A bracketing of `n ≥ 2` matrices has a last multiplication, splitting "
                       "the chain after matrix `k` for some `k` from 1 to `n−1`. The left part "
                       "is a bracketing of `k` matrices and the right part a bracketing of "
                       "`n−k`, and the two are chosen independently, so the count for `n` is "
                       "the sum over `k` of the count for `k` times the count for `n−k`.",
                       "Writing `c(n)` for the count, that is "
                       "`c(n) = sum over k of c(k)·c(n−k)` with `c(1) = 1`, which is the "
                       "Catalan recurrence shifted by one. Hence `c(n) = C(n−1)`, giving 5 at "
                       "four matrices, 42 at six and 132 at seven &mdash; and the lab's "
                       "enumeration returns exactly those counts, because it is the same "
                       "recursion with the trees kept instead of counted.")),
            ("p", "The split in that proof is the same split the recurrence minimises over. "
                  "That is not a coincidence: the recurrence is the enumeration with the "
                  "sub-answers reused instead of rebuilt, which is what dynamic programming "
                  "is. The table's `Θ(n³)` and the enumeration's `Catalan(n−1)` are two costs "
                  "for the same search, differing only in whether the sub-results are stored."),
            ("h3", "Following the pointers back"),
            ("p", "The reconstruction starts at the cell covering the whole chain and reads "
                  "its recorded split `k`. That gives two intervals, `i` to `k` and `k+1` to "
                  "`j`, each of which has its own recorded split, and the recursion bottoms "
                  "out at single matrices. On the lab's seven-matrix chain the result is "
                  "`((A1A2)(((A3A4)(A5A6))A7))`, which is a bracketing of seven matrices in "
                  "the given order, as it has to be."),
            ("example", ("Two claims, checked separately",
                         "The table reports 2052 after filling 28 cells. The enumeration walks "
                         "all 132 bracketings with no table at all and reports a best of 2052 "
                         "and a worst of 14 060. The reconstruction returns the tree above, "
                         "and re-costing that tree from `5 10 3 12 5 50 6 4` gives 2052. Three "
                         "numbers, three routes, one answer &mdash; and the third route is the "
                         "only one that says anything about the tree.")),
            ("p", "Why insist on the third route? Because a reconstruction that follows the "
                  "wrong pointer returns a bracketing, not an error. It is still a binary tree "
                  "over the matrices in order; it is still printable; it still looks like an "
                  "answer. The only cheap way to catch it is to cost it independently and "
                  "compare with the number the table reported, which is what the panel's "
                  "re-cost row does."),
            ("h3", "What the two counts say about each other"),
            ("p", "On this chain the table fills 28 cells and the enumeration walks 132 "
                  "bracketings, so the table is ahead by a factor of about five. At four "
                  "matrices the table fills 10 cells against 5 bracketings and the table is "
                  "behind. The crossing is early here, which is why matrix chain is the "
                  "friendly case, and the next course on this path has a problem where the "
                  "crossing does not arrive until ten items."),
            ("p", "Both numbers on the panel are measured on the chain on screen. The proved "
                  "statements are `Θ(n³)` against `Catalan(n−1)`, and `Catalan` grows like "
                  "`4^n` over `n` to the three halves, so the ratio widens without bound. "
                  "Neither of those growth claims is established by the two counts, and the "
                  "counts are what tell you that on four matrices the asymptotically better "
                  "method is the slower one."),
            ("p", "One more thing the enumeration buys: the worst bracketing. On this chain it "
                  "costs 14 060 against the optimum's 2052, a factor of about 6.9. The table "
                  "cannot tell you that, because it only ever keeps minima, and a reader who "
                  "wants to know what the optimisation is worth has to ask the enumeration "
                  "while the enumeration is still affordable."),
        ],
        "lab": ("dpkit", {
            "mode": "chain",
            "preset": "long",
            "panel_title": "Seven matrices, and every way of bracketing them",
            "panel_intro": "The panel loads a seven-matrix chain, so the enumeration is 132 "
                           "bracketings and still instant. The reconstruction is printed as a "
                           "bracketing and re-costed from the dimensions, and those are two "
                           "separate rows because they are two separate claims.",
        }),
        "steps_title": "Getting an object back out of a table, and checking it",
        "steps_intro": "The value and the object are different claims, and the second one needs its own check.",
        "steps": [
            ("Record the choice, not just the value",
             "When a cell takes a minimum, store which option attained it. Without that the "
             "table answers what the optimum costs and cannot answer what it is, and "
             "recovering the choice afterwards means recomputing the minimum."),
            ("Walk the choices from the whole problem inward",
             "Start at the cell covering everything, follow its recorded choice into "
             "subproblems, and stop at the base cases. For the chain that walk is a binary "
             "tree; for a knapsack it is a path; the shape of the walk is the shape of the "
             "answer."),
            ("Re-cost the object from the input alone",
             "Compute what the returned object costs, using only the problem's data and not "
             "the table. This is the check that catches a reconstruction that followed a stale "
             "or wrong pointer, because such a reconstruction still returns a well-formed "
             "object."),
            ("Enumerate while you still can, and record the cap",
             "Every bracketing at six, seven and eight matrices is 42, 132 and 429, and the "
             "lab refuses above eight. Use the enumeration to establish the table on small "
             "instances, then rely on the table &mdash; and write down the size at which you "
             "stopped being able to check."),
        ],
        "worked": {
            "title": "Seven matrices, three routes, and the worst bracketing",
            "intro": [
                "The dimensions are 5 10 3 12 5 50 6 4, so the matrices are 5 by 10, 10 by 3, "
                "3 by 12, 12 by 5, 5 by 50, 50 by 6 and 6 by 4. The table is 7 by 7 and only "
                "the upper triangle carries meaning.",
            ],
            "lines": [
                "route                                  answer     what it cost",
                "",
                "the table, filled by interval length     2052     28 cells, 112 reads",
                "every bracketing, no table at all        2052     132 bracketings walked",
                "the reconstruction, re-costed            2052     one tree, 6 internal nodes",
                "",
                "the bracketing the table found",
                "",
                "  ((A1A2)(((A3A4)(A5A6))A7))",
                "",
                "re-costing it from the dimensions alone",
                "",
                "  A1A2          5 · 10 · 3   =    150",
                "  A3A4          3 · 12 · 5   =    180",
                "  A5A6          5 · 50 · 6   =   1500",
                "  (A3A4)(A5A6)  3 ·  5 · 6   =     90",
                "  ... A7        3 ·  6 · 4   =     72",
                "  (A1A2) ...    5 ·  3 · 4   =     60",
                "                              -------",
                "                                 2052",
                "",
                "the worst of the 132 bracketings costs 14060, which is 6.9 times the best",
            ],
            "after": [
                "Every line of the re-costing uses only the dimensions and the shape of the "
                "tree. No cell of the table appears in it. That is what makes the agreement "
                "worth something: if the reconstruction had followed a wrong split the tree "
                "would still be a tree, the six products would still be computable, and the "
                "total would have come out as something other than 2052.",
                "The gap between 2052 and 14 060 is what the optimisation is worth on this "
                "chain, and it is knowable only by enumeration. Switch the dimensions to "
                "`10 100 5 50` and the same gap is 7 500 against 75 000, exactly ten times, on "
                "four matrices and two bracketings. Switch to `10 10 10 10 10` and the gap "
                "vanishes: every bracketing costs 3 000, so the optimum is unique in value and "
                "not in shape, and the split the table records is one arbitrary choice among "
                "five.",
                "For a faded rehearsal, predict the number of bracketings for eight matrices "
                "before you change the dimensions. The supplied first move: the counts so far "
                "are 1, 2, 5, 14, 42, 132 for one through seven matrices, and each is the sum "
                "of products of earlier pairs. Work out the next one, then add a dimension and "
                "read the panel &mdash; and note that one more matrix after that is refused.",
            ],
        },
        "quiz_title": "Objects, values, and the enumeration that checks both",
        "quiz": [
            {"q": "Why is the reconstructed bracketing re-costed from the dimensions rather than compared with the table's number directly?",
             "a": ["Because the table's number may be stale after the reconstruction runs",
                   "Because a reconstruction that follows a wrong pointer still returns a well-formed bracketing, and only an independent cost catches that",
                   "Because the re-cost is faster than reading the corner cell",
                   "Because the table stores costs in a different unit from the re-cost"],
             "c": 1,
             "why": "The failure mode of a reconstruction is a plausible wrong object, not an "
                    "error. Re-costing uses only the dimensions and the tree, so it shares no "
                    "state with the table and can disagree with it. Nothing about the table "
                    "goes stale, the re-cost is not a performance measure, and both are counts "
                    "of scalar multiplications."},
            {"q": "Seven matrices have 132 bracketings and the table fills 28 cells. At four matrices the figures are 5 and 10. What does the pair of comparisons show?",
             "a": ["That the table is only worth using above six matrices",
                   "That the enumeration has the better growth rate below the crossing",
                   "That the two methods cross, and a count at one size does not order two growth rates",
                   "That Catalan numbers grow polynomially up to four and exponentially after"],
             "c": 2,
             "why": "The crossing is a fact about these two instances; the growth rates are "
                    "`Θ(n³)` and `Catalan(n−1)`, and neither changes at four matrices. Growth "
                    "rates are not something an instance can have. Where the useful threshold "
                    "lies depends on constants this page does not measure."},
            {"q": "On the dimensions `10 10 10 10 10` every bracketing costs 3 000. What does the split point the table records mean there?",
             "a": ["It is one arbitrary choice among five equally good ones",
                   "It is still the unique optimum, since the table takes a strict minimum",
                   "It is undefined, and the reconstruction returns nothing",
                   "It is the split that minimises the depth of the tree"],
             "c": 0,
             "why": "When every option ties, the cell keeps whichever the comparison reached "
                    "first, and that is a tie-break rather than a property of the problem. The "
                    "optimum is unique in value and not in shape. The reconstruction still "
                    "returns a perfectly good bracketing, and re-costing it still gives 3 000."},
        ],
        "mistakes": [
            ("Treating the value and the object as one answer",
             "The corner cell is a number and the bracketing is a tree, and a table can be "
             "right about the first while the walk back is wrong about the second. They are "
             "printed as separate rows on the panel for that reason, with a third row for the "
             "re-cost, and a reader who merges them has removed the only check on the walk."),
            ("Relying on an enumeration you cannot run at the size you care about",
             "132 bracketings is instant, 429 is fine, and the lab refuses nine matrices. "
             "Every claim this page makes about the table's correctness was established at a "
             "size where the enumeration still ran. Extending those claims to a fifty-matrix "
             "chain is an argument from the recurrence's proof, not from the check."),
            ("Reading the optimum's value as the value of optimising",
             "2052 is what the best bracketing costs. What the optimisation is <em>worth</em> "
             "is 14 060 minus 2052, and the table cannot tell you either term of that "
             "subtraction except the first. On a chain where every bracketing costs the same "
             "the optimisation is worth nothing, and only the enumeration says so."),
        ],
        "standard": ("Finish when you can return an object from a table and check it without the table.",
                     "You should be able to store the choice a cell made, walk it back into an "
                     "object, re-cost that object from the problem's data alone, and say at "
                     "what size the exhaustive check you were relying on stops running."),
        "note": ("Both tables so far have been square and indexed by the problem's own "
                 "structure. The next lesson moves to a grid whose two axes are different kinds "
                 "of thing &mdash; which item, and how much room is left &mdash; and where the "
                 "bound that looks polynomial is not."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-knapsack-table-and-what-each-cell-reads",
        "title": "The Knapsack Table, and What Each Cell Reads",
        "module": "Two axes, and reading the answer back",
        "one_line": "Fill the 0/1 knapsack grid, watch the two cells each cell reads, and re-weigh the items the reconstruction hands back.",
        "summary": (
            "The density rule that solved the fractional problem in Greedy Algorithms and "
            "Matroids gives 8 on the lab's four items where the optimum is 9. What replaces it "
            "is a grid indexed by which items are on offer and how much room is left, where "
            "each cell asks one yes-or-no question and reads exactly two cells in the row "
            "above. The items it hands back are then re-weighed against the capacity, because "
            "a wrong reconstruction returns a perfectly plausible list."
        ),
        "key": [
            "V(i, w) = max( V(i−1, w),  value(i) + V(i−1, w − weight(i)) )",
            "            skip item i          take it, if it fits",
            "",
            "items 1/1, 3/4, 4/5, 5/7 and a capacity of 7",
            "  densest first    D then A         weight 6     value 8",
            "  the table        B and C          weight 7     value 9",
            "",
            "40 cells, and every cell reads exactly two",
        ],
        "key_label": "One cell, one question, two reads - and the rule that gets it wrong",
        "concepts_intro": (
            "The hard idea is the choice of state: two axes, one of which is a number from the "
            "input rather than a count of anything, and that is where the bound stops being "
            "what it looks like."
        ),
        "concepts": [
            ("A cell asks one yes-or-no question about one item",
             "`V(i, w)` is the best value obtainable from the first `i` items within capacity "
             "`w`. Item `i` is either in the answer or not. If it is not, the value is "
             "`V(i−1, w)`. If it is, the value is its own value plus `V(i−1, w − weight(i))`, "
             "which is only available if the item fits. The cell takes the larger, and that is "
             "the entire recurrence: two cells in the row above, no search."),
            ("The two axes are different kinds of thing",
             "The rows count items, so there are `n + 1` of them and that is a count of the "
             "input's parts. The columns are capacities from 0 to `W`, so there are `W + 1` of "
             "them and that is a <em>value</em> from the input, not a count of anything. The "
             "grid is `(n+1)(W+1)` cells &mdash; 40 here &mdash; and doubling the capacity "
             "doubles the work while adding one digit to the input."),
            ("The reconstruction is a walk, and it can return a plausible lie",
             "An item was taken exactly where the walk's row drops by one <em>and</em> its "
             "column moves. Follow those and you get a set of items; the set is well-formed "
             "whether or not the walk was right. So the panel re-weighs it against the "
             "capacity and re-values it against the number the table reported, and prints both "
             "&mdash; a list that fits and adds to the claimed value is a checked answer, and "
             "a list that merely exists is not."),
        ],
        "read_title": "The grid, the recurrence, the walk back, and the bound that is not polynomial",
        "read_intro": "Why the greedy rule fails here, what the cell reads, how the items come back, and what pseudo-polynomial means.",
        "body": [
            ("def", ("The 0/1 knapsack problem",
                     "Given `n` items with integer weights and values and an integer capacity "
                     "`W`, choose a subset whose total weight is at most `W` and whose total "
                     "value is as large as possible. Each item is taken whole or not at all "
                     "&mdash; that is the 0/1 &mdash; and it is the whole difference from the "
                     "fractional problem.")),
            ("p", "Greedy Algorithms and Matroids solves the fractional version by value "
                  "density: sort by value over weight, take greedily, and cut the last item to "
                  "fit. The exchange argument works because the last item can be cut. Remove "
                  "that and the argument has nothing to exchange with, and the rule stops "
                  "being optimal."),
            ("example", ("Four items, capacity seven, and the rule that gets 8",
                         "The items are `1/1`, `3/4`, `4/5` and `5/7`, written weight over "
                         "value, with densities 1, 1.33, 1.25 and 1.4. Densest first takes "
                         "`5/7`, leaving room for 2, which admits only `1/1`: total weight 6, "
                         "value 8. Heaviest first takes the same two. The table reports 9, "
                         "taking `3/4` and `4/5` for a total weight of exactly 7, and the "
                         "panel re-weighs that pair and confirms both numbers.")),
            ("thm", ("The knapsack recurrence",
                     "Let `V(i, w)` be the greatest value obtainable from the first `i` items "
                     "with capacity `w`, with `V(0, w) = 0` for every `w`. Then for `i ≥ 1`, "
                     "`V(i, w) = V(i−1, w)` when `weight(i) &gt; w`, and otherwise "
                     "`V(i, w) = max( V(i−1, w), value(i) + V(i−1, w − weight(i)) )`.")),
            ("proof", ("Consider an optimal subset `S` of the first `i` items within capacity "
                       "`w`. Either item `i` is in `S` or it is not. If it is not, `S` is a "
                       "subset of the first `i−1` items within capacity `w`, and it must be an "
                       "optimal one, so its value is `V(i−1, w)`.",
                       "If item `i` is in `S`, then `S` without it is a subset of the first "
                       "`i−1` items within capacity `w − weight(i)`, and again it must be "
                       "optimal there &mdash; a better subset could be substituted in, keeping "
                       "item `i`, and would beat `S`. So its value is "
                       "`value(i) + V(i−1, w − weight(i))`. The optimum is the larger of the "
                       "two cases, which is the recurrence.")),
            ("h3", "What the painting shows, and why it cannot be wrong"),
            ("p", "Move the two range controls and the lab paints the chosen cell in one "
                  "colour and the cells it read in another. For the cell at row 3, column 7 "
                  "those are `(2, 7)` and `(2, 3)` &mdash; skip the third item, or take it and "
                  "look back four columns. That list is not a description of the recurrence "
                  "written out beside it. It is collected by the reads the recurrence itself "
                  "performed while the cell was being computed, so it records what the code "
                  "did rather than what its author believed."),
            ("p", "Every cell here reads exactly two, which is what makes the grid `Θ(nW)` "
                  "work rather than `Θ(nW)` cells times something. Compare with the chain "
                  "table, where a cell reads two per split point and the total is `Θ(n³)`; the "
                  "number of reads per cell is a property of the recurrence and is worth "
                  "reading off the painting rather than assumed."),
            ("h3", "Pseudo-polynomial, and why the bound is not what it looks like"),
            ("def", ("Pseudo-polynomial",
                     "An algorithm is <strong>pseudo-polynomial</strong> when its running time "
                     "is polynomial in the numeric <em>value</em> of the input rather than in "
                     "the length of the input's encoding. The knapsack table is `Θ(nW)`, which "
                     "is polynomial in `W`; but `W` written down takes about `log W` digits, "
                     "so the table is exponential in the input's size.")),
            ("p", "This matters and it is easy to miss, because `Θ(nW)` reads like a "
                  "polynomial bound and behaves like one on the instances a lab can show you. "
                  "Forty cells for four items at a capacity of seven; five hundred for the "
                  "same four items at a capacity of ninety-nine; five hundred thousand at a "
                  "capacity of ninety-nine thousand nine hundred and ninety-nine. Three more "
                  "digits in the input, a thousand times the work. Intractability and "
                  "Approximation returns to this as the "
                  "definition of weak NP-hardness, and the table on this page is the reason "
                  "that distinction exists."),
            ("p", "The measured figures here are 40 cells and 51 reads on four items at "
                  "capacity seven, with every one of the 16 subsets enumerated as a check. The "
                  "proved statement is `Θ(nW)` cells with `O(1)` work each, against `Θ(2ⁿ)` "
                  "for the enumeration. On this instance the enumeration walks 16 subsets "
                  "where the table fills 40 cells, so the exponential route is again ahead "
                  "&mdash; and it stays ahead until the item count and the capacity are both "
                  "large enough for `nW` to fall below `2ⁿ`, which on the lab's own presets "
                  "never happens."),
        ],
        "lab": ("dpkit", {
            "mode": "knapsack",
            "preset": "small",
            "panel_title": "Choose the items and the capacity, then explain one cell",
            "panel_intro": "Items are written weight over value, so `3/4` weighs 3 and is "
                           "worth 4. The two range controls pick a cell; the panel paints what "
                           "that cell read, re-weighs the reconstruction against the capacity, "
                           "and compares the table's number with every subset.",
        }),
        "steps_title": "Filling a two-axis table and checking what comes out",
        "steps_intro": "The grid is easy; the two things worth doing carefully are choosing the state and checking the walk.",
        "steps": [
            ("Say what a cell means in one sentence before filling any",
             "Here: the best value from the first `i` items within capacity `w`. If the "
             "sentence needs an `and` and a `but`, the state is probably wrong, and a wrong "
             "state produces a table that fills cleanly and answers a different question."),
            ("Split on the last item, in or out",
             "Every 0/1 recurrence on this course has this shape. The two branches are "
             "`V(i−1, w)` and `value(i) + V(i−1, w − weight(i))`, and the second exists only "
             "when the item fits. Write the fit condition down; forgetting it is how a "
             "negative column index becomes a silent zero."),
            ("Read the answer back by watching the row and the column together",
             "An item was taken where the row drops and the column moves; the row dropping "
             "alone means the item was skipped. Those two conditions are the whole "
             "reconstruction, and confusing them returns a set that is the right size and the "
             "wrong contents."),
            ("Re-weigh and re-value whatever comes back",
             "Add the weights and compare with the capacity; add the values and compare with "
             "the table's number. Both, not one &mdash; a set can fit and be worth less, or be "
             "worth the right amount and not fit, and the panel prints a red verdict for "
             "either."),
            ("Ask whether the capacity is a count or a magnitude",
             "If the answer is a magnitude, the table is pseudo-polynomial and doubling the "
             "capacity doubles the work for one extra digit of input. That is a fact about the "
             "state you chose, and it is worth knowing before the instance arrives rather "
             "than after."),
        ],
        "worked": {
            "title": "Four items, capacity seven, and the two cells the corner reads",
            "intro": [
                "Rows are item prefixes, columns are capacities from 0 to 7. Item A is 1/1, B "
                "is 3/4, C is 4/5, D is 5/7, each written weight over value.",
            ],
            "lines": [
                "capacity        0   1   2   3   4   5   6   7",
                "",
                "no items        0   0   0   0   0   0   0   0",
                "A  1/1          0   1   1   1   1   1   1   1",
                "B  3/4          0   1   1   4   5   5   5   5",
                "C  4/5          0   1   1   4   5   6   6   9",
                "D  5/7          0   1   1   4   5   7   8   9",
                "",
                "the corner, row D column 7, read exactly two cells:",
                "  skip D   ->   row C, column 7      =   9",
                "  take D   ->   row C, column 2  + 7 =   1 + 7  =  8",
                "  the larger is 9, so D is skipped and the pointer goes up",
                "",
                "the walk back:   D skipped, C taken, B taken, A skipped",
                "the set:         B and C,  weight 3 + 4 = 7,  value 4 + 5 = 9",
                "",
                "densest first would have taken D then A:  weight 6, value 8",
            ],
            "after": [
                "The last row is where the greedy instinct is refuted in one line. Item D has "
                "the highest density and the largest value, and the corner cell declines it, "
                "because taking it leaves capacity 2 and the best thing that fits in 2 is "
                "worth 1. Density is a rate and the capacity is finite; the rule that works "
                "when the last item can be cut does not survive the item being indivisible.",
                "The walk back reads the row and the column together. From `(D, 7)` the "
                "pointer goes to `(C, 7)` &mdash; row drops, column stays, so D was skipped. "
                "From `(C, 7)` it goes to `(B, 3)` &mdash; row drops and column moves by 4, "
                "which is C's weight, so C was taken. Two more steps and the set is `B, C`, "
                "which the panel re-weighs to 7 and re-values to 9.",
                "For a faded rehearsal, switch to the three items `2/3, 2/3, 3/4` at capacity "
                "4 before running it. The supplied first move: the first two items together "
                "weigh exactly 4 and are worth 6, and the third alone is worth 4. Decide what "
                "the table reports, decide which set the walk returns, and check both &mdash; "
                "and notice that the two equal items give the same value at capacities 2 and "
                "3, where the tie-break picks one of them with no reason to prefer it.",
            ],
        },
        "quiz_title": "Cells, reads, walks, and the shape of the bound",
        "quiz": [
            {"q": "On the lab's four items the density rule returns 8 and the table returns 9. What has failed?",
             "a": ["Optimal substructure, which is why a table is needed",
                   "The greedy choice property: no optimum here starts with the densest item",
                   "The exchange argument, because the values are not integers",
                   "Nothing has failed; 8 and 9 are the fractional and integral optima, which differ by rounding"],
             "c": 1,
             "why": "Optimal substructure holds &mdash; it is exactly what the recurrence's "
                    "proof uses. What fails is that no optimal subset contains the densest "
                    "item, so a rule committing to it first cannot be completed to an optimum. "
                    "The values are integers, and 8 is not the fractional optimum either: "
                    "cutting is allowed there and gives more than 9."},
            {"q": "The cell at row 3, column 7 reads `(2, 7)` and `(2, 3)`. Where does that list come from?",
             "a": ["From the dependency pattern the kit's author wrote down beside the recurrence",
                   "From the reads the recurrence itself performed while that cell was computed",
                   "From the reconstruction, walked backwards from the corner",
                   "From the shape of the table, since every cell in a grid reads the two above it"],
             "c": 1,
             "why": "The table filler records what the recurrence's own lookups asked for, so "
                    "the painting cannot disagree with what the code did. It is not a "
                    "description and not a property of grids in general: the chain table's "
                    "cells read two per split point, and the coin table's cells read one from "
                    "above and one from their own row."},
            {"q": "The knapsack table is `Θ(nW)`. Why is that not a polynomial bound on the input size?",
             "a": ["Because `n` and `W` are multiplied rather than added",
                   "Because `W` is a value from the input, and writing it down takes about `log W` digits",
                   "Because the reconstruction adds another factor of `n`",
                   "Because the weights may be larger than `W`"],
             "c": 1,
             "why": "Input size is the length of the encoding. Adding one digit to the capacity "
                    "multiplies `W` by ten and the work with it, so the running time is "
                    "exponential in the number of digits. A product of two input measures is "
                    "perfectly polynomial when both are counts &mdash; the chain table is "
                    "`Θ(n³)` &mdash; and the reconstruction is `O(n)`."},
            {"q": "The reconstruction returns a set of items that fits inside the capacity. What still needs checking?",
             "a": ["Nothing: fitting is what the reconstruction is for",
                   "That the set is non-empty",
                   "That its total value equals the number the table reported",
                   "That no item appears in it twice"],
             "c": 2,
             "why": "A walk that follows the wrong pointer can return a set that fits and is "
                    "worth less than the optimum, and fitting alone will not catch it. The "
                    "panel re-weighs and re-values, and prints a red verdict if either "
                    "disagrees. An empty set is a legitimate answer when nothing fits, and "
                    "duplicates cannot arise because the walk drops a row each step."},
        ],
        "mistakes": [
            ("Carrying the density rule across from the fractional problem",
             "It is the same objective and the same constraint, and it is a different problem: "
             "the exchange argument that proves the rule optimal needs to cut the last item, "
             "and 0/1 does not allow it. The rule is not merely unproved here &mdash; it is "
             "refuted on four items, which is the smallest instance the lab ships."),
            ("Reading `Θ(nW)` as polynomial and stopping",
             "`n` is a count and `W` is a magnitude, and mixing them in a bound hides an "
             "exponential in the input's length. It is the difference between a table that "
             "scales with the problem and one that scales with the numbers written in it, and "
             "it is the reason Intractability and Approximation can call this problem both "
             "NP-hard and solvable by a table."),
            ("Accepting a reconstruction because it is well-formed",
             "The output of a wrong walk is a set of items, which fits inside the capacity as "
             "often as not, and looks exactly like the output of a right one. Re-weighing and "
             "re-valuing costs two additions per item and is the only thing on the panel that "
             "distinguishes them."),
        ],
        "standard": ("Finish when you can state what a cell means, name the two cells it reads, and check what the walk returns.",
                     "You should be able to write the in-or-out recurrence with its fit "
                     "condition, read the dependency painting as a record rather than a "
                     "diagram, re-weigh and re-value a reconstruction, and say why a bound "
                     "mixing a count with a magnitude is not polynomial in the input."),
        "note": ("The grid on this page holds a whole row that is read once and never again. "
                 "The next lesson throws the rest of it away, keeps one row, and finds that the "
                 "direction the single loop runs in changes which problem is being solved."),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "one-row-and-the-direction-of-the-loop",
        "title": "One Row, and the Direction of the Loop",
        "module": "Two axes, and reading the answer back",
        "one_line": "Collapse the knapsack grid to a single row and watch the loop direction decide whether each item may be taken once or any number of times.",
        "summary": (
            "Every cell of the knapsack grid reads only the row above it, so the rows below "
            "that one are dead weight and the table can be one row updated in place. Then the "
            "direction that row is swept in stops being a detail: backward, an item is taken "
            "at most once and the answer is 17; forward, the same three lines of code take "
            "items repeatedly and the answer is 19. Both are correct algorithms for different "
            "problems."
        ),
        "key": [
            "for each item:   for w = W down to weight(i):   row[w] = max(row[w], row[w − weight(i)] + value(i))",
            "for each item:   for w = weight(i) up to W:     row[w] = max(row[w], row[w − weight(i)] + value(i))",
            "",
            "items 2/3, 3/5, 5/9 and a capacity of 11",
            "  swept backward     17     each item at most once     the 0/1 answer",
            "  swept forward      19     items reusable             the unbounded answer",
            "",
            "one character of difference, two problems",
        ],
        "key_label": "The same three lines, run in two directions",
        "concepts_intro": (
            "The hard idea is that the loop direction encodes which row you are reading from, "
            "and the code never says which row it means."
        ),
        "concepts": [
            ("The grid's rows are read once, so only one is needed",
             "`V(i, w)` reads `V(i−1, w)` and `V(i−1, w − weight(i))`, both in the row "
             "immediately above. Nothing ever reads two rows up. So the whole table can be one "
             "array of `W + 1` numbers, overwritten once per item, and the space falls from "
             "`Θ(nW)` to `Θ(W)` with the same `Θ(nW)` time."),
            ("Swept backward, a cell reads the previous item's values",
             "Going from `W` down to the item's weight, the cell at `w` reads `w − weight(i)`, "
             "which is to its left and has not been touched yet in this pass. So it still "
             "holds the value from before this item was considered, which is exactly "
             "`V(i−1, ·)`. The item can therefore be used at most once, and the single row "
             "reproduces the grid exactly."),
            ("Swept forward, a cell reads this item's own updates",
             "Going upward, the cell at `w` reads `w − weight(i)`, which this same pass has "
             "already updated. That value may already include one copy of the current item, so "
             "adding another gives two, and the pass can stack as many copies as fit. The "
             "result is the unbounded knapsack, correctly solved &mdash; by code that differs "
             "from the 0/1 version only in which way the loop counts."),
        ],
        "read_title": "One array, two directions, and two different problems",
        "read_intro": "Why one row suffices, what each direction reads, the proof that backward is 0/1, and what the space saving costs.",
        "body": [
            ("p", "Look again at the recurrence. `V(i, w)` is the larger of `V(i−1, w)` and "
                  "`value(i) + V(i−1, w − weight(i))`. Both terms are in row `i−1`. Row `i−2` "
                  "is never mentioned, and once row `i` is complete row `i−1` is never read "
                  "again. A table whose rows are used once and discarded does not need to be "
                  "stored."),
            ("def", ("The one-row form",
                     "Keep an array `row[0..W]`, initialised to zero. For each item in turn, "
                     "update `row[w] = max(row[w], row[w − weight(i)] + value(i))` for every "
                     "`w` from `weight(i)` to `W`. The order in which those `w` are visited is "
                     "not specified by the recurrence and is the subject of this lesson.")),
            ("thm", ("Backward gives 0/1; forward gives unbounded",
                     "If the inner loop runs `w` from `W` downward, the array after item `i` "
                     "equals row `i` of the 0/1 grid. If it runs `w` upward, the array after "
                     "item `i` holds the best value obtainable from the first `i` items with "
                     "each usable any number of times.")),
            ("proof", ("Downward: when `w` is updated, the cell at `w − weight(i)` is strictly "
                       "to the left and, because the loop is descending, has not yet been "
                       "visited in this pass. It therefore still holds the value it had before "
                       "item `i` was considered, which by induction is `V(i−1, w − weight(i))`. "
                       "So the update computes exactly "
                       "`max(V(i−1, w), value(i) + V(i−1, w − weight(i)))`, which is the grid's "
                       "recurrence, and the array after the pass is row `i`.",
                       "Upward: the cell at `w − weight(i)` has already been visited this pass, "
                       "so it holds the best value using items `1..i` with item `i` allowed. "
                       "Adding one more copy of item `i` therefore extends a solution that may "
                       "already contain it, and by induction on `w` the array holds the "
                       "unbounded optimum over the first `i` items. Both statements are exact; "
                       "neither direction is an approximation of the other.")),
            ("example", ("Three items, capacity eleven, and the two rows in full",
                         "The items are `2/3`, `3/5` and `5/9`. Swept backward the array ends "
                         "`0 0 3 5 5 9 9 12 14 14 17 17`, so the answer is 17, which is all "
                         "three items at a total weight of 10. Swept forward it ends "
                         "`0 0 3 5 6 9 10 12 14 15 18 19`, so the answer is 19, which is two "
                         "copies of `3/5` and one of `5/9` at a total weight of exactly 11. "
                         "The grid, filled in full, also says 17, and every one of the eight "
                         "subsets says 17.")),
            ("h3", "Watching the first item make the difference"),
            ("p", "The clearest place to see it is after the first pass. Backward, item `2/3` "
                  "leaves the array `0 0 3 3 3 3 3 3 3 3 3 3`: one copy of a weight-2 item is "
                  "all that any capacity can hold, because the item appears once. Forward, the "
                  "same item leaves `0 0 3 3 6 6 9 9 12 12 15 15`: at capacity 4 it has been "
                  "taken twice, at capacity 6 three times, and the pass built each of those on "
                  "the value it had just written two columns earlier."),
            ("h3", "What the collapse costs"),
            ("p", "The reconstruction. The grid records, for each cell, which cell it came "
                  "from, and the walk back through those pointers is what produced the item "
                  "set on the previous page. One row has nowhere to keep them: by the time the "
                  "answer is known, every intermediate value has been overwritten. So the "
                  "one-row form answers what the optimum is and not what it consists of, and "
                  "the panel's one-row figures sit beside the grid's rather than replacing "
                  "them."),
            ("p", "That is the trade in one sentence: `Θ(W)` space instead of `Θ(nW)`, at the "
                  "cost of the object. Recovering the object from one row means either keeping "
                  "the rows after all, or running the whole thing again with a divide-and-"
                  "conquer trick that this course does not develop. Knowing which of the two "
                  "questions you are answering is the point."),
            ("p", "The measured figures are 17 and 19 on three items at capacity 11, with the "
                  "grid and the enumeration of all eight subsets both confirming 17. The "
                  "proved statement is that time is `Θ(nW)` in both forms and space falls from "
                  "`Θ(nW)` to `Θ(W)` &mdash; 48 cells against 12 numbers here, which at this "
                  "size is a saving of thirty-six words and no wall-clock time at all. The "
                  "space bound is what makes the collapse worth knowing; this instance is far "
                  "too small to show it, and saying so is more useful than a ratio measured on "
                  "twelve numbers."),
        ],
        "lab": ("dpkit", {
            "mode": "knapsack",
            "preset": "unbounded",
            "panel_title": "Three items, and a single row filled both ways",
            "panel_intro": "The lower drawing is the same problem in one row, swept backward "
                           "and forward. Both figures are on the panel beside the grid's, and "
                           "the backward one agrees with the grid while the forward one "
                           "answers a different question correctly.",
        }),
        "steps_title": "Collapsing a table safely",
        "steps_intro": "Three checks, and the first of them is the one that decides whether the collapse is available at all.",
        "steps": [
            ("Find the furthest row any cell reads",
             "If it is one, the table collapses to a single row. If cells read two rows back "
             "&mdash; some sequence recurrences do &mdash; keep two. If they read arbitrarily "
             "far back, as the chain recurrence does, the table does not collapse at all and "
             "trying it will produce exactly the silent failure of the fill-order lesson."),
            ("Derive the sweep direction from which values you need",
             "You need the previous row's value at `w − weight(i)`. Sweep away from the "
             "direction the reads come from, so that the cells you read are the ones you have "
             "not yet overwritten. For reads to the left, that means descending."),
            ("Run both directions and compare with the grid",
             "The wrong direction does not fail; it solves a different problem, correctly. The "
             "only cheap way to know which one you have written is to keep the full grid "
             "around on a small instance and compare, which is what the panel does."),
            ("Decide whether you need the object before you throw the rows away",
             "One row cannot be walked back. If the answer has to be a set of items rather "
             "than a number, the rows are not dead weight and the space saving is not "
             "available at this price."),
        ],
        "worked": {
            "title": "One row, three items, swept both ways",
            "intro": [
                "The array holds one number per capacity from 0 to 11 and starts as all zeros. "
                "Each line below is the whole array after one item has been processed. The "
                "items are A = 2/3, B = 3/5 and C = 5/9, written weight over value.",
            ],
            "lines": [
                "capacity        0   1   2   3   4   5   6   7   8   9  10  11",
                "",
                "swept backward, w from 11 down to the item's weight",
                "  after A       0   0   3   3   3   3   3   3   3   3   3   3",
                "  after B       0   0   3   5   5   8   8   8   8   8   8   8",
                "  after C       0   0   3   5   5   9   9  12  14  14  17  17",
                "",
                "swept forward, w from the item's weight up to 11",
                "  after A       0   0   3   3   6   6   9   9  12  12  15  15",
                "  after B       0   0   3   5   6   8  10  11  13  15  16  18",
                "  after C       0   0   3   5   6   9  10  12  14  15  18  19",
                "",
                "the full grid, all four rows, says                          17",
                "every one of the eight subsets says                         17",
                "the forward sweep says                                      19",
                "                                                            ",
                "19 is  3/5 twice and 5/9 once:  weight 11, value 19",
            ],
            "after": [
                "The first backward line is the tell. After item A the array is 3 at every "
                "capacity from 2 upward, because one copy of a weight-2 item is the most that "
                "can be in the answer. The first forward line climbs in steps of 3 every two "
                "columns, because each cell was built from a cell two to its left that this "
                "same pass had already improved.",
                "Both algorithms are correct. Neither is a bug in the other. If the problem "
                "says an item exists once, the backward sweep is the algorithm and the forward "
                "one silently answers a question nobody asked; if items are available in "
                "unlimited quantity, it is the other way round. The failure this page is about "
                "is not an incorrect answer but a correct answer to the wrong question, which "
                "is the hardest kind to notice in a number.",
                "For a faded rehearsal, keep the items and drop the capacity to 5 before "
                "running it. The supplied first move: at capacity 5 the backward answer must "
                "be one of `2/3 + 3/5`, `5/9` alone, or less, so it is 9 or less. Work out "
                "both sweeps by hand for the five columns, then check them &mdash; and note "
                "that the two agree at some capacities and not at others, which is why "
                "spot-checking one column proves nothing.",
            ],
        },
        "quiz_title": "Rows, directions, and which problem is being solved",
        "quiz": [
            {"q": "Why can the 0/1 knapsack grid be collapsed to a single row?",
             "a": ["Because the values in each row are non-decreasing",
                   "Because no cell ever reads a row more than one above itself",
                   "Because the capacity axis is longer than the item axis",
                   "Because the reconstruction only needs the last row"],
             "c": 1,
             "why": "`V(i, w)` reads `V(i−1, w)` and `V(i−1, w − weight(i))`, and nothing "
                    "reads further back, so a row is dead as soon as the next one is complete. "
                    "Monotonicity along a row is true but irrelevant, the axis lengths do not "
                    "matter, and the reconstruction is precisely what the collapse destroys."},
            {"q": "The forward sweep reports 19 where the grid reports 17. What is wrong with the forward sweep?",
             "a": ["It reads a cell before that cell has been written",
                   "It double-counts the capacity, so its answer exceeds the true optimum",
                   "Nothing: it correctly solves the unbounded problem, where items may be reused",
                   "It uses a strict inequality where the comparison should be non-strict"],
             "c": 2,
             "why": "19 is achievable: two copies of `3/5` and one of `5/9` weigh exactly 11 "
                    "and are worth 19. The sweep is a correct algorithm for a different "
                    "problem, and every cell it reads has been written &mdash; written by this "
                    "same pass, which is exactly what allows the reuse."},
            {"q": "You need the set of items, not just the best value. What does that rule out?",
             "a": ["The one-row form, because the intermediate values it would need are overwritten",
                   "The backward sweep, because it visits capacities in the wrong order for a walk",
                   "The grid, because it stores values rather than items",
                   "Nothing: the set can be recovered from the final row by subtracting weights"],
             "c": 0,
             "why": "The walk back needs to know, for each item, what the array looked like "
                    "before that item was processed, and one row keeps none of that. The grid "
                    "keeps it, which is why the previous lesson could return a set. Recovering "
                    "the set from a final row by subtracting weights is not reliable: several "
                    "different sets can produce the same final row."},
            {"q": "A sequence recurrence has cells that read two rows back. What follows for the collapse?",
             "a": ["It still collapses to one row, with the reads taken from the current pass",
                   "It collapses to two rows rather than one",
                   "It does not collapse, because the fill order would be violated",
                   "It collapses only if the sweep runs forward"],
             "c": 1,
             "why": "The rule is to keep as many rows as the furthest read reaches back, so "
                    "two reads back means two rows. Taking those reads from the current pass "
                    "would silently change the problem, as the forward sweep does. Recurrences "
                    "that read arbitrarily far back &mdash; the matrix chain, for one &mdash; "
                    "are the ones that do not collapse."},
        ],
        "mistakes": [
            ("Treating the sweep direction as a matter of taste",
             "It selects which row the reads come from, and the code never names a row at all. "
             "Both directions run, both terminate, both produce monotone plausible arrays, and "
             "they answer different questions. Write down, beside the loop, which row you "
             "intend each read to hit."),
            ("Calling the forward sweep a bug",
             "It is the unbounded knapsack, solved correctly and in one line less than the "
             "obvious formulation. The defect is only ever a mismatch between the sweep and "
             "the problem, which is why the panel prints both numbers rather than one number "
             "and a verdict."),
            ("Collapsing the table and then asking for the answer's contents",
             "The space saving and the reconstruction are alternatives at this price. A reader "
             "who collapses first and discovers the requirement second has to keep the rows "
             "after all, and the honest version of the trade is to ask which of the two "
             "questions is being answered before the rows are discarded."),
        ],
        "standard": ("Finish when you can collapse a table, choose the sweep direction from the reads, and say what the collapse cost.",
                     "You should be able to find the furthest row a recurrence reads, derive "
                     "the direction that keeps the reads on un-overwritten cells, recognise the "
                     "other direction as a correct algorithm for a different problem, and name "
                     "what one row cannot do."),
        "note": ("The two tables so far have been indexed by an item and a number. The next "
                 "lesson indexes by two prefixes at once, and the object it returns is not a set "
                 "but a program &mdash; a list of operations that is carried out, character by "
                 "character, on the string it claims to transform."),
    },
]
