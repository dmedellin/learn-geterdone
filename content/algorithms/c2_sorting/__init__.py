"""Sorting and Selection."""


from . import part_a, part_b


COURSE = {
    "slug": "sorting-and-selection",
    "title": "Sorting and Selection",
    "level": "Advanced",
    "summary": (
        "Everything the comparison lower bound leaves open: what a sort promises beyond "
        "order, quicksort and the expected analysis it needs, heapsort, the sorts that do "
        "not compare, selection in linear time, the adversary arguments that bound what any "
        "algorithm can do, and how sorting is actually done at scale."
    ),
    "blurb": (
        "Discrete Mathematics proved no comparison sort beats `n log n`. That leaves open "
        "everything that matters: stability, whether the bound applies at all, what "
        "randomness buys, and how close to the bound a real sort gets. This is also the "
        "course where the analysis becomes probabilistic &mdash; randomised quicksort's "
        "exact expectation is the pattern every later expectation on this path follows."
    ),
    "key": [
        "stable: equal keys keep input order  ⟹  multi-key sort by successive passes",
        "E[comparisons] = 2(n+1)Hₙ − 4n       exact, and on EVERY input",
        "counting sort: Θ(n + k)              and k can be 2³²",
        "T(n) ≤ T(n/5) + T(7n/10) + cn        linear because 1/5 + 7/10 < 1",
    ],
    "assumes_short": "The comparison bound, divide and conquer, heaps",
    "assumes_long": (
        "searching and sorting, analysing iterative algorithms, divide and conquer, "
        "recursion trees and amortised analysis, expected value, linearity of expectation "
        "and permutations, all from discrete mathematics; and priority queues and binary "
        "heaps, and building a heap in linear time, from the data structures course on "
        "this path"
    ),
    "outcomes_intro": (
        "By the end you can classify any sort on four promises, derive randomised "
        "quicksort's expectation with indicator variables and check it against a measured "
        "mean, and prove a lower bound by playing an adversary."
    ),
    "outcomes": [
        ("Classify a sort on four promises",
         "Stability, in-place, adaptivity and comparison versus key-based &mdash; and pick "
         "one for a stated key domain and memory limit, which is a different question from "
         "picking the fastest."),
        ("Run seven algorithms by hand",
         "Partition, quicksort, heapsort, counting sort, radix sort, quickselect and median "
         "of medians, each with its counter and its invariant."),
        ("Derive an expectation and check it",
         "The indicator argument for `2(n+1)Hₙ − 4n`, evaluated exactly as a fraction and "
         "compared with a mean over seeds &mdash; and the reason it holds for every input "
         "rather than for a typical one."),
        ("Prove a lower bound by adversary",
         "Answer comparisons so as to keep the most outcomes alive, for the maximum, for "
         "min-and-max together, and for the second largest &mdash; then meet each bound "
         "with an algorithm."),
    ],
    "syllabus_intro": (
        "What a sort promises, then quicksort and the expectation it needs, then the sorts "
        "that escape the comparison bound by not comparing, then selection, then the lower "
        "bounds, then sorting at a scale where the cost model changes."
    ),
    "how_to": [
        "Read the pivot rule as a claim about inputs. Every deterministic rule has a bad "
        "input and the lab will build it; randomisation moves the randomness from the data "
        "to the algorithm, which is the whole distinction of &ldquo;Randomised "
        "Quicksort&rdquo;.",
        "Count before you classify. A sort that is `Θ(n + k)` is linear only for the `k` "
        "you actually have, and the lab plots both terms.",
        "Play the adversary. &ldquo;Adversary Arguments&rdquo; is the one place on this "
        "path where the reader is asked to defeat an algorithm rather than run one.",
    ],
    "not_covered": [
        "Sorting networks and parallel sorts. The cost model here is sequential.",
        "Shellsort, and Timsort's run-merging policy. Timsort's <em>shape</em> &mdash; "
        "runs, then merges, with insertion sort below a cutoff &mdash; is in "
        "&ldquo;k-Way Merging and Sorting in Practice&rdquo;; its galloping and run-stack "
        "rules are not.",
        "Cache-oblivious analysis, and sorting linked lists.",
    ],
    "footer_lead": (
        "Every comparison count on this course is produced by running the sort on the array "
        "shown. `2(n+1)Hₙ − 4n` is evaluated as an exact fraction over BigInt, so the "
        "measured mean and the exact expectation can be compared as numbers rather than as "
        "decimals that nearly agree. The one place this course rounds is the plotted curve "
        "`n log₂ n`, which is a drawing, not a claim."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
