---
format: short
lesson: markov-chains-decisions-and-queues/finite-buffers-blocking-and-the-admitted-rate
title: The Little's Law mistake on every full queue
---

@art two-divisions
When a queue turns people away, the usual waiting time comes out too small.

@art admitted-split
A full buffer loses arrivals. So the rate that gets in is lambda times one minus the blocking probability, not lambda.

@math items="W = L / admitted ≈ 0.672@admitted rate;;L / λ ≈ 0.504@divide by lambda"
Divide L by the admitted rate, and you get about point six seven two. Divide by lambda, and about point five oh four, crediting customers who never got in.

@end text="Full lesson on Learn"
The full lesson, with the whole table, is on Learn.
