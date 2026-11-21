---
format: short
lesson: caching-and-hit-rates/cache-stampedes
title: Why a 99.9 percent hit rate cache can still flatten your database
---

@art expiry-gap
When a hot key expires, for a hundred milliseconds you have no cache at all.

@math items="5 000/s × 0.1 s = 500 requests@five thousand"
At five thousand reads a second and a hundred millisecond refill, five thousand times point one is five hundred requests, all for the same value, at the same moment.

@art single-flight
Single flight coalescing sends one of them to the backend and parks the rest on its answer. Five hundred becomes one.

@end text="Full lesson on Learn"
The full lesson, with the burst drawn against capacity, is on Learn.
