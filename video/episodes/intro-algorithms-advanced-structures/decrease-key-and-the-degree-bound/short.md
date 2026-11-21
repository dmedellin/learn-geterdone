---
format: short
lesson: intro-algorithms-advanced-structures/decrease-key-and-the-degree-bound
title: Why Fibonacci heaps are named after Fibonacci
---

@art children-in-order
Why is a Fibonacci heap named after Fibonacci?

@art mark-flag
Because of one rule. A node that loses a second child is cut from its parent.

@math items="size ≥ 1, 2, 3, 5, 8, 13@one, two, three, five;;not 1, 2, 4, 8, 16, 32@instead of"
That rule means a node of degree k still has at least F of k plus two nodes below it: one, two, three, five, eight, thirteen, instead of the binomial doubling.

@end text="Full lesson on Learn"
That's what keeps every degree logarithmic. Full lesson on Learn.
