---
format: short
lesson: intro-algorithms-design-techniques/elements-of-dynamic-programming
title: Longest paths break dynamic programming
---

@art path-clash
Shortest paths split into shortest pieces. Longest paths don't, and here's why.

@math items="longest u to w: u → v → w@u to w;;longest w to v: w → x → u → v@w to v;;spliced: repeats u and v  ✗@repeats"
In a four vertex graph, the longest path from u to w is u, v, w. The longest from w to v is w, x, u, v. Glue them, and the path repeats u and v.

@words text="The pieces compete for vertices"
The two halves aren't independent. So there's no optimal substructure.

@end text="Full lesson on Learn"
Check both ingredients in the full lesson on Learn.
