---
format: short
lesson: the-simplex-method/artificial-variables-and-two-phase-simplex
title: A one-line proof that no solution exists
---

@art empty-region
How do you prove a set of constraints has no solution at all?

@math items="x₁ + x₂ ≤ 1@at most one;;x₁ + x₂ ≥ 4@at least four;;combine with (−1, 1):  0 ≥ 3@zero at least three"
Take x one plus x two at most one, and x one plus x two at least four. Phase one stops at three. Combine the rows with minus one and one, and you get zero at least three.

@words text="Phase one's value is the certificate"
It's not a bug. It's a proof.

@end text="Full lesson on Learn"
The full lesson, with both phases, is on Learn.
