---
format: short
lesson: dynamic-programming/the-fill-order-is-part-of-the-algorithm
title: Fill this table row by row and get a cheaper wrong answer
---

@art row-fill
Same recurrence, different fill order, and the answer drops by six thousand.

@words text="by length: 15 125 · row by row: 9 000"
Fill the matrix chain table by interval length, and it says fifteen thousand one hundred and twenty five. Fill it row by row, and it says nine thousand.

@words text="unwritten cell = 0"
Row by row reads cells before they're written. A missing cell acts like zero, so the minimum gets smaller, and nothing complains.

@end text="Full lesson on Learn"
Watch it go wrong on Learn.
