"""Course 4, lessons 06-10 - staleness, the stampede, writes, two levels, and bytes."""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "ttl-and-staleness",
        "title": "TTL and Staleness",
        "module": "Where caches fail",
        "one_line": "Compute the fraction of reads that see a stale value for a chosen TTL, and the miss rate that shortening it costs.",
        "summary": (
            "A TTL is a staleness budget, and the budget has a price. With updates every "
            "`U` seconds and a TTL of `T`, the expected fraction of time the cached copy "
            "is out of date is piecewise in `T` &mdash; `T/(2U)` below the update "
            "interval and `1 − U/(2T)` above it. Halving `T` halves the staleness and "
            "doubles the misses, and the second half of that sentence is the one that "
            "gets left out."
        ),
        "key": [
            "stale fraction     T/(2U)        for T ≤ U",
            "                   1 − U/(2T)    for T ≥ U      both give 1/2 at T = U",
            "",
            "miss rate = 1/(λ_key·T)          one miss per key per TTL",
            "",
            "U = 60 s, T = 10 s, 5 reads/s:   stale 1/12 = 8.33%,  miss 1/50 = 2.00%",
        ],
        "key_label": "A piecewise staleness, and the misses a short TTL buys",
        "concepts_intro": (
            "A model with two branches and two assumptions. The branches are easy; the "
            "assumptions are the reason the lab runs a timeline beside the formula."
        ),
        "concepts": [
            ("A TTL does not keep data fresh — it bounds how stale it gets",
             "A cached copy written at time `0` and held for `T` seconds is correct "
             "until the source changes and wrong from then until the window ends. The "
             "TTL never prevents that; it caps its duration at `T`. &ldquo;We cache for "
             "sixty seconds&rdquo; and &ldquo;we serve data up to sixty seconds "
             "wrong&rdquo; are the same sentence."),
            ("The stale fraction is piecewise in `T`",
             "With updates every `U` and a uniform refresh phase, the expected stale "
             "fraction is `T/(2U)` while `T ≤ U` and `1 − U/(2T)` once `T ≥ U`. The two "
             "branches agree at `T = U`, where both give `1/2`. Below the update "
             "interval staleness is linear in the TTL; above it, it climbs toward `1` "
             "and never reaches it."),
            ("A shorter TTL is bought with misses",
             "A key read `λ_key` times a second and expiring every `T` seconds misses "
             "once per window, so its miss rate is `1/(λ_key·T)` &mdash; and `1` once "
             "the TTL is shorter than the gap between reads. At five reads a second and "
             "`T = 10 s` that is `1/50 = 2.00%`. Halve `T` and it becomes `1/25 = 4.00%`: "
             "half the staleness, twice the backend traffic."),
        ],
        "read_title": "The staleness a TTL admits, and the misses a short one costs",
        "read_intro": "Where the piecewise formula comes from, what it assumes, and why the lab runs a timeline next to it.",
        "body": [
            ("def", ("TTL and staleness",
                     "A cache entry written at time `t` with a "
                     "<strong>time to live</strong> `T` is served until `t + T` and then "
                     "discarded. If the underlying value changes at some time inside "
                     "that window, the entry is <strong>stale</strong> from the change "
                     "until the window ends. The <strong>stale fraction</strong> is the "
                     "expected proportion of the window during which the entry is "
                     "stale.",
                     "This is a staleness measured in time, not in reads. Weighting by "
                     "reads gives the same answer when reads are spread evenly through "
                     "the window, which is the case this lesson computes.")),
            ("p", "Two assumptions make the formula possible and both are visible on the "
                  "page rather than buried. The first is that updates are "
                  "<strong>periodic</strong>, every `U` seconds. The second is that the "
                  "<strong>phase</strong> between the refresh clock and the update clock "
                  "is uniform &mdash; the refresh lands at a time unrelated to the "
                  "updates. Neither is true of a real system, and the lab lets you fix "
                  "the phase and watch a single run disagree with the average."),
            ("h3", "Where the two branches come from"),
            ("p", "Let `G` be the time from the start of a refresh window to the next "
                  "update, uniform on `[0, U)`. The entry is fresh until that update and "
                  "stale for the remainder of the window, so the stale time is "
                  "`max(0, T − G)` &mdash; the piecewise function of Algebra, and the "
                  "expected value of Discrete Mathematics applied to it."),
            ("math", [
                "stale time in one window = max(0, T − G),    G uniform on [0, U)",
                "",
                "T ≤ U:   E[max(0, T − G)] = T²/(2U)",
                "         fraction = T²/(2U) ÷ T  =  T/(2U)",
                "",
                "T ≥ U:   an update always lands in the window, so stale time = T − G",
                "         E = T − U/2,  fraction = 1 − U/(2T)",
                "",
                "at T = U both give 1/2",
            ]),
            ("example", ("A one-minute update, a ten-second TTL",
                         "`U = 60 s`, `T = 10 s`. Since `T ≤ U` the stale fraction is "
                         "`T/(2U) = 10/120 = 1/12 = 8.33%`. Stretch the TTL to `30 s` "
                         "and it becomes `1/4 = 25.00%`; to `60 s` and it is "
                         "`1/2 = 50.00%`; to `120 s` and the other branch gives "
                         "`3/4 = 75.00%`. A TTL twice the update interval means three "
                         "quarters of the time you are serving something wrong.")),
            ("h3", "What the other direction costs"),
            ("p", "So shorten the TTL. Staleness falls linearly &mdash; and every key "
                  "now expires more often, so it misses more often. A key read `λ_key` "
                  "times a second expires once every `T` seconds, and exactly one of the "
                  "`λ_key·T` reads in that window pays for the refill, giving a miss "
                  "rate of `1/(λ_key·T)`. Once `λ_key·T ≤ 1` the key expires between "
                  "reads and every read is a miss."),
            ("example", ("The trade, at five reads a second",
                         "`λ_key = 5`. At `T = 10 s` the stale fraction is `1/12` and "
                         "the miss rate `1/50 = 2.00%`. At `T = 1 s` the stale fraction "
                         "falls to `1/120 = 0.83%` and the miss rate rises to "
                         "`1/5 = 20.00%` &mdash; a tenth of the staleness for ten times "
                         "the backend reads. At `T = 240 s` the stale fraction is "
                         "`7/8 = 87.50%` and the miss rate is `1/1200 = 0.08%`.")),
            ("p", "Both ends of that trade are a choice about what the system is for. A "
                  "price display can be a minute wrong and must not melt the pricing "
                  "service; a permission check can be nothing wrong and is read rarely "
                  "enough that a short TTL costs little. The formula does not decide; it "
                  "prices both options in the same units so the decision is not made by "
                  "whoever spoke last."),
            ("h3", "Why the lab runs a timeline beside the formula"),
            ("p", "`T/(2U)` is an expectation over the phase, not a prediction about a "
                  "particular run. Fix the phase at `30%` of `U` with `U = 60 s` and "
                  "`T = 10 s` and the run actually measures `1/30 = 3.33%` stale against "
                  "a formula that says `1/12 = 8.33%`; averaged over twenty-four phases "
                  "it lands back on `8.33%` exactly. Neither number is wrong. They "
                  "answer different questions."),
            ("p", "That is the honest way to use this: as a sensitivity rather than a "
                  "forecast. It tells you that doubling the TTL roughly doubles the "
                  "staleness while `T ≤ U`, and that is a shape you can rely on even "
                  "when the update process is not periodic at all. What it will not give "
                  "you is the stale fraction your system had last Tuesday, and a model "
                  "whose assumptions are on the page is one you can tell that about."),
        ],
        "lab": ("cache", {
            "mode": "ttl",
            "update": 60,
            "ttl": 10,
            "lam_key": 5,
            "phase_pct": 30,
        }),
        "steps_title": "Pricing a TTL",
        "steps_intro": "Both numbers, always. A TTL argument with only one of them in it is an argument about nothing.",
        "steps": [
            ("Find the update interval `U`",
             "How often does the underlying value actually change? Not how often it could "
             "&mdash; how often it does. If the answer is &ldquo;rarely, and then "
             "suddenly&rdquo;, the periodic model is the wrong one and the TTL should be "
             "paired with explicit invalidation."),
            ("Pick the branch and compute the stale fraction",
             "`T ≤ U` gives `T/(2U)`; `T ≥ U` gives `1 − U/(2T)`. Check the branch "
             "before substituting: at `T = 2U` the wrong branch gives `1` and the right "
             "one gives `3/4`, and the error is invisible in the answer."),
            ("Compute the miss rate the TTL implies",
             "`1/(λ_key·T)`, for the per-key read rate. This is the number that turns a "
             "staleness decision into a capacity decision, and it is the one that gets "
             "omitted."),
            ("State both, and say what the formula assumes",
             "&ldquo;A ten-second TTL means about eight per cent of reads see data up to "
             "ten seconds old, and two per cent of reads reach the database, assuming "
             "the value changes about once a minute.&rdquo; Every clause in that "
             "sentence is load-bearing."),
        ],
        "worked": {
            "title": "U = 60 s, T = 10 s, 5 reads a second",
            "intro": [
                "One branch check, one substitution, one division &mdash; and then the "
                "same key at four other TTLs, because the point is the shape."
            ],
            "lines": [
                "U = 60 s (the value changes once a minute),  λ_key = 5 reads/s",
                "",
                "T = 10 s.   T ≤ U, so the branch is T/(2U):",
                "    stale = 10/(2·60) = 10/120 = 1/12 = 8.33%",
                "    miss  = 1/(λ_key·T) = 1/(5·10) = 1/50 = 2.00%",
                "",
                "the same key at other TTLs:",
                "     T        branch         stale            miss rate",
                "     1 s      T/(2U)         1/120 =  0.83%    1/5    = 20.00%",
                "    15 s      T/(2U)         1/8   = 12.50%    1/75   =  1.33%",
                "    30 s      T/(2U)         1/4   = 25.00%    1/150  =  0.67%",
                "    60 s      T/(2U)         1/2   = 50.00%    1/300  =  0.33%",
                "   120 s      1 − U/(2T)     3/4   = 75.00%    1/600  =  0.17%",
                "   240 s      1 − U/(2T)     7/8   = 87.50%    1/1200 =  0.08%",
                "",
                "10 s → 1 s:   staleness ÷ 10,   backend reads × 10",
            ],
            "after": [
                "The last line is the lesson. Every factor of ten you take off the "
                "staleness you put back on the backend, exactly, and there is no TTL at "
                "which both numbers are small unless the key is read very often "
                "relative to how often it changes.",
                "For a faded rehearsal, take a key that changes every `10 s` and is read "
                "`200` times a second. The supplied first move is that a `60 s` TTL is "
                "past the update interval, so the branch is `1 − U/(2T)`; compute the "
                "stale fraction and the miss rate there, then find a TTL whose stale "
                "fraction is under `10%` and say what its miss rate is. Report which of "
                "the two numbers this key can afford.",
                "In the lab, set the phase control to `30%` and compare the run against "
                "the formula: `1/30` measured against `1/12` predicted, with the "
                "twenty-four-phase average landing back on the formula. Then move the "
                "phase and watch how far a single run can sit from the number you would "
                "have quoted.",
            ],
        },
        "quiz_title": "Staleness, TTLs and their price",
        "quiz": [
            {"q": "A value changes every `60 s` and is cached with a TTL of `10 s`. What fraction of the time is the cached copy stale?",
             "a": ["`1/6`, because the TTL is a sixth of the update interval",
                   "`1/12`",
                   "`0`, because the TTL is shorter than the update interval",
                   "`5/6`"],
             "c": 1,
             "why": "`T ≤ U`, so the branch is `T/(2U) = 10/120 = 1/12`. `1/6` is "
                    "`T/U`, the probability that an update lands inside a given window "
                    "&mdash; half of which is the average age when it does, which is "
                    "where the `2` comes from. A shorter TTL reduces staleness; it never "
                    "removes it, because the update can land anywhere."},
            {"q": "The same key is read `5` times a second. Its TTL is cut from `10 s` to `5 s`. What happens to the miss rate?",
             "a": ["It is unchanged, since the read rate did not change",
                   "It doubles, from `1/50` to `1/25`",
                   "It halves, from `1/50` to `1/100`",
                   "It becomes `1`, since the key now expires between reads"],
             "c": 1,
             "why": "The miss rate is `1/(λ_key·T)`: `1/50` at `T = 10 s` and `1/25` at "
                    "`T = 5 s`. Halving the TTL halves the staleness and doubles the "
                    "misses, which is the trade. It would only reach `1` if "
                    "`λ_key·T ≤ 1`, which at five reads a second needs a TTL under a "
                    "fifth of a second."},
            {"q": "A TTL of `120 s` is set on a value that changes every `60 s`. What is the stale fraction?",
             "a": ["`1`, since the TTL outlives the update", "`3/4`", "`1/4`", "`2`, which shows the model has broken"],
             "c": 1,
             "why": "`T ≥ U`, so the branch is `1 − U/(2T) = 1 − 60/240 = 3/4`. The "
                    "copy is fresh only for the part of the window before the first "
                    "update, which averages `U/2 = 30 s` out of `120 s`. `1/4` is that "
                    "fresh share, and `T/(2U) = 1` is the wrong branch &mdash; which "
                    "returns a plausible-looking number and is the reason to check the "
                    "branch first."},
            {"q": "Why does the lab run a timeline beside the formula?",
             "a": ["To check the arithmetic of the formula",
                   "Because the formula is an expectation over the refresh phase, and any single run can sit well away from it",
                   "Because the formula is only valid for `T ≤ U`",
                   "To show that the stale fraction is random"],
             "c": 1,
             "why": "At `U = 60 s`, `T = 10 s` and a phase of `30%` a single run measures "
                    "`1/30` against a formula that says `1/12`; averaged over twenty-four "
                    "phases it returns to `1/12` exactly. The formula is right about the "
                    "average and the run is right about that phase. Both branches are "
                    "valid, and the stale fraction of a given run is determined, not "
                    "random, once the phase is fixed."},
        ],
        "mistakes": [
            ("Believing a shorter TTL fixes staleness for free",
             "It does not fix it &mdash; `T/(2U)` is zero only at `T = 0` &mdash; and it "
             "is not free. Going from `T = 10 s` to `T = 1 s` at five reads a second "
             "takes the stale fraction from `1/12` to `1/120` and the miss rate from "
             "`1/50` to `1/5`, which is ten times the backend load. Quote both numbers "
             "or you have not made an argument."),
            ("Using the wrong branch",
             "At `T = 2U` the `T/(2U)` branch returns exactly `1`, which looks like a "
             "sensible answer for a very long TTL and is wrong: the right branch gives "
             "`3/4`. Compare `T` with `U` before substituting, every time. The branches "
             "meet at `T = U`, where both give `1/2`."),
            ("Reading the formula as a prediction about a particular run",
             "It is an expectation over the phase between the update clock and the "
             "refresh clock. With that phase fixed at `30%` of `U`, a run at "
             "`U = 60 s, T = 10 s` measures `1/30` rather than `1/12`. Use the formula "
             "to compare TTLs, not to report what last week&rsquo;s staleness was."),
        ],
        "standard": ("Finish when a TTL proposal without a miss rate attached looks incomplete to you.",
                     "You should be able to choose the correct branch, compute the stale "
                     "fraction and the implied miss rate for a TTL, state the two "
                     "assumptions the formula rests on, and describe the trade between "
                     "the two numbers as a factor rather than as a feeling."),
        "note": 'A TTL sets staleness against backend load on average. The moment it actually expires is not an average: a popular key going cold lets everything that arrives in the next few milliseconds through at once, and “Cache Stampedes” computes how many that is.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "cache-stampedes",
        "title": "Cache Stampedes",
        "module": "Where caches fail",
        "one_line": "Compute how many requests reach the backend in the window after a hot key expires, with and without coalescing.",
        "summary": (
            "For the few milliseconds between a hot key expiring and the first refill "
            "landing, there is no cache. Every request that arrives in that window "
            "misses and is forwarded, and by Little&rsquo;s Law the number of them is "
            "`λ·d` &mdash; a rate times a time. Single-flight coalescing reduces it to "
            "one, which is the difference between a cache that protects a backend and a "
            "cache that merely usually does."
        ),
        "key": [
            "stampede size = λ_key · d          a rate times a time, by Little's Law",
            "",
            "λ_key = 5 000 reads/s,  d = 100 ms fill",
            "    λ·d = 5 000 × 0.1 = 500 requests through the window",
            "    backend capacity 200 concurrent  →  the burst is 5/2 = 2.50× capacity",
            "",
            "with single-flight coalescing:  1 request, a factor of 500",
        ],
        "key_label": "The burst at expiry, and what coalescing makes of it",
        "concepts_intro": (
            "Three ideas, and the first one is a change of timescale: everything so far "
            "on this course was an average over a long window, and this is about one "
            "hundred-millisecond window."
        ),
        "concepts": [
            ("At expiry, there is no cache",
             "A cache entry expires. The next request misses and starts a fill that "
             "takes `d` milliseconds. Every request for that key arriving before the "
             "fill lands also finds nothing, also misses, and is also forwarded. For "
             "`d` milliseconds the hit rate for that key is zero, and `(1 − h)λ` "
             "describes none of it."),
            ("The burst is `λ·d`, and that is Little’s Law",
             "The number of requests in flight is the arrival rate times the time each "
             "spends in flight &mdash; the identity of &ldquo;Little&rsquo;s Law from a "
             "Trace&rdquo;, applied to one key over one window. At `5 000` reads a "
             "second and a `100 ms` fill that is `500` requests, all asking the backend "
             "for the same value at the same moment."),
            ("Coalescing, not caching, is what stops it",
             "Single-flight coalescing lets the first miss start the fill and makes "
             "every subsequent request for that key wait on the same in-flight fill. "
             "The backend sees exactly one request per key instead of `λ·d`. Nothing "
             "about the cache changed; what changed is what happens to the requests "
             "that miss together."),
        ],
        "read_title": "The window with no cache in it, and the two ways to survive it",
        "read_intro": "Where the burst comes from, how large it gets, and why a bigger cache does not help.",
        "body": [
            ("def", ("Miss window and stampede",
                     "The <strong>miss window</strong> `d` of a key is the time from a "
                     "miss being detected to the refilled value being available to serve "
                     "&mdash; the backend call plus the write back. A "
                     "<strong>stampede</strong> is the set of requests for that key "
                     "which arrive during the miss window and are therefore all "
                     "forwarded to the backend. Its size is `λ_key·d`.",
                     "`λ_key` is the read rate of the one key, not of the service. A "
                     "service at `50 000` rps whose hottest key takes ten per cent of "
                     "the traffic has `λ_key = 5 000`.")),
            ("p", "The formula is a rate times a time and nothing else. It does not "
                  "depend on the hit rate, the cache size, the policy or the "
                  "catalogue &mdash; those all describe steady state, and this is a "
                  "transient. That independence is the uncomfortable part: a cache with "
                  "a `99.9%` hit rate has exactly the same stampede as a cache with a "
                  "`50%` one, for the same key at the same read rate."),
            ("example", ("A hot key at five thousand reads a second",
                         "`λ_key = 5 000` reads a second, `d = 100 ms`. The stampede is "
                         "`5 000 × 0.1 = 500` requests. Against a backend that can hold "
                         "`200` concurrent fills that is `5/2 = 2.50` times its "
                         "capacity: the backend does not absorb this, and the requests "
                         "it cannot take either queue or fail.")),
            ("p", "Scale either input and it scales linearly. The same key at a `1 ms` "
                  "fill sends `5` requests through; at `500 ms` it sends `2 500`; at "
                  "`2 s`, `10 000`. And the fill time is the one thing you least "
                  "control, because a slow fill is exactly what happens when the backend "
                  "is already under pressure &mdash; which is a feedback loop, not a "
                  "coincidence."),
            ("h3", "Why the obvious fixes are not fixes"),
            ("p", "A bigger cache does not help: the key was in the cache and the "
                  "problem is the moment it left. A longer TTL does not help either; it "
                  "makes the expiry rarer, not smaller, and TTL and Staleness has "
                  "already priced what a longer TTL costs in wrongness. Nor does a "
                  "higher hit rate: the hit rate is an average over a window that "
                  "contains this one, and the average is fine."),
            ("p", "Two things do help. <strong>Coalescing</strong> &mdash; also called "
                  "single-flight or request collapsing &mdash; makes one request per key "
                  "per window reach the backend and parks the rest on the result. And "
                  "<strong>early refresh</strong>, where a request arriving near the end "
                  "of a TTL refreshes the entry while continuing to serve the old value, "
                  "removes the window altogether at the cost of a little more staleness."),
            ("thm", ("What coalescing is worth",
                     "Without coalescing, `λ_key·d` requests reach the backend per "
                     "expiry. With it, exactly one does, per key. The reduction factor "
                     "is `λ_key·d` itself.",
                     "So coalescing is worth the most precisely where the stampede is "
                     "worst: the hotter the key and the slower the fill, the larger the "
                     "factor. At `5 000` reads a second and a `100 ms` fill it is a "
                     "factor of `500`.")),
            ("h3", "Many keys at once, which is the version that takes systems down"),
            ("p", "A fleet that sets the same TTL on everything at deploy time expires "
                  "everything together. Then `k` hot keys each send `λ_key·d` requests "
                  "in the same window, and the burst is `k` times as large while "
                  "coalescing still reduces it to `k` &mdash; one per key. Jittering the "
                  "TTLs spreads the expiries out, and it is the cheapest of the three "
                  "fixes on this page."),
            ("p", "One limit on the model: `λ·d` counts arrivals in the window and "
                  "assumes the backend keeps accepting them. A backend that starts "
                  "queueing will make `d` longer, which lets more requests into the "
                  "window, which makes `d` longer still. The formula gives the first "
                  "step of that loop and not the rest of it, and the first step is "
                  "already enough to size the problem."),
        ],
        "lab": ("cache", {
            "mode": "stampede",
            "lam_key": 5000,
            "miss_ms": 100,
            "capacity": 200,
            "keys": 1,
        }),
        "steps_title": "Sizing the burst at expiry",
        "steps_intro": "Two inputs, one multiplication, and then the comparison that decides whether it matters.",
        "steps": [
            ("Find the read rate of the single hottest key",
             "Not the service&rsquo;s rate: one key&rsquo;s. If you know the total rate "
             "and the skew, Popularity Is Skewed: Zipf gives you the top key&rsquo;s "
             "share &mdash; at `N = 50` and `s = 2` it is `61.53%` of all requests, "
             "which makes `λ_key` most of `λ`."),
            ("Measure the miss window `d`",
             "From miss detected to value available, including the write back. Use a "
             "high percentile of the fill time rather than the mean: the stampede you "
             "care about is the one that happens when the backend is slow."),
            ("Multiply, and compare against what the backend can hold",
             "`λ_key·d` requests arrive in the window. Divide by the backend&rsquo;s "
             "concurrent capacity. Above `1` the backend does not absorb the burst, and "
             "the cache&rsquo;s excellent hit rate will not appear anywhere in the "
             "incident review."),
            ("Decide between coalescing, early refresh and jitter",
             "Coalescing takes the burst to one per key. Early refresh removes the "
             "window and costs a little staleness. Jitter stops many keys expiring "
             "together. They address different parts of the same failure and a busy "
             "system usually wants all three."),
        ],
        "worked": {
            "title": "One hot key: 5 000 reads a second, a 100 ms fill",
            "intro": [
                "The multiplication takes a line. The table under it is the same "
                "multiplication at six fill times, which is where the shape lives."
            ],
            "lines": [
                "λ_key = 5 000 reads/s,  d = 100 ms,  backend holds 200 concurrent fills",
                "",
                "stampede = λ_key · d = 5 000 × (100/1000) = 500 requests",
                "against capacity:  500/200 = 5/2 = 2.50×          the backend is overrun",
                "",
                "the same key at other fill times:",
                "     d          λ·d",
                "     1 ms         5",
                "    10 ms        50",
                "    50 ms       250",
                "   100 ms       500        ← here",
                "   500 ms     2 500",
                "  2000 ms    10 000",
                "",
                "with single-flight coalescing:   1 request       a factor of 500",
            ],
            "after": [
                "Read the table as a warning about `d` rather than about `λ`. The read "
                "rate of a hot key is a fact about your users; the fill time is a "
                "property of your backend, and it grows exactly when you can least "
                "afford it to.",
                "For a faded rehearsal, take a service at `20 000` rps whose hottest key "
                "is `10%` of traffic, with a `50 ms` fill and a backend that holds `200` "
                "concurrent requests. The supplied first move is that `λ_key = 2 000`; "
                "compute the burst and the ratio to capacity, then say what the ratio "
                "becomes if `12` hot keys expire together because they share a "
                "deploy-time TTL. State which of the three fixes you would reach for "
                "first and why.",
                "In the lab the burst is drawn as a rectangle against the "
                "backend&rsquo;s capacity line from Queues and Utilisation, with the "
                "coalesced version beside it. Raise the number of keys expiring together "
                "and watch the red rectangle grow while the green one does not.",
            ],
        },
        "quiz_title": "Bursts, windows and coalescing",
        "quiz": [
            {"q": "A key is read `5 000` times a second and takes `100 ms` to refill. How many requests reach the backend when it expires, without coalescing?",
             "a": ["`1`, because they are all for the same key", "`500`", "`5 000`", "`50`"],
             "c": 1,
             "why": "`λ_key·d = 5 000 × 0.1 = 500`. They are all for the same key, which "
                    "is exactly why they all miss &mdash; being identical does not merge "
                    "them unless something merges them, and that something is "
                    "coalescing. `5 000` is a whole second of reads and `50` is a `10 ms` "
                    "window."},
            {"q": "The same service has a `99.9%` overall hit rate. How does that change the stampede?",
             "a": ["It divides the burst by a thousand",
                   "It does not change it at all",
                   "It makes the burst `500` misses instead of `500` requests",
                   "It removes the burst, since almost everything hits"],
             "c": 1,
             "why": "The hit rate is a steady-state average over a window that contains "
                    "the stampede. During the miss window the hit rate for that key is "
                    "zero, whatever the long-run average is: every arrival finds nothing "
                    "and is forwarded. This is why `(1 − h)λ` cannot see this failure "
                    "mode."},
            {"q": "Which change actually reduces the number of requests the backend sees at expiry?",
             "a": ["A larger cache", "Single-flight coalescing", "A longer TTL", "A higher hit rate"],
             "c": 1,
             "why": "Coalescing makes one request per key reach the backend and parks "
                    "the rest on its result, a reduction by the factor `λ_key·d` itself. "
                    "A larger cache is irrelevant &mdash; the key was cached. A longer "
                    "TTL makes expiries rarer but not smaller, and buys that with "
                    "staleness."},
        ],
        "mistakes": [
            ("Believing a cache always protects the backend",
             "It protects it in steady state and not during the miss window, where for "
             "`d` milliseconds there is no cache at all. `5 000` reads a second through "
             "a `100 ms` fill is `500` simultaneous requests at a backend sized for "
             "`200`, and the hit rate that made the capacity plan work says nothing "
             "about it."),
            ("Using the service’s rate instead of the key’s",
             "The stampede is `λ_key·d`, and `λ_key` is one key&rsquo;s read rate. Using "
             "the whole service&rsquo;s rate overstates it by the reciprocal of the top "
             "key&rsquo;s share; using an average key&rsquo;s rate understates it by far "
             "more, because the key that stampedes is the hot one and popularity is "
             "skewed."),
            ("Reaching for a longer TTL",
             "A longer TTL makes the expiry happen less often; it does not make the "
             "burst any smaller when it does happen, and TTL and Staleness has already "
             "priced the wrongness it buys. The fixes that change the burst size are "
             "coalescing, early refresh, and jittering the TTLs so that many keys do not "
             "expire at once."),
        ],
        "standard": ("Finish when “we have a cache” stops sounding like an answer to a burst question.",
                     "You should be able to compute `λ_key·d` for a hot key, express it "
                     "as a multiple of the backend&rsquo;s concurrent capacity, state "
                     "what coalescing reduces it to and by what factor, and say why a "
                     "larger cache and a higher hit rate change neither number."),
        "note": 'Everything so far has been about reads. Writes have their own arithmetic and their own trade: “Write Policies” counts what a write-back cache actually sends to the backend on a trace, and what is lost if the process dies before the next flush.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "write-policies",
        "title": "Write Policies",
        "module": "Where caches fail",
        "one_line": "Count backend writes and bytes at risk for write-through and write-back on a write trace.",
        "summary": (
            "Write-through sends every write to the backend and keeps nothing at risk. "
            "Write-back holds writes in the cache and sends the distinct keys once per "
            "flush, which is a coalescing ratio on any trace with repeats. What it buys "
            "is fewer backend writes; what it costs is a loss window, and both come off "
            "the same trace."
        ),
        "key": [
            "write-through   backend writes = every write",
            "write-back      backend writes = distinct keys per flush window",
            "",
            "trace  A B A C A B A D A B,  flushed every 5 writes",
            "    10 writes → 6 distinct    ratio 5/3      1 000 → 600 writes/s",
            "    largest dirty set 3 keys × 4 kB = 12.00 kB at risk over 5.0 ms",
        ],
        "key_label": "Two policies, one trace, and the price of the better ratio",
        "concepts_intro": (
            "One rule each, and then a number that only exists for the second of them: "
            "what is lost if the process dies."
        ),
        "concepts": [
            ("Write-through sends every write",
             "The write goes to the backend and to the cache, and it is not acknowledged "
             "until the backend has it. Backend write rate equals the application write "
             "rate exactly. Nothing is ever only in the cache, so a crash loses nothing "
             "and the loss window is zero."),
            ("Write-back sends the distinct keys per flush",
             "The write goes to the cache and is acknowledged; the cache flushes dirty "
             "entries to the backend periodically. Repeated writes to the same key "
             "inside one flush window collapse into one backend write, so the backend "
             "sees the <em>distinct</em> keys per window. On `A B A C A B A D A B` "
             "flushed every five writes, that is `6` backend writes for `10` "
             "application writes."),
            ("The ratio is bought with a loss window",
             "Whatever is dirty when the process dies is gone. The right measure is the "
             "largest dirty set a flush interval ever holds, not the average: an average "
             "loss window is not what a crash takes. On that trace it is `3` keys, which "
             "at `4 kB` each is `12.00 kB`, held for the `5.0 ms` a flush interval lasts "
             "at `1 000` writes a second."),
        ],
        "read_title": "Two policies, the coalescing ratio, and what is at risk",
        "read_intro": "The rules, the counting, and why the trace decides whether write-back is worth anything at all.",
        "body": [
            ("def", ("Write-through and write-back",
                     "Under <strong>write-through</strong>, every write is applied to "
                     "the cache and to the backend before it is acknowledged. Under "
                     "<strong>write-back</strong>, a write is applied to the cache, "
                     "marked <strong>dirty</strong> and acknowledged; dirty entries are "
                     "written to the backend on a periodic <strong>flush</strong>.",
                     "The <strong>coalescing ratio</strong> of a trace under write-back "
                     "is the number of writes divided by the number of distinct keys "
                     "written, counted per flush window. It is `1` when every write in "
                     "a window is to a different key, and it is the window length when "
                     "they are all to the same key.")),
            ("p", "Both policies leave the cache correct. The difference is entirely "
                  "about the backend: how many writes it receives, how quickly it learns "
                  "about them, and what happens to the ones it has not learned about "
                  "yet."),
            ("h3", "Counting the ratio off a trace"),
            ("p", "Take the write trace `A B A C A B A D A B` and flush every five "
                  "writes. The first window is `A B A C A`: five writes, three distinct "
                  "keys, so two writes to `A` are coalesced away. The second is "
                  "`B A D A B`: five writes, three distinct keys again. Ten writes, six "
                  "backend writes, a ratio of `5/3`."),
            ("math", [
                "trace:   A B A C A | B A D A B          flush every 5 writes",
                "",
                "  window 1   A B A C A     5 writes → 3 distinct {A, B, C}",
                "  window 2   B A D A B     5 writes → 3 distinct {A, B, D}",
                "",
                "  write-through   10 backend writes      at 1 000 w/s → 1 000 w/s",
                "  write-back       6 backend writes      at 1 000 w/s →   600 w/s",
                "  ratio           10/6 = 5/3",
                "",
                "  largest dirty set: 3 keys × 4 kB = 12.00 kB, held for 5.0 ms",
            ]),
            ("p", "Widen the flush window to ten writes and the whole trace becomes one "
                  "window: four distinct keys, a ratio of `5/2`, and the backend sees "
                  "`400` writes a second instead of `600`. The dirty set grows to `4` "
                  "keys and `16.00 kB`, held for `10.0 ms`. That is the trade in its "
                  "entirety, and both ends of it moved together."),
            ("h3", "What the trace decides"),
            ("p", "The ratio is a property of the workload, not of the policy. A trace "
                  "in which every write is to a different key inside its window &mdash; "
                  "`A B C D E F G H I J` &mdash; coalesces nothing at all: write-back "
                  "sends ten writes, exactly as write-through does, and still carries "
                  "the loss window. A trace of one key repeated ten times coalesces to "
                  "one per window and buys a ratio of five."),
            ("p", "So &ldquo;write-back is faster&rdquo; is not a general claim. It is "
                  "a claim about a workload with repeated writes to the same keys inside "
                  "a flush interval, and if you do not have that, write-back is a loss "
                  "window with no compensating gain. Run your own trace before choosing."),
            ("h3", "What is actually at risk"),
            ("p", "The bytes at risk are the largest dirty set times the object size, "
                  "and the exposure lasts a flush interval &mdash; `w/λ_w` seconds, for "
                  "a window of `w` writes at `λ_w` writes a second. At `1 000` writes a "
                  "second and a five-write window that is `5.0 ms`, which sounds "
                  "negligible until you multiply it by the number of processes you run "
                  "and the number of times a year each of them dies."),
            ("p", "The honest statement of the trade is arithmetic on both numbers at "
                  "once: a flush window `k` times wider improves the ratio by at most "
                  "`k` and grows both the dirty set and the exposure time. Whether the "
                  "trade is acceptable is a durability question, and Availability and "
                  "Failure is where losing things gets priced."),
        ],
        "lab": ("cache", {
            "mode": "write",
            "trace": "A B A C A B A D A B",
            "window": 5,
            "rate": 1000,
            "obj_kb": 4,
        }),
        "steps_title": "Choosing a write policy from a trace",
        "steps_intro": "Count the distinct keys per window first. If the ratio is one, there is nothing to discuss.",
        "steps": [
            ("Take a real write trace and a flush interval",
             "A sequence of written keys in order, and how many writes a flush covers. "
             "The flush interval is usually configured in time; convert it with the "
             "write rate, since `w = λ_w · flush seconds`."),
            ("Count distinct keys per window",
             "Not distinct keys overall: per window. A key written in two different "
             "windows is two backend writes. This is the only counting in the lesson and "
             "it is where the ratio comes from."),
            ("Compute the ratio and the backend write rate",
             "`writes ÷ distinct` is the ratio, and `λ_w × (distinct/writes)` is what "
             "the backend actually receives. On this trace, `1 000` writes a second "
             "becomes `600`."),
            ("Compute the bytes at risk, using the largest dirty set",
             "Peak, not mean: a crash takes whatever was dirty at that instant, and the "
             "instant is not chosen kindly. Multiply by the object size and state the "
             "exposure as bytes over a flush interval."),
        ],
        "worked": {
            "title": "A B A C A B A D A B, flushed every five writes",
            "intro": [
                "Ten writes, two windows, and then the same trace at a wider flush so "
                "that both ends of the trade move where you can see them."
            ],
            "lines": [
                "trace:  A B A C A B A D A B      1 000 writes/s,  4 kB objects",
                "",
                "flush every 5 writes:",
                "  window 1   A B A C A     5 writes,  distinct {A,B,C} = 3",
                "  window 2   B A D A B     5 writes,  distinct {A,B,D} = 3",
                "                          10 writes,            total  = 6",
                "",
                "  write-through   10 backend writes    1 000 writes/s",
                "  write-back       6 backend writes      600 writes/s",
                "  coalescing ratio  10/6 = 5/3",
                "  at risk   peak dirty set 3 keys × 4 kB = 12.00 kB over 5.0 ms",
                "",
                "flush every 10 writes (one window):",
                "  distinct {A,B,C,D} = 4     ratio 10/4 = 5/2     400 writes/s",
                "  at risk   4 keys × 4 kB = 16.00 kB over 10.0 ms",
            ],
            "after": [
                "Doubling the flush window improved the ratio from `5/3` to `5/2` "
                "&mdash; a further `200` writes a second off the backend &mdash; and "
                "took the exposure from `12.00 kB` over `5.0 ms` to `16.00 kB` over "
                "`10.0 ms`. Both numbers moved, and a proposal that mentions only the "
                "first is not a proposal.",
                "For a faded rehearsal, run `A B C D E F G H I J` at a flush of five. "
                "The supplied first move is to count the distinct keys in the first "
                "window before computing anything; do that, then state the ratio, the "
                "backend write rate and the bytes at risk, and say in one sentence what "
                "write-back has bought on this trace.",
                "The lab marks every repeated write inside a window as coalesced away "
                "and counts the rest, so you can see which writes the ratio is made of. "
                "Try the one-hot-key trace and the all-distinct trace before deciding "
                "what you believe about write-back.",
            ],
        },
        "quiz_title": "Ratios, rates and loss windows",
        "quiz": [
            {"q": "On `A B A C A B A D A B` flushed every five writes, how many writes does a write-back cache send to the backend?",
             "a": ["`10`, one per write", "`6`", "`4`, the distinct keys in the whole trace", "`2`, one per flush"],
             "c": 1,
             "why": "Distinct keys are counted per window: `{A, B, C}` then `{A, B, D}`, "
                    "three each, six in total. `4` is the distinct count over the whole "
                    "trace, which would be right only if the whole trace were one flush "
                    "window; `10` is what write-through sends."},
            {"q": "A write trace is `A B C D E F G H I J`, flushed every five writes. What does write-back buy?",
             "a": ["A ratio of `2`, because there are two windows",
                   "Nothing: every write is to a different key inside its window, so it still sends ten",
                   "A ratio of `5/2`, as on the hot-key trace",
                   "Half the backend writes, since flushes are batched"],
             "c": 1,
             "why": "Coalescing only removes repeats within a window, and there are "
                    "none here: five distinct keys in each of two windows is ten backend "
                    "writes, exactly what write-through sends. The loss window is still "
                    "there. Batching writes into one flush does not reduce how many "
                    "writes the backend must apply."},
            {"q": "Why are the bytes at risk computed from the largest dirty set rather than the average one?",
             "a": ["Because the average is harder to compute",
                   "Because a crash takes whatever is dirty at that instant, and nothing guarantees it is an average instant",
                   "Because the peak is always double the average",
                   "Because the flush interval is not constant"],
             "c": 1,
             "why": "Loss is not an expectation you get to average over: a process dies "
                    "at one moment and takes what was dirty then. Sizing the exposure "
                    "from the peak is the only version of the number that bounds what "
                    "you can lose, and the peak bears no fixed relation to the mean."},
            {"q": "A team widens the flush interval from five writes to ten and the ratio improves from `5/3` to `5/2`. What else changed?",
             "a": ["Nothing else; the ratio is the whole effect",
                   "The peak dirty set grew from `3` keys to `4` and the exposure from `5.0 ms` to `10.0 ms`",
                   "The application write rate fell",
                   "The cache hit rate improved"],
             "c": 1,
             "why": "Widening the window holds more writes for longer, so both the "
                    "amount at risk and the time it is at risk grow. The application "
                    "write rate is an input and does not change, and read hit rate is a "
                    "different measurement entirely."},
        ],
        "mistakes": [
            ("Believing write-back is free",
             "It costs a loss window: whatever is dirty when the process dies is gone. "
             "On the trace above that is `12.00 kB` over `5.0 ms` &mdash; small, until "
             "it is multiplied by a fleet. A proposal for write-back that does not name "
             "the peak dirty set and the exposure time has priced only the half it "
             "likes."),
            ("Counting distinct keys over the whole trace",
             "The coalescing is per flush window. `A B A C A B A D A B` has four "
             "distinct keys overall and six backend writes at a five-write flush, "
             "because a key written in two windows is written to the backend twice. "
             "Counting globally overstates the ratio by whatever the flush interval "
             "would have been."),
            ("Assuming a coalescing ratio the workload does not have",
             "On `A B C D E F G H I J` the ratio is `1`: write-back sends every write, "
             "exactly as write-through does, and still carries the loss window. The "
             "ratio is a property of the trace, so measure it on yours before choosing "
             "the policy that depends on it."),
        ],
        "standard": ("Finish when you would not accept a write-back proposal without a peak dirty set in it.",
                     "You should be able to count distinct keys per flush window off a "
                     "trace, convert that into a coalescing ratio and a backend write "
                     "rate, compute the bytes at risk from the peak dirty set and the "
                     "exposure from the flush interval, and say what a wider flush does "
                     "to all four numbers."),
        "note": 'The next two lessons are about caches that are not one cache. The first is a second level behind the first, where the rate you measure is not the rate you want: “Multi-level Caches” shows why the two miss rates multiply rather than add.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "multi-level-caches",
        "title": "Multi-level Caches",
        "module": "Beyond one cache",
        "one_line": "Compute the global hit rate and mean latency of two cache levels, given that the second level's rate is conditional.",
        "summary": (
            "A second cache behind the first sees only what the first one missed, so its "
            "hit rate is measured on a different population. The global miss rate is the "
            "product `(1 − h₁)(1 − h₂)` rather than a sum, and the mean latency is "
            "`t₁ + (1 − h₁)(t₂ + (1 − h₂)t₃)` &mdash; a conditional expectation, over "
            "three outcomes you can list."
        ),
        "key": [
            "h₂ is measured on the L1 MISSES, so it is conditional",
            "",
            "global miss = (1 − h₁)(1 − h₂)          the misses multiply",
            "global hit  = h₁ + (1 − h₁)h₂",
            "E[latency]  = t₁ + (1 − h₁)(t₂ + (1 − h₂)t₃)",
            "",
            "h₁ = 80%, h₂ = 50%, t = (1, 5, 50) ms:  hit 9/10, miss 1/10, mean 7 ms",
        ],
        "key_label": "Two levels, one conditional rate, three outcomes",
        "concepts_intro": (
            "One new object is introduced here and it is small: an expectation taken "
            "over a restricted set of outcomes. Everything it is used for on this page "
            "is a list of three."
        ),
        "concepts": [
            ("`h₂` is conditional, and it is measured that way",
             "The second level only receives requests the first level missed, so its hit "
             "rate is a fraction of those, not of all requests. Written out, `h₂` is "
             "`P(L2 hit | L1 miss)`. A dashboard showing `50%` on L2 is telling you "
             "about half of the L1 misses, which at `h₁ = 80%` is `10%` of all "
             "requests."),
            ("The misses multiply",
             "A request reaches the origin only if it missed both levels, and the second "
             "event is conditioned on the first, so the global miss rate is "
             "`(1 − h₁)(1 − h₂)`. At `80%` and `50%` that is "
             "`(1/5)(1/2) = 1/10`, and the global hit rate is `9/10`. Adding the two "
             "rates gives `130%`, which is how you know that move is wrong."),
            ("A conditional expectation, over three outcomes",
             "`E[X | B]` is the expectation of `X` computed over only the outcomes in "
             "which `B` happened, with their probabilities renormalised by dividing by "
             "`P(B)`. Here `B` is &ldquo;missed L1&rdquo;, and the outcomes number "
             "three, so every use of it is a finite list you can add up by hand."),
        ],
        "read_title": "A conditional rate, a product of misses, and a latency read forwards",
        "read_intro": "What the second level's number actually measures, the one definition this needs, and the three-row enumeration that settles it.",
        "body": [
            ("def", ("Conditional expectation",
                     "For a random variable `X` and an event `B` with `P(B) > 0`, the "
                     "<strong>conditional expectation</strong> `E[X | B]` is the "
                     "expectation of `X` computed over only the outcomes in which `B` "
                     "happened, with their probabilities renormalised by dividing by "
                     "`P(B)`.",
                     'That is the whole definition, and it is all this lesson needs. '
                     'Discrete Mathematics gives conditional probability in '
                     '“Conditional Probability” and expectation in “Expected Value”; '
                     'this combines them, and every use of it here is a finite '
                     'enumeration of three outcomes rather than anything requiring '
                     'machinery.')),
            ("p", "The reason it turns up is that the second cache level&rsquo;s hit "
                  "rate is not a number about requests. It is a number about "
                  "<em>the requests that reached it</em>, which are exactly the ones "
                  "that missed the first level."),
            ("def", ("Two levels",
                     "A request is served by L1 with probability `h₁`. If it misses, it "
                     "is served by L2 with probability `h₂ = P(L2 hit | L1 miss)`. If it "
                     "misses both it is served by the origin. The "
                     "<strong>global hit rate</strong> is the fraction served by either "
                     "cache and the <strong>global miss rate</strong> is the fraction "
                     "reaching the origin.")),
            ("p", "Every request pays `t₁` for the L1 lookup, whether or not it hits. "
                  "The ones that miss pay `t₂` on top for the L2 lookup. The ones that "
                  "miss both pay `t₃` on top of that. Reading the branch forwards gives "
                  "the mean directly, and enumerating the three outcomes gives the same "
                  "number as a check."),
            ("math", [
                "h₁ = 80% = 4/5,   h₂ = 50% = 1/2,   t₁ = 1, t₂ = 5, t₃ = 50 ms",
                "",
                "  outcome            probability             latency    contribution",
                "  L1 hit             h₁            = 4/5      1 ms        4/5",
                "  L1 miss, L2 hit    (1−h₁)h₂      = 1/10     6 ms        3/5",
                "  both miss          (1−h₁)(1−h₂)  = 1/10    56 ms       28/5",
                "  ────────────────────────────────────────────────────────────",
                "  all                              = 1                   35/5 = 7 ms",
                "",
                "forwards:  t₁ + (1−h₁)(t₂ + (1−h₂)t₃) = 1 + (1/5)(5 + (1/2)(50)) = 7",
            ]),
            ("p", "The three probabilities sum to `1` and the contributions sum to the "
                  "mean, which is the check worth doing every time: if the column does "
                  "not sum to `1`, a conditional rate has been used as an unconditional "
                  "one somewhere."),
            ("h3", "The two wrong answers, and why each is tempting"),
            ("p", "The first is adding the hit rates: `80% + 50% = 130%`. It is easy to "
                  "spot here because it exceeds `100%`, and much harder to spot at "
                  "`h₁ = 40%` and `h₂ = 50%`, where it gives a plausible `90%` against a "
                  "true global rate of `70%`. Rates only add when the events are "
                  "disjoint on the same population, and these are not on the same "
                  "population at all."),
            ("p", "The second is reading L2&rsquo;s measured rate as a global one: "
                  "&ldquo;L2 is serving half our traffic.&rdquo; It is serving half of "
                  "the L1 misses, which is `(1/5)(1/2) = 1/10` of all requests. The "
                  "monitoring is not lying; it is answering a question about a "
                  "population that the reader has substituted for another one."),
            ("example", ("What a level is worth",
                         "Set `h₂ = 0` &mdash; an L2 that never hits &mdash; and `20%` "
                         "of requests reach the origin for a mean of `12 ms`. Raise "
                         "`h₂` to `50%` and the origin share halves to `10%` and the "
                         "mean falls to `7 ms`. The halving of origin load is the whole "
                         "point, by Hit Rate and Backend Load; the `12 ms` is what a "
                         "level that never hits still costs, because every L1 miss pays "
                         "`t₂` on the way to an origin it was going to reach anyway.")),
            ("p", "That last clause is the cost of a second level and it is easy to "
                  "overlook. A level that rarely hits adds its lookup time to every "
                  "request that misses the level above and returns nothing for it. The "
                  "arithmetic is `(1 − h₁)t₂` of pure overhead against "
                  "`(1 − h₁)h₂t₃` of saving, and the level is worth having when "
                  "`h₂t₃ > t₂` &mdash; which at `h₂ = 50%`, `t₃ = 50 ms` and `t₂ = 5 ms` "
                  "it comfortably is."),
            ("p", "One assumption to name: `h₂` is treated as a single number, but the "
                  "population reaching L2 is not a random sample of traffic. It is "
                  "precisely the unpopular keys, because the popular ones were absorbed "
                  "above &mdash; which is why a second level&rsquo;s hit rate is "
                  "generally much lower than the first&rsquo;s and why it cannot be "
                  "predicted by pointing the Zipf curve at L2&rsquo;s size."),
        ],
        "lab": ("cache", {
            "mode": "levels",
            "h1_tenths": 800,
            "h2_tenths": 500,
            "t1": 1,
            "t2": 5,
            "t3": 50,
        }),
        "steps_title": "Working with two levels",
        "steps_intro": "Establish which population each number was measured on before doing any arithmetic with it.",
        "steps": [
            ("Ask what each hit rate was measured on",
             "`h₁` is over all requests; `h₂` is over the requests that reached L2. If "
             "the monitoring reports L2&rsquo;s rate as a share of <em>all</em> traffic "
             "instead, that is `(1 − h₁)h₂` and you must divide by `1 − h₁` before using "
             "it as `h₂`."),
            ("Multiply the miss rates",
             "`(1 − h₁)(1 − h₂)` is the fraction reaching the origin, and "
             "`1 −` that is the global hit rate. Never add hit rates; if the answer can "
             "exceed `100%` the method is wrong even when the particular answer does "
             "not."),
            ("Enumerate the three outcomes",
             "L1 hit, L1 miss then L2 hit, both miss. Write the probability and the "
             "latency of each, multiply, add. Check that the probabilities sum to `1` "
             "&mdash; that check catches a conditional rate used unconditionally, which "
             "is the one error this lesson is about."),
            ("Charge every request for every level it touched",
             "The mean is `t₁ + (1 − h₁)(t₂ + (1 − h₂)t₃)`, not a weighted average of "
             "`t₁`, `t₂` and `t₃`. An L1 hit costs `t₁`; an L2 hit costs `t₁ + t₂`; an "
             "origin fetch costs `t₁ + t₂ + t₃`."),
        ],
        "worked": {
            "title": "h₁ = 80%, h₂ = 50% of the misses, latencies 1, 5 and 50 ms",
            "intro": [
                "Both routes to the same number: the enumeration, and the forwards read "
                "of the branch. They agree, and each catches a different mistake."
            ],
            "lines": [
                "h₁ = 4/5,  h₂ = 1/2 OF THE L1 MISSES,  t₁ = 1, t₂ = 5, t₃ = 50 ms",
                "",
                "global miss = (1 − h₁)(1 − h₂) = (1/5)(1/2) = 1/10 = 10.00%",
                "global hit  = 1 − 1/10 = 9/10 = 90.00%",
                "",
                "enumeration:",
                "  L1 hit            4/5      ×  1 ms  =   4/5",
                "  L1 miss, L2 hit   1/10     ×  6 ms  =   3/5",
                "  both miss         1/10     × 56 ms  =  28/5",
                "  probabilities     4/5 + 1/10 + 1/10 = 1            ✓",
                "  mean              4/5 + 3/5 + 28/5  = 35/5 = 7 ms",
                "",
                "forwards:  1 + (1/5)(5 + (1/2)(50))",
                "         = 1 + (1/5)(5 + 25) = 1 + 6 = 7 ms          ✓",
                "",
                "the two wrong answers:",
                "  adding the rates          80% + 50% = 130%    over 100%",
                "  reading h₂ as global      \"L2 serves 50%\"      it serves 1/10",
            ],
            "after": [
                "The probability column summing to `1` is the check that matters. "
                "Substituting `h₂` for `(1 − h₁)h₂` there makes the column sum to "
                "`13/10`, and that is the same error as adding the rates, caught one "
                "line earlier.",
                "For a faded rehearsal, take `h₁ = 90%`, `h₂ = 50%` and the same three "
                "latencies. The supplied first move is that the global miss rate is "
                "`(1/10)(1/2)`; finish it, enumerate the three outcomes, compute the "
                "mean both ways, and then say what fraction of all requests L2 is "
                "actually serving. Compare that with what a dashboard reporting "
                "&ldquo;L2 hit rate: 50%&rdquo; would have led you to believe.",
                "The lab draws the flow with each branch labelled as a share of all "
                "requests, and prints both wrong answers underneath so you can see them "
                "beside the right one rather than be told about them.",
            ],
        },
        "quiz_title": "Conditioning, products and means",
        "quiz": [
            {"q": "`h₁ = 80%` and L2 serves `50%` of the requests that reach it. What fraction of all requests reaches the origin?",
             "a": ["`30%`, since `100% − 80% − 50%`... ", "`10%`", "`50%`", "`20%`"],
             "c": 1,
             "why": "The misses multiply: `(1 − h₁)(1 − h₂) = (1/5)(1/2) = 1/10`. "
                    "`20%` is the L1 miss rate before L2 gets a chance at it, `50%` is "
                    "L2&rsquo;s conditional rate read as a global one, and subtracting "
                    "both rates from `100%` treats two rates measured on different "
                    "populations as if they were shares of the same one."},
            {"q": "With `h₁ = 80%`, `h₂ = 50%`, `t₁ = 1 ms`, `t₂ = 5 ms` and `t₃ = 50 ms`, what is the mean latency?",
             "a": ["`7 ms`", "`11 ms`", "`5.6 ms`", "`18.67 ms`"],
             "c": 0,
             "why": "`t₁ + (1 − h₁)(t₂ + (1 − h₂)t₃) = 1 + (1/5)(5 + 25) = 7 ms`, which "
                    "the three-outcome enumeration confirms: `4/5 + 3/5 + 28/5 = 7`. "
                    "`11 ms` is the mean with no L2 at all. `18.67 ms` is the unweighted "
                    "average of the three path latencies `1`, `6` and `56`, which "
                    "ignores the probabilities entirely."},
            {"q": "A dashboard reports &ldquo;L2 hit rate: 50%&rdquo; and `h₁ = 80%`. What share of all requests does L2 serve?",
             "a": ["`50%`", "`10%`", "`40%`", "`90%`"],
             "c": 1,
             "why": "L2 is serving half of the twenty per cent that missed L1: "
                    "`(1/5)(1/2) = 1/10`. `40%` would be `h₁ · h₂`, conditioning on the "
                    "wrong event, and `90%` is the global hit rate across both levels. "
                    "The dashboard is correct about the population it measured; the "
                    "error is substituting one population for another."},
            {"q": "Under what condition is a second cache level worth its lookup time?",
             "a": ["Whenever `h₂ > 0`",
                   "When `h₂t₃ > t₂`: what it saves on the requests it serves must beat what it costs on the ones it does not",
                   "When `h₂ > h₁`",
                   "When `t₂ < t₁`"],
             "c": 1,
             "why": "Every L1 miss pays `t₂` whether or not L2 hits, so the overhead is "
                    "`(1 − h₁)t₂` and the saving is `(1 − h₁)h₂t₃`. Dividing through by "
                    "`(1 − h₁)` leaves `h₂t₃ > t₂`. A level with a tiny hit rate in "
                    "front of a fast origin is a pure tax, however positive `h₂` is."},
        ],
        "mistakes": [
            ("Adding the two hit rates",
             "`80% + 50% = 130%` is visibly wrong; `40% + 50% = 90%` is not, and it is "
             "the same error with a plausible answer. The true global rate at those "
             "figures is `70%`. Hit rates add only across disjoint outcomes on one "
             "population, and `h₂` is measured on a different population from `h₁`."),
            ("Reading L2’s measured rate as a share of all traffic",
             "&ldquo;L2 is serving half our requests&rdquo; from a dashboard showing "
             "`h₂ = 50%` at `h₁ = 80%` overstates it by five: L2 serves `1/10` of all "
             "requests. Before using any cache statistic, ask which requests it was "
             "measured over."),
            ("Averaging the three latencies instead of accumulating them",
             "A request that reaches the origin has paid `t₁ + t₂ + t₃ = 56 ms`, not "
             "`t₃ = 50 ms`, and the mean is not a weighted average of `1`, `5` and `50`. "
             "Write the three path totals first, then weight them, and check the "
             "probabilities sum to `1`."),
        ],
        "standard": ("Finish when your first question about any cache statistic is which requests it was measured over.",
                     "You should be able to state `h₂` as a conditional probability, "
                     "compute the global miss rate as a product, enumerate the three "
                     "outcomes with their path latencies and probabilities, produce the "
                     "mean by both routes, and say what share of all requests the second "
                     "level actually serves."),
        "note": 'The last lesson moves the cache to the edge, where the arithmetic is the same and the unit is not. A CDN is billed in bytes, and “CDN Egress and Origin Load” shows that the byte hit rate and the request hit rate are two different numbers &mdash; and that the invoice follows the one nobody puts on the dashboard.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "cdn-egress-and-origin-load",
        "title": "CDN Egress and Origin Load",
        "module": "Beyond one cache",
        "one_line": "Compute origin gigabytes per day and the monthly egress bill from a byte hit rate, and the gap between that and the request hit rate.",
        "summary": (
            "A CDN is billed in bytes, so the hit rate that decides the invoice is a "
            "byte hit rate: the share of bytes served from the edge, not the share of "
            "requests. The two come apart whenever object size varies with popularity, "
            "and it usually does in the unhelpful direction &mdash; the popular objects "
            "are the small ones, so the cheap hits are the cheap ones."
        ),
        "key": [
            "request hit rate = share of REQUESTS served at the edge",
            "byte hit rate    = share of BYTES served at the edge",
            "",
            "N = 20, s = 1, top C = 4 cached, size ∝ rank¹",
            "    requests  57.91%        bytes  20.00%        a gap of 37.91 points",
            "",
            "origin GB/day = (1 − byte hit) × total GB/day",
            "    50 000 GB/day → 40 000 GB/day to the origin → $24 000 over 30 days",
        ],
        "key_label": "Two hit rates, and the one the invoice uses",
        "concepts_intro": (
            "The same harmonic ratio as the skew lessons, weighted differently. The "
            "weighting is the entire content, and it changes the answer by a factor of "
            "three here."
        ),
        "concepts": [
            ("The byte hit rate weights each rank by its size",
             "The request hit rate sums `p_i` over the cached ranks. The byte hit rate "
             "sums `p_i × size_i` over the same ranks, divided by the same sum over all "
             "ranks. With `size_i ∝ i^b` the weights are `i^(b−s)`, so it is the "
             "identical harmonic ratio at exponent `s − b` &mdash; one formula, not a "
             "second model."),
            ("They are equal only when size does not vary with rank",
             "At `b = 0` every object is the same size and the two rates are the same "
             "number under two names: that is the control. Move `b` off zero and they "
             "separate, and at `b = s` the byte hit rate collapses to exactly `C/N`, "
             "the uniform rate, because size grows exactly as fast as popularity falls."),
            ("The gap runs the wrong way for a CDN",
             "Real edge workloads have `b > 0`: thumbnails and API responses are "
             "popular and small, video segments and installers are unpopular and large. "
             "So the byte hit rate is the lower of the two, and an origin-load estimate "
             "made from the request hit rate is optimistic. At `N = 20`, `s = 1`, "
             "`C = 4` and `b = 1` it is `57.91%` against `20.00%`."),
        ],
        "read_title": "Two hit rates, the size profile that separates them, and the bill",
        "read_intro": "One weighted sum, three cases that fall out of it, and the invoice that follows the second number.",
        "body": [
            ("def", ("Request hit rate and byte hit rate",
                     "For a cache holding the top `C` of `N` ranked objects, the "
                     "<strong>request hit rate</strong> is the share of requests served "
                     "from it and the <strong>byte hit rate</strong> is the share of "
                     "bytes served from it. With Zipf popularity `p_i ∝ 1/iˢ` and sizes "
                     "`size_i ∝ i^b`, the second is `Σ i^(b−s)` over the cached ranks "
                     "divided by the same sum over all ranks.",
                     "`b` is a <strong>size exponent</strong>, positive when popular "
                     "objects are small. Setting `b = 0` recovers the request hit rate "
                     "exactly, which is how you can tell the two formulas are one "
                     "formula.")),
            ("p", "Everything that follows is that one ratio evaluated at three "
                  "exponents, and each case arrives as arithmetic rather than as an "
                  "assertion."),
            ("ul", [
                "`b = 0` &mdash; every object the same size. Byte hit rate equals "
                "request hit rate. The control.",
                "`b = s` &mdash; size grows exactly as fast as popularity falls, so "
                "every rank carries the same bytes and the byte hit rate is exactly "
                "`C/N`, the uniform answer.",
                "`b > 0` in general &mdash; popular objects are smaller, so the byte hit "
                "rate is below the request hit rate, and the gap widens with `b`.",
            ]),
            ("example", ("Twenty objects, classic Zipf, size proportional to rank",
                         "`N = 20`, `s = 1`, `C = 4`, `b = 1`. The top four objects are "
                         "`57.91%` of the requests and exactly `20.00%` of the bytes "
                         "&mdash; which is `C/N = 4/20`, because `b = s` here. A gap of "
                         "`37.91` points between two numbers people use "
                         "interchangeably.")),
            ("p", "Push the size profile harder and the gap widens. At `b = 2` on the "
                  "same catalogue the byte hit rate falls to `4.76%` while the request "
                  "hit rate is unchanged at `57.91%`: the edge is still serving more "
                  "than half of the requests and is now serving one twentieth of the "
                  "bytes, because the objects it is not holding are enormous."),
            ("h3", "The invoice follows the byte rate"),
            ("p", "Origin egress is `(1 − byte hit rate) × total bytes`, and the bill is "
                  "that times the price per gigabyte times the days. At `50 000 GB/day` "
                  "of edge egress with a `20.00%` byte hit rate, `40 000 GB/day` still "
                  "leaves the origin, and at two cents a gigabyte over thirty days that "
                  "is `$24 000`."),
            ("math", [
                "total edge egress      50 000 GB/day",
                "byte hit rate          20.00%",
                "",
                "origin  = (1 − 0.20) × 50 000  =  40 000 GB/day",
                "bill    = 40 000 × 30 × $0.02  =  $24 000.00",
                "",
                "billing from the REQUEST hit rate instead (57.91%):",
                "origin  = (1 − 0.5791) × 50 000 ≈  21 047 GB/day",
                "bill    ≈ $12 627.98                  barely half the real invoice",
            ]),
            ("p", "Nearly twice the bill, from using the number that was on the "
                  "dashboard. And the error is one-sided: because `b > 0` is the normal "
                  "shape of an edge workload, substituting the request hit rate always "
                  "<em>under</em>-estimates origin egress. A capacity plan made this way "
                  "is optimistic exactly where being wrong is expensive."),
            ("p", "The same gap applies to the origin&rsquo;s capacity, not only its "
                  "bill. The origin must actually serve `40 000 GB` a day; the request "
                  "hit rate predicted `21 047 GB`, and a link, an origin fleet and an "
                  "autoscaling policy sized against the second number meet the first "
                  "one on the day the video catalogue gets popular."),
            ("h3", "What to do about it"),
            ("p", "Two moves change the byte rate rather than the request rate. Caching "
                  "by <em>bytes served</em> rather than by request count &mdash; "
                  "admitting large popular objects even though they cost more slots "
                  "&mdash; moves the byte hit rate directly. And splitting large objects "
                  "into range-cacheable pieces turns one big miss into many small hits, "
                  "which is why video is served in segments."),
            ("p", "One caution on the model. `size_i ∝ i^b` is a smooth profile, and "
                  "real catalogues are lumpy: a handful of very large objects can "
                  "dominate the byte totals without being anywhere near a clean curve. "
                  "Use this to understand the direction and the rough size of the gap, "
                  "and measure the byte hit rate itself before writing a number into a "
                  "budget."),
        ],
        "lab": ("cache", {
            "mode": "hitrate",
            "view": "bytes",
            "n": 20,
            "s": 1,
            "c": 4,
            "b": 1,
            "gb_day": 50000,
            "cents_gb": 2,
        }),
        "steps_title": "Estimating origin load and egress cost",
        "steps_intro": "Get the byte hit rate first. Every number after it is a multiplication, and every one of them is wrong if you used the other rate.",
        "steps": [
            ("Ask which hit rate you have been given",
             "A CDN dashboard reports both and they are labelled similarly. If only one "
             "is available, assume it is the request hit rate, because that is the one "
             "that is easier to compute and the one more often displayed by default."),
            ("Get or estimate the byte hit rate",
             "Measure it if you can: bytes served from the edge over total bytes served. "
             "If you have to estimate, use the size profile &mdash; the same harmonic "
             "ratio at exponent `s − b` &mdash; and carry an interval rather than a "
             "figure."),
            ("Multiply out the origin egress",
             "`(1 − byte hit rate) × total bytes per day`. Keep decimal gigabytes, "
             "`1 GB = 10⁹ B`, because that is what egress is billed in and mixing it "
             "with binary gibibytes moves the answer by seven per cent."),
            ("Price it, and state the gap",
             "Multiply by the price per gigabyte and the days. Then compute what the "
             "request hit rate would have predicted and report both, because the "
             "difference between them is the single most useful sentence in the "
             "estimate."),
        ],
        "worked": {
            "title": "Twenty objects, size proportional to rank, 50 000 GB a day",
            "intro": [
                "Two hit rates off the same ranks, and then the invoice each of them "
                "would have produced."
            ],
            "lines": [
                "N = 20 objects,  s = 1,  edge holds the top C = 4,  size ∝ rank¹ (b = 1)",
                "",
                "request hit rate = H(4,1)/H(20,1) = 6466460/11167027 = 57.91%",
                "",
                "byte hit rate: weights are i^(b−s) = i⁰ = 1, so every rank weighs the same",
                "               = C/N = 4/20 = 1/5 = 20.00%           b = s exactly",
                "",
                "gap  57.91 − 20.00 = 37.91 points",
                "",
                "total edge egress 50 000 GB/day,  origin price 2 ¢/GB",
                "  origin = (1 − 1/5) × 50 000       = 40 000 GB/day",
                "  bill   = 40 000 × 30 × $0.02      = $24 000.00",
                "",
                "if you had billed from the request hit rate:",
                "  origin ≈ 21 047 GB/day            bill ≈ $12 627.98",
                "  the forecast would have been barely half the real invoice",
            ],
            "after": [
                "The `b = s` coincidence is worth noticing rather than relying on: at "
                "this catalogue the byte hit rate is exactly the uniform rate `C/N`, "
                "which makes the arithmetic clean and is not a general fact. Move `b` to "
                "`2` and it falls to `4.76%`, taking the bill to `$28 571.43`.",
                "For a faded rehearsal, keep `N = 20` and `s = 1` but set `b = 0`. The "
                "supplied first move is that the two hit rates must now be equal; "
                "confirm that, compute the origin egress and the bill, and say which of "
                "the three cases &mdash; `b = 0`, `b = s`, `b > 0` &mdash; describes a "
                "video CDN and which describes a cache of thumbnails.",
                "The lab draws the share of requests by rank and the share of bytes by "
                "rank as two profiles with the cached prefix shaded in both. The gap "
                "between the two shaded areas is the whole lesson, and setting `b = 0` "
                "closes it.",
            ],
        },
        "quiz_title": "Bytes, requests and invoices",
        "quiz": [
            {"q": "At `N = 20`, `s = 1`, `C = 4` and `b = 1`, the request hit rate is `57.91%`. What is the byte hit rate?",
             "a": ["`57.91%`, since they measure the same cache",
                   "`20.00%`",
                   "`4.76%`",
                   "`42.09%`, the complement"],
             "c": 1,
             "why": "With `b = s` the size weights are `i⁰ = 1`, so every rank carries "
                    "the same bytes and the byte hit rate is exactly `C/N = 4/20 = 20%`. "
                    "They would be equal only at `b = 0`; `4.76%` is the answer at "
                    "`b = 2`, where large objects dominate the byte totals even more."},
            {"q": "A CDN serves `50 000 GB` a day with a `20%` byte hit rate. Origin egress costs two cents a gigabyte. What is the thirty-day bill?",
             "a": ["`$24 000.00`", "`$30 000.00`", "`$6 000.00`", "`$12 627.98`"],
             "c": 0,
             "why": "`(1 − 0.20)(50 000) = 40 000 GB/day` to the origin, times thirty "
                    "days times two cents is `$24 000.00`. `$6 000` bills the `20%` that "
                    "was <em>cached</em>, `$30 000` bills the whole egress, and "
                    "`$12 627.98` is what the request hit rate of `57.91%` would have "
                    "predicted &mdash; the error this lesson exists to prevent."},
            {"q": "Why is the byte hit rate usually below the request hit rate on a CDN?",
             "a": ["Because caches evict large objects first",
                   "Because the popular objects tend to be the small ones, so cached hits carry fewer bytes than their share of requests",
                   "Because byte counting includes protocol overhead",
                   "Because the origin compresses what it serves"],
             "c": 1,
             "why": "Object size tends to grow with rank &mdash; `b > 0` &mdash; so the "
                    "cheap-to-cache objects are also the ones that carry few bytes. The "
                    "formula makes this exact: the byte hit rate is the same harmonic "
                    "ratio at exponent `s − b`, and at `b = 0` the two rates coincide, "
                    "which is the control."},
        ],
        "mistakes": [
            ("Using the request hit rate to forecast egress",
             "At `N = 20`, `s = 1`, `C = 4` and `b = 1` the request rate is `57.91%` and "
             "the byte rate is `20.00%`: the bill is `$24 000` and the forecast made "
             "from the wrong rate is `$12 627.98`. Because `b > 0` is the normal shape "
             "of an edge workload, this error is one-sided and always optimistic."),
            ("Assuming the two rates must be close",
             "They are equal only at `b = 0`, where every object is the same size. "
             "Nothing bounds the gap otherwise: at `b = 2` on the same catalogue the "
             "byte hit rate is `4.76%` against a request hit rate of `57.91%`, a factor "
             "of twelve. Check the size profile before assuming either number stands in "
             "for the other."),
            ("Mixing decimal and binary gigabytes",
             "Egress is billed in decimal units, `1 GB = 10⁹ B`. Computing origin volume "
             "in gibibytes and pricing it as gigabytes overstates or understates the "
             "bill by about seven per cent, which is small enough to survive review and "
             "large enough to matter on a `$24 000` line."),
        ],
        "standard": ("Finish when “which hit rate is that” is the first thing you ask a CDN dashboard.",
                     "You should be able to distinguish a request hit rate from a byte "
                     "hit rate, compute the second from a size profile, turn it into "
                     "origin gigabytes per day and a monthly bill, and state the gap "
                     "between the two forecasts as the reason the distinction is worth "
                     "making."),
        "note": 'That is the course: a cache is a miss rate, and every question about one &mdash; backend load, latency, size, policy, staleness, bursts, writes, levels and bytes &mdash; is arithmetic on that number. What it cannot tell you is what happens when a component is simply gone, which is where “Nines and Downtime” starts the next course.',
    },
]
