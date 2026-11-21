---
format: short
lesson: partitioning-and-load-balancing/hash-partitioning-and-imbalance
title: Hashing doesn't fill shards evenly
---

@art uneven-bins
A perfect hash, twelve hundred keys, twelve shards. Does every shard get a hundred?

@math items="mean = 1 200 / 12 = 100@exactly a hundred;;fullest = 122@a hundred and twenty two;;max/mean = 61/50 = 1.220@one point two two"
No. The mean is exactly a hundred, but on one seeded placement the fullest shard held a hundred and twenty two. That's one point two two times the mean.

@words text="Equally likely ≠ equally full"
Hashing makes every shard equally likely. It doesn't make them equally full.

@end text="Full lesson on Learn"
The full lesson, where you can reseed and count, is on Learn.
