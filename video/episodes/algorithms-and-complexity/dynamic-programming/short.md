---
format: short
lesson: algorithms-and-complexity/dynamic-programming
title: Forty billion calls, or fifty
---

@art fib-tree
Computing the fiftieth Fibonacci number the naive way takes about forty billion calls.

@words text="F(5) → F(3) twice, F(2) three times"
The naive recursion keeps recomputing the same values. F of five calls F of three twice, and F of two three times.

@list items="Naive: about 40 000 000 000 calls@about forty billion|Memoised: 50 calls@just fifty"
Store each value the first time you compute it, and about forty billion calls becomes just fifty. That's dynamic programming.

@end text="Full lesson on Learn"
The full lesson on dynamic programming is on Learn.
