---
format: short
lesson: intro-algorithms-graphs/bellman-ford-and-dag-shortest-paths
title: Negative edges don't break shortest paths
---

@art negative-cycle
Three negative edges, and every shortest path is still perfectly defined.

@math items="labels: 0, 2, 5, 0, 2@zero, two, five"
The lesson's graph has three negative arcs and no cycle. Bellman Ford finds every distance: zero, two, five, zero, two.

@words text="Add 5>3 −1 → cycle of weight −4"
Add one arc from five to three, of weight minus one, and a cycle of weight minus four appears. Only then are there no distances.

@end text="Full lesson on Learn"
Run it round by round in the full lesson on Learn.
