---
format: long
lesson: intro-algorithms-graphs/bellman-ford-and-dag-shortest-paths
title: Bellman-Ford and shortest paths in a dag
thumb: Negative edges are fine
---

@chapter The real worry
@title text="Bellman-Ford and Shortest Paths in DAGs" sub="Introduction to Algorithms, Sections 24.1–24.2" art=thumb
Chapter twenty four asks for the shortest path from one source to every vertex, where a path's weight is the sum of its arcs' weights, and weights may be negative.

@quote text="Shortest paths are always well defined in a dag, since even if there are negative-weight edges, no negative-weight cycles can exist." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 24.2"
A negative edge isn't a problem in itself. As section twenty four point two puts it: shortest paths are always well defined in a dag, since even if there are negative weight edges, no negative weight cycles can exist.

@art negative-cycle
What breaks things is a negative cycle reachable from the source. Going round it again always lowers the total, so no path through it is ever the cheapest.

@chapter Relaxation
@math heading="RELAX(u, v, w)" items="start: s.d = 0, every other v.d = ∞@every vertex keeps;;if v.d > u.d + w: v.d = u.d + w, v.π = u@lower v dot d"
Every vertex keeps an estimate. It starts at infinity, and zero at the source. Relaxing the arc from u to v asks whether going through u helps. If u dot d plus the weight is smaller, lower v dot d to it, and record u as v's predecessor.

@art relax-arc
Relaxation never pushes an estimate below the true distance. And if the arcs of a shortest path are relaxed in path order, with anything else in between, the last estimate becomes exact. Every algorithm in the chapter is a schedule of relaxations that guarantees that order.

@chapter Bellman-Ford
@art rounds
Bellman Ford is the bluntest schedule. Make V minus one passes, and in each one relax every arc. A shortest path can be taken to be simple, so it has at most V minus one arcs, and pass i fixes the i th arc of every shortest path at the latest.

@words text="One more look: any improvement ⇒ negative cycle" sub="O(VE)"
Then one more look at every arc. If any arc could still lower an estimate, a negative cycle is reachable, and the procedure returns false. The running time is O of V times E.

@chapter The lesson's graph
@math heading="1>2 4 · 1>3 5 · 2>4 −2 · 3>2 −3 · 3>4 3 · 4>5 2 · 2>5 6" items="after round 1: 0, 2, 5, 2, 4@round one;;after round 2: 0, 2, 5, 0, 2@round two;;round 3: no change@round three"
The lesson's graph has five vertices and seven arcs, three of them negative, and no cycle. After round one, the labels are zero, two, five, two, four. After round two, zero, two, five, zero, two. And round three changes nothing.

@art shortest-tree
The longest shortest path, one, three, two, four, five, has four arcs. Every label was final no later than its own path's arc count, just as the induction says. And the predecessors form a shortest paths tree rooted at the source.

@art reverse-order
The lab stops when a round changes nothing. Type the same arcs in reverse order, and it needs four rounds instead of three. The book's procedure would make all four passes either way, twenty eight calls to relax.

@words text="Add 5>3 −1" sub="cycle 2 → 4 → 5 → 3 → 2, weight −4"
Now add one arc, five to three, of weight minus one. The lab reports the negative cycle two, four, five, three, two, of weight minus four, and refuses to call anything a distance.

@chapter One pass in a dag
@art topo-pass
In a dag, one pass is enough. Sort the vertices topologically, and relax the arcs leaving each vertex as you reach it. Every path visits its vertices in that order, so every shortest path is relaxed in path order. That's theta of V plus E.

@math heading="Order 1, 3, 2, 4, 5" items="from 1: d[2] = 4, d[3] = 5@From one;;from 3: d[2] = 2, d[4] = 8@From three;;from 2: d[4] = 0, d[5] = 8@From two;;from 4: d[5] = 2@From four"
From one, d two becomes four, and d three five. From three, d two falls to two, and d four becomes eight. From two, d four falls to zero, and d five becomes eight. From four, d five falls to two. Seven relaxations, one per arc, and the same distances.

@chapter Where people slip
@list heading="Common slips" items="Negative weights make paths undefined@The first|Bellman-Ford always needs every round@The second|The dag algorithm needs nonnegative weights@the third"
The first slip is thinking a negative weight makes shortest paths undefined. Only a reachable negative cycle does. The second is expecting Bellman Ford to need all its rounds on every graph. And the third is believing the dag algorithm needs nonnegative weights. It needs no cycle, whatever the signs.

@chapter Try it
@words text="1>2 6 · 1>3 2 · 3>2 3 · 2>4 −4 · 3>4 5 · 4>5 1 · 3>5 4" sub="Bellman-Ford, then the dag algorithm"
Your turn. Run Bellman Ford by hand from one, with the arcs in this order, writing the labels after each pass. Then run the dag algorithm in a topological order, and count the relaxations each needs.

@end text="Watch the rounds"
You can watch Bellman Ford round by round and find negative cycles, on Learn. That's learn dot get er done dot I O.
