---
format: short
lesson: enterprise-patterns-layers-and-performance/enterprise-applications
title: Business logic is the least logical thing in your code
---

@art branching-rule
Martin Fowler says there's little less logical than business logic.

@code block=1 lines=1-19 label=Java focus="4-6@Government|7-9@northern|10-14@retail|15-17@cap"
Take a due date rule with four agreements. Government gets fifteen more days, northern customers ten, late retail invoices five, and a cap at sixty.

@math items="1 + if 5 + && 2 + || 1 = 9@nine decision points;;plain rule: 1@plain rule"
That's nine decision points. The plain rule has one. The other eight are agreements, and nobody could derive them.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts them, is on Learn.
