"""Course 2, lessons 01-06 - the floors, the tail as an object, and fan-out."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "latency-is-not-throughput",
        "title": "Latency Is Not Throughput",
        "module": "The floors",
        "one_line": "Classify a transfer as latency-bound or bandwidth-bound, and price the two improvements before choosing one.",
        "summary": (
            "Latency is how long one round trip takes; bandwidth is how many bits a "
            "second the link carries once the answer is flowing. They are two numbers, "
            "and their product &mdash; the bandwidth-delay product &mdash; is how many "
            "bytes the wire holds at once. A transfer smaller than that finishes before "
            "the pipe is full, and for it the bandwidth figure is very nearly irrelevant."
        ),
        "key": [
            "BDP = bandwidth × RTT         the bytes in flight at one instant",
            "t = RTT + size/bandwidth      one waiting term, one sending term",
            "size ≪ BDP  latency-bound     more bandwidth buys almost nothing",
            "size ≫ BDP  bandwidth-bound   a shorter round trip buys almost nothing",
            "100 Mbit/s × 80 ms = 1 MB     64 kB of it: 85.12 ms, 94.0% of it waiting",
        ],
        "key_label": "Two numbers, and the size at which they trade places",
        "concepts_intro": (
            "One hard idea, and it is that there are two numbers here rather than one. "
            "Everything else on this page is the arithmetic of deciding which of the two you are paying."
        ),
        "concepts": [
            ("Latency and bandwidth measure different things",
             "The round-trip time `RTT` is a duration: how long a signal takes to reach "
             "the far end and an answer to come back. Bandwidth is a rate: how many bits "
             "a second the link carries once data is moving. Buying a bigger link raises "
             "the rate. It does not shorten the distance, so it does not move the "
             "duration, and the two can be changed independently of each other."),
            ("The bandwidth-delay product is the wire’s capacity, in bytes",
             "A rate multiplied by a time is a quantity. `100 Mbit/s × 80 ms` is `1 MB`: "
             "that much data can be on the wire at once, sent and not yet arrived. That "
             "is the <strong>bandwidth-delay product</strong>, and it is measured in "
             "bytes rather than in bytes a second, which is what makes it comparable "
             "with the size of a transfer."),
            ("The transfer size decides which term you are paying",
             "Time is `RTT + size/bandwidth`. Well below the `BDP` the first term is "
             "nearly all of it and the transfer is <strong>latency-bound</strong>; well "
             "above it the second takes over and the transfer is "
             "<strong>bandwidth-bound</strong>. No property of the link settles this on "
             "its own. The size does, against the link."),
        ],
        "read_title": "Two numbers, their product, and the transfer that has to choose",
        "read_intro": "What a bandwidth-delay product is a quantity of, and how to read a transfer&rsquo;s size against it.",
        "body": [
            ("def", ("Bandwidth-delay product",
                     "The <strong>bandwidth-delay product</strong> of a link is its "
                     "bandwidth multiplied by its round-trip time. A rate in bits a "
                     "second times a time in seconds is a number of bits, so the product "
                     "is a <strong>quantity of data</strong>: how much can be in flight "
                     "&mdash; sent, and not yet acknowledged &mdash; at any instant.")),
            ("p", "It is worth doing that conversion once, slowly, because the units are "
                  "where this goes wrong. `100 Mbit/s` is `10⁸` bits a second, which is "
                  "`1.25 × 10⁷` bytes a second. Eighty milliseconds of that is `10⁶` "
                  "bytes &mdash; one megabyte, reading `1 kB` as `1000 B`, which is how "
                  "link rates are quoted and how this course counts. So a `100 Mbit/s` "
                  "link with an `80 ms` round trip has a megabyte of road on it."),
            ("math", [
                "bandwidth   100 Mbit/s  =  10⁸ bit/s  =  1.25 × 10⁷ B/s",
                "RTT         80 ms       =  0.08 s",
                "",
                "BDP  =  1.25 × 10⁷ × 0.08  =  10⁶ B  =  1 MB",
                "",
                "        size × 8",
                "t  =  RTT  +  ────────────────        ms, with bandwidth in Mbit/s",
                "        bandwidth × 1000",
            ]),
            ("p", "A `64 kB` transfer over that link costs one round trip of `80 ms` "
                  "plus `64 000 × 8 / (100 × 1000) = 5.12 ms` of sending. That is "
                  "`85.12 ms` in all, of which `94.0%` is waiting. The sending term is "
                  "the smaller number by a factor of more than fifteen, and it is the only one "
                  "bandwidth touches."),
            ("example", ("Pricing the two upgrades on the same transfer",
                         "Double the bandwidth to `200 Mbit/s` and the sending term "
                         "halves to `2.56 ms`: the transfer saves `2.560 ms` and now "
                         "takes `82.56 ms`. Halve the round trip to `40 ms` instead and "
                         "it saves `40 ms`, finishing in `45.12 ms`. The second change "
                         "is worth about sixteen times the first, on the same transfer, "
                         "and no amount of further bandwidth ever closes that gap.")),
            ("h3", "The crossover, and which side of it you are on"),
            ("p", "There is exactly one size at which the two terms cost the same: the "
                  "size for which `size/bandwidth = RTT`, which rearranges to "
                  "`size = bandwidth × RTT`. That is the bandwidth-delay product again. "
                  "The `BDP` is not merely a capacity; it is the crossover, and a "
                  "transfer is latency-bound or bandwidth-bound according to which side "
                  "of it the transfer falls on."),
            ("example", ("The same link, a transfer sixty-two and a half times larger",
                         "`4 MB` over the same `100 Mbit/s` link at `80 ms` spends "
                         "`320 ms` sending and `80 ms` waiting: `400 ms` in all, of "
                         "which the round trip is `20.0%`. This transfer is past the "
                         "`1 MB` crossover and is bandwidth-bound. Here doubling the "
                         "link saves `160 ms` and halving the round trip saves `40 ms` "
                         "&mdash; the advice from the previous example, applied here, "
                         "is four times worse than the alternative.")),
            ("p", "The misconception worth naming out loud is that a faster link lowers "
                  "the round-trip time. It does not. The round trip is set by how far "
                  "the signal goes and how many devices it passes through; a bigger pipe "
                  "moves more per second through the same pipe, at the same distance. "
                  "Someone whose page is slow because it makes four sequential requests "
                  "over an `80 ms` link can buy a gigabit connection and measure no "
                  "change at all."),
            ("p", "What does move the round trip is shortening the distance or removing "
                  "a trip. &ldquo;The Speed-of-Light Floor&rdquo; puts a hard bound "
                  "under the first of those, and &ldquo;Round Trips, Not Bytes&rdquo; "
                  "counts the second, which is usually the one you can change."),
        ],
        "lab": ("latency", {
            "mode": "bdp",
            "panel_title": "Set the link and the transfer",
            "panel_intro": "Both terms are computed exactly from the sizes you set. Start "
                           "at the preset, then push the transfer size past the "
                           "bandwidth-delay product and watch the verdict at the bottom "
                           "of the panel change from latency-bound to bandwidth-bound.",
        }),
        "steps_title": "Deciding what a transfer is bound by",
        "steps_intro": "Four lines of arithmetic, and the fourth is the one that stops you buying the wrong thing.",
        "steps": [
            ("Put the bandwidth into bytes a second",
             "Divide the bit rate by eight. `100 Mbit/s` is `1.25 × 10⁷ B/s`. Doing "
             "this first is what prevents the factor-of-eight error, which is the most "
             "common arithmetic mistake in this whole subject."),
            ("Multiply by the round-trip time to get the BDP",
             "Bytes a second times seconds is bytes. Keep the time in seconds for this "
             "one line even though the rest of the course is in milliseconds, then "
             "convert back; mixing the two here is how a thousand-fold error gets in."),
            ("Compare the transfer size with that product",
             "Smaller means latency-bound: the answer is roughly one round trip and the "
             "bytes are a rounding error. Larger means bandwidth-bound: the answer is "
             "roughly `size/bandwidth` and the round trip is the rounding error."),
            ("Price both improvements before choosing either",
             "Compute what halving the round trip saves and what doubling the bandwidth "
             "saves, in milliseconds, on this transfer. They are rarely close, and the "
             "larger one is almost never the one that was already being proposed."),
        ],
        "worked": {
            "title": "64 kB and 4 MB over one 100 Mbit/s link at 80 ms",
            "intro": [
                "The link never changes. Only the size does, and it changes the answer "
                "to &ldquo;what should we buy?&rdquo; completely."
            ],
            "lines": [
                "link      100 Mbit/s = 1.25 × 10⁷ B/s ,  RTT = 80 ms",
                "BDP       1.25 × 10⁷ × 0.08 s  =  1 000 000 B  =  1 MB",
                "",
                "64 kB     send  =  64 000 × 8 / (100 × 1000)  =  5.12 ms",
                "          t     =  80 + 5.12  =  85.12 ms       waiting: 94.0%",
                "          64 kB < 1 MB          →  latency-bound",
                "          double bandwidth  saves  2.560 ms",
                "          halve RTT         saves  40.000 ms",
                "",
                "4 MB      send  =  4 000 000 × 8 / (100 × 1000)  =  320 ms",
                "          t     =  80 + 320  =  400 ms           waiting: 20.0%",
                "          4 MB > 1 MB           →  bandwidth-bound",
                "          double bandwidth  saves  160 ms",
                "          halve RTT         saves  40 ms",
            ],
            "after": [
                "The two verdicts point in opposite directions on the same link, which "
                "is the point. &ldquo;Is this link fast?&rdquo; has no answer. "
                "&ldquo;Is this transfer fast on this link?&rdquo; has one, and it is "
                "decided by the size against the bandwidth-delay product.",
                "Notice what halving the round trip saves in both rows: `40 ms`, "
                "exactly, regardless of the transfer size. The round-trip term does not "
                "know how big the payload is. That is why it is the term that dominates "
                "small transfers and the term that vanishes into the noise on large ones.",
                "For a faded rehearsal, take a `20 Mbit/s` link with a `200 ms` round "
                "trip &mdash; a satellite hop. The supplied first move is the "
                "conversion: `20 Mbit/s` is `2.5 × 10⁶ B/s`. Compute the "
                "bandwidth-delay product, then decide what a `300 kB` transfer is bound "
                "by, and how many milliseconds each of the two upgrades would save it. "
                "Write down which side of the crossover you are on before you open the "
                "quiz, and check the figure in the lab by setting those three sliders.",
            ],
        },
        "quiz_title": "Which term are you paying?",
        "quiz": [
            {"q": "A link runs at `50 Mbit/s` with a `100 ms` round-trip time. What is its bandwidth-delay product?",
             "a": ["`625 kB`", "`5 MB`", "`50 kB`", "`5 Mbit`"],
             "c": 0,
             "why": "`50 Mbit/s` is `6.25 × 10⁶ B/s`, and `0.1 s` of that is `625 000 B`. "
                    "`5 MB` keeps the answer in bits and calls them bytes &mdash; the "
                    "factor-of-eight error. `50 kB` multiplies the rate by the time in "
                    "milliseconds without converting. `5 Mbit` is the right quantity in "
                    "the wrong unit, and the whole use of a BDP is comparing it with a "
                    "transfer size, which is quoted in bytes."},
            {"q": "On the lab&rsquo;s preset &mdash; `100 Mbit/s`, `80 ms`, `64 kB` &mdash; what does doubling the bandwidth to `200 Mbit/s` save?",
             "a": ["`42.56 ms`, half the total", "`40 ms`", "`2.56 ms`", "Nothing at all"],
             "c": 2,
             "why": "The transfer takes `85.12 ms`: `80 ms` of round trip and `5.12 ms` "
                    "of bytes. Only the second term halves, so the saving is `2.56 ms` "
                    "and the new total is `82.56 ms`. `42.56 ms` halves the whole time, "
                    "which would require the round trip to halve too. `40 ms` is what "
                    "halving the round trip saves. And it is not nothing &mdash; it is "
                    "just about three percent."},
            {"q": "A `10 MB` file is fetched over a `1 Gbit/s` link with a `5 ms` round trip. Which change helps more?",
             "a": ["Halving the round trip to `2.5 ms`",
                   "Doubling the bandwidth to `2 Gbit/s`",
                   "Neither: the transfer is already at the crossover",
                   "They help equally, because the BDP is the crossover"],
             "c": 1,
             "why": "The BDP is `1.25 × 10⁸ × 0.005 = 625 kB`, and `10 MB` is sixteen "
                    "times that, so the transfer is bandwidth-bound: `80 ms` of sending "
                    "against `5 ms` of waiting. Doubling the bandwidth saves `40 ms`; "
                    "halving the round trip saves `2.5 ms`. The BDP is the crossover, "
                    "but this transfer is well past it, so the two are not close."},
        ],
        "mistakes": [
            ("Treating bandwidth and latency as one quality called ‘speed’",
             "They are a rate and a duration, they have different units, and they are "
             "changed by different things. A connection can be enormous and slow, or "
             "tiny and immediate. Any sentence of the form &ldquo;the link is fast&rdquo; "
             "that does not say which of the two it means is a sentence that will "
             "eventually buy the wrong upgrade."),
            ("Dividing by eight in the wrong direction, or not at all",
             "A `100 Mbit/s` link moves `12.5 MB/s`, not `100 MB/s` and not `800 MB/s`. "
             "Every figure in this course that came out eight times too large or eight "
             "times too small came from this line. Convert the rate to bytes a second "
             "as the very first step and the rest of the arithmetic has no unit in it "
             "at all."),
            ("Assuming a faster link lowers the round-trip time",
             "It does not, at any size. The round trip is set by distance and by the "
             "devices on the path. A transfer well below the bandwidth-delay product is "
             "almost entirely round trip, which is exactly the case in which a bandwidth "
             "upgrade is measured, celebrated, and found to have changed nothing."),
        ],
        "standard": ("Finish when you can say which term a transfer is paying before computing anything else.",
                     "You should be able to convert a link rate to bytes a second, compute "
                     "its bandwidth-delay product, classify a given transfer against that "
                     "product, and state in milliseconds what each of the two possible "
                     "upgrades would save on that transfer."),
        "note": 'The round-trip time has been an input everywhere on this page. &ldquo;The Speed-of-Light Floor&rdquo; takes it apart: part of it is a distance divided by a speed and cannot be removed by anything, and the rest is the part worth arguing about. &ldquo;Round Trips, Not Bytes&rdquo; then shows that the count of round trips, not the size of any one of them, is usually what a slow first page load is made of.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-speed-of-light-floor",
        "title": "The Speed-of-Light Floor",
        "module": "The floors",
        "one_line": "Compute the light-speed minimum round trip for a route and the fraction of a measured RTT it accounts for.",
        "summary": (
            "Signals in fibre travel at about two thirds of the speed of light, so a "
            "round trip over a great-circle distance `d` cannot take less than "
            "`2d ÷ (⅔c)`, which is `3d/c`. New York to London is `55.889 ms` and no "
            "engineering removes it. What a measurement has above that floor is the "
            "part that is queueing, serialisation, middleboxes and software &mdash; and "
            "it is the only part anyone can fix."
        ),
        "key": [
            "RTT_min = 2d ÷ (⅔c) = 3d/c       c is exact by definition",
            "NY–London  d = 5585 km           floor 55.889 ms",
            "measured 76 ms                   1.360 × the floor",
            "remainder 20.111 ms              queues, serialisation, middleboxes, code",
            "a CDN shortens d. Nothing shortens 3/c.",
        ],
        "key_label": "A floor that is a distance divided by a speed",
        "concepts_intro": (
            "The hard idea is that one term of a latency measurement is not an "
            "engineering quantity at all. It is geography, and the only lever on it is "
            "moving the endpoints closer together."
        ),
        "concepts": [
            ("The floor is a distance divided by a speed",
             "Light in vacuum travels `299 792 458 m/s`, exactly &mdash; the metre is "
             "defined from it, so `c` is not measured but fixed. Glass slows it to about "
             "two thirds of that. A round trip covers `2d`, so the minimum is "
             "`2d ÷ (2c/3) = 3d/c`, and every figure on this page follows from those "
             "two numbers alone."),
            ("The remainder is the only part you can work on",
             "Subtract the floor from a measurement and what is left is queueing at each "
             "hop, the time to clock the bits onto each link, the middleboxes, and your "
             "own software. New York to London measured at `76 ms` leaves `20.111 ms`. "
             "That is the whole budget an engineering effort has to work inside, and "
             "knowing it stops an argument about the other `55.889 ms`."),
            ("A CDN shortens `d` and does nothing else",
             "Putting a copy of the content nearer the reader reduces the distance, which "
             "reduces the floor, which is a real and large win &mdash; for content that "
             "can be served from the copy. For a request that must reach the origin to "
             "read or change something only the origin knows, the distance is unchanged "
             "and so is the floor."),
        ],
        "read_title": "The floor, the remainder, and what shortens which",
        "read_intro": "An exact fraction of a millisecond, and the honest reading of a measurement that sits above it.",
        "body": [
            ("def", ("Light-speed floor",
                     "The <strong>light-speed floor</strong> for a route is the shortest "
                     "possible round-trip time over it: twice the great-circle distance, "
                     "divided by the propagation speed of a signal in fibre. This course "
                     "takes that speed as `⅔c`, so the floor is `2d ÷ (2c/3) = 3d/c`. It "
                     "assumes a perfectly straight cable and zero processing, and it is "
                     "therefore a bound nothing beats rather than a prediction.")),
            ("p", "Because `c` is exact by definition, so is the floor: for New York to "
                  "London it is the fraction `8 377 500 000 / 149 896 229` "
                  "milliseconds, which is `55.889 ms` to three places. The course quotes "
                  "it as `56 ms`, and the lab prints the fraction it came from so that "
                  "the rounding is visible rather than assumed."),
            ("math", [
                "d = 5585 km = 5 585 000 m",
                "",
                "        2d          2 × 5 585 000        3 × 5 585 000",
                "RTT = ──────  =  ───────────────────  =  ───────────────   s",
                "       ⅔c         ⅔ × 299 792 458         299 792 458",
                "",
                "    =  0.055889…  s  =  55.889 ms",
            ]),
            ("p", "Set the lab&rsquo;s measured round trip to `76 ms`, which is a "
                  "plausible figure for that route on a good day. The measurement is "
                  "`1.360` times the floor, and the unexplained remainder is "
                  "`20.111 ms`. That remainder is the number to take into a meeting. "
                  "Halving it &mdash; which would be an extremely good quarter of work "
                  "&mdash; takes the route from `76 ms` to about `66 ms`, a saving of "
                  "thirteen percent."),
            ("ul", [
                "New York &rarr; San Francisco, `4139 km` &mdash; floor `41.419 ms`",
                "New York &rarr; London, `5585 km` &mdash; floor `55.889 ms`",
                "Mumbai &rarr; London, `7200 km` &mdash; floor `72.050 ms`",
                "San Francisco &rarr; Tokyo, `8280 km` &mdash; floor `82.857 ms`",
                "Frankfurt &rarr; Singapore, `10 263 km` &mdash; floor `102.701 ms`",
                "London &rarr; Sydney, `16 993 km` &mdash; floor `170.048 ms`",
            ]),
            ("h3", "What a content network actually buys"),
            ("p", "A `170 ms` floor between London and Sydney is why a service with one "
                  "region has a bad day in the other hemisphere, and it is why the fix "
                  "is a second copy of the data rather than a faster anything. This is "
                  "the honest case for a content network: it does not accelerate a "
                  "packet, it shortens the route the packet has to take."),
            ("example", ("The request a CDN cannot help",
                         "A reader in Sydney loads a page: the images, the stylesheet "
                         "and the script come from a nearby cache, and their floor drops "
                         "from `170.048 ms` to whatever the local distance is. Then they "
                         "post a comment. That write must reach the one place that owns "
                         "the data, so its floor is `170.048 ms` again, and so is the "
                         "floor on the confirmation. No configuration of the cache "
                         "changes either number. &ldquo;Put it on a CDN&rdquo; is an "
                         "answer about the first group of requests offered as if it "
                         "were an answer about the second.")),
            ("p", "The lab will also let you enter a measurement below the floor, and it "
                  "prints a negative remainder when you do. That is not a fast network; "
                  "it is a wrong distance. The usual cause is measuring to a nearby edge "
                  "node while believing you measured to the origin, which is the same "
                  "confusion as the example above with the sign the other way round."),
            ("p", "Two cautions on the model. The `⅔c` figure is a convention &mdash; "
                  "real fibre runs at roughly `0.66` to `0.69` of `c` depending on the "
                  "glass &mdash; so treat the floor as accurate to a few percent rather "
                  "than exact in the physical sense, even though the arithmetic that "
                  "produces it is exact. And real cables are not great circles: they "
                  "follow coastlines, rights of way and existing ducts, so the true path "
                  "is longer than `d` and the true floor is therefore somewhat higher "
                  "than the one computed here."),
        ],
        "lab": ("latency", {
            "mode": "lightspeed",
            "panel_title": "Pick a route, or set a distance",
            "panel_intro": "The floor is an exact fraction because `c` is exact by "
                           "definition. Choose a route, then move the measured round trip "
                           "and watch the split between the part that is physics and the "
                           "part that is engineering.",
        }),
        "steps_title": "Putting a floor under a route",
        "steps_intro": "Three lines to the floor, and a fourth that decides whether the remainder is worth anyone&rsquo;s quarter.",
        "steps": [
            ("Get the great-circle distance, not the cable length",
             "The floor is a lower bound, so it should use the shortest distance that "
             "exists, which is the great circle. A real cable is longer and its true "
             "floor is higher; using the great circle keeps the bound honest."),
            ("Compute `3d/c` and keep it in milliseconds",
             "Twice the distance at two thirds of `c` is three times the distance at "
             "`c`. With `d` in metres and `c` in metres a second the answer is in "
             "seconds, so multiply by a thousand once, at the end."),
            ("Subtract the floor from what you measured",
             "The difference is the whole of the improvable part. Quote it as a number "
             "of milliseconds and as a ratio: `76 ms` against a `55.889 ms` floor is "
             "`20.111 ms` of remainder at `1.360` times the floor."),
            ("Decide what the remainder is worth before optimising it",
             "If the remainder is a fifth of the measurement, then a heroic effort that "
             "halves it moves the user-visible number by a tenth. If the remainder is "
             "four fifths of the measurement, the same effort is transformative. The "
             "ratio tells you which world you are in."),
        ],
        "worked": {
            "title": "A 76 ms measurement between New York and London",
            "intro": [
                "One measurement, split into the part that is geography and the part "
                "that is somebody&rsquo;s code."
            ],
            "lines": [
                "d            5585 km, great circle",
                "floor        3 × 5 585 000 / 299 792 458  s",
                "           = 8 377 500 000 / 149 896 229  ms   (exact)",
                "           = 55.889 ms",
                "",
                "measured     76.000 ms",
                "ratio        76 / 55.889  =  1.360",
                "remainder    76 − 55.889  =  20.111 ms",
                "",
                "if the remainder were halved:",
                "             55.889 + 10.056  =  65.945 ms",
                "             saving 10.055 ms, or 13.2% of the measurement",
            ],
            "after": [
                "The remainder is `26%` of the measurement, so the very best possible "
                "outcome &mdash; removing every queue, every middlebox and all the "
                "software &mdash; is a `26%` improvement. That is the ceiling on the "
                "whole category of work, and it is worth knowing before the work starts.",
                "The same arithmetic run the other way is how you decide to place a "
                "second region. If the target is a `100 ms` round trip, then `3d/c ≤ "
                "100 ms` gives `d ≤ 9993 km`, and every user further away than that "
                "cannot be served inside the target from this location no matter what is "
                "built. That is a siting decision falling out of one division.",
                "For a faded rehearsal, take Frankfurt to Singapore at `10 263 km` with "
                "a measured round trip of `165 ms`. The supplied first move is the "
                "floor, which the lab prints as `102.701 ms`. Compute the ratio and the "
                "remainder, then say what fraction of the measurement the best possible "
                "engineering effort could remove, and whether a `120 ms` target is "
                "reachable from Frankfurt at all. Write the answer down before opening "
                "the quiz.",
            ],
        },
        "quiz_title": "Floors and remainders",
        "quiz": [
            {"q": "A route is `10 000 km` and the floor is computed as `3d/c`. Roughly what is it?",
             "a": ["`33 ms`", "`67 ms`", "`100 ms`", "`150 ms`"],
             "c": 2,
             "why": "`3 × 10⁷ m ÷ 2.998 × 10⁸ m/s ≈ 0.1 s`, so about `100 ms`. `33 ms` "
                    "is `d/c`, a one-way trip in vacuum. `67 ms` is `2d/c`, the round "
                    "trip in vacuum, which omits the slowing in glass. `150 ms` would "
                    "need a propagation speed near `c/2`."},
            {"q": "A team measures `120 ms` between London and Sydney and reports a large optimisation opportunity. What does the floor say?",
             "a": ["The remainder is about `50 ms` and the opportunity is real",
                   "The measurement is below the `170.048 ms` floor, so something about the measurement is wrong",
                   "The floor does not apply because the traffic is encrypted",
                   "The floor is `85 ms`, since `170 ms` counts both directions"],
             "c": 1,
             "why": "The floor for `16 993 km` is `170.048 ms` and nothing beats it. A "
                    "`120 ms` measurement on that route means the packets did not go to "
                    "Sydney &mdash; usually they reached a nearby edge node instead. "
                    "Encryption adds round trips, it does not exempt anyone from physics. "
                    "And the floor already counts both directions: `2d` is in the numerator."},
            {"q": "Which change lowers the light-speed floor between two endpoints?",
             "a": ["Upgrading both ends to a faster link",
                   "Removing a TLS handshake",
                   "Serving the request from a location nearer the user",
                   "Using a protocol with smaller headers"],
             "c": 2,
             "why": "Only the distance is in the formula, so only moving an endpoint "
                    "changes the floor. Bandwidth does not appear in `3d/c`. Removing a "
                    "handshake removes a whole round trip, which is a large win &mdash; "
                    "but it lowers the total, not the floor on each remaining trip. "
                    "Headers affect the bytes, which is the other term entirely."},
        ],
        "mistakes": [
            ("Quoting a one-way figure as a round trip",
             "`2d` is in the numerator because the signal has to come back. The one-way "
             "minimum from New York to London is `27.944 ms`; the round trip is "
             "`55.889 ms`. Anything that halves the expected answer without changing the "
             "distance is this error, and it makes every budget built on it twice as "
             "generous as it should be."),
            ("Using `c` instead of `⅔c`",
             "In vacuum the New York to London round trip would be `37.259 ms`. In fibre "
             "it is `55.889 ms`, half as much again. The glass is not a detail: it is "
             "the difference between a floor that is comfortably under a target and one "
             "that is not."),
            ("Offering a cache as the answer to a request that must reach the origin",
             "A nearby copy shortens the distance for anything that can be served from "
             "the copy, and does nothing at all for a write, a personalised response, or "
             "a read that must be current. Both kinds of request usually exist in the "
             "same product, and the floor is the number that separates them."),
        ],
        "standard": ("Finish when a latency figure splits, in your head, into a floor and a remainder.",
                     "You should be able to compute `3d/c` for a route, express a "
                     "measurement as a multiple of that floor, state the remainder in "
                     "milliseconds, and say which proposed changes can move it and which "
                     "cannot."),
        "note": 'The floor is one round trip. A first page load usually pays for several of them in sequence, and &ldquo;Round Trips, Not Bytes&rdquo; counts them: at this route&rsquo;s measured `76 ms`, four sequential handshakes cost more than three hundred milliseconds before any content moves at all. The floor computed here reappears as a fixed, non-negotiable line item in &ldquo;Latency Budgets&rdquo;.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "round-trips-not-bytes",
        "title": "Round Trips, Not Bytes",
        "module": "The floors",
        "one_line": "Compute time-to-first-byte from a round-trip count, and the payload size at which bytes overtake round trips.",
        "summary": (
            "A first connection pays for DNS, a TCP handshake, a TLS handshake and then "
            "the request itself, and none of them can start until the one before has "
            "finished. The time is `k·RTT + bytes/bandwidth`, and for anything smaller "
            "than a few hundred kilobytes the first term is nearly all of it. The useful "
            "question is not how many bytes the response is but how many times the "
            "conversation went back and forth."
        ),
        "key": [
            "t = k·RTT + bytes/bandwidth      k is the sequential round-trip count",
            "DNS 1 + TCP 1 + TLS 1.2 2 + request 1   =  k = 5",
            "5 × 80 ms = 400 ms               before one byte of the answer arrives",
            "14 kB at 10 Mbit/s = 11.2 ms     the round trips are 35.7× the bytes",
            "crossover = k × BDP = 500 kB     the payload at which the terms are equal",
        ],
        "key_label": "Two terms again, and the one with a small integer in front of it",
        "concepts_intro": (
            "The new idea is the multiplier `k`. It is a count of sequential exchanges, "
            "it is usually between one and six, and it is nearly always the largest "
            "thing on the page."
        ),
        "concepts": [
            ("Handshakes are sequential, so they add",
             "The DNS answer is needed before the TCP connection can open, the connection "
             "is needed before the TLS negotiation, and the negotiation before the "
             "request. Nothing here overlaps. Four legs at `80 ms` is `320 ms` of doing "
             "nothing but waiting, and the reason it is `320` rather than `80` is "
             "ordering, not volume."),
            ("Time to first byte is `k·RTT`",
             "The bytes cannot begin to arrive until the last round trip has completed, "
             "so `k·RTT` is not a share of the total &mdash; it is the delay before the "
             "total starts. On the lab&rsquo;s preset that is `400 ms` of a `411.2 ms` "
             "request, and the whole payload accounts for the remaining `11.2 ms`."),
            ("The crossover is `k` bandwidth-delay products",
             "The bytes cost as much as the round trips when "
             "`bytes/bandwidth = k·RTT`, so the crossover payload is "
             "`k × bandwidth × RTT`. At `k = 1` that is exactly the bandwidth-delay "
             "product of &ldquo;Latency Is Not Throughput&rdquo;: the two lessons are "
             "one fact, counted once and then `k` times."),
        ],
        "read_title": "Counting the conversation",
        "read_intro": "Why the fix for a slow first load is usually removing an exchange rather than removing a kilobyte.",
        "body": [
            ("p", "Open the lab at its preset and read the four selectors down the side: "
                  "a DNS lookup, a TCP handshake, a TLS 1.2 negotiation worth two round "
                  "trips, and the request itself. That is `k = 5`, and at an `80 ms` "
                  "round trip the time to first byte is `400 ms`. The `14 kB` of HTML "
                  "then costs `11.2 ms` at `10 Mbit/s`. The whole request takes "
                  "`411.2 ms`, and `97.3%` of it is round trips."),
            ("def", ("Round-trip count",
                     "The <strong>round-trip count</strong> `k` of a request is the "
                     "number of exchanges that must complete in sequence before the "
                     "response can begin to arrive. It counts only exchanges on the "
                     "critical path: work that happens in parallel with something else "
                     "does not add to `k`, and that is the whole reason the count is "
                     "worth taking seriously rather than simply totalling the "
                     "protocol&rsquo;s messages.")),
            ("math", [
                "k     = 1 (DNS) + 1 (TCP) + 2 (TLS 1.2) + 1 (request)  =  5",
                "",
                "TTFB  = k × RTT          =  5 × 80          =  400.0 ms",
                "bytes = size × 8 / (Mbit/s × 1000)",
                "      = 14 000 × 8 / (10 × 1000)            =   11.2 ms",
                "",
                "total =                                        411.2 ms",
                "ratio = 400 / 11.2                          =   35.7 ×",
            ]),
            ("p", "The ratio is the number that settles the argument. The round trips "
                  "cost `35.7` times what the payload costs, so a proposal to halve the "
                  "HTML saves `5.6 ms` of a `411.2 ms` request &mdash; about one and a "
                  "third percent &mdash; while removing a single handshake saves `80 ms`, "
                  "or nineteen percent. Removing one round trip is worth as much as "
                  "deleting `100 kB` on this link, and the HTML is `14 kB`."),
            ("h3", "The crossover payload"),
            ("p", "The two terms are equal when the payload reaches "
                  "`k × bandwidth × RTT`, which here is `5 × 100 kB = 500 kB`. Below "
                  "that the round trips dominate and above it the bytes do. A `14 kB` "
                  "document is a thirty-fifth of the way there, which is why the byte "
                  "count is not the lever; a `4 MB` video segment on the same connection "
                  "is eight times past it, and for that one the bytes are the whole story."),
            ("example", ("The same request with the handshakes removed",
                         "Cache the DNS answer, reuse the connection, and the only "
                         "exchange left is the request itself: `k = 1`. Time to first "
                         "byte falls from `400 ms` to `80 ms` and the total from "
                         "`411.2 ms` to `91.2 ms` &mdash; a saving of `320 ms`, which is "
                         "`78%` of the original. Nothing about the payload changed, and "
                         "nothing about the link changed. Four exchanges were removed "
                         "from the front of the request.")),
            ("ul", [
                "DNS &mdash; one round trip, and zero once the answer is cached",
                "TCP &mdash; one round trip to open the connection, and zero when an open one is reused",
                "TLS &mdash; two round trips in version 1.2, one in 1.3, and zero on a resumed session",
                "the request &mdash; one round trip, and it is the only one that carries your data",
            ]),
            ("p", "Every entry in that list except the last is overhead that a "
                  "well-configured client and server pay once and then stop paying. This "
                  "is the reason a site feels slow on the first page and fast on the "
                  "second, and it is why the measurement to trust is the cold one."),
            ("p", "The misconception this lesson exists to name is optimising the term "
                  "you are not paying. Shaving bytes when `k·RTT` is thirty-five times "
                  "the byte cost is work that will be done carefully, measured "
                  "honestly, and found to have achieved nothing. Compute the ratio "
                  "first, and let it choose the work."),
        ],
        "lab": ("latency", {
            "mode": "roundtrips",
            "panel_title": "Turn handshakes on and off",
            "panel_intro": "Each selector removes one sequential exchange. Start from the "
                           "cold-connection preset, then turn them off one at a time and "
                           "watch the time to first byte fall in whole round trips.",
        }),
        "steps_title": "Counting round trips before counting bytes",
        "steps_intro": "The count comes first, because it decides whether the byte count matters at all.",
        "steps": [
            ("Count the exchanges that must complete in order",
             "DNS, connection, encryption, request. Count only what is sequential: a "
             "lookup that happens while another connection is already open does not add "
             "to `k`, and neither does anything the client did before the user clicked."),
            ("Multiply the count by the round-trip time",
             "That product is the time to first byte. It is not a share of the response "
             "time; it is the delay before the response time starts, and it is the same "
             "whether the answer is one byte or one megabyte."),
            ("Compute the byte term and take the ratio",
             "`size × 8 / (Mbit/s × 1000)` is the byte cost in milliseconds. Divide the "
             "round-trip term by it. A ratio above about three means the payload is not "
             "where the time is going."),
            ("Remove an exchange, or accept that bytes are the problem",
             "Each removed round trip is worth exactly `RTT` milliseconds. Compare that "
             "with what a realistic reduction in payload would save, using the crossover "
             "payload `k × bandwidth × RTT` as the point at which the two swap places."),
        ],
        "worked": {
            "title": "A cold 14 kB page load at 80 ms, then a warm one",
            "intro": [
                "Same page, same link, same bytes. The only thing that changes is how "
                "many times the two ends have to talk before the content can start."
            ],
            "lines": [
                "cold     DNS 1 + TCP 1 + TLS 1.2 2 + request 1   →  k = 5",
                "         TTFB   = 5 × 80                          =  400.0 ms",
                "         bytes  = 14 000 × 8 / (10 × 1000)        =   11.2 ms",
                "         total                                    =  411.2 ms",
                "         round trips are 400 / 11.2 = 35.7 × the bytes",
                "",
                "warm     DNS cached 0 + TCP reused 0 + TLS resumed 0 + request 1  →  k = 1",
                "         TTFB   = 1 × 80                          =   80.0 ms",
                "         bytes                                    =   11.2 ms",
                "         total                                    =   91.2 ms",
                "",
                "saving   411.2 − 91.2  =  320.0 ms   =  4 round trips, exactly",
                "compare  halving the payload to 7 kB saves 5.6 ms",
            ],
            "after": [
                "The saving is four round trips and not one byte. That is the shape of "
                "almost every real first-load improvement, and it is why the protocol "
                "versions matter: moving from TLS 1.2 to 1.3 removes one round trip, "
                "which on this link is worth fourteen times what halving the document "
                "would be worth.",
                "The crossover payload is `k × bandwidth × RTT`. At `k = 5` on this link "
                "it is `500 kB`; at `k = 1` it is `100 kB`, which is the bandwidth-delay "
                "product from &ldquo;Latency Is Not Throughput&rdquo;. Removing "
                "handshakes therefore moves the crossover downward as well as moving the "
                "total: on a warm connection the payload starts mattering sooner.",
                "For a faded rehearsal, take a mobile connection at `150 ms` round trip "
                "and `5 Mbit/s`, fetching a `40 kB` JSON response over a cold TLS 1.3 "
                "connection with an uncached DNS entry. The supplied first move is the "
                "count: `1 + 1 + 1 + 1 = 4`. Compute the time to first byte, the byte "
                "term, the total and the ratio, then say what resuming the session would "
                "save and what halving the JSON would save. Check both figures in the lab "
                "before opening the quiz.",
            ],
        },
        "quiz_title": "Counting exchanges",
        "quiz": [
            {"q": "A cold connection uses DNS, TCP and TLS 1.3, then makes the request, at a `100 ms` round trip. What is the time to first byte?",
             "a": ["`100 ms`", "`300 ms`", "`400 ms`", "`500 ms`"],
             "c": 2,
             "why": "TLS 1.3 is one round trip, so `k = 1 + 1 + 1 + 1 = 4` and the time "
                    "to first byte is `400 ms`. `300 ms` forgets that the request itself "
                    "is a round trip. `500 ms` uses the TLS 1.2 count of two. `100 ms` "
                    "is one round trip, which is what a warm connection would pay."},
            {"q": "On the lab&rsquo;s preset &mdash; `k = 5`, `80 ms`, `14 kB`, `10 Mbit/s` &mdash; which change saves the most?",
             "a": ["Compressing the payload from `14 kB` to `7 kB`",
                   "Reusing an open connection, removing one round trip",
                   "Doubling the bandwidth to `20 Mbit/s`",
                   "Compressing the payload to `1 kB`"],
             "c": 1,
             "why": "One round trip is `80 ms`. Halving the payload saves `5.6 ms`; "
                    "cutting it to `1 kB` saves `10.4 ms`; doubling the bandwidth saves "
                    "`5.6 ms`. Even deleting the payload entirely saves only `11.2 ms`, "
                    "which is less than a seventh of one handshake &mdash; on this "
                    "request every byte-side option is dominated."},
            {"q": "At what payload do the bytes cost as much as the round trips, on that same preset?",
             "a": ["`14 kB`, the current payload", "`100 kB`", "`500 kB`", "`1 MB`"],
             "c": 2,
             "why": "The crossover is `k × bandwidth × RTT = 5 × 10 Mbit/s × 80 ms`, and "
                    "`10 Mbit/s × 80 ms` is `100 kB`, so the crossover is `500 kB`. "
                    "`100 kB` is the crossover for a single round trip &mdash; the "
                    "bandwidth-delay product &mdash; which is what one removed handshake "
                    "is worth in bytes. `1 MB` is the product for a different link entirely."},
        ],
        "mistakes": [
            ("Forgetting that the request itself is a round trip",
             "The handshakes get counted and the request does not, which leaves `k` one "
             "too small and the answer one round trip too fast. On a cold TLS 1.2 "
             "connection the count is five, not four, and on a warm one it is one, not "
             "zero &mdash; a warm connection still has to ask."),
            ("Counting messages instead of sequential exchanges",
             "A protocol trace shows many more packets than `k`. What matters is how "
             "many times one side has to wait for the other before it can continue. "
             "Work that overlaps with something else costs nothing here, and a count "
             "taken off a packet capture without asking what waited for what will be far "
             "too large."),
            ("Optimising bytes when the ratio says round trips",
             "On the preset the round trips cost `35.7` times the payload, so deleting "
             "the entire response would save `11.2 ms` against the `80 ms` a single "
             "removed handshake saves. Compute the ratio before choosing the work; it "
             "takes one division and it regularly reverses the decision."),
        ],
        "standard": ("Finish when “how big is the response?” is your second question rather than your first.",
                     "You should be able to count `k` for a described connection, compute "
                     "time to first byte and the byte term, express their ratio, and name "
                     "the crossover payload at which the two swap places."),
        "note": 'So far every stage has been in a line. Real requests fan out: the server asks several things at once and waits for the slowest, and &ldquo;Serial Sums, Parallel Maxes&rdquo; is how those compose &mdash; serial stages add, parallel stages take the maximum, and the end-to-end time is the longest path through the graph. The handshake cost counted here returns as a fixed line in &ldquo;Latency Budgets&rdquo;.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "serial-sums-parallel-maxes",
        "title": "Serial Sums, Parallel Maxes",
        "module": "The floors",
        "one_line": "Compute end-to-end latency through a stage graph, name the critical path, and read the slack on every stage off it.",
        "summary": (
            "Stages that run one after another add their times; stages that run beside "
            "each other take the maximum. Put both rules together and the end-to-end "
            "time is the longest path through the graph of stages. Every stage off that "
            "path has slack &mdash; room to grow before it changes anything &mdash; and "
            "the slack column is precisely the list of optimisations that will do nothing."
        ),
        "key": [
            "series      t = t₁ + t₂ + … + tₙ",
            "parallel    t = max(t₁, t₂, …, tₙ)",
            "end to end  = the longest path through the stage DAG",
            "slack       = latest start − earliest start;  0 means critical",
            "preset: stages total 120 ms, the longest path is 92 ms",
        ],
        "key_label": "Two composition rules, and what they make together",
        "concepts_intro": (
            "The hard idea is that end-to-end latency is a property of the graph, not of "
            "the list of stages. Two systems with identical stage times can differ by "
            "thirty percent on how the stages depend on one another."
        ),
        "concepts": [
            ("Series adds, parallel takes the maximum",
             "If B cannot start until A finishes, the pair costs `t_A + t_B`. If they "
             "run beside each other and both must finish, the pair costs "
             "`max(t_A, t_B)`. Those are the only two rules, and every stage graph is "
             "built from them &mdash; which is why a fan-out of ten fast calls and one "
             "slow one costs what the slow one costs."),
            ("The end-to-end time is the longest path",
             "Take every chain of stages from the entry to the exit and add the times "
             "along it. The request cannot finish before the longest of those chains "
             "does, and if nothing else is waiting it does not take longer. That chain "
             "is the <strong>critical path</strong>, and its length is the answer."),
            ("Slack is the list of optimisations that change nothing",
             "A stage&rsquo;s slack is how much longer it could take before the "
             "end-to-end time moves. A stage with slack can be made instantaneous and "
             "the answer stays where it was. On the preset, `enrich` has `33 ms` of "
             "slack: taking it from `22 ms` to `1 ms` leaves the total at `92 ms`, exactly."),
        ],
        "read_title": "The longest path, and everything that is not on it",
        "read_intro": "How to evaluate a stage graph by hand, and what the slack column is telling you to leave alone.",
        "body": [
            ("p", "The lab&rsquo;s preset is a request with seven stages. A `gateway` "
                  "takes `4 ms` and then two things start at once: `authz` at `18 ms` "
                  "and a `cache` lookup at `6 ms`. The `db` read at `55 ms` needs both "
                  "authorisation and the cache result; an `enrich` step of `22 ms` needs "
                  "only the authorisation. `render` at `12 ms` waits for the database "
                  "and the enrichment, and `respond` takes `3 ms`."),
            ("def", ("Critical path",
                     "In a graph of stages where an edge means &ldquo;must finish "
                     "before&rdquo;, the <strong>critical path</strong> is a longest path "
                     "from an entry stage to an exit stage, measured by the total of the "
                     "stage times along it. Its length is the end-to-end time. A stage on "
                     "a critical path has zero <strong>slack</strong>: any increase in "
                     "its time increases the end-to-end time by the same amount.")),
            ("p", "The stage times total `120 ms`, and that total is not the answer to "
                  "anything. Evaluate the graph instead, stage by stage in dependency "
                  "order, recording for each stage the earliest instant it could start "
                  "&mdash; which is the largest finishing time among the stages it waits "
                  "for."),
            ("math", [
                "stage      time   earliest start   earliest finish",
                "gateway      4          0                4",
                "authz       18          4               22",
                "cache        6          4               10",
                "enrich      22         22               44",
                "db          55         22               77       ← waits for authz and cache",
                "render      12         77               89       ← waits for db and enrich",
                "respond      3         89               92",
                "",
                "end to end  =  92 ms          sum of all stage times  =  120 ms",
                "critical path:  gateway → authz → db → render → respond",
            ]),
            ("p", "The `cache` lookup finished at `10 ms` but the database could not "
                  "start until `22 ms`, so twelve of those milliseconds were spent "
                  "waiting. That is the cache&rsquo;s slack. The enrichment finished at "
                  "`44 ms` and `render` did not start until `77 ms`, so the enrichment "
                  "has `33 ms` of slack. Everything else is critical."),
            ("ul", [
                "`gateway` `4 ms` &mdash; slack `0`, critical",
                "`authz` `18 ms` &mdash; slack `0`, critical",
                "`cache` `6 ms` &mdash; slack `12 ms`",
                "`enrich` `22 ms` &mdash; slack `33 ms`",
                "`db` `55 ms` &mdash; slack `0`, critical",
                "`render` `12 ms` &mdash; slack `0`, critical",
                "`respond` `3 ms` &mdash; slack `0`, critical",
            ]),
            ("h3", "Slack, and the trap on the other side of it"),
            ("p", "Drag the `enrich` slider from `22 ms` down to `1 ms` in the lab. The "
                  "end-to-end time stays at `92 ms`, because the enrichment was never "
                  "what `render` was waiting for. Now drag `respond` from `3 ms` to "
                  "`2 ms`: the total falls to `91 ms`, the whole millisecond, because "
                  "`respond` is critical. That is the difference the slack column is "
                  "describing, and it is the difference between a quarter of work that "
                  "shows up in the graphs and one that does not."),
            ("p", "The trap sits on the other side. Take the database from `55 ms` to "
                  "`45 ms` and the total falls from `92 ms` to `82 ms` &mdash; the full "
                  "`10 ms`. Keep going: at `22 ms` the total is `59 ms`, a saving of "
                  "`33 ms` for a `33 ms` improvement. Take it to `10 ms` and the total "
                  "is still `59 ms`. Below `22 ms` the database has stopped being "
                  "critical: the path through `enrich` has taken over, and further work "
                  "on the database buys nothing. Shortening a critical stage pays in "
                  "full only until the moment a second path becomes the longest one."),
            ("example", ("One added dependency, and what it costs",
                         "Set the `authz → cache` selector to present, so the cache "
                         "lookup waits for authorisation instead of running beside it. "
                         "Nothing got slower &mdash; every stage time is unchanged "
                         "&mdash; but the cache is now on the path and the end-to-end "
                         "time is `98 ms`. Set `enrich → db` to present instead, so the "
                         "database needs the enriched key: the total becomes `114 ms` "
                         "and the critical path reroutes through the enrichment. Two "
                         "edges, twenty-two milliseconds, no code made slower.")),
            ("p", "The evaluation above works because the stages were listed in an order "
                  "where every stage came after everything it waits for, so one pass "
                  "settled each stage&rsquo;s earliest start in turn. That is a real "
                  "algorithm with a real proof, and it is not this lesson&rsquo;s: "
                  "&ldquo;Shortest and Longest Paths in DAGs&rdquo; on the Algorithms "
                  "path derives the one-pass topological-order method and shows why a "
                  "single pass is enough. The graph here is small enough to evaluate by "
                  "reading it, which is the whole reason it is seven stages and not "
                  "seventy."),
            ("p", "The same longest path is a subject in its own right on a third path. "
                  "&ldquo;Project Networks and the Critical Path&rdquo; in Operations "
                  "Research computes earliest and latest start times, defines slack as "
                  "the difference, and calls a zero-slack activity critical &mdash; the "
                  "same three columns as the lab, on a schedule of work rather than a "
                  "request. Its misconception is the complement of this one: there, the "
                  "error is believing that shortening a critical activity shortens the "
                  "project by the same amount, which the `55 → 22 → 10` sequence above "
                  "refutes; here, the error is believing that shortening any stage helps "
                  "at all."),
        ],
        "lab": ("latency", {
            "mode": "dag",
            "panel_title": "Edit the stages and the dependencies",
            "panel_intro": "The critical path is recomputed from the stage times and the "
                           "two dependency selectors, and every stage&rsquo;s slack is "
                           "printed beside it. Try making a stage with slack instant "
                           "before you try making a critical stage faster.",
        }),
        "steps_title": "Evaluating a stage graph by hand",
        "steps_intro": "Forward once for the answer, backward once for the slack. Both passes are additions.",
        "steps": [
            ("List the stages so that every stage follows what it waits for",
             "Any such order will do and there is usually more than one. With the list "
             "in that order, a single forward pass is correct, because everything a "
             "stage depends on has already been settled when you reach it."),
            ("Go forward: earliest start is the largest finish among the predecessors",
             "Entry stages start at zero. For every other stage, take the finishing "
             "times of the stages it waits for and keep the largest &mdash; this is the "
             "max rule &mdash; then add its own time to get its finish. This is the "
             "parallel rule and the series rule applied one stage at a time."),
            ("Read the end-to-end time and trace the path back",
             "The answer is the largest finishing time. Walk backwards from it, each "
             "time to the predecessor whose finish was the one that set the start. That "
             "chain is the critical path."),
            ("Go backward for slack, and use it as a do-not-touch list",
             "Latest finish for the exit is the end-to-end time; for any other stage it "
             "is the earliest of its successors&rsquo; latest starts. Slack is latest "
             "start minus earliest start. Zero means critical; anything else is a stage "
             "whose speed-up will not appear in the total."),
        ],
        "worked": {
            "title": "The seven-stage request, forward and backward",
            "intro": [
                "The forward pass gives the answer. The backward pass gives the reason "
                "four of the seven optimisations available here are worthless."
            ],
            "lines": [
                "forward     ES = max finish of predecessors,   EF = ES + time",
                "",
                "  gateway     4    ES 0                    EF  4",
                "  authz      18    ES 4                    EF 22",
                "  cache       6    ES 4                    EF 10",
                "  enrich     22    ES max(22) = 22         EF 44",
                "  db         55    ES max(22, 10) = 22     EF 77",
                "  render     12    ES max(77, 44) = 77     EF 89",
                "  respond     3    ES 89                   EF 92",
                "",
                "end to end  92 ms",
                "",
                "backward    LF = min start of successors,    LS = LF − time",
                "",
                "  respond     LF 92   LS 89      slack 89 − 89 =  0    critical",
                "  render      LF 89   LS 77      slack 77 − 77 =  0    critical",
                "  db          LF 77   LS 22      slack 22 − 22 =  0    critical",
                "  enrich      LF 77   LS 55      slack 55 − 22 = 33",
                "  cache       LF 22   LS 16      slack 16 −  4 = 12",
                "  authz       LF 22   LS  4      slack  4 −  4 =  0    critical",
                "  gateway     LF  4   LS  0      slack  0 −  0 =  0    critical",
            ],
            "after": [
                "Two stages have slack and five do not, so five of the seven possible "
                "speed-ups are worth something and two are worth nothing at all. That is "
                "a decision made by arithmetic in under a minute, and it is the decision "
                "a profiler will not make for you: a profiler ranks stages by how long "
                "they take, and `enrich` at `22 ms` is the second-largest stage here and "
                "the least useful of all seven to improve.",
                "The slack numbers are also a budget. The cache lookup can grow from "
                "`6 ms` to `18 ms` before anything changes, and the enrichment from "
                "`22 ms` to `55 ms`. If a proposed change makes the enrichment twice as "
                "expensive but removes a database query, the slack column says the first "
                "half of that trade is free.",
                "For a faded rehearsal, set the `enrich → db` selector to present, so "
                "the database waits for the enrichment. The supplied first move is the "
                "new earliest start for `db`, which is now `max(22, 44) = 44`. Carry the "
                "forward pass through to `respond`, name the new critical path, and say "
                "which stage has just acquired slack and how much. Then check the four "
                "figures the lab prints against yours before opening the quiz.",
            ],
        },
        "quiz_title": "Paths and slack",
        "quiz": [
            {"q": "On the preset, `enrich` takes `22 ms` and has `33 ms` of slack. An engineer makes it instant. What is the new end-to-end time?",
             "a": ["`70 ms`", "`92 ms`", "`59 ms`", "`89 ms`"],
             "c": 1,
             "why": "It stays at `92 ms`. The enrichment finished at `44 ms` while "
                    "`render` was waiting for the database until `77 ms`, so removing it "
                    "entirely removes nothing from the path. `70 ms` subtracts the stage "
                    "time from the total, which is the error the slack column exists to "
                    "prevent. `59 ms` is what the total becomes when the database is cut "
                    "to `22 ms`, which is a different change."},
            {"q": "Three stages run in parallel, taking `10 ms`, `40 ms` and `15 ms`, and all three must finish. How long does the group take?",
             "a": ["`65 ms`", "`21.7 ms`", "`40 ms`", "`10 ms`"],
             "c": 2,
             "why": "Parallel stages take the maximum, so `40 ms`. `65 ms` is the sum, "
                    "which is the series rule applied to a parallel group. `21.7 ms` is "
                    "the mean, which is not a rule for anything here. `10 ms` is the "
                    "minimum, which would be right only if any one result sufficed."},
            {"q": "The database is critical at `55 ms`. It is optimised to `10 ms`. What happens to the `92 ms` total?",
             "a": ["It falls to `47 ms`, by the full `45 ms`",
                   "It falls to `59 ms`, and stops falling below `db = 22 ms`",
                   "It does not move, because the database has slack",
                   "It falls to `37 ms`, the sum of the remaining critical stages"],
             "c": 1,
             "why": "The saving is real but it runs out. At `db = 22 ms` the path through "
                    "`enrich` &mdash; which had `33 ms` of slack &mdash; becomes the "
                    "longest one, and the total sticks at `59 ms` however much further "
                    "the database improves. Shortening a critical stage pays in full only "
                    "until a second path takes over, which is why slack is worth "
                    "recomputing after every change."},
        ],
        "mistakes": [
            ("Adding the stage times",
             "The preset&rsquo;s seven stages total `120 ms` and the request takes "
             "`92 ms`. The sum is an upper bound that is reached only when nothing runs "
             "in parallel, and quoting it as the latency overstates by whatever the "
             "parallelism was worth &mdash; here, thirty percent."),
            ("Optimising the largest stage rather than a critical one",
             "Size and criticality are different properties. `enrich` at `22 ms` is the "
             "second-largest stage on the preset and contributes nothing; `respond` at "
             "`3 ms` is the smallest and every millisecond of it is real. Rank by slack, "
             "not by duration."),
            ("Adding a dependency without noticing it is a latency change",
             "Making the cache lookup wait for authorisation costs `6 ms` of end-to-end "
             "time while making no individual stage slower. Changes like this arrive as "
             "refactors, correctness fixes or simplifications, and they never appear in "
             "a profile as a regression in any one stage."),
        ],
        "standard": ("Finish when you look for the path before you look for the biggest number.",
                     "You should be able to evaluate a stage graph forward for the "
                     "end-to-end time, name the critical path, compute the slack on every "
                     "other stage, and predict both what a speed-up on a given stage buys "
                     "and the point at which it stops buying anything."),
        "note": 'Every stage time so far has been a single number, as if a stage always took exactly that long. It does not: it has a distribution, and the interesting part of that distribution is its tail. &ldquo;Percentiles from a Sample&rdquo; makes the tail into an object you can compute with, and &ldquo;Percentiles Do Not Add&rdquo; returns to this lesson&rsquo;s series rule to show that it survives for means and fails for percentiles.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "percentiles-from-a-sample",
        "title": "Percentiles from a Sample",
        "module": "The tail",
        "one_line": "Compute p50, p95 and p99 of a sample exactly by rank, and say what the mean is and is not about.",
        "summary": (
            "A percentile is a position in a sorted list, not an average: the p99 is the "
            "`⌈0.99n⌉`-th value, which means it is a time some request actually took. "
            "The mean is a different kind of number about a different question, and on a "
            "latency sample it is usually a value no request came close to. Computing "
            "both on the same twenty measurements is what makes the difference stop "
            "being a slogan."
        ),
        "key": [
            "rank    r = ⌈q · n⌉             q the percentile, n the sample size",
            "p_q     the r-th smallest value  a value some request actually took",
            "n = 20  p50 = 19 ms   p95 = 180 ms   p99 = 420 ms",
            "mean    266/5 = 53.2 ms           and 17 of the 20 are faster than it",
            "no request in the sample took 53 ms",
        ],
        "key_label": "A percentile is a rank; a mean is an average",
        "concepts_intro": (
            "One idea, and it is a definition: `p99` names a position in a sorted list. "
            "Everything that makes percentiles behave strangely later follows from that "
            "and not from anything statistical."
        ),
        "concepts": [
            ("A percentile is selected by rank",
             "Sort the sample. Compute `r = ⌈q · n⌉`. Take the `r`-th value. For "
             "`q = 0.99` and `n = 20` that is `⌈19.8⌉ = 20`, so the p99 is the twentieth "
             "of twenty values. No arithmetic is done on the numbers themselves &mdash; "
             "they are only compared &mdash; which is why the answer is always a "
             "measurement rather than a construction."),
            ("The mean answers a different question",
             "The mean of this sample is `53.2 ms`, and `17` of the `20` requests were "
             "faster than that. It is not a typical experience and it is not meant to "
             "be: the mean times the count is the total time spent, which is the right "
             "number for capacity and cost and the wrong number for describing what a "
             "user saw."),
            ("A small sample cannot support a high percentile",
             "With `n = 20` the rank for `q = 0.99` is `20`, so the p99 of this sample "
             "<em>is</em> its maximum &mdash; one measurement, carrying the whole claim. "
             "A percentile is only as trustworthy as the number of observations beyond "
             "it, and `1/n` is the finest resolution a sample of size `n` has."),
        ],
        "read_title": "Ranks, and the average that is nobody",
        "read_intro": "The definition, then the same twenty numbers read four different ways.",
        "body": [
            ("def", ("Nearest-rank percentile",
                     "For a sample of `n` values sorted ascending and a fraction `q` "
                     "between `0` and `1`, the <strong>`q`-th percentile by nearest "
                     "rank</strong> is the value at position `r = ⌈q · n⌉`. It is one of "
                     "the observed values, always. Other definitions exist that "
                     "interpolate between neighbours and can return a number nobody "
                     "measured; this course uses nearest rank throughout and prints the "
                     "rank beside the value.")),
            ("p", "The lab&rsquo;s preset is twenty measurements in milliseconds, "
                  "already sorted: `12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, "
                  "27, 31, 38, 52, 96, 180, 420`. The ranks are the whole computation."),
            ("math", [
                "n = 20",
                "",
                "p50    r = ⌈0.50 × 20⌉ = ⌈10.0⌉ = 10      10th value  =  19 ms",
                "p90    r = ⌈0.90 × 20⌉ = ⌈18.0⌉ = 18      18th value  =  96 ms",
                "p95    r = ⌈0.95 × 20⌉ = ⌈19.0⌉ = 19      19th value  = 180 ms",
                "p99    r = ⌈0.99 × 20⌉ = ⌈19.8⌉ = 20      20th value  = 420 ms",
                "",
                "mean   (12 + 13 + … + 420) / 20  =  1064 / 20  =  266/5  =  53.2 ms",
            ]),
            ("p", "Four numbers describing one sample: `19`, `96`, `180`, `420`. The "
                  "median is `19 ms` and the p99 is twenty-two times that. A single "
                  "summary figure cannot carry that spread, and choosing which single "
                  "figure to carry is the decision this lesson is about."),
            ("h3", "Why the mean cannot be repaired"),
            ("p", "The mean is `53.2 ms`. Seventeen of the twenty requests were faster "
                  "than the mean, and no request in the sample took anything near "
                  "`53 ms` &mdash; the values on either side of it are `52` and `96`. "
                  "The mean has landed in a gap. This is not a defect of this sample; it "
                  "is what happens to an average whenever a few large values are pulled "
                  "far out, which is the normal shape of a latency distribution."),
            ("example", ("“The average user sees 53 ms”",
                         "No user saw `53 ms`. The claim, read as a claim about a "
                         "typical experience, is false in this sample by construction: "
                         "`85%` of the requests were faster and `15%` were much slower, "
                         "and the number in the middle belongs to neither group. What is "
                         "true of the mean is that twenty requests consumed "
                         "`20 × 53.2 = 1064 ms` of service time in total &mdash; a fact "
                         "about load, which is exactly what a capacity calculation needs "
                         "and exactly what a latency report does not.")),
            ("p", "Notice what removing one measurement does. Delete the `420` from the "
                  "sample in the lab and the p99 of the remaining nineteen becomes "
                  "`180 ms`, less than half of what it was, because at `n = 19` the "
                  "rank `⌈0.99 × 19⌉ = 19` now selects the new maximum. A high "
                  "percentile of a small sample is a claim resting on one or two "
                  "observations, and moving one of them moves the answer by a factor of "
                  "two. The fix is more measurements, not a different formula."),
            ("p", "The rank definition also says something about how the value is found. "
                  "Sorting is the obvious method and it is what the lab shows, because "
                  "seeing the sorted list is the point. It is not the only method: "
                  "&ldquo;Quickselect&rdquo; on the Algorithms path finds the `r`-th "
                  "smallest value without sorting the rest, which is how a system with "
                  "millions of measurements a second computes the same number. The "
                  "definition does not change; only the work does."),
        ],
        "lab": ("latency", {
            "mode": "percentile",
            "panel_title": "Edit the sample",
            "panel_intro": "The sorted list, the computed rank and the value that rank "
                           "selects are shown together, with the mean marked against "
                           "them. Add one very large measurement and watch which of the "
                           "four figures move.",
        }),
        "steps_title": "Reading a percentile off a sample",
        "steps_intro": "Do this by hand once. It is four steps and it permanently changes how the word p99 reads.",
        "steps": [
            ("Sort the sample ascending",
             "Every step after this is a position in that list. If the sample arrived as "
             "a stream of numbers this is the only part that costs anything, and it is "
             "also the part that makes the rest obviously correct."),
            ("Compute the rank `r = ⌈q · n⌉`",
             "Round up, always: `⌈0.99 × 20⌉ = 20` and `⌈0.99 × 200⌉ = 198`. Rounding "
             "down or to nearest gives a neighbouring value, which on a tail can be very "
             "different from the right one."),
            ("Take the `r`-th value and report it as a measurement",
             "It is a time some request actually took. Say which one it is if the sample "
             "is small &mdash; &ldquo;the p99 is the slowest of twenty&rdquo; is a more "
             "honest sentence than &ldquo;the p99 is 420 ms&rdquo; when both are the "
             "same fact."),
            ("Compute the mean too, and use it only for totals",
             "The mean times the count is the total service time, which is what capacity "
             "and cost are made of. Do not report it as an experience, and check how "
             "many observations fall below it &mdash; on a latency sample the answer is "
             "usually most of them."),
        ],
        "worked": {
            "title": "Twenty measurements, four summaries",
            "intro": [
                "The sample is small enough to count on your fingers, which is the "
                "point: everything here is a position, and the positions can be checked."
            ],
            "lines": [
                "sorted   12  13  14  14  15  15  16  17  18  19",
                "         21  22  24  27  31  38  52  96 180 420",
                "position  1   2   3   4   5   6   7   8   9  10",
                "         11  12  13  14  15  16  17  18  19  20",
                "",
                "p50   r = ⌈0.50 × 20⌉ = 10        →   19 ms",
                "p90   r = ⌈0.90 × 20⌉ = 18        →   96 ms",
                "p95   r = ⌈0.95 × 20⌉ = 19        →  180 ms",
                "p99   r = ⌈0.99 × 20⌉ = 20        →  420 ms",
                "",
                "mean  1064 / 20  =  53.2 ms",
                "      values below 53.2:  17 of 20   (85%)",
                "      values equal to 53:  none",
                "",
                "p99 / p50  =  420 / 19  =  22.1 ×",
            ],
            "after": [
                "The `22.1×` ratio at the bottom is the shape of the distribution in one "
                "number, and it is the figure that makes the rest of this course "
                "necessary. A system whose p99 is twenty-two times its median does not "
                "have a latency problem in any stage; it has a tail, and the tail is a "
                "separate object with its own arithmetic.",
                "It is worth noticing that the p50 and the mean disagree by nearly a "
                "factor of three, in the direction they always disagree: the mean is "
                "above the median whenever the large values are the far ones. If a "
                "system reports a mean close to its median, either the tail is unusually "
                "tame or something is truncating the measurements &mdash; which is its "
                "own subject, and belongs to Measuring Systems.",
                "For a faded rehearsal, take the eleven measurements "
                "`5, 6, 6, 7, 8, 9, 11, 14, 20, 60, 300`. The supplied first move is the "
                "size: `n = 11`. Compute the ranks and the values for p50, p90 and p99, "
                "then the mean, then count how many observations are below the mean. Say "
                "which single observation the p99 rests on, and type the sample into the "
                "lab to check every figure before opening the quiz.",
            ],
        },
        "quiz_title": "Ranks and averages",
        "quiz": [
            {"q": "A sorted sample has `n = 200` values. Which position is the p99?",
             "a": ["The 198th", "The 199th", "The 2nd from the end", "The 99th"],
             "c": 0,
             "why": "`⌈0.99 × 200⌉ = ⌈198⌉ = 198`, so it is the 198th value &mdash; "
                    "which is the third from the end, not the second. `199` comes from "
                    "adding one to a rank that did not need rounding up. `99` reads the "
                    "percentile as a position directly, which happens to be the median "
                    "region of this sample."},
            {"q": "On the lab&rsquo;s preset, the mean is `53.2 ms` and the median is `19 ms`. What follows?",
             "a": ["The sample is corrupt, since a mean should be near a median",
                   "A few large values are pulling the mean up, and most requests are faster than the mean",
                   "The median was computed with the wrong rank",
                   "The distribution is symmetric around `36 ms`"],
             "c": 1,
             "why": "`17` of the `20` observations are below `53.2 ms`; the `96`, `180` "
                    "and `420` carry the mean upward on their own. This is the normal "
                    "shape of a latency sample, not a defect. The median&rsquo;s rank is "
                    "`⌈0.5 × 20⌉ = 10`, which is correct, and a symmetric distribution is "
                    "precisely what this is not."},
            {"q": "A service reports a p99 from a sample of `50` requests. What is the strongest honest reading?",
             "a": ["The p99 is accurate to within one percent",
                   "The p99 is the 50th value &mdash; the slowest of the fifty &mdash; and rests on that one observation",
                   "The p99 cannot be computed from fewer than 100 samples",
                   "The p99 equals the mean of the top one percent"],
             "c": 1,
             "why": "`⌈0.99 × 50⌉ = 50`, so the p99 is the maximum of the sample and one "
                    "measurement carries it. It can be computed &mdash; the rank is "
                    "well defined at any `n` &mdash; but the resolution of a sample of "
                    "`50` is `1/50`, so a figure quoted at the `1/100` level is finer "
                    "than the data supports. The mean of the top one percent is a "
                    "different statistic entirely."},
        ],
        "mistakes": [
            ("Calling the p99 an average of the slow requests",
             "It is one observation, selected by position. It is not the mean of the "
             "worst one percent, and it is not an average of anything. The distinction "
             "matters as soon as percentiles are combined, because averages compose in "
             "ways that ranks do not."),
            ("Rounding the rank down or to nearest",
             "`⌈0.99 × 20⌉` is `20`, not `19`. On this sample rounding down returns "
             "`180 ms` instead of `420 ms`, an error of a factor of two and a third. "
             "The ceiling is part of the definition and it is exactly what stops the "
             "percentile from being a value below which fewer than `q` of the sample sits."),
            ("Reporting the mean as what a typical user experiences",
             "On the preset, `85%` of requests were faster than the mean and none took "
             "the mean. The mean is the right number for total work and the wrong number "
             "for a typical experience, and the two get confused because both are "
             "described with the word &ldquo;average&rdquo;."),
        ],
        "standard": ("Finish when you reach for a sorted list rather than a formula.",
                     "You should be able to compute a rank, select the value it names, "
                     "compute the mean of the same sample, count how many observations "
                     "fall below it, and state how many observations the reported "
                     "percentile actually rests on."),
        "note": 'A percentile of one call is now a computable object, which makes the rest of this course possible. &ldquo;Tail Amplification under Fan-out&rdquo; asks what happens when a request has to wait for many calls that each sit inside their own p99, and the answer &mdash; that at sixty-nine of them the p99 has become the median &mdash; is the result this course exists to establish.',
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "tail-amplification-under-fan-out",
        "title": "Tail Amplification under Fan-out",
        "module": "The tail",
        "one_line": "Compute the slow-request probability for a fan-out of n calls, and find the n at which a per-call p99 becomes the request’s median.",
        "summary": (
            "A request that fans out to `n` independent backends and waits for all of "
            "them is fast only if every one of them is fast. If each call is inside its "
            "own p99 with probability `0.99`, then all `n` are with probability "
            "`0.99ⁿ`. That is `0.499837` at `n = 69`: a service with a fan-out of "
            "sixty-nine misses its per-call p99 on most requests, and nothing anywhere "
            "in it is broken."
        ),
        "key": [
            "P(all n calls ≤ their p99)  =  0.99ⁿ        under independence",
            "P(at least one slow)        =  1 − 0.99ⁿ",
            "n = 69   0.99⁶⁹ = 0.499837                 a p99 has become the median",
            "n = 10   9.56% slow      n = 100   63.40% slow",
            "break-even n:  p90 → 7    p95 → 14    p99 → 69    p99.9 → 693",
        ],
        "key_label": "One multiplication, repeated n times",
        "concepts_intro": (
            "The hard idea is a single exponent, and the reason it is hard is that the "
            "arithmetic is trivial and the conclusion is not one most people will "
            "believe before seeing it."
        ),
        "concepts": [
            ("Waiting for all of them means every one must be fast",
             "A request that issues `n` calls in parallel and needs all the answers "
             "finishes when the slowest returns. So &ldquo;this request was fast&rdquo; "
             "is the conjunction of `n` separate statements, and a conjunction of "
             "independent events multiplies: `p × p × … × p = pⁿ`."),
            ("`0.99ⁿ` reaches one half at `n = 69`",
             "`0.99⁶⁹ = 0.499837`, just under a half, and `0.99⁶⁸ = 0.504886`, just "
             "over. So at a fan-out of sixty-nine, more than half of all requests "
             "contain at least one call outside its p99. The per-call p99 is now the "
             "whole request&rsquo;s median, which is a statement about arithmetic rather "
             "than about anything being wrong."),
            ("The break-even `n` is set by the per-call percentile",
             "A p90 per call breaks even at `n = 7`, a p95 at `n = 14`, a p99 at "
             "`n = 69` and a p99.9 at `n = 693`. Each step of a factor of ten in the "
             "per-call tail buys roughly a factor of ten in the fan-out you can afford, "
             "which is the only lever there is apart from not fanning out."),
        ],
        "read_title": "One multiplication, and what it does to a fan-out",
        "read_intro": "The exponent, the number sixty-nine, and the assumption the whole thing rests on.",
        "body": [
            ("p", "A search page assembles itself from many services: one for results, "
                  "one for advertisements, one for spelling, one for each of several "
                  "personalisation signals, and a shard of the index for each partition "
                  "of the corpus. They run in parallel, which is the right design "
                  "&mdash; by the max rule of &ldquo;Serial Sums, Parallel Maxes&rdquo; "
                  "the group costs what the slowest member costs rather than the sum. "
                  "The question is what the slowest member costs."),
            ("thm", ("Fan-out amplification",
                     "Let a request issue `n` calls that are independent, and let each "
                     "call complete within its own `q`-th percentile with probability "
                     "`p = q`. Then the probability that every call is inside its "
                     "percentile is `pⁿ`, and the probability that at least one is "
                     "outside it is `1 − pⁿ`.",
                     "The `n` at which `pⁿ = ½` is the fan-out width at which the "
                     "per-call `q`-th percentile has become the whole request&rsquo;s "
                     "median: half of all requests contain a call beyond it.")),
            ("p", "The proof is one line &mdash; independent events multiply &mdash; and "
                  "the content is entirely in the numbers it produces."),
            ("math", [
                "p = 0.99",
                "",
                "n =   1     0.99¹   = 0.990000        1.00% of requests contain a slow call",
                "n =  10     0.99¹⁰  = 0.904382        9.56%",
                "n =  50     0.99⁵⁰  = 0.605006       39.50%",
                "n =  68     0.99⁶⁸  = 0.504886       49.51%",
                "n =  69     0.99⁶⁹  = 0.499837       50.02%   ← the break-even",
                "n = 100     0.99¹⁰⁰ = 0.366032       63.40%",
                "n = 200     0.99²⁰⁰ = 0.133980       86.60%",
            ]),
            ("p", "Read the `n = 100` row slowly. Every backend is meeting its latency "
                  "objective, every dashboard is green, nobody is paged &mdash; and "
                  "`63.40%` of requests are waiting on a call that is outside the "
                  "objective. There is no failure here to find, because there is no "
                  "failure. The system is doing exactly what it was specified to do."),
            ("h3", "What it takes to move the number"),
            ("ul", [
                "a per-call p90 breaks even at `n = 7`",
                "a per-call p95 breaks even at `n = 14`",
                "a per-call p99 breaks even at `n = 69`",
                "a per-call p99.9 breaks even at `n = 693`",
            ]),
            ("p", "Those four rows are the whole strategy space. Reduce the fan-out, or "
                  "push the per-call tail down by a factor of ten to buy a factor of ten "
                  "in width, or stop requiring every answer &mdash; a request that can "
                  "return with nine of ten results has changed the conjunction and is no "
                  "longer in this arithmetic at all. There is also the option "
                  "&ldquo;Hedged Requests&rdquo; takes, which is to change the per-call "
                  "tail without changing the per-call service."),
            ("example", ("Two hundred shards at a p99.9",
                         "Push every call to a p99.9 &mdash; an expensive, real "
                         "engineering achievement &mdash; and the break-even moves to "
                         "`n = 693`. At a fan-out of `200` the probability that every "
                         "call is inside its p99.9 is `0.999²⁰⁰`, about `0.819`, so "
                         "`18%` of requests still contain a slow call. That is a far "
                         "better place to be than the `86.60%` the same fan-out gives at "
                         "a p99, and it is not zero and never will be.")),
            ("p", "Everything above assumes independence, and it is worth being precise "
                  "about which direction reality departs from it. Real slowness has "
                  "shared causes: a garbage-collection pause on a host that several "
                  "calls land on, a saturated switch, a hot shard. Shared causes make "
                  "slow calls arrive together, so <em>fewer</em> requests contain a slow "
                  "call than `1 − pⁿ` predicts &mdash; and the ones that do contain "
                  "several. Independence is the assumption that spreads the damage as "
                  "thinly and as widely as possible, and the real distribution is "
                  "lumpier than it."),
            ("p", "The misconception to name is the comfortable one: &ldquo;each call is "
                  "fast at its p99, so the request is.&rdquo; The premise is about one "
                  "call and the conclusion is about `n` of them, and the step between "
                  "them is a multiplication that nobody performs because it does not "
                  "look like there is anything to compute."),
        ],
        "lab": ("latency", {
            "mode": "fanout",
            "panel_title": "Set the fan-out",
            "panel_intro": "The curve and the break-even `n` are computed exactly &mdash; "
                           "`0.99⁶⁹` is a fraction with a hundred and thirty-eight digits "
                           "in it, and the panel prints its decimal rather than a "
                           "floating-point approximation of it. Move the width first, "
                           "then change the per-call percentile.",
        }),
        "steps_title": "Sizing a fan-out",
        "steps_intro": "Four steps, and the third is the one that turns a design review around.",
        "steps": [
            ("Count the calls the request waits for",
             "Only the ones it needs before it can answer. A call whose result is "
             "optional, or one that is fired and forgotten, is not in `n`. Shards count "
             "individually: a query against forty partitions is a fan-out of forty."),
            ("Raise the per-call percentile to that power",
             "`pⁿ` is the probability that every call is inside its percentile. "
             "`1 − pⁿ` is the probability that the request contains at least one that "
             "is not, which is the number worth quoting to anyone."),
            ("Find the `n` at which `pⁿ` falls to a half",
             "That is the width at which the per-call percentile has become the "
             "request&rsquo;s median. Compare it with the fan-out you actually have; if "
             "yours is larger, the per-call objective is no longer describing your users&rsquo; experience."),
            ("Choose among the three levers, or change the question",
             "Reduce `n`, reduce the per-call tail by a factor of ten per factor of ten "
             "in width, or stop waiting for every answer. If none is available, the "
             "remaining move is to hedge, which buys tail without buying service."),
        ],
        "worked": {
            "title": "A fan-out of 100 at a per-call p99",
            "intro": [
                "A hundred shards, each meeting a p99 objective, and a request that "
                "needs all hundred answers."
            ],
            "lines": [
                "per call    p = 0.99      (each call is inside its p99 with prob 0.99)",
                "fan-out     n = 100",
                "",
                "P(all fast)     = 0.99¹⁰⁰  =  0.366032",
                "P(one or more slow) = 1 − 0.366032  =  0.633968   →  63.40%",
                "",
                "where is the break-even?",
                "        0.99⁶⁸ = 0.504886   > ½",
                "        0.99⁶⁹ = 0.499837   < ½     →  n = 69",
                "",
                "so at n = 100 the request is well past the point at which",
                "the per-call p99 became the request's median.",
                "",
                "what would fix it?",
                "        n → 69 at p99        still half the requests",
                "        p → 0.999 at n = 100    0.999¹⁰⁰ = 0.904792  →  9.52% slow",
                "        stop needing all 100 answers   → different arithmetic entirely",
            ],
            "after": [
                "The third option is the one that gets used in practice, and it is worth "
                "seeing why it is not a cheat. Returning with ninety-five of a hundred "
                "shard results changes the event whose probability is being computed: "
                "the request no longer needs a conjunction of a hundred statements, so "
                "there is no `pⁿ` to compute. The cost is an answer that is slightly "
                "incomplete, and the whole design question is whether anyone can tell.",
                "It is also worth noticing how little the second option buys per unit of "
                "effort. Moving every call from a p99 to a p99.9 is an order-of-magnitude "
                "reduction in the tail, and at `n = 100` it takes the slow-request rate "
                "from `63.40%` to `9.52%` &mdash; a real improvement, and still not a "
                "number anyone would put on a slide.",
                "For a faded rehearsal, take a fan-out of `40` with a per-call p95. The "
                "supplied first move is the break-even for a p95, which the lab prints "
                "as `n = 14`. Say whether `40` is past it, compute `0.95⁴⁰` and the "
                "slow-request probability, then say which of the lab&rsquo;s four per-call "
                "percentiles brings that probability under ten percent at the same "
                "width. Check each figure in the lab before opening the quiz.",
            ],
        },
        "quiz_title": "Fan-out arithmetic",
        "quiz": [
            {"q": "Each of `10` independent calls completes inside its p99 with probability `0.99`. What fraction of requests contain at least one slow call?",
             "a": ["`1%`", "`about 9.6%`", "`10%`", "`about 90%`"],
             "c": 1,
             "why": "`0.99¹⁰ = 0.904382`, so `1 − 0.904382 = 0.095618`, about `9.56%`. "
                    "`1%` is the per-call figure, unchanged by the fan-out. `10%` is "
                    "`10 × 1%`, which is the right instinct and slightly too large "
                    "because it double-counts requests with more than one slow call. "
                    "`90%` inverts the answer."},
            {"q": "At what fan-out does a per-call p99 become the whole request&rsquo;s median?",
             "a": ["`n = 50`", "`n = 68`", "`n = 69`", "`n = 100`"],
             "c": 2,
             "why": "`0.99⁶⁸ = 0.504886`, still above a half, and `0.99⁶⁹ = 0.499837`, "
                    "below it &mdash; so `69` is the first width at which most requests "
                    "contain a slow call. `68` is the last width at which most do not, "
                    "and the off-by-one is the whole content of the question. At `n = 50` "
                    "the figure is `39.50%` and at `n = 100` it is `63.40%`."},
            {"q": "A service fans out to `200` shards and reports that every shard meets its p99. Which statement is supported?",
             "a": ["The request meets the p99 too",
                   "About `86.6%` of requests wait on at least one call outside its p99",
                   "The shards must be violating their objective, since users report slowness",
                   "The p99 of the request is `200` times the p99 of a shard"],
             "c": 1,
             "why": "`0.99²⁰⁰ = 0.133980`, so `86.60%` of requests contain a slow call, "
                    "with nothing failing anywhere. The first option is the misconception "
                    "exactly. The third looks for a fault that does not exist. The fourth "
                    "multiplies a percentile by a count, and percentiles do not compose "
                    "by arithmetic on the percentile at all."},
        ],
        "mistakes": [
            ("Reasoning from one call to the request",
             "&ldquo;Each call is fast at its p99&rdquo; is a statement about one call. "
             "&ldquo;The request is fast&rdquo; requires all `n` to be, and the step "
             "between them is `pⁿ`. It is invisible because there is no obvious place in "
             "the sentence where a multiplication belongs."),
            ("Adding the per-call tail probabilities",
             "`n × 1%` is close for small `n` and wrong for large: at `n = 10` it gives "
             "`10%` against the true `9.56%`, and at `n = 200` it gives `200%`. It "
             "overstates because it counts a request with two slow calls twice. `1 − pⁿ` "
             "is the figure, and it never exceeds one."),
            ("Forgetting that independence is an assumption, and which way it fails",
             "Shared causes make slow calls cluster, so fewer requests are affected than "
             "`1 − pⁿ` says and the affected ones are worse. `1 − pⁿ` is therefore the "
             "widest-spread case rather than the worst case, and a system whose slow "
             "requests arrive in bursts is telling you the calls were never independent."),
        ],
        "standard": ("Finish when a fan-out width makes you reach for an exponent.",
                     "You should be able to compute `pⁿ` and `1 − pⁿ` for a described "
                     "fan-out, locate the break-even `n` for a given per-call percentile, "
                     "and say which of the three levers &mdash; width, per-call tail, or "
                     "not waiting for everything &mdash; a particular system has available."),
        "note": 'The fan-out made the tail worse by composing independent calls. &ldquo;Hedged Requests&rdquo; composes two independent copies of the same call and makes the tail better by the same mechanism, squaring a tail probability instead of raising a success probability to a power. The two labs are worth reading in one sitting: they are one fact about independence, pointed in opposite directions.',
    },
]
