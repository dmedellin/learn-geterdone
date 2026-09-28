"""Simulation and Variance Reduction."""


from . import part_a, part_b


COURSE = {
    "slug": "simulation-and-variance-reduction",
    "title": "Simulation and Variance Reduction",
    "level": "Advanced",
    "summary": (
        "What to do when no exact method applies: run the model, and then refuse to "
        "pretend the number that came out is the answer. A seeded stream becomes draws, "
        "draws become an estimate, and the estimate arrives with a width attached "
        "&mdash; the only width this path can justify, which is Chebyshev's and says so. "
        "Then a queue run as an event calendar, the bias a run started empty puts in its "
        "own average, and four ways to make the width narrower without buying draws, "
        "each of them a covariance being moved and two of them shown failing."
    ),
    "blurb": (
        "Every other course on this path ends in a proof: a tableau is optimal, a corner "
        "is whole, a sequence is best by an exchange argument, a steady state is the "
        "solution of a linear system. This one ends in an interval. Simulation is the "
        "method of last resort, and what makes it a method rather than a guess is the "
        "discipline around the number it produces &mdash; a stream whose period has been "
        "certified, an estimator whose bias has been computed rather than hoped away, a "
        "guarantee that assumes nothing about the distribution, and a variance reduction "
        "measured against the honest comparison instead of the flattering one. The "
        "hazard the whole path warns about bites hardest here, because the output now "
        "carries sampling noise on top of it: a simulation of the wrong model is wrong "
        "in a way that more runs make look more convincing."
    ),
    "key": [
        "xₙ₊₁ = (a·xₙ + c) mod m,  U = x/m",
        "   the cumulative table IS the sampler",
        "Var(X̄ₙ) = σ²/n  ⟹  four times the runs",
        "   for half the width, and no cheaper way",
        "P(|X̄ − μ| ≥ k·SE) ≤ 1/k²",
        "   k = 5 guarantees 24/25 = 96%, ±2 SE 3/4",
        "bias is where the estimate is AIMED;",
        "replications shrink variance, not bias",
        "Var(A − B) = Var A + Var B − 2 Cov(A, B)",
        "   one stream fed to both systems",
        "b* = Cov(X, C)/Var C, and the variance",
        "is then multiplied by 1 − ρ²",
        "E_p[h] = E_q[h · p/q]  provided q > 0",
        "   wherever p·h is; else no estimator",
    ],
    "assumes_short": "Linear Programming Models through Markov Chains, Decisions and Queues; expectation, variance and the seeded generator",
    "assumes_long": (
        "this whole path, and Markov Chains, Decisions and Queues above all: the slotted "
        "queue four of these lessons run is the chain that course solves exactly, and "
        "the long-run mean every run here is measured against is its answer rather than "
        "this course's. From discrete mathematics, Discrete Probability in full "
        "— random variables, expected value, linearity of expectation, variance and "
        "standard deviation as the source of Chebyshev's inequality, the Bernoulli and "
        "binomial distributions, and the geometric distribution as a waiting time — "
        "together with Hashing and Pseudorandom Numbers from Number Theory and "
        "Cryptography, which is where the linear congruential generator and the "
        "Hull-Dobell conditions are built. From algebra, square roots kept in surd "
        "form, because the standard error is one and this course prints it exactly "
        "before it rounds it"
    ),
    "outcomes_intro": (
        "By the end you can build a sampler and certify the stream underneath it, attach "
        "a defensible interval to a simulated number and say what the interval assumes, "
        "run a system as an event calendar and remove the bias its starting state put in "
        "the answer, and apply four variance-reduction techniques while measuring each "
        "against the comparison that could refute it."
    ),
    "outcomes": [
        ("Sample a distribution exactly, and check the stream first",
         "A linear congruential generator run by hand, its period certified or refuted "
         "against the Hull-Dobell conditions, and inverse-transform sampling from a "
         "cumulative table with every comparison made in whole numbers &mdash; plus the "
         "index shortcut that samples the uniform distribution whatever table is on the "
         "page."),
        ("Report an estimate with a width, and say what the width guarantees",
         "The sample mean and sample variance as exact fractions, the standard error as "
         "a surd rounded once for printing, `n = σ²/SE²` as the budget, and Chebyshev's "
         "`1 − 1/k²` in place of a normal approximation that has not been built &mdash; "
         "with both prices of the wider guarantee, `k/2` in width and `(k/2)²` in runs."),
        ("Run a system as an event calendar",
         "A state, a calendar and a clock that jumps to the next scheduled event; a "
         "tie-breaking rule stated once and obeyed everywhere; the area under the "
         "occupancy curve read twice, as a time average and as `λ` times `W`; and a "
         "single run understood as one observation of a random quantity."),
        ("Separate bias from variance, and cure each with the right tool",
         "The exact expected occupancy of a chain started empty, the expected average "
         "over a window with and without a warm-up discard, the measured fact that "
         "deleting the transient beats diluting it, and batch means as replications out "
         "of one run with the condition that makes them legitimate."),
        ("Move a covariance instead of buying draws",
         "Common random numbers on a two-system comparison, antithetic pairing in the "
         "case where it removes the whole variance and the case where it exactly doubles "
         "it, and a control variate with its coefficient at the vertex of an exact "
         "quadratic and the factor `1 − ρ²` printed as the rational it is."),
        ("Estimate a rare event, and refuse the proposals that cannot be used",
         "The reweighting identity and the support condition that the derivation itself "
         "forces, a tilted proposal that divides the variance by about `123`, one that "
         "multiplies it by about `9546` while remaining perfectly unbiased, and a "
         "distribution with a hole in its support that yields no estimator at all."),
    ],
    "syllabus_intro": (
        "The stream first, because every figure on the course is a function of it and a "
        "sampler is only as good as the period underneath it. Then the estimate and its "
        "error bar, in that order and on the same table, so that the interval is met as "
        "a property of an estimator rather than as a convention. Then a system rather "
        "than a table &mdash; a queue as an event calendar, and the bias that running it "
        "from an empty start puts in its own average, which is the one defect no amount "
        "of care about the generator can touch. And last the four variance-reduction "
        "techniques, grouped because they are one idea in four costumes: every one of "
        "them moves a covariance, and the one that changes the sampling distribution "
        "itself comes last because it is the only one that can make things enormously "
        "worse."
    ),
    "how_to": [
        "Print the width beside the number, every time, from the first lesson onward. "
        "An estimate with no standard error attached makes no claim that can be checked, "
        "and every technique in the second half of this course is a technique for making "
        "that width smaller &mdash; which cannot be demonstrated, or refuted, on a page "
        "that never printed it.",
        'Name the inequality behind an interval. &ldquo;A 95% confidence interval&rdquo; on a simulation output is a claim about a normal approximation nobody has justified; &ldquo;Chebyshev at `k = 5`, so coverage at least `24/25` whatever the distribution&rsquo;s shape&rdquo; is a claim a reader can evaluate and, if they disagree, refuse. The lab of &ldquo;How Sure? Chebyshev&rsquo;s Bound&rdquo; prints the guarantee and the observed coverage side by side so that the two can never be quietly merged.',
        "Ask whether a problem is bias or variance before reaching for a cure. "
        "Replications, longer runs and every technique on the second half of this course "
        "attack variance. A run started in the wrong state is aimed at the wrong number, "
        "and a thousand replications of it give a beautifully narrow interval centred in "
        "the wrong place.",
        'Measure a variance reduction against the comparison that could refute it. An antithetic pair costs two draws, so it is compared with an independent pair and not with one draw; a paired comparison is judged on `Var(A − B)` and not on `Var A`; a control variate is judged on `1 − ρ²` and not on the estimate it produced. Two of the four techniques here are shown failing on the same page that shows them working, and both failures are invisible to any comparison that flatters the method.',
        "Reseed before believing anything, including a variance reduction. The reduction "
        "factor is itself a ratio of two sample variances: on the measured pairing it is "
        "`2.604` at one seed, `5.770` at another and `1.823` at a third. What is stable "
        "is the sign of the covariance; the size is a measurement, and quoting it to "
        "three figures from one run is the habit this course opens by warning about.",
    ],
    "not_covered": [
        "Continuous-time simulation, and every distribution that needs one. Exponential "
        "interarrivals, Poisson processes and continuous service times are where "
        "next-event simulation genuinely differs from a fixed-tick loop; the model here "
        "is slotted, the two methods agree slot for slot on it, and that is said "
        "positively on the page rather than hidden.",
        "Confidence intervals from the central limit theorem. The normal approximation "
        "is the reason `±2 SE` is usually quoted with `95%` attached, and this path has "
        "not built it. The cost of doing without it is printed rather than absorbed: "
        "`5/2` in width and `25/4` in runs, on the page that makes the trade.",
        "Choosing a warm-up length by a procedure. Welch's method, the marginal-standard-"
        "error rule and the rest are real techniques with real literature; what this "
        "course does instead is compute the bias exactly on a chain small enough to "
        "carry forward, so that the reader has seen what the procedures are trying to "
        "estimate before meeting one.",
        "Stratification, conditional Monte Carlo, quasi-random sequences, and adaptive "
        "importance sampling. All four are variance reduction and all four need "
        "machinery this path does not have &mdash; a partition with known probabilities, "
        "a conditional expectation available in closed form, discrepancy bounds, or an "
        "iterative fit of the proposal. Naming them is as far as this course goes.",
        "Anything that needs a random number generator fit for cryptography. An LCG is "
        "trivially predictable from a few outputs, which is fine for a simulation and "
        "fatal for a key; the distinction belongs to Number Theory and Cryptography and "
        "is not reopened here.",
        '<strong>The two results this course cites and does not prove.</strong> Chebyshev&rsquo;s inequality, whose statement is Discrete Mathematics&rsquo; in &ldquo;Variance and Standard Deviation&rdquo; and whose two-line derivation from Markov&rsquo;s inequality belongs to the Algorithms path, in Randomised Algorithms; and the Hull&ndash;Dobell conditions, which &ldquo;Hashing and Pseudorandom Numbers&rdquo; states and does not prove either. Both are named where they are used, with their owners.',
    ],
    "footer_lead": (
        "Every draw, count, frequency, sample mean, sample variance, covariance, "
        "coverage count, transient expectation and variance ratio on this course is an "
        "exact fraction, because the stream is integers and the sampled values are "
        "rational: a sample mean over two hundred draws prints as `413/200` and a "
        "coverage as `40` of `40`. Three quantities here are not rational in general "
        "&mdash; the standard error `√(s²/n)`, the Chebyshev half-width `k·SE` built on "
        "it, and `ρ` &mdash; and each is carried as an exact surd and printed with its "
        "decimal labelled <em>rounded</em>; where the radicand happens to be a perfect "
        "square the exact form is a fraction and nothing is rounded at all. Every other "
        "decimal on these pages says &ldquo;exact, shown to `N` places&rdquo; instead, "
        "and the distinction is load-bearing rather than fussy: a reader who has seen "
        "the word used loosely cannot tell which three figures really are approximate. "
        "Note that `ρ²` is a ratio of exact rationals even where `ρ` is not, which is "
        "why the reduction factor `1 − ρ²` needs no rounding and is the figure this "
        "course reports. What none of this can do is make a run into a proof: every "
        "answer here arrives with an error bar, and the model it came from is still only "
        "as true as what it left out."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
