---
format: short
lesson: intro-algorithms-algebraic-topics/solving-linear-systems
title: An invertible matrix that elimination can't handle
---

@art pivot-swap
This matrix is invertible, and plain Gaussian elimination still fails on it.

@math items="[[0, 2], [3, 1]]@zero in the corner;;det = −6@minus six"
It has a zero in the corner, so the first step would divide by zero. Yet its determinant is minus six. It's perfectly invertible.

@words text="Swap up the largest entry"
The fix is one row exchange. Before each step, bring up the entry of largest absolute value in the column.

@end text="Full lesson on Learn"
Decompose it exactly in the full lesson on Learn.
