---
format: short
lesson: first-order-linear-equations/stiffness-when-the-step-is-too-big
title: A step of one half breaks Euler's method
---

@art blow-up-steps
A step of one half sounds small. It can turn decay into explosive growth.

@math items="y′ = −5y,  h = 1/2@minus five y;;factor 1 − 5/2 = −3/2@minus three halves;;y₈ = 6561/256 ≈ 25.6@after eight steps"
On y prime equals minus five y, each Euler step multiplies by one minus five halves, minus three halves. After eight steps you're at about twenty five point six, while the true value is almost zero.

@words text="small means h < 2/a"
Euler needs h below two over a. Here, two fifths.

@end text="Full lesson on Learn"
The full lesson, with the backward step, is on Learn.
