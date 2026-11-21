---
format: short
lesson: queues-and-utilisation/arrival-rate-service-rate-utilisation
title: The service takes 2 ms, so mu is 500
---

@art slower-dependency
A service takes two milliseconds. What's its service rate? Not two.

@math items="μ = 1/S = 1/0.002 s = 500/s@five hundred;;800/s → ρ = 8/5@eight hundred"
Mu is one over the service time. Two milliseconds is two thousandths of a second, so mu is five hundred a second. Send eight hundred a second at it and rho is eight fifths.

@words text="ρ ≥ 1: the backlog grows at λ − μ"
Above one, the backlog just grows, by three hundred every second.

@end text="Full lesson on Learn"
The full lesson, with rho on a dial, is on Learn.
