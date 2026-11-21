---
format: short
lesson: latency-and-the-tail/timeouts-and-retries-in-the-budget
title: The timeout that kills 15% of good calls
---

@art mean-timeout
Setting your timeout at the average latency? You might be killing fifteen percent of good calls.

@math items="mean = 18.27 ms@eighteen point two seven;;T = 18 ms kills 15%@fifteen percent;;T = 90 ms kills 1%@ninety"
On this service the mean is eighteen point two seven milliseconds. A timeout at eighteen abandons fifteen percent of calls that were going to succeed. A timeout at ninety, the p ninety nine, abandons one percent.

@words text="Put timeouts in the gaps, not at the mean"

Look at the distribution, and put the timeout where it's sparse.

@end text="Full lesson on Learn"
The full lesson, with the timeout on a slider, is on Learn.
