---
format: short
lesson: graphs-and-trees/graph-traversal
title: One change turns BFS into DFS
---

@art queue-vs-stack
Change one data structure, and your search becomes a completely different algorithm.

@words text="Queue → BFS" sub="visits by distance"
With a queue, first in, first out, you get breadth first search. It visits everything one step away, then two, so it finds shortest paths.

@words text="Stack → DFS" sub="one branch to the end"
With a stack, last in, first out, you get depth first search. It dives down one branch to the end, which is what finds cycles. But its depths aren't distances.

@end text="Full lesson on Learn"
The full lesson, with both searches to run, is on Learn.
