"""Course 3, lessons 08-13 - the knee, variability, pooling, bounded buffers, buckets, backlog."""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-knee",
        "title": "The Knee: Response Time vs Utilisation",
        "module": "The M/M/1 model",
        "one_line": "Compute the response time at a given utilisation, and the utilisation at which it reaches k service times.",
        "summary": (
            "`W = S/(1 − ρ)` is the single most useful rearrangement on this path. Divided "
            "through by `S` it says the response time is the reciprocal of the headroom: two "
            "service times at 50%, ten at 90%, a hundred at 99%. It is a hyperbola, its "
            "asymptote is at `ρ = 1`, and nothing a designer can buy moves it."
        ),
        "key": [
            "W = S/(1 − ρ)            M/M/1's W, written in service times",
            "W/S = 1/(1 − ρ)          a hyperbola; the asymptote sits at ρ = 1",
            "ρ = 1/2 → 2      ρ = 9/10 → 10      ρ = 99/100 → 100",
            "50% to 90%  ×5           90% to 99%  ×10 more",
            "W = kS at ρ = (k − 1)/k  leaving exactly 1/k of headroom",
        ],
        "key_label": "One curve, read forwards and backwards",
        "concepts_intro": (
            "There is one function here and two ways of asking questions of it. The second way "
            "is the one capacity planning needs."
        ),
        "concepts": [
            ("Response time tracks the headroom, not the load",
             "`W/S = 1/(1 − ρ)` has `1 − ρ` in the denominator, so what determines the wait "
             "is how much of the server is <em>spare</em>. Halving the spare capacity doubles "
             "the response time regardless of where you started, which is why the same ten "
             "percentage points of load cost five times as much at the top of the range as "
             "at the bottom."),
            ("The asymptote is the whole content",
             "As `ρ` approaches one the curve rises without bound. No faster disk, no better "
             "garbage collector and no amount of tuning moves a vertical asymptote: those "
             "things change `S`, which scales the curve, while the blow-up stays exactly "
             "where it was. Algebra's `graphs-and-asymptotes` is the shape."),
            ("Planning reads the curve backwards",
             "Nobody picks a utilisation and accepts the response time that falls out. The "
             "useful direction is to name what you will tolerate &mdash; `W = kS` &mdash; and "
             "solve for `ρ = (k − 1)/k`. Tolerate four service times and you may run at three "
             "quarters; tolerate ten and you may run at nine tenths."),
        ],
        "read_title": "The hyperbola, and the target utilisation it implies",
        "read_intro": "The curve, three points on it, the inverse question, and what the last tenth of a machine actually costs.",
        "body": [
            ("p", "From the previous lesson, `W = L/λ` with `L = ρ/(1 − ρ)` gives "
                  "`W = 1/(μ − λ)`, and dividing numerator and denominator by `μ` turns that "
                  "into `W = S/(1 − ρ)` with `S = 1/μ`. It is the same quantity in the units "
                  "a designer thinks in: multiples of how long the work itself takes."),
            ("def", ("The response-time factor",
                     "`W/S = 1/(1 − ρ)` is how many service times a request spends in the "
                     "system. It is `1` at `ρ = 0` &mdash; the work and nothing else &mdash; "
                     "and it is unbounded as `ρ` approaches `1`. The <strong>knee</strong> is "
                     "not a particular point on this curve; it is the fact that the curve has "
                     "no particular point, and that the interesting region is always the last "
                     "few percent.")),
            ("math", [
                "S = 10 ms",
                "",
                "ρ = 1/2       W/S = 2          W =   20 ms",
                "ρ = 9/10      W/S = 10         W =  100 ms",
                "ρ = 99/100    W/S = 100        W = 1000 ms",
                "",
                "50% → 90%     10 ÷ 2  = 5      five times the wait",
                "90% → 99%     100 ÷ 10 = 10    ten times again",
            ]),
            ("p", "Notice what those two multipliers have in common: the first covers forty "
                  "points of utilisation and the second covers nine, and the second is the "
                  "more expensive. The utilisation axis is the wrong axis to reason on. The "
                  "headroom axis &mdash; `1 − ρ`, going `1/2`, `1/10`, `1/100` &mdash; is the "
                  "one the response time is actually a function of."),
            ("h3", "Reading it backwards: the target utilisation"),
            ("p", "Set `W = kS` and solve. `1/(1 − ρ) = k` gives `ρ = (k − 1)/k`, so the "
                  "headroom you must keep is exactly `1/k`. Tolerating twice the service time "
                  "means running at `1/2`; four times means `3/4`; ten times means `9/10`; a "
                  "hundred times means `99/100`, which is the point at which a single machine "
                  "failure in a pool is an outage rather than an event."),
            ("example", ("Where a capacity plan's target comes from",
                         "Capacity Estimation divided an offered rate by a target "
                         "utilisation rather than by `μ`, and took the target on trust. This "
                         "is where it is earned: the target is `(k − 1)/k` for whatever `k` "
                         "multiple of the service time the design is willing to pay. A plan "
                         "that names 80% has chosen `k = 5`, whether or not anybody said so.")),
            ("p", "The curve also explains a familiar and confusing incident shape. A service "
                  "at `ρ = 1/2` absorbs a doubling of traffic and moves from `2S` to `4S`, "
                  "which nobody notices. The same doubling at `ρ = 9/10` is not survivable at "
                  "all: `ρ` would be `9/5`, above one, and there is no response time to quote "
                  "&mdash; only the growth rate of &ldquo;λ, μ and ρ&rdquo;. Two systems, the "
                  "same relative "
                  "traffic change, and entirely different outcomes."),
            ("p", "Two honest caveats. The constant in `W = S/(1 − ρ)` is M/M/1's: the "
                  "`1/(1 − ρ)` shape is general and the multiplier in front of it depends on "
                  "how variable the arrivals and the service times are, which the next lesson "
                  "prices. And `W` is a mean; the percentiles that Latency and the Tail "
                  "measured sit further out still, because the number in the system is "
                  "geometrically distributed rather than concentrated around its average."),
        ],
        "lab": ("queue", {
            "mode": "knee",
            "rho100": 90,
            "service_ms": 10,
            "factor": 10,
            "panel_title": "Drag the utilisation along the curve",
            "panel_intro": "`W/S` is printed as an exact fraction at whatever `ρ` you choose, "
                           "with the asymptote drawn at `ρ = 1`. The second control asks the "
                           "inverse question: name the multiple of the service time you will "
                           "tolerate and read off the utilisation and the headroom it leaves.",
        }),
        "steps_title": "Using the curve in a capacity decision",
        "steps_intro": "Start from what you will tolerate, not from what the machine can take.",
        "steps": [
            ("Measure `S`, not the response time",
             "`S` is the service time with no queueing in it &mdash; the work itself. A "
             "measurement taken under load already contains the waiting this curve is about, "
             "and using it makes the arithmetic circular."),
            ("Name the multiple you will tolerate",
             "`k` in `W = kS`. This is a product decision expressed as arithmetic: two "
             "service times, four, ten. It is the only free parameter on the page."),
            ("Convert it to a target utilisation",
             "`ρ = (k − 1)/k`, leaving `1/k` of headroom. Quote the headroom alongside the "
             "utilisation, because the headroom is the quantity the response time depends on."),
            ("Check what a plausible surge does to that point",
             "Multiply the offered load by whatever surge the system has to survive and "
             "recompute `ρ`. If it crosses one, the plan does not have a response time, it "
             "has a growth rate."),
        ],
        "worked": {
            "title": "A 10 ms service, at three utilisations and then backwards",
            "intro": [
                "The same service, the same work, three loads &mdash; and then the question "
                "capacity planning actually asks."
            ],
            "lines": [
                "S = 10 ms        W = S/(1 − ρ)",
                "",
                "ρ = 1/2      W/S = 1/(1/2)    = 2        W =   20 ms",
                "ρ = 9/10     W/S = 1/(1/10)   = 10       W =  100 ms",
                "ρ = 99/100   W/S = 1/(1/100)  = 100      W = 1000 ms",
                "",
                "from 50% to 90%     ×5",
                "from 90% to 99%     ×10       nine points of load, ten times the wait",
                "",
                "backwards: tolerate W = 10S",
                "1/(1 − ρ) = 10   →   ρ = 9/10,  headroom 1/10",
                "",
                "tolerate W = 4S  →   ρ = 3/4,   headroom 1/4",
                "tolerate W = 2S  →   ρ = 1/2,   headroom 1/2",
            ],
            "after": [
                "The three headroom figures are the whole table restated: `1/k` of a machine "
                "kept idle buys a response time of `k` service times. Nothing else on this "
                "page is doing any work.",
                "It also shows why &ldquo;we have 10% headroom&rdquo; and &ldquo;we have 1% "
                "headroom&rdquo; are not neighbouring states. They differ by a factor of ten "
                "in response time, and the second one has no room for the variability of "
                "&ldquo;Why Queues Form at `ρ &lt; 1`&rdquo; at all.",
                "For a faded rehearsal, take `S = 4` ms and a tolerance of `W = 5S`. The "
                "supplied first move is that `k = 5` gives `ρ = 4/5`. Compute `W` at that "
                "target, then compute what `W` becomes if the service time degrades to 5 ms "
                "with the load unchanged.",
            ],
        },
        "quiz_title": "Along the hyperbola",
        "quiz": [
            {"q": "A queue runs at `ρ = 4/5`. How many service times does a request spend in the system?",
             "a": ["`5`", "`4`", "`4/5`", "`5/4`"],
             "c": 0,
             "why": "`W/S = 1/(1 − 4/5) = 5`. `4` is `L`, the mean number in the system; "
                    "`5/4` inverts the headroom the wrong way round; `4/5` is `ρ` itself."},
            {"q": "A service runs at 90% and the load grows until it runs at 99%. What happens to the mean response time?",
             "a": ["It grows by about 10%", "It is multiplied by 10", "It is multiplied by 100", "It roughly doubles"],
             "c": 1,
             "why": "`W/S` goes from `10` to `100`. The utilisation grew by nine percentage "
                    "points and the headroom fell by a factor of ten, and the response time "
                    "follows the headroom. `100` is the total factor from 50%, not from 90%."},
            {"q": "A design will tolerate a response time of four service times. What utilisation does that allow?",
             "a": ["`3/4`", "`4/5`", "`1/4`", "`4`"],
             "c": 0,
             "why": "`ρ = (k − 1)/k = 3/4`, leaving a quarter of the server idle. `4/5` is "
                    "the answer for `k = 5`; `1/4` is the headroom rather than the "
                    "utilisation."},
            {"q": "Which of these moves the asymptote of the response-time curve?",
             "a": ["Faster hardware, which lowers `S`",
                   "Tuning that removes a fixed overhead per request",
                   "Nothing &mdash; the asymptote is at `ρ = 1` whatever the service time is",
                   "A larger queue buffer in front of the server"],
             "c": 2,
             "why": "Faster hardware and tuning both reduce `S`, which scales the whole curve "
                    "down and moves `ρ` down with it for a fixed `λ` &mdash; genuinely "
                    "useful, and not a change to the asymptote. A buffer bounds the queue "
                    "rather than the utilisation, which the bounded-queue lesson prices. The "
                    "blow-up at `ρ = 1` is structural."},
        ],
        "mistakes": [
            ("Expecting response time to grow with load",
             "It grows with the reciprocal of the headroom, which is a different function "
             "entirely. A graph of `W` against `ρ` looks almost flat across most of its "
             "range and then leaves the page, and a team extrapolating linearly from two "
             "comfortable measurements will underestimate the third by an order of magnitude."),
            ("Planning to a maximum utilisation rather than a target",
             "&ldquo;The box can do 10 000 a second&rdquo; is a statement about `ρ = 1`, "
             "which is the one utilisation at which the system has no response time. The "
             "number a plan needs is `(k − 1)/k` for a stated `k`, and the difference between "
             "the two is the entire safety margin."),
            ("Quoting `W = S/(1 − ρ)` as universal",
             "The `1/(1 − ρ)` shape is general; the constant is M/M/1's. A service with very "
             "regular arrivals and durations waits less than this curve says, and one with "
             "bursty arrivals waits more. Carry the shape everywhere and carry the constant "
             "only where the assumptions hold."),
        ],
        "standard": ("Finish when a target utilisation reads as a choice of `k` in `W = kS`.",
                     "You should be able to compute `W/S` at any rational `ρ`, invert it to a "
                     "target utilisation and a headroom, explain why nine points of load cost "
                     "more than forty, and say what a plausible surge does to the point you "
                     "have chosen."),
        "note": 'The constant in front of the hyperbola is the next question. “Variability: the Kingman Approximation” splits the wait into three factors &mdash; utilisation, variability and service time &mdash; and the middle one is the only one on this course that can be halved without buying anything.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "variability-and-kingman",
        "title": "Variability: the Kingman Approximation",
        "module": "Variability and pooling",
        "one_line": "Compute the waiting time for given coefficients of variation and compare it with the exact answer.",
        "summary": (
            "Two services with the same mean service time can wait very differently, and "
            "Kingman's approximation says by how much: the queueing time factorises into "
            "utilisation, variability and service time. Halve the variability term and you "
            "halve the wait. The arithmetic is exact; the model is an approximation, and the "
            "lab shows it missing."
        ),
        "key": [
            "W_q ≈ (ρ/(1 − ρ)) · ((c_a² + c_s²)/2) · S      an approximation, not a theorem",
            "c = σ/mean       c² = 0 for clockwork, 1 for memoryless",
            "c_a² = c_s² = 1  reproduces M/M/1's W_q exactly",
            "ρ = 4/5, S = 2:  W_q = 8 at (1, 1);  4 at (1, 0)     halved",
            "at the chain's own c²:  Kingman 22/5,  exact 4        about 10% high",
        ],
        "key_label": "Three factors, of which the middle one is a design choice",
        "concepts_intro": (
            "The mean service time is not enough information to predict a wait, and this is the "
            "formula that says what else is needed."
        ),
        "concepts": [
            ("Variability is a second parameter",
             "Two queues can have identical `λ`, identical `μ` and identical `ρ` and wait "
             "differently, because one of them delivers its work in a steadier stream or "
             "finishes it in a more predictable time. The coefficient of variation `c = σ/mean` "
             "is the number that carries that difference, and it is dimensionless."),
            ("The formula factorises, which makes it a design tool",
             "`W_q` is a utilisation factor `ρ/(1 − ρ)` times a variability factor "
             "`(c_a² + c_s²)/2` times `S`. Each factor can be attacked separately: buy "
             "headroom, smooth the traffic, or make the work faster. Halving the variability "
             "term halves the wait, exactly and without buying a machine."),
            ("It is an approximation, and it is derived nowhere in this library",
             "Kingman's result is a heavy-traffic limit &mdash; it becomes accurate as `ρ` "
             "approaches one and is read here at moderate load. The arithmetic on this page "
             "is exact for rational inputs, and the <em>model</em> is what is approximate. "
             "The lab makes that concrete by putting the formula's answer next to an exact "
             "one and letting them disagree."),
        ],
        "read_title": "Utilisation × variability × service time",
        "read_intro": "The coefficient of variation, the approximation it feeds, the M/M/1 case it reproduces, and the exact answer it misses.",
        "body": [
            ("def", ("Coefficient of variation",
                     "For a positive random quantity with mean `m` and standard deviation "
                     "`σ`, the <strong>coefficient of variation</strong> is `c = σ/m`, and "
                     "`c²` is what appears in the formula below. Clockwork &mdash; every gap "
                     "or every service time identical &mdash; has `c² = 0`. A memoryless "
                     "quantity has `c² = 1`. Anything burstier than memoryless has `c² > 1`. "
                     "`c_a` describes the gaps between arrivals and `c_s` the service times; "
                     "these are the only `c`s on this course and neither is ever a count of "
                     "servers.")),
            ("p", "Kingman's approximation for a single server is then, for `ρ < 1`:"),
            ("math", [
                "W_q ≈ (ρ/(1 − ρ)) × ((c_a² + c_s²)/2) × S",
                "",
                "      utilisation      variability        the work itself",
                "",
                "ρ = 4/5, S = 2 slots",
                "",
                "c_a² = 1, c_s² = 1     (4)(1)(2)     = 8      the M/M/1 answer",
                "c_a² = 1, c_s² = 0     (4)(1/2)(2)   = 4      deterministic service",
            ]),
            ("p", "The first of those two lines is a useful check rather than a coincidence: "
                  "at `c_a² = c_s² = 1` the formula returns exactly `ρS/(1 − ρ)`, which is the "
                  "`W_q = L_q/λ` of the M/M/1 lesson. If it did not, the disagreement further "
                  "down this page would be an arithmetic bug rather than a modelling fact."),
            ("p", "The second line is the design lever. Making the service time deterministic "
                  "&mdash; same work, same duration, every time &mdash; takes `c_s²` from `1` "
                  "to `0` and halves the queueing time, at the same utilisation and the same "
                  "mean service time. Nothing was bought. An M/D/1 queue waits half of what "
                  "an M/M/1 queue waits, and the formula says so in one factor."),
            ("h3", "Where it misses, and by how much"),
            ("p", "The slotted chain of &ldquo;Why Queues Form at `ρ &lt; 1`&rdquo; has "
                  "coefficients of its own, and they are not free parameters: Bernoulli "
                  "arrivals leave geometric gaps with `c_a² = 1 − p`, and geometric service "
                  "has `c_s² = 1 − q`. At `p = 2/5` and `q = 1/2` that is `c_a² = 3/5` and "
                  "`c_s² = 1/2`. Feeding the formula its own model's coefficients is the "
                  "fairest test available."),
            ("math", [
                "p = 2/5, q = 1/2,  ρ = 4/5,  S = 1/q = 2 slots",
                "",
                "chain's own       c_a² = 1 − p = 3/5      c_s² = 1 − q = 1/2",
                "",
                "Kingman           (4)((3/5 + 1/2)/2)(2)  = 22/5 = 4.4 slots",
                "exact Geo/Geo/1   L_q/p = (8/5)/(2/5)    = 4 slots",
                "",
                "about 10% high, in the direction it is always high at moderate ρ",
            ]),
            ("p", "The formula is not wrong in the sense of a mistake; it is an approximation "
                  "being read outside the regime it was derived for, and the error it makes "
                  "is of the size approximations make. The exact answer here belongs to the "
                  "discrete chain; the Pollaczek&ndash;Khinchine formula that would give the "
                  "continuous-time answer for general service times is not derived anywhere "
                  "in this library either, and this course says so rather than implying "
                  "otherwise."),
            ("p", "The lab prints four bars: the formula at whatever coefficients you set, "
                  "the formula at the chain's own coefficients, the exact chain, and a seeded "
                  "simulation of the same chain. The simulation is a sample and moves with "
                  "the seed; the two exact bars do not move; and the gap between Kingman's "
                  "bar and the exact one is the point of the page."),
            ("p", "Used as a sensitivity tool the approximation is excellent, and that is how "
                  "to use it. It answers &ldquo;what would halving the variance of this stage "
                  "be worth?&rdquo; with a factor, and factors survive an approximate model "
                  "far better than absolute numbers do. Used as a promise it is a number with "
                  "an unstated error bar."),
            ("ul", [
                "Lower `c_s²`: make the work uniform &mdash; fixed batch sizes, a bounded "
                "unit of work, the same code path for every request.",
                "Lower `c_a²`: smooth the arrivals &mdash; a token bucket in front, jittered "
                "retries, client-side pacing rather than synchronised polling.",
                "Raise neither by accident: unbounded retries and synchronised timeouts are "
                "variability injected into `c_a²`, and this formula prices them.",
            ]),
        ],
        "lab": ("queue", {
            "mode": "variability",
            "p20": 8,
            "q20": 10,
            "ca2_halves": 2,
            "cs2_halves": 0,
            "seed": 7,
            "panel_title": "Set the variability and watch the formula miss",
            "panel_intro": "The two `c²` sliders feed Kingman's formula, whose arithmetic is "
                           "exact. Beside it are the formula evaluated at the chain's own "
                           "coefficients, the chain's exact answer, and a seeded run of the "
                           "chain itself. The disagreement between the first bars and the "
                           "third is what an approximation looks like.",
        }),
        "steps_title": "Pricing a variability change",
        "steps_intro": "Work in factors, not in absolute milliseconds, and the approximation earns its keep.",
        "steps": [
            ("Get `ρ` and `S` first",
             "The utilisation factor `ρ/(1 − ρ)` and the service time are shared by every "
             "scenario you are about to compare, so compute them once."),
            ("Estimate the two coefficients",
             "`c² = 0` for anything clockwork, `1` for anything memoryless, and above `1` for "
             "anything burstier. A measured `σ/m` from a trace is better, and for a first "
             "pass the three anchors are usually enough."),
            ("Compute the wait, and then compute it again with one factor changed",
             "The ratio between the two answers is the part of this that survives the "
             "approximation. Report the ratio, and report the absolute number only with the "
               "model named beside it."),
            ("Check the ratio against something exact where you can",
             "At `c_a² = c_s² = 1` the formula must return the M/M/1 answer, and the lab puts "
             "the exact discrete chain next to it at the chain's own coefficients. A formula "
             "that agrees where it should and misses by 10% where it should is behaving "
             "exactly as an approximation behaves."),
        ],
        "worked": {
            "title": "What deterministic service is worth at ρ = 4/5",
            "intro": [
                "One utilisation, one mean service time, and the variability factor moved from "
                "memoryless to clockwork &mdash; then the same formula held against an exact "
                "answer."
            ],
            "lines": [
                "ρ = 4/5      S = 2 slots      ρ/(1 − ρ) = 4",
                "",
                "memoryless service   c_a² = 1, c_s² = 1",
                "                     W_q = 4 × (1 + 1)/2 × 2 = 8 slots",
                "                     and this is exactly M/M/1's W_q at ρ = 4/5, S = 2",
                "",
                "clockwork service    c_a² = 1, c_s² = 0",
                "                     W_q = 4 × (1 + 0)/2 × 2 = 4 slots",
                "",
                "the saving           8 → 4, a factor of 2, with no machine bought",
                "",
                "now the fair test: the slotted chain's own coefficients",
                "p = 2/5, q = 1/2  →  c_a² = 1 − p = 3/5,  c_s² = 1 − q = 1/2",
                "",
                "Kingman              4 × (3/5 + 1/2)/2 × 2 = 22/5 = 4.4 slots",
                "exact chain          W_q = 4 slots",
            ],
            "after": [
                "The factor of two in the middle block is the lesson's design claim, and it "
                "is the one part of this page an approximation is reliable for: both answers "
                "carry the same modelling error, so the ratio between them is far better "
                "determined than either number alone.",
                "The last block is the honesty. Given the chain's true coefficients the "
                "formula still says `22/5` where the exact answer is `4`. That is an "
                "approximation behaving normally, and it is why this course states Kingman's "
                "result rather than proving it and never quotes it as an exact wait.",
                "For a faded rehearsal, keep `ρ = 4/5` and `S = 2` and set `c_a² = 2` with "
                "`c_s² = 1` &mdash; arrivals burstier than memoryless. The supplied first "
                "move is that the variability factor becomes `3/2`. Predict `W_q` and say "
                "what multiple of the M/M/1 answer it is.",
            ],
        },
        "quiz_title": "Three factors",
        "quiz": [
            {"q": "At a fixed `ρ` and `S`, service times are made perfectly regular so `c_s²` falls from 1 to 0 while `c_a²` stays 1. What happens to `W_q`?",
             "a": ["It halves", "It is unchanged", "It falls to zero", "It falls by a quarter"],
             "c": 0,
             "why": "The variability factor `(c_a² + c_s²)/2` goes from `1` to `1/2`, and it "
                    "multiplies the whole expression, so the wait halves. It does not reach "
                    "zero: the arrivals are still random, and random arrivals into a busy "
                    "server still queue."},
            {"q": "Kingman's formula is evaluated at `c_a² = c_s² = 1`. What does it return?",
             "a": ["An approximation to the M/M/1 waiting time",
                   "Exactly the M/M/1 waiting time `ρS/(1 − ρ)`",
                   "Twice the M/M/1 waiting time",
                   "The deterministic answer, since the two `c²` values cancel"],
             "c": 1,
             "why": "The variability factor is exactly `1` there, leaving `ρS/(1 − ρ)`, which "
                    "is the `W_q = L_q/λ` derived in the M/M/1 lesson. That exact agreement "
                    "is the check that makes the disagreement elsewhere on the page "
                    "meaningful."},
            {"q": "Fed the slotted chain's own coefficients, the formula says `22/5` while the chain's exact `W_q` is `4`. What does that show?",
             "a": ["The simulation was seeded badly",
                   "The arithmetic in the formula has a bug",
                   "The formula is an approximation, and this is the size of its error at moderate load",
                   "The chain's coefficients were computed wrongly"],
             "c": 2,
             "why": "Both numbers are exact arithmetic; what is approximate is the model. "
                    "Kingman's result is a heavy-traffic limit, so it is read here away from "
                    "the regime it is accurate in, and it lands about 10% high. No seed is "
                    "involved in either figure."},
            {"q": "Which of these is <em>not</em> an input to Kingman's approximation?",
             "a": ["The utilisation `ρ`",
                   "The mean service time `S`",
                   "The number of servers",
                   "The squared coefficient of variation of the arrival gaps"],
             "c": 2,
             "why": "The formula as stated here describes a single server: utilisation, the "
                    "two coefficients of variation, and the service time. Several servers is "
                    "a different model with a different instrument, which is the next "
                    "lesson."},
        ],
        "mistakes": [
            ("Believing only the mean service time matters",
             "Two stages with identical means and different spreads produce different waits, "
             "and the ratio between them can be a factor of two or more. Any latency "
             "investigation that has only measured means has not yet measured the quantity "
             "this formula is a function of."),
            ("Treating an exact calculation as an exact answer",
             "Every arithmetic step on this page is a rational operation, and the result is "
             "still approximate, because the <em>model</em> is. Fed the slotted chain's own "
             "coefficients the formula says `22/5` against an exact `4`. Quote factors, "
             "quote the model, and do not promise the absolute number."),
            ("Reading `c` as a count of servers",
             "`c_a` and `c_s` are coefficients of variation, dimensionless ratios of a "
             "standard deviation to a mean. The server count on this course is `s`, and the "
               "queue with several servers is written `M/M/s`. A `c` on this page is never a "
               "number of machines."),
        ],
        "standard": ("Finish when you can say what halving the variance of a stage is worth, as a factor.",
                     "You should be able to compute `W_q` from `ρ`, two coefficients of "
                     "variation and `S`, show that the formula reproduces M/M/1 at `c² = 1`, "
                     "say where its answer sits relative to an exact one, and name it as an "
                     "approximation every time you quote it."),
        "note": 'Variability was the first of the four controls. “Many Servers: Pooling, and Erlang C” is the second and the least intuitive: at an identical utilisation, one queue in front of several servers waits a fraction of what the same servers wait behind separate queues.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "many-servers-and-pooling",
        "title": "Many Servers: Pooling, and Erlang C",
        "module": "Variability and pooling",
        "one_line": "Compute the waiting time of one pooled queue and of s separate queues at the same load, and compare.",
        "summary": (
            "Split traffic evenly across four servers, each with its own queue, and the "
            "utilisation is identical to pooling them behind one queue &mdash; but the waiting "
            "is not. At `λ = 3`, `μ = 1` and `s = 4` the pooled queue waits `27/53` of a "
            "second where a separate queue waits `3`. Erlang C is the instrument that prices "
            "the difference."
        ),
        "key": [
            "a = λ/μ        offered load in servers        ρ = a/s",
            "C(s, a)        the chance an arrival has to wait at all",
            "L_q = C·ρ/(1 − ρ)        W_q = L_q/λ",
            "λ = 3, μ = 1, s = 4:  pooled W_q = 27/53 ≈ 0.51 s",
            "four separate queues at the same ρ = 3/4:  W_q = 3 s,  a ratio of 53/9",
        ],
        "key_label": "One queue of s servers, against s queues of one",
        "concepts_intro": (
            "The design idea is the whole lesson and the formula is only the instrument that "
            "puts a number on it."
        ),
        "concepts": [
            ("A separate queue can be idle while another waits",
             "That sentence is the entire mechanism. Four queues of one server each will, "
             "sooner or later, have a server with nothing to do while somebody waits in "
             "another line, and every such moment is capacity that was paid for and not used. "
             "One queue in front of four servers makes that state impossible."),
            ("The utilisation is identical either way",
             "Splitting `λ` four ways across four servers gives each `ρ = λ/(4μ)`, exactly "
             "the pooled `ρ = a/s`. So this is not a comparison between a busy system and a "
             "quiet one: the same work, the same servers, the same fraction of time busy, and "
             "a different amount of waiting."),
            ("Erlang C is stated here, not derived",
             "The formula below comes out of a birth&ndash;death chain whose service rate is "
             "`min(n, s)μ`, and that derivation is Operations Research, "
             "`markov-chains-decisions-and-queues/multiple-servers-and-erlang-c`. What is "
             "owned here is the design conclusion, and the formula is used as an instrument "
             "for reaching it."),
        ],
        "read_title": "Pooling, and the formula that prices it",
        "read_intro": "The offered load in servers, the Erlang C formula as stated, the worked comparison, and what pooling costs in practice.",
        "body": [
            ("def", ("Offered load, and the M/M/s queue",
                     "`M/M/s` is the M/M/1 model with `s` identical servers behind one queue. "
                     "The <strong>offered load</strong> `a = λ/μ` is measured in servers: it "
                     "is how many servers the work would keep permanently busy. The "
                     "per-server utilisation is `ρ = a/s`, and the system settles when "
                     "`ρ < 1`. The server count on this path is always `s`.")),
            ("def", ("Erlang C, stated",
                     "The probability that an arrival has to wait at all is "
                     "`C(s,a) = [a^s/(s!(1 − ρ))] ÷ [Σ_(n&lt;s) aⁿ/n! + a^s/(s!(1 − ρ))]`.",
                     "From it, `L_q = C(s,a)·ρ/(1 − ρ)` and `W_q = L_q/λ` by Little's Law. "
                     "The derivation is not given here: it is Operations Research, "
                     "`markov-chains-decisions-and-queues/multiple-servers-and-erlang-c`, and "
                     "this course's list of what it does not cover says the same.")),
            ("p", "At `s = 1` the formula collapses to `C = ρ` and the single-server "
                  "results of &ldquo;The M/M/1 Queue&rdquo;, which is the check worth doing "
                  "first on any implementation of it."),
            ("math", [
                "λ = 3 / s      μ = 1 / s per server      s = 4",
                "a = λ/μ = 3 servers' worth of work       ρ = a/s = 3/4",
                "",
                "pooled M/M/4      C(4, 3) = 27/53 ≈ 0.5094    the chance of waiting at all",
                "                  L_q = (27/53)(3) = 81/53 ≈ 1.528",
                "                  W_q = L_q/λ      = 27/53 ≈ 0.5094 s",
                "",
                "four separate M/M/1 queues, λ/4 = 3/4 each, same ρ = 3/4",
                "                  L_q = ρ²/(1 − ρ) = 9/4       per queue",
                "                  W_q = L_q/(3/4)  = 3 s",
                "",
                "3 ÷ 27/53 = 53/9 ≈ 5.9      the cost of splitting the traffic",
            ]),
            ("p", "Nearly six times the wait, for the same machines under the same load. The "
                  "split system is not overloaded and is not misconfigured; it is simply "
                  "wasting the moments when one of its servers is free and one of its queues "
                  "is not."),
            ("h3", "How the advantage moves with load"),
            ("p", "Pooling saves more seconds as the system gets busier and a larger multiple "
                  "of the wait when it is quiet, and both halves of that are worth carrying. "
                  "At `ρ = 1/2` the pooled queue waits `2/23` of a second against `1` second "
                  "separate &mdash; a ratio of `23/2` but a saving of under a second. At "
                  "`ρ = 3/4` the ratio is `53/9` and the saving is about two and a half "
                  "seconds. At `ρ = 9/10` the pooled wait is `4374/2221` against `9`, a ratio "
                  "of about `4.6` and a saving of about seven seconds."),
            ("p", "So the headline &ldquo;pooling matters most under load&rdquo; is true of "
                  "the seconds and false of the ratio, and it is the seconds that show up in "
                  "an incident. The lab prints both rows at whatever `λ`, `μ` and `s` you "
                  "set, so the two readings can be compared directly rather than argued "
                  "about."),
            ("p", "Pooling is not free, and the costs are real ones rather than rounding. A "
                  "shared queue needs a dispatcher, which is a component that can itself "
                  "queue or fail. Work that is not interchangeable &mdash; a session pinned "
                  "to a server, a cache warmed for one shard &mdash; loses locality when it "
                  "is pooled, and that shows up as a larger `S`, which the previous lesson "
                  "says is multiplied by everything. The question is whether the factor "
                  "gained on waiting exceeds the factor lost on service."),
            ("p", "The same argument explains why a few large machines usually beat many "
                  "small ones at the same total capacity, why a shared thread pool beats a "
                  "pool per endpoint, and why sharding a workload that does not need to be "
                  "sharded is a latency decision as well as a data one &mdash; which is where "
                  "Partitioning and Load Balancing picks it up."),
        ],
        "lab": ("queue", {
            "mode": "mms",
            "lam10": 30,
            "mu10": 10,
            "servers": 4,
            "panel_title": "Set the load and the servers",
            "panel_intro": "The pooled `M/M/s` row and the `s` separate `M/M/1` queues are "
                           "printed together at an identical `ρ`, with `P(wait)`, `L_q` and "
                           "`W_q` exact. Move the server count and the load and watch both "
                           "the ratio and the absolute saving change.",
        }),
        "steps_title": "Comparing a pool against a split",
        "steps_intro": "The comparison is only honest if both arms carry the same total load on the same servers.",
        "steps": [
            ("Compute the offered load in servers",
             "`a = λ/μ`. This is the number of servers the work would keep permanently busy, "
             "and it is the input Erlang C actually takes."),
            ("Get the per-server utilisation and check it",
             "`ρ = a/s < 1`, or nothing settles in either arm. Both arms have the same `ρ` by "
             "construction, which is what makes the comparison mean anything."),
            ("Compute the pooled wait",
             "`C(s,a)`, then `L_q = C·ρ/(1 − ρ)`, then `W_q = L_q/λ`. The lab prints all "
             "three exactly, and `s = 1` should reproduce M/M/1."),
            ("Compute one separate queue at `λ/s`",
             "It is an M/M/1 queue at the same `ρ`, so `L_q = ρ²/(1 − ρ)` and "
             "`W_q = L_q/(λ/s)`, the closed forms of &ldquo;The M/M/1 Queue&rdquo;."),
            ("Report both the ratio and the seconds",
             "The ratio is largest at light load and the absolute saving is largest at heavy "
             "load, and a decision usually turns on the second. Say which you are quoting."),
        ],
        "worked": {
            "title": "Four servers, one queue or four",
            "intro": [
                "Three requests a second into servers that manage one a second each. The two "
                "arrangements are indistinguishable on a utilisation dashboard."
            ],
            "lines": [
                "λ = 3 / s     μ = 1 / s each     s = 4",
                "a = λ/μ = 3            ρ = a/s = 3/4        both arrangements",
                "",
                "pooled, one queue of four servers",
                "  C(4, 3) = 27/53              the chance of waiting at all ≈ 51%",
                "  L_q     = (27/53)(3/4)/(1/4) = 81/53      ≈ 1.53 waiting",
                "  W_q     = (81/53)/3          = 27/53 s    ≈ 0.51 s",
                "",
                "split, four queues of one server, 3/4 per second each",
                "  L_q     = (3/4)²/(1/4)       = 9/4        per queue",
                "  W_q     = (9/4)/(3/4)        = 3 s",
                "",
                "ratio     3 ÷ (27/53) = 53/9 ≈ 5.9",
                "saving    3 − 27/53 = 132/53 ≈ 2.49 s per request",
            ],
            "after": [
                "Half of the pooled arrivals do not wait at all &mdash; `C(4,3) ≈ 0.51` is "
                "the chance of waiting, and the other half find a free server. In the split "
                "arrangement an arrival joins whichever line it was routed to and waits "
                "behind whatever is in it, with three idle-capable servers elsewhere.",
                "For a faded rehearsal, keep `μ = 1` and `s = 4` and drop the load to "
                "`λ = 2`. The supplied first move is `a = 2` and `ρ = 1/2`. Compute the "
                "pooled `W_q`, compare it with the separate `1` second, and notice that the "
                "ratio went up while the seconds saved went down.",
            ],
        },
        "quiz_title": "Pooling, priced",
        "quiz": [
            {"q": "Four servers handle one request a second each, and three requests a second arrive. What is `ρ` if the traffic is split evenly across four separate queues?",
             "a": ["`3/4`", "`3`", "`3/16`", "`1/4`"],
             "c": 0,
             "why": "Each server receives `3/4` a second and manages `1` a second, so "
                    "`ρ = 3/4` &mdash; identical to the pooled arrangement's `a/s = 3/4`. "
                    "That is what makes the comparison fair: the difference in waiting is "
                    "not a difference in load. `3` is the offered load `a`, measured in "
                    "servers."},
            {"q": "In that system, one pooled queue of four servers waits `27/53` of a second. What does one of four separate queues wait?",
             "a": ["`27/53` of a second, the same",
                   "`3` seconds",
                   "`4 × 27/53` of a second",
                   "`81/53` of a second"],
             "c": 1,
             "why": "A separate queue is M/M/1 at `ρ = 3/4` with `λ = 3/4`: "
                    "`L_q = 9/4` and `W_q = 3` seconds, nearly six times the pooled wait. "
                    "`81/53` is the pooled `L_q`, a count rather than a time."},
            {"q": "As the utilisation rises from `1/2` to `9/10`, what happens to the advantage of pooling?",
             "a": ["The ratio and the seconds saved both grow",
                   "The seconds saved grow while the ratio falls",
                   "Both shrink, since everything waits at high load",
                   "Neither changes; the ratio is a property of `s` alone"],
             "c": 1,
             "why": "At `ρ = 1/2` the ratio is `23/2` and under a second is saved; at "
                    "`ρ = 9/10` the ratio is about `4.6` and about seven seconds are saved. "
                    "The ratio is largest when the system is quiet, and the seconds &mdash; "
                    "which is what an incident is measured in &mdash; grow with load."},
            {"q": "What does `C(s, a)` compute?",
             "a": ["The mean number waiting",
                   "The probability that an arriving request has to wait at all",
                   "The mean waiting time",
                   "The utilisation of the busiest server"],
             "c": 1,
             "why": "It is a probability, and `L_q` and `W_q` are built from it: "
                    "`L_q = C·ρ/(1 − ρ)` and then Little's Law. At `s = 1` it reduces to "
                    "`ρ`, which is exactly the M/M/1 chance of finding the single server "
                    "busy."},
        ],
        "mistakes": [
            ("Assuming an even split is as good as a pool",
             "It is as good on a utilisation dashboard and nearly six times worse on waiting "
             "at `ρ = 3/4`. Evenness is not the issue: the loss comes from moments when one "
             "server is idle and another queue is not, and a perfectly even split still has "
             "them, because arrivals are random."),
            ("Comparing arrangements at different utilisations",
             "Quoting a pooled queue at one load against separate queues at another measures "
             "nothing. Set `a = λ/μ`, set `ρ = a/s`, and make sure the split arm carries "
             "`λ/s` into each server so that both arms sit at the same `ρ`."),
            ("Pooling work that is not interchangeable",
             "The whole argument assumes any server can take any request. Pinned sessions, "
             "warmed caches and per-shard data break that assumption, and pooling them raises "
             "`S` &mdash; which multiplies the entire waiting formula. The gain on the "
             "queueing factor has to beat the loss on the service factor."),
        ],
        "standard": ("Finish when “one queue, four servers” and “four queues, one server each” are obviously different systems to you.",
                     "You should be able to compute `a`, `ρ` and the pooled `W_q` from Erlang "
                     "C, compute a separate queue's `W_q` from the M/M/1 forms, report both "
                     "the ratio and the seconds, and say what would have to be true of the "
                     "work for pooling to be a bad trade."),
        "note": 'Pooling and variability both reduce the waiting. The third control removes it instead: “Bounded Queues and Loss” puts a limit on how many may wait, which turns latency into rejection &mdash; and changes which arrival rate Little&rsquo;s Law is entitled to use.',
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "bounded-queues-and-loss",
        "title": "Bounded Queues and Loss",
        "module": "Shedding and overload",
        "one_line": "Compute a buffer's loss, the K a loss target needs, its latency cap and its admitted rate.",
        "summary": (
            "A buffer of `K` converts waiting into dropping. The blocking probability is "
            "`π_K = (1 − ρ)ρ^K/(1 − ρ^(K+1))`, the wait can never exceed about `K·S`, and the "
            "rate that actually enters the system is `λ(1 − π_K)` &mdash; which is the rate "
            "Little's Law must be given, and the one most readers forget to use."
        ),
        "key": [
            "π_K = (1 − ρ)ρ^K/(1 − ρ^(K+1))     the fraction of TIME the system is full",
            "loss = π_K                          by PASTA, because arrivals here are Poisson",
            "admitted rate  λ_eff = λ(1 − π_K)   the rate that crosses the boundary",
            "W = L/λ_eff                         Little's Law takes the ADMITTED rate",
            "λ = 4/5, μ = 1, K = 4:  π_K = 256/2101 ≈ 12.2%",
            "W = 821/369 ≈ 2.22 s        not 4105/2101 ≈ 1.95 s",
        ],
        "key_label": "A truncated queue, and the rate that actually enters it",
        "concepts_intro": (
            "A bounded buffer is the one control on this course that makes the system worse on "
            "purpose, and the arithmetic has to keep up with that."
        ),
        "concepts": [
            ("A bound converts waiting into dropping",
             "The unbounded queue of &ldquo;The M/M/1 Queue&rdquo; makes everyone wait as "
             "long as it takes. Cap it "
             "at `K` and arrivals that find it full are refused instead: the system stops "
             "trading latency for completeness and starts trading completeness for latency. "
             "Which of the two is the better failure depends on the application, and it is a "
             "decision rather than a default."),
            ("The cap on the queue is a cap on the latency",
             "At most `K` jobs can be ahead of you, each taking about `S`, so the time in the "
             "system cannot exceed roughly `K·S` however hard the offered load pushes. That "
             "is the actual argument for a small buffer, and the argument against a large "
             "one: a buffer big enough never to drop anything is a buffer big enough to hold "
             "an unusable amount of waiting."),
            ("`L = λW` needs the rate that crosses the boundary",
             "A lossy system admits `λ(1 − π_K)` and refuses the rest. Little's Law was proved "
             "by counting the customers who actually entered, so it is the admitted rate that "
             "belongs in it. Using the offered rate produces a `W` that is too small by "
             "exactly the factor `1 − π_K`, and the error is invisible unless both numbers are "
             "printed."),
        ],
        "read_title": "Truncating the queue",
        "read_intro": "The blocking probability, the two arrival rates, the latency cap, and the buffer a loss target actually needs.",
        "body": [
            ("def", ("M/M/1/K",
                     "The M/M/1 model with room for at most `K` in the system, the one in "
                     "service included. An arrival that finds `K` present is <strong>"
                     "blocked</strong> and lost. The states `0` to `K` carry the same "
                     "geometric ratios as before, normalised over a finite sum, so "
                     "`πₙ = (1 − ρ)ρⁿ/(1 − ρ^(K+1))` and in particular "
                     "`π_K = (1 − ρ)ρ^K/(1 − ρ^(K+1))`.")),
            ("p", "One step in that definition deserves naming rather than sliding past. "
                  "`π_K` is the fraction of <em>time</em> the system is full; the loss is the "
                  "fraction of <em>arrivals</em> that find it full. Those are two different "
                  "quantities, and they are equal here because the arrivals are Poisson: a "
                  "Poisson arrival sees the system exactly as an outside observer sampling at "
                  "a random instant would. That property is called <strong>PASTA</strong> "
                  "&mdash; Poisson arrivals see time averages &mdash; and it is an "
                  "assumption of this model rather than a general truth about queues."),
            ("p", "The discrete-time chain of &ldquo;Why Queues Form at `ρ &lt; 1`&rdquo; does "
                  "<em>not</em> have it. Under the late-arrival convention a departure "
                  "resolves before the arrival in the same slot, so an arrival that meets a "
                  "full system is still admitted whenever a completion happened first, and "
                  "its blocking probability is strictly smaller than that chain's `π_K`. The "
                  "two statements look alike and are not the same statement; the discrete one "
                  "is Operations Research, "
                  "`markov-chains-decisions-and-queues/queues-in-discrete-time`, and the one "
                  "on this page is the continuous-time one."),
            ("p", "One consequence is worth stating on its own: this chain settles at every "
                  "`ρ`, including `ρ ≥ 1`. There are finitely many states and the queue cannot "
                  "grow past `K`, so there is always a stationary distribution &mdash; at "
                  "`ρ = 1` every state is equally likely, and with `K = 4` that makes the "
                  "blocking probability exactly `1/5`. Overload in a bounded system is not "
                  "unbounded growth; it is loss."),
            ("math", [
                "λ = 4/5 / s     μ = 1 / s     ρ = 4/5     K = 4",
                "",
                "π_K   = (1/5)(256/625) ÷ (1 − 1024/3125)  = 256/2101  ≈ 12.2%",
                "λ_eff = λ(1 − π_K) = (4/5)(1845/2101)     = 1476/2101 ≈ 0.703 / s",
                "L     = Σ n πₙ                            = 3284/2101 ≈ 1.563",
                "",
                "W = L/λ_eff = 3284/1476  = 821/369  ≈ 2.22 s      correct",
                "W = L/λ     = 3284/2101 ÷ (4/5)     ≈ 1.95 s      wrong",
                "",
                "the ratio between them is exactly 1/(1 − π_K) = 2101/1845",
            ]),
            ("p", "The wrong line is not a rounding difference; it is 12% low, and it is low "
                  "in the flattering direction. A team that computes it is reporting a "
                  "response time that no admitted request experiences, on a system that is "
                  "also dropping one arrival in eight. The lab prints both values side by "
                  "side and labels them, because the only reliable defence against this "
                  "mistake is seeing the two numbers together."),
            ("p", "The boundary form of the rule &mdash; that the rate in `L = λW` is "
                  "whatever crosses <em>into</em> the boundary you drew &mdash; is Operations "
                  "Research, `markov-chains-decisions-and-queues/littles-law`, which cites "
                  "this path's proof. A dropped arrival never crossed the boundary, so it "
                  "belongs in neither `λ` nor `W`."),
            ("h3", "Sizing the buffer"),
            ("p", "Loss falls quickly with `K`, and the latency cap rises with it just as "
                  "quickly, so the two constraints pull in opposite directions and the buffer "
                  "size is where they meet."),
            ("math", [
                "λ = 4/5, μ = 1, so S = 1 s",
                "",
                "K = 4      π_K ≈ 12.2%        latency cap ≈  4 s",
                "K = 14     π_K ≤ 1%           latency cap ≈ 14 s",
                "K = 24     π_K ≤ 0.1%         latency cap ≈ 24 s",
                "",
                "for comparison, the unbounded queue at the same ρ:",
                "           no loss at all     mean W = S/(1 − ρ) = 5 s, unbounded tail",
            ]),
            ("p", "That table is bufferbloat in four lines. Pushing the loss from 12% to 0.1% "
                  "costs a latency cap of twenty-four service times, and a queue that deep "
                  "delivers work whose answer stopped being wanted twenty seconds ago. The "
                  "interesting question is never &ldquo;how do we stop dropping&rdquo; but "
                  "&ldquo;which of dropping and delaying is the cheaper failure for this "
                  "request&rdquo;."),
            ("p", "For an interactive request with a client timeout, delay beyond the timeout "
                  "is loss with extra steps: the work is done, the resources are spent, and "
                  "nobody is listening. A short buffer refuses the request early enough for "
                  "the client to do something about it. For a batch pipeline with no reader "
                  "waiting, the trade runs the other way and a deep buffer is exactly right."),
            ("p", "Note also what a finite buffer does to the numbers of the previous "
                  "lessons. `L` and `W` both fall, because the worst states have been removed "
                  "from the distribution; throughput falls too, by the blocked fraction; and "
                  "the response-time curve no longer has an asymptote at `ρ = 1`, because "
                  "there is nothing left for it to blow up into."),
        ],
        "lab": ("queue", {
            "mode": "finite",
            "lam20": 16,
            "mu20": 20,
            "K": 4,
            "target": 100,
            "panel_title": "Set the buffer",
            "panel_intro": "The truncated distribution, the blocking probability, the admitted "
                           "rate and `L` print as exact fractions &mdash; and `W` prints "
                           "twice, once from the admitted rate and once from the offered one, "
                           "labelled. The gap between them is the size of the misconception.",
        }),
        "steps_title": "Sizing a bounded queue",
        "steps_intro": "Two constraints, pulling opposite ways, and one rate that has to be the right one.",
        "steps": [
            ("Compute `ρ`, and do not require it to be below one",
             "A finite buffer settles at any load. Above `ρ = 1` the answer is simply that "
             "most arrivals are refused, which is a legitimate operating point and not a "
             "failure of the model."),
            ("Get `π_K` and the admitted rate",
             "`π_K = (1 − ρ)ρ^K/(1 − ρ^(K+1))`, then `λ_eff = λ(1 − π_K)`. Write the admitted "
             "rate down next to the offered one so that the two never get confused later."),
            ("Compute `L`, then `W` from the admitted rate",
             "`W = L/λ_eff`. If you have computed `L/λ`, you have computed the wait for a "
             "population that includes requests which never entered the system."),
            ("Read the latency cap off `K`",
             "About `K·S`. This is the number the buffer was bought for, and it is the number "
             "to compare against a client timeout."),
            ("Choose `K` from a loss target, then sanity-check the cap",
             "Walk `K` up until `π_K` meets the target, then look at `K·S` and ask whether "
             "anybody still wants an answer that late. If not, the target was the wrong "
             "constraint."),
        ],
        "worked": {
            "title": "A buffer of four at ρ = 4/5, and the two waiting times",
            "intro": [
                "The same load as the M/M/1 lesson, with room for four instead of room for "
                "everyone. Both `W` values are computed so that the wrong one is recognisable."
            ],
            "lines": [
                "λ = 4/5 / s      μ = 1 / s      S = 1 s      ρ = 4/5      K = 4",
                "",
                "π_K   = (1 − ρ)ρ⁴/(1 − ρ⁵)",
                "      = (1/5)(256/625)/(1 − 1024/3125) = 256/2101 ≈ 12.2%",
                "",
                "λ_eff = (4/5)(1 − 256/2101) = 1476/2101 ≈ 0.703 / s",
                "L     = 3284/2101 ≈ 1.563",
                "",
                "W  = L/λ_eff = 3284/1476 = 821/369  ≈ 2.22 s        correct",
                "W  = L/λ                            ≈ 1.95 s        wrong, by 1/(1 − π_K)",
                "",
                "latency cap ≈ K·S = 4 s",
                "unbounded at the same ρ:  W = S/(1 − ρ) = 5 s, and no cap at all",
            ],
            "after": [
                "The buffer bought a hard ceiling of about four seconds in place of a mean of "
                "five with an unbounded tail, and it paid for it by refusing one arrival in "
                "eight. Whether that is a good trade is a question about the client, not "
                "about the queue.",
                "The two `W` lines differ by exactly `1/(1 − π_K) = 2101/1845`. That factor "
                "is the whole misconception: it is small enough to look like noise and always "
                "in the direction that makes the system look better than it is.",
                "For a faded rehearsal, keep `λ = 4/5` and `μ = 1` and set `K = 2`. The "
                "supplied first move is that `π_K` will be much larger than 12%, so the "
                "admitted rate falls further from the offered one. Compute both `W` values "
                "and the size of the factor between them.",
            ],
        },
        "quiz_title": "Loss, caps and the right λ",
        "quiz": [
            {"q": "A bounded queue blocks 12.2% of arrivals. Its mean number in the system is `L`, and the offered rate is `λ`. What is the mean time an admitted request spends inside?",
             "a": ["`L/λ`", "`L/(λ(1 − π_K))`", "`L/(λπ_K)`", "`Lλ`"],
             "c": 1,
             "why": "Little's Law counts the customers that actually entered, so the rate is "
                    "the admitted one, `λ(1 − π_K)`. Using the offered `λ` divides by too "
                    "large a number and understates `W` by exactly the factor `1 − π_K` "
                    "&mdash; here about 12%, and always in the flattering direction."},
            {"q": "What does a buffer of `K` guarantee that an unbounded queue does not?",
             "a": ["A lower mean response time at the same `ρ`",
                   "A ceiling on the time in the system, of about `K·S`",
                   "That no request is ever refused",
                   "That the utilisation stays below one"],
             "c": 1,
             "why": "At most `K` jobs can be ahead of you, so the wait cannot exceed about "
                    "`K·S` whatever the offered load does. The mean does also fall, because "
                    "the worst states were removed &mdash; but the guarantee, the thing you "
                    "can promise a client, is the ceiling."},
            {"q": "An M/M/1/K queue is offered `ρ = 1`, exactly. What happens?",
             "a": ["Nothing settles; the backlog grows without bound",
                   "It settles, with every state equally likely &mdash; at `K = 4` the blocking probability is `1/5`",
                   "The blocking probability becomes 1",
                   "The formulas are undefined at `ρ = 1`"],
             "c": 1,
             "why": "A finite chain always has a stationary distribution: there are only "
                    "`K + 1` states and nothing can grow past them. At `ρ = 1` the geometric "
                    "ratios are all one, so the distribution is uniform and the blocking "
                    "probability is `1/(K + 1)`. Unbounded growth is what happens when the "
                    "buffer is unbounded."},
            {"q": "Raising `K` from 4 to 24 takes the loss from about 12% to about 0.1%. What else changes?",
             "a": ["Nothing else &mdash; a bigger buffer is strictly better",
                   "The latency cap rises from about 4 service times to about 24",
                   "The utilisation falls",
                   "The admitted rate falls"],
             "c": 1,
             "why": "This is bufferbloat: the ceiling the buffer guarantees is about `K·S`, "
                    "so it grows with `K` exactly as the loss shrinks. The admitted rate "
                    "rises rather than falls, since less is refused, and the utilisation is "
                    "set by `λ` and `μ`."},
        ],
        "mistakes": [
            ("Using Little's Law with the offered rate",
             "The rate that crosses into a lossy system is `λ(1 − π_K)`, not `λ`. "
             "&ldquo;Little&rsquo;s Law from a Trace&rdquo; proved the identity on a trace "
             "of arrivals that actually entered, and a dropped "
             "arrival is not one of them. On the worked example the two answers are `2.22` "
             "and `1.95` seconds, and the wrong one is the smaller &mdash; which is why it "
             "survives review."),
            ("Believing a bigger buffer is always better",
             "Every unit of buffer is a unit of potential waiting, and the cap it removes is "
             "the only guarantee the buffer was providing. A buffer sized for 0.1% loss holds "
             "twenty-four service times of work, and if the client gave up after five of them "
             "that buffer is manufacturing expensive, unwanted answers."),
            ("Assuming the queue needs `ρ < 1` to settle",
             "That condition belongs to the unbounded model. A truncated chain has finitely "
             "many states and settles at every load; at `ρ = 1` with `K = 4` the states are "
             "uniform and exactly `1/5` of arrivals are blocked. Overload in a bounded system "
             "shows up as loss, not as growth."),
        ],
        "standard": ("Finish when the first thing you ask about a lossy system is which arrival rate the numbers used.",
                     "You should be able to compute `π_K`, the admitted rate, `L` and both "
                     "`W` values, choose a `K` from a loss target, state the latency cap that "
                     "`K` implies, and say why the truncated chain settles at every `ρ`."),
        "note": 'A bounded buffer refuses work only once the queue is full. “Token Buckets and Rate Limiting” refuses it earlier and on purpose, by an explicit rule about how much may be admitted in any window &mdash; and the rule is not the one most people think they are enforcing.',
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "token-buckets-and-rate-limiting",
        "title": "Token Buckets and Rate Limiting",
        "module": "Shedding and overload",
        "one_line": "Run a trace through a bucket and a fixed window, and count admissions, rejections and the largest burst each allows.",
        "summary": (
            "A token bucket admits at most `b + r·t` in any window of length `t`: a sustained "
            "rate `r` with a burst allowance `b` on top of it. A fixed window of the same "
            "nominal limit admits nearly twice the limit across a boundary &mdash; on the "
            "lesson's trace, nine in one second while advertising five."
        ),
        "key": [
            "tokens += r·Δt, capped at b        one token per admission",
            "admitted in any window of t        at most b + r·t",
            "b is a burst allowance             not a savings account: the cap is the point",
            "trace of 20, r = 5/s, b = 3        bucket admits 13; largest second 7",
            "same trace, fixed window of 5/s    admits 12; largest second 9",
        ],
        "key_label": "One limiter, and the counter it replaces",
        "concepts_intro": (
            "A rate limit is a promise about every window, not about the windows a counter "
            "happens to be keeping."
        ),
        "concepts": [
            ("A bucket accumulates permission, not requests",
             "Tokens arrive at `r` a second and each admission spends one. Because the level "
             "carries over between arrivals, the limiter has memory of how much of its "
             "allowance has recently been used &mdash; which is what lets it be precise about "
             "every window rather than about aligned ones."),
            ("`b` is the burst you are choosing to allow",
             "The level is capped at `b`, so an idle hour buys exactly `b` tokens and not one "
             "more. Without that cap a quiet night would pay for an unbounded morning and the "
             "`b + r·t` guarantee would be gone. The cap is the difference between a burst "
             "allowance and a savings account."),
            ("A fixed window is a weaker promise than it looks",
             "Counting to `limit` and resetting at each boundary admits `limit` at the end of "
             "one window and `limit` again at the start of the next, so a client that "
             "straddles the boundary gets up to twice the advertised rate in one window's "
             "width. The advertised number is true only of the windows the counter is aligned "
             "to."),
        ],
        "read_title": "The bucket, its bound, and the counter it replaces",
        "read_intro": "How a bucket admits, what it guarantees over every window, and what the same trace does to a fixed-window counter.",
        "body": [
            ("def", ("Token bucket",
                     "A bucket has a capacity `b` and refills at `r` tokens per unit time. "
                     "Between two arrivals separated by `Δt`, the level rises by `r·Δt` and "
                     "is then capped at `b`. An arrival is <strong>admitted</strong> if at "
                     "least one whole token is present, and it spends one; otherwise it is "
                     "<strong>rejected</strong> and the level is unchanged.")),
            ("thm", ("The bucket's guarantee",
                     "Over any window of length `t`, the number of admissions is at most "
                     "`b + r·t`: the tokens that were in the bucket at the start, plus the "
                     "tokens that arrived during the window.")),
            ("p", "That bound is the reason a bucket is used at all. It holds for every "
                  "window &mdash; not for aligned windows, not on average &mdash; because "
                  "every admission consumed a token, and the tokens available in an interval "
                  "are the starting level plus the refill, with the starting level capped at "
                  "`b`. With `r = 5` a second and `b = 3`, no second anywhere in any trace "
                  "carries more than `8` admissions."),
            ("math", [
                "trace: 20 arrivals over 2.2 seconds, bunched at 900 ms and 1000 ms",
                "r = 5 tokens / s      b = 3",
                "",
                "bucket        admitted 13,  rejected 7",
                "              largest second it allowed:  7      (bound is b + r = 8)",
                "",
                "fixed window at 5 per second, on the same trace",
                "              admitted 12,  rejected 8",
                "              largest second it allowed:  9      while advertising 5",
            ]),
            ("p", "The two limiters admit almost the same number of requests overall, which "
                  "is what makes the comparison interesting: they differ in <em>when</em>. "
                  "The window admitted fewer requests in total and let nine of them through "
                  "in one second, because the trace was built to straddle a boundary. The "
                  "bucket's worst second was seven, under its own bound of eight."),
            ("h3", "What the downstream service sees"),
            ("p", "The number that matters to whatever sits behind the limiter is the worst "
                  "second, not the total: it is the one that sets the queue of the previous "
                  "lessons, and a limiter advertising five that delivers nine has sized the "
                  "downstream system's headroom incorrectly by a factor of nearly two. A "
                  "bucket's worst case is `b + r·t`, which is a number you chose."),
            ("example", ("Twenty idle seconds buy three tokens",
                         "With `r = 1` a second and `b = 3`, a bucket left alone for twenty "
                         "seconds holds three tokens, not twenty. Seven arrivals at once "
                         "therefore see three admitted and four refused. The cap is what "
                         "makes `b` mean &ldquo;the burst I am willing to absorb&rdquo; "
                         "rather than &ldquo;whatever has accumulated since the last "
                         "quiet period&rdquo;.")),
            ("p", "Choosing the two parameters is a design conversation with two separate "
                  "questions in it. `r` is the sustained rate the downstream system can carry "
                  "&mdash; a capacity question, answered by the earlier courses. `b` is how "
                  "much bunching you are willing to pass through in one go, and its cost is "
                  "paid by the queue behind it: the burst arrives, and everything this "
                  "course has said about waiting says what that does to it."),
            ("p", "Two smaller points worth knowing. Rate limiting is loss, not delay: a "
                  "rejected request is refused immediately, which is a bounded, honest "
                  "failure that a client can retry &mdash; and retries are exactly the "
                  "`c_a²` that the variability lesson warns about, so they want jitter. And "
                  "a bucket can also be run as a shaper rather than a limiter, holding "
                  "arrivals until a token appears instead of refusing them, which converts "
                  "the same bound back into waiting."),
            ("p", "Token levels here are exact fractions of a token computed from integer "
                  "millisecond gaps, not floating-point approximations, so a long trace "
                  "cannot drift. That matters for a limiter more than for most arithmetic on "
                  "this course: a drift of a thousandth of a token per arrival is a different "
                  "limit after a million requests."),
        ],
        "lab": ("queue", {
            "mode": "bucket",
            "preset": "boundary-burst",
            "panel_title": "Edit the trace and the limiter",
            "panel_intro": "The token level is drawn over the trace and every arrival is "
                           "marked admitted or rejected, with the same trace through a fixed "
                           "window beneath it. Move the arrivals across a window boundary and "
                           "watch only one of the two limiters notice.",
        }),
        "steps_title": "Choosing and checking a rate limit",
        "steps_intro": "Pick the sustained rate and the burst separately; they answer different questions.",
        "steps": [
            ("Set `r` from what the downstream system can sustain",
             "This is a capacity number, and it is the one the earlier courses compute. A "
             "limiter set above the sustained capacity is a limiter that does not limit."),
            ("Set `b` from the bunching you are willing to pass",
             "The worst second the downstream service can see is `b + r`, and that is the "
             "number its headroom must cover. Choosing `b` is choosing that peak."),
            ("Run a real trace through it and count",
             "Admissions, rejections and the largest burst in any window. A trace that "
             "straddles a boundary is the one worth running, because it is the case a fixed "
             "window fails."),
            ("Check the worst window against the bound",
             "No window of length `t` may exceed `b + r·t`. If one does, the implementation "
             "is not a token bucket &mdash; most often because the level was allowed to "
             "exceed `b`."),
        ],
        "worked": {
            "title": "Twenty arrivals, a bucket and a fixed window",
            "intro": [
                "The trace bunches at 900 ms and again at 1000 ms, straddling a window "
                "boundary on purpose. Both limiters advertise five a second."
            ],
            "lines": [
                "arrivals (ms)  0 200 400 600 800  900×5  1000×5  1400 1600 1800 2000 2200",
                "",
                "token bucket   r = 5 / s      b = 3",
                "               admitted 13,  rejected 7",
                "               pattern  + + + + + + + − − − + − − − − + + + + +",
                "               largest second allowed: 7      bound b + r·1 = 8   ✓",
                "",
                "fixed window   5 per second, reset at each 1000 ms boundary",
                "               admitted 12,  rejected 8",
                "               largest second allowed: 9      advertised 5        ✗",
                "",
                "the nine: four admitted late in the first window, at 200-800 ms,",
                "          and five more the instant the counter reset at 1000 ms",
            ],
            "after": [
                "Both limiters passed about the same volume. Only one of them kept its "
                "promise about every second, and the one that did not is the one that is "
                "easier to implement &mdash; a counter and a timestamp &mdash; which is why "
                "it is so common.",
                "The bucket's worst second of seven is under its bound of eight rather than "
                "equal to it, because the trace's bunching does not line up perfectly with "
                "the refill. The bound is what you design against; seven is what this "
                "particular trace produced.",
                "For a faded rehearsal, keep the trace and set `b = 1`. The supplied first "
                "move is that the bound becomes `1 + 5 = 6` per second. Predict whether the "
                "total admitted goes up or down, and what happens to the largest second.",
            ],
        },
        "quiz_title": "Buckets and windows",
        "quiz": [
            {"q": "A bucket refills at `r = 5` tokens a second with capacity `b = 3`. What is the most it can admit in any one second?",
             "a": ["`5`", "`8`", "`3`", "`13`"],
             "c": 1,
             "why": "`b + r·t` with `t = 1` second is `3 + 5 = 8`: the three tokens that "
                    "could have been sitting there plus the five that arrive during the "
                    "second. `5` is the sustained rate, which is the promise a fixed-window "
                    "counter fails to keep, and `3` is the burst allowance alone."},
            {"q": "On the lesson's trace, what was the largest number of requests the fixed window let through in a single second?",
             "a": ["`5`", "`9`", "`12`", "`20`"],
             "c": 1,
             "why": "Nine: the four it admitted late in the first window, at 200 to 800 ms, "
                    "and the five it let through the instant the counter reset at 1000 ms. "
                    "`12` is the total it admitted over the whole "
                    "trace, and `5` is what it advertises. This is the boundary burst, and it "
                    "is why a counter is a weaker promise than a bucket."},
            {"q": "A bucket with `r = 1` a second and `b = 3` has been idle for twenty seconds. How many arrivals can it admit back to back?",
             "a": ["`3`", "`20`", "`23`", "`1`"],
             "c": 0,
             "why": "The level is capped at `b = 3`, so twenty idle seconds buy three tokens "
                    "rather than twenty. Without the cap the `b + r·t` guarantee would not "
                    "hold at all, and a long quiet period would licence an arbitrarily large "
                    "burst afterwards."},
            {"q": "A request is rejected by a rate limiter. What has the system done?",
             "a": ["Delayed it until capacity is available",
                   "Refused it immediately, which is loss rather than waiting",
                   "Queued it behind the admitted requests",
                   "Reduced the sustained rate for later requests"],
             "c": 1,
             "why": "A limiter refuses; it does not hold. That is a bounded and honest "
                    "failure the client can act on, and it is the same trade as the bounded "
                    "queue of the previous lesson. A bucket run as a <em>shaper</em> holds "
                    "arrivals instead, which converts the same bound back into waiting."},
        ],
        "mistakes": [
            ("“100 per second” read as at most 100 in any one second",
             "A fixed-window counter guarantees that only for windows aligned to its own "
             "boundaries; across a boundary it admits up to twice the limit, and on the "
             "lesson's trace a limit of five delivered nine. If the promise needs to hold for "
             "every second, the limiter has to be a bucket or a sliding window."),
            ("Letting the token level exceed `b`",
             "An implementation that accumulates tokens without a cap turns a burst allowance "
             "into a savings account, and the `b + r·t` bound fails by however long the "
             "system was quiet. The cap is applied when the level is topped up, before the "
             "arrival is charged."),
            ("Sizing the downstream system for `r` rather than for `b + r`",
             "The limiter's worst second is `b + r·t`, and that is the load the queue behind "
             "it actually sees. Sizing that queue for the sustained rate alone leaves it "
               "exposed to exactly the bursts the limiter was configured to permit."),
        ],
        "standard": ("Finish when you would ask “over which window?” before accepting any rate limit.",
                     "You should be able to run a trace through a bucket by hand, state the "
                     "`b + r·t` bound and check a trace against it, show how a fixed window "
                     "doubles its advertised limit across a boundary, and choose `r` and `b` "
                     "from two separate design questions."),
        "note": 'Limiters and buffers both assume the overload is something to refuse. The last lesson takes the other case: the surge is legitimate, it is accepted, and “Transient Overload and Draining the Backlog” measures what it leaves behind and how long the system takes to give it back.',
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "transient-overload-and-backlog",
        "title": "Transient Overload and Draining the Backlog",
        "module": "Shedding and overload",
        "one_line": "Compute the peak backlog, the drain time and the worst consumer lag from a piecewise arrival rate.",
        "summary": (
            "Every formula so far assumed a steady state. A spike above `μ` has none: it "
            "accumulates a backlog equal to the area of `λ − μ` over its duration, and that "
            "area drains afterwards at whatever headroom is left. A sixty-second spike can be "
            "a three-and-a-half-minute incident, and the worst lag arrives at the moment the "
            "spike ends."
        ),
        "key": [
            "backlog = area of (λ − μ) over the spike     500/s × 60 s = 30 000",
            "drains at the headroom μ − λ_after            1000 − 800 = 200 / s",
            "drain time = backlog ÷ headroom               30 000 ÷ 200 = 150 s",
            "worst lag  = backlog ÷ μ                      30 000 ÷ 1000 = 30 s",
            "total episode = 60 + 150 = 210 s              three and a half times the spike",
        ],
        "key_label": "An area, and the two divisions that drain it",
        "concepts_intro": (
            "Three quantities, each a division of the same area, and none of them is a steady "
            "state."
        ),
        "concepts": [
            ("A backlog is an area, not a rate",
             "While `λ > μ` the amount waiting grows at `λ − μ` per second, so the total left "
             "at the end of the spike is that excess multiplied by how long it lasted. Two "
             "spikes with the same peak and different durations leave completely different "
             "backlogs, and the peak alone does not predict the incident."),
            ("It drains at the headroom, not at `μ`",
             "Once the spike ends the consumer is still receiving `λ_after`, so only "
             "`μ − λ_after` per second is available to work through the backlog. Headroom, "
             "again: the same quantity the knee was a function of, doing the same job in a "
             "different form."),
            ("The lag peaks when the spike ends",
             "Consumer lag &mdash; how far behind the newest message the reader is, in time "
             "&mdash; is the backlog divided by `μ`. It rises throughout the spike, reaches "
             "its worst at the instant the arrival rate returns to normal, and only then "
             "starts to fall. Latency does not recover when the spike ends; it recovers when "
             "the area does."),
        ],
        "read_title": "The area a spike leaves behind",
        "read_intro": "What accumulates, what drains it, how long that takes, and why the worst moment is after the surge is over.",
        "body": [
            ("def", ("The episode",
                     "A system drains at `μ`. The arrival rate is `λ_before` until the spike, "
                     "`λ_spike` for `d` seconds, then `λ_after`. The <strong>excess</strong> "
                     "is `λ_spike − μ`, the <strong>peak backlog</strong> is that excess times "
                     "`d` when positive and zero otherwise, the <strong>headroom</strong> "
                     "afterwards is `μ − λ_after`, and the <strong>drain time</strong> is the "
                     "backlog divided by the headroom.")),
            ("p", "Two conditions are worth checking before any of it: the system must have "
                  "been stable before the spike, or the backlog did not start at zero; and "
                  "the headroom afterwards must be positive, or there is no drain time at all "
                  "and the backlog is permanent."),
            ("math", [
                "μ = 1000 / s     λ_before = 800 / s",
                "λ_spike = 1500 / s for d = 60 s      λ_after = 800 / s",
                "",
                "excess    1500 − 1000 = 500 / s",
                "peak      500 × 60    = 30 000 waiting, at the end of the spike",
                "headroom  1000 − 800  = 200 / s",
                "drain     30 000 ÷ 200 = 150 s",
                "lag       30 000 ÷ 1000 = 30 s        the worst a consumer is behind",
                "total     60 + 150      = 210 s",
            ]),
            ("p", "A minute of overload, three and a half minutes of incident. The asymmetry "
                  "is entirely in the two rates: work arrived 500 a second faster than it "
                  "could be handled and leaves only 200 a second faster, so every second of "
                  "the spike costs two and a half seconds of recovery."),
            ("p", "That ratio is the useful generalisation: the recovery is "
                  "`excess ÷ headroom` times the length of the spike. Systems run close to "
                  "`μ` have very little headroom, so their recovery multiplier is large "
                  "&mdash; another form of the knee, and another reason a target utilisation "
                  "is chosen rather than a maximum one."),
            ("h3", "What the consumer sees"),
            ("p", "The backlog rises linearly to `30 000` at `t = 60`, then falls linearly to "
                  "zero at `t = 210`, so at `t = 30` it is `15 000` on the way up and at "
                  "`t = 135` it is `15 000` again on the way down. Lag follows the same shape "
                  "divided by `μ`: nothing, then thirty seconds at the moment the surge ends, "
                  "then a slow return. An alert on lag fires late in the spike and clears "
                  "long after it, which is exactly what the arithmetic says should happen."),
            ("example", ("A spike with nowhere to drain",
                         "Keep everything the same but let the arrival rate return to `1000` "
                         "rather than `800`. The headroom is now zero, the drain time is "
                         "undefined, and the 30 000 that accumulated is permanent: the "
                         "system is stable in the sense that the backlog stops growing, and "
                         "the lag stays at thirty seconds for ever. Recovery is not a "
                         "property of a spike ending; it is a property of the headroom that "
                         "follows it.")),
            ("example", ("A spike that is not one",
                         "A surge to `900` a second against `μ = 1000` builds nothing at all, "
                         "however long it lasts. There is no excess, so there is no area. "
                         "What that surge does do is raise `ρ` from `4/5` to `9/10`, which "
                         "the knee says multiplies the response time by two &mdash; a real "
                         "effect, and a different one from a backlog.")),
            ("p", "The controls are the familiar ones, in a new arrangement. More headroom "
                  "shortens the drain and every other quantity on this page. A bounded queue "
                  "or a token bucket caps the area by refusing part of the spike, trading the "
                  "backlog for loss. And smoothing the arrivals &mdash; the variability "
                  "lesson's `c_a²` &mdash; reduces how much of a surge is a spike at all."),
            ("p", "This is also the lesson that says when the rest of the course applies. "
                  "Every steady-state formula here describes a system whose load has been "
                  "constant long enough to settle; during a spike, none of them is true, and "
                  "the honest calculation is the area. Afterwards they become true again, "
                  "which is what the drain time is measuring &mdash; the time until the "
                  "model's assumption is met."),
        ],
        "lab": ("queue", {
            "mode": "backlog",
            "mu": 1000,
            "before": 800,
            "spike": 1500,
            "duration": 60,
            "after": 800,
            "panel_title": "Shape the episode",
            "panel_intro": "Set the drain rate and the three arrival rates and the accumulated "
                           "area, its peak, the drain time and the lag curve are drawn "
                           "together. Take the headroom after the spike to zero and watch the "
                           "drain time disappear rather than grow large.",
        }),
        "steps_title": "Working out an overload episode",
        "steps_intro": "Everything is one area and two divisions, in this order.",
        "steps": [
            ("Check the system was stable before the spike",
             "`λ_before < μ`. If it was not, the backlog did not start at zero and the peak "
             "is larger than the area of the spike alone."),
            ("Compute the excess and multiply by the duration",
             "`(λ_spike − μ) × d` is the peak backlog, and it occurs at the end of the spike "
             "rather than at its start. A negative excess means no backlog at all."),
            ("Compute the headroom afterwards",
             "`μ − λ_after`. If this is zero or negative, stop: there is no drain time, and "
             "the backlog is permanent until something else changes."),
            ("Divide twice",
             "Backlog over headroom is the drain time; backlog over `μ` is the worst lag. The "
             "total episode is the spike plus the drain."),
            ("Compare the total with whatever it is measured against",
             "A retention window, an alerting threshold, a customer's patience. The answer "
             "that matters is rarely the peak backlog itself but the time the system spends "
             "away from normal."),
        ],
        "worked": {
            "title": "A sixty-second spike, and the three minutes after it",
            "intro": [
                "A consumer that drains a thousand a second, a steady eight hundred, and one "
                "minute at fifteen hundred."
            ],
            "lines": [
                "μ = 1000 / s      λ_before = 800 / s      stable before: 800 < 1000  ✓",
                "λ_spike = 1500 / s for 60 s               λ_after = 800 / s",
                "",
                "excess     1500 − 1000  =   500 / s",
                "peak       500 × 60     = 30 000          reached at t = 60 s",
                "",
                "headroom   1000 − 800   =   200 / s",
                "drain      30 000 ÷ 200 =   150 s",
                "total      60 + 150     =   210 s",
                "",
                "worst lag  30 000 ÷ 1000 =   30 s         also at t = 60 s",
                "",
                "backlog at t = 30   15 000        rising",
                "backlog at t = 60   30 000        the peak",
                "backlog at t = 135  15 000        falling",
                "backlog at t = 210       0        recovered",
            ],
            "after": [
                "The two halves of the episode are not symmetric and nothing makes them so. "
                "The backlog is built at 500 a second and removed at 200, so it takes two and "
                "a half times as long to leave as it took to arrive.",
                "Note where the worst lag sits: at `t = 60`, the instant the arrival rate "
                "returns to normal. A dashboard watched during the surge shows lag still "
                "climbing as the traffic falls, which is confusing only if the backlog is "
                "being thought of as a rate rather than as an area.",
                "For a faded rehearsal, keep everything but let the spike last thirty seconds "
                "instead of sixty. The supplied first move is that the excess is unchanged at "
                "500 a second, so the peak halves. Predict the drain time, the worst lag and "
                "the total episode before computing them.",
            ],
        },
        "quiz_title": "Areas, drains and lag",
        "quiz": [
            {"q": "A consumer drains 1000 a second. Arrivals run at 1500 a second for 60 seconds. What is the peak backlog?",
             "a": ["`30 000`", "`90 000`", "`500`", "`60 000`"],
             "c": 0,
             "why": "The excess is `1500 − 1000 = 500` a second, over 60 seconds, so the area "
                    "is `30 000`. `90 000` is the arrivals during the spike; `500` is the "
                    "excess rate rather than the accumulated amount."},
            {"q": "After that spike the arrival rate returns to 800 a second. How long does the backlog take to drain?",
             "a": ["`30` seconds", "`150` seconds", "`210` seconds", "`60` seconds"],
             "c": 1,
             "why": "The headroom is `1000 − 800 = 200` a second, and `30 000 ÷ 200 = 150` "
                    "seconds. `210` is the whole episode including the spike itself; `30` is "
                    "the worst lag, which is the backlog divided by `μ` rather than by the "
                    "headroom."},
            {"q": "In the same episode, when is the consumer furthest behind?",
             "a": ["At the start of the spike",
                   "At the moment the spike ends",
                   "Halfway through the drain",
                   "When the backlog reaches zero"],
             "c": 1,
             "why": "The backlog rises for as long as `λ > μ` and falls afterwards, so it "
                    "peaks exactly when the arrival rate returns to normal &mdash; at 30 "
                    "seconds of lag here. Latency recovers when the area is gone, not when "
                    "the traffic subsides."},
            {"q": "The same spike occurs, but afterwards the arrival rate settles at exactly `μ` rather than below it. What happens?",
             "a": ["The backlog drains, only more slowly",
                   "The backlog never drains &mdash; there is no headroom to drain it with",
                   "The backlog grows without bound",
                   "The lag returns to zero as soon as the spike ends"],
             "c": 1,
             "why": "The drain rate is the headroom `μ − λ_after`, which is now zero. The "
                    "backlog stops growing and never shrinks, so the lag stays at thirty "
                    "seconds indefinitely. Recovery is a property of the headroom after the "
                    "spike, not of the spike ending."},
        ],
        "mistakes": [
            ("Expecting latency to recover when the spike ends",
             "The spike ending stops the backlog growing. Removing it takes `backlog ÷ "
             "headroom`, which on the worked example is two and a half times as long as the "
             "spike itself. The worst moment of the incident is the first moment of the "
             "recovery, and an alert that clears when traffic normalises is clearing early."),
            ("Sizing from the peak rate instead of the area",
             "Two spikes with the same peak and different durations leave different "
             "backlogs, and it is the backlog that sets the lag and the drain. Multiply the "
             "excess by the duration; a very high spike for two seconds may be a smaller "
             "event than a mild one for ten minutes."),
            ("Using a steady-state formula during the surge",
             "`W = S/(1 − ρ)` describes a system that has settled, and a system with "
             "`ρ > 1` has not and will not. During the spike the honest calculation is the "
             "accumulating area; the steady-state results become applicable again only once "
             "the backlog has drained."),
        ],
        "standard": ("Finish when a spike reads as an area with a recovery multiplier attached to it.",
                     "You should be able to compute the peak backlog, the drain time, the "
                     "worst lag and the total episode from a piecewise arrival rate, say when "
                     "there is no drain time at all, and explain why the steady-state "
                     "formulas of this course do not apply while it is happening."),
        "note": 'That closes the four controls and the course. Every number here has been a consequence of `ρ` and of how irregularly work arrives; the next course changes `λ` at the source instead. “Caching and Hit Rates” asks what a cache is worth, and the answer is that a hit rate of `h` sends `(1 − h)λ` to the backend &mdash; a utilisation problem wearing different clothes.',
    },
]
