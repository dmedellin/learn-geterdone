---
format: short
lesson: intro-algorithms-sorting/heaps
title: Building a heap is linear, not n log n
---

@art height-layers
Building a heap looks like n log n. It's actually linear.

@words text="Half the nodes are leaves"
Each sift down costs the height of its node. And half the nodes are leaves, costing nothing. A quarter are at height one. Only the root is at the top.

@math items="20 keys: 21 vs n·⌊lg n⌋ = 80@twenty keys"
At twenty keys, the exact sum is twenty one, against eighty for the loose bound.

@end text="Full lesson on Learn"
Count the swaps yourself in the full lesson on Learn.
