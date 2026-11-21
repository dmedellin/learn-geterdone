---
format: short
lesson: dynamic-programming-and-sequential-decisions/wagner-whitin-and-the-order-intervals
title: The rule that turns ordering into intervals
---

@art holding-overlap
An optimal ordering plan never orders while stock is left. Here's why that matters.

@art sawtooth-stock
If a period held stock and ordered, you could shift units into the later order. Same setups, less holding.

@art order-intervals
So each order covers a run of whole periods, exactly. A plan is just where the runs break, and dynamic programming searches those breaks instead of quantities.

@end text="Full lesson on Learn"
The full lesson, with a worked six period table, is on Learn.
