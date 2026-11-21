---
format: short
lesson: enterprise-patterns-domain-logic/transaction-script
title: The simplest way to organise business logic
---

@art one-per-action
One procedure for each thing a user can do. That's a whole pattern.

@words text="Transaction Script"
Fowler calls its glory its simplicity. A script takes the input, validates, calculates, stores, and replies. For an application with little logic, it's natural, with very little overhead.

@art copied-block
The catch comes as the logic grows. Two scripts need the same rule, and each writes its own copy.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the copies, is on Learn.
