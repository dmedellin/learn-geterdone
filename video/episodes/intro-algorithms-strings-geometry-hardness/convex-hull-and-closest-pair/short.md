---
format: short
lesson: intro-algorithms-strings-geometry-hardness/convex-hull-and-closest-pair
title: Graham's scan never asks if a point is inside
---

@art pop-right-turn
Graham's scan finds the convex hull without ever testing whether a point is inside.

@art angle-sort
Sort the points by angle around the lowest one. Push each one onto a stack, but first pop the top while it fails to make a left turn.

@words text="Each point: one push, at most one pop"
A popped point can't be a corner. Every point is pushed once and popped at most once, so after sorting, the scan is linear.

@end text="Full lesson on Learn"
Wrap your own points in the full lesson on Learn.
