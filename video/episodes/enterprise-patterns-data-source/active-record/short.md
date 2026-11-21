---
format: short
lesson: enterprise-patterns-data-source/active-record
title: Active Record or Row Data Gateway? One method decides
---

@art row-only
Two classes, same row, same SQL. One is an Active Record. Why?

@code block=1 lines=1-19 label=Java focus="7-14@find and update|16-18@canWithdraw"
Both have find and update. But Account also has canWithdraw, which decides whether the balance plus the overdraft covers a sum. That's a rule of the business.

@words text="Domain logic → Active Record"
A Row Data Gateway holds only database access. Add domain logic, and it's an Active Record.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts routines, is on Learn.
