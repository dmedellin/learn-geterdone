---
format: short
lesson: combinatorics-and-counting/generating-functions
title: Counting coins by multiplying series
---

@art coin-stacks
How many ways can you make twenty five cents from pennies, nickels and dimes?

@art series-factors
Give each coin a series. Pennies can add any amount, nickels only multiples of five, and dimes only multiples of ten. Multiply the three series together.

@math items="[x²⁵] of the product = 12@twelve"
Each way to split twenty five cents among the coins gives one x to the twenty fifth in the product. So its coefficient is the answer: twelve.

@words text="multiply series = combine choices"
Multiplying series combines independent choices. That's a generating function.

@end text="Full lesson on Learn"
The full lesson, with constraints and recurrences, is on Learn.
