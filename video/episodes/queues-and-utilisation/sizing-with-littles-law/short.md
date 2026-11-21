---
format: short
lesson: queues-and-utilisation/sizing-with-littles-law
title: Your database got slower, and your throughput halved
---

@art slower-database
The database got slower. Why did your throughput halve?

@math items="20 connections ÷ 0.04 s = 500/s@forty milliseconds;;20 connections ÷ 0.08 s = 250/s@eighty"
A pool of twenty connections, each held for forty milliseconds, can start five hundred requests a second. Let the database slow to eighty milliseconds, and the same pool caps at two hundred and fifty.

@words text="A pool is a throughput ceiling: N/W"
A pool's ceiling is N over W. When W moves, so does your throughput.

@end text="Full lesson on Learn"
The full lesson, with the pool to size, is on Learn.
