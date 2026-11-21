---
format: short
lesson: sorting-and-selection/median-of-medians
title: Groups of three make this algorithm n log n
---

@art flat-levels
Median of medians uses groups of five. With groups of three, it stops being linear.

@math items="g = 5:  1/5 + 7/10 = 9/10@groups of five;;g = 3:  1/3 + 2/3 = 1@groups of three"
The two recursive calls take a fraction of the array each. With groups of five, they add to nine tenths, so each level shrinks. With groups of three, they add to exactly one.

@words text="Sum = 1 → n log n"
Then every level costs n, for log n levels. That's as slow as sorting.

@end text="Full lesson on Learn"
The full lesson, with the level sums worked out, is on Learn.
