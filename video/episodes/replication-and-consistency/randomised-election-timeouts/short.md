---
format: short
lesson: replication-and-consistency/randomised-election-timeouts
title: A fixed election timeout elects a leader with probability zero
---

@art identical-retry
Give every node the same election timeout, and your cluster will never elect a leader.

@math items="T = 1:  P(clean) = 5 · 1 · 0⁴ = 0@one timeout value;;T = 10:  P(clean) = 76.665%@ten slots"
With one timeout value, all five candidates stand at once, every time. Exactly zero clean rounds. Randomise over ten slots, and three rounds in four elect a leader.

@words text="1.3044 rounds on average"
That's about one point three rounds on average, instead of forever.

@end text="Full lesson on Learn"
The full lesson, with every term of the sum, is on Learn.
