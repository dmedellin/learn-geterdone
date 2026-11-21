---
format: short
lesson: latency-and-the-tail/tail-amplification-under-fan-out
title: Every service hits its p99, and half your requests are slow
---

@art fan-out
Every backend meets its p ninety nine. So why are half your requests slow?

@math items="0.99⁶⁹ = 0.499837@sixty nine"
If a request waits for sixty nine independent calls, each inside its p ninety nine with probability nought point nine nine, then all of them are fast with probability nought point nine nine to the sixty nine. That's just under a half.

@words text="Your p99 just became your median"
At that fan out, the per call p ninety nine is the request's median.

@end text="Full lesson on Learn"
The full lesson, with the fan out on a slider, is on Learn.
