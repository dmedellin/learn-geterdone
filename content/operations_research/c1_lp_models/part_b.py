"""Course 1, lessons 06-10 - the rewrites, standard form, and the two structural facts.

Every figure here was read off the `lp` kit rather than off a draft: the min-max
rewrite and the original agree at 132/17 and disagree the moment the direction is
flipped, the falling price band reports 38/3 against a true 16, the pottery costs
12 at (4, 0), the small workshop has ten bases and five corners, and the
objective along the chosen segment climbs by exactly 2 at each of eight steps.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "reformulations-that-keep-linearity",
        "title": "Reformulations That Keep Linearity",
        "module": "Keeping it linear",
        "one_line": "Rewrite an absolute value and a largest-of-several objective as linear programmes, and check the optimum did not move.",
        "summary": (
            "Four requirements that look non-linear are linear after an auxiliary variable is "
            "introduced, and all four are the same argument: the rewrite is legal exactly when "
            "the direction of optimisation forces the auxiliary variable to the value you "
            "intended. Flip the direction and three of the four stop being about the original "
            "problem at all &mdash; which is something a reader can detect, by solving both and "
            "subtracting."
        ),
        "key": [
            "x free            x = x⁺ − x⁻,          x⁺, x⁻ ≥ 0",
            "|x| minimised     |x| = x⁺ + x⁻         at least one is pushed to 0",
            "min of a max      t ≥ every piece,      minimise t",
            "a rising price     one variable per band, the cheaper band fills first",
            "",
            "legal  ⇔  the direction of optimisation forces the auxiliary value",
            "the check:  original by corners − rewrite by simplex  =  0",
        ],
        "key_label": "Four rewrites, one condition",
        "concepts_intro": (
            "There is one idea here and it is repeated four times. The four cases are practice "
            "at the same argument, not four things to memorise."
        ),
        "concepts": [
            ("An auxiliary variable is a claim about where the optimiser will push it",
             "Adding `t` with the rows `t ≥ piece₁` and `t ≥ piece₂` does not make `t` the "
             "larger piece; it makes `t` at least the larger piece. Minimising `t` squeezes it "
             "down onto that piece, and only then is the rewrite an equality in disguise."),
            ("Flip the direction and the same rows say something else",
             "Maximise `t` in that model and nothing above it stops it climbing: the programme "
             "is unbounded while the original still has a finite answer at a corner. The rows "
             "did not change &mdash; the claim about where the optimiser pushes `t` did."),
            ("Two methods that never look at each other are the only evidence worth having",
             "The lab optimises the original by enumerating the corners of each part of the "
             "region where one piece is the one that counts, and the rewrite by the simplex "
             "engine. Subtracting the two answers is a test that can fail, which is why it is "
             "worth running."),
        ],
        "read_title": "Four rewrites, and the direction that makes each one legal",
        "read_intro": "A free variable, an absolute value, a smallest largest piece, and a cost quoted in two bands &mdash; with the condition stated each time.",
        "body": [
            ("p", "The rewrites below sit on one region: `x + y ≤ 8`, `x ≤ 5`, `y ≤ 6` and "
                  "`2x + 3y ≥ 12`. For the first three, `x` is free to go negative as far as "
                  "`−4`; for the price-band rewrite it is held at or above zero, because a "
                  "quantity bought under a price schedule cannot be negative. What changes "
                  "between them is the objective, and what each rewrite does is trade a "
                  "non-linear objective for extra variables and extra rows."),
            ("h3", "A free variable, as a difference"),
            ("def", ("Splitting a free variable",
                     "A variable `x` with no sign restriction is carried as `x = x⁺ − x⁻` with "
                     "`x⁺ ≥ 0` and `x⁻ ≥ 0`. Every occurrence of `x` in every row and in the "
                     "objective is replaced by that difference.",
                     "Any pair with the right difference gives the same objective value, so "
                     "nothing needs to push either part anywhere in particular. This is the one "
                     "rewrite of the four that is legal whichever way the objective is pushed.")),
            ("p", "With the objective `3x + 2y` minimised, the answer is 3 at `x = −3`, "
                  "`y = 6`, and the rewrite reports `x⁺ = 0`, `x⁻ = 3`: the negative value is "
                  "carried by the second part. Maximised, the answer is 21 at `(5, 3)` with "
                  "`x⁻ = 0`. Both agree with the original exactly, which is what “legal in "
                  "either direction” means in practice."),
            ("h3", "An absolute value, when it is minimised"),
            ("p", "The same two parts serve for `|x|`, as their sum rather than their "
                  "difference. That sum is `|x|` only when at least one of `x⁺` and `x⁻` is "
                  "zero, because otherwise both could be inflated together without changing "
                  "`x`. Minimising a non-negative multiple of `x⁺ + x⁻` does push one of them "
                  "to zero. Maximising does the opposite."),
            ("example", ("The same rows, read twice",
                         "Minimise `2|x| + 5y`: the original is 40/3 at `(5, 2/3)` by corner "
                         "enumeration, the rewrite is 40/3 by the simplex engine with "
                         "`x⁺ = 5` and `x⁻ = 0`, and the difference is exactly zero. Now "
                         "maximise the same expression: the original is 36 at `(−3, 6)` and the "
                         "rewrite is unbounded, because `x⁺` and `x⁻` climb together for ever "
                         "with nothing to stop them. A reader who only ran the rewrite would "
                         "have no way to notice.")),
            ("h3", "The smallest largest piece"),
            ("thm", ("The epigraph rewrite",
                     "Let `f(x) = max(p₁(x), p₂(x), …)` with each `pᵢ` linear. Then minimising "
                     "`f` over a region is the same problem as minimising `t` over the same "
                     "region with the rows `t ≥ pᵢ(x)` added, one per piece, and `t` free.",
                     "The rows make `t` at least every piece, so `t ≥ f(x)` at every feasible "
                     "point, and minimising cannot leave `t` above `f(x)`. Maximising can and "
                     "does: the rewritten programme is then unbounded, and it is a different "
                     "problem rather than a worse answer to this one.")),
            ("p", "Minimise `max(2x + y, −x + 5y)` on the region and both routes report "
                  "132/17, at `x = 48/17`, `y = 36/17`, with `t = 132/17` sitting exactly on "
                  "the two pieces where they cross. The fraction is worth noting: the corner "
                  "that wins is the crossing of the boundary of the region with the line where "
                  "one piece overtakes the other, and nothing about it rounds."),
            ("h3", "A cost quoted in two price bands"),
            ("p", "Suppose the first 3 units of `x` cost 2 each and every unit after that costs "
                  "5. Split the quantity into one variable per band, cap the first at 3, and "
                  "price them separately. A minimiser fills the cheaper band first &mdash; and "
                  "the cheaper band is the earlier one only when the later band costs more. "
                  "That condition is convexity, and it is the condition rather than the "
                  "background."),
            ("example", ("A falling price, and a cost no quantity achieves",
                         "Quote the first 3 units at 5 each and everything after at 2. The true "
                         "cheapest cost on this region is 16, at `(0, 4)`. The band model "
                         "reports 38/3, with `x(1) = 0` and `x(2) = 5`: it has bought five "
                         "units out of the second band without filling the first, which the "
                         "price schedule does not allow. The model is not a worse answer to the "
                         "question; it is a cheaper answer to a question with no cost schedule "
                         "behind it.")),
            ("p", "So the rule to carry away is not “these four tricks work”. It is that an "
                  "auxiliary variable comes with a sentence &mdash; what forces it to the value "
                  "I intend &mdash; and that the sentence is checkable by solving the original "
                  "some other way and subtracting."),
        ],
        "lab": ("lp", {
            "mode": "reform",
            "panel_title": "Pick a rewrite, then flip the direction and watch it break",
            "panel_intro": "The original is answered by enumerating the corners of each part of "
                           "the region on which one piece of the objective is the one that "
                           "counts; the rewrite is answered by the simplex engine, and neither "
                           "looks at the other. Subtracting them is therefore evidence, and on "
                           "three of the four rewrites the difference stops being zero the "
                           "moment the direction is flipped.",
        }),
        "steps_title": "Checking a rewrite before trusting it",
        "steps_intro": "The first two steps are the argument and the last two are the evidence. Skipping the evidence is how an illegal rewrite ships.",
        "steps": [
            ("Name the auxiliary variables and what each is supposed to equal",
             "`t` is supposed to be the largest piece; `x⁺ + x⁻` is supposed to be `|x|`. "
             "Writing the intention down is what makes the next step possible."),
            ("Say what forces that value, in one sentence about the direction",
             "“Minimising `t` squeezes it onto the largest piece.” If the sentence needs the "
             "objective to be pushed the other way, the rewrite is legal the other way and not "
             "this way."),
            ("Solve the original by some other means",
             "In two variables, enumerate the corners &mdash; and on a piecewise objective, the "
             "corners of each part on which one piece is the one that counts, because the "
             "objective is linear on each of those."),
            ("Subtract, and treat a non-zero difference as a different problem",
             "Zero is the only acceptable answer. A rewrite that reports a better objective "
             "value than the original has not improved anything; it has escaped the "
             "constraints of the question."),
        ],
        "worked": {
            "title": "Minimise the larger of two expressions, then maximise it",
            "intro": [
                "One model, two directions. The first is a legal rewrite and the second is a "
                "different problem, and the only visible difference is which way the objective "
                "is pushed."
            ],
            "lines": [
                "the region       x + y ≤ 8,   x ≤ 5,   y ≤ 6,   2x + 3y ≥ 12,",
                "                 x ≥ −4  (x free),   y ≥ 0",
                "",
                "the objective    max(2x + y,  −x + 5y),  to be minimised",
                "",
                "the rewrite      minimise t",
                "                 t − 2x −  y  ≥ 0        t is at least the first piece",
                "                 t +  x − 5y  ≥ 0        t is at least the second piece",
                "                 t free",
                "",
                "the original, by corners of each part",
                "  where piece 1 counts    (48/17, 36/17) → 132/17      (5, 2/3) → 32/3",
                "                          (32/7, 24/7)   → 88/7        (5, 3)   → 13",
                "  where piece 2 counts    (−3, 6) → 33                 (2, 6)   → 28",
                "  smallest of them        132/17",
                "",
                "the rewrite, by simplex   132/17  at  x = 48/17,  y = 36/17,  t = 132/17",
                "the two, subtracted       0",
                "",
                "now maximise the same objective",
                "  the original, by corners    33  at (−3, 6)",
                "  the rewrite, by simplex     unbounded: nothing holds t down",
                "  the two, subtracted         there is no comparison to make",
            ],
            "after": [
                "The minimised pair agree to the last fraction, and they were computed by "
                "different methods on different models. The maximised pair do not agree at all, "
                "and the reason is one sentence: minimising `t` squeezes it onto the largest "
                "piece, and maximising `t` lets it float away from every piece at once.",
                "For a faded rehearsal, take the absolute-value rewrite with the same region "
                "and the objective `2|x| + 5y`. The supplied first move is the pieces: `|x|` is "
                "the larger of `x` and `−x`, so `2|x| + 5y` is the larger of `2x + 5y` and "
                "`−2x + 5y`. Minimise it both ways &mdash; by the corners of the two parts, and "
                "by the split model &mdash; then flip to maximise and say, before running "
                "anything, which of the two will report a finite answer.",
            ],
        },
        "quiz_title": "Rewrites and the direction that licenses them",
        "quiz": [
            {"q": "The rows `t ≥ p₁(x)` and `t ≥ p₂(x)` are added and `t` is minimised. What makes `t` equal to the larger piece at the optimum?",
             "a": ["The rows, which force `t` to equal the larger piece",
                   "The direction: the rows make `t` at least the larger piece, and minimising pushes it down onto it",
                   "The requirement that `t` be free rather than non-negative",
                   "Nothing: `t` is only ever an upper bound"],
             "c": 1,
             "why": "The rows alone give `t ≥ max(p₁, p₂)`, which is satisfied by any large "
                    "value. Minimising is what removes the slack. Maximise instead and the same "
                    "rows leave the programme unbounded, which is how you can tell the rows were "
                    "never doing the work alone."},
            {"q": "Maximising `2|x| + 5y` is rewritten as maximising `2(x⁺ + x⁻) + 5y`. What does the rewrite report?",
             "a": ["The same answer, 36",
                   "Infeasible, because `x⁺` and `x⁻` cannot both be positive",
                   "Unbounded, because `x⁺` and `x⁻` can grow together without changing `x`",
                   "36, but at a different point"],
             "c": 2,
             "why": "Adding the same amount to both parts leaves `x = x⁺ − x⁻` unchanged, so "
                    "every row still holds while the objective climbs for ever. The original is "
                    "36 at `(−3, 6)`, so the rewrite is not a better answer &mdash; it is a "
                    "different problem."},
            {"q": "The first 3 units of `x` cost 5 each and every unit after that costs 2. What does the two-band model report on this region?",
             "a": ["16, the true cheapest cost",
                   "38/3, by buying from the second band without filling the first",
                   "Unbounded, because the second band has no cap",
                   "Infeasible, because the bands overlap"],
             "c": 1,
             "why": "A minimiser fills the cheaper band first, and here the cheaper band is the "
                    "second one, so the model takes `x(2) = 5` with `x(1) = 0`. The true "
                    "cheapest cost under the stated schedule is 16 at `(0, 4)`. The band model "
                    "is exact only when each later band costs more than the one before, which "
                    "is convexity."},
            {"q": "Which of the four rewrites is legal whichever way the objective is pushed?",
             "a": ["Carrying `|x|` as `x⁺ + x⁻`",
                   "Replacing a max by `t` with one row per piece",
                   "Splitting a free variable as `x⁺ − x⁻`",
                   "Splitting a quantity into price bands"],
             "c": 2,
             "why": "The difference `x⁺ − x⁻` reproduces `x` whatever the pair, so nothing has "
                    "to be pushed anywhere: minimised it reports 3 and maximised 21, both "
                    "matching the original. The other three each need the optimiser to squeeze "
                    "an auxiliary value into place."},
        ],
        "mistakes": [
            ("Assuming a rewrite works in either direction",
             "Three of the four here do not. Applied to a maximised maximum, or to `|x|` in a "
             "maximised objective, the optimiser pushes the auxiliary variable the other way "
             "and the programme becomes unbounded or reports a value the original cannot reach. "
             "The detection is cheap: solve the original another way and subtract."),
            ("Treating a better objective value as good news",
             "A rewrite that beats the original has not found a better plan &mdash; it has "
             "dropped part of the question. The falling-price band model reports 38/3 against a "
             "true 16 by buying out of a band it never filled, and nothing in the arithmetic "
             "objects."),
            ("Leaving the convexity condition unstated in the price-band rewrite",
             "Segments fill in order only when each later segment costs more than the one "
             "before. That is a condition on the data, not a property of the modelling trick, "
             "and a schedule with a volume discount in it fails it. Say the condition when you "
             "write the model, and check it against the prices in front of you."),
        ],
        "standard": ("Finish when every auxiliary variable you introduce arrives with a sentence about the direction.",
                     "You should be able to rewrite an absolute value and a min-max objective as "
                     "linear programmes, say what forces each auxiliary variable to its intended "
                     "value, solve the original another way, and read a non-zero difference as "
                     "the rewrite being a different problem."),
        "note": "Deviation variables in “Goal Programming and Deviation Variables” are the same idea once more, with a twist: there are two of them per target, only the one you mind is penalised, and the direction argument is what keeps the other from absorbing it.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "goal-programming-and-deviation-variables",
        "title": "Goal Programming and Deviation Variables",
        "module": "Keeping it linear",
        "one_line": "Turn conflicting targets into a sequence of linear programmes and name the goal that pays.",
        "summary": (
            "A target is not a constraint. It is an equation carrying two deviation variables, "
            "one for falling short and one for overshooting, of which you penalise only the one "
            "you mind. Priorities are then handled lexicographically: one linear programme per "
            "level, each freezing the deviation the level above it achieved. A preemptive goal "
            "programme is a sequence of programmes rather than one programme with weights."
        ),
        "key": [
            "3S + 4D + u₁ − o₁ = 60     the profit target,   u₁ is minded",
            "3S + 6D + u₂ − o₂ = 30     the overtime limit,  o₂ is minded",
            "      D + u₃ − o₃ = 12     the deluxe run,      u₃ is minded",
            "every u and o ≥ 0",
            "",
            "level 1:  minimise the minded deviation of the first goal",
            "level 2:  freeze what level 1 achieved as an equality, then the next goal",
        ],
        "key_label": "Three targets, six deviation variables, one programme per level",
        "concepts_intro": (
            "Two ideas are easy and one is the lesson: the frozen constraint is what makes this "
            "a sequence rather than a weighting."
        ),
        "concepts": [
            ("A target is an equation with two deviations, and you penalise one of them",
             "`3S + 4D + u₁ − o₁ = 60` holds at every feasible plan, whatever the plan is: `u₁` "
             "takes up a shortfall and `o₁` an overshoot. Minimising `u₁` alone says “I mind "
             "missing 60, I do not mind beating it”, which is what an aspiration means."),
            ("Priorities are levels, and each level hands the next an equality",
             "Level one minimises the first goal's minded deviation. Level two adds the row "
             "“that deviation equals what level one achieved” and then minimises the second "
             "goal's. The frozen row is not a suggestion: it is what stops the second level "
             "from spending the first level's achievement."),
            ("The order is the answer",
             "The same three goals, reordered, give different plans. Profit first meets the "
             "profit target and pays 30 hours of overtime; overtime first meets the overtime "
             "limit and misses profit by 30; the deluxe run first meets two goals and pays 54 "
             "hours of overtime. None of these is more correct than the others, and choosing "
             "between them is not a mathematical act."),
        ],
        "read_title": "Targets, deviations and priority levels",
        "read_intro": "Why a target should not be a hard constraint, what the two deviation variables do, and how a preemptive ordering becomes a sequence of programmes.",
        "body": [
            ("p", "A cabinet shop builds standard and deluxe units, `S` and `D`, both counted "
                  "in units a week. Its one hard constraint is 60 machine hours: `2S + 3D ≤ 60`. "
                  "It also has three things it would like: 60 pounds of profit at 3 and 4 a "
                  "unit, no more than 30 hours of overtime at 3 and 6 a unit, and 12 deluxe "
                  "units built."),
            ("p", "Written as constraints, those three are infeasible together, and "
                  "“infeasible” is a much worse answer than “missed by 12 units” when the "
                  "numbers were aspirations in the first place. The point of a goal programme "
                  "is to keep the model answerable and make the compromise visible."),
            ("def", ("Deviation variables",
                     "A target `a·x = b` is written `a·x + u − o = b` with `u ≥ 0` and "
                     "`o ≥ 0`, where `u` is the amount by which the plan falls short and `o` "
                     "the amount by which it overshoots. The objective penalises whichever of "
                     "the two the situation minds.",
                     "At most one of `u` and `o` is positive at an optimum: the penalised one "
                     "is pushed to zero if it can be, and the unpenalised one only grows when "
                     "the row forces it. That is the same direction argument the rewrites lesson "
                     "made, which is why this lesson sits beside it.")),
            ("math", [
                "  2S + 3D                 ≤ 60      machine hours, a hard constraint",
                "",
                "  3S + 4D + u₁ − o₁        = 60      pounds of profit;  u₁ is minded",
                "  3S + 6D + u₂ − o₂        = 30      hours of overtime; o₂ is minded",
                "        D + u₃ − o₃        = 12      deluxe units;      u₃ is minded",
                "",
                "  S, D, and every u and o ≥  0",
            ]),
            ("h3", "One programme per level"),
            ("p", "Take the goals in the order profit, overtime, deluxe run. Level one "
                  "minimises `u₁` and achieves 0: a plan of no standard units and 15 deluxe "
                  "ones reaches the profit target exactly. Level two adds the row `u₁ = 0` and "
                  "minimises `o₂`, which comes out at 30 hours &mdash; the profit target, now "
                  "frozen, is what makes that overtime unavoidable. Level three adds `o₂ = 30` "
                  "and minimises `u₃`, which comes out at 12: the deluxe run is what pays."),
            ("p", "Reorder and everything moves. Overtime first: `o₂ = 0` with a plan of five "
                  "deluxe units, then profit misses by 30 and the deluxe run still misses by "
                  "12. Deluxe run first: it is met, profit is met as well, and overtime is 54 "
                  "hours over its limit. Three orderings, three different sacrifices, all of "
                  "them optimal for the priorities they were given."),
            ("example", ("The frozen row is what makes it a sequence",
                         "At level two of the profit-first ordering the model contains "
                         "`u₁ = 0` as an equality. Without it, minimising `o₂` would simply "
                         "abandon the profit target &mdash; the second level would undo the "
                         "first. With it, the second level searches only among the plans that "
                         "already achieve what the first level achieved, which is what "
                         "“preemptive” means.")),
            ("h3", "The other way this goes wrong, and it is silent"),
            ("p", "The tempting alternative is one objective: minimise `u₁ + o₂ + u₃`. It "
                  "solves, and it reports a total of 42. But `u₁` is in pounds, `o₂` is in "
                  "hours and `u₃` is in units, and nothing in the arithmetic objects to adding "
                  "pounds to hours. The plan it returns is 10 standard units and no deluxe "
                  "ones, with a profit shortfall of 30, no overtime and a deluxe shortfall of "
                  "12 &mdash; which is the answer to the overtime-first ordering, arrived at "
                  "without anyone choosing that ordering."),
            ("p", "That is the failure mode to watch: a weighted objective always produces a "
                  "number, and the number encodes an exchange rate between pounds and hours "
                  "that nobody wrote down. Weights can be made to work, but only by scaling "
                  "each deviation into a common currency on purpose. Raise the weight on a "
                  "pound of profit to 4 and the weighted answer switches to the profit-first "
                  "plan, which shows how little the unscaled version was saying."),
            ("p", "None of this leaves the linear class. Every row is linear, the deviations "
                  "are ordinary non-negative variables, and each level is an ordinary linear "
                  "programme. What is new is that the answer is a sequence of solves and a "
                  "sentence: which goal was sacrificed, at which level, and by how much in its "
                  "own unit."),
        ],
        "lab": ("lp", {
            "mode": "goal",
            "panel_title": "Reorder the priorities and watch which goal pays",
            "panel_intro": "Each target carries two deviation variables and only the one the "
                           "shop minds is penalised. The levels are solved in the order you "
                           "choose, and each freezes the deviation it achieved as an equality "
                           "before the next begins. Beside it, the same three goals added into "
                           "one weighted objective in three different units, with the answer "
                           "that produces.",
        }),
        "steps_title": "Building a preemptive goal programme",
        "steps_intro": "Hard constraints first, then one target at a time, then the order &mdash; which is a decision from the situation and not from the model.",
        "steps": [
            ("Separate the hard constraints from the aspirations",
             "The machine hours are hard: no plan may exceed them. The profit, the overtime and "
             "the deluxe run are aspirations. Anything in the second list that goes into the "
             "first can make the model infeasible, and infeasible is not an answer."),
            ("Give each target two deviations and penalise only the one you mind",
             "`u` for the shortfall, `o` for the overshoot, both at or above zero. Beating a "
             "profit target is not a defect, so `o₁` is not penalised; exceeding an overtime "
             "limit is, so `o₂` is."),
            ("Put the goals in priority order, from the situation",
             "The ordering is the substance of the answer and it comes from whoever owns the "
             "problem. Record it explicitly: a goal programme with an accidental order is a "
             "model that has made somebody's decision for them."),
            ("Solve one level at a time, freezing each achieved deviation",
             "After each level, add the row “this deviation equals what was just achieved” and "
             "move on. Report every level's deviation in its own unit, and name the goal that "
             "paid for the rest."),
        ],
        "worked": {
            "title": "Three goals, two orderings, and one weighted objective",
            "intro": [
                "The same three targets and the same hard constraint throughout. Only the order "
                "changes, and then only the method."
            ],
            "lines": [
                "hard          2S + 3D ≤ 60",
                "targets       3S + 4D + u₁ − o₁ = 60      mind u₁    pounds",
                "              3S + 6D + u₂ − o₂ = 30      mind o₂    hours",
                "                    D + u₃ − o₃ = 12      mind u₃    units",
                "",
                "profit, then overtime, then the deluxe run",
                "  level 1   minimise u₁                    u₁ =  0     plan (0, 15)",
                "  level 2   u₁ = 0 frozen, minimise o₂     o₂ = 30     plan (20, 0)",
                "  level 3   o₂ = 30 frozen, minimise u₃    u₃ = 12     plan (20, 0)",
                "  the deluxe run is what pays",
                "",
                "overtime, then profit, then the deluxe run",
                "  level 1   minimise o₂                    o₂ =  0     plan (0, 5)",
                "  level 2   o₂ = 0 frozen, minimise u₁     u₁ = 30     plan (10, 0)",
                "  level 3   u₁ = 30 frozen, minimise u₃    u₃ = 12     plan (10, 0)",
                "  the profit target is what pays",
                "",
                "one weighted objective:  minimise u₁ + o₂ + u₃",
                "  total 42,  plan (10, 0),  u₁ = 30,  o₂ = 0,  u₃ = 12",
                "  which is the overtime-first answer, chosen by nobody",
            ],
            "after": [
                "The two orderings sacrifice different goals and neither is wrong. What is "
                "wrong is the third block: the weighted objective adds 30 pounds to 0 hours to "
                "12 units, calls the total 42, and silently commits to the second ordering. "
                "Nothing in the arithmetic complains, which is why this way of writing it fails "
                "quietly rather than loudly.",
                "For a faded rehearsal, put the deluxe run first, then profit, then overtime. "
                "The supplied first move is level one: minimising `u₃` needs `D = 12`, which "
                "uses 36 of the 60 machine hours. Work out what the next two levels achieve and "
                "which goal ends up paying &mdash; then reorder in the lab and check both "
                "numbers, including the overtime figure, which is larger than in either "
                "ordering above.",
            ],
        },
        "quiz_title": "Targets, deviations and levels",
        "quiz": [
            {"q": "Why is a target written with two deviation variables rather than as a constraint?",
             "a": ["Because a constraint cannot be an equality",
                   "Because three hard targets here are infeasible together, and “missed by 12 units” is a more useful answer than “infeasible”",
                   "Because deviation variables make the model linear",
                   "Because the solver cannot handle equalities"],
             "c": 1,
             "why": "The model is linear either way and equalities are perfectly ordinary rows. "
                    "The reason is that an aspiration made hard can empty the feasible region, "
                    "and a report naming what was missed and by how much is what the situation "
                    "actually wanted."},
            {"q": "At level two of the profit-first ordering, what is the frozen row `u₁ = 0` doing?",
             "a": ["Recording the answer for the report",
                   "Making the model infeasible on purpose",
                   "Restricting level two to the plans that already achieve what level one achieved",
                   "Penalising the profit shortfall a second time"],
             "c": 2,
             "why": "Without it, minimising the overtime deviation would abandon the profit "
                    "target that level one had just secured. The frozen equality is what makes "
                    "the priorities preemptive &mdash; and it is why a three-goal programme is "
                    "three linear programmes rather than one."},
            {"q": "The three deviations are minimised as one sum, `u₁ + o₂ + u₃`, with equal weights. What is the defect?",
             "a": ["The sum is non-linear",
                   "It adds pounds to hours to units, so the total encodes an exchange rate nobody chose",
                   "It cannot be solved without artificial variables",
                   "It always reports the same plan as the first ordering"],
             "c": 1,
             "why": "The objective is perfectly linear and solves without complaint, returning "
                    "42. What it does not have is a common unit, so the implied trade of one "
                    "pound of profit for one hour of overtime was never a decision. Here it "
                    "silently reproduces the overtime-first ordering."},
            {"q": "At an optimum, why is at most one of `u₁` and `o₁` positive?",
             "a": ["Because the model forbids both being positive",
                   "Because the equality row cannot hold otherwise",
                   "Because the penalised one is driven to zero whenever the row allows, and the other only grows when the row forces it",
                   "Because they are complementary by definition"],
             "c": 2,
             "why": "Nothing in the rows forbids both being positive: adding the same amount to "
                    "each keeps the equality. What removes the slack is the direction of "
                    "optimisation, exactly as in the rewrites lesson, and that is why the "
                    "unpenalised deviation is the one left free to take up the difference."},
        ],
        "mistakes": [
            ("Making a target a hard constraint",
             "Three aspirations promoted to rows here have no common solution, and the model "
             "returns “infeasible” &mdash; which tells whoever asked nothing about which target "
             "to relax or by how much. A deviation variable converts an unanswerable model into "
             "a report that names the shortfall in its own unit."),
            ("Adding deviations in different units into one objective",
             "Pounds, hours and units summed with equal weights produce a number and a plan, "
             "and the plan encodes an exchange rate nobody chose: here it quietly solves the "
             "overtime-first ordering. If weights are wanted, each deviation has to be scaled "
             "into a common currency deliberately."),
            ("Penalising both deviations of a target",
             "Minimising `u₁ + o₁` says a plan is punished for beating the profit target as "
             "well as for missing it, which turns an aspiration into a demand for exactly 60. "
             "Choose the one the situation minds, and let the other absorb whatever the row "
             "forces on it."),
        ],
        "standard": ("Finish when you can say which goal paid, at which level, and in what unit.",
                     "You should be able to separate hard constraints from targets, write each "
                     "target with two deviations and penalise the right one, solve the levels in "
                     "a stated order freezing each achieved deviation, and say what a single "
                     "weighted objective would have hidden."),
        "note": "Both lessons so far in this part have added variables to keep a model linear. The next one adds variables to a model that was already linear, for a different reason: every solver wants equalities, and turning inequalities into equalities is a modelling act whose new variables measure something real.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "standard-form-slack-and-surplus",
        "title": "Standard Form, Slack and Surplus",
        "module": "Standard form and corners",
        "one_line": "Convert a mixed-constraint minimisation to equalities and say what each new variable measures.",
        "summary": (
            "Every linear programme becomes `Ax = b` with all variables at or above zero by "
            "adding a slack to each `≤` row and <em>subtracting</em> a surplus from each `≥` "
            "row. The sign is not a convention: add a surplus instead and the variable is "
            "forced negative at every feasible point. Each new column measures something in the "
            "situation, which is why this is a modelling step and belongs here."
        ),
        "key": [
            "a·x ≤ b     →     a·x + s = b,   s ≥ 0     s = what is left unused",
            "a·x ≥ b     →     a·x − e = b,   e ≥ 0     e = the over-fulfilment",
            "a·x = b     →     unchanged, and it carries no new column",
            "",
            "x free      →     x = x⁺ − x⁻,   both ≥ 0",
            "minimise f  →     maximise −f,   then negate the answer back",
            "tight row  ⇔  its own added variable is 0",
        ],
        "key_label": "One column per inequality row, with its sign",
        "concepts_intro": (
            "Four mechanical rules and one thing that is not mechanical: every column added has "
            "a meaning in the situation, and naming it is the work."
        ),
        "concepts": [
            ("A slack is added and a surplus is subtracted, and the sign is forced",
             "`F + G ≥ 4` becomes `F + G − e₁ = 4`. At a point where the row holds, `F + G` is "
             "at least 4, so `e₁ = F + G − 4` is at or above zero. Write `+ e₁` instead and "
             "`e₁ = 4 − (F + G)` is at or below zero at every feasible point, which breaks the "
             "sign restriction the whole form rests on."),
            ("Every added column measures something in the situation",
             "The kiln's slack is unfired capacity, in pieces a day. The contract's surplus is "
             "deliveries beyond what was promised, in pieces. A column you cannot describe in a "
             "sentence about the pottery is a column you have not understood, and “Duality "
             "and Sensitivity Analysis” reads prices and ranges off exactly these columns."),
            ("Tight and zero are the same fact, written twice",
             "A row is tight at a point exactly when its own added variable is zero there. That "
             "is what makes the corner table readable: a column of zeros is the list of rows "
             "used right up, and it is a computation rather than a claim about a diagram."),
        ],
        "read_title": "Equality standard form, and what the new columns measure",
        "read_intro": "The two signs and why they are forced, the columns a solver needs and the one it only needs for the search, and the negation that is usually forgotten.",
        "body": [
            ("p", "A pottery fires pieces plain or glazed: `F` pieces fired and left plain and "
                  "`G` pieces fired and glazed, both counted in pieces a day. A delivery "
                  "contract wants at least 4 pieces, the kiln takes at most 10 firing units "
                  "where a plain piece costs 2 and a glazed piece 1, and a licence allows at "
                  "most 4 plain pieces. Plain costs 3 to make and glazed 5, and the pottery "
                  "minimises cost."),
            ("math", [
                "minimise   3F + 5G",
                "subject to   F +  G  ≥  4        the delivery contract",
                "            2F +  G  ≤ 10        the kiln",
                "             F       ≤  4        the licence",
                "             F,  G   ≥  0",
            ]),
            ("def", ("Equality standard form",
                     "A linear programme is in <strong>standard form</strong> when it reads "
                     "`maximise c·x` subject to `Ax = b` and `x ≥ 0`. Every programme reaches "
                     "it: add a <strong>slack</strong> to each `≤` row, subtract a "
                     "<strong>surplus</strong> from each `≥` row, split each free variable into "
                     "a difference of two non-negative ones, and replace a minimisation of `f` "
                     "by a maximisation of `−f`.",
                     "The transformation is exact, not an approximation: the feasible points "
                     "correspond one to one, and so do the objective values &mdash; up to the "
                     "sign, which has to be put back.")),
            ("p", "The pottery in standard form carries three added columns with meanings: "
                  "`e₁`, the pieces delivered beyond the four promised; `s₂`, the firing units "
                  "the kiln has left; and `s₃`, the plain pieces the licence still allows. It "
                  "carries a fourth column, `a₁`, which measures nothing about the pottery: an "
                  "artificial variable, there to give the search a basis to start from, zero at "
                  "every feasible point. The lab leaves it out of the table of corners for that "
                  "reason and says how many it left out."),
            ("h3", "Every added variable, at every corner"),
            ("p", "The region has four corners. Evaluating the three meaningful columns at each "
                  "of them turns the phrase “tight if and only if the added variable is zero” "
                  "into something to read rather than accept."),
            ("math", [
                "  corner        e₁        s₂        s₃      cost",
                "  (0, 4)         0         6         4       20",
                "  (0, 10)        6         0         4       50",
                "  (4, 0)         0         2         0       12       cheapest",
                "  (4, 2)         2         0         0       22",
            ]),
            ("p", "At `(4, 0)` the contract is met exactly and the licence is used right up, so "
                  "two of the three rows are tight and the kiln has 2 firing units to spare. At "
                  "`(0, 10)` the kiln is full and the contract is exceeded by 6 pieces. Reading "
                  "down a column tells you which corners a row is tight at; reading across a "
                  "row describes a corner completely."),
            ("h3", "The sign that is not a convention"),
            ("p", "Suppose the contract row had been written `F + G + e₁ = 4`. At `(0, 10)` "
                  "that needs `e₁ = −6`, and at `(4, 0)` it needs `e₁ = 0`, so the only "
                  "feasible points left are the ones where the contract is met exactly. The "
                  "programme has silently acquired a new requirement, and every method that "
                  "follows in this subject assumes `x ≥ 0` and would carry the error forward "
                  "without a murmur."),
            ("h3", "Minimise by maximising, and then negate back"),
            ("p", "The engine maximises. So the pottery's cost is handed over as "
                  "`maximise −3F − 5G`, the answer comes back as `−12`, and the page negates it "
                  "to 12. That last step is the one that gets forgotten, and a cost reported as "
                  "a negative number is a symptom worth recognising rather than a mystery. The "
                  "lab prints both numbers with their signs for exactly that reason."),
            ("p", "Flip the kiln row from a limit to a requirement &mdash; at least 10 firing "
                  "units, perhaps because the kiln is uneconomic below that &mdash; and the "
                  "form changes shape. That row now takes a surplus rather than a slack, the "
                  "model needs a second artificial column, the number of added columns rises "
                  "from four to five, and the cheapest plan moves from 12 at `(4, 0)` to 22 at "
                  "`(4, 2)`. One character in one relation, and both the columns and the answer "
                  "move."),
        ],
        "lab": ("lp", {
            "mode": "standard",
            "panel_title": "Flip the kiln row and watch its new column change kind",
            "panel_intro": "Every added column is named and given a meaning in the pottery "
                           "rather than a letter. The table underneath evaluates all of them at "
                           "every corner, so that “tight if and only if the added variable is "
                           "zero” is a column of zeros you can read rather than a sentence you "
                           "are asked to accept.",
        }),
        "steps_title": "Converting to standard form",
        "steps_intro": "Four steps, and a sentence per new column. The sentence is the part that makes this modelling rather than clerking.",
        "steps": [
            ("Take the `≤` rows first and add a slack to each",
             "`a·x + s = b` with `s ≥ 0`. Name what `s` is: unused hours, unfired capacity, "
             "shelf space still free &mdash; in the row's own unit."),
            ("Take the `≥` rows and subtract a surplus from each",
             "`a·x − e = b` with `e ≥ 0`. Check the sign on a feasible point you know: if the "
             "variable comes out negative there, the sign is wrong and every later method will "
             "inherit the error."),
            ("Deal with free variables and with the direction",
             "Split a free variable into `x⁺ − x⁻`, both at or above zero. Convert a "
             "minimisation of `f` into a maximisation of `−f`, and write down now that the "
             "answer must be negated back."),
            ("Write the sentence for each new column, then solve",
             "One line per added variable saying what it measures. A column you cannot describe "
             "is either misunderstood or artificial &mdash; and an artificial column is zero at "
               "every feasible point, so it belongs in the search and not in the report."),
        ],
        "worked": {
            "title": "The pottery in equality form, column by column",
            "intro": [
                "The conversion is four lines. What takes the space is the meaning of each new "
                "column, which is the part “Duality and Sensitivity Analysis” reads."
            ],
            "lines": [
                "as written    minimise  3F + 5G",
                "                 F +  G  ≥  4       the delivery contract",
                "                2F +  G  ≤ 10       the kiln",
                "                 F       ≤  4       the licence",
                "                 F,  G   ≥  0",
                "",
                "as equalities",
                "                 F +  G − e₁          =  4",
                "                2F +  G      + s₂     = 10",
                "                 F                + s₃ =  4",
                "            F, G, e₁, s₂, s₃          ≥  0",
                "",
                "what each new column measures",
                "  e₁   pieces delivered beyond the four the contract asks for",
                "  s₂   firing units the kiln still has free",
                "  s₃   plain pieces the licence still allows",
                "  a₁   nothing about the pottery: an artificial column, 0 wherever feasible",
                "",
                "the cheapest corner",
                "  (4, 0)     e₁ = 0    s₂ = 2    s₃ = 0        cost 12",
                "  contract tight, licence tight, kiln with 2 to spare",
                "",
                "the engine maximised  −3F − 5G  and reported  −12",
                "the cost is           12,  negated back",
            ],
            "after": [
                "Three added columns with meanings and one without: `a₁` exists so that the "
                "search has somewhere to start, and it is zero at every feasible point, so a "
                "column of zeros beside the slacks would describe the algorithm rather than the "
                "pottery. That is why the lab tabulates three columns and says it left one out.",
                "For a faded rehearsal, change the kiln row from `≤ 10` to `≥ 10`. The supplied "
                "first move is the kind of column it now takes: a requirement takes a surplus, "
                "subtracted, so `2F + G − e₂ = 10`. Work out how many added columns the form "
                "now has, which of them are artificial, and where the cheapest plan moves to "
                "&mdash; then check all three against the lab.",
            ],
        },
        "quiz_title": "Slack, surplus and the sign",
        "quiz": [
            {"q": "`F + G ≥ 4` is put into equality form. Which row is right?",
             "a": ["`F + G + e₁ = 4` with `e₁ ≥ 0`",
                   "`F + G − e₁ = 4` with `e₁ ≥ 0`",
                   "`F + G + e₁ = 4` with `e₁` free",
                   "`F + G = 4`, since a surplus adds no information"],
             "c": 1,
             "why": "At a feasible point `F + G` is at least 4, so the amount above 4 is "
                    "`F + G − 4` and it is subtracted. Adding it instead forces `e₁` to be at "
                    "or below zero everywhere feasible, which contradicts the sign restriction "
                    "the form is built on; and dropping the row entirely replaces a requirement "
                    "with an exact demand."},
            {"q": "At the corner `(0, 10)` the kiln's slack is 0 and the contract's surplus is 6. What does that describe?",
             "a": ["A kiln with 6 firing units free and a contract met exactly",
                   "A kiln full, and 6 pieces delivered beyond the four promised",
                   "An infeasible point, since one variable is zero",
                   "A tight licence row"],
             "c": 1,
             "why": "`2(0) + 10 = 10` uses the kiln exactly, so its slack is zero and the row "
                    "is tight; `0 + 10 = 10` against a requirement of 4 gives a surplus of 6. "
                    "The licence row `F ≤ 4` has slack 4 at that corner and is not tight at all."},
            {"q": "What is the artificial column `a₁` for?",
             "a": ["It measures how far the contract is exceeded",
                   "It gives the search a basis to start from, and is zero at every feasible point",
                   "It carries the negated objective",
                   "It replaces the surplus when the row is tight"],
             "c": 1,
             "why": "An artificial column exists for the first phase of the search and measures "
                    "nothing about the pottery: it is zero wherever the model is feasible. "
                    "That is why it is not tabulated beside the slacks &mdash; a column of "
                    "zeros there would say something about the algorithm and nothing about the "
                    "situation."},
            {"q": "A cost-minimising programme is solved by an engine that maximises, and the answer comes back as `−12`. What should be reported?",
             "a": ["`−12`, since that is what the engine computed",
                   "12, because the objective was negated to hand it over and must be negated back",
                   "12, because costs are always positive",
                   "Either, since the sign of an objective is a convention"],
             "c": 1,
             "why": "`minimise f` was handed over as `maximise −f`, so the reported optimum is "
                    "`−f` and the cost is its negation. The reasoning matters more than the "
                    "answer: a cost is not positive by decree, and “the sign is a convention” is "
                    "exactly the belief that loses the step."},
        ],
        "mistakes": [
            ("Adding a surplus instead of subtracting it",
             "A surplus is not a slack with another name. `a·x + e = b` on a `≥` row forces `e` "
             "to be at or below zero at every feasible point, which breaks the `x ≥ 0` the "
             "whole form is built on, and every method later in this subject assumes that form. "
             "Check the new variable's sign at one feasible point you already know."),
            ("Reporting the negated objective",
             "A minimisation handed to a maximising engine comes back with its sign flipped. "
             "Forgetting to negate it produces a cost of `−12`, which reads as a mistake in the "
             "model rather than in the bookkeeping. Write the negation down at the moment you "
             "convert, not at the moment you report."),
            ("Treating the added columns as clerical",
             "Each one measures something: unused capacity, over-delivery, unbuilt licence "
             "allowance. “Duality and Sensitivity Analysis” reads prices, ranges and reduced "
             "costs off exactly these columns, and a column whose meaning was never written "
             "down is a column that will be misread there."),
        ],
        "standard": ("Finish when every added column has a sentence about the situation beside it.",
                     "You should be able to convert a mixed-constraint minimisation to "
                     "equalities with the right sign on every new variable, evaluate all of them "
                     "at a given corner, say which rows are tight from the zeros, and negate the "
                     "objective back."),
        "note": "Standard form is what makes the next idea possible. With `m` equalities in `n + m` variables, a point is picked out by choosing which variables are zero &mdash; and that is what replaces the drawing once there are too many variables to draw.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "basic-solutions-and-corners",
        "title": "Basic Solutions and Corners",
        "module": "Standard form and corners",
        "one_line": "Enumerate every basic solution of a small programme and classify each one without looking at the picture.",
        "summary": (
            "With `m` equalities in `n + m` variables, choose which `n` variables are zero and "
            "solve the rest by row reduction: the result is a <em>basic solution</em>. One with "
            "no negative entry is a <em>basic feasible solution</em>, and the basic feasible "
            "solutions are exactly the corners. That is what replaces the drawing, and there "
            "are at most `C(n + m, m)` bases to try."
        ),
        "key": [
            "m equalities,  n + m variables",
            "choose n of them to be zero, solve the rest by row reduction",
            "",
            "no negative entry      →  basic FEASIBLE solution  =  a corner",
            "some entry negative    →  a crossing outside the region",
            "the columns dependent  →  two parallel lines, no point at all",
            "",
            "bases to try:   C(n + m, m)    here  C(5, 3) = 10",
        ],
        "key_label": "A basis, and the four things it can turn out to be",
        "concepts_intro": (
            "The hard idea is the substitution of a computation for a picture. Everything else "
            "is the four outcomes that computation can have."
        ),
        "concepts": [
            ("Choosing which variables are zero is choosing a point",
             "Set `n` of the `n + m` variables to zero and the equalities pin the rest down. "
               "Each zero variable is a line the point lies on: a decision column set to zero "
               "gives an axis, a slack column set to zero gives its row's boundary. Two zeros "
               "in two dimensions is two lines, and two lines usually cross somewhere."),
            ("A basic solution is a corner exactly when nothing came out negative",
             "The crossing of two boundary lines need not satisfy the other rows. When a basic "
               "variable solves to a negative value, the point violates that variable's own "
               "sign restriction and lies outside the region. Rejection is arithmetic on a "
               "solved value, not a glance at a diagram."),
            ("The count is why an algorithm is needed",
             "There are at most `C(n + m, m)` ways to choose a basis, which is 10 for two "
               "decisions and three rows and grows far faster than any picture. Enumerating "
               "them all is possible here and hopeless at twenty variables, which is exactly "
               "the gap “The Simplex Method” exists to close."),
        ],
        "read_title": "Bases, basic solutions, and which of them are corners",
        "read_intro": "What a basis is, the four ways one can turn out, and the count that makes enumeration untenable.",
        "body": [
            ("p", "Take the small workshop again, in equality form: `C` chairs and `T` tables, "
                  "three packing rows with slacks `s₁`, `s₂` and `s₃`. Three equalities, five "
                  "variables. Choosing two of the five to be zero leaves three unknowns and "
                  "three equations, which row reduction settles."),
            ("math", [
                "maximise  3C + 5T",
                "   C            + s₁           =  4        the carpentry shop",
                "        2T           + s₂      = 12        the finishing shop",
                "  3C + 2T                + s₃  = 18        the assembly line",
                "  C, T, s₁, s₂, s₃            ≥   0",
            ]),
            ("def", ("Basic and basic feasible solutions",
                     "For `Ax = b` with `m` rows and `n + m` variables, choose `m` columns as "
                     "the <strong>basis</strong> and set the other `n` variables to zero. If "
                     "the chosen columns are independent, the equations determine the basic "
                     "variables uniquely, and the result is a <strong>basic solution</strong>. "
                     "A basic solution with no negative entry is a <strong>basic feasible "
                     "solution</strong>.",
                     "A basic solution with a basic variable equal to zero is called "
                     "<strong>degenerate</strong>: more boundaries pass through that point than "
                     "the dimension requires, so several different bases describe it.")),
            ("p", "Every one of the ten choices is worth seeing once. Five of them are "
                  "feasible and they are exactly the five corners of the picture; three solve "
                  "to points outside it; and two are not points at all."),
            ("math", [
                "  zero variables      lines they put the point on         point     kind",
                "  s₂, s₃              2T = 12    with  3C + 2T = 18      (2, 6)    feasible",
                "  s₁, s₃               C =  4    with  3C + 2T = 18      (4, 3)    feasible",
                "  s₁, s₂               C =  4    with  2T = 12           (4, 6)    infeasible",
                "  T,  s₃               T =  0    with  3C + 2T = 18      (6, 0)    infeasible",
                "  T,  s₂               T =  0    with  2T = 12           —         singular",
                "  T,  s₁               T =  0    with   C = 4            (4, 0)    feasible",
                "  C,  s₃               C =  0    with  3C + 2T = 18      (0, 9)    infeasible",
                "  C,  s₂               C =  0    with  2T = 12           (0, 6)    feasible",
                "  C,  s₁               C =  0    with   C = 4            —         singular",
                "  C,  T                C =  0    with   T = 0            (0, 0)    feasible",
            ]),
            ("h3", "What rejects a basic solution"),
            ("p", "`(4, 6)` is where the carpentry boundary meets the finishing boundary, and "
                  "it scores 42 against the optimum's 36. It is rejected because solving its "
                  "basis gives `s₃ = −6`: the assembly row is over by six hours, recorded as a "
                  "negative slack. `(0, 9)` scores 45 and is rejected by `s₂ = −6` in the same "
                  "way. These are the crossings a picture discards by eye, and here discarding "
                  "them is a number with a sign."),
            ("p", "That matters because the picture is about to go away. A negative entry is "
                  "available in any number of variables; “outside the shaded region” is "
                  "available in two."),
            ("h3", "Two of the ten are not points"),
            ("p", "Setting `T` and `s₂` to zero asks for the intersection of `T = 0` and "
                  "`2T = 12`, which are parallel and never meet, and row reduction stops at "
                  "rank 2 out of 3. The lab reports that as two parallel lines, named, rather "
                  "than as “the matrix was singular” &mdash; the geometry is the explanation and "
                  "the rank is the symptom."),
            ("h3", "Degeneracy, and why the counts stop matching"),
            ("example", ("Three boundaries through one corner",
                         "Push the assembly line from 18 hours to 24. Now `C = 4`, `2T = 12` "
                         "and `3C + 2T = 24` all pass through `(4, 6)`. Three different bases "
                         "solve to that same point, each with a basic variable equal to zero, "
                         "and the picture has four corners while the enumeration reports six "
                         "basic feasible solutions. The extra ones are not extra points; they "
                         "are extra descriptions of one point.")),
            ("p", "The count itself is the argument for an algorithm. `C(n + m, m)` is 10 "
                  "here and the ten fit in a table. It is the number of bases to try, it comes "
                  "from “Pascal's Triangle”, and it grows fast enough that a programme with ten "
                  "decisions and ten rows has 184,756 of them. Enumerating bases is a "
                  "definition of a corner, not a method for finding the best one."),
        ],
        "lab": ("lp", {
            "mode": "basic",
            "panel_title": "Walk the bases while the picture is still there to check them",
            "panel_intro": "Choosing which variables are zero and solving the rest by row "
                           "reduction gives a basic solution; one with no negative entry is a "
                           "corner. Every basis here is reduced by the same row reduction the "
                           "elimination lessons used, with the trace for whichever one you pick "
                           "printed underneath. Push the assembly line up until three "
                           "boundaries meet at one point and watch several bases collapse onto "
                           "one corner.",
        }),
        "steps_title": "Enumerating the basic solutions",
        "steps_intro": "Standard form first, then the choosing, then the classification. The classification is where the picture stops being needed.",
        "steps": [
            ("Put the programme in equality form and count",
             "`m` rows and `n + m` variables after the slacks and surpluses. Write the count "
               "`C(n + m, m)` down before starting: it tells you how long the enumeration is "
               "and whether it is worth doing at all."),
            ("Choose which variables are zero, and name the lines that puts you on",
             "A decision column at zero is an axis; a slack column at zero is that row's "
               "boundary. Naming the two lines is what lets you predict the point before "
               "solving for it."),
            ("Solve the remaining system by row reduction",
             "If the reduction does not reach full rank, the chosen columns are dependent: the "
               "two lines are parallel and there is no basic solution for this choice at all."),
            ("Classify from the solved values, not from the diagram",
             "No negative entry is a basic feasible solution, which is a corner. A negative "
               "entry is a crossing outside the region. A zero among the basic variables is "
               "degenerate, and several bases will describe the same point."),
        ],
        "worked": {
            "title": "One basis, reduced by hand, and the entry that rejects it",
            "intro": [
                "The basis `{C, T, s₃}` sets `s₁` and `s₂` to zero, which puts the point on "
                "`C = 4` and `2T = 12`. The reduction is three rows wide and the sign at the "
                "end is the whole verdict."
            ],
            "lines": [
                "the system      C            + s₁           =  4",
                "                     2T           + s₂      = 12",
                "               3C + 2T                + s₃  = 18",
                "",
                "the basis       {C, T, s₃},   so  s₁ = 0  and  s₂ = 0",
                "",
                "     C    T   s₃  =                 operation",
                "     1    0    0     4",
                "     0    2    0    12              divide row 2 by 2",
                "     3    2    1    18              row 3 − 3(row 1)",
                "",
                "     1    0    0     4",
                "     0    1    0     6",
                "     0    2    1     6              row 3 − 2(row 2)",
                "",
                "     1    0    0     4              C  = 4",
                "     0    1    0     6              T  = 6",
                "     0    0    1    −6              s₃ = −6",
                "",
                "verdict         s₃ = −6 is negative, so (4, 6) is a basic solution",
                "                that is NOT a corner: the assembly row is over by 6 hours",
                "objective there 3(4) + 5(6) = 42,  which is more than the optimum 36",
            ],
            "after": [
                "This is the crossing that would have won. It is rejected by one negative entry "
                "in a solved system, and that is the point of the whole lesson: at three "
                "variables there is no diagram to look at, and the rejection has to be "
                "arithmetic. The optimum 36 at `(2, 6)` comes from the basis `{C, T, s₁}`, whose "
                "solved values are all at or above zero.",
                "For a faded rehearsal, take the basis `{C, s₁, s₂}`, which sets `T` and `s₃` "
                "to zero. The supplied first move is the two lines: `T = 0` is the horizontal "
                "axis and `s₃ = 0` is the assembly boundary `3C + 2T = 18`. Predict the point, "
                "reduce the system by hand, say which entry rejects it, and compare the "
                "objective value there with 36 before opening the lab's trace.",
            ],
        },
        "quiz_title": "Bases, corners and the count",
        "quiz": [
            {"q": "The workshop in equality form has three rows and five variables. How many bases are there to try?",
             "a": ["`C(5, 2) = 10`, one per pair of variables set to zero",
                   "`C(5, 3) = 10`, one per choice of three basic columns",
                   "`3 × 5 = 15`",
                   "5, one per variable"],
             "c": 1,
             "why": "A basis is a choice of `m = 3` columns out of `n + m = 5`, so the count is "
                    "`C(5, 3) = 10`. Choosing the two variables to set to zero instead gives "
                    "`C(5, 2)`, which is the same 10 &mdash; the two descriptions agree, and the "
                    "second is the one that names the lines."},
            {"q": "Solving a basis gives `C = 4`, `T = 6`, `s₃ = −6`. What is that point?",
             "a": ["A corner of the region with an objective value of 42",
                   "A degenerate corner, since one variable is negative",
                   "A basic solution that is not a corner: the assembly row is exceeded by 6 hours",
                   "Not a basic solution at all, because the reduction failed"],
             "c": 2,
             "why": "The reduction succeeded, so `(4, 6)` is a genuine basic solution; the "
                    "negative slack says the assembly row is violated there, so it lies outside "
                    "the region. Degeneracy is a basic variable equal to zero, not below it."},
            {"q": "A basis sets `T` and `s₂` to zero, and the row reduction stops at rank 2 of 3. What does that mean?",
             "a": ["The point is infeasible",
                   "The point is degenerate",
                   "`T = 0` and `2T = 12` are parallel lines, so there is no basic solution for this choice",
                   "The system has infinitely many basic feasible solutions"],
             "c": 2,
             "why": "Dependent basis columns mean the two lines the zeros put you on never "
                    "meet. There is no point to classify, which is a different outcome from a "
                    "point that exists and is rejected, and naming the two parallel lines is "
                    "more use than naming the rank."},
            {"q": "The assembly line is raised to 24 hours. The enumeration reports six basic feasible solutions and the picture has four corners. Why?",
             "a": ["Two of the bases are singular",
                   "Three boundaries pass through `(4, 6)`, so three different bases describe that one point",
                   "The count `C(5, 3)` has changed",
                   "Two corners have moved outside the region"],
             "c": 1,
             "why": "That is degeneracy. Each of the three bases through `(4, 6)` has a basic "
                    "variable equal to zero and solves to the same point, so basic feasible "
                    "solutions outnumber corners. The count of bases is still 10; what changed "
                    "is how many of them describe the same place."},
        ],
        "mistakes": [
            ("Assuming every basic solution is a corner",
             "Three of the ten here solve to points outside the region, and two of those score "
             "better than the optimum. What rejects them is a negative entry in the solved "
             "system, and that is the only form of rejection available once there is no diagram "
             "to look at."),
            ("Reading “singular” as a failure of the arithmetic",
             "Dependent basis columns mean the two lines the zeros put you on are parallel. "
             "`T = 0` and `2T = 12` never meet, so there is nothing for the reduction to find. "
             "The geometry is the explanation; the rank is only how the reduction reports it."),
            ("Treating the count of bases as a method",
             "`C(n + m, m)` is 10 for this workshop and 184,756 for ten decisions and ten rows. "
             "Enumerating bases defines what a corner is and finds the best one only on "
             "problems small enough to be uninteresting, which is the whole argument for the "
             "algorithm that comes next."),
        ],
        "standard": ("Finish when you can reject a basic solution by its solved values rather than by its position on a drawing.",
                     "You should be able to count the bases of a small programme, name the two "
                     "lines a choice of zeros puts the point on, solve one basis by row "
                     "reduction, and classify it as feasible, infeasible, singular or "
                     "degenerate with the entry that decided it."),
        "note": "A corner is now an algebraic object, and one structural fact is still missing before an algorithm can use it: why stopping is allowed at all. That is convexity, and it is what “Convexity, and Why a Local Optimum Is Global” establishes.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "convexity-and-why-a-local-optimum-is-global",
        "title": "Convexity, and Why a Local Optimum Is Global",
        "module": "Standard form and corners",
        "one_line": "Prove the feasible set convex, show the objective affine along a segment, and state what licenses an algorithm to stop.",
        "summary": (
            "The segment between two feasible points is feasible &mdash; one line of argument "
            "per inequality &mdash; and a linear objective is affine along that segment, which "
            "means its first differences are constant. Put the two together and a feasible "
            "point with no improving feasible direction cannot be beaten anywhere at all. That "
            "is a global conclusion from a local check, and it is the licence an algorithm "
            "needs in order to stop."
        ),
        "key": [
            "x, y feasible,  0 ≤ t ≤ 1   →   x + t(y − x) feasible",
            "  because  a·(x + t(y − x))  =  (1 − t)(a·x) + t(a·y)  ≤  b",
            "",
            "c·(x + t(y − x))  =  c·x + t(c·y − c·x)        affine in t",
            "  so the first differences along the segment are constant",
            "",
            "no improving feasible direction  →  optimal everywhere",
        ],
        "key_label": "Convexity, affineness, and what follows from the two",
        "concepts_intro": (
            "Two short arguments and one conclusion. The conclusion is what “The Simplex "
            "Method” spends its time cashing in."
        ),
        "concepts": [
            ("A polyhedron is convex, one inequality at a time",
             "If `a·x ≤ b` and `a·y ≤ b`, then along the segment the left-hand side is a "
             "weighted average of two numbers that are both at most `b`, so it is at most `b`. "
             "Every row survives independently, so the whole set does &mdash; and the sign "
             "restrictions are rows, so they survive too."),
            ("A linear objective is affine along a segment",
             "`c·(x + t(y − x))` is `c·x + t(c·y − c·x)`, which is a straight line in `t`. "
             "Sample it at equal steps and the first differences are equal: there is no bump in "
             "the middle of a segment for a better point to hide in."),
            ("Together they make a local check a global proof",
             "Suppose `x` is feasible and no feasible direction from `x` improves the objective. "
             "For any feasible `y`, the whole segment from `x` to `y` is feasible, and the "
             "objective along it changes at a constant rate; if `y` were better, the rate would "
             "be an improvement and the segment an improving feasible direction. So no such `y` "
             "exists."),
        ],
        "read_title": "Convexity, affineness, and the licence to stop",
        "read_intro": "The two arguments, the sampled first differences that show the second one, and what goes wrong on a set that is not convex.",
        "body": [
            ("def", ("Convex set",
                     "A set `S` is <strong>convex</strong> when for every `x` and `y` in `S` "
                     "and every `t` with `0 ≤ t ≤ 1`, the point `x + t(y − x)` is also in `S`. "
                     "That point traces the segment from `x` at `t = 0` to `y` at `t = 1`.",
                     "The definition is about every pair of points in the set, so it says "
                     "nothing at all until both ends are in it &mdash; which is why the lab "
                     "refuses to answer the question while one of the two chosen points lies "
                     "outside.")),
            ("thm", ("The feasible set of a linear programme is convex",
                     "Let `S` be the set of points satisfying finitely many linear "
                     "inequalities `aᵏ·x ≤ bᵏ`, including the sign restrictions. Then `S` is "
                     "convex.")),
            ("proof", [
                "Take `x` and `y` in `S` and `t` with `0 ≤ t ≤ 1`, and write "
                "`z = x + t(y − x)`. For any one row, "
                "`aᵏ·z = aᵏ·x + t(aᵏ·y − aᵏ·x) = (1 − t)(aᵏ·x) + t(aᵏ·y)`.",
                "Both `1 − t` and `t` are at or above zero, and both `aᵏ·x` and `aᵏ·y` are at "
                "most `bᵏ`, so `aᵏ·z ≤ (1 − t)bᵏ + t bᵏ = bᵏ`. The row holds at `z`.",
                "The argument used nothing about the other rows, so it applies to each of them "
                "separately, and `z` satisfies all of them at once. An equality row is the "
                "same argument run twice, and a sign restriction is a row like any other.",
            ]),
            ("p", "Take the region `x + y ≤ 8`, `x ≤ 5`, `y ≤ 6` with both variables at or "
                  "above zero, the objective `3x + 2y`, and the two points `(1, 1)` and "
                  "`(5, 3)`. Sampling the objective at eight equal steps along the segment "
                  "gives 5, 7, 9, 11, 13, 15, 17, 19, 21: a first difference of exactly 2, "
                  "eight times over. That constant is what affine means, and it is computed "
                  "over exact fractions of the way along rather than measured off a graph."),
            ("h3", "The stopping principle"),
            ("thm", ("No improving feasible direction means optimal",
                     "Let `S` be convex, let `c·x` be linear, and let `p` be a point of `S` "
                     "such that for every `q` in `S` no movement from `p` towards `q` improves "
                     "the objective. Then `c·p` is at least as good as `c·q` for every `q` in "
                     "`S`: `p` is optimal, globally.",
                     "The proof is one line given the two facts above. For any `q`, the segment "
                     "from `p` to `q` lies in `S` and the objective is affine along it, so if "
                     "`c·q` were better than `c·p` the objective would improve immediately on "
                     "leaving `p` in that direction &mdash; a direction that was assumed not to "
                     "improve.")),
            ("p", "This is the result an algorithm needs, and it is worth being precise about "
                  "what it replaces. The corner point theorem says an optimum can be found at a "
                  "corner. That is a statement about where to look. It says nothing whatever "
                  "about the corner you happen to be standing on, and an algorithm that stops "
                  "needs to know about that one. Convexity plus a linear objective is what "
                  "licenses stopping, and the distinction becomes urgent the moment there are "
                  "too many corners to visit."),
            ("h3", "Take the convexity away"),
            ("p", "Replace the polyhedron with two blocks and a gap: one with `x` between 0 and "
                  "3, one with `x` between 5 and 8, both with `y` between 0 and 6. Every point "
                  "of each block is feasible and the union is not convex, because a segment can "
                  "leave it."),
            ("example", ("A segment that leaves the set, and a local best that is not best",
                         "From `(1, 1)` in the western block to `(5, 3)` on the edge of the "
                         "eastern one, the segment lies inside the western block for `t` from 0 "
                         "to `1/2` and then leaves the set entirely, touching the eastern block "
                         "again only at `t = 1`. Three of the nine sampled points are outside. "
                         "Meanwhile the best corner of the western block is `(3, 6)`, worth 21, "
                         "and no step inside that block improves on it &mdash; while `(8, 6)` "
                         "in the eastern block is worth 36. A purely local check at `(3, 6)` "
                         "proves nothing at all.")),
            ("p", "Notice what did and did not survive. The objective is still linear, and "
                  "along any segment it is still affine: the first differences are constant "
                  "whether or not the segment stays in the set. What failed is the first fact, "
                  "and losing it is enough to make a local optimum a local optimum and nothing "
                  "more."),
            ("p", "Whether a segment stays inside is decided rather than sampled. For one "
                  "block, `a·(p + t(q − p)) ≤ c` is a single linear inequality in `t`, so the "
                  "whole family of rows collapses to one interval of `t`; the segment lies in "
                  "that block exactly on that interval. Two blocks give two intervals, and "
                  "whether they cover all of `t` from 0 to 1 is a question with an exact answer "
                  "&mdash; here they do not, and the gap opens at `t = 1/2`."),
            ("p", "That is the end of the modelling course, and the hand-over is precise. A "
                  "corner is an algebraic object; there are at most `C(n + m, m)` of them; and "
                  "a corner with no improving feasible direction is optimal everywhere. An "
                  "algorithm that walks from corner to adjacent corner, improving each time, "
                  "may therefore stop when no improving direction remains &mdash; and that "
                  "algorithm is “The Simplex Method”."),
        ],
        "lab": ("lp", {
            "mode": "convex",
            "panel_title": "Choose two points, then take the gap away from under them",
            "panel_intro": "The objective is evaluated at nine exact fractions of the way along "
                           "the segment and its first differences are printed beside it. "
                           "Whether the segment stays inside is decided rather than sampled: the "
                           "condition collapses to one interval of `t` per block, and a union of "
                           "two intervals either covers the whole segment or leaves a gap the "
                           "panel names.",
        }),
        "steps_title": "Proving it, and reading the proof off the lab",
        "steps_intro": "Two arguments and one conclusion, in an order that makes the conclusion one line.",
        "steps": [
            ("Take one row and one segment, and average",
             "`aᵏ·z = (1 − t)(aᵏ·x) + t(aᵏ·y)` with both weights at or above zero. A weighted "
             "average of two numbers at most `bᵏ` is at most `bᵏ`. That is the whole argument "
             "for one row."),
            ("Say why one row is enough",
             "Nothing in the step used any other row, so it holds for each of them separately "
             "and therefore for all of them at once. Sign restrictions included: they are rows."),
            ("Check the objective is affine by sampling at equal steps",
             "Evaluate `c·(x + t(y − x))` at equal fractions and take first differences. They "
             "are equal, exactly, and a difference that is nearly equal would be a bug in the "
             "arithmetic rather than a fact about the geometry."),
            ("State the conclusion, and then state what it is not",
             "No improving feasible direction implies optimal everywhere. It is not the corner "
             "point theorem, which says only that some optimum sits at a corner and nothing "
             "about the one you are standing on."),
        ],
        "worked": {
            "title": "One segment, sampled exactly, in a convex set and then in a union",
            "intro": [
                "The same two points and the same objective in both settings. The objective "
                "behaves identically; the set does not."
            ],
            "lines": [
                "the objective      3x + 2y",
                "the two points     p = (1, 1),   q = (5, 3)",
                "the segment        p + t(q − p) = (1 + 4t,  1 + 2t)",
                "the objective      3(1 + 4t) + 2(1 + 2t) = 5 + 16t",
                "",
                "  t        0    1/8   1/4   3/8   1/2   5/8   3/4   7/8    1",
                "  value    5     7     9    11    13    15    17    19    21",
                "  change    —    +2    +2    +2    +2    +2    +2    +2   +2",
                "",
                "in the convex set   x + y ≤ 8,  x ≤ 5,  y ≤ 6,  x, y ≥ 0",
                "  every sampled point is inside;  the segment lies inside for all of t",
                "  the best corner is (5, 3), worth 21, and it is best anywhere",
                "",
                "in the union of two blocks   0 ≤ x ≤ 3   and   5 ≤ x ≤ 8,   0 ≤ y ≤ 6",
                "  inside the western block for t from 0 to 1/2",
                "  inside the eastern block only at t = 1",
                "  the segment leaves the set at t = 1/2;  3 of the 9 samples are outside",
                "  best corner of the western block   (3, 6)   worth 21   a LOCAL best",
                "  best corner of the eastern block   (8, 6)   worth 36   better",
            ],
            "after": [
                "The first differences are +2 in both settings, because affineness is a fact "
                "about the objective and not about the set. What changes is whether the segment "
                "is available as evidence: in the convex set it connects any two feasible "
                "points, so a local check at one of them speaks about the other, and in the "
                "union it does not.",
                "For a faded rehearsal, keep the union and move the second point to `(2, 4)`, "
                "inside the western block. The supplied first move is which block each end lies "
                "in: both are in the west, so the segment never has to cross the gap. Predict "
                "whether the whole segment stays inside, what the first differences are, and "
                "whether `(3, 6)` can still be beaten &mdash; and then say which of the two "
                "facts of this lesson your prediction used.",
            ],
        },
        "quiz_title": "Convexity and stopping",
        "quiz": [
            {"q": "Why is the feasible set of a linear programme convex?",
             "a": ["Because it has finitely many corners",
                   "Because along a segment each row's left-hand side is a weighted average of two values that already satisfy the row",
                   "Because the objective is linear",
                   "Because it is bounded"],
             "c": 1,
             "why": "The argument is per row and uses only that `1 − t` and `t` are at or above "
                    "zero. The objective plays no part, and boundedness is irrelevant: an "
                    "unbounded covering region is convex too, and a set with finitely many "
                    "corners need not be convex &mdash; the union of two blocks has eight."},
            {"q": "The objective is sampled at eight equal steps along a segment and the first differences are all +2. What has that shown?",
             "a": ["That the objective is affine along the segment, so it has no bump in the middle",
                   "That the segment lies inside the feasible set",
                   "That the optimum is at one end of the segment",
                   "That the objective is constant"],
             "c": 0,
             "why": "Constant first differences are exactly what affine means. It says nothing "
                    "about feasibility: in the union of two blocks the differences are still "
                    "+2 while three of the samples lie outside the set. And a constant "
                    "objective would have differences of 0."},
            {"q": "What licenses an algorithm to stop at a point where no feasible direction improves the objective?",
             "a": ["The corner point theorem",
                   "That the point is a basic feasible solution",
                   "Convexity of the feasible set together with a linear objective",
                   "That the count of bases is finite"],
             "c": 2,
             "why": "Those two give the global conclusion from the local check. The corner "
                    "point theorem says only that some optimum sits at a corner &mdash; it is "
                    "about where to look, not about the corner you are on. Being basic and "
                    "feasible says where you are, not that you may stop."},
            {"q": "On the union of two blocks, `(3, 6)` is worth 21 and no step inside its own block improves on it, while `(8, 6)` is worth 36. Which fact of this lesson has failed?",
             "a": ["The objective is no longer affine along a segment",
                   "The segment between two feasible points is no longer always feasible",
                   "The set no longer has corners",
                   "The objective is no longer linear"],
             "c": 1,
             "why": "The objective is the same linear function and is still affine along every "
                    "segment. What is lost is convexity: the segment from `(3, 6)` towards "
                    "`(8, 6)` leaves the set, so it is not an available direction, and the "
                    "local check at `(3, 6)` no longer speaks about the eastern block at all."},
        ],
        "mistakes": [
            ("Using the corner point theorem as a stopping rule",
             "It says an optimum can be found at a corner. It does not say that the corner you "
             "are standing on is one, which is the question an algorithm has to answer before "
             "it halts. What answers it is convexity together with a linear objective, and the "
             "difference matters the moment there are too many corners to visit."),
            ("Reading constant first differences as evidence that the segment is feasible",
             "Affineness is a property of the objective and holds along any segment whatever, "
             "inside the set or out of it. On the union of two blocks the differences are still "
             "constant while a third of the sampled points are outside. Feasibility of the "
             "segment is a separate claim and it is the one convexity supplies."),
            ("Testing convexity by sampling points along a segment",
             "Nine samples that all lie inside are nine facts about nine points. The question "
             "is decidable instead: for one block the condition collapses to a single interval "
             "of `t`, and a union of intervals either covers the segment or leaves a gap that "
             "can be named exactly."),
        ],
        "standard": ("Finish when you can prove the set convex in one line per row and say what that licenses.",
                     "You should be able to show a polyhedron is convex, show a linear objective "
                     "is affine along a segment by its constant first differences, state the "
                     "stopping principle that follows, and say which of the two facts fails on a "
                     "set that is not convex."),
        "note": "Every model on this course was written and then handed to a solver whose workings stayed behind a curtain. “The Simplex Method” opens the curtain: it walks from one basic feasible solution to an adjacent one, improving at every step, and stops exactly when no improving direction remains &mdash; which is allowed only because of what was proved here. A lattice of whole numbers is not convex, and “Integer Programming” is where this anxiety comes back with a reason.",
    },
]
