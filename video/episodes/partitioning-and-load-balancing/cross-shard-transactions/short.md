---
format: short
lesson: partitioning-and-load-balancing/cross-shard-transactions
title: Two shards, and half your transactions cross
---

@art two-keys-two-shards
Add just one shard, and half your two key transactions now cross.

@math items="P(local) = N¹⁻ᵏ@N to the one minus k;;k = 2,  N = 2:  1/2@one half;;k = 2,  N = 16:  1/16@one sixteenth"
Hash k keys over N shards, and they all land together with probability N to the one minus k. Two keys, two shards: one half. Two keys, sixteen shards: one sixteenth.

@words text="Crossing pays 5.00 ms of two-phase commit"
Every one that crosses pays for two phase commit.

@end text="Full lesson on Learn"
The full lesson, with the commit cost itemised, is on Learn.
