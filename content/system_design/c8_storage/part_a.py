"""Storage Engines and Indexes, lessons 01-06 - the cost model, the write side, the filter.

Every figure in this file was read off scripts/mathpath/labs/storage.py running
headlessly, not out of anyone's head. Where a figure here disagrees with a
textbook - 9.585 bits a key rather than 9.57 - the lab is the authority and the
lesson says which constant produced which number.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "sequential-vs-random-io",
        "title": "Sequential vs Random I/O",
        "module": "The cost model",
        "one_line": "Price the same read both ways from `time = seeks × t_seek + bytes/bandwidth`, and find the chunk size where its two terms balance.",
        "summary": (
            "A read costs a seek for every place it starts and a byte for every byte it "
            "moves. Reading a gigabyte in one sweep is one seek and ten seconds; reading "
            "the same gigabyte four kilobytes at a time is a quarter of a million seeks "
            "and forty-two minutes. The bytes term never moved, which is why "
            "`size ÷ bandwidth` is a model of one access pattern rather than a model of "
            "reading."
        ),
        "key": [
            "time = seeks × t_seek + bytes / bandwidth",
            "",
            "1 GB, one sweep        1 seek         10.00 ms + 10.00 s  =  10.01 s",
            "1 GB, 4 kB at a time   250 000 seeks  41.7 min + 10.00 s  =  41.8 min",
            "                                                        250.75× as long",
            "",
            "crossover chunk = t_seek × bandwidth = 10 ms × 100 MB/s = 1 MB",
        ],
        "key_label": "One formula, two access patterns, and the chunk where the terms are equal",
        "concepts_intro": (
            "One formula and two readings of it. Every disagreement about storage "
            "performance is a disagreement about which of its two terms is doing the work."
        ),
        "concepts": [
            ("A read has a fixed cost and a per-byte cost",
             "The first term, `seeks × t_seek`, is paid once for every place the read "
             "starts: the arm moves, the platter turns, nothing is transferred. The "
             "second term, `bytes/bandwidth`, is paid for the bytes themselves. A "
             "sequential read of a gigabyte pays the first term once and a `4 kB` "
             "random read of the same gigabyte pays it `250 000` times. The bytes are "
             "identical; the bill is not."),
            ("The chunk size sets the seek count",
             "Reading `B` bytes in chunks of `c` costs `⌈B/c⌉` seeks. At `c = 4 kB` over "
             "a gigabyte that is `250 000` of them, and at `10 ms` each they are "
             "`2 500 s` of waiting against `10 s` of transfer. Halving the chunk doubles "
             "the first term and leaves the second exactly where it was, which is why "
             "the ratio between the two patterns moves so violently."),
            ("The two terms are equal at one chunk size",
             "Set one seek equal to one chunk of transfer, `t_seek = c/bandwidth`, and "
             "solve: `c = t_seek × bandwidth`. On a `10 ms`, `100 MB/s` disk that is "
             "`1 MB`. Below it the arm decides the time and the size of each read barely "
             "matters; above it the bandwidth decides and the seek barely matters. It is "
             "one multiplication and it tells you which half of the formula you are in."),
        ],
        "read_title": "Seeks, bytes, and the chunk size between them",
        "read_intro": "Why the same gigabyte is ten seconds or forty-two minutes, and what the number in the middle is.",
        "body": [
            ("def", ("Read time",
                     "For a read of `B` bytes issued as `s` separate accesses on a device "
                     "with seek time `t_seek` and sequential bandwidth `bw`, the "
                     "<strong>read time</strong> is `s × t_seek + B/bw`. A "
                     "<strong>sequential</strong> read is the case `s = 1`. A "
                     "<strong>random</strong> read in chunks of `c` bytes is the case "
                     "`s = ⌈B/c⌉`.",
                     "There are not two formulas here. What changes between the two rows "
                     "of any comparison is `s`, and `s` is a property of the access "
                     "pattern rather than of the data or of the device.")),
            ("p", "The habit worth building is to write the two terms down separately "
                  "and look at them before adding. `10.00 ms + 10.00 s` and "
                  "`41.7 min + 10.00 s` are the same gigabyte off the same disk. The "
                  "second term is identical in both, to the digit. Every one of those "
                  "forty-two minutes is first-term."),
            ("math", [
                "1 GB = 10⁹ B      t_seek = 10 ms      bw = 100 MB/s",
                "",
                "sequential   s = 1",
                "             1 × 10 ms + 10⁹/10⁸ s        =      0.01 s + 10 s  =  10.01 s",
                "",
                "random       c = 4 kB,  s = 10⁹/4 000 = 250 000",
                "             250 000 × 10 ms + 10⁹/10⁸ s  =  2 500.00 s + 10 s  =  2 510 s",
                "",
                "ratio        2 510 / 10.01                =    250.75",
            ]),
            ("example", ("The same gigabyte on solid state",
                         "Hold the gigabyte and the `4 kB` chunk and change the device: "
                         "`100 µs` of seek and `500 MB/s` of bandwidth. The sequential "
                         "read is `2.0001 s`, the random read is `27 s`, and the ratio "
                         "falls from `250.75` to `13.50`. The access pattern still costs "
                         "more than an order of magnitude. What changed is that it costs "
                         "thirteen times rather than two hundred and fifty.")),
            ("h3", "Where the two terms are equal"),
            ("p", "Ask for the chunk size at which one seek costs exactly what one chunk "
                  "of transfer costs. `t_seek = c/bw` rearranges to `c = t_seek × bw`, "
                  "and the reason the answer is easy to carry around is that it is a "
                  "multiplication of the two numbers a device is sold on. The disk above "
                  "gives `10 ms × 100 MB/s = 1 MB`; the solid-state device gives "
                  "`100 µs × 500 MB/s = 50 kB`."),
            ("p", "Call that chunk `c*`. Then the whole comparison collapses to one "
                  "division, because the random time over the sequential time is about "
                  "`1 + c*/c` whenever the sequential read is dominated by its bytes "
                  "term. On the disk: `1 + 10⁶/4 000 = 251`, against the `250.75` the "
                  "lab computes exactly. At `c = c*` the ratio is `2`; at `64 kB` it is "
                  "`16.61`; at `4 MB` it is `1.25`. One number, `c*`, generates the "
                  "entire table."),
            ("example", ("Faster hardware does not always narrow the gap",
                         "The NVMe preset is `20 µs` of seek and `3000 MB/s` of "
                         "bandwidth. Its crossover chunk is `60 kB` — larger than the "
                         "SATA device's `50 kB` — and its `4 kB` ratio is `16.00`, "
                         "slightly worse than the SATA device's `13.50`. Bandwidth grew "
                         "by six and the seek fell by five, and since `c* = t_seek × bw` "
                         "the crossover went up. The penalty for a bad access pattern is "
                         "not a fact about how old the device is.")),
            ("p", "Bytes on this course are decimal: `1 kB = 1000 B` and "
                  "`1 GB = 10⁹ B`. That is not pedantry here, because it moves the "
                  "headline. The same gigabyte in `4 kB` random reads is `250.75` times "
                  "the sequential time in decimal units and `262.9` times it in binary "
                  "ones, so a reader checking the figure against their own arithmetic "
                  "has to know which two hundred and fifty is being quoted. The lab says "
                  "so on its face."),
            ("p", "What the formula does not carry is a queue, a read-ahead, or a second "
                  "request in flight. A device serving many concurrent random reads "
                  "overlaps some of the waiting, so the honest form of the claim is that "
                  "the seek term is <em>work the device must do</em> rather than "
                  "necessarily time one request must wait. Queues and Utilisation is "
                  "where waiting under concurrency gets its own arithmetic. The subject "
                  "here is the work."),
        ],
        "lab": ("storage", {
            "mode": "io",
            "panel_title": "Move the chunk and watch which term wins",
            "panel_intro": (
                "Both times come out of the one formula, evaluated at one seek and at one "
                "seek per chunk. Start at `4 kB` on the spinning disk and read the ratio; "
                "then drag the chunk to `1 MB` and watch it fall to `2.00`, which is the "
                "crossover arriving. The table marks where you are and names which term "
                "is deciding the time."
            ),
        }),
        "steps_title": "Pricing an access pattern",
        "steps_intro": "Four lines, and the first of them is the whole discipline: count the seeks before you touch the size.",
        "steps": [
            ("Count the seeks first",
             "`s = 1` for a sweep, `s = ⌈B/c⌉` for chunks of `c`. This is the only "
             "number that distinguishes the two rows of the comparison, so write it "
             "down before anything else and the rest is arithmetic."),
            ("Evaluate the two terms separately",
             "`s × t_seek` and `B/bw`, side by side, in the same unit, and do not add "
             "them yet. The question you are answering is which one is bigger, and "
             "adding first is what hides it."),
            ("Decide which term you are fighting",
             "If the seek term dominates, more bandwidth buys nothing and a larger "
             "chunk buys everything. If the bytes term dominates, the device is already "
             "working as hard as it can and the only lever left is reading fewer bytes."),
            ("Compute `c*` and place yourself on it",
             "`c* = t_seek × bw`, then `ratio ≈ 1 + c*/c`. That is a one-line check on "
             "whatever you just computed: at `c = c*` the ratio is `2`, at a tenth of "
             "`c*` it is about `11`, and at `c*/250` it is about `251`."),
        ],
        "worked": {
            "title": "One gigabyte off a 10 ms, 100 MB/s disk",
            "intro": [
                "Two rows, one formula, and the difference written out so that it can be "
                "pointed at rather than described."
            ],
            "lines": [
                "B = 1 GB = 10⁹ B     t_seek = 10 ms = 0.01 s     bw = 100 MB/s = 10⁸ B/s",
                "",
                "sequential    s = 1",
                "              seek term    1 × 0.01 s             =       0.01 s",
                "              bytes term   10⁹ / 10⁸              =      10.00 s",
                "              total                                      10.01 s",
                "",
                "random        c = 4 kB,  s = 10⁹ / 4 000 = 250 000",
                "              seek term    250 000 × 0.01 s       =   2 500.00 s",
                "              bytes term   10⁹ / 10⁸              =      10.00 s",
                "              total                                   2 510.00 s  =  41.8 min",
                "",
                "ratio         2 510.00 / 10.01                    =     250.75",
                "",
                "crossover     c* = 0.01 s × 10⁸ B/s               =  1 000 000 B  =  1 MB",
                "check         1 + c*/c = 1 + 10⁶/4 000            =     251       ✓ against 250.75",
            ],
            "after": [
                "The bytes term is `10.00 s` on both rows. Nothing about the amount of "
                "data changed, the disk did not get slower, and the read still took two "
                "hundred and fifty times as long.",
                "The check on the last line is worth keeping. `ratio ≈ 1 + c*/c` is a "
                "good approximation whenever the sequential time is dominated by its "
                "bytes term, and it turns the whole comparison into one division. It "
                "also explains the shape of the lab's table: every halving of the chunk "
                "roughly doubles the ratio, until the chunk passes `c*` and the ratio "
                "settles toward `1`.",
                "For a faded rehearsal, take the same gigabyte on the SATA solid-state "
                "preset — `100 µs` and `500 MB/s`. The supplied first move is the "
                "crossover, `c* = 50 kB`. From it, predict the `4 kB` ratio before "
                "computing either time; then compute both times and check the "
                "prediction. Then answer the question the numbers exist for: which chunk "
                "size on the slider reads the gigabyte in under three seconds? Run the "
                "lab at your answer before opening the quiz.",
            ],
        },
        "quiz_title": "Seeks, bytes and the crossover",
        "quiz": [
            {"q": "A `2 GB` file is read in `16 kB` chunks from a device with a `10 ms` seek and `100 MB/s` of bandwidth. How many seeks, and what is the seek term?",
             "a": ["`125 000` seeks, `1 250 s`",
                   "`125 000` seeks, `20 s`",
                   "`2 000` seeks, `20 s`",
                   "`16 000` seeks, `160 s`"],
             "c": 0,
             "why": "`s = 2×10⁹/16 000 = 125 000`, and `125 000 × 10 ms = 1 250 s`. "
                    "`20 s` is the <em>bytes</em> term `2×10⁹/10⁸`, which is the same "
                    "whatever the chunk size; `2 000` counts megabytes rather than "
                    "chunks."},
            {"q": "On that same device, which chunk size makes one seek cost exactly what transferring one chunk costs?",
             "a": ["`4 kB`", "`64 kB`", "`1 MB`", "`100 MB`"],
             "c": 2,
             "why": "`c* = t_seek × bw = 10 ms × 100 MB/s = 1 MB`. `100 MB` is the "
                    "bandwidth with the seek read as a whole second rather than ten "
                    "milliseconds. `4 kB` and `64 kB` are page sizes, and both sit well "
                    "below the crossover, where the seek term dominates."},
            {"q": "A device's bandwidth doubles and its seek time is unchanged. What happens to the random-to-sequential ratio at a fixed chunk size?",
             "a": ["It halves, because the sequential read is now twice as fast",
                   "It roughly doubles, because `c* = t_seek × bw` doubles",
                   "It is unchanged, because both reads move the same bytes",
                   "It falls toward `1`, because bandwidth is now the bottleneck"],
             "c": 1,
             "why": "The ratio is about `1 + c*/c`, and doubling `bw` doubles `c*`. The "
                    "sequential read did get twice as fast — that is exactly why the "
                    "ratio went up, since the random read is dominated by seeks and "
                    "barely moved. It is the arithmetic behind the NVMe preset scoring "
                    "`16.00` at `4 kB` where the SATA preset scores `13.50`."},
            {"q": "Reading `1 GB` sequentially takes `10.01 s` and reading it in `4 kB` chunks takes `41.8 min`. How much of those forty-two minutes is spent transferring bytes?",
             "a": ["All of it — the bytes have to move either way",
                   "About `41.7 min`; transferring is what a random read is slow at",
                   "`10.00 s`, exactly as in the sequential read",
                   "About `21 min`, half of each"],
             "c": 2,
             "why": "The bytes term is `10⁹/10⁸ = 10.00 s` on both rows, to the digit. "
                    "The other `2 500 s` is `250 000` seeks at `10 ms`. A random read "
                    "does not transfer more slowly; it transfers the same bytes with a "
                    "quarter of a million pauses in front of them."},
        ],
        "mistakes": [
            ("Quoting `size ÷ bandwidth` as the read time",
             "That is the second term alone, and it is the whole time only when `s = 1`. "
             "It gives `10 s` for a gigabyte that takes `41.8 min` on the same hardware "
             "— an answer wrong by a factor of two hundred and fifty, produced by a "
             "formula that looks like physics. Writing the seek count down first makes "
             "the error impossible."),
            ("Reading a device's specification as its throughput on your workload",
             "`100 MB/s` is what the disk does when `s = 1`. A workload of `4 kB` random "
             "reads on that disk moves `10⁹/2 510 ≈ 400 kB/s`, and both numbers are true "
             "of the same device. The specification is the bandwidth term; your workload "
             "chooses the seek term."),
            ("Assuming newer hardware makes the pattern stop mattering",
             "It shrinks the ratio and never removes it: `250.75` on the spinning disk, "
             "`13.50` on the SATA device and `16.00` on the NVMe one, all at `4 kB`. The "
             "last of those is larger than the one before it, because `c*` is "
             "`t_seek × bandwidth` and bandwidth grew faster than the seek fell."),
        ],
        "standard": ("Finish when you reach for the seek count before you reach for the size.",
                     "You should be able to price a read both ways on a stated device, "
                     "compute the crossover chunk in one multiplication, and say, for "
                     "any workload you are handed, which of the two terms the answer is "
                     "made of."),
        "note": (
            "The crossover chunk is the first of several numbers on this course that are "
            "one multiplication and settle an argument. “The Height of a B-tree” is "
            "another: the levels a tree needs are found by multiplying the fanout into "
            "an accumulator until it passes the key count, and the answer is a single "
            "digit for far more data than anyone expects."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-height-of-a-b-tree",
        "title": "The Height of a B-tree",
        "module": "The cost model",
        "one_line": "Find a tree's height by exact integer search, and turn it into the I/Os a lookup costs once the page cache is counted.",
        "summary": (
            "A B-tree's height is the smallest `h` with `Bʰ ≥ N` — which is `⌈log_B N⌉` "
            "written so that a computer gets it right. A billion keys at a fanout of "
            "five hundred is four levels, the page cache holds the top two of them for a "
            "couple of megabytes, and a lookup is therefore two disk reads. Nothing "
            "about a billion is slow here."
        ),
        "key": [
            "height = ⌈log_B N⌉ = the smallest h with Bʰ ≥ N",
            "",
            "B = 500     500        250 000       125 000 000      62 500 000 000",
            "            h = 1      h = 2         h = 3            h = 4  ≥ 10⁹   stop",
            "",
            "N = 10⁹, B = 500  →  4 levels,  top 2 cached  →  2 disk reads a lookup",
        ],
        "key_label": "Height as an integer search, and the I/Os the cache leaves behind",
        "concepts_intro": (
            "The definition is a power rather than a logarithm, the base is enormous, "
            "and the cost a reader pays is neither of those but what memory does not hold."
        ),
        "concepts": [
            ("Height is defined by a power, not by a logarithm",
             "The question is how many levels of fanout `B` it takes to cover `N` keys, "
             "and the answer is the smallest `h` with `Bʰ ≥ N`. That is a search over "
             "integers: multiply `B` into an accumulator and count the multiplications. "
             "`⌈log_B N⌉` names the same number in exact arithmetic, and the lab computes "
             "the power because a floating-point logarithm does not always agree."),
            ("Fanout is enormous because a page is",
             "A `4 kB` page holding `500` index entries gives `B = 500`, so every level "
             "multiplies the reach by five hundred. Four levels reach "
             "`62 500 000 000` keys. This is why the height of a real index is a single "
             "digit, and why “`log N` is slow for big `N`” has nothing to hold onto "
             "here: the base is five hundred and it is set by the page, not by the data."),
            ("A lookup costs the levels the cache does not hold",
             "The descent reads one page per level, so `h` page reads — except that the "
             "root and the level below it are `4.00 kB` and `2.00 MB` and live in memory "
             "permanently. At `N = 10⁹` and `B = 500` that turns a four-I/O lookup into "
             "a two-I/O one, and no change to the tree was involved."),
        ],
        "read_title": "The smallest h with Bʰ ≥ N, and what the cache takes off it",
        "read_intro": "How a height is actually computed, why a logarithm is the wrong instrument for it, and where the I/Os go.",
        "body": [
            ("def", ("B-tree height",
                     "For a tree in which every internal node holds up to `B` children, "
                     "the <strong>height</strong> `h` is the smallest integer with "
                     "`Bʰ ≥ N`, where `N` is the number of keys stored. Equivalently, "
                     "`h = ⌈log_B N⌉`.",
                     "A lookup descends one node per level and reads one page per node, "
                     "so an uncached lookup costs `h` page reads.")),
            ("math", [
                "N = 1 000 000 000      B = 500",
                "",
                "h = 1        500                 <  N",
                "h = 2        250 000             <  N",
                "h = 3        125 000 000         <  N",
                "h = 4        62 500 000 000      ≥  N      stop",
                "",
                "height = 4      level sizes at 4 kB a page",
                "                L1  4.00 kB    L2  2.00 MB    L3  1.00 GB    L4  500.00 GB",
            ]),
            ("p", "That table is not an illustration of the answer; it <em>is</em> the "
                  "computation. Four multiplications and four comparisons, in exact "
                  "integer arithmetic, and the height is the number of multiplications "
                  "the accumulator needed. The lab draws the same four rows."),
            ("h3", "Why the lab multiplies instead of taking a logarithm"),
            ("p", "Because at every exact power of the fanout a quotient of two "
                  "logarithms can land a few units in the last place above the integer, "
                  "and the ceiling then adds a level that does not exist. At `B = 3` and "
                  "`N = 9`, `log(9)/log(3)` evaluates to `2.0000000000000004` and its "
                  "ceiling is `3` — a two-level tree reported as three, which on a page "
                  "about counting I/Os is a whole extra I/O. It is not a rare corner: "
                  "`B = 5` at `N = 125`, `B = 8` at `N = 2 097 152` and `B = 19` at "
                  "`N = 2 476 099` all do the same thing. The lab prints what a logarithm "
                  "would have said beside the exact answer and tells you when the two "
                  "disagree."),
            ("example", ("Where the height actually moves",
                         "Hold `B = 500` and raise `N`. At `10⁶` the height is `3`; at "
                         "`10⁹` it is `4`; at `10¹²` it is `5`. Three orders of magnitude "
                         "buy one level. The height changes only when `N` crosses a whole "
                         "power of `B`, so every tree holding between `125 000 001` and "
                         "`62 500 000 000` keys — a range of five hundred to one — is "
                         "exactly four levels deep.")),
            ("h3", "The page cache takes the top off"),
            ("p", "Look at the level sizes rather than the level count. The top two "
                  "levels together are `4.00 kB + 2.00 MB`; the third is `1.00 GB` and "
                  "the fourth is `500.00 GB`. So the levels that are cheap to keep in "
                  "memory are exactly the ones every descent passes through, and keeping "
                  "them is what an engine does without being asked. Two megabytes removes "
                  "half the I/Os of every lookup in the system."),
            ("p", "The number that multiplies into a workload is the cached one. Ten "
                  "thousand lookups a second against this tree with two levels resident "
                  "is `20 000` disk reads a second; against the same tree with nothing "
                  "resident it is `40 000`. The height did not change and the device's "
                  "day did."),
            ("p", "Two things the model assumes. Nodes are taken to be full, and a real "
                  "B-tree's nodes sit somewhere between half full and full, so the "
                  "effective fanout is below the page's capacity and the true height is "
                  "occasionally one more than this calculation says. And a lookup is "
                  "taken to be one page read per level, which ignores the leaf splitting "
                  "across pages. Both errors point the same way — the real cost is at or "
                  "just above the computed one — which is what makes the computed one "
                  "usable."),
        ],
        "lab": ("storage", {
            "mode": "btree",
            "panel_title": "Set N, the fanout and what memory holds",
            "panel_intro": (
                "The height is the smallest `h` with `Bʰ ≥ N`, found by multiplying in "
                "BigInt, and the table is the search itself — one row per multiplication. "
                "Drag the power-of-ten slider across three decades and watch the height "
                "sit still, then set `B = 3` and `N = 9` and read what a logarithm would "
                "have said."
            ),
        }),
        "steps_title": "Getting a height and then an I/O count",
        "steps_intro": "The first step is the one people skip, and it is the one that decides every number after it.",
        "steps": [
            ("Get the fanout from the page, not from a guess",
             "`B` is the page size divided by the size of one index entry: a `4 kB` page "
             "with an `8 B` key and an `8 B` pointer is about `250`, and the same page "
             "with a shorter key is more. Every figure downstream depends on this one."),
            ("Multiply the fanout out until it reaches `N`",
             "`B`, `B²`, `B³`, …, stopping at the first value that is at least `N`, and "
             "count the multiplications. Four of them at `B = 500` passes a billion. Do "
             "not take a logarithm; at an exact power it can round the wrong way."),
            ("Subtract the levels memory holds",
             "Add the level sizes from the top — `4 kB`, `2 MB`, `1 GB` — and see how "
             "far down your memory reaches. The I/Os a lookup costs are the levels below "
             "that line, not the height."),
            ("Multiply by the lookup rate",
             "The height is a fact about the tree; the I/Os a second are the fact about "
             "the device. `10 000` lookups a second against a two-I/O tree is `20 000` "
             "reads a second, and that is the number to hold against what the disk can do."),
        ],
        "worked": {
            "title": "A billion keys at a fanout of 500",
            "intro": [
                "The search is four multiplications and a comparison. Everything after it "
                "is the page cache."
            ],
            "lines": [
                "N = 1 000 000 000 keys      4 kB page, 500 entries a page   →   B = 500",
                "",
                "   level        nodes            keys covered         level size",
                "     L1             1                     500            4.00 kB",
                "     L2           500                 250 000            2.00 MB",
                "     L3       250 000             125 000 000            1.00 GB",
                "     L4   125 000 000          62 500 000 000          500.00 GB",
                "",
                "   125 000 000 < 1 000 000 000 ≤ 62 500 000 000    →    height = 4",
                "",
                "lookup, nothing cached          4 page reads",
                "lookup, L1 and L2 cached        2 page reads      costing 4.00 kB + 2.00 MB",
                "",
                "a logarithm here     log(10⁹)/log(500) = 3.33…  →  ceiling 4      ✓ agrees",
                "the corner it misses log(9)/log(3) = 2.0000000000000004  →  3, but 3² = 9",
            ],
            "after": [
                "Read the fourth column. Two megabytes of memory removes half the I/Os of "
                "every lookup in the system, and it is the cheapest two megabytes anyone "
                "will ever spend. The third level is a gigabyte, which is a real "
                "decision; the fourth is five hundred, which is not.",
                "The misconception this page is aimed at is that `log N` gets "
                "uncomfortable for large `N`. Multiply the fanout out and see what it "
                "would take: five levels cover `31.25` trillion keys and six cover about "
                "fifteen quadrillion. The base is five hundred, and a base of five "
                "hundred has no large logarithm anywhere you will ever put data.",
                "For a faded rehearsal, take `N = 10⁹` with a fanout of `100` — a longer "
                "key, so fewer entries a page. The supplied first move is that "
                "`100³ = 10⁶` is far short of `N`. Finish the search, state the height, "
                "and then say how many levels have to be resident to keep a lookup at "
                "two I/Os. Check both on the sliders before opening the quiz.",
            ],
        },
        "quiz_title": "Heights, powers and page reads",
        "quiz": [
            {"q": "`N = 10⁶` keys at a fanout of `B = 500`. What is the height?",
             "a": ["`2`", "`3`", "`4`", "`20`"],
             "c": 1,
             "why": "`500² = 250 000 < 10⁶ ≤ 125 000 000 = 500³`, so three levels. `2` "
                    "stops one multiplication early. `20` is `log₂(10⁶)`, the height of a "
                    "binary tree over the same keys — which is the thing a fanout of "
                    "five hundred exists to avoid."},
            {"q": "A four-level tree serves `10 000` lookups a second with its top two levels resident in memory. How many disk reads a second is that?",
             "a": ["`10 000`", "`20 000`", "`40 000`", "None; the cache serves them"],
             "c": 1,
             "why": "Two levels are resident, so each lookup costs `4 − 2 = 2` page "
                    "reads and the workload is `20 000` reads a second. `40 000` is the "
                    "uncached tree and `10 000` counts one read a lookup, which would be "
                    "a hash index rather than a tree. The cache removes the top of every "
                    "descent and never the bottom."},
            {"q": "Why does the lab compute `Bʰ` rather than evaluating `⌈log_B N⌉` directly?",
             "a": ["Because logarithms are slower to evaluate than multiplication",
                   "Because a floating-point logarithm can land just above an integer, and the ceiling then reports one level too many",
                   "Because `log_B N` is only defined when `N` is an exact power of `B`",
                   "Because the height is not actually `⌈log_B N⌉`"],
             "c": 1,
             "why": "At `B = 3`, `N = 9` the quotient comes out as `2.0000000000000004` "
                    "and its ceiling is `3`, for a tree that is genuinely two levels "
                    "deep. The height <em>is</em> `⌈log_B N⌉` — the two agree in exact "
                    "arithmetic and disagree in floating point at exact powers, which is "
                    "precisely where indexes like to sit."},
            {"q": "The dataset grows from a billion keys to ten billion, with `B = 500` unchanged. What happens to the height?",
             "a": ["It grows to `5`",
                   "It stays at `4`",
                   "It grows to `6`, one level per order of magnitude",
                   "It cannot be said without knowing the key size"],
             "c": 1,
             "why": "Four levels cover `62 500 000 000` keys and ten billion is inside "
                    "that. The height moves only when `N` crosses a power of `B`, and "
                    "the next crossing is at sixty-two and a half billion. The key size "
                    "decides `B`, and `B` was given as `500`."},
        ],
        "mistakes": [
            ("Taking `⌈log_B N⌉` from a floating-point logarithm",
             "At every exact power of the fanout the quotient can land a few units in "
             "the last place above the integer, and the ceiling adds a level that is not "
             "there. `B = 3` at `N = 9`, `B = 5` at `N = 125` and `B = 8` at "
             "`N = 2 097 152` all do it. Multiply the fanout out instead: it is four or "
             "five multiplications and it is exact."),
            ("Quoting the height as the cost of a lookup",
             "The height is how many levels exist; the cost is how many of them are not "
             "in memory. A four-level tree with its top two resident costs two reads, "
             "and the difference between two and four is the difference between a device "
             "that keeps up and one that does not."),
            ("Reasoning about the height as though the base were two",
             "`log₂(10⁹)` is about `30` and `log₅₀₀(10⁹)` is about `3.33`. A B-tree "
             "exists precisely to make the base the number of entries that fit on a "
             "page, and an intuition carried over from binary search trees — where the "
             "depth really does reach thirty — is an intuition about a different "
             "structure."),
        ],
        "standard": ("Finish when “a billion keys” stops sounding like a lot of levels.",
                     "You should be able to find a height by multiplying a fanout out, "
                     "state the level sizes and therefore which of them memory will "
                     "hold, and convert a lookup rate into a disk read rate without "
                     "going anywhere near a logarithm."),
        "note": (
            "A tree costs its height for a point lookup and a hash index costs one, "
            "which sounds settled until a query asks for a range. “Hash vs Tree for "
            "Ranges” counts both engines on the same workload, and the ordering reverses "
            "by a factor of nearly a hundred and seventy."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "hash-vs-tree-for-ranges",
        "title": "Hash vs Tree for Ranges",
        "module": "The cost model",
        "one_line": "Count the I/Os a mixed workload costs on a hash index and on a B-tree, and solve for the range rate at which the ordering reverses.",
        "summary": (
            "A hash index answers a point lookup in one I/O and answers a range query "
            "only by reading the whole table, because hashing destroys the order a range "
            "needs. A tree pays its height on both. On a workload of nine hundred "
            "lookups and a hundred small ranges a second that is `500 900` I/O against "
            "`3 000`, and “hash is faster” turns out to be a true claim about one "
            "operation wearing the clothes of a claim about an index."
        ),
        "key": [
            "hash    point  1 I/O            range  a full scan = rows / rows a page",
            "tree    point  h I/O            range  (h − 1) + ⌈k / rows a page⌉",
            "",
            "10⁶ rows, B = 500, 200 rows a page, ranges returning 100 rows",
            "                point      range         900 point/s + 100 range/s",
            "hash                1      5 000               500 900 I/O a second",
            "tree                3          3                 3 000 I/O a second",
        ],
        "key_label": "Both engines on the same two operations, and then on the same mix",
        "concepts_intro": (
            "Two structures, two operations, four numbers. The argument people have "
            "about this is entirely caused by quoting one of the four."
        ),
        "concepts": [
            ("A hash index is fast at exactly one thing",
             "It computes a bucket from a key and reads it: one I/O, no descent, no "
             "comparisons. The expected probe length behind that `1` is `Θ(1 + α)` under "
             "simple uniform hashing, with a `Θ(n)` worst case no hash function removes; "
             "“Hashing with Chaining” on the Algorithms path establishes both, and this "
             "lesson uses them rather than re-deriving them. What the structure spends "
             "to get that `1` is the order of the keys."),
            ("A range query has no hash plan at all",
             "There is no way to ask a hash index for the keys between two values except "
             "to look at every one of them, so a range costs a full scan: `10⁶` rows at "
             "`200` rows a page is `5 000` page reads. It is not that a hash is slower at "
             "ranges. It is that it has no access path for them, and what you are pricing "
             "is the table scan the planner falls back to."),
            ("A tree charges its height and then walks",
             "A B-tree descends to the first matching key and then reads leaves in key "
             "order, so a range of `k` rows costs about `(h − 1) + ⌈k/rows per page⌉`. "
             "Over a million rows at `B = 500` the height is `3`, and a range of a "
             "hundred rows is `3` I/Os altogether: two internal levels, then one leaf "
             "that already holds all hundred."),
        ],
        "read_title": "One I/O, or the whole table",
        "read_intro": "What a hash index gives up for its point lookup, and what that costs on the operation it gave up.",
        "body": [
            ("def", ("Point lookup and range query",
                     "A <strong>point lookup</strong> retrieves the row for one exact "
                     "key. A <strong>range query</strong> retrieves every row whose key "
                     "lies between two bounds, and is priced by the number of rows `k` it "
                     "returns.",
                     "An index is <strong>ordered</strong> if it stores keys in a "
                     "comparison order, and <strong>unordered</strong> if it stores them "
                     "by a hash of the key. Only an ordered index has an access path for "
                     "a range.")),
            ("p", "The hash index's `1` is worth taking seriously rather than waving at. "
                  "Under simple uniform hashing the expected number of probes is "
                  "`Θ(1 + α)` in the load factor `α`, so a table kept at a sensible load "
                  "factor really does answer in about one access — and the worst case, "
                  "where every key collides, really is `Θ(n)`. Those are Algorithms' "
                  "results, proved in “Hashing with Chaining”; what this lesson adds is "
                  "that on disk the unit is a page read and the constant is therefore "
                  "expensive."),
            ("math", [
                "10⁶ rows     B = 500     200 rows a page     ranges return 100 rows",
                "",
                "hash    point    1 I/O",
                "        range    10⁶ / 200                    =  5 000 I/O   (full scan)",
                "",
                "tree    height   500² = 250 000 < 10⁶ ≤ 125 000 000 = 500³   →   h = 3",
                "        point    3 I/O",
                "        range    (3 − 1) + ⌈100/200⌉          =      3 I/O",
                "",
                "mix     900 point/s + 100 range/s",
                "        hash     900(1) + 100(5 000)          =  500 900 I/O a second",
                "        tree     900(3) + 100(3)              =    3 000 I/O a second",
            ]),
            ("p", "The hash index does one hundred and sixty-seven times the I/O of the "
                  "tree on that mix, and it is genuinely three times cheaper on the "
                  "operation it is good at. Both facts come out of the same four numbers. "
                  "Which one you quote is a choice about what you want the answer to be."),
            ("h3", "Where the ordering reverses"),
            ("p", "Set the two totals equal and solve for the range rate `r` at a fixed "
                  "point rate. With `900` point lookups a second: "
                  "`900(1) + r(5 000) = 900(3) + r(3)`, so `r(5 000 − 3) = 900(3 − 1)` "
                  "and `r = 1800/4997 ≈ 0.360` range scans a second. One range query "
                  "every three seconds is enough to make the tree the cheaper engine on "
                  "this table."),
            ("example", ("A workload where the hash genuinely wins",
                         "Remove the ranges entirely. At `900` point lookups a second and "
                         "nothing else, the hash index does `900` I/O a second and the "
                         "tree does `2 700` — three times as many, exactly the ratio of "
                         "`1` to `h`. The true claim behind “hash is faster” is alive; it "
                         "is just very small, and it is a claim about one operation.")),
            ("p", "The same misconception exists in memory, where “a hash table is always "
                  "the fastest map” is corrected by pointing out that it cannot answer "
                  "predecessor, range or ordered iteration at all. “Choosing a Structure” "
                  "on the Algorithms path is that statement. This lesson is the same fact "
                  "with a disk attached, and the disk is what turns a structural "
                  "limitation into a number: not “unsupported” but `5 000` I/O."),
            ("p", "What the count assumes: that pages hold their nominal number of rows, "
                  "that nothing is cached, and that the range is contiguous in the index's "
                  "key order. Cache the tree's top two levels and its point lookup falls "
                  "from `3` to `1`, at which point the hash index's advantage on the "
                  "operation it is good at disappears entirely — which is worth knowing "
                  "before anyone builds an argument on the `1` against `3`."),
        ],
        "lab": ("storage", {
            "mode": "rangeq",
            "panel_title": "Set the mix and the width of a range",
            "panel_intro": (
                "Both totals are the same two products summed: point rate times I/O a "
                "point, plus range rate times I/O a range. Take the range rate down to "
                "zero and watch the hash index win; bring it back to one range every "
                "three seconds and watch them tie."
            ),
        }),
        "steps_title": "Counting a workload in I/Os",
        "steps_intro": "Four costs, then two products, then a comparison. The order stops you from quoting the wrong one of the four.",
        "steps": [
            ("Write all four costs before looking at the workload",
             "Point and range, hash and tree. Any claim about an index made from fewer "
             "than four numbers is a claim about one operation, and it will be defended "
             "as though it were about the index."),
            ("Count a range in pages, not in rows",
             "A range returning `k` rows at `p` rows a page is `⌈k/p⌉` leaf pages, and a "
             "full scan of `n` rows is `⌈n/p⌉` pages. Rows are what the query asks for; "
             "pages are what the device delivers."),
            ("Multiply each cost by its rate and add",
             "`point rate × I/O a point + range rate × I/O a range`, for each engine, in "
             "I/O a second. Now the two engines are comparable, which they were not when "
             "the units were operations."),
            ("Solve for the rate that ties them",
             "Set the two totals equal and solve for whichever rate is in doubt. The "
             "crossover is more useful than the winner: it tells you how much of the "
             "workload would have to change to change the answer, and here that is one "
             "range query every three seconds."),
        ],
        "worked": {
            "title": "900 point lookups and 100 ranges a second over a million rows",
            "intro": [
                "Four costs, two totals, and then the rate at which the two totals meet."
            ],
            "lines": [
                "10⁶ rows      4 kB page holds 500 index entries or 200 rows",
                "ranges return 100 rows      900 point lookups/s      100 ranges/s",
                "",
                "tree height     500² = 250 000 < 10⁶ ≤ 125 000 000 = 500³    →    h = 3",
                "",
                "                         hash index              B-tree",
                "  point lookup             1 I/O                  3 I/O",
                "  range of 100 rows    5 000 I/O  (full scan)     3 I/O   = 2 + ⌈100/200⌉",
                "",
                "  900 point lookups/s        900                 2 700",
                "  100 range scans/s      500 000                   300",
                "  the mix                500 900                 3 000",
                "",
                "crossover     900(1) + r(5 000) = 900(3) + r(3)",
                "              r(4 997) = 1 800      r = 1 800/4 997 = 0.360 ranges a second",
            ],
            "after": [
                "The `5 000` contains no hash parameter. It is `10⁶/200`: rows divided by "
                "rows a page, which is what a scan costs when there is no access path. "
                "Doubling the buckets, improving the hash function or removing every "
                "collision leaves it exactly where it is.",
                "The crossover is the honest summary. At these page geometries the tree "
                "wins any workload with more than about one range scan every three "
                "seconds, and the hash index wins below that. Neither engine is faster; "
                "one of them is cheaper at your mix, and the mix is measurable.",
                "For a faded rehearsal, widen the range to `1 000` rows and keep "
                "everything else. The supplied first move is that the tree's range cost "
                "becomes `2 + ⌈1 000/200⌉`. Compute it, recompute both totals, and then "
                "say what happened to the crossover rate and why it moved in the "
                "direction it did. Run the lab at your numbers before opening the quiz.",
            ],
        },
        "quiz_title": "Two engines, four costs",
        "quiz": [
            {"q": "A range query returns `100` rows from a million-row table with `200` rows to a page. What does it cost on a hash index?",
             "a": ["`1` I/O, the same as a point lookup",
                   "`1` I/O per row, so `100`",
                   "`5 000` I/O — the whole table, `10⁶/200` pages",
                   "`3` I/O, the height of the equivalent tree"],
             "c": 2,
             "why": "A hash index stores keys by hash, so the rows of a range are "
                    "scattered across every bucket and the only way to find them is to "
                    "read everything: `10⁶/200 = 5 000` pages. `100` would be one I/O a "
                    "row, which is worse than a scan, not better; the `3` is what the "
                    "tree charges."},
            {"q": "On the same table the workload is `900` point lookups and `100` ranges a second. Which engine does less I/O, and by roughly how much?",
             "a": ["The hash index, by about three times",
                   "The B-tree, by about one hundred and sixty-seven times",
                   "They are within a few per cent of each other",
                   "The hash index, by about one hundred and sixty-seven times"],
             "c": 1,
             "why": "`500 900` against `3 000`. The hash index is three times cheaper on "
                    "the point lookups — `900` against `2 700` — and that advantage is "
                    "swamped by `100 × 5 000` I/O of scans. The first answer quotes the "
                    "true fact about the wrong operation."},
            {"q": "At `900` point lookups a second, how many range scans a second make the two engines cost the same?",
             "a": ["About `0.36` a second", "About `3.6` a second", "About `36` a second", "`900`, one per lookup"],
             "c": 0,
             "why": "`900(1) + r(5 000) = 900(3) + r(3)` gives `r = 1 800/4 997 ≈ 0.360`. "
                    "One range query every three seconds is the whole margin: the tree's "
                    "extra `2` I/O on each of nine hundred lookups is `1 800`, and one "
                    "scan costs `4 997` more than the tree's range."},
            {"q": "The B-tree's top two levels are cached, so a point lookup costs `1` I/O rather than `3`. What happens to the comparison?",
             "a": ["The hash index becomes cheaper on the mix",
                   "The tree matches the hash on point lookups and still wins the mix outright",
                   "Nothing; caching affects both engines equally",
                   "The crossover rate rises above `100` ranges a second"],
             "c": 1,
             "why": "Caching the top two levels removes two of the three reads in "
                    "every descent, so a tree point lookup costs `1` I/O — the same as "
                    "the hash index's. Its range still costs a handful of leaf reads "
                    "against a `5 000`-page scan, so the tree wins the mix by more than "
                    "before. Caching helps a hash index too; it simply has no descent to "
                    "remove, and its `1` cannot go below `1`."},
        ],
        "mistakes": [
            ("Saying that one index is faster than another",
             "There is no such quantity. The four costs here are `1`, `5 000`, `3` and "
             "`3`, and every honest sentence names an operation: faster at point lookups, "
             "by a factor of three, on an uncached tree. A claim without the operation in "
             "it cannot be checked, and it is usually the true claim about the wrong half "
             "of the workload."),
            ("Counting a range in rows",
             "A range returning `100` rows out of pages holding `200` is one page read, "
             "not a hundred. The device delivers pages, so a range is `⌈k/rows per page⌉` "
             "leaves however few rows it returns — which is also why widening a range "
             "from ten rows to a hundred can cost nothing at all."),
            ("Expecting a better hash to fix the range",
             "The `5 000` is `10⁶/200`: rows divided by rows a page, containing no hash "
             "parameter of any kind. It is the cost of having no access path. More "
             "buckets, a better function or zero collisions leave it untouched, because "
             "the problem is not collisions — it is that the order was thrown away on "
             "purpose."),
        ],
        "standard": ("Finish when you answer “which is faster” with a question about the mix.",
                     "You should be able to write down all four costs for a stated page "
                     "geometry, total a workload in I/O a second on both engines, and "
                     "solve for the rate at which the answer changes."),
        "note": (
            "Both engines here were priced for readers. “The Write Cost of an Index” "
            "prices the same indexes for the writer, and the arithmetic is a division "
            "rather than an addition — which is why the answer surprises people who have "
            "only ever been shown the read side."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-write-cost-of-an-index",
        "title": "The Write Cost of an Index",
        "module": "The write side",
        "one_line": "Compute the random writes an insert costs with `k` indexes, the insert rate that leaves, and the most indexes a throughput target allows.",
        "summary": (
            "An index has to contain the column it answers questions about, so inserting "
            "a row changes every index on the table. With `k` of them an insert is "
            "`k + 1` random writes and throughput is divided by `k + 1` — not reduced by "
            "a percentage. A device doing ten thousand random writes a second carries "
            "two and a half thousand inserts a second once three indexes are on the table."
        ),
        "key": [
            "writes per insert = k + 1          the row, and one page in every index",
            "inserts a second  = device / (k + 1)",
            "",
            "device 10 000 random writes a second",
            "k = 0   1 write  10 000/s  100%      k = 3   4 writes  2 500/s  25.0%",
            "k = 1   2 writes   5 000/s   50%     k = 4   5 writes  2 000/s  20.0%",
            "",
            "⌊10 000 / 2 500⌋ − 1 = 3      the most indexes a 2 500/s target allows",
        ],
        "key_label": "The exchange rate between a reader's index and a writer's throughput",
        "concepts_intro": (
            "One addition and one division. The addition is obvious once it is said; the "
            "division is where the intuition goes wrong, because people expect a subtraction."
        ),
        "concepts": [
            ("An insert touches every index",
             "The row goes into the table and a key goes into each of the `k` indexes, so "
             "an insert is `k + 1` writes. Nothing here depends on the index being clever "
             "or badly designed: a structure that answers questions about a column has to "
             "contain that column, and inserting a row changes that column."),
            ("The writes are random, and that is the expensive word",
             "Each index is ordered on a different key, so where an insert lands in one "
             "index says nothing about where it lands in another. An insert that is "
             "perfectly sequential in the table is `k` scattered page writes elsewhere. "
             "That is why the cost is `k + 1` <em>random</em> writes rather than "
             "`k + 1` bytes, and it is the seek term of the first lesson arriving on the "
             "write side."),
            ("Throughput divides, it does not decrease by a percentage",
             "If the device sustains `D` random writes a second, inserts run at "
             "`D/(k + 1)` and the share left is `1/(k + 1)`: `1/2` at one index, `1/4` at "
             "three, `1/9` at eight. The first index is the expensive one — it halves the "
             "write rate on its own — and every index after it costs less than the one "
             "before."),
        ],
        "read_title": "k + 1 random writes, and the throughput that leaves",
        "read_intro": "Why the first index is the expensive one, and how to turn a throughput target into a budget of indexes.",
        "body": [
            ("def", ("Write cost of an index",
                     "For a table carrying `k` secondary indexes, one insert performs "
                     "`k + 1` <strong>random writes</strong>: one for the row and one for "
                     "each index page the new key lands on. On a device sustaining `D` "
                     "random writes a second the insert rate is `D/(k + 1)`, and the "
                     "<strong>share of the bare rate</strong> is `1/(k + 1)`.",
                     "The same count holds for a delete, and an update counts once for "
                     "every index whose key it changes.")),
            ("p", "Nothing in that definition is about how a particular engine is built. "
                  "It is what it means for an index to be an index. A query planner can "
                  "choose not to use an index; the writer has no such choice, because an "
                  "index that skipped an insert would be wrong."),
            ("math", [
                "device       10 000 random writes a second",
                "",
                "indexes k        0        1        2        3        4        5",
                "writes/insert    1        2        3        4        5        6",
                "inserts/s   10 000    5 000    3 333    2 500    2 000    1 667",
                "share            1      1/2      1/3      1/4      1/5      1/6",
                "              100%    50.0%    33.3%    25.0%    20.0%    16.7%",
            ]),
            ("p", "Read the last row from left to right. The first index costs fifty "
                  "percentage points, the second seventeen, the third eight, the fourth "
                  "five. `1/(k + 1)` falls fastest at the start, so the question “can we "
                  "afford one more index?” has a different answer depending on how many "
                  "there already are — and the cheapest place to add one is a table that "
                  "already has several."),
            ("example", ("Three indexes on a ten-thousand-write device",
                         "`k = 3` makes an insert `4` random writes, so a device doing "
                         "`10 000` random writes a second does `2 500` inserts a second: "
                         "`25%` of its bare rate. The device did not get slower and the "
                         "rows did not get bigger. Three quarters of its write budget is "
                         "now being spent keeping indexes correct.")),
            ("h3", "Turning a target into a budget of indexes"),
            ("p", "Run the division the other way. If the workload needs `T` inserts a "
                  "second on a device doing `D` random writes a second, the writes "
                  "available per insert are `D/T` and the indexes you can afford are "
                  "`⌊D/T⌋ − 1`. At `D = 10 000` and `T = 2 500` that is `3`. Raise the "
                  "target by twenty per cent, to `3 000`, and it falls to `2`: the "
                  "relation is a floor, so it moves in whole indexes, and every index is "
                  "free until the division crosses an integer."),
            ("p", "This is the arithmetic that makes an index a decision rather than an "
                  "optimisation. An index that serves a query is worth it; an index that "
                  "was added years ago for a report nobody runs is still being written on "
                  "every insert, and the way to see that is to price it in the units "
                  "above rather than in megabytes."),
            ("p", "One honest caveat. An engine that buffers index updates — a change "
                  "buffer, or an LSM's memtable — converts some of these random writes "
                  "into sequential ones performed later, which is exactly the trade "
                  "“Write Amplification in LSM Trees” prices. The `k + 1` is the count of "
                  "index pages that must eventually be written. When they are written, "
                  "and how many times each, is a different question with a much larger "
                  "answer."),
        ],
        "lab": ("storage", {
            "mode": "indexcost",
            "panel_title": "Add indexes and watch the writer pay",
            "panel_intro": (
                "Insert throughput is the device's random-write rate divided by `k + 1`, "
                "recomputed as you move `k`. Start at three indexes, then take `k` to zero "
                "one index at a time and watch which single step costs the most."
            ),
        }),
        "steps_title": "Pricing the write side of an index",
        "steps_intro": "Two of these steps are the calculation and two are the decision it is for.",
        "steps": [
            ("Count the indexes, then add one",
             "`k` secondary indexes and the table itself: `k + 1` random writes an "
             "insert. Count every index that exists, not every index the queries use — "
             "the writer pays for all of them."),
            ("Divide the device's random-write rate",
             "`D/(k + 1)` is the insert rate. Use the device's <em>random</em> write "
             "figure, not its sequential one; the two can differ by two orders of "
             "magnitude and only one of them is relevant here."),
            ("Hold it against what the workload needs",
             "If the required insert rate is above `D/(k + 1)` the table is already over "
             "budget, and no amount of query tuning changes that: the shortfall is on the "
             "write path."),
            ("Invert it to get the index budget",
             "`⌊D/T⌋ − 1` is the most indexes a target of `T` inserts a second allows. It "
             "is a floor, so it steps: knowing where the next step is tells you how much "
             "headroom the table actually has."),
        ],
        "worked": {
            "title": "Three indexes on a device that does 10 000 random writes a second",
            "intro": [
                "One division, run across every plausible index count, and then run "
                "backwards from two throughput targets."
            ],
            "lines": [
                "device      10 000 random writes a second",
                "",
                "indexes k         0        1        2        3        4        5",
                "writes/insert     1        2        3        4        5        6",
                "inserts/s    10 000    5 000    3 333    2 500    2 000    1 667",
                "share             1      1/2      1/3      1/4      1/5      1/6",
                "               100%    50.0%    33.3%    25.0%    20.0%    16.7%",
                "cost of this index      −50.0    −16.7     −8.3     −5.0     −3.3  points",
                "",
                "target 2 500 inserts/s      ⌊10 000 / 2 500⌋ − 1  =  4 − 1  =  3 indexes",
                "target 3 000 inserts/s      ⌊10 000 / 3 000⌋ − 1  =  3 − 1  =  2 indexes",
            ],
            "after": [
                "The index that halves throughput is the first one. Not the fifth, not "
                "the tenth: going from none to one costs fifty percentage points and "
                "going from three to four costs five, because `1/(k + 1)` falls fastest "
                "at the start. Anyone who has ever said “one more index will not hurt” "
                "was right, and was right for a reason that stops applying at `k = 0`.",
                "Raising the required insert rate by twenty per cent, from `2 500` to "
                "`3 000`, costs an index. The budget is a floor function, so it changes "
                "in whole indexes at the points where the division crosses an integer, "
                "and between those points a target can move a long way for free.",
                "For a faded rehearsal, take a device that sustains `6 000` random writes "
                "a second and a workload needing `1 000` inserts a second. The supplied "
                "first move is that the answer is a floor: `⌊6 000/1 000⌋ − 1`. Compute "
                "it, then state the insert rate you actually get at that many indexes and "
                "how much headroom is left over. Run the lab at your numbers before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "Indexes, writes and throughput",
        "quiz": [
            {"q": "A table has `4` indexes and the device sustains `10 000` random writes a second. What is the insert rate?",
             "a": ["`2 500` a second", "`2 000` a second", "`6 000` a second", "`10 000` a second, indexes are read structures"],
             "c": 1,
             "why": "`4` indexes make an insert `5` random writes, so "
                    "`10 000/5 = 2 000` inserts a second. `2 500` is the answer for three "
                    "indexes; `6 000` subtracts forty per cent rather than dividing by "
                    "five. Indexes are read structures that have to be written."},
            {"q": "Which single index costs the most insert throughput?",
             "a": ["The first", "The last", "Whichever has the largest keys", "They all cost the same fraction"],
             "c": 0,
             "why": "Throughput is `D/(k + 1)`, so the share falls `1 → 1/2 → 1/3 → 1/4`: "
                    "fifty percentage points for the first index, seventeen for the "
                    "second, eight for the third. Key size changes how much data is "
                    "written and not how many random writes there are, which is what the "
                    "device is rate-limited on."},
            {"q": "An insert appends a row to the end of a table. Why are the index writes random?",
             "a": ["Because indexes are stored on a different device",
                   "Because each index is ordered on a different key, so the new entry lands in an unrelated place in each one",
                   "Because the engine deliberately scatters writes to spread wear",
                   "They are not; the index entries are appended too"],
             "c": 1,
             "why": "A table can be append-ordered while an index on a customer name and "
                    "another on a timestamp put the same new row in two completely "
                    "unrelated pages. That is what makes the cost `k + 1` seeks rather "
                    "than `k + 1` bytes, and it is why the ordering of the table buys the "
                    "indexes nothing."},
            {"q": "The device does `10 000` random writes a second and the workload needs `3 000` inserts a second. How many indexes can the table carry?",
             "a": ["`1`", "`2`", "`3`", "`4`"],
             "c": 1,
             "why": "`⌊10 000/3 000⌋ − 1 = 3 − 1 = 2`. At two indexes an insert is three "
                    "writes and the rate is `3 333` a second, which clears the target; at "
                    "three indexes it is `2 500`, which does not. `3` is the budget for a "
                    "`2 500` target, which is a different question."},
        ],
        "mistakes": [
            ("Counting an index's cost in bytes",
             "An index entry may be sixteen bytes, which sounds free. The cost is not the "
             "bytes — it is that those sixteen bytes are somewhere else on the device, "
             "and the device is rate-limited on how many separate somewhere-elses it can "
             "reach in a second. Price an index in random writes and the number stops "
             "looking free."),
            ("Believing an unused index is free",
             "The planner can ignore an index; the writer cannot. An index that no query "
             "has touched in a year is still one of the `k`, still one random write on "
             "every insert, and still dividing throughput. Dropping it is the only "
             "operation that removes it from the count."),
            ("Reading `k + 1` as a penalty to subtract",
             "It divides. Three indexes do not cost thirty per cent of the write rate; "
             "they cost seventy-five per cent of it, leaving `1/4`. Anyone whose estimate "
             "of an index's cost is a small percentage has done a subtraction where the "
             "arithmetic is a division."),
        ],
        "standard": ("Finish when “add an index” sounds like a division rather than a favour.",
                     "You should be able to state the writes an insert costs from the "
                     "index count, convert that into an insert rate on a stated device, "
                     "and invert it to say how many indexes a throughput target allows."),
        "note": (
            "The `k + 1` random writes here are exactly what a log-structured engine "
            "refuses to pay at insert time. The bill it pays instead is the subject of "
            "“Write Amplification in LSM Trees”: twenty-five bytes written for every byte "
            "handed over, on ordinary settings, and all of them sequential."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "write-amplification-in-lsm-trees",
        "title": "Write Amplification in LSM Trees",
        "module": "The write side",
        "one_line": "Compute the write and read amplification of a levelled LSM from its fanout and level count, and the compaction bandwidth they imply.",
        "summary": (
            "A levelled log-structured tree never writes randomly, and it writes "
            "everything about twenty-five times. Each of `L` levels rewrites a byte "
            "passing through it about `F/2` times, so `WA ≈ L·F/2`; and a lookup that "
            "finds nothing has to try every level, so `RA ≈ L` before any filter. "
            "Append-only describes the pattern of the writes, not their number."
        ),
        "key": [
            "WA ≈ L · F/2      each byte rewritten about F/2 times on each of L levels",
            "RA ≈ L            a miss has to be looked for on every level",
            "",
            "F = 10, L = 5       WA = 25×        RA = 5 probes",
            "",
            "compaction bandwidth = ingest × WA = 50 MB/s × 25 = 1.25 GB/s",
        ],
        "key_label": "What an append-only engine writes, and what a lookup reads",
        "concepts_intro": (
            "One new idea — the F/2 — and two consequences of it that decide what "
            "hardware the engine needs."
        ),
        "concepts": [
            ("A level rewrites about `F/2` bytes for every byte that passes through it",
             "Merging a run into a level rewrites the part of that level it overlaps. "
             "When the merge happens, the level is on average about half full of the data "
             "it will eventually hold, so a byte crossing it is rewritten about `F/2` "
             "times before it moves on. That is the `F/2`, and it is an average over the "
             "level's filling cycle rather than a count of anything."),
            ("Every level charges it, so the total is `L·F/2`",
             "There are `L` levels between the memtable and the bottom and a byte crosses "
             "all of them, so `5` levels at `F/2 = 5` rewrites each is `25` bytes written "
             "for every byte the engine was handed. Every one of those writes was "
             "sequential. There were simply twenty-five times as many of them as the "
             "writer asked for."),
            ("Read amplification is the level count, before filters",
             "A key that is not present has to be searched for on every level, because no "
             "level can prove the absence of a key that another might hold. That is "
             "`RA ≈ L = 5` probes for a miss. It is the one number on this page that can "
             "be bought back cheaply, and “Bloom Filters: Bits per Key” is where it is "
             "bought."),
        ],
        "read_title": "L levels at F/2 rewrites each, and the bandwidth that implies",
        "read_intro": "Why sequential writing is not the same as cheap writing, and what number to size a device against.",
        "body": [
            ("def", ("Write and read amplification",
                     "<strong>Write amplification</strong> is the bytes an engine writes "
                     "to durable storage for every byte the application hands it. "
                     "<strong>Read amplification</strong> is the storage reads a single "
                     "logical lookup performs.",
                     "For a levelled LSM tree with fanout `F` and `L` levels these are "
                     "`WA ≈ L·F/2` and `RA ≈ L`. Both are counts, both are ratios, and "
                     "neither is a latency.")),
            ("p", "The `F/2` is the part worth slowing down for. It is not `F`. A merge "
                  "into a level rewrites whatever part of that level overlaps the "
                  "incoming run, and a level spends its life filling from empty to full "
                  "between merges — so averaged over that cycle, a byte passing through "
                  "is rewritten about half of `F` times rather than `F` times. Every "
                  "figure on this page inherits that word “about”."),
            ("math", [
                "memtable 64 MB      F = 10      L = 5      ingest 50 MB/s",
                "",
                "  level    capacity = memtable · Fᴸ    rewrites a byte    bandwidth    cumulative",
                "    L1                    640.00 MB            5 ×      250.00 MB/s        5 ×",
                "    L2                      6.40 GB            5 ×      250.00 MB/s       10 ×",
                "    L3                     64.00 GB            5 ×      250.00 MB/s       15 ×",
                "    L4                    640.00 GB            5 ×      250.00 MB/s       20 ×",
                "    L5                      6.40 TB            5 ×      250.00 MB/s       25 ×",
                "",
                "  WA = L · F/2 = 5 × 5 = 25        compaction = 25 × 50 MB/s = 1.25 GB/s",
                "  RA = L = 5 probes on a miss",
            ]),
            ("p", "The last column is the whole lesson. A device sized to the ingest rate "
                  "needs `50 MB/s`; the engine needs `1.25 GB/s`, and it needs it whether "
                  "or not anybody is reading. That factor of twenty-five is not overhead "
                  "in the loose sense — it is the mechanism by which the writes became "
                  "sequential in the first place."),
            ("example", ("How many levels the data actually forces",
                         "The level count is not really a setting. Level capacities are "
                         "`memtable × Fᴸ`, so at a `64 MB` memtable and `F = 10` the "
                         "levels hold `640 MB`, `6.40 GB`, `64 GB`, `640 GB` and "
                         "`6.40 TB`. A terabyte of data does not fit in four levels and "
                         "does fit in five, so `L = 5` — found by the same integer search "
                         "that gives a B-tree its height, multiplying `F` in until the "
                         "capacity covers the data.")),
            ("h3", "The misconception: append-only means cheap"),
            ("p", "It means <em>sequential</em>, which is a claim about the first term of "
                  "the read-time formula and a good one: an LSM has no random writes at "
                  "all on the ingest path, which is exactly what “The Write Cost of an "
                  "Index” showed a B-tree paying `k + 1` of. What it does not mean is "
                  "few. The engine bought a better access pattern by agreeing to rewrite "
                  "the data twenty-five times, and both halves of that sentence are the "
                  "design."),
            ("p", "Lowering the fanout lowers the write amplification and raises "
                  "everything else. At `F = 4` the same terabyte over the same memtable "
                  "forces `7` levels, so `WA` falls to `14` — `700 MB/s` of compaction "
                  "instead of `1.25 GB/s` — and `RA` rises from `5` probes to `7`. There "
                  "is no setting of `F` that improves both, which is the shape “The RUM "
                  "Trade-off” draws as a triangle."),
            ("p", "Two caveats the lab carries. `WA ≈ L·F/2` describes levelled "
                  "compaction; a tiered engine merges whole runs instead and pays `L` "
                  "rather than `L·F/2`, in exchange for a much worse read amplification. "
                  "And compaction is bursty: `1.25 GB/s` is the average the device must "
                  "sustain, while the instantaneous demand during a large merge is higher "
                  "and the demand between merges is lower."),
        ],
        "lab": ("storage", {
            "mode": "lsm",
            "panel_title": "Set the fanout, the levels and the ingest rate",
            "panel_intro": (
                "Write amplification is `L × F/2`, summed one level at a time in the "
                "table, and the compaction bandwidth is the ingest rate multiplied by it. "
                "Drop the fanout to `4` and watch the amplification fall while the level "
                "count the data forces climbs — the two move in opposite directions and "
                "the table shows both."
            ),
        }),
        "steps_title": "Pricing a log-structured write",
        "steps_intro": "Get the level count from the data before you trust the level count in the configuration.",
        "steps": [
            ("Find the levels the data forces",
             "Multiply the memtable size by `F` repeatedly until the capacity covers the "
             "dataset, and count the multiplications. A configured level count below that "
             "is not a smaller tree; it is a tree that will grow one."),
            ("Multiply `L` by `F/2`",
             "That is the write amplification, and it is a pure ratio: bytes written per "
             "byte ingested, with no device in it yet. At `F = 10` and `L = 5` it is `25`."),
            ("Multiply the ingest rate by the amplification",
             "`50 MB/s × 25 = 1.25 GB/s` of sustained write bandwidth. This is the number "
             "a device is chosen against, and it is the one nobody quotes."),
            ("Write the read amplification down beside it",
             "`RA ≈ L` probes on a miss, before filters. Doing this in the same breath is "
             "what stops a fanout change from looking like a free improvement, because "
             "the two amplifications move in opposite directions."),
        ],
        "worked": {
            "title": "A terabyte at F = 10, ingested at 50 MB/s",
            "intro": [
                "The level count comes from the data, the amplification comes from the "
                "level count, and the bandwidth comes from the amplification."
            ],
            "lines": [
                "memtable 64 MB      F = 10      ingest 50 MB/s      data 1.00 TB",
                "",
                "  level     capacity      rewrites a byte    bandwidth at 50 MB/s   cumulative WA",
                "    L1     640.00 MB              5 ×              250.00 MB/s            5 ×",
                "    L2       6.40 GB              5 ×              250.00 MB/s           10 ×",
                "    L3      64.00 GB              5 ×              250.00 MB/s           15 ×",
                "    L4     640.00 GB              5 ×              250.00 MB/s           20 ×",
                "    L5       6.40 TB              5 ×              250.00 MB/s           25 ×",
                "",
                "  1.00 TB does not fit in L4 (640.00 GB) and fits in L5     →     L = 5",
                "",
                "  WA = L · F/2 = 5 × 5              =     25 bytes written per byte in",
                "  compaction   = 25 × 50 MB/s       =  1.25 GB/s of sustained write bandwidth",
                "  RA = L                            =      5 probes on a lookup that misses",
            ],
            "after": [
                "Two numbers describe the same engine and only one of them is ever on a "
                "dashboard. The ingest is `50 MB/s`; the disk sees `1.25 GB/s`. Sizing a "
                "device against the first figure is not a small error — it is off by a "
                "factor of twenty-five, and the symptom is an engine that keeps up until "
                "compaction falls behind and then never catches up again.",
                "Lower the fanout to `4` and the arithmetic moves the other way: the "
                "terabyte now forces `7` levels, `WA` falls to `14` and the compaction "
                "bandwidth to `700 MB/s`, while the read amplification rises from `5` "
                "probes to `7`. Cheaper writes, dearer reads, bought at a fixed exchange "
                "rate.",
                "For a faded rehearsal, keep `F = 10` and set the level count to `3`. The "
                "supplied first move is that `WA` falls to `15`. Compute the compaction "
                "bandwidth at `50 MB/s`, then read the capacity column and say what the "
                "largest dataset three levels can actually hold over a `64 MB` memtable "
                "— which is the constraint the setting was hiding. Check both in the lab "
                "before opening the quiz.",
            ],
        },
        "quiz_title": "Amplification and bandwidth",
        "quiz": [
            {"q": "A levelled LSM has fanout `F = 10` and `L = 5` levels. What is its write amplification?",
             "a": ["`5`, one per level", "`10`, the fanout", "`25`", "`50`, `L × F`"],
             "c": 2,
             "why": "`WA ≈ L·F/2 = 5 × 5 = 25`. `5` is the read amplification and `50` "
                    "uses `F` where the merge costs `F/2`, because a level is on average "
                    "half full of its eventual contents when the merge into it happens."},
            {"q": "That engine ingests `50 MB/s`. What sustained write bandwidth does the device need?",
             "a": ["`50 MB/s`", "`250 MB/s`", "`1.25 GB/s`", "`2.50 GB/s`"],
             "c": 2,
             "why": "`ingest × WA = 50 MB/s × 25 = 1.25 GB/s`. `250 MB/s` is what one "
                    "level costs; there are five of them. Sizing the device to the "
                    "`50 MB/s` of ingest is the misconception this lesson exists for."},
            {"q": "Why is the per-level rewrite figure `F/2` rather than `F`?",
             "a": ["Because half of every merge is skipped when the keys do not overlap",
                   "Because a level is on average about half full of its eventual contents when a merge into it happens",
                   "Because compaction runs on two threads",
                   "Because half of the data is already in the page cache"],
             "c": 1,
             "why": "A level fills from empty toward full between merges, so averaged "
                    "over that cycle a byte crossing it is rewritten about `F/2` times "
                    "rather than `F`. It is an average over the filling cycle, not a "
                    "saving from skipped work or from concurrency."},
            {"q": "An engine performs no random writes at all. Does that make its writes cheap?",
             "a": ["Yes — sequential writes run at the device's full bandwidth",
                   "No — it says the writes are sequential, and here there are twenty-five times as many of them",
                   "Yes, provided the memtable is large enough",
                   "Only if read amplification is also `1`"],
             "c": 1,
             "why": "Sequential is a claim about the access pattern and a true one: an "
                    "LSM has no random writes on the ingest path at all. The count is a "
                    "separate question, and it is `25` bytes written per byte handed "
                    "over. A larger memtable changes the level count, not the exchange "
                    "rate."},
        ],
        "mistakes": [
            ("Sizing the disk to the ingest rate",
             "`50 MB/s` in means `1.25 GB/s` on the device at `F = 10` and `L = 5`. A "
             "device chosen against the ingest figure is undersized by the amplification "
             "factor, and the failure mode is delayed: everything works until compaction "
             "falls behind, at which point read amplification climbs too and the engine "
             "gets worse in both directions at once."),
            ("Reading “append-only” as “written once”",
             "Appending is how the data enters a level. Compaction is what happens to it "
             "afterwards, on every level, `F/2` times each. The log-structured design "
             "converted random writes into sequential ones by agreeing to do a great many "
             "more of them, and only one half of that bargain is in the name."),
            ("Lowering the fanout and quoting only the improvement",
             "Halving `F` from ten to five roughly halves the per-level rewrite count and "
             "raises the number of levels the data forces — so the read amplification "
             "goes up, and the write amplification falls by less than the fanout did. "
             "Any change to `F` has to be quoted with both amplifications and the level "
             "count, or it is a claim with its cost removed."),
        ],
        "standard": ("Finish when you can say what an engine writes as well as what it is given.",
                     "You should be able to derive the level count from the memtable and "
                     "the dataset, compute both amplifications from `F` and `L`, and turn "
                     "the write amplification into the sustained device bandwidth the "
                     "engine actually needs."),
        "note": (
            "The five probes a miss costs here are what a filter on every level removes "
            "almost entirely. “Bloom Filters: Bits per Key” sizes that filter — about ten "
            "bits a key at a one per cent false-positive rate, independent of how many "
            "keys there are — and turns a read amplification of `5` into `1.04`."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "bloom-filters",
        "title": "Bloom Filters: Bits per Key",
        "module": "Filters and the trade-off",
        "one_line": "Size a filter from a target false-positive rate, compute the memory it costs for `n` keys, and the read amplification a filter per level leaves.",
        "summary": (
            "A Bloom filter's space cost is about `log₂(1/p)/ln 2` bits for every key it "
            "holds, and that figure does not depend on `n` at all: one per cent costs "
            "about `9.585` bits a key whether the set has a thousand members or a "
            "billion. Put one on every level of a log-structured tree and a read "
            "amplification of `5` becomes `1.04`, for `1.20 GB` of memory over a billion "
            "keys."
        ),
        "key": [
            "bits a key ≈ log₂(1/p) / ln 2          independent of n",
            "",
            "p = 1/10      4.7925 bits      p = 1/1 000    14.3776 bits",
            "p = 1/100     9.5851 bits      p = 1/10 000   19.1701 bits",
            "",
            "n = 10⁹ at p = 1/100  →  9 585 058 378 bits = 1.20 GB,  k = 7 hashes",
            "read amplification with a filter per level = 1 + (L − 1)p = 1.04 at L = 5",
        ],
        "key_label": "Bits a key at a target rate, and the read amplification it leaves",
        "concepts_intro": (
            "One formula, one property of it that surprises everybody, and one design "
            "fact without which the whole use would be unsound."
        ),
        "concepts": [
            ("The bargain is bits per key, and it does not depend on `n`",
             "At the number of hash functions that minimises the error, a filter needs "
             "about `log₂(1/p)/ln 2` bits for each key it holds. Double the keys and the "
             "filter doubles; the bits per key do not move. So the sizing question is "
             "never “how large is my dataset” but “what false-positive rate am I buying”, "
             "and one per cent costs a little under ten bits a key."),
            ("The error is one-sided, and everything depends on that",
             "If any of the `k` positions a key hashes to is clear, that key was never "
             "inserted: a clear bit is a certain negative. The filter can say "
             "<em>possibly</em> about a key that is absent; it can never say "
             "<em>no</em> about a key that is present. A structure that could say no "
             "wrongly would be useless for skipping a disk read, because the read it "
             "skipped might be the one holding the answer."),
            ("A filter per level turns `L` probes into `1 + (L − 1)p`",
             "A lookup still reads the level that holds the key. On the other `L − 1` "
             "levels it is sent to disk only by a false positive, which happens with "
             "probability `p` on each. At `L = 5` and `p = 1/100` that is "
             "`1 + 4/100 = 1.04` probes — the read amplification an LSM paid for its "
             "sequential writes, bought back for about a gigabyte of memory."),
        ],
        "read_title": "Bits a key, the memory that costs, and the probes it removes",
        "read_intro": "The sizing formula, the constant people get wrong, and what a filter on every level does to a lookup.",
        "body": [
            ("def", ("Bloom filter",
                     "A <strong>Bloom filter</strong> for a set of `n` keys is an array "
                     "of `m` bits together with `k` hash functions. Inserting a key sets "
                     "the `k` bits it hashes to. A query reports <strong>possibly "
                     "present</strong> if all `k` of its bits are set, and "
                     "<strong>certainly absent</strong> if any one of them is clear.",
                     "The second answer is exact. The <strong>false-positive rate</strong> "
                     "`p` is the probability that a key which was never inserted "
                     "nevertheless finds all `k` of its bits set by other keys.")),
            ("p", "At the `k` that minimises the rate, the space needed is about "
                  "`m/n = log₂(1/p)/ln 2` bits a key and the hash count is about "
                  "`k = log₂(1/p)`. This lesson states those two and uses them to size "
                  "filters. The derivation, the exact form "
                  "`(1 − (1 − 1/m)^(kn))^k` under the idealisation that the hashes are "
                  "independent, the optimal `k = (m/n)·ln 2`, and the rule that a Bloom "
                  "filter supports no deletion all belong to “Bloom Filters” on the "
                  "Algorithms path, which owns them and proves them."),
            ("p", "The independence from `n` is the part worth pausing on, because it is "
                  "the reason a filter is a practical thing to build. A billion keys at "
                  "one per cent is `1.20 GB`; two billion keys at one per cent is "
                  "`2.40 GB`, and both are `9.5851` bits a key. Nothing about the filter "
                  "gets relatively worse as the set grows, which is unusual enough that "
                  "people assume it must be false."),
            ("math", [
                "bits a key = log₂(1/p) / ln 2                 1/ln 2 = 1.442695…",
                "",
                "p = 1/10         log₂(10)   = 3.3219    →     4.7925 bits a key",
                "p = 1/100        log₂(100)  = 6.6439    →     9.5851 bits a key",
                "p = 1/1 000      log₂(1000) = 9.9658    →    14.3776 bits a key",
                "",
                "n = 10⁹ at p = 1/100     m = 9 585 058 378 bits = 1.20 GB,  k = 7",
                "n = 2×10⁹ at the same p                       = 2.40 GB,  still 9.5851 a key",
            ]),
            ("h3", "9.585, not 9.57"),
            ("p", "The figure usually quoted for one per cent is `9.57` bits a key, and "
                  "it comes from writing the constant as `1.44`. The constant is "
                  "`1/ln 2 = 1.442695…`, and at `p = 1/100` the two produce `9.5851` and "
                  "`9.5672` — a gap of `0.0179` bits a key, which is about `2.2 MB` over "
                  "a billion keys. That is small, and it is the wrong kind of small to "
                  "leave unexplained on a page whose subject is exact counting. The lab "
                  "prints both columns side by side and says which constant produced "
                  "which, so the difference is visible rather than argued about."),
            ("p", "Both columns are approximations, and so is everything derived from "
                  "them. The bits-per-key figure is a logarithm and the false-positive "
                  "estimate is an exponential; neither returns a fraction, and the lab "
                  "labels every figure that inherits the rounding. Where an exact answer "
                  "still exists it shows one: at `m = 64`, `n = 8`, `k = 5` the exact "
                  "rate is `0.02230073` and the approximation gives `0.02167922`, so the "
                  "approximation is optimistic by about three per cent of itself at that "
                  "size. It gets better as `m` grows, which is why it is safe at the "
                  "sizes anyone actually builds."),
            ("h3", "What a filter does to a log-structured tree"),
            ("p", "A lookup that misses has to try every level, which “Write "
                  "Amplification in LSM Trees” priced at `RA ≈ L`. Put a filter on each "
                  "level and the lookup consults memory first: on the level that holds "
                  "the key it goes to disk as before, and on each of the other `L − 1` "
                  "levels it goes to disk only on a false positive. So the expected "
                  "probes are `1 + (L − 1)p`, which at `L = 5` and `p = 1/100` is "
                  "`26/25 = 1.0400` — and that figure is exact, because `p` is a target "
                  "you chose and `L` is a count."),
            ("p", "Choosing `p` is choosing how many of the `L − 1` useless probes you "
                  "are willing to keep. One in ten leaves `1.40` probes at `4.79` bits a "
                  "key; one in a hundred leaves `1.04` at `9.59`; one in a thousand "
                  "leaves `1.004` at `14.38`. The cost is linear in the digits of `1/p` "
                  "and the benefit falls off a cliff after the first few, which is why "
                  "most engines sit at one per cent and stop."),
            ("p", "And a filter is only worth anything to a workload that asks for keys "
                  "that are not there. A lookup that hits still reads the level holding "
                  "its key, and the filter saved it nothing. What `1.20 GB` bought over a "
                  "billion keys was four probes out of five on <em>misses</em>, so the "
                  "value of the filter is proportional to the miss rate — which is a "
                  "property of the workload and has to be measured, not assumed."),
        ],
        "lab": ("storage", {
            "mode": "bloom",
            "panel_title": "Set the keys, the target rate and the levels",
            "panel_intro": (
                "Bits a key is `log₂(1/p)/ln 2`, computed in the browser at the target you "
                "choose, with the textbook `1.44` form printed beside it and the exact "
                "false-positive rate evaluated at a size where an exact fraction still "
                "exists. Move the key count across two decades and watch the bits-per-key "
                "column refuse to move."
            ),
        }),
        "steps_title": "Sizing a filter",
        "steps_intro": "Five lines, and the last of them is the one that keeps the page honest.",
        "steps": [
            ("Choose `p` before you look at `n`",
             "The false-positive rate is the decision; the key count only scales the "
             "answer. Ask what fraction of useless disk reads you are willing to keep, "
             "and convert that into a target — one in a hundred, one in a thousand."),
            ("Read the bits a key off `log₂(1/p)/ln 2`",
             "One per cent is `9.5851`, one in a thousand is `14.3776`. Each extra factor "
             "of ten in `1/p` costs the same `4.79` bits a key, because the formula is a "
             "logarithm — so the cost is linear in the number of nines."),
            ("Multiply by `n` and convert to bytes",
             "`m = n × bits a key`, then divide by eight. A billion keys at one per cent "
             "is `9 585 058 378` bits, which is `1.20 GB` of memory that has to be "
             "resident or the filter has bought nothing."),
            ("Compute the read amplification the filter leaves",
             "`1 + (L − 1)p`. This is the number the filter was for, and it is exact: `p` "
             "is the target and `L` is a count, so no rounding enters it."),
            ("Say which of your figures are rounded",
             "The bits a key, the filter size, the memory and the hash count all come "
             "from the approximation to the false-positive rate. The read amplification "
             "does not. Reporting them without that distinction is how a page ends up "
             "asserting `9.57` as though it were exact."),
        ],
        "worked": {
            "title": "A billion keys at a one per cent false-positive rate, over five levels",
            "intro": [
                "The sizing, the constant that is usually got wrong, and the probes the "
                "filter removes."
            ],
            "lines": [
                "target p = 1/100        log₂(1/p) = log₂(100) = 6.643856…",
                "",
                "bits a key      6.643856 / ln 2 = 6.643856 / 0.693147   =   9.5851   rounded",
                "textbook form   1.44 × 6.643856                         =   9.5672   rounded",
                "difference                                                  0.0179 bits a key",
                "                                        over 10⁹ keys           ≈ 2.2 MB",
                "",
                "n = 10⁹         m = 9 585 058 378 bits",
                "                m / 8 ≈ 1 198 132 297 B                 =   1.20 GB",
                "                k                                       =   7 hash functions",
                "",
                "read amplification, 5 levels, no filters                =   5     probes on a miss",
                "read amplification, a filter on every level",
                "                1 + (5 − 1)(1/100)  =  26/25            =   1.0400   exact",
            ],
            "after": [
                "The `1.0400` is exact and nothing else on the page is. `p` is the target "
                "you chose and `L` is a count of levels, so `1 + (L − 1)p` is arithmetic "
                "on two exact inputs. The bits a key, the filter size, the memory and the "
                "hash count all descend from the approximation to the false-positive "
                "rate, and the lab marks each of them.",
                "A gigabyte and a fifth of memory to remove four probes out of five from "
                "every miss in a billion-key store is the trade this page exists to "
                "price. Whether it is worth paying is a question about how many of your "
                "lookups are misses: a workload that only ever asks for keys that exist "
                "gets nothing from a filter at all.",
                "For a faded rehearsal, keep `n = 10⁹` and the five levels and move the "
                "target to one in a thousand. The supplied first move is that "
                "`log₂(1000) = 9.9658`. Compute the bits a key and the memory, state the "
                "read amplification, and then say what the extra `600 MB` actually "
                "bought relative to one per cent. Check all three in the lab before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "Sizing, and what a filter promises",
        "quiz": [
            {"q": "A filter is sized for `10⁹` keys at `p = 1/100`. The key count doubles and the target is unchanged. What happens to the bits per key?",
             "a": ["They double, to about `19.2`",
                   "They are unchanged at about `9.585`, and the filter's memory doubles",
                   "They halve, because the array is shared across more keys",
                   "They rise slowly, as `log₂ n`"],
             "c": 1,
             "why": "`log₂(1/p)/ln 2` contains no `n`. Doubling the keys doubles `m` and "
                    "leaves `m/n` exactly where it was, so the memory goes from `1.20 GB` "
                    "to `2.40 GB` at `9.5851` bits a key throughout. `19.2` is the bits a "
                    "key for `p = 1/10 000`, which is a different question."},
            {"q": "A Bloom filter reports that a key is absent. What can you conclude?",
             "a": ["That it is probably absent, with probability `1 − p`",
                   "That it is certainly absent — the error is one-sided",
                   "That it is absent from this level but may be on another",
                   "Nothing definite; both answers carry error"],
             "c": 1,
             "why": "A clear bit is only ever clear because no inserted key hashed to it, "
                    "so a single clear position proves the key was never inserted. The "
                    "error is one-sided: the filter can waste a read and cannot lose one. "
                    "It does describe only the set it was built over — one level's filter "
                    "says nothing about another level — but about that set its “no” is "
                    "certain."},
            {"q": "Where does the familiar figure of `9.57` bits a key at one per cent come from?",
             "a": ["From the exact false-positive formula, rather than the approximation",
                   "From writing the constant as `1.44` instead of `1/ln 2 = 1.4427`",
                   "From rounding `9.585` down to three significant figures",
                   "From a different optimal `k`"],
             "c": 1,
             "why": "`1.44 × log₂(100) = 9.5672` and "
                    "`log₂(100)/ln 2 = 9.5851`. Both come from the same approximation to "
                    "the rate; they differ only in how many digits of `1/ln 2` were "
                    "carried. Rounding `9.585` to three figures gives `9.59`, not `9.57`."},
            {"q": "A levelled tree has `L = 5` levels and a filter on each at `p = 1/100`. What is the expected read amplification?",
             "a": ["`5`, unchanged; the filters only save time, not probes",
                   "`1.04`", "`0.05`", "`1.00` — a filter removes every useless probe"],
             "c": 1,
             "why": "`1 + (L − 1)p = 1 + 4(1/100) = 26/25 = 1.04`. The lookup still reads "
                    "the one level that holds the key, and on each of the other four it "
                    "goes to disk only on a false positive. It cannot be `1.00`, because "
                    "`p` is not zero, and it cannot be below `1`, because the real read "
                    "still has to happen."},
        ],
        "mistakes": [
            ("Believing a filter can wrongly say no",
             "It cannot. A “no” means some position was clear, and a clear position means "
             "no inserted key ever hashed there. Readers who expect symmetric error then "
             "design a fallback that re-reads on a negative, which throws away the entire "
             "benefit — the point of a one-sided error is that one of the two answers can "
             "be trusted absolutely and acted on without checking."),
            ("Sizing a filter from bytes rather than keys",
             "A filter holds keys; the size of the values they point at is irrelevant to "
             "it. A billion keys at one per cent costs `1.20 GB` whether the rows are "
             "`100 B` or `10 kB`. Sizing from the dataset's bytes gives an answer that is "
             "wrong by whatever the row width happens to be and moves when the row width "
             "moves."),
            ("Quoting `9.57` bits a key as exact",
             "It is the two-digit constant's answer to an approximate formula, and the "
             "approximation is itself optimistic — at `m = 64`, `n = 8`, `k = 5` it gives "
             "`0.02167922` where the exact rate is `0.02230073`. Any page that prints a "
             "bits-per-key figure owes the reader the words “approximately”, and the "
             "reason."),
        ],
        "standard": ("Finish when a filter's size is a question about `p` and not about the data.",
                     "You should be able to turn a target false-positive rate into bits a "
                     "key and total memory for a stated key count, compute the read "
                     "amplification a filter per level leaves, and say which of those "
                     "figures are rounded and which are exact."),
        "note": (
            "A filter buys one amplification back with memory, which is the shape of the "
            "bargain this whole course is named after. “The RUM Trade-off” computes the "
            "read, update and memory amplifications of three engine shapes at once and "
            "shows that no setting of anything minimises all three."
        ),
    },
]
