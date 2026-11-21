---
format: short
lesson: number-theory-and-cryptography/hashing-and-pseudorandom-numbers
title: Change one number and the random generator dies
---

@words text="xₙ₊₁ = (a·xₙ + 3) mod 16"
Change one number by one, and this random number generator dies.

@math items="a = 5:  1, 8, 11, 10, 5, 12, …@with a equal to five;;a = 6:  1, 9, 9, 9, …@with a equal to six"
With a equal to five, from seed one, it visits all sixteen values before repeating. With a equal to six, it gives one, then nine, nine, nine, forever.

@art dead-generator
Six minus one is five, and two doesn't divide it, so the Hull Dobell conditions fail.

@end text="Full lesson on Learn"
The full lesson, with a generator lab, is on Learn.
