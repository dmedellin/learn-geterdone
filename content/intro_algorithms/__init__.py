"""The Introduction to Algorithms path, as data: a read-along of Cormen,
Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd edition (MIT
Press, 2009).

Eight courses that follow the book's Parts I to VII (Part VII in two). Each
lesson sets out a chapter's argument in its own words and runs the algorithm on
an instance written for the lesson, counting what the chapter analyses. The
content lives here and only here; scripts/ turns it into pages. The design is
docs/intro-algorithms/PLAN.md.
"""

from . import (
    c1_foundations,
    c2_sorting,
    c3_data_structures,
    c4_design_techniques,
    c5_advanced_structures,
    c6_graphs,
    c7_algebraic_topics,
    c8_strings_geometry_hardness,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_foundations.COURSE,
    c2_sorting.COURSE,
    c3_data_structures.COURSE,
    c4_design_techniques.COURSE,
    c5_advanced_structures.COURSE,
    c6_graphs.COURSE,
    c7_algebraic_topics.COURSE,
    c8_strings_geometry_hardness.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "intro-algorithms",
    "title": "Introduction to Algorithms, Read Along",
    "level": "Intermediate → Advanced",
    "level_note": "you can program, and you know induction, sums and logarithms",
    "tagline": (
        "Cormen, Leiserson, Rivest and Stein&rsquo;s <em>Introduction to Algorithms</em>, read chapter by chapter from the first loop invariant to NP-completeness &mdash; and each algorithm run and counted on an instance written for the lesson: comparisons, shifts, recursive calls, hires, rotations, splits, relaxations, pivots. Eight courses and 61 lessons are available."
    ),
    "description": (
        "The Introduction to Algorithms Subject: a read-along of the third edition of the textbook known as CLRS, following its Parts I to VII in the book&rsquo;s own order, Part VII in two. Eight courses take the reader from insertion sort, asymptotic notation and recurrences through sorting, data structures, dynamic programming and greedy algorithms, advanced structures and graph algorithms to multithreading, linear programming, the FFT, number theory, string matching, geometry and NP-completeness. Each lesson sets out a chapter&rsquo;s argument in its own words &mdash; the loop invariant, the recurrence, the exchange or cut argument &mdash; runs the algorithm in the lab and prints the counts the chapter analyses beside the bound it proves, and ends with an instance to work by hand. All eight courses and 61 lessons are available."
    ),
    "key": [
        "an invariant: initialisation, maintenance, end",
        "T(n) = 2T(n/2) + Θ(n) gives Θ(n lg n)",
        "f = Θ(g): c₁·g ≤ f ≤ c₂·g from n₀ on",
        "expected hires on a random order = H_n",
        "a count is about one input, a bound about all",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it. The first course supplies the method every later chapter uses: a loop invariant for correctness, a count of steps for cost, asymptotic notation for the count, and a recurrence or an expectation when the algorithm recurses or randomizes. Sorting then uses all of it at once; the data structures, the design techniques and the advanced structures build on the sorting and the method; the graph algorithms use the structures; and the last two courses take the method into parallel, numerical, algebraic and combinatorial territory."
    ),
    "why_order": [
        "The order is the book&rsquo;s, Part by Part. Foundations is Part I: what an algorithm is, insertion sort and merge sort, the notation, divide-and-conquer and the recurrences it produces, and probabilistic analysis. Sorting and Order Statistics is Part II, Data Structures Part III, Advanced Design and Analysis Techniques Part IV, Advanced Data Structures Part V and Graph Algorithms Part VI. Part VII, Selected Topics, holds nine chapters and is read as two courses: parallel, matrix, linear-programming, polynomial and number-theoretic algorithms, then strings, geometry, NP-completeness and approximation.",
        "Part I comes first because every later proof is one of its shapes. Heapsort&rsquo;s build is a loop invariant; quicksort&rsquo;s expected comparisons are indicator random variables; Strassen&rsquo;s recurrence returns in the multithreaded matrix product; the amortized analyses of Chapter 17 reappear in Fibonacci heaps and disjoint sets. A reader who meets them in Part I recognises them later rather than learning them again under a new name.",
        "The appendices, Part VIII, are not a course. Sums, sets, counting, probability and matrices are background the book gathers at its end, and a lesson points to the appendix where it leans on one, as the book does.",
        "The courses can be read separately once Foundations is done. Graph Algorithms uses the queues and priority queues of Courses 2 and 3, and the hardness lessons at the end use the reductions and running-time vocabulary of everything before them, but every result a lesson uses is restated where it is used.",
    ],
    "prerequisites": [
        "You can program. The book writes its algorithms in a pseudocode close to C, Java or Python, with arrays numbered from 1; the lessons describe each procedure in prose and name it, and you will follow them if you can read a loop and a recursive call in any language.",
        "You know proof by induction, sums such as 1 + 2 + &hellip; + n and a geometric series, and logarithms. The book reviews sums, counting and probability in its appendices, and the lessons point there where they lean on them; Appendix A&rsquo;s sums and Appendix C&rsquo;s probability are the two you will want nearest.",
        "No other Subject. The library&rsquo;s Algorithms Subject runs many of the same algorithms with its own lessons, and a lesson here names the matching one once as a place to practise further, but nothing here depends on it.",
        "A copy of the book is strongly recommended. The book is in copyright, so a lesson states each chapter&rsquo;s argument in its own words, points to the section, procedure and exercise by name and number, and quotes at most a sentence or two. The arrays, graphs and instances are written for these lessons, and none of the book&rsquo;s pseudocode, figures or exercises is reproduced.",
        "Patience with arithmetic by hand. Every lesson asks you to run the algorithm on paper once on a small instance before the lab runs a larger one, because a count you have made yourself is the only kind you can check a machine against.",
    ],
    "material": (
        "every count on this path is produced by running the algorithm in your browser on the instance a lesson states, and a count on one instance is evidence about that instance &mdash; the bound the book proves holds for every input, and only its proof establishes that."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser by running the algorithm on the instance a lesson states: comparisons and shifts counted as an array is sorted, the exact value of a recurrence at the sizes you choose, the average over every order of a few candidates, the rotations of a red-black insertion, the relaxations of a shortest-path run. The instances are written for these lessons; nothing you type is sent anywhere. What the labs cannot do is prove a bound &mdash; a count describes one input, and the book&rsquo;s proofs are about all of them."
    ),
    "courses": COURSES,
}
