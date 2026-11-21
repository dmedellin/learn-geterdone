---
format: short
lesson: induction-and-recursion/recursive-algorithms
title: Binary search on unsorted data still finishes. That's the problem.
---

@art sorted-bars
Run binary search on unsorted data. It still finishes, and it's wrong.

@words text="terminates  ≠  correct"
Why it stops has nothing to do with sorting. The range shrinks at every call, so it always finishes.

@art shrinking-range
But throwing away half the array is only safe because the data is sorted. Without that, it returns a confident wrong answer. So prove both: it stops, and it's right.

@end text="Full lesson on Learn"
The full lesson on recursive algorithms is on Learn.
