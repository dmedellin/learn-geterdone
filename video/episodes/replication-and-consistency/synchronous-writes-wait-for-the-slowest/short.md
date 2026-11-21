---
format: short
lesson: replication-and-consistency/synchronous-writes-wait-for-the-slowest
title: Three synchronous replicas aren't three times slower
---

@art parallel-vs-serial
One replica's p ninety nine is sixteen milliseconds. Three replicas: forty eight? No. Twenty four.

@math items="0.992² = 0.984064 < 0.99@point nine nine two;;0.998² = 0.996004 ≥ 0.99  →  24 ms@point nine nine eight"
A synchronous write waits for the slowest of two followers, so you square the distribution. Point nine nine two squared falls short of ninety nine percent. Point nine nine eight squared clears it, at twenty four milliseconds.

@words text="Parallel waits cost the slowest, not the sum"
Parallel waits cost the slowest, not the sum.

@end text="Full lesson on Learn"
The full lesson, with replicas to add, is on Learn.
