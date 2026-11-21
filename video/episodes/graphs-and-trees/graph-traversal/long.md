---
format: long
lesson: graphs-and-trees/graph-traversal
title: BFS vs DFS: same vertices, different order, different uses
thumb: Queue or stack?
---

@chapter The question
@title text="Breadth-First and Depth-First Search" sub="Graphs and Trees" art=thumb
You want to visit every vertex you can reach from a starting point. There are two classic ways to do it, and they reach exactly the same vertices. The difference is the order, and the order is everything.

@chapter Breadth-first search
@art bfs-ripples
Breadth first search spreads out like ripples. It visits the start, then everything one edge away, then everything two edges away, and so on. Every vertex at distance k is visited before any vertex at distance k plus one.

@list heading="BFS from s" items="mark s, dist[s] = 0, queue = [s]@mark the start|take v from the front@take a vertex from the front|mark each unvisited neighbour u@each unvisited neighbour|dist[u] = dist[v] + 1, push u on the back@one more than"
Here's how. Mark the start, give it distance zero, and put it in a queue. Then repeatedly take a vertex from the front. For each unvisited neighbour, mark it, set its distance to one more than the current vertex, and add it to the back.

@words text="BFS finds shortest paths" sub="in an unweighted graph"
And that gives you something for free. In an unweighted graph, the distance BFS records is the fewest edges on any path from the start. The queue keeps vertices in order of distance, so the first time you reach a vertex, it's by a shortest route.

@chapter Depth-first search
@art queue-vs-stack
Now swap the queue for a stack. Last in, first out, or just use recursion. That's depth first search. It follows one branch as far as it can go, then backs up and tries the next.

@art dfs-deep-branch
Its tree is deep and narrow. And the distance guarantee vanishes immediately. DFS can reach a neighbour of the start by a long detour, and the depth it records is about the search order, not about the graph.

@chapter Both on one graph
@math heading="Edges 1–2, 1–3, 2–4, 3–4, 4–5, 5–6" items="BFS order: 1 2 3 4 5 6@BFS from one;;dist: 0 1 1 2 3 4@distances;;DFS order: 1 2 4 3 5 6@DFS from one;;DFS reaches 3 at depth 3, true distance 1@depth three"
Six vertices, with edges one two, one three, two four, three four, four five, and five six. BFS from one visits one, two, three, four, five, six, with distances zero, one, one, two, three, four. DFS from one goes one, two, four, three, then backs up to five and six. It hit vertex three at depth three, though three is one edge from the start.

@art two-search-trees
Both searches build a spanning tree of the component, but different ones. BFS uses the edges one two, one three, two four, four five and five six. DFS swaps one three for four three. Same six vertices, two different trees.

@chapter Cycles
@art back-edge-cycle
DFS is the tool for finding cycles. In an undirected graph, an edge to a vertex you've already visited, that isn't your parent, closes a cycle. In the example, at vertex three, the edge back to one is that kind of edge. It closes the cycle one, two, four, three, and back to one.

@words text="Exclude the parent"
That parent exclusion matters. Without it, every edge would look like a cycle of length two, back to where you just came from.

@chapter What each is for
@list heading="Uses" items="BFS: shortest paths, distances, bipartiteness@BFS knows distances|DFS: cycles, topological sort, bridges@DFS knows the nesting|Both: components, spanning trees@either one"
BFS knows distances, so it's for shortest unweighted paths, levels, and bipartiteness testing. DFS knows the nesting of the recursion, so it's for cycle detection, topological sort, and bridges. For components and spanning trees, either one works.

@words text="Both: Θ(n + |E|)" sub="with adjacency lists"
And both are cheap. Each vertex is marked once and each edge is looked at twice, once from each end. So with adjacency lists, both run in time proportional to n plus the number of edges.

@chapter Where people slip
@list heading="Common slips" items="Using DFS for shortest paths@The first|Marking on removal, not discovery@The second|Forgetting to exclude the parent@And the third"
The first slip is using DFS for shortest paths. The second is marking a vertex when you take it out, instead of when you discover it. Then it can be queued several times, and both the cost and the distances break. And the third is forgetting to exclude the parent when you look for cycles.

@art components-search
One last thing. A single search only covers one component. To traverse the whole graph, keep starting new searches from vertices nobody has visited yet.

@chapter Try it
@words text="Which finds shortest paths?" sub="BFS, DFS, both, or neither?"
Your turn. Which search finds shortest paths in an unweighted graph, and why can't the other one? Then run both on the example and write down the edge each tree leaves out.

@end text="Run both searches yourself"
You can run both searches on this graph and watch the trees differ, on Learn. That's learn dot get er done dot I O.
