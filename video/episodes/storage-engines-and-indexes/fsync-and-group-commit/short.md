---
format: short
lesson: storage-engines-and-indexes/fsync-and-group-commit
title: Your database can only do 100 durable writes a second
---

@art one-per-fsync
A ten millisecond fsync. That's a hundred durable writes a second, total.

@math items="1 / 0.01 s = 100 /s@a hundred;;64 / 0.01 s = 6 400 /s@six thousand four hundred"
A write isn't durable until fsync returns, so one commit per fsync caps you at a hundred a second. Group sixty four commits behind one fsync, and the ceiling is six thousand four hundred.

@words text="Paid for with a wait to fill the batch"
The catch is the wait while the batch fills.

@end text="Full lesson on Learn"
The full lesson, with the latency curve, is on Learn.
