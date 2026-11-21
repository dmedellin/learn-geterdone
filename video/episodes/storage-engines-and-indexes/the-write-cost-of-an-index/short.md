---
format: short
lesson: storage-engines-and-indexes/the-write-cost-of-an-index
title: Your first index halves your insert rate
---

@art insert-fanout
Add three indexes to a table. You just lost three quarters of your insert rate.

@math items="writes per insert = k + 1@k plus one;;10 000 / 4 = 2 500 inserts/s@two thousand five hundred"
Every insert writes the row, plus one random page in every index. That's k plus one writes. On a device doing ten thousand random writes a second, three indexes leave two thousand five hundred inserts.

@words text="It divides. It doesn't subtract."
And the very first index costs the most. It halves the rate.

@end text="Full lesson on Learn"
The full lesson, with an index budget calculator, is on Learn.
