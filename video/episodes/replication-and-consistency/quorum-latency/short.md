---
format: short
lesson: replication-and-consistency/quorum-latency
title: Adding a replica halved this quorum's write latency
---

@art more-racers
Add a fourth replica, and your quorum writes get twice as fast.

@math items="2 of 3:  p99 = 8 ms@two of three;;2 of 4:  p99 = 4 ms@two of four"
A write that waits for two of three replicas has a p ninety nine of eight milliseconds. Two of four: four milliseconds.

@words text="More racers, earlier second place"
It only waits for the second fastest, and more racers means second place arrives sooner. But check your reads still overlap.

@end text="Full lesson on Learn"
The full lesson, with N to sweep, is on Learn.
