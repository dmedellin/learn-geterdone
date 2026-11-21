---
format: short
lesson: enterprise-patterns-layers-and-performance/performance-terms
title: The faster system is slower at twenty users
---

@art two-curves
Which system is faster? Wrong question.

@math items="A: 500 ms at 10 users, 500 ms at 20@System A;;B: 200 ms at 10 users, 2,000 ms at 20@System B"
In Fowler's illustration, System A answers in half a second at ten users and at twenty. System B answers in a fifth of a second at ten, and two seconds at twenty.

@words text="Faster at what load?"
So B wins at ten users and loses badly at twenty. Neither is faster. Each is faster at some load.

@end text="Full lesson on Learn"
The full lesson, with a lab for your own measurements, is on Learn.
