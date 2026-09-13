"""Course 3, lessons 01-07 - rates, Little's Law, bunching, the two limit distributions, M/M/1."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "arrival-rate-service-rate-utilisation",
        "title": "λ, μ and ρ",
        "module": "Rates and Little's Law",
        "one_line": "Compute ρ from an arrival rate and a service time, and give the growth rate when ρ reaches one.",
        "summary": (
            "Three symbols carry the whole course. `λ` is how fast work arrives, `μ` is how "
            "fast one server finishes it, and `ρ = λ/μ` is the fraction of the time that "
            "server is busy. The trap is the middle one: `μ` is a rate and not a duration, "
            "so a service taking 2 ms has `μ = 500` per second."
        ),
        "key": [
            "λ         arrivals per second           a rate",
            "S         mean service time             a duration",
            "μ = 1/S   services per second           S = 2 ms gives μ = 500/s",
            "ρ = λ/μ   utilisation                   a pure number; the seconds cancel",
            "ρ ≥ 1     nothing settles               the backlog grows at λ − μ, for ever",
        ],
        "key_label": "Two rates, one duration, and the ratio they make",
        "concepts_intro": (
            "One of these three symbols is a rate written as the reciprocal of a duration, and "
            "most of the confusion on this course starts there."
        ),
        "concepts": [
            ("`μ` is a rate; `S` is the duration",
             "A request that takes `S = 1` ms is served at `μ = 1000` per second, not at "
             "`μ = 1`. The two are reciprocals, `μ = 1/S`, and they are never "
             "interchangeable. When `S` is quoted in milliseconds the conversion carries a "
             "thousand with it: `μ = 1000/S`."),
            ("`ρ` is a fraction of a server, not a speed",
             "`ρ = λ/μ` divides a rate by a rate, so the seconds cancel and what is left is a "
             "pure number: the fraction of time the one server is busy. At `ρ = 4/5` it works "
             "four seconds in every five and is idle the fifth, and that idle fifth is the "
             "only thing a burst has to land in."),
            ("Above `ρ = 1` there is nothing to average",
             "Every closed form later in this course divides by `1 − ρ`, and at `ρ ≥ 1` that "
             "is zero or negative because there is no settled queue length to report. What "
             "there is instead is a slope: work accumulates at `λ − μ` a second and keeps "
             "doing it until something changes."),
        ],
        "read_title": "Rates, reciprocals, and the ratio between them",
        "read_intro": "What each symbol is, what it is measured in, and what changes at ρ = 1.",
        "body": [
            ("def", ("Arrival rate, service time, service rate",
                     "The <strong>arrival rate</strong> `λ` is the mean number of arrivals "
                     "per unit time. The <strong>mean service time</strong> `S` is how long "
                     "one server takes over one job. The <strong>service rate</strong> "
                     "`μ = 1/S` is how many jobs that server can finish per unit time when "
                     "it never waits for work.")),
            ("p", "Both `λ` and `μ` are rates and `S` is a duration. Keeping that straight is "
                  "the whole of this lesson, because the two quantities a designer is handed "
                  "are usually a rate (requests per second, from a dashboard) and a duration "
                  "(a service time in milliseconds, from a trace), and they cannot be divided "
                  "until one of them has been turned into the other's kind."),
            ("example", ("A 1 ms service under 800 requests a second",
                         "`S = 1` ms is `1/1000` of a second, so `μ = 1000` per second. Then "
                         "`ρ = 800/1000 = 4/5`: the server is busy four fifths of the time. "
                         "It is not 800 times too slow and it is not running at 800; it has "
                         "a fifth of itself spare.")),
            ("def", ("Utilisation",
                     "The <strong>utilisation</strong> `ρ = λ/μ` is the long-run fraction of "
                     "time a single server is busy. It is dimensionless: a rate divided by a "
                     "rate. Equivalently it is the <strong>offered load</strong> measured in "
                     "servers &mdash; `ρ = 4/5` says the work offered would keep four fifths "
                     "of one server occupied.")),
            ("math", [
                "λ = 800 / s          S = 1 ms = 1/1000 s",
                "",
                "μ = 1/S  = 1000 / s",
                "ρ = λ/μ  = 800/1000 = 4/5          busy 4 s in every 5",
                "1 − ρ    = 1/5                     the headroom a burst lands in",
            ]),
            ("p", "Doubling the service time halves `μ`, and `ρ` doubles with it. This is the "
                  "cheapest sensitivity on the course and the one most often missed: nothing "
                  "about the offered traffic has to change for a system to cross `ρ = 1`. A "
                  "slower dependency, a larger payload, a colder cache &mdash; each of them "
                  "moves `μ` and therefore moves `ρ`."),
            ("example", ("The same 800 requests a second into a 2 ms service",
                         "`S = 2` ms gives `μ = 500` per second, so `ρ = 800/500 = 8/5`. The "
                         "load did not change. The service time did, and that was enough to "
                         "put the system above one.")),
            ("h3", "What ρ ≥ 1 actually means"),
            ("p", "At `ρ ≥ 1` work arrives at least as fast as it can be finished, so the "
                  "amount waiting has no long-run average at all. It grows at `λ − μ` per "
                  "second for as long as the condition lasts. That is a straight line, not a "
                  "queue, and quoting a queue length for it is the first mistake this course "
                  "can catch."),
            ("math", [
                "λ = 1200 / s        μ = 1000 / s",
                "",
                "λ − μ = 200 / s                    the line's slope",
                "after one minute    200 × 60    = 12 000 waiting",
                "after one hour      200 × 3600  = 720 000 waiting",
            ]),
            ("p", "Below one the queue does settle, and the rest of this course is about what "
                  "it settles at. The one thing to carry forward from here is that `ρ` is the "
                  "input to all of it: every later formula is a function of `ρ` alone, and the "
                  "closer `ρ` is to one the more violently that function moves."),
        ],
        "lab": ("queue", {
            "mode": "rates",
            "preset": "eighty-percent",
            "panel_title": "Set the load and the service time",
            "panel_intro": "Move the arrival rate and the service time and watch `μ`, `ρ` and "
                           "the growth rate follow as exact fractions. Push the service time "
                           "up without touching the load and find the point where the system "
                           "stops settling.",
        }),
        "steps_title": "Turning a service time into a utilisation",
        "steps_intro": "Four lines of arithmetic, of which the second is the one that goes wrong.",
        "steps": [
            ("Write the service time down with its unit",
             "`S = 2` ms, not `S = 2`. Half the errors below are unit errors, and they are "
             "invisible once the unit has been dropped."),
            ("Invert it, carrying the conversion",
             "`μ = 1/S`. In milliseconds that is `μ = 1000/S` per second: `S = 2` ms gives "
             "`μ = 500` per second, `S = 40` ms gives `μ = 25` per second."),
            ("Put λ in the same unit of time and divide",
             "`ρ = λ/μ` is a pure number. If the answer has seconds or milliseconds attached "
             "to it, the division was not the one intended."),
            ("Check ρ against 1 before computing anything else",
             "Below one, the queue settles and every formula on this course applies. At or "
             "above one, report `λ − μ` per second and the backlog after the interval you "
             "care about, and stop."),
        ],
        "worked": {
            "title": "800 requests a second, into a 1 ms service and then a 2 ms one",
            "intro": [
                "The same offered load twice, with only the service time changed. The point "
                "is that the second column is not a small degradation of the first."
            ],
            "lines": [
                "λ = 800 / s        S = 1 ms = 1/1000 s",
                "",
                "μ = 1/S  = 1000 / s",
                "ρ = λ/μ  = 800/1000 = 4/5              settles; busy 4 s in 5",
                "",
                "now the same load into a service twice as slow",
                "",
                "S = 2 ms           μ = 500 / s",
                "ρ = 800/500 = 8/5                      8/5 ≥ 1: nothing settles",
                "",
                "λ − μ = 800 − 500 = 300 / s",
                "after one minute   300 × 60 = 18 000 waiting",
            ],
            "after": [
                "Nothing about the traffic changed between the two columns. A service time of "
                "1 ms leaves a fifth of a server spare; a service time of 2 ms asks for "
                "eight fifths of one, and the shortfall of 300 a second does not average "
                "away &mdash; it accumulates.",
                "For a faded rehearsal, keep the 1 ms service and raise the load to 1200 a "
                "second instead. The supplied first move is that `μ` is unchanged at 1000. "
                "Work out `ρ`, say whether it settles, and if it does not give the backlog "
                "after five minutes before opening the quiz.",
            ],
        },
        "quiz_title": "Rates and the ratio",
        "quiz": [
            {"q": "A request takes 4 ms to serve. What is `μ`?",
             "a": ["`4` per second", "`250` per second", "`1/4` per second", "`400` per second"],
             "c": 1,
             "why": "`μ = 1/S` and `S = 4` ms `= 4/1000` s, so `μ = 1000/4 = 250` per second. "
                    "`4` is the service time with its unit dropped; `1/4` inverts the number "
                    "without converting from milliseconds; `400` divides 1000 by 2.5."},
            {"q": "600 requests a second arrive at a service that takes 1 ms. What is `ρ`?",
             "a": ["`3/5`", "`5/3`", "`600`", "`3/5` ms"],
             "c": 0,
             "why": "`μ = 1000` per second, so `ρ = 600/1000 = 3/5`. `5/3` is the division "
                    "done upside down; `600` is `λ` multiplied by the service time in "
                    "milliseconds; and `ρ` carries no unit at all, because the seconds in "
                    "the numerator and the denominator cancel."},
            {"q": "Arrivals run at 1200 a second into a service with `μ = 1000`. How much work is waiting after five minutes?",
             "a": ["None &mdash; it drains", "`60 000` requests", "`1200` requests", "`200` requests"],
             "c": 1,
             "why": "`λ − μ = 200` a second, and five minutes is 300 seconds, so `200 × 300 "
                    "= 60 000`. `200` is the growth rate rather than the backlog, and `1200` "
                    "is one second of arrivals. Nothing drains: `ρ = 6/5`."},
            {"q": "`λ = 250` a second and `S = 5` ms. What is `ρ`?",
             "a": ["`5/4`", "`4/5`", "`1250`", "`50`"],
             "c": 0,
             "why": "`μ = 1000/5 = 200` per second, so `ρ = 250/200 = 5/4`, which is above "
                    "one: this system does not settle. `4/5` is the same division upside "
                    "down and is the tempting answer because it looks like a healthy "
                    "utilisation; `1250` multiplies the rate by the milliseconds."},
        ],
        "mistakes": [
            ("Reading `μ` as a latency",
             "&ldquo;The service takes 2 ms, so `μ = 2`&rdquo; is the error this lesson "
             "exists to prevent. `μ` counts completions per unit time: 2 ms per job is 500 "
             "jobs a second. Any `ρ` that comes out in the hundreds or thousands is this "
             "mistake, because it is `λ` multiplied by a duration rather than divided by a "
             "rate."),
            ("Dividing a per-second rate by a millisecond figure",
             "`800/2` is 400 only if both numbers are in the same unit of time, and they are "
             "not: one is per second and the other is milliseconds per job. Convert first, "
             "divide second. Writing the unit next to every number makes this error visible "
             "before the division rather than after it."),
            ("Quoting a queue length above `ρ = 1`",
             "`ρ/(1 − ρ)` at `ρ = 8/5` returns `-8/3`, and a negative queue is the formula "
             "reporting that its assumption has failed. Above one there is no steady state "
             "to average; the honest answer is the growth rate `λ − μ` and the interval you "
             "are prepared to let it run."),
        ],
        "standard": ("Finish when “a 2 ms service” and “μ = 500 per second” are the same sentence to you.",
                     "You should be able to take a service time in milliseconds to `μ`, take "
                     "`λ` and `μ` to `ρ`, say at a glance whether a system settles at all, "
                     "and when it does not give the growth rate rather than a queue length."),
        "note": 'Everything above is one server at one moment. The next lesson leaves models behind entirely: “Little&rsquo;s Law from a Trace” proves the one relation on this course that assumes nothing at all &mdash; no distribution, no steady state, not even a queue discipline &mdash; by counting the same area twice.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "littles-law-from-a-trace",
        "title": "Little's Law from a Trace",
        "module": "Rates and Little's Law",
        "one_line": "Compute L, λ and W from arrival and departure times and verify L = λW exactly.",
        "summary": (
            "`L = λW` is not a model and not an approximation: it is one area counted two "
            "ways. Slice the graph of the number in system vertically and you get the "
            "time-average `L`; slice it horizontally and you get one bar per customer, whose "
            "total is `n·W`. The library proves it here, on a trace of five customers."
        ),
        "key": [
            "N(t)                   how many are in the system at time t",
            "L = area(N)/T          the time-average number in system",
            "λ = n/T                arrivals per unit time over the window",
            "W = Σ(dᵢ − aᵢ)/n       the mean time one customer spends inside",
            "L = λW                 the same area, counted the other way round",
        ],
        "key_label": "Three averages over one window, and the identity between them",
        "concepts_intro": (
            "The proof is a picture, and once the picture is seen the formula stops needing to "
            "be remembered."
        ),
        "concepts": [
            ("The area under `N(t)` is the sum of the stays",
             "Each customer adds exactly `1` to `N(t)` for exactly as long as it is in the "
             "system, and nothing to it otherwise. So the region under the staircase can be "
             "added in vertical strips &mdash; one per unit of time, height `N(t)` &mdash; or "
             "in horizontal bars, one per customer, length `dᵢ − aᵢ`. The two totals are the "
             "same number because they are the same region."),
            ("No distribution appears anywhere in it",
             "There is no Poisson here, no memorylessness, no steady state, no service "
             "discipline and no independence. `L = λW` holds for one particular trace of five "
             "customers, for a queue served in reverse order, for a system that is not a "
             "queue at all. It is arithmetic about a window."),
            ("The window must be closed to be counted",
             "The identity compares an area that has accrued with stays that have finished. "
             "If someone is still inside at time `T`, the area has counted time that no "
             "completed stay has counted yet, and the two sides differ &mdash; not because "
             "the law failed but because the measurement stopped early."),
        ],
        "read_title": "One area, counted twice",
        "read_intro": "The definitions, the proof, the arithmetic on a five-customer trace, and the one way to get it wrong.",
        "body": [
            ("def", ("The three averages over a window",
                     "Over a window `[0, T]` in which `n` customers arrive at times `aᵢ` and "
                     "leave at times `dᵢ`: `N(t)` is the number present at time `t`; "
                     "<strong>L</strong> is the time-average of `N(t)`, the area under it "
                     "divided by `T`; <strong>λ</strong> is `n/T`; and <strong>W</strong> is "
                     "the mean of the sojourn times `dᵢ − aᵢ`.")),
            ("p", "Take five customers arriving at `0, 1, 2, 5, 6` and leaving at "
                  "`3, 4, 6, 8, 10`. Nothing is assumed about why they arrived when they did "
                  "or how long they were served. This is a record, not a model."),
            ("math", [
                "t        0  1  2  3  4  5  6  7  8  9",
                "N(t)     1  2  3  2  1  2  2  2  1  1      area = 17",
                "",
                "stays    3 − 0 = 3",
                "         4 − 1 = 3",
                "         6 − 2 = 4",
                "         8 − 5 = 3",
                "        10 − 6 = 4                          sum  = 17",
            ]),
            ("p", "The two seventeens are not a coincidence and they are not a check that "
                  "might have failed. They are the same area, added in two directions."),
            ("thm", ("Little's Law, on a closed window",
                     "If every customer who arrives in `[0, T]` has also departed by `T`, "
                     "then `L = λW` exactly, where `L`, `λ` and `W` are as defined above.")),
            ("proof", [
                "Customer `i` contributes `1` to `N(t)` for `t` in `[aᵢ, dᵢ)` and `0` "
                "elsewhere, so the total area under `N(t)` is `Σᵢ (dᵢ − aᵢ)`: adding the "
                "strips vertically and adding the bars horizontally are two orders of "
                "summation over the same finite set of unit cells.",
                "Divide that equality by `T`. The left side is `area/T = L`. The right side "
                "is `Σᵢ(dᵢ − aᵢ)/T`, and multiplying and dividing by `n` makes it "
                "`(n/T)·(Σᵢ(dᵢ − aᵢ)/n) = λW`. No property of the arrival times or the "
                "service times was used, only that every stay lies inside the window.",
            ]),
            ("p", "On the trace above: `L = 17/10`, `λ = 5/10 = 1/2`, `W = 17/5`, and "
                  "`λW = (1/2)(17/5) = 17/10`, which is `L` to the digit. The lab prints all "
                  "three as exact fractions for whatever trace you type into it."),
            ("h3", "Where it appears to fail, and why that is never the law"),
            ("p", "Cut the same trace at `T = 8`, while the last customer is still inside. "
                  "Now `L = 15/8 = 1.875` and `λW = (5/8)(13/4) = 65/32 = 2.03125`. The two "
                  "sides part company because `λ` counted five arrivals while `W` averaged "
                  "the four stays that had finished. Extend the window to 10 and they agree "
                  "again. Every report of &ldquo;Little's Law not holding&rdquo; on a real "
                  "system is this: a measurement window with work still in flight, or three "
                  "quantities measured at three different boundaries."),
            ("example", ("A trace with no overlap at all",
                         "Arrivals at `0, 2, 4, 6, 8` and departures at `2, 4, 6, 8, 10`: "
                         "exactly one customer is present at every instant, so `L = 1`. With "
                         "`λ = 1/2` and `W = 2`, `λW = 1`. Here `L` is the fraction of time "
                         "the system is occupied, which is the `ρ` of the previous lesson "
                         "seen from this side.")),
            ("p", "What the identity does not give you is any information about the "
                  "<em>distribution</em> of the waiting. `W` is a mean, and a mean says "
                  "nothing about the p99 that Latency and the Tail measured. Two systems "
                  "with identical `L`, `λ` and `W` can have entirely different tails."),
            ("p", "The same counting argument works across any boundary you can draw, with "
                  "`λ` the rate that crosses <em>into</em> it: a component, a thread pool, a "
                  "whole datacentre. That generalisation is Operations Research, "
                  "`markov-chains-decisions-and-queues/littles-law`, which cites this proof "
                  "and carries the boundary version and the rule that the rate must be the "
                  "one actually admitted &mdash; which is exactly what a lossy system later "
                  "in this course will need."),
        ],
        "lab": ("queue", {
            "mode": "trace",
            "preset": "five-customers",
            "panel_title": "Edit the trace and watch both counts",
            "panel_intro": "The staircase, its area, the bar per customer and the sum of the "
                           "bars are drawn together. Change an arrival time, change a "
                           "departure time, shorten the window: the two totals move together "
                           "until a customer is left inside at the end.",
        }),
        "steps_title": "Verifying the identity on a trace you have been handed",
        "steps_intro": "Do this once by hand. It takes a minute and it is the difference between a formula and a fact.",
        "steps": [
            ("Draw N(t) as a staircase",
             "Step up at each arrival, down at each departure. On a slotted trace it is "
             "enough to write the count in each slot in a row."),
            ("Add the area by counting",
             "Sum the heights. On a unit-slot trace that is a sum of whole numbers, and it is "
             "the left-hand side of the identity."),
            ("Add the stays one customer at a time",
             "`dᵢ − aᵢ` for each, then total them. This is the same number, and getting a "
             "different one means a time was mis-transcribed."),
            ("Divide, and check",
             "`L = area/T`, `λ = n/T`, `W = total/n`. Multiply `λ` by `W` and compare with "
             "`L`; as exact fractions they are equal, not close."),
            ("Say which window you used",
             "`L = λW` is a statement about a window, so the window is part of the answer. "
             "If work was still in flight at the end, say so &mdash; that is the one "
             "condition the proof needed."),
        ],
        "worked": {
            "title": "Five customers over ten slots, then the same trace cut short",
            "intro": [
                "The first column is the identity. The second is the only way to break it, "
                "done deliberately so that the break is recognisable later."
            ],
            "lines": [
                "arrivals    a = 0, 1, 2, 5, 6",
                "departures  d = 3, 4, 6, 8, 10          T = 10,  n = 5",
                "",
                "t        0  1  2  3  4  5  6  7  8  9",
                "N(t)     1  2  3  2  1  2  2  2  1  1     area = 17",
                "stays    3, 3, 4, 3, 4                    sum  = 17",
                "",
                "L = 17/10      λ = 5/10 = 1/2      W = 17/5",
                "λW = (1/2)(17/5) = 17/10 = L                      ✓",
                "",
                "now stop the clock at T = 8, with one customer still inside",
                "",
                "area over [0,8] = 15        L = 15/8   = 1.875",
                "arrivals 5, λ = 5/8;  four stays done, W = 13/4",
                "λW = (5/8)(13/4) = 65/32 = 2.03125                ✗",
            ],
            "after": [
                "The second column did not break the law. It measured `λ` over five arrivals "
                "and `W` over four completions, which are two different populations, and the "
                "gap between `15/8` and `65/32` is exactly the stay that had not finished.",
                "For a faded rehearsal, take arrivals `0, 1, 4` with departures `2, 5, 6`. "
                "The supplied first move is that the horizon is `T = 6` and every customer "
                "has left by it. Build the staircase, get the area both ways, and predict "
                "`L` before dividing anything.",
            ],
        },
        "quiz_title": "Counting the same area twice",
        "quiz": [
            {"q": "Three customers arrive at `0, 1, 4` and leave at `2, 5, 6`, with `T = 6`. What is `L`?",
             "a": ["`4/3`", "`8/3`", "`8`", "`1/2`"],
             "c": 0,
             "why": "The stays are `2, 4, 2`, totalling `8`, so the area is `8` and "
                    "`L = 8/6 = 4/3`. `8/3` is `W`, the mean stay; `8` is the area before "
                    "dividing by the window; `1/2` is `λ`."},
            {"q": "Which assumption does `L = λW` require?",
             "a": ["Poisson arrivals",
                   "Exponentially distributed service times",
                   "First-in first-out service",
                   "None of those &mdash; only a window in which everyone who arrived has left"],
             "c": 3,
             "why": "The proof adds one finite region in two directions. It never mentions "
                    "how the arrival times were generated, how long service took or what "
                    "order customers were served in. The single condition is the closed "
                    "window, which is what makes the two sums cover the same area."},
            {"q": "A team measures a service and finds `L = 1.875` but `λW = 2.03125`. What is the most likely cause?",
             "a": ["The law only holds in steady state, which the service was not in",
                   "The measurement window ended while a request was still in flight",
                   "The arrivals were not Poisson",
                   "`W` should have been the median rather than the mean"],
             "c": 1,
             "why": "Those are exactly the numbers from cutting the lesson's trace at "
                    "`T = 8`. Five arrivals were counted against four finished stays. The "
                    "law needs no steady state and no distribution, and `W` is a mean by "
                    "definition &mdash; a median would not satisfy the identity at all."},
        ],
        "mistakes": [
            ("Believing the identity needs Poisson arrivals",
             "It is quoted so often beside M/M/1 that the two get welded together, and then "
             "a reader refuses to use it on a real system whose arrivals are obviously not "
             "Poisson. The proof above uses no property of the arrival process. If you can "
             "count arrivals and time stays, `L = λW` is available."),
            ("Measuring over a window with work still in flight",
             "Counting every arrival but only the completed stays gives `λ` a bigger "
             "population than `W`, and the identity fails by the amount still inside &mdash; "
             "`15/8` against `65/32` on the lesson's trace. Extend the window until it is "
             "closed, or count only the customers who both arrived and left inside it."),
            ("Measuring the three quantities at three different boundaries",
             "`L` inside a thread pool, `λ` at the load balancer and `W` from the client's "
             "stopwatch are three different systems, and their numbers have no reason to "
             "satisfy anything. Draw the boundary first, then count what crosses it and how "
             "long things stay inside it."),
        ],
        "standard": ("Finish when you would reach for `L = λW` on a system with no model at all.",
                     "You should be able to build `N(t)` from arrival and departure times, "
                     "get the area by counting in either direction, produce `L`, `λ` and `W` "
                     "as exact fractions, and diagnose a failed check as a window or a "
                     "boundary problem rather than a broken law."),
        "note": 'The identity is most useful solved for something you do not know. “Sizing with Little&rsquo;s Law” does exactly that: fix any two of the three and the third is determined, which is how a connection pool, a thread count and a throughput ceiling turn out to be one arithmetic problem.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "sizing-with-littles-law",
        "title": "Sizing with Little's Law",
        "module": "Rates and Little's Law",
        "one_line": "Size a connection pool from a rate and a latency, and state the throughput cap it implies.",
        "summary": (
            "Concurrency is not a number anyone chooses: it is `λW`, a throughput multiplied "
            "by a latency. Fix any two of `L`, `λ` and `W` and the third follows, which makes "
            "the same identity a pool sizer, a throughput ceiling and a latency budget "
            "depending on which one you leave blank."
        ),
        "key": [
            "L = λW           concurrency = throughput × latency",
            "N = λW           the pool a target rate needs",
            "λ = N/W          the rate a pool of N can support",
            "W = L/λ          the latency the other two imply",
            "units            500/s × 40 ms = 500 × 0.04 s = 20, not 20 000",
        ],
        "key_label": "One identity, three ways round",
        "concepts_intro": (
            "Nothing new is proved here. What is new is which of the three letters you leave "
            "unknown, and that choice is the whole of capacity sizing."
        ),
        "concepts": [
            ("Concurrency is a product, not a preference",
             "A service handling `λ` requests a second, each spending `W` seconds inside, has "
             "`λW` of them inside at any moment whether or not anyone planned for it. A pool "
             "smaller than that number does not reduce the concurrency; it converts the "
             "excess into queueing in front of the pool."),
            ("A pool is a throughput ceiling",
             "Read the same identity the other way: `N` connections, each occupied for `W`, "
             "can start at most `N/W` pieces of work per second. A pool of 20 at 40 ms caps "
             "at 500 a second, and no amount of offered load gets more than that through it."),
            ("Latency and throughput are welded together by it",
             "If `W` doubles and `N` is fixed, the ceiling halves. That is why a dependency "
             "getting slower shows up as a throughput incident rather than a latency one: "
             "the pool was the binding constraint, and `N/W` moved."),
        ],
        "read_title": "Solving the identity for the letter you do not know",
        "read_intro": "The three rearrangements, the unit trap in the middle of them, and the thread-count question they settle.",
        "body": [
            ("def", ("The three forms",
                     "With `L` the mean number in flight, `λ` the arrival rate and `W` the "
                     "mean time in system: `L = λW` sizes the concurrency, `λ = L/W` gives "
                     "the throughput a fixed concurrency supports, and `W = L/λ` gives the "
                     "time in system implied by the other two. They are one equation "
                     "rearranged, in the sense of Algebra's `literal-equations-and-formulas`.")),
            ("p", "The only difficulty is units. `λ` is per second and `W` is usually quoted "
                  "in milliseconds, so the product needs one conversion &mdash; and skipping "
                  "it produces an answer a thousand times too large, which is large enough to "
                  "be noticed and small enough to be believed once someone has typed it into "
                  "a configuration file."),
            ("math", [
                "λ = 500 / s        W = 40 ms = 0.04 s",
                "",
                "L = λW = 500 × 0.04 = 20            connections in flight",
                "wrong: 500 × 40     = 20 000        per-second times milliseconds",
                "",
                "the other direction",
                "λ = N/W = 20 / 0.04 = 500 / s       the ceiling that pool implies",
            ]),
            ("example", ("What a slower database does to a fixed pool",
                         "The pool of 20 above supports 500 a second at 40 ms. If the "
                         "database slows to 80 ms, the same pool supports `20/0.08 = 250` a "
                         "second. Holding 500 a second through it now needs "
                         "`500 × 0.08 = 40` connections. Nothing about the traffic changed.")),
            ("h3", "Threads, cores, and work that waits"),
            ("p", "A thread that is waiting on a network call is not using a core. Sizing a "
                  "thread pool by core count is right for work that is CPU-bound and wrong "
                  "for work that is not, and the identity says by how much: a service taking "
                  "200 requests a second, each spending 250 ms mostly waiting on a "
                  "dependency, has `200 × 0.25 = 50` requests in flight. Eight cores is the "
                  "wrong number to compare that with; 50 is the concurrency the work has, "
                  "and the question is only whether the runtime can hold 50 waiting things "
                  "cheaply."),
            ("p", "This is also the honest way to read a &ldquo;max connections&rdquo; limit "
                  "on a database. It is not a popularity cap; it is a `W`-dependent "
                  "throughput cap, and the number it implies changes every time the query "
                  "mix changes."),
            ("ul", [
                "Unknown `L`: you have a target rate and a measured latency, and you want a "
                "pool size.",
                "Unknown `λ`: you have a fixed pool and a measured latency, and you want the "
                "ceiling it imposes.",
                "Unknown `W`: you have a pool running at its ceiling, and you want the "
                "latency that implies &mdash; the answer the dashboard should agree with.",
            ]),
            ("p", "One warning before the lab. Sizing a pool at exactly `L` sizes it at the "
                  "<em>mean</em>, and the mean is not the peak: arrivals bunch, and a pool "
                  "sized at the mean is a queue in front of a queue. How much headroom that "
                  "argues for is what the rest of this course prices, and the answer is a "
                  "function of how close to its ceiling you are willing to run."),
        ],
        "lab": ("queue", {
            "mode": "little",
            "solve": "L",
            "rate": 500,
            "wait": 40,
            "pool": 20,
            "panel_title": "Fix two, read the third",
            "panel_intro": "Choose which of `L`, `λ` and `W` is unknown, set the other two, "
                           "and the answer is printed with its units spelled out. The "
                           "rectangle is the identity: its width is the rate, its height is "
                           "the wait, and its area is the concurrency.",
        }),
        "steps_title": "Sizing with the identity",
        "steps_intro": "Name the unknown first. Everything else is one multiplication or one division.",
        "steps": [
            ("Decide which letter you are solving for",
             "A pool size is `L`, a ceiling is `λ`, an implied latency is `W`. Writing down "
             "which one is unknown before touching numbers prevents the answer coming out "
             "upside down."),
            ("Put both known quantities into seconds",
             "Milliseconds divided by 1000. Do it explicitly and leave it written down: "
             "`40 ms = 0.04 s`."),
            ("Multiply or divide once",
             "`L = λW`, `λ = L/W`, `W = L/λ`. One operation; if the arithmetic is longer than "
             "that, a unit was left in."),
            ("Sanity-check the magnitude against the latency",
             "A pool much larger than `λ` in seconds' worth of requests, or an answer in the "
             "tens of thousands for a service that handles hundreds a second, is the "
             "millisecond-times-per-second error."),
            ("Add headroom deliberately, and say how much",
             "The number the identity gives is a mean. Whatever multiple of it you choose, "
               "record the multiple as a decision rather than rolling it into the estimate."),
        ],
        "worked": {
            "title": "A connection pool for 500 requests a second at 40 ms",
            "intro": [
                "One sizing, then the same pool re-read as a ceiling when the dependency "
                "gets slower."
            ],
            "lines": [
                "target λ = 500 / s      measured W = 40 ms = 0.04 s",
                "",
                "L = λW = 500 × 0.04 = 20        connections in flight, on average",
                "",
                "read the other way",
                "λ = N/W = 20 / 0.04 = 500 / s   the pool's ceiling, as expected",
                "",
                "the dependency slows to 80 ms",
                "",
                "λ = 20 / 0.08 = 250 / s         the same pool, half the throughput",
                "N = 500 × 0.08 = 40             what holding 500 / s would now cost",
                "",
                "sanity check    500 × 40 = 20 000 would be the answer in",
                "                millisecond-connections, not connections",
            ],
            "after": [
                "The third block is the useful one. A pool is a throughput cap expressed in "
                "the units of whatever latency the dependency happens to have today, so a "
                "latency regression and a throughput regression are the same event seen "
                "through `N/W`.",
                "For a faded rehearsal, size a pool for 2000 requests a second at 5 ms, then "
                "state the ceiling that same pool imposes if the service time doubles. The "
                "supplied first move is `5 ms = 0.005 s`; predict both numbers before "
                "opening the quiz.",
            ],
        },
        "quiz_title": "Sizing, both directions",
        "quiz": [
            {"q": "A service handles 2000 requests a second, each spending 5 ms in the system. How many are in flight on average?",
             "a": ["`10`", "`400`", "`10 000`", "`2.5`"],
             "c": 0,
             "why": "`L = 2000 × 0.005 = 10`. `10 000` multiplies the per-second rate by the "
                    "millisecond figure without converting; `400` divides 2000 by 5; `2.5` "
                    "inverts the multiplication."},
            {"q": "A pool of 64 connections is used for work taking 40 ms. What throughput can it support?",
             "a": ["`1600` per second", "`2560` per second", "`160` per second", "`40` per second"],
             "c": 0,
             "why": "`λ = N/W = 64/0.04 = 1600` a second. `2560` is `64 × 40`, the product "
                    "instead of the quotient and in the wrong units besides; `160` divides "
                    "by 0.4 s."},
            {"q": "A service takes 200 requests a second, each spending 250 ms mostly waiting on a dependency. It runs on 8 cores. What is the mean concurrency?",
             "a": ["`50`", "`8`", "`500`", "`0.8`"],
             "c": 0,
             "why": "`200 × 0.25 = 50` requests are in flight, and the core count does not "
                    "enter the identity at all. Cores would bound the concurrency of work "
                    "that is actually computing; this work is waiting, and 50 things waiting "
                    "is what the arithmetic says regardless of how many cores are behind it."},
            {"q": "A pool is sized at exactly the `L` the identity gives. What does that leave?",
             "a": ["Nothing &mdash; it is exactly right, by construction",
                   "No room for the variation around the mean, so work queues for the pool",
                   "A pool that is twice as large as necessary",
                   "A pool whose throughput ceiling is unbounded"],
             "c": 1,
             "why": "`L` is a mean. Arrivals bunch around it, and a pool sized at the mean "
                    "is busy whenever the instantaneous demand is above it &mdash; which is "
                    "a queue in front of the pool, added to whatever queue is behind it. "
                    "How much headroom to buy is what the rest of this course prices."},
        ],
        "mistakes": [
            ("Multiplying a per-second rate by a figure in milliseconds",
             "`500 × 40 = 20 000` is the single most common arithmetic error on this course, "
             "and it is believable enough to reach production. Convert the latency to "
             "seconds first, every time, and write the conversion down."),
            ("Sizing threads by core count when the threads wait",
             "Core count bounds work that computes. Concurrency of work that waits is "
             "`λW`, and at 200 a second and 250 ms that is 50 whatever the machine has. The "
             "question cores answer is a different one: how much of that `W` is CPU."),
            ("Treating the sized pool as a guarantee",
             "The identity gives the mean concurrency at the given `λ` and `W`. It does not "
             "promise that `W` stays put &mdash; and `W` is exactly what rises when the pool "
             "becomes the constraint, which is a feedback loop rather than a fixed point. "
             "Size with headroom and measure `W` again afterwards."),
        ],
        "standard": ("Finish when a pool size, a thread count and a throughput ceiling all look like the same equation to you.",
                     "You should be able to size a pool from a rate and a latency, state the "
                     "ceiling any fixed pool implies, convert units without thinking about "
                     "it, and explain why the core count is the wrong comparison for work "
                     "that waits."),
        "note": 'Everything so far has been exact and model-free. “Why Queues Form at ρ &lt; 1” asks the question the identity cannot answer &mdash; why `W` is bigger than the service time at all when the server is idle a fifth of the time &mdash; and the answer is not overload.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "why-queues-form-below-full-utilisation",
        "title": "Why Queues Form at ρ < 1",
        "module": "Randomness",
        "one_line": "Compare the mean queue of random and clockwork arrivals at the same utilisation and name the difference.",
        "summary": (
            "A server busy four fifths of the time has a fifth of itself spare, and yet work "
            "waits. It waits because arrivals bunch: run clockwork arrivals and clockwork "
            "service at `ρ = 4/5` and nothing ever queues, then run random ones at exactly "
            "the same `ρ` and the mean number in the system triples. Bunching, not overload."
        ),
        "key": [
            "clockwork in, clockwork out     nothing waits at all below ρ = 1",
            "Bernoulli(p) in, Geometric(q)   ρ = p/q, and now things wait",
            "p = 2/5, q = 1/2, ρ = 4/5       D/D/1: L = 4/5    Geo/Geo/1: L = 12/5",
            "12/5 ÷ 4/5 = 3                  three times as many, at the same ρ",
            "ρ/(1 − ρ) = 4                   a different model's answer: 5/3 too big here",
        ],
        "key_label": "Two arrival patterns, one utilisation",
        "concepts_intro": (
            "The comparison is the lesson. Both arms have identical rates, identical "
            "utilisation and identical mean service time, and one of them never queues."
        ),
        "concepts": [
            ("Determinism does not queue below one",
             "One arrival every five slots, served in exactly four: the server is busy `4/5` "
             "of the time and no second customer ever exists. The mean number in the system "
             "is exactly `4/5` &mdash; the one in service, counted for the fraction of time "
             "it is there &mdash; and the largest the system ever holds is one."),
            ("Randomness bunches, and bunching waits",
             "Keep `ρ = 4/5` and make the arrivals random and the service random. Now the "
             "mean number in the system is `12/5`, three times the clockwork answer. The "
             "server is idle exactly as often as before; it is idle at the wrong moments, "
             "and the work that arrives while it is busy is what waits."),
            ("A simulation is a model, so it has to be named",
             "&ldquo;I ran a simulation&rdquo; is not a measurement of anything until the "
             "model is stated. This one is a Bernoulli arrival per slot, a geometric "
             "service, and a rule about what happens when both land in the same slot. Change "
             "any of the three and the number changes."),
        ],
        "read_title": "The same utilisation, twice",
        "read_intro": "What clockwork does, what randomness does, exactly which model the simulation is, and which number in it is exact.",
        "body": [
            ("p", "&ldquo;We are only at 70% &mdash; nobody should be waiting.&rdquo; The "
                  "sentence assumes that a server with headroom is a server with no queue, "
                  "and it is true of exactly one system: the one where work arrives on a "
                  "timetable and takes the same time every time."),
            ("example", ("Clockwork, at ρ = 4/5",
                         "One arrival every five slots; each takes exactly four slots to "
                         "serve. The server finishes a slot before the next arrival appears, "
                         "so the system holds one customer four slots in five and none in "
                         "the fifth. `L = 4/5`, and the largest number ever present is "
                         "`1`. Nothing queues, ever, at any utilisation below one.")),
            ("def", ("The slotted model, named",
                     "Time advances in slots. In each slot <strong>one arrival occurs with "
                     "probability `p`</strong>, independently of everything else. A customer "
                     "in service <strong>completes with probability `q`</strong> in each "
                     "slot, so service times are geometric with mean `1/q` slots. Within a "
                     "slot the departure is resolved first and the arrival second &mdash; the "
                     "<strong>late-arrival convention</strong> &mdash; so a customer arriving "
                     "in slot `t` cannot leave before slot `t + 1`.",
                     "That is a discrete-time chain, written <strong>Geo/Geo/1</strong>. It "
                     "is not M/M/1, and the convention in the last sentence is part of the "
                     "model: change it and the exact answer changes.")),
            ("p", "The utilisation of that chain is `ρ = p/q`: arrivals come at `p` per slot, "
                  "each takes `1/q` slots of the server, so the server is busy `p/q` of the "
                  "time. At `p = 2/5` and `q = 1/2` that is `ρ = 4/5` &mdash; the same "
                  "utilisation as the clockwork run, the same mean service time of two slots, "
                  "and the same throughput."),
            ("math", [
                "at ρ = 4/5, three numbers for the mean number in system",
                "",
                "clockwork  D/D/1          L = 4/5   = 0.8     and never more than 1",
                "slotted    Geo/Geo/1      L = 12/5  = 2.4     exact, p = 2/5, q = 1/2",
                "",
                "12/5 ÷ 4/5 = 3            randomness alone, at identical utilisation",
                "",
                "for comparison, the continuous M/M/1 formula",
                "           M/M/1          ρ/(1 − ρ) = 4",
                "4 ÷ 12/5   = 5/3          which is a different model, not this one",
            ]),
            ("p", "The `12/5` is exact, and it is not this lesson's to derive. The chain "
                  "above is solved in closed form in Operations Research, "
                  "`markov-chains-decisions-and-queues/queues-in-discrete-time`, which gives "
                  "the stationary distribution and the mean `L = p(1 − p)/(q − p)` "
                  "&mdash; equivalently `ρ(1 − p)/(1 − ρ)` &mdash; for any `p` and `q` "
                  "under this convention. What belongs here is the phenomenon: "
                  "waiting appears well below `ρ = 1`, and the lab shows it happening."),
            ("p", "Note what the third line of the table does <em>not</em> say. `ρ/(1 − ρ)` "
                  "is `4` at this utilisation, and `4` is not the slotted system's answer: it "
                  "overstates the exact `12/5` by a factor of `5/3`. The continuous formula "
                  "describes the limit of this chain as the slot shrinks, not the chain at a "
                  "slot of one. &ldquo;The M/M/1 Queue&rdquo; states that limit precisely and "
                  "shows the convergence; treating the two as the same model is the error "
                  "that comparison is designed to prevent."),
            ("h3", "The simulation starts empty"),
            ("p", "A run begins with nothing in the system, which is a state the settled "
                  "chain visits only a fifth of the time. Averaging from `t = 0` therefore "
                  "includes a stretch that is unrepresentatively quiet, and the mean comes "
                  "out biased low. The lab prints the mean twice &mdash; from `t = 0` and "
                  "after discarding a warm-up &mdash; and draws the ensemble occupancy "
                  "rising from zero so that the bias is visible rather than argued about. "
                  "The general treatment is Operations Research, "
                  "`simulation/warm-up-and-the-initial-transient`."),
            ("p", "Neither printed mean is the exact answer. One run is a sample: the same "
                  "seed gives the same run and a different seed gives a different number, and "
                  "with a few thousand slots the sampling error is larger than the difference "
                  "between many wrong formulas. What is stable across seeds is the "
                  "comparison &mdash; the random arm above the clockwork arm, by a factor "
                  "near three &mdash; and that comparison is what the lesson claims."),
            ("ul", [
                "Identical in both arms: the arrival rate, the mean service time, the "
                "utilisation `ρ = 4/5`, and the throughput.",
                "Different in the random arm: when the arrivals land, and how long each "
                "service actually takes.",
                "Consequence: a mean number in system of `12/5` rather than `4/5`, from "
                "nothing but the pattern.",
            ]),
            ("p", "So the honest version of the opening sentence is: at 70% utilisation the "
                  "server is idle 30% of the time, and whether anyone waits depends entirely "
                  "on how that idleness is distributed. Randomness guarantees it is "
                  "distributed badly."),
        ],
        "lab": ("queue", {
            "mode": "slotted",
            "p20": 8,
            "q20": 10,
            "sub": 1,
            "seed": 7,
            "warm": 10,
            "panel_title": "Set the slotted model and run both arms",
            "panel_intro": "`p` and `q` set the chain; the clockwork arm is drawn at the same "
                           "`ρ` beside it. The mean from `t = 0`, the mean after the warm-up "
                           "you discard, and the exact Geo/Geo/1 answer are printed together, "
                           "so the sampling error and the initial bias are both visible.",
        }),
        "steps_title": "Comparing two arrival patterns honestly",
        "steps_intro": "The comparison is only worth anything if the two arms differ in exactly one respect.",
        "steps": [
            ("Fix the utilisation before anything else",
             "`ρ = p/q` for the random arm. Choose `p` and `q` first, compute `ρ`, and give "
             "the clockwork arm the same one. A comparison at two different `ρ` values "
             "measures nothing."),
            ("Read the clockwork arm's mean",
             "It is exact and it is small: at `ρ = 4/5` the mean number in system is `4/5`, "
             "and the maximum is `1`. This arm has no sampling error because there is "
             "nothing random in it."),
            ("Run the random arm and discard a warm-up",
             "Take the mean from `t = 0` and the mean after the warm-up and note the gap "
             "between them. The run starts empty, so the first is the biased one."),
            ("Change the seed and run it again",
             "Whatever moves between seeds is sampling error, not signal. The factor of "
             "about three does not move; the third decimal place does."),
            ("Compare against the exact chain, not against ρ/(1 − ρ)",
             "The exact answer for this model is `12/5`. `ρ/(1 − ρ) = 4` is the answer for a "
             "different model and is `5/3` too large here, so a run landing near `2.4` is "
             "agreement and a run landing near `4` would be a bug."),
        ],
        "worked": {
            "title": "Two queues at ρ = 4/5",
            "intro": [
                "Both columns have the same utilisation and the same mean service time. Only "
                "the pattern differs, and that is the entire cause of the third number."
            ],
            "lines": [
                "clockwork     one arrival every 5 slots, service exactly 4 slots",
                "              ρ = 4/5    L = 4/5    most ever in the system = 1",
                "",
                "slotted       arrival:  Bernoulli, p = 2/5 per slot",
                "              service:  geometric, q = 1/2 per slot (mean 2 slots)",
                "              ρ = p/q = (2/5)/(1/2) = 4/5          the same ρ",
                "",
                "exact chain   Operations Research's closed form for this convention",
                "              L = p(1 − p)/(q − p)",
                "                = (2/5)(3/5)/(1/10) = 12/5 = 2.4",
                "",
                "the effect    12/5 ÷ 4/5 = 3       three times, from the pattern alone",
                "",
                "not this      ρ/(1 − ρ) = (4/5)/(1/5) = 4",
                "              4 ÷ 12/5 = 5/3       the continuous formula, overstating",
            ],
            "after": [
                "The clockwork column is the intuition being corrected: it really is true "
                "that a deterministic system with headroom never queues. Every real system "
                "fails its assumption, and the cost of failing it is the factor of three.",
                "The last block is worth reading twice. `ρ/(1 − ρ)` is the right formula for "
                "a different model, and reaching for it here would overstate the queue by "
                "`5/3`. The two agree only in the limit of a vanishing slot, which is the "
                "subject of &ldquo;The M/M/1 Queue&rdquo;.",
                "For a faded rehearsal, set `p = 1/4` and `q = 1/2`. The supplied first move "
                "is `ρ = 1/2`. Predict whether the gap between the random and clockwork arms "
                "is larger or smaller than it was at `ρ = 4/5`, then run it and see.",
            ],
        },
        "quiz_title": "Bunching against overload",
        "quiz": [
            {"q": "Arrivals come every 5 slots exactly and each takes exactly 4 slots to serve. How many customers wait, on average, behind the one in service?",
             "a": ["`4/5`", "None &mdash; nothing ever waits", "`4`", "`12/5`"],
             "c": 1,
             "why": "The next arrival appears a slot after the previous customer has left, "
                    "so a second customer never exists. `4/5` is the mean number in the "
                    "<em>system</em>, which is the one being served counted over the "
                    "fraction of time it is there; `12/5` and `4` belong to the random arm "
                    "and to a different model respectively."},
            {"q": "Bernoulli arrivals with `p = 2/5`, geometric service with `q = 1/2`. What is the exact mean number in the system?",
             "a": ["`4/5`", "`12/5`", "`4`", "`2/5`"],
             "c": 1,
             "why": "`12/5`, which is the exact answer for this chain under the late-arrival "
                    "convention. `4/5` is the clockwork answer at the same `ρ`, and it is "
                    "also `ρ` itself; `4` is `ρ/(1 − ρ)`, which describes a continuous-time "
                    "model and overstates this one by `5/3`."},
            {"q": "Why does a mean taken from `t = 0` come out below the chain's true mean?",
             "a": ["Because the seed biases the early slots",
                   "Because the run starts empty and spends its first slots in states the settled chain visits rarely",
                   "Because Bernoulli arrivals are lighter than Poisson ones",
                   "Because the slot size is too large"],
             "c": 1,
             "why": "An empty start is a state the settled chain is in only `1 − ρ` of the "
                    "time, so the opening stretch is unrepresentatively quiet and drags the "
                    "average down. Discarding a warm-up removes it. The seed decides which "
                    "particular run you get, not which direction the early bias points."},
            {"q": "Which quantity is identical in the clockwork and random arms of the comparison?",
             "a": ["The mean number in the system",
                   "The utilisation `ρ`",
                   "The largest queue observed",
                   "The pattern of arrival times"],
             "c": 1,
             "why": "Holding `ρ` fixed is what makes the comparison mean anything: same "
                    "arrival rate, same mean service time, same fraction of time busy. "
                    "Everything else in the list differs, and the mean number in system "
                    "differs by a factor of three."},
        ],
        "mistakes": [
            ("“At 70% utilisation nobody waits”",
             "Utilisation says how much of the time the server is busy, not when. Random "
             "arrivals put work in front of a busy server and leave the idle time scattered "
             "where nothing needs it, and the result at `ρ = 4/5` is three times the "
             "clockwork queue. The threshold at which waiting begins is not `ρ = 1`; there "
             "is no such threshold."),
            ("Reading a simulated mean as the exact answer",
             "One seeded run of a few thousand slots is a sample, and it starts empty, so it "
             "carries both sampling error and a downward bias. Quote it as a demonstration "
             "of the effect, and quote the chain's closed form &mdash; `12/5` here &mdash; "
             "when an exact number is wanted."),
            ("Expecting this simulation to produce `ρ/(1 − ρ)`",
             "It will not, and a run that did would mean the simulator was wrong. At "
             "`p = 2/5`, `q = 1/2` the exact slotted mean is `12/5` while `ρ/(1 − ρ)` is "
             "`4` &mdash; the continuous formula overstates this system by `5/3`. They meet "
             "only as the slot shrinks, which is a limit rather than a check."),
        ],
        "standard": ("Finish when “we have headroom, so nothing is waiting” reads as a statement about a timetable.",
                     "You should be able to compute `ρ = p/q` for the slotted model, say what "
                     "the clockwork arm does at that `ρ`, name the model a simulation is "
                     "running, and say why `ρ/(1 − ρ)` is not the number to compare a slotted "
                     "run against."),
        "note": 'The random service time above was geometric: a fixed chance of finishing in each slot, whatever has happened so far. “Memoryless Waiting: from Geometric to Exponential” takes that property seriously, shrinks the slot, and arrives at the exponential distribution without writing a density.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "memoryless-waiting",
        "title": "Memoryless Waiting: from Geometric to Exponential",
        "module": "Randomness",
        "one_line": "Compute a waiting-time tail exactly in slots and as its continuous limit, and report the gap.",
        "summary": (
            "Chop a second into slots of width `Δ` and give each slot an arrival with "
            "probability `λΔ`. The chance of still waiting after `t` is `(1 − λΔ)^(t/Δ)`, "
            "exactly. Shrink `Δ` and that expression walks toward `e^(−λt)` &mdash; the "
            "exponential distribution, arriving as a limit of a distribution you already have."
        ),
        "key": [
            "P(T > t) = (1 − λΔ)^(t/Δ)          exact, for slots of width Δ",
            "(1 − λΔ)^(t/Δ) → e^(−λt)           as Δ → 0",
            "E[T] = 1/λ                          the mean gap",
            "P(T > s + t | T > s) = P(T > t)     memoryless, exactly, at every Δ",
            "λ = 1/2, t = 4:  (19/20)⁴⁰ = 0.1285122      e^(−2) ≈ 0.1353353",
        ],
        "key_label": "One tail, two ways of computing it",
        "concepts_intro": (
            "The geometric distribution from Discrete Mathematics is doing all the work here. "
            "The exponential is what it becomes when the slot stops mattering."
        ),
        "concepts": [
            ("`λΔ` is a probability; `λ` is not",
             "A rate of `1/2` arrivals a second is not a probability of `1/2`. Chopped into "
             "slots of `Δ = 1/10` second it becomes a probability of `λΔ = 1/20` per slot, "
             "and that is the number a coin gets flipped against. Halve the slot and the "
             "per-slot probability halves with it; the rate does not move."),
            ("The limit is where `e` comes from",
             "`(1 − λΔ)^(t/Δ)` is `(1 − x/n)ⁿ` with `x = λt` and `n = t/Δ`, and Algebra's "
               "`the-number-e` says where that goes. Nothing on this path writes a density or "
               "an integral: the exponential distribution is defined here by the limit of a "
               "geometric tail, and that is enough to compute with."),
            ("Memorylessness is exact, not a limit",
             "The conditional tail `P(T > s + t | T > s)` equals `P(T > t)` at every slot "
               "size, for every `s`, with no approximation anywhere. It is not something the "
               "exponential acquires in the limit; the geometric already has it, and the "
               "limit inherits it."),
        ],
        "read_title": "From a coin per slot to a continuous tail",
        "read_intro": "The exact tail, the limit it approaches, the property both share, and why one of the two columns is printed as rounded.",
        "body": [
            ("def", ("Waiting in slots",
                     "Divide time into slots of width `Δ`. In each slot an arrival occurs "
                     "with probability `λΔ`, independently. The waiting time `T` until the "
                     "first arrival is <strong>geometric</strong>, and surviving `t` units of "
                     "time means surviving `t/Δ` consecutive slots without one: "
                     "`P(T > t) = (1 − λΔ)^(t/Δ)`.")),
            ("p", "That expression is exact and rational. With `λ = 1/2` per second, "
                  "`Δ = 1/10` second and `t = 4` seconds it is `(19/20)⁴⁰` &mdash; a ratio of "
                  "two forty-digit integers, computed as a fraction and only then printed as "
                  "a decimal."),
            ("math", [
                "λ = 1/2 per second,   t = 4 s,   so λt = 2",
                "",
                "Δ = 1/10 s     λΔ = 1/20,   40 slots     (19/20)⁴⁰  = 0.1285122",
                "Δ = 1/100 s    λΔ = 1/200, 400 slots     (199/200)⁴⁰⁰ = 0.1346580",
                "Δ → 0          e^(−λt) = e^(−2)                     ≈ 0.1353353",
                "",
                "gap at Δ = 1/10     0.0068231",
                "gap at Δ = 1/100    0.0006772        about a tenth of it",
            ]),
            ("p", "Each tenfold refinement of the slot closes about nine tenths of the "
                  "remaining gap, which is what &ldquo;the error is of order `Δ`&rdquo; looks "
                  "like when it is printed rather than asserted. The exact column approaches "
                  "the rounded one from below, because a slotted clock can only let an "
                  "arrival happen at a slot boundary and so gives it slightly fewer chances."),
            ("thm", ("The memoryless property",
                     "For the geometric waiting time above, and for every whole number of "
                     "slots `s` and `t`: `P(T > s + t | T > s) = P(T > t)`. Having waited "
                     "already tells you nothing about how much longer you will wait.")),
            ("proof", [
                "`P(T > s + t | T > s) = P(T > s + t)/P(T > s)` because the event `T > s + t` "
                "is contained in `T > s`. Substituting the tail formula gives "
                "`(1 − λΔ)^((s+t)/Δ) / (1 − λΔ)^(s/Δ)`.",
                "The powers subtract: the quotient is `(1 − λΔ)^(t/Δ)`, which is `P(T > t)`. "
                "Nothing about `s` survives the cancellation, which is the whole content of "
                "the property. It holds at every slot size, so it holds in the limit too.",
            ]),
            ("p", "Concretely: if the bus has not come for three minutes, the chance it takes "
                  "another four is the same as it was when you arrived. Quiet time is not "
                  "credit. This is the single most counter-intuitive fact on the course, and "
                  "it is the assumption the M/M/1 model rests on &mdash; which is why it is "
                  "worth being able to say precisely what it claims and what it does not."),
            ("p", "What it does not claim is that arrivals are evenly spread. Memorylessness "
                  "is exactly what makes bunching possible: nothing in the process discourages "
                  "two arrivals landing in consecutive slots, because the process has no "
                  "record of the first one."),
            ("h3", "One exact column and one rounded one"),
            ("p", "The geometric column is a fraction. The exponential column is not: "
                  "`e^(−λt)` is computed by summing a series and is printed as rounded, with "
                  "the method named on the page. The lab bounds `λt` at 12, because the "
                  "series it uses loses significant digits to cancellation beyond that and a "
                  "confident wrong number is worse than a refusal. The exact column has no "
                  "such limit, which is the argument for exactness stated as a number."),
            ("p", "The mean of the waiting time is `1/λ` &mdash; two seconds at `λ = 1/2` "
                  "&mdash; and it is worth noticing that the tail at the mean is not a half: "
                  "`e^(−1) ≈ 0.368`. An exponential wait is longer than its mean about 37% of "
                  "the time, not half of it, and that asymmetry is the shape behind every "
                  "long tail in the previous course."),
        ],
        "lab": ("queue", {
            "mode": "memoryless",
            "lam10": 5,
            "t": 4,
            "inv_delta": 10,
            "already": 3,
            "panel_title": "Set the rate, the horizon and the slot",
            "panel_intro": "The geometric tail is an exact fraction; the exponential beside it "
                           "is summed from a series and labelled as rounded. Shrink `Δ` and "
                           "watch the gap close. The conditional row is the memoryless "
                           "property, and it does not move when you change how long it has "
                           "already been quiet.",
        }),
        "steps_title": "Computing a waiting tail",
        "steps_intro": "Decide which number you want exact before deciding which formula to use.",
        "steps": [
            ("Turn the rate into a per-slot probability",
             "`λΔ`, with `λ` and `Δ` in the same unit of time. A per-slot probability above "
             "one is not a probability, which is the slot being too coarse for the rate."),
            ("Count the slots in the horizon",
             "`t/Δ`, a whole number. The exact tail is `(1 − λΔ)` raised to that power, and "
             "because both are rational nothing is approximated."),
            ("Take the limit only when you want the shape",
             "`e^(−λt)` is the limit, and it is quicker and independent of `Δ`. It is also "
             "rounded. Use it to reason about shape and use the exact column when the number "
             "goes into a decision."),
            ("Check the conditional tail if the answer surprises you",
             "`P(T > s + t | T > s)` should equal `P(T > t)` for any `s` you try. If it does "
             "not, the model in your head has memory in it that the arithmetic does not."),
        ],
        "worked": {
            "title": "P(no arrival in four seconds) at half an arrival a second",
            "intro": [
                "The same probability computed at two slot sizes and in the limit, with the "
                "memoryless check underneath."
            ],
            "lines": [
                "λ = 1/2 per second     t = 4 s     λt = 2",
                "",
                "Δ = 1/10 s       λΔ = 1/20        slots = 40",
                "                 P(T > 4) = (19/20)⁴⁰    = 0.1285122   exact",
                "",
                "Δ = 1/100 s      λΔ = 1/200       slots = 400",
                "                 P(T > 4) = (199/200)⁴⁰⁰ = 0.1346580   exact",
                "",
                "Δ → 0            e^(−2)                  ≈ 0.1353353   rounded",
                "",
                "gaps             0.0068231   then   0.0006772",
                "",
                "already quiet 3 s?",
                "                 P(T > 3 + 4 | T > 3) = (19/20)⁴⁰ = 0.1285122",
                "                 the same number: the three seconds bought nothing",
            ],
            "after": [
                "The two exact lines are fractions with forty and four hundred digit "
                "denominators, and they are computed as fractions. Only the last digit "
                "printed is rounding, and the `e^(−2)` line says on its face that it is the "
                "rounded one.",
                "The final block is the property, not a coincidence of these numbers. Change "
                "the three seconds to thirty and the conditional tail is unchanged, which is "
                "either obvious or deeply strange depending on how long you look at it.",
                "For a faded rehearsal, take `λ = 1` per second and `t = 3`. The supplied "
                "first move is `λt = 3`, so the limit is `e^(−3)`. Predict whether the "
                "geometric tail at `Δ = 1/10` is above or below it before computing either.",
            ],
        },
        "quiz_title": "Tails, limits and memory",
        "quiz": [
            {"q": "Arrivals come at `λ = 1/2` a second. Time is chopped into slots of `Δ = 1/10` second. What is the probability of an arrival in one slot?",
             "a": ["`1/2`", "`1/20`", "`1/10`", "`5`"],
             "c": 1,
             "why": "`λΔ = (1/2)(1/10) = 1/20`. `1/2` is the rate mistaken for a "
                    "probability; `1/10` is the slot width; `5` is the rate multiplied by "
                    "ten rather than divided."},
            {"q": "The last bus was twenty minutes ago and buses arrive memorylessly at one every ten minutes. What is the chance of waiting another ten?",
             "a": ["Lower than it was when you arrived &mdash; one is due",
                   "The same as it was when you arrived, `e^(−1) ≈ 0.368`",
                   "Higher than when you arrived, because the service is clearly disrupted",
                   "Exactly `1/2`, since ten minutes is the mean"],
             "c": 1,
             "why": "The conditional tail equals the unconditional one, so the twenty "
                    "minutes already spent change nothing: the answer is `e^(−1) ≈ 0.368`. "
                    "It is not `1/2` either &mdash; an exponential wait exceeds its own mean "
                    "about 37% of the time, not half."},
            {"q": "Which of the two columns the lab prints is the exact one?",
             "a": ["The exponential, because it is the true distribution",
                   "The geometric, because `(1 − λΔ)` is rational and the exponent is a whole number of slots",
                   "Both are exact",
                   "Neither is exact"],
             "c": 1,
             "why": "The geometric tail is a power of a fraction and is computed as one. "
                    "`e^(−λt)` is summed from a series and printed rounded &mdash; the lab "
                    "says so on its face, and bounds `λt` at 12 because the method stops "
                    "being trustworthy beyond that."},
            {"q": "The slot shrinks from `Δ = 1/10` to `Δ = 1/100`. What happens to the gap between the geometric tail and `e^(−λt)`?",
             "a": ["It falls to about a tenth of what it was",
                   "It falls to about a hundredth of what it was",
                   "It does not change",
                   "It grows, because more slots mean more rounding"],
             "c": 0,
             "why": "At `λt = 2` the gap goes from about `0.0068` to about `0.00068`. The "
                    "error is of order `Δ`, so a tenfold finer slot closes about nine tenths "
                    "of it. Nothing rounds in the exact column, so more slots do not mean "
                    "more error."},
        ],
        "mistakes": [
            ("“It hasn't arrived in a while, so it's due”",
             "The conditional tail is identical for every amount of time already spent "
             "waiting, and the proof is two lines of cancellation. A process with no memory "
             "cannot owe you anything. The intuition that it does comes from timetables, "
             "which are the deterministic arm of the previous lesson."),
            ("Treating `λ` itself as a per-slot probability",
             "`λ` is a rate and can exceed one; `λΔ` is a probability and cannot. A model "
             "that flips a coin with probability `λ` per slot is running at a completely "
             "different rate from the one intended, and the error scales with how coarse the "
             "slot is."),
            ("Quoting the exponential figure as exact",
             "`e^(−λt)` is the limit, and on this page it is also a sum of a series printed "
             "to a few places. When a number is going into a decision, take the geometric "
             "column at the slot size you actually run at &mdash; it is a fraction, and it is "
             "the one the machine can check."),
        ],
        "standard": ("Finish when memorylessness is a property you can prove in two lines, not a slogan.",
                     "You should be able to turn a rate into a per-slot probability, compute "
                     "`P(T > t)` exactly in slots, say where `e^(−λt)` comes from and which "
                     "of the two is rounded, and show that the conditional tail does not "
                     "depend on how long the wait has already lasted."),
        "note": 'The same shrinking-slot argument answers a different question: not how long until the next arrival, but how many arrive in a fixed window. “Poisson Arrivals and Bursts” builds that count from the binomial, and its variance turns out to equal its mean.',
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "poisson-arrivals-and-bursts",
        "title": "Poisson Arrivals and Bursts",
        "module": "Randomness",
        "one_line": "Compute the chance a window overflows a capacity, and the capacity a burst target needs.",
        "summary": (
            "&ldquo;A thousand requests a second&rdquo; is a mean, not a schedule. Chop the "
            "second into `n` opportunities each of probability `m/n` and the count is "
            "binomial; let `n` grow and it becomes `P(k) = e^(−m)m^k/k!`, whose variance "
            "equals its mean. The burst headroom a system needs is `P(count > C)`."
        ),
        "key": [
            "count ~ Binomial(n, m/n)        n chances in the window, each small",
            "P(k) = e^(−m)m^k/k!             the limit as n grows: the Poisson count",
            "variance = mean = m             so the spread is √m",
            "m = 1000 per second             1000 ± 32, because √1000 ≈ 31.6",
            "P(count > C)                    the fraction of windows that overflow",
        ],
        "key_label": "A count in a window, and the tail above a capacity",
        "concepts_intro": (
            "One distribution, reached from the binomial you already have, and one consequence "
            "of it that decides how much headroom a queue needs."
        ),
        "concepts": [
            ("A rate is a mean, not a schedule",
             "1000 requests a second says that the expected count in a one-second window is "
             "1000. It says nothing about any particular second, and the counts in "
             "consecutive seconds vary by tens without anything having gone wrong."),
            ("The Poisson count is the binomial's limit",
             "Chop the window into `n` opportunities, each carrying an arrival with "
             "probability `m/n`. The count is `Binomial(n, m/n)` with mean `m`, exactly. As "
             "`n` grows the binomial's probabilities converge to `e^(−m)m^k/k!`, and no "
             "density or integral is needed to say so."),
            ("Variance equals the mean, so headroom scales as `√m`",
             "The binomial's variance is `m(1 − m/n)`, which climbs to `m` as the chopping "
             "gets finer. A standard deviation of `√m` means the <em>relative</em> burstiness "
             "of a big stream is smaller than that of a small one: `1000 ± 32` is a 3% "
             "wobble, while `10 ± 3.2` is a 32% one."),
        ],
        "read_title": "Counting arrivals in a window",
        "read_intro": "The binomial, its limit, the variance that follows, and the capacity a burst target buys.",
        "body": [
            ("def", ("The count in a window",
                     "Fix a window and let `m` be the expected number of arrivals in it. "
                     "Divide the window into `n` equal opportunities, each carrying one "
                     "arrival with probability `m/n`. The count `X` is "
                     "<strong>binomial</strong>, `P(X = k) = C(n,k)(m/n)^k(1 − m/n)^(n−k)`, "
                     "and its limit as `n` grows is the <strong>Poisson</strong> count "
                     "`P(X = k) = e^(−m)m^k/k!`.")),
            ("p", "Both columns are available at once, which is unusual and useful: the "
                  "binomial is exact arithmetic on fractions at any `n`, and the Poisson is "
                  "the shape it is heading for. The lab draws them over each other so that "
                  "the limit is something you watch rather than something you accept."),
            ("math", [
                "m = 10 expected in the window,  n = 200 opportunities of 1/20 each",
                "",
                "P(count > 15)   binomial, exact     0.0443556",
                "                Poisson limit       0.0487404      rounded",
                "",
                "variance        binomial  m(1 − m/n) = 10(19/20) = 19/2 = 9.5",
                "                Poisson                          m    = 10",
            ]),
            ("p", "The two tails differ in the third decimal place at `n = 200`, and the "
                  "difference is not noise: the binomial genuinely has a slightly smaller "
                  "variance, because a chopped window can hold at most `n` arrivals while a "
                  "Poisson count has no upper bound at all. Chop it finer and the two "
                  "converge."),
            ("h3", "Sizing for a burst"),
            ("p", "The design question is rarely &ldquo;what is the mean&rdquo;. It is "
                  "&ldquo;how much must this window hold so that it overflows no more than "
                  "one time in a hundred&rdquo;, and that is a tail: the smallest `C` with "
                  "`P(count > C) ≤ target`."),
            ("math", [
                "m = 10 expected arrivals in the window",
                "",
                "P(count > C) ≤ 1/100     needs C = 18        80% over the mean",
                "P(count > C) ≤ 1/1000    needs C = 21        110% over the mean",
                "",
                "and a window sized at the mean itself, C = 10:",
                "P(count > 10) is about 0.42                  two windows in five",
            ]),
            ("p", "Sizing at the mean is therefore not a conservative choice or even a "
                  "neutral one: it overflows about two windows in five. The three extra "
                  "arrivals between 15 and 18 are the difference between overflowing 4.4% of "
                  "the time and 1% of the time, which is what buying the tail costs."),
            ("p", "The `√m` scaling cuts the other way for large streams. A service taking "
                  "1000 a second has a standard deviation of about 32, so 1100 is over three "
                  "standard deviations out; a service taking 10 a second is over three "
                  "standard deviations out at 20. Consolidating ten small streams into one "
                  "big one does not change the mean load and does reduce the relative "
                  "burstiness &mdash; a first look at the pooling argument that "
                  "&ldquo;Many Servers: Pooling, and Erlang C&rdquo; makes precisely."),
            ("p", "Two limits are worth stating plainly. The Poisson column uses `e^(−m)` "
                  "summed as a series, so it is rounded and the lab bounds `m` at 12, where "
                  "the method still has its digits. The binomial column is exact fractions "
                  "and has no such bound; it is capped only by how fine a chopping stays "
                  "readable, since exactness at `n = 20m` already means denominators of "
                  "hundreds of digits."),
        ],
        "lab": ("queue", {
            "mode": "poisson",
            "mean": 10,
            "threshold": 15,
            "multiplier": 20,
            "target": 100,
            "panel_title": "Set the window and the capacity",
            "panel_intro": "The exact binomial distribution is drawn with its Poisson limit "
                           "over it, and both tails above the capacity are printed &mdash; "
                           "the first exact, the second rounded and labelled. Change how "
                           "finely the window is chopped and watch the two converge.",
        }),
        "steps_title": "Sizing a window for a burst target",
        "steps_intro": "Everything here is a tail. The mean is the input, not the answer.",
        "steps": [
            ("State the window and the mean count in it",
             "`m` is a count, not a rate: a rate of 1000 a second is `m = 1000` for a "
             "one-second window and `m = 100` for a hundred-millisecond one. The window has "
             "to be named before anything else is true."),
            ("Decide the target overflow fraction",
             "One window in a hundred, one in a thousand. This is a business decision and it "
             "is the only free parameter; everything downstream follows from it."),
            ("Find the smallest `C` whose tail is under the target",
             "Walk `C` upward and read `P(count > C)` at each step. The lab does the search "
             "and prints the answer; doing it by hand once shows how flat the tail is in that "
             "region."),
            ("Quote the headroom as a multiple of the mean, and check the `√m` scaling",
             "`C = 18` at `m = 10` is 80% headroom. The same target at a much larger `m` "
             "needs proportionally less, because the spread grows like `√m` while the mean "
             "grows like `m`."),
        ],
        "worked": {
            "title": "A window expecting ten arrivals, and how much it must hold",
            "intro": [
                "One mean, one capacity, and the two tails computed both ways so the "
                "difference between exact and rounded is visible."
            ],
            "lines": [
                "m = 10 expected arrivals in the window",
                "n = 200 opportunities, each with probability m/n = 1/20",
                "",
                "exact binomial    P(count > 15) = 0.0443556      an exact fraction",
                "Poisson limit     P(count > 15) = 0.0487404      rounded, by series",
                "",
                "variance          binomial 10(1 − 10/200) = 19/2 = 9.5",
                "                  Poisson                          10",
                "                  standard deviation about √10 ≈ 3.16",
                "",
                "sizing            P(count > C) ≤ 1/100    →   C = 18",
                "                  P(count > C) ≤ 1/1000   →   C = 21",
                "",
                "and at C = m = 10:  P(count > 10) ≈ 0.42",
            ],
            "after": [
                "Capacity 15 is 50% above the mean and still overflows one window in "
                "twenty-two. Capacity 18 is 80% above it and overflows one in a hundred. "
                "That steepness is the whole reason burst headroom is bought explicitly "
                "rather than assumed.",
                "For a faded rehearsal, keep the target at one window in a hundred and set "
                "`m = 5`. The supplied first move is that the answer must be above 5 and "
                "that the relative headroom will be <em>larger</em> than it was at `m = 10`, "
                "because the spread scales as `√m` and the mean does not. Predict the "
                "capacity, then read it off.",
            ],
        },
        "quiz_title": "Counts, spreads and headroom",
        "quiz": [
            {"q": "A service takes 1000 requests a second, Poisson. Roughly what is the standard deviation of the count in one second?",
             "a": ["`1000`", "`32`", "`100`", "`1`"],
             "c": 1,
             "why": "Variance equals the mean for a Poisson count, so the standard deviation "
                    "is `√1000 ≈ 31.6`. `1000` is the variance and the mean, not their "
                    "square root; `100` would be the answer if the variance were `m²`."},
            {"q": "A window expects 10 arrivals and can hold 15. What fraction of windows overflow?",
             "a": ["None &mdash; 15 is above the mean",
                   "About 4.4%",
                   "About 50%",
                   "About 0.1%"],
             "c": 1,
             "why": "The exact binomial tail is `0.0443556`, so about one window in "
                    "twenty-two, despite 50% headroom over the mean. Sizing at the mean "
                    "itself would overflow about 42% of windows, and 0.1% needs a capacity "
                    "of 21."},
            {"q": "Which column in the lab is computed exactly?",
             "a": ["The Poisson one, since it is the true limit",
                   "The binomial one, since it is a finite sum of exact fractions",
                   "Both, since the arithmetic is rational throughout",
                   "Neither, since both use `e`"],
             "c": 1,
             "why": "The binomial probabilities are products of rationals and are computed "
                    "as fractions. The Poisson column needs `e^(−m)`, which is summed from a "
                    "series and printed rounded &mdash; and which is why the lab bounds `m` "
                    "at 12."},
            {"q": "To hold overflow under one window in a hundred at a mean of 10, what capacity is needed?",
             "a": ["`11`", "`18`", "`15`", "`100`"],
             "c": 1,
             "why": "`C = 18` is the smallest capacity whose tail is under 1%. `15` leaves "
                    "4.4%; `11` is barely above the mean and leaves about a third; `100` "
                    "would be ten times the mean, which is the opposite error and very "
                    "expensive."},
        ],
        "mistakes": [
            ("“1000 a second” read as 1000 in each second",
             "It is a mean. The actual counts are spread around it with standard deviation "
             "about 32, so seconds carrying 1050 or 940 are ordinary and neither is an "
             "incident. Treating a rate as a schedule is the deterministic intuition of "
             "&ldquo;Why Queues Form at `ρ &lt; 1`&rdquo; in a different costume."),
            ("Sizing a window at the mean",
             "A capacity equal to the mean overflows roughly two windows in five, because a "
             "count is above its mean about half the time. Headroom is not a safety margin "
             "bolted onto a correct number; it <em>is</em> the number, and the target "
             "overflow fraction is what sets it."),
            ("Reading the Poisson column as the exact one",
             "It is the limit of the binomial and, here, a rounded series besides. The exact "
             "answer for a window chopped into `n` opportunities is the binomial, and the two "
             "differ by about a tenth of the tail at `n = 20m` &mdash; small, but not zero, "
             "and in a predictable direction."),
        ],
        "standard": ("Finish when a rate on a dashboard reads as a mean with a `√m` spread around it.",
                     "You should be able to build the count in a window as a binomial, say "
                     "what it becomes in the limit and why, compute `P(count > C)` both ways, "
                     "and size a capacity to a stated overflow target rather than to the "
                     "mean."),
        "note": 'Memoryless gaps and Poisson counts are the two halves of the same assumption, and together they name a queue: arrivals memoryless, service memoryless, one server. “The M/M/1 Queue” solves it by balancing flow across a cut, and the library&rsquo;s closed forms for `L`, `W` and the tail come from that one argument.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "the-mm1-queue",
        "title": "The M/M/1 Queue",
        "module": "The M/M/1 model",
        "one_line": "Compute πₙ, L, L_q and a tail probability at a rational utilisation, exactly.",
        "summary": (
            "One server, memoryless arrivals at `λ`, memoryless service at `μ`, room for "
            "everyone. Balancing the flow across the cut between `n` and `n + 1` gives "
            "`λπₙ = μπₙ₊₁`, so the states decay geometrically and every quantity the course "
            "needs &mdash; `L`, `L_q`, `W`, `W_q` and `P(N > k)` &mdash; follows from a "
            "geometric series."
        ),
        "key": [
            "λπₙ = μπₙ₊₁                     balance across the cut between n and n+1",
            "πₙ = (1 − ρ)ρⁿ                  so the states decay geometrically",
            "L = ρ/(1 − ρ)                   L_q = ρ²/(1 − ρ)     L − L_q = ρ",
            "W = L/λ = S/(1 − ρ)             with S = 1/μ, by Little's Law",
            "P(N > k) = ρ^(k+1)              the tail, exactly",
        ],
        "key_label": "One balance equation, and everything that follows from it",
        "concepts_intro": (
            "The derivation is three lines and a geometric series. What takes care is knowing "
            "which system it describes and which it does not."
        ),
        "concepts": [
            ("Balance across a cut, not a theory of chains",
             "Draw a line between the states with `n` in the system and those with `n + 1`. "
               "In the long run the system crosses that line upward exactly as often as "
               "downward, so `λπₙ = μπₙ₊₁`. That single conservation statement, applied at "
               "every `n`, determines the whole distribution."),
            ("Everything else is the geometric series",
             "`πₙ = ρⁿπ₀` follows immediately, and the probabilities must sum to one, so "
               "`π₀ = 1 − ρ` by Algebra's `infinite-geometric-series` &mdash; which also needs "
               "`ρ < 1`, and that is the same condition as the queue settling at all. The mean "
               "`L = Σ nπₙ` is the same series differentiated."),
            ("`L` counts the one being served",
             "`L` is the number in the <em>system</em> and `L_q` the number <em>waiting</em>, "
               "and the difference is not a rounding detail: `L − L_q = ρ` exactly, the "
               "probability that the server is busy. At `ρ = 4/5` the system holds `4` on "
               "average and `16/5` of them are queueing."),
        ],
        "read_title": "The cut, the distribution, and the four numbers that follow",
        "read_intro": "The derivation, the worked arithmetic at ρ = 4/5, and a careful statement of what this formula is and is not checked against.",
        "body": [
            ("def", ("M/M/1",
                     "Arrivals are memoryless at rate `λ`; service times are memoryless with "
                     "rate `μ`, so the mean service time is <strong>`S = 1/μ`</strong>; there "
                     "is one server, unlimited room, and customers are taken in order. `N` is "
                     "the number in the system, including the one in service, and "
                     "`πₙ = P(N = n)` in the long run. The model settles precisely when "
                     "`ρ = λ/μ < 1`.")),
            ("p", "The notation `S = 1/μ` is fixed here and used by the rest of this path: it "
                  "is the mean service time, the thing a trace measures directly, and writing "
                  "the results in terms of it is what makes the knee legible in the next "
                  "lesson."),
            ("thm", ("The stationary distribution",
                     "For `ρ = λ/μ < 1`, `πₙ = (1 − ρ)ρⁿ` for every `n ≥ 0`.")),
            ("proof", [
                "Consider the boundary between `{0, 1, …, n}` and `{n + 1, n + 2, …}`. Every "
                "crossing upward is an arrival that happens while the system holds `n`, at "
                "rate `λπₙ`; every crossing downward is a completion while it holds `n + 1`, "
                "at rate `μπₙ₊₁`. In the long run the two counts differ by at most one, so "
                "the rates are equal: `λπₙ = μπₙ₊₁`.",
                "Therefore `πₙ₊₁ = ρπₙ`, and by induction `πₙ = ρⁿπ₀`. The probabilities sum "
                "to one, so `π₀ Σ ρⁿ = 1`; the series converges exactly when `ρ < 1`, to "
                "`1/(1 − ρ)`, giving `π₀ = 1 − ρ` and `πₙ = (1 − ρ)ρⁿ`.",
                "The mean is `L = Σ nπₙ = (1 − ρ) Σ nρⁿ = (1 − ρ)·ρ/(1 − ρ)² = ρ/(1 − ρ)`, "
                "using the same geometric sum in its `Σ nrⁿ = r/(1 − r)²` form.",
            ]),
            ("p", "The tail falls out of the same geometric shape: `P(N > k) = ρ^(k+1)`, "
                  "because being above `k` means the chain climbed `k + 1` steps each costing "
                  "a factor `ρ`. `L_q` is `L` minus the one in service, `L − ρ`, which "
                  "rearranges to `ρ²/(1 − ρ)`. And `W` comes from Little's Law rather than "
                  "from any new argument: `W = L/λ`, which simplifies to `1/(μ − λ)` and "
                  "hence to `S/(1 − ρ)`."),
            ("math", [
                "λ = 4/5 per second     μ = 1 per second     S = 1/μ = 1 s",
                "ρ = λ/μ = 4/5",
                "",
                "π₀ = 1 − ρ        = 1/5",
                "π₂ = (1 − ρ)ρ²    = (1/5)(16/25) = 16/125",
                "",
                "L   = ρ/(1 − ρ)   = (4/5)/(1/5)   = 4",
                "L_q = ρ²/(1 − ρ)  = (16/25)/(1/5) = 16/5",
                "L − L_q = 4 − 16/5 = 4/5 = ρ           the one in service",
                "",
                "W   = L/λ   = 4 ÷ 4/5   = 5 s      = S/(1 − ρ)",
                "W_q = L_q/λ = (16/5) ÷ (4/5) = 4 s = W − S",
                "",
                "P(N > 3) = ρ⁴ = 256/625 ≈ 0.4096",
            ]),
            ("p", "Every one of those is an exact fraction, and the two checks in the middle "
                  "are free: `L − L_q` must be `ρ`, and `W − W_q` must be `S`. If either "
                  "fails, an arithmetic slip has happened rather than a modelling one."),
            ("h3", "What this formula is not checked against"),
            ("p", "It is tempting to say the slotted simulation of &ldquo;Why Queues Form at "
                  "`ρ &lt; 1`&rdquo; confirms these closed forms. <strong>It does not, and "
                  "the claim would be false.</strong> That simulation is a discrete-time "
                  "chain: Bernoulli arrivals with probability `p` per slot, geometric service "
                  "with parameter `q`, late arrivals. At `p = 2/5` and `q = 1/2` its server "
                  "utilisation is `p/q = 4/5`, exactly as it should be, and its exact mean "
                  "number in system is `12/5`. `ρ/(1 − ρ)` at `ρ = 4/5` is `4`. The "
                  "continuous formula overstates that system by a factor of `5/3`."),
            ("p", "The relation between the two is a <strong>limit</strong>, not an "
                  "agreement. Hold `λ` and `μ` fixed and let the slot `Δ` shrink with "
                  "`p = λΔ` and `q = μΔ`: the discrete chain's mean climbs toward "
                  "`ρ/(1 − ρ)`, and the gap closes in proportion to `Δ`."),
            ("math", [
                "λ = 4/5, μ = 1, so ρ = 4/5 and ρ/(1 − ρ) = 4",
                "",
                "Δ = 1        p = 4/5,   q = 1        exact mean  4/5      gap 16/5",
                "Δ = 1/10     p = 2/25,  q = 1/10     exact mean  92/25    gap 8/25",
                "Δ = 1/100    p = 1/125, q = 1/100    exact mean  496/125  gap 4/125",
                "",
                "each gap is exactly a tenth of the one above it: linear in Δ",
            ]),
            ("p", "The lab prints that sequence beside the closed form rather than claiming a "
                  "single slot size agrees with it. The exact finite-slot answer at each step "
                  "is Operations Research's, "
                  "`markov-chains-decisions-and-queues/queues-in-discrete-time`; what is "
                  "shown here is that it converges to this lesson's formula and how fast."),
            ("p", "The same reconciliation runs the other way. The balance argument above is "
                  "the steady state of a birth&ndash;death chain, and Operations Research "
                  "builds that chain properly in "
                  "`markov-chains-decisions-and-queues/poisson-arrivals-and-the-mm1-queue`, "
                  "recovering this distribution as its continuous-time limit. System Design "
                  "owns the closed forms &mdash; this lesson is the library's reference for "
                  "`L`, `L_q`, `W`, `W_q` and `P(N > k)` &mdash; and nothing in the two "
                  "treatments contradicts the other."),
            ("p", "Four assumptions are doing the work, and the rest of this course takes "
                  "each of them away in turn: memorylessness (&ldquo;Variability: the "
                  "Kingman Approximation&rdquo; prices getting it wrong), the single server "
                  "(&ldquo;Many Servers: Pooling, and Erlang C&rdquo;), the unlimited room "
                  "(&ldquo;Bounded Queues and Loss&rdquo;), and the steady state itself "
                  "(&ldquo;Transient Overload and Draining the Backlog&rdquo;)."),
        ],
        "lab": ("queue", {
            "mode": "mm1",
            "lam20": 16,
            "mu20": 20,
            "n": 2,
            "k": 3,
            "panel_title": "Set the two rates",
            "panel_intro": "`ρ`, `π₀`, `πₙ`, `L`, `L_q`, `W`, `W_q` and `P(N > k)` print as "
                           "exact fractions for any rational `λ` and `μ` you set. The second "
                           "table is the shrinking-slot sequence: a discrete-time chain at "
                           "three slot sizes, walking toward this formula rather than "
                           "agreeing with it.",
        }),
        "steps_title": "Computing an M/M/1 queue",
        "steps_intro": "Get ρ first. Every other quantity is a function of it alone.",
        "steps": [
            ("Compute `ρ = λ/μ` and check it is below one",
             "Above one there is no stationary distribution to compute, and the formulas "
             "return negative numbers rather than refusing. `S = 1/μ` is worth writing down "
             "at the same time."),
            ("Read off the distribution",
             "`π₀ = 1 − ρ` and `πₙ = (1 − ρ)ρⁿ`. The tail `P(N > k) = ρ^(k+1)` needs no sum: "
             "it is one power."),
            ("Take `L`, then get `L_q` by subtracting `ρ`",
             "`L = ρ/(1 − ρ)`, and `L_q = L − ρ`. Doing it in that order makes the "
             "relationship between the two visible and gives a free check."),
            ("Convert to times with Little's Law",
             "`W = L/λ` and `W_q = L_q/λ`. Check that `W − W_q = S`; if it does not, the "
             "arithmetic went wrong rather than the model."),
            ("Say which assumption you are least sure of",
             "Poisson arrivals, exponential service, one server, unlimited room. Naming the "
             "weakest one is what turns a computed number into an estimate with a direction "
             "of error."),
        ],
        "worked": {
            "title": "An M/M/1 queue at λ = 4/5, μ = 1",
            "intro": [
                "A service taking one second on average, offered work four fifths as fast as "
                "it can do it. Every figure below is exact."
            ],
            "lines": [
                "λ = 4/5 / s      μ = 1 / s      S = 1/μ = 1 s      ρ = 4/5",
                "",
                "π₀ = 1 − ρ     = 1/5                    idle a fifth of the time",
                "π₂ = (1/5)(4/5)² = 16/125",
                "",
                "L   = (4/5)/(1/5)   = 4                 in the system",
                "L_q = L − ρ = 4 − 4/5 = 16/5            waiting",
                "",
                "W   = L/λ   = 4 ÷ (4/5)     = 5 s",
                "W_q = L_q/λ = (16/5) ÷ (4/5) = 4 s",
                "check   W − W_q = 1 s = S                         ✓",
                "",
                "P(N > 3) = ρ⁴ = 256/625 ≈ 0.4096",
            ],
            "after": [
                "Read the last two lines together. The server takes one second over a "
                "request, and a request spends five seconds in the system: four of those "
                "five seconds are spent waiting behind other people, at a utilisation most "
                "capacity plans would call comfortable.",
                "And there is a 41% chance of finding four or more in the system. The mean of "
                "4 is not a typical value in any useful sense &mdash; the distribution is "
                "geometric, so it has no characteristic scale below its tail.",
                "For a faded rehearsal, take `λ = 9/10` with `μ = 1`. The supplied first move "
                "is `ρ = 9/10`, so `π₀ = 1/10`. Predict `L`, `W` and `P(N > 3)` before "
                "computing them, and notice how much moved for one tenth of extra load.",
            ],
        },
        "quiz_title": "The closed forms",
        "quiz": [
            {"q": "An M/M/1 queue runs at `ρ = 9/10`. What is `L`?",
             "a": ["`9`", "`9/10`", "`10`", "`81/10`"],
             "c": 0,
             "why": "`L = ρ/(1 − ρ) = (9/10)/(1/10) = 9`. `81/10` is `L_q`, the number "
                    "waiting; `10` is `W/S`, the response-time multiplier; `9/10` is `ρ` "
                    "itself, which is the mean number <em>in service</em>."},
            {"q": "At `ρ = 4/5` a queue holds `L = 4` on average. How many of those are waiting rather than being served?",
             "a": ["`4`", "`16/5`", "`4/5`", "`3`"],
             "c": 1,
             "why": "`L_q = L − ρ = 4 − 4/5 = 16/5`. The remaining `4/5` is the probability "
                    "the server is busy, which is exactly the mean number in service. `3` is "
                    "the tempting whole number and is not any of the quantities here."},
            {"q": "A slotted simulation with `p = 2/5` and `q = 1/2` has utilisation `4/5` and an exact mean of `12/5`, while `ρ/(1 − ρ) = 4`. What follows?",
             "a": ["The simulation has a bug, since the formula is proved",
                   "The formula is wrong, since the simulation is empirical",
                   "They are two different models &mdash; a discrete chain and its continuous limit &mdash; and they agree only as the slot shrinks",
                   "`ρ` was computed incorrectly in one of the two"],
             "c": 2,
             "why": "Both numbers are exact and both are right about their own model. The "
                    "continuous formula overstates the slotted chain by `5/3` at a slot of "
                    "one, and the gap shrinks in proportion to the slot: `4/5`, `92/25`, "
                    "`496/125` at `Δ = 1, 1/10, 1/100`, converging on `4`."},
            {"q": "What is `P(N > 2)` in an M/M/1 queue at `ρ = 1/2`?",
             "a": ["`1/8`", "`1/4`", "`1/2`", "`3/8`"],
             "c": 0,
             "why": "`P(N > k) = ρ^(k+1) = (1/2)³ = 1/8`. `1/4` is `P(N > 1)`; `1/2` is "
                    "`P(N > 0)`, which is `ρ`, the probability the server is busy at all."},
        ],
        "mistakes": [
            ("Reading `L` as the number waiting",
             "`L` counts everyone in the system, including whoever is being served. The "
             "waiting number is `L_q = ρ²/(1 − ρ)`, and the two differ by exactly `ρ`. "
             "Quoting `L` as a queue depth overstates it by the better part of a customer "
             "at high utilisation and by nearly all of it at low."),
            ("Saying this formula is checked against the slotted simulation",
             "It is not, and it must not be: the slotted system is a Geo/Geo/1 chain whose "
             "exact mean at `p = 2/5`, `q = 1/2` is `12/5`, against `4` from `ρ/(1 − ρ)`. "
             "The relationship is a limit as the slot shrinks &mdash; gaps of `16/5`, `8/25`, "
             "`4/125` at `Δ = 1, 1/10, 1/100` &mdash; and stating it as a check would be "
             "stating something false."),
            ("Applying it to a service whose variability is not exponential",
             "The `M`s are assumptions with a price. A service with very regular service "
             "times waits about half what this formula says, and one with a heavy tail waits "
             "considerably more. &ldquo;Variability: the Kingman Approximation&rdquo; puts "
             "a number on that, and the right habit here is to name the assumption "
             "whenever the result is quoted."),
        ],
        "standard": ("Finish when the whole distribution comes out of one balance equation and a geometric series.",
                     "You should be able to derive `πₙ = (1 − ρ)ρⁿ` from the cut, compute "
                     "`L`, `L_q`, `W`, `W_q` and `P(N > k)` as exact fractions at a rational "
                     "`ρ`, and state precisely why the slotted chain of &ldquo;Why Queues "
                     "Form at `ρ &lt; 1`&rdquo; does not produce `ρ/(1 − ρ)` at a finite "
                     "slot size."),
        "note": 'One rearrangement of `W = L/λ` is the most useful sentence on this course. “The Knee: Response Time vs Utilisation” reads it as `W = S/(1 − ρ)` &mdash; a hyperbola with an asymptote at `ρ = 1` &mdash; and that curve is why every capacity plan on this path names a target utilisation instead of a maximum one.',
    },
]
