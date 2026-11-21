---
format: short
lesson: enterprise-patterns-distribution/remote-facade
title: A Remote Facade removes waits, not work
---

@art chatty-client
Eleven remote calls, and nearly ninety eight percent of the time is waiting.

@math items="fine-grained: 11 trips, 225.50 ms@eleven round trips;;facade: 2 trips, 45.50 ms@two"
At twenty milliseconds of latency, a fine grained client makes eleven round trips and takes two hundred and twenty five point five milliseconds. Through a facade, two trips: forty five point five.

@words text="Same work. Fewer waits."
The facade does the same work behind it. It just stops paying the network for every small call.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the waits, is on Learn.
