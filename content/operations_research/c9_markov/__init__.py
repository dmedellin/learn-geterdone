"""Markov Chains, Decisions and Queues."""


from . import part_a, part_b


COURSE = {
    "slug": "markov-chains-decisions-and-queues",
    "title": "Markov Chains, Decisions and Queues",
    "level": "Advanced",
    "summary": (
        "A process that forgets everything but where it is, and the one equation that says "
        "where it settles: `&pi;P = &pi;`, solved as a linear system and never waited for. Classes "
        "and periods read off the arcs, absorption from a matrix inverse that is really a sum "
        "of powers, a decision attached to every state, and then queues &mdash; every one of "
        "them a single cut equation with different rates in it."
    ),
    "blurb": (
        "Everything on this course comes out of one matrix or one equation, and the point of it "
        "is a distinction that is easy to state and easy to lose: a steady state is the "
        "solution of a linear system, not the limit of anything. On one matrix here the system "
        "has exactly one answer and the powers never converge at all &mdash; they return to the "
        "identity every third step, for ever &mdash; so the two ideas can be seen coming apart "
        "rather than argued about. The second half turns the same machinery on queues. Cut the "
        "chain between two states, balance the crossings, and M/M/1, several servers, a finite "
        "waiting room and a customer who declines to join are four readings of one equation "
        "rather than four formulas; the closed forms are borrowed from the System Design path "
        "so that two Subjects cannot disagree about the same model. Every figure is an exact "
        "fraction except one, which is named."
    ),
    "key": [
        "P[i][j] = P(next is j | now at i)      every row a distribution, or it is not a chain",
        "recurrent ⟺ no arc leaves the class;  period = gcd of the cycle lengths",
        "πP = π  with  Σπ = 1     drop one dependent equation, solve exactly, iterate never",
        "the 3-cycle: π = (1/3, 1/3, 1/3) unique, P³ = P⁰, and no limit exists at all",
        "N = I + Q + Q² + ⋯ = (I − Q)⁻¹      t = N·1 steps,  B = N·R destinations",
        "v = r + γPᵈv       policy iteration stops by finiteness, not by a tolerance",
        "πₙλₙ = πₙ₊₁μₙ₊₁     one cut equation, and every queue here is a reading of it",
        "μₙ = min(n, s)μ is M/M/s;  λ(1 − π_K) is the rate Little's Law actually needs",
    ],
    "assumes_short": "Linear Programming Models through Dynamic Programming and Sequential Decisions; matrices, and discrete probability",
    "assumes_long": (
        "linear programming models, the simplex method, duality and sensitivity analysis, "
        "networks, integer programming, scheduling and dynamic programming and sequential "
        "decisions from this path: exact elimination over fractions is used as a tool "
        "throughout and is not re-derived, and the discounted value of a policy here is the "
        "backward recursion of Dynamic Programming and Sequential Decisions written as a linear "
        "system instead. From discrete mathematics, graphs and trees for reachability, "
        "connectivity and directed cycles, and Discrete Probability in full: conditional "
        "probability, random variables, expected value, linearity of expectation, variance, and "
        "the binomial and geometric distributions. From algebra, matrix products and inverse "
        "matrices, solving linear systems by elimination, infinite geometric series for the "
        "normalisation of an unbounded queue, and the number e, which is where the one rounded "
        "quantity on this course comes from"
    ),
    "outcomes_intro": (
        "By the end you can read a chain's structure off its arcs, solve for a steady state "
        "exactly and say what an iteration would and would not have given you, compute how long "
        "a chain runs and where it ends, choose an action in every state with a stopping "
        "argument rather than a tolerance, and build any queue on the course from one cut "
        "equation while naming what your model left out."
    ),
    "outcomes": [
        ("Write a chain down, and refuse one that is not a chain",
         "A transition matrix tested row by row with the failing row named, the support digraph "
         "drawn from the pattern of nonzero entries alone, a distribution pushed forward as a "
         "row vector, and `Pⁿ` computed exactly &mdash; with the width of its entries printed, "
         "because past a certain power a decimal has quietly stopped holding them."),
        ("Read structure off the arcs, not off the probabilities",
         "Communicating classes from reachability, recurrence from whether any arc leaves a "
         "class, and the period as a gcd obtained from a breadth-first levelling rather than "
         "from an enumeration of cycles &mdash; which together are the two hypotheses of the "
         "one result this path states without proving."),
        ("Solve πP = π, and say why that is not a limit",
         "The dependency of the n balance equations shown from the row sums, one equation "
         "dropped by name and `Σπ = 1` put in its place, exact Gauss-Jordan over the rationals, "
         "and the answer verified on the page by recomputing `πP` &mdash; beside a power "
         "iteration whose error is measured rather than assumed to shrink."),
        ("Compute how long a chain runs and where it stops",
         "The canonical blocks extracted from the matrix, `N = (I − Q)⁻¹` derived as the sum of "
         "the powers of `Q` with the partial sums shown climbing towards it, expected times as "
         "row sums and absorption probabilities as `N·R`, and a singular `I − Q` recognised as "
         "a second closed class rather than as a numerical failure."),
        ("Choose an action in every state, and know when to stop choosing",
         "A policy evaluated by solving `v = r + γPᵈv` exactly rather than iterating it, greedy "
         "improvement from that value, and termination argued from finiteness and monotonicity "
         "&mdash; with value iteration on the same problem shown approaching from below the "
         "number the solve already had."),
        ("Build any queue from one cut equation",
         "`πₙλₙ = πₙ₊₁μₙ₊₁` chained into a distribution and checked against the full balance "
         "system solved by elimination; M/M/1 with its truncation error printed, `min(n, s)μ` "
         "and Erlang C read off the same `π`, a bounded queue where `ρ ≥ 1` is permitted and "
         "`λ(1 − π_K)` is the divisor, and a balking chain no closed form covers."),
    ],
    "syllabus_intro": (
        "The object first &mdash; what a transition matrix is and what a power of one means "
        "&mdash; then the structure its arcs force, because the two hypotheses of the "
        "convergence result are needed before anything can be said about limits. Then the "
        "central claim, with the solve and the iteration on the same page and one matrix where "
        "they come apart completely. Absorption and the decision problem follow, both of them "
        "the same linear solve wearing different clothes. The queueing half then starts from "
        "one cut equation and never leaves it: four named models and one homemade one, each a "
        "different pair of rate lists handed to the same function, and the arrival process "
        "itself last, because it is the only place on the course where exactness stops."
    ),
    "how_to": [
        "Ask whether a question is about the arcs or about the numbers, and answer it with the "
        "right one. Classes, recurrence, irreducibility and the period depend only on which "
        "entries are nonzero; steady states, expected times and values depend on the "
        "magnitudes. Reasoning about a probability when the question was structural is how a "
        "reader decides that an arc of `1/1000` out of a class may as well not be there, and "
        "the stationary probability it forces to exactly zero says otherwise.",
        "Solve, then compare an iteration against the solve &mdash; never the other way round. "
        "Every iterative method on this course is present to be measured, and it can only be "
        "measured because the exact answer is sitting beside it. Reporting an iterate as the "
        "answer concedes precision for nothing where a limit exists, and on the three-cycle it "
        "reports a number for a limit that does not.",
        "Say which rate you divided by. `W = L/λ` is right only when nothing is lost and the "
        "arrival rate does not depend on the state, and the whole second half of this course is "
        "about chains where one or the other fails. The lab prints both divisions side by side "
        "on the bounded queue because the wrong one is the commonest error in the subject and "
        "it is always too small.",
        "Quote the truncation mass beside any figure from a finite chain that stands in for an "
        "unbounded one. It is `ρ^(N+1)`, it costs one power, and it is the difference between a "
        "figure you can defend and one you are hoping about: at four fifths loaded on forty "
        "states it is `0.000106` and the answer is good to three decimals, and at nineteen "
        "twentieths on sixty states it is `0.043766` and the mean is out by nearly three.",
    ],
    "not_covered": [
        "Continuous-time chains as a theory in their own right. The queueing half writes rates "
        "and balances flows, which is the continuous-time picture used as a tool; generator "
        "matrices, uniformisation and the exponential of a matrix are the machinery behind it "
        "and are not built here. Nothing on the course needs them, and the cut equation is "
        "derived from an argument about crossings rather than from a generator.",
        "Chains on infinitely many states, other than as a limit compared against. Every "
        "computation here is on a finite chain, and where the model is genuinely unbounded the "
        "page prints the mass the truncation discarded rather than waving at it. The closed "
        "forms for the unbounded queues are imported from the System Design path and named "
        "where they are used.",
        "Mixing times, coupling, and the rate at which `Pⁿ` approaches its limit. The "
        "convergence itself is stated and not proved here, and a quantitative version of it "
        "needs spectral gaps or a coupling argument. What is measured instead is the "
        "disagreement between an iteration and an exact answer at a given step count, which is "
        "a different and much more concrete thing.",
        "Hidden Markov models, parameter estimation, and anything that infers a chain from "
        "data. Every matrix on this course is given. Fitting one &mdash; maximum likelihood, "
        "the forward-backward recursion, the expectation-maximisation algorithm &mdash; is a "
        "statistics course, and the modelling hazard this path warns about would need restating "
        "for it rather than reusing.",
        "Queueing networks, priority disciplines and non-exponential service. Jackson networks, "
        "the M/G/1 queue and the Pollaczek-Khinchine formula all need machinery beyond a "
        "birth-death chain, and Kingman's variability approximation belongs to the System "
        "Design path, in &ldquo;Variability: the Kingman Approximation&rdquo;. What this course "
        "gives instead is one equation that survives every state-dependent rate, which is the "
        "direction the textbook formulas cannot go.",
        "<strong>The result this course cites and does not prove.</strong> The convergence of "
        "`Pⁿ` to the steady state on an irreducible aperiodic chain, which is one of the three "
        "the footer of this Subject names. Both of its hypotheses are computed here on whatever "
        "matrix a reader types, and its conclusion's `π` is obtained by solving a linear system "
        "rather than by taking the limit &mdash; so the unproved statement is never load-bearing "
        "for any figure on the course.",
    ],
    "footer_lead": (
        "Every transition probability, matrix power, steady-state probability, expected number "
        "of visits, absorption probability, policy value, queue-length distribution, blocking "
        "probability and binomial probability on this course is an exact fraction, and the "
        "arithmetic behind them is Gauss-Jordan elimination over the rationals rather than "
        "anything numerical. That matters more here than it looks: the central claim is an "
        "equality &mdash; `&pi;P` is <em>exactly</em> `&pi;`, and the cut equations give "
        "<em>exactly</em> the fractions the full balance system gives &mdash; and an equality "
        "between two decimals that look alike is evidence of nothing. It also keeps numbers a "
        "double cannot hold: `P&#8319;` on a five-state chain reaches fifteen-digit numerators "
        "by the twelfth power, and a truncated queue at ninety states has a `&pi;&#8320;` whose "
        "denominator runs to a hundred and nineteen digits. <strong>One quantity here is not "
        "rational and says so</strong>: `e^(&minus;&lambda;)` in the Poisson limit, computed by "
        "`expNegApprox` as the reciprocal of a positive-term series so that nothing cancels, "
        "printed beside the exact binomial with the difference between them given as a number. "
        "One result is stated and not proved, and says so: the convergence of `P&#8319;` to the "
        "steady state, whose two hypotheses this course computes and whose conclusion it "
        "obtains by solving instead. What none of this can do is decide whether the chain you "
        "wrote down is the process you meant."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
