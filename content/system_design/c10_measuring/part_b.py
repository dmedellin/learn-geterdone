"""Measuring Systems, lessons 06-10 - sampling, cardinality, test length, and the two alerts."""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "sampling-and-rare-events",
        "title": "Sampling and Rare Events",
        "module": "Sizing samples and alerts",
        "one_line": "Compute the chance a sampling rate catches at least one event of a rare problem, and the rate a stated confidence requires.",
        "summary": (
            "Sampling one request in a hundred does not show you one per cent of a "
            "problem. A problem made of ten requests is caught with probability "
            "`1 − (1 − s)¹⁰`, which at one per cent is 9.56% &mdash; so it is missed "
            "nine times in ten, and reaching ninety-five per cent confidence takes a "
            "rate of 25.9%, not 10%. Sampling the tail instead fixes the capture "
            "problem and breaks the average, and the repair is to count each sampled "
            "request `1/s` times."
        ),
        "key": [
            "P(capture ≥ 1 of k at rate s) = 1 − (1−s)ᵏ",
            "s = 1%, k = 10   →  9.56% caught,  90.44% missed entirely",
            "95% confidence on k = 10 needs s = 259/1000 — 26× the rate, not 10×",
            "keep everything over 100 ms and the mean reads 203.69 ms",
            "count each sampled request 1/s times and it returns to 9.34 ms exactly",
        ],
        "key_label": "What a sampling rate can and cannot see",
        "concepts_intro": (
            "One formula and one repair. The formula is the same `1 − (1 − p)ᵏ` that "
            "fan-out amplification uses, and it is about to be used twice more on this "
            "course."
        ),
        "concepts": [
            ("A rate is a per-event probability, and a problem is many events",
             "Sampling at `s` keeps each request independently with probability `s`, so "
             "a problem that manifests in `k` requests is missed entirely with "
             "probability `(1 − s)ᵏ` and seen at all with probability `1 − (1 − s)ᵏ`. "
             "The intuition that a one per cent sample shows one per cent of everything "
             "is right about totals and wrong about existence: it gives `s·k = 0.1` "
             "expected captures, and the expected number of captures being a tenth is "
             "exactly why the probability of any capture is small."),
            ("Confidence in a rare event costs far more rate than it looks",
             "Solving `1 − (1 − s)¹⁰ ≥ 0.95` gives `s ≥ 25.9%`: to move from 9.56% "
             "confidence to 95% takes twenty-six times the sampling rate, not ten "
             "times. The relationship is exponential in `k` and nothing like linear in "
             "`s`, which is why &ldquo;let us raise sampling from 1% to 10% and see&rdquo; "
             "is a decision that buys 65% confidence and feels like it should buy more."),
            ("Sampling the tail is a good sample and a dishonest average",
             "Keep every request over a threshold and sample the rest at `s`, and you "
             "capture every slow request while shrinking the volume &mdash; the right "
             "trade for finding problems. The sampled set is then not representative, "
             "so its plain mean is meaningless: on the lab&rsquo;s traffic it reads "
             "203.69 ms against a true 9.34. Dividing each kept request by its own "
             "inclusion probability before averaging recovers the true mean exactly."),
        ],
        "read_title": "The capture probability, the rate it takes, and the mean sampling ruins",
        "read_intro": (
            "Why one per cent sampling misses a ten-request problem nine times in ten, "
            "what confidence costs, and how to average a sample that was deliberately "
            "biased."
        ),
        "body": [
            ("def", ("Sampling rate, and capture",
                     "Under <strong>uniform sampling</strong> at rate `s`, each event "
                     "is retained independently with probability `s`. A problem that "
                     "produces `k` events is <strong>captured</strong> if at least one "
                     "of them is retained. The capture probability is",
                     "`1 − (1 − s)ᵏ`,",
                     "which depends on `k` as strongly as it depends on `s` &mdash; a "
                     "fact the phrase &ldquo;one per cent sampling&rdquo; hides "
                     "completely, because it names only one of the two.")),
            ("math", [
                "s = 1/100,  k = 10",
                "",
                "missed   (1 − s)ᵏ = (99/100)¹⁰ = 0.904382075…      90.44%",
                "caught   1 − that                = 0.095617925…      9.56%",
                "",
                "expected captures   s·k = 0.1",
                "",
                "the rule of thumb 1 − e^(−s·k) = 1 − e^(−0.1) = 9.516%",
                "differs from the exact 9.562% by 0.045 percentage points",
            ]),
            ("p", "The last two lines are a small lesson of their own. The "
                  "`1 − e^(−sk)` form is an approximation, and the lab computes it by a "
                  "series that rounds at about `10⁻¹³`; the gap between the two columns "
                  "is `4.5 × 10⁻⁴`, nine orders of magnitude larger. An approximation "
                  "and a rounded approximation are different kinds of wrong, and only "
                  "one of them gets smaller if you compute harder."),
            ("h3", "The rate a stated confidence needs"),
            ("p", "Turn it round: given `k` and a target confidence `c`, find the "
                  "smallest `s` with `1 − (1 − s)ᵏ ≥ c`. The lab scans the thousandths "
                  "and reports the first that clears the bar, which avoids a logarithm "
                  "and gives an exact fraction."),
            ("math", [
                "want   1 − (1 − s)¹⁰ ≥ 95/100",
                "       (1 − s)¹⁰      ≤  5/100",
                "",
                "scan s = 1/1000, 2/1000, … :",
                "   s = 250/1000   (3/4)¹⁰  = 0.0563   → 94.37%, short",
                "   s = 259/1000            = 0.0499…  → 95.01%, first to clear",
                "",
                "so 25.9% sampling, against 1% — a factor of 26 for a factor of 10",
                "in confidence",
            ]),
            ("p", "Ten per cent sampling, the obvious compromise, gives "
                  "`1 − 0.9¹⁰ = 65.13%` &mdash; better than a coin toss and not a "
                  "guarantee of anything. If a problem must be visible whenever it "
                  "occurs, uniform sampling is the wrong instrument at any rate you can "
                  "afford, and the answer is to stop sampling uniformly."),
            ("h3", "Tail-biased sampling, and the average it breaks"),
            ("p", "Keep every request slower than a threshold and sample the rest. Now "
                  "every slow request survives, which is what you wanted, and the "
                  "retained set over-represents the tail by a factor of `1/s`. Any "
                  "statistic computed naively on the retained set is a statistic of a "
                  "population that does not exist."),
            ("math", [
                "true traffic    5 ms × 900    8 ms × 60    12 ms × 30    400 ms × 10",
                "                                                        n = 1 000",
                "true mean       (4 500 + 480 + 360 + 4 000)/1 000 = 9 340/1 000",
                "                                                  = 9.34 ms",
                "",
                "keep all ≥ 100 ms, sample the rest at s = 1/100:",
                "  retained        10 slow  +  990/100 = 9.9 of the fast",
                "  naive mean      (4 000 + 53.4)/19.9 = 4 053.4/19.9 = 203.69 ms",
                "",
                "reweight: divide each retained request by its own keep probability",
                "  slow counted ×1        fast counted ×100",
                "  (4 000 + 5 340)/(10 + 990) = 9 340/1 000 = 9.34 ms     exactly",
            ]),
            ("p", "The reweighted figure is not an approximation of the true mean: it "
                  "is the true mean, recovered exactly, because the weights are the "
                  "reciprocals of known inclusion probabilities. This is the "
                  "Horvitz&ndash;Thompson estimator, and it is the whole content of "
                  "&ldquo;remember to divide by the sampling rate&rdquo;."),
            ("p", "It does not rescue everything. A weighted mean is easy; a weighted "
                  "percentile needs the weights carried into the rank, and a naive "
                  "percentile of a tail-biased sample is far worse than a naive mean "
                  "because it is the tail that was over-kept. If your pipeline samples "
                  "non-uniformly, every statistic downstream of it needs to know the "
                  "rate, and the rate has to travel with the data."),
            ("example", ("Two teams, one trace pipeline",
                         "The platform team samples traces at 1% uniformly, so the "
                         "trace store holds one request in a hundred and its averages "
                         "are honest. A customer reports ten slow requests; the "
                         "probability any of them is in the store is 9.56%, and nobody "
                         "finds anything.",
                         "They switch to keeping every request over 100 ms plus 1% of "
                         "the rest. Now all ten are there. A week later a dashboard "
                         "built on the same store reports a mean latency of 203.69 ms "
                         "and an incident is declared about a service whose true mean "
                         "is 9.34 ms. Both problems are the same decision seen from "
                         "two ends, and the fix is to store the rate alongside the "
                         "request rather than to choose between the two failures.")),
        ],
        "lab": ("measure", {
            "mode": "sample",
            "panel_title": "Set the rate and the problem",
            "panel_intro": (
                "The capture probability is exact, printed as a fraction beside the "
                "percentage, and the rate needed for a stated confidence is found by "
                "scanning the thousandths rather than by a logarithm. The table&rsquo;s "
                "third column is the `1 − e^(−sk)` rule of thumb, kept beside the exact "
                "answer so the gap between an approximation and a rounding is visible "
                "rather than asserted."
            ),
        }),
        "steps_title": "Choosing a sampling rate for something you must not miss",
        "steps_intro": (
            "The rate is a consequence of two numbers: how many events the problem "
            "makes, and how sure you need to be."
        ),
        "steps": [
            ("Say how many events the problem produces",
             "`k` is the number of requests, traces or log lines the thing you are "
             "hunting will generate. A ten-request problem and a ten-thousand-request "
             "problem need completely different rates, and &ldquo;rare&rdquo; without a "
             "number cannot be sized."),
            ("Compute 1 − (1 − s)ᵏ at the rate you have",
             "If the answer is under a half, your current pipeline is a coin toss you "
             "lose. Quote it as a probability of capture rather than as a sampling "
             "percentage, because the two numbers are wildly different and only one of "
             "them answers the question."),
            ("Solve for the rate your confidence needs",
             "Scan `s` upward until `1 − (1 − s)ᵏ` clears the target. Then price it: "
             "the rate multiplies storage and ingest directly, and 25.9% sampling is "
             "a quarter of full volume."),
            ("If the price is impossible, sample non-uniformly instead of lowering the bar",
             "Keep everything that is already interesting &mdash; errors, slow "
             "requests, a named customer &mdash; and sample the rest. Capture becomes "
             "certain for the events you selected on, at a fraction of the volume."),
            ("Carry the rate with the data",
             "Every record needs to know the probability it was kept with, or no "
             "downstream statistic can be corrected. Reweighting recovers a mean "
             "exactly; it can only do so if the weight survived the trip."),
        ],
        "worked": {
            "title": "One per cent sampling against a ten-request problem",
            "intro": [
                "The first half is the capture arithmetic and the second half is what "
                "the obvious fix does to an average. Both use the lab&rsquo;s preset "
                "traffic, and every figure except the rule-of-thumb column is exact.",
            ],
            "lines": [
                "PART ONE — CAPTURE",
                "",
                "  s = 1/100      k = 10 requests",
                "",
                "  missed   (99/100)¹⁰ = 0.904382075…            90.44%",
                "  caught   1 − (99/100)¹⁰                        9.56%",
                "  expected captures   s·k = 0.1",
                "",
                "  at other rates, same k = 10:",
                "     s =  1%   →   9.56%",
                "     s =  5%   →  40.13%",
                "     s = 10%   →  65.13%",
                "     s = 25%   →  94.37%",
                "     s = 25.9% →  95.01%       first rate to clear 95%",
                "",
                "PART TWO — THE MEAN",
                "",
                "  traffic   5 ms × 900   8 ms × 60   12 ms × 30   400 ms × 10",
                "  true mean = 9 340/1 000 = 9.34 ms",
                "",
                "  keep all ≥ 100 ms, sample the rest at 1%:",
                "    kept       10 slow requests, 9.9 fast ones",
                "    total      4 000 + 53.4 = 4 053.4 ms over 19.9 requests",
                "    naive mean 203.69 ms                     ×21.8 the truth",
                "",
                "  reweighted: slow ×1, fast ×100",
                "    (4 000 + 5 340) / (10 + 990) = 9 340/1 000 = 9.34 ms",
            ],
            "after": [
                "The two halves pull in opposite directions and that is the shape of "
                "the problem. Uniform sampling gives an honest average and cannot find "
                "a rare event; tail-biased sampling finds every rare event and gives a "
                "dishonest average. Reweighting is what lets you have both, and it "
                "costs nothing except carrying one number per record.",
                "The factor of 21.8 is worth remembering as an order of magnitude "
                "rather than a constant: it is roughly the ratio of the tail value to "
                "the true mean, scaled by how much of the body was thrown away. Push "
                "the sampling rate down and it grows.",
                "For faded practice, take a problem of `k = 40` requests at `s = 1%`. "
                "The supplied first move is `(99/100)⁴⁰`. Compute the capture "
                "probability, then find the rate that reaches 95% for this larger `k`, "
                "and say in one sentence why the answer is so much smaller than 25.9% "
                "even though the confidence target did not change.",
            ],
        },
        "quiz_title": "Rates, captures and weighted means",
        "quiz": [
            {"q": "A problem manifests in exactly 10 requests. Your tracing pipeline samples at 1%. What is the probability that at least one of the ten is in the store?",
             "a": ["1%", "10%", "9.56%", "90.44%"],
             "c": 2,
             "why": "`1 − (99/100)¹⁰ = 0.09562`. The 10% answer is the expected number of "
                    "captures expressed as a percentage of nothing in particular &mdash; "
                    "`s·k = 0.1` &mdash; which is close to the right answer here only "
                    "because both are small. `90.44%` is the probability of missing it "
                    "entirely."},
            {"q": "To reach 95% confidence of catching that same ten-request problem, what sampling rate is needed?",
             "a": ["About 10%", "About 25.9%", "About 50%", "About 95%"],
             "c": 1,
             "why": "`(1 − s)¹⁰ ≤ 0.05` first holds at `s = 259/1000`. Ten per cent gives "
                    "`1 − 0.9¹⁰ = 65.13%`, which is the intuitive answer and is not close. "
                    "Note the shape: twenty-six times the rate for the extra confidence, "
                    "because the relationship is exponential in `k`."},
            {"q": "A pipeline keeps every request over 100 ms and 1% of the rest. On traffic whose true mean is 9.34 ms, the retained set averages 203.69 ms. What is the right repair?",
             "a": ["Discard the slow requests before averaging",
                   "Count each retained request `1/s` times &mdash; slow ones once, sampled ones a hundred times &mdash; before taking the mean",
                   "Multiply the retained mean by the sampling rate",
                   "Raise the threshold until the retained mean matches the true one"],
             "c": 1,
             "why": "Each record is weighted by the reciprocal of its own inclusion "
                    "probability, which returns `9 340/1 000 = 9.34` exactly. Discarding "
                    "the slow requests throws away the reason the sample was taken; "
                    "multiplying by `s` is a rescaling that happens to be wrong by the "
                    "ratio of the two populations; tuning the threshold to match a known "
                    "answer is fitting, not measuring."},
            {"q": "Your team raises uniform trace sampling from 1% to 10% to improve incident debugging on problems of about ten requests. What did that buy?",
             "a": ["Ten times the capture probability, from 9.56% to 95.6%",
                   "Capture probability from 9.56% to 65.13%, at ten times the storage",
                   "Nothing, since the capture probability depends only on `k`",
                   "Certainty, since the expected number of captures is now 1"],
             "c": 1,
             "why": "`1 − 0.9¹⁰ = 65.13%`. The rate rose by a factor of ten and so did the "
                    "bill; the confidence went from very bad to unreliable. An expected "
                    "count of 1 is not certainty &mdash; it is the level at which about a "
                    "third of occurrences still produce nothing at all."},
        ],
        "mistakes": [
            ("Reading the sampling rate as the fraction of a problem you will see",
             "&ldquo;One per cent sampling sees one per cent of every problem&rdquo; is "
             "true of totals over millions of requests and false of any individual "
             "incident. What a rate gives you for a `k`-event problem is "
             "`1 − (1 − s)ᵏ`, and at small `s·k` that is close to `s·k` &mdash; a tenth "
             "of one capture, meaning almost always none at all."),
            ("Scaling the rate linearly with the confidence you want",
             "Going from 9.56% to 95% confidence takes twenty-six times the rate, not "
             "ten. The reason is that the confidence is `1 − (1 − s)ᵏ` and the quantity "
             "that scales cleanly is `(1 − s)ᵏ`, the probability of missing. Halving "
             "the miss probability is what costs a fixed amount of rate, and you need "
             "to halve it four times over."),
            ("Averaging a deliberately biased sample",
             "The moment a pipeline keeps &ldquo;all errors plus 1% of successes&rdquo; "
             "or &ldquo;everything over 100 ms&rdquo;, every plain mean and every plain "
             "percentile computed downstream describes a population that was never "
             "served. The repair is one division per record and it must happen before "
             "the aggregation, not after it."),
        ],
        "standard": ("Finish when a sampling rate is quoted with the capture probability it implies for a stated k.",
                     "You should be able to compute `1 − (1 − s)ᵏ`, solve it for the "
                     "rate a confidence requires, say why the answer is nothing like "
                     "linear, and reweight a non-uniform sample so that its mean is the "
                     "population mean again."),
        "note": "Keeping everything is the alternative to sampling, and it has its own "
                "arithmetic: every distinct combination of label values is a separate "
                "series, stored for ever. &ldquo;Metric Cardinality&rdquo; multiplies "
                "five ordinary labels into 3 456 000 series and 39.81 GB a day, and "
                "then adds one more label that multiplies it by ten thousand.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "metric-cardinality",
        "title": "Metric Cardinality",
        "module": "Sizing samples and alerts",
        "one_line": "Compute the series count a set of labels produces and the bytes a day it costs, and price one more label before adding it.",
        "summary": (
            "A metric with labels is not one time series; it is one series per distinct "
            "combination of label values, so the count is the product of the "
            "cardinalities. Five ordinary labels give 3 456 000 series, which at a "
            "fifteen-second scrape and two bytes a sample is 39.81 GB a day. Adding a "
            "label is not adding a column &mdash; it is multiplying, and a label with "
            "ten thousand values multiplies the whole bill by ten thousand."
        ),
        "key": [
            "series = ∏ label cardinalities    40 × 120 × 6 × 30 × 4 = 3 456 000",
            "samples per day = 86 400 ÷ I      I = 15 s → 5 760",
            "bytes per day = series × samples per day × bytes per sample",
            "3 456 000 × 5 760 × 2 = 39 813 120 000 B = 39.81 GB/day",
            "add user_id at 10 000 values → 34 560 000 000 series, 398 TB/day",
            "a label is a multiplier, and an unbounded label is an unbounded one",
        ],
        "key_label": "What a label costs",
        "concepts_intro": (
            "One product, one multiplication, and the operational consequence that the "
            "arithmetic does not show."
        ),
        "concepts": [
            ("A labelled metric is one series per combination of values",
             "`http_requests_total{service, endpoint, status, instance, method}` is not "
             "a metric with five columns. It is a family, and every distinct tuple of "
             "values that has ever been observed is its own time series with its own "
             "retained history. The count is the product of the cardinalities, and a "
             "product of five modest numbers is not a modest number."),
            ("The storage is the series count times the sample rate times the sample size",
             "Each series is written once per scrape, so the daily sample count per "
             "series is `86 400/I`. Multiply by the bytes a compressed sample occupies "
             "&mdash; a couple of bytes in a modern format, because timestamps and "
             "values in a slowly changing series compress extremely well &mdash; and "
             "the total falls out. Every one of the three factors is a decision "
             "somebody made."),
            ("Series that stop being written do not stop costing",
             "The product counts combinations that exist; the index counts "
             "combinations that have <em>ever</em> existed. An `instance` label that "
             "changes on every deploy adds a fresh set of series each release and the "
             "old ones remain in the index until they age out of retention. This is "
             "called churn, it is invisible in the product above, and it is the usual "
             "reason a metrics system that was sized correctly falls over three months "
             "later."),
        ],
        "read_title": "The product, the bytes, and the label that should not exist",
        "read_intro": (
            "How a series count is computed, what it turns into per day, and which "
            "labels multiply a system out of existence."
        ),
        "body": [
            ("def", ("Time series and cardinality",
                     "A <strong>time series</strong> is identified by a metric name "
                     "together with a complete set of label values. The "
                     "<strong>cardinality</strong> of a label is the number of distinct "
                     "values it takes. For a metric with labels of cardinality "
                     "`c₁, …, c_m`, the number of series is at most",
                     "`∏ cᵢ = c₁ × c₂ × … × c_m`,",
                     "reached when every combination occurs. Real systems reach some "
                     "fraction of it, and the product is the number to plan against.")),
            ("math", [
                "service    40",
                "endpoint  120",
                "status      6",
                "instance   30",
                "method      4",
                "                       40 × 120 × 6 × 30 × 4  =  3 456 000 series",
                "",
                "scrape interval I = 15 s   →   86 400/15  =  5 760 samples/day/series",
                "bytes per sample           =   2",
                "",
                "3 456 000 × 5 760 × 2  =  39 813 120 000 bytes",
                "                       =  39.81 GB per day",
                "                       ≈  14.5 TB per year",
            ]),
            ("p", "Nothing in that list is unreasonable on its own. Forty services is a "
                  "medium company, a hundred and twenty endpoints is one large service, "
                  "six status classes is fewer than HTTP defines, thirty instances is a "
                  "small fleet and four methods is restrained. The product of five "
                  "reasonable numbers is three and a half million series and forty "
                  "gigabytes a day, for one metric family."),
            ("h3", "The label that ends the discussion"),
            ("p", "Now add a sixth label. A `region` and `zone` pair at fifty "
                  "combinations multiplies everything by fifty: 172.8 million series "
                  "and about 2 TB a day, which is a large and survivable number. A "
                  "`customer` label at five hundred multiplies by five hundred. A "
                  "`user_id` label at ten thousand multiplies by ten thousand."),
            ("math", [
                "base                3 456 000 series        39.81 GB/day",
                "",
                "× region-zone (50)       172 800 000        1.99 TB/day",
                "× customer   (500)     1 728 000 000        19.91 TB/day",
                "× user_id (10 000)    34 560 000 000        398.13 TB/day",
                "× request_id (10⁶)     3.456 × 10¹²         39 813 TB/day",
            ]),
            ("p", "The last row is the mistake that gets made, and it is worth being "
                  "precise about why it is qualitatively different rather than merely "
                  "larger. A `request_id` is unbounded: its cardinality is not a "
                  "hundred thousand or a million, it is however many requests you serve, "
                  "growing without limit, and every one of those series is written "
                  "exactly once and then kept for the retention period. A metric with "
                  "an unbounded label is not an expensive metric; it is a log with the "
                  "worst possible storage engine."),
            ("example", ("A URL path as a label",
                         "`endpoint=\"/users/12345/orders\"` looks like one label with a "
                         "sensible name, and its cardinality is the number of users. The "
                         "same metric with `endpoint=\"/users/{id}/orders\"` has "
                         "cardinality one for that route. The difference between the two "
                         "is a templating step in the instrumentation, and it is the "
                         "difference between a hundred and twenty series and ten million.",
                         "The tell is that the cardinality of a label should be "
                         "predictable from the design of the system rather than from its "
                         "traffic. If you cannot state a label&rsquo;s cardinality "
                         "without querying production, it is probably unbounded.")),
            ("h3", "Where the pain actually arrives"),
            ("p", "The bytes on disk are the easy part; the index is not. Every series "
                  "needs an entry mapping its label set to its data, that index is "
                  "consulted on every query and is usually held in memory, and a query "
                  "that touches a million series has to merge a million streams before "
                  "it can sum them. A dashboard panel that was fast at three thousand "
                  "series is not slow at three million &mdash; it times out."),
            ("p", "This is also why histogram resolution and cardinality are the same "
                  "budget. Every bucket boundary is a label value, so the choice made "
                  "in &ldquo;Histograms and Bucket Error&rdquo; &mdash; a ratio of 2 "
                  "against a ratio of 5/4, at 3.1 times as many buckets &mdash; "
                  "multiplies this product by 3.1 as well. Precision in the tail and "
                  "the number of labels you can afford are drawn from one account."),
            ("h3", "What to do instead"),
            ("ul", [
                "Bucket the label. An `http_status` of `2xx, 3xx, 4xx, 5xx` has "
                "cardinality four; the exact code has cardinality sixty and answers a "
                "question you ask twice a year.",
                "Move the detail to a different system. High-cardinality identifiers "
                "belong in logs and traces, which are built to be searched by one key "
                "and not aggregated across all of them.",
                "Template anything derived from a path or a query. The route, not the "
                "URL.",
                "Bound what you cannot template. A label with an explicit allow-list "
                "and an `other` value has the cardinality of the list plus one, for "
                "ever, whatever production does.",
            ]),
            ("p", "And compute the product before shipping the label, not after. The "
                  "multiplication takes ten seconds and the alternative is discovering "
                  "the answer from an out-of-memory kill on the storage layer at a time "
                  "of somebody else&rsquo;s choosing."),
        ],
        "lab": ("measure", {
            "mode": "cardinality",
            "panel_title": "Set the labels",
            "panel_intro": (
                "The series count is the exact product of the cardinalities you set, "
                "and the storage is that product times the samples a day your scrape "
                "interval implies times the bytes a sample. Add the sixth label from "
                "the list and watch every figure move by that label&rsquo;s cardinality "
                "&mdash; the multiplication is the lesson, and it is the same "
                "multiplication whether the factor is 4 or 10 000."
            ),
        }),
        "steps_title": "Pricing a label before you add it",
        "steps_intro": (
            "Four multiplications and one question. The question is the one that "
            "prevents the outage."
        ),
        "steps": [
            ("Write down every label and its cardinality",
             "Including the ones the client library adds for you: `instance`, `job`, "
             "`pod`, and whatever your service mesh injects. A cardinality you did not "
             "choose still multiplies."),
            ("Multiply them",
             "That is the series count. Compare it to what your storage currently "
             "holds; a single metric family that is a large fraction of the whole "
             "system&rsquo;s series count is a finding on its own."),
            ("Turn it into bytes a day",
             "`series × (86 400/I) × bytes per sample`. Then multiply by the retention "
             "in days for the number that actually gets provisioned, and remember that "
             "the index is separate and is in memory."),
            ("Ask whether any label's cardinality is set by traffic rather than by design",
             "A label whose value comes from a user, a request, a session, a URL or an "
             "error message is unbounded regardless of what it looks like today. "
             "Unbounded is not a big number; it is a different kind of number, and no "
             "capacity plan covers it."),
        ],
        "worked": {
            "title": "Five ordinary labels, and the sixth one that ends it",
            "intro": [
                "One metric family, five labels nobody would query in review, and a "
                "fifteen-second scrape. The arithmetic is a product and three "
                "multiplications, and the only reason it surprises anyone is that the "
                "labels are added one at a time over eighteen months.",
            ],
            "lines": [
                "LABELS                cardinality",
                "  service                     40",
                "  endpoint                   120",
                "  status                       6",
                "  instance                    30",
                "  method                       4",
                "",
                "  series = 40 × 120 × 6 × 30 × 4",
                "         = 4 800 × 6 × 30 × 4",
                "         = 28 800 × 30 × 4",
                "         = 864 000 × 4",
                "         = 3 456 000 series",
                "",
                "STORAGE",
                "  samples per day per series = 86 400 / 15 = 5 760",
                "  bytes per sample           = 2",
                "",
                "  3 456 000 × 5 760 = 19 906 560 000 samples/day",
                "                × 2 = 39 813 120 000 bytes/day",
                "                    = 39.81 GB/day",
                "                    = 1 194 GB over a 30-day retention",
                "",
                "THE SIXTH LABEL",
                "  user_id, cardinality 10 000",
                "",
                "  series  3 456 000 × 10 000 = 34 560 000 000",
                "  bytes   39.81 GB × 10 000  = 398 131 GB/day = 398.13 TB/day",
                "",
                "  the label was one line of instrumentation",
            ],
            "after": [
                "Halving the scrape interval to 7.5 seconds doubles the last block and "
                "changes nothing about the first: the sample rate is a storage lever "
                "and the labels are a series lever, and only the series lever touches "
                "the index. When a metrics system is in trouble it is almost always the "
                "series count rather than the byte count, which is why the first "
                "question is always the product.",
                "Notice also what the sixth label does to the four-label decisions "
                "above it. Dropping `method` entirely divides everything by four and "
                "saves 30 GB a day; it also removes the ability to separate reads from "
                "writes. Adding `user_id` multiplies by ten thousand and answers a "
                "question that a trace store answers better. The two decisions are not "
                "in the same unit of importance and they are usually made with the same "
                "amount of thought.",
                "For faded practice, keep the five labels, set the scrape interval to "
                "30 seconds and add the `region × zone` label at 50. The supplied first "
                "move is that the series count is `3 456 000 × 50`. Compute the new "
                "daily bytes, then say which of the two changes &mdash; the halved "
                "sample rate or the fiftyfold label &mdash; your storage layer will "
                "notice first, and why.",
            ],
        },
        "quiz_title": "Products, bytes and unbounded labels",
        "quiz": [
            {"q": "A metric has labels with cardinalities 40, 120, 6, 30 and 4. How many time series is that?",
             "a": ["200, the sum of the cardinalities", "3 456 000, the product of the cardinalities",
                   "5, one per label", "It depends on the scrape interval"],
             "c": 1,
             "why": "Each distinct combination of label values is its own series, so the "
                    "count is `40 × 120 × 6 × 30 × 4 = 3 456 000`. The sum is the answer "
                    "to a question nobody asked; the scrape interval sets how many "
                    "<em>samples</em> each series produces, not how many series there are."},
            {"q": "Those 3 456 000 series are scraped every 15 seconds and each sample costs 2 bytes. What is the daily storage?",
             "a": ["About 6.9 MB", "About 39.81 GB", "About 398 GB", "About 14.5 TB"],
             "c": 1,
             "why": "`86 400/15 = 5 760` samples per series per day, so "
                    "`3 456 000 × 5 760 × 2 = 39 813 120 000` bytes, about 39.81 GB. "
                    "`14.5 TB` is the same figure over a year; `398 GB` is ten days of it, "
                    "and is also what one extra label of cardinality 10 would cost per day."},
            {"q": "Someone proposes adding a `user_id` label, with about 10 000 active users. What happens?",
             "a": ["10 000 more series are created", "The series count rises by about 0.3%",
                   "Every figure is multiplied by 10 000: 34.56 billion series and about 398 TB a day",
                   "Nothing, until a user actually appears in a request"],
             "c": 2,
             "why": "Labels multiply. The new count is `3 456 000 × 10 000`, and the "
                    "storage scales with it. The &ldquo;10 000 more series&rdquo; answer "
                    "is the additive intuition this lesson exists to break &mdash; it "
                    "would be right if `user_id` were a separate metric rather than a "
                    "label on this one."},
            {"q": "Which of these labels is genuinely dangerous rather than merely expensive?",
             "a": ["`status_code`, with 60 distinct values", "`instance`, with 30 values that change on each deploy",
                   "`request_id`, one distinct value per request", "`region`, with 50 values"],
             "c": 2,
             "why": "The first, second and fourth have cardinalities you can state from "
                    "the design, so they can be priced &mdash; and `instance` has churn, "
                    "which makes it worse than its 30 suggests. `request_id` has no bound "
                    "at all: it grows with traffic, each series receives exactly one "
                    "sample, and the result is a log stored in a database built for "
                    "aggregation."},
        ],
        "mistakes": [
            ("Treating a label as a field rather than as a multiplier",
             "&ldquo;It is one more label&rdquo; is an additive sentence about a "
             "multiplicative operation. The test is arithmetic, not judgement: write "
             "the product with the new factor in it and read the answer. A label of "
             "cardinality four costs four times everything you already have."),
            ("Pricing the bytes and forgetting the index",
             "Forty gigabytes a day is a disk problem and is easily solved. Three and a "
             "half million label sets held in memory and merged on every query is a "
             "different problem, it is the one that actually takes the system down, and "
             "it does not appear anywhere in the storage calculation. Count series "
             "first and bytes second."),
            ("Assuming a series stops costing when it stops being written",
             "A pod that was deleted, a deploy that changed every `instance` value, a "
             "customer who churned &mdash; each leaves its series in the index for the "
             "whole retention period. A system sized on the current product and then "
             "deployed forty times a week accumulates forty times the label sets and "
             "falls over on a Tuesday for no visible reason."),
        ],
        "standard": ("Finish when adding a label is a multiplication you do before the pull request, not after the incident.",
                     "You should be able to compute a series count as a product, turn "
                     "it into bytes a day from a scrape interval and a sample size, say "
                     "what one more label of a given cardinality does to both, and "
                     "identify a label whose cardinality is set by traffic rather than "
                     "by design."),
        "note": "Cardinality is the cost of measuring a production system continuously. "
                "The next page is about a measurement you take deliberately and stop: "
                "&ldquo;How Long to Run a Load Test&rdquo; computes how many requests a "
                "run needs before it has even met the request it is reporting on "
                "&mdash; a six-hundred-request run sees the top 0.1% only 45.14% of the "
                "time.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "how-long-to-run-a-load-test",
        "title": "How Long to Run a Load Test",
        "module": "Sizing samples and alerts",
        "one_line": "Compute the number of requests a run needs before a stated percentile has probably occurred in it at all.",
        "summary": (
            "A run of `n` requests meets the slowest `t` fraction at least once with "
            "probability `1 − (1 − t)ⁿ`. At the top 0.1% a six-hundred-request run "
            "manages 45.14% &mdash; worse than a coin toss &mdash; and ninety-five per "
            "cent confidence takes 2 995 requests. Even that only establishes that the "
            "tail was met once; measuring it takes an order of magnitude more again, "
            "and a percentile a run has fewer than one expected sample for is just the "
            "maximum wearing a label."
        ),
        "key": [
            "P(a run of n meets the top t) = 1 − (1−t)ⁿ",
            "t = 1/1000, n = 600   →  45.14%       a minute at 10/s loses the toss",
            "even chance at n = 693                the fan-out break-even again",
            "95% confidence needs n = 2 995        by exact scan, not a logarithm",
            "meeting the tail once is not measuring it: that needs ten times more",
        ],
        "key_label": "How many requests a percentile needs to exist",
        "concepts_intro": (
            "The same `1 − (1 − p)ᵏ` as the sampling page, asked about requests instead "
            "of about events, plus the distinction that matters more than the formula."
        ),
        "concepts": [
            ("A percentile the run never met is the run's maximum with a label on it",
             "Nearest rank returns the value at position `⌈q·n⌉`, and that position "
             "always exists whatever `n` is. At `n = 600` and `q = 99.99%` the rank is "
             "600 &mdash; the largest observed value &mdash; so the tool reports a "
             "p99.99 and the number is the maximum of six hundred requests. Nothing in "
             "the output says so, and the more extreme the percentile you ask for, the "
             "more confidently the tool answers with the same number."),
            ("The chance of meeting the tail is exponential in the run length",
             "Each request is in the slowest `t` fraction with probability `t` and they "
             "are independent, so a run misses it entirely with probability `(1 − t)ⁿ`. "
             "At `t = 1/1000`, six hundred requests give `0.999⁶⁰⁰ = 54.86%` of missing "
             "it. The break-even &mdash; the run length with an even chance &mdash; is "
             "`n = 693`, which is precisely the fan-out break-even of "
             "&ldquo;Tail Amplification under Fan-out&rdquo;, because it is the same "
             "equation with `n` moved from one side to the other."),
            ("Meeting it once and measuring it are different orders of magnitude",
             "A run with one sample in the top 0.1% can say that such a latency exists. "
             "It cannot say what the p99.9 <em>is</em>: that value is estimated by a "
             "single observation, and the next run will produce a different one. "
             "Putting ten samples above the percentile takes an expected `10/t = 10 000` "
             "requests, and a stable estimate takes more. The `n` on this page is a "
             "floor below which the number is meaningless, not the length that makes it "
             "good."),
        ],
        "read_title": "The run length a percentile requires, and the one that would measure it",
        "read_intro": (
            "Where the exponent comes from, why the answer is found by scanning rather "
            "than by a logarithm, and what confidence in a tail actually buys."
        ),
        "body": [
            ("def", ("Meeting a percentile in a run",
                     "Let a request be in the slowest `t` fraction of the distribution "
                     "with probability `t`, independently across requests. A run of `n` "
                     "requests <strong>meets</strong> that tail if at least one of them "
                     "falls in it, which happens with probability",
                     "`1 − (1 − t)ⁿ`.",
                     "For the p99.9, `t = 1/1000`; for the p99, `t = 1/100`; for the "
                     "p99.99, `t = 1/10000`. Independence is the assumption, and it "
                     "fails for a run that ramps, for a cache that is warming and for "
                     "anything periodic.")),
            ("math", [
                "t = 1/1000",
                "",
                "n = 600    P = 1 − (999/1000)⁶⁰⁰   = 45.14%",
                "n = 693    P = 1 − (999/1000)⁶⁹³   = 50.01%     first past even",
                "n = 2 995  P = 1 − (999/1000)²⁹⁹⁵  = 95.00%     first past 95%",
                "",
                "expected number of top-0.1% requests in 600:  600 × 1/1000 = 0.6",
            ]),
            ("p", "A six-hundred-request run is a minute at ten requests a second, "
                  "which is a completely ordinary thing to do, and it produces a report "
                  "with a p99.9 in it. More than half the time that number was computed "
                  "from a sample containing no request from the top 0.1% at all: rank "
                  "`⌈0.999 × 600⌉ = 600` returns the maximum, and the maximum of six "
                  "hundred draws from the body of the distribution is not the p99.9 of "
                  "anything."),
            ("h3", "Why the lab scans instead of taking a logarithm"),
            ("p", "Solving `(1 − t)ⁿ ≤ 1 − c` for `n` is one logarithm, and the answer "
                  "it gives here is `n ≥ 2 994.23`, so 2 995. The lab does not do that. "
                  "It computes `(999/1000)ⁿ` as an exact fraction and compares it to "
                  "`1/20` directly, increasing `n` until the comparison flips."),
            ("p", "The reason is that the exact answer is a rational number a double "
                  "cannot hold: `(999/1000)²⁹⁹⁵` has a numerator of about nine thousand "
                  "digits, and converting it to a floating-point number before "
                  "comparing gives infinity divided by infinity. A scan over exact "
                  "fractions has no such failure mode, and it also makes the boundary "
                  "checkable &mdash; the lab can show that `n = 2 994` does not clear "
                  "the bar and `n = 2 995` does, which a logarithm and a ceiling can "
                  "only assert."),
            ("example", ("Three reports of the same service",
                         "A one-minute run at 10 requests a second: 600 requests, "
                         "p99.9 reported, and a 45.14% chance the run ever met the "
                         "tail. A five-minute run: 3 000 requests, 95.03% &mdash; the "
                         "number is now probably about something real, estimated from "
                         "about three observations. A one-hour run: 36 000 requests, "
                         "certainty of meeting the tail and roughly thirty-six samples "
                         "above it, which is enough for the reported value to be stable "
                         "between runs.",
                         "The three reports look identical. They differ by the length "
                         "of the run, which is the one field nobody reads, and the "
                         "first of the three is where most load-testing conclusions "
                         "come from.")),
            ("h3", "From meeting a tail to measuring it"),
            ("p", "The expected number of requests above the `q`-th percentile in a run "
                  "of `n` is `n·t`. One expected sample is the threshold at which the "
                  "percentile stops being the maximum; it is nowhere near the threshold "
                  "at which it is stable. As a working rule, ask for ten samples in the "
                  "tail &mdash; `n = 10/t`, so 10 000 requests for a p99.9 and 100 000 "
                  "for a p99.99 &mdash; and treat anything less as a lower bound with a "
                  "wide error around it."),
            ("p", "This is also the honest answer to &ldquo;why did the p99.9 change "
                  "between runs?&rdquo; With `n·t` near one, it changed because it is "
                  "the maximum of a random sample and maxima are volatile. Nothing "
                  "regressed, nothing improved, and the difference between the two runs "
                  "is the same kind of noise the first page of this course put an error "
                  "bar on &mdash; except that a percentile deep in the tail has a far "
                  "wider one than a ratio near the middle."),
            ("h3", "The assumption the arithmetic rests on"),
            ("p", "`1 − (1 − t)ⁿ` assumes every request is an independent draw from one "
                  "fixed distribution. A run that ramps load over its first two minutes "
                  "is drawing from a different distribution every second; a run against "
                  "a cold cache is measuring the cache filling; a run short enough to "
                  "sit inside one garbage-collection cycle may draw zero or all of its "
                  "tail from that one pause. In each case the request count is right and "
                  "the independence is not, and the practical response is to discard the "
                  "ramp, warm the system first, and run for several periods of whatever "
                  "the system does periodically."),
        ],
        "lab": ("measure", {
            "mode": "loadtest",
            "panel_title": "Choose the percentile and the confidence",
            "panel_intro": (
                "`(1 − t)ⁿ` is carried as an exact fraction and compared to the target "
                "directly, so the required `n` is found by a scan that can show you the "
                "integer either side of the boundary. Move the target from the p99 to "
                "the p99.99 and watch the required run length move by a factor of a "
                "hundred while the confidence setting does not move at all."
            ),
        }),
        "steps_title": "Sizing a run before you trust its tail",
        "steps_intro": (
            "Two of these are arithmetic and two are about what you do with the answer."
        ),
        "steps": [
            ("Write down the percentile you intend to report and its tail fraction",
             "p99 is `t = 1/100`, p99.9 is `1/1000`, p99.99 is `1/10000`. If the report "
             "will quote several, size for the most extreme of them, because that is "
             "the one that will be quoted in the summary."),
            ("Compute 1 − (1 − t)ⁿ for the run you were going to do",
             "Under a half means the run is more likely than not to be reporting its "
             "own maximum. This is worth doing before the run rather than after, "
             "because afterwards there is a number on a slide and the argument becomes "
             "about the number."),
            ("Scan for the n your confidence requires, and then multiply it",
             "`n` for 95% confidence is the floor. For a value you intend to compare "
             "against another run, size for about ten samples in the tail: `n ≈ 10/t`, "
             "which is 10 000 requests for a p99.9."),
            ("Check the run was one distribution",
             "Discard the ramp, warm the caches, and make the run long enough to "
             "contain several of whatever cycle the system has &mdash; garbage "
             "collection, checkpoint flushes, a cron job. Independence is the "
             "assumption underneath every number above and it is the one a short run "
             "breaks."),
        ],
        "worked": {
            "title": "A 600-request run reporting a p99.9",
            "intro": [
                "Ten requests a second for a minute, which is what a quick check looks "
                "like. The question is not whether the service is fast; it is whether "
                "this run is in a position to say anything about the slowest one "
                "request in a thousand.",
            ],
            "lines": [
                "t = 1/1000        n = 600",
                "",
                "P(the run never met the tail)  = (999/1000)⁶⁰⁰ = 0.548647…",
                "P(it met the tail at least once) = 1 − that     = 0.451353…",
                "                                               = 45.14%",
                "",
                "expected requests in the top 0.1%   600 × 1/1000 = 0.6",
                "",
                "reported rank   ⌈0.999 × 600⌉ = 600   →  the maximum of the run",
                "",
                "HOW LONG WOULD BE ENOUGH",
                "",
                "  even chance      first n with (999/1000)ⁿ ≤ 1/2   →  n =   693",
                "  95% confidence   first n with (999/1000)ⁿ ≤ 1/20  →  n = 2 995",
                "     check         n = 2 994  →  0.050012…  above 1/20, short",
                "                   n = 2 995  →  0.049962…  first to clear",
                "",
                "  ten samples in the tail   n ≈ 10/t = 10 000 requests",
                "",
                "at 10 requests a second:   693 → 69 s    2 995 → 5 min    10 000 → 17 min",
            ],
            "after": [
                "The 693 is the same integer as the fan-out break-even in "
                "&ldquo;Tail Amplification under Fan-out&rdquo;, and it is not a "
                "coincidence: that page asks how many parallel calls it takes for one "
                "of them to exceed its p99.9, this one asks how many sequential "
                "requests it takes to see one, and both are `0.999ⁿ = 1/2`. The same "
                "arithmetic appears a third time on this course, in the false-alarm "
                "rate of a threshold alert over a month of windows.",
                "Notice the last line. The gap between a run that is meaningless and a "
                "run that is useful is about seventeen minutes, which is less than the "
                "time usually spent arguing about the result of the meaningless one.",
                "For faded practice, size a run that will report a p99.99 at 95% "
                "confidence. The supplied first move is `t = 1/10000`, so the required "
                "`n` will be about ten times the p99.9 answer. Predict it, find it in "
                "the lab by the scan, and then compute how long that run takes at a "
                "hundred requests a second &mdash; and whether ten samples in that tail "
                "is a run you would actually schedule.",
            ],
        },
        "quiz_title": "Run lengths and tails",
        "quiz": [
            {"q": "A 600-request run reports a p99.9. What is the probability that the run contained at least one request from the slowest 0.1%?",
             "a": ["99.9%", "60%", "45.14%", "0.6%"],
             "c": 2,
             "why": "`1 − (999/1000)⁶⁰⁰ = 0.4513`. The `0.6%` answer is the expected "
                    "<em>count</em> of such requests, `600 × 1/1000 = 0.6`, misread as a "
                    "probability. More than half the time the reported p99.9 is the "
                    "maximum of a sample containing nothing from the tail at all."},
            {"q": "How many requests does a run need before it meets the top 0.1% with 95% confidence?",
             "a": ["About 1 000", "About 2 995", "About 10 000", "About 100 000"],
             "c": 1,
             "why": "`(999/1000)ⁿ ≤ 1/20` first holds at `n = 2 995`. `10 000` is the "
                    "different and larger question of putting ten samples in the tail so "
                    "that the value is stable between runs; `1 000` gives only 63.2% "
                    "confidence, which is the level at which a run fails to see the tail "
                    "more than a third of the time."},
            {"q": "Two consecutive 3 000-request runs report p99.9 values of 210 ms and 340 ms. What is the most likely explanation?",
             "a": ["A regression between the two runs",
                   "Each run has about three samples in the tail, so the reported value is volatile by construction",
                   "The second run was measuring a different percentile",
                   "The first run was too short to meet the tail at all"],
             "c": 1,
             "why": "`3 000 × 1/1000 = 3` expected samples above the p99.9, so the "
                    "reported value is being estimated from about three observations and "
                    "will move substantially between runs. Both runs almost certainly met "
                    "the tail &mdash; 95% confidence needs 2 995 &mdash; which is exactly "
                    "the point: meeting it is not measuring it."},
            {"q": "A tool is asked for the p99.99 of a 600-request run. What does it return?",
             "a": ["An error, since the run is too short", "The maximum of the 600 requests",
                   "The 60th slowest request", "An interpolated value above the maximum"],
             "c": 1,
             "why": "Nearest rank is `⌈0.9999 × 600⌉ = 600`, the last position, so the "
                    "answer is the run&rsquo;s maximum &mdash; and it would also be the "
                    "answer for the p99.9 and for the p100. Nothing in the output "
                    "distinguishes them, which is why the run length has to be checked "
                    "against the percentile before the report is believed."},
        ],
        "mistakes": [
            ("Believing a one-minute run has shown you the p99.9",
             "Six hundred requests meet the top 0.1% less than half the time, so the "
             "reported figure is usually the run&rsquo;s maximum. The tell is that "
             "asking the same tool for the p99.9, the p99.99 and the maximum returns "
             "the same number; if it does, the run is too short for every percentile "
             "you asked about."),
            ("Confusing meeting a tail with measuring it",
             "Confidence of 95% that at least one tail request occurred is a statement "
             "about existence. The reported percentile is then estimated from one or "
             "two observations and will move by tens of per cent between runs. Size for "
             "about ten samples above the percentile if two runs are going to be "
             "compared."),
            ("Reading run-to-run variation in a deep percentile as a change in the system",
             "With one or two samples in the tail the reported value is essentially a "
             "maximum, and maxima are volatile even when nothing whatever has changed. "
             "Before opening an investigation, compute `n·t` for both runs: if it is "
             "near one, the difference is the sample and not the service."),
        ],
        "standard": ("Finish when the first question about a load-test report is its request count, not its p99.9.",
                     "You should be able to compute `1 − (1 − t)ⁿ` for a run you are "
                     "planning, find the `n` a stated confidence needs by an exact "
                     "comparison, say how many more requests a stable estimate takes, "
                     "and recognise a percentile that is the run&rsquo;s maximum "
                     "wearing a label."),
        "note": "Everything so far has been about measuring. The last two pages are "
                "about acting on a measurement, and both are arithmetic rather than "
                "judgement. &ldquo;Burn-rate Alerts&rdquo; computes what a window of "
                "elevated errors costs against a budget of 43.2 minutes, and names why "
                "another page of this library says 43.8 for the same objective.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "burn-rate-alerts",
        "title": "Burn-rate Alerts",
        "module": "Sizing samples and alerts",
        "one_line": "Compute the fraction of an error budget a window consumes at a given burn rate, and the time to exhaustion, and choose the pairs that page at the right moment.",
        "summary": (
            "An objective over a period implies a budget: 99.9% over 30 days is exactly "
            "216/5 = 43.2 minutes of failure. A burn rate `b` is a multiple of the rate "
            "that would spend the budget exactly at the end of the period, so a window "
            "`w` at burn `b` consumes `b·w/period` of it and exhausts the budget in "
            "`period/b`. Alerting on the budget rather than on the raw error rate is "
            "what makes a fast page and a slow page into two settings of one rule."
        ),
        "key": [
            "budget = (1 − objective) × period",
            "99.9% of 30 days = 0.001 × 43 200 min = 216/5 = 43.2 minutes exactly",
            "99.9% of a 2 628 000 s month = 43.8 minutes — a different month, also exact",
            "a window w at burn b spends b·w/period      14.4× for 1 h → 2%",
            "time to exhaustion = period ÷ b             14.4× → 50 hours",
            "an SLO is not an SLA: one arithmetic, two consequences",
        ],
        "key_label": "A budget, and the rate it is being spent at",
        "concepts_intro": (
            "The budget is a quantity of failure you are allowed, the burn rate is how "
            "fast you are spending it, and the pair `(b, w)` is an alert."
        ),
        "concepts": [
            ("An objective is a budget, and the period is part of the definition",
             "99.9% over 30 days permits `0.001 × 43 200 = 43.2` minutes of failure, "
             "and nothing about that figure is meaningful without the 30 days. The same "
             "objective over a 2 628 000-second month &mdash; a twelfth of a 365-day "
             "year, which is what &ldquo;Error Budgets&rdquo; on the Availability and "
             "Failure course uses &mdash; permits 43.8 minutes. Both are exact, neither "
             "is a rounding of the other, and a budget quoted without its period cannot "
             "be compared with anything."),
            ("The burn rate is a multiple, not a rate",
             "A burn rate of 1 is the error rate that would spend exactly the whole "
             "budget exactly at the end of the period. At a 99.9% objective that is "
             "0.1% of requests failing. A burn of 14.4 means 1.44% of requests failing, "
             "and a burn of 0 means none. Expressing it this way makes the arithmetic "
             "independent of the objective: `b = 14.4` spends 2% of the budget in an "
             "hour whether the objective is three nines or five."),
            ("A pair (b, w) is an alert, and one pair is never enough",
             "A short window at a high burn catches a severe outage within minutes and "
             "is blind to a slow leak; a long window at a low burn catches the leak and "
             "arrives hours after a severe outage has spent everything. The standard "
             "set is two or four pairs together: 14.4× over 1 hour, 6× over 6 hours, "
             "3× over 1 day, 1× over 3 days &mdash; spending 2%, 5%, 10% and 10% of the "
             "budget respectively by the time each fires."),
        ],
        "read_title": "The budget, the burn, the exhaustion time, and the pairs",
        "read_intro": (
            "Two conventions for the same objective and which period each assumes, the "
            "arithmetic of a window, and why multi-window alerting has the shape it has."
        ),
        "body": [
            ("def", ("Error budget and burn rate",
                     "For an objective `o` over a period `P`, the "
                     "<strong>error budget</strong> is `(1 − o)·P` &mdash; the quantity "
                     "of failure permitted. The <strong>burn rate</strong> `b` is the "
                     "current failure rate divided by `1 − o`, so `b = 1` spends the "
                     "budget exactly over `P`. A window of length `w` at burn `b` "
                     "consumes",
                     "`b·w/P` of the budget, and exhausts it after `P/b`.")),
            ("math", [
                "objective 99.9%,  period 30 days = 43 200 minutes",
                "",
                "budget  = (1 − 999/1000) × 43 200",
                "        = 43 200/1000  =  216/5  =  43.2 minutes      exactly",
                "",
                "the other convention, used by the availability course:",
                "  a month of 2 628 000 s = 43 800 minutes  (a twelfth of 365 days)",
                "  budget = 43 800/1000 = 43.8 minutes                 also exactly",
                "",
                "43.2 and 43.8 are the same objective over two different months",
            ]),
            ("p", "Say which period you mean, every time. The two figures differ by 1.4% "
                  "and they show up side by side in postmortems, where one of them gets "
                  "treated as an error in the other. They are not in conflict: a "
                  "calendar month has between 40 320 and 44 640 minutes, thirty days is "
                  "the convention this page uses because it is the one burn-rate "
                  "alerting is normally quoted against, and a twelfth of a year is the "
                  "convention that makes twelve months add to one year. Both are "
                  "defensible; neither is discoverable from the number alone."),
            ("p", "&ldquo;Error Budgets&rdquo; on the Availability and Failure course "
                  "also counts the budget in <em>failed requests</em> rather than in "
                  "minutes, which is a third useful framing and a fourth way for two "
                  "pages to appear to disagree. A budget is a quantity, a period and a "
                  "unit, and all three have to travel together."),
            ("thm", ("What a window costs and when the budget runs out",
                     "At a constant burn `b` over a window of length `w`, the failure "
                     "consumed is `b·(1 − o)·w`, and as a fraction of the budget "
                     "`(1 − o)·P` that is",
                     "`b·w/P`,  independent of the objective.",
                     "Setting the consumed fraction to 1 and solving for the elapsed "
                     "time gives exhaustion at `P/b`. So a burn of 14.4 sustained from "
                     "now spends the whole 30-day budget in `30/14.4` days, which is 50 "
                     "hours, and has spent 2% of it after the first hour.")),
            ("h3", "The standard pairs, and why there are several"),
            ("math", [
                "period 30 days,  budget 43.2 min at 99.9%",
                "",
                "  burn      window      b·w/P        of the budget     exhausts in",
                "  14.4×     1 hour      1/50         2%   = 0.864 min   50 hours",
                "   6×       6 hours     1/20         5%   = 2.16 min     5 days",
                "   3×       1 day       1/10         10%  = 4.32 min    10 days",
                "   1×       3 days      1/10         10%  = 4.32 min    30 days",
            ]),
            ("p", "Read the last column and the fourth column together. The fast pair "
                  "fires having spent 2% of the budget, which is why it can afford to "
                  "page a human at three in the morning: almost everything is still "
                  "there. The slow pair fires having spent 10%, over three days, at a "
                  "burn the fast pair never notices &mdash; a burn of 1 is exactly the "
                  "rate that spends the budget by the end of the period, so it is not an "
                  "emergency, and it is also not sustainable."),
            ("p", "A single pair cannot do both jobs. Choose only the fast one and a "
                  "service failing 0.15% of requests for a fortnight blows the budget "
                  "without ever tripping it; choose only the slow one and a total outage "
                  "pages you after it has already cost a third of the quarter&rsquo;s "
                  "allowance. The multi-window rule is not sophistication, it is the "
                  "minimum number of pairs that covers both failure shapes."),
            ("example", ("The same incident under two rules",
                         "A deploy at 02:00 takes the error rate to 1.44%, a burn of "
                         "14.4. Under a raw-rate alert at &ldquo;more than 1% errors for "
                         "five minutes&rdquo; it pages at 02:05 and would equally have "
                         "paged for a 1.1% blip lasting six minutes that costs 0.02% of "
                         "the budget.",
                         "Under the burn-rate rule it pages at 03:00, having spent "
                         "0.864 of the 43.2 minutes, and it does not page for the blip "
                         "at all. The difference is not the threshold; it is that one "
                         "rule is about the instantaneous rate and the other is about "
                         "the quantity of budget the rate is consuming.")),
            ("h3", "An SLO is not an SLA"),
            ("p", "The arithmetic above is identical for both. What differs is what "
                  "happens when the last row runs out. An <strong>objective</strong> is "
                  "an internal target: missing it spends a budget your own organisation "
                  "owns, and the usual consequence is a freeze on feature work until it "
                  "recovers. An <strong>agreement</strong> is a contract: missing it "
                  "spends money, because a refund or a credit is attached to it."),
            ("p", "Because the consequences differ by an order of magnitude, an "
                  "agreement is normally set looser than the objective it is measured "
                  "against &mdash; 99.5% promised against 99.9% targeted &mdash; so "
                  "that the internal alarm fires long before the external one does. A "
                  "team that sets both to the same number has arranged for the first "
                  "warning and the financial penalty to arrive on the same day."),
            ("p", "One more distinction worth keeping: the budget is measured in one "
                  "unit or the other, minutes or requests, and they are not "
                  "interchangeable. Forty-three minutes of total unavailability and "
                  "0.1% of requests failing all month are both &ldquo;the whole "
                  "budget&rdquo;, and they are very different experiences for a user. "
                  "Which unit the objective is written in decides which of them you "
                  "have agreed to."),
        ],
        "lab": ("measure", {
            "mode": "burn",
            "panel_title": "Set the objective and the burn",
            "panel_intro": (
                "The budget, the share a window spends and the time to exhaustion are "
                "exact fractions of a minute. The banner names which period convention "
                "the figures assume and what the other one would give, so that two "
                "pages of this library quoting 43.2 and 43.8 for the same objective can "
                "be reconciled rather than mistrusted. Slide the period to 30 days and "
                "the budget reads 216/5 exactly."
            ),
        }),
        "steps_title": "Turning an objective into an alert",
        "steps_intro": (
            "The first two steps are definitions, the third is the arithmetic, and the "
            "fourth is the one that gets skipped."
        ),
        "steps": [
            ("State the objective, the period and the unit",
             "99.9% of requests over 30 days is a different promise from 99.9% of "
             "minutes over a twelfth of a year, and both are called three nines. Write "
             "all three down before computing anything, and put them on the dashboard "
             "beside the number."),
            ("Compute the budget",
             "`(1 − o) × P` in whatever unit the objective is written in. For 99.9% "
             "over 30 days that is 43.2 minutes; keep it as `216/5` while you are doing "
             "arithmetic with it, because the fractions stay exact and the decimals "
             "invite rounding."),
            ("For each candidate pair, compute b·w/P and P/b",
             "The first says how much of the budget is gone when this pair fires; the "
             "second says how long you have if the burn continues. A pair that fires "
             "after 30% of the budget is gone is a pair that pages too late, whatever "
             "its burn rate looks like."),
            ("Take at least one fast pair and one slow pair",
             "Fast catches the outage, slow catches the leak, and neither substitutes "
             "for the other. The standard four are 14.4× over an hour, 6× over six "
             "hours, 3× over a day and 1× over three days; two of them is a reasonable "
             "minimum."),
            ("Decide what the page means before it arrives",
             "A burn-rate page says a quantity of budget is being consumed at a rate, "
             "not that anything is broken. The response to the fast pair is to stop the "
             "bleeding; the response to the slow pair is usually to plan work, and "
             "waking someone for it is how a good alert becomes an ignored one."),
        ],
        "worked": {
            "title": "43.2 minutes, a burn of 14.4, and the hour it takes to spend 2% of it",
            "intro": [
                "A 99.9% objective over 30 days, and a deploy that takes the failure "
                "rate to 1.44%. Every figure is an exact fraction of a minute; the only "
                "decisions in the calculation are the period and the unit.",
            ],
            "lines": [
                "THE BUDGET",
                "",
                "  objective  o = 999/1000        period  P = 30 days = 43 200 min",
                "",
                "  budget = (1 − o)·P = (1/1000)(43 200) = 216/5 = 43.2 minutes",
                "",
                "  the other convention:  P = 2 628 000 s = 43 800 min",
                "                         budget = 43.8 minutes",
                "  same objective, different month, both exact",
                "",
                "THE BURN",
                "",
                "  b = 14.4  means failing at 14.4 × (1 − o) = 14.4/1000 = 1.44%",
                "",
                "  one hour at that burn:",
                "    fraction  b·w/P = 14.4 × 60 / 43 200 = 864/43 200 = 1/50 = 2%",
                "    minutes   2% of 43.2                 = 0.864 minutes",
                "",
                "  time to exhaustion  P/b = 43 200/14.4 = 3 000 min = 50 hours",
                "",
                "THE FOUR PAIRS",
                "",
                "    burn   window    b·w/P    budget spent    exhausts",
                "   14.4×   1 hour     1/50     0.864 min      50 hours",
                "    6×     6 hours    1/20     2.16  min       5 days",
                "    3×     1 day      1/10     4.32  min      10 days",
                "    1×     3 days     1/10     4.32  min      30 days",
            ],
            "after": [
                "The fourth column is why these particular pairs are the standard ones. "
                "Every row fires having spent a single-figure percentage of the budget, "
                "so every row leaves room to respond; and the rows span burn rates from "
                "14.4 down to 1, so between them they catch a total outage and a leak "
                "small enough that nobody would call it an incident.",
                "The bottom row deserves a second look. A burn of exactly 1 is the rate "
                "at which the budget is spent precisely on schedule &mdash; not an "
                "emergency by any instantaneous measure, and exactly the rate that "
                "leaves you with nothing at the end of the period. It is the case a raw "
                "error-rate threshold can never be tuned to catch, because at a 99.9% "
                "objective the raw rate is 0.1% and no threshold distinguishes that from "
                "healthy noise in a five-minute window.",
                "For faded practice, take a 99.95% objective over 30 days. The supplied "
                "first move is that the budget halves to 21.6 minutes. Compute what the "
                "14.4× pair over one hour now spends as a fraction and in minutes, and "
                "say whether the fraction changed &mdash; then explain in one sentence "
                "why, which is the whole reason burn is expressed as a multiple.",
            ],
        },
        "quiz_title": "Budgets, burns and pairs",
        "quiz": [
            {"q": "What is the error budget for a 99.9% objective over a 30-day period?",
             "a": ["43.2 minutes", "43.8 minutes", "4.32 minutes", "It depends on the traffic volume"],
             "c": 0,
             "why": "`0.001 × 43 200 minutes = 216/5 = 43.2` minutes exactly. `43.8` is "
                    "the same objective over a 2 628 000-second month &mdash; a twelfth "
                    "of a 365-day year &mdash; which is the convention the availability "
                    "course uses; both are right and the period is what tells them apart. "
                    "Traffic volume matters only if the budget is counted in requests "
                    "instead of minutes."},
            {"q": "A service is burning at 14.4× against a 99.9% objective over 30 days. How much of the budget does one hour consume, and when does it run out?",
             "a": ["2% of the budget; 50 hours", "14.4% of the budget; about 2 days",
                   "1.44% of the budget; 30 days", "2% of the budget; 30 days"],
             "c": 0,
             "why": "`b·w/P = 14.4 × 60/43 200 = 1/50`, which is 2% or 0.864 of the 43.2 "
                    "minutes; exhaustion is at `P/b = 43 200/14.4 = 3 000` minutes, 50 "
                    "hours. `1.44%` is the failure rate, not the fraction of budget an "
                    "hour spends &mdash; two different quantities that both look like "
                    "percentages."},
            {"q": "A team alerts only on the 14.4× over 1 hour pair. What failure mode does that miss?",
             "a": ["A total outage, which is too fast for an hourly window",
                   "A sustained low burn &mdash; say 1.5× &mdash; which never trips the fast pair and spends the whole budget in under three weeks",
                   "Nothing; a high burn rate covers every case",
                   "A burn rate above 14.4, which saturates the window"],
             "c": 1,
             "why": "The fast pair is defined by a high burn, so a burn of 1.5× never "
                    "reaches it while exhausting the budget in `30/1.5 = 20` days. That is "
                    "exactly the leak the slow pairs exist for. A total outage is a very "
                    "high burn and trips the fast pair almost immediately."},
            {"q": "What is the difference between an objective and an agreement, given that the arithmetic is identical?",
             "a": ["An agreement is measured over a longer period",
                   "An objective is internal and its budget is owned by your organisation; an agreement is contractual and missing it costs money, so it is normally set looser than the objective",
                   "An agreement uses minutes and an objective uses requests",
                   "An objective is a target and an agreement is a measurement"],
             "c": 1,
             "why": "Same budget arithmetic, different consequence for the last row. "
                    "Because the external consequence is financial, the agreement is set "
                    "below the internal target &mdash; 99.5% promised against 99.9% "
                    "aimed at &mdash; so the internal alarm fires well before any refund "
                    "is owed. Periods and units are chosen separately for each and are "
                    "not what distinguishes them."},
        ],
        "mistakes": [
            ("Alerting on the raw error rate rather than on the budget",
             "A threshold on the instantaneous rate fires for a two-minute blip that "
             "costs 0.05% of the budget and stays quiet through a fortnight at 0.15% "
             "that spends all of it. The budget framing makes severity and duration one "
             "quantity &mdash; `b·w/P` &mdash; which is the whole reason for the change "
             "of variable."),
            ("Quoting a budget without the period it is a budget for",
             "43.2 and 43.8 minutes are the same objective over 30 days and over a "
             "twelfth of a year, and a budget counted in failed requests is a third "
             "quantity again. Two teams comparing numbers without their periods will "
             "eventually conclude that one of the two systems is broken, and neither "
             "will be."),
            ("Running one burn-rate pair",
             "A single fast pair is blind to the slow leak that is spending the budget "
             "on schedule; a single slow pair arrives after a severe outage has already "
             "taken a third of the allowance. The pairs are not alternatives to be "
             "chosen between &mdash; they cover different shapes of failure, and the "
             "minimum useful configuration has one of each."),
        ],
        "standard": ("Finish when a budget is quoted with its period and its unit, and an alert is a (b, w) pair rather than a threshold.",
                     "You should be able to compute `(1 − o)·P` exactly, convert a "
                     "failure rate into a burn multiple, compute `b·w/P` and `P/b` for "
                     "any pair, say which of two budget figures assumes which period, "
                     "and explain why an agreement is set looser than the objective "
                     "behind it."),
        "note": "A burn-rate rule fires on a quantity that is genuinely being spent. A "
                "plain threshold on a noisy ratio fires on the sample, and it fires "
                "whether or not anything has changed: &ldquo;Threshold Alerts and False "
                "Alarms&rdquo; computes that a 2% threshold on 200-request windows at a "
                "true 1% error rate trips 5.175% of the time, which is 104.32 pages a "
                "week from a perfectly healthy service.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "threshold-alerts-and-false-alarms",
        "title": "Threshold Alerts and False Alarms",
        "module": "Sizing samples and alerts",
        "one_line": "Compute the exact probability that a fixed threshold fires on a healthy service, and the pages a week that produces.",
        "summary": (
            "A threshold on a measured ratio is a statement about a sample. With 200 "
            "requests a window at a true error rate of 1%, a 2% threshold fires at five "
            "errors, and the exact binomial tail says that happens in 5.175% of "
            "windows &mdash; 104.32 pages a week, all of them false, from a service in "
            "which nothing at all has changed. Widening the window to 600 requests at "
            "the same threshold takes it to 5.71."
        ),
        "key": [
            "errors in a window ~ Binomial(n, p)     n = 200, p = 1% → mean 2",
            "threshold 2% of 200 = 4, so it fires at 5 or more",
            "P(X ≥ 5) = 5.1746…% ≈ 5.175%           exact binomial tail",
            "windows a week = 7×24×60 ÷ 5 = 2 016   → 104.32 false pages a week",
            "P(at least one in the next hour) = 1 − (1−0.05175)¹² = 47.14%",
            "same threshold on 600-request windows: fires at 13, 5.71 pages a week",
        ],
        "key_label": "What a threshold fires at when nothing is wrong",
        "concepts_intro": (
            "The threshold is compared against a measurement, the measurement is a "
            "sample, and samples fluctuate. Everything else follows."
        ),
        "concepts": [
            ("A threshold is a statement about the sample, not about the system",
             "&ldquo;More than 2% errors&rdquo; is evaluated against the ratio observed "
             "in one window, and that ratio is a random quantity even when the "
             "underlying rate is constant. With 200 requests at a true 1%, the observed "
             "count is `Binomial(200, 0.01)` with a mean of 2, and it exceeds 4 in one "
             "window in twenty. The alert is firing correctly; it is answering a "
             "question about arithmetic."),
            ("Small per-window probabilities multiply into large weekly counts",
             "5.175% sounds like a tolerable rate until it is multiplied by the number "
             "of windows. Five-minute windows give `7 × 24 × 60 ÷ 5 = 2 016` of them a "
             "week, so the expected false pages are `0.05175 × 2 016 = 104.32`. Fifteen "
             "a day. The per-window figure and the weekly figure are the same fact and "
             "only one of them is ever quoted."),
            ("The fix is more requests per window, not a higher threshold",
             "Both work arithmetically and they differ in what they cost. Widening the "
             "window to 600 requests keeps the 2% threshold and drops the false rate to "
             "0.849%, or 5.71 pages a week, because the ratio of a larger sample varies "
             "less &mdash; the `1/√n` of the first page of this course, arriving as an "
             "alerting decision. Raising the threshold to 4% on the same 200 requests "
             "gives 0.021% and 0.43 pages a week, and buys it by refusing to detect a "
             "genuine doubling of the error rate."),
        ],
        "read_title": "The binomial tail, the pages it produces, and what to change",
        "read_intro": (
            "Where the firing count comes from, how a per-window probability becomes a "
            "weekly number, and the two levers with their prices."
        ),
        "body": [
            ("def", ("Threshold alert, and its false-alarm rate",
                     "A <strong>threshold alert</strong> fires when a statistic "
                     "measured over a window crosses a fixed value. For an error ratio "
                     "with threshold `τ` over `n` requests, it fires at the smallest "
                     "integer error count strictly above `τ·n`. Its "
                     "<strong>false-alarm probability</strong> is the chance of "
                     "reaching that count when the true rate is the healthy one, and it "
                     "is the upper tail of a binomial distribution.")),
            ("math", [
                "true rate p = 1/100,  window n = 200 requests,  threshold τ = 2%",
                "",
                "τ·n = 0.02 × 200 = 4,  so the alert fires at k = 5 or more",
                "",
                "X ~ Binomial(200, 1/100)        E[X] = 2 errors a window",
                "",
                "P(X ≥ 5) = Σ_{j=5}^{200} C(200, j) (1/100)ʲ (99/100)²⁰⁰⁻ʲ",
                "         = 0.051746263…",
                "         = 5.1746…%  ≈ 5.175%",
            ]),
            ("p", "Nothing has changed about the service. The true rate is 1%, the "
                  "threshold is twice that, and one window in twenty crosses it anyway "
                  "because five errors out of two hundred is an ordinary thing for a "
                  "process with a mean of two to produce. This is not a tuning problem "
                  "with a better threshold hiding behind it; it is what a threshold on "
                  "a small sample does."),
            ("h3", "From a per-window probability to a pager"),
            ("math", [
                "window length 5 minutes",
                "",
                "windows in a week   7 × 24 × 60 ÷ 5   = 2 016",
                "expected false pages 0.051746… × 2 016 = 104.32 a week",
                "                                        ≈ 14.9 a day",
                "",
                "windows in an hour  60 ÷ 5 = 12",
                "P(at least one page in the next hour)",
                "     = 1 − (1 − 0.051746…)¹²  = 47.14%",
            ]),
            ("p", "The second block is `1 − (1 − p)ᵏ` for the third time on this course "
                  "&mdash; the capture probability of a sampling rate, the chance a load "
                  "test meets its tail, and now the chance of at least one false page "
                  "in the next hour. Three lessons, one function, and the lab calls the "
                  "same one in all three places so the claim can be checked rather than "
                  "taken on trust."),
            ("p", "A 47% chance of being paged in any given hour by a service in which "
                  "nothing is wrong is the number that matters operationally. It is not "
                  "merely wasteful: after a week of it the page has no information "
                  "content left, and the response to the hundred and fifth one is "
                  "indistinguishable from the response to a real outage, because there "
                  "is nothing to distinguish it by."),
            ("h3", "The two levers, and what each costs"),
            ("example", ("The same alert, three configurations",
                         "<strong>200 requests, 2%.</strong> Fires at 5 errors, 5.175% "
                         "of windows, 104.32 pages a week. This is the configuration "
                         "almost everyone starts with.",
                         "<strong>600 requests, 2%.</strong> A fifteen-minute window "
                         "instead of five, so the threshold now means 13 errors. "
                         "0.849% of windows and 672 windows a week: 5.71 pages. The "
                         "threshold did not move; the sample got bigger and its ratio "
                         "got less variable.",
                         "<strong>200 requests, 4%.</strong> Fires at 9 errors, 0.021% "
                         "of windows, 0.43 pages a week. Quieter still &mdash; and it "
                         "no longer fires on a true rate of 2%, which is double the "
                         "healthy rate and is exactly the kind of change the alert "
                         "existed to catch.")),
            ("p", "The two levers are not equivalent. Widening the window buys quiet "
                  "with detection <em>latency</em>: the same regression is caught, ten "
                  "minutes later. Raising the threshold buys quiet with detection "
                  "<em>sensitivity</em>: some regressions are now never caught at all, "
                  "at any latency. Latency is usually the cheaper currency, which is "
                  "why the first move on a noisy alert should be the window."),
            ("p", "There is a floor. A low-traffic service has few requests per window "
                  "however long the window is, and at twenty requests a window no "
                  "threshold on a ratio is stable: one error is 5% and two is 10%. For "
                  "those services the honest answer is to alert on something else "
                  "&mdash; an absolute count of errors, a budget consumed over a long "
                  "window, or a synthetic probe &mdash; rather than to choose a "
                  "threshold and live with the noise."),
            ("h3", "What this calculation is and is not"),
            ("p", "It is a false-alarm rate for a stated rule on a stated healthy rate. "
                  "It is not a detector design: it says nothing about how quickly a real "
                  "change is caught, and it does not compare this rule against any "
                  "other. Those questions need the distribution under the alternative "
                  "as well, which is the beginning of hypothesis testing and is outside "
                  "this course."),
            ("p", "What it does give you is the arithmetic to reject a rule before "
                  "shipping it. If a proposed alert would fire a hundred times a week "
                  "on a healthy service, that fact is available from four numbers "
                  "&mdash; the true rate, the requests per window, the threshold and "
                  "the window length &mdash; and it is available before anybody is "
                  "woken up. The previous page&rsquo;s burn-rate rule is the "
                  "better-behaved alternative for exactly this reason: it thresholds a "
                  "quantity that accumulates rather than a ratio that fluctuates."),
        ],
        "lab": ("measure", {
            "mode": "threshold",
            "panel_title": "Set the rate, the window and the threshold",
            "panel_intro": (
                "The firing probability is the exact binomial upper tail, computed two "
                "ways &mdash; directly, and as a suffix sum of the whole distribution "
                "&mdash; so the page can show the two agree. Raise the requests per "
                "window without touching the threshold and watch the pages a week "
                "collapse; then raise the threshold instead, and notice what the alert "
                "has stopped being able to see."
            ),
        }),
        "steps_title": "Checking an alert before it checks you",
        "steps_intro": (
            "Four numbers in, two numbers out, and the second one is the one to put in "
            "the review."
        ),
        "steps": [
            ("Write down the healthy rate and the requests per window",
             "Not the threshold &mdash; the rate the service actually runs at, and how "
             "many requests fall in one evaluation window at its typical traffic. If "
             "traffic varies by time of day, do this twice: the quiet hours are where "
             "the false alarms live."),
            ("Find the count the threshold fires at",
             "The smallest integer strictly above `τ·n`. At `τ = 2%` and `n = 200` that "
             "is 5, not 4 &mdash; the off-by-one matters, because the tail at 4 is "
             "several times the tail at 5."),
            ("Compute the exact binomial upper tail at that count",
             "`P(X ≥ k)` for `X ~ Binomial(n, p)`. This is the probability of a page "
             "per window when nothing is wrong, and it is the number people expect to "
             "be small and are surprised by."),
            ("Multiply by the windows, and read the weekly figure out loud",
             "`7 × 24 × 60 ÷ w` windows a week. A hundred pages a week is not a tuning "
             "detail; it is a rule that should not ship. Then try the window lever "
             "first and the threshold lever second, and say what each one gave up."),
        ],
        "worked": {
            "title": "A 2% threshold on a 1% service, and 104 pages a week",
            "intro": [
                "The service is healthy throughout: a true error rate of 1%, unchanging. "
                "The alert is an ordinary one, and every figure below is an exact "
                "binomial calculation on the numbers a team would actually have chosen.",
            ],
            "lines": [
                "true rate   p = 1/100        window n = 200 requests over 5 minutes",
                "threshold   τ = 2%",
                "",
                "FIRING COUNT",
                "  τ·n = 4 exactly, so the alert needs strictly more:  k = 5",
                "  E[X] = n·p = 2 errors per window",
                "",
                "THE TAIL",
                "  P(X ≥ 5) = 1 − P(X ≤ 4)",
                "           = 0.05174626363…",
                "           = 5.175%          about one window in nineteen",
                "",
                "  for comparison:  P(X ≥ 4) = 14.20%    P(X ≥ 6) = 1.60%",
                "  the off-by-one at the threshold is a factor of about three",
                "",
                "PAGES",
                "  windows a week   7 × 24 × 60 / 5 = 2 016",
                "  false pages      0.0517462… × 2 016 = 104.32 a week",
                "                                      ≈ 14.9 a day",
                "",
                "  windows an hour  12",
                "  P(≥ 1 page in the next hour) = 1 − (1 − 0.0517462…)¹² = 47.14%",
                "",
                "TWO FIXES",
                "  n = 600, τ = 2%   fires at 13   P = 0.849%   672 windows  → 5.71/week",
                "  n = 200, τ = 4%   fires at  9   P = 0.021%  2 016 windows → 0.43/week",
            ],
            "after": [
                "The comparison line in the middle is worth keeping. Moving the firing "
                "count by one, from 5 to 4, changes the false-alarm rate by a factor of "
                "nearly three; from 5 to 6, by a factor of three the other way. A "
                "threshold on a small count is extremely sensitive to exactly where the "
                "boundary falls, which is another way of saying that a round-numbered "
                "threshold like 2% has no particular claim to being right.",
                "The two fixes are not interchangeable even though both make the pager "
                "quiet. The wider window still detects a doubling of the error rate, "
                "ten minutes later than before. The higher threshold does not detect a "
                "doubling at all: at a true rate of 2% the mean is 4 errors in 200 and "
                "the alert wants 9. Quiet is easy; quiet while still detecting the thing "
                "you built the alert for is the actual problem.",
                "For faded practice, take a service with a true rate of 0.5% and "
                "100-request windows of one minute, with a 2% threshold. The supplied "
                "first move is that the mean is 0.5 errors and the alert fires at 3. "
                "Compute the tail, the windows a week and the pages, then say which "
                "lever you would pull &mdash; and whether a ratio threshold is the "
                "right instrument for a service this small at all.",
            ],
        },
        "quiz_title": "Thresholds, tails and pagers",
        "quiz": [
            {"q": "A window holds 200 requests and the alert fires when the error ratio exceeds 2%. At how many errors does it fire?",
             "a": ["At 4, since 2% of 200 is 4", "At 5, the smallest count strictly above 4",
                   "At 2, the expected count", "At 20, since 2% is 1 in 50"],
             "c": 1,
             "why": "&ldquo;More than 2%&rdquo; means strictly above `0.02 × 200 = 4`, so "
                    "the firing count is 5. The distinction is not pedantic: the tail at "
                    "4 errors is 14.2% and at 5 it is 5.175%, a factor of nearly three, "
                    "so the convention changes the pager load by more than most threshold "
                    "tuning does."},
            {"q": "With a true error rate of 1%, that alert fires in 5.175% of windows. Over five-minute windows, how many false pages a week is that?",
             "a": ["About 5", "About 36", "About 104", "About 2 016"],
             "c": 2,
             "why": "`7 × 24 × 60 ÷ 5 = 2 016` windows a week, and `0.05175 × 2 016 = "
                    "104.32`. About fifteen a day, every day, from a service in which "
                    "nothing has changed. `2 016` is the window count itself, and it is "
                    "the multiplier people leave out when they judge 5% to be acceptable."},
            {"q": "Which change keeps the alert able to detect a doubling of the error rate while reducing the false pages?",
             "a": ["Raising the threshold from 2% to 4% on the same 200-request window",
                   "Widening the window to 600 requests at the same 2% threshold",
                   "Lowering the threshold to 1.5% to catch problems earlier",
                   "Requiring two consecutive windows above 4%"],
             "c": 1,
             "why": "The wider window drops the false rate to 0.849% &mdash; 5.71 pages a "
                    "week &mdash; and still fires on a true 2% rate, at the cost of ten "
                    "minutes of detection latency. Raising the threshold to 4% is quieter "
                    "still and can no longer see a doubling at all: it wants 9 errors "
                    "where a 2% rate produces a mean of 4."},
            {"q": "The alert fires 5.175% of windows, with twelve windows an hour. What is the chance of at least one page in the next hour on a healthy service?",
             "a": ["5.175%", "About 62%, since 12 × 5.175% = 62%", "47.14%", "It cannot be computed without the incident rate"],
             "c": 2,
             "why": "`1 − (1 − 0.05175)¹² = 47.14%` &mdash; the same "
                    "`1 − (1 − p)ᵏ` the sampling and load-test pages use. Multiplying the "
                    "per-window probability by twelve gives 62%, which overcounts because "
                    "it double-counts the hours with more than one page; it is a usable "
                    "approximation only while the product is small, and 0.62 is not."},
        ],
        "mistakes": [
            ("Treating a threshold crossing as a fact about the system",
             "It is a fact about one sample of a random quantity. Before investigating "
             "a single crossing, compute what fraction of windows cross by chance at "
             "the healthy rate; if the answer is five per cent, a crossing is evidence "
             "of almost nothing and the correct response to a single page is to look at "
             "the next window rather than at the service."),
            ("Judging an alert by its per-window probability",
             "5% per window reads as rare and is a hundred and four pages a week. The "
             "number to put in a design review is always the weekly count, because that "
             "is the number a human experiences, and the conversion factor &mdash; 2 016 "
             "windows for five-minute evaluation &mdash; is larger than anybody&rsquo;s "
             "intuition allows for."),
            ("Reaching for the threshold when the window is the problem",
             "Raising the threshold is the quickest way to silence a noisy alert and "
             "the one that silently removes its reason for existing. Widening the "
             "window reduces the variance of the ratio instead, costs detection latency "
             "rather than detection sensitivity, and leaves the alert firing on the "
             "regressions it was built for."),
        ],
        "standard": ("Finish when a proposed alert is priced in pages a week on a healthy service before it ships.",
                     "You should be able to find the count a threshold fires at, "
                     "compute the exact binomial upper tail at it, convert that into "
                     "pages a week and into the chance of a page in the next hour, and "
                     "say which of the window and the threshold you would change and "
                     "what each one gives up."),
        "note": "That is the whole course: a ratio with an error bar, two aggregates "
                "that lie in different ways, two biases a measurement introduces, and "
                "four sizing calculations for a sample, a metric, a test and an alert. "
                "Every one of them is the same discipline &mdash; write down what the "
                "number is a measurement of, and then compute how far it can be from "
                "the thing you wanted to know.",
    },
]
