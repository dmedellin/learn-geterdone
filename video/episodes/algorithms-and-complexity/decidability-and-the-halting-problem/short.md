---
format: short
lesson: algorithms-and-complexity/decidability-and-the-halting-problem
title: The program that breaks every halting checker
---

@art oracle-box
Suppose a program could tell whether any program halts. Here's why it can't.

@list items="D asks H about P run on P@asks H|H says halts → loop forever@says halts|H says loops → halt@says loops"
Call it H. Build D, which takes a program P and asks H whether P halts on its own code. If H says halts, D loops forever. If H says loops, D halts.

@art mirror-loop
Now run D on itself. Whatever H predicts, D does the opposite. So H can't exist.

@end text="Full lesson on Learn"
The full lesson on the halting problem is on Learn.
