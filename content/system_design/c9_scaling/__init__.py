"""Scaling Laws and Cost."""


from . import part_a, part_b


COURSE = {
    "slug": "scaling-laws-and-cost",
    "title": "Scaling Laws and Cost",
    "level": "Intermediate",
    "summary": (
        "What another machine actually buys, and what capacity costs when you pay "
        "for the peak: Amdahl&rsquo;s ceiling, the Universal Scalability Law&rsquo;s "
        "peak and decline, and the break-evens for batching, reservation, tiering, "
        "compression and moving data against moving compute."
    ),
    "blurb": (
        "Adding a machine buys less than a machine&rsquo;s worth, and sometimes less "
        "than nothing; paying for capacity buys more than you use, by a ratio you can "
        "compute. The course fits Amdahl&rsquo;s ceiling and the Universal Scalability "
        "Law&rsquo;s peak, prices batching, reserved capacity, autoscaling lag and "
        "storage tiers, and closes with two transfer break-evens."
    ),
    "key": [
        "S(n) = 1/((1−p) + p/n) → 1/(1−p)     5% serial caps at 20×",
        "C(N) = N/(1 + α(N−1) + βN(N−1))      peaks, then falls",
        "waste = 1 − mean·ρ_target/peak",
        "u* = reserved price / on-demand price",
        "shortfall = r·τ·(D − τ/2)            unless a reserve of r·τ is held",
    ],
    "assumes_short": (
        "Capacity Estimation, Queues and Utilisation, Partitioning and Load Balancing "
        "and Storage Engines and Indexes; asymptotes and optimisation"
    ),
    # esc(...).capitalize() -- so this is written lowercase-first, with no
    # backticks: both would ship literally.
    "assumes_long": (
        "capacity estimation, queues and utilisation, partitioning and load balancing "
        "and storage engines and indexes, plus recursion trees and amortised analysis "
        "from discrete mathematics, and graphs and asymptotes, maximum and minimum "
        "problems and compound interest and continuous growth from algebra"
    ),
    "outcomes_intro": (
        "By the end you can say what the next machine buys, locate the point past "
        "which it buys nothing, and compute the five break-evens that decide how "
        "capacity is bought rather than how much of it there is."
    ),
    "outcomes": [
        ("Compute what parallelism buys and where it stops",
         "Amdahl&rsquo;s speedup, its ceiling read off the asymptote, the `n` that "
         "reaches ninety per cent of it, and the Universal Scalability Law&rsquo;s "
         "peak &mdash; after which more machines are worse."),
        ("Price a batch and a machine shape",
         "Per-item cost against added latency for a batch size, and horizontal "
         "against vertical capacity with the break-even found by evaluation and the "
         "single box&rsquo;s missing parallel path named."),
        ("Compute what capacity costs when you pay for the peak",
         "Waste from a peak-to-mean profile, the reserved against on-demand "
         "break-even utilisation and the cost-minimising split, and the shortfall an "
         "autoscaling lag leaves."),
        ("Compute the three transfer break-evens",
         "The accesses per month at which a cold tier stops paying, the bandwidth at "
         "which compressing stops paying, and the result-to-input ratio that decides "
         "whether to move the data or the compute."),
    ],
    "syllabus_intro": (
        "What another machine buys first, then what a batch and a machine shape cost, "
        "then the three ways capacity is paid for, and last the three break-evens "
        "about moving bytes."
    ),
    "how_to": [
        "Read Amdahl&rsquo;s ceiling off the asymptote rather than from a table. The "
        "interesting claim is that a ceiling exists at all, and the asymptote is where "
        "you see it.",
        "Scan the Universal Scalability Law rather than differentiating it. The peak "
        "is found by evaluating at integer `N`, and the closed form is checked against "
        "the scan, not used in place of it.",
        "Do every break-even as an equality before you interpret it. Each one on this "
        "course is a single equation set to zero, and the interpretation is easier "
        "once the algebra is already done.",
    ],
    "not_covered": [
        "Vendor pricing, discount structures and FinOps process. Prices are inputs.",
        "Fitting `α` and `β` for the Universal Scalability Law. That is regression; "
        "here they are given and the peak is computed.",
        "Capacity planning under uncertainty beyond the ranges of "
        "&ldquo;Capacity Estimation&rdquo;.",
    ],
    "footer_lead": (
        "Speedups, break-evens, waste fractions and per-request costs on this course "
        "are exact fractions of the rational inputs you set, which is what makes a "
        "break-even a crossing you can locate rather than a decimal you have to trust. "
        "The Universal Scalability Law is evaluated at integer machine counts exactly "
        "and its closed-form peak, which is a square root, is printed rounded and "
        "labelled."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
