---
format: short
lesson: dynamic-programming-and-sequential-decisions/filling-the-table-from-the-end
title: The dynamic programming bug that passes every check
---

@art tie-fork
Your shortest path answer is right, and it's still hiding two other routes.

@math items="f(B) = min(7 + 1, 4 + 4) = 8@seven plus one;;f(A) = min(0 + 8, 4 + 4) = 8@zero plus eight"
At B, seven plus one and four plus four both give eight. At A, zero plus eight and four plus four tie again.

@art three-routes
Follow every tie, and three routes cost eight. Keep only the first best arc, and the page quietly shows one.

@end text="Full lesson on Learn"
The full lesson, with a network to fill in yourself, is on Learn.
