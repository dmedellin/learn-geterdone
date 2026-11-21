---
format: short
lesson: sorting-and-selection/partitioning
title: After partition, only one element is sorted
---

@art final-swap
After quicksort's partition, how much of the array is sorted? One element.

@math items="3 9 10 16 7@three, nine, ten;;24@twenty four;;43 55 38 27 91 82@forty three"
Partition around twenty four, and you get three, nine, ten, sixteen, seven. Then twenty four. Then forty three, fifty five, thirty eight, twenty seven, ninety one, eighty two.

@words text="Placed, not sorted"
The pivot is in its final place forever. The sides are just separated. Sorting them is the recursion's job.

@end text="Full lesson on Learn"
The full lesson, step by step, is on Learn.
