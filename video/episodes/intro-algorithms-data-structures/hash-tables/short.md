---
format: short
lesson: intro-algorithms-data-structures/hash-tables
title: Same load factor, four times slower
---

@art one-chain
Same table, same load factor, and searches get over four times slower.

@words text="20 keys, 8 slots: mean 2.3"
Twenty random keys in eight chained slots: a successful search examines two point three elements on average.

@math items="all multiples of 8, h(k) = k mod 8@multiple of eight;;all in slot 0: mean 10.5@slot zero"
Now make every key a multiple of eight, and hash with k mod eight. Every key lands in slot zero, and the mean jumps to ten and a half. The average assumed keys spread evenly.

@end text="Full lesson on Learn"
Measure your own chains in the full lesson on Learn.
