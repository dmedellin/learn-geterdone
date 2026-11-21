---
format: short
lesson: combinatorics-and-counting/binomial-coefficients
title: Why every row of Pascal's triangle is a power of two
---

@art pascal-triangle
Every row of Pascal's triangle adds up to a power of two. Why?

@math items="1 + 6 + 15 + 20 + 15 + 6 + 1 = 64 = 2⁶@two to the sixth"
Take row six: one, six, fifteen, twenty, fifteen, six, one. Add them, and you get sixty four, which is two to the sixth.

@art fixed-element
Row n counts the subsets of an n element set, grouped by size. So the whole row counts every subset once. And each element is either in or out, which gives two to the n.

@words text="Σ C(n, k) = 2ⁿ"
One set, counted two ways.

@end text="Full lesson on Learn"
The full lesson, with the hockey stick, is on Learn.
