---
format: short
lesson: enterprise-patterns-domain-logic/special-case
title: Return a guest instead of null
---

@art repeated-checks
Every null you return becomes a check in every caller.

@code block=1 lines=1-11 label=Java focus="3@not null|7@again"
This greeting tests that the customer is not null before asking its name, and again before asking its plan. Five decision points.

@art stand-in
Fowler's Special Case: return a GuestCustomer instead, named friend, on the basic plan. Now the greeting just asks. One decision point.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the checks, is on Learn.
