---
format: long
lesson: graph-algorithms/prims-algorithm
title: Prim's algorithm: grow one tree, and skip the stale entries
thumb: Same tree, different work
---

@chapter The question
@title text="Prim's Algorithm" sub="Graph Algorithms" art=thumb
Kruskal sorts every edge in one global list. Prim does something different. It grows a single tree outward from one vertex, always across its own boundary. Same answer, a different schedule, and one odd side effect in the heap.

@chapter The cut, fixed in advance
@art growing-tree
Let S be the vertices already in the tree. The cut is its boundary: S on one side, everything else on the other. At every step, take the lightest edge leaving S, and pull its far end in. By the cut property, that edge is always safe.

@list heading="Prim, with a heap" items="Start S at one vertex, push its edges@Start|Pop the lightest; both ends in S? discard@Pop the lightest|Otherwise take it, add the far end, push its edges@Otherwise|Stop at V − 1 edges@Stop"
With a heap keyed by edge weight: put the start vertex in S and push its edges. Pop the lightest. If both its ends are already in S, discard it and pop again. Otherwise take it, add its far end to S, and push that vertex's edges. Stop at V minus one edges.

@art frontier
Every edge leaving the tree is a candidate, and the heap holds them. Kruskal's cut lived only in its proof. Prim keeps the cut explicit, and that's the only real difference.

@chapter Seven vertices
@math heading="Start at 1" items="1-3:3 → 3 · 2-3:2 → 2@one three;;1-2:4  stale, discarded@one two at four;;2-4:5 → 4 · 4-5:1 → 5@two four;;5-6:6 → 6 · 6-7:2 → 7@five six"
Here's the lab's graph, from vertex one. The pops come out: one three at three, adding three. Two three at two, adding two. Then one two at four, but both ends are in S already, so it's discarded. Then two four, four five, five six and six seven.

@words text="weight 19 · 9 pushes · 7 pops · 12 comparisons"
Six edges, total weight nineteen, the same tree Kruskal built. The counters read nine pushes, seven pops, and twelve key comparisons.

@art unsorted-pops
And look at the pop order. It isn't sorted. Weight three came out before weight two, and five before one. The heap returns the lightest edge it holds, and an edge is only held once its tail joins the tree. Four five wasn't a candidate until four was in.

@chapter Stale entries
@art stale-entry
That discarded edge is a stale entry. It was pushed while its far end was outside, then another edge brought that end in first. A binary heap can't cheaply find and delete it, so you leave it, and check on the way out.

@words text="heap holds up to E entries, not V" sub="that's where E log V comes from"
The cost is that the heap may hold up to E entries rather than V. That's where the E log V in the usual bound comes from.

@art lazy-preset
The lab's lazy preset was built to fill the heap with stale entries. It pushes nine and pops only four, and discards none. The heavy edges do go stale, but the four light edges at vertex one finish the tree first. Here, staleness cost memory, and no pops at all.

@chapter Same answer, different work
@math heading="Same graph, four starts" items="from 1:  12 comparisons@from vertex one;;from 2:  14@from two;;from 4:  24@from four;;from 7:  15@from seven"
Start the same graph at different vertices, and you always get the same tree, weight nineteen. But the work moves. Twelve comparisons from vertex one, fourteen from two, twenty four from four, and fifteen from seven.

@words text="E × ⌊log₂ V⌋ = 18" sub="a reference scale, not a verdict"
The panel prints a reference of nine edges times two, eighteen. Twelve below it isn't beating the bound, and twenty four above it isn't failing one. It's a scale to watch counts against across graphs, so no verdict is printed.

@art tie-orders
Run both algorithms on four vertices with tied weights, and both get weight five, taking the same three edges in different orders. Kruskal takes the weight one edge first, because it sorted first. Prim reaches it last.

@chapter Where people slip
@list heading="Common slips" items="Keying the heap on the wrong quantity@The first|Expecting the pops to come out sorted@The second|Reading the reference column as a bound@And the third"
The first slip is keying the heap on distance from a source, which is Dijkstra's key, not Prim's. You still get a spanning tree, just not a minimum one. The second is expecting the pops to come out sorted. And the third is reading the reference column as a bound the run must respect.

@chapter Try it
@words text="Run Prim from vertex 4" sub="list each pop, and mark the stale ones"
Your turn. Run Prim's algorithm on the same graph starting from vertex four. List every pop, mark which are stale, and check you get the same tree of weight nineteen.

@end text="Step the heap yourself"
You can choose the start vertex and step the heap one pop at a time, on Learn. That's learn dot get er done dot I O.
