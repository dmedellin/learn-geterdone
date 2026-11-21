---
format: short
lesson: intro-algorithms-foundations/analyzing-insertion-sort
title: Same algorithm, same size, 36 or 120 steps
---

@art best-worst
Same algorithm, same eight keys: thirty six steps, or a hundred and twenty.

@math items="sorted: 5n − 4 = 36@already sorted;;reversed: (3n² + 7n − 8)/2 = 120@in reverse"
Count every line of insertion sort. On eight keys already sorted, it runs five n minus four lines, thirty six. On eight keys in reverse, it's a hundred and twenty.

@words text="Best case linear, worst case Θ(n²)"
The best case is linear. The worst case is quadratic, and that's the one the book reports, because it's a guarantee.

@end text="Full lesson on Learn"
Count your own arrays in the full lesson on Learn.
