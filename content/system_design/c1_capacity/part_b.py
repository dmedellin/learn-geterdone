"""Course 1, lessons 06-10 - the latency ladder, the peak, the machine count, memory, and the check."""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "latency-numbers-on-a-log-scale",
        "title": "Latency Numbers on a Log Scale",
        "module": "Scale and shape",
        "one_line": "Read the exact ratio between two operations off a logarithmic ruler and state which decade it falls in.",
        "summary": (
            "The operations a system is built out of &mdash; a cache reference, a "
            "memory read, an SSD read, a disk seek, a packet crossing a continent "
            "&mdash; span a hundred and fifty million to one. No linear picture "
            "holds that, which is why every version of this table is drawn on a "
            "ratio scale. What is worth carrying away is not the individual figures, "
            "which drift with the hardware, but the ratios between them, which decide "
            "designs and do not."
        ),
        "key": [
            "L1 cache reference                         1 ns",
            "main memory reference                    100 ns",
            "SSD random read                      150 000 ns",
            "disk seek                         10 000 000 ns",
            "California ↔ Netherlands and back 150 000 000 ns",
            "",
            "disk seek / memory reference = 100 000       10⁵ ≤ ratio < 10⁶",
            "the whole ruler, end to end  = 150 000 000×",
        ],
        "key_label": "Five rungs, and the ratio the lesson is about",
        "concepts_intro": (
            "One quantity carries the lesson: how many memory references fit inside "
            "one disk seek. The scale and the bracket are the two things needed to "
            "state it in a form that survives."
        ),
        "concepts": [
            ("One disk seek is a hundred thousand memory references",
             "A memory reference is about `100 ns` and a disk seek about "
             "`10 000 000 ns`, so the ratio is `100 000` exactly &mdash; a quotient "
             "of two integers, not a rounded decimal. That single figure decides more "
             "design arguments than any other number on this course: it is why an "
             "index is worth building, why a cache is worth having, and why "
             "&ldquo;just read it from disk&rdquo; and &ldquo;just read it from "
             "memory&rdquo; are not variations on one plan."),
            ("Only a ratio scale holds a range this wide",
             "From `1 ns` to `150 000 000 ns` is a hundred and fifty million to one. "
             "Drawn linearly, every rung below the top decade lands on top of every "
             "other at the left edge, and the picture says only that the last one is "
             "large. On a logarithmic ruler a factor of ten is the same distance "
             "everywhere, so the gaps between rungs become readable &mdash; and the "
             "gaps are the content."),
            ("The ratios outlive the numbers",
             "Every absolute figure here is a measurement on particular hardware and "
             "will be wrong within a few years; the ratios move far more slowly, and "
             "they are what a design decision actually turns on. So the durable form "
             "is the decade bracket: &ldquo;a disk seek is between `10⁵` and `10⁶` "
             "memory references&rdquo; is a sentence still worth saying when both "
             "figures have changed."),
        ],
        "read_title": "A ladder of reference latencies, and the ratios between its rungs",
        "read_intro": "Where the rungs come from, why the ruler is logarithmic, and what a linear intuition does to the ones near the bottom.",
        "body": [
            ("def", ("Reference latency",
                     "A <strong>reference latency</strong> is a measured figure for "
                     "one elementary operation &mdash; a cache hit, a memory "
                     "reference, a disk seek, a network round trip &mdash; quoted to "
                     "one significant figure and used for estimating. It is data "
                     "rather than a derived quantity: the lab prints every rung in "
                     "full, and the only thing computed from them is the ratio "
                     "between two.")),
            ("math", [
                "L1 cache reference                             1 ns",
                "branch mispredict                              3 ns",
                "L2 cache reference                             4 ns",
                "mutex lock and unlock                         17 ns",
                "main memory reference                        100 ns",
                "compress 1 kB                              2 000 ns",
                "send 1 kB over a 1 Gbit/s link            10 000 ns",
                "SSD random read                          150 000 ns",
                "read 1 MB sequentially from memory       250 000 ns",
                "round trip inside one datacentre         500 000 ns",
                "read 1 MB sequentially from SSD        1 000 000 ns",
                "disk seek                             10 000 000 ns",
                "read 1 MB sequentially from disk      20 000 000 ns",
                "packet California to the Netherlands 150 000 000 ns",
            ]),
            ("p", "Both ends of any ratio taken from that table are integers, so "
                  "the ratio is exact. That matters more than it looks: a reader who "
                  "is handed `99 999.99999` cannot tell it from a wrong answer, "
                  "while `100 000` is obviously the number the lesson is about. The "
                  "only rounded thing in the lab is where each bar is drawn, which "
                  "goes through a logarithm and is a fact about pixels."),
            ("example", ("Memory against a disk seek",
                         "`10 000 000 ns ÷ 100 ns = 100 000`. A hundred thousand "
                         "memory references fit inside one disk seek, and the ratio "
                         "sits between `10⁵` and `10⁶`. Said the other way round: if "
                         "a memory reference took a second, a disk seek would take "
                         "rather more than a day.")),
            ("h3", "Why the ruler is logarithmic"),
            ("p", "Because the alternative shows nothing. Drawn to a linear scale "
                  "reaching `150 000 000 ns`, the memory reference at `100 ns` is "
                  "less than one millionth of the width of the picture, and so is "
                  "everything faster than it. Eleven of the fourteen rungs are crowded "
                  "into the leftmost few percent of it. The picture would be honest "
                  "about the largest "
                  "number and silent about every comparison worth making."),
            ("p", "A logarithmic ruler puts equal ratios at equal distances: the gap "
                  "from `1` to `10` is the same as the gap from `10⁶` to `10⁷`. That "
                  "is the right scale for this table precisely because the questions "
                  "asked of it are ratio questions &mdash; how many of these fit in "
                  "one of those &mdash; and never difference questions."),
            ("h3", "“Disk is somewhat slower than SSD”"),
            ("p", "That sentence is true of one comparison and badly wrong about "
                  "the others, and which one a person has in mind is usually not "
                  "stated. Reading a megabyte sequentially is `20 000 000 ns` from "
                  "disk and `1 000 000 ns` from SSD, a ratio of `20`: somewhat "
                  "slower, fairly described. A disk seek against an SSD random read "
                  "is `10 000 000` against `150 000`, a ratio of `200/3`. And a disk "
                  "seek against a memory reference is `100 000`. Same two words, "
                  "three answers, three different decisions."),
            ("p", "The pattern is that sequential work narrows the gaps and random "
                  "work widens them, which is a preview of an argument &ldquo;Storage "
                  "Engines and Indexes&rdquo; makes at length. Here the useful habit "
                  "is smaller: before saying one thing is slower than another, name "
                  "which operation on each, then take the ratio."),
            ("h3", "Carrying it around"),
            ("p", "Two forms are worth keeping. The first is a handful of exact "
                  "ratios: `100 000` memory references to a disk seek, `300` "
                  "datacentre round trips to a cross-continent one, `20` sequential "
                  "megabytes from SSD to one from disk. The second is the decade "
                  "bracket for anything else &mdash; `10⁵ ≤ r < 10⁶` &mdash; which is "
                  "what the lab prints beside every ratio and is the form that "
                  "survives new hardware."),
            ("p", "What these numbers are not is a model of a running system. They "
                  "are single operations measured in isolation, with nothing queued "
                  "behind them and nothing contending for the same device. A real "
                  "disk seek under load takes longer than the figure above, and by "
                  "how much is the subject of &ldquo;Queues and Utilisation&rdquo;. "
                  "The ladder is a floor and a set of ratios, and it is honest about "
                  "being only that."),
        ],
        "lab": ("estimate", {
            "mode": "scale",
            "preset": "ram-vs-disk",
            "panel_title": "Pick two operations and read the ratio between them",
            "panel_intro": "Every rung is drawn on a logarithmic ruler and every "
                           "ratio is a quotient of two integers, printed exactly with "
                           "its decade bracket beside it. Try the pairs the phrase "
                           "&ldquo;somewhat slower&rdquo; is usually applied to, and "
                           "compare what they actually come to.",
        }),
        "steps_title": "Comparing two operations honestly",
        "steps_intro": "Name both operations, take the quotient, keep the bracket.",
        "steps": [
            ("Name the operation, not the device",
             "&ldquo;Disk&rdquo; is not an operation: a seek and a sequential "
             "megabyte differ by a factor of two on the same device and by far more "
             "against anything else. Almost every confused latency argument is two "
             "people comparing different operations and each assuming the other "
             "meant theirs."),
            ("Divide the slower by the faster and keep it whole",
             "The answer is &ldquo;how many of the faster fit inside one of the "
             "slower&rdquo;, which is the form the number gets used in. Both figures "
             "are integers, so keep the quotient exact rather than turning it into a "
             "decimal that has to be trusted."),
            ("Round to the decade bracket before quoting it",
             "`10⁵ ≤ r < 10⁶` is the durable statement; the mantissa is not. A "
             "bracket stays true across a hardware generation and a three-digit "
             "ratio does not, and quoting the second suggests a precision the "
             "reference figures never had."),
            ("Turn the ratio into the design question",
             "A factor of `100 000` says an index or a cache pays for itself many "
             "times over; a factor of `20` says the same choice is worth arguing "
             "about. The ratio is not the conclusion, but it is what tells you "
             "whether the conclusion needs thought or is already obvious."),
        ],
        "worked": {
            "title": "Three comparisons that all get called “somewhat slower”",
            "intro": [
                "The same two devices, three pairs of operations, and three ratios "
                "that do not support the same sentence."
            ],
            "lines": [
                "1 MB sequentially                disk  20 000 000 ns",
                "                                 SSD    1 000 000 ns",
                "                                 ratio         20      10¹ ≤ r < 10²",
                "",
                "random access                    disk seek   10 000 000 ns",
                "                                 SSD read       150 000 ns",
                "                                 ratio            200/3  ≈ 66.67",
                "                                                        10¹ ≤ r < 10²",
                "",
                "disk seek against memory         disk seek   10 000 000 ns",
                "                                 RAM               100 ns",
                "                                 ratio         100 000      10⁵ ≤ r < 10⁶",
                "",
                "one datacentre round trip            500 000 ns",
                "California ↔ Netherlands         150 000 000 ns",
                "                                 ratio    300            10² ≤ r < 10³",
            ],
            "after": [
                "The first two ratios share a decade bracket and the third is four "
                "brackets away. That is the whole reason to insist on naming the "
                "operation: the first two comparisons are arguments about cost and "
                "the third is not an argument at all.",
                "`300` datacentre round trips in one cross-continent round trip is "
                "the other figure worth keeping, because it is the one that makes "
                "geography a design input rather than a deployment detail. "
                "&ldquo;Latency and the Tail&rdquo; starts from exactly that number.",
                "For a faded rehearsal, pick two rungs whose ratio you think you "
                "know &mdash; sending a kilobyte over a gigabit link against "
                "compressing a kilobyte, say &mdash; and write down your guess, the "
                "decade bracket you expect, and the design sentence you would base "
                "on it. Then select both in the lab. The exercise is worth doing on "
                "the pairs you are confident about.",
            ],
        },
        "quiz_title": "Rungs and ratios",
        "quiz": [
            {"q": "A memory reference is `100 ns` and a disk seek is `10 000 000 ns`. How many memory references fit inside one disk seek?",
             "a": ["`1 000`", "`10 000`", "`100 000`", "`10 000 000`"],
             "c": 2,
             "why": "`10 000 000 / 100 = 100 000`, exactly, and the ratio sits "
                    "between `10⁵` and `10⁶`. `10 000 000` is the seek itself in "
                    "nanoseconds rather than a ratio &mdash; the commonest slip here "
                    "is to quote one of the two figures instead of the quotient. "
                    "`1 000` and `10 000` are the answer with one or two decades "
                    "dropped, which is what happens when the division is done from "
                    "memory rather than on the page."},
            {"q": "Which comparison best supports the sentence “disk is somewhat slower than SSD”?",
             "a": ["A disk seek against an SSD random read, a ratio of `200/3`",
                   "Reading 1 MB sequentially from each, a ratio of `20`",
                   "A disk seek against a memory reference, a ratio of `100 000`",
                   "None of them: the ratios are all in the same decade"],
             "c": 1,
             "why": "A factor of `20` for the same sequential operation is fairly "
                    "described as somewhat slower. `200/3` &mdash; about sixty-seven "
                    "&mdash; is a different claim in the same decade bracket but at "
                    "the far end of it, and it is about random access rather than "
                    "sequential. The third comparison does not involve an SSD at "
                    "all. The ratios are not all in one decade: `100 000` is four "
                    "brackets from the other two."},
            {"q": "Why does this lesson insist on the decade bracket rather than the exact ratio?",
             "a": ["Because the exact ratio is irrational and has to be rounded",
                   "Because the reference latencies are measurements that drift, while the bracket survives them",
                   "Because a logarithmic scale cannot represent an exact value",
                   "Because the bracket is easier to compute than the quotient"],
             "c": 1,
             "why": "Both rungs are integers, so the ratio is exact and the lab "
                    "prints it as one &mdash; nothing here is irrational and nothing "
                    "forces a rounding. The bracket is preferred because the inputs "
                    "are hardware measurements with a shelf life: the absolute "
                    "figures change and the order of magnitude between them mostly "
                    "does not. Quoting three digits claims a precision the reference "
                    "figures never had."},
        ],
        "mistakes": [
            ("Reading the ladder with a linear intuition",
             "&ldquo;Disk is somewhat slower than SSD, and SSD is somewhat slower "
             "than memory&rdquo; chains two vague comparisons into a picture in "
             "which everything is within reach of everything else. A disk seek is "
             "`100 000` memory references. The phrase survives because a linear "
             "ruler piles every rung below the top decade at the same place, and the "
             "picture in most people&rsquo;s heads is linear."),
            ("Memorising the figures rather than the ratios",
             "`100 ns` for a memory reference is a measurement on particular "
             "hardware and will be wrong before long; the fact that a disk seek is "
             "about `10⁵` of them will still be usable. Someone who has learnt the "
             "column of numbers has learnt the part with the shorter shelf life, and "
             "&mdash; worse &mdash; has no way to tell when it has expired, because "
             "the ratios that would have flagged it were never the thing being "
             "remembered."),
            ("Thinking the log scale is softening the comparison",
             "A logarithmic axis looks gentle, and it is easy to read the picture as "
             "a presentational kindness that hides how bad disk really is. It is the "
             "opposite: the log ruler is the only one on which all fourteen rungs "
             "are visible at once, and the linear ruler is the one that hides "
             "things, by crowding eleven of them into its left-hand edge. The ratio printed "
             "beneath the bars is exact, and it is what the picture is claiming."),
        ],
        "standard": ("Finish when “slower” without a named operation and a ratio reads as an incomplete claim.",
                     "You should be able to state the memory-to-disk-seek ratio and "
                     "its bracket from memory, produce any other pair&rsquo;s ratio "
                     "off the ladder, say why the ruler has to be logarithmic, and "
                     "explain what these figures leave out about a system under "
                     "load."),
        "note": "The ladder is about one operation at a time. The other quantity this course needs before it can count machines is about a whole day at a time: &ldquo;Peak to Average&rdquo; asks what a daily profile does to a rate, computes the multiplier between the busiest hour and the mean one from twenty-four buckets rather than from a rule of thumb, and names the number you must not size to.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "peak-to-average",
        "title": "Peak to Average",
        "module": "Scale and shape",
        "one_line": "Compute peak and mean request rates from a 24-bucket daily profile and report the provisioning multiplier between them.",
        "summary": (
            "A daily total divided by `86 400` is a real number about a system and "
            "it is not the number to build for. Traffic has a shape, and the ratio "
            "between the busiest hour and the average one is a property of that "
            "shape: flat for an internal service, a factor of two or three for a "
            "consumer app with an evening, far more for anything driven by a "
            "broadcast. You pay for the mean and you build for the peak, and nothing "
            "but the profile says how far apart they are."
        ),
        "key": [
            "mean rps  =  daily total / 86 400",
            "peak rps  =  busiest bucket / 3 600",
            "peak/mean =  24 · busiest bucket / daily total     two integers",
            "",
            "456 000 000 req/day, busiest hour 46 000 000 at 21:00",
            "   mean   5 277.78 req/s      peak  12 777.78 req/s",
            "   ratio  46/19 = 2.421×      short by 7 500 req/s at the peak",
        ],
        "key_label": "Peak, mean, and the multiplier between them",
        "concepts_intro": (
            "One hard idea: the provisioning multiplier is measured, not assumed. "
            "The other two concepts are what it is measured from and what happens "
            "when it is assumed instead."
        ),
        "concepts": [
            ("You pay for the mean and you build for the peak",
             "The bill over a day is set by the total, which is the mean rate times "
             "`86 400`. Whether the system stays up is set by the busiest hour. "
             "Those are different numbers about the same day &mdash; here "
             "`5 277.78` and `12 777.78` requests a second &mdash; and confusing "
             "them produces a system that is correctly sized for a day that never "
             "happens."),
            ("The multiplier comes out of the profile",
             "Peak over mean is `24` times the busiest bucket over the day&rsquo;s "
             "total: two integers, and no rule of thumb anywhere in it. A consumer "
             "app with one evening peak gives `46/19`, about `2.421×`. Flatten the "
             "same day completely and the ratio is exactly `1`. A broadcast where a "
             "single hour carries the day gives `26/3`, about `8.667×`. The number "
             "is a fact about the traffic and it has to be looked up."),
            ("Sizing to the mean is short by the difference, every day",
             "At `5 277.78` a second of capacity against a peak of `12 777.78`, the "
             "shortfall is `7 500` requests a second &mdash; not occasionally, but "
             "for an hour every day, at the hour that matters most. The failure is "
             "predictable and dated, which is what distinguishes it from the kind of "
             "overload that arrives as a surprise."),
        ],
        "read_title": "A day with a shape, and the two rates you can read off it",
        "read_intro": "What a profile is, how the peak and the mean come out of it, and what the ratio between them is a fact about.",
        "body": [
            ("def", ("Daily profile",
                     "A <strong>daily profile</strong> is the request count in each "
                     "of the twenty-four hours of a day. Its <strong>mean rate</strong> "
                     "is the daily total over `86 400` seconds; its "
                     "<strong>peak rate</strong> is the busiest bucket over `3 600` "
                     "seconds. The <strong>provisioning multiplier</strong> is the "
                     "ratio of the two.")),
            ("p", "Both rates are computed from the same twenty-four numbers and "
                  "neither is more real than the other. The mean is what the day "
                  "cost; the peak is what the day required. A capacity estimate that "
                  "reports one without the other has answered half a question, and "
                  "usually the half that does not determine whether the system works."),
            ("math", [
                "daily total                    456 000 000   req/day",
                "÷ 86 400 s/day                                   mean   5 277.78 req/s",
                "",
                "busiest bucket (21:00)          46 000 000   req/hour",
                "÷ 3 600 s/hour                                   peak  12 777.78 req/s",
                "",
                "peak / mean   =  24 · 46 000 000 / 456 000 000  =  46/19  =  2.421×",
                "shortfall     =  12 777.78 − 5 277.78           =  7 500  req/s",
            ]),
            ("p", "The middle line is worth dwelling on. Peak over mean is "
                  "`24 · peak bucket / daily total` &mdash; both ends integers, so "
                  "the multiplier is an exact fraction and is completely independent "
                  "of how big the day is. Double every bucket and the ratio does not "
                  "move; change the shape of the day and it does. The multiplier is "
                  "a statement about shape and nothing else."),
            ("example", ("A consumer app with an evening",
                         "Twenty-four buckets rising to `46 000 000` requests at "
                         "`21:00` and falling to `10 000 000` in the quiet hours; "
                         "`456 000 000` requests over the day. The mean is "
                         "`5 277.78` a second, the peak is `12 777.78`, and the "
                         "multiplier is `46/19`. Anyone who sized this system from "
                         "the daily total alone has built for `5 277.78` and will be "
                         "`7 500` requests a second short every evening.")),
            ("h3", "Two point four is not a rule"),
            ("p", "It is this profile&rsquo;s answer. Flatten the shape in the lab "
                  "&mdash; an internal service with no daily rhythm &mdash; and the "
                  "multiplier falls to exactly `1`, because the peak bucket is the "
                  "mean bucket. Switch to the broadcast example, where one hour "
                  "carries the day, and it rises to `26/3`, about `8.667×`. Three "
                  "systems, one arithmetic, multipliers an order of magnitude apart."),
            ("p", "So the estimate to distrust is the one that says &ldquo;call it "
                  "`2×` for peak&rdquo;. The multiplier is one of the few figures on "
                  "this course that can be measured directly and cheaply from data "
                  "the system already produces, and a measured one collapses a "
                  "factor that would otherwise be carried as a ranged guess all the "
                  "way to the machine count."),
            ("h3", "What an hourly bucket cannot see"),
            ("p", "The peak this profile reports is the busiest <em>hour</em>, "
                  "which is itself an average over `3 600` seconds. A five-minute "
                  "burst inside that hour is flattened by the bucket and does not "
                  "appear. So the multiplier computed here is a lower bound on the "
                  "one a finer profile would give: bucket the same day by minute and "
                  "the peak can only rise or stay the same, never fall."),
            ("p", "That is the assumption to say out loud whenever this number is "
                  "quoted. &ldquo;Peak over mean is `2.421`, measured hourly&rdquo; "
                  "is a complete statement; without the last two words it is a claim "
                  "about a resolution nobody chose deliberately. Where the burstiness "
                  "inside a bucket is the thing that matters, the tools are in "
                  "&ldquo;Queues and Utilisation&rdquo; &mdash; this lesson is about "
                  "the shape of the day, not the shape of a minute."),
            ("p", "One more thing the profile does not carry: the read/write mix "
                  "moves with it. A daily ratio of `100:1` can be a different ratio "
                  "in the busiest hour, and the rates that get sized are the "
                  "peak-hour ones. If the profile is being measured anyway, it costs "
                  "nothing to bucket the two request kinds separately and find out."),
        ],
        "lab": ("estimate", {
            "mode": "peak",
            "preset": "consumer-evening",
            "panel_title": "Shape the day, then read the multiplier",
            "panel_intro": "Move the busy period, change how pronounced it is, or "
                           "reshape a single hour by hand. Peak, mean and the exact "
                           "ratio between them redraw with every change &mdash; and "
                           "scaling the whole day up or down leaves the ratio exactly "
                           "where it was.",
        }),
        "steps_title": "Getting a provisioning multiplier from traffic",
        "steps_intro": "Bucket the day, take both rates, divide, and say what resolution you used.",
        "steps": [
            ("Bucket a real day rather than reasoning about one",
             "Twenty-four counts from a log or a metric is usually an afternoon of "
             "work and removes a factor from the estimate that would otherwise be "
             "guessed. It is also the one input on this course that a running system "
             "will simply hand you."),
            ("Compute the mean, and label it as what you pay for",
             "Daily total over `86 400`. Write &ldquo;mean&rdquo; next to it, not "
             "&ldquo;the rate&rdquo;. Most of the damage this lesson is about comes "
             "from a figure that was correctly computed and then carried forward "
             "under a name that does not say which rate it is."),
            ("Compute the peak from the busiest bucket",
             "Busiest bucket over `3 600`. This is the figure that goes into "
             "&ldquo;From a Request&rsquo;s Cost to a Machine Count&rdquo;, and it "
             "is the only one of the two that decides whether the system stands up."),
            ("Divide, and keep the ratio as the transferable part",
             "`24 · peak bucket / daily total`. The multiplier is independent of the "
             "size of the day, so it stays valid as the system grows and can be "
             "applied to a forecast total years later, which the two rates cannot."),
            ("State the bucket width alongside the number",
             "An hourly peak is an hourly average, and a finer bucket can only raise "
             "it. Quoting the multiplier with its resolution is what keeps it from "
             "being read as a hard ceiling on demand."),
        ],
        "worked": {
            "title": "456 million requests a day, with an evening peak at 21:00",
            "intro": [
                "One day, twenty-four buckets, and the three figures that come out "
                "of them."
            ],
            "lines": [
                "quietest hours        10 000 000 req      rising from 03:00",
                "busiest hour (21:00)  46 000 000 req",
                "daily total          456 000 000 req",
                "",
                "mean rate    456 000 000 / 86 400        =   5 277.78 req/s",
                "peak rate     46 000 000 /  3 600        =  12 777.78 req/s",
                "",
                "multiplier   24 · 46 000 000 / 456 000 000  =  1 104/456",
                "                                            =  46/19  =  2.421×",
                "",
                "sized to the mean, at the peak:",
                "             12 777.78 − 5 277.78         =   7 500 req/s short",
                "                                              for an hour, every day",
                "",
                "same arithmetic, other shapes:",
                "   flat internal service                  =  1×",
                "   broadcast, one hour carries the day    =  26/3 = 8.667×",
            ],
            "after": [
                "The multiplier line is the one that generalises. `46/19` is an "
                "exact fraction of two integers and it does not depend on the size "
                "of the day at all: scale every bucket by ten and it is still "
                "`46/19`. That is what makes it the figure worth recording and "
                "reusing, while the two rates go stale as soon as the system grows.",
                "The shortfall line is the one that makes the case. `7 500` requests "
                "a second is not an outage risk in the abstract; it is a scheduled "
                "one, at a known hour, with the same size every day.",
                "For a faded rehearsal, use the lab&rsquo;s broadcast example. The "
                "supplied first move is that only one bucket is lifted, so the daily "
                "total is `23` quiet hours plus one large one. Predict whether the "
                "multiplier will be nearer `3` or nearer `9` before you look, then "
                "read off the peak, the mean and the ratio &mdash; and say what "
                "sizing that system to its mean would cost.",
            ],
        },
        "quiz_title": "Peaks, means and multipliers",
        "quiz": [
            {"q": "A service takes `456 000 000` requests a day and its busiest hour carries `46 000 000` of them. What is the peak rate?",
             "a": ["`5 277.78 req/s`", "`12 777.78 req/s`", "`46 000 000 req/s`", "`2.421 req/s`"],
             "c": 1,
             "why": "The peak is the busiest bucket spread over its own hour: "
                    "`46 000 000 / 3 600 = 12 777.78` requests a second. `5 277.78` "
                    "is the mean, the daily total over `86 400` &mdash; a real figure "
                    "about the same day and the wrong one to size to. `46 000 000` "
                    "is the bucket itself, which is a count and not a rate. `2.421` "
                    "is the multiplier between the two rates."},
            {"q": "Every bucket in the profile is doubled. What happens to the peak-to-mean multiplier?",
             "a": ["It doubles", "It halves", "It is unchanged", "It depends which hour is busiest"],
             "c": 2,
             "why": "The multiplier is `24 · peak bucket / daily total`, and "
                    "doubling every bucket doubles both. It is a statement about the "
                    "shape of the day and carries no information about its size, "
                    "which is exactly why it is the part worth recording: it stays "
                    "valid as the system grows, while the peak and mean rates do not."},
            {"q": "An hourly profile gives a peak-to-mean of `2.421`. The same day is re-bucketed by the minute. What can be said about the new multiplier?",
             "a": ["It will be the same: the day has not changed",
                   "It can only be the same or larger",
                   "It can only be the same or smaller",
                   "It could be anything; finer buckets are not comparable"],
             "c": 1,
             "why": "The mean is unchanged &mdash; it depends only on the daily "
                    "total &mdash; while the peak is the busiest bucket, and a "
                    "shorter bucket cannot average away less than a longer one. Any "
                    "burst inside the busiest hour shows up at minute resolution and "
                    "was flattened at hourly resolution. So the hourly multiplier is "
                    "a lower bound, which is why the bucket width belongs in the "
                    "quoted figure."},
        ],
        "mistakes": [
            ("Sizing to the daily total over 86 400",
             "It is a correctly computed number and it is the mean, which is the "
             "rate the system experiences at no particular moment. Here it is "
             "`5 277.78` requests a second against a peak of `12 777.78`, so a "
             "fleet built to it is `7 500` requests a second short for an hour every "
             "evening. What makes this mistake so durable is that the figure is "
             "right; only its name is wrong."),
            ("Using a remembered multiplier instead of a measured one",
             "&ldquo;Call it `2×` for peak&rdquo; gets `2.421` roughly right for "
             "one consumer app, gives `1` for a flat internal service and is out by "
             "more than four times for a broadcast at `26/3`. The multiplier is a "
             "fact about a particular day&rsquo;s shape, it is cheap to measure from "
             "data the system already emits, and measuring it removes one of the few "
             "factors in a capacity estimate that does not have to stay a guess."),
            ("Reading the hourly peak as the real peak",
             "The busiest bucket is an average over `3 600` seconds, so a burst "
             "lasting a few minutes inside it has been flattened before the "
             "multiplier was computed. Re-bucket the same day more finely and the "
             "peak can only rise. An hourly figure is therefore a lower bound on the "
             "demand, and quoting it without its resolution turns a floor into an "
             "apparent ceiling."),
        ],
        "standard": ("Finish when a request rate quoted without saying peak or mean reads as ambiguous rather than adequate.",
                     "You should be able to take twenty-four bucket counts to a "
                     "mean, a peak and an exact multiplier, say why the multiplier is "
                     "independent of the size of the day, state the shortfall that "
                     "sizing to the mean would produce, and name the resolution your "
                     "peak was measured at."),
        "note": "The peak is now a number, and a number of requests per second is one input short of a fleet. &ldquo;From a Request&rsquo;s Cost to a Machine Count&rdquo; supplies the other two &mdash; what one request costs and how full you are willing to run &mdash; and turns all three into an integer, which is the first answer on this course that cannot be a range.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "from-request-cost-to-machine-count",
        "title": "From a Request's Cost to a Machine Count",
        "module": "Machines and memory",
        "one_line": "Produce an integer machine count from a peak rate, a per-request cost and a stated target utilisation, and say what the headroom is for.",
        "summary": (
            "A machine&rsquo;s capacity is one over what a request costs it, and the "
            "fleet is the peak divided by the capacity you are willing to use. Two "
            "things make this more than a division. The answer is a ceiling, because "
            "machines are integers and most of a machine will not serve anything. "
            "And the utilisation you divide by is a decision that has to be named: "
            "at `60%` the fleet here is `167` machines, at `100%` it is `100`, and "
            "the difference is not a rounding."
        ),
        "key": [
            "capacity  =  1 / (resource per request)",
            "          =  8 cores · 1000 ms/s / 40 ms  =  200 req/s per machine",
            "usable    =  capacity · ρ_target          =  200 · 0.6 = 120 req/s",
            "N         =  ⌈peak / usable⌉  =  ⌈20 000/120⌉ = ⌈500/3⌉ = 167",
            "",
            "at N = 167 the peak sits at 100/167 = 59.88% of the fleet",
            "sized at ρ = 1 the same peak would have said N = 100",
        ],
        "key_label": "Capacity, headroom, and the integer that falls out",
        "concepts_intro": (
            "One hard idea, the ceiling, with the two quantities it needs on either "
            "side of it: what a request costs, and how full you are willing to run."
        ),
        "concepts": [
            ("Capacity per machine is one over the cost of a request",
             "A request that occupies one core for `40 ms` lets a machine with `8` "
             "cores serve `8 · 1000/40 = 200` requests a second. The general form is "
             "the same for any resource: capacity is the reciprocal of what one "
             "request consumes, in whatever unit is scarce. Choosing which resource "
             "is scarce is the modelling decision; the arithmetic after that is a "
             "reciprocal."),
            ("N is a ceiling, and the ceiling is the point",
             "`20 000` requests a second over `120` usable gives `500/3` machines, "
             "which is `166.67` and therefore `167`. Machines come in whole numbers, "
             "so the exact fraction is never the answer &mdash; and rounding down "
             "for tidiness gives a fleet that is short at exactly the moment the "
             "peak arrives. The lab draws the staircase so the `2/3` of a machine at "
             "the top of the last tread is visible."),
            ("The headroom is named, and it is not an error bar",
             "`60%` is a decision about how full a queue should be allowed to run, "
             "and it comes from queueing theory rather than from uncertainty about "
             "the inputs. It is taken as given on this course. &ldquo;The Knee: "
             "Response Time vs Utilisation&rdquo; is where it is earned, and the "
             "short version is that response time rises steeply as utilisation "
             "approaches one, so the last `40%` of a machine buys latency you cannot "
             "pay for any other way."),
        ],
        "read_title": "One request, one machine, one fleet",
        "read_intro": "The reciprocal that gives a machine&rsquo;s capacity, the target that reduces it, and the ceiling that turns the quotient into a fleet.",
        "body": [
            ("def", ("Capacity and target utilisation",
                     "The <strong>capacity</strong> of a machine is the reciprocal "
                     "of the scarce resource one request consumes. Its <strong>target "
                     "utilisation</strong> `ρ` is the fraction of that capacity the "
                     "design is willing to use, so <strong>usable capacity</strong> "
                     "is `capacity · ρ`. The <strong>machine count</strong> is "
                     "`N = ⌈peak / (capacity · ρ)⌉`.")),
            ("p", "Every term has to be a peak or none of them can be. The rate "
                  "going in is the peak rate from &ldquo;Peak to Average&rdquo;, not "
                  "the mean; a fleet sized from a mean rate is short for as long as "
                  "the busy period lasts, and no amount of care about the ceiling "
                  "rescues it."),
            ("math", [
                "cores per machine                8",
                "cost of one request             40 ms of one core",
                "capacity     8 · 1000 ms/s / 40 ms          =  200 req/s",
                "",
                "target utilisation ρ            60%",
                "usable       200 · 0.6                      =  120 req/s",
                "",
                "peak rate                    20 000 req/s",
                "machines needed  20 000 / 120 = 500/3       =  166.67",
                "N = ⌈500/3⌉                                 =  167",
                "",
                "fleet capacity   167 · 200                  =  33 400 req/s",
                "the peak sits at 20 000 / 33 400 = 100/167  =  59.88%",
                "spare            33 400 − 20 000            =  13 400 req/s",
            ]),
            ("p", "`59.88%` rather than `60%` is the ceiling showing up in the "
                  "answer: rounding `166.67` up to `167` bought two-thirds of a "
                  "machine that nobody asked for, and the fleet is very slightly "
                  "emptier than the target. That is the normal direction for this "
                  "error to run, and it is the safe one."),
            ("example", ("A checkout API at twenty thousand a second",
                         "Eight cores, `40 ms` of one core per request, `60%` "
                         "target. Each machine serves `200` requests a second and is "
                         "allowed `120`, so the fleet is `167` machines carrying "
                         "`33 400` requests a second of raw capacity, `13 400` of "
                         "which is deliberately unused. Sized at `100%` the same "
                         "peak gives `100` machines, and the sixty-seven machines "
                         "between those two answers are the headroom, priced.")),
            ("h3", "What the sixty-seven machines buy"),
            ("p", "Not insurance against the estimate being wrong. The target "
                  "utilisation is a queueing decision: as utilisation approaches "
                  "one, waiting time rises without bound, and a fleet run at `95%` "
                  "has a latency profile that no amount of extra patience fixes. "
                  "`60%` is a point on that curve, chosen so that the response time "
                  "is tolerable and a machine can be lost without the rest going "
                  "over the knee."),
            ("p", "The uncertainty in the inputs is a separate and multiplicative "
                  "thing. If the peak rate and the per-request cost are each known "
                  "to a factor of two, the ranges from &ldquo;Orders of "
                  "Magnitude&rdquo; put the fleet somewhere across a `÷4 … ×4` "
                  "interval, and the headroom does not begin to cover that. Two "
                  "different questions, two different answers, and conflating them "
                  "produces a fleet that is neither adequately provisioned nor "
                  "honestly estimated."),
            ("h3", "An integer is not a precise answer"),
            ("p", "`167` looks like a hard number and is only as hard as its "
                  "inputs. Halve the per-request cost in the lab and the same peak "
                  "and target give `84`; double it and they give `334`. Nothing "
                  "about the ceiling makes `167` more certain than the `40 ms` it "
                  "came from &mdash; the ceiling removes the fractional part, not "
                  "the range. The honest report names the fleet and the assumption "
                  "that moves it most, which here is the cost of a request."),
            ("h3", "One constraint, and the case with two"),
            ("p", "This is the one-constraint version: the fleet is sized by "
                  "request throughput and by nothing else. Real fleets are often "
                  "held up by a second constraint at the same time &mdash; a data "
                  "volume that will not fit, a connection count, a per-node write "
                  "rate &mdash; and then the answer is the larger of the two "
                  "ceilings rather than either one. &ldquo;How Many Shards&rdquo;, "
                  "on Partitioning and Load Balancing, is that lesson: the same "
                  "ceiling computed twice and a maximum taken. Doing the "
                  "one-constraint case first is worth it, because the trap there is "
                  "always to compute one ceiling and stop."),
        ],
        "lab": ("estimate", {
            "mode": "machines",
            "preset": "checkout-api",
            "panel_title": "Set the peak, the cost of a request and the headroom",
            "panel_intro": "The staircase is `N` against the peak rate, and the "
                           "marker sits partway up a tread &mdash; that gap is the "
                           "capacity the ceiling bought you. Drag the target "
                           "utilisation to `100%` and watch `N` collapse to the "
                           "figure the panel calls &ldquo;N if sized at 100%&rdquo;.",
        }),
        "steps_title": "Turning a peak rate into a fleet",
        "steps_intro": "The scarce resource first, then a reciprocal, then a target, then a ceiling.",
        "steps": [
            ("Decide which resource a request actually consumes",
             "CPU milliseconds, memory, disk I/O, connections &mdash; one of them "
             "runs out first and it is the one to count. Getting this wrong produces "
             "a fleet sized by a resource that was never scarce, and the symptom is "
             "a system that falls over at a fraction of its computed capacity."),
            ("Turn the per-request cost into a per-machine capacity",
             "Capacity is the reciprocal: `cores × 1000 ms/s ÷ cost in ms` for a CPU "
             "bound. Keep the units on the page &mdash; the `1000 ms/s` row is the "
             "one people drop, and dropping it moves the answer by three orders of "
             "magnitude."),
            ("Multiply by the target utilisation, and say where it came from",
             "`ρ = 0.6` is a decision, not a measurement, and it belongs in the "
             "write-up next to the answer. An estimate that reports `N` without "
             "reporting `ρ` cannot be checked by anyone, because the two numbers are "
             "only meaningful together."),
            ("Divide the peak by the usable capacity and take the ceiling",
             "`⌈peak / usable⌉`. Round up always: the fractional machine is doing "
             "real work at the peak, and the alternative is a fleet that is short "
             "for exactly as long as the busy hour lasts."),
            ("Report the fleet with the assumption that moves it most",
             "Say what `N` is, what `ρ` was, and what the per-request cost was &mdash; "
             "and then say what `N` would be if that cost were half or double. The "
             "integer looks exact and inherits every range that went into it."),
        ],
        "worked": {
            "title": "20 000 req/s at 40 ms of one core, 8 cores, 60% target",
            "intro": [
                "Four inputs, one reciprocal, one ceiling, and a comparison against "
                "the answer that skips the headroom."
            ],
            "lines": [
                "peak rate                      20 000 req/s     from the profile",
                "cost of one request               40 ms of one core",
                "cores per machine                  8",
                "target utilisation ρ              60%",
                "",
                "capacity per machine   8 cores × 1000 ms/s / 40 ms   =   200 req/s",
                "usable at the target   200 × 0.6                     =   120 req/s",
                "",
                "machines needed        20 000 / 120  =  500/3         =   166.67",
                "N                      ⌈500/3⌉                        =   167",
                "",
                "fleet raw capacity     167 × 200                      = 33 400 req/s",
                "peak as a fraction     20 000 / 33 400 = 100/167      =  59.88%",
                "spare at the peak      33 400 − 20 000                = 13 400 req/s",
                "",
                "sized at ρ = 1         ⌈20 000 / 200⌉                 =   100",
                "the headroom costs     167 − 100                      =    67 machines",
                "",
                "cost halved to 20 ms   capacity 400, usable 240       =  N = 84",
                "cost doubled to 80 ms  capacity 100, usable  60       =  N = 334",
            ],
            "after": [
                "The two lines at the bottom are the ones that stop `167` from "
                "looking like a measurement. The per-request cost is a ranged factor "
                "like every other input on this course, and a factor of two in it is "
                "very nearly a factor of two in the fleet. The ceiling removed the "
                "fraction; it did not remove the range.",
                "The `59.88%` is worth noticing too. The target was `60%` and the "
                "fleet runs just under it, because the ceiling handed you two-thirds "
                "of a machine you had not asked for. Over-provisioning by a fraction "
                "of a machine is the correct direction for that error, and it is the "
                "direction the ceiling always errs in.",
                "For a faded rehearsal, take the lab&rsquo;s edge-cache example: "
                "`500 000` requests a second, `2 ms` a request, `4` cores, `80%` "
                "target. The supplied first move is the capacity, `4 · 1000/2 = "
                "2 000` requests a second per machine. Produce the usable capacity, "
                "the exact machine count and `N`, then predict what `N` becomes at a "
                "`60%` target before changing the slider.",
            ],
        },
        "quiz_title": "Capacity, headroom and the ceiling",
        "quiz": [
            {"q": "A machine serves `200` requests a second and the target utilisation is `60%`. The peak is `20 000` requests a second. How many machines?",
             "a": ["`100`", "`120`", "`167`", "`166`"],
             "c": 2,
             "why": "Usable capacity is `200 · 0.6 = 120` a second, so the fleet "
                    "needs `20 000/120 = 500/3 = 166.67` machines and `N = 167`. "
                    "`100` is the answer at `100%` utilisation, with the headroom "
                    "dropped. `120` is the usable capacity of one machine, not a "
                    "count. `166` is the quotient rounded the wrong way, which "
                    "leaves the fleet short at exactly the peak it was sized for."},
            {"q": "What is the `60%` target utilisation there for?",
             "a": ["To cover the possibility that the peak rate estimate is too low",
                   "Because response time rises steeply as utilisation approaches one",
                   "To leave room for the fleet to grow next year",
                   "Because a machine cannot physically exceed about 60% of its cores"],
             "c": 1,
             "why": "The target is a queueing decision: waiting time climbs without "
                    "bound as utilisation approaches one, so the unused capacity "
                    "buys a response time that nothing else can. Uncertainty in the "
                    "inputs is a separate, multiplicative thing &mdash; two factors "
                    "known to `±2×` put the fleet across a `÷4 … ×4` interval, which "
                    "`60%` does not begin to cover. Growth is a different "
                    "conversation again, and there is no physical ceiling at `60%`."},
            {"q": "The per-request cost of `40 ms` turns out to be `80 ms`. What happens to `N = 167`?",
             "a": ["It is unchanged: `N` is an integer",
                   "It rises to `334`",
                   "It rises to about `200`",
                   "It cannot be recomputed without remeasuring the peak"],
             "c": 1,
             "why": "Capacity halves to `100` a second and usable capacity to `60`, "
                    "so the fleet is `⌈20 000/60⌉ = ⌈1000/3⌉ = 334`. The ceiling "
                    "removed the fractional part of the answer, not the uncertainty "
                    "in the inputs: `N` is exactly as well known as the per-request "
                    "cost it was computed from, and a factor of two in that cost is "
                    "very nearly a factor of two in the fleet."},
        ],
        "mistakes": [
            ("Sizing the fleet at a hundred percent of capacity",
             "`⌈20 000/200⌉ = 100` machines is arithmetically correct and describes "
             "a fleet with no room for a deploy, a failed machine or a bad "
             "afternoon, running at the part of the queueing curve where response "
             "time climbs fastest. The same peak at a `60%` target needs `167`. The "
             "sixty-seven machines are not waste; they are the latency the design "
             "asked for, and they should be reported as such."),
            ("Treating the headroom as cover for a wrong estimate",
             "The `60%` answers &ldquo;how full should a queue run&rdquo; and the "
             "ranges answer &ldquo;how well do we know the inputs&rdquo;, and they "
             "compose by multiplying rather than one absorbing the other. A peak "
             "known to `±2×` and a cost known to `±2×` put `N` across a `÷4 … ×4` "
             "interval; a target of `60%` covers a factor of well under two. Anyone "
             "relying on the headroom to absorb the estimate has covered neither."),
            ("Reading the integer as a precise answer",
             "`167` is a ceiling of an exact fraction, which makes it exact given "
             "its inputs and no better known than they are. In the lab, halving the "
             "per-request cost gives `84` and doubling it gives `334` &mdash; the "
             "same peak, the same target, three fleets. The ceiling is the last step "
             "of the arithmetic and it is not a promotion from estimate to "
             "measurement."),
        ],
        "standard": ("Finish when a machine count quoted without its target utilisation reads as an unfinished answer.",
                     "You should be able to turn a peak rate, a per-request cost and "
                     "a target into `N` without assistance, say why the answer is a "
                     "ceiling and never a rounding, distinguish the headroom from the "
                     "uncertainty in the inputs, and name what `N` becomes if the "
                     "per-request cost is out by a factor of two."),
        "note": "Machines are counted; memory is not counted the same way. &ldquo;Memory and the Working Set&rdquo; is the last of the four things a rate sizes, and it is the one where the whole dataset is the wrong denominator &mdash; a cache is sized to the fraction of the data the traffic actually touches, and the curve relating that fraction to the hit rate has a knee in it that decides the budget.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "memory-and-the-working-set",
        "title": "Memory and the Working Set",
        "module": "Machines and memory",
        "one_line": "Size a cache in gigabytes for a target hit rate, given a dataset size and a stated hot fraction.",
        "summary": (
            "Nobody buys enough memory for the dataset. Memory is sized to the part "
            "of the data the traffic actually touches, which is usually a small "
            "fraction of it, and the question is not whether the data fits but how "
            "many of the reads do. Given a hot fraction and the share of traffic it "
            "takes, the hit rate is a piecewise-linear function of what you cache "
            "&mdash; with a knee where the hot region runs out, and the knee is where "
            "the budget is decided."
        ),
        "key": [
            "hot fraction f of the data takes share s of the reads",
            "h(c) = s · c/f                   c ≤ f      inside the hot region",
            "h(c) = s + (1−s)(c−f)/(1−f)      c > f      past the knee",
            "",
            "5 TB of timelines, f = 10%, s = 90%:",
            "   h = 80%  needs 4/45 = 8.89% of the data  =  444.44 GB",
            "   the whole hot 10% is 500 GB and buys 9/10",
            "   h = 95%  needs 11/20 = 55%               =  2.75 TB",
        ],
        "key_label": "The hit-rate curve, and what a target costs in gigabytes",
        "concepts_intro": (
            "One hard idea &mdash; the denominator is the working set and not the "
            "dataset &mdash; and then the shape of the curve that idea produces, and "
            "what the curve is a model of."
        ),
        "concepts": [
            ("Size the cache to the working set, not to the dataset",
             "Five terabytes of timelines with a tenth of it taking `90%` of the "
             "reads needs `444.44 GB` of memory for an `80%` hit rate: `4/45` of the "
             "data, `8.89%`. The dataset size sets what caching everything would "
             "cost and is otherwise not the relevant quantity. The question a memory "
             "budget answers is how many reads are served, and reads are not "
             "distributed over the data the way bytes are."),
            ("The curve has a knee, and the price changes at it",
             "Inside the hot region every gigabyte buys the same number of hits, and "
             "outside it every gigabyte buys far fewer. Caching the whole hot `10%` "
             "costs `500 GB` and buys `9/10` of the reads; pushing the target to "
             "`95%` costs `2.75 TB`, because the extra five points have to be bought "
             "out of the cold region at the cold region&rsquo;s price. A target "
             "chosen without looking at the knee is a budget decision made by "
             "accident."),
            ("The hot fraction is stated, and it is a fact about traffic",
             "`10%` of the data taking `90%` of the reads is an input here, measured "
             "over some window, and it moves: a release, an import, a story everyone "
             "reads at once. The model also assumes every key inside each region is "
             "equally popular, which is false in detail and is what makes the curve "
             "two straight lines rather than a smooth one. &ldquo;Cache Size and Hit "
             "Rate&rdquo; replaces the stated fraction with a popularity exponent and "
             "derives the same shape instead of asserting it."),
        ],
        "read_title": "How much memory a target hit rate costs",
        "read_intro": "What a working set is, the two-segment curve a stated skew produces, and where the money goes.",
        "body": [
            ("def", ("Working set",
                     "The <strong>working set</strong> is the portion of the data "
                     "that the traffic touches over a window. A workload with "
                     "<strong>hot fraction</strong> `f` and <strong>hot share</strong> "
                     "`s` has `f` of its bytes taking `s` of its reads; caching a "
                     "fraction `c` of the data gives a <strong>hit rate</strong> "
                     "`h(c)`, and the <strong>memory needed</strong> for a target `h` "
                     "is the dataset times the `c` that reaches it.")),
            ("p", "The two numbers `f` and `s` are what makes caching work at all. "
                  "If reads were spread evenly over the data, caching `c` of it "
                  "would buy `c` of the hits and a cache would be exactly as useful "
                  "as it was large &mdash; which is to say, not useful, because you "
                  "cannot afford a cache the size of the data. Skew is the whole "
                  "business case."),
            ("math", [
                "inside the hot region       c ≤ f",
                "   h(c)  =  s · c/f",
                "",
                "past the knee               c > f",
                "   h(c)  =  s + (1 − s) · (c − f)/(1 − f)",
                "",
                "inverted, for a target h:",
                "   h ≤ s :   c  =  f · h/s",
                "   h > s :   c  =  f + (1 − f) · (h − s)/(1 − s)",
            ]),
            ("p", "Both branches are straight lines and they meet at `(f, s)`, which "
                  "is the knee. The first has slope `s/f` &mdash; here `9`, so each "
                  "point of cached data buys nine points of hit rate &mdash; and the "
                  "second has slope `(1−s)/(1−f)`, here `1/9`. A factor of "
                  "eighty-one between the price of a hit before the knee and after "
                  "it, and it changes at a single point."),
            ("example", ("Five terabytes of timelines, eighty percent wanted",
                         "With `f = 10%` and `s = 90%`, a target of `80%` is inside "
                         "the hot region, so `c = 0.1 · 80/90 = 4/45`, which is "
                         "`8.89%` of the data, or `444.44 GB`. Less than half a "
                         "terabyte of memory serves four reads in five out of a five-"
                         "terabyte store. That ratio &mdash; and not the absolute "
                         "figure &mdash; is why caches exist.")),
            ("h3", "What the last five points cost"),
            ("p", "Caching the entire hot region costs `500 GB` and gives a hit "
                  "rate of `9/10`. Ask for `95%` instead and the memory needed is "
                  "`11/20` of the data, `2.75 TB`. The first ninety points of hit "
                  "rate cost half a terabyte; the next five cost more than four times "
                  "that again, because they are bought from a region where reads are "
                  "spread thinly over a lot of bytes."),
            ("p", "This is the shape of every cache-sizing conversation worth "
                  "having. The target hit rate is a choice, it has a price, and the "
                  "price is wildly non-linear in the target. A team that asks for "
                  "&ldquo;`99%`&rdquo; because it sounds rigorous has usually asked "
                  "for the whole dataset in memory without noticing; a team that "
                  "reads the knee off the curve first asks for a number it can pay "
                  "for."),
            ("h3", "What the model assumes"),
            ("p", "Two things, and both are visible in the shape of the curve. "
                  "Within the hot region every key is equally popular, and within the "
                  "cold region every key is equally popular &mdash; which is what "
                  "makes each branch a straight line, and it is not true of any real "
                  "workload. And the split into two regions is itself a "
                  "simplification of a smooth popularity curve. The model is right "
                  "about the two things this lesson claims &mdash; that a small cache "
                  "buys a large hit rate, and that there is a knee &mdash; and it is "
                  "an approximation about everything else."),
            ("p", "The other assumption is quieter: `f` and `s` were measured over "
                  "some window and are being used as though they were properties of "
                  "the system. They move. The honest report says which window they "
                  "came from, exactly as a read/write ratio does, and treats them as "
                  "ranged factors when they are carried into a product."),
            ("p", "&ldquo;Cache Size and Hit Rate&rdquo;, on Caching and Hit Rates, "
                  "replaces the stated pair with a Zipf popularity exponent, from "
                  "which the same curve is derived rather than asserted &mdash; and "
                  "the knee softens into a genuine curve with diminishing returns "
                  "everywhere. This lesson is the version that can be done on an "
                  "envelope, and it gets the two structural facts right."),
        ],
        "lab": ("estimate", {
            "mode": "workingset",
            "preset": "social-timeline",
            "panel_title": "Set the dataset, the skew and the hit rate you want",
            "panel_intro": "The curve is the hit rate against the fraction of the "
                           "data held in memory, with the knee where the hot region "
                           "runs out. Drag the target past the knee and watch the "
                           "gigabytes needed pull away from the line they were "
                           "following.",
        }),
        "steps_title": "Sizing memory for a target hit rate",
        "steps_intro": "Measure the skew, find the knee, choose the target knowing what it costs.",
        "steps": [
            ("Get the skew from traffic, not from the data",
             "What is wanted is the fraction of keys taking a large share of the "
             "reads over a window &mdash; a question about access logs. Any reasoning "
             "that starts from how the data is distributed has answered a different "
             "question, and a cache sized from it will be sized to the dataset."),
            ("Find the knee before choosing a target",
             "The knee sits at `(f, s)`: caching the hot fraction buys the hot "
               "share, and here that is `500 GB` for `9/10` of the reads. Everything "
               "to the left of it is cheap and everything to the right is expensive, "
               "so the knee is the fact a target should be chosen against."),
            ("Invert the curve at the target you chose",
             "For a target at or below `s`, the fraction needed is `f · h/s`; past "
               "it, `f + (1−f)(h−s)/(1−s)`. Multiply by the dataset for the "
               "gigabytes. Keeping the fraction as an exact ratio &mdash; `4/45` "
               "&mdash; makes the arithmetic checkable and the answer scalable."),
            ("Quote the memory, the hit rate and the two inputs together",
             "`444.44 GB` on its own is unauditable. `444.44 GB` for `80%`, given "
               "`10%` of the data taking `90%` of the reads, can be argued with "
               "&mdash; and the argument will be about the skew, which is the right "
               "place for it."),
            ("Say what happens if the skew is weaker than measured",
             "Reduce the hot share in the lab and watch the memory needed climb. "
               "The skew is the input the answer is most sensitive to and the one "
               "most likely to drift, so a sizing that does not say what a weaker "
               "skew would cost has not been stress-tested at all."),
        ],
        "worked": {
            "title": "5 TB of timelines, 10% of it taking 90% of the reads",
            "intro": [
                "One dataset, one skew, two targets &mdash; one on each side of the "
                "knee."
            ],
            "lines": [
                "dataset            5 TB",
                "hot fraction f     10%       taking share s = 90% of the reads",
                "knee               (10%, 90%)   cache 500 GB, get 9/10 of the reads",
                "",
                "target h = 80%     h ≤ s, so inside the hot region",
                "   c = f · h/s  =  0.1 · 80/90  =  0.1 · 8/9  =  4/45  =  8.89%",
                "   memory       =  5 TB · 4/45  =  444.44 GB",
                "",
                "target h = 95%     h > s, so past the knee",
                "   c = f + (1−f)(h−s)/(1−s)",
                "     = 0.1 + 0.9 · (0.05/0.10)  =  0.1 + 0.45  =  11/20  =  55%",
                "   memory       =  5 TB · 11/20  =  2.75 TB",
                "",
                "the first 90 points of hit rate      500 GB",
                "reaching 95 points instead         2.75 TB",
                "caching everything                    5 TB",
            ],
            "after": [
                "The three lines at the bottom are the lesson. Nine reads in ten for "
                "a tenth of the storage is why a cache is worth having; the jump "
                "from there to `95%` costing most of the dataset is why a target hit "
                "rate is a budget decision and not an aspiration.",
                "Notice that `80%` cost less than the whole hot region. Targets "
                "below the hot share are bought at the cheap slope, and there is no "
                "reason to cache the entire hot region unless the target requires "
                "it &mdash; which is the practical content of &ldquo;caching is not "
                "all-or-nothing&rdquo;.",
                "For a faded rehearsal, take the lab&rsquo;s catalogue example: "
                "`200 GB` with `5%` hot at `75%` of reads, and a `95%` target. The "
                "supplied first move is that `95% > 75%`, so the target is past the "
                "knee and the second branch applies. Work out the fraction, the "
                "gigabytes, and what caching just the hot region would have bought "
                "&mdash; then check all three in the lab, and say which of the two "
                "inputs you would go and measure again.",
            ],
        },
        "quiz_title": "Working sets and hit rates",
        "quiz": [
            {"q": "A `5 TB` dataset has `10%` of its data taking `90%` of the reads. How much memory does an `80%` hit rate need?",
             "a": ["`400 GB`", "`444.44 GB`", "`500 GB`", "`4 TB`"],
             "c": 1,
             "why": "`80%` is below the hot share, so the target is inside the hot "
                    "region and `c = f · h/s = 0.1 · 8/9 = 4/45`, which is `8.89%` "
                    "of `5 TB` or `444.44 GB`. `500 GB` is the whole hot region, "
                    "which buys `90%` and is more than the target requires. `400 GB` "
                    "is `8%` &mdash; the answer you get by scaling the hot fraction "
                    "by the target directly and forgetting to divide by the share. "
                    "`4 TB` is `80%` of the dataset, which is the all-or-nothing "
                    "reading of the question."},
            {"q": "With the same skew, what does raising the target from `90%` to `95%` cost?",
             "a": ["Another `500 GB`, at the rate the first ninety points cost",
                   "Nothing: `90%` already caches the hot region",
                   "The memory rises from `500 GB` to `2.75 TB`",
                   "The whole dataset, `5 TB`"],
             "c": 2,
             "why": "`90%` is exactly the knee and costs `500 GB`. Past it, hits "
                    "have to be bought from the cold region, where reads are spread "
                    "thinly: `c = 0.1 + 0.9 · (0.05/0.10) = 11/20`, which is `55%` "
                    "of the data, or `2.75 TB`. Extrapolating the cheap slope would have "
                    "predicted about another `500 GB`, and that slope stops at the "
                    "knee. It is not the whole dataset either &mdash; that would be "
                    "`100%`, or `5 TB`."},
            {"q": "What is the hot fraction a fact about?",
             "a": ["The data: some records are simply bigger than others",
                   "The traffic over a window: which keys the reads actually touched",
                   "The cache: how much of it is currently occupied",
                   "The storage engine: how the records are laid out on disk"],
             "c": 1,
             "why": "`f` and `s` describe access, not layout: `10%` of the keys "
                    "taking `90%` of the reads is a statement about a log of "
                    "requests over some window. That is also why the pair drifts "
                    "&mdash; a release or an import changes what is being read "
                    "without changing a byte of the data &mdash; and why a sizing "
                    "that quotes them without their window cannot be checked later."},
        ],
        "mistakes": [
            ("Treating caching as all-or-nothing",
             "&ldquo;The dataset is five terabytes, so a cache is pointless until we "
             "can afford five terabytes of RAM&rdquo; skips the only fact that "
             "matters: `444.44 GB` serves `80%` of the reads, and `500 GB` serves "
             "`90%`. The relevant denominator is the reads, not the bytes, and the "
             "interesting region of the curve is the part between caching nothing "
             "and caching everything &mdash; which is where every real system sits."),
            ("Assuming the last points of hit rate cost what the first did",
             "Going from nothing to `90%` costs `500 GB`; going from there to `95%` "
             "costs `2.75 TB`. Inside the hot region each point of cached data buys "
             "nine points of hit rate and outside it each buys a ninth of a point, "
             "so a target picked without locating the knee is a budget picked at "
             "random. Round numbers like `99%` are where this does the most damage, "
             "because they sound like rigour and price like the whole dataset."),
            ("Taking the hot fraction for a property of the data",
             "`f` and `s` are measured from access logs over a window and describe "
             "traffic, so they move when traffic moves &mdash; a release, a batch "
             "job, one story everybody reads. The model layered on top of them "
             "assumes uniform popularity within each region, which is what makes the "
             "curve two straight lines rather than a smooth one. Both are worth "
             "saying out loud whenever the gigabyte figure is quoted."),
        ],
        "standard": ("Finish when a memory budget is argued from the hit rate it buys rather than from the size of the data.",
                     "You should be able to turn a dataset size, a hot fraction, a "
                     "hot share and a target hit rate into gigabytes, locate the knee "
                     "and say what it costs, explain why the points past it are so "
                     "much more expensive, and name the two assumptions the "
                     "piecewise-linear model rests on."),
        "note": "Every quantity this course produces is now in hand, and all of them share one weakness: they were computed once, by one route, from factors that were guessed. &ldquo;Triangulating an Estimate&rdquo; is the only honest check &mdash; a second route to the same number that shares no assumption with the first &mdash; and it is precise about what makes a second route a check rather than a ritual.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "triangulating-an-estimate",
        "title": "Triangulating an Estimate",
        "module": "The check",
        "one_line": "Build two independent routes to one quantity and test their ratio against the width the inputs deserve.",
        "summary": (
            "An estimate cannot be checked by redoing it. It is checked by reaching "
            "the same quantity along a route that shares no assumption with the "
            "first, and then asking whether the two answers agree &mdash; where "
            "&ldquo;agree&rdquo; means inside the interval the inputs earned, not "
            "&ldquo;close&rdquo;. The failure mode is specific and common: a second "
            "route that borrows a factor from the first cannot contradict it, "
            "because a shared factor cancels out of the ratio between them."
        ),
        "key": [
            "route A   500 000 uploaders · 20 photos · 2 MB     =  2.0·10¹³ B/day",
            "route B   10 000 000 objects · 1.8 MB              =  1.8·10¹³ B/day",
            "",
            "A / B  =  10/9  =  1.1111",
            "band from Orders of Magnitude:  ÷8 … ×8",
            "10/9 lies inside the band, so the routes agree",
            "",
            "a factor in BOTH chains cancels: the ratio cannot move",
        ],
        "key_label": "Two routes, one ratio, and the band it has to fall in",
        "concepts_intro": (
            "One hard idea &mdash; independence is what makes a check a check "
            "&mdash; stated three ways: what a second route has to avoid, what "
            "agreement has to mean, and what a shared factor does to the arithmetic."
        ),
        "concepts": [
            ("A check is a route that shares no assumption with the first",
             "Route A goes from people: uploaders, photos each, bytes each. Route B "
             "goes from the object store: objects written, mean size measured on "
             "disk. They arrive at the same quantity &mdash; bytes uploaded per day "
             "&mdash; through different data, and that is the only property that "
             "makes the second one informative. Redoing the same multiplication more "
             "carefully is not a check; it is the same claim, twice."),
            ("Agreement is a claim about a band, not about closeness",
             "`2.0·10¹³` against `1.8·10¹³` is a ratio of `10/9`. Whether that "
             "counts as agreement depends entirely on how well the inputs were "
             "known: against the `÷8 … ×8` band that three `±2×` factors earn, it is "
             "comfortable agreement; against factors known to a few percent it would "
             "be a serious disagreement. The band comes from &ldquo;Orders of "
             "Magnitude&rdquo;, and without it the word agree means nothing."),
            ("A shared factor cancels and therefore cannot be contradicted",
             "Give route B the same `2 MB` per photo that route A assumed, and the "
             "two answers become `2.0·10¹³` and `2.0·10¹³` and the ratio becomes "
             "exactly `1` &mdash; for every possible value of that factor. A "
             "quantity that appears in both products divides out of their quotient, "
             "so no value of it could ever make the check fail. An agreement nothing "
             "could have broken has tested nothing."),
        ],
        "read_title": "Two routes to one number, and what makes the second one a check",
        "read_intro": "Why a second route is the only available check, what agreement has to mean, and how a shared factor makes the whole exercise empty.",
        "body": [
            ("def", ("Triangulation",
                     "To <strong>triangulate</strong> an estimate is to compute the "
                     "same quantity by a second route whose factors are "
                     "<strong>independent</strong> of the first &mdash; no factor "
                     "appears in both chains &mdash; and to compare the two answers "
                     "by their <strong>ratio</strong>. The estimates "
                     "<strong>agree</strong> when the ratio lies within the "
                     "<strong>band</strong> `÷k … ×k` that the inputs&rsquo; "
                     "half-widths earn.")),
            ("p", "The reason a second route is the only check available is that "
                  "nothing else can fail. The arithmetic can be verified by redoing "
                  "it, and the units can be verified by writing them down, and "
                  "neither of those can tell you that a factor was wrong. An "
                  "assumption is only testable against evidence that did not come "
                  "from it."),
            ("math", [
                "route A · from the people",
                "   daily uploaders                 500 000",
                "   × photos per person per day          20",
                "   × bytes per photo             2 000 000",
                "   =                        20 000 000 000 000   B/day",
                "",
                "route B · from the object store",
                "   objects written per day      10 000 000",
                "   × mean object size on disk    1 800 000",
                "   =                        18 000 000 000 000   B/day",
                "",
                "A / B  =  20/18  =  10/9  =  1.1111",
                "band   =  ÷8 … ×8          1/8 ≤ 10/9 ≤ 8        inside",
            ]),
            ("p", "The two routes share no factor. Route A rests on a guess about "
                  "how many photos a person uploads and on an assumed size per "
                  "photo; route B rests on an object count and a mean size measured "
                  "on disk. Drag the assumed size per photo in the lab and route A "
                  "moves while route B stays exactly where the measurement put it, "
                  "which is precisely what makes the comparison capable of failing."),
            ("example", ("The same check, sabotaged",
                         "Now give route B the assumed `2 MB` per photo instead of "
                         "the measured `1.8 MB`. Both routes now say `2.0·10¹³` "
                         "bytes a day, the ratio is exactly `1`, and the check looks "
                         "better than it did. It is worth nothing: the shared factor "
                         "divides out of the quotient, so the ratio stays at `1` "
                         "whatever value that factor takes. The lab marks the shared "
                         "row in red and reports the verdict as &ldquo;no check "
                         "made&rdquo;, which is the accurate description.")),
            ("h3", "Why a cancelling factor is invisible from the inside"),
            ("p", "A fake check does not look like a failure; it looks like an "
                  "unusually good result. That is what makes it worth a lesson. The "
                  "test is mechanical rather than intuitive: list the factors of both "
                  "chains and look for a name appearing twice. If one does, the "
                  "agreement carries no information about it, and the honest move is "
                  "to say which factor remains untested rather than to report the "
                  "ratio."),
            ("p", "The lab makes the mechanism visible by letting you drag the "
                  "shared factor. With independent routes the ratio moves and the "
                  "check can fail; with the factor shared the ratio does not move at "
                  "all, however far the slider goes. A quantity no possible value of "
                  "which could change the outcome has not been tested."),
            ("h3", "What the band is, and where it comes from"),
            ("p", "The band is the half-width of the estimate, computed in "
                  "&ldquo;Orders of Magnitude&rdquo;: three factors known to `±2×` "
                  "give `÷8 … ×8`. Two routes whose answers differ by `10/9` are "
                  "well inside that and are telling the same story to the accuracy "
                  "anyone claimed. Two routes differing by `20×` are not, and no "
                  "amount of explaining will make them."),
            ("p", "So the band has to be fixed before the two answers are compared, "
                  "and it has to come from the inputs rather than from the results. "
                  "Widening `k` after seeing a disagreement is the same defect as a "
                  "shared factor, arriving a step later: it makes the check "
                  "unfailable after the fact."),
            ("h3", "When they do not agree"),
            ("p", "A disagreement outside the band is the useful outcome, not the "
                  "failed one. It means one of the assumptions is wrong, and it "
                  "usually says which: the factors the two routes do not share are "
                  "the suspects, and the one the two routes disagree about most is "
                  "the place to go and measure. Rechecking the multiplication is the "
                  "wrong response, because the multiplication was never the part "
                  "carrying the uncertainty."),
            ("p", "One last piece of procedure, which is a fact about the order you "
                  "do things in rather than about arithmetic. Build the second route "
                  "before looking at the first answer again. A route constructed "
                  "with the target number in mind will reach it, by a series of small "
                  "and individually defensible choices, and the resulting agreement "
                  "will be as empty as a shared factor and much harder to see."),
        ],
        "lab": ("estimate", {
            "mode": "triangulate",
            "preset": "photo-bytes",
            "panel_title": "Build the second route, then decide whether it is one",
            "panel_intro": "The second selector is the whole lesson: hand route B "
                           "route A&rsquo;s assumption and the ratio pins to `1` and "
                           "stops responding to anything. Shared factors are marked "
                           "in the chains, and the verdict changes to &ldquo;no check "
                           "made&rdquo; rather than to a better-looking number.",
        }),
        "steps_title": "Checking an estimate you have just made",
        "steps_intro": "Fix the band, build a route that could disagree, compare last.",
        "steps": [
            ("Write down the band before you start the second route",
             "It comes from the half-widths of the first route&rsquo;s factors: "
             "three at `±2×` give `÷8 … ×8`. Fixing `k` in advance is what stops the "
             "comparison from being adjusted to fit whatever comes out, which is the "
             "most comfortable way to fail this lesson."),
            ("Build the second route from different evidence, before looking back",
             "Different data, different people, a different part of the system. Do "
             "not consult the first answer while doing it &mdash; a chain built "
             "toward a known number reaches it, one defensible choice at a time, and "
             "the agreement means nothing afterwards."),
            ("List both chains and look for a name that appears twice",
             "Mechanical, and quicker than reasoning about it. Any factor common to "
             "both products cancels out of their ratio, so it cannot be contradicted "
             "by the comparison. If one shows up, say so and name it as untested "
             "rather than reporting the ratio as a check."),
            ("Take the ratio, and compare it against the band you fixed",
             "`A ÷ B`, against `÷k … ×k`. Inside the band the routes agree to the "
             "accuracy the inputs claimed; outside it they do not, and the band does "
             "not get widened at this point."),
            ("On a disagreement, go after the factor rather than the arithmetic",
             "The multiplication is not where the uncertainty was. Compare the "
             "factors the two routes do not share, find the one they most disagree "
             "about, and measure that. A disagreement that identifies a factor is "
             "the most useful thing an estimate can produce."),
        ],
        "worked": {
            "title": "Bytes uploaded a day, from the people and from the object store",
            "intro": [
                "Two routes to one quantity, the ratio between them, and then the "
                "same comparison with one factor shared."
            ],
            "lines": [
                "band, fixed first:   three factors at ±2×   ⟹   ÷8 … ×8",
                "",
                "route A · from the people",
                "   500 000 uploaders × 20 photos/day × 2 000 000 B",
                "                              = 20 000 000 000 000 B/day",
                "",
                "route B · from the object store",
                "   10 000 000 objects/day × 1 800 000 B measured on disk",
                "                              = 18 000 000 000 000 B/day",
                "",
                "A / B = 20/18 = 10/9 = 1.1111        1/8 ≤ 10/9 ≤ 8      agree",
                "shared factors: none                 the routes are independent",
                "",
                "now let route B borrow route A's 2 000 000 B per photo:",
                "   10 000 000 × 2 000 000     = 20 000 000 000 000 B/day",
                "   A / B                      = 1      exactly, for ANY value",
                "   shared factors: bytes per photo      verdict: no check made",
            ],
            "after": [
                "The last block is the one to sit with. The ratio did not merely "
                "come out well, it came out at exactly `1`, and it will come out at "
                "exactly `1` for every possible value of the shared factor. Nothing "
                "about that comparison could have gone wrong, which is the same as "
                "saying nothing about it was a test.",
                "The independent version can fail, and that is its entire value. "
                "Move the assumed bytes per photo in the lab and route A moves while "
                "route B stays put; push it far enough and the ratio leaves the "
                "band, at which point you have learnt that the assumption is "
                "incompatible with what the object store measured.",
                "For a faded rehearsal, take the lab&rsquo;s requests-a-day example: "
                "daily active users times sessions each times requests per session, "
                "against sessions counted in the access log times requests per "
                "session counted in the log. The supplied first move is to fix the "
                "band before computing anything. Then decide, before you look at the "
                "verdict, whether those two routes are independent &mdash; the "
                "phrase &ldquo;requests per session&rdquo; appears in both, and the "
                "question is whether the two figures came from the same place.",
            ],
        },
        "quiz_title": "Routes, ratios and bands",
        "quiz": [
            {"q": "Route A gives `2.0·10¹³` bytes a day and route B gives `1.8·10¹³`. The inputs were three factors at `±2×`. What should be concluded?",
             "a": ["They disagree: the answers differ by more than ten percent",
                   "They agree: `10/9` is well inside the `÷8 … ×8` band the inputs earned",
                   "Nothing, until the two routes are averaged",
                   "They agree, because the two answers are close"],
             "c": 1,
             "why": "Agreement is a claim about a band, and three factors at `±2×` "
                    "earn `÷8 … ×8`. `10/9` is comfortably inside it. Ten percent "
                    "sounds like a lot only if you forget what was claimed about the "
                    "inputs &mdash; against factors known to a few percent the same "
                    "ratio would be a real disagreement. &ldquo;Close&rdquo; is not "
                    "a criterion; it is the absence of one."},
            {"q": "Route B is rebuilt using route A&rsquo;s assumed bytes per photo. The ratio comes out at exactly `1`. What has been learnt?",
             "a": ["That the estimate is confirmed to high precision",
                   "That the assumed size per photo is correct",
                   "Nothing: the shared factor cancels, so no value of it could have failed",
                   "That route B is more accurate than route A"],
             "c": 2,
             "why": "A factor appearing in both products divides out of their "
                    "quotient, so the ratio is `1` whatever that factor is &mdash; "
                    "including badly wrong. The comparison had no possible failing "
                    "outcome, which is exactly what it means for a check to be "
                    "empty. The exactness of the `1` is the tell: a real check on "
                    "independent data essentially never lands on a whole number."},
            {"q": "Two independent routes disagree by a factor of `20`, against a band of `÷8 … ×8`. What is the right next move?",
             "a": ["Recheck the arithmetic in both chains",
                   "Widen the band until the two routes agree",
                   "Average the two answers and carry the mean forward",
                   "Compare the unshared factors and go and measure the one they most disagree about"],
             "c": 3,
             "why": "The multiplication was never where the uncertainty lived, so "
                    "rechecking it will usually confirm both answers and settle "
                    "nothing. Widening the band after seeing the result is the same "
                    "defect as a shared factor, one step later: it makes the check "
                    "unfailable. Averaging buries the finding. A disagreement that "
                    "points at a specific factor is the most useful output an "
                    "estimate can have, and following it is the reason to triangulate."},
        ],
        "mistakes": [
            ("Calling a second route a check when it shares a factor",
             "Both chains multiply by the same assumed bytes per photo, the answers "
             "come out at `2.0·10¹³` apiece, the ratio is exactly `1`, and the "
             "estimate looks confirmed. The shared factor cancels out of the "
             "quotient, so the ratio would have been `1` for any value of it. "
             "Nothing could have failed, so nothing was tested &mdash; and a fake "
             "check does not feel like a failure, it feels like an unusually clean "
             "result."),
            ("Deciding agreement by how close the numbers look",
             "`2.0·10¹³` against `1.8·10¹³` is agreement or disagreement depending "
             "entirely on what was claimed about the inputs. Three factors at `±2×` "
             "earn a `÷8 … ×8` band, inside which `10/9` is unremarkable; factors "
             "known to a few percent would make the same ratio a serious problem. "
             "Fix the band from the half-widths before comparing, and never widen it "
             "after seeing the ratio."),
            ("Treating a disagreement as a mistake to be found",
             "Two routes outside the band are not evidence of a slip in the "
             "arithmetic; they are evidence that an assumption is wrong, which is "
             "the most valuable thing an estimate can tell you. The productive "
             "response is to list the factors the routes do not share and go after "
             "the one they most disagree about. Rechecking the multiplications "
             "confirms both answers and leaves the actual finding unexamined."),
        ],
        "standard": ("Finish when a second route that borrows a factor from the first reads as no check at all.",
                     "You should be able to build an independent second route to a "
                     "quantity you have estimated, fix the agreement band from the "
                     "half-widths before comparing, detect a shared factor by "
                     "inspection of the two chains, and say what a disagreement "
                     "identifies rather than what it invalidates."),
        "note": "That is capacity: a rate, the four things it sizes, and a way of checking any of them. &ldquo;Latency and the Tail&rdquo; asks the other question about the same request &mdash; not how many arrive, but how long one takes &mdash; and it begins where this course ended, with the ratio that says a packet crossing a continent costs three hundred round trips inside a datacentre.",
    },
]
