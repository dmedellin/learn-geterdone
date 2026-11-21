---
format: short
lesson: intro-algorithms-graphs/all-pairs-shortest-paths
title: Why adding a constant to every edge breaks shortest paths
---

@art same-shift
Negative weights? Don't just add a constant to every edge.

@words text="+c per edge" sub="longer paths pay more"
That penalises a path once per edge. Paths with more edges lose, and the shortest path can change.

@math items="w′ = w + h(u) − h(v)@w plus h"
Johnson's shift is w plus h of u minus h of v. Every path between the same two ends moves by the same amount, so the shortest ones stay shortest.

@end text="Full lesson on Learn"
Reweight a graph by hand in the full lesson on Learn.
