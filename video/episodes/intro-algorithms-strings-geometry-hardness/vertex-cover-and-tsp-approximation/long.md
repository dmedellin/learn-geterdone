---
format: long
lesson: intro-algorithms-strings-geometry-hardness/vertex-cover-and-tsp-approximation
title: Approximating vertex cover and TSP within a factor of two
thumb: Twice a lower bound
---

@chapter There may be hope
@title text="Approximating Vertex Cover and TSP" sub="Introduction to Algorithms, Sections 35.1–35.2" art=thumb
Chapter thirty five begins after the bad news.

@quote text="Even if a problem is NP-complete, there may be hope." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 35"
Even if a problem is NP complete, there may be hope. Small inputs can afford an exponential search. Special cases may be easy. Or you can find an answer near the optimum in polynomial time, with near proved as a factor.

@math heading="The approximation ratio" items="max(C/C*, C*/C) ≤ ρ(n)@the larger;;ρ = 1: optimal@one means"
The approximation ratio is the larger of C over C star, and C star over C, so it works for minimizing and maximizing alike. It's never below one, and one means optimal.

@art ratio-scale
Some problems have small constant ratios. For others, the best known ratio grows with n. And an approximation scheme takes an extra input, epsilon, and gets within one plus epsilon. It's fully polynomial when halving epsilon costs only a constant factor more time.

@chapter Vertex cover
@art take-both-ends
A vertex cover is a set of vertices touching every edge, and finding a smallest one is NP hard. The approximation is short. While edges remain, take any edge, put both its ends in the cover, and delete every edge touching either one. That's O of V plus E.

@art matching-bound
Why is it within a factor of two? The edges it picked share no vertex, so they form a matching. Any cover, the optimal one included, needs at least one end of each matching edge. And the algorithm's cover has exactly two ends per edge.

@math heading="Theorem 35.1" items="|C*| ≥ |A|@at least;;|C| = 2|A|@exactly;;|C| ≤ 2|C*|@So"
So the optimum is at least the matching's size, the algorithm's cover is exactly twice the matching, and so it's at most twice the optimum. The optimum only appears in an inequality. Nobody had to know it.

@chapter The lesson's graph
@math heading="1-2, 2-3, 3-4, 4-5, 2-6, 3-6, 6-7" items="take 1-2, then 3-4, then 6-7@takes one two;;cover {1, 2, 3, 4, 6, 7}: 6@six vertices;;optimum 3, e.g. {2, 4, 6} · ratio 2@an optimum of three"
On the lesson's graph, the algorithm takes one two, which removes two three and two six. Then three four, which removes three six and four five. Then six seven. That's a cover of six vertices. The exhaustive search finds an optimum of three, for instance two, four and six. The ratio is exactly two. The bound is met.

@words text="cycle5: 4/3 · triangles: 1" sub="one graph, one value under the bound"
Other graphs land under it. A five cycle gives four thirds. Two disjoint triangles give one. The guarantee is the worst over every input. The lab's sweep over all sixty three graphs on four vertices with an edge finds a worst ratio of two. List the edges in another order, and the cover can change. The guarantee can't.

@chapter The travelling salesman
@art mst-tour
With the triangle inequality, there's a tour within twice the optimum too. Grow a minimum spanning tree with Prim's algorithm, and visit the vertices in preorder.

@art full-walk
The tree is the lower bound. Delete any edge from the best tour, and what's left is a spanning tree, so the tree weighs no more than the tour. A full walk around the tree crosses each edge twice. Skipping repeated vertices can only shorten it, under the triangle inequality.

@art no-triangle
And the hypothesis is doing the work. Without the triangle inequality, no polynomial time algorithm has any constant ratio, unless P equals NP. Give the graph's edges cost one, and every missing edge a cost above rho times V. A hamiltonian cycle is then a tour of cost V, and any other tour costs more than rho times V, so a rho approximation would tell them apart.

@chapter Where people slip
@list heading="Common slips" items="The ratio needs the optimum@The first|A realised ratio is the algorithm's ratio@The second|Dropping the triangle inequality@the third"
The first slip is thinking the ratio needs the optimum. The proof uses a lower bound the algorithm can see. The second is reading one graph's ratio as the algorithm's. And the third is dropping the triangle inequality from the tour.

@chapter Try it
@code block=1 lines=1-1 focus="1@in the order listed"
Your turn. Run the vertex cover algorithm by hand, taking these edges in the order listed. Give the matching, the cover and its size, then find the optimum by reasoning about the triangle one, two, three and the edge four five.

@end text="Measure the ratio"
You can set the cover against the matching and the optimum, on Learn. That's learn dot get er done dot I O.
