"""Course 1 -- Foundations: Part I of CLRS, Chapters 1-5.

Eight lessons in five modules: part_a reads Chapters 1, 2 and 3.1-3.2 (the
role of algorithms, insertion sort and its invariant, its analysis, merge
sort and divide-and-conquer, asymptotic notation), part_b Chapters 4 and 5
(the maximum-subarray problem and Strassen's method, solving recurrences,
the hiring problem and randomized algorithms). Section numbers and printed
pages are those of Cormen, Leiserson, Rivest and Stein, Introduction to
Algorithms, 3rd ed. (MIT Press, 2009). The design is
docs/intro-algorithms/PLAN.md, section C, Course 1.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-foundations",
    "title": "Foundations",
    "level": "Intermediate",
    "summary": (
        "Part I of the book, Chapters 1 to 5: The Role of Algorithms in Computing; Getting "
        "Started; Growth of Functions; Divide-and-Conquer; and Probabilistic Analysis and "
        "Randomized Algorithms. Each lesson sets out a chapter's argument in its own words, the "
        "loop invariant, the line-by-line cost, the recurrence or the indicator variables, and "
        "then runs the algorithm on an instance written for the lesson and counts what the "
        "chapter analyses: the crossover between two programs on two machines, insertion sort's "
        "comparisons and shifts pass by pass, merge sort's comparisons level by level, a claimed "
        "witness checked at ten thousand sizes, three routes to a maximum subarray, the exact "
        "value of a recurrence beside the master method's verdict, and the hires of the hiring "
        "problem averaged over every order."
    ),
    "blurb": (
        "Read Part I a few sections at a time. Race a quadratic program on a fast machine "
        "against an n lg n program on a slow one, check insertion sort's invariant pass by pass, "
        "add up its line costs, count merge sort's comparisons per level, test a claimed c and "
        "n₀, find a maximum subarray three ways, solve a recurrence exactly and by the master "
        "method, and average the hires over every order of eight candidates."
    ),
    "key": [
        "an algorithm is a technology",
        "an invariant: start, maintenance, end",
        "count line costs; keep the leading term",
        "divide, conquer, combine",
        "Θ, O and Ω are claims with witnesses",
        "seven products where eight were needed",
        "compare f(n) with n^(log_b a)",
        "indicator variables give H_n hires",
    ],
    "assumes_short": "Programming, induction, sums and logarithms",
    "assumes_long": (
        "that you can read a loop and a recursive call in some programming language, and know "
        "proof by induction, simple sums and logarithms; the lessons lean on Appendix A's sums "
        "and Appendix C's probability where the book does"
    ),
    "outcomes_intro": (
        "By the end you can do to a small algorithm what Part I does to insertion sort, merge "
        "sort and the hiring problem: prove it correct, count its steps, state the count in "
        "asymptotic notation, solve the recurrence or the expectation, and say which of your "
        "figures is a fact about one input and which is a bound for every input."
    ),
    "outcomes": [
        ("Prove a loop correct",
         "State a loop invariant and show its initialisation, maintenance and termination, as "
         "Section 2.1 does for insertion sort and Section 2.3 for merging."),
        ("Count an algorithm's steps",
         "Write the line-by-line cost of a procedure in the RAM model, find its best and worst "
         "cases, and reduce the sum to its order of growth."),
        ("Use asymptotic notation exactly",
         "Read Θ, O, Ω, o and ω as claims about constants c and n₀, produce a witness for a true "
         "claim, and show why a false one has none."),
        ("Solve a divide-and-conquer recurrence",
         "Set up the recurrence of a divide-and-conquer algorithm, solve it by a recursion tree "
         "or by substitution, and apply the master method or say why it does not apply."),
        ("Analyse with indicator random variables",
         "Compute an expected count by linearity of expectation, check it against the average "
         "over every input at small n, and say what randomizing the input buys."),
    ],
    "syllabus_intro": (
        "Eight lessons follow Part I in the book's order: one on Chapter 1, the role of "
        "algorithms; three on Chapter 2, insertion sort, its analysis and merge sort; one on "
        "Chapter 3, asymptotic notation; two on Chapter 4, divide-and-conquer and recurrences; "
        "and one on Chapter 5, probabilistic analysis and randomized algorithms."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Part I, with instances written for these lessons. Each lesson names its sections, "
        "opens with at most one short quotation, and sets out the argument in its own words; "
        "the book's pseudocode, figures and exercises are better read in the book, and the "
        "lessons point to them by name and number.",
        "Run the algorithm by hand once. Every lesson works one small instance on paper before "
        "the lab runs a larger one, because a count you have made yourself is the only kind "
        "you can check the lab against.",
        "Keep the count and the bound apart. The labs run each algorithm in your browser and "
        "print what it did on the input in front of them, beside the bound the chapter "
        "proves. The first is a fact about one input; the second holds for every input, and "
        "only its proof establishes that.",
        "Change the input. Each lab takes your own arrays, constants or sizes, and each lesson "
        "ends by asking you to try one of your own. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are named in the lessons and left "
        "to the book; the arrays, machines and orders in these lessons are written for them.",
        "Section 4.6, the proof of the master theorem, and the starred Section 5.4 on the "
        "birthday paradox, balls and bins, streaks and the on-line hiring problem. Both are "
        "named where they belong and left to the book.",
        "The chapter-end problems, among them insertion sort on small subarrays inside merge "
        "sort and inversions in Chapter 2, the asymptotic orderings of Chapter 3 and the many "
        "recurrences of Chapter 4. They are worth working in the book.",
        "Strassen's method as a lab. Its seven products and eighteen additions are set out in "
        "prose and its recurrence is solved in the lab of Solving Recurrences; the products "
        "themselves are left to the book's Section 4.2.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser by running the algorithm on "
        "the input a lesson states: the times of two programs on two machines, the comparisons "
        "and shifts of insertion sort pass by pass, merge sort's comparisons level by level, a "
        "claimed witness checked at every size in a range, three maximum-subarray algorithms "
        "side by side, a recurrence evaluated exactly, and the hires on every order of a few "
        "candidates. The instances are written for these lessons. A count describes one input; "
        "the book's bounds are proved for all of them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
