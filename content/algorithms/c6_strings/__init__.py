"""Strings and Pattern Matching."""


from . import part_a, part_b


COURSE = {
    "slug": "strings-and-pattern-matching",
    "title": "Strings and Pattern Matching",
    "level": "Advanced",
    "summary": (
        "The simplest matcher and the two texts that answer differently, the failure function "
        "built character by character rather than quoted, a table that removes comparison "
        "altogether, a shift that skips four fifths of the text and a text where it skips "
        "nothing, a hash whose collisions are printed with their characters, and the two "
        "structures that search for a whole dictionary and for questions nobody has asked yet."
    ),
    "blurb": (
        "This is the course where the asymptotically better algorithm loses, three times, on "
        "inputs one click apart. Naive matching beats Knuth&ndash;Morris&ndash;Pratt on prose "
        "with an absent pattern; Horspool beats both by a factor of three on English and loses "
        "to naive matching by a factor of five on a run of one letter; a rolling hash reports "
        "three positions that are not matches until the characters are compared. None of the "
        "bounds moves while any of that happens, and every page prints both columns."
    ),
    "key": [
        "m(n − m + 1)     naive and Horspool: the same worst case, attained by opposite inputs",
        "2n               KMP: the text pointer never moves backwards",
        "exactly n        the automaton: one lookup per character, whatever the text",
        "a hash equal is a CANDIDATE; the verification is the correctness argument",
        "output links chain SUFFIXES, so he is reported with she and abc never with abcd",
        "distinct substrings = n(n + 1)/2 − sum of the LCP array",
    ],
    "assumes_short": "Strings, induction, amortised analysis, modular arithmetic",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Strings and String Operations, Big-O, "
        "Big-Omega and Big-Theta, Analysing Iterative Algorithms, Loop Invariants and Program "
        "Correctness, Amortised Analysis, Strong Induction, Modular Arithmetic and Modular "
        "Exponentiation, and Trees. From this path: Data Structures and Their Cost Models, for "
        "the map and array trade the trie mode prints as two numbers, and Sorting and "
        "Selection, for the comparison counting every page here does. Geometric Algorithms and "
        "Randomised Algorithms assume nothing from this course and may be taken before it"
    ),
    "outcomes_intro": (
        "By the end you can state a matcher's proved bound and its measured cost on one input "
        "without confusing them, construct the worst case for any of the four matchers from "
        "its own rules, and say which of the two structures at the end answers a question the "
        "matchers cannot."
    ),
    "outcomes": [
        ("Separate a count from a bound on every page",
         "Naive matching makes 50 comparisons where its bound allows 123, and 100 where its "
         "bound allows 100. Both numbers are correct and only one of them is about all texts "
         "&mdash; and on a third input the count beats the algorithm with the better bound."),
        ("Build a worst case from an algorithm's own rules",
         "Read the shift rule and the comparison order as separate requirements and defeat each: "
         "the run of a's that makes Horspool five times slower than naive matching, and the "
         "reversed pattern on the same text that swaps the two numbers exactly."),
        ("Construct the preprocessing rather than quote it",
         "Borders found by trying every length beside the linear construction, the amortised "
         "total counted rather than asserted, and the transition table written out in full so "
         "that the failure function is recognisable as its compressed form."),
        ("Say what a hash establishes, and what it does not",
         "Three windows on the lab's prose share the pattern's residue and are not the pattern. "
         "The verification is not an optimisation to skip, the collision count is a property of "
         "the text and the modulus together, and the bound behind it is an expectation over a "
         "random modulus rather than a promise about the one chosen."),
    ],
    "syllabus_intro": (
        "The simplest matcher first, at its best, at its reversal and at its worst case, "
        "because every later algorithm is an answer to what it throws away; then three ways of "
        "keeping that information, from the failure function to a full transition table; then "
        "skipping, with its saving and its collapse; then hashing, where a new kind of wrong "
        "answer appears; and last the two structures that preprocess the patterns together or "
        "the text itself."
    ),
    "how_to": [
        "Read the two columns before reading the prose. Every lab on this course prints a "
        "measured count and a proved bound, and on four of the twelve opening inputs the "
        "algorithm with the better bound makes more comparisons. The counts move when you type "
        "and the bounds do not, and that is the difference the course is about.",
        "Change the preset before writing a conclusion down. Three pages share one lab and "
        "differ only in which text it opens on: &ldquo;Naive Matching, Measured and "
        "Bounded&rdquo;, &ldquo;Where the Simple Algorithm Wins&rdquo; and &ldquo;The Text "
        "Built to Reach the Bound&rdquo; have the same algorithm at 1.22, 1.00 and 5.00 "
        "comparisons per alignment. Any sentence that survives only one of them is a sentence "
        "about a text.",
        "Distrust a matcher that merely returned an answer. Six routines on these pages report "
        "match positions and every one of them is checked against comparing the whole substring "
        "at every offset, on your own text, on every keystroke &mdash; because an algorithm "
        "whose idea is skipping can skip over a match, and a shorter list of correct positions "
        "is the one wrong answer that looks right.",
    ],
    "not_covered": [
        "Boyer&ndash;Moore in full. The good-suffix rule needs a second table and a separate "
        "correctness argument, and the linear-time variants of it need a third; Horspool's "
        "single table is developed and counted here, and the sublinear bounds are stated "
        "nowhere.",
        "Suffix trees, suffix automata and the linear-time suffix array constructions. The "
        "array and its LCP array answer every question this course asks, and prefix doubling "
        "reaches them in `log2 n` rounds; building a suffix array in `O(n)` is a real "
        "improvement that changes no claim made here.",
        "Approximate matching. Edit distance is a dynamic program and is built on the "
        "preceding course; the string-specific machinery for approximate search &mdash; bit "
        "parallelism, the four-Russians speedup, filtering by exact seeds &mdash; is a separate "
        "subject and none of it appears.",
        "Compression, and the Burrows&ndash;Wheeler transform. The transform is the last column "
        "of the sorted rotations and is one step from the suffix array, which makes it "
        "tempting; it belongs with compression rather than with matching, and no page here "
        "needs it.",
    ],
    "footer_lead": (
        "Every count on this course is produced by running the matcher in your browser on the "
        "text in the box, and every count is a character comparison, an arithmetic step or a "
        "table lookup actually made. Comparison counts, alignment counts, shifts, characters "
        "skipped, table cells, trie nodes, collision counts and distinct-substring counts are "
        "exact integers; the ratios &mdash; comparisons per alignment, comparisons per "
        "character, average shift and table cells per text character &mdash; are exact "
        "fractions with a decimal printed beside them rather than instead of them. Every hash "
        "is an arbitrary-precision integer, so the three colliding windows the rolling-hash "
        "page lists are the same three on every machine and can be checked by hand from their "
        "code points. Six routines that report match positions are checked on every keystroke "
        "against comparing the whole substring at every offset; the failure function is checked "
        "against the longest border found by trying every length; the suffix array against "
        "sorting the suffixes as whole strings, and the LCP array against comparing each "
        "adjacent pair character by character; the prefix query against filtering the word "
        "list; and one Aho&ndash;Corasick pass word by word against scanning the text "
        "separately for each word. One quantity on this course is an average over a "
        "distribution rather than a measurement or a bound &mdash; Horspool's expected "
        "comparisons on a uniformly random text &mdash; and the page that names it says so and "
        "says what it therefore cannot promise about the input on screen."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
