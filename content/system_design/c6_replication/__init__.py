"""Replication and Consistency."""


from . import part_a, part_b


COURSE = {
    "slug": "replication-and-consistency",
    "title": "Replication and Consistency",
    "level": "Advanced",
    "summary": (
        "What replication costs in write work, latency and staleness: order statistics for synchronous writes and quorums, a lag distribution for stale reads, overlap arithmetic for `(N, R, W)`, and consistency turned into counts — of concurrent pairs, of valid linearizations, of lost updates."
    ),
    "blurb": (
        "Replication is bought in three currencies — write work, latency and staleness — and the course prices each. Reads scale by `N` and writes do not; a synchronous write waits for the slowest replica and a quorum for the `W`-th fastest; a follower read is stale with a probability read off the lag distribution; and “consistency” becomes a count — of concurrent pairs in a vector-clock diagram, of valid linearizations of a history, of updates a last-writer-wins merge throws away."
    ),
    "key": [
        "N replicas: N× reads, 1× writes, N× write work and storage",
        "P(all N−1 acked by t) = F(t)^(N − 1)   the slowest, not the average",
        "R + W > N  ⟹  overlap ≥ R + W − N",
        "miss probability = C(N−W, R)/C(N, R)   2/3 at N = 3, R = W = 1",
        "2f + 1 tolerates f                     a fourth node adds nothing to three",
    ],
    "assumes_short": "Latency and the Tail and Availability and Failure; combinations, partial orders, permutations",
    "assumes_long": (
        "latency and the tail and availability and failure from this path, plus "
        "combinations, the pigeonhole principle, partial orders, permutations, the "
        "binomial distribution, computing probabilities and independence from discrete "
        "mathematics"
    ),
    "outcomes_intro": (
        "By the end you can price a replication factor in four currencies, read a staleness probability off a lag distribution, decide whether a quorum configuration overlaps, and turn three consistency questions into counts you can check."
    ),
    "outcomes": [
        ("Price a replication factor",
         "Read capacity, write capacity, write work and storage for `N` replicas, and the read/write ratio that Capacity Estimation taught you to measure, which decides whether that trade pays."),
        ("Compute replication's two latencies and its staleness",
         "The p99 of a synchronous write as the maximum of `N − 1` replicas, the p99 of a quorum as the `W`-th fastest, and the probability a follower read at delay `t` is stale."),
        ("Decide and size a quorum",
         "Whether `(N, R, W)` overlaps and by how much, the miss probability when it does not, and the fault tolerance and availability of a majority."),
        ("Turn consistency into a count",
         "Lamport and vector timestamps from a message diagram with the concurrent pairs counted, the valid linearizations of a short history enumerated, and the updates a last-writer-wins merge discards against a counter CRDT that discards none."),
    ],
    "syllabus_intro": (
        "What replication costs first, then its two latencies and its staleness, then quorums, and last the three questions that turn “consistent” into something countable."
    ),
    "how_to": [
        "Compute the binomial tail in “Quorum Latency: the W-th Fastest” before reading its conclusion. That more replicas make a fixed-`W` quorum <em>faster</em> is the one result on this course that most readers refuse until they have computed it.",
        "Draw the message diagram yourself before stamping it. Vector clocks are mechanical once the happens-before edges are on the page and confusing before.",
        "Take the six-operation cap on the linearizability lab seriously. It is there because the enumeration is factorial, and that fact is a lesson about why real checkers do not enumerate.",
    ],
    "not_covered": [
        "Consensus log mechanics — Raft replication, snapshots, membership change. Only the quorum arithmetic, majority availability and election timing are here.",
        "Transactions and isolation levels; CAP and PACELC as slogans. What this course carries instead are the measurable consequences — lag, staleness, overlap and the sloppy-quorum miss.",
        "CRDT design beyond the counter of “Conflict Resolution, Counted”.",
    ],
    "footer_lead": (
        "Every probability on this course is exact: the order statistics are computed from enumerated distributions, the quorum tails are binomial sums over exact fractions, the overlap counts are combinations, and the linearizations are enumerated rather than estimated. Where a lab caps its input size — six operations for the linearizability check — the cap is the factorial growth of the enumeration, and the lesson says so."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
