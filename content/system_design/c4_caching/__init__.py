"""Caching and Hit Rates."""


from . import part_a, part_b


COURSE = {
    "slug": "caching-and-hit-rates",
    "title": "Caching and Hit Rates",
    "level": "Intermediate",
    "summary": (
        "The miss rate as the number that matters: what it does to the backend and to "
        "the tail, how skew decides the size, what a policy is worth on a trace, what a "
        "TTL costs in staleness, and what happens in the second after a hot key expires."
    ),
    "blurb": (
        "A cache is a number &mdash; the miss rate &mdash; and every decision about it is "
        "arithmetic on that number: what it does to the backend, what it does to the "
        "average and to the tail, how big the cache must be given how skewed the requests "
        "are, how stale it is allowed to be, and what happens in the second after a hot "
        "key expires."
    ),
    "key": [
        "backend load = (1 − h)λ              90% → 99% is a 10× cut, not 9% better",
        "E[latency] = h·t_hit + (1 − h)·t_miss",
        "h(C) = H(C,s) / H(N,s)               Zipf: the top keys carry the traffic",
        "stampede size = λ·d                  one, with coalescing",
        "global miss = (1 − h₁)(1 − h₂ | miss)",
    ],
    "assumes_short": "Courses 1 and 3; expectation and conditioning",
    "assumes_long": (
        'Capacity Estimation and Queues and Utilisation. Discrete Mathematics '
        '“Expected Value”, “Conditional Probability” and “Independence”. Algebra '
        '“Piecewise Functions” and “Sigma Notation”.'
    ),
    "outcomes_intro": (
        "By the end you can convert a hit rate into backend load and into latency, size a "
        "cache from the skew of its workload, judge a policy on a trace, and price the two "
        "failure modes a cache has: staleness and the stampede."
    ),
    "outcomes": [
        ("Turn a hit rate into backend load and latency",
         "`(1 − h)λ` and the `ρ` it leaves the backend at, the mean latency by "
         "expectation, and the reason the p99 is the miss latency whenever the miss rate "
         "is at least one per cent."),
        ("Size a cache from the skew",
         "The top-`k` share under a Zipf popularity as a ratio of harmonic numbers, the "
         "`C` that reaches a target hit rate, and the diminishing returns that make the "
         "next nine expensive."),
        ("Judge a replacement policy on a trace",
         "Hits for FIFO, LRU, LFU and farthest-in-future at two cache sizes, with the "
         "optimum as the bound and Belady&rsquo;s anomaly as the reason a bigger cache is "
         "not a guarantee."),
        ("Price staleness and the stampede",
         "The stale fraction for a TTL against an update interval, the miss rate a short "
         "TTL buys, the `λ·d` requests that pass through at expiry, and what coalescing "
         "reduces them to."),
    ],
    "syllabus_intro": (
        "What the miss rate does first, then what decides it (skew, size, policy), then "
        "the two ways a cache goes wrong, and last the two places a cache is something "
        "else: a second level, and a CDN."
    ),
    "how_to": [
        "State the miss rate, not the hit rate, whenever you are talking about the "
        "backend. Ninety per cent and ninety-nine per cent sound adjacent; ten per cent "
        "and one per cent do not, and the backend sees the second pair.",
        'Run the policy lab at two cache sizes before reading the anomaly lesson. Seeing '
        'FIFO lose hits when the cache grows is more convincing than the sentence that '
        'says it does.',
        "Treat the TTL formula as a sensitivity, not a prediction. It assumes periodic "
        "updates and a uniform refresh phase, and the timeline in the lab exists so that "
        "you can see the assumption rather than take it.",
    ],
    "not_covered": [
        "Cache coherence protocols; this course&rsquo;s caches are independent copies with "
        "a TTL, not a coherent memory system.",
        'CPU caches beyond the latency table of “Latency Numbers on a Log Scale”.',
        "Eviction implementations &mdash; the data structures that make LRU cheap are "
        "Algorithms&rsquo; business, not this course&rsquo;s.",
    ],
    "footer_lead": (
        "Hit rates, harmonic sums, stale fractions and policy hit counts on this course "
        "are exact fractions. The Zipf normaliser `H(N, s)` is summed exactly for "
        "catalogues up to about fifty keys, which is where its exact form stays readable; "
        "past that the lab prints a rounded value and says so."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
