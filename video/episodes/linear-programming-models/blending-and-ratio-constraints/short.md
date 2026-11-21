---
format: short
lesson: linear-programming-models/blending-and-ratio-constraints
title: The ratio you shouldn't multiply out
---

@art zero-denominator
Multiplying an inequality through by a variable can quietly change your model.

@math items="N ÷ B ≥ 2  →  N − 2B ≥ 0 ?@N minus two B;;(30, 70, 0) is feasible@thirty, seventy, zero;;30 ≥ 0 holds, N ÷ B is not a number@not a number"
Clear N over B at least two and you get N minus two B at least zero. But the blend thirty, seventy, zero is feasible. The cleared row holds there, and N over B is not a number.

@words text="Clear only when the denominator stays positive"
So clear a ratio only when the constraints keep its denominator strictly positive.

@end text="Full lesson on Learn"
The full lesson, with a blend that refutes the move, is on Learn.
