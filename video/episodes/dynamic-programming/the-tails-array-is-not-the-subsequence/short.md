---
format: short
lesson: dynamic-programming/the-tails-array-is-not-the-subsequence
title: The fast LIS algorithm's array is a trap
---

@art two-checks
The fast increasing subsequence algorithm gets the length right, and the answer wrong.

@words text="3 1 4 1 5 9 2 6 5 3"
Run its tails array on this sequence, one value at a time.

@words text="tails: 1 2 3 6" sub="increasing ✓ · in the input ✗"
It ends as one, two, three, six. Length four, and increasing. But the only six comes before the last three, so it's not a subsequence at all. The array tracks lengths, not a run.

@end text="Full lesson on Learn"
Compare both methods on Learn.
