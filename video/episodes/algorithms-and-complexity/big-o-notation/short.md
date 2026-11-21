---
format: short
lesson: algorithms-and-complexity/big-o-notation
title: Quicksort is O(n log n)? Not quite
---

@words text="Quicksort is O(n log n)?"
You've heard quicksort is big O of n log n. As stated, that's false.

@art ceiling-curve
Big O is an upper bound, and quicksort's worst case is Theta of n squared. No n log n ceiling holds it.

@words text="Average case: Θ(n log n)" sub="worst case: Θ(n²)"
What's true is that its average case is Theta of n log n. So whenever you quote a bound, say which case it's bounding.

@end text="Full lesson on Learn"
The full lesson on big O, Omega and Theta is on Learn.
