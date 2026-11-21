---
format: long
lesson: scheduling/machines-in-parallel-and-the-lpt-bound
title: Longest job first on parallel machines, and what it guarantees
thumb: A bound is not a schedule
---

@chapter The question
@title text="Machines in Parallel" sub="Scheduling" art=thumb
Three identical machines, seven jobs. Each job goes on one machine. You want the last machine to finish as soon as possible. There's no rule that's always optimal here. But there's a rule with a guarantee, and two bounds to measure it against.

@art parallel-machines
Each machine's load is the total time of its jobs, and the makespan is the largest load. The order within a machine doesn't matter. So a schedule is just a split of the jobs into groups, an assignment, not an order. There's nothing adjacent to swap.

@chapter Two lower bounds
@art average-bound
First bound: the loads add up to the total work, so the largest is at least the average. Total work over the number of machines.

@art longest-bound
Second bound: the longest job runs on one machine without a break, so the makespan is at least that job's length. Neither bound implies the other.

@math heading="A 7, B 6, C 5, D 4, E 4, F 4, G 4 on 3" items="average:  34/3 ≈ 11.33@thirty four thirds;;longest:  7@seven;;binding bound:  34/3@binding"
On the lesson's seven jobs, the total is thirty four. The average is thirty four thirds, about eleven point three three. The longest job is seven. So the average is the binding bound. With one eleven hour job and four small ones, it's the other way round.

@chapter Longest first
@art lpt-placing
The rule: sort the jobs longest first, and place each one on whichever machine is free soonest. One pass, no going back. Seven, six and five go on the three machines. Then come four fours, onto loads of seven, six and five.

@math heading="LPT" items="M1:  A 7, F 4  =  11@machine one;;M2:  B 6, E 4  =  10@machine two;;M3:  C 5, D 4, G 4  =  13@machine three"
They go to the third, the second, the first, and the third again. Machine one carries eleven, machine two carries ten, and machine three carries five plus four plus four, thirteen. The makespan is thirteen.

@math heading="Best of all 2187 assignments" items="M1:  A 7, C 5  =  12@seven with the five;;M2:  B 6, D 4  =  10@six with a four;;M3:  E 4, F 4, G 4  =  12@three fours"
The best of all two thousand one hundred and eighty seven assignments pairs the seven with the five, the six with a four, and puts three fours together. Twelve, ten, and twelve. The makespan is twelve. A one pass rule would never find that.

@chapter Three different numbers
@art bound-gap
So the bound is thirty four thirds, the optimum is twelve, and the heuristic is thirteen. Thirty four doesn't divide by three, and every load is whole, so nothing reaches the bound. The gap from thirteen to twelve is the heuristic's failure. The gap from twelve down to the bound isn't anybody's failure.

@words text="Ratio 13/12  ≤  4/3 − 1/9 = 11/9"
Longest first is proved to finish within four thirds minus one over three m of the best. On three machines that's eleven ninths. The measured ratio here is thirteen twelfths, comfortably inside. But one measured ratio isn't evidence about the guarantee in either direction.

@chapter When the bound is tight
@words text="One 11-hour job: bound 11, LPT 11, optimum 11"
With one eleven hour job and four small ones, the longest job bound is eleven, longest first finishes at eleven, and so does the optimum. With six four hour jobs on three machines, it's eight, eight and eight. Those are just instances where the bound happens to be reachable. Compute both bounds first: if they meet the heuristic, you're done.

@chapter The rival rule
@art lpt-vs-best
Shortest first is the natural rival, and it's much worse. On the seven jobs it finishes at fifteen, because it spends the small jobs early and then has to drop the seven hour job onto a machine that's already loaded. That's why the rule sorts descending.

@chapter Where people slip
@list heading="Common slips" items="Reading the average bound as a target@The first|Sorting the jobs ascending@The second|Reporting a heuristic value with no bound@And the third"
The first slip is reading the average bound as a target you can reach. The second is sorting the jobs ascending. And the third is reporting a heuristic value with no bound. Thirteen alone says nothing. Thirteen, against a bound of thirty four thirds and an optimum of twelve, says three things.

@chapter Try it
@words text="Six 4-hour jobs on 3 machines" sub="both bounds, then LPT"
Your turn. Take six four hour jobs on three machines. Compute the average load bound and the longest job bound, and say which binds. Then place the jobs longest first, and check the makespan meets the bound.

@end text="Place the jobs yourself"
You can place jobs on parallel machines and compare both rules against both bounds, on Learn. That's learn dot get er done dot I O.
