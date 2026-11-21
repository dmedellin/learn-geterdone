---
format: short
lesson: intro-algorithms-design-techniques/activity-selection-and-the-greedy-strategy
title: Greedy fails the knapsack, unless you cut
---

@art knapsack-whole
Fill a knapsack greedily by value per pound, and you can lose.

@math items="greedy: 1 + 3 lb → 3 + 7 = 10@greedy;;better: 3 + 4 lb → 7 + 9 = 16@three and four"
Capacity seven, items weighing one, three and four, worth three, seven and nine. Greedy takes the first two, for ten. But three and four pounds together fit exactly, worth sixteen.

@art knapsack-fraction
Allow fractions, and greedy is optimal: sixteen point seven five.

@end text="Full lesson on Learn"
See when greedy is safe in the full lesson on Learn.
