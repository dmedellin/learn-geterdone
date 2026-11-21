---
format: short
lesson: caching-and-hit-rates/average-latency-under-a-cache
title: Your cache's mean latency is a number no request takes
---

@art two-clusters
Your cached endpoint averages two point nine five milliseconds. Not one request takes that long.

@math items="(19/20)(1) + (1/20)(40) = 2.95 ms@nineteen twentieths"
Hits take one millisecond, misses take forty, and ninety five percent hit. Nineteen twentieths times one plus one twentieth times forty is two point nine five.

@words text="Every request: 1 ms or 40 ms" sub="p99 = 40 ms"
But every request takes one or forty. And because more than one in a hundred misses, the p ninety nine is forty.

@end text="Full lesson on Learn"
The full lesson, with the percentile staircase, is on Learn.
