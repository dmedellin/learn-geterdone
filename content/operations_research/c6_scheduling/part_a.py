"""Scheduling, the first five lessons - one machine, and what an order can move.

The objective first, because a reader who has not watched one order win on one
measure and lose on five will keep asking whether a schedule is good; then the
adjacent exchange twice, unweighted and weighted, because it is the whole proof
technique of this course; then the two due-date questions, which look like one
question and are not.

Every figure below is read off the `schedule` kit. The kit computes each
objective by two routes that share no arithmetic and refuses to print anything
if they disagree, and it checks every claim of optimality against all `n!`
orders, so a number here is a number the reader can watch being produced.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "one-machine-and-six-objectives",
        "title": "One Machine, Six Objectives",
        "module": "A schedule is never simply good",
        "one_line": "Run five jobs in the order they arrived, score that order against six objectives at once, and find it is best at none of them.",
        "summary": (
            "One machine, five jobs, no idle time and nothing random: the simplest "
            "scheduling problem there is. It already has six sensible objectives, and "
            "the order that is best for one of them is beaten on the others by a "
            "different order each time. One number does not move at all &mdash; the "
            "makespan is the same in every one of the 120 orders &mdash; and knowing "
            "which number that is, before any rule is chosen, is what this lesson is "
            "for."
        ),
        "key": [
            "one machine, all jobs ready at time 0, no preemption, no idle time",
            "C_j the finish time     L_j = C_j − d_j     T_j = max(L_j, 0)     U_j = 1 if late",
            "sum C   sum w C   L max   T max   sum T   sum U        six objectives, six answers",
            "makespan = sum p = 25 in EVERY one of the 120 orders — no rule can move it",
            "A B C D E: 74, 165, 12, 12, 26, 4 late    optimal for 0 of the 6",
            "the six optima: 65, 108, 6, 6, 16, 2      attained by five DIFFERENT orders",
        ],
        "key_label": "One instance, six questions, and the one that has no question in it",
        "concepts_intro": (
            "Three ideas, and the first is a subtraction that has no answer: there is "
            "nothing to optimise about the makespan on one machine, and a reader who "
            "does not know that will spend effort on it."
        ),
        "concepts": [
            ("The makespan is the one number an order cannot move",
             "One machine that never stops finishes the last job when the work runs "
             "out, and the work does not depend on the order. On the lab's five jobs "
             "that is `6 + 4 + 5 + 3 + 7 = 25`, and the panel reports `25` for all 120 "
             "orders. Every other objective moves, some of them by a factor of two. "
             "Sequencing buys you nothing at all on the makespan and a great deal on "
             "the rest, and that asymmetry is the shape of the whole subject."),
            ("Six objectives, and a different winner for each",
             "Shortest-first gives the least total completion time, `65`. Smith's "
             "ratio gives the least weighted total, `108`. Earliest-due-date gives the "
             "least maximum lateness, `6`. The fewest late jobs is `2`, and the least "
             "total tardiness is `16` &mdash; attained by an order that no rule on this "
             "course produces. Five different orders, five different answers, and none "
             "of them is <em>the</em> schedule."),
            ("Optimal here means checked, not asserted",
             "Each objective in the panel is computed twice, by a forward clock and by "
             "a position-weighted sum that never forms a running clock, and the two "
             "must agree before anything is drawn. Then each is compared with the best "
             "of all `120` orders, found by enumeration. So the word &ldquo;optimal&rdquo; "
             "on the screen means a comparison was made, and when the instance is too "
             "large to enumerate the panel says the claim is unchecked rather than "
             "printing it anyway."),
        ],
        "read_title": "Six objectives on one machine, and the one that does not move",
        "read_intro": "The definitions, one order scored against all six at once, and the five rules that each win exactly one of them.",
        "body": [
            ("def", ("A single-machine instance, and the six objectives",
                     "`n` jobs, job `j` with a <strong>processing time</strong> `p_j`, "
                     "a <strong>weight</strong> `w_j` and a <strong>due date</strong> "
                     "`d_j`. One machine runs one job at a time, every job is "
                     "available at time zero, no job is interrupted, and the machine "
                     "never idles. A <strong>schedule</strong> is then just an order.",
                     "For an order, `C_j` is the clock when job `j` finishes. The "
                     "<strong>lateness</strong> is `L_j = C_j − d_j`, which may be "
                     "negative; the <strong>tardiness</strong> is `T_j = max(L_j, 0)`, "
                     "which may not; and `U_j` is `1` if `C_j > d_j` and `0` "
                     "otherwise. The six objectives are `sum C`, `sum w C`, `L max`, "
                     "`T max`, `sum T` and `sum U`, and every one of them is to be "
                     "made small.")),
            ("p", "The <strong>makespan</strong> `C max` is the seventh, and it is the "
                  "one worth disposing of first. It is the largest `C_j`, and on this "
                  "model it is `sum p` whatever the order, because the machine starts "
                  "at zero and never stops. That is not a theorem about a clever "
                  "schedule; it is arithmetic about a machine with no gaps in it."),
            ("thm", ("The makespan is constant on one machine",
                     "With every job available at time zero, no preemption and no "
                     "forced idle time, every order has makespan `sum p`.")),
            ("proof", ["The machine starts the first job at time `0` and starts each "
                       "later job the instant the previous one finishes, so at every "
                       "moment before the end it is working.",
                       "The total amount of work is `sum p` and none of it is done "
                       "twice or skipped, so the last job finishes at `sum p`. The "
                       "order was never used in the argument, so it cannot matter."]),
            ("p", "Drop any one of the three assumptions and this stops being true, "
                  "which is why they are stated rather than assumed. Release dates "
                  "force idle time; a second machine makes the makespan the hard part; "
                  "and a setup cost that depends on which job ran before makes the "
                  "total work itself depend on the order."),
            ("h3", "One order, six verdicts"),
            ("math", [
                "jobs   A 6:1:8   B 4:2:4   C 5:4:12   D 3:3:6   E 7:1:20",
                "order  A B C D E      the order they arrived in",
                "",
                "         p   w   d    C    wC     L     T   late",
                "  A      6   1   8    6     6    -2     0",
                "  B      4   2   4   10    20     6     6   late",
                "  C      5   4  12   15    60     3     3   late",
                "  D      3   3   6   18    54    12    12   late",
                "  E      7   1  20   25    25     5     5   late",
                "",
                "  sum C   74     sum wC  165     L max  12",
                "  T max   12     sum T    26     late    4 of 5",
                "  makespan 25",
            ]),
            ("p", "Every column there is read off one clock. The `C` column is the "
                  "running total of `p`; `wC` multiplies it by the weight; `L` "
                  "subtracts the due date and is allowed to be negative; `T` clips the "
                  "negatives to zero. Nothing in the table required a decision, and "
                  "that is the point &mdash; the decision was the order, and it was "
                  "made before any of this."),
            ("h3", "The same order, against every order there is"),
            ("math", [
                "objective   this order   the best there is   an order that attains it",
                "  sum C         74             65             D B C A E",
                "  sum wC       165            108             D C B A E",
                "  L max         12              6             B D A C E",
                "  T max         12              6             B D A C E",
                "  sum T         26             16             B D C A E",
                "  sum U          4              2             A C E B D",
                "",
                "  best at 0 of the 6            all 120 orders were scored",
                "  makespan      25             25             all 120 of them",
            ]),
            ("p", "Four different orders appear in that last column and none of them "
                  "is the one typed. The arrival order is optimal for nothing, which "
                  "is unremarkable; what is worth looking at is that no single order "
                  "appears twice. `D B C A E` is shortest-first and is `9` worse than "
                  "the best on weighted completion time. `B D A C E` is earliest-due-"
                  "date and is `17` against a best total tardiness of `16`. Being best "
                  "at one of these is normally being beaten at the rest."),
            ("example", ("Five rules, five winners, and a rival that loses",
                         "The lab fills the order box from a rule. Shortest processing "
                         "time gives `D B C A E`, which attains `sum C = 65`. Smith's "
                         "ratio `p/w` gives `D C B A E`, which attains `sum wC = 108`. "
                         "Earliest due date gives `B D A C E`, which attains `L max = "
                         "6` and `T max = 6`.",
                         "Now the two that lose. Heaviest-weight-first &mdash; a rule "
                         "that sounds exactly as reasonable as the others &mdash; gives "
                         "`C D B A E` and costs `111` on weighted completion time "
                         "against the `108` Smith's ratio reaches. And shortest-first, "
                         "which is <em>provably</em> optimal for `sum C`, costs `114` "
                         "on the weighted version: the same order, a different "
                         "question, and a worse answer than the rule that loses to it "
                         "on the unweighted one.")),
            ("p", "So the first thing to do with a scheduling problem is not to choose "
                  "a rule. It is to write down which of these six numbers you are "
                  "being paid to make small, because the rules disagree and there is "
                  "no tie-break between them that lives inside the arithmetic. A "
                  "workshop that is judged on how many orders ship late wants `sum U` "
                  "and should not be running shortest-first; a workshop billed by "
                  "customer-hours waiting wants `sum w C` and should not be running "
                  "earliest-due-date."),
            ("p", "This is the path's hazard in its cheapest possible form. Every "
                  "figure in the table above is exact and every claim of optimality "
                  "has been checked against 120 orders. An answer that is right about "
                  "`sum C` and was wanted for `sum T` is still wrong, and nothing in "
                  "the solve will ever say so."),
        ],
        "lab": ("schedule", {
            "mode": "objectives",
            "preset": "mixed",
            "panel_title": "One order, six objectives, and the best of every order beside each",
            "panel_intro": "Type the jobs and an order, or fill the order from one of "
                           "five rules. Every objective is computed twice by routes "
                           "that share no arithmetic and shown only if the two agree, "
                           "then compared with the best of all the orders there are. "
                           "The banner reports the makespan first, because it is the "
                           "one figure the order box cannot change.",
        }),
        "steps_title": "Scoring an order, and choosing what to score it on",
        "steps_intro": "Five steps, and the last one is the only one that involves a decision.",
        "steps": [
            ("Write the jobs down with the fields named",
             "`name p:w:d`, and say out loud what each number is. A weight is not a "
             "priority number to be sorted on and a due date is not a deadline that "
             "cannot be missed; they are the multiplier in one objective and the "
             "subtrahend in three others."),
            ("Build the clock once",
             "`C` is the running total of the processing times in the chosen order. "
             "Everything else on the page comes off that one column, which is why an "
             "error there is an error in all six figures at once and an error anywhere "
             "else is local."),
            ("Read each objective off the same clock",
             "`sum C` adds the column. `sum w C` adds it weighted. `L_j = C_j − d_j`, "
             "and `L max` is the largest of those <em>including</em> the negative ones. "
             "`T_j` clips at zero, `sum T` adds the clipped values, `sum U` counts the "
             "positive ones."),
            ("Check the makespan has not moved",
             "It should equal `sum p`, and it should be the same for every order you "
             "try. If it is not, one of the three assumptions has quietly been "
             "dropped &mdash; usually a release date, sometimes an idle gap you put in "
             "by hand."),
            ("Name the objective before naming a rule",
             "Write the objective at the top of the page and then choose. Every rule in "
             "this course is optimal for exactly one thing and beaten on the rest, and "
             "the decision about which thing was made outside the arithmetic long "
             "before the first job ran."),
        ],
        "worked": {
            "title": "Five jobs, 120 orders, and no order that wins twice",
            "intro": [
                "The lab's opening example, in full. The instance is its first preset, "
                "so every line below can be checked against the panel by switching the "
                "order box between the five rules.",
            ],
            "lines": [
                "jobs     A 6:1:8   B 4:2:4   C 5:4:12   D 3:3:6   E 7:1:20",
                "         total work 6 + 4 + 5 + 3 + 7 = 25",
                "",
                "THE ORDER THEY ARRIVED IN          A B C D E",
                "  C        6   10   15   18   25",
                "  wC       6   20   60   54   25          sum wC 165",
                "  L       -2    6    3   12    5          L max  12",
                "  T        0    6    3   12    5          sum T  26",
                "                                          sum C  74,  4 late",
                "",
                "THE FIVE RULES, EACH ON THE SAME FIVE JOBS",
                "  SPT     D B C A E    sum C  65   *      sum wC 114",
                "  WSPT    D C B A E    sum wC 108  *      sum C   66",
                "  EDD     B D A C E    L max   6   *      sum T   17",
                "  WEIGHT  C D B A E    sum wC 111         sum C   68",
                "  LPT     E A C B D    sum C  85          sum wC 211",
                "",
                "THE BEST OF ALL 120 ORDERS",
                "  sum C   65    sum wC 108    L max 6    T max 6    sum T 16    late 2",
                "  attained by  D B C A E,  D C B A E,  B D A C E,  B D C A E,  A C E B D",
                "",
                "  makespan 25 in all 120 of them",
            ],
            "after": [
                "The starred lines are the three theorems of the next three lessons, "
                "and each of them is a rule attaining an enumerated optimum. The "
                "unstarred figures beside them are the price of that optimum measured "
                "on a different objective, and they are what makes this a subject "
                "rather than a list of rules.",
                "`WEIGHT` is the row to stare at. Running the heaviest job first is a "
                "perfectly sensible policy, it is what most workshops actually do, and "
                "it costs `111` where `108` was available from a rule that is no harder "
                "to run. The gap is small and it is not zero, and nothing in the "
                "schedule announces it.",
                "For a rehearsal, switch the preset to the four-job example and repeat "
                "the whole table. The supplied first move is that the makespan will be "
                "`2 + 8 + 3 + 6 = 19` and will not move; predict, before the panel says "
                "so, whether the typed order is optimal for any of the six. It is "
                "optimal for none of them, and the total tardiness it costs is `14` "
                "against a best of `8`.",
            ],
        },
        "quiz_title": "What an order can move, and what it cannot",
        "quiz": [
            {"q": "On one machine with every job ready at time zero and no idle time, which objective is the same for every order?",
             "a": ["Total completion time `sum C`", "The makespan `C max`",
                   "Maximum lateness `L max`", "The number of late jobs `sum U`"],
             "c": 1,
             "why": "The machine works continuously from `0` until the work runs out, "
                    "so the last job finishes at `sum p` regardless of the order &mdash; "
                    "`25` on the lab's instance, in all 120 orders. The other three all "
                    "move: `sum C` ranges from `65` to `85` across the five rule orders "
                    "alone."},
            {"q": "An order attains the minimum `sum C` on an instance. What does that tell you about its `sum w C`?",
             "a": ["That it also minimises `sum w C`, since the weights only rescale",
                   "Nothing: on the lab's instance the `sum C` optimum costs `114` on `sum w C` where `108` is available",
                   "That its `sum w C` is within a factor of the maximum weight",
                   "That it minimises `sum w C` whenever all the weights are distinct"],
             "c": 1,
             "why": "Shortest-first gives `D B C A E`, which is optimal for `sum C` at "
                    "`65` and costs `114` on the weighted version against the `108` that "
                    "Smith's ratio reaches. The weights do not rescale the problem; they "
                    "change which order is best, which is the whole content of the "
                    "weighted lesson."},
            {"q": "The panel reports that an order is optimal for maximum lateness. What has actually been checked?",
             "a": ["That no adjacent swap improves it",
                   "That the order agrees with the earliest-due-date rule",
                   "That its `L max` equals the smallest `L max` over all `n!` orders, found by enumeration",
                   "That its `L max` is not positive"],
             "c": 2,
             "why": "The kit enumerates every order and compares. That is why it can "
                    "also report a rule <em>failing</em> to attain an optimum, which a "
                    "local check could not, and why it says the claim is unchecked "
                    "rather than printing it when the instance is too large to "
                    "enumerate."},
            {"q": "Which of these is a reason to prefer one objective over another on a real shop floor?",
             "a": ["`sum C` is smaller than `sum w C`, so it is the safer choice",
                   "`L max` is the only one that can be negative, so it carries the most information",
                   "Nothing in the arithmetic decides it: the objective is a statement about what the work is worth, and it is chosen before any rule is",
                   "`sum U` counts jobs rather than hours, so it is the most robust"],
             "c": 2,
             "why": "The six objectives disagree and the disagreement cannot be settled "
                    "from inside the model. A shop judged on orders shipped late wants "
                    "`sum U`; one billed for customer-hours waiting wants `sum w C`. "
                    "Choosing the objective is the modelling step, and it is the one "
                    "step a correct solve cannot rescue."},
        ],
        "mistakes": [
            ("Trying to improve the makespan by resequencing",
             "On one machine with no release dates there is nothing there: the last job "
             "finishes at `sum p` in every order, and the lab prints `25` for all 120 of "
             "them. Effort spent on it is effort not spent on the five objectives that "
             "do move, and a report claiming a makespan improvement from resequencing "
             "has changed the model without saying so."),
            ("Reading “optimal” as optimal for everything",
             "Shortest-first is optimal for `sum C` and costs `114` on `sum w C` where "
             "`108` exists. Earliest-due-date is optimal for `L max` and leaves `4` jobs "
             "late where `2` is possible. Each theorem on this course names one "
             "objective, and the name is load-bearing."),
            ("Treating lateness and tardiness as the same column",
             "`L_j` may be negative and `T_j` may not, so a job finishing early pulls "
             "`L max` down and contributes nothing to `sum T`. On the lab's instance "
             "`A` has `L = −2` and `T = 0`. Averaging lateness over the jobs, which the "
             "sign makes tempting, gives a number no objective on this course asks for."),
        ],
        "standard": ("Finish when you can score an order on all six objectives and say, before looking, which one will not move.",
                     "You should be able to build the completion-time clock for a typed "
                     "order, read `sum C`, `sum w C`, `L max`, `T max`, `sum T` and "
                     "`sum U` off it, state that the makespan is `sum p` and say which "
                     "three assumptions make that true, and explain why an order that "
                     "attains one of the six optima is normally beaten on the other "
                     "five."),
        "note": 'Every rule in the rest of this course is proved the same way, and it is not by calculus and not by induction on a clever invariant: take two jobs that sit next to each other, swap them, and compute the exact quantity the swap moved. &ldquo;Shortest Processing Time and the Adjacent Exchange&rdquo; does it for the first of the six objectives, and the lab walks from the worst order to the best one improving swap at a time, so the argument is watched rather than asserted.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "shortest-processing-time-and-the-adjacent-exchange",
        "title": "Shortest Processing Time and the Adjacent Exchange",
        "module": "The adjacent exchange",
        "one_line": "Swap two neighbouring jobs, watch the total completion time move by one subtraction, and let the swaps walk you from the worst order to the best.",
        "summary": (
            "Swapping two adjacent jobs changes the completion time of those two jobs "
            "and of nothing else, and the whole change in `sum C` is `p_b − p_a`. That "
            "one subtraction is the entire proof that shortest-first is optimal: it is "
            "negative exactly when the shorter job was behind, so an order with a "
            "longer job in front of a shorter one can always be improved, and only the "
            "sorted order cannot. The lab runs the argument rather than stating it."
        ),
        "key": [
            "swap adjacent a then b:   only C_a and C_b change",
            "sum C moves by  p_b − p_a       negative exactly when  p_b < p_a",
            "so an out-of-order adjacent pair can ALWAYS be improved",
            "SPT = sort by p ascending;  no adjacent pair is out of order, so nothing improves",
            "A 9, B 2, C 6, D 3, E 5:   LPT 92,  FCFS 82,  SPT 58,  best of 120  58",
            "the walk from LPT to SPT is 10 improving swaps, moving −34 in total",
        ],
        "key_label": "One swap, one subtraction, and where the swaps run out",
        "concepts_intro": (
            "One argument, taken slowly, because every later rule on this course is "
            "this argument with a different quantity in the subtraction."
        ),
        "concepts": [
            ("A swap is local, and that is what makes it computable",
             "Take the jobs in positions `i` and `i + 1` and exchange them. Everything "
             "before position `i` finishes at the same clock, because nothing about it "
             "changed. Everything after position `i + 1` finishes at the same clock "
             "too, because the same two jobs were done in between and the same total "
             "amount of work was completed. Only two completion times move, so the "
             "difference in `sum C` is a subtraction rather than a recomputation."),
            ("The subtraction has no other terms in it",
             "Let the pair start at time `t`. Before the swap the two finish at "
             "`t + p_a` and `t + p_a + p_b`; after it, at `t + p_b` and `t + p_b + p_a`. "
             "The second of each pair is the same number, so the difference is "
             "`(t + p_b) − (t + p_a) = p_b − p_a`. The start time `t` cancels, which is "
             "why the same subtraction works at every position in every order."),
            ("An order nothing improves is the sorted one",
             "If any adjacent pair has the longer job first, the swap strictly improves "
             "`sum C`, so that order is not optimal. The only orders with no such pair "
             "are those sorted by `p` ascending. Hence shortest-first is optimal &mdash; "
             "and the lab does not take this on trust: from the worst order it takes "
             "improving swaps one at a time and reports where it stops."),
        ],
        "read_title": "The exchange, the subtraction, and the walk it induces",
        "read_intro": "One definition, the swap identity proved in three lines, and ten improving swaps taken in front of you.",
        "body": [
            ("def", ("An adjacent exchange",
                     "Given an order and a position `i`, the <strong>adjacent "
                     "exchange</strong> at `i` is the order obtained by swapping the "
                     "jobs in positions `i` and `i + 1` and leaving everything else "
                     "alone. It is <strong>improving</strong> for an objective when "
                     "the swapped order has a strictly smaller value.")),
            ("p", "Adjacent is the load-bearing word. An arbitrary transposition moves "
                  "every completion time between the two jobs and gives a difference "
                  "with a sum in it; an adjacent one moves exactly two, and the "
                  "difference collapses to a single subtraction that does not mention "
                  "the rest of the schedule."),
            ("thm", ("The exchange identity for total completion time",
                     "Let `a` and `b` be adjacent, with `a` first, and let the pair "
                     "begin at time `t`. Swapping them changes `sum C` by exactly "
                     "`p_b − p_a`, whatever `t` is and whatever the rest of the order "
                     "is.")),
            ("proof", ["Only `C_a` and `C_b` change: every earlier job is untouched, "
                       "and every later job starts when the same two jobs have been "
                       "done, so it starts and finishes at the same clock as before.",
                       "Before: `C_a = t + p_a` and `C_b = t + p_a + p_b`, summing to "
                       "`2t + 2p_a + p_b`. After: `C_b = t + p_b` and "
                       "`C_a = t + p_b + p_a`, summing to `2t + 2p_b + p_a`.",
                       "Subtract: the change is `(2p_b + p_a) − (2p_a + p_b) = "
                       "p_b − p_a`. No term involving `t` or any other job survives."]),
            ("p", "Read the sign. The change is negative exactly when `p_b < p_a`, "
                  "that is, exactly when the shorter job was behind the longer one. So "
                  "any order containing an adjacent pair in the wrong length order can "
                  "be strictly improved by one swap, and an order that cannot be "
                  "improved by any adjacent swap has no such pair &mdash; which is to "
                  "say it is sorted by processing time ascending."),
            ("h3", "Shortest processing time, and what the theorem actually says"),
            ("def", ("The SPT rule",
                     "The <strong>shortest processing time</strong> rule orders the "
                     "jobs by `p` ascending, breaking ties arbitrarily. Every tie-"
                     "break gives the same `sum C`, because swapping two jobs with "
                     "equal `p` moves `sum C` by `p_b − p_a = 0`.")),
            ("p", "The theorem is that SPT minimises `sum C`, and nothing more. It "
                  "says nothing about weights, nothing about due dates, and nothing "
                  "about the makespan, which does not move. It also says nothing about "
                  "the individual jobs: shortest-first is the rule that makes the "
                  "longest job wait the longest, which is exactly what minimising an "
                  "unweighted total of finish times asks for."),
            ("math", [
                "jobs      A 9,  B 2,  C 6,  D 3,  E 5          total work 25",
                "",
                "  LPT     A C E D B       C = 9 15 20 23 25     sum C 92",
                "  FCFS    A B C D E       C = 9 11 17 20 25     sum C 82",
                "  SPT     B D E C A       C = 2  5 10 16 25     sum C 58",
                "",
                "  best of all 120 orders  58,  attained by B D E C A alone",
                "  makespan 25 in every one of them",
            ]),
            ("h3", "Ten swaps, and the walk that stops on its own"),
            ("p", "The lab starts from the worst order there is and repeatedly takes "
                  "the first adjacent swap that improves `sum C`, printing the exact "
                  "quantity each one moved. It is never told what SPT is. On this "
                  "instance it takes ten swaps and then stops, and where it stops is "
                  "the sorted order:"),
            ("math", [
                "start   A C E D B    sum C 92",
                "   1    swap A,C     p_C − p_A =  6 − 9 =  −3        89",
                "   2    swap A,E     p_E − p_A =  5 − 9 =  −4        85",
                "   3    swap C,E     p_E − p_C =  5 − 6 =  −1        84",
                "   4    swap A,D     p_D − p_A =  3 − 9 =  −6        78",
                "   5    swap C,D     p_D − p_C =  3 − 6 =  −3        75",
                "   6    swap E,D     p_D − p_E =  3 − 5 =  −2        73",
                "   7    swap A,B     p_B − p_A =  2 − 9 =  −7        66",
                "   8    swap C,B     p_B − p_C =  2 − 6 =  −4        62",
                "   9    swap E,B     p_B − p_E =  2 − 5 =  −3        59",
                "  10    swap D,B     p_B − p_D =  2 − 3 =  −1        58",
                "",
                "stop    B D E C A    sum C 58        total moved  −34",
            ]),
            ("p", "Ten swaps is not a bound and not an estimate; it is the count on "
                  "this instance, and it is the number of pairs in a five-job order, "
                  "because the starting order was the exact reverse of the finishing "
                  "one. The second preset starts one swap away from sorted and takes "
                  "two, not one: swapping the out-of-order pair puts a new out-of-order "
                  "pair next to each other. Watching that happen is worth more than "
                  "being told that greedy local improvement is subtle."),
            ("p", "What the walk demonstrates and the theorem proves are two different "
                  "things, and it is worth being clear about which is which. The walk "
                  "shows that on this instance improving swaps exist until the order is "
                  "sorted. The theorem shows that on <em>every</em> instance an "
                  "unsorted order has an improving swap, so no unsorted order can be "
                  "optimal. The lab then checks the conclusion a third way, against all "
                  "120 orders, and reports `58` from the enumeration as well."),
        ],
        "lab": ("schedule", {
            "mode": "spt",
            "preset": "worst",
            "panel_title": "Swap two neighbours, and watch the walk from the worst order to the best",
            "panel_intro": "The slider picks a position and swaps that job with the "
                           "next one. The panel prints the objective before, the "
                           "objective after, and the exact quantity the swap moved "
                           "&mdash; checked against a full recomputation of both "
                           "schedules, so the claim that nothing else changed is "
                           "tested rather than asserted. It also counts the improving "
                           "swaps from here to the rule's own order.",
        }),
        "steps_title": "Proving a sequencing rule by exchange",
        "steps_intro": "Four steps, and the third one is where a wrong rule dies.",
        "steps": [
            ("Take two jobs that are next to each other, and give the pair a start time",
             "Call them `a` then `b`, starting at `t`. Do not choose a position and do "
             "not choose an instance: the argument has to work at every position in "
             "every order, and it will, because `t` cancels."),
            ("Write both schedules' completion times and subtract",
             "Only the two swapped jobs move, so the difference is "
             "`(w_a C_a + w_b C_b)` after minus the same before. For `sum C` that is "
             "`p_b − p_a`; for a different objective it is a different subtraction, and "
             "the rest of the argument is unchanged."),
            ("Read off the condition under which the swap improves",
             "`p_b − p_a < 0` exactly when `p_b < p_a`. That condition is the rule: "
             "keep the smaller `p` in front. If your condition depends on `t` or on "
             "another job, the objective does not have an exchange rule and the "
             "argument stops here rather than being patched."),
            ("Conclude by contradiction, then check the conclusion",
             "Any order violating the condition on some adjacent pair is improvable, so "
             "it is not optimal; the orders that violate it nowhere are the sorted ones. "
             "Then run the enumeration on a small instance anyway. A proof and a "
             "measurement that agree are worth more than either alone, and the lab "
             "prints both."),
        ],
        "worked": {
            "title": "The worst order there is, improved ten times",
            "intro": [
                "The lab's opening preset, with the subtraction written out at every "
                "step. The instance is five jobs whose longest is nine hours long, "
                "started in the order that makes everything wait behind it.",
            ],
            "lines": [
                "jobs   A 9,  B 2,  C 6,  D 3,  E 5",
                "",
                "TYPED / LPT   A C E D B",
                "  C            9  15  20  23  25          sum C 92",
                "  every job waits behind the nine-hour one",
                "",
                "THE SWAP IDENTITY, at position 1",
                "  a = A (9), b = C (6), the pair starts at t = 0",
                "  before   C_A = 0 + 9 = 9    C_C = 0 + 9 + 6 = 15     sum of the two 24",
                "  after    C_C = 0 + 6 = 6    C_A = 0 + 6 + 9 = 15     sum of the two 21",
                "  moved    21 − 24 = −3   =   p_C − p_A = 6 − 9",
                "  and C_E, C_D, C_B are 20, 23, 25 before AND after",
                "",
                "THE WALK,  taking the first improving swap each time",
                "  92  −3  89  −4  85  −1  84  −6  78  −3  75",
                "  −2  73  −7  66  −4  62  −3  59  −1  58",
                "  ten swaps, total −34, ending at  B D E C A",
                "",
                "SPT       B D E C A",
                "  C            2   5  10  16  25          sum C 58",
                "  best of all 120 orders  58          makespan 25, unchanged throughout",
            ],
            "after": [
                "The `−3` at position 1 is the whole lesson in one line. Two completion "
                "times changed, `9` and `15` became `6` and `15`, and the three jobs "
                "after the pair finished at `20`, `23` and `25` both before and after. "
                "The lab recomputes all five completion times on both schedules and "
                "confirms it rather than asking you to believe it.",
                "Notice that the walk never goes uphill and never needs to. Greedy "
                "local improvement solves this problem exactly, which is unusual and is "
                "a consequence of the identity: there is no order with an out-of-order "
                "pair that is nonetheless optimal, so there is nowhere for a local "
                "search to get stuck.",
                "For a rehearsal, switch to the preset where only one adjacent pair is "
                "out of order and predict the number of swaps before running it. The "
                "supplied first move is that the typed order `A B C D E` has "
                "`p = 2, 3, 7, 5, 6`, so the only inverted adjacent pair is `C, D`. The "
                "answer is not one swap. Say why, and by how much each of the swaps "
                "moves `sum C`, before the panel tells you.",
            ],
        },
        "quiz_title": "Swaps, subtractions and what they prove",
        "quiz": [
            {"q": "Two adjacent jobs `a` then `b` start at time `t`. By how much does swapping them change `sum C`?",
             "a": ["`p_b − p_a`", "`t + p_b − p_a`", "`p_a − p_b`", "`2(p_b − p_a)`"],
             "c": 0,
             "why": "The two completion times go from `t + p_a` and `t + p_a + p_b` to "
                    "`t + p_b` and `t + p_b + p_a`. The second is the same in both, so "
                    "the difference is `(t + p_b) − (t + p_a) = p_b − p_a`, and `t` "
                    "cancels. The third choice has the sign backwards, which reverses "
                    "the rule it proves."},
            {"q": "Why does the argument use adjacent jobs rather than any two jobs?",
             "a": ["Because non-adjacent jobs cannot be swapped without reordering the rest",
                   "Because swapping two jobs that are not adjacent also moves every completion time between them, so the difference is a sum rather than one subtraction",
                   "Because the makespan would change",
                   "Because the rule only ever compares neighbours"],
             "c": 1,
             "why": "Any two jobs can be swapped. The point is what it costs to compute: "
                    "an adjacent swap moves exactly two completion times, so the "
                    "difference collapses to `p_b − p_a`; a distant swap moves every job "
                    "in between as well. The local version is enough for the proof, "
                    "which is why it is the one used."},
            {"q": "An order has no adjacent pair whose swap improves `sum C`. What follows?",
             "a": ["Nothing, since local optimality does not imply global optimality",
                   "That it is one swap away from the optimum",
                   "That it is sorted by `p` ascending, and is therefore optimal for `sum C`",
                   "That every pair has equal processing times"],
             "c": 2,
             "why": "No improving adjacent swap means no adjacent pair has the longer "
                    "job first, which means the order is sorted. Since any unsorted "
                    "order is improvable and therefore not optimal, the sorted ones are "
                    "the optima. The first choice is the right instinct for most "
                    "problems and is refuted here by the identity itself."},
            {"q": "The lab walks from the worst order to the shortest-first order in ten improving swaps. What is that ten?",
             "a": ["A bound on how many swaps any instance needs",
                   "The measured count on this instance, which started as the exact reverse of the sorted order",
                   "The number of jobs times two",
                   "Proof that greedy improvement always terminates in `n(n−1)/2` swaps"],
             "c": 1,
             "why": "It is a measurement, not a bound. This instance begins reversed, so "
                    "every one of the ten pairs is out of order. The second preset "
                    "begins with a single inverted adjacent pair and still takes two "
                    "swaps, because fixing one pair can create another."},
        ],
        "mistakes": [
            ("Getting the sign of the subtraction backwards",
             "The change is `p_b − p_a` with `a` in front, so it is negative when the "
             "job behind is shorter. Write it as `after minus before` every time and "
             "keep the order of the letters straight; the reversed version proves "
             "longest-first, which costs `92` where `58` is available on the lab's "
             "instance."),
            ("Believing the identity holds for a distant swap",
             "Exchange the first and last of five jobs and three completion times in "
             "between move as well. The difference is then a sum over the jobs "
             "straddled, not one subtraction, and it depends on their processing times. "
             "Every proof on this course exchanges neighbours for exactly this reason."),
            ("Reporting the walk as the proof",
             "Ten improving swaps on one instance show that this order was not optimal. "
             "They do not show that no unsorted order anywhere is optimal &mdash; that "
             "is the identity, applied to an arbitrary pair at an arbitrary position. "
             "The walk is how the argument is watched; it is not the argument."),
        ],
        "standard": ("Finish when you can prove shortest-first optimal in four lines without looking anything up.",
                     "You should be able to set up an adjacent pair with a symbolic "
                     "start time, write both schedules' completion times, subtract to "
                     "get `p_b − p_a`, say why no other job appears in the difference, "
                     "read the improvement condition off the sign, and finish the "
                     "argument by observing that the orders with no improving swap are "
                     "exactly the sorted ones."),
        "note": 'The identity never mentioned the weights, because this objective has none. Put one on each job and rerun the same three lines: the difference becomes `w_a p_b − w_b p_a`, which is negative under a condition that is no longer &ldquo;the shorter job goes first&rdquo;. &ldquo;Smith&rsquo;s Rule and Weighted Completion Time&rdquo; runs that subtraction, and the rule it produces beats the obvious rival by a measured amount.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "smiths-rule-and-weighted-completion-time",
        "title": "Smith's Rule and Weighted Completion Time",
        "module": "The adjacent exchange",
        "one_line": "Put a weight on each job, run the same exchange, and the ordering key becomes the ratio p/w rather than either number on its own.",
        "summary": (
            "The same swap, with weights on, moves `sum w C` by `w_a p_b − w_b p_a`. "
            "That is negative exactly when `p_a / w_a > p_b / w_b`, so the ordering key "
            "is the ratio and not the time and not the weight. The two rules that use "
            "one number each are both wrong, and on the lab's instance running the "
            "heaviest job first costs `113` where the ratio reaches `97`."
        ),
        "key": [
            "swap adjacent a then b:   sum w C moves by  w_a p_b − w_b p_a",
            "negative  ⟺  w_a p_b < w_b p_a  ⟺  p_a / w_a > p_b / w_b",
            "WSPT (Smith): sort by p/w ASCENDING       ties give the same sum w C",
            "A 3:1, B 8:4, C 2:3, D 6:2   ratios 3, 2, 2/3, 3",
            "WSPT C B A D 97   heaviest-first B C D A 113   shortest-first C A D B 109",
            "equal weights ⟹ p/w is p rescaled ⟹ Smith’s rule collapses to SPT",
        ],
        "key_label": "The same exchange, one multiplication heavier",
        "concepts_intro": (
            "One new subtraction and two corollaries, one of which is that the two "
            "rules a reader would guess are both beaten on the same instance."
        ),
        "concepts": [
            ("The weighted swap is the unweighted swap with two multiplications",
             "Only `C_a` and `C_b` move, exactly as before, so the change in `sum w C` "
             "is `w_a C_a + w_b C_b` after minus before. Substituting the four "
             "completion times and cancelling the start time gives "
             "`w_a p_b − w_b p_a`. Nothing about the derivation changed; the objective "
             "put a multiplier on each term and the multiplier survived into the "
             "answer."),
            ("The condition is a ratio, so neither number decides alone",
             "`w_a p_b < w_b p_a` divides through by `w_a w_b`, which is positive, to "
             "give `p_a / w_a < p_b / w_b`. So the swap improves exactly when the job "
             "in front has the <em>larger</em> ratio, and the rule is to sort by `p/w` "
             "ascending. A long heavy job and a short light job can have the same "
             "ratio, in which case the order between them does not matter at all: the "
             "difference is exactly zero."),
            ("Both one-number rules lose, and they lose differently",
             "Heaviest-weight-first ignores `p` and puts an eight-hour job at the front "
             "because it is worth four; shortest-first ignores `w` and puts a nearly "
             "worthless job at the front because it takes two hours. On the lab's "
             "instance they cost `113` and `109` against the ratio's `97`. Neither is "
             "a silly rule; each is a correct rule for a question nobody asked."),
        ],
        "read_title": "Weights, the ratio, and two plausible rules that lose",
        "read_intro": "The subtraction with weights in it, the rule it produces, and a measured comparison against the two rules a reader would reach for first.",
        "body": [
            ("def", ("Weighted completion time",
                     "Each job carries a positive <strong>weight</strong> `w_j`, and "
                     "the objective is `sum w C = sum over j of w_j C_j`. The weight "
                     "is the cost of one unit of waiting for that job: twice the "
                     "weight means an hour of delay hurts twice as much. Weights are "
                     "not priorities and they are not ranks &mdash; they are "
                     "multipliers, and the arithmetic uses their sizes.")),
            ("thm", ("The weighted exchange identity",
                     "Let `a` and `b` be adjacent with `a` first. Swapping them "
                     "changes `sum w C` by exactly `w_a p_b − w_b p_a`, whatever the "
                     "start time and whatever the rest of the order.")),
            ("proof", ["Only `C_a` and `C_b` change, for the same reason as in the "
                       "unweighted case: earlier jobs are untouched, and later jobs "
                       "start once the same two jobs have been done.",
                       "Let the pair start at `t`. Before, the two contribute "
                       "`w_a(t + p_a) + w_b(t + p_a + p_b)`. After, they contribute "
                       "`w_b(t + p_b) + w_a(t + p_b + p_a)`.",
                       "Subtracting, every term in `t` cancels, `w_a p_a` cancels "
                       "against itself and `w_b p_b` against itself, and what is left "
                       "is `w_a p_b − w_b p_a`."]),
            ("p", "Divide the improvement condition `w_a p_b − w_b p_a < 0` by the "
                  "positive quantity `w_a w_b` and it becomes `p_a / w_a > p_b / w_b`. "
                  "This is why the weights must be strictly positive and why the lab "
                  "refuses a weight of zero rather than accepting it: the ratio is a "
                  "division, and a job of no weight at all is a job whose position "
                  "cannot be argued about by this method."),
            ("def", ("Smith's rule",
                     "The <strong>weighted shortest processing time</strong> rule, or "
                     "<strong>Smith's rule</strong>, orders the jobs by `p / w` "
                     "ascending. It minimises `sum w C`. With all the weights equal it "
                     "is `p` divided by a constant, so it is shortest-first again "
                     "&mdash; the unweighted theorem is the special case, not a "
                     "separate result.")),
            ("h3", "Four jobs, three rules, and two of them wrong"),
            ("math", [
                "jobs    A 3:1   B 8:4   C 2:3   D 6:2         p:w",
                "ratios  A 3     B 2     C 2/3   D 3",
                "",
                "  typed    A B C D    sum wC 124",
                "  WEIGHT   B C D A    sum wC 113      heaviest weight first",
                "  SPT      C A D B    sum wC 109      shortest time first",
                "  WSPT     C B A D    sum wC  97      the ratio",
                "",
                "  best of all 24 orders   97        attained twice: C B A D and C B D A",
                "  makespan 19 in every one of them",
            ]),
            ("p", "`B` is both the longest job and the heaviest, which is what makes "
                  "the instance worth looking at: the two one-number rules disagree "
                  "about it as loudly as they can. Heaviest-first puts `B` at the very "
                  "front, where its eight hours delay everything else. Shortest-first "
                  "puts it at the very back, where four units of weight wait the whole "
                  "nineteen hours. The ratio puts it second, and the `97` is not "
                  "available any other way."),
            ("example", ("The one swap that separates the two rules",
                         "Heaviest-first produces `B C D A`. The ratio of `B` is `2` "
                         "and the ratio of `C` is `2/3`, so the pair at the front is "
                         "out of order and the identity says the swap moves "
                         "`w_B p_C − w_C p_B = 4 × 2 − 3 × 8 = 8 − 24 = −16`.",
                         "Make that one swap and the order becomes `C B D A`, worth "
                         "`113 − 16 = 97`, which is optimal. So the entire gap between "
                         "the rival rule and the theorem on this instance is one "
                         "adjacent pair, and the exact size of the gap was available "
                         "from two multiplications before the swap was made.")),
            ("h3", "Where the walk from the typed order goes"),
            ("math", [
                "start   A B C D    sum wC 124",
                "   1     swap A,B   w_A p_B − w_B p_A = 1(8) − 4(3) =  −4     120",
                "   2     swap A,C   w_A p_C − w_C p_A = 1(2) − 3(3) =  −7     113",
                "   3     swap B,C   w_B p_C − w_C p_B = 4(2) − 3(8) = −16      97",
                "",
                "stop    C B A D    sum wC 97      Smith’s own order",
                "",
                "the finished schedule, job by job",
                "        C   p 2  w 3   C  2    wC   6",
                "        B   p 8  w 4   C 10    wC  40",
                "        A   p 3  w 1   C 13    wC  13",
                "        D   p 6  w 2   C 19    wC  38",
                "                                   97",
            ]),
            ("p", "Three swaps, three subtractions, and the walk stops on Smith's order "
                  "without ever having been told what Smith's rule is. That is the "
                  "same demonstration as in the unweighted case with one difference "
                  "worth noticing: the largest single improvement, `−16`, came last. "
                  "There is no reason for the improvements to get smaller, and a reader "
                  "who stops swapping because the gains look small has stopped early."),
            ("p", "The unweighted rule is not merely analogous to this one; it is this "
                  "one. Set every weight to the same value `w` and the ratio `p/w` "
                  "orders the jobs exactly as `p` does, so Smith's rule returns the "
                  "shortest-first order and `sum w C = w sum C` is minimised by "
                  "minimising `sum C`. The lab has a preset with four equal weights for "
                  "exactly this check, and the two rules return the same order on it."),
            ("p", "One warning about the ratio, because it is the kind of thing that "
                  "survives into practice as folklore. `p/w` is an ordering key and "
                  "nothing else. It is not a cost, it is not a priority score to be "
                  "compared across instances, and adding the ratios up or averaging "
                  "them computes nothing. The only fact about it is that sorting by it "
                  "ascending minimises `sum w C`."),
        ],
        "lab": ("schedule", {
            "mode": "wspt",
            "preset": "ratio",
            "panel_title": "Weight the jobs, swap two neighbours, and watch the ratio decide",
            "panel_intro": "The same exchange with weights on. The panel prints the "
                           "two ratios beside the swap, the exact quantity "
                           "`w_a p_b − w_b p_a` that it moved, and a full "
                           "recomputation of both schedules to show that nothing else "
                           "did. Fill the order from heaviest-weight-first and from "
                           "shortest-first to see both rivals lose on the same data.",
        }),
        "steps_title": "Sequencing when the jobs are not worth the same",
        "steps_intro": "Four steps, and the second is the one that separates this rule from the two that look like it.",
        "steps": [
            ("Write each job as time and weight, and say what the weight means",
             "`p:w`, with `w` the cost of one unit of waiting. If you cannot say what a "
             "weight of `4` means relative to a weight of `1` in the units of the "
             "problem, the model is not finished and no rule will finish it for you."),
            ("Compute `p/w` for every job, exactly",
             "As a fraction. `2/3` and `2` and `3` are the keys on the lab's instance, "
             "and two jobs there tie at `3`. Rounding the ratios to decimals is how a "
             "genuine tie becomes a fictitious ordering, and on a tie the exchange "
             "identity says the order genuinely does not matter."),
            ("Sort ascending by the ratio, not by either number",
             "Smallest ratio first. Checking one pair by hand is worth the seconds it "
             "takes: on the lab's instance `C` has ratio `2/3` and `B` has `2`, so `C` "
             "goes first even though `B` is four times the weight."),
            ("Check the result against the rival you were going to use",
             "Run heaviest-weight-first on the same jobs and compute `sum w C` for "
             "both. On the lab's instance that is `113` against `97`, and the "
             "difference is the number worth carrying into the argument about whether "
             "the rule is worth changing."),
        ],
        "worked": {
            "title": "Four jobs where the heaviest is also the longest",
            "intro": [
                "The lab's opening preset. `B` is eight hours long and worth four, so "
                "the two one-number rules put it at opposite ends of the schedule and "
                "the ratio puts it in the middle.",
            ],
            "lines": [
                "jobs     A 3:1    B 8:4    C 2:3    D 6:2",
                "ratios   A 3      B 2      C 2/3    D 3",
                "",
                "SMITH’S ORDER, by ratio ascending      C (2/3), B (2), A (3), D (3)",
                "         job   p   w    C    wC",
                "          C    2   3    2     6",
                "          B    8   4   10    40",
                "          A    3   1   13    13",
                "          D    6   2   19    38",
                "                            97",
                "  A and D tie at 3, so C B D A is also worth 97 — 2 of the 24 orders attain it",
                "",
                "HEAVIEST WEIGHT FIRST    B C D A     sum wC 113",
                "  one swap at the front:  w_B p_C − w_C p_B = 4(2) − 3(8) = −16",
                "  113 − 16 = 97, and the order is C B D A",
                "",
                "SHORTEST TIME FIRST      C A D B     sum wC 109     (sum C 37, which IS optimal)",
                "",
                "THE WALK FROM THE TYPED ORDER  A B C D, worth 124",
                "  swap A,B   1(8) − 4(3) =  −4    120",
                "  swap A,C   1(2) − 3(3) =  −7    113",
                "  swap B,C   4(2) − 3(8) = −16     97      three swaps, and it stops",
            ],
            "after": [
                "The line to keep is the one about shortest-first: it attains `sum C = "
                "37`, which is the true optimum for the unweighted objective, and it "
                "costs `109` on the weighted one. A rule can be exactly, provably "
                "optimal and be the wrong rule, and there is nothing in its output that "
                "reveals which of the two it is being.",
                "The tie between `A` and `D` at ratio `3` is worth checking by hand. "
                "`A` is `3:1` and `D` is `6:2`; the swap moves "
                "`w_A p_D − w_D p_A = 1(6) − 2(3) = 0`. Two of the twenty-four orders "
                "attain `97`, and the lab reports the count rather than naming one "
                "order and implying it is unique.",
                "For a rehearsal, type the five jobs of &ldquo;One Machine, Six "
                "Objectives&rdquo; in as `p:w` &mdash; "
                "`A 6:1, B 4:2, C 5:4, D 3:3, E 7:1` &mdash; and work out the three "
                "figures before the panel does. The supplied first move is that the "
                "ratios are `6, 2, 5/4, 1, 7`. Smith's rule gives `108`, heaviest-first "
                "gives `111` and shortest-first gives `114`; one adjacent swap "
                "separates the shortest-first order from Smith's, and it is worth `−6`.",
            ],
        },
        "quiz_title": "Ratios, rivals and the weighted subtraction",
        "quiz": [
            {"q": "Swapping adjacent jobs `a` then `b` changes `sum w C` by which quantity?",
             "a": ["`w_b p_b − w_a p_a`", "`w_a p_b − w_b p_a`", "`p_b/w_b − p_a/w_a`",
                   "`(w_a + w_b)(p_b − p_a)`"],
             "c": 1,
             "why": "Substituting the four completion times and cancelling gives "
                    "`w_a p_b − w_b p_a`. The third choice has the right <em>sign "
                    "behaviour</em> &mdash; it is negative under the same condition "
                    "&mdash; but it is not the amount moved, and the lab prints the "
                    "amount: `−16` on the front pair of the heaviest-first order, not "
                    "`2/3 − 2`."},
            {"q": "On the lab's instance `B` is `8:4` and `C` is `2:3`. Which goes first under Smith's rule, and why?",
             "a": ["`B`, because its weight of `4` is the largest",
                   "`C`, because two hours is shorter than eight",
                   "`C`, because its ratio `2/3` is smaller than `B`'s ratio `2`",
                   "Either, because the ratios are not comparable"],
             "c": 2,
             "why": "The rule sorts on `p/w` ascending and `2/3 < 2`. The second choice "
                    "reaches the right answer by the wrong route and fails elsewhere on "
                    "the same instance: `A` is shorter than `D` and `B` is longer than "
                    "both, yet `B` comes second, ahead of both of them."},
            {"q": "All the weights on an instance are equal to `5`. What does Smith's rule return?",
             "a": ["The shortest-first order, since `p/5` sorts exactly as `p` does",
                   "The heaviest-first order, since every job is heaviest",
                   "The order typed, since the ratios carry no information",
                   "A different order, because `sum w C` is five times `sum C`"],
             "c": 0,
             "why": "Dividing every key by the same positive constant does not change "
                    "the sort, so Smith's rule is shortest-first and `sum w C = 5 sum "
                    "C` is minimised by minimising `sum C`. The unweighted theorem is "
                    "this one's special case, and the lab has a preset with four equal "
                    "weights that shows the two rules returning the same order."},
            {"q": "Heaviest-weight-first costs `113` on the lab's instance where Smith's rule costs `97`. What is the right conclusion?",
             "a": ["That heaviest-first is within `17%` of optimal in general",
                   "That heaviest-first happens to be beaten here, and the exchange identity says why: its front pair has the larger ratio first, worth `−16`",
                   "That heaviest-first never attains the optimum",
                   "That the weights on this instance are badly scaled"],
             "c": 1,
             "why": "The gap is a measurement on one instance, and the identity accounts "
                    "for all of it: one adjacent swap worth `−16` takes `113` to `97`. "
                    "Nothing here bounds the rule's error in general, and a rival rule "
                    "can attain the optimum on some instances &mdash; with equal "
                    "weights, heaviest-first is an arbitrary order and may be any of "
                    "them."},
        ],
        "mistakes": [
            ("Sorting by the weight, or by the time, and calling it a priority rule",
             "Each ignores half of the data. On the lab's instance heaviest-first costs "
             "`113` and shortest-first `109` where `97` is available, and shortest-first "
             "is simultaneously optimal for the unweighted objective. The ratio is not a "
             "compromise between the two rules; it is the condition the subtraction "
             "produced."),
            ("Rounding the ratios",
             "`2/3`, `2`, `3` and `3` are exact. Two jobs tie here and the identity says "
             "their order moves `sum w C` by exactly zero; a decimal ratio invents a "
             "difference between them and hides the fact that two of the twenty-four "
             "orders attain the optimum. Every figure on this path is a fraction for "
             "reasons of exactly this kind."),
            ("Treating `p/w` as a score with meaning of its own",
             "It is an ordering key. Adding the ratios, averaging them, comparing them "
             "between instances or reporting one as a job's priority computes nothing. "
             "The only theorem is that sorting ascending by it minimises `sum w C`, and "
             "it says nothing about any other objective &mdash; Smith's order costs `66` "
             "on `sum C` where `65` was available on the instance of &ldquo;One "
             "Machine, Six Objectives&rdquo;."),
        ],
        "standard": ("Finish when you can derive the ratio rule from the swap rather than recalling it.",
                     "You should be able to run the adjacent exchange with weights, "
                     "reach `w_a p_b − w_b p_a`, divide by `w_a w_b` to turn the "
                     "improvement condition into `p_a/w_a > p_b/w_b`, state Smith's rule, "
                     "show that equal weights reduce it to shortest-first, and compute "
                     "by how much a named rival rule loses on a given instance rather "
                     "than asserting that it does."),
        "note": 'Both rules so far minimise a total, and a total is forgiving: one job finishing very late can be paid for by four finishing early. Due dates are not like that. The next objective takes a maximum rather than a sum, so one bad job sets the whole figure, and the exchange argument that proves the rule for it has to compare two maxima rather than two sums. &ldquo;Earliest Due Date and Maximum Lateness&rdquo; runs it, and then shows the same order losing on the objective a reader will assume it also solves.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "earliest-due-date-and-maximum-lateness",
        "title": "Earliest Due Date and Maximum Lateness",
        "module": "Due dates, and which question you asked",
        "one_line": "Earliest-due-date minimises the worst lateness, by the same exchange; on the same five jobs it is beaten on total tardiness and leaves twice as many jobs late as it needs to.",
        "summary": (
            "Sorting by due date minimises maximum lateness, and the proof is the "
            "adjacent exchange with a maximum in place of a sum. It is the most useful "
            "rule on the course and the most over-claimed: on the lab's five jobs it "
            "attains `L max = 6`, which is optimal, while costing `17` of total "
            "tardiness where `16` exists and leaving `4` jobs late where `2` is "
            "possible. Three due-date objectives, one rule, and it answers one of them."
        ),
        "key": [
            "L_j = C_j − d_j  (may be negative)      T_j = max(L_j, 0)      U_j = 1 if late",
            "L max = max L_j        T max = max T_j        sum T          sum U",
            "EDD: sort by d ascending.  Minimises L max, and minimises T max",
            "the exchange: swapping an out-of-order pair cannot raise the larger of two latenesses",
            "A 6:8, B 4:4, C 5:12, D 3:6, E 7:20:  EDD B D A C E, L max 6 — optimal",
            "same order, sum T 17 where 16 exists;  4 jobs late where 2 is possible",
        ],
        "key_label": "One rule, four due-date objectives, and one of them answered",
        "concepts_intro": (
            "The rule and its proof are short. The two ideas that take work are what "
            "the proof does not cover, and why the objective it does cover is the one "
            "with a maximum in it."
        ),
        "concepts": [
            ("A maximum is not a sum, and the exchange handles it differently",
             "For `sum C` the swap produced a difference. For `L max` it produces an "
             "inequality: after swapping an out-of-order adjacent pair, the later-due "
             "job finishes earlier than it did, and the earlier-due job finishes no "
             "later than the pair finished before. So the larger of the two latenesses "
             "cannot have gone up, and since no other job moved, `L max` cannot have "
             "gone up. That is enough &mdash; optimality needs an argument that the "
             "swap never hurts, not one that it always helps."),
            ("Minimising the worst is not minimising the total",
             "`L max` is decided by one job; `sum T` is paid by all of them. Making the "
             "worst job less bad routinely means making several others worse, and the "
             "lab's instance is exactly that: EDD gives latenesses `0, 1, 5, 6, 5` for "
             "a maximum of `6` and a total tardiness of `17`, while the order that "
             "attains `16` has a maximum of `10`. Neither order dominates the other, "
             "and no rule reconciles them because they are different questions."),
            ("Total tardiness is where the exchange argument stops",
             "`1 || sum T` has no exchange rule, and this course does not invent one. "
             "Swapping an adjacent pair changes the tardiness of both jobs by amounts "
             "that depend on where the due dates sit relative to the clock, so the "
             "difference does not collapse to a subtraction on the two jobs alone. The "
             "lab exhibits the optimum by enumeration and names the boundary, which is "
             "more useful than a plausible-looking heuristic."),
        ],
        "read_title": "Sorting by due date, what it proves, and the three things it does not",
        "read_intro": "The four due-date objectives, the exchange argument for the one with a maximum in it, and the same order measured on the other three.",
        "body": [
            ("def", ("Lateness, tardiness, and the four objectives",
                     "For a job finishing at `C_j` with due date `d_j`, the "
                     "<strong>lateness</strong> is `L_j = C_j − d_j` and may be "
                     "negative; the <strong>tardiness</strong> is "
                     "`T_j = max(L_j, 0)` and may not; and `U_j` is `1` when "
                     "`C_j > d_j`.",
                     "The four objectives are `L max` (the worst lateness, which can be "
                     "negative if everything finishes early), `T max` (the worst "
                     "tardiness, which cannot), `sum T` (total tardiness) and `sum U` "
                     "(the number of late jobs). They are four questions, not four "
                     "spellings of one.")),
            ("thm", ("Earliest due date minimises maximum lateness",
                     "Ordering the jobs by `d` ascending minimises `L max`, and it "
                     "also minimises `T max`.")),
            ("proof", ["Take any order and any adjacent pair `a` then `b` with "
                       "`d_a > d_b`, starting at time `t` and finishing at "
                       "`t + p_a + p_b`. Before the swap the two latenesses are "
                       "`t + p_a − d_a` and `t + p_a + p_b − d_b`; the larger of the "
                       "two is at least the second one.",
                       "After the swap they are `t + p_b − d_b` and "
                       "`t + p_b + p_a − d_a`. The first of these is smaller than "
                       "`t + p_a + p_b − d_b` because `p_b < p_a + p_b`; the second is "
                       "smaller than `t + p_a + p_b − d_b` because `d_a > d_b`. So "
                       "both new latenesses are below the old maximum of the pair.",
                       "No other job moved, so `L max` over the whole schedule did not "
                       "increase. Repeating on any remaining out-of-order pair reaches "
                       "the due-date order without ever increasing `L max`, so that "
                       "order attains the minimum. `T max` is `max(L max, 0)`, so the "
                       "same order minimises it."]),
            ("p", "Notice what shape that argument has. The unweighted case gave an "
                  "identity and a strict improvement; this one gives only that the swap "
                  "does no harm. That is the normal situation for a maximum, and it is "
                  "enough: a sequence of harmless swaps reaching the rule's order shows "
                  "the rule's order is at least as good as where you started, whatever "
                  "that was."),
            ("h3", "The rule, on five jobs, doing exactly what it promises"),
            ("math", [
                "jobs     A 6:8   B 4:4   C 5:12   D 3:6   E 7:20        p:d",
                "",
                "EDD      B D A C E",
                "   job     p    d     C     L     T",
                "    B      4    4     4     0     0",
                "    D      3    6     7     1     1   late",
                "    A      6    8    13     5     5   late",
                "    C      5   12    18     6     6   late",
                "    E      7   20    25     5     5   late",
                "",
                "   L max 6      T max 6      sum T 17      late 4 of 5",
                "   best L max over all 120 orders: 6           EDD attains it",
                "   best T max over all 120 orders: 6           EDD attains it",
            ]),
            ("p", "`L max = 6` is set by `C`, which finishes at `18` against a due date "
                  "of `12`. Seventeen hours of work are due by hour twelve and twenty-"
                  "five hours of work exist, so something has to be late; the rule's "
                  "achievement is that nothing is more than six hours late, and the "
                  "enumeration confirms that no order does better."),
            ("h3", "The same order, on the objective it does not solve"),
            ("math", [
                "EDD          B D A C E    T = 0, 1, 5, 6, 5      sum T 17    late 4",
                "the best     B D C A E    T = 0, 1, 0, 10, 5     sum T 16    late 3",
                "                          and its L max is 10, not 6",
                "",
                "Moore–Hodgson              late 2, which is the enumerated minimum",
                "best sum T over 120 orders  16      best sum U over 120 orders  2",
            ]),
            ("example", ("Where the extra hour of tardiness went",
                         "The order that attains `sum T = 16` differs from EDD by one "
                         "adjacent swap: `C` and `A` change places. `C` then finishes "
                         "at `12` exactly on its due date and contributes nothing, "
                         "while `A` slides from `13` to `18` and goes from `5` hours "
                         "tardy to `10`.",
                         "Total tardiness falls from `17` to `16` because one job was "
                         "taken from `6` to `0` while another rose by `5`. Maximum "
                         "lateness rises from `6` to `10`, because the worst job is now "
                         "worse. Both orders are optimal &mdash; for different "
                         "objectives &mdash; and choosing between them is a decision "
                         "about whether a schedule is judged on its worst job or on all "
                         "of them.")),
            ("p", "So EDD is optimal for two of the four due-date objectives and beaten "
                  "on the other two: `17` against `16`, and `4` late against `2`. The "
                  "second of those has a rule, and &ldquo;Minimising the Number of Late "
                  "Jobs&rdquo; is it. The first does "
                  "not, and the honest thing is to say so."),
            ("h3", "The boundary, stated rather than worked around"),
            ("p", "`1 || sum T` &mdash; one machine, minimise total tardiness &mdash; "
                  "has no adjacent-exchange rule. Run the argument and see why: "
                  "swapping `a` and `b` changes `T_a` and `T_b`, but each of those "
                  "changes is a clipped quantity, so the amount depends on whether "
                  "`t + p_a` sits above or below `d_a`, and the same swap moves the sum "
                  "by different amounts in different parts of the schedule. There is no "
                  "condition on the pair alone that decides it."),
            ("p", "This is worth dwelling on because it is the one place on the course "
                  "where the technique runs out, and a reader who has seen three rules "
                  "fall out of one subtraction will expect a fourth. The lab's answer is "
                  "to enumerate: it reports `16` and the order that attains it, and says "
                  "that no rule here produced that order. On a larger instance the "
                  "enumeration is not available either, and then the honest report is a "
                  "heuristic value with a bound attached &mdash; which is the shape of "
                  "answer &ldquo;Integer Programming&rdquo; is about."),
            ("p", "One more warning about due dates, and it is about the model rather "
                  "than the rule. A due date here is a number the objective is measured "
                  "against, not a constraint. Nothing in this model refuses to run a "
                  "schedule in which four of five jobs are late; the arithmetic prices "
                  "it. If a date genuinely cannot be missed it is a constraint, the "
                  "problem may be infeasible, and that is a different question from any "
                  "of the four here."),
        ],
        "lab": ("schedule", {
            "mode": "edd",
            "preset": "loses",
            "panel_title": "Order by due date, and watch it win one objective and lose another",
            "panel_intro": "Four rules fill the order box and the panel scores each "
                           "against the enumerated best of every order, on maximum "
                           "lateness and on total tardiness at once. The slider swaps a "
                           "pair you choose and prints both maxima, so the exchange "
                           "argument can be run by hand on the instance it is being "
                           "claimed for.",
        }),
        "steps_title": "Meeting due dates, and saying which promise you kept",
        "steps_intro": "Five steps, and the fourth stops a true statement being used as a false one.",
        "steps": [
            ("Write the jobs as `p:d` and add the times up",
             "If the total work exceeds the last due date, something is late no matter "
             "what, and knowing that before you start prevents the search for a "
             "schedule that does not exist. On the lab's instance the work is `25` and "
             "the last due date is `20`."),
            ("Sort by due date ascending",
             "Ties in the due dates can be broken arbitrarily for `L max`; the exchange "
             "argument only ever needed `d_a > d_b`, so equal due dates are already in "
             "order either way."),
            ("Build the clock and subtract the due dates, keeping the signs",
             "`L_j = C_j − d_j`, negative for a job that finishes early. `L max` is the "
             "largest of these <em>including</em> the negatives, so a schedule where "
             "everything is early has a negative maximum lateness and that is a "
             "meaningful, useful number."),
            ("Say which objective you have just optimised, and measure the others",
             "You have minimised `L max` and `T max`. You have not minimised `sum T` "
             "and you have not minimised the number of late jobs. Compute both anyway: "
             "on the lab's instance they are `17` and `4`, against `16` and `2`."),
            ("If total tardiness is the objective, stop and say so",
             "There is no exchange rule for it. At this size, enumerate and report the "
             "exact optimum. At any larger size, report a value and a bound, and do not "
             "present a due-date order as though it answered the question."),
        ],
        "worked": {
            "title": "Five jobs, two due-date objectives, and one order that cannot serve both",
            "intro": [
                "The lab's opening preset &mdash; the five jobs of &ldquo;One Machine, "
                "Six Objectives&rdquo; with the "
                "weights dropped and the due dates kept. Every figure is what the panel "
                "reports as the rule selector is moved.",
            ],
            "lines": [
                "jobs    A 6:8   B 4:4   C 5:12   D 3:6   E 7:20",
                "        work 25, last due date 20, so at least one job is late",
                "",
                "EDD, by due date ascending      B (4), D (6), A (8), C (12), E (20)",
                "   job    p    d     C     L     T",
                "    B     4    4     4     0     0",
                "    D     3    6     7     1     1",
                "    A     6    8    13     5     5",
                "    C     5   12    18     6     6",
                "    E     7   20    25     5     5",
                "   L max 6   T max 6   sum T 17   late 4",
                "",
                "THE OTHER RULES, SAME JOBS",
                "   SLACK d − p   B A D C E    L max  7    sum T 20    late 4",
                "   SPT          D B C A E    L max 10    sum T 18    late 3",
                "   FCFS         A B C D E    L max 12    sum T 26    late 4",
                "",
                "THE ENUMERATED OPTIMA, over all 120 orders",
                "   L max  6   attained by EDD",
                "   T max  6   attained by EDD",
                "   sum T 16   attained by B D C A E, which no rule here produces",
                "   sum U  2   attained by 10 of the 120 orders",
                "",
                "   B D C A E:  T = 0, 1, 0, 10, 5     sum T 16   but L max 10",
            ],
            "after": [
                "The two starred orders differ by one adjacent swap and neither "
                "dominates the other. EDD has the smaller worst job and the larger "
                "total; `B D C A E` has the smaller total and a worst job nearly twice "
                "as bad. A report that says &ldquo;we scheduled by due date, so "
                "lateness is minimised&rdquo; is true and is routinely heard as the "
                "other claim.",
                "`SLACK`, ordering by `d − p`, is the rule most often confused with "
                "this one, and it is not the same rule and not optimal for anything "
                "here: `7` against `6` on maximum lateness, and `20` against `17` on "
                "total tardiness. The lab has a preset where the two orders differ, "
                "for exactly this comparison.",
                "For a rehearsal, type `A 5:5, B 4:6, C 6:7, D 2:9` &mdash; four jobs "
                "with seventeen hours of work and a last due date of nine. Predict "
                "before running it whether EDD attains the best `L max`, and what it "
                "costs on total tardiness. The supplied first move is that EDD is the "
                "typed order `A B C D`. It attains `L max = 8`, which is optimal, and "
                "costs `19` on `sum T` where `15` exists &mdash; four worse, on an "
                "instance with only four jobs.",
            ],
        },
        "quiz_title": "Which due-date question a due-date order answers",
        "quiz": [
            {"q": "Why does the exchange argument for `L max` show only that the swap does no harm, rather than that it helps?",
             "a": ["Because `L max` can be negative",
                   "Because the objective is a maximum over all jobs, so a swap that improves the pair may leave the overall maximum unchanged; showing it never rises is enough to reach the rule's order",
                   "Because due dates are not constraints",
                   "Because the swap changes three completion times rather than two"],
             "c": 1,
             "why": "The pair's own maximum strictly falls, but the schedule's maximum "
                    "may be set by some other job entirely. &ldquo;Never rises&rdquo; is "
                    "what the proof needs: a chain of harmless swaps reaches the "
                    "due-date order from any order, so that order is at least as good as "
                    "any."},
            {"q": "EDD attains `L max = 6` on the lab's instance and costs `17` on total tardiness where `16` is available. What does this show?",
             "a": ["That EDD is nearly optimal for total tardiness too",
                   "That the enumeration is finding a different `L max`",
                   "That minimising the worst job and minimising the total are different problems with different optima, and one order cannot attain both here",
                   "That the due dates on this instance are inconsistent"],
             "c": 2,
             "why": "The order attaining `16` has `L max = 10`, so the two optima are "
                    "attained by different orders and neither dominates. `17` against "
                    "`16` is a small gap on this instance and is not a general bound: on "
                    "the four-job instance in the worked example the gap is `19` against "
                    "`15`."},
            {"q": "What does this course offer for `1 || sum T`, minimising total tardiness on one machine?",
             "a": ["A rule based on slack `d − p`",
                   "The exhaustive optimum on small instances, and the statement that no adjacent-exchange rule exists for it",
                   "Earliest due date, which is optimal for it as well",
                   "Shortest processing time, which minimises the total of anything"],
             "c": 1,
             "why": "The swap changes two clipped quantities by amounts that depend on "
                    "where the due dates sit relative to the clock, so no condition on "
                    "the pair alone decides it. The lab enumerates instead, and names "
                    "the boundary rather than offering a heuristic that would teach the "
                    "opposite of the course."},
            {"q": "A schedule has every job finishing before its due date. What is `L max`?",
             "a": ["Zero, since nothing is late", "Negative, and it measures how much slack the tightest job had",
                   "Undefined", "Equal to `T max`"],
             "c": 1,
             "why": "`L_j = C_j − d_j` is not clipped, so an all-early schedule has a "
                    "negative maximum lateness, and its size says how much the tightest "
                    "job spared. `T max` would be `0` here, which is why the two are "
                    "listed as separate objectives: the tardiness has thrown away the "
                    "information the lateness kept."},
        ],
        "mistakes": [
            ("Hearing “minimises lateness” as “minimises how late things are in total”",
             "It minimises the largest single lateness. On the lab's instance that "
             "costs `17` of total tardiness where `16` exists, and on the four-job "
             "instance `19` where `15` exists. Both sentences are about lateness and "
             "they name different numbers; the rule answers one of them."),
            ("Clipping the negatives before taking the maximum",
             "`L max` uses the signed latenesses, so a job finishing two hours early "
             "contributes `−2`. Clip first and you have computed `T max`, which is a "
             "different objective that happens to agree whenever anything is late. On "
             "an all-early schedule the two differ, and the signed one is the "
             "informative one."),
            ("Ordering by slack `d − p` and calling it earliest due date",
             "They are different rules and they give different orders. On the lab's "
             "third preset they disagree on all four jobs; on its opening preset slack "
             "ordering gives `L max = 7` where earliest-due-date gives `6`. The "
             "exchange argument was about `d`, and `d − p` is not `d`."),
        ],
        "standard": ("Finish when you can prove the rule and state, unprompted, the two objectives it does not touch.",
                     "You should be able to run the adjacent exchange for a maximum, "
                     "showing that both new latenesses fall below the pair's old "
                     "maximum, conclude that due-date order minimises `L max` and "
                     "`T max`, compute `sum T` and the number of late jobs for the same "
                     "order, and say why total tardiness has no exchange rule rather "
                     "than reaching for slack or for shortest-first."),
        "note": 'One of the two objectives EDD lost is not lost for long. Counting late jobs rather than adding up hours of lateness turns out to have a rule, and it is not a sorting rule &mdash; it builds a set of jobs that will finish on time and throws jobs out of it, and the job it throws out is not the job that was late. &ldquo;Minimising the Number of Late Jobs&rdquo; runs it a step at a time, and on these same five jobs it leaves two late where due-date order leaves four.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "minimising-the-number-of-late-jobs",
        "title": "Minimising the Number of Late Jobs",
        "module": "Due dates, and which question you asked",
        "one_line": "Offer the jobs in due-date order, and whenever the accepted set runs past a due date throw out the longest job accepted so far, not the one that went late.",
        "summary": (
            "Counting late jobs is a different objective again, and it has an exact "
            "algorithm rather than a sorting rule. Moore&ndash;Hodgson offers the jobs "
            "in due-date order, and the moment the accepted set runs past a due date it "
            "discards the <em>longest</em> job accepted so far. The job discarded is "
            "usually not the job that went late, and on the lab's five jobs the "
            "algorithm leaves two late where due-date order alone leaves four."
        ),
        "key": [
            "objective  sum U  =  the NUMBER of late jobs;  how late they are does not count",
            "offer the jobs in due-date order, keeping a set that finishes on time",
            "when the set runs past a due date, discard the LONGEST job in the set",
            "not the job that just went late — the longest one frees the most room",
            "A 6:8, B 4:4, C 5:12, D 3:6, E 7:20:  keeps D C E, discards B then A, 2 late",
            "due-date order alone leaves 4 late;  the enumerated minimum is 2",
        ],
        "key_label": "One pass, one discard rule, and the job it chooses",
        "concepts_intro": (
            "Three ideas: what the objective throws away, why the discard is the "
            "longest job, and why the answer is a set rather than an order."
        ),
        "concepts": [
            ("Counting late jobs throws away how late they are",
             "`sum U` adds one for each job that misses its date and nothing for how "
             "badly. A job one minute late and a job three weeks late contribute the "
             "same. That makes the objective coarse and makes it the right one "
             "surprisingly often &mdash; a shipment either made the sailing or did not "
             "&mdash; and it changes the problem completely, because now a job can be "
             "written off entirely and pushed to the very end at no further cost."),
            ("The discard is the longest accepted job, not the one that was late",
             "When the set runs past a due date, exactly one job has to go, and every "
             "candidate costs the same one unit of `sum U`. So take the one that frees "
             "the most machine time, which is the longest job accepted so far. On the "
             "lab's instance the job that goes late at the second step is `D`, taking "
             "three hours, and the job discarded is `B`, taking four: the same one late "
             "job either way, and one extra hour of room for everything after it."),
            ("The answer is a set, and the order is what makes the set work",
             "What the algorithm computes is the largest set of jobs that can all "
             "finish on time. Once that set is known, running it in due-date order is "
             "what makes it feasible, and the discarded jobs go afterwards in any order "
             "at all &mdash; they are late whatever happens and no objective here "
             "prices how late. So the output is `kept, then discarded`, and only the "
             "first half is a scheduling decision."),
        ],
        "read_title": "The algorithm, step by step, and the discard that surprises people",
        "read_intro": "The objective, the algorithm in four lines, five steps run in front of you, and the two rival rules it beats.",
        "body": [
            ("def", ("The number of late jobs",
                     "`U_j` is `1` when `C_j > d_j` and `0` otherwise, and the "
                     "objective `sum U` counts the late jobs. A schedule is measured by "
                     "how many promises it broke, not by how far.")),
            ("def", ("The Moore–Hodgson algorithm",
                     "Sort the jobs by due date ascending. Keep a set `S`, initially "
                     "empty, and a running finish time. Offer the jobs in that order: "
                     "add the next job to `S` and advance the finish time by its "
                     "processing time. If the finish time now exceeds the due date of "
                     "the job just added, remove from `S` the job with the "
                     "<strong>largest processing time</strong> and reduce the finish "
                     "time by it.",
                     "At the end, `S` is a largest set of jobs that can all be on time. "
                     "Schedule `S` in due-date order, then the discarded jobs in any "
                     "order. The number of late jobs is the number discarded.")),
            ("p", "The algorithm is offered the jobs in due-date order and it is not "
                  "the due-date rule. That distinction is the whole reason it works, "
                  "and the lab prints both figures side by side so it cannot be "
                  "blurred: due-date order alone leaves four jobs late on the instance "
                  "where the algorithm leaves two."),
            ("h3", "Five jobs, five steps, two discards"),
            ("math", [
                "jobs offered in due-date order   B 4:4,  D 3:6,  A 6:8,  C 5:12,  E 7:20",
                "",
                "  1   B joins    set B        finish 4   against due 4    on time",
                "  2   D joins    set B D      finish 7   against due 6    LATE",
                "         discard the longest in the set: B at 4",
                "         set D,  finish drops to 3",
                "  3   A joins    set D A      finish 9   against due 8    LATE",
                "         discard the longest in the set: A at 6",
                "         set D,  finish drops to 3",
                "  4   C joins    set D C      finish 8   against due 12   on time",
                "  5   E joins    set D C E    finish 15  against due 20   on time",
                "",
                "  kept D C E      discarded B, A      late 2",
                "  schedule  D C E B A      C = 3, 8, 15, 19, 25",
                "  enumerated minimum over all 120 orders: 2      the algorithm attains it",
            ]),
            ("example", ("Step 2, and why B goes rather than D",
                         "`D` is the job that pushed the set past a due date: adding it "
                         "took the finish from `4` to `7` against `D`'s due date of "
                         "`6`. The instinct is to discard `D`. Either choice leaves "
                         "exactly one job late at this point, so the two are tied on "
                         "the objective and the tie is broken by what is left behind.",
                         "Discarding `D` frees three hours; discarding `B` frees four. "
                         "The algorithm takes the four, and the extra hour is what lets "
                         "`C` and `E` both join later without another discard. `B` had "
                         "been comfortably on time at step 1 and is thrown out at step "
                         "2 without ever having been the problem.")),
            ("h3", "The two rules it beats, measured"),
            ("math", [
                "  due-date order alone      B D A C E     late 4",
                "  Moore–Hodgson             D C E B A     late 2",
                "  shortest-first            D B C A E     late 3",
                "  the enumerated minimum                  late 2,  attained by 10 of the 120 orders",
            ]),
            ("p", "Due-date order leaves four late, and it is not a bad rule &mdash; it "
                  "is the optimal rule for maximum lateness on this very instance. It "
                  "loses here because it never gives up on anything: it keeps trying to "
                  "run `B` and `A` on time and fails at both, and the hours spent "
                  "failing make `C` late as well. Writing two jobs off at the start is "
                  "what buys the other three."),
            ("p", "That is the difference between a sorting rule and an algorithm, and "
                  "it is why this lesson is not a fourth exchange argument. There is no "
                  "key you can sort the jobs by that produces `D C E B A`; the answer "
                  "depends on a set being built and repaired, and the repair looks at "
                  "jobs that were accepted several steps earlier."),
            ("h3", "What the algorithm does not do"),
            ("p", "It does not minimise total tardiness, and it does not try to. Its "
                  "output on the lab's instance runs the two discarded jobs at the very "
                  "end, where `B` finishes at `19` against a due date of `4` and `A` at "
                  "`25` against `8`. That is `15 + 17 = 32` hours of tardiness against "
                  "the `17` due-date order costs, and the algorithm is indifferent to "
                  "all of it, because the objective counts jobs."),
            ("p", "It also does not weight the jobs. The weighted version &mdash; "
                  "minimise `sum w U`, the value of the work that misses its date "
                  "&mdash; is a genuinely harder problem, and no version of this "
                  "argument reaches it: the tie that let us discard the longest job was "
                  "a tie because every discard cost one unit, and with weights the "
                  "discards cost different amounts. The lab does not offer a weighted "
                  "mode, and this is why."),
            ("p", "One structural point worth keeping. The kept set finishes on time "
                  "<em>in due-date order</em>, and the lab checks that job by job rather "
                  "than trusting it: `D` at `3` against `6`, `C` at `8` against `12`, "
                  "`E` at `15` against `20`. If a set can be run on time at all, it can "
                  "be run on time in due-date order &mdash; which is the exchange "
                  "argument of &ldquo;Earliest Due Date and Maximum Lateness&rdquo;, "
                  "used here as a tool rather than as a result."),
        ],
        "lab": ("schedule", {
            "mode": "late",
            "preset": "throws",
            "panel_title": "Offer the jobs one at a time, and watch which one gets thrown out",
            "panel_intro": "The slider stops the algorithm after a chosen number of "
                           "jobs have been offered, so each discard can be watched as "
                           "it happens. The panel names the job that went late and the "
                           "job that was discarded separately, reports what due-date "
                           "order alone would leave late on the same jobs, and checks "
                           "the result against the fewest late jobs any order achieves.",
        }),
        "steps_title": "Running Moore–Hodgson by hand",
        "steps_intro": "Five steps, and the fourth is the one people get wrong.",
        "steps": [
            ("Sort the jobs by due date and keep them in that order",
             "This is the order they will be <em>offered</em> in, not the answer. The "
             "answer is the set that survives, and the algorithm is not finished until "
             "every job has been offered once."),
            ("Add the next job and advance the running finish time",
             "The finish time is the sum of the processing times of the jobs currently "
             "in the set, so adding a job advances it by that job's `p`. Keep the "
             "number in front of you; it is the only state the algorithm has besides "
             "the set."),
            ("Compare the finish time with the due date of the job just added",
             "Not with any other job's due date. Because the set is kept in due-date "
             "order and every earlier job was on time when it was checked, the newest "
             "job is the only one that can have gone late."),
            ("If it is late, discard the longest job in the set",
             "The longest in the whole set, which may be a job accepted several steps "
             "ago and may be the job just added. Reduce the finish time by that job's "
             "processing time. Discarding the job that went late is the natural move "
             "and it is not the algorithm: on the lab's instance it would free three "
             "hours where four were available."),
            ("At the end, schedule the survivors in due-date order and the rest after",
             "The survivors all finish on time, and the count of late jobs is the count "
             "of discards. The order among the discarded jobs is free &mdash; they are "
             "late however they run, and this objective does not price how late."),
        ],
        "worked": {
            "title": "Five jobs, two thrown out, and neither of them the one that broke the schedule",
            "intro": [
                "The lab's opening preset &mdash; the same five jobs as the due-date "
                "lesson. Every line is what the panel shows as the step slider is moved "
                "from one to five.",
            ],
            "lines": [
                "jobs   A 6:8   B 4:4   C 5:12   D 3:6   E 7:20",
                "offered in due-date order:  B (4), D (6), A (8), C (12), E (20)",
                "",
                "  step   offered   set after       finish   due   verdict",
                "    1      B       B                  4      4    on time",
                "    2      D       B D                7      6    LATE",
                "                   discard B (4, the longest in the set)",
                "                   D                  3",
                "    3      A       D A                9      8    LATE",
                "                   discard A (6, the longest in the set)",
                "                   D                  3",
                "    4      C       D C                8     12    on time",
                "    5      E       D C E             15     20    on time",
                "",
                "  kept D C E, checked one at a time:  3 ≤ 6,  8 ≤ 12,  15 ≤ 20",
                "  discarded B, A        late 2",
                "",
                "  final schedule    D C E B A",
                "     C   =   3    8   15   19   25",
                "     d   =   6   12   20    4    8",
                "     late          B and A, by 15 and 17 hours",
                "",
                "  COMPARISONS ON THE SAME FIVE JOBS",
                "     due-date order  B D A C E   late 4",
                "     shortest first  D B C A E   late 3",
                "     the minimum over all 120 orders   2",
            ],
            "after": [
                "Step 2 is the step to reread. The job that went late was `D`; the job "
                "thrown out was `B`. Both choices leave one job late at that moment, so "
                "the objective cannot distinguish them, and the algorithm breaks the tie "
                "on the only thing that matters afterwards &mdash; how much machine time "
                "the discard returns. Four hours rather than three is the whole reason "
                "`C` and `E` both fit later on.",
                "The bottom block is the reason this lesson exists. Due-date order is "
                "the optimal rule for maximum lateness on these same jobs, and it is "
                "twice as bad here. There is no ordering of the five jobs by any key "
                "that produces `D C E B A`; the answer came from a set that was built "
                "and repaired, and the repair reached back to a job accepted two steps "
                "earlier.",
                "For a rehearsal, switch to the preset with one twelve-hour job and four "
                "small ones and predict the run before starting it. The supplied first "
                "move is that the four small jobs `B 2:5, C 3:7, D 2:9, E 4:13` are "
                "offered first and all fit, reaching a finish of `11`. Say what happens "
                "when the twelve-hour job arrives, which job is discarded, and how many "
                "end up late &mdash; and then check whether the big job could have been "
                "kept alongside any of the others.",
            ],
        },
        "quiz_title": "Discards, sets and the objective that counts jobs",
        "quiz": [
            {"q": "The accepted set runs past a due date. Which job does Moore–Hodgson discard?",
             "a": ["The job that has just gone late", "The job with the earliest due date",
                   "The job with the largest processing time in the set",
                   "The job with the least slack"],
             "c": 2,
             "why": "Every discard costs the same one unit of `sum U`, so the tie is "
                    "broken on how much machine time is freed, and that is the longest "
                    "job. On the lab's instance at step 2 the late job is `D` at three "
                    "hours and the discard is `B` at four; the extra hour is what lets "
                    "two later jobs fit."},
            {"q": "Why is the answer reported as a kept set plus a discarded set rather than as a single sorted order?",
             "a": ["Because the discarded jobs could still finish on time in a different order",
                   "Because what is computed is the largest set that can all be on time; the kept jobs run in due-date order and the late ones run afterwards in any order at all",
                   "Because the algorithm does not produce an order",
                   "Because the objective counts sets rather than jobs"],
             "c": 1,
             "why": "`sum U` prices nothing about a job once it is late, so the order "
                    "among the discarded jobs is free. The kept set is the decision, and "
                    "running it in due-date order is what makes it feasible &mdash; which "
                    "is the exchange argument of &ldquo;Earliest Due Date and Maximum "
                    "Lateness&rdquo;, used as a tool."},
            {"q": "On the lab's instance, due-date order leaves `4` jobs late and the algorithm leaves `2`. Why does due-date order do badly here?",
             "a": ["Because it is not optimal for anything",
                   "Because it sorts on the wrong key",
                   "Because it never writes a job off: it spends hours trying to run `B` and `A` on time, fails at both, and makes `C` late as well",
                   "Because the due dates are too tight for any rule"],
             "c": 2,
             "why": "Due-date order is optimal for maximum lateness on these same jobs, "
                    "so it is not a bad rule. It loses on this objective because "
                    "minimising the count rewards giving up early, and a sorting rule "
                    "cannot give up on anything."},
            {"q": "What does Moore–Hodgson say about total tardiness?",
             "a": ["Nothing: it minimises the count, and its own output costs `32` hours of tardiness on the lab's instance against the `17` due-date order costs",
                   "That it is minimised as well, since fewer late jobs means less tardiness",
                   "That it is within a factor of two of optimal",
                   "That total tardiness is the same for every order"],
             "c": 0,
             "why": "The discarded jobs are pushed to the very end, where `B` finishes "
                    "`15` hours late and `A` `17`. The objective counts jobs and is "
                    "indifferent to all of it. Fewer late jobs does not mean less "
                    "tardiness, and on this instance it means nearly twice as much."},
        ],
        "mistakes": [
            ("Discarding the job that went late",
             "It is the obvious move and it is not the algorithm. Both discards cost one "
             "unit of `sum U`, so the choice is decided by how much time is freed, and "
             "the longest job frees the most. On the lab's instance the difference is "
             "one hour at step 2 and it changes the final answer from three late jobs to "
             "two."),
            ("Reading the offer order as the answer",
             "The jobs are offered in due-date order and the schedule produced is "
             "`D C E B A`, which is not due-date order and is not sorted by anything. "
             "Reporting the due-date order as though it were the algorithm's output "
             "gives four late jobs instead of two, and the lab prints both figures so "
             "the confusion has somewhere to die."),
            ("Using it when the late jobs are not all worth the same",
             "The whole argument rests on every discard costing one unit. Put weights on "
             "the jobs and minimising `sum w U` is a different and genuinely harder "
             "problem, which nothing on this course solves. If a missed date on one job "
             "costs ten times what it costs on another, this algorithm is answering the "
             "wrong question and will answer it confidently."),
        ],
        "standard": ("Finish when you can run the algorithm by hand and say, at each discard, why that job and not the late one.",
                     "You should be able to offer the jobs in due-date order, maintain "
                     "the set and the running finish time, compare against the due date "
                     "of the job just added, discard the longest job in the set when the "
                     "set runs late, check the surviving set job by job, report the "
                     "schedule as the kept set followed by the discards, and say what "
                     "the same jobs cost under due-date order alone."),
        "note": 'That closes the single machine: four objectives with rules, one without, and every rule proved or run rather than asserted. What changes next is the machine. With two machines in series the makespan stops being a constant and becomes the whole problem &mdash; the second machine has gaps in it, and the gaps depend on the order. &ldquo;Two Machines in Series and Johnson&rsquo;s Rule&rdquo; is the last exact sequencing rule on the course.',
    },
]
