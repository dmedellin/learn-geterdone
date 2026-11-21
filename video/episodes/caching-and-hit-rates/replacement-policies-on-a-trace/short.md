---
format: short
lesson: caching-and-hit-rates/replacement-policies-on-a-trace
title: The cache that got worse when you gave it more memory
---

@art bigger-worse
Can giving a cache more memory make it miss more often? Yes.

@words text="1 2 3 4 1 2 5 1 2 3 4 5"
Run this trace through a FIFO cache: one, two, three, four, one, two, five, one, two, three, four, five.

@math items="k = 3:  9 misses@three slots;;k = 4:  10 misses@four slots"
With three slots, FIFO misses nine times. With four slots, it misses ten. That's Belady's anomaly. LRU can't do this, because it's a stack algorithm.

@end text="Full lesson on Learn"
The full lesson, with your own trace to replay, is on Learn.
