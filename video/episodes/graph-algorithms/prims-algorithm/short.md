---
format: short
lesson: graph-algorithms/prims-algorithm
title: Prim's heap pops weight three before weight two
---

@art unsorted-pops
Prim's algorithm uses a min heap. So why does weight three come out before weight two?

@words text="an edge is held only once its tail joins the tree"
The heap only holds edges leaving the tree built so far. The weight two edge wasn't a candidate until its end joined.

@words text="lightest it holds, not lightest overall"
So the heap pops the lightest edge it holds, which isn't the lightest in the graph.

@end text="Full lesson on Learn"
The full lesson, one pop at a time, is on Learn.
