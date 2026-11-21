---
format: long
lesson: graphs-and-trees/graphs-and-graph-models
title: What a graph really is (and why it isn't a plot)
thumb: Things, and which pairs connect
---

@chapter The question
@title text="Graphs and Graph Models" sub="Graphs and Trees" art=thumb
What do a friendship network, a road map, a list of task dependencies and a molecule have in common? They're all the same kind of object. They're all graphs.

@words text="A graph is not a plot" sub="no axes, no curve"
First, clear one thing up. The word graph means two different things. Here it doesn't mean a curve on axes. Nothing is being plotted. A graph is a set of things, and which pairs of them are joined.

@chapter The definition
@math heading="Simple graph" items="G = (V, E)@G is a pair;;V: a finite set of vertices@a finite set;;E: unordered pairs of distinct vertices@each one an unordered pair;;no loops, no repeated edges@no loops"
A simple graph G is a pair, V and E. V is a finite set of vertices. E is a set of edges, each one an unordered pair of distinct vertices. So there are no loops, and no repeated edges.

@list heading="The vocabulary" items="adjacent, or neighbours@adjacent|incident@incident|order: how many vertices@the order|size: how many edges@the size"
Two vertices joined by an edge are adjacent, or neighbours. A vertex and an edge that meet are incident. The number of vertices is the order of the graph, and the number of edges is the size.

@art same-graph-two-drawings
Here's the idea that trips people up. The drawing is not the graph. Where you put the dots, and how you bend the lines, carries no information at all. Two pictures that look nothing alike can be exactly the same graph.

@chapter The variants
@art graph-variants
The definition is spare, and you can relax it. A multigraph allows repeated edges, like parallel roads between two towns. A pseudograph allows loops as well, which suits state machines. A directed graph gives each edge a direction. And a weighted graph puts a number on each edge, like a distance or a cost.

@words text="Asymmetric relation → directed graph" sub="follows · must precede"
These aren't interchangeable. If the relation only goes one way, like follows, or must precede, you need direction. Drop it, and you throw away the very information the model was there to carry. On this course, graph means a simple undirected graph unless we say otherwise.

@chapter The standard families
@art standard-families
A few graphs come up so often they have names. The complete graph K n joins every pair of its n vertices. The cycle C n is a single closed ring, with n edges. The path P n is a single open chain, with n minus one edges.

@art complete-bipartite
The complete bipartite graph K m n has a left side and a right side, with every left vertex joined to every right one. That's m times n edges. And the hypercube Q n has bit strings as vertices, joined when they differ in exactly one position.

@chapter Counting edges
@math heading="Edges in the families" items="Kₙ: C(n,2) = n(n−1)/2@n choose two;;K₅: 10 edges · K₁₀: 45 edges@K five has ten;;K₃,₃: 3 · 3 = 9 edges@K three three;;Qₙ: n · 2ⁿ / 2 = n · 2ⁿ⁻¹@the hypercube"
K n has n choose two edges, which is n times n minus one, over two. So K five has ten edges, and K ten has forty five. K three three has three times three, nine. And in the hypercube, each of the two to the n vertices has degree n, so the edge count is n times two to the n, over two.

@words text="At most C(n,2) edges" sub="equality exactly for Kₙ"
That first count is also a limit. Every edge is an unordered pair of distinct vertices, and no pair can repeat. So a simple graph on n vertices has at most n choose two edges, and only the complete graph reaches it.

@chapter Four models
@art road-network
Now the payoff. Road networks: vertices are junctions, edges are roads, weights are distances, and the best route is a shortest path. Social networks: vertices are people, edges are acquaintance.

@art dependency-arrows
Dependencies: vertices are tasks, and directed edges mean must precede. A valid schedule exists exactly when there's no cycle. Molecules: vertices are atoms, edges are bonds, and two molecules with the same formula but different structures are different graphs.

@chapter Where people slip
@list heading="Common slips" items="Reading a graph as a plot@The first|Treating the drawing as the object@The second|Undirected edges for a one-way relation@And the third"
The first slip is reading a graph as a plot. The second is treating the drawing as the object, when position and curvature mean nothing. And the third is using an undirected graph for a one way relation, like must precede.

@chapter Try it
@words text="How many edges does K₆ have?" sub="every pair joined exactly once"
Your turn. How many edges does K six have? Not six, that's the cycle. Not thirty, that counts each pair twice. Count the pairs of six vertices, each joined exactly once, and you should get fifteen.

@end text="Build any graph, watch the counts"
You can build any graph you like and watch every count update, on Learn. That's learn dot get er done dot I O.
