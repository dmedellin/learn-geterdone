---
format: long
lesson: scheduling/the-job-shop-and-disjunctive-orientations
title: The job shop: one binary choice per pair, and schedules that deadlock
thumb: Some choices deadlock
---

@chapter The question
@title text="The Job Shop" sub="Scheduling" art=thumb
In a job shop, every job has its own route through the machines. So there's no single order to choose. What do you choose instead? And why can some perfectly reasonable choices produce a schedule that can never run?

@art two-routes
Each job is an ordered list of operations. This machine for so long, then that one. The route is fixed by the data. What's undecided is the order in which each machine serves the operations that need it.

@chapter One choice per pair
@art disjunctive-pair
Two operations that need the same machine can't overlap. One goes first. That's a disjunctive pair, and choosing which goes first is one binary decision. Choose for every pair, and you have an orientation. With k pairs, there are two to the k orientations.

@art oriented-network
Once every pair is oriented, nothing is left to decide. Add the route arcs and the chosen arcs, and the shop is an ordinary project network. A forward pass gives the start times, and the longest path is the makespan. The scheduling is entirely in the choice.

@chapter Two jobs, opposite routes
@math heading="The two-job shop" items="J1:  M1 for 3,  then M2 for 2@job one;;J2:  M2 for 4,  then M1 for 1@job two;;lower bound:  max(4, 6, 5, 5) = 6@lower bound"
Job one needs machine one for three, then machine two for two. Job two goes the other way: machine two for four, then machine one for one. Machine loads are four and six, and both jobs are five long. No machine can compress its work, so the lower bound is six.

@math heading="Two pairs: 4 orientations" items="J2 first on M1,  J2 first on M2:  10@ten;;J1 first on M1,  J2 first on M2:  6@six;;J2 first on M1,  J1 first on M2:  deadlock@deadlocks;;J1 first on M1,  J1 first on M2:  10@also ten"
There are two shared pairs, so four orientations. Two of them finish at ten. One finishes at six. And one deadlocks. The last one is also ten.

@art best-gantt
The best lets both jobs start at once on the machines they each need first. Job one takes machine one from zero to three. Job two takes machine two from zero to four. Then they cross over, finishing at six and five. Machine two never stopped, so six matches the bound.

@chapter The deadlock
@art deadlock-cycle
Now choose job two first on machine one, and job one first on machine two. Follow the waits round. Job one's first step waits for job two on machine one. That waits, by job two's route, for job two on machine two. That waits for job one on machine two, which waits, by job one's route, for job one's first step.

@words text="A deadlock is an answer, not an error"
Four requirements in a circle, and none unreasonable on its own. Nothing can start. That's not a bug to skip. It's a real outcome: one of four orientations here, and seven of sixteen on the lesson's three job preset.

@chapter Counting orientations
@art orientation-count
Two to the k is the number to watch. Four pairs is sixteen orientations, which is comfortable. Ten pairs is about a thousand, still fine. Thirty pairs is about a billion. And the pairs grow roughly as the square of the operations on the busiest machine.

@words text="No exchange argument here"
There's no exchange argument for this, and there won't be. One flipped choice can turn a working schedule into a deadlock, and no local swap can see that. What remains is search: branch on a pair, bound each node with machine loads and job lengths, and report a gap.

@chapter Where people slip
@list heading="Common slips" items="Looking for a single sequence@The first|Treating a deadlock as a bug@The second|Enumerating orientations at any scale@And the third"
The first slip is looking for a single sequence. That answers the flow shop question on job shop data. The second is treating a deadlock as a bug. And the third is enumerating orientations at any scale. It's exact at this size and hopeless at thirty pairs.

@chapter Try it
@words text="J1 first on M1, J1 first on M2" sub="find the makespan of 10"
Your turn. Orient both pairs with job one first. Run the forward pass by hand: when does each operation start and finish? Check the makespan comes out at ten, and say which machine waited, and why.

@end text="Orient every pair yourself"
You can orient each pair, watch the network form, and see which choices deadlock, on Learn. That's learn dot get er done dot I O.
