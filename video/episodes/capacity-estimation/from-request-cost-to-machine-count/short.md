---
format: short
lesson: capacity-estimation/from-request-cost-to-machine-count
title: Why your fleet is 167 machines, not 100
---

@art staircase-ceiling
Twenty thousand requests a second, two hundred per machine. A hundred machines? Not if you want it to stay fast.

@math items="⌈20 000 / 200⌉ = 100@a hundred percent;;⌈20 000 / 120⌉ = 167@sixty percent"
At a hundred percent utilisation you'd need a hundred. At a sixty percent target, each machine is allowed a hundred and twenty, so you need a hundred and sixty seven.

@words text="67 machines = the latency you asked for"
Those sixty seven machines aren't waste. They keep you off the steep part of the queueing curve.

@end text="Full lesson on Learn"
The full lesson, with the target on a slider, is on Learn.
