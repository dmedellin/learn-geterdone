---
format: short
lesson: latency-and-the-tail/hedged-requests
title: Cut your p99 by 62% with five percent more load
---

@art hedge-timeline
What if a second copy of a slow request could cut your p ninety nine by sixty two percent?

@math items="hedge at the p95, 30 ms@thirty milliseconds;;extra load +5.0%@five percent;;p99: 120 ms → 45 ms@forty five"
If a call hasn't answered by thirty milliseconds, its p ninety five, send a second copy and take the first answer. Only five percent of requests trigger it. The p ninety nine falls from a hundred and twenty to forty five.

@words text="Only if the copies are independent"
That only works if the second copy is independent, so send it to a different replica.

@end text="Full lesson on Learn"
The full lesson, with the delay on a slider, is on Learn.
