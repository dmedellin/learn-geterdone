"""Course 5, lessons 08-13 - the load a system makes for itself, then durability and blast radius."""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "retries-and-request-amplification",
        "title": "Retries and Request Amplification",
        "module": "Budgets and retries",
        "one_line": "Compute the attempts a retry policy costs per request and the success probability it buys.",
        "summary": (
            "A policy of `r` retries after a failed attempt costs "
            "`(1 − pʳ⁺¹)/(1 − p)` attempts per request and delivers success with "
            "probability `1 − pʳ⁺¹`. Both are geometric series in the failure "
            "probability, and both move the wrong way together: as `p` rises the success "
            "falls and the cost climbs toward `r + 1`, so the policy is cheapest when it "
            "is least needed and most expensive at the moment the service can least "
            "afford it."
        ),
        "key": [
            "attempts = (1 − pʳ⁺¹)/(1 − p) = 1 + p + p² + … + pʳ",
            "success  = 1 − pʳ⁺¹                 lost = pʳ⁺¹",
            "p = 0.1, r = 2:  1.11 attempts, 99.9% success, 1 in 1000 lost",
            "p = 0.9, r = 2:  2.71 attempts     p → 1:  attempts → r + 1",
        ],
        "key_label": "One geometric series, read as cost and as benefit",
        "concepts_intro": (
            "The same sum answers both questions a retry policy raises, which is why they "
            "cannot be traded against each other freely."
        ),
        "concepts": [
            ("Attempt i happens only if every earlier one failed",
             "The first attempt always happens. The second happens with probability `p`, "
             "the third with `p²`, and attempt `i + 1` with `pⁱ`. Summing over the "
             "`r + 1` attempts the policy allows gives the expected attempts per request: "
             "`1 + p + p² + … + pʳ = (1 − pʳ⁺¹)/(1 − p)`. That is the amplification "
             "factor &mdash; the number by which the offered load is multiplied before "
             "the service sees it."),
            ("Success is the complement of everything failing",
             "A request is lost only when all `r + 1` attempts fail, which under "
             "independence is `pʳ⁺¹`, so the policy succeeds with probability "
             "`1 − pʳ⁺¹`. At `p = 0.1` and `r = 2` that is `99.9%`, bought for `1.11` "
             "attempts a request &mdash; an eleven per cent surcharge for a factor of a "
             "hundred in the loss rate, which is why retries are standard."),
            ("The cost is worst exactly when the service is worst",
             "`(1 − pʳ⁺¹)/(1 − p)` is increasing in `p` and tends to `r + 1` as `p` "
             "approaches one. The same two-retry policy that costs `1.11` attempts at a "
             "`10%` failure rate costs `2.71` at `90%` and `2.97` at `99%`. The "
             "surcharge arrives as extra load precisely when the service is already "
             "failing, and that is the feedback the next lesson closes."),
        ],
        "read_title": "The geometric series behind a retry policy",
        "read_intro": (
            "Where the attempt count comes from, what it buys, and the two shapes of "
            "duplicate work the same series also counts."
        ),
        "body": [
            ("def", ("Retry policy, attempts and success",
                     "A <strong>retry policy</strong> of `r` retries makes up to "
                     "`r + 1` attempts at a request, stopping at the first success. If "
                     "each attempt fails independently with probability `p`, the expected "
                     "number of <strong>attempts</strong> per request is "
                     "`(1 − pʳ⁺¹)/(1 − p)` and the probability the request eventually "
                     "<strong>succeeds</strong> is `1 − pʳ⁺¹`. The ratio of attempts to "
                     "requests is the <strong>amplification factor</strong>.")),
            ("p", "The independence of attempts is a real assumption and it is generous. "
                  "A request that failed because its payload is malformed will fail again "
                  "with probability `1`, and one that failed because a shard is down will "
                  "fail again until the shard returns. Retrying a deterministic failure "
                  "buys nothing and costs the full amplification, which is why policies "
                  "distinguish retriable errors from the rest."),
            ("math", [
                "p = 1/10,  r = 2,  offered load 500 rps",
                "",
                "attempt      P(it is ever made)     at 500 rps",
                "the request        p⁰ = 1             500.0 /s",
                "retry 1            p¹ = 1/10           50.0 /s",
                "retry 2            p² = 1/100           5.0 /s",
                "                   ────────           ────────",
                "attempts = 111/100 = 1.1100            555.0 /s",
                "",
                "lost anyway  p³ = 1/1000        success = 999/1000 = 99.9000%",
                "share of the load that is retry traffic = 0.11/1.11 = 9.91%",
            ]),
            ("p", "Eleven per cent more load for a hundredfold reduction in loss is an "
                  "easy trade, and it is the trade every default retry configuration is "
                  "quietly making. The difficulty is that the eleven per cent is not a "
                  "constant."),
            ("h3", "What the same policy costs when things are bad"),
            ("math", [
                "the same r = 2 policy, at three failure rates",
                "",
                "p = 0.10     attempts 1.110     success 99.9000%",
                "p = 0.50     attempts 1.750     success 87.5000%",
                "p = 0.90     attempts 2.710     success 27.1000%",
                "p = 0.99     attempts 2.970     success  2.9701%",
                "",
                "as p → 1:   attempts → r + 1 = 3,   success → 0",
            ]),
            ("p", "Read the two columns together. At a `90%` failure rate the policy has "
                  "nearly tripled the load and is delivering just over a quarter of the "
                  "requests; at `99%` it has tripled the load to deliver three per cent. "
                  "The load multiplier saturates at `r + 1` while the benefit collapses, "
                  "so the policy is at its most expensive and least useful in the same "
                  "regime."),
            ("example", ("Duplicate work under at-least-once delivery",
                         "The same series counts something else. If an attempt can "
                         "succeed at the server and still be retried &mdash; a timeout "
                         "on the response rather than on the request &mdash; then every "
                         "attempt beyond the first is duplicate work at the server, and "
                         "the expected duplicates per request are "
                         "`attempts − 1 = p + p² + … + pʳ`. At `p = 0.1, r = 2` that is "
                         "`0.11`, or `9.91%` of the server's work. This is one line of "
                         "the geometric series rather than a separate model, and it is "
                         "the reason at-least-once delivery needs idempotent handlers.")),
            ("h3", "Retries multiply along a chain"),
            ("p", "The factor compounds with depth. A request crossing three tiers, each "
                  "retrying twice at `p = 0.1`, produces `1.11` attempts at the first "
                  "tier, `1.11²` at the second and `1.11³ ≈ 1.368` at the third: a "
                  "`37%` surcharge on the innermost service from a policy that looked "
                  "like `11%` at each hop. When the innermost service degrades, every "
                  "tier above it begins retrying at once and the product is what arrives."),
            ("example", ("Why retry budgets are per-client, not per-call",
                         "The standard mitigation is a cap on the fraction of a client's "
                         "traffic that may be retries &mdash; typically a few per cent "
                         "&mdash; enforced across the client rather than per call site. "
                         "At `p = 0.1` and `r = 2` the retry share is `9.91%`, already "
                         "over such a budget, and the budget is what stops the share "
                         "reaching `66.33%`, which is where `p = 0.99` puts it. The cap "
                         "does not make retries cheaper; it makes the amplification "
                         "bounded by something other than `r + 1`.")),
            ("p", "The last figure is the one to carry into the next lesson. A policy "
                  "whose cost rises with the failure rate, in a system whose failure rate "
                  "rises with load, is a loop. Nothing in this lesson closes it; the "
                  "amplification is computed here against a failure probability handed in "
                  "from outside."),
        ],
        "lab": ("avail", {
            "mode": "retry",
            "p_pct": 10,
            "retries": 2,
            "rps": 500,
            "panel_title": "Set the failure rate and the policy",
            "panel_intro": "Two retries at a ten per cent failure rate, over 500 requests "
                           "a second. The ladder shows one bar per attempt at the "
                           "probability it is ever reached, and the bars sum to the "
                           "attempts each request costs. Drag the failure rate to 90% and "
                           "watch the amplification climb while the success column falls.",
        }),
        "steps_title": "Pricing a retry policy",
        "steps_intro": (
            "Two numbers come out of the same series, and the fourth step is the one that "
            "stops the policy being sized against the wrong day."
        ),
        "steps": [
            ("Check that the failure is worth retrying at all",
             "An attempt must have an independent chance of succeeding. A malformed "
             "request, a rejected credential or a permanently missing key fails "
             "identically every time, so the policy pays the full amplification for a "
             "success probability of zero. Retry timeouts and transient errors; do not "
             "retry a deterministic failure."),
            ("Compute the attempts and the success from the same p",
             "`attempts = (1 − pʳ⁺¹)/(1 − p)` and `success = 1 − pʳ⁺¹`. Write both down "
             "together: quoting the success without the attempts is how a policy gets "
             "adopted without its cost being noticed."),
            ("Multiply the offered load by the amplification",
             "`λ × attempts` is what the service actually receives. At 500 rps and `1.11` "
             "attempts that is 555 attempts a second, of which `9.91%` is retry traffic "
             "&mdash; and along a three-tier chain the factors multiply rather than add."),
            ("Evaluate the same policy at the failure rate of a bad day",
             "Recompute at `p = 0.5` and `p = 0.9`. The healthy-day figure decides "
             "nothing; the bad-day figure decides whether the policy is survivable. If "
             "`λ × (r + 1)` exceeds capacity, the policy has a worst case the system "
             "cannot serve."),
        ],
        "worked": {
            "title": "Three retries at 2000 rps: the healthy day and the bad one",
            "intro": [
                "A team proposes three retries rather than two, on the grounds that the "
                "extra attempt is almost never used. That is true on the healthy day, "
                "and the healthy day is not what the capacity has to cover.",
            ],
            "lines": [
                "r = 3, so up to 4 attempts,  offered λ = 2000 rps",
                "",
                "the healthy day,  p = 0.05",
                "attempts = 1 + 0.05 + 0.0025 + 0.000125 = 1.052625",
                "load     = 2000 × 1.052625 = 2105.25 /s      a 5.3% surcharge",
                "success  = 1 − 0.05⁴ = 1 − 0.00000625 = 99.999375%",
                "",
                "the bad day,  p = 0.9",
                "attempts = 1 + 0.9 + 0.81 + 0.729 = 3.439",
                "load     = 2000 × 3.439 = 6878 /s           a 244% surcharge",
                "success  = 1 − 0.9⁴ = 1 − 0.6561 = 34.39%",
                "",
                "the ceiling",
                "as p → 1,  attempts → r + 1 = 4,  load → 8000 /s",
                "",
                "the same comparison at r = 2",
                "p = 0.9   attempts 2.71   load 5420 /s    ceiling 6000 /s",
            ],
            "after": [
                "The fourth attempt costs `0.000125` of an attempt on the healthy day and "
                "`0.729` on the bad one, which is the whole argument. Choosing `r` on "
                "healthy-day evidence sizes the policy against the case where it does "
                "nothing; the number that has to fit inside the capacity is "
                "`λ × (r + 1)`, and at `r = 3` that is four times the offered load.",
                "Note what the bad-day success column says about the benefit as well. "
                "Going from `r = 2` to `r = 3` at `p = 0.9` raises the success rate from "
                "`27.1%` to `34.39%` while raising the load ceiling from `6000` to "
                "`8000`. Both directions are worse than they look on the healthy day.",
                "For a faded rehearsal, the service has a capacity of `5000` rps and an "
                "offered load of `2000`. The supplied first move is that the binding "
                "constraint is the ceiling `λ × (r + 1)`, not the expected attempts. Find "
                "the largest `r` whose worst case fits inside capacity, then compute the "
                "success probability that choice gives at `p = 0.5` and at `p = 0.9`, and "
                "check both against the lab.",
            ],
        },
        "quiz_title": "Attempts and amplification",
        "quiz": [
            {"q": "A policy allows two retries and each attempt fails independently with probability `p = 0.1`. What is the expected number of attempts per request?",
             "a": ["`3`, since three attempts are allowed", "`1.11`", "`1.2`", "`0.111`"],
             "c": 1,
             "why": "`1 + p + p² = 1 + 0.1 + 0.01 = 1.11`. The first choice is the "
                    "ceiling `r + 1`, which is the limit as `p` approaches one rather "
                    "than the expectation here. `1.2` counts both retries at full weight "
                    "instead of weighting the second by the probability that the first "
                    "also failed. `0.111` is the retry surcharge misplaced by a factor "
                    "of ten."},
            {"q": "The same two-retry policy is evaluated at `p = 0.1` and at `p = 0.9`. What happens to the amplification?",
             "a": ["It falls, because more attempts succeed early when `p` is high",
                   "It stays at `1.11`; the policy does not depend on the failure rate",
                   "It rises from `1.11` to `2.71`, approaching `r + 1 = 3` as `p` approaches one",
                   "It rises to exactly `3`, since at `p = 0.9` nearly everything is retried"],
             "c": 2,
             "why": "`1 + 0.9 + 0.81 = 2.71`. The series is increasing in `p` and its "
                    "limit is `r + 1`, which it approaches without reaching: at `p = 0.99` "
                    "it is `2.97`. This is the property the whole course turns on here "
                    "&mdash; the policy adds the most load exactly when the service is "
                    "failing most."},
            {"q": "A request crosses three tiers, each retrying twice at `p = 0.1`. What load does the innermost tier see, relative to the original request rate?",
             "a": ["`1.11×`, since the amplification is a property of the policy",
                   "`3.33×`, the three amplifications added",
                   "`1.368×`, the three amplifications multiplied",
                   "`1×`, because only the outermost tier retries"],
             "c": 2,
             "why": "Each tier multiplies what it receives, so the factors compound: "
                    "`1.11³ ≈ 1.368`. The surcharge that looked like eleven per cent per "
                    "hop is thirty-seven per cent at the bottom, and it is far larger "
                    "when the innermost tier is the one failing, because every tier "
                    "above then retries at its bad-day rate at once."},
        ],
        "mistakes": [
            ("Treating retries as free because they usually succeed",
             "The `11%` surcharge at a ten per cent failure rate is a fact about a "
             "healthy service. The same policy costs `2.71` attempts at `p = 0.9` and "
             "tends to `r + 1`, so capacity has to cover `λ × (r + 1)` rather than "
             "`λ × 1.11`. A policy sized against the healthy day is sized against the "
             "case in which it does nothing."),
            ("Retrying failures that cannot succeed",
             "The formulas assume attempts fail independently. A malformed payload, a "
             "bad credential and a missing key fail identically on every attempt, so the "
             "policy pays `r + 1` attempts for a success probability of zero and returns "
             "the same error `r + 1` times more slowly. Classify errors before "
             "configuring retries."),
            ("Counting the amplification once on a multi-tier path",
             "Three tiers each retrying twice do not add to `3 × 11%`; they multiply to "
             "`1.11³ ≈ 1.368`. Worse, the factors are correlated in time: when the "
             "bottom tier degrades every tier above it reaches its bad-day amplification "
             "simultaneously, so the innermost service sees the product of three "
             "bad-day factors rather than three healthy ones."),
        ],
        "standard": ("Finish when a proposed retry count reads as a multiple of the offered load rather than as a number of chances.",
                     "You should be able to compute attempts and success from the same "
                     "geometric series, convert an amplification into a load, evaluate "
                     "the policy at a bad-day failure rate, and say why the factors "
                     "multiply rather than add along a chain of tiers."),
        "note": 'This lesson takes the failure probability as given. In a loaded system it is not given: it rises with utilisation, and the retries that rise with it are themselves load. &ldquo;Retry Storms&rdquo; closes that loop and iterates it, and the fixed point it lands on can sit above capacity when the load without retries was comfortably inside it.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "retry-storms",
        "title": "Retry Storms",
        "module": "Budgets and retries",
        "one_line": "Iterate the load-failure-retry map to its fixed point and say whether that point is above capacity.",
        "summary": (
            "Load raises the failure rate, the failure rate raises the amplification, and "
            "the amplification raises the load. Iterating that map from an offered load "
            "of `0.95` of capacity, with three retries and a ten per cent base failure "
            "rate, walks `0.95 → 1.06 → 1.11 → 1.17 → 1.24` and settles at `1.727` "
            "&mdash; above capacity, from a starting point that was comfortably inside "
            "it. The retries are not a response to the overload; they are the overload."
        ),
        "key": [
            "p(L) = base + (1 − base)·max(0, (L − C)/L)      failure rises with load",
            "L′   = λ · (1 − p(L)ʳ⁺¹)/(1 − p(L))             retries raise the load",
            "λ = 0.95 C, base = 0.10, r = 3   →  fixed point 1.727 C",
            "the failure rate there is 0.479 and the amplification 1.818",
        ],
        "key_label": "A map from load to load, and where it settles",
        "concepts_intro": (
            "Two functions from the last two lessons, composed. Neither is new; the "
            "composition is, and so is the answer it lands on."
        ),
        "concepts": [
            ("Failure rises with load, by a model you state",
             "Above capacity the server cannot finish everything inside a client's "
               "patience, and the share it does finish is `C/L`, so the failure "
             "probability is `base + (1 − base)·(L − C)/L`. Below capacity it is just "
             "`base`. That is this lesson's model, stated rather than assumed, and the "
             "lab evaluates it rather than drawing a curve someone liked the shape of."),
            ("Composing the two gives a map from load to load",
             "`L′ = λ · attempts(p(L))`. Feed a load in, get the failure rate it causes, "
             "get the amplification that failure rate produces, multiply the original "
             "offered load by it. The result is the load the service actually sees, and "
             "feeding it back in is one step of the iteration. Three steps by hand are "
             "enough to see which way it is going."),
            ("The fixed point can sit above capacity when the offered load did not",
             "Starting at `0.95` of capacity with three retries and a `10%` base failure "
             "rate, the iteration passes capacity on its first step and settles at "
             "`1.727`. Nothing external changed: the offered load was serviceable "
             "throughout, and the policy meant to protect requests is what is drowning "
             "the service. Switching the retries off returns the load to `0.95`."),
        ],
        "read_title": "The loop, the iteration and the fixed point",
        "read_intro": (
            "How the two earlier formulas compose into a feedback loop, what iterating it "
            "looks like, and why a bracket answers a question the iteration cannot afford to."
        ),
        "body": [
            ("def", ("The retry-storm map",
                     "Write `C` for capacity, `λ` for the offered load before retries, "
                     "`base` for the failure probability under no overload and `r` for "
                     "the retry count. Define `p(L) = base + (1 − base)·max(0, (L − C)/L)` "
                     "and `L′ = λ · (1 − p(L)ʳ⁺¹)/(1 − p(L))`. A "
                     "<strong>fixed point</strong> is a load with `L′ = L`; the system's "
                     "steady state is such a point, if one exists below the ceiling "
                     "`λ(r + 1)`.")),
            ("p", "Capacity is the unit: every load on this page is a multiple of `C`, "
                  "so `C = 1` and the offered load `λ = 0.95` means ninety-five per cent "
                  "of capacity. The base failure rate is what the service returns when "
                  "it is not overloaded &mdash; a small tail of genuine errors, here ten "
                  "per cent, which is high enough to make the iteration visible in five "
                  "steps."),
            ("h3", "Five steps of the map, by hand"),
            ("math", [
                "λ = 0.95, C = 1, base = 0.10, r = 3",
                "",
                "step  load in     p        attempts   load out    denominator digits",
                " 1    0.95000   0.10000    1.11100    1.05545              5",
                " 2    1.05545   0.14728    1.17217    1.11356             13",
                " 3    1.11356   0.19178    1.23562    1.17384             39",
                " 4    1.17384   0.23328    1.30040    1.23538            119",
                " 5    1.23538   0.27148    1.36519    1.29693            358",
                "",
                "the first step alone crosses capacity: 0.95 × 1.111 = 1.05545",
            ]),
            ("p", "Work step two by hand and the loop stops being a metaphor. The load "
                  "is `1.05545`, so the overload share is "
                  "`(1.05545 − 1)/1.05545 = 0.05254`, and the failure rate is "
                  "`0.1 + 0.9 × 0.05254 = 0.14728`. Four attempts at that rate cost "
                  "`1 + 0.14728 + 0.02169 + 0.00319 = 1.17217`, and `0.95 × 1.17217` is "
                  "`1.11356`. Every figure in the row came from the row above it."),
            ("p", "The last column is worth a sentence of its own. The amplification "
                  "carries the `r`-th power of the failure rate's denominator, so each "
                  "step cubes it at `r = 3`: five digits, then thirteen, thirty-nine, a "
                  "hundred and nineteen, three hundred and fifty-eight. By the seventh "
                  "iterate the exact fraction has over three thousand digits, and the "
                  "table stops and says so rather than silently rounding."),
            ("h3", "Bracketing the fixed point instead of iterating to it"),
            ("p", "The iteration cannot reach the answer, so the lab does not use it to. "
                  "The map is increasing in `L` and bounded above by `λ(r + 1)`, so the "
                  "function `g(L) = L′ − L` is non-negative at `λ` and non-positive at "
                  "`λ(r + 1)`, and a root is trapped between them. Bisection evaluates "
                  "the map afresh at each probe, so nothing compounds and the "
                  "denominators stay small."),
            ("math", [
                "λ = 0.95, base = 0.10, r = 3",
                "",
                "fixed point bracketed at   1.72736  ≤  L*  ≤  1.72736",
                "failure rate there                   p = 0.47897",
                "amplification there                      1.8183",
                "",
                "with the retries switched off            0.95000",
                "",
                "check:  0.95 × 1.8183 = 1.72739 ≈ L*        ✓",
            ]),
            ("p", "The result is an enclosure rather than a rounded number: the fixed "
                  "point is at least the lower bound and at most the upper one, and both "
                  "ends are exact fractions. At this setting the two ends agree to five "
                  "decimal places, which is why the readout prints the same figure twice."),
            ("example", ("The service that could have served the load",
                         "`0.95` of capacity was serviceable. With three retries the "
                         "system settles at `1.727` of capacity and a `47.9%` failure "
                         "rate &mdash; and that failure rate is what sustains the "
                         "amplification that produced the load. Turn the retries off in "
                         "the lab and the load returns to `0.95` immediately. The "
                         "overload has no external cause at all, which is exactly why it "
                         "does not end when the original trigger does.")),
            ("h3", "Where the transition is"),
            ("p", "It is not gradual. At the same `10%` base rate and three retries, an "
                  "offered load of `0.80` settles at `0.8888` and one of `0.90` settles "
                  "at `0.9999` &mdash; both below capacity and stable in a single step. "
                  "`0.95` settles at `1.727`. The system is fine, fine, and then "
                  "eighty per cent over capacity, and the parameter that moved was five "
                  "per cent of offered load."),
            ("example", ("The retry count as the control",
                         "Hold the offered load at `0.95` and vary only the policy: with "
                         "no retries the fixed point is `0.95`, with one retry `1.168`, "
                         "with two `1.439`, with three `1.727`. Every one of those is the "
                         "same traffic against the same service. The policy is not a "
                         "response to the overload in any of the last three cases; it is "
                         "the whole of it.")),
        ],
        "lab": ("avail", {
            "mode": "storm",
            "load_pct": 95,
            "base_pct": 10,
            "retries": 3,
            "steps": 5,
            "panel_title": "Set the load and the retry policy",
            "panel_intro": "An offered load of 95% of capacity with three retries. Work "
                           "the first three rows of the table by hand before reading the "
                           "fixed point &mdash; the iterates move away from where the "
                           "offered load sits, and watching that happen is the point. "
                           "Then set the retries to none and watch the same load stay put.",
        }),
        "steps_title": "Iterating the loop",
        "steps_intro": (
            "Three of these are arithmetic you already have. The fourth is the question the "
            "arithmetic was for."
        ),
        "steps": [
            ("State the failure model and the capacity",
             "Write down what failure probability each load produces, and in what units "
             "capacity is measured. This lesson uses "
             "`p(L) = base + (1 − base)(L − C)/L` above capacity and `base` below it; a "
             "different model gives different numbers and the same shape of conclusion, "
             "but it has to be written down either way."),
            ("Apply the map by hand three times",
             "Failure rate from the load, amplification from the failure rate, load from "
             "the amplification times the original offered load. Three iterations are "
             "enough to see the direction, and doing them by hand is what makes the "
             "fourth believable."),
            ("Find the fixed point by bracketing, not by iterating",
             "The map is increasing and bounded by `λ(r + 1)`, so bisect between the "
             "offered load and that ceiling. Iterating instead compounds the exact "
             "fractions until they are unusable, and rounding them is how a divergence "
             "gets reported as a convergence."),
            ("Compare the fixed point with capacity, and with the offered load",
             "Above capacity is a storm; below it the policy is affordable. Then compare "
             "with the load that would have applied with no retries at all, because that "
             "difference is the part the system did to itself and the only part a policy "
             "change can remove."),
        ],
        "worked": {
            "title": "Two retries at 90% offered load, and what one more retry does",
            "intro": [
                "A service running at ninety per cent of capacity with a five per cent "
                "base failure rate. The question on the table is whether to raise the "
                "retry count from two to three to improve a customer-visible error rate.",
            ],
            "lines": [
                "C = 1, λ = 0.90, base = 0.05",
                "",
                "r = 2",
                "step 1  L = 0.90  ≤ C  so p = 0.05",
                "        attempts = 1 + 0.05 + 0.0025 = 1.0525",
                "        L′ = 0.90 × 1.0525 = 0.94725",
                "step 2  L = 0.94725 ≤ C  so p = 0.05 again",
                "        L′ = 0.94725 → unchanged, this is the fixed point",
                "fixed point 0.94725,  below capacity,  stable",
                "",
                "r = 3",
                "step 1  attempts = 1 + 0.05 + 0.0025 + 0.000125 = 1.052625",
                "        L′ = 0.90 × 1.052625 = 0.9473625",
                "fixed point 0.9473625,  below capacity,  stable",
                "",
                "now the same two policies at λ = 0.98",
                "r = 2   fixed point 1.38247    above capacity",
                "r = 3   fixed point 1.63311    above capacity",
            ],
            "after": [
                "At ninety per cent offered load the extra retry is nearly free: the "
                "fixed point moves by one part in ten thousand and stays well inside "
                "capacity, because the load never crosses `C` and so the failure rate "
                "never leaves its base value. The feedback term is switched off entirely "
                "in this regime, which is why the policy looks harmless.",
                "At ninety-eight per cent the same two policies both storm, and the one "
                "with the extra retry storms harder. The decision therefore is not about "
                "the retry count at all &mdash; it is about how close to capacity the "
                "service is allowed to run, because that is what decides whether the "
                "loop is engaged.",
                "For a faded rehearsal, keep `base = 0.05` and `r = 2` and find the "
                "offered load at which the fixed point first exceeds capacity. The "
                "supplied first move is that while `L ≤ C` the map has the constant "
                "amplification `1.0525`, so the loop only engages once "
                "`λ × 1.0525 > 1`. Solve that inequality by hand, then check the value "
                "against the lab's bracket by stepping the offered-load slider across it.",
            ],
        },
        "quiz_title": "Loops and fixed points",
        "quiz": [
            {"q": "Offered load is `0.95` of capacity, the base failure rate is `10%` and there are three retries. What is the load after one application of the map?",
             "a": ["`0.95`, unchanged, since the load is below capacity",
                   "`1.05545`",
                   "`3.80`, the offered load times `r + 1`",
                   "`1.00`, because the service saturates at capacity"],
             "c": 1,
             "why": "Below capacity the failure rate is the base `0.10`, so the "
                    "amplification is `1 + 0.1 + 0.01 + 0.001 = 1.111`, and "
                    "`0.95 × 1.111 = 1.05545`. The retries apply at the base failure "
                    "rate too &mdash; they are not switched off below capacity, which is "
                    "precisely how the first step crosses it. The third choice is the "
                    "ceiling as `p` approaches one."},
            {"q": "In this model, what makes a retry storm self-sustaining?",
             "a": ["The original trigger persists, so the load stays high",
                   "The failure rate rises with load and the amplification rises with the failure rate, so the retries supply their own cause",
                   "Clients retry forever, with no bound on the attempt count",
                   "Capacity falls during overload, which is a separate mechanism"],
             "c": 1,
             "why": "The loop closes on itself: load raises `p`, `p` raises the "
                    "amplification, the amplification raises the load. At `λ = 0.95` the "
                    "offered load was always serviceable, so there is no persisting "
                    "external trigger to point at. The attempt count is bounded at "
                    "`r + 1` and the storm happens anyway &mdash; the ceiling "
                    "`λ(r + 1)` is `3.80` of capacity, and the fixed point at `1.727` "
                    "sits well under it."},
            {"q": "At `base = 0.10` and `r = 3`, offered loads of `0.80`, `0.90` and `0.95` settle at `0.8888`, `0.9999` and `1.727`. What does that say about the transition?",
             "a": ["It is linear in the offered load",
                   "It is abrupt: a five-point rise in offered load moves the fixed point from just inside capacity to 73% over it",
                   "It is an artefact of exact fractions and would not appear in a real system",
                   "The system is unstable at every load, and the three figures are transients"],
             "c": 1,
             "why": "`0.90` settles at `0.9999`, one part in ten thousand under capacity, "
                    "and `0.95` settles at `1.727`. The map is smooth but the margin "
                    "between the amplified load and capacity is what determines whether "
                    "the feedback term engages at all, so the outcome changes character "
                    "over a very small range. All three figures are fixed points, not "
                    "transients: the map returns them unchanged."},
        ],
        "mistakes": [
            ("Believing the retries stop when the service recovers",
             "They are what prevents it recovering. At `λ = 0.95` with three retries the "
             "fixed point is `1.727` of capacity and the failure rate there is `47.9%` "
             "&mdash; a failure rate the retries themselves are sustaining. Removing the "
             "original trigger changes nothing, because the offered load was never the "
             "problem; switching the retries off returns the load to `0.95` at once."),
            ("Sizing capacity against the offered load rather than the fixed point",
             "`0.95` of capacity is the load a capacity plan would record. What arrives "
             "is `1.727` of capacity, and the ceiling `λ(r + 1)` is `3.80`. A headroom "
               "figure that does not include the amplification is measuring traffic the "
             "system does not actually receive on the day it matters."),
            ("Iterating the exact map to find the fixed point",
             "Each step raises the failure rate to the `(r + 1)`-th power, so the "
             "denominators cube: five digits, thirteen, thirty-nine, a hundred and "
             "nineteen. The seventh iterate has over three thousand, and rounding to "
             "carry on is how a diverging iteration gets reported as a converging one. "
             "Bracket the root instead &mdash; the map is increasing and bounded, so a "
             "sign change traps it."),
        ],
        "standard": ("Finish when you would ask for a system's fixed point rather than its offered load.",
                     "You should be able to state the failure model, apply the map by "
                     "hand for three steps, bracket the fixed point between `λ` and "
                     "`λ(r + 1)`, and say how much of the resulting load is the system's "
                     "own doing rather than its users'."),
        "note": 'The loop is closed by two different mechanisms and they are not alternatives. Spreading the retries in time is one, and &ldquo;Backoff and Jitter&rdquo; shows that the spreading, not the delay, is what actually cuts the peak. Refusing work at the door is the other, and that is &ldquo;Load Shedding&rdquo;.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "backoff-and-jitter",
        "title": "Backoff and Jitter",
        "module": "Containing the load",
        "one_line": "Count retries per second after an outage, from one seed, with jitter and without.",
        "summary": (
            "Exponential backoff decays the retry rate geometrically, which fixes the "
            "total. It does nothing at all to the peak: every client that failed at the "
            "same instant schedules its first retry at the same millisecond, so the "
            "retries arrive in waves at 1, 2, 4, 8, 16 and 32 seconds. Adding jitter to "
            "the delay spreads the same retries over the interval, and at 600 clients it "
            "cuts the peak from 3000 a second to 925 without changing the policy."
        ),
        "key": [
            "delay of attempt i = base × 2ⁱ⁻¹      waves at 1, 2, 4, 8, 16, 32 s",
            "with jitter w:  delay ~ Uniform[d(1 − w/2), d(1 + w/2))",
            "600 clients, no jitter:  peak 3000 /s      with 100% jitter:  925 /s",
            "a factor of 3.24 off the peak, from the same seed and the same total",
        ],
        "key_label": "Backoff fixes the total; only jitter fixes the peak",
        "concepts_intro": (
            "Two properties of a retry schedule that are usually named together and are "
            "controlled by different parts of it."
        ),
        "concepts": [
            ("An outage synchronises every client",
             "An outage is, by definition, a moment at which all of a service's clients "
             "fail at once. Each then schedules retry `i` at `base × 2ⁱ⁻¹` after its own "
             "failure, and since the failures were simultaneous the retries are too: the "
             "first wave at one second, the next at two, then four, eight, sixteen and "
             "thirty-two. Doubling a constant leaves it constant."),
            ("Backoff controls the total, not the peak",
             "Geometric delays mean a client makes six attempts in forty seconds rather "
             "than forty, which is a real reduction in total work. But all six of those "
             "attempts land in six instants, so the instantaneous rate at each instant is "
             "the full client population. The peak is what decides whether a recovering "
             "service stays up, and backoff alone does not touch it."),
            ("Jitter is the part that spreads them",
             "Drawing the delay uniformly from `[d(1 − w/2), d(1 + w/2))` turns each "
             "wave into a smear over an interval proportional to the delay. With 600 "
             "clients, a one-second base and full-width jitter the peak falls from 3000 "
             "retries a second to 925 &mdash; a factor of `3.24` &mdash; with the same "
               "clients, the same policy and the same seed. Nothing was delayed longer "
             "on average; it was spread."),
        ],
        "read_title": "Waves, and the one parameter that flattens them",
        "read_intro": (
            "What a synchronised retry schedule looks like, why the measurement resolution "
            "matters, and what jitter costs."
        ),
        "body": [
            ("def", ("Exponential backoff and jitter",
                     "Under <strong>exponential backoff</strong> the delay before attempt "
                     "`i` is `base × 2ⁱ⁻¹`. Under <strong>jitter</strong> of width `w` "
                     "the delay is instead drawn uniformly from "
                     "`[d(1 − w/2), d(1 + w/2))`, where `d` is that same nominal delay. "
                     "Jitter of `100%` therefore spreads attempt `i` uniformly over an "
                     "interval of length `d` centred on `d`.")),
            ("p", "The lab draws its delays from a seeded linear congruential generator "
                  "&mdash; multiplier `1 103 515 245`, increment `12 345`, modulus "
                  "`2³¹` &mdash; so the histogram is the same every time the page is "
                  "opened and a reader can check what they were told. Change the seed "
                  "and the peak moves a little; change the jitter and it moves a lot."),
            ("math", [
                "600 clients, 20-second outage, base 1000 ms, 8 attempts allowed",
                "",
                "retries per second, no jitter",
                "second     0   1   2   3   4   5   6   7   8   9  …  16  …  32",
                "count      0 600 600   0 600   0   0   0 600   0  … 600  … 600",
                "",
                "six waves of 600 = 3600 retries in total",
                "peak, measured in 200 ms slots:  600 per slot = 3000 /s",
            ]),
            ("p", "The slot width is the whole measurement and the lab says so on its "
                  "face. Without jitter every client in a wave retries in the same "
                  "millisecond, so the true instantaneous spike is six hundred requests "
                  "in one millisecond; any bucket wider than that understates it. At the "
                  "200 ms resolution the lab uses, the reported `3000` a second is a "
                  "floor rather than a measurement."),
            ("h3", "The same clients, spread"),
            ("math", [
                "the same run with 100% jitter, seed 7",
                "",
                "peak, no jitter        3000 /s",
                "peak, with jitter       925 /s        a factor of 3.24",
                "",
                "total, no jitter       3600 retries",
                "total, with jitter     3323 retries",
                "",
                "retries per second, with jitter",
                "second     0   1   2   3   4   5   6   7   8   9  10  11",
                "count    298 603 438 161 233 225  81  76 122  99 100 109",
            ]),
            ("p", "Two things changed and they are worth separating. The peak fell by a "
                  "factor of `3.24`, which is what jitter is for. The total fell slightly "
                  "too, from `3600` to `3323`, which is an artefact of the outage "
                  "boundary: a jittered attempt that lands after the service has "
                  "recovered succeeds and the client stops, where its unjittered twin "
                  "would have retried once more. Jitter is not a way to reduce total "
                  "load; the small change here is a side effect."),
            ("example", ("What the recovering service sees",
                         "A service coming back after a twenty-second outage has a first "
                         "second in which it is either hit by 3000 requests or by about "
                         "900, depending on a single configuration parameter. If its "
                         "capacity is 1500 a second, the first case fails again "
                         "immediately &mdash; and every client that fails re-enters the "
                         "backoff schedule, which is the previous lesson's loop with a "
                         "synchronised phase. The second case is served.")),
            ("h3", "What jitter costs, and what full width means"),
            ("p", "Jitter does not increase the mean delay: the interval "
                  "`[d(1 − w/2), d(1 + w/2))` is centred on `d`, so half the draws are "
                  "earlier than the nominal delay and half later. What it costs is "
                  "predictability &mdash; a particular client may retry sooner or later "
                  "than the schedule says &mdash; and that is almost never a cost anyone "
                  "is actually paying."),
            ("p", "Full-width jitter, `w = 100%`, spreads attempt `i` over "
                  "`[0.5d, 1.5d)`. Half-width leaves the waves partly visible: at `50%` "
                  "the same run peaks at `1240` a second rather than `925`, because each "
                  "wave is smeared over half the interval and neighbouring waves no "
                  "longer overlap enough to fill the gaps. The lab's jitter slider makes "
                  "that comparison directly."),
            ("example", ("The cap that matters more than the base",
                         "Backoff without a cap reaches a 32-second delay by the sixth "
                         "attempt and 512 seconds by the tenth, which is long enough that "
                         "the client has effectively given up without saying so. Real "
                         "policies cap the delay, and a capped backoff with jitter is "
                         "the standard shape: exponential up to a ceiling, then uniform "
                         "on a jittered interval around that ceiling. The waves this "
                         "lesson is about are a property of the early attempts, which is "
                         "exactly where the cap does not apply.")),
        ],
        "lab": ("avail", {
            "mode": "backoff",
            "clients": 600,
            "outage_seconds": 20,
            "base_ms": 1000,
            "jitter_pct": 100,
            "seed": 7,
            "panel_title": "Set the outage and the policy",
            "panel_intro": "600 clients failing together, a one-second base and a "
                           "twenty-second outage. The upper histogram is the policy "
                           "without jitter and the lower one is the same clients, the "
                           "same seed and the same policy with it. Take the jitter to "
                           "zero and watch the lower panel become the upper one.",
        }),
        "steps_title": "Designing a retry schedule for a synchronised failure",
        "steps_intro": (
            "The third step is the one that is usually skipped, and skipping it makes the "
            "policy look better than it is by whatever factor the bucket is too wide."
        ),
        "steps": [
            ("Assume every client fails at the same instant",
             "That is what an outage is, and it is the case the schedule has to survive. "
             "A policy evaluated against independent, uniformly distributed failures is "
             "being evaluated against the case it was never needed for."),
            ("Write down where the waves land",
             "`base × 2ⁱ⁻¹` for each attempt, until the delay exceeds the outage or the "
             "attempt budget runs out: 1, 2, 4, 8, 16, 32 seconds at a one-second base. "
             "Each of those instants receives the entire client population."),
            ("Measure the peak at a resolution finer than the wave",
             "A one-second bucket turns six hundred simultaneous retries into a "
             "comfortable-looking six hundred a second. Use a slot narrow enough to "
             "resolve the spike, and report the slot width alongside the peak, because "
             "without jitter the true spike is instantaneous and every bucket "
             "understates it."),
            ("Add jitter and compare peaks, not totals",
             "The total barely moves; the peak falls by roughly the factor the spreading "
             "achieves &mdash; `3.24` here at full width. Compare the jittered peak with "
             "the capacity the service has while it is recovering, which is generally "
             "less than its steady-state capacity."),
        ],
        "worked": {
            "title": "A thundering herd at 2000 clients, and the capacity it needs",
            "intro": [
                "A service with 2000 clients and a recovery capacity of 1200 requests a "
                "second comes back from a thirty-second outage. The question is whether "
                "it survives its own clients, and the answer is a comparison of two "
                "numbers.",
            ],
            "lines": [
                "2000 clients, base 1000 ms, 30-second outage, recovery capacity 1200 /s",
                "",
                "no jitter: the waves",
                "1 s, 2 s, 4 s, 8 s, 16 s, 32 s   six waves of 2000 = 12 000 retries",
                "each wave lands inside one millisecond",
                "peak at 200 ms resolution = 2000 per slot = 10 000 /s",
                "10 000 /s against 1200 /s of capacity        the service fails again",
                "",
                "and what failing again does",
                "every one of the 2000 clients re-enters the schedule",
                "the next wave is the same size, one doubling later",
                "",
                "with 100% jitter, seed 7, the same 2000 clients",
                "total   11 597 retries      against 12 000 without",
                "peak     3075 /s            against 10 000 without",
                "                            a factor of 3.25 off the spike",
                "",
                "3075 /s against the 1200 /s the service has while recovering",
            ],
            "after": [
                "Jitter cut the peak by a factor of `3.25` and the result is still nearly "
                "three times what the service can serve, because spreading 2000 clients "
                "over roughly a second is still thousands a second. This is the honest result: "
                "jitter is necessary and it is not sufficient, and the remaining gap has "
                "to be closed somewhere else &mdash; a larger base delay, a retry budget "
                "that lets only a fraction of clients retry at all, or refusing the "
                "excess at the door.",
                "Note which number the design has to be compared against. Recovery "
                "capacity is lower than steady-state capacity: caches are cold, "
                "connection pools are empty and the first requests after an outage are "
                "the expensive ones. Sizing the first wave against the steady-state "
                "figure is how a service that should have survived does not.",
                "For a faded rehearsal, keep the 2000 clients and the 1200 per second, "
                "and find the backoff base at which the jittered peak first fits inside "
                "capacity. The supplied first move is that full-width jitter spreads "
                "wave one over an interval about as long as the base, so the peak falls "
                "roughly as `clients/base` &mdash; which is a lower bound, because later "
                "waves overlap the first. Estimate the base from that, then find the "
                "true answer in the lab by stepping the base slider and reading the "
                "jittered peak, and say how far your estimate was out.",
            ],
        },
        "quiz_title": "Waves and spreading",
        "quiz": [
            {"q": "Six hundred clients fail at the same instant and retry with a one-second exponential backoff and no jitter. When do the retries arrive?",
             "a": ["Spread evenly over the first minute",
                   "In waves at 1, 2, 4, 8, 16 and 32 seconds, each of 600 retries",
                   "All at one second, since backoff only applies after the second attempt",
                   "At random times, because clients are never perfectly synchronised"],
             "c": 1,
             "why": "Each client computes `base × 2ⁱ⁻¹` from its own failure time, and "
                    "the failure times are identical, so the delays are too. Doubling a "
                    "constant keeps it constant, which is why backoff alone cannot "
                    "desynchronise anything. The last option is the assumption that makes "
                    "people skip jitter; the clients are synchronised by the outage "
                    "itself, which is the event under discussion."},
            {"q": "Adding full-width jitter to that policy cuts the measured peak from 3000 a second to 925. What happened to the total number of retries?",
             "a": ["It fell by the same factor of 3.24",
                   "It fell slightly, from 3600 to 3323, and only because some jittered attempts land after the service recovers",
                   "It rose, since jitter adds extra attempts",
                   "It was unchanged at 3600, exactly"],
             "c": 1,
             "why": "Jitter redistributes attempts in time; it does not remove them. The "
                    "small drop in the total is an edge effect at the recovery boundary: "
                    "an attempt jittered past the twenty-second mark succeeds and the "
                    "client stops, where its unjittered twin would have made one more. "
                    "The peak is what jitter is for, and it fell by `3.24`."},
            {"q": "A retry peak is reported as &ldquo;600 a second&rdquo;, measured in one-second buckets, for a policy with no jitter. What is wrong with that figure?",
             "a": ["Nothing; a one-second bucket is the natural unit for a rate",
                   "Without jitter the whole wave lands in one millisecond, so a one-second bucket understates the spike by up to a thousandfold",
                   "It should have been divided by the number of clients",
                   "It is too high, because not every client retries"],
             "c": 1,
             "why": "The bucket must be narrower than the event being measured. Six "
                    "hundred simultaneous retries inside a one-second bucket read as a "
                    "comfortable `600` a second, and the service experiences six hundred "
                    "requests at once. Reporting the slot width alongside the peak, as "
                    "the lab does at 200 ms, is what stops the measurement flattering the "
                    "policy."},
        ],
        "mistakes": [
            ("Using backoff without jitter",
             "Backoff bounds the total attempts and leaves the peak exactly where it "
             "was, because every client doubles the same constant. The service that has "
             "just come back is then hit by its entire client population in one "
             "millisecond, fails, and sends all of them into the next wave. Jitter is "
             "not an optimisation of backoff; it is the half of the policy that "
             "addresses the peak."),
            ("Measuring the peak in buckets wider than the wave",
             "An unjittered wave is instantaneous. A one-second bucket divides it by a "
             "thousand and reports a rate the service never experienced, which makes a "
             "dangerous policy look safe in exactly the graph that would have caught it. "
             "Report the resolution with the number, and treat any peak measured without "
             "jitter as a lower bound."),
            ("Judging jitter by the total instead of the peak",
             "The totals here are `3600` and `3323`, a difference of under eight per "
             "cent, and the peaks are `3000` and `925`. A comparison made on totals "
             "concludes that jitter barely matters. The quantity that decides whether a "
               "recovering service survives is the instantaneous rate, and that is the "
             "one jitter moves."),
        ],
        "standard": ("Finish when “we use exponential backoff” prompts you to ask about the jitter width.",
                     "You should be able to say where the waves of an unjittered schedule "
                     "land, measure a peak at a resolution that resolves them, predict "
                     "the effect of jitter on the peak and on the total separately, and "
                     "compare a first wave against a recovering service's capacity "
                     "rather than its steady-state one."),
        "note": 'Backoff and jitter make the clients behave. The service can also defend itself, and the arithmetic for that is a comparison of two goodput curves rather than a histogram. &ldquo;Load Shedding&rdquo; computes what a system delivers when it refuses work at the door against what it delivers when it accepts everything, and the second is worse in a way that surprises people.',
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "load-shedding-and-circuit-breakers",
        "title": "Load Shedding",
        "module": "Containing the load",
        "one_line": "Compute goodput under a shedding threshold and compare it with goodput under collapse.",
        "summary": (
            "Above capacity a server spreads its work across more requests than it can "
            "finish inside a client's patience, so the share that completes is `C/L` and "
            "the goodput is `C × (C/L)` &mdash; it falls as the load rises. Refusing the "
            "excess at the door replaces that curve with a flat line at the threshold. At "
            "twice capacity, shedding delivers 900 requests a second against 500, so "
            "rejecting 55% of the traffic serves 1.8 times as many users as accepting all "
            "of it."
        ),
        "key": [
            "no shedding:  goodput = C × (C/L) for L > C,  and L below it",
            "shedding:     admit min(L, T), then the same model  →  flat at T",
            "C = 1000, L = 2000, T = 900:   900 /s shed against 500 /s unshed",
            "rejected 1100 /s = 55.0% of offered,  and 1.80 × the goodput",
        ],
        "key_label": "One service model, two admission policies",
        "concepts_intro": (
            "The collapse is not an assumption about pathological systems; it follows from "
            "one sentence about what happens to work spent on a request nobody is waiting "
            "for any more."
        ),
        "concepts": [
            ("Work spent on an abandoned request is work lost",
             "Above capacity the server still does `C` units of work a second, but it is "
             "spread across `L` requests and only the share `C/L` of them finish before "
             "the client gives up. The useful output is therefore `C × (C/L) = C²/L`, "
             "which falls as `L` rises. At twice capacity a thousand-per-second service "
             "delivers five hundred; at four times capacity, two hundred and fifty."),
            ("Shedding is admission control, not a second service model",
             "A shedder admits `min(L, T)` and puts that through exactly the same model. "
             "Below the threshold nothing changes; above it the admitted load is capped "
             "and the goodput is flat at `T`, provided `T` is at or below capacity. A "
             "threshold set above capacity collapses too, more slowly, which is why the "
             "threshold is chosen relative to the knee rather than to the load."),
            ("Rejecting requests is how availability is defended",
             "At twice capacity, refusing `55%` of the traffic outright serves `900` "
             "requests a second where accepting everything serves `500`. The rejected "
               "requests cost almost nothing &mdash; a fast error is cheap &mdash; and "
             "the accepted ones are the ones the server can finish. More users get an "
             "answer under the policy that says no."),
        ],
        "read_title": "Goodput under collapse, and goodput under a threshold",
        "read_intro": (
            "The model, both curves, where the threshold belongs, and what a circuit "
            "breaker is doing when it is the client that refuses."
        ),
        "body": [
            ("def", ("Goodput, and the overload model",
                     "<strong>Goodput</strong> is the rate of requests that are both "
                     "served and still wanted. With capacity `C` and offered load `L`, "
                     "this lesson's model is: for `L ≤ C` the goodput is `L`; for "
                     "`L > C` the server's capacity is spread across `L` requests, only "
                     "`C/L` of them complete within the client's patience, and the "
                     "goodput is `C × (C/L)`. A <strong>shedder</strong> with threshold "
                     "`T` admits `min(L, T)` and passes it through the same model.")),
            ("p", "The model is this lesson's own and it is stated so that it can be "
                  "argued with. The mechanism behind it &mdash; a queue that fills, work "
                  "spent on entries whose clients have already left, and an admitted rate "
                  "that is not the completed rate &mdash; is the subject of Queues and "
                  "Utilisation's &ldquo;Bounded Queues and Loss&rdquo;, and the knee that "
                  "makes the threshold choice non-obvious is &ldquo;The Knee: Response "
                  "Time vs Utilisation&rdquo;."),
            ("math", [
                "C = 1000 rps,  threshold T = 900 rps",
                "",
                "offered   load   goodput shedding   goodput not shedding   ratio",
                "  50%       500        500.0                500.0          1.00",
                "  90%       900        900.0                900.0          1.00",
                " 100%      1000        900.0               1000.0          0.90",
                " 150%      1500        900.0                666.7          1.35",
                " 200%      2000        900.0                500.0          1.80",
                " 300%      3000        900.0                333.3          2.70",
                " 400%      4000        900.0                250.0          3.60",
            ]),
            ("p", "Two features of the table decide everything. The shedder costs "
                  "goodput at exactly one point &mdash; between the threshold and "
                  "capacity, where it is refusing work the server could have done "
                  "&mdash; and that cost is bounded by `C − T`, here a hundred requests "
                  "a second. Everywhere above capacity it wins, and the margin grows "
                  "without limit as the load rises."),
            ("h3", "Where to put the threshold"),
            ("p", "The cost of a threshold below capacity is `C − T` at full load; the "
                  "benefit is that the system never enters the collapsing regime. Since "
                  "response time is already rising steeply as utilisation approaches one, "
                  "the threshold is normally placed a little under capacity &mdash; "
                  "`0.9C` here &mdash; and the ten per cent is bought as insurance "
                  "against the estimate of `C` being wrong."),
            ("example", ("A threshold above capacity still collapses",
                         "Set the threshold to `120%` of capacity and offer `200%`. The "
                         "shedder admits `1200` requests a second, which the server "
                         "cannot serve, so the goodput is `1000²/1200 = 833.3` a second "
                         "&mdash; better than the `500` of no shedding and worse than the "
                         "`900` of a threshold at `90%`. The shedder is not a magic "
                         "boundary; it is a cap, and a cap above capacity caps nothing "
                         "that matters.")),
            ("h3", "Utilisation is the quantity being defended"),
            ("p", "With the shedder the utilisation is `admitted/C = 0.9`; without it, "
                  "`offered/C = 2.0`. A utilisation above one is not a state a system "
                  "occupies, it is a description of a queue growing without bound, and "
                  "every second spent there adds latency that never comes back. The "
                  "shedder's real product is that `0.9`."),
            ("example", ("The circuit breaker, from the other end",
                         "A circuit breaker is the same arithmetic with the client doing "
                         "the refusing. After a threshold number of failures the client "
                         "stops calling for a cooling period and fails fast locally, "
                         "which removes its share of `L` at the source rather than at the "
                         "server's door. The advantage over server-side shedding is that "
                         "the rejected request never crosses the network; the "
                         "disadvantage is that the client is deciding on stale local "
                         "evidence about a service it has stopped observing.")),
            ("p", "Both mechanisms are about the same quantity and neither of them makes "
                  "the offered load smaller. The requests that are shed still failed from "
                  "the user's point of view &mdash; the argument is not that rejection is "
                  "free, it is that rejection is cheap and collapse is not, so a fixed "
                  "amount of failure buys far more successes when it is taken at the "
                  "door."),
            ("example", ("Why this is not a loss of availability",
                         "At `200%` offered load the unshed service succeeds on `500` of "
                         "`2000` requests a second, a success ratio of `25%`. The shed "
                         "service succeeds on `900` of `2000`, a ratio of `45%`, while "
                         "explicitly rejecting `1100`. By the error-budget measurement of "
                         "&ldquo;Error Budgets&rdquo;, which counts failed requests, the "
                         "shedder spends less budget &mdash; `1100` rejections against "
                         "`1500` timeouts a second &mdash; and the rejections are "
                         "returned immediately rather than after a timeout.")),
        ],
        "lab": ("avail", {
            "mode": "shed",
            "capacity_rps": 1000,
            "offered_pct": 200,
            "threshold_pct": 90,
            "panel_title": "Set the load and the shedding threshold",
            "panel_intro": "A thousand requests a second of capacity, twice that offered, "
                           "and a threshold at ninety per cent. The green curve is flat "
                           "above the threshold and the red one turns over at capacity "
                           "and falls. Find the one region where the green curve is below "
                           "the red one, and read off how wide it is.",
        }),
        "steps_title": "Choosing and checking a shedding threshold",
        "steps_intro": (
            "The first step is the hard one, because the threshold is expressed relative to "
            "a capacity that has to be measured rather than assumed."
        ),
        "steps": [
            ("Measure capacity as the rate at which latency turns up",
             "Not the rate at which the service falls over: the knee, where response time "
             "begins rising steeply, is the capacity this model means. A figure taken "
             "from the maximum throughput ever observed is already inside the collapsing "
             "regime and will put the threshold in the wrong place."),
            ("Put the threshold a little below it",
             "`T` slightly under `C` &mdash; ninety per cent is a common choice. The cost "
             "is `C − T` of goodput at full load and the benefit is that an error in the "
             "capacity estimate, or a slow drift in request cost, does not push the "
             "system over the edge before the shedder engages."),
            ("Compute both goodput curves at the loads you expect",
             "`min(L, T)` through the model for the shedder, `C²/L` above capacity for "
             "the collapse. Compare them at the peak load you plan for and at two or "
             "three times it, because the ratio is what justifies the threshold and it "
             "grows with the overload."),
            ("Make the rejection cheap and say so to the client",
             "A shed request must cost the server almost nothing and must be "
             "distinguishable by the client from a timeout, so that the client can back "
             "off rather than retry immediately. A rejection that is expensive to "
             "produce, or that looks like a failure worth retrying at once, feeds the "
             "loop rather than breaking it."),
        ],
        "worked": {
            "title": "A service at three times capacity: what shedding is worth",
            "intro": [
                "A service with a measured knee at 1200 requests a second meets a promotion "
                "that offers 3600. The question is what each policy delivers and what it "
                "costs in failed requests.",
            ],
            "lines": [
                "C = 1200 rps,  L = 3600 rps  (300% of capacity),  T = 0.9C = 1080 rps",
                "",
                "no shedding",
                "goodput = C²/L = 1200²/3600 = 1 440 000/3600 = 400 /s",
                "failed  = 3600 − 400 = 3200 /s, all of them after a timeout",
                "utilisation = 3600/1200 = 3.00",
                "",
                "shedding at 1080",
                "admitted = 1080 /s   (below C, so all of it completes)",
                "goodput  = 1080 /s",
                "rejected = 3600 − 1080 = 2520 /s, refused immediately",
                "failed   = 2520 /s",
                "utilisation = 1080/1200 = 0.90",
                "",
                "the comparison",
                "goodput   1080 against 400          2.70 ×",
                "failures  2520 against 3200         680 /s fewer",
                "and the 2520 are refused in microseconds, not after a timeout",
            ],
            "after": [
                "Shedding wins on both columns at once, which is the part that surprises "
                "people: it serves nearly three times as many users and produces fewer "
                "failures, because the failures it produces are cheap and the ones it "
                "avoids were consuming capacity on their way to failing anyway. The "
                "utilisation of `0.90` against `3.00` is the same fact stated as a queue "
                "property.",
                "The cost is visible only in a narrow band. Between `1080` and `1200` "
                "requests a second the shedder refuses work the server could have done, "
                "up to `120` requests a second at the top of that band. That is the whole "
                "price of the policy, and it is paid in a region the system passes "
                "through rather than sits in.",
                "For a faded rehearsal, the team proposes raising the threshold to `1200` "
                "&mdash; exactly capacity &mdash; to recover that band. The supplied "
                "first move is that the goodput at `T = C` is still `C` as long as the "
                "capacity estimate is exact. Work out what the goodput becomes if the "
                "true capacity turns out to be `1100` rather than `1200`, under both "
                "thresholds, and say what that says about where the ten per cent was "
                "actually going.",
            ],
        },
        "quiz_title": "Goodput and thresholds",
        "quiz": [
            {"q": "Capacity is 1000 requests a second and 2000 are offered, with no shedding. What is the goodput under this lesson's model?",
             "a": ["`1000` a second, since the server works at capacity",
                   "`500` a second",
                   "`2000` a second, with high latency",
                   "`0`, because the system has collapsed"],
             "c": 1,
             "why": "The server does `C` units of work a second, spread across `L` "
                    "requests, so the share completing in time is `C/L = 0.5` and the "
                    "goodput is `C × (C/L) = 1000²/2000 = 500`. The first option is the "
                    "common intuition &mdash; that a saturated server still delivers its "
                    "capacity &mdash; and it ignores that half the work went to requests "
                    "whose clients had already given up."},
            {"q": "The same service sheds everything above 900 a second. What does it deliver, and how much does it reject?",
             "a": ["`900` a second delivered, `1100` rejected &mdash; `1.80` times the unshed goodput",
                   "`900` delivered, `100` rejected",
                   "`500` delivered, `1500` rejected",
                   "`1000` delivered, `1000` rejected"],
             "c": 0,
             "why": "It admits `min(2000, 900) = 900`, which is under capacity and "
                    "therefore all completes, and refuses the other `1100` &mdash; "
                    "`55.0%` of the offered load. `900` against `500` is a ratio of "
                    "`1.80`. The second option rejects only the excess over capacity "
                    "rather than over the threshold."},
            {"q": "A team sets the shedding threshold to 120% of capacity, reasoning that it should only refuse work the server genuinely cannot do. At 200% offered load, what happens?",
             "a": ["Goodput is 900 a second, as with any threshold",
                   "Goodput is `833.3` a second: better than no shedding, worse than a threshold below capacity",
                   "Goodput is 1200 a second, since that is what is admitted",
                   "Nothing is shed, since the threshold is above capacity"],
             "c": 1,
             "why": "The shedder admits `1200` a second, which exceeds capacity, so the "
                    "admitted load goes through the collapse model: `1000²/1200 = 833.3`. "
                    "A cap above capacity caps nothing that matters. The reasoning in the "
                    "question sounds careful and gets the comparison backwards &mdash; "
                    "the threshold exists to keep utilisation under one, not to ration "
                    "work the server could theoretically start."},
        ],
        "mistakes": [
            ("Believing that rejecting requests lowers availability",
             "At twice capacity the shedding service answers `900` requests a second and "
             "the accepting one answers `500`. Measured as a success ratio that is `45%` "
               "against `25%`, and the shed failures are immediate rather than "
             "timeouts. Refusal is how the successes are protected; accepting everything "
             "is what converts capacity into work nobody is waiting for."),
            ("Setting the threshold from the maximum throughput ever observed",
             "That figure is taken inside the collapsing regime and is higher than the "
             "knee, so a threshold based on it admits load the system cannot serve and "
             "the shedder never engages until the collapse is already under way. Measure "
             "the knee &mdash; where latency turns up &mdash; and set the threshold "
             "below it."),
            ("Rejecting expensively, or indistinguishably from a timeout",
             "A rejection that costs the server real work is just another request, and a "
             "rejection the client cannot tell from a transient failure is retried "
             "immediately, which returns the load at once. The policy depends on the "
             "refusal being cheap for the server and legible to the client, and both of "
             "those are implementation properties rather than arithmetic ones."),
        ],
        "standard": ("Finish when “we reject 55% of requests” reads as a defence of availability rather than an admission of failure.",
                     "You should be able to compute goodput under both policies, identify "
                     "the narrow band where shedding costs something, place a threshold "
                     "relative to a measured knee rather than to a maximum, and say why "
                     "the shedding arm produces both more successes and fewer failures at "
                     "high overload."),
        "note": 'The course has been about requests up to here. The last two lessons are about sets of machines rather than about one request, and they ask two questions that redundancy cannot answer on its own: how likely is it that every copy of a piece of data is gone at once, and how much of a fleet does a single bad machine take with it. &ldquo;Replica Loss and Durability&rdquo; is the first, and it is the one lesson on the course whose headline figure is not exact.',
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "replica-loss-and-durability",
        "title": "Replica Loss and Durability",
        "module": "Fleets",
        "one_line": "Estimate the annual probability of losing every copy of an item, and what halving the repair window is worth.",
        "summary": (
            "Losing data needs all `N` copies gone inside one repair window, so to first "
            "order the annual probability per placement group is "
            "`N! × fᴺ × (R/8760)ᴺ⁻¹`: at three copies, a two per cent annual failure rate "
            "and a 24-hour window, `3.603 × 10⁻¹⁰`. The repair window appears `N − 1` "
            "times, so halving it divides the risk by `2ᴺ⁻¹` rather than by two. This is "
            "the one figure on the course that is rounded, and what is approximate is the "
            "model rather than the arithmetic."
        ),
        "key": [
            "P(lose an item in a year)  ≈  N! × fᴺ × (R/8760)ᴺ⁻¹",
            "N = 3, f = 2%/year, R = 24 h   →   3.603 × 10⁻¹⁰ per group",
            "halving R divides by 2ᴺ⁻¹ = 4, not by 2       R appears N − 1 times",
            "first-order: every term with overlapping failures is dropped",
        ],
        "key_label": "A rare-event estimate, and the exponent that does the work",
        "concepts_intro": (
            "Durability is a race between failures and repairs, and the shape of the answer "
            "comes from which of those two quantities appears how many times."
        ),
        "concepts": [
            ("Losing data needs N failures inside one window",
             "One copy failing is routine and costs nothing: the system notices and "
               "rebuilds it. Data is lost only when the remaining `N − 1` copies also "
             "fail before the rebuild finishes. To first order the first copy fails at "
             "rate `N f` a year and each further one must follow inside `R`, giving "
             "`N! × fᴺ × (R/8760)ᴺ⁻¹` as the annual probability per group."),
            ("The repair window carries the exponent N − 1",
             "`f` appears `N` times and `R` appears `N − 1` times, so at three copies the "
             "risk is quadratic in the repair window: halving `R` divides the probability "
             "by four, not by two, and at four copies by eight. The rebuild rate is "
             "therefore a lever of the same order as the failure rate, and it is usually "
             "the one an operator can actually move."),
            ("Three copies is not three times the durability",
             "At `f = 2%` and `R = 24` h, two copies give `2.192 × 10⁻⁶` a year and three "
             "give `3.603 × 10⁻¹⁰` &mdash; a factor of about six thousand, not a factor "
             "of one and a half. Each copy multiplies the probability by `f` and by "
             "`R/8760`, both of which are small, so the improvement is exponential in `N` "
             "and the intuition of proportionality is wrong by orders of magnitude."),
        ],
        "read_title": "A race between failure and repair, to first order",
        "read_intro": (
            "Where the formula comes from, what it drops, why the dropped part is small "
            "here, and what the resulting number is and is not a statement about."
        ),
        "body": [
            ("def", ("Durability, and the first-order loss estimate",
                     "Consider a <strong>placement group</strong> holding `N` copies of "
                     "an item, each on a device that fails independently at rate `f` a "
                     "year, with a lost copy rebuilt within a <strong>repair "
                     "window</strong> of `R` hours. The annual probability of losing the "
                     "item is approximately `N! × fᴺ × (R/8760)ᴺ⁻¹`. This is a "
                     "<strong>first-order rare-event estimate</strong>: it drops every "
                     "term in which failures overlap or a repair completes mid-window.")),
            ("p", "The shape is easier to see than the constant. Any one of the `N` "
                  "copies can fail first, at rate `f` each; the second must fail inside "
                  "the window, which happens with probability about `f × R/8760`; the "
                  "third likewise. Multiplying and counting the orderings gives the "
                  "factorial, the `N`-th power of `f` and the `(N − 1)`-th power of the "
                  "window fraction."),
            ("math", [
                "N = 3,  f = 0.02 a year,  R = 24 h,  8760 h in a year",
                "",
                "R/8760 = 24/8760 = 0.00273973",
                "",
                "P ≈ 3! × 0.02³ × 0.00273973²",
                "  = 6 × 0.000008 × 0.0000075061",
                "  = 3.603 × 10⁻¹⁰ per group per year",
                "",
                "the same first-order formula as an exact fraction",
                "  = 3/8 326 562 500",
                "",
                "across 10 000 placement groups",
                "  3.603 × 10⁻⁶ losses a year, one every 2.776 × 10⁵ years",
            ]),
            ("p", "The exact fraction is printed beside the float deliberately. The "
                  "arithmetic on rational `f` and `R` is exact and the two agree, which "
                  "is how you can tell that the gap between this number and the truth is "
                  "in the modelling rather than in the division. Every other figure on "
                  "this course is exact; this one is rounded, and what rounds is the "
                  "first-order truncation."),
            ("h3", "How big the truncation is"),
            ("p", "The estimate stands in for an exponential: the probability that a "
                  "further copy fails within the window is `1 − e⁻ˣ` with "
                  "`x = (N − 1) f R/8760`, and the formula uses `x` itself. Here "
                  "`x = 1.095890 × 10⁻⁴` and `1 − e⁻ˣ = 1.095830 × 10⁻⁴`, a relative gap "
                  "of `0.0055%`. The truncation is negligible in this regime and would "
                  "not be if `f` or `R` were large, which is the condition under which "
                  "the formula may be used at all."),
            ("example", ("What halving the repair window is worth",
                         "Cutting `R` from 24 hours to 12 takes the annual loss "
                         "probability from `3.603 × 10⁻¹⁰` to `9.007 × 10⁻¹¹`, a factor "
                         "of `2ᴺ⁻¹ = 4`. At four copies the same halving is a factor of "
                         "eight. Rebuild speed is not a second-order concern that gets "
                         "attention after the replica count is settled; at three copies "
                         "it is exactly as powerful as reducing the device failure rate "
                         "by the same factor, twice over.")),
            ("h3", "What the number is a statement about"),
            ("p", "It is a per-group, per-year probability under a model in which "
                  "devices fail independently at a constant rate and rebuilds always "
                  "finish inside `R`. Multiply it by the number of groups to get an "
                  "expected count for the fleet &mdash; `3.603 × 10⁻⁶` a year across ten "
                  "thousand groups &mdash; and invert that for a mean time between "
                  "losses. Those conversions are arithmetic; the model underneath them is "
                  "the part that can be wrong."),
            ("p", "And it usually is wrong in one specific direction. Independence is the "
                  "assumption of &ldquo;Correlated Failure&rdquo;, and it fails here for "
                  "the reasons it fails everywhere: three copies in one rack, on one "
                  "power feed, in one firmware version, or written by one buggy release. "
                  "The eleven-figure durability numbers quoted for storage systems are "
                  "answers about device failure, and device failure is rarely what loses "
                  "data."),
            ("example", ("Where the real losses come from",
                         "A three-copy system at `3.603 × 10⁻¹⁰` per group per year would "
                         "lose an item roughly once every `2.776 × 10⁵` years across ten "
                         "thousand groups. Operators do not observe that; they observe "
                         "losses from deletion bugs, from a bad deploy that corrupts all "
                         "three copies identically, from an operator command applied "
                         "fleet-wide, and from a rebuild that silently did not happen. "
                         "None of those are in the model, and all of them are correlated "
                         "&mdash; which is why backups with a different failure domain "
                         "exist alongside replication rather than instead of it.")),
            ("p", "One consequence worth naming: the model says a rebuild that does not "
                  "finish is not a slow repair, it is an infinite `R`. A group whose "
                  "rebuild is stalled has left the regime the formula describes entirely, "
                  "and the durability figure computed for the fleet does not apply to it. "
                  "Monitoring under-replicated groups is therefore not an operational "
                  "nicety; it is the condition under which the arithmetic is true."),
        ],
        "lab": ("avail", {
            "mode": "durability",
            "copies": 3,
            "rate_per_1000": 20,
            "window_hours": 24,
            "groups": 10000,
            "panel_title": "Set the copies, the failure rate and the repair window",
            "panel_intro": "Three copies, a two per cent annual device failure rate and a "
                           "24-hour repair window. The float and the exact fraction of the "
                           "same first-order formula print side by side and agree; the "
                           "footer measures the truncation itself, by comparing the "
                           "first-order term with the exponential it stands in for.",
        }),
        "steps_title": "Estimating durability",
        "steps_intro": (
            "The arithmetic is four multiplications. The first and the last steps are what "
            "decide whether the answer means anything."
        ),
        "steps": [
            ("Check that the rare-event regime applies",
             "The formula needs `f R/8760` to be small &mdash; here `5.5 × 10⁻⁵`. If the "
             "failure rate is high or the repair window is long, the truncated terms stop "
             "being negligible and the estimate overstates the risk, mildly, in a way "
             "that is no longer worth the simplicity."),
            ("Put the window and the rate in the same units",
             "`f` per year, `R` in hours, `8760` hours in the year. Express the window as "
             "the fraction `R/8760` before raising it to a power; a window in minutes "
             "raised to the power `N − 1` is wrong by a factor of `3600` at three copies."),
            ("Multiply, and keep the exponent in view",
             "`N! × fᴺ × (R/8760)ᴺ⁻¹`. Write the two exponents down: `f` appears `N` "
             "times and `R` appears `N − 1` times. That asymmetry is the result, and it "
             "is what makes rebuild speed comparable in power to device quality."),
            ("Report it as an estimate under an independence assumption",
             "Say that the figure is first-order, say what the truncation is worth, and "
             "say that it assumes independent device failures. A durability figure quoted "
             "to eleven significant figures with no assumption attached is a number about "
             "a fleet that does not exist."),
        ],
        "worked": {
            "title": "Two copies or three, and a rebuild that takes a week",
            "intro": [
                "A team is choosing between two and three copies, and separately has a "
                "rebuild window of seven days because the devices are large and the "
                "network is not. Both decisions are in the same formula and only one of "
                "them is being discussed.",
            ],
            "lines": [
                "f = 0.02 a year,  10 000 placement groups",
                "",
                "N = 2, R = 24 h",
                "P ≈ 2! × 0.02² × (24/8760)¹ = 2 × 0.0004 × 0.00273973",
                "  = 2.192 × 10⁻⁶ per group per year",
                "fleet: 2.192 × 10⁻² losses a year, one every 45.6 years",
                "",
                "N = 3, R = 24 h",
                "P ≈ 3! × 0.02³ × (24/8760)² = 3.603 × 10⁻¹⁰",
                "fleet: 3.603 × 10⁻⁶ a year, one every 2.776 × 10⁵ years",
                "",
                "the third copy is worth a factor of 6083",
                "",
                "N = 3, R = 168 h  (one week)",
                "P ≈ 3! × 0.02³ × (168/8760)² = 1.765 × 10⁻⁸",
                "",
                "so a week-long rebuild costs a factor of 49 = 7²",
                "and the third copy at R = 168 h is still far better than",
                "two copies at R = 24 h",
            ],
            "after": [
                "Both levers are in view now and they are not the same size. The third "
                "copy buys a factor of about six thousand; the rebuild window, from a "
                "week to a day, buys forty-nine. Neither is negligible and the second is "
                "usually far cheaper, because it is a network and scheduling problem "
                "rather than a third of the storage bill.",
                "The exponent is doing all of the work in the second comparison: `168/24` "
                "is seven, and seven squared is forty-nine because `R` appears `N − 1 = 2` "
                "times. At four copies the same change would cost a factor of "
                "`7³ = 343`, which is why systems that run wide erasure codes care about "
                "rebuild bandwidth to a degree that looks obsessive from outside.",
                "For a faded rehearsal, keep three copies and a 24-hour window and "
                "suppose the device failure rate is revised upward from `2%` to `5%`. The "
                "supplied first move is that `f` appears `N = 3` times, so the change is "
                "a factor of `(5/2)³`. Compute the new per-group probability and the "
                "fleet expectation, then find the repair window that would restore the "
                "original figure &mdash; and check both in the lab.",
            ],
        },
        "quiz_title": "Copies, windows and orders of magnitude",
        "quiz": [
            {"q": "Three copies, a `2%` annual device failure rate and a 24-hour repair window. The repair window is halved to 12 hours. By what factor does the annual loss probability fall?",
             "a": ["By two, in proportion to the window", "By four", "By eight", "It is unchanged; the window affects speed, not durability"],
             "c": 1,
             "why": "`R` appears `N − 1 = 2` times in `N! fᴺ (R/8760)ᴺ⁻¹`, so halving it "
                    "divides by `2² = 4`: `3.603 × 10⁻¹⁰` becomes `9.007 × 10⁻¹¹`. "
                    "&ldquo;By eight&rdquo; would be right at four copies, where the "
                    "exponent is three. The first option is the proportional intuition "
                    "the exponent contradicts."},
            {"q": "&ldquo;Three copies gives three times the durability of one.&rdquo; What is wrong with this?",
             "a": ["Nothing; durability is linear in the number of copies",
                   "The improvement is exponential in `N`: two copies give `2.192 × 10⁻⁶` a year and three give `3.603 × 10⁻¹⁰`, a factor of about 6000",
                   "It understates it; three copies give nine times the durability",
                   "It is unanswerable without knowing the read quorum"],
             "c": 1,
             "why": "Each extra copy multiplies the loss probability by roughly `f` and by "
                    "`R/8760`, both small, so the risk falls by orders of magnitude per "
                    "copy rather than by a constant multiple. The third option replaces a "
                    "linear intuition with a quadratic one and is wrong by about three "
                    "orders of magnitude. The read quorum is a question about "
                    "availability, not about whether the data still exists."},
            {"q": "A storage system publishes a durability of eleven nines, computed from device failure rates. What does that figure not account for?",
             "a": ["Nothing significant; device failure is the dominant loss mode",
                   "Correlated losses &mdash; a bad deploy, a deletion bug, a fleet-wide command, a stalled rebuild &mdash; none of which are in the model",
                   "The cost of the storage, which is a separate calculation",
                   "Read availability during a rebuild"],
             "c": 1,
             "why": "The model assumes independent device failures at a constant rate "
                    "with rebuilds that always complete inside `R`. Every common real "
                    "cause of data loss violates one of those: a deploy that corrupts all "
                    "three copies identically is one event, not three, and a stalled "
                    "rebuild is an infinite `R` rather than a slow one. The eleven nines "
                    "are an honest answer to a question that is not the one being asked."},
        ],
        "mistakes": [
            ("Reading durability as proportional to the copy count",
             "&ldquo;Three copies means three times the durability&rdquo; is wrong by "
             "about three orders of magnitude: two copies give `2.192 × 10⁻⁶` a year and "
             "three give `3.603 × 10⁻¹⁰`. Each copy contributes a factor of `f` and a "
             "factor of `R/8760`, so the scale is exponential in `N` and no linear "
             "intuition survives contact with it."),
            ("Treating the repair window as an operational detail",
             "`R` appears `N − 1` times, so at three copies it is quadratic: a week-long "
             "rebuild instead of a day-long one is a factor of `49` in the loss "
             "probability. Rebuild bandwidth is a durability parameter of the same order "
             "as device quality, and it is normally the cheaper of the two to change."),
            ("Quoting the figure without the model it came from",
             "The number is first-order, it assumes independent constant-rate device "
             "failures, and it assumes every rebuild finishes inside `R`. Published to "
             "eleven significant figures with none of that attached, it invites a "
             "comparison with observed losses that it cannot survive &mdash; because the "
             "observed losses are the correlated ones the model does not contain."),
        ],
        "standard": ("Finish when a durability figure prompts you to ask about the rebuild window before the copy count.",
                     "You should be able to evaluate `N! fᴺ (R/8760)ᴺ⁻¹`, say why halving "
                     "`R` divides the risk by `2ᴺ⁻¹`, state what the first-order "
                     "truncation drops and roughly what it is worth, and name the "
                     "correlated loss modes that sit entirely outside the model."),
        "note": 'Durability asks whether every copy of one item is gone. The last question of the course is the other half of the same picture: when one machine fails, how much of the fleet notices. &ldquo;Blast Radius and Shuffle Sharding&rdquo; answers it with exact combinatorics, and the result is that overlap between two tenants is common while a full collision &mdash; the only kind that takes them both down &mdash; is rare by a factor you can count.',
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "shuffle-sharding",
        "title": "Blast Radius and Shuffle Sharding",
        "module": "Fleets",
        "one_line": "Count the overlap between two randomly drawn shards and separate degradation from outage.",
        "summary": (
            "Give each tenant `k` of your `n` nodes, drawn at random. Two tenants share no "
            "node at all with probability `C(n−k, k)/C(n, k)` and hold the identical set "
            "with probability `1/C(n, k)` &mdash; and only the identical set means one "
            "tenant's bad request can take the other down. At `n = 16` and `k = 2` those "
            "are `91/120` and `1/120`, and one failed node degrades `1/8` of tenants "
            "while taking down none of them."
        ),
        "key": [
            "C(n, k) distinct shards            n = 16, k = 2  →  120",
            "P(share no node)   = C(n−k, k)/C(n, k) = 91/120 = 75.833%",
            "P(identical set)   = 1/C(n, k)         =  1/120 =  0.8333%",
            "one bad node degrades k/n = 1/8 of tenants and takes down none",
        ],
        "key_label": "Two binomial coefficients, and the difference between them",
        "concepts_intro": (
            "The whole lesson is a hypergeometric distribution over how many nodes two "
            "tenants have in common, and the two ends of it are the ones that matter."
        ),
        "concepts": [
            ("Overlap has a distribution, and you can count it",
             "A tenant holds `k` of `n` nodes. A second tenant, drawn independently and "
             "uniformly, shares exactly `j` of them with probability "
             "`C(k,j)·C(n−k, k−j)/C(n,k)`. Summing over `j` gives one, which is the "
             "cheapest check on the arithmetic. At `n = 16`, `k = 2` the three outcomes "
             "are `91/120`, `7/30` and `1/120` for zero, one and two shared nodes."),
            ("Only the identical set is an outage for both",
             "A tenant that shares one of your two nodes has lost half its capacity and "
             "still has the other half; it is degraded, not down. A tenant holding "
             "exactly your set has nowhere to go. So the number that matters is "
             "`1/C(n,k) = 1/120`, not the `23.3%` chance of some overlap &mdash; and "
             "those two differ by a factor of twenty-eight at this setting."),
            ("Blast radius is k/n, and it is degradation",
             "A single bad node is used by the `k/n` of tenants whose shard includes it "
             "&mdash; `1/8` at `n = 16, k = 2`. Every one of them loses one node out of "
             "`k` and keeps the rest. Without shuffle sharding, a fleet split into "
             "`n/k` fixed shards would give the same node `k/n` of the tenants as a full "
             "outage, which is the same fraction with an entirely different consequence."),
        ],
        "read_title": "Counting shards, overlaps and what each one costs",
        "read_intro": (
            "Where the two probabilities come from, why overlap is not collision, and how "
            "the numbers move when the shard size does."
        ),
        "body": [
            ("def", ("Shuffle sharding",
                     "Under <strong>shuffle sharding</strong> each tenant is assigned a "
                     "random `k`-subset of the `n` nodes, drawn independently per tenant, "
                     "rather than being placed in one of `n/k` fixed shards. There are "
                     "`C(n,k)` distinct assignments. Two tenants <strong>overlap</strong> "
                     "in `j` nodes with probability `C(k,j)·C(n−k, k−j)/C(n,k)`; they are "
                     "<strong>disjoint</strong> when `j = 0` and <strong>identical</strong> "
                     "when `j = k`.")),
            ("p", "The counting is direct. Fix the first tenant's `k` nodes. The second "
                  "tenant's set is one of the `C(n,k)` equally likely subsets, and the "
                  "ones sharing exactly `j` nodes are formed by choosing `j` from the "
                  "first tenant's `k` and the remaining `k − j` from the `n − k` nodes it "
                  "does not hold. That is the hypergeometric distribution, and nothing "
                  "about it is approximate."),
            ("math", [
                "n = 16, k = 2.     C(16,2) = 120 distinct shards",
                "",
                "j   ways                          probability      meaning",
                "0   C(2,0)·C(14,2) = 91           91/120  75.8333%  untouched",
                "1   C(2,1)·C(14,1) = 28            7/30   23.3333%  degraded, 1 of 2 left",
                "2   C(2,2)·C(14,0) =  1            1/120   0.8333%  down with you",
                "                     ───                   ────────",
                "                     120                   100%",
            ]),
            ("p", "Read the third row against the second. Nearly a quarter of tenants "
                  "share a node with you, and one in a hundred and twenty shares both. "
                  "Sharing nothing is `91` times likelier than sharing everything, and "
                  "that ratio is the entire argument for drawing shards at random rather "
                  "than assigning them in blocks."),
            ("h3", "Why overlap is not collision"),
            ("p", "Suppose a tenant sends a request that makes a node unusable &mdash; a "
                  "poison pill, a query that exhausts memory, a pattern that triggers a "
                  "bug. Every tenant sharing that node is affected. But a tenant that "
                  "shares one of your two nodes still has one working node and, if the "
                  "client retries elsewhere, still has a service. Only a tenant whose "
                  "entire set is inside the damage has nothing left."),
            ("example", ("One bad node, sixteen nodes, two per tenant",
                         "The node fails or is poisoned. `k/n = 1/8` of tenants use it, "
                         "so one in eight is degraded to a single remaining node. None "
                         "is down, because no tenant's shard is a subset of a "
                         "single-node failure when `k = 2`. Compare a fixed-shard layout "
                         "of eight shards of two: the same node takes out one shard "
                         "entirely, and every tenant in it &mdash; `1/8` of the fleet "
                         "&mdash; is fully down.")),
            ("h3", "What raising k does"),
            ("p", "Raising `k` cuts the collision probability hard, because `C(n,k)` "
                  "grows quickly, while raising the blast radius `k/n` of each individual "
                  "node. At `n = 24` and `k = 4` there are `10 626` distinct shards, so "
                  "two tenants collide with probability `1/10 626` &mdash; `0.0094%` "
                  "&mdash; and `45.596%` share nothing. The cost is that one bad node now "
                  "touches `1/6` of tenants rather than `1/8`, each of them losing one "
                  "node of four."),
            ("math", [
                "n = 24, k = 4.     C(24,4) = 10 626 distinct shards",
                "",
                "P(share no node)  = C(20,4)/C(24,4) = 4845/10 626 = 45.596%",
                "P(identical set)  =        1/10 626              =  0.0094%",
                "one bad node degrades k/n = 1/6 of tenants",
                "",
                "against n = 16, k = 2:  1/120 = 0.8333%, blast 1/8",
            ]),
            ("p", "Two levers and they pull in opposite directions, which is the design "
                  "question this lesson leaves you with. More nodes per tenant means "
                  "fewer tenants can take you down with them and more tenants feel each "
                  "individual failure, at a lower severity each. The lab computes both "
                  "columns for whatever `n` and `k` you set."),
            ("example", ("Reading the drawn assignment",
                         "The lab draws a sample assignment from a seed and marks each "
                         "tenant with the number of your nodes it shares. At `n = 16`, "
                         "`k = 2` and twelve tenants, the expected number holding your "
                         "exact set is `11/120 ≈ 0.0917`, so a draw in which none does is "
                         "the ordinary outcome. Raise the tenant count and the seed and "
                         "watch how rarely a red row appears &mdash; that rarity is the "
                         "`1/120`, made visible.")),
            ("p", "One boundary. At `k = 1` the distinction this lesson turns on "
                  "disappears: a tenant on one node is degraded and down by the same "
                  "event, and the collision probability is `1/n`, which is simply the "
                  "chance of landing on the same node. Shuffle sharding needs `k ≥ 2` to "
                  "mean anything, and the client has to be able to use the surviving "
                  "nodes &mdash; if a request is pinned to one node of the `k`, the "
                  "arithmetic on this page is describing a system you do not have."),
        ],
        "lab": ("avail", {
            "mode": "shuffle",
            "nodes": 16,
            "per_tenant": 2,
            "tenants": 12,
            "seed": 3,
            "panel_title": "Set the fleet and the shard size",
            "panel_intro": "Sixteen nodes, two per tenant, twelve tenants drawn from a "
                           "seed. The table lists every overlap outcome with its exact "
                           "probability and says what each one means for the other "
                           "tenant; the grid beneath it is a drawn assignment you can "
                           "count by eye. Take `k` to 4 and `n` to 24 and watch the "
                           "collision probability fall by two orders of magnitude.",
        }),
        "steps_title": "Sizing a shuffle-sharded fleet",
        "steps_intro": (
            "Two coefficients answer the question, and the third and fourth steps are where "
            "the answer either applies to your system or does not."
        ),
        "steps": [
            ("Compute C(n,k), and read it as the number of distinct shards",
             "That integer is the headline: `C(16,2) = 120`, `C(24,4) = 10 626`. The "
             "probability that two tenants hold the identical set is its reciprocal, so "
             "the whole design is an argument about how large you can make a binomial "
             "coefficient at acceptable cost."),
            ("Separate the two probabilities, and check the terms sum to one",
             "`C(n−k,k)/C(n,k)` for sharing nothing, `1/C(n,k)` for sharing everything, "
             "and the hypergeometric terms in between. Summing all `k + 1` of them must "
             "give exactly one; if it does not, a coefficient is wrong."),
            ("Decide what a partial overlap actually costs you",
             "The arithmetic says a tenant sharing `j < k` nodes keeps `k − j` of them. "
             "Whether that is a working service depends on whether your client retries "
             "on another node and whether one node can carry the tenant's load. If "
             "either answer is no, partial overlap is an outage and the `1/C(n,k)` "
             "figure is not the one to quote."),
            ("Trade k against the blast radius deliberately",
             "Raising `k` shrinks `1/C(n,k)` fast and raises `k/n`, so more tenants feel "
             "each failure at lower severity. Pick the point on that trade rather than "
             "inheriting it, and state both numbers when you do &mdash; a collision "
             "probability quoted without the blast radius has reported one half of the "
             "design."),
        ],
        "worked": {
            "title": "Thirty-two nodes, four per tenant, a thousand tenants",
            "intro": [
                "A realistic sizing question. One tenant is capable of making a node "
                "unusable, and the operator wants to know how many other tenants go down "
                "with it and how many merely notice.",
            ],
            "lines": [
                "n = 32, k = 4,  1000 tenants",
                "",
                "C(32,4) = 35 960 distinct shards",
                "",
                "P(share no node) = C(28,4)/C(32,4) = 20 475/35 960 = 56.94%",
                "P(identical set) = 1/35 960                        = 0.00278%",
                "",
                "the poisoned tenant takes down another tenant only if that tenant",
                "holds its exact four nodes",
                "expected fully-down tenants = 999 × 1/35 960 = 0.0278",
                "",
                "and the degradation",
                "each of the 4 nodes is used by k/n = 1/8 of tenants",
                "tenants touching at least one of the 4 = 1 − 20 475/35 960 = 43.06%",
                "expected degraded tenants = 999 × 0.4306 ≈ 430",
                "",
                "so: about 430 tenants notice, and 0.03 tenants are down",
            ],
            "after": [
                "Both numbers are needed and they say opposite-sounding things. Nearly "
                "half the fleet is touched, which sounds alarming until the severity is "
                "attached: each of those tenants has lost one node of four and keeps "
                "three. The number of tenants that lose everything is `0.0278` in "
                "expectation &mdash; about one occurrence in thirty-six such events.",
                "Compare the fixed-shard alternative at the same `k`: eight shards of "
                "four, each holding `125` tenants. The poisoned tenant takes its entire "
                "shard down, so `125` tenants are fully out and `875` are untouched. "
                "Shuffle sharding converts one hundred and twenty-five outages into four "
                "hundred and thirty degradations and a rounding error, which is the "
                "trade in one sentence.",
                "For a faded rehearsal, the operator proposes `n = 32, k = 2` instead, to "
                "halve the per-tenant footprint. The supplied first move is that "
                "`C(32,2) = 496`, so the collision probability rises by a factor of "
                "`35 960/496`. Compute the expected fully-down tenants and the expected "
                "degraded tenants under that setting, check both in the lab, and say "
                "which of the two columns you would be willing to trade.",
            ],
        },
        "quiz_title": "Overlaps and blast radius",
        "quiz": [
            {"q": "Sixteen nodes, two per tenant, drawn at random. What is the probability that two tenants share no node at all?",
             "a": ["`1/120`", "`91/120`", "`7/30`", "`1/8`"],
             "c": 1,
             "why": "The second tenant must take both its nodes from the `14` your tenant "
                    "does not hold: `C(14,2)/C(16,2) = 91/120`, or `75.833%`. `1/120` is "
                    "the identical-set probability, `7/30` is exactly one node in common, "
                    "and `1/8` is `k/n`, the blast radius of a single node."},
            {"q": "A tenant sends a request that makes one of its two nodes unusable. Another tenant shares that node but not the other. What has happened to it?",
             "a": ["It is down, since one of its nodes is gone",
                   "It is degraded: it has lost one node of two and still has the other",
                   "It is untouched, because the damage is confined to the first tenant",
                   "It is down, but only if it retries"],
             "c": 1,
             "why": "Overlap is not collision. Losing `j` of `k` nodes leaves `k − j`, and "
                    "only `j = k` leaves nothing &mdash; which happens with probability "
                    "`1/C(n,k) = 1/120` here. The qualification in the last option "
                    "reverses the mechanism: retrying is what converts the degradation "
                    "into a served request, so a client that retries elsewhere is the "
                    "condition under which this arithmetic holds at all."},
            {"q": "Moving from `n = 16, k = 2` to `n = 24, k = 4` changes two numbers. Which description is right?",
             "a": ["Collisions become far rarer, `1/120` to `1/10 626`, and each bad node touches more tenants, `1/8` to `1/6`",
                   "Both the collision probability and the blast radius fall",
                   "Both rise, since there are more nodes and more assignments",
                   "Neither changes, since `k/n` is what matters and it is nearly the same"],
             "c": 0,
             "why": "`C(24,4) = 10 626` against `C(16,2) = 120`, so a full collision is "
                    "about ninety times rarer; and `k/n` rises from `1/8` to `1/6`, so "
                    "each failed node is felt by a sixth of tenants rather than an eighth "
                    "&mdash; each of them losing one node of four rather than one of two, "
                    "which is a milder degradation. The two levers pull in opposite "
                    "directions, which is the design trade."},
        ],
        "mistakes": [
            ("Treating any overlap as a shared outage",
             "At `n = 16, k = 2`, `23.3%` of tenants share exactly one node with you and "
             "`0.8333%` share both. Quoting the first figure as the risk overstates it by "
             "a factor of twenty-eight, and it also hides the design's entire point, "
             "which is that partial overlap leaves a working remainder. The number to "
             "quote is `1/C(n,k)`, with the degradation figure beside it."),
            ("Quoting a collision probability without the blast radius",
             "`1/C(n,k)` falls as `k` rises and `k/n` rises with it. A design justified "
             "only by the first number has chosen to make each individual node failure "
             "felt by more tenants without saying so. Both figures are properties of the "
             "same choice and belong in the same sentence."),
            ("Assuming the client can use the surviving nodes",
             "Every probability here counts nodes, not service. If a tenant's requests "
             "are pinned to one node of its `k`, or if one node cannot carry the tenant's "
             "load alone, then losing `j` of `k` is an outage rather than a degradation "
             "and the arithmetic on this page is describing a system you do not have. "
             "Shuffle sharding is a placement scheme plus a client that retries."),
        ],
        "standard": ("Finish when you would answer “how bad is one bad node” with two numbers rather than one.",
                     "You should be able to compute `C(n,k)`, the disjoint and identical "
                     "probabilities and the hypergeometric terms between them, check that "
                     "they sum to one, separate degradation from outage, and state the "
                     "collision probability and the blast radius together as the two "
                     "halves of one design choice."),
        "note": 'That closes the course. Availability is a fraction; chains multiply it down and redundant paths multiply it up, but only under an independence assumption that &ldquo;Correlated Failure&rdquo; exists to break; retries multiply load at the worst possible moment; and durability and blast radius are the two questions that are about a fleet rather than a request. The next course takes the replicas this one merely counted and asks whether they agree with one another, which turns out to be a different kind of arithmetic entirely.',
    },
]
