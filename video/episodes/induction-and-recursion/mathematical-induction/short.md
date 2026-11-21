---
format: short
lesson: induction-and-recursion/mathematical-induction
title: The induction proof that all horses are the same colour
---

@art horse-groups
Here's a proof that all horses are the same colour. Spot the flaw.

@words text="k + 1 horses:  first k agree,  last k agree"
One horse is one colour. Given k plus one horses, the first k agree by hypothesis, and so do the last k. So they all agree.

@words text="k = 1:  no overlap"
The step breaks at k equals one. Two horses make two groups of one, which don't overlap, so nothing links them.

@art chain-anchor
One broken link breaks the whole chain. So test your step at the smallest values.

@end text="Full lesson on Learn"
The full lesson on induction is on Learn.
