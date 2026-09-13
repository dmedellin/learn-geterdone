"""Partitioning and Load Balancing, lessons 01-06 - the count, where the keys land, skew."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "how-many-shards",
        "title": "How Many Shards",
        "module": "Choosing the count",
        "one_line": "Compute the shard count from load and the shard count from storage, and build the larger of the two.",
        "summary": (
            "There is no single formula for a shard count, because there are two "
            "constraints and each of them is a ceiling. Load asks for enough nodes that "
            "the peak rate divided among them sits under a target utilisation; storage "
            "asks for enough nodes that the dataset, multiplied by its replication "
            "factor, fits. You build the larger number, and the smaller one is the "
            "headroom you have in that dimension."
        ),
        "key": [
            "N_load    = ⌈λ_peak / (c · ρ_target)⌉    c is ONE node's capacity",
            "N_storage = ⌈D · RF / per-node⌉          RF copies, not one",
            "N         = max(N_load, N_storage)       the other one is slack",
            "",
            "120 000/(8 000 × 0.65) = 23.08 → 24      48 TB × 3 / 4 TB = 36.00 → 36",
        ],
        "key_label": "Two ceilings, and the one you actually build",
        "concepts_intro": (
            "Both constraints are one division and one ceiling. What is new is that there "
            "are two of them and that the answer is a maximum rather than a sum."
        ),
        "concepts": [
            ("Each constraint is a ceiling, not a division",
             "`120 000/(8 000 × 0.65) = 23.08` shards is not an answer, because a system "
             "cannot run 0.08 of a node. The ceiling is what makes the count buildable, "
             "and it is the reason a target utilisation of 65% produces a fleet that "
             "actually runs at 41.67% once the other constraint has had its say."),
            ("`c` is one node's capacity, never a count of nodes",
             "In `⌈λ_peak/(c · ρ_target)⌉` the symbol `c` is requests a second that a "
             "single node can serve, and `ρ_target` is the fraction of that you are "
             "willing to use. Reading `c` as a machine count inverts the whole "
             "expression and gives an answer in the wrong units, which is a mistake that "
             "survives review because the number it produces still looks like a count."),
            ("The constraint that does not bind is your headroom",
             "Two ceilings give two numbers and you build the larger, so one of them is "
             "always slack. That slack is worth reporting: at the defaults the fleet is "
             "sized by storage and each node is then running at 41.67% of its request "
             "capacity, which says exactly how much traffic growth the shard count "
             "already absorbs before anyone has to reshard."),
        ],
        "read_title": "Two constraints, two ceilings, one count",
        "read_intro": (
            "What a shard is, the two questions that size a fleet of them, and why the "
            "answer is the larger of two numbers rather than either one of them."
        ),
        "body": [
            ("def", ("Shard",
                     "A <strong>shard</strong> is a disjoint piece of a dataset, together "
                     "with the node or nodes that serve it. Every key belongs to exactly "
                     "one shard, and the rule that decides which is the "
                     "<strong>partitioning function</strong>. A shard is not a "
                     "<strong>replica</strong>: a replica is a copy of a piece, a shard is "
                     "a piece. Splitting is this course; copying is “Replication and "
                     "Consistency”.")),
            ("p", "Two independent questions decide how many shards you build, and they "
                  "are asked of different resources. The first is about throughput: how "
                  "many nodes does it take for the peak request rate, divided among "
                  "them, to sit under the utilisation you are willing to run at? The "
                  "second is about bytes: how many nodes does it take to hold the "
                  "dataset once every item has been written `RF` times?"),
            ("math", [
                "load        N_load    = ⌈ λ_peak / (c · ρ_target) ⌉",
                "storage     N_storage = ⌈ D · RF / per-node ⌉",
                "the count   N         = max(N_load, N_storage)",
                "",
                "λ_peak = 120 000 /s   c = 8 000 /s   ρ_target = 0.65",
                "D = 48 TB   RF = 3   per-node = 4 TB",
                "",
                "N_load    = ⌈ 120 000 / 5 200 ⌉ = ⌈ 300/13 ⌉ = ⌈ 23.08 ⌉ = 24",
                "N_storage = ⌈ 144 TB / 4 TB ⌉   = ⌈ 36.00 ⌉             = 36",
                "N         = max(24, 36) = 36",
            ]),
            ("p", "The `RF` in the storage line is the whole of that constraint. A "
                  "48 TB dataset at three copies is 144 TB of stored bytes, and it is the "
                  "144 that has to fit. Dropping the factor gives 12 shards instead of 36 "
                  "— a fleet a third the size, sized against a number that never existed "
                  "on any disk."),
            ("example", ("The same fleet, one constraint at a time",
                         "At the numbers above, load asks for 24 and storage asks for 36, "
                         "so you build 36 and storage binds by 12 shards. Hold the "
                         "storage figures and take the peak to `200 000 /s`: load now "
                         "asks for `⌈200 000/5 200⌉ = ⌈38.46⌉ = 39`, storage still asks "
                         "for 36, and load binds by 3. Hold the load figures and take the "
                         "dataset to 20 TB: storage asks for `⌈60/4⌉ = 15` and load binds "
                         "by 9. Nothing about the method changed; which constraint won "
                         "changed twice.")),
            ("h3", "What the slack tells you, and what no slack tells you"),
            ("p", "At 36 shards each node serves `120 000/36 = 3 333 /s` against a "
                  "capacity of `8 000 /s`, which is 41.67% — well under the 65% target "
                  "that produced the load ceiling. Request traffic could grow by more "
                  "than half before load starts to bind, and that is a real answer to "
                  "“when do we reshard?”."),
            ("p", "Storage at the same count has no slack at all. Each node holds "
                  "`144 TB/36 = 4.00 TB` of a 4 TB node, because the storage ceiling "
                  "happened to land on a whole number. A dataset that grows by one byte "
                  "adds a shard, and the lab shows this by moving the dataset slider a "
                  "single terabyte. A ceiling that comes out exact is the least "
                  "comfortable answer this arithmetic can give."),
            ("h3", "Where the load ceiling came from"),
            ("p", "The load line is not new. “From a Request's Cost to a Machine Count” "
                  "derives it from one request's cost and one machine's capacity, and "
                  "everything this lesson adds is the second constraint and the maximum. "
                  "If the utilisation target in it looks arbitrary, “The Knee: Response "
                  "Time vs Utilisation” is where the number comes from: the wait rises "
                  "without bound as `ρ` approaches 1, so the target is chosen on the flat "
                  "part of that curve and then divided into."),
            ("p", "Both ceilings are computed as exact fractions in the lab and rounded "
                  "only at the ceiling itself, which matters more than it sounds: "
                  "`300/13` is `23.076923…`, and a calculation that rounds to 23.1 before "
                  "taking the ceiling still gives 24, while one that rounds to 23 gives "
                  "23 and under-provisions the fleet by a node."),
        ],
        "lab": ("shard", {
            "mode": "count",
            "peak_rps": 120000,
            "node_rps": 8000,
            "target_rho_pct": 65,
            "data_tb": 48,
            "replication_factor": 3,
            "node_tb": 4,
            "panel_title": "Size it on both constraints at once",
            "panel_intro": "Move the load sliders until load binds, then move the storage "
                           "sliders until storage binds again. The point of the exercise "
                           "is not either number: it is watching which of them is the "
                           "answer change hands while both are on the screen.",
        }),
        "steps_title": "Sizing a fleet on two constraints",
        "steps_intro": (
            "Four lines. Only the third and fourth are arithmetic; the first two are what "
            "stop the arithmetic being done on the wrong quantity."
        ),
        "steps": [
            ("Write the peak rate, not the average",
             "The count is sized on `λ_peak`. An average rate with a peak-to-average "
             "ratio of three in front of it will size a fleet that falls over daily, and "
             "“Peak to Average” is where that ratio comes from."),
            ("Divide by one node's capacity and by the utilisation target",
             "`c · ρ_target` is the rate you are actually willing to take from one node. "
             "Divide the peak by it and take the ceiling. Carrying the division as an "
             "exact fraction until the ceiling is what keeps `23.08` from becoming 23."),
            ("Multiply the dataset by the replication factor first",
             "`D · RF` is the bytes that exist, and that is what has to fit on the nodes "
             "you buy. Divide by one node's usable capacity and take the ceiling again. "
             "Usable, not nominal: whatever the filesystem, the index and the compaction "
             "headroom take is not available to store the data."),
            ("Take the maximum, and report the slack in the other one",
             "One number is the answer and the other is headroom. Say both: “36 shards, "
             "sized by storage; load then runs at 41.67% of capacity” is an answer "
             "someone can plan against, and “36 shards” alone is not."),
        ],
        "worked": {
            "title": "48 TB at three copies, 120 000 requests a second",
            "intro": [
                "Both ceilings, then the maximum, then what the loser of the two is "
                "worth as headroom.",
            ],
            "lines": [
                "load",
                "  usable rate a node = c · ρ_target = 8 000 × 0.65 = 5 200 /s",
                "  N_load = ⌈ 120 000 / 5 200 ⌉ = ⌈ 300/13 ⌉ = ⌈ 23.0769… ⌉ = 24",
                "",
                "storage",
                "  bytes that exist = D · RF = 48 TB × 3 = 144 TB",
                "  N_storage = ⌈ 144 / 4 ⌉ = ⌈ 36.00 ⌉ = 36",
                "",
                "the count",
                "  N = max(24, 36) = 36          storage binds, by 12 shards",
                "",
                "what the fleet then looks like",
                "  each node serves 120 000/36 = 3 333.3 /s of 8 000 /s = 41.67%",
                "  each node holds  144/36     = 4.00 TB of 4 TB        = 100%",
            ],
            "after": [
                "The last two lines are the ones worth keeping. The fleet was sized by "
                "storage, so storage is full and load is half idle, and those two facts "
                "together say which way this system will break: not under a traffic "
                "spike, but on the day the dataset grows.",
                "For a faded rehearsal, hold `c = 8 000 /s`, `ρ_target = 0.65`, "
                "`per-node = 4 TB` and `RF = 3`, and take the peak to `260 000 /s` with "
                "the dataset at 60 TB. The supplied first move is the usable rate a node, "
                "which is unchanged at `5 200 /s`. Produce both ceilings, say which binds "
                "and by how much, and then state the utilisation each node runs at under "
                "the count you chose. Check all three in the lab before opening the quiz.",
            ],
        },
        "quiz_title": "Two ceilings and a maximum",
        "quiz": [
            {"q": "The peak is `120 000 /s`, a node serves `8 000 /s`, and the target utilisation is 65%. How many shards does the load constraint ask for?",
             "a": ["`15`", "`10`", "`23`", "`24`"],
             "c": 3,
             "why": "`⌈120 000/(8 000 × 0.65)⌉ = ⌈300/13⌉ = ⌈23.08⌉ = 24`. `15` is "
                    "`⌈120 000/8 000⌉`, which sizes the fleet to run every node at 100%. "
                    "`10` multiplies by `ρ_target` instead of dividing by it. `23` is the "
                    "exact quotient rounded down, and 0.08 of a shard is a whole shard."},
            {"q": "A 48 TB dataset is stored at a replication factor of 3 on nodes holding 4 TB each. How many shards does the storage constraint ask for?",
             "a": ["`12`", "`36`", "`4`", "`144`"],
             "c": 1,
             "why": "`⌈48 × 3/4⌉ = ⌈36.00⌉ = 36`. `12` is `48/4`, which sizes the fleet "
                    "for one copy of a dataset that is stored three times. `4` divides by "
                    "the replication factor instead of multiplying. `144` is the stored "
                    "volume in terabytes, which is a quantity of bytes and not a count of "
                    "machines."},
            {"q": "Load asks for 24 shards and storage asks for 36. A team builds 24. What happens?",
             "a": ["Nothing; 24 satisfies the constraint that matters, because load is the tighter one",
                   "The fleet runs out of disk, because 144 TB does not fit on 24 nodes of 4 TB",
                   "The fleet runs out of throughput, because 24 nodes cannot serve `120 000 /s`",
                   "The fleet is over-provisioned by 12 shards"],
             "c": 1,
             "why": "24 nodes hold `24 × 4 = 96 TB` and the data is 144 TB, so the fleet "
                    "is 48 TB short. Throughput is fine — that was the constraint they "
                    "did size on — which is exactly why this failure arrives as a "
                    "surprise rather than as a slow degradation."},
            {"q": "In `⌈λ_peak/(c · ρ_target)⌉`, what is `c`?",
             "a": ["The number of nodes in the fleet",
                   "The number of cores on a node",
                   "One node's capacity, in requests a second",
                   "The fraction of capacity you are willing to use"],
             "c": 2,
             "why": "`c` is a rate one machine can serve; `ρ_target` is the fraction of "
                    "it you will use, and the product is the rate you take from a node. "
                    "Reading `c` as a node count makes the expression a count divided by "
                    "a count, which returns a plausible-looking number in no units at all."},
        ],
        "mistakes": [
            ("Sizing on one constraint and meeting the other in production",
             "A fleet sized on load alone runs out of disk and a fleet sized on storage "
             "alone runs out of throughput, and in both cases the number that was "
             "computed was correct. Compute both, always, and write the loser down "
             "beside the winner — it is the only record of how much room you have."),
            ("Dropping the replication factor from the storage line",
             "The bytes that have to fit are `D · RF`, not `D`. At three copies the "
             "difference is a factor of three in the fleet size, and the error is easy to "
             "make because the dataset is the number everybody quotes and the replication "
             "factor lives in a different team's configuration."),
            ("Rounding before the ceiling instead of at it",
             "`300/13` is `23.0769…`; rounded to 23 it under-provisions, and rounded to "
             "23.1 it does not, because the ceiling comes last. Carry the division exact "
             "and apply `⌈·⌉` once, at the end. The lab keeps both constraints as "
             "fractions for exactly this reason."),
        ],
        "standard": ("Finish when “how many shards?” is two questions to you rather than one.",
                     "You should be able to produce both ceilings from a description of a "
                     "workload, say which binds, state the utilisation and the bytes per "
                     "node that the chosen count implies, and name what the slack in the "
                     "other constraint buys."),
        "note": (
            "Having chosen `N`, the next question is what happens when it changes, and the "
            "answer is worse than most people expect: under a plain `mod N` assignment, "
            "going from `N` to `N + 1` relocates nearly every key in the system. "
            "“Rehashing When N Changes” counts exactly how many."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "hash-partitioning-and-imbalance",
        "title": "Hash Partitioning and Imbalance",
        "module": "Where the keys land",
        "one_line": "Measure max over mean on a seeded hashed placement, then reseed and watch the maximum move.",
        "summary": (
            "Hashing makes every shard equally likely to receive a key, which is not the "
            "same as making every shard receive the same number of keys. The mean is "
            "exactly `m/N` and the maximum is whatever the stream produced, and the gap "
            "between them is the quantity a capacity plan has to be built on. This "
            "lesson measures that gap on a placement you can reproduce, and reseeds, "
            "because one placement is one sample of a distribution."
        ),
        "key": [
            "mean = m/N          exact          max = whatever landed        measured",
            "max/mean = max · N / m                    a ratio of two integers",
            "",
            "1 200 keys, 12 shards, seed 7:  max 122, mean 100, max/mean = 61/50 = 1.220",
            "excess = 122 − 100 = 22 = 2.20 √mean      the term that does not vanish",
            "maximum load at m = N is Θ(log n / log log n)      stated, not proved",
        ],
        "key_label": "The mean is exact; the maximum is measured",
        "concepts_intro": (
            "One hard idea, and it is a negative one: the property hashing gives you is "
            "about expectations, and a capacity plan is not built on expectations."
        ),
        "concepts": [
            ("Hashing equalises the probability, not the counts",
             "A good hash makes each of the `N` shards equally likely for each of the `m` "
             "keys. That is a statement about one key at a time. The counts that result "
             "are a random vector whose mean is `m/N` in every coordinate and whose "
             "maximum is above that mean essentially always — with 1 200 keys in 12 "
             "shards the fullest shard held 122 against a mean of 100."),
            ("max/mean is an exact ratio of integers",
             "`max/mean = max · N / m`, and all three of those are counts, so the "
             "imbalance is a fraction rather than a float: `122 × 12/1 200 = 61/50`. "
             "There is nothing to approximate and nothing to model. The lab counts the "
             "occupancies and divides, which is why the figure it prints is the same "
             "figure you would get by counting the placement by hand."),
            ("One seed is one sample",
             "Across seeds 7 through 14 with the same 1 200 keys and 12 shards, the "
             "fullest shard ran from 112 to 122 and max/mean averaged 1.170. Quoting the "
             "1.220 from a single run as “the imbalance” treats one draw as a property of "
             "the scheme. The lesson is about the distribution of the maximum, and that "
             "only becomes visible when you move the seed."),
        ],
        "read_title": "What a hash actually gives you, and what it does not",
        "read_intro": (
            "The placement, the two numbers that describe it, how the gap between them "
            "behaves as the load grows, and the one result here that this library states "
            "without proving."
        ),
        "body": [
            ("def", ("Hash partitioning",
                     "Under <strong>hash partitioning</strong> the shard of a key `k` is "
                     "`h(k) mod N` for a hash function `h`. Keys near each other in the "
                     "original key space are scattered, so range scans become expensive "
                     "and the placement stops depending on what the keys mean. The "
                     "<strong>occupancy</strong> of a shard is the number of keys assigned "
                     "to it, and its <strong>mean</strong> over the fleet is `m/N` "
                     "whatever the hash does.")),
            ("p", "The claim under examination is the everyday one: that hashing spreads "
                  "keys evenly. It spreads them <em>uniformly at random</em>, which is a "
                  "different sentence. Uniform means no shard is favoured; it does not "
                  "mean no shard is fuller, and the whole of this course's imbalance "
                  "arithmetic lives in that distinction."),
            ("p", "The placements here come from a seeded generator printed on the page, "
                  "so “random” is reproducible: the stream is `x → 16 807·x mod (2³¹ − 1)`, "
                  "with the modulus prime on purpose. The generator used elsewhere on "
                  "this library's paths has a modulus of `2³¹`, and the low bits of such a "
                  "stream are periodic — `x mod 4` cycles `0, 1, 2, 3` for ever. Taking "
                  "that stream modulo 8 or 16 fills the shards perfectly level, which "
                  "would demonstrate the opposite of this lesson's claim. The constants "
                  "are on the page so you can check which generator drew your placement."),
            ("math", [
                "m = 1 200 keys      N = 12 shards      seed 7",
                "",
                "mean          = 1 200/12 = 100        exact",
                "fullest shard = 122                   counted",
                "emptiest      = 82                    counted",
                "max/mean      = 122 × 12/1 200 = 61/50 = 1.220",
                "excess        = 122 − 100 = 22 = 2.20 × √100",
            ]),
            ("h3", "Why the excess is a square-root term"),
            ("p", "Raise the load and max/mean improves: the same 12 shards with 12 000 "
                  "keys came out at 1.046 and with 120 000 keys at 1.018. It is tempting "
                  "to read that as the imbalance going away. It is not going away — it is "
                  "being divided by a larger mean. The absolute excess over the mean went "
                  "from 22 keys to 46 keys to 182 keys as the mean went from 100 to 1 000 "
                  "to 10 000, which is growth like `√mean` rather than a constant."),
            ("p", "That is why the lab prints the excess in units of `√mean` rather than "
                  "as a percentage. Measured that way it stays a small number of order "
                  "one — 2.20, 1.45, 1.82 on those three runs — instead of appearing to "
                  "shrink. It is a noisy small number, and reseeding shows it moving "
                  "between 1.20 and 2.20 on the default placement, which is the honest "
                  "picture: a term of a fixed order of magnitude, not a constant."),
            ("example", ("What this costs a capacity plan",
                         "Provision every shard for the mean and the fullest one is over "
                         "its allocation by 22% on the default placement. Provision every "
                         "shard for the fullest and 11 of the 12 are over-bought. The "
                         "usable answer is neither: size for a maximum you have measured "
                         "across several seeds — 1.170 on average and 1.220 at worst here "
                         "— and treat the excess as a cost of hashing rather than as a "
                         "defect to be engineered away.")),
            ("h3", "The result this lesson measures and does not prove"),
            ("p", "When the number of keys equals the number of shards, the maximum "
                  "occupancy is `Θ(log n / log log n)`. That result is "
                  "<strong>stated, not proved</strong> — not here and nowhere else in this "
                  "library. Its proof needs Chernoff bounds, which the Algorithms path "
                  "excludes from its own scope, so no lesson anywhere establishes it. What "
                  "this lesson does is measure the maximum on placements you choose."),
            ("p", "Two related quantities <em>are</em> computed exactly, and they are "
                  "computed elsewhere. “Balls in Bins and the Birthday Bound”, on the "
                  "Randomised Algorithms course of the Algorithms path, derives the "
                  "expected number of colliding pairs as `n(n − 1)/2m` and the expected "
                  "number of empty bins as `m(1 − 1/m)ⁿ`, both by linearity of "
                  "expectation and both exact. Those are the expectations this lesson "
                  "does not compute; the maximum is the thing it measures. The seeded "
                  "generator itself is “Hashing and Pseudorandom Numbers” on the Discrete "
                  "Mathematics path."),
            ("p", "Keep the three statuses apart when you quote a figure from this "
                  "course. The mean is exact. The maximum on a given placement is "
                  "measured and reproducible. The growth rate of the maximum is stated. "
                  "A design review that treats the third as though it had the standing of "
                  "the first is the failure this paragraph exists to prevent."),
        ],
        "lab": ("shard", {
            "mode": "bins",
            "keys": 1200,
            "shards": 12,
            "seed": 7,
            "panel_title": "Place the keys, then move the seed",
            "panel_intro": "Read max/mean off the first placement, then step the seed "
                           "through eight values and watch the fullest shard move while "
                           "the mean does not move at all. The table beside the histogram "
                           "keeps every run you have drawn, so the spread in the maximum "
                           "is on the screen rather than in your memory.",
        }),
        "steps_title": "Measuring the imbalance rather than assuming it",
        "steps_intro": (
            "The order matters: compute what is exact first, so that everything measured "
            "afterwards has something to be measured against."
        ),
        "steps": [
            ("Write down the mean before you look at anything",
             "`m/N` is exact and needs no placement. It is the number every later figure "
             "is a ratio to, and having it first stops a large maximum from looking "
             "alarming when it is ordinary."),
            ("Count the fullest shard and divide",
             "`max · N / m` is max/mean as a fraction. Keep it as a fraction: `61/50` "
             "says more than `1.22` when you come to compare two placements, because you "
             "can see the counts it came from."),
            ("Reseed at least half a dozen times",
             "One placement is one draw. Record the maximum from each and take both the "
             "average and the worst you saw. Eight seeds on the default placement give an "
             "average max/mean of 1.170 and a worst of 1.220, and those are two different "
             "numbers for two different purposes."),
            ("Size on the measured maximum, and say what you measured",
             "Provisioning at the mean under-provisions the fullest shard by the excess. "
             "Quote the figure with its sample: “max/mean 1.17 on average over eight "
             "seeds, 1.22 at worst” is a defensible input to a capacity plan; “about 1.2” "
             "is not."),
        ],
        "worked": {
            "title": "1 200 keys into 12 shards, and then into 120",
            "intro": [
                "One placement measured exactly, and then the same key count spread over "
                "ten times as many shards, which is where the ratio misleads.",
            ],
            "lines": [
                "m = 1 200, N = 12, seed 7",
                "  mean     = 1 200/12 = 100",
                "  fullest  = 122            emptiest = 82        empty shards = 0",
                "  max/mean = 122 × 12/1 200 = 1464/1200 = 61/50 = 1.220",
                "  excess   = 22 keys = 2.20 √mean",
                "",
                "m = 1 200, N = 120, seed 7",
                "  mean     = 1 200/120 = 10",
                "  fullest  = 18",
                "  max/mean = 18 × 120/1 200 = 1.800",
                "  excess   = 8 keys = 2.53 √mean",
                "",
                "the ratio got worse; the excess in root-means barely moved",
                "  2.20 √mean  →  2.53 √mean",
            ],
            "after": [
                "Ten times the shards made max/mean look much worse and did not really "
                "change the underlying quantity. That is the shape of the whole result: "
                "the excess tracks `√mean`, so shrinking the mean by spreading keys "
                "thinner makes the ratio deteriorate even though nothing about the "
                "hashing changed.",
                "For a faded rehearsal, keep 12 shards and take the key count to 12 000. "
                "The supplied first move is the mean, which is 1 000. Predict whether "
                "max/mean will be closer to or further from 1 than it was at 1 200 keys, "
                "then read the fullest shard off the lab, compute max/mean and the excess "
                "in root-means, and say which of the two figures actually told you "
                "something about the hash. Reseed three times before you commit to an "
                "answer.",
            ],
        },
        "quiz_title": "Means, maxima and what was measured",
        "quiz": [
            {"q": "1 200 keys are hashed into 12 shards and the fullest shard holds 122. What is max/mean?",
             "a": ["`1.22`", "`0.82`", "`10.17`", "`1.00`"],
             "c": 0,
             "why": "`max · N/m = 122 × 12/1 200 = 61/50 = 1.22`. `0.82` is the emptiest "
                    "shard over the mean — the other end of the same placement. `10.17` "
                    "is `122/12`, the maximum divided by the shard count, which is not a "
                    "ratio to anything. `1.00` is what a reader who believes hashing "
                    "balances would predict, and the placement disagrees."},
            {"q": "You change the seed and redraw the same 1 200 keys into the same 12 shards. What moves?",
             "a": ["Both the mean and the maximum move",
                   "Neither moves, because the generator is seeded and therefore deterministic",
                   "The maximum moves — 112 to 122 over eight seeds — and the mean does not move at all",
                   "The mean moves and the maximum does not"],
             "c": 2,
             "why": "The mean is `1 200/12 = 100` for every seed, because it is a "
                    "property of the two counts and not of the placement. The maximum is "
                    "a draw: it ran from 112 to 122 across seeds 7 to 14. Determinism is "
                    "about reproducing one placement, not about the placements agreeing "
                    "with each other."},
            {"q": "What is the status on this path of the result that the maximum occupancy is `Θ(log n / log log n)` when there are as many keys as shards?",
             "a": ["Proved in this lesson, from the occupancy counts",
                   "Proved on the Algorithms path and quoted here",
                   "Stated, not proved anywhere in this library — its proof needs Chernoff bounds, which no subject here teaches — and measured in the labs",
                   "Disproved by the measurements, which show a maximum of 122"],
             "c": 2,
             "why": "The Algorithms path states the same result and computes the exact "
                    "collision and empty-bin expectations, but its scope excludes "
                    "Chernoff bounds, which the proof of the maximum-load result needs. "
                    "So the result is stated in two places and proved in none of them, "
                    "and what both paths do instead is measure it. The 122 is at 1 200 "
                    "keys in 12 shards, which is not the `m = N` regime the result is "
                    "about."},
            {"q": "Provisioning every shard at the mean, what does the default placement cost you?",
             "a": ["Nothing; the mean is the correct capacity by definition",
                   "The fullest shard is over its allocation by 22%",
                   "The fullest shard is over its allocation by 2.2%",
                   "Eleven of the twelve shards are over their allocation"],
             "c": 1,
             "why": "The fullest holds 122 against an allocation of 100. The `2.2` in "
                    "the lab's other figure is the excess in root-means, `22/√100`, which "
                    "is a different quantity with a different unit. Eleven shards are "
                    "<em>under</em> their allocation, which is the same fact seen from "
                    "the cheap end."},
        ],
        "mistakes": [
            ("Reading “uniform” as “equal”",
             "A uniform hash makes every shard equally likely for every key. The counts "
             "that result are still a random vector, and its maximum is above its mean "
             "almost always. Every capacity figure on this course exists because those "
             "two sentences are not the same sentence."),
            ("Quoting an imbalance from a single placement",
             "One seed produced 1.220 and eight seeds averaged 1.170 with a worst of "
             "1.220. A figure from one run is a draw, not a property, and it is equally "
             "wrong to be reassured by a lucky one. Reseed, record, and quote the sample "
             "you took."),
            ("Treating a falling max/mean as a disappearing problem",
             "Going from 1 200 keys to 120 000 on the same 12 shards moved max/mean from "
             "1.220 to 1.018, while the absolute excess grew from 22 keys to 182. The "
             "ratio improved because its denominator grew. Nothing about the placement "
             "became more even."),
        ],
        "standard": ("Finish when you would not accept an imbalance figure without being told how many seeds it came from.",
                     "You should be able to compute the mean and max/mean from a "
                     "placement, describe how the excess behaves as the mean grows, and "
                     "say which of the figures on this page are exact, which are "
                     "measured, and which are stated without proof."),
        "note": (
            "Two questions follow immediately. The first is what happens to this placement "
            "when `N` changes, which is “Rehashing When N Changes” and has a sharper "
            "answer than the imbalance does. The second is whether a small change to the "
            "placement rule can make the maximum much better, and it can: “The Power of "
            "Two Choices” measures a rule that costs one extra lookup and collapses the "
            "maximum load."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "rehashing-when-n-changes",
        "title": "Rehashing When N Changes",
        "module": "Where the keys land",
        "one_line": "Count the keys that move when a shard is added, under mod-N assignment and on a ring, and check that the two counts are the whole key set.",
        "summary": (
            "Adding one node to a `mod N` placement does not move a small share of the "
            "keys; it moves `N/(N+1)` of them, which is nearly all. A consistent-hash "
            "ring moves `1/(N+1)`, which is the rest of the same whole. The two "
            "fractions add to exactly one, and that single line is the entire argument "
            "for consistent hashing."
        ),
        "key": [
            "mod N → mod N+1 moves  N/(N+1)      exact, by enumeration",
            "a ring moves           1/(N+1)      the arc the joining node took",
            "their sum              N/(N+1) + 1/(N+1) = 1",
            "",
            "N = 7 → 8:   7/8 = 87.50%      against      1/8 = 12.50%",
            "the “it moves 1/N” intuition is wrong by 6.13× at N = 7",
        ],
        "key_label": "Two fractions that are the whole key set between them",
        "concepts_intro": (
            "The counting is easy once the object being counted is right, and the object "
            "is a complete cycle of hash values rather than a sample of keys."
        ),
        "concepts": [
            ("`mod N` scrambles every key when `N` changes",
             "A key sits on shard `h mod N`. Change `N` to `N + 1` and `h mod (N+1)` is a "
             "different residue for almost every `h`: the two agree only when both equal "
             "the same value below `N`. Adding one node does not perturb the placement, "
             "it replaces it, and the keys that happen to stay are a coincidence rather "
             "than a design."),
            ("A ring moves only the arc the new node takes",
             "On a consistent-hash ring each node owns the arc ending at its token, and a "
             "key belongs to the first token at or after its position. Adding a node adds "
             "tokens and moves nothing else, so the keys that relocate are exactly the "
             "keys in the arcs the newcomer claimed — `1/(N+1)` of the ring in "
             "expectation, and whatever the newcomer's arcs actually measure on a given "
             "placement."),
            ("The two fractions add to one, and that is the argument",
             "`N/(N+1) + 1/(N+1) = 1`. The keys that `mod N` moves and the keys that a "
             "ring moves are the entire key set between them, so the comparison is not "
             "“somewhat better” — one scheme moves all but a sliver and the other moves "
             "the sliver. At `N = 7` that is 87.50% against 12.50%, and the ratio only "
             "widens as the fleet grows."),
        ],
        "read_title": "Counting the keys that move, exactly",
        "read_intro": (
            "The misconception first, then the enumeration that refutes it, then the ring "
            "and the identity the two fractions satisfy."
        ),
        "body": [
            ("p", "The expectation almost everybody brings to this is that adding one "
                  "node to a fleet of seven moves about a seventh of the keys — the share "
                  "the new node will end up owning. Under `mod N` assignment that is "
                  "wrong, and it is wrong by a factor of about `N`: the true figure at "
                  "`N = 7` is seven eighths, which is `6.13` times the one-seventh "
                  "prediction."),
            ("thm", ("Keys moved by a mod-N rehash",
                     "Assigning key `k` to shard `h(k) mod N` and then to `h(k) mod (N+1)` "
                     "moves a fraction `N/(N+1)` of a complete cycle of hash values. At "
                     "`N = 7` that is `7/8`; at `N = 100` it is `100/101`.")),
            ("proof", [
                "Take the hash values `h = 0, 1, …, N(N+1) − 1`, one complete cycle. A "
                "key stays exactly when `h mod N = h mod (N+1)`. Write `v` for that "
                "common value; since `v` is a residue mod `N` it satisfies `v ≤ N − 1`, "
                "and every such `v` is also its own residue mod `N + 1`, so the pairs "
                "that agree are exactly `(v, v)` for `v = 0, 1, …, N − 1`.",
                "Because `N` and `N + 1` are consecutive integers their greatest common "
                "divisor is 1, so by the Chinese Remainder Theorem each of the `N(N+1)` "
                "possible residue pairs occurs exactly once as `h` runs over the cycle. "
                "The `N` agreeing pairs therefore correspond to exactly `N` values of "
                "`h`, and the remaining `N(N+1) − N = N²` values move.",
                "The moved fraction is `N²/(N(N+1)) = N/(N+1)`, with no sampling and no "
                "approximation anywhere in the argument. The lab performs this "
                "enumeration for the `N` you choose: at `N = 7` it reports 49 of 56.",
            ]),
            ("p", "The Chinese Remainder Theorem step is the only piece of machinery "
                  "here, and it is “The Chinese Remainder Theorem” on the Discrete "
                  "Mathematics path; the residue arithmetic under it is “Modular "
                  "Arithmetic” on the same path. Everything else is counting."),
            ("def", ("Consistent hashing",
                     "Under <strong>consistent hashing</strong>, nodes and keys are both "
                     "placed on a ring of hash values. Each node holds one or more "
                     "<strong>tokens</strong> on the ring, and a key belongs to the first "
                     "token at or after the key's position, going clockwise and wrapping. "
                     "Adding a node adds tokens; it changes no existing token's position, "
                     "so the only keys that move are those in the arcs the new tokens "
                     "claimed.")),
            ("math", [
                "N = 7 shards, one more added",
                "",
                "mod N       moved = 7/8  = 87.50%      enumerated over 56 hashes",
                "ring        moved = 1/8  = 12.50%      in expectation",
                "sum         7/8 + 1/8 = 1",
                "",
                "a seeded sample of 600 keys",
                "  mod N     519 of 600 = 86.50%        near 7/8, not equal to it",
                "  ring       82 of 600 = 13.67%        the joining arc measured 12.89%",
                "  spared    437 of 600 by the ring",
            ]),
            ("h3", "Why the sample and the enumeration disagree, and why both are printed"),
            ("p", "The `7/8` is a count over a complete cycle of hash values, so it is "
                  "exact for that object. A real key set is a finite sample of hashes, and "
                  "the 600 keys the lab draws moved 519 times — `86.50%`, near `87.50%` "
                  "and not equal to it. Neither figure is a correction of the other. The "
                  "lab prints both because a reader who has only seen the exact fraction "
                  "will believe their own measurement is a bug."),
            ("p", "The ring's numbers work the same way with one extra wrinkle: what "
                  "moves is the arc the joining node actually took, which on this seed "
                  "was `12.89%` of the ring rather than the `12.50%` its expectation "
                  "predicts. The 82 keys that moved are the keys in that arc. The "
                  "expectation is a property of the scheme; the arc is a property of the "
                  "placement, and “Virtual Nodes” is about how far apart those two can be."),
            ("example", ("Reading the identity as a design argument",
                         "`7/8` and `1/8` are not two independent measurements that "
                         "happen to be different. They partition the same key set: every "
                         "key either changes shard under `mod N` or does not, and the "
                         "ones a ring leaves alone are precisely the complement. So the "
                         "choice between the schemes is not a tuning decision, and a "
                         "system that reshards regularly under `mod N` is copying its "
                         "entire dataset every time it grows. The identity is verified by "
                         "enumeration at eleven shard counts from 1 to 100 rather than "
                         "asserted once.")),
            ("p", "One thing the ring does not fix is the imbalance of the previous "
                  "lesson. It changes what moves when `N` changes; it does not make the "
                  "arcs equal, and with one token a node they are wildly unequal. That is "
                  "the next lesson."),
        ],
        "lab": ("shard", {
            "mode": "rehash",
            "shards": 7,
            "keys": 600,
            "seed": 11,
            "ring_seed": 3,
            "panel_title": "Add one shard, and count what moved",
            "panel_intro": "Every key's old home and new home is listed under both "
                           "schemes, with the moved ones marked, so the two fractions are "
                           "a count you can scroll through rather than a formula. Move "
                           "the shard count and watch the exact fractions and the sampled "
                           "ones move together without ever meeting.",
        }),
        "steps_title": "Pricing a change in the shard count",
        "steps_intro": (
            "Two fractions, and the check that they add to one. The check is the part that "
            "catches an arithmetic slip before it becomes a migration plan."
        ),
        "steps": [
            ("Write the mod-N fraction as `N/(N+1)`, from the current `N`",
             "Not `1/N`, and not `1/(N+1)`. At seven shards going to eight it is `7/8`. "
             "The quickest sanity check is that the fraction should be close to 1 and get "
             "closer as the fleet grows, which is the opposite of what intuition offers."),
            ("Write the ring fraction as `1/(N+1)`",
             "It is the share of the ring the joining node takes in expectation. On any "
             "particular placement the keys that move are the ones in the arcs it "
             "actually took, which will be near that fraction rather than on it."),
            ("Add them and require exactly 1",
             "`N/(N+1) + 1/(N+1) = 1`. If your two fractions do not sum to one, one of "
             "them is wrong, and it is almost always the first: `1/N` and `1/(N+1)` do "
             "not add to one with anything."),
            ("Turn the fraction into bytes and hours before deciding",
             "A fraction is not yet a cost. `7/8` of a 48 TB dataset is 42 TB to move, "
             "and “Rebalancing Cost” turns that into a duration and a utilisation. The "
             "argument for a ring is that the same growth step moves 6 TB instead."),
        ],
        "worked": {
            "title": "Seven shards to eight, counted both ways",
            "intro": [
                "The exact enumeration first, then the seeded sample of 600 keys, then "
                "the identity as a check on both.",
            ],
            "lines": [
                "mod N, by enumeration over a complete cycle",
                "  cycle length = N(N+1) = 7 × 8 = 56 hash values",
                "  keys that stay: h mod 7 = h mod 8, which forces both to be v ≤ 6",
                "                  by CRT each residue pair occurs once, so 7 values stay",
                "  moved = 56 − 7 = 49 = 7²        moved fraction = 49/56 = 7/8 = 87.50%",
                "",
                "the ring",
                "  joining node's expected arc = 1/(7+1) = 1/8 = 12.50%",
                "  on this placement it took      12.89% of the ring",
                "",
                "the check",
                "  7/8 + 1/8 = 1                  the two cover the whole key set",
                "",
                "the seeded sample, 600 keys",
                "  mod N moved 519 = 86.50%       ring moved 82 = 13.67%",
                "  the ring spared 519 − 82 = 437 of the 600",
            ],
            "after": [
                "The line worth memorising is `49 = 7²`. The count of moved hashes over a "
                "complete cycle is `N²` out of `N(N+1)`, which is where the whole result "
                "comes from, and it is a fact about consecutive integers rather than "
                "about hashing.",
                "For a faded rehearsal, take `N = 12` going to 13. The supplied first move "
                "is the cycle length, `12 × 13 = 156`. Produce the count that stays, the "
                "count that moves, both fractions as exact ratios, and their sum; then "
                "predict the sampled figure the lab will report for 600 keys — not the "
                "exact fraction, but the range you would accept — and check it. Say which "
                "of your five numbers is exact and which is a draw.",
            ],
        },
        "quiz_title": "What moves, and how much of it",
        "quiz": [
            {"q": "A fleet of 7 shards using `h mod N` grows to 8. What fraction of the keys change shard?",
             "a": ["`1/8`", "`1/7`", "`7/8`", "`1/56`"],
             "c": 2,
             "why": "`N/(N+1) = 7/8 = 87.50%`, enumerated over the 56 hashes of a "
                    "complete cycle. `1/8` is what a ring moves — the other side of the "
                    "same identity. `1/7` is the share the new node ends up owning, which "
                    "is the intuition this lesson exists to refute; the true figure is "
                    "`6.13` times it. `1/56` is one cycle length, not a fraction of keys."},
            {"q": "The same growth step on a consistent-hash ring moves what share of the keys, in expectation?",
             "a": ["`7/8`", "`1/8`", "`1/7`", "`1/64`"],
             "c": 1,
             "why": "`1/(N+1) = 1/8 = 12.50%`, the arc the joining node takes. On the "
                    "lab's placement the arc actually measured 12.89% and 82 of 600 keys "
                    "moved, which is 13.67% — near the expectation and not equal to it, "
                    "because an arc is a draw."},
            {"q": "Why is the mod-N figure `N/(N+1)` exact rather than an estimate?",
             "a": ["Because it is the average over many seeded key sets",
                   "Because the 600-key sample in the lab measured it",
                   "Because over a complete cycle of `N(N+1)` hash values each residue pair occurs exactly once, so exactly `N` keys stay",
                   "Because it is an upper bound that happens to be tight"],
             "c": 2,
             "why": "`N` and `N + 1` are coprime, so the Chinese Remainder Theorem makes "
                    "the map from a hash to its pair of residues a bijection over one "
                    "cycle. The agreeing pairs are `(v, v)` for `v` below `N`, so `N` "
                    "stay and `N²` move. The sample is a separate measurement and lands "
                    "near the fraction rather than on it — 519 of 600, or 86.50%."},
            {"q": "The lab reports 87.50% from the enumeration and 86.50% from a 600-key sample. Which is right?",
             "a": ["The enumeration; the sample has a bug",
                   "The sample; the enumeration is an idealisation",
                   "Both: one counts a complete cycle of hash values, the other counts one finite key set",
                   "Neither, because the two disagree"],
             "c": 2,
             "why": "They are answers to different questions. `7/8` is a property of the "
                    "map from `mod 7` to `mod 8` over every hash value; 86.50% is what "
                    "600 particular keys did. Reseed the key set and the sample moves; "
                    "the enumeration never does. The lab prints both so that a reader "
                    "measuring their own system does not conclude their measurement is "
                    "broken."},
        ],
        "mistakes": [
            ("Predicting that adding a node moves `1/N` of the keys",
             "It is the share the new node will <em>own</em>, not the share that moves. "
             "Under `mod N` the moved fraction is `N/(N+1)`, which at seven shards is "
             "`6.13` times the prediction. The two numbers are so far apart that a "
             "migration plan built on the wrong one is not conservative, it is fiction."),
            ("Adding `1/N` and `1/(N+1)` and expecting one",
             "The identity is `N/(N+1) + 1/(N+1) = 1`, and it is the check that catches "
             "the previous mistake immediately. If your two fractions do not sum to "
             "exactly one, you are not describing the same key set twice."),
            ("Expecting a sampled measurement to equal the exact fraction",
             "600 keys moved 86.50% of the time against an exact 87.50%, and the ring's "
             "82 moves came from an arc that measured 12.89% rather than 12.50%. A finite "
             "key set is a draw. Chasing the difference is chasing noise; reporting the "
             "sample without its size is worse."),
        ],
        "standard": ("Finish when “we will just add a node” sounds to you like a proposal to copy the dataset.",
                     "You should be able to state both fractions for any `N`, justify the "
                     "mod-N one by the cycle argument, check the pair sums to one, and say "
                     "why a sampled measurement of either will be near its fraction "
                     "without matching it."),
        "note": (
            "A ring fixes what moves and does not fix how evenly the keys sit, because one "
            "token a node produces arcs that are nothing like equal. “Virtual Nodes” "
            "measures how unequal, and prices the fix: the relative spread falls like the "
            "square root of the number of tokens, which is a slower purchase than it looks."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "consistent-hashing-and-virtual-nodes",
        "title": "Virtual Nodes",
        "module": "Where the keys land",
        "one_line": "Measure the ring's max over mean and relative spread at one, ten and a hundred tokens a node, and read the rate the spread falls at.",
        "summary": (
            "A node's share of a ring is the total length of the arcs it owns, and with "
            "one token a node those arcs are nothing like equal — the largest node in an "
            "eight-node ring took 28.29% where an equal share is 12.50%. Giving each "
            "node `V` tokens averages `V` independent arcs together, and the relative "
            "spread falls like `1/√V`. That is a real improvement and a slow one: a "
            "hundred times the tokens buys ten times the evenness."
        ),
        "key": [
            "a node's share = the total length of the arcs it owns   successor ownership",
            "",
            "8 nodes, 8 seeds     max/mean      relative spread      1/√V, stated",
            "V = 1                3.349         1.0370               1.0000",
            "V = 10               1.520         0.3309               0.3162",
            "V = 100              1.141         0.0959               0.1000",
            "",
            "100× the tokens, 10× the evenness      the rate is rounded and stated",
        ],
        "key_label": "What tokens buy, and at what rate",
        "concepts_intro": (
            "One measurement and one rate. The measurement is the surprise; the rate is "
            "the thing that decides how many tokens a real fleet runs."
        ),
        "concepts": [
            ("A ring does not balance by itself",
             "With one token a node, the ring is cut at `N` uniformly random positions and "
             "each node owns the arc ending at its cut. Uniform cut points do not give "
             "equal arcs: across eight seeded rings of eight nodes, max/mean averaged "
             "`3.349`, and on the drawn ring the largest node held 28.29% of the key "
             "space while the smallest held 2.95%. The property consistent hashing gives "
             "is stability under growth, not balance."),
            ("`V` tokens average `V` arcs together",
             "Give each node `V` tokens and its share is the sum of `V` arcs drawn from "
             "the same distribution instead of one. Sums of independent draws concentrate: "
             "the relative spread of the shares falls, and it falls like `1/√V` rather "
             "than like `1/V`. The lab measures `1.0370`, `0.3309` and `0.0959` at "
             "`V = 1, 10, 100` against a stated `1.0000`, `0.3162`, `0.1000`."),
            ("A square root is a slow purchase",
             "To halve the spread you need four times the tokens; to get a tenth of it "
             "you need a hundred times. Tokens are not free — each one is a ring entry "
             "every router and every client caches, and the lookup structure grows with "
             "`N · V` — so `V` in a real system is a few hundred rather than a few "
             "thousand, and the spread it leaves is a cost that has to be planned for "
             "rather than eliminated."),
        ],
        "read_title": "Arcs, tokens, and the rate the spread falls at",
        "read_intro": (
            "What a node's share actually is, how badly one token a node does, what `V` "
            "tokens buy, and the difference between a spread going to zero and a ratio "
            "going to one."
        ),
        "body": [
            ("def", ("Virtual node",
                     "A <strong>virtual node</strong>, or <strong>token</strong>, is one "
                     "position a physical node occupies on the ring. A node with `V` "
                     "tokens owns the union of the `V` arcs ending at them, and its "
                     "<strong>share</strong> is the total length of that union as a "
                     "fraction of the ring. Keys are assigned by successor ownership: a "
                     "key belongs to the first token at or after its position, clockwise, "
                     "wrapping at the end.")),
            ("p", "The quantity to measure is the shares, and the two ways of describing "
                  "how uneven they are answer different questions. `max/mean` is what the "
                  "fullest node costs you, and it is the number a capacity plan needs. The "
                  "<strong>relative spread</strong> — the root-mean-square deviation of "
                  "the shares divided by the mean share — is what falls at a clean rate, "
                  "and it is the number that tells you what another token is worth."),
            ("math", [
                "8 nodes, shares measured over 8 seeded rings",
                "",
                "  V     tokens on the ring   max/mean   spread    1/√V, stated",
                "  1       8                  3.349      1.0370    1.0000",
                " 10      80                  1.520      0.3309    0.3162",
                "100     800                  1.141      0.0959    0.1000",
                "",
                "the drawn ring, seed 5, V = 1",
                "  largest node  28.29% of the ring = 2.263 × an equal share of 12.50%",
                "  smallest node  2.95%             = 0.236 × the mean",
                "  the shares add to 1 — nothing is missing, they are simply not equal",
            ]),
            ("h3", "The two numbers do not go to the same place"),
            ("p", "The spread goes to zero and `max/mean` goes to one, and reading the "
                  "wrong one as the other makes `V` look either better or worse than it "
                  "is. At `V = 100` the spread is `0.0959` — about a tenth of what it was "
                  "— while `max/mean` is `1.141`, still 14% of extra capacity on the "
                  "fullest node. A tenth of the spread is not a tenth of the imbalance, "
                  "because `max/mean` has a floor of 1 that it approaches and never "
                  "passes."),
            ("p", "The `1/√V` rate is <strong>stated</strong> on this page and measured "
                  "in the lab, and the square roots printed beside the measurements are "
                  "rounded — `1/√10 = 0.3162…` is irrational, and the lab labels it as "
                  "rounded where it prints it. Measurement and statement sit in adjacent "
                  "columns on purpose: `0.3309` against `0.3162` is agreement to about "
                  "five per cent on eight seeds, which is what a rate claim is entitled "
                  "to, and it is not the same as an identity."),
            ("example", ("What one token a node costs a real fleet",
                         "An eight-node ring at `V = 1` gave a largest share of 28.29%. "
                         "If that ring were serving `100 000` requests a second, the "
                         "busiest node would take `28 290 /s` against a fair `12 500 /s`, "
                         "so every node has to be built for well over twice its share or "
                         "one of them saturates. At `V = 100` the same fleet's worst node "
                         "averages `1.141` times the mean, which is a 14% margin rather "
                         "than a 126% one. The tokens did not change the number of "
                         "machines; they changed how much of each machine is reachable.")),
            ("h3", "What a token costs"),
            ("p", "Every token is a row in the ring that routers, clients and the "
                  "membership protocol all carry, and the ownership lookup is over "
                  "`N · V` entries rather than `N`. At `N = 8` and `V = 100` that is 800 "
                  "rows, which is nothing; at `N = 1 000` and `V = 1 000` it is a million, "
                  "which is a data structure with its own operational behaviour. The "
                  "square-root rate is what makes this a real trade: since the next "
                  "halving of the spread costs four times the tokens, there is always a "
                  "point where buying evenness stops being worth the ring."),
            ("p", "Two things this lesson does not change. Tokens do not affect what "
                  "moves when a node joins — that is still the arcs the newcomer took, as "
                  "in “Rehashing When N Changes”, and it is still roughly `1/(N+1)` of "
                  "the keys. And tokens do not help at all against a single key that is "
                  "hot, because that key sits in exactly one arc however finely the ring "
                  "is cut. “Hot Keys and Salting” is where that is priced."),
        ],
        "lab": ("shard", {
            "mode": "vnodes",
            "nodes": 8,
            "vnodes": 1,
            "seed": 5,
            "panel_title": "Give each node more tokens, and watch the rate",
            "panel_intro": "Start at one token a node and look at the drawn arcs before "
                           "looking at any number: the ring is visibly lopsided. Then take "
                           "`V` to 10 and to 100 and read the table, which holds the "
                           "measured spread beside the stated `1/√V` so that a rate claim "
                           "and a measurement never get confused for one another.",
        }),
        "steps_title": "Measuring a ring and choosing `V`",
        "steps_intro": (
            "Measure before you tune. The first two steps say how bad it is; the last two "
            "say what fixing it costs."
        ),
        "steps": [
            ("Measure the shares at the `V` you actually run",
             "A node's share is the total arc it owns. Take max/mean and the relative "
             "spread, and take both over several seeds — a ring is one draw of `N · V` "
             "positions, and one draw is no more representative here than one placement "
             "was in “Hash Partitioning and Imbalance”."),
            ("Read max/mean as capacity and the spread as a rate",
             "`max/mean` is the multiple of the mean your fullest node must be built for. "
             "The spread is the quantity that falls like `1/√V`, and it is the one to "
             "watch when deciding whether another token is worth buying."),
            ("Price the next factor of two",
             "Halving the spread costs four times the tokens. Write down the ring size "
             "that implies — `N · V` entries — and whether the membership and routing "
             "layers carry it comfortably. This is where the decision actually gets made."),
            ("Check what `V` has not fixed",
             "Tokens do not reduce what moves when a node joins, and they do nothing "
             "about a hot key. If the imbalance you measured is one shard far above the "
             "others rather than a spread across all of them, more tokens is the wrong "
             "tool and the next two lessons have the right ones."),
        ],
        "worked": {
            "title": "Eight nodes at V = 1, 10 and 100",
            "intro": [
                "One ring measured, then the same ring with more tokens, then the rate "
                "checked against what was stated.",
            ],
            "lines": [
                "8 nodes, equal share = 1/8 = 12.50%",
                "",
                "V = 1, seed 5, the drawn ring",
                "  largest  28.29%  = 2.263 × mean",
                "  smallest  2.95%  = 0.236 × mean",
                "  shares sum to 1",
                "",
                "averaged over 8 seeds",
                "  V =   1    max/mean 3.349    spread 1.0370    1/√V = 1.0000",
                "  V =  10    max/mean 1.520    spread 0.3309    1/√V = 0.3162",
                "  V = 100    max/mean 1.141    spread 0.0959    1/√V = 0.1000",
                "",
                "the rate, as a ratio against V = 1",
                "  measured   1.000    0.319    0.093",
                "  stated     1.000    0.316    0.100      agreement to about 5%",
            ],
            "after": [
                "The two right-hand columns are the lesson. The measured ratios track the "
                "stated `1/√V` closely enough to believe the rate and not closely enough "
                "to call it an identity, which is exactly the standing a rate claim "
                "should have when it has been measured on eight seeds rather than proved.",
                "For a faded rehearsal, stay at eight nodes and take `V` to 25. The "
                "supplied first move is the stated rate, `1/√25 = 0.2000`. Predict the "
                "relative spread the lab will report, then read it, then say how far off "
                "your prediction was as a percentage — and separately predict whether "
                "`max/mean` at `V = 25` will be nearer to `1.520` or to `1.141`, and why "
                "that question has a different answer from the first one.",
            ],
        },
        "quiz_title": "Arcs, tokens and rates",
        "quiz": [
            {"q": "An eight-node ring at one token a node has a largest share of 28.29%. How does that compare with an equal share?",
             "a": ["It is 2.263 times an equal share of 12.50%",
                   "It is 28.29% above an equal share",
                   "It is a little over an equal share of 25%",
                   "It cannot be compared, because the shares do not sum to 1"],
             "c": 0,
             "why": "An equal share of eight nodes is `1/8 = 12.50%`, and "
                    "`28.29/12.50 = 2.263`. The shares do sum to exactly 1 — the lab "
                    "prints that check — which is the point: nothing is missing from the "
                    "ring, the pieces are just very unequal."},
            {"q": "Taking `V` from 1 to 100 changes the measured relative spread from 1.0370 to 0.0959. By what factor, and why that factor?",
             "a": ["By 100, because each node now has 100 tokens",
                   "By about 10, because the spread falls like `1/√V`",
                   "By about 1.14, because that is max/mean at `V = 100`",
                   "By 10 000, because variance adds"],
             "c": 1,
             "why": "`1.0370/0.0959 = 10.8`, against a stated `√100 = 10`. The rate is "
                    "`1/√V`: a hundred times the tokens buys about ten times the "
                    "evenness. `1.141` is `max/mean` at `V = 100`, a different quantity "
                    "that approaches 1 rather than 0."},
            {"q": "Someone argues that consistent hashing balances load, so no further work is needed. What does the measurement say?",
             "a": ["It agrees: the shares sum to 1, so they are equal",
                   "It agrees at `V = 1` and disagrees at larger `V`",
                   "It disagrees: at one token a node, max/mean averaged 3.349 over eight seeds",
                   "It disagrees, but only for rings of fewer than eight nodes"],
             "c": 2,
             "why": "What consistent hashing gives is stability under growth — only the "
                    "joining node's arc moves. Balance is a separate property and it has "
                    "to be bought with tokens: at `V = 1` the fullest node averaged 3.349 "
                    "times the mean, and it took `V = 100` to bring that to 1.141."},
            {"q": "You have measured the spread at `V = 25` and want to halve it. What does that cost?",
             "a": ["`V = 50`", "`V = 100`", "`V = 35`", "It cannot be halved by adding tokens"],
             "c": 1,
             "why": "The spread falls like `1/√V`, so halving it needs four times the "
                    "tokens: `V = 100`. `V = 50` buys a factor of `√2`, about 29%. The "
                    "square root is why `V` in real systems settles in the hundreds — the "
                    "next halving always costs four times the last one."},
        ],
        "mistakes": [
            ("Believing a ring balances because the shares sum to one",
             "They always sum to one; that is what makes them shares. The question is "
             "whether they are equal, and at one token a node they are not remotely — "
             "28.29% against 2.95% on the drawn ring. Summing to one is a check that "
             "nothing was lost, not evidence of balance."),
            ("Expecting `V` tokens to divide the spread by `V`",
             "The rate is `1/√V`, measured at `1.0370`, `0.3309` and `0.0959` for "
             "`V = 1, 10, 100`. Budgeting for a linear improvement makes every "
             "token-count decision look ten times cheaper than it is and leads to a ring "
             "sized for an evenness it will not deliver."),
            ("Reading a falling spread as a falling max/mean",
             "The spread goes to zero and `max/mean` goes to 1. At `V = 100` the spread "
             "is about a tenth of what it was and the fullest node is still 14% above "
             "the mean. Capacity is bought against `max/mean`, so quoting the spread in "
             "a capacity conversation understates what the fleet needs."),
        ],
        "standard": ("Finish when you can say what a token buys and what it costs, in the same sentence.",
                     "You should be able to compute a node's share from its arcs, measure "
                     "max/mean and the relative spread over several seeds, state the rate "
                     "at which the spread falls and that it is stated rather than proved, "
                     "and say what `V` does not fix."),
        "note": (
            "Everything so far has assumed the partitioning function scatters the keys. A "
            "range partition deliberately does not, because ordered keys make scans cheap "
            "— and that choice has a cost that no number of tokens touches. “Range "
            "Partitioning and Hot Ranges” measures it."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "range-partitioning-and-hot-ranges",
        "title": "Range Partitioning and Hot Ranges",
        "module": "Skew",
        "one_line": "Compute the hottest range's share of the writes happening now, for a monotonic key and for a hashed one, and say what each costs a scan.",
        "summary": (
            "A range partition keeps keys in order, which is what makes a scan read one "
            "shard instead of all of them. The cost arrives when the key is monotonic: a "
            "timestamp or an auto-increment id sends every write happening now to exactly "
            "one range, whatever `N` is. Over the whole run that range holds its fair "
            "share, which is why a lifetime histogram makes the problem invisible."
        ),
        "key": [
            "monotonic key      hottest range takes 100.00% of the writes happening NOW",
            "                   and 12.50% of the writes over the whole run",
            "hashed key         hottest 16.00% now = 1.28 × an equal share",
            "                   but a one-window scan reads 8 of 8 ranges, not 1",
            "hashed bucket, then timestamp, 4 buckets",
            "                   hottest 30.33% now, and a scan reads 4 of 8",
        ],
        "key_label": "Balance now, ordering now, and the dial between them",
        "concepts_intro": (
            "The hard idea is a distinction between two histograms of the same writes, "
            "and every number on this page is one or the other of them."
        ),
        "concepts": [
            ("A range partition keeps order, and order is what a scan wants",
             "Under range partitioning shard boundaries are key values, so keys that are "
             "adjacent stay adjacent. “Everything written in the last hour” is then a "
             "read of one range rather than a question asked of every shard. That is the "
             "property being bought, and “Scatter-Gather Cost” is the price of not having "
             "it."),
            ("A monotonic key is perfectly balanced over all time and completely unbalanced at every instant",
             "Both sentences are true of the same run. Every write in a window lands in "
             "the one range that currently contains the largest key, so the hottest range "
             "takes 100.00% of the current writes. The hot range moves on as the key "
             "space advances, and by the end of the run each of the eight ranges has taken "
             "12.50% — a perfect lifetime histogram over a workload that never used more "
             "than one shard at a time."),
            ("The dial between them is how much of the key you hash",
             "Hash the whole key and the current writes spread over all 8 ranges, at "
             "16.00% for the hottest against an equal 12.50% — but a one-window scan now "
             "reads all 8. Hash only a small prefix into 4 buckets and put the timestamp "
             "after it: the hottest range takes 30.33% and a scan reads 4. The bucket "
             "count is a continuous choice between write balance and read fan-out, and "
             "nothing makes both free."),
        ],
        "read_title": "Two histograms of the same writes",
        "read_intro": (
            "What a range partition is for, what a monotonic key does to it, why the "
            "lifetime view hides that, and what the two fixes cost."
        ),
        "body": [
            ("def", ("Range partitioning",
                     "Under <strong>range partitioning</strong> the key space is cut into "
                     "contiguous intervals and each interval is a shard. The shard of a "
                     "key is found by locating the interval that contains it, so ordering "
                     "is preserved: a scan over an interval of keys touches only the "
                     "shards whose ranges overlap it. Hash partitioning destroys this "
                     "property deliberately; range partitioning is chosen when it is "
                     "needed.")),
            ("p", "The workload that breaks it is the most common workload there is. "
                  "Events keyed by arrival time, rows keyed by an auto-increment id, "
                  "documents keyed by a monotonically increasing version — in all of them "
                  "the key of the next write is larger than the key of the last one, so "
                  "the next write goes to whichever range holds the top of the key space."),
            ("math", [
                "8 ranges, 2 400 writes, monotonic key",
                "",
                "  window 1   300 · · · · · · ·     hottest 100.0%",
                "  window 2   · 300 · · · · · ·     hottest 100.0%",
                "  window 3   · · 300 · · · · ·     hottest 100.0%",
                "  …",
                "  window 8   · · · · · · · 300     hottest 100.0%",
                "",
                "over the whole run   every range 300 of 2 400 = 12.50%",
                "ranges taking any writes right now:  1 of 8",
            ]),
            ("p", "There is no `N` in the first column of that table. Doubling the shard "
                  "count gives sixteen ranges of which one is taking every write, and "
                  "halving it gives four ranges of which one is taking every write. "
                  "Splitting the hot range is the same: the write pointer moves into one "
                  "of the halves immediately and that half is then taking everything. "
                  "This is the first of the three skews on this course that resharding "
                  "does not touch."),
            ("h3", "Why nobody notices until it is in production"),
            ("p", "The lifetime histogram is flat. Every range ends the run with 12.50% "
                  "of the writes, which is exactly an equal share, so a dashboard that "
                  "plots writes-per-shard over a long window reports a perfectly balanced "
                  "cluster. The measurement that shows the problem is writes-per-shard "
                  "over the last few minutes, and it reports one shard at 100% and seven "
                  "idle."),
            ("example", ("The same fact from the read side",
                         "The flip side is the reason to have done this at all. Under the "
                         "monotonic key, “read everything from one window” touches "
                         "1 range of 8. Under a hashed key the writes spread — the hottest "
                         "range takes 16.00% of a window against an equal 12.50%, which is "
                         "`1.28` times a fair share rather than `8.00` times it — and the "
                         "same read now touches 8 of 8. The write hotspot and the scan "
                         "cost are the same property seen from two directions.")),
            ("h3", "The middle setting, and what it is a dial on"),
            ("p", "Put a hashed bucket in front of the timestamp and the current writes "
                  "spread over as many ranges as there are buckets. At four buckets the "
                  "lab measures the hottest range at 30.33% of the current writes instead "
                  "of 100%, and a one-window scan reads 4 ranges instead of 1 or 8. "
                  "Increasing the bucket count moves both numbers in the directions you "
                  "would expect, and the bucket count is the only thing being chosen."),
            ("p", "Notice that even hashing does not deliver the equal share. 16.00% "
                  "against 12.50% is the imbalance of “Hash Partitioning and Imbalance” "
                  "showing up in a different measurement, on 300 writes a window rather "
                  "than 1 200 keys. Hashing moves the problem from a factor of eight to a "
                  "factor of 1.28; it does not move it to one."),
            ("p", "One more caution about the word “hot”. A hot <em>range</em> is a "
                  "region of the key space that is busy, and splitting the range or "
                  "hashing the key addresses it. A hot <em>key</em> is a single key that "
                  "is busy, and neither of those helps at all, because a single key lands "
                  "in one place under every partitioning function there is. That is the "
                  "next lesson."),
        ],
        "lab": ("shard", {
            "mode": "range",
            "pattern": "monotonic",
            "ranges": 8,
            "writes": 2400,
            "buckets": 4,
            "seed": 5,
            "panel_title": "Choose what the key is",
            "panel_intro": "Start on the monotonic key and read the two hottest-range "
                           "figures — the one for the current window and the one for the "
                           "whole run — before changing anything. Then switch the pattern "
                           "and watch both figures and the scan cost move together, which "
                           "is the trade this lesson is about.",
        }),
        "steps_title": "Diagnosing a hot range",
        "steps_intro": (
            "The first step is the one that is usually skipped, and skipping it is what "
            "makes the rest of the diagnosis impossible."
        ),
        "steps": [
            ("Measure writes per shard over a short window, not over the run",
             "A lifetime histogram of a monotonic key is flat at `1/N` per shard and "
             "tells you nothing. Take the window down to minutes. If one shard is at or "
             "near 100% and the identity of that shard changes over the day, the key is "
             "monotonic and you have found it."),
            ("Look at the key, and ask whether the next one is larger",
             "Timestamps, auto-increment ids, sequence numbers and version counters all "
             "answer yes. A key that answers yes will concentrate current writes on one "
             "range under any range partitioning and under any shard count."),
            ("Price the scan you would lose",
             "Before hashing the key, find out what reads it in order. If the answer is "
             "“a time-range scan, constantly”, hashing turns every one of those into a "
             "read of all `N` shards, and “Scatter-Gather Cost” is what that costs. If "
             "nothing scans it, hash it and stop."),
            ("If both matter, choose the bucket count deliberately",
             "A hashed prefix over `b` buckets spreads current writes over `b` ranges and "
             "makes a scan read `b` of them. At `b = 4` the lab measures a hottest range "
             "of 30.33% and a scan of 4 of 8. Pick `b` from the fan-out you can afford on "
             "the read side, then check the write balance it leaves."),
        ],
        "worked": {
            "title": "The same 2 400 writes under three key designs",
            "intro": [
                "Eight ranges throughout, and the only thing that changes is what the key "
                "is. Both hottest-range figures are reported each time, because quoting "
                "one of them is how this problem stays hidden.",
            ],
            "lines": [
                "monotonic — a timestamp or an auto-increment id",
                "  hottest range, current window   100.00%    = 8.00 × an equal share",
                "  hottest range, whole run         12.50%    = an equal share exactly",
                "  ranges taking writes now          1 of 8",
                "  a one-window scan reads           1 of 8",
                "",
                "hashed — the hash of the id",
                "  hottest range, current window    16.00%    = 1.28 × an equal share",
                "  hottest range, whole run         13.21%",
                "  ranges taking writes now          8 of 8",
                "  a one-window scan reads           8 of 8",
                "",
                "hashed bucket, then timestamp — 4 buckets",
                "  hottest range, current window    30.33%    = 2.43 × an equal share",
                "  hottest range, whole run         13.92%",
                "  ranges taking writes now          4 of 8",
                "  a one-window scan reads           4 of 8",
            ],
            "after": [
                "Read the table down the “whole run” column and all three designs look "
                "the same, within a point or two of an equal 12.50%. That column is the "
                "one most monitoring reports. Every fact in this lesson is in the other "
                "columns.",
                "For a faded rehearsal, keep the monotonic key and take the range count "
                "from 8 to 32. The supplied first move is the equal share, which is now "
                "`1/32 = 3.125%`. Predict the hottest range's share of the current "
                "window, predict its share over the whole run, and then predict the "
                "multiple of an equal share the first figure represents. Check all three "
                "in the lab and say which of the three moved when `N` did.",
            ],
        },
        "quiz_title": "Hot ranges, now and over the run",
        "quiz": [
            {"q": "Writes are keyed by arrival timestamp and spread over 8 ranges. What share of the writes happening right now goes to the hottest range?",
             "a": ["`12.5%`", "`100%`", "`16%`", "`8%`"],
             "c": 1,
             "why": "Every write in the current window has a key larger than every key "
                    "before it, so all of them land in the one range holding the top of "
                    "the key space — 100.00%, and the lab's grid shows the single "
                    "occupied column marching right. `12.5%` is that range's share over "
                    "the whole run, which is the figure that hides this. `16%` is what "
                    "the hashed key measured."},
            {"q": "Over the whole run, every one of the 8 ranges took 12.50% of the writes. What does that tell you?",
             "a": ["The cluster is balanced",
                   "Nothing about the instantaneous load: the hot range moved, and there was always exactly one",
                   "The key is hashed rather than monotonic",
                   "The ranges were split correctly"],
             "c": 1,
             "why": "A monotonic key produces a perfect lifetime histogram, because the "
                    "hot range advances through the key space and every range gets its "
                    "turn. At no instant were more than one of the eight ranges taking "
                    "writes. This is precisely why the diagnostic has to be a short "
                    "window."},
            {"q": "Hashing the key brings the hottest range to 16.00% of the current writes. What did that cost?",
             "a": ["Nothing; hashing is strictly better here",
                   "Write throughput, which falls by the hash cost",
                   "The ordering: a one-window scan now reads 8 of 8 ranges instead of 1",
                   "Durability, because hashed keys are harder to replicate"],
             "c": 2,
             "why": "Range partitioning was chosen so that ordered reads touch one "
                    "shard. Hashing the key scatters adjacent keys, so a time-range scan "
                    "becomes a scatter-gather across every shard. That is the whole trade "
                    "and it is why “hash the key” is not automatically the answer."},
            {"q": "A hashed bucket in front of the timestamp, with 4 buckets, gives a hottest range of 30.33% and a scan that reads 4 of 8. What is the bucket count a dial on?",
             "a": ["The shard count",
                   "Write balance against read fan-out",
                   "The hash function's quality",
                   "The number of writes per window"],
             "c": 1,
             "why": "More buckets spread the current writes over more ranges and make "
                    "every ordered read touch more of them; fewer buckets do the "
                    "opposite. The two endpoints are the monotonic key — 1 range writing, "
                    "1 range scanned — and the fully hashed key — 8 and 8. Nothing in "
                    "between makes both cheap."},
        ],
        "mistakes": [
            ("Diagnosing a hot range from a lifetime histogram",
             "A monotonic key gives every range exactly `1/N` of the writes over a long "
             "enough window, so the chart most teams look at is flat while one shard is "
             "saturated. The measurement that finds this is writes per shard over "
             "minutes, and the tell is that the busy shard keeps changing identity."),
            ("Expecting more shards, or a split, to fix it",
             "There is no `N` in “100% of current writes”. Sixteen ranges give one range "
             "at 100%, and splitting the hot range hands the whole load to whichever half "
             "contains the top of the key space. Range skew from a monotonic key is a "
             "property of the key, and it is fixed on the key."),
            ("Hashing the key without pricing the scans",
             "Hashing brings the hottest range to `1.28` times a fair share and turns "
             "every ordered read into a request to all `N` shards. If the reason for "
             "range partitioning was the scans, that trade can be much worse than the "
             "hotspot — check what reads the table before changing how it is keyed."),
        ],
        "standard": ("Finish when you would ask “over what window?” before accepting any writes-per-shard chart.",
                     "You should be able to compute the hottest range's share both "
                     "instantaneously and over a run, explain why they differ for a "
                     "monotonic key, and state what hashing the key or a hashed prefix "
                     "does to each of them and to the cost of an ordered scan."),
        "note": (
            "A hot range is a busy region of the key space and can be split, hashed or "
            "bucketed. A single key that is busy can be none of those things: it lands in "
            "one place under every partitioning function, and “Hot Keys and Salting” shows "
            "that the hottest shard's load has a floor no shard count reaches under."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "hot-keys-and-salting",
        "title": "Hot Keys and Salting",
        "module": "Skew",
        "one_line": "Compute the hottest shard's load before and after salting, and the read amplification the salt costs.",
        "summary": (
            "One key carrying a fraction `f` of the traffic leaves the hottest shard at "
            "`f·λ + (1 − f)λ/N`. The first term has no `N` in it, so resharding cannot "
            "reach below `f·λ` however far it is pushed — a thousand shards barely moved "
            "it in the lab. What does work is splitting the key into `s` pieces, which "
            "turns `f` into `f/s`, and the price is paid on every read of that key."
        ),
        "key": [
            "hottest = f·λ + (1 − f)λ/N        the first term is not a function of N",
            "floor   = f·λ                     what no shard count reaches under",
            "",
            "f = 12%, λ = 100 000/s:   floor = 12 000/s",
            "  N = 16   →  17 500/s        N = 1 024  →  12 086/s",
            "salted into s:  hot term becomes (f/s)·λ    s = 8  →  7 000/s",
            "reads overall × (1 − f + f·s) = 1.84 at f = 12%, s = 8",
        ],
        "key_label": "A floor, and the only thing that moves it",
        "concepts_intro": (
            "One expression with two terms, and everything on this page follows from "
            "which of the two terms contains `N`."
        ),
        "concepts": [
            ("The hot term does not contain `N`",
             "Split the load in two: the hot key's `f·λ` and everybody else's `(1 − f)λ`. "
             "The second is spread over the fleet and becomes `(1 − f)λ/N` on each shard. "
             "The first goes wherever that one key hashes and stays there, whole. So the "
             "hottest shard carries `f·λ + (1 − f)λ/N`, and taking `N` to infinity drives "
             "the second term to zero and leaves the first exactly where it was."),
            ("Salting splits the key, not the traffic",
             "Write the key as `key#0` through `key#(s−1)`, choosing the suffix at random "
             "on each write. Those are `s` distinct keys, so they hash to `s` places and "
             "the hot term becomes `(f/s)·λ` on each of them. At `f = 12%` and `s = 8` "
             "the hottest shard falls from `17 500 /s` to `7 000 /s`, which is close to "
             "the mean of `6 250 /s`."),
            ("The price is on every read of that key",
             "A read of a salted key has to visit all `s` pieces and combine them, so "
             "reads of that key are multiplied by `s`. Over the whole read stream the "
             "multiplier is `1 − f + f·s`, because only the `f` share fans out: at "
             "`f = 12%` and `s = 8` that is `1.84` times the reads overall. Salting is a "
             "write-side fix bought with read-side work, and it is only worth it when "
             "reads of that key are rare or cheap."),
        ],
        "read_title": "A load with a floor in it",
        "read_intro": (
            "Where the two terms come from, what happens to each as `N` grows, what "
            "salting changes, and what it costs on the read path."
        ),
        "body": [
            ("def", ("Hot key",
                     "A <strong>hot key</strong> is a single key that receives a "
                     "disproportionate share `f` of the traffic to a dataset. Because "
                     "every partitioning function maps one key to one shard, the whole of "
                     "`f·λ` arrives at one node no matter how the function is chosen or "
                     "how many shards there are. The remaining `(1 − f)λ` is spread by "
                     "whatever the function does.")),
            ("math", [
                "hottest shard's load, with one hot key",
                "",
                "  hottest(N) = f·λ  +  (1 − f)·λ/N",
                "               ↑         ↑",
                "               no N      goes to 0 as N grows",
                "",
                "λ = 100 000 /s, f = 12%",
                "",
                "  N       mean     hottest    imbalance    above the floor",
                "    1   100 000    100 000       1.00×          88 000",
                "   16     6 250     17 500       2.80×           5 500",
                "   32     3 125     14 750       4.72×           2 750",
                "  128       781     12 688      16.24×             688",
                "1 024        98     12 086     123.76×              86",
                "",
                "  floor = f·λ = 12 000 /s",
            ]),
            ("p", "Read the last column down. Sixty-four times the shards took the "
                  "hottest shard from `17 500 /s` to `12 086 /s`, a reduction of 31%, and "
                  "the remaining `12 086` is `12 000` of hot key plus `86` of everything "
                  "else. Every further shard is buying a share of the `86`. The imbalance "
                  "column is going the other way — 2.80 times the mean at 16 shards and "
                  "123.76 times at 1 024 — because the mean is collapsing while the "
                  "hottest shard is not."),
            ("p", "This is the second of the three skews on this course that resharding "
                  "does not fix, and it is the starkest. A hot range at least moves when "
                  "you split it; a hot key does not move at all, because there is nothing "
                  "in it to split. The asymptote is the shape “Graphs and Asymptotes” on "
                  "the Algebra path describes: a curve falling toward a horizontal line "
                  "it never meets, and the line is at `f·λ`."),
            ("h3", "Salting: making one key into several"),
            ("def", ("Salting",
                     "<strong>Salting</strong> a key replaces it with `s` derived keys — "
                     "`key#0, key#1, …, key#(s−1)` — choosing a suffix uniformly at random "
                     "on each write. Writes to the original key are then spread over `s` "
                     "distinct keys, which hash independently. A read must fetch all `s` "
                     "pieces and combine them, so the operation the salt makes cheap is "
                     "the write and the operation it makes expensive is the read.")),
            ("p", "The arithmetic is immediate: the hot term becomes `(f/s)·λ` and the "
                  "rest is unchanged, so the hottest shard holds "
                  "`(f/s)·λ + (1 − f)λ/N`. At `f = 12%`, `λ = 100 000 /s`, `N = 16` and "
                  "`s = 8` that is `1 500 + 5 500 = 7 000 /s`, against a mean of "
                  "`6 250 /s`. Where sixty-four times the shards bought a 31% reduction, "
                  "eight salt pieces bought 60%."),
            ("example", ("What the salt costs, stated two ways",
                         "Every read of the salted key now issues `s = 8` requests instead "
                         "of one, so reads <em>of that key</em> are 8 times as expensive. "
                         "Across the whole read stream the multiplier is smaller, because "
                         "only the hot key fans out: `1 − f + f·s = 0.88 + 0.96 = 1.84`, "
                         "so the fleet does 1.84 times the reads overall. Both numbers are "
                         "true and they answer different questions — the first sizes the "
                         "latency of a read of that key, the second sizes the fleet. "
                         "Quoting only the second makes salting sound cheaper than it is "
                         "for the request that actually touches the hot key.")),
            ("p", "Choose `s` from the target, not from habit. The lab reports that at "
                  "these numbers a salt of 4 already brings the hottest shard within "
                  "`1.5` times the mean, at a read multiplier of `1.36` rather than "
                  "`1.84`. Going to `s = 16` gets the hottest shard to `6 250 /s` — the "
                  "mean exactly — for a read multiplier of `2.80`. The last increments of "
                  "balance are the expensive ones."),
            ("h3", "When not to salt"),
            ("p", "Salting is one of three answers and it is the one with a running "
                  "cost. If the hot key is read far more than it is written, a cache in "
                  "front of it removes the load without touching the partitioning at all "
                  "— “Hit Rate and Backend Load” prices that. If the key is hot because of "
                  "one client, a rate limit is cheaper than either. Salt when the traffic "
                  "is genuinely write-heavy on a key that genuinely has to be one key, "
                  "and then write down the read multiplier you accepted."),
            ("p", "One more property worth stating plainly: `f` is measured, not "
                  "assumed. It is the hot key's share of the traffic, and getting it from "
                  "a sampled request log is usually easy. Everything on this page is a "
                  "function of `f`, `λ`, `N` and `s`, so a designer who knows those four "
                  "numbers can answer “will more shards help?” before anyone builds "
                  "anything — and the answer, when `f·λ` is already above one node's "
                  "capacity, is no."),
        ],
        "lab": ("shard", {
            "mode": "hotkey",
            "rps": 100000,
            "hot_pct": 12,
            "shards": 16,
            "salt": 8,
            "panel_title": "Make one key hot, then try to shard it away",
            "panel_intro": "Take the shard count as high as it goes and watch the curve "
                           "flatten onto `f·λ` instead of falling. Then bring `N` back and "
                           "move the salt instead, and compare what the two dials cost: "
                           "one of them is a fleet and the other is a read multiplier.",
        }),
        "steps_title": "Pricing a hot key",
        "steps_intro": (
            "Measure `f` first. Every other number on this page is a function of it, and "
            "an assumed `f` makes the whole calculation decorative."
        ),
        "steps": [
            ("Measure `f` from a request sample",
             "`f` is the hot key's share of requests, and a sampled log gives it "
             "directly. Do this before anything else: the difference between `f = 2%` and "
             "`f = 12%` is the difference between a problem more shards will handle and "
             "one they cannot touch."),
            ("Compute the floor, `f·λ`, and compare it with one node",
             "`f·λ` is what the hot shard carries after infinite resharding. If it is "
             "already above a node's capacity, resharding is not a candidate solution and "
             "there is no point pricing it. At `f = 12%` and `λ = 100 000 /s` the floor is "
             "`12 000 /s`, which is more than the `8 000 /s` node of “How Many Shards”."),
            ("Compute the hottest shard at the `N` you have, and at a much larger one",
             "`f·λ + (1 − f)λ/N` at both. The gap between them is the entire benefit "
             "resharding can deliver — `17 500` to `12 086` here, and the second figure "
             "needed sixty-four times the fleet."),
            ("Choose `s` from a target multiple of the mean, and write down the read cost",
             "Pick the imbalance you will accept, solve for `s`, and record "
             "`1 − f + f·s` beside it. At these numbers `s = 4` lands within `1.5` times "
             "the mean for a `1.36` read multiplier and `s = 8` within `1.12` for "
             "`1.84`. The number you must not omit from the write-up is the second one."),
        ],
        "worked": {
            "title": "One key at 12% of 100 000 requests a second",
            "intro": [
                "The hottest shard at the current fleet, then after a large reshard, then "
                "after a salt — with the read cost of the last one stated both ways.",
            ],
            "lines": [
                "λ = 100 000 /s    f = 12%    N = 16",
                "",
                "  mean shard      = 100 000/16                = 6 250 /s",
                "  hot term        = 0.12 × 100 000            = 12 000 /s",
                "  everyone else   = 0.88 × 100 000/16         =  5 500 /s",
                "  hottest shard   = 12 000 + 5 500            = 17 500 /s = 2.80 × mean",
                "",
                "reshard to N = 1 024",
                "  mean shard      = 100 000/1 024             =     98 /s",
                "  hottest shard   = 12 000 + 0.88 × 97.7      = 12 086 /s = 123.76 × mean",
                "  bought: 17 500 → 12 086, a 31% reduction for 64× the fleet",
                "",
                "salt into s = 8, back at N = 16",
                "  hot term        = (0.12/8) × 100 000        =  1 500 /s",
                "  hottest shard   = 1 500 + 5 500             =  7 000 /s = 1.12 × mean",
                "  reads of that key            × 8",
                "  reads overall   1 − 0.12 + 0.12 × 8 = 1.84  × 1.84",
            ],
            "after": [
                "Put the two middle blocks side by side. Sixty-four times the machines "
                "bought a 31% reduction; eight salt pieces bought 60% and left the fleet "
                "alone. That comparison is the lesson, and it is available before anything "
                "is built, from four numbers.",
                "For a faded rehearsal, take `f` to 30% with `λ = 100 000 /s` and "
                "`N = 16`. The supplied first move is the floor, `f·λ = 30 000 /s`. "
                "Produce the hottest shard now, the hottest shard at `N = 1 024`, and the "
                "salt `s` that would bring the hottest shard within 1.5 times the mean; "
                "then state the read multiplier that `s` costs overall and the multiplier "
                "it costs a read of that key. Say which of your answers would change if "
                "`λ` doubled.",
            ],
        },
        "quiz_title": "Floors, salts and read costs",
        "quiz": [
            {"q": "One key takes 12% of `100 000` requests a second, spread over 16 shards. What does the hottest shard carry?",
             "a": ["`6 250 /s`", "`12 000 /s`", "`17 500 /s`", "`5 500 /s`"],
             "c": 2,
             "why": "`f·λ + (1 − f)λ/N = 12 000 + 5 500 = 17 500 /s`. `12 000` is the hot "
                    "term alone, which ignores the rest of the traffic on that shard. "
                    "`5 500` is the rest of the traffic alone, which ignores the hot key. "
                    "`6 250` is the mean shard, which is what the fleet would look like "
                    "if no key were hot."},
            {"q": "The same key, the same traffic, and the fleet is resharded to 1 024 shards. What does the hottest shard carry?",
             "a": ["`98 /s`", "`12 086 /s`", "`274 /s`", "`12 000 /s` exactly"],
             "c": 1,
             "why": "`12 000 + 0.88 × 100 000/1 024 = 12 000 + 86 = 12 086 /s`. `98 /s` "
                    "is the mean shard at that count, which the hot shard is 123.76 times "
                    "above. Exactly `12 000` is the floor, approached and not reached — "
                    "there is always some ordinary traffic on that shard too."},
            {"q": "Salting the key into 8 pieces brings the hottest shard to `7 000 /s`. What does it cost on the read path?",
             "a": ["Nothing; salting is a write-side change",
                   "Reads of that key fan out to 8 shards, which is 1.84 times the reads over the whole stream",
                   "All reads become 8 times as expensive",
                   "Reads become 1.12 times as expensive, matching the imbalance"],
             "c": 1,
             "why": "A read of the salted key must fetch all 8 pieces, so that read is 8 "
                    "times as expensive. Across the whole read stream only the `f` share "
                    "fans out, so the fleet-wide multiplier is `1 − f + f·s = 1.84`. Both "
                    "figures matter and they size different things — the latency of one "
                    "read, and the capacity of the fleet."},
            {"q": "Why does adding shards not fix a hot key?",
             "a": ["Because hash functions are not uniform enough",
                   "Because the hot term `f·λ` contains no `N`, so only the `(1 − f)λ/N` part falls",
                   "Because the hot key is always placed on the first shard",
                   "Because resharding moves the key to a new shard each time"],
             "c": 1,
             "why": "One key maps to one shard under any partitioning function, so `f·λ` "
                    "arrives whole wherever it lands. Shards divide the other `(1 − f)λ`, "
                    "and that term goes to zero while the first stays fixed — which is "
                    "why the lab's curve flattens onto `f·λ` rather than falling. The "
                    "hash function's quality is the subject of a different lesson and is "
                    "not what is happening here."},
        ],
        "mistakes": [
            ("Answering a hot key with more shards",
             "The load on the hot shard is `f·λ + (1 − f)λ/N` and only the second term "
             "responds. Sixty-four times the fleet bought 31% in the lab, and the "
             "remaining `12 086 /s` is almost all hot key. If `f·λ` is above one node's "
             "capacity, no shard count is a solution and the design has to change."),
            ("Quoting the fleet-wide read multiplier as the cost of a salt",
             "`1 − f + f·s = 1.84` is what the fleet does; a read of the salted key does "
             "`s = 8` requests and waits for all of them. The second number is the one a "
             "latency budget needs, and it is the one that gets left out of the "
             "write-up."),
            ("Salting a key that is read far more than it is written",
             "Salting trades read work for write balance, so it is backwards for a "
             "read-heavy key — where a cache in front of that one key removes the load "
             "entirely and changes nothing about the partitioning. Establish the read/write "
             "mix on the key before reaching for the salt."),
        ],
        "standard": ("Finish when “will more shards help?” is a question you answer with arithmetic rather than an opinion.",
                     "You should be able to compute the hottest shard's load at any `N`, "
                     "state the floor and compare it with one node's capacity, choose a "
                     "salt from a target imbalance, and report both read multipliers the "
                     "salt costs."),
        "note": (
            "Two skews down, one to go. A hot range and a hot key are both about where the "
            "work lands; the third is about when it finishes, and it appears on any job "
            "that waits for all of its partitions. “Stragglers” shows that a job's time is "
            "the maximum of `N` draws, which grows with `N` even when nothing is skewed "
            "at all."
        ),
    },
]
