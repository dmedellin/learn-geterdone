---
format: short
lesson: scaling-laws-and-cost/autoscaling-lag
title: Autoscaling is always one boot window behind
---

@art lagging-lines
Your autoscaler is always ninety seconds behind. That costs over a million requests.

@math items="gap = r·τ = 50 × 90 = 4 500 rps@four thousand five hundred;;shortfall = r·τ·(D − τ/2) = 1 147 500@one million"
Demand climbs at fifty requests a second per second, and new instances take ninety seconds to boot. So the fleet runs four thousand five hundred requests a second short, the whole ramp. Over five minutes, one million one hundred and forty seven thousand five hundred requests.

@words text="Hold r·τ warm, and it's zero"
A warm reserve of exactly that gap removes it.

@end text="Full lesson on Learn"
The full lesson, with the boot time on a slider, is on Learn.
