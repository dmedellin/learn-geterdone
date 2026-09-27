"""Intractability and Approximation, lessons 08-13 - parameterising, the four guarantees, and what a sweep settles.

Same discipline as part_a: every figure was read off the lab at the preset the
lesson opens on, by executing the shipped JavaScript. Two numbers in these six
dicts are not measurements and both say so on the page: the promise of 2 for the
metric tour and the promise of `H_n` for greedy set cover are proved bounds over
every instance, printed beside ratios of 10/7 and 3/2 that were counted on one.
"""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "parameterising-the-budget",
        "title": "Parameterising the Budget",
        "module": "Exact answers, still exponential",
        "one_line": "Branch on both ends of an uncovered edge, spend one unit of budget either way, and settle a six-cycle in 9 nodes against a tree bound of 16.",
        "summary": (
            "An exponential does not have to be an exponential in the size of the input. Ask "
            "whether a graph has a vertex cover of size at most `k` and there is a search tree of "
            "depth `k`: one end of an uncovered edge must be in the cover, so branching costs a "
            "factor of two per unit of budget and the size of the graph enters only as the cost "
            "of scanning for an edge. The lab prints `2^k · n` against `2^n` with both computed, "
            "and on one of its examples the first is larger."
        ),
        "key": [
            "an uncovered edge uv: one of u, v is in the cover — there is no third option",
            "so branch on it, spend 1 of the budget either way, and the depth is at most k",
            "",
            "six-cycle, k = 3:   a cover of 3 exists, 2 does not",
            "9 nodes opened against a tree bound of 16, and the answer is right",
            "2^k · n = 48 against 2^n = 64",
            "",
            "on two triangles with k = 4:  2^k · n = 96 against 2^n = 64",
        ],
        "key_label": "A tree whose depth is the budget, and the two work figures side by side",
        "concepts_intro": (
            "The first idea is the branching rule, which is a two-line argument and the whole "
            "method. The second is what &ldquo;fixed-parameter tractable&rdquo; asks for, which "
            "is a shape of running time rather than a speed. The third is the instance where the "
            "shape does not pay."
        ),
        "concepts": [
            ("One end or the other, and no third option",
             "Take an edge whose ends are both still uncovered. Any vertex cover must contain `u` "
             "or `v`, because the edge has to be touched and there is nothing else touching it. "
             "That is a complete case split, so branching on it loses no solution, and each "
             "branch has spent one unit of the budget. After `k` levels the budget is gone: if "
             "some uncovered edge remains the branch fails, and if none does the branch has a "
             "cover. The depth of the tree is the budget and not the graph."),
            ("Fixed-parameter tractable is a shape, not a speed",
             "A problem is fixed-parameter tractable in a parameter `k` when it can be solved in "
             "time `f(k)` times a polynomial in the input size, for some function `f` depending on "
             "`k` alone. Here `f(k) = 2^k` and the polynomial is the cost of scanning the edges, "
             "so the running time is about `2^k · n`. Nothing in that says the algorithm is fast: "
             "`f` is allowed to be monstrous. What it says is that the exponential has been moved "
             "off the input size and onto a quantity that may be small in practice."),
            ("The shape does not pay at every parameter",
             "The panel prints `2^k · n` and `2^n` as two integers. On the six-cycle with `k = 3` "
             "they are 48 and 64, so parameterising wins narrowly. On the two-triangles example "
             "with `k = 4` they are 96 and 64, so it loses: the cover needs four vertices in a "
             "graph with six, and a budget almost as large as the graph buys nothing. "
             "Parameterising is worth doing when the parameter is genuinely small, and whether it "
             "is is a fact about your instances rather than about the method."),
        ],
        "read_title": "The branching rule, the tree bound, and the two work figures",
        "read_intro": "The rule, why it is exhaustive, the bound on the tree, what the lab counted at each budget, and the instance where the method costs more than brute force.",
        "body": [
            ("def", ("The parameterised problem",
                     "<strong>Vertex cover, parameterised by solution size</strong>: given a "
                     "graph and an integer `k`, is there a vertex cover with at most `k` "
                     "vertices? The parameter is `k`, chosen by whoever asks the question, and "
                     "the algorithm's running time is allowed to depend on it in any way at all "
                     "provided the dependence on the graph is polynomial.")),
            ("thm", ("The bounded search tree is correct, and its depth is k",
                     "The branching algorithm returns a cover of size at most `k` if one exists "
                     "and reports failure otherwise, and it opens at most `2^(k+1)` nodes.")),
            ("proof", ("For correctness, induct on the budget. With budget 0 the algorithm "
                       "succeeds exactly when no edge is uncovered, which is right. With budget "
                       "`b > 0`, if no edge is uncovered the current set is already a cover. "
                       "Otherwise pick an uncovered edge `uv`; every cover of size at most `b` "
                       "more contains `u` or `v`, so one of the two recursive calls sees a "
                       "sub-problem with a solution whenever the current node has one, and by "
                       "induction finds it.",
                       "For the size, the recursion branches into two children and decreases the "
                       "budget by one, so the tree has depth at most `k` and at most `2^(k+1) - "
                       "1` nodes. The work at each node is a scan for an uncovered edge, which is "
                       "linear in the number of edges, so the whole search costs `O(2^k · m)`.")),
            ("h3", "What the lab counted"),
            ("p", "The loaded graph is the cycle on six vertices with `k = 3`. The panel reports "
                  "a cover of size 3 &mdash; vertices 1, 3 and 5 &mdash; an exhaustive optimum of "
                  "3, the answer correct, 9 nodes opened, a tree bound of 16, and `2^k · n = 48` "
                  "against `2^n = 64`. Moving the budget down one at a time gives the shape of "
                  "the search: `k = 0` fails in 1 node, `k = 1` fails in 3, `k = 2` fails in 7, "
                  "and `k = 3` succeeds in 9."),
            ("p", "Two of those numbers are worth pausing on. At `k = 2` the search opens 7 nodes "
                  "against a bound of 8 and fails, which is the bound almost exactly attained: "
                  "when there is no cover the tree is explored in full. At `k = 3` it opens 9 "
                  "against a bound of 16, because it stops at the first cover it finds and does "
                  "not enumerate the rest. Success is cheaper than failure here, and that is "
                  "typical of a search with no bound to prune with."),
            ("example", ("A budget that settles a graph of any size",
                         "Load the star on eight vertices with `k = 1`. The hub covers every "
                         "edge, so one unit of budget suffices, and the panel reports 3 nodes "
                         "against `2^k · n = 16` and `2^n = 256`. A star with forty leaves would open the "
                         "same 3 nodes, because the tree's depth is the budget and the graph "
                         "enters only through the scan &mdash; though that is an argument "
                         "rather than a measurement, since the panel's parser stops at eight "
                         "vertices. That is the whole promise of parameterising, on the "
                         "instance where it is most visible.")),
            ("h3", "And the instance where it does not pay"),
            ("p", "Load the two disjoint triangles with `k = 4`. Each triangle needs two vertices "
                  "covered, so 4 is the smallest budget that works, and 4 is large relative to "
                  "the graph's 6 vertices. The panel prints `2^k · n = 96` against `2^n = 64`: "
                  "the parameterised bound is worse than checking every subset. The search still "
                  "only opens 9 nodes, which is the honest measurement, but the two work figures "
                  "are the ones that generalise and one of them is losing."),
            ("p", "This is the same reading discipline as the previous page in a new costume. "
                  "`2^k · n` and `2^n` are expressions evaluated at the instance on screen; they "
                  "are not measurements, and the panel labels them as the expressions they are. "
                  "The node count is the measurement. Neither is a claim about the other, and the "
                  "interesting cases are exactly the ones where they disagree."),
            ("p", "One thing this course does not build: kernelisation, where the instance itself "
                  "is shrunk to a size depending only on `k` before any search begins. A vertex "
                  "of degree above `k` must be in any cover of size `k`, which is the first "
                  "reduction rule, and there are others that leave a graph with `O(k^2)` edges. "
                  "It is the other half of parameterised algorithms and it is named here rather "
                  "than demonstrated."),
        ],
        "lab": ("coping", {"mode": "fpt", "preset": "cycle6"}),
        "steps_title": "Choosing a parameter, and checking it is doing work",
        "steps_intro": "The method is mechanical. Deciding whether it helps is a measurement on your instances.",
        "steps": [
            ("Find a complete case split with few cases",
             "The branching rule must cover every possibility: one end of an uncovered edge, or "
               "the other. A rule with a case missing loses solutions silently, and a rule with "
               "many cases gives a bigger base for the exponential. Two is the smallest "
               "interesting number and it is what this problem gives."),
            ("Check that every branch spends budget",
             "The depth bound is the budget, so a branch that recurses without decreasing `k` "
             "destroys it and the search may not terminate. This is the invariant to state "
             "explicitly, and it is what makes the tree bound a bound rather than a hope."),
            ("Compare the two work figures at your own parameter",
             "Evaluate `2^k · n` and `2^n` on the instance you actually have. If the parameter is "
             "a constant fraction of the input size, parameterising is not buying anything, and "
             "the panel has an example where it is measurably worse."),
            ("Check the answer against an exhaustive optimum",
             "The bounded search answers a yes-or-no question about a budget, so it can be right "
             "for the wrong reason. The lab computes the true minimum cover separately and "
             "requires the search to say yes exactly when that minimum is at most `k`, at every "
             "budget the slider covers."),
            ("Say which numbers were counted and which were evaluated",
             "The node count was counted. `2^k · n` and `2^n` are expressions evaluated at this "
             "instance's numbers. Mixing the two produces sentences of the form &ldquo;the "
             "algorithm did 48 units of work&rdquo;, which nothing on the page measured."),
        ],
        "worked": {
            "title": "The six-cycle at four budgets",
            "intro": [
                "The graph is `1-2, 2-3, 3-4, 4-5, 5-6, 6-1`, and the exhaustive minimum cover "
                "has 3 vertices. One row per budget: whether a cover of that size exists, how "
                "many nodes the search opened, and the bound on the tree.",
            ],
            "lines": [
                "   k    cover of size k?   nodes opened   tree bound 2^(k+1)   2^k · n",
                "",
                "   0          no                 1               2                6",
                "   1          no                 3               4               12",
                "   2          no                 7               8               24",
                "   3          YES                9              16               48",
                "   4          yes                9              32               96",
                "",
                "   2^n for this graph                                            64",
                "   exhaustive minimum cover                    3 vertices  {1, 3, 5}",
                "   the search says yes exactly when the minimum is at most k     every k",
                "",
                "   two disjoint triangles instead, k = 4:",
                "      nodes 9,  2^k · n = 96,  2^n = 64      the parameter is too large to pay",
            ],
            "after": [
                "The failing budgets are the expensive ones. At `k = 2` the search opens 7 nodes "
                "against a bound of 8, which is the tree explored almost in full &mdash; there is "
                "no cover to find, so every branch runs to the bottom of its budget before "
                "failing. At `k = 3` it opens 9 against a bound of 16 and stops at the first "
                "cover, so the extra budget costs almost nothing.",
                "The rows at `k = 3` and `k = 4` have the same node count and different work "
                "figures, which is the distinction this page keeps insisting on. The search did "
                "the same amount of work in both because it found a cover at the same depth; the "
                "expression `2^k · n` doubled because `k` did. One of those is a fact about the "
                "run and the other is a fact about the formula.",
                "For a faded rehearsal, load the path on seven vertices with `k = 3` and predict "
                "the node count before running it. The supplied first move: a path with six edges "
                "needs three interior vertices, so the budget is exactly enough and the search "
                "cannot afford a single wrong turn. Say whether you expect the count to be nearer "
                "9 or nearer the bound of 16, and then check.",
            ],
        },
        "quiz_title": "Parameters, trees and two kinds of number",
        "quiz": [
            {"q": "Why is branching on both ends of an uncovered edge exhaustive?",
             "a": ["Because every vertex is in some cover",
                   "Because the edge must be touched and only its two ends touch it",
                   "Because the graph is connected",
                   "Because the budget decreases"],
             "c": 1,
             "why": "A cover has to contain a vertex incident to that edge, and exactly two "
                    "vertices are. So the two branches between them contain every possible "
                    "cover, which is what makes the split lose nothing. Connectivity is "
                    "irrelevant, and the budget decreasing is what bounds the depth rather than "
                    "what makes the rule complete."},
            {"q": "The panel reports 9 nodes and a tree bound of 16 at `k = 3`. Why is the count so much lower than the bound?",
             "a": ["The bound is wrong",
                   "The search stops at the first cover it finds rather than exploring the whole tree",
                   "The graph is too small for the bound to apply",
                   "Nine is `2^3 + 1`, which is the real bound"],
             "c": 1,
             "why": "The bound is worst case and the worst case is failure: at `k = 2`, where no "
                    "cover exists, the search opens 7 against a bound of 8. Success short-circuits "
                    "the rest of the tree. The coincidence that 9 is one more than `2^3` is just a "
                    "coincidence on this instance."},
            {"q": "On two disjoint triangles with `k = 4`, `2^k · n` is 96 and `2^n` is 64. What follows?",
             "a": ["The parameterised algorithm is incorrect on this graph",
                   "The parameterised bound is worse than examining every subset here, because the parameter is large relative to the graph",
                   "Vertex cover is not fixed-parameter tractable",
                   "The tree bound has been exceeded"],
             "c": 1,
             "why": "Both numbers are expressions evaluated on this instance, and the "
                    "parameterised one is larger. The algorithm is still correct and still opens "
                    "only 9 nodes; the point is that the shape `f(k)` times a polynomial pays "
                    "only when `k` is small, which is a property of the instances you have. "
                    "Fixed-parameter tractability is about the existence of that shape, not about "
                    "it winning everywhere."},
            {"q": "Which of these would break the depth bound?",
             "a": ["Choosing a different uncovered edge at each node",
                   "A branch that adds a vertex without decreasing the budget",
                   "A graph with more edges than vertices",
                   "Starting from a non-empty partial cover"],
             "c": 1,
             "why": "The depth bound is the budget, so every branch must spend one. Which edge is "
                    "chosen affects the shape of the tree and not its depth; the size of the "
                    "graph enters only through the scan; and starting from a partial cover is "
                    "exactly what the recursion does at every level."},
        ],
        "mistakes": [
            ("Reading fixed-parameter tractable as fast",
             "The definition permits any dependence on the parameter whatever, and for some "
             "problems `f(k)` is a tower of exponentials. What the definition buys is that the "
             "input size appears polynomially, which is a structural statement about where the "
             "hardness lives."),
            ("Quoting `2^k · n` as work done",
             "It is an expression evaluated at two numbers from the instance, and the panel prints "
             "it beside a node count that was actually measured. On the six-cycle they are 48 and "
             "9. Naming which is which is the difference between a measurement and a label."),
            ("Choosing a parameter without checking it is small",
             "Vertex cover parameterised by solution size is a good idea when covers are small "
             "and a bad one when they are half the graph. The two-triangles example is the "
             "smallest case where the method measurably loses, and the check costs one evaluation "
             "of two expressions."),
        ],
        "standard": (
            "Finish when you can design a bounded search tree and say at which parameter it stops paying.",
            "You should be able to state a complete case split, prove every branch spends budget, "
            "derive the `2^(k+1)` node bound, check the yes-or-no answer against an exhaustive "
            "minimum at every budget, and evaluate `2^k · n` against `2^n` on your own instance "
            "before recommending the method.",
        ),
        "note": (
            "Exactness has been kept in both of the strategies so far, and paid for in an "
            "exponential. Everything after this page gives up exactness instead, and the first "
            "question is what a guarantee can possibly be a guarantee against when nobody knows "
            "the optimum."
        ),
    },

    # ---------------------------------------------------------------- 09
    {
        "slug": "twice-a-matching",
        "title": "Twice a Matching",
        "module": "Guarantees, and the lower bound they rest on",
        "one_line": "Take both ends of every matched edge, and watch a cover of 6 sit against an optimum of 3 with the promise of 2 exactly attained.",
        "summary": (
            "A guarantee cannot be a claim about the optimum, because nobody computing it knows "
            "the optimum. It is a claim about a <em>lower bound the algorithm can see</em>. A "
            "maximal matching is such a bound: its edges share no vertex, so any cover needs a "
            "distinct vertex for each, and taking both ends of each is a cover of exactly twice "
            "that. On the loaded graph the ratio is exactly 2, and the panel then searches every "
            "graph on four vertices to see whether anything does worse."
        ),
        "key": [
            "matching ≤ optimum ≤ cover = 2 × matching     the whole proof, four numbers",
            "the optimum appears in the middle link and nowhere in the algorithm",
            "",
            "three disjoint edges:  matching 3, optimum 3, cover 6, ratio exactly 2",
            "worst ratio over all 63 graphs on four vertices with an edge:  2",
            "",
            "on a bipartite graph the exact answer is a maximum matching — König, and cheap",
        ],
        "key_label": "The chain of four numbers, and the one link that mentions the optimum",
        "concepts_intro": (
            "The first idea is what a ratio is a ratio to, and where the guarantee's evidence "
            "actually comes from. The second is the chain, which is the proof written as four "
            "comparisons. The third is the special case where none of this is needed."
        ),
        "concepts": [
            ("A guarantee is proved against a lower bound, not against the optimum",
             "Say an algorithm returns a cover at most twice the smallest. The smallest is not "
             "known &mdash; computing it is the problem. What is known is the matching the "
             "algorithm built, and the argument runs entirely through it: the matching is below "
             "the optimum, and the answer is exactly twice the matching. The optimum is squeezed "
             "in the middle and is never computed. That is the shape of every approximation "
             "guarantee on this course, and it is why the panel draws four numbers on one axis "
             "rather than two."),
            ("Why both ends, and why maximal is enough",
             "Take edges one at a time, skipping any that touches a vertex already used: that is "
             "a <strong>maximal</strong> matching, meaning no edge can be added, not a "
             "<strong>maximum</strong> one. Maximal is enough for both halves. Its edges are "
             "disjoint, so every cover needs a vertex from each and the optimum is at least its "
             "size; and if some edge had neither end in the chosen set, that edge could have been "
             "added, contradicting maximality &mdash; so taking both ends of every matched edge "
             "covers everything."),
            ("Bipartite graphs do not need this at all",
             "König's theorem, proved from max-flow in the graph course, says the minimum vertex "
             "cover of a bipartite graph equals its maximum matching, and both are computable in "
             "polynomial time. The graph on screen is bipartite: three disjoint edges, maximum "
             "matching 3, minimum cover 3. So the approximation returns 6 where an exact "
             "polynomial algorithm returns 3, and this instance &mdash; where the guarantee is "
             "exactly attained &mdash; is an instance where the guarantee should not have been "
             "used. Knowing which special cases are exactly solvable is part of knowing when to "
             "approximate."),
        ],
        "read_title": "The algorithm, the chain it rests on, and the sweep that tests the promise",
        "read_intro": "The two-line algorithm, the four-link chain, the measured ratio, the search over every graph of a size, and the special case where the exact answer is cheap.",
        "body": [
            ("def", ("Maximal matching, and the cover built from it",
                     "A <strong>matching</strong> is a set of edges no two of which share a "
                     "vertex; it is <strong>maximal</strong> when no further edge can be added. "
                     "The algorithm scans the edges in order, keeps an edge whenever neither end "
                     "has been used, and returns the set of all endpoints of the kept edges as "
                     "its cover.")),
            ("thm", ("The endpoints of a maximal matching are a cover of at most twice the minimum",
                     "Let `M` be a maximal matching and `C` the set of endpoints of its edges. "
                     "Then `C` is a vertex cover, and `|C| = 2|M| ≤ 2 · τ`, where `τ` is the size "
                     "of the smallest cover.")),
            ("proof", ("`C` is a cover: if some edge had neither end in `C`, neither of its ends "
                       "is used by a matched edge, so it could be added to `M`, contradicting "
                       "maximality.",
                       "`|M| ≤ τ`: the edges of `M` are pairwise disjoint, and any cover must "
                       "contain at least one end of each, so it contains at least `|M|` distinct "
                       "vertices.",
                       "`|C| = 2|M|` by construction, since the endpoints of disjoint edges are "
                       "all different. Combining, `|C| = 2|M| ≤ 2τ`. Note which quantities appear "
                       "in each line: the algorithm computes `M` and `C`, and `τ` enters only in "
                       "the middle inequality, which is the one nobody has to evaluate.")),
            ("h3", "The chain, as four numbers on the panel"),
            ("math", [
                "matching        3      a lower bound the algorithm can see",
                "optimum         3      by exhaustive search over the subsets",
                "cover built     6      the endpoints of the matching",
                "twice the matching  6  the promise",
            ]),
            ("p", "The loaded graph is the three disjoint edges `1-2, 3-4, 5-6`. The matching "
                  "takes all three, the cover takes all six vertices, and the optimum is 3 "
                  "&mdash; one end of each edge. The realised ratio is exactly 2 and the panel "
                  "prints it against the promised 2. This is the worst the algorithm can do, and "
                  "it is not an artefact of a strange graph: every matched edge needs one vertex "
                  "in a cover and the algorithm takes two."),
            ("p", "The middle link is the only one needing an optimum, and it is the only one the "
                  "panel had to do extra work for: 3 comes from an exhaustive search over the "
                  "subsets of the vertices. Without it the ratio printed above would be a "
                  "fraction with an invented denominator, which is why every mode of this lab "
                  "computes both halves."),
            ("h3", "Every graph of a size, not just this one"),
            ("p", "The panel then does something a page about approximation usually only "
                  "describes. It enumerates every graph on the number of vertices its slider "
                  "names &mdash; 63 non-empty graphs on four vertices &mdash; solves each one "
                  "exactly, runs the approximation on each, and reports the worst ratio any of "
                  "them produced. The answer is 2, attained by 49 of the 63, and it names both "
                  "the first witness in edge order, which is a single edge, and the densest, "
                  "which has five edges. Both, because a reader shown only a single edge "
                  "concludes the bound is an artefact of a degenerate case."),
            ("example", ("A ratio strictly inside the promise",
                         "Switch to the five-cycle: the greedy matching takes two edges, the "
                         "cover has four vertices, the optimum is three, and the ratio is 4/3. "
                         "Switch to the two triangles and the ratio is 1 &mdash; the algorithm "
                         "returns the optimum. Neither number is the algorithm's number, and both "
                         "are inside a promise of 2 that the first graph attains exactly.")),
            ("p", "One honest caveat the panel states itself. The matching is greedy in edge "
                  "order, so the worst ratio found by the sweep is the worst case of this "
                  "implementation on graphs of that size; a different edge order is a different "
                  "matching. The bound of 2 covers all of them, because the proof never mentioned "
                  "the order &mdash; which is the sense in which a proof is stronger than a sweep "
                  "over every instance of a size."),
        ],
        "lab": ("coping", {"mode": "vertexcover", "preset": "matching"}),
        "steps_title": "Stating and checking an approximation guarantee",
        "steps_intro": "Five steps, and the first is the one that decides whether the guarantee means anything.",
        "steps": [
            ("Find a lower bound the algorithm can compute",
             "Not the optimum &mdash; something below it that falls out of the run. A maximal "
             "matching is the example here; a minimum spanning tree is the example on the next "
             "page. If there is no computable lower bound, there is no guarantee to prove, only a "
             "hope to measure."),
            ("Bound the answer against that lower bound",
             "Show the returned solution is at most `ρ` times the lower bound, by construction "
             "rather than by argument if possible. Here it is exactly twice, because the cover is "
             "the endpoints of disjoint edges and nothing else."),
            ("Write the chain out and check which link needs the optimum",
             "Lower bound, optimum, answer, promise. Only the middle inequality involves the "
             "optimum, and it holds because the lower bound is a lower bound. If your chain needs "
             "the optimum anywhere else, the guarantee is not provable in this shape."),
            ("Print the realised ratio with the optimum it is a ratio to",
             "On instances small enough to solve exactly, compute the optimum and divide. A ratio "
             "without its denominator is not a measurement, and the panel refuses to show one. "
             "Say also that the realised ratio is about this instance and the promise is about all "
             "of them."),
            ("Check the special cases before approximating at all",
             "Bipartite graphs have an exact polynomial algorithm for this problem, and the graph "
             "on screen is bipartite. Trees, bipartite graphs and bounded-degree graphs are the "
             "usual islands of tractability; walking past one to use a 2-approximation is a real "
             "mistake and the panel's default instance is an example of it."),
        ],
        "worked": {
            "title": "Three disjoint edges, and the sweep over every graph on four vertices",
            "intro": [
                "The graph is `1-2, 3-4, 5-6`. The matching is greedy in edge order and takes "
                "every edge, since none of them touch. The sweep below is a separate computation "
                "and does not depend on the graph in the box.",
            ],
            "lines": [
                "  the link in the chain        value        why it holds",
                "",
                "  matching ≤ optimum           3 ≤ 3        disjoint edges need distinct vertices",
                "  optimum ≤ cover              3 ≤ 6        the optimum is the smallest cover",
                "  cover = 2 × matching         6 = 2 × 3    both ends of each matched edge",
                "  so cover ≤ 2 × optimum       6 ≤ 6        the three lines above, in that order",
                "",
                "  realised ratio               6 / 3 = 2    against the promised 2",
                "  the cover is a cover                      checked against the edge list",
                "",
                "  the claim, and what it is about                          result",
                "  the ratio on the graph on screen        one graph          2",
                "  the worst over EVERY graph on 4 vertices  63 graphs        2",
                "  the smallest graph attaining it         the single edge 1-2",
                "  the largest graph attaining it          1-2, 1-3, 1-4, 2-3, 3-4",
                "  and the promise                         every graph, every size    2",
            ],
            "after": [
                "The first row of the chain is an equality here, and that is the coincidence that "
                "makes this instance the worst case: the matching is not merely a lower bound on "
                "the optimum, it equals it. The cover is then twice the optimum exactly, with no "
                "slack anywhere in the chain.",
                "The two witnesses from the sweep are both worth looking at. The single edge "
                "attains the ratio trivially &mdash; matching 1, cover 2, optimum 1 &mdash; and "
                "proves nothing about interesting graphs. The five-edge witness on four vertices "
                "is the same ratio on a graph that is nearly complete, and it is the one that "
                "shows the bound is not about degenerate cases. A page reporting only the first "
                "would be technically correct and would mislead.",
                "For a faded rehearsal, move the slider to five vertices and predict the worst "
                "ratio before running it. The supplied first move: the proof gives 2 for every "
                "size, and a single edge is a graph on five vertices too, so the worst ratio "
                "cannot be below 2 and cannot be above it. Say how many graphs are searched, and "
                "then check &mdash; and note that the answer being the same at three, four and "
                "five vertices is still not the theorem.",
            ],
        },
        "quiz_title": "Ratios, lower bounds and special cases",
        "quiz": [
            {"q": "The algorithm returns a cover at most twice the minimum. What does the proof actually compare the answer against?",
             "a": ["The minimum cover, computed by exhaustive search",
                   "The maximal matching it built, which is below the minimum",
                   "The number of edges",
                   "The best answer found so far"],
             "c": 1,
             "why": "The optimum cannot be part of the algorithm's reasoning, because computing "
                    "it is the problem. The matching is computable and is a lower bound on the "
                    "optimum, so bounding the answer by twice the matching bounds it by twice the "
                    "optimum. The exhaustive search on the panel is there to print a realised "
                    "ratio, not to make the guarantee work."},
            {"q": "Why is a maximal matching enough, rather than a maximum one?",
             "a": ["It is not: the proof needs a maximum matching",
                   "Because both halves of the argument need only that no edge can be added and that the edges are disjoint",
                   "Because maximal and maximum matchings are the same size",
                   "Because a maximum matching would give a ratio below 2"],
             "c": 1,
             "why": "Disjointness gives the lower bound and maximality gives the covering "
                    "property, and neither needs the matching to be largest. They are not the "
                    "same size in general &mdash; on a path of three edges a greedy scan can take "
                    "one where two fit. A maximum matching would not improve the worst-case "
                    "ratio, since the three-disjoint-edges instance has a maximum matching and "
                    "still attains 2."},
            {"q": "The sweep reports a worst ratio of 2 over all 63 graphs on four vertices. What does that establish?",
             "a": ["That no graph of any size does worse than 2",
                   "That the bound of 2 is attained at this size, so the promise cannot be improved for this algorithm",
                   "That the algorithm is optimal",
                   "That the bound of 2 is proved"],
             "c": 1,
             "why": "A sweep over one size shows attainment, which is what &ldquo;tight&rdquo; "
                    "means, and it cannot quantify over sizes. The proof does that. And "
                    "attainment is the opposite of the algorithm being optimal &mdash; it means "
                    "there are instances where it is as bad as the promise allows."},
            {"q": "The loaded graph is bipartite. What is the practical consequence?",
             "a": ["The approximation is exact on it",
                   "König's theorem gives the exact minimum cover in polynomial time, so approximating this instance was unnecessary",
                   "The ratio must be below 2",
                   "The matching is maximum, so the cover is minimum"],
             "c": 1,
             "why": "In a bipartite graph the minimum cover equals the maximum matching, and both "
                    "come from max-flow &mdash; which the graph course built. Here the exact "
                    "answer is 3 and the approximation returns 6, the worst it is allowed to. The "
                    "last answer is the standard slip: a maximum matching does not make the set of "
                    "its endpoints a minimum cover."},
        ],
        "mistakes": [
            ("Reading a guarantee as a statement about the optimum",
             "&ldquo;Within a factor 2 of optimal&rdquo; is true and is proved without ever "
             "evaluating the optimum. If you cannot say which computable quantity the argument "
             "compares the answer to, you cannot check the guarantee and you cannot tell a proved "
             "bound from an observed one."),
            ("Quoting a realised ratio as the algorithm's ratio",
             "This graph gives 2, the five-cycle gives 4/3 and the two triangles give 1. The "
             "promise is 2 for every graph and no single instance establishes it. The panel prints "
             "the instance's ratio, the worst over a whole size, and the promise as three separate "
             "rows for exactly this reason."),
            ("Approximating a problem on an instance where it is exactly solvable",
             "Bipartite structure, bounded degree, tree shape: each turns this problem "
             "polynomial. Reaching for the 2-approximation without checking is how an algorithm "
             "returns twice the right answer on an instance that would have given the right answer "
             "cheaply, which is precisely what happens on the default graph here."),
        ],
        "standard": (
            "Finish when you can prove a ratio against a lower bound and print it with its optimum.",
            "You should be able to construct a maximal matching by hand, show its endpoints cover "
            "the graph, prove the two inequalities that give the factor of 2, write the four-link "
            "chain and identify the only link mentioning the optimum, and name a special case "
            "where the exact answer is available in polynomial time.",
        ),
        "note": (
            "The lower bound here came from the algorithm's own run. &ldquo;The Hypothesis Doing "
            "the Work&rdquo; takes its lower bound from a minimum spanning tree instead, and the "
            "guarantee holds only under an assumption about the input that the panel lets you "
            "switch off."
        ),
    },

    # ---------------------------------------------------------------- 10
    {
        "slug": "the-hypothesis-doing-the-work",
        "title": "The Hypothesis Doing the Work",
        "module": "Guarantees, and the lower bound they rest on",
        "one_line": "Double a spanning tree of weight 5, shortcut it to a tour of 10 against an optimum of 7, then raise one distance and watch the promise fail.",
        "summary": (
            "A minimum spanning tree is below the optimal tour, doubling it gives a walk, and "
            "shortcutting the walk gives a tour &mdash; but only if a direct hop is never longer "
            "than going round. That proviso is the triangle inequality and the panel has a slider "
            "that removes it. On the loaded instance the tree is 5, the tour is 10, the optimum is "
            "7 and the ratio is 10/7, which is the worst ratio over all 482 metric instances on "
            "four cities with distances up to 3."
        ),
        "key": [
            "delete an edge of an optimal tour and a spanning tree is left:   MST ≤ OPT",
            "walk the tree twice:  2 × MST.   shortcut it:  no longer, IF the triangle inequality holds",
            "",
            "four cities:  MST 5,  optimum 7,  tour 10,  2 × MST 10       ratio 10/7",
            "worst over all 482 metric instances on four cities, distances ≤ 3:   10/7",
            "",
            "raise one distance to 50 and the tour is 53 against an optimum of 4",
        ],
        "key_label": "The chain for the metric tour, and the hypothesis the last link needs",
        "concepts_intro": (
            "The first idea is where the lower bound comes from, which is a one-line argument "
            "about deleting an edge. The second is the step the hypothesis is doing work in. The "
            "third is what a small exhaustive sweep can and cannot say about a guarantee."
        ),
        "concepts": [
            ("The lower bound is a spanning tree, and the argument is one deletion",
             "Take an optimal tour and delete any one of its steps. What remains visits every "
             "city and has no cycle, so it is a spanning tree, and its weight is less than the "
             "tour's. A minimum spanning tree is therefore no heavier than the optimal tour "
             "&mdash; a lower bound the algorithm computes with Prim's algorithm from the graph "
             "course, and the only thing the guarantee is proved against."),
            ("The shortcut step is where the hypothesis is spent",
             "Walking every tree edge twice gives a closed walk of weight exactly `2 · MST` "
             "visiting every city, but repeating cities. Shortcutting means skipping a city "
             "already visited and going straight to the next new one. That can only shorten the "
             "walk provided a direct hop is no longer than the path it replaces &mdash; which is "
             "exactly the triangle inequality. Without it the shortcut can cost more than the "
             "walk it replaces, and the panel's slider makes that happen."),
            ("A sweep bounds the ratio below the guarantee, and that is not evidence against it",
             "The panel enumerates every symmetric instance on four cities with distances from 1 "
             "to 3, keeps the 482 satisfying the triangle inequality, solves each exactly, and "
             "reports the worst ratio: 10/7, which is about 1.43 against a promise of 2. The "
             "guarantee is not thereby shown to be loose. It quantifies over every size and every "
             "distance range, and the family swept here is tiny &mdash; four cities and three "
             "possible distances. A bound over all instances is not refuted by the worst of a "
             "finite few."),
        ],
        "read_title": "The tree, the doubling, the shortcut, and the assumption it needs",
        "read_intro": "The algorithm in three steps, the chain of four numbers, the measured ratio, the sweep over every small metric instance, and what happens when the hypothesis fails.",
        "body": [
            ("def", ("The metric travelling salesman",
                     "Distances are given for every pair of cities, are symmetric, and satisfy "
                     "the <strong>triangle inequality</strong>: `D(a,b) ≤ D(a,c) + D(c,b)` for "
                     "all `a`, `b`, `c`. The problem is to find a shortest tour visiting every "
                     "city once and returning. Distances that come from positions in space "
                     "always satisfy the inequality, which is why the hypothesis is usually "
                     "free.")),
            ("h3", "The algorithm"),
            ("ol", [
                "Build a minimum spanning tree of the cities.",
                "Walk it, using every edge exactly twice, returning to the start. The walk has "
                "weight exactly twice the tree.",
                "Traverse the walk and skip every city already visited, hopping directly to the "
                "next new one. What is left visits each city once: a tour.",
            ]),
            ("thm", ("The doubled tree gives a tour within twice the optimum",
                     "For distances satisfying the triangle inequality, the tour produced has "
                     "length at most `2 · MST ≤ 2 · OPT`.")),
            ("proof", ("Deleting one step from an optimal tour leaves a connected acyclic "
                       "spanning subgraph, that is, a spanning tree, of weight at most the "
                       "tour's. So `MST ≤ OPT`.",
                       "The doubled walk has weight exactly `2 · MST` and visits every city. "
                       "Shortcutting replaces a sub-path from `a` to `b` through already-visited "
                       "cities by the direct hop `D(a,b)`; by the triangle inequality applied "
                       "along that sub-path, the hop is no longer than the sub-path it replaces. "
                       "So the tour is at most `2 · MST`, and combining gives `2 · OPT`.")),
            ("h3", "The chain, as four numbers"),
            ("math", [
                "the tree           5      a lower bound the algorithm computes",
                "the optimum        7      by exhaustive search over the tours",
                "the tour built    10      the doubled tree, shortcut",
                "twice the tree    10      the promise",
            ]),
            ("p", "The loaded instance is four cities with the distances `1-2 2, 1-3 1, 1-4 3, "
                  "2-3 3, 2-4 2, 3-4 2`, which satisfies the triangle inequality. The tree takes "
                  "the edges of weight 1, 2 and 2 for a total of 5; the shortcut tour is "
                  "`1, 2, 3, 4` at length 10; the optimum is 7, attained by `1, 2, 4, 3`; and the "
                  "realised ratio is 10/7. Notice that the tour equals `2 · MST` exactly here, so "
                  "the last link of the chain is an equality and all the slack in the promise "
                  "lives in the gap between 5 and 7."),
            ("p", "This instance was not chosen by hand. The panel enumerates every symmetric "
                  "instance on four cities with distances from 1 to 3 &mdash; 729 of them &mdash; "
                  "keeps the 482 that are metric, solves each exactly, and reports the worst ratio "
                  "any produced. It is 10/7, and this is the instance attaining it. On three "
                  "cities the same sweep reports a worst ratio of 1: the heuristic is exact there, "
                  "because every tour on three cities is the same tour."),
            ("example", ("Switching the hypothesis off",
                         "Load the instance with one distance raised: `1-2 50` with every other "
                         "distance 1. The direct hop from 1 to 2 costs 50 while going round "
                         "through 3 costs 2, so the triangle inequality fails by a factor of 25. "
                         "The panel reports metric: no, a tree of 3, a promise of 6, an optimum of "
                         "4 &mdash; and a tour of 53, against a promise of 6. The answer is "
                         "more than eight times the promise the algorithm made, "
                         "because the shortcut step replaced a cheap path by an enormous hop and "
                         "the proof's last line is simply false.")),
            ("p", "That is the most important thing on this page. A guarantee is a conditional, "
                  "and when the condition fails there is no residual weaker guarantee: the "
                  "algorithm can be arbitrarily bad, and the slider can make the ratio as large "
                  "as you like. Raising the distance further raises the tour without limit while "
                  "the optimum stays at 4."),
            ("p", "And the general problem really is that bad, which was proved earlier on this "
                  "course by putting `ρ · n + 1` on the non-edges: no constant-factor "
                  "approximation exists for the travelling salesman without a hypothesis, unless "
                  "`P = NP`. So the triangle inequality is not a convenience that simplifies the "
                  "analysis. It is the difference between a problem with a factor-2 algorithm and "
                  "a problem with no constant-factor algorithm at all."),
        ],
        "lab": ("coping", {"mode": "tsp", "preset": "worst4"}),
        "steps_title": "Using a guarantee that has a hypothesis attached",
        "steps_intro": "Four steps, and the first one is the only defence against a guarantee that does not apply.",
        "steps": [
            ("Check the hypothesis on your data before quoting the ratio",
             "Test the triangle inequality on every triple, which is what the panel's metric "
               "verdict is. Distances derived from coordinates always pass; distances that are "
               "prices, travel times with one-way roads, or measurements with noise may not, and "
               "a single violating triple is enough to void the guarantee."),
            ("Compute the lower bound, and keep it",
             "The minimum spanning tree is not a by-product, it is the evidence. Report it beside "
             "the tour: the pair `MST` and `2 · MST` brackets the answer, and it is the only "
             "bracket available when the optimum is out of reach."),
            ("Print the realised ratio with the optimum beside it, or not at all",
             "On an instance small enough to enumerate, compute the optimum and divide. On a real "
             "instance you cannot, and then the honest report is the tour and the tree &mdash; a "
             "ratio against an unknown denominator is not a number."),
            ("Read a small sweep for what it is",
             "482 metric instances on four cities with distances up to 3 give a worst ratio of "
             "10/7. That is a fact about a small family, and it neither confirms nor threatens a "
             "bound of 2 over all families. The panel reports the family size precisely so the "
             "claim can be read at the right scope."),
        ],
        "worked": {
            "title": "Four cities: the tree, the walk, the shortcut, and the optimum",
            "intro": [
                "Distances `1-2 2, 1-3 1, 1-4 3, 2-3 3, 2-4 2, 3-4 2`, every triple checked and "
                "metric. The tree is built by Prim's algorithm, unchanged from the graph course.",
            ],
            "lines": [
                "  the tree        1-3 at 1,  1-2 at 2,  3-4 at 2          weight 5",
                "  the walk        1 → 2 → 1 → 3 → 4 → 3 → 1               weight 10",
                "  shortcut        1 → 2 → 3 → 4 → 1                       length 10",
                "                  2 + 3 + 2 + 3 = 10",
                "",
                "  the three tours on four cities, enumerated:",
                "     1-2-3-4     2 + 3 + 2 + 3 = 10",
                "     1-2-4-3     2 + 2 + 2 + 1 = 7        the optimum",
                "     1-3-2-4     1 + 3 + 2 + 3 = 9",
                "",
                "  MST 5  ≤  optimum 7  ≤  tour 10  ≤  2 × MST 10          all four links hold",
                "  realised ratio     10 / 7      against the promised 2",
                "",
                "  every metric instance on four cities, distances 1 to 3:",
                "     729 instances, 482 of them metric, worst ratio 10/7",
                "     attained by this instance",
                "",
                "  the same instance with 1-2 raised to 50:",
                "     metric no,  tree 3,  promise 6,  optimum 4,  tour 53",
            ],
            "after": [
                "The shortcut here saves nothing: the walk weighs 10 and the tour is 10. That "
                "happens when the walk's repeated visits are all immediate backtracks, so the "
                "shortcut hops are the same edges the walk used. It is why this instance is the "
                "worst of the 482 &mdash; the algorithm pays the full `2 · MST` while the optimum "
                "gets away with 7.",
                "The optimum is `1-2-4-3`, which uses the two edges of weight 2 and the edge of "
                "weight 1, avoiding the 3s. The tree also used the edge of weight 1, so the two "
                "solutions overlap; the tree is not a bad guess, it is simply a different object, "
                "and the factor of 2 is the price of turning one into the other.",
                "For a faded rehearsal, load the instance the heuristic gets exactly right and "
                "predict the ratio before running it. The supplied first move: its distances are "
                "3, 4, 5 on one side and 3, 4, 3 on the other, so the tree weighs 9 and twice the "
                "tree is 18. Say what the tour and the optimum have to be for the ratio to come "
                "out at 1, then check &mdash; and note that an instance where the ratio is 1 is "
                "as uninformative about the worst case as one where it is 10/7.",
            ],
        },
        "quiz_title": "Trees, shortcuts and conditionals",
        "quiz": [
            {"q": "Why is a minimum spanning tree no heavier than the optimal tour?",
             "a": ["Because a tree has fewer edges than a tour",
                   "Because deleting one step from the optimal tour leaves a spanning tree",
                   "Because Prim's algorithm is greedy",
                   "Because every tour contains a spanning tree as a subgraph of equal weight"],
             "c": 1,
             "why": "Delete a step and what remains is connected, acyclic and spans, so it is a "
                    "spanning tree of weight below the tour's; the minimum tree is at most that. "
                    "Edge counts alone prove nothing about weights, the greedy rule is how the "
                    "tree is computed rather than why the inequality holds, and the subgraph left "
                    "after deletion has strictly smaller weight, not equal."},
            {"q": "Which step of the algorithm uses the triangle inequality?",
             "a": ["Building the tree",
                   "Doubling the tree into a walk",
                   "Shortcutting past cities already visited",
                   "Comparing the tour against the optimum"],
             "c": 2,
             "why": "The tree and the doubling are valid for any symmetric distances: the walk "
                    "weighs exactly twice the tree whatever the numbers are. Only the shortcut "
                    "needs a direct hop to be no longer than the path it replaces. The panel's "
                    "broken instance leaves the first two steps intact and produces a tour of 53 "
                    "against a promise of 6."},
            {"q": "The sweep finds a worst ratio of 10/7 over all 482 small metric instances. Does that show the promise of 2 is too weak?",
             "a": ["Yes: no instance reached 2, so the analysis is loose",
                   "No: the sweep covers four cities and three distance values, and the promise covers every size and every distance",
                   "Yes: a tight bound would be attained somewhere",
                   "No, because 10/7 is greater than 2"],
             "c": 1,
             "why": "A finite family cannot bound an infinite one, and the family here is very "
                    "small. Larger instances can push the ratio closer to 2. The last answer is "
                    "arithmetic nonsense, and the third confuses a tight bound with a bound that "
                    "is attained at every size &mdash; which vertex cover's is and this one's is "
                    "not, at four cities."},
            {"q": "You raise one distance until the triangle inequality fails and the tour comes out at 53 against an optimum of 4. What is the right conclusion?",
             "a": ["The algorithm has a bug",
                   "The guarantee is conditional, and when the condition fails nothing weaker survives &mdash; the ratio is unbounded",
                   "The guarantee becomes a factor of 13 instead of 2",
                   "The optimum was computed wrongly"],
             "c": 1,
             "why": "The algorithm does exactly what it is specified to do; its proof simply no "
                    "longer applies. There is no residual factor, because raising the distance "
                    "further raises the tour as far as the slider reaches while the optimum stays at 4. "
                    "And the "
                    "general problem has no constant-factor approximation at all unless "
                    "`P = NP`, which was proved earlier on this course."},
        ],
        "mistakes": [
            ("Quoting the factor of 2 without checking the input is metric",
             "The hypothesis is a property of the data, not of the algorithm, and it is cheap to "
             "test. Travel times on a road network with one-way streets are not even symmetric; "
             "prices with volume discounts break the inequality. The panel prints a metric verdict "
             "on every redraw for this reason."),
            ("Expecting a weaker guarantee when the hypothesis fails",
             "There is none. The measured ratio on the broken instance is 53/4, and multiplying "
             "that distance again moves it further with nothing to stop it. A conditional "
             "result with a false condition says "
             "nothing, and that is different from saying something weak."),
            ("Reading a small sweep as evidence about the bound",
             "10/7 over 482 instances is a fact about instances with four cities and distances of "
             "1, 2 or 3. It is worth having, and it is not a comment on a bound quantified over "
             "every instance. Report the family with the number, always."),
        ],
        "standard": (
            "Finish when you can run the three steps by hand and say which of them needs the hypothesis.",
            "You should be able to build the tree, write the doubled walk, shortcut it, prove "
            "`MST ≤ OPT` by deleting an edge, identify the shortcut as the step needing the "
            "triangle inequality, test that inequality on given data, and state what survives "
            "when it fails.",
        ),
        "note": (
            "Both guarantees so far have been constants. &ldquo;Charging Every Element&rdquo; has "
            "a guarantee that grows with the instance &mdash; the harmonic number of the universe "
            "&mdash; and an argument that prices each element separately and then adds the prices "
            "up."
        ),
    },

    # ---------------------------------------------------------------- 11
    {
        "slug": "charging-every-element",
        "title": "Charging Every Element",
        "module": "Guarantees, and the lower bound they rest on",
        "one_line": "Price each element at one over the number of new elements its set covered, add the prices, and get the size of the cover exactly.",
        "summary": (
            "Greedy set cover takes the set covering the most uncovered elements. Its guarantee is "
            "not a constant: it is the harmonic number of the universe. The argument prices every "
            "element at the moment it is covered, shows the prices add to the answer exactly, and "
            "then bounds each price separately. On the loaded family greedy takes 3 sets where 2 "
            "suffice, the prices add to 3, and `H` over seven elements is 363/140."
        ),
        "key": [
            "a set covering k new elements charges each of them 1/k",
            "the charges add to the number of sets taken — exactly, every time",
            "",
            "seven elements, three sets:  greedy 3, optimum 2 from 8 subfamilies, ratio 3/2",
            "charges  1/4 · 4 + 1/2 · 2 + 1 · 1 = 3",
            "",
            "H over 7 = 363/140 ≈ 2.593        the bound is H × optimum = 363/70 ≈ 5.186",
        ],
        "key_label": "Seven prices that add to three, and a bound that grows with the universe",
        "concepts_intro": (
            "The first idea is the accounting trick that makes the analysis possible. The second "
            "is why the bound is a harmonic number rather than a constant. The third is what a "
            "logarithmic guarantee is worth in practice, which is more than it sounds."
        ),
        "concepts": [
            ("Pricing turns one number into many",
             "The answer is a count of sets, which is hard to bound directly. So hand each set's "
               "cost of 1 out to the elements it newly covered, equally: a set covering `k` new "
               "elements charges each of them `1/k`. Every set gives away its whole cost and every "
               "element is charged exactly once, so the charges add to the number of sets taken. "
               "Now bounding the answer means bounding a sum of small quantities, and each can be "
               "bounded separately &mdash; which is the move that makes the proof work."),
            ("The bound is a harmonic number because the prices rise",
             "When `r` elements are still uncovered, some set in an optimal cover of size `OPT` "
             "holds at least `r / OPT` of them, and greedy takes a set covering at least as many. "
             "So the element covered when `r` remain pays at most `OPT / r`. Adding over "
             "`r = n` down to `1` gives `OPT · (1/n + ... + 1/1) = OPT · H_n`. The prices rise as "
             "the cover fills up, and the last element can pay as much as `OPT` on its own."),
            ("A logarithm is not a constant, and it is not nothing",
             "`H_n` grows without bound, so unlike vertex cover's factor of 2 this guarantee gets "
             "worse on larger instances &mdash; `H` over seven elements is about 2.59, over a "
             "thousand about 7.49. It is also essentially the best possible: no polynomial "
             "algorithm can do asymptotically better unless `P = NP`, a result quoted here and "
             "proved nowhere in this library. So the growing bound is a property of the problem "
             "and not a weakness of the analysis."),
        ],
        "read_title": "The rule, the charging identity, the harmonic bound, and the family greedy gets wrong",
        "read_intro": "The greedy rule, the pricing, the proof that the prices add to the answer, the bound on each price, and what the lab measured on a family designed to trip it.",
        "body": [
            ("def", ("Set cover, and the greedy rule",
                     "Given a family of sets whose union is a universe, find as few of them as "
                     "possible whose union is still the whole universe. The <strong>greedy "
                     "rule</strong> repeatedly takes a set covering the largest number of "
                     "elements not yet covered, stopping when everything is covered.")),
            ("thm", ("The charges add to the answer",
                     "If each set taken by greedy charges `1/k` to each of the `k` elements it "
                     "newly covers, then the sum of all charges equals the number of sets greedy "
                     "took.")),
            ("proof", ("A set covering `k` new elements distributes `k` charges of `1/k`, which is "
                       "1 in total, so each set hands out exactly its own cost. Every element is "
                       "newly covered exactly once, by the set that first covers it, so no "
                       "element is charged twice and none is missed &mdash; greedy stops only when "
                       "the universe is covered. Summing over sets gives the count; summing over "
                       "elements gives the same number a different way, which is the identity.")),
            ("thm", ("Greedy set cover is within `H_n` of the optimum",
                     "Greedy returns a cover of size at most `H_n · OPT`, where `n` is the size of "
                     "the universe, `OPT` is the size of a smallest cover and `H_n = 1 + 1/2 + "
                     "... + 1/n`.")),
            ("proof", ("Consider the moment an element is covered, with `r` elements uncovered "
                       "including it. An optimal cover of size `OPT` covers all `r`, so one of its "
                       "sets covers at least `r / OPT` of them; greedy takes a set covering at "
                       "least that many new elements, so the charge is at most `OPT / r`.",
                       "The elements are covered in some order; the first is charged at most "
                       "`OPT / n`, the next at most `OPT / (n - 1)`, and so on down to at most "
                       "`OPT / 1` for the last. Adding, the total charge is at most "
                       "`OPT · H_n`. By the identity the total charge is the size of greedy's "
                       "cover, which gives the bound.")),
            ("h3", "What the lab measured"),
            ("p", "The loaded family is `{3,4,5,6}`, `{1,2,3}`, `{4,5,6,7}` over the universe 1 "
                  "to 7. Greedy takes the four-element set first, then needs two more; the "
                  "optimum is 2, found by an exhaustive search over the 8 subfamilies, and it is "
                  "the second and third sets together. The panel reports a realised ratio of 3/2, "
                  "`H` over 7 as 363/140, the bound `H × OPT` as 363/70, the answer inside the "
                  "bound, and the charges adding to the answer exactly."),
            ("p", "The charges are 1/4 to each of the four elements the first set covered, 1/2 to "
                  "each of the two the second set newly covered, and 1 to the single element the "
                  "third set brought in. That is `4 × 1/4 + 2 × 1/2 + 1 = 3`, which is the number "
                  "of sets, and the panel checks the sum rather than showing the prices and "
                  "moving on."),
            ("example", ("The allowance each element was entitled to",
                         "With `OPT = 2` and seven elements, the allowances `OPT / r` for `r` from "
                         "7 down to 1 are `2/7, 1/3, 2/5, 1/2, 2/3, 1, 2`, adding to "
                         "`2 · H_7 = 363/70`. The realised charges are `1/4, 1/4, 1/4, 1/4, 1/2, "
                         "1/2, 1`, and each is at or below its own allowance &mdash; the tightest "
                         "being the first, `1/4` against `2/7`. The bar chart draws each charge "
                         "against the most the analysis allows it.")),
            ("h3", "Why greedy loses here, and why it usually does not"),
            ("p", "The family is built to trip the rule. The four-element set is the largest, so "
                  "greedy takes it first, and afterwards neither of the two sets that together "
                  "cover everything is whole any more: one has two new elements and the other "
                  "one. A rule that had looked ahead would have taken those two and finished. "
                  "This is the same shape as the greedy failure the dynamic programming course "
                  "opened on &mdash; a first choice that is locally best and globally wrong."),
            ("p", "Most families are not like this. Switch to the disjoint partition and the ratio "
                  "is 1 because every cover is the whole family; switch to the one big set with "
                  "singletons under it and greedy takes the big set and stops, which is the "
                  "optimum. The panel's default is the interesting case precisely because it is "
                  "not the common one, and reading 3/2 as typical would be as wrong as reading 1 "
                  "as a guarantee."),
            ("p", "One number here is not a measurement: `H_n` and the bound `H_n · OPT` are the "
                  "proved guarantee evaluated at this instance's numbers. 3/2 was counted. "
                  "363/70 was derived. They sit in the same panel and the gap between them "
                  "&mdash; 1.5 against about 5.19 &mdash; is the usual state of an approximation "
                  "guarantee: comfortable, and not evidence that the bound could be improved."),
        ],
        "lab": ("coping", {"mode": "setcover", "preset": "trap"}),
        "steps_title": "Running the charging argument on a cover you have built",
        "steps_intro": "The accounting is arithmetic. The discipline is checking that it balances before believing the bound.",
        "steps": [
            ("Record how many NEW elements each chosen set covered",
             "Not its size &mdash; its fresh count. A set covering four elements of which two "
             "were already covered charges `1/2`, not `1/4`, and getting this wrong makes the "
             "identity fail in a way that is easy to see and easy to overlook."),
            ("Add the charges and require the sum to be the number of sets",
             "Exactly, as a fraction, not approximately. The identity is the hinge of the "
             "argument: if the sum is not the answer then the quantity being bounded is not the "
             "answer either. The panel prints the verdict as a separate row."),
            ("Bound each charge by `OPT / r` at the moment it was paid",
             "`r` is the number of elements still uncovered when that element was covered, "
             "counting it. This is where the optimum enters the proof &mdash; once, as a bound on "
             "a set size in an optimal cover, and never as something the algorithm computes."),
            ("Add the allowances and recognise the harmonic number",
             "`OPT/n + OPT/(n-1) + ... + OPT/1` is `OPT · H_n`. Keep it exact: `H_7` is 363/140, "
             "and a decimal here would hide that the bound is a sum of unit fractions, which is "
             "the whole reason it is logarithmic."),
            ("Report the realised ratio, the bound and the universe size together",
             "The bound depends on `n`, so quoting a logarithmic guarantee without saying over "
             "what is quoting a function without its argument. The panel prints the universe size "
             "in the same row as the sets."),
        ],
        "worked": {
            "title": "Seven elements, three greedy choices, and the prices that add to three",
            "intro": [
                "The family is `{3,4,5,6}; {1,2,3}; {4,5,6,7}` over the universe 1 to 7. The "
                "optimum is the second and third sets. Greedy takes the largest first.",
            ],
            "lines": [
                "  step   set taken      new elements      charge each",
                "",
                "    1     {3,4,5,6}     3, 4, 5, 6            1/4",
                "    2     {1,2,3}       1, 2                  1/2",
                "    3     {4,5,6,7}     7                     1",
                "",
                "  element   3     4     5     6     1     2     7",
                "  charge   1/4   1/4   1/4   1/4   1/2   1/2    1     total 3",
                "  allowed  2/7   1/3   2/5   1/2   2/3    1     2     total 363/70",
                "",
                "  greedy 3 sets      optimum 2, from 8 subfamilies      ratio 3/2",
                "  H over 7 elements  363/140 ≈ 2.593",
                "  the bound          H × optimum = 363/70 ≈ 5.186        3 ≤ 363/70",
                "  the charges add to the answer                          3 = 3",
            ],
            "after": [
                "The optimum is `{1,2,3}` together with `{4,5,6,7}`, and greedy takes both of them "
                "&mdash; just not first. Its mistake costs exactly one set, and the whole of the "
                "trap is that the largest set overlaps both members of the optimal cover. Remove "
                "the first set from the family and greedy is optimal.",
                "The charge on element 7 is the most anything pays here, and it pays 1 because it "
                "was the last element covered and the set that covered it brought in nothing else. "
                "That is the general pattern: prices rise as the cover fills, and the bound is a "
                "sum of rising prices, which is what makes it harmonic rather than constant.",
                "For a faded rehearsal, load the same trap one size up &mdash; ten elements, five "
                "sets &mdash; and predict the charges before running it. The supplied first move: "
                "greedy takes the six-element set first, charging `1/6` to each. Say how many more "
                "sets it needs, what those charges are, and check that they add to the number of "
                "sets; then compare the ratio with this instance's 3/2 and notice it has not "
                "changed while `H` has.",
            ],
        },
        "quiz_title": "Charges, harmonics and what greedy is guaranteed",
        "quiz": [
            {"q": "A greedy step takes a set of five elements, two of which were already covered. What is the charge on each new element?",
             "a": ["1/5", "1/3", "1/2", "1"],
             "c": 1,
             "why": "The charge is one over the number of NEW elements, which is three. Using the "
                    "set's size instead would hand out only 3/5 of the set's cost and break the "
                    "identity that the charges add to the number of sets &mdash; which is the "
                    "step the whole proof rests on."},
            {"q": "Why do the charges add to the size of greedy's cover exactly?",
             "a": ["Because every set has the same size",
                   "Because each set hands out its whole cost of 1, and each element is newly covered exactly once",
                   "Because the optimum is smaller",
                   "Because `H_n` is a sum of unit fractions"],
             "c": 1,
             "why": "`k` charges of `1/k` add to 1, so each set gives away exactly its cost; and "
                    "an element is charged only by the set that first covers it. Summing over "
                    "sets and summing over elements are two ways of adding the same charges. Set "
                    "sizes vary here, and `H_n` appears later, in the bound on each charge."},
            {"q": "The panel reports a realised ratio of 3/2 and a bound of 363/70. What is the relationship between those two numbers?",
             "a": ["The second is a prediction of the first that came out too high",
                   "The first was counted on this family; the second is the proved bound evaluated at this family's numbers",
                   "The second should be tight, so the analysis is wrong",
                   "They are the same quantity at different precisions"],
             "c": 1,
             "why": "One is a measurement, the other is a theorem evaluated at `n = 7` and "
                    "`OPT = 2`. A guarantee is an upper bound over all instances and is usually "
                    "far from the realised ratio on any particular one. That gap is not evidence "
                    "about the bound's quality in either direction."},
            {"q": "Greedy's guarantee is `H_n`, which grows without limit. What follows about the problem?",
             "a": ["A better algorithm with a constant factor must exist, since vertex cover has one",
                   "The guarantee is essentially the best possible: no polynomial algorithm does asymptotically better unless `P = NP`",
                   "Set cover is harder than the travelling salesman",
                   "The bound can be improved by choosing sets in a different order"],
             "c": 1,
             "why": "The logarithmic factor is a property of the problem rather than of this "
                    "analysis, which is a result quoted on this course and proved nowhere in this "
                    "library. Different problems have different approximability, so vertex "
                    "cover's constant implies nothing here; and reordering the choices does not "
                    "change a worst-case bound."},
        ],
        "mistakes": [
            ("Charging one over the set's size",
             "The denominator is the number of elements the set covers that were not covered "
             "before. Using the size makes the charges add to less than the answer, and the "
             "identity the proof rests on quietly fails while every individual number still looks "
             "plausible."),
            ("Quoting a logarithmic guarantee without the universe",
             "`H_n` is a function of the number of elements, so &ldquo;greedy is within a "
             "logarithmic factor&rdquo; needs to say a logarithmic factor of what. Over seven "
             "elements the bound is about 2.59 and over a thousand about 7.49, and those are very "
             "different promises."),
            ("Reading 3/2 as what greedy usually does",
             "The loaded family was constructed to make greedy lose a set. Three of the panel's "
             "five families give a ratio of 1. The realised ratio is a fact about the family in "
             "the box, and the only statement covering all of them is the bound."),
        ],
        "standard": (
            "Finish when you can run the charging argument on a cover of your own and check that it balances.",
            "You should be able to apply the greedy rule, record fresh counts rather than set "
            "sizes, price each element, verify the prices add to the number of sets exactly, bound "
            "each price by `OPT` over the number of elements then uncovered, and add the "
            "allowances to a harmonic number kept exact.",
        ),
        "note": (
            "Every guarantee so far has been fixed by the algorithm. &ldquo;Accuracy by the "
            "Epsilon&rdquo; is the last strategy and it inverts that: the reader names the "
            "accuracy, and the price is paid in the size of a table."
        ),
    },

    # ---------------------------------------------------------------- 12
    {
        "slug": "accuracy-by-the-epsilon",
        "title": "Accuracy by the Epsilon",
        "module": "Paying for accuracy, and what the numbers settle",
        "one_line": "Divide every value by 451/30, solve the scaled knapsack exactly in 238 cells instead of 3604, and lose nothing at all against a promise of 193.5.",
        "summary": (
            "The last strategy lets the caller choose the accuracy. Scale the knapsack's values "
            "down by a factor tuned to epsilon, solve the scaled instance exactly with the value "
            "table from the dynamic programming course, and read the chosen items back at their "
            "original prices: the loss is at most epsilon times the optimum. On the loaded "
            "instance the promise is 193.5 and the realised loss is 0, and the table is 238 cells "
            "against the exact table's 3604."
        ),
        "key": [
            "K = ε · vmax / n     round every value DOWN by K, solve exactly, keep the items",
            "rounding loses at most K per item, so at most n · K = ε · vmax ≤ ε · OPT in total",
            "",
            "six items, capacity 12, ε = 1/10:   K = 451/30 ≈ 15.033",
            "value 1935 = the optimum, loss 0, against a promise of 387/2 = 193.5",
            "238 cells scaled against 3604 exact",
            "",
            "on five tiny values the scaled table is 171 cells against 32 — it costs more than it saves",
        ],
        "key_label": "One scale factor, a promise of 193.5, and a realised loss of nothing",
        "concepts_intro": (
            "The first idea is what a scheme is, as opposed to a fixed guarantee. The second is "
            "why scaling the values is the right thing to coarsen. The third is the reason a "
            "scheme exists for this problem and not for the travelling salesman."
        ),
        "concepts": [
            ("A scheme takes the accuracy as an input",
             "Vertex cover's factor of 2 and greedy set cover's `H_n` are fixed by the algorithm. "
             "An <strong>approximation scheme</strong> takes `ε > 0` as a parameter and returns an "
             "answer within a factor `1 + ε` of the optimum; it is <strong>fully "
             "polynomial</strong> when the running time is polynomial in the input size and in "
             "`1/ε` together. So the caller names the accuracy and pays for it, and the panel "
             "prints both halves of that trade as two columns of integers."),
            ("Scaling the values, because the table is indexed by value",
             "The knapsack has a table indexed by achievable value, whose size is the sum of the "
             "values, and that is the quantity making it pseudo-polynomial. Divide every value by "
             "`K = ε · vmax / n` and round down, and the table shrinks by a factor of about `K`. "
             "Rounding down loses less than `K` per item and at most `n · K = ε · vmax` in total; "
             "since the best single item fits, `vmax ≤ OPT`, so the loss is at most `ε · OPT`. "
             "Every one of those quantities is an exact fraction on the panel, so the promise is "
             "a number and the loss is compared against it."),
            ("Weak hardness is what makes a scheme possible",
             "This works because the knapsack is only weakly NP-hard: it has an algorithm "
             "polynomial in the magnitude of its numbers, and the scheme's whole job is to make "
             "the numbers small enough for that algorithm to be affordable. A strongly NP-hard "
             "problem has no such algorithm to shrink into, and the travelling salesman has no "
             "constant-factor approximation at all without a hypothesis. The digit-table "
             "reduction earlier on this course is the same distinction seen from the other side."),
        ],
        "read_title": "The scale factor, the exact table it shrinks, and the two costs the sweep prints",
        "read_intro": "What a scheme is, how the scaling works, the proof of the loss bound, what the lab measured at one epsilon and across six, and the instance where the scheme is a net loss.",
        "body": [
            ("def", ("Approximation scheme, and the fully polynomial kind",
                     "A <strong>polynomial-time approximation scheme</strong> is a family of "
                     "algorithms, one per `ε > 0`, each running in time polynomial in the input "
                     "size and returning a value within `1 + ε` of the optimum. It is "
                     "<strong>fully polynomial</strong> when the running time is also polynomial "
                     "in `1/ε`, so that halving the error does not square the cost.")),
            ("h3", "The algorithm"),
            ("ol", [
                "Let `vmax` be the largest value and `n` the number of items. Set "
                "`K = ε · vmax / n`.",
                "Replace each value `v` by the integer part of `v / K`.",
                "Solve the scaled instance exactly with the value-indexed table, which is now "
                "much smaller.",
                "Return the set of items the scaled table chose, valued at their ORIGINAL prices.",
            ]),
            ("p", "The last step is the one to get right. The answer is the set, not the scaled "
                  "number: reporting the scaled optimum would report a value in the wrong units "
                  "and it is the standard way an approximation scheme comes out looking wrong. The "
                  "guarantee is about the original value of the chosen set."),
            ("thm", ("The scheme loses at most `ε` times the optimum",
                     "Let `S` be the set the scaled table chooses and `S*` an optimal set for the "
                     "original instance. Then the original value of `S` is at least "
                     "`OPT - ε · OPT`.")),
            ("proof", ("Write `v'` for the scaled values. For any item, `K · v'(i) ≤ v(i) < K · "
                       "v'(i) + K`, so scaling then rescaling loses less than `K` per item.",
                       "`S` is optimal for the scaled instance, so `v'(S) ≥ v'(S*)`. Multiplying "
                       "by `K` and using the two inequalities, the original value of `S` is at "
                       "least `K · v'(S) ≥ K · v'(S*) > v(S*) - |S*| · K ≥ OPT - n · K`.",
                       "Now `n · K = ε · vmax`, and `vmax ≤ OPT` because the single most valuable "
                       "item is a feasible solution on its own &mdash; assuming it fits, which "
                       "items too heavy to fit are discarded first to ensure. So the loss is at "
                       "most `ε · OPT`.")),
            ("h3", "What the lab measured"),
            ("p", "The instance is six items `3:520, 4:610, 5:805, 2:311, 6:902, 4:455` with "
                  "capacity 12, and epsilon at 1/10. The largest value is 902 and there are six "
                  "items, so `K = 902/60 = 451/30`, about 15.033. The scaled values are 34, 40, "
                  "53, 20, 60 and 30. The scaled table chooses the first three items, whose "
                  "original value is 1935 &mdash; exactly the optimum. The promised loss is "
                  "`ε · OPT = 387/2`, that is 193.5, and the realised loss is 0."),
            ("p", "The cost side is the other column. The exact table is indexed by value from 0 "
                  "to the sum of the values, which is 3603, so 3604 cells. The scaled table needs "
                  "238. That is the whole trade: a promise of losing up to a tenth of the optimum, "
                  "bought with a table one fifteenth the size, and on this instance the promise "
                  "was not called in at all."),
            ("example", ("The epsilon sweep, as two columns",
                         "The panel sweeps `ε = 1, 1/2, 1/4, 1/8, 1/16` and `1/32` and prints the "
                         "cells and the loss at each: 24, 47, 95, 190, 382 and 765 cells, with a "
                         "realised loss of 0 at every one. The cells roughly double as epsilon "
                         "halves, which is what &ldquo;polynomial in `1/ε`&rdquo; looks like as "
                         "integers, and the loss column stays at zero because this instance is "
                         "kind. A promise is an upper bound on the loss and this one is never "
                         "reached.")),
            ("h3", "Where the scheme costs more than it saves"),
            ("p", "Switch to the five small items `3:5, 4:6, 5:8, 2:3, 6:9` with capacity 10 "
                  "&mdash; the instance the branch-and-bound page used. The exact table has 32 "
                  "cells. At epsilon one tenth, `K = 9/50`, which is less than 1, so dividing by "
                  "it makes the values BIGGER: the scaled values are 27, 33, 44, 16, 50 and the "
                  "scaled table needs 171 cells. The scheme is a fivefold loss, and the answer is "
                  "the exact optimum either way."),
            ("p", "This is worth more than a footnote. An approximation scheme is an asymptotic "
                  "device: its saving comes from large values, and on small ones the scaling is "
                  "counterproductive rather than merely useless. The cell counts say so, and "
                  "nothing about the complexity class does. It is also a clean instance of the "
                  "hazard this Subject is built around, in the direction people do not expect "
                  "&mdash; the asymptotically better method losing on the instance on screen."),
            ("p", "One more reading from the same sweep, on that small instance: at `ε = 1` the "
                  "scheme returns 15 against an optimum of 16, a loss of 1 inside a promise of "
                  "16, and at every smaller epsilon it returns 16 exactly. So the only epsilon at "
                  "which the promise was ever needed is the one nobody would choose."),
        ],
        "lab": ("coping", {"mode": "fptas", "preset": "big"}),
        "steps_title": "Using a scheme, and checking what it actually bought",
        "steps_intro": "Five steps, two of which are measurements you should take before believing the scheme is worth running.",
        "steps": [
            ("Choose epsilon from what the answer is for",
             "Epsilon is a business decision, not a mathematical one: it says how much value you "
             "are willing to leave on the table. Write it as an exact fraction, because the scale "
             "factor, the promise and the loss are all computed from it and a rounded epsilon "
             "makes a promise that is not quite the one you were given."),
            ("Compute the scale factor from the largest value and the item count",
             "`K = ε · vmax / n`. The largest value is what sets the coarseness, so one enormous "
             "item coarsens every small one &mdash; the panel has an instance where a single item "
               "of 900 scales five values into 0, 1, 1, 2 and 0."),
            ("Solve the scaled instance exactly, and keep the SET",
             "Run the value-indexed table on the scaled values and record which items it took. "
             "Then value that set at the original prices. Reporting the scaled optimum is "
             "reporting a number in units nobody asked about."),
            ("Compare the realised loss against the promise, and the cells against the exact table",
             "Two comparisons, both available on small instances: the loss against `ε · OPT`, and "
             "the size of the scaled table against the size of the exact one. The first says "
             "whether the guarantee held; the second says whether it was worth having."),
            ("Check that the scale factor is above 1 before bothering",
             "If `K < 1` the scaled values are larger than the originals and the table grows. "
             "That happens whenever `ε · vmax < n`, which on small instances is easy to arrange "
             "by accident, and the panel's small example is exactly that case."),
        ],
        "worked": {
            "title": "Six items at one tenth, and the same items at six epsilons",
            "intro": [
                "Items `3:520, 4:610, 5:805, 2:311, 6:902, 4:455`, capacity 12. The largest value "
                "is 902 and there are six items, so at `ε = 1/10` the scale factor is "
                "`902/60 = 451/30`.",
            ],
            "lines": [
                "  item      weight   value    value / K, rounded down",
                "",
                "   1          3       520            34",
                "   2          4       610            40",
                "   3          5       805            53",
                "   4          2       311            20",
                "   5          6       902            60",
                "   6          4       455            30",
                "",
                "  the scaled table chooses items 1, 2, 3     weight 12 of 12",
                "  their original value                       1935",
                "  the optimum, by exhaustive search          1935        loss 0",
                "  the promise, ε × optimum                   387/2 = 193.5",
                "",
                "  cells in the scaled table      238",
                "  cells in the exact table      3604      (the values add to 3603)",
                "",
                "   ε      cells    loss    promise",
                "   1        24       0      1935",
                "   1/2      47       0      1935/2",
                "   1/4      95       0      1935/4",
                "   1/8     190       0      1935/8",
                "   1/16    382       0      1935/16",
                "   1/32    765       0      1935/32",
            ],
            "after": [
                "The cells double as epsilon halves and the loss column never moves off zero. "
                "Both halves of that are worth noticing: the doubling is the `1/ε` in the running "
                "time appearing as integers, and the zeros are this instance being kind. A "
                "promise is an upper bound on the loss, and a page reporting only the promise "
                "would have told you nothing about what actually happened.",
                "At `ε = 1` the table has 24 cells and still finds the optimum, which looks like "
                "the scheme being free. It is not a general fact: on the five-item instance from "
                "the branch-and-bound page, `ε = 1` loses 1 against an optimum of 16. The "
                "difference is that here the rounding happens not to change which set the table "
                "chooses, and there is no way to know that without computing it.",
                "For a faded rehearsal, load the instance with one dominant value &mdash; `5:900` "
                "among five small items &mdash; and predict the scale factor before running it. "
                "The supplied first move: `vmax` is 900 and there are six items, so at one tenth "
                "`K` is 15. Say what that does to a value of 11, and then check the scaled column "
                "&mdash; and notice which items become indistinguishable from nothing.",
            ],
        },
        "quiz_title": "Scaling, promises and what a scheme costs",
        "quiz": [
            {"q": "Why is the scale factor `ε · vmax / n` rather than just `ε`?",
             "a": ["To keep it an integer",
                   "Because the total rounding loss is at most `n` times the factor, and `vmax ≤ OPT`, so `n · K = ε · vmax` is at most `ε · OPT`",
                   "Because the table is indexed by weight",
                   "Because `vmax` is the optimum"],
             "c": 1,
             "why": "Each item loses less than `K` to rounding, so `n` items lose less than "
                    "`n · K`. Choosing `K` so that `n · K = ε · vmax` and using `vmax ≤ OPT` "
                    "turns that into `ε · OPT`. The factor is a fraction, not an integer; the "
                    "table is indexed by value; and `vmax` is a lower bound on the optimum rather "
                    "than equal to it."},
            {"q": "The scaled table chooses items 1, 2 and 3. What should the algorithm report as its answer?",
             "a": ["The scaled optimum, 127",
                   "The original value of those three items, 1935",
                   "The scaled optimum multiplied by `K`",
                   "The optimum of the original instance"],
             "c": 1,
             "why": "The set is the answer and the guarantee is about its value at the original "
                    "prices. Reporting the scaled number, or the scaled number rescaled, gives a "
                    "quantity in the wrong units and is the commonest way an implementation of "
                    "this scheme looks broken. And the algorithm does not know the true optimum "
                    "&mdash; that is what it is approximating."},
            {"q": "On five small items the exact table has 32 cells and the scaled table has 171. What has gone wrong?",
             "a": ["The implementation is wrong",
                   "Nothing: `K` is below 1 here, so dividing by it enlarges the values &mdash; the scheme is an asymptotic device and this instance is too small for it",
                   "Epsilon was chosen too large",
                   "The exact table was computed incorrectly"],
             "c": 1,
             "why": "With `vmax = 9`, `n = 5` and `ε = 1/10`, `K` is `9/50`, which is less than 1, "
                    "so every value grows on scaling. Everything is computed correctly and the "
                    "answer is exact; the scheme is simply the wrong tool at this size, and only "
                    "the cell counts reveal that. A larger epsilon would shrink the table, which "
                    "is the opposite of the usual direction of the trade."},
            {"q": "Why does the knapsack have a fully polynomial scheme while the general travelling salesman has no constant-factor approximation at all?",
             "a": ["Because the knapsack is easier to state",
                   "Because the knapsack is only weakly NP-hard, so there is an algorithm polynomial in the numbers for the scaling to shrink into",
                   "Because the knapsack has a greedy algorithm",
                   "Because the travelling salesman has no numbers to scale"],
             "c": 1,
             "why": "The whole scheme is a way of making the numbers small enough for the "
                    "pseudo-polynomial table to be affordable, and that table exists only because "
                    "the problem is weakly hard. For the general travelling salesman, a "
                    "constant-factor algorithm would decide the Hamilton circuit problem, which "
                    "was proved on this course by raising the off-edge distance."},
        ],
        "mistakes": [
            ("Reporting the scaled value as the answer",
             "The scheme's output is a set of items, and its guarantee is about that set's value "
             "at the original prices. The scaled optimum is a number about a different instance. "
             "The lab re-values the chosen set from the original items for exactly this reason."),
            ("Assuming a smaller epsilon is always better",
             "Smaller epsilon means a bigger table: 24 cells at `ε = 1` and 765 at one "
             "thirty-second on the loaded instance, with the same answer throughout. The accuracy "
             "you pay for is an upper bound on a loss you may never incur, and the panel prints "
             "the realised loss so the question can be asked."),
            ("Running a scheme on an instance too small for it",
             "If `K` falls below 1 the scaled table is larger than the exact one. Check the scale "
             "factor before running anything: on values in single figures with a handful of items, "
             "the exact table is small and the scheme is pure overhead."),
        ],
        "standard": (
            "Finish when you can run the scheme by hand and say what it bought in cells and what it cost in value.",
            "You should be able to compute `K` from epsilon, the largest value and the item count, "
            "scale and round the values, solve the scaled instance, re-value the chosen set at the "
            "original prices, compare the realised loss against `ε · OPT`, and compare the two "
            "table sizes before deciding the scheme was worth running.",
        ),
        "note": (
            "All six responses are now on the table. One page remains, and it does not add a "
            "seventh: it takes one of the guarantees and measures it on one instance, then on "
            "every instance of a size, then compares both with what was proved &mdash; which is "
            "the question this whole Subject has been circling."
        ),
    },

    # ---------------------------------------------------------------- 13
    {
        "slug": "what-a-measurement-settles",
        "title": "What a Measurement Settles",
        "module": "Paying for accuracy, and what the numbers settle",
        "one_line": "Read a ratio of 4/3 on one graph, 2 over all 63 graphs of a size, and 2 proved over every graph there is, and say what each of the three is worth.",
        "summary": (
            "One algorithm, three numbers. On the five-cycle the 2-approximation for vertex cover "
            "realises 4/3. Over every one of the 63 non-empty graphs on four vertices, each solved "
            "exactly, the worst it realises is 2. And over every graph of every size the proof "
            "gives at most 2. Three statements of increasing strength, and only the last is a "
            "theorem &mdash; which is the hazard this Subject was built around, met one last time "
            "where it matters most."
        ),
        "key": [
            "the five-cycle:  matching 2, optimum 3, cover 4        ratio 4/3",
            "every graph on four vertices:  63 of them, each solved exactly        worst 2",
            "every graph of every size:  proved, at most 2",
            "",
            "a count on one input is not a bound",
            "a count on every input of one size is not a bound either",
            "",
            "the sweep is also implementation-specific; the proof is not",
        ],
        "key_label": "Three claims about one algorithm, in increasing order of strength",
        "concepts_intro": (
            "The first idea is the ladder of three claims and what separates each rung from the "
            "next. The second is a subtlety about what an exhaustive sweep is a sweep over. The "
            "third is the close: what the six strategies have in common."
        ),
        "concepts": [
            ("Three rungs, and two gaps that a computer cannot cross",
             "A ratio measured on the graph in the box is a fact about that graph. A sweep over "
             "every graph of a size is a much stronger fact &mdash; it is a genuine universal "
             "statement, quantified over a finite set that has been exhausted. A bound over every "
             "size is stronger again and no enumeration can reach it, because there are infinitely "
             "many sizes. The first gap is closed by computing more; the second cannot be closed "
             "by computing at all."),
            ("An exhaustive sweep is still a sweep over one implementation",
             "The panel says this itself, and it is the subtlety that makes the third rung "
             "necessary rather than merely tidier. The matching is built greedily in edge order, "
             "so the worst ratio the sweep finds is the worst case of <em>this</em> matching "
             "routine on graphs of that size; a different edge order gives a different matching "
             "and possibly a different ratio. The proof never mentioned the order, so the bound of "
             "2 covers every implementation at once, including ones nobody has written."),
            ("Six responses, and what all of them have in common",
             "Prune an exact search; parameterise the exponential; approximate with a guarantee; "
             "approximate under a hypothesis; buy accuracy by the epsilon; or restrict to a "
             "tractable special case. Each gives something up, and every one of them is defended "
             "the same way: a quantity the algorithm can compute, compared against a claim that "
             "quantifies over inputs. The measurement says what happened; the proof says what can "
             "happen. Neither is a substitute for the other, and this course has printed them "
             "side by side on every page."),
        ],
        "read_title": "The three claims, the sweep's fine print, and the close",
        "read_intro": "The measured ratio, the exhaustive sweep, the proved bound, what separates them, and the six responses this course built.",
        "body": [
            ("p", "The graph is the five-cycle. The maximal matching takes two edges, the cover "
                  "takes their four endpoints, the optimum is three, and the realised ratio is "
                  "4/3 against a promise of 2. Everything about that sentence is measured except "
                  "the promise."),
            ("h3", "The three claims, written out"),
            ("math", [
                "on this graph          cover 4, optimum 3            ratio 4/3",
                "on every graph on 4 vertices   63 graphs, each solved exactly    worst 2",
                "on every graph, every size     proved from the matching          at most 2",
            ]),
            ("p", "The middle row is the one this library can rarely produce, and it is worth "
                  "being clear about how strong it is. It is not a sample. Every non-empty graph "
                  "on four vertices is examined &mdash; there are `2^6 - 1 = 63` of them, one per "
                  "non-empty subset of the six possible edges &mdash; and each is solved exactly "
                  "by enumerating subsets of its vertices. So it is a universal statement over a "
                  "finite domain, and 49 of the 63 attain the worst ratio of 2."),
            ("p", "It still is not the theorem. Five vertices gives 1023 graphs and the worst "
                  "ratio is again 2; three vertices gives 7 and the answer is again 2. Three "
                  "sizes, three exhaustive answers, all equal to the proved bound &mdash; and the "
                  "bound holds for sizes no enumeration will ever reach, for a reason that has "
                  "nothing to do with any of the three counts: the matched edges are disjoint, so "
                  "any cover needs a vertex from each, and the algorithm takes exactly two per "
                  "edge."),
            ("def", ("Tight",
                     "A bound is <strong>tight</strong> when some instance attains it, so the "
                     "constant cannot be lowered without changing the algorithm. The sweep is how "
                     "this page establishes tightness: it produces the attaining instances rather "
                     "than asserting that they exist, and it reports both the first in edge order "
                     "&mdash; a single edge &mdash; and the densest, which on four vertices has "
                     "five edges.")),
            ("p", "Reporting both witnesses is not fussiness. A reader shown only the single edge "
                  "concludes that the factor of 2 is an artefact of a degenerate case and that "
                  "real graphs are fine. The five-edge witness on four vertices, and the "
                  "seven-edge witness at five vertices, say otherwise: the worst case lives among "
                  "dense graphs too."),
            ("h3", "What this course did with the numbers"),
            ("p", "Every page here has put a measured quantity beside a claim the measurement "
                  "cannot establish, and said which is which. The reductions measured the map on "
                  "solutions and proved the equivalence of answers. Branch and bound measured node "
                  "counts and proved only that the bound cannot cut the optimum. The "
                  "parameterised search measured nodes and printed `2^k · n` beside `2^n` as "
                  "expressions. The four guarantees each measured a realised ratio and printed the "
                  "promise beside it, and never a ratio without the optimum it was a ratio to."),
            ("ul", [
                "<strong>Prune an exact search.</strong> Built in &ldquo;A Bound the Search Can "
                "See&rdquo;: 14 nodes against 44, one answer, and a bound that is proved never to "
                "cut the optimum.",
                "<strong>Parameterise the exponential.</strong> Built in &ldquo;Parameterising the "
                "Budget&rdquo;: 9 nodes against a tree bound of 16, and `2^k · n` against `2^n` "
                "with both computed &mdash; one of the panel's instances has the first larger.",
                "<strong>Approximate with a guarantee.</strong> Built in &ldquo;Twice a "
                "Matching&rdquo; and &ldquo;Charging Every Element&rdquo;: a constant factor "
                "proved against a matching, and a harmonic factor proved by pricing every "
                "element.",
                "<strong>Approximate under a hypothesis.</strong> Built in &ldquo;The Hypothesis "
                "Doing the Work&rdquo;: within 2 when the triangle inequality holds, and a tour "
                "of 53 against an optimum of 4 when it does not.",
                "<strong>Buy accuracy by the epsilon.</strong> Built in &ldquo;Accuracy by the "
                "Epsilon&rdquo;: 238 cells against 3604, a promise of 193.5, a realised loss of "
                "nothing &mdash; and an instance where the scheme costs five times what it saves.",
                "<strong>Restrict to a tractable special case.</strong> Named in &ldquo;Twice a "
                "Matching&rdquo; for bipartite graphs, where K&ouml;nig's theorem gives the exact "
                "cover in polynomial time, and in &ldquo;Numbers as Gadgets&rdquo; for subset sum "
                "with bounded values.",
            ]),
            ("p", "The path ends here, and the position is worth stating plainly. Data structures "
                  "paid for the operations everything else spends; sorting made the analysis "
                  "probabilistic; graphs supplied the algorithms that certify their own answers; "
                  "greedy methods and dynamic programming are two answers to one question about "
                  "optimal substructure; strings, geometry and randomisation applied all of it to "
                  "one world each. This course needed every one of them &mdash; the "
                  "probabilistic method, subset sum's table, K&ouml;nig's theorem and both proof "
                  "templates &mdash; because an approximation ratio is a stays-ahead argument "
                  "against a lower bound, and a reduction is a construction you have to be able "
                  "to build."),
            ("p", "And the discipline that ran through all of it is the sentence in the footer of "
                  "every page: a count is measured by running the algorithm on the input shown, "
                  "and a count on one input is not a bound. This page adds the only refinement it "
                  "ever needed. A count on every input of one size is not a bound either. It is a "
                  "great deal better than one count, it is the strongest thing a computer can "
                  "hand you, and it is still not a quantifier over all sizes. That last step is "
                  "the one you take with a proof, and it is why every lab on this path has a "
                  "theorem printed next to it."),
        ],
        "lab": ("coping", {"mode": "vertexcover", "preset": "cycle5"}),
        "steps_title": "Reading any measurement on any of these pages",
        "steps_intro": "Four questions, in this order, for every number a lab hands you.",
        "steps": [
            ("Ask what the number is about",
             "One instance, every instance of a size, or every instance? The three are different "
             "kinds of claim and they are printed in the same typeface. The panel here labels its "
             "rows &ldquo;one graph&rdquo;, &ldquo;63 graphs&rdquo; and &ldquo;every graph, of "
             "every size&rdquo; for exactly this reason."),
            ("Ask what the denominator is",
             "A ratio without the quantity it is a ratio to is not a measurement. If the optimum "
             "is not on the page, the fraction above it has an invented denominator, and no "
             "arrangement of the other numbers repairs that."),
            ("Ask whether it was counted or evaluated",
             "A node count was counted. `2^k · n`, `H_n` and `ε · OPT` are expressions evaluated "
             "at this instance's numbers. Both belong on the page and they answer different "
             "questions, and a sentence mixing them is a sentence about nothing."),
            ("Ask what would change it",
             "Move the slider, switch the preset, break the hypothesis. A measurement that "
             "survives every instance you can reach is worth having and is not a bound; a "
             "measurement that changes when you move one control was never more than a fact about "
             "one input. Either way, the thing that settles the general claim is the proof beside "
             "it."),
        ],
        "worked": {
            "title": "One graph, sixty-three graphs, and every graph",
            "intro": [
                "The graph in the box is `1-2, 2-3, 3-4, 4-5, 5-1`. The sweep below is over every "
                "graph on four vertices and does not depend on it.",
            ],
            "lines": [
                "  the five-cycle",
                "     matching       2 edges       1-2 and 3-4",
                "     cover          4 vertices    1, 2, 3, 4",
                "     optimum        3 vertices    by exhaustive search",
                "     ratio          4/3           against the promised 2",
                "     chain          2 ≤ 3 ≤ 4 ≤ 4",
                "",
                "  every graph on four vertices",
                "     graphs searched       63       one per non-empty edge subset",
                "     each solved exactly   yes      by enumerating vertex subsets",
                "     worst ratio           2        attained by 49 of the 63",
                "     first witness         1-2",
                "     densest witness       1-2, 1-3, 1-4, 2-3, 3-4",
                "",
                "  every graph, of every size",
                "     proved bound          2        from disjointness and maximality",
                "     instances examined    none",
                "",
                "  three vertices    7 graphs      worst 2",
                "  five vertices  1023 graphs      worst 2",
            ],
            "after": [
                "The five-cycle's chain has slack in exactly one place: the matching is 2 and the "
                "optimum is 3, so the cover of 4 comes in under the promise of 4 only because "
                "twice the matching happens to equal it. An odd cycle cannot be covered by a "
                "perfect matching's endpoints, and that is where the 4/3 rather than 2 comes "
                "from.",
                "Three exhaustive sweeps at three sizes all return 2, which is as much agreement "
                "between measurement and proof as this library can produce. It is worth enjoying "
                "and it is worth being precise about: the proof would still be the only reason to "
                "believe the bound at six vertices, and the slider stops at five &mdash; six "
                "vertices would be 32767 graphs to solve exactly.",
                "For a faded rehearsal, and as the last exercise on this path: predict the worst "
                "ratio at three vertices before moving the slider, and then say what you would "
                "have to do to establish it at a hundred. The supplied first move: a single edge "
                "is a graph at every size and realises exactly 2, so the worst ratio is at least "
                "2 at every size, and the proof says it is at most 2. Write down which of those "
                "two facts a computer gave you.",
            ],
        },
        "quiz_title": "One instance, one size, all sizes",
        "quiz": [
            {"q": "The sweep examines all 63 non-empty graphs on four vertices and reports a worst ratio of 2. Which claim does that establish?",
             "a": ["The algorithm's ratio is at most 2 on every graph",
                   "The ratio is exactly 2 on every graph of four vertices",
                   "No graph on four vertices makes this implementation do worse than 2, and 49 of them attain it",
                   "The bound of 2 is proved"],
             "c": 2,
             "why": "It is a universal statement over a finite domain that was exhausted, and "
                    "attainment is what makes the bound tight. It says nothing about other sizes, "
                    "and it is not the proof &mdash; and the ratio is certainly not 2 on every "
                    "graph of that size, since the panel's own five-cycle gives 4/3 at a "
                    "different size and many four-vertex graphs give 1."},
            {"q": "Why does the proof cover implementations the sweep does not?",
             "a": ["Because the proof is about larger graphs",
                   "Because the sweep uses a greedy matching in edge order, while the proof uses only disjointness and maximality",
                   "Because the proof assumes the graph is bipartite",
                   "Because the sweep only checks graphs with an edge"],
             "c": 1,
             "why": "The argument needs the matched edges to be disjoint and the matching to admit "
                    "no further edge; it never refers to how the matching was chosen. So it holds "
                    "for every maximal matching, including ones produced by rules nobody has "
                    "written, while the sweep measured one routine. The panel states this caveat "
                    "itself."},
            {"q": "A lab reports a ratio of 4/3 with no other number beside it. What is missing?",
             "a": ["The promise",
                   "The optimum the ratio is a ratio to",
                   "The instance size",
                   "The lower bound"],
             "c": 1,
             "why": "Without the denominator the fraction is unverifiable: the same numerator over "
                    "a guessed optimum is a different number. This course's rule is that no ratio "
                    "is printed without the optimum it is a ratio to, and every mode of both kits "
                    "computes both halves. The promise, the size and the lower bound are all worth "
                    "having too, and none of them rescues a ratio with an invented denominator."},
            {"q": "Which of the six responses to a hard problem keeps an exact answer?",
             "a": ["Only pruning an exact search",
                   "Pruning an exact search, parameterising, and restricting to a tractable special case",
                   "All of them except the approximation scheme",
                   "None: hardness means exactness is impossible"],
             "c": 1,
             "why": "Branch and bound returns the optimum and proves it; a bounded search tree "
                    "answers the exact yes-or-no question about a budget; and a special case such "
                    "as bipartite vertex cover has an exact polynomial algorithm. The three "
                    "approximation strategies give up exactness by design, and the scheme lets you "
                    "choose how much. Hardness rules out fast exactness in the worst case, not "
                    "exactness."},
        ],
        "mistakes": [
            ("Treating an exhaustive sweep over one size as the theorem",
             "It is the strongest thing a computer can give you and it is not a quantifier over "
             "sizes. Three sweeps here agree with the proved bound at three sizes, which is "
             "reassuring and is not a proof; there are infinitely many sizes and the fourth one is "
             "already refused by the cap."),
            ("Forgetting that the sweep measured one implementation",
             "The worst ratio found is the worst case of a greedy matching in edge order. A "
             "different order is a different algorithm with the same guarantee, and only the proof "
             "covers both. This is the one place where a proof is not merely more general than a "
             "measurement but about a different object."),
            ("Reading a comfortable realised ratio as a better guarantee",
             "4/3 on this graph, 10/7 on the metric tour, 3/2 on the set cover family: every "
             "realised ratio on this course came in well inside its promise, and not one of them "
             "improves a promise. The guarantee is what holds when the instance is chosen by "
             "someone who wants you to fail."),
        ],
        "standard": (
            "Finish when you can say, of any number on any page of this path, what it is a number about.",
            "You should be able to distinguish a ratio measured on one instance, a worst case "
            "found by exhausting a finite family, and a bound proved over all instances; name the "
            "denominator every ratio needs; separate a counted quantity from an evaluated "
            "expression; and state which of the six responses to a hard problem keeps exactness "
            "and what each of the others gives up.",
        ),
        "note": (
            "That is the whole of this Subject, and the last page of this path. What a reader "
            "leaves with is not a catalogue of algorithms but a habit: every number comes with the "
            "question of what it is a number about, and the answer is either an input, a finite "
            "family that was exhausted, or a theorem. The labs can give you the first two. The "
            "third is why the proofs are on the page beside them."
        ),
    },
]
