---
format: short
lesson: enterprise-patterns-data-source/database-connections
title: Batching statements saves waits, not work
---

@art batch-trip
Batching makes saves faster, and the database does no less work.

@math items="25 one at a time: 62.50 ms, 80% waiting@twenty five statements;;3 batches: 18.50 ms@three batches"
Twenty five statements sent one at a time, with a two millisecond wait each, take sixty two and a half milliseconds, eighty percent of it waiting. In three batches: eighteen and a half.

@words text="Short waits, small saving"
On the same machine, the saving shrinks to about one point two times. Measure yours.

@end text="Full lesson on Learn"
The full lesson, with a lab for batching, is on Learn.
