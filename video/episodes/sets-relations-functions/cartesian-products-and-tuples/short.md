---
format: short
lesson: sets-relations-functions/cartesian-products-and-tuples
title: Why subsets and bit strings have the same count
---

@art subset-to-bits
A set with n elements has two to the n subsets. So do bit strings of length n. Why?

@words text="in or out → 1 or 0"
A subset makes one choice for each element: in, or out. Write in as one and out as zero, and the subset becomes a bit string.

@math items="P(A) ↔ {0, 1}ⁿ@every subset;;|P(A)| = 2ⁿ@two to the n"
Every subset gives exactly one bit string, and every bit string gives back exactly one subset. So they're counted by the same number, two to the n.

@end text="Full lesson on Learn"
The full lesson, with products you can count, is on Learn.
