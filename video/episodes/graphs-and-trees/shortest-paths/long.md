---
format: long
lesson: graphs-and-trees/shortest-paths
title: Dijkstra's algorithm: fewest edges is not the cheapest route
thumb: Cheapest beats shortest
---

@chapter The question
@title text="Shortest Paths and Dijkstra's Algorithm" sub="Graphs and Trees" art=thumb
Breadth first search finds the route with the fewest edges. But on a road map, what you want is the route with the least distance. And those aren't the same thing at all.

@art cheap-vs-few
In a weighted graph, every edge carries a number, like a distance or a cost. The weight of a path is the sum of its edge weights, and a shortest path is one of minimum weight. A two edge route of weight twenty loses to a five edge route of weight eight.

@chapter The idea
@art settle-frontier
Dijkstra's algorithm grows a region of settled vertices outward from the source. At each step, it picks the unsettled vertex with the smallest known distance, settles it, and declares that distance final.

@list heading="Dijkstra from s" items="dist[s] = 0, every other vertex ∞@Start with|settle the nearest unsettled vertex u@settle the unsettled|relax: dist[v] = min(dist[v], dist[u] + w(u,v))@relax"
Start with the source at zero and every other vertex at infinity. Then repeat. Settle the unsettled vertex with the smallest distance. And relax its edges: for each neighbour, if going through the vertex you just settled is cheaper, update its distance and remember where it came from.

@art relax-edge
That relaxing step is what breadth first search can't do. BFS fixes a vertex the first time it touches it. Dijkstra lets a distance come down when a cheaper route turns up.

@chapter A worked example
@math heading="s→a 10 · s→b 3 · b→a 2 · a→t 1 · b→t 9" items="settle s:  a = 10, b = 3, t = ∞@settle s;;settle b (3):  a = min(10, 3 + 2) = 5,  t = min(∞, 3 + 9) = 12@settle b;;settle a (5):  t = min(12, 5 + 1) = 6@settle a;;settle t (6)@settle t"
Here's a graph. S to a weighs ten, s to b three, b to a two, a to t one, and b to t nine. Settle s: a is ten, b is three, t is infinity. Settle b at three: a drops to five, and t becomes twelve. Settle a at five: t drops to six. Finally, settle t, at six.

@art worked-route
So the cheapest route is s, b, a, t, with weight six, using three edges. The fewest edge routes, s a t and s b t, use two edges but weigh eleven and twelve. BFS would hand you one of those. Eleven or twelve, against six.

@chapter Why it works
@words text="Once settled, a distance is final" sub="if every weight is ≥ 0"
Why can Dijkstra declare a distance final? Any other route to that vertex has to leave the settled region somewhere, through a vertex that's already at least as far away. And the rest of the route can only add weight, because the weights aren't negative.

@art negative-edge-trap
That's exactly where it breaks. Take s, a and b, with s to a weighing one, s to b two, and b to a minus two. Dijkstra settles a at distance one, and never looks back. But s, b, a weighs zero. The answer is wrong, and the algorithm never notices.

@words text="Negative weights → Bellman–Ford" sub="relax every edge n − 1 times"
For negative weights, use Bellman Ford. It relaxes every edge n minus one times, which is slower, and it detects negative cycles, where no shortest path exists at all, because going round again always lowers the total.

@chapter Cost
@art priority-queue
The cost depends on how you find the smallest unsettled vertex. A linear scan gives n squared plus the edges. A binary heap gives n plus the edges, times log n. Heaps win on sparse graphs, and the simple scan holds its own on dense ones.

@words text="All weights 1 → Dijkstra is BFS"
And if every weight is one, the priority queue becomes a plain queue, and vertices settle in exactly the order BFS visits them. BFS is just Dijkstra's special case.

@chapter Where people slip
@list heading="Common slips" items="Using BFS on a weighted graph@The first|Dijkstra with negative weights@The second|Adding a constant to every weight@And the third"
The first slip is using BFS on a weighted graph. It answers fewest edges, a different question. The second is running Dijkstra with negative weights, which fails silently. And the third is adding a constant to make every weight positive. Longer paths get penalised more, so the answer changes.

@chapter Try it
@words text="All weights equal to 1" sub="Dijkstra reduces to…?"
Your turn. Run Dijkstra on the example yourself, and check the settled distances are zero, five, three and six for s, a, b and t. Then ask: with all weights equal to one, what does Dijkstra turn into?

@end text="Watch Dijkstra settle each vertex"
You can load this graph and watch Dijkstra settle each vertex, on Learn. That's learn dot get er done dot I O.
