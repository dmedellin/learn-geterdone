---
format: short
lesson: intro-algorithms-advanced-structures/disjoint-sets
title: The function that never gets past four
---

@art forest
A function so slow it never gets past four, for any real input.

@art path-compression
Keep disjoint sets as trees. Hang the lower ranked root under the higher, and make every find point its path straight at the root.

@math items="O(m α(n))@times alpha;;α(n) ≤ 4 in practice@at most four"
Then m operations cost O of m times alpha of n. Alpha grows so slowly that it's at most four for every n that could ever occur.

@end text="Full lesson on Learn"
Switch each rule on and off in the full lesson on Learn.
