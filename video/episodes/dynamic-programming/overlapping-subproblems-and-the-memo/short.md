---
format: short
lesson: dynamic-programming/overlapping-subproblems-and-the-memo
title: From 22,089 calls to 50
---

@art repeated-subtrees
One recursion makes twenty two thousand calls. It only needed fifty.

@words text="coins 1, 2, 5 · amount 18" sub="only 18 distinct questions"
Fewest coins for eighteen, from ones, twos and fives, has just eighteen distinct subproblems. The plain recursion keeps asking them again.

@words text="22 089 → 50 calls"
Write each answer down the first time, and every repeat becomes a lookup. Twenty two thousand and eighty nine calls fall to fifty.

@end text="Full lesson on Learn"
Count them yourself on Learn.
