---
format: short
lesson: integer-programming/when-rounding-fails-the-lp-relaxation
title: Rounding an LP answer: three of four roundings break a row
---

@art rounding-box
Round your fractional answer, and three of the four ways to do it break a row.

@math items="LP corner (9/4, 3/2)@nine quarters;;(2, 1) feasible, worth 10@two, one;;best whole plan (0, 3), worth 12@zero, three"
The relaxation stops at nine quarters, three halves. Of its four roundings, only two, one is feasible, worth ten. The best whole plan is zero, three, worth twelve.

@words text="Not a rounding at all"
Zero, three is at the far end of the region. Rounding never looks there.

@end text="Full lesson on Learn"
The full lesson, with every whole plan to test, is on Learn.
