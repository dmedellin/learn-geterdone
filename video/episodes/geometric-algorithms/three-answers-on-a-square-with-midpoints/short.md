---
format: short
lesson: geometric-algorithms/three-answers-on-a-square-with-midpoints
title: How many corners does a square have? Four, six or eight
---

@art square-midpoints
Three correct hull algorithms, one square, and they answer four, six and eight.

@words text="vertices 4 · boundary 8" sub="the midpoints are on an edge, not corners"
Add the midpoint of each side. The monotone chain returns the four corners, the vertices. The boundary oracle returns all eight boundary points.

@art gift-wrap-ties
Gift wrapping returns six, because collinear ties go to whichever point the sorted scan meets first. None of them is wrong. They answer different questions.

@end text="Full lesson on Learn"
The full lesson is on Learn.
