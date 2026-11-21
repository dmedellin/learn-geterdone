---
format: short
lesson: simulation-and-variance-reduction/control-variates
title: Cut simulation noise with a number you already know
---

@art tilt-correction
You can remove almost half your simulation's variance with something you're already counting.

@words text="X − b(C − E[C])"
In the lesson's queue, the number of arrivals has a known mean: two hundred slots at two fifths, exactly eighty. Subtract the right multiple of how far it strayed.

@math items="Var: 1.53 → 0.83@one point five three"
The correction averages to zero, so nothing is biased. And the variance falls from one point five three to point eight three.

@end text="Full lesson on Learn"
The full lesson, with the parabola to slide, is on Learn.
