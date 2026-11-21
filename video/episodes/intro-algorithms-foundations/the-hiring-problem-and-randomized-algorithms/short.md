---
format: short
lesson: intro-algorithms-foundations/the-hiring-problem-and-randomized-algorithms
title: A thousand candidates, about seven hires
---

@art candidate-line
Interview a thousand candidates in random order. You'll hire about seven.

@math items="Pr{candidate i is hired} = 1/i@one over i;;1 + 1/2 + … + 1/n = Hₙ ≈ ln n@add them up"
You hire candidate i only if they're the best of the first i. In a random order, the chance is one over i. Add them up, and you get the harmonic number, about the natural log of n.

@art shuffle
And if you shuffle the list yourself first, that holds for every input.

@end text="Full lesson on Learn"
Average every order yourself in the full lesson on Learn.
