---
format: short
lesson: intro-algorithms-design-techniques/matroids-and-greedy-methods
title: The one property that makes greedy always work
---

@art exchange-grow
One property decides whether greedy is always right. It's called exchange.

@words text="A smaller independent set can always grow"
If you have two independent sets, and one is smaller, you can always move an element from the bigger one into the smaller one, and stay independent.

@art greedy-pick
Any family with that property, and closed under subsets, is a matroid. On every matroid, taking the heaviest element that still fits is optimal.

@end text="Full lesson on Learn"
Test some families in the full lesson on Learn.
