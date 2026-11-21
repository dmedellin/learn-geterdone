---
format: short
lesson: queues-and-utilisation/bounded-queues-and-loss
title: The response time that's 12% too good
---

@art dropped-arrivals
Your queue drops one request in eight. Your response time is probably wrong too.

@math items="W = L/λ ≈ 1.95 s  ✗@offered rate;;W = L/λ_eff ≈ 2.22 s  ✓@admitted rate"
With room for four at four fifths load, about twelve percent of arrivals are blocked. Divide by the offered rate and you get one point nine five seconds. Divide by the admitted rate and it's two point two two.

@words text="Little's Law counts only who got in"
Dropped arrivals never entered, so they don't count.

@end text="Full lesson on Learn"
The full lesson, with the buffer size on a slider, is on Learn.
