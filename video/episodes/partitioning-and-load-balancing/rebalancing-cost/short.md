---
format: short
lesson: partitioning-and-load-balancing/rebalancing-cost
title: Halve your rebalance time, overload every node
---

@art throttle-trade
Your rebalance takes sixteen hours. Double the throttle to finish in eight?

@math items="200 MB/s:  serves 6 000 /s,  ρ 83.33%@two hundred;;400 MB/s:  serves 4 000 /s < 5 000 arriving@four hundred"
At two hundred megabytes a second, the copy takes a quarter of each node's budget, and utilisation sits at eighty three point three three percent. At four hundred, it takes half, and the node serves four thousand requests against five thousand arriving.

@words text="The workload sets the ceiling"
The queue just grows until the copy ends.

@end text="Full lesson on Learn"
The full lesson, with the throttle on a slider, is on Learn.
