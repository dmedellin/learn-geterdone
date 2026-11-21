---
format: short
lesson: simulation-and-variance-reduction/warm-up-and-the-initial-transient
title: A thousand runs, all aimed at the wrong number
---

@art biased-cluster
A thousand simulation runs won't fix this error. They'll just make it look convincing.

@words text="Started empty ⇒ biased"
Start a queue empty, and the early slots drag every average down. That's bias, and replications don't shrink it.

@math items="from slot 0:  2.2443@from slot zero;;discard 100:  2.3717@Throw away;;truth:  2.4@the truth"
Averaged from slot zero, the run is aimed at two point two four. Throw away the first hundred slots, and it's aimed at two point three seven. The truth is two point four.

@end text="Full lesson on Learn"
The full lesson, with the exact transient, is on Learn.
