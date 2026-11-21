---
format: short
lesson: markov-chains-decisions-and-queues/markov-decision-processes-and-policy-iteration
title: Policy iteration knows when it's finished
---

@art staircase-up
Most algorithms stop when the numbers stop moving. This one stops for a reason.

@art evaluate-improve
Policy iteration solves each policy's value exactly, then switches every state to its best action. The value never goes down.

@words text="Finitely many policies"
And there are only finitely many policies. So when nothing switches, you've provably reached the optimum. Here, that took two rounds.

@end text="Full lesson on Learn"
The full lesson, with the exact values, is on Learn.
