"""Networks: Flows, Paths and Assignments -- the second half.

The assignment problem and the method that solves it by duality, the one
network on the course with nothing flowing along it, and the three places where
a path, a cut and a matching turn out to be the same theorem.

Every figure below is read off the kits -- scripts/mathpath/labs/network.py and
scripts/mathpath/labs/transport.py -- by executing their shipped JavaScript,
rather than asserted here, and scripts/mathcheck.js executes those same blocks.
Where a design note and a kit disagreed, the kit won.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-assignment-problem",
        "title": "The Assignment Problem",
        "module": "Integer corners",
        "one_line": "Take a constant off every row and every column, count the cover properly, and watch the running total climb to meet the cost of the assignment it finds.",
        "summary": (
            "One worker per job and one job per worker: a transportation problem with every "
            "supply and every demand equal to one, so its corners are the permutations. The "
            "Hungarian method takes constants off rows and columns until the zeros carry a "
            "complete assignment, and the constants it has taken are a dual solution whose "
            "total climbs until it equals the assignment's cost. The one step that is done "
            "properly here is the cover, which is a matching and not a drawing."
        ),
        "key": [
            "n workers, n jobs, cost cᵢⱼ;  choose a permutation minimising Σ cᵢ,σ(i)",
            "taking t off a whole row lowers EVERY assignment by t, so the argmin cannot move",
            "reduce rows, reduce columns, then cover all the zeros with as few lines as possible",
            "smallest cover = largest matching on the zero cells        this is Koenig",
            "cover of size n  ⟺  the zeros carry a complete assignment; fewer means adjust",
            "adjust by θ, the smallest uncovered entry: off the uncovered, onto the twice-covered",
            "the constants taken off are u and v;  Σu + Σv climbs to the assignment's cost",
        ],
        "key_label": "The method, and the dual quantity that says when to stop",
        "concepts_intro": (
            "The reductions are easy to justify and easy to believe. The cover is the step that "
            "is usually taught wrong, and the dual is the reason any of it terminates."
        ),
        "concepts": [
            ("A row constant moves every assignment by the same amount",
             "Every complete assignment uses exactly one cell of each row, so subtracting `t` "
             "from a whole row lowers every assignment's total by exactly `t`. Not by at most "
             "`t`, not by between zero and `t` &mdash; by `t`. The lab measures this rather than "
             "asserting it: on its five-by-five example the two rounds of reductions take off 37 "
             "in total, and all 120 complete assignments are cheaper in the reduced matrix by "
             "the same 37, one number and not a range."),
            ("The cover is a matching, not a drawing",
             "&ldquo;Draw lines through the zeros until you cannot do better&rdquo; has no "
             "stopping rule and no tie-break, and on the lab's own default example it does not "
             "even give an answer: cover whichever line holds the most uncovered zeros and, at "
             "the second cover step, breaking ties towards rows draws four lines while breaking "
             "them towards columns draws three &mdash; same matrix, same rule. The lab computes "
             "a maximum matching on the zero cells instead and reads the cover off it, which is "
             "König's theorem and is why the number is well defined."),
            ("The constants are a dual solution, and they are the stopping test",
             "Row constant `uᵢ`, column constant `vⱼ`; the reduced entries stay non-negative "
             "throughout, which says `uᵢ + vⱼ ≤ cᵢⱼ` everywhere &mdash; dual feasibility. So "
             "`Σuᵢ + Σvⱼ` is a lower bound on every assignment, and it never falls. The method "
             "stops when it equals the cost of an assignment it has actually found, and at that "
             "moment both are optimal."),
        ],
        "read_title": "Reductions, covers and the bound that closes",
        "read_intro": "Why the reductions are legitimate, why the cover has to be computed, and what the running total is.",
        "body": [
            ("def", ("The assignment problem",
                     "Given an `n × n` cost matrix `C`, the <strong>assignment problem</strong> "
                     "is to choose a permutation `σ` of `{1, …, n}` minimising "
                     "`Σᵢ cᵢ,σ(i)` &mdash; one job per worker, one worker per job.",
                     "Written as a linear programme it is the transportation problem with every "
                     "supply and every demand equal to one, so the previous lessons apply "
                     "unchanged; and since its matrix is a node-arc incidence matrix, its "
                     "corners are whole and are exactly the permutations.")),
            ("p", "That last sentence is worth pausing on, because it is what makes the problem "
                  "tractable. There are `n!` permutations &mdash; 24 on a four-by-four table, "
                  "120 on a five-by-five &mdash; and yet the linear relaxation does not need a "
                  "single integrality constraint. The relaxation's corners <em>are</em> the "
                  "permutations, by the determinant argument of &ldquo;Total Unimodularity and Integer Corners&rdquo;."),
            ("thm", ("Reductions do not change the answer",
                     "Subtracting a constant from every entry of a row, or from every entry of "
                     "a column, changes the cost of every complete assignment by that same "
                     "constant. The set of optimal assignments is therefore unchanged, and the "
                     "optimal value of the original problem is the optimal value of the reduced "
                     "one plus the total subtracted.",
                     "The proof is the counting observation: a complete assignment meets each "
                     "row once and each column once, so it picks up each constant exactly once. "
                     "The lab verifies it by brute force on its five-by-five example rather "
                     "than by restating it.")),
            ("math", [
                "       J1   J2   J3   J4      row min",
                "  A    10   19    8   15          8",
                "  B    10   18    7   17          7",
                "  C    13   16    9   14          9",
                "  D    12   19    8   18          8        total off the rows  32",
                "",
                "after the rows           then the column minima  2  7  0  5   (14)",
                "   2  11   0   7                 0   4   0   2",
                "   3  11   0  10        =>       1   4   0   5",
                "   4   7   0   5                 2   0   0   0",
                "   4  11   0  10                 2   4   0   5",
                "",
                "   taken off so far  32 + 14 = 46,  and the answer will be 49",
            ]),
            ("h3", "Counting the cover"),
            ("p", "The reduced matrix above has seven zeros. The question is whether they carry "
                  "a complete assignment &mdash; four zeros, no two in the same row or column "
                  "&mdash; and the answer is that they do not: the largest matching on the zero "
                  "cells has three pairs, so by König's theorem three lines suffice to cover "
                  "every zero, and three is fewer than four. The lab prints both numbers side by "
                  "side at every cover step, because they are always equal and that equality is "
                  "the whole justification for counting lines at all."),
            ("example", ("The step where drawing lines by eye stops working",
                         "After one adjustment the matrix is "
                         "`0 4 1 2 / 0 3 0 4 / 2 0 1 0 / 1 3 0 4`, with six zeros. The minimum "
                         "cover is 3 and it is attained exactly one way: the third row together "
                         "with the first and third columns.",
                         "Apply the usual eye test &mdash; cover whichever row or column holds "
                         "the most still-uncovered zeros, and repeat &mdash; and the answer "
                         "depends on how ties are broken: towards rows it draws four lines, "
                         "towards columns three. Four is `n`, so the reader who broke ties "
                         "towards rows now goes looking for a complete assignment among six "
                         "zeros that cannot supply one. The recipe is not a function of the "
                         "matrix, and that is why this lab does not implement it.")),
            ("p", "When the cover is short of `n`, adjust: let `θ` be the smallest uncovered "
                  "entry, subtract it from every uncovered entry and add it to every entry "
                  "covered twice. Entries covered once are untouched. Nothing becomes negative, "
                  "no existing zero is destroyed, and at least one new zero appears. This is "
                  "again a row-and-column operation in disguise, so the previous theorem still "
                  "applies and the answer still cannot move."),
            ("h3", "The bound, climbing"),
            ("example", ("Two numbers meeting",
                         "Run the method on the four fitters. The constants taken off total 32, "
                         "then 46, then 47, then 49; the adjustments are `θ = 1` and then "
                         "`θ = 2`, and the third cover has four lines. The final zeros carry the "
                         "assignment A to the fourth job, B to the first, C to the second and D "
                         "to the third, costing `15 + 10 + 16 + 8 = 49`.",
                         "The constants recovered as a dual solution are "
                         "`u = (10, 10, 9, 11)` and `v = (0, 7, −3, 5)`, which add to 49 as "
                         "well, and satisfy `uᵢ + vⱼ ≤ cᵢⱼ` in all sixteen cells. A feasible "
                         "dual point and a feasible primal point with the same value: that is "
                         "strong duality, on this instance, and it is the certificate the method "
                         "hands you rather than a claim that it terminated.")),
            ("p", "The dual total never falls &mdash; `32, 46, 46, 47, 47, 49, 49` step by step, "
                  "standing still at the cover steps and rising at the adjustments &mdash; and "
                  "it is dual feasible at every one of them, not only at the end. So the method "
                  "can be stopped early and what you have is still a genuine lower bound, which "
                  "is more than most hand methods offer."),
            ("example", ("Greed, priced",
                         "Take the cheapest cell, strike out its row and column, repeat. On the "
                         "fitters it picks `(B, J3)` at 7, then `(A, J1)` at 10, "
                         "`(C, J4)` at 14 and `(D, J2)` at 19, for 50 &mdash; one more than the "
                         "optimum. On the four crews and four sites it opens at 35 and ends at "
                         "315 against an optimum of 275, forty too much. On the five drivers it "
                         "lands on 38, which is exactly right.",
                         "That third case is the one to remember. Greed produced the optimum and "
                         "produced no reason to believe it, and a right answer with no "
                         "certificate is not a method. The Hungarian run on the same table ends "
                         "with a dual total of 38 beside a primal cost of 38, and that pair is "
                         "the difference.")),
        ],
        "lab": ("transport", {
            "mode": "hungarian",
            "preset": "jobs",
            "panel_title": "One step at a time, with the cover computed rather than drawn",
            "panel_intro": "Every step recomputes from the matrix in the box: the two "
                           "reductions, the maximum matching on the zero cells, the minimum "
                           "cover König's theorem reads off that matching, and the adjustment. "
                           "The row and column constants are added up beside the cost of the "
                           "assignment, so you can watch the bound climb to meet it.",
        }),
        "steps_title": "Running the method, and knowing when to stop",
        "steps_intro": "Two reductions, then a loop of cover-and-adjust. The only step with any judgement in it is the one you should not be exercising judgement on.",
        "steps": [
            ("Take the minimum off every row, then off every column of the result",
             "Order matters only for the arithmetic, not for the outcome. Keep a running total "
             "of everything subtracted; that total is the bound, and forgetting it is how "
             "readers end up with the reduced answer and no way back to the real one."),
            ("Find a maximum matching on the zero cells",
             "Pair rows to columns using zero cells only, no two pairs sharing a row or a "
             "column, as many pairs as you can. On a small table this is a minute's work by "
             "hand, and it is the number the cover is about to equal."),
            ("Read the cover off the matching and compare it with `n`",
             "The minimum cover has exactly as many lines as the matching has pairs. If that is "
             "`n`, the matching is a complete assignment and you have finished. Do not count "
             "lines by eye instead: the eye test has no tie-break and gives different answers on "
             "the same matrix."),
            ("Adjust by the smallest uncovered entry",
             "Subtract `θ` from every uncovered entry, add it to every entry covered by two "
             "lines, leave the singly covered alone. Add `θ × (number of uncovered rows)` worth "
             "of bookkeeping to your running total if you are tracking it by hand &mdash; or "
             "simply re-derive the total from the current constants, which the lab does."),
            ("Stop when the bound equals a real assignment, and say so",
             "The deliverable is a pair of numbers, not one: an assignment costing `z` and row "
             "and column constants adding to `z`. Quote both. That pair is a proof, and it is "
             "checkable in the time it takes to add up `n` numbers twice."),
        ],
        "worked": {
            "title": "Four fitters, four jobs, and the bound closing on 49",
            "intro": [
                "Every matrix below is what the lab holds at that step, and every total is the "
                "row and column constants recovered from it and added up."
            ],
            "lines": [
                "COSTS          10 19  8 15 / 10 18  7 17 / 13 16  9 14 / 12 19  8 18",
                "               24 complete assignments exist",
                "",
                "ROWS off       8, 7, 9, 8                     total taken 32",
                "                2 11  0  7 /  3 11  0 10 /  4  7  0  5 /  4 11  0 10",
                "",
                "COLUMNS off    2, 7, 0, 5                     total taken 46",
                "                0  4  0  2 /  1  4  0  5 /  2  0  0  0 /  2  4  0  5",
                "",
                "COVER          maximum matching on the zeros: 3 pairs",
                "               so the minimum cover is 3 lines, and 3 < 4",
                "",
                "ADJUST         smallest uncovered entry  θ = 1        total 47",
                "                0  4  1  2 /  0  3  0  4 /  2  0  1  0 /  1  3  0  4",
                "",
                "COVER          matching 3, cover 3 (row 3, columns 1 and 3)",
                "               the eye test: 4 lines if ties go to rows, 3 if to columns",
                "",
                "ADJUST         θ = 2                                  total 49",
                "                0  2  1  0 /  0  1  0  2 /  4  0  3  0 /  1  1  0  2",
                "",
                "COVER          matching 4 = n                         STOP",
                "               A-J4  B-J1  C-J2  D-J3",
                "               cost  15 + 10 + 16 + 8 = 49",
                "",
                "THE DUAL       u = (10, 10, 9, 11)   v = (0, 7, -3, 5)",
                "               Σu + Σv = 40 + 9 = 49       and u_i + v_j ≤ c_ij everywhere",
                "               the trace, step by step:  32 46 46 47 47 49 49",
                "",
                "GREED          (B,J3) 7, (A,J1) 10, (C,J4) 14, (D,J2) 19  =  50",
            ],
            "after": [
                "The two 49s are the point of the whole lesson. One is the cost of something you "
                "can do; the other is a bound on everything you could have done; and because "
                "they are equal, neither needs any further argument. Quote both or you have "
                "quoted half a result.",
                "For a rehearsal, run the five drivers and five routes. Greed happens to land on "
                "38, which is optimal, and the method reaches 38 as well &mdash; but watch where "
                "the constants come from: 35 off the rows, 2 off the columns, the cheapest "
                "assignment in the reduced matrix costing 1, and `1 + 37 = 38`. The reduced "
                "matrix still has work left in it, which is why 37 alone was not the answer.",
                "The harder rehearsal: on the four crews and four sites, stop the method at the "
                "second cover step and write down what you have. A dual total of 270 and no "
                "assignment. That is still a real statement &mdash; no assignment on that table "
                "costs less than 270 &mdash; and the optimum turns out to be 275. Being able to "
                "stop early with something true is what dual feasibility at every step buys you.",
            ],
        },
        "quiz_title": "Reductions, covers and the two numbers",
        "quiz": [
            {"q": "Why does subtracting the minimum from every entry of a row leave the optimal assignment unchanged?",
             "a": ["Because the minimum is usually small",
                   "Because every complete assignment uses exactly one cell of that row, so all of them drop by the same amount",
                   "Because the reduced matrix has a zero in that row",
                   "Because the row and column constants cancel later"],
             "c": 1,
             "why": "One cell per row, always, so each assignment picks the constant up exactly "
                    "once and the whole set of totals shifts rigidly. The lab measures this on "
                    "its five-by-five table: all 120 complete assignments are cheaper in the "
                    "reduced matrix by exactly 37, one number rather than a spread, which is "
                    "what makes the argmin immovable."},
            {"q": "On a four-by-four reduced matrix, the maximum matching on the zero cells has three pairs. What does that tell you?",
             "a": ["Three lines cover every zero, and no complete assignment of zeros exists yet",
                   "Four lines are needed, since one row has no zero in it",
                   "The problem is infeasible",
                   "The current reduction is optimal and the method should stop"],
             "c": 0,
             "why": "König's theorem: on the bipartite graph of zero cells the minimum vertex "
                    "cover and the maximum matching have the same size. Three pairs therefore "
                    "means three lines, and three is short of four, so the zeros cannot carry a "
                    "complete assignment and an adjustment is needed. The lab prints the "
                    "matching and the cover together at every cover step for exactly this "
                    "reason."},
            {"q": "You cover the zeros by eye — always covering the line with the most uncovered zeros — and get four lines on a four-by-four table. What can you conclude?",
             "a": ["That the zeros carry a complete assignment",
                   "That the minimum cover is four",
                   "Nothing: the recipe has no tie-break and can give four where the minimum is three",
                   "That the matrix needs one more adjustment"],
             "c": 2,
             "why": "On the lab's own default table, at the second cover step, that recipe gives "
                    "four lines if ties go to rows and three if they go to columns, on the same "
                    "matrix. The minimum really is three and the maximum matching is three, so a "
                    "reader who stopped at four would search for a complete assignment among "
                    "zeros that cannot supply one. Compute the matching; do not draw."},
            {"q": "A Hungarian run ends with row and column constants adding to 49 and an assignment costing 49. What has been proved?",
             "a": ["Only that the method terminated",
                   "That 49 is optimal, since a feasible dual value bounds every assignment from below",
                   "That 49 is optimal, provided the cost matrix has no ties",
                   "That 49 is within one unit of the optimum"],
             "c": 1,
             "why": "The constants satisfy `uᵢ + vⱼ ≤ cᵢⱼ` in every cell, so `Σu + Σv` is a lower "
                    "bound on the cost of any assignment whatever; and 49 is achieved. A bound "
                    "of 49 and an achievement of 49 leave no room. Ties are irrelevant &mdash; "
                    "one of the lab's tables has two optimal assignments and the value is still "
                    "the thing that is proved."},
        ],
        "mistakes": [
            ("Drawing lines until you cannot obviously do better",
             "There is no stopping proof behind that, and the number it produces is not "
             "determined by the matrix: on the lab's default table the same rule gives three or "
             "four lines depending on an arbitrary tie-break. Compute a maximum matching on the "
             "zero cells; the cover is its size, by König, and that number is unambiguous."),
            ("Reporting the reduced matrix's answer",
             "The reduced optimum on the five-driver table is 1, and 1 is not the answer; 38 is. "
             "Everything subtracted has to be added back. Keeping a running total as you go is "
             "the habit, and it has the side benefit that the running total is the bound you "
             "will eventually quote as the certificate."),
            ("Treating the assignment as the deliverable",
             "A permutation on its own is a proposal. Two of the lab's three tables have an "
             "optimal value attained by more than one permutation, and on one of them greed "
             "reaches the optimal value with no way of knowing it has. What is optimal is the "
             "value, what proves it is the dual total, and both belong in the answer."),
        ],
        "standard": ("Finish when you can run the method by hand and hand back an assignment and a matching dual total.",
                     "You should be able to justify the reductions by the one-cell-per-row "
                     "argument, find a maximum matching on the zero cells and read the cover off "
                     "it, adjust by the smallest uncovered entry, keep the running total, and "
                     "state the pair of equal numbers that ends the method."),
        "note": 'The cover step is where this lesson earns its place: König&rsquo;s theorem is doing real work, and it is the same theorem that comes back at the end of this course as Hall&rsquo;s condition read off a minimum cut. &ldquo;Project Networks and the Critical Path&rdquo; leaves flow behind entirely. A project network has arcs and nodes and a longest path, and nothing moves along any of it &mdash; which turns out to change what the certificate looks like without changing that there is one.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "project-networks-and-the-critical-path",
        "title": "Project Networks and the Critical Path",
        "module": "Time instead of flow",
        "one_line": "Two passes over an acyclic network give every activity's earliest and latest times, and the zero-slack chain is what actually holds the finish date.",
        "summary": (
            "A project is a network whose arcs carry precedence and whose nodes carry durations, "
            "and nothing flows along it at all. A forward pass gives the earliest each activity "
            "can start, a backward pass the latest it can start without delaying the project, "
            "and the difference is slack. The activities with none form the critical path "
            "&mdash; and shortening one of them stops paying the moment a second path draws "
            "level."
        ),
        "key": [
            "ES(i) = max over predecessors p of EF(p),      EF(i) = ES(i) + duration(i)",
            "LF(i) = min over successors s of LS(s),        LS(i) = LF(i) − duration(i)",
            "slack(i) = LS(i) − ES(i) = LF(i) − EF(i)       zero slack ⟹ critical",
            "project length = max EF = the LONGEST path through the precedence network",
            "a cycle in the precedence graph means no order exists, so nothing is computable",
            "shortening a critical activity pays until a second path becomes critical too",
        ],
        "key_label": "Two passes, one subtraction, and where the return stops",
        "concepts_intro": (
            "The arithmetic is two sweeps and is over in a minute. The three ideas are about "
            "what the numbers mean and what they stop meaning as soon as you act on them."
        ),
        "concepts": [
            ("The project length is a longest path, not a sum",
             "Adding the durations up gives the time to do everything one at a time, which is "
             "not the question. The finish date is the longest chain of activities that must "
             "happen in order, and the forward pass computes it by taking a maximum at every "
             "node. On the lab's nine-activity project the durations add to 21 and the project "
             "takes 12."),
            ("Slack belongs to the activity; criticality belongs to the path",
             "An activity with slack can start late without moving the finish date. But the "
             "slack is not private: two activities on the same non-critical chain share it, and "
             "spending it on one leaves none for the other. That is why the useful object is the "
             "critical path rather than the list of critical activities &mdash; and why the lab "
             "counts distinct critical paths rather than just naming zero-slack activities."),
            ("Shortening pays until something else becomes binding",
             "Take a day off a critical activity and the project shortens by a day &mdash; once. "
             "Then some other chain, previously a day shorter, is the same length, and the next "
             "day off buys nothing at all. The lab draws the whole curve, and the interesting "
             "number on it is where it goes flat rather than its first step."),
        ],
        "read_title": "Two passes, and what happens when you act on them",
        "read_intro": "The definitions, the two sweeps in full on a nine-activity project, then slack, then the crash curve and the case where the first day already buys nothing.",
        "body": [
            ("def", ("A project network and its four times",
                     "A <strong>project</strong> is a set of activities, each with a duration "
                     "and a list of predecessors that must finish before it starts. For each "
                     "activity: `ES` is the <strong>earliest start</strong>, `EF = ES + d` the "
                     "earliest finish, `LF` the <strong>latest finish</strong> that does not "
                     "delay the project, and `LS = LF − d` the latest start.",
                     "The <strong>slack</strong> of an activity is `LS − ES`, equivalently "
                     "`LF − EF`. An activity with zero slack is <strong>critical</strong>: any "
                     "delay to it delays the whole project.")),
            ("p", "Nothing flows here. The arcs are precedence, the numbers on the nodes are "
                  "times, and the quantity being computed is a longest path rather than a "
                  "cheapest one. It is on this course because it is a network with a duality "
                  "reading of its own: the critical path is the certificate that the project "
                  "cannot be finished sooner, in the same way that a cut certifies a flow."),
            ("math", [
                "A 3 | B 2 after A | C 4 after A | G 5 after A | D 2 after B",
                "E 3 after C | H 2 after G | F 1 after D E | I 1 after F H",
                "",
                "forward pass          ES    EF          backward pass    LS    LF",
                "   A                   0     3                           0     3",
                "   B                   3     5                           6     8",
                "   C                   3     7                           3     7",
                "   G                   3     8                           4     9",
                "   D                   5     7                           8    10",
                "   E                   7    10                           7    10",
                "   H                   8    10                           9    11",
                "   F                  10    11                          10    11",
                "   I                  11    12                          11    12",
                "",
                "slack = LS - ES       A 0   B 3   C 0   G 1   D 3",
                "                      E 0   H 1   F 0   I 0",
                "",
                "project length 12     durations add to 21",
                "critical A C E F I    one critical path",
            ]),
            ("p", "Read the forward pass off the predecessors: `F` waits for both `D` and `E`, "
                  "which finish at 7 and 10, so `F` starts at 10 and not at 7. The maximum is "
                  "the whole of the rule. The backward pass is the mirror image: `G` is followed "
                  "only by `H`, which must start by 9, so `G` must finish by 9 &mdash; and since "
                  "`G` can finish at 8, it has a unit of slack."),
            ("h3", "Acting on it, and the point where it stops paying"),
            ("example", ("One day off C, and then nothing",
                         "`C` is critical, so shortening it by one takes the project from 12 to "
                         "11. Shorten it by two, three or four and the project stays at 11. The "
                         "lab draws the curve `12, 11, 11, 11, 11` and reports that the return "
                         "stopped after one unit.",
                         "The reason is on the screen at the moment it happens: with one day off "
                         "`C` the project has two critical paths rather than one, and past that "
                         "the length is held by `A, G, H, I` &mdash; a chain that `C` is not on. "
                         "Every further day taken off `C` is spent on an activity that no longer "
                         "controls the finish date.")),
            ("p", "This is the single most useful thing the method produces and it is not the "
                  "critical path itself. Knowing which activity to shorten is easy; knowing when "
                  "to stop shortening it, and which chain has become binding instead, is what "
                  "keeps a schedule from absorbing money for nothing. The lab reports the slack "
                  "of the chosen activity, what shortening it is worth, and after how many units "
                  "it stops paying."),
            ("example", ("A project where the first day already buys nothing",
                         "Six activities: `A` for 3, then two chains of two activities each, "
                         "joining at `F`. Both chains take the same time, so the project length "
                         "is 8 and every activity is critical &mdash; two distinct critical "
                         "paths, `A B D F` and `A C E F`.",
                         "Shorten `B` by one and the project is still 8, because `A C E F` is "
                         "untouched and still takes 8. The return stops after zero units. With "
                         "parallel critical paths, shortening one activity is not enough; you "
                         "have to shorten one on each path, or shorten a shared activity like "
                         "`A` or `F`.")),
            ("h3", "When there is nothing to compute"),
            ("p", "The forward pass needs an order in which every predecessor comes before its "
                  "activity, and such an order exists exactly when the precedence graph has no "
                  "cycle. Write `A` after `C`, `B` after `A`, `C` after `B` and there is no "
                  "order at all: each of the three is waiting for one of the others. The lab "
                  "names the loop rather than reporting a length, because &ldquo;the project "
                  "takes zero&rdquo; would be a lie and &ldquo;error&rdquo; would not say what "
                  "to fix."),
            ("p", "Two smaller refusals are worth the same treatment. An activity waiting on "
                  "something that is not in the project is refused by name, and so are two "
                  "activities sharing a name. Both are typing errors, and both would otherwise "
                  "produce a schedule that looks complete."),
            ("p", "What this lesson does not do is cost anything. Real project crashing trades "
                  "money for time, with a cost per day for each activity and a budget, and that "
                  "is a linear programme of its own &mdash; a perfectly good one, and not this "
                  "course's. What is here is the structural half: which activities can be "
                  "shortened usefully at all, and for how long."),
        ],
        "lab": ("network", {
            "mode": "cpm",
            "preset": "nine",
            "panel_title": "Type a project, then shorten something and watch the return stop",
            "panel_intro": "The four times and the slack for every activity, every distinct "
                           "critical path rather than just the list of critical activities, and "
                           "a crash control that shortens one activity by up to six units and "
                           "reports the project length at each step. The step at which a second "
                           "path becomes critical is the step where the return stops.",
        }),
        "steps_title": "Scheduling a project and deciding what to shorten",
        "steps_intro": "Order first, then forward, then backward, then subtract. Only after all four does any decision get made.",
        "steps": [
            ("Put the activities in an order with every predecessor first",
             "If you cannot, the precedence graph has a cycle and there is nothing to compute. "
             "Find the loop and fix the data; no amount of care with the arithmetic will help."),
            ("Forward pass: `ES` is the largest `EF` among the predecessors",
             "Start at zero for activities with none. Take the maximum, not the sum and not the "
             "most recent; an activity waiting on three others waits for the last of them. The "
             "largest `EF` in the project is its length."),
            ("Backward pass: `LF` is the smallest `LS` among the successors",
             "Start at the project length for activities with none. Take the minimum: an "
             "activity feeding three others must be done in time for the earliest of them."),
            ("Subtract, and list the critical activities and the critical paths",
             "`slack = LS − ES`. Zero means critical. Then chain the critical activities "
             "together into paths &mdash; there may be more than one, and how many there are is "
             "what decides whether shortening any single activity is worth anything."),
            ("Shorten a critical activity one unit at a time, re-running both passes",
             "Do not assume the saving continues. Re-run the passes after each unit and watch "
             "for a second path reaching the same length; that is the moment the return stops, "
             "and it is usually much sooner than expected."),
        ],
        "worked": {
            "title": "Nine activities, twelve days, and one day's worth of improvement",
            "intro": [
                "The whole schedule, then what happens when the obvious activity is shortened. "
                "Every figure is what the lab reports as the crash control is moved."
            ],
            "lines": [
                "PROJECT   A 3 | B 2 after A | C 4 after A | G 5 after A | D 2 after B",
                "          E 3 after C | H 2 after G | F 1 after D E | I 1 after F H",
                "",
                "             ES   EF   LS   LF   slack",
                "   A          0    3    0    3     0     critical",
                "   B          3    5    6    8     3",
                "   C          3    7    3    7     0     critical",
                "   G          3    8    4    9     1",
                "   D          5    7    8   10     3",
                "   E          7   10    7   10     0     critical",
                "   H          8   10    9   11     1",
                "   F         10   11   10   11     0     critical",
                "   I         11   12   11   12     0     critical",
                "",
                "   length 12,  one critical path  A C E F I",
                "   durations add to 21, which is not the answer to anything here",
                "",
                "SHORTEN C    by 0   1   2   3   4",
                "   length      12  11  11  11  11",
                "   paths        1   2   1   1   1",
                "   critical   ACEFI | ACGEHFI | AGHI | AGHI | AGHI",
                "",
                "   the return stops after ONE unit",
                "   at that unit a second path draws level; past it, A G H I holds the",
                "   length and C is not on it",
                "",
                "   G has one unit of slack, so shortening G is worth nothing at all",
                "   until that unit has been used up somewhere",
                "",
                "TWO PATHS FROM THE START   A 3 | B 2, C 2 after A | D 2 after B,",
                "                           E 2 after C | F 1 after D E",
                "   length 8, every activity critical, TWO paths  A B D F and A C E F",
                "   shorten B by one:  still 8.  The return stops after ZERO units.",
            ],
            "after": [
                "The row of path counts is the row to read. It goes from one to two and back to "
                "one, and the two is where the improvement ended: a second chain reached the "
                "same length, and one more day off `C` left that chain untouched.",
                "For a rehearsal, shorten `G` instead. It has a unit of slack, so the first day "
                "buys nothing; the second and third then start to matter, because by then the "
                "chain through `G` has become the binding one. Slack is a budget that has to be "
                "spent before anything else happens.",
                "The harder rehearsal: on the two-path project, shorten `F` &mdash; the activity "
                "both chains pass through. One day off `F` takes the project from 8 to 7, "
                "because both paths shorten together. A shared activity is worth more than a "
                "private one, and the crash curve is where that becomes a number rather than an "
                "intuition.",
            ],
        },
        "quiz_title": "Passes, slack and what shortening buys",
        "quiz": [
            {"q": "An activity waits for three predecessors, finishing at times 4, 7 and 5. What is its earliest start?",
             "a": ["4, the earliest of them", "16, their total", "7, the latest of them", "5, the middle one"],
             "c": 2,
             "why": "All three must be complete, so the activity waits for the last. The forward "
                    "pass is a maximum at every node, and that is exactly what makes the project "
                    "length a longest path. On the lab's project, `F` waits for `D` at 7 and `E` "
                    "at 10 and starts at 10."},
            {"q": "The activities of a project have durations adding to 21, and the project takes 12. What explains the difference?",
             "a": ["Nine days of the work are unnecessary",
                   "The project length is the longest chain of activities that must run in order, and independent chains run at the same time",
                   "The backward pass has subtracted the slack",
                   "Some activity has been counted twice"],
             "c": 1,
             "why": "Independent chains run concurrently, so the finish date is set by the "
                    "longest chain and not by the total work. On the lab's project the critical "
                    "chain is `A C E F I` at `3 + 4 + 3 + 1 + 1 = 12`, while `B`, `D`, `G` and "
                    "`H` run alongside it."},
            {"q": "You shorten a critical activity by one unit and the project shortens by one. What should you expect from the second unit?",
             "a": ["Another unit of saving, since the activity is still critical",
                   "Nothing, because a critical activity can only be shortened once",
                   "Possibly nothing: another path may now be the same length, and the lab's example is exactly that case",
                   "Two units of saving, because the effect compounds"],
             "c": 2,
             "why": "Shortening changes which chain is binding. On the lab's project, one unit "
                    "off `C` takes it from 12 to 11 and creates a second critical path; from "
                    "then on the length is held by `A G H I`, which `C` is not on, and further "
                    "units buy nothing. Re-run both passes after each unit rather than assuming "
                    "the saving continues."},
            {"q": "A project's precedence data says `A` waits for `C`, `B` waits for `A`, and `C` waits for `B`. What does the method report?",
             "a": ["A project length of zero",
                   "That no order exists, naming the loop, because the forward pass needs an acyclic graph",
                   "The longest of the three durations",
                   "A critical path containing all three"],
             "c": 1,
             "why": "The forward pass needs every predecessor computed before its activity, "
                    "which is possible exactly when the precedence graph is acyclic. With a loop "
                    "there is no such order and nothing to compute. The lab names the three "
                    "activities in the loop, because a reader has to know which precedence to "
                    "delete, and any number reported instead would be a lie."},
        ],
        "mistakes": [
            ("Adding the durations up",
             "That is the time to do the project with one worker and no concurrency, and it is "
             "usually far larger than the answer &mdash; 21 against 12 on the lab's example. The "
             "forward pass takes a maximum at every node precisely because independent chains "
             "run at the same time."),
            ("Treating slack as private to an activity",
             "Two activities on the same non-critical chain share their slack: use it on the "
             "first and the second has none left. The list of critical activities does not "
             "capture this and the list of critical paths does, which is why the lab reports the "
             "paths and counts them."),
            ("Assuming a critical activity is worth shortening indefinitely",
             "The saving lasts exactly until a second chain draws level, which on the lab's "
             "project is after a single unit and on its two-path project is immediately. Money "
             "spent past that point buys nothing, and nothing in the schedule says so unless you "
             "re-run the passes and look at how many paths are critical."),
        ],
        "standard": ("Finish when you can schedule a project by hand and say how much shortening any given activity is worth.",
                     "You should be able to order the activities, run both passes taking a "
                     "maximum forwards and a minimum backwards, compute slack, list the distinct "
                     "critical paths rather than just the critical activities, and find the "
                     "point at which shortening a chosen activity stops reducing the project "
                     "length."),
        "note": 'The critical path is a certificate: it is a chain of activities that must run in order and takes as long as the project does, so no schedule can finish sooner, and anyone can check it by adding up five numbers. That is the same shape of argument as a cut bounding a flow, and the rest of this course is about making that resemblance precise. &ldquo;Shortest Paths and Node Potentials&rdquo; starts with the simplest case, where the certificate is one number attached to each node.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "shortest-paths-and-node-potentials",
        "title": "Shortest Paths and Node Potentials",
        "module": "Paths, cuts and matchings",
        "one_line": "The distance labels are a feasible dual solution, adding a constant to all of them changes nothing, and a negative cycle is dual infeasibility.",
        "summary": (
            "Relax every arc, as many rounds as there are nodes, and the labels settle. What "
            "they settle on is not just a list of distances: it is a feasible solution of the "
            "dual programme, `πⱼ − πᵢ ≤ cᵢⱼ` on every arc, and the tight arcs are the shortest "
            "routes. Because every constraint is a difference, adding a constant to every label "
            "changes nothing &mdash; which is what makes them prices. A negative cycle is the "
            "dual saying it has no feasible point at all."
        ),
        "key": [
            "primal    min Σ cᵢⱼ xᵢⱼ   with one unit supplied at s and one demanded at t",
            "dual      max πₜ − πₛ     subject to  πⱼ − πᵢ ≤ cᵢⱼ  on every arc",
            "relax arc (i,j):   if πᵢ + cᵢⱼ < πⱼ  then  πⱼ := πᵢ + cᵢⱼ",
            "tight arc:  πⱼ − πᵢ = cᵢⱼ      the tight arcs carry the shortest routes",
            "every constraint is a DIFFERENCE, so π and π + k are equally feasible",
            "an improvement in round n certifies a negative cycle: no potentials exist",
        ],
        "key_label": "The two programmes, the relaxation, and the two things a shift cannot change",
        "concepts_intro": (
            "The algorithm takes three lines. What it computes takes a lesson, because the "
            "labels are the dual and readers meet them as distances."
        ),
        "concepts": [
            ("A label is a price, and the whole vector floats",
             "The dual constraint `πⱼ − πᵢ ≤ cᵢⱼ` involves only the difference of two labels, and "
             "so does the objective `πₜ − πₛ`. Add seven to every label and every constraint "
             "still holds and the objective is unchanged: the lab has a control that does "
             "exactly this and reports both facts. A distance from the source is one particular "
             "normalisation of a potential, chosen by setting `πₛ = 0`."),
            ("Tightness is complementary slackness",
             "An arc with `πⱼ − πᵢ = cᵢⱼ` is tight. Complementary slackness says that flow can "
             "only travel on tight arcs, and that is exactly the statement that the shortest "
             "route uses tight arcs and no others. The lab draws the tight arcs heavily, so the "
             "shortest-path tree is visible as the subgraph where the dual constraint holds with "
             "equality."),
            ("A negative cycle is infeasibility, not a bug",
             "Add the constraints round a cycle: the labels cancel completely and what is left "
             "is `0 ≤ (the cycle's total cost)`. A cycle of negative total cost therefore makes "
             "the dual infeasible, and by duality the primal is unbounded &mdash; go round the "
             "cycle forever and the cost falls forever. The relaxation detects it by still "
             "improving in a round it should not, and the lab names the cycle and prints what it "
             "costs."),
        ],
        "read_title": "What the labels are, and what a negative cycle says",
        "read_intro": "The dual first, then the relaxation that finds a feasible point of it, then the shift, then the case with no feasible point at all.",
        "body": [
            ("p", "The shortest-path problem is already on this course: one unit supplied at the "
                  "source, one demanded at the sink, and the costs read as lengths. What is new "
                  "here is its dual, which is worth writing down because the labels every "
                  "shortest-path algorithm computes turn out to be a feasible point of it."),
            ("def", ("Node potentials",
                     "A vector `π`, one number per node, is <strong>feasible</strong> for the "
                     "shortest-path dual when `πⱼ − πᵢ ≤ cᵢⱼ` for every arc from `i` to `j`. The "
                     "dual problem is to maximise `πₜ − πₛ` over all such vectors.",
                     "An arc is <strong>tight</strong> when the inequality holds with equality. "
                     "The <strong>reduced cost</strong> of an arc is `cᵢⱼ − (πⱼ − πᵢ)`, which is "
                     "non-negative exactly when `π` is feasible.")),
            ("p", "The constraint says something plain: the price at the head may exceed the "
                  "price at the tail by at most the cost of getting there. Any feasible `π` "
                  "therefore has `πₜ − πₛ` at most the cost of every path from source to sink "
                  "&mdash; add the constraints along the path and the intermediate terms cancel "
                  "&mdash; so the dual objective is a lower bound on the shortest path. That is "
                  "weak duality, in one line, with no machinery."),
            ("math", [
                "arcs     s>a 4     s>b 2     b>a 1     a>t 3     b>t 7",
                "",
                "relaxation, one round = one pass over the arcs in the order typed",
                "",
                "   round 0     s 0    a  -    b  -    t  -",
                "   round 1     s 0    a  3    b  2    t  6",
                "   round 2     s 0    a  3    b  2    t  6      nothing moved, stop",
                "",
                "check every arc:   c - (pi_j - pi_i)",
                "",
                "   s>a   4 - (3 - 0) = 1     slack",
                "   s>b   2 - (2 - 0) = 0     TIGHT",
                "   b>a   1 - (3 - 2) = 0     TIGHT",
                "   a>t   3 - (6 - 3) = 0     TIGHT",
                "   b>t   7 - (6 - 2) = 1     slack",
                "",
                "dual objective  pi_t - pi_s = 6 - 0 = 6",
                "the tight arcs are exactly the route  s, b, a, t,  which costs 6",
            ]),
            ("p", "Two things about that table are worth noticing. The first is that `a` ends at "
                  "3 rather than 4: the direct arc costs 4 and the route through `b` costs "
                  "`2 + 1 = 3`, so the direct arc ends up slack. The second is that one pass "
                  "over the arcs was enough, because the order they were typed in happened to "
                  "relax them usefully; the second round is what proves it, by changing nothing."),
            ("h3", "The shift, and why the labels are prices"),
            ("example", ("Add seven to everything",
                         "Take the labels `0, 3, 2, 6` and add 7 to each, giving `7, 10, 9, 13`. "
                         "Every arc constraint still holds &mdash; each is a difference, and the "
                         "seven cancels &mdash; and the dual objective is still "
                         "`13 − 7 = 6`. The same tight arcs are still tight.",
                         "Now add 5 to one label only. The lab reports the arcs that are "
                         "violated, in red. This is the contrast that makes the point: the "
                         "vector floats as a whole and does not float component by component, "
                         "which is precisely the behaviour of a price.")),
            ("p", "This is why the lesson is called potentials rather than distances. Calling "
                  "them distances is not wrong &mdash; the normalisation `πₛ = 0` makes each "
                  "label the distance from the source &mdash; but it hides the fact that the "
                  "object is determined only up to a constant, and it makes the next two courses "
                  "harder than they need to be, where the same potentials are used to reprice a "
                  "network without changing which route is cheapest."),
            ("example", ("A negative arc is fine",
                         "`s>a 4, s>b 2, a>b −3, b>t 2, a>t 6` has a negative cost on it, and "
                         "the labels settle at `0, 4, 1, 3` with `s>a`, `a>b` and `b>t` tight. "
                         "The cheapest way to `b` is through `a` at `4 − 3 = 1`, not the direct "
                         "arc at 2.",
                         "So a negative cost is not a problem in itself &mdash; it is perfectly "
                         "meaningful when an arc earns rather than spends. What cannot be "
                         "tolerated is a <em>cycle</em> whose total is negative, which is a "
                         "different thing entirely.")),
            ("h3", "When no potentials exist"),
            ("example", ("Three arcs and no feasible dual point",
                         "`x>y 1, y>z −3, z>x 1, x>z 5`. Add the dual constraints round the "
                         "cycle `x, y, z, x`: the labels cancel and what is left is "
                         "`0 ≤ 1 + (−3) + 1 = −1`. No vector `π` can satisfy all three, so the "
                         "dual is infeasible.",
                         "The relaxation finds this by still improving when it should have "
                         "stopped: the labels go `0, ∞, ∞` then `−1, 1, −2` then `−2, 0, −3` "
                         "then `−3, −1, −4`, one unit lower every round and never settling. The "
                         "lab names the cycle `y, z, x` and reports that it costs `−1`.")),
            ("p", "The word for this on the primal side is unbounded: send a unit round that "
                  "cycle as many times as you like and the cost falls without limit. An "
                  "unbounded primal and an infeasible dual are the pair the duality course "
                  "described, and here they arrive as a picture you can point at."),
            ("p", "One thing deliberately absent from this page is a second algorithm. "
                  "Dijkstra's algorithm computes the same labels faster on non-negative costs, "
                  "it belongs to Discrete Mathematics' &ldquo;Shortest Paths and Dijkstra's "
                  "Algorithm&rdquo;, and putting it beside this one would invite the question "
                  "&ldquo;which is better&rdquo; when the question here is &ldquo;what are these "
                  "numbers&rdquo;. They are a dual solution. That is the lesson."),
        ],
        "lab": ("network", {
            "mode": "bellmanford",
            "preset": "prices",
            "panel_title": "Relax the arcs, then check the prices",
            "panel_intro": "Every round of labels is tabulated, every arc is checked against "
                           "`πⱼ − πᵢ ≤ cᵢⱼ` and coloured tight, slack or violated, and a shift "
                           "control adds a constant to every potential at once. Watch the "
                           "potentials all move and not one reduced cost change &mdash; and then "
                           "open the instance with a negative cycle, where nothing settles at "
                           "all.",
        }),
        "steps_title": "Finding the potentials, and checking somebody else's",
        "steps_intro": "Checking is much cheaper than finding, and this is the lesson where that gap is widest.",
        "steps": [
            ("Set the source to zero and everything else to infinity",
             "Zero is a normalisation. Any other value for the source works and shifts every "
             "label by the same amount, which the lab will show you; zero is chosen because it "
             "makes the labels read as distances."),
            ("Relax every arc, and repeat until a round changes nothing",
             "Relaxing arc `(i, j)` means: if `πᵢ + cᵢⱼ` is less than `πⱼ`, lower `πⱼ` to it. A "
             "round that changes nothing is the stopping condition and the proof of feasibility "
             "at once."),
            ("If a round still improves after as many rounds as there are nodes, stop and find the cycle",
             "There is a negative cycle, the dual is infeasible and the primal unbounded. Report "
             "the cycle and what it costs; no set of labels exists to report instead."),
            ("Check the result arc by arc",
             "`πⱼ − πᵢ ≤ cᵢⱼ` on every arc, not just the ones on the route you expect. This is "
             "one subtraction per arc and it is the whole verification &mdash; a feasible `π` is "
             "a certificate that no path is shorter than `πₜ − πₛ`."),
            ("Read the route off the tight arcs",
             "The arcs where the inequality is an equality carry the shortest paths. If more "
             "than one tight route reaches the sink, there is more than one shortest path, and "
             "that is information rather than ambiguity."),
        ],
        "worked": {
            "title": "Three networks: one ordinary, one with a negative arc, one with no answer",
            "intro": [
                "Each block is the labels the relaxation settles on, the arc-by-arc check, and "
                "the dual objective. All three are what the lab reports."
            ],
            "lines": [
                "NETWORK 1     s>a 4   s>b 2   b>a 1   a>t 3   b>t 7",
                "   round 0    0   -   -   -",
                "   round 1    0   3   2   6",
                "   round 2    0   3   2   6        settled",
                "   tight      s>b, b>a, a>t        3 of 5 arcs",
                "   dual       pi_t - pi_s = 6      and the route s,b,a,t costs 6",
                "   shift +7   7  10   9  13        every arc still satisfied",
                "              dual 13 - 7 = 6      unchanged",
                "   shift one label by +5 instead:  arcs violated, and the lab says which",
                "",
                "NETWORK 2     s>a 4   s>b 2   a>b -3   b>t 2   a>t 6",
                "   round 1    0   4   1   3",
                "   round 2    0   4   1   3        settled",
                "   tight      s>a, a>b, b>t",
                "   dual       3.  Note b is reached at 1 THROUGH a, not at 2 direct",
                "   a negative ARC is fine",
                "",
                "NETWORK 3     x>y 1   y>z -3   z>x 1   x>z 5",
                "   round 0    0    -    -",
                "   round 1   -1    1   -2",
                "   round 2   -2    0   -3",
                "   round 3   -3   -1   -4          still falling",
                "   the cycle  y, z, x   costs  -3 + 1 + 1 = -1",
                "   adding the three dual constraints round it gives  0 ≤ -1",
                "   so the dual is INFEASIBLE and the primal UNBOUNDED",
            ],
            "after": [
                "Network 1 settles after a single pass because the arcs happen to have been "
                "typed in a helpful order; the second round is not wasted, it is the proof. "
                "Reorder the arcs in the box and watch the number of rounds change while the "
                "answer does not.",
                "For a rehearsal, take network 1 and hand-write the labels `0, 4, 2, 7`. Every "
                "arc constraint holds, so this is a feasible dual point too &mdash; and its "
                "objective is 7, which is more than 6 and therefore impossible. Find your error: "
                "`b>a` gives `4 − 2 = 2 &gt; 1`, so the point is not feasible after all. This is "
                "the whole skill: a claimed certificate is checked arc by arc, not by eye.",
                "The harder rehearsal: on network 3, change `y>z` from `−3` to `−2`. The cycle "
                "now costs zero, the labels settle, and a feasible potential exists. A "
                "zero-cost cycle is the boundary case, and it is worth seeing both sides of it.",
            ],
        },
        "quiz_title": "Potentials, tightness and cycles",
        "quiz": [
            {"q": "A feasible set of node potentials is shifted by adding 7 to every one of them. What happens?",
             "a": ["Every constraint still holds and the dual objective is unchanged",
                   "Every constraint still holds and the dual objective rises by 7",
                   "The constraints on arcs leaving the source are violated",
                   "The tight arcs become slack"],
             "c": 0,
             "why": "Both the constraints `πⱼ − πᵢ ≤ cᵢⱼ` and the objective `πₜ − πₛ` are "
                    "differences of labels, so a constant added everywhere cancels in each of "
                    "them. Tightness is a difference too and survives. The lab's shift control "
                    "does this and reports both facts; adding a constant to one label only is "
                    "an entirely different matter and generally violates something."},
            {"q": "What does it mean for an arc to be tight?",
             "a": ["It is at capacity",
                   "`πⱼ − πᵢ = cᵢⱼ`, and the shortest routes use exactly these arcs",
                   "Its cost is the smallest in the network",
                   "It lies on every shortest path"],
             "c": 1,
             "why": "Tight means the dual constraint holds with equality. Complementary "
                    "slackness then says flow may travel only on tight arcs, so the tight "
                    "subgraph carries the shortest routes. Capacity has nothing to do with it "
                    "&mdash; this dual has no capacities in it. An arc can be tight without "
                    "lying on every shortest path, since there may be several."},
            {"q": "The relaxation is still improving labels after as many rounds as there are nodes. What has been discovered?",
             "a": ["The network is disconnected",
                   "A negative cycle: the dual is infeasible and the primal unbounded",
                   "A numerical error, since exact arithmetic cannot improve forever",
                   "That the source was chosen badly"],
             "c": 1,
             "why": "Adding the dual constraints round a cycle cancels every label and leaves "
                    "`0 ≤ (cycle cost)`, so a negative cycle admits no feasible potentials at "
                    "all. On the primal side, going round the cycle repeatedly lowers the cost "
                    "without limit. The lab's third instance names the cycle and reports its "
                    "cost of `−1`."},
            {"q": "A network has an arc of cost `−3`. Is the shortest-path problem still well posed?",
             "a": ["No: shortest paths require non-negative costs",
                   "Yes, provided no cycle has negative total cost",
                   "Yes, but only if the negative arc leaves the source",
                   "Only if the negative arc is on the shortest path"],
             "c": 1,
             "why": "A negative arc is meaningful whenever traversing it earns rather than "
                    "spends, and the lab's second instance has one: the labels settle at "
                    "`0, 4, 1, 3` and `b` is reached at 1 through `a` rather than at 2 directly. "
                    "What breaks the problem is a negative <em>cycle</em>. Non-negativity is a "
                    "requirement of Dijkstra's algorithm specifically, which is a different "
                    "claim."},
        ],
        "mistakes": [
            ("Calling the labels distances and stopping there",
             "They are distances under the normalisation `πₛ = 0` and they are potentials in "
             "general, and the difference matters as soon as you want to reprice a network, "
             "check somebody else's answer, or say what the dual objective is. A vector "
             "determined only up to a constant is a price; treating it as a fixed quantity leads "
             "to arguments about whose numbers are right when both are."),
            ("Confusing a negative arc with a negative cycle",
             "A negative arc is ordinary. A negative cycle makes the problem unbounded and no "
             "labels exist. Readers who have learned Dijkstra's algorithm first often carry over "
             "its non-negativity requirement as though it were a property of the problem rather "
             "than of that algorithm."),
            ("Checking a claimed potential only along the route",
             "Feasibility is a statement about every arc, and the arcs that are not on the route "
             "are where a wrong claim hides. It is one subtraction per arc. A potential that "
             "passes every arc is a certificate; a potential that has only been checked along "
             "one path certifies nothing."),
        ],
        "standard": ("Finish when you can hand back a set of potentials and a one-line argument that no path is shorter.",
                     "You should be able to write the shortest-path dual, run the relaxation to "
                     "a settled vector, check every arc, identify the tight arcs and read the "
                     "route off them, explain why a constant shift changes nothing, and "
                     "recognise a negative cycle as dual infeasibility rather than as a failure "
                     "of the method."),
        "note": 'One number per node, checkable arc by arc, and it proves a lower bound on every route at once &mdash; the dual of a network problem keeps turning out to be a small object a reader can verify by hand. &ldquo;Maximum Flow and Minimum Cut&rdquo; does the same thing, and there the dual solution is not a set of numbers but a set of nodes: a cut, whose capacity bounds every flow and which the residual network hands you for free the moment the algorithm stops.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "maximum-flow-and-minimum-cut",
        "title": "Maximum Flow and Minimum Cut",
        "module": "Paths, cuts and matchings",
        "one_line": "Any cut bounds any flow, the smallest cut equals the largest flow, and the set reachable in the final residual network is that cut.",
        "summary": (
            "Push flow along paths in the residual network &mdash; forward where there is spare "
            "capacity, backward where flow can be undone &mdash; until no path remains. The set "
            "of nodes still reachable from the source is then a cut whose capacity equals the "
            "flow value, which proves both optimal at once. And the reason a cut bounds a flow "
            "is not an analogy: every cut is a zero-one feasible point of the dual programme."
        ),
        "key": [
            "a cut is a set S containing s and not t; its capacity is Σ of the arcs leaving S",
            "weak duality: value(f) ≤ capacity(S) for EVERY flow f and EVERY cut S",
            "residual arc: forward with u − f spare, backward carrying what f already sent",
            "no residual path from s to t ⟹ the reachable set is a cut of exactly that value",
            "max flow = min cut, and both are the optimum of one linear programme and its dual",
            "the dual has one variable per interior node and one per arc; a cut sets them 0/1",
        ],
        "key_label": "The bound, the algorithm that attains it, and the certificate it leaves behind",
        "concepts_intro": (
            "The theorem is famous and the bound half of it is easy. The two ideas that repay "
            "attention are the backward arc and the sense in which a cut is a dual solution."
        ),
        "concepts": [
            ("Every cut bounds every flow, before any algorithm runs",
             "Everything reaching the sink must cross from the source's side to the other side "
             "at some point, and the arcs crossing can carry at most their total capacity. So "
             "each cut gives a bound, immediately, with no computation beyond an addition. The "
             "lab enumerates every cut of the network &mdash; four on its first instance, "
             "sixteen on its widest &mdash; and checks that each one bounds the current flow."),
            ("The backward arc is what makes the algorithm correct",
             "The residual network holds a forward arc wherever spare capacity remains and a "
             "backward arc wherever flow has already been sent. A path using a backward arc "
             "un-sends flow on that arc and re-routes it, and without that the algorithm can "
             "strand itself at a non-maximum flow. On the lab's first instance the third "
             "augmentation does exactly this: it routes through `b`, undoes a unit that had gone "
             "from `a` to `b`, and sends it to the sink instead."),
            ("A cut is a zero-one point of the dual programme",
             "The maximum-flow programme has one equality row per interior node and one bound "
             "row per arc, so its dual has one variable per interior node and one per arc. Set "
             "the node variable to one for nodes inside `S` and the arc variable to one for arcs "
             "crossing out of `S`, and that point is dual feasible with objective exactly the "
             "cut's capacity. The lab checks this for every cut it enumerates, which is why "
             "&ldquo;a cut bounds a flow&rdquo; is weak duality rather than a resemblance."),
        ],
        "read_title": "The bound, the algorithm, and the certificate",
        "read_intro": "Cuts and the bound first, then augmentation on the residual network, then the theorem and the dual reading that explains it.",
        "body": [
            ("def", ("Cuts and their capacity",
                     "An <strong>s-t cut</strong> is a set of nodes `S` containing the source "
                     "and not the sink. Its <strong>capacity</strong> is the total capacity of "
                     "the arcs whose tail is in `S` and whose head is not &mdash; arcs running "
                     "the other way do not count.",
                     "The <strong>value</strong> of a flow is the net amount leaving the source. "
                     "Every unit of it must cross every cut, so the value of any flow is at most "
                     "the capacity of any cut.")),
            ("p", "That is the easy half and it is worth having on its own: any cut you can "
                  "write down is a bound on every flow that will ever be found, and an "
                  "arithmetic check that takes seconds. The hard half is that the bound is "
                  "attained &mdash; that some cut has exactly the capacity of the largest flow "
                  "&mdash; and the algorithm proves it by producing the cut."),
            ("math", [
                "arcs   s>a 3   s>b 2   a>b 2   a>t 2   b>t 3",
                "",
                "every cut, enumerated:        S            capacity",
                "                              {s}              5",
                "                              {s,a,b}          5",
                "                              {s,a}            6",
                "                              {s,b}            6",
                "",
                "   two of the four are minimum, so a minimum cut need not be unique",
                "",
                "augmenting, from nothing:",
                "",
                "   residual  s>a s>b a>b a>t b>t        [x>y] below is BACKWARD",
                "   take      s>a, a>b, b>t           bottleneck 2      value 2",
                "   take      s>a, a>t                bottleneck 1      value 3",
                "   take      s>b, [b>a], a>t         bottleneck 1      value 4    BACKWARD",
                "   take      s>b, b>t                bottleneck 1      value 5",
                "   no residual path from s to t remains",
                "",
                "   final flow   s>a 3   s>b 2   a>b 1   a>t 2   b>t 3",
                "   reachable from s in the residual network:  {s}",
                "   capacity of that cut:  3 + 2  =  5  =  the flow value",
            ]),
            ("p", "Notice the third augmentation. The path runs from `s` to `b` on a forward "
                  "arc, then from `b` to `a` on a <em>backward</em> arc &mdash; there is no arc "
                  "from `b` to `a` in the network at all; what exists is a unit already sent "
                  "from `a` to `b`, which this path un-sends &mdash; and then from `a` to `t`. "
                  "The net effect is to reroute a unit that had been sent the wrong way. Without "
                  "backward arcs the algorithm would have stopped at 4."),
            ("thm", ("Max-flow min-cut",
                     "In any network the maximum value of an s-t flow equals the minimum "
                     "capacity of an s-t cut.",
                     "When no augmenting path remains, let `S` be the set of nodes reachable "
                     "from the source in the residual network. Every arc out of `S` must be "
                     "saturated, or its forward residual arc would extend the reachable set; "
                     "every arc into `S` must be empty, or its backward residual arc would. So "
                     "the flow across that cut is exactly its capacity, and since flow value is "
                     "at most any cut's capacity, both are optimal.")),
            ("p", "The proof is the algorithm's stopping condition read as a statement about the "
                  "cut, which is why the certificate costs nothing extra: it is the set the "
                  "search had already computed when it failed to find a path. The lab shades it "
                  "and prints its capacity beside the flow value."),
            ("h3", "Why a cut bounds a flow: the dual"),
            ("p", "The maximum-flow programme on the four-node network above has five variables "
                  "&mdash; one per arc &mdash; and seven rows: two conservation equalities at "
                  "the interior nodes `a` and `b`, and five capacity bounds. Its dual therefore "
                  "has seven variables, one for each of those rows: a potential for each "
                  "interior node and an indicator for each arc."),
            ("example", ("Two cuts, written as dual points",
                         "The cut `S = {s}` becomes the point with both node potentials at zero "
                         "and the indicators on `s>a` and `s>b` at one, everything else zero. "
                         "The cut `S = {s, a, b}` becomes both potentials at one and the "
                         "indicators on `a>t` and `b>t` at one.",
                         "The lab checks both against the dual's constraints row by row: each is "
                         "feasible, and each has dual objective 5 &mdash; exactly its own "
                         "capacity. It then does the same for every cut of the network, "
                         "including the two of capacity 6, and every one is a feasible dual "
                         "point whose objective is its capacity. That is why a cut bounds a "
                         "flow: it is weak duality with different nouns.")),
            ("p", "And the exact simplex on the primal programme returns 5. A feasible primal "
                  "point worth 5, a feasible dual point worth 5, and the simplex agreeing with "
                  "both: strong duality, exhibited on the instance rather than cited."),
            ("example", ("Minimum cuts need not be unique, or few",
                         "The four-node instance has two minimum cuts out of four. A second "
                         "instance has exactly one, `{s, b}` at capacity 5, and it is the "
                         "reachable set the algorithm lands on. A six-node instance has sixteen "
                         "cuts, four of them minimum at capacity 7, and the augmenting loop "
                         "still finishes at a flow of 7.",
                         "The reachable set is one minimum cut and the algorithm names it; the "
                         "others are just as valid as certificates. What the theorem asserts is "
                         "about the number 7, not about which set attains it.")),
            ("p", "What is deliberately not here is the choice of augmenting path. Take them in "
                  "a bad order and the algorithm still terminates on integer capacities, but the "
                  "number of augmentations can be much larger than it needs to be; bounding it "
                  "is the Algorithms path's business, in its treatment of graph algorithms. The "
                  "lab lets you pick any residual path from a list precisely so that the choice "
                  "is visible as a choice."),
        ],
        "lab": ("network", {
            "mode": "maxflow",
            "preset": "twocuts",
            "panel_title": "Push flow, then read the cut off the residual network",
            "panel_intro": "Choose an augmenting path from the residual network and push its "
                           "bottleneck, or run to the end. The residual network is drawn "
                           "underneath, with the backward arcs visible as arcs; when no path is "
                           "left, the reachable set is shaded and its capacity printed beside "
                           "the flow value. Every other cut can be selected and compared, and "
                           "each is checked as a point of the dual programme.",
        }),
        "steps_title": "Finding a maximum flow and proving it maximum",
        "steps_intro": "The proof arrives with the algorithm; the work is in not throwing it away.",
        "steps": [
            ("Build the residual network from the current flow",
             "A forward arc with `uᵢⱼ − fᵢⱼ` wherever there is spare capacity, and a backward "
             "arc with `fᵢⱼ` wherever something has been sent. The backward arcs are not "
             "optional and they are not arcs of the original network."),
            ("Find any path from source to sink in it, and push its bottleneck",
             "The bottleneck is the smallest residual capacity on the path. Push that much: add "
             "it on forward arcs, subtract it on backward arcs. Any path will do for "
             "correctness; which one you take affects only how many pushes you make."),
            ("Repeat until no such path exists",
             "On integer capacities each push increases the value by at least one, so this "
             "terminates. The stopping condition is the absence of a path, not the exhaustion of "
             "any particular arc."),
            ("Take the reachable set as your cut, and add up the arcs leaving it",
             "Every arc out of it is saturated and every arc into it is empty, so its capacity "
             "equals the flow value. This is the certificate, and it is free: the search that "
             "failed to find a path has already computed the set."),
            ("Report the pair",
             "A flow of value `v` and a cut of capacity `v`. Anyone can verify the cut by adding "
             "up a handful of capacities, and that verification proves no flow exceeds `v` "
             "without re-running anything."),
        ],
        "worked": {
            "title": "Five arcs, four augmentations, and the cut that was waiting at the end",
            "intro": [
                "Every residual network, every path offered, every bottleneck and every cut "
                "below is what the lab computes as the flow is pushed."
            ],
            "lines": [
                "NETWORK    s>a 3   s>b 2   a>b 2   a>t 2   b>t 3",
                "           [x>y] below is a BACKWARD residual arc: it undoes flow sent",
                "",
                "PUSH 1     residual   s>a  s>b  a>b  a>t  b>t",
                "           paths      s>a,a>b,b>t | s>a,a>t | s>b,b>t",
                "           take       s>a, a>b, b>t     bottleneck 2",
                "           flow       s>a 2  s>b 0  a>b 2  a>t 0  b>t 2     value 2",
                "",
                "PUSH 2     residual   s>a  [a>s]  s>b  [b>a]  a>t  b>t  [t>b]",
                "           take       s>a, a>t          bottleneck 1",
                "           flow       s>a 3  s>b 0  a>b 2  a>t 1  b>t 2     value 3",
                "",
                "PUSH 3     residual   [a>s]  s>b  [b>a]  a>t  [t>a]  b>t  [t>b]",
                "           paths      s>b,[b>a],a>t | s>b,b>t",
                "           take       s>b, [b>a], a>t   bottleneck 1",
                "                      the middle step UNDOES a unit sent a to b",
                "           flow       s>a 3  s>b 1  a>b 1  a>t 2  b>t 2     value 4",
                "",
                "PUSH 4     take       s>b, b>t          bottleneck 1",
                "           flow       s>a 3  s>b 2  a>b 1  a>t 2  b>t 3     value 5",
                "",
                "STOP       residual   [a>s]  [b>s]  a>b  [b>a]  [t>a]  [t>b]",
                "           no path from s to t:  every arc out of s is backward",
                "           reachable set  S = {s}",
                "           capacity       s>a 3 + s>b 2  =  5  =  the flow value",
                "",
                "ALL FOUR CUTS      {s} 5   {s,a,b} 5   {s,a} 6   {s,b} 6",
                "   two are minimum; every one of them bounds the flow of 5",
                "",
                "AS DUAL POINTS     {s}      potentials 0,0   indicators on s>a, s>b",
                "                   {s,a,b}  potentials 1,1   indicators on a>t, b>t",
                "   both feasible, both with dual objective 5",
                "   the simplex on the primal programme:  5",
            ],
            "after": [
                "Push 3 is the lesson. There is no arc from `b` to `a` in the network; the path "
                "uses one anyway, because a unit had already been sent from `a` to `b` and "
                "sending it back is allowed. Delete the backward arcs from the residual network "
                "and the algorithm stops at 4 and reports it as maximum.",
                "For a rehearsal, restart and take the paths in a different order &mdash; "
                "`s, a, t` first, then `s, b, t`, then whatever remains. You will reach 5 again, "
                "in a different number of pushes, and quite possibly without ever needing a "
                "backward arc. The order affects the work and not the answer.",
                "The harder rehearsal: open the six-node instance. It has sixteen cuts and four "
                "of them are minimum at capacity 7. Find a second minimum cut by hand, check it "
                "against the lab's enumeration, and satisfy yourself that it certifies the same "
                "7 as the reachable set does. A certificate does not have to be the one the "
                "algorithm found.",
            ],
        },
        "quiz_title": "Cuts, residual arcs and the dual",
        "quiz": [
            {"q": "You write down a cut of capacity 9 in a network. What have you proved?",
             "a": ["That the maximum flow is 9",
                   "That no flow in that network exceeds 9",
                   "That some flow of value 9 exists",
                   "Nothing until you check that it is the minimum cut"],
             "c": 1,
             "why": "Every unit of flow must cross every cut, so any cut is an upper bound "
                    "immediately &mdash; no algorithm and no minimality required. Whether 9 is "
                    "attained is the other half of the theorem. On the lab's first instance the "
                    "cuts have capacities 5, 5, 6 and 6, and all four bound the flow of 5 while "
                    "only two of them are tight."},
            {"q": "An augmenting path uses a backward residual arc. What does that step do?",
             "a": ["It sends flow the wrong way down an arc, which the capacities forbid",
                   "It cancels flow previously sent on that arc and reroutes it",
                   "It is a bookkeeping trick with no effect on the flow",
                   "It is only needed when the network has antiparallel arcs"],
             "c": 1,
             "why": "A backward residual arc exists exactly where flow has already been sent, "
                    "and using it un-sends some. On the lab's first instance the third "
                    "augmentation routes through `b`, undoes a unit that had gone from `a` to "
                    "`b`, and delivers it to the sink from `a` instead. Remove backward arcs and "
                    "the algorithm stops at 4 on a network whose maximum flow is 5."},
            {"q": "The algorithm stops. Which set of nodes is a minimum cut?",
             "a": ["The nodes adjacent to the source",
                   "The nodes whose arcs are all saturated",
                   "The set reachable from the source in the final residual network",
                   "The set from which the sink is unreachable in the original network"],
             "c": 2,
             "why": "By the stopping condition, the sink is not reachable in the residual "
                    "network, so that set is a cut; every arc out of it must be saturated and "
                    "every arc into it empty, or the set would be larger. Its capacity therefore "
                    "equals the flow value, and both are optimal. The certificate is free: the "
                    "failed search already computed the set."},
            {"q": "In what sense is a cut a solution of the maximum-flow dual?",
             "a": ["Loosely: the two problems merely have the same optimal value",
                   "Literally: put a one on each node inside `S` and on each arc leaving it, and the result is a feasible dual point whose objective is the cut's capacity",
                   "Only for minimum cuts; other cuts are not dual feasible",
                   "Only after the capacities have been scaled to lie between zero and one"],
             "c": 1,
             "why": "The dual has one variable per interior node and one per arc, and the "
                    "zero-one point the cut names satisfies every dual constraint with objective "
                    "equal to the capacity. The lab checks this for every cut it enumerates, "
                    "including the two of capacity 6, so weak duality for flows and cuts is the "
                    "general weak duality theorem rather than an analogy for it."},
        ],
        "mistakes": [
            ("Counting the arcs that run back into `S`",
             "A cut's capacity counts only the arcs whose tail is inside and whose head is "
             "outside. Arcs running the other way are irrelevant to the bound, because flow "
             "crossing back has to cross forward again. Including them inflates the capacity and "
             "produces bounds that are true but useless, and sometimes a claimed minimum cut "
             "that is not minimum."),
            ("Leaving the backward arcs out of the residual network",
             "This is the single error that makes the algorithm wrong rather than slow. Without "
             "them it can reach a flow with no augmenting path that is not maximum &mdash; 4 "
             "instead of 5 on the lab's first instance &mdash; and it will report that "
             "confidently, since its stopping condition has been met."),
            ("Reporting the flow and discarding the cut",
             "The cut is the proof, and it is the cheapest thing on the page: the set was "
             "computed by the search that failed. A flow value on its own is a claim that "
             "somebody has to re-run the algorithm to check; a flow value with a cut of the same "
             "capacity is checkable in an addition."),
        ],
        "standard": ("Finish when you can run the augmenting loop, hand back a cut of the same capacity, and explain what the cut is dually.",
                     "You should be able to build a residual network including its backward "
                     "arcs, push along a path and update, recognise the stopping condition, take "
                     "the reachable set as a minimum cut and verify its capacity, and write a "
                     "cut as a zero-one point of the dual programme."),
        "note": 'The pattern of this course is now complete on three problems: a cheapest route certified by potentials, a project length certified by a chain, a flow certified by a cut. &ldquo;Bipartite Matching and Hall&rsquo;s Condition&rdquo; applies the flow theorem to something that does not look like flow at all &mdash; who can be given which job &mdash; and gets back Hall&rsquo;s condition, with the violating set read straight off the minimum cut.',
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "bipartite-matching-and-halls-condition",
        "title": "Bipartite Matching and Hall's Condition",
        "module": "Paths, cuts and matchings",
        "one_line": "Turn a bipartite graph into a unit-capacity network, and the minimum cut hands back the set of applicants with too few jobs between them.",
        "summary": (
            "A matching is a flow. Put a unit arc from a source to every applicant, keep every "
            "original edge at capacity one, and put a unit arc from every job to a sink: a flow "
            "of value `k` is a matching of size `k`, and it comes out whole because of the "
            "matrix. Then the minimum cut is not just a bound &mdash; it names a set of "
            "applicants whose jobs between them are too few, which is Hall's condition failing, "
            "and it is a certificate anybody can check by counting."
        ),
        "key": [
            "matching: a set of edges no two of which share a vertex",
            "the reduction: src>each applicant at 1, each edge at 1, each job>snk at 1",
            "a flow of value k on that network is a matching of size k, and it is whole",
            "Hall: a matching saturating X exists ⟺ every S ⊆ X has |N(S)| ≥ |S|",
            "if the matching falls short, S = the applicants on the source side of the min cut",
            "Koenig: smallest vertex cover = largest matching     the Hungarian cover, again",
        ],
        "key_label": "The reduction, the theorem, and where the violating set comes from",
        "concepts_intro": (
            "The reduction is three lines and the integrality is already proved. What this "
            "lesson adds is that the failure comes with a reason attached."
        ),
        "concepts": [
            ("A matching is a flow, and the flow is whole for a reason",
             "Unit arcs from a source to the applicants, the original edges at capacity one, "
             "unit arcs from the jobs to a sink. Any integral flow of value `k` saturates `k` of "
             "the source arcs and `k` of the sink arcs and uses `k` edges no two of which share "
             "an endpoint &mdash; a matching. And the flow is integral because the constraint "
             "matrix is the one already swept for total unimodularity: half an applicant is "
             "excluded by the matrix, not by the algorithm."),
            ("Hall's condition is necessary for an obvious reason and sufficient for a hard one",
             "If some set `S` of applicants has fewer jobs between them than there are members "
             "of `S`, clearly not all of `S` can be placed. That direction is counting. The "
             "content of the theorem is the converse, and the flow argument supplies it "
             "constructively: when the maximum matching falls short, the minimum cut produces "
             "the violating `S`."),
            ("The certificate is a set, and checking it is counting",
             "The lab prints `S`, its neighbourhood `N(S)` and the difference. Verifying the "
             "claim means listing the jobs those applicants are willing to take and counting "
             "them &mdash; no algorithm, no trust. That is the same shape as a cut certifying a "
             "flow and a critical path certifying a project length, which by now is the point of "
             "the whole course."),
        ],
        "read_title": "Matchings as flows, and the set the cut hands back",
        "read_intro": "The reduction, then the theorem, then the three instances: one where every job is filled and somebody is still left out, one where the deficient set is small, and one where nothing is deficient.",
        "body": [
            ("def", ("Matchings, and Hall's condition",
                     "In a bipartite graph with parts `X` and `Y`, a <strong>matching</strong> "
                     "is a set of edges no two of which share a vertex. It "
                     "<strong>saturates</strong> `X` when every member of `X` is in one of its "
                     "edges.",
                     "For `S ⊆ X`, write `N(S)` for the set of vertices in `Y` joined to at "
                     "least one member of `S`. <strong>Hall's condition</strong> is that "
                     "`|N(S)| ≥ |S|` for every `S ⊆ X`.")),
            ("thm", ("Hall's marriage theorem",
                     "A bipartite graph has a matching saturating `X` if and only if "
                     "`|N(S)| ≥ |S|` for every subset `S` of `X`.",
                     "Discrete Mathematics states this in &ldquo;Bipartite Graphs&rdquo; and "
                     "does not prove the sufficient direction. This lesson supplies it as a "
                     "consequence of max-flow min-cut, and does so constructively: when the "
                     "maximum matching misses a vertex, the minimum cut of the flow network "
                     "exhibits the violating `S`.")),
            ("p", "The reduction is short enough to keep in your head. Add a source with a "
                  "capacity-one arc to each member of `X`; keep every edge of the graph as an "
                  "arc of capacity one; add a sink with a capacity-one arc from each member of "
                  "`Y`. On a three-applicant, two-job instance that is seven nodes and eleven "
                  "arcs."),
            ("math", [
                "the graph        1-a  1-b  2-a  2-b  3-a  3-b",
                "",
                "the network      src>1  src>2  src>3            each capacity 1",
                "                 1>a 1>b 2>a 2>b 3>a 3>b        each capacity 1",
                "                 a>snk  b>snk                   each capacity 1",
                "                 7 nodes, 11 arcs",
                "",
                "maximum flow     2      and the linear programme agrees: 2",
                "maximum matching 2 of 3",
                "minimum cut      {src, 1, 2, 3, a, b}   capacity 2",
                "",
                "S = the applicants on the source side  =  {1, 2, 3}",
                "N(S)                                   =  {a, b}",
                "|N(S)| - |S|                           =  -1      Hall FAILS on S",
            ]),
            ("p", "Both jobs are filled, and an applicant is still left out. Those two sentences "
                  "are not in tension: there are three applicants and two jobs, and a matching "
                  "saturating the applicants would need three distinct jobs. The certificate is "
                  "the whole of `X` here, and it takes one sentence to check &mdash; all three "
                  "applicants will take only `a` or `b`, and there are two of those."),
            ("h3", "The deficient set need not be everybody"),
            ("example", ("Three sharing one job, and a fourth with three of its own",
                         "Edges `1-a, 2-a, 3-a, 4-b, 4-c, 4-d`. The maximum matching has two "
                         "edges out of a possible four, the minimum cut has capacity 2, and the "
                         "deficient set the cut names is `S = {1, 2, 3}` with "
                         "`N(S) = {a}`.",
                         "Three applicants, one job between them, a shortfall of two. Applicant "
                         "`4` is not part of the certificate at all &mdash; it has three jobs to "
                         "itself and is doing nothing wrong. A reader who expects the violating "
                         "set to be all of `X` will not find it here, and the searching that "
                         "follows is exactly what the minimum cut saves.")),
            ("example", ("Nothing deficient, and nothing to produce",
                         "Edges `1-a, 1-b, 2-b, 2-c, 3-c, 3-d, 4-d, 4-a`: four applicants in a "
                         "ring with four jobs. The maximum matching has four edges, every "
                         "applicant is placed, and the minimum cut has capacity 4 &mdash; the "
                         "set `{src}` alone.",
                         "`S` and `N(S)` come back empty and the lab reports that Hall's "
                         "condition holds on every subset. There is nothing to certify: the "
                         "alternating search that produces the violating set starts from the "
                         "unmatched applicants, and here there are none. Remove one edge and the "
                         "certificate appears.")),
            ("h3", "The same theorem, a third time"),
            ("p", "König's theorem &mdash; that in a bipartite graph the smallest vertex cover "
                  "has exactly as many vertices as the largest matching &mdash; is the same "
                  "statement again. The lab computes the cover from the matching, and it is the "
                  "cover the Hungarian method was counting when it drew lines through the zeros. "
                  "On the three-applicant instance the cover is the two jobs; on the "
                  "three-sharing-one instance it is applicant `4` together with job `a`."),
            ("p", "So the assignment lesson's cover step, this lesson's deficient set, and the "
                  "maximum-flow theorem are three readings of one fact. That is not a "
                  "coincidence worth admiring; it is the reason the assignment problem can be "
                  "solved by a method with a stopping proof, and the reason that method's most "
                  "delicate step is the one this lesson has now justified."),
            ("p", "One limitation to state plainly. All of this is about <em>bipartite</em> "
                  "graphs. Matching in a general graph is a genuinely harder problem with a "
                  "different theory, its own theorem about odd sets, and an algorithm this path "
                  "does not contain. The boundary is exactly the odd cycle that broke total "
                  "unimodularity in the integrality lesson, which is a pleasing place for a "
                  "course to end."),
        ],
        "lab": ("network", {
            "mode": "matching",
            "preset": "three-two",
            "panel_title": "Edit the bipartite graph, and watch the certificate appear",
            "panel_intro": "The flow network built from the graph, the maximum matching drawn on "
                           "it, the minimum cut shaded, and the deficient set `S` with its "
                           "neighbourhood `N(S)` counted on screen. Add an edge and the "
                           "certificate can vanish; remove one and it comes back, naming a "
                           "different set.",
        }),
        "steps_title": "Deciding whether everyone can be placed, and proving it either way",
        "steps_intro": "Build the network, find the flow, and then take whichever of the two certificates the answer offers you.",
        "steps": [
            ("Build the unit-capacity network",
             "Source to every applicant at capacity one, every edge at capacity one, every job "
             "to the sink at capacity one. Every capacity is one; a capacity of two anywhere "
             "means somebody is being allowed two jobs, and that is a different problem."),
            ("Find a maximum flow, and read the matching off it",
             "The arcs between the two sides carrying one unit are the matched pairs. The flow "
             "is whole automatically &mdash; this is a network, and its matrix is totally "
             "unimodular &mdash; so there is no rounding step and no half-matched applicant to "
             "interpret."),
            ("Compare the matching's size with the number of applicants",
             "Equal, and everybody is placed. Short, and there is a certificate to produce, "
             "which is the interesting case and the one most write-ups skip."),
            ("If it is short, take `S` from the minimum cut",
             "`S` is the set of applicants on the source side of the minimum cut. Write it down "
             "with `N(S)`, and check the count: `|N(S)| &lt; |S|`. That inequality is the answer "
             "to &ldquo;why can they not all be placed&rdquo;, and it is checkable without "
             "re-running anything."),
            ("If it is not short, say what has been proved and what has not",
             "A saturating matching exists and you have one. Hall's condition holds on every "
             "subset, but you have not checked every subset and you do not need to: the matching "
             "itself is the certificate in this direction."),
        ],
        "worked": {
            "title": "Three graphs: one certificate, a smaller certificate, and none",
            "intro": [
                "Each block is the maximum matching, the minimum cut of the flow network, and "
                "the deficient set the cut names. All of it is what the lab reports."
            ],
            "lines": [
                "GRAPH 1   1-a, 1-b, 2-a, 2-b, 3-a, 3-b       3 applicants, 2 jobs",
                "   network        7 nodes, 11 arcs, every capacity 1",
                "   maximum flow   2       LP on the same network: 2",
                "   matching       2 of 3",
                "   minimum cut    {src, 1, 2, 3, a, b}   capacity 2",
                "   S = {1, 2, 3}    N(S) = {a, b}    |N(S)| - |S| = -1",
                "   minimum vertex cover  {a, b}, size 2 = the matching     Koenig",
                "",
                "GRAPH 2   1-a, 2-a, 3-a, 4-b, 4-c, 4-d       4 applicants, 4 jobs",
                "   network        10 nodes, 14 arcs",
                "   matching       2 of 4",
                "   minimum cut    {src, 1, 2, 3, a}      capacity 2",
                "   S = {1, 2, 3}    N(S) = {a}       |N(S)| - |S| = -2",
                "   applicant 4 is NOT in the certificate; it has three jobs to itself",
                "   minimum vertex cover  {4, a}, size 2",
                "",
                "GRAPH 3   1-a, 1-b, 2-b, 2-c, 3-c, 3-d, 4-d, 4-a",
                "   network        10 nodes, 16 arcs",
                "   matching       4 of 4      every applicant placed",
                "   minimum cut    {src}                  capacity 4",
                "   S = {}    N(S) = {}       nothing to certify",
                "   minimum vertex cover  {1, 2, 3, 4}, size 4",
                "",
                "REFUSALS   an edge without a dash is refused",
                "           six vertices on one side is refused: the drawing takes five",
            ],
            "after": [
                "Graph 1 is the one that catches people. Every job is filled &mdash; the "
                "matching saturates the jobs perfectly &mdash; and an applicant is still left "
                "out, because saturating the applicants is a different requirement. The "
                "certificate is about the applicants, and it says the whole of `X` has only two "
                "jobs between it.",
                "For a rehearsal, take graph 2 and add the edge `1-b`. The matching goes to "
                "three and the certificate shrinks: the deficient set is now `{2, 3}` with a "
                "single job between them. Keep adding edges and watch the set contract until it "
                "disappears.",
                "The harder rehearsal: take graph 3 and remove `4-a`. Everybody is still placed, "
                "because the ring had slack in it. Remove `4-d` as well and applicant 4 has "
                "nothing left; the certificate that appears is `S = {4}` with "
                "`N(S)` empty, which is the smallest violation there is.",
            ],
        },
        "quiz_title": "The reduction, the certificate, and what it does not say",
        "quiz": [
            {"q": "In the flow network built from a bipartite graph, what capacity do the original edges get?",
             "a": ["Their weight, if the graph is weighted",
                   "One, like the source and sink arcs",
                   "No upper bound, since the source arcs already limit the flow",
                   "The number of jobs the applicant will accept"],
             "c": 1,
             "why": "Every capacity in the reduction is one. The source and sink arcs stop any "
                    "applicant taking two jobs or any job taking two applicants; giving the "
                    "middle arcs capacity one as well keeps the network uniform and makes the "
                    "cut argument read cleanly. Leaving them unbounded happens to give the same "
                    "maximum flow, but the minimum cut is then no longer the object Hall's "
                    "condition is about."},
            {"q": "Three applicants all willing to take only jobs `a` and `b`. The maximum matching has two edges. What is the certificate?",
             "a": ["`S = {a, b}`, since only two jobs exist",
                   "`S = {1, 2, 3}` with `N(S) = {a, b}`, so three applicants share two jobs",
                   "There is none: two of three placed is the best possible and needs no proof",
                   "The matching itself, since it is maximum"],
             "c": 1,
             "why": "`S` is always a set of applicants, and here it is all three: their "
                    "neighbourhood is `{a, b}`, of size two, which is fewer than three. That is "
                    "Hall's condition failing, and it can be checked by reading the edge list. "
                    "The matching being maximum is exactly what needs proving, and the matching "
                    "cannot prove it about itself."},
            {"q": "A bipartite graph has four applicants; three of them share a single job and the fourth has three jobs to itself. What deficient set does the minimum cut produce?",
             "a": ["All four applicants", "The three who share a job", "The fourth applicant alone", "The single shared job"],
             "c": 1,
             "why": "The cut names `S = {1, 2, 3}` with `N(S)` a single job, a shortfall of two. "
                    "The fourth applicant has three jobs of its own and is not part of the "
                    "problem, so including it would weaken the certificate: `|N(S)|` would rise "
                    "to four against `|S|` of four and the inequality would no longer fail. A "
                    "deficient set need not be all of `X`, and finding the right subset by hand "
                    "is what the cut spares you."},
            {"q": "A maximum matching saturates every applicant. What has been established about Hall's condition?",
             "a": ["Nothing, until every subset has been checked",
                   "That it holds on every subset — the matching is the certificate in that direction",
                   "That it holds on the subsets the algorithm examined",
                   "That it holds, provided the two sides are the same size"],
             "c": 1,
             "why": "The theorem is an equivalence, so a saturating matching implies the "
                    "condition on every subset without any of them being examined: each member "
                    "of `S` has its own distinct partner in `N(S)`, so `|N(S)| ≥ |S|`. The lab "
                    "reports empty sets and says there is nothing to certify, which is the "
                    "honest output &mdash; the alternating search that produces a violating set "
                    "starts from the unmatched applicants, and there are none."},
        ],
        "mistakes": [
            ("Expecting the deficient set to be all of the applicants",
             "It sometimes is and usually is not. On the lab's second instance it is three of "
             "the four, and adding the fourth would destroy the inequality rather than "
             "strengthen it. The certificate is a particular subset, the minimum cut produces "
             "it, and guessing is what the reduction exists to avoid."),
            ("Reading a matching that fills every job as a matching that places every applicant",
             "The lab's first instance fills both jobs and leaves an applicant out. Saturating "
             "`Y` and saturating `X` are different conditions, and Hall's theorem is about the "
             "side you are trying to place. Say which side you mean before claiming anything "
             "about the answer."),
            ("Carrying the theorem across to general graphs",
             "Hall's condition and the whole flow reduction are about bipartite graphs. Matching "
             "in a general graph has a different characterisation, a different algorithm, and "
             "no unit-capacity network that captures it &mdash; the obstruction is the odd "
             "cycle, the same one whose incidence matrix failed total unimodularity earlier on "
             "this course."),
        ],
        "standard": ("Finish when you can decide a placement question and hand back the right certificate for whichever answer you get.",
                     "You should be able to build the unit-capacity network from a bipartite "
                     "graph, read a matching off a flow, explain why the flow is whole, produce "
                     "the deficient set from the minimum cut when the matching falls short, "
                     "check `|N(S)| &lt; |S|` by counting, and say why a saturating matching needs "
                     "no further certificate."),
        "note": 'That is the course: one linear programme, one matrix, and four duals that turned out to be a set of prices, a chain of activities, a set of nodes and a set of applicants. The next course keeps the linear programme and throws away the matrix. Integer Programming is what remains when the corners are not lattice points &mdash; when rounding is not an answer, when a relaxation is only a bound, and when the honest deliverable stops being a certificate of optimality and becomes a gap.',
    },
]
