"""Course 4, lessons 01-05 - the miss rate, the tail, the skew, the size, the policy."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "hit-rate-and-backend-load",
        "title": "Hit Rate and Backend Load",
        "module": "The miss rate",
        "one_line": "Turn a hit rate into the requests per second the backend still receives, and into the utilisation that leaves it at.",
        "summary": (
            "A cache is described by its hit rate and judged by its miss rate. The "
            "backend never sees `h`; it sees `1 − h`, multiplied by the arrival rate. "
            "So the interesting number is the one nobody quotes, and moving a cache "
            "from ninety to ninety-nine per cent is a tenfold cut in what arrives "
            "rather than a nine-point improvement."
        ),
        "key": [
            "backend load = (1 − h)·λ        the cache absorbs hλ; the backend sees the rest",
            "",
            "λ = 10 000 rps,  μ = 2 000 rps",
            "h = 90%    1 − h = 1/10    →  1 000 rps    ρ = 1/2",
            "h = 95%    1 − h = 1/20    →    500 rps    ρ = 1/4     half the load",
            "h = 99%    1 − h = 1/100   →    100 rps    ρ = 1/20    a tenth of it",
        ],
        "key_label": "The hit rate, converted into the number the backend sees",
        "concepts_intro": (
            "One multiplication, and two habits of reading it. The multiplication is "
            "easy; the habits are what make the answer feel wrong the first time."
        ),
        "concepts": [
            ("The backend is a function of `1 − h`",
             "Requests arrive at `λ`. A fraction `h` is served from the cache and never "
             "leaves it; the rest, `(1 − h)λ`, is forwarded. At `λ = 10 000` requests a "
             "second and `h = 90%` the cache absorbs `9 000` and the backend receives "
             "`1 000`. Every sentence about the backend &mdash; its load, its "
             "utilisation, its wait, its bill &mdash; is a sentence about `1 − h`."),
            ("A gain in `h` is a ratio of miss rates, not a difference",
             "From `90%` to `95%` the miss rate goes `1/10 → 1/20`, so the backend load "
             "is <strong>halved</strong>. From `90%` to `99%` it goes `1/10 → 1/100`, so "
             "the load is <strong>divided by ten</strong>. Five points and nine points "
             "look comparable written down and are not: what matters is the ratio of the "
             "two small numbers, not the gap between the two large ones."),
            ("What moved is the backend’s `ρ`",
             "Backend load divided by backend capacity is the utilisation of Queues and "
             "Utilisation. At `μ = 2 000` requests a second, `1 000` in means `ρ = 1/2` "
             "and `100` in means `ρ = 1/20`. A cache is a utilisation control, and the "
             "wait it buys is not proportional to the load it removes."),
        ],
        "read_title": "The miss rate, the backend load, and the utilisation it leaves",
        "read_intro": "Why the same improvement reads as small on one side of the cache and enormous on the other.",
        "body": [
            ("def", ("Hit rate and miss rate",
                     "For a stream of requests arriving at rate `λ`, the "
                     "<strong>hit rate</strong> `h` is the fraction served from the "
                     "cache and the <strong>miss rate</strong> `1 − h` is the fraction "
                     "forwarded. The <strong>backend load</strong> is `(1 − h)λ`, in the "
                     "same units as `λ`.",
                     "The two rates are one number written two ways. Which one you write "
                     "down decides what the sentence is about: `h` is about the cache, "
                     "`1 − h` is about everything behind it.")),
            ("p", "There is no model in that definition and no assumption to argue "
                  "with. It is a split of a rate into two parts, and it is exact "
                  "whenever the hit rate is measured over the same window as the "
                  "arrival rate. What it is not is stable: `h` is a property of the "
                  "workload and the cache together, and a change in either moves it."),
            ("example", ("Ten thousand requests a second at a ninety per cent hit rate",
                         "`λ = 10 000` rps and `h = 90%`. The cache absorbs "
                         "`(9/10)(10 000) = 9 000` rps and the backend receives "
                         "`(1/10)(10 000) = 1 000` rps. Against a backend that can serve "
                         "`μ = 2 000` rps that is `ρ = 1 000/2 000 = 1/2`, so the backend "
                         "is busy half the time.")),
            ("h3", "One more nine is a factor, not a gain"),
            ("p", "Take the same `λ` and improve the cache. At `h = 95%` the backend "
                  "receives `(1/20)(10 000) = 500` rps: the hit rate went up by five "
                  "points and the backend&rsquo;s work <strong>halved</strong>. At "
                  "`h = 99%` it receives `100` rps, a tenth of what it received at "
                  "`90%`. Nothing about the backend improved by nine per cent."),
            ("math", [
                "backend at h₂     (1 − h₂)λ     1 − h₂",
                "───────────────  =  ─────────  =  ───────",
                "backend at h₁     (1 − h₁)λ     1 − h₁",
                "",
                "h₁ = 90%, h₂ = 95%     (1/20)/(1/10)  = 1/2      half the load",
                "h₁ = 90%, h₂ = 99%     (1/100)/(1/10) = 1/10     a tenth of the load",
            ]),
            ("p", "The `λ` cancels, which is why the factor is a property of the two "
                  "hit rates alone. It is also why the same percentage point is worth "
                  "wildly different amounts at different places on the scale: `50%` to "
                  "`51%` divides the backend load by `50/49`, about two per cent, while "
                  "`98%` to `99%` divides it by two."),
            ("example", ("The same cache, four ways",
                         "At `λ = 10 000` rps into a backend of `μ = 2 000` rps: "
                         "`h = 90%` leaves `1 000` rps and `ρ = 1/2`; `h = 95%` leaves "
                         "`500` rps and `ρ = 1/4`; `h = 99%` leaves `100` rps and "
                         "`ρ = 1/20`; `h = 99.9%` leaves `10` rps and `ρ = 1/200`. The "
                         "hit rates in that list are nearly the same number. The "
                         "utilisations differ by a factor of a hundred.")),
            ("h3", "The utilisation is the thing you were actually buying"),
            ("p", 'Backend load on its own does not tell you what the backend feels. '
                  '“The M/M/1 Queue” gives the mean wait at a rational utilisation as '
                  '`W = 1/(μ − λ)`, and on these four rows that is `1.00 ms`, `0.67 ms`, '
                  '`0.53 ms` and `0.50 ms`. Notice how little the last two moved: past '
                  'the knee, further hit rate buys almost nothing, because the queue was '
                  'already nearly empty. “The Knee: Response Time vs Utilisation” is the '
                  'curve that says which side of it you are on.'),
            ("p", "So a cache is worth the most exactly where the backend is worst. "
                  "Going from `ρ = 0.95` to `ρ = 0.5` is the difference between a "
                  "system that falls over and one that does not; going from `ρ = 0.05` "
                  "to `ρ = 0.005` is the difference between two numbers nobody can "
                  "feel. The hit rate is the lever and the utilisation is the load, and "
                  "it is the load you should be looking at."),
            ("p", "Two cautions before the lab. First, `(1 − h)λ` is the "
                  "<em>average</em> backend rate, and the backend&rsquo;s bad moments "
                  "are not averages &mdash; a hot key expiring sends a burst through "
                  "that this formula does not see, which is what Cache Stampedes is "
                  "for. Second, the hit rate is measured, not chosen: writing `99%` into "
                  "a capacity plan is a forecast about a workload, and it deserves the "
                  "error bar Capacity Estimation taught you to carry."),
        ],
        "lab": ("cache", {
            "mode": "hitrate",
            "view": "load",
            "lam": 10000,
            "hit_tenths": 900,
            "capacity": 2000,
        }),
        "steps_title": "Converting a hit rate into a backend number",
        "steps_intro": "Four lines, and the first one is the whole discipline: write down the miss rate before anything else.",
        "steps": [
            ("Write the miss rate, not the hit rate",
             "`h = 99%` becomes `1 − h = 1/100`. Do it as a fraction rather than a "
             "decimal: `1/100` invites you to compare it with `1/10`, and `0.01` "
             "invites you to compare it with `0.10`, which reads as a small difference."),
            ("Multiply by the arrival rate",
             "`(1 − h)λ` is the backend load in the units `λ` came in. Keep the units "
             "visible &mdash; requests per second, not just a number &mdash; because the "
             "next step divides it by a capacity that must be in the same units."),
            ("Divide by the backend’s capacity",
             "`ρ = (1 − h)λ/μ` is what the backend is actually running at. If `ρ ≥ 1` "
             "the cache has not saved it: the backlog grows without bound and there is "
             "no mean wait to quote."),
            ("Quote the change as a ratio",
             "Two hit rates give a factor `(1 − h₂)/(1 − h₁)`, and that factor is the "
             "honest way to report a cache improvement. &ldquo;We halved the database "
             "load&rdquo; is a claim someone can check; &ldquo;we improved the hit rate "
             "by five per cent&rdquo; is a claim about the wrong side of the cache."),
        ],
        "worked": {
            "title": "λ = 10 000 rps, μ = 2 000 rps: what one more nine buys",
            "intro": [
                "The arithmetic is one multiplication and one division. What is worth "
                "watching is how the four columns move at different speeds."
            ],
            "lines": [
                "λ = 10 000 rps arriving,  backend capacity μ = 2 000 rps",
                "",
                "  h        1 − h     backend (1 − h)λ      ρ = load/μ     W = 1/(μ − load)",
                "  90%       1/10        1 000 rps            1/2            1.00 ms",
                "  95%       1/20          500 rps            1/4            0.67 ms",
                "  99%       1/100         100 rps            1/20           0.53 ms",
                "  99.9%     1/1000         10 rps            1/200          0.50 ms",
                "",
                "90% → 95%    (1/20)/(1/10)  = 1/2      the backend does HALF the work",
                "90% → 99%    (1/100)/(1/10) = 1/10     the backend does a TENTH of it",
                "",
                "the hit rate moved by 9 points;  the backend load moved by a factor of 10",
            ],
            "after": [
                "Read the third column and the fifth column together. Between `90%` and "
                "`99%` the backend load falls by a factor of ten and the mean wait falls "
                "by about half: the load is linear in the miss rate and the wait is not. "
                "That is the whole reason to compute both.",
                "For a faded rehearsal, take `λ = 40 000` rps into a backend of "
                "`μ = 1 000` rps. The supplied first move is that the backend is "
                "overloaded at `h = 95%`: check that, then find the smallest hit rate in "
                "tenths of a per cent that puts `ρ` below `1/2`, and state the factor by "
                "which the load fell relative to `95%`. Run the lab at your answer "
                "before opening the quiz.",
                "The lab recomputes every row from `(1 − h)λ` as you move the sliders, "
                "and prints the backend&rsquo;s wait from the M/M/1 result of Queues and "
                "Utilisation beside it. Drag the hit rate from `90%` to `99%` and watch "
                "which of the four numbers actually moves.",
            ],
        },
        "quiz_title": "Miss rates and backend loads",
        "quiz": [
            {"q": "`λ = 10 000` rps and the hit rate improves from `90%` to `99%`. What happens to the backend&rsquo;s load?",
             "a": ["It falls from `1 000` rps to `910` rps",
                   "It falls from `1 000` rps to `100` rps",
                   "It falls from `1 000` rps to `900` rps",
                   "It is unchanged at `1 000` rps, because `λ` has not changed"],
             "c": 1,
             "why": "Backend load is `(1 − h)λ`: `(1/10)(10 000) = 1 000` rps becomes "
                    "`(1/100)(10 000) = 100` rps, a factor of ten. `910` is the load cut "
                    "by nine per cent and `900` is the load cut by nine hundred, both of "
                    "which read the nine points linearly. `λ` is indeed unchanged; the "
                    "fraction of it that reaches the backend is not."},
            {"q": "The backend can serve `μ = 2 000` rps and `λ = 10 000` rps arrive. Which hit rate leaves it at `ρ = 1/4`?",
             "a": ["`90%`", "`95%`", "`97.5%`", "`99%`"],
             "c": 1,
             "why": "`ρ = 1/4` means a load of `500` rps, so `(1 − h)(10 000) = 500` and "
                    "`1 − h = 1/20`, giving `h = 95%`. At `90%` the load is `1 000` and "
                    "`ρ = 1/2`; at `97.5%` the miss rate has halved again and `ρ = 1/8`; "
                    "at `99%` it is `ρ = 1/20`."},
            {"q": "A cache change takes the hit rate from `98%` to `99%`. By what factor does the backend&rsquo;s load change?",
             "a": ["It falls by about one per cent",
                   "It is halved",
                   "It falls by a factor of `98/99`",
                   "It falls by a factor of about `50`"],
             "c": 1,
             "why": "The miss rate goes from `1/50` to `1/100`, so the load is halved. "
                    "One percentage point at the top of the range is a factor of two; "
                    "the same point from `50%` to `51%` is a factor of `50/49`, which is "
                    "where &ldquo;about one per cent&rdquo; would have been right. "
                    "`98/99` is the ratio of the hit rates, the wrong pair of numbers, "
                    "and `50` is the miss rate mistaken for the factor."},
        ],
        "mistakes": [
            ("Reading a hit-rate gain as a percentage gain",
             "&ldquo;We improved the hit rate by five per cent&rdquo; says nothing about "
             "the backend. From `90%` to `95%` the backend&rsquo;s work halves; from "
             "`50%` to `55%` it falls by a ninth. The same five points, two different "
             "factors, because the quantity that moved is `1 − h` and the factor is the "
             "ratio of the two miss rates."),
            ("Quoting `h` in a sentence that is about the backend",
             "A capacity plan, a database size, an egress bill and a page about database "
             "CPU are all statements about `1 − h`. Writing `h` there is not wrong, it "
             "is unreadable: `99.9%` and `99%` look like the same number and differ by a "
             "factor of ten in every consequence."),
            ("Assuming the wait falls in step with the load",
             "At `μ = 2 000` rps, taking the backend from `1 000` rps to `100` rps cuts "
             "the load by ten and the mean wait from `1.00 ms` to `0.53 ms`. Waiting is "
             "a function of `ρ` and it is nearly flat once `ρ` is small, so most of what "
             "a cache buys in latency is bought before the last nine."),
        ],
        "standard": ("Finish when `1 − h` is the number you reach for without being asked.",
                     "You should be able to convert a hit rate and an arrival rate into "
                     "backend requests per second, divide by a capacity to get `ρ`, and "
                     "state a cache improvement as the factor by which the backend load "
                     "fell rather than as a change in percentage points."),
        "note": 'Backend load is only half of what a cache changes. The other half is what a single request experiences, and there the hit rate stops being a multiplier and becomes a weight: “Average Latency under a Cache” computes the mean as an expectation over two outcomes, and then shows that the percentile ignores the mean entirely.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "average-latency-under-a-cache",
        "title": "Average Latency under a Cache",
        "module": "The miss rate",
        "one_line": "Compute the mean latency as a weighted average of two outcomes, and the p99 as a rank that is one of them.",
        "summary": (
            "Under a cache a request has two possible latencies and nothing in between. "
            "The mean is the weighted average of the two, with the hit rate as the "
            "weight, and it is a number no request ever takes. The percentile is a "
            "different object: a rank on the same two outcomes, so it is always one of "
            "them, and it does not move gradually &mdash; it steps."
        ),
        "key": [
            "E[latency] = h·t_hit + (1 − h)·t_miss",
            "",
            "h = 95%,  t_hit = 1 ms,  t_miss = 40 ms",
            "mean = (19/20)(1) + (1/20)(40) = 59/20 = 2.95 ms",
            "",
            "P(latency ≤ t_hit) = h,  so the q-quantile is t_hit exactly when h ≥ q",
            "p50 = 1 ms    p95 = 1 ms    p99 = 40 ms    p99.9 = 40 ms",
        ],
        "key_label": "One expectation, and four ranks on the same two outcomes",
        "concepts_intro": (
            "The distribution here has exactly two values in it. That is what makes both "
            "calculations short and what makes them disagree so visibly."
        ),
        "concepts": [
            ("The mean is weighted, and the weight is the hit rate",
             "`E[latency] = h·t_hit + (1 − h)·t_miss` is the expected value of Discrete "
             "Mathematics applied to a two-outcome random variable. At `h = 95%`, "
             "`t_hit = 1 ms` and `t_miss = 40 ms` it is `59/20 = 2.95 ms` &mdash; nowhere "
             "near the midpoint `20.5 ms`, because the outcomes are not equally likely."),
            ("No request takes the mean",
             "Every request takes `1 ms` or `40 ms`. `2.95 ms` is a property of the "
             "stream, not of any request in it, and it is the number that a cache "
             "improvement moves smoothly. If somebody reports a mean latency of `3 ms` "
             "for a cached endpoint, one request in twenty is still taking `40`."),
            ("A percentile is a rank, so it steps",
             "`P(latency ≤ t_hit) = h` and `P(latency ≤ t_miss) = 1`. There is nothing "
             "between the two values, so the `q`-quantile is `t_hit` exactly when "
             "`h ≥ q` and `t_miss` otherwise. It cannot land between them, it does not "
             "interpolate, and it jumps by `t_miss − t_hit` all at once at `h = q`."),
        ],
        "read_title": "An expectation over two outcomes, and the percentile that ignores it",
        "read_intro": "The mean, the staircase it comes from, and the one hit rate at which each percentile flips.",
        "body": [
            ("def", ("Latency under a cache",
                     "A request is served in `t_hit` with probability `h` and in "
                     "`t_miss` with probability `1 − h`. Its "
                     "<strong>mean latency</strong> is "
                     "`E[latency] = h·t_hit + (1 − h)·t_miss`, and its "
                     "<strong>distribution</strong> takes only those two values.",
                     "`t_miss` here is the whole miss path: the lookup that failed, the "
                     "backend call, and the write back into the cache. It is not the "
                     "backend&rsquo;s service time alone.")),
            ("p", "The mean lies strictly between the two latencies whenever `h` is "
                  "strictly between `0` and `1`, and it equals neither. It sits close to "
                  "`t_hit` because `h` is close to `1`: the weighted average is dragged "
                  "toward whichever outcome is common, and in a cache that is the hit."),
            ("example", ("A ninety-five per cent cache over a forty-millisecond backend",
                         "`h = 95%`, `t_hit = 1 ms`, `t_miss = 40 ms`. The mean is "
                         "`(19/20)(1) + (1/20)(40) = 19/20 + 2 = 59/20 = 2.95 ms`. The "
                         "unweighted average of the two latencies is `20.5 ms`, seven "
                         "times too large, and it is the answer you get by forgetting "
                         "that one outcome happens nineteen times as often as the "
                         "other.")),
            ("h3", "The percentile is a different question with a different answer"),
            ("p", 'A percentile asks for a value, not an average: the `q`-quantile is '
                  'the smallest `t` with `P(latency ≤ t) ≥ q`, which is the '
                  'nearest-rank convention of “Percentiles from a Sample”. Here the '
                  'function `P(latency ≤ t)` is a staircase with two steps &mdash; it is '
                  '`0` below `t_hit`, `h` from `t_hit` up to `t_miss`, and `1` at '
                  '`t_miss` and above.'),
            ("math", [
                "P(latency ≤ t)      1 ┤                        ┌──────",
                "                      │                        │",
                "                    h ┤      ┌─────────────────┘",
                "                      │      │",
                "                    0 ┼──────┘",
                "                      └──────┴─────────────────┴──────",
                "                          t_hit              t_miss",
                "",
                "the curve is FLAT at h between the two values, so no percentile",
                "can land between them:  q ≤ h → t_hit,   q > h → t_miss",
            ]),
            ("p", "At `h = 95%` that gives `p50 = 1 ms`, `p95 = 1 ms`, `p99 = 40 ms` and "
                  "`p99.9 = 40 ms`. The median and the p95 are the hit latency; the p99 "
                  "is the miss latency, because more than one request in a hundred "
                  "misses and the hundredth-slowest is one of them."),
            ("h3", "Where each percentile flips"),
            ("p", "The `q`-quantile becomes `t_hit` at exactly `h = q` and not before. "
                  "So the p99 is the miss latency for every hit rate below `99%`, and "
                  "the p99.9 is the miss latency for every hit rate below `99.9%`. "
                  "Improving a cache from `95%` to `98.9%` does not move the p99 at all, "
                  "and then one more tenth of a point moves it by `39 ms`."),
            ("example", ("Three hit rates, one tail",
                         "`t_hit = 1 ms`, `t_miss = 40 ms`. At `h = 95%` the mean is "
                         "`2.95 ms` and the p99 is `40 ms`. At `h = 99%` the mean is "
                         "`139/100 = 1.39 ms` and the p99 has just become `1 ms` "
                         "&mdash; but the p99.9 is still `40 ms`. At `h = 99.9%` the "
                         "mean is `1039/1000 = 1.039 ms` and the p99.9 is `1 ms` too. "
                         "The mean moved by under two milliseconds across that whole "
                         "range; the tail moved in two jumps of thirty-nine.")),
            ("p", "This is why a cache is a poor answer to a tail problem and a good "
                  "answer to a throughput problem. It removes work, which is what Hit "
                  "Rate and Backend Load measured, and it shifts the mean, but the slow "
                  "requests it leaves behind are exactly as slow as they were. To move "
                  "the tail you have to move `t_miss`, or push `h` past the percentile "
                  "you care about &mdash; and the second of those gets expensive fast, "
                  "which is what Cache Size and Hit Rate is about."),
            ("p", "The model assumes two latencies and one hit rate. A real cache has a "
                  "spread on each &mdash; a hit is `0.8` to `1.4 ms`, a miss depends on "
                  "what the backend was doing &mdash; so treat `t_hit` and `t_miss` as "
                  "the typical values and read the answer as a shape rather than a "
                  "measurement. What survives the simplification is the staircase: two "
                  "clusters with a gap, and a percentile that lands in one cluster or "
                  "the other."),
        ],
        "lab": ("cache", {
            "mode": "hitrate",
            "view": "latency",
            "hit_tenths": 950,
            "t_hit": 1,
            "t_miss": 40,
        }),
        "steps_title": "Reporting the latency of a cached path",
        "steps_intro": "Compute the mean first because it is one line, then stop trusting it and compute the rank.",
        "steps": [
            ("Write both latencies and the hit rate",
             "`t_hit`, `t_miss` and `h`, with `t_miss` covering the whole miss path "
             "including the write back. Getting `t_miss` wrong is the largest error "
             "available here, because it carries almost all of the tail."),
            ("Take the weighted average",
             "`h·t_hit + (1 − h)·t_miss`. Keep `h` as a fraction and the answer stays "
             "exact: `(19/20)(1) + (1/20)(40) = 59/20`. Sanity-check it against "
             "`t_hit`: a mean far above the hit latency means `h` is lower than you "
             "thought."),
            ("For a percentile, compare `h` with `q`",
             "No arithmetic is needed. `h ≥ q` gives `t_hit`; otherwise `t_miss`. Do "
             "this for every percentile anyone quotes to you, because the answer is "
             "different for each and there is no interpolation to fall back on."),
            ("Say which percentiles moved and which did not",
             "A cache improvement moves the mean smoothly and moves each percentile "
             "once, at one specific hit rate. Reporting &ldquo;latency improved&rdquo; "
             "without saying which of the two you mean is how a team ships a change that "
             "helps the average and leaves every slow request exactly as slow."),
        ],
        "worked": {
            "title": "t_hit = 1 ms, t_miss = 40 ms: the mean and the four ranks",
            "intro": [
                "One expectation and four comparisons. The comparisons are the part "
                "worth slowing down for, because each one has a different answer."
            ],
            "lines": [
                "h = 95% = 19/20,  t_hit = 1 ms,  t_miss = 40 ms",
                "",
                "mean  = (19/20)(1) + (1/20)(40)",
                "      = 19/20 + 40/20",
                "      = 59/20 = 2.95 ms                    no request takes this",
                "",
                "ranks:  q ≤ h → t_hit,  q > h → t_miss",
                "  p50    q = 1/2      19/20 ≥ 1/2       →   1 ms",
                "  p95    q = 19/20    19/20 ≥ 19/20     →   1 ms",
                "  p99    q = 99/100   19/20 < 99/100    →  40 ms",
                "  p99.9  q = 999/1000 19/20 < 999/1000  →  40 ms",
                "",
                "now raise h to 99% = 99/100:",
                "  mean   = (99/100)(1) + (1/100)(40) = 139/100 = 1.39 ms",
                "  p99    99/100 ≥ 99/100             →   1 ms      it just flipped",
                "  p99.9  99/100 < 999/1000           →  40 ms      unchanged",
            ],
            "after": [
                "The `p95` line is the one to look at twice. `h = q` exactly, and the "
                "rule is `≥`, so the p95 is the hit latency &mdash; the boundary belongs "
                "to the hit. One tenth of a point lower and it is `40 ms`.",
                "For a faded rehearsal, take `t_hit = 2 ms`, `t_miss = 120 ms` and "
                "`h = 99%`. The supplied first move is that the mean is `(99/100)(2) + "
                "(1/100)(120)`; finish it, then find the smallest hit rate in tenths of "
                "a per cent at which the p99.9 becomes the hit latency, and say what the "
                "mean is there. State which percentile you have <em>not</em> moved.",
                "In the lab the staircase is drawn with the four percentile lines across "
                "it. Drag the hit rate slowly from `95%` upward and watch the mean slide "
                "while the p99 sits still, then jumps.",
            ],
        },
        "quiz_title": "Means, ranks and the gap between them",
        "quiz": [
            {"q": "`t_hit = 1 ms`, `t_miss = 40 ms`, `h = 95%`. What is the mean latency?",
             "a": ["`20.5 ms`", "`2.95 ms`", "`1.95 ms`", "`3.9 ms`"],
             "c": 1,
             "why": "`(19/20)(1) + (1/20)(40) = 59/20 = 2.95 ms`. `20.5` is the "
                    "unweighted average of the two latencies, which ignores the hit rate "
                    "entirely. `1.95` drops the hit&rsquo;s own contribution, and `3.9` "
                    "weights the miss by `1/10` rather than `1/20`."},
            {"q": "A service reports a `99%` cache hit rate, `t_hit = 1 ms` and `t_miss = 40 ms`. Which statement is true?",
             "a": ["The p99 and the p99.9 are both `1 ms`",
                   "The p99 is `1 ms` and the p99.9 is `40 ms`",
                   "The p99 is `1.39 ms`, the mean",
                   "The p99 is somewhere between `1 ms` and `40 ms`"],
             "c": 1,
             "why": "`h = 99/100 ≥ 99/100` so the p99 is the hit latency, but "
                    "`99/100 < 999/1000` so the p99.9 is still the miss latency. The "
                    "distribution has only two values in it: no percentile is the mean, "
                    "and none lands between the two."},
            {"q": "At `h = 95%` a team improves the cache to `98%`. What happens to the p99?",
             "a": ["It falls from `40 ms` to about `2 ms`",
                   "It does not move",
                   "It falls from `40 ms` to `1 ms`",
                   "It falls in proportion to the miss rate"],
             "c": 1,
             "why": "The p99 is the miss latency for every `h` below `99%`, so at `98%` "
                    "it is still `40 ms`. It flips to `1 ms` at `h = 99%` and not "
                    "before, in one jump of `39 ms`. The mean did improve over that "
                    "range, from `2.95 ms` to `1.78 ms`, which is the number the team "
                    "will be tempted to quote."},
            {"q": "Why is the mean latency of a cached path a number no request ever takes?",
             "a": ["Because latency is always measured with error",
                   "Because the distribution has only two values and the mean is between them",
                   "Because the mean is an estimate of the median",
                   "Because the hit rate changes over time"],
             "c": 1,
             "why": "Every request takes `t_hit` or `t_miss`, and the weighted average "
                    "of two distinct numbers with weights strictly between `0` and `1` "
                    "lies strictly between them. That is a fact about the arithmetic, "
                    "not about measurement error or drift, and it is why the mean and "
                    "the median can disagree by a factor of forty here."},
        ],
        "mistakes": [
            ("Averaging the two latencies instead of weighting them",
             "`(1 + 40)/2 = 20.5 ms` is the mean of a cache that hits half the time. The "
             "weight is the hit rate: `(19/20)(1) + (1/20)(40) = 2.95 ms`. The "
             "unweighted answer is wrong by a factor of seven here, and it gets worse as "
             "the cache gets better."),
            ("“Ninety-nine per cent hit rate, so the p99 is the hit latency”",
             "It is, at exactly `99%` and above &mdash; and the sentence is still "
             "misleading, because the p99.9 is the miss latency until the hit rate "
             "passes `99.9%`. Below `99%` the p99 is the miss latency outright. The rule "
             "is `h ≥ q`, applied to each percentile separately, and every quoted "
             "percentile needs its own comparison."),
            ("Expecting the tail to improve gradually",
             "Between `h = 95%` and `h = 98.9%` the p99 does not move by a "
             "microsecond, and then it moves by `39 ms` in one tenth of a point. A "
             "latency graph that shows a flat p99 across a cache improvement is not a "
             "broken graph; it is the shape of a two-valued distribution."),
        ],
        "standard": ("Finish when you compute the mean and the percentile as two different questions.",
                     "You should be able to produce the mean latency as a weighted "
                     "average, decide any percentile by comparing `h` with `q`, and say "
                     "which percentiles a proposed hit-rate improvement will and will "
                     "not move."),
        "note": 'Both lessons so far took the hit rate as given. It is not given &mdash; it comes out of how skewed the requests are and how much you are willing to store. “Popularity Is Skewed: Zipf” computes the first of those exactly, and it is the reason a cache holding one per cent of a catalogue is worth building at all.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "popularity-is-skewed",
        "title": "Popularity Is Skewed: Zipf",
        "module": "Skew, size and policy",
        "one_line": "Compute the share of requests the top k keys carry, as an exact ratio of harmonic sums.",
        "summary": (
            "Requests are not spread evenly over keys. Under a Zipf popularity the "
            "key of rank `i` is requested in proportion to `1/iˢ`, and the share the top "
            "`k` keys carry is the ratio of two harmonic sums &mdash; an exact fraction, "
            "computable term by term. That ratio is far larger than `k/N`, and the gap "
            "between the two is the entire case for caching."
        ),
        "key": [
            "p_i ∝ 1/i^s            rank 1 is the most popular; s is the Zipf exponent",
            "H(n, s) = 1 + 1/2^s + 1/3^s + … + 1/n^s",
            "",
            "top-k share = H(k, s) / H(N, s)          uniform would give k/N",
            "",
            "N = 50, s = 2:   k = 5  →  90.06% of the requests from 10% of the keys",
            "                 k = 1  →  61.53% of the requests from one key in fifty",
        ],
        "key_label": "A popularity law, and the share it gives the head",
        "concepts_intro": (
            "One assumption about the workload, one sum, and one comparison. The "
            "comparison is what the lesson is for: the uniform answer is the "
            "misconception, and it is computed here rather than described."
        ),
        "concepts": [
            ("Popularity falls with rank, and it falls fast",
             "Sort the keys by how often they are requested. Under a Zipf law the "
             "`i`-th most popular key takes a share proportional to `1/iˢ`, so rank `2` "
             "gets `1/2ˢ` of what rank `1` gets, rank `10` gets `1/10ˢ`. At `s = 1` that "
             "is a tenth; at `s = 2` it is a hundredth. `s` is the "
             "<strong>Zipf exponent</strong>, and it is the only thing on this course "
             "called `s`."),
            ("The normaliser is a harmonic sum",
             "Probabilities must sum to `1`, so `p_i = (1/iˢ)/H(N, s)` where "
             "`H(N, s) = Σ 1/iˢ` over `i` from `1` to `N` &mdash; the sigma notation of "
             "Algebra, summed exactly. `H(20, 1) = 55835135/15519504`. Dividing by it is "
             "the only step in this lesson that is not addition."),
            ("The top-`k` share is a ratio, and it beats `k/N`",
             "Adding the first `k` probabilities gives `H(k, s)/H(N, s)`. At `N = 50` "
             "and `s = 2` the top five keys &mdash; a tenth of the catalogue &mdash; "
             "carry `90.06%` of the requests, `9.01` times their share of the "
             "catalogue. Under uniform popularity they would carry exactly `10%`. That "
             "multiple is what a cache is buying."),
        ],
        "read_title": "A rank law, a harmonic normaliser, and the share of the head",
        "read_intro": "Where the sum comes from, what it gives at two exponents, and the one figure on this course that is not exact.",
        "body": [
            ("def", ("Zipf popularity",
                     "Rank `N` keys from most to least requested. Under a "
                     "<strong>Zipf popularity</strong> with exponent `s ≥ 0`, the key of "
                     "rank `i` is requested with probability "
                     "`p_i = (1/iˢ)/H(N, s)`, where "
                     "`H(N, s) = 1 + 1/2ˢ + 1/3ˢ + … + 1/Nˢ` is the "
                     "<strong>generalised harmonic number</strong>.",
                     "`s = 0` makes every key equally likely: `H(n, 0) = n` and "
                     "`p_i = 1/N`. Larger `s` concentrates the requests on the head. "
                     "Measured web and key-value workloads usually land between `s = 0.7` "
                     "and `s = 1.2`; this lesson uses integer exponents, for a reason "
                     "given below.")),
            ("p", "Two things are being assumed and both are worth saying out loud. The "
                  "first is the rank law itself, which is an empirical regularity rather "
                  "than a theorem &mdash; workloads are measured and found to look like "
                  "this, not derived and found to be this. The second is that the "
                  "ranking is stable over the window you care about, which is false for "
                  "news and true for a product catalogue."),
            ("p", "Given the law, everything after it is addition. The share of the "
                  "requests carried by the top `k` keys is the sum of the first `k` "
                  "probabilities, and the normaliser cancels down to a ratio of two "
                  "sums of the same shape."),
            ("math", [
                "                  k                    k",
                "                  Σ  p_i   =   (1/H(N,s))  Σ  1/i^s   =   H(k,s)",
                "                 i=1                  i=1            ──────",
                "                                                     H(N,s)",
                "",
                "uniform popularity (s = 0):   H(k,0)/H(N,0) = k/N",
            ]),
            ("example", ("Fifty keys at s = 2",
                         "`H(5, 2) = 1 + 1/4 + 1/9 + 1/16 + 1/25 = 5269/3600`. Dividing "
                         "by `H(50, 2)` gives `90.06%`: five keys out of fifty carry "
                         "ninety per cent of the requests. One key on its own &mdash; "
                         "two per cent of the catalogue &mdash; carries `61.53%`, "
                         "`30.77` times its share. Under uniform popularity those two "
                         "numbers would be `10%` and `2%`.")),
            ("h3", "Why this is the whole case for caching"),
            ("p", "A cache is worth building when a small store serves a large fraction "
                  "of the requests, and the ratio `H(k, s)/H(N, s)` divided by `k/N` is "
                  "exactly how much better than proportional you are doing. At `N = 50` "
                  "and `s = 2` that multiple is `9.01` for the top five keys and `30.77` "
                  "for the top one. At `s = 0` it is `1` for every `k`, and a cache "
                  "holding a tenth of the catalogue serves a tenth of the requests "
                  "&mdash; which is the misconception, arrived at by computing it."),
            ("p", "The multiple also shrinks as `k` grows, and that is the shape that "
                  "decides how big a cache should be: the first key is worth thirty "
                  "times its weight, the fiftieth is worth almost nothing. Cache Size "
                  "and Hit Rate reads a required cache size off exactly this curve."),
            ("h3", "The one figure on this course that is not exact"),
            ("p", "`H(n, s)` is a finite sum of fractions, so it is an exact rational "
                  "and the lab computes it that way, term by term, over arbitrary-"
                  "precision integers. What goes wrong is not accuracy but "
                  "readability: `H(50, 2)` is a fraction whose numerator and denominator "
                  "each run to forty-three digits, and a page that prints it has stopped "
                  "communicating."),
            ("p", "So the lab prints the exact fraction while the catalogue has at most "
                  "fifty keys, and above that it switches to a rounded value, marks the "
                  "figure with a `~`, and says on its own face that it has switched. "
                  "Drag `N` to `200` and the top two keys read `~25.865%` of the "
                  "requests &mdash; one per cent of the catalogue carrying a quarter of "
                  "the traffic, `25.87` times its share &mdash; with the tilde there to "
                  "tell you the sum is no longer exact. Every other number on this "
                  "course is a fraction."),
            ("p", "The exponent is an integer here for a related reason: at a fractional "
                  "`s` every term `1/iˢ` is irrational and there is no exact fraction to "
                  "print at all. Real workloads have fractional exponents, and the right "
                  "way to use this lesson on one is to bracket it &mdash; compute the "
                  "share at `s = 1` and at `s = 2` and report the interval, rather than "
                  "quote a rounded number with a confidence it has not earned."),
        ],
        "lab": ("cache", {
            "mode": "zipf",
            "n": 50,
            "s": 2,
            "k": 5,
        }),
        "steps_title": "Finding the share the head carries",
        "steps_intro": "Rank, sum, divide, and then compare against the uniform answer, because the comparison is the result.",
        "steps": [
            ("Rank the keys and name `N` and `s`",
             "Rank `1` is the most requested. `N` is how many distinct keys the workload "
             "touches in the window, not how many rows exist in the database &mdash; a "
             "table of ten million rows with forty thousand distinct daily readers has "
             "`N = 40 000`."),
            ("Sum the first `k` terms",
             "`H(k, s) = 1 + 1/2ˢ + … + 1/kˢ`, as fractions. At `s = 2` and `k = 5` that "
             "is `1 + 1/4 + 1/9 + 1/16 + 1/25 = 5269/3600`. Keep the fractions: the "
             "decimals here agree to four places and diverge after."),
            ("Sum all `N` terms and divide",
             "`H(k, s)/H(N, s)` is the share. If `N` is large enough that the sum is "
             "unreadable, the lab will round it and mark it; take the rounding as a "
             "signal to report an interval rather than a figure."),
            ("Divide by `k/N` and report the multiple",
             "The share on its own sounds impressive and means little. `90.06%` from "
             "`10%` of the keys is `9.01` times proportional, and that multiple is what "
             "tells you whether a cache is worth building for this workload."),
        ],
        "worked": {
            "title": "N = 50, s = 2: what the top five keys carry",
            "intro": [
                "Five terms, one division, and one comparison. The comparison at the end "
                "is the only part a reader will remember."
            ],
            "lines": [
                "N = 50 keys,  s = 2,  so p_i ∝ 1/i²",
                "",
                "H(5, 2) = 1 + 1/4 + 1/9 + 1/16 + 1/25",
                "        = 3600/3600 + 900/3600 + 400/3600 + 225/3600 + 144/3600",
                "        = 5269/3600",
                "",
                "H(50, 2) = 1 + 1/4 + … + 1/2500          43 digits over 43 digits",
                "         ≈ 1.625133",
                "",
                "share = H(5,2)/H(50,2) = 90.06%          exact, and unreadable printed",
                "",
                "uniform would give k/N = 5/50 = 1/10 = 10%",
                "multiple = 90.06 / 10 = 9.01×",
                "",
                "and one key alone:   H(1,2)/H(50,2) = 61.53%      = 30.77 × (1/50)",
            ],
            "after": [
                "The `9.01` is the number to carry away. It says that at this skew a "
                "cache is nine times more effective than its size suggests, and that is "
                "a statement about the workload, not about the cache.",
                "For a faded rehearsal, take `N = 20` and `s = 1`. The supplied first "
                "move is that `H(20, 1) = 55835135/15519504`; compute the share carried "
                "by the top two keys, which is ten per cent of that catalogue, and "
                "report it as a multiple of `k/N`. Then say what the same two numbers "
                "become at `s = 0`, and why.",
                "The lab draws the rank curve with the top `k` shaded and the cumulative "
                "share over it, with the uniform line dashed across for comparison. Set "
                "`s = 0` and watch the two lines meet: that is the misconception, drawn.",
            ],
        },
        "quiz_title": "Skew, sums and shares",
        "quiz": [
            {"q": "Under a Zipf popularity with `N = 50` and `s = 2`, the top five keys carry `90.06%` of the requests. What would uniform popularity give?",
             "a": ["`90.06%`, because the ranking is the same",
                   "`10%`, because five keys out of fifty is a tenth of the catalogue",
                   "`61.53%`, the share of the single most popular key",
                   "`50%`, because the median key is rank 25"],
             "c": 1,
             "why": "Uniform popularity is `s = 0`, where `H(n, 0) = n` and the share "
                    "collapses to `k/N = 5/50 = 10%`. The whole content of the skew is "
                    "the gap between `90.06%` and `10%`, a multiple of `9.01`. "
                    "`61.53%` is the top key&rsquo;s share at `s = 2`, not a uniform "
                    "figure."},
            {"q": "What is `H(3, 2)`?",
             "a": ["`1/9`", "`49/36`", "`6`", "`11/6`"],
             "c": 1,
             "why": "`H(3, 2) = 1 + 1/2² + 1/3² = 1 + 1/4 + 1/9 = 49/36`. `1/9` is only "
                    "the last term. `6` is `H(3, 0) · 2`, and `11/6` is `H(3, 1)`, the "
                    "sum at exponent one rather than two &mdash; the commonest slip, "
                    "because the exponent goes on `i` and not on the whole term."},
            {"q": "A workload has `N = 200` keys and `s = 1`. The lab reports the top two keys as carrying `~25.865%` of requests. Why the tilde?",
             "a": ["Because the measurement is noisy",
                   "Because `H(200, 1)` is summed in floating point rather than exactly, past the readable limit",
                   "Because `s = 1` makes the terms irrational",
                   "Because the top two keys are not exactly the top two"],
             "c": 1,
             "why": "The sum is still finite and still rational, but past about fifty "
                    "keys the exact fraction runs to dozens of digits and stops "
                    "communicating, so the lab switches to a rounded sum and marks the "
                    "figure. At `s = 1` every term is rational; it is a fractional `s` "
                    "that makes them irrational, which is why the exponent here is an "
                    "integer."},
        ],
        "mistakes": [
            ("Assuming uniform popularity — “cache 10%, get 10%”",
             "This is the default model people carry without noticing they hold it, and "
             "it is exactly `s = 0`. At `N = 50` and `s = 2` a tenth of the keys carries "
             "`90.06%` of the requests, not `10%`. Any argument that a cache is not "
             "worth building because it can only hold a small fraction of the data is "
             "this assumption, unstated."),
            ("Putting the exponent on the wrong thing",
             "`p_i ∝ 1/iˢ` raises the <em>rank</em> to the exponent, so at `s = 2` the "
             "terms are `1, 1/4, 1/9, 1/16`. Raising the whole term instead gives "
             "`1, 1/2, 1/3` squared away somewhere else and a harmonic number that is "
             "not `H(n, s)`. Check against `H(3, 2) = 49/36` before going further."),
            ("Taking `N` as the size of the database",
             "`N` is the number of distinct keys the workload touches in the window "
             "under discussion. A ten-million-row table read by forty thousand distinct "
             "keys a day has `N = 40 000` for a daily cache, and using ten million "
             "instead makes every share look hopeless and every cache look pointless."),
        ],
        "standard": ("Finish when the uniform answer is something you compute in order to reject it.",
                     "You should be able to write `p_i` for a Zipf workload, sum "
                     "`H(k, s)` and `H(N, s)` exactly at an integer exponent, produce the "
                     "top-`k` share as a fraction, and state it as a multiple of `k/N`."),
        "note": 'This lesson reads the share off a chosen `k`. The question a cache actually poses is the other way round: given a hit rate you want, how many keys must you hold? “Cache Size and Hit Rate” inverts the same ratio, and the answer has a shape &mdash; the first nine is cheap and the second is not.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "cache-size-and-hit-rate",
        "title": "Cache Size and Hit Rate",
        "module": "Skew, size and policy",
        "one_line": "Find the smallest cache that reaches a target hit rate, and price the next nine.",
        "summary": (
            "Holding the `C` most popular keys gives a hit rate of `H(C, s)/H(N, s)`, "
            "the same ratio the previous lesson computed, read as a function of `C`. It "
            "is a curve that rises steeply and then flattens, so the cache size a target "
            "requires is read off it rather than scaled: at `N = 50` and `s = 2`, ninety "
            "per cent costs five keys and ninety-nine costs twenty-eight."
        ),
        "key": [
            "h(C) = H(C, s) / H(N, s)        cache the top C of N keys",
            "",
            "N = 50, s = 2",
            "C = 1   →  61.533%        C = 5   →  90.061%       90% costs 5 keys",
            "C = 10  →  95.363%        C = 28  →  99.060%       99% costs 28 keys",
            "C = 47  →  99.923%                                 99.9% costs 47 keys",
            "",
            "5 → 28 keys is 5.6× the cache for one more nine",
        ],
        "key_label": "The hit-rate curve, and what each nine costs on it",
        "concepts_intro": (
            "The formula is the previous lesson&rsquo;s, with `k` renamed `C` and read "
            "backwards. What is new is the shape of the curve and what the shape implies."
        ),
        "concepts": [
            ("A cache of the top `C` keys hits `H(C, s)/H(N, s)`",
             "The idealisation is that the cache holds exactly the `C` most popular keys "
             "and never anything else. Then a request hits when its key is in the top "
             "`C`, which happens with probability `H(C, s)/H(N, s)`. Real caches "
             "approximate this badly or well depending on the policy, which is "
             "Replacement Policies on a Trace; this lesson is the ceiling they aim at."),
            ("The curve rises steeply and then flattens",
             "At `N = 50` and `s = 2` the first key alone gives `61.533%`, five keys give "
             "`90.061%`, twenty-eight give `99.060%` and forty-seven give `99.923%`. The "
             "marginal value of a key falls with its rank because its probability does, "
             "so each further nine costs several times the cache of the one before."),
            ("Hit rate is not proportional to cache size",
             "Doubling a cache does not double its hit rate and cannot: the hit rate is "
             "bounded by `1` and the curve is concave. Going from `90%` to `99%` here "
             "takes the cache from `5` keys to `28`, which is `5.6` times the memory for "
             "`9` percentage points &mdash; and, by Hit Rate and Backend Load, a tenfold "
             "cut in backend load, which is what you were buying."),
        ],
        "read_title": "The hit-rate curve, the size a target costs, and where the returns go",
        "read_intro": "One formula read as a function of C, the scan that inverts it, and what this replaces from Capacity Estimation.",
        "body": [
            ("def", ("Hit rate as a function of cache size",
                     "For a Zipf workload over `N` keys with exponent `s`, a cache "
                     "holding the `C` most popular keys has hit rate "
                     "`h(C) = H(C, s)/H(N, s)`, for `C` from `0` to `N`.",
                     "`h(0) = 0` and `h(N) = 1`. Between them `h` is strictly increasing "
                     "and concave: each additional key adds `p_{C+1}`, and the "
                     "probabilities are decreasing, so the increments shrink.")),
            ("p", "That is the whole model, and the assumption inside it is worth "
                  "naming: the cache holds the <em>right</em> `C` keys. No online policy "
                  "knows which those are, so `h(C)` is an upper bound on what a cache of "
                  "`C` slots achieves on this workload, reached only if the popularity "
                  "ranking is stable and the policy is good."),
            ("h3", "Inverting the curve: the C a target costs"),
            ("p", "To find the smallest `C` reaching a target `h`, add probabilities in "
                  "rank order until the running total crosses it. No formula is needed "
                  "and none exists in closed form for integer `C`; the lab runs the scan "
                  "over exact fractions, so the `C` it reports is the smallest one, not "
                  "the smallest one up to rounding."),
            ("math", [
                "N = 50, s = 2        running total of p_i, in rank order",
                "",
                "  C      h(C)          target reached",
                "  1    61.533%",
                "  5    90.061%         ← 90%   costs 5 keys, a tenth of the catalogue",
                " 10    95.363%         ← 95%   costs 10",
                " 28    99.060%         ← 99%   costs 28, more than half the catalogue",
                " 47    99.923%         ← 99.9% costs 47",
            ]),
            ("example", ("What the second nine costs",
                         "From `90%` to `99%` the cache goes from `5` keys to `28`: "
                         "twenty-three more keys, `5.6` times the memory. From `99%` to "
                         "`99.9%` it goes from `28` to `47`, and the catalogue only has "
                         "fifty keys in it &mdash; past that point you are not caching, "
                         "you are copying.")),
            ("p", "Put the two courses together and the trade is visible. Five keys of "
                  "cache cut the backend load by a factor of ten (from `100%` to `10%` "
                  "of `λ`); twenty-eight keys cut it by a hundred. The second factor of "
                  "ten cost `5.6` times the memory of the first. Whether that is a good "
                  "deal depends entirely on what the backend was doing at the higher "
                  "load, which is the `ρ` of Hit Rate and Backend Load."),
            ("h3", "This replaces a number you were previously handed"),
            ("p", '“Memory and the Working Set” sized a cache by stating a hot fraction '
                  '&mdash; assume ten per cent of the data is hot, multiply by the row '
                  'size, buy that much memory. That is a serviceable estimate and it is '
                  'an assumption. Here the hot fraction is a <em>result</em>: it comes '
                  'out of `N` and `s`, and at `N = 50` and `s = 2` the ten per cent that '
                  'lesson assumed turns out to deliver `90.061%`, which is either lucky '
                  'or a coincidence depending on the workload.'),
            ("p", "So the honest procedure is the other way round from the one that "
                  "course taught: measure the skew, choose the hit rate you need from "
                  "what the backend can take, and let the curve tell you the cache size. "
                  "If the skew is unknown, bracket it &mdash; compute the required `C` "
                  "at `s = 1` and at `s = 2` and carry both numbers, which is the error "
                  "bar Capacity Estimation asked you never to drop."),
            ("p", "One caution about the flattening. The curve says the last nine is "
                  "expensive in memory; it does not say the last nine is worthless. "
                  "Whether it is worth buying is a question about the backend, and there "
                  "the same nine is a tenfold cut in load every time. Read the two "
                  "curves together or you will talk yourself out of a cache that was "
                  "about to save a database."),
        ],
        "lab": ("cache", {
            "mode": "size",
            "n": 50,
            "s": 2,
            "target_tenths": 900,
        }),
        "steps_title": "Sizing a cache from a target hit rate",
        "steps_intro": "The target comes from the backend, not from the cache. Everything after that is a scan.",
        "steps": [
            ("Get the target from the backend, not from taste",
             "Decide what backend load the backend can take, divide by `λ`, and that is "
             "your miss rate. A backend that can serve `500` rps under `10 000` rps of "
             "traffic needs `1 − h ≤ 1/20`, so `h ≥ 95%`. Choosing `99%` because it "
             "sounds professional sizes the cache from a slogan."),
            ("Measure `N` and `s` for the window that matters",
             "`N` is the distinct keys touched, `s` is the skew. Both are measurements. "
             "If you have a rank-frequency sample, fit `s` roughly by comparing the top "
             "key&rsquo;s share against the table; if you have nothing, bracket `s` "
             "between `1` and `2` and carry both answers."),
            ("Scan the running total to the target",
             "Add `p₁, p₂, p₃, …` until the total reaches `h`. The `C` at which it "
             "crosses is the answer, and it is an integer &mdash; there is no "
             "interpolating a cache to two and a half keys."),
            ("Price the next nine before you commit",
             "Compute `C` for your target and for one nine beyond it. If the second "
             "number is a small multiple of the first, buy it now; if it is most of the "
             "catalogue, you have found the point where this workload stops rewarding "
             "memory and the answer is a different design."),
        ],
        "worked": {
            "title": "N = 50, s = 2: the cache for 90% and the cache for 99%",
            "intro": [
                "The scan is a running sum over exact fractions. Only the crossings are "
                "written out here; the lab shows every step."
            ],
            "lines": [
                "N = 50, s = 2.   H(50,2) ≈ 1.625133.   h(C) = H(C,2)/H(50,2)",
                "",
                "  C = 1    H(1,2) = 1              h = 61.533%",
                "  C = 2    + 1/4                   h = 76.917%",
                "  C = 3    + 1/9                   h = 83.754%",
                "  C = 4    + 1/16                  h = 87.600%",
                "  C = 5    + 1/25 = 5269/3600      h = 90.061%   ← first ≥ 90%",
                "  …",
                "  C = 28                           h = 99.060%   ← first ≥ 99%",
                "",
                "for 90%:   C = 5   =  10% of the catalogue",
                "for 99%:   C = 28  =  56% of the catalogue",
                "",
                "cost of the extra nine:  28 − 5 = 23 keys,  28/5 = 5.6× the cache",
                "what it buys, by Hit Rate and Backend Load:  backend load 1/10 → 1/100 of λ",
            ],
            "after": [
                "Five keys reach ninety per cent and twenty-eight reach ninety-nine. "
                "Notice that the second figure is more than half the catalogue: on a "
                "workload this small, the last nine means keeping most of the data, and "
                "the word &ldquo;cache&rdquo; has stopped being accurate.",
                "For a faded rehearsal, keep `N = 50` and set `s = 1`. The supplied first "
                "move is that the head is much flatter, so every target costs more; find "
                "the `C` for `90%` and for `99%` at that skew and state the ratio "
                "between them. Then say, in one sentence, what the two skews together "
                "tell you about how confident you can be in a cache size when `s` is "
                "only known to within a point.",
                "The lab draws the curve with the target line across it and the required "
                "`C` marked, and the red bar under the axis is the distance between the "
                "ninety and the ninety-nine. Move the skew slider and watch that bar "
                "grow.",
            ],
        },
        "quiz_title": "Sizes, targets and diminishing returns",
        "quiz": [
            {"q": "At `N = 50` and `s = 2`, five keys give `90.061%`. Roughly how many keys give `99%`?",
             "a": ["About `10`, because the miss rate has to halve twice",
                   "`28`",
                   "`50`, the whole catalogue",
                   "About `6`, because the curve is nearly flat there"],
             "c": 1,
             "why": "The scan crosses `99%` at `C = 28`: twenty-three more keys, `5.6` "
                    "times the cache. `10` is the `C` for `95%`. The curve being nearly "
                    "flat is exactly why `6` is wrong &mdash; a flat curve means each "
                    "further key adds very little, so reaching a higher target takes "
                    "<em>more</em> keys, not fewer."},
            {"q": "A team doubles a cache from `C` to `2C` and the hit rate goes from `90%` to `93%`. What does that tell you?",
             "a": ["The cache is broken; doubling should have doubled the hit rate",
                   "Nothing is wrong: `h(C)` is concave, so the second half of a cache is always worth less than the first",
                   "The workload must be uniform",
                   "The hit rate must have been mismeasured, since it cannot exceed `100%`"],
             "c": 1,
             "why": "Hit rate cannot be proportional to cache size &mdash; it is bounded "
                    "by `1` &mdash; and under any decreasing popularity the increments "
                    "shrink with rank. A uniform workload would be the one case where "
                    "doubling the cache does double the hit rate, up to the bound, so "
                    "this result is evidence <em>against</em> uniformity."},
            {"q": "Why is `h(C) = H(C, s)/H(N, s)` an upper bound rather than a prediction for a real cache of `C` slots?",
             "a": ["Because real caches lose entries to TTLs",
                   "Because it assumes the cache holds exactly the `C` most popular keys, which no online policy knows",
                   "Because harmonic sums are only approximate",
                   "Because `s` is never exactly an integer"],
             "c": 1,
             "why": "The formula prices a cache that already contains the right keys. A "
                    "running policy has to learn which they are from the request stream "
                    "and will hold some it should not. TTLs and fractional exponents are "
                    "real complications, but the bound is a bound because of the "
                    "idealised contents, not because of either."},
        ],
        "mistakes": [
            ("Scaling the hit rate with the cache size",
             "&ldquo;We have a `90%` hit rate on `5` keys, so `10` keys would give us "
             "`180%`&rdquo; is obviously wrong, and the same reasoning with smaller "
             "numbers is not. `h` is concave and bounded: at `N = 50` and `s = 2`, `10` "
             "keys give `95.363%`, not twice `90.061%`."),
            ("Sizing the cache before choosing the target",
             "The target hit rate is a statement about what the backend can absorb, and "
             "it comes from `λ` and `μ`. Picking a cache size first and reporting "
             "whatever hit rate it happens to give is how a team ends up defending a "
             "number they did not choose."),
            ("Treating the assumed hot fraction as a measurement",
             'The ten-per-cent working set of “Memory and the Working Set” is an '
             'assumption that makes an estimate possible, not a property of your '
             'workload. Here it is a consequence of `N` and `s`, and at `s = 1` the same '
             'ten per cent of fifty keys delivers far less than it does at `s = 2`. If '
             'the skew is unknown, carry both answers.'),
        ],
        "standard": ("Finish when you size a cache from a target and price the nine beyond it without being asked.",
                     "You should be able to compute `h(C)` for a given `C`, scan to the "
                     "smallest `C` reaching a target hit rate, express that `C` as a "
                     "share of the catalogue, and state what the next nine costs in "
                     "keys and buys in backend load."),
        "note": 'Both of the last two lessons assumed the cache holds the most popular keys. Nothing running in production knows which those are. “Replacement Policies on a Trace” counts what four policies actually achieve on a reference string, with the offline optimum as the ceiling &mdash; and finds a trace where a bigger cache makes one of them worse.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "replacement-policies-on-a-trace",
        "title": "Replacement Policies on a Trace",
        "module": "Skew, size and policy",
        "one_line": "Count hits for FIFO, LRU, LFU and farthest-in-future at two cache sizes, and find a trace where a bigger cache is worse.",
        "summary": (
            "A replacement policy is judged by the hits it gets on a reference string, "
            "not by how sensible its rule sounds. Farthest-in-future is the offline "
            "optimum and therefore the bound; the three runnable policies fall short of "
            "it by different amounts on different traces. And FIFO can miss more often "
            "with a larger cache, which is Belady&rsquo;s anomaly and is measured here "
            "rather than asserted."
        ),
        "key": [
            "trace   1 2 3 4 1 2 5 1 2 3 4 5        12 references, 5 distinct keys",
            "",
            "hits      OPT       FIFO      LRU       LFU",
            "k = 3     5/12      1/4       1/6       1/6",
            "k = 4     1/2       1/6       1/3       1/3",
            "",
            "FIFO misses 9 at k = 3 and 10 at k = 4        Belady's anomaly",
            "OPT = evict the key whose next use is farthest in the future",
        ],
        "key_label": "Four policies, one reference string, two cache sizes",
        "concepts_intro": (
            "A policy is a rule for choosing a victim. Three of these can be run by a "
            "cache; the fourth cannot, and that is what makes it useful."
        ),
        "concepts": [
            ("A policy is measured on a trace, not argued about",
             "Give a policy a reference string and a number of slots and it produces a "
             "definite number of hits. FIFO evicts the oldest arrival, LRU the "
             "least recently used, LFU the least frequently used. On "
             "`1 2 3 4 1 2 5 1 2 3 4 5` with three slots those give `1/4`, `1/6` and "
             "`1/6` &mdash; and FIFO, the policy nobody defends, wins."),
            ("Farthest-in-future is the bound, and it cannot be run",
             "The offline optimum evicts the resident key whose next use is furthest "
             "ahead in the trace. It needs the rest of the trace, so no cache can "
             "execute it, and that is precisely why it is useful: no online policy beats "
             "it, so the gap between it and LRU is the most any policy change could "
             "possibly buy. On this trace with three slots it gets `5/12` against "
             "LRU&rsquo;s `1/6`."),
            ("A bigger cache is not a guarantee",
             "LRU and farthest-in-future are stack algorithms: a cache of `k+1` slots "
             "always contains everything a cache of `k` slots would, so their miss "
             "counts cannot rise when the cache grows. FIFO has no such property, and on "
             "this trace it misses `9` times with three slots and `10` times with four."),
        ],
        "read_title": "Four policies, the bound, and the anomaly",
        "read_intro": "What each rule does, who proves the optimum is optimal, and the trace on which more memory costs hits.",
        "body": [
            ("def", ("Reference string and replacement policy",
                     "A <strong>reference string</strong> is the sequence of keys a "
                     "cache is asked for. A <strong>replacement policy</strong> is the "
                     "rule that chooses which resident key to evict when a miss arrives "
                     "at a full cache of `k` slots. Its "
                     "<strong>hit rate on that string</strong> is hits divided by "
                     "references.",
                     "The first reference to each key must miss whatever the policy and "
                     "whatever `k`: those are the "
                     "<strong>compulsory misses</strong>, and on a trace of five "
                     "distinct keys there are five of them.")),
            ("ul", [
                "<strong>FIFO</strong> evicts the key that entered the cache earliest, "
                "regardless of use since.",
                "<strong>LRU</strong> evicts the key that was used least recently.",
                "<strong>LFU</strong> evicts the key with the smallest use count, ties "
                "broken by insertion order; a count dies with the entry it belongs to.",
                "<strong>Farthest-in-future</strong> evicts the resident key whose next "
                "use is furthest ahead, or one that is never used again.",
            ]),
            ("h3", "The bound, and whose proof it is"),
            ("p", 'Farthest-in-future &mdash; also called Belady&rsquo;s algorithm, or '
                  'OPT &mdash; minimises misses over every possible policy on a given '
                  'trace. It is <strong>offline</strong>: it reads the rest of the '
                  'request sequence to choose a victim, which no cache can do. So it is '
                  'not a policy anyone runs; it is a ceiling against which the policies '
                  'people do run are measured.'),
            ("p", 'That it is optimal is a theorem, proved by an exchange argument, and '
                  'the proof is not this course&rsquo;s. It is Algorithms, in “Greedy '
                  'Algorithms and Matroids”, in the lesson “Optimal Offline Caching” '
                  '&mdash; `algorithms/greedy-algorithms-and-matroids/optimal-caching` '
                  '&mdash; which also draws the offline/online distinction properly. '
                  'What this lesson does with the theorem is use it: the bound turns '
                  '&ldquo;our hit rate is `1/6`&rdquo; into &ldquo;the best any policy '
                  'could have done on this trace is `5/12`, and we are getting `1/6`&rdquo;.'),
            ("example", ("Twelve references, five keys, three slots",
                         "On `1 2 3 4 1 2 5 1 2 3 4 5` with `k = 3`: "
                         "farthest-in-future gets `5` hits (`5/12`), FIFO gets `3` "
                         "(`1/4`), LRU gets `2` (`1/6`) and LFU gets `2` (`1/6`). The "
                         "gap between the bound and LRU is `1/4` of all references, "
                         "which is the most that a better online policy could have "
                         "recovered &mdash; and no online policy can recover all of it, "
                         "because the bound reads the future.")),
            ("h3", "Belady's anomaly: more memory, more misses"),
            ("p", "Now give the same trace four slots instead of three. LRU improves "
                  "from `2` hits to `4`, LFU from `2` to `4`, the optimum from `5` to "
                  "`6`. FIFO goes from `3` hits to `2`: its miss count rises from `9` "
                  "to `10`. A larger cache made it worse."),
            ("thm", ("Stack algorithms, and what FIFO is not",
                     "A policy is a <strong>stack algorithm</strong> if, at every point "
                     "of every trace, the contents of a `k`-slot cache are a subset of "
                     "the contents of a `(k+1)`-slot cache. For such a policy every hit "
                     "at `k` is a hit at `k+1`, so the miss count is non-increasing in "
                     "the cache size.",
                     "LRU and farthest-in-future are stack algorithms; FIFO is not, "
                     "because its eviction order depends on insertion times that change "
                     "when the cache size changes. Having no such guarantee is not the "
                     "same as always failing &mdash; FIFO is well behaved on most traces "
                     "&mdash; but it means no trace is safe.")),
            ("p", "This is the misconception the lesson exists to kill, and it is a "
                  "belief people genuinely hold: that adding memory to a cache can be "
                  "neutral at worst. It cannot, unless you know which policy you are "
                  "running and that it is a stack algorithm. The lab scans every cache "
                  "size from `1` to `6` for all four policies on your own trace and "
                  "reports where any of their miss counts rises, so the anomaly arrives "
                  "as a measurement rather than as a claim."),
            ("p", "Two limits on what a trace can tell you. A hit count on twelve "
                  "references is a fact about twelve references and not about your "
                  "system; policies are separated by workloads, and a trace with a hot "
                  "key ranks them differently from a round robin. And nothing here is "
                  "about cost: LRU needs bookkeeping that FIFO does not, and whether "
                  "that is worth two per cent of hit rate is an implementation question "
                  "this course leaves to Algorithms."),
        ],
        "lab": ("cache", {
            "mode": "replace",
            "trace": "1 2 3 4 1 2 5 1 2 3 4 5",
            "k1": 3,
            "k2": 4,
            "step": 10,
        }),
        "steps_title": "Running a policy comparison honestly",
        "steps_intro": "Two cache sizes, always. One size tells you which policy won a coin toss.",
        "steps": [
            ("Write the trace and count the distinct keys",
             "The distinct count is the compulsory misses, the floor every policy shares. "
             "A comparison that does not subtract them exaggerates how close the "
             "policies are: on twelve references with five distinct keys, five of the "
             "misses were never anyone&rsquo;s fault."),
            ("Run the optimum first",
             "Farthest-in-future gives you the ceiling before you have any attachment to "
             "a policy. If the gap between the bound and your current policy is small, "
             "no replacement change will help and the answer is a bigger cache or a "
             "different workload."),
            ("Run the runnable policies at two sizes",
             "FIFO, LRU and LFU at `k` and at `k+1`. Two sizes, because a single size is "
             "one sample and because the second size is where an anomaly becomes "
             "visible. Compare hit counts, not hit rates, if the traces differ in "
             "length."),
            ("Check whether any miss count rose",
             "If a policy misses more with more slots, you have found Belady&rsquo;s "
             "anomaly and you have learned something about the policy rather than about "
             "the trace. LRU and the optimum cannot do this; FIFO and LFU carry no such "
             "guarantee."),
        ],
        "worked": {
            "title": "1 2 3 4 1 2 5 1 2 3 4 5 at three slots and at four",
            "intro": [
                "Twelve references over five keys. The four-slot run is the one that "
                "matters, and it is the one most people would not bother with."
            ],
            "lines": [
                "trace:  1 2 3 4 1 2 5 1 2 3 4 5        12 references, 5 distinct keys",
                "        compulsory misses: 5, for any policy at any size",
                "",
                "k = 3 slots        hits   rate     misses",
                "  OPT               5     5/12       7        the bound",
                "  FIFO              3     1/4        9",
                "  LRU               2     1/6       10",
                "  LFU               2     1/6       10",
                "",
                "k = 4 slots        hits   rate     misses",
                "  OPT               6     1/2        6",
                "  FIFO              2     1/6       10        ← MORE misses than at k = 3",
                "  LRU               4     1/3        8",
                "  LFU               4     1/3        8",
                "",
                "FIFO:   9 misses at k = 3  →  10 misses at k = 4",
                "gap at k = 3:  OPT 5/12 − LRU 1/6 = 1/4 of all references",
            ],
            "after": [
                "Two results, and they point in different directions. At three slots "
                "FIFO beats LRU on this trace, which is a fact about this trace. At four "
                "slots FIFO gets worse than it was at three, which is a fact about "
                "FIFO: it is not a stack algorithm and has no guarantee to break.",
                "For a faded rehearsal, run `A B C A B D A B C D` at `k = 3` and "
                "`k = 4`. The supplied first move is that the optimum gets `5` hits at "
                "three slots; find LRU and FIFO at both sizes, and then say which "
                "policy&rsquo;s ranking changed between the two cache sizes and whether "
                "any miss count rose. Report what that trace does and does not show "
                "about the anomaly.",
                "The lab replays your own trace through all four policies, steps through "
                "the cache contents reference by reference so you can watch a policy "
                "make the eviction it is about to regret, and scans every cache size "
                "from one to six looking for a rise. It reports which policies it found "
                "one for and which it did not.",
            ],
        },
        "quiz_title": "Policies, bounds and anomalies",
        "quiz": [
            {"q": "On `1 2 3 4 1 2 5 1 2 3 4 5`, FIFO misses `9` times with three slots and `10` times with four. What does this show?",
             "a": ["That the simulation has a bug, since a bigger cache cannot miss more",
                   "Belady&rsquo;s anomaly: FIFO is not a stack algorithm, so its miss count need not fall when the cache grows",
                   "That LRU is optimal and FIFO is not",
                   "That the trace is too short to draw conclusions from"],
             "c": 1,
             "why": "FIFO evicts by insertion order, and changing the cache size changes "
                    "which keys are resident and therefore that order &mdash; so a "
                    "`k`-slot cache&rsquo;s contents need not be a subset of a "
                    "`(k+1)`-slot cache&rsquo;s. LRU and farthest-in-future are stack "
                    "algorithms and cannot do this; whether LRU is optimal is a "
                    "different question, settled in Algorithms."},
            {"q": "Why is farthest-in-future used as a bound rather than as a policy?",
             "a": ["Because it is too slow to compute",
                   "Because it evicts by looking at the rest of the trace, which a running cache does not have",
                   "Because it is only optimal for small caches",
                   "Because it needs the popularity distribution in advance"],
             "c": 1,
             "why": "It is offline: choosing a victim requires knowing when each "
                    "resident key is next referenced. Computing it is cheap once you "
                    "have the trace, and it is optimal at every cache size &mdash; the "
                    "exchange-argument proof is in Algorithms, in &ldquo;Optimal Offline "
                    "Caching&rdquo;. What it cannot be is executed by a cache serving "
                    "live traffic."},
            {"q": "A trace has `12` references over `5` distinct keys. What is the largest possible hit rate at any cache size?",
             "a": ["`1`, with a big enough cache",
                   "`7/12`",
                   "`5/12`",
                   "`1/2`, the optimum&rsquo;s rate at four slots"],
             "c": 1,
             "why": "The first reference to each distinct key must miss, so at least `5` "
                    "of the `12` are compulsory misses and at most `7` can be hits: "
                    "`7/12`. No cache size and no policy removes a compulsory miss. "
                    "`5/12` is the optimum&rsquo;s actual rate at three slots, well "
                    "below the ceiling."},
            {"q": "At three slots on this trace, FIFO gets `1/4` and LRU gets `1/6`. What follows?",
             "a": ["FIFO is a better policy than LRU",
                   "On this trace at this size FIFO does better, which is a fact about the trace rather than a ranking of the policies",
                   "LRU must have been implemented incorrectly",
                   "The workload must have no temporal locality at all"],
             "c": 1,
             "why": "A single trace at a single size is one measurement. At four slots "
                    "the order reverses: LRU gets `1/3` and FIFO gets `1/6`. Policies "
                    "are separated by workloads, which is why the method is two sizes "
                    "and, in practice, a trace taken from the system you actually run."},
        ],
        "mistakes": [
            ("Believing a bigger cache can never hurt",
             "It can, and the trace `1 2 3 4 1 2 5 1 2 3 4 5` is where: FIFO misses `9` "
             "times at three slots and `10` at four. The guarantee people are reaching "
             "for is real but belongs to stack algorithms &mdash; LRU and "
             "farthest-in-future &mdash; and FIFO is not one. Before adding memory to a "
             "cache, know which policy it runs."),
            ("Comparing policies on one trace at one size",
             "FIFO beats LRU here at three slots and loses to it at four. A comparison "
             "that reports the first number and stops has measured the trace, not the "
             "policies. Two sizes at minimum, and a trace from the system you are "
             "actually asking about."),
            ("Reading the bound as a target",
             "Farthest-in-future is what an oracle would achieve, and the gap between it "
             "and your policy is the most any online change could recover &mdash; not "
             "the amount one will. If the bound is `5/12` and you have `1/6`, a better "
             "policy might close part of that; nothing closes all of it, because nothing "
             "online reads the future."),
        ],
        "standard": ("Finish when you would not accept a policy comparison run at one cache size.",
                     "You should be able to replay a short reference string through FIFO, "
                     "LRU, LFU and farthest-in-future, count hits at two cache sizes, "
                     "identify the compulsory misses, quote the bound as a bound, and "
                     "recognise a rising miss count as Belady&rsquo;s anomaly rather "
                     "than as a mistake."),
        "note": 'That is the last of the three things which decide a hit rate: the skew, the size and the policy. The rest of the course is about the two things a cache does wrong even when its hit rate is excellent. The first is staleness, and “TTL and Staleness” prices it &mdash; along with what a shorter TTL costs in misses, which is the part that is usually left out.',
    },
]
