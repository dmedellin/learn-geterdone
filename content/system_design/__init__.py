"""The System Design path, as data.

Ten courses in one order. The content lives here and only here; scripts/
turns it into pages. Nothing in this package emits markup beyond the inline
`x` shorthand, and nothing in scripts/ decides what a lesson says.

Every figure this path prints is computed in the browser from the model the
lesson states. The engine is scripts/mathpath/labs/sysdesign_core.py, on top
of algebra_core's rationals: rates, counts, percentiles by nearest rank,
availabilities, quorum overlaps, queue lengths at rational utilisations and
convolved latency distributions are exact fractions rather than decimals that
are nearly them.
"""

from . import (
    c1_capacity,
    c2_latency,
    c3_queues,
    c4_caching,
    c5_availability,
    c6_replication,
    c7_partitioning,
    c8_storage,
    c9_scaling,
    c10_measuring,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_capacity.COURSE,
    c2_latency.COURSE,
    c3_queues.COURSE,
    c4_caching.COURSE,
    c5_availability.COURSE,
    c6_replication.COURSE,
    c7_partitioning.COURSE,
    c8_storage.COURSE,
    c9_scaling.COURSE,
    c10_measuring.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

PATH = {
    "slug": "system-design",
    "title": "System Design",
    "level": "Intermediate → Advanced",
    "level_note": 'discrete probability and algebra are assumed',
    "tagline": (
        'Every decision a system designer makes that has a number attached, taught as that number: capacity from rates and retention, latency from distance and round trips, waiting from utilisation and variability, availability as a product of probabilities, replication as lag and overlap, partitioning as balls into bins, storage as I/O counts, scaling as a ceiling, and measurement as the arithmetic that tells you whether any of it is true. Ten courses and 114 lessons are available.'
    ),
    "description": (
        'The System Design Subject: ten courses in one order, from back-of-envelope capacity through latency and the tail, queueing, caching, availability, replication, partitioning, storage engines, scaling laws and cost, to the measurement of a running system. Every lesson closes on a number the reader computes in the lab and can check by hand, and every model states the assumption it rests on. All ten courses and 114 lessons are available.'
    ),
    "key": [
        "L = λW                               an identity about a trace, not a model",
        "W = S/(1 − ρ)                        0.9 → 0.99 multiplies the wait by 10",
        "P(all n calls ≤ their p99) = 0.99ⁿ   one half at n = 69",
        "A = ∏Aᵢ   series        A = 1 − ∏(1 − Aᵢ)   parallel, given independence",
        "h(C) = H_{C,s} / H_{N,s}             a small cache of a skewed workload",
        "R + W > N  ⟹  every read set meets every write set",
    ],
    "sequence_intro": (
        'Each course assumes the ones before it and the two prerequisite paths, and nothing else. Latency and the Tail supplies the percentile vocabulary that Queues and Utilisation explains the origin of; Caching, Availability, Replication and Partitioning are four applications of one probability toolkit, each adding a single tool; Storage, Cost and Measuring consume numbers produced by all of the others.'
    ),
    "why_order": [
        'Capacity Estimation comes first because every later number begins as a rate. A reader who cannot turn ten million users into requests per second, with an error bar they can defend, cannot start any of the nine courses that follow &mdash; and the habit of carrying the error bar is the course&rsquo;s real content.',
        'Latency and the Tail precedes Queues and Utilisation because queueing is the explanation and the tail is the thing explained. Percentiles, fan-out amplification and the convolution of two stages have to exist as objects before &ldquo;why is the p99 like that&rdquo; is a question with an answer.',
        'Caching, Availability, Replication and Partitioning are four applications of the same probability, in increasing order of what they add: conditional hit rates, then binomials and products, then order statistics, then balls into bins. Each could stand alone; in this order each one&rsquo;s new tool is the only new thing in it.',
        'Storage Engines, Scaling Laws and Cost, and Measuring Systems come last because each consumes numbers from all of the others. A page cache is the cache of course 4, a shard count is the machine count of course 1 under two constraints, and the last course asks the question the whole path has been deferring: how would you know any of this from a system that is running?',
    ],
    "prerequisites": [
        'The Algebra path through course 9, and the Discrete Mathematics path through course 8. Specifically: scientific notation, logarithmic scales, geometric series and asymptotes from Algebra; independence, conditional probability, expectation, variance, the binomial and geometric distributions, combinations, partial orders, modular arithmetic and the seeded generator from Discrete Mathematics. Each course names the slugs it uses.',
        'No calculus and no continuous probability. Where this path needs the exponential or the Poisson distribution it builds them as limits of the geometric and the binomial you already have, and no lesson writes a density or an integral.',
        'No programming and no operational experience. The labs run the models for you; nothing asks you to write code, configure a service or have carried a pager.',
        'Willingness to distrust a number you just computed. The arithmetic on this path is easy, and every wrong answer in it comes from an assumption &mdash; independence, memorylessness, a steady state &mdash; that was true of the model and not of the system.',
    ],
    # The hazard of learning THIS subject from interactive examples is its own.
    # Algebra's characteristic error is the invented law; System Design's is the
    # model that answers confidently about a system it does not describe. A lab
    # cannot check an assumption, so every lesson has to name its own.
    "material": (
        "every figure on this path is computed in your browser from the model "
        "the lesson states, and a model&rsquo;s answer is only as true as its "
        "assumptions &mdash; independence, memorylessness and steady state are "
        "named where they are used, and each lesson says where its own fails."
    ),
    "footer_lead": (
        '<strong>Educational course material.</strong> Every figure on this path is computed in your browser from the model the lesson states. Rates, counts, percentiles by nearest rank, availabilities, quorum overlaps, queue lengths at rational utilisations and convolved latency distributions are all exact fractions, not decimals that are nearly them. Six quantities on the path are genuinely irrational &mdash; a standard error, a square root, `e^(−x)`, a Bloom filter&rsquo;s rate, a Zipf normaliser past the point where its exact form is readable, and the Universal Scalability Law&rsquo;s peak &mdash; and every lesson that prints one says that it is rounded and how. What the labs cannot do is check an assumption: a model that assumes independence will report a confident number for a system whose failures are correlated, and naming that gap is what each lesson closes on.'
    ),
    "courses": COURSES,
}
