---
format: short
lesson: caching-and-hit-rates/cdn-egress-and-origin-load
title: Your CDN hit rate is not the one on your bill
---

@art two-profiles
Fifty eight percent of requests hit your CDN edge. Only twenty percent of the bytes do.

@words text="Popular objects are small"
On most edge workloads, the popular objects are the small ones. And a CDN bills you in bytes.

@math items="byte hit 20%  →  $24 000@the real byte hit rate;;request hit 57.91%  →  ≈ $12 628@the request rate"
At fifty thousand gigabytes a day, the real byte hit rate gives a twenty four thousand dollar month. Forecast from the request rate, and you'd budget barely half.

@end text="Full lesson on Learn"
The full lesson, with both profiles drawn, is on Learn.
