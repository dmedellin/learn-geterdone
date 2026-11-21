---
format: short
lesson: queues-and-utilisation/token-buckets-and-rate-limiting
title: The rate limiter that let nine through at a limit of five
---

@art window-boundary
A limit of five a second. Nine got through in one second. How?

@math items="4 late in window 1@four late;;+ 5 at the reset@five more;;= 9 in one second@nine"
A fixed window counts to five and resets at each boundary. On this trace it admitted four late in the first window, then five more the instant the counter reset. That's nine inside one second.

@words text="Token bucket: at most b + r·t in any window"
A token bucket keeps its promise for every window.

@end text="Full lesson on Learn"
The full lesson, with both limiters on the same trace, is on Learn.
