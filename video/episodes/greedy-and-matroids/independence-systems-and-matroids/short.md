---
format: short
lesson: greedy-and-matroids/independence-systems-and-matroids
title: The three-edge path that isn't a matroid
---

@art path-matching
Three edges in a row are enough to break the matroid rule.

@words text="independent = no shared vertex"
Call a set of edges independent if no two share a vertex. Then the middle edge alone can't be extended.

@words text="{B}: size 1, maximal · {A, C}: size 2"
But the two end edges together make a bigger independent set. Two maximal sets of different sizes. That's exactly what a matroid forbids.

@end text="Full lesson on Learn"
Test every exchange pair on Learn.
