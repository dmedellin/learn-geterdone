---
format: short
lesson: caching-and-hit-rates/ttl-and-staleness
title: Shorter TTL, fresher data, and ten times the backend reads
---

@art seesaw
Cut your cache TTL from ten seconds to one. What did that just cost you?

@math items="T = 10 s:  stale 1/12 · miss 1/50@ten seconds;;T = 1 s:  stale 1/120 · miss 1/5@one second"
A value changes once a minute, read five times a second. At ten seconds, it's stale a twelfth of the time and misses one in fifty. At one second, a hundred and twentieth stale, but one in five misses.

@words text="Staleness ÷ 10 · backend × 10"
A tenth of the staleness, for ten times the backend reads.

@end text="Full lesson on Learn"
The full lesson, with the TTL to drag, is on Learn.
