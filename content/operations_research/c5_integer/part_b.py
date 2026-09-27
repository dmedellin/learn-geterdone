"""Course 5, lessons 06-09 - the three honest tools, and one hard problem.

Branch, then measure the gap the branching is closing, then cut it; and last a
problem where all three are needed at once. Every bound, node count, cut
coefficient and tour length below is read off the `integer` kit, which solves
each instance exactly.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "branch-and-bound",
        "title": "Branch and Bound",
        "module": "Search and bounds",
        "one_line": "Split on a fractional variable, bound each child, and close a node for one of exactly three reasons.",
        "summary": (
            "Solve the relaxation; if a variable comes back fractional, split the problem "
            "into two children that lose no whole-number plan and exclude the fractional "
            "point. Re-solve each child from its parent's final tableau, and close a node "
            "when it is infeasible, when its bound cannot beat the best plan in hand, or "
            "when its relaxation is already whole. What makes this a method rather than "
            "an enumeration is the bound, and the bound is a linear programme."
        ),
        "key": [
            "x_k fractional at v  →  children  x_k ≤ ⌊v⌋   and   x_k ≥ ⌈v⌉",
            "no whole plan is lost; the fractional optimum is in neither child",
            "close a node  infeasible | bound cannot beat the incumbent | already whole",
            "root 413/18 at (37/18, 19/6)      z_IP = 22 at (2, 3)",
            "depth first closes in 5 nodes;  best bound takes 7 on this instance",
            "on a binary  include/exclude  is  x ≤ 0  and  x ≥ 1 — the same tree",
        ],
        "key_label": "One split, three ways to close a node",
        "concepts_intro": (
            "One hard idea, and it is the correctness argument: the two children between "
            "them keep every whole-number plan the parent had, and neither keeps the "
            "fractional point that caused the split."
        ),
        "concepts": [
            ("A branch is a pair of inequalities, not a pair of assignments",
             "If `x₁` comes back at `37/18`, the children are `x₁ ≤ 2` and `x₁ ≥ 3`. The "
             "first still permits `x₁ = 0`; the second still permits `x₁ = 5`. Every "
             "whole value of `x₁` satisfies one of the two, and `37/18` satisfies "
             "neither &mdash; which is the entire reason the method is correct and the "
             "entire reason it makes progress."),
            ("A node's bound is a bound, so three reasons close it",
             "The bound says nothing inside that node beats this number. So a node closes "
             "when its relaxation is infeasible, when its bound cannot beat the best "
             "whole plan already in hand, or when its relaxation came back whole &mdash; "
             "in which case it is a new best plan. There is no fourth reason and no case "
             "in which a closed node needs revisiting."),
            ("The bound is a linear programme, and the child starts from the parent",
             "Adding `x₁ ≤ 2` to a solved tableau leaves it optimal and makes it "
             "infeasible, which is exactly the situation the dual simplex of “Duality and "
             "Sensitivity Analysis” was built for. Each child therefore costs a few "
             "pivots from its parent rather than a fresh solve, and the table in the lab "
             "names the method it used on every node."),
        ],
        "read_title": "The tree, and what closes a node",
        "read_intro": "Why the split loses nothing, what each of the three closing reasons proves, and where the bound comes from.",
        "body": [
            ("p", "Take `max 5x₁ + 4x₂` subject to `6x₁ + 4x₂ ≤ 25` machine hours and "
                  "`3x₁ + 5x₂ ≤ 22` inspection hours. The relaxation stops at "
                  "`(37/18, 19/6)`, worth `413/18`, which is about `22.94` and is not a "
                  "plan. Both coordinates are fractional, so there are two variables to "
                  "choose between and the method works either way."),
            ("def", ("Branching on a fractional variable",
                     "If the relaxation of a node returns `x_k = v` with `v` not an "
                     "integer, the node is replaced by two <strong>children</strong>: the "
                     "same problem with `x_k ≤ ⌊v⌋` added, and the same problem with "
                     "`x_k ≥ ⌈v⌉` added. The node itself is not solved again.")),
            ("thm", ("Branching loses no whole-number plan",
                     "Every integer point feasible for the parent is feasible for exactly "
                     "one of the two children, and the parent's fractional optimum is "
                     "feasible for neither.")),
            ("proof", ["Let `x` be feasible for the parent with `x_k` an integer. Then "
                       "either `x_k ≤ ⌊v⌋` or `x_k ≥ ⌊v⌋ + 1 = ⌈v⌉`, because there is no "
                       "integer strictly between `⌊v⌋` and `⌈v⌉` when `v` is not an "
                       "integer. So `x` satisfies one of the two added rows and every "
                       "other row unchanged.",
                       "The parent's optimum has `x_k = v` with `⌊v⌋ < v < ⌈v⌉`, so it "
                       "satisfies neither added row. Hence the union of the children "
                       "contains every whole-number plan of the parent and the two bounds "
                       "are computed on strictly smaller regions."]),
            ("p", "That is the whole correctness argument, and it is why the children are "
                  "inequalities. Fixing `x₁ = 2` in one child and `x₁ = 3` in the other "
                  "would lose every plan with `x₁ = 0` or `x₁ = 4`, and the search would "
                  "return a confident wrong answer."),
            ("h3", "Three reasons to close a node, and no others"),
            ("ul", ["<strong>Infeasible.</strong> The added rows have emptied the region. "
                    "There is nothing in it, so there is nothing to find.",
                    "<strong>Bounded out.</strong> The node's bound is no better than the "
                    "best whole plan already in hand. Nothing inside beats the bound, so "
                    "nothing inside beats the plan you have.",
                    "<strong>Integral.</strong> The relaxation came back whole. It is "
                    "feasible and it attains the node's bound, so it is the best plan in "
                    "that node &mdash; and if it beats the plan in hand it becomes the "
                    "new one."]),
            ("example", ("The five-node tree on this instance",
                         "Branch on `x₁` at `37/18`. Child `x₁ ≤ 2` bounds at `114/5` and "
                         "stops at `(2, 16/5)`, still fractional; child `x₁ ≥ 3` bounds at "
                         "`22` and stops at `(3, 7/4)`. Split the first on `x₂` at `16/5`: "
                         "`x₂ ≤ 3` comes back at `(2, 3)`, whole, worth `22`, and becomes "
                         "the plan in hand; `x₂ ≥ 4` bounds at `58/3`, about `19.33`, "
                         "which cannot beat `22`, so it closes. Now `x₁ ≥ 3` bounds at "
                         "exactly `22` and cannot beat `22` either, so it closes too. Five "
                         "nodes, no open nodes, answer `22` at `(2, 3)`.")),
            ("p", "Read the last two closures again, because they are the method. Neither "
                  "node was explored and neither needed to be: a bound of `58/3` is a "
                  "promise that nothing inside is worth more than `58/3`, and `22` is "
                  "already in hand. The tree did not decide those subtrees were "
                  "unpromising; it proved there was nothing in them."),
            ("p", "The search tree itself &mdash; explore, keep the best so far, prune any "
                  "branch whose optimistic bound cannot beat it, and accept that the bound's "
                  "quality is the whole algorithm &mdash; belongs to the Algorithms path's "
                  "&ldquo;Backtracking and Branch-and-Bound&rdquo;, which works it on a "
                  "six-item knapsack with the fractional bound. What is this course's own "
                  "is that the bound here is a linear programme, and that each child is "
                  "re-solved from its parent's final tableau by the dual simplex rather "
                  "than from scratch."),
            ("p", "One reconciliation worth stating once: on a binary variable the two "
                  "branching schemes are the same tree. “Include the item” and “exclude "
                  "the item” are `x ≥ 1` and `x ≤ 0`, which is exactly `x ≥ ⌈v⌉` and "
                  "`x ≤ ⌊v⌋` for any `v` strictly between `0` and `1`. The knapsack tree "
                  "of that lesson and the tree here are one method described in two "
                  "vocabularies."),
            ("p", "None of this is a complexity result. Pruning removes subtrees that "
                  "have been proved empty of better plans, and on a bad instance it "
                  "removes none of them: the worst case is still exponential, and that "
                  "fact is Algorithms&rsquo;. The practical consequence is visible in the "
                  "lab, where the order the nodes are taken in changes the work and never "
                  "the answer &mdash; depth first closes this instance in five nodes and "
                  "best bound takes seven, which is the opposite of the usual "
                  "expectation and is what measuring is for."),
        ],
        "lab": ("integer", {
            "mode": "bb",
            "preset": "mixed",
            "panel_title": "Grow the tree one node at a time",
            "panel_intro": "Every node is a linear programme and every child is re-solved "
                           "from its parent's final tableau by the dual simplex, which the "
                           "last column of the table names. Raise the node budget one step "
                           "at a time: below the budget that closes the tree, the panel "
                           "refuses to name an optimum.",
        }),
        "steps_title": "Running a tree by hand",
        "steps_intro": "Five steps, and the fourth is the one that turns a search into a proof.",
        "steps": [
            ("Solve the relaxation at the node you are at",
             "Exactly. Its value is that node's bound and its solution tells you whether "
             "there is anything to split. A whole solution here means this node is "
             "finished."),
            ("Pick a fractional variable and write the two children",
             "`x_k ≤ ⌊v⌋` and `x_k ≥ ⌈v⌉`, as inequalities added to the node's own rows. "
             "Which variable you pick changes the shape of the tree and not the answer, "
             "so pick one and record which."),
            ("Bound each child from its parent's tableau",
             "The added row makes the parent's optimal tableau infeasible without making "
             "it non-optimal, which is the dual simplex's case. A few pivots, not a fresh "
             "solve."),
            ("Close every node you can, and name the reason",
             "Infeasible, bounded out, or integral. Writing the reason next to the node is "
             "what makes the finished tree a proof: a reader can check each closure "
             "without re-solving anything."),
            ("Stop when no node is open, not when you are tired",
             "An open node is an unproved region. If you must stop early, report the best "
             "plan in hand together with the best bound over the open nodes &mdash; which "
             "is the next lesson, and is what the lab does when it hits its budget."),
        ],
        "worked": {
            "title": "max 5x₁ + 4x₂ on machine hours and inspection",
            "intro": [
                "One instance, taken depth first, branching on the first fractional "
                "variable. Every bound is exact and every closure names its reason.",
            ],
            "lines": [
                "max  5x₁ + 4x₂        6x₁ + 4x₂ ≤ 25     (machine hours)",
                "                      3x₁ + 5x₂ ≤ 22     (inspection)",
                "                      x₁, x₂ ≥ 0 and whole",
                "",
                "node 0  root            bound 413/18 ≈ 22.94   at (37/18, 19/6)",
                "        x₁ = 37/18 is fractional, so branch: x₁ ≤ 2 or x₁ ≥ 3",
                "",
                "node 1  x₁ ≤ 2          bound 114/5 = 22.8     at (2, 16/5)",
                "        still fractional in x₂, so branch again",
                "node 2  x₁ ≥ 3          bound 22               at (3, 7/4)",
                "",
                "node 3  x₁ ≤ 2, x₂ ≤ 3  bound 22               at (2, 3)   WHOLE",
                "        → plan in hand: 22 at (2, 3)",
                "node 4  x₁ ≤ 2, x₂ ≥ 4  bound 58/3 ≈ 19.33     at (2/3, 4)",
                "        58/3 < 22, so closed by the bound",
                "",
                "back to node 2:  bound 22, and 22 is already in hand",
                "        closed by the bound — nothing inside can beat it",
                "",
                "no open nodes.   z_IP = 22 at (2, 3), proved in 5 nodes",
                "",
                "same instance, best bound first:  7 nodes, same answer",
            ],
            "after": [
                "Node 2 is the interesting closure. Its bound is `22`, exactly equal to "
                "the plan in hand, and that is enough: nothing in a node beats the node's "
                "bound, so nothing there beats `22`. It might <em>tie</em> `22`, and there "
                "may well be a second optimal plan inside &mdash; the method finds an "
                "optimum, not all of them.",
                "Node 4 shows why a branch is an inequality. Its region has `x₂ ≥ 4`, "
                "which forces `x₁` down to `2/3`, and the bound collapses to `58/3`. Had "
                "the branch been the assignment `x₂ = 4` the effect would have looked the "
                "same here and would have been wrong elsewhere, because `x₂ ≥ 4` also "
                "contains `x₂ = 5`.",
                "For a faded rehearsal, run the same instance branching on the second "
                "variable first &mdash; the lab has a control for it. The supplied first "
                "move is that the root is unchanged, since the root does not depend on "
                "the branching rule: `x₂ = 19/6`, so the children are `x₂ ≤ 3` and "
                "`x₂ ≥ 4`. Predict the node count before you look, then say whether the "
                "answer moved.",
            ],
        },
        "quiz_title": "Branches, bounds and closures",
        "quiz": [
            {"q": "A relaxation returns `x₁ = 37/18`. What are the two children?",
             "a": ["`x₁ = 2` and `x₁ = 3`", "`x₁ ≤ 2` and `x₁ ≥ 3`",
                   "`x₁ ≤ 2` and `x₁ ≥ 2`", "`x₁ ≤ 37/18` and `x₁ ≥ 37/18`"],
             "c": 1,
             "why": "Inequalities, so that `x₁ = 0` and `x₁ = 5` are both still reachable. "
                    "Assignments would delete whole plans and the search would return a "
                    "wrong answer confidently. The third choice overlaps at `x₁ = 2` and "
                    "keeps the fractional point in neither child, so it also fails to "
                    "exclude it."},
            {"q": "A node's bound is `58/3` and the best whole plan in hand is worth `22`. What follows?",
             "a": ["The node should be explored, in case something inside beats `22`",
                   "The node can be closed: nothing inside beats `58/3`, and `58/3 < 22`",
                   "The node's bound must be recomputed, since a bound below the incumbent is impossible",
                   "The incumbent must be wrong"],
             "c": 1,
             "why": "A bound is a bound. `58/3` is about `19.33`, so every plan in that "
                    "node is worth at most that, and `22` already beats all of them. This "
                    "is the closure that makes the method a method; exploring anyway is "
                    "what makes readers explore everything."},
            {"q": "Which of these is not one of the three reasons to close a node?",
             "a": ["Its relaxation is infeasible",
                   "Its relaxation came back with every variable whole",
                   "Its bound cannot beat the best whole plan in hand",
                   "Its bound is worse than its parent's"],
             "c": 3,
             "why": "A child's bound is always at least as bad as its parent's, because "
                    "the child's region is smaller &mdash; so that condition holds at "
                    "every node and closes nothing. The three real reasons are "
                    "infeasibility, being bounded out, and integrality."},
            {"q": "On a 0/1 variable, how does “include the item or exclude it” relate to `x ≤ ⌊v⌋` and `x ≥ ⌈v⌉`?",
             "a": ["They are different trees, and the include/exclude one is smaller",
                   "They are the same two children: `x ≤ 0` and `x ≥ 1`",
                   "Include/exclude applies only when the relaxation is fractional at exactly `1/2`",
                   "They differ, because `x ≤ 0` also permits negative values"],
             "c": 1,
             "why": "For any `v` strictly between `0` and `1`, `⌊v⌋ = 0` and `⌈v⌉ = 1`, so "
                    "the two schemes produce the same pair of children. With `x ≥ 0` "
                    "already in the model, `x ≤ 0` is exactly “exclude”."},
        ],
        "mistakes": [
            ("Branching by fixing the variable to a rounded value",
             "`x₁ = 2` and `x₁ = 3` in place of `x₁ ≤ 2` and `x₁ ≥ 3`. It looks tidier and "
             "it deletes every plan with `x₁ = 0`, `1`, `4` or `5`. The method's "
             "correctness rests entirely on the two children covering every whole point of "
             "the parent, and assignments do not."),
            ("Exploring a worse-bounded node in case something good is inside",
             "This is the mistake that makes a reader explore everything, and it comes from "
             "reading a bound as an estimate. A bound of `58/3` is a proof that nothing in "
             "that region exceeds `58/3`. If `22` is in hand, the region has been searched "
             "&mdash; by arithmetic, which is cheaper than by tree."),
            ("Reporting an optimum from a tree that has not closed",
             "An open node is a region nothing has been proved about, so the best plan in "
             "hand is a plan and not an answer. The honest report is the pair &mdash; plan "
             "and bound &mdash; which is why the lab refuses to name an optimum when it "
             "hits its node budget, and why the next lesson exists."),
        ],
        "standard": ("Finish when a closed node reads as a region you have proved empty of anything better.",
                     "You should be able to run a two-variable tree by hand with every "
                     "node's bound as an exact fraction, name which of the three reasons "
                     "closed each node, say why the two children lose no whole-number plan, "
                     "explain what the dual simplex is doing between a parent and a child, "
                     "and state what changes and what does not when the search order "
                     "changes."),
        "note": 'A node with a worse bound is still the second mistake above, and it is worth one more sentence because it is so natural. A bound is not a forecast: nothing inside that node beats that number, so if the plan in hand already does, the region contains nothing for you. What a tree that has <em>not</em> closed leaves you with is a plan and a bound rather than an answer &mdash; and &ldquo;Incumbents, Bounds and the Gap&rdquo; is about reporting that pair honestly.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "incumbents-bounds-and-the-optimality-gap",
        "title": "Incumbents, Bounds and the Gap",
        "module": "Search and bounds",
        "one_line": "Produce a plan and a bound, compute the gap, and say exactly what has been proved after each node.",
        "summary": (
            "Any feasible plan, from any source at all, bounds the optimum from one side, "
            "and any relaxation bounds it from the other. The distance between them is the "
            "only thing actually proved at a given moment; closing it is what the search "
            "spends its time on; and reporting it is what honesty looks like when the "
            "exponential worst case cannot be ruled out. A small gap is not a probability."
        ),
        "key": [
            "incumbent   any feasible plan        a lower bound (max)",
            "global bound   the best bound over the open nodes   an upper bound",
            "gap = bound − incumbent      relative gap = gap ÷ incumbent",
            "after 5 nodes   21 and 47/2    gap 5/2,  relative 5/42 ≈ 11.9%",
            "after 7 nodes   21 and 70/3    gap 7/3,  relative 1/9  ≈ 11.1%",
            "after 9 nodes   23 and 23      gap 0 — and that is the proof",
        ],
        "key_label": "Two numbers, and the only statement they support",
        "concepts_intro": (
            "One hard idea, and it is about what the word “proved” covers. The gap is a "
            "statement about the bound, and there is no probability anywhere in it."
        ),
        "concepts": [
            ("Two bounds, from two entirely different kinds of object",
             "A feasible plan is a lower bound for a maximisation because it is achievable; "
             "it can come from greed, from a tree, from a person who knows the business. A "
             "relaxation is an upper bound because it optimises over a larger set. Neither "
             "knows about the other, and the optimum is between them."),
            ("The gap is what is proved, and the incumbent is usually better than it",
             "A gap of `5/2` on an incumbent of `21` proves that nothing whole beats `21` "
             "by more than `5/2`. It does not say the optimum is near `23.5`, and it does "
             "not say `21` is probably optimal. On this instance `21` is <em>not</em> "
             "optimal, and on the next one the plan found at the third node is optimal for "
             "a long stretch of nodes during which nothing has been proved about it."),
            ("Relative gap is measured against the value in hand",
             "`gap ÷ incumbent`: `5/2` on `21` is `5/42`, about `11.9%`. The incumbent "
             "is the number "
             "you have, which is the only one defined before the optimum is known, and it "
             "is what every solver reports. Dividing by the bound instead gives a "
             "different number and is a different claim, so the denominator belongs in the "
             "report."),
        ],
        "read_title": "Two bounds, one gap, and the sentence it licenses",
        "read_intro": "Where each bound comes from, what their difference proves, and why search order changes the work and never the answer.",
        "body": [
            ("def", ("Incumbent",
                     "The <strong>incumbent</strong> is the best feasible solution found "
                     "so far, together with its value. It is a lower bound on the optimum "
                     "of a maximisation and an upper bound for a minimisation, and its "
                     "provenance is irrelevant: a plan is a plan.")),
            ("def", ("Global bound and optimality gap",
                     "The <strong>global bound</strong> is the best bound over every node "
                     "still open, or the incumbent's own value when none is. The "
                     "<strong>absolute gap</strong> is the difference between the global "
                     "bound and the incumbent; the <strong>relative gap</strong> is that "
                     "difference divided by the incumbent. A gap of zero means the "
                     "incumbent is optimal, and that is a proof.")),
            ("p", "Take `max 4x₁ + 3x₂` subject to `3x₁ + 2x₂ ≤ 17` welding and "
                  "`2x₁ + 5x₂ ≤ 23` painting. The root relaxation is worth `261/11`, "
                  "about `23.73`. Its answer is `23`, at `(5, 1)`. Watch what is proved "
                  "along the way, taking the newest open node each time."),
            ("math", ["  after node   incumbent   global bound   gap     relative",
                      "      3          none         47/2         —          —",
                      "      5           21          47/2        5/2      11.9%",
                      "      7           21          70/3        7/3      11.1%",
                      "      9           23           23          0       0.00%"]),
            ("p", "Read the second row as a sentence. “Nothing beats `21` by more than "
                  "`5/2`.” That is all of it. It is a statement about `47/2`, which is a "
                  "property of a relaxation, and it contains no claim about how likely `21` "
                  "is to be best. As it happens `21` is not best: the answer is `23`, two "
                  "more, and well within the `5/2` the bound allowed."),
            ("p", "The first row is worth as much as the others. With no incumbent there is "
                  "no gap and nothing whatever has been proved &mdash; a bound alone rules "
                  "out nothing, because it does not exhibit a plan. Two numbers are needed, "
                  "and a report with one of them is not a weaker report; it is a different "
                  "kind of statement."),
            ("h3", "What a two per cent gap says, and what it does not"),
            ("p", "A 2% gap proves that nothing beats the incumbent by more than 2%. There "
                  "is no probability in that sentence and none can be smuggled in: the gap "
                  "is a bound on how wrong the plan in hand could be, not an estimate of "
                  "how wrong it is. The incumbent is frequently optimal long before the "
                  "gap closes, and the nodes spent after it was found buy the proof rather "
                  "than the plan."),
            ("p", "That is also the honest answer to “can we stop?”. Stopping with a stated "
                  "gap is a result: the plan is in hand and its worst case is quantified. "
                  "Stopping without one leaves a plan and a hope, and the two look "
                  "identical on a slide."),
            ("p", "Search order changes the work and not the answer. On this instance, "
                  "taking the newest open node closes the tree in nine nodes; taking the "
                  "most promising open node closes it in seven, and reaches the answer "
                  "without ever holding a worse incumbent &mdash; its first incumbent is "
                  "`23`, and the gap is zero the moment it appears. Neither order is right; "
                  "they trade a good early plan against a fast-falling bound, and which "
                  "helps depends on the instance."),
            ("p", "The reason a gap is the deliverable at all is that the alternative "
                  "cannot be promised. The search tree's worst case is exponential and "
                  "that result belongs to the Algorithms path&rsquo;s &ldquo;Backtracking "
                  "and Branch-and-Bound&rdquo;; the vocabulary for saying what kind of "
                  "hardness this is belongs to Discrete Mathematics&rsquo; &ldquo;P, NP "
                  "and NP-Completeness&rdquo;. Neither is restated here. What is this "
                  "lesson's own is the consequence: if the tree may not close, then the "
                  "number you report has to be the pair."),
        ],
        "lab": ("integer", {
            "mode": "gap",
            "preset": "early",
            "panel_title": "Watch the two bounds close on each other",
            "panel_intro": "The incumbent comes from any feasible point and the bound from "
                           "the relaxation; both are re-derived from the node list, so the "
                           "same tree gives the same trace. Drag the node count back to "
                           "the beginning and read the “what is proved” column one row at "
                           "a time.",
        }),
        "steps_title": "Reporting a result with a gap attached",
        "steps_intro": "Five steps, and the last is the one that makes the other four worth doing.",
        "steps": [
            ("Get an incumbent from anywhere",
             "Greed, a heuristic, last year's plan, a guess that turns out feasible. Its "
             "quality does not matter yet; its existence does, because without a feasible "
             "plan there is nothing for a bound to bound."),
            ("Get a bound from a relaxation",
             "The root relaxation is the cheapest one. Later, the best bound over the open "
             "nodes is the global bound, and it falls as the tree grows because every "
             "child's region is smaller than its parent's."),
            ("Compute both gaps",
             "Absolute, as an exact difference, and relative, against the incumbent. Say "
             "which denominator you used: the same tree supports two different percentages "
             "and only one of them is the convention."),
            ("Say what is proved, in a sentence with no probability in it",
             "“Nothing beats `21` by more than `5/2`.” If the sentence you write contains "
               "“probably”, “roughly” or “close to”, it is not the sentence the arithmetic "
             "supports."),
            ("Report the pair, never the incumbent alone",
             "A plan with a gap of zero is an optimum with a proof. A plan with a gap of "
             "`5/42` is a result. A plan with no gap is a number, and nobody reading it "
             "can tell which of the three they have been handed."),
        ],
        "worked": {
            "title": "max 4x₁ + 3x₂ on the welding and painting rows",
            "intro": [
                "One instance, run both ways. The answer is `23` in both; everything else "
                "differs.",
            ],
            "lines": [
                "max  4x₁ + 3x₂        3x₁ + 2x₂ ≤ 17     (welding)",
                "                      2x₁ + 5x₂ ≤ 23     (painting)",
                "",
                "root relaxation  261/11 ≈ 23.73  at (39/11, 35/11)",
                "answer           23 at (5, 1)",
                "",
                "TAKING THE NEWEST OPEN NODE",
                "  after 3 nodes   incumbent none    bound 47/2 = 23.5",
                "                  nothing is proved: there is no plan to bound",
                "  after 5 nodes   incumbent 21      bound 47/2",
                "                  gap 5/2, relative 5/2 ÷ 21 = 5/42 ≈ 11.9%",
                "                  nothing beats 21 by more than 5/2",
                "  after 7 nodes   incumbent 21      bound 70/3 ≈ 23.33",
                "                  gap 7/3, relative 1/9 ≈ 11.1%",
                "  after 9 nodes   incumbent 23      bound 23",
                "                  gap 0 — 23 is optimal, and that is proved",
                "",
                "TAKING THE MOST PROMISING OPEN NODE",
                "  after 3 nodes   none, bound 47/2",
                "  after 5 nodes   none, bound 70/3",
                "  after 7 nodes   23 and 23, gap 0",
                "",
                "  9 nodes against 7, for the same answer",
            ],
            "after": [
                "The two runs illustrate the trade directly. Depth first had a plan worth "
                "`21` in hand after five nodes and spent four more proving it was beatable "
                "and then beaten. Best bound had no plan at all until node seven and then "
                "had the answer with a closed gap in the same step.",
                "Which is preferable depends entirely on whether you might have to stop "
                "early. With a hard time limit, a run holding `21` with an `11.9%` gap "
                "is "
                "worth more than a run holding nothing with a tighter bound, because the "
                "first can be acted on. That is a reason to prefer depth first early and "
                "best bound late, and it is why real solvers switch.",
                "For a faded rehearsal, use the lab's first instance &mdash; the one whose "
                "bound comes down slowly &mdash; and stop the node count at each value in "
                "turn. The supplied first move is that the incumbent can never fall and "
                "the global bound can never rise, so the gap is non-increasing. Find the "
                "first node at which the gap is below `5%`, and then say whether the "
                "incumbent changed after that point.",
            ],
        },
        "quiz_title": "What the two numbers prove",
        "quiz": [
            {"q": "The incumbent is `21` and the global bound is `47/2`. What has been proved?",
             "a": ["That the optimum is about `23.5`",
                   "That `21` is probably optimal, since `5/2` is a small gap",
                   "That nothing feasible beats `21` by more than `5/2`",
                   "That the optimum is either `21` or `47/2`"],
             "c": 2,
             "why": "A gap bounds how much better anything could be. It makes no claim "
                    "about where the optimum is inside the interval and contains no "
                    "probability. Here the optimum is `23`, which is two above the "
                    "incumbent and comfortably inside the `5/2` the bound permitted."},
            {"q": "A run has a bound of `47/2` and no incumbent yet. What has been proved?",
             "a": ["Nothing, because there is no feasible plan to bound",
                   "That the optimum is at least `47/2`, since a relaxation bounds it",
                   "That the problem is infeasible",
                   "That the gap is infinite"],
             "c": 0,
             "why": "A bound does rule out values above `47/2`, and with no feasible "
                    "plan in hand nothing has been achieved and nothing can be reported "
                    "as a result. Reading it as a lower bound is the direction error: a "
                    "relaxation of a maximisation bounds the optimum from above. The lab "
                    "says so in words rather than printing a dash, because “no gap yet” "
                    "and “a small gap” are completely different situations."},
            {"q": "Absolute gap `7/3` on an incumbent of `21` and a bound of `70/3`. What is the relative gap as solvers report it?",
             "a": ["`7/3 ÷ (70/3) = 1/10`, about `10%`", "`7/3 ÷ 21 = 1/9`, about `11.1%`",
                   "`7/3 ÷ (70/3 + 21) = 1/19`, about `5.3%`", "`7/3` is already a relative gap"],
             "c": 1,
             "why": "The convention divides by the incumbent &mdash; the value in hand, "
                    "which is defined before the optimum is known. Dividing by the bound "
                    "gives `1/10`, a different and also computable number, which is "
                    "exactly why the denominator has to be stated."},
            {"q": "Two search orders close the same instance in nine nodes and seven nodes. What differs?",
             "a": ["The answer, since best bound finds a better optimum",
                   "The work, and the shape of the trace; the answer is the same",
                   "The bound at the root, which depends on the order",
                   "Nothing measurable; node counts are implementation details"],
             "c": 1,
             "why": "Order decides which node is taken next and therefore how quickly the "
                    "bound falls and when a plan appears. It cannot change which plans are "
                    "feasible, so a closed tree returns the same optimum either way. The "
                    "root bound is solved before any choice of order is made."},
        ],
        "mistakes": [
            ("Reading a small gap as a probability",
             "“A 2% gap, so it is almost certainly optimal” is not what the arithmetic "
             "says. The gap bounds how much better anything could be; it is a statement "
             "about the relaxation. The incumbent may be optimal and it may be 2% short, "
             "and the gap does not distinguish those two cases &mdash; which is the point "
             "of reporting it rather than interpreting it."),
            ("Reporting the incumbent on its own",
             "One number cannot be checked. `23` with a gap of zero is an optimum with a "
             "proof; `23` with a gap of `11%` is a good plan; `23` with no gap is a number "
             "whose status the reader has to guess. The pair costs one extra column and "
             "carries all the information."),
            ("Treating a falling bound as progress on the answer",
             "On the instance above the bound went `47/2`, then `70/3`, then `23` while "
             "the plan in hand sat at `21` for four nodes and then jumped to `23`. Most of "
             "the search's work went into the proof and none of it into the plan. A falling "
             "bound means the claim is getting stronger, not that the answer is improving."),
        ],
        "standard": ("Finish when you would rather report two numbers with a proof than one number with a hope.",
                     "You should be able to produce an incumbent from a heuristic and a "
                     "bound from a relaxation, compute the absolute and relative gaps with "
                     "the denominator named, write the one sentence each stage licenses "
                     "without the word “probably” in it, and say what changes and what "
                     "cannot change when the search order changes."),
        "note": 'The gap is the deliverable, and the reason is that the alternative cannot be promised: the search tree&rsquo;s exponential worst case is the Algorithms path&rsquo;s result and the vocabulary of hardness is Discrete Mathematics&rsquo;, and neither is restated here. What this course adds next is a way of making the bound better rather than the tree bigger &mdash; &ldquo;Cutting Planes and Gomory Cuts&rdquo; derives an inequality that the relaxation breaks and no whole-number plan does.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "cutting-planes-and-gomory-cuts",
        "title": "Cutting Planes and Gomory Cuts",
        "module": "Cuts, and one hard problem",
        "one_line": "Derive a cut from a fractional tableau row, test it on every lattice point, and re-solve by the dual simplex.",
        "summary": (
            "Take a row of the final tableau whose basic variable is fractional and split "
            "every coefficient into its floor and its fractional part. The fractional "
            "parts give an inequality that every whole-number plan satisfies and the "
            "current relaxation optimum breaks, so it can be added; the dual simplex "
            "restores optimality; and repeating drives the corner toward a whole point "
            "without ever removing one."
        ),
        "key": [
            "a row      Σ a_j x_j = b        a_j = ⌊a_j⌋ + f_j,  0 ≤ f_j ≤ 1",
            "the cut    Σ f_j x_j ≥ f_0      breaks the corner, keeps every whole plan",
            "53/10 at (7/2, 9/5)   cut 1  6x₁ + 6x₂ ≤ 31   →  31/6 at (25/6, 1)",
            "                      cut 2   x₁ +  x₂ ≤  5   →  5 at (5, 0), whole",
            "two cuts, two dual-simplex pivots, and no lattice point lost",
            "x₁ + x₂ ≤ 4 breaks the corner and kills (3, 2), (4, 1), (5, 0) — not a cut",
        ],
        "key_label": "One row, one cut, and what validity means",
        "concepts_intro": (
            "One hard idea, and it is what the word “valid” covers: a claim about every "
            "whole-number plan, not about the fractional point you would like to remove."
        ),
        "concepts": [
            ("A fractional row yields an inequality from its leftovers",
             "Write each coefficient as its floor plus a fractional part in `[0, 1)`. Move "
             "the floors to the other side; what remains is `Σ f_j x_j ≥ f_0`, an "
             "inequality built out of the parts that could not be accounted for by whole "
             "multiples. It is a consequence of the row together with integrality, so no "
             "whole-number plan breaks it."),
            ("Validity is a claim about every integer point",
             "A cut is valid when no whole-number plan in the region violates it. Cutting "
             "off the current fractional corner is what makes a cut <em>useful</em> and has "
             "nothing to do with whether it is <em>valid</em>. `x₁ + x₂ ≤ 4` removes the "
             "corner on this instance and also removes `(3, 2)`, `(4, 1)` and `(5, 0)` "
             "&mdash; which are the three optimal plans."),
            ("Adding a cut is a dual-simplex step, not a new solve",
             "The added row makes the current tableau infeasible and leaves it optimal, "
             "which is the dual simplex's case exactly &mdash; the same fact that let a "
             "branch-and-bound child start from its parent. Each cut here costs one pivot, "
             "and two cuts take this instance from a fractional corner to a whole one."),
        ],
        "read_title": "A cut derived from a row, and what makes it valid",
        "read_intro": "The derivation, the validity claim, the re-solve, and the inequality that looks like a cut and is not one.",
        "body": [
            ("p", "Take `max x₁ + x₂` subject to `2x₁ + 5x₂ ≤ 16` kiln hours and "
                  "`6x₁ + 5x₂ ≤ 30` glaze. The relaxation stops where the two rows meet, "
                  "at `(7/2, 9/5)`, worth `53/10`. Sixteen whole points lie in the "
                  "region, "
                  "around the region, and the best of them is worth `5` &mdash; attained "
                  "at `(3, 2)`, at `(4, 1)` and at `(5, 0)`, three ways."),
            ("def", ("Fractional part",
                     "For a rational `a`, the <strong>floor</strong> `⌊a⌋` is the largest "
                     "integer at most `a` and the <strong>fractional part</strong> is "
                     "`f = a − ⌊a⌋`, which lies in `[0, 1)`. On a fraction `n/d` this is a "
                     "division with remainder, so nothing is rounded and `f` is exact: "
                     "`⌊9/5⌋ = 1` and the fractional part is `4/5`.")),
            ("def", ("Gomory cut",
                     "Let a row of the final tableau read `Σ a_j x_j = b` with the basic "
                     "variable fractional, and let `f_j` and `f₀` be the fractional parts "
                     "of `a_j` and `b`. Then <strong>`Σ f_j x_j ≥ f₀`</strong> is a "
                     "<strong>Gomory cut</strong>: it is satisfied by every non-negative "
                     "integer solution of the row and violated by the current relaxation "
                     "optimum.")),
            ("thm", ("A Gomory cut removes no whole-number plan",
                     "Every non-negative integer point satisfying the original rows "
                     "satisfies `Σ f_j x_j ≥ f₀`.")),
            ("proof", ["Substitute `a_j = ⌊a_j⌋ + f_j` and `b = ⌊b⌋ + f₀` into the row and "
                       "rearrange: `Σ f_j x_j − f₀ = ⌊b⌋ − Σ ⌊a_j⌋ x_j`.",
                       "For integer `x` the right-hand side is an integer, so the left-hand "
                       "side is an integer too. And `f₀ ` is in `[0, 1)` while every `f_j` "
                       "and every `x_j` is non-negative, so `Σ f_j x_j − f₀` is greater "
                       "than `−1`. An integer greater than `−1` is at least `0`, which is "
                       "the cut."]),
            ("p", "The derivation used integrality twice and the objective not at all, "
                  "which is why the cut is a fact about the feasible set rather than about "
                  "the problem being solved. It is also why it is safe to add: the region "
                  "shrinks, every whole point stays, so `z_IP` cannot move while `z_LP` can "
                  "only fall."),
            ("example", ("The first cut, in two coordinate systems",
                         "The row whose basic variable is `x₂` gives, in the tableau's own "
                         "variables, `(3/10)s₁ + (9/10)s₂ ≥ 4/5`, where `s₁` and `s₂` are "
                         "the slacks of the kiln and glaze rows. Substituting the slacks "
                         "back turns that into `6x₁ + 6x₂ ≤ 31` in the reader's own "
                         "coordinates. At `(7/2, 9/5)` the left-hand side is `6(7/2) + "
                         "6(9/5) = 21 + 54/5 = 159/5`, which is `31.8` and breaks it. At "
                         "every whole point of the region it holds, because `6x₁ + 6x₂` is "
                         "a multiple of `6`, so breaking `≤ 31` would need `36`, which "
                         "means `x₁ + x₂ ≥ 6` &mdash; and the relaxation's own optimum "
                         "is `53/10`, so nothing in the region gets near it.")),
            ("h3", "Two cuts, and a whole corner"),
            ("p", "Add that cut and re-solve. One dual-simplex pivot moves the optimum to "
                  "`(25/6, 1)`, worth `31/6`, which is about `5.17` &mdash; still "
                  "fractional, and the bound has come down from `53/10 = 5.3`. Now cut "
                  "again, from the row whose basic variable is `x₁`: in the tableau it is "
                  "`(1/6)s₃ ≥ 1/6`, where `s₃` is the slack of the cut just added, and in "
                  "the reader's variables it is `x₁ + x₂ ≤ 5`. One more pivot, and the "
                  "relaxation stops at `(5, 0)`, worth `5`, whole."),
            ("math", ["  cut  from row     in the tableau           in x       then at     z",
                      "   1   basic x₂   (3/10)s₁+(9/10)s₂ ≥ 4/5   6x₁+6x₂ ≤ 31  (25/6, 1)  31/6",
                      "   2   basic x₁   (1/6)s₃ ≥ 1/6             x₁+x₂ ≤ 5     (5, 0)      5",
                      "",
                      "  53/10  >  31/6  >  5 = z_IP        two cuts, two pivots"]),
            ("p", "Two cuts have driven the relaxation to the integer optimum, and the "
                  "certificate is that the final corner is whole: a whole point attaining "
                  "the relaxation's value is optimal for the integer problem, by the "
                  "bounding theorem of the first lesson. No search tree was needed on this "
                  "instance."),
            ("p", "Now the counterexample. `x₁ + x₂ ≤ 4` also removes `(7/2, 9/5)`, and it "
                  "is not a cut: it removes `(3, 2)`, `(4, 1)` and `(5, 0)` as well, which "
                  "are every optimal whole plan there is. Adding it produces a smaller "
                  "region whose integer optimum is `4`, and nothing in the arithmetic "
                  "afterwards would reveal that the answer had been changed. Validity is a "
                  "claim about all sixteen whole points of the region, and the lab "
                  "tests it "
                  "against every one of them."),
            ("p", "Cutting is not a complexity result either. Each round strengthens the "
                  "bound, which is worth having &mdash; a better bound closes nodes, so "
                  "cuts and the search tree are used together rather than in competition. "
                  "What a round of cuts does not come with is a promise about how many "
                  "rounds are needed, and in practice a solver adds a few, branches, and "
                  "adds more inside the tree."),
        ],
        "lab": ("integer", {
            "mode": "gomory",
            "preset": "corner",
            "panel_title": "Add cuts one at a time, and test one of your own",
            "panel_intro": "Each cut is derived from a fractional row, drawn in the "
                           "reader's own coordinates, added to the tableau and re-solved by "
                           "the dual simplex; every one is tested against every lattice "
                           "point in the box. Type an invalid cut and the panel names the "
                           "whole-number plan it killed.",
        }),
        "steps_title": "Deriving a cut and proving it valid",
        "steps_intro": "Five steps, and the fourth is the one that separates a cut from an inequality you happen to like.",
        "steps": [
            ("Solve the relaxation and find a row with a fractional basic variable",
             "There may be several, and any of them will do; different rows give different "
             "cuts and all of them are valid. The lab lets you pick the row, which is the "
             "cheapest way to see that."),
            ("Split every coefficient into its floor and its fractional part",
             "Exactly, on fractions. `⌊9/5⌋ = 1` with fractional part `4/5`; `⌊−7/2⌋ = −4` "
             "with fractional part `1/2`. Floor is not rounding, and a negative "
             "coefficient is where the difference bites."),
            ("Write the cut",
             "`Σ f_j x_j ≥ f₀` in the tableau's variables. Then substitute the slacks back "
             "if you want to see it in your own coordinates, which is where it can be "
             "drawn and where it is worth checking."),
            ("Test it on every whole point of the region",
             "This is the validity claim and it is the whole lesson. One whole point on the "
             "wrong side means the inequality is not a cut, whatever it does to the "
             "fractional corner, and the point that died is the diagnosis."),
            ("Add it and re-solve with the dual simplex",
             "The tableau is still optimal and now infeasible, so a few pivots restore it. "
             "Then look: if the corner is whole you are finished, and if it is not there is "
             "another row to cut from."),
        ],
        "worked": {
            "title": "max x₁ + x₂ on the kiln and glaze rows, cut to a whole corner",
            "intro": [
                "One instance, two cuts, and a third inequality that is not one. Every "
                "coefficient is exact.",
            ],
            "lines": [
                "max  x₁ + x₂          2x₁ + 5x₂ ≤ 16     (kiln)",
                "                      6x₁ + 5x₂ ≤ 30     (glaze)",
                "",
                "relaxation   (7/2, 9/5)   z = 7/2 + 9/5 = 35/10 + 18/10 = 53/10",
                "whole optimum   5, at (3, 2), (4, 1) and (5, 0) — three of them",
                "",
                "CUT 1, from the row whose basic variable is x₂",
                "  in the tableau    (3/10)s₁ + (9/10)s₂ ≥ 4/5",
                "  in x              6x₁ + 6x₂ ≤ 31",
                "  at (7/2, 9/5):    21 + 54/5 = 159/5 = 31.8  >  31      broken ✓",
                "  at (3,2) 30 ≤ 31   (4,1) 30 ≤ 31   (5,0) 30 ≤ 31      kept ✓",
                "  re-solve, 1 dual-simplex pivot →  (25/6, 1)   z = 31/6",
                "",
                "CUT 2, from the row whose basic variable is x₁",
                "  in the tableau    (1/6)s₃ ≥ 1/6",
                "  in x              x₁ + x₂ ≤ 5",
                "  at (25/6, 1):     25/6 + 1 = 31/6 ≈ 5.17  >  5          broken ✓",
                "  re-solve, 1 pivot →  (5, 0)   z = 5   WHOLE",
                "",
                "  53/10  >  31/6  >  5        and 5 is the answer, proved by",
                "                              a whole point attaining the bound",
                "",
                "NOT A CUT:  x₁ + x₂ ≤ 4",
                "  at (7/2, 9/5):  53/10 > 4     it does break the corner",
                "  at (3, 2): 5 > 4     at (4, 1): 5 > 4     at (5, 0): 5 > 4",
                "  it removes all three optimal plans, so the answer becomes 4",
            ],
            "after": [
                "The two cuts differ in an instructive way. The first is written in the "
                "original slacks and comes out as `6x₁ + 6x₂ ≤ 31`, whose coefficients are "
                "ugly and whose content is simple: `x₁ + x₂ ≤ 31/6`. The second is derived "
                "from the slack of the first cut, and it says `x₁ + x₂ ≤ 5` &mdash; the "
                "same inequality with the right-hand side pushed down to the nearest whole "
                "value the objective can reach.",
                "The last block is the one to keep. `x₁ + x₂ ≤ 4` looks exactly like the "
                "cut that worked, one unit tighter, and it silently deletes the answer. "
                "Nothing downstream complains: the relaxation solves, the corner is whole, "
                "and the reported optimum of `4` is the correct answer to a problem that "
                "was never asked.",
                "For a faded rehearsal, derive the first cut from the second row instead "
                "&mdash; the lab has a control for the row. The supplied first move is that "
                "the derivation does not depend on which row you pick, only on that row's "
                "fractional parts, so the cut will be different and equally valid. Get "
                "`3x₁ + 5x₂ ≤ 19`, check it at `(7/2, 9/5)` and at all three optimal "
                "plans, and say what the bound becomes.",
            ],
        },
        "quiz_title": "Cuts, validity and the re-solve",
        "quiz": [
            {"q": "What makes an inequality a valid cut?",
             "a": ["That it removes the current relaxation optimum",
                   "That no whole-number plan of the region violates it",
                   "That its coefficients are integers",
                   "That it is implied by one of the original rows"],
             "c": 1,
             "why": "Validity is the claim about every whole-number plan. Removing the "
                    "fractional corner makes a valid cut useful and is not itself "
                    "validity: `x₁ + x₂ ≤ 4` removes the corner and also the three optimal "
                    "plans. A cut is generally not implied by any single original row "
                    "&mdash; the derivation uses integrality as well."},
            {"q": "In the derivation, why is `Σ f_j x_j − f₀` at least `0` for integer `x`?",
             "a": ["Because every `f_j` is at least `1`",
                   "Because it equals an integer and is greater than `−1`",
                   "Because the objective is maximised",
                   "Because the slacks are non-negative"],
             "c": 1,
             "why": "Rearranging the row makes it equal to `⌊b⌋ − Σ ⌊a_j⌋ x_j`, an integer. "
                    "And it exceeds `−1`, since `f₀` is below `1` and every term "
                    "`f_j x_j` is non-negative. An integer greater than `−1` is at least "
                    "`0`."},
            {"q": "What is `⌊−7/2⌋`, and what is the fractional part of `−7/2`?",
             "a": ["`−3` and `−1/2`", "`−4` and `1/2`", "`−3` and `1/2`", "`−4` and `−1/2`"],
             "c": 1,
             "why": "The floor is the largest integer at most `−7/2 = −3.5`, which is `−4`, "
                    "and the fractional part `a − ⌊a⌋` is then `1/2`. Reading floor as "
                    "“round toward zero” gives `−3` and a negative fractional part, which "
                    "breaks the derivation, since it needs every `f_j` in `[0, 1)`."},
            {"q": "You add a valid cut to a solved tableau. What is the state of that tableau?",
             "a": ["Optimal and feasible, so nothing is needed",
                   "Optimal and infeasible, which is the dual simplex's case",
                   "Feasible and not optimal, which is the primal simplex's case",
                   "Neither, so the problem must be solved again from the start"],
             "c": 1,
             "why": "The cut is violated by the current solution, so the tableau is "
                    "infeasible; the objective row is untouched, so it is still optimal. "
                    "That is exactly the situation the dual simplex handles, which is why "
                    "each cut here costs one pivot rather than a fresh solve."},
        ],
        "mistakes": [
            ("Believing any inequality that cuts off the fractional optimum is a cut",
             "`x₁ + x₂ ≤ 4` does remove `(7/2, 9/5)`, and it removes `(3, 2)`, `(4, 1)` and "
             "`(5, 0)` with it &mdash; every optimal whole plan. Validity is a claim about "
             "all the whole points, not about the one you dislike, and the only way to hold "
             "the claim is to check them."),
            ("Reading the floor as a rounding",
             "`⌊9/5⌋` is `1`, not `2`; `⌊−7/2⌋` is `−4`, not `−3`. The derivation needs "
             "every fractional part in `[0, 1)`, and “round to nearest” or “round toward "
             "zero” breaks that on exactly the coefficients where it matters. On a fraction "
             "the floor is a division with remainder and it is exact."),
            ("Re-solving from scratch after adding a cut",
             "It is not wrong and it is wasteful, and it also hides what happened. The "
             "tableau was optimal and became infeasible, which is one specific thing "
             "&mdash; the dual simplex case &mdash; and knowing that is what makes the cut "
             "loop cheap enough to repeat. Two cuts on this instance cost two pivots in "
             "total."),
        ],
        "standard": ("Finish when “is it valid?” means “which whole-number plans does it keep?” rather than “does it look reasonable?”",
                     "You should be able to derive a cut from a given fractional row with "
                     "exact fractional parts, write it in both the tableau's variables and "
                     "your own, verify that it breaks the relaxation optimum and keeps every "
                     "whole point of the region, re-solve by the dual simplex, and recognise "
                     "an inequality that cuts the corner and is not valid."),
        "note": 'Floors of exact rationals are what make the derivation clean, and `⌊x⌋` is already defined in the library: Discrete Mathematics&rsquo; &ldquo;Functions&rdquo; gives `⌊x⌋` as the largest integer at most `x` and `⌈x⌉` as the smallest integer at least `x`. On a fraction `n/d` the floor is a division with remainder, so nothing is rounded and every coefficient of every cut on this page is exact.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-travelling-salesman-problem",
        "title": "The Travelling Salesman Problem",
        "module": "Cuts, and one hard problem",
        "one_line": "Bound a tour by the assignment problem, cut the subtours it leaves, branch, and measure a heuristic against the result.",
        "summary": (
            "The assignment problem is a relaxation of the travelling salesman problem: it "
            "forces one departure and one arrival per city and permits several disjoint "
            "subtours. The constraints that would forbid them are exponentially many, so "
            "they are added only when a solution actually violates one. Relaxation, cut, "
            "branch, repeat solves small instances exactly &mdash; and a heuristic tour is "
            "only as good as the bound you can measure it against."
        ),
        "key": [
            "assignment relaxation   one departure and one arrival per city; subtours allowed",
            "subtour cut   forbid an arc of the shortest subtour, then re-solve and branch",
            "distinct undirected tours, fixed start   (n − 1)!/2      360 at n = 7",
            "6 cities   60 tours   bound 80   subtours (1 5)(2 3)(4 6)",
            "optimum 88 in 5 nodes      nearest neighbour 96, measured gap 8 = 1/12",
            "nearest neighbour then 2-opt   88 — optimal here, and only a bound says so",
        ],
        "key_label": "A relaxation that leaves subtours, and a gap you can measure",
        "concepts_intro": (
            "One hard idea: the relaxation here is not “drop integrality” but “drop one "
            "requirement”, and the requirement it drops is the one that makes a tour a "
            "tour."
        ),
        "concepts": [
            ("The assignment problem is the relaxation",
             "Choose, for each city, one city to leave for and one to arrive from, at "
             "minimum total cost. Every tour satisfies that; so does a set of disjoint "
             "subtours, which is not a tour at all. So the assignment optimum is a lower "
             "bound on the tour, and the subtours it returns are the exact way in which it "
             "failed to be an answer."),
            ("The constraints that forbid subtours are added on demand",
             "There is one subtour-elimination constraint for every proper subset of the "
             "cities, which is exponentially many and cannot be written down. They are also "
             "almost all slack at the optimum, so they are added when a solution violates "
             "one: solve, find the shortest subtour, forbid an arc of it, re-solve. That is "
             "the branching, and it is a cut in the sense of the previous lesson."),
            ("Near-optimal is meaningless without a bound",
             "A nearest-neighbour tour on the lab's six-city instance costs `96`. Whether "
             "that is good is not a question the tour can answer. Against the optimum of "
             "`88` it is `8` worse, a measured `1/12` of the tour in hand; and "
             "improving it by 2-opt gives "
             "`88` exactly, which is optimal &mdash; a fact that only the bound could have "
             "established."),
        ],
        "read_title": "A bound, the subtours it leaves, and the gap a heuristic leaves",
        "read_intro": "How many tours there actually are, where the bound comes from, and why a measured gap and a proved ratio are different kinds of knowledge.",
        "body": [
            ("p", "Before any method, the count &mdash; because three different numbers "
                  "are in circulation and each is correct for something else. On `n` "
                  "cities there are `n!` orderings of the cities; `(n − 1)!` tours from a "
                  "fixed start, counting each once per direction; and `(n − 1)!/2` "
                  "<em>distinct undirected</em> tours, which is what you are choosing "
                  "among when the cost from one city to another is the same both ways."),
            ("math", ["  n = 7      n! = 5040        orderings of the cities",
                      "           7!/2 = 2520        each ordering once per direction",
                      "        (n−1)! =  720         tours from a fixed start, both ways",
                      "      (n−1)!/2 =  360         DISTINCT UNDIRECTED TOURS",
                      "",
                      "  n = 6      (n−1)!/2 = 60    and the lab enumerates exactly 60"]),
            ("p", "Those `360` at seven cities are why the lab stops at seven: `360` tours "
                  "can be enumerated instantly, so an exact answer is available to check "
                  "every bound against, and that is worth more at this size than another "
                  "city. The cap is this lab's own and it is a consequence of "
                  "`(n − 1)!/2` &mdash; nothing to do with the `n!` orderings that "
                  "Discrete Mathematics&rsquo; Hamilton lab enumerates, which is a "
                  "different quantity on a different object."),
            ("p", "The claim “the number of tours is `n!`” is therefore an overcount by a "
                  "factor of `2n`: at seven cities `5040` against `360`, and "
                  "`5040 ÷ 360 = 14 = 2 × 7`. The factor `n` is the arbitrary choice of "
                  "starting city and the factor `2` is the direction, neither of which "
                  "changes the tour or its length."),
            ("def", ("Subtour-elimination constraint",
                     "For a proper non-empty subset `S` of the cities, the constraint says "
                     "that the chosen arcs may not form a closed cycle inside `S`: at "
                     "least one arc must leave `S`. There is one such constraint per "
                     "subset, so there are exponentially many, and a formulation that "
                     "wrote them all down could not be built for a moderate `n`.")),
            ("example", ("Six cities: the bound, the subtours, and the tree",
                         "On the lab's opening instance the assignment relaxation is worth "
                         "`80`, and it returns three two-city subtours: cities `1` and `5` "
                         "shuttling between each other, `2` and `3`, and `4` and `6`. That "
                         "is a bound and not a route. Forbid one arc of the shortest "
                         "subtour and re-solve; two of the children come back with a "
                         "four-city subtour and a two-city one, still not a tour; forbid an "
                         "arc again and the next child is a genuine tour worth `88`. Five "
                         "nodes in total, and the answer `88` is the route "
                         "`1 → 2 → 4 → 6 → 3 → 5 → 1`.")),
            ("h3", "A measured gap, and a proved ratio"),
            ("p", "Nearest neighbour from city `1` gives `1 → 5 → 3 → 4 → 6 → 2 → 1`, "
                  "costing `96`. Against the optimum of `88` that is `8` worse, which is "
                  "`8/96 = 1/12` of the tour in hand &mdash; a measured gap, on this "
                  "instance, for this heuristic, which the panel shows as `8.3%`. "
                  "with a gap of zero. That happens, and it is worth knowing rather than "
                  "assuming, which takes a bound."),
            ("p", "A measured gap and a proved ratio are different kinds of knowledge and "
                  "the difference is worth a paragraph. The Algorithms path&rsquo;s "
                  "&ldquo;Metric TSP by MST Doubling&rdquo; proves a factor of two for "
                  "every metric instance there is, for ever, without solving any of them. "
                  "This lesson measures `1/12` on one instance, exactly, and claims "
                  "nothing about the next one. The first is a theorem about a class; the "
                  "second is a fact about a case &mdash; and on your own data, the fact is "
                  "often what you need and is the only one of the two you can compute."),
            ("p", "Three results are used here and proved elsewhere. The other exact "
                  "method is the dynamic programme over subsets of "
                  "&ldquo;DP over Subsets: Held–Karp&rdquo;, which runs in `n² 2ⁿ` time "
                  "&mdash; a different trade, since it beats `(n − 1)!` badly and still "
                  "grows exponentially. Why the problem is hard at all is "
                  "&ldquo;Reductions and Their Direction&rdquo;, in the same subject. And "
                  "the two-approximation above is that path's as well. None of the three "
                  "is derived here."),
            ("p", "The apparent tension between “hard” and “solved exactly in five nodes” "
                  "is not one. Hardness is a statement about every instance of every size; "
                  "a certificate is a statement about the instance in front of you. "
                  "Branch and cut solves small and structured instances routinely, and the "
                  "gap it reports on the ones it cannot close is exactly the honest form of "
                  "the same fact &mdash; which is what this course has been building "
                  "toward since the first rounded point failed."),
            ("p", "Every cost in the lab is an integer or a fraction, so every tour length, "
                  "every bound and every gap on the page is exact. That is deliberate: the "
                  "one place this problem could produce an irrational number is a Euclidean "
                  "distance, and a comparison between two tours that differs in the sixth "
                  "decimal place is not a comparison anybody should be making on a rounded "
                  "value."),
        ],
        "lab": ("integer", {
            "mode": "tsp",
            "preset": "plants",
            "panel_title": "Edit the costs; the bound, the tree and the gap all move",
            "panel_intro": "Every distinct tour is enumerated, the assignment relaxation is "
                           "solved and branched on its subtours, and a heuristic tour is "
                           "measured against the result. Switch the heuristic to nearest "
                           "neighbour alone to see a gap that is not zero, and raise the "
                           "city count to seven to watch the tour count go to `360`.",
        }),
        "steps_title": "Solving a small tour exactly, and measuring a heuristic",
        "steps_intro": "Five steps, and the count in the first one is what keeps the last one honest.",
        "steps": [
            ("Count the tours before choosing a method",
             "`(n − 1)!/2` distinct undirected tours: `60` at six cities, `360` at seven, "
             "`2 520` at eight. Enumeration is the right method for exactly as long as that "
             "number is small, and knowing where that stops is why the other four steps "
             "exist."),
            ("Solve the assignment relaxation",
             "One departure and one arrival per city, at minimum cost. Its value is a lower "
             "bound on every tour. If it happens to return a single cycle, that cycle is "
             "the optimal tour and you are finished."),
            ("Find the subtours and forbid an arc of the shortest",
             "The shortest subtour is the cheapest one to break and gives the fewest "
             "children. Forbidding one arc is a cut: no tour is lost, because a tour "
             "cannot contain that subtour anyway. The panel names the banned arc by "
             "its raw index, so the city drawn as `1` appears in that column as `0`."),
            ("Branch, and keep the bound with each node",
             "Each child is another assignment problem with one arc forbidden, so the bound "
             "rises as arcs are banned. Close a node the moment its bound cannot beat the "
             "best tour in hand &mdash; the three closing reasons are the ones from the "
             "search lesson."),
            ("Measure the heuristic against the bound and report the pair",
             "A tour of `96` is a number. A tour of `96` against a proved optimum of `88` "
             "is a result: `8` worse, `1/12` of it. Without the second number, “near-optimal” "
             "has nothing behind it."),
        ],
        "worked": {
            "title": "Six plants, the assignment bound, and two heuristic tours",
            "intro": [
                "The lab's opening instance at six cities, with the costs symmetric. Every "
                "figure is exact and every one can be checked against the panel.",
            ],
            "lines": [
                "6 cities, symmetric costs.   distinct undirected tours: 5!/2 = 60",
                "  not 720 = 6!, which counts orderings",
                "  not 360 = 6!/2, and not 120 = 5!, which counts each tour twice",
                "",
                "ASSIGNMENT RELAXATION",
                "  value 80, and it returns three two-city subtours:",
                "     (1 5)   (2 3)   (4 6)",
                "  80 is a lower bound on every tour; it is not a route",
                "",
                "THE TREE",
                "  node 0   bound 80    subtours (1 5)(2 3)(4 6)   branch on (1 5)",
                "  node 1   bound 88    subtours (1 2 3 5)(4 6)    branch on (4 6)",
                "  node 2   bound 88    subtours (1 5 3 2)(4 6)    closed by the bound",
                "  node 3   bound 96    one cycle: a tour, worth 96",
                "  node 4   bound 88    one cycle: a tour, worth 88   ←  the optimum",
                "  5 nodes.  optimum 88 on  1 → 2 → 4 → 6 → 3 → 5 → 1",
                "",
                "  check by enumeration:  all 60 tours tried, best is 88",
                "",
                "HEURISTICS, MEASURED",
                "  nearest neighbour from city 1:   1 → 5 → 3 → 4 → 6 → 2 → 1   = 96",
                "     gap 96 − 88 = 8,   8/96 = 1/12 of the tour in hand, shown as 8.3%",
                "  then 2-opt:                                                   = 88",
                "     gap 0 — optimal on this instance, and the bound is how you know",
            ],
            "after": [
                "Node 0's three two-city subtours are the clearest possible picture of what "
                "the relaxation dropped. Shuttling between two plants satisfies “one "
                "departure and one arrival each” perfectly, costs very little, and visits "
                "nothing. The `8` between `80` and `88` is the price of the requirement "
                "that the route be one cycle.",
                "Node 2 is closed by the bound at `88`, equal to the best tour in hand, "
                "which is the same closure the search lesson used: nothing in a node beats "
                "the node's bound. And node 3 is a reminder that a node returning a tour "
                "does not return the best one &mdash; `96` is a genuine tour and it is "
                "beaten two nodes later.",
                "For a faded rehearsal, raise the lab to seven cities. The supplied first "
                "move is the count: `(7 − 1)!/2 = 360` distinct undirected tours, six times "
                "the sixty at six cities. Predict whether the root bound rises or falls "
                "when a city is added, then read the optimum, the node count, and the "
                "measured gap of the 2-opt tour &mdash; which this time is not zero.",
            ],
        },
        "quiz_title": "Counts, bounds and gaps",
        "quiz": [
            {"q": "How many distinct undirected tours are there on seven cities?",
             "a": ["`5040`, which is `7!`", "`2520`, which is `7!/2`",
                   "`720`, which is `6!`", "`360`, which is `6!/2`"],
             "c": 3,
             "why": "`(n − 1)!/2` with `n = 7` is `720/2 = 360`. The other three count "
                    "real things: `5040` orderings of the cities, `2520` orderings up to "
                    "direction, and `720` tours from a fixed start counted once per "
                    "direction. Quoting one of them as “the number of tours” is where "
                    "three specifications once disagreed."},
            {"q": "The assignment relaxation returns three two-city subtours worth `80` in total. What is `80`?",
             "a": ["The length of the shortest tour",
                   "A lower bound on every tour, and not a route",
                   "An upper bound on every tour",
                   "The length of the shortest tour through three of the cities"],
             "c": 1,
             "why": "Every tour satisfies the assignment constraints, so the assignment "
                    "minimum is at most the shortest tour: `80 ≤ 88` here. The solution "
                    "attaining it is not a tour at all, which is precisely why the value "
                    "is a bound."},
            {"q": "Why are the subtour-elimination constraints added only when a solution violates one?",
             "a": ["Because they are not valid until a subtour appears",
                   "Because there is one per subset of the cities, and almost all are slack at the optimum",
                   "Because adding them all would make the problem infeasible",
                   "Because the assignment relaxation cannot be solved with them present"],
             "c": 1,
             "why": "They are all valid all along; there are simply exponentially many, and "
                    "the optimum satisfies nearly all of them without being told to. Adding "
                    "the one a solution actually breaks is the same economy as a cutting "
                    "plane: generate the inequality that is doing work."},
            {"q": "A nearest-neighbour tour costs `96` and the proved optimum is `88`. What can you say, and what can you not?",
             "a": ["It is `8` worse than optimal on this instance; nothing follows about other instances",
                   "Nearest neighbour is within `1/12` of optimal in general",
                   "It is `8` worse, so 2-opt will improve it by `8`",
                   "Nothing, because a gap needs a relaxation rather than an exact optimum"],
             "c": 0,
             "why": "A measured gap is a fact about one instance. A statement about every "
                    "instance is a proved ratio, which is what “Metric TSP by MST Doubling” "
                    "establishes for a different algorithm &mdash; and the two are different "
                    "kinds of knowledge. 2-opt does reach `88` here, but that is another "
                    "measurement, not a consequence."},
        ],
        "mistakes": [
            ("Calling a heuristic tour near-optimal with no bound",
             "“Near” is a comparison and there is nothing to compare with until something "
             "has been proved. On the lab's instance nearest neighbour is `8` off, which is "
             "`1/12` of the tour, and on the next instance it could be `40%`; the word carries no "
             "information either way. A tour and a bound is a result; a tour alone is a "
             "route."),
            ("Quoting the number of tours as n!",
             "`n!` counts orderings of the cities, and the tours it corresponds to are "
               "counted `2n` times each: once per starting city and once per direction. At "
             "seven cities that is `5040` against `360`. The overcount matters because it "
             "is the number that decides whether enumeration is possible, and it is wrong "
             "by a factor of fourteen at the size where the decision is made."),
            ("Taking an assignment solution as a route",
             "One departure and one arrival per city is satisfied by a set of disjoint "
             "shuttles, and the lab's opening relaxation returns exactly that: three pairs "
             "of plants visiting each other. Its value is a perfectly good bound and its "
             "arcs are not a plan, which is the same distinction as a fractional `y` in the "
             "modelling lessons."),
        ],
        "standard": ("Finish when a tour without a bound beside it reads as an unfinished result.",
                     "You should be able to say how many distinct undirected tours a size "
                     "has and why the other two counts are counts of something else, solve "
                     "the assignment relaxation and name the subtours it leaves, add a "
                     "subtour cut and branch to an optimal tour with its certificate, and "
                     "report a heuristic tour with its measured gap while distinguishing "
                     "that from a proved ratio."),
        "note": 'The cost matrix here is integer or rational, so every tour length, bound and gap on the page is exact. A Euclidean coordinate preset would introduce surds; if one is ever added, the distances are square roots of integers, printed as surds and rounded only for display, with every comparison between tours made on the exact value. A square root of a non-square is the one place this course could round, and it does not.',
    },
]
