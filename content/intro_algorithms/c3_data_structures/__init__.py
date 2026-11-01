"""Course 3 -- Data Structures: Part III of CLRS, Chapters 10-14.

Eight lessons in five modules: part_a reads Chapters 10, 11 and 12 (stacks,
queues and lists; hashing with chaining, hash functions and open addressing;
binary search trees), part_b Chapters 13 and 14 (red-black trees, their
insertion and deletion, and augmenting a tree). Section numbers and printed
pages are those of Cormen, Leiserson, Rivest and Stein, Introduction to
Algorithms, 3rd ed. (MIT Press, 2009). The design is
docs/intro-algorithms/PLAN.md, section C, Course 3.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-data-structures",
    "title": "Data Structures",
    "level": "Intermediate",
    "summary": (
        "Part III of the book, Chapters 10 to 14: Elementary Data Structures; Hash Tables; "
        "Binary Search Trees; Red-Black Trees; and Augmenting Data Structures. Each lesson sets "
        "out a chapter's argument in its own words, the cost of each operation, the expectation "
        "under a stated assumption, or the property a structure keeps, and then runs the "
        "structure on an instance written for the lesson and counts what the chapter analyses: "
        "the cost of one operation sequence on an array and on a list, chain lengths and probes "
        "beside the load factor, the collisions of a universal family counted over every "
        "function in it, the comparisons of a search tree, the five red-black properties checked "
        "node by node, the fix-up cases of each insertion, and the nodes an order-statistic "
        "query visits."
    ),
    "blurb": (
        "Read Part III a few sections at a time. Price operations on an array and a list, hash "
        "keys into chains and into an open table and set the probes beside the load factor, "
        "count a universal family's collisions exactly, delete from a search tree by its "
        "successor, check a red-black tree's five properties, count the recolorings and "
        "rotations of its insertions, and answer rank queries from subtree sizes."
    ),
    "key": [
        "a cost belongs to a representation",
        "chaining costs Θ(1 + α) on average",
        "choose the hash function at random",
        "open addressing: 1/(1 − α) probes",
        "search-tree costs are O(h)",
        "red-black height is at most 2 lg(n + 1)",
        "an insertion rotates at most twice",
        "keep a field its children determine",
    ],
    "assumes_short": "Foundations, and Sorting and Order Statistics",
    "assumes_long": (
        "Foundations, for loop invariants, asymptotic notation and indicator random variables, "
        "and Sorting and Order Statistics, for heaps and order statistics; the lessons lean on "
        "Appendix B's trees and Appendix C's probability where the book does"
    ),
    "outcomes_intro": (
        "By the end you can run each of Part III's structures by hand on a few keys, count "
        "what its chapter counts, and say which of your counts is a fact about those keys and "
        "which bound the book proves for every set of keys."
    ),
    "outcomes": [
        ("Price the elementary structures",
         "Run a stack, an array queue and a doubly linked list by hand, give each operation's "
         "cost, and say which costs depend on holding a pointer rather than a key."),
        ("Analyse a hash table",
         "Compute the load factor and the expected search costs under chaining and under open "
         "addressing, hash keys by the division and multiplication methods, and count the "
         "collisions of a universal family exactly."),
        ("Operate a binary search tree",
         "Search, find a successor, insert and delete by transplanting, and relate every cost "
         "to the height of the tree."),
        ("Keep a tree balanced",
         "Check the five red-black properties and the black-height, apply Lemma 13.1's bound, "
         "and run RB-INSERT-FIXUP by hand, counting its recolorings and rotations."),
        ("Augment a structure",
         "Maintain subtree sizes, answer select and rank queries in time proportional to the "
         "height, and test a proposed field against Theorem 14.1."),
    ],
    "syllabus_intro": (
        "Eight lessons follow Part III in the book's order: one on Chapter 10, the elementary "
        "structures; three on Chapter 11, chaining, hash functions and open addressing; one on "
        "Chapter 12, binary search trees; two on Chapter 13, the red-black properties and the "
        "insertion and deletion that keep them; and one on Chapter 14, augmenting a tree."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Part III, with instances written for these lessons. Each lesson names its sections, "
        "opens with at most one short quotation, and sets out the argument in its own words; "
        "the book's pseudocode, figures and exercises are better read in the book, and the "
        "lessons point to them by name and number.",
        "Run the structure by hand once. Every lesson works a few keys on paper before the lab "
        "runs more of them, because a count you have made yourself is the only kind you can "
        "check the lab against.",
        "Keep the count and the bound apart. The labs run each structure in your browser and "
        "print what it did on the keys in front of them, beside the bound or the expectation "
        "the chapter proves. The first is a fact about one input; the second holds for every "
        "input, or on average under a stated assumption, and only its proof establishes that.",
        "Change the input. Each lab takes your own keys or settings, and each lesson ends by "
        "asking you to try some of your own. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are named in the lessons and left "
        "to the book; the keys and trees in these lessons are written for them.",
        "The chapter-end problems, among them the comparison of list representations in "
        "Chapter 10, quadratic probing's parameters in Chapter 11, radix trees in Chapter 12, "
        "and AVL and join operations in Chapter 13. They are worth working in the book.",
        "The full proofs of the starred sections: perfect hashing in 11.5 and the expected "
        "height of a randomly built search tree in 12.4. The lessons state their results and "
        "point to them.",
        "A lab for red-black deletion. Section 13.4's fix-up cases are set out in prose and by "
        "hand; the lab runs insertion.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser by running the structure on "
        "the input a lesson states: the cost of an operation sequence on an array and on a "
        "list, chain lengths and probe counts beside the load factor, collisions counted over "
        "every function in a universal family, the comparisons of a search tree, the red-black "
        "properties checked node by node with the recolorings and rotations of each insertion, "
        "and the nodes an order-statistic query visits. The keys are written for these lessons. "
        "A count describes one input; the book's bounds are proved for all of them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
