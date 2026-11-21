---
format: short
lesson: intro-algorithms-advanced-structures/van-emde-boas-trees
title: One extra call per level turns lg lg u into lg u
---

@art two-calls
Same tree shape, same keys, and one structure makes eight times the calls.

@math items="T(u) = T(√u) + O(1) → O(lg lg u)@one call;;T(u) = 2T(√u) + O(1) → Θ(lg u)@two calls"
Split each key into a cluster and a position, and recurse into a universe of root u. With one call a level you get log log u. With two calls a level, it's log u.

@art min-kept-out
The van Emde Boas tree's fix is a min and max at every level, so each operation recurses only once.

@end text="Full lesson on Learn"
Race both structures in the full lesson on Learn.
