---
format: short
lesson: number-theory-and-cryptography/bezout-and-modular-inverses
title: Where RSA's private key comes from
---

@words text="17 × ? ≡ 1 (mod 3120)"
What times seventeen gives one, mod three thousand one hundred and twenty? RSA needs it.

@math items="1 = 2 · 3120 − 367 · 17@run Euclid's algorithm;;−367 + 3120 = 2753@add the modulus"
Run Euclid's algorithm backwards, and one comes out as two times three thousand one hundred and twenty, minus three hundred and sixty seven times seventeen. Add the modulus, and you get two thousand seven hundred and fifty three.

@art round-trip
That's the private exponent of the textbook RSA key.

@end text="Full lesson on Learn"
The full lesson, with the extended algorithm, is on Learn.
