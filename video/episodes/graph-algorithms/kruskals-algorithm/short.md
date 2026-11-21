---
format: short
lesson: graph-algorithms/kruskals-algorithm
title: Kruskal rejects an edge between unlinked vertices
---

@art triangle-reject
Vertices one and two have no edge between them. Kruskal still rejects the edge one two.

@words text="joined through 3"
They're already in the same piece, joined through three, by edges of weight two and three. Taking one two would close a cycle.

@words text="Connected, not adjacent"
The test is whether a path already exists, not whether an edge does.

@end text="Full lesson on Learn"
The full lesson, with every rejection explained, is on Learn.
