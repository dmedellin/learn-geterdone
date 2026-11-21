---
format: short
lesson: geometric-algorithms/the-orientation-test
title: There's no such thing as nearly collinear
---

@art near-collinear
These three points are almost on a line. Almost doesn't count.

@math items="7·2 − 3·5 = −1@seven times two;;area = 1/2@one half"
Take zero, zero, then seven, three, then five, two. The orientation determinant is seven times two, minus three times five, which is minus one. That's a triangle of area one half.

@words text="Smallest nonzero determinant: 1"
With integer coordinates, one is the smallest nonzero value there is. So this is a real right turn, and rounding it to zero would be wrong.

@end text="Full lesson on Learn"
The full lesson on the orientation test is on Learn.
