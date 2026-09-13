"""Partitioning and Load Balancing."""


from . import part_a, part_b


COURSE = {
    "slug": "partitioning-and-load-balancing",
    "title": "Partitioning and Load Balancing",
    "level": "Advanced",
    "summary": (
        "Splitting data and traffic as a balls-into-bins problem: how uneven a hash actually is, what fraction of keys move when `N` changes, what one hot key does regardless of `N`, why sampling two bins beats one, and what a query that must visit every shard costs."
    ),
    "blurb": (
        "Splitting data or traffic across `N` nodes is a balls-into-bins problem, and the course measures it: how uneven a hash actually is, what fraction of keys move when `N` changes, what one hot key does to the hottest shard regardless of `N`, why sampling two bins beats one so dramatically, and what a query that must visit every shard costs."
    ),
    "key": [
        "N = max(⌈λ_peak/(c·ρ)⌉, ⌈D·RF/per-node⌉)   two constraints, take the max",
        "mod N → mod N+1 moves N/(N+1);  a ring moves 1/(N+1)",
        "hottest = f·λ + (1 − f)λ/N          a hot key does not care about N",
        "two choices: ln n/ln ln n  →  ln ln n   stated, not proved; measured here",
        "P(k random keys on one shard) = N¹⁻ᵏ",
    ],
    "assumes_short": "Queues and Utilisation, Replication and Consistency; hashing, variance, combinations",
    "assumes_long": (
        "queues and utilisation and replication and consistency from this path, plus "
        "modular arithmetic, hashing and pseudorandom numbers, expected value, variance "
        "and combinations from discrete mathematics, and ratio, proportion and percent "
        "from algebra"
    ),
    "outcomes_intro": (
        "By the end you can choose a shard count under two constraints, measure the "
        "imbalance a hash actually produces, price the three things that change it, and "
        "cost the two queries that sharding makes expensive."
    ),
    "outcomes": [
        ("Choose and re-choose a shard count",
         "The count from load, capacity and target utilisation, the count from storage "
         "and replication factor, the binding one — and the fraction of keys that move "
         "when the count changes, under mod-`N` and under a ring."),
        ("Measure imbalance rather than assume it",
         "Max-over-mean on a seeded hashed placement, the improvement from `V` virtual "
         "nodes, and the write share a monotonic key sends to one range."),
        ("Price a hot key and a straggler",
         "The hottest shard's load before and after salting, and the expected and p99 "
         "completion of a job that ends with its slowest partition."),
        ("Cost the queries sharding makes expensive",
         "A scatter-gather's shard requests and latency tail, a global against a local "
         "secondary index with the crossover ratio, the cross-shard fraction of a `k`-key "
         "transaction, and the hours a rebalance takes."),
    ],
    "syllabus_intro": (
        "How many shards first, then how evenly the keys actually land and what moves "
        "when the count changes, then the three sources of imbalance, and last the "
        "queries and operations that cross shards."
    ),
    "how_to": [
        "Reseed the placement labs several times. A single seeded run of balls into bins "
        "is one sample; the lesson is about the distribution of the maximum, and that "
        "only shows up across seeds.",
        "Read the rehashing fractions as a pair. That `N/(N+1)` and `1/(N+1)` sum to one "
        "is the whole argument for consistent hashing and takes one line.",
        "Keep “shard” and “replica” apart. A shard is a piece of the data; a replica is a "
        "copy of a piece. “Replication and Consistency” replicated; this course splits.",
    ],
    "not_covered": [
        "Shard-router internals and the mechanics of a resharding algorithm — the cost is "
        "computed in “Rebalancing Cost”; the algorithm is not.",
        "Geo-partitioning and data-residency constraints.",
        "Proofs of the maximum-load asymptotics. They are stated and measured; see the "
        "notes in “Hash Partitioning and Imbalance” and “The Power of Two Choices”.",
    ],
    "footer_lead": (
        "The placements on this course are produced by a seeded generator defined on the "
        "page, so a “random” assignment is a computed one that you can reproduce and step "
        "through. The fractions of keys moved, the shard counts, the hot-key shares and "
        "the cross-shard probabilities are exact. The two maximum-load results — "
        "`Θ(log n / log log n)` for one choice and `≈ ln ln n` for two — are stated, not "
        "proved, and what the labs do is measure them."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
