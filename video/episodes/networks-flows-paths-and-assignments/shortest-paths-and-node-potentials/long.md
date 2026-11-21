---
format: long
lesson: networks-flows-paths-and-assignments/shortest-paths-and-node-potentials
title: Shortest-path labels are prices: node potentials and the dual
thumb: Distances are prices
---

@chapter The question
@title text="Shortest Paths and Node Potentials" sub="Networks, Flows, Paths and Assignments" art=thumb
Every shortest path algorithm hands you a label at each node. You'd probably call them distances. But they're something more useful than that: a solution to a dual programme. And that changes what you can do with them.

@chapter Relaxation
@art relax-arc
Start with zero at the source and no label anywhere else. Then relax every arc: if the label at the tail plus the arc's cost beats the label at the head, lower the head. Repeat, round after round, until nothing moves.

@math heading="Arcs s→a 4, s→b 2, b→a 1, a→t 3, b→t 7" items="round 1:  s 0,  a 3,  b 2,  t 6@round one;;round 2:  nothing moved, stop@round two"
On the lesson's network, after round one the labels are zero, three, two and six. In round two, nothing moves, so you stop. The second round is what proves you're done.

@art detour-cheaper
Notice a ends at three, not four. The direct arc from s costs four, but the detour through b costs two plus one, which is three. So the direct arc ends up with room to spare.

@chapter The dual
@math heading="Node potentials" items="πⱼ − πᵢ ≤ cᵢⱼ  on every arc@on every arc;;max  πₜ − πₛ@maximise"
Here's the dual. Give each node a potential, pi. On every arc from i to j, the potential at the head may exceed the one at the tail by at most the arc's cost. And you maximise pi at the sink minus pi at the source.

@words text="Any feasible π: πₜ − πₛ ≤ any path's cost"
Add those constraints along any path from source to sink, and the middle terms cancel. So any feasible set of potentials gives a lower bound on every path. That's weak duality, in one line.

@math heading="Reduced cost  c − (πⱼ − πᵢ)" items="s→a:  4 − 3 = 1  slack@s to a;;s→b:  2 − 2 = 0  tight@s to b;;b→a:  1 − 1 = 0  tight@b to a;;a→t:  3 − 3 = 0  tight@a to t;;b→t:  7 − 4 = 1  slack@b to t"
Now check every arc. S to a has one to spare. S to b is tight. B to a, tight. A to t, tight. B to t has one to spare. Every arc passes, so the labels are feasible.

@art tight-arcs
And look at the tight arcs. They're exactly the route s, b, a, t, which costs six. The dual objective is six minus zero, also six. Flow only travels on tight arcs. That's complementary slackness.

@chapter Why they're prices
@art float-potentials
Add seven to every label: seven, ten, nine, thirteen. Every constraint is a difference, so the seven cancels. Everything still holds, the objective is still six, and the same arcs are tight. The whole vector floats.

@art one-potential-moved
But add five to one label only, and arcs break. The vector floats as a whole, not piece by piece. That's exactly how prices behave. A distance is just one choice, setting the source to zero.

@chapter Negative arcs, negative cycles
@words text="s→a 4, s→b 2, a→b −3, b→t 2, a→t 6" sub="labels 0, 4, 1, 3"
A negative arc is fine. On this network the labels settle at zero, four, one and three. The cheapest way to b goes through a, at four minus three, which is one. An arc that earns rather than spends is perfectly meaningful.

@art negative-cycle
A negative cycle is different. Take x to y at one, y to z at minus three, and z to x at one. Add the constraints round the cycle, and the labels cancel, leaving zero at most minus one. Impossible. No potentials exist.

@words text="Labels fall by one every round" sub="cycle y, z, x costs −1"
Relaxation finds this by never settling. The labels drop by one every round. On the primal side the problem is unbounded: go round the cycle forever and the cost falls forever. An infeasible dual, and an unbounded primal.

@chapter Where people slip
@list heading="Common slips" items="Calling the labels distances and stopping there@The first|Confusing a negative arc with a negative cycle@The second|Checking a potential only along the route@And the third"
The first slip is calling the labels distances and stopping there. The second is confusing a negative arc with a negative cycle. And the third is checking a claimed potential only along the route. Feasibility is about every arc, and the arcs off the route are where a wrong claim hides.

@chapter Try it
@words text="Labels 0, 4, 1, 3" sub="s→a 4, s→b 2, a→b −3, b→t 2, a→t 6"
Your turn. Take the network with the negative arc and its labels zero, four, one, three. Compute the reduced cost on all five arcs. Confirm none is negative, and that the three tight arcs are s to a, a to b, and b to t.

@end text="Relax the arcs yourself"
You can relax the arcs, shift every label, and break a constraint on purpose, on Learn. That's learn dot get er done dot I O.
