"""The Algorithms path, as data.

Nine courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.

Discrete Mathematics analysed algorithms; this path builds them, proves them
and measures them. Every count a lesson prints is produced by executing the
algorithm in the browser and incrementing a counter, never by quoting its
complexity class -- the measured column and the proved bound sit beside each
other, and where they diverge the lesson says why.
"""

from . import (
    c1_data_structures,
    c2_sorting,
    c3_graphs,
    c4_greedy,
    c5_dynamic_programming,
    c6_strings,
    c7_geometry,
    c8_randomised,
    c9_intractability,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_data_structures.COURSE,
    c2_sorting.COURSE,
    c3_graphs.COURSE,
    c4_greedy.COURSE,
    c5_dynamic_programming.COURSE,
    c6_strings.COURSE,
    c7_geometry.COURSE,
    c8_randomised.COURSE,
    c9_intractability.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "algorithms",
    "title": "Algorithms",
    "level": "Advanced",
    "level_note": 'assumes Discrete Mathematics in full',
    "tagline": (
        'The structures every program stands on, the algorithms that run on them, the proof that each is correct and its bound tight, and the six honest responses to a problem that has no fast algorithm. Every count on this path is produced by running the algorithm on the input in front of you. Nine courses and 109 lessons are available.'
    ),
    "description": (
        'The Algorithms Subject: nine courses in one order, from the data structures and their cost models through sorting and selection, graphs and flow, greedy methods and matroids, dynamic programming, strings, geometry, randomisation, and the NP line with everything that can honestly be done about it. Discrete Mathematics analysed algorithms; this path builds them, proves them, and measures them. Every lesson closes on a count the reader produces in the lab and a claim the lab cannot establish. All nine courses and 109 lessons are available.'
    ),
    "key": [
        "heap: parent ≤ children      ⟹  insert, extract-min in O(log n)",
        "E[comparisons] = 2(n+1)Hₙ − 4n   randomised quicksort, on EVERY input",
        "relax(u, v):  d[v] = min(d[v], d[u] + w(u, v))",
        "max flow = min cut           the algorithm certifies its own optimality",
        "A ≤ₚ B:  hardness flows from A to B, never the other way",
        "|cover| ≤ 2|M| ≤ 2·OPT       a ratio is proved against a lower bound",
    ],
    "sequence_intro": (
        'Each course assumes the ones before it and Discrete Mathematics in full, and nothing else. Data Structures pays for the operations Sorting and Graph Algorithms spend; Greedy and Dynamic Programming are two answers to the same question about optimal substructure, in that order because the boundary greed fails at is where the table begins; Strings, Geometry and Randomised Algorithms each apply the first five courses to one world; and Intractability consumes all eight.'
    ),
    "why_order": [
        'Data Structures comes first because every later bound is quoted in terms of one. Prim and Dijkstra are a heap with a schedule, Kruskal is union&ndash;find with a sort, and the sweep line of the geometry course is a search tree that changes as the line moves. A reader who has not costed a heap operation by running it will read `O(E log V)` as a label rather than as a count of something.',
        'Sorting and Selection comes second because it is where the analysis becomes probabilistic. Randomised quicksort&rsquo;s exact expectation is the model for every argument in Randomised Algorithms, and the comparison lower bound Discrete Mathematics proved is used twice more here &mdash; by the adversary arguments and by the convex-hull lower bound &mdash; as a thing to reduce <em>to</em>.',
        'Graph Algorithms precedes Greedy Algorithms and Matroids rather than following it, because the cut property and Kruskal are the instance the matroid theorem generalises, and a general theorem read before its instance is a definition rather than an insight. Dynamic Programming then follows Greedy for the same reason in the other direction: 0/1 knapsack is interesting because the density rule that solved the fractional problem has just failed on it.',
        'Strings, Geometry and Randomised Algorithms are three applications of the first five courses and could be taken in any order; they sit here so that Intractability and Approximation, which needs all of them, comes last. It needs the probabilistic method to derandomise, subset-sum&rsquo;s dynamic program to explain weak NP-hardness, K&ouml;nig&rsquo;s theorem to explain a tractable special case, and the two proof templates because an approximation ratio is a stays-ahead argument against a lower bound.',
    ],
    "prerequisites": [
        'Discrete Mathematics in full, and its course on Algorithms and Complexity as a hard prerequisite. Specifically: big-O with witnesses, analysis of iterative algorithms, recursion trees and amortised analysis, the master theorem, the comparison lower bound, greedy and dynamic programming on one example each, complexity classes and reductions as definitions. Also, by name: strong and structural induction, recurrence relations, loop invariants; expected value, linearity of expectation, independence, variance, the geometric distribution; modular arithmetic and exponentiation, Fermat and Euler, the seeded generator; Graphs and Trees in full; satisfiability and normal forms. Each course names the slugs it uses.',
        'From Algebra, only `the-coordinate-plane` and the 2&times;2 determinant, both for Geometric Algorithms, and the determinant is defined inline there so that a reader who has not taken Algebra&rsquo;s Systems and Matrices loses nothing.',
        'No programming. Every lesson reads pseudocode in Discrete Mathematics&rsquo; conventions &mdash; one-based indices, `=` for assignment &mdash; and none asks you to write or run code. The labs execute the algorithm so that you can watch it and count what it does.',
        'Willingness to distrust a count you just watched. The lab measures cases; the lesson proves a claim about all of them. Every misconception on this path is a case mistaken for a class &mdash; a hash table that was fast on the keys you tried, a pivot rule that survived the inputs you chose, an approximation that matched the optimum on the instance in front of you.',
    ],
    # Each path's hazard is its own. Discrete Mathematics' is that a worked
    # example is not a proof; Algebra's is the invented law; System Design's is
    # the model that answers confidently about a system it does not describe.
    # This path's is narrower and sharper: a lab can execute an algorithm on an
    # input, and no number of inputs is a quantifier.
    "material": (
        "every count is measured by running the algorithm on the input shown, "
        "and a count on one input is not a bound."
    ),
    "footer_lead": (
        '<strong>Educational course material.</strong> Every count on this path is produced by executing the algorithm in your browser and incrementing a counter, never by quoting its complexity class: the measured column and the proved bound sit beside each other, and where they diverge the lesson says why. Comparison counts, exact expectations, Huffman code lengths, collision and false-positive probabilities, contraction success probabilities, set-cover charges, orientation determinants and polygon areas are exact integers or exact fractions, not decimals that are nearly them. Four quantities on the path are genuinely approximate and every lesson that prints one says so and how: linear probing&rsquo;s clustering curve, the asymptotic `2 ln n` height of a random search tree, a Bloom filter&rsquo;s rate under the independent-hash idealisation, and the maximum-load asymptotics, which are stated and proved nowhere in this library. What the labs cannot do is quantify over inputs. A count on the input on screen is evidence about that input; the claim the lesson makes is about all of them, and the gap between the two is what each page closes on.'
    ),
    "courses": COURSES,
}
