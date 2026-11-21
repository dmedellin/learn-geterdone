---
format: short
lesson: availability-and-failure/k-of-n-and-quorums
title: The config change that took a cluster from three nines to one
---

@art config-constant
One number in a config file took this cluster from three nines to one.

@math items="2-of-3:  99.97020%@two of three;;3-of-3:  97.0299%@all three"
Three replicas, each ninety nine percent. Writes needing two of three are available ninety nine point nine seven percent of the time. Change it to all three, and it's ninety seven point oh three.

@words text="2 h 36 min → 10 d 20 h a year"
That's two and a half hours of downtime a year becoming ten days. Same hardware.

@end text="Full lesson on Learn"
The full lesson, with n and k to set, is on Learn.
