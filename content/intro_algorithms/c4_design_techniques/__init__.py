"""Course 4 -- Advanced Design and Analysis Techniques: Part IV of CLRS, Chapters 15-17.

Nine lessons in three modules: part_a reads Chapter 15 (rod cutting,
matrix-chain multiplication, the elements of dynamic programming, longest
common subsequence, optimal binary search trees), part_b Chapters 16 and 17
(activity selection, Huffman codes, matroids, amortized analysis). Section
numbers and printed pages are those of Cormen, Leiserson, Rivest and Stein,
Introduction to Algorithms, 3rd ed. (MIT Press, 2009). The design is
docs/intro-algorithms/PLAN.md, section C, Course 4.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-design-techniques",
    "title": "Advanced Design and Analysis Techniques",
    "level": "Intermediate → Advanced",
    "summary": (
        "Part IV of the book, Chapters 15 to 17: Dynamic Programming; Greedy Algorithms; and "
        "Amortized Analysis. Each lesson sets out a chapter's argument in its own words, the "
        "optimal substructure, the greedy choice, the exchange or the potential function, and "
        "then runs the algorithm on an instance written for the lesson and counts what the "
        "chapter counts: the calls a plain recursion makes against a memoized one, the cells of "
        "a table and the choices behind each, the merges that build a code, the elements a "
        "greedy rule keeps, and the actual and amortized costs of a sequence of operations."
    ),
    "blurb": (
        "Read Part IV a section or two at a time. Cut a rod three ways and count the calls, fill "
        "the tables for a matrix chain, a common subsequence and a search tree, check a greedy "
        "rule against every subset, build a Huffman code, test the exchange property, and "
        "price a growing and shrinking table with a potential function."
    ),
    "key": [
        "solve each subproblem once, and save it",
        "the table's fill order follows the recurrence",
        "optimal substructure is proved, not assumed",
        "a greedy choice needs its own proof",
        "matroids make the greedy rule always right",
        "amortized cost bounds a whole sequence",
    ],
    "assumes_short": "Foundations and Data Structures",
    "assumes_long": (
        "Foundations, for induction, asymptotic notation, recurrences and the substitution "
        "method, and Data Structures, for stacks, binary search trees and hash tables; the "
        "lessons lean on Appendix A's sums and Appendix B's trees and graphs where the book does"
    ),
    "outcomes_intro": (
        "By the end you can design a dynamic program or a greedy algorithm for a small problem, "
        "fill its table or run its rule by hand, count what the chapter counts, and say which "
        "of your counts is a fact about one instance and which bound the book proves for all."
    ),
    "outcomes": [
        ("Build a dynamic program",
         "State the subproblems, write the recurrence, choose a fill order the recurrence "
         "allows, fill the table by hand and reconstruct an optimal solution from the choices "
         "you recorded."),
        ("Argue optimal substructure, or its absence",
         "Give the cut-and-paste argument for a problem that has optimal substructure, and a "
         "small instance showing a problem that lacks it."),
        ("Prove and run a greedy algorithm",
         "Run a greedy rule by hand, check it against an exhaustive search on a small instance, "
         "and give the exchange argument that makes the greedy choice safe."),
        ("Recognise a matroid",
         "Check heredity and the exchange property on a small family, run GREEDY on a weighted "
         "matroid, and schedule unit-time tasks with deadlines by it."),
        ("Bound a sequence of operations",
         "Bound the total cost of a sequence by aggregate analysis, by credits and by a "
         "potential function, and compute each operation's amortized cost exactly."),
    ],
    "syllabus_intro": (
        "Nine lessons follow Part IV in the book's order: five on Chapter 15, one per section; "
        "three on Chapter 16, activity selection with the elements of the greedy strategy, "
        "Huffman codes, and matroids with the task-scheduling problem; and one on Chapter 17, "
        "its three methods and the dynamic table."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Part IV, with instances written for these lessons. Each lesson names its sections, "
        "opens with at most one short quotation, and sets out the argument in its own words; "
        "the book's pseudocode, figures and exercises are better read in the book, and the "
        "lessons point to them by name and number.",
        "Fill a table by hand once. Every lesson works one small instance on paper before the "
        "lab runs a larger one, because a cell you have computed yourself is the only kind you "
        "can check the lab against.",
        "Keep the count and the bound apart. The labs run each algorithm in your browser and "
        "print what it did on the input in front of them, beside the bound the chapter "
        "proves. The first is a fact about one input; the second holds for every input, and "
        "only its proof establishes that.",
        "Change the input. Each lab takes your own prices, strings, weights or operations, and "
        "each lesson ends by asking you to try some of your own. Nothing you type leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are named in the lessons and left "
        "to the book; the prices, strings, probabilities and weights in these lessons are "
        "written for them.",
        "The chapter-end problems, among them the bitonic tour, edit distance and the Viterbi "
        "algorithm of Chapter 15, coin changing and off-line caching of Chapter 16, and the "
        "weight-balanced trees and self-organizing lists of Chapter 17. They are worth working "
        "in the book.",
        "A lab for the task-scheduling matroid of Section 16.5. The lesson works it by hand; "
        "the matroid lab tests the graphic, uniform and partition families.",
        "The starred proofs and the faster implementations the book leaves to its problems, "
        "such as Knuth's speed-up for optimal search trees and the union-find version of task "
        "scheduling.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser by running the algorithm on "
        "the input a lesson states: calls counted in a plain and a memoized recursion, tables "
        "filled and checked against every bracketing or every tree, greedy rules checked "
        "against every subset, codes checked prefix-free, and the actual, amortized and "
        "potential costs of each operation in a sequence. The instances are written for these "
        "lessons. A count describes one input; the book's bounds are proved for all of them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
