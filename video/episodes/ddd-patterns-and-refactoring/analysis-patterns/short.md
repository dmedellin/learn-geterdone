---
format: short
lesson: ddd-patterns-and-refactoring/analysis-patterns
title: Two accounting errors that hide each other
---

@art offsetting-errors
Two bookkeeping errors, and the grand total says you're only off by three.

@math items="t3: +27.00@plus twenty seven;;t4: −24.00@minus twenty four;;total: +3.00@three"
One transaction is off by plus twenty seven. Another by minus twenty four. Added together, the total of all entries is just three.

@words text="Every transaction nets to zero"
So check each movement on its own. That's what Fowler's Transaction buys: its entries must net to zero.

@end text="Full lesson on Learn"
Find the slips in a box office week in the full lesson on Learn.
