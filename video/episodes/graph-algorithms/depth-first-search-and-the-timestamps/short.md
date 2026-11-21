---
format: short
lesson: graph-algorithms/depth-first-search-and-the-timestamps
title: The same arc can be forward or cross
---

@art forward-and-cross
Is this arc a forward arc or a cross arc? It depends where you start walking.

@words text="start at 1: forward 1 · cross 1" sub="start at 3: forward 0 · cross 2"
Start the depth first walk at vertex one, and the arc from one to four is forward. Start at three, and the same arc is cross.

@words text="Back arcs: 2 either way"
What never changes is the back count. A back arc means a cycle, and cycles belong to the graph, not the walk.

@end text="Full lesson on Learn"
The full lesson, with a root you can move, is on Learn.
