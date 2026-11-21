---
format: short
lesson: number-theory-and-cryptography/rsa-encryption
title: Breaking an RSA key takes one division
---

@words text="Public key: (143, 7)"
This RSA public key can be broken with a single division.

@math items="143 = 11 · 13@a hundred and forty three;;φ(n) = 10 · 12 = 120@phi of n;;d = 7⁻¹ mod 120 = 103@so d"
A hundred and forty three is eleven times thirteen. Then phi of n is ten times twelve, a hundred and twenty. So d is the inverse of seven mod a hundred and twenty, which is a hundred and three.

@art split-hard
At two thousand and forty eight bits, the method's the same. Only the time the factoring takes changes.

@end text="Full lesson on Learn"
The full lesson, with a key you can break, is on Learn.
