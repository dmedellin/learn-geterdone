---
format: long
lesson: graph-algorithms/depth-first-search-and-the-timestamps
title: Depth-first search: two numbers on every vertex
thumb: Nest or disjoint, never overlap
---

@chapter The question
@title text="Depth-First Search and the Timestamps" sub="Graph Algorithms" art=thumb
One depth first walk can tell you whether a graph has a cycle, which vertices descend from which, and what kind of arc every arc is. All from two numbers written on each vertex. Here's how.

@chapter Two timestamps
@art walk-forest
Keep one counter, starting at zero. When the walk first reaches a vertex v, tick the counter and write it down as d of v, the discovery time. When every arc out of v is done, tick again and write f of v, the finish time. When one walk runs out, restart at the lowest undiscovered vertex. So the tree arcs form a forest.

@art two-ticks
The counter is shared across the whole forest, so times are comparable everywhere. With n vertices it always ends at two n, because each vertex ticks once opening and once closing.

@chapter The parenthesis theorem
@art intervals
Each vertex is open for the interval from d to f. Here's the key fact. For any two vertices, their intervals either nest, one inside the other, or are completely disjoint. They never partly overlap.

@list heading="Why they never overlap" items="u still open when v starts: v is inside u@still open|u already closed: the intervals are disjoint@If u is closed"
Say u was discovered first. When v is discovered, either u is still open, or it's closed. If it's open, the walk reached v from inside u, and u can't close while v is open. So they nest. If u is closed, the intervals are disjoint, and neither is the other's ancestor.

@words text="v descends from u ⟺ d[u] < d[v] and f[v] < f[u]"
So ancestry is just arithmetic. v is a descendant of u exactly when its interval sits inside u's. On the lab's graph, there are fifteen pairs. Seven nest, eight are disjoint, and none overlap.

@chapter Four classes of arc
@list heading="Arc u → v" items="Tree: it discovered v@Tree|Back: v is a proper ancestor@Back|Forward: v is a finished descendant@Forward|Cross: the intervals don't meet@Cross"
Every arc gets exactly one of four labels. Tree, if it discovered v. Back, if v is an ancestor of u. Forward, if v is a descendant, but not through this arc. And cross, if the two intervals don't meet at all.

@math heading="Arcs 1>2 1>4 2>5 4>2 5>4 3>5 3>6 6>3, start at 1" items="d = 1, 2, 9, 4, 3, 10@The discovery times are;;f = 8, 7, 12, 5, 6, 11@The finish times are;;tree 4 · back 2 · forward 1 · cross 1@four tree"
Here are eight arcs, with the walk starting at one. It goes one, two, five, four, closes them all, then restarts at three and reaches six. The discovery times are one, two, nine, four, three, ten. The finish times are eight, seven, twelve, five, six, eleven. That gives four tree arcs, two back, one forward and one cross.

@art forward-and-cross
Two deserve a look. One to four is forward, not tree, because the walk reached four first through two and five. And three to five is cross, even though both are in the same picture. Five closed at step six, before three opened at step nine.

@chapter A fact about the walk
@words text="start at 3: tree 4 · back 2 · forward 0 · cross 2"
Now start the same arcs at three instead. The times change, and so do the counts: still four tree arcs and two back, but now no forward arcs and two cross. One to four went from forward to cross. The class of an arc is a fact about the walk, not the graph.

@art back-arc-cycle
But the back count didn't move. It's two from either start, and it has to be. A back arc points to a vertex that's still open, which is an ancestor, so the tree path plus that arc is a cycle. And every cycle produces a back arc. So acyclic means no back arc in one walk.

@art undirected
Read the same arcs as undirected, and forward and cross both vanish. An undirected edge is met from whichever end the walk reached first, so the far end is always an open ancestor. Forward and cross only happen with direction.

@chapter The cost
@words text="6 visits · 8 arc reads" sub="Θ(V + E)"
On the opening graph, the lab counts six vertex visits and eight arc reads. That's the V plus E in Theta of V plus E. Each vertex is opened once, and each arc is examined once, from its tail.

@chapter Where people slip
@list heading="Common slips" items="Treating the classes as a property of the graph@The first|Hunting for a cycle by eye@The second|Reading a cross arc as a second component@And the third"
The first slip is treating the classes as a property of the graph. The second is hunting for cycles by eye, when one walk answers it with a count. And the third is reading a cross arc as a second component. Five is perfectly reachable from three. The walk just finished it first.

@chapter Try it
@words text="Start the eight arcs at 3" sub="write d and f, then classify every arc"
Your turn. Run the walk on those eight arcs from vertex three. Write down both times for every vertex, then classify every arc using only those numbers.

@end text="Move the root"
You can change the starting vertex and watch every arc reclassify itself, on Learn. That's learn dot get er done dot I O.
