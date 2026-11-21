---
format: short
lesson: number-theory-and-cryptography/fermat-and-euler
title: Seven to the thousand in two multiplications
---

@words text="7¹⁰⁰⁰ mod 13"
Seven to the thousand, mod thirteen, takes just two multiplications.

@math items="1000 = 83 · 12 + 4@a thousand;;7¹⁰⁰⁰ ≡ 7⁴ ≡ 9@so seven to the"
Powers of seven return to one every twelve steps mod thirteen. A thousand is eighty three twelves, plus four. So seven to the thousand is seven to the fourth, which is nine.

@art exponent-wheel
That's Euler's theorem at work. Exponents reduce modulo phi of m, not modulo m, and phi of thirteen is twelve.

@end text="Full lesson on Learn"
The full lesson, with a powers lab, is on Learn.
