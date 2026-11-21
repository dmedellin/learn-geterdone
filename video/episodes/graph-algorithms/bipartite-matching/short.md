---
format: short
lesson: graph-algorithms/bipartite-matching
title: Greedy matching can get half the answer
---

@art greedy-blocked
Pair people with jobs greedily, and you can end up with half as many pairs as you could have had.

@math items="L2–R2 first:  1 pair@greedy takes;;best:  2 pairs@the best"
With these three allowed pairs, greedy takes L two with R two first, and that blocks both of the others. One pair. But the best matching has two.

@words text="Maximal is not maximum"
Nothing can be added to the greedy answer. It still isn't the largest. An augmenting path is what fixes it.

@end text="Full lesson on Learn"
The full lesson, with the flow construction, is on Learn.
