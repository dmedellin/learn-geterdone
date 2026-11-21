---
format: short
lesson: latency-and-the-tail/latency-budgets
title: Half your latency budget is gone before you write code
---

@art floors-eaten
A four hundred millisecond objective. How much of it can your code actually spend?

@math items="light-speed floor: 56 ms@fifty six;;2 round trips × 76 ms: 152 ms@two handshake;;left for code: 192 ms@a hundred and ninety two"
New York to London has a light speed floor of fifty six milliseconds. Two handshake round trips at seventy six take a hundred and fifty two more. That leaves a hundred and ninety two.

@words text="Subtract the floors first"
More than half the budget was physics and protocol. Subtract it first.

@end text="Full lesson on Learn"
The full lesson, with a budget to balance, is on Learn.
