"""Course 1, lessons 01-05 - the three questions, and the four model families.

Every figure in this file is computed by the `lp` kit and was read off it rather
than off a draft: the workshop is worth 36 at (2, 6) by corner enumeration and
75/2 at (1, 9/2, 3) by the exact simplex, the ration costs 12 at (3, 2), the
batch costs 335 at 30 / 45 / 25 litres, and the four-period plan costs 775
against the aggregate row's 675 with fifty units of demand unserved.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "decision-variables-objective-and-constraints",
        "title": "From a Situation to a Linear Program",
        "module": "What a model is",
        "one_line": "Write a paragraph as a linear programme and check one candidate point against every row by name.",
        "summary": (
            "Three questions, answered in a fixed order, turn a paragraph into a linear "
            "programme: what do I decide, what do I want, what stops me. The first answer is "
            "a list of variables with a unit on each, the second is one linear expression in "
            "those variables, and the third is one row for every limit &mdash; including the "
            "sign restrictions, which are constraints and not conventions about what letters "
            "mean."
        ),
        "key": [
            "what do I decide  →  variables, a unit on each     C, T in units",
            "what do I want    →  one expression in them        3C + 5T",
            "what stops me     →  one row per limit             C ≤ 4",
            "                                                   2T ≤ 12",
            "                                                   3C + 2T ≤ 18",
            "                  →  and the sign restrictions     C, T ≥ 0",
        ],
        "key_label": "Three questions, and where each answer goes",
        "concepts_intro": (
            "The hard part is the first question. An answer to the second one written in the "
            "first slot survives a perfectly correct solve, and the solve will not tell you."
        ),
        "concepts": [
            ("A decision variable is a quantity you control",
             "`C` is the number of chairs the workshop makes this week, in units. You can set "
             "it, and everything else in the paragraph either limits it or is computed from it. "
             "Two tests: could you hand the number to somebody as an instruction, and does it "
             "have a unit? The hours a chair takes are data, the hours available are data, and "
             "the chairs are the decision."),
            ("The objective is an expression in the decisions, not a variable of its own",
             "Profit here is `3C + 5T`, a number you read off once the decisions are fixed "
             "rather than something you choose. Giving it a letter and a row of its own adds a "
             "column the model does not need and a row that says nothing, and it hides the "
             "resource that actually binds."),
            ("Every limit is a row, and the sign restrictions are rows",
             "A limit becomes one inequality carrying the same unit on both sides. `C ≥ 0` is "
             "one of them: a workshop cannot make −2 chairs, and dropping the line leaves a "
             "different model with a different answer. The lab checks a typed point against "
             "the sign restrictions in the same shape as the rest for exactly that reason."),
        ],
        "read_title": "The three questions, and the model they produce",
        "read_intro": "What a decision variable is, what the objective may and may not be, and how a candidate point is checked.",
        "body": [
            ("def", ("Linear programme",
                     "A <strong>linear programme</strong> is a list of "
                     "<strong>decision variables</strong>, an <strong>objective</strong> that "
                     "is a linear expression in them to be maximised or minimised, and "
                     "finitely many <strong>constraints</strong>, each a linear equation or "
                     "inequality in the same variables. The <strong>sign restrictions</strong> "
                     "`C ≥ 0` are constraints like any other.",
                     "Linear means every variable appears multiplied by a constant and then "
                     "added: `3C + 5T` is linear, and `3CT`, `C²` and `C/T` are not. That is "
                     "the whole of the class. Much of this course is spent recognising when a "
                     "requirement has left it &mdash; and rather more of it on the requirements "
                     "that look as though they have and have not.")),
            ("p", "The three questions are worth writing as three separate lists before any "
                  "algebra. What do I decide, what do I want, what stops me. They are asked in "
                  "that order because the second and third are both expressions in the answer "
                  "to the first, so there is nothing to write until the first is settled."),
            ("example", ("A workshop, as a paragraph",
                         "A workshop makes chairs and tables. A chair takes 1 bench hour in "
                         "the carpentry shop and 3 hours on the assembly line; a table takes 2 "
                         "hours in the finishing shop and 2 hours on the assembly line. The "
                         "week has 4 bench hours, 12 finishing hours and 18 assembly hours in "
                         "it. A chair earns 3 pounds and a table 5. What should the workshop "
                         "make?")),
            ("p", "The decisions are the chairs and the tables, `C` and `T`, both counted in "
                  "units made this week. Nothing else in that paragraph is a decision: the "
                  "rates are properties of the products and the availabilities are properties "
                  "of the week."),
            ("math", [
                "maximise   3C + 5T                pounds a week",
                "",
                "subject to      C      ≤  4       bench hours, carpentry",
                "               2T      ≤ 12       finishing hours",
                "          3C + 2T      ≤ 18       assembly hours",
                "               C, T    ≥  0",
            ]),
            ("p", "Read one row across and check its units. In the carpentry row the "
                  "coefficient is 1 bench hour for each chair, so the left-hand side is bench "
                  "hours; the right-hand side is 4 bench hours. Both sides agree, which is the "
                  "cheapest available check that a row is about what you think it is about."),
            ("h3", "The answer to the second question, written in the first slot"),
            ("p", "The commonest broken model on this course introduces `P` for profit, adds "
                  "the row `P = 3C + 5T`, and maximises `P`. Nothing is gained. `P` is "
                  "determined by `C` and `T`, so the new column carries no freedom and the new "
                  "row carries no information; the model has one more variable and one more "
                  "equation and exactly the same optimum."),
            ("p", "The related move is to write a target as a constraint: `3C + 5T ≥ 500`. "
                  "That is a legal row, and it is a different question &mdash; it asks whether "
                  "500 can be reached, not what the best achievable profit is. A reader who "
                  "adds it to the model above and then maximises the same expression has "
                  "written the objective twice and constrained nothing that matters."),
            ("h3", "Checking a candidate point"),
            ("p", "A model is worth solving once you can test a point in it by hand. Take a "
                  "point, substitute it into each row separately, and record the left-hand "
                  "value, the right-hand value and the difference. A point that fails should "
                  "fail with the name of a row attached to it; “the solver rejected it” is not "
                  "a diagnosis."),
            ("example", ("Two points, one of them not a plan",
                         "At `(2, 6)` the three rows read `2 ≤ 4`, `12 ≤ 12` and `18 ≤ 18`, "
                         "both sign restrictions hold, and the objective is 36. At `(4, 6)` "
                         "the objective is 42, which is larger, and the assembly row reads "
                         "`24 ≤ 18`: over by 6 hours. The second point is not a worse plan, it "
                         "is not a plan.")),
            ("p", "That is also why `C ≥ 0` is a constraint rather than a convention. Drop the "
                  "two sign restrictions from the workshop and the region runs away to the "
                  "south-west, where the model cheerfully unmakes tables to free assembly "
                  "hours for chairs. The rows are not decoration; they are two of the five "
                  "things a point has to satisfy."),
        ],
        "lab": ("lp", {
            "mode": "model",
            "preset": "mix",
            "view": "candidate",
            "panel_title": "Write the programme, then type a point and watch each row answer",
            "panel_intro": "Every coefficient below is read off the data table, so moving an "
                           "availability rewrites the programme and re-solves it rather than "
                           "adjusting an answer. Type a candidate point and each row reports "
                           "its own left-hand value, right-hand value and difference, with the "
                           "sign restrictions in the same list.",
        }),
        "steps_title": "Turning a paragraph into a programme",
        "steps_intro": "Four passes over the same paragraph, in this order. Doing them at once is what produces a model with profit on both sides.",
        "steps": [
            ("Name the decisions and give each one a unit",
             "Write `C = chairs made this week, in units` rather than `C = chairs`. The unit is "
             "what lets you check a row later, and a quantity you cannot put a unit on is "
             "usually not a decision."),
            ("Write the objective as an expression in those names",
             "One line, with its own unit: pounds a week, litres, hours. If the expression "
             "needs a quantity that is not in the list of decisions, the list is incomplete "
             "&mdash; go back rather than inventing a variable to hold the total."),
            ("Write one row per limit, and check both sides for units",
             "Each limit is one inequality. Read it across and name what the left-hand side "
             "measures and what the right-hand side measures; if they differ, the row is wrong "
             "before it is solved and no amount of solving will say so."),
            ("Add the sign restrictions, then test a point by hand",
             "List `C ≥ 0` beside the rest. Then pick a point you believe in and check it "
             "against every row in turn, writing the difference down. A sign error shows up "
             "here in a minute and nowhere else at all."),
        ],
        "worked": {
            "title": "The workshop, written down and then tested at two points",
            "intro": [
                "The three questions first, each answered in its own block, and only then the "
                "arithmetic. The check at the end is the part most readers skip and the part "
                "that finds the error."
            ],
            "lines": [
                "what do I decide",
                "    C = chairs made this week, in units",
                "    T = tables made this week, in units",
                "",
                "what do I want",
                "    maximise  3C + 5T          pounds a week",
                "",
                "what stops me",
                "    C          ≤  4            bench hours in the carpentry shop",
                "    2T         ≤ 12            hours in the finishing shop",
                "    3C + 2T    ≤ 18            hours on the assembly line",
                "    C, T       ≥  0",
                "",
                "the candidate (2, 6)",
                "    carpentry     2        ≤  4      left minus right = −2     holds",
                "    finishing     12       ≤ 12      left minus right =  0     holds",
                "    assembly      6 + 12   ≤ 18      left minus right =  0     holds",
                "    C ≥ 0         2                                           holds",
                "    T ≥ 0         6                                           holds",
                "    objective     6 + 30 = 36",
                "",
                "the candidate (4, 6)",
                "    assembly      12 + 12  ≤ 18      left minus right =  6     broken",
                "    objective     12 + 30 = 42,  and nobody can run it",
            ],
            "after": [
                "The second candidate is the one worth studying. It scores 42 against 36 and "
                "it is not a plan at all: the assembly line is over its limit by 6 hours. The "
                "difference between a better plan and an impossible one is exactly this table, "
                "and a model you cannot check by hand is a model you are trusting rather than "
                "using.",
                "For a faded rehearsal, let the workshop make benches too. A bench takes 1 "
                "bench hour, 1 finishing hour and 2 assembly hours, and earns 4. The supplied "
                "first move is the unit: benches are counted in units made this week, so the "
                "new column enters all three rows and the objective. Write the three rows out, "
                "then check `(1, 9/2, 3)` against each of them and against the three sign "
                "restrictions before you look at what the lab reports &mdash; and notice that "
                "the answer is a fraction, which is a thing a workshop will have to be asked "
                "about later.",
            ],
        },
        "quiz_title": "Decisions, objectives and rows",
        "quiz": [
            {"q": "In the workshop above, which of these is a decision variable?",
             "a": ["The 18 hours available on the assembly line",
                   "The number of chairs made this week",
                   "The 3 hours a chair takes on the assembly line",
                   "The profit `3C + 5T`"],
             "c": 1,
             "why": "Only the chairs can be set by whoever runs the workshop. The 18 hours and "
                    "the 3 hours are data the week and the product hand you, and the profit is "
                    "an expression that has a value once the decisions do."},
            {"q": "A reader introduces `P` for profit, adds the row `P = 3C + 5T`, and maximises `P`. What has that achieved?",
             "a": ["It makes the model non-linear, because `P` appears on both sides",
                   "It makes the model unbounded, because nothing limits `P` from above",
                   "Nothing: `P` is determined by the decisions, so the column carries no freedom and the row carries no information",
                   "It changes the optimum, because `P` may now be negative"],
             "c": 2,
             "why": "The row is linear and the model is still bounded &mdash; every row that "
                    "limited `C` and `T` still limits them, and `P` is pinned to them by an "
                    "equation. What the reader has added is one column with no freedom in it "
                    "and one row that repeats the objective."},
            {"q": "Which point satisfies every row of the workshop model?",
             "a": ["`(4, 6)`", "`(0, 7)`", "`(2, 6)`", "`(−1, 6)`"],
             "c": 2,
             "why": "`(2, 6)` holds everywhere, with the finishing and assembly rows exactly "
                    "tight. `(4, 6)` breaks the assembly row by 6 hours, `(0, 7)` breaks the "
                    "finishing row because `2(7) = 14` is more than 12, and `(−1, 6)` breaks a "
                    "sign restriction, which is a row like the others."},
            {"q": "Both sides of the carpentry row `C ≤ 4` are measured in what?",
             "a": ["Units of chairs", "Bench hours in the carpentry shop", "Pounds a week",
                   "Nothing: an inequality carries no unit"],
             "c": 1,
             "why": "The coefficient hidden in front of `C` is 1 bench hour for each chair, so "
                    "the left-hand side is `hours per unit × units`, which is hours; the right "
                    "is 4 bench hours. Reading the row as “at most four chairs” happens to "
                    "give the same numbers here and stops doing so the moment the rate is not 1."},
        ],
        "mistakes": [
            ("Writing the objective into the variable slot",
             "Profit, cost, revenue and “the total” are expressions in the decisions. A "
             "variable list that opens with profit has answered the second question in the "
             "first slot, and the row that follows &mdash; `P = 3C + 5T` &mdash; adds a letter "
             "and no information. The test is whether the number could be handed over as an "
             "instruction: “make 2 chairs” is one, “earn 36 pounds” is not."),
            ("Dropping the sign restrictions because they look obvious",
             "`C ≥ 0` and `T ≥ 0` are two of the five rows here. Without them the region is "
             "unbounded to the south-west and the optimum moves, so they are constraints "
             "rather than a convention about what a letter may mean. Any lab verdict that "
             "surprises you is worth checking against them first."),
            ("Turning a datum into a decision",
             "The 18 assembly hours and the 3 hours a chair takes are given. Promoting an "
             "availability to a decision produces a model whose answer is “make everything”, "
             "and the row it came from has quietly become an equation about a quantity nobody "
             "controls."),
        ],
        "standard": ("Finish when the three questions are answered separately, in order, before any algebra.",
                     "You should be able to read a paragraph and produce the variables with "
                     "their units, the objective, every row including the sign restrictions, "
                     "and then a point you have checked by hand against each row in turn "
                     "&mdash; naming the row that fails when one does."),
        "note": "The third question keeps taking four shapes, and they are the four model families. “Product Mix and Packing Constraints” is `usage ≤ availability`; “Covering and Diet Models” is `supply ≥ requirement`; “Blending and Ratio Constraints” is a percentage of a total the decisions themselves make up; and “Multiperiod Planning and Balance Constraints” is one equation for each period, linking it to the period before.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "product-mix-and-resource-constraints",
        "title": "Product Mix and Packing Constraints",
        "module": "The four model families",
        "one_line": "Build a packing model from a rate table and say which resources the optimum exhausts.",
        "summary": (
            "A packing row says `usage ≤ availability`. Its coefficients are per-unit rates "
            "read down a column of a data table, and the gap it leaves at a point is that "
            "resource's <em>slack</em>, measured in the resource's own unit. A row with no "
            "slack left is tight, and this lesson is careful about what tight does and does "
            "not tell you."
        ),
        "key": [
            "usage ≤ availability",
            "  rate per unit × units made, summed over the products",
            "  slack = availability − usage,  in that resource’s own unit",
            "  tight  ⇔  slack = 0  ⇔  the resource is used right up",
            "",
            "3C + 2T ≤ 18        at (2, 6):  18 ≤ 18,  slack 0",
            "     C  ≤  4        at (2, 6):   2 ≤  4,  slack 2 bench hours",
        ],
        "key_label": "A packing row, and what its slack measures",
        "concepts_intro": (
            "One shape, repeated once per resource. The interesting content is in the slacks, "
            "and in one thing they cannot tell you."
        ),
        "concepts": [
            ("A packing row has usage on the left and availability on the right",
             "Every `≤` row in this family is the same sentence: what the plan consumes of one "
             "resource, at most what there is of it. The row belongs to the resource, not to "
             "the product, so three products and three shops give three rows and not nine."),
            ("The coefficients are per-unit rates, read down a column",
             "The assembly row `3C + 2T ≤ 18` takes its 3 from the chairs column of the "
             "assembly row of the table and its 2 from the tables column. Reading the table "
             "across instead of down transposes the model into a different, solvable, wrong "
             "one, which is why the lab prints the table beside the programme it produced."),
            ("Slack is the unused amount, in the resource’s own unit",
             "At `(2, 6)` the carpentry row has 2 bench hours left and the other two rows have "
             "nothing left. That number is not a score and not a percentage: it is hours, and "
             "the same optimum has a slack in each row measured in a different unit."),
        ],
        "read_title": "Packing rows, slack, and what tight does not mean",
        "read_intro": "One row per resource, read off a table; the slacks at the optimum; and the question this course deliberately cannot answer yet.",
        "body": [
            ("p", "The data arrive as a table, and the model is a transcription of it. Rates "
                  "down the columns, availabilities down the right, and the profit row "
                  "underneath."),
            ("math", [
                "                     chairs (C)   tables (T)    available",
                "  carpentry shop          1            0         4 bench hours",
                "  finishing shop          0            2         12 finishing hours",
                "  assembly line           3            2         18 assembly hours",
                "  profit a unit           3            5         —",
            ]),
            ("def", ("Slack",
                     "For a row `a·x ≤ b` and a point `x`, the <strong>slack</strong> of the "
                     "row at `x` is `b − a·x`. It is at or above zero exactly where the row "
                     "holds, and the row is <strong>tight</strong> at `x` when the slack is "
                     "zero.",
                     "Slack is a quantity in the situation and not a diagnostic: the slack in "
                     "the carpentry row is the bench hours the plan leaves unused. “Standard "
                     "Form, Slack and Surplus” promotes it to a variable of the model; here it "
                     "is only computed.")),
            ("p", "The two-product workshop is worth 36 at `(2, 6)`, and the slacks there are "
                  "2 bench hours, 0 finishing hours and 0 assembly hours. Two of the three "
                  "rows are used right up, which is the usual state of affairs: an optimum of "
                  "a two-variable programme sits where two boundaries cross."),
            ("h3", "A third product, and the end of the picture"),
            ("p", "Let the workshop also make benches, at 1 bench hour, 1 finishing hour and 2 "
                  "assembly hours each, earning 4. The table grows a column, every row grows a "
                  "term, and the optimum becomes 75/2 at `(1, 9/2, 3)` with all three rows "
                  "tight. Two things changed. The answer is a fraction, and there is no longer "
                  "a picture: three decisions cannot be drawn on a plane, so the lab hands the "
                  "programme to the exact simplex instead of enumerating corners."),
            ("p", "Both routes are solving the same kind of object and they agree wherever "
                  "they overlap &mdash; pin the bench column at zero and the engine returns 36 "
                  "again. That agreement is worth more than either method alone, because it is "
                  "the only evidence that the picture was a method and not a habit."),
            ("h3", "Tight is not the same as worth relieving"),
            ("p", "A tight row is a resource the plan has used up. It is tempting to read that "
                  "as “the bottleneck”, and to conclude that one more hour of it would buy "
                  "something. It need not."),
            ("example", ("Three exhausted resources, two of them worth nothing",
                         "Push the assembly line to 24 hours. The optimum moves to `(4, 6)` "
                         "and earns 42, and now all three rows are tight: `4 ≤ 4`, `12 ≤ 12` "
                         "and `24 ≤ 24`. Add a twenty-fifth assembly hour and the answer is "
                         "still 42, with one assembly hour idle. Add a bench hour and it is "
                         "still 42. Add two finishing hours and it is 45. Three resources "
                         "exhausted, one of them worth paying for.")),
            ("p", "What separates them is a number this course cannot yet compute: the change "
                  "in the optimum for one more unit of a resource, and the range of "
                  "availabilities over which that change is the truth. It is called a shadow "
                  "price, it is “Duality and Sensitivity Analysis”, and the honest report here "
                  "is that a tight row names a resource the plan exhausted and says nothing "
                  "about what relieving it would be worth."),
            ("p", "The slacks do settle a smaller question completely, and it is worth having. "
                  "A row with slack left is a row that is not currently deciding anything: "
                  "change its availability by less than its slack and neither the plan nor the "
                  "profit moves at all."),
        ],
        "lab": ("lp", {
            "mode": "model",
            "preset": "mix",
            "view": "slacks",
            "panel_title": "Move one availability and watch which rows stay tight",
            "panel_intro": "The slack table evaluates every row at the optimum and marks it "
                           "tight or slack, each in its own unit. Take the assembly line up to "
                           "24 and all three rows go tight at once; take it to 25 and one of "
                           "them comes back with an hour to spare while the profit does not "
                           "move.",
        }),
        "steps_title": "Building a packing model from a table",
        "steps_intro": "The table is the model. These four steps are a transcription with two checks in it.",
        "steps": [
            ("One row per resource, one column per product",
             "Count the rows of your model before writing them: as many as there are things in "
             "limited supply. A row for each product is the commonest transposition, and it "
             "produces a model about nothing at all."),
            ("Read the rates down the column of the product",
             "The chairs column of the table supplies the coefficient of `C` in every row. "
             "Write the column out beside the rows it feeds if the table is wide; a "
             "misplaced rate is invisible once the programme is written."),
            ("Check each row for units, both sides",
             "`hours per unit × units` is hours, and the availability is hours of the same "
             "shop. When a rate is quoted in minutes and an availability in hours, that is a "
             "real error and the only place it shows is here."),
            ("Solve, then read the slacks before the answer",
             "Which rows are tight is the structural fact about the solution; the objective "
             "value is one number. Note the slacks in their own units, and resist the "
             "conclusion that a tight row is worth relieving."),
        ],
        "worked": {
            "title": "Three products and three shops, solved by the engine",
            "intro": [
                "The two-product version is worth 36 at `(2, 6)` and can be drawn. Adding the "
                "bench column removes the picture and changes the kind of answer, so it is the "
                "case worth writing out in full."
            ],
            "lines": [
                "                chairs (C)  tables (T)  benches (B)   available",
                "  carpentry          1           0           1        4 bench hours",
                "  finishing          0           2           1        12 finishing hours",
                "  assembly           3           2           2        18 assembly hours",
                "  profit a unit      3           5           4        —",
                "",
                "maximise   3C + 5T + 4B",
                "subject to    C      +  B  ≤  4",
                "                  2T +  B  ≤ 12",
                "          3C  + 2T  + 2B  ≤ 18",
                "              C, T, B     ≥  0",
                "",
                "optimum    C = 1,  T = 9/2,  B = 3        profit  75/2",
                "",
                "carpentry     1 + 3        =  4  ≤  4     slack 0     tight",
                "finishing     9 + 3        = 12  ≤ 12     slack 0     tight",
                "assembly      3 + 9 + 6    = 18  ≤ 18     slack 0     tight",
                "",
                "check      3(1) + 5(9/2) + 4(3)  =  3 + 45/2 + 12  =  75/2",
            ],
            "after": [
                "Every row is tight, the plan asks for four and a half tables, and 75/2 is not "
                "a number a decimal would have kept. A reader who wanted whole tables has a "
                "real question and it is answered in “Integer Programming”, not by rounding "
                "&mdash; that warning is the standing one on this course.",
                "For a faded rehearsal, drop the bench column and take the finishing shop from "
                "12 hours to 13. The supplied first move is which rows can possibly change: "
                "only the ones that were tight, because a row with slack to spare is not "
                "deciding anything. Predict the new plan and profit, then check it against the "
                "lab, and say in a sentence why the carpentry slack grew rather than shrank.",
            ],
        },
        "quiz_title": "Rates, rows and slacks",
        "quiz": [
            {"q": "At the two-product optimum `(2, 6)` the carpentry row has slack 2. What is that 2?",
             "a": ["Two chairs the workshop could still make",
                   "Two bench hours the plan leaves unused in the carpentry shop",
                   "Two pounds of profit still available",
                   "The number of rows that are tight"],
             "c": 1,
             "why": "Slack is `availability − usage` in the row's own unit, and the carpentry "
                    "row is measured in bench hours. It happens to equal two chairs here only "
                    "because a chair takes exactly one bench hour."},
            {"q": "The assembly line is raised from 18 hours to 24 and all three rows become tight at `(4, 6)`. What follows?",
             "a": ["All three resources are now worth relieving",
                   "The plan is degenerate and therefore wrong",
                   "Each exhausted resource is worth the same amount per hour",
                   "All three are used right up, and which of them is worth relieving is a separate question"],
             "c": 3,
             "why": "Tight means used up. A twenty-fifth assembly hour leaves the profit at 42 "
                    "and a twenty-fifth bench hour does too, while two more finishing hours "
                    "take it to 45. What distinguishes them is a price, and prices are “Duality "
                    "and Sensitivity Analysis”."},
            {"q": "A shop's availability is quoted in minutes while the rates are in hours per unit. Where does that show up?",
             "a": ["In the objective, which will be in the wrong units",
                   "Nowhere: the solver rescales each row",
                   "In the row itself, whose two sides then measure different things",
                   "In the sign restrictions"],
             "c": 2,
             "why": "The left-hand side is `hours per unit × units`, which is hours, and the "
                    "right-hand side is minutes. Nothing in the arithmetic objects, the model "
                    "solves, and the answer is about a shop with sixty times too much capacity."},
            {"q": "Why does the three-product workshop go to the simplex engine rather than to corner enumeration?",
             "a": ["Because its optimum is a fraction",
                   "Because three decisions have no picture to enumerate the corners of",
                   "Because all three of its rows are tight",
                   "Because corner enumeration only works for maximisation"],
             "c": 1,
             "why": "The corner route crosses pairs of boundary lines in a plane, and three "
                    "decisions are not a plane. Fractions are no obstacle to either method: "
                    "both carry exact rationals, and the two-variable route produces fractions "
                    "as happily."},
        ],
        "mistakes": [
            ("Reading a tight row as a bottleneck worth relieving",
             "Tight means used up. It does not mean that one more unit would buy anything, and "
             "two resources can both be exhausted with only one of them worth paying for. The "
             "distinction is a price and a range, which this course can name and deliberately "
             "cannot compute; saying so is more useful than guessing."),
            ("One row per product instead of one row per resource",
             "The rows of a packing model belong to the things in limited supply and the "
             "columns to the things you decide. Transposing the table produces a model that "
             "builds, solves and answers a question nobody asked, and the usual symptom is "
             "coefficients that all look like profits."),
            ("Quietly dropping a row with slack in it",
             "A row with slack at one optimum is not a row you may delete: move an "
             "availability or a profit and it can become the row that binds. What the slack "
             "licenses is narrower and exact &mdash; changing that availability by less than "
             "its slack moves neither the plan nor the objective."),
        ],
        "standard": ("Finish when you can say which rows are tight before you are told the objective value.",
                     "You should be able to transcribe a rate table into rows and columns "
                     "without transposing it, compute the slack in every row at a given point "
                     "in that row's own unit, and state what a tight row does and does not "
                     "settle."),
        "note": "A packing row limits what a plan may consume. The next family turns the inequality round: a requirement says a plan must supply at least something, its gap is an over-fulfilment rather than an unused remainder, and the region such rows cut out has no ceiling at all &mdash; which turns out to be harmless, for a reason worth being careful about.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "covering-diet-and-minimisation-models",
        "title": "Covering and Diet Models",
        "module": "The four model families",
        "one_line": "Build a requirement model, certify that its cost cannot run away, and name the requirements met exactly.",
        "summary": (
            "A requirement is a `≥` row and the gap it leaves is a <em>surplus</em>: "
            "over-fulfilment rather than an unused remainder. The region such rows cut out "
            "runs on forever, and that is harmless while every direction it runs in costs "
            "money. Unboundedness is a property of the objective along those directions, not "
            "of the region &mdash; and it is decided rather than sampled."
        ),
        "key": [
            "supply ≥ requirement",
            "  surplus = usage − requirement,  over-fulfilment",
            "",
            "minimise 2G + 3P     G + 3P ≥ 9      2G + P ≥ 8",
            "",
            "d is a recession direction:  x + td feasible for every t ≥ 0",
            "the cost runs away  ⇔  some recession direction d has c·d negative",
        ],
        "key_label": "A requirement row, its surplus, and the test for a runaway cost",
        "concepts_intro": (
            "The model is the packing model with the inequality turned round. The care goes "
            "into one question that looks alarming in a picture and is settled by arithmetic."
        ),
        "concepts": [
            ("A requirement is a `≥` row and its gap is a surplus",
             "`G + 3P ≥ 9` says the ration supplies at least 9 grams of protein. At a point "
             "that satisfies it, `usage − requirement` is the over-fulfilment: grams of "
             "protein more than were asked for. It is not slack &mdash; nothing is being left "
             "unused &mdash; and “Standard Form, Slack and Surplus” is where the sign of that "
             "distinction stops being a name and starts mattering."),
            ("A covering region has no ceiling",
             "Feed more of everything and every requirement still holds, so the region "
             "extends forever to the north-east. In a picture that looks like a problem "
             "without an answer. It is not: the picture has no top, and the question is what "
             "the objective does out there."),
            ("Unboundedness belongs to the objective, along the directions the region runs in",
             "A direction `d` is a recession direction when `x + td` stays feasible for every "
             "`t ≥ 0`. The cost runs away exactly when some recession direction lowers it, "
             "which is a statement about `c·d` and not about the shape of the region. With "
             "non-negative costs, every step out costs money and the minimum sits at a corner."),
        ],
        "read_title": "Requirements, surpluses, and why an unbounded region is harmless",
        "read_intro": "The `≥` row and what its gap measures, the corners of a covering model, and the recession test that certifies the minimum exists.",
        "body": [
            ("p", "A feed merchant blends grain and pellets into a ration. Each kilogram of "
                  "grain supplies 1 gram of protein and 2 of fibre; each kilogram of pellets "
                  "supplies 3 grams of protein and 1 of fibre. The ration must carry at least "
                  "9 grams of protein and at least 8 of fibre. Grain costs 2 a kilogram and "
                  "pellets 3."),
            ("math", [
                "                     grain (G)   pellets (P)    at least",
                "  protein                1            3         9 grams",
                "  fibre                  2            1         8 grams",
                "  cost a kilogram        2            3         —",
                "",
                "minimise   2G + 3P",
                "subject to  G + 3P  ≥  9",
                "           2G +  P  ≥  8",
                "            G, P    ≥  0",
            ]),
            ("def", ("Surplus",
                     "For a row `a·x ≥ b` and a point `x`, the <strong>surplus</strong> of the "
                     "row at `x` is `a·x − b`. It is at or above zero exactly where the row "
                     "holds, and the row is tight at `x` when the surplus is zero.",
                     "At `(4, 2)` the protein surplus is 1 gram and the fibre surplus is 2 "
                     "grams: the ration over-delivers both. At the cheapest ration `(3, 2)` "
                     "both surpluses are zero, which is the usual outcome when nothing is "
                     "gained by exceeding a requirement.")),
            ("p", "The corners are `(0, 8)` at a cost of 24, `(3, 2)` at 12 and `(9, 0)` at "
                  "18. The cheapest is `(3, 2)`: three kilograms of grain and two of pellets, "
                  "supplying exactly 9 grams of protein and exactly 8 of fibre. Both "
                  "requirements are met exactly, and neither is exceeded, because exceeding "
                  "one would cost money and buy nothing."),
            ("h3", "The region runs on forever, and the minimum still exists"),
            ("p", "There is no boundary to the north-east: feed ten kilograms of each and both "
                  "requirements are still satisfied. A reader who has been warned about "
                  "unbounded problems will reach for that observation, and it is the wrong "
                  "observation. Being able to walk forever is a fact about the region; whether "
                  "the cost falls forever as you walk is a fact about the objective."),
            ("thm", ("When a minimum exists",
                     "Let the feasible region be non-empty, and let `d` be any direction in "
                     "which it runs on forever &mdash; a direction with `x + td` feasible for "
                     "every `t ≥ 0`. If `c·d` is at or above zero for every such `d`, then the "
                     "objective `c·x` has a smallest value on the region, and it is attained at "
                     "a corner.",
                     "The contrapositive is the whole diagnostic: the cost runs away exactly "
                     "when some direction the region contains lowers it. This is the ray check "
                     "of “Systems of Inequalities and Linear Programming” written for a cost "
                     "rather than for a picture.")),
            ("p", "Along `(1, 0)` the cost changes by 2 a step, along `(0, 1)` by 3, and along "
                  "`(1, 1)` by 5. All three are directions the region runs in, and all three "
                  "cost money, so walking out never helps and the smallest cost is at one of "
                  "the three corners. The lab reports each direction it tested and then, "
                  "separately, a verdict over every direction at once &mdash; because three "
                  "directions that rise are evidence and not a proof."),
            ("example", ("A disposal credit, and the same region with no minimum",
                         "Suppose the merchant is paid 1 a kilogram to take pellets away, so "
                         "the cost is `2G − P`. Nothing about the region changes: the two "
                         "requirements are the same two rows and it still runs to the "
                         "north-east. But `(0, 1)` now changes the cost by `−1` a step, so the "
                         "cost falls forever along a direction the region contains, and there "
                         "is no cheapest ration at all. The lab reports no value rather than "
                         "the last point its search stood on.")),
            ("p", "That is the shape of the answer to keep. An unbounded region with a "
                  "non-negative cost is a covering model behaving normally. An unbounded "
                  "problem needs a recession direction along which the objective improves, "
                  "and finding one is a computation."),
        ],
        "lab": ("lp", {
            "mode": "model",
            "preset": "diet",
            "panel_title": "Set the requirements, then try to make the cost run away",
            "panel_intro": "The region here has no ceiling, and the recession panel tests each "
                           "named direction against the cone the constraints leave, then "
                           "decides the same question over every direction at once. Push the "
                           "price of pellets below zero and watch the verdict change while the "
                           "region does not.",
        }),
        "steps_title": "Working a covering model",
        "steps_intro": "Requirements first, then the certificate, then the answer. The middle step is the one that is usually assumed.",
        "steps": [
            ("Write one `≥` row per requirement, and check its units",
             "Grams of protein per kilogram times kilograms is grams of protein, and the "
             "requirement is grams of protein. A requirement written as `≤` is a different "
             "model with a cheapest answer of zero, and zero looks like an answer."),
            ("Ask what the region does far away from the origin",
             "List the directions in which it runs on forever. For a model whose rows are all "
             "`≥` with non-negative coefficients, every non-negative direction is one of them."),
            ("Certify the objective along those directions",
             "Compute `c·d` for each. If all of them are at or above zero the minimum exists "
             "and sits at a corner; if one is negative there is no minimum and the model, not "
             "the solver, is what needs changing."),
            ("Solve, then read the surpluses",
             "Name the requirements met exactly &mdash; surplus zero &mdash; and the ones "
             "over-delivered, each in its own unit. A requirement with surplus at the optimum "
             "is one the cheapest plan could not avoid exceeding."),
        ],
        "worked": {
            "title": "The cheapest ration, with the certificate first",
            "intro": [
                "The certificate is written before the corners on purpose. If the cost ran "
                "away, the corner arithmetic would be work spent on a question with no answer."
            ],
            "lines": [
                "minimise   2G + 3P        pounds",
                "  G + 3P  ≥  9            grams of protein",
                " 2G +  P  ≥  8            grams of fibre",
                "  G, P    ≥  0",
                "",
                "does the cost run away?",
                "  the region runs on forever along every non-negative direction",
                "  (1, 0):   cost change  2(1) + 3(0)  =  2       rises",
                "  (0, 1):   cost change  2(0) + 3(1)  =  3       rises",
                "  (1, 1):   cost change  2(1) + 3(1)  =  5       rises",
                "  over every direction at once:  no recession direction lowers the cost",
                "  so a minimum exists, and it is at a corner",
                "",
                "the corners",
                "  (0, 8)    cost 2(0) + 3(8)  = 24",
                "  (3, 2)    cost 2(3) + 3(2)  = 12      cheapest",
                "  (9, 0)    cost 2(9) + 3(0)  = 18",
                "",
                "at (3, 2)",
                "  protein   3 + 6   =  9  ≥  9     surplus 0 grams     met exactly",
                "  fibre     6 + 2   =  8  ≥  8     surplus 0 grams     met exactly",
            ],
            "after": [
                "Both requirements are met exactly, which is what a cost minimiser does when "
                "exceeding a requirement costs money and buys nothing. The surpluses are the "
                "structural reading of the answer: this ration has no room in it anywhere.",
                "For a faded rehearsal, raise the protein requirement from 9 grams to 12 and "
                "leave everything else alone. The supplied first move is the certificate: the "
                "costs have not changed, so the verdict cannot have changed, and the minimum "
                "still exists at a corner. Find the new cheapest ration and its cost as exact "
                "fractions, then say which requirements are met exactly at it &mdash; and "
                "check both against the lab before believing either.",
            ],
        },
        "quiz_title": "Requirements, surpluses and runaway costs",
        "quiz": [
            {"q": "The feasible region of the ration model runs on forever to the north-east. What does that tell you about the problem?",
             "a": ["That it is unbounded and has no answer",
                   "Nothing on its own: whether the cost falls forever along those directions is a separate question",
                   "That the cheapest ration is not at a corner",
                   "That one of the requirements is redundant"],
             "c": 1,
             "why": "With costs 2 and 3, every direction the region runs in raises the cost, "
                    "so the minimum exists and sits at a corner &mdash; it is 12 at `(3, 2)`. "
                    "Pay the merchant to remove pellets and the same region has no cheapest "
                    "ration, which shows the verdict was never about the shape."},
            {"q": "At `(4, 2)` the protein row `G + 3P ≥ 9` has a gap of 1. What is that 1?",
             "a": ["A gram of protein the ration supplies beyond the requirement",
                   "A kilogram of grain that could be removed",
                   "A pound of cost that could be saved",
                   "Slack, meaning a gram of protein left unused"],
             "c": 0,
             "why": "`4 + 6 = 10` against a requirement of 9, so the surplus is 1 gram of "
                    "protein: over-fulfilment. Calling it slack inverts the meaning, and "
                    "removing a kilogram of grain would take the protein to 7 and break the row."},
            {"q": "Which of these makes a covering model genuinely unbounded?",
             "a": ["A region with no boundary to the north-east",
                   "A requirement that is met exactly at the optimum",
                   "A negative cost on a feed the region lets you use without limit",
                   "Two requirements that are both tight at once"],
             "c": 2,
             "why": "Unboundedness needs a direction the region contains along which the "
                    "objective improves without limit. A disposal credit supplies one. The "
                    "other three describe the model as it stands, whose minimum is 12."},
            {"q": "A reader writes both requirements as `≤` by mistake. What does the model then report?",
             "a": ["Infeasible, because nothing satisfies both rows",
                   "The same answer, since the solver detects the intended direction",
                   "Unbounded, because the region now has no ceiling",
                   "A cheapest cost of 0, at the point where nothing is fed at all"],
             "c": 3,
             "why": "`G + 3P ≤ 9` and `2G + P ≤ 8` are satisfied at `(0, 0)`, which costs "
                    "nothing, so the model is feasible, bounded and about a ration that feeds "
                    "no animal. A wrong inequality direction produces an answer rather than a "
                    "complaint, which is why the units check on each row is worth the minute."},
        ],
        "mistakes": [
            ("Concluding that an unbounded region means an unbounded problem",
             "The region of every covering model runs on forever, and almost none of them is "
             "unbounded. What decides the question is whether some direction the region "
             "contains lowers the objective, which is arithmetic on `c·d` rather than a look at "
             "a diagram."),
            ("Testing a few directions and calling the result a certificate",
             "Three named directions that all raise the cost are evidence about those three. "
             "The claim needed is about every direction the region runs in at once, and it is "
             "decidable: the lab prints the named rows and then the verdict over the whole "
             "cone, separately, because they are different statements."),
            ("Writing a requirement as a ceiling",
             "`≤` where `≥` was meant leaves a model that is feasible and bounded and whose "
             "cheapest answer is to do nothing at all. Nothing in the solve objects. Reading "
             "each row aloud with its units &mdash; “the ration supplies at least 9 grams” "
             "&mdash; is what catches it."),
        ],
        "standard": ("Finish when you certify that the cost cannot run away before you enumerate anything.",
                     "You should be able to write requirements as `≥` rows with matching units, "
                     "say which directions the region runs in and what the objective does along "
                     "them, produce the cheapest point as exact fractions, and name the "
                     "requirements it meets exactly."),
        "note": "Both families so far compare a quantity with a number. The next one compares a quantity with a fraction of a total that the decisions themselves make up &mdash; which puts a decision in the denominator, and looks for a moment as though it has left the linear class altogether.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "blending-and-ratio-constraints",
        "title": "Blending and Ratio Constraints",
        "module": "The four model families",
        "one_line": "Clear a percentage requirement into a linear row, and say when clearing is legal.",
        "summary": (
            "“At least 30% of the blend is naphtha” has a decision in its denominator, and it "
            "is linear anyway: multiply out and the row becomes `(1 − t)` on the component "
            "named and `−t` on every other. Clearing is legal because the total is a quantity "
            "that cannot be negative, which is a condition to check rather than a step to "
            "take &mdash; and this lesson shows one ratio where it fails and declines it."
        ),
        "key": [
            "N ≥ 3/10 (N + R + B)                  as the specification states it",
            "(7/10)N − (3/10)R − (3/10)B ≥ 0       once the denominator is cleared",
            "",
            "B ≤ 1/4 (N + R + B)",
            "−(1/4)N − (1/4)R + (3/4)B ≤ 0",
            "",
            "share of a component  =  its litres ÷ the litres in the batch",
            "legal because the total cannot be negative;  N ÷ B ≥ 2 is not",
        ],
        "key_label": "A share, as stated and as cleared",
        "concepts_intro": (
            "One algebraic move, and the condition that makes it a rearrangement rather than a "
            "new statement. The condition is the lesson."
        ),
        "concepts": [
            ("A share is a fraction of a total the decisions themselves make up",
             "The batch is `N + R + B` litres, so “at least 30% naphtha” is `N ≥ 3/10 "
             "(N + R + B)`. The denominator is not data; it is the sum of the decisions, which "
             "is why the requirement looks non-linear and why writing `N ≥ 3/10` instead is "
             "about a different problem."),
            ("Clearing puts `(1 − t)` on the component and `−t` on every other",
             "Multiply out `N ≥ t(N + R + B)` and collect: `(1 − t)N − tR − tB ≥ 0`. Every "
             "variable appears, including the ones the requirement never mentioned, and that "
             "is the visible sign that a share is a statement about the whole batch."),
            ("Multiplying an inequality through is only a rearrangement when the multiplier cannot be negative or zero",
             "The total litres cannot be negative, so the move is legal here. `N ÷ B ≥ 2` is "
             "the same move applied to a denominator that a feasible blend can drive to zero, "
             "and `N − 2B ≥ 0` is then a different requirement rather than the same one "
             "rewritten."),
        ],
        "read_title": "Shares, clearing, and the ratio this lesson declines",
        "read_intro": "The requirement as stated, the row it becomes, the percentages achieved at the optimum, and the condition that makes the move legal.",
        "body": [
            ("p", "A refinery blends naphtha, reformate and butane into a 100-litre batch. At "
                  "least 30% of the batch must be naphtha and at most 25% of it may be butane; "
                  "naphtha costs 5 a litre, reformate 3 and butane 2. Minimise the cost of the "
                  "batch."),
            ("def", ("Share constraint",
                     "For decisions `x₁, …, xₙ` measured in the same unit, the requirement "
                     "“component `i` is at least a fraction `t` of the total” is "
                     "`xᵢ ≥ t(x₁ + … + xₙ)`. Collecting terms gives the linear row "
                     "`(1 − t)xᵢ − t(the rest) ≥ 0`, and “at most `t`” gives the same row with "
                     "the inequality reversed.",
                     "The right-hand side of the cleared row is 0, always. A share requirement "
                     "carries no constant: it compares one decision with a multiple of the sum "
                     "of all of them, and scaling the whole batch up or down does not change "
                     "whether it holds.")),
            ("math", [
                "minimise   5N + 3R + 2B                    pounds a batch",
                "subject to   N +  R +  B  = 100            litres in the batch",
                "",
                "  at least 30% naphtha     N ≥ 3/10 (N + R + B)",
                "  cleared                  (7/10)N − (3/10)R − (3/10)B ≥ 0",
                "",
                "  at most 25% butane       B ≤ 1/4 (N + R + B)",
                "  cleared                  −(1/4)N − (1/4)R + (3/4)B ≤ 0",
                "",
                "             N, R, B  ≥  0",
            ]),
            ("p", "The cheapest batch is 30 litres of naphtha, 45 of reformate and 25 of "
                  "butane, costing 335. Both share requirements are met exactly: the achieved "
                  "shares are 30%, 45% and 25%, printed as the exact fractions `3/10`, `9/20` "
                  "and `1/4` rather than as rounded percentages. The blend takes as much of the "
                  "cheap butane as the ceiling allows and as little of the expensive naphtha as "
                  "the floor allows, which is what the two bounds were written to control."),
            ("h3", "The quantity where a proportion was meant"),
            ("p", "Write the naphtha requirement as `N ≥ 3/10` instead and something worse than "
                  "an error happens: the model stays feasible and solvable, and it answers a "
                  "different question. The cheapest batch becomes `N = 3/10` litres, "
                  "`R = 747/10` litres and `B = 25` litres at a cost of 1378/5 &mdash; and the "
                  "naphtha share is 0.3%, not 30%. The variable is measured in litres and the "
                  "requirement, being a proportion, is measured in nothing; the two sides of "
                  "that row do not carry the same unit and no arithmetic will complain."),
            ("p", "A subtler version takes the share of the wrong total: `N ≥ 3/10 (R + B)` "
                  "asks for 30% of the others rather than 30% of the batch. It is a legal "
                  "linear row and a weaker requirement &mdash; it is satisfied at "
                  "`N = 300/13` litres, which is a naphtha share of `3/13`, about 23.08% of the "
                  "batch. Clearing is only as good as the total you cleared."),
            ("h3", "The ratio this lesson declines"),
            ("p", "The same move applied to `N ÷ B ≥ 2` gives `N − 2B ≥ 0`, and that is not a "
                  "rearrangement. Multiplying an inequality by `B` preserves it only when `B` "
                  "is strictly positive, and the question of whether it can vanish is itself a "
                  "linear programme: add `B ≤ 0` to the constraints and ask whether anything is "
                  "left."),
            ("example", ("Why `N ÷ B ≥ 2` may not be cleared here",
                         "The batch `(30, 70, 0)` fills 100 litres, is 30% naphtha and is "
                         "within the butane ceiling, so it is feasible with `B = 0`. At that "
                         "point `N ÷ B` is not a number at all, while `N − 2B ≥ 0` reads "
                         "`30 ≥ 0` and holds comfortably. The cleared row admits points the "
                         "original requirement says nothing about, so the lab declines the "
                         "move and says which feasible blend refutes it.")),
            ("p", "The honest form of the rule is therefore conditional. A ratio requirement "
                  "may be cleared when the denominator is a quantity the constraints keep "
                  "strictly positive &mdash; and when it is the total of the batch, that is "
                  "usually evident. When it is one component, it is a claim, and claims on "
                  "this course get checked."),
        ],
        "lab": ("lp", {
            "mode": "model",
            "preset": "blend",
            "panel_title": "Set the shares the specification demands",
            "panel_intro": "Three panels in a row: the requirement as the specification states "
                           "it, the same requirement with the denominator cleared, and the "
                           "share actually achieved at the optimum as an exact fraction. The "
                           "last row is a ratio whose denominator a feasible blend can drive to "
                           "zero, and the lab declines to clear it.",
        }),
        "steps_title": "Writing a share requirement",
        "steps_intro": "Four steps, of which the third is the one that separates a rearrangement from a new statement.",
        "steps": [
            ("Say what the total is, in words, before writing anything",
             "“30% of the batch” and “30% of the other components” are different requirements, "
             "and they differ by more than notation: the first gives a naphtha share of 30% "
             "and the second about 23%."),
            ("Write it as stated, with the total spelled out",
             "`N ≥ 3/10 (N + R + B)`, not `N ≥ 3/10`. Keeping the total visible for one line "
             "is what makes the next step a calculation rather than a guess."),
            ("Check the denominator cannot be zero or negative, then clear",
             "The total litres of a batch cannot be negative, so multiplying through preserves "
             "the inequality. Collect terms into `(1 − t)` on the component and `−t` on every "
             "other, with 0 on the right."),
            ("Solve, then read the achieved shares back",
             "Compute each component divided by the total at the optimum and compare it with "
             "what was required. A share that comes out wildly below its floor is the signature "
             "of a proportion written as a quantity."),
        ],
        "worked": {
            "title": "The batch, cleared and then checked",
            "intro": [
                "The clearing is three lines of algebra. The check at the end is what tells you "
                "the three lines were about the right total."
            ],
            "lines": [
                "as stated        N ≥ 3/10 (N + R + B)",
                "",
                "multiply out     N ≥ (3/10)N + (3/10)R + (3/10)B",
                "collect          N − (3/10)N − (3/10)R − (3/10)B ≥ 0",
                "                 (7/10)N − (3/10)R − (3/10)B ≥ 0",
                "",
                "legal because    N + R + B is litres in a batch, which cannot be negative",
                "",
                "the programme",
                "  minimise  5N + 3R + 2B",
                "    N + R + B = 100",
                "    (7/10)N − (3/10)R − (3/10)B ≥ 0",
                "    −(1/4)N − (1/4)R + (3/4)B ≤ 0",
                "    N, R, B ≥ 0",
                "",
                "optimum     N = 30,  R = 45,  B = 25        cost 335",
                "",
                "achieved shares",
                "  naphtha    30 ÷ 100  =  3/10   =  30%     required at least 30%",
                "  reformate  45 ÷ 100  =  9/20   =  45%     no share stated",
                "  butane     25 ÷ 100  =  1/4    =  25%     required at most 25%",
            ],
            "after": [
                "Both stated shares are met exactly, which is what happens when one bound "
                "forces expensive naphtha in and the other stops cheap butane taking over. The "
                "check is not ceremony: it is the only step that would notice the requirement "
                "had been written about the wrong total.",
                "For a faded rehearsal, tighten the butane ceiling from 25% to 10% and leave "
                "the naphtha floor alone. The supplied first move is the cleared form: only the "
                "coefficient `t` changes, so the row becomes `−(1/10)N − (1/10)R + (9/10)B ≤ 0`. "
                "Predict the new blend and its cost, compute the three achieved shares as exact "
                "fractions, and say which of the two bounds is now doing the work.",
            ],
        },
        "quiz_title": "Shares, cleared and declined",
        "quiz": [
            {"q": "“At least 30% of the batch is naphtha”, with a batch of `N + R + B` litres, is which row?",
             "a": ["`N ≥ 3/10`",
                   "`(7/10)N − (3/10)R − (3/10)B ≥ 0`",
                   "`N ≥ 3/10 (R + B)`",
                   "`10N − 3R − 3B ≥ 0`"],
             "c": 1,
             "why": "Multiplying out `N ≥ 3/10 (N + R + B)` and collecting gives `(1 − t)` on "
                    "naphtha and `−t` on the rest. `N ≥ 3/10` compares litres with a "
                    "proportion; `N ≥ 3/10 (R + B)` is 30% of the others, which is about 23% of "
                    "the batch; and the last row is that same weaker requirement multiplied "
                    "through by 10."},
            {"q": "Why is clearing the denominator of `N ≥ 3/10 (N + R + B)` legal?",
             "a": ["Because the inequality is not strict",
                   "Because a batch of 100 litres is a constant",
                   "Because the total litres in a batch cannot be negative, so multiplying through preserves the inequality",
                   "Because every coefficient of the cleared row is a fraction"],
             "c": 2,
             "why": "Multiplying an inequality by a quantity preserves its direction when the "
                    "quantity cannot be negative, and reverses it when the quantity is "
                    "negative. That the batch happens to be fixed at 100 litres in this "
                    "instance is not the reason: the cleared row is correct for any batch size, "
                    "which is why its right-hand side is 0."},
            {"q": "The lab declines to clear `N ÷ B ≥ 2` into `N − 2B ≥ 0`. What justifies declining?",
             "a": ["`N − 2B ≥ 0` is not a linear row",
                   "The constraints allow a feasible blend with `B = 0`, where the ratio is not a number at all",
                   "The two rows have different units",
                   "Ratios can never be written as linear constraints"],
             "c": 1,
             "why": "`(30, 70, 0)` is feasible, so the denominator can vanish, and at that "
                    "point the cleared row holds while the original says nothing. Clearing a "
                    "ratio is fine when the denominator is kept strictly positive by the "
                    "constraints; deciding whether it is, is itself a small linear programme."},
            {"q": "A reader writes the naphtha floor as `N ≥ 3/10` and solves. What happens?",
             "a": ["The solver reports that the row is dimensionally wrong",
                   "The model becomes infeasible",
                   "The model solves, and the cheapest batch is 0.3% naphtha at a cost of 1378/5",
                   "The model becomes non-linear"],
             "c": 2,
             "why": "Nothing objects. The row compares litres with a bare proportion, the "
                    "batch comes out at `N = 3/10` litres, and the cost 1378/5 is lower than "
                    "335 because the requirement that made naphtha expensive has evaporated. "
                    "Reading the achieved share back is what exposes it."},
        ],
        "mistakes": [
            ("Writing `N ≥ 0.3` where a proportion was meant",
             "The variable is litres and the requirement is a proportion, which is measured in "
             "nothing. The resulting model is feasible, solvable and about a different problem "
             "&mdash; the cheapest batch is three tenths of a litre of naphtha. Both sides of a "
             "row must carry the same unit, and a share requirement satisfies that only after "
             "the total has been multiplied back in."),
            ("Clearing a ratio whose denominator a feasible point can drive to zero",
             "`N ÷ B ≥ 2` becomes `N − 2B ≥ 0` only if `B` is kept strictly positive. Here a "
             "feasible blend has no butane in it at all, so the cleared row admits points the "
             "original requirement never spoke about. The condition is checkable and worth "
             "checking rather than assuming."),
            ("Taking the share of the wrong total",
             "“30% of the blend” includes the component being constrained; “30% of the "
             "remainder” does not. Both clear to legal linear rows, and they differ by about "
             "seven percentage points here. The safeguard is to compute the achieved share at "
             "the optimum and compare it with the number the specification asked for."),
        ],
        "standard": ("Finish when you state the condition before clearing, not after.",
                     "You should be able to turn a percentage requirement into a linear row "
                     "with 0 on the right, say why multiplying through was legal, compute the "
                     "achieved shares at the optimum as exact fractions, and refuse a ratio "
                     "whose denominator the constraints allow to vanish."),
        "note": "Each family so far has written its rows one situation at a time. The last of the four writes the same row `T` times over and links the periods to each other, and its one hard idea is what carries the link: a variable for the stock left at the end of each period, and one equation per period saying where that stock came from.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "multiperiod-planning-and-balance-constraints",
        "title": "Multiperiod Planning and Balance Constraints",
        "module": "The four model families",
        "one_line": "Link periods with one balance equation each, and read the production and inventory paths off the solution.",
        "summary": (
            "One equation per period, `Iₜ = Iₜ₋₁ + Pₜ − Dₜ`, is what ties a plan together: the "
            "stock carried out of a period is the stock carried in, plus what was made, minus "
            "what was sold. The inventory variable is the thing that carries the link, so it "
            "is a decision of the model rather than a formula, and one aggregate row about "
            "total production is not the same statement."
        ),
        "key": [
            "Iₜ = Iₜ₋₁ + Pₜ − Dₜ            one equation for each period",
            "written for a solver:   Pₜ + Iₜ₋₁ − Iₜ = Dₜ",
            "",
            "period 1 carries the opening stock:   P₁ − I₁ = 20 − 5",
            "Pₜ ≤ capacity,    Pₜ ≥ 0,    Iₜ ≥ 0",
            "",
            "one aggregate row instead:   P₁ + P₂ + P₃ + P₄ ≥ 105",
        ],
        "key_label": "The balance equation, and the row that is not the same thing",
        "concepts_intro": (
            "The shape is one equality repeated. What makes it work is that the quantity "
            "linking two periods is a variable the model may choose."
        ),
        "concepts": [
            ("Inventory is a decision variable, not a formula",
             "`Iₜ` is the stock in the store at the end of period `t`, in units. The plan "
             "chooses it, subject to the balance equation and to `Iₜ ≥ 0`. Substituting a "
             "formula for it collapses the link into the objective and makes the constraint "
             "that forbids a negative store impossible to write."),
            ("One equation per period, the same shape every time",
             "`Pₜ + Iₜ₋₁ − Iₜ = Dₜ` for each `t`, with the first period taking the opening "
             "stock as data. The rows are equalities: the stock does not merely satisfy an "
             "inequality, it is determined by where it came from, and it appears in exactly "
             "two of the rows &mdash; the period that carries it out and the period that "
             "carries it in."),
            ("The link is what forbids producing too late",
             "Demand in the second period must be met by stock that exists in the second "
             "period. The balance rows say so, period by period. A single row about total "
             "production over the horizon says something strictly weaker and cannot see the "
             "difference."),
        ],
        "read_title": "Balance equations, and the aggregate row that is not equivalent",
        "read_intro": "The equation each period contributes, what the inventory variable carries, and the plan an aggregate constraint prefers instead.",
        "body": [
            ("p", "A plant makes one product over four periods. Demand is 20, 35, 30 and 25 "
                  "units; making one unit costs 9, 8, 7 and 6 as the periods go on; at most 60 "
                  "units can be made in a period; carrying a unit into the next period costs "
                  "1; and there are 5 units in the store before the first period begins."),
            ("def", ("Balance constraint",
                     "For each period `t`, with `Pₜ` made, `Dₜ` demanded and `Iₜ` left in the "
                     "store at the end, the <strong>balance constraint</strong> is "
                     "`Iₜ = Iₜ₋₁ + Pₜ − Dₜ`, where `I₀` is the opening stock. Rearranged for a "
                     "solver, with the data on the right, it is `Pₜ + Iₜ₋₁ − Iₜ = Dₜ`.",
                     "With `Iₜ ≥ 0` for every `t`, the family of equations says exactly that "
                     "demand is met in the period it occurs, out of stock that exists by then. "
                     "Allowing `Iₜ` to go negative is a modelling decision with a name &mdash; "
                     "a backorder &mdash; and it has to be made deliberately.")),
            ("math", [
                "                        period 1   period 2   period 3   period 4",
                "  demand                   20         35         30         25",
                "  cost to make one          9          8          7          6",
                "",
                "  opening stock 5,  capacity 60 a period,  1 to carry a unit onward",
                "",
                "minimise  9P₁ + 8P₂ + 7P₃ + 6P₄ + I₁ + I₂ + I₃ + I₄",
                "",
                "  P₁           − I₁       =  15        20 demanded, 5 already in the store",
                "  P₂ + I₁      − I₂       =  35",
                "  P₃ + I₂      − I₃       =  30",
                "  P₄ + I₃      − I₄       =  25",
                "  P₁, …, P₄               ≤  60",
                "  every P and every I     ≥   0",
            ]),
            ("p", "The cheapest plan makes 15, 35, 30 and 25 and carries nothing at any point, "
                  "at a cost of 775. That is worth reading rather than accepting: making a unit "
                  "gets cheaper every period and carrying one costs money, so there is no "
                  "reason to build stock and every reason to make each unit as late as the "
                  "balance rows allow &mdash; which is the period it is sold in."),
            ("example", ("When the store earns its keep",
                         "Cut the capacity to 30 a period and raise the second period's demand "
                         "to 40. Now the second period cannot make what it sells, so the plan "
                         "makes 25 in the first period, carries 10 units forward, and makes 30, "
                         "30 and 25 after that, at a cost of 835. The first inventory variable "
                         "is 10, and it is the only thing in the model that could have made the "
                         "second period feasible at all.")),
            ("h3", "The aggregate row, and the plan it prefers"),
            ("p", "The tempting simplification is one row instead of four: total production at "
                  "least total demand. With 110 units demanded and 5 in the store that is "
                  "`P₁ + P₂ + P₃ + P₄ ≥ 105`, and the inventory variables disappear along with "
                  "the balance equations."),
            ("p", "It solves, and it is cheaper: 675 against 775. The plan it prefers makes "
                  "nothing at all in the first two periods and then 45 and 60 in the last two, "
                  "because production is cheapest at the end and nothing in the model any "
                  "longer says when a unit has to exist. Run that plan through the periods and "
                  "15 units of demand go unmet in the first period and 35 in the second: fifty "
                  "units of demand unserved, by a plan the objective calls better."),
            ("p", "This is the sharpest example on the course of a model being exactly wrong. "
                  "Nothing is infeasible, no arithmetic is off, and the reported cost is a real "
                  "number about a plan nobody would run. The aggregate row is a true statement "
                  "about the plan; it is simply a much weaker one than the four rows it "
                  "replaced, and the cost cannot show what was lost."),
            ("p", "The same weakening is available inside the balance rows themselves. Drop "
                  "`I₂ ≥ 0` and the second period's row is satisfied by `I₂ = −35` with nothing "
                  "made, which reads as thirty-five units promised and not delivered. If "
                  "backorders are what the situation allows, that is a variable to introduce "
                  "and price on purpose; if they are not, the sign restriction is the row that "
                  "says so."),
        ],
        "lab": ("lp", {
            "mode": "model",
            "preset": "multiperiod",
            "panel_title": "Set the demands, then replace the balance rows with one aggregate row",
            "panel_intro": "One balance equation per period says stock carried out is stock "
                           "carried in plus what was made minus what was sold. The selector "
                           "swaps all of them for the single row “total made is at least total "
                           "demand”, and the table beside it shows the plan that then becomes "
                           "optimal and the demand that plan misses.",
        }),
        "steps_title": "Writing a plan over periods",
        "steps_intro": "The variables come in two families and the rows come one per period. Doing the first period separately is what keeps the opening stock honest.",
        "steps": [
            ("Two variables per period, with units",
             "`Pₜ` is units made in period `t` and `Iₜ` is units in the store at the end of it. "
             "A four-period plan therefore has eight decisions, not four, and the second "
             "family is the one that carries the link."),
            ("Write the balance equation for a middle period first",
             "`Pₜ + Iₜ₋₁ − Iₜ = Dₜ`. Get the signs right where the pattern is plain: what was "
             "carried in is added, what is carried out is subtracted, and the demand is on the "
             "right with the data."),
            ("Then do the first period by hand",
             "There is no `I₀` variable: the opening stock is data, so the first row is "
             "`P₁ − I₁ = D₁ − (opening stock)`. Copying the middle pattern into the first "
             "period is the error this step exists to prevent."),
            ("Solve, then read both paths and the store",
             "Report `Pₜ` and `Iₜ` for every period, not just the total cost. A plan is a path "
             "through the horizon, and whether it ever holds stock is the thing the balance "
             "rows were written to decide."),
        ],
        "worked": {
            "title": "The aggregate plan, run through the periods one at a time",
            "intro": [
                "The aggregate row's plan costs less than the balance plan. Running it forward "
                "period by period is what shows why the number is not the answer."
            ],
            "lines": [
                "aggregate row      P₁ + P₂ + P₃ + P₄ ≥ 105        cost 675",
                "the plan it picks  P = (0, 0, 45, 60)",
                "",
                "period   opening   made   available   demand   sold   short   closing",
                "   1         5        0        5         20      5      15       0",
                "   2         0        0        0         35      0      35       0",
                "   3         0       45       45         30     30       0      15",
                "   4        15       60       75         25     25       0      50",
                "",
                "demand unserved    15 + 35 = 50 units",
                "left in the store  50 units, made too late to sell",
                "",
                "balance rows       P = (15, 35, 30, 25),  I = (0, 0, 0, 0)     cost 775",
                "demand unserved    0",
            ],
            "after": [
                "The aggregate plan satisfies its one row exactly &mdash; 105 units made "
                "&mdash; and misses fifty units of demand, then finishes with fifty units in "
                "the store. Both facts follow from the same thing: the row counts units over "
                "the whole horizon and says nothing about when they exist.",
                "For a faded rehearsal, keep the balance rows and cut the capacity to 30 a "
                "period. The supplied first move is where the trouble must be: the second "
                "period demands 35 and can make at most 30, so its row can only be satisfied "
                "with stock carried in. Predict `P₁` and `I₁`, then the rest of both paths and "
                "the cost, and check them against the lab &mdash; and say what happens to the "
                "model when the capacity goes to 20.",
            ],
        },
        "quiz_title": "Balance, inventory and aggregation",
        "quiz": [
            {"q": "Why is `Iₜ` a variable of the model rather than an expression computed afterwards?",
             "a": ["Because the objective has to charge for holding it",
                   "Because it is what the balance equations link two periods with, and `Iₜ ≥ 0` has to be a row",
                   "Because the solver cannot evaluate expressions",
                   "Because demand is data and inventory is not"],
             "c": 1,
             "why": "`Iₜ` appears in the row that carries it out of one period and the row that "
                    "carries it into the next; that is the link. And the store cannot go "
                    "negative, which is a constraint on a variable &mdash; not something you "
                    "can say about a quantity you never introduced. Charging for it is a "
                    "consequence, not the reason."},
            {"q": "The first period's balance row is `P₁ − I₁ = 15`, with demand 20. Where did the 15 come from?",
             "a": ["The capacity of 60, scaled down",
                   "Demand of 20 minus the 5 units already in the store",
                   "The cost of 9 subtracted from demand",
                   "Demand of 20 minus the holding cost of 5"],
             "c": 1,
             "why": "There is no `I₀` variable, because the opening stock is data. It moves to "
                    "the right-hand side, so the first row asks for `20 − 5` and every later "
                    "row keeps the `Iₜ₋₁` term as a variable."},
            {"q": "Replacing the four balance rows with `P₁ + P₂ + P₃ + P₄ ≥ 105` gives a cost of 675 against 775. What has happened?",
             "a": ["A better plan has been found, and the balance rows were redundant",
                   "The model is now infeasible in the first two periods",
                   "The aggregate row is a weaker statement, and its cheaper plan leaves fifty units of demand unserved",
                   "The holding cost was double-counted in the original"],
             "c": 2,
             "why": "The aggregate plan makes nothing until the third period, when production is "
                    "cheap, and 15 then 35 units of demand go unmet before it starts. Both "
                    "models are feasible and correctly solved; one of them is about a different "
                    "situation."},
            {"q": "Someone drops the sign restriction `I₂ ≥ 0`. What does the second period's row then permit?",
             "a": ["Nothing new, since inventory is obviously not negative",
                   "A plan that makes nothing in the period and records `I₂ = −35`, which is thirty-five units promised and not delivered",
                   "An infeasible model, because an equality cannot hold with a negative variable",
                   "A plan that exceeds the capacity of 60"],
             "c": 1,
             "why": "`P₂ + I₁ − I₂ = 35` with `P₂ = 0` and `I₁ = 0` is satisfied by "
                    "`I₂ = −35`. Negative stock is a backorder, and it is a modelling choice "
                    "with a price attached rather than an accident to leave lying in the model."},
        ],
        "mistakes": [
            ("Replacing the balance rows with one aggregate row",
             "“Total production at least total demand” sounds equivalent and is strictly "
             "weaker: it is satisfied by making everything in the last period, after every "
             "earlier demand has already gone unmet. Here it is 100 pounds cheaper and misses "
             "fifty units, and the objective cannot show either fact."),
            ("Copying the middle-period pattern into the first period",
             "The first row has no `Iₜ₋₁` variable in it, because the opening stock is data. "
             "Writing `P₁ + I₀ − I₁ = D₁` with `I₀` as a variable hands the plan a free store "
             "to draw on, and the symptom is a first period that makes suspiciously little."),
            ("Treating the store as something that can go negative",
             "Without `Iₜ ≥ 0`, a balance equation is satisfied by unmet demand recorded as "
             "negative stock, and the plan that results looks cheap. Backorders may well be "
             "what the situation allows &mdash; then they get their own variable and their own "
             "cost, on purpose."),
        ],
        "standard": ("Finish when you write the middle period first and the first period by hand.",
                     "You should be able to declare two variables per period with units, write "
                     "one balance equality per period with the opening stock handled separately, "
                     "read the production and inventory paths off the solution, and say what an "
                     "aggregate row would fail to say."),
        "note": "That is the four families, and every row in them was linear as written or after one multiplication. The rest of the course is about requirements that are not: an absolute value, a largest-of-several cost, a price that changes at a break point, a variable allowed to go negative. One of the four is legal whichever way the objective is pushed and the other three are not, which is what “Reformulations That Keep Linearity” is about.",
    },
]
