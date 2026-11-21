---
format: short
lesson: enterprise-patterns-domain-logic/money
title: Split five cents and gain a penny
---

@art split-bar
Split five cents seventy thirty, and you can end up with six.

@math items="exact: 3.5 and 1.5@three and a half;;nearest: 4 + 2 = 6@four and two;;down: 3 + 1 = 4@three and one"
The exact shares are three and a half and one and a half. Round to nearest, and it's four and two: six cents. Round down, three and one: four.

@art allocator
Fowler's favourite fix is an allocator. Round down, then hand the leftover cents out one at a time.

@end text="Full lesson on Learn"
The full lesson, with a lab for every rule, is on Learn.
