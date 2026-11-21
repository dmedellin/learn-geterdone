---
format: short
lesson: queues-and-utilisation/memoryless-waiting
title: The bus is not due
---

@art bus-stop
You've waited three minutes for a bus. Is it more likely to come now?

@math items="P(T > s + t | T > s) = P(T > t)@already waited"
Not if arrivals are memoryless. The chance of waiting another t, given you've already waited s, is exactly the chance of waiting t from scratch. The time you've already spent cancels out.

@words text="Quiet time is not credit"
A process with no memory can't owe you anything.

@end text="Full lesson on Learn"
The full lesson, with the slot on a slider, is on Learn.
