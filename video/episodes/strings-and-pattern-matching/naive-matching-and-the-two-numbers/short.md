---
format: short
lesson: strings-and-pattern-matching/naive-matching-and-the-two-numbers
title: Why naive string search is usually fast
---

@art english-vs-uniform
The slowest string matcher is usually fast, and the reason fits in one fraction.

@words text="most alignments fail at once"
Slide a pattern along a text. At most offsets, the very first character already disagrees, so you stop after one comparison.

@math items="expected per alignment = σ/(σ − 1)@sigma over sigma minus one"
With sigma equally likely letters, the expected cost per alignment is sigma over sigma minus one. The pattern's length isn't even in it.

@end text="Full lesson on Learn"
Count it yourself on Learn.
