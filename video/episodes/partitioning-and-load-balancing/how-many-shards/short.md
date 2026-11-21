---
format: short
lesson: partitioning-and-load-balancing/how-many-shards
title: The shard count that's three times too small
---

@art three-copies
Forty eight terabytes on four terabyte nodes. Twelve shards, right?

@math items="48 TB × 3 = 144 TB@three copies;;⌈144 / 4⌉ = 36 shards@thirty six"
Not if you keep three copies. The bytes that have to fit are a hundred and forty four terabytes, and that needs thirty six shards.

@words text="Size the bytes that exist: D · RF"
Twelve would be a fleet a third the size, sized against a number that never existed on any disk.

@end text="Full lesson on Learn"
The full lesson, with both constraints on sliders, is on Learn.
