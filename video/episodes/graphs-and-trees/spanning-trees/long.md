---
format: long
lesson: graphs-and-trees/spanning-trees
title: Minimum spanning trees: the rare problem where greedy is right
thumb: Greedy, and provably right
---

@chapter The question
@title text="Spanning Trees and Minimum Spanning Trees" sub="Graphs and Trees" art=thumb
You need to connect a set of towns with cable, and every link has a cost. You want every town reachable, and you want to spend as little as possible. What's the cheapest network?

@chapter Spanning trees
@art spanning-tree-highlight
Start without costs. A spanning tree of a connected graph is a subgraph that's a tree and contains every vertex. Because it's a tree on all n vertices, it has n minus one edges.

@art remove-cycle-edges
Every connected graph has one. If there's a cycle, remove one of its edges. An edge on a cycle is never a bridge, so the graph stays connected. Keep going until no cycle is left, and you have a spanning tree.

@words text="BFS and DFS each give one for free"
You can also get one for free. The tree edges of a breadth first or depth first search, from any vertex, form a spanning tree of its component.

@chapter Kruskal's algorithm
@words text="Minimum spanning tree" sub="a spanning tree of least total weight"
Now add weights. A minimum spanning tree is a spanning tree with the least total weight. And the algorithm for it is almost embarrassingly simple.

@list heading="Kruskal" items="sort the edges by increasing weight@Sort the edges|take each edge in order@take each one in turn|skip it if it closes a cycle@skip it"
Sort the edges from lightest to heaviest. Then take each one in turn, and add it to the tree, unless it would close a cycle. If both ends are already connected, skip it. That's it. Every edge is decided once and never revisited.

@chapter A worked example
@math heading="AB 1 · BC 2 · CD 3 · DE 4 · AE 5 · AC 6 · BD 7" items="AB 1, BC 2, CD 3, DE 4:  take@take all four;;AE 5:  A and E already connected, skip@A E, weight five;;AC 6, BD 7:  skip@skip those too;;MST = {AB, BC, CD, DE}, weight 10@total weight ten"
Five vertices, A to E, with edges sorted by weight, one to seven. A B, B C, C D and D E each reach a new vertex, so take all four. A E, weight five? A and E are already connected, so skip it. A C and B D, skip those too. Four edges, n minus one, total weight ten.

@art kruskal-pentagon
Here it is. The tree is the chain A, B, C, D, E. Every rejected edge was rejected because its ends were already joined, never because it was heavy.

@chapter Why greed works here
@art cut-crossing
Why is this right? It's the cut property. Split the vertices into a set S and the rest. The lightest edge crossing between them belongs to some minimum spanning tree. And if it's strictly the lightest, it belongs to every one.

@art cycle-swap
Here's the proof. Suppose a minimum tree T doesn't use that lightest edge e. Add e to T, and you create exactly one cycle. That cycle has to cross the cut a second time, at some edge f. Swap f out for e. It's still a spanning tree, and since e is no heavier than f, the total didn't go up. So there's a minimum tree containing e.

@words text="Greedy is usually wrong" sub="coin change {1, 3, 4} at 6 · travelling salesman"
And that's unusual. Most optimisation problems have no such property, and greed fails. Coin change with coins one, three and four goes wrong at six, and the travelling salesman goes wrong routinely. Greedy working here is a theorem about this problem, not a general method.

@chapter Prim, and the cost
@art prim-growing
Prim's algorithm uses the same theorem differently. Grow one tree from a single vertex, always adding the lightest edge leaving it. It's shaped like Dijkstra, with a different priority. For Kruskal, sorting the edges dominates the cost, since each cycle test is nearly constant time.

@chapter Where people slip
@list heading="Common slips" items="Assuming greedy works in general@The first|Reading it as a shortest-path tree@The second|Assuming the tree is unique@And the third"
The first slip is assuming greedy works in general. The second is reading the tree as a shortest path tree. In the example, the tree route from A to E weighs ten, while the rejected edge A E weighs five. And the third is assuming the tree is unique. It is when all the weights are distinct, but with ties there may be several, all with the same total.

@chapter Try it
@words text="A connected graph on 20 vertices" sub="How many edges in a spanning tree?"
Your turn. How many edges does a spanning tree of a connected graph on twenty vertices have? Then rerun Kruskal on the example, and say exactly why each skipped edge was skipped.

@end text="Run Kruskal edge by edge"
You can run Kruskal on this graph, edge by edge, on Learn. That's learn dot get er done dot I O.
