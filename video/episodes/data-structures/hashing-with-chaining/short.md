---
format: short
lesson: data-structures/hashing-with-chaining
title: Same load factor, five times slower
---

@art one-long-chain
Same table, same load factor, and searches get five times slower.

@math items="m = 8,  n = 20,  α = 5/2@eight slots;;random keys:  2.3 probes@random keys;;keys 8, 16, … 160:  10.5 probes@multiples of eight"
Eight slots, twenty keys, alpha five halves. Random keys cost two point three probes. But multiples of eight all land in slot zero, and cost ten and a half.

@words text="Θ(1 + α) expected · Θ(n) worst"
A hash lookup is constant on average, under an assumption about the keys. The worst case is linear.

@end text="Full lesson on Learn"
The full lesson, with a key set to break the table, is on Learn.
