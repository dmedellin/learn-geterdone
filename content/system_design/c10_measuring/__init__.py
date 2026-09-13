"""Measuring Systems."""


from . import part_a, part_b


COURSE = {
    "slug": "measuring-systems",
    "title": "Measuring Systems",
    "level": "Advanced",
    "summary": (
        "How the measurement lies, and by how much: averaged percentiles, bucket "
        "error, coordinated omission, scrape intervals, sampling of rare events, "
        "metric cardinality, load-test length, and the arithmetic of burn-rate and "
        "threshold alerts."
    ),
    "blurb": (
        "Every earlier course produced a number; this one asks how you would know it "
        "from a live system, and shows the four ways the measurement lies: "
        "percentiles that were averaged, histograms with wide buckets, load "
        "generators that skipped the slow requests, and scrape intervals that never "
        "saw the spike. It ends with the arithmetic of sampling, cardinality, "
        "load-test length and alerts."
    ),
    "key": [
        "SE = √(p(1−p)/n)             1 000 requests cannot tell 99.9% from 99.8%",
        "fleet p99 = p99 of the merged sample, never the mean of per-host p99s",
        "P(catch a spike of length d) = min(1, d/I)",
        "P(see the top 0.1% in n) = 1 − 0.999ⁿ      95% needs about 3 000",
        "pages/week = P(false alarm per window) × windows",
    ],
    "assumes_short": (
        "Latency and the Tail and Availability and Failure; binomials, variance, "
        "the product rule"
    ),
    # esc(...).capitalize() -- so this is written lowercase-first, with no
    # backticks: both would ship literally.
    "assumes_long": (
        "latency and the tail, and availability and failure, plus the binomial "
        "distribution, the geometric distribution and waiting times, the sum and "
        "product rules, variance and standard deviation and expected value from "
        "discrete mathematics"
    ),
    "outcomes_intro": (
        "By the end you can put an error bar on an indicator of service quality, "
        "aggregate percentiles without inventing one, correct two measurement "
        "biases, and size a sample, a load test and an alert so that each sees what "
        "it claims to see."
    ),
    "outcomes": [
        ("Put a ± on a measured ratio",
         "The standard error of an indicator from its window size, the `n` needed to "
         "resolve a tenth of a per cent, and the reason a short window&rsquo;s 99.95% "
         "is not evidence of meeting a 99.9% objective."),
        ("Aggregate and bucket percentiles honestly",
         "The fleet p99 from merged samples against the mean of per-host p99s on the "
         "same data, and the interval a histogram&rsquo;s p99 is actually known to."),
        ("Correct the two biases a measurement introduces",
         "Coordinated omission, corrected by imputing the requests a stalled "
         "generator never sent; and the spike a scrape interval cannot see, with the "
         "longest invisible one named."),
        ("Size a sample, a test and an alert",
         "The sampling rate that captures a rare event, the number of requests a "
         "load test needs to see its p99.9, the label cardinality a metric costs, "
         "and the false-alarm rate a threshold produces on a noisy ratio."),
    ],
    "syllabus_intro": (
        "The error bar on a ratio first, because every later lesson is about a "
        "ratio; then the three ways an aggregate lies; then the arithmetic of what a "
        "sample can and cannot see; and last the two alert calculations."
    ),
    "how_to": [
        "Compute the standard error before arguing about any measured ratio. Most "
        "disagreements about whether an objective was met are disagreements about a "
        "number whose error bar contains both positions.",
        "Do the aggregation lesson on data where the answer is surprising. The mean "
        "of per-host p99s can land below the fleet median, and the lab has a preset "
        "where it does.",
        "Treat every alert threshold as a statement about the sample, not about the "
        "system. The last page computes what a threshold fires at when nothing at "
        "all has changed.",
    ],
    "not_covered": [
        "Tracing systems, dashboard design and the operational tooling around "
        "metrics.",
        "Statistical inference beyond these direct calculations &mdash; no "
        "hypothesis tests, no confidence intervals by a normal approximation, no "
        "regression.",
        "Anomaly detection as a technique. &ldquo;Threshold Alerts and False "
        "Alarms&rdquo; computes a false-alarm rate; it does not propose a detector.",
    ],
    "footer_lead": (
        "The percentile arithmetic on this course is exact and is done on the "
        "samples you edit, so that the fleet p99 and the average of per-host p99s "
        "are two numbers you can see differ rather than a claim you have to accept. "
        "Capture probabilities, cardinalities, load-test lengths and false-alarm "
        "rates are exact fractions. The one rounded figure is the standard error of "
        "a proportion, which is a square root, and its lesson says so."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
