---
format: long
lesson: graphs-and-trees/graph-representations
title: Adjacency matrix or adjacency list? And how matrix powers count walks
thumb: Same graph, stored two ways
---

@chapter The question
@title text="Graph Representations" sub="Graphs and Trees" art=thumb
A graph is dots and lines on paper. But a computer can't store a picture. So how do you write a graph down, and does the choice matter? It matters a lot.

@chapter The adjacency matrix
@art matrix-grid
The first way is the adjacency matrix. Number the vertices one to n, and make an n by n grid. Put a one in row i, column j when vertices i and j are adjacent, and a zero when they're not.

@words text="Symmetric, zero diagonal" sub="for a simple undirected graph"
For a simple undirected graph, the matrix is symmetric, because adjacency goes both ways. And its diagonal is all zeros, because there are no loops.

@chapter The adjacency list
@art adjacency-lists
The second way is the adjacency list. For each vertex, keep a list of its neighbours. Each edge shows up in two lists, once from each end, so the total length is twice the number of edges, not the number of edges.

@list heading="Matrix vs list" items="Is u adjacent to v?  O(1) vs O(deg u)@is u adjacent|Neighbours of v:  O(n) vs O(deg v)@the neighbours of v|Space:  Θ(n²) vs Θ(n + edges)@for space"
Compare them. Is u adjacent to v? Constant time with the matrix, up to the degree of u with the list. To visit the neighbours of v, the matrix scans a row of n entries, while the list hands you exactly those neighbours. And for space, it's n squared against n plus the number of edges.

@chapter Which one to use
@art sparse-matrix
Most real graphs are sparse. A road network with a million junctions has a few million edges. A matrix for it would need ten to the twelve entries, almost all of them zero. So lists are the default for anything real.

@words text="Breadth-first search" sub="list Θ(n + |E|) · matrix Θ(n²)"
It shows up in running time too. Searches walk through neighbours constantly, so breadth first search runs in time proportional to n plus the edges with a list, and n squared with a matrix. On a sparse graph, that's linear against quadratic.

@words text="When the matrix wins" sub="dense graphs · many adjacency tests · linear algebra"
The matrix still wins when the graph is dense, when adjacency tests dominate, or when you want the linear algebra. And the linear algebra is where it gets beautiful.

@chapter Powers count walks
@math heading="Matrix powers" items="Aᵏ[i][j] = number of walks of length k from i to j@the entry in row i;;Aᵏ⁺¹[i][j] = Σₜ Aᵏ[i][t] · A[t][j]@sum over every middle vertex"
Raise the matrix to the power k, and the entry in row i, column j counts the walks of length exactly k from i to j. A walk may repeat vertices and edges. Why? A longer walk is a walk to some vertex t, then one edge to j. Sum over every middle vertex t, and that's precisely matrix multiplication.

@chapter A worked example
@math heading="C₄: 1–2–3–4–1" items="A rows: 0101 · 1010 · 0101 · 1010@the four cycle;;A² rows: 2020 · 0202 · 2020 · 0202@Square it"
Take the four cycle, with vertices one, two, three, four, and back to one. Its matrix has rows zero one zero one, then one zero one zero, repeating. Square it, and you get rows two zero two zero, then zero two zero two, repeating.

@art walk-there-and-back
Read the entries. A squared, row one, column one, is two: the walks one to two to one, and one to four to one. That's just the degree of vertex one, out and straight back.

@art walk-two-steps
Row one, column three, is also two: one to two to three, and one to four to three. But row one, column two, is zero. No walk of length two joins neighbours here, because the four cycle is bipartite.

@art triangle-walks
And cubes count triangles. Each triangle gives six closed walks of length three, three starting points times two directions. So the number of triangles is the trace of A cubed, over six. For the four cycle the trace is zero, so there's no triangle.

@chapter Where people slip
@list heading="Common slips" items="Confusing walks with paths@The first|A matrix for a big sparse graph@The second|Forgetting each edge is listed twice@And the third"
The first slip is confusing walks with paths. Powers count walks, which can revisit vertices, and paths have no matrix formula. The second is using a matrix for a large sparse graph. And the third is forgetting that each edge appears in two lists.

@chapter Try it
@words text="A sparse graph, a million vertices" sub="matrix or list?"
Your turn. For a sparse graph with a million vertices, which representation should you use, and roughly how many entries would the other one need?

@end text="Square the matrix yourself"
You can load the four cycle, square its matrix, and count the walks, on Learn. That's learn dot get er done dot I O.
