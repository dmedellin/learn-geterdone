---
format: short
lesson: integer-programming/binary-variables-and-logical-constraints
title: The if-then constraint that says the opposite
---

@art if-then-arrow
If A then B. Swap two letters, and your model allows the one thing you meant to forbid.

@math items="y_A − y_B ≤ 0  ✓@right;;y_B − y_A ≤ 0  ✗@converse"
The right encoding is y A minus y B, at most zero. The converse, y B minus y A, at most zero, looks just as tidy.

@art refuting-row
But at A one, B zero, the condition fails and the converse holds. One row refutes it. Check every row.

@end text="Full lesson on Learn"
The full lesson, with a truth table for every encoding, is on Learn.
