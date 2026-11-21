---
format: short
lesson: latency-and-the-tail/percentiles-do-not-add
title: You can't add two p99s
---

@art two-stages
Thirty eight milliseconds plus seventy two milliseconds. Is that the p ninety nine? No.

@math items="p99(A) + p99(B) = 110 ms@a hundred and ten;;p99(A + B) = 78 ms@seventy eight"
Add the two stage p ninety nines and you get a hundred and ten. Convolve the two distributions and the real p ninety nine is seventy eight, forty one percent lower.

@words text="p95: naive 48 ms, true 52 ms"
And at the p ninety five, the naive sum is too low. Means add. Percentiles don't.

@end text="Full lesson on Learn"
The full lesson, with the convolution worked out, is on Learn.
