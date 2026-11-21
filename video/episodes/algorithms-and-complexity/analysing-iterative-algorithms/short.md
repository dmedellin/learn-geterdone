---
format: short
lesson: algorithms-and-complexity/analysing-iterative-algorithms
title: The loop that runs only log n times
---

@art doubling-hops
This loop climbs all the way to n, but it barely runs at all.

@math items="i = 1;  while i < n:  i = i · 2@double it;;1, 2, 4, 8, …@one, two;;runs ⌈log₂ n⌉ times@log two of n"
Start i at one, and double it until it reaches n. It takes the values one, two, four, eight, so the loop runs the ceiling of log two of n times.

@words text="Multiply or divide the counter → log n"
Whenever a counter is multiplied or divided by a constant, you've found a log factor.

@end text="Full lesson on Learn"
The full lesson on analysing loops is on Learn.
