"""Course 8 — Algorithms and Complexity."""

from . import part_a, part_b

COURSE = {
    "slug": "algorithms-and-complexity",
    "title": "Algorithms and Complexity",
    "level": "Advanced",
    "summary": (
        "How to say how long an algorithm takes and why it matters: correctness and "
        "termination, growth of functions, big-O with explicit witnesses, analysis of "
        "iterative and recursive algorithms, greedy and dynamic programming, complexity "
        "classes, and the limits of computation."
    ),
    "blurb": (
        (
        'The course the rest of the path was building toward. Recurrences from Induction and Recursion, counting from Combinatorics and Counting and graphs from Graphs and Trees all reappear as the running time of something &mdash; and the last two lessons say what no algorithm can do.'
    )
    ),
    "key": [
        "f(n) = O(g(n))   ⟺   ∃C, k.  f(n) ≤ C·g(n)  for all n ≥ k",
        "T(n) = aT(n/b) + nᵈ   ⟹   compare log_b a with d",
        "P ⊆ NP;  whether the inclusion is strict is open",
        "some problems have NO algorithm at all",
    ],
    "assumes_short": "Induction, recurrences, and graphs",
    "assumes_long": "especially induction, recurrences and graphs",
    "outcomes_intro": (
        "By the end you can analyse an algorithm you are shown and recognise when a "
        "problem is likely to be intractable."
    ),
    "outcomes": [
        ("Prove a bound with witnesses",
         "Big-O is an existence claim about a constant and a threshold. Producing them "
         "is the proof; quoting the class is not."),
        ("Analyse loops and recursions",
         "Counting the operations of an iterative algorithm, and solving a "
         "divide-and-conquer recurrence with the master theorem."),
        ("Recognise the two design techniques",
         "Greedy where it is provably correct, dynamic programming where it is not "
         "&mdash; and be able to say which and why."),
        ("Place a problem",
         "P, NP, NP-complete, undecidable. Knowing which of those a problem is in "
         "changes what you should attempt."),
        ("Prove an algorithm right, and bound a sequence",
         'An invariant for partial correctness and a decreasing measure for termination (“Correctness and Termination”); the cost of a whole sequence of operations rather than the worst single one (“Recursion Trees and Amortised Analysis”); and the lower bound no comparison sort beats (“Searching and Sorting”).'),
    ],
    "syllabus_intro": (
        'First what an algorithm is and what correctness means, then analysis, then design, and last the limits.'
    ),
    "how_to": [
        'Produce the witnesses. Every big-O claim in “Big-O, Big-Omega and Big-Theta” comes with a `C` and a `k`, and the lab searches for them; a claim without them is a slogan. When the relation is false the lab says so from the growth classes and shows the ratio diverging, because no finite search can refute a claim about every `n`.',
        "Use the measured columns. The lab counts operations by running the algorithms, so the predicted growth can be compared with something rather than believed. Each lesson's lab opens on that lesson's own example &mdash; the invariant trace of “Correctness and Termination”’s `POWER(3, 13)`, “Analysing Iterative Algorithms”’s four loop nests, “Searching and Sorting”’s counts at `n = 16`, “Divide and Conquer”’s `4T(n/2) + n`, “Recursion Trees and Amortised Analysis”’s sixteen inserts, “Dynamic Programming”’s table to 8 &mdash; and every panel quotes what the lab prints there.",
        'Take “Decidability and the Halting Problem” seriously. Undecidability is not a statement about current technology, and the halting proof is short enough to follow completely.',
    ],
    "not_covered": [
        "Data structures as a subject: heaps, balanced trees, hash tables and their "
        "analyses. They appear where an algorithm needs one and are not developed.",
        "Randomised and approximation algorithms beyond passing mentions, and the "
        "average-case analysis that quicksort needs.",
        'Formal models of computation. Turing machines are described in “Decidability and the Halting Problem” only as far as the halting problem requires.',
    ],
    "footer_lead": (
        "Every operation count on this course is produced by executing the algorithm "
        "with a counter, on a deterministic input, so the measured column is a "
        "measurement. Where it diverges from the predicted growth the reason is stated "
        "rather than smoothed over."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
