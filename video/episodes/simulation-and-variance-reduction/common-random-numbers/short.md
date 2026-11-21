---
format: short
lesson: simulation-and-variance-reduction/common-random-numbers
title: Same random numbers, much sharper comparison
---

@art shared-stream
Comparing two systems? Give them the same random numbers.

@math items="Var(A − B) = Var A + Var B − 2·Cov(A, B)@the variance"
The variance of a difference subtracts twice the covariance. Share the stream, and busy stretches hit both systems at once, so the covariance goes positive.

@art difference-spread
In the lesson's queue, the variance of the difference fell from about two point one to about point eight, a factor of two point six.

@end text="Full lesson on Learn"
The full lesson, with both schemes measured, is on Learn.
