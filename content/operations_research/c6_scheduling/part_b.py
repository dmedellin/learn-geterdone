"""Scheduling, the last four lessons - more than one machine, and then money.

One machine had a constant makespan and five movable objectives. Add a second
machine and the makespan becomes the whole problem; add a third and the exchange
argument runs out, which is where this course hands the question to the search
of "Integer Programming" rather than inventing a rule for it. The last lesson
puts a price on time: the project network of "Networks: Flows, Paths and
Assignments" with a cost per day attached, solved as a linear programme and
checked by a forward and a backward pass that share no arithmetic with it.

Every figure below is read off the `schedule` kit: the flow-shop and parallel
makespans against an enumeration of every order and every assignment, the job
shop against every orientation of every disjunctive pair, and the crashing plan
against a fresh solve at each deadline and a critical-path pass over the
durations it bought.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "two-machines-in-series-and-johnsons-rule",
        "title": "Two Machines in Series and Johnson's Rule",
        "module": "More than one machine",
        "one_line": "Every job goes through machine one then machine two; the makespan is now worth optimising, and it is machine two's idle time that the rule attacks.",
        "summary": (
            "Two machines in series, every job visiting them in the same order. The "
            "first machine never stops, so the makespan is the work on the second "
            "machine plus the idle time in between &mdash; and the work does not "
            "depend on the order, so minimising the makespan <em>is</em> minimising "
            "idle time on the second machine. Johnson's rule does it exactly: jobs "
            "quicker on the first machine go to the front, shortest first, and the "
            "rest go to the back, longest on the second machine first."
        ),
        "key": [
            "two machines in series, every job M1 then M2, no preemption, all ready at 0",
            "C2(k) = max(C1(k), C2(k−1)) + p2(k)          the second machine waits or works",
            "makespan = (work on M2) + (idle on M2);  the work is order-independent",
            "Johnson: p1 < p2 to the FRONT by p1 ascending;  the rest to the BACK by p2 descending",
            "A 5:2, B 1:6, C 9:7, D 3:8, E 10:4:  Johnson B D C E A, makespan 30",
            "typed order A B C D E: 34, and M2 idles 7 where Johnson idles 3",
        ],
        "key_label": "One recursion, one rule, and the gap it is closing",
        "concepts_intro": (
            "Three ideas: what the second machine is waiting for, why that turns the "
            "makespan into an idle-time problem, and what the rule's two halves are "
            "each doing."
        ),
        "concepts": [
            ("The first machine never stops; the second one waits",
             "Machine one runs the jobs back to back from time zero, so its timeline "
             "has no gaps and its finish times do not depend on anything but the "
             "order. Machine two can only start a job once machine one has released it "
             "<em>and</em> machine two is free, so its timeline has gaps in it. Every "
             "interesting quantity here is about those gaps."),
            ("Minimising the makespan is minimising idle time on the second machine",
             "The project ends when machine two finishes its last job, and machine "
             "two's timeline is made of exactly two things: the processing it does, "
             "which is `sum p2` whatever the order, and the time it spends waiting. So "
             "`makespan = sum p2 + idle`, the first term is a constant, and the whole "
             "of the optimisation is the second. On the lab's five jobs the work is "
             "`27` in every order and the idle time is `3` under the rule and `7` in "
             "the typed order &mdash; which is the whole of the difference between "
             "`30` and `34`."),
            ("The rule has two halves and they do different jobs",
             "A job quicker on machine one is a job that gets machine two started "
             "early, so those jobs go to the front, shortest on machine one first, to "
             "start machine two as soon as possible. A job quicker on machine two "
             "leaves machine one free early, so those go to the back, longest on "
             "machine two first, so that the longest tail is not the thing left at the "
             "end. Both halves are minimising idle time, at the two ends where idle "
             "time happens."),
        ],
        "read_title": "Two machines, one recursion, and the rule that empties the gaps",
        "read_intro": "The model, the recursion that builds the schedule, the rule in two halves, and it measured against every one of the 120 orders.",
        "body": [
            ("def", ("The two-machine flow shop",
                     "`n` jobs; job `j` needs `p1_j` on machine one and then `p2_j` on "
                     "machine two, in that order. Both machines run one job at a time, "
                     "nothing is interrupted, everything is available at time zero, "
                     "and every job visits the machines in the same order &mdash; "
                     "which is what makes it a <strong>flow shop</strong>.",
                     "The same order is used on both machines. A schedule that "
                     "resequenced between the machines could in principle do better on "
                     "more than two machines; on two it cannot, which is why one "
                     "permutation is the whole decision here.")),
            ("p", "Write the order as `k = 1, 2, …, n`. Machine one finishes job `k` at "
                  "`C1(k) = C1(k−1) + p1(k)`, with `C1(0) = 0`, so it is the running "
                  "total. Machine two cannot start job `k` until both that job has left "
                  "machine one and machine two has finished job `k−1`:"),
            ("math", [
                "  C1(k) = C1(k−1) + p1(k)",
                "  C2(k) = max( C1(k), C2(k−1) ) + p2(k)",
                "",
                "  makespan = C2(n)",
                "  idle on machine 2 = C2(n) − sum p2       and sum p2 does not move",
            ]),
            ("p", "The `max` is where the whole problem lives. When `C1(k)` wins, "
                  "machine two was idle waiting for the job; when `C2(k−1)` wins, "
                  "machine two was busy and the job waited instead. Waiting jobs cost "
                  "nothing in this objective; a waiting machine costs the makespan."),
            ("def", ("Johnson's rule",
                     "Split the jobs. Those with `p1 < p2` form the <strong>front "
                     "group</strong> and are ordered by `p1` ascending. The rest, with "
                     "`p1 ≥ p2`, form the <strong>back group</strong> and are ordered "
                     "by `p2` descending. The schedule is the front group followed by "
                     "the back group, and it minimises the makespan.")),
            ("h3", "Five jobs, and where the four hours went"),
            ("math", [
                "jobs    A 5:2   B 1:6   C 9:7   D 3:8   E 10:4        p1:p2",
                "",
                "  quicker on machine 1:  B (1 < 6) and D (3 < 8)   →  front, by p1 up:  B, D",
                "  the rest:              A, C, E                   →  back, by p2 down: C (7), E (4), A (2)",
                "",
                "JOHNSON   B D C E A",
                "   M1     B[0,1]  D[1,4]   C[4,13]   E[13,23]  A[23,28]",
                "   M2     B[1,7]  D[7,15]  C[15,22]  E[23,27]  A[28,30]",
                "   makespan 30     idle on M2 = 1 + 1 + 1 = 3      work on M2 = 27",
                "",
                "TYPED     A B C D E",
                "   M1     A[0,5]  B[5,6]   C[6,15]   D[15,18]  E[18,28]",
                "   M2     A[5,7]  B[7,13]  C[15,22]  D[22,30]  E[30,34]",
                "   makespan 34     idle on M2 = 5 + 2 = 7          work on M2 = 27",
                "",
                "  best of all 120 orders  30,  attained by 2 of them — Johnson's is one",
            ]),
            ("p", "The two schedules do the same `27` hours of work on machine two and "
                  "differ only in how long that machine spent waiting. In the typed "
                  "order it waits five hours at the start, because `A` occupies machine "
                  "one for five hours before anything can be handed over. Johnson puts "
                  "`B` first, which occupies machine one for one hour, and machine two "
                  "starts at `1` instead of at `5`."),
            ("example", ("The starved second machine, on purpose",
                         "The lab has a preset built to make this visible: four jobs "
                         "where the typed order begins with an eight-hour job on "
                         "machine one that needs one hour on machine two. Machine two "
                         "stands idle for the whole eight hours, and the typed order "
                         "finishes at `35` with `18` hours of idle time against `17` "
                         "hours of work.",
                         "Johnson's rule turns it round completely: `D C B A`, "
                         "finishing at `24` with `7` hours of idle. Same jobs, same "
                         "work, eleven hours saved, and the enumeration confirms that "
                         "`24` is the best any of the twenty-four orders can do.")),
            ("h3", "Checking the picture before believing the number"),
            ("p", "A recursion that produces a number is easy to get subtly wrong, so "
                  "the lab reads the drawing back. It checks that machine one runs with "
                  "no gaps, that machine two never overlaps itself, that no job reaches "
                  "machine two before it has left machine one, and that the makespan "
                  "taken off the last bar is the makespan the recursion reported. Then "
                  "it checks `work + idle = makespan` exactly, which is the identity "
                  "the rule is built on."),
            ("p", "It also runs every one of the `n!` orders through the same two-"
                  "machine clock and reports the best, the count and how many orders "
                  "tie for it. On the lab's instance two orders attain `30`, and "
                  "Johnson's is one of them. Reporting the tie count matters: naming a "
                  "single order and implying it is the unique optimum is a claim "
                  "nobody made."),
            ("h3", "Where this stops"),
            ("p", "Three machines in series is a different problem and this rule does "
                  "not extend to it. There is a special case &mdash; when the middle "
                  "machine is dominated by one of the others &mdash; in which a "
                  "two-machine reduction works, and the general case is hard in the "
                  "sense &ldquo;Algorithms and Complexity&rdquo; gave the word. The lab "
                  "offers two machines and says so rather than offering a third with a "
                  "rule that is not a theorem."),
            ("p", "The tie case is worth one line. When `p1 = p2` for every job, as in "
                  "the lab's third preset, the front group is empty and the rule sorts "
                  "everything into the back group by `p2` descending. That order attains "
                  "the optimum, and so does every other order: all twenty-four tie at "
                  "`21`. The rule is not doing any work there, and the panel's tie "
                  "count says so."),
        ],
        "lab": ("schedule", {
            "mode": "flowshop",
            "preset": "johnson",
            "panel_title": "Two machines, your order against the rule's, and the idle time between them",
            "panel_intro": "Both schedules are drawn as two tracks, and both are read "
                           "back off the drawing before any figure is printed: machine "
                           "one with no gaps, machine two never overlapping itself, and "
                           "no job on machine two before it left machine one. The panel "
                           "reports the idle time on machine two for each order beside "
                           "the makespan, and checks the rule against every one of the "
                           "orders there are.",
        }),
        "steps_title": "Sequencing a two-machine flow shop",
        "steps_intro": "Four steps, and the second is the one that decides which half a job belongs to.",
        "steps": [
            ("Write each job as its two times, in machine order",
             "`p1:p2`, machine one first. Getting the two columns the wrong way round "
             "produces a valid schedule for a problem you do not have, and nothing in "
             "the output looks wrong &mdash; the makespan will simply be larger than it "
             "should be."),
            ("Split the jobs on `p1 < p2`",
             "Strictly quicker on machine one goes to the front group; everything else, "
             "including the ties, goes to the back group. The split is the decision; the "
             "two sorts that follow are bookkeeping."),
            ("Sort the front by `p1` ascending and the back by `p2` descending",
             "Two different keys for the two groups, and they are not the same sort run "
             "twice. The front wants the smallest first-machine time first, to start "
             "machine two as early as possible; the back wants the largest "
             "second-machine time first, so the tail at the end is short."),
            ("Build both timelines and check the identity",
             "Run the recursion, then add up the second machine's processing and its "
             "idle time and check that they come to the makespan. If they do not, the "
             "recursion has a gap in it that the drawing will show at once, and the lab "
             "refuses the schedule rather than printing the number."),
        ],
        "worked": {
            "title": "Five jobs through two machines, and four hours of waiting removed",
            "intro": [
                "The lab's opening preset, with both timelines written out. Every figure "
                "is what the panel reports when the comparison order is left as typed.",
            ],
            "lines": [
                "jobs   A 5:2   B 1:6   C 9:7   D 3:8   E 10:4",
                "       work on machine 2  =  2 + 6 + 7 + 8 + 4  =  27,  in every order",
                "",
                "THE SPLIT",
                "   p1 < p2:   B (1 < 6),  D (3 < 8)        front, by p1 ascending:  B, D",
                "   p1 ≥ p2:   A (5 ≥ 2),  C (9 ≥ 7),  E (10 ≥ 4)",
                "                                           back, by p2 descending: C 7, E 4, A 2",
                "   Johnson’s order   B D C E A",
                "",
                "JOHNSON’S SCHEDULE",
                "   machine 1   B 0–1    D 1–4    C 4–13   E 13–23  A 23–28",
                "   machine 2   B 1–7    D 7–15   C 15–22  E 23–27  A 28–30",
                "   idle on machine 2:  0–1,  22–23,  27–28        three hours",
                "   27 + 3 = 30 = makespan",
                "",
                "THE TYPED ORDER",
                "   machine 1   A 0–5    B 5–6    C 6–15   D 15–18  E 18–28",
                "   machine 2   A 5–7    B 7–13   C 15–22  D 22–30  E 30–34",
                "   idle on machine 2:  0–5,  13–15                seven hours",
                "   27 + 7 = 34 = makespan",
                "",
                "   the best of all 120 orders is 30, and 2 of them attain it",
            ],
            "after": [
                "The two idle blocks in the typed order are the whole of the four-hour "
                "gap, and they have different causes. The five hours at the start are "
                "machine two waiting for the first job to exist; the two hours in the "
                "middle are machine two having finished `B` at `13` while `C` is still "
                "on machine one until `15`. Johnson's split attacks the first with the "
                "front group and the second with the back group.",
                "Machine one is worth checking too. In both schedules it runs from `0` "
                "to `28` without a break and finishes before machine two does. That is "
                "always true here, and it is why no amount of cleverness about machine "
                "one helps: its timeline is fixed up to the order and it is never the "
                "thing that ends the schedule.",
                "For a rehearsal, use the preset where every job takes the same time on "
                "both machines. The supplied first move is that no job satisfies "
                "`p1 < p2`, so the front group is empty. Predict what the rule returns "
                "and what the enumeration says about how many orders tie for the best "
                "makespan, before the panel tells you. The answer is that all "
                "twenty-four tie, which means the rule is choosing arbitrarily and the "
                "tie count is the only honest way to say so.",
            ],
        },
        "quiz_title": "Idle time, the split, and what the rule is minimising",
        "quiz": [
            {"q": "Why is minimising the makespan on two machines the same as minimising idle time on the second machine?",
             "a": ["Because the first machine has no idle time",
                   "Because the makespan is the second machine's processing plus its idle time, and its processing is `sum p2` whatever the order",
                   "Because the second machine is always the bottleneck",
                   "Because every job finishes on the second machine"],
             "c": 1,
             "why": "The schedule ends when machine two finishes, and machine two's "
                    "timeline is processing plus waiting. The processing is `27` in "
                    "every order on the lab's instance, so the whole of the difference "
                    "between `30` and `34` is the idle time: `3` against `7`."},
            {"q": "Under Johnson's rule, where does a job with `p1 = 3` and `p2 = 8` go?",
             "a": ["To the back group, because `p2` is larger",
                   "To the front group, ordered by `p1` ascending, because it is quicker on machine one",
                   "To the front group, ordered by `p2` descending",
                   "Either group: the rule is indifferent when the two differ by more than a factor of two"],
             "c": 1,
             "why": "`p1 < p2` puts the job in the front group, and the front group is "
                    "sorted by `p1` ascending. A job quick on machine one gets machine "
                    "two started early, which is what the front of the schedule is for. "
                    "The third choice uses the front group with the back group's key."},
            {"q": "The lab reports that two of the 120 orders attain the best makespan. Why does it report the count rather than just Johnson's order?",
             "a": ["Because Johnson's rule might not be one of them",
                   "Because naming one order and implying it is the unique optimum is a claim the enumeration did not make",
                   "Because ties mean the instance is degenerate",
                   "Because the makespan is not well defined when orders tie"],
             "c": 1,
             "why": "The enumeration knows how many orders attain the value and saying so "
                    "costs nothing. On the all-ties preset every one of the twenty-four "
                    "orders is optimal, and a page reporting only the rule's order there "
                    "would suggest the rule had done work it did not do."},
            {"q": "Does Johnson's rule extend to three machines in series?",
             "a": ["Yes, by applying it to each adjacent pair",
                   "Yes, by sorting on `p1 + p2` against `p2 + p3`",
                   "No: there is a special case where the middle machine is dominated and a two-machine reduction works, and the general problem is hard",
                   "No, because three machines cannot be a flow shop"],
             "c": 2,
             "why": "The special case is real and narrow. The general three-machine flow "
                    "shop is NP-hard in the sense &ldquo;Algorithms and "
                    "Complexity&rdquo; gives the word, and this course offers two "
                    "machines and says so rather than shipping a rule that is not a "
                    "theorem."},
        ],
        "mistakes": [
            ("Sorting the whole list by one key",
             "The rule is a split and then two <em>different</em> sorts: `p1` ascending "
             "in the front group, `p2` descending in the back. Sorting everything by "
             "`p1` ascending gives `B D A C E` on the lab's instance, which is not "
             "Johnson's order and does not attain `30`."),
            ("Trying to improve machine one",
             "It runs from zero to the end of its work with no gaps in every order, and "
             "it always finishes before machine two. Effort spent smoothing it is "
             "effort spent on a timeline that is not deciding anything; the gaps that "
             "matter are all on the second machine."),
            ("Carrying the makespan intuition over from one machine",
             "On one machine the makespan is a constant and there is nothing to "
             "optimise. On two it ranges from `30` to well above `34` on the lab's five "
             "jobs, and it is the only objective in this lesson. The constant was a "
             "consequence of one machine never idling, and a second machine breaks it."),
        ],
        "standard": ("Finish when you can build both timelines by hand and account for the makespan as work plus idle.",
                     "You should be able to run the two-machine recursion with its `max`, "
                     "split the jobs on `p1 < p2`, sort the two groups on their own keys, "
                     "draw both machines' timelines, list the idle intervals on machine "
                     "two, check that the idle time plus `sum p2` equals the makespan, "
                     "and compare the rule against a typed order on the same jobs."),
        "note": 'The rule worked because the two machines are visited in the same order by every job, which made one permutation the whole decision. Let two jobs visit the machines in <em>opposite</em> orders and there is no permutation to choose: each shared machine has its own sequencing question, and the questions interact. &ldquo;The Job Shop and Disjunctive Orientations&rdquo; is what is left when the exchange argument runs out &mdash; but first, the same jobs on machines that run in parallel rather than in series, where a rule survives and arrives with a guarantee rather than a proof of optimality.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "machines-in-parallel-and-the-lpt-bound",
        "title": "Machines in Parallel, and What LPT Guarantees",
        "module": "More than one machine",
        "one_line": "Place the longest jobs first on whichever machine is free soonest, and the answer is not optimal — it is within a factor that is proved from two lower bounds.",
        "summary": (
            "`m` identical machines, each job on exactly one of them, minimise the time "
            "the last machine finishes. No exchange argument reaches this: the "
            "decision is an assignment rather than an order. What is available is a "
            "heuristic with a guarantee, and two lower bounds &mdash; the average load "
            "and the longest single job &mdash; that the guarantee is proved from. On "
            "the lab's instance longest-first finishes at `13` where `12` is possible, "
            "and the binding lower bound is `34/3`, which no schedule attains."
        ),
        "key": [
            "m identical machines, each job on one machine, minimise the last finish",
            "LPT: longest job first, onto whichever machine is free soonest",
            "bound 1   sum p / m       some machine does at least its share",
            "bound 2   max p           that job runs on one machine without a break",
            "neither implies the other, and the OPTIMUM can be above both",
            "A 7, B 6, C 5, D 4, E 4, F 4, G 4 on 3:  LPT 13, optimum 12, bounds 34/3 and 7",
        ],
        "key_label": "One heuristic, two bounds, and a gap above both of them",
        "concepts_intro": (
            "Three ideas: why the exchange argument is not available, what the two "
            "bounds each see, and what a guarantee is when an optimum is not."
        ),
        "concepts": [
            ("The decision is an assignment, so there is nothing adjacent to swap",
             "On one machine a schedule was an order and two jobs could be neighbours. "
             "Here a schedule says which machine each job runs on, and the order within "
             "a machine does not affect when that machine finishes at all. Swapping two "
             "jobs between machines changes two loads by different amounts and changes "
             "the makespan only if one of them was the last to finish &mdash; so there "
             "is no local identity and no exchange proof, and the problem is hard in "
             "the sense &ldquo;Algorithms and Complexity&rdquo; gives the word."),
            ("Two lower bounds, and neither implies the other",
             "The total work divided by the number of machines is a lower bound, "
             "because some machine must do at least the average. The longest single job "
             "is a lower bound, because that job runs on one machine without a break. "
             "On the lab's instance they are `34/3` and `7` and the first binds; on its "
             "one-big-job preset they are `7` and `11` and the second binds. A "
             "schedule cannot beat the larger of them, and the lab prints both so it is "
             "clear which one is doing the work."),
            ("A guarantee is not an optimum, and a bound is not a schedule",
             "Longest-first is proved to finish within `4/3 − 1/(3m)` of the best "
             "possible. On the lab's instance that allows `11/9` and the measured ratio "
             "is `13/12`, so the guarantee holds with room to spare and is not tight. "
             "More important is what happens underneath: the optimum is `12` and the "
             "binding lower bound is `34/3`, which is less than `12`. A reader who "
             "stopped at the bound would believe in a schedule finishing at `34/3` that "
             "does not exist."),
        ],
        "read_title": "Identical machines, a greedy rule, and the two numbers underneath it",
        "read_intro": "The model, the rule, the two bounds it is measured against, and a worked instance where the optimum sits strictly above both of them.",
        "body": [
            ("def", ("Identical machines in parallel",
                     "`m` machines, all the same speed. Each job runs on exactly one "
                     "machine, without interruption, and a machine runs one job at a "
                     "time. The <strong>load</strong> of a machine is the total "
                     "processing time assigned to it, and the <strong>makespan</strong> "
                     "is the largest load. The order within a machine does not matter, "
                     "so a schedule is just a partition of the jobs into `m` groups.")),
            ("def", ("The LPT rule",
                     "<strong>Longest processing time</strong>: sort the jobs by `p` "
                     "descending and place each one, in turn, on whichever machine is "
                     "currently free soonest. It is a <strong>list-scheduling</strong> "
                     "rule &mdash; one pass, no backtracking &mdash; and it does not in "
                     "general find the optimum.")),
            ("thm", ("The two lower bounds",
                     "For every assignment of jobs to `m` identical machines, the "
                     "makespan is at least `sum p / m` and at least `max p`.")),
            ("proof", ["The `m` loads add to `sum p`, so the largest of them is at "
                       "least the average `sum p / m`. A maximum is never below a mean "
                       "of the same numbers.",
                       "The longest job runs on one machine without a break, so that "
                       "machine's load is at least `max p`, and the makespan is at "
                       "least that machine's load."]),
            ("p", "Neither bound implies the other, and the lab has a preset for each "
                  "direction. With seven jobs adding to `34` on three machines the "
                  "average is `34/3` and the longest job is `7`, so the average binds. "
                  "With one eleven-hour job and four small ones adding to `21` the "
                  "average is `7` and the longest job is `11`, so the longest binds "
                  "&mdash; and there the bound is tight, because the optimum really is "
                  "`11`."),
            ("h3", "Seven jobs, three machines, and one hour that cannot be recovered"),
            ("math", [
                "jobs   A 7, B 6, C 5, D 4, E 4, F 4, G 4        total 34,  m = 3",
                "",
                "  bound 1   34/3   the average load",
                "  bound 2    7     the longest single job",
                "  the binding bound is 34/3, which is about 11.33 and is not attainable",
                "",
                "LPT, placing 7, 6, 5, 4, 4, 4, 4 in turn on the machine free soonest",
                "   M1   A 7,  F 4                 load 11",
                "   M2   B 6,  E 4                 load 10",
                "   M3   C 5,  D 4,  G 4           load 13      makespan 13",
                "",
                "THE BEST OF ALL 2187 ASSIGNMENTS",
                "   M1   A 7,  C 5                 load 12",
                "   M2   B 6,  D 4                 load 10",
                "   M3   E 4,  F 4,  G 4           load 12      makespan 12",
                "",
                "   ratio 13/12,  inside the guarantee of 4/3 − 1/9 = 11/9",
                "   and 12 > 34/3: the optimum is strictly above the binding bound",
            ]),
            ("p", "Follow the rule's placements and the failure is visible. It puts the "
                  "seven-hour job on the first machine, the six on the second, the five "
                  "on the third, and then has four four-hour jobs to place onto loads "
                  "of `7`, `6` and `5`. They go to the third, the second, the first and "
                  "the third again, which leaves the third machine carrying `5 + 4 + 4 "
                  "= 13`. The optimum instead pairs the seven with the five and puts "
                  "three fours together, which nothing in a one-pass rule would find."),
            ("example", ("The optimum above the bound, which is the part worth keeping",
                         "The binding lower bound here is `34/3`, and `34` is not "
                         "divisible by `3`. Every load is a whole number, so no "
                         "assignment has all three loads equal to `34/3`, and in fact "
                         "no assignment gets below `12`.",
                         "So the bound is `34/3`, the optimum is `12` and the heuristic "
                         "is `13`. The gap between the heuristic and the optimum is a "
                         "failure of the heuristic; the gap between the optimum and the "
                         "bound is not a failure of anything. A report that treats the "
                         "bound as a target to be chased has confused the two, and the "
                         "target it is chasing does not exist.")),
            ("h3", "When the bound is tight, and when the rule is exact"),
            ("p", "The lab's other two presets are the easy cases and they are worth "
                  "running. With one eleven-hour job and four small ones the longest-job "
                  "bound is `11`, longest-first finishes at `11`, and the enumeration "
                  "confirms `11`: bound, heuristic and optimum all agree, and the "
                  "average-load bound of `7` is simply blind to why. With six four-hour "
                  "jobs on three machines the average-load bound is `8`, longest-first "
                  "finishes at `8` and the optimum is `8`; the longest-job bound is "
                  "only `4` and contributes nothing, which is the same asymmetry the "
                  "other way round."),
            ("p", "Neither of those is evidence about the rule. They are instances where "
                  "the bound happens to be attainable, and that is a property of the "
                  "data rather than of the method. The useful habit is to compute both "
                  "bounds first: when they meet the optimum the work is over before any "
                  "schedule is built, and when they do not, the size of the remaining "
                  "gap is what you have actually proved."),
            ("h3", "What the guarantee is and is not"),
            ("p", "The `4/3 − 1/(3m)` guarantee is a worst-case statement about every "
                  "instance, and it is proved from the two bounds rather than from any "
                  "property of a particular schedule. On three machines it allows "
                  "`11/9`; the measured ratio on the lab's instance is `13/12`, "
                  "comfortably inside it. A measured ratio on one instance is not "
                  "evidence about the bound in either direction, and the lab reports "
                  "both numbers separately for that reason."),
            ("p", "Shortest-first is the natural rival and it is much worse: on the "
                  "same seven jobs it finishes at `15` against the optimum of `12`, "
                  "because it spends the small jobs early and is left placing the "
                  "seven-hour job onto a machine that is already loaded. The lab offers "
                  "both rules on the same data, and the contrast is the argument for "
                  "sorting descending rather than an appeal to intuition."),
        ],
        "lab": ("schedule", {
            "mode": "parallel",
            "preset": "ratio",
            "panel_title": "Place the jobs greedily, then look at both bounds and at the best assignment there is",
            "panel_intro": "The rule's assignment is drawn as one track per machine "
                           "and its loads are added up again from the assignment rather "
                           "than taken from the rule. Beside it is the best of every "
                           "assignment, found by enumeration, and both lower bounds "
                           "&mdash; the average load and the longest job &mdash; so it "
                           "is visible which one binds and whether the optimum sits "
                           "above it.",
        }),
        "steps_title": "Splitting work across identical machines",
        "steps_intro": "Four steps, and the first one is done before any schedule exists.",
        "steps": [
            ("Compute both lower bounds before scheduling anything",
             "`sum p / m` exactly, as a fraction, and `max p`. The larger of the two is "
             "what no schedule can beat. On the lab's instance that is `34/3` against "
             "`7`, and knowing it before you start is what makes the answer "
             "interpretable when it arrives."),
            ("Sort the jobs descending and place them one at a time",
             "Each job goes on the machine that is free soonest, which at this point is "
             "the machine with the smallest load so far. Ties can be broken any way; "
             "the loads are what matter, not which physical machine is which."),
            ("Add the loads up again from the assignment",
             "Do not take the makespan from the placement loop. Recompute each "
             "machine's load from the list of jobs on it, check that the loads add to "
             "`sum p`, and take the largest. The lab does exactly this, because a "
             "placement loop with an off-by-one in it reports a plausible number."),
            ("Report the makespan with the bound beside it",
             "`13, against a lower bound of 34/3` is a result. `13` on its own is a "
             "number. If the two are equal you have proved optimality and can stop; if "
             "they are not, the difference is the most you could still gain, and on "
             "this instance most of it is not gainable at all."),
        ],
        "worked": {
            "title": "Seven jobs on three machines, greedily and then exactly",
            "intro": [
                "The lab's opening preset, placed one job at a time. Every figure is "
                "what the panel reports as the rule selector is moved between "
                "longest-first and shortest-first.",
            ],
            "lines": [
                "jobs   A 7, B 6, C 5, D 4, E 4, F 4, G 4      total 34,  three machines",
                "",
                "THE BOUNDS, BEFORE ANY SCHEDULE",
                "   average load   34/3",
                "   longest job     7",
                "   binding        34/3     no schedule finishes earlier than this",
                "",
                "LPT, PLACING IN DESCENDING ORDER",
                "   A 7  → M1 (0)      loads  7  0  0",
                "   B 6  → M2 (0)      loads  7  6  0",
                "   C 5  → M3 (0)      loads  7  6  5",
                "   D 4  → M3 (5)      loads  7  6  9",
                "   E 4  → M2 (6)      loads  7 10  9",
                "   F 4  → M1 (7)      loads 11 10  9",
                "   G 4  → M3 (9)      loads 11 10 13",
                "   makespan 13        M1 A F,  M2 B E,  M3 C D G",
                "",
                "THE BEST OF ALL 2187 ASSIGNMENTS",
                "   M1 A C  12     M2 B D  10     M3 E F G  12      makespan 12",
                "",
                "   ratio 13/12       guarantee on three machines  4/3 − 1/9 = 11/9",
                "   optimum 12  >  binding bound 34/3",
                "",
                "SHORTEST FIRST, ON THE SAME JOBS",
                "   M1 A D G  15     M2 C E  9     M3 B F  10        makespan 15",
            ],
            "after": [
                "The placement of `G`, the last job, is where the thirteen comes from. "
                "At that moment the loads are `11`, `10` and `9`, so `G` goes to the "
                "third machine and takes it to `13`. Nothing at that point can be "
                "undone, and the rule has no mechanism for undoing it &mdash; which is "
                "what a one-pass heuristic is.",
                "Three numbers, three meanings. `34/3` is proved and unattainable. `12` "
                "is attainable and was found by trying all `3⁷ = 2187` assignments. "
                "`13` is what the rule produced. Only the middle one is the answer to "
                "the question as asked, and on any instance large enough to matter it "
                "is the one you will not have.",
                "For a rehearsal, switch to the one-big-job preset: `A 11, B 3, C 3, D "
                "2, E 2` on three machines. Compute both bounds before running it. The "
                "supplied first move is that the total is `21`, so the average bound is "
                "`7` and the longest-job bound is `11`. Say which binds, predict the "
                "optimum, and say why the average-load bound could never have seen it.",
            ],
        },
        "quiz_title": "Bounds, guarantees and what a heuristic proves",
        "quiz": [
            {"q": "Why is there no adjacent-exchange proof for this problem?",
             "a": ["Because the machines are identical",
                   "Because a schedule is an assignment of jobs to machines rather than an order, so there is no adjacent pair and no local identity for the makespan",
                   "Because the makespan is a maximum",
                   "Because the jobs have no due dates"],
             "c": 1,
             "why": "The order within a machine does not affect when that machine "
                    "finishes, so the only decision is the partition. Moving a job "
                    "between machines changes two loads by different amounts and moves "
                    "the makespan only if one of them was largest &mdash; there is no "
                    "subtraction that settles it, and the problem is hard."},
            {"q": "The average-load bound on an instance is `34/3` and the optimum is `12`. What does that say about the bound?",
             "a": ["That the enumeration is wrong, since a bound must be attainable",
                   "That the schedule found is `2/3` away from optimal",
                   "That the bound is valid and simply not attainable here: every load is a whole number and `34` is not divisible by `3`",
                   "That another lower bound must be larger"],
             "c": 2,
             "why": "A lower bound is a statement that nothing does better, not a "
                    "promise that something does that well. Here the loads are integers "
                    "and no assignment reaches below `12`. Treating the bound as a "
                    "target is how a report ends up chasing a schedule that does not "
                    "exist."},
            {"q": "Longest-first finishes at `13` on the lab's instance and the guarantee on three machines is `4/3 − 1/9 = 11/9`. What has been shown?",
             "a": ["That the ratio `13/12` is inside the guarantee on this instance, which is one measurement and not evidence about the guarantee",
                   "That the guarantee is tight",
                   "That the rule is optimal for this instance",
                   "That the guarantee is wrong, since `13/12` is smaller than `11/9`"],
             "c": 0,
             "why": "The guarantee is a worst-case statement about every instance; "
                    "`13/12` is what happened here. A measurement inside a bound neither "
                    "confirms nor tightens it, and the lab prints the two figures "
                    "separately so the distinction survives."},
            {"q": "Both lower bounds are computed and the larger is `11`, and a schedule is found with makespan `11`. What follows?",
             "a": ["Nothing until every assignment has been tried",
                   "That `11` is optimal, because no schedule can beat the bound and this one attains it",
                   "That the rule used is optimal in general",
                   "That the other bound was computed wrongly"],
             "c": 1,
             "why": "A feasible schedule attaining a valid lower bound is a proof of "
                    "optimality and no enumeration is needed. That is what happens on "
                    "the one-big-job preset, where the longest-job bound is `11` and "
                    "longest-first attains it. It says nothing about the rule "
                    "elsewhere."},
        ],
        "mistakes": [
            ("Reading the average-load bound as a reachable target",
             "`34/3` is a proof that nothing finishes sooner. On this instance the true "
             "optimum is `12`, which is more than half an hour above it, and no "
             "rearrangement will ever close that part of the gap. The distance from a "
             "heuristic to the bound is not the distance from the heuristic to the "
             "answer."),
            ("Sorting the jobs ascending",
             "Placing the small jobs first leaves the large ones to land on machines "
             "that are already loaded: on the lab's instance shortest-first finishes at "
             "`15` against longest-first's `13` and an optimum of `12`. The rule sorts "
             "descending for that reason, and the lab runs both so the difference is "
             "measured rather than argued."),
            ("Reporting a heuristic value without the bound",
             "`13` alone says nothing about how good it is. `13, against a lower bound "
             "of 34/3 and an enumerated optimum of 12` says three separate things, only "
             "one of which survives to a larger instance. A number with no bound "
             "attached is the thing this path's last courses exist to stop."),
        ],
        "standard": ("Finish when you can compute both bounds first and say what a heuristic value means against them.",
                     "You should be able to compute `sum p / m` exactly and `max p`, say "
                     "which binds and why neither implies the other, run longest-first "
                     "placement by hand recording the loads after each job, recompute the "
                     "loads from the finished assignment rather than from the loop, and "
                     "state the result as a makespan with a lower bound beside it, "
                     "distinguishing the part of the gap that is the heuristic's fault "
                     "from the part that is not."),
        "note": 'That is the first result on this course that is not exact, and it is the first that arrives with a guarantee instead. Two of the three objectives left on the path work this way. The remaining machine model is worse again: let each job visit the machines in its own order and there is not even a sequence to choose &mdash; there is one binary decision per pair of operations sharing a machine, and some combinations of those decisions describe a schedule that cannot be run at all.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-job-shop-and-disjunctive-orientations",
        "title": "The Job Shop and Disjunctive Orientations",
        "module": "More than one machine",
        "one_line": "Each job visits the machines in its own order; every pair of operations sharing a machine is one binary choice, and some choices produce a schedule that deadlocks.",
        "summary": (
            "In a job shop each job has its own route through the machines, so there is "
            "no single sequence to choose. What there is is one binary decision per "
            "pair of operations that share a machine. Fix all of them and the shop "
            "becomes an ordinary project network whose longest path is the makespan; "
            "fix them badly and the network has a cycle, which is a deadlock and a real "
            "answer rather than an error. On the lab's four operations there are four "
            "orientations, one of them deadlocks, and the best finishes at `6`."
        ),
        "key": [
            "job shop: each job has its OWN machine route, fixed; the sequencing is not",
            "two operations on one machine  ⟹  one binary choice: which goes first",
            "k such pairs  ⟹  2^k orientations, each an acyclic network or a deadlock",
            "an acyclic orientation’s makespan is the LONGEST PATH — CPM, as before",
            "J1 M1 3, J1 M2 2, J2 M2 4, J2 M1 1:  2 pairs, 4 orientations, 1 deadlock, best 6",
            "lower bound  max(machine load, job length) = max(4, 6, 5, 5) = 6, and it is tight here",
        ],
        "key_label": "One bit per shared pair, and what the bits can add up to",
        "concepts_intro": (
            "Three ideas, and the second is the one that makes this an integer "
            "programme rather than a sequencing problem."
        ),
        "concepts": [
            ("A route is fixed; a sequence is not",
             "Each job carries an ordered list of operations &mdash; this machine, then "
             "that one &mdash; and that list is part of the data. What is undecided is "
             "the order in which a machine serves the operations that need it. With two "
             "jobs going through two machines in opposite directions there is no single "
             "permutation to optimise: the two machines have two separate questions, "
             "and the answers interact."),
            ("Each shared pair is one binary variable",
             "Two operations needing the same machine must not overlap, which means one "
             "finishes before the other starts &mdash; a choice with exactly two "
             "answers. That is the either-or constraint of &ldquo;Integer "
             "Programming&rdquo;, and it is why this problem is an integer programme "
             "and the single-machine rules are not. With `k` shared pairs there are "
             "`2^k` orientations, and the lab enumerates all of them at this size."),
            ("A deadlock is an answer, not an error",
             "Orient the pairs and every precedence in the shop becomes an arc: the "
             "route arcs from the data, the disjunctive arcs from the choices. If the "
             "resulting network is acyclic it is an ordinary project network and its "
             "longest path is the makespan. If it has a cycle, the choices require each "
             "of a set of operations to wait for another, and no schedule exists at "
             "all. The lab counts those orientations rather than skipping them, because "
             "how many of the choices are infeasible is part of what the problem looks "
             "like."),
        ],
        "read_title": "Routes, orientations, longest paths and cycles",
        "read_intro": "The model, one bit per shared pair, all four orientations of a two-job shop written out, and the one that cannot be run.",
        "body": [
            ("def", ("A job shop",
                     "A set of jobs, each an ordered list of <strong>operations</strong>. "
                     "Operation `i` of job `j` needs a named machine for a given "
                     "duration and cannot start until operation `i − 1` of the same job "
                     "has finished. A machine runs one operation at a time. The route "
                     "is fixed by the data; the order in which each machine serves the "
                     "operations assigned to it is the decision.",
                     "A <strong>flow shop</strong> is the special case where every job "
                     "has the same route. A job shop allows the routes to differ, and "
                     "that is the whole of the difficulty.")),
            ("def", ("Disjunctive pairs and orientations",
                     "Two operations needing the same machine form a "
                     "<strong>disjunctive pair</strong>, and an "
                     "<strong>orientation</strong> chooses, for every such pair, which "
                     "of the two goes first. With `k` pairs there are `2^k` "
                     "orientations. An orientation together with the route arcs is a "
                     "directed graph; when it is acyclic the earliest start times are a "
                     "forward pass over it and the makespan is its longest path.")),
            ("p", "That last sentence is the whole method and it is borrowed rather "
                  "than invented. Once every pair is oriented there is nothing left to "
                  "decide, and what remains is the project network of &ldquo;Networks: "
                  "Flows, Paths and Assignments&rdquo;, with the same forward pass and "
                  "the same longest path. The scheduling content is entirely in the "
                  "choice of orientation."),
            ("h3", "Two jobs, two machines, opposite routes"),
            ("math", [
                "operations, in each job’s own order",
                "   J1   M1 for 3,  then  M2 for 2",
                "   J2   M2 for 4,  then  M1 for 1",
                "",
                "   machine loads   M1 = 3 + 1 = 4     M2 = 2 + 4 = 6",
                "   job lengths     J1 = 5             J2 = 5",
                "   lower bound     max(4, 6, 5, 5) = 6",
                "",
                "two shared pairs — one on M1, one on M2 — so 2 to the 2 = 4 orientations",
                "",
                "   J2 first on M1,  J2 first on M2      makespan 10",
                "   J1 first on M1,  J2 first on M2      makespan  6     the best",
                "   J2 first on M1,  J1 first on M2      DEADLOCK",
                "   J1 first on M1,  J1 first on M2      makespan 10",
            ]),
            ("p", "The best orientation is the one that lets the two jobs start at once "
                  "on the machines they each need first. `J1` takes `M1` from `0` to "
                  "`3`; `J2` takes `M2` from `0` to `4`; then `J1` moves to `M2` at `4` "
                  "and finishes at `6`, and `J2` moves to `M1` at `4` and finishes at "
                  "`5`. The makespan is `6`, which equals the load on `M2` &mdash; that "
                  "machine never stopped, so nothing could have been faster."),
            ("example", ("The orientation that cannot be run",
                         "Choose `J2` before `J1` on `M1` and `J1` before `J2` on `M2`. "
                         "Now follow the requirements round: `J1`'s `M1` operation "
                         "waits for `J2`'s `M1` operation, which waits &mdash; by "
                         "`J2`'s own route &mdash; for `J2`'s `M2` operation, which "
                         "waits for `J1`'s `M2` operation, which waits &mdash; by "
                         "`J1`'s own route &mdash; for `J1`'s `M1` operation.",
                         "Four requirements in a circle, and not one of the four is "
                         "unreasonable on its own. Nothing can start. The lab reports "
                         "this orientation as deadlocked rather than assigning it a "
                         "makespan or quietly dropping it, and it counts how many of "
                         "the orientations are in that state: one of the four here, "
                         "seven of the sixteen on its three-job preset.")),
            ("h3", "Every orientation, scored"),
            ("p", "At this size the lab does the only completely honest thing: it "
                  "builds all `2^k` orientations, computes start times for each acyclic "
                  "one, and reads the schedule back off the drawing to check that no "
                  "machine runs two operations at once and no job starts a step before "
                  "the one before it finished. Then it reports the best, the count and "
                  "how many deadlocked."),
            ("math", [
                "preset          operations   pairs   orientations   deadlocked   best",
                "  two jobs           4          2           4            1         6",
                "  three jobs         5          4          16            7         9",
                "  one busy machine   5          4          16            4        10",
            ]),
            ("p", "`2^k` is the number to look at. Four pairs is sixteen orientations "
                  "and is comfortable; ten pairs is a thousand and is still fine; thirty "
                  "pairs is a billion and is not. The count of pairs grows roughly as "
                  "the square of the operations on the busiest machine, so a shop with "
                  "one machine everything passes through gets expensive fastest &mdash; "
                  "which is what the lab's third preset is for, with three of its four "
                  "pairs on a single machine."),
            ("h3", "Why this is where the course stops"),
            ("p", "There is no exchange argument here and there is not going to be. The "
                  "single-machine rules worked because a schedule was an order, two jobs "
                  "could be adjacent, and swapping them moved the objective by one "
                  "subtraction. In a job shop a schedule is a set of binary choices "
                  "whose feasibility is a property of the whole set &mdash; one flipped "
                  "bit can turn a working schedule into a deadlock &mdash; and no local "
                  "argument reaches that."),
            ("p", "What remains is search, and the search is the one "
                  "&ldquo;Integer Programming&rdquo; builds: branch on a disjunction, "
                  "bound each node, and report a gap when the tree has not closed. The "
                  "lower bound is free and worth taking &mdash; every machine's total "
                  "load and every job's total length are both lower bounds on the "
                  "makespan, since a machine cannot compress its own work and a job "
                  "cannot overlap its own operations. On the two-job shop that gives "
                  "`6`, which the best orientation attains, so the enumeration was "
                  "confirming something a bound had already proved."),
        ],
        "lab": ("schedule", {
            "mode": "jobshop",
            "preset": "two",
            "panel_title": "Orient every shared pair, score all of them, and draw the one you choose",
            "panel_intro": "Every orientation of every disjunctive pair is built and "
                           "scored, the deadlocked ones are counted as answers rather "
                           "than dropped, and the schedule drawn is read back off the "
                           "picture: no machine running two operations at once, and no "
                           "job starting a step before the one before it finished. The "
                           "slider picks an orientation by number so a deadlock can be "
                           "looked at directly.",
        }),
        "steps_title": "Working a job shop by orientations",
        "steps_intro": "Five steps, and the third is the one that decides whether there is a schedule at all.",
        "steps": [
            ("Write the operations out in each job's own order",
             "`job machine duration`, listed in route order for each job. The route is "
             "data and is not up for discussion; writing it in the wrong order produces "
             "a perfectly consistent answer to a different shop."),
            ("Find the pairs: two operations, one machine",
             "A machine with `r` operations on it contributes `r(r−1)/2` pairs, so the "
             "busiest machine dominates the count. Three operations on one machine is "
             "three pairs, and with a fourth pair elsewhere that is sixteen orientations "
             "to consider."),
            ("Choose an orientation and look for a cycle",
             "Draw the route arcs and the oriented arcs together and follow them. A "
             "cycle means no operation in it can start, and the orientation is a "
             "deadlock &mdash; not a slow schedule, not an error in the data, just a "
             "combination of choices that cannot be run."),
            ("On an acyclic orientation, run the forward pass",
             "Earliest start of an operation is the largest earliest finish among its "
             "predecessors, route arcs and disjunctive arcs alike. The makespan is the "
             "longest path, exactly as in a project network, and the critical path is "
             "the chain that holds it."),
            ("Compute the free lower bound before and after",
             "Every machine's total load and every job's total length bound the makespan "
             "from below. If the best orientation you have found attains the largest of "
             "them, you have a proof and can stop searching. On the two-job shop that "
             "bound is `6` and the best orientation attains it."),
        ],
        "worked": {
            "title": "Four operations, four orientations, and one of them impossible",
            "intro": [
                "The lab's opening preset in full: two jobs passing through two machines "
                "in opposite directions, which is the smallest shop in which the "
                "sequencing questions interact.",
            ],
            "lines": [
                "operations     J1  M1 3  then  M2 2",
                "               J2  M2 4  then  M1 1",
                "",
                "THE FREE BOUNDS",
                "   machine M1   3 + 1 = 4          machine M2   2 + 4 = 6",
                "   job J1       3 + 2 = 5          job J2       4 + 1 = 5",
                "   makespan ≥ max(4, 6, 5, 5) = 6",
                "",
                "THE FOUR ORIENTATIONS",
                "   J2 first on M1,  J2 first on M2",
                "       J2.M2 0–4   J2.M1 4–5   J1.M1 5–8   J1.M2 8–10        makespan 10",
                "   J1 first on M1,  J2 first on M2",
                "       J1.M1 0–3   J2.M2 0–4   J1.M2 4–6   J2.M1 4–5         makespan  6",
                "   J2 first on M1,  J1 first on M2",
                "       J1.M1 waits for J2.M1, which waits for J2.M2,",
                "       which waits for J1.M2, which waits for J1.M1          DEADLOCK",
                "   J1 first on M1,  J1 first on M2",
                "       J1.M1 0–3   J1.M2 3–5   J2.M2 5–9   J2.M1 9–10        makespan 10",
                "",
                "   best 6, attained by one orientation, and it equals the bound of 6",
                "   so no search was needed once both numbers were in hand",
            ],
            "after": [
                "The best schedule keeps `M2` working from `0` to `6` without a break, "
                "and `M2` carries six hours of work, so nothing could finish sooner. "
                "That is the bound and the schedule meeting each other, and it is why "
                "the free bounds are worth computing before any orientation is tried.",
                "The deadlock is the part worth rereading. Each of the four requirements "
                "in the cycle is individually sensible &mdash; two of them are the jobs' "
                "own routes and two are sequencing choices &mdash; and together they "
                "describe nothing. That is what makes this an integer programme: the "
                "feasibility of a set of binary choices is not a property of any one of "
                "them.",
                "For a rehearsal, switch to the three-job preset: five operations, four "
                "pairs, sixteen orientations. The supplied first move is that `M1` "
                "carries three of the five operations, so three of the four pairs are on "
                "`M1` alone. Predict how many of the sixteen deadlock before running it, "
                "and then compute the free bound from the machine loads and job lengths "
                "and compare it with the best makespan the enumeration finds.",
            ],
        },
        "quiz_title": "Orientations, cycles and where the rules ran out",
        "quiz": [
            {"q": "A shop has one machine carrying three operations and one machine carrying two. How many orientations are there?",
             "a": ["Five, one per operation", "Six, three times two",
                   "Sixteen: three pairs on the first machine and one on the second, so `2⁴`",
                   "Eight, `2³`"],
             "c": 2,
             "why": "A machine with `r` operations contributes `r(r−1)/2` pairs, so three "
                    "operations give three pairs and two give one: four pairs, `2⁴ = 16` "
                    "orientations. The busiest machine dominates the count, which is why "
                    "a shop with one machine everything passes through gets expensive "
                    "fastest."},
            {"q": "An orientation produces a directed graph with a cycle in it. What should be reported?",
             "a": ["A makespan of zero", "That the orientation deadlocks: no operation in the cycle can start, so this combination of choices has no schedule",
                   "The longest path ignoring the cycle", "An input error in the routes"],
             "c": 1,
             "why": "The routes are fine and the data are fine; this particular "
                    "combination of sequencing choices requires each of a set of "
                    "operations to wait for another. The lab counts the deadlocked "
                    "orientations &mdash; one of four here, seven of sixteen on the "
                    "three-job preset &mdash; because that count is part of what the "
                    "problem looks like."},
            {"q": "Why do the single-machine exchange arguments not apply to a job shop?",
             "a": ["Because the jobs have different durations",
                   "Because a schedule is a set of binary choices whose feasibility depends on the whole set: one flipped bit can turn a schedule into a deadlock, and no local comparison sees that",
                   "Because the makespan is a maximum",
                   "Because there is more than one machine"],
             "c": 1,
             "why": "The exchange arguments needed a schedule to be an order, with two "
                    "jobs adjacent and one subtraction settling the swap. Here the "
                    "objects are orientations, and flipping one bit can make the whole "
                    "thing infeasible. That is the either-or structure of "
                    "&ldquo;Integer Programming&rdquo;, and it is why the remaining tool "
                    "is search."},
            {"q": "The machine loads on a shop are `4` and `6` and the job lengths are `5` and `5`. What does that give you?",
             "a": ["A makespan of `20`, the total work",
                   "An upper bound of `6` on the makespan",
                   "A lower bound of `6`: no machine can compress its own work and no job can overlap its own operations",
                   "Nothing until an orientation is chosen"],
             "c": 2,
             "why": "Each of the four is a lower bound and the largest is `6`. On this "
                    "shop the best orientation attains `6`, so the bound and a feasible "
                    "schedule together prove optimality and the enumeration only "
                    "confirmed it. Computing the free bounds first is worth the seconds "
                    "it takes."},
        ],
        "mistakes": [
            ("Looking for a single sequence",
             "There is not one. Each machine serves the operations assigned to it in "
             "some order, and with different routes those orders are separate decisions "
             "that constrain each other. A reader who writes down one permutation of "
             "the jobs has answered the flow-shop question on job-shop data."),
            ("Treating a deadlock as a bug",
             "It is a feasible-looking set of choices with no schedule behind it, and it "
             "is a normal outcome: one of four orientations here and seven of sixteen on "
             "the three-job preset. Skipping them silently would make the enumeration "
             "look smaller than it is and would hide the reason this problem is hard."),
            ("Enumerating orientations at any scale",
             "`2^k` is fine for four pairs and hopeless for thirty, and `k` grows as the "
             "square of the operations on the busiest machine. The enumeration here is a "
             "teaching device that happens to be exact at this size; the method that "
             "survives is branch and bound on the same binary choices, with the free "
             "machine-load and job-length bounds at every node."),
        ],
        "standard": ("Finish when you can turn a shop into a set of binary choices and say which of them describe a schedule.",
                     "You should be able to list the operations in route order, find "
                     "every pair sharing a machine and count the orientations as `2^k`, "
                     "orient the pairs and draw the arcs, detect a cycle and report it as "
                     "a deadlock rather than a number, run a forward pass on an acyclic "
                     "orientation to get the makespan as a longest path, and compute the "
                     "machine-load and job-length lower bounds before deciding whether "
                     "any search is needed at all."),
        "note": 'That is the end of the sequencing half, and it ended by handing the question to a search. &ldquo;Crashing a Project and the Time-Cost Curve&rdquo; changes the currency. Until now time has been the only thing being spent; a project activity can also be shortened by paying for it, which makes the finish date a variable with a price attached and turns the question into a linear programme whose right-hand side is the deadline itself.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "crashing-a-project-and-the-time-cost-curve",
        "title": "Crashing a Project and the Time-Cost Curve",
        "module": "Buying time",
        "one_line": "Each activity can be shortened at a price; the cheapest way to meet a deadline is a linear programme, and the deadline is one right-hand side.",
        "summary": (
            "Project activities can be shortened by paying for them, at a known cost "
            "per day each, down to a floor. Minimising the bill subject to finishing by "
            "a deadline is a linear programme whose deadline is a single right-hand "
            "side, so the exact time-cost curve is the ranging function of "
            "&ldquo;Duality and Sensitivity Analysis&rdquo; applied to that row. The "
            "curve bends where the set of critical paths changes, and the first day is "
            "not always bought on the activity a reader expects."
        ),
        "key": [
            "each activity: normal duration and cost, crash duration and cost, y days bought",
            "rate = (crash cost − normal cost) / (normal − crash)      cost per day, constant",
            "min  sum rate·y   s.t.  finish ≤ deadline,  0 ≤ y ≤ normal − crash, path timing",
            "the normal cost is paid whatever the deadline: it shifts the curve, never bends it",
            "diamond project: normal 14 days, all-crash 9, normal cost 290",
            "the curve reading inwards: 15 a day, then 20, then 30, then 35 — convex",
        ],
        "key_label": "One programme, one moving right-hand side, four pieces",
        "concepts_intro": (
            "Three ideas: what the variables are, why the curve is convex, and why the "
            "programme's answer is checked by something that is not a programme."
        ),
        "concepts": [
            ("The variable is days bought, not the duration",
             "Write `y_i` for the number of days taken off activity `i`, between zero "
             "and its crash room `normal − crash`. Its duration is then `normal − y_i` "
             "and its cost is `normal cost + rate × y_i`. The objective is only "
             "`sum rate × y`, because the normal cost is paid whatever happens &mdash; "
             "`290` on the lab's project &mdash; and a constant in the objective shifts "
             "the curve without bending it."),
            ("The curve is convex, and the bends say why",
             "Each day taken off the finish costs at least as much as the day before. "
             "On the lab's project, reading from the loosest deadline inwards, the days "
             "cost `15`, `20`, `30` and `35`. The reason is on the screen at the moment "
             "it happens: once a second path becomes critical, a day off the finish has "
             "to be bought on both paths at once, and the bill per day is the sum of two "
             "rates rather than one."),
            ("The programme is checked by something that is not a programme",
             "A linear programme reports an optimal bill and a set of `y` values. "
             "Whether those durations actually finish the project on time is a separate "
             "question with a separate method: a forward and a backward pass over the "
             "crashed durations, sharing no arithmetic with the simplex. The lab runs "
             "it on every plan it prints, and re-solves each piece of the curve from "
             "scratch at its own endpoint as well."),
        ],
        "read_title": "Paying for days, the programme that spends the money, and the curve it traces",
        "read_intro": "The model, the rates, the programme, and the exact curve on a four-activity project where the first day is not bought where you would expect.",
        "body": [
            ("def", ("A crashable activity",
                     "An activity has a <strong>normal duration</strong> and a normal "
                     "cost, and a <strong>crash duration</strong> and a crash cost. "
                     "Its <strong>crash room</strong> is `normal − crash` days and its "
                     "<strong>rate</strong> is `(crash cost − normal cost) / (normal − "
                     "crash)`, the cost of one day, assumed constant across the range.",
                     "The decision variable `y_i` is the number of days bought on "
                     "activity `i`, with `0 ≤ y_i ≤ crash room`. The duration becomes "
                     "`normal − y_i` and the bill is `sum rate × y`.")),
            ("p", "Two refusals are worth naming because both are modelling errors "
                  "rather than typing errors, and the lab rejects them by name. An "
                  "activity that crashes to a <em>longer</em> duration is not a crashable "
                  "activity; and one that is <em>cheaper</em> crashed than normal makes "
                  "the normal plan the wrong baseline, so the whole curve is measured "
                  "from the wrong place."),
            ("def", ("The crashing programme",
                     "Minimise `sum rate_i y_i` subject to: `0 ≤ y_i ≤ crash room_i` "
                     "for every activity; a timing row for every precedence, saying "
                     "that an activity starts no earlier than its predecessors finish "
                     "with their crashed durations; and one <strong>deadline "
                     "row</strong> saying the project finish is at most `d`.",
                     "The deadline appears in exactly one row, as its right-hand side. "
                     "That is what makes the exact time-cost curve a right-hand-side "
                     "ranging problem rather than a family of separate solves.")),
            ("h3", "Four activities, two parallel paths"),
            ("math", [
                "activity   normal  crash   normal cost  crash cost   room   rate   after",
                "   A         6       4         100         140         2      20     —",
                "   B         4       2          80         120         2      20     A",
                "   C         5       3          60          90         2      15     A",
                "   D         3       2          50          80         1      30     B and C",
                "",
                "   normal cost 100 + 80 + 60 + 50 = 290, paid whatever the deadline",
                "   two paths:   A B D = 6 + 4 + 3 = 13     A C D = 6 + 5 + 3 = 14",
                "   at normal durations the project takes 14, critical A C D, B has 1 day of slack",
                "   with everything crashed it takes 9",
            ]),
            ("p", "The rates are the data to read first. `C` is the cheapest activity "
                  "to shorten at `15` a day, `A` and `B` cost `20`, and `D` costs `30`. "
                  "But cheapness is not the whole story: `A` and `D` lie on both paths, "
                  "so a day bought on either shortens the project by a day whatever "
                  "else is happening, while `B` and `C` each lie on one path and a day "
                  "bought there only helps while that path is the long one."),
            ("h3", "The exact curve, and where the first day is bought"),
            ("math", [
                "deadline   crash bill   total       bought",
                "   14           0         290       nothing",
                "   13          15         305       C by 1",
                "   12          35         325       A by 1, C by 1",
                "   11          55         345       A by 2, C by 1",
                "   10          85         375       A by 2, C by 1, D by 1",
                "    9         120         410       A by 2, B by 1, C by 2, D by 1",
                "",
                "the curve as four pieces, from the tightest deadline outwards",
                "    9 to 10    35 a day        10 to 11    30 a day",
                "   11 to 13    20 a day        13 to 14    15 a day",
                "",
                "   every piece re-solved from scratch at its own endpoint and confirmed",
            ]),
            ("example", ("The first day is bought on C, not on A",
                         "`A` is the obvious candidate: it is critical, it lies on both "
                         "paths, and shortening it always shortens the project. It is "
                         "also `20` a day, and it is not what the programme buys first. "
                         "The first day costs `15` and is bought on `C`.",
                         "The reason is the day of slack on `B`. At normal durations "
                         "`A C D` is `14` and `A B D` is `13`, so one day can be taken "
                         "off the longer path alone, and `C` is the cheapest way to do "
                         "it. After that day both paths are `13` and both are critical, "
                         "and from then on a day off the finish needs a day off both "
                         "&mdash; which is when `A`, at `20` a day on both paths at "
                         "once, becomes the cheapest thing to buy. Nothing is bought on "
                         "`A` until the two middle paths are critical together.")),
            ("p", "That ordering is read off the programme rather than reasoned "
                  "towards: the lab re-solves at every integer deadline, and `A` first "
                  "appears at `d = 12`. An argument starting from &ldquo;shorten the "
                  "critical activity on both paths&rdquo; buys `A` first and pays `20` "
                  "for a day that was on sale at `15`."),
            ("h3", "Reading the curve, and one trap in it"),
            ("p", "The slopes go `15, 20, 30, 35` as the deadline tightens, and each "
                  "increase has a cause. `15` buys the slack on `B`. `20` buys `A`, "
                  "which shortens both paths at once, for two days until `A` runs out "
                  "of room. `30` buys `D`, the other shared activity, at its higher "
                  "rate. `35` is the last day and it is bought on two activities at "
                  "once &mdash; `B` at `20` and a second day of `C` at `15` &mdash; "
                  "because by then every path must be shortened separately."),
            ("p", "The trap is counting pieces as rates. The lab's straight-chain "
                  "preset reports three pieces with slopes `15`, `20` and `20`: a piece "
                  "is an interval on which one basis stays optimal, and the basis can "
                  "change without the price per day changing."),
            ("h3", "Two checks, because the programme cannot check itself"),
            ("p", "The first is critical-path method run on the crashed durations. At "
                  "`d = 11` the plan buys `A` by two and `C` by one, giving durations "
                  "`A 4, B 4, C 4, D 3`; a forward and a backward pass over those "
                  "finish the project on day `11` with all four activities critical. "
                  "That is a different calculation from the simplex, done on the answer "
                  "the simplex produced, and the lab runs it on every plan it prints."),
            ("p", "The second is a fresh solve at each breakpoint. Ranging one "
                  "right-hand side through a sequence of bases is exactly the sort of "
                  "machinery that can drift, so every piece is re-solved from scratch "
                  "at its own left endpoint and the two values compared. The panel "
                  "reports the count, and on all three presets it is every piece."),
            ("p", "What the model leaves out is the usual gap between a project plan "
                  "and a project. The rates are constant and real overtime is not; the "
                  "activities are independent, so two crashed at once never compete for "
                  "the same people; and the durations are point estimates with no "
                  "uncertainty on them. The programme prices the plan it was given "
                  "exactly, which is a different thing from pricing the project."),
        ],
        "lab": ("schedule", {
            "mode": "crash",
            "preset": "diamond",
            "panel_title": "Set a deadline, buy the days, and check the plan with a method that is not the simplex",
            "panel_intro": "The programme is solved exactly, the durations it buys are "
                           "put through a forward and a backward pass to confirm the "
                           "deadline is really met, and every piece of the time-cost "
                           "curve is re-solved from scratch at its own endpoint. The "
                           "table of pieces gives the cost per day over each range of "
                           "deadlines, and the slider moves the deadline itself.",
        }),
        "steps_title": "Pricing a deadline",
        "steps_intro": "Five steps, and the last is the one that catches a plan that does not work.",
        "steps": [
            ("Compute every activity's crash room and rate",
             "Room is `normal − crash`; rate is the cost difference divided by the room, "
             "exactly. An activity with no room has no rate and is not a decision. Refuse "
             "an activity that is cheaper crashed than normal rather than modelling it: "
             "the normal plan is then not the baseline and the curve measures from the "
             "wrong place."),
            ("Run the critical-path method at normal durations, and again at crash durations",
             "The first gives the project length you are paying to reduce, and the slack "
             "on each activity; the second gives the floor below which no amount of money "
             "helps. On the lab's project that is `14` and `9`, and every deadline "
             "outside that range is either free or impossible."),
            ("Write the programme with the deadline as one right-hand side",
             "Days bought as the variables, rate times days as the objective, crash room "
             "as upper bounds, one timing row per precedence and one deadline row. The "
             "normal cost is not in the objective; add it back at the end."),
            ("Range the deadline row to get the whole curve at once",
             "This is right-hand-side ranging on a single row, and it produces exact "
             "breakpoints rather than a scan over sampled deadlines. Read the cost per "
             "day off each piece, and expect the slopes to rise as the deadline tightens."),
            ("Run the passes again on the durations you bought",
             "Forward and backward over `normal − y`, and confirm the project really "
             "finishes by the deadline. This is not a formality: it is the only check in "
             "the procedure that does not share arithmetic with the thing being checked, "
             "and it is what turns an optimal tableau into a plan you can hand to "
             "somebody."),
        ],
        "worked": {
            "title": "Fourteen days down to nine, and what each day cost",
            "intro": [
                "The lab's opening preset, priced at every integer deadline. Every "
                "figure is what the panel reports as the deadline slider is moved.",
            ],
            "lines": [
                "activities     A 6:4:100:140            room 2   rate 20",
                "               B 4:2:80:120  after A    room 2   rate 20",
                "               C 5:3:60:90   after A    room 2   rate 15",
                "               D 3:2:50:80   after B,C  room 1   rate 30",
                "",
                "AT NORMAL DURATIONS",
                "   A B D = 13      A C D = 14      project 14, critical A C D",
                "   slack   A 0   B 1   C 0   D 0",
                "   normal cost 290, paid whatever the deadline",
                "   fully crashed the project takes 9",
                "",
                "EVERY DEADLINE",
                "   d = 14    bill   0    total 290    buys nothing",
                "   d = 13    bill  15    total 305    C by 1          both paths now 13",
                "   d = 12    bill  35    total 325    A by 1, C by 1",
                "   d = 11    bill  55    total 345    A by 2, C by 1",
                "   d = 10    bill  85    total 375    A by 2, C by 1, D by 1",
                "   d =  9    bill 120    total 410    A by 2, B by 1, C by 2, D by 1",
                "",
                "THE CURVE, from the loosest deadline inwards",
                "   14 → 13   15 a day        13 → 11   20 a day",
                "   11 → 10   30 a day        10 →  9   35 a day",
                "",
                "CHECKING d = 11 WITH CPM, NOT WITH THE SIMPLEX",
                "   durations A 4, B 4, C 4, D 3",
                "   A B D = 11      A C D = 11      project 11, all four critical",
            ],
            "after": [
                "The first purchase is the one to remember. `A` is critical, lies on both "
                "paths and costs `20`; `C` is on one path and costs `15`. The programme "
                "buys `C`, because at normal durations `B` has a day of slack and only "
                "the longer path needs shortening. Buy `A` first and you have paid `20` "
                "for a day that was on sale at `15`.",
                "After that day both paths are `13` and every later day has to be bought "
                "on both. That is where the `20` comes from &mdash; `A` shortens both at "
                "once &mdash; and it is why the slopes only ever rise. Convexity here is "
                "not an assumption about the cost data; it is a consequence of paths "
                "becoming critical and never becoming uncritical again.",
                "For a rehearsal, switch to the preset where the cheapest activities are "
                "not the ones that matter: `A 4:2:40:48, B 7:4:60:120 | A, C 2:1:20:24, "
                "D 5:3:40:70 | C`. The supplied first move is that there are two chains, "
                "`A B` at `11` days and `C D` at `7`, so only the first decides the "
                "finish and `C` and `D` have four days of slack each. `A` and `C` both "
                "cost `4` a day, the cheapest on the project. Predict which one the "
                "programme buys and what the first two days cost, before the panel says.",
            ],
        },
        "quiz_title": "Rates, right-hand sides and the check that is not a solve",
        "quiz": [
            {"q": "Why is the normal cost left out of the objective?",
             "a": ["Because it is not known until the deadline is chosen",
                   "Because it is paid whatever the deadline, so it is a constant that shifts the curve without bending it or changing which plan is optimal",
                   "Because it would make the programme nonlinear",
                   "Because the crash costs already include it"],
             "c": 1,
             "why": "`290` is paid at every deadline on the lab's project. A constant in "
                    "the objective cannot change the argmin, so the programme minimises "
                    "the crash bill and the panel adds the normal cost back for the total "
                    "column."},
            {"q": "The lab's project has two paths, `A B D` at `13` days and `A C D` at `14`. Which activity does the programme buy the first day on?",
             "a": ["`A`, because it is on both paths and always shortens the project",
                   "`D`, because it is the last activity",
                   "`C`, at `15` a day, because only the longer path needs shortening while `B` still has a day of slack",
                   "`B`, because it has slack to give up"],
             "c": 2,
             "why": "`A` costs `20` and `C` costs `15`, and a day off `C` alone takes the "
                    "longer path from `14` to `13` while the other path is already `13`. "
                    "The programme buys `C` first and does not touch `A` until `d = 12`. "
                    "Buying the both-paths activity first is the natural move and costs "
                    "five more than it needs to."},
            {"q": "Why can the exact time-cost curve be produced by right-hand-side ranging rather than by solving at every deadline?",
             "a": ["Because the curve is a straight line",
                   "Because the deadline appears in exactly one row, as its right-hand side, so the curve is the optimal value as that one `b` moves",
                   "Because the rates are constant",
                   "Because the project network is acyclic"],
             "c": 1,
             "why": "One row, one right-hand side, and the ranging machinery of "
                    "&ldquo;Duality and Sensitivity Analysis&rdquo; applies unchanged. It "
                    "gives exact breakpoints rather than a scan over sampled deadlines, "
                    "and the lab re-solves each piece from scratch at its own endpoint to "
                    "confirm it."},
            {"q": "A solve returns an optimal bill and a set of days bought. What still has to be checked, and with what?",
             "a": ["Nothing: an optimal tableau is a proof",
                   "That the durations bought really finish the project by the deadline, using a forward and a backward pass over the crashed durations — a method that shares no arithmetic with the simplex",
                   "That the rates were entered correctly",
                   "That the bill is below the normal cost"],
             "c": 1,
             "why": "The tableau is optimal for the programme that was written down. "
                    "Running the critical-path method over `normal − y` asks a different "
                    "question with a different method, and it is the check that catches a "
                    "timing row that was formulated wrongly. At `d = 11` it finishes the "
                    "project on day `11` with all four activities critical."},
        ],
        "mistakes": [
            ("Buying the cheapest activity rather than the cheapest day",
             "A rate is the price of shortening an <em>activity</em>; what you are buying "
             "is a day off the <em>project</em>. An activity with slack is free of charge "
             "and worth nothing: on the lab's third preset, `C` costs `4` a day and lies "
             "on a chain with four days of slack, so a day bought there shortens nothing "
             "at all."),
            ("Counting curve pieces as distinct prices",
             "The lab's straight-chain preset reports three pieces with slopes `15`, `20` "
             "and `20`. A piece is an interval on which one basis stays optimal, and the "
             "basis can change without the cost per day changing. Read the slopes, not "
             "the count, and expect them to be non-decreasing rather than distinct."),
            ("Trusting the plan without re-running the passes",
             "An optimal tableau is optimal for the programme as written, and a timing "
             "row with the wrong predecessor in it produces a confident bill for a "
             "schedule that misses the deadline. The forward and backward passes over the "
             "crashed durations are the only step here that could catch that, which is "
             "why the lab runs them on every plan and reports the project length they "
             "find."),
        ],
        "standard": ("Finish when you can price a deadline exactly and check the plan by a method that is not the programme.",
                     "You should be able to compute crash rooms and rates as exact "
                     "fractions, run the critical-path method at normal and at crash "
                     "durations to bracket the deadlines that mean anything, write the "
                     "programme with the deadline as one right-hand side and the normal "
                     "cost outside the objective, read the exact curve off a ranging of "
                     "that row, say why the slopes rise, and confirm any chosen plan with "
                     "a forward and a backward pass over the durations it bought."),
        "note": 'This course began with a model in which the only currency was time and the makespan could not be moved at all, and ends with one in which the finish date has a price per day and the answer is a curve rather than a number. Everything between was proved by exchanging two neighbouring jobs, and the two places the exchange did not reach were named rather than papered over: total tardiness on one machine, and the orientation of a shared machine in a job shop. What follows on this path replaces the exchange with a backward recursion, and the first thing it does with it is the problem this course could not solve by sorting.',
    },
]
