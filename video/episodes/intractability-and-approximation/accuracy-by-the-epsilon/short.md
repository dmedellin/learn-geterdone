---
format: short
lesson: intractability-and-approximation/accuracy-by-the-epsilon
title: A knapsack shortcut that can make things worse
---

@art scaling-backfires
This knapsack shortcut shrinks the table. Sometimes it grows it fivefold.

@words text="K = ε · vmax / n"
It divides every value by K and solves the smaller table. With big values, the table shrinks from three thousand six hundred and four cells to two hundred and thirty eight.

@math items="K = 9/50 < 1@nine fiftieths;;32 cells → 171@a hundred and seventy one"
But on five tiny values, K is nine fiftieths, less than one. Dividing makes the values bigger, and the table grows to a hundred and seventy one cells.

@end text="Full lesson on Learn"
The full lesson is on Learn.
