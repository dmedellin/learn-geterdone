---
format: short
lesson: algorithms-and-complexity/recursion-trees-and-amortised-analysis
title: Why doubling an array makes it fast
---

@art doubling-array
Sometimes adding one item copies the whole array. It's still constant time, amortised.

@math items="copies: 1 + 2 + 4 + ⋯ < 2n@the copies;;plus n insertions: total < 3n@plus the n"
If the array doubles when it's full, the copies cost one, two, four, and so on, less than two n in total. Plus the n insertions, that's under three n.

@words text="Under 3 per insertion, amortised"
So across any sequence, each insertion costs under three. Grow by a fixed amount instead, and it's linear per insertion.

@end text="Full lesson on Learn"
The full lesson on amortised analysis is on Learn.
