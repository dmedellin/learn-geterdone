---
format: short
lesson: queues-and-utilisation/the-knee
title: Why 99% busy means 100 times the wait
---

@art hyperbola
Your server is ninety nine percent busy. How long does a request take? A hundred times the work itself.

@math items="ρ = 1/2:  W = 2S@a half;;ρ = 9/10:  W = 10S@nine tenths;;ρ = 99/100:  W = 100S@ninety nine"
Response time is the service time over one minus rho. At a half, that's two service times. At nine tenths, ten. At ninety nine percent, a hundred.

@words text="W/S = 1/headroom"
Response time follows the headroom, not the load.

@end text="Full lesson on Learn"
The full lesson, with the curve to drag along, is on Learn.
