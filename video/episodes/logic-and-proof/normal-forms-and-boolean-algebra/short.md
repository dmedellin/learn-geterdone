---
format: short
lesson: logic-and-proof/normal-forms-and-boolean-algebra
title: One logic gate can build them all
---

@art nand-bricks
You could build an entire computer chip from just one kind of logic gate.

@math items="¬p ≡ p ↑ p@not p;;p ∧ q ≡ (p ↑ q) ↑ (p ↑ q)@p and q"
The gate is NAND, not of p and q. Not p is p NAND p. And p and q is p NAND q, NAND, p NAND q.

@words text="NAND alone is functionally complete"
With not and and, you can express every truth function. So NAND alone can express everything.

@end text="Full lesson on Learn"
The full lesson, with normal forms to check, is on Learn.
