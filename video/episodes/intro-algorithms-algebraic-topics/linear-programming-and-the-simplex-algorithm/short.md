---
format: short
lesson: intro-algorithms-algebraic-topics/linear-programming-and-the-simplex-algorithm
title: The simplex method never tries every corner
---

@art corner-walk
The simplex method doesn't check every corner. It walks.

@math items="(0, 0) → (0, 6) → (2, 6)@from the origin;;z: 0 → 30 → 36@thirty six"
On the lesson's program, it goes from the origin to zero, six, then to two, six, as z climbs to thirty six. Three of the five corners, in two pivots.

@words text="No positive coefficient → stop"
Each pivot moves to a neighbouring corner that's no worse. When no coefficient in z is positive, it stops.

@end text="Full lesson on Learn"
Walk the corners in the full lesson on Learn.
