---
format: short
lesson: enterprise-patterns-distribution/distribution-strategies
title: Split by class, and it's a thousand times slower
---

@art by-class-nodes
Give each kind of object its own server. What happens to your calls?

@math items="75 calls × 1,000 µs = 75,000 µs@seventy five calls;;one process: 75 µs@one process"
In the lesson's design, seventy five calls each cross the network, at an illustrative thousand microseconds. That's seventy five thousand. In one process, it's seventy five.

@words text="Don't distribute your objects!"
That's Fowler's First Law. Keep the application together, and run copies of the whole thing instead.

@end text="Full lesson on Learn"
The full lesson, with a lab that prices the calls, is on Learn.
