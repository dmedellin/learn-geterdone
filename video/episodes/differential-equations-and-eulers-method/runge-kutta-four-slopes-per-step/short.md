---
format: short
lesson: differential-equations-and-eulers-method/runge-kutta-four-slopes-per-step
title: Halve the step, divide the error by sixteen
---

@art sixteen-shrink
Halve the step, and this method's error doesn't halve. It falls by sixteen.

@math items="h = 1/4:   1/30720@at a quarter;;h = 1/8:   1/491520@At an eighth;;ratio:  16@sixteen times"
Runge Kutta reads four slopes per step, with weights one, two, two, one. On y prime equals t to the fourth, its error at a quarter is one over thirty thousand seven hundred and twenty. At an eighth, it's sixteen times smaller.

@words text="error ≈ C·h⁴"
That's what fourth order means.

@end text="Full lesson on Learn"
The full lesson, with a lab that runs it exactly, is on Learn.
