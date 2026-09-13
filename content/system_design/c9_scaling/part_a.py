"""Scaling Laws and Cost, lessons 01-06 - the two scaling laws, two shapes, two ways of paying."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "amdahls-law",
        "title": "Amdahl's Law",
        "module": "What a machine buys",
        "one_line": "Compute the speedup n machines give, the ceiling it never passes, and the n that reaches a stated fraction of that ceiling.",
        "summary": (
            "A job splits into a part that can be shared out and a part that cannot. "
            "Machines shrink the first and leave the second exactly as it was, so the "
            "speedup climbs toward `1/(1 − p)` and stops there. Five per cent of "
            "serial work caps the whole job at twenty times, and no machine count "
            "anywhere on the curve changes that number."
        ),
        "key": [
            "S(n) = 1/((1 − p) + p/n)          p is the parallel share of the runtime",
            "ceiling  S(∞) = 1/(1 − p)         p = 19/20 → 20×, for every n",
            "S(32) = 640/51 = 12.549×          62.75% of the ceiling",
            "n ≥ (f/(1 − f))·(p/(1 − p))       f = 9/10 → 9 × 19 = 171 machines",
            "efficiency  S(n)/n = 39.22%       at n = 32, and 10.5% at n = 171",
        ],
        "key_label": "One fraction that never shrinks, and the ceiling it sets",
        "concepts_intro": (
            "One equation, and then the two things it is usually misread about: where "
            "its limit is, and what you paid for the part of the curve you are on."
        ),
        "concepts": [
            ("The serial part is a duration, not a share",
             "Split the runtime on one machine into `p` that can be spread across "
             "machines and `1 − p` that cannot. Adding machines divides the first by "
             "`n` and does nothing whatever to the second, so the total time falls to "
             "`(1 − p) + p/n` of what it was and the speedup is the reciprocal. The "
             "serial piece is not a percentage that shrinks as the rest does &mdash; "
             "it is a fixed stretch of wall-clock time, and at large `n` it is "
             "essentially the whole runtime."),
            ("The ceiling is an asymptote, so no table shows it",
             "`p/n` falls toward zero and never reaches it, so `S(n)` rises toward "
             "`1/(1 − p)` and never reaches that either. At `p = 19/20` the ceiling is "
             "`20×`: two machines give `1.905×`, thirty-two give `12.549×`, and five "
             "hundred and twelve give `19.284×`. Reading a table of the first few rows "
             "tells you the curve is bending; only the asymptote tells you what it is "
             "bending toward."),
            ("Efficiency is the half of the answer that gets dropped",
             "`S(n)/n` is the share of each machine you are actually using. At "
             "`n = 32` it is `20/51`, or `39.22%` &mdash; three fifths of the fleet is "
             "waiting on the serial part. At the `171` machines that reach ninety per "
             "cent of the ceiling it is `10.5%`. A speedup quoted without its "
             "efficiency hides what the speedup cost."),
        ],
        "read_title": "The speedup, the ceiling, and the machines it takes to approach one",
        "read_intro": (
            "Where the formula comes from, why its limit is the interesting part, and "
            "the closed form for the machine count that reaches a fraction of it."
        ),
        "body": [
            ("def", ("Amdahl's Law",
                     "Let `p` be the fraction of a job&rsquo;s single-machine runtime "
                     "that can be executed in parallel, so `1 − p` is the "
                     "<strong>serial fraction</strong>. On `n` machines the runtime "
                     "becomes `(1 − p) + p/n` of the original, and the "
                     "<strong>speedup</strong> is",
                     "`S(n) = 1/((1 − p) + p/n)`.",
                     "The model assumes the parallel part divides perfectly, the "
                     "machines are identical, and coordinating them is free. All three "
                     "are optimistic, which is why this curve is an upper bound.")),
            ("p", "Normalise the one-machine runtime to `1`. The serial part takes "
                  "`1 − p` no matter how many machines are present; the parallel part "
                  "takes `p` on one machine and `p/n` on `n`. Add them, and the "
                  "speedup is the ratio of the old runtime to the new one."),
            ("math", [
                "one machine     (1 − p)  +  p        =  1",
                "n machines      (1 − p)  +  p/n",
                "",
                "S(n) = 1 / ((1 − p) + p/n)",
                "",
                "p = 19/20,  n = 32:",
                "  (1/20) + (19/20)/32  =  32/640 + 19/640  =  51/640",
                "  S(32) = 640/51 = 12.549…×",
            ]),
            ("thm", ("The ceiling",
                     "As `n` grows without bound, `p/n → 0`, so",
                     "`S(n) → 1/(1 − p)`,",
                     "and because `p/n > 0` for every finite `n`, `S(n)` is strictly "
                     "below `1/(1 − p)` at every machine count. The bound depends on "
                     "the serial fraction alone: the hardware does not appear in it.")),
            ("p", "This is the whole point of the law and the reason it is worth a "
                  "lesson. A curve that climbs more and more slowly could be climbing "
                  "toward anything; this one is climbing toward a number you can write "
                  "down before you buy a single machine. The reciprocal of the serial "
                  "fraction is the answer, and &ldquo;Graphs and Asymptotes&rdquo; on "
                  "the Algebra path is where reading a limit off a curve was set up."),
            ("example", ("Five per cent serial, and a fleet that cannot help",
                         "`p = 19/20` gives a ceiling of `20×`. Two machines reach "
                         "`40/21 = 1.905×`; four reach `80/23 = 3.478×`; eight reach "
                         "`160/27 = 5.926×`; thirty-two reach `640/51 = 12.549×`. Each "
                         "doubling adds less than the one before, and the sequence is "
                         "converging on `20` rather than on anything larger. A team "
                         "that has measured the first three rows and extrapolated a "
                         "line through them will budget for a speedup that does not "
                         "exist.")),
            ("h3", "Reaching a stated fraction of the ceiling"),
            ("p", "Since the ceiling is never reached, the useful question is how many "
                  "machines it takes to get a given share of the way there. Write the "
                  "target as a fraction `f` of the ceiling and solve the inequality: "
                  "the algebra is one cross-multiplication and it leaves no root and no "
                  "logarithm behind."),
            ("math", [
                "want    S(n) ≥ f · 1/(1 − p)",
                "",
                "        1/((1 − p) + p/n)  ≥  f/(1 − p)",
                "        (1 − p)            ≥  f·(1 − p) + f·p/n",
                "        (1 − p)(1 − f)     ≥  f·p/n",
                "",
                "        n  ≥  (f/(1 − f)) · (p/(1 − p))",
                "",
                "f = 9/10, p = 19/20:   9 × 19 = 171 machines",
                "and S(171) = 1/(1/20 + 19/3420) = 1/(190/3420) = 18 = 0.9 × 20",
            ]),
            ("p", "The two factors are worth reading separately. `f/(1 − f)` is the "
                  "odds of the target &mdash; nine for ninety per cent, ninety-nine for "
                  "ninety-nine &mdash; and `p/(1 − p)` is the ratio of parallel work to "
                  "serial work. The machine count is their product, so tightening the "
                  "target from ninety to ninety-nine per cent costs eleven times as "
                  "many machines against the same code."),
            ("p", "The lab finds `171` twice: once by scanning integer `n` until the "
                  "speedup clears the target, and once by evaluating the product above "
                  "and rounding up. Two routes to one integer is the check, and the "
                  "scan is the one that carries the claim &mdash; a closed form that "
                  "happens to agree is a check on the algebra, not a substitute for it."),
            ("h3", "What efficiency says about the same point"),
            ("p", "`S(n)/n` is the fraction of a machine each machine contributes. It "
                  "starts at `1` and falls monotonically: `95.2%` at two machines, "
                  "`74.1%` at eight, `39.22%` at thirty-two, `10.5%` at the one hundred "
                  "and seventy-one that reach ninety per cent of the ceiling. Every one "
                  "of those machines is paid for in full."),
            ("example", ("What the second thirty-two machines buy",
                         "At `p = 19/20`, thirty-two machines give `640/51 = 12.549×` "
                         "and sixty-four give `1280/83 = 15.422×`. The second block of "
                         "thirty-two adds a factor of `1.23`, and everything still "
                         "unbought above it is the `20/12.549 = 1.59×` between here and "
                         "the ceiling &mdash; which no purchase can close. That is the "
                         "arithmetic a &ldquo;double the fleet, halve the runtime&rdquo; "
                         "plan is up against.")),
            ("p", "One caution about `p` itself. It is a share of <em>time</em> measured "
                  "on one machine, not a share of code or of functions: a lock held for "
                  "a tenth of the runtime is a tenth of the serial fraction even if it "
                  "is two lines. This course takes `p` as given. Measuring it is "
                  "&ldquo;Measuring Systems&rdquo;, and it is harder than this lesson."),
        ],
        "lab": ("scale", {
            "mode": "amdahl",
            "panel_title": "Set the parallel fraction and add machines",
            "panel_intro": (
                "`S(n)`, the ceiling and the machine count that reaches a stated "
                "fraction of it are exact fractions of the parallel fraction you set. "
                "Watch the grey line &mdash; `n` machines, `n` times faster &mdash; "
                "leave the curve behind, and watch the machine count that reaches the "
                "target come out the same by a scan over integers and by the product "
                "`(f/(1 − f))·(p/(1 − p))`."
            ),
        }),
        "steps_title": "Costing a parallelisation before you buy it",
        "steps_intro": "The ceiling first, because it decides whether the rest of the arithmetic is worth doing.",
        "steps": [
            ("Write down the serial fraction and invert it",
             "`1/(1 − p)` is the most the job can ever go faster. If that number is "
             "below what the plan needs, no machine count rescues it and the next move "
             "is to shrink `1 − p`, not to buy."),
            ("Evaluate `S(n)` at the size you were actually going to buy",
             "Substitute into `1/((1 − p) + p/n)` and keep it as a fraction. Compare it "
             "to `n` &mdash; the speedup people assume &mdash; and to the ceiling, and "
             "report the gaps to both."),
            ("Divide by `n` and report the efficiency",
             "`S(n)/n` is the share of each machine you are using. It is the figure "
             "that turns a speedup into a bill, and quoting a speedup without it is how "
             "a `12.5×` result on thirty-two machines gets called a success."),
            ("Solve for the machine count your target needs",
             "`n ≥ (f/(1 − f))·(p/(1 − p))`, rounded up. Do it for two targets, not "
             "one: the jump from ninety to ninety-nine per cent of the ceiling "
             "multiplies the fleet by eleven, and seeing that pair is what makes the "
             "target a decision."),
            ("Say out loud what the model has assumed away",
             "Perfect division of the parallel part, identical machines, free "
             "coordination. Every one of those is generous, so `S(n)` is an upper "
             "bound &mdash; and &ldquo;The Universal Scalability Law&rdquo; is the "
             "lesson that charges for the third one."),
        ],
        "worked": {
            "title": "p = 19/20: the ceiling, thirty-two machines, and the 90% point",
            "intro": [
                "Everything below is an exact fraction of `p = 19/20`. The decimals are "
                "printed only where a reader wants to compare two of them by eye."
            ],
            "lines": [
                "serial fraction   1 − p = 1/20",
                "ceiling           1/(1 − p) = 20×",
                "",
                "S(32) = 1/((1/20) + (19/20)/32)",
                "      = 1/(32/640 + 19/640)",
                "      = 640/51  =  12.549…×",
                "",
                "fraction of the ceiling   (640/51)/20 = 32/51 = 62.75%",
                "efficiency                (640/51)/32 = 20/51 = 39.22%",
                "the linear expectation    32× , which overstates by 32/(640/51) = 2.55",
                "",
                "90% of the ceiling:",
                "  n ≥ (0.9/0.1)·(0.95/0.05) = 9 × 19 = 171",
                "  S(171) = 1/((1/20) + (19/20)/171)",
                "         = 1/(171/3420 + 19/3420)",
                "         = 3420/190 = 18       and  18 = 0.9 × 20   ✓",
                "  efficiency at 171          18/171 = 10.5%",
            ],
            "after": [
                "The `S(171) = 18` line is the one doing the work. `171` came out of an "
                "inequality, and substituting it back gives exactly `18`, which is "
                "exactly nine tenths of `20` &mdash; so the algebra and the definition "
                "of the target agree on the nose rather than to three decimal places.",
                "Notice what `171` machines bought: `18×` where the honest linear "
                "expectation was `171×`, at `10.5%` efficiency. Ninety per cent of the "
                "ceiling is a long way past the point where the fleet is mostly idle.",
                "For a faded attempt, take `p = 4/5`. Write down the ceiling, then "
                "`S(8)` and `S(64)` as fractions, then the efficiency at each, then the "
                "`n` that reaches ninety per cent. Predict which of the two speedups is "
                "closer to half the ceiling before you compute either, and check your "
                "four answers against the lab with the parallel fraction set to 80%.",
            ],
        },
        "quiz_title": "Ceilings, speedups and what they cost",
        "quiz": [
            {"q": "A job is 80% parallel. What is the largest speedup any number of machines can give it?",
             "a": ["`1.25×`", "`4×`", "`5×`", "`20×`"],
             "c": 2,
             "why": "The ceiling is `1/(1 − p) = 1/(1/5) = 5×`. `1.25×` is `1/p`, which "
                    "is the reciprocal of the wrong fraction. `4×` is `p/(1 − p)`, the "
                    "ratio of parallel work to serial work &mdash; a factor in the "
                    "machine-count formula, not a speedup. `20×` is the ceiling for a "
                    "95% parallel job, which is the case the lab opens on."},
            {"q": "At `p = 19/20` and `n = 32` the speedup is `640/51 ≈ 12.549×`. What is the efficiency?",
             "a": ["`39.22%`", "`62.75%`", "`95.00%`", "`12.55%`"],
             "c": 0,
             "why": "Efficiency is `S(n)/n = (640/51)/32 = 20/51 = 39.22%`. `62.75%` is "
                    "`S(n)` divided by the <em>ceiling</em> rather than by `n` &mdash; "
                    "how far up the curve you are, which is a different question. "
                    "`95.00%` is the input `p`. `12.55%` is the speedup with a per cent "
                    "sign written after it, which is not a quantity at all."},
            {"q": "At `p = 19/20`, thirty-two machines give `12.549×` and sixty-four give `15.422×`. What does the second thirty-two buy, and what is left to buy?",
             "a": ["another `12.549×`, because the fleet doubled",
                   "a factor of `1.23`, with at most `1.59×` still available at any price",
                   "nothing, because the ceiling has already been reached",
                   "a factor of `2`, since speedup is linear in the machine count"],
             "c": 1,
             "why": "`15.422/12.549 = 1.23`, and the whole distance left to the ceiling "
                    "is `20/12.549 = 1.59×` &mdash; not reachable, only approachable. "
                    "The first option is the linear assumption the law contradicts; the "
                    "third is false because the curve is still rising (`15.422 > "
                    "12.549`) and never touches `20`; the fourth states the same linear "
                    "assumption as a principle."},
            {"q": "What has to be true for `n` machines to make a job exactly `n` times faster?",
             "a": ["`p = 1`: no part of the runtime is serial",
                   "`p ≥ 0.99`",
                   "`n` is small enough that the serial part has not started to dominate",
                   "the machines are identical and the network is fast"],
             "c": 0,
             "why": "`S(n) = n` requires `(1 − p) + p/n = 1/n`, which forces `p = 1`. "
                    "Any positive serial fraction puts `S(n) < n` at every `n > 1`: at "
                    "`p = 0.99` the ceiling is `100×`, so two hundred machines are "
                    "already beaten by it. Small `n` narrows the gap without closing it "
                    "&mdash; at `p = 19/20`, two machines give `1.905×`, not `2×`. "
                    "Identical machines and free coordination are already assumed by "
                    "the model, so granting them changes nothing."},
        ],
        "mistakes": [
            ("Reading the ceiling off the largest `n` you tried",
             "The curve is still climbing at every finite machine count, so a table "
             "stopping at thirty-two rows looks like slow growth rather than a bound. "
             "`12.549×` at `n = 32` is `62.75%` of a ceiling the table never displays. "
             "The ceiling comes from `1/(1 − p)` before any row is computed, and the "
             "table is then read against it."),
            ("Treating `p` as a share of the code",
             "`p` is the share of the single-machine <em>runtime</em> that parallelises. "
             "A lock held for five per cent of the wall clock is a five per cent serial "
             "fraction and a `20×` ceiling, whether it guards two lines or two thousand. "
             "Counting functions instead of milliseconds usually produces a `p` that is "
             "far too high and a plan built on it."),
            ("Quoting a speedup with the efficiency left out",
             "`18×` sounds like a result until you see it took `171` machines, which is "
             "`10.5%` of each of them. Both numbers are in every row of the lab&rsquo;s "
             "table for this reason: the speedup says what happened and the efficiency "
             "says what it was bought with."),
        ],
        "standard": ("Finish when a ceiling reads as a fact about the serial fraction rather than as a limit of the hardware.",
                     "You should be able to write `1/(1 − p)` down before evaluating "
                     "anything, compute `S(n)` and `S(n)/n` as exact fractions at a "
                     "stated `n`, and produce the machine count for a target fraction "
                     "of the ceiling both by the inequality and by a scan, getting the "
                     "same integer twice."),
        "note": "Amdahl&rsquo;s curve rises to a plateau, which is already a "
                "disappointment. It is also the optimistic case: it charges nothing for "
                "the machines talking to each other. &ldquo;The Universal Scalability "
                "Law&rdquo; adds that charge, and the curve stops plateauing &mdash; it "
                "peaks and comes back down, so that past a certain fleet size the next "
                "machine makes throughput <em>worse</em>. If you take one shape away "
                "from this course, take that one.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-universal-scalability-law",
        "title": "The Universal Scalability Law",
        "module": "What a machine buys",
        "one_line": "Locate the machine count at which throughput peaks, and show that adding machines past it makes throughput fall.",
        "summary": (
            "Amdahl charges for work that cannot be shared. The Universal Scalability "
            "Law charges twice more: for contention on a shared resource, and for the "
            "cost of keeping every machine&rsquo;s copy of the state consistent with "
            "every other&rsquo;s. The second charge grows as `N²` while throughput "
            "grows as `N`, so the curve peaks and then falls."
        ),
        "key": [
            "C(N) = N/(1 + α(N − 1) + βN(N − 1))     α contention, β coherency",
            "β = 0   →   C(N) → 1/α = 50×            a plateau, Amdahl’s shape",
            "C(N+1) ≤ C(N)  ⟺  β·N(N + 1) ≥ 1 − α    the peak, over integers",
            "α = 1/50, β = 1/10000  →  N* = 99       peak 495000/19651 = 25.19×",
            "√((1 − α)/β) = 98.9949                  the same peak, rounded",
            "C(198) = 990000/44203 = 22.397×         twice the fleet, 88.9% of the peak",
        ],
        "key_label": "Three terms, and the one that turns the curve over",
        "concepts_intro": (
            "The new term is `β`. Everything surprising on this page follows from it "
            "being multiplied by `N²` while the thing it is divided into is only `N`."
        ),
        "concepts": [
            ("Two penalties, not one",
             "`α` is <strong>contention</strong>: a share of each request that has to "
             "queue for something only one machine can hold at a time. `β` is "
             "<strong>coherency</strong>: the cost of every machine agreeing with every "
             "other. With `β = 0` the law is Amdahl in different clothing and its "
             "ceiling is `1/α`. With `β > 0` it is a different shape entirely."),
            ("Agreement is quadratic in the fleet",
             "`N` machines have `N(N − 1)/2` pairs, and a protocol in which each must "
             "reconcile with each pays in proportion to that count. The numerator of "
             "`C(N)` grows like `N`; the `βN(N − 1)` term in the denominator grows like "
             "`N²`. One of those wins eventually, and it is not the numerator."),
            ("The peak is an integer, and it is found by comparing neighbours",
             "You do not need calculus. `C(N + 1) ≤ C(N)` reduces exactly to "
             "`β·N(N + 1) ≥ 1 − α`, an inequality in integers with no root in it. The "
             "smallest `N` that satisfies it is the peak. `√((1 − α)/β)` is the same "
             "answer with a square root left in, and a square root is a decimal that "
             "has to be trusted rather than a count that can be checked."),
        ],
        "read_title": "Three terms, one peak, and the descent on the other side",
        "read_intro": (
            "What each term charges for, the exact test that locates the peak, and why "
            "the closed form is printed beside that test rather than in place of it."
        ),
        "body": [
            ("def", ("The Universal Scalability Law",
                     "For a system of `N` machines, the relative capacity is",
                     "`C(N) = N/(1 + α(N − 1) + βN(N − 1))`,",
                     "measured in multiples of what one machine delivers, where `α ≥ 0` "
                     "is the <strong>contention</strong> coefficient and `β ≥ 0` the "
                     "<strong>coherency</strong> coefficient. `C(1) = 1` by "
                     "construction. This course takes `α` and `β` as given; fitting "
                     "them to measurements is regression and is not covered here.")),
            ("p", "Read the denominator as three charges. The `1` is the work itself. "
                  "`α(N − 1)` is what the other `N − 1` machines cost you in contention "
                  "&mdash; linear, and by itself it produces a plateau at `1/α`. "
                  "`βN(N − 1)` is what every machine costs every other machine in "
                  "keeping their state in agreement, and it is the only term that is "
                  "quadratic."),
            ("example", ("The dashed line, and the solid one",
                         "Take `α = 1/50` and `β = 0`. Then `C(N) = N/(1 + (N − 1)/50)` "
                         "climbs forever toward `1/α = 50×` and never turns down: the "
                         "familiar plateau. Now set `β = 1/10000`. At `N = 10` the new "
                         "term contributes `90/10000 = 0.009` against a denominator of "
                         "about `1.19`, which is nothing. At `N = 200` it contributes "
                         "`3.98` against a denominator of about `8.96`, which is nearly "
                         "half of it. The term that was invisible at ten machines is the "
                         "dominant one at two hundred.")),
            ("h3", "Where the curve turns over"),
            ("p", "Comparing `C(N + 1)` with `C(N)` is a single cross-multiplication, "
                  "and almost everything in it cancels. What survives is a statement "
                  "about `N(N + 1)` that can be tested with integer arithmetic at any "
                  "size."),
            ("thm", ("The turnover test",
                     "For `C(N) = N/(1 + α(N − 1) + βN(N − 1))` with `β > 0`,",
                     "`C(N + 1) ≤ C(N)`  if and only if  `β·N(N + 1) ≥ 1 − α`.",
                     "So the peak `N*` is the smallest positive integer `N` satisfying "
                     "that inequality, and `C` is strictly increasing below it and "
                     "strictly decreasing above it.")),
            ("proof", [
                "Both denominators are positive, so `C(N + 1) ≤ C(N)` is equivalent to "
                "`(N + 1)(1 + α(N − 1) + βN(N − 1)) ≤ N(1 + αN + βN(N + 1))` after "
                "cross-multiplying.",
                "The left side expands to `(N + 1) + α(N² − 1) + βN(N² − 1)` and the "
                "right side to `N + αN² + βN³ + βN²`.",
                "Subtracting the right side from the left leaves "
                "`1 + α(N² − 1) − αN² + βN³ − βN − βN³ − βN²`, which is "
                "`1 − α − βN − βN²`, that is `1 − α − βN(N + 1)`.",
                "So `C(N + 1) ≤ C(N)` exactly when `1 − α − βN(N + 1) ≤ 0`, which is "
                "`β·N(N + 1) ≥ 1 − α`. Since `N(N + 1)` is strictly increasing in `N`, "
                "the inequality fails below one integer and holds from it on, so there "
                "is a single turning point.",
            ]),
            ("p", "That inequality is `N* = √((1 − α)/β)` with the square root taken "
                  "out of it. The two say the same thing; only one of them can be "
                  "checked by multiplying two integers together. This course does the "
                  "check and prints the root beside it, labelled as rounded, which is "
                  "the convention &ldquo;Compound Interest and Continuous Growth&rdquo; "
                  "on the Algebra path uses for the same reason."),
            ("example", ("α = 1/50, β = 1/10000: the peak is 99 machines",
                         "The test is `N(N + 1) ≥ (1 − α)/β = 9800`. At `N = 98`, "
                         "`98 × 99 = 9702`, which is short &mdash; so the ninety-ninth "
                         "machine still helps. At `N = 99`, `99 × 100 = 9900 ≥ 9800` "
                         "&mdash; so the hundredth machine does not. The peak is "
                         "`N* = 99`, exactly, by comparing two products of integers. "
                         "The closed form gives `√9800 = 98.9949`, printed rounded, and "
                         "it agrees.")),
            ("math", [
                "C(99)  = 99/(1 + 98/50 + 99·98/10000)",
                "       = 99/(39302/10000)  =  495000/19651  =  25.1896×",
                "",
                "C(98)  = 10000/397 = 25.1889×        C(100) = 10000/397 = 25.1889×",
                "",
                "so the hundredth machine gives back exactly what the",
                "ninety-ninth bought, and the hundred-and-first gives back more",
            ]),
            ("p", "`C(98)` and `C(100)` being the same exact fraction is not a "
                  "coincidence of rounding &mdash; it is the curve being symmetric about "
                  "its peak in this neighbourhood, and it is the clearest possible "
                  "statement that machine one hundred was not merely unhelpful but "
                  "actively cancelled machine ninety-nine."),
            ("h3", "The descent, in money"),
            ("p", "Past the peak the curve does not level off; it comes down. At "
                  "`N = 198` &mdash; twice the peak, and twice the bill &mdash; capacity "
                  "is `990000/44203 = 22.397×`, which is `88.9%` of what the fleet "
                  "delivered at ninety-nine machines. At `N = 260` it is `20.133×`. "
                  "There exists a fleet size at which you are paying for two hundred and "
                  "sixty machines and getting less than a hundred delivered."),
            ("p", "The dangerous property of this shape is that its symptoms look like "
                  "a capacity shortage. Throughput is below target and latency is up, "
                  "so the fleet is grown, and throughput falls further. The only "
                  "diagnosis that distinguishes it from ordinary saturation is the "
                  "experiment nobody wants to run: remove machines and see whether "
                  "throughput rises."),
            ("p", "`β > 0` is a fact about the protocol, not about the machines. "
                  "Anything that makes every node agree with every other &mdash; a "
                  "distributed lock, a replicated write that waits for all copies, a "
                  "gossip mesh &mdash; puts a quadratic term in that denominator. "
                  "&ldquo;Replication and Consistency&rdquo; is where those protocols "
                  "are priced; this lesson is what their price does to the shape of the "
                  "curve."),
        ],
        "lab": ("scale", {
            "mode": "usl",
            "panel_title": "Set contention and coherency, and watch the curve turn over",
            "panel_intro": (
                "`C(N)` is evaluated as an exact fraction at every integer `N`. The "
                "peak is the smallest `N` with `βN(N + 1) ≥ 1 − α`, which is the closed "
                "form with the square root taken out of it; the root itself is printed "
                "rounded beside it as a check, and the two must name the same machine. "
                "Set `β` to zero and the curve stops turning over &mdash; that is what "
                "the coherency term is."
            ),
        }),
        "steps_title": "Finding the peak of a scalability curve",
        "steps_intro": "Two integer products and a comparison. No differentiation, and no reading a maximum off a plot.",
        "steps": [
            ("Compute the target `(1 − α)/β`",
             "One division, done once. With `α = 1/50` and `β = 1/10000` it is `9800`. "
             "Everything after this is comparing `N(N + 1)` against that one number."),
            ("Find the smallest `N` with `N(N + 1)` at or above it",
             "Scan, or estimate and then check the two neighbours. `98 × 99 = 9702` is "
             "short; `99 × 100 = 9900` clears it; so `N* = 99`. Both products are "
             "integers, so the comparison is exact."),
            ("Evaluate `C(N*)` and the two neighbours",
             "`C(98)`, `C(99)`, `C(100)` as fractions. The middle one must be the "
             "largest, and seeing `C(98) = C(100)` is the strongest evidence that you "
             "have the peak and not a point near it."),
            ("Print `√((1 − α)/β)` beside the integer and label it rounded",
             "`98.9949` here. It is a check on the arithmetic, and it must be presented "
             "as the gloss rather than as the answer: a machine count is a count, and "
             "`98.9949` machines is not one."),
            ("Evaluate well past the peak before you report anything",
             "`C(2N*)` says how much capacity a fleet twice the size delivers &mdash; "
             "`22.397×` against `25.19×` here. Without that row the page shows a curve "
             "that flattens; with it, the reader sees it fall."),
        ],
        "worked": {
            "title": "α = 1/50, β = 1/10000: the peak located by integer comparison",
            "intro": [
                "The whole of the peak-finding is two multiplications and a comparison. "
                "The value at the peak is then one substitution."
            ],
            "lines": [
                "target     (1 − α)/β = (49/50)/(1/10000) = 9800",
                "",
                "N = 98     98 × 99  = 9702  < 9800     machine 99 still helps",
                "N = 99     99 × 100 = 9900  ≥ 9800     machine 100 does not",
                "                                        so  N* = 99",
                "",
                "C(99) = 99 / (1 + (1/50)(98) + (1/10000)(99)(98))",
                "      = 99 / (1 + 1.96 + 0.9702)",
                "      = 99 / (39302/10000)",
                "      = 495000/19651   =  25.1896×",
                "",
                "C(98)  = 490000/19453 = 10000/397 = 25.1889×",
                "C(100) = 500000/19850 = 10000/397 = 25.1889×      equal, exactly",
                "",
                "closed form   √((1 − α)/β) = √9800 = 98.9949   (rounded)",
                "",
                "C(198) = 990000/44203 = 22.397×      88.9% of the peak, twice the bill",
                "β = 0  instead:  C(N) → 1/α = 50×    and never comes down",
            ],
            "after": [
                "`C(98) = C(100)` exactly is the line that settles it. If the peak were "
                "somewhere else, those two would differ; they are equal because `99` "
                "sits between them, and the hundredth machine returned precisely what "
                "the ninety-ninth added.",
                "The last two lines are the lesson. Twice the peak fleet delivers "
                "`88.9%` of the peak&rsquo;s throughput &mdash; and with the coherency "
                "term switched off the same contention `α` would have given a plateau "
                "at `50×`, which is the curve a reader arriving from Amdahl expects to "
                "see.",
                "For a faded attempt, keep `α = 1/50` and set `β = 1/2500`. Compute the "
                "target, find `N*` by testing the two neighbouring products, evaluate "
                "`C(N*)`, and predict before you compute it whether the peak throughput "
                "is higher or lower than `25.19×`. Then check all four against the lab.",
            ],
        },
        "quiz_title": "Peaks, plateaus and the difference",
        "quiz": [
            {"q": "With `α = 0.02` and `β = 0.0001`, at which machine count is throughput highest?",
             "a": ["`50`", "`98.9949`", "`99`", "`100`"],
             "c": 2,
             "why": "`N(N + 1) ≥ (1 − α)/β = 9800` first holds at `N = 99`, since "
                    "`98 × 99 = 9702` and `99 × 100 = 9900`. `50` is `1/α`, the "
                    "<em>throughput</em> ceiling the curve would have if `β` were zero "
                    "&mdash; a multiple, not a machine count. `98.9949` is the closed "
                    "form rounded, and there is no such fleet. `100` is past the peak: "
                    "`C(100) = 10000/397`, which is exactly `C(98)` and below `C(99)`."},
            {"q": "What does the coherency term `βN(N − 1)` do that a serial fraction cannot?",
             "a": ["It lowers the plateau the curve settles at",
                   "It makes the curve fall past a peak, so more machines deliver less",
                   "It delays the plateau until a larger machine count",
                   "It makes the first few machines less effective"],
             "c": 1,
             "why": "Amdahl&rsquo;s serial fraction, and the contention term `α` on its "
                    "own, produce a curve that rises to a bound and stays there &mdash; "
                    "a plateau at `1/α = 50×` here. Because `βN(N − 1)` is quadratic "
                    "while the numerator is linear, it eventually dominates and the "
                    "curve turns down: `C(198) = 22.397×` against a peak of `25.19×`. "
                    "The first and third options describe a plateau moving; the fourth "
                    "is false, since at `N = 10` the coherency term contributes `0.009` "
                    "of a denominator near `1.19`."},
            {"q": "Why does the page print the integer `99` and the value `98.9949` side by side rather than just rounding the root?",
             "a": ["Because `√9800` is irrational, so only the integer test is exact and the root is a check on it",
                   "Because the root is wrong and the scan is right",
                   "Because rounding a root always gives the neighbour below the true peak",
                   "Because the curve is flat between 98 and 100, so either answer will do"],
             "c": 0,
             "why": "`√9800` cannot be written exactly as a fraction, so a rounded "
                    "decimal is the best it offers; `βN(N + 1) ≥ 1 − α` compares two "
                    "integers and is exact at any size. The root is not wrong &mdash; it "
                    "agrees. Rounding it has no guaranteed direction, which is exactly "
                    "why it is checked rather than trusted. And the curve is not flat "
                    "there: `C(99) > C(98) = C(100)`, which is how the peak was found."},
            {"q": "A fleet at 198 machines is delivering less throughput than the team expected. Which observation would distinguish this curve from ordinary saturation?",
             "a": ["Latency rises when load rises",
                   "Throughput rises when machines are removed",
                   "Throughput stops rising when machines are added",
                   "Utilisation on every machine is below 100%"],
             "c": 1,
             "why": "Only a falling curve predicts that taking machines away increases "
                    "throughput, and at `N = 198` the model says removing ninety-nine "
                    "of them takes capacity from `22.397×` to `25.19×`. Rising latency "
                    "under load happens in every queueing system. Throughput that "
                    "merely stops rising is a plateau, which is Amdahl&rsquo;s shape "
                    "and not this one. Spare utilisation is consistent with both."},
        ],
        "mistakes": [
            ("Expecting a plateau and reading the peak as one",
             "A reader who has only met Amdahl sees a curve that flattens and concludes "
             "that further machines are merely wasted. Here they are harmful: `C(198)` "
             "is below `C(99)`, so the second hundred machines took capacity away and "
             "were paid for. The plateau is the `β = 0` curve, and it is drawn dashed on "
             "the same axes so the two shapes can be told apart."),
            ("Rounding the closed form and calling it the answer",
             "`√((1 − α)/β) = 98.9949` rounds to `99`, which happens to be right here "
             "and is not guaranteed anywhere. The claim the page makes is "
             "`β·N(N + 1) ≥ 1 − α` tested at integers, which is two multiplications and "
             "a comparison and can be redone by hand. The root is printed as a gloss "
             "and labelled as rounded."),
            ("Treating `β` as a property of the hardware",
             "`β` is a property of the protocol: what has to agree with what, and how "
             "often. Faster machines and a faster network change how long each exchange "
             "takes, not how many exchanges the design requires, so they move the curve "
             "up without moving the peak much. Removing the need for agreement is what "
             "moves the peak."),
        ],
        "standard": ("Finish when you can locate a peak by comparing two integer products, and say what is on the far side of it.",
                     "You should be able to compute `(1 − α)/β`, find `N*` by testing "
                     "`N(N + 1)` at two neighbouring integers, evaluate `C(N*)` and its "
                     "neighbours as exact fractions, and state what `C(2N*)` is &mdash; "
                     "in multiples of one machine and as a share of the peak."),
        "note": "Both scaling laws so far answer &ldquo;what does another machine "
                "buy?&rdquo; in throughput. The rest of this course asks what it costs, "
                "and the first two questions are about shape rather than size: how big "
                "a batch should be, and whether capacity is better bought as many small "
                "machines or one large one. &ldquo;Vertical vs Horizontal&rdquo; uses "
                "this same contention term with `β` set to zero, so the two pages cannot "
                "disagree about what a fleet delivers.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "batching-cost-and-latency",
        "title": "Batching: Cost and Latency",
        "module": "What a shape costs",
        "one_line": "Choose a batch size from where the per-item cost curve flattens, and report the wait that size costs.",
        "summary": (
            "A batch spreads one fixed charge over `B` items, so the per-item cost "
            "`F/B + v` falls like a hyperbola onto a floor at `v`. Filling the batch "
            "makes items wait, and that wait rises linearly with `B`. Two curves in "
            "opposite directions, and no `B` that is best at both."
        ),
        "key": [
            "per item   F/B + v        F = 2 000 µ$ a call, v = 100 µ$ an item",
            "B = 1 → 2 100 µ$          B = 100 → 120 µ$        floor v = 100 µ$",
            "first item waits  (B − 1)/λ = 198 ms    λ = 500 items/s",
            "mean wait         (B − 1)/(2λ) = 99 ms",
            "rule of thumb     B/λ = 200 ms          over by 1/λ = 2 ms, at every B",
        ],
        "key_label": "One curve down onto a floor, one line up",
        "concepts_intro": (
            "The cost curve is the interesting one, because the shape of a hyperbola is "
            "what makes &ldquo;bigger is better&rdquo; stop being true long before the "
            "cost stops falling."
        ),
        "concepts": [
            ("The fixed charge is what batching buys back",
             "`F` is paid once per batch whatever is in it: a request, a round trip, an "
             "`fsync`, a commit. Spread over `B` items it is `F/B` each, so the first "
             "few doublings of `B` are enormous &mdash; `2 100 µ$` at `B = 1` becomes "
             "`1 100` at two and `300` at ten. `v` is paid per item and batching does "
             "not touch it at all."),
            ("The curve lands on a floor, and the floor is `v`",
             "`F/B + v` is a hyperbola sitting on `v = 100 µ$`. At `B = 100` the item "
             "costs `120 µ$`, so the entire remaining saving available at any batch "
             "size whatever is the `20 µ$` still in the `F/B` term. Going to `B = 800` "
             "recovers `17.5` of that `20` and costs just over eight times the wait. The curve "
             "flattening is not a feature of this example; it is what a hyperbola does."),
            ("The wait is linear, and it is not `B/λ`",
             "Items arrive at `λ` a second, so the first item in a batch waits for the "
             "other `B − 1` to arrive: `(B − 1)/λ`, which is `198 ms` at `B = 100` and "
             "`λ = 500`. Averaged over the batch it is half that, `99 ms`. The familiar "
             "`B/λ` is the rule of thumb and it overstates the first item&rsquo;s wait "
             "by exactly one inter-arrival time, `1/λ = 2 ms`, at every `B`."),
        ],
        "read_title": "Two curves, their shapes, and where a batch size comes from",
        "read_intro": (
            "What each curve does, the two exact waits against the rule of thumb, and "
            "where the exact optimum lives when you are prepared to price the latency."
        ),
        "body": [
            ("def", ("Batched per-item cost",
                     "Let `F` be the cost charged once per batch and `v` the cost "
                     "charged per item. For a batch of `B` items the "
                     "<strong>per-item cost</strong> is",
                     "`F/B + v`,",
                     "which is strictly decreasing in `B`, is bounded below by `v`, and "
                     "reaches `v` only in the limit.")),
            ("p", "The two facts worth carrying are that it always falls and that it "
                  "never reaches the floor. Together they mean there is no batch size "
                  "at which the cost stops improving, and therefore no batch size that "
                  "a cost argument alone will ever choose. Something else has to stop "
                  "you, and that something is the wait."),
            ("math", [
                "F = 2 000 µ$,  v = 100 µ$,  λ = 500 items/s",
                "",
                "  B      F/B + v      fixed share     mean wait     first item",
                "  1      2 100 µ$       95.2%            0 ms          0 ms",
                "  2      1 100 µ$       90.9%            1 ms          2 ms",
                " 10        300 µ$       66.7%            9 ms         18 ms",
                "100        120 µ$       16.7%           99 ms        198 ms",
                "800      102.5 µ$        2.4%          799 ms        1.6 s",
            ]),
            ("p", "Read the last two rows against each other. Going from `B = 100` to "
                  "`B = 800` saves `17.5 µ$` an item &mdash; a further `14.6%` &mdash; "
                  "and multiplies the wait by eight. Going from `B = 1` to `B = 100` "
                  "saved `1 980 µ$` an item, a factor of `17.5`, for `99 ms`. Same "
                  "curve, and the two ends of it are not remotely the same trade."),
            ("def", ("Fill wait",
                     "With Poisson-free, evenly spaced arrivals at rate `λ` and a batch "
                     "that closes when it is full, the `k`-th item to arrive waits "
                     "`(B − k)/λ` for the batch to fill. The first waits `(B − 1)/λ`, "
                     "the last waits nothing, and the mean over the batch is "
                     "`(B − 1)/(2λ)`.")),
            ("p", "`B/λ` is what gets quoted, and it is the time to <em>collect</em> `B` "
                  "items rather than the time any item spends waiting. The difference is "
                  "one inter-arrival time and it does not shrink as `B` grows: at "
                  "`λ = 500` it is `2 ms` at every batch size. At `B = 100` that is "
                  "`200 ms` quoted against `198 ms` actual, which is a one per cent "
                  "error; at `B = 2` it is `2 ms` quoted against `2 ms` actual for the "
                  "first item and `1 ms` on average, which is not."),
            ("h3", "A flush timer is the other half of the design"),
            ("p", "A batch that closes only when full stalls forever if arrivals stop, "
                  "so real systems close on whichever comes first: `B` items, or a timer "
                  "of `T`. The timer bounds the wait no matter what the traffic does; "
                  "the size bounds it when traffic is heavy. At `λ = 500`, `B = 100` and "
                  "a `200 ms` timer the size wins, which is why the wait in the table is "
                  "the fill wait rather than the timer."),
            ("h3", "Where the batch size actually comes from"),
            ("p", "&ldquo;Choose `B` where the curve flattens&rdquo; is a judgement, "
                  "and the lab makes it a reproducible one by naming the threshold: it "
                  "picks the smallest `B` at which the fixed share `F/B` has fallen to a "
                  "stated fraction of `v`. At twenty per cent of `v = 100 µ$` that is "
                  "`F/B ≤ 20`, so `B = 100`. Stating the threshold is what turns a "
                  "judgement into something a second person can check."),
            ("p", "It is still a judgement, and there is an exact answer available once "
                  "you are willing to price the latency rather than merely observe it. "
                  "Give waiting a cost per item-second and the total becomes fixed cost "
                  "per item plus holding cost per item, which is the economic order "
                  "quantity &mdash; minimised in closed form, with no calculus, in "
                  "&ldquo;The EOQ Formula Without Calculus&rdquo; in the Operations "
                  "Research course &ldquo;Inventory Models&rdquo;. Latency plays the "
                  "holding cost&rsquo;s part exactly."),
            ("example", ("The same bargain, one layer down",
                         "A storage engine that calls `fsync` once per commit pays a "
                         "fixed charge per call and amortises it across whatever "
                         "transactions are waiting; the transactions wait for the group "
                         "to form. That is `F/B + v` against `(B − 1)/(2λ)` with "
                         "different units, and it is priced in &ldquo;fsync and Group "
                         "Commit&rdquo; on &ldquo;Storage Engines and Indexes&rdquo;. "
                         "Recognising the shape is most of the value of this lesson: it "
                         "recurs at every layer that has a per-operation charge.")),
            ("p", "One warning about the floor. If `v` is large relative to `F`, "
                  "batching is nearly pointless however large `B` gets: the curve starts "
                  "close to its floor and has nowhere to fall. The quantity that decides "
                  "whether batching is worth designing for is `F/v`, and it should be "
                  "computed before the batch size is argued about."),
        ],
        "lab": ("scale", {
            "mode": "batch",
            "panel_title": "Set the costs, the arrival rate and the batch",
            "panel_intro": (
                "`F/B + v` and the two exact waits &mdash; `(B − 1)/λ` for the first "
                "item and half that on average &mdash; are fractions of the numbers you "
                "set. `B/λ` is printed beside them as the rule of thumb, overstating "
                "the first item&rsquo;s wait by exactly one inter-arrival time at every "
                "batch size. Drag the batch past the flat part and watch the cost stop "
                "moving while the wait does not."
            ),
        }),
        "steps_title": "Choosing a batch size you can defend",
        "steps_intro": "Compute the ratio that decides whether batching helps at all, then pick the size against a stated threshold.",
        "steps": [
            ("Compute `F/v` before anything else",
             "It is the whole size of the prize. At `F = 2 000 µ$` and `v = 100 µ$` it "
             "is `20`, so batching can take an item from `21v` to `v` &mdash; a factor "
             "of twenty-one is available. If `F/v` is a half, close the question and go "
             "and find a different cost."),
            ("Tabulate `F/B + v` at powers of two, not at a single `B`",
             "The shape is the point, and one row cannot show it. Four or five rows make "
             "it obvious where the curve stops paying, and keeping `F/B` as its own "
             "column shows exactly how much saving is still on the table."),
            ("State the threshold that stops you",
             "&ldquo;The fixed share is down to a fifth of `v`&rdquo; gives `B = 100` "
             "here, reproducibly. Any rule will do as long as it is written down; what "
             "does not work is stopping where the curve looks flat, because that is a "
             "property of the axis scale."),
            ("Compute both waits at the chosen `B`, and the rule of thumb beside them",
             "`(B − 1)/λ` and `(B − 1)/(2λ)`. Report the first-item figure &mdash; "
             "`198 ms` here &mdash; because it is the one a percentile sees, and note "
             "that `B/λ` would have said `200 ms`."),
            ("Add a timer and say which bound is binding",
             "If the timer fires before the batch fills, the wait is the timer and the "
             "per-item cost is worse than the table says, because the batch closed "
             "short. At `λ = 500`, `B = 100` and a `200 ms` timer, the size binds and "
             "the timer is insurance."),
        ],
        "worked": {
            "title": "F = 2 000 µ$, v = 100 µ$, λ = 500/s: choosing B = 100",
            "intro": [
                "The threshold used here is that the fixed share falls to a fifth of the "
                "variable cost. It is stated first so that the batch size is a "
                "consequence rather than a preference."
            ],
            "lines": [
                "prize        F/v = 2 000/100 = 20        item can fall from 21v to v",
                "",
                "threshold    F/B ≤ v/5 = 20 µ$",
                "             2 000/B ≤ 20   ⟹   B ≥ 100      so  B = 100",
                "",
                "per item     F/B + v = 20 + 100 = 120 µ$",
                "against B=1  2 100/120 = 17.5× cheaper",
                "fixed share  20/120 = 16.7%",
                "still on the table   F/B = 20 µ$ , ever, at any B",
                "",
                "wait, first item    (B − 1)/λ = 99/500 s = 198 ms",
                "wait, mean          (B − 1)/(2λ) = 99/1000 s = 99 ms",
                "rule of thumb       B/λ = 100/500 s = 200 ms      over by 1/λ = 2 ms",
                "",
                "and if B = 800 instead:",
                "  per item   2 000/800 + 100 = 102.5 µ$     a further 14.6% saved",
                "  first item 799/500 s = 1.6 s            8.1× the wait",
            ],
            "after": [
                "The `still on the table` line is the one that settles the batch size. "
                "Whatever `B` you choose above one hundred, the most it can save is "
                "`20 µ$` an item, because that is all of `F/B` that is left. The wait, "
                "by contrast, has no ceiling at all &mdash; it is linear in `B` "
                "forever.",
                "The last block prices the temptation. `B = 800` is genuinely cheaper, "
                "by `17.5 µ$` an item, and it makes the first item in every batch wait "
                "`1.6 s`. Whether that is a good trade is a question about the service, "
                "and it is answerable only because both numbers are on the page.",
                "For a faded attempt, set `F = 500 µ$`, `v = 250 µ$` and `λ = 200/s`. "
                "Compute `F/v` and predict from it alone whether batching is worth much "
                "here. Then apply the same threshold, compute the per-item cost and "
                "both waits at the `B` it gives, and check against the lab.",
            ],
        },
        "quiz_title": "Batch sizes, costs and waits",
        "quiz": [
            {"q": "With `F = 2 000 µ$` and `v = 100 µ$`, the per-item cost at `B = 100` is `120 µ$`. What is the most any larger batch could save per item?",
             "a": ["`120 µ$`, since the cost keeps falling", "`100 µ$`", "`20 µ$`", "`102.5 µ$`"],
             "c": 2,
             "why": "What is left to save is the whole of `F/B = 20 µ$`, because the "
                    "curve is falling onto a floor at `v = 100 µ$` that batching cannot "
                    "touch. `120 µ$` would mean the item becomes free. `100 µ$` is the "
                    "floor itself &mdash; the part you keep paying. `102.5 µ$` is the "
                    "per-item cost at `B = 800`, which is a cost and not a saving."},
            {"q": "At `B = 100` and `λ = 500` items a second, how long does the first item in a batch wait for the batch to fill?",
             "a": ["`99 ms`", "`198 ms`", "`200 ms`", "`2 ms`"],
             "c": 1,
             "why": "It waits for the other `B − 1 = 99` items, which is `99/500 s = "
                    "198 ms`. `99 ms` is `(B − 1)/(2λ)`, the mean across the batch "
                    "rather than the worst case. `200 ms` is the rule of thumb `B/λ`, "
                    "which counts one arrival too many. `2 ms` is the single "
                    "inter-arrival time `1/λ` &mdash; the gap between the rule of thumb "
                    "and the exact answer."},
            {"q": "A service has `F = 50 µ$` per call and `v = 500 µ$` per item. What should be decided about batching?",
             "a": ["Batch as large as latency permits; the saving is the same shape as any other",
                   "There is little to win: `F/v = 0.1`, so the per-item cost can fall by at most a tenth",
                   "Batching will increase the per-item cost, because `F` is paid per batch",
                   "Nothing can be said until `λ` is known"],
             "c": 1,
             "why": "The per-item cost runs from `550 µ$` at `B = 1` down to a floor of "
                    "`500 µ$`, so the whole prize is ten per cent and it is mostly "
                    "collected by `B = 10`. Batching never raises the per-item cost "
                    "&mdash; `F/B + v` is decreasing in `B`. And `λ` sets the wait, not "
                    "the saving: the cost curve does not contain `λ` at all."},
            {"q": "Why does the lab print `B/λ` beside `(B − 1)/λ` instead of just using the exact figure?",
             "a": ["Because `B/λ` is the wait when a flush timer fires first",
                   "Because `B/λ` is what is usually quoted, and showing both makes the size of the error visible",
                   "Because `(B − 1)/λ` is only valid for large `B`",
                   "Because the two differ by a factor that grows with `B`"],
             "c": 1,
             "why": "The rule of thumb is in wide use and it is wrong by exactly one "
                    "inter-arrival time at every batch size, so printing both shows "
                    "`200 ms` against `198 ms` and names the `2 ms` gap. The timer is a "
                    "separate bound with its own value. `(B − 1)/λ` is exact at every "
                    "`B`, small ones included. And the gap is `1/λ` &mdash; constant, "
                    "which is why it matters at small `B` and disappears into the noise "
                    "at large `B`."},
        ],
        "mistakes": [
            ("Reading “the cost keeps falling” as “bigger is better”",
             "It does keep falling, and that is exactly why the cost curve cannot choose "
             "a batch size. Past `B = 100` the entire remaining prize is `20 µ$` an "
             "item while the wait goes on growing without bound. The decision needs the "
             "second curve, and quoting only the first is how a `1.6 s` fill wait gets "
             "shipped to save fifteen per cent of a cost that was already small."),
            ("Quoting `B/λ` as the added latency",
             "`B/λ` is the time to collect `B` items; the first item in the batch waits "
             "`(B − 1)/λ` and the average item waits half that. At `B = 100` and "
             "`λ = 500` the three figures are `200 ms`, `198 ms` and `99 ms`, and they "
             "answer three different questions. The one a percentile sees is `198 ms`."),
            ("Forgetting that the timer changes both curves",
             "A batch closed early by a timer holds fewer than `B` items, so its "
             "per-item cost is higher than the table promised and its wait is the timer "
             "rather than the fill time. Under light traffic every batch is a timer "
             "batch, which means the cost measured in production can be far above the "
             "cost the batch size was chosen for."),
        ],
        "standard": ("Finish when a batch size comes with a stated threshold and two waits attached to it.",
                     "You should be able to compute `F/v` and say how much batching can "
                     "possibly buy, tabulate `F/B + v` across several `B`, name the "
                     "threshold you stopped at, and report the first-item and mean fill "
                     "waits alongside the rule of thumb they differ from."),
        "note": "This lesson chose a shape for one operation. The next chooses a shape "
                "for the machines themselves: the same capacity bought as many small "
                "nodes or as one large one. The two costs are easy; what makes it a real "
                "question is that coordination means `N` nodes do not deliver `N` "
                "nodes&rsquo; worth &mdash; the contention term of &ldquo;The Universal "
                "Scalability Law&rdquo;, reappearing as a line on a price comparison.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "vertical-vs-horizontal",
        "title": "Vertical vs Horizontal",
        "module": "What a shape costs",
        "one_line": "Cost a target capacity as many small nodes and as one large machine, and locate every capacity at which the cheaper side changes.",
        "summary": (
            "Buying `N` small nodes costs `N` times a node and delivers less than `N` "
            "nodes&rsquo; worth, because they coordinate. Buying one large machine "
            "costs a premium that grows faster than the size does, and you can only buy "
            "the rungs that exist. Neither is always cheaper, and the crossing is found "
            "by evaluating both."
        ),
        "key": [
            "horizontal   N nodes deliver N/(1 + α(N − 1)) nodes’ worth   α = 1/200",
            "5× a node needs 6 nodes, not 5                    $600.00 a month",
            "vertical     each doubling of size multiplies price by 2.2",
            "rung 3 = 8× a node = $1 064.80                    you round up to a rung",
            "crossings    horizontal first wins at 3× and loses again at 4×",
            "             from 5× on it never loses again      fleet ceiling 1/α = 200×",
        ],
        "key_label": "A straight line against a staircase, and two crossings",
        "concepts_intro": (
            "Three things make this harder than dividing one price by another: "
            "coordination, the rung, and the fact that a staircase can cross a line "
            "more than once."
        ),
        "concepts": [
            ("`N` nodes deliver less than `N` nodes",
             "The same contention term as &ldquo;The Universal Scalability Law&rdquo;, "
             "with `β = 0`: `N` nodes deliver `N/(1 + α(N − 1))` nodes&rsquo; worth. At "
             "`α = 1/200`, reaching five times a node takes six nodes, not five, and "
             "reaching sixty-four times takes ninety-four. The penalty is invisible at "
             "small `N` and enormous at large `N`, and it also caps the fleet at "
             "`1/α = 200×` however many nodes are bought."),
            ("Vertical is a staircase, and you round up to a rung",
             "Machine sizes come in discrete steps, so a target of five times a node is "
             "served by the eight-times rung with three times a node left idle. That "
             "rounding is a real cost and it is why the vertical curve is a step "
             "function rather than a smooth one. Half a machine size is not for sale."),
            ("The premium is superlinear, so the staircase pulls away",
             "Here each doubling of size multiplies the price by `2.2` rather than by "
             "`2`, so eight times a node costs `$1 064.80` where eight nodes would cost "
             "`$800`, and sixty-four times costs `$11 337.99` against `$9 400` for the "
             "nodes that deliver it. The gap widens with every rung, which is why large "
             "systems end up horizontal in the end."),
        ],
        "read_title": "Two price curves, the coordination penalty, and the crossings",
        "read_intro": (
            "How each side is costed, why there are two crossings rather than one, and "
            "the thing the price comparison leaves out entirely."
        ),
        "body": [
            ("def", ("The two plans",
                     "To reach a target capacity `T`, measured in multiples of one small "
                     "node:",
                     "<strong>horizontal</strong> &mdash; buy the smallest `N` with "
                     "`N/(1 + α(N − 1)) ≥ T`, at `N · u` where `u` is the price of a "
                     "node;",
                     "<strong>vertical</strong> &mdash; buy the smallest rung of the "
                     "size ladder that is at least `T`, at the ladder&rsquo;s price for "
                     "that rung.",
                     "Both are exact given `α`, `u` and the ladder. Neither is an "
                     "approximation of the other.")),
            ("p", "The horizontal side is a straight line in the number of nodes and a "
                  "curve in the capacity delivered, because of the coordination term. "
                  "The vertical side is a staircase in both. Comparing a line to a "
                  "staircase is what produces more than one crossing."),
            ("math", [
                "α = 1/200,  node $100.00,  ladder: ×2 size costs ×2.2 price",
                "",
                " target    nodes (ideal)   horizontal      rung       vertical    cheaper",
                "   1×         1  (1)         $100.00       2⁰ = 1×     $100.00    vertical",
                "   2×         3  (2)         $300.00       2¹ = 2×     $220.00    vertical",
                "   3×         4  (3)         $400.00       2² = 4×     $484.00    horizontal",
                "   4×         5  (4)         $500.00       2² = 4×     $484.00    vertical",
                "   5×         6  (5)         $600.00       2³ = 8×   $1 064.80    horizontal",
                "  16×        18 (16)       $1 800.00       2⁴ = 16×  $2 342.56    horizontal",
                "  64×        94 (64)       $9 400.00       2⁶ = 64× $11 337.99    horizontal",
            ]),
            ("h3", "Why six nodes for five nodes’ worth"),
            ("p", "Solve the delivered-capacity condition rather than dividing. With "
                  "`α = 1/200`, `N` nodes deliver `200N/(199 + N)` nodes&rsquo; worth, "
                  "so reaching `5×` needs `200N ≥ 995 + 5N`, that is `N ≥ 995/195 = "
                  "5.10…`, so `N = 6`. Five nodes deliver `4.90…`, which is short. The "
                  "sixth node is bought entirely to pay for the coordination of the "
                  "first five."),
            ("example", ("The penalty at scale",
                         "The same inequality at `T = 64` gives `N ≥ 12 736/136 = "
                         "93.6…`, so ninety-four nodes. Thirty of them exist only to "
                         "carry the overhead the other sixty-four create. And the "
                         "ceiling is absolute: `200N/(199 + N)` rises to `200` and no "
                         "further, so a target of `250×` cannot be met horizontally at "
                         "this `α` by any number of nodes at all.")),
            ("h3", "Two crossings, because a staircase is not a line"),
            ("p", "Horizontal first becomes cheaper at `3×`, where four nodes at `$400` "
                  "beat the four-times rung at `$484`. At `4×` it loses again: the same "
                  "rung now serves the larger target at the same `$484`, while "
                  "horizontal has had to buy a fifth node. From `5×` on it never loses "
                  "again."),
            ("p", "The reason is the rung. A size you have just bought is cheap per unit "
                  "of capacity until it is full, and it gets cheaper per unit as the "
                  "target rises toward the top of it. Every rung repeats that pattern, "
                  "so the vertical curve is a sawtooth against the horizontal line and "
                  "the comparison can flip back. Reporting a single break-even hides "
                  "this; the honest report is two numbers &mdash; where horizontal first "
                  "wins, and where it stops losing."),
            ("example", ("Buying at the wrong end of a rung",
                         "At a target of `5×` the vertical plan buys the eight-times "
                         "rung for `$1 064.80` and leaves three nodes&rsquo; worth idle: "
                         "`$600` of horizontal capacity would have done. At a target of "
                         "`8×` the same rung costs the same `$1 064.80` and is full, while "
                         "horizontal now needs nine nodes at `$900`. The rung is at its "
                         "worst the moment after you are forced onto it and at its best "
                         "the moment before you outgrow it.")),
            ("h3", "What the prices do not say"),
            ("p", "One machine is one failure domain. The horizontal plan has a parallel "
                  "path through it and the vertical plan does not, and that difference "
                  "is a probability rather than a price &mdash; it is computed in "
                  "&ldquo;Parallel: Redundancy&rdquo; on &ldquo;Availability and "
                  "Failure&rdquo;, where two independent components at `99.9%` compose "
                  "to `99.9999%` and one component at `99.9%` composes to `99.9%`. This "
                  "page does not repeat that arithmetic; it names the gap, because a "
                  "cost comparison that omits it will pick the single box every time it "
                  "is close."),
            ("p", "There is a second omission worth stating. The vertical plan has no "
                  "coordination term because there is nothing to coordinate, which is "
                  "genuinely an advantage: the single box delivers its nameplate. The "
                  "comparison above already credits it with that &mdash; the rung is "
                  "compared against delivered capacity, not against node count &mdash; "
                  "and it is still the more expensive side from `5×` on."),
        ],
        "lab": ("scale", {
            "mode": "vertical",
            "panel_title": "Price a target capacity both ways",
            "panel_intro": (
                "The node count comes from the same contention term &ldquo;The "
                "Universal Scalability Law&rdquo; draws, with `β` set to zero, so the "
                "two pages cannot disagree about what a fleet delivers. Both prices are "
                "exact, and the crossing is reported twice &mdash; the first target "
                "horizontal wins at, and the target past which it never loses again. "
                "Move the ladder&rsquo;s multiplier toward `2.0` and watch both "
                "crossings move. Money at or above a thousand dollars is shown to the "
                "nearest dollar, so the eight-times rung&rsquo;s exact `$1 064.80` "
                "appears there as `$1 065`."
            ),
        }),
        "steps_title": "Costing a target capacity both ways",
        "steps_intro": "Delivered capacity first on both sides, so that the two prices are for the same thing.",
        "steps": [
            ("Convert the target into delivered capacity, not nameplate",
             "Horizontal: solve `N/(1 + α(N − 1)) ≥ T` for the smallest integer `N`. "
             "Vertical: take the smallest rung at or above `T`. Doing this first is "
             "what stops the comparison being between six nodes and five nodes&rsquo; "
             "worth of box."),
            ("Price each side at that size",
             "`N · u` on one side, the ladder&rsquo;s entry on the other. Keep the idle "
             "capacity visible on the vertical side: `$1 064.80` for a target of `5×` is "
             "buying `8×`, and the reader should be able to see that."),
            ("Evaluate across a range of targets, not at your target alone",
             "One target gives one verdict and no idea how stable it is. A column of "
             "targets shows the staircase and shows the verdict flipping, which is the "
             "thing that a single row cannot tell you."),
            ("Report both crossings",
             "The first target at which horizontal wins, and the target past which it "
             "never loses again. Here those are `3×` and `5×`, and the gap between them "
             "is precisely the price of being forced onto the next rung."),
            ("Name the failure domain before you conclude",
             "The single box has no parallel path. That is not in either price, it is a "
             "separate calculation, and it belongs in the recommendation rather than in "
             "a footnote to it."),
        ],
        "worked": {
            "title": "A target of 5× a node: $600 of nodes against a $1 064.80 rung",
            "intro": [
                "The node count is solved as an inequality rather than divided out, "
                "which is where the sixth node comes from."
            ],
            "lines": [
                "α = 1/200      node price u = $100.00 a month",
                "ladder         2× the size costs 2.2× the price, from $100.00",
                "",
                "horizontal, delivered capacity of N nodes:",
                "    N/(1 + (N − 1)/200)  =  200N/(199 + N)",
                "  want ≥ 5:   200N ≥ 995 + 5N   ⟹   195N ≥ 995   ⟹   N ≥ 5.102…",
                "                                                so  N = 6",
                "  check  N = 5:  1000/204 = 4.90…×   short",
                "         N = 6:  1200/205 = 5.85…×   clears it",
                "  cost   6 × $100.00 = $600.00",
                "",
                "vertical, rungs:   1× $100.00   2× $220.00   4× $484.00   8× $1 064.80",
                "  smallest rung ≥ 5× is 8×      cost $1 064.80",
                "  idle                          3× a node, paid for",
                "",
                "verdict at 5×      horizontal, by $464.80 a month",
                "",
                "and at 4×:   5 nodes = $500.00   against the same 4× rung at $484.00",
                "             vertical wins — the second crossing",
            ],
            "after": [
                "The `N ≥ 5.102…` line is where the coordination penalty becomes a "
                "purchase. It is a fraction of a node that cannot be bought, so it "
                "becomes a whole node, and at this target that single rounding is a "
                "sixth of the horizontal bill.",
                "The last block is the part that a single-crossing answer would have "
                "hidden. At `4×` the vertical plan is cheaper and at `5×` it is not, "
                "because the four-times rung serves `4×` exactly and cannot serve `5×` "
                "at all. That is why the lab reports where horizontal first wins and "
                "where it stops losing, rather than one break-even.",
                "For a faded attempt, change the ladder so a doubling costs `1.6×` "
                "rather than `2.2×`, keeping `α` and the node price. Predict before "
                "computing whether the two crossings move up or down, then find them "
                "both in the lab and say which targets changed verdict.",
            ],
        },
        "quiz_title": "Nodes, rungs and crossings",
        "quiz": [
            {"q": "At `α = 1/200`, how many nodes are needed to deliver five times what one node delivers?",
             "a": ["`5`", "`6`", "`10`", "`5.102…`, and you buy what you need of the sixth"],
             "c": 1,
             "why": "`200N/(199 + N) ≥ 5` gives `N ≥ 995/195 = 5.102…`, and machines "
                    "are integers, so `N = 6`. Five nodes deliver `1000/204 = 4.90…×`, "
                    "which is short of the target. `10` would be the answer if the "
                    "penalty were fifty per cent rather than the half of one per cent "
                    "`α` actually specifies. And a fifth of a node is not a purchase; "
                    "rounding up is part of the answer, not a detail of it."},
            {"q": "Horizontal first becomes cheaper at a target of `3×`, and at `4×` vertical is cheaper again. What causes the second crossing?",
             "a": ["The coordination penalty grows faster than the node count",
                   "The four-times rung serves the larger target at the same price, while horizontal has had to buy another node",
                   "The ladder&rsquo;s price multiplier changes between rungs",
                   "Rounding in the price of a node"],
             "c": 1,
             "why": "The `4×` rung costs `$484` at a target of `3×` and the same `$484` "
                    "at `4×`, because it is one product; horizontal has gone from four "
                    "nodes at `$400` to five at `$500`. A rung gets cheaper per unit of "
                    "capacity as the target rises toward the top of it, which is why a "
                    "staircase crosses a line more than once. The coordination penalty "
                    "is smooth and makes horizontal steadily worse, not better; the "
                    "multiplier is a constant `2.2` at every rung; and nothing here "
                    "turns on rounding a price."},
            {"q": "At `α = 1/200`, what is the largest capacity a horizontal fleet can deliver, however many nodes are bought?",
             "a": ["`200×` one node", "`400×` one node", "There is no limit; `N/(1 + α(N − 1))` grows without bound", "`94×` one node"],
             "c": 0,
             "why": "`N/(1 + α(N − 1)) = 200N/(199 + N) → 200` as `N` grows, so `1/α` is "
                    "an asymptote the fleet never reaches &mdash; the same shape as "
                    "Amdahl&rsquo;s ceiling, with contention in the serial "
                    "fraction&rsquo;s role. `400×` is `2/α` and corresponds to nothing. "
                    "The expression is bounded, so it does not grow without bound. And "
                    "`94` is the node count that delivers `64×`, which is a point on the "
                    "curve rather than its limit."},
            {"q": "Two plans cost within a few per cent of each other at the target capacity. What has the price comparison left out?",
             "a": ["Nothing; the cheaper plan wins",
                   "That the single box is one failure domain with no parallel path through it",
                   "That the ladder price will fall next year",
                   "That the coordination penalty was already counted twice"],
             "c": 1,
             "why": "Availability is a separate calculation and it is not in either "
                    "price: redundancy multiplies availability up only when there is a "
                    "second path, and the vertical plan has none. Vendor price movements "
                    "are out of scope here &mdash; prices are inputs. And the penalty is "
                    "counted exactly once, on the horizontal side, which is why that "
                    "side needs six nodes for a `5×` target."},
        ],
        "mistakes": [
            ("Dividing the target by a node’s capacity",
             "`5 × 500 rps` does not mean five nodes, because five nodes do not deliver "
             "five nodes&rsquo; worth. The condition to solve is "
             "`N/(1 + α(N − 1)) ≥ T`, which gives six here and ninety-four at a target "
             "of `64×`. Dividing understates the fleet at every size and understates it "
             "badly at large ones."),
            ("Reporting one break-even when the curve crosses twice",
             "&ldquo;Horizontal wins above `3×`&rdquo; is false at `4×`, where the same "
             "rung serves a larger target at the same price. Two numbers are needed: "
             "where horizontal first wins and where it stops losing. The gap between "
             "them is exactly the cost of being pushed onto the next rung early."),
            ("Comparing a rung’s nameplate against a fleet’s node count",
             "The single box delivers what it says; a fleet does not. Comparing `8×` of "
             "box against `8` nodes credits the fleet with capacity it will not produce "
             "&mdash; eight nodes deliver `7.73…×` here. Both sides have to be converted "
             "to delivered capacity before the prices are put next to each other."),
        ],
        "standard": ("Finish when a machine-shape decision arrives with both crossings and a named failure domain.",
                     "You should be able to solve `N/(1 + α(N − 1)) ≥ T` for the node "
                     "count, price both plans across a column of targets, report where "
                     "horizontal first wins and where it stops losing, and say what the "
                     "two prices do not contain."),
        "note": "Both shapes so far were bought for a target capacity, and the target "
                "was treated as a single number. It is not: load has a shape over the "
                "day, capacity is bought for the top of that shape, and the difference "
                "between the top and the average is paid for every hour. "
                "&ldquo;Utilisation and Waste&rdquo; puts a fraction on that gap, and "
                "the fraction is larger than most people guess.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "utilisation-and-waste",
        "title": "Utilisation and Waste",
        "module": "Paying for the peak",
        "one_line": "Compute the fraction of purchased capacity a load profile leaves unused, and show what cutting to the mean would do.",
        "summary": (
            "Capacity is bought for the busiest hour and used at the average one. Buy "
            "`peak/ρ_target` and use the mean, and the share you paid for and did not "
            "use is `1 − mean·ρ_target/peak`. The size of the day cancels out of "
            "that fraction entirely: only the shape of the profile and the target "
            "utilisation move it."
        ),
        "key": [
            "paid = peak/ρ_target          used = mean",
            "waste = 1 − mean·ρ_target/peak     the size of the day cancels",
            "peak 12 000 rps at 21:00,  mean 5 250 rps,  peak/mean = 16/7",
            "ρ_target = 70%  →  paid 17 143 rps, used 5 250 rps",
            "waste = 1 − (5 250 × 0.7)/12 000 = 111/160 = 69.4%",
        ],
        "key_label": "What you buy, what you use, and the gap as a fraction",
        "concepts_intro": (
            "The formula is one line. What it is worth knowing is what is missing from "
            "it, and what happens to a service that acts on the waste figure directly."
        ),
        "concepts": [
            ("You buy for the peak hour, divided by the utilisation you will run it at",
             "Nobody runs the busy hour at a hundred per cent: waiting explodes as "
             "`ρ` approaches one, which is the subject of &ldquo;The Knee: Response "
             "Time vs Utilisation&rdquo;. So the purchase is `peak/ρ_target` &mdash; "
             "`12 000/0.7 = 17 143 rps` here &mdash; and the headroom in that division "
             "is bought deliberately rather than wasted."),
            ("You use the mean, and the ratio of the two is the shape",
             "Every hour below the peak contributes its own gap, and averaged over the "
             "day the capacity actually consumed is the mean: `5 250 rps` against "
             "`17 143` purchased. The `16/7` peak-to-mean ratio is the whole of what "
             "the profile contributes &mdash; the same shape at ten times the traffic "
             "gives exactly the same waste."),
            ("The waste fraction contains no units and no volume",
             "`1 − mean·ρ/peak` is built from a ratio and a fraction, so doubling "
             "every bucket changes nothing and switching from requests to watts changes "
             "nothing. Only two things move it: flattening the profile, and raising the "
             "utilisation you are prepared to run the peak at. That is the entire list."),
        ],
        "read_title": "What is bought, what is used, and the fraction between them",
        "read_intro": (
            "Where the two capacities come from, why the fraction is scale-free, and "
            "what happens if you act on it by cutting to the average."
        ),
        "body": [
            ("def", ("Waste from a load profile",
                     "For a load profile with maximum `peak` and average `mean`, bought "
                     "at a target utilisation `ρ_target` for the busiest hour, the "
                     "<strong>purchased capacity</strong> is `peak/ρ_target`, the "
                     "<strong>used capacity</strong> is `mean`, and the "
                     "<strong>waste</strong> is",
                     "`1 − mean·ρ_target/peak`,",
                     "the share of what was bought that was not used, averaged over the "
                     "period the profile covers.")),
            ("p", "`ρ` here is the `λ/μ` of &ldquo;λ, μ and ρ&rdquo; and nothing "
                  "else: demand over the capacity actually in service. This course does "
                  "not define a second utilisation, and every page that prints a `ρ` "
                  "means that one."),
            ("math", [
                "peak = 12 000 rps at 21:00      mean = 5 250 rps      ρ_target = 7/10",
                "",
                "paid   = peak/ρ = 12 000 ÷ 7/10 = 120 000/7 = 17 142.86 rps",
                "used   = mean    = 5 250 rps",
                "",
                "waste  = 1 − used/paid",
                "       = 1 − 5 250 × 7 / 120 000",
                "       = 1 − 36 750/120 000  =  1 − 49/160  =  111/160",
                "       = 69.375%",
                "",
                "peak/mean = 12 000/5 250 = 16/7 = 2.286",
            ]),
            ("p", "Note the middle line. `used/paid` is `mean·ρ/peak`, which is "
                  "`(mean/peak)·ρ` &mdash; the reciprocal of the peak-to-mean ratio, "
                  "multiplied by the target utilisation. Both factors are pure numbers, "
                  "which is why nothing about the size of the service survives into the "
                  "answer."),
            ("example", ("The same shape, ten times the traffic",
                         "Multiply every hour of the profile by ten. The peak becomes "
                         "`120 000 rps`, the mean `52 500`, the purchase `171 429` "
                         "&mdash; and the waste is `1 − 52 500 × 0.7/120 000`, which "
                         "is `111/160` again. Growth does not improve this number. "
                         "Flattening the profile does, and so does daring to run the "
                         "peak hour hotter.")),
            ("h3", "“Sixty-nine per cent idle, so cut it”"),
            ("p", "This is the misconception the lesson exists for, and it is easy to "
                  "fall into because the number really is `69.4%`. But that figure is an "
                  "average over the day, and the day has a shape: cut the fleet to the "
                  "`5 250 rps` you use on average and nine of the twenty-four hours are "
                  "over capacity, the worst of them by `6 750 rps`."),
            ("p", "At the peak hour the utilisation of that cut fleet would be "
                  "`12 000/5 250 = 16/7`, which is not a busy queue &mdash; it is "
                  "`ρ > 1`, where there is no steady state at all and the backlog grows "
                  "at `λ − μ` for as long as the hour lasts. &ldquo;λ, μ and "
                  "ρ&rdquo; is where that threshold is established; the point here is "
                  "that the waste figure gives no warning of it, because it is a mean "
                  "and the failure is at the maximum."),
            ("example", ("What can actually be cut",
                         "The honest reading of `69.4%` is that the profile is "
                         "expensive, not that the fleet is oversized. Three moves change "
                         "the number and none of them is a straight cut: raise "
                         "`ρ_target` from `70%` to `80%` and the waste falls to "
                         "`1 − 5 250 × 0.8/12 000 = 65%`; move work out of the peak "
                         "hour so the peak-to-mean ratio falls; or put work on the "
                         "trough that does not care when it runs, which raises the mean "
                         "without touching the peak.")),
            ("h3", "The only profile with no waste"),
            ("p", "Set the shape to flat and `peak = mean`, so the waste is "
                  "`1 − ρ_target` &mdash; `30%` at a seventy per cent target, and that "
                  "residue is the headroom, which is not waste at all. A perfectly flat "
                  "profile is the best case and it is rare, which is why batch work, "
                  "index rebuilds and backfills are scheduled into troughs: they are the "
                  "cheapest capacity in the building because they are already paid for."),
            ("p", "The profile this lesson uses is the consumer shape of &ldquo;Peak to "
                  "Average&rdquo;, on &ldquo;Capacity Estimation&rdquo; &mdash; one "
                  "evening peak, a quiet early morning. That course turned a population "
                  "into a peak rate; this one prices the gap that peak leaves behind for "
                  "the other twenty-three hours."),
        ],
        "lab": ("scale", {
            "mode": "waste",
            "panel_title": "Reshape the day and set the target utilisation",
            "panel_intro": (
                "Each bucket is an exact multiple of the profile’s base, so the mean, "
                "the peak and `1 − mean·ρ/peak` are exact fractions. The size of the "
                "day cancels out of the waste entirely: only the shape and `ρ` move it. "
                "Lift one hour at a time and watch the waste fall as the profile "
                "flattens, then set the shape to zero and see the only case in which "
                "nothing is wasted."
            ),
        }),
        "steps_title": "Putting a number on a profile’s waste",
        "steps_intro": "Two capacities and one subtraction — and then the check that stops the number being acted on wrongly.",
        "steps": [
            ("Find the peak bucket and the mean across all of them",
             "The peak is a maximum over the period, not the busiest bucket you happened "
             "to look at. Both come from the same profile, so state the period: a waste "
             "figure over a day and one over a week are different numbers about "
             "different shapes."),
            ("Divide the peak by the utilisation you will run it at",
             "`peak/ρ_target` is what you buy. Choosing `ρ_target` is a latency "
             "decision rather than a cost one &mdash; the response-time multiplier is "
             "`1/(1 − ρ)` &mdash; and it should be decided before this arithmetic "
             "rather than tuned to make the waste look better."),
            ("Compute `1 − mean·ρ_target/peak` and keep it as a fraction",
             "`111/160` here. Keeping it exact makes it obvious that the answer contains "
             "only a ratio and a fraction, and therefore that nothing about the volume "
             "of traffic is in it."),
            ("Test the cut before recommending it",
             "Take the capacity you propose and count the hours of the profile above it, "
             "and the worst overshoot. Cutting to the mean here leaves nine hours over "
             "and a worst case of `6 750 rps`, with `ρ = 16/7` at the peak. That test "
             "is one pass over the buckets and it is what separates a saving from an "
             "outage."),
            ("Say which of the three levers you are proposing",
             "A higher `ρ_target`, a flatter profile, or more work in the trough. "
             "&ldquo;Reduce waste&rdquo; without one of those named is not a proposal, "
             "because the only other way to move the number is to serve less traffic."),
        ],
        "worked": {
            "title": "An evening peak of 12 000 rps against a mean of 5 250",
            "intro": [
                "The profile is the consumer shape: quiet overnight, a long climb, one "
                "peak at 21:00. Everything below is exact."
            ],
            "lines": [
                "peak          12 000 rps  (21:00)",
                "mean           5 250 rps  (over all 24 hours)",
                "peak/mean     12 000/5 250 = 16/7 = 2.286",
                "ρ_target       7/10",
                "",
                "paid          12 000 ÷ 7/10 = 120 000/7 = 17 142.86 rps",
                "used           5 250 rps",
                "",
                "waste         1 − 5 250·(7/10)/12 000",
                "              = 1 − 3 675/12 000",
                "              = 1 − 49/160  =  111/160  =  69.375%",
                "",
                "now test the cut to the mean, 5 250 rps:",
                "  hours above it                    9 of 24",
                "  worst overshoot                   12 000 − 5 250 = 6 750 rps",
                "  ρ at the peak hour                12 000/5 250 = 16/7 > 1",
                "  ⇒ no steady state; backlog grows at λ − μ while it lasts",
                "",
                "and at ρ_target = 8/10 instead:",
                "  waste = 1 − 5 250·(8/10)/12 000 = 1 − 4 200/12 000 = 65%",
            ],
            "after": [
                "The two blocks at the bottom are the lesson. The first shows that the "
                "`69.4%` cannot be taken as slack: acting on it directly puts nine hours "
                "of the day above capacity and the busiest one far above it. The second "
                "shows the lever that does work &mdash; ten points of target utilisation "
                "moved the waste by more than four points, and it cost latency rather "
                "than reliability.",
                "Notice that the volume never appeared. `16/7` and `7/10` are the only "
                "inputs to the waste, and both are pure numbers: the same fraction comes "
                "out for a service a hundred times the size with the same daily shape.",
                "For a faded attempt, take the business profile &mdash; two humps either "
                "side of lunch, which is flatter. Predict before computing whether its "
                "waste is above or below `69.4%` at the same `ρ_target`, then read the "
                "peak, the mean and the waste off the lab and say which of the two "
                "factors did the work."
            ],
        },
        "quiz_title": "Buying for the peak, using the mean",
        "quiz": [
            {"q": "A profile peaks at 12 000 rps and averages 5 250 rps, and the peak hour is to run at `ρ = 70%`. How much capacity is purchased?",
             "a": ["`5 250 rps`", "`8 400 rps`", "`12 000 rps`", "`17 143 rps`"],
             "c": 3,
             "why": "`peak/ρ = 12 000 ÷ 0.7 = 17 142.86`, rounded up to `17 143 rps`. "
                    "`5 250` is the mean, which is what gets used rather than bought. "
                    "`8 400` is `peak × 0.7`, which multiplies where the definition "
                    "divides and buys less than the peak. `12 000` is the peak itself, "
                    "which would mean running the busy hour at `ρ = 1`."},
            {"q": "Every hour of that profile doubles — same shape, twice the traffic. What happens to the waste fraction?",
             "a": ["It halves", "It doubles", "It is unchanged at `111/160`", "It falls, but by less than half"],
             "c": 2,
             "why": "`1 − mean·ρ/peak` depends on `mean/peak` and on `ρ`, and "
                    "doubling every bucket leaves both untouched: `10 500 × 0.7/24 000` "
                    "is the same `49/160` as before. Growth is not a cure for this "
                    "number. Only a flatter shape or a higher target utilisation moves "
                    "it."},
            {"q": "The fleet is cut from 17 143 rps to the 5 250 rps the service uses on average. What does the profile then do?",
             "a": ["It fits, since 5 250 rps is what is actually consumed",
                   "Nine of the twenty-four hours are over capacity, the worst by 6 750 rps, and the peak hour has no steady state",
                   "It fits, but with no headroom, so latency roughly doubles",
                   "Only the single peak hour is over capacity"],
             "c": 1,
             "why": "The mean is an average over a shape, not a bound on it: nine hours "
                    "sit above `5 250 rps` and the peak hour needs `12 000`, so "
                    "`ρ = 16/7 > 1` and the backlog grows at `λ − μ` rather than "
                    "settling at a longer queue. &ldquo;It fits&rdquo; confuses a mean "
                    "with a maximum; &ldquo;latency doubles&rdquo; would require "
                    "`ρ = 1/2`; and it is nine hours over, not one."},
            {"q": "Which change reduces the waste fraction without serving less traffic?",
             "a": ["Buying smaller machines, so the fleet is a closer fit to demand",
                   "Moving deferrable work into the quiet hours",
                   "Measuring the profile per week instead of per day",
                   "Reserving capacity rather than buying it on demand"],
             "c": 1,
             "why": "Work moved into the trough raises the mean while leaving the peak "
                    "alone, so `mean/peak` rises and the waste falls &mdash; and the "
                    "capacity it consumes was already paid for. Machine size does not "
                    "appear in `1 − mean·ρ/peak` at all. Changing the period changes "
                    "which profile you are describing rather than reducing anything. And "
                    "reservation changes the price of an instance-hour, not how many "
                    "instance-hours sit idle."},
        ],
        "mistakes": [
            ("Reading the waste as slack that can be cut",
             "`69.4%` is an average over a shaped day. The fleet is not `69.4%` too "
             "large at any hour &mdash; it is enormously too large at 04:00 and exactly "
             "right at 21:00. Cutting to the mean leaves nine hours over capacity and "
             "the peak hour at `ρ = 16/7`, which is not a slow service but an "
             "unbounded backlog."),
            ("Counting the headroom in `peak/ρ_target` as waste",
             "The gap between `12 000` and `17 143` was bought on purpose, because the "
             "response-time multiplier at `ρ = 1` is unbounded. It shows up inside the "
             "waste fraction, which is why a flat profile still reports "
             "`1 − ρ_target = 30%`. That residue is the price of a latency target "
             "rather than an inefficiency."),
            ("Expecting growth to improve the number",
             "Traffic cancels out of `1 − mean·ρ/peak` completely, so a service that "
             "grows tenfold with the same daily shape wastes the same fraction and ten "
             "times the money. The two things that move it are the shape and the target "
             "utilisation, and neither of them arrives on its own."),
        ],
        "standard": ("Finish when a waste figure always arrives with the shape it came from and a test of the cut it suggests.",
                     "You should be able to compute `peak/ρ_target`, the mean, and "
                     "`1 − mean·ρ_target/peak` as an exact fraction, show that the "
                     "answer does not change when the whole profile is scaled, and count "
                     "the hours a proposed cut would put over capacity before you "
                     "propose it."),
        "note": "That fraction assumed every instance-hour costs the same. It does not: "
                "the same hour can be bought up front at a discount or on demand at a "
                "premium, and the profile decides which is cheaper for each layer of the "
                "fleet. &ldquo;Reserved vs On-demand&rdquo; turns the price ratio into a "
                "utilisation threshold and then reads the optimal reserved level "
                "straight off the profile you just measured.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "reserved-vs-on-demand",
        "title": "Reserved vs On-demand",
        "module": "Paying for the peak",
        "one_line": "Compute the break-even utilisation of a reserved instance and the reserved level that minimises the bill for a profile.",
        "summary": (
            "A reserved instance is paid for whether it runs or not, so it pays off "
            "exactly when it runs more than `reserved price ÷ on-demand price` of the "
            "time. Applied layer by layer to a load profile, that threshold picks the "
            "level to reserve: the floor the profile spends most of its day above, with "
            "everything on top of it bought on demand."
        ),
        "key": [
            "u* = reserved price / on-demand price = 7¢/12¢ = 7/12 = 58.3%",
            "raise the reserved level while the share of hours above it exceeds u*",
            "optimum 12 instances       11 of 24 hours (45.8%) are still above",
            "$51.84 → $37.44 a day       saves $14.40, or 27.8%",
            "reserve the peak instead: $60.48, which is $8.64 worse than reserving none",
            "spot beats on demand only while q < (d − s)/d = 2/3",
        ],
        "key_label": "One price ratio, applied one instance at a time",
        "concepts_intro": (
            "The threshold is a single division. The work is in applying it to a layer "
            "of the fleet rather than to the fleet as a whole."
        ),
        "concepts": [
            ("A reserved instance is a bet on hours, and `u*` is the odds",
             "Reserved costs `r` an hour for every hour of the term whether or not it "
             "serves anything; on demand costs `d` an hour only when it runs. Over any "
             "period, reserving is cheaper exactly when the instance runs more than "
             "`u* = r/d` of it. At `7¢` and `12¢` that is `7/12`, or `58.3%` of the "
             "hours — and nothing else about the profile enters the threshold."),
            ("Reserve a level, not a fleet",
             "The decision is taken one instance at a time, from the bottom of the "
             "profile upward. The first instance runs all twenty-four hours and is an "
             "easy reservation; the thirty-sixth runs for one hour and is an obvious "
             "mistake. Somewhere between them the share of hours above the level falls "
             "through `u*`, and that level is the optimum."),
            ("The marginal rule never evaluates a total",
             "Raising the reserved level by one costs `24r` a day and saves `d` for "
             "every hour the profile is above the new level. So raise while "
             "`hours above × d > 24r`, which is exactly `hours above / 24 > u*`. "
             "Costing every level from zero to the peak gives the same answer &mdash; "
             "`12` here &mdash; and the two agreeing is the check."),
        ],
        "read_title": "The price ratio, the level it picks, and what spot really costs",
        "read_intro": (
            "Where `u*` comes from, the marginal argument that turns it into a level, "
            "the two ways of getting that level wrong, and an interruption model for "
            "spot."
        ),
        "body": [
            ("def", ("Break-even utilisation",
                     "Let `r` be the price of a reserved instance-hour, charged for "
                     "every hour of the term, and `d` the price of an on-demand "
                     "instance-hour, charged only when the instance runs. Over a term "
                     "of `H` hours an instance that runs `uH` of them costs `rH` "
                     "reserved and `duH` on demand, so reserving is cheaper exactly when",
                     "`u > u* = r/d`.",
                     "The term length `H` cancels, so `u*` is a property of the two "
                     "prices alone.")),
            ("p", "`7¢` against `12¢` gives `u* = 7/12 = 58.3%`. Read it as a "
                  "duty cycle: an instance that will be up for more than fourteen hours "
                  "of every twenty-four should be reserved, and one that will not should "
                  "not be. Every other question on this page is which instances those "
                  "are."),
            ("h3", "From a threshold to a level"),
            ("p", "Stack the profile as layers. Layer `k` is the `k`-th instance, and it "
                  "runs during exactly those hours when demand is at or above `k`. Its "
                  "utilisation is therefore the share of hours the profile spends above "
                  "`k`, which falls as `k` rises — so there is one crossing, and it is "
                  "the level to reserve up to."),
            ("math", [
                "r = $0.07000/h     d = $0.12000/h     u* = r/d = 7/12 = 58.3%",
                "",
                "raising the reserved level from k to k+1:",
                "   costs   24r   = 24 × $0.07000 = $1.68 a day",
                "   saves   h·d   where h = hours the profile is above k+1",
                "",
                "   worth it while  h·d > 24r,  i.e.  h/24 > r/d = u*",
                "",
                "the crossing lands at 12 instances:",
                "   hours above 12      11 of 24  =  45.8%  <  58.3%    stop",
                "",
                "and a scan over every level 0 … 36 agrees:  12",
            ]),
            ("p", "The marginal rule is worth preferring because it never evaluates a "
                  "total bill. It compares one day of reservation against one day of the "
                  "hours that reservation covers, and it is the same argument that picks "
                  "an order quantity or a staffing level: raise while the margin is "
                  "positive, stop when it turns."),
            ("example", ("The bill at the three candidate levels",
                         "This profile uses `432` instance-hours a day and peaks at "
                         "thirty-six instances. All on demand: `432 × $0.12 = $51.84`. "
                         "Reserved to `12`: `288` reserved hours at `$0.07` plus `144` "
                         "on-demand at `$0.12`, which is `$20.16 + $17.28 = $37.44`, "
                         "saving `$14.40` a day — `27.8%`. Reserved to the peak of "
                         "thirty-six: `864 × $0.07 = $60.48`, which is `$8.64` worse "
                         "than reserving nothing at all.")),
            ("h3", "Why reserving the peak is worse than reserving nothing"),
            ("p", "The peak hour&rsquo;s instances run for one hour in twenty-four, a "
                  "utilisation of `4.2%` against a threshold of `58.3%`. Reserving them "
                  "buys twenty-three idle hours each, at full price, every day of the "
                  "term. The instinct behind it is a good one — the peak is the part "
                  "that hurts — but the peak is precisely the part with the worst duty "
                  "cycle, and a commitment is a bet on hours rather than on importance."),
            ("p", "The opposite error is quieter. Reserving nothing leaves the bottom "
                  "twelve instances, which run every hour of every day at `100%` "
                  "utilisation, paying the on-demand premium for capacity that is never "
                  "not needed. That is the `$14.40` a day the optimum recovers."),
            ("h3", "Spot is not simply the cheapest column"),
            ("p", "A spot instance-hour at `s` can be reclaimed part-way through, and "
                  "the work still has to be done, so an interrupted hour is re-bought on "
                  "demand. With a reclaim probability `q` the expected delivered cost is "
                  "`s + q·d`, which at `s = $0.04`, `d = $0.12` and `q = 15%` is "
                  "`$0.058` &mdash; genuinely below `$0.12`, but nowhere near the "
                  "headline `$0.04`."),
            ("math", [
                "delivered cost of a spot hour    s + q·d",
                "beats on demand while            s + q·d < d",
                "                                 q < (d − s)/d = (12 − 4)/12 = 2/3",
                "",
                "at q = 15%:   $0.04000 + 0.15 × $0.12000 = $0.05800 delivered",
                "burst layer on spot:  $28.51 a day, against $51.84 all on demand",
            ]),
            ("p", "So spot is a third arm on the same comparison rather than a free "
                  "lunch: it wins while interruptions are rarer than two in three, and "
                  "it is the burst layer &mdash; the one with the utilisation too low to "
                  "reserve &mdash; that it belongs on."),
            ("p", "Everything above assumes the profile is known. When it is a forecast "
                  "with a distribution around it, the quantity to commit to is a "
                  "quantile of that distribution rather than a level of a known shape, "
                  "which is the newsvendor problem &mdash; solved in &ldquo;The "
                  "Newsvendor Problem&rdquo; in the Operations Research course "
                  "&ldquo;Inventory Models&rdquo;, with the under-commitment and "
                  "over-commitment costs in the shortage and overage roles."),
        ],
        "lab": ("scale", {
            "mode": "reserve",
            "panel_title": "Set both prices and reshape the profile",
            "panel_intro": (
                "`u*` is the price ratio exactly. The optimal reserved level is found "
                "twice &mdash; by the marginal rule, which never evaluates a total, and "
                "by costing every level from zero to the peak &mdash; and the two must "
                "agree. Spot is priced with an interruption model, because without one "
                "it is only a smaller number. Drag the reserved price up toward the "
                "on-demand price and watch the optimal level collapse toward zero."
            ),
        }),
        "steps_title": "Choosing what to commit to",
        "steps_intro": "The threshold first, because it is one division and it decides how the profile is read.",
        "steps": [
            ("Divide the reserved price by the on-demand price",
             "`u* = r/d`. That is the duty cycle a commitment needs to pay for itself, "
             "and it is independent of the term, the profile and the size of the fleet. "
             "At `7¢` and `12¢` it is `58.3%`, or just over fourteen hours a day."),
            ("Turn the profile into hours-above-a-level",
             "For each level `k`, count the hours the profile is at or above `k`. That "
             "count divided by the period is the `k`-th instance&rsquo;s utilisation, "
             "and it is what the threshold is compared against."),
            ("Raise the level while the share above it exceeds `u*`",
             "Stop at the first level where it does not. Here that is `12`, with `45.8%` "
             "of hours above it against a threshold of `58.3%`. No total has been "
             "computed at any point in this step."),
            ("Cost the whole plan once, and cost two wrong plans beside it",
             "The optimum, reserving nothing, and reserving the peak: `$37.44`, `$51.84` "
             "and `$60.48` a day. The third being worse than the second is the number "
             "that makes the argument, and it is invisible if only the recommendation is "
             "priced."),
            ("Price spot with its interruption rate, not its sticker",
             "`s + q·d` is what a delivered spot hour costs, and `q < (d − s)/d` is "
             "the condition for it to beat on demand at all. Put it on the burst layer, "
             "which is the layer whose utilisation was too low to reserve."),
        ],
        "worked": {
            "title": "7¢ reserved against 12¢ on demand, on an evening-peaking profile",
            "intro": [
                "The profile uses 432 instance-hours a day and peaks at thirty-six "
                "instances. The threshold is computed once and then applied upward."
            ],
            "lines": [
                "u* = r/d = 0.07/0.12 = 7/12 = 58.3%",
                "        ⇒ a commitment needs 14.0 of every 24 hours to pay",
                "",
                "marginal test, level k → k+1:",
                "   cost   24 × $0.07000 = $1.68 a day",
                "   save   (hours above k+1) × $0.12000",
                "   raise while hours above > 14",
                "",
                "   … the crossing lands at level 12",
                "   hours above 12:  11 of 24 = 45.8%  <  58.3%     so stop at 12",
                "   full scan of levels 0 … 36 also returns 12     ✓",
                "",
                "cost a day, three plans:",
                "   reserve nothing   432 on demand              $51.84",
                "   reserve 12        288 res + 144 on demand    $37.44   −$14.40  (27.8%)",
                "   reserve the peak  864 reserved               $60.48   +$8.64",
                "",
                "spot on the burst layer, s = $0.04000, q = 15%:",
                "   delivered   $0.04000 + 0.15 × $0.12000 = $0.05800 an hour",
                "   plan        288 res + 144 spot             $28.51   −$23.33",
                "   and spot beats on demand only while q < (12 − 4)/12 = 2/3",
            ],
            "after": [
                "The `+$8.64` line is the one to remember. Reserving the peak is not a "
                "cautious version of reserving the optimum &mdash; it is worse than "
                "making no commitment at all, because the instances it commits to are "
                "the ones that run for an hour a day.",
                "The spot block shows why an interruption model is not optional. The "
                "sticker price is a third of on demand; the delivered price is under "
                "half of it; and at a reclaim rate of two in three the two are equal and "
                "spot stops being cheap at all. Quoting `$0.04` without `q` is quoting a "
                "price for something you may not receive.",
                "For a faded attempt, raise the reserved price to `10¢` and leave on "
                "demand at `12¢`. Compute the new `u*` first and predict from it alone "
                "whether the optimal level rises or falls, then find the level and the "
                "three daily bills in the lab and say how much of the original saving "
                "survived."
            ],
        },
        "quiz_title": "Commitments, levels and delivered prices",
        "quiz": [
            {"q": "A reserved instance-hour costs `7¢` and an on-demand one `12¢`. Above what utilisation does reserving pay?",
             "a": ["`41.7%`", "`58.3%`", "`70.0%`", "`171.4%`"],
             "c": 1,
             "why": "`u* = r/d = 7/12 = 58.3%`. `41.7%` is `1 − u*`, the share of the "
                    "term the reservation may be idle rather than the share it must run. "
                    "`70.0%` is the reserved price read as a percentage, which is a price "
                    "and not a utilisation. `171.4%` is `d/r`, the ratio the wrong way up, "
                    "and no instance runs more than all of the time."},
            {"q": "Why is reserving the peak (`$60.48` a day) worse than reserving nothing (`$51.84`)?",
             "a": ["Because reserved capacity cannot be resized once committed",
                   "Because the top instances run about one hour in twenty-four, far below the 58.3% a commitment needs",
                   "Because the peak hour is short enough that on-demand capacity is discounted",
                   "Because the reserved price applies only below the mean"],
             "c": 1,
             "why": "A commitment pays for every hour of the term. The thirty-sixth "
                    "instance serves one hour a day &mdash; a duty cycle near `4%` "
                    "against a threshold of `58.3%` &mdash; so twenty-three hours of it "
                    "are bought and wasted daily. Resizing is not in this model; "
                    "on-demand is a flat `12¢` with no volume discount; and the reserved "
                    "price applies to whatever level you choose, which is the decision "
                    "being made."},
            {"q": "Spot is `$0.04` an hour against on demand at `$0.12`, and 15% of spot hours are reclaimed and must be re-bought on demand. What does a delivered spot hour cost?",
             "a": ["`$0.04000`", "`$0.04600`", "`$0.05800`", "`$0.10200`"],
             "c": 2,
             "why": "`s + q·d = $0.04 + 0.15 × $0.12 = $0.058`. `$0.04000` is the "
                    "sticker, which is what you pay for an hour you may not get to keep. "
                    "`$0.04600` charges the interruption at the spot price "
                    "(`s + q·s`) rather than at the price the work is actually "
                    "re-bought at. `$0.10200` is `s + q` treated as dollars, mixing a "
                    "probability with a price."},
            {"q": "The reserved price is raised from `7¢` to `11¢` while on demand stays at `12¢`. What happens to the optimal reserved level?",
             "a": ["It rises, because reserving is now closer to on-demand pricing",
                   "It falls, because `u*` rises to `91.7%` and fewer layers clear it",
                   "It does not move; the level depends on the profile, not the prices",
                   "It falls to zero, because there is no longer any saving"],
             "c": 1,
             "why": "`u* = 11/12 = 91.7%`, so only layers running more than about "
                    "twenty-two hours a day still pay, and the level drops to the "
                    "profile&rsquo;s near-constant floor. It does not reach zero: an "
                    "instance that runs all twenty-four hours still has `u = 100% > u*` "
                    "and is still worth reserving. And the level depends on both &mdash; "
                    "the profile supplies the hours-above curve and the prices supply "
                    "the threshold it is cut at."},
        ],
        "mistakes": [
            ("Reserving for the peak",
             "The peak is the part of the profile with the worst duty cycle, so it is "
             "the worst possible thing to commit to. Here it costs `$60.48` a day "
             "against `$51.84` for no commitment at all. The instinct — cover the part "
             "that hurts — is answering a reliability question with a pricing "
             "instrument."),
            ("Comparing total bills instead of the margin",
             "&ldquo;Reserving is 27.8% cheaper&rdquo; is an outcome, not an argument, "
             "and it cannot tell you whether `11` or `13` would have been better. The "
             "rule that can is the marginal one: raise while the share of hours above "
             "the level exceeds `u*`. Costing every level is then the check on it, not "
             "the method."),
            ("Quoting spot at its sticker price",
             "`$0.04` is the price of an hour that may be taken back. With `15%` "
             "reclaimed and the work re-bought on demand, the delivered price is "
             "`$0.058`, and above a reclaim rate of `2/3` spot costs more than on "
             "demand outright. A spot saving with no `q` beside it is not a number."),
        ],
        "standard": ("Finish when a commitment is justified by a duty cycle rather than by a discount.",
                     "You should be able to compute `u* = r/d`, turn a profile into "
                     "hours-above-a-level, pick the reserved level by the marginal rule "
                     "and confirm it by scanning every level, and price both the "
                     "reserve-nothing and reserve-the-peak plans beside the one you "
                     "recommend."),
        "note": "Reservation and on-demand both assume capacity appears when it is "
                "asked for. It does not: instances take time to boot, and during that "
                "window demand is served by the fleet that already exists. &ldquo;"
                "Autoscaling Lag&rdquo; puts an area on that window, and the surprise is "
                "that without a warm reserve the requests missed during the boot are "
                "never made up.",
    },
]
