---
format: short
lesson: dynamic-programming/the-knapsack-table-and-what-each-cell-reads
title: Why the knapsack table isn't really polynomial
---

@art grid-axes
The knapsack table looks polynomial. It isn't, quite.

@words text="Θ(nW)"
It fills one cell for every item, times every capacity up to W. But W is a number, not a count.

@math items="capacity 99:  500 cells@ninety nine;;capacity 99 999:  500 000 cells@ninety nine thousand"
Four items at capacity ninety nine need five hundred cells. At ninety nine thousand nine hundred and ninety nine, five hundred thousand. Three more digits, a thousand times the work.

@end text="Full lesson on Learn"
Fill the table on Learn.
