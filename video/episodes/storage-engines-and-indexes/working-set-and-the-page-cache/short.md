---
format: short
lesson: storage-engines-and-indexes/working-set-and-the-page-cache
title: 13% of your data serves 89% of your reads
---

@art miss-trickle
Your data is on disk. So every read is a disk read? Not even close.

@math items="64 GB of 500 GB = 12.80% of pages@twelve point eight;;s = 1:  h ≈ 88.905%@eighty eight point nine"
Sixty four gigabytes of page cache over five hundred gigabytes of data is twelve point eight percent of the pages. With skewed popularity, it serves about eighty eight point nine percent of the reads.

@words text="Skew is the reason the cache exists"
With uniform popularity, it would serve only twelve point eight.

@end text="Full lesson on Learn"
The full lesson, with memory on a slider, is on Learn.
