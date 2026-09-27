"""Markov Chains, Decisions and Queues -- the queues half.

One cut equation, and four readings of it: constant rates, s servers, a chain
with a wall, and the arrival process underneath all of them.

Every figure below is read off the kit -- scripts/mathpath/labs/birthdeath.py --
by executing its shipped JavaScript under node, rather than asserted here, and
scripts/mathcheck.js executes that same block. The closed forms this course
compares against are IMPORTED from sysdesign_core rather than re-derived, so
nothing here may contradict the System Design pages built on them. Where a
design note and the kit disagreed, the kit won.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-cut-equation-and-every-queue-from-it",
        "title": "The Cut Equation, and Every Queue From It",
        "module": "One cut equation",
        "one_line": "Cut the chain between n and n+1: what crosses upward must cross back down, and chaining those ratios gives the whole distribution.",
        "summary": (
            "A queue is a chain on `0, 1, 2, …` whose only moves are up one and down one. Draw a "
            "line between n and n+1 and the chain crosses it upward exactly as often as it "
            "crosses back down in the long run &mdash; it cannot do otherwise, because to cross "
            "up twice running it would have to be on both sides at once. That single equation "
            "`πₙλₙ = πₙ₊₁μₙ₊₁` gives every ratio, and chaining them from state 0 and dividing by "
            "the total gives `π` with no matrix anywhere in it. Because cutting is the step you "
            "are being asked to believe, the page also builds the full balance system and solves "
            "it by elimination, and compares the two as fractions rather than to a tolerance."
        ),
        "key": [
            "πₙλₙ = πₙ₊₁μₙ₊₁       one equation per cut, and nothing is assumed about the rates",
            "πₙ = π₀ · (λ₀λ₁⋯λₙ₋₁)/(μ₁μ₂⋯μₙ),   then divide by the total to normalise",
            "the full balance system:  πₙ(λₙ + μₙ) = πₙ₋₁λₙ₋₁ + πₙ₊₁μₙ₊₁, with Σπ = 1 for one row",
            "three machines, one repairer:  λ = 3, 2, 1 and μ = 2, 2, 2",
            "π = (4/19, 6/19, 6/19, 3/19) from the cuts, and identically from the system",
            "L = 27/19, admitted rate 30/19, W = L/λ_eff = 9/10",
        ],
        "key_label": "One equation per cut, and a second route that shares no arithmetic with it",
        "concepts_intro": (
            "Three ideas. The first is the equation, the second is why it is legitimate, and the "
            "third is why this course meets it before any named queue."
        ),
        "concepts": [
            ("A cut balances because crossings alternate",
             "Between two consecutive upward crossings of the line between n and n+1 there must "
             "be a downward crossing, since the chain moves one state at a time and cannot be on "
             "both sides at once. So in the long run the two rates are equal: the rate up is "
             "`πₙλₙ` and the rate down is `πₙ₊₁μₙ₊₁`, and those are the same number. Nothing "
             "about the sizes of the rates entered that argument."),
            ("The cut answer is checkable against a system that knows nothing about cuts",
             "The full balance equations &mdash; flow into each state equals flow out, with one "
             "dependent row replaced by `Σπ = 1` &mdash; are built and solved by exact "
             "Gauss-Jordan on the same page. The comparison is `Requ` on fractions, not a "
             "tolerance, so a cut argument that were merely a convenient shortcut would show up "
             "as a disagreement rather than as two decimals that look alike."),
            ("Nothing here assumes the rates are constant",
             "That is the reason to meet the cut before any named model. M/M/1 is the case where "
             "every `λₙ` is the same number; s servers is `μₙ = min(n, s)μ`; a finite room is the "
             "same chain stopped; a customer who balks is `λₙ` falling with n. The moment a rate "
             "depends on the state, the closed forms stop applying and this equation does not."),
        ],
        "read_title": "One equation, and four models that are readings of it",
        "read_intro": "The chain, the crossing argument, the product that comes out of it, the independent check, and Little's Law on the rate that actually gets in.",
        "body": [
            ("def", ("A birth-death chain",
                     "States `0, 1, 2, …, N`. From state `n` the chain moves to `n + 1` at rate "
                     "`λₙ` (an <strong>arrival</strong>) and to `n − 1` at rate `μₙ` (a "
                     "<strong>service completion</strong>), and nowhere else. There is no "
                     "arrival out of the top state and no service out of state 0.",
                     "The lab takes two lists: one arrival rate per state starting at 0, and one "
                     "service rate per state starting at 1. A chain with N arrival rates has "
                     "states `0` to `N`.")),
            ("thm", ("The cut equation",
                     "In the long run, for every `n`, `πₙ λₙ = πₙ₊₁ μₙ₊₁`. Hence "
                     "`πₙ₊₁ = πₙ · λₙ/μₙ₊₁`, and chaining from `π₀` gives `πₙ` as a product of "
                     "ratios, fixed by `Σπ = 1`.")),
            ("proof", ["Draw the line between `n` and `n + 1`. The chain moves one state at a "
                       "time, so every upward crossing of that line is followed by a downward "
                       "crossing before the next upward one: it cannot cross up twice in a row "
                       "without being on both sides at once.",
                       "So over a long run the numbers of crossings in the two directions differ "
                       "by at most one, and the long-run rates are equal. The rate of upward "
                       "crossings is the long-run fraction of time at `n` times the arrival rate "
                       "there, which is `πₙλₙ`; the rate downward is `πₙ₊₁μₙ₊₁`. Setting them "
                       "equal and solving for `πₙ₊₁` gives the ratio."]),
            ("p", "The argument used the one-step-at-a-time structure and nothing else. It did "
                  "not assume the rates were constant, that the chain was infinite, that "
                  "arrivals were Poisson, or that anything was stable. That is why one function "
                  "serves every model on this material: there is one chain and several readings "
                  "of it rather than several models."),
            ("h3", "Three machines and one repairer"),
            ("math", [
                "λ = 3, 2, 1      three machines, each failing at rate 1; fewer left to fail",
                "μ = 2, 2, 2      one repairer, working at rate 2 whatever the backlog",
                "",
                "  cut 0 | 1     π₁ = π₀ · 3/2            ratio 3/2",
                "  cut 1 | 2     π₂ = π₁ · 2/2            ratio 1",
                "  cut 2 | 3     π₃ = π₂ · 1/2            ratio 1/2",
                "",
                "  running product from π₀:   1,  3/2,  3/2,  3/4",
                "  total                      1 + 3/2 + 3/2 + 3/4  =  19/4",
                "",
                "  π = (4/19, 6/19, 6/19, 3/19)",
                "",
                "  from the FULL balance system, 4 equations, equation 4 dropped,",
                "  Σπ = 1 in its place, 15 elimination operations over the rationals:",
                "",
                "  π = (4/19, 6/19, 6/19, 3/19)          identical, fraction by fraction",
            ]),
            ("p", "The two routes share no arithmetic. The left-hand one multiplies ratios and "
                  "divides by a total; the right-hand one builds the equation "
                  "`πₙ(λₙ + μₙ) = πₙ₋₁λₙ₋₁ + πₙ₊₁μₙ₊₁` for every state, drops one by name because "
                  "the equations are dependent for exactly the reason they were dependent on a "
                  "general chain, puts the normalisation in its place, and eliminates. They agree "
                  "entry for entry, and the page says so with an exact equality rather than a "
                  "comparison of decimals."),
            ("p", "Dropping a different equation changes nothing, as it did not on a general "
                  "chain: all four choices give `(4/19, 6/19, 6/19, 3/19)`. The dependency is the "
                  "same one &mdash; sum the balance equations and every term cancels &mdash; and "
                  "so is the repair."),
            ("h3", "Little's Law, on the rate that actually gets in"),
            ("p", "`L = Σ n πₙ` is the mean number in the system, and it comes straight out of "
                  "`π`. `W` is `L` divided by a rate, and the rate is not always `λ`: on a chain "
                  "whose arrival rate depends on the state, the long-run rate of admissions is "
                  "`λ_eff = Σ πₙ λₙ`. On the repairer example that is "
                  "`(4/19)(3) + (6/19)(2) + (6/19)(1) = 30/19`, so `W = (27/19)/(30/19) = 9/10`. "
                  "The identity is the one &ldquo;Little's Law from a Trace&rdquo; proves by "
                  "counting; what this page contributes is the right rate to divide by."),
            ("example", ("Two servers, from one change to one list",
                         "Set `λ = 4, 4, 4, 4, 4` and `μ = 3, 6, 6, 6, 6`. The service rate out "
                         "of state 1 is 3 and out of every higher state is 6: a second server "
                         "that comes into use once there are two customers and then has nobody "
                         "else to add.",
                         "The ratios are `4/3` for the first cut and `2/3` thereafter, giving "
                         "`π = (243, 324, 216, 144, 96, 64)/1087`. The mode is state 1 rather "
                         "than state 0, which is what the single early ratio above 1 does, and "
                         "no formula was needed to see it.")),
            ("example", ("Arrivals faster than service, on a chain that stops anyway",
                         "Set `λ = 5, 5, 5, 5` and `μ = 3, 3, 3, 3`. Every ratio is `5/3`, so "
                         "`π` rises geometrically to `π = (81, 135, 225, 375, 625)/1441` with "
                         "its mass at the top.",
                         "The page flags that at the top of the chain arrivals are at least as "
                         "fast as service, so the untruncated chain would have no distribution "
                         "at all. What you are looking at is a finite chain and its answers are "
                         "answers about that chain, not about an unbounded queue. Which model "
                         "you meant is a modelling question and the page will not decide it for "
                         "you.")),
            ("p", "One restriction: every service rate has to be strictly positive. A zero `μ` "
                  "closes the chain off &mdash; nothing can come back down from that state "
                  "&mdash; so the cut above it has no solution with probability on both sides, "
                  "and the lab refuses rather than dividing by zero. This mode also stops at "
                  "eight cuts, because it prints every cut equation and the whole balance "
                  "system; the constant-rate readings take chains as long as you like."),
        ],
        "lab": ("birthdeath", {
            "mode": "cut",
            "preset": "machines",
            "panel_title": "Type any rates you like — they do not have to be constant",
            "panel_intro": "The cut equations build π as a product of ratios. Beside them the "
                           "full balance system is solved by exact elimination with one "
                           "dependent equation dropped by name, and the page compares the two "
                           "distributions fraction by fraction rather than to a tolerance. Move "
                           "the cut slider to see one equation at a time.",
        }),
        "steps_title": "Getting π out of a birth-death chain",
        "steps_intro": "Four steps and no matrix. The last one is the one that decides whether your W means anything.",
        "steps": [
            ("Write the two rate lists and check they line up",
             "One arrival rate out of each state from 0 upward, one service rate out of each "
             "state from 1 upward, the same count in each. Getting the offset wrong by one is "
             "the standard error here and it produces a plausible distribution for a different "
             "chain."),
            ("Take the ratio at each cut and chain them",
             "`πₙ₊₁/πₙ = λₙ/μₙ₊₁`. Multiply them up from `π₀ = 1` to get the unnormalised "
             "weights. Keep them as fractions: the product of ratios is where a decimal starts "
             "losing digits, and the whole point of the second route is a comparison that has "
             "to be exact."),
            ("Divide by the total",
             "Add the weights and divide. This is the only place normalisation enters, and it is "
             "the same replacement for the same dependency that a general chain needed: the "
             "balance equations fix `π` up to a scale and nothing more."),
            ("Compute L from π, then divide by the rate that actually gets in",
             "`L = Σ n πₙ`. For `W`, divide by `λ_eff = Σ πₙ λₙ`, not by `λ`. On a chain with "
             "constant rates and no losses those coincide; on every other chain on this material "
             "they do not, and the difference is not small."),
        ],
        "worked": {
            "title": "Three machines and one repairer, by cuts and then by elimination",
            "intro": [
                "Three machines, each failing at rate 1, and one repairer working at rate 2. "
                "With `n` already broken there are `3 − n` left to fail, so the arrival rate "
                "falls: `λ = 3, 2, 1`. The repairer does not speed up: `μ = 2, 2, 2`.",
            ],
            "lines": [
                "cuts",
                "   0 | 1     π₀ · 3  =  π₁ · 2       π₁ = (3/2) π₀",
                "   1 | 2     π₁ · 2  =  π₂ · 2       π₂ = (1)   π₁  = (3/2) π₀",
                "   2 | 3     π₂ · 1  =  π₃ · 2       π₃ = (1/2) π₂  = (3/4) π₀",
                "",
                "   weights   1,  3/2,  3/2,  3/4        total  19/4",
                "   π         4/19, 6/19, 6/19, 3/19",
                "",
                "the full balance system, which knows nothing about cuts",
                "   state 0        −3 π₀ + 2 π₁                          = 0",
                "   state 1     3 π₀ − 4 π₁ + 2 π₂                       = 0",
                "   state 2            2 π₁ − 3 π₂ + 2 π₃                = 0",
                "   state 3                                              dropped",
                "   in its place   π₀ + π₁ + π₂ + π₃ = 1",
                "",
                "   Gauss-Jordan over the rationals, 15 operations, rank 4 of 4",
                "   π = (4/19, 6/19, 6/19, 3/19)            identical",
                "",
                "   dropping equation 1, 2 or 3 instead gives the same four fractions",
                "",
                "the readings",
                "   L      = 0(4/19) + 1(6/19) + 2(6/19) + 3(3/19)  =  27/19  =  1.421053",
                "   Lq     = 1(6/19) + 2(3/19)                      =  12/19",
                "   λ_eff  = 3(4/19) + 2(6/19) + 1(6/19)            =  30/19",
                "   W      = L / λ_eff = (27/19)/(30/19)            =  9/10   =  0.900000",
                "   Wq     = Lq / λ_eff                             =  2/5",
            ],
            "after": [
                "Two things are being claimed at once here and it is worth separating them. The "
                "first is that the cut equations are <em>correct</em>, and the check for that is "
                "the balance system: two routes, no shared arithmetic, the same four fractions. "
                "The second is that they are <em>easy</em>, and the check for that is the line "
                "count: three multiplications and one division against a four-by-five "
                "elimination.",
                "The `λ_eff` line is the one that generalises. It is `30/19 ≈ 1.579`, not 3, "
                "because the arrival rate is 3 only while nothing is broken. Dividing `L` by 3 "
                "would give `0.474` and would be a statement about a queue in which all three "
                "machines can fail while three are already broken.",
                "For a rehearsal, change the repairer's rate from 2 to 3 and predict the "
                "direction of every figure before recomputing. The supplied first move is that "
                "each ratio is multiplied by `2/3`, so all the weight shifts towards state 0. "
                "Say what that does to `L`, to `λ_eff` and to `W` &mdash; and note that two of "
                "those move in opposite directions, which is why `W` is worth computing rather "
                "than guessing.",
            ],
        },
        "quiz_title": "Cuts, products and the right rate",
        "quiz": [
            {"q": "What does the cut argument assume about the arrival and service rates?",
             "a": ["That they are constant", "That arrivals are Poisson",
                   "Nothing: it uses only that the chain moves one state at a time",
                   "That the chain is infinite"],
             "c": 2,
             "why": "Crossings of a line between neighbouring states must alternate because the "
                    "chain cannot be on both sides at once, and that is the whole argument. "
                    "State-dependent rates, finite chains and unstable chains are all covered, "
                    "which is why one function serves every model here."},
            {"q": "Why does the page solve the full balance system as well as chaining the cuts?",
             "a": ["Because the cut equations only give ratios and cannot be normalised",
                   "Because the balance system is faster",
                   "Because cutting the chain is the step the reader is being asked to believe, and an independent exact route either confirms it or disagrees",
                   "Because the two apply to different models"],
             "c": 2,
             "why": "Both are exact, so `Requ` decides the comparison and there is no tolerance "
                    "to hide behind. The balance system is built from inflow-equals-outflow at "
                    "each state and has no notion of a cut in it, so agreement is evidence "
                    "rather than restatement."},
            {"q": "On the repairer chain, `L = 27/19` and `λ = 3` out of state 0. What is `W`?",
             "a": ["`L/3 = 9/19`", "`L/λ_eff` where `λ_eff = 30/19`, giving `9/10`",
                   "`L × 3 = 81/19`", "Undefined, because the arrival rate is not constant"],
             "c": 1,
             "why": "Little's Law needs the rate that actually enters the system in the long "
                    "run, which is `Σ πₙ λₙ = 30/19` here. Dividing by 3 would price the queue "
                    "as though all three machines could fail while three were already broken."},
            {"q": "A service rate of 0 is typed for one of the states. Why does the lab refuse?",
             "a": ["Because zero is not a fraction",
                   "Because nothing can come back down from the state above it, so the cut there has no solution with probability on both sides",
                   "Because Little's Law needs a positive rate",
                   "Because the balance system would then be rank deficient by two"],
             "c": 1,
             "why": "The cut equation `πₙλₙ = πₙ₊₁μₙ₊₁` with `μₙ₊₁ = 0` forces `πₙλₙ = 0`, which "
                    "closes the chain off above that point rather than describing a queue. The "
                    "page names the condition instead of dividing by zero."},
        ],
        "mistakes": [
            ("Lining the two rate lists up wrong",
             "`λₙ` is the rate OUT OF state `n`, indexed from 0; `μₙ` in the lab's second box is "
             "the rate out of state `n + 1`, indexed from 1. An off-by-one here produces a "
             "perfectly normalised distribution for a chain you did not mean, and nothing "
             "downstream will look wrong."),
            ("Dividing L by λ when the arrival rate depends on the state",
             "`W = L/λ_eff`, and `λ_eff = Σ πₙ λₙ`. The two agree only when every `λₙ` is the "
             "same and nothing is lost. Everywhere else the naive division is too small, because "
             "it credits the system with customers it never took in."),
            ("Treating the cut equation as a special trick for M/M/1",
             "It is the general statement and M/M/1 is its constant-rate case. A reader who "
             "learns the geometric distribution first and the cut second will reach for a closed "
             "form the moment a rate varies, and there is none for a balking queue or a repair "
             "shop with a finite population."),
        ],
        "standard": ("Finish when a queue whose rates vary with the state is no harder for you than one whose rates do not.",
                     "You should be able to state the crossing argument, write one cut equation "
                     "per boundary and chain them into an unnormalised product, normalise, build "
                     "the full balance system and recognise its dependency as the same one a "
                     "general chain has, compute `L` and `λ_eff` from `π`, and divide by the "
                     "right one of them."),
        "note": 'Hold every rate still and the product of ratios becomes a product of one number with itself: a geometric distribution, derived rather than quoted. That is also where the awkward fact arrives, since a real M/M/1 queue has infinitely many states and this kit has finitely many. &ldquo;The M/M/1 Chain and the Cost of Truncation&rdquo; prints the mass the truncation threw away instead of choosing a number of states at which to stop mentioning it.',
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "the-mm1-chain-and-the-cost-of-truncation",
        "title": "The M/M/1 Chain and the Cost of Truncation",
        "module": "The named queues",
        "one_line": "Constant rates make every cut ratio ρ, so π is geometric — and a finite chain is an approximation whose error is printed rather than assumed away.",
        "summary": (
            "Hold `λ` and `μ` still and every cut gives the same ratio `ρ = λ/μ`, so the product "
            "telescopes and `πₙ = π₀ρⁿ`. The geometric distribution is a consequence of the cut "
            "equations rather than a separate result: nothing was assumed about the shape of `π`. "
            "But this kit works on a finite chain and an M/M/1 queue does not, so every figure "
            "here is an approximation and the page prints the size of it &mdash; the exact tail "
            "mass `ρ^(N+1)` the truncation redistributed, and the gap between the chain's `L` and "
            "the closed form's. The closed form is `sysdesign_core`'s, called rather than "
            "rewritten, so the two Subjects cannot disagree about M/M/1."
        ),
        "key": [
            "every cut gives the same ratio ρ = λ/μ, so πₙ = π₀ρⁿ — derived, not quoted",
            "untruncated:  π₀ = 1 − ρ,  L = ρ/(1 − ρ),  P(N > k) = ρ^(k+1)",
            "truncated at N:  the chain normalises over what it kept, and ρ^(N+1) is what it lost",
            "ρ = 4/5 at 40 states:  L is 3.99564 against the closed form's 4",
            "the truncation drops 0.000106, and the gap in L is 0.004360",
            "ρ = 19/20 at 60 states:  it drops 0.043766, and L is 16.20806 against 19",
        ],
        "key_label": "A geometric distribution derived, and the price of a finite chain",
        "concepts_intro": (
            "Three ideas. The first is where the geometric shape comes from, the second is what "
            "the truncation costs, and the third is why the closed form on the page is borrowed "
            "rather than written here."
        ),
        "concepts": [
            ("The geometric distribution is a consequence, not an assumption",
             "With `λₙ = λ` and `μₙ = μ` for every n, each cut ratio is `λ/μ = ρ`, so the running "
             "product from `π₀` is `1, ρ, ρ², …` and normalising gives `πₙ = π₀ρⁿ`. On an "
             "unbounded chain the total is `1/(1 − ρ)` and `π₀ = 1 − ρ`. Nothing was postulated "
             "about the shape of `π`; it fell out of one equation applied repeatedly."),
            ("A finite chain is a different model, and the difference is a number",
             "`birthDeath` truncates, and an M/M/1 queue has infinitely many states. The exact "
             "mass the untruncated chain puts above state N is `ρ^(N+1)`, and the truncation "
             "redistributes it over the states kept. At `ρ = 4/5` and forty states that is "
             "`0.000106`; at `ρ = 19/20` and sixty states it is `0.043766`, which is not small. "
             "The page prints it rather than choosing a state count at which to stop mentioning "
             "it."),
            ("The closed form is imported, so two Subjects cannot drift apart",
             "`mm1` comes from `sysdesign_core`, the same function &ldquo;The M/M/1 "
             "Queue&rdquo; is built on. This page calls it and labels the column with its name. "
             "Writing a second implementation would be inviting exactly the disagreement that "
             "is hardest to find: two pages in one library quoting different numbers for the "
             "same model, each internally consistent."),
        ],
        "read_title": "Constant rates, a geometric distribution, and an honest error term",
        "read_intro": "Where the geometric shape comes from, what the finite chain costs, the tail probabilities against their closed forms, and what ρ ≥ 1 does.",
        "body": [
            ("def", ("The M/M/1 chain",
                     "A birth-death chain with `λₙ = λ` for every `n` and `μₙ = μ` for every "
                     "`n ≥ 1`. Write `ρ = λ/μ`, the <strong>utilisation</strong>.",
                     "`μ` is a <strong>rate</strong>, not a duration: a service taking `1/5` of "
                     "a unit of time has `μ = 5`. That confusion is the single commonest way to "
                     "get a queueing answer exactly upside down, and it is worth checking in "
                     "the units before anything else.")),
            ("p", "Everything about this model follows from feeding two constant lists to the "
                  "same function the preceding material used. The lab does not switch "
                  "algorithms; it switches the rate lists. That is the claim &ldquo;one chain, "
                  "five readings&rdquo; being kept rather than asserted."),
            ("thm", ("Geometric stationary distribution",
                     "For the M/M/1 chain with `ρ < 1` on states `0, 1, 2, …`, "
                     "`πₙ = (1 − ρ)ρⁿ`, `L = ρ/(1 − ρ)`, and `P(N > k) = ρ^(k+1)`.")),
            ("proof", ["Each cut gives `πₙ₊₁ = πₙ · λ/μ = πₙρ`, so `πₙ = π₀ρⁿ` by induction.",
                       "The weights sum to `Σₙ ρⁿ = 1/(1 − ρ)` for `ρ < 1`, so `π₀ = 1 − ρ`. "
                       "Then `P(N > k) = Σ_{n>k} (1 − ρ)ρⁿ = ρ^(k+1)`, and `L = Σ n(1 − ρ)ρⁿ` "
                       "is the standard geometric mean `ρ/(1 − ρ)`. The `ρ ≥ 1` case has no "
                       "distribution at all, because the weights do not sum to anything "
                       "finite."]),
            ("h3", "What the truncation costs, in fractions"),
            ("math", [
                "λ = 4, μ = 5, ρ = 4/5, chain kept to state 40",
                "",
                "                    from the cut equations      from sysdesign_core.mm1",
                "     ρ                    4/5                          4/5",
                "     π₀                   0.2000212699                 1/5",
                "     L                    3.99563967                   4",
                "     Lq                   3.19566094                   16/5",
                "     W                    0.99893648                   1",
                "",
                "     gap in L             0.004360",
                "     ρ⁴¹ = what the untruncated chain puts above state 40   0.000106",
                "",
                "     π₀ as an exact fraction: 28 digits over 29",
                "",
                "λ = 19, μ = 20, ρ = 19/20, chain kept to state 60",
                "",
                "     L from the chain     16.20806          closed form   19",
                "     ρ⁶¹                   0.043766",
                "     π₀ exactly            79 digits over 80",
                "     at 90 states, π₀'s denominator runs to 119 digits",
            ]),
            ("p", "Read the two `L` columns together. They are close at `ρ = 4/5` and they are "
                  "not close at `ρ = 19/20`, and the reason is entirely in the tail: at four "
                  "fifths loaded the untruncated chain puts about one part in ten thousand above "
                  "state 40, and at nineteen twentieths it puts four per cent above state 60. "
                  "The mean is sensitive to that mass because the mass sits at large n, so a "
                  "four-per-cent tail moves `L` from 19 to 16.2."),
            ("p", "The chain's `π₀` comes out as `0.2000212699` rather than `0.2` for the same "
                  "reason: the truncation redistributes the lost tail over the states kept, and "
                  "state 0 gets the largest share of it. That is not error in the arithmetic "
                  "sense &mdash; the fraction is exact, twenty-eight digits over twenty-nine "
                  "&mdash; it is the exact answer to a slightly different question. Pulling the "
                  "state slider down and watching the two `L` columns separate is the fastest "
                  "way to see the difference stop being negligible."),
            ("h3", "The tail, twice"),
            ("p", "`P(N > k)` on the truncated chain is a finite sum of exact fractions; on the "
                  "untruncated chain it is `ρ^(k+1)`. The page prints both and their difference. "
                  "At `ρ = 4/5` and forty states: `0.79997873` against `0.8` at `k = 0`, "
                  "`0.40953721` against `0.4096` at `k = 3`, `0.00911800` against `0.00922337` "
                  "at `k = 20`. The discrepancy grows with `k`, which is exactly where the "
                  "missing tail is."),
            ("example", ("ρ at least 1, and what the finite chain is then",
                         "Set `λ = 5` and `μ = 4`. The page reports `ρ = 5/4 ≥ 1` in red: there "
                         "is no untruncated M/M/1 queue here at all, and the backlog grows "
                         "without bound at rate 1 per unit time.",
                         "The finite chain still has a distribution, because it cannot grow past "
                         "the last state. But that distribution belongs to a different model "
                         "&mdash; one with a buffer &mdash; and reporting it as an M/M/1 answer "
                         "would be reporting a number for a queue that has none. "
                         "&ldquo;Finite Buffers, Blocking and the Admitted Rate&rdquo; is where "
                         "the buffered model belongs, and there `ρ ≥ 1` is not a problem at "
                         "all.")),
            ("example", ("Half loaded, where the truncation genuinely is negligible",
                         "At `λ = 1`, `μ = 2` and thirty states, `ρ = 1/2` and `ρ³¹` is about "
                         "`5 × 10⁻¹⁰`. The chain's `L` is `0.99999999` against the closed "
                         "form's `1`, and `π₀` is `0.5000000002` against `1/2`.",
                         "This is the case people generalise from, and generalising from it is "
                         "the mistake. The tail mass falls like `ρ^N`, so halving the load does "
                         "not halve the error, it changes its exponent; and at `ρ = 19/20` the "
                         "same thirty states would be useless. The page prints the number so "
                         "that you never have to reason about which case you are in.")),
            ("p", "One more thing the exact column buys. At sixty states and `ρ = 19/20`, `π₀` "
                  "is a fraction of seventy-nine digits over eighty, and at ninety states its "
                  "denominator runs to a hundred and nineteen. Those are carried whole. A "
                  "double could not hold them, so a decimal implementation would be storing the "
                  "nearest number it had and calling it `π₀` &mdash; and it would have no way to "
                  "tell you that the difference between its `L` and the closed form's was "
                  "truncation rather than rounding."),
        ],
        "lab": ("birthdeath", {
            "mode": "mm1",
            "preset": "eighty",
            "panel_title": "Set the two rates and choose how much of the chain to keep",
            "panel_intro": "Every figure on the left comes from the cut equations on a finite "
                           "chain. The column beside it is the closed form the System Design "
                           "path already owns, called rather than re-derived, so the two "
                           "Subjects cannot disagree about M/M/1. Drag the state count down and "
                           "watch the two L columns separate.",
        }),
        "steps_title": "Reading an M/M/1 answer without overclaiming it",
        "steps_intro": "Four steps, and the last one is what separates a number from a number you can defend.",
        "steps": [
            ("Check the units on μ before anything else",
             "`μ` is completions per unit time. If what you have is a service duration, invert "
             "it. A model built with a duration where a rate belongs gives `ρ` upside down and "
             "every subsequent figure with it, and the numbers will look entirely plausible."),
            ("Compute ρ and stop if it is at least 1",
             "At `ρ ≥ 1` there is no M/M/1 distribution: the weights do not sum to anything "
             "finite. Any finite answer you see is an answer about a bounded model, and you "
             "should say which bound."),
            ("Derive π from the cuts rather than recalling it",
             "Each ratio is `ρ`, so `πₙ = π₀ρⁿ` and `π₀ = 1 − ρ`. Two lines, no memorised "
             "formula, and the derivation survives the moment one of the rates stops being "
             "constant &mdash; which is the next thing that will happen to it."),
            ("Quote the truncation mass beside any figure from a finite chain",
             "`ρ^(N+1)` is the exact probability the untruncated chain puts above your last "
             "state. If it is `0.000106` your `L` is good to three decimals; if it is `0.043766` "
             "your `L` is out by nearly three. Printing the number costs one power and removes "
             "the judgement call entirely."),
        ],
        "worked": {
            "title": "Four fifths loaded at forty states, and nineteen twentieths at sixty",
            "intro": [
                "The same arithmetic at two loads. Only the two rates and the state count "
                "change, and the point of the pair is how differently the truncation behaves.",
            ],
            "lines": [
                "λ = 4, μ = 5     ρ = 4/5      chain kept to state 40",
                "",
                "   cut ratio at every cut      4/5",
                "   weights   1, 4/5, 16/25, 64/125, …, (4/5)⁴⁰",
                "   total     (1 − (4/5)⁴¹)/(1 − 4/5)",
                "",
                "                        chain            closed form      difference",
                "      π₀              0.2000212699          1/5",
                "      L               3.99563967             4             0.004360",
                "      Lq              3.19566094            16/5",
                "      W               0.99893648             1",
                "",
                "      truncation mass  ρ⁴¹ = 0.000106",
                "",
                "   P(N > k), truncated against ρ^(k+1):",
                "      k =  0     0.79997873      0.80000000      0.000021",
                "      k =  3     0.40953721      0.40960000      0.000063",
                "      k = 10     0.08580213      0.08589935      0.000097",
                "      k = 20     0.00911800      0.00922337      0.000105",
                "",
                "λ = 19, μ = 20    ρ = 19/20     chain kept to state 60",
                "",
                "                        chain            closed form      difference",
                "      π₀              0.0522884735          1/20",
                "      L              16.20806234            19             2.791938",
                "      W               0.85511582             1",
                "",
                "      truncation mass  ρ⁶¹ = 0.043766",
                "      π₀ exactly:  79 digits over 80",
            ],
            "after": [
                "The `P(N > k)` block is the clearest picture of where the missing mass went. At "
                "`k = 0` the two agree to five decimals; by `k = 20` the difference has grown to "
                "`0.000105`, which is almost the whole truncation mass `0.000106`. That is not a "
                "coincidence: the mass the truncation threw away was all above state 40, so it "
                "is missing from every tail probability and the shortfall converges on the full "
                "`ρ⁴¹`.",
                "The second block is the same computation at a load a designer would actually "
                "worry about, and it is where the habit of printing the error pays. `L = 16.2` "
                "against a true `19` is not a rounding; it is a sixty-state model being asked a "
                "question about an unbounded one. Nothing about the left-hand column looks "
                "suspicious on its own.",
                "For a rehearsal, take the four-fifths case and drag the state count from 40 "
                "down to 10. The supplied first move is that `ρ¹¹` is about `0.086`, so roughly "
                "nine per cent of the mass is being redistributed. Predict which way `π₀` moves "
                "and by how much before you look, and then say why `L` moves further in relative "
                "terms than `π₀` does.",
            ],
        },
        "quiz_title": "Geometric shape, and the price of a finite chain",
        "quiz": [
            {"q": "Where does `πₙ = (1 − ρ)ρⁿ` come from on this course?",
             "a": ["It is the definition of the M/M/1 queue",
                   "It is assumed, and then checked against a simulation",
                   "It falls out of the cut equations once every rate is held constant, since each ratio is then ρ",
                   "It is a limit of the binomial distribution"],
             "c": 2,
             "why": "Each cut gives `πₙ₊₁ = πₙρ`, so the running product is `ρⁿ` and normalising "
                    "over an unbounded chain gives `π₀ = 1 − ρ`. Nothing about the shape of `π` "
                    "was postulated, which matters because the derivation survives a rate that "
                    "varies and a memorised formula does not."},
            {"q": "At `ρ = 19/20` on a chain kept to sixty states, `L` is `16.21` against the closed form's `19`. What is the difference?",
             "a": ["Rounding error in the exact arithmetic",
                   "The truncation: the untruncated chain puts `0.043766` of its probability above state 60, and that mass sits at large n",
                   "An error in `sysdesign_core.mm1`",
                   "The two quantities mean different things"],
             "c": 1,
             "why": "Both columns are exact. The left one is the exact answer for a sixty-state "
                    "chain and the right one the exact answer for an unbounded one, and at this "
                    "load four per cent of the probability lives above state 60. Because that "
                    "mass is at large occupancy it carries a lot of the mean."},
            {"q": "Why does this kit call `sysdesign_core.mm1` rather than implementing the closed form?",
             "a": ["Because the closed form is hard to implement",
                   "Because a second implementation could drift, and then one library would quote two different answers for the same model, each internally consistent",
                   "Because the exact arithmetic cannot express `ρ/(1 − ρ)`",
                   "Because the System Design path owns the licence to the formula"],
             "c": 1,
             "why": "The same function is what &ldquo;The M/M/1 Queue&rdquo; is built on. "
                    "Sharing it makes disagreement between the two Subjects impossible rather "
                    "than unlikely, and the page names the function beside the column it "
                    "produced."},
            {"q": "A service takes on average `1/5` of a unit of time. What is `μ`?",
             "a": ["`1/5`", "`5`", "`4/5`", "It depends on λ"],
             "c": 1,
             "why": "`μ` is a rate: completions per unit time, so a service of duration `1/5` "
                    "gives `μ = 5`. Typing the duration instead inverts `ρ` and turns a lightly "
                    "loaded queue into an overloaded one, with every downstream figure "
                    "plausible and wrong."},
        ],
        "mistakes": [
            ("Reporting a finite chain's figures as M/M/1 figures",
             "They are exact answers for the chain you truncated, not for the model you meant. "
             "The gap is `ρ^(N+1)` in probability mass and is printed on the page; at "
             "`ρ = 19/20` and sixty states it moves `L` by nearly three, and nothing about the "
             "figure looks wrong on its own."),
            ("Generalising from a lightly loaded example",
             "At `ρ = 1/2` and thirty states the truncation mass is about `5 × 10⁻¹⁰` and can be "
             "ignored. The mass falls like `ρ^N`, so the same state count at `ρ = 19/20` leaves "
             "several per cent outside the model. &ldquo;Enough states&rdquo; is a function of "
             "the load and not a habit."),
            ("Confusing the service rate with the service time",
             "`μ = 5` means five completions per unit time, that is a mean service of `1/5`. "
             "Entering `1/5` as `μ` against `λ = 4` reports `ρ = 20` and an overloaded system "
             "where the truth is four fifths loaded. The lab says `μ` is a rate in the error "
             "message for exactly this reason."),
        ],
        "standard": ("Finish when you can derive the geometric distribution from a cut in two lines and say what your state count cost you.",
                     "You should be able to get `πₙ = (1 − ρ)ρⁿ` from the cut equations rather "
                     "than from memory, compute `L`, `Lq`, `W` and `P(N > k)` from it, quote "
                     "`ρ^(N+1)` as the truncation mass beside any finite-chain figure, and "
                     "recognise `ρ ≥ 1` as the absence of a model rather than as a large "
                     "answer."),
        "note": 'One change to one list turns this into a queue with several servers: `μₙ = min(n, s)μ`, and the cut equations do not notice, because they were never told the rates were constant. What falls out is Erlang C, added up from the same π rather than computed from a second formula. &ldquo;More Servers, and Erlang C Read Off π&rdquo; also has the argument for pooling as a single number, and one banner that had to be corrected.',
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "more-servers-and-erlang-c-read-off-pi",
        "title": "More Servers, and Erlang C Read Off π",
        "module": "The named queues",
        "one_line": "μₙ = min(n, s)μ is the whole of M/M/s, and the probability an arrival waits is P(N ≥ s) added up from the same π.",
        "summary": (
            "One line changes. Below `s` customers an arrival finds a free server, so adding a "
            "customer adds a busy server and the service rate rises with n; at and above `s` "
            "every server is busy and the rate stops rising. That is `μₙ = min(n, s)μ`, and the "
            "cut equations do not notice, because they were never told the rates were constant. "
            "<strong>Erlang C is not a second formula on this page</strong>: the probability an "
            "arrival has to wait is the probability the system is already at `s` or above, which "
            "is `πₛ + πₛ₊₁ + ⋯`, added up from the distribution the cuts produced. The closed "
            "form from the System Design core sits beside it."
        ),
        "key": [
            "μₙ = min(n, s)μ        one change to one list, and that is all of M/M/s",
            "offered load a = λ/μ, utilisation ρ = a/s;  a does not change when s does",
            "P(an arrival waits) = P(N ≥ s) = πₛ + πₛ₊₁ + ⋯      a reading, not a formula",
            "a = 2:  one server 100%, two 96.296%, three 44.444%, four 17.391%, five 5.970%",
            "at s = 3 the closed form erlangC gives 4/9 = 44.444%, and the two agree",
            "busy servers = a only when the queue settles: at a = 2, s = 1 it is 1, not 2",
        ],
        "key_label": "One line changed, and the waiting probability collapsing at fixed load",
        "concepts_intro": (
            "Three ideas. The first is the model, the second is what Erlang C actually is, and "
            "the third is a sentence that is true only under a condition and used to be printed "
            "without it."
        ),
        "concepts": [
            ("Several servers is one change to the service-rate list",
             "With `n` customers and `s` servers, `min(n, s)` of them are busy, so the completion "
             "rate out of state `n` is `min(n, s)μ`. Below `s` the chain speeds up as it fills; "
             "at and above `s` it cannot speed up any further. Nothing else about the model "
             "changes, and the cut equations apply unaltered because they never assumed a "
             "constant rate."),
            ("Erlang C is a reading of π, not a second derivation",
             "An arriving customer waits exactly when every server is already busy, that is when "
             "the system is at state `s` or above. So the waiting probability is "
             "`Σ_{n ≥ s} πₙ`, summed from the distribution the cuts produced. The closed form "
             "`erlangC` from `sysdesign_core` is printed beside it as a check on the truncated "
             "chain, and at three servers on the worked load both give `44.444%`."),
            ("Adding a server does not reduce the work, only the waiting",
             "The offered load `a = λ/μ` is a property of the arrivals and the service, and "
             "neither moves when a server is added: the same work arrives and, while the queue "
             "settles, the same work is done. What collapses is the probability of waiting "
             "&mdash; from `96.296%` at two servers to `44.444%` at three to `17.391%` at four, "
             "at a fixed load of 2. That is the argument for pooling as a number."),
        ],
        "read_title": "s servers, the same work, far less waiting",
        "read_intro": "The rate list, the waiting probability read off π, the pooling table, and the one sentence that needed a condition attached to it.",
        "body": [
            ("def", ("The M/M/s chain",
                     "A birth-death chain with `λₙ = λ` for every `n` and "
                     "`μₙ = min(n, s)·μ`, where `μ` is the rate of ONE server. Write "
                     "`a = λ/μ` for the <strong>offered load</strong> and `ρ = a/s` for the "
                     "<strong>utilisation</strong> per server.",
                     "An arriving customer <strong>waits</strong> when all `s` servers are busy, "
                     "which is exactly when the system is in state `s` or above. That "
                     "probability is <strong>Erlang C</strong>.")),
            ("p", "Two ratios and it is easy to use the wrong one. `a = λ/μ` is how much work "
                  "arrives per unit time, measured in server-loads; it is `2` on the worked "
                  "example whether there are two servers or five. `ρ = a/s` is the fraction of "
                  "each server's time that work would occupy, and it is the one that has to be "
                  "below 1 for an unbounded queue to settle."),
            ("math", [
                "λ = 2, μ = 1 (per server), s = 3        a = 2,  ρ = a/s = 2/3",
                "",
                "   service rate out of state n:   n = 1 → 1     n = 2 → 2",
                "                                  n = 3 → 3     n = 4 → 3   and 3 thereafter",
                "",
                "   cut ratios:   2/1, 2/2, 2/3, 2/3, 2/3, …",
                "   weights:      1, 2, 2, 4/3, 8/9, 16/27, …",
                "",
                "   π₀ = 0.111111   π₁ = 0.222222   π₂ = 0.222222",
                "   π₃ = 0.148148   π₄ = 0.098765   π₅ = 0.065844",
                "",
                "   P(wait) = π₃ + π₄ + π₅ + ⋯   =   44.444%",
                "   sysdesign_core.erlangC(2, 1, 3)  =  4/9  =  44.444%",
            ]),
            ("p", "The two figures are computed from different things. The left one is a sum of "
                  "entries of the truncated chain's `π`; the right one is the closed form for an "
                  "unbounded M/M/s, `4/9` exactly. They agree to well under a millionth here, "
                  "and the page prints a green tick when they do. On a chain kept too short for "
                  "its load they will not, and the page will say so &mdash; which is the correct "
                  "behaviour, because the disagreement is real and belongs to the truncation."),
            ("h3", "Pooling, at a fixed load"),
            ("math", [
                "the same offered load a = 2, spread over more servers",
                "",
                "   servers    ρ = a/s    P(wait)     Lq        Wq       each server busy",
                "      1          2       100.000%   38.00000  38.00000       100.00%",
                "      2          1        96.296%   18.29630   9.37975        97.53%",
                "      3         2/3       44.444%    0.88889   0.44444        66.67%",
                "      4         1/2       17.391%    0.17391   0.08696        50.00%",
                "      5         2/5        5.970%    0.03980   0.01990        40.00%",
                "",
                "   the offered load is 2 in every row, and the waiting collapses anyway",
            ]),
            ("p", "The third row is where the system becomes usable and the second is where it "
                  "is not. At two servers `ρ = 1` exactly: the work arriving equals the work the "
                  "servers can do, the unbounded queue does not settle, and the only reason a "
                  "finite `Lq` appears at all is the truncation at forty states. At three the "
                  "utilisation is two thirds and the waiting probability has fallen by more than "
                  "half. Nothing about the arrivals or the service changed between those rows."),
            ("p", "Notice also the last column. Each server is busy `66.67%` of the time at "
                  "three servers and `40%` at five, so the per-server utilisation falls as the "
                  "waiting falls &mdash; which is the price of pooling and the reason it is a "
                  "trade rather than a free lunch. &ldquo;Many Servers: Pooling, and Erlang "
                  "C&rdquo; makes the same comparison from the closed forms; this page makes it "
                  "from a distribution you can see."),
            ("h3", "The sentence that needed a condition"),
            ("p", "The expected number of busy servers is `Σ min(n, s)πₙ`, and on a queue that "
                  "settles it equals the offered load `a`: every arriving customer is eventually "
                  "served, so the work completed per unit time equals the work arriving, and "
                  "adding a server does not change either. At `a = 2` the busy count is `2.0000` "
                  "at three servers, at four and at five."),
            ("example", ("Where busy servers equals offered load stops being true",
                         "Set `λ = 2`, `μ = 1` and one server. The offered load is still 2. The "
                         "expected number of busy servers is `1.0` &mdash; it cannot exceed "
                         "`s = 1` &mdash; and the work the server finishes is `1` per unit time "
                         "against the `2` arriving.",
                         "So &ldquo;on average `a`'s worth of work is being done, whatever `s` "
                         "is&rdquo; is false here, and this page used to print it without a "
                         "condition. The banner now branches on `ρ`: below 1 it states the "
                         "identity, and at `ρ ≥ 1` it says instead that the servers cannot keep "
                         "up, prints what they do finish, and notes that only the truncation "
                         "stops the difference piling up without bound.")),
            ("p", "That correction is worth dwelling on, because the false version is more "
                  "memorable than the true one and survives being half-remembered. The identity "
                  "&ldquo;throughput equals offered load&rdquo; is a conservation statement "
                  "about a system in equilibrium, and a system at `ρ ≥ 1` has none; what it has "
                  "is a backlog growing at `λ − sμ` per unit time, which "
                  "&ldquo;Transient Overload and Draining the Backlog&rdquo; is about."),
            ("example", ("Two servers at three quarters loaded",
                         "With `λ = 3`, `μ = 2` and two servers the offered load is `3/2` and "
                         "`ρ = 3/4`. The chain gives `P(wait) = 64.285%` and `Lq = 1.928`, and "
                         "the closed form gives `64.286%`.",
                         "The two differ by about three parts in a million, which is larger than "
                         "the page's own agreement threshold, so it prints a disagreement here "
                         "even though nothing is wrong: the chain is kept to forty states at a "
                         "load whose tail decays like `(3/4)ⁿ`. The lesson is the one the "
                         "preceding material made &mdash; a truncated chain is a different model "
                         "&mdash; and the threshold is a property of this page rather than of "
                         "the mathematics.")),
        ],
        "lab": ("birthdeath", {
            "mode": "mms",
            "preset": "desk",
            "panel_title": "Set the load and slide the number of servers",
            "panel_intro": "The service rate out of state n is min(n, s)μ, and that single "
                           "change is the whole of M/M/s. The probability of waiting is summed "
                           "from the resulting π and checked against the closed form the System "
                           "Design path uses. Slide the servers and watch the offered load stay "
                           "still while the waiting collapses.",
        }),
        "steps_title": "Sizing a bank of servers",
        "steps_intro": "Four steps. The first two are about which ratio you are holding, and the fourth is the one that turns a table into a decision.",
        "steps": [
            ("Compute the offered load first, and keep it separate from the utilisation",
             "`a = λ/μ` in server-loads, `ρ = a/s` per server. `a` is a property of the demand "
             "and the service; `ρ` is what you change by adding capacity. Writing both down "
             "stops the standard slip of comparing a load of 2 against a utilisation of 2."),
            ("Build the rate list with min(n, s)μ and hand it to the same machinery",
             "No new model and no new formula. The cut equations give the ratios, the product "
             "gives the weights, normalising gives `π`, exactly as on a single server."),
            ("Read the waiting probability off π rather than computing it",
             "`P(wait) = Σ_{n ≥ s} πₙ`. This is what Erlang C is. Having it as a sum rather than "
             "as a formula is what lets you answer a variant &mdash; a finite waiting room, a "
             "customer who balks &mdash; where the formula does not apply."),
            ("Compare across s at fixed a, and price the idle capacity",
             "Hold the load and vary the servers: the waiting probability falls sharply and the "
             "per-server utilisation falls with it. Both columns are the decision. A table that "
             "shows only the waiting makes pooling look free."),
        ],
        "worked": {
            "title": "A three-server desk at an offered load of two, and the same load on one to five servers",
            "intro": [
                "Arrivals at 2 per unit time, each server completing 1 per unit time. The "
                "offered load is 2 in every row below; only the number of servers changes.",
            ],
            "lines": [
                "λ = 2,  μ = 1 per server,  s = 3        a = 2,  ρ = 2/3",
                "",
                "  service rates out of states 1, 2, 3, 4, …:   1, 2, 3, 3, …",
                "  cut ratios                                   2, 1, 2/3, 2/3, …",
                "  weights from π₀ = 1                          1, 2, 2, 4/3, 8/9, 16/27, …",
                "",
                "  π    0.111111   0.222222   0.222222   0.148148   0.098765   0.065844",
                "       n = 0      n = 1      n = 2      n = 3      n = 4      n = 5",
                "",
                "  an arrival waits when n ≥ 3:",
                "     P(wait)  =  π₃ + π₄ + π₅ + ⋯  =  44.444%",
                "     erlangC(2, 1, 3)               =  4/9  =  44.444%",
                "     the two differ by 5.0e-8, which is the truncation at 40 states",
                "",
                "  Lq from the chain   0.88889          closed form  8/9",
                "  Wq                  0.44444          busy servers 2.0000 of 3",
                "",
                "the same load on one to five servers",
                "",
                "     s     ρ       P(wait)      Lq          each server busy",
                "     1     2       100.000%    38.00000        100.00%",
                "     2     1        96.296%    18.29630         97.53%",
                "     3     2/3      44.444%     0.88889         66.67%",
                "     4     1/2      17.391%     0.17391         50.00%",
                "     5     2/5       5.970%     0.03980         40.00%",
                "",
                "and the case the banner had to be fixed for:",
                "     λ = 2, μ = 1, s = 1:   a = 2,  busy servers = 1.0,  not 2",
            ],
            "after": [
                "The `Lq` column is the one that makes the case. Going from two servers to three "
                "takes the expected queue from about eighteen to under one &mdash; a factor of "
                "twenty for one more server, at a load that did not change. That is not a "
                "smooth trade-off; it is the collapse that happens as `ρ` comes away from 1, and "
                "&ldquo;The Knee: Response Time vs Utilisation&rdquo; is the same phenomenon "
                "seen from the other side.",
                "The two-server row deserves suspicion rather than admiration. `ρ = 1` exactly, "
                "so the unbounded queue does not settle at all and `Lq = 18.3` is a fact about "
                "keeping forty states. Drag the state count up and it grows; the closed form "
                "refuses the row entirely. A finite number appearing where none should is "
                "exactly the failure mode the preceding material warned about.",
                "The last line is the honesty fix. At one server the offered load is 2 and the "
                "busy count is 1, so the tidy sentence &ldquo;busy servers equals the offered "
                "load whatever `s` is&rdquo; is false. It is true while the queue settles, and "
                "the page now branches on `ρ` and says the other thing when it does not.",
                "For a rehearsal, keep three servers and raise `λ` from 2 to 3. The supplied "
                "first move is that `a` becomes 3 and `ρ` becomes 1. Predict what happens to "
                "`P(wait)` and to the agreement with the closed form, then check: one of the two "
                "columns stops existing, and the other keeps printing a number.",
            ],
        },
        "quiz_title": "Servers, load and waiting",
        "quiz": [
            {"q": "What single change turns the M/M/1 chain into M/M/s?",
             "a": ["The arrival rate becomes `λ/s`",
                   "The service rate out of state `n` becomes `min(n, s)μ`",
                   "The chain gains `s` parallel copies of itself",
                   "The cut equation gains a factor of `s`"],
             "c": 1,
             "why": "Below `s` customers, adding one adds a busy server; at and above `s` every "
                    "server is already working. That is one line in the rate list, and the cut "
                    "equations are untouched because they never assumed the rates were "
                    "constant."},
            {"q": "Erlang C on this page is computed how?",
             "a": ["From the standard closed-form expression",
                   "By summing `πₙ` over `n ≥ s`, which is what the quantity means",
                   "By simulating arrivals and counting those that wait",
                   "As `ρ` raised to the power `s`"],
             "c": 1,
             "why": "An arrival waits exactly when every server is busy, that is when the system "
                    "is at `s` or above. The closed form is printed beside the sum as a check, "
                    "and having the quantity as a sum is what lets the same reasoning survive "
                    "into models the formula does not cover."},
            {"q": "At a fixed offered load of 2, going from three servers to four takes `P(wait)` from `44.444%` to `17.391%`. What happened to the work arriving?",
             "a": ["It fell by the same proportion", "It fell by one server's worth",
                   "Nothing: `a = λ/μ` and neither λ nor μ moved",
                   "It rose, because more servers attract more arrivals"],
             "c": 2,
             "why": "The offered load is a property of the demand and the service rate. Adding "
                    "a server reduces the waiting and lowers each server's utilisation; it does "
                    "not reduce the work. That is what makes pooling a real argument and also "
                    "what makes it a trade."},
            {"q": "At `λ = 2`, `μ = 1` and one server, the expected number of busy servers is `1.0` while the offered load is `2`. Why?",
             "a": ["Because the calculation is wrong",
                   "Because the busy count cannot exceed `s`, and at `ρ ≥ 1` the server cannot keep up, so throughput is `sμ = 1` rather than the offered `2`",
                   "Because the chain was truncated at forty states",
                   "Because the offered load should have been divided by `s`"],
             "c": 1,
             "why": "&ldquo;Busy servers equals offered load&rdquo; is a conservation statement "
                    "about a system that settles: work in equals work out. At `ρ ≥ 1` there is "
                    "no equilibrium, the server is busy essentially always, and the excess "
                    "`λ − sμ` accumulates in the queue."},
        ],
        "mistakes": [
            ("Comparing the offered load against 1 instead of the utilisation",
             "`a = λ/μ` can be 4 on a perfectly comfortable five-server system. The condition "
             "for an unbounded queue to settle is `ρ = a/s < 1`. Writing both down and labelling "
             "them removes the whole class of error, and the lab prints them as two separate "
             "figures for that reason."),
            ("Quoting a finite queue length at ρ = 1",
             "The unbounded queue has no stationary distribution at `ρ = 1`, so any `Lq` you see "
             "is a property of the state count. It grows as you keep more states. The closed "
             "form refuses the case; a truncated chain will happily print `18.29630` and look "
             "like an answer."),
            ("Saying that the servers do a's worth of work whatever s is",
             "True while the queue settles and false otherwise. At `a = 2` with one server the "
             "busy count is `1`, not `2`, and the missing work is piling up. The sentence needs "
             "`ρ < 1` attached to it every time, which is why the page branches rather than "
             "printing one version."),
        ],
        "standard": ("Finish when adding a server is a change you can make to one list, and Erlang C is a sum you can point at in a distribution.",
                     "You should be able to write `μₙ = min(n, s)μ`, keep the offered load and "
                     "the utilisation apart, read the waiting probability off `π` as "
                     "`P(N ≥ s)`, produce the pooling table at a fixed load and read both of its "
                     "consequences, and state the condition under which busy servers equals "
                     "offered load together with a case where it fails."),
        "note": 'Every chain so far has been truncated as an approximation and apologised for it. The next one is truncated on purpose: a system with a waiting room of size K loses the arrivals that find it full, so the wall is the model rather than a compromise. `ρ ≥ 1` stops mattering entirely, and one division becomes two. &ldquo;Finite Buffers, Blocking and the Admitted Rate&rdquo; prints both of them side by side.',
    },

    # ---------------------------------------------------------------- 09
    {
        "slug": "finite-buffers-blocking-and-the-admitted-rate",
        "title": "Finite Buffers, Blocking and the Admitted Rate",
        "module": "The named queues",
        "one_line": "A queue with a wall does not need to be stable: ρ ≥ 1 is fine, and Little's Law wants λ(1 − π_K) rather than λ.",
        "summary": (
            "Stop the chain at `K` and the truncation is no longer an approximation &mdash; it "
            "is the model. An arrival that finds the system full is lost, so "
            "<strong>`ρ ≥ 1` stops being a stability condition</strong>: a queue that cannot "
            "grow cannot run away, and it has a perfectly good distribution at any load. Two "
            "consequences follow. The rate that actually gets in is `λ(1 − π_K)` rather than "
            "`λ`, and that is the rate Little's Law needs; dividing by `λ` instead is the "
            "standard error in a finite-queue calculation and it is always too small. Both "
            "divisions are printed, labelled, side by side."
        ),
        "key": [
            "a chain stopped at K: no arc out of the top state, and an arrival that finds it full is lost",
            "ρ = λ/μ is no longer a stability condition — a queue with a wall cannot run away",
            "blocking = π_K       admitted rate = λ(1 − π_K)       and that is what L = λW needs",
            "λ = 6, μ = 5, K = 5:  ρ = 6/5, blocking 25.0588%, admitted 4.496471 of 6",
            "L = 3.021172,  W = L/admitted = 0.671899,  L/λ = 0.503529 — too small by 1 − π_K",
            "balking instead:  λₙ = λ/(n+1), and no closed form covers it at all",
        ],
        "key_label": "A wall instead of a stability condition, and the two numbers people call W",
        "concepts_intro": (
            "Three ideas. The first removes a condition, the second adds a rate, and the third "
            "is the case that shows why this course builds queues from a cut rather than from a "
            "table."
        ),
        "concepts": [
            ("Truncation here is the model, not an approximation of one",
             "The chain genuinely stops at `K` because the system genuinely has `K + 1` places. "
             "Nothing is being thrown away and no error term is owed. That also means `ρ ≥ 1` is "
             "not a problem: at `λ = 6` and `μ = 5` the distribution exists, it is simply "
             "weighted towards the top, and `25.0588%` of the time the system is full."),
            ("The admitted rate is not the arrival rate",
             "Arrivals that find the system full are lost, so the long-run rate of admissions is "
             "`λ(1 − π_K)`. That is the rate Little's Law needs, because `L = λW` counts "
             "customers who were in the system, and a blocked arrival never was. On the worked "
             "example the admitted rate is `4.496471` against an arrival rate of `6`."),
            ("The balking chain is what a table of formulas cannot cover",
             "Let an arrival join a queue of length `n` with probability `1/(n + 1)`, so "
             "`λₙ = λ/(n + 1)`. The closed form for a blocking queue assumes a constant arrival "
             "rate and does not apply. The cut equation never assumed one, so it handles the "
             "case without changing &mdash; which is the whole reason this material started from "
             "the cut."),
        ],
        "read_title": "A queue with a wall, and the rate that actually gets in",
        "read_intro": "What a hard limit does to the stability condition, the two divisions Little's Law invites, the closed form agreeing exactly, and the chain no closed form covers.",
        "body": [
            ("def", ("The M/M/1/K chain, and a balking chain",
                     "<strong>M/M/1/K</strong>: constant rates on states `0` to `K`, with no "
                     "arrival out of state `K`. An arrival finding the system full is "
                     "<strong>blocked</strong> and lost. The <strong>blocking "
                     "probability</strong> is `π_K` and the <strong>admitted rate</strong> is "
                     "`λ(1 − π_K)`.",
                     "<strong>Balking</strong>: the same service but `λₙ = λ/(n + 1)`, so an "
                     "arrival who finds `n` already waiting joins with probability `1/(n + 1)`. "
                     "The rates now depend on the state, which is the one thing a closed form "
                     "cannot absorb.")),
            ("p", "The chain is built by the same function with the same two lists, stopped at "
                  "`K`. Nothing in the machinery is aware that the truncation has changed "
                  "meaning; what changes is what you are entitled to say about the answer. On an "
                  "unbounded queue the finite chain's figures come with an error term; here they "
                  "come with none."),
            ("h3", "Stability stops being a question"),
            ("math", [
                "λ = 6, μ = 5, K = 5        ρ = 6/5, which is at least 1 and does not matter",
                "",
                "   weights   1, 6/5, 36/25, 216/125, 1296/625, 7776/3125",
                "   π  =  3125/31031,  3750/31031,  4500/31031,",
                "         5400/31031,  6480/31031,  7776/31031",
                "",
                "   blocking  π₅ = 7776/31031 = 25.0588%",
                "   sysdesign_core.mm1k(6, 5, 5) gives 7776/31031 and L = 93750/31031",
                "   the two routes agree EXACTLY, fraction for fraction",
                "",
                "   L                          93750/31031  =  3.021172",
                "   admitted rate  λ(1 − π₅) = 139530/31031 =  4.496471   of 6",
                "   W  = L / admitted        =  3125/4651   =  0.671899",
                "   L / λ                    = 15625/31031  =  0.503529   ✗",
                "",
                "   the ratio of the two:  1 − π₅ = 23255/31031 = 0.749412",
            ]),
            ("p", "The distribution rises with `n` rather than falling, because every ratio is "
                  "`6/5`. On an unbounded chain that is a queue with no stationary distribution "
                  "at all; here it is a system that is usually nearly full, and the numbers are "
                  "the exact answers for that system. Nothing about `ρ` needs checking before "
                  "trusting them."),
            ("h3", "The two numbers people call W"),
            ("p", "`W` is `L` divided by a rate, and there are two candidates. Divide by the "
                  "admitted rate and you get the mean time in the system of the customers who "
                  "got in: `0.671899`. Divide by `λ` and you get `0.503529`, which is too small "
                  "by a factor of exactly `1 − π_K`, because it credits the system with serving "
                  "customers it never admitted. The lab prints both, one green and one red, in "
                  "the same row of the same table."),
            ("p", "The error is always in the same direction and it grows with the blocking, so "
                  "it is worst exactly where the system is most stressed and the answer matters "
                  "most. At `K = 1` on these rates the blocking is `54.545%` and the wrong "
                  "division is out by a factor of more than two; at `K = 12` on a load of four "
                  "fifths the blocking is `1.4543%` and it is out by about one and a half per "
                  "cent. There is no regime in which it is right and the system is interesting."),
            ("math", [
                "λ = 6, μ = 5: capacity against blocking, and the two divisions",
                "",
                "     K     blocking    admitted     L        W = L/admitted   L/λ  ✗",
                "     1      54.545%     2.72727   0.54545      0.20000       0.09091",
                "     2      39.560%     3.62637   1.12088      0.30909       0.18681",
                "     3      32.191%     4.06855   1.72578      0.42418       0.28763",
                "     4      27.865%     4.32810   2.35949      0.54516       0.39325",
                "     5      25.059%     4.49647   3.02117      0.67190       0.50353",
                "     6      23.119%     4.61288   3.70984      0.80423       0.61831",
                "     8      20.673%     4.75960   5.16358      1.08488       0.86060",
                "",
                "   more room buys throughput and costs waiting, in the same column pair",
            ]),
            ("p", "Read the table as a design trade and not as a limit. Every extra place raises "
                  "the admitted rate and raises `W` at the same time, because the customers who "
                  "used to be turned away are now waiting instead. Which of those you want is a "
                  "question about the system and not about the queue; what the model supplies is "
                  "both columns, exactly. &ldquo;Bounded Queues and Loss&rdquo; makes the same "
                  "trade from the closed forms."),
            ("example", ("The closed form agreeing exactly rather than nearly",
                         "`sysdesign_core.mm1k(6, 5, 5)` gives blocking `7776/31031` and "
                         "`L = 93750/31031`. The cut equations on the same rates give the same "
                         "two fractions.",
                         "That is a stronger check than the one the unbounded models could "
                         "offer. There the chain was finite and the formula was not, so the best "
                         "available was agreement to within the truncation. Here both describe "
                         "the same finite system, so the comparison is an equality of fractions "
                         "and the page reports it as exact.")),
            ("example", ("Arrivals that balk, where no closed form applies",
                         "Switch the chain to balking on the same rates: `λₙ = 6/(n + 1)`, so "
                         "the ratios are `6/5, 3/5, 2/5, 3/10, 6/25`. The distribution now falls "
                         "steeply: `π` runs from `15625/51799` down to `324/51799`, the blocking "
                         "is `0.6255%`, and `L` is `1.192494` against the blocking chain's "
                         "`3.021172`.",
                         "`mm1k` does not apply here at all &mdash; it assumes a constant "
                         "arrival rate &mdash; and the page says so rather than printing its "
                         "number beside a chain it does not describe. The cut equations needed "
                         "no change, because customers who decline to join are just a smaller "
                         "`λₙ`.")),
            ("p", "That contrast is the closing argument for the whole of this half. Four named "
                  "models and one homemade one have come out of a single equation applied "
                  "between neighbouring states, and the one the textbooks have no formula for "
                  "cost exactly as much work as the others."),
        ],
        "lab": ("birthdeath", {
            "mode": "finite",
            "preset": "buffer",
            "panel_title": "Set the capacity, or let arrivals balk instead",
            "panel_intro": "Truncation here is not an approximation: it is the model. Both W "
                           "values are printed side by side and labelled, because the wrong one "
                           "is the commonest error in a finite-queue calculation and it is "
                           "always too small. The balking chain is the case no closed form "
                           "covers and the cut equation handles without changing.",
        }),
        "steps_title": "Working with a bounded queue",
        "steps_intro": "Four steps. The third is the one that is usually skipped, and it is the reason a reported W is too small.",
        "steps": [
            ("Decide whether the wall is real",
             "A genuine limit on places means the finite chain is the model and owes no error "
             "term. A state count chosen because the computation had to stop somewhere means it "
             "is an approximation and owes one. The arithmetic is identical; what you may claim "
             "is not."),
            ("Stop worrying about ρ",
             "A queue that cannot grow cannot run away, so `ρ ≥ 1` is allowed and the "
             "distribution exists. `ρ` is now a fact about the shape of `π` &mdash; rising "
             "rather than falling &mdash; instead of a condition for `π` to exist."),
            ("Compute the blocking, then the admitted rate",
             "`π_K` is the fraction of time the system is full, so `λ(1 − π_K)` is the rate that "
             "actually enters. Write it down before reaching for `W`; once `λ` is in your hand "
             "the wrong division is the natural one."),
            ("Divide L by the admitted rate, and say which rate you used",
             "`W = L/λ(1 − π_K)`. Dividing by `λ` understates the answer by exactly the factor "
             "`1 − π_K`, which at a quarter blocked is a twenty-five per cent error in the "
             "wrong direction. Naming the rate in the report makes the mistake visible to a "
             "reader who did not make it."),
        ],
        "worked": {
            "title": "A buffer of five at a load above one, and the same system with balking instead",
            "intro": [
                "Arrivals at 6 per unit time, service at 5, and room for five in total. The load "
                "is above 1 and it does not matter. Then the same rates with a customer who "
                "sometimes declines to join.",
            ],
            "lines": [
                "hard wall at K = 5      λ = 6, μ = 5, ρ = 6/5",
                "",
                "   every cut ratio 6/5, so the weights RISE:",
                "      1, 6/5, 36/25, 216/125, 1296/625, 7776/3125",
                "   total 31031/3125",
                "",
                "   π   3125   3750   4500   5400   6480   7776       all over 31031",
                "       n=0    n=1    n=2    n=3    n=4    n=5",
                "",
                "   blocking π₅        7776/31031    =  25.0588%",
                "   mm1k(6, 5, 5)      7776/31031       identical",
                "   admitted rate      139530/31031  =   4.496471    of 6",
                "   L                   93750/31031  =   3.021172",
                "   mm1k L              93750/31031      identical",
                "",
                "   W  = L / admitted    3125/4651   =   0.671899    ✓",
                "   L / λ               15625/31031  =   0.503529    ✗  too small",
                "   ratio  1 − π₅       23255/31031  =   0.749412",
                "",
                "balking on the same rates      λₙ = 6/(n+1)",
                "",
                "   ratios   6/5, 3/5, 2/5, 3/10, 6/25",
                "   π  15625  18750  11250  4500  1350  324     all over 51799",
                "",
                "   blocking π₅         324/51799   =   0.6255%",
                "   admitted rate     180870/51799  =   3.491766",
                "   L                  61770/51799  =   1.192494",
                "   W  = L / admitted    2059/6029  =   0.341516",
                "   mm1k does not apply: it assumes a constant arrival rate",
            ],
            "after": [
                "Compare the two distributions rather than the two summaries. The blocking chain "
                "puts its mass at the top, because every ratio is above 1 and the only thing "
                "stopping it is the wall. The balking chain puts its mass at the bottom, because "
                "the ratios fall away after the first one: `6/5`, then `3/5`, then `2/5`. Same "
                "service, same nominal arrival rate, completely different systems.",
                "The admitted rates are the surprising pair. Balking admits `3.49` per unit time "
                "against the wall's `4.50`, even though it blocks almost nobody: turning "
                "customers away gently and often admits less than turning them away brutally and "
                "rarely. That is the kind of comparison a table of blocking probabilities cannot "
                "make, and it is one subtraction away once you have both distributions.",
                "The `L/λ` column is there to be wrong. `0.503529` against `0.671899` is a "
                "twenty-five per cent understatement, exactly the blocking fraction, and it is "
                "the number a calculation that reached for `λ` out of habit would report. It is "
                "not a rounding and it does not average out.",
                "For a rehearsal, hold `λ = 6` and `μ = 5` and raise `K` from 5 to 8. The "
                "supplied first move is that the blocking falls from `25.059%` to `20.673%`. "
                "Predict the direction of `W` before checking, and then say why both `W` and the "
                "admitted rate went up, which sounds contradictory and is not.",
            ],
        },
        "quiz_title": "Walls, blocking and the right divisor",
        "quiz": [
            {"q": "On an M/M/1/K queue with `ρ = 6/5`, what does the load above 1 tell you?",
             "a": ["That there is no stationary distribution",
                   "That the chain must be truncated further",
                   "Nothing about existence: a queue that cannot grow cannot run away, so π exists and simply rises with n",
                   "That the blocking probability must be 100%"],
             "c": 2,
             "why": "The stability condition belongs to the unbounded model. With a hard limit "
                    "the chain is finite, the weights always normalise, and `ρ` describes the "
                    "shape of `π` rather than whether it exists. Here it makes the distribution "
                    "rise, and the system is full a quarter of the time."},
            {"q": "`L = 3.021172` and `λ = 6`, with blocking `25.0588%`. What is `W`?",
             "a": ["`3.021172/6 = 0.503529`",
                   "`3.021172/4.496471 = 0.671899`, dividing by the admitted rate",
                   "`3.021172 × 6 = 18.13`",
                   "It cannot be computed without the service time"],
             "c": 1,
             "why": "Little's Law relates the number in the system to the rate that actually "
                    "enters it. Blocked arrivals never entered, so they do not belong in the "
                    "divisor. Dividing by `λ` understates `W` by exactly `1 − π_K`, which is a "
                    "quarter here."},
            {"q": "Why does the page refuse to print `mm1k`'s answer beside the balking chain?",
             "a": ["Because `mm1k` is only defined for `ρ < 1`",
                   "Because `mm1k` assumes a constant arrival rate, and a balking chain has `λₙ = λ/(n+1)`",
                   "Because the balking chain has no stationary distribution",
                   "Because the two use different service rates"],
             "c": 1,
             "why": "The closed form describes a different model. Printing its number in the "
                    "same table would invite a comparison that means nothing. The cut equations "
                    "need no change for balking, which is the reason this course builds queues "
                    "from them rather than from a table of formulas."},
            {"q": "Raising `K` from 5 to 8 on the same rates lowers the blocking and raises both `W` and the admitted rate. Why is that not a contradiction?",
             "a": ["It is: one of the figures must be wrong",
                   "Because customers who used to be turned away now wait instead, so more get in and the average time in the system rises",
                   "Because `W` is measured in different units at different `K`",
                   "Because `L` is unchanged"],
             "c": 1,
             "why": "More room converts rejections into waiting. Throughput goes up because "
                    "fewer arrivals are lost; the time in the system goes up because the extra "
                    "customers are queueing. Both columns move together and which one you want "
                    "is a design question."},
        ],
        "mistakes": [
            ("Dividing L by λ on a lossy system",
             "The result is too small by exactly `1 − π_K`, always in the same direction, and "
             "worst where the blocking is highest and the answer matters most. The correct "
             "divisor is `λ(1 − π_K)`, and it costs one multiplication once `π_K` is in hand."),
            ("Carrying the stability condition into a bounded model",
             "`ρ < 1` is a condition for an unbounded queue to have a stationary distribution. "
             "With a wall there is nothing to check: the chain is finite and always normalises. "
             "Refusing to model a system because its nominal load exceeds 1 rejects exactly the "
             "systems a buffer exists for."),
            ("Reaching for a closed form on a chain whose rates vary",
             "`mm1k` assumes a constant `λ`. A balking queue, a finite population of machines, a "
             "server that speeds up under load: none of them is covered, and all of them are one "
             "rate list away from an exact answer through the cut equations. The formula is the "
             "special case, not the tool."),
        ],
        "standard": ("Finish when a bounded queue is easier for you than an unbounded one, and you never divide by λ without asking.",
                     "You should be able to build the stopped chain, say why `ρ ≥ 1` is "
                     "permitted, compute the blocking as `π_K` and the admitted rate as "
                     "`λ(1 − π_K)`, produce both candidate `W` values and name which one you "
                     "used, and model a balking arrival stream without reaching for a formula "
                     "that does not cover it."),
        "note": 'Every model here has assumed Poisson arrivals without saying what that means or where they come from. The last of this material builds them: n independent opportunities in one unit of time, each firing with probability λ/n, which is an exact binomial. Its limit as n grows is the Poisson distribution, and that is where this course stops being exact — `e^(−λ)` is irrational. &ldquo;The Poisson Limit, and Where Exactness Stops&rdquo; prints the difference rather than describing it.',
    },

    # ---------------------------------------------------------------- 10
    {
        "slug": "the-poisson-limit-and-where-exactness-stops",
        "title": "The Poisson Limit, and Where Exactness Stops",
        "module": "The arrival process",
        "one_line": "n chances at λ/n each is an exact binomial; its limit carries e^(−λ), which is irrational, and the page prints the gap.",
        "summary": (
            "Every queue on this course has assumed Poisson arrivals. Here is where they come "
            "from: cut one unit of time into n independent opportunities, each an arrival with "
            "probability `λ/n`. The count is <strong>binomial</strong> and that is exact rational "
            "arithmetic &mdash; at `n = 40` the entries are fractions over sixty-five-digit "
            "denominators. Its limit as n grows is the Poisson distribution, and that is "
            "<strong>not</strong> exact and cannot be, because every entry carries a factor of "
            "`e^(−λ)`, which is irrational for every rational `λ` other than 0. The exact column "
            "and the rounded column sit side by side and the difference between them is printed: "
            "on the worked numbers, `8.866e-3` at `k = 3`."
        ),
        "key": [
            "n opportunities, each firing with probability λ/n — the count is binomial, exactly",
            "P(k+1) = P(k) · ((n−k)/(k+1)) · p/(1−p)   from P(0) = (1−p)ⁿ:  the shipped recurrence",
            "the limit is e^(−λ)λᵏ/k!, and e^(−λ) is irrational for every rational λ but 0",
            "λ = 3, n = 40:  the two columns differ by at most 8.866e-3, at k = 3",
            "variance λ(1 − λ/n) = 111/40, short of the mean 3 by exactly λ²/n = 9/40",
            "as n rises the largest gap runs 5.759e-2, 1.879e-2, 7.015e-3, 2.850e-3, 8.446e-4",
        ],
        "key_label": "An exact binomial, an irrational limit, and the measured distance between them",
        "concepts_intro": (
            "Three ideas. The first builds the arrival process, the second says exactly where "
            "the exactness stops, and the third gives the limit a name in terms of a quantity "
            "you can compute."
        ),
        "concepts": [
            ("Poisson arrivals are a limit of something countable",
             "Split a unit of time into n slots and let each hold an arrival with probability "
             "`λ/n`, independently. The number of arrivals is `Binomial(n, λ/n)`, whose mean is "
             "`λ` whatever n is. Letting n grow while holding the mean fixed is what the Poisson "
             "distribution is, and the whole content of the word &ldquo;limit&rdquo; is how far "
             "apart the two are at a given n."),
            ("One quantity on this page is irrational, and it says so",
             "`e^(−λ)` is irrational for every rational `λ` other than 0, so the Poisson column "
             "cannot be a fraction. It is computed by `expNegApprox`, shared with the System "
             "Design path, as the reciprocal of the positive-term series for `e^λ` &mdash; every "
             "term the same sign, so nothing cancels &mdash; and it is correct to the rounding "
             "of a double. The page names the function, names the method, and prints the "
             "difference from the exact column beside it."),
            ("The variance gives the gap a name",
             "The Poisson signature is that the variance equals the mean. The binomial's "
             "variance is `λ(1 − λ/n)`, short of `λ` by exactly `λ²/n`. At `λ = 3` and `n = 40` "
             "that is `111/40` against `3`, short by `9/40`. So the distance to the limit is not "
             "a vague closeness; it is a fraction, it is printed, and it is what a window of "
             "finitely many opportunities costs."),
        ],
        "read_title": "Where the arrivals come from, and where the exactness stops",
        "read_intro": "The Bernoulli construction, the exact binomial and the recurrence that makes it computable, the limit, the irrational factor, and the variance gap.",
        "body": [
            ("def", ("The Bernoulli construction and the Poisson limit",
                     "Divide one unit of time into `n` independent opportunities, each producing "
                     "an arrival with probability `p = λ/n`. The number of arrivals is "
                     "`Binomial(n, p)`, with mean `np = λ` and variance `np(1 − p) = "
                     "λ(1 − λ/n)`.",
                     "As `n → ∞` with `λ` fixed, `P(k) → e^(−λ)λᵏ/k!`, the "
                     "<strong>Poisson</strong> distribution with mean `λ`. Its variance is `λ`, "
                     "equal to its mean.")),
            ("p", "That construction is the reason Poisson arrivals are a sensible default and "
                  "not a convenience. Many small independent chances of something happening, "
                  "none of them individually likely, adding up to a fixed expected number: that "
                  "is the shape of a great many arrival processes, and the limit says the count "
                  "does not depend on how the time was sliced."),
            ("h3", "The exact column, and the recurrence that makes it computable"),
            ("p", "The binomial probabilities are computed as exact fractions, but not from "
                  "`C(n, k) pᵏ(1 − p)^(n−k)` term by term: at `n = 1000` the closed form's "
                  "denominator per term runs to two thousand digits and the page never paints. "
                  "The kit uses the same recurrence the System Design path uses for the same "
                  "job, `P(k+1) = P(k) · ((n − k)/(k + 1)) · p/(1 − p)` starting from "
                  "`P(0) = (1 − p)ⁿ`, and `scripts/mathcheck.js` holds the two implementations "
                  "against each other on the same inputs so that the Subjects cannot drift "
                  "apart about a binomial."),
            ("math", [
                "λ = 3, n = 40, so p = 3/40",
                "",
                "     k     binomial, exactly    Poisson, rounded     difference    denominator",
                "     0        0.044225149         0.049787068        −5.562e-3      65 digits",
                "     1        0.143432917         0.149361205        −5.928e-3      63",
                "     2        0.226779072         0.224041808         2.737e-3      63",
                "     3        0.232908236         0.224041808         8.866e-3      63",
                "     4        0.174681177         0.168031356         6.650e-3      64",
                "     5        0.101976038         0.100818813         1.157e-3      64",
                "     6        0.048231910         0.050409407        −2.177e-3      63",
                "     7        0.018994806         0.021604031        −2.609e-3      63",
                "     8        0.006352993         0.008101512        −1.749e-3      64",
                "",
                "   largest difference 8.866e-3, at k = 3",
                "   P(0) exactly = (1 − 3/40)⁴⁰ = (37/40)⁴⁰, a fraction over 65 digits",
            ]),
            ("p", "The left column is exact rational arithmetic and has no caveat attached to "
                  "it. The right column is not exact and cannot be. Every Poisson entry carries "
                  "a factor of `e^(−λ)`, which is irrational whenever `λ` is a nonzero rational, "
                  "so no amount of care makes that column a fraction. What the page can do, and "
                  "does, is name the function that produced it, name the method, and print the "
                  "difference rather than describing it."),
            ("p", "`expNegApprox` is worth a sentence on its own. It is the reciprocal of a "
                  "positive-term series for `e^λ`, which matters: the alternating series for "
                  "`e^(−λ)` suffers catastrophic cancellation at moderate `λ`, where large terms "
                  "of opposite sign subtract to leave a small answer, and the result can lose "
                  "most of its digits. Summing positive terms and inverting at the end has no "
                  "cancellation anywhere, so the answer is right to the rounding of a double "
                  "&mdash; about sixteen significant figures, and at `λ = 3` it differs from the "
                  "platform's own exponential by `1.4e-17`."),
            ("h3", "The word limit, as a measurement"),
            ("math", [
                "λ = 3 throughout; only the number of opportunities changes",
                "",
                "      n      p = λ/n     P(0) exactly      largest gap    variance   short by",
                "      8        3/8       0.023283064        5.759e-2       15/8        9/8",
                "     20       3/20       0.038759531        1.879e-2       51/20       9/20",
                "     40       3/40       0.044225149        8.866e-3      111/40       9/40",
                "     50       3/50       0.045330727        7.015e-3      141/50       9/50",
                "    120       1/40       0.047924091        2.850e-3      117/40       3/40",
                "    400      3/400       0.049227318        8.446e-4     1191/400      9/400",
                "",
                "   the Poisson value of P(0) is e⁻³ = 0.049787068…, irrational",
                "   at n = 400 the exact P(0) is a fraction over a 1041-digit denominator",
            ]),
            ("p", "Two columns of that table say the same thing in different currencies. The "
                  "largest gap falls roughly like `1/n`, and the variance shortfall `λ²/n` falls "
                  "exactly like `1/n`; the second is an exact fraction and the first is a "
                  "measurement in doubles. Either way &ldquo;the binomial tends to the "
                  "Poisson&rdquo; has a size attached to it at every n, and at `n = 8` that size "
                  "is nearly six per cent."),
            ("p", "The last line is the other half of the exactness story. Pushing n up makes "
                  "the approximation better and the exact column more expensive: at four hundred "
                  "opportunities `P(0)` is a fraction whose denominator has a thousand and "
                  "forty-one digits, carried whole. That is the trade this library makes "
                  "deliberately, and it is why the recurrence rather than the closed form is "
                  "what ships."),
            ("example", ("A small n that is visibly not Poisson",
                         "Set `λ = 8` with only twenty opportunities, so `p = 2/5`. The exact "
                         "`P(0)` is `0.000036562` against the Poisson's `0.000335463`, an order "
                         "of magnitude out, and the largest difference across the table is "
                         "`4.012e-2` at `k = 8`.",
                         "With `p = 2/5` the individual chances are not small and the "
                         "construction's premise has gone. The variance is `24/5` against a mean "
                         "of `8`, short by `16/5`, so the binomial here is far tighter than any "
                         "Poisson distribution and the shapes genuinely differ. The limit is a "
                         "statement about large n and small p together.")),
            ("example", ("A rate below one, where two entries are nearly everything",
                         "At `λ = 1/2` with twenty opportunities, `P(0) = 0.602687680` and "
                         "`P(1) = 0.309070605`, so more than ninety-one per cent of the mass is "
                         "in the first two counts. The largest gap to the Poisson column is "
                         "`5.805e-3` at `k = 1`.",
                         "This is the regime most arrival models live in per unit of time, and "
                         "it is the one where the approximation is best and matters least: the "
                         "shape is nearly all in the head of the distribution, and both columns "
                         "agree about where the head is.")),
            ("p", "Every arrival process in the rest of this course is Poisson, which is why "
                  "this is the page that says where the exactness stops. The cut equations, the "
                  "balance systems, the steady states, the fundamental matrices and the policy "
                  "values are all exact fractions; `e^(−λ)` is the one quantity on this half of "
                  "the course that is not, and the footer of this Subject names it in public "
                  "alongside the other three."),
        ],
        "lab": ("birthdeath", {
            "mode": "poisson",
            "preset": "three",
            "panel_title": "Slide the number of opportunities and watch the limit arrive",
            "panel_intro": "The exact column is a binomial in rational arithmetic, with "
                           "denominators running to sixty-five digits on the default view and "
                           "past a thousand at the top of the slider. The column beside it is "
                           "the Poisson limit, which cannot be exact because e^(−λ) is "
                           "irrational, and the page prints the difference between them at every "
                           "count.",
        }),
        "steps_title": "Using a Poisson model without overstating it",
        "steps_intro": "Four steps. The second and the fourth are about saying what kind of number you are holding.",
        "steps": [
            ("Say what one opportunity is before choosing a distribution",
             "The construction needs many independent chances, each unlikely, in the window you "
             "are counting over. If the chances are few or large &mdash; twenty slots at `2/5` "
             "each &mdash; the count is binomial and the Poisson shape is genuinely different, "
             "not merely approximated."),
            ("Compute the exact binomial when you can",
             "One recurrence from `(1 − p)ⁿ` gives every term as a fraction and costs one "
             "multiplication each. It is exact, it has no caveat, and it lets the approximation "
             "be measured instead of assumed."),
            ("Check the variance against the mean",
             "The Poisson has them equal. The binomial's variance is short by `λ²/n`, which is "
             "an exact fraction and is the cheapest single number describing how far from "
             "Poisson your window is. At `λ = 3` and `n = 8` it is `9/8`, more than a third of "
             "the mean."),
            ("Label every quantity that carries e^(−λ) as rounded, and say how",
             "&ldquo;Correct to the rounding of a double, from a positive-term series&rdquo; is "
             "a claim a reader can evaluate. &ldquo;Approximately&rdquo; is not. Everything else "
             "on this course is exact, and that distinction is only load-bearing if the word is "
             "reserved for the places it belongs."),
        ],
        "worked": {
            "title": "Three arrivals a second, from forty chances, and the same mean from eight to four hundred",
            "intro": [
                "One unit of time, `n` independent opportunities, each an arrival with "
                "probability `3/n`. The mean is 3 in every row. Only the slicing changes.",
            ],
            "lines": [
                "n = 40, p = 3/40        P(0) = (37/40)⁴⁰, exactly",
                "",
                "     k    binomial exact   Poisson rounded    difference",
                "     0      0.044225149      0.049787068      −5.562e-3",
                "     1      0.143432917      0.149361205      −5.928e-3",
                "     2      0.226779072      0.224041808       2.737e-3",
                "     3      0.232908236      0.224041808       8.866e-3     ← largest",
                "     4      0.174681177      0.168031356       6.650e-3",
                "     5      0.101976038      0.100818813       1.157e-3",
                "     6      0.048231910      0.050409407      −2.177e-3",
                "     7      0.018994806      0.021604031      −2.609e-3",
                "     8      0.006352993      0.008101512      −1.749e-3",
                "",
                "   variance   λ(1 − λ/n) = 3(1 − 3/40) = 111/40 = 2.775",
                "   mean       3            short by exactly λ²/n = 9/40 = 0.225",
                "",
                "the same mean, sliced more finely",
                "",
                "      n      p        largest gap     variance    short by   P(0) denominator",
                "      8     3/8        5.759e-2        15/8        9/8",
                "     20     3/20       1.879e-2        51/20       9/20",
                "     40     3/40       8.866e-3       111/40       9/40         65 digits",
                "     50     3/50       7.015e-3       141/50       9/50",
                "    120     1/40       2.850e-3       117/40       3/40",
                "    400    3/400       8.446e-4      1191/400      9/400      1041 digits",
                "",
                "   Poisson P(0) = e⁻³ = 0.049787068…, and e⁻³ is irrational",
                "   expNegApprox(3) differs from the platform exponential by 1.4e-17",
            ],
            "after": [
                "The signs in the difference column are worth reading rather than skipping. The "
                "binomial is below the Poisson at `k = 0` and `k = 1`, above it at `k = 2` "
                "through `k = 5`, and below again from `k = 6`. That is the tighter variance "
                "showing: mass has been pulled out of both ends and into the middle, and the "
                "single number `λ²/n = 9/40` is what the pulling amounts to.",
                "The second block is the word &ldquo;limit&rdquo; turned into a table. Eight "
                "slices gives a largest error of nearly six per cent; four hundred gives eight "
                "parts in ten thousand. Nothing about the sequence is mysterious and nothing "
                "about it requires a limit theorem to describe at a fixed n &mdash; the "
                "shortfall in variance is `9/n`, exactly, at every row.",
                "And the price of the exact column is in the last entry. At four hundred "
                "opportunities the exact `P(0)` has a denominator of a thousand and forty-one "
                "digits. It is carried whole, the Poisson column beside it is a double, and the "
                "page is explicit about which is which. That is the arrangement this whole "
                "Subject is built on: exact everywhere it can be, labelled everywhere it cannot.",
                "For a rehearsal, set `λ = 1/2` and predict the largest gap at `n = 20` before "
                "looking. The supplied first move is that the variance shortfall is "
                "`λ²/n = 1/80`, one fortieth of the mean, against `9/40 / 3 = 3/40` in the "
                "worked case. Say whether you expect the gap to be larger or smaller than "
                "`8.866e-3`, and then check the `5.805e-3` the page reports at `k = 1`.",
            ],
        },
        "quiz_title": "Binomial, limit and what is rounded",
        "quiz": [
            {"q": "Which quantity on this page is not exact, and why?",
             "a": ["The binomial probabilities, because they involve large powers",
                   "The Poisson probabilities, because every one carries a factor of `e^(−λ)`, which is irrational for rational λ other than 0",
                   "The variance, because it is a difference of two large numbers",
                   "Nothing: the whole page is exact rational arithmetic"],
             "c": 1,
             "why": "The binomial column is exact rational arithmetic with denominators of "
                    "sixty-five digits at the worked setting. The Poisson column cannot be a "
                    "fraction at all. It is computed by `expNegApprox` as the reciprocal of a "
                    "positive-term series, and the page names the function and prints the "
                    "difference."},
            {"q": "Why is `e^(−λ)` computed as the reciprocal of a series for `e^λ` rather than by summing the series for `e^(−λ)` directly?",
             "a": ["Because the second series does not converge",
                   "Because the alternating series for `e^(−λ)` cancels large terms of opposite sign and loses digits, while a positive-term series cancels nothing",
                   "Because reciprocals are cheaper than additions",
                   "Because the two series have different limits"],
             "c": 1,
             "why": "At moderate `λ` the alternating series has terms far larger than the answer, "
                    "and subtracting them destroys precision. Summing `e^λ` involves only "
                    "positive terms, so no cancellation occurs, and one division at the end "
                    "gives a result good to the rounding of a double."},
            {"q": "At `λ = 3` and `n = 40` the binomial variance is `111/40` against a mean of `3`. What is the shortfall `9/40`?",
             "a": ["A rounding error", "Exactly `λ²/n`, the price of using finitely many opportunities",
                   "The difference between the two columns at `k = 0`",
                   "The probability of more than eight arrivals"],
             "c": 1,
             "why": "`np(1 − p) = λ(1 − λ/n) = λ − λ²/n`. The Poisson signature is variance "
                    "equal to mean, and `λ²/n` is exactly what a finite window costs. It is an "
                    "exact fraction, it falls like `1/n`, and it is the cheapest single "
                    "description of how far from Poisson a given slicing is."},
            {"q": "With `λ = 8` and only twenty opportunities, the exact `P(0)` is about a tenth of the Poisson value. What has gone wrong?",
             "a": ["Nothing has gone wrong: `p = 2/5` is not small, so the construction's premise fails and the two distributions genuinely differ",
                   "The exact computation has overflowed",
                   "`λ` must be less than 1 for the binomial to be defined",
                   "The recurrence is inaccurate at small `k`"],
             "c": 0,
             "why": "The Poisson limit needs many opportunities each unlikely. At `p = 2/5` with "
                    "twenty slots neither holds, the binomial variance is `24/5` against a mean "
                    "of `8`, and the shapes are different rather than nearly the same. The "
                    "largest gap across the table is `4.012e-2`."},
        ],
        "mistakes": [
            ("Calling the Poisson column approximate without saying how",
             "&ldquo;Approximately&rdquo; is not a claim a reader can check. &ldquo;`e^(−λ)` is "
             "irrational, so this column is computed by `expNegApprox` as the reciprocal of a "
             "positive-term series and is correct to the rounding of a double&rdquo; is. Every "
             "other figure on this course is exact, and the distinction only carries weight if "
             "the word is reserved."),
            ("Using the Poisson shape when the per-slot chance is not small",
             "Twenty opportunities at `2/5` each has the right mean and the wrong shape: the "
             "variance is short of the mean by `16/5` and `P(0)` is out by an order of "
             "magnitude. The limit needs large n and small p together, and the variance "
             "shortfall `λ²/n` is the one-number test."),
            ("Pushing n up to make the exact column agree, without noticing what it costs",
             "At four hundred opportunities the exact `P(0)` has a thousand-and-forty-one-digit "
             "denominator. The approximation improves like `1/n` and the exact representation "
             "grows like n, so &ldquo;just use more slots&rdquo; is a trade rather than a fix, "
             "and it is worth making deliberately."),
        ],
        "standard": ("Finish when you can say, of any number on this course, whether it is exact and why — and produce the one that is not.",
                     "You should be able to build the Bernoulli construction and identify the "
                     "count as binomial, compute its terms exactly from the recurrence, state "
                     "the Poisson limit and name `e^(−λ)` as the irrational factor that makes it "
                     "unrepresentable, quote the variance shortfall `λ²/n` as the distance to "
                     "the limit, and describe how `expNegApprox` avoids cancellation."),
        "note": 'That closes the course and the Operations Research path’s exact half. Everything here was solved: a steady state by elimination, an expected time by an inverse that is really a series, a queue by one equation applied between neighbours, and the only rounded quantity named in public. &ldquo;Simulation and Variance Reduction&rdquo; is what is left when none of those applies, and it runs the same slotted queue this material solves exactly &mdash; measuring its own answers against the ones computed here rather than against themselves.',
    },
]
