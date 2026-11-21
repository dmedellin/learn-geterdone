---
format: short
lesson: scheduling/shortest-processing-time-and-the-adjacent-exchange
title: The one subtraction that proves shortest-job-first
---

@art adjacent-swap
Why does running the shortest job first work? One swap tells you.

@math items="change in Σ C = p_b − p_a@p b minus p a"
Swap two neighbouring jobs, a then b. Only their two finish times move, and the total changes by exactly p b minus p a.

@words text="Shorter behind? Swap and improve."
So if a shorter job sits behind a longer one, swapping them always helps. The only order nothing improves is shortest first.

@end text="Full lesson on Learn"
The full lesson, with ten swaps to watch, is on Learn.
