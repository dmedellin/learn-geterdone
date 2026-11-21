---
format: short
lesson: availability-and-failure/load-shedding-and-circuit-breakers
title: Turning away 55 percent of traffic serves more users
---

@art door-cap
Twice the traffic your service can handle. Turn away more than half of it.

@math items="accept all:  1000²/2000 = 500/s@accept everything;;shed at 900:  900/s@shed at nine hundred"
A thousand a second service that tries to accept everything finishes only five hundred in time. Shed at nine hundred, and all nine hundred are served.

@words text="1.8× the users, fewer failures"
Saying no serves one point eight times as many users, and the rejections are instant, not timeouts.

@end text="Full lesson on Learn"
The full lesson, with the threshold to move, is on Learn.
