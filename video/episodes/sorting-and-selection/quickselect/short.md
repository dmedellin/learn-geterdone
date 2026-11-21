---
format: short
lesson: sorting-and-selection/quickselect
title: Don't sort to find a median
---

@art discard-side
Sorting to find the median does far more work than you need.

@words text="Partition, then keep one side"
Partition around a pivot. The value you want is on one known side, so throw the other side away, unexamined.

@math items="sort, then index:  83@sorting first;;quickselect:  35@quickselect"
For the twelfth smallest of twenty four keys, sorting first costs eighty three comparisons. Quickselect, with that seed, costs thirty five. With random pivots, it's expected linear.

@end text="Full lesson on Learn"
The full lesson, with the linear-time argument, is on Learn.
