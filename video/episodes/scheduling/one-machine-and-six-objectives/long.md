---
format: long
lesson: scheduling/one-machine-and-six-objectives
title: One machine, five jobs, six objectives, and no single best order
thumb: Best at none of them
---

@chapter The question
@title text="One Machine, Six Objectives" sub="Scheduling" art=thumb
Five jobs, one machine. You run them in the order they arrived. Is that a good schedule? The honest answer is: good at what? There are six reasonable things to measure, and they disagree.

@art one-machine-queue
Here's the model. Each job has a processing time, a weight, and a due date. One machine runs one job at a time, every job is ready at time zero, nothing is interrupted, and the machine never idles. So a schedule is just an order.

@chapter The six objectives
@list heading="For each job j" items="C: finish time@finish time|L = C − d: lateness@lateness|T = max(L, 0): tardiness@tardiness|U = 1 if late@counts one"
For each job, C is its finish time. Lateness is the finish time minus the due date, and it can be negative. Tardiness clips that at zero. And U counts one if the job is late, zero if not.

@list heading="Six objectives" items="Σ C@total completion|Σ wC@weighted total|L max@maximum lateness|T max@maximum tardiness|Σ T@total tardiness|Σ U@number of late jobs"
The six objectives are total completion time, the weighted total, maximum lateness, maximum tardiness, total tardiness, and the number of late jobs. All to be made small.

@chapter The one that never moves
@art same-makespan
There's a seventh, the makespan: when the last job finishes. And on this model it never changes. The machine starts at zero and never stops, so the last job finishes when the work runs out. That's six plus four plus five plus three plus seven, twenty five, in every one of the hundred and twenty orders.

@art idle-gap
Drop any assumption and that breaks. Release dates force idle time. A second machine makes the makespan the hard part. And setups that depend on the previous job change the total work itself.

@chapter One order, six verdicts
@math heading="Arrival order A B C D E" items="Σ C = 74,  Σ wC = 165@seventy four;;L max = 12,  T max = 12@twelve;;Σ T = 26,  late 4 of 5@twenty six;;makespan 25@twenty five"
Run them as they arrived, A, B, C, D, E. Total completion time is seventy four, weighted total a hundred and sixty five. Maximum lateness and maximum tardiness are both twelve. Total tardiness is twenty six, with four of five jobs late. And the makespan, twenty five.

@art lateness-vs-tardiness
Every one of those is read off one clock. Job A finishes at six against a due date of eight, so its lateness is minus two and its tardiness is zero. Early jobs pull lateness down and add nothing to tardiness.

@chapter Against every order
@math heading="Best of all 120 orders" items="Σ C: 65  ·  D B C A E@sixty five;;Σ wC: 108  ·  D C B A E@a hundred and eight;;L max, T max: 6  ·  B D A C E@six;;Σ T: 16  ·  B D C A E@sixteen;;Σ U: 2  ·  A C E B D@two late"
Now score all hundred and twenty orders. The best total completion is sixty five. The best weighted total is a hundred and eight. The best maximum lateness and tardiness are both six. The best total tardiness is sixteen, and the fewest late jobs is two late. The arrival order is best at none of them.

@art different-winners
And look at who wins. Five different orders. Shortest first wins total completion time. Smith's ratio wins the weighted total. Earliest due date wins maximum lateness. Being best at one of these normally means being beaten on the rest.

@art six-dials
Shortest first, provably optimal for total completion time, costs a hundred and fourteen on the weighted version. Heaviest weight first sounds just as reasonable, and costs a hundred and eleven. Same orders, different questions.

@chapter Choose the objective first
@words text="Which number are you paid to make small?"
So the first step isn't choosing a rule. It's writing down which number you're being paid to make small. A workshop judged on how many orders ship late shouldn't run shortest first. An answer that's right about the wrong objective is still wrong, and nothing in the solve will say so.

@chapter Where people slip
@list heading="Common slips" items="Resequencing to improve the makespan@The first|Reading optimal as optimal for everything@The second|Treating lateness and tardiness as one column@And the third"
The first slip is trying to improve the makespan by resequencing. There's nothing there. The second is reading optimal as optimal for everything. Each theorem names one objective. And the third is treating lateness and tardiness as the same column.

@chapter Try it
@words text="Score D B C A E" sub="A 6:1:8 · B 4:2:4 · C 5:4:12 · D 3:3:6 · E 7:1:20"
Your turn. Take the shortest first order, D, B, C, A, E. Run the clock, and write each job's finish time. Check the total comes to sixty five, and the makespan is still twenty five. Then count how many jobs are late.

@end text="Score every order at once"
You can type an order and see it scored against all six objectives and all hundred and twenty orders, on Learn. That's learn dot get er done dot I O.
