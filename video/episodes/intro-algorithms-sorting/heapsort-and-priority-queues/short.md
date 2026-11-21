---
format: short
lesson: intro-algorithms-sorting/heapsort-and-priority-queues
title: Heapsort is not stable, and here is why
---

@art unstable
Heapsort is n log n, like merge sort. But it scrambles equal keys.

@art root-to-end
Each step swaps the root with the last slot of the heap. That long jump carries a key straight past others equal to it.

@words text="4 keys × 4 copies: 15 pairs reversed"
In the lab, four distinct keys repeated four times come out with fifteen pairs of equal keys in the wrong order.

@end text="Full lesson on Learn"
See it for yourself in the full lesson on Learn.
