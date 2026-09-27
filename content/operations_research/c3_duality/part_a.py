"""Duality and Sensitivity Analysis, lessons 01-05.

Construction, the two theorems, the certificate that needs no algorithm, and
the first of the four answers a final tableau already holds.

Every figure below is read off the kit -- scripts/mathpath/labs/duality.py --
rather than asserted here, and scripts/mathcheck.js executes that kit's own
JavaScript. Where the design note and the kit disagreed, the kit won.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-dual-problem",
        "title": "The Dual Problem",
        "module": "The second problem",
        "one_line": "Write the dual of a mixed-form programme with units on every price, and take the dual of the dual back to the primal.",
        "summary": (
            "Every linear programme carries a second one with a variable for each of its "
            "constraints and a constraint for each of its variables. The transformation is not "
            "a table to memorise: each direction and each sign restriction is forced by the "
            "single requirement that the prices, multiplied through the rows and added up, "
            "must bound the objective. Take the dual twice and the programme you started with "
            "comes back."
        ),
        "key": [
            "primal   max 3x1 + 5x2      x1 ≤ 4,  2x2 ≤ 12,  3x1 + 2x2 ≤ 18,  x ≥ 0",
            "dual     min 4y1 + 12y2 + 18y3      y1 + 3y3 ≥ 3,  2y2 + 2y3 ≥ 5,  y ≥ 0",
            "one price per ROW, one constraint per COLUMN, and A becomes its transpose",
            "in a max:  ≤ row → y ≥ 0      ≥ row → y ≤ 0      = row → y free",
            "           x ≥ 0 → dual row ≥        x free → dual row =",
            "units of y for a row = the objective's units ÷ that row's units",
        ],
        "key_label": "The workshop, its dual, and the rules that fixed every sign",
        "concepts_intro": (
            "The transpose is the easy half and nobody gets it wrong. The three ideas here are "
            "about the half that decides the directions and the signs."
        ),
        "concepts": [
            ("One price per row, one constraint per column",
             "A programme with `m` constraints and `n` variables has a dual with `n` "
             "constraints and `m` variables, and the pairing is fixed: the `i`-th row creates "
             "`yᵢ`, the `j`-th column creates the `j`-th dual constraint. The dual's objective "
             "coefficients are the primal's right-hand sides, and its right-hand sides are the "
             "primal's objective coefficients &mdash; the two vectors swap places."),
            ("Every direction is forced, not chosen",
             "Multiply each row by a number of its own and add the results. For that to be a "
             "valid bound on `cᵀx`, two things must hold: the multipliers must have signs that "
             "preserve the inequality when they multiply through, and the resulting combination "
             "must dominate `c` on every variable that can be positive. Those two requirements "
             "produce the whole table, row rules and column rules alike."),
            ("The units are the check that costs ten seconds",
             "A dual variable's units are the objective's units divided by its row's units: "
             "pounds per hour for an hours row, pounds per kilogram for a kilograms row. A "
             "price whose units you cannot state out loud is a price you have paired with the "
             "wrong constraint, and that is the commonest construction error there is."),
        ],
        "read_title": "Building the second programme out of the requirement that it bound the first",
        "read_intro": "One derivation, then the four row rules and the three column rules it produces, then the cases that are not the textbook case.",
        "body": [
            ("def", ("The dual problem",
                     "Given a maximisation `max cᵀx` subject to `Ax ≤ b` and `x ≥ 0`, its "
                     "<strong>dual</strong> is the minimisation `min bᵀy` subject to "
                     "`Aᵀy ≥ c` and `y ≥ 0`. The original programme is called the "
                     "<strong>primal</strong>. There is one dual variable for each primal "
                     "constraint and one dual constraint for each primal variable.",
                     "The dual variables are called <strong>prices</strong> throughout this "
                     "course, because that is what their units make them: a quantity of "
                     "objective per unit of right-hand side.")),
            ("p", "That definition is the clean case, and reading it as a recipe is how the "
                  "mixed-form cases go wrong. So here is where it comes from, on the workshop "
                  "programme above: three resources, two products, and the question of how "
                  "large `3x1 + 5x2` could possibly be."),
            ("math", [
                "choose y1, y2, y3 ≥ 0 and multiply each row by its own price:",
                "",
                "      y1 ( x1           )  ≤   4y1",
                "      y2 (       2x2    )  ≤  12y2",
                "      y3 ( 3x1 + 2x2    )  ≤  18y3",
                "      -----------------------------------------------------",
                "      (y1 + 3y3) x1 + (2y2 + 2y3) x2  ≤  4y1 + 12y2 + 18y3",
                "",
                "the left side is at least 3x1 + 5x2 for every x ≥ 0 exactly when",
                "",
                "      y1 + 3y3 ≥ 3          2y2 + 2y3 ≥ 5",
                "",
                "and then, for every feasible x,",
                "",
                "      3x1 + 5x2  ≤  4y1 + 12y2 + 18y3",
                "",
                "so the best bound this construction can give is",
                "",
                "      min 4y1 + 12y2 + 18y3   subject to those two rows, y ≥ 0",
            ]),
            ("p", "Every line of that is forced. `y ≥ 0` is needed at the first step, because "
                  "a negative multiplier would turn each `≤` into a `≥` and the sum would bound "
                  "nothing. `x ≥ 0` is needed at the second step, because "
                  "`(y1 + 3y3)x1 ≥ 3x1` requires `x1` not to be negative. And the dual is a "
                  "minimisation because a bound is only worth having as small as it can be "
                  "made. The dual is not the transpose of the primal; it is the cheapest "
                  "certificate the primal admits, and the transpose is what that turns out to "
                  "look like."),
            ("thm", ("The transformation rules",
                     "Let the primal be a maximisation. Then each row contributes a price whose "
                     "sign its direction fixes: a `≤` row gives `y ≥ 0`, a `≥` row gives "
                     "`y ≤ 0`, and an `=` row gives a `y` with no sign restriction at all. Each "
                     "column contributes a dual constraint whose direction its variable's sign "
                     "fixes: `x ≥ 0` gives a `≥` row, `x` free gives an `=` row, and `x ≤ 0` "
                     "gives a `≤` row.",
                     "If the primal is a minimisation every one of those turns over: now `≥` "
                     "rows give `y ≥ 0`, `≤` rows give `y ≤ 0`, `x ≥ 0` gives a `≤` dual row, "
                     "and the dual is a maximisation.",
                     "Each rule is the derivation above run on that shape. A `≥` row in a "
                     "maximisation is a floor; relaxing a floor cannot improve a maximum, so "
                     "its price cannot be positive. An `=` row binds in both directions, so "
                     "nothing restricts the sign of its price. A free variable can be made "
                     "negative, so the domination step must hold as an equality rather than as "
                     "an inequality.")),
            ("example", ("The workshop and its dual, side by side",
                         "The primal reads `max 3x1 + 5x2` subject to `x1 ≤ 4` (cutting), "
                         "`2x2 ≤ 12` (glazing), `3x1 + 2x2 ≤ 18` (assembly), `x ≥ 0`. Its dual "
                         "reads `min 4y1 + 12y2 + 18y3` subject to `y1 + 3y3 ≥ 3` (the `x1` "
                         "column), `2y2 + 2y3 ≥ 5` (the `x2` column), `y ≥ 0`.",
                         "Read the first dual row aloud: the cutting and assembly capacity that "
                         "one unit of `x1` consumes must be worth at least the 3 that unit "
                         "earns. That sentence is the dual constraint, and it is why the "
                         "direction is `≥` rather than `≤`.")),
            ("h3", "The three cases that are not the textbook case"),
            ("p", "A programme with only `≤` rows and only non-negative variables is the one "
                  "every textbook prints, and it is the one that teaches least, because in it "
                  "the rules are invisible. The lab ships a preset with a cap, a floor, a quota "
                  "and a variable free to go negative precisely so that all three of the "
                  "awkward rules have to be applied at once."),
            ("example", ("A cap, a floor, a quota and a free variable",
                         "`max 4u + 3v` subject to `2u + v ≤ 10` (capacity), `u − v ≥ 1` "
                         "(balance), `u + v = 4` (quota), `u ≥ 0` and `v` free. The dual is "
                         "`min 10y1 + y2 + 4y3` subject to `2y1 + y2 + y3 ≥ 4` (the `u` column) "
                         "and `y1 − y2 + y3 = 3` (the `v` column), with `y1 ≥ 0`, `y2 ≤ 0` and "
                         "`y3` free.",
                         "Three separate rules did that. The `≥` row turned `y2` non-positive, "
                         "the `=` row left `y3` unrestricted, and the free `v` turned its dual "
                         "row into an equality. The lab prints the sentence that fixed each one "
                         "on the link joining the pair, and the programme solves to `z* = 18` at "
                         "`u = 6`, `v = −2` &mdash; a negative variable at the optimum, which is "
                         "what declaring it free was for.")),
            ("p", "Take the dual of that dual and the original programme comes back, sign for "
                  "sign and direction for direction. That is not a special case of the tidy "
                  "shape: it is a property of the four rules, and it holds on the minimisation, "
                  "on the floor, on the quota and on the free variable alike. The lab's last "
                  "control runs the construction twice and reports whether the result agrees "
                  "with what it started from &mdash; and on every preset it does."),
            ("example", ("A minimisation, where every direction turns over",
                         "`min 2x + 3y` subject to `x + y ≥ 4` (protein), `x ≤ 3` (supply), "
                         "`y ≥ 1` (oats), `x, y ≥ 0` has the dual `max 4y1 + 3y2 + y3` subject "
                         "to `y1 + y2 ≤ 2` (the `x` column) and `y1 + y3 ≤ 3` (the `y` column), "
                         "with `y1 ≥ 0`, `y2 ≤ 0`, `y3 ≥ 0`.",
                         "Everything has flipped and nothing has been memorised. In a "
                         "minimisation the requirement to be met is the `≥` row, so that is the "
                         "row with a non-negative price; the `≤` row is now the cap whose "
                         "relaxation cannot help, so its price is non-positive; and the dual "
                         "constraints say that what a unit is worth must not exceed what it "
                         "costs.")),
        ],
        "lab": ("duality", {
            "mode": "construct",
            "preset": "workshop",
            "panel_title": "Choose a programme, and which one to take the dual of",
            "panel_intro": "Each row is drawn joined to the price it creates and each variable "
                           "to the dual constraint it creates, with the rule that fixed the "
                           "direction written on the link. The last control takes the dual "
                           "twice: the programme that comes back is the one you started from, "
                           "on the free variable and the quota as much as on the tidy caps.",
        }),
        "steps_title": "Writing the dual of something you have been handed",
        "steps_intro": "Count first, then transpose, then apply one rule per row and one per column. The units are the last step and they catch the pairing errors.",
        "steps": [
            ("Count the rows and the columns before writing anything",
             "`m` rows means `m` dual variables; `n` variables means `n` dual constraints. If "
             "your dual has a different count in either direction you have paired a price with "
             "a variable, which is the error the count catches for free."),
            ("Swap the objective and the right-hand sides, and turn the objective over",
             "The primal's `b` becomes the dual's objective coefficients and the primal's `c` "
             "becomes the dual's right-hand sides. A maximisation becomes a minimisation and "
             "the other way round."),
            ("Give each row its price, with the sign its direction forces",
             "In a maximisation: `≤` gives `y ≥ 0`, `≥` gives `y ≤ 0`, `=` gives `y` free. "
             "Reach for the reason rather than the table &mdash; a floor you would like to "
             "relax cannot be worth a positive amount &mdash; because the reason survives a "
             "minimisation and the table does not."),
            ("Give each column its constraint, with the direction its variable forces",
             "The `j`-th dual row has the `j`-th column of `A` as its coefficients and `cⱼ` as "
             "its right-hand side. A non-negative variable gives `≥` in a maximisation's dual; "
             "a free variable gives `=`."),
            ("Put units on every price, and then take the dual again",
             "State each price's units aloud: objective units per unit of that row. Then run "
             "the construction on what you have written. If it does not return the programme "
             "you started from, the error is in the sign or direction of whichever row or "
             "column has changed."),
        ],
        "worked": {
            "title": "The dual of the workshop, derived rather than looked up",
            "intro": [
                "Nothing below is taken from a table. The two dual constraints appear as the "
                "conditions under which the combination of rows is a bound at all, and the "
                "objective appears as the wish to make that bound small."
            ],
            "lines": [
                "primal      max 3x1 + 5x2",
                "            cutting     x1          ≤   4",
                "            glazing          2x2    ≤  12",
                "            assembly   3x1 + 2x2    ≤  18",
                "                              x1, x2 ≥ 0",
                "",
                "count       3 rows  → 3 prices y1, y2, y3",
                "            2 columns → 2 dual constraints",
                "",
                "combine     y1(x1) + y2(2x2) + y3(3x1 + 2x2)",
                "               ≤ 4y1 + 12y2 + 18y3            needs y ≥ 0",
                "",
                "collect     x1 coefficient:  y1 + 3y3",
                "            x2 coefficient:  2y2 + 2y3",
                "",
                "dominate    y1 + 3y3 ≥ 3                      needs x1 ≥ 0",
                "            2y2 + 2y3 ≥ 5                     needs x2 ≥ 0",
                "",
                "dual        min 4y1 + 12y2 + 18y3",
                "            y1 + 3y3   ≥ 3      the x1 column",
                "            2y2 + 2y3  ≥ 5      the x2 column",
                "            y1, y2, y3 ≥ 0",
                "",
                "units       profit is in pounds; cutting is in hours",
                "            y1 is pounds per hour of cutting",
                "",
                "check       take the dual of that dual:",
                "            3 dual columns → 3 variables      2 dual rows → 2 prices",
                "            max 3x1 + 5x2 subject to the three original rows   ✓",
            ],
            "after": [
                "The two `needs` annotations are the whole content of the sign rules. Drop "
                "`y ≥ 0` and the first line stops being an inequality in the right direction; "
                "drop `x ≥ 0` and the domination step stops being valid. Everything else is "
                "bookkeeping.",
                "For a faded rehearsal, do the same on the bakery: `max 5x + 4y` subject to "
                "`6x + 4y ≤ 24`, `x + 2y ≤ 6`, `x + y ≥ 2`, `x, y ≥ 0`. The supplied first move "
                "is that the third row, being a floor in a maximisation, gets the price the "
                "derivation cannot allow to be positive. Write both dual rows, state the sign "
                "of all three prices, and then check your answer against the lab's `bakery` "
                "preset before opening the quiz.",
                "If you want the harder rehearsal, take the dual of the minimisation preset "
                "and then take the dual of your answer. Everything reverses twice, which is the "
                "only way to be sure you applied rules rather than recalled a shape.",
            ],
        },
        "quiz_title": "Rows, columns, directions and signs",
        "quiz": [
            {"q": "Which is the dual of `max 3x1 + 5x2` subject to `x1 ≤ 4`, `2x2 ≤ 12`, `3x1 + 2x2 ≤ 18`, `x ≥ 0`?",
             "a": ["`max 4y1 + 12y2 + 18y3` subject to `y1 + 3y3 ≤ 3`, `2y2 + 2y3 ≤ 5`, `y ≥ 0`",
                   "`min 4y1 + 12y2 + 18y3` subject to `y1 + 3y3 ≥ 3`, `2y2 + 2y3 ≥ 5`, `y ≥ 0`",
                   "`min 3y1 + 5y2` subject to `y1 + 3y2 ≥ 4`, `2y1 + 2y2 ≥ 12`, `y ≥ 0`",
                   "`min 4y1 + 12y2 + 18y3` subject to `y1 + 3y3 ≥ 3`, `2y2 + 2y3 ≥ 5`, `y` free"],
             "c": 1,
             "why": "The first choice is the named misconception: the matrix has been transposed "
                    "and everything else copied across, so the objective still maximises and the "
                    "rows still point the same way. It bounds nothing. The third has paired the "
                    "prices with the variables instead of the rows, which the count catches: "
                    "three rows must give three prices. The fourth has the right shape and no "
                    "sign restriction, and without `y ≥ 0` the first step of the derivation "
                    "fails."},
            {"q": "In a maximisation, what sign restriction does the price of a `≥` row carry?",
             "a": ["`y ≥ 0`", "`y ≤ 0`", "`y` is unrestricted in sign",
                   "It depends on the sign of that row's right-hand side"],
             "c": 1,
             "why": "A `≥` row in a maximisation is a floor. Relaxing a floor can only enlarge "
                    "the feasible region, and enlarging it cannot lower a maximum, so the row "
                    "cannot be worth a positive amount &mdash; and in the derivation, "
                    "multiplying a `≥` row by a non-positive number is what turns it into the "
                    "`≤` the sum needs. An `=` row is the one whose price is unrestricted."},
            {"q": "A workshop maximises profit in pounds, and its assembly row is measured in hours. What are the units of the assembly row's price?",
             "a": ["Hours", "Pounds", "Pounds per hour", "Hours per pound"],
             "c": 2,
             "why": "A price is the objective's units divided by its row's units, so pounds per "
                    "hour. This is worth doing out loud on every row: if the answer is not a "
                    "rate of objective per unit of that constraint, the price has been paired "
                    "with the wrong row and every number after it will be wrong in a way the "
                    "arithmetic cannot show you."},
            {"q": "You take the dual of the dual of a programme that has a `≥` row, an `=` row and a variable free to go negative. What do you get?",
             "a": ["The programme you started from",
                   "The programme you started from, with every inequality reversed",
                   "A third programme, different from both but with the same optimal value",
                   "The programme you started from only if you first rewrite the `=` row as two inequalities"],
             "c": 0,
             "why": "The four rules undo each other, and the awkward shapes are where that is "
                    "visible rather than where it fails: a `≥` row gives a non-positive price, "
                    "whose own dual row comes back as a `≥` row. The lab's toggle runs the "
                    "construction twice on every preset and reports agreement row by row and "
                    "sign by sign. Splitting the `=` row would work and is not needed."},
        ],
        "mistakes": [
            ("Transposing the matrix and copying everything else across",
             "This is the error the lesson exists for. `A` becomes `Aᵀ`, `b` and `c` swap, and "
             "then the objective is left maximising and the rows left pointing the same way. "
             "The result is a programme that bounds nothing at all, and you find out only when "
             "its optimal value comes out below the primal's. Every direction and every sign has "
             "to be decided separately, from the requirement that the combination be a bound."),
            ("Pairing a price with a variable instead of a row",
             "A programme with three rows and two variables has a dual with three variables and "
             "two rows, and getting that backwards produces a dual of the wrong size. Count "
             "before you write: the dual's variable count is the primal's row count, always. "
             "The units check catches the same error a second way, because a price paired with a "
             "variable has no sensible units."),
            ("Giving an equality row a non-negative price",
             "An `=` row binds from both sides, so nothing in the derivation restricts the sign "
             "of its price, and at a real optimum it often is negative. Writing `y ≥ 0` there "
             "silently removes feasible dual points, and the dual you have written then has a "
             "larger minimum than the primal's maximum &mdash; a gap that looks like an "
             "arithmetic slip and is a modelling one."),
        ],
        "standard": ("Finish when you can write the dual of a mixed-form programme without looking at a table of rules.",
                     "You should be able to take the dual of a maximisation and of a "
                     "minimisation, apply the `≥` and `=` row rules and the free-variable column "
                     "rule from the reason rather than from recall, state the units of every "
                     "price, and take the dual of your own answer to get back what you started "
                     "with."),
        "note": 'A price has units, and stating them takes ten seconds. Pounds per hour of cutting, pounds per kilogram of flour: a dual variable whose units you cannot say is a dual variable you have attached to the wrong constraint. The next lesson, “Weak Duality and Certificates”, is where the bound this construction was built to produce becomes a proof about the primal that costs nothing to check.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "weak-duality-and-certificates-of-optimality",
        "title": "Weak Duality and Certificates",
        "module": "The second problem",
        "one_line": "Check a pair of points, compute the chain, and state exactly what the gap proves and what it does not.",
        "summary": (
            "For any primal-feasible plan and any dual-feasible set of prices, the plan's value "
            "is at most the middle quantity and the middle quantity is at most the prices' "
            "value. Two inequalities, each coming from one sign restriction, and between them "
            "they bracket the optimum. A single feasible set of prices is therefore a proof "
            "about the primal that cost no solving at all, and when the two ends agree, both "
            "points are proved optimal with no further argument."
        ),
        "key": [
            "cᵀx ≤ yᵀAx ≤ bᵀy        every primal-feasible x, every dual-feasible y",
            "left link needs   Aᵀy ≥ c  and  x ≥ 0",
            "right link needs  Ax ≤ b   and  y ≥ 0",
            "workshop  x = (1, 1), y = (0, 2, 1):   8 ≤ 9 ≤ 42      gaps 1 and 33",
            "equal ends:  cᵀx = bᵀy  ⟹  both points optimal, no further argument",
            "a minimisation runs the same chain downwards:  bᵀy ≤ yᵀAx ≤ cᵀx",
        ],
        "key_label": "One chain, two links, and one sign restriction behind each",
        "concepts_intro": (
            "There is one inequality here and it has two halves. What is new is not the algebra "
            "but what a single feasible point of the second programme is now worth."
        ),
        "concepts": [
            ("The chain has two links and each needs one sign restriction",
             "`yᵀAx` is the same number read two ways. Grouped as `(Aᵀy)ᵀx` it is at least "
             "`cᵀx`, because `Aᵀy ≥ c` and `x ≥ 0`. Grouped as `yᵀ(Ax)` it is at most `bᵀy`, "
             "because `Ax ≤ b` and `y ≥ 0`. Neither half uses optimality, an algorithm, or any "
             "property of the points beyond feasibility."),
            ("A feasible set of prices is a certificate",
             "Any dual-feasible `y` &mdash; guessed, inherited from a previous solve, produced "
             "by a heuristic &mdash; proves that no feasible plan earns more than `bᵀy`. That is "
             "a claim about every point of a region you have not enumerated, from one point you "
             "did not have to solve for, and it is the property everything later on this path "
             "lives on."),
            ("Equal ends prove both points at once",
             "If a feasible pair has `cᵀx = bᵀy`, then no plan beats `x` and no prices beat "
             "`y`, so both are optimal. That is the whole proof: two lines of it, and it needs "
             "no pivots. A gap, by contrast, brackets the optimum without locating it."),
        ],
        "read_title": "The chain, the two sign restrictions behind it, and what a gap is worth",
        "read_intro": "Where the two inequalities come from, why a guessed set of prices is already a proof, and what happens when you try to beat the bound.",
        "body": [
            ("p", "Take any plan that satisfies the primal's constraints and any set of prices "
                  "that satisfies the dual's. Neither has to be optimal and neither has to have "
                  "been solved for. Then write down the single number `yᵀAx` and read it two "
                  "ways."),
            ("math", [
                "     y'Ax  =  (A'y)' x   ≥   c'x        because A'y ≥ c  and  x ≥ 0",
                "     y'Ax  =  y' (Ax)    ≤   b'y        because Ax ≤ b   and  y ≥ 0",
                "",
                "     therefore        c'x  ≤  y'Ax  ≤  b'y",
                "",
                "workshop, x = (1, 1) and y = (0, 2, 1):",
                "",
                "     c'x  = 3(1) + 5(1)                      =  8",
                "     Ax   = (1, 2, 5)",
                "     y'Ax = 0(1) + 2(2) + 1(5)               =  9",
                "     b'y  = 4(0) + 12(2) + 18(1)             = 42",
                "",
                "     8  ≤  9  ≤  42          gap 1 at the left link, 33 at the right",
            ]),
            ("thm", ("Weak duality",
                     "If `x` is feasible for the primal maximisation and `y` is feasible for its "
                     "dual, then `cᵀx ≤ bᵀy`. In particular every dual-feasible `y` gives an "
                     "upper bound on the primal optimum, and every primal-feasible `x` gives a "
                     "lower bound on the dual optimum.",
                     "If `cᵀx = bᵀy` for such a pair, then `x` is optimal for the primal and `y` "
                     "is optimal for the dual.")),
            ("proof", [
                "Both inequalities of the chain hold by the two sign arguments above, so "
                "`cᵀx ≤ bᵀy` for every feasible pair. Now suppose `cᵀx = bᵀy`. Any feasible `x̂` "
                "satisfies `cᵀx̂ ≤ bᵀy = cᵀx`, so no feasible plan earns more than `x` does, and "
                "`x` is optimal. Any feasible `ŷ` satisfies `bᵀŷ ≥ cᵀx = bᵀy`, so no feasible "
                "prices value the resources below `y`, and `y` is optimal.",
                "Note what is absent. No algorithm was run, no basis was mentioned, and nothing "
                "was assumed about how either point was obtained.",
            ]),
            ("example", ("A bound from prices nobody solved for",
                         "The bakery maximises `5x + 4y` subject to `6x + 4y ≤ 24`, "
                         "`x + 2y ≤ 6` and `x + y ≥ 2`. Guess the crudest prices that work: "
                         "`y = (1, 0, 0)`. Check dual feasibility &mdash; `6(1) ≥ 5` for the `x` "
                         "column and `4(1) ≥ 4` for the `y` column &mdash; and the certificate "
                         "is valid.",
                         "It says no plan earns more than `bᵀy = 24`. The plan `x = (1, 1)` "
                         "earns 9, so the chain reads `9 ≤ 10 ≤ 24`. The true optimum is 21, so "
                         "the guess was not sharp; it was, nonetheless, a proved bound obtained "
                         "by inspecting one column at a time.")),
            ("h3", "What a gap proves, and what it does not"),
            ("p", "A chain reading `8 ≤ 9 ≤ 42` establishes that the optimum lies between 8 and "
                  "42 and says nothing at all about where. On the workshop it is 36, close to "
                  "the upper end; nothing in the chain could have told you that. What the two "
                  "links do give you is an account of where the gap went: 1 of it is the amount "
                  "by which the prices overvalue what this plan actually consumes, and 33 of it "
                  "is the amount of resource the plan leaves unused at those prices."),
            ("p", "This is also why a gap is not evidence against either point. One end of a "
                  "wide chain can already be optimal &mdash; the plan could be perfect and the "
                  "prices dreadful &mdash; and the chain cannot distinguish that case from one "
                  "where both are poor. Only a closed gap says anything about either point on "
                  "its own."),
            ("h3", "Trying to beat the bound"),
            ("p", "The lab invites you to type a plan that earns more than the prices allow, and "
                  "refuses every attempt by naming which of the two points is not feasible. "
                  "That refusal is the theorem. Type `x = (10, 10)` against the workshop's "
                  "optimal prices and the numbers do read `80` against `36` &mdash; and the "
                  "panel reports that all three rows are broken, so the plan was never a "
                  "candidate."),
            ("example", ("Prices that are not a certificate",
                         "Offer `y = (0, 0, 1)` for the workshop. Then `bᵀy = 18`, and the "
                         "optimal plan `(2, 6)` earns 36, which is more. Weak duality has not "
                         "failed: the `x2` dual constraint asks for `2y2 + 2y3 ≥ 5` and these "
                         "prices give 2, so `y` is not dual feasible and was never a "
                         "certificate.",
                         "This is the check to run first and the one most often skipped. A "
                         "number is a bound because its point is feasible, and feasibility is "
                         "one substitution per dual constraint.")),
            ("h3", "The same chain on a minimisation"),
            ("example", ("A certificate that bounds from below",
                         "`min 2x + 3y` subject to `x + y ≥ 4`, `x ≤ 3`, `y ≥ 1` has the dual "
                         "`max 4y1 + 3y2 + y3` subject to `y1 + y2 ≤ 2`, `y1 + y3 ≤ 3`, with "
                         "`y1, y3 ≥ 0` and `y2 ≤ 0`. At `x = (3, 2)` and `y = (1, 0, 0)` the "
                         "chain reads `4 ≤ 5 ≤ 12`, with the primal value at the top.",
                         "Everything has turned over: now the dual value is the lower bound and "
                         "the primal value the upper one, and a certificate proves that no plan "
                         "costs less than 4. The optimum is 9. A kit that had hard-coded the "
                         "direction would report the wrong claim here rather than the wrong "
                         "number, which is the harder failure to notice.")),
            ("p", "This one inequality reappears twice more on this path wearing different "
                  "nouns. In Networks: Flows, Paths and Assignments it is the statement that any cut's "
                  "capacity "
                  "bounds any flow, with the cut playing the part of the prices. In Integer "
                  "Programming it is the optimality gap that lets a search stop early, with the "
                  "relaxation's value playing the part of `bᵀy`. Both of those are this chain, "
                  "and both cite it."),
        ],
        "lab": ("duality", {
            "mode": "certificate",
            "preset": "workshop",
            "panel_title": "Type a plan and a set of prices",
            "panel_intro": "Neither box has to be optimal and neither has to be solved for. "
                           "While both are feasible the chain holds and its two ends bracket the "
                           "answer. Try to type a plan that beats the bound: every attempt is "
                           "refused, and the panel names the link that forbids it.",
        }),
        "steps_title": "Turning a pair of points into a statement",
        "steps_intro": "Feasibility first, both times. The three numbers are worthless if either point has not been checked.",
        "steps": [
            ("Check the plan against every primal row and every sign",
             "Substitute and compare, one row at a time, and check the sign restrictions too. A "
             "plan with a negative entry fails before any row is reached, and the lab reports "
             "that as a sign failure rather than as a broken constraint."),
            ("Check the prices against every dual constraint and every sign",
             "One substitution per primal column, plus the sign rule each row's direction "
             "imposed. This is the step that gets skipped, and skipping it is how a number that "
             "bounds nothing gets quoted as a bound."),
            ("Compute all three quantities, not just the two ends",
             "`cᵀx`, then `Ax` and `yᵀ(Ax)`, then `bᵀy`. The middle quantity is what splits the "
             "gap into the part the prices overvalue and the part the plan leaves unused, and "
             "computing it is how you check your own arithmetic."),
            ("State the conclusion in the form the chain licenses",
             "With a gap: the optimum lies between these two numbers. With no gap: both points "
             "are optimal, and no algorithm was needed. Never say the optimum is near the "
             "middle quantity &mdash; it need not be."),
        ],
        "worked": {
            "title": "One guessed pair, then the pair that closes",
            "intro": [
                "The first pair is deliberately poor: a plan making one of each product and "
                "prices somebody rounded off. It still proves something. The second pair is the "
                "optimum, and the point of putting them side by side is that the second proof "
                "is no harder than the first."
            ],
            "lines": [
                "workshop    max 3x1 + 5x2      cutting  x1      ≤  4",
                "                               glazing     2x2  ≤ 12",
                "                               assembly 3x1+2x2 ≤ 18",
                "dual        min 4y1 + 12y2 + 18y3    y1 + 3y3 ≥ 3",
                "                                     2y2 + 2y3 ≥ 5",
                "",
                "pair one    x = (1, 1)          y = (0, 2, 1)",
                "",
                "  feasible?  1 ≤ 4 ✓    2 ≤ 12 ✓    5 ≤ 18 ✓    x ≥ 0 ✓",
                "             0 + 3(1) = 3 ≥ 3 ✓     2(2) + 2(1) = 6 ≥ 5 ✓    y ≥ 0 ✓",
                "",
                "  c'x  = 3 + 5                            =  8",
                "  y'Ax = 0(1) + 2(2) + 1(5)               =  9",
                "  b'y  = 4(0) + 12(2) + 18(1)             = 42",
                "",
                "  8 ≤ 9 ≤ 42        so 8 ≤ z* ≤ 42, and nothing sharper",
                "  left gap  9 − 8  = 1     the prices overvalue what this plan uses",
                "  right gap 42 − 9 = 33    the resource this plan leaves unused",
                "",
                "pair two    x = (2, 6)          y = (0, 3/2, 1)",
                "",
                "  feasible?  2 ≤ 4 ✓    12 ≤ 12 ✓   18 ≤ 18 ✓",
                "             0 + 3 = 3 ≥ 3 ✓        2(3/2) + 2 = 5 ≥ 5 ✓",
                "",
                "  c'x  = 3(2) + 5(6)                      = 36",
                "  b'y  = 4(0) + 12(3/2) + 18(1)           = 36",
                "",
                "  36 ≤ 36        gap 0, so BOTH points are optimal",
            ],
            "after": [
                "The second half is a complete proof of optimality for a two-variable programme, "
                "and it consists of eight substitutions and two dot products. No pivot, no "
                "tableau, no corner enumeration. That is what a certificate buys.",
                "It also leaves an obvious question, which is the next lesson's: where did "
                "`y = (0, 3/2, 1)` come from? Guessing prices that close the gap exactly is not "
                "something you would want to rely on. They were read off the final tableau of "
                "the primal solve, and “Strong Duality from the Final Tableau” is where that "
                "stops being a coincidence.",
                "For a faded rehearsal, take the bakery: `max 5x + 4y` subject to "
                "`6x + 4y ≤ 24`, `x + 2y ≤ 6`, `x + y ≥ 2`. The supplied move is the plan "
                "`x = (1, 1)`. Find any dual-feasible set of prices by inspection, compute all "
                "three quantities, and write down the bracket you have proved. Then compare it "
                "with the true optimum of 21 and say how much of your gap each link accounts "
                "for.",
            ],
        },
        "quiz_title": "What the chain licenses",
        "quiz": [
            {"q": "Which pair of conditions produces the LEFT inequality, `cᵀx ≤ yᵀAx`?",
             "a": ["`Ax ≤ b` and `y ≥ 0`", "`Aᵀy ≥ c` and `x ≥ 0`", "`x ≥ 0` and `y ≥ 0`",
                   "Both points feasible and `cᵀx = bᵀy`"],
             "c": 1,
             "why": "Group the middle quantity as `(Aᵀy)ᵀx`. Dual feasibility gives "
                    "`Aᵀy ≥ c` coefficient by coefficient, and multiplying a larger coefficient "
                    "by a non-negative `x` gives a larger total &mdash; so `x ≥ 0` is needed "
                    "too. The first choice is exactly the other link, obtained by grouping the "
                    "same number as `yᵀ(Ax)`."},
            {"q": "You are handed a dual-feasible `y` for a maximisation, with `bᵀy = 30`. What does that prove?",
             "a": ["The primal optimum is 30", "The primal optimum is at most 30",
                   "The primal optimum is at least 30",
                   "Nothing, until the dual has been solved to optimality"],
             "c": 1,
             "why": "Weak duality gives `cᵀx ≤ bᵀy` for every feasible plan, so 30 is an upper "
                    "bound and the optimum could be far below it. The last choice is the "
                    "misconception this lesson exists to break: the bound comes from "
                    "feasibility alone, and where `y` came from is irrelevant."},
            {"q": "At a feasible pair the chain reads `8 ≤ 9 ≤ 42`. Which statement does weak duality license?",
             "a": ["The optimum is 9", "The optimum lies between 8 and 42",
                   "The optimum is nearer 8 than 42",
                   "The optimum is 42 less the gap at the right link"],
             "c": 1,
             "why": "Two inequalities bracket and do not locate. On this instance the optimum is "
                    "36, close to the upper end, which is exactly why the third choice is not "
                    "something the chain can say. The middle quantity is an accounting device "
                    "for splitting the gap, not an estimate of the answer."},
            {"q": "Someone offers `y = (0, 0, 1)` as a certificate for the workshop: `bᵀy = 18`, while the plan `(2, 6)` earns 36. What has gone wrong?",
             "a": ["The plan is infeasible", "The prices are infeasible: they do not cover the `x2` column",
                   "Weak duality fails when one of the prices is zero",
                   "The chain runs the other way on this programme"],
             "c": 1,
             "why": "The `x2` dual constraint asks for `2y2 + 2y3 ≥ 5` and these prices give "
                    "`0 + 2 = 2`, so `y` is not dual feasible and never bounded anything. The "
                    "plan `(2, 6)` is perfectly feasible, and a zero price is fine &mdash; the "
                    "optimal prices have one. The lab names which of the two points it is "
                    "refusing on every attempt."},
        ],
        "mistakes": [
            ("Believing a set of prices is only worth having if you solved for it",
             "The bound comes from feasibility and nothing else. A guess, a set of prices left "
             "over from a similar problem, a number a heuristic produced &mdash; if it satisfies "
             "the dual constraints and their signs, it proves something about every feasible "
             "plan at once. This is the property that makes branch-and-bound affordable later, "
             "and it is free here."),
            ("Quoting a bound without checking dual feasibility",
             "`bᵀy` is a number for any `y` at all, and it is a bound only when `y` is feasible. "
             "Skipping the check is how `18` gets quoted as an upper bound for a programme whose "
             "optimum is 36. The check is one substitution per primal column plus one sign per "
             "row, and it is the cheapest thing in the lesson."),
            ("Reading a gap as evidence that neither point is any good",
             "A wide chain is compatible with one end being exactly optimal: the plan may be "
             "perfect while the prices are crude, and the chain cannot tell you which. What a "
             "gap establishes is a bracket, and what closes it is the only thing that certifies "
             "either point."),
        ],
        "standard": ("Finish when you can hand someone a set of prices and say precisely what it proves.",
                     "You should be able to check a pair for feasibility on both programmes, "
                     "compute all three quantities of the chain, name which sign restriction "
                     "produces each link, split a gap into its two parts, and state the "
                     "conclusion as a bracket or as a proof of optimality &mdash; without ever "
                     "saying the optimum is near the middle number."),
        "note": 'This inequality is the one result on the course that gets reused under other names. Networks: Flows, Paths and Assignments states it as “any cut\'s capacity bounds any flow”; Integer Programming states it as the optimality gap that lets a search prune a subtree without exploring it. Both are this chain with different nouns, and both cite this lesson rather than reproving it.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "strong-duality-from-the-final-tableau",
        "title": "Strong Duality from the Final Tableau",
        "module": "The two theorems",
        "one_line": "Read the prices off a final tableau and verify dual feasibility column by column and `bᵀy = z*` exactly.",
        "summary": (
            "At the optimum, the objective-row entries under the columns that started as the "
            "identity are exactly `c_BᵀB⁻¹`. That vector is dual feasible and its dual objective "
            "equals the primal optimum, so the simplex method has been solving both programmes "
            "all along and the final tableau is a proof of strong duality on this instance "
            "rather than evidence for it. The prices are not in the right-hand column, and on a "
            "floor or a quota the identity columns are not the slack columns."
        ),
        "key": [
            "y = c_B ᵀ B⁻¹        the z-row entries under the INITIAL identity columns",
            "workshop final z-row      0    0    0   3/2    1   |   36",
            "                         x1   x2   s1    s2    s3       z*",
            "so y = (0, 3/2, 1)       and the right-hand column holds the PLAN, not y",
            "dual check   yᵀaⱼ − cⱼ ≥ 0 for every column:  0, 0, 0, 3/2, 1",
            "bᵀy = 4(0) + 12(3/2) + 18(1) = 36 = z*        exactly, in fractions",
        ],
        "key_label": "Where the prices are, and the two checks that confirm them",
        "concepts_intro": (
            "One hard idea: the second programme was never solved separately. Everything else "
            "here is knowing which columns to look under."
        ),
        "concepts": [
            ("The prices are in the objective row, under the initial identity columns",
             "Column `i` of `B⁻¹` is the tableau column standing over whatever column of the "
             "original data was `eᵢ`. The objective-row entry there is `c_BᵀB⁻¹eᵢ`, which is "
             "`yᵢ`. So the whole price vector is `m` numbers already printed in the tableau you "
             "finished with, in a row most readers walk past."),
            ("Those columns are not always the slack columns",
             "On a `≤` row the identity column is the slack. On a `≥` row the slack is a "
             "surplus, whose original column is `−eᵢ`, so the identity column is the artificial "
             "beside it. An `=` row has no slack column at all, and its identity column is the "
             "artificial. The lab prints the kind of every column it used for exactly this "
             "reason."),
            ("Two checks turn the reading into a proof",
             "Check `yᵀaⱼ ≥ cⱼ` column by column and you have dual feasibility. Check "
             "`bᵀy = z*` and weak duality does the rest: equal values at a feasible pair prove "
             "both points optimal. Together those are a proof of strong duality on this "
             "instance, done in exact fractions, with no appeal to a general theorem."),
        ],
        "read_title": "Reading the second programme out of the first one's final tableau",
        "read_intro": "Which columns hold the inverse, why the objective row over them is the price vector, and the two checks that close the argument.",
        "body": [
            ("p", "The previous lesson ended with prices that closed the gap exactly and no "
                  "account of where they came from. They were not guessed. They were sitting in "
                  "the final tableau of the primal solve, in the objective row, and this lesson "
                  "is the whole of that fact."),
            ("def", ("The initial identity columns",
                     "In standard form the constraint matrix `A` contains, for each row `i`, "
                     "some column equal to the unit vector `eᵢ`. Call those the "
                     "<strong>initial identity columns</strong>. A `≤` row contributes its "
                     "slack; a `≥` row contributes its artificial, because its surplus column is "
                     "`−eᵢ`; an `=` row contributes its artificial, having no slack at all.",
                     "The tableau is `B⁻¹[A | b]`, so the tableau column standing over the "
                     "initial identity column for row `i` is `B⁻¹eᵢ`, which is column `i` of "
                     "`B⁻¹`. That is the sentence the rest of the lesson rests on.")),
            ("math", [
                "workshop, final tableau      basis  x1, s1, x2",
                "",
                "         x1    x2    s1     s2     s3   |   rhs",
                "     ---------------------------------------------",
                "          1     0     0   −1/3    1/3   |     2      x1",
                "          0     0     1    1/3   −1/3   |     2      s1",
                "          0     1     0    1/2      0   |     6      x2",
                "     ---------------------------------------------",
                "  z       0     0     0    3/2      1   |    36",
                "                    ^^^^^^^^^^^^^^^^^",
                "                    the three initial identity columns",
                "",
                "     y = (0, 3/2, 1)          z* = 36",
                "     the right-hand column, (2, 2, 6), is the PLAN: x1 = 2, s1 = 2, x2 = 6",
            ]),
            ("thm", ("Strong duality, from the tableau",
                     "Let the simplex method finish on a maximisation with basis `B`, and set "
                     "`y = c_BᵀB⁻¹`, read off the objective row under the initial identity "
                     "columns. Then `y` is dual feasible and `bᵀy = z*`. Consequently `y` is "
                     "optimal for the dual and the primal optimum equals the dual optimum.",
                     "Dual feasibility is the optimality test itself: the objective-row entry "
                     "over column `j` is `c_BᵀB⁻¹aⱼ − cⱼ = yᵀaⱼ − cⱼ`, and the method stopped "
                     "precisely because every one of those is non-negative. And "
                     "`bᵀy = c_BᵀB⁻¹b = c_Bᵀx_B = z*`, because `B⁻¹b` is the basic part of the "
                     "plan. Weak duality then gives optimality of both points.",
                     "This is an argument about the instance in front of you, and it is the "
                     "version this course takes, because it is the one a reader can execute. "
                     "The separating-hyperplane route through the theorems of the alternative "
                     "proves more and shows less.")),
            ("example", ("Reading the workshop, then checking it",
                         "The three initial identity columns are the slacks `s1`, `s2`, `s3`, "
                         "and the objective row over them reads `0`, `3/2`, `1`. So the cutting "
                         "row is worth nothing, an hour of glazing is worth `3/2`, and an hour "
                         "of assembly is worth 1.",
                         "The dual check, column by column: `x1` gives "
                         "`(0)(1) + (3/2)(0) + (1)(3) = 3 ≥ 3`, a gap of 0; `x2` gives "
                         "`(0)(0) + (3/2)(2) + (1)(2) = 5 ≥ 5`, a gap of 0; the three slack "
                         "columns give `0`, `3/2` and `1` against a cost of 0, gaps of `0`, "
                         "`3/2` and `1`. Every gap is non-negative, so `y` is dual feasible. And "
                         "`bᵀy = 4(0) + 12(3/2) + 18(1) = 36`, which is `z*`.")),
            ("p", "Notice which gaps came out zero. The two decision columns are in the basis or "
                  "were brought into it, and a basic column's gap is exactly zero; the slack "
                  "columns' gaps are the prices themselves. That pattern is not a coincidence "
                  "either, and it is the next lesson."),
            ("h3", "When the identity column is not the slack column"),
            ("p", "Every worked example above has only `≤` rows, which is the case where the two "
                  "lists coincide and the distinction is invisible. The moment a row is a floor "
                  "or a quota the lists part company, and reading the price out of the slack "
                  "column gives a number that is not a price."),
            ("example", ("A floor, whose price hides in an artificial column",
                         "The bakery maximises `5x + 4y` subject to `6x + 4y ≤ 24` (flour), "
                         "`x + 2y ≤ 6` (sugar) and `x + y ≥ 2` (contract). Its standard form has "
                         "columns `x, y, s1, s2, e3, a3`: two slacks, then a surplus and an "
                         "artificial for the floor.",
                         "The lab reports the columns it read as `slack, slack, artificial`. The "
                         "prices are `y = (3/4, 1/2, 0)`, and `bᵀy = 24(3/4) + 6(1/2) + 2(0) = "
                         "21`, which is `z*` at the plan `(3, 3/2)`. Read the third price out of "
                         "the surplus column `e3` instead and you get the negative of it, "
                         "because that column of the original data is `−e₃`.")),
            ("example", ("A quota, which has no slack column at all",
                         "Replace the bakery's floor with `x + y = 3`. Now the standard form is "
                         "`x, y, s1, s2, a3` &mdash; there is no third slack to read anything "
                         "out of. The identity column for that row is the artificial, the prices "
                         "are `y = (0, 0, 5)`, and `bᵀy = 24(0) + 6(0) + 3(5) = 15 = z*` at the "
                         "plan `(3, 0)`.",
                         "Both of the `≤` rows have slack here and are priced at nothing, and "
                         "the entire value of the programme is attributed to the quota. The `y` "
                         "column's dual gap is `5 − 4 = 1`, which says the second product is "
                         "worth 1 less than the quota room it would consume.")),
            ("h3", "The tableau rebuilt from the original data"),
            ("p", "The claim that the tableau is `B⁻¹[A | b]` can be checked rather than "
                  "believed. Gather the basis columns out of the <em>original</em> matrix, "
                  "invert that, multiply by the original `A`, and compare entry for entry with "
                  "the tableau on the screen. On the workshop the basis is `x1, s1, x2`, "
                  "`B⁻¹` has rows `(0, −1/3, 1/3)`, `(1, 1/3, −1/3)` and `(0, 1/2, 0)`, and "
                  "`B⁻¹b = (2, 2, 6)` &mdash; the right-hand column. The lab's second view does "
                  "this for every preset, and the engine's own checks do it on 178 programmes."),
            ("p", "So the reading is not a rule of thumb about where numbers sit. It is a "
                  "consequence of what the tableau is, and once that is seen, the sensitivity "
                  "questions in the second half of this course are all ratio tests on the same "
                  "object."),
        ],
        "lab": ("duality", {
            "mode": "read",
            "preset": "workshop",
            "panel_title": "Choose a programme, and what to read off it",
            "panel_intro": "The tableau shown is the one the simplex method finished with. The "
                           "marked columns are the ones that were the identity when it started "
                           "&mdash; which stops being the same list as the slack columns the "
                           "moment a row is a floor or a quota. The third view checks every dual "
                           "constraint and prints its gap.",
        }),
        "steps_title": "Getting the prices out of a tableau you have finished",
        "steps_intro": "Identify the columns before reading any numbers. Everything that goes wrong here goes wrong at that step.",
        "steps": [
            ("Write down which column of the ORIGINAL data was each unit vector",
             "One per row. A `≤` row gives its slack, a `≥` row gives its artificial, an `=` row "
             "gives its artificial. Do this from the original standard form, not from the final "
             "tableau, because the final tableau is what those columns have become."),
            ("Read the objective row over those columns, in order",
             "That is `y`, row by row, and the order is the constraint order. Do not read the "
             "right-hand column: that holds the plan, and the single number at the end of the "
             "objective row is `z*`."),
            ("Check dual feasibility one column at a time",
             "For each primal column `j`, compute `yᵀaⱼ − cⱼ` and confirm it is non-negative for "
             "a maximisation. Every basic column gives exactly zero; a nonbasic column's gap is "
             "its reduced cost, which the ranging lessons use directly."),
            ("Check `bᵀy = z*` exactly",
             "In fractions, not in decimals. If the two agree you have proved both points "
             "optimal by weak duality, with no further argument; if they do not, the identity "
             "columns were misidentified, which is the failure this check is here to catch."),
        ],
        "worked": {
            "title": "y read off the workshop tableau, then proved",
            "intro": [
                "The tableau below is what the simplex method left behind. Nothing is "
                "recomputed: the prices are copied out of it, and then the two checks turn the "
                "copy into a proof."
            ],
            "lines": [
                "original standard form      columns  x1  x2  s1  s2  s3",
                "  cutting    x1                 + s1        = 4      s1 is e1",
                "  glazing         2x2                 + s2   = 12     s2 is e2",
                "  assembly  3x1 + 2x2                  + s3  = 18    s3 is e3",
                "",
                "so the initial identity columns are s1, s2, s3",
                "",
                "final tableau          basis  x1, s1, x2",
                "         x1    x2    s1     s2     s3   |   rhs",
                "          1     0     0   −1/3    1/3   |     2",
                "          0     0     1    1/3   −1/3   |     2",
                "          0     1     0    1/2      0   |     6",
                "  z       0     0     0    3/2      1   |    36",
                "",
                "read     y1 = 0        y2 = 3/2       y3 = 1",
                "",
                "check 1  dual feasibility, column by column",
                "  x1:  (0)(1) + (3/2)(0) + (1)(3)  = 3    ≥ 3    gap 0",
                "  x2:  (0)(0) + (3/2)(2) + (1)(2)  = 5    ≥ 5    gap 0",
                "  s1:  (0)(1) + (3/2)(0) + (1)(0)  = 0    ≥ 0    gap 0",
                "  s2:  (0)(0) + (3/2)(1) + (1)(0)  = 3/2  ≥ 0    gap 3/2",
                "  s3:  (0)(0) + (3/2)(0) + (1)(1)  = 1    ≥ 0    gap 1",
                "  every gap ≥ 0, so y is dual feasible",
                "",
                "check 2  b'y against z*",
                "  b'y = 4(0) + 12(3/2) + 18(1) = 0 + 18 + 18 = 36",
                "  z*  = 36                                        equal",
                "",
                "conclude  a feasible pair with equal values: (2, 6) is optimal for the",
                "          workshop and (0, 3/2, 1) is optimal for its dual.",
            ],
            "after": [
                "The two checks are doing different work. Dual feasibility is what makes `y` a "
                "certificate at all; the equality is what makes it a sharp one. Neither needed "
                "the dual programme to be solved, and the second is the whole of strong duality "
                "on this instance.",
                "For a faded rehearsal, do the same on the bakery, where the third row is a "
                "floor. The supplied move is the one that matters: its initial identity column "
                "is the artificial `a3`, not the surplus `e3`. Read all three prices, check the "
                "two dual constraints, and confirm `bᵀy = 21`. Then predict what you would have "
                "got from `e3` instead, and check that prediction in the lab.",
                "A reader who wants the third case should then do the quota preset, where there "
                "is no third slack column at all and the entire value of the programme is "
                "attributed to one equality row.",
            ],
        },
        "quiz_title": "Where the prices are",
        "quiz": [
            {"q": "Where in a final tableau are the dual values?",
             "a": ["In the right-hand column, beside the plan",
                   "In the objective row, under the columns that started as the identity",
                   "In the objective row, under the decision columns",
                   "In the last entry of the objective row"],
             "c": 1,
             "why": "The right-hand column holds `B⁻¹b`, which is the plan; the last entry of "
                    "the objective row is `z*`. The prices are `c_BᵀB⁻¹`, and `B⁻¹` lives in the "
                    "columns whose original entries were the unit vectors. Under the decision "
                    "columns the objective row holds reduced costs, which are `yᵀaⱼ − cⱼ` "
                    "&mdash; built from the prices rather than equal to them."},
            {"q": "The bakery's third row is `x + y ≥ 2`. Which column of its final tableau holds the third column of `B⁻¹`?",
             "a": ["The surplus column for that row", "The artificial column for that row",
                   "The slack column of the first row",
                   "There is no such column, so the third price cannot be read"],
             "c": 1,
             "why": "The surplus column of a `≥` row is `−e₃` in the original data, so the "
                    "tableau column above it is `−B⁻¹e₃` &mdash; the negative of what is wanted. "
                    "The artificial is `+e₃`, so that is the identity column. The lab prints the "
                    "kinds of the columns it used, and on this preset they read `slack, slack, "
                    "artificial`."},
            {"q": "At the workshop's optimum `y = (0, 3/2, 1)`. What is `yᵀa − c` for the `x1` column?",
             "a": ["`0`", "`3/2`", "`1`", "`3`"],
             "c": 0,
             "why": "`(0)(1) + (3/2)(0) + (1)(3) = 3`, and `c1 = 3`, so the gap is `0`. Every "
                    "column in the basis gives exactly zero, which is another way of saying the "
                    "objective row is zero there. `3/2` and `1` are the gaps of the `s2` and "
                    "`s3` columns, and `3` is the value of the dot product before `c1` is "
                    "subtracted."},
            {"q": "You have a dual-feasible `y` read off a final tableau, and `bᵀy` equals `z*`. What does that establish?",
             "a": ["That `y` is optimal for the dual and the plan is optimal for the primal",
                   "That the simplex method has finished pivoting",
                   "That no constraint has slack left",
                   "That the simplex method reached this basis in the fewest possible pivots"],
             "c": 0,
             "why": "Equal values at a feasible pair prove both points optimal, by the second "
                    "half of weak duality &mdash; and that is all they prove. The workshop's "
                    "cutting row has 2 units of slack and the values are equal all the same, so "
                    "the third choice is false; the number of pivots taken leaves no trace in "
                    "the final tableau at all; and the objective row being non-negative is the "
                    "reason the method stopped rather than something the equality establishes."},
        ],
        "mistakes": [
            ("Reading the prices out of the right-hand column",
             "That column is `B⁻¹b`, the plan. It has one entry per row and so does `y`, which "
             "is what makes the mistake survive a sanity check: on the workshop it gives "
             "`(2, 2, 6)` instead of `(0, 3/2, 1)`, three plausible-looking numbers that fail "
             "`bᵀy = z*` immediately. Running that check is how you find out."),
            ("Assuming the identity columns are the slack columns",
             "True only when every row is a `≤`. A `≥` row's surplus column is `−eᵢ`, so reading "
             "the price there returns its negative; an `=` row has no slack column at all. This "
             "is the warning The Simplex Method gives about which columns hold `B⁻¹`, and it "
             "applies here for the same reason, on the same tableau."),
            ("Treating dual feasibility as something to assume rather than check",
             "The objective-row entries being non-negative is the optimality test, so on a "
             "tableau the method actually finished with it holds &mdash; but on a tableau you "
             "have modified, cut, re-costed or rebuilt by hand it may not, and every later "
             "lesson modifies tableaux. Check the columns; it is one dot product each."),
        ],
        "standard": ("Finish when you can get the prices out of any final tableau, including one whose rows are not all caps.",
                     "You should be able to name the initial identity column of a `≤`, a `≥` and "
                     "an `=` row, read `y` out of the objective row over them, check `yᵀaⱼ ≥ cⱼ` "
                     "for every column, and confirm `bᵀy = z*` in exact fractions &mdash; and "
                     "say what it proves when it does."),
        "note": 'Everything in the second half of this course is a ratio test on this tableau. The price of a row and the range that price survives, the range of an objective coefficient, the value of a product not yet in the model, the cost of a rule not yet in the model: four different questions, one object, no re-solving. What comes first is the pattern of zero gaps noticed above, which “Complementary Slackness” turns into a way of certifying an answer somebody else has handed you.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "complementary-slackness",
        "title": "Complementary Slackness",
        "module": "The two theorems",
        "one_line": "Turn a claimed optimum into a small linear system, solve it for prices, and certify or refute the claim without pivoting.",
        "summary": (
            "At optimality a positive price forces its constraint tight and a positive activity "
            "forces its dual constraint tight. Run those implications backwards and a claimed "
            "plan determines a candidate set of prices by a small linear system; testing those "
            "prices for feasibility certifies the claim or refutes it, with no algorithm run at "
            "all. The converse does not hold, and where it fails is where degeneracy first "
            "bites."
        ),
        "key": [
            "yᵢ > 0  ⟹  row i tight          row i has slack  ⟹  yᵢ = 0",
            "xⱼ > 0  ⟹  dual column j tight  column j has slack  ⟹  xⱼ = 0",
            "claim x = (2, 6):   cutting has 2 spare  ⟹  y1 = 0",
            "                    x1 > 0  ⟹  y1 + 3y3 = 3        so y3 = 1",
            "                    x2 > 0  ⟹  2y2 + 2y3 = 5       so y2 = 3/2",
            "test y ≥ 0 ✓ and bᵀy = 36 = cᵀx ✓        certified, with no pivot",
            "the converse fails: a tight row can be worth exactly nothing",
        ],
        "key_label": "The conditions, run backwards to produce prices",
        "concepts_intro": (
            "The conditions themselves are two lines. The idea is that they can be read as a "
            "system to solve rather than a property to observe."
        ),
        "concepts": [
            ("The conditions are what a closed gap forces, term by term",
             "Weak duality's two links are sums of non-negative terms. If the ends are equal "
               "then every term in both sums is zero, which means `yᵢ` and row `i`'s slack are "
               "never both positive, and `xⱼ` and dual column `j`'s gap are never both "
               "positive. Complementary slackness is that statement and nothing more."),
            ("Read backwards, they are a linear system for the prices",
             "Given a claimed plan you know which rows have slack &mdash; those prices are zero "
             "&mdash; and which activities are positive &mdash; those dual constraints are "
             "equalities. That is `m` linear equations in `m` unknowns, usually, and solving it "
             "is arithmetic rather than search."),
            ("Testing the candidate is the whole verdict",
             "If the prices come out feasible for the dual, then the claim and the prices are a "
             "feasible pair with equal values, so both are optimal. If any sign or any dual "
             "constraint fails, the claim is refuted and the failing constraint is the reason. "
             "No pivot is performed either way."),
        ],
        "read_title": "Certifying somebody else's answer, and the converse that does not hold",
        "read_intro": "Where the conditions come from, how to run them backwards, and the two ways the system can fail to settle the question the way you expect.",
        "body": [
            ("def", ("Complementary slackness",
                     "A primal-feasible `x` and a dual-feasible `y` satisfy "
                     "<strong>complementary slackness</strong> when, for every row `i`, either "
                     "`yᵢ = 0` or row `i` holds with equality; and for every column `j`, either "
                     "`xⱼ = 0` or dual constraint `j` holds with equality.",
                     "The two halves have names worth keeping apart. A row with slack must be "
                     "priced at zero; an activity that is used must be exactly worth its "
                     "ingredients.")),
            ("thm", ("Complementary slackness characterises optimality",
                     "A feasible pair `(x, y)` is optimal for both programmes if and only if it "
                     "satisfies complementary slackness.")),
            ("proof", [
                "Weak duality gave `cᵀx ≤ yᵀAx ≤ bᵀy`. Write the two gaps out: the right one is "
                "`bᵀy − yᵀAx = yᵀ(b − Ax)`, a sum of products of a price and its row's slack, "
                "and the left one is `yᵀAx − cᵀx = (Aᵀy − c)ᵀx`, a sum of products of a dual "
                "gap and its activity. Feasibility makes every factor in both sums "
                "non-negative.",
                "So `cᵀx = bᵀy` exactly when both sums are zero, which for non-negative terms "
                "means every individual product is zero &mdash; which is complementary "
                "slackness. And by weak duality, `cᵀx = bᵀy` at a feasible pair is precisely "
                "optimality of both.",
            ]),
            ("p", "That is the theorem. The use is what makes it worth a lesson: somebody hands "
                  "you a plan and says it is optimal, and you would like to find out without "
                  "running the algorithm. The conditions tell you which prices are forced to be "
                  "zero and which dual constraints are forced to be equalities, and that is "
                  "usually enough equations to determine `y` outright."),
            ("math", [
                "claim      x = (2, 6) is optimal for the workshop",
                "",
                "rows       cutting   2 ≤ 4       slack 2      ⟹  y1 = 0",
                "           glazing  12 ≤ 12      tight        ⟹  no condition on y2",
                "           assembly 18 ≤ 18      tight        ⟹  no condition on y3",
                "",
                "columns    x1 = 2 > 0            ⟹  y1 + 3y3  = 3",
                "           x2 = 6 > 0            ⟹  2y2 + 2y3 = 5",
                "",
                "solve      y1 = 0, so 3y3 = 3            y3 = 1",
                "           2y2 + 2 = 5                   y2 = 3/2",
                "",
                "test       y = (0, 3/2, 1) ≥ 0                          ✓",
                "           b'y = 4(0) + 12(3/2) + 18(1) = 36 = c'x      ✓",
                "",
                "verdict    certified",
            ]),
            ("example", ("A claim that turns out to be right",
                         "The system above has three equations &mdash; one from the slack row, "
                         "two from the positive activities &mdash; and three unknowns, and it "
                         "produces the same `y` the final tableau holds, reached without a "
                         "single pivot. The lab prints each equation with the sentence that "
                         "produced it, so that the system is visibly derived rather than "
                         "assembled.",
                         "The three-activity preset is the same exercise with one activity not "
                         "made. Claim `(2, 6, 0)`: the contract row has 2 spare, so its price is "
                         "0; the two positive activities give `2y1 + y2 + y3 = 8` and "
                         "`y1 + y2 = 5`; solving gives `y = (3, 2, 0)`, and `bᵀy = 46 = cᵀx`. "
                         "The unused third activity contributes no equation at all, and its dual "
                         "constraint is left to be checked as an inequality: "
                         "`y1 + 2y2 = 7 ≥ 3`, which holds with 4 to spare.")),
            ("h3", "A refutation, and the trap inside it"),
            ("example", ("A feasible claim that is not optimal",
                         "Claim `x = (4, 3)` for the workshop. It is feasible: `4 ≤ 4`, "
                         "`6 ≤ 12`, `18 ≤ 18`. Glazing now has 6 spare, so `y2 = 0`; both "
                         "activities are positive, so `y1 + 3y3 = 3` and `2y2 + 2y3 = 5`. The "
                         "second gives `y3 = 5/2`, and then `y1 = 3 − 15/2 = −9/2`.",
                         "The cutting row is a `≤` row in a maximisation, so its price may not "
                         "be negative. The claim is refuted, and the reason is a specific one "
                         "that can be stated: no set of prices consistent with this plan is dual "
                         "feasible, so this plan cannot be optimal.")),
            ("p", "Now the trap. At that refuted claim, `cᵀx = 27` and `bᵀy = 27` as well "
                  "&mdash; the two numbers agree. Equal values prove optimality only for a "
                  "<em>feasible</em> pair, and `y = (−9/2, 0, 5/2)` is not feasible, so the "
                  "agreement establishes nothing. The lab prints both numbers side by side on "
                  "this preset for exactly that reason: the coincidence is what makes the "
                  "feasibility test look skippable, and it is not."),
            ("h3", "Where the converse fails"),
            ("p", "It is tempting to read the conditions in both directions and conclude that a "
                  "tight row must carry a positive price. That is false, and it fails precisely "
                  "at a degenerate optimum. The conditions say that a positive price forces "
                  "tightness; they say nothing at all about a tight row, and at a corner where "
                  "more rows are tight than there are variables they cannot."),
            ("example", ("A corner where three rows are tight and only two matter",
                         "`max x + y` subject to `x ≤ 2` (kiln), `y ≤ 2` (wheel) and "
                         "`x + y ≤ 4` (firing). The optimum is `(2, 2)` with `z* = 4`, and all "
                         "three rows are tight there. No row has slack, so the conditions give "
                         "only two equations &mdash; `y1 + y3 = 1` and `y2 + y3 = 1` &mdash; for "
                         "three unknowns.",
                         "The lab solves that underdetermined system, reports `y = (1, 1, 0)`, "
                         "and says in as many words that `y3` was never pinned down: the "
                         "conditions left it free and a choice was made. So here is a row that "
                         "is tight and priced at exactly nothing, and a second set of prices "
                         "`(0, 0, 1)` that is equally optimal. Degeneracy in the primal is "
                         "multiple optima in the dual, and this is the smallest instance of "
                         "it.")),
            ("p", "The system can also be contradictory, which is a refutation of a different "
                  "shape. Claim `(1, 1)` on the same programme: every row has slack, so all "
                  "three prices are forced to zero, and both activities are positive, so "
                  "`y1 + y3 = 1` &mdash; `0 = 1`. There are no prices to test at all, and the "
                  "lab reports the verdict as such rather than inventing one. An infeasible "
                  "claim, by contrast, is refused before any of this begins."),
        ],
        "lab": ("duality", {
            "mode": "slackness",
            "preset": "workshop",
            "panel_title": "Claim a plan is optimal, and watch it be tested",
            "panel_intro": "Type a plan. The panel writes out the slackness conditions it "
                           "forces, one line each with the reason, solves them exactly for a "
                           "candidate set of prices, and then either certifies the claim or "
                           "names the dual constraint those prices violate. Try the degenerate "
                           "preset: it certifies, and it tells you which price the conditions "
                           "never pinned down.",
        }),
        "steps_title": "Testing a claim without solving anything",
        "steps_intro": "Feasibility, then the conditions, then the system, then the test. Stop at the first step that fails, and say why.",
        "steps": [
            ("Check the claim is feasible at all",
             "One substitution per row and the sign restrictions. An infeasible claim is refuted "
             "here, and going on to solve for prices would be answering a question nobody "
             "asked."),
            ("Write one condition per slack row and one per positive activity",
             "A row with slack forces its price to zero. A strictly positive activity forces its "
             "dual constraint to hold with equality. Tight rows and unused activities contribute "
             "nothing &mdash; that is the asymmetry the converse gets wrong."),
            ("Solve the system exactly, and say what it left free",
             "Usually it determines `y`. When it does not &mdash; fewer equations than prices, "
             "which is what a degenerate corner produces &mdash; say so, and record that any "
             "choice you then make is a choice rather than a consequence."),
            ("Test the candidate against every dual constraint and every sign",
             "Certified means: feasible pair, equal values, both points optimal. Refuted means: "
             "name the constraint or the sign that failed. Do not let `cᵀx = bᵀy` stand in for "
             "the feasibility test; those two numbers can agree at a refuted claim."),
        ],
        "worked": {
            "title": "Two claims about the workshop, one certified and one refuted",
            "intro": [
                "Both claims are feasible and both produce a full set of prices. The difference "
                "is one sign, and the second half is written out because the numbers there "
                "conspire to look like a proof."
            ],
            "lines": [
                "workshop     max 3x1 + 5x2      cutting  x1      ≤  4",
                "                                glazing     2x2  ≤ 12",
                "                                assembly 3x1+2x2 ≤ 18",
                "dual rows    x1 column   y1 + 3y3  ≥ 3",
                "             x2 column   2y2 + 2y3 ≥ 5          y ≥ 0",
                "",
                "CLAIM A      x = (2, 6)",
                "  rows       cutting  2 vs 4    slack 2   ⟹  y1 = 0",
                "             glazing 12 vs 12   tight     ⟹  −",
                "             assembly 18 vs 18  tight     ⟹  −",
                "  columns    x1 = 2 > 0   ⟹  y1 + 3y3 = 3",
                "             x2 = 6 > 0   ⟹  2y2 + 2y3 = 5",
                "  solve      y1 = 0 → 3y3 = 3 → y3 = 1 → 2y2 = 3 → y2 = 3/2",
                "  test       y = (0, 3/2, 1) ≥ 0                     ✓",
                "             c'x = 36        b'y = 0 + 18 + 18 = 36   equal",
                "  VERDICT    certified: both points optimal, no pivot run",
                "",
                "CLAIM B      x = (4, 3)",
                "  feasible?  4 ≤ 4 ✓   6 ≤ 12 ✓   18 ≤ 18 ✓        yes",
                "  rows       cutting  4 vs 4    tight     ⟹  −",
                "             glazing  6 vs 12   slack 6   ⟹  y2 = 0",
                "             assembly 18 vs 18  tight     ⟹  −",
                "  columns    x1 = 4 > 0   ⟹  y1 + 3y3 = 3",
                "             x2 = 3 > 0   ⟹  2y2 + 2y3 = 5",
                "  solve      y2 = 0 → 2y3 = 5 → y3 = 5/2",
                "             y1 = 3 − 3(5/2) = 3 − 15/2 = −9/2",
                "  test       y1 = −9/2, and a ≤ row in a maximisation",
                "             may not be priced below zero                ✗",
                "  and yet    c'x = 3(4) + 5(3) = 27",
                "             b'y = 4(−9/2) + 12(0) + 18(5/2) = −18 + 45 = 27",
                "             the two values AGREE, and prove nothing",
                "  VERDICT    refuted: no feasible prices accompany this plan",
            ],
            "after": [
                "Claim B is the one to remember. Its two values agree to the last fraction, and "
                "the pair is still not optimal, because equal values prove optimality only when "
                "both points are feasible. Reading `27 = 27` as a certificate is the error the "
                "feasibility test exists to prevent, and the true optimum is 36.",
                "For a faded rehearsal, claim `(2, 2)` on the degenerate programme `max x + y` "
                "subject to `x ≤ 2`, `y ≤ 2`, `x + y ≤ 4`. The supplied observation is that no "
                "row has slack, so the conditions give you two equations and not three. Write "
                "them, say what is left undetermined, choose a value, and check that your choice "
                "is dual feasible. Then find a second, different set of optimal prices for the "
                "same plan.",
                "Then claim `(1, 1)` on that same programme and watch the conditions "
                "contradict each other: every row slack forces every price to zero, and a "
                "positive activity then asks for `0 = 1`. There is nothing to test, and the "
                "honest verdict is that no prices can accompany the claim.",
            ],
        },
        "quiz_title": "Certify, refute, or neither",
        "quiz": [
            {"q": "At a claimed plan, the cutting row uses 2 of its 4 units. What do the slackness conditions force?",
             "a": ["`y1 = 0`", "`y1 > 0`", "That the first dual constraint holds with equality",
                   "`x1 = 0`"],
             "c": 0,
             "why": "A row with slack cannot be worth anything at an optimum, so its price is "
                    "zero &mdash; that is the row half of the conditions. The column half is "
                    "about the dual constraints and is triggered by an activity being positive, "
                    "not by a row having slack. Nothing here forces `y1 > 0`; the conditions "
                    "never force a price to be positive."},
            {"q": "For the claim `x = (4, 3)` the conditions force `y = (−9/2, 0, 5/2)`, and `cᵀx` and `bᵀy` both come out 27. What is the verdict?",
             "a": ["Certified: a feasible pair with equal values",
                   "Refuted: `y1` is negative, and a `≤` row in a maximisation may not be priced below zero",
                   "Refuted: `bᵀy` does not equal `cᵀx`",
                   "Undecidable without running the simplex method"],
             "c": 1,
             "why": "The two values do agree, which is exactly the trap: equal values prove "
                    "optimality only for a <em>feasible</em> pair, and these prices are not dual "
                    "feasible. The third choice misreads the arithmetic. Nothing is undecidable "
                    "&mdash; a refutation with a named violated sign is a complete answer, and "
                    "it cost no pivots."},
            {"q": "At a degenerate corner all three rows are tight and the conditions leave one price undetermined; the lab reports `y = (1, 1, 0)`. Which claim does that refute?",
             "a": ["That complementary slackness characterises optimality",
                   "That a tight row must carry a positive price",
                   "That the primal and dual optima are equal",
                   "That a positive price forces its row to be tight"],
             "c": 1,
             "why": "The firing row is tight and priced at exactly nothing, so tightness does "
                    "not force a positive price &mdash; the converse fails. The implication that "
                    "does hold, that a positive price forces tightness, is untouched, and so are "
                    "the two theorems: the pair is feasible with equal values and both points "
                    "are optimal."},
            {"q": "A claimed plan sits strictly inside the region: every row has slack and both activities are positive. What happens?",
             "a": ["It is certified, with `y = 0`",
                   "The conditions contradict each other, so no prices accompany the claim and it is refuted",
                   "It is refused as infeasible before the conditions are written",
                   "The conditions have many solutions, and any of them will do"],
             "c": 1,
             "why": "Every slack row forces its price to zero; then a positive activity demands "
                    "that its dual constraint hold with equality, which reads `0 = 1`. There is "
                    "no candidate to test and the claim is refuted. It is not infeasible &mdash; "
                    "an interior point satisfies every row &mdash; and the system is "
                    "inconsistent rather than underdetermined."},
        ],
        "mistakes": [
            ("Reading the converse: a tight constraint must have a positive price",
             "The conditions say a positive price forces tightness. The reverse fails at every "
             "degenerate optimum, where more rows are tight than there are variables and at "
             "least one of them must be priced at zero. The lab ships that instance on purpose. "
             "A reader who has only ever seen the conditions behave will assert the converse for "
             "years, and it will be wrong every time a corner is over-determined."),
            ("Letting equal values stand in for the feasibility test",
             "`cᵀx = bᵀy` proves optimality only when both points are feasible, and at the "
             "refuted claim `(4, 3)` both numbers come out 27. The candidate prices produced by "
             "the conditions are candidates: their signs and their dual constraints have to be "
             "checked before the agreement means anything."),
            ("Writing a condition for a tight row or an unused activity",
             "Only slack rows and positive activities generate conditions. Adding an equation "
             "for every tight row over-determines the system and produces a contradiction that "
             "looks like a refutation; adding one for an activity that is zero asserts something "
             "the theorem never claimed. Count the conditions before solving: slack rows plus "
             "positive activities, and nothing else."),
        ],
        "standard": ("Finish when you can certify or refute a claimed optimum in writing, with no algorithm run and no step left implicit.",
                     "You should be able to check a claim for feasibility, write exactly one "
                     "condition per slack row and per positive activity, solve for `y`, test "
                     "every sign and every dual constraint, and state the verdict &mdash; "
                     "including the two verdicts that are neither a clean certificate nor a "
                     "clean refutation: an undetermined price at a degenerate corner, and a "
                     "contradictory system with no prices at all."),
        "note": 'Do this lesson on the degenerate instance as well as on the clean one. Complementary slackness is where degeneracy first bites, and it bites twice: a tight row can be priced at nothing, and the conditions can leave a price undetermined so that the answer you get depends on a choice you made. Both show up again in the next lesson, where a degenerate corner also makes a right-hand-side range collapse against one of its ends.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "shadow-prices-and-right-hand-side-ranging",
        "title": "Shadow Prices and Right-Hand-Side Ranging",
        "module": "What the tableau knows",
        "one_line": "Compute each price with the range it survives, predict the optimum inside that range, and watch the prediction fail outside it.",
        "summary": (
            "A shadow price is the change in the optimum per unit of a right-hand side, and it "
            "is valid only while the current basis stays feasible. The interval over which that "
            "holds comes from a ratio test of the plan against one column of the basis inverse, "
            "and outside it a different basis and a different price take over. So the optimum is "
            "a piecewise-linear function of each right-hand side, with a corner at every "
            "breakpoint, and a price is a rate with a stated interval rather than a derivative."
        ),
        "key": [
            "yᵢ = the change in z* per unit of bᵢ, while B⁻¹b stays ≥ 0",
            "range    a ratio test of B⁻¹b against column i of B⁻¹",
            "assembly  y3 = 1 over 12 ≤ b3 ≤ 24:   z*(20) = 36 + 1(2) = 38   ✓",
            "outside   b3 = 26 gives 42, not 44 — a different basis, and y3 = 0 there",
            "glazing   y2 = 3/2 over 6 ≤ b2 ≤ 18       cutting  y1 = 0 over 2 ≤ b1",
            "z*(bᵢ) is piecewise linear with a corner at every breakpoint",
        ],
        "key_label": "A price, its range, and what happens one unit past the end",
        "concepts_intro": (
            "The price is the easy half and it is already in the tableau. The hard idea is that "
            "the number is attached to an interval, and outside that interval it is not "
            "approximately right."
        ),
        "concepts": [
            ("A price is the slope of one straight segment",
             "Change `bᵢ` and the plan changes to `B⁻¹b` with the same basis, so `z*` changes by "
             "`c_BᵀB⁻¹` times the change &mdash; that is, by `yᵢ` per unit. The relationship is "
             "exactly linear for as long as that basis remains the right one, which makes `z*` "
               "a straight line in `bᵢ` over an interval and not a curve at all."),
            ("The range comes from a ratio test, and it ends when a variable hits zero",
             "The basis stays feasible while every entry of `B⁻¹(b + Δeᵢ)` stays non-negative. "
             "Each basic variable gives one bound on `Δ`, from its own entry divided by its "
             "entry in column `i` of `B⁻¹`, and the binding ones give the two ends. At each end "
             "some basic variable is exactly zero and a different basis takes over."),
            ("Outside the range the price is a different number, not a slightly wrong one",
             "Past a breakpoint the slope changes, so extending the old price gives an answer "
             "that is wrong by an amount that grows with the distance. On the workshop, four "
             "units past the end of assembly's range the naive prediction is out by 2 and the "
             "true slope is zero: more assembly capacity has stopped being worth anything at "
             "all."),
        ],
        "read_title": "The price, the interval it holds over, and the corner at each end",
        "read_intro": "Where the range comes from, what the optimum looks like as a function of one right-hand side, and the two different ways a row can be worth nothing.",
        "body": [
            ("def", ("Shadow price",
                     "The <strong>shadow price</strong> of constraint `i` is the rate of change "
                     "of the optimal objective value with respect to `bᵢ`, holding everything "
                     "else fixed, over the interval in which the current optimal basis remains "
                     "feasible. It is the `i`-th entry of `y = c_BᵀB⁻¹`.",
                     "The interval is part of the answer. This course never prints a price "
                     "without it, because a price quoted outside its interval is not "
                     "approximately right &mdash; it is a different number.")),
            ("p", "Why the price is the slope at all is one line, now that the tableau has been "
                  "read. With basis `B` fixed, the plan is `B⁻¹b` and the value is "
                  "`c_BᵀB⁻¹b = yᵀb`. Add `Δ` to `bᵢ` and the value becomes `yᵀb + yᵢΔ`. So the "
                  "value is linear in `bᵢ` with slope `yᵢ`, for exactly as long as `B` is still "
                  "the optimal basis &mdash; and the only thing that can go wrong is "
                  "feasibility, because the objective row does not involve `b` at all."),
            ("thm", ("The range a shadow price holds over",
                     "Let `d = B⁻¹eᵢ` be column `i` of the basis inverse and `x_B = B⁻¹b` the "
                     "current basic plan. The current basis stays optimal for `bᵢ + Δ` exactly "
                     "while `x_B + Δd ≥ 0`, which gives",
                     "`Δ ≥ max over rows with dᵣ > 0 of (−x_Bᵣ / dᵣ)` and "
                     "`Δ ≤ min over rows with dᵣ &lt; 0 of (−x_Bᵣ / dᵣ)`,",
                     "with an infinite bound on either side when no row constrains it. Inside "
                     "that interval `z*` changes by `yᵢ` per unit; at each end some basic "
                     "variable reaches exactly zero, and past it a different basis is "
                     "optimal.")),
            ("example", ("The workshop's three prices, each with its range",
                         "Cutting is worth `0` over `2 ≤ b1`, with no upper limit. Glazing is "
                         "worth `3/2` over `6 ≤ b2 ≤ 18`. Assembly is worth `1` over "
                         "`12 ≤ b3 ≤ 24`.",
                         "Read the first one carefully: the cutting row is worth nothing, and "
                         "its range still has an end. Below `b1 = 2` the row starts to bite and "
                         "the price stops being zero, which is a thing a reader who has been "
                         "told that slack rows are worth nothing does not expect.")),
            ("math", [
                "z* as a function of the assembly capacity b3, exactly",
                "",
                "     b3 from 0 to 12      slope 5/2      basis  s1, s2, x2",
                "     b3 from 12 to 24     slope 1        basis  s1, x1, x2",
                "     b3 from 24 up        slope 0        basis  s3, x1, x2",
                "",
                "     b3  =  10   12   15   18   20   24   26",
                "     z*  =  25   30   33   36   38   42   42",
                "",
                "     at b3 = 18 the price is 1, and the range is 12 ≤ b3 ≤ 24",
                "     inside:   z*(20) = 36 + 1(20 − 18) = 38            correct",
                "     outside:  36 + 1(26 − 18) = 44, and the truth is 42",
            ]),
            ("p", "The three slopes are the whole lesson in one row of numbers. Assembly "
                  "capacity is worth `5/2` an hour while it is the only thing in short supply, "
                  "worth 1 an hour once cutting has begun to bind as well, and worth nothing at "
                  "all past 24, where the plan has run out of cutting capacity and more assembly "
                  "hours cannot be used. Three prices, one row, and each true on its own "
                  "interval."),
            ("h3", "Outside the range the number is simply different"),
            ("p", "At `b3 = 26` the naive extension predicts 44 and the answer is 42. That is "
                  "not a small error in a linear approximation: the function is exactly linear "
                  "and the slope used was the wrong one, because the basis that slope belonged "
                  "to stopped being feasible at 24. The lab checks this the hard way, by solving "
                  "again at every endpoint and at a point a hundredth outside it, and requiring "
                  "the prediction to break there."),
            ("h3", "Two different ways a row can be worth nothing"),
            ("example", ("Slack, and tight-but-worthless",
                         "The workshop's cutting row has 2 units spare at the optimum, so "
                         "complementary slackness forces its price to zero: more of a resource "
                         "you are not using cannot help. That is the easy case and it is the one "
                         "most readers expect.",
                         "The other case is `max x + y` subject to `x ≤ 2`, `y ≤ 2`, "
                         "`x + y ≤ 4`. At `(2, 2)` all three rows are tight, and the firing row "
                         "is priced at `0` over `4 ≤ b3` &mdash; tight, fully used, and worth "
                         "nothing. Its range is also one-sided at the current value, which is "
                         "the second way degeneracy shows up here: the kiln and wheel rows are "
                         "priced at 1 over `0 ≤ b ≤ 2`, and 2 is where they already are, so "
                         "there is no room above at all.")),
            ("p", "That last observation is worth stating plainly. A range whose end is the "
                  "current right-hand side means the price is valid for decreases and for "
                  "nothing else. Quoting it as the value of one more unit is then simply wrong, "
                  "and a degenerate optimum is where it happens."),
            ("p", "This is also the lesson that replaces calculus on this path, and it is worth "
                  "saying why the replacement is an improvement rather than a workaround. At a "
                  "breakpoint `z*` has a corner: the slope arriving from the left and the slope "
                  "leaving to the right are both correct and they are different &mdash; `5/2` "
                  "and `1` at `b3 = 12`, `1` and `0` at `b3 = 24`. A derivative would have to "
                  "choose one of them or fail to exist. A rate with a stated interval reports "
                  "both, and it is the honest object."),
        ],
        "lab": ("duality", {
            "mode": "rhs",
            "preset": "workshop",
            "panel_title": "Move one right-hand side and watch the price hold, then stop holding",
            "panel_intro": "The curve is computed rather than sampled: at the end of a basis's "
                           "range some quantity is exactly zero, and a ratio test names the plan "
                           "that takes over. No step size is chosen anywhere, so the breakpoints "
                           "are the breakpoints &mdash; and the panel prints what the price "
                           "predicts beside what solving again actually gives.",
        }),
        "steps_title": "Quoting a price so that it means something",
        "steps_intro": "The price and the range are one answer in two parts, and the second part is the one that gets dropped.",
        "steps": [
            ("Read the price out of the objective row",
             "Under the initial identity column for that row, as in the previous lesson. For a "
             "row with slack the answer is zero before you compute anything, by complementary "
             "slackness."),
            ("Take the ratio test against that column of the basis inverse",
             "Divide each basic variable's current value by its entry in column `i` of `B⁻¹`. "
             "The positive entries bound the decrease and the negative entries bound the "
             "increase. Where no entry constrains a side, that side is unbounded &mdash; a "
             "one-sided interval is a real answer."),
            ("Quote the two together, always",
             "A price with no interval attached is a number with no claim attached. Write "
               "`y = 1 over 12 ≤ b3 ≤ 24`, and notice at once when one end of the interval is "
               "the current value: then the price is valid in one direction only."),
            ("Predict, then solve again and compare",
             "Inside the range the prediction `z* + yᵢΔ` is exact. Make one prediction inside "
             "and one outside, and check both. The one outside is the one that teaches: it fails "
             "by an amount that grows, and the basis named on the other segment is the reason."),
        ],
        "worked": {
            "title": "The assembly row, priced and ranged, then pushed past its end",
            "intro": [
                "One row, one price, one interval, and two predictions. The second prediction is "
                "wrong on purpose, and the size of the error is what the interval was protecting "
                "you from."
            ],
            "lines": [
                "workshop    max 3x1 + 5x2      cutting  x1      ≤  4",
                "                               glazing     2x2  ≤ 12",
                "                               assembly 3x1+2x2 ≤ 18",
                "optimum     x = (2, 6)   z* = 36   y = (0, 3/2, 1)",
                "basis       x1, s1, x2       B inverse rows",
                "                                (  0, −1/3,  1/3 )",
                "                                (  1,  1/3, −1/3 )",
                "                                (  0,  1/2,    0 )",
                "",
                "price       y3 = 1         from the z-row under the s3 column",
                "",
                "range       column 3 of B inverse is d = ( 1/3, −1/3, 0 )",
                "            basic plan   x_B = (  2,    2,    6 )   for x1, s1, x2",
                "",
                "            need x_B + Δd ≥ 0, entry by entry:",
                "              x1:  2 + Δ(1/3)  ≥ 0    ⟹  Δ ≥ −6",
                "              s1:  2 − Δ(1/3)  ≥ 0    ⟹  Δ ≤  6",
                "              x2:  6 + Δ(0)    ≥ 0    ⟹  no bound",
                "",
                "            so −6 ≤ Δ ≤ 6, that is   12 ≤ b3 ≤ 24",
                "",
                "inside      b3 = 20, so Δ = 2",
                "            predict  36 + 1(2) = 38",
                "            solve    z* = 38 at (8/3, 6)                 ✓",
                "",
                "at the end  b3 = 24, so Δ = 6      predict 42, solve 42   ✓",
                "            and s1 = 2 − 6(1/3) = 0 exactly: the basis is about to change",
                "",
                "outside     b3 = 26, so Δ = 8",
                "            predict  36 + 1(8) = 44",
                "            solve    z* = 42 at (4, 6)                    ✗  out by 2",
                "            the slope past 24 is 0: cutting has run out, and more",
                "            assembly hours cannot be used at all",
            ],
            "after": [
                "The `s1 = 0` line is the mechanism. The range ends where a basic variable "
                "reaches zero, and that is what the ratio test computes; one unit further and "
                "that variable would be negative, so a different basis &mdash; and a different "
                "price &mdash; has taken over.",
                "For a faded rehearsal, do the glazing row on the same programme. The supplied "
                "move is that column 2 of the basis inverse is `(−1/3, 1/3, 1/2)`, so the signs "
                "of the three ratios are the other way round from the ones above. Compute the "
                "interval, predict `z*` at `b2 = 15` and at `b2 = 21`, and check both. One of "
                "them is inside the range and one is not; say which before you solve.",
                "Then do the three-activity preset, whose three prices and ranges are all whole "
                "numbers: `3` over `8 ≤ b1 ≤ 12`, `2` over `6 ≤ b2 ≤ 10`, and `0` over "
                "`2 ≤ b3`. Predict the effect of one more unit of each and check all three at "
                "once.",
            ],
        },
        "quiz_title": "Prices, ranges, and predictions",
        "quiz": [
            {"q": "The assembly row is priced at `1` over `12 ≤ b3 ≤ 24`, and `z* = 36` at `b3 = 18`. What is `z*` at `b3 = 20`?",
             "a": ["`36`", "`38`", "`40`", "`42`"],
             "c": 1,
             "why": "Inside the range the relationship is exactly linear with slope 1, so "
                    "`36 + 1(2) = 38`, and the lab confirms it by solving again at that value. "
                    "`42` is what happens at the far end of the range, `b3 = 24`, and `40` is "
                    "the answer to no question &mdash; the price is 1 a unit, not 2."},
            {"q": "Same row, same price. What is `z*` at `b3 = 26`?",
             "a": ["`44`", "`42`", "`43`", "`36`"],
             "c": 1,
             "why": "`26` is outside `12 ≤ b3 ≤ 24`, so the price 1 no longer applies. Past 24 "
                    "the slope is 0 &mdash; cutting capacity has become the binding constraint "
                    "and more assembly hours cannot be used &mdash; so `z*` is 42, the value it "
                    "reached at the breakpoint. `44` is the naive extension, and the gap between "
                    "44 and 42 is the whole reason a price is quoted with its range."},
            {"q": "The cutting row has 2 units of slack at the workshop's optimum. What is its price, and does it have a range?",
             "a": ["`0`, and the range is `2 ≤ b1` with no upper limit",
                   "`0`, and the range is the single point `b1 = 4`",
                   "Positive but small, since the row is used at all",
                   "Undefined, because a slack row has no price"],
             "c": 0,
             "why": "Complementary slackness forces a slack row's price to zero, and the range "
                    "is still a real interval: reducing `b1` below 2 makes the row bite and the "
                    "price stop being zero, while raising it has no effect however far it goes. "
                    "A price of zero is a price, and it has a range like any other."},
            {"q": "At the degenerate corner of `max x + y` subject to `x ≤ 2`, `y ≤ 2`, `x + y ≤ 4`, the firing row is tight and priced at `0`. What does that show?",
             "a": ["That the model has been written down wrongly",
                   "That a tight constraint need not be worth anything",
                   "That the price will become positive as soon as the row is relaxed",
                   "That the range of that price is empty"],
             "c": 1,
             "why": "All three rows are tight at `(2, 2)` and there are only two variables, so "
                    "at least one tight row must be priced at zero &mdash; the converse of "
                    "complementary slackness fails, and this is the instance. Relaxing the "
                    "firing row does not help either: its price stays 0 over `4 ≤ b3` with no "
                    "upper limit. The ranges here are real, and it is the kiln and wheel rows "
                    "whose ranges end at the value they already have."},
        ],
        "mistakes": [
            ("Treating a shadow price as valid for any change in the right-hand side",
             "This is the misconception the lesson exists to break. The price belongs to a "
             "basis, the basis stays optimal over an interval, and the interval is computed by a "
             "ratio test that costs nothing. Four units past the end of assembly's range the "
             "naive prediction is out by 2 and the true slope is zero. Never quote the price "
             "without the interval, and never extend it past the interval's end."),
            ("Believing a price must be positive because it is a price",
             "A row with slack is worth exactly zero. A tight row at a degenerate corner can "
             "also be worth exactly zero. And on a floor in a maximisation the price is "
             "non-positive by construction, because relaxing a floor cannot raise a maximum. "
             "The word price is doing the damage here: the object is a rate of change, and it "
             "takes whatever sign the model gives it."),
            ("Confusing this range with the range of an objective coefficient",
             "They answer different questions and they are different ratio tests. Moving a "
               "right-hand side moves the plan and keeps the basis; moving an objective "
               "coefficient keeps the plan and may change which basis is best. The next lesson "
               "is the second computation, and reading a range from the wrong one produces an "
               "interval that looks like an answer."),
        ],
        "standard": ("Finish when you never write a shadow price down without the interval beside it.",
                     "You should be able to read a price out of the objective row, compute its "
                     "interval by a ratio test against one column of the basis inverse, predict "
                     "the optimum for a change inside the interval and confirm it, and say why "
                     "the same prediction fails outside &mdash; naming the basic variable that "
                     "reached zero at the end."),
        "note": 'This is the lesson that replaces calculus on this path, and it is worth being explicit about the trade. At a breakpoint the optimum has a corner: the slope from the left and the slope from the right are both correct and they are different. A derivative would have to choose between them or fail to exist; a rate with a stated interval reports both, and it is the more honest object of the two. The next lesson does the same for the objective coefficients, where the two cases &mdash; an activity that is made and one that is not &mdash; need two different computations.',
    },
]
