"""Course 7 -- Parallel, Matrix, Linear and Number Algorithms: Part VII of
Introduction to Algorithms, Chapters 27-31.

Seven lessons in five modules: part_a reads Chapters 27 to 30 (multithreaded
algorithms, matrix operations, linear programming, polynomials and the FFT),
part_b Chapter 31 (number-theoretic algorithms). Section numbers and printed
pages are those of Cormen, Leiserson, Rivest and Stein, Introduction to
Algorithms, 3rd ed. (MIT Press, 2009). The design is
docs/intro-algorithms/PLAN.md, section C, Course 7.
"""

from . import part_a, part_b

COURSE = {
    "slug": "intro-algorithms-algebraic-topics",
    "title": "Parallel, Matrix, Linear and Number Algorithms",
    "level": "Advanced",
    "summary": (
        "The first five chapters of Part VII, 27 to 31: Multithreaded Algorithms; Matrix "
        "Operations; Linear Programming; Polynomials and the FFT; and Number-Theoretic "
        "Algorithms. Each chapter changes what is being computed on, from a graph of parallel "
        "strands to a matrix, a system of inequalities, a polynomial and a large integer, and "
        "each lesson sets out the chapter's argument in its own words before running the "
        "algorithm on an instance and counting what the chapter counts: work and span, the "
        "pivots of an exact LUP decomposition, the corners a simplex walk visits, a "
        "certificate that closes on the optimum, multiplications against butterflies, the "
        "divisions of Euclid's algorithm, and the witnesses that prove a number composite."
    ),
    "blurb": (
        "Read chapters 27 to 31 a few sections at a time. Compute the work and span of a "
        "parallel program, factor a matrix exactly, walk a linear program to its optimum and "
        "certify it with a dual solution, multiply polynomials through the FFT, and run the "
        "number theory behind RSA, down to counting the bases that expose a composite."
    ),
    "key": [
        "span, not processors, caps the speedup",
        "factor once, then solve each b in Θ(n²)",
        "the simplex walk moves edge by edge",
        "a dual solution certifies the optimum",
        "the FFT multiplies in Θ(n lg n)",
        "Euclid takes O(lg b) steps",
        "a witness proves a number composite",
    ],
    "assumes_short": "Graph Algorithms",
    "assumes_long": (
        "the earlier courses, especially Foundations for recurrences and the master method, "
        "Graph Algorithms for maximum flow and the max-flow min-cut theorem, and Strassen's "
        "method from Chapter 4; the lessons lean on Appendix D's matrices and Appendix C's "
        "probability where the book does, and on complex numbers in polar form for the FFT"
    ),
    "outcomes_intro": (
        "By the end you can carry each of these chapters' algorithms through by hand on a "
        "small instance, count what the chapter counts, and say which of your figures is a "
        "fact about that instance and which bound the book proves for every instance."
    ),
    "outcomes": [
        ("Analyse a multithreaded algorithm",
         "Compute the work, span and parallelism of a spawn-and-sync program, bound its time "
         "on P processors with the work law, the span law and the greedy theorem, and solve "
         "the span recurrences of P-FIB and multithreaded merge sort."),
        ("Solve a linear system by LUP decomposition",
         "Factor a small matrix with partial pivoting, solve by forward and back "
         "substitution, and explain why the pivot is the largest entry in its column."),
        ("Run and certify the simplex algorithm",
         "Convert a linear program to slack form, pivot to its optimum, read the optimal dual "
         "solution off the final slack form, and find a feasible start with the auxiliary "
         "program."),
        ("Multiply polynomials with the FFT",
         "Compute a small discrete Fourier transform by the even-odd recursion, invert it, "
         "and count butterflies against schoolbook multiplications."),
        ("Compute with large integers",
         "Run extended Euclid, solve linear congruences and Chinese remainder systems, "
         "exponentiate by repeated squaring, build an RSA key, and trace a Miller-Rabin "
         "base."),
    ],
    "syllabus_intro": (
        "Seven lessons follow chapters 27 to 31 in the book's order: one on multithreaded "
        "algorithms, one on linear systems, two on linear programming, one on the FFT, and "
        "two on number theory, the second of them on RSA and primality testing."
    ),
    "how_to": [
        "Read the sections before the lesson. This is a read-along of Cormen, Leiserson, "
        "Rivest and Stein, <em>Introduction to Algorithms</em>, 3rd edition (MIT Press, 2009), "
        "Chapters 27 to 31, with instances written for these lessons. Each lesson names its "
        "sections, opens with at most one short quotation, and sets out the argument in its "
        "own words; the book's pseudocode, figures and exercises are better read in the book, "
        "and the lessons point to them by name and number.",
        "Run the algorithm by hand once. Every lesson works a small instance on paper, a "
        "slack form, a transform of size 4, an RSA key with two-digit primes, before the lab "
        "runs it, because a figure you have computed yourself is the only kind you can check "
        "the lab against.",
        "Keep the count and the bound apart. The labs run each algorithm in your browser and "
        "print what it did on the input in front of them, beside the bound the chapter "
        "proves. The first is a fact about one input; the second holds for every input, and "
        "only its proof establishes that.",
        "Change the input. Most labs take your own matrix, polynomials or numbers, and each "
        "lesson ends by asking you to try one of your own. Nothing you type leaves your "
        "browser.",
    ],
    "not_covered": [
        "The book's pseudocode, figures and exercises. They are named in the lessons and left "
        "to the book; the instances in these lessons are written for them, except that the "
        "two linear-programming labs run their kits' built-in programs.",
        "Section 31.9 on integer factorization, and the full proofs of the starred material, "
        "which the lessons name and leave to the book.",
        "The chapter-end problems, among them Chapter 27's prefix computations and "
        "multithreaded LU decomposition, Chapter 28's splines, Chapter 29's complementary "
        "slackness and Farkas's lemma, and Chapter 30's FFT in modular arithmetic. They are "
        "worth working in the book.",
        "Numerical stability in floating point. Chapter 28 names it and leaves it to "
        "specialist texts; the matrix lab computes in exact fractions, and only the FFT lab "
        "works in floating point, with its rounding checked.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser by running the algorithm on "
        "the input a lesson states: work and span from exact recurrences, LUP factors as "
        "exact fractions, the bases a simplex walk visits, the links of a weak-duality chain, "
        "an FFT product checked against the schoolbook one, Euclid's divisions, and a count of "
        "Miller-Rabin witnesses over every base. A count describes one input; the book's "
        "bounds are proved for all of them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
