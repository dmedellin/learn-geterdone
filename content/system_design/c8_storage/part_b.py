"""Storage Engines and Indexes, lessons 07-11 - the triangle, durability, layout, memory, recovery.

Every figure in this file was read off scripts/mathpath/labs/storage.py running
headlessly. Where a page prints a rounded quantity - the Zipf hit rate of the
page cache is the only one here - the lesson says so and says where the exact
form stops being computable.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "the-rum-trade-off",
        "title": "The RUM Trade-off",
        "module": "Filters and the trade-off",
        "one_line": "Compute the read, update and memory amplification of three engine shapes from the same parameters, and the disk bandwidth each one implies.",
        "summary": (
            "Read amplification, update amplification and memory amplification cannot all "
            "be minimised at once. Levelled trees, tiered trees and B-trees sit at three "
            "corners of the same triangle, each best at something and paying for it "
            "somewhere else — and the disk bandwidth an engine needs is the ingest rate "
            "multiplied by its update amplification, which is never the ingest rate."
        ),
        "key": [
            "read × update × memory — choose two, and pay in the third",
            "",
            "engine            read      update      memory     disk write at 50 MB/s in",
            "levelled LSM         5          25       11/10                  1.25 GB/s",
            "tiered LSM          50           5          10                250.00 MB/s",
            "B-tree               4       125/4         3/2                  1.56 GB/s",
            "",
            "compaction bandwidth = ingest × update amplification",
        ],
        "key_label": "Three engines, one triangle, and the bandwidth each corner implies",
        "concepts_intro": (
            "Three ratios that describe any storage engine, and the observation that "
            "pushing any one of them down pushes another up."
        ),
        "concepts": [
            ("Three amplifications describe an engine",
             "<strong>Read</strong> amplification is the storage reads one logical lookup "
             "performs. <strong>Update</strong> amplification is the bytes written per "
             "byte ingested. <strong>Memory</strong> amplification is the bytes stored "
             "per byte of unique data. Every engine has all three, all three are ratios, "
             "and a design is a choice about which of them to make small."),
            ("Each shape's strength causes its weakness",
             "A tiered tree writes each byte only `5` times, the least of the three, and "
             "pays by probing `50` runs on a lookup and keeping `10` copies of a key. A "
             "levelled tree buys the reads back to `5` and writes `25`. A B-tree reads in "
             "`4` and writes `31.25` bytes to change one row. The connection is causal "
             "rather than coincidental: merging less means keeping more, and keeping more "
             "means searching more."),
            ("The bandwidth a device needs is ingest × update amplification",
             "At `50 MB/s` of ingest the three engines demand `1.25 GB/s`, `250.00 MB/s` "
             "and `1.56 GB/s` of sustained write bandwidth. None of those is `50 MB/s`. "
             "Sizing the disk to what the application hands the engine is the "
             "misconception this page exists to kill, and it is off by between five and "
             "thirty-one times."),
        ],
        "read_title": "Three amplifications, three engines, one triangle",
        "read_intro": "What each shape is best at, what it pays for it, and how much disk bandwidth each one actually needs.",
        "body": [
            ("def", ("Read, update and memory amplification",
                     "For a storage engine, <strong>read amplification</strong> `RA` is "
                     "the number of storage reads a logical lookup performs; "
                     "<strong>update amplification</strong> `UA` is the bytes written to "
                     "storage per byte ingested; <strong>memory amplification</strong> "
                     "`MA` is the bytes occupied per byte of unique data.",
                     "The <strong>RUM conjecture</strong> is that no engine minimises all "
                     "three: a design that is best in one is, in general, worse in at "
                     "least one other.")),
            ("p", "Memory amplification is a measure of <em>space</em>, not of RAM. A "
                  "tiered tree with `MA = 10` is keeping ten copies of a key on disk "
                  "while it waits to merge them, and that is ten times the storage bill "
                  "for the same unique data. The word is historical and it costs people "
                  "an argument every time."),
            ("math", [
                "F = 10      L = 5      ingest 50 MB/s      4 kB pages, 128 B rows, ⅔ fill",
                "",
                "engine             read        update        memory      bandwidth at 50 MB/s",
                "levelled LSM          5            25         11/10                1.25 GB/s",
                "tiered LSM           50             5            10              250.00 MB/s",
                "B-tree                4   125/4 = 31.25        3/2                1.56 GB/s",
                "",
                "levelled   RA = L        UA = L·F/2      MA = 1 + 1/F",
                "tiered     RA = L·F      UA = L          MA = F",
                "B-tree     RA = height   UA = page/row   MA = 1/fill",
            ]),
            ("p", "The two LSM rows are the same tree with two compaction policies. A "
                  "levelled tree merges each incoming run into the level below "
                  "immediately, so each level holds one sorted run and a lookup probes "
                  "`L` of them — at the cost of rewriting `F/2` bytes per byte per level. "
                  "A tiered tree lets runs accumulate and merges `F` of them at once, so "
                  "it writes each byte once per level and a lookup has `F` runs to search "
                  "on every level. `RA` and `UA` swap places almost exactly."),
            ("example", ("Where a B-tree's triple comes from",
                         "Nothing in the B-tree row is a table lookup. Its read "
                         "amplification is the height — `4`, from a billion keys at a "
                         "fanout of `500`, by the integer search of “The Height of a "
                         "B-tree”. Its update amplification is page over row: writing a "
                         "whole `4 000 B` page to change a `128 B` row is "
                         "`4 000/128 = 31.25`. Its memory amplification is one over the "
                         "fill factor: pages kept about two-thirds full occupy "
                         "`1/(2/3) = 3/2` times the space of the rows in them.")),
            ("h3", "The bandwidth question"),
            ("p", "Compaction bandwidth is `ingest × UA`, and it is the number a device "
                  "is chosen against. At `50 MB/s` the levelled tree needs `1.25 GB/s`, "
                  "the B-tree `1.56 GB/s` and the tiered tree `250.00 MB/s`. The tiered "
                  "engine is the only one of the three that a modest device can feed, "
                  "and it is also the one that will probe fifty runs to answer a lookup. "
                  "That is the trade stated in the two units that matter."),
            ("p", "So the way to use the triangle is not to rank the corners. It is to "
                  "name the amplification your workload cannot afford and then read what "
                  "the other two cost. A write-heavy ingest pipeline that is queried "
                  "rarely can live at the tiered corner. A point-lookup service on "
                  "expensive storage cannot afford `MA = 10` and will not go there. A "
                  "workload with both constraints is a workload that needs two engines."),
            ("p", "What the triple does not include: compression, which moves `MA` and "
                  "nothing else; a block cache, which moves the <em>observed</em> `RA` "
                  "without moving the engine's; and any constant factor at all. These are "
                  "ratios, so they compare shapes rather than products, and an "
                  "implementation can be a factor of two better or worse than its shape "
                  "at every corner."),
        ],
        "lab": ("storage", {
            "mode": "rum",
            "panel_title": "Set the fanout, the levels and the row size",
            "panel_intro": (
                "Each engine's triple comes out of the same parameters, and the bandwidth "
                "beside it is the ingest rate times its update amplification. Drop the "
                "fanout to `4` and watch the levelled and tiered corners move in opposite "
                "directions while the B-tree, which has no `F`, sits still."
            ),
        }),
        "steps_title": "Placing a workload on the triangle",
        "steps_intro": "The engine is chosen last. The first three steps are about the workload and the device.",
        "steps": [
            ("Write down what the workload demands, in the same three units",
             "How many lookups a second and how many of them miss; how many bytes a "
             "second arrive; how much storage you are willing to buy. Those are the read, "
             "update and memory sides, stated before any engine is named."),
            ("Compute each engine's triple from its own parameters",
             "`L` and `F` give both LSM rows. The page size, the row size and the fill "
             "factor give the B-tree's update and memory amplification, and its height "
             "gives its read amplification."),
            ("Multiply every update amplification by the ingest rate",
             "That is the sustained write bandwidth each engine requires. Compare the "
             "three numbers against the device you actually have, and some corners will "
             "disappear before you have chosen anything."),
            ("Name the corner you are paying in and check you can afford it",
             "Every engine is expensive somewhere. The decision is finished when you can "
             "say which amplification you are paying and what it costs in the unit it is "
             "measured in — probes, bytes a second, or terabytes."),
        ],
        "worked": {
            "title": "Three engines at F = 10, L = 5, ingesting 50 MB/s",
            "intro": [
                "Same parameters, three shapes, and then the one column that turns the "
                "comparison into a hardware decision."
            ],
            "lines": [
                "F = 10   L = 5   ingest 50 MB/s   4 kB pages   128 B rows   ⅔ fill   N = 10⁹, B = 500",
                "",
                "levelled LSM     read    L                          =      5",
                "                 update  L · F/2                    =     25",
                "                 memory  1 + 1/F                    =  11/10 = 1.1",
                "                 bandwidth  25 × 50 MB/s            =   1.25 GB/s",
                "",
                "tiered LSM       read    L · F                      =     50",
                "                 update  L                          =      5",
                "                 memory  F                          =     10",
                "                 bandwidth   5 × 50 MB/s            = 250.00 MB/s",
                "",
                "B-tree           read    height at N = 10⁹, B = 500 =      4",
                "                 update  4 000 / 128                =  125/4 = 31.25",
                "                 memory  1 / (2/3)                  =    3/2 = 1.5",
                "                 bandwidth  31.25 × 50 MB/s         =   1.56 GB/s",
            ],
            "after": [
                "Read down each block and then across. Every engine is best at something: "
                "the tiered tree writes the least, the B-tree reads the least, the "
                "levelled tree stores the least. Every engine is worst at something too, "
                "and the worst figure is always the direct consequence of the best one.",
                "None of the three bandwidth figures is `50 MB/s`. That is the "
                "misconception the page is built around, and it is the most expensive "
                "arithmetic error in this course: a device chosen against the ingest rate "
                "is short by a factor of between five and thirty-one, and the failure "
                "arrives weeks later as compaction debt rather than immediately as an "
                "error.",
                "For a faded rehearsal, drop the fanout to `4` and keep five levels. The "
                "supplied first move is that the levelled update amplification falls to "
                "`10`. Compute all three triples at `F = 4`, say which engine moved most "
                "and which did not move at all, and then compute the three bandwidths at "
                "the same `50 MB/s`. Check them in the lab before opening the quiz.",
            ],
        },
        "quiz_title": "Corners, and what each one costs",
        "quiz": [
            {"q": "At `F = 10` and `L = 5`, which engine writes the fewest bytes per byte ingested, and what does it pay for that?",
             "a": ["The levelled LSM, paying with `11/10` memory amplification",
                   "The tiered LSM, paying with `50` probes a lookup and `10` copies of every key",
                   "The B-tree, paying with a height of `4`",
                   "The tiered LSM, and it pays nothing; it is strictly better"],
             "c": 1,
             "why": "The tiered tree's update amplification is `L = 5`, against `25` "
                    "levelled and `31.25` for the B-tree. It pays at the other two "
                    "corners: `RA = L·F = 50` and `MA = F = 10`. Nothing is strictly "
                    "better; that is what the conjecture says."},
            {"q": "A levelled LSM at `F = 10`, `L = 5` ingests `50 MB/s`. What sustained write bandwidth does its device need?",
             "a": ["`50 MB/s`", "`250 MB/s`", "`1.25 GB/s`", "`1.56 GB/s`"],
             "c": 2,
             "why": "`ingest × UA = 50 MB/s × 25 = 1.25 GB/s`. `250 MB/s` is the tiered "
                    "tree's requirement, at `UA = 5`, and `1.56 GB/s` is the B-tree's, at "
                    "`UA = 31.25`. The one figure that is never the answer is the ingest "
                    "rate itself."},
            {"q": "Where does a B-tree's update amplification of `31.25` come from?",
             "a": ["From the height, `4`, times the fanout over eight",
                   "From writing a whole `4 000 B` page to change a `128 B` row",
                   "From the two-thirds fill factor",
                   "From rewriting every level, as an LSM does"],
             "c": 1,
             "why": "`4 000/128 = 125/4 = 31.25`: the page is the unit of writing and the "
                    "row is the unit of change. The fill factor gives the memory "
                    "amplification, `1/(2/3) = 3/2`, and the height gives the read "
                    "amplification. A B-tree updates in place and rewrites no levels."},
            {"q": "Which engine minimises all three amplifications at once?",
             "a": ["The levelled LSM, at a high enough fanout",
                   "The B-tree, because it updates in place",
                   "None; the question to ask is which corner the workload can afford",
                   "The tiered LSM, once a Bloom filter is added"],
             "c": 2,
             "why": "That is the content of the trade-off. A filter genuinely does repair "
                    "the tiered tree's read amplification, and it does so by spending "
                    "memory — which is a fourth resource, not a free lunch, and it leaves "
                    "`MA = 10` on disk exactly where it was."},
        ],
        "mistakes": [
            ("Sizing a device to the ingest rate",
             "The device sees `ingest × UA`. At `50 MB/s` into a levelled tree that is "
             "`1.25 GB/s`, and into a B-tree `1.56 GB/s`. The engine does not fail when "
             "the device is undersized; it falls behind, and falling behind raises the "
             "read amplification as well, so the system gets worse in two directions from "
             "one bad multiplication."),
            ("Reading the triangle as a ranking",
             "There is no best corner. A page that says “tiered engines are "
             "write-optimised” has said something true and useless: the sentence that "
             "helps names the two prices as well — fifty probes on a lookup and ten times "
             "the storage. Any comparison quoting one amplification is a comparison with "
             "the cost removed."),
            ("Reading memory amplification as RAM",
             "It is bytes stored per byte of unique data, and it lands on the storage "
             "bill. `MA = 10` for a tiered tree means ten copies of a key on disk waiting "
             "to be merged, which is a decision about how much storage to buy — not about "
             "how much memory the process needs."),
        ],
        "standard": ("Finish when “which engine is best” reads as a malformed question.",
                     "You should be able to compute all three amplifications for a "
                     "levelled tree, a tiered tree and a B-tree from stated parameters, "
                     "turn each update amplification into a device bandwidth, and name "
                     "which corner a given workload is paying in."),
        "note": (
            "Every number on this page assumed the write reached durable storage. “fsync "
            "and Group Commit” is where that assumption gets priced: a single fsync caps "
            "durable commits at `1/t_fsync` a second no matter what the rest of the "
            "engine can do, and the only way past it costs latency."
        ),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "fsync-and-group-commit",
        "title": "fsync and Group Commit",
        "module": "Durability and layout",
        "one_line": "Compute the durable write ceiling from the fsync time, what grouping `B` commits buys, and the batch wait it costs.",
        "summary": (
            "Durability is a count of fsyncs. One commit per fsync on a `10 ms` device is "
            "`100` durable writes a second, whatever the CPU and the network could have "
            "done. Grouping sixty-four commits into one fsync makes it `6 400` a second — "
            "paid for with a wait to fill the batch, which is why commit latency has a "
            "minimum at a batch size rather than falling for ever."
        ),
        "key": [
            "durable writes a second ≤ 1 / t_fsync              one commit per fsync",
            "grouped B at a time     ≤ B / t_fsync              t_fsync/B each",
            "",
            "t_fsync = 10 ms      B = 1        100 a second",
            "                     B = 64     6 400 a second,  156.3 µs of fsync each",
            "",
            "paid for with a wait:  (B − 1)/2λ to fill the batch, then the queue",
        ],
        "key_label": "The durability ceiling, what grouping buys, and what the batch costs",
        "concepts_intro": (
            "One hard ceiling, one way around it, and the price of that way — which is "
            "the only part that needs arithmetic."
        ),
        "concepts": [
            ("Durability is a count of fsyncs, not a count of bytes",
             "A `write()` that returns has put bytes in the operating system's page cache. "
             "The disk learns about them when something calls `fsync`, and until then a "
             "power loss takes them. So the durable write rate is bounded by how many "
             "fsyncs a second the device can complete: `1/t_fsync`, which at `10 ms` is "
             "`100` — a number that has nothing to do with how fast anything else is."),
            ("Grouping divides one fsync among a batch",
             "Nothing says one commit must get one fsync. Collect `B` commits, write them "
             "all, call `fsync` once, and acknowledge all `B`: the ceiling becomes "
             "`B/t_fsync` and each write carries `t_fsync/B` of the cost. At `B = 64` on "
             "a `10 ms` device that is `6 400` durable writes a second and `156.3 µs` of "
             "fsync apiece, on the same disk."),
            ("The batch is paid for in latency, and the total has a minimum",
             "A write that arrives first waits for the rest of its batch — about "
             "`(B − 1)/2λ` at arrival rate `λ` — and then waits in the queue in front of "
             "the fsync. Raising `B` lengthens the first wait and shortens the second, so "
             "commit latency falls, flattens and rises again. On the worked settings it "
             "bottoms at `B = 121` and `29.04 ms`."),
        ],
        "read_title": "The durability ceiling, and what a batch buys and costs",
        "read_intro": "Why a returning write is not a durable one, what grouping does to the ceiling, and where the latency minimum sits.",
        "body": [
            ("def", ("Durable write, fsync, group commit",
                     "A write is <strong>durable</strong> when it survives the loss of "
                     "power. <strong>fsync</strong> is the call that forces buffered "
                     "bytes onto the device and returns when they are there; `t_fsync` is "
                     "how long it takes. <strong>Group commit</strong> is the practice of "
                     "batching `B` pending commits behind a single fsync and "
                     "acknowledging them together.",
                     "The durable write rate is at most `1/t_fsync` without grouping and "
                     "`B/t_fsync` with it. Both are ceilings, not achieved rates.")),
            ("p", "The misconception this lesson is aimed at is that a successful "
                  "`write()` means the data is safe. It means the bytes reached the page "
                  "cache, which is memory, which is exactly the thing a power loss "
                  "empties. Every engine that promises durability is therefore paying for "
                  "fsyncs, and the count of them is the whole budget."),
            ("math", [
                "t_fsync = 10 ms = 0.01 s          arrivals λ = 5 000 a second",
                "",
                "B = 1      cap 1/0.01                   =   100 durable writes a second",
                "           batches arrive at 5 000/s, served at 100/s   →   ρ = 50",
                "           no steady state: the backlog grows without bound",
                "",
                "B = 64     cap 64/0.01                  = 6 400 durable writes a second",
                "           fsync per write 0.01/64      = 156.3 µs",
                "           fill wait (64 − 1)/(2 × 5 000)= 6.30 ms",
                "           batches 5 000/64 = 78.125/s against 100/s  →  ρ = 0.781",
                "           queue + fsync 1/(100 − 78.125)= 45.71 ms",
                "           commit latency 6.30 + 45.71  = 52.01 ms",
            ]),
            ("p", "The `B = 1` row is worth reading twice. At five thousand writes a "
                  "second arriving and one hundred fsyncs a second available, the "
                  "utilisation is `50` and there is no mean latency to quote at all — the "
                  "backlog simply grows. The ceiling arrives as a queueing fact rather "
                  "than as an assertion, which is the M/M/1 model of Queues and "
                  "Utilisation reused rather than a second model invented here."),
            ("h3", "What the batch costs"),
            ("p", "Two waits, moving in opposite directions. The <strong>fill wait</strong> "
                  "is how long a write sits while its batch assembles, about "
                  "`(B − 1)/2λ` on average, and it grows linearly in `B`. The "
                  "<strong>queue</strong> in front of the fsync shrinks as `B` grows, "
                  "because batches arrive at `λ/B` while the fsync still serves at "
                  "`1/t_fsync`, so the utilisation `ρ = λ t_fsync/B` falls. Adding the "
                  "two gives a curve with an interior minimum."),
            ("example", ("Scanning the curve",
                         "At `λ = 5 000` and `t_fsync = 10 ms`: `B = 64` gives `6.30 ms` "
                         "of fill and `45.71 ms` of queue, `52.01 ms` in total. `B = 121` "
                         "gives `12.00 ms` and `17.04 ms`, `29.04 ms` in total — the "
                         "lowest on the curve. `B = 256` gives `25.50 ms` and `12.43 ms`, "
                         "`37.93 ms`, and is past the minimum: the batch is now the "
                         "problem. The durable ceiling rose the whole way, from `6 400` "
                         "to `25 600` a second, while the latency turned around.")),
            ("p", "The lab finds that minimum by evaluating every `B` rather than by a "
                  "formula, and it says so. A closed form exists for this shape of "
                  "bargain — a fixed cost amortised over a batch against a cost that "
                  "grows with the batch — and it belongs to “The EOQ Formula Without "
                  "Calculus” on the Operations Research path. The same trade appears "
                  "again as “Batching: Cost and Latency” in Scaling Laws and Cost, with "
                  "throughput in place of durability and a per-item cost in place of a "
                  "holding cost."),
            ("p", "Two things this model takes on trust, both of which have cost people "
                  "data. It assumes `t_fsync` is what the device actually does, and a "
                  "device with a volatile write cache that acknowledges an fsync before "
                  "the platter has it will report a delightful figure and lose your "
                  "commits anyway — measure it, do not read it off a datasheet. And it "
                  "assumes a single thread issuing the fsyncs, which is what makes the "
                  "M/M/1 arithmetic apply."),
        ],
        "lab": ("storage", {
            "mode": "fsync",
            "panel_title": "Set the fsync time, the batch and the arrival rate",
            "panel_intro": (
                "The ceiling is `1/t` and the grouped ceiling `B/t`; the latency beside "
                "them is the wait to fill the batch plus the sojourn of the batch at the "
                "fsync. Take the batch down to `1` and watch the queue lose its steady "
                "state entirely, then walk it up and find where the total turns around."
            ),
        }),
        "steps_title": "Pricing durability",
        "steps_intro": "The ceiling takes one division. The interesting part is the curve underneath it.",
        "steps": [
            ("Measure `t_fsync` on the device you will use",
             "Not the datasheet figure, and not the write latency. An fsync is a "
             "round-trip to durable media, and a device that returns from it too quickly "
             "is usually acknowledging from a volatile cache."),
            ("Divide one second by it",
             "`1/t_fsync` is the ungrouped ceiling: `100` a second at `10 ms`, `1 000` at "
             "`1 ms`. Nothing above the line matters if this number is below what the "
             "workload needs — no amount of CPU or network moves it."),
            ("Choose `B` and recompute the ceiling and the per-write cost",
             "`B/t_fsync` durable writes a second, at `t_fsync/B` of fsync each. This is "
             "the only lever that raises the ceiling without changing hardware."),
            ("Add the fill wait and the queue, then scan `B`",
             "`(B − 1)/2λ` plus the sojourn at utilisation `ρ = λ t_fsync/B`. Evaluate it "
             "across the batch sizes you would consider and take the minimum; it is "
             "interior, so neither the smallest nor the largest `B` wins."),
        ],
        "worked": {
            "title": "A 10 ms fsync under 5 000 writes a second",
            "intro": [
                "One division for the ceiling, then the two waits that decide the batch."
            ],
            "lines": [
                "t_fsync = 10 ms = 0.01 s          arrivals λ = 5 000 a second",
                "",
                "B = 1     ceiling 1/0.01                     =    100 durable writes/s",
                "          batches at 5 000/s served at 100/s →    ρ = 50, no steady state",
                "",
                "B = 64    ceiling 64/0.01                    =  6 400 durable writes/s",
                "          fsync per write  0.01/64           =  156.3 µs",
                "          fill wait  (64 − 1)/(2 × 5 000)    =   6.30 ms",
                "          ρ = λ·t/B = 5 000 × 0.01 / 64      =   0.781",
                "          queue + fsync  1/(100 − 78.125)    =  45.71 ms",
                "          commit latency 6.30 + 45.71        =  52.01 ms",
                "",
                "scanning the curve",
                "  B =  64   ceiling  6 400/s   fill  6.30 ms   queue 45.71 ms   total 52.01 ms",
                "  B = 121   ceiling 12 100/s   fill 12.00 ms   queue 17.04 ms   total 29.04 ms  lowest",
                "  B = 128   ceiling 12 800/s   fill 12.70 ms   queue 16.41 ms   total 29.11 ms",
                "  B = 256   ceiling 25 600/s   fill 25.50 ms   queue 12.43 ms   total 37.93 ms",
            ],
            "after": [
                "The two middle columns move in opposite directions and neither of them "
                "is the answer on its own. The ceiling rises monotonically with `B` all "
                "the way to `25 600` a second, so a page that reported only throughput "
                "would recommend the largest batch available — and it would be "
                "recommending `37.93 ms` of commit latency over `29.04 ms`.",
                "The minimum here is `B = 121`, found by evaluating the curve rather than "
                "by differentiating it. The closed form for this shape of bargain belongs "
                "to “The EOQ Formula Without Calculus” on the Operations Research path; "
                "this course chooses `B` by looking, and says that a formula exists and "
                "where it lives.",
                "For a faded rehearsal, keep `λ = 5 000` and take the fsync down to `1 ms` "
                "— a device an order of magnitude better. The supplied first move is the "
                "new ungrouped ceiling: `1 000` durable writes a second. Find the batch "
                "that minimises commit latency and the latency there, then say what "
                "happened to both relative to the `10 ms` device. Check in the lab before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "Ceilings, batches and waits",
        "quiz": [
            {"q": "A device completes an fsync in `10 ms`. With one commit per fsync, what is the durable write ceiling?",
             "a": ["`10` a second", "`100` a second", "`1 000` a second", "It depends on the write size"],
             "c": 1,
             "why": "`1/t_fsync = 1/0.01 = 100` durable writes a second. The write size "
                    "does not enter: an fsync is a round trip to durable media, and its "
                    "cost is dominated by that round trip rather than by the bytes riding "
                    "on it — which is exactly why batching works at all."},
            {"q": "The same device groups `64` commits behind one fsync. What does each write now pay in fsync cost, and what is the ceiling?",
             "a": ["`156.3 µs` each, ceiling `6 400` a second",
                   "`10 ms` each, ceiling `6 400` a second",
                   "`156.3 µs` each, ceiling `100` a second",
                   "`640 µs` each, ceiling `1 562` a second"],
             "c": 0,
             "why": "`t_fsync/B = 0.01/64 = 156.3 µs` and `B/t_fsync = 6 400` a second. "
                    "The fsync still takes `10 ms`; what changed is how many "
                    "acknowledgements it carries. Both halves have to move together — a "
                    "higher ceiling and a lower per-write cost are the same fact."},
            {"q": "`write()` has returned successfully. Is the data durable?",
             "a": ["Yes; a successful write is a completed write",
                   "No; the bytes are in the page cache, and a power loss takes them until something calls fsync",
                   "Yes, provided the file was opened for synchronous writing",
                   "Only if the write was smaller than one page"],
             "c": 1,
             "why": "A returning `write()` means the operating system accepted the bytes "
                    "into memory. Durability begins at the fsync. Opening with "
                    "synchronous semantics does force the flush, and it does so by paying "
                    "the `t_fsync` on every write — which puts you back at the `100` a "
                    "second ceiling rather than exempting you from it."},
            {"q": "Raising the batch size raises the durable ceiling every time. Why is the largest batch not the best choice?",
             "a": ["Because very large batches overflow the log buffer",
                   "Because the wait to fill the batch grows linearly in `B`, and past a point it grows faster than the queue shrinks",
                   "Because the fsync itself takes longer for a larger batch",
                   "Because the utilisation rises with `B`"],
             "c": 1,
             "why": "Fill wait is about `(B − 1)/2λ` and the queue shrinks because "
                    "`ρ = λt/B` falls, so the sum turns around — here at `B = 121`, after "
                    "which the total rises again. The utilisation falls rather than "
                    "rising with `B`, which is precisely the half of the trade that makes "
                    "batching worth doing at all."},
        ],
        "mistakes": [
            ("Reading a successful `write()` as durability",
             "It is an acknowledgement from memory. Everything an engine promises about "
             "surviving power loss is bought with fsyncs, and the number of them a second "
             "is a hard ceiling set by the device. A system whose durability claim is not "
             "backed by a count of fsyncs per second does not have a durability claim."),
            ("Quoting the grouped ceiling as though latency were unchanged",
             "`64` commits a batch raises the ceiling from `100` to `6 400` a second and "
             "adds `6.30 ms` of fill wait before the queue is even considered. Throughput "
             "and latency move in opposite directions here, and the honest report gives "
             "both figures at the chosen `B`."),
            ("Raising `B` until throughput is sufficient and stopping",
             "The latency minimum is interior. At these settings `B = 256` clears any "
             "plausible throughput target and costs `37.93 ms` where `B = 121` costs "
             "`29.04 ms`. Choosing the batch on the throughput axis alone lands on the "
             "wrong side of a curve that was cheap to evaluate."),
        ],
        "standard": ("Finish when a durability claim sounds like a rate, and a batch size sounds like a latency decision.",
                     "You should be able to state the ungrouped ceiling from an fsync "
                     "time, compute what a given batch does to the ceiling and to the "
                     "per-write cost, and find the batch that minimises commit latency by "
                     "evaluating the curve."),
        "note": (
            "The fsync caps how quickly durable bytes land. What a query has to read back "
            "is decided somewhere else entirely — by how the values are laid out on the "
            "page. “Row vs Column Storage” counts the bytes a scan touches each way and "
            "finds the query on which the answer reverses."
        ),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "row-vs-column-storage",
        "title": "Row vs Column Storage",
        "module": "Durability and layout",
        "one_line": "Compute the bytes a scan reads in each layout and the time each takes, then find the query on which the ordering reverses.",
        "summary": (
            "A scan reads whatever the layout makes contiguous. A row store reads whole "
            "rows even when the query named three columns of twenty; a column store reads "
            "only the named columns, and compresses them better because a column holds "
            "like values. Over a billion two-hundred-byte rows that is `100.00 GB` "
            "against `6.00 GB` — and one I/O against twenty when the query wants a whole "
            "row back."
        ),
        "key": [
            "row store      bytes = rows × full row width ÷ row ratio",
            "column store   bytes = rows × Σ named column widths ÷ column ratio",
            "",
            "10⁹ rows, 200 B a row, 20 columns, 3 named, 1 GB/s scan",
            "        row store      100.00 GB      100.00 s",
            "        column store     6.00 GB        6.00 s        16.67× faster",
            "",
            "one whole row:   1 I/O in the row store,   20 in the column store",
        ],
        "key_label": "Bytes scanned each way, and the query that reverses the answer",
        "concepts_intro": (
            "One formula per layout, one compression ratio that is part of the layout "
            "rather than separate from it, and one query that flips the result."
        ),
        "concepts": [
            ("A scan reads what the layout makes contiguous",
             "In a row store a row is one run of bytes, so reading any column of it reads "
             "all of it: a query naming three columns of twenty still moves the full "
             "`200 B` per row. In a column store each column is its own run, so the same "
             "query moves `3 × 10 B` per row. Neither engine is reading the wrong number "
             "of rows; they are reading different amounts of each row."),
            ("The compression ratio belongs to the layout",
             "A column holds a million values of one type and often one distribution, "
             "which is what compresses; a row holds a timestamp, a name and a price side "
             "by side, which does not. Quoting a columnar scan without its ratio hides "
             "half the effect — here `5×` against `2×`, which turns a factor of ten in "
             "bytes named into a factor of `16.67` in bytes read."),
            ("The crossover is a column count, and there is a query past every crossover",
             "The two scans tie when the named columns reach "
             "`columns × column ratio / row ratio`, which at these ratios is `50` of "
             "`20` — so no selection flips the scan here. The flip comes from a different "
             "query: fetching one whole row is `1` I/O in a row store and `20` in a "
             "column store, one page per column."),
        ],
        "read_title": "Bytes scanned, and the query where the answer reverses",
        "read_intro": "Two formulas, the compression that is part of each of them, and the point lookup that undoes the whole comparison.",
        "body": [
            ("def", ("Row store, column store, bytes scanned",
                     "A <strong>row store</strong> keeps the values of one row "
                     "contiguously; a <strong>column store</strong> keeps the values of "
                     "one column contiguously. <strong>Bytes scanned</strong> is the "
                     "volume a query must read from storage.",
                     "For `r` rows of total width `w` across `c` columns, with `j` "
                     "columns named and compression ratios `ρ_row` and `ρ_col`, the row "
                     "store scans `r·w/ρ_row` and the column store scans "
                     "`r·(w/c)·j/ρ_col`.")),
            ("p", "The row store's formula contains no `j`. That is the entire "
                  "asymmetry: naming fewer columns cannot make a row store read less, "
                  "because the unit it stores and the unit the device delivers are both "
                  "the row. A query naming one column of twenty scans exactly as many "
                  "bytes as a query naming all twenty."),
            ("math", [
                "10⁹ rows     200 B a row     20 columns, so 10 B a column     3 named",
                "row store compresses 2×      column store compresses 5×      scan 1 GB/s",
                "",
                "row store      10⁹ × 200 B ÷ 2          = 100.00 GB  ÷ 1 GB/s  = 100.00 s",
                "column store   10⁹ × (3 × 10 B) ÷ 5     =   6.00 GB  ÷ 1 GB/s  =   6.00 s",
                "",
                "ratio                                                          16.67×",
                "",
                "crossover      columns × col ratio / row ratio = 20 × 5/2  =  50 columns",
                "               there are only 20, so no selection flips the scan here",
            ]),
            ("p", "A factor of `16.67` from a query that named a seventh of the columns "
                  "is more than the seven you might expect, and the extra comes from the "
                  "compression ratios: `10/3` from the columns and `5/2` from the "
                  "compression, multiplied. That is why the ratio has to travel with the "
                  "claim."),
            ("h3", "Where the answer reverses"),
            ("p", "Set the two byte counts equal and solve for the number of named "
                  "columns: `j* = c × ρ_col/ρ_row`. At `c = 20`, `ρ_col = 5` and "
                  "`ρ_row = 2` that is `50`, which is past all twenty columns — so at "
                  "these ratios no scan, however wide, makes the row store cheaper. Drop "
                  "the columnar ratio to `2×`, which is what happens when the columns "
                  "hold high-cardinality values that do not compress, and the crossover "
                  "falls to exactly `20`: the two layouts tie on a query that reads "
                  "everything."),
            ("example", ("The query that actually flips it",
                         "Fetch one whole row by key. In a row store it is one page read: "
                         "the row is contiguous, so the page holding any of its columns "
                         "holds all of them. In a column store it is twenty page reads, "
                         "one per column, because the twenty values live in twenty "
                         "different places. That is a factor of twenty in the row store's "
                         "favour on the same table, and it is not a scan at all.")),
            ("p", "So “columnar is always faster” is a claim about analytical scans "
                  "wearing the clothes of a claim about storage. The honest form names "
                  "the query shape: for scans over a few columns of many rows, columnar "
                  "by a large factor; for retrieving whole rows one at a time, row store "
                  "by a factor of the column count. A system doing both is a system that "
                  "keeps the data twice, and that is a decision with a storage bill "
                  "rather than a clever trick."),
            ("p", "Two things held fixed here. The scan runs at `1 GB/s` in both layouts, "
                  "so nothing in the comparison is hiding a bandwidth difference — the "
                  "whole effect is bytes. And the compression ratio is an input on this "
                  "course rather than something derived: what a codec achieves on your "
                  "data is measured, and the break-even between the ratio and the CPU it "
                  "costs to decompress belongs to Scaling Laws and Cost."),
        ],
        "lab": ("storage", {
            "mode": "columnar",
            "panel_title": "Set the row, the columns named and the compression",
            "panel_intro": (
                "Bytes scanned is rows times the width the layout forces you to read, "
                "divided by what that layout compresses to. Walk the named columns from "
                "one to twenty and watch the columnar time climb toward the row store's; "
                "then drop the columnar ratio to `2×` and watch the crossover move inside "
                "the table."
            ),
        }),
        "steps_title": "Costing a query against a layout",
        "steps_intro": "Four steps, and the fourth is the one that keeps the answer honest.",
        "steps": [
            ("Write down what the query actually needs",
             "Which columns, and how many rows. The column list is the only input the two "
             "formulas disagree about, and it is the one people summarise away when they "
             "describe a workload."),
            ("Compute both byte counts",
             "`rows × full width ÷ row ratio` and `rows × named widths ÷ column ratio`. "
             "Keep both compression ratios in the arithmetic; leaving them out is the "
             "most common way to get a plausible wrong answer here."),
            ("Divide both by the same bandwidth",
             "The comparison is about bytes, so hold the scan rate fixed across the two "
             "layouts. If you want to argue that one layout also reads faster, that is a "
             "separate claim and it needs its own measurement."),
            ("Ask the other query",
             "Price a whole-row fetch as well as the scan: `1` I/O against one per "
             "column. A layout decision made on the scan alone is a decision made on half "
             "of the workload."),
        ],
        "worked": {
            "title": "Three of twenty columns over a billion rows",
            "intro": [
                "Two formulas, the same bandwidth, and then the query the comparison "
                "forgets."
            ],
            "lines": [
                "10⁹ rows      200 B a row      20 columns → 10 B a column      3 named",
                "row store compresses 2×        column store compresses 5×      scan 1 GB/s",
                "",
                "row store      10⁹ × 200 B      = 200.00 GB   ÷ 2   = 100.00 GB",
                "                                              ÷ 1 GB/s   = 100.00 s",
                "column store   10⁹ × 3 × 10 B   =  30.00 GB   ÷ 5   =   6.00 GB",
                "                                              ÷ 1 GB/s   =   6.00 s",
                "",
                "speedup        100.00 / 6.00                        =  16.67×",
                "   of which    20/3 from the columns named          =   6.67×",
                "               5/2  from the compression            =   2.50×",
                "",
                "crossover      20 × 5/2                             =  50 columns",
                "               only 20 exist, so no scan flips it at these ratios",
                "",
                "one whole row  row store    1 I/O      the row is contiguous",
                "               column store 20 I/O     one page per column",
            ],
            "after": [
                "The row store is not reading more rows. It is reading whole rows, "
                "because a row is what is contiguous there, and the query named three "
                "columns out of twenty. Every byte of the difference is layout.",
                "The crossover is worth computing even when it lands outside the table, "
                "because it says how far outside. A query would have to name fifty of "
                "twenty columns to make the row store cheaper, which is not close; drop "
                "the columnar ratio to `2×` and it falls to exactly `20`, at which point "
                "a full-width scan ties. That is the number to quote when someone asks "
                "how robust the comparison is.",
                "For a faded rehearsal, keep the table and make the query name ten "
                "columns instead of three. The supplied first move is that the columnar "
                "scan becomes `20.00 GB`. Compute the two times and the ratio, then say "
                "what the crossover becomes if the columnar compression falls to `3×`. "
                "Check all three in the lab before opening the quiz.",
            ],
        },
        "quiz_title": "Bytes, layouts and the query shape",
        "quiz": [
            {"q": "A query names `3` of `20` columns over `10⁹` rows of `200 B`. How many bytes does a row store scan, at a `2×` compression ratio?",
             "a": ["`15.00 GB` — the named columns, compressed",
                   "`30.00 GB` — the named columns, uncompressed",
                   "`100.00 GB` — the whole table, compressed",
                   "`200.00 GB` — the whole table, uncompressed"],
             "c": 2,
             "why": "`10⁹ × 200 B = 200.00 GB` uncompressed, `÷ 2 = 100.00 GB`. A row "
                    "store's formula contains no term for the columns named: the row is "
                    "the contiguous unit, so reading any of it reads all of it. The "
                    "`15.00 GB` answer applies the columnar formula with the row store's "
                    "ratio."},
            {"q": "On the same table, what does fetching one complete row cost in each layout?",
             "a": ["`1` I/O in both; a key lookup is a key lookup",
                   "`1` I/O in the row store, `20` in the column store",
                   "`20` in the row store, `1` in the column store",
                   "`1` in the row store, `3` in the column store"],
             "c": 1,
             "why": "A row store holds the row contiguously, so one page read gets all "
                    "twenty values. A column store holds each column in its own run, so "
                    "the twenty values are in twenty places and cost twenty reads. `3` "
                    "would be the cost of fetching the three columns the earlier scan "
                    "named, which is a different query."},
            {"q": "The columnar compression ratio falls from `5×` to `2×` while the row store stays at `2×`. What is the crossover in columns named?",
             "a": ["`8`", "`20`", "`50`", "There is no crossover once the ratios are equal"],
             "c": 1,
             "why": "`j* = columns × ρ_col/ρ_row = 20 × 2/2 = 20`. With equal ratios the "
                    "two layouts tie precisely when the query names every column, which "
                    "is the sensible answer: reading all of a row is reading all of a row "
                    "however it is stored. `50` is the crossover at the original `5×`."},
            {"q": "What is the honest form of “columnar is always faster”?",
             "a": ["“Columnar is faster once the table is large enough”",
                   "“Columnar is faster for scans naming few columns of many rows, and slower for retrieving whole rows”",
                   "“Columnar is faster whenever the data compresses”",
                   "“Columnar is faster unless the query has a predicate”"],
             "c": 1,
             "why": "The claim has to name the query shape, because the layouts reverse "
                    "between the two shapes: `16.67×` in favour of columns on the scan "
                    "here and `20×` in favour of rows on the whole-row fetch. Table size "
                    "scales both layouts equally, and compression helps whichever layout "
                    "is doing the compressing."},
        ],
        "mistakes": [
            ("Treating the comparison as a property of the storage rather than of the query",
             "The same table gives `16.67×` to the column store on a three-column scan "
             "and `20×` to the row store on a whole-row fetch. A layout is fast at a query "
             "shape, and the sentence that omits the shape will be quoted at the one "
             "workload where it is backwards."),
            ("Leaving the compression ratio out of the comparison",
             "Here it is `2×` against `5×`, and it supplies `2.50` of the `16.67`. A "
             "columnar figure quoted without its ratio is not checkable, and the ratio is "
             "the part most sensitive to the actual data — high-cardinality columns "
             "compress like rows do, and the advantage shrinks with them."),
            ("Costing a point lookup at a scan's rate",
             "A scan is priced in bytes at a bandwidth; a whole-row fetch is priced in "
             "I/Os at a seek. `1` against `20` is an I/O count, and converting it into "
             "bytes to compare it with the scan is the mistake the first lesson of this "
             "course exists to prevent."),
        ],
        "standard": ("Finish when the first question you ask about a layout is which query.",
                     "You should be able to compute bytes scanned in both layouts from a "
                     "row width, a column count, a selection and two compression ratios; "
                     "convert both to times at a stated bandwidth; and find the crossover "
                     "in named columns."),
        "note": (
            "Both scans here went to disk. How much of the data is on disk <em>at the "
            "moment a query asks for it</em> is a question about memory, and it is the "
            "cache arithmetic of Caching and Hit Rates wearing a different set of names. "
            "“Working Set and the Page Cache” is that callback, and it is deliberately "
            "not new material."
        ),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "working-set-and-the-page-cache",
        "title": "Working Set and the Page Cache",
        "module": "Durability and layout",
        "one_line": "Compute the page cache's hit rate from memory, dataset and skew, and the disk IOPS the misses leave behind.",
        "summary": (
            "The page cache is the cache you already know, with pages for objects and "
            "page reads for requests: `h = H(C,s)/H(N,s)`, and the disk still sees "
            "`(1 − h) × reads`. Sixty-four gigabytes over a five-hundred-gigabyte dataset "
            "is `12.80%` of the pages and, at classic Zipf skew, about `88.9%` of the "
            "reads — which is why “it is on disk, so every read is a disk read” is wrong "
            "by a factor of nine."
        ),
        "key": [
            "h = H(C, s) / H(N, s)          C pages resident of N, Zipf exponent s",
            "disk IOPS = (1 − h) × reads",
            "",
            "64 GB of 500 GB at 8 kB a page  →  C = 8 000 000 of N = 62 500 000 = 12.80%",
            "",
            "s = 1     h ≈ 88.905%    →   (1 − h) × 20 000 =  2 219 IOPS",
            "s = 0     h =  12.800%   →                      17 440 IOPS",
        ],
        "key_label": "The hit rate from memory, dataset and skew, and the IOPS it leaves",
        "concepts_intro": (
            "Nothing here is a new model. What is new is the vocabulary, and one property "
            "of the formula that decides how much memory is worth buying."
        ),
        "concepts": [
            ("The page cache is the cache you already know",
             "Caching and Hit Rates computed a hit rate from a cache size, a dataset size "
             "and a Zipf exponent. This is the same formula, called through the same "
             "function, with pages in place of objects and page reads in place of "
             "requests. The lesson is a callback: if you can size a cache you can size a "
             "page cache, and there is no second model to learn."),
            ("The skew is what makes a small cache worth having",
             "At classic Zipf skew, `12.80%` of the pages carry about `88.9%` of the "
             "reads — `6.9` times their share of the data. Uniform popularity would give "
             "exactly `12.80%`, the share itself. Every argument for buying memory is an "
             "argument about the skew, and the skew is measurable rather than assumed."),
            ("The number that matters is `(1 − h) × reads`",
             "A hit rate is a fraction and the disk is a device with an IOPS limit. At "
             "`20 000` page reads a second and `h ≈ 88.905%`, about `2 219` of them reach "
             "the disk; uniform popularity would send `17 440`. Both are true of the same "
             "memory over the same data, and only the second sounds like a system in "
             "trouble."),
        ],
        "read_title": "Pages, skew, and the reads that still reach the disk",
        "read_intro": "The same cache arithmetic in storage vocabulary, and what each doubling of memory actually buys.",
        "body": [
            ("def", ("Working set and page-cache hit rate",
                     "The <strong>page cache</strong> holds `C` pages of a dataset of `N` "
                     "pages in memory. Under Zipf popularity with exponent `s`, the "
                     "<strong>hit rate</strong> is `h = H(C,s)/H(N,s)`, where `H(n,s)` is "
                     "the generalised harmonic number `Σ 1/iˢ` over `i = 1…n`.",
                     "The <strong>disk IOPS</strong> the workload leaves is "
                     "`(1 − h) × reads`. At `s = 0` the formula collapses to `h = C/N`, "
                     "and every page is equally likely to be wanted.")),
            ("p", "Both sizes have to be converted into pages before anything else "
                  "happens. At an `8 kB` page a `500 GB` dataset is `62 500 000` pages "
                  "and `64 GB` of memory is `8 000 000` of them, so `C/N = 12.80%`. The "
                  "formula takes counts, not bytes, and a units error here moves the "
                  "answer more than the skew does."),
            ("math", [
                "page 8 kB     dataset 500 GB  →  N = 62 500 000 pages",
                "              memory   64 GB  →  C =  8 000 000 pages      C/N = 12.80%",
                "",
                "s = 1    h = H(8 000 000, 1) / H(62 500 000, 1)  ≈  88.905%     rounded",
                "         disk IOPS = (1 − 0.88905) × 20 000       ≈   2 219 a second",
                "",
                "s = 0    h = C/N = 16/125                         =  12.800%     exact",
                "         disk IOPS = (1 − 0.128) × 20 000         =  17 440 a second",
            ]),
            ("p", "The two rows are the lesson. The same memory holding the same share of "
                  "the same data serves about `88.9%` of the reads when popularity is "
                  "skewed and `12.8%` when it is not, and the difference at the disk is a "
                  "factor of nearly eight. Skew is not a detail of the workload; it is "
                  "the reason the page cache exists."),
            ("h3", "What each doubling of memory buys"),
            ("p", "Hold the dataset and the skew and walk the memory up by factors of "
                  "two. From a sixty-fourth of the data to a half, the hit rate goes "
                  "`77.553%`, `81.294%`, `85.036%`, `88.777%`, `92.518%`, `96.259%` — "
                  "about `3.74` points every time. That is what `H(C,1)` growing like the "
                  "logarithm of `C` looks like: equal <em>multiples</em> of memory buy "
                  "equal <em>absolute</em> improvements."),
            ("example", ("Diminishing returns, in the unit the disk cares about",
                         "The residual IOPS on those same six rows are `4 489`, `3 741`, "
                         "`2 993`, `2 245`, `1 496` and `748`. Each doubling removes about "
                         "`748` IOPS — the same amount every time, not the same fraction. "
                         "So the first doubling and the last one are worth the same to the "
                         "disk, and the memory to buy them is thirty-two times more "
                         "expensive on the last.")),
            ("p", "The hit rate on this page is rounded and the lab says so on its face. "
                  "Past `N = 40` pages the exact harmonic number is neither computable in "
                  "a redraw nor readable when printed — its denominator grows far faster "
                  "than the page — so `h` comes from a floating-point approximation to "
                  "`H(n,s)`. The lab prints the exact fraction at `N = 40`, `C = 4` "
                  "alongside, so the machinery producing the approximation is visible "
                  "rather than asserted. At `s = 0` the formula is `C/N` and stays exact "
                  "at any size."),
            ("p", "And the model is Zipf, which is a description of many real workloads "
                  "and a description of none of them exactly. `s` is measured from a "
                  "trace, not chosen; a real page cache also does read-ahead, which "
                  "converts some misses into sequential reads that the IOPS figure treats "
                  "too harshly, and holds dirty pages, which occupy `C` without serving "
                  "reads. The arithmetic is the right first estimate and it is not a "
                  "measurement."),
        ],
        "lab": ("storage", {
            "mode": "workingset",
            "panel_title": "Set the memory, the dataset and the skew",
            "panel_intro": (
                "The hit rate is `H(C,s)/H(N,s)` with `C` and `N` counted in pages, and "
                "the disk IOPS are `(1 − h) × the read rate`. Take the skew to `s = 0` and "
                "watch the hit rate collapse to the share of the data, which is the whole "
                "argument for why skew is worth measuring."
            ),
        }),
        "steps_title": "Sizing a page cache",
        "steps_intro": "Convert to pages, get the skew honestly, and then stay in the unit the device is limited by.",
        "steps": [
            ("Convert both sizes into pages",
             "`N = dataset/page` and `C = memory/page`. At an `8 kB` page, `500 GB` is "
             "`62 500 000` pages and `64 GB` is `8 000 000`. The formula counts pages, "
             "and a mismatch of units here is the one error that changes the answer by "
             "orders of magnitude."),
            ("Get the skew from a trace, not from a default",
             "`s` is the Zipf exponent of your workload's page popularity, and it is the "
             "single most influential input: at `s = 0` the hit rate is the share of the "
             "data and at `s = 1` it is seven times that. Assuming `s = 1` because it is "
             "the classic value is an assumption, and it should be labelled as one."),
            ("Compute `h`, and immediately write `1 − h` beside it",
             "A hit rate is for describing the cache and a miss rate is for describing "
             "everything behind it. `88.905%` and `11.095%` are the same measurement, and "
             "only the second one multiplies into a device limit."),
            ("Multiply by the read rate and compare against the disk",
             "`(1 − h) × reads` is the IOPS the device must actually serve — `2 219` a "
             "second here. That is the number to hold against what the storage can do, "
             "and the number that tells you whether another doubling of memory is worth "
             "buying."),
        ],
        "worked": {
            "title": "64 GB of page cache over a 500 GB dataset",
            "intro": [
                "Convert to pages, apply the formula at two skews, and then walk the "
                "memory to see what each doubling is worth."
            ],
            "lines": [
                "page 8 kB      dataset 500 GB  →  N = 62 500 000 pages",
                "               memory   64 GB  →  C =  8 000 000 pages     C/N = 12.80%",
                "               reads 20 000 a second",
                "",
                "s = 1     h = H(8 000 000, 1)/H(62 500 000, 1)   ≈   88.905%    rounded",
                "          disk IOPS  (1 − 0.88905) × 20 000      ≈    2 219 a second",
                "",
                "s = 0     h = C/N = 16/125                       =    12.800%    exact",
                "          disk IOPS  (1 − 0.128) × 20 000        =   17 440 a second",
                "",
                "memory      1/64     1/32     1/16      1/8      1/4      1/2   of the data",
                "h        77.553%  81.294%  85.036%  88.777%  92.518%  96.259%",
                "IOPS       4 489    3 741    2 993    2 245    1 496      748",
                "each doubling:  +3.74 points of hit rate,  −748 IOPS",
            ],
            "after": [
                "The two skew rows first. The same `12.80%` of the data serves `88.9%` of "
                "the reads under classic Zipf and `12.8%` under uniform popularity, and "
                "the disk sees `2 219` IOPS against `17 440`. Every sentence anyone writes "
                "about a page cache being effective is a sentence about the top row, and "
                "it is only true because real workloads are skewed.",
                "Now read the last two rows across. Every doubling of memory adds about "
                "`3.74` points of hit rate and removes about `748` IOPS — the same amount "
                "each time, not the same fraction. That is `H(C,1)` growing like the "
                "logarithm of `C`, and it is why memory sizing is a question with a "
                "budget rather than a knee: there is no point at which another doubling "
                "suddenly stops helping, and no point at which it starts helping more.",
                "For a faded rehearsal, halve the memory to `32 GB` and keep everything "
                "else. The supplied first move is that `C` falls to `4 000 000` pages. "
                "Compute the hit rate and the residual IOPS, check them against the "
                "doubling rule above, and then say roughly how much memory it would take "
                "to get the disk below `1 500` IOPS. Run the lab at your answer before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "Pages, skew and residual IOPS",
        "quiz": [
            {"q": "A `500 GB` dataset with `64 GB` of page cache and `8 kB` pages. What are `N` and `C`?",
             "a": ["`N = 500`, `C = 64`", "`N = 62 500 000`, `C = 8 000 000`", "`N = 62 500`, `C = 8 000`", "`N = 4 000 000`, `C = 512 000`"],
             "c": 1,
             "why": "`500 GB / 8 kB = 62 500 000` pages and `64 GB / 8 kB = 8 000 000`. "
                    "The formula counts pages, so both sizes have to be divided by the "
                    "page size — and `C/N = 12.80%` either way, which is why the ratio "
                    "survives a units error and the IOPS figure does not."},
            {"q": "At `s = 0` — every page equally likely — what is the hit rate for that cache?",
             "a": ["`88.905%`", "`12.800%`", "`50%`", "`0`, because nothing is hot"],
             "c": 1,
             "why": "`H(n,0) = n`, so `h = C/N = 12.80%`: memory serves exactly its share "
                    "of the data and nothing more. `88.905%` is the classic-Zipf answer, "
                    "which is `6.9` times the share — and the entire value of a page cache "
                    "is that gap."},
            {"q": "The hit rate is `88.905%` and the workload does `20 000` page reads a second. What does the disk see?",
             "a": ["`17 781` a second", "`2 219` a second", "`20 000` a second", "`11 095` a second"],
             "c": 1,
             "why": "`(1 − h) × reads = 0.11095 × 20 000 ≈ 2 219`. `17 781` multiplies by "
                    "`h` rather than by `1 − h`, which is the hit rate answering a "
                    "question about the miss rate; `20 000` is the claim that being on "
                    "disk makes every read a disk read, off by a factor of nine here."},
            {"q": "Memory doubles from `64 GB` to `128 GB` on the same dataset and skew. What happens to the disk IOPS?",
             "a": ["They halve, to about `1 110`",
                   "They fall by about `748`, to roughly `1 471`",
                   "They are unchanged; the working set did not change",
                   "They fall by a factor of `6.9`, the skew advantage"],
             "c": 1,
             "why": "The hit rate rises by about `3.74` points per doubling, so the IOPS "
                    "fall by about `0.0374 × 20 000 ≈ 748` — the same absolute amount for "
                    "every doubling, because `H(C,1)` grows like `log C`. Expecting them "
                    "to halve is expecting a geometric improvement from a logarithmic "
                    "formula."},
        ],
        "mistakes": [
            ("“It is on disk, so every read is a disk read”",
             "At `64 GB` over `500 GB` with skewed popularity, about `88.9%` of reads "
             "never reach the device: `2 219` IOPS out of `20 000`, a factor of nine. A "
             "capacity plan built on the assumption specifies nine times the storage IOPS "
             "it needs, which is expensive, and a plan that assumes the cache works "
             "without measuring the skew is wrong in the other direction, which is worse."),
            ("Sizing memory against the dataset rather than the working set",
             "The dataset is `500 GB` and the memory is `64 GB`, and the cache still "
             "serves nine reads in ten. What memory has to cover is the pages that are "
             "actually asked for, and under skew that is a small and slowly growing "
             "fraction of the whole — so “we cannot cache it, it is half a terabyte” is a "
             "sentence about the wrong quantity."),
            ("Expecting the IOPS to halve when memory doubles",
             "They fall by a fixed number, not a fixed fraction: about `748` IOPS per "
             "doubling at these settings. The hit rate is a ratio of harmonic numbers and "
             "grows like a logarithm, so the improvement from `1/64` to `1/32` of the "
             "data is the same size as the improvement from `1/4` to `1/2` — and costs "
             "thirty-two times less."),
        ],
        "standard": ("Finish when a page cache is obviously the same object as a cache.",
                     "You should be able to convert a dataset and a memory size into "
                     "pages, compute the hit rate at a stated skew, turn it into residual "
                     "disk IOPS, and say what one more doubling of memory would buy in "
                     "that unit."),
        "note": (
            "Every figure so far has described a system that is running. “RPO and RTO” "
            "prices the one that is not: how many bytes a backup schedule puts at risk "
            "and how many hours a restore takes — two questions in two different units, "
            "and a single sentence about having backups answers neither of them."
        ),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "rpo-and-rto",
        "title": "RPO and RTO",
        "module": "Durability and layout",
        "one_line": "Compute the bytes a backup schedule puts at risk and the hours a restore takes, and invert the second to get the schedule a target allows.",
        "summary": (
            "Two questions, two units. The recovery point objective is bytes: the backup "
            "interval multiplied by the write rate, `1.73 TB` at a daily backup and "
            "`20 MB/s` of writes. The recovery time objective is hours: the dataset over "
            "the restore bandwidth plus the log replay, `12.38 h` for two terabytes. "
            "Shortening the interval moves both — and cannot touch the copy, which is the "
            "floor under either promise."
        ),
        "key": [
            "RPO = backup interval × write rate                      bytes at risk",
            "RTO = size / restore bandwidth + log / replay rate      hours to be back",
            "",
            "24 h at 20 MB/s        RPO   1.73 TB worst,   864.00 GB expected",
            "2 TB at 200 MB/s       copy back                          2.78 h",
            "1.73 TB at 50 MB/s     replay                             9.60 h",
            "                       RTO                               12.38 h",
        ],
        "key_label": "Two questions, two units, and the floor no schedule can move",
        "concepts_intro": (
            "The whole lesson is that these are different numbers. Everything else is two "
            "multiplications and a division."
        ),
        "concepts": [
            ("RPO is bytes and RTO is hours",
             "The recovery <em>point</em> objective asks how much work is lost: the "
             "backup interval times the write rate, in bytes. The recovery "
             "<em>time</em> objective asks how long the system is down: the dataset over "
             "the restore bandwidth, plus replaying whatever log survived. They answer "
             "different questions, they are measured in different units, and a single "
             "statement cannot satisfy both."),
            ("A failure lands inside the interval, so the expected loss is half the worst case",
             "The worst case is a failure one instant before the next backup, losing a "
             "whole interval of writes: `1.73 TB` at a daily backup and `20 MB/s`. A "
             "failure at a uniformly random moment inside the interval loses half of "
             "that on average, `864.00 GB`. Quote both — the first is what you must "
             "survive and the second is what you will typically pay."),
            ("The copy is the floor, and the schedule cannot move it",
             "Halving the backup interval halves the bytes at risk and halves the replay, "
             "but copying `2.00 TB` back at `200 MB/s` takes `2.78 h` on every row of the "
             "table. No backup schedule in existence makes a restore faster than the time "
             "it takes to move the data, which is why an aggressive RTO target is a "
             "statement about bandwidth and dataset size rather than about backups."),
        ],
        "read_title": "Bytes at risk, hours to be back, and the floor under both",
        "read_intro": "Two formulas, the difference between worst case and expected, and what a target actually constrains.",
        "body": [
            ("def", ("Recovery point and recovery time objectives",
                     "The <strong>recovery point objective</strong> (RPO) is the volume "
                     "of writes lost by a failure, measured in bytes: at most "
                     "`interval × write rate`, and `interval × write rate / 2` in "
                     "expectation for a failure at a uniformly random moment.",
                     "The <strong>recovery time objective</strong> (RTO) is the elapsed "
                     "time to be serving again, measured in hours: "
                     "`size / restore bandwidth + surviving log / replay rate`.")),
            ("p", "Writing them side by side is most of the work, because the two are "
                  "routinely collapsed into one sentence about backups existing. They are "
                  "controlled by different things: the RPO by the schedule, the RTO by "
                  "bandwidth. Doubling the backup frequency improves the first "
                  "proportionally and the second hardly at all."),
            ("math", [
                "interval 24 h = 86 400 s      writes 20 MB/s      dataset 2.00 TB",
                "restore 200 MB/s              log replay 50 MB/s",
                "",
                "RPO worst       86 400 s × 20 MB/s             =  1.73 TB",
                "RPO expected    half the interval, on average  = 864.00 GB",
                "",
                "copy back       2.00 TB / 200 MB/s = 10 000 s  =   2.78 h",
                "replay          1.73 TB / 50 MB/s  = 34 560 s  =   9.60 h",
                "RTO             2.78 h + 9.60 h                =  12.38 h",
            ]),
            ("p", "Notice what dominates. Of the `12.38 h`, the copy is `2.78` and the "
                  "replay is `9.60` — so on this schedule most of the outage is spent "
                  "reapplying a day's worth of log, and the fastest available lever is "
                  "the backup interval rather than the restore path. That balance flips "
                  "as the interval shortens, which is exactly why both terms have to be "
                  "computed rather than one of them assumed dominant."),
            ("h3", "What a shorter interval buys"),
            ("p", "It buys twice: fewer bytes at risk, and less log to replay. Backing up "
                  "hourly instead of daily takes the RPO from `1.73 TB` to `72.00 GB` and "
                  "the RTO from `12.38 h` to `3.18 h` — a factor of twenty-four on the "
                  "first and most of the way to the floor on the second. What it does not "
                  "touch is the `2.78 h` of copying, which sits under every row."),
            ("example", ("The same table at four intervals",
                         "At `20 MB/s` of writes into a `2.00 TB` dataset restored at "
                         "`200 MB/s` with `50 MB/s` of replay: one hour gives `72.00 GB` "
                         "at risk and an RTO of `3.18 h`; six hours, `432.00 GB` and "
                         "`5.18 h`; twelve hours, `864.00 GB` and `7.58 h`; twenty-four "
                         "hours, `1.73 TB` and `12.38 h`. The RPO is linear in the "
                         "interval and so is the replay, so the RTO is a straight line "
                         "starting at `2.78 h`.")),
            ("p", "Run it backwards to turn a target into a schedule. A four-hour RTO "
                  "leaves `4 h − 2.78 h = 1.22 h` for replay, which at `50 MB/s` is about "
                  "`220 GB` of log, which at `20 MB/s` of writes is `3.06 h` of interval. "
                  "So “we must be back inside four hours” is, on this hardware, a "
                  "requirement to back up at least every three hours — and if the copy "
                  "alone exceeded four hours the target would be unreachable at any "
                  "schedule, which the arithmetic says immediately."),
            ("p", "The misconception this page exists for is offering “we have backups” "
                  "as an answer. It is not a number of bytes, so it is not an RPO; it is "
                  "not a number of hours, so it is not an RTO. Both of the real answers "
                  "are one multiplication away from figures an operator already has, and "
                  "the unwillingness to produce them is usually a sign that nobody has "
                  "timed a restore."),
            ("p", "Which is the honest caveat. Restore bandwidth must be measured on a "
                  "real restore, not assumed from a network specification; a backup that "
                  "has never been restored is a forecast rather than a fact. And this "
                  "model starts the clock at the moment of failure, while a real outage "
                  "also contains detection and the decision to restore — neither of which "
                  "is in these two formulas and both of which are in the outage."),
        ],
        "lab": ("storage", {
            "mode": "recovery",
            "panel_title": "Set the schedule and the two bandwidths",
            "panel_intro": (
                "RPO is the interval times the write rate; RTO is the dataset over the "
                "restore bandwidth plus the log over the replay rate. Drag the interval "
                "from a day down to an hour and watch the RTO fall toward the copy time "
                "and stop there — that floor is the point of the lesson."
            ),
        }),
        "steps_title": "Turning a schedule into two promises",
        "steps_intro": "Two multiplications, one addition, and then the same arithmetic run backwards.",
        "steps": [
            ("Multiply the interval by the write rate",
             "That is the worst-case RPO in bytes: `86 400 s × 20 MB/s = 1.73 TB` for a "
             "daily backup. Use the write rate, not the read rate and not the ingest of "
             "the busiest hour unless that is the hour you are protecting."),
            ("Halve it for the expected case, and keep both figures",
             "A failure at a uniformly random moment inside the interval loses half the "
             "worst case on average, `864.00 GB` here. The worst case is what a "
             "commitment has to survive; the expected case is what the business will "
             "actually experience."),
            ("Add the copy and the replay",
             "`size / restore bandwidth` plus `RPO / replay rate`. Write the two terms "
             "separately: the first is the floor and cannot be moved by the schedule, and "
             "seeing which of the two dominates tells you which lever is worth pulling."),
            ("Invert it: solve for the interval a target allows",
             "Subtract the copy from the target, multiply what is left by the replay rate "
             "to get a log size, and divide by the write rate. A four-hour target on this "
             "hardware allows `3.06 h` between backups. If the copy alone exceeds the "
             "target, no schedule reaches it and the conversation is about bandwidth."),
        ],
        "worked": {
            "title": "A daily backup of two terabytes at 20 MB/s",
            "intro": [
                "The two objectives, then the same arithmetic at four intervals, then run "
                "backwards from a target."
            ],
            "lines": [
                "interval 24 h = 86 400 s      writes 20 MB/s      dataset 2.00 TB",
                "restore 200 MB/s              log replay 50 MB/s",
                "",
                "RPO worst       86 400 s × 20 MB/s               =   1.73 TB",
                "RPO expected    half of the interval, on average = 864.00 GB",
                "",
                "copy back       2.00 TB / 200 MB/s = 10 000 s    =   2.78 h",
                "replay          1.73 TB / 50 MB/s  = 34 560 s    =   9.60 h",
                "RTO             2.78 + 9.60                      =  12.38 h",
                "",
                "interval    RPO worst     copy      replay        RTO",
                "     1 h     72.00 GB    2.78 h    24.0 min     3.18 h",
                "     6 h    432.00 GB    2.78 h     2.40 h      5.18 h",
                "    12 h    864.00 GB    2.78 h     4.80 h      7.58 h",
                "    24 h      1.73 TB    2.78 h     9.60 h     12.38 h",
                "",
                "for RTO ≤ 4 h    4 h − 2.78 h = 1.22 h of replay",
                "                 1.22 h × 50 MB/s ≈ 220 GB of log",
                "                 220 GB / 20 MB/s        →   interval ≤ 3.06 h",
            ],
            "after": [
                "The copy column never moves. `2.78 h` is the floor under every recovery "
                "promise this hardware can make, and only a faster restore path or a "
                "smaller dataset lowers it — no backup schedule does. That is the single "
                "most useful sentence on this page, because it converts an argument about "
                "backup frequency into an arithmetic fact about bandwidth.",
                "Shortening the interval buys on both axes at once, which is unusual "
                "enough to be worth saying out loud: from twenty-four hours to one, the "
                "bytes at risk fall by a factor of twenty-four and the recovery time "
                "falls from `12.38 h` to `3.18 h`, which is within half an hour of the "
                "floor. Past that point more frequent backups buy almost nothing.",
                "For a faded rehearsal, keep the daily schedule and double the restore "
                "bandwidth to `400 MB/s`. The supplied first move is that the copy falls "
                "to `1.39 h`. Compute the new RTO, then say what a four-hour target now "
                "allows as a backup interval, and why that answer moved so much further "
                "than the RTO did. Check both in the lab before opening the quiz.",
            ],
        },
        "quiz_title": "Bytes at risk and hours to be back",
        "quiz": [
            {"q": "Backups run every `6` hours and the system writes `20 MB/s`. What is the worst-case RPO?",
             "a": ["`72.00 GB`", "`216.00 GB`", "`432.00 GB`", "`1.73 TB`"],
             "c": 2,
             "why": "`6 × 3 600 s × 20 MB/s = 432.00 GB`. `216.00 GB` is the expected "
                    "loss, half the worst case, which is a different figure and worth "
                    "quoting separately; `72.00 GB` is the hourly schedule and `1.73 TB` "
                    "the daily one."},
            {"q": "A `2.00 TB` dataset restores at `200 MB/s` with `50 MB/s` of log replay, on a daily backup. Which term dominates the `12.38 h` recovery?",
             "a": ["The copy, at `9.60 h`",
                   "The replay, at `9.60 h`",
                   "They are about equal",
                   "Neither; most of it is detection time"],
             "c": 1,
             "why": "The copy is `2.00 TB / 200 MB/s = 2.78 h` and the replay is "
                    "`1.73 TB / 50 MB/s = 9.60 h`. A day of log at a replay rate four "
                    "times slower than the restore path is most of the outage, which is "
                    "why the backup interval is the effective lever here. Detection time "
                    "is real and is not in this model."},
            {"q": "The backup interval is halved. What happens to the recovery time?",
             "a": ["It halves", "It falls, but by less than half, because the copy is unchanged", "It is unchanged", "It falls by the same factor as the RPO"],
             "c": 1,
             "why": "Halving the interval halves the log and therefore the replay term, "
                    "and leaves the copy exactly where it is. From `12.38 h` at "
                    "twenty-four hours to `7.58 h` at twelve: the RPO halved exactly and "
                    "the RTO did not, because `2.78 h` of it was never a function of the "
                    "schedule."},
            {"q": "Someone answers a recovery question with “we have backups”. What has that established?",
             "a": ["The RPO, but not the RTO",
                   "The RTO, but not the RPO",
                   "Neither — it is not a number of bytes and not a number of hours",
                   "Both, provided the backups are recent"],
             "c": 2,
             "why": "An RPO is bytes and an RTO is hours; the sentence produces neither. "
                    "Both are one multiplication away from figures the operator already "
                    "has — interval, write rate, dataset size, restore bandwidth — and "
                    "the absence of them usually means no restore has been timed."},
        ],
        "mistakes": [
            ("Offering “we have backups” as a recovery-time claim",
             "Backups existing is a precondition, not an answer. The two answers are "
             "`interval × write rate` in bytes and `size/bandwidth + log/replay` in "
             "hours, and both are computable in a minute from numbers an operator "
             "already has. A recovery plan whose strongest statement is that backups run "
             "has not been tested, and the first restore will discover the bandwidth."),
            ("Quoting the worst case and the expected loss as if they were one number",
             "A daily backup at `20 MB/s` puts `1.73 TB` at risk and loses `864.00 GB` on "
             "average, and the two figures are for different conversations: the first is "
             "what a commitment must survive, the second what will typically happen. "
             "Using the expected figure in a contract understates the exposure by two."),
            ("Leaving the log replay out of the recovery time",
             "The copy is `2.78 h` of a `12.38 h` recovery here — less than a quarter. A "
             "plan that quotes only the restore bandwidth is quoting the smaller term, "
             "and it is the term that does <em>not</em> respond to the backup schedule, "
             "so the plan also loses the one lever it had."),
        ],
        "standard": ("Finish when a recovery question gets two numbers in two units.",
                     "You should be able to compute worst-case and expected RPO from a "
                     "schedule and a write rate, compute RTO from a dataset, a restore "
                     "bandwidth and a replay rate, and invert the second to say what "
                     "backup interval a stated target allows."),
        "note": (
            "Every number on this course has been a count — of seeks, levels, rewrites, "
            "bits, fsyncs and hours — and none of them has had a price attached. Scaling "
            "Laws and Cost is where a count becomes money, and where the compression "
            "ratio this course took as an input finally has to earn the processor time it "
            "costs."
        ),
    },
]
