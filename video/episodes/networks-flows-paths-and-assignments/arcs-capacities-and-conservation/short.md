---
format: short
lesson: networks-flows-paths-and-assignments/arcs-capacities-and-conservation
title: Why adding up the imbalances never catches a bad flow
---

@art cancelling-errors
Your flow check says everything balances. It would say that for any flow.

@words text="Net outflows 4, −1, 1, −4" sub="against supplies 4, 0, 0, −4"
Change one arc from two units to one. Node a takes in one more than it sends. Node b sends one more than it takes in. The two errors cancel.

@words text="Report each node, not the total"
Every arc leaves one node and enters another, so the total imbalance is always zero. Check node by node.

@end text="Full lesson on Learn"
The full lesson, with a network you can edit, is on Learn.
