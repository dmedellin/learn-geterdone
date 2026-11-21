---
format: short
lesson: intractability-and-approximation/decision-search-and-the-certificate
title: How a yes-or-no machine can hand you the answer
---

@art fix-variable
A machine that only says yes or no can still find you the answer.

@words text="fix x₁ = true, ask again"
Fix the first variable to true and ask if the formula is still satisfiable. If yes, keep it. If no, every solution has it false.

@math items="n + 1 questions@n plus one;;3 variables: 4 calls@four calls"
One question settles one variable. So n plus one questions write out a full assignment, four calls for three variables.

@end text="Full lesson on Learn"
The full lesson is on Learn.
