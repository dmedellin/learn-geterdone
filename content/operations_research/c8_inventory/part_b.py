"""Inventory Models -- the last three lessons: demand that is a distribution.

The deterministic half chose a quantity against a rate. These three choose a
quantity, a reorder point and a base-stock level against a random variable, and
the arithmetic stays exact throughout: the distributions are rational, the
convolutions are rational, and the service levels are fractions printed as
percentages rather than percentages standing in for fractions.

The middle lesson carries this course's best misconception. Cycle service and
fill rate are two different numbers computed from one policy, they are both
routinely called "service level", and on the worked instance they are 68.75%
and 99.625%.

Every figure below is READ OFF scripts/mathpath/labs/inventory.py by extracting
its shipped JavaScript with the regex scripts/mathcheck.js uses and executing
it under node. Where the plan and the kit disagreed, the kit won.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-newsvendor-and-the-critical-ratio",
        "title": "The Newsvendor and the Critical Ratio",
        "module": "One order, one season",
        "one_line": "One order, one season, no second chance: the quantity to stop at is where the cumulative probability first reaches the ratio of the two unit costs.",
        "summary": (
            "Order once for a season whose demand is a random variable, and the decision "
            "is a balance between two unit costs: `cᵤ` for every unit short and `cₒ` for "
            "every unit left. The rule is the <strong>critical ratio</strong> "
            "`cᵤ/(cᵤ + cₒ)`, and the answer is the smallest quantity whose cumulative "
            "probability reaches it. The ratio is a probability, not a quantity, which is "
            "the single most useful thing to know about it &mdash; and the panel tabulates "
            "the whole expected-cost curve beside the rule so that the rule is checked "
            "rather than applied."
        ),
        "key": [
            "one order, one season: what is unsold is lost and what is short cannot be reordered",
            "underage cᵤ per unit short,  overage cₒ per unit left over",
            "critical ratio  cᵤ/(cᵤ + cₒ)  —  a PROBABILITY the CDF has to reach, not a quantity",
            "order the smallest Q with  P(D ≤ Q) ≥ cᵤ/(cᵤ + cₒ)",
            "cᵤ = 7, cₒ = 3 ⟹ ratio 7/10;  on 0…4 with 1,2,3,3,1 tenths the CDF reaches it at Q = 3",
            "expected cost there 37/10, against 47/10 at Q = 2 and 57/10 at Q = 4",
        ],
        "key_label": "Two unit costs, one probability, and the quantity it picks",
        "concepts_intro": (
            "Three ideas. The first is what makes this model different from every earlier "
            "one on the course, the second is the rule, and the third is the reading of the "
            "rule that stops it being misused."
        ),
        "concepts": [
            ("There is no cycle, so there is no ordering cost to trade off",
             "Every earlier model on this course repeats: order, deplete, order again, and "
             "the fixed cost `K` is what stops the batches being tiny. Here there is one "
             "order and one season. Nothing repeats, `K` is paid once whatever is decided "
             "and drops out of the comparison, and what is traded off instead is the cost "
             "of a unit that was not there against the cost of a unit that was not "
             "wanted."),
            ("The expected cost is a sum over the distribution, and it has one minimum",
             "Order `Q` and, for each possible demand `d`, you are left with `Q − d` units "
             "if `d` is below `Q` and short by `d − Q` if it is above. Weighting those by "
             "their probabilities gives `cₒ·E[over] + cᵤ·E[under]`, a sum of finitely many "
             "rational terms. Raising `Q` by one buys one more unit of protection at "
             "expected benefit `cᵤ·P(D > Q)` and expected cost `cₒ·P(D ≤ Q)`, so it is "
             "worth doing exactly while `P(D ≤ Q)` is below the critical ratio."),
            ("The ratio is a probability, and reading it as a quantity is the standard error",
             "`cᵤ/(cᵤ + cₒ) = 7/10` does not mean order seven tenths of something. It means "
             "&ldquo;be willing to have stock left over 70% of the time&rdquo;, and the "
             "order quantity is whatever level of demand that corresponds to on this "
             "distribution. Change the distribution and keep the costs and the ratio is "
             "unchanged while the quantity moves; that is the clearest evidence of what "
             "kind of object it is."),
        ],
        "read_title": "One decision, one season, and the probability that settles it",
        "read_intro": "The costs, the expected-cost sum, the rule, and the three instances that show what the ratio is doing.",
        "body": [
            ("def", ("The newsvendor problem",
                     "Demand `D` for a single season is a random variable with a known "
                     "distribution. A quantity `Q` is ordered before the season and cannot "
                     "be changed. Each unit short costs `cᵤ`, the "
                     "<strong>underage</strong> cost; each unit left over costs `cₒ`, the "
                     "<strong>overage</strong> cost.",
                     "The expected cost is "
                     "`C(Q) = cₒ·E[(Q − D)⁺] + cᵤ·E[(D − Q)⁺]`, and the problem is to "
                     "choose `Q` to minimise it.")),
            ("p", "Both costs are usually margins rather than prices. If a unit is bought "
                  "for 3 and sold for 10, the overage cost is the 3 that was spent and not "
                  "recovered, and the underage cost is the 7 of margin that was not earned. "
                  "Working out which is which is most of the modelling; once they are "
                  "numbers, the rest is one comparison."),
            ("thm", ("The critical ratio",
                     "The optimal order quantity is the smallest `Q` with "
                     "`P(D ≤ Q) ≥ cᵤ/(cᵤ + cₒ)`.",
                     "Raising the order from `Q` to `Q + 1` saves `cᵤ` whenever demand "
                     "exceeds `Q`, which happens with probability `1 − P(D ≤ Q)`, and "
                     "costs `cₒ` otherwise. The change in expected cost is therefore "
                     "`cₒ·P(D ≤ Q) − cᵤ·(1 − P(D ≤ Q))`, which is negative exactly while "
                     "`P(D ≤ Q)` is below the ratio.")),
            ("p", "The steps are of decreasing benefit and then of increasing cost, so the "
                  "expected-cost curve falls and then rises with one minimum, and the first "
                  "quantity at which the cumulative distribution reaches the ratio is it. "
                  "Nothing in that argument needs the distribution to have any particular "
                  "shape, and nothing needs it to be continuous."),
            ("math", [
                "demand 0,1,2,3,4 with probabilities 1/10, 2/10, 3/10, 3/10, 1/10",
                "underage cᵤ = 7,   overage cₒ = 3,   ratio  7/(7+3) = 7/10",
                "",
                "   Q    P(D ≤ Q)   E[left over]   E[short]    expected cost",
                "",
                "   0      1/10          0           21/10        147/10",
                "   1      3/10        1/10            6/5         87/10",
                "   2      3/5         2/5             1/2         47/10",
                "   3      9/10  ✓       1             1/10         37/10     the minimum",
                "   4      1          19/10             0           57/10",
                "   5      1          29/10             0           87/10",
                "   6      1          39/10             0          117/10",
                "",
                "the CDF first reaches 7/10 at Q = 3, and 37/10 is the cheapest row",
            ]),
            ("p", "The window runs past the top of the demand distribution on purpose. A "
                  "reader's first instinct is to try ordering nothing and to try ordering "
                  "more than demand could ever be, and both are priced here: `Q = 6` costs "
                  "`117/10` and never runs short, `Q = 0` costs `147/10` and never has "
                  "anything left. &ldquo;The crossing is the minimum&rdquo; is then a "
                  "statement about the whole line rather than about the five points where "
                  "demand has mass."),
            ("p", "Every figure on that table is exact. Expectations over a finite "
                  "distribution with rational probabilities are ratios of whole numbers, "
                  "there is no square root anywhere in this model, and nothing on the page "
                  "rounds &mdash; which is worth saying explicitly, because the two "
                  "quantities this course does round, the economic order quantity and its "
                  "cost, are the headline of the lessons before it."),
            ("h3", "Moving the ratio, and watching the quantity follow"),
            ("example", ("Overage dominating: a bakery",
                         "Demand `8` to `12` with probabilities `1/8, 1/4, 1/4, 1/4, 1/8`, "
                         "underage `2`, overage `5`. The ratio is `2/7 ≈ 28.6%`, and the "
                         "cumulative distribution reaches it at `Q = 9` for an expected "
                         "cost of `23/8`.",
                         "The mean demand is exactly `10` and the order is `9`. When "
                         "leftovers cost more than shortages, the right answer is to order "
                         "<em>below</em> the mean and be short some of the time on "
                         "purpose &mdash; which is the clearest possible demonstration "
                         "that the mean is not the answer.")),
            ("example", ("Underage dominating: a spare part",
                         "Demand `0` to `4` with probabilities `1/2, 1/4, 1/8, 1/16, 1/16`, "
                         "underage `20`, overage `1`. The ratio is `20/21 ≈ 95.2%`, and the "
                         "cumulative distribution does not reach it until the very top of "
                         "the support: `Q = 4`, costing `49/16`.",
                         "Mean demand is `15/16`, less than one unit, and the order is "
                         "four. A stockout costing twenty times a leftover pushes the "
                         "order to cover the whole of the distribution, and the wide window "
                         "confirms that `5` and `6` are dearer &mdash; `65/16` and "
                         "`81/16` &mdash; so the answer really is the top of the support "
                         "rather than a runaway.")),
            ("p", "Three instances, three ratios, three answers relative to the mean: above "
                  "it, below it, and far above it. Nothing about the distributions "
                  "explains that pattern and everything about the two unit costs does, "
                  "which is the whole content of the rule."),
            ("h3", "Checking the rule instead of applying it"),
            ("p", "The panel computes the answer twice. Once by the critical ratio, walking "
                  "the cumulative distribution until it reaches the threshold; and once by "
                  "tabulating the expected cost at every whole quantity in the window and "
                  "taking the cheapest. It then prints whether the two agree, and says so "
                  "in red if they do not. They agree on all three worked instances."),
            ("p", "That is a habit worth carrying rather than a feature of this page. A "
                  "rule derived by an argument about one step at a time is exactly the kind "
                  "of rule that is right in general and mis-stated in a particular "
                  "textbook &mdash; with `≥` written as `>`, or the ratio inverted &mdash; "
                  "and a tabulation of the objective is the cheapest possible refutation. "
                  "The panel also refuses a distribution whose probabilities do not sum to "
                  "one, rather than rescaling it: a distribution that does not sum to one "
                  "is a typo, and normalising it silently answers a question nobody asked."),
        ],
        "lab": ("inventory", {
            "mode": "newsvendor",
            "preset": "papers",
            "panel_title": "Set the distribution and the two unit costs",
            "panel_intro": "The bars are the demand distribution with the chosen order "
                           "quantity marked and the outcomes that would run you short "
                           "shaded. Beneath them is the expected cost at every whole "
                           "quantity in a window wider than the demand, so that ordering "
                           "nothing and ordering more than demand can ever be are both "
                           "priced. The rule and the curve are computed separately and the "
                           "panel reports whether they agree.",
        }),
        "steps_title": "Working a single-season order",
        "steps_intro": "Four steps. The first is the modelling and it is where the mistakes are; the rest is arithmetic.",
        "steps": [
            ("Name the two unit costs, and say which is which out loud",
             "`cᵤ` is what one unit of unmet demand costs &mdash; usually lost margin, "
             "sometimes a penalty. `cₒ` is what one unsold unit costs &mdash; usually the "
             "purchase price less any salvage. Swapping them inverts the ratio and "
             "produces a confidently wrong answer in the opposite direction, which no "
             "later arithmetic will reveal."),
            ("Form the ratio and read it as a probability",
             "`cᵤ/(cᵤ + cₒ)` is between zero and one and it is the fraction of the time you "
             "are willing to be left holding stock. Write it as a fraction, not a "
             "percentage: `7/10` is exact and `70%` invites rounding at the comparison "
             "step."),
            ("Walk the cumulative distribution until it reaches the ratio",
             "Smallest `Q` with `P(D ≤ Q) ≥` the ratio. The inequality is not strict, so a "
             "cumulative probability landing exactly on the ratio is reached. Ties here "
             "mean two quantities cost the same, not that the rule is ambiguous."),
            ("Price a few quantities either side and confirm",
             "The expected cost at `Q − 1`, `Q` and `Q + 1` should fall then rise. This is "
             "three sums over a finite distribution and it catches an inverted ratio "
             "immediately, which is the one error the rule cannot catch by itself."),
        ],
        "worked": {
            "title": "A stall, a bakery and a spare part, priced the same way",
            "intro": [
                "Three distributions and three pairs of unit costs. The only thing that "
                "changes between them is the ratio, and it moves the answer from above the "
                "mean to below it and back again.",
            ],
            "lines": [
                "A   demand 0..4 at 1,2,3,3,1 tenths      cᵤ = 7   cₒ = 3   ratio 7/10",
                "",
                "      Q        0      1      2      3      4      5      6",
                "      CDF     1/10   3/10   3/5    9/10    1      1      1",
                "      cost   147/10 87/10  47/10  37/10  57/10  87/10 117/10",
                "",
                "      first CDF at or above 7/10:  Q = 3       cheapest row:  Q = 3",
                "      mean demand 21/10, so the order is ABOVE the mean",
                "",
                "B   demand 8..12 at 1/8,1/4,1/4,1/4,1/8  cᵤ = 2   cₒ = 5   ratio 2/7",
                "",
                "      first CDF at or above 2/7:   Q = 9       cost 23/8",
                "      mean demand 10, so the order is BELOW the mean",
                "",
                "C   demand 0..4 at 1/2,1/4,1/8,1/16,1/16  cᵤ = 20  cₒ = 1  ratio 20/21",
                "",
                "      first CDF at or above 20/21: Q = 4       cost 49/16",
                "      mean demand 15/16, so the order is four times the mean",
                "      and 5 costs 65/16, 6 costs 81/16 — the top of the support, not a runaway",
            ],
            "after": [
                "Three answers, three positions relative to the mean, and one rule. The "
                "distributions in A and C have the same support and the same shape of "
                "story; what separates an order of `3` from an order of `4` is that a "
                "stockout costs twenty times a leftover in one and a little over twice as "
                "much in the other. Anyone who reaches for the mean is answering a "
                "question about demand when the question was about costs.",
                "Every number above is a ratio of whole numbers, and there is nothing on "
                "this page to round. That is a property of the model rather than of the "
                "worked example: the expected cost is a finite sum of products of rational "
                "probabilities and rational costs, so no root can arise. The two quantities "
                "this course does round belong to the earlier lessons, and it is worth "
                "being able to say which is which without checking.",
                "For a rehearsal, keep distribution A and raise the overage cost from `3` "
                "to `7`. The supplied first move is that the ratio becomes `1/2`. Work out "
                "which quantity the cumulative distribution reaches it at, and predict "
                "whether the expected cost there is above or below `37/10` before the panel "
                "prices it.",
            ],
        },
        "quiz_title": "Ratios, means and what one season allows",
        "quiz": [
            {"q": "Underage costs `2` and overage costs `5`, and mean demand is exactly `10`. What does the rule order?",
             "a": ["`10`, the mean", "Something below `10`, because leftovers cost more than shortages",
                   "Something above `10`, because the ratio is below a half",
                   "`10` rounded up to the next whole unit of demand"],
             "c": 1,
             "why": "The ratio is `2/7`, well below a half, so the cumulative distribution "
                    "reaches it early and the order lands below the mean &mdash; at `9` on "
                    "the worked bakery. A ratio below a half means you would rather be "
                    "short than left holding, and the mean is not the answer to any "
                    "question this model asks."},
            {"q": "The critical ratio comes out at `7/10`. What is that number?",
             "a": ["The fraction of demand to order", "The probability of a stockout under the optimal policy",
                   "The cumulative probability the order quantity has to reach", "Seven tenths of the mean demand"],
             "c": 2,
             "why": "It is a level for the cumulative distribution: order the smallest `Q` "
                    "with `P(D ≤ Q) ≥ 7/10`. It is not a quantity and not a fraction of "
                    "one. Nor is it the stockout probability &mdash; the chance of running "
                    "short is `1 − P(D ≤ Q)`, which on the worked stall is `1/10` rather "
                    "than `3/10`, because the cumulative distribution overshoots the ratio "
                    "at the quantity it picks."},
            {"q": "Why does the panel price quantities above the largest possible demand?",
             "a": ["To make the curve look symmetric", "Because the optimum can be above the support",
                   "So that &ldquo;the crossing is the minimum&rdquo; is a claim about the whole line rather than about the points where demand has mass",
                   "Because the cumulative distribution is undefined inside the support"],
             "c": 2,
             "why": "Beyond the top of the support every extra unit is pure overage, so "
                    "the curve rises with certainty and the optimum cannot be there. That "
                    "is exactly why pricing those quantities is worth doing: it turns an "
                    "assertion about the shape of the curve into something a reader can "
                    "see, and it answers the first question most readers actually have."},
            {"q": "How does this model differ from the economic order quantity model in what it trades off?",
             "a": ["It trades ordering cost against holding cost, with a random demand rate",
                   "It trades the cost of a missing unit against the cost of an unsold one, and the fixed ordering cost drops out",
                   "It trades purchase price against holding cost", "It makes the same trade-off with a different formula"],
             "c": 1,
             "why": "There is one order, so `K` is paid whatever is decided and cannot "
                    "influence the decision; there is no cycle, so there is no ongoing "
                    "holding rate either. What is left is two unit costs and a "
                    "distribution. That is a genuinely different model rather than the "
                    "earlier one with randomness added, which is why its answer is a "
                    "quantile rather than a square root."},
        ],
        "mistakes": [
            ("Ordering the mean",
             "The mean answers &ldquo;how much will be wanted&rdquo;. The question is "
             "&ldquo;how much should be bought given what each kind of error costs&rdquo;, "
             "and the three worked instances land above the mean, below it, and at four "
             "times it. Ordering the mean is right only when the two unit costs are equal, "
             "and even then only when the distribution is symmetric."),
            ("Swapping the two unit costs",
             "`cᵤ` is the cost of being short and `cₒ` of being long. Swapping them "
             "replaces the ratio by its complement, and on the worked stall that moves the "
             "answer from `3` to `2` with no sign that anything has gone wrong &mdash; both "
             "are plausible quantities and both come with a confident-looking table. "
             "Pricing one quantity either side is the check that catches it."),
            ("Normalising a distribution that does not sum to one",
             "A set of probabilities summing to `0.99` or `1.02` is a typing error, and "
             "rescaling it answers a question about a different distribution. The lab "
             "refuses the input and says why, which is the behaviour to copy: the cost of "
             "stopping is a few seconds and the cost of rescaling is an answer that looks "
             "finished."),
        ],
        "standard": ("Finish when the critical ratio reads as a probability rather than as a quantity.",
                     "You should be able to identify the underage and overage costs in a "
                     "described situation, form the ratio, find the smallest quantity whose "
                     "cumulative probability reaches it, confirm by pricing either side, "
                     "and say why the answer can be above or below the mean depending on "
                     "nothing but the two costs."),
        "note": "One season and one order is the smallest random model there is. The next lesson puts the cycle back: demand is random, orders repeat, and the question becomes when to place one rather than how big to make it &mdash; which turns out to be a question about the lead time and nothing else.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "reorder-points-and-two-service-levels",
        "title": "Reorder Points, and Two Numbers Called Service",
        "module": "Reorder points and review intervals",
        "one_line": "The risk lives in the lead time, so the reorder point is a quantile of lead-time demand — and the two numbers everyone calls the service level are not the same number.",
        "summary": (
            "With demand random and stock watched continuously, the order quantity and the "
            "reorder point are separate decisions, and only the second one carries any "
            "risk: the only interval in which a stockout can happen is the lead time "
            "between placing an order and receiving it. So the reorder point is a quantile "
            "of the demand over `L` periods, built by convolution. Then the sting: "
            "<strong>cycle service</strong> and <strong>fill rate</strong> are two "
            "different measurements of one policy, and on the worked instance they are "
            "68.75% and 99.625%."
        ),
        "key": [
            "a stockout can only happen between placing an order and receiving it",
            "lead-time demand = the L-fold convolution of one period's demand",
            "safety stock = r − E[lead-time demand];  it can be zero, or negative",
            "cycle service  = P(no stockout in a cycle) = P(lead-time demand ≤ r)",
            "fill rate      = 1 − E[shortage per cycle]/Q      — a different number entirely",
            "0,1,2 at 1/4,1/2,1/4 with L = 2, r = 2, Q = 100:  68.75% and 99.625%",
        ],
        "key_label": "One policy, one exposure window, and two ways to measure it",
        "concepts_intro": (
            "Three ideas. The first says where the risk is, the second says how to build "
            "the distribution it lives on, and the third is the one this course would "
            "choose if it could only keep one."
        ),
        "concepts": [
            ("The only exposure is the lead time",
             "While stock is above the reorder point nothing can go wrong: an order has not "
             "been placed and none is needed. Once one is placed, the question is whether "
             "what remains covers demand until it arrives. Everything before that moment "
             "and everything after it is safe, so the reorder point is a decision about the "
             "distribution of demand over `L` periods and about nothing else."),
            ("Lead-time demand is a convolution, and its spread does not scale like its mean",
             "Two periods of demand is the distribution of a sum, so the probabilities are "
             "convolved rather than the values multiplied. The mean does scale: `L` periods "
             "of a mean-1 demand has mean `L`. The shape does not. On the worked "
             "distribution one period runs `0` to `2` and two periods run `0` to `4` with "
             "`3/8` of the mass in the middle, so the tail grows more slowly than the "
             "support does &mdash; which is why doubling the lead time needs less than "
             "double the safety stock."),
            ("Cycle service and fill rate answer different questions",
             "Cycle service is the probability that a cycle ends without a stockout. Fill "
             "rate is the fraction of demand met from stock. They are computed from the "
             "same policy and they are not the same number: the first counts cycles and "
             "the second counts units, and the order quantity appears in one and not in "
             "the other. Both get called &ldquo;the service level&rdquo;, and quoting one "
             "where a contract means the other is the most expensive confusion in this "
             "subject."),
        ],
        "read_title": "Where the risk is, and the two numbers it can be measured with",
        "read_intro": "The exposure window, the convolution that describes it, the reorder point, and then the two service levels side by side.",
        "body": [
            ("def", ("Continuous review, and the reorder point",
                     "Stock is watched continuously. When it falls to the "
                     "<strong>reorder point</strong> `r`, an order for `Q` is placed and "
                     "arrives after a <strong>lead time</strong> of `L` periods. Demand in "
                     "each period is an independent random variable with a known "
                     "distribution.",
                     "<strong>Safety stock</strong> is `r − μ`, where `μ` is the expected "
                     "demand over the lead time. It is the amount held against variation "
                     "rather than against the average, and it can be zero or negative.")),
            ("p", "`Q` and `r` are separate decisions. `Q` is a cost question and the "
                  "earlier lessons of this course answer it; `r` is a risk question and "
                  "this lesson answers it. Treating them together is possible and it is not "
                  "what makes this model useful: almost all of the value is in noticing "
                  "that the risk window is the lead time and nothing else."),
            ("math", [
                "one period's demand:    0 with 1/4,   1 with 1/2,   2 with 1/4",
                "",
                "two periods, by convolution — every way each total can happen:",
                "",
                "   0:  (0,0)                            = 1/16",
                "   1:  (0,1) + (1,0)                    = 1/4",
                "   2:  (0,2) + (1,1) + (2,0)            = 3/8",
                "   3:  (1,2) + (2,1)                    = 1/4",
                "   4:  (2,2)                            = 1/16",
                "",
                "mean 2, support 0 to 4 — the mean doubled, the support doubled,",
                "and the mass piled up in the middle, which is the part that matters",
            ]),
            ("p", "That distribution is what the reorder point is a quantile of. Set "
                  "`r = 2` &mdash; exactly the mean, so zero safety stock &mdash; and a "
                  "cycle survives whenever lead-time demand is `0`, `1` or `2`, which is "
                  "`1/16 + 1/4 + 3/8 = 11/16`. As a percentage that is `68.75%`, and it is "
                  "an exact fraction printed to two places rather than a rounded decimal."),
            ("h3", "The same policy, measured two ways"),
            ("def", ("Cycle service and fill rate",
                     "<strong>Cycle service</strong> is `P(lead-time demand ≤ r)`, the "
                     "probability that a cycle ends without running out. It does not "
                     "mention `Q`.",
                     "<strong>Fill rate</strong> is `1 − E[shortage per cycle]/Q`, the "
                     "fraction of demand met from stock. The expected shortage is "
                     "`E[(lead-time demand − r)⁺]`, and dividing by the order quantity "
                     "turns a per-cycle expectation into a per-unit one.")),
            ("p", "At `r = 2` the expected shortage is `3/8` of a unit per cycle: with "
                  "probability `1/4` you are one short and with probability `1/16` you are "
                  "two short. Spread that over an order quantity of `100` and the fill rate "
                  "is `1 − (3/8)/100 = 797/800`, which is `99.625%`. The same policy, at "
                  "the same instant, is 68.75% reliable per cycle and 99.625% reliable per "
                  "unit of demand."),
            ("math", [
                "one period 0,1,2 at 1/4,1/2,1/4;   L = 2;   Q = 100",
                "",
                "   r    safety   cycle service   E[short]/cycle   fill rate",
                "",
                "   0      −2        1/16  =  6.25%      2          49/50   = 98.000%",
                "   1      −1        5/16  = 31.25%    17/16      1583/1600 = 98.938%",
                "   2       0       11/16  = 68.75%      3/8        797/800 = 99.625%",
                "   3       1       15/16  = 93.75%      1/16      1599/1600= 99.938%",
                "   4       2         1    =100.00%        0            1   =100.000%",
                "",
                "at r = 0 the two readings are 6.25% and 98.0% — of one policy",
            ]),
            ("p", "The top row is the one to stare at. A reorder point of zero means "
                  "ordering only when the shelf is empty, and fifteen cycles in sixteen "
                  "will run short. It is also, measured by units, a 98% service: almost all "
                  "demand is still met, because the shortages are small and the order "
                  "quantity is large. Neither number is wrong. They are answers to "
                  "different questions, and a supplier who promised one and delivered the "
                  "other would be in court."),
            ("p", "The gap between them is the order quantity. A larger `Q` spreads the "
                  "same expected shortage over more demand, so the fill rate rises while "
                  "the cycle service does not move at all &mdash; `Q` does not appear in "
                  "it. Shrink `Q` to `1` on the worked instance and the fill rate falls to "
                  "`5/8`, which is `62.5%`, now BELOW the cycle service of 68.75%. That "
                  "inversion is the proof that one is not the other rescaled."),
            ("h3", "Hitting a target"),
            ("p", "Cycle service rises with `r` and never falls, so &ldquo;the smallest "
                  "reorder point reaching 95%&rdquo; is well defined and can be found by "
                  "walking up. On the worked instance no reorder point gives between 93.75% "
                  "and 100%: the distribution is discrete, `r = 3` gives `15/16` and "
                  "`r = 4` gives `1`, so the smallest reorder point meeting a 95% target is "
                  "`4` &mdash; total coverage, two units of safety stock, and an achieved "
                  "service of 100% rather than 95%."),
            ("p", "Overshooting a target is what discrete distributions do, and it is a "
                  "fact about the distribution rather than a rounding. It is also the "
                  "reason a service target should be stated with the measurement attached: "
                  "a 95% target on cycle service costs two units of safety stock here, "
                  "while a 95% target on fill rate is already met at `r = 0`, where the safety stock is `−2`."),
            ("example", ("A longer lead time, and why it costs more than the extra mean",
                         "Raise the lead time to three periods. The mean rises from `2` to "
                         "`3` and the support from `0…4` to `0…6`, and a reorder point of "
                         "`2` &mdash; unchanged &mdash; now delivers a cycle service of "
                         "`11/32`, which is `34.38%`.",
                         "Holding the reorder point at the old mean was already marginal "
                         "at 68.75%; at the longer lead time it is worse than a coin. "
                         "Restoring the old service level takes more than the one extra "
                         "unit of mean demand, because the distribution has spread as well "
                         "as shifted &mdash; which is the practical content of the word "
                         "&ldquo;convolution&rdquo;.")),
            ("p", "Everything on this page is exact. The per-period probabilities are "
                  "fractions, the convolution is a finite sum of products of fractions, the "
                  "expected shortage is a finite sum, and the two service levels are "
                  "fractions printed as percentages to a stated number of places. Nothing "
                  "here is rounded, and the distinction from the earlier lessons &mdash; "
                  "where the economic order quantity and its cost genuinely are irrational "
                  "&mdash; is one a reader should be able to state without looking."),
        ],
        "lab": ("inventory", {
            "mode": "reorder",
            "preset": "steady",
            "panel_title": "Set the per-period demand, the lead time and the reorder point",
            "panel_intro": "The bars are the demand over the whole lead time, built here by "
                           "convolving the period distribution with itself, with the "
                           "reorder point marked and the outcomes above it shaded as "
                           "shortages. Cycle service and fill rate are computed from that "
                           "same distribution and printed side by side, with their "
                           "definitions, because they are routinely quoted for one "
                           "another. Raise the lead time and watch the distribution spread "
                           "rather than merely shift.",
        }),
        "steps_title": "Setting a reorder point against a service target",
        "steps_intro": "Five steps, and the first one is the question that decides all the others.",
        "steps": [
            ("Ask which service level the target refers to",
             "Cycle service counts cycles; fill rate counts units. They differ by an order "
             "of magnitude in the gap on the worked instance, and a target quoted without "
             "its definition is not a number. If nobody can say which is meant, that is the "
             "finding, and it is worth more than any calculation that follows."),
            ("Build the lead-time distribution by convolution, not by scaling",
             "Convolve the per-period distribution with itself `L` times. The mean is `L` "
             "times one period's mean, but the shape is not one period's shape stretched, "
             "and using a scaled single-period distribution understates the middle and "
             "overstates the tails."),
            ("Read the reorder point off the cumulative distribution",
             "For a cycle-service target, the smallest `r` with "
             "`P(lead-time demand ≤ r) ≥ α`. Cycle service is monotone in `r`, so walking "
             "up from zero finds it and the first one that clears is the answer."),
            ("Compute the expected shortage as well, and divide it by Q",
             "`E[(lead-time demand − r)⁺]` is a short sum over the tail. Divide by the "
             "order quantity for the fill rate. Print both, always: the pair is the "
             "description of the policy and either one alone is an invitation to be "
             "misread."),
            ("Say what the achieved level actually is",
             "A discrete distribution overshoots. On the worked instance a 95% cycle-"
             "service target is met at `r = 4` and delivers 100%, which costs two units of "
             "safety stock that nobody asked for. Reporting &ldquo;95% achieved&rdquo; "
             "there would be false in the cheap direction and would hide the overshoot."),
        ],
        "worked": {
            "title": "One policy, five reorder points, and two service columns",
            "intro": [
                "Demand of `0`, `1` or `2` a period with probabilities `1/4`, `1/2`, `1/4`; "
                "a lead time of two periods; an order quantity of `100`. Every figure is "
                "the panel's own and every one of them is exact.",
            ],
            "lines": [
                "lead-time demand (two periods, convolved):",
                "    0: 1/16    1: 1/4    2: 3/8    3: 1/4    4: 1/16       mean 2",
                "",
                "  r   safety   cycle service        E[short]    fill rate at Q = 100",
                "",
                "  0     −2      1/16  =   6.25%        2         49/50    =  98.000%",
                "  1     −1      5/16  =  31.25%     17/16      1583/1600  =  98.938%",
                "  2      0     11/16  =  68.75%       3/8        797/800  =  99.625%",
                "  3      1     15/16  =  93.75%       1/16      1599/1600 =  99.938%",
                "  4      2        1   = 100.00%         0            1    = 100.000%",
                "",
                "smallest r reaching a 95% CYCLE-SERVICE target:   r = 4   (achieves 100%)",
                "smallest r reaching a 95% FILL-RATE target:       r = 0   (achieves 98%)",
                "",
                "shrink the order quantity to Q = 1, leaving r = 2:",
                "    fill rate = 1 − (3/8)/1 = 5/8 = 62.5%,  now BELOW cycle service",
            ],
            "after": [
                "The two right-hand columns are the lesson. One policy, one instant, two "
                "numbers that differ by thirty percentage points at `r = 2` and by ninety "
                "at `r = 0`. Both are called the service level in ordinary use, and the "
                "only defence is to print the definition beside the figure every single "
                "time &mdash; which is what the panel does and why it does it.",
                "The last block is the part that proves they are genuinely different "
                "quantities rather than one rescaled. With `Q = 1` the fill rate drops "
                "below the cycle service, so no fixed relationship holds between them. The "
                "order quantity is in one definition and not in the other, and that single "
                "structural difference is enough to make the ordering depend on the data.",
                "For a rehearsal, switch the panel to the lumpy example: demand `0`, `1` or "
                "`4` with probabilities `3/5`, `1/5`, `1/5`, a lead time of three periods, "
                "a reorder point of `4` and an order quantity of `60`. The supplied first "
                "move is that the mean lead-time demand is `3`. Predict which of the two "
                "service figures will be the larger, then check the sizes: they come out "
                "`72.80%` and `98.893%`, and the smallest reorder point reaching a 95% "
                "cycle service is `8`.",
            ],
        },
        "quiz_title": "Windows, convolutions and two definitions",
        "quiz": [
            {"q": "Why is the reorder point a quantile of demand over the LEAD TIME rather than over the cycle?",
             "a": ["Because the cycle length is random", "Because a stockout can only occur between placing an order and receiving it",
                   "Because the lead time is shorter than the cycle", "Because demand is independent between periods"],
             "c": 1,
             "why": "Above the reorder point no order is outstanding and none is needed; "
                    "once one is placed, the only question is whether what remains lasts "
                    "until it arrives. Everything outside that window is safe by "
                    "construction, so the distribution that matters is the one over `L` "
                    "periods. Independence is what lets the convolution be computed, not "
                    "what makes the window the right one."},
            {"q": "A policy has a cycle service of `68.75%` and a fill rate of `99.625%`. Which is correct?",
             "a": ["One of them has been computed wrongly",
                   "Both are correct: one counts cycles that end without a stockout, the other counts units met from stock",
                   "The fill rate is the cycle service adjusted for the order quantity, so they always differ by a fixed factor",
                   "The fill rate is always the larger of the two"],
             "c": 1,
             "why": "They measure different things and both are right. There is no fixed "
                    "relationship: shrinking the order quantity to `1` on this instance "
                    "drops the fill rate to `62.5%`, below the cycle service, because `Q` "
                    "appears in one definition and not the other."},
            {"q": "The lead time rises from two periods to three and the reorder point stays at `2`. What happens to cycle service?",
             "a": ["It falls by one period's worth of demand, from 68.75% to about 58%",
                   "It is unchanged, since the reorder point has not moved",
                   "It falls to `11/32`, about 34.38%, because the distribution spreads as well as shifts",
                   "It cannot be computed without the order quantity"],
             "c": 2,
             "why": "The lead-time distribution is a fresh convolution: mean `3` instead of "
                    "`2`, support `0…6` instead of `0…4`. A reorder point of `2` is now "
                    "below the mean and covers only `11/32` of the outcomes. The order "
                    "quantity is irrelevant to cycle service, which is exactly the "
                    "difference between it and the fill rate."},
            {"q": "A 95% cycle-service target on the worked instance is met at `r = 4`, which achieves 100%. Why not report 95%?",
             "a": ["Because the target was a minimum and the policy exceeds it, which costs two units of safety stock",
                   "Because 95% is not achievable with rational probabilities",
                   "Because the fill rate is higher", "Because `r = 4` also maximises the fill rate"],
             "c": 0,
             "why": "A discrete distribution jumps: `r = 3` gives `93.75%` and `r = 4` "
                    "gives `100%`, with nothing in between. Reporting the target rather "
                    "than the achievement hides the overshoot, and the overshoot is real "
                    "inventory being paid for. It is a fact about the distribution and not "
                    "a rounding &mdash; every figure here is an exact fraction."},
        ],
        "mistakes": [
            ("Quoting one service level and meaning the other",
             "This is the costly one. On the worked instance the same policy reads 68.75% "
             "or 99.625% depending on which definition is used, and both numbers are "
             "correct. A contract, a target or a dashboard that says &ldquo;service "
             "level&rdquo; without saying which has not specified anything, and the "
             "difference is usually noticed at the first dispute rather than at the first "
             "review."),
            ("Scaling the single-period distribution instead of convolving it",
             "Multiplying one period's values by `L` gets the mean right and the shape "
             "wrong: it puts the mass at `0`, `L` and `2L` when the truth is concentrated "
             "in the middle. On two periods it would give `1/4, 1/2, 1/4` at `0, 2, 4` "
             "instead of the five-point distribution with `3/8` in the middle, and every "
             "service figure computed from it would be wrong in both directions."),
            ("Setting the reorder point to the mean and expecting half",
             "Zero safety stock does not mean 50% service. On the worked instance "
             "`r = 2` is exactly the mean and gives 68.75%, because the distribution is "
             "discrete and the event is `≤ r` rather than `< r`. The number can land "
             "anywhere; the only way to know it is to read it off the cumulative "
             "distribution."),
        ],
        "standard": ("Finish when you refuse to act on a service target until somebody says which service it is.",
                     "You should be able to say why the lead time is the only exposure "
                     "window, build a lead-time distribution by convolution, compute safety "
                     "stock, cycle service and expected shortage from it, turn the shortage "
                     "into a fill rate with the order quantity, find the smallest reorder "
                     "point reaching a cycle-service target, and report what it actually "
                     "achieves rather than what was asked for."),
        "note": "Continuous review assumes the shelf is watched every moment. The last lesson of this course assumes it is watched every `R` periods instead, which changes the exposure window in a way that is easy to state and easy to get wrong &mdash; and the panel prices the mistake rather than warning about it.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "periodic-review-and-the-base-stock-level",
        "title": "Periodic Review and the Base-Stock Level",
        "module": "Reorder points and review intervals",
        "one_line": "If the shelf is only looked at every R periods, the stock in hand has to cover R + L periods — and covering the lead time alone is the mistake this lesson prices.",
        "summary": (
            "Under periodic review, stock is inspected every `R` periods and topped up to a "
            "<strong>base-stock level</strong> `S`. The order placed now arrives after `L` "
            "periods; the next chance to order anything is `R` periods from now and it "
            "arrives `L` after that. So what is on hand and on order right now has to last "
            "`R + L` periods, and `S` is a quantile of the demand over that whole span. "
            "Covering only the lead time is the standard error, and on the worked instance "
            "it turns a 90% target into 34.38%."
        ),
        "key": [
            "review every R periods, order up to the base-stock level S",
            "the order placed now lands after L;  the NEXT one lands R + L from now",
            "so the exposure window is R + L periods, not L and not R",
            "S = the smallest level with  P(demand over R + L periods ≤ S) ≥ α",
            "0,1,2 at 1/4,1/2,1/4 with R = 2, L = 1:  three periods, mean 3, S = 5 at α = 90%",
            "S = 5 actually achieves 63/64 = 98.44%;  covering L alone gives S = 2 and 34.38%",
        ],
        "key_label": "One window, and the two shorter ones it is mistaken for",
        "concepts_intro": (
            "Three ideas, and the first of them is the whole lesson: everything else is "
            "what follows once the window is right."
        ),
        "concepts": [
            ("Think about when the next chance to act arrives, not when this order does",
             "An order placed at this review lands `L` periods from now. If demand in the "
             "meantime turns out high, the earliest correction is the order placed at the "
             "<em>next</em> review, `R` periods from now, and that one lands `R + L` "
             "periods from now. So the stock in hand and on order at this moment is the "
             "last defence for the whole of `R + L`. The window is a statement about when "
             "you can next intervene, which is why it contains the review interval at "
             "all."),
            ("A base-stock level is a position, not an order quantity",
             "The order placed is `S` minus whatever is already on hand and on order, so it "
             "varies from review to review while `S` does not. That is the difference "
             "between this and continuous review: there the quantity `Q` is fixed and the "
             "moment varies; here the moment is fixed and the quantity varies. Comparing "
             "the two policies by comparing `S` with `Q` compares two unlike things."),
            ("A discrete distribution overshoots a target, and that is not a rounding",
             "The cumulative distribution jumps, so the smallest level reaching a target "
             "usually passes it. On the worked instance a 90% target is first cleared at "
             "`S = 5`, which delivers `63/64`, or 98.44%. Reporting 90% there would "
             "understate the stock being held by a whole unit, and the gap is a "
             "property of the distribution rather than of any arithmetic done to it."),
        ],
        "read_title": "Why the interval is in the formula",
        "read_intro": "The policy, the argument that fixes the window, the quantile, and what covering the wrong window actually costs.",
        "body": [
            ("def", ("Periodic review, and the base-stock level",
                     "Stock is inspected every `R` periods &mdash; the <strong>review "
                     "interval</strong> &mdash; and an order is placed bringing the total "
                     "on hand plus on order up to the <strong>base-stock level</strong> "
                     "`S`. The order arrives after a lead time of `L` periods.",
                     "`S` is chosen so that the probability of meeting all demand over the "
                     "exposure window is at least the target `α`.")),
            ("p", "Everything turns on what the exposure window is, and the argument is "
                  "worth doing slowly because the wrong answer is so plausible. Suppose a "
                  "review happens now. The order placed now arrives at time `L`. Between "
                  "now and then, nothing can be changed. At time `R` there is another "
                  "review, and whatever is ordered there arrives at time `R + L`. So the "
                  "first moment at which a decision made after now can affect the stock "
                  "position is `R + L`, and the position taken now must carry the demand of "
                  "the entire interval up to it."),
            ("math", [
                "     now          R                 L                R + L",
                "      |-----------|-----------------|------------------|",
                "      |           |                 |                  |",
                "   review      next review     this order       next order",
                "   order to S                    arrives           arrives",
                "",
                "  the position taken NOW is the last one that can affect stock",
                "  before R + L, so it must cover demand over R + L periods",
            ]),
            ("p", "Set `L = 0` and the window is still `R` periods: the order arrives "
                  "instantly, but the next one cannot be placed until the next review, so "
                  "the stock has to last the interval. Set `R = 1` and the window is "
                  "`1 + L`, which is the continuous-review answer with one period of "
                  "granularity added. Both limits are worth checking on the panel, because "
                  "they are the two cases in which a reader's intuition says the interval "
                  "should disappear and it does not."),
            ("h3", "The quantile, on the worked instance"),
            ("p", "Demand is `0`, `1` or `2` a period with probabilities `1/4`, `1/2`, "
                  "`1/4`. Review every two periods, lead time one period, so the window is "
                  "three periods and the distribution to quantile is the three-fold "
                  "convolution: mean `3`, support `0` to `6`, and mass concentrated in the "
                  "middle."),
            ("math", [
                "demand over R + L = 3 periods:",
                "",
                "   total      0      1      2      3      4      5      6",
                "   prob     1/64   3/32  15/64   5/16  15/64   3/32   1/64",
                "   cumul    1/64   7/64  11/32  21/32  57/64  63/64    1",
                "            1.56% 10.94% 34.38% 65.63% 89.06% 98.44% 100.00%",
                "",
                "target 90%:  the first cumulative at or above it is at 5",
                "             S = 5, achieving 63/64 = 98.44%",
                "",
                "target 95%:  also S = 5.      target 99%:  S = 6, achieving 100%",
            ]),
            ("p", "`S = 4` reaches 89.06%, just short of the 90% target, and `S = 5` "
                  "reaches 98.44%. There is nothing between them, so the policy that meets "
                  "the target exceeds it by more than eight percentage points and holds a "
                  "unit of stock that a continuous target would not have asked for. That is "
                  "worth reporting rather than smoothing: the panel prints the achieved "
                  "level beside the target for exactly this reason."),
            ("h3", "What covering the lead time alone costs"),
            ("example", ("The standard error, priced",
                         "Cover only the lead time. `L = 1` period of demand, quantiled at "
                         "90%, gives `S = 2` &mdash; a perfectly sensible-looking number "
                         "reached by a perfectly sensible-looking calculation.",
                         "Over the real exposure window of three periods, a level of `2` "
                         "delivers `11/32` of service: 34.38% against a target of 90%. The "
                         "policy is not slightly under-stocked, it is wrong by a factor, "
                         "and every figure used to produce it was computed correctly.")),
            ("p", "The panel shows both levels on the same table, the right one in amber "
                  "and the wrong one in red, with the service each delivers over the real "
                  "window. That is the design choice worth copying: a misconception that "
                  "gets priced on the same page as the correct answer is much harder to "
                  "keep than one that gets a warning in the margin."),
            ("example", ("A longer interval, and where the stock goes",
                         "Raise the lead time to two periods, so the window becomes four. "
                         "The mean rises to `4`, and the base-stock level for a 90% target "
                         "rises to `6`, achieving 96.48%.",
                         "One extra period of lead time bought one extra unit of "
                         "base-stock, which is less than the extra mean demand would "
                         "suggest if the levels were driven by the mean alone &mdash; and "
                         "more than nothing, which is what a reader who had fixed on the "
                         "review interval might expect. The window is `R + L` and both "
                         "letters do work.")),
            ("p", "Compare the two review policies on their exposure. Continuous review "
                  "watches the shelf every moment, so it is exposed only for `L`; periodic "
                  "review is exposed for `R + L`. The extra stock is what the reviewing "
                  "discipline is not doing, and the trade is a real one: reviewing more "
                  "often costs effort and holds less stock, reviewing less often costs "
                  "stock and holds less attention. The model does not choose between them, "
                  "and it does say exactly what the difference is."),
            ("p", "Every figure on this page is exact. The convolution over `R + L` periods "
                  "is a finite sum of products of rational probabilities, the cumulative "
                  "column is a running sum of fractions, and the percentages are those "
                  "fractions printed to two places rather than decimals standing in for "
                  "them. `98.44%` is `63/64`, and `34.38%` is `11/32`; neither is rounded "
                  "in the sense the earlier lessons of this course use the word, where an "
                  "order quantity of `20√30` genuinely has no exact decimal form."),
        ],
        "lab": ("inventory", {
            "mode": "review",
            "preset": "steady",
            "panel_title": "Set the review interval, the lead time and the target",
            "panel_intro": "The distribution quantiled here is the demand over the review "
                           "interval PLUS the lead time, built by convolution on this "
                           "page. The base-stock level is the first total whose cumulative "
                           "probability reaches the target, and the achieved level is "
                           "printed beside it because a discrete distribution overshoots. "
                           "The comparison row prices the usual mistake &mdash; covering "
                           "the lead time alone &mdash; over the real window, instead of "
                           "warning about it.",
        }),
        "steps_title": "Setting a base-stock level",
        "steps_intro": "Four steps. The first is the one this lesson exists for, and it takes one sentence to get right and one to get wrong.",
        "steps": [
            ("Write down the window as R + L, in words, before computing anything",
             "&ldquo;The order I place now is the last one that can arrive before the one "
             "I place at the next review.&rdquo; Say it about the actual situation, with "
             "the actual numbers in it. A reader who writes `L` here will get every "
             "subsequent step right and the answer wrong."),
            ("Convolve the per-period distribution R + L times",
             "Not `L` times and not `R` times. The mean is `(R + L)` times one period's "
             "mean, and the spread grows more slowly than the mean does, which is why the "
             "safety component of `S` grows more slowly than the window."),
            ("Read S off the cumulative distribution at the target",
             "The smallest total whose cumulative probability reaches `α`. The cumulative "
             "column is monotone, so the first one that clears is the answer and there is "
             "nothing to search."),
            ("Report the achieved service, not the target",
             "A discrete distribution jumps past the target. On the worked instance a 90% "
             "target is met at `S = 5` and achieves 98.44%, which is a unit of stock more "
             "than the target strictly required. Both numbers belong in the answer, and "
             "the gap between them is the cost of a discrete world."),
        ],
        "worked": {
            "title": "Three periods of exposure, and the level that covers them",
            "intro": [
                "Demand `0`, `1`, `2` a period at `1/4`, `1/2`, `1/4`. Review every two "
                "periods, lead time one, target 90%. Every figure is the panel's own and "
                "all of them are exact fractions.",
            ],
            "lines": [
                "window:  R + L = 2 + 1 = 3 periods        mean over it: 3",
                "",
                "  total      0      1      2      3      4      5      6",
                "  prob     1/64   3/32  15/64   5/16  15/64   3/32   1/64",
                "  cumul    1/64   7/64  11/32  21/32  57/64  63/64    1",
                "           1.56% 10.94% 34.38% 65.63% 89.06% 98.44% 100.00%",
                "",
                "  first cumulative at or above 90%:   S = 5,  achieving 63/64 = 98.44%",
                "  S = 4 would give 57/64 = 89.06%, short of the target by under 1%",
                "",
                "covering the LEAD TIME alone:",
                "",
                "  one period of demand, quantiled at 90%   ⟹   S = 2",
                "  what S = 2 delivers over the real three periods:  11/32 = 34.38%",
                "",
                "changing the window:",
                "",
                "  R = 1, L = 0  ⟹  1 period,  S = 2,  100.00%",
                "  R = 2, L = 0  ⟹  2 periods, S = 3,   93.75%",
                "  R = 2, L = 1  ⟹  3 periods, S = 5,   98.44%",
                "  R = 2, L = 2  ⟹  4 periods, S = 6,   96.48%",
            ],
            "after": [
                "The two middle blocks are the same distribution read twice. `S = 2` is the "
                "right answer to the wrong question &mdash; it is exactly the 90% quantile "
                "of one period's demand &mdash; and it delivers 34.38% against the target. "
                "Nothing in the calculation that produced it is wrong, which is what makes "
                "the error durable: it survives checking, and it can only be caught by "
                "asking what window the number is supposed to cover.",
                "The bottom block shows both letters doing work. With `L = 0` the answer is "
                "still `S = 2` over one period, because the order arrives instantly but the "
                "next one cannot be placed until the next review. Adding a period of lead "
                "time to a two-period review takes `S` from `3` to `5`; adding another "
                "takes it to `6`. The level is not proportional to the window, because the "
                "safety component grows like the spread rather than like the mean.",
                "For a rehearsal, keep the distribution and set the target to 95%. The "
                "supplied first move is that the cumulative column does not change at all "
                "&mdash; only the threshold does. Predict the base-stock level and its "
                "achieved service before you move the slider, and then say what that "
                "result implies about how precisely a service target can be specified on a "
                "discrete distribution.",
            ],
        },
        "quiz_title": "Windows, positions and overshoot",
        "quiz": [
            {"q": "Review every `R = 2` periods with a lead time of `L = 1`. How many periods of demand must the position taken now cover?",
             "a": ["`1`, the lead time", "`2`, the review interval", "`3`, because the next order placed lands `R + L` from now",
                   "`2`, the larger of the two"],
             "c": 2,
             "why": "The order placed now arrives at `L`. The next chance to change "
                    "anything is the review at `R`, and that order lands at `R + L = 3`. "
                    "So the position taken now is the last one that can affect stock before "
                    "then, and it must cover the whole three periods."},
            {"q": "The lead time is zero and the review interval is two periods. What does the base-stock level have to cover?",
             "a": ["Nothing, since orders arrive instantly", "One period", "Two periods, because the next order cannot be placed until the next review",
                   "It depends on the target"],
             "c": 2,
             "why": "Instant arrival removes the lead time, not the interval. Between this "
                    "review and the next there is no opportunity to order at all, so the "
                    "stock has to last two periods. This is the case where the intuition "
                    "&ldquo;cover the lead time&rdquo; fails most visibly: it would say "
                    "cover nothing."},
            {"q": "On the worked instance, a 90% target gives `S = 5` and the panel reports 98.44%. What is that gap?",
             "a": ["Rounding in the cumulative column", "The overshoot of a discrete distribution: `S = 4` gives 89.06% and there is nothing in between",
                   "The difference between cycle service and fill rate", "An error of one unit in the convolution"],
             "c": 1,
             "why": "The cumulative distribution jumps from `57/64` to `63/64`, so the "
                    "smallest level clearing 90% clears it by a lot. Nothing is rounded "
                    "&mdash; `63/64` is exact and `98.44%` is that fraction printed to two "
                    "places. Fill rate is a different measurement and belongs to the "
                    "continuous-review lesson."},
            {"q": "A reader computes the 90% quantile of one period's demand, gets `2`, and uses it as the base-stock level. What is wrong?",
             "a": ["The quantile is computed incorrectly", "Nothing, provided the lead time is one period",
                   "The window is `R + L = 3` periods, and `S = 2` delivers 34.38% over it",
                   "The target should have been applied to the mean rather than the quantile"],
             "c": 2,
             "why": "The quantile itself is right: `2` really is the 90% point of one "
                    "period's demand. The window is wrong, and over the real three periods "
                    "a level of `2` covers `11/32` of outcomes. Every step after the first "
                    "was correct, which is exactly why this error survives review."},
        ],
        "mistakes": [
            ("Covering the lead time and forgetting the interval",
             "The order placed now is not the last one before the stock runs down; it is "
             "the last one before the <em>next review's</em> order arrives. Omitting `R` "
             "turns a 90% target into 34.38% on the worked instance, and every figure in "
             "the wrong calculation is correct, so nothing in the arithmetic will reveal "
             "it."),
            ("Treating the base-stock level as an order quantity",
             "`S` is a target position, and the order placed is `S` minus what is already "
             "on hand and on order. Ordering `S` units at every review ignores everything "
             "in transit and over-orders by exactly the amount already coming, which is "
             "the classic way a periodic-review system oscillates."),
            ("Reporting the target instead of the achievement",
             "A discrete distribution overshoots, so &ldquo;we hold a 90% service "
             "level&rdquo; is usually false and usually false in the expensive direction: "
             "here the policy achieves 98.44% and holds the stock to match. The pair of "
             "numbers is the honest report, and the gap between them is a real cost that a "
             "single figure hides."),
        ],
        "standard": ("Finish when you can say why the review interval belongs in the window without looking it up.",
                     "You should be able to derive `R + L` from the timing of the next "
                     "review and its arrival, build the demand distribution over that "
                     "window by convolution, read the base-stock level off the cumulative "
                     "column at a target, report the service it actually achieves, and "
                     "state what covering the lead time alone would deliver on the same "
                     "data."),
        "note": "That completes the course: a quantity from a discriminant, two corrections to the cycle, and three models in which demand is a distribution rather than a rate. What none of them can do is check the distribution against the world it came from &mdash; the demand model is an input here, and Simulation and Variance Reduction is where a system too tangled for any of these formulas gets run instead of solved.",
    },
]
