---
format: short
lesson: partitioning-and-load-balancing/local-vs-global-secondary-indexes
title: Local vs global index in one division
---

@art cost-lines
Local or global secondary index? One division decides it.

@math items="local = r·N + w@r times N;;global = r + 2w@r plus two w;;equal when r/w = 1/(N − 1)@one over N minus one"
A local index makes every read ask all N shards, so it costs r times N plus w. A global index doubles every write, r plus two w. They're equal at one over N minus one.

@words text="16 shards: crossover 1/15"
At sixteen shards, one indexed read per fifteen writes already favours global.

@end text="Full lesson on Learn"
The full lesson, with the crossover on sliders, is on Learn.
