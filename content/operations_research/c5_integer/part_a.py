"""Course 5, lessons 01-05 - the failure, then the modelling.

The failure first, because a reader who has not watched rounding fail will keep
reaching for it; then the four modelling atoms an integer programme is mostly
built from. Every figure below is read off the `integer` kit, which solves each
instance exactly rather than storing an answer.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "when-rounding-fails-the-lp-relaxation",
        "title": "When Rounding Fails",
        "module": "When rounding fails",
        "one_line": "Solve the relaxation, test every rounding of its optimum, and find the whole-number optimum by enumeration.",
        "summary": (
            "Dropping the requirement that the variables be whole numbers gives a "
            "different problem &mdash; a relaxation &mdash; whose optimum bounds the "
            "integer optimum rather than being it. The rounded point is a third object "
            "again: it can break a row outright, and when it does not it can be worth "
            "much less than the best whole-number plan, which may sit at the far end of "
            "the region."
        ),
        "key": [
            "relaxation   drop “whole numbers”     the region grows, so z_LP ≥ z_IP  (max)",
            "max 3x₁ + 4x₂    2x₁ + x₂ ≤ 6,  2x₁ + 3x₂ ≤ 9,  x₁, x₂ ≥ 0 and whole",
            "z_LP = 51/4  at (9/4, 3/2)      four roundings, and one of them is feasible",
            "best feasible rounding  (2, 1)  worth 10",
            "z_IP = 12  at (0, 3)            51/4 ≥ 12 ≥ 10   is the order to remember",
        ],
        "key_label": "One instance, three numbers, in that order",
        "concepts_intro": (
            "One hard idea, and it is a distinction: the relaxation, the rounded point "
            "and the integer optimum are three different objects, and the arithmetic "
            "that relates them relates only two."
        ),
        "concepts": [
            ("A relaxation is a different problem, and its value is a bound",
             "Delete the words “and whole” from the model and every plan that was "
             "allowed is still allowed, plus a great many that were not. A maximum "
             "taken over a larger set cannot be smaller, so `z_LP ≥ z_IP` always &mdash; "
             "and that inequality is the entire relationship. It says nothing about "
             "where the integer optimum is, only that it is not above `z_LP`."),
            ("There is no such thing as the rounding",
             "A point fractional in two coordinates has four roundings: floor and "
             "ceiling in every combination, `2ⁿ` of them for `n` fractional "
             "coordinates. “Round the answer” does not name one of them, and on this "
             "instance three of the four break a row. The one that does not is worth "
             "`10` against an optimum of `12`."),
            ("Feasible and best are two separate questions",
             "A rounding can pass every row and still be a poor plan, and that is the "
             "case worth fearing, because nothing complains. Here the best feasible "
             "rounding is `(2, 1)` and the best whole-number plan is `(0, 3)` &mdash; "
             "not adjacent to the fractional corner, not reachable from it by rounding, "
             "and worth two more."),
        ],
        "read_title": "The relaxation, the rounded point, and the integer optimum",
        "read_intro": "Three objects, one of which is a bound on another, and neither of which is the third.",
        "body": [
            ("def", ("Relaxation",
                     "A <strong>relaxation</strong> of an optimisation problem is "
                     "another problem with the same objective and a feasible set that "
                     "<em>contains</em> the original one. Dropping the requirement that "
                     "the variables be integers gives the <strong>linear programming "
                     "relaxation</strong>: the same rows, the same objective, and "
                     "`x ≥ 0` in place of `x ∈ {0, 1, 2, …}`.")),
            ("p", "The word is worth taking literally. Nothing has been approximated "
                  "and nothing has been solved approximately. A second, easier problem "
                  "has been written down, and it has its own exact answer, which the "
                  "simplex method of the earlier courses produces in exact fractions."),
            ("thm", ("The relaxation bounds the integer optimum",
                     "For a maximisation, `z_LP ≥ z_IP`. For a minimisation, "
                     "`z_LP ≤ z_IP`. In both cases the relaxation errs on the "
                     "optimistic side, and by an amount nothing in the relaxation "
                     "reveals.")),
            ("proof", ["Every plan that satisfies the rows and is whole also satisfies "
                       "the rows, so the integer feasible set is a subset of the "
                       "relaxed one.",
                       "A maximum over a subset is at most the maximum over the whole "
                       "set. Hence `z_IP ≤ z_LP`, and the minimisation case is the same "
                       "argument with the inequality reversed."]),
            ("p", "That is all that is proved, and readers routinely hear more in it. "
                  "It does not say the integer optimum is close to `z_LP`; it does not "
                  "say the integer optimum is near the fractional point; and it says "
                  "nothing whatever about rounding, which has not been mentioned."),
            ("example", ("Four roundings of (9/4, 3/2)",
                         "The relaxation of `max 3x₁ + 4x₂` subject to `2x₁ + x₂ ≤ 6` "
                         "and `2x₁ + 3x₂ ≤ 9` stops at `(9/4, 3/2)`, worth `51/4`. Its "
                         "roundings are `(2, 1)`, `(2, 2)`, `(3, 1)` and `(3, 2)`. "
                         "`(2, 2)` breaks the second row, which wants `10` where `9` is "
                         "allowed; `(3, 1)` breaks the first, which wants `7`; `(3, 2)` "
                         "breaks the first, which wants `8`. Only `(2, 1)` survives, and "
                         "it is worth `10`.")),
            ("h3", "The best whole-number plan need not be anywhere near the fractional one"),
            ("p", "There are ten whole-number plans in this region, and the best of them "
                  "is `(0, 3)`, worth `12`. It is not a rounding of `(9/4, 3/2)`; it is "
                  "at the other end of the region, with the first variable at zero "
                  "rather than at two or three. No amount of care about which way to "
                  "round finds it, because rounding only ever looks at the corners of "
                  "one little box."),
            ("math", ["  51/4   =  12.75          z_LP,  the relaxation",
                      "    12                     z_IP,  the best whole-number plan",
                      "    10                     the best feasible rounding",
                      "",
                      "  51/4  ≥  12  ≥  10       and only the first ≥ is a theorem"]),
            ("p", "The `3/4` between `51/4` and `12` is the integrality gap of this "
                  "instance. It is not an error bar and not a rounding error: it is the "
                  "price of the requirement that the plan be whole, measured on this "
                  "instance and no other. The second gap, the `2` between `12` and `10`, "
                  "is the price of having rounded instead of solved."),
            ("p", "The integer optimum here was found by trying every whole-number point "
                  "in the box &mdash; thirty candidates, ten of them feasible. That is "
                  "honest at this size and hopeless at any interesting one, which is "
                  "what the last four lessons of this course are for. What matters now "
                  "is that a number produced by enumeration is an answer, and a number "
                  "produced by rounding is a guess with no bound attached."),
            ("p", 'Algebra&rsquo;s &ldquo;Systems of Inequalities and Linear '
                  'Programming&rdquo; ends by saying that rounding an optimal corner is '
                  'not guaranteed to give the best whole-number answer, and that this is '
                  'a different subject. This is that subject, and this is its first '
                  'page: everything after it exists because the sentence is true.'),
        ],
        "lab": ("integer", {
            "mode": "lattice",
            "preset": "far",
            "panel_title": "Solve it, round it, then look at every whole-number plan",
            "panel_intro": "The relaxation is solved exactly, each of its roundings is "
                           "tested against every row with the broken row named, and the "
                           "best whole-number plan is found by trying all of them. Move "
                           "the right-hand side and watch which of the three numbers "
                           "moves.",
        }),
        "steps_title": "What to do with a fractional optimum",
        "steps_intro": "Four steps, and the third is the one that stops a wrong answer leaving the building.",
        "steps": [
            ("Solve the relaxation and write the optimum down",
             "Exactly, as fractions. `(9/4, 3/2)` worth `51/4` is a fact about a "
             "different problem, and labelling it `z_LP` rather than “the answer” is "
             "half of this lesson."),
            ("List every rounding, not one",
             "Floor and ceiling in every combination of the fractional coordinates: "
             "four here, `2ⁿ` in general. A coordinate that is already whole is not "
             "rounded at all and does not double the list."),
            ("Test each one against every row",
             "A rounding is a candidate until it has passed all of them, and when it "
             "fails, name the row. “It breaks the finishing row, which wants 10 where 9 "
             "is allowed” is a diagnosis; “it looked wrong” is not."),
            ("Find the whole-number optimum some other way",
             "At this size, by enumerating the lattice points of the region. The point "
             "of doing it once by hand is to see where the answer actually is before "
             "any method is trusted to find it."),
            ("Report the three numbers in order",
             "`z_LP`, then `z_IP`, then whatever the rounding was worth. The order "
             "`z_LP ≥ z_IP ≥ z_rounded` is the shape of every result in this course, "
             "and a report missing the middle term is a report with no answer in it."),
        ],
        "worked": {
            "title": "max 3x₁ + 4x₂ on the assembly and finishing rows",
            "intro": [
                "Two rows, two variables, and every figure exact. The instance is the "
                "lab's opening preset, so each line below can be checked against the "
                "panel.",
            ],
            "lines": [
                "max  3x₁ + 4x₂        2x₁ +  x₂ ≤ 6      (assembly)",
                "                      2x₁ + 3x₂ ≤ 9      (finishing)",
                "                      x₁, x₂ ≥ 0 and whole",
                "",
                "relaxation            x₁ = 9/4,  x₂ = 3/2",
                "                      z_LP = 3(9/4) + 4(3/2) = 27/4 + 6 = 51/4",
                "",
                "its four roundings",
                "  (2, 1)  down/down   assembly 5 ≤ 6,  finishing 7 ≤ 9    feasible, z = 10",
                "  (2, 2)  down/up     finishing wants 10, and 9 is allowed  infeasible",
                "  (3, 1)  up/down     assembly wants 7,  and 6 is allowed   infeasible",
                "  (3, 2)  up/up       assembly wants 8,  and 6 is allowed   infeasible",
                "",
                "every whole-number plan in the region — ten of them",
                "  (0,0) (0,1) (0,2) (0,3) (1,0) (1,1) (1,2) (2,0) (2,1) (3,0)",
                "  best is (0, 3):     assembly 3 ≤ 6,  finishing 9 ≤ 9     z_IP = 12",
                "",
                "  51/4  =  12.75   ≥   12   ≥   10",
                "   z_LP                z_IP    best rounding",
            ],
            "after": [
                "The line worth staring at is the last block. The relaxation put the "
                "first variable at `9/4` and the integer optimum puts it at `0`. Nothing "
                "about `(9/4, 3/2)` pointed at `(0, 3)`, and nothing was going to.",
                "The `(0, 3)` plan is also the one that uses the finishing row to the "
                "last unit &mdash; `2(0) + 3(3) = 9` exactly &mdash; while leaving three "
                "units of assembly idle. A whole-number plan often has that shape: one "
                "row tight, another slack, because the corner where both are tight is "
                "not a whole point.",
                "For a faded rehearsal, use the lab's slider to move the assembly "
                "right-hand side down to `5` and repeat all four steps. The supplied "
                "first move is that `z_LP` can only fall, because the region only "
                "shrank: it becomes `25/2` at `(3/2, 2)`. Notice that only one "
                "coordinate is fractional now, so there are two roundings rather than "
                "four. Say which of them is feasible and what it is worth, and whether "
                "`z_IP` moved at all, before the panel tells you.",
            ],
        },
        "quiz_title": "Bounds, roundings and the whole-number optimum",
        "quiz": [
            {"q": "For a maximisation, which relation between the relaxation's value `z_LP` and the integer optimum `z_IP` is always true?",
             "a": ["`z_LP ≥ z_IP`", "`z_LP ≤ z_IP`", "`z_LP = z_IP` whenever the region is bounded",
                   "`z_LP ≥ z_IP`, and `z_LP − z_IP ≤ 1`"],
             "c": 0,
             "why": "The relaxed feasible set contains the integer one, so a maximum "
                    "over it cannot be smaller. The fourth choice adds a bound on the "
                    "gap that is simply false: the gap can be made as large as you like "
                    "by scaling the objective."},
            {"q": "A relaxation stops at `(7/2, 3)`. How many roundings does this point have?",
             "a": ["One", "Two", "Four", "Eight"],
             "c": 1,
             "why": "Only the first coordinate is fractional, so the roundings are "
                    "`(3, 3)` and `(4, 3)`. `Four` would be right if both coordinates "
                    "were fractional; a coordinate already whole is not rounded and does "
                    "not double the list."},
            {"q": "On the instance above, the best feasible rounding is worth `10` and the integer optimum is `12`. What does the relaxation's value of `51/4` tell you about the `10`?",
             "a": ["That `10` is within `51/4 − 10 = 11/4` of the best whole-number plan, and no more than that",
                   "That `10` is within `1` of the best whole-number plan",
                   "That `10` is the best whole-number plan, since the others were infeasible",
                   "Nothing at all, because `51/4` is not a whole number"],
             "c": 0,
             "why": "A bound bounds. `51/4` proves that nothing whole beats `10` by more "
                    "than `11/4`, which happens to be loose here &mdash; the true "
                    "shortfall is `2`. The third choice confuses “the only feasible "
                    "rounding” with “the best whole plan”, which is the error this lesson "
                    "exists to destroy."},
            {"q": "A relaxation's optimum comes back at `(1, 3)`, already whole. What follows?",
             "a": ["Nothing, until the roundings are tested",
                   "That `(1, 3)` is optimal for the integer problem too",
                   "That the integer problem has no other feasible point",
                   "That the integrality gap of this instance is at least `1`"],
             "c": 1,
             "why": "A whole point attaining `z_LP` is feasible for the integer problem "
                    "and attains the bound, so nothing whole can beat it: the gap is "
                    "zero. This is the one case where the relaxation answers the "
                    "question, and it is worth checking for rather than assuming &mdash; "
                    "the lab's third preset is an instance where it happens."},
        ],
        "mistakes": [
            ("Rounding to the nearest whole point and stopping",
             "The nearest point is one of `2ⁿ` candidates and there is no reason for it "
             "to be feasible, let alone best. On this instance the nearest point to "
             "`(9/4, 3/2)` is `(2, 2)`, which breaks the finishing row, and the best "
             "whole plan is `(0, 3)`, which is nearest to nothing."),
            ("Treating an infeasible rounding as close enough",
             "`(2, 2)` wants ten units of finishing capacity where nine exist. That is "
             "not a plan that is slightly wrong; it is not a plan. The habit of naming "
             "the row it breaks &mdash; and by how much &mdash; is what keeps “close” "
             "from quietly becoming “allowed”."),
            ("Reading z_LP as an estimate of the answer",
             "`51/4` is an exact answer to a different question. It bounds `z_IP` from "
             "above and predicts nothing: the gap here is `3/4`, and an instance of the "
             "same size can have a gap of zero or of a hundred. Any sentence of the form "
             "“the answer is about `z_LP`” is unsupported."),
        ],
        "standard": ("Finish when a rounded optimum reads as a candidate to be tested, not as an answer.",
                     "You should be able to solve a two-variable relaxation exactly, "
                     "list all of its roundings, name the row each infeasible one breaks, "
                     "find the whole-number optimum by enumeration at this size, and "
                     "state `z_LP ≥ z_IP ≥ z_rounded` while saying which of those two "
                     "inequalities is a theorem and which is an observation about the "
                     "instance in front of you."),
        "note": 'Everything after this lesson is a way of getting `z_IP` without enumerating the region, because the region is the part that grows. The next four lessons do not solve anything: they write models, because an integer programme is mostly a modelling problem and a correct solve of the wrong model is the most expensive result in the subject. “Binary Variables and Logical Constraints” starts with the variable that carries a yes-or-no decision.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "binary-variables-and-logical-constraints",
        "title": "Binary Variables and Logical Constraints",
        "module": "Modelling with binaries",
        "one_line": "Turn five stated conditions into inequalities on binaries and verify each against its truth table.",
        "summary": (
            "A variable restricted to `0` or `1` is a yes-or-no decision, and the "
            "connectives of logic become linear inequalities on such variables. The "
            "point of the lesson is not the list of encodings but the check: an "
            "inequality is compared with the condition on every assignment, and a wrong "
            "encoding is refuted by a row rather than argued about."
        ),
        "key": [
            "y ∈ {0, 1}          y = 1 the project is chosen,  y = 0 it is not",
            "if A then B         y_A − y_B ≤ 0        not  y_B − y_A ≤ 0",
            "at least one of A, B    y_A + y_B ≥ 1    at most k    Σ y ≤ k",
            "exactly one         Σ y = 1              both         y_A + y_B ≥ 2",
            "an encoding is checked on all 2ⁿ assignments; one disagreeing row refutes it",
        ],
        "key_label": "Five conditions, and the check that settles each one",
        "concepts_intro": (
            "The encodings are a short list and they are not the hard part. The hard "
            "part is that an encoding is a claim about every assignment, and claims like "
            "that are settled by evidence rather than by plausibility."
        ),
        "concepts": [
            ("A binary is a decision, not a quantity",
             "`y_A = 1` means “project A is chosen” and `y_A = 0` means it is not. There "
             "is no `y_A = 0.6`, and the first thing to write next to any binary is the "
             "sentence it stands for. Half of all wrong encodings are wrong because the "
             "author never fixed which way round `1` meant."),
            ("A connective becomes an inequality, and the direction is the content",
             "“If A then B” is `y_A − y_B ≤ 0`, which reads: A may not be chosen unless "
             "B is. Swap the two letters and you have the converse, which permits A "
             "without B &mdash; the one case the condition forbids. The inequality is "
             "short enough that nothing in its appearance tells you which of the two you "
             "have written."),
            ("An encoding is refuted by a row",
             "There are `2ⁿ` assignments and the encoding must agree with the condition "
             "on every one of them. With three binaries that is eight rows, which can be "
             "read in a few seconds, and the converse of “if A then B” disagrees on four "
             "of them. A reader who has seen the row `y_A = 1, y_B = 0` does not write "
             "the converse again."),
        ],
        "read_title": "Yes-or-no decisions, and encodings that have been checked",
        "read_intro": "The five conditions almost every practical model is built from, and the eight-row check that certifies each one.",
        "body": [
            ("def", ("Binary variable",
                     "A <strong>binary variable</strong> is a variable restricted to the "
                     "set `{0, 1}`. It carries a decision: `1` for the thing happening "
                     "and `0` for it not happening. A model with binaries and nothing "
                     "else is a <strong>binary</strong> or <strong>0/1</strong> "
                     "programme; a model with binaries and continuous variables together "
                     "is a <strong>mixed integer</strong> programme.")),
            ("def", ("Encoding of a condition",
                     "A linear inequality on binaries <strong>encodes</strong> a "
                     "condition when, for every assignment of `0` and `1` to the "
                     "variables, the inequality holds exactly when the condition holds. "
                     "One assignment on which the two disagree <strong>refutes</strong> "
                     "the encoding, and one is all it takes.")),
            ("p", "That definition is why the lab evaluates your inequality on every "
                  "assignment beside the truth table of the condition. Discrete "
                  "Mathematics builds those tables in "
                  "&ldquo;Logical Connectives&rdquo; and &ldquo;Truth Tables&rdquo;, and "
                  "the check here is the same object with one extra column: what the "
                  "inequality evaluates to, and whether it holds."),
            ("example", ("If A then B, and the row that refutes the converse",
                         "The condition forbids one combination and permits the other "
                         "three: `y_A = 1, y_B = 0` is out, and `(0,0)`, `(0,1)`, `(1,1)` "
                         "are in. The inequality `y_A − y_B ≤ 0` agrees on all eight "
                         "assignments of three binaries. The converse `y_B − y_A ≤ 0` "
                         "disagrees on four of them, and the first the lab reports is "
                         "`y_A y_B y_C = 1 0 1`: the condition fails there and the "
                         "inequality holds, so the converse permits exactly the case the "
                         "condition was written to forbid.")),
            ("h3", "Five conditions and the inequality each one is"),
            ("ul", ["<strong>If A then B.</strong> `y_A − y_B ≤ 0`. Equivalently "
                    "`y_A ≤ y_B`: choosing A forces B, and B alone is allowed.",
                    "<strong>At least one of A and B.</strong> `y_A + y_B ≥ 1`. "
                    "Both is allowed, because “or” here is the inclusive one.",
                    "<strong>At most k of them.</strong> `y_A + y_B + y_C ≤ k`. "
                    "With three projects and `k = 2` the only excluded assignment is "
                    "all three.",
                    "<strong>Exactly one.</strong> `y_A + y_B + y_C = 1`. An "
                    "equality, and the `≤ 1` version is a different condition.",
                    "<strong>Both A and B.</strong> `y_A + y_B ≥ 2`, or simply the two "
                    "assignments `y_A = 1` and `y_B = 1` if one row is not required."]),
            ("p", "The `≤ 1` against `= 1` pair is worth one more sentence, because the "
                  "two conditions differ on a single assignment and it is the empty one. "
                  "“At most one” permits choosing nothing; “exactly one” does not. The "
                  "lab refutes `y_A + y_B + y_C ≤ 1` as an encoding of “exactly one” on "
                  "the row `0 0 0`, and on that row alone."),
            ("example", ("Both is not a product",
                         "The condition “both A and B” describes one assignment, and the "
                         "expression `y_A · y_B` is not linear, so it has no place in a "
                         "linear model at all. Nothing is lost: `y_A + y_B ≥ 2` holds on "
                         "`1 1` and fails on the other three combinations, which is "
                         "exactly the condition. `y_A + y_B ≥ 1` is the encoding readers "
                         "reach for instead, and it is refuted on four rows &mdash; the "
                         "first being `1 0 1`, where one project is chosen and the "
                         "inequality is satisfied.")),
            ("p", "Checking costs `2ⁿ` rows, so it is affordable for a handful of "
                  "binaries and not for fifty. That is not a limitation of the method: "
                  "the encodings being checked are local &mdash; two or three variables "
                  "at a time &mdash; and a model with fifty binaries is built from rows "
                  "that each involve a few. Verify the row, then use it."),
            ("p", "The habit generalises past the point where a truth table fits. In the "
                  "two lessons after next, the condition is about continuous quantities "
                  "and the check is a pair of re-solves rather than eight rows, but the "
                  "discipline is identical: fix the binary at each value, look at what "
                  "the model then says, and confirm it is what you meant."),
        ],
        "lab": ("integer", {
            "mode": "logic",
            "preset": "ifthen",
            "panel_title": "Pick a condition, then test an inequality against it",
            "panel_intro": "The condition is evaluated on all eight assignments of three "
                           "binaries and so is the inequality; every row where they "
                           "disagree is marked. Try the encoding that is right, then the "
                           "one readers reach for, then one of your own.",
        }),
        "steps_title": "Writing an encoding you can defend",
        "steps_intro": "The first two steps are prose and the last two are evidence. Skipping either pair is how a wrong row ships.",
        "steps": [
            ("Name each binary and say what 1 means",
             "In a sentence, on the page. “`y_A = 1` when the extension is built.” An "
             "encoding cannot be checked against a condition until both are written down "
             "in the same words."),
            ("State the condition with no arithmetic in it",
             "“We may not build the extension unless the yard is resurfaced.” Which "
             "combinations are forbidden is now readable, and it is the only thing the "
             "inequality has to reproduce."),
            ("Propose the inequality",
             "Usually a sum of the binaries against a constant. Write the relation and "
             "the right-hand side deliberately: `≥ 1`, `≤ 1` and `= 1` are three "
             "different conditions, and `≤ 2` differs from `≤ 3` on exactly one "
             "assignment."),
            ("Evaluate it on every assignment beside the condition",
             "Two columns, `2ⁿ` rows, and a third column saying whether they agree. This "
             "is the step that turns an opinion into a fact, and it is the whole reason "
             "the lab exists."),
            ("Keep the refuting row",
             "When an encoding fails, write down the assignment that killed it next to "
             "the encoding that survived. `y_A = 1, y_B = 0` is worth more than the rule "
             "it corrects, because it is what you will remember."),
        ],
        "worked": {
            "title": "Four projects, four conditions, one table each",
            "intro": [
                "A capital budget with four candidate projects. Each condition is stated, "
                "encoded, and then checked on the assignments its variables range over.",
            ],
            "lines": [
                "y₁ y₂ y₃ y₄ ∈ {0, 1}      y = 1 means the project is funded",
                "",
                "1  the warehouse needs the access road first",
                "   if y₁ then y₂                y₁ − y₂ ≤ 0",
                "   y₁ y₂ = 0 0   condition holds   0 ≤ 0   holds     agree",
                "         0 1   holds              −1 ≤ 0   holds     agree",
                "         1 0   FAILS                1 ≤ 0   fails     agree",
                "         1 1   holds                0 ≤ 0   holds     agree",
                "   the converse y₂ − y₁ ≤ 0 holds at 1 0, where the condition fails",
                "",
                "2  fund at most two of the first three",
                "   y₁ + y₂ + y₃ ≤ 2             excluded assignment: 1 1 1 only",
                "   ≤ 3 is refuted by that one row, and by no other",
                "",
                "3  fund exactly one of the two depots",
                "   y₃ + y₄ = 1                  ≤ 1 is refuted by 0 0",
                "",
                "4  fund both or neither of the paired upgrades",
                "   y₁ − y₂ ≤ 0  and  y₂ − y₁ ≤ 0,  which together are  y₁ = y₂",
                "   here the converse is not an error: both directions were wanted",
            ],
            "after": [
                "Condition 4 is the reason the converse must be recognised rather than "
                "merely avoided. `y_B − y_A ≤ 0` is a perfectly good inequality; it "
                "encodes “if B then A”. Writing both directions encodes equivalence, and "
                "that is sometimes the condition. What is never right is writing one and "
                "believing it says the other.",
                "Condition 2 shows how thin the margin can be. `≤ 2` and `≤ 3` differ on "
                "one assignment out of eight, and with `≤ 3` the row is satisfied by "
                "every assignment there is &mdash; a constraint that constrains nothing, "
                "which is a harder defect to notice than an infeasible model.",
                "For a faded rehearsal, encode “if either depot is funded then the access "
                "road is” and check it. The supplied first move is that this is two "
                "implications rather than one, so it is `y₃ − y₂ ≤ 0` together with "
                "`y₄ − y₂ ≤ 0`. Decide before opening the quiz whether the single row "
                "`y₃ + y₄ − 2y₂ ≤ 0` encodes the same condition, and name the assignment "
                "that settles it.",
            ],
        },
        "quiz_title": "Conditions, encodings and refuting rows",
        "quiz": [
            {"q": "Which inequality encodes “if project A is chosen then project B must be too”?",
             "a": ["`y_A − y_B ≤ 0`", "`y_B − y_A ≤ 0`", "`y_A + y_B ≥ 1`", "`y_A + y_B = 1`"],
             "c": 0,
             "why": "`y_A ≤ y_B` forbids `y_A = 1` with `y_B = 0` and permits the other "
                    "three combinations. The second choice is the converse, which is "
                    "satisfied at `y_A = 1, y_B = 0` &mdash; the row that refutes it. The "
                    "third permits A without B, and the fourth forbids funding both, "
                    "which the condition allows."},
            {"q": "On which assignment does `y_A + y_B + y_C ≤ 1` fail to encode “exactly one of the three”?",
             "a": ["`1 1 0`", "`1 1 1`", "`0 0 0`", "`0 1 0`"],
             "c": 2,
             "why": "At `0 0 0` the inequality holds and the condition fails, so “at most "
                    "one” and “exactly one” part company there and only there. `1 1 0` "
                    "and `1 1 1` are excluded by both; `0 1 0` is permitted by both."},
            {"q": "You need “at least one of A and B”. A colleague writes `y_A + y_B ≤ 1`. Which row refutes it?",
             "a": ["`y_A = 0, y_B = 0`, where the condition holds and the inequality fails",
                   "`y_A = 1, y_B = 1`, where the condition holds and the inequality fails",
                   "`y_A = 1, y_B = 0`, where both hold",
                   "No row refutes it; the two are the same condition written twice"],
             "c": 1,
             "why": "`≤ 1` is “at most one”, which excludes choosing both &mdash; and "
                    "choosing both satisfies “at least one”. The first choice has the "
                    "right assignment for a different refutation and describes it "
                    "backwards: at `0 0` the condition fails and the inequality holds, "
                    "which is a second disagreeing row rather than the one stated."},
            {"q": "Why is `y_A · y_B = 1` not used for “both A and B”?",
             "a": ["Because it is false when both are chosen",
                   "Because a product of variables is not linear, and `y_A + y_B ≥ 2` says the same thing",
                   "Because it permits `y_A = 1, y_B = 0`",
                   "Because products are only defined for continuous variables"],
             "c": 1,
             "why": "The product is arithmetically correct and structurally inadmissible: "
                    "a linear model has no term `y_A y_B`. Nothing is lost, because "
                    "`y_A + y_B ≥ 2` holds on `1 1` and fails on the other three "
                    "assignments, which is the condition exactly."},
        ],
        "mistakes": [
            ("Writing the converse for if-then",
             "`y_A ≥ y_B` permits choosing A while leaving B unfunded, which is the one "
             "thing “if A then B” forbids. The assignment `y_A = 1, y_B = 0` is where it "
             "shows, and it is the row to keep: the lab reports it as the first of four "
             "disagreements once the third binary is free to be either value."),
            ("Using ≤ 1 for at least one",
             "“At most one” and “at least one” differ on two assignments and share the "
             "word “one”, which is the whole trap. `≥ 1` forbids the empty choice; `≤ 1` "
             "forbids the full one. Reading the relation aloud as “at least” or “at most” "
             "before writing it catches this every time."),
            ("Multiplying binaries",
             "`y_A y_B` for “both”, `y_A(1 − y_B)` for “A but not B”: both are natural and "
             "neither is linear, so a solver that accepts them is not solving a linear "
             "programme. Every condition on this list has a linear encoding, and where a "
             "product genuinely seems necessary the model usually wants one more binary "
             "rather than one fewer."),
        ],
        "standard": ("Finish when writing an encoding without checking it feels like asserting a theorem without proving one.",
                     "You should be able to translate if-then, at-least-one, at-most-k, "
                     "exactly-one and both into inequalities on binaries, verify each on "
                     "every assignment of its variables, and name the row that would "
                     "refute the encoding a reader reaches for instead &mdash; "
                     "`y_A = 1, y_B = 0` for the converse, and `0 0 0` for “at most one” "
                     "standing in for “exactly one”."),
        "note": '“Both” is not `y_A · y_B`. A product is not linear and it is not needed: “both” is the pair of assignments `y_A = 1` and `y_B = 1`, or the single row `y_A + y_B ≥ 2` when one row is wanted. The same instinct produces `y_A(1 − y_B)` for “A but not B”, which is `y_A − y_B ≥ 1` written badly &mdash; and that one the lab will check for you.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-knapsack-and-set-covering-models",
        "title": "Knapsack and Set Covering",
        "module": "Modelling with binaries",
        "one_line": "Build both atoms from data, solve both relaxations, and say what each one made fractional.",
        "summary": (
            "One capacity with chosen items, and every requirement covered by at least "
            "one chosen set: these are the two models most practical binary programmes "
            "are assembled from. Their relaxations are fractional in characteristic ways "
            "&mdash; one splits a single item, the other spreads halves across "
            "overlapping sets &mdash; and that is exactly why a relaxation's value is a "
            "bound rather than an answer."
        ),
        "key": [
            "knapsack    max Σ v_j y_j    s.t.  Σ w_j y_j ≤ W,   y_j ∈ {0, 1}",
            "covering    min Σ c_j y_j    s.t.  Σ y_j ≥ 1 over the sets covering i",
            "relaxed knapsack  take in v/w order and split exactly one item",
            "relaxed covering  spread halves over a ring of overlapping sets",
            "240 ≥ 220 ≥ 160        bound ≥ optimum ≥ what greed got",
            "covering ≥ 1  is not  partitioning = 1:  one instance, two answers",
        ],
        "key_label": "Two models, and three numbers for each",
        "concepts_intro": (
            "Two models and one idea about both of them: the way a relaxation goes "
            "fractional is a property of the model's shape, not an accident of the data."
        ),
        "concepts": [
            ("One capacity, chosen items",
             "Maximise `Σ v_j y_j` subject to one row `Σ w_j y_j ≤ W`. Every selection "
             "problem with a single budget is this model: which features to ship in a "
             "release, which repairs to fund this year, which crates to load. The "
             "binaries make it hard; the single row makes it the smallest hard model "
             "there is."),
            ("Every requirement covered by some chosen set",
             "Minimise `Σ c_j y_j` subject to one row per requirement saying that at "
             "least one set containing it is chosen. Depots covering districts, shifts "
             "covering hours, tests covering code paths. The rows outnumber the variables "
             "and each one is an “at least one of these” from the previous lesson."),
            ("Each relaxation goes fractional in its own way",
             "The relaxed knapsack fills in value-per-weight order and splits exactly one "
             "item, because one row can only be tight in one place. The relaxed covering "
             "problem does something else entirely: on a ring of overlapping sets it puts "
             "`1/2` on every one of them, satisfying each row with two halves and paying "
             "half the price."),
        ],
        "read_title": "The two atoms, and the shape of each relaxation",
        "read_intro": "Both models from data, both relaxations solved, and the three numbers each one produces.",
        "body": [
            ("def", ("The 0/1 knapsack model",
                     "Items `1, …, n` with values `v_j` and weights `w_j`, and a capacity "
                     "`W`. Choose `y_j ∈ {0, 1}` to maximise `Σ v_j y_j` subject to "
                     "`Σ w_j y_j ≤ W`. The name is the picture: one bag, a weight limit, "
                     "and each item either in or out.")),
            ("def", ("The set-covering model",
                     "Requirements `1, …, m` and sets `1, …, n` with costs `c_j`, where "
                     "set `j` covers some of the requirements. Choose `y_j ∈ {0, 1}` to "
                     "minimise `Σ c_j y_j` subject to, for each requirement `i`, the row "
                     "`Σ y_j ≥ 1` taken over the sets that cover `i`. Replacing that `≥` "
                     "by `=` gives <strong>set partitioning</strong>, which is a "
                     "different problem.")),
            ("p", "Take three items worth `60`, `100` and `120` weighing `10`, `20` and "
                  "`30`, with a capacity of `50`. Their values per unit weight are `6`, "
                  "`5` and `4`, so the relaxation loads the first two whole &mdash; "
                  "thirty units of weight, `160` of value &mdash; and then takes `2/3` of "
                  "the third to fill the bag, for `240`. That is the bound."),
            ("example", ("Three answers on one instance",
                         "The relaxation is worth `240` and gets there by splitting the "
                         "third item. Greed by value per weight takes the first two, "
                         "cannot fit the third in the remaining twenty units, and stops "
                         "at `160`. The best whole choice, found by trying all eight "
                         "subsets, is the second and third items together: weight exactly "
                         "`50`, value `220`. So `240 ≥ 220 ≥ 160`, and the middle number "
                         "is the only one that is an answer.")),
            ("p", "Discrete Mathematics&rsquo; &ldquo;Greedy Algorithms&rdquo; closes by "
                  "showing the value-per-weight rule optimal for the fractional problem "
                  "and defeated by the 0/1 version, which is precisely the gap between "
                  "`240` and `160` here. The rule is not a heuristic for this model; it "
                  "is the exact solution to the relaxation, and the two facts are easy to "
                  "confuse because the arithmetic is the same."),
            ("h3", "The covering relaxation spreads halves"),
            ("p", "Five districts in a ring, each reachable from two of five depots, "
                  "every depot costing `2`. Each row says “at least one of these two "
                  "depots”. The relaxation satisfies all five rows by opening every depot "
                  "to the extent of `1/2`, and pays `5`. No whole choice does: three "
                  "depots are needed, costing `6`. The `1` between them is the price of "
                  "not being able to open half a depot."),
            ("example", ("Covering is not partitioning",
                         "On that same ring, require each district to be covered "
                         "<em>exactly</em> once instead of at least once. Nothing in the "
                         "data changed and only the relation did, and now there is no "
                         "feasible choice of depots at all: an odd ring cannot be "
                         "partitioned by adjacent pairs. The relaxation of the "
                         "partitioning version is still solvable and still worth `5`, "
                         "which is the cruellest part &mdash; a relaxation being feasible "
                         "says nothing about whether the integer problem is.")),
            ("p", "Both atoms above were solved exactly by enumerating every subset, and "
                  "that is where this lesson's method ends: `2¹²` is `4096`, which is "
                  "instant, and `2⁵⁰` is not a number of subsets anybody enumerates. What "
                  "is this lesson's own is the pair of models and the shape of their "
                  "relaxations. Four results about them are used here and proved "
                  "elsewhere, each by its owner."),
            ("ul", ["The exact method for 0/1 knapsack beyond enumeration is a "
                    "pseudo-polynomial dynamic programme &mdash; the Algorithms path, "
                    "&ldquo;0/1 Knapsack and Pseudo-Polynomial Time&rdquo;.",
                    "The approximation with a proved ratio is the fully polynomial scheme "
                    "of &ldquo;A Fully Polynomial Approximation for Knapsack&rdquo;, in "
                    "the same subject.",
                    "The `ln n` ratio for greedy set cover is &ldquo;Greedy Set Cover and "
                    "the ln n Ratio&rdquo;, which proves what greed costs in the worst "
                    "case rather than measuring it on one instance.",
                    "Why both problems are hard in the technical sense belongs to "
                    "Discrete Mathematics&rsquo; &ldquo;P, NP and NP-Completeness&rdquo;, "
                    "which is also where the word “hard” acquires its meaning."]),
            ("p", "None of those four is derived here, and none of them is needed to "
                  "write the models down. What is needed is the reflex of solving the "
                  "relaxation first and looking at what it made fractional, because the "
                  "split item and the spread halves each point at the row doing the work "
                  "&mdash; which is the variable to branch on when the search lesson "
                  "arrives."),
        ],
        "lab": ("integer", {
            "mode": "knapsack",
            "preset": "classic",
            "cover": "cycle",
            "panel_title": "Edit the instance; the bound, the guess and the optimum all move",
            "panel_intro": "Every number is recomputed from the items or the incidence "
                           "rows as typed: the relaxation by simplex, greed by the "
                           "density rule, the optimum by enumerating every subset. Switch "
                           "the model to the covering instance and then change “at least "
                           "once” to “exactly once”.",
        }),
        "steps_title": "Building either atom from data",
        "steps_intro": "The same five steps for both models. The fourth is where a relaxation earns its keep.",
        "steps": [
            ("Decide what one binary stands for",
             "An item taken, or a set opened. If the answer is “how many of them”, this "
             "is not one of these two models and a binary is the wrong variable."),
            ("Write the rows, one per constraint you actually have",
             "A knapsack has exactly one row, and a second row means a second model. A "
             "covering problem has one row per requirement, and each row lists the sets "
             "that cover it &mdash; which is read straight off the incidence table."),
            ("Solve the relaxation and look at what is fractional",
             "One split item, or a scatter of halves. This is the diagnostic step: it "
             "tells you which row is binding and, later, which variable to branch on."),
            ("Get a whole answer, and a second whole answer",
             "Greed by value per weight, or greed by cost per newly covered requirement, "
             "gives one. Enumeration at this size gives the best one. Two whole numbers "
             "are worth more than one, because their difference is what greed cost."),
            ("State the bound relation",
             "`z_LP ≥ z_IP ≥ z_greedy` for a maximisation, reversed for a minimisation. "
             "Write all three and label them; a covering result reported as one number "
             "cannot be told apart from a guess."),
        ],
        "worked": {
            "title": "Three items at a capacity of 50, and five districts in a ring",
            "intro": [
                "Both atoms on one page, each solved three ways. Every figure is the "
                "lab's, on its opening presets.",
            ],
            "lines": [
                "KNAPSACK      v = 60, 100, 120      w = 10, 20, 30      W = 50",
                "",
                "  density     60/10 = 6     100/20 = 5     120/30 = 4",
                "  relaxation  item 1 whole, item 2 whole   →  w = 30, v = 160",
                "              20 of capacity left, so 20/30 = 2/3 of item 3",
                "              z_LP = 160 + (2/3)(120) = 160 + 80 = 240",
                "  greed       items 1 and 2; item 3 does not fit    z = 160",
                "  exact       all 2³ = 8 subsets:",
                "                {1,2}  w 30  v 160        {1,3}  w 40  v 180",
                "                {2,3}  w 50  v 220        {1,2,3}  w 60  too heavy",
                "              z_IP = 220 at {2, 3}",
                "",
                "  240   ≥   220   ≥   160        gap 20 above, gap 60 below",
                "",
                "COVERING      5 districts in a ring, 5 depots, each cost 2",
                "              district i is covered by depot i and depot i+1",
                "",
                "  relaxation  every y_j = 1/2, each row 1/2 + 1/2 = 1 ≥ 1",
                "              z_LP = 5(2)(1/2) = 5",
                "  exact       32 subsets, 11 of them feasible; cheapest is 3 depots",
                "              z_IP = 6",
                "  greed       cost per newly covered district: also 6 here",
                "",
                "  with “exactly once” instead:   no feasible choice at all",
                "  its relaxation:                still 5",
            ],
            "after": [
                "The knapsack's two gaps say different things. The `20` above is what "
                "integrality costs on this instance; the `60` below is what greed costs. "
                "Only the first is a property of the model &mdash; the second would change "
                "if greed were replaced by anything better, and the bound would not.",
                "The covering relaxation's halves are worth a second look. Every one of "
                "the five rows is satisfied with nothing to spare, and the total is `5` "
                "against an answer of `6`. That is the characteristic shape: a covering "
                "relaxation pays for the rows and not for the indivisibility, and on an "
                "odd ring the indivisibility is the whole cost.",
                "For a faded rehearsal, drop the knapsack capacity to `40` and redo all "
                "three numbers. The supplied first move is that the density order does "
                "not change, because the items did not &mdash; so the relaxation is still "
                "items 1 and 2 whole and then a fraction of item 3, and only the fraction "
                "moves. Work out the fraction, then the exact optimum, and say what "
                "happened to each of the two gaps.",
            ],
        },
        "quiz_title": "Two atoms and their relaxations",
        "quiz": [
            {"q": "The relaxed knapsack on three items is worth `240`, greed gets `160`, and enumeration gives `220`. Which number is the bound, and which is the answer?",
             "a": ["`240` bounds and `220` answers", "`220` bounds and `240` answers",
                   "`160` bounds and `220` answers", "`240` bounds and `160` answers"],
             "c": 0,
             "why": "The relaxation maximises over a larger set, so `240` is above the "
                    "integer optimum; enumeration over every subset gives the optimum "
                    "itself, `220`. Greed's `160` is a feasible choice and therefore a "
                    "lower bound, which is useful and is not an answer."},
            {"q": "In the relaxed 0/1 knapsack with a single capacity row, how many items can come back at a fractional value?",
             "a": ["None", "At most one", "At most two", "Any number of them"],
             "c": 1,
             "why": "One row can be tight in one place. The relaxation fills in "
                    "value-per-weight order until the capacity runs out part way through "
                    "an item, and that item is the only fractional one. This is exactly "
                    "the fractional rule Discrete Mathematics proves optimal in “Greedy "
                    "Algorithms”."},
            {"q": "A covering instance is feasible with each requirement covered at least once. You change `≥ 1` to `= 1`. What can happen?",
             "a": ["Nothing: the two are the same condition written differently",
                   "The cost can rise, but feasibility is unaffected",
                   "The instance can become infeasible, even though its relaxation still solves",
                   "The relaxation becomes infeasible first, which is how you notice"],
             "c": 2,
             "why": "An odd ring covered by adjacent pairs is feasible under `≥ 1` and "
                    "has no whole solution at all under `= 1`. Its relaxation is still "
                    "worth `5`, so the relaxation gives no warning &mdash; which is why "
                    "“covering and partitioning are the same problem” is an expensive "
                    "belief."},
            {"q": "The relaxed covering problem on the five-district ring puts `1/2` on every depot. What does that tell you?",
             "a": ["That rounding each `1/2` up gives the optimal cover: all five depots",
                   "That the cheapest whole cover costs at least `5`, and nothing more",
                   "That every depot is in the optimal cover",
                   "That the instance is infeasible for whole choices"],
             "c": 1,
             "why": "A relaxation's value is a lower bound for a minimisation and the "
                    "fractional solution is not a plan. The optimum is `6`, using three "
                    "depots; rounding every `1/2` up gives five depots costing `10`, "
                    "which is the fallacy this course opened with."},
        ],
        "mistakes": [
            ("Using the density rule as though it solved the 0/1 problem",
             "Value per weight is exactly optimal when items may be split and merely "
             "plausible when they may not. Here it returns `160` against an optimum of "
             "`220`, because it commits the capacity to two light items and then cannot "
             "fit the third. The rule is how you solve the relaxation, not how you solve "
             "the model."),
            ("Turning ≥ 1 into = 1 to tidy the model",
             "It looks like the same requirement stated more precisely and it is a "
             "different problem: the ring instance loses every feasible solution. If "
             "double coverage is genuinely forbidden, the equality is right and the "
             "infeasibility is real information; if it is merely untidy, the `≥` was "
             "correct."),
            ("Reading the relaxation's fractional take as a plan",
             "“Two-thirds of the third crate” and “half a depot” are arithmetic, not "
             "instructions. The value of such a solution is a bound and the solution "
             "itself is not a solution &mdash; which is the same lesson as the first "
             "lesson of this course, arriving in a model where it is harder to see."),
        ],
        "standard": ("Finish when you can write either atom from a table of data and predict what its relaxation will make fractional.",
                     "You should be able to formulate a knapsack and a covering instance "
                     "from data, solve both relaxations, name the single split item in "
                     "one and the spread halves in the other, produce a greedy answer and "
                     "an exact one by enumeration at this size, state both gaps, and say "
                     "what changes when a covering row becomes an equality."),
        "note": 'Enumeration stops being an option somewhere around a dozen binaries, and the two lessons that close this course are what replaces it. Before that, &ldquo;Fixed Charges, Facility Location and Big-M&rdquo; adds the one piece these two atoms are missing: a cost that is paid only if an activity happens at all, which needs a binary tied to a continuous quantity rather than standing alone.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "fixed-charges-facility-location-and-big-m",
        "title": "Fixed Charges, Facility Location and Big-M",
        "module": "Modelling with binaries",
        "one_line": "Link a fixed cost to a decision, size the constant that does the linking, and measure what a loose one costs.",
        "summary": (
            "A cost paid only if an activity happens at all needs a binary tied to the "
            "continuous activity by `x ≤ M y`. The link works for any `M` large enough, "
            "and that is the trap: every unit above the smallest valid value weakens the "
            "relaxation's bound, because the relaxation is then free to open a facility "
            "for a fraction of its fixed cost. The price is measurable, in bound and in "
            "nodes, on your own instance."
        ),
        "key": [
            "fixed charge   x ≤ M y,   y ∈ {0, 1}      y = 0 forces x = 0",
            "valid M        at least every feasible x:  capacity, or total demand",
            "the relaxation buys  y = x/M              a facility open for a fraction",
            "effective unit cost  c_j + f_j/M          2 + 200/M = 6 + 60/M at M = 35",
            "M = 30   bound 240 = the answer, 1 node",
            "M = 600  bound 70,  y₁ = 1/20,  5 nodes — same answer, weaker proof",
        ],
        "key_label": "One link, and the price of the constant in it",
        "concepts_intro": (
            "The link itself is one inequality and takes a minute. The lesson is the "
            "constant in it, which is a modelling decision with a measurable price and "
            "no error message."
        ),
        "concepts": [
            ("The link is one inequality, and it works in one direction",
             "`x ≤ M y` with `y` binary. At `y = 0` the row reads `x ≤ 0`, which with "
             "`x ≥ 0` forces `x = 0`: no activity without the decision. At `y = 1` it "
             "reads `x ≤ M`, which is slack provided `M` is large enough. Note what it "
             "does <em>not</em> do: `y = 1` never forces `x` to be positive, so paying a "
             "fixed cost for nothing stays feasible and is simply never optimal."),
            ("Validity has a reason, and the reason gives the tightest M",
             "`M` must permit every `x` the rest of the model allows, so any upper bound "
             "on `x` is valid and the smallest such bound is best. A facility ships no "
             "more than its own capacity and no more than the whole demand, so the "
             "smaller of those two is valid and nothing smaller is. “A million” is not a "
             "reason; “total demand is 30” is."),
            ("Every unit above that is paid for twice",
             "The relaxation does not have to choose `y ∈ {0, 1}`; it sets `y = x/M`, "
             "which is the cheapest value satisfying the row. Its effective unit cost "
             "becomes `c_j + f_j/M`, falling as `M` grows &mdash; so the bound decays "
             "toward the fixed costs being free. On the lab's instance the bound goes "
             "from `240`, which is the answer, to `70`; and the search that must close "
             "that gap goes from one node to five."),
        ],
        "read_title": "A cost paid only if it happens, and the constant that links it",
        "read_intro": "The fixed-charge row, the reason behind a valid M, and the measured cost of a careless one.",
        "body": [
            ("def", ("Fixed charge",
                     "A <strong>fixed charge</strong> is a cost `f` incurred if an "
                     "activity `x` is positive and not otherwise. Modelling it needs a "
                     "binary `y` with `f y` in the objective and the "
                     "<strong>linking constraint</strong> `x ≤ M y`, where `M` is a "
                     "constant at least as large as any feasible value of `x`.")),
            ("p", "The facility-location problem is this device repeated. Facilities have "
                  "opening costs `f_j`, unit shipping costs `c_j` and capacities; demand "
                  "must be met; and the objective is `Σ f_j y_j + Σ c_j x_j`. Without the "
                  "binaries the model would ship a trickle from every facility and pay no "
                  "opening cost at all, which is not what a warehouse costs."),
            ("example", ("Two facilities, thirty units of demand",
                         "Facility 1 costs `200` to open and `2` a unit; facility 2 costs "
                         "`60` to open and `6` a unit. Each can handle `40` units and "
                         "demand is `30`. Opening facility 1 costs `200 + 60 = 260`; "
                         "opening facility 2 costs `60 + 180 = 240`. So the answer is "
                         "`240`, and every figure below is about how well a relaxation "
                         "knows it.")),
            ("p", "The tightest valid `M` here is `30`: no facility can ship more than "
                  "the total demand, whatever its capacity says. At `M = 30` the "
                  "relaxation returns `y₂ = 1` whole, a bound of `240`, and a search tree "
                  "that closes in a single node &mdash; the bound is the answer, so there "
                  "is nothing left to prove."),
            ("h3", "What a loose M buys the relaxation"),
            ("p", "Put `M = 600`, twenty times the tightest, and nothing about "
                  "feasibility changes. The relaxation now ships all thirty units from "
                  "facility 1 and sets `y₁ = 30/600 = 1/20`, paying a twentieth of the "
                  "opening cost: `10 + 60 = 70`. The bound has fallen from `240` to `70` "
                  "while the answer stayed `240`, and the tree needs five nodes instead "
                  "of one to prove it."),
            ("math", ["  M       bound     y₁      nodes      answer",
                      "   30       240       0        1         240",
                      "   60       160     1/2        5         240",
                      "  150       100     1/5        5         240",
                      "  600        70    1/20        5         240",
                      " 1200        65    1/40        5         240"]),
            ("p", "The shape of that column is the algebra: with `y_j = x_j/M` the "
                  "objective contributes `c_j x_j + f_j x_j/M`, so facility `j` has an "
                  "effective unit cost of `c_j + f_j/M`. As `M` grows the fixed cost is "
                  "amortised over a larger and larger notional capacity, and the "
                  "relaxation drifts toward the model in which opening a facility is free."),
            ("p", "That also explains the bend. At small `M`, facility 2 is cheaper per "
                  "unit: `6 + 60/30 = 8` against `2 + 200/30 = 26/3`. The two cross where "
                  "`2 + 200/M = 6 + 60/M`, which is `140/M = 4`, so `M = 35` &mdash; and "
                  "there the bound is exactly `1620/7`. Above that value the relaxation "
                  "prefers to half-open the expensive-to-build, cheap-to-run facility, "
                  "and the bound decays from there without ever coming back."),
            ("p", "Two things are worth separating. A loose `M` does not make the model "
                  "wrong: every value in the table above returns the same integer answer, "
                  "`240`. What it costs is the <em>bound</em>, and therefore the proof and "
                  "the work &mdash; which on a real instance is the difference between a "
                  "tree that closes and one that does not."),
            ("p", "An `M` that is too <em>small</em> is a different and worse failure. It "
                  "is not a weak bound, it is a wrong model: the row `x ≤ M y` then "
                  "forbids shipping quantities the situation permits, and the answer it "
                  "returns is the optimum of a problem nobody asked about. This is why "
                  "the reason matters more than the number: “the facility's capacity” "
                  "cannot be too small, and a value chosen by feel can be."),
        ],
        "lab": ("integer", {
            "mode": "bigm",
            "preset": "two",
            "panel_title": "Make M larger and watch the bound fall away",
            "panel_intro": "The relaxation is re-solved exactly at each value of `M`, the "
                           "breakpoints are solved for and then checked on both sides, "
                           "and the node count comes from the same branch-and-bound "
                           "engine the search lesson uses. The slider starts at the "
                           "tightest valid value, so everything it shows you is a model "
                           "that is still correct.",
        }),
        "steps_title": "Sizing a big-M, with a reason attached",
        "steps_intro": "Five steps, and the second is the one that separates a modelling decision from a habit.",
        "steps": [
            ("Write the fixed cost and the link together",
             "`f y` in the objective and `x ≤ M y` in the rows. One without the other is "
             "either a cost nothing controls or a decision nothing charges for, and both "
             "produce models that solve and mean nothing."),
            ("Name the upper bound on the activity, in words",
             "“This facility's capacity.” “Total demand.” “The largest order any customer "
             "can place.” Then take the smallest of the bounds you can justify. The words "
               "are the deliverable; the number is derived from them."),
            ("Solve the relaxation and read the binaries",
             "A `y` at `1/20` is the relaxation telling you what it bought. Anything "
             "strictly between `0` and `1` means a fixed cost has been charged "
             "fractionally, which is the one thing the binary existed to prevent."),
            ("Measure the loose M against the tight one",
             "Same instance, two values of `M`, two bounds and two node counts. “A loose "
             "`M` is bad practice” is folklore; “on this instance it moved the bound from "
             "`240` to `70` and the tree from one node to five” is an engineering result."),
            ("Keep the reason next to the number",
             "In the model, as a comment or a line of prose. Six months later the only "
             "way to tell a justified `M` from a guess is that the justified one says why, "
             "and the only way to safely tighten one is to know what it was bounding."),
        ],
        "worked": {
            "title": "Two facilities, and the bound at three values of M",
            "intro": [
                "One instance, solved exactly at each `M`. The answer never moves; "
                "everything else does.",
            ],
            "lines": [
                "facility 1    open 200    ship 2 a unit    capacity 40",
                "facility 2    open  60    ship 6 a unit    capacity 40",
                "demand 30",
                "",
                "min  200y₁ + 60y₂ + 2x₁ + 6x₂",
                "      x₁ + x₂ = 30,        x₁ ≤ M y₁,   x₂ ≤ M y₂,   y ∈ {0, 1}",
                "",
                "the integer answer",
                "  open 1 only:  200 + 2(30) = 260",
                "  open 2 only:   60 + 6(30) = 240      ←  the optimum",
                "",
                "tightest valid M = 30, because total demand is 30 and no facility",
                "                  can ship more than that, so 30 is valid and",
                "                  nothing smaller is",
                "",
                "  M = 30    relaxation:  y₂ = 1 whole,  z = 240      1 node",
                "  M = 60    relaxation:  y₁ = 1/2,      z = 160      5 nodes",
                "  M = 600   relaxation:  y₁ = 1/20,     z =  70      5 nodes",
                "",
                "why the bound falls:  y_j = x_j/M, so unit cost is c_j + f_j/M",
                "  facility 1     2 + 200/M        facility 2     6 + 60/M",
                "  equal when  140/M = 4,  i.e.  M = 35,  where the bound is 1620/7",
                "  at M = 600:  2 + 1/3 = 7/3   against   6 + 1/10 = 61/10",
                "  so all 30 units go from facility 1 at 7/3 each = 70",
            ],
            "after": [
                "The first row of that table is the one to want. At the tightest `M` the "
                "relaxation returns a whole `y` and a bound equal to the answer, so the "
                "search closes immediately &mdash; the model did the work that would "
                "otherwise be a tree.",
                "Notice that the node count jumps from one to five as soon as `M` leaves "
                "its tightest value and then stops changing. The bound keeps decaying "
                "smoothly, the work does not: a weaker bound costs nothing until it stops "
                "closing a node, and then it costs a subtree. That is why the price of a "
                "loose `M` has to be measured rather than estimated.",
                "For a faded rehearsal, use the lab's demand slider to raise demand to "
                "`45` and re-derive the tightest valid `M`. The supplied first move is "
                "that total demand is no longer the binding bound &mdash; `45` exceeds "
                "either capacity, so the capacity is now what limits a single facility. "
                "Say what the tightest `M` becomes and why, then check the panel, and "
                "then say whether one facility can still meet demand alone.",
            ],
        },
        "quiz_title": "Links, constants and what they cost",
        "quiz": [
            {"q": "In `x ≤ M y` with `y` binary and `x ≥ 0`, what does `y = 1` force?",
             "a": ["`x = M`", "`x > 0`", "Nothing beyond `x ≤ M`", "`x` to be an integer"],
             "c": 2,
             "why": "The row is one-directional. `y = 0` forces `x = 0`; `y = 1` merely "
                    "leaves the row slack. Paying a fixed cost while shipping nothing "
                    "stays feasible, and the objective is what makes it never optimal."},
            {"q": "A facility with capacity `40` faces total demand `30`. Which value of `M` in `x ≤ M y` is the tightest valid one?",
             "a": ["`30`", "`40`", "`70`", "`1 000 000`"],
             "c": 0,
             "why": "`M` must permit every feasible `x`, and `x` can never exceed the "
                    "total demand of `30` however large the capacity is. `40` and "
                    "`1 000 000` are valid and looser; both weaken the bound, and the "
                    "second weakens it enormously."},
            {"q": "Moving `M` from `30` to `600` on the lab's instance takes the bound from `240` to `70`. What happened to the integer optimum?",
             "a": ["It fell to `70` as well", "It fell, but by less than the bound did",
                   "It stayed at `240`", "It became unbounded"],
             "c": 2,
             "why": "A larger `M` only relaxes a row that was already slack at `y = 1`, "
                    "so no whole plan is added or removed and the answer is untouched. "
                    "What changed is the quality of the proof, and the five nodes needed "
                    "to finish it."},
            {"q": "The relaxation returns `y₁ = 1/20`. What has it done?",
             "a": ["Opened facility 1 and shipped a twentieth of the demand",
                   "Charged a twentieth of facility 1's opening cost while shipping everything from it",
                   "Rounded a binary down, which is always safe",
                   "Reported that facility 1 should be open with probability `1/20`"],
             "c": 1,
             "why": "`y = x/M` is the cheapest value satisfying `x ≤ M y`, so all thirty "
                    "units ship and only `200/20 = 10` of the `200` opening cost is paid. "
                    "There is no probability anywhere in a linear programme, and rounding "
                    "that `y` up to `1` is not a constraint &mdash; it is the first "
                    "lesson's fallacy in a new place."},
        ],
        "mistakes": [
            ("Setting M to a million to be safe",
             "It is safe for feasibility and ruinous for the bound. On the lab's instance "
             "the bound at the tightest `M` is the answer itself; a million takes it "
             "toward `2(30) = 60`, the shipping cost alone with the opening cost "
             "amortised away into nothing, and the tree has to close every unit "
             "practice” but a number: here is the bound I lost and here are the extra "
             "nodes."),
            ("Choosing M by feel rather than by bound",
             "An `M` that happens to be too small does not weaken anything &mdash; it "
             "deletes feasible plans and returns a confident answer to a different "
             "problem. That failure is silent, because the model still solves. A value "
             "derived from a stated upper bound on the activity cannot make this mistake; "
             "a value chosen because it “looks big enough” can."),
            ("Rounding the fractional y up and calling it a solution",
             "Replacing the binary by `x/M` and rounding up is not a constraint at all: "
             "it is a post-processing step with no argument behind it. Whether the "
             "rounded-up plan is feasible, and whether it is anywhere near best, are the "
             "two questions “When Rounding Fails” answered with no and no."),
        ],
        "standard": ("Finish when a big-M in someone else's model is a question you ask, with a number ready to measure the answer.",
                     "You should be able to write a fixed-charge link and say what each "
                     "value of the binary forces, justify the tightest valid `M` from an "
                     "upper bound on the activity, predict which facility a loose `M` "
                     "makes the relaxation half-open, and report the bound and the node "
                     "count at two values of `M` on the same instance."),
        "note": 'Replacing the binary by `x/M` and rounding up is not a constraint at all &mdash; it is the fallacy of &ldquo;When Rounding Fails&rdquo; one level up, applied to a variable that was invented to prevent it. It is named here as that rather than as a separate error, because a reader who has watched `(9/4, 3/2)` fail to round has already been given the argument.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "either-or-constraints-and-disjunctions",
        "title": "Either–Or Constraints",
        "module": "Modelling with binaries",
        "one_line": "Write a disjunction as two relaxed rows switched by one binary, and verify both branches by re-solving.",
        "summary": (
            "“Constraint A or constraint B” cannot be written by writing both, because "
            "writing both is the conjunction &mdash; and on a sequencing pair the "
            "conjunction is infeasible. It is written by relaxing each row with a big-M "
            "term that a single binary switches off, so that one value of the binary "
            "enforces A and makes B vacuous and the other value does the reverse."
        ),
        "key": [
            "A or B      A relaxed by M_A(1 − y)      B relaxed by M_B y",
            "y = 1  enforces A and makes B vacuous;  y = 0  does the reverse",
            "x₁ − x₂ ≤ −4 + 14(1 − y)        −x₁ + x₂ ≤ −3 + 13y",
            "y = 1   start at (0, 4)   cost 4        y = 0   start at (3, 0)   cost 3",
            "y free  →  y = 3/13, both jobs at 0, cost 0 — a bound, not a schedule",
            "both rows at once  →  0 ≤ −7,  infeasible",
        ],
        "key_label": "One binary, two rows, and what each value does to them",
        "concepts_intro": (
            "One hard idea: “or” is not something you can write by writing more "
            "constraints, because constraints accumulate as “and”."
        ),
        "concepts": [
            ("Writing both rows writes the conjunction",
             "Constraints in a model are simultaneous. Adding a row never creates a "
             "choice; it removes plans. So writing A and writing B asks for both, and on "
             "two jobs competing for one machine that asks job one to finish before job "
             "two starts <em>and</em> job two to finish before job one starts. Add the two "
             "rows and you get `0 ≤ −7`."),
            ("A big-M term, switched by one binary, is what or costs",
             "Relax A by `M_A(1 − y)` and B by `M_B y`. At `y = 1` the first term "
             "vanishes and A binds, while B has `M_B` added to its right-hand side and "
             "nothing in the region can break it. At `y = 0` the roles swap. The binary "
             "is not a variable in the problem; it is the choice the problem contains."),
            ("A fractional binary describes nothing",
             "The relaxation may set `y = 3/13`. Both rows are then half-relaxed at once, "
               "both jobs start at time zero on one machine, and the cost is `0` &mdash; "
             "below either real branch, which is what a bound looks like. There is no "
             "schedule here at all: “job one is three-thirteenths before job two” is not "
             "a sentence about machines."),
        ],
        "read_title": "Or, written with one binary and two constants",
        "read_intro": "Why the conjunction is infeasible, what each branch is, and what the relaxation says instead.",
        "body": [
            ("p", "Two jobs share one machine. Job one takes four hours, job two takes "
                  "three, and neither can run while the other is on the machine. Let `x₁` "
                  "and `x₂` be the start times. Either job one finishes before job two "
                  "starts, which is `x₁ + 4 ≤ x₂`, or job two finishes before job one "
                  "starts, which is `x₂ + 3 ≤ x₁`. Exactly one of those must hold."),
            ("def", ("Either-or pair",
                     "Given two rows `A(x) ≤ a` and `B(x) ≤ b` of which at least one must "
                     "hold, the <strong>disjunctive formulation</strong> introduces one "
                     "binary `y` and writes `A(x) ≤ a + M_A(1 − y)` together with "
                     "`B(x) ≤ b + M_B y`, where each `M` is large enough to make its own "
                     "row vacuous over the rest of the feasible region.")),
            ("p", "Written as `≤` rows, the pair above is `x₁ − x₂ ≤ −4` and "
                  "`−x₁ + x₂ ≤ −3`. With deadlines putting both start times in `[0, 10]`, "
                  "the most the first left-hand side can exceed its right-hand side is "
                  "`10 − 0 − (−4) = 14`, so `M_A = 14`; by the mirror argument "
                  "`M_B = 13`. Each constant is the slack its own row needs to become "
                  "harmless, and not one unit more."),
            ("example", ("Both branches, solved",
                         "Minimise `x₁ + x₂`. Fixing `y = 1` enforces “job one first” and "
                         "the model starts the jobs at `(0, 4)`, costing `4`. Fixing "
                         "`y = 0` enforces “job two first” and starts them at `(3, 0)`, "
                         "costing `3`. Both are genuine schedules, the second is cheaper, "
                         "and the integer problem wants the better of exactly these two "
                         "&mdash; which is what the binary means.")),
            ("h3", "What the conjunction does, and what the relaxation does"),
            ("p", "Write both original rows together and add them: the left-hand sides "
                  "cancel to `0` and the right-hand sides give `−7`, so the model asserts "
                  "`0 ≤ −7` and is infeasible. That is the diagnosis to recognise, "
                  "because the symptom is a solver reporting infeasibility on data that "
                  "is perfectly consistent, and the usual response is to go looking for a "
                  "typo in the processing times."),
            ("p", "Now leave `y` continuous. The relaxation sets `y = 3/13`, starts both "
                  "jobs at time zero, and reports `0`. Every row is satisfied: `y` is "
                  "large enough to relax the second row by `3` and small enough to relax "
                  "the first by `4`, so both are half-off at once. The value `0` is a "
                  "perfectly good lower bound on the integer answer of `3`. It is not a "
                  "schedule, and the machine cannot run two jobs at once because a "
                  "variable took a value between `0` and `1`."),
            ("p", "The two constants need not be equal and each must be valid for its own "
                  "row: here `14` and `13`. One `M` used for both, unchecked, is how a "
                  "disjunction quietly becomes an implication &mdash; if the shared value "
                  "is big enough for one row and too small for the other, then one branch "
                  "of the “or” is partially enforced even when the binary says it should "
                  "be off, and the model answers a question with one alternative "
                  "half-deleted."),
            ("p", "The same pair, repeated over every pair of jobs on every machine, is "
                  "what makes a job shop an integer programme rather than a linear one. "
                  "That is why “Scheduling” can prove single-machine rules by exchange "
                  "arguments and still needs this course the moment two jobs contend for "
                  "one resource: the sequencing decision is a binary, and there is no "
                  "linear model of it."),
            ("p", "The device generalises past two alternatives. Three rows of which "
                  "exactly one must hold need three binaries summing to `1`, each "
                  "relaxing its own row by `M(1 − y_k)`; and a two-level capacity &mdash; "
                  "either run at the small size or at the large one &mdash; is the same "
                  "pattern with the two rows being the two capacity limits. What does not "
                  "generalise is guessing the constants: each one is sized against its "
                  "own row, every time."),
        ],
        "lab": ("integer", {
            "mode": "disjunction",
            "preset": "machine",
            "panel_title": "Fix the binary either way, then let it go",
            "panel_intro": "Each branch is solved exactly and drawn as its own region, "
                           "the two regions do not overlap, and the relaxation is solved "
                           "with the binary left continuous so its value can be read for "
                           "what it is. The last setting writes both rows at once, which "
                           "is the mistake.",
        }),
        "steps_title": "Writing a disjunction you can check",
        "steps_intro": "The check at the end is two re-solves rather than eight rows, and it is the same discipline.",
        "steps": [
            ("Write each alternative on its own, as a ≤ row",
             "`x₁ − x₂ ≤ −4` and `−x₁ + x₂ ≤ −3`. Getting both into the same relation "
               "first makes the relaxation term easy to place and makes the sign errors "
             "visible while they are still cheap."),
            ("Decide which alternative y = 1 enforces",
             "Then write `M_A(1 − y)` on that row and `M_B y` on the other. Writing the "
             "convention down is not ceremony: the two rows look alike, and a swapped "
             "pair gives a model that solves and means the opposite."),
            ("Size each M against its own row",
             "The most that row's left-hand side can exceed its right-hand side anywhere "
             "the other constraints allow. Here `14` and `13`, from the deadlines. Two "
             "rows, two constants, two reasons."),
            ("Fix y to each value and re-solve",
             "`y = 1` should give a schedule with job one first; `y = 0` one with job two "
             "first. If either branch is infeasible or describes the wrong order, the "
             "fault is in the signs or in an `M` that is too small, and you have just "
             "found out which."),
            ("Leave y continuous and read what it says",
             "A fractional `y` is the relaxation's bound and it is not a plan. Looking at "
             "it once, and naming the impossible schedule it describes, is what stops it "
             "being reported later as an answer."),
        ],
        "worked": {
            "title": "Two jobs, one machine, and the three things you can write",
            "intro": [
                "One instance, three formulations: the conjunction, the two fixed "
                "branches, and the relaxation. Only the middle one describes a machine.",
            ],
            "lines": [
                "job one takes 4 hours, job two takes 3; one machine; both start by 10",
                "x₁, x₂ = start times,  minimise x₁ + x₂",
                "",
                "the two alternatives, as ≤ rows",
                "  A   job one first    x₁ + 4 ≤ x₂       x₁ − x₂ ≤ −4",
                "  B   job two first    x₂ + 3 ≤ x₁      −x₁ + x₂ ≤ −3",
                "",
                "WRONG: write both",
                "  add them:  (x₁ − x₂) + (−x₁ + x₂) ≤ −4 − 3",
                "                                 0 ≤ −7        infeasible",
                "",
                "RIGHT: one binary, two constants",
                "  M_A = 10 − 0 − (−4) = 14        M_B = 10 − 0 − (−3) = 13",
                "  x₁ − x₂ ≤ −4 + 14(1 − y)       −x₁ + x₂ ≤ −3 + 13y",
                "",
                "  y = 1   A binds:  x₁ − x₂ ≤ −4      B reads −x₁ + x₂ ≤ 10",
                "          optimum (0, 4)             cost 4",
                "  y = 0   B binds: −x₁ + x₂ ≤ −3      A reads  x₁ − x₂ ≤ 10",
                "          optimum (3, 0)             cost 3      ←  the answer",
                "",
                "  y continuous:  y = 3/13",
                "          14(1 − 3/13) = 140/13 ≥ 4   and   13(3/13) = 3 ≥ 3",
                "          so (0, 0) satisfies both rows      cost 0   — a bound",
            ],
            "after": [
                "The `0 ≤ −7` line is the one to memorise, because it is what the model "
                "says rather than what the solver says. A solver reports “infeasible” and "
                "a reader goes looking for bad data; adding the two rows takes ten seconds "
                "and names the real cause, which is that “or” was written as “and”.",
                "The relaxation's `y = 3/13` is worth reading arithmetically once. It is "
                "the smallest `y` that relaxes row B by the three hours it needs; and it "
                "is small enough that row A is still relaxed by `140/13`, comfortably more "
                "than the four hours it needs. Both alternatives are switched most of the "
                "way off at the same time, which is precisely the plan that does not exist.",
                "For a faded rehearsal, use the lab's second instance &mdash; a seven-hour "
                "job against a two-hour one, with the short job weighted twice as heavily "
                "in the objective. The supplied first move is that the tightest constants "
                "are now `19` and `14`, from the same deadline argument. Work out both "
                "branches before opening the quiz and say which order wins, and by how "
                "much.",
            ],
        },
        "quiz_title": "Or, and, and the binary between them",
        "quiz": [
            {"q": "You need “row A or row B” and you write both rows. What have you written?",
             "a": ["The disjunction, since a solver will satisfy whichever it can",
                   "The conjunction: both rows must hold",
                   "Nothing: a model cannot contain two rows on the same variables",
                   "The disjunction, provided the two rows do not overlap"],
             "c": 1,
             "why": "Constraints in a model are simultaneous, so adding rows only removes "
                    "plans. On a sequencing pair the conjunction is infeasible, and adding "
                    "the two rows shows why in one line: `0 ≤ −7`."},
            {"q": "In `A ≤ a + M_A(1 − y)` and `B ≤ b + M_B y`, what does `y = 1` do?",
             "a": ["Enforces A and makes B vacuous", "Enforces B and makes A vacuous",
                   "Enforces both", "Makes both vacuous"],
             "c": 0,
             "why": "At `y = 1` the term `M_A(1 − y)` is zero, so A binds, while B gains "
                    "`M_B` on its right-hand side and cannot be broken anywhere in the "
                    "region. `y = 0` does the reverse, and the two branches are the two "
                    "schedules."},
            {"q": "Both start times lie in `[0, 10]`. What is the tightest valid `M_A` for the row `x₁ − x₂ ≤ −4`?",
             "a": ["`4`", "`10`", "`14`", "`20`"],
             "c": 2,
             "why": "`M_A` must be at least the most the left-hand side can exceed the "
                    "right-hand side anywhere the other constraints allow: `x₁ = 10` with "
                    "`x₂ = 0` gives `10`, and the right-hand side is `−4`, so `14`. `10` "
                    "is too small and would leave part of the row enforced when it should "
                    "be off; `20` is valid and loose."},
            {"q": "The relaxation returns `y = 3/13` with both jobs starting at time zero, costing `0`. What is that `0`?",
             "a": ["The optimal cost, which the integer model will also reach",
                   "A lower bound on the integer optimum of `3`, and not a schedule",
                   "Evidence that the model is infeasible",
                   "The cost of running the two jobs in parallel, which is allowed here"],
             "c": 1,
             "why": "A relaxation minimising over a larger set returns a value at or below "
                    "the integer optimum, so `0 ≤ 3` and `0` is a bound. The point it "
                    "came from has both jobs on one machine at once, which is why it is a "
                    "bound and nothing else."},
        ],
        "mistakes": [
            ("Writing both constraints",
             "It is the conjunction, it forces both alternatives, and on a sequencing pair "
             "it makes the model infeasible. The reason this one is expensive is the "
             "diagnosis: infeasibility on consistent data sends readers looking for a "
             "data error, and the fault is in the formulation."),
            ("Using one M for both rows without checking it",
             "The two rows need not need the same slack &mdash; here `14` and `13`. A "
             "shared value that is valid for one row and short for the other leaves part "
             "of one alternative enforced when the binary says it is off, so the "
             "disjunction has quietly become an implication and the model is answering a "
             "narrower question."),
            ("Reading a fractional y as mostly one order",
             "`y = 3/13` is not “job one goes first about a quarter of the time”, and "
             "there is no probability in a linear programme. It is a point at which both "
             "rows are partly relaxed, describing a schedule that cannot be run. Its "
             "value is a bound; its coordinates are not a plan."),
        ],
        "standard": ("Finish when writing both rows for an either-or reads as a category error rather than a near miss.",
                     "You should be able to write a disjunctive pair with one binary and "
                     "two separately sized constants, say what each value of the binary "
                     "enforces and what it makes vacuous, show in one line why writing "
                     "both rows is infeasible, and read a fractional binary as a bound "
                     "with an impossible plan behind it."),
        "note": 'The two constants need not be equal and each must be valid for its own side; one `M` used for both, unchecked, is how a disjunction quietly becomes an implication. Sequencing two jobs on one machine is exactly this pair of rows, which is why the job shop of &ldquo;Scheduling&rdquo; is an integer programme and its single-machine rules are not &mdash; and this lesson is where that boundary is drawn.',
    },
]
