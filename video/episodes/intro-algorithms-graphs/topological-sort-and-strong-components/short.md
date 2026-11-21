---
format: short
lesson: intro-algorithms-graphs/topological-sort-and-strong-components
title: Sort tasks by when they finish, not when they start
---

@art dag-in-a-line
To order tasks so every arrow points forward, sort by finish time.

@math items="✓ decreasing finish: 2, 5, 1, 3, 4, 6@decreasing finish;;✗ discovery: 1, 3, 4, 6, 2, 5@discovery time"
Run depth first search on the lesson's dag. By decreasing finish time you get two, five, one, three, four, six, and every arc points forward. By discovery time, the arc from two to three points backward.

@words text="In a dag, v.f < u.f for every arc u → v"
That's the theorem: the tail always finishes after the head.

@end text="Full lesson on Learn"
Sort your own graph in the full lesson on Learn.
