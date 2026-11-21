---
format: short
lesson: integer-programming/the-knapsack-and-set-covering-models
title: The greedy knapsack rule that's exact, and wrong
---

@art greedy-stuck
The value per weight rule is exactly optimal, and it still loses sixty on this knapsack.

@math items="relaxation: split the third, 240@split;;greedy whole: 160@greedy;;best whole: 220@best"
Three items, capacity fifty. If you may split, the rule fills the bag and gets two hundred and forty. Kept whole, greedy stops at a hundred and sixty. The best whole choice is two hundred and twenty.

@words text="Exact for the relaxation, not the model"
The rule solves the relaxation. It doesn't solve the zero one problem.

@end text="Full lesson on Learn"
The full lesson, with both models built from data, is on Learn.
