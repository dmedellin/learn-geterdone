---
format: short
lesson: replication-and-consistency/reads-scale-writes-do-not
title: Three replicas don't give you three times the throughput
---

@art write-every-copy
Add replicas, and your write capacity doesn't move at all.

@words text="Reads: N× · Writes: 1×"
A read needs one copy. A write has to reach every copy. So N replicas serve N times the reads, and exactly the same writes.

@math items="ρ = 9, N = 3:  1 / (1/10 + 3/10) = 2.5×@nine reads;;ceiling 1 + ρ = 10×@the ceiling"
At nine reads per write, three replicas give two and a half times. And the ceiling is ten, however many you buy.

@end text="Full lesson on Learn"
The full lesson, with all four multipliers, is on Learn.
