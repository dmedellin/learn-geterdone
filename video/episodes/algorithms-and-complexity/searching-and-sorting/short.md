---
format: short
lesson: algorithms-and-complexity/searching-and-sorting
title: Binary search's most dangerous failure
---

@art unsorted-trap
Binary search on unsorted data doesn't crash. It confidently gives you the wrong answer.

@art halving-range
Binary search compares with the middle, then throws away half. That's only safe because the array is sorted: everything in the discarded half really is on the wrong side.

@words text="Unsorted → it stops, and it's wrong"
On unsorted data it still stops, and nothing tells you the answer is wrong. So sort first, or don't use it.

@end text="Full lesson on Learn"
The full lesson on searching and sorting is on Learn.
