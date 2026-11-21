---
format: short
lesson: replication-and-consistency/vector-clocks-and-concurrency
title: Concurrent doesn't mean simultaneous
---

@art wall-clock
These two events could be minutes apart. They're still concurrent.

@math items="A3 = (3,0,0) · C3 = (2,3,3)@three zero zero;;3 ≤ 2 no · 3 ≤ 0 no  →  concurrent@neither"
A three's vector is three, zero, zero. C three's is two, three, three. Neither is at most the other in every component. So neither could have known about the other.

@words text="Concurrent = no chain of messages"
Concurrent means no chain of messages connects them. That's exactly when two updates conflict.

@end text="Full lesson on Learn"
The full lesson, with a diagram to stamp, is on Learn.
