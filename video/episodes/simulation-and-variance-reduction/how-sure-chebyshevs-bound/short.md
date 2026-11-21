---
format: short
lesson: simulation-and-variance-reduction/how-sure-chebyshevs-bound
title: Plus or minus two standard errors is not 95%
---

@art narrow-misses
Plus or minus two standard errors does not guarantee ninety five percent.

@math items="k = 2:  1 − 1/4 = 3/4@three quarters;;k = 5:  1 − 1/25 = 96%@ninety six"
With no assumption about the distribution, Chebyshev guarantees one minus one over k squared. At two, that's three quarters. To guarantee ninety six percent, you need five.

@words text="95% assumes normality"
The ninety five comes from a normal approximation. Chebyshev assumes nothing at all, so it holds for any shape.

@end text="Full lesson on Learn"
The full lesson, with forty replications counted, is on Learn.
