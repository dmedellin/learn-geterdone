---
format: short
lesson: geometric-algorithms/the-closest-pair-and-the-strip
title: Why the closest pair needs only seven checks per point
---

@art eight-squares
Finding the closest pair, each strip point needs at most seven comparisons. Here's why.

@words text="2d × d  →  8 squares of side d/2"
The candidates above a point fit in a two d by d rectangle. Cut it into eight squares of side d over two.

@art strip
Two points in one square would be closer than d, which the recursion already rules out. So there's at most one per square, and at most seven neighbours to check.

@end text="Full lesson on Learn"
The full lesson on the closest pair is on Learn.
