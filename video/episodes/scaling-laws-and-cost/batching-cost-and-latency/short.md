---
format: short
lesson: scaling-laws-and-cost/batching-cost-and-latency
title: Bigger batches are always cheaper. That's the problem.
---

@art hyperbola-floor
Bigger batches are always cheaper. So the cost curve can never tell you when to stop.

@math items="B = 100:  120 µ$,  first item waits 198 ms@a hundred;;B = 800:  102.5 µ$,  first item waits 1.6 s@eight hundred"
At a hundred items a batch, each costs a hundred and twenty micro dollars and the first waits a hundred and ninety eight milliseconds. At eight hundred, you save a little more, and the first waits one point six seconds.

@words text="Cost falls to a floor. Wait rises forever."
So the wait has to choose.

@end text="Full lesson on Learn"
The full lesson, with both curves, is on Learn.
