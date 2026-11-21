---
format: short
lesson: geometric-algorithms/the-two-furthest-points
title: Find the furthest pair without checking every pair
---

@art cloud-rectangle
Sixteen points make a hundred and twenty pairs. You only need to check four.

@art interior-average
The furthest pair is always two hull vertices, so the twelve inside points drop out. And it's always an antipodal pair, where parallel rulers can touch the hull at both.

@math items="4 pairs  vs  120@four antipodal pairs;;12² + 9² = 225@twelve squared"
Here the hull is a rectangle, with four antipodal pairs. Twelve squared plus nine squared gives a squared diameter of two hundred and twenty five.

@end text="Full lesson on Learn"
The full lesson, with rotating calipers, is on Learn.
