---
format: short
lesson: intro-algorithms-algebraic-topics/multithreaded-algorithms
title: Eight times the processors, a third off the time
---

@art serial-merge
Eight times the processors, and only about a third off the time. Why?

@math items="parallelism ≈ 5.5@five and a half;;8 → 64 processors: 3,455 → 2,223@eight to sixty four"
Merge sort with a serial merge, on a thousand and twenty four keys, has a parallelism of about five and a half. Going from eight to sixty four processors only lowers the bound from three thousand four hundred fifty five to two thousand two hundred twenty three.

@words text="T_P ≥ T∞"
The span sets a floor that no number of processors can break.

@end text="Full lesson on Learn"
Find the span yourself in the full lesson on Learn.
