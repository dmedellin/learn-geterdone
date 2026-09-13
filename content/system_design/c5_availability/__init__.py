"""Availability and Failure."""


from . import part_a, part_b


COURSE = {
    "slug": "availability-and-failure",
    "title": "Availability and Failure",
    "level": "Intermediate",
    "summary": (
        "Availability as a fraction and what composition does to it: chains multiply it down, redundancy multiplies it up under independence, retries multiply load at the worst moment, and durability is a race between failures and repair."
    ),
    "blurb": (
        "Nines are a fraction, and everything else in this course is what happens to that fraction under composition: chains multiply it down, redundancy multiplies it up but only if the failures are independent, retries multiply load exactly when the system can least afford it, and three copies of a file are safe in proportion to how fast a lost copy is replaced. Every claim is a probability you compute."
    ),
    "key": [
        "downtime = (1 − A) × period          99.9% = 43.8 min/month",
        "A = MTBF/(MTBF + MTTR)               halving MTTR = doubling MTBF",
        "A = ∏Aᵢ     series          A = 1 − ∏(1 − Aᵢ)     parallel",
        "P(both down) = c + (1 − c)p²         a 0.1% common cause swamps a 10⁻⁴ pair",
        "attempts = (1 − pʳ⁺¹)/(1 − p)        amplification, worst when p is worst",
    ],
    "assumes_short": "Courses 1 and 3; independence, binomials, combinations",
    "assumes_long": (
        "C1, C3. Discrete Mathematics independence, binomial-distribution, "
        "combinations, conditional-probability, expected-value. Algebra "
        "geometric-sequences-and-series"
    ),
    "outcomes_intro": (
        "By the end you can convert nines into minutes, compose availability in series "
        "and in parallel while naming the assumption that lets you, compute what a retry "
        "policy does to load, and put a number on both durability and blast radius."
    ),
    "outcomes": [
        ("Convert between nines, minutes and repair time",
         "Downtime per month and per year from an availability, the availability from "
         "MTBF and MTTR, and the MTTR a target requires &mdash; which is usually the "
         "cheaper lever."),
        ("Compose availability and say what you assumed",
         "The product for a chain, `1 − ∏(1 − Aᵢ)` for redundant paths, the binomial "
         "tail for `k`-of-`n`, and the common-cause term that makes all three optimistic "
         "when it is not zero."),
        ("Compute what retries do to load",
         "Expected attempts and success for a policy, the fixed point of a retry loop "
         "that can sit above `ρ = 1` when the un-retried load was fine, and the "
         "synchronised waves that backoff without jitter produces."),
        ("Put a number on durability and blast radius",
         "The annual probability of losing every copy of a replicated item and what "
         "halving the repair window does to it; and the probability two tenants share "
         "every node under shuffle sharding."),
    ],
    "syllabus_intro": (
        "The fraction first, then composition in three shapes, then the two ways a system makes its own load worse, and last the two questions that are about sets of machines rather than one: durability and blast radius."
    ),
    "how_to": [
        "Say the independence assumption out loud every time you multiply. Four of this "
        "course&rsquo;s formulas are exactly right under independence and badly wrong "
        "without it, and &ldquo;Correlated Failure&rdquo; is the lesson that measures how "
        "wrong.",
        "Do the retry-storm iteration by hand for three steps. A fixed point is easier to "
        "believe when you have watched the first three iterates move away from where you "
        "expected.",
        "Keep availability as a fraction, not a percentage, inside any calculation. The "
        "interesting differences on this course are in the fourth decimal place and "
        "percentages hide them.",
    ],
    "not_covered": [
        "Incident process, on-call practice and chaos engineering as a discipline.",
        "Consensus availability, which needs the quorum arithmetic of course 6.",
        "Failure-rate models over time. Every failure here has a constant rate; bathtub "
        "curves and wear-out are out of scope.",
    ],
    "footer_lead": (
        "Availabilities, binomial tails, retry amplifications and shuffle-sharding overlaps on this course are exact fractions, which is what lets a page show that four nines and three nines differ by a factor of ten rather than by a rounding. The one figure computed in floating point is the durability estimate of &ldquo;Replica Loss and Durability&rdquo;, which is a first-order rare-event approximation and says so."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
