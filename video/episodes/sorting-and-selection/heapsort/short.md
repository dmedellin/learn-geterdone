---
format: short
lesson: sorting-and-selection/heapsort
title: Heapsort charges the most for sorted input
---

@art build-vs-teardown
Give heapsort an array that's already sorted, and it does more work than on a shuffle.

@math items="increasing:  85@increasing;;shuffled:  80@shuffled;;decreasing:  72@decreasing"
At sixteen keys, increasing input costs eighty five comparisons. Shuffled, eighty. Decreasing, seventy two.

@words text="Not adaptive"
Ascending order is the worst start for a max heap, so every key has to travel. The n log n bound holds on every input, and no input is good.

@end text="Full lesson on Learn"
The full lesson, counted by hand, is on Learn.
