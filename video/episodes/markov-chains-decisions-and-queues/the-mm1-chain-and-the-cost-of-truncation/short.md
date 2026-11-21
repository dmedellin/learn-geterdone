---
format: short
lesson: markov-chains-decisions-and-queues/the-mm1-chain-and-the-cost-of-truncation
title: Sixty states, and the queue is still badly wrong
---

@art heavy-tail
Sixty states should be plenty for a queue model. At high load, it isn't.

@math items="L from the chain: 16.2@sixteen point two;;true L: 19@nineteen"
At nineteen twentieths loaded, cut the chain at sixty states and the mean comes out at about sixteen point two. The real answer is nineteen.

@words text="Lost tail: ρ⁶¹ ≈ 4.4%"
About four point four percent of the probability sits above state sixty, and that's where the mean lives.

@end text="Full lesson on Learn"
The full lesson, with the tail printed, is on Learn.
