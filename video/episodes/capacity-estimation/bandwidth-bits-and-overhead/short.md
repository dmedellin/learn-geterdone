---
format: short
lesson: capacity-estimation/bandwidth-bits-and-overhead
title: When your headers are half your traffic
---

@art crossover-point
When is most of your bandwidth not your data?

@math items="h/(p + h) ≥ 1/2@at least half;;h ≥ p@exactly when"
Headers are charged once per request. They're at least half the bytes on the wire exactly when the payload is no bigger than the header.

@words text="200 B headers: 200 B payload is half, 50 B is 4/5"
With two hundred bytes of headers, a two hundred byte payload is half overhead. At fifty bytes, it's four fifths.

@end text="Full lesson on Learn"
The full lesson, with the payload on a slider, is on Learn.
