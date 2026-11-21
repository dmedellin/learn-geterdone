---
format: short
lesson: induction-and-recursion/solving-linear-recurrences
title: Why a repeated root needs an extra n
---

@art merged-curves
Solve a recurrence with a repeated root the usual way, and it breaks.

@words text="aₙ = 4aₙ₋₁ − 4aₙ₋₂,  a₀ = 1,  a₁ = 4"
The characteristic equation is r minus two, squared. So you try A times two to the n, plus B times two to the n.

@words text="C·2ⁿ:  a₀ needs C = 1,  a₁ needs C = 2"
But that's just one constant. a nought needs it to be one, and a one needs it to be two.

@math items="aₙ = (A + Bn)·2ⁿ = (n + 1)·2ⁿ@times n"
The fix is a second solution, times n. That gives n plus one, times two to the n.

@end text="Full lesson on Learn"
The full lesson is on Learn.
