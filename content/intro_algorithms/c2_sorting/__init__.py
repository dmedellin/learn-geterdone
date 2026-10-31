"""Course 2 -- Sorting and Order Statistics: Part II of CLRS, Chapters 6-9.

Seven lessons in four modules: part_a reads Chapters 6, 7 and 8.1-8.2
(heaps, heapsort, quicksort and its analysis, the lower bound and counting
sort), part_b Chapters 8.3-8.4 and 9 (radix and bucket sort, medians and
order statistics). Section numbers and printed pages are those of Cormen,
Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT Press,
2009). The design is docs/intro-algorithms/PLAN.md, section C, Course 2.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-sorting",
    "title": "Sorting and Order Statistics",
    "level": "Intermediate",
    "summary": (
        "Part II of the book, Chapters 6 to 9: Heapsort; Quicksort; Sorting in Linear Time; "
        "and Medians and Order Statistics. Each lesson sets out a chapter's argument in its "
        "own words, the loop invariant, the recurrence or the counting argument, and then runs "
        "the algorithm on an instance written for the lesson and counts what the chapter "
        "analyses: exchanges while a heap is built, comparisons while it is taken apart, the "
        "comparisons of one partition, the exact expected comparisons of randomized quicksort, "
        "the work of counting sort and radix sort beside the comparison bound they sit "
        "outside, and the comparisons spent finding a median."
    ),
    "blurb": (
        "Read Part II a few sections at a time. Build a heap and price the build by the sum "
        "over heights, take it apart into a sorted array, step through a partition with its "
        "invariant checked, compute randomized quicksort's expected comparisons exactly, set "
        "counting and radix sort against the decision-tree bound, and find a median in "
        "expected linear time."
    ),
    "key": [
        "a heap is a tree kept in an array",
        "building a heap costs linear time",
        "partition puts one key in its place",
        "randomness in the pivot, not the input",
        "comparison sorts need lg(n!) steps",
        "stable passes make radix sort work",
        "a median costs linear time",
    ],
    "assumes_short": "Foundations",
    "assumes_long": (
        "Foundations, for loop invariants, merge sort, asymptotic notation, the master method "
        "and indicator random variables; the lessons lean on Appendix A's sums and Appendix C's "
        "probability where the book does"
    ),
    "outcomes_intro": (
        "By the end you can run each of Part II's algorithms by hand on a small array, count "
        "what its chapter counts, and say which of your counts is a fact about that array and "
        "which bound the book proves for every array."
    ),
    "outcomes": [
        ("Build and use a heap",
         "Run MAX-HEAPIFY and BUILD-MAX-HEAP on an array, count the exchanges, evaluate the sum "
         "over heights that bounds them, and carry heapsort and the priority-queue operations "
         "through by hand."),
        ("Partition and analyse quicksort",
         "Step through PARTITION with its invariant, count its comparisons, write the "
         "recurrences for the worst and the balanced split, and compute randomized quicksort's "
         "expected comparisons from the indicator variables."),
        ("Place the comparison lower bound",
         "Compute the decision-tree bound for a given n and say which sorts it binds, and why "
         "counting sort, radix sort and bucket sort are outside it."),
        ("Sort with digits and counts",
         "Run counting sort and radix sort by hand, count their work, and show where stability "
         "is needed and what goes wrong without it."),
        ("Select an order statistic",
         "Find the minimum and maximum together in 3⌊n/2⌋ comparisons, trace randomized "
         "selection, and check the groups-of-five arithmetic behind the worst-case linear "
         "bound."),
    ],
    "syllabus_intro": (
        "Seven lessons follow Part II in the book's order: two on Chapter 6, heaps and "
        "heapsort; two on Chapter 7, quicksort and its analysis; two on Chapter 8, the lower "
        "bound and the linear-time sorts; and one on Chapter 9, medians and order statistics."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Part II, with instances written for these lessons. Each lesson names its sections, "
        "opens with at most one short quotation, and sets out the argument in its own words; "
        "the book's pseudocode, figures and exercises are better read in the book, and the "
        "lessons point to them by name and number.",
        "Run the algorithm by hand once. Every lesson works one small array on paper before "
        "the lab runs a larger one, because a count you have made yourself is the only kind "
        "you can check the lab against.",
        "Keep the count and the bound apart. The labs run each algorithm in your browser and "
        "print what it did on the input in front of them, beside the bound the chapter "
        "proves. The first is a fact about one input; the second holds for every input, and "
        "only its proof establishes that.",
        "Change the input. Each lab takes your own keys or sizes, and each lesson ends by "
        "asking you to try one of your own. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are named in the lessons and left "
        "to the book; the arrays in these lessons are written for them.",
        "The chapter-end problems, among them the d-ary heaps and Young tableaus of Chapter 6, "
        "Hoare's partition and median-of-3 partitioning of Chapter 7, and the water jugs of "
        "Chapter 8. They are worth working in the book.",
        "Bucket sort's lab. Section 8.4's average-case argument is set out in prose and by "
        "hand; the Algorithms lesson Bucket Sort and Average-Case Claims runs it.",
        "The substitution proofs of Sections 9.2 and 9.3 in full, the expected linear time of "
        "randomized selection and the worst-case bound with its constant 140, which the "
        "lessons outline and leave to the book.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser by running the algorithm on "
        "the input a lesson states: exchanges and comparisons counted as a heap is built and "
        "taken apart, the comparisons of a partition step by step, the expectation of "
        "randomized quicksort as an exact fraction, the tallies of counting sort and the "
        "passes of radix sort, and the comparisons of a selection. The arrays are written for "
        "these lessons. A count describes one input; the book's bounds are proved for all of "
        "them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
