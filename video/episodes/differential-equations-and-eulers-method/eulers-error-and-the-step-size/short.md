---
format: short
lesson: differential-equations-and-eulers-method/eulers-error-and-the-step-size
title: Tiny misses, bigger error
---

@art pieces-add
Each step of Euler's method misses by a tiny amount. So why is the total so much bigger?

@math items="one step misses by h²@h squared;;1/h steps:   (1/h)·h² = h@one over h steps"
On y prime equals two t, every step misses by exactly h squared. But reaching one takes one over h steps. One over h, times h squared, is h.

@words text="halve h → halve the error"
So halve the step, and the error halves. That's what first order means.

@end text="Full lesson on Learn"
The full lesson, with a lab that measures the error, is on Learn.
