"""Course 6, lessons 01-07 - what replication costs, then quorums and majorities."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "reads-scale-writes-do-not",
        "title": "Reads Scale, Writes Do Not",
        "module": "What it costs",
        "one_line": "Compute the four multipliers a replication factor buys, and the ceiling the read/write ratio puts on them.",
        "summary": (
            "Adding replicas buys read capacity and nothing else. `N` copies serve `N×` "
            "the reads, accept `1×` the writes however many you buy, apply `N×` the write "
            "work and hold `N×` the bytes. What a real mixed workload gains is "
            "`1/(w + r/N)`, and the ceiling on that is `1 + ρ` — a property of the "
            "read/write ratio rather than of the fleet, which is why a write-heavy "
            "service gets nothing from replication and pays `N` times for it."
        ),
        "key": [
            "N replicas:  N× reads,  1× writes,  N× write work,  N× storage",
            "ρ reads per write:  w = 1/(1 + ρ) writes,  r = ρ/(1 + ρ) reads",
            "speed-up(N) = 1 / (w + r/N)        only the read share divides",
            "ceiling = 1 + ρ                    set by the mix, never reached",
            "N = 3, ρ = 9:  2.5× of a ceiling of 10×, for 3× the write work",
        ],
        "key_label": "Four multipliers, and the one that never moves",
        "concepts_intro": (
            "Three sentences, and the third decides whether the replication factor was "
            "worth buying at all."
        ),
        "concepts": [
            ("Every replica applies every write",
             "A copy that skipped a write would not be a copy. So each write is applied "
             "`N` times, once per replica, and the rate at which the cluster can accept "
             "writes is exactly the rate at which one machine can apply them — `1×`, at "
             "`N = 3` and at `N = 30`. The `N×` that replication is sold on is the read "
             "side and only the read side."),
            ("Only the read stream divides",
             "Reads can be served by any replica that holds the data, so `N` replicas "
             "serve `N` times the reads of one. That is a genuine multiplier and it is "
             "the reason to replicate. It is also the only one of the four numbers that "
             "moves in your favour: the write work and the storage move against you at "
             "exactly the same rate."),
            ("The ceiling belongs to the workload, not to the fleet",
             "If a fraction `w` of operations are writes and `r = 1 − w` are reads, the "
             "cluster does `1/(w + r/N)` times the work of one machine. Send `N` to "
             "infinity and the reads cost nothing, leaving `1/w = 1 + ρ`. At nine reads "
             "per write that ceiling is `10×`; at one read per write it is `2×`; at zero "
             "reads it is `1×`. No number of replicas raises it, because every replica "
             "still applies every write."),
        ],
        "read_title": "What a replication factor buys, and what it bills",
        "read_intro": (
            "The four multipliers, the speed-up a real mix actually gets, and the ceiling "
            "that no fleet size reaches."
        ),
        "body": [
            ("def", ("Replication factor, and the four multipliers",
                     "A <strong>replication factor</strong> of `N` keeps `N` complete "
                     "copies of the data. Against a single machine it multiplies "
                     "<strong>read capacity</strong> by `N`, <strong>write capacity</strong> "
                     "by `1`, <strong>write work</strong> by `N` and <strong>storage</strong> "
                     "by `N`. The first is the benefit; the other three are the bill.")),
            ("p", "The asymmetry is not an implementation detail that a better design "
                  "removes. It follows from what a replica is. A read is answered by one "
                  "copy, so copies divide the read stream between them; a write must "
                  "reach every copy, so copies multiply the write stream instead."),
            ("math", [
                "one replica serves 1000 ops/s,  ρ = 9 reads per write",
                "",
                " N    read capacity    write capacity    write work    storage",
                " 1     1000 reads/s     1000 writes/s        1×           1×",
                " 2     2000             1000                 2×           2×",
                " 3     3000             1000                 3×           3×",
                " 4     4000             1000                 4×           4×",
                "",
                "column three is constant by construction, not by coincidence",
            ]),
            ("p", "Neither of the first two columns is what the cluster serves, because a "
                  "real workload is a mix. The read capacity is what you would get if "
                  "every operation were a read, and the write capacity is what you would "
                  "get if every operation were a write. The mix decides where between "
                  "them you land."),
            ("h3", "The mix decides, and it sets a ceiling"),
            ("math", [
                "at ρ = 9 reads per write:  w = 1/10 of the ops are writes",
                "                           r = 9/10 are reads",
                "",
                "speed-up(N) = 1 / (w + r/N)",
                "",
                "  N = 1    1 / (1/10 + 9/10)      = 1×",
                "  N = 3    1 / (1/10 + 3/10)      = 1/(2/5)   = 2.5×",
                "  N = 12   1 / (1/10 + 3/40)      = 1/(7/40)  = 5.714…×",
                "  N → ∞    1 / (1/10)             = 10×       = 1 + ρ",
            ]),
            ("p", "The shape is the one Scaling Laws and Cost will name: a serial part "
                  "that no amount of parallelism divides. Here the serial part is the "
                  "write, and it is serial in a precise sense — every machine does all of "
                  "it. Three replicas at nine reads per write reach `2.5×` of a possible "
                  "`10×`, and the remaining nine machines in the world cannot close that "
                  "gap."),
            ("example", ("The write-heavy service",
                         "At `ρ = 0` — every operation a write — `w = 1`, so "
                         "`speed-up(N) = 1/(1 + 0) = 1×` at every `N`, and the ceiling "
                         "`1 + ρ` is `1×` as well. Three replicas serve exactly what one "
                         "served, for three times the storage and three times the write "
                         "work. This is not a corner case: an append-only ingest path, a "
                         "metrics writer or an audit log can sit very close to it, and "
                         "replicating one of those buys durability and availability and "
                         "no throughput whatsoever. Those are good reasons to replicate. "
                         "They are not this reason.")),
            ("p", "So the honest report of a replication factor is four numbers and a "
                  "ratio, not one number. “We tripled the replicas” is a statement about "
                  "the storage bill; whether it is also a statement about throughput "
                  "depends entirely on `ρ`, and `ρ` is a measurement of the workload that "
                  "Capacity Estimation already taught you to take."),
        ],
        "lab": ("replica", {
            "mode": "fanout",
            "panel_title": "Set the replication factor and the mix",
            "panel_intro": "The four multipliers, the cluster throughput and the ceiling "
                           "are all computed from `N` and the read/write ratio. Move `ρ` "
                           "to zero and watch the speed-up collapse to `1×` at every "
                           "replication factor while the storage column keeps climbing.",
        }),
        "steps_title": "Pricing a replication factor",
        "steps_intro": (
            "The ratio comes first. Every number after it is arithmetic, and every "
            "argument about whether replication helped is really an argument about `ρ`."
        ),
        "steps": [
            ("Measure the read/write ratio before anything else",
             "`ρ` is reads per write on the workload you actually have, not the one in "
             "the design document. A cache in front of the database removes reads and "
             "lowers `ρ`, which lowers the ceiling; a fan-out that turns one user action "
             "into twenty reads raises it. Take this number from a trace."),
            ("Write the four multipliers down separately",
             "`N×` reads, `1×` writes, `N×` write work, `N×` storage. Keeping them apart "
             "is what stops the read multiplier from being quoted as though it were the "
             "cluster's."),
            ("Compute the speed-up, and put the ceiling beside it",
             "`1/(w + r/N)` against `1 + ρ`. Two numbers, always together: the second "
             "says how much of the possible gain the first one is, and how much buying "
             "more machines could ever add."),
            ("Charge the write work and the storage against the gain",
             "`N` times the bytes and `N` times the write applications are paid whether "
             "or not the reads arrived. If the speed-up is `2.5×` for a `3×` bill, say "
             "so; that may still be the right trade, but it is a trade and not a win."),
        ],
        "worked": {
            "title": "Three replicas at nine reads per write",
            "intro": [
                "One machine serves a thousand operations a second. The workload is nine "
                "reads for every write. Two more machines are added. The question is what "
                "each of the four currencies did.",
            ],
            "lines": [
                "one replica        1000 ops/s",
                "N = 3              ρ = 9 reads per write",
                "",
                "read capacity      3 × 1000 = 3000 reads/s",
                "write capacity           1000 writes/s      at every N",
                "write work         3×    every replica applies every write",
                "storage            3×    the bytes, three times",
                "",
                "the mix            w = 1/10 writes,  r = 9/10 reads",
                "speed-up           1 / (1/10 + (9/10)/3)",
                "                 = 1 / (1/10 + 3/10)",
                "                 = 1 / (2/5) = 5/2 = 2.5×",
                "",
                "cluster            2.5 × 1000 = 2500 ops/s",
                "                   of which 2250 reads/s and 250 writes/s",
                "",
                "ceiling            1 + ρ = 10×, and 2.5× is a quarter of it",
                "N = 12             1 / (1/10 + (9/10)/12) = 40/7 = 5.714…×",
            ],
            "after": [
                "Two and a half times the work for three times the storage and three "
                "times the write applications. That is a defensible trade and it is not "
                "the `3×` the replication factor suggests, because a tenth of the "
                "operations were never going to divide.",
                "The last line is the one that changes decisions. Going from three "
                "replicas to twelve — four times the fleet — takes the speed-up from "
                "`2.5×` to about `5.71×`, a little over double, and the ceiling is still "
                "`10×`. Replication is subject to diminishing returns that are set by the "
                "workload, and the way to raise the ceiling is to change `ρ`, which means "
                "caching or batching the writes, not buying machines.",
                "For a faded rehearsal, take the same service at `ρ = 2` reads per write. "
                "The supplied first move is `w = 1/3`, so the ceiling is `3×`. Compute the "
                "speed-up at `N = 3` and at `N = 12`, say what fraction of the ceiling "
                "each reaches, and state the storage bill beside each before you check "
                "them in the lab.",
            ],
        },
        "quiz_title": "Four currencies, one ratio",
        "quiz": [
            {"q": "One replica serves `1000` ops/s and the workload is nine reads per write. You add two more replicas. What does the cluster serve?",
             "a": ["`1000` ops/s", "`2500` ops/s", "`3000` ops/s", "`10 000` ops/s"],
             "c": 1,
             "why": "`1/(1/10 + (9/10)/3) = 2.5`, so `2500` ops/s. `3000` is the read "
                    "capacity — what three replicas would serve if every operation were a "
                    "read. `10 000` is the ceiling `1 + ρ`, which no replication factor "
                    "reaches. `1000` is the write capacity, which is what the cluster "
                    "would serve if every operation were a write."},
            {"q": "Same three replicas. What has happened to the rate at which the cluster can accept writes?",
             "a": ["It tripled, to `3000` writes/s",
                   "It is unchanged at `1000` writes/s",
                   "It fell to a third, because each write now costs three applications",
                   "It rose by the read/write ratio, to `9000` writes/s"],
             "c": 1,
             "why": "Every replica applies every write, so the cluster accepts writes at "
                    "the rate one machine applies them — unchanged. It did not fall "
                    "either: the three applications happen on three machines in parallel, "
                    "not three times on one. What tripled is the total write work being "
                    "done, which is why the bill went up while the capacity did not."},
            {"q": "Two services, each `1000` ops/s per replica, replicated three ways. One runs at `ρ = 9` reads per write, the other at `ρ = 1`. Which gains more, and what caps each?",
             "a": ["`ρ = 9`, reaching `2.5×` against a ceiling of `10×`; `ρ = 1` reaches `1.5×` against a ceiling of `2×`",
                   "`ρ = 1`, because fewer reads means less work to divide",
                   "Neither — both reach `3×`, because both have three replicas",
                   "`ρ = 9`, but only because it is running on more machines"],
             "c": 0,
             "why": "`1/(1/10 + 3/10) = 2.5` and `1/(1/2 + 1/6) = 1.5`, with ceilings "
                    "`1 + ρ` of `10×` and `2×`. The third option is the misconception this "
                    "lesson exists to break: `N` replicas give `N×` reads, not `N×` "
                    "throughput, and a mixed workload never reaches the read multiplier. "
                    "The fourth is wrong on its face — both are running three machines."},
        ],
        "mistakes": [
            ("Quoting `N×` for the cluster when it is `N×` for the reads only",
             "The read capacity and the cluster throughput are different numbers and they "
             "differ by the mix. At `ρ = 9` and `N = 3` they are `3000` and `2500`; at "
             "`ρ = 1` they are `3000` and `1500`; at `ρ = 0` they are `3000` and `1000`. "
             "Any capacity plan that used the first number has over-provisioned its "
             "confidence and under-provisioned its machines."),
            ("Forgetting that the write work is billed `N` times",
             "Each replica applies the full write stream, so the cluster's total write "
             "work is `N` times one machine's — `N` times the disk writes, `N` times the "
             "index maintenance, `N` times the compaction. It is invisible in a "
             "throughput number and very visible in a bill, and it is the reason a "
             "write-heavy service gets slower per unit of cost as it is replicated."),
            ("Reading the ceiling as something a larger fleet reaches",
             "`1 + ρ` is a limit, not a target. Every replica still applies every write, "
             "so the write share of the work never divides, and the speed-up approaches "
             "`1 + ρ` without arriving. If `2.5×` of a possible `10×` is not enough, the "
             "lever is `ρ` — cache the reads elsewhere, batch the writes — because the "
             "lever `N` has already been most of the way pulled."),
        ],
        "standard": ("Finish when “we added replicas” makes you ask for the read/write ratio before anything else.",
                     "You should be able to state the four multipliers for a given `N` "
                     "without hesitating, compute `1/(w + r/N)` and the ceiling `1 + ρ` "
                     "beside it, say what a write-only workload gains from replication, "
                     "and name the storage and write-work bill in the same sentence as "
                     "the throughput gain."),
        "note": "That prices replication in capacity. It also has a latency, and the next "
                "lesson, “Synchronous Writes Wait for the Slowest”, is where most readers "
                "get a number badly wrong for the first time on this course: asked what "
                "three replicas cost in write latency against one, almost everyone "
                "multiplies, and the write is not waiting for a sum.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "synchronous-writes-wait-for-the-slowest",
        "title": "Synchronous Writes Wait for the Slowest",
        "module": "What it costs",
        "one_line": "Compute a synchronous write's p99 as the maximum of `N − 1` replicas, and price the asynchronous alternative in bytes.",
        "summary": (
            "A write that waits for its followers is acknowledged when the last of them "
            "replies, so its distribution is the maximum of `N − 1` reply times and its "
            "CDF is `F(t)` raised to the power `N − 1`. Maxima do not add: on a real reply "
            "distribution, three replicas cost `24 ms` at the p99 against `16 ms` for one, "
            "while “three replicas cost three times one replica” predicts `48 ms` — "
            "exactly twice the truth. The asynchronous alternative charges no latency and "
            "risks un-replicated bytes instead."
        ),
        "key": [
            "P(acked by t) = F(t)^(N − 1)        the slowest follower, not the average",
            "one replica          p99 = 16 ms",
            "synchronous to 3     p99 = 24 ms    the maximum of 2 followers",
            "“3 replicas cost 3×” predicts 48 ms, exactly 2.00× the truth",
            "asynchronous instead: writes/s × mean lag × bytes, on the leader alone",
        ],
        "key_label": "The maximum of N − 1, and what it is not",
        "concepts_intro": (
            "One rule, one arithmetic fact about powers, and one honest account of what "
            "the alternative costs instead."
        ),
        "concepts": [
            ("The write waits for the last follower, not the typical one",
             "A synchronous write is acknowledged when every follower has acked, so its "
             "wait is the <em>maximum</em> of `N − 1` reply times. Under independence, "
             "`P(max ≤ t) = F(t)^(N − 1)`, because all `N − 1` must land by `t`. The "
             "median follower is irrelevant; the write is held by whichever one is slow "
             "this time, and which one that is changes every request."),
            ("A maximum is a power, and a power is not a product",
             "Raising a number below one to a power pushes it down, but nothing like as "
             "fast as multiplying a time by `N` pushes that up. Here `F(16) = 0.992` for "
             "one replica and `0.992² = 0.984064` for two, which is still close to one — "
             "so the p99 moves from `16 ms` to `24 ms`, not to `48 ms`. The penalty for "
             "replication is real and it is a fraction of the one intuition charges."),
            ("Asynchronous does not remove the cost, it changes the currency",
             "Replicating in the background removes the wait entirely and puts "
             "acknowledged-but-unreplicated data at risk instead: `write rate × mean lag "
             "× bytes per write`. At `2000` writes/s, a mean lag of `3.536 ms` and `400` "
             "bytes a write that is about `2.83 kB` living on the leader and nowhere "
             "else. The trade is latency against a durability window, and both sides of "
             "it are computable."),
        ],
        "read_title": "The distribution of the slowest follower",
        "read_intro": (
            "Where `F(t)^(N − 1)` comes from, what it does to a p99, and what the "
            "asynchronous alternative puts at risk instead."
        ),
        "body": [
            ("def", ("Synchronous write, and its acknowledged-by distribution",
                     "A <strong>synchronous write</strong> is acknowledged to the client "
                     "only after every follower has applied it. If each follower's reply "
                     "time is independent with CDF `F`, the write is acknowledged by `t` "
                     "with probability `F(t)^(N − 1)`, the CDF of the "
                     "<strong>maximum</strong> of the `N − 1` followers.")),
            ("p", "Independence is a real assumption and it is named here rather than "
                  "buried. Two replicas sharing a rack switch, a hypervisor or a garbage "
                  "collector do not fail to reply independently, and this lesson's "
                  "arithmetic describes replicas that do."),
            ("math", [
                "one replica's ack time, as ms:weight over a total weight of 1000",
                "",
                "   t    weight    F(t)      F(t)²  = P(both followers acked by t)",
                "   2      600     0.600     0.360000",
                "   4      300     0.900     0.810000",
                "   8       70     0.970     0.940900",
                "  16       22     0.992     0.984064",
                "  24        6     0.998     0.996004",
                "  40        2     1.000     1.000000",
                "",
                "p99 of one replica   = 16 ms     first t with F(t)  ≥ 0.99",
                "p99 of the maximum   = 24 ms     first t with F(t)² ≥ 0.99",
            ]),
            ("p", "Read the fourth row carefully, because it is the whole lesson. One "
                  "replica is done by `16 ms` in `99.2%` of cases. Two replicas are both "
                  "done by `16 ms` in `98.4064%` of cases — a little worse, not twice as "
                  "bad — and that shortfall against `99%` is what pushes the p99 out one "
                  "step, to `24 ms`."),
            ("h3", "Why three replicas do not cost three times one"),
            ("math", [
                "N = 3, so the write waits for the slowest of 2 followers",
                "",
                "  the claim      3 × 16 ms  = 48 ms",
                "  the truth                   24 ms",
                "  ratio          48 / 24    = 2.00× too high",
                "",
                "and the mean is not the story either",
                "  mean ack, one replica          = 3.536 ms",
                "  mean wait, slowest of two      = 4.704224 ms",
                "  p99 wait, slowest of two       = 24 ms",
            ]),
            ("p", "The mean wait rises by about a third and the p99 rises by half, while "
                  "the multiplicative claim charges three times. The reason is that "
                  "latencies of parallel requests do not add — only latencies of "
                  "<em>sequential</em> requests add. Three replicas contacted one after "
                  "another really would cost something like `3×`; three contacted at once "
                  "cost the slowest of them."),
            ("example", ("The asynchronous alternative, priced in bytes",
                         "Drop the wait and replicate in the background. The write's "
                         "latency becomes the leader's alone, and the data that has been "
                         "acknowledged to a client but reached no other machine is "
                         "`rate × lag × bytes`: at `2000` writes/s, a mean lag of "
                         "`3.536 ms` and `400` bytes a write, `2000 × 0.003536 × 400 ≈ "
                         "2828` bytes, about `2.83 kB`. If the leader's disk is lost in "
                         "that instant, those writes are gone and their clients were told "
                         "they succeeded. That is the durability window, it is small "
                         "here, and it is a number rather than a feeling.")),
            ("p", "Neither option is free and both are computable, which is the useful "
                  "position to argue a design from: `8 ms` added to the p99 of every "
                  "write, or `2.83 kB` of acknowledged data living in one place. Which "
                  "is worse is a question about the business; which is which is a "
                  "question this page answers."),
        ],
        "lab": ("replica", {
            "mode": "sync",
            "panel_title": "Set the replicas and their reply times",
            "panel_intro": "The maximum's distribution is enumerated at every attainable "
                           "time rather than sampled, so both percentiles are exact. Take "
                           "`N` to 5 and then to 9 and watch how slowly the p99 moves "
                           "against what the claim in red is charging.",
        }),
        "steps_title": "Costing a synchronous write",
        "steps_intro": (
            "Four steps, and the third is the one that separates this from the arithmetic "
            "most people do in their heads."
        ),
        "steps": [
            ("Get one replica's reply distribution, not its average",
             "A mean reply time cannot answer a question about a p99, and a maximum is "
             "almost entirely a question about the tail. What you need is the "
             "distribution, or at least several of its percentiles."),
            ("Count the followers, which is `N − 1`",
             "The leader's own apply is not a network wait and the write is not waiting "
             "for it in the same sense. Three replicas means two followers and an "
             "exponent of two; five replicas means an exponent of four."),
            ("Raise the CDF to that power and read the percentile off the result",
             "`F(t)^(N − 1)` at each attainable `t`, then the smallest `t` where it "
             "reaches `0.99`. Do not multiply a percentile by anything: the percentile of "
             "a maximum is not a function of the percentile of one replica, it is a "
             "function of the whole curve."),
            ("If you choose asynchronous instead, compute the window",
             "`write rate × mean lag × bytes per write` is the acknowledged data that "
             "exists in one place. State it in bytes and in seconds of writes, and say "
             "which failure would lose it."),
        ],
        "worked": {
            "title": "Three replicas, one distribution, and the claim that fails",
            "intro": [
                "A leader and two followers. The per-replica ack time is measured and "
                "written as value:weight pairs. The question is the p99 of a synchronous "
                "write, and the answer the team has already guessed is three times one "
                "replica's.",
            ],
            "lines": [
                "per-replica ack time (ms:weight, total weight 1000)",
                "  2:600,  4:300,  8:70,  16:22,  24:6,  40:2",
                "",
                "F(t)      2 → 600/1000 = 0.600      16 → 992/1000 = 0.992",
                "          4 → 900/1000 = 0.900      24 → 998/1000 = 0.998",
                "          8 → 970/1000 = 0.970      40 →              1",
                "",
                "N = 3  ⟹  wait for the maximum of N − 1 = 2 followers",
                "P(acked by t) = F(t)²",
                "",
                "  t = 16    0.992² = 0.984064    < 0.99",
                "  t = 24    0.998² = 0.996004    ≥ 0.99      p99 = 24 ms",
                "",
                "one replica       p99 = 16 ms",
                "three replicas    p99 = 24 ms        +8 ms, or 1.5×",
                "“three times one replica”  = 48 ms   — 2.00× the truth",
                "",
                "asynchronous instead, at 2000 writes/s and 400 B a write",
                "  2000 × 3.536 ms × 400 B / 1000 = 2828 B ≈ 2.83 kB at risk",
            ],
            "after": [
                "The `24 ms` is not a small penalty and nobody should pretend it is: half "
                "as much again on the p99 of every write is a real cost, and it is the "
                "price of not having an unreplicated window. What it is not is `48 ms`, "
                "and a team that budgeted `48 ms` has given up a design option on the "
                "strength of arithmetic that was never right.",
                "Notice which part of the distribution did the work. The move from `16` "
                "to `24` happened because `0.992²` fell below `0.99`, a shortfall of "
                "about eight thousandths. Everything below the `99th` percentile — the "
                "`600` weight at `2 ms`, the `300` at `4 ms` — contributed nothing at all "
                "to the answer. Tail questions are answered by tails.",
                "For a faded rehearsal, take `N` to `5` and then to `9` on the same "
                "distribution. The supplied first move is that the exponents are `4` and "
                "`8`, so the quantities to test are `0.998⁴` and `0.998⁸`. Predict both "
                "p99s before computing them, then check both in the lab, and say in one "
                "sentence why one of them did not move at all.",
            ],
        },
        "quiz_title": "Maxima, and what they are not",
        "quiz": [
            {"q": "One replica's p99 is `16 ms`, and `F(16) = 0.992`, `F(24) = 0.998`. What is the p99 of a write synchronised to three replicas?",
             "a": ["`16 ms`", "`24 ms`", "`32 ms`", "`48 ms`"],
             "c": 1,
             "why": "Two followers, so the acknowledged-by probability is `F(t)²`. "
                    "`0.992² = 0.984064`, below `0.99`, so `16 ms` is not enough; "
                    "`0.998² = 0.996004`, so `24 ms` is. `48 ms` is `3 × 16`, the claim "
                    "this lesson refutes, and `32 ms` is `2 × 16`, the same mistake with "
                    "the follower count."},
            {"q": "Why is the synchronous write's p99 not `N` times one replica's p99?",
             "a": ["Because replicas run faster when there are more of them",
                   "Because the write waits for the maximum of `N − 1` independent times, and a maximum is a power of the CDF rather than a sum",
                   "Because the p99 is an average, and averages do not add",
                   "Because only one follower is actually contacted"],
             "c": 1,
             "why": "Requests made in parallel are resolved by their maximum; only "
                    "requests made in sequence add. `P(max ≤ t) = F(t)^(N − 1)`, and "
                    "raising a number just below one to a small power barely moves it. "
                    "The p99 is not an average, and all `N − 1` followers really are "
                    "contacted — that is exactly why the maximum is the right statistic."},
            {"q": "You choose asynchronous replication instead, at `2000` writes/s, a mean lag of `3.536 ms` and `400` bytes a write. How much acknowledged data lives in one place?",
             "a": ["None — the writes were acknowledged, so they are safe",
                   "About `2.83 kB`, on the leader and nowhere else",
                   "`800 kB`, one full second of writes",
                   "About `2.83 MB`"],
             "c": 1,
             "why": "`rate × lag × bytes = 2000 × 0.003536 s × 400 B ≈ 2828 B`. The first "
                    "option is the misconception: acknowledged is a statement about the "
                    "client's request, not about how many machines hold the data. "
                    "`800 kB` is a whole second of writes, which is what you get by "
                    "treating the lag as one second; `2.83 MB` is a thousand times too "
                    "large."},
        ],
        "mistakes": [
            ("Adding replica latencies together",
             "Three replicas contacted in parallel cost the slowest of them, not the sum "
             "of them. The sum is right only for sequential calls — a leader that "
             "forwards to follower one, waits, then forwards to follower two. If your "
             "system does that, `3×` is the correct arithmetic and the fix is to fan out "
             "rather than to accept the latency."),
            ("Answering a tail question with a mean",
             "The mean wait for the slowest of two here is `4.704224 ms` and the p99 is "
             "`24 ms`, a factor of five apart. A maximum concentrates whatever mass the "
             "distribution has in its tail, so the mean of the maximum tells you almost "
             "nothing about the percentile a client experiences. Carry the distribution, "
             "not a summary of it."),
            ("Taking the independence assumption as free",
             "`F(t)^(N − 1)` assumes the followers are slow independently. Positively "
             "correlated replicas — a shared switch, a shared host, a synchronised "
             "compaction — have a maximum closer to a single replica's own time, so this "
             "arithmetic is pessimistic; but a shared cause of slowness also shifts each "
             "replica's own distribution, and then neither the exponent nor the measured "
             "`F` describes the system you have. Where you can, measure the maximum "
             "directly and compare it with what the model predicts."),
        ],
        "standard": ("Finish when “three replicas cost three times one replica” sounds like an arithmetic error rather than a rule of thumb.",
                     "You should be able to raise a measured CDF to the power `N − 1`, "
                     "read a p99 off the result, say how far the multiplicative claim is "
                     "from it, compute the asynchronous alternative's window in bytes, "
                     "and name the independence assumption the exponent rests on."),
        "note": "Both options on this page leave something behind. The synchronous write "
                "leaves a longer p99; the asynchronous one leaves a follower that does not "
                "yet have the data — and a reader who reaches that follower gets the old "
                "value. “Replication Lag and Stale Reads” turns that into a probability "
                "you can read off a distribution, and it is the number behind every "
                "complaint that begins “I saved it and it did not save”.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "replication-lag-and-stale-reads",
        "title": "Replication Lag and Stale Reads",
        "module": "What it costs",
        "one_line": "Read the probability that a follower read is stale off a lag distribution, at a chosen delay and at the mean.",
        "summary": (
            "A read issued `t` after a write is stale exactly when the follower's lag "
            "exceeds `t`, so `P(stale) = P(lag > t)` — a tail, and nothing else. On a "
            "measured lag distribution a read at `50 ms` is stale with probability "
            "`2/25`, and a read at the <em>mean</em> lag of `31.45 ms` is still stale one "
            "time in five. Read-your-writes and monotonic reads are the two guarantees "
            "that fail on precisely this mass."
        ),
        "key": [
            "P(stale at t) = P(lag > t)        the tail past t, and nothing else",
            "t = 50 ms:  2/25 = 8%             at 12 000 reads/s, 960 stale reads/s",
            "mean lag = 31.45 ms               P(stale at the mean) = 1/5",
            "99% fresh needs 250 ms            99.9% fresh needs 400 ms",
            "read-your-writes and monotonic reads fail on exactly this mass",
        ],
        "key_label": "The tail past the read delay",
        "concepts_intro": (
            "Staleness is one subtraction away from a distribution you can measure. The "
            "difficulty is entirely in which number people reach for instead."
        ),
        "concepts": [
            ("A stale read is a tail event, and the tail is the whole answer",
             "The follower has the write if its lag is at most `t`, and does not if the "
             "lag is more. So `P(stale) = P(lag > t)` — the sum of the probabilities "
             "above `t` and no other part of the distribution. On the measured lag here, "
             "a read `50 ms` after the write lands in `2/25` of cases on a follower that "
             "has not caught up."),
            ("The mean is the wrong question about a tail",
             "The mean lag on this distribution is `31.45 ms`, and the mass strictly "
             "above `31.45 ms` is `200` parts in `1000`. Waiting for the mean therefore "
             "leaves one read in five stale, because a mean is a balance point and not a "
             "deadline. Any lag distribution with a tail behaves like this, and lag "
             "distributions are all tail."),
            ("Two named guarantees fail on exactly this mass",
             "<strong>Read-your-writes</strong> says a client that wrote sees its own "
             "write; it fails when that client's next read lands on a follower still in "
             "the tail. <strong>Monotonic reads</strong> says a client never sees time go "
             "backwards; it fails when a client is moved from a caught-up follower to a "
             "lagging one. Both are statements about this one number, which is why "
             "measuring it is what makes them arguable."),
        ],
        "read_title": "Lag, the tail, and the two guarantees that live in it",
        "read_intro": (
            "What staleness is a probability of, why the mean cannot answer it, and what "
            "the tail costs at a real read rate."
        ),
        "body": [
            ("def", ("Replication lag and a stale read",
                     "<strong>Replication lag</strong> is the delay between a write "
                     "committing on the leader and being visible on a follower. A read of "
                     "that follower issued `t` after the write is <strong>stale</strong> "
                     "if it returns the value from before the write, which happens "
                     "exactly when the lag exceeds `t`. So "
                     "`P(stale at t) = P(lag > t)`.")),
            ("p", "Lag is not a constant and it is not well described by its average. It "
                  "is a distribution with a long right tail, produced by whatever the "
                  "follower is occasionally busy doing — a compaction, a slow disk, a "
                  "network hiccup, a burst of writes it is still applying."),
            ("math", [
                "follower lag, as ms:weight over a total weight of 1000",
                "",
                "  lag (ms)   weight    P(lag ≤ this)    P(lag > this)",
                "     10        500        1/2              1/2",
                "     25        300        4/5              1/5",
                "     50        120       23/25             2/25",
                "    120         60       49/50             1/50",
                "    250         15      199/200            1/200",
                "    400          5         1                0",
                "",
                "a read 50 ms after the write is stale with probability 2/25 = 8%",
            ]),
            ("p", "Every figure in that table is a sum of weights divided by `1000`. "
                  "There is no model being fitted and no parameter being estimated: if "
                  "you can measure the lag, the staleness probability at any delay is a "
                  "column of the same table."),
            ("h3", "Why the mean cannot answer the question"),
            ("math", [
                "mean lag = (10·500 + 25·300 + 50·120 + 120·60 + 250·15 + 400·5) / 1000",
                "         = 31 450 / 1000  =  629/20  =  31.45 ms",
                "",
                "P(lag > 31.45 ms) = (120 + 60 + 15 + 5)/1000 = 200/1000 = 1/5",
                "",
                "  wait for the mean       one read in five is stale",
                "  wait 250 ms             one read in a hundred",
                "  wait 400 ms             none, on this distribution",
            ]),
            ("p", "“Average lag is fifty milliseconds, so reads after fifty milliseconds "
                  "are fine” is the sentence this lesson exists to break, and the break is "
                  "not subtle: at the mean of this distribution, twenty per cent of reads "
                  "are wrong. Half the mass sits at `10 ms` and pulls the average down "
                  "while the `120`, `250` and `400` millisecond events — the ones that "
                  "actually produce the complaint — sit far above it."),
            ("example", ("What eight per cent costs at twelve thousand reads a second",
                         "A service serving `12 000` follower reads a second with a "
                         "read-after-write delay of `50 ms` produces `12 000 × 2/25 = 960` "
                         "stale reads every second. That is the number to put in front of "
                         "anyone who has described the problem as intermittent. It is not "
                         "intermittent; it is eight per cent, all day, and the reason it "
                         "is reported as intermittent is that most reads are not of "
                         "something the reader just wrote.")),
            ("p", "The repairs are all versions of the same idea: make the read wait, or "
                  "make it go somewhere that has the data. Route a client's reads to the "
                  "leader for a while after it writes; pin a session to one follower so "
                  "monotonic reads hold even though read-your-writes may not; or carry the "
                  "write's version with the client and have the follower wait until it has "
                  "reached that version. Each costs something, and this distribution is "
                  "what says how much of it you need."),
        ],
        "lab": ("replica", {
            "mode": "lag",
            "panel_title": "Set the lag distribution and the read delay",
            "panel_intro": "The shaded mass is the answer: every bar to the right of the "
                           "red line is a read that sees the old value. The amber line is "
                           "the mean, drawn so that the gap between it and the tail is "
                           "visible rather than argued about.",
        }),
        "steps_title": "Turning a lag measurement into a staleness probability",
        "steps_intro": (
            "The read delay is a design choice and the lag is a measurement. Keeping them "
            "apart is most of the discipline here."
        ),
        "steps": [
            ("Measure the lag as a distribution, not as a gauge",
             "A single lag number on a dashboard is usually a mean or a current value, "
             "and neither answers a staleness question. What you want is a histogram, or "
             "failing that a handful of percentiles including a `p99` and a `p999`."),
            ("State the read delay the question is about",
             "“Stale” is meaningless without a `t`. A page that re-reads immediately "
             "after a write has a `t` of a few milliseconds; one that re-reads after a "
             "redirect and a render has a `t` of a few hundred. These give wildly "
             "different answers from the same distribution."),
            ("Sum the mass strictly above that delay",
             "That sum is `P(stale)`, exactly. Resist substituting the mean, the median "
             "or a percentile for the delay: the question is about a specific `t` you "
             "chose, and the answer is the tail past it."),
            ("Multiply by the read rate before reporting it",
             "`P(stale)` is easy to dismiss and `960` stale reads a second is not. Report "
             "both, and say which guarantee — read-your-writes or monotonic reads — the "
             "failures will be reported as."),
        ],
        "worked": {
            "title": "A measured lag, and three delays",
            "intro": [
                "The lag of a read replica has been measured for a day and bucketed. The "
                "product question is how long the application must wait after a write "
                "before reading a follower is safe, and “safe” has to be given a number "
                "before it can be answered.",
            ],
            "lines": [
                "lag (ms:weight, total 1000)",
                "  10:500,  25:300,  50:120,  120:60,  250:15,  400:5",
                "",
                "cumulative                    tail",
                "  P(lag ≤ 10)  = 1/2          P(lag > 10)  = 1/2",
                "  P(lag ≤ 25)  = 4/5          P(lag > 25)  = 1/5",
                "  P(lag ≤ 50)  = 23/25        P(lag > 50)  = 2/25",
                "  P(lag ≤ 120) = 49/50        P(lag > 120) = 1/50",
                "  P(lag ≤ 250) = 199/200      P(lag > 250) = 1/200",
                "  P(lag ≤ 400) = 1            P(lag > 400) = 0",
                "",
                "delay chosen        P(stale)     at 12 000 reads/s",
                "  31.45 ms (mean)     1/5          2400 stale reads/s",
                "  50 ms               2/25          960 stale reads/s",
                "  250 ms              1/200          60 stale reads/s",
                "  400 ms              0               0",
                "",
                "99% fresh    needs 250 ms       99.9% fresh   needs 400 ms",
            ],
            "after": [
                "The middle column is the deliverable and the right-hand one is what gets "
                "the work scheduled. Nobody argues with `2/25`; everybody argues with "
                "`960` complaints a second, and it is the same statement.",
                "The mean row is there to be looked at. Waiting the average lag — which "
                "sounds like a generous, even wasteful, thing to do — leaves twenty per "
                "cent of reads stale, worse than waiting a flat `50 ms`. That is what it "
                "means for a distribution to be right-skewed, and lag distributions "
                "always are.",
                "For a faded rehearsal, suppose the team cannot wait `250 ms` and proposes "
                "`120 ms` instead. The supplied first move is that the tail past `120` is "
                "`60 + 15 + 5 = 80` parts in `1000`. Wait — check that against the table "
                "before you trust it, state the correct `P(stale)` at `120 ms`, convert it "
                "to stale reads a second at `12 000` reads/s, and say which of the two "
                "guarantees a user would report the failure as.",
            ],
        },
        "quiz_title": "Tails, means and guarantees",
        "quiz": [
            {"q": "On the lag distribution above, a client reads a follower `50 ms` after its write. With what probability is the read stale?",
             "a": ["`2/25`", "`23/25`", "`1/2`", "`1/5`"],
             "c": 0,
             "why": "The tail past `50 ms` is `60 + 15 + 5 = 80` parts in `1000`, which is "
                    "`2/25`. `23/25` is its complement — the probability the read is "
                    "fresh. `1/2` is the tail past `10 ms` and `1/5` is the tail past "
                    "`25 ms`, both of which answer a different delay."},
            {"q": "The mean lag of that distribution is `31.45 ms`. What fraction of reads issued `31.45 ms` after a write are stale?",
             "a": ["None — that is what the mean is for",
                   "About half, since the mean splits the distribution",
                   "`20%`",
                   "`8%`"],
             "c": 2,
             "why": "The mass strictly above `31.45 ms` is `120 + 60 + 15 + 5 = 200` parts "
                    "in `1000`. “About half” confuses the mean with the median — the "
                    "median here is `10 ms`, because half the mass sits in the first "
                    "bucket. `8%` is the answer at `50 ms`, not at the mean."},
            {"q": "A user saves a form, is redirected, and the next page shows the old value. Which guarantee failed, and what would fix it without changing the lag?",
             "a": ["Monotonic reads; pin the session to one follower",
                   "Read-your-writes; route that client's reads to the leader for a window longer than the lag tail",
                   "Linearizability; add a third replica",
                   "Read-your-writes; raise the replication factor"],
             "c": 1,
             "why": "The client is failing to see its own write, which is exactly "
                    "read-your-writes. Sending that client to the leader — or having the "
                    "follower wait for the version the client carries — fixes it without "
                    "touching the lag distribution. Monotonic reads is the different "
                    "failure where a client sees a value and then an older one; and "
                    "adding replicas changes neither, since staleness is a tail of the "
                    "lag and not a shortage of copies."},
        ],
        "mistakes": [
            ("Using the mean lag as a freshness delay",
             "The mean of a right-skewed distribution sits well inside the mass, not past "
             "it. Here the mean is `31.45 ms` and the tail past it is `20%`, while a "
             "`99%`-fresh read needs `250 ms` — eight times the mean. If you want a "
             "freshness guarantee, the number you need is a high percentile of the lag, "
             "and the mean is not even an approximation of it."),
            ("Quoting the probability without the read rate",
             "`8%` sounds like a rounding error and `960` stale reads a second does not. "
             "They are the same measurement at `12 000` reads/s. Reporting only the "
             "fraction is how a staleness problem gets logged as an intermittent oddity "
             "for a year."),
            ("Assuming a stale read is the only failure",
             "Read-your-writes is the one users notice, but monotonic reads is the one "
             "that produces the incident report nobody can reproduce: a client load "
             "balanced onto a caught-up follower and then onto a lagging one sees a value "
             "and then an <em>older</em> value, with no write in between. That failure is "
             "in the same tail and is fixed by session stickiness rather than by waiting."),
        ],
        "standard": ("Finish when a lag dashboard showing one number reads to you as a missing distribution.",
                     "You should be able to compute `P(lag > t)` from a measured "
                     "distribution at any delay, say why the mean cannot be used as a "
                     "freshness delay, convert the probability into stale reads a second, "
                     "and name which of read-your-writes and monotonic reads a given user "
                     "report corresponds to."),
        "note": "Three lessons have priced replication in capacity, in latency and in "
                "staleness, and all three assumed a reader who talks to one replica. The "
                "rest of the course is about readers and writers who talk to several at "
                "once, starting with “Quorums Overlap” — where a counting argument buys a "
                "guarantee that none of the three numbers so far could.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "quorums-overlap",
        "title": "Quorums Overlap",
        "module": "Quorums",
        "one_line": "Decide whether a configuration overlaps, and compute the minimum overlap it actually guarantees.",
        "summary": (
            "If a read consults `R` nodes and a write reaches `W` of `N`, then `R + W` "
            "node names are drawn from a pool of `N`, and `R + W > N` forces at least "
            "`R + W − N` of them to coincide. That is the pigeonhole principle applied to "
            "machine names, and the bound is attained, which is what makes it the "
            "guarantee rather than merely a limit. It is also strictly less than "
            "consistency, and this lesson says exactly how much less."
        ),
        "key": [
            "R + W > N   ⟹   every read set meets every write set",
            "minimum overlap = R + W − N, and it is attained",
            "N = 3, R = 2, W = 2:   R + W = 4 > 3,  minimum overlap 1",
            "3 read sets × 3 write sets = 9 pairs, none of them disjoint",
            "overlap is a statement about nodes, not about what the reader can tell",
        ],
        "key_label": "The pigeonhole argument, and its limit",
        "concepts_intro": (
            "A counting argument, a check that the count is tight, and a careful statement "
            "of what the argument does not give you."
        ),
        "concepts": [
            ("Pigeonhole, applied to node names",
             "A read set of `R` nodes and a write set of `W` nodes name `R + W` nodes "
             "between them, all drawn from the same `N`. If `R + W > N` they cannot all "
             "be distinct, so at least `R + W − N` names appear in both sets. Nothing "
             "about time, ordering or protocol enters the argument — it is Discrete "
             "Mathematics' pigeonhole principle with nodes as pigeonholes."),
            ("The minimum is attained, so it is the guarantee",
             "A bound that is never reached would be the wrong number to design on. Here "
             "it is reached: at `N = 3, R = 2, W = 2` the lab compares all `9` read-set "
             "and write-set pairs and finds the smallest intersection is exactly `1`, "
             "which is `R + W − N`. So `R + W − N` is what you get in the worst case, and "
             "sizing a design as though you got more is sizing it wrong."),
            ("Overlap says a node saw it, not that the reader can tell",
             "The guarantee is that at least one node in the read set holds the latest "
             "acknowledged write. It does not say the reader can identify which of the "
             "returned values that is, what happens when two writes are concurrent, or "
             "that the whole history looks like it happened at single instants. Those are "
             "separate questions, and “Linearizability by Enumeration” is where the last "
             "of them gets answered."),
        ],
        "read_title": "The overlap bound, and the line it does not cross",
        "read_intro": (
            "A one-line proof, an enumeration that shows the bound is tight, and a careful "
            "account of what a quorum configuration does not buy."
        ),
        "body": [
            ("thm", ("The quorum overlap bound",
                     "Let a write be applied to a set of `W` nodes and a read consult a "
                     "set of `R` nodes, both subsets of the same `N`. If `R + W > N` then "
                     "the two sets intersect, and the intersection contains at least "
                     "`R + W − N` nodes. If `R + W ≤ N` there exist a read set and a "
                     "write set that are disjoint.")),
            ("proof", [
                "The read set and the write set together name `R + W` nodes, counted with "
                "repetition, from a pool of `N` distinct nodes. Each node can be named at "
                "most twice — once by each set — so the number of nodes named by both is "
                "at least `R + W − N`. When `R + W > N` that quantity is positive, so the "
                "sets intersect.",
                "For the converse, if `R + W ≤ N` then the `W` nodes of the write and `R` "
                "further nodes can be chosen from the `N` without reusing any, and those "
                "`R` form a read set disjoint from the write set. Such a read returns no "
                "copy of the write at all.",
            ]),
            ("p", "The theorem is about set membership and it is proved in two lines, "
                  "which is why it is the load-bearing fact in every quorum system. What "
                  "takes care is the second half of the statement: the bound is a "
                  "<em>minimum</em>, and a minimum is only useful if something attains it."),
            ("math", [
                "N = 3 nodes {1, 2, 3},   R = 2,   W = 2",
                "",
                "read sets    {1,2}   {1,3}   {2,3}",
                "write sets   {1,2}   {1,3}   {2,3}",
                "",
                "size of the intersection, over all 9 pairs",
                "",
                "                {1,2}   {1,3}   {2,3}",
                "       {1,2}      2       1       1",
                "       {1,3}      1       2       1",
                "       {2,3}      1       1       2",
                "",
                "smallest entry = 1 = R + W − N, and it occurs in 6 of the 9 pairs",
            ]),
            ("p", "Two thirds of the pairs sit exactly on the bound, so a design that "
                  "assumed a comfortable margin of agreement between the read set and the "
                  "write set has assumed something that is false most of the time. The "
                  "guarantee is one node, and one node is enough — provided the reader "
                  "knows what to do with a set of answers that disagree."),
            ("h3", "What the overlap does not buy"),
            ("p", "The read set contains a node holding the latest acknowledged write. It "
                  "also contains, in general, nodes holding older values, and the reader "
                  "receives all of them without a label saying which is which. Version "
                  "numbers or timestamps are what turn the overlap into an answer, and "
                  "they bring their own difficulties — “Lamport Clocks” and “Physical "
                  "Clocks and Drift” are both about how badly a naive version of that can "
                  "go."),
            ("example", ("Two concurrent writes, and an overlap that decides nothing",
                         "`N = 3, R = 2, W = 2`. Client one writes `x = 1` to `{1,2}`; at "
                         "the same moment client two writes `x = 2` to `{2,3}`. Both "
                         "writes satisfy the configuration and both are acknowledged. A "
                         "reader consulting `{1,3}` sees `1` and `2` and overlaps with "
                         "both write sets, exactly as the theorem promises. The theorem "
                         "has done its job and the reader still does not know which value "
                         "is current, because neither write happened before the other. "
                         "That is a conflict rather than a staleness problem, and it is "
                         "what “Vector Clocks and Concurrency” makes countable and "
                         "“Conflict Resolution, Counted” decides.")),
            ("p", "So the right claim for a `(N, R, W)` configuration with `R + W > N` is: "
                  "no acknowledged write can be missed entirely by a subsequent read. That "
                  "is a real and useful guarantee. It is not “the read returns the current "
                  "value”, and the gap between the two is where most of the remaining "
                  "lessons on this course live."),
        ],
        "lab": ("replica", {
            "mode": "quorum",
            "panel_title": "Set the quorum configuration",
            "panel_intro": "Both families of sets are enumerated and every pair compared, "
                           "so the minimum overlap shown is measured rather than asserted "
                           "from the formula. Drop `R` to `1` and the lab exhibits an "
                           "actual disjoint pair instead of a minimum.",
        }),
        "steps_title": "Deciding a quorum configuration",
        "steps_intro": (
            "Two integers decide it and the third step is where a real design usually goes "
            "wrong — not in the arithmetic, but in what it is asked to mean."
        ),
        "steps": [
            ("Add `R` and `W` and compare with `N`",
             "Strictly greater. `R + W = N` is not the boundary case of a guarantee, it "
             "is the absence of one, and “Sloppy Quorums and the Miss Probability” prices "
             "exactly how absent."),
            ("Compute `R + W − N` and treat it as the worst case",
             "That is the number of nodes the read and write sets are guaranteed to share, "
             "and it is attained. If your design needs two shared nodes — because you "
             "intend to survive one of them being wrong — then `R + W − N ≥ 2` is the "
             "condition, not `R + W > N`."),
            ("Decide where to spend the sum, since only the sum is constrained",
             "`(N, R, W) = (3, 3, 1)` gives fast writes and slow reads; `(3, 1, 3)` the "
             "reverse; `(3, 2, 2)` balances them. All three overlap. Choose by which of "
             "the two paths is hot, using the latency arithmetic of “Quorum Latency: the "
             "W-th Fastest”."),
            ("Say out loud what the overlap does not give you",
             "It gives you a node with the latest acknowledged write in every read set. It "
             "does not give you a way to recognise that node's answer, a resolution for "
             "concurrent writes, or linearizability. Writing that sentence into the design "
             "document is what stops a quorum from being quoted as consistency later."),
        ],
        "worked": {
            "title": "Five nodes, and four configurations",
            "intro": [
                "A five-node cluster, and four proposals on the table. For each one the "
                "question is whether it overlaps at all and, if so, by how much in the "
                "worst case.",
            ],
            "lines": [
                "N = 5",
                "",
                "  R = 3, W = 3    R + W = 6 > 5    minimum overlap  6 − 5 = 1   overlaps",
                "  R = 1, W = 5    R + W = 6 > 5    minimum overlap        1    overlaps",
                "  R = 5, W = 1    R + W = 6 > 5    minimum overlap        1    overlaps",
                "  R = 2, W = 3    R + W = 5 = 5    no guarantee",
                "                  write {1,2,3}, read {4,5}:  intersection empty",
                "",
                "and a configuration with a margin",
                "",
                "  R = 4, W = 4    R + W = 8 > 5    minimum overlap  8 − 5 = 3",
                "                  C(5,4) = 5 read sets, 5 write sets, 25 pairs",
                "                  smallest intersection 3, attained by",
                "                  {1,2,3,4} ∩ {2,3,4,5} = {2,3,4}",
            ],
            "after": [
                "The first three configurations are equally safe and wildly different to "
                "operate. `R = 1, W = 5` cannot tolerate a single node being down for "
                "writes; `R = 5, W = 1` cannot tolerate one being down for reads; "
                "`R = 3, W = 3` tolerates one being down on either path. The overlap "
                "arithmetic is blind to all of that, which is why it is a necessary "
                "condition and never the whole design.",
                "The fourth line is the trap, and it is a popular one because `R + W = N` "
                "looks like a boundary you are standing on rather than one you are outside "
                "of. The exhibited pair settles it: a write to `{1,2,3}` and a read of "
                "`{4,5}` are both legal under that configuration and share nothing.",
                "For a faded rehearsal, take `N = 7` with `R = 3` and `W = 5`. The "
                "supplied first move is `R + W = 8 > 7`, so it overlaps. Compute the "
                "minimum overlap, then find the smallest `R` that keeps the configuration "
                "overlapping if `W` is cut to `4`, and say what that change does to the "
                "read path before you check it in the lab.",
            ],
        },
        "quiz_title": "Overlaps, minimums and what they mean",
        "quiz": [
            {"q": "`N = 5`, `R = 2`, `W = 3`. Is every read guaranteed to see the latest acknowledged write?",
             "a": ["Yes — the minimum overlap is `0`, which is enough",
                   "No — `R + W = 5` is not greater than `5`, and a write to `{1,2,3}` with a read of `{4,5}` shares nothing",
                   "Yes, because `W` is a majority of five",
                   "Only if the read is retried on a different set"],
             "c": 1,
             "why": "The condition is strict. `R + W = N` permits a disjoint pair and the "
                    "example exhibits one. A majority write does guarantee that two "
                    "<em>writes</em> overlap, which is a different and also useful fact, "
                    "but it says nothing about a two-node read. Retrying draws another "
                    "read set that may also miss."},
            {"q": "`N = 7`, `R = 3`, `W = 5`. What is the minimum overlap?",
             "a": ["`1`", "`2`", "`3`", "`8`"],
             "c": 0,
             "why": "`R + W − N = 3 + 5 − 7 = 1`. `8` is `R + W` before subtracting `N`; "
                    "`3` is `R` and `2` would be the answer if `W` were `6`. One shared "
                    "node is the guarantee here, and it is attained."},
            {"q": "A configuration has `R + W > N`. Which statement does the overlap bound actually support?",
             "a": ["Every read returns the value of the most recently completed write",
                   "Every read set contains at least one node holding the latest acknowledged write",
                   "Reads and writes appear to take effect at single instants in real time",
                   "Two concurrent writes cannot both be acknowledged"],
             "c": 1,
             "why": "The theorem is about set membership and that is all it claims. "
                    "Whether the reader can recognise the latest value among the ones it "
                    "receives is a separate question; whether the whole history looks "
                    "instantaneous is linearizability, which “Linearizability by "
                    "Enumeration” turns into a count; and two concurrent writes to "
                    "overlapping sets are both acknowledged routinely, which is the "
                    "conflict that closes this course."},
        ],
        "mistakes": [
            ("Reading `R + W > N` as `R + W ≥ N`",
             "The strictness is the whole condition. At `N = 3`, `R + W = 3` leaves a read "
             "missing the write one time in three, which is not a boundary case of a "
             "guarantee but a coin flip with bad odds. Any configuration you cannot "
             "immediately place on the correct side of that inequality should be written "
             "out and checked."),
            ("Treating `R + W − N` as a lower bound with slack in it",
             "It is attained. At `N = 3, R = W = 2` six of the nine set pairs share "
             "exactly one node, so the worst case is the common case. A design that "
             "quietly relies on two of the read's nodes agreeing needs "
             "`R + W − N ≥ 2`, and must say so."),
            ("Calling a quorum configuration “consistent”",
             "The overlap guarantees that no acknowledged write is missed entirely. It "
             "does not order concurrent writes, does not tell the reader which returned "
             "value is current without version information, and does not make the history "
             "linearizable. Every one of those has cost somebody an outage that the "
             "quorum arithmetic said was impossible, because the arithmetic was answering "
             "a narrower question than the one being asked."),
        ],
        "standard": ("Finish when you can prove the bound in two lines and state, in one more, what it does not give you.",
                     "You should be able to decide any `(N, R, W)` at sight, compute the "
                     "minimum overlap and know it is attained, exhibit a disjoint pair "
                     "when the condition fails, and separate “no acknowledged write is "
                     "missed” from “the read returns the current value”."),
        "note": "The overlap condition constrains `R + W` and leaves you free to choose "
                "where to spend it, and that choice is a latency choice. “Quorum Latency: "
                "the W-th Fastest” computes it — and produces the one result on this "
                "course that most readers refuse to believe until they have worked the "
                "binomial tail themselves.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "quorum-latency",
        "title": "Quorum Latency: the W-th Fastest",
        "module": "Quorums",
        "one_line": "Compute a quorum write's p99 as a binomial tail, and say which way it moves when `N` grows.",
        "summary": (
            "A quorum write is acknowledged when `W` of `N` replicas have replied, so it "
            "waits for an order statistic rather than for everyone: "
            "`P(ack by t) = P(at least W of N replied by t)`, the same binomial tail that "
            "a `k`-of-`n` availability is. Hold `W` fixed and raise `N` and the write gets "
            "<em>faster</em> — `8 ms` at `N = 3`, `4 ms` at `N = 4` — which is the opposite "
            "of what everyone expects, and it quietly breaks the overlap condition on the "
            "way."
        ),
        "key": [
            "P(ack by t) = P(at least W of N replies ≤ t),  a binomial tail at p = F(t)",
            "W = 2, N = 3   p99 = 8 ms        W = 2, N = 4   p99 = 4 ms",
            "W = 2, N = 8   p99 = 2 ms        W = 3, N = 3   p99 = 24 ms",
            "more replicas at fixed W is FASTER, not slower",
            "and R + W > N is what a fixed W stops satisfying",
        ],
        "key_label": "A binomial tail, and the trap underneath it",
        "concepts_intro": (
            "One distributional fact, one counter-intuitive consequence, and the cost the "
            "consequence hides."
        ),
        "concepts": [
            ("The quorum waits for the W-th fastest, not for everyone",
             "The coordinator sends to all `N` and acknowledges as soon as `W` have come "
             "back. The wait is therefore the `W`-th smallest of `N` reply times, and "
             "`P(ack by t)` is the probability that at least `W` of `N` independent "
             "replies landed by `t` — exactly the binomial tail Availability and Failure "
             "used for `k`-of-`n`, with success probability `F(t)`."),
            ("More replicas at fixed W is more chances to be early",
             "At a fixed `t`, each replica independently has probability `F(t)` of having "
             "replied. Adding another replica adds another Bernoulli trial without raising "
             "the threshold `W`, so the probability of reaching `W` by `t` goes up, and "
             "the p99 goes down or stays put. On the distribution here `W = 2` costs "
             "`8 ms` at `N = 3`, `4 ms` at `N = 4` and `2 ms` at `N = 8`."),
            ("Latency is not the only thing N moves",
             "Raising `N` with `W` fixed is free latency and expensive correctness: the "
             "overlap condition `R + W > N` has an `N` on the wrong side of it. Going from "
             "three replicas to four with `R = W = 2` takes a configuration that "
             "overlapped to one that does not, and the read now misses the write one time "
             "in six. The fast answer and the correct answer are different answers."),
        ],
        "read_title": "The W-th fastest, and what the sweep in N really costs",
        "read_intro": (
            "Where the binomial tail comes from, why a larger `N` is faster, and what the "
            "same change does to the overlap."
        ),
        "body": [
            ("def", ("Quorum write, and its acknowledged-by distribution",
                     "A <strong>quorum write</strong> with parameters `(N, W)` is sent to "
                     "all `N` replicas and acknowledged when `W` of them have replied. If "
                     "replies are independent with CDF `F`, then "
                     "`P(acked by t) = Σ C(N,k) F(t)^k (1 − F(t))^(N−k)` summed over "
                     "`k = W` to `N` — the probability that at least `W` of `N` replies "
                     "arrived by `t`.")),
            ("p", "This is the same sum as a `k`-of-`n` availability and the lab computes "
                  "it with the same code, which is the point: “at least `W` of `N` "
                  "replied by `t`” and “at least `k` of `n` are up” are one question asked "
                  "of two different Bernoulli trials."),
            ("math", [
                "per-replica reply time as in the synchronous-write lesson",
                "F(2) = 0.6   F(4) = 0.9   F(8) = 0.97   F(16) = 0.992   F(24) = 0.998",
                "",
                "W = 2, sweeping N              p99 of the quorum ack",
                "  N = 2    wait for both                 24 ms",
                "  N = 3                                   8 ms",
                "  N = 4                                   4 ms",
                "  N = 5                                   4 ms",
                "  N = 8                                   2 ms",
                "",
                "and for comparison, waiting for everybody",
                "  N = 3, W = 3                           24 ms",
            ]),
            ("p", "Two of the rows are worth pausing on. `W = N` is the synchronous write "
                  "of an earlier lesson and it costs `24 ms`; relaxing the same three-node "
                  "cluster to `W = 2` costs `8 ms`, a third as much, for a write that is "
                  "still on two machines. And then adding a fourth replica — a change "
                  "everybody describes as making writes more expensive — halves it again."),
            ("h3", "Why a larger N is faster"),
            ("p", "Because `W` is a threshold and `N` is the number of attempts at it. "
                  "Each replica is an independent chance to be among the first two back; "
                  "more chances means the second one arrives sooner. The write is not "
                  "waiting for the extra replica, it is racing it, and a race with more "
                  "entrants finishes its second place earlier."),
            ("math", [
                "at t = 4 ms a replica has replied with probability F(4) = 9/10",
                "",
                "N = 3, W = 2   P = C(3,2)(9/10)²(1/10) + C(3,3)(9/10)³",
                "                 = 3(81/100)(1/10) + 729/1000",
                "                 = 243/1000 + 729/1000",
                "                 = 972/1000 = 0.972          < 0.99",
                "",
                "N = 4, W = 2   P = 1 − (1/10)⁴ − C(4,1)(9/10)(1/10)³",
                "                 = 1 − 1/10 000 − 36/10 000",
                "                 = 9963/10 000 = 0.9963      ≥ 0.99",
                "",
                "so the p99 falls from 8 ms to 4 ms when the fourth replica is added",
            ]),
            ("p", "Nothing about the fourth replica is faster than the first three. What "
                  "changed is that the event “fewer than two replies by `4 ms`” now "
                  "requires three or four stragglers instead of two, and stragglers are "
                  "rare enough that requiring one more of them pushes the probability "
                  "below the `1%` the p99 is asking about."),
            ("example", ("The fourth replica, and the read that stopped overlapping",
                         "The same cluster runs `R = 2, W = 2` at `N = 3`: `R + W = 4 > 3`, "
                         "so it overlaps and the minimum overlap is `1`. Add the fourth "
                         "replica for the latency and now `R + W = 4 = N`, which overlaps "
                         "nothing — and “Sloppy Quorums and the Miss Probability” prices "
                         "the damage as `C(N−W, R)/C(N, R) = C(2,2)/C(4,2) = 1/6`. One "
                         "read in six misses the write. Restoring the guarantee means "
                         "`R = 3`, which makes every read wait for the third fastest of "
                         "four instead of the second of three. The write got faster by "
                         "making the read slower, and no dashboard would have shown the "
                         "trade.")),
            ("p", "So the useful rule is not “more replicas are slower” or “more replicas "
                  "are faster”. It is that `N` moves the latency of a fixed-`W` quorum "
                  "down and moves the overlap condition against you at the same time, and "
                  "both effects have to be computed whenever `N` changes."),
        ],
        "lab": ("replica", {
            "mode": "quorumlat",
            "panel_title": "Set the quorum and the reply times",
            "panel_intro": "The tail is summed exactly at every attainable time, and the "
                           "sweep in `N` is computed rather than extrapolated. Work the "
                           "binomial tail at `N = 3` and `N = 4` by hand before you read "
                           "the verdict — this is the one result on the course most "
                           "readers refuse until they have done that.",
        }),
        "steps_title": "Computing a quorum's latency",
        "steps_intro": (
            "The arithmetic is a binomial tail. The discipline is remembering that `N` "
            "appears in two places in your design and you have only changed one of them."
        ),
        "steps": [
            ("Fix `W` and get the per-replica reply CDF",
             "`W` is the threshold the quorum is defined by. `F` is a measurement, and as "
             "with any tail question you need the distribution rather than a mean."),
            ("Evaluate the binomial tail at each attainable time",
             "`P(at least W of N by t)` with success probability `F(t)`. Sum from `k = W` "
             "to `N`, or subtract the terms below `W` from one, whichever is shorter — at "
             "small `W` the second is much shorter."),
            ("Take the smallest `t` where the tail reaches your percentile",
             "That is the quorum's p99. Compare it with the `W = N` case, which is the "
             "synchronous write, to see what the relaxation bought."),
            ("Re-check `R + W > N` before you accept the `N` you chose",
             "Every increase in `N` at fixed `W` improves the latency and erodes the "
             "overlap. If the configuration no longer overlaps, either raise `R` — and "
             "recompute the read's latency by this same method — or keep the smaller `N`."),
        ],
        "worked": {
            "title": "Two of three, then two of four",
            "intro": [
                "A three-node cluster acknowledges writes at two replicas. The p99 is "
                "`8 ms` and the team wants it lower. Somebody proposes removing a replica, "
                "on the grounds that fewer machines are fewer things to wait for.",
            ],
            "lines": [
                "per-replica reply CDF",
                "  F(2) = 6/10,   F(4) = 9/10,   F(8) = 97/100",
                "",
                "N = 3, W = 2",
                "  t = 2    P = C(3,2)(6/10)²(4/10) + (6/10)³",
                "             = 3(36/100)(4/10) + 216/1000",
                "             = 432/1000 + 216/1000 = 648/1000     < 0.99",
                "  t = 4    P = 972/1000 = 0.972                   < 0.99",
                "  t = 8    P = 3(97/100)²(3/100) + (97/100)³",
                "             = 0.084681 + 0.912673 = 0.997354     ≥ 0.99   p99 = 8 ms",
                "",
                "N = 4, W = 2",
                "  t = 4    P = 1 − (1/10)⁴ − 4(9/10)(1/10)³",
                "             = 1 − 0.0001 − 0.0036 = 0.9963       ≥ 0.99   p99 = 4 ms",
                "",
                "N = 2, W = 2   the proposal:  P = F(t)², p99 = 24 ms",
                "",
                "so removing a replica TRIPLES the p99, and adding one halves it",
            ],
            "after": [
                "The proposal is exactly backwards and the binomial tail says why in one "
                "line: with `W` fixed at two, each replica is another chance to be one of "
                "the first two back. At `N = 2` there are no spare chances at all and the "
                "write waits for both, which is the `24 ms` maximum of the synchronous "
                "lesson.",
                "The second line of the lab's arithmetic is the one to keep. Between "
                "`N = 3` and `N = 4` the p99 halves, and between `N = 4` and `N = 8` it "
                "halves again to `2 ms`, which is the floor of this distribution — no "
                "configuration can beat the fastest time any replica ever replies in.",
                "For a faded rehearsal, the team accepts `N = 4` for the write and now has "
                "`R = W = 2` on four nodes. The supplied first move is that `R + W = 4` is "
                "no longer greater than `N = 4`. Work out what `R` must become, compute "
                "the read's p99 at that `R` by the same binomial tail, and state the net "
                "change to a read-then-write round trip before checking either figure.",
            ],
        },
        "quiz_title": "Order statistics and thresholds",
        "quiz": [
            {"q": "`W` is fixed at `2` and `N` goes from `3` to `4`. What happens to the write's p99?",
             "a": ["It rises, because there is one more replica to wait for",
                   "It falls, from `8 ms` to `4 ms`",
                   "It is unchanged, because `W` did not change",
                   "It falls only if `W` rises with `N`"],
             "c": 1,
             "why": "The quorum waits for the `W`-th fastest, so an extra replica is an "
                    "extra chance to supply the second reply early. The coordinator never "
                    "waits for the fourth replica at all — it stops at two — which is why "
                    "the first option's intuition does not apply."},
            {"q": "`N = 4`, `W = 2`, and a replica has replied by `4 ms` with probability `9/10`. What is `P(ack by 4 ms)`?",
             "a": ["`0.9963`", "`0.972`", "`0.81`", "`0.9`"],
             "c": 0,
             "why": "`1 − P(no replies) − P(exactly one) = 1 − (1/10)⁴ − 4(9/10)(1/10)³ = "
                    "0.9963`. `0.972` is the same tail at `N = 3`; `0.81` is the "
                    "probability that two specific replicas have both replied; `0.9` is "
                    "one replica alone."},
            {"q": "You raise `N` from `3` to `4` for the latency and leave `R = W = 2`. What did that change break?",
             "a": ["Nothing — the write quorum is still two machines",
                   "The overlap: `R + W = 4` is no longer greater than `N = 4`, so a read set and a write set can be disjoint",
                   "The write latency, which now rises",
                   "Only the storage bill, which is `4×` instead of `3×`"],
             "c": 1,
             "why": "`R + W > N` is the condition and it has `N` on the wrong side. At "
                    "`N = 4` with `R = W = 2` the miss probability is "
                    "`C(2,2)/C(4,2) = 1/6`. The write latency fell rather than rose, and "
                    "the storage bill did rise — but a correctness guarantee disappearing "
                    "silently is the change that matters."},
        ],
        "mistakes": [
            ("Assuming more replicas make a fixed-`W` write slower",
             "This is the misconception the lesson exists for. The coordinator waits for "
             "`W` replies and ignores the rest, so extra replicas are extra racers and not "
             "extra waits. The arithmetic that makes it obvious is the binomial tail: "
             "adding a trial without raising the threshold can only raise "
             "`P(at least W by t)`."),
            ("Raising `N` without re-checking `R + W > N`",
             "Latency work and correctness work touch the same parameter from opposite "
             "sides. Every time `N` moves, both the quorum p99 and the overlap condition "
             "have to be recomputed, and the second one fails quietly: nothing gets "
             "slower, nothing logs an error, and a fraction of reads simply stop seeing "
             "recent writes."),
            ("Quoting the quorum's p99 as though it were the slowest replica's",
             "`W = 2` of three costs `8 ms` here and `W = 3` of three costs `24 ms`. "
             "Those are different statistics of the same replicas — the second fastest and "
             "the slowest — and treating a quorum write as though it waited for everyone "
             "over-charges it by a factor of three on this distribution."),
        ],
        "standard": ("Finish when “we added a replica, so writes will be slower” prompts you to ask what W is.",
                     "You should be able to write `P(ack by t)` as a binomial tail, "
                     "evaluate it at a handful of times, read a p99 off it, sweep `N` and "
                     "predict the direction before computing, and state what the same "
                     "sweep did to `R + W > N`."),
        "note": "The last example on this page left a configuration where `R + W = N`, "
                "which is a guarantee you no longer have. “Sloppy Quorums and the Miss "
                "Probability” computes exactly what that costs — and the answer at three "
                "replicas with one read and one write is not a small number.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "sloppy-quorums",
        "title": "Sloppy Quorums and the Miss Probability",
        "module": "Quorums",
        "one_line": "Compute the exact probability that a read misses the write when `R + W ≤ N`.",
        "summary": (
            "When `R + W ≤ N` the read set may be drawn entirely from nodes the write "
            "never reached, and the probability of that is a ratio of combinations: "
            "`C(N − W, R)/C(N, R)`. At `N = 3` with `R = W = 1` it is exactly `2/3` — two "
            "reads in three see the old value. And `R + W = N`, which reads like the "
            "boundary of the guarantee, is `1/3` at three nodes: one read in three, for a "
            "system that has paid for three replicas."
        ),
        "key": [
            "R + W ≤ N:   P(miss) = C(N − W, R) / C(N, R)",
            "N = 3, R = 1, W = 1    C(2,1)/C(3,1) = 2/3",
            "N = 3, R = 2, W = 1    C(2,2)/C(3,2) = 1/3",
            "N = 3, R = 2, W = 2    C(1,2)/C(3,2) = 0        the overlapping case",
            "R + W = N is not nearly R + W > N: here it is one read in three",
        ],
        "key_label": "The miss probability, as a ratio of combinations",
        "concepts_intro": (
            "A counting argument, the assumption it rests on, and the reason the near-miss "
            "configuration is the worst place to stand."
        ),
        "concepts": [
            ("A miss is a read set drawn entirely from the untouched nodes",
             "The write reached `W` nodes and left `N − W` without it. The read misses "
             "exactly when all `R` of its nodes come from those `N − W`, and the number of "
             "such read sets is `C(N − W, R)` out of `C(N, R)` in total. Every quantity in "
             "that ratio is a combination, so the probability is an exact fraction rather "
             "than an estimate."),
            ("The uniform draw is an assumption, and it is stated",
             "The formula counts read sets as equally likely, which is what a coordinator "
             "picking `R` nodes at random does. A coordinator that always prefers the same "
             "nodes — the nearest, the least loaded, the first in a list — has a miss "
             "probability that is not this number and may be `0` or `1` depending on where "
             "the write landed. The formula is the random-placement case, and real "
             "systems are often less random than that."),
            ("R + W = N is the worst place to stand",
             "It is one short of a guarantee and it is paying the full price of `N` "
             "replicas. At `N = 3` it misses one read in three; at `N = 5` it misses one "
             "in ten. It never misses zero, and the single node that would fix it — one "
             "more in `R` or in `W` — is nearly always cheaper than the incident it "
             "prevents."),
        ],
        "read_title": "Counting the read sets that miss",
        "read_intro": (
            "Where the ratio of combinations comes from, what it says at three nodes and "
            "at five, and what a miss does and does not mean."
        ),
        "body": [
            ("def", ("Sloppy quorum, and the miss probability",
                     "A configuration with `R + W ≤ N` is a <strong>sloppy quorum</strong>: "
                     "it has no overlap guarantee. If the read's `R` nodes are drawn "
                     "uniformly from the `N`, the probability that the read set contains "
                     "no node the write reached — the <strong>miss probability</strong> — "
                     "is `C(N − W, R) / C(N, R)`.")),
            ("p", "The counting is direct. There are `C(N, R)` possible read sets. A read "
                  "set misses precisely when it avoids all `W` nodes the write reached, "
                  "which means choosing all `R` of its members from the remaining `N − W`, "
                  "and there are `C(N − W, R)` ways to do that."),
            ("math", [
                "N nodes; the write reached W of them; the read draws R uniformly",
                "",
                "  read sets that miss  =  those lying inside the N − W untouched nodes",
                "                       =  C(N − W, R)",
                "  read sets in total   =  C(N, R)",
                "",
                "  P(miss) = C(N − W, R) / C(N, R)",
                "",
                "and when R + W > N the numerator is C of a number smaller than R,",
                "which is 0 — the overlap theorem, arrived at by counting",
            ]),
            ("p", "That last remark is worth keeping: the overlap theorem and this formula "
                  "are the same statement. When `R + W > N` there are no read sets that "
                  "miss, so the numerator is zero; when `R + W ≤ N` there are some, and "
                  "the formula says how many."),
            ("h3", "The edge case is not nearly the good case"),
            ("math", [
                "N = 3",
                "",
                "  R   W   R + W    P(miss) = C(3 − W, R)/C(3, R)",
                "  1   1     2      C(2,1)/C(3,1) = 2/3     = 66.66…%",
                "  2   1     3      C(2,2)/C(3,2) = 1/3     = 33.33…%",
                "  1   2     3      C(1,1)/C(3,1) = 1/3     = 33.33…%",
                "  2   2     4      C(1,2)/C(3,2) = 0/3     = 0",
                "  3   1     4      C(2,3)/C(3,3) = 0/1     = 0",
                "",
                "N = 5",
                "",
                "  1   1     2      C(4,1)/C(5,1) = 4/5     = 80%",
                "  2   2     4      C(3,2)/C(5,2) = 3/10    = 30%",
                "  2   3     5      C(2,2)/C(5,2) = 1/10    = 10%",
                "  3   3     6      C(2,3)/C(5,3) = 0       = 0",
            ]),
            ("p", "Two patterns come out of the table. The `R + W = N` rows are never "
                  "zero and they get better as `N` grows — one third at three nodes, one "
                  "tenth at five — which is why the configuration survives in production "
                  "long enough to be believed in. And the step from the last sloppy row to "
                  "the first overlapping one is always one node, on either path."),
            ("example", ("R = W = 1, and what two thirds actually means",
                         "The fastest possible configuration on three replicas: write to "
                         "one node, read from one node. Both operations wait for a single "
                         "machine, so both are as quick as the medium allows, and two "
                         "reads in three that immediately follow a write return the old "
                         "value. Note what this is not: the write is not lost. It is on a "
                         "node, background repair will spread it, and a read a second "
                         "later will very likely find it. The `2/3` is the probability at "
                         "the moment before that happens — the same moment that "
                         "“Replication Lag and Stale Reads” priced from the other "
                         "direction.")),
            ("p", "So a sloppy quorum is a bet that reads rarely follow writes closely. "
                  "That bet is sometimes right — an analytics store, a feed nobody re-reads "
                  "immediately — and it is catastrophic for anything a user writes and then "
                  "looks at. The number that decides it is this one, multiplied by how "
                  "often your reads really do chase your writes."),
        ],
        "lab": ("replica", {
            "mode": "sloppy",
            "panel_title": "Set the sloppy configuration",
            "panel_intro": "Both combinations are computed as exact integers and their "
                           "ratio reduced, so the miss probability on this page is a "
                           "fraction rather than a rounding of one. The panel also shows "
                           "the smallest `R` that would restore the guarantee.",
        }),
        "steps_title": "Pricing a configuration that does not overlap",
        "steps_intro": (
            "Three of the four steps are arithmetic. The fourth is the one that decides "
            "whether the arithmetic applies to your system at all."
        ),
        "steps": [
            ("Confirm that `R + W ≤ N`, so there is something to compute",
             "If `R + W > N` the miss probability is zero and the question is the overlap "
             "question instead. The formula returns zero in that case too, because "
             "`C(N − W, R)` is `C` of a number below `R`."),
            ("Compute `C(N − W, R)` and `C(N, R)` as integers, then reduce",
             "Keep them as exact integers. These are small numbers and there is no reason "
             "to let a decimal in: `C(2,1)/C(3,1)` is `2/3`, not `0.67`, and the exact "
             "form is what makes the comparison with the neighbouring configuration "
             "obvious."),
            ("Compare with the configuration one node away",
             "Raise `R` by one, then `W` by one, and compute both. One of them usually "
             "costs less than the other on your workload, and one of them is usually "
             "enough to reach `R + W > N`."),
            ("Check that your coordinator actually draws uniformly",
             "If reads are routed by locality, by load or by a fixed preference list, the "
             "read set is not uniform and this probability is the wrong one. It may be "
             "better — a coordinator that reads and writes the same preferred node never "
             "misses — or much worse, and either way the formula is describing a system "
             "you have not got."),
        ],
        "worked": {
            "title": "Three replicas, one of each, and the two repairs",
            "intro": [
                "A key-value store is configured for speed: three replicas, write "
                "acknowledged by one, read served by one. Users report that a value they "
                "just saved sometimes comes back as it was. The question is how often "
                "“sometimes” is, and what the cheapest fix costs.",
            ],
            "lines": [
                "N = 3, R = 1, W = 1",
                "",
                "  the write reached 1 node; 2 nodes do not have it",
                "  read sets that miss  = C(2,1) = 2",
                "  read sets in total   = C(3,1) = 3",
                "  P(miss) = 2/3                two reads in three see the old value",
                "",
                "repair 1: raise R to 2",
                "  C(2,2)/C(3,2) = 1/3          R + W = 3 = N, still no guarantee",
                "  cost: the read now waits for the 2nd fastest of 3",
                "",
                "repair 2: raise W to 2 as well",
                "  C(1,2)/C(3,2) = 0/3 = 0      R + W = 4 > 3, guaranteed",
                "  cost: the write now waits for the 2nd fastest of 3,",
                "        which the quorum-latency lesson priced at 8 ms p99",
                "",
                "so: 2/3  →  1/3  →  0,  for two order statistics",
            ],
            "after": [
                "The first repair halves the problem and does not solve it, which is "
                "exactly the trap: it will look like a fix in a test that issues ten "
                "reads, and it leaves a third of them wrong. `R + W = N` is not a weaker "
                "version of the guarantee, it is the absence of one with better odds.",
                "The second repair costs the write an order statistic — the second fastest "
                "of three rather than the first — and that was priced at `8 ms` at the p99 "
                "on the distribution this course has been using. Eight milliseconds on the "
                "write path to remove two thirds of a correctness problem is not a close "
                "call.",
                "For a faded rehearsal, the same store is moved to five replicas and "
                "somebody proposes `R = 2, W = 2` as a compromise. The supplied first move "
                "is `C(3,2) = 3` and `C(5,2) = 10`. Compute the miss probability, then "
                "find every configuration on five nodes with `R + W = 6` and say which of "
                "them you would choose for a workload whose reads outnumber its writes "
                "nine to one.",
            ],
        },
        "quiz_title": "Missing the write, exactly",
        "quiz": [
            {"q": "`N = 3`, `R = 1`, `W = 1`. What is the probability that a read misses the write?",
             "a": ["`2/3`", "`1/3`", "`1/2`", "`1/9`"],
             "c": 0,
             "why": "`C(N − W, R)/C(N, R) = C(2,1)/C(3,1) = 2/3`. `1/3` is the probability "
                    "the read hits — and also the miss probability one node up, at "
                    "`R = 2`. `1/2` and `1/9` do not come out of any configuration here; "
                    "the second is what you get by treating the two events as independent "
                    "draws of the same node."},
            {"q": "`N = 5`, `R = 2`, `W = 3`, so `R + W = 5 = N`. What is the miss probability?",
             "a": ["`0`", "`1/10`", "`3/10`", "`1/5`"],
             "c": 1,
             "why": "`C(5 − 3, 2)/C(5, 2) = C(2,2)/C(5,2) = 1/10`. `0` is what `R + W = N` "
                    "is widely assumed to give and is the answer only when the sum is "
                    "strictly greater. `3/10` is `R = W = 2` on five nodes, and `1/5` is "
                    "not a configuration on this cluster at all."},
            {"q": "Your coordinator always sends reads to the two nearest replicas and writes to the nearest one. Does `C(N − W, R)/C(N, R)` describe its miss probability?",
             "a": ["Yes — the formula holds for any routing",
                   "No — the formula assumes the read set is drawn uniformly, and a fixed preference makes the miss probability `0` or `1` depending on where the write landed",
                   "Yes, provided `R + W ≤ N`",
                   "No, because the formula needs `R` and `W` to be equal"],
             "c": 1,
             "why": "The counting divides by `C(N, R)` because every read set is treated "
                    "as equally likely. Deterministic routing collapses that: if the "
                    "nearest node is in both the read set and the write set, the read "
                    "never misses; if a failover put the write elsewhere, it may always "
                    "miss. The formula is not wrong, it is about a different coordinator, "
                    "and `R + W ≤ N` is the condition for it to be non-zero rather than "
                    "the condition for it to apply."},
        ],
        "mistakes": [
            ("Reading `R + W = N` as good enough",
             "It is one read in three at `N = 3` and one in ten at `N = 5`, and neither is "
             "a rounding of zero. The configuration is especially convincing because it "
             "usually works, which means it fails in production under load and not in the "
             "test that sent twenty requests."),
            ("Assuming a miss means the write was lost",
             "A miss is a read that did not see a write which is sitting safely on `W` "
             "nodes. Anti-entropy, read repair and hinted handoff will spread it; the "
             "probability computed here is about the moment before they do. Confusing the "
             "two turns a staleness conversation into a durability panic and sends the "
             "investigation to the wrong place."),
            ("Applying the formula when the coordinator does not draw uniformly",
             "Locality-aware routing, preference lists and least-loaded selection all "
             "break the uniform draw the counting rests on. Before quoting "
             "`C(N − W, R)/C(N, R)`, check how your read set is actually chosen — and if "
             "it is chosen the same way the write set was, you may have a much better "
             "number than the formula, with a much worse failure mode when that node is "
             "down."),
        ],
        "standard": ("Finish when R + W = N reads to you as a configuration with a number attached, not as a near miss.",
                     "You should be able to compute `C(N − W, R)/C(N, R)` as an exact "
                     "fraction, state it for the common small configurations without "
                     "looking them up, name the cheapest change that reaches "
                     "`R + W > N`, distinguish a miss from a lost write, and check the "
                     "uniform-draw assumption against your own coordinator."),
        "note": "Every configuration so far has been a free choice of `R` and `W`. One "
                "choice is not free: a cluster that has to agree on a leader or a "
                "membership list uses a majority, and a majority's size is forced by `n`. "
                "“Majorities and Fault Tolerance” works out what that costs — and shows "
                "that the fourth node in a three-node cluster adds nothing at all.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "majorities-and-fault-tolerance",
        "title": "Majorities and Fault Tolerance",
        "module": "Majorities and leaders",
        "one_line": "Compute the failures a cluster size tolerates and the availability of its majority, and say what an even size buys.",
        "summary": (
            "A majority of `n` is `⌊n/2⌋ + 1`, and any two majorities intersect, which is "
            "why consensus is built on them. The failures tolerated are `f = ⌊(n − 1)/2⌋`, "
            "so `2f + 1` is the only cluster size worth buying: four nodes tolerate one "
            "failure exactly as three do, while needing three of four up instead of two of "
            "three. With nodes up `99%` of the time that makes four nodes strictly "
            "<em>less</em> available than three — `99.940797%` against `99.9702%`."
        ),
        "key": [
            "majority of n = ⌊n/2⌋ + 1        any two majorities share a node",
            "f = ⌊(n − 1)/2⌋                  so the useful sizes are n = 2f + 1",
            "n = 3   majority 2   f = 1   A = 99.9702%",
            "n = 4   majority 3   f = 1   A = 99.940797%      worse, for one more node",
            "n = 5   majority 3   f = 2   A = 99.99901494%",
            "each node up 99/100, failures assumed independent",
        ],
        "key_label": "Two integers and a binomial tail",
        "concepts_intro": (
            "The intersection property, the integer that follows from it, and the "
            "availability that follows from the integer."
        ),
        "concepts": [
            ("Any two majorities intersect, which is why consensus uses them",
             "Two subsets of `n` each larger than `n/2` cannot be disjoint — it is the "
             "overlap theorem with `R = W = ⌊n/2⌋ + 1`. That is what stops two leaders "
             "being elected in the same term and two conflicting decisions being "
             "committed: any two decisions share a node, and a node does not vote both "
             "ways."),
            ("A majority survives exactly `f = ⌊(n − 1)/2⌋` failures",
             "The cluster keeps working while a majority is still up, so it tolerates "
             "`n − (⌊n/2⌋ + 1)` failures, which is `⌊(n − 1)/2⌋`. At `n = 3` that is `1`; "
             "at `n = 4` it is also `1`; at `n = 5` it is `2`. `f` only moves on the odd "
             "sizes, and `n = 2f + 1` is the cheapest cluster tolerating `f`."),
            ("An even `n` raises the quorum and not the tolerance",
             "Going from three nodes to four takes the majority from `2` to `3` while `f` "
             "stays at `1`. You now need three specific machines up instead of two, out of "
             "a pool with one more thing in it that can break. With independent `99%` "
             "nodes that is a net loss: `99.940797%` against `99.9702%`, and the fourth "
             "machine has been bought to make the cluster worse."),
        ],
        "read_title": "Majorities, the integer f, and the availability that follows",
        "read_intro": (
            "Why consensus is built on majorities, what an even cluster size actually buys, "
            "and the binomial tail that prices both."
        ),
        "body": [
            ("def", ("Majority, and fault tolerance",
                     "A <strong>majority</strong> of `n` nodes is any subset of size "
                     "`⌊n/2⌋ + 1`. A cluster that requires a majority to make progress "
                     "<strong>tolerates</strong> `f = ⌊(n − 1)/2⌋` failures, and the "
                     "relation is usually written `n = 2f + 1`: to tolerate `f`, buy "
                     "`2f + 1` nodes.")),
            ("p", "The intersection property is the reason for all of it. Two majorities "
                  "of the same `n` must share a node, by the same pigeonhole argument that "
                  "“Quorums Overlap” proved, so a node that has voted for one decision can "
                  "refuse a conflicting one. Nothing else about a majority is special — it "
                  "is simply the smallest quorum that overlaps itself."),
            ("math", [
                "each node up with probability 99/100, failures independent",
                "A = P(at least the majority are up), a k-of-n binomial tail",
                "",
                "  n    majority   f    A",
                "  1        1      0    99%",
                "  2        2      0    98.01%",
                "  3        2      1    99.9702%",
                "  4        3      1    99.940797%",
                "  5        3      2    99.99901494%",
                "  6        4      2    99.998044641%",
                "  7        4      3    99.99996583302%",
                "",
                "f rises only on the odd sizes, and A falls on every even one",
            ]),
            ("p", "Read down the `f` column and the design rule falls out: `3`, `5`, `7`. "
                  "The even sizes are transitional — they carry the cost of the next size "
                  "up and the tolerance of the one below. That is why production clusters "
                  "are almost always odd, and why the advice is repeated so often that its "
                  "reason gets lost."),
            ("h3", "Why the fourth node makes it worse"),
            ("math", [
                "n = 3, majority 2",
                "  A = C(3,2)(99/100)²(1/100) + (99/100)³",
                "    = 3(9801/10 000)(1/100) + 970 299/1 000 000",
                "    = 29 403/1 000 000 + 970 299/1 000 000",
                "    = 999 702/1 000 000   =  99.9702%",
                "",
                "n = 4, majority 3",
                "  A = C(4,3)(99/100)³(1/100) + (99/100)⁴",
                "    = 4(970 299/1 000 000)(1/100) + 96 059 601/100 000 000",
                "    = 3 881 196/100 000 000 + 96 059 601/100 000 000",
                "    = 99 940 797/100 000 000  =  99.940797%",
                "",
                "one more node, the same f, and 0.029403 points LESS availability",
            ]),
            ("p", "The arithmetic is not a curiosity, it is the direct consequence of "
                  "needing three specific things to work instead of two. Availability of a "
                  "`k`-of-`n` system falls as `k` rises and rises as `n` does, and the even "
                  "step raises `k` by one while raising `n` by one — and at `99%` per node "
                  "the first effect wins."),
            ("example", ("Where the next real step is",
                         "From three nodes, the upgrade is five, not four. Five tolerates "
                         "two failures instead of one and is available `99.99901494%` of "
                         "the time against `99.9702%` — a factor of about thirty in the "
                         "downtime, for two more machines. Four tolerates one failure and "
                         "is available `99.940797%`, which is worse than the three it "
                         "replaced. If the budget allows one more node and not two, the "
                         "right answer is to keep three and spend the money on making a "
                         "node's own availability better, because that is the quantity "
                         "every figure in this table is a function of.")),
            ("p", "Every number here assumes failures are independent, and Availability "
                  "and Failure's “Correlated Failure” exists to say how badly that can go. "
                  "Three nodes in one rack share a switch, a power feed and an operator; "
                  "the majority arithmetic is then describing a cluster that does not exist "
                  "and the real availability is closer to one node's. Spreading the `2f + 1` "
                  "across failure domains is what makes the independence assumption "
                  "approximately true, and it is the whole reason to care where the nodes "
                  "are."),
        ],
        "lab": ("replica", {
            "mode": "majority",
            "panel_title": "Sweep the cluster size",
            "panel_intro": "Tolerance is an integer and the availability beside it is the "
                           "same `k`-of-`n` binomial tail summed over exact fractions. "
                           "Step through `n` one at a time and watch the availability "
                           "column fall on every even size.",
        }),
        "steps_title": "Sizing a cluster that needs a majority",
        "steps_intro": (
            "Start from the failures you intend to survive, not from the number of machines "
            "you happen to have."
        ),
        "steps": [
            ("Decide `f` first, then take `n = 2f + 1`",
             "“How many failures must this survive” is a product question with an answer; "
             "“how many nodes should we run” is not. One failure means three nodes, two "
             "means five, three means seven, and nothing in between is worth buying."),
            ("Compute the majority `⌊n/2⌋ + 1` and check it against `f`",
             "`n − majority` must equal the `f` you chose. Doing this explicitly is what "
             "catches an even `n`: at `n = 4` the majority is `3` and `n − 3 = 1`, which "
             "is the tolerance you would have had for one machine less."),
            ("Compute the availability as a `k`-of-`n` tail at your node availability",
             "`A = Σ C(n,k) p^k (1 − p)^(n−k)` from `k = majority` to `n`. Do it for your "
             "`n` and for `n − 1` and `n + 1`, so that the shape of the table is in front "
             "of you rather than remembered."),
            ("State the independence assumption and where it fails",
             "Name the failure domains the nodes are spread across. If two of three share "
             "a rack, the binomial tail is optimistic and the number to report is much "
             "closer to that rack's availability than to `99.9702%`."),
        ],
        "worked": {
            "title": "Three nodes, then four",
            "intro": [
                "A three-node consensus cluster is running and a fourth machine has become "
                "available. The proposal is to add it, on the grounds that four is more "
                "than three. Both halves of the question — tolerance and availability — "
                "have exact answers.",
            ],
            "lines": [
                "each node up 99/100, independent",
                "",
                "n = 3    majority = ⌊3/2⌋ + 1 = 2      f = 3 − 2 = 1",
                "  A = C(3,2)(99/100)²(1/100) + (99/100)³",
                "    = 29 403/1 000 000 + 970 299/1 000 000",
                "    = 999 702/1 000 000   =  99.9702%",
                "  downtime ≈ 0.0298% of the time",
                "",
                "n = 4    majority = ⌊4/2⌋ + 1 = 3      f = 4 − 3 = 1",
                "  A = C(4,3)(99/100)³(1/100) + (99/100)⁴",
                "    = 3 881 196/100 000 000 + 96 059 601/100 000 000",
                "    = 99 940 797/100 000 000  =  99.940797%",
                "  downtime ≈ 0.0592% of the time",
                "",
                "the fourth node:  f unchanged at 1",
                "                  availability DOWN by 0.029403 points",
                "                  downtime roughly DOUBLED",
                "                  storage and write work up 33%",
                "",
                "n = 5    majority 3,  f = 2,  A = 99.99901494%",
            ],
            "after": [
                "Four numbers went the wrong way and one stayed still. The fourth node "
                "buys no additional tolerance, roughly doubles the expected downtime, adds "
                "a third to the storage and write work, and gives the operator one more "
                "machine to patch. There is no reading of that table in which it is an "
                "improvement.",
                "The five-node row is the honest alternative and it is a large step: two "
                "tolerated failures and about a thirtieth of the downtime. Whether it is "
                "worth two machines is a real question; whether the four-node cluster is "
                "worth one machine is not.",
                "For a faded rehearsal, suppose the nodes are only `95%` available each "
                "rather than `99%`. The supplied first move is that the `n = 3` majority "
                "availability becomes `3(0.95)²(0.05) + (0.95)³`. Compute it, do the same "
                "for `n = 4` and `n = 5`, and say whether the even-size penalty is larger "
                "or smaller at `95%` than it was at `99%` — then check both in the lab.",
            ],
        },
        "quiz_title": "Tolerance, majorities and availability",
        "quiz": [
            {"q": "A four-node cluster requires a majority to make progress. How many node failures does it tolerate?",
             "a": ["`2`", "`1`", "`3`", "`0`"],
             "c": 1,
             "why": "The majority of four is `3`, so one failure leaves three up and two "
                    "leave only two — short of a majority. `f = ⌊(4 − 1)/2⌋ = 1`, the same "
                    "as a three-node cluster. `2` is the tolerance of five nodes."},
            {"q": "Nodes are up `99%` of the time, independently. Which cluster is more available, three nodes or four?",
             "a": ["Four, at `99.940797%` against `99.9702%`",
                   "Three, at `99.9702%` against `99.940797%`",
                   "They are identical, since both tolerate one failure",
                   "Four, because more nodes always helps"],
             "c": 1,
             "why": "Three nodes need two of three up; four need three of four. Raising "
                    "the threshold costs more than adding the node gains at this node "
                    "availability, so the four-node cluster has roughly double the "
                    "downtime. Equal tolerance does not mean equal availability — "
                    "tolerance is a worst case and availability is a probability."},
            {"q": "You must survive two simultaneous node failures. What is the smallest cluster that does it?",
             "a": ["`4` nodes", "`5` nodes", "`6` nodes", "`3` nodes, if the failures are brief"],
             "c": 1,
             "why": "`n = 2f + 1` with `f = 2` gives `5`. Four tolerates one, six also "
                    "tolerates two but costs an extra machine and is less available than "
                    "five, and three tolerates one regardless of how brief the failures "
                    "are — a majority is a count of live nodes, not a count weighted by "
                    "duration."},
        ],
        "mistakes": [
            ("Believing a bigger majority tolerates more failures",
             "The majority of four is three, which is bigger than the majority of three, "
             "and it tolerates exactly the same single failure. Tolerance is "
             "`n − majority`, and the even step adds one to both sides of that "
             "subtraction. This is the misconception the lesson exists to break, and it is "
             "the reason four- and six-node clusters get built."),
            ("Sizing a cluster on an even number",
             "Every even `n` is dominated: it costs a machine more than `n − 1`, tolerates "
             "the same failures, and is less available. If somebody has a spare machine, "
             "it belongs in a different cluster, or as a non-voting replica that serves "
             "reads without joining the quorum."),
            ("Quoting the binomial availability of nodes that are not independent",
             "`99.9702%` is what three nodes give if their failures are unrelated. Three "
             "nodes in one rack, on one power feed, patched by one script at one time, "
             "fail together often enough that the correct number is closer to the shared "
             "component's availability than to the tail. The arithmetic is only as good as "
             "the failure domains the nodes are spread across, and “Correlated Failure” on "
             "the availability course is the treatment of what goes wrong when they are "
             "not."),
        ],
        "standard": ("Finish when a proposal to add one node to a three-node cluster makes you ask which failure it is meant to survive.",
                     "You should be able to compute `⌊n/2⌋ + 1` and `f` for any `n`, "
                     "evaluate the majority's availability as a `k`-of-`n` binomial tail, "
                     "say why every even size is dominated by the odd one below it, and "
                     "name the independence assumption and the failure domains it needs."),
        "note": "A majority decides who the leader is, but it does not decide how the "
                "candidates agree to hold a vote at all. If every node times out at the "
                "same instant they all stand, they all split the vote, and the cluster has "
                "no leader — for ever, if the timeout is fixed. “Randomised Election "
                "Timeouts” computes the probability of a clean first round and the number "
                "of rounds it takes, and shows that a fixed timeout gives exactly zero.",
    },
]
