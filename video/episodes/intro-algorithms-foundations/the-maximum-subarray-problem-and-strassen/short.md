---
format: short
lesson: intro-algorithms-foundations/the-maximum-subarray-problem-and-strassen
title: How one fewer multiplication beats n cubed
---

@art bushy-trees
One fewer multiplication changes the whole order of growth.

@math items="8T(n/2) + Θ(n²) = Θ(n³)@eight;;7T(n/2) + Θ(n²) = Θ(n^(lg 7))@seven"
Split matrices into quarters, and you need eight half size products, still n cubed. Strassen needs only seven, and that's n to the log seven, about n to the two point eight.

@words text="Fewer branches, smaller tree"
The extra additions are cheap. Cutting one branch at every level is what pays.

@end text="Full lesson on Learn"
See the recursion trees in the full lesson on Learn.
