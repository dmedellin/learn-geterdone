"""Randomised Algorithms."""


from . import part_a, part_b


COURSE = {
    "slug": "randomised-algorithms",
    "title": "Randomised Algorithms",
    "level": "Advanced",
    "summary": (
        "What a coin buys, and what it costs to say so honestly. A randomised algorithm's "
        "cost is a distribution rather than a number, so every page here prints three "
        "things that are never the same: the exact quantity over every execution, the mean "
        "over the seeds on screen, and the bound the lesson proves &mdash; with the word "
        "always or the words with high probability attached to it, and a run shown where "
        "the second kind does not hold."
    ),
    "blurb": (
        "Everywhere else on this path a measured count sits beside a proved bound. Here the "
        "thing being bounded is itself random, and the easiest mistake in the subject is to "
        "run an algorithm a hundred times, take the average, and call it the expectation. "
        "So the labs enumerate: every tape of a shuffle, every execution of a quicksort, "
        "every contraction order, every base, every assignment. The exact fraction and the "
        "sample sit in the same row, and the gap between them is what the course is about."
    ),
    "key": [
        "a cost is a DISTRIBUTION:  28 always,  2369/140 expected,  415/24 measured",
        "P(X ≥ a) ≤ E[X]/a            Markov, for a non-negative X",
        "P(|X − μ| ≥ t) ≤ Var(X)/t²   Chebyshev, which is Markov on (X − μ)²",
        "n! does not divide nⁿ, so the naive swap CANNOT be uniform",
        "always  /  with high probability  /  in expectation      say which",
        "P(some minimum cut) = 19/35 against a bound of 1/15, and 53 seeds of 120 missed",
        "E[clauses satisfied] = 7m/8, so some assignment reaches it",
    ],
    "assumes_short": "Expectation and variance, linearity, modular exponentiation, search trees",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Sample Spaces and Events, Computing "
        "Probabilities, Independence, Random Variables, Expected Value, Linearity of "
        "Expectation, Variance and Standard Deviation, and The Geometric Distribution and "
        "Waiting Times, whose statement of Chebyshev's inequality this course finally "
        "proves; Modular Exponentiation and Fermat's Little Theorem and Euler's Theorem, "
        "for the primality tests; Hashing and Pseudorandom Numbers, for the generator every "
        "lab here draws from; and Permutations and Combinations. From this path: Data "
        "Structures, for hash tables and binary search trees, whose randomised versions are "
        "built here; Sorting and Selection, whose Randomised Quicksort derives the "
        "expectation this course turns into a distribution; and Graph Algorithms, for cuts "
        "and for the graph representation Karger's algorithm contracts"
    ),
    "outcomes_intro": (
        "By the end you can say which of three numbers on a page is a guarantee, prove a "
        "tail bound from an expectation, tell a one-sided error from a two-sided one, and "
        "give an exact answer to the question &ldquo;how many times do I have to run "
        "this?&rdquo;"
    ),
    "outcomes": [
        ("Tell an expectation from a sample",
         "Every lab here prints the exact quantity over every execution, as a fraction, "
         "beside the mean over the seeds on screen. On the opening quicksort they are "
         "`2369/140` and `415/24`, and moving one slider moves the second and not the "
         "first. Neither is wrong and neither is the other."),
        ("Turn an expectation into a probability",
         "Prove Markov's inequality from the definition of expectation, derive Chebyshev's "
         "from it by applying it to `(X − μ)²`, and then read both against the exact tail "
         "the lab computes &mdash; including the instance where Markov returns a number "
         "above one and is therefore true and useless."),
        ("Say which kind of guarantee you have",
         "Always, with high probability, or in expectation. Quicksort never exceeds "
         "`n(n − 1)/2`; Karger returns a given minimum cut with probability at least "
         "`2/(n(n − 1))`; a random assignment satisfies `7m/8` clauses on average. Each "
         "page names its kind and shows a run where the middle one fails."),
        ("Cost the repetition that makes a guarantee usable",
         "One contraction succeeds with probability `19/35`; six independent runs reach "
         "`99/100`, and the panel computes the smallest number that does by multiplying "
         "rather than by taking a logarithm. The same arithmetic prices a primality test at "
         "`1024/1690522737399` after five bases."),
    ],
    "syllabus_intro": (
        "Sampling first, because a shuffle is the smallest place a distribution can be "
        "enumerated whole; then the cost of an algorithm as a distribution, and the two "
        "inequalities that turn one into a probability. Then linearity of expectation, "
        "which needs no independence and pays for four results in a row. Then the two "
        "guarantees a randomised algorithm can offer and what repetition does to each. "
        "Last, four structures that put the coin inside the data structure rather than "
        "beside it."
    ),
    "how_to": [
        "Read the three columns as three different questions before you read any number in "
        "them. Exact means over every execution the algorithm has, computed as a fraction. "
        "Measured means over the seeds the slider names, and it moves when the slider "
        "moves. A bound is what the proof gives for every instance of the problem, and its "
        "distance from the exact column is the slack the proof left on the table.",
        "Move the seed slider before you write a measured number down, and move the "
        "instance before you generalise a bound. The two do different damage: the first "
        "shows you how far a sample wanders around a fixed truth, and the second shows you "
        "which quantities were properties of the instance all along. &ldquo;The Cost Is a "
        "Distribution&rdquo; is built so that changing the input moves one number on the "
        "page and leaves the other two exactly where they are.",
        "When a page says with high probability, go and find the failure. Karger's lab "
        "lists the seeds that returned the wrong cut, Miller&ndash;Rabin's prints the bases "
        "that testify to nothing, and the satisfiability lab counts the assignments that do "
        "worse than average. A probabilistic guarantee whose failure you have never seen is "
        "a guarantee you have not understood.",
    ],
    "not_covered": [
        "Chernoff and Hoeffding bounds, and everything that needs them. That is the largest "
        "deliberate hole on this path: it is why the maximum load of `n` balls in `n` bins "
        "is stated and proved nowhere in this library, why the Count-Min sketch is given "
        "its Markov guarantee rather than the sharper textbook one, and why no lesson here "
        "claims a concentration result. Markov and Chebyshev are proved and used; anything "
        "stronger is named as absent.",
        "Randomised complexity classes. The one-sided and two-sided errors this course "
        "measures are exactly the distinction those classes are built on, and naming them "
        "would add vocabulary without adding a computation. Intractability and Approximation "
        "uses the probabilistic method from here and defines no new class either.",
        "Derandomisation beyond the existence argument. This course proves that an "
        "assignment reaching `7m/8` exists because the average does, and stops there. "
        "Walking the conditional expectations down to that assignment is a real algorithm "
        "and it is built nowhere in this library.",
        "Markov chain Monte Carlo, mixing times and rapidly mixing chains. The Operations "
        "Research path builds Markov chains and their steady states; how quickly a chain "
        "forgets where it started is a different subject, and no lab here runs one.",
    ],
    "footer_lead": (
        "Every probability, expectation, variance, tail and bound on this course is an exact "
        "ratio of two integers held as BigInt, and the decimals beside them are long "
        "division of those integers rather than floating point. The distributions are "
        "enumerated, not sampled: every tape of a shuffle, every execution of a randomised "
        "quicksort by recursion over subproblem sizes, every contraction order by recursion "
        "over contraction states, every base from 2 to `n − 2`, every assignment of a "
        "formula, and every bipartition when a minimum cut is checked. Where a sample "
        "appears it is labelled a measurement, it names the number of seeds it ran, and the "
        "exact quantity it estimates is printed in the same row &mdash; no page here prints "
        "one without the other. Three quantities are genuinely approximate and each is "
        "labelled where it is printed: `2 ln n` as an asymptote for the mean depth of a "
        "randomly built search tree, `2 log₂ n` as a reference curve for a skip list's hops, "
        "and a Bloom filter's rate under the independent-hash idealisation, which is printed "
        "beside the exact rate so the gap between them is visible. Two more are quoted and "
        "established nowhere in this library: the maximum load of `n` keys in `n` bins with "
        "one choice and with two. They are labelled STATED, NOT PROVED in those words, "
        "because their proofs need Chernoff bounds and this course excludes them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
