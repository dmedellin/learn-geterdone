"""Greedy Algorithms and Matroids."""


from . import part_a, part_b


COURSE = {
    "slug": "greedy-and-matroids",
    "title": "Greedy Algorithms and Matroids",
    "level": "Advanced",
    "summary": (
        "Four plausible rules for the same problem, three of them wrong; the two proof "
        "templates that separate a rule that works from a rule that has not failed yet; the "
        "theorem that says exactly which families greedy solves for every weighting; and the "
        "problems where the rule keeps its answer and loses the guarantee."
    ),
    "blurb": (
        "This is the one course on the path where a lesson can do better than putting a "
        "measured count beside a proved bound. A greedy rule commits to a choice and never "
        "revisits it, so on a small instance the optimum is enumerable &mdash; and every "
        "verdict here is computed twice, once by running the rule and once by a search that "
        "has never heard of it. When the two disagree the lab names the subset that beats the "
        "rule, which is what a counterexample looks like when it is produced rather than "
        "quoted."
    ),
    "key": [
        "greedy: take the next feasible thing by some rule, and never undo a choice",
        "stays ahead     gᵢ ≤ oᵢ at every step i,  from an optimum computed separately",
        "exchange        turn an optimum into greedy's answer one swap at a time",
        "matroid  ⟺  greedy is optimal for EVERY weighting        Rado and Edmonds",
        "fractional 240,  0/1 optimum 220,  density greedy 160    one instance, three numbers",
        "max(greedy, best single item) ≥ OPT / 2        a ratio proved against a bound",
    ],
    "assumes_short": "Kruskal and the cut property, heaps, union–find, big-O",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Greedy Algorithms, Trees, Spanning Trees "
        "and Minimum Spanning Trees, Bipartite Graphs, Big-O, Big-Omega and Big-Theta, "
        "Analysing Iterative Algorithms, Loop Invariants and Program Correctness, and Strong "
        "Induction; from the data structures course on this path, Priority Queues and Binary "
        "Heaps and Union–Find; and from Graph Algorithms, The Cut Property and Kruskal's "
        "Algorithm, which are the instance the matroid theorem generalises and are assumed "
        "rather than restated here"
    ),
    "outcomes_intro": (
        "By the end you can tell a greedy rule that is proved from one that has merely "
        "survived the instance in front of you, run both proof templates by hand, decide "
        "whether a family is a matroid by testing the exchange property, and state what an "
        "approximation guarantee does and does not promise."
    ),
    "outcomes": [
        ("Judge a rule against an optimum, not against your intuition",
         "Run four selection rules on one instance, check each selection feasible before "
         "reading its size, and put every size beside the best of all `2ⁿ` subsets &mdash; "
         "then find, for each losing rule, the instance that exposes it."),
        ("Run the two proof templates",
         "Stays-ahead, step by step against an independently computed optimum; and the "
         "exchange argument, performed as a sequence of swaps with feasibility rechecked "
         "after each. Both break on a wrong rule at a named step, and the step is where the "
         "textbook proof stops working."),
        ("Decide whether greedy is right for a whole family",
         "Test the exchange property on every ordered pair of independent sets, say whether "
         "the family is a matroid, and &mdash; when it is not &mdash; produce the weighting "
         "on which greedy loses rather than asserting that one exists."),
        ("Say what a guarantee actually promises",
         "Separate stable from fair, optimal-offline from implementable, and "
         "at-least-half-the-optimum from good. Each of the last three lessons is one "
         "algorithm whose guarantee is real and is not the one a reader expects."),
    ],
    "syllabus_intro": (
        "Interval scheduling first, because it is where a rule can be judged against an "
        "enumerated optimum and where both proof templates are short enough to run by hand; "
        "then Huffman, the one construction here whose optimality is proved by induction on "
        "the tree; then matroids, which say which families have this property at all; then "
        "three problems whose guarantees are each weaker than they sound, ending on the one "
        "that hands the next course its subject."
    ),
    "how_to": [
        "Change the instance before you believe the verdict. Every lab on this course ships "
        "an instance on which the rule under discussion is right and another on which it is "
        "wrong, and the only difference between them is the input. A rule that reaches the "
        "optimum on the instance you were given has been tested once.",
        "Read &ldquo;feasible&rdquo; and &ldquo;large&rdquo; as separate questions. Every "
        "panel here checks the selection it reports before it reports its size, because a "
        "rule that returned a big infeasible set would otherwise look like the winner and "
        "the size alone cannot tell you.",
        "When a rule fails, find the step. &ldquo;It is only a heuristic&rdquo; is not a "
        "finding. Both proof templates in this course break at a named point on a wrong "
        "rule, and that point &mdash; a swap that makes the set overlap, a step where greedy "
        "falls behind &mdash; is the thing worth writing down.",
        "Distrust a caption. Several of the grey notes under these panels were written from "
        "an expectation rather than from a run, and three of them say something the table "
        "directly above them contradicts. Where a lesson here quotes a figure it was read "
        "off the lab, and where the two disagree the lesson says so.",
    ],
    "not_covered": [
        "Greedy set cover and its `ln n` ratio. It is an approximation argument charged "
        "against a lower bound rather than a claim of optimality, and it belongs with the "
        "other approximation ratios in Intractability and Approximation rather than here.",
        "Matroid intersection, matroid union, and the greedy algorithm for weighted matroid "
        "intersection. The single-matroid theorem is what explains Kruskal, and the "
        "intersection theory is a subject rather than a lesson.",
        "Scheduling to minimise lateness, and the whole family of one-machine objectives. "
        "The exchange argument they use is the one performed here on intervals, and running "
        "it twice on two problems teaches the template once.",
        "Competitive analysis as a discipline &mdash; the `k`-competitiveness of LRU, "
        "randomised marking, and the lower bound for deterministic paging. The offline "
        "optimum is built and measured here; the ratio against it for every trace is not "
        "proved anywhere in this library.",
    ],
    "footer_lead": (
        "Every verdict on this course was computed twice: once by running the greedy rule, "
        "and once by a search that does not know what the rule is. The optima are exact "
        "&mdash; the best of every subset, every full binary tree on `n` leaves against every "
        "assignment of the weights to its leaves, every one of the `n!` matchings, every "
        "eviction decision a cache of that size could make, every weighting in `{1, 2, 3}ⁿ`. "
        "Two quantities are genuinely fractional and both are printed as fractions first: a "
        "Huffman code's expected length, and the fractional knapsack's optimum. A decimal "
        "beside a fraction on these pages is a rounding of the printing at a stated number of "
        "places, and the fraction next to it is the number. Where a search would be too large "
        "the panel refuses and says so rather than printing a figure it cannot stand behind, "
        "and where a panel's own caption disagrees with the table above it, the lesson names "
        "the caption."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
