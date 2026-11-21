---
format: short
lesson: strings-and-pattern-matching/choosing-a-modulus
title: A bigger hash modulus isn't always safer
---

@art prime-strip
A bigger hash modulus isn't always safer. Here's a text that proves it.

@words text="41 ✗ · 43 ✓ · 47 ✗"
Sweep the primes under two hundred on a single Rabin Karp search. Forty one collides, forty three doesn't, forty seven does.

@words text="q divides a fixed difference"
A collision happens when the modulus divides a fixed difference, and that has nothing to do with size. The real safety comes from picking the modulus at random.

@end text="Full lesson on Learn"
Sweep it on Learn.
