---
format: short
lesson: intractability-and-approximation/numbers-as-gadgets
title: Subset sum has a fast algorithm, and it's still hard
---

@art table-explodes
Subset sum has a dynamic programme. It's still NP hard. Both are true.

@words text="table size ∝ n × target"
The table has a column for every value up to the target. That's polynomial in the target's value.

@math items="target with d digits  ≈  10ᵈ columns@d digits"
But the input is the target's digits. A target with d digits has about ten to the d columns, which is exponential in the input. That's called weakly NP hard.

@end text="Full lesson on Learn"
The full lesson is on Learn.
