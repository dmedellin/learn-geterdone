---
format: long
lesson: scheduling/two-machines-in-series-and-johnsons-rule
title: Johnson's rule: keep the second machine from waiting
thumb: Starve the second machine less
---

@chapter The question
@title text="Two Machines in Series" sub="Scheduling" art=thumb
On one machine, the makespan never changes. Add a second machine in series, and suddenly the order matters a lot. Why? And which order finishes soonest?

@art two-machines
Every job goes through machine one, then machine two. Each machine runs one job at a time, nothing is interrupted, and every job uses the same order on both. So one permutation is the whole decision.

@chapter Where the time goes
@math heading="The clock" items="C1(k) = C1(k−1) + p1(k)@machine one;;C2(k) = max(C1(k), C2(k−1)) + p2(k)@machine two"
Machine one just runs a running total: each job finishes when the last one did, plus its own time. Machine two can't start job k until that job has left machine one, and until machine two itself is free. So it takes the later of the two, then adds the job's time.

@art gantt-two-rows
That max is where the whole problem lives. Machine one never stops. Machine two sometimes waits. And machine two's timeline is made of exactly two things: work, and waiting.

@words text="makespan = work on M2 + idle on M2" sub="the work never changes"
The work on machine two is the same in every order. So minimising the makespan is the same as minimising the time machine two stands idle. Waiting jobs cost nothing here. A waiting machine costs the makespan.

@chapter Johnson's rule
@art johnson-split
Split the jobs. Those quicker on machine one go to the front, shortest on machine one first. They get machine two started early. The rest go to the back, longest on machine two first, so that a long tail isn't what's left at the end.

@math heading="A 5:2,  B 1:6,  C 9:7,  D 3:8,  E 10:4" items="front, p1 < p2:  B, D@front;;back, by p2 down:  C, E, A@The rest;;Johnson:  B D C E A@order is B"
The lesson's five jobs, as machine one time and machine two time. B and D are quicker on machine one, so they go to the front, by machine one time: B, then D. The rest, by machine two time, longest first: C at seven, E at four, A at two. Johnson's order is B, D, C, E, A.

@chapter Counting the idle hours
@math heading="Work on M2 = 27 in every order" items="Johnson  B D C E A:  idle 1 + 1 + 1 = 3,  makespan 30@Johnson's;;typed  A B C D E:  idle 5 + 2 = 7,  makespan 34@typed order"
Machine two does twenty seven hours of work in every order. Under Johnson's order it idles one, one and one, three hours, finishing at thirty. In the typed order it idles five and two, seven hours, finishing at thirty four. And thirty is the best of all hundred and twenty orders.

@art starved-start
Where did those five hours go? In the typed order, A holds machine one for five hours before anything can be handed over. Johnson's order puts B first, which needs machine one for just one hour, so machine two starts at one instead of five.

@art idle-gaps-shrink
The lesson has a preset that makes this stark. Four jobs, where the typed order opens with eight hours on machine one and one on machine two. It finishes at thirty five, with eighteen hours idle. Johnson's rule finishes at twenty four, with seven idle. Eleven hours saved.

@words text="Best 30, attained by 2 orders" sub="Johnson's is one of them"
And report ties honestly. On the five jobs, two orders reach thirty, and Johnson's is one. Naming one order as the unique optimum would be a claim nobody made.

@chapter Where this stops
@art three-machines
Three machines in series is a different problem, and this rule doesn't extend to it. In general that case is hard. So the method is offered for two machines, and it says so.

@chapter Where people slip
@list heading="Common slips" items="Sorting the whole list by one key@The first|Trying to improve machine one@The second|Carrying over the one-machine intuition@And the third"
The first slip is sorting the whole list by one key. Sorting everything by machine one time gives B, D, A, C, E, which doesn't reach thirty. The second is trying to improve machine one. It never has gaps. And the third is carrying over the one machine intuition that the makespan can't move.

@chapter Try it
@words text="Run B D A C E" sub="A 5:2 · B 1:6 · C 9:7 · D 3:8 · E 10:4"
Your turn. Run the two machine clock on B, D, A, C, E, the order you get by sorting everything on machine one time. Write each finish time on machine two, add up the idle hours, and see how far it lands from thirty.

@end text="Run the two-machine clock"
You can type any order and watch the second machine's idle time grow and shrink, on Learn. That's learn dot get er done dot I O.
