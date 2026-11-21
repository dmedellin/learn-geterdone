---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/pessimistic-and-coarse-grained-locks
title: Why a finer lock can protect less
---

@art line-locks
Two people edit two different lines of one order. Should both be allowed?

@words text="Lock per line: both commit"
With a lock per line, both commit. But if the order has a credit limit, each change can keep the rule, and together they break it.

@art root-lock
Lock the order instead. Now the second editor is refused at once, before doing any work, and the order's rule holds.

@end text="Full lesson on Learn"
The full lesson, with a lab that replays it, is on Learn.
