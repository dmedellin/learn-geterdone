---
format: short
lesson: randomised-algorithms/the-probabilistic-method
title: Proving an answer exists without ever finding it
---

@art eight-cube
Flip a coin for every variable. Each three-literal clause survives seven times in eight.

@math items="E[satisfied] = 7m/8@seven m over eight"
Exactly one of the eight settings of a clause's three variables makes it false. So by linearity, a random assignment satisfies seven m over eight clauses on average.

@words text="Some assignment beats the average"
A value can't always fall below its own average. So an assignment satisfying at least that many must exist, even though we never found it.

@end text="Full lesson on Learn"
The full lesson is on Learn.
