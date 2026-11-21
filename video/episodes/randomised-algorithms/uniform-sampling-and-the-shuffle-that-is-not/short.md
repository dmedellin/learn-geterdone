---
format: short
lesson: randomised-algorithms/uniform-sampling-and-the-shuffle-that-is-not
title: One division proves this shuffle is broken
---

@art unequal-piles
The shuffle most people write is biased, and one division proves it.

@math items="4⁴ = 256 tapes@two hundred and fifty six;;4! = 24 permutations@twenty four;;256 = 24 × 10 + 16@sixteen left over"
Swap each position with any random position. On four items, that's two hundred and fifty six equally likely runs, and twenty four permutations. Divide, and you get ten, with sixteen left over.

@words text="No equal piles, so not uniform"
Some permutation must get more runs than another. Use Fisher Yates instead.

@end text="Full lesson on Learn"
The full lesson is on Learn.
