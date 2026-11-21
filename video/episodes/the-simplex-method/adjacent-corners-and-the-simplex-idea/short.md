---
format: short
lesson: the-simplex-method/adjacent-corners-and-the-simplex-idea
title: Why simplex never checks every corner
---

@art corner-path
The simplex method finds the best corner without looking at most of them.

@math items="(0, 0) → (0, 6) → (2, 6)@zero, six;;z: 0 → 30 → 36@thirty six"
On this region there are five corners. From the origin, the method steps to zero, six, then to two, six, raising z to thirty six. Every edge out of there goes down, so it stops.

@words text="A plane on a convex region: local is global"
Because the objective is a plane and the region has no dents, a corner that beats its neighbours beats everything.

@end text="Full lesson on Learn"
The full lesson, with bases to swap, is on Learn.
