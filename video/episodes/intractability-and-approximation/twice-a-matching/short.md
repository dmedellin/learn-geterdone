---
format: short
lesson: intractability-and-approximation/twice-a-matching
title: Never more than twice the best cover
---

@art greedy-matching
A two line algorithm for vertex cover that's never worse than double.

@words text="take both ends of a maximal matching"
Grab edges that share no vertex, until none can be added. Take both ends of each.

@math items="matching ≤ optimum@at most;;cover = 2 × matching ≤ 2 × optimum@twice"
Every cover needs a different vertex for each matched edge, so the matching is at most the optimum. Your cover is exactly twice the matching, so at most twice the optimum.

@end text="Full lesson on Learn"
The full lesson is on Learn.
