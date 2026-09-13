"""Partitioning and Load Balancing, lessons 07-12 - the maximum of N, and crossing shards."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "stragglers",
        "title": "Stragglers",
        "module": "The maximum of N",
        "one_line": "Compute a job's mean and p99 from one partition's time distribution, and say what another partition buys.",
        "summary": (
            "A job that waits for all of its partitions finishes when its slowest one "
            "does, so its running time is the maximum of `N` draws rather than the mean "
            "of them. The maximum's distribution is computed exactly here by "
            "enumeration, and it moves the wrong way as `N` grows: with the lab's "
            "distribution, 24 partitions average `111.63 ms` against a single partition's "
            "`25.80 ms`, and 32 partitions are slower still."
        ),
        "key": [
            "job time = max of N partition times      not the mean, and not the sum",
            "",
            "one partition, from 20:900, 40:70, 120:25, 400:5",
            "  mean 25.80 ms      p99 120 ms",
            "N = 24     job mean 111.63 ms      job p99 400 ms",
            "straggler tax = 111.63/25.80 = 4.33×",
            "P(at least one past 120 ms) = 1 − 0.995²⁴ = 11.33%",
        ],
        "key_label": "The job is the slowest partition, priced",
        "concepts_intro": (
            "One substitution — the maximum where the mean was expected — and three "
            "consequences that all point the same way."
        ),
        "concepts": [
            ("The job's distribution is the maximum's distribution",
             "If a job is done when every partition is done, then `P(job ≤ t)` is the "
             "probability that all `N` partitions came in at or under `t`, which is "
             "`P(one ≤ t)ᴺ` under independence. That single line gives the whole "
             "distribution of the job time from the distribution of one partition, and "
             "the lab enumerates it exactly rather than sampling it."),
            ("More partitions make the mean job time larger, not smaller",
             "Each partition's own time distribution does not change when you add "
             "partitions; what changes is how many draws the maximum is taken over. With "
             "the lab's distribution the job mean goes `25.80`, `41.61`, `88.73`, "
             "`111.63`, `130.62` ms at `N = 1, 4, 16, 24, 32`. The work per partition "
             "shrinking is a separate effect, and it is not what this arithmetic is "
             "measuring."),
            ("A rare tail becomes the common case",
             "The `400 ms` outcome has weight `5` in a thousand — half a per cent of "
             "partitions. `P(no partition past 120 ms) = 0.995ᴺ`, which is `0.990` at "
             "`N = 2` and `0.985` at `N = 3`, so from three partitions on, `400 ms` "
             "<em>is</em> the job's p99. The lab finds that crossing by exact search over "
             "`N` rather than from a logarithm."),
        ],
        "read_title": "The maximum of N, enumerated",
        "read_intro": (
            "Where the maximum comes from, how to get its distribution exactly, what it "
            "does as `N` grows, and the separate effect that makes anybody believe "
            "partitions are free."
        ),
        "body": [
            ("def", ("Straggler",
                     "In a job that must wait for every partition, the "
                     "<strong>straggler</strong> is the partition that finishes last. The "
                     "job's completion time is that partition's completion time, so the "
                     "job's running time is `max(T₁, …, T_N)` where `Tᵢ` is partition `i`'s "
                     "time. The <strong>straggler tax</strong> is the ratio of the job's "
                     "mean time to one partition's mean time.")),
            ("p", "The distribution of the maximum follows from one observation, and "
                  "the observation is about the complement. The maximum is at most `t` "
                  "exactly when every one of the `N` partitions is at most `t`; there is "
                  "no other way for the largest of them to be small. Under independence "
                  "that probability is the product, and since the partitions are drawing "
                  "from the same distribution it is a power."),
            ("math", [
                "P(max ≤ t) = P(T ≤ t)ᴺ        independent, identically distributed",
                "",
                "the lab's partition-time distribution, in ms",
                "  20 with weight 900     40 with 70     120 with 25     400 with 5",
                "",
                "one partition",
                "  mean = 0.900(20) + 0.070(40) + 0.025(120) + 0.005(400) = 25.80 ms",
                "  p99  = 120 ms          since P(T ≤ 40) = 0.970 and P(T ≤ 120) = 0.995",
                "",
                "the job over N = 24",
                "  mean = 111.63 ms       p99 = 400 ms",
                "  tax  = 111.63/25.80 = 4.33×",
                "  P(at least one past 120 ms) = 1 − 0.995²⁴ = 11.33%",
            ]),
            ("p", "Every figure above is exact. The distribution of the maximum over a "
                  "finite set of outcomes is a finite object, so the lab enumerates it "
                  "rather than simulating it — the `111.63 ms` is a sum over outcomes, "
                  "not an average over runs, and it will be the same number every time "
                  "you open the page."),
            ("h3", "What another partition actually buys"),
            ("p", "Two things happen when a job is spread over more partitions and they "
                  "point in opposite directions. Each partition has less work, which "
                  "shifts its own time distribution down; and the job takes a maximum "
                  "over more draws, which pushes the job time up. The first effect is "
                  "real, and it is why partitioning works at all. The second is what this "
                  "lesson measures, and it is the one nobody budgets for."),
            ("math", [
                "the same distribution, job time against partition count",
                "",
                "   N     mean (ms)    p50    p90    p99    P(job past 120 ms)",
                "   1        25.80      20     20    120        0.50%",
                "   2        31.32      20     40    120        1.00%",
                "   4        41.61      20    120    400        1.99%",
                "   8        59.70      40    120    400        3.93%",
                "  16        88.73      40    120    400        7.71%",
                "  24       111.63     120    400    400       11.33%",
                "  32       130.62     120    400    400       14.82%",
                "  64       185.43     120    400    400       27.44%",
                " 128       250.97     120    400    400       47.36%",
            ]),
            ("p", "The p99 column is the sharpest reading. One partition has a p99 of "
                  "`120 ms`; by `N = 4` the job's p99 is `400 ms`, the worst outcome in "
                  "the distribution, and it stays there for every larger `N`. Nothing "
                  "about the partitions got slower. The job simply takes enough draws "
                  "that the rarest outcome is no longer rare."),
            ("example", ("Reading the last column as a failure rate",
                         "`P(job past 120 ms)` is `0.50%` at one partition and `47.36%` "
                         "at 128. If `120 ms` is a timeout, the same code that succeeded "
                         "199 times in 200 as a single unit fails about half the time as "
                         "a 128-way job — and every one of those failures is a retry, "
                         "which “Retries and Request Amplification” prices. The "
                         "partition count did not change any component's reliability; it "
                         "changed how many components have to all be fast at once.")),
            ("h3", "What to do about it"),
            ("p", "Three responses, in increasing order of what they cost. Reduce the "
                  "tail of one partition, which moves the whole table at once and is "
                  "almost always the best value. Stop waiting for every partition where "
                  "the answer permits it — a job that can return on 95% of its partitions "
                  "is taking a much lower quantile of the same distribution. Or send the "
                  "slow partition somewhere else and take the first answer, which is "
                  "“Hedged Requests” and costs duplicate work."),
            ("p", "What does not help is adding partitions, and it is worth being "
                  "precise about why that differs from the two previous lessons. A hot "
                  "range and a hot key are skew: the work is unevenly distributed and the "
                  "arithmetic is about where it lands. A straggler needs no skew at all. "
                  "Every partition here draws from the same distribution and the job is "
                  "still four times slower than one partition, because the maximum of "
                  "many identical things is larger than any of them."),
        ],
        "lab": ("shard", {
            "mode": "straggler",
            "pmf": "20:900, 40:70, 120:25, 400:5",
            "partitions": 24,
            "panel_title": "Edit the partition-time distribution",
            "panel_intro": "Change the weight on the slowest outcome first — take `400:5` "
                           "down to `400:1` and watch the whole job column move — then put "
                           "it back and change the partition count instead. One of those "
                           "two dials is worth far more than the other, and the table says "
                           "which.",
        }),
        "steps_title": "Costing a job that waits for everything",
        "steps_intro": (
            "Get one partition's distribution first. Everything else on this page is "
            "computed from it, and a mean alone is not enough to compute anything."
        ),
        "steps": [
            ("Write down one partition's distribution, not just its mean",
             "You need the outcomes and their weights. A mean of `25.80 ms` is consistent "
             "with a job mean of `25.80 ms` and with one of `250 ms`, and which of those "
             "you get depends entirely on the tail that the mean hides."),
            ("Compute the job's distribution as `P(T ≤ t)ᴺ`",
             "For each candidate time, raise the single-partition cumulative probability "
             "to the power `N`. Over a finite set of outcomes this is a short table, and "
             "it gives the job's mean and every quantile at once."),
            ("Read the p99 and the tax separately",
             "The mean tells you throughput and the p99 tells you what a user or a "
             "timeout sees, and they move differently: at `N = 24` the mean is 4.33 times "
             "one partition's and the p99 has jumped to the distribution's worst outcome. "
             "Quote both."),
            ("Compare the tail-reduction lever against the partition-count lever",
             "Halve the weight on the slowest outcome and recompute; then add partitions "
             "and recompute. On this distribution the first improves every row of the "
             "table and the second makes the job slower. Do that comparison before "
             "choosing a partition count, not after."),
        ],
        "worked": {
            "title": "A 24-way job over a distribution with a half-per-cent tail",
            "intro": [
                "One partition first, exactly; then the job; then the question of where "
                "the job's p99 came from.",
            ],
            "lines": [
                "one partition, times in ms with weights out of 1 000",
                "  20:900   40:70   120:25   400:5",
                "",
                "  mean = 0.900(20) + 0.070(40) + 0.025(120) + 0.005(400)",
                "       = 18.0 + 2.8 + 3.0 + 2.0 = 25.80 ms",
                "  P(T ≤  20) = 0.900     P(T ≤  40) = 0.970",
                "  P(T ≤ 120) = 0.995     P(T ≤ 400) = 1.000      so p99 = 120 ms",
                "",
                "the job over N = 24",
                "  P(job ≤ 120) = 0.995²⁴ = 0.8867      so p99 is above 120 ms",
                "  P(job ≤ 400) = 1                      so p99 = 400 ms",
                "  mean = 111.63 ms                      tax = 111.63/25.80 = 4.33×",
                "  P(at least one past 120 ms) = 1 − 0.8867 = 11.33%",
                "",
                "where the job's p99 starts being 400 ms",
                "  N = 2:  0.995² = 0.990025 ≥ 0.99      p99 = 120 ms",
                "  N = 3:  0.995³ = 0.985075 < 0.99      p99 = 400 ms",
            ],
            "after": [
                "Three partitions. That is where a 0.5% outcome stops being a tail and "
                "becomes the number a p99 reports, and it is found by evaluating "
                "`0.995ᴺ` rather than by any rule of thumb about long tails.",
                "For a faded rehearsal, keep the same outcomes and take the weights to "
                "`20:940, 40:40, 120:15, 400:5` — a tighter middle with the same slow "
                "tail. The supplied first move is the new single-partition mean. Produce "
                "the job's mean and p99 at `N = 24`, then say whether the p99 moved and "
                "why, and then predict what would have happened instead if you had "
                "halved the weight on `400` and left the middle alone. Check both in the "
                "lab.",
            ],
        },
        "quiz_title": "Maxima, tails and partition counts",
        "quiz": [
            {"q": "One partition averages `25.80 ms`. A job waits for 24 of them. What does the job average?",
             "a": ["`25.80 ms`, because the partitions run in parallel",
                   "`619.2 ms`, which is `24 × 25.80`",
                   "`111.63 ms`, the mean of the maximum of 24 draws",
                   "`400 ms`, the slowest outcome"],
             "c": 2,
             "why": "The job is the maximum, not the mean and not the sum. Running in "
                    "parallel is why it is not `619.2 ms`; waiting for all of them is why "
                    "it is not `25.80 ms`. `400 ms` is the job's p99 at this `N`, which "
                    "is a different statistic of the same distribution."},
            {"q": "The same job is spread over 32 partitions instead of 24. What happens to the job's mean time, holding each partition's own distribution fixed?",
             "a": ["It falls to about `83.7 ms`, in proportion to the extra partitions",
                   "It is unchanged, because the partitions are independent",
                   "It rises to `130.62 ms`, because the maximum is over more draws",
                   "It falls to `55.8 ms`"],
             "c": 2,
             "why": "Holding each partition's time distribution fixed, more partitions "
                    "means a maximum over more draws, and the maximum grows. The "
                    "proportional answers assume the job time is work divided by "
                    "partitions, which is the effect that makes partitioning worth doing "
                    "and is not what this table is measuring."},
            {"q": "The `400 ms` outcome has probability `0.005`. From what partition count is `400 ms` the job's p99?",
             "a": ["From `N = 3`, because `0.995³ = 0.985 &lt; 0.99` while `0.995² = 0.990 ≥ 0.99`",
                   "From `N = 200`, since `1/0.005 = 200`",
                   "From `N = 24`, where the lab reports it",
                   "Never; a 0.5% outcome cannot be a p99"],
             "c": 0,
             "why": "`P(job ≤ 120) = 0.995ᴺ`, and the p99 is above `120 ms` as soon as "
                    "that drops below `0.99`. Two partitions are just inside; three are "
                    "outside. `N = 24` is where the lab happens to be set, and `200` is "
                    "the reciprocal of the probability, which answers a different "
                    "question."},
            {"q": "Which change improves this job most, and why?",
             "a": ["Doubling the partition count, which halves the work per partition",
                   "Halving the weight on the `400 ms` outcome, which moves every row of the job table",
                   "Doubling the weight on the `20 ms` outcome, which improves the mean",
                   "Nothing can improve it; the maximum is a property of `N`"],
             "c": 1,
             "why": "The job is a maximum, so it is dominated by the slow tail: reducing "
                    "the probability of the worst outcome moves the job's mean and its "
                    "p99 together. Doubling the partition count makes the job slower on "
                    "this arithmetic. Adding weight to the fast outcome helps the mean "
                    "far less than removing weight from the slow one, because `0.995ᴺ` is "
                    "what the p99 turns on."},
        ],
        "mistakes": [
            ("Budgeting a job at its partitions' mean",
             "One partition averaging `25.80 ms` gives a 24-way job averaging "
             "`111.63 ms` — a tax of 4.33 times. Any latency budget that adds up "
             "per-partition means has understated the parallel stage by whatever the "
             "maximum costs, and “Serial Sums, Parallel Maxes” is the rule that was "
             "skipped."),
            ("Expecting partition count to buy time linearly",
             "Twice the partitions halves the work each one does and doubles the number "
             "of draws the maximum is over. Past the point where the second effect wins, "
             "more partitions make the job slower — `111.63 ms` at 24 becomes "
             "`130.62 ms` at 32 on this distribution."),
            ("Dismissing a half-per-cent outcome as a tail",
             "At `N = 3` a 0.5% outcome is already the job's p99, and at `N = 128` it "
             "happens in nearly half of all jobs. The probability that matters is not the "
             "outcome's own but `1 − (1 − p)ᴺ`, and `N` is usually large enough to make "
             "that a different number entirely."),
        ],
        "standard": ("Finish when a fan-out stage in a latency budget makes you ask for a distribution rather than a mean.",
                     "You should be able to compute a job's mean and quantiles from one "
                     "partition's distribution and a count, find the `N` at which a rare "
                     "outcome becomes the p99, and say which of tail reduction, partial "
                     "results and hedging you would reach for first."),
        "note": (
            "The maximum over `N` draws is the shape of this half of the course. The next "
            "lesson takes the same object and changes one rule of the game: let each key "
            "look at two shards instead of one before it settles, and the maximum "
            "collapses from a logarithm to a logarithm of a logarithm. “The Power of Two "
            "Choices” measures it."
        ),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-power-of-two-choices",
        "title": "The Power of Two Choices",
        "module": "The maximum of N",
        "one_line": "Measure the maximum load under one random choice and under the lesser of two, from the same stream, and reseed.",
        "summary": (
            "Placing each key in a single random shard leaves a maximum load of about "
            "`ln n / ln ln n`. Sampling two shards and taking the lesser-loaded one leaves "
            "about `ln ln n` — a logarithm replaced by the logarithm of a logarithm, for "
            "the cost of one extra lookup. Both of those results are stated and not "
            "proved anywhere in this library, so what this lesson does is measure them on "
            "placements you can reproduce."
        ),
        "key": [
            "1 024 keys into 1 024 bins, one stream, seed 3",
            "  one choice    fullest bin 5        two choices   fullest bin 3",
            "  seeds 3–10    mean 5.25            seeds 3–10    mean 3.00",
            "",
            "ln n / ln ln n = 3.58        ln ln n = 1.94      at n = 1 024, rounded",
            "both asymptotics are stated, not proved — anywhere in this library",
        ],
        "key_label": "Two placements from one stream, and two results nobody here proves",
        "concepts_intro": (
            "The rule is one sentence and the effect is out of all proportion to it, "
            "which is why the honest thing to do with the theory is to state it and "
            "measure the rest."
        ),
        "concepts": [
            ("The rule: sample `d` bins, take the lesser-loaded",
             "Instead of hashing a key to one shard and placing it there, hash it to `d` "
             "shards, look at how full each of them is, and put the key in the least full. "
             "At `d = 2` that is one extra lookup per placement and no coordination "
             "between placements. The lab runs both rules from the same stream of draws, "
             "so the comparison is not confounded by the randomness."),
            ("The improvement is exponential in the wrong direction to be intuitive",
             "The one-choice maximum grows like `ln n / ln ln n`, which is `3.58` at "
             "`n = 1 024` and `5.27` at `n = 1 048 576`. The two-choice maximum grows "
             "like `ln ln n`, which is `1.94` and `2.63` at the same two sizes. Taking a "
             "logarithm of a quantity that was already a logarithm is why doubling `n` "
             "barely moves the second column at all."),
            ("`d = 2` gets essentially all of it",
             "The obvious next thought is that scanning every bin would be better still. "
             "It is, marginally: the gain from one choice to two is the collapse, and the "
             "gain from two to a full least-loaded search is small. Over seeds 3 to 10 "
             "the lab's one-choice maximum averaged `5.25` and the two-choice maximum was "
             "`3` on every single seed. The expensive part of the rule is the first extra "
             "look."),
        ],
        "read_title": "One extra look, and what it is worth",
        "read_intro": (
            "The rule, the two growth rates and their standing on this path, what the "
            "measurement shows, and why more than two choices is not the next step."
        ),
        "body": [
            ("def", ("Maximum load",
                     "For a placement of `m` keys into `n` bins, the "
                     "<strong>maximum load</strong> is the occupancy of the fullest bin. "
                     "The case of interest here is `m = n`, where the mean occupancy is "
                     "exactly 1 and the maximum is therefore entirely a statement about "
                     "the spread. The <strong>d-choice</strong> rule places each key in "
                     "the least loaded of `d` bins chosen at random for that key.")),
            ("p", "At `m = n` the mean is one key a bin, so any maximum above 1 is "
                  "imbalance and nothing else. That is what makes this the clean case to "
                  "measure: there is no scale in the answer, and a maximum of 5 means the "
                  "fullest bin holds five times what an even placement would give it."),
            ("math", [
                "1 024 keys into 1 024 bins, mean exactly 1 key a bin",
                "",
                "  seed      max, one choice    max, 2 choices    ratio",
                "     3             5                  3          1.67×",
                "     4             5                  3          1.67×",
                "     5             5                  3          1.67×",
                "     6             5                  3          1.67×",
                "     7             5                  3          1.67×",
                "     8             6                  3          2.00×",
                "     9             6                  3          2.00×",
                "    10             5                  3          1.67×",
                "  mean          5.25               3.00",
                "",
                "  bins left empty, seed 3:   377 under one choice, 243 under two",
            ]),
            ("p", "The second column is the striking one: eight seeds, eight maxima, and "
                  "every one of them is 3. One choice produced 5 or 6; two choices "
                  "produced 3 every time. The rule does not merely lower the maximum, it "
                  "makes it much less variable, which is the property a capacity plan "
                  "actually wants."),
            ("p", "The empty-bin counts are worth a glance too. Two choices left 243 bins "
                  "empty where one choice left 377, because a key that would have piled "
                  "onto a busy bin goes to a quieter one instead. The exact expectation "
                  "for the one-choice case, `n(1 − 1/n)ᵐ`, is computed on the Algorithms "
                  "path in “Balls in Bins and the Birthday Bound”; this lesson counts "
                  "rather than derives it."),
            ("h3", "The standing of the two results"),
            ("p", "The one-choice maximum load at `m = n` is "
                  "`Θ(log n / log log n)`, and sampling `d` bins instead of one replaces it "
                  "with a quantity growing like `log log n` — this course states and "
                  "measures the `d = 2` case as `ln ln n`, which is the figure the lab "
                  "prints. Both of those results are "
                  "<strong>stated, not proved</strong> — not in this lesson, "
                  "not on the Algorithms path, not anywhere in this library. Their proofs "
                  "need Chernoff bounds, which no subject here teaches, and the Algorithms "
                  "path's scope explicitly excludes them."),
            ("p", "So the numbers printed beside the measurements are quoted results "
                  "rather than derived ones, and they are quoted as floating-point "
                  "approximations: `ln n / ln ln n = 3.58` and `ln ln n = 1.94` at "
                  "`n = 1 024` are rounded, and the lab labels them where it prints them. "
                  "“Balls in Bins and the Birthday Bound” states the one-choice result "
                  "with the same caveat and computes the exact collision and empty-bin "
                  "expectations that this lesson does not; it points back here as the "
                  "place where the maximum load is what a system actually pays for."),
            ("example", ("What a stated rate can and cannot be used for",
                         "At `n = 1 024` the stated one-choice figure is `3.58` and the "
                         "measured maximum over eight seeds averaged `5.25`. Those do not "
                         "contradict each other: `Θ(log n / log log n)` is a growth rate "
                         "with constants suppressed, so it says how the maximum scales "
                         "and not what it equals at a particular `n`. Use the rate to "
                         "answer “what happens when the fleet is ten times bigger”, and "
                         "use the measurement to answer “what do I provision now”. "
                         "Substituting one for the other is the error this example "
                         "exists to prevent.")),
            ("h3", "Why not scan every bin"),
            ("p", "Because the benefit is nearly all in the first extra look, and the "
                  "cost of the search is not. A full least-loaded placement needs the "
                  "load of every bin at the moment of placement, which in a distributed "
                  "system means either a central allocator or a global view that is "
                  "stale by the time it is used — and a stale global view herds new keys "
                  "onto whichever bin looked emptiest, which is worse than either rule "
                  "here. Two random probes need no global state at all."),
            ("p", "The rule also has an obvious application outside key placement, and "
                  "it is the reason the result is famous: the same arithmetic governs a "
                  "load balancer choosing between backends. Sampling two backends and "
                  "sending the request to the one with fewer outstanding requests gets "
                  "most of the benefit of least-loaded balancing with none of its "
                  "coordination, which is exactly the trade above with keys replaced by "
                  "requests."),
        ],
        "lab": ("shard", {
            "mode": "twochoice",
            "balls": 1024,
            "choices": 2,
            "seed": 3,
            "panel_title": "Give each key a second look",
            "panel_intro": "Both placements are run from the same stream of draws, so the "
                           "difference you see is the rule and not the randomness. Step "
                           "the seed through eight values and watch the two-choice maximum "
                           "refuse to move, then take `d` to 4 and notice how little the "
                           "second improvement is worth.",
        }),
        "steps_title": "Measuring a placement rule",
        "steps_intro": (
            "Two placements, one stream, several seeds — and a clear label on which "
            "numbers were measured and which were quoted."
        ),
        "steps": [
            ("Fix `m = n` so the mean is exactly 1",
             "With as many keys as bins the mean occupancy is one and the maximum is "
             "pure imbalance. Any other ratio mixes the spread with a scale and makes two "
             "rules harder to compare."),
            ("Run both rules from the same draws",
             "The comparison is between placement rules, so the stream must be shared. "
             "Running each rule from its own seed leaves you comparing two samples as "
             "well as two rules, and at these sizes the sampling difference is the same "
             "size as the effect."),
            ("Reseed, and record the maxima separately",
             "One choice gave 5 or 6 across eight seeds; two choices gave 3 on all eight. "
             "The spread is part of the result — a rule with a stable maximum is worth "
             "more to a capacity plan than one with the same mean and a wider range."),
            ("Put the stated rate beside the measurement, labelled",
             "Write `ln n / ln ln n = 3.58 (stated, rounded)` next to `5.25 (measured, "
             "eight seeds)`. They are different kinds of claim, and keeping them in "
             "adjacent columns with their labels is what stops the asymptotic being "
             "quoted as a provisioning figure."),
        ],
        "worked": {
            "title": "1 024 keys into 1 024 bins, one choice against two",
            "intro": [
                "One seeded run of each rule, then the same comparison over eight seeds, "
                "then the two quoted rates beside them.",
            ],
            "lines": [
                "m = n = 1 024, so the mean is exactly 1 key a bin",
                "",
                "seed 3, one stream, both rules",
                "  one choice     fullest bin = 5        empty bins = 377",
                "  two choices    fullest bin = 3        empty bins = 243",
                "",
                "seeds 3 through 10",
                "  one choice     5, 5, 5, 5, 5, 6, 6, 5      mean 5.25",
                "  two choices    3, 3, 3, 3, 3, 3, 3, 3      mean 3.00",
                "",
                "the stated rates at n = 1 024, rounded, proved nowhere here",
                "  one choice     ln n / ln ln n = 3.58",
                "  two choices    ln ln n        = 1.94",
                "",
                "measured improvement    5.25 → 3.00, a factor of 1.75",
                "cost                    one extra bin lookup per key",
            ],
            "after": [
                "The stated rates are smaller than the measurements and that is expected: "
                "they are growth rates with their constants suppressed, and they are being "
                "evaluated at a single, fairly small `n`. What they are for is the "
                "comparison between the two columns rather than the value of either.",
                "For a faded rehearsal, take `n` to 4 096 with `d = 2` and reseed four "
                "times. The supplied first move is the two stated rates at that size — "
                "`ln n / ln ln n = 3.93` and `ln ln n = 2.12`. Record both measured "
                "maxima, say how much each moved relative to `n = 1 024`, and then state "
                "which of the two columns moved by roughly the amount its stated rate "
                "predicted. Label every figure you write down as measured or stated.",
            ],
        },
        "quiz_title": "Two choices, measured and stated",
        "quiz": [
            {"q": "1 024 keys are placed into 1 024 bins from one stream, seed 3. What are the maximum loads under one choice and under two?",
             "a": ["`5` and `3`", "`3.58` and `1.94`", "`1` and `1`", "`5.25` and `3.00`"],
             "c": 0,
             "why": "The measured maxima on that seed are 5 and 3. `3.58` and `1.94` are "
                    "the stated asymptotics at `n = 1 024`, which are rates rather than "
                    "counts and are not what any placement produced. `5.25` and `3.00` "
                    "are the averages over seeds 3 to 10. `1` is the mean occupancy, not "
                    "the maximum."},
            {"q": "What is the standing of `Θ(log n / log log n)` and `ln ln n` on this path?",
             "a": ["Both are proved in this lesson from the placements",
                   "Both are proved on the Algorithms path and quoted here",
                   "Both are stated, not proved anywhere in this library, because their proofs need Chernoff bounds that no subject here teaches",
                   "The first is proved and the second is stated"],
             "c": 2,
             "why": "“Balls in Bins and the Birthday Bound” on the Algorithms path states "
                    "the one-choice result under the same caveat, and that course's scope "
                    "excludes Chernoff bounds, which is what the proof requires. So both "
                    "results are stated in two places and established in neither, and "
                    "what the labs do instead is measure them."},
            {"q": "Someone proposes scanning all 1 024 bins and always placing into the least loaded. What does the measurement suggest about that?",
             "a": ["It would roughly halve the maximum again, from 3 to about 1.5",
                   "It would buy little: `d = 2` already gave 3 on every one of eight seeds, and the mean is 1",
                   "It would be worse than two choices",
                   "It is the only way to reach a maximum of 3"],
             "c": 1,
             "why": "The collapse is between one choice and two; a full search is bounded "
                    "below by the mean of 1 and two choices is already at 3 with no "
                    "variation across seeds. It also needs every bin's load at the moment "
                    "of placement, which in a distributed system is either a central "
                    "allocator or a stale global view — and a stale view herds keys onto "
                    "whichever bin last looked empty."},
            {"q": "The stated one-choice rate at `n = 1 024` is `3.58` and the measured maximum averaged `5.25`. What does that mean?",
             "a": ["The measurement is wrong",
                   "The stated rate is wrong",
                   "Nothing is wrong: `Θ(·)` suppresses constants, so the rate describes how the maximum scales and not its value at one `n`",
                   "The lab used a different number of bins"],
             "c": 2,
             "why": "A growth rate with suppressed constants cannot be evaluated for a "
                    "provisioning figure; it answers “what happens when `n` grows”. The "
                    "measurement answers “what should I provision at this `n`”. The lab "
                    "prints them in adjacent columns with labels precisely so that "
                    "neither gets used for the other's question."},
        ],
        "mistakes": [
            ("Quoting an asymptotic as a capacity figure",
             "`ln n / ln ln n = 3.58` at `n = 1 024` is a rate with its constants "
             "dropped, and the measured maximum averaged `5.25`. Provision from the "
             "measurement and reason about growth from the rate. A plan built on `3.58` "
             "is short by a third and looks rigorous."),
            ("Believing the result must need a full least-loaded search",
             "The whole point is that two random probes get essentially all of it — "
             "eight seeds, a maximum of 3 every time — with no global state. Reaching for "
             "the full search costs coordination and, if the global view is stale, "
             "produces herding that is worse than one random choice."),
            ("Comparing the two rules on different seeds",
             "Run both from the same stream. At `n = 1 024` the seed-to-seed variation in "
             "the one-choice maximum is 5 to 6, which is the same order as the effect "
             "being measured, so a comparison across seeds can report almost anything."),
        ],
        "standard": ("Finish when you can state both results, say that neither is proved here, and still use them.",
                     "You should be able to run and read both placements, quote the "
                     "measured maxima with the number of seeds behind them, write the "
                     "stated rates beside them with the word “stated”, and explain why "
                     "`d = 2` rather than `d = n` is the engineering answer."),
        "note": (
            "That is the last of the placement lessons. What remains is the cost of "
            "queries and operations that cannot be routed to a single shard, and the first "
            "of them is the one that makes a fleet's request rate go up rather than down: "
            "“Scatter-Gather Cost” prices a query that has to ask every shard."
        ),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "scatter-gather-cost",
        "title": "Scatter-Gather Cost",
        "module": "Crossing shards",
        "one_line": "Compute the shard requests a second and the query latency tail for a query that must ask every shard.",
        "summary": (
            "A query whose predicate is not the partition key cannot be routed, so it "
            "goes to all `N` shards and waits for the last answer. Both halves of that "
            "sentence cost something: the fleet's request rate is multiplied by `N`, and "
            "the query's latency is the maximum of `N` shard latencies rather than one of "
            "them. The partition count is the same dial for both, and for how many "
            "consumers can read in parallel."
        ),
        "key": [
            "shard requests = N × query rate      24 × 400/s = 9 600/s",
            "a routed query would leave                          400/s",
            "amplification = N                                    24×",
            "",
            "query latency = max of N shard latencies",
            "one shard's p99 90 ms   →   the query's p99 250 ms at N = 24",
            "consumer parallelism ≤ N             the same dial as the fan-out",
        ],
        "key_label": "One query, N requests, and the slowest of N waits",
        "concepts_intro": (
            "Two costs from one fan-out, plus a third consequence of the partition count "
            "that is easy to forget because it lives on a different team's diagram."
        ),
        "concepts": [
            ("Sharding divides the work per query and multiplies the requests",
             "Both are true and only one of them is usually said. Each shard does "
             "`1/N` of the scan, which is why the query is fast at all; and the fleet "
             "receives `N` requests where it used to receive one. At 24 shards and 400 "
             "queries a second that is `9 600` shard requests a second against the `400` "
             "a routed query would leave — and it is the second number that sizes "
             "connection pools, thread pools and every per-request cost in the system."),
            ("The query waits for the slowest shard",
             "This is the maximum of “Stragglers” in a different costume. A shard whose "
             "own p99 is `90 ms` gives a 24-way query a p99 of `250 ms`, because the "
             "query is fast only if all 24 were fast. The lab computes the query's "
             "distribution exactly from the per-shard one and also samples it from a "
             "seeded run, and the two agree at `250 ms`."),
            ("The partition count is one dial with three effects",
             "Raising `N` reduces per-shard work, raises the fleet's request rate, "
             "worsens the latency tail, and raises the ceiling on how many consumers can "
             "read the data in parallel — that ceiling is `N` itself, because a partition "
             "is the unit of consumption. Choosing `N` for any one of those in isolation "
             "is how a system ends up with a tail nobody chose."),
        ],
        "read_title": "What an unrouted query costs",
        "read_intro": (
            "Why some queries cannot be routed, what the fan-out does to the request rate "
            "and to the tail, and what else the partition count is quietly deciding."
        ),
        "body": [
            ("def", ("Scatter-gather",
                     "A <strong>scatter-gather</strong> query is one whose predicate does "
                     "not determine the shard, so the router sends it to all `N` shards "
                     "(<strong>scatter</strong>) and combines the partial results "
                     "(<strong>gather</strong>). A <strong>routed</strong> query names the "
                     "partition key and goes to one shard. The <strong>request "
                     "amplification</strong> of a scatter-gather is `N`: shard requests "
                     "per client query.")),
            ("p", "Which queries are unroutable is decided by the partitioning function "
                  "and nothing else. Partition by user and “everything for user 91” is "
                  "routed while “everything created yesterday” is a scatter; partition by "
                  "day and the two swap. Every partitioning choice makes one family of "
                  "queries cheap and the rest of them scatters, which is why the choice "
                  "belongs with the access patterns rather than with the data model."),
            ("math", [
                "N = 24 shards, 400 client queries a second",
                "",
                "  shard requests   = 24 × 400 = 9 600 /s",
                "  amplification    = 24×",
                "  routed instead   = 400 /s",
                "",
                "per-shard latency, in ms with weights out of 100",
                "  10:80   25:15   90:4   250:1",
                "",
                "  one shard    mean 17.85 ms    p50 10    p90 25    p99  90 ms",
                "  the query    N = 24                                p99 250 ms",
                "               exact 250 ms, and 250 ms in a seeded run of 400 queries",
            ]),
            ("p", "The amplification is the figure that surprises people, because the "
                  "sentence “we sharded, so each node does less work” is true and is not "
                  "the whole of it. Each node does less work <em>per query</em>; the node "
                  "receives `N` times as many queries, so a fleet serving 400 client "
                  "queries a second is handling `9 600` requests a second. Everything that "
                  "is priced per request — a connection, a lock acquisition, a log line, a "
                  "tracing span — is multiplied by 24."),
            ("h3", "The tail, again"),
            ("math", [
                "the same per-shard distribution, against the shard count",
                "",
                "   N     shard requests /s    query mean (ms)    p50    p90    p99",
                "   1            400               17.85           10     25     90",
                "   2            800               24.92           10     25    250",
                "   4          1 600               37.22           25     90    250",
                "   8          3 200               56.72           25     90    250",
                "  16          6 400               84.74           90    250    250",
                "  24          9 600              105.24           90    250    250",
                "  32         12 800              121.40           90    250    250",
                "  64         25 600              163.47           90    250    250",
            ]),
            ("p", "At two shards the query's p99 is already `250 ms` — the worst outcome "
                  "in the per-shard distribution — because `0.99² = 0.9801`, which is "
                  "below the `0.99` a p99 needs. By sixteen shards the p90 has reached "
                  "`250 ms` too. The per-shard distribution never changed; the query is "
                  "simply asking more shards to all be fast at once, and "
                  "“Tail Amplification under Fan-out” is the same calculation stated in "
                  "general."),
            ("example", ("The third effect: consumer parallelism",
                         "A partition is also the unit of parallel consumption. If a "
                         "downstream reader wants to process this dataset with more than "
                         "`N` workers, it cannot: worker `N + 1` has no partition to read, "
                         "and at `N = 24` the ceiling is 24 regardless of how much "
                         "hardware is available. So the partition count that was chosen "
                         "for storage and load has also set a limit on a pipeline nobody "
                         "in that conversation was thinking about, and raising it later "
                         "means the rehash of “Rehashing When N Changes”.")),
            ("h3", "What to do instead"),
            ("p", "The direct fix is to make the query routable, by partitioning on the "
                  "attribute it filters on — which usually means another copy of the data "
                  "partitioned differently, and that is exactly the global secondary index "
                  "of the next lesson. Failing that, the levers are the ones from "
                  "“Stragglers”: narrow the per-shard tail, accept a partial result, or "
                  "hedge. What does not help is raising `N`, which makes both costs worse."),
            ("p", "It is worth writing the two numbers down together whenever a "
                  "scatter-gather is proposed, because they trade against each other in a "
                  "way that a single figure hides. `9 600` requests a second is a capacity "
                  "question and `250 ms` is a latency question; a fleet can be sized for "
                  "the first and still fail the second, and a tail fix that adds hedged "
                  "requests makes the first worse."),
        ],
        "lab": ("shard", {
            "mode": "scatter",
            "shards": 24,
            "query_rate": 400,
            "pmf": "10:80, 25:15, 90:4, 250:1",
            "seed": 9,
            "panel_title": "Ask every shard, and count what that costs",
            "panel_intro": "The amplification and the tail are on the screen together "
                           "because they are the same decision. Move the shard count and "
                           "watch the request rate rise while the p99 climbs to the worst "
                           "outcome in the per-shard distribution — and notice how few "
                           "shards it takes for that to happen.",
        }),
        "steps_title": "Pricing an unrouted query",
        "steps_intro": (
            "Two numbers, always both. A scatter-gather that has been costed only for "
            "capacity or only for latency has been costed for neither."
        ),
        "steps": [
            ("Establish that the query really cannot be routed",
             "A query is unroutable when its predicate does not determine the partition "
             "key. If it does determine it and the router is not using it, that is a "
             "routing bug and none of this arithmetic applies."),
            ("Multiply the query rate by `N` for the fleet's request rate",
             "`N × rate` is what the shards receive, and it is the number that sizes "
             "connection pools, per-request overheads and anything billed per call. Write "
             "the routed rate beside it so the multiple is visible."),
            ("Compute the query's tail from the per-shard distribution",
             "`P(query ≤ t) = P(shard ≤ t)ᴺ`. Take the p99 and compare it with one "
             "shard's p99. At the lab's numbers those are `250 ms` and `90 ms`, and the "
             "gap is the whole cost of the fan-out on the latency side."),
            ("Check what else `N` has decided",
             "Consumer parallelism is capped at `N`, and the rehash cost of changing `N` "
             "later is `N/(N+1)` of the dataset under mod assignment. Both belong in the "
             "same decision, because both are hard to revisit once the data is placed."),
        ],
        "worked": {
            "title": "400 queries a second against 24 shards",
            "intro": [
                "The request rate first, because it is a multiplication; then the tail, "
                "because it is not.",
            ],
            "lines": [
                "N = 24, client query rate = 400 /s",
                "",
                "requests",
                "  shard requests = 24 × 400 = 9 600 /s",
                "  routed would be             400 /s        amplification 24×",
                "",
                "per-shard latency, ms with weights out of 100",
                "  10:80   25:15   90:4   250:1",
                "  mean = 0.80(10) + 0.15(25) + 0.04(90) + 0.01(250)",
                "       = 8 + 3.75 + 3.6 + 2.5 = 17.85 ms",
                "  P(shard ≤ 25) = 0.95     P(shard ≤ 90) = 0.99      so p99 = 90 ms",
                "",
                "the query",
                "  P(query ≤ 90) = 0.99²⁴ = 0.7857      below 0.99, so p99 is above 90",
                "  P(query ≤ 250) = 1                   so the query's p99 = 250 ms",
                "  seeded run of 400 queries also reports 250 ms",
                "",
                "and where the p99 first reached 250 ms",
                "  N = 2:  0.99² = 0.9801 < 0.99        already there",
            ],
            "after": [
                "Two shards. The p99 of a fan-out query reaches the worst per-shard "
                "outcome at `N = 2` with this distribution, which is worth holding on to: "
                "the tail cost of scatter-gather is not something that arrives at large "
                "fleet sizes, it arrives immediately.",
                "For a faded rehearsal, keep 24 shards and narrow the per-shard tail to "
                "`10:80, 25:16, 90:4` — the `250 ms` outcome removed entirely. The "
                "supplied first move is the new per-shard p99, which is still `90 ms`. "
                "Compute the query's p99 at `N = 24`, say how much the fleet's request "
                "rate changed, and then state which of the two costs of scatter-gather "
                "that change addressed and which it left exactly where it was.",
            ],
        },
        "quiz_title": "Amplification and the tail",
        "quiz": [
            {"q": "400 client queries a second each visit all 24 shards. What request rate do the shards see in total?",
             "a": ["`400 /s`", "`9 600 /s`", "`16.7 /s`", "`24 /s`"],
             "c": 1,
             "why": "`N × rate = 24 × 400 = 9 600 /s`. `400 /s` is what a routed query "
                    "would leave. `16.7 /s` is `400/24`, which divides where the fan-out "
                    "multiplies — that is the per-shard share of one query's work, not a "
                    "rate of requests."},
            {"q": "One shard's p99 is `90 ms`. What is the p99 of a query that must wait for all 24?",
             "a": ["`90 ms`", "`250 ms`", "`2 160 ms`", "`17.85 ms`"],
             "c": 1,
             "why": "`P(query ≤ 90) = 0.99²⁴ = 0.786`, well below the `0.99` a p99 needs, "
                    "so the p99 moves to the next outcome, `250 ms`. `2 160 ms` is "
                    "`24 × 90`, which would be the answer if the shards ran one after "
                    "another. `17.85 ms` is one shard's mean."},
            {"q": "“Sharding reduces the load on each node, so it reduces load overall.” What is wrong with the second half?",
             "a": ["Nothing; both halves are true",
                   "The first half is also false — each node does the same work",
                   "Each node does `1/N` of a query's work, but the fleet receives `N` requests per query, so the total request rate rises by `N`",
                   "Load cannot be compared across different shard counts"],
             "c": 2,
             "why": "Work per query per node falls and the number of requests rises, and "
                    "those are different quantities. Anything priced per request — a "
                    "connection, a lock, a log line, a tracing span — is multiplied by "
                    "`N`, which is why the fleet's request rate went from `400 /s` to "
                    "`9 600 /s` while each shard's share of any one query went down."},
            {"q": "A downstream pipeline wants to read this dataset with 64 parallel workers. The data is in 24 partitions. What can it achieve?",
             "a": ["64-way parallelism, since workers and partitions are independent",
                   "24-way parallelism, because a partition is the unit of consumption",
                   "Unlimited parallelism, if the workers coordinate",
                   "One worker, because a scatter-gather is serial"],
             "c": 1,
             "why": "The partition count caps consumer parallelism at `N`; the 25th "
                    "worker has nothing to read. It is the same dial as the fan-out and "
                    "the amplification, which is why the partition count deserves to be "
                    "chosen once, deliberately, with all three consequences on the table."},
        ],
        "mistakes": [
            ("Costing the fan-out for capacity and not for latency, or the reverse",
             "`9 600 /s` and `250 ms` are both consequences of the same `N` and neither "
             "implies the other. A fleet sized comfortably for the request rate can still "
             "miss its latency target by a factor of three, and a tail fix built from "
             "hedged requests makes the request rate worse."),
            ("Expecting the tail cost to arrive only at large fleet sizes",
             "With the lab's per-shard distribution, the query's p99 is already at the "
             "worst per-shard outcome at two shards, because `0.99²` is below `0.99`. "
             "Fan-out tail amplification is not a big-cluster problem; it starts at the "
             "second shard."),
            ("Raising the shard count to make a scatter-gather faster",
             "It raises the request rate proportionally and pushes the tail further out, "
             "and each shard's smaller slice rarely compensates. The fixes are to make "
             "the query routable, to narrow the per-shard tail, or to stop waiting for "
             "every shard."),
        ],
        "standard": ("Finish when a proposed scatter-gather makes you write down two numbers before anything else.",
                     "You should be able to compute the amplified request rate and the "
                     "query's tail from a per-shard distribution, say at what shard count "
                     "the tail reached the worst per-shard outcome, and name what else "
                     "the partition count has decided."),
        "note": (
            "The standing answer to an unroutable query is to keep a second copy of the "
            "data partitioned by the attribute the query filters on. That is a global "
            "secondary index, and it is not free either: it turns a scatter on every read "
            "into an extra write on every write. “Local vs Global Secondary Indexes” "
            "prices both and finds the ratio at which they change places."
        ),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "local-vs-global-secondary-indexes",
        "title": "Local vs Global Secondary Indexes",
        "module": "Crossing shards",
        "one_line": "Compute the shard operations a second for both index designs and the read-to-write ratio at which they change places.",
        "summary": (
            "A local secondary index lives beside the data it indexes, so a write touches "
            "one shard and a lookup has to ask all `N`. A global secondary index is "
            "partitioned by the indexed attribute, so a lookup goes to one shard and a "
            "write has to touch two. The costs are `r·N + w` against `r + 2w`, they are "
            "equal at `r/w = 1/(N − 1)`, and which of them is cheaper is a fact about the "
            "workload rather than about the designs."
        ),
        "key": [
            "local    read all N shards, write 1        cost = r·N + w",
            "global   read 1 shard,       write 2       cost = r + 2w",
            "equal when r·N + w = r + 2w   ⟺   r/w = 1/(N − 1)",
            "",
            "r = 5 000/s, w = 2 000/s, N = 16",
            "  local 82 000 ops/s     global 9 000 ops/s     global cheaper by 9.11×",
            "  crossover 1/15 = 0.0667      this workload is r/w = 2.500",
        ],
        "key_label": "Two costs, and the ratio where they meet",
        "concepts_intro": (
            "Two designs, one algebraic comparison, and a crossover that depends on the "
            "fleet size and on nothing else."
        ),
        "concepts": [
            ("A local index puts the scatter on the read",
             "The index entry for a row lives on the same shard as the row, so writing a "
             "row writes its index entry locally — one shard touched. But the index is "
             "then spread across every shard, so a lookup by the indexed attribute has no "
             "idea which shards hold matches and must ask all `N`. Cost per second: "
             "`r·N + w`."),
            ("A global index puts the cost on the write",
             "The index is partitioned by the indexed attribute, so a lookup goes "
             "straight to the one shard holding that attribute's entries. The price is "
             "that a write now touches two shards — the row's own and the index's — and "
             "those are on different machines, which brings the consistency questions of "
             "the lesson after next. Cost per second: `r + 2w`."),
            ("The crossover is `1/(N − 1)`, and it depends only on `N`",
             "Setting `r·N + w = r + 2w` gives `r(N − 1) = w`, so the two designs cost "
             "the same when `r/w = 1/(N − 1)`. At two shards that is `r/w = 1`: any "
             "workload with more reads than writes wants the global index. At sixteen "
             "shards it is `1/15 = 0.0667`, so a workload with one indexed read per "
             "fifteen writes already prefers the global index. The larger the fleet, the "
             "smaller the read share that tips it."),
        ],
        "read_title": "Two indexes, two costs, one ratio",
        "read_intro": (
            "What each design does on a read and on a write, the algebra that puts them "
            "in the same units, where they cross, and what the comparison leaves out."
        ),
        "body": [
            ("def", ("Secondary index",
                     "A <strong>secondary index</strong> maps a non-key attribute to the "
                     "rows carrying it. In a partitioned store it can be "
                     "<strong>local</strong> — each shard indexes only its own rows — or "
                     "<strong>global</strong>, partitioned by the indexed attribute so "
                     "that all entries for one value live together. The primary key's own "
                     "index is neither; it is the partitioning function.")),
            ("p", "The two designs are the same data structure placed differently, and "
                  "the placement decides which operation pays. What makes the comparison "
                  "tractable is that both costs can be measured in the same unit — shard "
                  "operations a second, meaning the total number of per-shard requests the "
                  "fleet performs — so a read that fans out to sixteen shards counts as "
                  "sixteen."),
            ("math", [
                "r = indexed reads a second      w = writes a second      N = shards",
                "",
                "  local    r · N  +  w          every read asks all N, every write is local",
                "  global   r      +  2w         every read is routed, every write is doubled",
                "",
                "r = 5 000 /s, w = 2 000 /s, N = 16",
                "",
                "  local    5 000 × 16 + 2 000 = 80 000 + 2 000 = 82 000 ops/s",
                "  global   5 000 + 2 × 2 000  =  5 000 + 4 000 =  9 000 ops/s",
                "  ratio    82 000/9 000 = 9.11×      the global index wins here",
            ]),
            ("h3", "Where they cross"),
            ("math", [
                "r·N + w = r + 2w",
                "r·N − r = 2w − w",
                "r(N − 1) = w",
                "r/w = 1/(N − 1)",
                "",
                "  N        crossover r/w    as a decimal    cheaper at r/w = 2.5",
                "   2         1/1              1.0000          global",
                "   4         1/3              0.3333          global",
                "   8         1/7              0.1429          global",
                "  16         1/15             0.0667          global",
                "  32         1/31             0.0323          global",
                "  64         1/63             0.0159          global",
            ]),
            ("p", "Read the middle column down and the shape of the trade is obvious. At "
                  "two shards the two designs meet at equal reads and writes, which is a "
                  "genuinely balanced decision. By sixty-four shards they meet at one read "
                  "per sixty-three writes, so any workload that reads the indexed "
                  "attribute at all is already past the crossover. The local index is a "
                  "design for small fleets and write-dominated workloads, and the "
                  "arithmetic says so without any appeal to taste."),
            ("example", ("A workload on the other side of the line",
                         "Take an audit log partitioned by record id, indexed on a status "
                         "field, with `w = 10 000 /s` of writes and `r = 200 /s` of "
                         "status lookups across `N = 4` shards. The local index costs "
                         "`200 × 4 + 10 000 = 10 800` ops/s and the global costs "
                         "`200 + 20 000 = 20 200` — the local index is cheaper by nearly "
                         "two to one. The ratio is `r/w = 0.02`, comfortably below the "
                         "crossover of `1/3`, and the same two formulas that chose the "
                         "global index in the lab choose the local one here.")),
            ("h3", "What the ratio does not capture"),
            ("p", "Three things, and all of them push the same way. A local index read is "
                  "a scatter-gather, so it also carries the tail of “Scatter-Gather Cost” "
                  "— `N` requests and a wait for the slowest — while a global index read "
                  "is one routed request with one shard's latency. A global index write "
                  "touches two shards, so unless it is done in a transaction it is "
                  "briefly inconsistent with the row, and doing it in a transaction is the "
                  "cross-shard commit of the next lesson. And the global index has its own "
                  "hot-key problem: all entries for one attribute value live on one shard, "
                  "so a heavily skewed attribute reproduces “Hot Keys and Salting” inside "
                  "the index."),
            ("p", "So `r·N + w` against `r + 2w` is the first cut and not the whole "
                  "decision. It is worth doing first anyway, because it is arithmetic on "
                  "two numbers you already have, and when it comes out at nine to one "
                  "the qualitative arguments are unlikely to reverse it."),
        ],
        "lab": ("shard", {
            "mode": "index",
            "reads": 5000,
            "writes": 2000,
            "shards": 16,
            "panel_title": "Set the workload mix, then move the fleet size",
            "panel_intro": "Take the read rate down until the local index wins, and note "
                           "how far down it has to go. Then hold the workload and move the "
                           "shard count instead: the crossover is `1/(N − 1)` and it "
                           "collapses toward zero, which is why fleet size decides this "
                           "argument more often than workload does.",
        }),
        "steps_title": "Choosing an index design",
        "steps_intro": (
            "Two rates and a shard count. Compute the crossover before either cost — it "
            "is one division and it usually settles the question on its own."
        ),
        "steps": [
            ("Write down `r`, `w` and `N`",
             "`r` is reads <em>that use the index</em>, not all reads; a lookup by "
             "primary key is routed and is irrelevant here. `w` is writes that change the "
             "indexed attribute, which may be fewer than all writes."),
            ("Compute the crossover `1/(N − 1)` and compare it with `r/w`",
             "One division each. If `r/w` is above the crossover the global index is "
             "cheaper and if it is below the local one is, and at `N = 16` the crossover "
             "is `0.0667` against a workload ratio of `2.500` — not a close call."),
            ("Compute both costs anyway, to size the fleet",
             "`r·N + w` and `r + 2w` in shard operations a second. The winner's figure is "
             "what the fleet has to serve, and the ratio between them — `9.11×` at the "
             "lab's numbers — is what the decision is worth."),
            ("Check the three things the ratio leaves out",
             "The local index inherits the scatter-gather tail; the global index needs "
             "two shards written and can be hot on a skewed attribute. If any of those "
             "is decisive the arithmetic has not changed, but the answer might."),
        ],
        "worked": {
            "title": "5 000 indexed reads and 2 000 writes a second, on 16 shards",
            "intro": [
                "Both costs, then the crossover, then the same workload on a fleet small "
                "enough to change the answer.",
            ],
            "lines": [
                "r = 5 000 /s     w = 2 000 /s     N = 16",
                "",
                "  local    r·N + w = 5 000 × 16 + 2 000 = 82 000 shard ops/s",
                "  global   r + 2w  = 5 000 + 4 000      =  9 000 shard ops/s",
                "  global is cheaper by 82 000/9 000 = 9.11×",
                "",
                "the crossover",
                "  r·N + w = r + 2w   ⟹   r(N − 1) = w   ⟹   r/w = 1/(N − 1)",
                "  at N = 16:  1/15 = 0.0667",
                "  this workload: r/w = 5 000/2 000 = 2.500, far above it",
                "",
                "what would have to change for the local index to win",
                "  hold w = 2 000 /s and N = 16:  r must fall below 2 000/15 = 133 /s",
                "  that is 1 indexed read for every 15 writes",
            ],
            "after": [
                "The last block is the useful way to report this. “The global index wins” "
                "is a conclusion; “the global index wins unless indexed reads fall below "
                "133 a second” is a conclusion with a margin attached, and it is the "
                "version that survives a workload changing after the decision is made.",
                "For a faded rehearsal, take the same workload to a four-shard fleet. The "
                "supplied first move is the crossover, `1/(4 − 1) = 1/3`. Compute both "
                "costs, say which wins and by how much, and then find the read rate at "
                "which the answer would flip. Say in one sentence why the margin is so "
                "much narrower here than at sixteen shards.",
            ],
        },
        "quiz_title": "Index costs and crossovers",
        "quiz": [
            {"q": "`r = 5 000 /s`, `w = 2 000 /s`, `N = 16`. What does the local index cost in shard operations a second?",
             "a": ["`9 000`", "`82 000`", "`7 000`", "`80 000`"],
             "c": 1,
             "why": "`r·N + w = 5 000 × 16 + 2 000 = 82 000`. `9 000` is the global "
                    "index's `r + 2w`. `7 000` is `r + w`, which counts each operation "
                    "once and so describes neither design. `80 000` is `r·N` with the "
                    "write forgotten."},
            {"q": "At what read-to-write ratio do the two designs cost the same on a 16-shard fleet?",
             "a": ["`r/w = 1/15`", "`r/w = 16`", "`r/w = 1/16`", "`r/w = 2`"],
             "c": 0,
             "why": "`r·N + w = r + 2w` gives `r(N − 1) = w`, so `r/w = 1/(N − 1) = "
                    "1/15 ≈ 0.0667`. The off-by-one matters: `1/16` would be `1/N`, and "
                    "the `−1` is there because one of the global index's two writes is "
                    "the row write the local design also performs."},
            {"q": "A team argues that global secondary indexes are simply the better design. What does the arithmetic say?",
             "a": ["It agrees; `r + 2w` is smaller than `r·N + w` whenever `N` is above 2",
                   "It disagrees: below `r/w = 1/(N − 1)` the local index is cheaper, and at `N = 4` that is one read per three writes",
                   "It agrees for reads and disagrees for writes, so the comparison is undecidable",
                   "It disagrees only for `N = 1`"],
             "c": 1,
             "why": "Neither design wins in general. A write-heavy workload with a rare "
                    "lookup — an audit log indexed on status, say — sits below the "
                    "crossover and prefers the local index, and at small `N` the crossover "
                    "is high enough for that to be a common situation. What is true is "
                    "that the crossover falls like `1/(N − 1)`, so large fleets push "
                    "almost everything toward the global design."},
            {"q": "Besides the operation counts, what does a local index read inherit?",
             "a": ["Nothing; the operation count is the whole cost",
                   "The scatter-gather tail: `N` requests and a wait for the slowest of them",
                   "The cost of two-phase commit",
                   "A hot-key problem on the indexed attribute"],
             "c": 1,
             "why": "A local index lookup is a scatter-gather, so it carries the "
                    "amplification and the maximum-of-`N` latency of the previous lesson. "
                    "Two-phase commit is what a global index's two-shard write may need, "
                    "and the hot-key problem belongs to the global design, where every "
                    "entry for one attribute value lands on one shard."},
        ],
        "mistakes": [
            ("Writing the crossover as `1/N`",
             "It is `1/(N − 1)`. The `−1` comes from the row write that both designs "
             "perform: `r·N + w = r + 2w` reduces to `r(N − 1) = w`, not `r·N = w`. At "
             "small `N` the difference is large — `1/1` against `1/2` at two shards — and "
             "that is exactly the regime where the decision is close."),
            ("Counting all reads as indexed reads",
             "`r` is reads that go through the secondary index. A lookup by primary key "
             "is routed by the partitioning function and costs one shard operation under "
             "either design. Inflating `r` with primary-key traffic pushes the "
             "arithmetic toward the global index for a reason that does not exist."),
            ("Taking the operation count as the whole comparison",
             "The local index read is also a scatter-gather with the tail that implies; "
             "the global index write touches two shards and is briefly inconsistent "
             "unless committed together; and a skewed indexed attribute makes the global "
             "index hot in exactly one place. Do the arithmetic first, then check all "
             "three."),
        ],
        "standard": ("Finish when “local or global?” is a division you perform rather than a preference you hold.",
                     "You should be able to write both costs in shard operations a "
                     "second, derive the crossover `1/(N − 1)` from them, report which "
                     "design wins with the margin that would flip it, and name the three "
                     "costs the ratio does not include."),
        "note": (
            "A global index write touches two shards, and writing two shards together "
            "raises the question this course has been deferring: what does it cost to make "
            "an operation over several shards atomic? “Cross-shard Transactions” answers "
            "it in two parts — how often a transaction crosses, which is a counting "
            "problem, and what crossing costs, which is round trips and fsyncs."
        ),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "cross-shard-transactions",
        "title": "Cross-shard Transactions",
        "module": "Crossing shards",
        "one_line": "Compute the fraction of k-key transactions that cross shards and the mean latency two-phase commit adds to every transaction.",
        "summary": (
            "`k` randomly hashed keys all land on one shard with probability `N¹⁻ᵏ`, "
            "which collapses in `k` rather than in `N`: at two shards a two-key "
            "transaction already crosses half the time. Everything that crosses pays "
            "two-phase commit — two round trips and extra fsyncs — and the cost that "
            "belongs in a latency budget is that price multiplied by the crossing "
            "probability."
        ),
        "key": [
            "P(k random keys all on one shard) = N¹⁻ᵏ",
            "",
            "k = 2, N = 2     1/2 local — half of them cross at the very first shard",
            "k = 2, N = 16    1/16 = 6.25% local,  93.75% cross",
            "k = 3, N = 16    1/256 = 0.39% local",
            "E[shards touched] = N(1 − (1 − 1/N)ᵏ) = 1.938 of 16 at k = 2",
            "2PC adds 2 round trips + 2 fsyncs = 4.00 + 1.00 = 5.00 ms per crossing",
        ],
        "key_label": "How often it crosses, and what crossing costs",
        "concepts_intro": (
            "A counting question and a latency question, kept apart until the last step "
            "where one multiplies the other."
        ),
        "concepts": [
            ("`N¹⁻ᵏ` collapses in `k`, not in `N`",
             "Fix the first key's shard; each of the remaining `k − 1` keys joins it with "
             "probability `1/N`, so all `k` agree with probability `N¹⁻ᵏ`. `N` appears "
             "once and `k` appears in the exponent, so adding a key is worth far more "
             "than adding shards: at `N = 16`, going from two keys to three takes the "
             "local fraction from `6.25%` to `0.39%`."),
            ("The smallest case ends the argument",
             "At `N = 2` and `k = 2` the probability of staying local is `1/2`. One extra "
             "shard — the first one anybody adds — already sends half of all two-key "
             "transactions across a boundary. Nobody has to reach a large fleet before "
             "this matters, which is why “most of our transactions are local” is worth "
             "checking rather than assuming."),
            ("The cost in a budget is the price times the probability",
             "A crossing transaction pays two-phase commit: a prepare round and a commit "
             "round, plus an fsync on each. At `2.00 ms` a round trip and `0.50 ms` an "
             "fsync that is `5.00 ms`. But `6.25%` of transactions are local and pay none "
             "of it, so the figure that belongs in a mean latency budget is "
             "`0.9375 × 5.00 = 4.688 ms` — and the figure that belongs in a tail budget "
             "is the full `5.00 ms`."),
        ],
        "read_title": "How often it crosses, and what it costs when it does",
        "read_intro": (
            "The counting argument, what it does as `k` and `N` move, the protocol that "
            "the crossing transactions run, and how to put the two together without "
            "double-counting."
        ),
        "body": [
            ("def", ("Cross-shard transaction",
                     "A transaction is <strong>local</strong> when every key it touches "
                     "lives on one shard, and <strong>cross-shard</strong> otherwise. A "
                     "local transaction commits with the store's ordinary single-node "
                     "path. A cross-shard one needs an atomic commitment protocol across "
                     "the participants, and <strong>two-phase commit</strong> is the "
                     "standard one: a prepare round in which every participant durably "
                     "votes, then a commit round.")),
            ("thm", ("The local fraction",
                     "If `k` keys are hashed independently and uniformly over `N` shards, "
                     "the probability that all of them land on the same shard is "
                     "`N¹⁻ᵏ`.")),
            ("proof", [
                "Condition on the shard of the first key, whatever it is. Each of the "
                "remaining `k − 1` keys is independently uniform over the `N` shards, so "
                "each lands on that same shard with probability `1/N`.",
                "By independence the probability that all `k − 1` of them do is "
                "`(1/N)ᵏ⁻¹ = N¹⁻ᵏ`, and this does not depend on which shard the first "
                "key chose, so it is the unconditional probability as well.",
                "At `k = 1` this gives `N⁰ = 1`, which is the right answer: a "
                "single-key transaction is always local.",
            ]),
            ("math", [
                "P(all k on one shard) = N¹⁻ᵏ",
                "",
                "  N        k = 2, local     crosses      shards touched   added latency",
                "   2       1/2   50.00%      50.00%           1.500          2.500 ms",
                "   4       1/4   25.00%      75.00%           1.750          3.750 ms",
                "   8       1/8   12.50%      87.50%           1.875          4.375 ms",
                "  16       1/16   6.25%      93.75%           1.938          4.688 ms",
                "  32       1/32   3.13%      96.88%           1.969          4.844 ms",
                "  64       1/64   1.56%      98.44%           1.984          4.922 ms",
                "",
                "  and in k, at N = 16",
                "  k = 2   1/16    = 6.2500%       k = 3   1/256  = 0.3906%",
                "  k = 4   1/4096  = 0.0244%",
            ]),
            ("p", "The first table's second column barely changes after the first few "
                  "rows — `93.75%` at sixteen shards and `98.44%` at sixty-four — which "
                  "is what “collapses in `k`, not in `N`” looks like from the other side. "
                  "Once `N` is past a handful, essentially every multi-key transaction "
                  "crosses, and the remaining question is only what crossing costs."),
            ("p", "The expected number of shards a transaction touches is a different "
                  "count and a useful one: it is `N(1 − (1 − 1/N)ᵏ)`, which at `k = 2` and "
                  "`N = 16` is `1.938`. That is the number of participants the commit "
                  "protocol coordinates, and it stays close to `k` for any `N` much "
                  "larger than `k`. A two-key transaction on a large fleet is a two-"
                  "participant commit almost always, which is why the protocol's cost "
                  "does not grow with the fleet."),
            ("h3", "What two-phase commit adds"),
            ("math", [
                "round trip between shards = 2.00 ms      an fsync = 0.50 ms",
                "",
                "  prepare   1 round trip + 1 fsync at each participant",
                "  commit    1 round trip + 1 fsync at each participant",
                "",
                "  round trips   2 × 2.00 = 4.00 ms",
                "  fsyncs        2 × 0.50 = 1.00 ms",
                "  total         5.00 ms per crossing transaction",
                "",
                "  mean over ALL transactions at k = 2, N = 16",
                "    0.9375 × 5.00 = 4.688 ms",
            ]),
            ("p", "Two numbers, two purposes. `5.00 ms` is what a crossing transaction "
                  "pays and it belongs in a tail budget, because at `93.75%` crossing "
                  "the p99 transaction certainly crosses. `4.688 ms` is the mean over all "
                  "transactions and belongs in a throughput calculation. Quoting the mean "
                  "where the tail is wanted understates the p99 by the 6.25% of "
                  "transactions that got off free."),
            ("example", ("Why the fsyncs are worth itemising separately",
                         "The round-trip term scales with distance and the fsync term "
                         "does not. Move the participants into one rack and the `4.00 ms` "
                         "may fall by an order of magnitude while the `1.00 ms` of "
                         "durable votes stays exactly where it is; move them across "
                         "regions and the round trips dominate everything. Itemising the "
                         "two means the same model answers both questions, and “The "
                         "Speed-of-Light Floor” gives the round trip a lower bound that no "
                         "amount of engineering moves.")),
            ("h3", "The designs that avoid the question"),
            ("p", "Every practical answer is a way of making `k = 1` rather than a way of "
                  "making two-phase commit cheap. Partition by the entity the transaction "
                  "is about — orders by customer, posts by author — so that a transaction "
                  "touching several rows touches one shard. Or deliberately co-locate "
                  "related keys by giving them a shared partition key prefix, which is the "
                  "same idea stated as a schema choice. Both are decisions about the "
                  "partitioning function, and both are much harder to make after the data "
                  "is placed."),
            ("p", "Where the transaction genuinely spans entities, the remaining levers "
                  "are to weaken what is being asked for — an eventually-consistent "
                  "compensating action instead of an atomic commit — or to accept the "
                  "`5.00 ms` and make sure it is in the budget. What is not a lever is the "
                  "shard count: `N¹⁻ᵏ` is already near zero at any `N` worth having, and "
                  "the protocol's cost does not depend on `N` at all."),
        ],
        "lab": ("shard", {
            "mode": "crossshard",
            "keys_per_txn": 2,
            "shards": 16,
            "rtt_us": 2000,
            "fsync_us": 500,
            "panel_title": "Spread a transaction over k keys",
            "panel_intro": "Set the shard count to 2 before anything else and read the "
                           "local fraction — one half, at the smallest fleet that can be "
                           "called partitioned. Then move `k` rather than `N` and watch "
                           "how much faster the exponent works than the base.",
        }),
        "steps_title": "Budgeting for transactions that cross",
        "steps_intro": (
            "One probability, one protocol cost, and a multiplication — with the mean and "
            "the tail kept apart at the end."
        ),
        "steps": [
            ("Count the keys a transaction touches, and check they are independently hashed",
             "`k` is the number of distinct partition keys, not the number of rows or "
             "statements. If the keys are deliberately co-located under a shared prefix "
             "then they are not independent, `N¹⁻ᵏ` does not apply, and the transaction "
             "is local by construction — which is the good case."),
            ("Compute `N¹⁻ᵏ`, and its complement",
             "`N¹⁻ᵏ` is the local fraction and `1 − N¹⁻ᵏ` is what crosses. Sanity-check "
             "at `k = 1`, where it must give 1. At `k = 2`, `N = 16` the crossing "
             "fraction is `93.75%`, so the interesting number is the complement rather "
             "than the probability itself."),
            ("Itemise the protocol cost — round trips and fsyncs separately",
             "Two round trips and two fsyncs for two-phase commit. Keep them apart: "
             "`4.00 ms` of round trips responds to where the participants are, and "
             "`1.00 ms` of fsyncs responds to what the storage does."),
            ("Multiply for the mean, and use the unmultiplied figure for the tail",
             "Mean added latency is `(1 − N¹⁻ᵏ) × protocol cost`, which is `4.688 ms` at "
             "the lab's numbers. The p99 transaction crosses, so its added latency is the "
             "full `5.00 ms`. Put the right one in the right budget."),
        ],
        "worked": {
            "title": "Two keys over sixteen shards, and then over two",
            "intro": [
                "The probability, the participants, the protocol cost, and the two "
                "latency figures that come out of them.",
            ],
            "lines": [
                "k = 2 keys, N = 16 shards, round trip 2.00 ms, fsync 0.50 ms",
                "",
                "  P(local)  = N¹⁻ᵏ = 16⁻¹ = 1/16 = 6.2500%",
                "  P(crosses)                     = 93.7500%",
                "  E[shards touched] = 16(1 − (15/16)²) = 16 × 31/256 = 31/16 = 1.938",
                "",
                "  two-phase commit",
                "    round trips  2 × 2.00 = 4.00 ms",
                "    fsyncs       2 × 0.50 = 1.00 ms",
                "    per crossing transaction  5.00 ms",
                "",
                "  mean over all transactions   0.9375 × 5.00 = 4.688 ms",
                "  p99 transaction              crosses, so                5.00 ms",
                "",
                "the smallest fleet there is",
                "  k = 2, N = 2:   P(local) = 2⁻¹ = 1/2",
                "  mean added latency = 0.5 × 5.00 = 2.500 ms",
            ],
            "after": [
                "The last two lines are the ones to carry away. At the very first shard "
                "anybody adds, half of all two-key transactions are already crossing — the "
                "problem does not wait for a large fleet, and by sixteen shards the "
                "crossing fraction has only gone from a half to `93.75%`.",
                "For a faded rehearsal, keep `N = 16` and take `k` to 3. The supplied "
                "first move is the local probability, `16⁻² = 1/256`. Produce the crossing "
                "fraction, the expected number of participants, and the mean added "
                "latency; then say which of those three changed most between `k = 2` and "
                "`k = 3`, and whether raising `N` to 64 would have changed any of them "
                "comparably.",
            ],
        },
        "quiz_title": "Crossing fractions and commit costs",
        "quiz": [
            {"q": "A transaction touches 2 independently hashed keys on a 16-shard store. What is the probability it stays on one shard?",
             "a": ["`1/16 = 6.25%`", "`1/256 = 0.39%`", "`1/8 = 12.5%`", "`15/16 = 93.75%`"],
             "c": 0,
             "why": "`N¹⁻ᵏ = 16¹⁻² = 16⁻¹ = 1/16`. `1/256` is the answer for three keys. "
                    "`15/16` is the complement — the fraction that crosses. Fixing the "
                    "first key's shard and asking only about the second is what makes the "
                    "exponent `k − 1` rather than `k`."},
            {"q": "At the smallest partitioned fleet there is — 2 shards — what fraction of two-key transactions cross?",
             "a": ["A quarter", "A half", "An eighth", "None, because two shards can hold both keys"],
             "c": 1,
             "why": "`N¹⁻ᵏ = 2⁻¹ = 1/2` stay local, so a half cross. This is the figure "
                    "that ends the argument that “most of our transactions will be "
                    "local”: it is already untrue at the first shard added, before any of "
                    "the scaling that people imagine causes the problem."},
            {"q": "A round trip is `2.00 ms` and an fsync is `0.50 ms`. What does two-phase commit add to a crossing transaction, and what belongs in a mean latency budget at `k = 2`, `N = 16`?",
             "a": ["`5.00 ms` and `5.00 ms`",
                   "`2.50 ms` and `2.50 ms`",
                   "`5.00 ms` for a crossing transaction, and `4.688 ms` as the mean over all transactions",
                   "`4.688 ms` for a crossing transaction, and `5.00 ms` as the mean"],
             "c": 2,
             "why": "Two round trips and two fsyncs are `4.00 + 1.00 = 5.00 ms`, paid by "
                    "the `93.75%` that cross. The mean over all transactions is "
                    "`0.9375 × 5.00 = 4.688 ms`. The tail budget wants the first figure, "
                    "because a p99 transaction at this crossing rate has certainly "
                    "crossed."},
            {"q": "Which change most reduces the number of transactions that cross?",
             "a": ["Raising the shard count from 16 to 64",
                   "Lowering the shard count from 16 to 8",
                   "Partitioning so that the keys a transaction touches share a shard, making `k` effectively 1",
                   "Reducing the round-trip time between shards"],
             "c": 2,
             "why": "`N¹⁻ᵏ` is already `6.25%` at sixteen shards and moving `N` barely "
                    "shifts the crossing fraction — `93.75%` to `98.44%` going up, and to "
                    "`87.50%` going down. Co-locating the keys makes the transaction "
                    "local by construction. A faster round trip reduces what crossing "
                    "costs, which is a different and also useful lever."},
        ],
        "mistakes": [
            ("Writing the exponent as `k` rather than `k − 1`",
             "`N¹⁻ᵏ` comes from fixing the first key's shard for free and asking the "
             "other `k − 1` to match it. At `k = 1` the formula must return 1, which is "
             "the check that catches the slip: `N⁻¹` would say a single-key transaction "
             "crosses, which is nonsense."),
            ("Assuming most transactions stay local",
             "At two shards a two-key transaction crosses half the time, and at sixteen "
             "shards it crosses `93.75%` of the time. The assumption is not "
             "approximately right and then degrading; it is wrong at the first shard. "
             "Compute `N¹⁻ᵏ` before designing around it."),
            ("Putting the mean added latency into a tail budget",
             "`4.688 ms` is the average over transactions including the `6.25%` that pay "
             "nothing. The p99 transaction has crossed and pays the whole `5.00 ms`. The "
             "two figures are a few per cent apart here and much further apart when the "
             "crossing fraction is low, which is precisely when the substitution is most "
             "tempting."),
        ],
        "standard": ("Finish when “the transaction spans two entities” makes you reach for `N¹⁻ᵏ` before anything else.",
                     "You should be able to compute the local and crossing fractions for "
                     "any `k` and `N`, state the expected number of participants, itemise "
                     "two-phase commit into round trips and fsyncs, and produce a mean and "
                     "a tail figure that are not the same number."),
        "note": (
            "One cost remains, and it is the one that turns every earlier decision into "
            "hours of wall clock: changing `N`. “Rebalancing Cost” multiplies the fraction "
            "of keys that move — the `N/(N+1)` or `1/(N+1)` of “Rehashing When N Changes” "
            "— by the dataset and divides by a throttle, and then prices the utilisation "
            "the copy holds the fleet at while it runs."
        ),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "rebalancing-cost",
        "title": "Rebalancing Cost",
        "module": "Crossing shards",
        "one_line": "Compute how long a rebalance takes at a given throttle and the utilisation the fleet runs at while it does.",
        "summary": (
            "Moving a fraction `m` of a `D`-byte dataset at a throttled bandwidth `B` "
            "takes `m·D/B`, which at the lab's defaults is sixteen hours and forty "
            "minutes. That is not idle time: the copy is holding a share of each node's "
            "transfer budget, so the node serves fewer requests and its utilisation rises "
            "for the whole window — and the wait at the higher utilisation is three times "
            "the wait at the lower one. Turning the throttle up shortens the window and "
            "makes the utilisation worse, and past a point it puts it above one."
        ),
        "key": [
            "duration = m · D / B      0.25 × 48 TB = 12.00 TB at 200 MB/s",
            "                          = 60 000 s = 16 h 40 min",
            "the copy holds B/budget of the node:  200/800 = 1/4",
            "so the node serves 6 000/s instead of 8 000/s",
            "ρ goes 62.50% → 83.33%      M/M/1 wait 0.333 ms → 1.000 ms, a factor of 3.00",
            "at 400 MB/s the window halves and ρ passes 1",
        ],
        "key_label": "A duration, and the utilisation it is bought at",
        "concepts_intro": (
            "One division for the duration and one subtraction for the capacity, and the "
            "two are joined by a dial that moves them in opposite directions."
        ),
        "concepts": [
            ("The duration is bytes over bandwidth, and nothing is hidden in it",
             "`m · D` is the bytes that must move and `B` is the rate they move at, so "
             "the window is their quotient. At `m = 25%` of `48 TB` that is `12.00 TB`, "
             "and at `200 MB/s` it is `60 000` seconds — sixteen hours and forty minutes. "
             "A terabyte here is `10¹²` bytes and a MB/s is `10⁶` bytes a second, which is "
             "how both a disk and a throttle are sold."),
            ("The copy is capacity the node is no longer serving with",
             "A node has a finite transfer budget, and whatever the rebalance takes from "
             "it is not available for serving. At `200 MB/s` out of `800 MB/s` the copy "
             "holds a quarter, so a node that served `8 000 /s` now serves `6 000 /s`. "
             "The arrival rate did not change, so utilisation goes from `62.50%` to "
             "`83.33%` and stays there until the copy finishes."),
            ("The throttle moves the two costs in opposite directions",
             "Turn it up and the window shortens and the utilisation worsens; turn it "
             "down and the reverse. At `50 MB/s` the move takes two days and eighteen "
             "hours and forty minutes at `ρ = 66.67%`; at `200 MB/s` it takes sixteen hours and forty "
             "minutes at `83.33%`; at `400 MB/s` it takes eight hours and twenty minutes "
             "and the node can no longer serve the arriving load at all. There is no "
             "setting that is cheap on both axes."),
        ],
        "read_title": "How long it takes, and what it costs while it runs",
        "read_intro": (
            "The duration, the capacity the copy steals, what that does to the wait, and "
            "the setting at which shortening the window stops being an option."
        ),
        "body": [
            ("def", ("Rebalance",
                     "A <strong>rebalance</strong> moves a fraction `m` of the stored data "
                     "between nodes, because the shard count changed, because a node was "
                     "added or lost, or because the placement became uneven. The "
                     "<strong>throttle</strong> `B` is the bandwidth the copy is allowed "
                     "to use, and it is a deliberate limit rather than a property of the "
                     "hardware: the whole reason to set one is that the node has other "
                     "work to do.")),
            ("p", "Where `m` comes from is the earlier lesson. Under `mod N` assignment a "
                  "growth step moves `N/(N+1)` of the keys — at seven shards going to "
                  "eight, `87.50%` of the dataset — and on a ring it moves `1/(N+1)`, or "
                  "`12.50%`. The `25%` in the lab's defaults is a middling figure that "
                  "could come from either a ring on a small fleet or a deliberate "
                  "re-spread; what this lesson does is turn any such fraction into hours "
                  "and a utilisation."),
            ("math", [
                "m = 25%, D = 48 TB, B = 200 MB/s, node budget 800 MB/s",
                "λ at the node = 5 000 /s, service rate μ = 8 000 /s",
                "",
                "  bytes to move   = 0.25 × 48 TB            = 12.00 TB",
                "  duration        = 12 × 10¹² / (200 × 10⁶) = 60 000 s = 16 h 40 min",
                "",
                "  capacity taken  = 200/800                 = 1/4 = 25.00%",
                "  service during  = 8 000 × (1 − 1/4)       = 6 000 /s",
                "",
                "  ρ before        = 5 000/8 000             = 62.50%",
                "  ρ during        = 5 000/6 000             = 83.33%",
                "",
                "  M/M/1 wait  W = 1/(μ − λ)",
                "  before          = 1/(8 000 − 5 000)       = 0.333 ms",
                "  during          = 1/(6 000 − 5 000)       = 1.000 ms      3.00×",
            ]),
            ("p", "The wait figures are not new arithmetic. They are “The M/M/1 Queue” "
                  "evaluated at two utilisations, and the reason a 21-point rise in `ρ` "
                  "triples the wait is the knee that “The Knee: Response Time vs "
                  "Utilisation” describes: the response time rises without bound as `ρ` "
                  "approaches 1, so equal steps in utilisation are not equal steps in "
                  "latency. A rebalance is a decision to sit further up that curve for a "
                  "measured number of hours."),
            ("h3", "Turning the throttle"),
            ("math", [
                "the same move, at six throttles",
                "",
                "  throttle     duration          capacity taken    ρ during    wait",
                "   50 MB/s     2 d 18 h 40 min        6.3%          66.67%     0.400 ms",
                "  100 MB/s     1 d  9 h 20 min       12.5%          71.43%     0.500 ms",
                "  200 MB/s         16 h 40 min       25.0%          83.33%     1.000 ms",
                "  400 MB/s          8 h 20 min       50.0%          past capacity",
                "  800 MB/s          4 h 10 min      100.0%          past capacity",
            ]),
            ("p", "The fourth row is the one to look at. Halving the window from sixteen "
                  "hours to eight takes half the node's transfer budget, which leaves it "
                  "serving `4 000 /s` against an arrival rate of `5 000 /s`. That is not "
                  "a slower system; it is a queue that grows without bound for as long as "
                  "the copy runs, and “Transient Overload and Draining the Backlog” is "
                  "what happens afterwards. The throttle has a hard ceiling and it is "
                  "reached well before the hardware's."),
            ("example", ("The same rebalance, priced two ways",
                         "“Moving 12 TB takes about seventeen hours” is the version that "
                         "gets said in a planning meeting. The version that describes what "
                         "will actually happen is “for sixteen hours and forty minutes, "
                         "every node's utilisation is `83.33%` instead of `62.50%` and the "
                         "queueing wait is three times normal” — and if there is a latency "
                         "objective, that is the sentence it has to be checked against. "
                         "The duration is the easy half of the cost and it is the half "
                         "that gets reported.")),
            ("h3", "What this makes cheaper elsewhere"),
            ("p", "Run the arithmetic on the two fractions from “Rehashing When N "
                  "Changes” and the argument for consistent hashing stops being "
                  "theoretical. Growing a seven-shard fleet under `mod N` moves `7/8` of "
                  "48 TB — `42 TB`, which at `200 MB/s` is `2 d 10 h 20 min` at "
                  "`ρ = 83.33%` throughout. The same growth step on a ring moves `1/8`, "
                  "or `6 TB`, which is eight hours and twenty minutes. The identity "
                  "`7/8 + 1/8 = 1` is, in the end, a statement about how many days of "
                  "elevated latency a growth step costs."),
            ("p", "It also prices the choice of `V` from “Virtual Nodes” and the decision "
                  "to reshard from “Hot Keys and Salting”. A rebalance is the operation "
                  "that every structural change on this course eventually has to pay for, "
                  "which is why it is worth computing before the change rather than after "
                  "it — the duration and the utilisation are both available from numbers "
                  "you already have."),
        ],
        "lab": ("shard", {
            "mode": "rebalance",
            "moved_pct": 25,
            "data_tb": 48,
            "throttle_mbs": 200,
            "budget_mbs": 800,
            "node_rps": 5000,
            "service_rps": 8000,
            "panel_title": "Move a fraction of the data, and watch what it costs",
            "panel_intro": "Try to shorten the window. Push the throttle up and watch the "
                           "duration fall and the utilisation climb, and find the setting "
                           "at which the node stops being able to serve the arriving load "
                           "at all — it is closer to the default than it looks.",
        }),
        "steps_title": "Planning a rebalance",
        "steps_intro": (
            "Compute the duration, then the utilisation, then check the second one "
            "against whatever latency objective exists. The order matters because the "
            "first number is the one that tempts you to stop."
        ),
        "steps": [
            ("Get `m` from the change you are making, not from a guess",
             "Under `mod N` assignment a growth step moves `N/(N+1)`; on a ring it moves "
             "about `1/(N+1)`; a deliberate re-spread moves whatever you choose. The "
             "fraction is the largest single lever in this calculation and it is decided "
             "by a design choice made much earlier."),
            ("Divide bytes by the throttle for the window",
             "`m · D / B`, in consistent units — a TB is `10¹²` bytes and a MB/s is "
             "`10⁶` bytes a second. `12 TB` at `200 MB/s` is `60 000` seconds. Report it "
             "in hours, because that is the unit the decision is made in."),
            ("Compute the service rate and the utilisation during the move",
             "The copy takes `B/budget` of the node's transfer capacity, so the effective "
             "service rate is `μ(1 − B/budget)` and `ρ` during the move is `λ` over that. "
             "If the result is at or above 1, the throttle is too high and nothing else "
             "in the plan matters."),
            ("Check the wait at that `ρ` against the latency objective",
             "`W = 1/(μ − λ)` at the reduced service rate. Here it triples, from "
             "`0.333 ms` to `1.000 ms`, and it stays tripled for sixteen hours and forty "
             "minutes. That is the sentence the plan needs, and it is the one that decides "
             "whether the rebalance happens at this throttle or a lower one."),
        ],
        "worked": {
            "title": "A quarter of 48 TB, throttled to 200 MB/s",
            "intro": [
                "The window first, then what the node looks like while it is open, then "
                "what happens if you try to close it faster.",
            ],
            "lines": [
                "m = 25%    D = 48 TB    B = 200 MB/s    budget = 800 MB/s",
                "λ = 5 000 /s    μ = 8 000 /s",
                "",
                "the window",
                "  bytes    = 0.25 × 48 × 10¹²           = 12 × 10¹² = 12.00 TB",
                "  duration = 12 × 10¹² / (200 × 10⁶)    = 60 000 s  = 16 h 40 min",
                "",
                "the node while it is open",
                "  capacity taken = 200/800 = 1/4",
                "  service rate   = 8 000 × 3/4          = 6 000 /s",
                "  ρ before       = 5 000/8 000          = 62.50%",
                "  ρ during       = 5 000/6 000          = 83.33%",
                "  W before       = 1/(8 000 − 5 000)    = 0.333 ms",
                "  W during       = 1/(6 000 − 5 000)    = 1.000 ms      3.00×",
                "",
                "trying to halve the window",
                "  B = 400 MB/s   duration = 8 h 20 min",
                "                 capacity taken = 1/2, service rate = 4 000 /s",
                "                 λ = 5 000 /s > 4 000 /s, so ρ ≥ 1 and the queue grows",
            ],
            "after": [
                "The last block is where the plan is actually decided. Halving the window "
                "is arithmetically available and operationally impossible, because the "
                "node cannot serve `5 000 /s` on `4 000 /s` of remaining capacity. The "
                "throttle's ceiling is set by the workload, not by the network.",
                "For a faded rehearsal, keep every other number and take the dataset to "
                "`96 TB`. The supplied first move is the bytes to move, `24.00 TB`. "
                "Produce the duration at `200 MB/s`, then say what happens to `ρ` during "
                "the move and why, then find the throttle at which the window would be "
                "back to sixteen hours and forty minutes — and say whether that throttle "
                "is usable at this arrival rate.",
            ],
        },
        "quiz_title": "Windows, throttles and utilisation",
        "quiz": [
            {"q": "25% of a 48 TB dataset is moved at a throttle of 200 MB/s. How long does it take?",
             "a": ["`16 h 40 min`", "`4 h 10 min`", "`2 d 18 h 40 min`", "`60 min`"],
             "c": 0,
             "why": "`0.25 × 48 TB = 12.00 TB`, and `12 × 10¹² / (200 × 10⁶) = 60 000` "
                    "seconds. `4 h 10 min` is the whole `800 MB/s` budget, which is not "
                    "available. `2 d 18 h 40 min` is the same move throttled to "
                    "`50 MB/s`."},
            {"q": "The copy takes 200 MB/s of a node's 800 MB/s transfer budget. The node served `8 000 /s` against `5 000 /s` of arrivals. What is `ρ` while the copy runs?",
             "a": ["`62.50%`, unchanged, because the request path is separate",
                   "`83.33%`, because the node now serves `6 000 /s`",
                   "`25.00%`, the share the copy took",
                   "`75.00%`, the share the node kept"],
             "c": 1,
             "why": "The copy holds a quarter of the transfer budget, so the effective "
                    "service rate is `8 000 × 3/4 = 6 000 /s` and `ρ = 5 000/6 000 = "
                    "83.33%`. `62.50%` is `ρ` before the move. `25%` and `75%` are the "
                    "split of the transfer budget, which is an input to the calculation "
                    "and not a utilisation."},
            {"q": "The window is sixteen hours and forty minutes and someone proposes doubling the throttle to `400 MB/s` to halve it. What happens?",
             "a": ["The window halves to `8 h 20 min` with no other effect",
                   "The window halves and `ρ` rises to about 91%",
                   "The window halves, the copy takes half the transfer budget, and the node can serve only `4 000 /s` against `5 000 /s` of arrivals, so the queue grows without bound",
                   "The window does not halve, because throughput does not scale linearly"],
             "c": 2,
             "why": "Half the `800 MB/s` budget leaves `4 000 /s` of service against "
                    "`5 000 /s` of arrivals, which is `ρ ≥ 1`: there is no steady-state "
                    "wait, the backlog grows for as long as the copy runs, and draining "
                    "it afterwards is its own incident. The throttle's usable ceiling is "
                    "set by the arrival rate."},
            {"q": "Utilisation goes from `62.50%` to `83.33%` for the duration. What does that do to the M/M/1 wait?",
             "a": ["It rises by about a third, in proportion to the utilisation",
                   "It triples, from `0.333 ms` to `1.000 ms`",
                   "It is unchanged, because the arrival rate did not change",
                   "It doubles, from `0.333 ms` to `0.667 ms`"],
             "c": 1,
             "why": "`W = 1/(μ − λ)`, so the wait is set by the gap between service and "
                    "arrivals, and that gap fell from `3 000 /s` to `1 000 /s`. A 21-point "
                    "rise in `ρ` tripling the wait is the knee: equal steps in utilisation "
                    "are not equal steps in latency, and this one is held for sixteen "
                    "hours and forty minutes."},
        ],
        "mistakes": [
            ("Reporting the duration and not the utilisation",
             "“About seventeen hours” sounds like scheduled maintenance. “Sixteen hours "
             "and forty minutes at `ρ = 83.33%` with three times the queueing wait” is "
             "what will happen, and it is the version that can be checked against a "
             "latency objective. The duration is the half of the cost that is easy to "
             "compute, which is why it is the half that gets quoted."),
            ("Raising the throttle to shorten the window without checking `ρ`",
             "The copy and the request path share one transfer budget. At `400 MB/s` of "
             "an `800 MB/s` budget the node serves `4 000 /s` against `5 000 /s` of "
             "arrivals, and the queue grows for the whole window. The throttle's ceiling "
             "is the arrival rate's, and it is well below the hardware's."),
            ("Taking the moved fraction as `1/N` out of habit",
             "It is `N/(N+1)` under `mod N` assignment and about `1/(N+1)` on a ring, and "
             "those differ by a factor of `N`. At seven shards on a 48 TB dataset that is "
             "`42 TB` against `6 TB` — the difference between `2 d 10 h 20 min` of "
             "elevated latency and `8 h 20 min` of it."),
        ],
        "standard": ("Finish when a rebalance plan you read makes you ask what `ρ` will be while it runs.",
                     "You should be able to turn a moved fraction, a dataset size and a "
                     "throttle into a window, compute the service rate and utilisation the "
                     "copy leaves, evaluate the wait at both utilisations, and find the "
                     "throttle at which the node stops keeping up."),
        "note": (
            "That closes the course. Every structural decision on it — the shard count, "
            "the partitioning function, the token count, the salt, the index design — is "
            "eventually paid for in the currency of this last lesson: bytes moved, hours "
            "of wall clock, and a utilisation held above normal while they move. The "
            "cheapest rebalance is the one a partitioning choice made years earlier does "
            "not require."
        ),
    },
]
