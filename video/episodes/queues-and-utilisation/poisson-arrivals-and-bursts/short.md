---
format: short
lesson: queues-and-utilisation/poisson-arrivals-and-bursts
title: Size for the mean and you overflow two windows in five
---

@art overflow-tail
Expecting ten arrivals per window, so you make room for ten? You'll overflow two windows in five.

@math items="C = 10:  P(overflow) ≈ 0.42@room for ten;;C = 18:  P(overflow) ≤ 1/100@eighteen"
Random arrivals land above their mean about half the time. With room for ten, the chance of overflowing is about nought point four two. To overflow just one window in a hundred, you need room for eighteen.

@words text="Headroom is the number"
The target overflow rate sets the capacity.

@end text="Full lesson on Learn"
The full lesson, with the tail on a slider, is on Learn.
