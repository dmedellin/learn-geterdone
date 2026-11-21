---
format: short
lesson: graph-algorithms/shortest-and-longest-paths-in-a-dag
title: A graph with no cycles can still have negative weights
---

@art tails-first
A DAG can't have negative weights? It can. It just can't have cycles.

@math items="one pass:  0, 1, 3, 2@a single pass;;nearest-first:  0, 1, 3, 3@nearest first"
On four vertices with one negative arc, a single pass in topological order gets zero, one, three, two. Nearest first settles too early and gets three at the end.

@words text="The order justifies the settling"
Visit vertices in topological order, and every label is final when you reach it, whatever the signs.

@end text="Full lesson on Learn"
The full lesson, with longest paths and slack, is on Learn.
