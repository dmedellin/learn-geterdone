"""Course 8 -- Strings, Geometry and Hardness: Part VII of Introduction to
Algorithms, Chapters 32-35.

Eight lessons in four modules: part_a reads Chapters 32 and 33 (string matching
and computational geometry), part_b Chapters 34 and 35 (NP-completeness and
approximation algorithms). Page references are to Cormen, Leiserson, Rivest
and Stein, Introduction to Algorithms, 3rd ed. (MIT Press, 2009). The design is
docs/intro-algorithms/PLAN.md, section C, Course 8.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-strings-geometry-hardness",
    "title": "Strings, Geometry and Hardness",
    "level": "Advanced",
    "summary": (
        "The last four chapters of Part VII, 32 to 35: String Matching; Computational "
        "Geometry; NP-Completeness; and Approximation Algorithms. The first two are about "
        "algorithms that are fast for a reason you can count: a rolling hash and its "
        "spurious hits, a prefix function whose inner loop is bounded in aggregate, four "
        "cross products that decide whether two segments meet, and a stack on which each "
        "point is pushed once. The last two are about problems that are probably not fast "
        "at all, and what to do about them: certificates, reductions built digit by digit, "
        "and approximation ratios proved against a lower bound the algorithm can see. Each "
        "lesson sets out the sections' argument and then runs the algorithm on an instance "
        "written for it."
    ),
    "blurb": (
        "Read Chapters 32 to 35 two sections at a time. Count the spurious hits of a "
        "rolling hash, build a prefix function and its fallback chain, decide whether two "
        "segments meet from four signs, run Graham's scan by hand, check a certificate and "
        "build one from yes-or-no answers, turn a formula into a subset-sum instance, and "
        "measure an approximation against its optimum and its bound."
    ),
    "key": [
        "every valid shift, checked or fingerprinted",
        "never read a text character twice",
        "one cross product: which way it turns",
        "certificates make NP; reductions, NPC",
        "prove the ratio against a lower bound",
    ],
    "assumes_short": "Parallel, Matrix, Linear and Number Algorithms",
    "assumes_long": (
        "Parallel, Matrix, Linear and Number Algorithms, for modular arithmetic (Chapter 31) "
        "behind the rolling hash, and the earlier courses for amortized analysis, divide and "
        "conquer, greedy algorithms, minimum spanning trees and linear programming, which "
        "these chapters reuse"
    ),
    "outcomes_intro": (
        "By the end you can do, on a small instance and by hand, what these chapters do in "
        "general, and say which of the chapters' claims are proved for every input and which "
        "rest on an assumption."
    ),
    "outcomes": [
        ("Run and analyse the string matchers",
         "Find the valid shifts of a pattern, compute the naive bound, run Rabin-Karp's "
         "rolling hash and name its spurious hits, compute the prefix function π, and explain "
         "why its inner loop runs at most m − 1 times in total."),
        ("Answer segment questions with cross products",
         "Decide which way three points turn, compute the four directions of "
         "SEGMENTS-INTERSECT with its boundary case, and say what the sweep of section 33.2 "
         "decides and in what time."),
        ("Find a hull and bound the work",
         "Run Graham's scan by hand with every push and pop, compare O(n lg n) with Jarvis's "
         "O(n·h), and explain why the closest-pair strip needs only seven comparisons per "
         "point."),
        ("Place a problem in NP and prove it hard",
         "Name a certificate and its polynomial-time check, explain why encodings matter, "
         "build the subset-sum instance for a 3-CNF formula, and say which direction a "
         "reduction must go."),
        ("Prove and measure an approximation",
         "Run APPROX-VERTEX-COVER and GREEDY-SET-COVER, prove their ratios from a matching "
         "and from charges, compute the expected clauses a random assignment satisfies, and "
         "trim a list of subset sums."),
    ],
    "syllabus_intro": (
        "Eight lessons follow Chapters 32 to 35 in the book's order, two per chapter: "
        "naive and Rabin-Karp matching, then automata and Knuth-Morris-Pratt; segment "
        "properties, then hulls and the closest pair; polynomial time and verification, then "
        "NP-completeness and reductions; and vertex cover and TSP, then set cover, "
        "randomization and subset sum."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, "
        "2009), Chapters 32 to 35, with instances written for these lessons. Each lesson "
        "names its sections, opens with at most one short quotation, and sets out the "
        "argument in its own words; the book's pseudocode, figures and exercises are better "
        "read in the book, and each procedure is named by its book name so you can find it.",
        "Keep two kinds of claim apart. Each chapter proves some bounds for every input and "
        "states others under an assumption: Rabin-Karp's expected time assumes the hash "
        "behaves randomly, and P versus NP is open. The lessons say which is which, and so "
        "should you.",
        "Treat each count as evidence about one instance. The labs run the algorithm in your "
        "browser on the text, points, formula, graph or family you type and print what the "
        "chapter counts: spurious hits, inner-loop iterations, orientations, pushes and pops, "
        "oracle questions, subsets, and ratios against an optimum found by exhaustive search. "
        "A count on one instance never proves the bound beside it; only the book's proof "
        "does.",
        "Type your own instances. Every lesson ends with an exercise to work by hand and "
        "check in the lab, and with a step that sends you to an instance of your own. Nothing "
        "you type leaves your browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures, worked examples and exercises. They are the book's, "
        "and the lessons name procedures and point to exercises by number instead of "
        "reproducing them.",
        "The full correctness proofs of the prefix-function iteration lemma, the sweep's "
        "correctness, Graham's scan, CIRCUIT-SAT's hardness and the HAM-CYCLE widget. The "
        "lessons give each argument's idea and leave the details to the book.",
        "The automaton's transition table and the sweep, closest-pair, TSP, MAX-3-CNF and "
        "trimming algorithms as labs. The labs cover Rabin-Karp, the prefix function, the "
        "segment test, the hull, the self-reduction, the subset-sum construction, vertex "
        "cover and set cover; the others are worked in prose or by hand, and the Algorithms "
        "Subject has labs for several of them.",
        "Chapter notes and the problems at each chapter's end, which point to later work: "
        "the Boyer-Moore matcher, robust geometric predicates, and inapproximability.",
        "Part VIII, the appendices. The lessons lean on Appendix A's harmonic series and "
        "Appendix C's probability and name them where they do.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the instance a lesson "
        "states or you type: window hashes and spurious hits, the prefix function beside "
        "every border found by trying each length, four orientations in exact integers, hull "
        "vertices checked against the definition, oracle questions checked against brute "
        "force, subset sums matched to satisfying assignments, and approximate answers set "
        "beside an optimum found by exhaustive search. The instances are written for these "
        "lessons; quotations from the book are marked as the book's. A count on one instance "
        "is evidence about that instance; the bound the book proves holds for every input."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
