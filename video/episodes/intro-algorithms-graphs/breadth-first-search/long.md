---
format: long
lesson: intro-algorithms-graphs/breadth-first-search
title: Breadth-first search: distances fall out of a queue
thumb: Layer by layer from the source
---

@chapter Two plain tasks
@title text="Graph Representations and Breadth-First Search" sub="Introduction to Algorithms, Sections 22.1–22.2" art=thumb
Part six of the book opens with two plain tasks: storing a graph, and searching it. Nearly every graph algorithm after them starts by doing both.

@chapter Lists or a matrix
@art adjacency-lists
Adjacency lists give each vertex a list of the vertices it has an edge to. In an undirected graph each edge appears twice, once in each end's list, so the lists hold two E entries. The memory is theta of V plus E.

@art adjacency-matrix
An adjacency matrix is a V by V table, with a one where an edge exists. That's theta of V squared memory, however few edges there are. But it tells you whether one particular edge exists in constant time.

@math heading="The lesson's graph: 10 vertices, 11 edges" items="lists: 2 × 11 = 22 entries + 10 heads@twenty two entries;;matrix: 10 × 10 = 100 cells, 22 of them 1@a hundred cells"
On the lesson's own graph of ten vertices and eleven edges, the lists hold twenty two entries beside ten list heads. The matrix would have a hundred cells, twenty two of them ones. For a sparse graph like this, the authors prefer lists.

@chapter The search
@quote text="Breadth-first search is one of the simplest algorithms for searching a graph and the archetype for many important graph algorithms." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 22.2"
The authors introduce it like this: breadth first search is one of the simplest algorithms for searching a graph and the archetype for many important graph algorithms. Prim's algorithm and Dijkstra's both descend from it.

@art grey-frontier
Every vertex starts white, at distance infinity, with no parent. The source turns grey, at distance zero, and goes into a queue. Take the vertex at the head. For each white neighbour, set its distance to one more, make the head its parent, colour it grey, and add it to the tail. Then the head turns black.

@words text="v.d = u.d + 1" sub="every vertex at distance k before any at k + 1"
The queue is why the search spreads evenly. Every vertex at distance k is discovered before any at distance k plus one.

@chapter Why it's linear
@list heading="O(V + E)" items="each vertex enqueued at most once@enqueued|each list scanned once@scanned once|unreached vertices never read@never enqueued"
No vertex is ever made white again, so each one is enqueued and dequeued at most once. Each adjacency list is scanned once, when its vertex leaves the queue. So the total is O of V plus E. It's O, not theta, because a vertex the source can't reach is never enqueued.

@words text="Theorem 22.5: v.d = δ(s, v)" sub="follow parents back for a shortest path"
The section then proves the distances are right. The queue always holds distances in nondecreasing order, with the tail at most one more than the head. So every reachable vertex ends with its true distance, and following parents back from it gives a shortest path.

@chapter On the lesson's graph
@art layers
Search the lesson's graph from s, and the vertices come out in layers. Layer zero is s. Then a and b, then c and d, then e and f, and finally g, at distance four.

@math heading="From s" items="layers: s · a b · c d · e f · g@Those are the layers;;8 of 10 enqueued · 20 of 22 entries examined@eight of the ten;;h, i: distance ∞@h and i"
Those are the layers. The lab enqueues eight of the ten vertices, and examines twenty of the twenty two adjacency entries. H and i aren't reachable, so they keep distance infinity, and their entries are never read.

@art direction-matters
Read the same records as arcs, and start from c instead. Now only e and g can be reached, at distances one and two. Three of ten vertices are enqueued. Direction decides what a search can see.

@chapter The tree can change
@art hexagon
On a hexagon searched from vertex one, the far vertex, four, is at distance three either way round. It gets parent three, because three is dequeued before five. Type the edge from six to one first, and its parent becomes five. Theorem twenty two point five fixes the distances, not the tree.

@chapter Where people slip
@list heading="Common slips" items="Treating the tree as the graph's@The first|Expecting weighted shortest paths@The second|Assuming every vertex is visited@the third"
The first slip is thinking the breadth first tree belongs to the graph. It depends on list order. The second is expecting weighted shortest paths. Every edge counts as one. And the third is assuming the search visits every vertex. It only finds what the source can reach.

@chapter Try it
@words text="p,q · p,r · q,s · r,s · s,t · t,u · r,u · v,w" sub="search from p: queue, distances, parents"
Your turn. Search this undirected graph by hand from p. Write the queue after each dequeue, and every distance and parent. How many adjacency entries does the search examine, out of how many?

@end text="Search a graph of your own"
You can type your own edges and watch the layers form, on Learn. That's learn dot get er done dot I O.
