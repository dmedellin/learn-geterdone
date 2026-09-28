"""Dynamic Programming and Sequential Decisions."""


from . import part_a, part_b


COURSE = {
    "slug": "dynamic-programming-and-sequential-decisions",
    "title": "Dynamic Programming and Sequential Decisions",
    "level": "Advanced",
    "summary": (
        "One recursion, filled from the last stage to the first, and nine problems that turn "
        "out to be it: a route, a split of indivisible units, an order schedule, a gamble "
        "repeated, a signal you could buy, an offer you could refuse, and a horizon with no "
        "last period. The method is short. What takes a course is the state &mdash; choose the "
        "wrong one and the recursion is still exact, still fast, and answering a different "
        "question &mdash; so every table here is filled twice, once backwards and once by "
        "enumerating the thing the recursion is a shortcut for."
    ),
    "blurb": (
        "Every method so far on this path has been a way of solving one big object. This course "
        "takes the opposite view: a decision made once is a decision made in a state, the state "
        "carries into the next decision, and the whole sequence collapses into a table you can "
        "fill in one pass from the end. The recursion is four lines and it is exact &mdash; "
        "these are not approximations and nothing here converges. But it is exact about the "
        "state you wrote down, and a state that leaves something out gives a table whose every "
        "entry is right and whose answer is wrong, with no symptom on the page. That is this "
        "path&rsquo;s hazard at its sharpest, so every lab here computes its answer a second "
        "time by enumerating every path, every split, every order pattern, every policy, every "
        "strategy and every accept-set, and shows the two numbers side by side. Two of the "
        "lessons exist because the second number disagrees with something a reader would "
        "otherwise have assumed."
    ),
    "key": [
        "f(v) = min over arcs out of v of",
        "   [ cost of the arc + f(where it leads) ]",
        "filled from the LAST stage back; a value",
        "is written once and never revised",
        "the state is whatever the future needs",
        "to know, and nothing else at all",
        "Vₜ(i) = max over a of",
        "   [ r(a,i) + Σⱼ P(a,i,j)·Vₜ₊₁(j) ],  V_T = 0",
        "F(t) = min over j ≤ t (one order interval)",
        "   [ F(j−1) + K + holding from j to t ]",
        "V(t) = E[ max(x, V(t−1)) ] − c",
        "   stop when the offer beats carrying on",
        "v = r + γPv is a LINEAR SYSTEM:",
        "(I − γP)v = r, solved, not approached",
    ],
    "assumes_short": "Linear Programming Models through Integer Programming; recursion, conditional probability and expectation",
    "assumes_long": (
        "this path as far as Integer Programming, and Networks: Flows, Paths and Assignments "
        "above all \u2014 a staged network is a network, the first thing this course solves is a "
        "shortest path, and branch and bound has already shown what a search over decisions "
        "looks like when no single programme will do. From discrete mathematics, Induction and "
        "Recursion, in particular recursive definitions, recurrence relations and strong "
        "induction, because the principle this whole course rests on is an induction over the "
        "stages; Discrete Probability through Bayes\u2019 Theorem, Expected Value and Linearity "
        "of Expectation, because from the midpoint of the course on, every value in the table is "
        "an expectation and one lesson turns a prior into a posterior; Combinatorics and "
        "Counting, for the enumerations each lab runs beside its recursion; and Algorithms and "
        "Complexity, whose Dynamic Programming and Greedy Algorithms lessons name from the "
        "outside what this course does from the inside. From algebra, systems of equations and "
        "row reduction, because the closing lesson solves for a value instead of iterating "
        "towards it"
    ),
    "outcomes_intro": (
        "By the end you can recognise a problem as sequential, choose a state and defend the "
        "choice, fill the table backwards, reconstruct the decisions the table implies, and say "
        "for each answer what would have to be true of the world for it to mean anything."
    ),
    "outcomes": [
        ("Fill a table from the end, and keep the ties",
         "A staged network solved backwards with every argmin carried rather than the first one "
         "found, the reconstructed routes priced again from the arcs, and the enumeration of "
         "every path printed beside the recursion &mdash; which is what turns &ldquo;the optimal "
         "policy is unique&rdquo; from an assumption into a false statement with a counterexample "
         "on the page."),
        ("Choose a state, and know when you have chosen wrongly",
         "A state as &ldquo;what is left&rdquo; rather than &ldquo;what has been done&rdquo;, a "
         "network built from a return table rather than given, and the arithmetic showing that a "
         "rule which looks only at the next unit gets `15` where the recursion gets `21` &mdash; "
         "not because it computed badly but because it is answering a smaller question."),
        ("Solve the lot-sizing problem exactly, and price a heuristic against it",
         "The `F(t)` table with its argmin in every row, the plan reconstructed and re-priced "
         "from the demand, all `2ᵀ⁻¹` order patterns enumerated as a check, and two textbook "
         "heuristics traced interval by interval with the averages they were watching &mdash; "
         "including the instance where both of them miss, by different amounts, in different "
         "directions."),
        ("Take an expectation inside a maximum",
         "The finite-horizon recursion on exact fractions, with every deterministic policy "
         "evaluated independently by pushing a distribution forward, and the measured fact that "
         "the best action in a state can depend on how many periods are left &mdash; which is why "
         "a policy in a finite horizon has a time index and a stationary one is a special case."),
        ("Put a price on information before buying it",
         "A payoff table and a prior folded back to a single number, the value of perfect "
         "information as an upper bound that no signal can exceed, and the value of one specific "
         "signal computed from the joint distribution &mdash; including a signal that looks "
         "informative, is not, and is worth exactly nothing."),
        ("Know when to stop, and prove the rule has the shape you assumed",
         "Sell-or-wait thresholds that fall as the deadline nears, the secretary rule as an exact "
         "harmonic sum rather than a limit, both checked by brute force &mdash; every accept-set "
         "in every period, every ordering of the candidates &mdash; and the infinite-horizon "
         "value found by row reduction while value iteration is still climbing towards it."),
    ],
    "syllabus_intro": (
        "The recursion first, on a network where the whole thing is visible at once, and then "
        "immediately the harder half: a problem with no network in it, where the state has to be "
        "invented before anything can be solved. Then lot sizing, twice &mdash; exactly, and then "
        "with the two rules of thumb that are used instead, measured against the exact answer on "
        "an instance where both of them lose. Then chance enters, first in the transition and "
        "then in what you are allowed to observe. The last three are about stopping: when to take "
        "an offer, when to stop looking at candidates, and what happens to the recursion when "
        "there is no last period to fill in from."
    ),
    "how_to": [
        "Write the state down as a sentence before you write any arithmetic. &ldquo;How many "
        "units are still unspent when this activity decides&rdquo; is a state; &ldquo;where I "
        "am&rdquo; is not, until you have said what &ldquo;where&rdquo; has to include. Every "
        "wrong answer on this course that survives every check comes from this step, and the "
        "check that catches it is not arithmetic &mdash; it is asking whether two situations the "
        "state calls identical really can be finished the same way.",
        "Fill the table from the end and never revise a value. If you find yourself wanting to go "
        "back and change `f` at a node you have already written, the ordering is wrong or the "
        "state is: the recursion works precisely because a value depends only on values already "
        "settled. The labs print the table in the order it was filled for that reason.",
        "Reconstruct the decisions and then price them independently. A value table is a claim "
        "about a number; the plan it describes is a different claim, and the second one is the "
        "one a reader can act on. Every lab here re-prices what its recursion returned, and two "
        "of them would have shipped a wrong plan beside a right number without it.",
        "Keep every tie. When two continuations are worth the same, a recursion that records the "
        "first one found still reports the right value and reports one of the right answers as "
        "though it were the only one. The lab of &ldquo;Filling the Table from the End&rdquo; "
        "carries all of them, and the example with three optimal routes is one arc cost away from "
        "the example with one.",
        "Before believing any optimum here, say what the model left out. The arithmetic on this "
        "course is exact and the enumerations are exhaustive, so nothing on the page will ever "
        "disagree with the answer. That is exactly why the modelling question has to be asked out "
        "loud: an exhaustive search over the wrong set of plans is a proof about the wrong "
        "problem.",
    ],
    "not_covered": [
        "Infinite-horizon policy iteration, and the average-reward criterion. Both need a Markov "
        "chain already defined &mdash; a transition matrix, a steady state, a class structure "
        "&mdash; and Markov Chains, Decisions and Queues builds all three. What this course does "
        "instead is the discounted fixed point on a chain small enough to solve by row reduction, "
        "which is as much of the infinite horizon as a course with no chains behind it can "
        "honestly claim.",
        "A continuous state, and the discretisation that would be needed to handle one. Every "
        "state here is one of a listed few and every quantity is rational. Dynamic programming "
        "over a continuous resource is a real subject whose interesting part is the "
        "discretisation error, and doing it badly in passing would be worse than naming it.",
        "The economic order quantity and continuous-review stock policies. The lot-sizing "
        "problem here has discrete periods, a known demand in each of them, and an exact answer "
        "by recursion; Inventory Models takes the other road, with a rate rather than a "
        "schedule, and finds `Q*` by a discriminant. The two answer different questions and the "
        "pair is worth meeting as a pair.",
        "Dynamic programming as an algorithmic technique &mdash; memoisation, tabulation, the "
        "distinction between top-down and bottom-up, and the complexity arguments around them. "
        "Algorithms and Complexity owns that framing and states it well. Here the recursion is a "
        "way of writing down what an optimal plan must satisfy, and the enumeration beside it is "
        "an oracle rather than a rival algorithm.",
        "Stochastic programming with recourse, and anything that puts a probability inside a "
        "linear programme. It is the natural meeting point of the first half of this path and "
        "this course, it is genuinely useful, and it needs both scenario trees and a decomposition "
        "method; naming it is as far as this course goes.",
        "<strong>The one limit this course prints and does not prove.</strong> The secretary "
        "problem&rsquo;s `n/e` is where the optimal `r` sits in the limit, and the page holds it "
        "against the number you reject, which is `r − 1` &mdash; at a hundred candidates, 36.7879 "
        "against 37. The argument that it is the limit is an asymptotic one this path has not "
        "built. It appears on the page labelled as rounded, beside an exact table of fractions "
        "that never needs it, and how many to reject is read off that table rather than off the "
        "limit.",
    ],
    "footer_lead": (
        "Every value, cost, expectation, threshold, posterior and fixed point on this course is "
        "an exact fraction. A three-period expectation prints as `53/8`, a search is worth "
        "`71/3`, a discounted value is `22/7`, and the secretary table at four candidates is "
        "`1/4`, `11/24`, `5/12`, `1/4` rather than four decimals. That is doing real work here "
        "rather than decorating: the closing lesson&rsquo;s whole argument is that value "
        "iteration never reaches the fixed point, and the evidence is the denominator growing "
        "from one digit to ten in twelve steps while the exact answer was available at step zero "
        "&mdash; a float would have hidden both the exactness and the cost behind the same "
        "fifteen digits. Two numbers on the course are genuinely irrational and both are labelled "
        "where they appear: `1/e`, and the `n/e` built from it. Every other decimal here says "
        "&ldquo;exact, shown to so many places&rdquo;. What none of this can check is the state: "
        "a recursion is exact about the problem you described to it, and each lesson ends by "
        "naming what its description left out."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
