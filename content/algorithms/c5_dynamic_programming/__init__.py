"""Dynamic Programming and Optimal Substructure."""


from . import part_a, part_b


COURSE = {
    "slug": "dynamic-programming",
    "title": "Dynamic Programming and Optimal Substructure",
    "level": "Advanced",
    "summary": (
        "A table, an order to fill it in, and a recurrence &mdash; and the part that goes "
        "wrong is never the recurrence. Optimal substructure discharged by substitution, "
        "overlapping subproblems counted rather than asserted, fill orders that finish and "
        "answer wrongly, reconstructions re-costed and performed, and three tables whose "
        "index is not a number at all."
    ),
    "blurb": (
        "Greedy Algorithms and Matroids proved a rule correct wherever the structure allowed "
        "it. This course is what to do where it does not: the same optimal substructure, "
        "without the greedy choice property, evaluated by filling a table. Every page runs "
        "the table against at least one route that has no table in it &mdash; an exhaustive "
        "search, a memo-free recursion, or a re-costing of the object that came back "
        "&mdash; because a filled table is the easiest thing on this path to get confidently "
        "wrong."
    ),
    "key": [
        "optimal substructure   an optimum contains an optimum of the part",
        "overlapping subproblems   22 089 calls, 18 distinct arguments",
        "a table, an ORDER, a recurrence   -   the order is the part that fails silently",
        "an unwritten cell reads as nothing, and nothing plus a number is a number",
        "n²2ⁿ beats (n−1)! only from ten cities up",
    ],
    "assumes_short": "Greedy and the exchange argument, induction, recurrences",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Dynamic Programming and Greedy "
        "Algorithms, where both were met on one example each; Strong Induction, which every "
        "correctness proof here uses; Recurrence Relations; Big-O, Big-Omega and Big-Theta; "
        "Analysing Iterative Algorithms; and Trees. From this path: Greedy Algorithms and "
        "Matroids, whose exchange arguments and fractional knapsack are the thing this "
        "course starts by breaking, and Graph Algorithms, for the relaxation step and for "
        "shortest paths in a directed acyclic graph, which is a dynamic program in the "
        "language of graphs"
    ),
    "outcomes_intro": (
        "By the end you can turn a problem into a table by naming its state, prove the "
        "recurrence by substitution, derive the fill order from the reads rather than from "
        "habit, and check every object a table hands back by a route that shares nothing "
        "with it."
    ),
    "outcomes": [
        ("Name the state, and know what you have chosen",
         "A subproblem is an index: a remaining amount, a pair of prefixes, an interval, a "
         "vertex with a yes-or-no, a subset with an end point. The choice fixes the table's "
         "size and the bound, and two correct choices for one problem can differ by a factor "
         "of four in cells."),
        ("Prove the recurrence and derive the order from it",
         "Discharge optimal substructure by substituting a better part and deriving a "
         "contradiction, then read the fill order off the cells each cell reads &mdash; and "
         "check it by counting the reads that landed on cells not yet written, where the "
         "only acceptable count is zero."),
        ("Check what a table hands back without using the table",
         "Re-weigh a set of items against the capacity it claims to fit, re-cost a "
         "bracketing from the dimensions, perform an edit script character by character, "
         "close a tour before measuring it, and test an independent set against the edge "
         "list as it was typed."),
        ("Put a measured count beside a proved bound and say where they part",
         "Four pages here have the asymptotically better method losing on the instance "
         "shown, by factors from 1.2 to more than forty; two have the same recurrence in two "
         "loop orders at identical cost answering different questions. Neither number is "
         "wrong and neither is the other."),
    ],
    "syllabus_intro": (
        "The recurrence first, on the smallest problem where a greedy rule already fails; "
        "then the memo and the table as two ways of evaluating it; then the fill order, "
        "twice, because that is the part that fails without saying so; then two-axis grids "
        "and the objects read back out of them; then sequences and counting, where the loop "
        "order decides the question rather than the cost; and last, three tables indexed by "
        "a tree, by the positions of a game, and by subsets."
    ),
    "how_to": [
        "Read every count as a measurement on the input on screen. The table is not the "
        "faster method on four of the twelve instances this course loads by default, and the "
        "bounds do not change between the instance where it wins and the instance where it "
        "loses. Every page prints both and names the gap.",
        "Write the fill order down beside the recurrence. It is the third of the three parts "
        "and the only one that can be wrong while every symptom looks like success: "
        "&ldquo;The Fill Order Is Part of the Algorithm&rdquo; has a complete table, "
        "consistent arithmetic in every cell, and a number 41 per cent below the truth.",
        "Treat the value and the object as two answers. A table can be right about what the "
        "optimum costs and wrong about what it is, and every reconstruction on this course "
        "is checked by a route that does not read the table &mdash; re-costing, re-weighing, "
        "or in one case running the answer as a program.",
    ],
    "not_covered": [
        "The Bellman equations, policies, and discounting. Sequential decision under "
        "uncertainty is a dynamic program over states and actions, and it belongs to "
        "Operations Research rather than here; every problem on this course is "
        "deterministic and every table is filled once.",
        "Convex hull and divide-and-conquer optimisations, the Knuth&ndash;Yao speedup, and "
        "the monotonicity conditions they need. They lower a `Θ(n³)` fill to `Θ(n²)` without "
        "changing a correctness argument, and none of the bounds this course states depends "
        "on them.",
        "Bitmask dynamic programming beyond one example, and profile methods over grid "
        "columns. &ldquo;Subsets as a Table, and Where the Table Loses&rdquo; shows that a "
        "subset is a legitimate index; the catalogue of problems for which that is the right "
        "index is a different skill from proving a recurrence.",
        "Space-efficient reconstruction. One row gives the value and cannot give the object, "
        "and recovering the object in linear space needs a divide-and-conquer argument that "
        "is stated nowhere here &mdash; the trade is named and the alternative is not built.",
    ],
    "footer_lead": (
        "Every count on this course is produced by running the algorithm on the input you "
        "typed. Call counts, cell counts, reads, comparisons, table entries and distances "
        "are exact integers; the two ratios that are printed as ratios &mdash; the calls a "
        "memo saves and Held-Karp's work against brute force's &mdash; are exact fractions, "
        "with a decimal beside them at a stated number of places for reading. Counts of ways "
        "are arbitrary-precision integers and are never converted: the number of ordered "
        "ways to make 100 from 1, 2 and 5 has twenty-three digits, and a page holding it as "
        "a double would print a number that is merely close. Every table on this course is "
        "checked against at least one route that contains no table &mdash; an exhaustive "
        "enumeration at a cap the page states, a memo-free recursion, or a re-costing of the "
        "object that came back &mdash; and where an exhaustive check is refused for being "
        "too large, the page says so rather than reporting a number with nothing behind it. "
        "The two work figures on the travelling-salesman page are the expressions `n²2ⁿ` and "
        "`(n−1)!` evaluated at the number of cities on screen; they are bounds printed as "
        "integers, not measurements, and the page says which of the figures beside them are "
        "measured."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
