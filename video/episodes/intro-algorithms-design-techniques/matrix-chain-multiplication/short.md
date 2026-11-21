---
format: short
lesson: intro-algorithms-design-techniques/matrix-chain-multiplication
title: Same matrices, 102 or 240 multiplications
---

@art two-orders
Same four matrices, same answer. A hundred and two multiplications, or two hundred and forty.

@math items="((A₁A₂)(A₃A₄)): 102@a hundred and two;;(A₁((A₂A₃)A₄)): 240@two hundred and forty"
With dimensions three, five, two, six, four, pairing the left two and the right two costs a hundred and two. Another bracketing costs two hundred and forty.

@words text="Associative product, different cost"
Every bracketing gives the same product. Dynamic programming finds the cheap one.

@end text="Full lesson on Learn"
Fill the table yourself in the full lesson on Learn.
