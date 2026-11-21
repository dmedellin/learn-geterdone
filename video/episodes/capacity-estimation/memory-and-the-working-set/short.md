---
format: short
lesson: capacity-estimation/memory-and-the-working-set
title: The last five points of cache hit rate cost the most
---

@art knee-curve
Ninety percent cache hits cost half a terabyte. Ninety five percent costs over five times as much.

@math items="90%: 500 GB@ninety percent;;95%: 2.75 TB@ninety five"
Five terabytes of data, with a tenth of it taking ninety percent of the reads. Cache that hot tenth, five hundred gigabytes, and you get ninety percent hits. For ninety five percent, you need two point seven five terabytes.

@words text="Past the knee, every gigabyte buys far less"
Past the knee, each gigabyte buys a ninth as much.

@end text="Full lesson on Learn"
The full lesson, with the knee on a slider, is on Learn.
