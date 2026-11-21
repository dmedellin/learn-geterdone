---
format: short
lesson: intractability-and-approximation/charging-every-element
title: The pricing trick that proves greedy set cover works
---

@art charges
To bound greedy set cover, put a price on every element.

@words text="cover k new elements → charge 1/k each"
Each set costs one. Split that cost equally over the elements it newly covers. The prices then add up to exactly the number of sets.

@math items="each price ≤ OPT / r@at most;;total ≤ OPT · Hₙ@the harmonic number"
When r elements remain, the next one pays at most the optimum over r. Add those up, and greedy is within the harmonic number of the optimum.

@end text="Full lesson on Learn"
The full lesson is on Learn.
