---
format: short
lesson: capacity-estimation/latency-numbers-on-a-log-scale
title: One disk seek is a hundred thousand memory reads
---

@art log-ruler
Disk is somewhat slower than memory? Try a hundred thousand times slower.

@math items="10 000 000 ns ÷ 100 ns = 100 000@ten million"
A disk seek is about ten million nanoseconds. A memory reference is about a hundred. Ten million over a hundred is a hundred thousand.

@words text="1 second of memory → more than a day of disk"
If a memory reference took a second, one disk seek would take more than a day. That's why an index is worth building.

@end text="Full lesson on Learn"
The full lesson, with the whole ladder on a log ruler, is on Learn.
