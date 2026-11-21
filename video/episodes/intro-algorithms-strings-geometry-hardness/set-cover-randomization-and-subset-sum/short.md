---
format: short
lesson: intro-algorithms-strings-geometry-hardness/set-cover-randomization-and-subset-sum
title: Flip a coin for every variable, satisfy seven eighths
---

@art coin-flips
Flip a coin per variable, and seven eighths of the clauses hold, on average.

@math items="P(clause fails) = (1/2)³ = 1/8@one eighth;;expected satisfied: 7/8@seven eighths of"
A clause of three distinct literals fails only if all three come out false. That's one half cubed, one eighth. So by linearity of expectation, seven eighths of the clauses hold.

@words text="Expected ratio ≤ 8/7"
That's an average over the coin flips. A single run can do worse.

@end text="Full lesson on Learn"
See all three guarantees in the full lesson on Learn.
