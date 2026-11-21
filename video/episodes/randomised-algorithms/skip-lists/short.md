---
format: short
lesson: randomised-algorithms/skip-lists
title: A sorted list with coin-flip express lanes
---

@art lanes
Take a sorted linked list. Let every key flip coins to join express lanes above it.

@words text="each lane holds about half the one below"
Each heads lifts a key one more level. So each lane holds about half the keys of the lane below.

@art search-path
To search, go right along the top lane until the next key would overshoot, then drop down. On sixteen keys the lab's mean is under five hops, and nothing is ever rebalanced.

@end text="Full lesson on Learn"
The full lesson on skip lists is on Learn.
