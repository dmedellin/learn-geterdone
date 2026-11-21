---
format: long
lesson: graph-algorithms/kruskals-algorithm
title: Kruskal's algorithm: sort the edges, skip the cycles
thumb: Connected, not adjacent
---

@chapter The question
@title text="Kruskal's Algorithm" sub="Graph Algorithms" art=thumb
To build a minimum spanning tree, sort every edge by weight and walk the list once. Take an edge unless it would close a cycle. That's the whole algorithm. The interesting part is why it's right, and what it really costs.

@chapter The algorithm
@list heading="Kruskal" items="Sort the edges by weight@Sort|Every vertex starts as its own piece@own piece|Same piece: reject · different: take and merge@same piece|Stop at V − 1 edges@Stop"
Sort the edges by weight, breaking ties any way at all. Put every vertex in its own piece. For each edge in order, ask whether its ends are in the same piece. If they are, reject it. If not, take it and merge the pieces. Stop at V minus one edges.

@art sorted-edges
The sort is the expensive step. Ordering E edges costs E log E, which is the same as E log V, since E is less than V squared.

@art pieces-merge
The pieces are exactly what a union find structure tracks: find tells you which piece, and union merges two. This lesson doesn't redo that analysis. It counts how many of each operation the algorithm does.

@chapter Why it's right
@art safe-edge
Each taken edge joins two different pieces, so it never closes a cycle. Let S be the piece containing one of its ends. Every other edge across that cut is either still unexamined, and so at least as heavy, or impossible to have rejected. So the edge is a lightest crossing edge, and the cut property says it's safe.

@words text="the algorithm never computes S" sub="the argument does"
Notice the algorithm never computes S. The argument does. And if the list runs out early, two pieces would still need an edge between them, which would have been taken. So on a connected graph, it ends spanning.

@chapter Nine edges
@math heading="Sorted" items="4-5:1  2-3:2  6-7:2  1-3:3@take the first four;;1-2:4  rejected@rejects one two;;2-4:5  5-6:6  taken@takes two four;;3-4:7  5-7:8  rejected@then rejects"
Here are nine edges. Sorted: four five at one, two three at two, six seven at two, one three at three. Take the first four. Then the algorithm rejects one two, at four. It takes two four and five six. Then rejects three four and five seven.

@words text="total weight 19 · 6 edges, 7 vertices"
Total weight nineteen, six edges for seven vertices. An independently written Kruskal, from another subject with its own representation, gets nineteen too.

@art triangle-reject
Look at the first rejection. One and two have no edge between them yet, but they're already joined, through three, by edges of weight two and three. One two, at four, is the heaviest on that triangle. That's the cycle property, which is why a rejected edge is never reconsidered.

@chapter Three counters
@math heading="Opening graph" items="finds:  18 = 2 per edge@eighteen finds;;unions:  6 = V − 1@six unions;;pointer hops:  10@ten pointer hops"
The lab counts three things. Eighteen finds, two per edge, whatever the graph looks like. Six unions, one per taken edge. And ten pointer hops, how far the finds had to climb. Only the hops depend on how the pieces happened to be arranged.

@art hop-chain
On a chain, the counts are twelve finds, five unions and five hops. On the complete graph on five vertices: twenty finds, four unions, and eighteen hops. This structure uses neither union by rank nor path compression, on purpose. Those would leave finds and unions alone and collapse the hops.

@chapter Not connected
@art forest
On a graph in two pieces, the list runs out after four edges, one short of a tree on six vertices. The lab reports that it doesn't span, rather than calling a forest of weight ten a tree. It's still the minimum spanning forest.

@words text="O(E log V)" sub="dominated by the sort"
The bound is order E log V, and the sort dominates. Finds are exactly two E, unions at most V minus one. So a faster union find can't speed this algorithm up at all.

@chapter Where people slip
@list heading="Common slips" items="Testing adjacent instead of connected@The first|Re-examining a rejected edge@The second|Quoting the union-find bound as the cost@And the third"
The first slip is testing whether the ends are adjacent, rather than connected. That's what puts a cycle in a hand run. The second is reconsidering a rejected edge later. And the third is quoting the union find bound as the cost, when the sort dominates.

@chapter Try it
@words text="Run Kruskal on the nine edges by hand" sub="give the reason for every rejection"
Your turn. Take those nine edges, sort them, and run the algorithm by hand. For every rejection, name the cycle it would have closed.

@end text="Watch each edge taken or rejected"
You can run Kruskal on your own graph and see the reason for every rejection, on Learn. That's learn dot get er done dot I O.
