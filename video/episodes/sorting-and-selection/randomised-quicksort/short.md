---
format: short
lesson: sorting-and-selection/randomised-quicksort
title: Random pivots don't need a random input
---

@art five-arrays
Sorted, reversed, or built to kill quicksort. With random pivots, the expected cost is identical.

@math items="n = 9:  E[X] = 2593/126@nine keys"
At nine keys, it's two five nine three over a hundred and twenty six comparisons, on all five arrays, averaged over every pivot sequence there is.

@words text="The coins are the algorithm's"
The randomness is in the pivot choices, not the data. So the guarantee holds on every input, one at a time.

@end text="Full lesson on Learn"
The full lesson, with the exact derivation, is on Learn.
