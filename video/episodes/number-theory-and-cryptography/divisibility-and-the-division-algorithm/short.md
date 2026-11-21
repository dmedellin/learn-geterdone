---
format: short
lesson: number-theory-and-cryptography/divisibility-and-the-division-algorithm
title: Minus seven mod three is not minus one
---

@art number-line-steps
What's minus seven mod three? Your programming language might get it wrong.

@math items="−7 = (−3)(3) + 2@minus three times three;;✗  −7 = (−2)(3) − 1@minus two times three"
Minus seven is minus three times three, plus two. You could write minus two times three, minus one, but the theorem needs a remainder of at least zero.

@words text="−7 mod 3 = 2" sub="C-style % says −1"
So minus seven mod three is two. C style percent says minus one. The mathematics agrees with Python.

@end text="Full lesson on Learn"
The full lesson, with a division lab, is on Learn.
