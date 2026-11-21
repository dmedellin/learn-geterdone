---
format: short
lesson: intro-algorithms-data-structures/hash-functions
title: Never hash with k mod 16
---

@art low-bits
Thirty seven, fifty three, sixty nine and eighty five. Hash them mod sixteen, and they all collide.

@words text="k mod 2ᵖ keeps only the low bits"
A power of two as the modulus just keeps the lowest bits of the key. Every higher bit is thrown away, so keys that share their low bits share a slot.

@art division-ring
So with the division method, the book's advice is a prime, not close to a power of two.

@end text="Full lesson on Learn"
See universal hashing in the full lesson on Learn.
