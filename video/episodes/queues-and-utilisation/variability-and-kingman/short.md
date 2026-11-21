---
format: short
lesson: queues-and-utilisation/variability-and-kingman
title: Same mean, half the wait
---

@art halved-wait
Same server, same load, same average job. Half the waiting. How?

@math items="random service:  (4)(1)(2) = 8@random;;fixed service:  (4)(1/2)(2) = 4@same length"
Kingman's approximation multiplies utilisation, variability and the service time. At four fifths busy and two slots of work, random service waits eight. Make every job the same length, and the variability factor halves, so the wait is four.

@words text="W_q ≈ utilisation × variability × S"
Variability is a lever, and pulling it buys no extra machines.

@end text="Full lesson on Learn"
The full lesson, with both coefficients on sliders, is on Learn.
