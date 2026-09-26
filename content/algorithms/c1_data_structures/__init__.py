"""Data Structures."""


from . import part_a, part_b


COURSE = {
    "slug": "data-structures",
    "title": "Data Structures",
    "level": "Advanced",
    "summary": (
        "The structures every later algorithm stands on, each introduced by the operation "
        "it makes cheap and the operation it makes expensive: arrays and lists, stacks and "
        "queues, heaps, hash tables, search trees and their balancing, augmented trees, and "
        "union&ndash;find. Every cost is counted by running the operation and every bound is "
        "proved once."
    ),
    "blurb": (
        "Discrete Mathematics analysed algorithms and never built a structure to run one "
        "on. This course builds eight, and costs each by executing an operation sequence "
        "rather than by quoting a class &mdash; because the interesting facts here are all "
        "about the difference between a worst case, an amortised bound and an expectation, "
        "and those three are indistinguishable from a single fast run."
    ),
    "key": [
        "heap: parent ≤ children        array layout, children of i at 2i, 2i + 1",
        "Σ ⌈n/2ʰ⁺¹⌉·h  <  2n            build-heap is linear, n inserts are not",
        "chaining: Θ(1 + α) expected, Θ(n) worst — no hash function removes it",
        "AVL: |h_L − h_R| ≤ 1 everywhere  ⟹  h ≤ 1.44 log₂ n, by Fibonacci",
    ],
    "assumes_short": "Big-O, amortised analysis, trees and hashing",
    "assumes_long": (
        "Discrete Mathematics in full, and by name: Big-O Notation, Analysing "
        "Iterative Algorithms, Recursion Trees and Amortised Analysis, Trees, Tree "
        "Traversals, Graph Representations, Hashing and Pseudorandom Numbers, and "
        "Linearity of Expectation"
    ),
    "outcomes_intro": (
        "By the end you can cost an operation sequence on any of eight structures, say for "
        "each cost whether it is worst-case, amortised or expected, and choose a structure "
        "from a workload while naming what the choice cannot do."
    ),
    "outcomes": [
        ("Cost a sequence, and label the cost",
         "Run an operation sequence on a named structure and say whether its cost is "
         "worst-case, amortised or expected &mdash; three different promises that a single "
         "measurement cannot tell apart."),
        ("Operate each structure by hand",
         "Heap insert and extract, hash insert with chaining and with probing including "
         "deletion, search-tree insert and two-child delete, and AVL rebalancing with the "
         "case named."),
        ("Prove the four bounds",
         "Build-heap's `Σ h/2ʰ`, chaining's `1 + α`, AVL's Fibonacci height, and union by "
         "rank's `log n` &mdash; each proved once, and each one the reason a later course "
         "can quote a cost without re-deriving it."),
        ("Choose, and say what you gave up",
         "From an operation mix, pick among sorted array, hash table, AVL tree, heap and "
         "union&ndash;find, and name the operation the winner cannot answer at all."),
    ],
    "syllabus_intro": (
        "Sequences first, because their cost model is the vocabulary; then the three "
        "structures that trade a different thing for search &mdash; a heap trades order, a "
        "hash table trades order and worst case, a search tree trades constants; then "
        "balance, augmentation, and the one structure that is not a container at all."
    ),
    "how_to": [
        "Run the sequence before reading the bound. Every lab on this course counts an "
        "execution, and the number it prints is the answer for that sequence only. The "
        "bound is the lesson's claim about all of them.",
        "When a cost is amortised, find the expensive operation. It is still there, it "
        "still happens, and the guarantee is about the total. A reader who cannot point at "
        "it has read the bound as &ldquo;always fast&rdquo;.",
        "Break the structure deliberately. The degenerate key set, the sorted insertion "
        "order, the delete that empties a slot: each lab can produce the input that "
        "defeats its structure, and that input is the lesson.",
    ],
    "not_covered": [
        "Red&ndash;black trees and B-trees. AVL stands in for balance, and B-trees are "
        "about disk &mdash; System Design's &ldquo;The Height of a B-tree&rdquo; costs one "
        "in I/O, which is the reason they exist.",
        "Fibonacci heaps, and AVL deletion. Both are stated and neither is developed; the "
        "first changes Dijkstra's bound and no lesson here depends on the change.",
        "The proof of union&ndash;find's `α(n)` bound. The statement is used; the proof is "
        "out of scope, and &ldquo;Union&ndash;Find&rdquo; says so in those words.",
        "Cache-aware and persistent structures. The cost model here is the word RAM, where "
        "every access costs one.",
    ],
    "footer_lead": (
        "Every count on this course is produced by executing the operation sequence on the "
        "structure drawn beside it. Expected chain lengths and load factors are exact "
        "fractions; `Σ ⌈n/2ʰ⁺¹⌉·h` is evaluated exactly. Two numbers are approximations "
        "and say so: linear probing's `½(1 + 1/(1−α)²)`, which is Knuth's and which the lab "
        "refuses to quote at all above `α = 0.98`, and the `2 ln n` expected depth of a "
        "random search tree, which is asymptotic and is printed beside the height and the "
        "mean depth that were measured."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
