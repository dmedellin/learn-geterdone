---
format: short
lesson: dynamic-programming/subsets-as-a-table-and-where-it-loses
title: The faster algorithm is slower until ten cities
---

@art crossing-late
The faster travelling salesman algorithm keeps losing, right up to nine cities.

@math items="n = 4:  256  vs  6@four cities;;n = 9:  41 472  vs  40 320@nine;;n = 10:  102 400  vs  362 880@ten"
Held Karp costs n squared times two to the n. Trying every order costs n minus one factorial. At four cities, two hundred and fifty six against six. At nine, still behind. At ten, it finally wins, and from there it pulls away for good.

@end text="Full lesson on Learn"
Check your own n on Learn.
