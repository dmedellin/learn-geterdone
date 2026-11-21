---
format: short
lesson: dynamic-programming-and-sequential-decisions/value-iteration-and-the-fixed-point
title: Value iteration never actually arrives
---

@art iterates-approach
Twelve steps of value iteration, and it still hasn't reached the answer.

@math items="exact: 22/7@twenty two sevenths;;12 steps: 6746787645/2147483648@twelve steps"
The exact value is twenty two sevenths. After twelve steps, value iteration is at a fraction with a ten digit denominator, and it will never land on it.

@words text="(I − γP) v = r"
Row reduction on this small linear system gets the exact answer in four operations.

@end text="Full lesson on Learn"
The full lesson, with the exact solve and its check, is on Learn.
