"""Capacity Estimation."""


from . import part_a, part_b


COURSE = {
    "slug": "capacity-estimation",
    "title": "Capacity Estimation",
    "level": "Intermediate",
    "summary": (
        "Back-of-envelope arithmetic done honestly: rates between per-day and "
        "per-second, storage as a sum over a retention window, bandwidth in bits, "
        "peak against mean, and the machine count that falls out &mdash; each "
        "carried with the error bar its inputs deserve."
    ),
    "blurb": (
        "Ten million users, a hundred actions a day, a kilobyte each: how much "
        "machine is that? The course teaches estimation as arithmetic with error "
        "bars &mdash; every factor is a range, every product is a wider range, and "
        "an estimate that arrives as a single number is hiding its width. It ends "
        "by checking an estimate the only honest way, by a second route that shares "
        "no assumption with the first."
    ),
    "key": [
        "1 day ≈ 10⁵ s                       15.7% high, and worth it",
        "three factors ±2×  ⟹  product ±8×",
        "storage = ingest × retention × replication, plus growth",
        "N = ⌈peak / (capacity × ρ_target)⌉   an integer, with headroom named",
    ],
    "assumes_short": "School algebra: exponents, ratios, log scales",
    "assumes_long": (
        "algebra: scientific-notation, integer-exponents, "
        "ratio-proportion-and-percent, logarithmic-scales, "
        "arithmetic-sequences-and-series, geometric-sequences-and-series"
    ),
    "outcomes_intro": (
        "By the end you can turn a population into a rate, a rate into storage and "
        "bandwidth, and a peak into a machine count &mdash; and say, for each, how "
        "wide the answer is and which assumption would move it."
    ),
    "outcomes": [
        ("Convert a rate and know what the shortcut cost",
         "Per-day to per-second and back with the `10⁵`-second day, stating the "
         "`15.7%` error it introduces and when that error matters."),
        ("Multiply factors that are ranges",
         "Three factors each known to a factor of two give a product known to a "
         "factor of eight; report `[lo, hi]` and the width in powers of ten rather "
         "than a single number."),
        ("Size storage, bandwidth and memory",
         "From an ingest rate, a retention window, a growth rate and a replication "
         "factor; in bits where the link is measured in bits; and for the hot "
         "fraction rather than the whole dataset."),
        ("Produce a machine count and then check it",
         "An integer `N` from peak load, per-request cost and a named headroom "
         "&mdash; then a second route sharing no assumption with the first, and the "
         "ratio between them against the range."),
    ],
    "syllabus_intro": (
        "Ranges first, because everything after is a product of them; then the four "
        "things a rate sizes &mdash; storage, bandwidth, machines, memory &mdash; "
        "and last the check."
    ),
    "how_to": [
        "Write the unit chain down before computing anything. Nearly every wrong "
        "capacity estimate is a unit error, and the lab prints the chain so that a "
        "missing `/s` is visible rather than merely wrong.",
        "Keep the range to the end. The lab carries `[lo, hi]` through every step; "
        "the temptation is to collapse to the midpoint early, and the last lesson "
        "is about what that costs.",
        "Do the second route before looking at the first answer again. "
        "Triangulation only works when the two routes are built independently, "
        "which is a fact about the order you do them in.",
    ],
    "not_covered": [
        "Prices. What a machine or a gigabyte costs belongs to Scaling Laws and "
        "Cost; this course counts machines and gigabytes.",
        "Latency. How long a request takes belongs to Latency and the Tail; this "
        "course counts how many of them arrive.",
        "Why the headroom is what it is. The target utilisation is taken as given "
        "here and earned in Queues and Utilisation, where the knee explains it.",
    ],
    "footer_lead": (
        "Every range on this course is computed as an exact interval: the product "
        "of `[lo, hi]` intervals is `[∏lo, ∏hi]` in exact arithmetic, so the "
        "approximation is in the inputs and the lesson, never in the lab. The "
        "geometric mean of an interval is a square root and is printed rounded, "
        "labelled."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
