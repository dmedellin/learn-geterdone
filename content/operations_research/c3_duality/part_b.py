"""Duality and Sensitivity Analysis, lessons 06-10.

The second ranging computation, the two questions about something not in the
model, the method that re-optimises instead of restarting, and the two places
where duality is the content rather than the method.

Every figure below is read off the kit -- scripts/mathpath/labs/duality.py --
and the parametric lesson follows the kit's own parametrisation,
max (1 - L)f1 + L f2, which is the one its slider is labelled with.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "objective-coefficient-ranging-and-reduced-costs",
        "title": "Objective Coefficient Ranging",
        "module": "What the tableau knows",
        "one_line": "Range one coefficient that is being made and one that is not, and say for a given change whether the plan moves or only the total.",
        "summary": (
            "Moving what a basic activity earns changes the total but not the corner, until the "
            "coefficient crosses a value at which some reduced cost hits zero. Moving what a "
            "nonbasic activity earns changes nothing at all until it has improved by exactly its "
            "reduced cost. Two different ratio tests, and which one applies depends only on "
            "whether the activity is in the basis &mdash; so the first question to ask about a "
            "coefficient is whether the plan currently makes any of that product."
        ),
        "key": [
            "basic j     range from a ratio test of the z-row against row j of B⁻¹A",
            "            inside it the plan does not move;  z* moves by (Δcⱼ)(xⱼ)",
            "nonbasic j  the range is cⱼ up to cⱼ + its reduced cost;  nothing moves",
            "three activities at (2, 6, 0), z* = 46, y = (3, 2, 0):",
            "     c1 = 8 over 5 ≤ c1 ≤ 10       c2 = 5 over 4 ≤ c2 ≤ 8",
            "     c3 = 3, reduced cost 4, range c3 ≤ 7        nothing until 7",
            "c1 = 9 → still (2, 6, 0), z* = 48;   c1 = 10 → (4, 2, 0) ties at 50",
        ],
        "key_label": "Two computations, and the one question that chooses between them",
        "concepts_intro": (
            "One hard idea: the answer to a corner problem does not care about the objective "
            "until a sign changes. The rest is keeping the two cases apart."
        ),
        "concepts": [
            ("A corner does not move until a reduced cost changes sign",
             "The optimal plan is a vertex, and which vertex is best is decided by the signs of "
             "the objective-row entries rather than by their sizes. Move a coefficient a little "
             "and every one of those signs is unchanged, so the same vertex is still best and "
             "only the total moves. The answer changes at one value, not gradually."),
            ("A basic coefficient moves the whole objective row",
             "If `xⱼ` is basic then `cⱼ` appears in `c_B`, so changing it changes every entry of "
             "`c_BᵀB⁻¹A − c`. Each nonbasic column gives one bound on the change, from its "
             "reduced cost divided by its entry in `xⱼ`'s row of the tableau, and the binding "
             "ones are the two ends. Inside the interval the plan is unchanged and `z*` moves by "
             "`Δcⱼ` times how much of `xⱼ` the plan makes."),
            ("A nonbasic coefficient does nothing until it catches up",
             "If `xⱼ` is not in the basis its reduced cost is `yᵀaⱼ − cⱼ > 0`, and only `cⱼ`'s "
             "own entry changes when `cⱼ` moves. So the range is one-sided: anything downwards, "
             "and upwards exactly as far as the reduced cost, at which point the column is worth "
             "bringing in. Below that value nothing changes &mdash; not the plan, not the total, "
             "not any other range."),
        ],
        "read_title": "The two ranging computations, and which one a coefficient gets",
        "read_intro": "Why the basis is the deciding question, what each ratio test looks like, and what changes at the end of each kind of interval.",
        "body": [
            ("def", ("Reduced cost",
                     "The <strong>reduced cost</strong> of column `j` is `yᵀaⱼ − cⱼ`, the "
                     "objective-row entry over that column at the optimum. For a maximisation it "
                     "is zero on every basic column and non-negative on every other one.",
                     "Read as a sentence it is the amount by which what one unit of activity `j` "
                     "would consume, valued at the current prices, exceeds what it earns. A "
                     "nonbasic activity is not made because that number is positive.")),
            ("p", "Right-hand-side ranging asked how far the data could move while the basis "
                  "stayed <em>feasible</em>. This lesson asks how far it can move while the "
                  "basis stays <em>optimal</em>. Those are different questions about different "
                  "halves of the tableau: `b` appears only in the right-hand column, and the "
                  "objective coefficients appear only in the objective row. Which is why one is "
                  "a ratio test down a column and the other is a ratio test along a row."),
            ("thm", ("The two ranges",
                     "Let the simplex method finish with basis `B`, plan `x`, prices `y` and "
                     "reduced costs `rⱼ = yᵀaⱼ − cⱼ`.",
                     "If `xⱼ` is <strong>basic</strong>, occupying row `p` of the tableau, then "
                     "the basis stays optimal for `cⱼ + Δ` exactly while "
                     "`rₖ + Δ·(row p of B⁻¹A)ₖ ≥ 0` for every nonbasic `k` &mdash; one bound per "
                     "nonbasic column, `Δ` bounded above by the smallest `rₖ / (−a_pk)` over "
                     "negative entries and below by the largest over positive ones. Inside, the "
                     "plan is unchanged and `z*` becomes `z* + Δxⱼ`.",
                     "If `xⱼ` is <strong>nonbasic</strong>, the basis stays optimal exactly while "
                     "`Δ ≤ rⱼ`, with no lower bound at all. Inside, neither the plan nor `z*` "
                     "changes.")),
            ("math", [
                "three activities   max 8x1 + 5x2 + 3x3",
                "   machine   2x1 +  x2 +  x3 ≤ 10",
                "   labour     x1 +  x2 + 2x3 ≤  8",
                "   contract   x1            ≤  4",
                "",
                "optimum   x = (2, 6, 0)   z* = 46   y = (3, 2, 0)",
                "",
                "reduced costs    x1: 0    x2: 0    x3: y'a3 − c3 = 3 + 4 − 3 = 4",
                "",
                "               coefficient   made?    range        at the ends",
                "   c1 = 8        basic        yes     5 ≤ c1 ≤ 10   40 and 50",
                "   c2 = 5        basic        yes     4 ≤ c2 ≤  8   40 and 64",
                "   c3 = 3        nonbasic     no      c3 ≤ 7        46 at 7",
                "",
                "inside a basic range      c1 = 9:   plan still (2, 6, 0),  z* = 48",
                "at its end                c1 = 10:  (2, 6, 0) and (4, 2, 0) BOTH earn 50",
                "inside a nonbasic range   c3 = 6:   plan still (2, 6, 0),  z* = 46",
                "past its end              c3 = 8:   plan becomes (4, 0, 2), z* = 48",
            ]),
            ("example", ("A coefficient that is being made",
                         "`c1 = 8` is basic, and the plan makes 2 of it. Its range is "
                         "`5 ≤ c1 ≤ 10`. Raise it to 9 and the plan does not move at all: still "
                         "`(2, 6, 0)`, and the total goes from 46 to `46 + 1(2) = 48`. That is "
                         "the whole of the inside of a basic range &mdash; a different number "
                         "and the same decision.",
                         "At `c1 = 10` something exact happens: a reduced cost is precisely "
                         "zero, and `(4, 2, 0)` earns 50 as well. Both corners are optimal and "
                         "one pivot moves between them. Past 10 the answer really is `(4, 2, 0)` "
                         "and the plan has changed once, at a value the lab prints.")),
            ("h3", "The other computation, which is smaller and easier to get wrong"),
            ("example", ("A coefficient that is not being made",
                         "`c3 = 3` is nonbasic with a reduced cost of 4, so its range is "
                         "`c3 ≤ 7`. Raise it from 3 to 6 and nothing whatever happens: the plan "
                         "is still `(2, 6, 0)` and the total is still 46. The third product got "
                         "twice as profitable and it is still not worth making.",
                         "At `c3 = 7` the reduced cost is exactly zero and `(4, 0, 2)` also earns "
                         "46. At `c3 = 8` the answer moves: `(4, 0, 2)` with a total of 48. So "
                         "the improvement needed before anything happens is exactly the reduced "
                         "cost, and the range is one-sided because making the product even less "
                         "profitable cannot make it worth starting.")),
            ("p", "Two things about that one-sidedness are worth saying out loud. An interval "
                  "unbounded below is a complete answer, not a missing number &mdash; the lab "
                  "prints it as such. And the value at which a nonbasic coefficient matters is "
                  "`cⱼ + rⱼ`, which is `yᵀaⱼ`: the coefficient becomes interesting exactly when "
                  "it reaches what the activity's ingredients are already worth. That is the "
                  "next lesson's question asked about a column already in the model."),
            ("h3", "Which of the plan and the value changes"),
            ("p", "So the answer to any single stated change comes in two parts, and the "
                  "commonest error is to give only one of them. Inside a basic range: the plan "
                  "does not change and the value does, by `Δcⱼ` times the amount made. Inside a "
                  "nonbasic range: neither changes. At the end of either: two plans tie, both "
                  "optimal, one pivot apart. Past the end: the plan has changed, and the old "
                  "range no longer describes anything."),
            ("example", ("The same ranging on a minimisation",
                         "`min 2x + 3y` subject to `x + y ≥ 4`, `x ≤ 3`, `y ≥ 1` costs 9 at "
                         "`(3, 1)`. The first ingredient may cost anything from 0 to 3: at "
                         "`c = 3/2` the total is `15/2` with nothing tied, and at either end of "
                         "the interval two plans tie, costing 3 at the bottom and 12 at the "
                         "top.",
                         "The second ingredient's range is `2 ≤ c` with no upper end, and at "
                         "`c = 2` the total is 8. Both are ranges in exactly the sense above; "
                         "what has changed is only that the solver negates a minimisation on the "
                         "way in, so a coefficient handed to it has to be negated too. A kit "
                         "that skipped that would print intervals that look like intervals and "
                         "endpoints that are not endpoints.")),
        ],
        "lab": ("duality", {
            "mode": "cost",
            "preset": "three",
            "panel_title": "Move what one activity earns",
            "panel_intro": "Pick something the plan makes and something it does not, and watch "
                           "the two computations differ. The answer changes exactly once, at a "
                           "value the panel prints, and the pivot to the new corner is performed "
                           "there so that you see the change happen rather than accumulate.",
        }),
        "steps_title": "Ranging one objective coefficient",
        "steps_intro": "Ask the basis question first. Everything after it depends on the answer, and the two computations look alike on the page.",
        "steps": [
            ("Ask whether the plan makes any of that activity",
             "If it is in the basis, you are ranging along its row of the tableau against every "
             "nonbasic column. If it is not, the answer is its reduced cost and you are nearly "
             "done. Getting this backwards produces an interval of the wrong shape, which is "
             "hard to notice."),
            ("For a nonbasic activity, read its reduced cost and stop",
             "The range is everything downwards and `rⱼ` upwards. Inside it, nothing changes at "
             "all &mdash; say so explicitly, because the expected answer is that a better "
               "coefficient must do something."),
            ("For a basic activity, take the ratio test along its row",
             "One bound per nonbasic column: that column's reduced cost divided by its entry in "
             "this activity's row. Negative entries bound the increase, positive entries bound "
             "the decrease, and a side with no entries at all is unbounded."),
            ("State both halves of the answer for the change you were asked about",
             "Does the plan move, and does the value move? Inside a basic range only the value "
             "moves, by `Δcⱼ` times how much is made. Inside a nonbasic range neither moves. At "
             "an endpoint two plans tie and both are optimal."),
        ],
        "worked": {
            "title": "One coefficient that is made and one that is not",
            "intro": [
                "The same programme, the same tableau, two coefficients, and two computations "
                "with nothing in common but the object they are read off."
            ],
            "lines": [
                "programme   max 8x1 + 5x2 + 3x3",
                "            machine   2x1 +  x2 +  x3 ≤ 10",
                "            labour     x1 +  x2 + 2x3 ≤  8",
                "            contract   x1            ≤  4",
                "optimum     x = (2, 6, 0)   z* = 46   y = (3, 2, 0)",
                "",
                "CASE 1      c1 = 8, and the plan makes 2 of x1, so x1 is basic",
                "",
                "  range     5 ≤ c1 ≤ 10          from the ratio test along x1's row",
                "",
                "  at c1 = 9     Δ = +1, inside the range",
                "      plan    unchanged, (2, 6, 0)",
                "      value   46 + 1(2) = 48         because the plan makes 2 of it",
                "",
                "  at c1 = 10    Δ = +2, the upper end",
                "      a reduced cost is exactly 0, and TWO plans earn 50:",
                "          (2, 6, 0):  10(2) + 5(6) = 50",
                "          (4, 2, 0):  10(4) + 5(2) = 50",
                "      one pivot moves between them; both are optimal",
                "",
                "  at c1 = 5     Δ = −3, the lower end",
                "      (2, 6, 0) and (0, 8, 0) both earn 40",
                "",
                "CASE 2      c3 = 3, and the plan makes none of x3, so x3 is nonbasic",
                "",
                "  the column    a3 = (1, 2, 0)   one machine hour, two labour, no contract",
                "  reduced cost  y'a3 − c3 = 3(1) + 2(2) + 0(0) − 3 = 7 − 3 = 4",
                "",
                "  the trap      taking (1, 1, 0) off the wrong row gives",
                "                3(1) + 2(1) + 0(0) − 3 = 5 − 3 = 2, and a range",
                "                ending at 5 that looks entirely reasonable",
                "",
                "  range     c3 ≤ 7          that is, c3 ≤ 3 + 4, and nothing below",
                "",
                "  at c3 = 6     inside the range",
                "      plan    unchanged, (2, 6, 0)",
                "      value   unchanged, 46          nothing happens at all",
                "",
                "  at c3 = 7     the end: (4, 0, 2) also earns 46, and ties",
                "  at c3 = 8     the plan MOVES to (4, 0, 2), and z* = 48",
            ],
            "after": [
                "The trap line in case 2 is the error worth seeing once. The third column of "
                "this programme is `(1, 2, 0)`, and reading `(1, 1, 0)` off the wrong row gives "
                "a reduced cost of 2 and a range ending at 5 &mdash; an interval that looks "
                "perfectly reasonable and that predicts, at `c3 = 6`, a change which does not "
                "happen. Nothing about the wrong answer announces itself; only checking the "
                "column against the original model does.",
                "Notice also that `c3 + r3 = 7 = yᵀa3`: the coefficient starts to matter exactly "
                "when it reaches what the activity's ingredients are already worth at the current "
                "prices. That is the same test the next lesson applies to a column that is not "
                "in the model at all.",
                "For a faded rehearsal, range `c2` on the same programme. The supplied move is "
                "that `x2` is basic, so this is the ratio test along `x2`'s row. Find the "
                "interval, then answer three questions before checking: what happens at "
                "`c2 = 6`, what happens at `c2 = 8`, and which second plan ties there.",
            ],
        },
        "quiz_title": "Which computation, and what changes",
        "quiz": [
            {"q": "`c1 = 8` is basic with range `5 ≤ c1 ≤ 10`, the plan is `(2, 6, 0)` and `z* = 46`. What happens at `c1 = 9`?",
             "a": ["The plan moves to a new corner",
                   "The plan stays `(2, 6, 0)` and `z*` becomes 48",
                   "The plan stays `(2, 6, 0)` and `z*` stays 46",
                   "The plan stays `(2, 6, 0)` and `z*` becomes 47"],
             "c": 1,
             "why": "9 is inside the range, so the corner is unchanged, and the value moves by "
                    "the change in the coefficient times how much of that activity the plan "
                    "makes: `46 + 1(2) = 48`. `47` would be the answer if the plan made one unit "
                    "rather than two, and `46` is what happens inside a <em>nonbasic</em> range, "
                    "which is the other computation."},
            {"q": "`c3 = 3` is nonbasic with reduced cost 4, so its range is `c3 ≤ 7`. What happens at `c3 = 6`?",
             "a": ["Nothing at all: the plan is still `(2, 6, 0)` and `z*` is still 46",
                   "`z*` rises by 3, to 49",
                   "`x3` enters the basis and the plan moves",
                   "The plan moves to `(4, 0, 2)` and `z*` becomes 48"],
             "c": 0,
             "why": "6 is inside the range, and inside a nonbasic range neither the plan nor the "
                    "value changes &mdash; the activity is still not made, so a better "
                    "coefficient on it earns nothing. The last choice is what happens at "
                    "`c3 = 8`, past the end; `z*` rising by 3 would require the plan to be making "
                    "one unit of `x3`, and it is making none."},
            {"q": "`c3 = 3` and `x3` is nonbasic. By how much must `c3` improve before the plan changes at all?",
             "a": ["`2`", "`3`", "`4`", "`7`"],
             "c": 2,
             "why": "By its reduced cost. `yᵀa3 = 3(1) + 2(2) + 0(0) = 7` against a coefficient "
                    "of 3, so the reduced cost is 4: at `c3 = 7` two plans tie and past it the "
                    "answer moves to `(4, 0, 2)`. `7` is the value the coefficient must reach "
                    "rather than the improvement needed, `3` is the coefficient itself, and `2` "
                    "is what you get from reading the wrong column, `(1, 1, 0)` instead of "
                    "`(1, 2, 0)`."},
            {"q": "Which of the two ranging computations applies to a coefficient is decided by what?",
             "a": ["Whether that activity is in the basis",
                   "Whether the coefficient is positive",
                   "Whether the row it appears in is tight",
                   "Whether the programme is a maximisation or a minimisation"],
             "c": 0,
             "why": "Basic and nonbasic are the two cases, and nothing else is: a basic "
                    "coefficient moves the whole objective row and needs a ratio test along its "
                    "own row of the tableau; a nonbasic one moves a single entry and its range is "
                    "read straight off the reduced cost. Maximisation versus minimisation changes "
                    "the direction of the tests, not which one you run."},
        ],
        "mistakes": [
            ("Expecting any change to the objective to change the answer",
             "Most changes move only the number. The optimal plan is a corner, and which corner "
             "is best is decided by the signs of the reduced costs rather than by their "
             "magnitudes &mdash; so the plan sits still through the whole interior of its range "
             "and then moves once, at a value you can compute in advance. A reader who expects "
             "gradual movement will keep looking for it, and the slider in the lab is there to "
             "show that it never arrives."),
            ("Running the basic computation on a nonbasic coefficient, or the reverse",
             "They look alike on the page and they answer different questions. A nonbasic range "
             "is one-sided and its end is `cⱼ` plus a reduced cost; a basic range is two-sided "
             "and both ends come from a ratio test along a row of the tableau. Ask whether the "
             "plan makes any of that product before doing any arithmetic at all."),
            ("Reading the reduced cost off the wrong column",
             "`yᵀaⱼ` needs the `j`-th column of the original matrix, and taking the numbers from "
             "the wrong row of the model produces a plausible reduced cost and a plausible range "
             "that predict changes at the wrong value. On the three-activity programme the true "
             "column is `(1, 2, 0)` and the reduced cost is 4; reading `(1, 1, 0)` gives 2 and an "
             "interval ending at 5, and nothing about that interval looks wrong."),
        ],
        "standard": ("Finish when you can say, for any stated change to a coefficient, whether the plan moves and whether the total does.",
                     "You should be able to decide which of the two computations applies from the "
                     "basis alone, produce the interval either way &mdash; including a one-sided "
                     "one &mdash; compute the new total inside a basic range, and describe what "
                     "happens exactly at an endpoint: two plans, both optimal, one pivot "
                     "apart."),
        "note": 'The value at which a nonbasic coefficient begins to matter is `cⱼ` plus its reduced cost, which is `yᵀaⱼ` &mdash; what the activity\'s ingredients are already worth at the current prices. That is the same test the next lesson runs on a column that is not in the model at all, and chaining this ranging over a weight is the whole of “Parametric Objectives and the Pareto Front”.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "pricing-a-new-activity-and-adding-a-constraint",
        "title": "Pricing a New Activity, Adding a Constraint",
        "module": "What the tableau knows",
        "one_line": "Price a product that is not in the model and test a rule that is not, both from the tableau you already have.",
        "summary": (
            "A column that is not in the model is priced by what it earns less what it would "
            "consume at the prices you already have, and a row that is not in the model is "
            "tested by evaluating it at the plan you already have. Both questions are answered "
            "from the final tableau, and only a favourable price or a broken rule costs anything "
            "further. A profitable product can still be the wrong thing to make, and that is the "
            "point of the lesson."
        ),
        "key": [
            "new column   cₙₑw − yᵀaₙₑw       with the prices already in the tableau",
            "             positive ⟹ it enters, and ONE pivot is the re-optimisation",
            "new row      evaluate it at the current plan",
            "             satisfied ⟹ nothing follows;  broken ⟹ restore feasibility",
            "workshop y = (0, 3/2, 1), plan (2, 6), z* = 36:",
            "   a = (1, 1, 1) earning 4:   4 − 5/2 = 3/2  > 0,  enters,  36 → 39",
            "   a = (1, 2, 3) earning 4:   4 − 6 = −2,  profitable and still wrong",
            "   rule x1 + x2 ≤ 5 reads 8:  broken by 3.    x1 + x2 ≤ 10 reads 8:  2 spare",
        ],
        "key_label": "Two questions, one tableau, and no re-solve unless the answer says so",
        "concepts_intro": (
            "One hard idea, which is that profit is not the test. The second panel is the same "
            "trick applied to a row instead of a column."
        ),
        "concepts": [
            ("A column is priced against what it would displace",
             "The prices already say what each resource is worth in the plan you have. A new "
             "activity consuming `aₙₑw` would take `yᵀaₙₑw` worth of that out of other "
             "activities, so the only figure that matters is `cₙₑw − yᵀaₙₑw`. Positive means it "
             "pays for what it displaces; negative means making it would lower the total, "
             "however profitable it looks on its own."),
            ("A row is tested by substitution, and usually does nothing",
             "A proposed constraint either the current plan satisfies or it does not. If it "
             "does, the plan is still feasible and still optimal &mdash; adding the rule changes "
             "nothing, costs nothing and needs no arithmetic beyond the substitution. If it does "
             "not, the current basis is still a basis of the new problem and only feasibility has "
             "to be restored."),
            ("Neither answer costs a re-solve by itself",
             "Both questions are one dot product against numbers already computed. The work only "
             "begins when a column prices favourably &mdash; one pivot &mdash; or a row is "
             "broken, which is the next lesson. Deciding cheaply whether to do any work is most "
             "of what sensitivity analysis is for."),
        ],
        "read_title": "What a product you have never made is worth, and whether a new rule matters",
        "read_intro": "The pricing formula and the two ways it comes out, the substitution test for a row, and why a rule can only ever cost.",
        "body": [
            ("def", ("The reduced cost of a column not in the model",
                     "For a proposed activity with column `aₙₑw` and objective coefficient "
                     "`cₙₑw`, its <strong>reduced cost</strong> at the current optimum is "
                     "`cₙₑw − yᵀaₙₑw`, where `y` is the price vector already in the final "
                     "tableau. For a maximisation the activity is worth introducing exactly when "
                     "that number is positive.",
                     "Nothing about this formula requires the column to have been in the model "
                     "when it was solved. The prices are properties of the basis, and any column "
                     "at all can be valued against them.")),
            ("p", "That is the same expression as the objective-row entry over a column that is "
                  "in the model, which is why this lesson needs no new machinery. What is new is "
                  "the use: a product nobody has ever made, a machine nobody has bought, a "
                  "contract nobody has signed &mdash; all of them can be valued before anything "
                  "is committed, from numbers a single solve already produced."),
            ("example", ("A product that pays for what it uses",
                         "The workshop's prices are `y = (0, 3/2, 1)`: cutting is worth nothing, "
                         "glazing `3/2` an hour, assembly 1 an hour. Propose a third product "
                         "taking one hour of each and earning 4.",
                         "It would consume `(0)(1) + (3/2)(1) + (1)(1) = 5/2` worth of what the "
                         "plan is already short of, and it earns 4, so its reduced cost is "
                         "`4 − 5/2 = 3/2` a unit. It enters, and a single pivot &mdash; not a "
                         "re-solve &mdash; takes the total from 36 to 39.")),
            ("h3", "A profitable product that makes the plan worse"),
            ("example", ("The same earnings, a heavier column",
                         "Propose instead a product taking one hour of cutting, two of glazing "
                         "and three of assembly, also earning 4. Now it consumes "
                         "`(0)(1) + (3/2)(2) + (1)(3) = 6`, and its reduced cost is `4 − 6 = −2`.",
                         "Making it would cost 2 a unit. Every unit of it would displace work "
                         "worth 6 to make 4, and the plan you already have is still optimal with "
                         "this column present in the model. Profit is not the test. Profit beyond "
                         "what the ingredients are already worth is the test, and the break-even "
                         "point for this column's lighter cousin is at earnings of exactly "
                         "`5/2`, where the reduced cost is zero and the lab reports that it does "
                         "not enter.")),
            ("p", "The reason this is the misconception worth naming is that the wrong answer is "
                  "the one a reader arrives at by a perfectly sound-sounding argument: the "
                  "product makes money, so make it. It does make money, and it makes less money "
                  "than what it would have to stop making. The prices are what convert that "
                  "sentence into arithmetic, and they are already on the screen."),
            ("h3", "A row that is not in the model"),
            ("p", "The second question has a shorter answer. A proposed constraint is a "
                  "statement about plans, so evaluate it at the plan you have. If it holds, "
                  "nothing at all follows: the plan is still feasible for the enlarged problem "
                  "and still optimal, since adding a constraint cannot create a better plan. If "
                  "it fails, the plan is no longer feasible, and the work of restoring "
                  "feasibility is the next lesson's."),
            ("example", ("One rule that bites and one that does not",
                         "The workshop's plan is `(2, 6)`. The proposed rule `x1 + x2 ≤ 5` reads "
                         "`8` there, so it is broken by 3, and something has to change; the lab "
                         "reports that restoring feasibility from the tableau in hand takes two "
                         "pivots and lands at 25.",
                         "The proposed rule `x1 + x2 ≤ 10` also reads `8`, which leaves 2 spare. "
                         "It is satisfied, so it changes nothing whatever: no pivot, no re-solve, "
                         "and the same plan and the same total. That is a real answer to a real "
                         "question, arrived at by one substitution.")),
            ("p", "And a rule can only ever cost. A constraint removes points from the feasible "
                  "region and never adds any, so the new optimum is at most the old one: 36 "
                  "becomes 25 in the first case and stays 36 in the second. If a proposed "
                  "constraint appears to raise the objective, the arithmetic is wrong. That is a "
                  "useful check, and it is the mirror image of the one for a new column, which "
                  "can only ever help."),
            ("math", [
                "PRICE A COLUMN                          TEST A ROW",
                "",
                "  y from the final tableau                x from the final tableau",
                "  reduced = c_new − y'a_new               reads = a'x,  slack = b − reads",
                "",
                "  reduced > 0   it enters                 slack ≥ 0   nothing follows",
                "  one pivot, and z* goes UP               same plan, same total",
                "",
                "  reduced ≤ 0   leave it out              slack < 0   the plan is broken",
                "  same plan, same total                   restore feasibility, z* goes DOWN",
                "",
                "workshop, y = (0, 3/2, 1), plan (2, 6), z* = 36",
                "",
                "  (1,1,1) at 4:   4 − 5/2 = 3/2  enters     x1+x2 ≤  5:  8, short by 3",
                "  (1,2,3) at 4:   4 − 6   = −2   no         x1+x2 ≤ 10:  8, 2 to spare",
                "  three activities, (1,1,1) at 6:",
                "                  6 − 5   = 1    enters, and 46 → 48",
            ]),
            ("p", "One warning about the row test. It says whether the plan you have is still "
                  "feasible, and that is all. A satisfied rule is genuinely free; a broken rule "
                  "tells you that work is needed but not how much, and the amount by which it is "
                  "broken is not the amount the objective will fall. On the workshop the rule is "
                  "short by 3 and the objective falls by 11."),
        ],
        "lab": ("duality", {
            "mode": "newcol",
            "preset": "worth-making",
            "panel_title": "Propose an activity, and propose a rule",
            "panel_intro": "Both questions are answered from the tableau already in hand, and "
                           "the panel keeps them in separate tables. Only a favourable price or a "
                           "broken rule costs anything further, and the second preset is the one "
                           "worth dwelling on: a profitable product whose reduced cost is "
                           "negative, beside a rule the plan already obeys.",
        }),
        "steps_title": "Deciding about something not in the model",
        "steps_intro": "Take the prices and the plan off the tableau first. Both questions are then one line each.",
        "steps": [
            ("Write the proposal as a column or as a row, and say which",
             "A new product, machine or contract that consumes resources is a column, with one "
               "entry per existing constraint. A new rule, limit or requirement is a row, with "
               "one entry per existing activity. They are answered by different tests and "
               "confusing them is the first thing to rule out."),
            ("For a column, value what it consumes at the prices you have",
             "`yᵀaₙₑw`, one product per row, added up. Then subtract that from what it earns. "
               "Positive for a maximisation means it enters; zero means it is exactly "
               "break-even and the plan you have is still optimal."),
            ("For a row, evaluate it at the plan you have",
             "Substitute and compare with the proposed right-hand side. Satisfied means nothing "
               "follows at all, and that is the answer rather than a step towards one. Broken "
               "means the plan has to change, and the shortfall is not the size of the change in "
               "the objective."),
            ("Do the work only if one of the two answers demands it",
             "A favourable column costs one pivot, performed from the tableau you already have. "
               "A broken row costs a dual simplex run from the same tableau. Neither costs a "
               "fresh solve, and most proposals cost nothing at all."),
        ],
        "worked": {
            "title": "Two products and two rules, priced against one tableau",
            "intro": [
                "Everything below comes from a single finished solve of the workshop. Nothing is "
                "re-solved until the last two lines, and those are one pivot and two pivots "
                "respectively."
            ],
            "lines": [
                "workshop    max 3x1 + 5x2      cutting  x1      ≤  4",
                "                               glazing     2x2  ≤ 12",
                "                               assembly 3x1+2x2 ≤ 18",
                "in hand     plan (2, 6)    z* = 36    y = (0, 3/2, 1)",
                "",
                "COLUMN A    one hour of each resource, earning 4",
                "  consumes  (0)(1) + (3/2)(1) + (1)(1)  =  5/2",
                "  earns     4",
                "  reduced   4 − 5/2  =  3/2   > 0    so it enters",
                "  one pivot z* goes from 36 to 39, and the new product is made",
                "",
                "COLUMN B    (1, 2, 3) hours, also earning 4",
                "  consumes  (0)(1) + (3/2)(2) + (1)(3)  =  0 + 3 + 3  =  6",
                "  earns     4",
                "  reduced   4 − 6  =  −2   ≤ 0    so leave it out",
                "  the plan (2, 6) is STILL OPTIMAL with this column in the model",
                "",
                "  break-even for column A's shape is earnings of 5/2 exactly:",
                "     reduced = 5/2 − 5/2 = 0, and it does not enter",
                "",
                "ROW P       x1 + x2 ≤ 5",
                "  reads     2 + 6  =  8",
                "  slack     5 − 8  =  −3        BROKEN by 3",
                "  restoring two dual pivots from the tableau in hand, 36 → 25 at (0, 5)",
                "",
                "ROW Q       x1 + x2 ≤ 10",
                "  reads     2 + 6  =  8",
                "  slack     10 − 8 =  2         satisfied, 2 to spare",
                "  nothing follows: no pivot, same plan, same total 36",
                "",
                "check       a column can only help:  36 → 39, never down",
                "            a row can only cost:     36 → 25, never up",
            ],
            "after": [
                "Column B is the one to keep. It earns money, it earns the same money as column "
                "A, and it is the wrong thing to make &mdash; because it displaces 6 worth of "
                "glazing and assembly to produce 4. Nothing about the model changed between A "
                "and B except the recipe.",
                "Notice too that the row test gives no estimate of the damage. Row P is short by "
                "3 and the objective falls by 11. Those two numbers are not related by anything "
                "simple, and the lesson's answer to how far it falls is the next lesson's "
                "method.",
                "For a faded rehearsal, use the three-activity programme, whose prices are "
                "`y = (3, 2, 0)` and whose plan is `(2, 6, 0)` at 46. The supplied move is that "
                "a proposed fourth activity taking one unit of each resource consumes "
                "`3 + 2 + 0 = 5`. Decide whether it is worth making if it earns 6, if it earns "
                "5, and if it earns 4; then propose the rule `x1 + x2 + x3 ≤ 7` and say whether "
                "it bites before you check.",
            ],
        },
        "quiz_title": "Price it, test it, or leave it alone",
        "quiz": [
            {"q": "With `y = (0, 3/2, 1)`, a proposed activity uses one unit of each resource and earns 4. What is its reduced cost?",
             "a": ["`4`", "`5/2`", "`3/2`", "`−2`"],
             "c": 2,
             "why": "It consumes `(0)(1) + (3/2)(1) + (1)(1) = 5/2` at the current prices and "
                    "earns 4, so `4 − 5/2 = 3/2`. `5/2` is what it consumes, `4` is what it "
                    "earns, and `−2` is the other proposed column's answer. Positive means it "
                    "enters, and one pivot takes the total from 36 to 39."},
            {"q": "A second proposed activity uses `(1, 2, 3)` and also earns 4. Is it worth making?",
             "a": ["Yes, because it is profitable",
                   "No: it consumes 6 worth of resources, so making it would cost 2 a unit",
                   "Yes, because it uses more of the resource that is priced at zero",
                   "Only if the plan currently has slack somewhere"],
             "c": 1,
             "why": "It consumes `(0)(1) + (3/2)(2) + (1)(3) = 6` and earns 4, so its reduced "
                    "cost is `−2` and the existing plan stays optimal with this column in the "
                    "model. Profitability is not the test: what it earns has to exceed what its "
                    "ingredients are already worth. The workshop does have slack &mdash; 2 units "
                    "of cutting &mdash; and it makes no difference."},
            {"q": "A proposed rule reads `x1 + x2 ≤ 10`, and the current plan is `(2, 6)`. What follows?",
             "a": ["Nothing at all: the plan already obeys it, with 2 to spare",
                   "The plan must be re-optimised from scratch",
                   "The objective falls by 2",
                   "The rule must be appended to the tableau before anything can be concluded"],
             "c": 0,
             "why": "`2 + 6 = 8 ≤ 10`, so the plan is still feasible and still optimal &mdash; "
                    "adding a constraint cannot produce a better plan than one you already have "
                    "inside the smaller region. That is the whole answer, for one substitution, "
                    "and appending the row would confirm it at the cost of two row operations "
                    "and zero pivots. On this programme the rule happens to be redundant "
                    "outright, since the largest total the region permits is 8 &mdash; but the "
                    "substitution test does not need to know that."},
            {"q": "When can adding a constraint raise `z*`?",
             "a": ["When the constraint is tight at the new optimum", "Never",
                   "When its price comes out negative",
                   "When the current plan already satisfies it"],
             "c": 1,
             "why": "A constraint only removes feasible points, so the new optimum is at most the "
                    "old one &mdash; the lab prints the new value as down from the old, and if "
                    "your arithmetic says otherwise the arithmetic is wrong. If the plan already "
                    "satisfies the rule the value is unchanged, which is not a rise. This is the "
                    "mirror of the fact that a new column can only ever help."},
        ],
        "mistakes": [
            ("Believing a product with positive profit is worth making",
             "This is the misconception the lesson is built on. A product earning 4 that consumes "
             "6 worth of glazing and assembly makes the plan worse by 2 a unit, and every unit of "
             "it displaces work that was earning more. The test is `cₙₑw − yᵀaₙₑw`, and the "
             "prices needed for it are already printed in the tableau you finished with."),
            ("Reading a broken row's shortfall as the damage to the objective",
             "The rule `x1 + x2 ≤ 5` is short by 3 at the workshop's plan, and the objective "
             "falls by 11. The shortfall is a statement about feasibility; the fall is the result "
             "of a re-optimisation, and finding it is the next lesson's method. Quoting one as "
             "the other produces a confident number that is wrong by a factor of nearly four."),
            ("Testing a proposed column as though it were a row, or the reverse",
             "A proposal that consumes resources is a column and gets priced against `y`; a "
             "proposal that limits activity is a row and gets evaluated at `x`. The two tests use "
             "different halves of the tableau and produce answers with different units, so "
             "swapping them gives a number that cannot be interpreted at all. Say which shape "
             "the proposal is before touching any arithmetic."),
        ],
        "standard": ("Finish when you can answer both questions about something not in the model with the tableau you already have.",
                     "You should be able to price a proposed activity against the current prices "
                     "and decide, evaluate a proposed rule at the current plan and decide, say "
                     "what each answer costs &mdash; nothing, one pivot, or a dual simplex run "
                     "&mdash; and state without checking which direction the objective can move "
                     "in each case."),
        "note": 'When a proposed rule is broken, the work that follows is “The Dual Simplex Method”: the current basis is still a basis of the enlarged problem, so only feasibility has to be restored, and doing it from the tableau in hand is what makes the whole family of these questions cheap. That method is also why Integer Programming can afford a search tree with hundreds of nodes.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-dual-simplex-method",
        "title": "The Dual Simplex Method",
        "module": "What the tableau knows",
        "one_line": "Restore feasibility while keeping optimality, one dual ratio test at a time, from the tableau you already have.",
        "summary": (
            "A tableau can be optimal in its objective row and infeasible in its right-hand "
            "column, which is exactly the state a new constraint or an out-of-range change "
            "leaves. The dual simplex method restores feasibility while preserving optimality: "
            "the leaving row is a negative right-hand side, and the entering column comes from a "
            "ratio test along that row against the objective row. It is the primal simplex run "
            "on the dual, seen in the primal tableau, and it is why re-optimisation and "
            "branch-and-bound are affordable at all."
        ),
        "key": [
            "start   objective row already optimal, right-hand column has a negative entry",
            "leave   the row with the most negative right-hand side",
            "enter   min over j of |zⱼ| ÷ |a_rj|, over the NEGATIVE entries of that row",
            "z falls monotonically for a maximisation — the opposite way from the primal",
            "workshop + (x1 + x2 ≤ 5):  new row  0  0  0  −1/6  −1/3  1  |  −3",
            "   row 4 at −3 → s3 enters (3 beats 9),  36 → 27",
            "   row 1 at −1 → s2 enters (2),          27 → 25  at (0, 5)",
        ],
        "key_label": "The two rules, and the workshop cut walked back",
        "concepts_intro": (
            "One hard idea: the old tableau describes the old basis, and that basis is still a "
            "basis of the new problem. Everything else is the two rules swapping places."
        ),
        "concepts": [
            ("Optimal and infeasible is a real state, and a useful one",
             "The objective row and the right-hand column can be checked independently. The "
             "primal simplex keeps the right-hand column non-negative and hunts for a "
             "non-negative objective row; the dual simplex keeps the objective row non-negative "
             "and hunts for a non-negative right-hand column. Both are walking from a basis to a "
             "neighbouring basis; they differ in which property they refuse to give up."),
            ("The two rules swap places",
             "In the primal method the entering column is chosen first, by the objective row, "
             "and a ratio test down that column picks the leaving row. Here the leaving row is "
             "chosen first, by the right-hand column, and a ratio test along that row picks the "
             "entering column. The ratio is `|zⱼ| ÷ |a_rj|` over the negative entries only, "
             "because only a negative entry can lift a negative right-hand side."),
            ("The value comes down to meet the answer",
             "For a maximisation the reported value on an infeasible tableau is an overstatement "
             "&mdash; it is what the basis would earn if the plan were legal &mdash; so each "
             "pivot lowers it, monotonically, until feasibility is restored and the number is "
             "real. On the workshop cut it goes 36, 27, 25. That direction is a check: if the "
             "value rises, the ratio test was misapplied."),
        ],
        "read_title": "Keeping optimality and hunting feasibility",
        "read_intro": "The starting state, the two rules, what each pivot does to the value, and the two ways the method can stop.",
        "body": [
            ("p", "A new constraint has just been added and the plan breaks it. The temptation is "
                  "to start again, on the reasoning that the old tableau described the old "
                  "problem. It described the old <em>basis</em>, and that basis is still a basis "
                  "of the new problem &mdash; just not a feasible one. Restoring feasibility is "
                  "cheaper than rebuilding, and this is the method that does it."),
            ("def", ("The dual simplex method",
                     "Given a tableau whose objective row is non-negative (optimal) but whose "
                     "right-hand column has a negative entry (infeasible), one "
                     "<strong>dual pivot</strong> is: choose as the leaving row `r` the one with "
                     "the most negative right-hand entry; choose as the entering column the `j` "
                     "minimising `|zⱼ| ÷ |a_rj|` over the columns with `a_rj &lt; 0`; and pivot "
                     "on `(r, j)`.",
                     "The <strong>dual simplex method</strong> repeats that until no right-hand "
                     "entry is negative, at which point the tableau is both feasible and optimal, "
                     "or until some leaving row has no negative entry at all, at which point the "
                     "problem is infeasible.")),
            ("p", "The ratio is worth reading rather than memorising. The entering column has to "
                  "have a negative entry in row `r`, because raising that variable must raise a "
                  "negative right-hand side towards zero. Among those candidates, "
                  "`|zⱼ| ÷ |a_rj|` is the amount of objective given up per unit of infeasibility "
                  "removed, so choosing the smallest is choosing the cheapest way to become "
                  "legal. That is why the objective-row entries appear in the numerator: this is "
                  "a cost-per-unit comparison, not an amount."),
            ("p", "And why it is the primal simplex on the dual. A negative right-hand entry in "
                  "the primal tableau is a violated dual constraint; the row with the most "
                  "negative entry is the dual's entering variable under the steepest rule; and "
                  "the ratio test along that row is the dual's own leaving-variable ratio test. "
                  "Everything happens in the primal tableau, so no second tableau has to be "
                  "built, which is the practical point."),
            ("math", [
                "workshop optimum, then the rule x1 + x2 ≤ 5 added as row 4",
                "",
                "  append the row and clear the basic variables out of it:",
                "     R4 → R4 − R1   removes x1        R4 → R4 − R3   removes x2",
                "",
                "         x1   x2   s1     s2      s3    s4  |   rhs",
                "     ------------------------------------------------",
                "          1    0    0   −1/3    1/3      0  |     2     x1",
                "          0    0    1    1/3   −1/3      0  |     2     s1",
                "          0    1    0    1/2      0      0  |     6     x2",
                "          0    0    0   −1/6   −1/3      1  |    −3     s4",
                "     ------------------------------------------------",
                "  z       0    0    0    3/2      1      0  |    36",
                "",
                "  optimal z-row, and −3 in the right-hand column: exactly the state",
                "",
                "PIVOT 1   leave row 4, whose rhs −3 is the most negative",
                "     ratios along row 4, over its negative entries only:",
                "        s2:  |3/2| ÷ |−1/6|  =  9",
                "        s3:  |1|   ÷ |−1/3|  =  3        smallest, so s3 enters",
                "     z:  36 → 27",
                "",
                "PIVOT 2   row 1 now has rhs −1, the most negative",
                "     ratios along row 1:",
                "        s2:  |1| ÷ |−1/2|  =  2          eligible, and smallest",
                "        s4:  entry is +1, not negative — raising s4 cannot help",
                "     z:  27 → 25",
                "",
                "STOP      every right-hand entry ≥ 0.  z* = 25 at (0, 5)",
                "          a fresh solve of the four-row problem gives 25 as well",
            ]),
            ("example", ("A rule the plan already obeys",
                         "Add `x1 + x2 ≤ 10` instead. After the same two row operations the new "
                         "row's right-hand entry is `+1` rather than `−3`, so there is no "
                         "negative entry anywhere and the method performs zero pivots. The "
                         "tableau was already feasible and already optimal.",
                         "That is the cheapest possible outcome and it is the common one. The "
                         "previous lesson's substitution test predicts it without doing even "
                         "this much work: the plan reads 8 against a limit of 10.")),
            ("example", ("A cut on the three-activity programme",
                         "The plan `(2, 6, 0)` earns 46 and uses 8 units in total. Add "
                         "`x1 + x2 + x3 ≤ 6`, which it breaks by 2. After the row operations the "
                         "new row reads `0, 0, −1, 0, −1, 0, 1 | −2`, and the ratio test over its "
                         "two negative entries gives `|4| ÷ |−1| = 4` for `x3` and "
                         "`|2| ÷ |−1| = 2` for `s2`.",
                         "So `s2` enters, one pivot is enough, and the answer is 42 at "
                         "`(4, 2, 0)`. One pivot to re-optimise a programme that a fresh solve "
                         "would have restarted from an initial basis.")),
            ("h3", "The two ways it stops"),
            ("p", "It stops successfully when no right-hand entry is negative: the tableau is "
                  "feasible, the objective row was never allowed to go negative, so the basis is "
                  "optimal and the number is real. It stops unsuccessfully when the chosen "
                  "leaving row has no negative entry at all. That row then asserts that a "
                  "non-negative combination of non-negative variables equals a negative number, "
                  "which nothing satisfies, and the new problem is infeasible. Adding "
                  "`x1 + x2 ≥ 9` to the workshop does exactly that: the region's largest total is "
                  "8, and the lab reports the rule as unsatisfiable rather than pivoting for "
                  "ever."),
            ("p", "One habit is worth building here and the lab's hint asks for it directly: "
                  "before moving the slider, try to say which plan the method will land on. You "
                  "will usually be wrong, and being wrong on purpose is how the ratio test along "
                  "the objective row stops being a rule to apply and starts being a reason. On "
                  "the workshop cut, most readers predict `(2, 3)` or `(4, 1)` &mdash; plans that "
                  "obey the new rule and look like small adjustments &mdash; and the answer is "
                  "`(0, 5)`, which abandons the first product altogether."),
            ("p", "This method is also the reason a search tree is affordable. Integer "
                  "Programming re-solves every branch-and-bound child exactly this way, starting "
                  "from its parent's final tableau with one bound added, which is one cut and a "
                  "handful of dual pivots rather than a fresh solve per node. A tree with "
                  "hundreds of nodes costs what a few dozen solves would, and this lesson is "
                  "where that becomes believable rather than asserted."),
        ],
        "lab": ("duality", {
            "mode": "dualsimplex",
            "preset": "workshop",
            "panel_title": "Add a rule that cuts the plan off, then walk back",
            "panel_intro": "The slider performs the pivots one at a time. At each one the leaving "
                           "row is the most negative right-hand side and the entering column is "
                           "whichever costs least to bring in, measured along that row against "
                           "the objective row &mdash; and the whole ratio test is tabulated, "
                           "including the entries that were not eligible and why.",
        }),
        "steps_title": "Running a dual simplex pivot",
        "steps_intro": "Append, clear, then alternate between the right-hand column and one row. Both rules are simpler than their primal counterparts.",
        "steps": [
            ("Append the new row and clear the basic variables out of it",
             "The new row arrives in terms of the original variables, and the basic variables have "
             "to be eliminated from it before it is a tableau row. One row operation per basic "
             "variable that appears in it; the lab prints each one with the variable it removed."),
            ("Choose the leaving row from the right-hand column",
             "The most negative entry. Note that this is a choice about infeasibility and involves "
               "the objective not at all &mdash; which is the mirror of the primal method, where "
               "the entering column is chosen from the objective row and involves feasibility not "
               "at all."),
            ("Take the ratio test along that row, over its negative entries only",
             "`|zⱼ| ÷ |a_rj|` for each nonbasic column with a negative entry in the row. A "
             "positive or zero entry is ineligible, because raising that variable cannot lift a "
             "negative right-hand side. The smallest ratio enters; a tie is a choice, as it is in "
             "the primal method."),
            ("Pivot, and check that the value moved the right way",
             "For a maximisation it must fall. If it rises, the ratio test was taken over the "
             "wrong entries or the wrong row was chosen. Repeat until no right-hand entry is "
             "negative &mdash; or until a leaving row has no negative entry, which means the new "
             "problem is infeasible."),
        ],
        "worked": {
            "title": "The workshop, cut at five units in total, walked back in two pivots",
            "intro": [
                "The starting tableau is the workshop's own final tableau with one row appended. "
                "Nothing is rebuilt, and the ratio test is written out in full at both pivots, "
                "including the entries that were not eligible."
            ],
            "lines": [
                "in hand     plan (2, 6)   z* = 36   basis  x1, s1, x2",
                "new rule    x1 + x2 ≤ 5,  which the plan reads as 8: short by 3",
                "",
                "append      row 4 is  x1 + x2 + s4 = 5",
                "clear       R4 → R4 − R1    (removes the basic x1)",
                "            R4 → R4 − R3    (removes the basic x2)",
                "",
                "            x1   x2   s1     s2      s3   s4  |   rhs",
                "             1    0    0   −1/3    1/3    0  |     2",
                "             0    0    1    1/3   −1/3    0  |     2",
                "             0    1    0    1/2      0    0  |     6",
                "             0    0    0   −1/6   −1/3    1  |    −3",
                "  z          0    0    0    3/2      1    0  |    36",
                "",
                "  the z-row is non-negative: still optimal",
                "  the rhs has a −3: no longer feasible",
                "",
                "PIVOT 1",
                "  leave     row 4, rhs = −3, the most negative",
                "  ratios    s2:  entry −1/6   |3/2| ÷ |−1/6| = 9",
                "            s3:  entry −1/3   |1|   ÷ |−1/3| = 3    ← smallest",
                "  enter     s3,  and s4 leaves the basis",
                "  value     36 → 27",
                "",
                "PIVOT 2",
                "  leave     row 1, rhs = −1, the most negative",
                "  ratios    s2:  entry −1/2   |1| ÷ |−1/2| = 2      ← smallest",
                "            s4:  entry +1     ineligible: a positive entry cannot",
                "                              lift a negative right-hand side",
                "  enter     s2,  and x1 leaves the basis",
                "  value     27 → 25",
                "",
                "STOP        every right-hand entry is ≥ 0",
                "            z* = 25 at x = (0, 5)",
                "",
                "check       solve the four-row problem from scratch:  25.   Same.",
                "            and 25 ≤ 36, because a rule can only ever cost",
            ],
            "after": [
                "The two pivots cost what two pivots cost, and the fresh solve they replace would "
                "have started from an initial basis and worked up. On a two-variable programme "
                "that difference is a curiosity. On a branch-and-bound tree with one added bound "
                "per node it is the difference between a tractable search and an impossible one.",
                "The ineligible entry at pivot 2 is worth pausing on. `s4` has a `+1` in row 1, "
                "and raising `s4` would make that row's right-hand side more negative rather than "
                "less. The ratio test's restriction to negative entries is that observation, and "
                "it is the half of the rule most often dropped.",
                "For a faded rehearsal, cut the three-activity programme with "
                "`x1 + x2 + x3 ≤ 6`. The supplied move is that the plan reads 8 there, so the new "
                "row's right-hand entry after clearing is `−2`. Find the ratio test's two "
                "candidates, say which enters, predict the plan it lands on, and only then check "
                "&mdash; the prediction is the exercise.",
            ],
        },
        "quiz_title": "The two rules, and the direction of travel",
        "quiz": [
            {"q": "Which row leaves in a dual simplex pivot?",
             "a": ["The row with the largest positive right-hand side",
                   "The row with the most negative right-hand side",
                   "The row whose ratio along the entering column is smallest",
                   "Any row that contains a negative entry"],
             "c": 1,
             "why": "The leaving row is chosen from the right-hand column, by infeasibility, and "
                    "the objective plays no part in it &mdash; which is the mirror of the primal "
                    "method, where the entering column is chosen from the objective row and "
                    "feasibility plays no part. The third choice is the primal method's rule, and "
                    "it is the step that comes second here."},
            {"q": "Along the leaving row, over which entries is the ratio test taken?",
             "a": ["All of them", "The positive entries", "The negative entries",
                   "The entries in columns currently in the basis"],
             "c": 2,
             "why": "Only a negative entry can lift a negative right-hand side towards zero: "
                    "raising a variable with a positive entry in that row makes the infeasibility "
                    "worse. The lab tabulates the ineligible entries with that sentence beside "
                    "each, which is the half of the rule readers most often drop."},
            {"q": "After the cut `x1 + x2 ≤ 5`, the reported value goes 36, then 27, then 25. What is that direction telling you?",
             "a": ["The method is diverging and needs a different starting basis",
                   "The objective row stays optimal throughout, so the overstated value comes down to meet the real one",
                   "The ratio test was applied to the wrong entries",
                   "The programme is being minimised rather than maximised"],
             "c": 1,
             "why": "On an infeasible tableau the reported value is what the basis would earn if "
                    "the plan were legal, which for a maximisation is an overstatement. Each "
                    "pivot buys feasibility and lowers it, monotonically, until it is real at 25 "
                    "&mdash; the opposite direction from the primal method, which climbs. A rise "
                    "here would be the symptom of a misapplied ratio test, not the normal case."},
            {"q": "The chosen leaving row has no negative entry anywhere. What does that mean?",
             "a": ["The tableau is already optimal and the method should stop successfully",
                   "The new problem is infeasible",
                   "A different leaving row should be chosen and the method continued",
                   "The objective is unbounded"],
             "c": 1,
             "why": "That row says a non-negative combination of non-negative variables equals a "
                    "negative number, which nothing satisfies, so the enlarged problem has no "
                    "feasible point at all. Adding `x1 + x2 ≥ 9` to the workshop produces exactly "
                    "this, because the largest total the region permits is 8. Unboundedness is "
                    "the primal method's failure mode, not this one's."},
        ],
        "mistakes": [
            ("Starting again because the problem has changed",
             "The old tableau described the old basis, and that basis is still a basis of the new "
             "problem &mdash; the columns did not move and the objective row is still "
             "non-negative. Only feasibility broke, and restoring it is two pivots on the "
             "workshop rather than a fresh solve. This is the misconception that makes "
             "branch-and-bound look unaffordable, and it is wrong at every node."),
            ("Taking the ratio test over every entry of the leaving row",
             "Only the negative entries are eligible, because only they move a negative "
             "right-hand side upwards. Including a positive entry produces a ratio that looks "
             "like the others and a pivot that makes the tableau worse, and the symptom is a "
             "reported value that rises instead of falling."),
            ("Expecting the new plan to be near the old one",
             "The workshop's plan `(2, 6)` becomes `(0, 5)` under the rule `x1 + x2 ≤ 5`: the "
             "first product is dropped entirely, and plans like `(2, 3)` that look like small "
             "adjustments are not optimal. Predicting the landing point before pivoting is worth "
             "doing precisely because the prediction is usually wrong, and the ratio test is the "
             "reason it is wrong."),
        ],
        "standard": ("Finish when you can re-optimise a cut programme from the tableau in hand without reaching for a fresh solve.",
                     "You should be able to append a row and clear the basic variables out of it, "
                     "choose the leaving row from the right-hand column, take the ratio test "
                     "along that row over the negative entries only, state why the value falls at "
                     "every pivot, and recognise the row with no negative entry as a proof of "
                     "infeasibility."),
        "note": 'Integer Programming re-solves every branch-and-bound child exactly this way, starting from its parent\'s final tableau with one bound appended. That is why a tree with hundreds of nodes is affordable, and this is the lesson where that stops being an assertion: two pivots to re-optimise a cut programme, against a fresh solve from an initial basis, at every node of the tree.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "parametric-objectives-and-the-pareto-front",
        "title": "Parametric Objectives and the Pareto Front",
        "module": "Duality as the subject",
        "one_line": "Compute the exact weights at which the answer changes, and list the corners no feasible point beats in both objectives at once.",
        "summary": (
            "Maximise a weighted sum of two objectives and sweep the weight from one end to the "
            "other. The optimal basis changes at only finitely many weights &mdash; objective "
            "coefficient ranging, chained &mdash; and the corners visited along the way are "
            "exactly the efficient points of the two-objective problem. The weights are the "
            "decision and they are made outside the model; what the mathematics delivers is the "
            "set of corners nothing beats in both objectives together."
        ),
        "key": [
            "max (1 − λ)f₁ + λf₂ ,   λ from 0 to 1        λ = 0 is f₁ alone, λ = 1 is f₂",
            "for a fixed basis the reduced costs are affine in λ, so each basis owns an",
            "interval of λ; the breakpoint is where one of them reaches zero",
            "four corners   (7, 0)     (6, 3)     (4, 6)     (0, 10)",
            "scoring        (28, 7)   (27, 18)   (22, 28)   (10, 40)",
            "breaking at    λ = 1/12,  1/3,  1/2        exact fractions, not sampled",
            "efficient: no feasible point beats it on BOTH objectives at once",
        ],
        "key_label": "One weight, four corners, three exact breakpoints",
        "concepts_intro": (
            "Nothing new is computed here. What is new is that a two-objective problem has a set "
            "of answers rather than an answer, and that the set is finite and computable."
        ),
        "concepts": [
            ("A weighted sum is one objective, and ranging it is the previous lesson",
             "`(1 − λ)f₁ + λf₂` is a single linear objective whose coefficients are affine in "
             "`λ`. For a fixed basis, every reduced cost is therefore affine in `λ` too, so the "
             "set of weights keeping that basis optimal is an intersection of intervals &mdash; "
             "one line of arithmetic, not a search. The breakpoint is where some reduced cost "
             "reaches exactly zero, which is an objective coefficient range endpoint under a "
             "different name."),
            ("Finitely many breakpoints, found exactly rather than by sampling",
             "There are only so many bases, so the sweep from `λ = 0` to `λ = 1` visits finitely "
             "many corners and changes at finitely many weights. Those weights are exact "
             "fractions. Sampling `λ` on a grid would find the same corners on a good day and "
             "could never establish that there are no others between two samples."),
            ("Efficient means nothing beats it on both at once",
             "A corner is <em>efficient</em>, or Pareto optimal, when no feasible point scores at "
             "least as much on both objectives and strictly more on one. That is a weaker demand "
             "than being best, and it is the right one: a two-objective problem has no single "
             "best point unless the objectives happen to agree, and what the mathematics can "
             "deliver is the set that survives this test."),
        ],
        "read_title": "Sweeping one weight, and the set of answers it traces",
        "read_intro": "Why the breakpoints are finite and exact, what the corners in between are, and which part of the problem the mathematics does not decide.",
        "body": [
            ("def", ("Efficient, and the front",
                     "For a feasible region and two objectives `f₁`, `f₂` to be maximised, a "
                     "feasible point `p` is <strong>efficient</strong> when no feasible point `q` "
                     "has `f₁(q) ≥ f₁(p)` and `f₂(q) ≥ f₂(p)` with at least one inequality "
                     "strict. The set of efficient points is the <strong>Pareto front</strong>.",
                     "The corners found by maximising `(1 − λ)f₁ + λf₂` over `λ` in `[0, 1]` are "
                     "the <strong>supported</strong> efficient corners &mdash; those a weighted "
                     "sum can reach.")),
            ("p", "The lab's slider is the weight on the second objective, so `λ = 0` maximises "
                  "`f₁` alone and `λ = 1` maximises `f₂` alone. Everything between is a trade, "
                  "and the useful fact is that the trade is not continuous in the answer: the "
                  "corner chosen is constant over an interval of weights and then jumps."),
            ("thm", ("Finitely many breakpoints, and what happens at one",
                     "Fix a basis. Under the objective `(1 − λ)f₁ + λf₂`, every reduced cost is "
                     "of the form `a + λ(b − a)`, where `a` and `b` are that column's reduced "
                     "costs under `f₁` and `f₂` alone. The basis is optimal exactly while all of "
                     "them are non-negative, which is an intersection of at most one interval per "
                     "nonbasic column.",
                     "At the upper end of that interval some reduced cost is exactly zero, and "
                     "one pivot on that column reaches the next basis, whose interval begins "
                     "there. Since there are finitely many bases, the sweep terminates, and the "
                     "breakpoints are the finitely many weights at which two corners score the "
                     "same weighted total.")),
            ("math", [
                "region      x1 ≤ 8,  x1 + x2 ≤ 10,  2x1 + x2 ≤ 16,",
                "            3x1 + 2x2 ≤ 24,  3x1 + x2 ≤ 21,   x ≥ 0",
                "objectives  f1 = 4x1 + x2         f2 = x1 + 4x2",
                "",
                "weighted    (1 − λ)f1 + λf2  has coefficients",
                "            x1:  4 − 3λ           x2:  1 + 3λ",
                "",
                "     λ in         corner      f1    f2     weighted total",
                "   0 .. 1/12      (7, 0)      28     7     28 − 21λ",
                "   1/12 .. 1/3    (6, 3)      27    18     27 −  9λ",
                "   1/3 .. 1/2     (4, 6)      22    28     22 +  6λ",
                "   1/2 .. 1       (0, 10)     10    40     10 + 30λ",
                "",
                "breakpoints  28 − 21λ = 27 −  9λ   ⟹   1 = 12λ   ⟹  λ = 1/12",
                "             27 −  9λ = 22 +  6λ   ⟹   5 = 15λ   ⟹  λ = 1/3",
                "             22 +  6λ = 10 + 30λ   ⟹  12 = 24λ   ⟹  λ = 1/2",
                "",
                "all four corners are efficient: no other beats any of them on both",
            ]),
            ("example", ("Reading the front off the table",
                         "At `λ = 0` the answer is `(7, 0)`, which is the most `f₁` the region "
                         "allows. Nudge the weight towards the second objective and nothing "
                         "happens until `λ = 1/12`, where `(7, 0)` and `(6, 3)` score the same "
                         "`105/4` and the answer changes. It then holds until `1/3`, and so on.",
                         "So `λ = 0.08` chooses `(7, 0)` and `λ = 0.09` chooses `(6, 3)`, and no "
                         "slider position in hundredths ever lands on `1/12` itself &mdash; the "
                         "breakpoint falls strictly between two hundredths. That is the "
                         "difference between computing the breakpoints and looking for them.")),
            ("h3", "The weights are the decision"),
            ("p", "This is the misconception the lesson exists for. A two-objective problem does "
                  "not have an optimum, and the weights are not a technical detail on the way to "
                  "one: they <em>are</em> the decision, and they are made outside the model by "
                  "whoever is entitled to make it. What the mathematics delivers is smaller and "
                  "more honest &mdash; the set of corners that no feasible point beats on both "
                  "objectives at once, with the exact weight at which each one takes over."),
            ("p", "Which is genuinely useful, because it rules things out. A point that is not "
                  "efficient is one nobody should choose under any weights at all, since "
                  "something else is at least as good on both counts. Presenting four corners and "
                  "their scores is a complete answer to what the model can say, and it leaves the "
                  "part it cannot say visible rather than buried in a weight somebody picked."),
            ("example", ("A smaller region, and three corners",
                         "`x1 ≤ 8`, `x2 ≤ 6`, `x1 + x2 ≤ 10`, `2x1 + x2 ≤ 16`, with "
                         "`f₁ = 3x1 + x2` and `f₂ = x1 + 3x2`. The front is `(8, 0)` scoring "
                         "`(24, 8)` for `λ` up to `1/6`, then `(6, 4)` scoring `(22, 18)` up to "
                         "`1/2`, then `(4, 6)` scoring `(18, 22)`.",
                         "Note that `(0, 6)`, which scores `(6, 18)`, is a corner of the region "
                         "and is not on the front: `(4, 6)` beats it on both objectives at once. "
                         "A corner being reachable is not the same as a corner being worth "
                         "considering, and the front is the smaller list.")),
            ("h3", "The same front, read through the other ranging"),
            ("p", "There is a second route to the same set. Instead of weighting the two "
                  "objectives, maximise `f₁` subject to a constraint `f₂ ≥ t` and sweep `t` "
                  "&mdash; the ε-constraint method. That is right-hand-side ranging rather than "
                  "objective ranging, and its breakpoints are the values of `t` at which the "
                  "basis changes, exactly as in the shadow-price lesson. The two sweeps trace the "
                  "same front, and the ε-constraint route additionally reaches efficient points "
                  "that no weighted sum does, which is a distinction that costs nothing here "
                  "&mdash; a linear programme has none &mdash; and matters elsewhere."),
            ("p", "One structural fact, and the place it stops being true. Every efficient point "
                  "of a linear programme is a convex combination of efficient corners, so the "
                  "four corners above describe the whole front and not merely samples of it. That "
                  "is false for integer problems: an integer programme's efficient set has points "
                  "that lie between corners and are not combinations of them, because the "
                  "combinations are not feasible. Integer Programming is where that is felt, and "
                  "it is worth knowing in advance that this lesson's tidiness is a property of "
                  "linearity rather than of two-objective problems."),
        ],
        "lab": ("duality", {
            "mode": "parametric",
            "preset": "four-corners",
            "panel_title": "Weigh two objectives against each other",
            "panel_intro": "The corners and the weights at which they change are computed exactly, "
                           "from the same ranging that decided how far one coefficient could "
                           "move. Chaining that is all a parametric sweep is &mdash; and the "
                           "slider moves in hundredths while the breakpoints do not, so the first "
                           "one, at one twelfth, is a weight no slider position can land on.",
        }),
        "steps_title": "Tracing a front",
        "steps_intro": "Solve at one end, range the weight, pivot at the breakpoint, repeat. The Pareto test comes last and is a comparison, not a solve.",
        "steps": [
            ("Solve at one end of the weight range",
             "At `λ = 0` the objective is `f₁` alone. That gives the first corner and the basis "
             "the sweep starts from. Solving at the other end as well is a useful check on where "
             "the sweep must finish."),
            ("Range the weight for the current basis",
             "For each nonbasic column, its reduced cost is affine in `λ`; require all of them to "
             "be non-negative and intersect the intervals. The upper end of the result is the "
             "next breakpoint, and the column whose reduced cost reached zero there is the one "
             "that enters."),
            ("Pivot at the breakpoint and record the corner",
             "One pivot on that column reaches the next basis, whose interval starts where the "
             "last one ended. Record the corner and its two scores `(f₁, f₂)`, not just the "
             "weighted total, because the weighted total is the thing that depends on a choice."),
            ("Mark the efficient corners, and say what is left to the reader",
             "Compare every recorded corner against every other: drop any that another beats on "
             "both objectives. Then present the survivors with their scores and their weight "
             "intervals, and state plainly that choosing among them is not a mathematical "
             "question."),
        ],
        "worked": {
            "title": "Four corners and three breakpoints, computed rather than sampled",
            "intro": [
                "The weight below is the weight on the second objective, so the sweep starts at "
                "the corner that maximises the first one. Each breakpoint is found by setting two "
                "weighted totals equal, which is why they come out as exact fractions."
            ],
            "lines": [
                "region      kiln      x1        ≤  8",
                "            clay      x1 +  x2  ≤ 10",
                "            glaze    2x1 +  x2  ≤ 16",
                "            firing   3x1 + 2x2  ≤ 24",
                "            packing  3x1 +  x2  ≤ 21",
                "",
                "objectives  f1 = 4x1 + x2        f2 = x1 + 4x2",
                "weighted    (1 − λ)f1 + λf2",
                "            x1 coefficient  4(1 − λ) + 1λ  =  4 − 3λ",
                "            x2 coefficient  1(1 − λ) + 4λ  =  1 + 3λ",
                "",
                "λ = 0       maximise 4x1 + x2   →   (7, 0), packing tight at 21",
                "            f1 = 28   f2 = 7",
                "",
                "corner totals, as functions of λ",
                "   (7, 0)    7(4 − 3λ)                     = 28 − 21λ",
                "   (6, 3)    6(4 − 3λ) + 3(1 + 3λ)         = 27 −  9λ",
                "   (4, 6)    4(4 − 3λ) + 6(1 + 3λ)         = 22 +  6λ",
                "   (0, 10)  10(1 + 3λ)                     = 10 + 30λ",
                "",
                "breakpoint 1   28 − 21λ = 27 − 9λ",
                "               1 = 12λ            λ = 1/12",
                "               both score 28 − 21/12 = 105/4",
                "",
                "breakpoint 2   27 − 9λ = 22 + 6λ       5 = 15λ      λ = 1/3",
                "breakpoint 3   22 + 6λ = 10 + 30λ     12 = 24λ      λ = 1/2",
                "",
                "the front       λ in        corner     (f1, f2)",
                "              0 .. 1/12     (7, 0)     (28,  7)",
                "              1/12 .. 1/3   (6, 3)     (27, 18)",
                "              1/3 .. 1/2    (4, 6)     (22, 28)",
                "              1/2 .. 1      (0, 10)    (10, 40)",
                "",
                "Pareto test   no corner beats another on both:",
                "              f1 falls 28, 27, 22, 10 while f2 rises 7, 18, 28, 40",
                "              so all four are efficient",
                "",
                "sliders       λ = 0.08 → (7, 0)      λ = 0.09 → (6, 3)",
                "              1/12 = 0.0833..., which no hundredth lands on",
            ],
            "after": [
                "The Pareto test at the end is three comparisons and no arithmetic: the corners "
                "come out of the sweep sorted by `f₁` descending, and if `f₂` is ascending at the "
                "same time then none can dominate another. When `f₂` is not monotone the sweep has "
                "produced a corner that something else beats on both counts, and it is dropped "
                "&mdash; as `(0, 6)` is on the smaller region.",
                "The last two lines are the reason the breakpoints are computed. The slider moves "
                "in hundredths, `1/12` is `0.0833…`, and no position on the slider is ever exactly "
                "at the breakpoint. A reader sweeping by hand would see the answer change between "
                "two positions and would have no way to say where.",
                "For a faded rehearsal, run the smaller region: `x1 ≤ 8`, `x2 ≤ 6`, "
                "`x1 + x2 ≤ 10`, `2x1 + x2 ≤ 16`, with `f₁ = 3x1 + x2` and `f₂ = x1 + 3x2`. The "
                "supplied move is that `λ = 0` gives `(8, 0)`. Find the two breakpoints by setting "
                "corner totals equal, list the front, and then explain why the region's corner "
                "`(0, 6)` does not appear on it.",
            ],
        },
        "quiz_title": "Weights, breakpoints and the front",
        "quiz": [
            {"q": "What does a breakpoint in the weight mark?",
             "a": ["A change of optimal basis, and so of the corner the weighted sum chooses",
                   "A change in the feasible region",
                   "A weight at which the two objectives happen to score equally",
                   "A weight at which the front stops being convex"],
             "c": 0,
             "why": "At a breakpoint some reduced cost is exactly zero, two corners score the same "
                    "weighted total, and one pivot moves between them &mdash; it is an objective "
                    "coefficient range endpoint, reached by moving `λ` instead of a single `cⱼ`. "
                    "The region never changes during a sweep, and the objectives scoring equally "
                    "is a different condition entirely."},
            {"q": "The front breaks at `λ = 1/12`, `1/3` and `1/2`. Which corner does `λ = 0.4` choose?",
             "a": ["`(7, 0)`", "`(6, 3)`", "`(4, 6)`", "`(0, 10)`"],
             "c": 2,
             "why": "`0.4` lies between `1/3 ≈ 0.333` and `1/2`, which is the interval belonging "
                    "to `(4, 6)`. The intervals are what the sweep produces, and reading the "
                    "answer off them is the whole use of the table &mdash; there is nothing to "
                    "re-solve for a weight you have already bracketed."},
            {"q": "Is `(6, 3)`, which scores `(27, 18)`, efficient?",
             "a": ["No, because `(7, 0)` beats it on the first objective",
                   "No, because `(0, 10)` beats it on the second",
                   "Yes: no feasible point beats it on both objectives at once",
                   "It cannot be decided without knowing which weight was chosen"],
             "c": 2,
             "why": "Efficiency asks about both objectives together. `(7, 0)` scores more on `f₁` "
                    "and much less on `f₂`; `(0, 10)` the reverse. Neither dominates, and nothing "
                    "else does either, so `(6, 3)` is efficient. And the test mentions no weight "
                    "at all: efficiency is a comparison between points, which is exactly what "
                    "makes the front reportable before anybody has chosen a weight."},
            {"q": "Which part of a two-objective problem is not settled by the mathematics?",
             "a": ["The breakpoints", "The efficient corners", "The weights",
                   "The score of each objective at each corner"],
             "c": 2,
             "why": "The breakpoints, the corners and the scores are all computed exactly. The "
                    "weights are the decision, they are made outside the model by whoever is "
                    "entitled to make it, and presenting a single answer obtained from a weight "
                    "somebody picked hides that. What the model can offer is the set of corners "
                    "nothing beats on both counts."},
        ],
        "mistakes": [
            ("Treating a two-objective problem as having an optimum",
             "It has a front. Choosing a point on that front is a decision about how much of one "
             "objective a unit of the other is worth, and no amount of solving produces it. The "
             "error is usually invisible, because picking a weight and reporting one answer looks "
             "like a solution &mdash; and the reader is never told that a different weight would "
             "have given a different answer, or how different."),
            ("Sweeping the weight on a grid and reporting what turns up",
             "A grid of hundredths never lands on `1/12`, so the change of answer appears "
             "somewhere between two positions and its location is unknown. Worse, a corner whose "
             "interval is shorter than the grid spacing can be missed entirely, and nothing in "
             "the output says so. The breakpoints are an intersection of intervals and cost one "
             "line of arithmetic per nonbasic column."),
            ("Confusing being reachable with being worth considering",
             "Every corner of the region is optimal for some objective, but not every corner is "
             "efficient for a given pair of objectives: on the smaller region `(0, 6)` scores "
             "`(6, 18)` and `(4, 6)` scores `(18, 22)`, which is better on both. The Pareto test "
             "is a comparison at the end of the sweep, and dropping it presents the reader with "
             "options that nobody should choose."),
        ],
        "standard": ("Finish when you can hand someone a front rather than an answer, with exact weights attached.",
                     "You should be able to write the weighted objective, range the weight for a "
                     "basis, find each breakpoint by setting two corner totals equal, list the "
                     "corners with both their scores and their weight intervals, drop the ones "
                     "another dominates, and say which part of the problem the mathematics did "
                     "not decide."),
        "note": 'The ε-constraint method reads the same front through right-hand-side ranging instead of objective ranging: maximise one objective subject to a floor on the other, and sweep the floor. Also worth carrying forward: every efficient point of a linear programme is a convex combination of efficient corners, so the corner list describes the whole front &mdash; which is false for integer problems, and Integer Programming is where that is felt.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "zero-sum-games-and-the-minimax-theorem",
        "title": "Zero-Sum Games and the Minimax Theorem",
        "module": "Duality as the subject",
        "one_line": "Write both players' linear programmes, solve them, and verify the value and both mixtures by complementary slackness.",
        "summary": (
            "The row player's problem &mdash; choose a mixture maximising the worst case &mdash; "
            "is a linear programme, the column player's is precisely its dual, and so strong "
            "duality is the minimax theorem: the best guaranteed payoff equals the least "
            "enforceable loss, and the common optimum is the value of the game. A pure strategy "
            "is exploitable and a mixture is not, and the gap between the best pure guarantee "
            "and the value is exactly what mixing buys."
        ),
        "key": [
            "row player      max v    s.t.  Σᵢ pᵢAᵢⱼ ≥ v for every column j,  Σ p = 1, p ≥ 0",
            "column player   min w    s.t.  Σⱼ Aᵢⱼqⱼ ≤ w for every row i,     Σ q = 1, q ≥ 0",
            "the second is the DUAL of the first, so strong duality gives max min = min max = v",
            "v is a FREE variable in both: a game can be worth a negative amount",
            "the 3 × 3 cycle:  v = 0,  p = q = (1/3, 1/3, 1/3)",
            "(3 −1 / −2 1):    v = 1/7,  p = (3/7, 4/7),  q = (2/7, 5/7)",
            "best pure guarantee −1, least pure enforcement 1, and v = 1/7 between them",
        ],
        "key_label": "Two programmes that are each other's dual, and one number they share",
        "concepts_intro": (
            "One hard idea: the two players are solving the same linear programme from opposite "
            "sides. Everything the minimax theorem says is what strong duality already said."
        ),
        "concepts": [
            ("Maximising a worst case is a linear programme",
             "The worst case over the opponent's choices is a minimum of linear functions, which "
             "is not linear &mdash; so introduce a variable `v` for it and require `v` to be at "
             "most the expected payoff against every single column. Maximising `v` then maximises "
             "the worst case, and every constraint is linear. That substitution is the entire "
             "modelling step."),
            ("The column player's programme is the dual, not a second model",
             "Take the dual of the row player's programme and out comes: minimise `w` subject to "
             "the expected payoff against every row being at most `w`, with the mixture weights "
             "summing to one. That is the column player's problem, with the dual variables of the "
             "column constraints turning out to be the column player's mixture. No second solver "
             "is involved."),
            ("The value is a guarantee, and mixing is what buys it",
             "`v` is what the row player can promise against any opponent at all, including one "
             "who sees the mixture. Against the optimal mixture no pure row does better than `v` "
             "and some do worse; what a pure row cannot do is <em>promise</em> `v`, because its "
             "own worst case is lower. On the two-by-two game the best pure promise is `−1` and "
             "the value is `1/7`."),
        ],
        "read_title": "A game as a pair of dual programmes",
        "read_intro": "The substitution that makes a worst case linear, the dual that is the other player, and what a mixture buys that no single choice can.",
        "body": [
            ("def", ("Zero-sum game, mixed strategy, value",
                     "A <strong>zero-sum game</strong> is a payoff matrix `A`: the row player "
                     "chooses a row, the column player a column, and the row player receives "
                     "`Aᵢⱼ` while the column player pays it. A <strong>mixed strategy</strong> "
                     "is a probability distribution over one's own choices.",
                     "The <strong>value</strong> of the game is the largest expected payoff the "
                     "row player can guarantee with a mixture, whatever the column player does "
                     "&mdash; and, as the theorem below says, also the smallest expected payoff "
                     "the column player can be held to.")),
            ("p", "Maximising a worst case looks nonlinear, and the fix is one variable. Let `v` "
                  "stand for the guaranteed payoff. Requiring `v` to be no more than the expected "
                  "payoff against each individual column is the same as requiring it to be no "
                  "more than the minimum, and every one of those requirements is linear in the "
                  "mixture. Then maximise `v`."),
            ("math", [
                "payoffs      A = (  3  −1 )       rows are the row player's choices",
                "                 ( −2   1 )",
                "",
                "ROW PLAYER   max v",
                "             against column 1:   3p1 − 2p2 ≥ v",
                "             against column 2:  −p1  +  p2 ≥ v",
                "             mixture:             p1  +  p2 = 1",
                "             p1, p2 ≥ 0     and v FREE",
                "",
                "as the lab writes it, with v moved to the left:",
                "             −3p1 + 2p2 + v ≤ 0",
                "               p1 −  p2 + v ≤ 0",
                "               p1 +  p2     = 1",
                "",
                "ITS DUAL     min y3",
                "             −3y1 +  y2 + y3 ≥ 0",
                "              2y1 −  y2 + y3 ≥ 0",
                "               y1 +  y2      = 1",
                "             y1, y2 ≥ 0      and y3 FREE",
                "",
                "which is the COLUMN player's problem: y1, y2 is the column mixture q",
                "and y3 is the value it can hold the row player to",
                "",
                "solved       v = 1/7      p = (3/7, 4/7)      q = (2/7, 5/7)",
            ]),
            ("thm", ("The minimax theorem is strong duality",
                     "For every payoff matrix, the row player's programme and the column player's "
                     "programme are duals of each other, both are feasible and bounded, and so "
                     "their optima are equal. That common number `v` satisfies",
                     "`v = max over mixtures p of min over columns j of the expected payoff = "
                     "min over mixtures q of max over rows i of the expected payoff`,",
                     "and it is the value of the game. Optimal mixtures exist for both players, "
                     "and there is nothing left to prove: the theorem is strong duality with "
                     "different nouns.")),
            ("p", "Two details of the programmes are worth naming, because they are where a "
                  "careless formulation goes wrong. `v` must be declared free: a game can be "
                  "worth a negative amount, and restricting `v` to be non-negative silently "
                  "changes the problem. And the mixture constraint is an equality, which is what "
                  "makes its dual variable free in turn &mdash; the value on the other side."),
            ("example", ("A game that goes round in a circle",
                         "The three-by-three matrix with rows `(0, −1, 1)`, `(1, 0, −1)` and "
                         "`(−1, 1, 0)` is the familiar cycle: each choice beats one other and "
                         "loses to one other. Its value is `0` and both optimal mixtures are "
                         "`(1/3, 1/3, 1/3)`.",
                         "Against `q = (1/3, 1/3, 1/3)` every pure row earns exactly `0`, so no "
                         "single choice is punished by playing it once. What a single choice "
                         "cannot do is promise anything: each row's own worst case is `−1`, "
                         "against an opponent who knows which row it is.")),
            ("h3", "What mixing actually buys"),
            ("example", ("The two-by-two game, with both guarantees written out",
                         "On `(3, −1 / −2, 1)` the value is `1/7` with `p = (3/7, 4/7)` and "
                         "`q = (2/7, 5/7)`. Against `q`, row 1 earns "
                         "`3(2/7) − 1(5/7) = 1/7` and row 2 earns "
                         "`−2(2/7) + 1(5/7) = 1/7` &mdash; both exactly the value.",
                         "Now the guarantees. Row 1 played alone has worst case `min(3, −1) = −1`; "
                         "row 2 alone has `min(−2, 1) = −2`. So the best a pure strategy can "
                         "promise is `−1`. The mixture promises `1/7`, and the difference, "
                         "`8/7`, is what mixing bought. On the other side, the column player's "
                         "best pure enforcement is `min(max(3, −2), max(−1, 1)) = 1`, and the "
                         "mixture brings that down to `1/7` as well. The value sits strictly "
                         "between the two pure numbers, which is exactly the case in which "
                         "mixing is necessary.")),
            ("p", "So the honest version of the claim is not that pure strategies do worse "
                  "against the optimal mixture. Against `q`, every row in the support of `p` does "
                  "exactly as well as `v` &mdash; that is complementary slackness, and it is "
                  "forced. What pure strategies cannot do is guarantee `v` against an opponent "
                  "who responds, and the lab's hint says exactly that: not one pure choice does "
                  "better than the value, and most do worse."),
            ("h3", "When a pure strategy really is enough"),
            ("example", ("A game with a saddle point",
                         "On `(4, 2 / 3, 1)` the value is `2`, with `p = (1, 0)` and "
                         "`q = (0, 1)`: both optimal strategies are pure. The best pure "
                         "guarantee is `max(min(4, 2), min(3, 1)) = 2` and the least pure "
                         "enforcement is `min(max(4, 3), max(2, 1)) = 2`, and they agree.",
                         "That agreement is what a saddle point is, and when it happens mixing "
                         "buys nothing at all. The lab reports this case as such, which matters: "
                         "a reader shown only games that need mixing will over-generalise in the "
                         "other direction.")),
            ("p", "Complementary slackness reads across to the game with no translation. A row "
                  "played with positive probability forces the column player's constraint for "
                  "that row to be tight &mdash; that row earns exactly `v` against `q`. A column "
                  "played with positive probability forces the row player's constraint for that "
                  "column to be tight &mdash; that column holds `p` to exactly `v`. And a row "
                  "that earns strictly less than `v` against `q` must be played with probability "
                  "zero. Those three sentences are the whole of how a claimed pair of mixtures is "
                  "verified, and they are the previous certification lesson applied to different "
                  "nouns."),
            ("p", "A last note on scope, because a similarly named lesson exists elsewhere in "
                  "this library. Dynamic Programming and Optimal Substructure, on the Algorithms "
                  "path, has a lesson on games; it is about combinatorial games of perfect "
                  "information and the classification of positions as winning or losing. It "
                  "shares no object with this one &mdash; no payoff matrix, no mixture, no value "
                  "&mdash; and neither cites the other for a result."),
        ],
        "lab": ("duality", {
            "mode": "game",
            "preset": "cycle",
            "panel_title": "Edit the payoffs, and try a single choice against the mixture",
            "panel_intro": "The row player's programme and the column player's are each other's "
                           "dual, and the panel writes and solves both. Their common value is the "
                           "value of the game, and the last control plays one choice on its own "
                           "against the optimal mixture: not one of them does better than the "
                           "value, and most do worse.",
        }),
        "steps_title": "Solving a game as a pair of programmes",
        "steps_intro": "One substitution, one dual, one solve, and then a verification that needs no solving at all.",
        "steps": [
            ("Write the row player's programme with a variable for the guarantee",
             "Introduce `v`, require it to be at most the expected payoff against every column, "
             "add the mixture equality, and maximise `v`. Declare `v` free &mdash; a game can be "
             "worth a negative amount, and restricting it to be non-negative changes the "
             "problem."),
            ("Take the dual, and recognise the other player in it",
             "One dual variable per column constraint, which is the column mixture, plus one for "
             "the mixture equality, which is the value. The dual is a minimisation of that value "
             "subject to every row earning at most it. You have not written a second model; you "
             "have written the same one from the other side."),
            ("Solve, and read the value and both mixtures",
             "One solve gives the row mixture and, from the dual values in its final tableau, the "
             "column mixture. The two objectives are equal, which is the minimax theorem on this "
             "instance and a check on the arithmetic."),
            ("Verify by complementary slackness, then test each pure choice",
             "Every row played with positive probability must earn exactly `v` against the column "
             "mixture, and every column played with positive probability must hold the row "
             "mixture to exactly `v`. Then play each pure strategy on its own: none beats `v` "
             "against the optimum, and each one's own worst case shows what mixing bought."),
        ],
        "worked": {
            "title": "A two-by-two game, both programmes, and the verification",
            "intro": [
                "Two choices each, no best single one, and a value that is not a whole number. "
                "The verification at the end uses complementary slackness and no algorithm, which "
                "is what makes it worth writing out."
            ],
            "lines": [
                "payoffs      A = (  3  −1 )",
                "                 ( −2   1 )",
                "",
                "ROW PLAYER'S PROGRAMME",
                "  max v",
                "     column 1:    3p1 − 2p2  ≥  v",
                "     column 2:     −p1 + p2  ≥  v",
                "     mixture:       p1 + p2  =  1",
                "     p1, p2 ≥ 0,  v free",
                "",
                "ITS DUAL, which is the COLUMN PLAYER'S PROGRAMME",
                "  min w",
                "     row 1:        3q1 − q2  ≤  w",
                "     row 2:      −2q1 + q2   ≤  w",
                "     mixture:      q1 + q2   =  1",
                "     q1, q2 ≥ 0,  w free",
                "",
                "SOLVED       v = 1/7        p = (3/7, 4/7)      q = (2/7, 5/7)",
                "             w = 1/7        the two optima agree: minimax",
                "",
                "VERIFY, by complementary slackness and nothing else",
                "  p1 = 3/7 > 0  ⟹  row 1 must earn exactly v against q",
                "        3(2/7) − 1(5/7) = 6/7 − 5/7 = 1/7      ✓",
                "  p2 = 4/7 > 0  ⟹  row 2 must earn exactly v against q",
                "       −2(2/7) + 1(5/7) = −4/7 + 5/7 = 1/7     ✓",
                "  q1 = 2/7 > 0  ⟹  column 1 holds p to exactly v",
                "        3(3/7) − 2(4/7) = 9/7 − 8/7 = 1/7      ✓",
                "  q2 = 5/7 > 0  ⟹  column 2 holds p to exactly v",
                "         −(3/7) + 1(4/7) = 1/7                 ✓",
                "",
                "WHAT MIXING BOUGHT",
                "  row 1 alone   worst case  min( 3, −1) = −1",
                "  row 2 alone   worst case  min(−2,  1) = −2",
                "  best pure guarantee                   = −1",
                "  the mixture guarantees                =  1/7",
                "  difference                            =  8/7",
                "",
                "  column 1 alone  best the row player gets  max( 3, −2) = 3",
                "  column 2 alone                            max(−1,  1) = 1",
                "  least pure enforcement                                = 1",
                "  the mixture holds it to                               = 1/7",
                "",
                "  so  −1  <  1/7  <  1:  strictly between, and mixing is necessary",
            ],
            "after": [
                "The verification block is the lesson's real payload. Four substitutions confirm a "
                "claimed solution to a game, using only the conditions from the certification "
                "lesson, and no simplex run is involved &mdash; which is the same trick that "
                "certified a production plan, applied to different nouns.",
                "The final inequality is what distinguishes this game from one with a saddle "
                "point. On `(4, 2 / 3, 1)` the best pure guarantee and the least pure enforcement "
                "are both `2`, they meet, and the optimal strategies are pure: mixing buys "
                "nothing. Strict inequality is the condition under which a mixture is necessary, "
                "and computing both pure numbers is how you tell in advance.",
                "For a faded rehearsal, take the three-by-three cycle with rows `(0, −1, 1)`, "
                "`(1, 0, −1)`, `(−1, 1, 0)`. The supplied move is that symmetry makes "
                "`p = q = (1/3, 1/3, 1/3)` the obvious candidate. Verify it by complementary "
                "slackness rather than by solving, compute each row's own worst case, and say "
                "what the mixture bought. Then try the four-by-four preset, whose value is "
                "`8/21`, and confirm that every pure choice against the optimum earns exactly "
                "that.",
            ],
        },
        "quiz_title": "Two programmes, one value",
        "quiz": [
            {"q": "What is the column player's programme?",
             "a": ["The row player's, with every payoff negated",
                   "The dual of the row player's",
                   "A second, independently formulated linear programme",
                   "The row player's, with `v` fixed at the value"],
             "c": 1,
             "why": "Taking the dual of the row player's programme produces exactly the column "
                    "player's: the dual variables of the column constraints are the column "
                    "mixture and the dual variable of the mixture equality is the value. No "
                    "second model is written and no second solver is used, which is why strong "
                    "duality gives the minimax theorem for free."},
            {"q": "In the three-by-three cycle, `v = 0` and both optimal mixtures are `(1/3, 1/3, 1/3)`. What does each pure row earn against the optimal column mixture?",
             "a": ["`−1`", "`0`", "`1/3`", "It differs from row to row"],
             "c": 1,
             "why": "Each row earns exactly `0`, which is the value. That is complementary "
                    "slackness, not a coincidence: every row played with positive probability "
                    "must earn exactly `v` against the column mixture, and here all three rows "
                    "are played. `−1` is a pure row's own worst case, which is a different "
                    "quantity."},
            {"q": "Against `q = (2/7, 5/7)` in the two-by-two game, every pure row earns exactly `1/7`. So what does mixing buy?",
             "a": ["A higher payoff against the optimal opponent",
                   "A guarantee: the best a pure row can promise against the worst column is `−1`, and the mixture promises `1/7`",
                   "Nothing, since the payoffs against the optimum are equal",
                   "Protection against an opponent who chooses at random"],
             "c": 1,
             "why": "Against the optimal mixture nothing can do better than `v` &mdash; that is "
                    "what optimal means &mdash; so the gain is not there. It is in the worst "
                    "case: row 1 alone can be held to `−1` and row 2 alone to `−2`, while the "
                    "mixture cannot be held below `1/7`. An opponent choosing at random is the "
                    "easy case and needs no mixing at all."},
            {"q": "Why must `v` be a free variable in the row player's programme?",
             "a": ["So that the simplex method has a basic variable to start from",
                   "Because the value of a game can be negative",
                   "Because the mixture weights are already non-negative, so a further sign restriction would be redundant",
                   "Because the mixture equality already bounds it"],
             "c": 1,
             "why": "A game can be worth a negative amount &mdash; type `-2 -5; -6 -1` into the "
                    "lab's payoff box and the value is `−7/2` &mdash; and declaring `v ≥ 0` "
                    "would silently exclude the answer and return a different problem's optimum. "
                    "The sign of `v` has nothing to do with the signs of the probabilities, and "
                    "the mixture equality constrains those probabilities rather than `v`."},
        ],
        "mistakes": [
            ("Believing there is always a best single row, and that mixing is a confession of ignorance",
             "Against an opponent who can see your choice, a pure strategy is exploitable: row 1 "
             "of the two-by-two game can be held to `−1` and row 2 to `−2`, while the mixture "
             "cannot be held below `1/7`. Mixing is not hedging against uncertainty about the "
             "opponent; it is what makes the guarantee unexploitable. When a saddle point exists "
             "a pure strategy really is enough, and the lab ships one of those too so that the "
             "correction does not overshoot."),
            ("Restricting the value to be non-negative",
             "`v` is the guaranteed payoff and it can be negative &mdash; the payoff table is "
             "editable, and `-2 -5; -6 -1` is worth `−7/2` to the row player. Writing `v ≥ 0` "
             "produces a feasible programme with a different "
             "optimum, and nothing about the output announces that the wrong problem was solved. "
             "The same goes for its dual counterpart: the mixture equality's dual variable is "
             "free for the same reason."),
            ("Reading a mixture as a plan for a single play",
             "`p = (3/7, 4/7)` is not an instruction to play three sevenths of row 1. It is a "
             "probability distribution, and the value is an expectation: what the mixture "
             "guarantees on average against any opponent, not what any one play returns. On a "
             "single play the row player receives one entry of the matrix, and the guarantee is a "
             "statement about the distribution of that entry."),
        ],
        "standard": ("Finish when you can turn a payoff matrix into two dual programmes and verify a claimed solution without solving.",
                     "You should be able to write the row player's programme with a free `v`, "
                     "obtain the column player's as its dual, solve for the value and both "
                     "mixtures, verify them by complementary slackness, and compute the best pure "
                     "guarantee and the least pure enforcement to say whether mixing was "
                     "necessary at all."),
        "note": 'This is the second place on the course where duality is the content rather than the method, and it is the one where the theorem already had a name before it had this proof. Nothing new was needed: the row player\'s programme, its dual, and strong duality between them. A similarly named lesson on the Algorithms path, in Dynamic Programming and Optimal Substructure, is about combinatorial games of perfect information and winning and losing positions; it shares no object with this one and neither cites the other.',
    },
]
