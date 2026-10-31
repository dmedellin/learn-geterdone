"""Course 5 -- Advanced Data Structures: Part V of CLRS, Chapters 18-21.

Five lessons in four modules, all in part_a: B-trees (Chapter 18), Fibonacci
heaps in two lessons (Chapter 19), van Emde Boas trees (Chapter 20) and
disjoint sets (Chapter 21). Section numbers and printed pages are those of
Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009). The design is docs/intro-algorithms/PLAN.md, section C,
Course 5.
"""

from . import part_a

COURSE = {
    "slug": "intro-algorithms-advanced-structures",
    "title": "Advanced Data Structures",
    "level": "Intermediate",
    "summary": (
        "Part V of the book, Chapters 18 to 21: B-Trees; Fibonacci Heaps; van Emde Boas Trees; "
        "and Data Structures for Disjoint Sets. Each lesson sets out a chapter's argument in its "
        "own words, the height bound, the potential function, the square-root recurrence or the "
        "rank argument, and then runs the structure on operations written for the lesson and "
        "counts what the chapter counts: the splits and disk accesses of B-tree insertion, the "
        "actual and amortized cost of every Fibonacci-heap operation with the potential beside "
        "it, the cuts and cascading cuts of decreasing a key, the recursive calls of proto-vEB "
        "structures against van Emde Boas trees, and the pointers a find walks under union by "
        "rank and path compression."
    ),
    "blurb": (
        "Read Part V a chapter or two at a time. Grow a B-tree and count its disk accesses "
        "against the height theorem, run a Fibonacci heap and watch the potential pay for "
        "consolidation and for cascading cuts, count the recursive calls that separate a "
        "proto-vEB structure from a van Emde Boas tree, and flatten a forest of disjoint sets "
        "by ranking its unions and compressing its paths."
    ),
    "key": [
        "a B-tree node is a disk page",
        "B-trees grow at the root",
        "Fibonacci heaps put work off",
        "potential pays for consolidation",
        "marks limit what a node can lose",
        "one recursive call a level: lg lg u",
        "rank and compression flatten a forest",
    ],
    "assumes_short": "Advanced Design and Analysis Techniques",
    "assumes_long": (
        "Advanced Design and Analysis Techniques, above all Chapter 17's aggregate, accounting "
        "and potential methods, which two of these chapters use throughout; Data Structures, for "
        "binary search trees, red-black trees and direct addressing; and Sorting and Order "
        "Statistics, for binary heaps and the comparison lower bound"
    ),
    "outcomes_intro": (
        "By the end you can run each of Part V's structures by hand on a few operations, count "
        "what its chapter counts, and say which of your counts is a fact about those operations "
        "and which bound the book proves for every sequence of them."
    ),
    "outcomes": [
        ("Grow a B-tree and price it in disk accesses",
         "Insert keys with B-TREE-INSERT, splitting full nodes on the way down, count the "
         "DISK-READs and DISK-WRITEs, and set the height against Theorem 18.1's bound."),
        ("Run a Fibonacci heap under its potential",
         "Carry insertions and EXTRACT-MIN through by hand, consolidate the root list, and "
         "compute each operation's actual cost, the change in t(H) + 2m(H) and the amortized "
         "cost."),
        ("Decrease keys and bound the degree",
         "Apply cuts and cascading cuts, keep the marks, check the amortized constant of "
         "DECREASE-KEY, and check Lemma 19.4's Fibonacci lower bound on subtree sizes."),
        ("Count the calls of a van Emde Boas tree",
         "Split elements into high and low parts, run member, insert, successor and delete on "
         "a proto-vEB structure and on a vEB tree, and explain the gap from the two "
         "recurrences."),
        ("Maintain disjoint sets",
         "Run unions and finds on linked lists with the weighted-union heuristic and on forests "
         "with union by rank and path compression, and say what α(n) is and why it is small."),
    ],
    "syllabus_intro": (
        "Five lessons follow Part V in the book's order: one on Chapter 18, B-trees; two on "
        "Chapter 19, the mergeable-heap operations and then decreasing keys with the degree "
        "bound; one on Chapter 20, van Emde Boas trees; and one on Chapter 21, disjoint sets."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Part V, with instances written for these lessons. Each lesson names its sections, "
        "opens with at most one short quotation, and sets out the argument in its own words; "
        "the book's pseudocode, figures and exercises are better read in the book, and the "
        "lessons point to them by name and number.",
        "Run the structure by hand once. Every lesson works a few operations on paper before "
        "the lab runs more, because a count you have made yourself is the only kind you can "
        "check the lab against.",
        "Keep the count and the bound apart. The labs run each structure in your browser and "
        "print what it did on the operations in front of them, beside the bound the chapter "
        "proves. The first is a fact about one sequence; the second holds for every sequence, "
        "and only its proof establishes that.",
        "Change the input. The B-tree, Fibonacci-heap and van Emde Boas labs take your own "
        "keys and operations, the disjoint-set lab your own size and rules, and each lesson "
        "ends by asking you to try one of your own. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are named in the lessons and left "
        "to the book; the keys and operations in these lessons are written for them.",
        "Deletion from a B-tree, Section 18.3, runs in no lab. Its cases are set out in prose "
        "and the book sketches it without pseudocode.",
        "The full potential-function proof of Section 21.4, starred in the book, which shows "
        "the O(m α(n)) bound for union by rank with path compression. The lesson defines α(n) "
        "and states the bound; the proof is left to the book.",
        "The chapter-end problems, among them Problem 19-2's binomial trees, Problem 20-1's "
        "reduced-space van Emde Boas trees and Problem 21-3's off-line least common ancestors. "
        "They are worth working in the book.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser by running the structure on "
        "the operations a lesson states: the splits, reads and writes of B-tree insertion, the "
        "actual and amortized cost of each Fibonacci-heap operation with its potential, the "
        "cuts and marks of decreasing keys, the recursive calls of two recursive structures "
        "over the same universe, and the pointers walked by every find in a disjoint-set "
        "forest. The operations are written for these lessons. A count describes one sequence; "
        "the book's bounds are proved for all of them."
    ),
    "lessons": part_a.LESSONS,
}
