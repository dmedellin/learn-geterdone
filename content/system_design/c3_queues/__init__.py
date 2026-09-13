"""Queues and Utilisation.

Course 3 of the System Design path, and the one the rest of the path leans on:
the target utilisation course 1 took on trust is earned here, and the tail
course 2 measured is explained here.

Two lessons carry an obligation settled across three subjects. "Why Queues Form
at rho < 1" names its model -- Bernoulli arrivals, geometric service, late
arrival -- and reports the exact discrete answer as Operations Research's to
derive; "The M/M/1 Queue" owns the continuous closed forms for the library and
states the agreement between them as a LIMIT, not as a check. At p = 2/5,
q = 1/2 the exact slotted mean is 12/5 while rho/(1 - rho) is 4, so the
continuous formula overstates the slotted answer by 5/3, and no lesson here may
claim the two agree at a finite slot size.
"""


from . import part_a, part_b


COURSE = {
    "slug": "queues-and-utilisation",
    "title": "Queues and Utilisation",
    "level": "Advanced",
    "summary": (
        "Why a server at 80% is nearly full: `L = λW` proved on a trace, the exponential "
        "and Poisson distributions built as limits, M/M/1 by flow balance, the knee, "
        "Kingman's variability term, pooling, bounded buffers and token buckets."
    ),
    "blurb": (
        "Why a server at 80% is nearly full, in numbers. The course opens with the one law "
        "that needs no assumptions &mdash; `L = λW`, proved on a trace by counting &mdash; "
        "builds the exponential and Poisson distributions as limits of the geometric and "
        "binomial you already have, derives M/M/1 by flow balance, and ends with the four "
        "controls a designer actually has: fewer queues with more servers, less variance, "
        "a bounded buffer, and a token bucket."
    ),
    "key": [
        "ρ = λ/μ                            a ratio of rates; μ is not a latency",
        "L = λW                             an identity; no distribution assumed",
        "πₙ = (1 − ρ)ρⁿ    L = ρ/(1 − ρ)    M/M/1, by balance across a cut",
        "W = S/(1 − ρ)                      S = 1/μ; the hyperbola and its asymptote",
        "π_K = (1 − ρ)ρ^K/(1 − ρ^(K+1))     and the admitted rate is λ(1 − π_K)",
    ],
    "assumes_short": "Courses 1 and 2; geometric and binomial distributions",
    "assumes_long": (
        "C1, C2. Discrete Mathematics `geometric-distribution`, `binomial-distribution`, "
        "`expected-value`, `hashing-and-pseudorandom-numbers`. Algebra "
        "`infinite-geometric-series`, `the-number-e`, `graphs-and-asymptotes`, "
        "`literal-equations-and-formulas`"
    ),
    "outcomes_intro": (
        "By the end you can compute the three quantities of a queue from a trace, from a "
        "model and from a simulation, locate the knee, and price each of the four controls "
        "a designer has over waiting."
    ),
    "outcomes": [
        ("Verify Little's Law on a trace and size with it",
         "Compute `L`, `λ` and `W` from arrival and departure times, check `L = λW` "
         "exactly, and solve it for a connection pool, a thread count or the throughput "
         "cap they imply."),
        ("Compute M/M/1 at a rational utilisation and find the knee",
         "`πₙ`, `L`, `L_q`, `W` and the tail `P(N > k)` as exact fractions, and the `ρ` at "
         "which the response time reaches `k` service times."),
        ("Say where the waiting comes from",
         "Bunching rather than overload &mdash; shown on a seeded slotted simulation "
         "against deterministic arrivals at the same `ρ` &mdash; and the variability term "
         "that halves the wait when the variance halves."),
        ("Price the four controls",
         "One pooled queue of `s` servers against `s` separate ones; a bounded buffer's "
         "loss, its latency cap and its admitted rate; a token bucket's admissions on a "
         "trace; and the backlog a transient spike leaves behind."),
    ],
    "syllabus_intro": (
        "The identity that needs no model comes first, then the two distributions built as "
        "limits, then the model they support, and last the four things a designer can change."
    ),
    "how_to": [
        "Do the trace lesson with pencil and paper before touching the lab. `L = λW` is a "
        "statement about an area and a sum, and seeing the two agree by counting is what "
        "stops it being a formula.",
        "Watch what the slot size does in the slotted lab. Every claim in this course about "
        "a continuous-time queue is the limit of a discrete one, and the slot control is "
        "where that limit is visible rather than asserted.",
        "Read the knee as a hyperbola, not as a table of numbers. The asymptote at `ρ = 1` "
        "is the whole content; the numbers at 0.5, 0.9 and 0.99 are three points on it.",
    ],
    "not_covered": [
        "Queueing networks, and priority disciplines beyond a mention.",
        "The Pollaczek&ndash;Khinchine derivation. Kingman's formula is stated as an "
        "approximation and the lab shows the simulation disagreeing with it.",
        "<strong>The derivation of Erlang C.</strong> It is stated in &ldquo;Many Servers: "
        "Pooling, and Erlang C&rdquo; and used there; the state-dependent birth&ndash;death "
        "chain it comes from is Operations Research "
        "`markov-chains-decisions-and-queues/multiple-servers-and-erlang-c`.",
        "Markov chains as a theory. M/M/1 here is a conservation argument across a cut, not "
        "a chapter on chains; Operations Research builds the chain.",
    ],
    "footer_lead": (
        "Utilisations, queue lengths, waiting times, blocking probabilities and token-bucket "
        "admissions on this course are exact fractions computed from the rational rates you "
        "set, so `ρ/(1 − ρ)` at `ρ = 4/5` prints as `4`, not as `3.9999999999999996`. Three "
        "figures are not exact and say so: the exponential tail `e^(−λt)`, the Poisson "
        "probabilities that use it, and Kingman's formula &mdash; whose arithmetic is exact "
        "but whose model is an approximation, which the lab demonstrates by disagreeing with "
        "the simulation."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
