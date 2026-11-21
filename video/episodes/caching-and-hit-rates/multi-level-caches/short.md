---
format: short
lesson: caching-and-hit-rates/multi-level-caches
title: Your L2 cache is not serving half your traffic
---

@art population-swap
Your dashboard says your second cache hits fifty percent. It's serving a tenth of your traffic.

@math items="L2 sees only the L1 misses: 1/5@the misses;;L2 serves (1/5)(1/2) = 1/10@a fifth times a half"
If level one hits eighty percent, level two only sees the misses, a fifth of all requests. Half of those is a fifth times a half, a tenth.

@words text="Ask which requests a rate was measured on"
Before trusting any cache statistic, ask which requests it was measured on.

@end text="Full lesson on Learn"
The full lesson, with every branch counted, is on Learn.
