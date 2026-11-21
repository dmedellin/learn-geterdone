---
format: short
lesson: geometric-algorithms/inside-by-parity-and-by-winding
title: Is the point inside? Count to six
---

@art comb
Walk a point across this comb and the ray counts down six, five, four.

@math items="6 · 5 · 4 · 3 · 2 · 1@six crossings"
Cast a ray to the right and count the edges it crosses. Outside on the left, six crossings. Then five, four, three, two, one, as the point moves right.

@words text="Odd: inside · Even: outside"
Each step passes one edge and flips the parity. Odd means inside, even means outside.

@end text="Full lesson on Learn"
The full lesson, with the winding number, is on Learn.
