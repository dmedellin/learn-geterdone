---
format: short
lesson: replication-and-consistency/physical-clocks-and-drift
title: Your synchronised clocks can be 12 milliseconds apart
---

@art two-clocks-apart
Your clocks are synchronised. They can still be twelve milliseconds apart.

@math items="200 µs/s × 30 s = 6 ms@two hundred;;2ε = 12 ms@twelve"
Drift of two hundred parts per million is two hundred microseconds a second. Corrected every thirty seconds, one clock can be six milliseconds out. Two clocks, opposite ways: twelve.

@words text="5 ms apart? No order to read."
So two events five milliseconds apart can't be ordered by their timestamps at all.

@end text="Full lesson on Learn"
The full lesson, with the window to set, is on Learn.
