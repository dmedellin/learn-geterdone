---
format: long
lesson: scheduling/earliest-due-date-and-maximum-lateness
title: Earliest due date: optimal for the worst job, not for the total
thumb: Best worst, not best total
---

@chapter The question
@title text="Earliest Due Date" sub="Scheduling" art=thumb
Every job has a due date. Run the one due soonest first. It's the most useful rule in scheduling, and the most over claimed. Here's exactly what it promises, and two things it doesn't.

@art due-markers
For each job, lateness is its finish time minus its due date, and it can be negative. Tardiness clips that at zero. Four objectives come from these: the worst lateness, the worst tardiness, total tardiness, and the number of late jobs. They're four questions, not four spellings of one.

@chapter The exchange, with a maximum
@words text="EDD minimises L max, and T max"
The theorem: ordering by due date, earliest first, minimises the worst lateness. And since the worst tardiness is just that, clipped at zero, it minimises that too.

@art pair-swap-max
Take an adjacent pair where the first is due later than the second. Swap them. The job due sooner now finishes earlier than the pair used to. And the job due later finishes exactly when the pair used to, but against a later due date. So neither new lateness exceeds the old worst of the two.

@words text="The swap never hurts" sub="for a maximum, that's enough"
For total completion time, the swap gave an identity and a strict improvement. Here it only does no harm. That's normal for a maximum, and it's enough. Harmless swaps reach the due date order from anywhere, so nothing beats it.

@chapter Five jobs
@math heading="A 6:8,  B 4:4,  C 5:12,  D 3:6,  E 7:20" items="EDD:  B D A C E@B, D, A, C, E;;finish  4, 7, 13, 18, 25@finish times;;lateness  0, 1, 5, 6, 5@latenesses"
The lesson's five jobs, as time and due date. Earliest due date gives B, D, A, C, E. The finish times are four, seven, thirteen, eighteen, and twenty five. The latenesses are zero, one, five, six and five.

@art edd-order
So the worst lateness is six, set by C, which finishes at eighteen against a due date of twelve. Seventeen hours of work are due by hour twelve, so something has to be late. The rule's achievement is that nothing is more than six late, and checking all hundred and twenty orders confirms it.

@chapter The objective it doesn't solve
@math heading="Total tardiness" items="EDD  B D A C E:  Σ T = 17,  late 4@seventeen;;best  B D C A E:  Σ T = 16,  late 3@sixteen;;but its L max = 10@ten"
But its total tardiness is seventeen, with four jobs late. The best total is sixteen, from B, D, C, A, E. That order differs by one swap: C and A change places. And its worst lateness is ten, not six.

@art worst-vs-total
C now finishes at twelve, exactly on time, while A slides from thirteen to eighteen, going from five hours tardy to ten. The total falls by one, because one job dropped six while another rose five. Both orders are optimal, for different objectives.

@words text="Fewest late jobs: 2, not 4"
And the fewest late jobs possible is two, where earliest due date leaves four. That has its own rule, in the next lesson.

@chapter Where the method stops
@art no-rule-boundary
Total tardiness on one machine has no adjacent exchange rule. Each job's tardiness is clipped, so the same swap moves the total by different amounts in different parts of the schedule. The lesson enumerates instead, and says so, rather than inventing a plausible heuristic.

@chapter Where people slip
@list heading="Common slips" items="Hearing minimises lateness as minimises it in total@The first|Clipping negatives before taking the maximum@The second|Ordering by slack and calling it EDD@And the third"
The first slip is hearing minimises lateness as minimises it in total. The second is clipping the negatives before taking the maximum, which computes tardiness instead. And the third is ordering by slack, due date minus time, and calling it earliest due date. On the opening jobs, slack gives a worst lateness of seven.

@art clipped-tardiness
On that second slip: a job finishing two hours early has a lateness of minus two. On an all early schedule, the signed worst lateness is the informative one.

@chapter Try it
@words text="Run B D C A E" sub="A 6:8 · B 4:4 · C 5:12 · D 3:6 · E 7:20"
Your turn. Run the clock on B, D, C, A, E. Write each finish time and each tardiness. Check the total tardiness is sixteen and the worst lateness is ten. Then decide which order you'd run if a customer only cared about the worst job.

@end text="See which objective a rule solves"
You can run any order and see all four due date objectives side by side, on Learn. That's learn dot get er done dot I O.
