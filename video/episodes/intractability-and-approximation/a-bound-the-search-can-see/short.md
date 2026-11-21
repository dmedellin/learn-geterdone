---
format: short
lesson: intractability-and-approximation/a-bound-the-search-can-see
title: Cut the search tree, keep the exact answer
---

@art search-tree
Same knapsack, same answer, fourteen nodes instead of forty four.

@art fractional-fill
At each node, let the remaining items be split into fractions. That's easy to solve, and it can only beat what the branch can really reach.

@words text="bound ≤ best so far  ⟹  cut"
So if that bound can't beat your best answer so far, cut the branch. Nothing in it can be better.

@end text="Full lesson on Learn"
The full lesson is on Learn.
