---
format: short
lesson: markov-chains-decisions-and-queues/the-cut-equation-and-every-queue-from-it
title: One line that solves every simple queue
---

@art cut-line
Draw one line between two states, and the whole queue falls out.

@art alternating-crossings
The chain only moves one step at a time, so it crosses that line up exactly as often as it crosses down.

@math items="πₙ λₙ = πₙ₊₁ μₙ₊₁@pi n"
So pi n times the arrival rate equals pi n plus one times the service rate. Chain those ratios from zero, divide by the total, and you have every probability.

@end text="Full lesson on Learn"
The full lesson, with a repair shop worked out, is on Learn.
