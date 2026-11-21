---
format: short
lesson: intro-algorithms-sorting/medians-and-order-statistics
title: Groups of five make the median linear
---

@art groups-of-five
Why groups of five? Because one fifth plus seven tenths is less than one.

@art guarantee-block
Take the median of each group of five, then the median of those. At least three tenths of the keys sit on each side of it.

@math items="T(⌈n/5⌉) + T(7n/10 + 6) + O(n)@a fifth;;1/5 + 7/10 = 9/10 < 1@nine tenths"
So the two recursive calls handle a fifth and at most seven tenths. Together that's nine tenths, and each level shrinks. The total is linear.

@end text="Full lesson on Learn"
Find a median yourself in the full lesson on Learn.
