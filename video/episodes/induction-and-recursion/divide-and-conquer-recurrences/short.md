---
format: short
lesson: induction-and-recursion/divide-and-conquer-recurrences
title: One fewer multiplication changes the exponent
---

@art four-vs-three
Multiply big numbers by splitting them in half, and you need four smaller products.

@words text="4T(n/2) + n  →  Θ(n²)"
Four half size products gives n squared, no better than schoolbook multiplication.

@words text="3T(n/2) + n  →  Θ(n^1.585)"
Karatsuba's trick needs only three. Log base two of three is about one point five eight five, so the cost drops to n to the one point five eight five.

@end text="Full lesson on Learn"
The full lesson, with the master theorem, is on Learn.
