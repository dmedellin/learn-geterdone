---
format: short
lesson: differential-equations-and-eulers-method/the-improved-euler-method
title: One extra slope, eleven times less error
---

@art average-slope
Read one extra slope per step, and the error can drop eleven times.

@math items="Euler,  h = 1/4:   11/96@Euler's error;;improved,  h = 1/4:   1/96@The improved method"
On y prime equals t squared, at a step of a quarter, Euler's error is eleven ninety sixths. The improved method, which averages the slopes at both ends of each step, gets one ninety sixth.

@words text="halve h → the error ÷ 4"
And halve the step, and its error falls to a quarter, not a half.

@end text="Full lesson on Learn"
The full lesson, with a lab for both methods, is on Learn.
