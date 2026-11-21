---
format: long
lesson: intro-algorithms-graphs/all-pairs-shortest-paths
title: All-pairs shortest paths: Floyd-Warshall and Johnson
thumb: One more vertex at a time
---

@chapter The whole table
@title text="All-Pairs Shortest Paths" sub="Introduction to Algorithms, Chapter 25" art=thumb
Chapter twenty five wants every distance at once.

@quote text="This problem might arise in making a table of distances between all pairs of cities for a road atlas." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 25"
As the authors put it, this problem might arise in making a table of distances between all pairs of cities for a road atlas.

@words text="V × single source" sub="Dijkstra O(V³) · Bellman-Ford O(V²E)"
The obvious answer runs a single source algorithm from every vertex. Dijkstra V times, O of V cubed with an array, if no weight is negative. Otherwise Bellman Ford V times, which is O of V to the four on a dense graph. The chapter does better.

@chapter One more edge
@art distance-matrix
Section twenty five point one fills a matrix. Entry i, j of L of m is the least weight of a path from i to j with at most m edges. A path of m edges is a path of m minus one, plus one more, so you try every possible last edge.

@math heading="A min-plus product" items="L(m) = L(m − 1) ⊗ W@Written out;;Σ → min, × → +@minimum replaces sum;;square: L(2), L(4), L(8)… → Θ(n³ lg n)@you can square"
Written out, that step is a matrix product where minimum replaces sum and addition replaces multiplication. With no negative cycle, L of n minus one is the answer. And since the product is associative, you can square: L two, L four, L eight. That's theta of n cubed log n.

@chapter Floyd-Warshall
@art interior-vertices
Section twenty five point two changes the subproblem. D of k holds the least weight of a path whose interior vertices all come from one to k. A best path either avoids vertex k, or passes through it once and splits there into two paths that only use one to k minus one.

@math heading="The recurrence" items="d⁽ᵏ⁾ᵢⱼ = min(d⁽ᵏ⁻¹⁾ᵢⱼ, d⁽ᵏ⁻¹⁾ᵢₖ + d⁽ᵏ⁻¹⁾ₖⱼ)@the smaller;;k outermost · Θ(n³)@three nested loops"
Each entry is the smaller of those two. Floyd Warshall computes it with three nested loops, k outermost, theta of n cubed in all.

@art loop-order
The order matters. With the pair loops outside and k inside, each entry would be computed once with whatever its neighbours held at the time, and that isn't the recurrence. And the same scheme with or and and computes a graph's transitive closure.

@chapter Watching the matrix
@math heading="1>2 3 · 2>3 4 · 3>1 −2 · 1>4 7 · 4>3 1 · 2>4 2" items="k = 1: 3→2 = 1, 3→4 = 5@Through vertex one;;k = 2: 1→3 = 7, 1→4 = 5, 3→4 = 3@Through vertex two;;k = 3: 4→1 = −1, 4→2 = 2, 2→1 = 2@Through vertex three;;k = 4: 1→3 = 6, 2→1 = 1, 2→3 = 3@Through vertex four"
The lesson's graph has four vertices, six arcs, and one negative weight. Through vertex one, three to two becomes one. Through vertex two, one to three becomes seven, one to four becomes five, and three to four falls to three. Through vertex three, row four fills in. Through vertex four, three cells improve.

@art path-rebuilt
The entry from four to two first appears at k equals three, at distance two, along four, three, one, two. Its path needs both three and one inside. That's sixty four cell visits, four cubed.

@chapter Johnson's reweighting
@art reweight
For sparse graphs, Johnson's algorithm reweights the arcs so Dijkstra can run from every vertex. Add a new vertex with zero weight arcs to every other one, and run Bellman Ford from it. Call the distances h.

@math heading="w′(u, v) = w + h(u) − h(v)" items="h = (−2, 0, 0, 0)@h is;;new weights: 1, 4, 0, 5, 1, 2@all nonnegative;;1 → 2 → 4 → 3: 4 − h(1) + h(3) = 6@undoing the shift"
On the lesson's graph, h is minus two, zero, zero, zero. The new weights are one, four, zero, five, one and two, all nonnegative. The best reweighted route from one to three is one, two, four, three, at four, and undoing the shift gives six, matching the matrix.

@art same-shift
Every path between the same two ends shifts by the same amount, so the shortest ones stay shortest. Then Dijkstra from every vertex, with a Fibonacci heap, gives O of V squared log V, plus V E.

@chapter Where people slip
@list heading="Common slips" items="Reading k as a number of edges@The first|Treating the loop order as a detail@The second|Adding one constant to every arc@the third"
The first slip is reading Floyd Warshall's k as the number of edges on a path. It bounds the interior vertices. The second is treating the loop order as a detail. K must be outermost. And the third is adding one constant to every arc. That penalises paths with more edges, and changes which is shortest.

@chapter Try it
@words text="add 3>4 −6" sub="which diagonal entries go negative?"
Your turn. Add the arc three to four, of weight minus six. Before you type it into the lab, predict which diagonal entries Floyd Warshall will make negative, and why.

@end text="Step the matrix by k"
You can step the matrix one interior vertex at a time, on Learn. That's learn dot get er done dot I O.
