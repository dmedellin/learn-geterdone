"""Scheduling."""


from . import part_a, part_b


COURSE = {
    "slug": "scheduling",
    "title": "Scheduling",
    "level": "Advanced",
    "summary": (
        "What order to do the work in, when the only thing being spent is time: six "
        "objectives on one machine and the one of them no order can move, three rules "
        "proved by swapping two neighbouring jobs, an algorithm for the jobs that will "
        "be late anyway, two machines in series and `m` in parallel where a rule "
        "arrives with a guarantee instead of a proof &mdash; and last, a deadline with "
        "a price per day attached."
    ),
    "blurb": (
        "This is the course on this path with no matrix in it. Five jobs on one machine "
        "have `120` orders and six reasonable objectives, and the order that wins on one "
        "of them is beaten on the others by a different order each time &mdash; so the "
        "first thing here is that a schedule is not good, it is good at something. The "
        "rules that follow are all proved the same way and none of them needs calculus: "
        "take two jobs standing next to each other, swap them, and compute the exact "
        "quantity the swap moved. That one subtraction gives shortest-processing-time, "
        "Smith&rsquo;s ratio and earliest-due-date, and it is honest about the two places "
        "it does not reach. Then the machine count goes up: two in series still has an "
        "exact rule, `m` in parallel has a heuristic with a bound proved from two lower "
        "bounds, and a shop where each job has its own route has neither &mdash; one "
        "binary choice per shared machine, and some combinations of those choices "
        "describe no schedule at all."
    ),
    "key": [
        "one machine, all ready at 0, no idle: makespan = sum p, the SAME in every order",
        "swap adjacent a then b:  sum C moves by p_b − p_a,  sum wC by w_a p_b − w_b p_a",
        "SPT minimises sum C     WSPT (p/w ascending) minimises sum wC",
        "EDD minimises L max and T max, and does NOT minimise sum T or the late count",
        "Moore–Hodgson: offer in due-date order, discard the LONGEST accepted job",
        "Johnson: p1 < p2 to the front by p1 up, the rest to the back by p2 down",
        "m machines: makespan ≥ sum p / m  and  ≥ max p;  LPT within 4/3 − 1/(3m)",
        "crashing: min sum rate·y with the deadline as ONE right-hand side; the curve is convex",
    ],
    "assumes_short": "Linear Programming Models through Integer Programming; sorting, greedy exchange arguments, and the vocabulary of hardness",
    "assumes_long": (
        "linear programming models and duality and sensitivity analysis from this path "
        "— right-hand-side ranging in particular, because the exact time-cost curve is "
        "that machinery applied to a deadline row and not a second implementation of "
        "anything; networks: flows, paths and assignments, for the project network and "
        "the critical path, which the last two lessons use as a tool rather than "
        "rebuild; and integer programming, for the either-or constraint, which is "
        "exactly what a pair of operations sharing a machine is; from discrete "
        "mathematics, searching and sorting, greedy algorithms and the exchange "
        "arguments behind them, paths and connectivity for the cycle that is a "
        "deadlock, and P, NP and NP-completeness, because three of the models here are "
        "hard and the course says so rather than offering a rule; and from algebra, "
        "inequalities and the arithmetic of ratios"
    ),
    "outcomes_intro": (
        "By the end you can say which of six objectives a schedule is being judged on "
        "and which one it cannot affect, <em>prove</em> a sequencing rule by swapping "
        "two neighbours rather than quoting it, run an algorithm whose discard is not "
        "the job that went wrong, bound a parallel-machine schedule from below before "
        "building one, and price a deadline exactly and then check the plan with a "
        "method that is not the programme that produced it."
    ),
    "outcomes": [
        ("Score one order against every objective at once",
         "Completion times, weighted completion times, lateness, tardiness and the late "
         "count off a single clock; the makespan shown to be `sum p` in every order; and "
         "each figure compared with the best of all `n!` orders rather than asserted."),
        ("Prove a sequencing rule by adjacent exchange",
         "The swap identity `p_b − p_a` for total completion time and `w_a p_b − w_b p_a` "
         "for the weighted version, derived with a symbolic start time that cancels, the "
         "improvement condition read off the sign, and the rule obtained as the orders "
         "no swap improves."),
        ("Beat the rules that use one number",
         "Heaviest-weight-first and shortest-first measured against Smith's ratio on the "
         "same data, with the size of the gap accounted for by named adjacent swaps "
         "rather than asserted as a general property."),
        ("Meet due dates, and name the question you answered",
         "Earliest-due-date proved optimal for maximum lateness by an exchange over a "
         "maximum, then measured on total tardiness and on the late count, where it is "
         "beaten; Moore&ndash;Hodgson run step by step for the count; and `1 || sum T` "
         "named as the boundary the technique does not reach."),
        ("Schedule more than one machine, with a bound",
         "Johnson's rule for two machines in series, with the makespan accounted for as "
         "second-machine work plus second-machine idle; longest-first on `m` identical "
         "machines against both lower bounds and against the best assignment there is; "
         "and a job shop as one binary choice per shared pair, with the deadlocked "
         "combinations counted as answers."),
        ("Price a deadline and verify the plan",
         "The crashing programme with the deadline as a single right-hand side, the "
         "exact convex time-cost curve from ranging that row, and the durations it buys "
         "put back through a forward and a backward pass that share no arithmetic with "
         "the simplex."),
    ],
    "syllabus_intro": (
        "The objectives first, because a reader who has not watched one order win once "
        "and lose five times will keep asking whether a schedule is good; then the "
        "adjacent exchange twice, unweighted and weighted, because it is the whole "
        "proof technique and the second use of it is the first with one multiplication "
        "added; then the two due-date questions, which sound like one question and have "
        "different answers, with the one that has no rule named rather than "
        "approximated. After that the machine count rises, and each rise costs "
        "something: two machines in series keeps an exact rule, `m` in parallel keeps a "
        "guarantee, a job shop keeps neither. The last lesson changes what is being "
        "spent."
    ),
    "how_to": [
        "Write the objective at the top of the page before choosing a rule. Every "
        "theorem on this course names one objective and is silent about the other five, "
        "and the rules disagree: shortest-first is optimal for total completion time and "
        "costs `114` on the weighted version where `108` is available from a rule that "
        "is no harder to run.",
        "Prove a rule by swapping two neighbours and writing one subtraction. Give the "
        "pair a symbolic start time, write both schedules' completion times, subtract, "
        'and check that the start time cancelled. If the difference still mentions '
        "another job or the clock, the objective has no exchange rule and the right move "
        "is to say so.",
        "Whenever a rule wins, measure what it cost elsewhere. Earliest-due-date attains "
        "the best maximum lateness on the lab's five jobs and leaves four jobs late where "
        "two is possible. Both sentences are true, both are about due dates, and a report "
        "that states only the first is misleading without containing a falsehood.",
        "On more than one machine, compute a lower bound before building a schedule. "
        "Total work over the machine count and the longest single job are both free, and "
        "a schedule that attains the larger of them is proved optimal with no search at "
        "all &mdash; while a schedule that does not tells you how much of the remaining "
        "gap you have actually bounded.",
    ],
    "not_covered": [
        "Release dates and preemption. Every job here is available at time zero and runs "
        "to completion, and that is not a simplification of the proofs &mdash; it is a "
        "condition on them. Release dates change which exchanges are legal and interrupts "
        "change what a schedule is, and nothing proved on this course survives either.",
        "An algorithm for total tardiness. `1 || sum T` has no adjacent-exchange rule, "
        "the labs exhibit its optimum by enumeration on small instances, and the course "
        "names it as the boundary of the technique. Offering a plausible heuristic here "
        "would teach the opposite of everything before it.",
        "Anything random, and anything arriving over time. Durations are known numbers, "
        "the work is all present at the start, and no machine breaks down. Queues with "
        "arrivals and service times as distributions are &ldquo;Markov Chains, Decisions "
        "and Queues&rdquo;, and a schedule evaluated under uncertainty is "
        "&ldquo;Simulation and Variance Reduction&rdquo;.",
        "Resource-constrained project scheduling. The crashing programme assumes the "
        "activities are independent, so two of them can be shortened at once without "
        "competing for the same people. Adding a resource pool turns the timing rows "
        "into disjunctions and makes the project network an integer programme, which is "
        "a real subject and not a variant of this one.",
        "The job shop at any interesting scale. Enumerating `2^k` orientations is exact "
        "and is a teaching device; what survives is branch and bound on the same binary "
        "choices, which is &ldquo;Integer Programming&rdquo;, plus the shifting-bottleneck "
        "and local-search methods built on top of it, which are named here and nowhere "
        "developed.",
        "<strong>The results this course cites and does not prove.</strong> The "
        "`4/3 − 1/(3m)` guarantee for longest-first on identical machines is stated and "
        "measured against, never derived; the NP-hardness of `1 || sum T`, of makespan "
        "on identical machines and of the three-machine flow shop and the job shop are "
        "taken from &ldquo;Algorithms and Complexity&rdquo;; and the special case in "
        "which a three-machine flow shop reduces to two is named without its condition "
        "being worked. Each is stated where it is needed, with its owner named.",
    ],
    "footer_lead": (
        "Every processing time, completion time, lateness, load, makespan, crash rate "
        "and curve breakpoint on this course is exact, and the ratios are fractions "
        "rather than decimals for a reason that shows up immediately: Smith's rule "
        "sorts on `p/w`, two jobs on the opening instance tie at `3`, and a rounded "
        "ratio invents an ordering between them where the exchange identity says the "
        "difference is exactly zero. The enumerated optima are enumerations &mdash; "
        "every one of the `n!` orders, every one of the `m^n` assignments, every one of "
        "the `2^k` orientations &mdash; and where an instance is too large for that, the "
        "labs say the claim is unchecked rather than printing it. Two figures on the "
        "course are not exact answers to the question asked and say so: the "
        "longest-first makespan, which is a heuristic measured against a guarantee, and "
        "the lower bounds on a parallel machine, which are proofs that nothing does "
        "better rather than promises that anything does that well."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
