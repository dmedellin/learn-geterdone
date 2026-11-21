---
format: short
lesson: markov-chains-decisions-and-queues/absorbing-states-and-the-fundamental-matrix
title: That inverse matrix is secretly counting
---

@art visit-counts
The inverse of I minus Q isn't just algebra. It counts visits.

@math items="N = I + Q + Q² + ⋯@I plus Q"
It's I plus Q plus Q squared, and so on. Each power is the chance of being at a state after exactly that many steps.

@art gambler-line
Add them, and you get expected visits. For a gambler starting with two of four units, that middle state is visited twice on average.

@end text="Full lesson on Learn"
The full lesson, with the gambler worked out, is on Learn.
