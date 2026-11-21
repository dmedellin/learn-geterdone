---
format: short
lesson: scheduling/the-job-shop-and-disjunctive-orientations
title: Four sensible scheduling choices that can never run
---

@art deadlock-cycle
Every choice is reasonable on its own. Together, nothing can start.

@words text="J2 first on M1 · J1 first on M2"
Two jobs, two machines, opposite routes. Put job two first on machine one, and job one first on machine two.

@words text="Each waits for the next, in a circle"
Now job one waits for job two, which waits for itself on the other machine, which waits for job one. It's a deadlock, and it's a real answer, not an error.

@end text="Full lesson on Learn"
The full lesson, with every orientation scored, is on Learn.
