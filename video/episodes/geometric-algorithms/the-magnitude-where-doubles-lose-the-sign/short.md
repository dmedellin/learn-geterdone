---
format: short
lesson: geometric-algorithms/the-magnitude-where-doubles-lose-the-sign
title: One power of two, and floating point loses a turn
---

@art product-collision
One power of two bigger, and floating point calls a right turn straight.

@math items="(2ᵏ + 1)(2ᵏ − 1) − 2ᵏ·2ᵏ = −1@minus one;;k ≥ 27: both products round to 2²ᵏ@twenty seven"
The determinant of this family is exactly minus one at every size. But once k reaches twenty seven, both products round to the same double, and the difference is zero.

@words text="A collapse, never a flip"
And it only ever collapses. Rounding is monotone, so the double can lose a turn but never report the opposite one.

@end text="Full lesson on Learn"
The full lesson, with the sweep, is on Learn.
