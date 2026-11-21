---
format: short
lesson: sorting-and-selection/quicksort-and-its-worst-case
title: Median of three has its own killer input
---

@art adversary
Median of three makes quicksort safe? There's an input built just to beat it.

@words text="answer every comparison adversarially"
Run the rule on values not yet decided, and answer each comparison so the pivot keeps landing near the bottom. What comes out is a real permutation.

@math items="n = 32:  304 comparisons@thirty two keys;;n log₂ n = 160@n log n"
At thirty two keys, quicksort spends three hundred and four comparisons on it, where n log n is a hundred and sixty.

@end text="Full lesson on Learn"
The full lesson, with a killer for every rule, is on Learn.
