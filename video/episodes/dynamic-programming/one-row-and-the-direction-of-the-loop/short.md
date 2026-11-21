---
format: short
lesson: dynamic-programming/one-row-and-the-direction-of-the-loop
title: Flip one loop and solve a different knapsack
---

@art forward-sweep
Reverse one loop, and your knapsack starts reusing items.

@words text="row[w] = max(row[w], row[w − weight] + value)"
Shrink the knapsack table to one row, and update each cell from a cell to its left.

@math items="backward  →  17  each item once@Sweep backward;;forward  →  19  items reused@sweep forward"
Sweep backward, and the cell you read is still from before this item, so each item is used once. Seventeen. Sweep forward, and it already includes this item. Nineteen. Both are right, for different problems.

@end text="Full lesson on Learn"
Try both on Learn.
