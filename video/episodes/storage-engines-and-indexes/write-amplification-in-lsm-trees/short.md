---
format: short
lesson: storage-engines-and-indexes/write-amplification-in-lsm-trees
title: Fifty megabytes in, 1.25 gigabytes to disk
---

@art bandwidth-pipes
Your database ingests fifty megabytes a second. The disk sees twenty five times that.

@math items="WA ≈ L · F/2 = 5 × 5 = 25@twenty five;;25 × 50 MB/s = 1.25 GB/s@one point two five"
In a levelled LSM tree, each of five levels rewrites a byte about five times as it compacts. That's twenty five times, so one point two five gigabytes a second of sustained writes.

@words text="Append-only means sequential. Not few."
Size the disk to the ingest, and compaction falls behind.

@end text="Full lesson on Learn"
The full lesson, with the fanout on a slider, is on Learn.
