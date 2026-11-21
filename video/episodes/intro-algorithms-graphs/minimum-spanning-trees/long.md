---
format: long
lesson: intro-algorithms-graphs/minimum-spanning-trees
title: Minimum spanning trees: why greedy is safe here
thumb: The light edge is safe
---

@chapter The problem
@title text="Minimum Spanning Trees: Kruskal and Prim" sub="Introduction to Algorithms, Chapter 23" art=thumb
Connect every vertex of a weighted, connected, undirected graph, using edges of least total weight. The cheapest such set has no cycle, so it's a tree that spans the graph, with V minus one edges.

@quote text="The greedy strategy advocates making the choice that is the best at the moment." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 23"
Chapter twenty three recalls the greedy strategy: making the choice that is the best at the moment. Greed doesn't find an optimum in general. For this problem, the authors prove that it does.

@chapter A generic method
@art growing-forest
Keep a set of edges, A, with one invariant: A lies inside some minimum spanning tree. Start with A empty. While A isn't a spanning tree yet, add an edge that's safe, meaning A plus that edge is still inside some minimum spanning tree.

@art cut-and-light-edge
To find a safe edge, take a cut: split the vertices into a set S and the rest. The cut respects A if no edge of A crosses it. A light edge is a crossing edge of least weight.

@words text="Theorem 23.1" sub="a light edge across a cut that respects A is safe"
Theorem twenty three point one: take any cut that respects A, and any light edge crossing it. That edge is safe.

@art exchange
The proof is an exchange. Take a minimum tree T that contains A. If it doesn't hold the light edge, add it. That closes a cycle, which must cross the cut somewhere else, at an edge not in A. Swap that edge out. The result is no heavier, so it's minimum too.

@chapter Two algorithms
@list heading="Kruskal" items="sort edges by weight@sorts all the edges|keep an edge joining two trees@different trees|skip an edge inside one tree@skips|O(E lg V)@all"
Kruskal's algorithm sorts all the edges by weight and takes them in order. It keeps each edge whose ends lie in different trees of the forest, and skips each edge whose ends are already connected, using the disjoint set forest. That's O of E log V in all.

@art prim-grows
Prim's algorithm grows a single tree from a root. Each outside vertex has a key, the weight of its lightest edge to the tree. Repeatedly take the vertex of least key and lower its neighbours' keys. With a binary heap, O of E log V. With a Fibonacci heap, O of E plus V log V.

@chapter Test the theorem
@math heading="Lesson graph, S = {1, 3}" items="4 edges cross · lightest: 1–2 and 2–3, weight 3@four edges cross;;55 spanning trees · 2 of minimum weight 12@fifty five;;1–2: in some minimum tree, not every one@some minimum tree"
Take the lesson's graph of six vertices and nine edges, and let S be one and three. Four edges cross, two of them tied at weight three: one two and two three. The lab lists all fifty five spanning trees, and two have the minimum weight, twelve. The light edge one two is in some minimum tree, but not every one.

@art two-light-edges
That's exactly the theorem's promise. Safe means some minimum tree holds it. With a tie, the other light edge, two three, is in the other tree. Ties are where minimum spanning trees stop being unique.

@art heaviest-on-cycle
The lab's table of every edge says more. One three, two four, five six and three five are in every minimum tree. Four five, four six and three four are in none. Each is the heaviest edge on some cycle.

@chapter By hand
@math heading="Kruskal on the lesson's graph" items="keep 1–3, 2–4, 5–6, 1–2@keep;;skip 2–3@skip two three;;keep 3–5 · skip the rest@then keep;;5 edges, weight 12@five edges"
Run Kruskal by hand, taking ties in typed order. Keep one three, two four, five six, and one two. Skip two three, whose ends are now joined. Then keep three five, and skip the last three edges. Five edges, weight twelve. Prim from one also gives twelve.

@chapter Where people slip
@list heading="Common slips" items="A light edge is in every minimum tree@The first|Every vertex's lightest edge makes a tree@The second|Kruskal and Prim return the same tree@And the third"
The first slip is thinking a light edge must be in every minimum tree. The second is taking every vertex's lightest edge and calling it a tree. On this graph that's three edges, leaving three pieces. And the third is expecting Kruskal and Prim to return the same tree. With ties, they may not.

@chapter Try it
@words text="1-2 2 · 1-3 2 · 2-3 1 · 2-4 4 · 3-4 3 · 3-5 5 · 4-5 2" sub="Kruskal and Prim from 1 · unique?"
Your turn. Run Kruskal and Prim from one on this graph by hand, listing each edge kept and the cut that makes it light. Is the minimum spanning tree unique?

@end text="Test the cut theorem yourself"
You can check the theorem against every spanning tree of your own graph, on Learn. That's learn dot get er done dot I O.
