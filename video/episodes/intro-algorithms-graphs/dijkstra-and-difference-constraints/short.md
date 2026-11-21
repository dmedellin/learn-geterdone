---
format: short
lesson: intro-algorithms-graphs/dijkstra-and-difference-constraints
title: One negative edge, and Dijkstra gets it wrong
---

@art negative-trap
No negative cycle at all, and Dijkstra still gets the wrong answer.

@math items="settles 4 at 2@four at two;;true distance: 1@true distance"
On four arcs with one weight of minus four, Dijkstra settles vertex four at two, and never revisits it. Its true distance is one.

@words text="Needs every weight ≥ 0"
Dijkstra assumes a route only gets longer after it leaves the settled set. One negative arc breaks that.

@end text="Full lesson on Learn"
Break it yourself in the full lesson on Learn.
