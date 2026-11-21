---
format: short
lesson: code-complete-statements/boolean-expressions
title: The DeMorgan mistake that is wrong half the time
---

@art wrong-row
Negate a condition the easy way, and it's wrong on half its rows.

@math items="!(done || error)  ≡  !done && !error@not done and not error;;✗  !done || !error@not done or not error"
Not, done or error, is the same as not done and not error. But not done or not error, negating each part and keeping the or, differs on two of four rows.

@words text="Negate each part, and switch the operator"
DeMorgan needs both steps. Negate each part, and switch the ands and ors.

@end text="Full lesson on Learn"
The full lesson, with a truth table lab, is on Learn.
