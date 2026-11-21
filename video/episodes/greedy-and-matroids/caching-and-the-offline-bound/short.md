---
format: short
lesson: greedy-and-matroids/caching-and-the-offline-bound
title: Adding cache made it slower
---

@art bigger-cache
Give a cache one more slot, and it can get fewer hits.

@words text="1 2 3 4 1 2 5 1 2 3 4 5"
Run these twelve requests through a FIFO cache, which evicts whatever has been there longest.

@math items="3 slots: 3 hits@three slots;;4 slots: 2 hits@four slots"
With three slots, it gets three hits. With four slots, only two. That's Belady's anomaly. LRU, which evicts the page unused longest, never does this.

@end text="Full lesson on Learn"
Sweep the cache size, one slot at a time, on Learn.
