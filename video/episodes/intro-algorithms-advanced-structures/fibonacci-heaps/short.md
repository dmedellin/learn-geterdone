---
format: short
lesson: intro-algorithms-advanced-structures/fibonacci-heaps
title: One heap operation cost 17 steps, and was still cheap
---

@art insert-a-root
Seventeen steps for one operation, and its amortized cost is one. How?

@art root-list
Insert seventeen keys into a Fibonacci heap. Each insert just adds a root, and stores one unit of potential.

@art consolidate
Then extract the minimum. It scans every root and links all sixteen survivors into one tree. Seventeen actual steps, but the potential falls from seventeen to one.

@end text="Full lesson on Learn"
The insertions paid in advance. See the full lesson on Learn.
