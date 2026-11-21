---
format: short
lesson: sets-relations-functions/set-operations
title: The counting mistake that adds the overlap twice
---

@art double-count
Seven in one set, five in another. How many in the union?

@words text="7 + 5 = 12 ✗"
Not twelve, unless the sets share nothing. Adding the sizes counts every shared element twice, once in each.

@math items="|A ∪ B| = |A| + |B| − |A ∩ B|@subtract;;7 + 5 − 2 = 10@seven plus five"
So subtract the overlap once. If they share two elements, it's seven plus five minus two, which is ten.

@end text="Full lesson on Learn"
The full lesson, with set expressions you can evaluate, is on Learn.
