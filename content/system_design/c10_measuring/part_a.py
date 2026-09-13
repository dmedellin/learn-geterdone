"""Measuring Systems, lessons 01-05 - the error bar, the two aggregates, the two biases."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "slis-as-ratios",
        "title": "SLIs as Ratios",
        "module": "What a number means",
        "one_line": "Compute the standard error of a measured ratio, and the window size it takes to resolve a tenth of a per cent.",
        "summary": (
            "An indicator of service quality is a ratio: good events over valid "
            "events, counted across a window. It is measured, not observed, so it "
            "arrives with an error bar whose width is `√(p(1 − p)/n)` and depends on "
            "the size of the window rather than on the health of the service. A "
            "thousand requests cannot tell 99.9% from 99.8%, and most arguments about "
            "whether an objective was met are arguments about a number whose error bar "
            "contains both positions."
        ),
        "key": [
            "SLI = good events ÷ valid events, over a stated window",
            "SE = √(p(1−p)/n)          n = 1 000, p = 0.9995 → SE ≈ 0.0707%",
            "gap to a 99.9% objective   0.05% = 0.71 SE      inside the noise",
            "n ≥ p(1−p)/w²              w = 0.025% → 7 996 requests",
            "precision goes as 1/√n     4× the requests buys 2× the precision",
        ],
        "key_label": "A ratio, and the error bar that arrives with it",
        "concepts_intro": (
            "One formula, and the two things it is usually misread about: what is in "
            "the denominator, and what a difference smaller than the error bar is "
            "evidence of."
        ),
        "concepts": [
            ("An SLI is a ratio, and its denominator is a decision",
             "Good events over valid events. Both halves are choices you make before "
             "you measure anything: a request that a client abandoned, a health check, "
             "a request rejected for a malformed body &mdash; each is either valid or "
             "not, and moving one of them across the line moves the ratio without "
             "anything happening to the service. Two teams quoting different "
             "availabilities for the same week are usually quoting different "
             "denominators, and no amount of precision resolves that."),
            ("The ± is a property of the count, not of the service",
             "Each valid event either succeeds or does not, so the count of good ones "
             "behaves like `n` independent trials at probability `p`, and the measured "
             "ratio has variance `p(1 − p)/n`. Its standard error is the square root, "
             "`√(p(1 − p)/n)`. Nothing about the system appears in that expression "
             "except `p` itself: a healthy service measured over a short window "
             "produces a noisy number, and the noise is arithmetic rather than a "
             "symptom."),
            ("Precision costs the square",
             "The error bar shrinks as `1/√n`, so halving it costs four times the "
             "traffic and the rest of the day buys less than the morning did. At "
             "`p = 0.999` one thousand requests give a standard error of about "
             "`0.1%` &mdash; the entire distance between 99.9% and 99.8%, which is why "
             "a thousand requests cannot tell those two apart. Resolving a tenth of a "
             "per cent takes about four thousand, and resolving a hundredth takes a "
             "hundred times as many again."),
        ],
        "read_title": "The ratio, its standard error, and the window that resolves a tenth of a per cent",
        "read_intro": (
            "Where `√(p(1 − p)/n)` comes from, what a gap of 0.71 standard errors is "
            "evidence of, and the request count a stated precision requires."
        ),
        "body": [
            ("def", ("Service level indicator",
                     "A <strong>service level indicator</strong> is a ratio "
                     "`good ÷ valid` of events counted over a stated "
                     "<strong>window</strong>. The <strong>objective</strong> is a "
                     "target the indicator is compared against. An indicator is not "
                     "complete without its window and its denominator: "
                     "&ldquo;99.95%&rdquo; names neither, and the same events can "
                     "produce several different correct values of it.")),
            ("p", "Everything on this course is a ratio of this shape or a percentile "
                  "of a sample, and both are measurements. The first thing to do with "
                  "a measurement is to say how wide it is, because a ratio quoted to "
                  "four figures from a five-minute window is three of those figures "
                  "wider than it looks."),
            ("thm", ("The standard error of a measured ratio",
                     "Let each of `n` valid events be good with probability `p`, "
                     "independently. The number of good events has variance "
                     "`n·p(1 − p)`, so the measured ratio `good/n` has variance",
                     "`p(1 − p)/n`,  and standard error  `SE = √(p(1 − p)/n)`.",
                     "The variance of a Bernoulli trial, and the rule that the "
                     "variance of a mean of `n` independent copies is the variance "
                     "divided by `n`, are proved in &ldquo;Variance and Standard "
                     "Deviation&rdquo; on the Discrete Mathematics path. This page "
                     "uses the result; that page establishes it.")),
            ("p", "Independence is the assumption and it is the one that fails. "
                  "Requests that fail because one dependency is down are not "
                  "independent trials, and during an incident the true error bar is "
                  "wider than this one &mdash; the formula is a floor on the "
                  "uncertainty, not a description of it. What it is exactly right "
                  "about is the quiet week, which is when the arguments happen."),
            ("math", [
                "a window of n = 1 000 requests reporting 99.95%",
                "",
                "p = 9995/10000 = 1999/2000        1 − p = 1/2000",
                "",
                "p(1 − p)     = 1999/4000000",
                "p(1 − p)/n   = 1999/4000000000            exact",
                "",
                "SE = √(1999/4000000000) = 0.000706929…",
                "                        ≈ 0.0707%          rounded, and it is a root",
            ]),
            ("p", "The variance is an exact fraction and the standard error is not, "
                  "because a square root of a rational is almost never rational. The "
                  "lab prints the fraction under the root exactly and labels the root "
                  "itself as rounded. That is the only rounded figure on this course "
                  "and its lesson says so."),
            ("p", "Now compare the measurement to the objective. The gap is "
                  "`0.9995 − 0.9990 = 0.0005`, which is `0.05%`. In units of the error "
                  "bar that is `0.0005 ÷ 0.000707 = 0.71` &mdash; less than one "
                  "standard error. A window that reports 99.95% against a 99.9% "
                  "objective has produced a number that a service sitting exactly on "
                  "the objective would produce routinely."),
            ("example", ("A window that says 99.95% and settles nothing",
                         "One thousand requests, 99.95% good, a 99.9% objective, and a "
                         "meeting. The measured ratio is above the objective, so the "
                         "objective was met &mdash; except that the same window run "
                         "again on a service that is exactly at 99.9% would land above "
                         "99.95% about a quarter of the time by arithmetic alone. The "
                         "honest report is &ldquo;99.95% ± 0.07%, which does not "
                         "separate us from the objective&rdquo;. It is a shorter "
                         "meeting.")),
            ("h3", "How many requests resolve a tenth of a per cent"),
            ("p", "Turn the formula round. To resolve a difference of `w`, ask for an "
                  "error bar of `w`: set `√(p(1 − p)/n) ≤ w` and solve for `n`. A "
                  "difference worth acting on is usually wanted at two standard errors "
                  "rather than one, so put half the gap in as `w`."),
            ("math", [
                "want   SE ≤ w,   so   p(1 − p)/n ≤ w²,   so   n ≥ p(1 − p)/w²",
                "",
                "gap of 0.05%, wanted at 2 SE:   w = 0.00025",
                "",
                "n ≥ (1999/4000000) ÷ (1/16000000)",
                "  = 1999 × 4",
                "  = 7 996 requests",
                "",
                "check by search: the smallest n with 2·√(p(1−p)/n) ≤ 0.0005  →  7 996",
            ]),
            ("p", "Two routes to one integer, which is the check: the closed form and "
                  "an exact scan over `n` agree on 7 996. At a hundred requests a "
                  "second that is eighty seconds, which is a useful thing to know "
                  "before anyone proposes a five-minute window as the unit an "
                  "objective is judged in."),
            ("p", "The `1/√n` is not specific to measurement. Estimating a quantity by "
                  "running a simulation many times has exactly the same error bar for "
                  "exactly the same reason, which is what &ldquo;Monte Carlo "
                  "Estimation and the Standard Error&rdquo; on the Operations Research "
                  "path is about: four times the runs for twice the precision, whether "
                  "the trials are simulated or served. No tail inequality is needed on "
                  "this page &mdash; Markov and Chebyshev, which bound a deviation "
                  "without knowing the distribution, are &ldquo;From Expectation to "
                  "Probability&rdquo; on the Algorithms path, and here the "
                  "distribution is known."),
            ("h3", "What the error bar does not cover"),
            ("p", "It covers sampling noise and nothing else. A denominator that "
                  "silently excludes the requests that never reached the load balancer "
                  "produces a ratio that is biased, not noisy, and doubling the window "
                  "makes it more precisely wrong. The same is true of a window whose "
                  "boundary falls in the middle of an incident, of retries counted as "
                  "separate valid events, and of a client-side timeout the server "
                  "never saw. Systematic error has no `√n` in it, and the only defence "
                  "is writing down what the denominator is."),
        ],
        "lab": ("measure", {
            "mode": "sli",
            "panel_title": "Set the window and what it measured",
            "panel_intro": (
                "The variance and the required `n` are exact fractions of the window "
                "and the ratio you set; the standard error is the square root of that "
                "fraction and is labelled as rounded. Push the window down to a few "
                "hundred requests and watch the error bar swallow the objective line, "
                "then find the `n` at which the two separate."
            ),
        }),
        "steps_title": "Putting a ± on a ratio you were handed",
        "steps_intro": (
            "The first two steps are arithmetic and the third is the one that changes "
            "what anybody says next."
        ),
        "steps": [
            ("Write down the denominator before the ratio",
             "What counts as a valid event, and over what window. If you cannot say it "
             "in a sentence, the number is not yet a measurement of anything and the "
             "error bar is the smaller of your problems."),
            ("Compute p(1 − p)/n, then take the root",
             "Keep the variance as a fraction and round only at the root. At `p` near "
             "one the product `p(1 − p)` is small and the arithmetic is easy: "
             "`0.999 × 0.001 = 0.000999`, divided by the window size."),
            ("Express the gap to the objective in units of SE",
             "Subtract, divide by the standard error, and say the answer out loud. "
             "Below about two, the window has not separated the measurement from the "
             "objective, and that is the finding &mdash; not a smaller finding than a "
             "clear pass or fail, a different one."),
            ("If the gap matters, solve for the window",
             "`n ≥ p(1 − p)/w²` with `w` set to half the gap you want resolved. Then "
             "ask whether that many requests exist in the period you are allowed to "
             "wait, because often they do not and the objective has to be judged over "
             "a longer window instead."),
        ],
        "worked": {
            "title": "1 000 requests, 99.95% measured, a 99.9% objective",
            "intro": [
                "Every figure below except the root is an exact fraction, and the root "
                "is the only rounded number on the page. The question is not whether "
                "99.95% is bigger than 99.9% &mdash; it plainly is &mdash; but whether "
                "this window can tell the difference.",
            ],
            "lines": [
                "p = 9995/10000 = 1999/2000            n = 1 000",
                "",
                "p(1 − p)      = (1999/2000)(1/2000) = 1999/4000000",
                "variance      = p(1 − p)/n          = 1999/4000000000",
                "",
                "SE            = √(1999/4000000000)",
                "              = 0.000706929…         ≈ 0.0707%   (rounded)",
                "",
                "gap           = 0.9995 − 0.9990 = 0.0005 = 0.05%",
                "gap ÷ SE      = 0.0005 ÷ 0.000706929 = 0.71",
                "",
                "so the window reports  99.95% ± 0.07%",
                "and the objective 99.90% is 0.71 SE away — inside the bar",
                "",
                "for a 2 SE separation:   w = 0.00025",
                "  n ≥ p(1 − p)/w² = (1999/4000000) × 16000000 = 7 996",
                "  exact scan over n agrees:  7 996",
            ],
            "after": [
                "The last block is the one to keep. A window of 1 000 requests can "
                "distinguish 99.95% from about 99.81% and from nothing closer; to "
                "separate it from 99.9% takes eight times as many requests, and to "
                "separate 99.99% from 99.95% would take far more again.",
                "For faded practice, take the same objective and a window of 5 000 "
                "requests reporting 99.92%. The supplied first move is "
                "`p(1 − p) = (2498/2500)(2/2500)`; compute the standard error, express "
                "the gap of 0.02% in units of it, and say in one sentence what the "
                "window has established. Then set the lab to those values and check "
                "the error bar against the objective line before opening the quiz.",
                "A last habit worth forming: when someone quotes an indicator to four "
                "significant figures, the first question is the window, not the "
                "figure. The digits past the error bar were produced by the division, "
                "not by the service.",
            ],
        },
        "quiz_title": "Ratios, windows and error bars",
        "quiz": [
            {"q": "A window of 1 000 requests reports 99.95% against a 99.9% objective, with a standard error of 0.0707%. What has the window established?",
             "a": ["That the objective was met, since 99.95% &gt; 99.9%",
                   "That the objective was missed, since the error bar reaches below it",
                   "That the measurement and the objective are 0.71 standard errors apart, which this window cannot separate",
                   "Nothing, because a standard error cannot be computed from one window"],
             "c": 2,
             "why": "The gap is `0.05% ÷ 0.0707% = 0.71` standard errors. That is neither "
                    "a pass nor a fail: it is a window too short to tell the two apart. "
                    "The first two answers read a difference smaller than the noise as a "
                    "verdict in opposite directions, which is how the same number ends up "
                    "supporting both sides of the argument."},
            {"q": "Traffic doubles, so a window of the same length now holds 2 000 requests instead of 1 000. What happens to the standard error?",
             "a": ["It halves", "It falls by a factor of `√2`, to about 71% of what it was",
                   "It is unchanged, because `p` is unchanged", "It doubles"],
             "c": 1,
             "why": "`SE = √(p(1 − p)/n)`, so `n` appears under a root: doubling `n` "
                    "divides the error bar by `√2 ≈ 1.414`. Halving it would need four "
                    "times the traffic. The third answer confuses the ratio, which is "
                    "unchanged in expectation, with the precision of the measurement of "
                    "it, which is not."},
            {"q": "You want to resolve a difference of 0.1% at two standard errors, around `p = 0.999`. Roughly how many valid events does that take?",
             "a": ["About 1 000", "About 4 000", "About 16 000", "About 400 000"],
             "c": 1,
             "why": "`w` is half the gap, `0.0005`, so `n ≥ p(1 − p)/w² = 0.000999 ÷ "
                    "0.00000025 ≈ 3 996`. About four thousand. `1 000` is the window that "
                    "cannot do it; `16 000` is what resolving 0.05% would take, four times "
                    "as many for half the distance; `400 000` is another factor of ten too "
                    "far."},
            {"q": "A team excludes from the denominator every request that timed out at the client without reaching the server. What does a longer window do to the resulting indicator?",
             "a": ["It narrows the error bar and leaves the exclusion intact",
                   "It corrects the exclusion, because more data covers more cases",
                   "It widens the error bar, because the excluded requests add variance",
                   "Nothing, since excluded events never affected the ratio"],
             "c": 0,
             "why": "The exclusion is a systematic error and `√n` does not appear in it: "
                    "more data makes a biased ratio more precisely biased. The error bar "
                    "shrinks and the number moves no closer to the truth. This is why the "
                    "denominator is written down before the measurement rather than "
                    "discovered afterwards."},
        ],
        "mistakes": [
            ("Reading a ratio over requests as a ratio over users",
             "&ldquo;Our p99 is 200 ms, so 99% of users see under 200 ms&rdquo; is the "
             "same slip in percentile clothing, and it is wrong in the direction that "
             "matters. A user who makes ten requests meets the slow tail with "
             "probability `1 − 0.99¹⁰ = 9.56%`, not 1%, and a page that fans out to "
             "twenty backend calls is worse again. The indicator counts events; a user "
             "is a bundle of them, and &ldquo;Tail Amplification under Fan-out&rdquo; "
             "on the Latency and the Tail course is the arithmetic that converts one "
             "into the other."),
            ("Quoting more digits than the window supports",
             "99.9473% from a five-minute window is a division carried out to six "
             "figures on a measurement good to two. The digits are real arithmetic and "
             "they are not information, and once they are in a dashboard someone will "
             "compare two of them and find a difference. Round the report to the error "
             "bar and state the bar."),
            ("Changing the denominator between the two windows being compared",
             "Last month excluded health checks and this month does not, so the "
             "indicator moved by more than any error bar explains and nothing happened "
             "to the service. Any comparison of two indicators is first a comparison "
             "of two denominators, and a change in definition should be recorded as an "
             "event on the graph rather than absorbed into it."),
        ],
        "standard": ("Finish when a difference smaller than the error bar reads as a finding, not as a result.",
                     "You should be able to state the denominator and window of any "
                     "indicator you quote, compute `√(p(1 − p)/n)` from them, express "
                     "the gap to an objective in units of it, solve `n ≥ p(1 − p)/w²` "
                     "for a stated resolution, and say which of your error sources the "
                     "square root does not cover."),
        "note": "Every number after this one is a percentile rather than a ratio, and "
                "percentiles fail in a second way that has nothing to do with noise: "
                "they are routinely combined by an operation that is not defined on "
                "them. &ldquo;Percentiles Do Not Average&rdquo; takes three hosts whose "
                "individual p99s are 12, 14 and 400 ms and shows that the average of "
                "those three numbers lands below the fleet&rsquo;s median.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "percentiles-do-not-average",
        "title": "Percentiles Do Not Average",
        "module": "Aggregates that lie",
        "one_line": "Compute a fleet p99 from the merged sample, and the mean of the per-host p99s on the same data, and say what the second one is.",
        "summary": (
            "A fleet percentile is the percentile of the merged sample: one definition, "
            "applied once, to every request. The number most dashboards show instead is "
            "the mean of the per-host percentiles, which is not a percentile of "
            "anything and is not an estimate of one. On the sample in the lab the three "
            "host p99s are 12, 14 and 400 ms, their mean is 142 ms, and the fleet "
            "median is 180 ms &mdash; so the average of three 99th percentiles lands "
            "below the middle of the distribution it is supposed to sit far above."
        ),
        "key": [
            "fleet p99 = p99 of the merged sample     one definition, applied once",
            "mean of per-host p99s = a percentile of nothing",
            "preset  host p99s  12, 14, 400 ms        hosts carry 5, 5 and 90 requests",
            "        mean 142      fleet p99 400      fleet median 180",
            "142 sits BELOW the median it should sit far above",
            "min pᵢ ≤ fleet p ≤ max pᵢ                the mean is inside the range too",
        ],
        "key_label": "Two numbers from one set of requests",
        "concepts_intro": (
            "The definition is the whole lesson. What has to be added to it is why the "
            "wrong number looks so reasonable, and what it is actually weighting."
        ),
        "concepts": [
            ("A percentile is defined on a sample, so the fleet one needs the fleet sample",
             "Nearest rank, as &ldquo;Percentiles from a Sample&rdquo; on the Latency "
             "and the Tail course defines it: sort the `n` values, take the one at "
             "position `⌈q·n⌉`. Applied to one host&rsquo;s requests it gives that "
             "host&rsquo;s p99; applied to every request the fleet served it gives the "
             "fleet&rsquo;s. These are two different samples, so they are two different "
             "questions, and only the second one is about the fleet."),
            ("The mean of the per-host values weights hosts; the fleet percentile weights requests",
             "That is the entire mechanism. In the lab&rsquo;s sample one host served "
             "90 of the 100 requests and the other two served five each, so averaging "
             "the three p99s gives the busy host one vote out of three when it "
             "deserves ninety out of a hundred. The result, 142 ms, is dragged down by "
             "two hosts that between them handled a tenth of the traffic."),
            ("The fleet value is bounded by the per-host values, which is why the mean looks safe",
             "If every host reports a p99 at or below `v`, then at least 99% of each "
             "host&rsquo;s requests are at or below `v`, so at least 99% of all of them "
             "are, and the fleet p99 is at or below `v` as well. The same argument "
             "downward gives `min pᵢ ≤ fleet p ≤ max pᵢ`, and the mean is inside that "
             "range too. So the wrong number is never absurd, which is precisely why it "
             "survives review. It is simply not the answer to any question."),
        ],
        "read_title": "The fleet percentile, the number that is not one, and the bound they share",
        "read_intro": (
            "One definition applied to two samples, why the average of per-host "
            "percentiles is not an estimate of the fleet value, and what the per-host "
            "values do and do not determine."
        ),
        "body": [
            ("def", ("Fleet percentile",
                     "Given the requests served by every host in a fleet over a window, "
                     "the <strong>fleet q-th percentile</strong> is the q-th percentile "
                     "of that single merged sample: sort all `n` latencies and take the "
                     "one at position `⌈q·n⌉`. It is computed from requests, not from "
                     "per-host summaries, and every request counts once.")),
            ("p", "There is no second definition. The bucketed percentile of "
                  "&ldquo;Histograms and Bucket Error&rdquo; and the corrected "
                  "percentile of &ldquo;Coordinated Omission&rdquo; are this same rule "
                  "applied to a coarsened sample and to a repaired one. Where two of "
                  "this course&rsquo;s numbers disagree, the disagreement is about "
                  "which requests were in the sample, never about what a percentile is."),
            ("p", "The number a metrics system usually makes easy, by contrast, is one "
                  "p99 per host per minute, and the obvious thing to do with several of "
                  "those is to average them. That average has a name in no textbook. It "
                  "is not the fleet p99, it is not an estimate of the fleet p99, and it "
                  "does not converge to the fleet p99 as the window grows."),
            ("math", [
                "host A   8, 9, 10, 11, 12                            5 requests",
                "host B   10, 11, 12, 13, 14                          5 requests",
                "host C   150×20, 180×20, 220×20, 260×15, 320×10, 400×5   90 requests",
                "",
                "per host, nearest rank at q = 99/100:",
                "  A   ⌈0.99×5⌉  = 5   of 5    →  12 ms",
                "  B   ⌈0.99×5⌉  = 5   of 5    →  14 ms",
                "  C   ⌈0.99×90⌉ = 90  of 90   →  400 ms",
                "",
                "mean of the three                = (12 + 14 + 400)/3 = 142 ms",
                "",
                "merged sample, n = 100:",
                "  fleet p99   ⌈0.99×100⌉ = 99  of 100  →  400 ms",
                "  fleet p50   ⌈0.50×100⌉ = 50  of 100  →  180 ms",
            ]),
            ("p", "Read the last three lines together. The average of three 99th "
                  "percentiles is 142 ms; the fleet&rsquo;s median is 180 ms. The "
                  "number being presented as a statement about the slowest one per cent "
                  "of requests is smaller than the number that half of all requests "
                  "beat. It is not a slightly optimistic p99. It is below the middle."),
            ("thm", ("The fleet percentile lies between the smallest and the largest per-host percentile",
                     "Let host `i` have `nᵢ` requests and q-th percentile `pᵢ`, and let "
                     "`M = max pᵢ`. At least a fraction `q` of each host&rsquo;s "
                     "requests are at most `pᵢ ≤ M`, so at least a fraction `q` of all "
                     "`Σnᵢ` requests are at most `M`, and the merged q-th percentile is "
                     "therefore at most `M`. Running the argument with `m = min pᵢ` from "
                     "the other side gives",
                     "`min pᵢ ≤ fleet p ≤ max pᵢ`.",
                     "One corollary is worth stating because the folklore gets it "
                     "backwards: if every host reports the <em>same</em> p99, the fleet "
                     "p99 is that number exactly &mdash; the bound closes. Percentiles "
                     "fail to average, but they do not fail by leaving the range of "
                     "the values being averaged.")),
            ("p", "So the mean of the per-host values is always somewhere plausible, "
                  "and it is why nobody notices. What the bound does not give you is "
                  "the value: anywhere inside `[min, max]` is consistent with the "
                  "per-host figures, and where the fleet value actually falls depends "
                  "on data the per-host summaries threw away."),
            ("h3", "The per-host percentiles do not determine the fleet percentile"),
            ("p", "That claim deserves a demonstration rather than an assertion, so "
                  "here are two fleets. Both have two hosts, both hosts serve a hundred "
                  "requests, and in both fleets the two host p99s are 40 ms and 100 ms. "
                  "The fleet p99 is not the same number in the two cases."),
            ("example", ("Two fleets, the same pair of host p99s, two different answers",
                         "<strong>Fleet one.</strong> Host X is 98 requests at 10 ms, "
                         "one at 40, one at 50; its p99 is position 99 of 100, which is "
                         "40 ms. Host Y is 98 at 20 ms, one at 100, one at 200; its p99 "
                         "is 100 ms. Merged, `n = 200` and the fleet p99 is position "
                         "198, which is <strong>50 ms</strong>.",
                         "<strong>Fleet two.</strong> Host X is 98 at 10 ms and two at "
                         "40; its p99 is again 40 ms. Host Y is 96 at 30 ms and four at "
                         "100; its p99 is again 100 ms. Merged, position 198 of 200 is "
                         "<strong>100 ms</strong>.",
                         "Same two host p99s, fleet answers of 50 ms and 100 ms. The "
                         "average, 70 ms, is a fact about neither fleet, and it is not "
                         "even between the two right answers in any useful sense: it is "
                         "above one and below the other. Both fleet values sit inside "
                         "`[40, 100]`, exactly as the bound promises, and the bound is "
                         "the most that can be said without the requests.")),
            ("h3", "What you can combine, and what to keep instead"),
            ("p", "Counts and sums combine, because they are additive: total requests, "
                  "total errors, total milliseconds. A ratio of two sums is fine "
                  "&mdash; the fleet error rate really is the sum of the errors over "
                  "the sum of the requests &mdash; and so is a mean weighted by its own "
                  "denominator. It is the order statistics that do not: a percentile, a "
                  "median, a maximum-of-percentiles all need the sample."),
            ("p", "The practical answer is to keep something mergeable. A histogram of "
                  "counts per bucket adds bucket by bucket, and the percentile is read "
                  "off the merged histogram rather than averaged across hosts; that is "
                  "what almost every metrics system is doing when it gets this right. "
                  "It costs an interval instead of a point, which is the subject of the "
                  "next page, and an interval that contains the answer is a better "
                  "object than a point that does not."),
        ],
        "lab": ("measure", {
            "mode": "aggregate",
            "panel_title": "Edit the per-host samples",
            "panel_intro": (
                "Both numbers are nearest rank, computed by the same function: one on "
                "each host&rsquo;s sample, one on the merged sample. Move requests "
                "between the hosts without changing any latency and watch the mean of "
                "the p99s move while the fleet p99 stays put &mdash; the mean is "
                "responding to how the traffic was divided, which is not a property of "
                "the service at all."
            ),
        }),
        "steps_title": "Aggregating a percentile across hosts",
        "steps_intro": (
            "The first step is the one that gets skipped, and skipping it is what makes "
            "the rest impossible."
        ),
        "steps": [
            ("Ask what sample the number is a percentile of",
             "If the answer is &ldquo;several samples&rdquo;, it is not a percentile "
             "yet. Write down how many requests each contributing host served; the "
             "moment those counts are unequal, the mean of the per-host values is "
             "weighting hosts rather than requests."),
            ("Merge the requests, then take the percentile once",
             "Sort the combined latencies and take position `⌈q·n⌉`. This is the "
             "answer. Everything else on this page is about what to do when you cannot "
             "get the requests."),
            ("If you cannot merge requests, merge histograms",
             "Bucket counts add across hosts, so the merged histogram is exact even "
             "though the percentile read from it is an interval. An interval that "
             "certainly contains the fleet p99 beats a point that certainly is not it."),
            ("Bound what you have, and report the bound as a bound",
             "With only per-host percentiles, `min pᵢ ≤ fleet p ≤ max pᵢ` is "
             "everything that can honestly be said. Report the range. If the range is "
             "too wide to act on, that is a finding about the pipeline, not about the "
             "service."),
            ("Say which one your dashboard is showing",
             "Most panels that plot one line per host and then add an aggregation are "
             "averaging percentiles by default. Find the aggregation setting, read it, "
             "and write the answer in the panel description so the next person does not "
             "have to."),
        ],
        "worked": {
            "title": "Three hosts, one hundred requests, two answers",
            "intro": [
                "The three samples are the lab&rsquo;s preset. Two of the hosts are "
                "healthy and lightly loaded; the third is carrying the traffic and is "
                "slow. Nothing here is adversarial &mdash; it is what a fleet behind a "
                "load balancer with a stuck host looks like.",
            ],
            "lines": [
                "host A    8, 9, 10, 11, 12                                  n = 5",
                "host B    10, 11, 12, 13, 14                                n = 5",
                "host C    150×20  180×20  220×20  260×15  320×10  400×5     n = 90",
                "                                                     total  n = 100",
                "",
                "per host, nearest rank ⌈q·n⌉ at q = 0.99:",
                "  A   rank 5 of 5     →   12 ms",
                "  B   rank 5 of 5     →   14 ms",
                "  C   rank 90 of 90   →  400 ms",
                "",
                "the average of the three                 (12 + 14 + 400)/3 = 142 ms",
                "",
                "merged and sorted:",
                "  positions   1–10    8, 9, 10, 10, 11, 11, 12, 12, 13, 14",
                "  positions  11–30    150          positions  31–50    180",
                "  positions  51–70    220          positions  71–85    260",
                "  positions  86–95    320          positions  96–100   400",
                "",
                "  fleet p99   rank ⌈0.99×100⌉ = 99   →  400 ms",
                "  fleet p50   rank ⌈0.50×100⌉ = 50   →  180 ms",
                "",
                "  142 < 180:  the average of three 99th percentiles is below the median",
            ],
            "after": [
                "The bound holds throughout: `12 ≤ 400 ≤ 400`, and the average 142 is "
                "inside `[12, 400]` as well. Nothing here is out of range. The average "
                "is wrong by being an answer to no question, not by being extreme, and "
                "that is why it needs a worked example rather than a warning.",
                "Notice also what a per-host p99 means on a five-request host: nearest "
                "rank at `⌈0.99 × 5⌉ = 5` is the maximum. Host A&rsquo;s "
                "&ldquo;p99&rdquo; of 12 ms is its slowest request out of five, and two "
                "of the three numbers being averaged are maxima of tiny samples. The "
                "lab makes this visible &mdash; move requests onto A and watch its "
                "reported p99 stop being its maximum.",
                "For faded practice, keep the three samples and change only the "
                "division of traffic: give host C thirty requests and hosts A and B "
                "thirty-five each, drawn from the same value lists. The supplied first "
                "move is that the three per-host p99s barely change. Predict the new "
                "fleet p99 and the new average before you compute either, then check "
                "both in the lab and say which of the two moved and why.",
            ],
        },
        "quiz_title": "Fleet percentiles and per-host summaries",
        "quiz": [
            {"q": "Three hosts report p99s of 12, 14 and 400 ms, on 5, 5 and 90 requests. The fleet p99 of the merged 100 requests is 400 ms and the fleet median is 180 ms. What is the number 142?",
             "a": ["An estimate of the fleet p99, biased low by the small hosts",
                   "The mean of the three per-host p99s, which is not a percentile of any sample",
                   "The fleet p99 computed with hosts weighted by request count",
                   "The p99 of the two fast hosts merged"],
             "c": 1,
             "why": "`(12 + 14 + 400)/3 = 142` is an average of three order statistics "
                    "taken from three different samples. It is not an estimator of the "
                    "fleet p99 &mdash; it does not converge to it as the window grows "
                    "&mdash; and here it is below the fleet median of 180. Weighting by "
                    "request count would give a different wrong number, not this one."},
            {"q": "Every host in a fleet reports a p99 of exactly 90 ms. What is the fleet p99 of the merged sample?",
             "a": ["Exactly 90 ms", "Somewhere above 90 ms, because merging exposes more of the tail",
                   "Somewhere below 90 ms, because the fast hosts dilute the slow ones",
                   "Not determined by the per-host values"],
             "c": 0,
             "why": "At least 99% of each host&rsquo;s requests are at most 90 ms, so at "
                    "least 99% of all requests are, and the same argument from below "
                    "closes the bound: `min pᵢ ≤ fleet p ≤ max pᵢ` with both ends at 90. "
                    "The popular claim that identical per-host percentiles can pool to "
                    "something different is simply false. Percentiles fail to average; "
                    "they do not leave the range."},
            {"q": "Two hosts each serve 100 requests, with p99s of 40 ms and 100 ms. What can you say about the fleet p99?",
             "a": ["It is 70 ms", "It is 100 ms", "It is somewhere in `[40, 100]`, and the host p99s do not pin it down",
                   "It is at least 100 ms, since merging can only add tail"],
             "c": 2,
             "why": "The bound gives `[40, 100]` and nothing tighter. Two fleets with "
                    "exactly these host p99s can have fleet p99s of 50 ms and of 100 ms, "
                    "depending on how many requests sit near each host&rsquo;s own "
                    "99th-percentile rank &mdash; information the summaries discarded. "
                    "`70` is the average, which is a fact about neither."},
            {"q": "Your metrics pipeline keeps only a per-host histogram of latency counts per bucket, not the raw requests. Can you compute a fleet percentile?",
             "a": ["No &mdash; percentiles need the raw sample",
                   "Yes, exactly, by summing the bucket counts across hosts",
                   "Yes, to within a bucket, by summing the bucket counts and reading the rank off the merged histogram",
                   "Only if every host has the same bucket boundaries and the same request count"],
             "c": 2,
             "why": "Counts are additive, so the merged histogram is exact; what the "
                    "histogram costs is resolution, so the percentile read from it is the "
                    "containing bucket rather than a value. Equal request counts are not "
                    "needed &mdash; that is the point of merging counts rather than "
                    "summaries. Shared boundaries are needed, and that is a pipeline "
                    "decision made once."},
        ],
        "mistakes": [
            ("Averaging the per-host percentiles",
             "The headline error, and it is usually made by a dashboard rather than by "
             "a person: a panel plots one series per host and an aggregation of "
             "&ldquo;avg&rdquo; is applied over them. The fix is to merge before taking "
             "the percentile, or to merge histograms and read the percentile off the "
             "sum. Check what your panel is configured to do before quoting its number "
             "in an incident review."),
            ("Taking the maximum of the per-host p99s as the fleet p99",
             "It is an upper bound and it is often loose. On the worked sample it "
             "happens to be exactly right &mdash; both are 400 ms &mdash; which is how "
             "the habit forms; in the two-host example above the maximum is 100 ms and "
             "the fleet p99 is 50 ms, wrong by a factor of two in the direction that "
             "causes a pointless investigation. Report it as a bound if you use it."),
            ("Quoting a per-host percentile from a sample too small to have one",
             "Nearest rank at `⌈0.99 × 5⌉` is rank 5 of 5: the maximum, relabelled. A "
             "host serving five requests a minute has no p99, and averaging its "
             "&ldquo;p99&rdquo; with anything gives the maximum of five requests a vote "
             "equal to a host that served ninety. A percentile needs enough samples to "
             "have a rank that is not the last one &mdash; a point &ldquo;How Long to "
             "Run a Load Test&rdquo; turns into an exact request count."),
        ],
        "standard": ("Finish when “what sample is this a percentile of?” is the first question you ask about any aggregate.",
                     "You should be able to compute a fleet percentile from merged "
                     "samples by nearest rank, compute the mean of the per-host values "
                     "on the same data and say what it is, state and use the bound "
                     "`min pᵢ ≤ fleet p ≤ max pᵢ`, and name what your own pipeline "
                     "aggregates."),
        "note": "Merging histograms rescues the aggregation and costs resolution: the "
                "answer stops being a value and becomes the bucket that contains it. "
                "&ldquo;Histograms and Bucket Error&rdquo; computes how wide that "
                "bucket is &mdash; on logarithmic boundaries the relative error is "
                "`ratio − 1`, which at the usual ratio of two is one hundred per cent, "
                "in every bucket, no matter how much traffic you collect.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "histograms-and-bucket-error",
        "title": "Histograms and Bucket Error",
        "module": "Aggregates that lie",
        "one_line": "Report a percentile read from a histogram as the interval it is actually known to, and compute that interval's relative width.",
        "summary": (
            "A histogram keeps counts per bucket and throws the values away, so a "
            "percentile read from it is known only to the width of the bucket it lands "
            "in. On logarithmic boundaries every bucket has the same relative width, "
            "`ratio − 1`, so the usual ratio of two means every percentile is known to "
            "within a factor of two &mdash; a hundred per cent relative error that does "
            "not shrink with more traffic, because it is not noise."
        ),
        "key": [
            "edges  b, b·r, b·r², …        here 25, 50, 100, 200, 400, 800, 1 600 ms",
            "exact p99 of the sample = 137 ms",
            "from the histogram:  p99 ∈ [100, 200)          the bucket, and no finer",
            "relative width  (r·x − x)/x = r − 1            r = 2 → 100%, every bucket",
            "r = 5/4 → 25%, at 3.1× as many buckets to cover the same range",
            "bucket error is systematic: ten times the traffic does not narrow it",
        ],
        "key_label": "What a bucketed percentile is known to",
        "concepts_intro": (
            "A histogram is a lossy compression with a known loss, which is a better "
            "object than it sounds. The three ideas are what is lost, how much, and why "
            "the loss does not respond to more data."
        ),
        "concepts": [
            ("A histogram keeps counts and discards values",
             "Each request increments the counter for the bucket its latency fell in, "
             "and the latency itself is gone. What survives is enough to say how many "
             "requests were below any boundary, which is enough to find which bucket a "
             "given rank falls in &mdash; and not enough to say where inside that "
             "bucket it fell. The percentile is therefore an interval: the bucket, "
             "reported as `[lower, upper)`."),
            ("Logarithmic boundaries give a constant relative error",
             "With edges in a geometric progression `b, b·r, b·r², …`, a bucket "
             "starting at `x` ends at `r·x`, so its width relative to its own position "
             "is `(r·x − x)/x = r − 1` everywhere. At `r = 2` that is 100% in every "
             "bucket, at the bottom of the range and at the top. The choice of `r` is a "
             "choice of precision, made once, and it applies uniformly."),
            ("Bucket error is systematic, so traffic does not fix it",
             "The error bar of &ldquo;SLIs as Ratios&rdquo; shrinks as `1/√n`; this one "
             "does not shrink at all. Ten times the requests put ten times the counts "
             "in the same buckets and the answer is still an interval of the same "
             "relative width. The two errors compose: a percentile from a histogram is "
             "uncertain by a rank that moves with the noise <em>and</em> by a bucket "
             "that does not move at all."),
        ],
        "read_title": "Reading a percentile off counts, and the width of the answer",
        "read_intro": (
            "How a rank is located in a table of counts, what the answer is an interval "
            "of, and why interpolating inside the bucket invents a digit."
        ),
        "body": [
            ("def", ("Histogram, and the percentile read from one",
                     "A <strong>histogram</strong> over boundaries "
                     "`e₀ &lt; e₁ &lt; … &lt; e_k` stores, for each bucket "
                     "`[eᵢ, eᵢ₊₁)`, the count of observations falling in it, plus an "
                     "underflow count below `e₀` and an overflow count at or above "
                     "`e_k`. The <strong>bucketed q-th percentile</strong> is the "
                     "bucket containing rank `⌈q·n⌉` in the cumulative counts. Its "
                     "value is that bucket, not a number inside it.")),
            ("p", "Boundaries are chosen once, before any data arrives, and they are "
                  "chosen geometrically because latency spans orders of magnitude: a "
                  "millisecond and a second belong in the same picture, and equal-width "
                  "buckets that resolve the first give thousands of empty ones before "
                  "the second. The lab&rsquo;s preset starts at 25 ms and doubles."),
            ("math", [
                "edges   25, 50, 100, 200, 400, 800, 1 600 ms        base 25, ratio 2",
                "",
                "sample  30×40   45×25   60×15   85×10   120×6   137×3   400×1",
                "                                                  n = 100",
                "",
                "bucket        count   cumulative",
                "  [25, 50)      65        65        30×40 and 45×25",
                "  [50, 100)     25        90        60×15 and 85×10",
                "  [100, 200)     9        99        120×6 and 137×3",
                "  [200, 400)     0        99",
                "  [400, 800)     1       100",
                "",
                "p99   rank ⌈0.99×100⌉ = 99   first reached in  [100, 200)",
            ]),
            ("p", "The exact p99 of that sample is 137 ms: sort the hundred values and "
                  "take the 99th. The histogram cannot say 137. It can say that the "
                  "99th value is at least 100 and less than 200, which is true, useful, "
                  "and a hundred milliseconds wide."),
            ("thm", ("The relative width of a geometric bucket",
                     "Let the boundaries be `eᵢ = b·rⁱ` with `r &gt; 1`. A value "
                     "reported as lying in `[eᵢ, eᵢ₊₁)` is known to within an absolute "
                     "width `eᵢ₊₁ − eᵢ = eᵢ(r − 1)`, so relative to the smallest value "
                     "it could be, the width is",
                     "`(eᵢ₊₁ − eᵢ)/eᵢ = r − 1`,",
                     "independent of `i`. At `r = 2` every bucketed answer is known to "
                     "within a factor of two &mdash; 100% &mdash; and at `r = 5/4` to "
                     "within 25%. The price of the smaller `r` is buckets: covering the "
                     "same range needs `ln 2 ÷ ln(5/4) ≈ 3.1` times as many.")),
            ("p", "That factor of 3.1 is not free, and the bill arrives in a different "
                  "lesson. Every bucket is a time series with its own label value, so "
                  "tripling the buckets triples the series count and the storage, which "
                  "is the arithmetic of &ldquo;Metric Cardinality&rdquo;. Resolution in "
                  "a histogram is bought with cardinality, and the exchange rate is "
                  "known in advance."),
            ("example", ("Two histograms of the same requests",
                         "On the sample above with `r = 2`, the p99 is `[100, 200)` "
                         "&mdash; a width of 100 ms around a true value of 137. Refine "
                         "to `r = 5/4` starting at the same 25 ms and the boundaries "
                         "near the answer become `…, 119.21, 149.01, …`; the same rank "
                         "now lands in `[119.21, 149.01)`, a width of about 30 ms. The "
                         "true value did not move and no new requests were collected. "
                         "The report got narrower because the boundaries did.")),
            ("h3", "Interpolating inside the bucket"),
            ("p", "It is tempting, and most metrics systems do it: assume the "
                  "observations are spread evenly across the bucket and read off a "
                  "point. On the sample above, linear interpolation inside `[100, 200)` "
                  "returns a confident 200 ms &mdash; the top of the bucket, since rank "
                  "99 is the last of the nine observations in it &mdash; against a true "
                  "137. The assumption of uniformity is wrong in the direction that "
                  "matters, because latency inside a bucket is not uniform; it is "
                  "concentrated near the bottom, which is why the bucket boundaries "
                  "were geometric in the first place."),
            ("p", "Interpolation does not add information. It converts an honest "
                  "interval into a point whose error you can no longer see, and the "
                  "point is not even guaranteed to be inside the range of the data. "
                  "Report the interval; if it is too wide to act on, change the "
                  "boundaries rather than the arithmetic."),
            ("h3", "What the histogram is still good for"),
            ("p", "Everything the previous page needed. Counts add, so histograms from "
                  "many hosts merge exactly, and a percentile read from the merged "
                  "histogram is a real fleet percentile with a known interval around "
                  "it. That is a strictly better object than an averaged per-host "
                  "percentile, which has no interval around it because it is not an "
                  "estimate of anything."),
            ("p", "It is also the right place to be honest about what a dashboard can "
                  "promise. A p99 of &ldquo;about 150 ms&rdquo; from `r = 2` buckets "
                  "means somewhere in `[100, 200)`; a regression from 137 ms to 195 ms "
                  "would not move the reported bucket at all, and a regression from 199 "
                  "to 201 would move it a whole bucket. Alerting on a bucketed "
                  "percentile inherits both behaviours, and choosing boundaries so that "
                  "the values you care about are not near an edge is part of the "
                  "design."),
        ],
        "lab": ("measure", {
            "mode": "histogram",
            "panel_title": "Set the buckets and the sample",
            "panel_intro": (
                "The exact percentile of the sample and the bucket the histogram can "
                "report are computed by the same nearest-rank function, one on the "
                "values and one on the cumulative counts. Change the ratio from 2 to "
                "5/4 and watch the interval narrow while the exact value stays exactly "
                "where it was; then add ten times as many requests and watch the "
                "interval not narrow at all."
            ),
        }),
        "steps_title": "Reporting a percentile from bucket counts",
        "steps_intro": (
            "Four steps, and the last one is the difference between a measurement and "
            "a number."
        ),
        "steps": [
            ("Find the rank you are looking for",
             "`⌈q·n⌉` where `n` is the total count across every bucket, including the "
             "underflow and the overflow. Getting `n` wrong by forgetting the overflow "
             "bucket moves the rank and can move the answer by a whole bucket."),
            ("Walk the cumulative counts until they reach it",
             "Add the bucket counts from the bottom. The first bucket whose cumulative "
             "total reaches the rank is the containing bucket. If the rank is only "
             "reached in the overflow bucket, the honest answer is &ldquo;at least "
             "`e_k`&rdquo; and the boundaries are too low for this workload."),
            ("Report the bucket, with both ends",
             "`[100, 200)`, not 150 and not 137. The half-open interval matters when a "
             "boundary is also a common value &mdash; a 100 ms timeout piles requests "
             "exactly on an edge, and which side they land is a convention you should "
             "know rather than discover."),
            ("Quote the relative width alongside it",
             "`r − 1`. It is the same number for every bucket and it is the honest "
             "precision of every percentile the histogram will ever report. If it is "
             "wider than the change you need to detect, the boundaries are wrong and no "
             "amount of traffic will fix them."),
        ],
        "worked": {
            "title": "A p99 of 137 ms that a doubling histogram can only call [100, 200)",
            "intro": [
                "One hundred requests, boundaries starting at 25 ms and doubling. The "
                "exact answer and the reportable answer are computed from the same "
                "sample by the same rule, which is what makes the gap between them a "
                "property of the boundaries rather than of the method.",
            ],
            "lines": [
                "sample   30×40   45×25   60×15   85×10   120×6   137×3   400×1",
                "         n = 100",
                "",
                "exact:   sort and take rank ⌈0.99×100⌉ = 99",
                "         positions  1–40  =  30       41–65  =  45",
                "                   66–80  =  60       81–90  =  85",
                "                   91–96  = 120       97–99  = 137      100 = 400",
                "         rank 99  →  137 ms",
                "",
                "edges    25, 50, 100, 200, 400, 800, 1 600        base 25, ratio 2",
                "",
                "         bucket        count   cumulative",
                "         [25, 50)        65        65",
                "         [50, 100)       25        90",
                "         [100, 200)       9        99   ← rank 99 first reached here",
                "         [200, 400)       0        99",
                "         [400, 800)       1       100",
                "",
                "reported p99   [100, 200)          width 100 ms",
                "relative width r − 1 = 1 = 100%     the same in every bucket",
                "",
                "true value 137 is inside the interval, and the interval is all",
                "the histogram knows — with 10× or 1 000× the traffic, still all",
            ],
            "after": [
                "The last line is the one that separates this error from the one on the "
                "first page of the course. Sampling noise shrinks as `1/√n`; bucket "
                "width does not shrink at all. A dashboard showing a bucketed p99 over "
                "a month of traffic is showing an interval exactly as wide as the one "
                "it showed after five minutes.",
                "Notice the empty `[200, 400)` bucket and the single observation in "
                "`[400, 800)`. That lone request is the p100, and the histogram places "
                "it within a factor of two as well: somewhere in `[400, 800)`. If your "
                "maximum matters, `r = 2` says it to one significant figure.",
                "For faded practice, keep the sample and the base of 25 and set the "
                "ratio to 3/2. The supplied first move is that the boundaries become "
                "`25, 37.5, 56.25, 84.375, 126.5625, 189.84…`. Predict which bucket "
                "rank 99 lands in and what the relative width becomes, then check both "
                "in the lab and count how many buckets it now takes to reach 800 ms.",
            ],
        },
        "quiz_title": "Buckets, ranks and intervals",
        "quiz": [
            {"q": "A histogram with boundaries 25, 50, 100, 200, 400 ms reports its p99 in the bucket `[100, 200)`. The exact p99 of the same requests is 137 ms. What is the relative error of the bucketed answer?",
             "a": ["About 45%, the distance from 137 to 200 over 137",
                   "100%, the ratio minus one, which is the width of every bucket relative to its own lower edge",
                   "It cannot be stated without knowing the exact value",
                   "It falls as more requests are collected"],
             "c": 1,
             "why": "The reportable precision is a property of the boundaries: "
                    "`(r·x − x)/x = r − 1 = 1`, the same in every bucket. The first "
                    "answer measures a distance you could only compute by already "
                    "knowing the exact value, which is the thing the histogram does not "
                    "have. The last answer confuses this with sampling noise."},
            {"q": "You collect a hundred times as many requests into the same histogram. What happens to the width of the reported p99 interval?",
             "a": ["It falls by a factor of 10, as `√n`", "It falls by a factor of 100",
                   "It is unchanged", "It grows, because the tail fills in"],
             "c": 2,
             "why": "Bucket error is systematic, not statistical: more requests put more "
                    "counts in the same buckets, and the answer is still &ldquo;the "
                    "bucket&rdquo;. The `√n` answers are the error bar of a measured "
                    "ratio, which is a different error in the same number. Both are "
                    "present; only one responds to traffic."},
            {"q": "Moving from a bucket ratio of 2 to a ratio of 5/4 improves the relative error from 100% to 25%. What does it cost?",
             "a": ["Nothing &mdash; the same counters hold more precise boundaries",
                   "About 3.1 times as many buckets, and so about 3.1 times the series and storage",
                   "Four times as many buckets, since 100/25 = 4",
                   "Accuracy at the top of the range, where the buckets become too narrow"],
             "c": 1,
             "why": "Covering a fixed range takes `ln 2 ÷ ln(5/4) ≈ 3.1` times as many "
                    "geometric steps. Each bucket is a series, so this is a cardinality "
                    "cost, computed exactly in &ldquo;Metric Cardinality&rdquo;. The "
                    "`100/25 = 4` answer divides the precisions instead of comparing the "
                    "logarithms of the ratios."},
            {"q": "A service has a hard 100 ms timeout, and the histogram boundaries include 100 ms. Why is that a problem?",
             "a": ["It is not &mdash; a boundary at a meaningful value is ideal",
                   "Because the timeout pile-up lands exactly on an edge, so which bucket it counts in is a convention rather than a measurement",
                   "Because a bucket boundary must be a power of the ratio times the base",
                   "Because timeouts should be excluded from latency histograms"],
             "c": 1,
             "why": "A large mass of observations at exactly the boundary value makes the "
                    "half-open convention `[100, 200)` against `(100, 200]` decide where "
                    "a big fraction of the distribution is reported, and the reported "
                    "percentile can jump a whole bucket on a convention. Put boundaries "
                    "where the data is sparse, not where it piles up."},
        ],
        "mistakes": [
            ("Reporting a bucketed percentile as a number",
             "&ldquo;p99 = 150 ms&rdquo; from `r = 2` buckets is an interval "
             "`[100, 200)` with a midpoint printed in place of it, and the midpoint is "
             "not more likely than either end &mdash; inside a geometric bucket the "
             "mass sits low. Report the bucket. If a single number is unavoidable, "
             "report the lower edge and say it is a lower bound."),
            ("Expecting more traffic to sharpen the answer",
             "It sharpens the rank and not the bucket. A team that waits for a longer "
             "window to settle an argument about whether the p99 is 130 or 190 ms will "
             "wait for ever, because both are `[100, 200)` and the histogram has no "
             "opinion. The fix is boundaries, and it is retroactive only if the raw "
             "requests were kept."),
            ("Choosing linear buckets for a latency distribution",
             "Equal-width buckets give a relative error of `width/x`, which is "
             "enormous at the bottom of the range and negligible at the top &mdash; "
             "exactly backwards for latency, where the interesting structure is at "
             "small values and the tail is one long thin thing. Ten-millisecond buckets "
             "resolve a 1 000 ms p999 to 1% and a 5 ms median to 200%."),
        ],
        "standard": ("Finish when a percentile read from a histogram is reported as an interval without being asked.",
                     "You should be able to locate a rank in cumulative bucket counts, "
                     "name the containing bucket with both ends, compute the relative "
                     "width `r − 1`, say how many buckets a finer ratio costs over the "
                     "same range, and explain why neither number moves when the traffic "
                     "does."),
        "note": "Both aggregates so far were computed from requests that were actually "
                "served. The next two pages are about requests that were not: "
                "&ldquo;Coordinated Omission&rdquo; puts back the ones a stalled load "
                "generator never sent, which moves a p99 from 2 ms to 990 ms on one "
                "trace, and &ldquo;Scrape Intervals and What They Cannot See&rdquo; "
                "counts the spikes that happened between two reads.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "coordinated-omission",
        "title": "Coordinated Omission",
        "module": "Biases a measurement adds",
        "one_line": "Compute the naive and the corrected percentile from one trace with a stall, and say which arrival model each one assumes.",
        "summary": (
            "A closed-loop load generator sends its next request when the last one "
            "comes back, so while the system is stalled it sends nothing and the stall "
            "is recorded once instead of once per request it delayed. Putting back the "
            "requests the schedule called for, each waiting from the moment it was due, "
            "moves the p99 of one trace from 2 ms to 990 ms &mdash; a factor of 495 "
            "&mdash; without measuring anything new."
        ),
        "key": [
            "closed loop: the next request goes out when the last one returns",
            "a 1 000 ms stall on a 10 ms schedule hides 99 requests",
            "naive p99 = 2 ms        corrected p99 = 990 ms        ×495",
            "the k-th missing request waited  stall − k·interval",
            "the correction adds no measurement: one stall, charged to all it delayed",
        ],
        "key_label": "One stall, measured once or measured properly",
        "concepts_intro": (
            "The bias is in the generator, not in the system, and it is invisible in "
            "the output because the numbers it reports are all true."
        ),
        "concepts": [
            ("A closed loop stops generating exactly when the system stops responding",
             "Send a request, wait for the reply, send the next. It is the obvious way "
             "to write a load generator and it has a built-in feedback: the slower the "
             "system, the less load it receives. During a one-second stall a loop "
             "scheduled at 10 ms apart issues no requests at all, so instead of a "
             "hundred slow requests the trace contains one, and the other ninety-nine "
             "are simply absent from the sample."),
            ("Real arrivals do not wait for you to be ready",
             "Users, upstream services and message queues keep arriving during a stall. "
             "The requests the closed loop did not send are requests that would have "
             "existed, and each would have waited from the moment it was due until the "
             "stall cleared. That is what the correction restores: not an invented "
             "distribution, but the schedule the generator itself was configured with."),
            ("The correction changes the sample, never a measurement",
             "Every latency the generator recorded stays exactly as recorded. What is "
             "added is one entry per request the schedule called for during the stall, "
             "at the wait that request would have experienced. The percentile is then "
             "the same nearest-rank rule applied to a larger sample &mdash; the "
             "disagreement between 2 ms and 990 ms is a disagreement about which "
             "requests existed, not about what a percentile is."),
        ],
        "read_title": "The requests that were never sent, and where they belong in the sample",
        "read_intro": (
            "Why a stall appears once in a closed-loop trace, what the imputed "
            "latencies are, and the arrival model each of the two answers assumes."
        ),
        "body": [
            ("def", ("Coordinated omission",
                     "<strong>Coordinated omission</strong> is the bias in which a "
                     "measurement process suspends its own sampling during the events "
                     "it exists to measure. In a closed-loop load generator, the next "
                     "request is issued only after the previous reply, so a stall of "
                     "duration `S` on a schedule of one request every `I` suppresses "
                     "about `S/I` requests &mdash; and every one of them would have "
                     "been slow.")),
            ("p", "The name says the important part: the omission is "
                  "<em>coordinated</em> with the fault. Requests are not dropped at "
                  "random from the sample, which would be harmless; they are dropped "
                  "precisely when the system is behaving worst, which is where the "
                  "percentile you are reporting lives."),
            ("p", "Consider a generator configured to send one request every 10 ms with "
                  "a healthy service time of 2 ms. It sends a hundred requests and "
                  "during one of them the service stalls for a full second. The trace "
                  "it produces is ninety-nine requests at 2 ms and one at 1 000 ms."),
            ("math", [
                "trace as recorded          99 × 2 ms      1 × 1 000 ms      n = 100",
                "",
                "naive p99   rank ⌈0.99×100⌉ = 99 of 100   →   2 ms",
                "",
                "schedule during the stall: one request due every 10 ms",
                "  requests due inside 1 000 ms, not sent:   99",
                "  the k-th of them was due at k·10 ms into the stall and",
                "  waited until the stall cleared:           1 000 − 10k ms",
                "  k = 1 → 990 ms    k = 50 → 500 ms    k = 99 → 10 ms",
                "",
                "corrected sample   99 × 2 ms   +   990, 980, …, 10   +   1 × 1 000 ms",
                "                   n = 199",
                "",
                "corrected p99   rank ⌈0.99×199⌉ = 198 of 199   →   990 ms",
                "",
                "990 ÷ 2 = 495",
            ]),
            ("p", "The naive p99 is 2 ms, which is the healthy service time. That is "
                  "not a coincidence and it is the signature of the bug: with one slow "
                  "request in a hundred, rank 99 never reaches it, so the reported "
                  "99th percentile is a measurement of the system when nothing was "
                  "wrong. A report of &ldquo;p99 = 2 ms&rdquo; on a run that contained "
                  "a one-second outage is arithmetically correct and completely "
                  "uninformative."),
            ("p", "The median moves too, and the direction is worth noticing: 2 ms "
                  "naive against 10 ms corrected. A bias that is usually described as a "
                  "tail problem reaches the middle of the distribution as soon as the "
                  "stall is long relative to the schedule."),
            ("thm", ("What the correction assumes",
                     "Imputing the missing requests at their scheduled times is exactly "
                     "right when arrivals are <strong>open</strong>: generated by a "
                     "process indifferent to how long the system is taking. It is "
                     "exactly wrong when arrivals are genuinely "
                     "<strong>closed</strong> &mdash; a fixed population of clients that "
                     "each wait for their own reply before acting again, such as a "
                     "bounded thread pool or a human at a terminal.",
                     "In the closed case the requests really were not made, the users "
                     "really did wait once, and the naive number is what happened. "
                     "Applying the correction there double-counts. Deciding which model "
                     "your workload follows is a modelling judgement the arithmetic "
                     "cannot make for you, and it is the assumption this page rests on.")),
            ("h3", "Why more threads is not the fix"),
            ("p", "The usual first reaction is to raise the generator&rsquo;s "
                  "concurrency: a hundred threads instead of one, so a stall blocks only "
                  "one of them. It moves the number and it does not remove the bias. "
                  "Each thread is still a closed loop, each still stops issuing during "
                  "a stall, and a fault that affects the whole service stalls all of "
                  "them at once &mdash; which is the case you are trying to measure. "
                  "What removes the bias is generating requests on a clock rather than "
                  "on replies, and recording each request&rsquo;s latency from its "
                  "<em>scheduled</em> start rather than from when a thread got round to "
                  "sending it."),
            ("example", ("Two generators, one service, one stall",
                         "A clock-driven generator issues a request every 10 ms whether "
                         "or not the last one returned, and timestamps each from its due "
                         "time. Through the same one-second stall it records a hundred "
                         "slow requests with waits from 1 000 ms down to 10 ms, and its "
                         "p99 is 990 ms with no correction applied at all.",
                         "The closed-loop generator records one. The corrected sample "
                         "above is an after-the-fact reconstruction of what the "
                         "clock-driven generator would have seen, which is why it lands "
                         "on the same number: the correction is not a heuristic, it is "
                         "the missing half of the experiment.")),
            ("h3", "The same bias outside load testing"),
            ("p", "A monitoring agent that scrapes its own metrics and blocks while the "
                  "process is stalled omits exactly the samples that matter. So does a "
                  "client library that records latency only for requests that completed "
                  "and drops the ones the user abandoned, and so does any dashboard "
                  "whose denominator quietly excludes timeouts. In each case the "
                  "sample is missing the events the measurement exists to detect, and "
                  "in each case the reported number is a true statement about a sample "
                  "nobody wanted."),
            ("p", "The check is one question: could this measurement have been "
                  "prevented from being taken by the very fault it is supposed to "
                  "record? If yes, the number is biased in a direction that flatters, "
                  "and the size of the bias is what the lab computes."),
        ],
        "lab": ("measure", {
            "mode": "omission",
            "panel_title": "Set the schedule and the stall",
            "panel_intro": (
                "The naive column is what the generator recorded and the corrected "
                "column is that same recording plus the requests the schedule called "
                "for while it was blocked. Both columns are nearest rank on their own "
                "sample. Shrink the stall below one scheduled interval and watch the "
                "two columns become the same number &mdash; with no requests due inside "
                "the stall, there is nothing to put back."
            ),
        }),
        "steps_title": "Correcting a trace for the requests it does not contain",
        "steps_intro": (
            "Before any arithmetic, decide whether the correction applies at all. Steps "
            "two to four are mechanical once it does."
        ),
        "steps": [
            ("Decide whether your arrivals are open or closed",
             "Open means the request rate is set by something outside the system "
             "&mdash; users, a queue, a cron fleet &mdash; and does not slow down when "
             "the system does. Closed means a fixed population each waiting on its own "
             "reply. The correction belongs to the open case only, and applying it to a "
             "closed workload overstates the tail."),
            ("Find the intended schedule",
             "One request every `I`, or whatever rate the generator was configured for. "
             "This is the piece of information that makes the correction possible: it "
             "is not inferred from the trace, it is what you told the generator to do."),
            ("Count the requests due inside each stall, and give each its wait",
             "A stall of `S` starting when a request was due suppresses `⌈S/I⌉ − 1` "
             "later requests. The `k`-th is due `k·I` into the stall and waits `S − k·I` "
             "until it clears. Add those latencies to the sample; change nothing that "
             "was measured."),
            ("Recompute the percentile on the enlarged sample",
             "Same nearest-rank rule, larger `n`, so the rank moves too. Report both "
             "numbers and the ratio, because the ratio is the finding: a factor of 495 "
             "is a statement about the measurement apparatus that the corrected number "
             "alone does not convey."),
        ],
        "worked": {
            "title": "A hundred requests, a one-second stall, and a p99 of 2 ms",
            "intro": [
                "The trace is the lab&rsquo;s preset: a generator issuing one request "
                "every 10 ms against a service that normally answers in 2 ms, through "
                "a single stall of one second. Every number below comes from that one "
                "trace and the schedule it was generated from.",
            ],
            "lines": [
                "configured    one request every I = 10 ms      healthy service 2 ms",
                "observed      99 requests at 2 ms, 1 request at 1 000 ms      n = 100",
                "",
                "AS MEASURED",
                "  p50   rank ⌈0.50×100⌉ = 50  →    2 ms",
                "  p99   rank ⌈0.99×100⌉ = 99  →    2 ms",
                "  p100                        → 1 000 ms",
                "",
                "WHAT THE SCHEDULE CALLED FOR",
                "  requests due during the 1 000 ms stall, never sent:   99",
                "  the k-th was due at 10k ms in, and waited 1 000 − 10k ms",
                "      k = 1   →  990 ms",
                "      k = 2   →  980 ms",
                "      …",
                "      k = 99  →   10 ms",
                "",
                "CORRECTED SAMPLE          n = 100 + 99 = 199",
                "  99 × 2 ms   +   {10, 20, …, 990}   +   1 × 1 000 ms",
                "",
                "  sorted:  positions   1– 99   =  2 ms",
                "           positions 100–198   =  10, 20, …, 990 ms",
                "           position      199   =  1 000 ms",
                "",
                "  p50   rank ⌈0.50×199⌉ = 100  →   10 ms",
                "  p99   rank ⌈0.99×199⌉ = 198  →  990 ms",
                "",
                "  990 ÷ 2 = 495",
            ],
            "after": [
                "Nothing in the corrected sample was measured twice and nothing was "
                "invented. The ninety-nine added entries are the schedule, and the "
                "schedule was an input to the experiment. If you object to them you are "
                "objecting to the configured request rate, not to the arithmetic.",
                "The factor of 495 is not a general constant. It is `S/I` scaled by "
                "where the ranks land: lengthen the stall and it grows, shorten the "
                "scheduled interval and it grows, and take the stall below one interval "
                "and it collapses to 1 because no request was due inside it. The lab "
                "lets you find the point where the two columns separate.",
                "For faded practice, set the stall to 200 ms and the interval to 50 ms "
                "on the same hundred requests. The supplied first move is that three "
                "requests were due inside the stall, at 150, 100 and 50 ms of waiting. "
                "Predict both the naive and the corrected p99 before you touch the "
                "sliders, then check, and say in one sentence why this trace is so much "
                "less alarming than the first.",
            ],
        },
        "quiz_title": "Stalls, schedules and the sample",
        "quiz": [
            {"q": "A closed-loop generator sends one request every 10 ms, the service stalls for 1 000 ms, and the trace of 100 requests shows a p99 of 2 ms. Why is 2 ms the reported p99?",
             "a": ["Because the stalled request was excluded as an outlier",
                   "Because with one slow request in a hundred, rank 99 of 100 does not reach it &mdash; so the p99 measures the healthy service",
                   "Because the generator averages the latencies within each window",
                   "Because 1 000 ms exceeds the generator's timeout"],
             "c": 1,
             "why": "Nearest rank at `⌈0.99 × 100⌉` is position 99, and the single slow "
                    "request is position 100. The reported 99th percentile is therefore a "
                    "measurement of the service when it was working. Nothing was excluded "
                    "or averaged &mdash; the arithmetic is right and the sample is wrong."},
            {"q": "On that same trace, how many requests did the schedule call for during the stall, and what did the first of them wait?",
             "a": ["99 requests; the first waited 990 ms", "100 requests; the first waited 1 000 ms",
                   "99 requests; the first waited 10 ms", "1 request; it waited 1 000 ms"],
             "c": 0,
             "why": "A 1 000 ms stall on a 10 ms schedule has 99 later requests due inside "
                    "it. The `k`-th is due `10k` ms in and waits `1 000 − 10k`, so the "
                    "first waits 990 ms and the ninety-ninth waits 10 ms. The 100-request "
                    "answer double-counts the request that was actually sent and recorded "
                    "at 1 000 ms."},
            {"q": "A team raises their load generator from one thread to two hundred so that a stall blocks only one of them. Does this remove coordinated omission?",
             "a": ["Yes &mdash; with enough threads, some are always issuing requests",
                   "Yes, provided the thread count exceeds the concurrency of the system under test",
                   "No &mdash; each thread is still a closed loop, and a service-wide stall blocks all of them at once",
                   "No, because more threads increase the load and change the result"],
             "c": 2,
             "why": "Concurrency reduces the bias for faults that affect one connection "
                    "and does nothing for faults that affect the service, which is the "
                    "case being measured. The fix is to issue requests on a clock and to "
                    "time each from its scheduled start rather than from when a thread "
                    "was free."},
            {"q": "A workload consists of exactly 50 batch clients, each of which submits a job, waits for the result, and then submits the next. The service stalls. Should the naive percentile be corrected?",
             "a": ["Yes &mdash; the correction applies to any stall",
                   "No &mdash; these arrivals are genuinely closed, so the suppressed requests never existed and correcting double-counts",
                   "Yes, but only for the slowest client",
                   "No, because 50 clients is too few to compute a percentile"],
             "c": 1,
             "why": "The correction reconstructs requests an <em>open</em> arrival process "
                    "would have generated. Here the clients themselves wait, so no request "
                    "was suppressed and the naive figure is what happened. Deciding open "
                    "against closed is a judgement about the workload, and it is the "
                    "assumption the correction rests on."},
        ],
        "mistakes": [
            ("Believing the generator saw what users would have seen",
             "It saw what a client that politely stops sending during an outage would "
             "have seen, which is nobody. The tell is a reported percentile equal to "
             "the healthy service time on a run that contained a visible stall: if the "
             "p99 and the median are the same number and the maximum is three orders of "
             "magnitude away, the sample is missing the requests that were due while "
             "the maximum was happening."),
            ("Fixing it by adding threads or by discarding the outlier",
             "Both make the number prettier. Threads spread the omission across more "
             "loops without removing it, and dropping the single slow request removes "
             "the only surviving evidence that the stall occurred. The measurement "
             "problem is that ninety-nine slow requests are missing, and neither move "
             "puts one back."),
            ("Applying the correction to a genuinely closed workload",
             "A fixed pool of clients that each wait really did experience one delay "
             "each, and imputing extra arrivals on top invents load that could not have "
             "existed. The correction is a model of open arrivals, it is stated as one, "
             "and reporting a corrected percentile without saying which arrival model "
             "it assumes is the same failure in the other direction."),
        ],
        "standard": ("Finish when “could this fault have suppressed its own measurement?” is a question you ask of every measurement.",
                     "You should be able to recognise a closed-loop trace from its "
                     "percentiles, count the requests a stall suppressed from the "
                     "schedule, give each its imputed wait, recompute the percentile on "
                     "the enlarged sample, and state whether the workload being "
                     "measured is open or closed."),
        "note": "The stall in that trace was at least recorded once. A metrics pipeline "
                "has a second way of not seeing an event, which is that nothing was "
                "sampled while it was happening at all: &ldquo;Scrape Intervals and "
                "What They Cannot See&rdquo; computes the probability that a spike "
                "lands between two reads, and names the longest spike that can hide "
                "entirely.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "scrape-intervals",
        "title": "Scrape Intervals and What They Cannot See",
        "module": "Biases a measurement adds",
        "one_line": "Compute the probability a spike of a given duration is caught at a given scrape interval, and the longest spike that can hide entirely.",
        "summary": (
            "A gauge read every `I` seconds is a sample of the signal at `I`-second "
            "instants, and a spike of duration `d` is caught only if a read falls "
            "inside it: probability `min(1, d/I)`. At the common fifteen-second "
            "interval a three-second spike is seen one time in five, and a spike of up "
            "to fourteen seconds can hide completely. The same interval hides a second "
            "thing entirely &mdash; a counter that restarted, whose only evidence is "
            "that the number went down."
        ),
        "key": [
            "P(catch a spike of length d) = min(1, d/I)     d = 3, I = 15 → 1/5",
            "longest spike that can hide entirely = I − 1 s      I = 15 → 14 s",
            "a flat graph is evidence about the reads, not about the system",
            "counter reset  reads 6 000 → 520 over 15 s",
            "naive rate (520 − 6 000)/15 = −365.33/s     corrected 520/15 = +34.67/s",
            "and 80 increments between the last read and the restart are unrecoverable",
        ],
        "key_label": "What falls between two reads",
        "concepts_intro": (
            "A monitoring interval is a sampling rate, and sampling rates have "
            "consequences that are arithmetic rather than opinion."
        ),
        "concepts": [
            ("A scrape is a sample of an instant, not a summary of an interval",
             "A gauge read at `t` reports the value at `t`. Whatever the signal did "
             "between `t − I` and `t` is not averaged, not maximised and not recorded "
             "&mdash; it is absent. Two reads fifteen seconds apart both showing a "
             "quiet system are two facts about two instants, and the graph drawn "
             "between them is a line your plotting library invented."),
            ("A spike is caught only if a read lands inside it",
             "Reads are `I` apart, so a spike shorter than `I` can contain at most one "
             "of them, and whether it contains one depends on where it starts. With the "
             "start uniform relative to the scrape clock, the chance is the fraction of "
             "the cycle the spike occupies: `d/I`, capped at one when `d ≥ I`. Three "
             "seconds in fifteen is exactly `1/5`."),
            ("A counter that went down is the only trace of a restart",
             "Counters are read as differences, so a process restart that zeroes one "
             "turns the next difference into a large negative rate &mdash; or, if the "
             "counter has already climbed past the previous read, into a small positive "
             "one that looks like a quiet spell. The fix is to treat any decrease as a "
             "restart and take the new reading as the increment, which recovers the "
             "rate and loses whatever accumulated between the last read and the restart."),
        ],
        "read_title": "The catch probability, the invisible spike, and the counter that went backwards",
        "read_intro": (
            "Where `min(1, d/I)` comes from and what it assumes, what a run of spikes "
            "actually does, and the second thing an interval hides."
        ),
        "body": [
            ("def", ("Scrape interval",
                     "The <strong>scrape interval</strong> `I` is the period at which a "
                     "monitoring system reads a target&rsquo;s current metric values. "
                     "For a gauge, the value recorded is the one in effect at the "
                     "instant of the read. For a counter, what is stored is the running "
                     "total, and a <strong>rate</strong> is computed as the difference "
                     "between two reads divided by the time between them.")),
            ("thm", ("The probability of catching a spike",
                     "Let a spike of duration `d` begin at a time uniformly distributed "
                     "relative to the scrape clock, and let reads occur every `I`. If "
                     "`d ≥ I` at least one read falls inside the spike and it is caught "
                     "with certainty. If `d &lt; I` the spike covers a fraction `d/I` of "
                     "the scrape cycle, so",
                     "`P(caught) = min(1, d/I)`.",
                     "The assumption is the uniformity. It fails exactly when the spike "
                     "is produced by something on a clock of its own &mdash; a cron job, "
                     "a flush every sixty seconds, or the scrape itself &mdash; in which "
                     "case the phase is fixed and the probability is not `d/I` but zero "
                     "or one, permanently.")),
            ("p", "That failure mode is worth more than the formula. A spike that is "
                  "always missed is indistinguishable from no spike, and a periodic job "
                  "whose period shares a factor with the scrape interval produces "
                  "exactly that. If a graph is suspiciously flat, changing the interval "
                  "to a value coprime with your suspicions is a cheap experiment."),
            ("math", [
                "I = 15 s,  d = 3 s",
                "",
                "P(caught) = 3/15 = 1/5 = 20%",
                "so four spikes in five leave no trace at all",
                "",
                "longest spike that can fall entirely between two reads:",
                "  a spike of d seconds contains a read unless it fits strictly",
                "  inside one gap, which needs d ≤ I − 1 at one-second resolution",
                "",
                "  I = 15 s  →  14 s",
                "  I = 60 s  →  59 s",
                "  I =  1 s  →   0 s      nothing can hide",
            ]),
            ("p", "Fourteen seconds is the figure to carry away. At the default "
                  "fifteen-second interval that most monitoring is configured with, an "
                  "outage lasting a quarter of a minute can leave a completely flat "
                  "graph, and the graph is not lying: it is reporting every value it "
                  "was given."),
            ("h3", "One run is not the probability"),
            ("p", "The lab draws a run of spikes at seeded times across five minutes "
                  "and lays the scrape instants over them. At `d = 3` and `I = 15` the "
                  "expected fraction caught is a fifth, and the fraction actually caught "
                  "on a given run is some other number near it &mdash; which is what a "
                  "single afternoon of monitoring is. Reseed and it changes; the "
                  "probability does not."),
            ("p", "This is the same distinction the first page of the course made about "
                  "a measured ratio, arriving in a different costume. `1/5` is a "
                  "property of the configuration; &ldquo;we caught three of twelve "
                  "yesterday&rdquo; is a measurement with its own error bar, and "
                  "twelve spikes is a very small sample."),
            ("example", ("A quarter-minute outage that nothing recorded",
                         "A service fails hard for twelve seconds and recovers. The "
                         "scrape interval is fifteen seconds; the outage happens to "
                         "start two seconds after a read and end one second before the "
                         "next. Error-rate gauges read zero on both sides. The request "
                         "counter, being cumulative, does carry the missing successes "
                         "&mdash; a dip in the computed rate that is real and easy to "
                         "dismiss &mdash; but every gauge-based panel and every alert "
                         "built on one saw a healthy system throughout. Users saw "
                         "twelve seconds of errors.")),
            ("h3", "The second thing the interval hides: a counter that reset"),
            ("p", "Counters only go up, so monitoring systems compute rates by "
                  "differencing consecutive reads. A process restart sets the counter "
                  "back to zero, and the restart itself happens between two reads where "
                  "nothing can observe it. The only evidence is that the second read is "
                  "smaller than the first, and a naive difference turns that into a "
                  "spectacular negative rate."),
            ("math", [
                "a counter climbing at 40/s, read every 15 s, process restarts at 152 s",
                "",
                "read at 150 s     40 × 150            =  6 000",
                "read at 165 s     40 × (165 − 152)    =    520",
                "",
                "naive rate        (520 − 6 000)/15    =  −365.33/s",
                "corrected         a decrease means a restart, so take the new read:",
                "                  520/15              =   +34.67/s",
                "",
                "true rate                                  40.00/s",
                "unrecoverable     40 × (152 − 150)    =     80 increments",
            ]),
            ("p", "The corrected rate is 34.67 rather than 40 and the gap is exactly "
                  "the eighty increments that accumulated between the last read and the "
                  "restart. They are gone: the process that held them no longer exists, "
                  "and no correction applied downstream can recover a number nobody "
                  "read. What the correction buys is a rate that is positive, "
                  "approximately right, and does not poison every aggregate it feeds."),
            ("p", "Notice how the error behaves if the restart happens earlier in the "
                  "window. Once the counter has climbed past its previous reading before "
                  "the next scrape, the difference is positive again and nothing looks "
                  "wrong at all &mdash; the restart is then completely invisible, and "
                  "the rate it reports is understated by however much was lost. The "
                  "large negative number is the friendly case."),
        ],
        "lab": ("measure", {
            "mode": "scrape",
            "panel_title": "Set the interval and the spike",
            "panel_intro": (
                "`min(1, d/I)` is an exact comparison, not a rounding, and the longest "
                "invisible spike follows from the same two numbers. The run of spikes "
                "below it is one seeded draw, so the fraction it catches sits near the "
                "probability rather than on it. The second table restarts a counter "
                "mid-window and shows the naive rate, the corrected rate, and the "
                "increments neither of them can recover."
            ),
        }),
        "steps_title": "Sizing an interval against the thing you need to see",
        "steps_intro": (
            "Start from the event, not from the default. The interval is a consequence "
            "of what you are willing to miss."
        ),
        "steps": [
            ("Name the shortest event you need to detect",
             "Ten seconds of elevated errors, a two-second pause, a thirty-second "
             "queue build-up. Until this is a number, no interval can be defended, and "
             "the default of fifteen seconds is a decision somebody else made about "
             "your system."),
            ("Compute min(1, d/I) at the interval you have",
             "If it is well below one, you are sampling the event rather than "
             "observing it, and the graph will be quiet most of the times it happens. "
             "Compute `I − 1` as well: that is the longest such event that can leave no "
             "trace at all."),
            ("Prefer a counter to a gauge for anything you must not miss",
             "A counter accumulates between reads, so a burst of errors during a gap "
             "still shows up in the next difference. A gauge samples an instant and a "
             "burst between two instants is gone. Where you must use a gauge, a "
             "max-since-last-scrape or a histogram of the interval turns it back into "
             "something cumulative."),
            ("Decide what a decrease means before you see one",
             "Any rate computation over a counter needs a restart rule. Treat a "
             "decrease as a restart and use the new reading as the increment; record "
             "that the correction discards whatever accumulated since the previous "
             "read, and do not let a negative rate reach an average, a percentile or an "
             "alert threshold."),
            ("Re-check the phase assumption for anything periodic",
             "If the event you are hunting is produced by a scheduled job, `d/I` does "
             "not apply: the phase is fixed rather than uniform, and you will either "
             "always see it or never see it. Change the interval to something coprime "
             "with the job&rsquo;s period and compare."),
        ],
        "worked": {
            "title": "Fifteen seconds, a three-second spike, and a counter that restarted",
            "intro": [
                "Two independent calculations at the same interval. The first is the "
                "probability arithmetic, which is exact and needs no data. The second "
                "is a single restart, which needs two counter reads and a rule.",
            ],
            "lines": [
                "PART ONE — THE SPIKE",
                "",
                "  I = 15 s,   d = 3 s",
                "",
                "  P(caught) = min(1, d/I) = 3/15 = 1/5 = 20%",
                "  P(missed)                       = 4/5 = 80%",
                "",
                "  longest spike that can hide entirely   = I − 1 = 14 s",
                "",
                "  twelve such spikes in five minutes:",
                "    expected caught  12 × 1/5 = 2.4",
                "    a seeded run catches some integer near 2.4, not 2.4",
                "",
                "  drop the interval to 5 s:   P = 3/5 = 60%,  invisible ≤ 4 s",
                "  drop the interval to 1 s:   P = 1,           invisible ≤ 0 s",
                "",
                "PART TWO — THE COUNTER",
                "",
                "  counter climbing at 40/s, read every 15 s, restart at t = 152 s",
                "",
                "    t = 150 s     value 40 × 150         = 6 000",
                "    t = 165 s     value 40 × (165 − 152) =   520",
                "",
                "  naive      (520 − 6 000) / 15 = −5 480/15 = −365.33/s",
                "  corrected  decrease ⇒ restart ⇒ 520/15    =  +34.67/s",
                "  true                                        40.00/s",
                "",
                "  lost   40 × (152 − 150) = 80 increments, unrecoverable",
            ],
            "after": [
                "Part one is a statement about the configuration and part two is a "
                "statement about one event, and they share a cause: everything that "
                "happens strictly between two reads is invisible, and only its "
                "aftermath is available for inference.",
                "The 34.67 is worth dwelling on. It is not the true rate, it is not a "
                "rounding of the true rate, and the difference from 40 is a known "
                "quantity &mdash; eighty increments over fifteen seconds is 5.33/s, and "
                "`34.67 + 5.33 = 40`. A correction whose residual you can name is a "
                "much better thing to ship than one you cannot.",
                "For faded practice, set the interval to 10 s and the spike to 4 s, and "
                "move the restart to 96 s. The supplied first move is that the catch "
                "probability becomes `2/5` and the longest invisible spike becomes 9 s. "
                "Predict the two counter reads around the restart and both rates before "
                "you look, then check, and say which of the two panels changed more "
                "when you halved the interval.",
            ],
        },
        "quiz_title": "Intervals, spikes and resets",
        "quiz": [
            {"q": "A monitoring system scrapes every 15 seconds. What is the probability that a 3-second spike is caught, and what is the longest spike that can leave no trace at all?",
             "a": ["`1/5` and 15 s", "`1/5` and 14 s", "`1/15` and 14 s", "`3/5` and 12 s"],
             "c": 1,
             "why": "`min(1, d/I) = 3/15 = 1/5`, and a spike must fit strictly inside a "
                    "gap to avoid every read, which at one-second resolution means "
                    "`I − 1 = 14` s. A 15-second spike always contains a read, so 15 is "
                    "wrong by exactly the case that makes the bound tight."},
            {"q": "An alert built on a gauge did not fire during a 12-second outage at a 15-second scrape interval. What does that tell you about the system?",
             "a": ["That the outage did not affect the metric being gauged",
                   "Nothing &mdash; a 12-second event can fall entirely between two reads",
                   "That the alert threshold is set too high",
                   "That the outage was shorter than reported"],
             "c": 1,
             "why": "A flat graph is evidence about the reads, not about the system: at "
                    "`I = 15` anything up to 14 seconds can hide completely. Investigating "
                    "the threshold or the metric first is how a sampling problem gets "
                    "diagnosed as an alerting problem."},
            {"q": "A counter climbing at 40/s is read as 6 000 at t = 150 s and as 520 at t = 165 s, because the process restarted at t = 152 s. What do the naive and corrected rates report?",
             "a": ["−365.33/s and +34.67/s", "−365.33/s and +40.00/s", "+34.67/s and +40.00/s", "0/s and +34.67/s"],
             "c": 0,
             "why": "Naive is `(520 − 6 000)/15 = −365.33/s`. Treating the decrease as a "
                    "restart takes the new reading as the increment: `520/15 = 34.67/s`. "
                    "It is not 40, because the 80 increments between the last read and the "
                    "restart were never read by anyone and cannot be recovered."},
            {"q": "A job runs every 60 seconds and causes a 3-second spike. Your scrape interval is 15 seconds. What does `min(1, d/I) = 1/5` tell you here?",
             "a": ["That you will catch about one spike in five",
                   "That you will catch about one spike in four, since 60/15 = 4",
                   "Very little &mdash; the spike's phase relative to the scrape clock is fixed, not uniform, so you will catch either all of them or none",
                   "That the interval should be set to 60 seconds to match"],
             "c": 2,
             "why": "The formula assumes the spike start is uniform relative to the scrape "
                    "clock. A periodic cause whose period is a multiple of the interval "
                    "has a fixed phase, so the outcome is the same every cycle: always "
                    "caught or never caught. This is the assumption on which the whole "
                    "page rests, and it is the one that fails in practice."},
        ],
        "mistakes": [
            ("Reading a flat graph as a quiet system",
             "The graph shows what was sampled. At a fifteen-second interval it is "
             "consistent with fourteen seconds of total failure, repeatedly, and with "
             "a three-second spike on four out of every five occurrences. Before "
             "concluding that nothing happened, compute `d/I` for the shortest event "
             "you would have wanted to see."),
            ("Assuming a shorter interval solves it",
             "It raises `d/I` and it never reaches certainty while `d &lt; I`; going "
             "from fifteen seconds to five turns a one-in-five chance into three in "
             "five, which is better and is not detection. It also multiplies the "
             "samples per series, which is a direct storage cost computed in "
             "&ldquo;Metric Cardinality&rdquo;. The structural answer is a cumulative "
             "metric, not a faster gauge."),
            ("Letting a negative rate through",
             "A restart produces one enormous negative rate, and if it reaches an "
             "average it drags a whole dashboard down, while a percentile over rates "
             "will place it at the bottom and quietly shift every rank. Decide the "
             "restart rule up front, apply it where the difference is taken, and never "
             "let the raw difference reach an aggregate."),
        ],
        "standard": ("Finish when an interval is chosen from the shortest event you must see, rather than inherited from a default.",
                     "You should be able to compute `min(1, d/I)` and `I − 1` for any "
                     "interval, say what a flat graph is and is not evidence of, state "
                     "when the uniform-phase assumption fails, and turn two counter "
                     "reads across a restart into a naive rate, a corrected rate and "
                     "the increments that are gone."),
        "note": "Scraping every instant is one way of not seeing an event; sampling one "
                "request in a hundred is another, and it has the more surprising "
                "arithmetic. &ldquo;Sampling and Rare Events&rdquo; computes the chance "
                "that one per cent sampling catches a ten-request problem &mdash; it is "
                "9.56%, not one per cent &mdash; and the rate it would actually take, "
                "which is twenty-six times higher rather than ten.",
    },
]
