---
format: short
lesson: code-complete-statements/nesting-and-complexity
title: Flattening code doesn't remove its decisions
---

@art moved-boxes
You flattened the routine. Its decisions didn't go anywhere.

@math items="nesting: 5 → 1@five to one;;decision points: 9 → 6@nine to six"
A shipping routine nested five deep, with guard clauses, goes from five to one level. Decision points drop from nine to six.

@words text="The for, its if and its || moved out"
But three of them just moved into another routine, where they still have to be read. The reader juggles less at once. The program decides just as much.

@end text="Full lesson on Learn"
The full lesson, with a complexity lab, is on Learn.
