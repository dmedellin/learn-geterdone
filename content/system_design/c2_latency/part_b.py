"""Course 2, lessons 07-11 - hedging, convolution, the budget, timeouts and the loss bound."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "hedged-requests",
        "title": "Hedged Requests",
        "module": "The tail",
        "one_line": "Compute the hedged p99 and the extra load for a chosen hedge delay, and say when the independence it rests on is absent.",
        "summary": (
            "Send the request; if it has not answered by the p95 delay, send a second "
            "copy and take whichever returns first. Under independence the request is "
            "slow only if both copies are, so the tail past the delay is squared &mdash; "
            "and the second copy goes out only for the five percent of requests that "
            "were still running, so it costs about five percent more load. On the "
            "lab&rsquo;s service that takes a `120 ms` p99 to `45 ms`."
        ),
        "key": [
            "hedge at d:  finish at min(X, d + Y)     Y an independent copy",
            "P(hedged > t)  =  P(X > t) · P(X > t − d)",
            "extra load     =  P(X > d)               the tail past the delay",
            "d = 30 ms (the p95):  load +5.0%,  p99 falls 120 ms → 45 ms",
            "P(both slow past d)  =  (1/20)² = 1/400",
        ],
        "key_label": "A second copy, and what it costs to send it late",
        "concepts_intro": (
            "The hard idea is that the same independence that made a fan-out worse makes "
            "a duplicate better, and that the cost of the duplicate is decided entirely "
            "by when you send it."
        ),
        "concepts": [
            ("A hedge turns one call into the faster of two",
             "Issue the call. If no answer has arrived by `d` milliseconds, issue a "
             "second copy and use whichever finishes first. The request finishes at "
             "`min(X, d + Y)` with `Y` an independent copy of the same service, so a "
             "request is slow only when both copies are slow at once."),
            ("The tail past the delay is multiplied, not added",
             "`P(hedged > t) = P(X > t) · P(X > t − d)`. Just past `d` that is roughly "
             "the tail squared: on the lab&rsquo;s service, a `1/20` tail at `30 ms` "
             "becomes `1/400`. Squaring a small probability is a large change, and it is "
             "the same multiplication rule that made a fan-out of sixty-nine calls miss "
             "its p99 half the time."),
            ("The cost is exactly the tail you hedge past",
             "The second copy is sent only for requests still running at `d`, so the "
             "extra load is `P(X > d)` and nothing else. Hedge at the p95 and that is "
             "`5%`. Hedge nearer the median and the figure climbs fast: at the "
             "lab&rsquo;s `12 ms` median the backup goes out for `35%` of requests, "
             "seven times the traffic for a worse result."),
        ],
        "read_title": "A second copy, sent late",
        "read_intro": "What squaring a tail buys, what sending it costs, and the assumption that decides whether either number is real.",
        "body": [
            ("p", "The lab&rsquo;s preset is a hundred measured calls, given as run "
                  "lengths: forty at `10 ms`, twenty-five at `12 ms`, fifteen at "
                  "`15 ms`, ten at `20 ms`, five at `30 ms`, three at `50 ms`, one at "
                  "`120 ms` and one at `300 ms`. Its median is `12 ms`, its p95 is "
                  "`30 ms` and its p99 is `120 ms` &mdash; a tail ten times the median, "
                  "which is an ordinary shape for a service that is not in trouble."),
            ("def", ("Hedged request",
                     "A <strong>hedged request</strong> with delay `d` issues a second, "
                     "independent copy of the call if the first has not answered within "
                     "`d`, and completes when either copy answers. Its completion time "
                     "is `min(X, d + Y)`, where `X` and `Y` are independent draws from "
                     "the service&rsquo;s latency distribution. The <strong>extra "
                     "load</strong> it creates is `P(X > d)`: the fraction of requests "
                     "that live long enough to trigger the copy.")),
            ("p", "The tail of the hedged request factorises. It exceeds `t` only if the "
                  "first copy is still running at `t` and the second copy, which started "
                  "at `d`, is still running at `t`. Those are independent, so their "
                  "probabilities multiply:"),
            ("math", [
                "P(hedged > t)  =  P(X > t) · P(X > t − d)",
                "",
                "d = 30 ms,  the p95 of the service",
                "",
                "extra load    =  P(X > 30)              =  5/100   =  1/20   =  5.0%",
                "just past d   =  P(X > 30)·P(X > 0)     ≈  1/20     (one copy only)",
                "at t = 42     =  P(X > 42)·P(X > 12)    =  (1/20)(7/20)  =  7/400",
                "at t = 45     =  P(X > 45)·P(X > 15)    =  1/100",
                "",
                "hedged p99    =  45 ms          unhedged p99  =  120 ms",
                "hedged p50    =  12 ms          unhedged p50  =   12 ms",
            ]),
            ("p", "Two things happened and only one of them was asked for. The p99 fell "
                  "from `120 ms` to `45 ms`, a reduction of `62%`, for five percent more "
                  "traffic. The median did not move at all &mdash; it is still `12 ms` "
                  "&mdash; because ninety-five percent of requests never reach the delay "
                  "and never trigger anything. A hedge is a tail instrument. It does not "
                  "make a service faster; it makes a service less occasionally awful."),
            ("h3", "Choosing the delay"),
            ("ul", [
                "`d = 12 ms`, the median &mdash; load `+35.0%`, hedged p99 `30 ms`",
                "`d = 20 ms` &mdash; load `+10.0%`, hedged p99 `35 ms`",
                "`d = 30 ms`, the p95 &mdash; load `+5.0%`, hedged p99 `45 ms`",
                "`d = 50 ms` &mdash; load `+2.0%`, hedged p99 `62 ms`",
                "`d = 120 ms`, the p99 &mdash; load `+1.0%`, hedged p99 `120 ms`",
            ]),
            ("p", "The list is the whole design decision. Hedging at the median buys "
                  "`15 ms` more of tail reduction than hedging at the p95 and costs "
                  "seven times the extra traffic to get it. Hedging at the p99 costs "
                  "almost nothing and achieves almost nothing, because by `120 ms` the "
                  "only requests left running are the ones whose second copy will not "
                  "finish in time either. Somewhere around the p95 is where the curve "
                  "bends, which is why that is the usual recommendation."),
            ("example", ("Why the extra load is not a rounding error",
                         "A service handling `40 000` requests a second at a `5%` hedge "
                         "rate sends an extra `2000` calls a second. That is real "
                         "capacity, it must be provisioned, and it arrives precisely "
                         "when the service is already having difficulty &mdash; the "
                         "requests that trigger hedges are the slow ones, and slowness "
                         "is correlated in time. A hedge that is not capacity-planned "
                         "adds load to a system at the exact moment load is what is "
                         "wrong with it.")),
            ("p", "That last observation is also the limit of the technique, and it is "
                  "worth stating as sharply as possible. Every number on this page "
                  "assumes the second copy is independent of the first. If the call is "
                  "slow because the <em>request</em> is expensive &mdash; a large query, "
                  "a cold cache entry, a user with a great deal of data &mdash; then the "
                  "second copy is expensive in exactly the same way and `P(both slow)` "
                  "is not `p²` but something close to `p`. The hedge then costs its "
                  "extra load and buys nothing."),
            ("p", "Independence is plausible when the slowness belongs to the server: a "
                  "garbage-collection pause, a scheduling delay, a disk that is briefly "
                  "busy. It is implausible when the slowness belongs to the request, and "
                  "it is worse than implausible when the second copy is routed to the "
                  "same replica, which makes the two copies the same draw. Hedging to a "
                  "different replica is not a refinement of the technique; it is a "
                  "condition for the arithmetic being about anything."),
        ],
        "lab": ("latency", {
            "mode": "hedge",
            "panel_title": "Set the hedge delay",
            "panel_intro": "The hedged tail is computed on the grid of times where it can "
                           "change &mdash; the sample&rsquo;s own values, and those values "
                           "shifted by the delay. Move the delay from the p99 down toward "
                           "the median and watch the extra load rise faster than the tail falls.",
        }),
        "steps_title": "Sizing a hedge",
        "steps_intro": "The delay is the only parameter, and it sets both numbers at once.",
        "steps": [
            ("Check that the slowness belongs to the server, not the request",
             "If an expensive request is slow on every replica, a second copy is a "
             "second expensive request. Hedging is for variance that the request does "
             "not carry with it, and this question is prior to all the arithmetic."),
            ("Read the percentiles of the service you are hedging",
             "You need the distribution, not a mean: the median, the p95 and the p99 of "
             "measured calls. The delay will be chosen against these and the extra load "
             "read off the same list."),
            ("Pick the delay and read both consequences",
             "The extra load is `P(X > d)`, straight off the distribution. The hedged "
             "percentile comes from `P(X > t)·P(X > t − d)`. Quote them together: a "
             "hedge is a trade and a number that reports only the improvement is half "
             "an answer."),
            ("Provision the extra capacity, and make the copy go elsewhere",
             "The hedge rate is extra steady-state load and it clusters in time with "
             "the trouble that caused it. Route the second copy to a different replica, "
             "or the two draws are the same draw and `p²` is a fiction."),
        ],
        "worked": {
            "title": "Hedging the lab’s service at its p95",
            "intro": [
                "One hundred measured calls, one delay, and the two numbers that decide "
                "whether to do it."
            ],
            "lines": [
                "service    10:40  12:25  15:15  20:10  30:5  50:3  120:1  300:1",
                "           p50 = 12 ms    p95 = 30 ms    p99 = 120 ms",
                "",
                "choose     d = 30 ms   (the p95)",
                "",
                "cost       extra load = P(X > 30) = (3 + 1 + 1)/100 = 5/100 = 5.0%",
                "",
                "benefit    P(hedged > t) = P(X > t) · P(X > t − 30)",
                "",
                "             t = 42   (1/20)(7/20)  =  7/400   = 0.0175",
                "             t = 45   (1/20)(1/5)   =  1/100   = 0.0100   ← reaches 1%",
                "",
                "           hedged p99 = 45 ms          was 120 ms      −62%",
                "           hedged p50 = 12 ms          was  12 ms       unchanged",
                "",
                "compare    d = 12 ms (the median):  load 35.0%,  hedged p99 30 ms",
            ],
            "after": [
                "The final line is the comparison worth keeping. Moving the delay from "
                "the p95 to the median improves the hedged p99 from `45 ms` to `30 ms` "
                "&mdash; a further `15 ms` &mdash; and takes the extra load from `5%` to "
                "`35%`. Seven times the traffic to remove a further fifteen milliseconds "
                "is the sort of trade that looks reasonable when only one of its two "
                "numbers is on the slide.",
                "Notice also how the hedged p99 is found. It is not a formula: the "
                "function `P(X > t)·P(X > t − d)` can only change at the sample&rsquo;s "
                "own values and at those values shifted by `d`, so the answer is a "
                "search over that grid for the first time the product falls to `1/100`. "
                "Here it lands exactly on `1/100` at `45 ms`, which is `30 ms` of delay "
                "plus the `15 ms` atom.",
                "For a faded rehearsal, keep the same service and set the delay to "
                "`20 ms`. The supplied first move is the cost: `P(X > 20) = (5 + 3 + 1 "
                "+ 1)/100 = 10.0%`. Work out the hedged p99 by walking the grid upward "
                "from `20 ms`, then say whether doubling the extra load from the p95 "
                "choice was worth the improvement it bought. Check both figures in the "
                "lab before opening the quiz.",
            ],
        },
        "quiz_title": "Delays and duplicates",
        "quiz": [
            {"q": "A hedge is set at the service&rsquo;s p95. Roughly what extra load does it create?",
             "a": ["`95%`", "`50%`", "`5%`", "None, since the first copy is usually cancelled"],
             "c": 2,
             "why": "The second copy goes out only for requests still running at the "
                    "delay, and by definition `5%` of requests are still running at the "
                    "p95. `95%` inverts the percentile. `50%` is roughly what hedging at "
                    "the median would cost. Cancelling the loser saves the tail of its "
                    "work but the copy was still issued, and both copies still consumed "
                    "a slot."},
            {"q": "On the lab&rsquo;s preset, hedging at `30 ms` takes the p99 from `120 ms` to `45 ms`. What happens to the median?",
             "a": ["It halves, to `6 ms`",
                   "It stays at `12 ms`",
                   "It rises, because of the extra load",
                   "It falls to `10 ms`, the fastest observed call"],
             "c": 1,
             "why": "Ninety-five percent of requests finish before the delay and never "
                    "trigger a second copy, so nothing about the middle of the "
                    "distribution changes. A hedge is a tail instrument. The third "
                    "option is a real effect in an under-provisioned system, but it is a "
                    "consequence of not planning the capacity rather than of the hedge "
                    "arithmetic."},
            {"q": "A service is slow on exactly the requests that ask for a lot of data. What does a hedge buy?",
             "a": ["A squared tail, as usual, since the copies are still two separate calls",
                   "Nothing much: the second copy is slow for the same reason, so `P(both slow)` is near `p`, not `p²`",
                   "A halved tail, since two copies race",
                   "The same tail at half the load"],
             "c": 1,
             "why": "The `p²` depends on the two copies being independent draws. When the "
                    "slowness is a property of the request rather than of the server, "
                    "both copies inherit it and the joint probability barely falls below "
                    "`p`. The hedge still costs its extra load, which makes this the one "
                    "case where hedging is strictly worse than not hedging."},
        ],
        "mistakes": [
            ("Hedging near the median",
             "The extra load is the tail past the delay, so moving the delay toward the "
             "middle of the distribution moves the cost toward a second copy of every "
             "request. On the lab&rsquo;s service the p95 costs `5%` and the median "
             "costs `35%`, for `15 ms` of further improvement. Read both numbers before "
             "choosing, not just the one that improved."),
            ("Assuming independence when the request carries the slowness",
             "`P(both slow) = p²` is a consequence of two independent draws. An "
             "expensive query, a cold entry or a large user makes both copies slow "
             "together, and a second copy sent to the same replica makes them the same "
             "draw. In either case the hedge pays its load and buys nothing."),
            ("Treating the extra load as free because it is small",
             "Five percent of a large service is a large number of calls, and it arrives "
             "correlated with exactly the conditions that produced the slow requests. A "
             "hedge deployed without provisioning for its steady-state load is a "
             "mechanism for adding traffic to a system at its worst moment."),
        ],
        "standard": ("Finish when you quote a hedge as two numbers, never one.",
                     "You should be able to read a service&rsquo;s percentiles from a "
                     "sample, choose a hedge delay, compute the extra load and the hedged "
                     "percentile it produces, and state the condition under which the "
                     "second of those figures is meaningless."),
        "note": 'Both &ldquo;Tail Amplification under Fan-out&rdquo; and this lesson compose independent copies of a distribution. So does &ldquo;Percentiles Do Not Add&rdquo;, which asks what happens to the tail when two stages run one after the other instead of beside each other &mdash; and finds that the obvious arithmetic, adding the two stage p99s, is not the percentile of anything.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "percentiles-do-not-add",
        "title": "Percentiles Do Not Add",
        "module": "Budgets and limits",
        "one_line": "Compute the p99 of a two-stage sum by convolution and compare it with the sum of the two stage p99s.",
        "summary": (
            "Means add: the expected time of two stages in series is the sum of their "
            "expected times, exactly. Percentiles do not. The distribution of the sum is "
            "the convolution of the two stage distributions, and on the lab&rsquo;s "
            "stages its p99 is `78 ms` while the two stage p99s add to `110 ms`. The "
            "naive sum is not a bound and it is not conservative &mdash; it is a "
            "percentile of nothing."
        ),
        "key": [
            "means       E[A + B] = E[A] + E[B]        exactly, always",
            "percentiles p99(A + B) ≠ p99(A) + p99(B)",
            "the sum's distribution = the convolution of the two",
            "preset:  p99(A) = 38   p99(B) = 72   sum of p99s = 110 ms",
            "         p99(A + B) = 78 ms          the naive sum is 41.0% high",
        ],
        "key_label": "One rule that survives composition, and one that does not",
        "concepts_intro": (
            "The hard idea is that a percentile is a rank and ranks do not compose. The "
            "arithmetic that replaces the addition is the convolution, and it is "
            "enumeration rather than algebra."
        ),
        "concepts": [
            ("The sum’s distribution is the convolution",
             "If stage A takes `a` with probability `P(a)` and stage B takes `b` with "
             "probability `Q(b)`, independently, then the total takes `a + b` with "
             "probability `P(a)·Q(b)`. Enumerate every pair, add up the probabilities "
             "that land on the same total, and you have the distribution of the sum. "
             "Seven outcomes each give forty-nine pairs and `43` distinct totals."),
            ("Expectation is linear; ranks are not",
             "`E[A + B] = E[A] + E[B]` needs no independence and holds exactly: on the "
             "preset, `881/125 + 2414/125 = 659/25`, which the lab prints as three exact "
             "fractions. There is no corresponding law for percentiles, because a "
             "percentile is a position in a sorted list and positions do not add."),
            ("Adding the p99s assumes both bad days coincide",
             "`p99(A) + p99(B)` is the time taken when stage A is at its p99 "
             "<em>and</em> stage B is at its p99 in the same request. Independently that "
             "happens with probability `7/25000`, about `0.028%` &mdash; roughly three "
             "requests in ten thousand, not one in a hundred. The naive sum is a "
             "percentile of the joint worst case, which is a far rarer event than the "
             "one being asked about."),
        ],
        "read_title": "Convolution, and the sum that is not a percentile",
        "read_intro": "Two stages, forty-nine pairs, and two numbers that differ by a third.",
        "body": [
            ("p", "The lab holds two stages, each given as a list of "
                  "`milliseconds:weight` pairs. Stage A is mostly fast &mdash; `4 ms` "
                  "on more than half of calls &mdash; with a thin tail out to `70 ms`. "
                  "Stage B is slower and steadier, centred near `17 ms` with a tail to "
                  "`130 ms`. They run one after the other, so the request takes the sum."),
            ("def", ("Convolution of two distributions",
                     "For independent `A` and `B` taking values with probabilities "
                     "`P(a)` and `Q(b)`, the <strong>convolution</strong> is the "
                     "distribution of `A + B`: the probability of a total `t` is the sum "
                     "of `P(a)·Q(b)` over every pair with `a + b = t`. With finitely "
                     "many outcomes it is computed by enumerating all the pairs, so it "
                     "is exact and needs no approximation at all.")),
            ("p", "Take the two stages&rsquo; own percentiles first, by the rank rule of "
                  "&ldquo;Percentiles from a Sample&rdquo;. Stage A has a p99 of "
                  "`38 ms`; stage B has a p99 of `72 ms`. Add them and you get `110 ms`, "
                  "and that number appears in a great many latency budgets. Now compute "
                  "the distribution of the sum and read its p99 off the same rank rule."),
            ("math", [
                "stage A    4:520  6:250  9:120  14:60  22:30  38:16  70:4",
                "stage B    12:420 17:300 24:150 34:80  48:36  72:12  130:2",
                "",
                "            p50    p95    p99     mean",
                "  A           4     14     38     881/125   =  7.048",
                "  B          17     34     72    2414/125   = 19.312",
                "  added      21     48    110     659/25    = 26.360",
                "  A + B      21     52     78     659/25    = 26.360",
                "",
                "p99(A + B) = 78 ms      p99(A) + p99(B) = 110 ms      gap 32 ms, 41.0%",
                "cumulative at 77 ms:  24693/25000 = 0.98772   — short of 99/100",
                "cumulative at 78 ms:   3096/3125  = 0.99072   — first to reach it",
            ]),
            ("p", "The true p99 of the two stages together is `78 ms`. The sum of the "
                  "p99s is `110 ms`, which overstates it by `32 ms` &mdash; `41.0%`. "
                  "Budgeting the pair at `110 ms` reserves a third more time than the "
                  "percentile being promised actually needs, and if that budget is what "
                  "sizes a timeout or a machine count, the overstatement is paid for in "
                  "capacity."),
            ("p", "Read the two mean columns while you are here. `881/125 + 2414/125` is "
                  "`3295/125`, which is `659/25` &mdash; and `659/25` is exactly the mean "
                  "of the convolved distribution. The added row and the true row agree to "
                  "the last digit for means and disagree by a third for the p99. That is "
                  "the whole lesson in one table: linearity of expectation is a theorem, "
                  "and there is no theorem next to it for percentiles."),
            ("h3", "Why it is not a bound either"),
            ("p", "The natural repair is to keep adding the percentiles and call the "
                  "result conservative. Look at the p95 row of the same table. The stage "
                  "p95s are `14 ms` and `34 ms`, which add to `48 ms`; the true p95 of "
                  "the sum is `52 ms`. Here the naive arithmetic <em>understates</em> by "
                  "four milliseconds, on the very same pair of stages, at a percentile "
                  "one step away."),
            ("p", "So the sum of the percentiles is not an upper bound, not a lower "
                  "bound, and not conservative. It is a number obtained by adding two "
                  "quantities that were never addends. Whether it comes out high or low "
                  "depends on how the mass beyond each stage&rsquo;s percentile is "
                  "arranged: when each stage&rsquo;s tail is thin and far out, a single "
                  "rare spike carries the pair over the line on its own and the true "
                  "percentile can sit above the naive sum."),
            ("example", ("How rare the naive answer actually is",
                         "For the total to reach `110 ms` by both stages being at their "
                         "p99 together, stage A must exceed `37 ms` &mdash; probability "
                         "`1/50` &mdash; and stage B must exceed `71 ms` &mdash; "
                         "probability `7/500`. Independently that is `7/25000`, or "
                         "`0.0280%`. The question asked was about the worst one percent "
                         "of requests; the number returned describes the worst three in "
                         "ten thousand. They are different questions with a factor of "
                         "thirty-five between them.")),
            ("p", "What to do instead is in the lab. Convolve: enumerate the pairs, "
                  "accumulate the probabilities onto their totals, and read the "
                  "percentile of the result by rank. For two stages of seven outcomes "
                  "that is forty-nine multiplications, every probability an exact "
                  "fraction, and the answer is the percentile of the thing that was "
                  "actually asked about."),
        ],
        "lab": ("latency", {
            "mode": "convolve",
            "panel_title": "Edit the two stages",
            "panel_intro": "Every pair of outcomes is enumerated and its probability "
                           "multiplied out, so the distribution of the total is exact and "
                           "so is its p99. The table prints the naive addition and the "
                           "convolution side by side at the p50, the p95 and the p99 "
                           "&mdash; they do not always disagree in the same direction.",
        }),
        "steps_title": "Adding two stages properly",
        "steps_intro": "Four steps, and the first is a decision about which question you are answering.",
        "steps": [
            ("Decide whether the question is about means or about a percentile",
             "For total work, capacity and cost, add the means: that is exact and needs "
             "no independence. For a latency objective stated as a percentile, the "
             "addition is not available and the next three steps are the method."),
            ("Enumerate every pair of outcomes",
             "Each pair contributes its two times added together, with probability the "
             "product of the two probabilities. Keep the probabilities as fractions; "
             "with integer weights they stay exact and the final comparison needs no "
             "rounding argument."),
            ("Accumulate onto totals and read the percentile by rank",
             "Different pairs land on the same total, so add their probabilities "
             "together. Then walk the totals in order, accumulating, and take the first "
             "value whose cumulative probability reaches `q`. That is the percentile of "
             "the sum."),
            ("Compare it with the naive sum and quote the gap",
             "Report both numbers and their difference. The gap is what the naive "
             "arithmetic was about to cost, in either direction, and it is the only "
             "thing that will persuade anyone to do the convolution next time."),
        ],
        "worked": {
            "title": "Two stages in series, at the p99",
            "intro": [
                "The stages are small enough to enumerate and the arithmetic is exact, "
                "so the comparison at the end rests on nothing but counting."
            ],
            "lines": [
                "A   4:520  6:250  9:120  14:60  22:30  38:16  70:4     (1000 calls)",
                "B  12:420 17:300 24:150 34:80  48:36  72:12 130:2     (1000 calls)",
                "",
                "stage percentiles, by rank:",
                "    p99(A) = 38 ms          p99(B) = 72 ms",
                "    naive   38 + 72         = 110 ms",
                "",
                "convolve:  49 pairs  →  43 distinct totals",
                "    P(total = t) = Σ P(a)·Q(b)   over all a + b = t",
                "",
                "walk the totals upward, accumulating:",
                "    …",
                "    at 77 ms   cumulative = 24693/25000 = 0.98772    < 99/100",
                "    at 78 ms   cumulative =  3096/3125  = 0.99072    ≥ 99/100   ←",
                "",
                "    p99(A + B) = 78 ms",
                "",
                "compare      110 − 78 = 32 ms overstated,  41.0% high",
                "means        881/125 + 2414/125 = 659/25,  and mean(A + B) = 659/25   ✓",
            ],
            "after": [
                "The tick on the last line is not decoration. The means were computed two "
                "ways &mdash; added, and taken from the convolved distribution &mdash; "
                "and they agree exactly. That is a check on the convolution itself: if "
                "those two disagreed, the enumeration would have a bug in it, and the "
                "p99 it produced would be worth nothing.",
                "The `41.0%` gap is not a general figure. It depends entirely on the "
                "shapes: two stages with fat, nearby tails give a smaller gap, and the "
                "p95 row of the same pair gives a gap of the opposite sign. What is "
                "general is that the two numbers are answers to different questions, and "
                "that only one of them was asked.",
                "For a faded rehearsal, replace stage B with `10:900, 100:100` &mdash; a "
                "stage that is fast nine times in ten and takes `100 ms` otherwise. The "
                "supplied first move is B&rsquo;s own p99, which by rank is `100 ms`. "
                "Predict whether the true p99 of the sum will be above or below "
                "`38 + 100 = 138 ms` before you compute anything, then type the stage "
                "into the lab and see. Write down which way you guessed and why before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "What composes and what does not",
        "quiz": [
            {"q": "Two independent stages have means `7.048 ms` and `19.312 ms`. What is the mean of the total?",
             "a": ["`26.360 ms`, exactly", "`26.360 ms`, approximately",
                   "It cannot be determined without the distributions",
                   "`19.312 ms`, the larger of the two"],
             "c": 0,
             "why": "Expectation is linear, so the means add exactly, and the lab prints "
                    "`881/125 + 2414/125 = 659/25` as three exact fractions to show it. "
                    "Linearity does not even require independence. The maximum rule "
                    "belongs to parallel stages, not serial ones."},
            {"q": "On the lab&rsquo;s preset, `p99(A) = 38 ms` and `p99(B) = 72 ms`. What is `p99(A + B)`?",
             "a": ["`110 ms`", "`78 ms`", "`72 ms`", "`55 ms`, the average of the two"],
             "c": 1,
             "why": "The convolution puts `99%` of the mass at or below `78 ms`: the "
                    "cumulative reaches `3096/3125` there and is only `24693/25000` at "
                    "`77 ms`. `110 ms` is the naive sum, which overstates by `41.0%` "
                    "because it describes both stages having their bad day together "
                    "&mdash; an event of probability `0.0280%`."},
            {"q": "Is the sum of two stage p99s a safe upper bound on the p99 of the total?",
             "a": ["Yes, always, by the triangle inequality",
                   "Yes, provided the stages are independent",
                   "No &mdash; on the lab&rsquo;s own stages the p95s add to `48 ms` while the true p95 is `52 ms`",
                   "No, but only when the stages are positively correlated"],
             "c": 2,
             "why": "The same two stages give a naive sum above the truth at the p99 and "
                    "below it at the p95, with independence assumed throughout. So it is "
                    "not a bound in either direction and independence does not rescue it. "
                    "There is no triangle inequality for quantiles; the sum of "
                    "percentiles is simply not a percentile of anything."},
        ],
        "mistakes": [
            ("Adding stage percentiles to get an end-to-end percentile",
             "It is the single most common arithmetic error in a latency budget. On the "
             "lab&rsquo;s stages it overstates the p99 by `32 ms`, and on the same "
             "stages it understates the p95 by `4 ms`. The operation is not conservative, "
             "not a bound, and not defined &mdash; the right method is to convolve."),
            ("Assuming the naive sum errs in a known direction",
             "&ldquo;It is at least pessimistic&rdquo; is the usual defence, and the p95 "
             "row refutes it on the very same data. Which way it errs depends on how the "
             "mass past each percentile is arranged, so it has to be computed rather "
             "than assumed."),
            ("Using the mean because it composes, when the objective is a percentile",
             "The means do add, exactly, which makes them tempting. But an SLO written "
             "as a p99 is not a statement about a mean, and on the lab&rsquo;s stages "
             "the mean of the total is `26.36 ms` against a p99 of `78 ms`. Budgeting the "
             "p99 in means understates the requirement by a factor of three."),
        ],
        "standard": ("Finish when adding two p99s looks like a category error rather than an approximation.",
                     "You should be able to convolve two small distributions by "
                     "enumerating pairs, read the percentile of the result by rank, "
                     "compare it with the sum of the stage percentiles, and state the "
                     "probability of the joint event the naive sum actually describes."),
        "note": 'The stage floors of &ldquo;The Speed-of-Light Floor&rdquo; and &ldquo;Round Trips, Not Bytes&rdquo;, the graph of &ldquo;Serial Sums, Parallel Maxes&rdquo; and the percentile arithmetic of this lesson are now all available, and &ldquo;Latency Budgets&rdquo; puts them in one place: an objective at the top, the floors subtracted first, and what is left divided among the stages that are allowed to spend it.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "latency-budgets",
        "title": "Latency Budgets",
        "module": "Budgets and limits",
        "one_line": "Allocate a budget backwards from an SLO across a stage graph and report the residual per stage, including where it is negative.",
        "summary": (
            "A budget is built from the objective downwards, not from the stages upwards. "
            "Take the SLO, subtract the floors that no code can remove &mdash; the "
            "light-speed minimum and the handshake round trips &mdash; and what is left "
            "is all the code may spend. Divide it among the stages and the arithmetic "
            "will usually tell you, immediately, that one stage cannot fit."
        ),
        "key": [
            "available = SLO − (light-speed floor + handshake round trips)",
            "even share = available ÷ number of stages",
            "residual per stage = share − that stage's own floor",
            "400 − (56 + 152) = 192 ms available,  48 ms each across four stages",
            "search floors at 150 ms:  residual −102 ms, and the plan is 26 ms short",
        ],
        "key_label": "Subtract the floors first; divide what is left",
        "concepts_intro": (
            "The hard idea is the direction. A budget assembled by adding up what the "
            "stages currently cost is not a budget, it is a measurement with a total at "
            "the bottom."
        ),
        "concepts": [
            ("Allocate backwards from the objective",
             "Start with the number that was promised. Subtract everything that cannot "
             "be changed. Divide the remainder among the stages that can. A budget built "
             "the other way &mdash; adding stage costs upward &mdash; can only ever "
             "report what the system already does, which is the one thing a budget is "
             "not for."),
            ("The floors come out before anything is allocated",
             "The light-speed minimum for the route and the sequential handshakes are "
             "fixed: `56 ms` and `152 ms` on the preset, `208 ms` of a `400 ms` "
             "objective. More than half the budget is gone before a line of code is "
             "considered, and pretending otherwise is how a plan that was never feasible "
             "gets approved."),
            ("A negative residual is the finding, not a failure of the method",
             "The even share is `48 ms` and `search` cannot run in less than `150 ms`, "
             "so its residual is `−102 ms`. The other three stages release `76 ms` "
             "between them against a need of `102 ms`, leaving the plan `26 ms` short. "
             "That arithmetic is the output: it names the stage, the amount, and the "
             "size of the gap that remains after every other stage has given up what it can."),
        ],
        "read_title": "Building a budget from the top",
        "read_intro": "What comes out first, what is left, and how to read a residual that has gone negative.",
        "body": [
            ("p", "The objective on the lab&rsquo;s preset is a p99 of `400 ms`. The "
                  "route has a light-speed floor of `56 ms` &mdash; the New York to "
                  "London figure from &ldquo;The Speed-of-Light Floor&rdquo;, rounded to "
                  "the nearest millisecond &mdash; and the connection costs two "
                  "sequential round trips at the measured `76 ms`, which is `152 ms`. "
                  "Those two are not negotiable and they are subtracted before anything "
                  "else happens."),
            ("math", [
                "SLO                                            400 ms",
                "  − light-speed floor                          −56 ms",
                "  − handshake round trips (2 × 76 ms)         −152 ms",
                "                                              ────────",
                "  available for the code                       192 ms",
                "",
                "four stages, even share  =  192 / 4  =  48 ms each",
                "",
                "  stage      floor    share    residual",
                "  gateway       8       48        +40      fits",
                "  auth         20       48        +28      fits",
                "  search      150       48       −102      does not fit",
                "  render       40       48         +8      fits",
                "                                ────────",
                "  floors total 218                         192 − 218 = −26 ms",
                "  spare  +76     need  102                  76 − 102 = −26 ms   ✓",
            ]),
            ("p", "The two ways of counting the shortfall agree, which is the check the "
                  "lab performs on every redraw: available minus the floors is `−26 ms`, "
                  "and the surplus the fitting stages release minus the shortfall of the "
                  "one that does not is also `−26 ms`. An allocation that does not "
                  "balance both ways has an arithmetic error in it, and the panel says so "
                  "when it happens."),
            ("def", ("Residual",
                     "A stage&rsquo;s <strong>residual</strong> is its allocated share "
                     "minus its own floor: the time it has left to spend on work that is "
                     "not already forced. A positive residual is headroom the stage can "
                     "release to another stage. A negative residual is a stage that "
                     "cannot meet its allocation under any implementation, and the "
                     "<strong>overall residual</strong> &mdash; available time minus the "
                     "sum of the floors &mdash; says whether the whole plan is feasible.")),
            ("h3", "Reading a plan that does not fit"),
            ("p", "The even split is a diagnostic, not a design. Nobody believes a "
                  "gateway and a search engine deserve the same `48 ms`; the split is "
                  "there because it shows in one line which stage the objective cannot "
                  "hold. Here it is `search`, by `102 ms`, and the three other stages "
                  "together have only `76 ms` to give. Four things can be done and the "
                  "arithmetic prices each of them."),
            ("ul", [
                "raise the objective &mdash; at a `500 ms` SLO the available time is `292 ms` and the overall residual becomes `+74 ms`",
                "remove a floor &mdash; dropping the two handshakes takes available to `344 ms` and the residual to `+126 ms`",
                "make `search` cheaper &mdash; at a `100 ms` floor the plan has `+24 ms` overall, though `search` still exceeds an even share",
                "take work off the critical path &mdash; which is the graph question of &ldquo;Serial Sums, Parallel Maxes&rdquo;, not a budgeting one",
            ]),
            ("p", "The third of those is worth pausing on. Cut `search` to a `100 ms` "
                  "floor and the overall residual turns positive at `+24 ms`, but "
                  "`search` is still `52 ms` above the even share of `48 ms` and the "
                  "lab still marks it as not fitting. Both statements are true and they "
                  "mean different things: the plan is now feasible, and it is feasible "
                  "only because the other three stages are subsidising the fourth. The "
                  "even split is what makes that visible."),
            ("example", ("Why the SLO has to be a percentile all the way down",
                         "If the objective is a p99, then every floor and every "
                         "allocation in the table is a p99, and the stage figures cannot "
                         "be means. A budget built by summing mean stage times will fit "
                         "comfortably and be violated on most slow requests: on the "
                         "stages of &ldquo;Percentiles Do Not Add&rdquo; the mean of the "
                         "total is `26.36 ms` and its p99 is `78 ms`, a factor of three. "
                         "Choosing the statistic is the first line of the budget, not an "
                         "afterthought.")),
            ("p", "There is one more trap, and it is the one the previous lesson exists "
                  "to prevent. Having filled in a p99 for every stage, it is natural to "
                  "add them and compare the total with the objective. That total is not "
                  "the p99 of anything. On the two stages of &ldquo;Percentiles Do Not "
                  "Add&rdquo; it overstated by `41.0%`, and on a different pair it would "
                  "understate. A budget is a planning device built from per-stage "
                  "allocations; the end-to-end percentile it implies has to be computed "
                  "by convolution, and the two should be checked against each other "
                  "rather than assumed equal."),
        ],
        "lab": ("latency", {
            "mode": "budget",
            "panel_title": "Set the SLO and the floors",
            "panel_intro": "The floors are subtracted first and what remains is split "
                           "evenly, with every stage that cannot fit its share marked. "
                           "Push the objective up until the plan balances, then bring it "
                           "back down and remove a floor instead.",
        }),
        "steps_title": "Laying out a budget",
        "steps_intro": "Top down, floors first, and the failing stage named rather than averaged away.",
        "steps": [
            ("Write the objective and say which statistic it is",
             "A p99 objective makes every number below it a p99. Mixing a percentile "
             "objective with mean stage figures produces a budget that fits on paper and "
             "fails in production, and it is the most common way for this exercise to go "
             "wrong before any arithmetic happens."),
            ("Subtract the floors that no implementation removes",
             "The light-speed minimum for the route, and the sequential round trips the "
             "connection costs. On the preset that is `56 + 152 = 208 ms` of a `400 ms` "
             "objective &mdash; more than half &mdash; and what is left is the only part "
             "anybody gets to allocate."),
            ("Split what remains and compute each stage’s residual",
             "An even split first, because it is the fastest way to find the stage the "
             "objective cannot hold. Residual is share minus the stage&rsquo;s own "
             "floor; negative means impossible, not merely tight."),
            ("Balance the surplus against the shortfall, and check it twice",
             "Add the positive residuals and the negative ones separately. Their "
             "difference must equal available time minus the total of the floors. If the "
             "two disagree, the arithmetic is wrong; if they agree and are negative, the "
             "plan is infeasible by exactly that much."),
        ],
        "worked": {
            "title": "A 400 ms p99 across four stages",
            "intro": [
                "The objective comes first and everything else is subtraction. The "
                "answer arrives before any stage has been optimised."
            ],
            "lines": [
                "objective      p99 ≤ 400 ms",
                "",
                "floors         light-speed, NY–London        56 ms",
                "               2 round trips at 76 ms       152 ms",
                "                                           ───────",
                "                                            208 ms",
                "",
                "available      400 − 208                  =  192 ms",
                "even share     192 / 4                    =   48 ms",
                "",
                "  gateway    floor   8    residual  48 −   8  =  +40    fits",
                "  auth       floor  20    residual  48 −  20  =  +28    fits",
                "  search     floor 150    residual  48 − 150  = −102    DOES NOT FIT",
                "  render     floor  40    residual  48 −  40  =   +8    fits",
                "",
                "check      floors total   8 + 20 + 150 + 40   =  218 ms",
                "           overall        192 − 218           =  −26 ms",
                "           spare 40 + 28 + 8 = 76,  need 102",
                "           76 − 102                           =  −26 ms   ✓ agrees",
                "",
                "verdict    infeasible by 26 ms, and search is the stage",
            ],
            "after": [
                "Nothing here required knowing anything about the code. Four floors, two "
                "fixed costs and one objective produced a verdict, the name of the stage "
                "responsible, and the exact size of the gap &mdash; which is the "
                "difference between &ldquo;we should look at performance&rdquo; and "
                "&ldquo;search has to lose 26 ms or the objective has to move&rdquo;.",
                "The `208 ms` of floors is the figure that most often surprises people. "
                "It is more than half the objective, it belongs to physics and protocol "
                "rather than to anyone&rsquo;s code, and it is why a `400 ms` promise on "
                "a transatlantic route is a much tighter promise than it sounds. "
                "Removing one of the two handshakes &mdash; a warm connection &mdash; is "
                "worth `76 ms`, which is nearly three times what the whole plan is short by.",
                "For a faded rehearsal, keep the four stages and set the objective to "
                "`350 ms` with a `40 ms` light-speed floor and one round trip of `76 ms` "
                "instead of two. The supplied first move is the available time: "
                "`350 − 116 = 234 ms`. Compute the even share, the four residuals, the "
                "spare and the need, and check the shortfall both ways. Say whether the "
                "plan fits and, if it does not, by how much &mdash; then reproduce all of "
                "it on the lab&rsquo;s sliders before opening the quiz.",
            ],
        },
        "quiz_title": "Allocating backwards",
        "quiz": [
            {"q": "An SLO of `400 ms` has fixed floors totalling `208 ms` and four stages. What is the even share?",
             "a": ["`100 ms`", "`52 ms`", "`48 ms`", "`98 ms`"],
             "c": 2,
             "why": "`400 − 208 = 192`, and `192 / 4 = 48 ms`. `100 ms` divides the "
                    "objective without removing the floors, which is the error the whole "
                    "method exists to prevent. `52 ms` divides `208` by four. `98 ms` "
                    "subtracts half the floors."},
            {"q": "A stage has a floor of `150 ms` and an allocated share of `48 ms`. What does the residual of `−102 ms` mean?",
             "a": ["The stage is `102 ms` slower than it should be and needs profiling",
                   "The stage cannot meet its allocation under any implementation, and `102 ms` must come from elsewhere or from the objective",
                   "The budget should be recomputed with an uneven split so the residual disappears",
                   "The stage should be moved off the critical path"],
             "c": 1,
             "why": "A floor is what the stage costs at best, so a negative residual is "
                    "an infeasibility rather than an inefficiency. Profiling cannot help "
                    "a floor. Re-splitting unevenly can make the plan feasible &mdash; "
                    "here the others have `76 ms` to give, which is not enough &mdash; "
                    "but it does not make the number disappear. Moving the stage off the "
                    "path is a real option and a different lesson&rsquo;s."},
            {"q": "Every stage&rsquo;s p99 has been filled in and they sum to less than the SLO. Is the end-to-end p99 within the objective?",
             "a": ["Yes, since the stages are in series and series adds",
                   "Yes, provided the stages are independent",
                   "Not established &mdash; the sum of stage p99s is not the p99 of the total and can err either way",
                   "No, it will always be larger"],
             "c": 2,
             "why": "Series adds <em>times</em>, not percentiles. On the stages of "
                    "&ldquo;Percentiles Do Not Add&rdquo; the sum of the p99s overstates "
                    "the true p99 by `41.0%` while the sum of the p95s understates it. "
                    "Independence does not repair this. The end-to-end percentile has to "
                    "be computed by convolution and compared with the budget."},
        ],
        "mistakes": [
            ("Building the budget upward from what the stages currently cost",
             "That produces a total, not a budget. A budget is an allocation of a "
             "promised number, so it starts at the promise and works down; the useful "
             "output is the residual on each stage, and a plan assembled from the bottom "
             "has no residuals in it at all."),
            ("Budgeting in means when the objective is a percentile",
             "The means are smaller, they add exactly, and they are about a different "
             "question. On the stages of &ldquo;Percentiles Do Not Add&rdquo; the mean "
             "total is `26.36 ms` and the p99 is `78 ms`. A budget filled in with means "
             "against a p99 objective understates the requirement by roughly a factor of "
             "three and will pass every review."),
            ("Leaving the fixed floors out, or discovering them last",
             "On the preset the light-speed minimum and the handshakes are `208 ms` of a "
             "`400 ms` objective. A plan that allocates the full `400 ms` among the "
             "stages is over-committed by more than half before anyone writes anything, "
             "and the error is invisible because every individual stage figure is reasonable."),
        ],
        "standard": ("Finish when your first move on a latency target is a subtraction.",
                     "You should be able to take an objective, subtract the fixed floors, "
                     "divide what remains, compute each stage&rsquo;s residual, balance "
                     "the surplus against the shortfall two ways, and state whether the "
                     "plan is feasible and by how much it is not."),
        "note": 'The budget so far assumes every call eventually answers. It does not: a call has to be given up on at some point, and that decision has two consequences the budget has to hold. &ldquo;Timeouts and Retries in the Budget&rdquo; puts the worst case `(r + 1) × T` inside the allocation and prices the good calls the timeout throws away.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "timeouts-and-retries-in-the-budget",
        "title": "Timeouts and Retries in the Budget",
        "module": "Budgets and limits",
        "one_line": "Choose a timeout and retry count that fit a budget, and report the fraction of good calls the timeout kills.",
        "summary": (
            "A timeout and a retry count are a pair of numbers with two consequences "
            "each. The worst case is `(r + 1) × T` and it has to fit inside the "
            "allocation the budget gave this call. And the timeout itself discards every "
            "call that would have succeeded after it &mdash; `1 − F(T)` of them &mdash; "
            "so a timeout set at the mean throws away fifteen percent of perfectly good "
            "calls on the lab&rsquo;s service."
        ),
        "key": [
            "worst case  =  (r + 1) × T        it must fit the budget for this call",
            "good calls killed  =  1 − F(T)    F is the measured distribution",
            "all attempts lost  =  (1 − F(T))ʳ⁺¹   under independence",
            "T = 90 ms (the p99), r = 1:   180 ms worst case,  1% killed",
            "T = 18 ms (the mean),  r = 1:  36 ms worst case, 15% killed",
        ],
        "key_label": "Two numbers, four consequences",
        "concepts_intro": (
            "The hard idea is that a timeout is not a safety device with no cost. It is "
            "a decision to abandon calls that were going to work, and the size of that "
            "decision is a number you can read off the distribution."
        ),
        "concepts": [
            ("The worst case is `(r + 1) × T`, and it is what the budget holds",
             "A call with `r` retries can consume `r + 1` full timeouts before giving up. "
             "That is the number the budget has to accommodate, not the typical case: on "
             "the lab&rsquo;s preset, `T = 90 ms` with one retry is `180 ms` against a "
             "`250 ms` allocation, which fits, while a second retry would need `270 ms` "
             "and does not."),
            ("A timeout kills good calls, and the fraction is `1 − F(T)`",
             "Every call that would have finished after `T` is abandoned even though it "
             "was going to succeed. On the preset, `T = 90 ms` kills `1%` &mdash; the "
             "one call in a hundred that takes `400 ms`. Move the timeout to the "
             "mean of `18.27 ms` and it kills `15%`, which is fifteen working calls in "
             "every hundred turned into errors by a configuration value."),
            ("Retries multiply the worst case and shrink the failure probability",
             "If attempts are independent, all `r + 1` of them time out with probability "
             "`(1 − F(T))ʳ⁺¹`: at `T = 90 ms` that is `1/100` with no retry and "
             "`1/10 000` with one. The retry buys two decimal places of reliability and "
             "costs a doubling of the worst case, and the budget is what decides whether "
             "the second half of that trade is affordable."),
        ],
        "read_title": "Two numbers, and the four consequences they have",
        "read_intro": "What the budget holds, what the timeout discards, and why the mean is the worst place to put it.",
        "body": [
            ("p", "The lab&rsquo;s preset is a hundred measured calls: forty-five at "
                  "`8 ms`, twenty-five at `11 ms`, fifteen at `16 ms`, eight at `24 ms`, "
                  "four at `45 ms`, two at `90 ms` and one at `400 ms`. Its median is "
                  "`11 ms`, its p95 is `45 ms`, its p99 is `90 ms` and its mean is "
                  "`18.27 ms`. The budget has given this call `250 ms`."),
            ("def", ("Timeout and retry budget",
                     "For a timeout `T` and a retry count `r`, the <strong>worst-case "
                     "latency</strong> of the call is `(r + 1) × T`: every attempt may "
                     "run to the timeout before the next begins. The <strong>kill "
                     "fraction</strong> is `1 − F(T)`, where `F` is the measured "
                     "distribution of call latency &mdash; the proportion of calls that "
                     "would have succeeded and are abandoned. The call fails entirely "
                     "with probability `(1 − F(T))ʳ⁺¹` if attempts are independent.")),
            ("math", [
                "sample   8:45  11:25  16:15  24:8  45:4  90:2  400:1      (100 calls)",
                "         p50 = 11    p95 = 45    p99 = 90    mean = 18.27",
                "",
                "  T       worst case     worst case     killed      all lost",
                "         (r = 1)        (r = 2)       1 − F(T)     (r = 1)",
                "",
                "  18        36 ms          54 ms        15.00%       2.25%",
                "  45        90 ms         135 ms         3.00%       0.09%",
                "  90       180 ms         270 ms         1.00%       0.01%",
                " 125       250 ms         375 ms         1.00%       0.01%",
                " 400       800 ms        1200 ms         0.00%       0.00%",
                "",
                "budget for this call: 250 ms",
            ]),
            ("p", "Read the `250 ms` budget across that table and the feasible choices "
                  "appear immediately. `T = 90 ms` with one retry costs `180 ms` in the "
                  "worst case, kills `1%` of good calls and loses the call entirely once "
                  "in ten thousand. `T = 90 ms` with two retries needs `270 ms` and does "
                  "not fit. `T = 125 ms` with one retry uses the whole `250 ms` exactly "
                  "and kills the same `1%`, because there is nothing in the distribution "
                  "between `90 ms` and `400 ms` for the extra `35 ms` to rescue."),
            ("h3", "The mean is the worst place to put a timeout"),
            ("p", "It is a common instinct: the calls take `18.27 ms` on average, so "
                  "anything much past that has clearly gone wrong. On this distribution "
                  "that setting kills `15%` of good calls. Fifteen in every hundred "
                  "requests that were going to return a correct answer are turned into "
                  "errors, retried, counted as failures, and &mdash; if the retry goes "
                  "to the same overloaded place &mdash; used to generate more load."),
            ("p", "The reason is the shape from &ldquo;Percentiles from a Sample&rdquo;. "
                  "The mean of a latency distribution sits well above the median and well "
                  "below the tail, in the sparse region between the bulk and the "
                  "outliers. A timeout there is close enough to the bulk to catch a great "
                  "deal of ordinary variation and far enough from the tail to be no "
                  "protection against the calls that are genuinely stuck. It is the worst "
                  "of both, and it is the most common setting there is."),
            ("example", ("What the retry actually buys, and what it costs",
                         "At `T = 90 ms` a single attempt is abandoned `1%` of the time. "
                         "With one retry, and assuming the two attempts are independent, "
                         "both are abandoned `1/100 × 1/100 = 1/10 000` of the time "
                         "&mdash; the call now fails once in ten thousand instead of once "
                         "in a hundred. The cost is that the worst case doubles from "
                         "`90 ms` to `180 ms`, and the budget has to hold the worst case "
                         "rather than the typical one. Two decimal places of reliability "
                         "for a doubling of the reservation is usually a good trade; a "
                         "third retry, at `270 ms`, is one this budget cannot make.")),
            ("p", "The independence assumption in that example deserves the same "
                  "scepticism it got in &ldquo;Hedged Requests&rdquo;. If the call timed "
                  "out because the far side is overloaded, the retry is a second request "
                  "to an overloaded service and its probability of timing out is not "
                  "`1/100`; it is close to `1`. Retries against a saturated dependency "
                  "are not a reliability mechanism, they are a load multiplier, which is "
                  "why the retry count is capped and why the cap matters more than its value."),
            ("p", "Two figures should therefore be quoted together whenever a timeout is "
                  "proposed: the worst case `(r + 1) × T` against the allocation, and the "
                  "kill fraction `1 − F(T)` against the measured distribution. A timeout "
                  "chosen without the second is a number chosen without knowing what it "
                  "throws away, and on this sample the difference between the p99 and the "
                  "mean is a factor of fifteen in exactly that quantity."),
        ],
        "lab": ("latency", {
            "mode": "timeout",
            "panel_title": "Set the timeout and the retries",
            "panel_intro": "The worst case and the killed fraction are computed against "
                           "the sample you type in, and the panel says whether the pair "
                           "fits the budget. Slide the timeout down toward the mean and "
                           "watch the killed fraction climb while the worst case improves.",
        }),
        "steps_title": "Choosing a timeout and a retry count",
        "steps_intro": "Both numbers at once, because each one constrains the other through the budget.",
        "steps": [
            ("Take the allocation this call was given by the budget",
             "It is the figure from &ldquo;Latency Budgets&rdquo;, and it is what the "
             "worst case has to fit inside. Without it there is no constraint and any "
             "timeout looks defensible."),
            ("Read `1 − F(T)` off the measured distribution for candidate timeouts",
             "Not a guess and not a mean: the actual proportion of calls that finish "
             "after `T`. Try the median, the p95 and the p99 and write down the kill "
             "fraction for each. The three numbers usually settle the question by "
             "themselves."),
            ("Choose `r` so that `(r + 1) × T` fits the allocation",
             "Divide the allocation by the timeout and round down; that is the largest "
             "number of attempts available, and one less than it is the retry count. If "
             "the answer is zero attempts, the timeout is too large for the budget and "
             "one of the two has to move."),
            ("Quote the worst case and the kill fraction together",
             "A timeout proposal with only one of those numbers is incomplete. Add the "
             "failure probability `(1 − F(T))ʳ⁺¹` if the attempts are plausibly "
             "independent, and say so explicitly if they are not."),
        ],
        "worked": {
            "title": "A 250 ms allocation against a hundred measured calls",
            "intro": [
                "Three candidate timeouts, the same distribution, and the budget doing "
                "the deciding."
            ],
            "lines": [
                "sample     8:45  11:25  16:15  24:8  45:4  90:2  400:1",
                "           p50 11 ms   p95 45 ms   p99 90 ms   mean 18.27 ms",
                "budget     250 ms for this call",
                "",
                "T = 18 ms  (at the mean)",
                "   killed    1 − F(18) = 15/100          = 15.00%",
                "   worst     (1 + 1) × 18                =  36 ms      fits easily",
                "   both lost (15/100)²                   =   2.25%",
                "   verdict   cheap and wrong: 15 good calls in 100 discarded",
                "",
                "T = 45 ms  (at the p95)",
                "   killed    1 − F(45) = 3/100           =  3.00%",
                "   worst     2 × 45                      =  90 ms      fits",
                "   both lost (3/100)²                    =  0.09%",
                "",
                "T = 90 ms  (at the p99)",
                "   killed    1 − F(90) = 1/100           =  1.00%",
                "   worst     2 × 90                      = 180 ms      fits",
                "   both lost (1/100)²  = 1/10 000        =  0.01%",
                "   with r = 2:  3 × 90 = 270 ms          >  250 ms     does NOT fit",
                "",
                "choose     T = 90 ms, r = 1:  180 ms worst case, 1% killed,",
                "                              call lost once in ten thousand",
            ],
            "after": [
                "The budget is what eliminated the third retry, and it did so without "
                "any judgement about reliability at all: `270 ms` does not fit inside "
                "`250 ms`. That is the value of having done the budget first. Without it "
                "the retry count is chosen by taste, and taste has no way of knowing that "
                "the third attempt would break an end-to-end promise made three lessons ago.",
                "Notice the `T = 125 ms` row in the lab, which uses the entire `250 ms` "
                "on two attempts and kills exactly the same `1%` as `T = 90 ms`. The "
                "extra `35 ms` of patience rescues nothing, because the distribution has "
                "nothing in it between `90 ms` and `400 ms`. Timeouts should be placed "
                "against the gaps in the measured distribution, and the gaps are visible "
                "only if the distribution is looked at.",
                "For a faded rehearsal, keep the sample and set the allocation to "
                "`150 ms`. The supplied first move is the attempt count at the p99 "
                "timeout: `⌊150 / 90⌋ = 1`, so no retry is available there. Work out "
                "whether `T = 45 ms` with one retry fits, what it kills, and what its "
                "failure probability is, then decide between the two and write down the "
                "two figures you would quote. Check them on the lab&rsquo;s sliders "
                "before opening the quiz.",
            ],
        },
        "quiz_title": "Timeouts, retries and what they discard",
        "quiz": [
            {"q": "A call has a `250 ms` allocation. With `T = 90 ms`, what is the largest retry count that fits?",
             "a": ["`r = 0`", "`r = 1`", "`r = 2`", "`r = 3`"],
             "c": 1,
             "why": "The worst case is `(r + 1) × T`, so `r = 1` costs `180 ms` and fits "
                    "while `r = 2` costs `270 ms` and does not. `r = 0` fits but leaves "
                    "reliability on the table: the retry takes the failure probability "
                    "from `1/100` to `1/10 000` for `90 ms` of reservation the budget "
                    "already has."},
            {"q": "On the lab&rsquo;s sample, the mean call takes `18.27 ms`. What does a timeout at `18 ms` discard?",
             "a": ["Half the calls, since the mean is the middle",
                   "`15%` of calls that would have succeeded",
                   "`1%`, the same as a timeout at the p99",
                   "Nothing: calls slower than the mean have already failed"],
             "c": 1,
             "why": "`F(18) = 85/100`, so `15%` of calls finish after `18 ms` and are "
                    "abandoned despite being on their way to succeeding. The mean is not "
                    "the middle &mdash; the median is `11 ms` and `85%` of calls are "
                    "below the mean. A timeout at the p99 kills `1%`, fifteen times less."},
            {"q": "Attempts at `T = 90 ms` are abandoned `1%` of the time. With one retry, how often is the call lost entirely?",
             "a": ["`2%`", "`1%`", "`0.01%`", "It cannot be computed"],
             "c": 2,
             "why": "If the two attempts are independent, both are abandoned with "
                    "probability `(1/100)² = 1/10 000`, which is `0.01%`. `2%` adds the "
                    "probabilities, which is the wrong operation for a conjunction. The "
                    "real caution is the independence: if the call timed out because the "
                    "dependency is saturated, the retry faces the same saturation and "
                    "`0.01%` is far too optimistic."},
        ],
        "mistakes": [
            ("Setting the timeout at or near the mean",
             "The mean of a latency distribution sits in the sparse region above the "
             "bulk and below the tail. On the lab&rsquo;s sample a timeout there kills "
             "`15%` of good calls against the `1%` a p99 timeout kills, and it still "
             "does not catch the call that takes `400 ms` any sooner than a larger "
             "timeout would."),
            ("Budgeting the typical case instead of `(r + 1) × T`",
             "The budget has to hold the worst case, because the worst case is what "
             "happens when the dependency is in trouble &mdash; which is the only time "
             "any of this matters. A retry count chosen against the typical case will be "
             "exactly wrong at exactly the wrong moment."),
            ("Assuming retries are independent of the failure that caused them",
             "`(1 − F(T))ʳ⁺¹` requires the attempts to be independent draws. A timeout "
             "caused by an overloaded dependency is not independent of the retry sent to "
             "the same dependency, and the retry adds load to the thing that was already "
             "failing. Cap the retries, and treat the computed failure probability as "
             "the optimistic end of a range."),
        ],
        "standard": ("Finish when a proposed timeout makes you ask what it throws away.",
                     "You should be able to compute `(r + 1) × T` against an allocation, "
                     "read `1 − F(T)` off a measured distribution for several candidate "
                     "timeouts, choose the largest retry count the budget permits, and "
                     "state the failure probability together with the assumption it rests on."),
        "note": 'Everything in this course has been about one request&rsquo;s time. &ldquo;Packet Loss and Throughput&rdquo; closes it with the other side of the same round trip: a single connection&rsquo;s sustained rate is bounded by its round-trip time and its loss rate together, which is why a cross-region transfer can be slow on a link with capacity to spare.',
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "packet-loss-and-throughput",
        "title": "Packet Loss and Throughput",
        "module": "Budgets and limits",
        "one_line": "Compute the loss-limited bound on one TCP flow and the number of parallel streams needed to fill a link.",
        "summary": (
            "A single TCP flow cannot sustain more than about `(MSS/RTT) × 1/√p`, where "
            "`p` is the loss rate. At `1460`-byte segments, a `100 ms` round trip and "
            "one percent loss that is `1.168 Mbit/s` &mdash; on a link of any capacity "
            "whatever. Filling a ten-gigabit link under those conditions needs `8 562` "
            "parallel streams, which is why a slow cross-region copy is usually a "
            "flow-count problem rather than a bandwidth one."
        ),
        "key": [
            "Mathis bound   rate ≤ (MSS / RTT) × 1/√p",
            "1460 B, 100 ms, p = 1%:   1.168 Mbit/s, whatever the link is",
            "streams to fill 10 Gbit/s  =  ⌈10 000 / 1.168⌉  =  8 562",
            "halve the loss  → × √2 ≈ 1.414        halve the RTT  → × 2",
            "the square root is why this is the one rounded figure on the course",
        ],
        "key_label": "One flow’s ceiling, and the square root in it",
        "concepts_intro": (
            "The hard idea is that a link&rsquo;s capacity is an upper bound on what all "
            "flows together can do, and says almost nothing about what one flow will do."
        ),
        "concepts": [
            ("A flow’s rate is bounded by its round trip and its loss",
             "A congestion-controlled sender grows its window until a loss, then cuts it. "
             "Averaged over that cycle the sustainable rate comes out proportional to "
             "`MSS/RTT` and inversely proportional to `√p`. The link capacity does not "
             "appear in the expression at all, which is the entire surprise."),
            ("The round trip enters linearly and the loss as a square root",
             "Halving the round-trip time doubles the bound: the same `1460 B` at "
             "`1%` loss gives `1.168 Mbit/s` at `100 ms` and `11.680 Mbit/s` at "
             "`10 ms`. Halving the loss multiplies it by `√2`, about `1.414`. Doubling "
             "the loss from `1%` to `2%` gives `0.826 Mbit/s`, not `0.584` &mdash; and "
             "`0.584` is what doubling the round trip would give instead."),
            ("Parallel streams are how the gap is closed",
             "If one flow is bounded at `1.168 Mbit/s` and the link carries "
             "`10 000 Mbit/s`, then `⌈10 000 / 1.168⌉ = 8 562` concurrent flows are "
             "needed to use it. That figure is the honest reason bulk transfer tools "
             "open many connections, and it is a number to compute before concluding "
             "that a link was mis-sold."),
        ],
        "read_title": "One flow, bounded by two numbers that are not the link",
        "read_intro": "Where the square root comes from, what it does to the arithmetic, and the one place this course rounds.",
        "body": [
            ("p", "A team copies a dataset between two regions over a ten-gigabit link "
                  "and measures a little over a megabit a second. The link is not the "
                  "problem, the disks are not the problem, and nothing is broken. The "
                  "transfer is using one TCP connection over a `100 ms` round trip with "
                  "one percent packet loss, and that combination has a ceiling."),
            ("def", ("Mathis bound",
                     "For a loss rate `p`, a maximum segment size `MSS` and a round-trip "
                     "time `RTT`, a single congestion-controlled flow sustains at most "
                     "approximately `(MSS / RTT) × (1 / √p)`. It is a bound on the "
                     "average rate over many congestion cycles, derived from the "
                     "sawtooth of window growth and halving; it ignores timeouts, "
                     "receive-window limits and the slow-start phase, so a real flow "
                     "achieves this or less.")),
            ("math", [
                "MSS = 1460 B    RTT = 100 ms    p = 1% = 1/100",
                "",
                "MSS / RTT   =  1460 B / 0.1 s        =  14 600 B/s",
                "1 / √p      =  1 / √0.01             =  10",
                "",
                "bound       =  14 600 × 10           =  146 000 B/s",
                "            =  146 000 × 8 / 10⁶     =  1.168 Mbit/s",
                "",
                "link          10 000 Mbit/s",
                "streams     =  ⌈10 000 / 1.168⌉      =  8 562",
            ]),
            ("p", "The bound is `1.168 Mbit/s` and the link is `10 Gbit/s`. The flow is "
                  "using about one ten-thousandth of the capacity that was bought, and "
                  "buying more capacity changes the numerator of nothing. What would "
                  "change the answer is a shorter round trip, a lower loss rate, a larger "
                  "segment, or more flows &mdash; and the `8 562` figure prices the last "
                  "of those exactly."),
            ("h3", "The square root, and why it matters more than it looks"),
            ("ul", [
                "`p = 0.1%` &mdash; bound `3.694 Mbit/s`, `2 708` streams to fill the link",
                "`p = 0.5%` &mdash; bound `1.652 Mbit/s`, `6 054` streams",
                "`p = 1%` &mdash; bound `1.168 Mbit/s`, `8 562` streams",
                "`p = 2%` &mdash; bound `0.826 Mbit/s`, `12 108` streams",
                "`p = 5%` &mdash; bound `0.522 Mbit/s`, `19 145` streams",
            ]),
            ("p", "Loss enters as `1/√p`, so a factor of two in loss is a factor of "
                  "`√2` in throughput, not a factor of two. Going from `1%` to `2%` "
                  "takes the bound from `1.168` to `0.826 Mbit/s` &mdash; it multiplies "
                  "by `1/√2 ≈ 0.707`, and a reader who expected `0.584` has applied the "
                  "wrong rule. Going the other way is the same story in reverse: halving "
                  "the loss buys `41%` more throughput, not `100%` more, which is why "
                  "loss reduction has diminishing returns and round-trip reduction does "
                  "not."),
            ("example", ("The two levers, priced against each other",
                         "At `1460 B` and `1%` loss, moving the round trip from `100 ms` "
                         "to `10 ms` &mdash; a nearer region &mdash; takes the bound from "
                         "`1.168` to `11.680 Mbit/s`, exactly ten times, because `RTT` is "
                         "in the denominator linearly. Moving the loss from `1%` to "
                         "`0.1%` &mdash; a tenfold improvement in a much harder quantity "
                         "&mdash; takes it to `3.694 Mbit/s`, a factor of `√10 ≈ 3.16`. "
                         "Distance is the more powerful lever by a factor of three, and "
                         "it is also the one &ldquo;The Speed-of-Light Floor&rdquo; said "
                         "was the only one physics cares about.")),
            ("p", "One honesty note about the arithmetic, because this lesson is the "
                  "exception on this course. Every other figure in these eleven labs is "
                  "an exact fraction: percentiles are ranks, convolutions are enumerated "
                  "pairs, and budgets are subtractions. This bound contains `√p`, and a "
                  "square root of a rational is usually irrational &mdash; `√(1/50)`, the "
                  "root needed at two percent loss, has no rational value at all. So the "
                  "`mathis` mode computes its root by Newton&rsquo;s method to fifteen "
                  "decimal places and says on its face that it has done so. Every figure "
                  "on that panel inherits the rounding, and no other page on the course does."),
            ("p", "Two limits on the model itself. It is a bound on the average rate, so "
                  "a real flow reaches it at best and usually less: retransmission "
                  "timeouts, a receive window too small for the bandwidth-delay product, "
                  "and slow start all cost more. And it describes loss-based congestion "
                  "control; a flow using a rate-based or delay-based controller is not "
                  "governed by this sawtooth and is not described by this formula. Read "
                  "it as the ceiling a classical flow cannot pass, which is exactly the "
                  "use it gets put to."),
            ("p", "The misconception it exists to correct is short enough to state in "
                  "one sentence: a ten-gigabit link does not give a ten-gigabit flow. The "
                  "link capacity is a bound on the aggregate; a single connection is "
                  "bounded by its own round-trip time and loss rate, and those two "
                  "numbers were never on the invoice."),
        ],
        "lab": ("latency", {
            "mode": "mathis",
            "panel_title": "Set the path",
            "panel_intro": "The bound is the one figure on this course computed in "
                           "floating point, because `1/√p` is usually irrational. The "
                           "panel labels the rounding. Move the loss rate first and watch "
                           "the bound fall as a square root rather than in proportion.",
        }),
        "steps_title": "Bounding one flow",
        "steps_intro": "Four steps, and the fourth is the one that stops the wrong invoice being blamed.",
        "steps": [
            ("Get `MSS`, `RTT` and the loss rate for the actual path",
             "The segment size is typically `1460 B` on a standard ethernet path and "
             "larger with jumbo frames. The round trip and the loss rate come from "
             "measurement, not from the contract, and the loss rate is the one people "
             "most often do not have."),
            ("Compute `MSS / RTT` in bytes a second",
             "Keep the round trip in seconds for this line. `1460 B / 0.1 s` is "
             "`14 600 B/s`. This is the per-round-trip rate of one segment, and it is "
             "the whole of the bound when the loss rate is one hundred percent."),
            ("Multiply by `1 / √p` and convert to bits",
             "The square root is the step to do carefully: `√0.01 = 0.1`, so `1/√p` is "
             "`10`, not `100`. Multiply by eight and divide by `10⁶` for megabits a "
             "second, and expect a figure far below the link rate."),
            ("Divide the link capacity by the bound to get the stream count",
             "Round up. `⌈10 000 / 1.168⌉ = 8 562` says how many concurrent flows the "
             "link needs before its capacity is reachable at all &mdash; and if that "
             "number is implausible, the fix is the round trip or the loss, not the link."),
        ],
        "worked": {
            "title": "One flow over a 10 Gbit/s intercontinental link",
            "intro": [
                "The link is enormous, the transfer is slow, and nothing is broken. The "
                "bound explains it in four lines."
            ],
            "lines": [
                "path       MSS 1460 B    RTT 100 ms    loss p = 1% = 1/100",
                "link       10 000 Mbit/s",
                "",
                "MSS / RTT  =  1460 / 0.1                =   14 600 B/s",
                "1 / √p     =  1 / √0.01  =  1 / 0.1     =       10",
                "bound      =  14 600 × 10               =  146 000 B/s",
                "           =  146 000 × 8 / 10⁶         =    1.168 Mbit/s",
                "",
                "utilisation of the link by one flow:  1.168 / 10 000  ≈  0.0117%",
                "streams to fill it:  ⌈10 000 / 1.168⌉   =  8 562",
                "",
                "what changes it:",
                "   RTT 100 → 10 ms       bound → 11.680 Mbit/s     × 10",
                "   loss 1% → 0.1%        bound →  3.694 Mbit/s     × √10 ≈ 3.16",
                "   loss 1% → 2%          bound →  0.826 Mbit/s     × 1/√2 ≈ 0.707",
                "   link 10 → 40 Gbit/s   bound →  1.168 Mbit/s     unchanged",
            ],
            "after": [
                "The last line is the one to keep. Quadrupling the link changes the bound "
                "by nothing at all, because the link capacity does not appear in the "
                "formula. Every hour spent on a bandwidth upgrade for a single-stream "
                "transfer is an hour spent on a term that is not in the expression.",
                "The `× √10 ≈ 3.16` line is the one that gets misread. A tenfold "
                "reduction in loss &mdash; from one percent to one in a thousand, which "
                "is a serious network engineering achievement &mdash; buys a factor of "
                "three in throughput. Meanwhile moving the endpoint from `100 ms` to "
                "`10 ms` away buys a factor of ten. The square root is not a detail of "
                "the formula; it is the reason the two levers are ranked the way they are.",
                "For a faded rehearsal, take a jumbo-frame path: `MSS = 9000 B`, "
                "`RTT = 40 ms`, `p = 0.5%`, over a `1 Gbit/s` link. The supplied first "
                "move is `MSS / RTT = 9000 / 0.04 = 225 000 B/s`. Compute `1/√p`, the "
                "bound in megabits a second, and the number of streams needed to fill the "
                "link. Then say which single change &mdash; halving the round trip or "
                "halving the loss &mdash; buys more, and by what factor. Check the figures "
                "on the lab&rsquo;s sliders before opening the quiz.",
            ],
        },
        "quiz_title": "One flow against a large link",
        "quiz": [
            {"q": "A path has `MSS = 1460 B`, `RTT = 100 ms` and `1%` loss. Roughly what can one flow sustain?",
             "a": ["`1.168 Mbit/s`", "`11.68 Mbit/s`", "`116.8 Mbit/s`", "Whatever the link allows"],
             "c": 0,
             "why": "`1460 / 0.1 = 14 600 B/s`, times `1/√0.01 = 10`, is `146 000 B/s`, "
                    "which is `1.168 Mbit/s`. `11.68` would follow from a `10 ms` round "
                    "trip. The last option is the misconception the bound exists to "
                    "correct: the link capacity is not in the formula."},
            {"q": "The loss rate doubles from `1%` to `2%`. What happens to the bound?",
             "a": ["It halves, to `0.584 Mbit/s`",
                   "It falls by a factor of `√2`, to `0.826 Mbit/s`",
                   "It is unchanged, since loss is already accounted for",
                   "It quarters, to `0.292 Mbit/s`"],
             "c": 1,
             "why": "Loss enters as `1/√p`, so doubling it multiplies the bound by "
                    "`1/√2 ≈ 0.707`: `1.168` becomes `0.826 Mbit/s`. `0.584` is exactly "
                    "half, which is what doubling the <em>round-trip time</em> would give "
                    "&mdash; the round trip is linear and the loss is a square root, and "
                    "swapping the two rules is the error this question is about."},
            {"q": "A `10 Gbit/s` link carries a single flow bounded at `1.168 Mbit/s`. How many parallel streams would fill the link?",
             "a": ["`10`", "`856`", "`8 562`", "It cannot be filled at all"],
             "c": 2,
             "why": "`⌈10 000 / 1.168⌉ = 8 562`. The bound is per flow, so concurrency is "
                    "the lever that converts it into link utilisation &mdash; which is "
                    "exactly why bulk transfer tools open many connections. `856` is out "
                    "by a factor of ten, and the link certainly can be filled; it just "
                    "cannot be filled by one connection."},
        ],
        "mistakes": [
            ("Expecting one flow to reach the link rate",
             "A `10 Gbit/s` link gives one flow `1.168 Mbit/s` at a `100 ms` round trip "
             "and one percent loss, because neither the capacity nor the price appears in "
             "the bound. The link rate bounds every flow together; the Mathis bound "
             "bounds each one separately, and the two can differ by four orders of magnitude."),
            ("Treating loss as linear",
             "Doubling the loss does not halve the throughput, it multiplies it by "
             "`1/√2`. Halving the loss does not double it, it multiplies by `1.414`. "
             "Every plan built on the linear reading over-promises what a loss reduction "
             "will achieve and under-values moving the endpoint closer."),
            ("Quoting the bound as an exact figure",
             "`1/√p` is irrational for most loss rates &mdash; `√(1/50)` has no rational "
             "value &mdash; so the lab computes it by Newton&rsquo;s method and labels "
             "the panel accordingly. It is also a bound on an average rate, so a real "
             "flow achieves it at best. Quote it as a ceiling, to three or four "
             "significant figures, and not as a prediction."),
        ],
        "standard": ("Finish when a slow single-stream transfer makes you ask for the loss rate, not the link rate.",
                     "You should be able to compute `(MSS/RTT) × 1/√p` for a described "
                     "path, convert it to megabits a second, work out how many parallel "
                     "streams a given link would need, and say which of the round trip "
                     "and the loss rate is the more valuable thing to improve and by what factor."),
        "note": 'That is the course. Latency had a floor set by distance, a multiplier set by the round-trip count, and a shape set by the longest path through the stage graph; the tail turned out to be a rank rather than an average, to amplify under fan-out and shrink under hedging, and to refuse to add across stages; and the budget held all of it, with a timeout and a retry count fitted inside. What none of it explained is where the tail came from in the first place. Queues and Utilisation is the answer: the tail is what waiting in line looks like, and it is a function of how busy the server is.',
    },
]
