---
format: short
lesson: induction-and-recursion/recurrence-relations
title: Fibonacci hiding in binary strings
---

@art bead-rows
How many binary strings have no two ones in a row? Fibonacci knows.

@math items="ends in 0  →  aₙ₋₁@ends in zero;;ends in 01  →  aₙ₋₂@ends in zero one;;aₙ = aₙ₋₁ + aₙ₋₂@add them"
A valid string either ends in zero, after any valid string one shorter, or ends in zero one, after any valid string two shorter. Add them, and you get Fibonacci's rule.

@words text="2, 3, 5, 8, 13, 21, 34"
Starting from two and three, the counts run two, three, five, eight, thirteen, twenty one, thirty four.

@end text="Full lesson on Learn"
The full lesson on recurrence relations is on Learn.
