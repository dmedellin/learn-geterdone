"""Latency and the Tail."""


from . import part_a, part_b


COURSE = {
    "slug": "latency-and-the-tail",
    "title": "Latency and the Tail",
    "level": "Intermediate",
    "summary": (
        "Where a request's time goes: the speed-of-light floor, the round-trip count, "
        "the longest path through a stage graph, and the percentile arithmetic that "
        "explains why a fan-out of sixty-nine calls turns a p99 into a median."
    ),
    "blurb": (
        "A request is slow for one of four reasons &mdash; it went far, it went back and "
        "forth, it waited for the slowest of many, or it was the unlucky one in a "
        "hundred &mdash; and each has a number. The course puts a floor under latency "
        "with the speed of light, counts round trips, computes percentiles by rank, and "
        "builds the budget that a timeout and a retry have to fit inside."
    ),
    "key": [
        "RTT_min = 2d / (⅔c)                  NY–London ≈ 56 ms, whatever you buy",
        "t = k·RTT + bytes/bandwidth          k is usually what matters",
        "p99 = the ⌈0.99n⌉-th sorted value    a rank, not an average",
        "P(all n ≤ p99) = 0.99ⁿ               ½ at n = 69",
        "p99(A + B) < p99(A) + p99(B)",
    ],
    "assumes_short": "Course 1; independence and random variables",
    "assumes_long": (
        "course 1, plus independence, computing probabilities, random variables, "
        "cartesian products and tuples, and graph traversal from discrete mathematics, "
        "and roots and radicals from algebra"
    ),
    "outcomes_intro": (
        "By the end you can put a floor under a route, read a percentile off a sample, "
        "say what a fan-out does to it, add two stages correctly, and lay out a budget "
        "that a timeout and a retry fit inside."
    ),
    "outcomes": [
        ("Put a floor under a route and read a critical path",
         "The light-speed minimum for a distance, the fraction of a measured round trip "
         "it explains, and the longest path through a stage graph &mdash; the only "
         "stages whose speed-up changes the answer."),
        ("Compute percentiles from a sample, exactly",
         "p50, p95 and p99 by nearest rank, and the reason the mean is none of them and "
         "cannot be made into one."),
        ("Quantify what fan-out and hedging do to a tail",
         "The probability that all `n` independent calls clear their p99, the `n` at "
         "which a p99 becomes the median, and the tail and extra load a hedge at the "
         "p95 buys."),
        ("Add stages and lay out a budget",
         "The p99 of a two-stage sum by convolution &mdash; below the sum of the p99s "
         "&mdash; then a budget allocated backwards from an SLO with a timeout and "
         "retry count that fit inside it."),
    ],
    "syllabus_intro": (
        "The floors first (distance, round trips, the critical path), then the tail as "
        "an object, then what composition does to it, and last the budget that "
        "everything has to fit inside."
    ),
    "how_to": [
        "Sort the sample by hand once. The nearest-rank percentile is a position in a "
        "sorted list, and a reader who has done it once stops treating p99 as an "
        "average for good.",
        "Read the fan-out and the convolution labs together. They are the same fact "
        "twice &mdash; independence composing &mdash; once making the tail worse and "
        "once making it better than the naive sum.",
        "Keep milliseconds throughout. Mixing microseconds into a budget is the one "
        "arithmetic error this course reliably produces.",
    ],
    "not_covered": [
        "Where the tail comes from. Queueing is course 3; this course measures the tail "
        "and composes it.",
        "How the measurement could be lying. Coordinated omission, bucket error and "
        "scrape intervals are course 10.",
        'Congestion control as a subject. One bound &mdash; Mathis &mdash; is computed '
        'in &ldquo;Packet Loss and Throughput&rdquo; because it decides cross-region '
        'throughput; the algorithms behind it are not taught.',
    ],
    "footer_lead": (
        "Percentiles here are nearest rank, so every one printed is a value some request "
        "actually took. The convolution of two stage distributions is computed by "
        "enumerating pairs in exact fractions, which is why the sum's p99 can be "
        "compared with the sum of the p99s without a rounding argument. The one "
        "floating-point figure on the course is the Mathis bound's square root, and its "
        "lesson says so."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
