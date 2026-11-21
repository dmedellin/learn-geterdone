---
format: long
lesson: graph-algorithms/relaxation-and-dijkstras-schedule
title: Dijkstra is a schedule: one step, three orders, same distances
thumb: One step, many schedules
---

@chapter The question
@title text="Relaxation and Dijkstra's Schedule" sub="Graph Algorithms" art=thumb
Dijkstra's algorithm, Bellman Ford, the DAG method. They look like three different algorithms. They're really one line of arithmetic, applied in different orders.

@chapter The step
@math heading="Relax the edge u → v" items="if d[u] + w < d[v]@if d of u;;  d[v] = d[u] + w,  parent[v] = u@set d of v"
Here's the line. Every vertex has a label d, starting at infinity, except the source at zero. To relax an edge from u to v of weight w: if d of u plus w is less than d of v, set d of v to d of u plus w, and record u as v's predecessor.

@art relax-step
In words: if going to u and then along this edge beats the best known route to v, write the better number down.

@chapter It never undershoots
@words text="d[v] is always ∞ or the length of a real path"
And here's the invariant. At every moment, d of v is either infinite or the length of some actual path from the source. So it's never below the true distance.

@list heading="Proof by induction" items="Start: only the source, at 0, the empty path@Before any|Step: d[u] is a path, add the edge@appending"
Before any relaxation, only the source has a finite label, and zero is the empty path. And if d of u is the length of some path to u, appending the edge gives a path to v of length exactly d of u plus w. No path is shorter than the shortest one.

@art upper-bound
Picture one label over time. It starts at infinity and only ever steps down. It can land on the true distance, but never below it.

@art three-schedules
So no schedule can underestimate. Every schedule is just a rule for which edge to relax next. The only questions are whether the labels reach the truth, and how much work that takes.

@chapter Three schedules
@list heading="Three schedules" items="Nearest unfinished first, from a heap@Nearest unfinished|The same choice, by scanning every label@scanning|Arc order, sweep until nothing changes@Arc order"
Nearest unfinished first: keep a heap of labels, pop the smallest, call it finished, and relax its edges. That's Dijkstra's schedule. The same choice, found by scanning every label instead of a heap. And arc order: ignore distance, sweep the whole edge list, and repeat until a sweep changes nothing.

@math heading="Six vertices, from 1" items="distances:  0, 7, 9, 20, 20, 11@zero, seven, nine;;route to 5:  1, 3, 6, 5 = 9 + 2 + 9 = 20@route to vertex five"
On the lab's six vertex graph from vertex one, all three reach zero, seven, nine, twenty, twenty, eleven. So does an independent Dijkstra from another subject. The route to vertex five is one, three, six, five, at nine plus two plus nine, twenty.

@math heading="What each schedule cost" items="heap:  18 relaxations · 8 pushes · 8 pops · 15 comparisons@the heap;;scan:  18 relaxations · 42 label reads@the scan;;arc order:  36 relaxations@arc order"
But the work differs. The heap does eighteen relaxations, with eight pushes, eight pops and fifteen comparisons. The scan does the same eighteen relaxations, because it makes the same choices, but needs forty two label reads to find them. And arc order does thirty six, twice as many, because a second sweep has to confirm nothing changed.

@art sparse-dense
On a chain, the scan does fifty six label reads, while the heap needs no key comparisons at all. On ten edges over five vertices, it's thirty reads against fourteen comparisons. The heap's advantage is biggest where the frontier is small, the sparse case.

@chapter Settling early
@art settled
What nearest first buys is settling. Once a vertex is the closest unfinished one, it's finished, and never reconsidered. That's only sound because every weight is at least zero, so nothing reached later can offer a cheaper route back.

@art negative-undirected
And on an undirected graph, a negative weight is a negative cycle. Walk the edge and walk back, and the total falls by twice the weight. On one two at minus three, the heap schedule gives the source a label of minus six, when its distance to itself is zero. Negative weights belong to directed arcs.

@chapter Where people slip
@list heading="Common slips" items="Confusing the step with the schedule@The first|Settling without non-negative weights@The second|Reading the reference column as a budget@And the third"
The first slip is confusing the step with the schedule. Dijkstra names a schedule. The second is trusting a settled vertex without non negative weights. And the third is reading the reference column as a budget. On the opening graph it equals the relaxation count, eighteen, by coincidence.

@chapter Try it
@words text="Relax the six-vertex graph in arc order" sub="count the sweeps"
Your turn. Take the six vertex graph and relax the edges in the order they're listed, sweep after sweep. Record the labels after each sweep, and check you reach the same distances.

@end text="Switch the schedule"
You can switch between the three schedules and watch the counts change while the distances don't, on Learn. That's learn dot get er done dot I O.
