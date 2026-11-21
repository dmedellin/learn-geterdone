---
format: short
lesson: intro-algorithms-sorting/quicksort
title: A nine to one split is still n log n
---

@art lopsided-split
Split an array nine to one, every single time. Quicksort is still n log n.

@words text="Every level costs at most cn"
Each level of the recursion tree still costs at most c n in total.

@math items="depth = log₁₀/₉ n = Θ(lg n)@log base ten ninths"
And the longest path, always keeping the bigger side, ends after log base ten ninths of n levels. That's still theta of log n. What ruins quicksort is a split that leaves almost nothing on one side, level after level.

@end text="Full lesson on Learn"
Step through a partition in the full lesson on Learn.
