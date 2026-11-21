---
format: short
lesson: replication-and-consistency/replication-lag-and-stale-reads
title: Wait the average replication lag, and one read in five is still stale
---

@art balance-point
Average replication lag is thirty one milliseconds. So wait thirty one, and you're safe? One read in five is stale.

@math items="mean lag = 31.45 ms@the mean;;P(lag > 31.45 ms) = 1/5@a fifth of the lag"
Most of the lag is ten milliseconds, which pulls the mean down. But a fifth of the lag is longer than the mean.

@words text="Stale = the tail past your delay"
A stale read is the tail past your delay. Ask for a percentile, never the mean.

@end text="Full lesson on Learn"
The full lesson, with a measured lag to read, is on Learn.
