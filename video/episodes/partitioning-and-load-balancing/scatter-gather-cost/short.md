---
format: short
lesson: partitioning-and-load-balancing/scatter-gather-cost
title: Sharding multiplied our requests by 24
---

@art scatter-fan
Four hundred queries a second. Your shards see nine thousand six hundred.

@math items="24 shards × 400 queries/s = 9 600 /s@nine thousand six hundred"
A query that can't be routed goes to every shard. With twenty four shards, four hundred client queries become nine thousand six hundred shard requests a second.

@art slowest-answer
And it waits for the slowest one. A shard with a p ninety nine of ninety milliseconds gives the query a p ninety nine of two hundred and fifty.

@end text="Full lesson on Learn"
The full lesson, with the tail worked out exactly, is on Learn.
