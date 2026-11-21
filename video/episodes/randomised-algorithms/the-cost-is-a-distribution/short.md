---
format: short
lesson: randomised-algorithms/the-cost-is-a-distribution
title: The average cost isn't the typical cost
---

@art distribution-bars
Randomised quicksort on eight keys expects about seventeen comparisons. Sixteen is likelier.

@math items="E[C] = 2369/140 ≈ 16.92@the expectation;;most likely: C = 16@sixteen;;P(17) < ⅕ · P(16)@seventeen"
The expectation is two three six nine over one forty, about sixteen point nine two. But the most likely count is sixteen, and seventeen has less than a fifth of its probability.

@words text="Look at the bars first"
The expectation summarises a lumpy shape. It doesn't describe a typical run.

@end text="Full lesson on Learn"
The full lesson is on Learn.
