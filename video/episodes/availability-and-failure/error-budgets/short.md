---
format: short
lesson: availability-and-failure/error-budgets
title: Never went down, still blew the error budget
---

@art green-checks
Every uptime check stayed green all month. You still spent a hundred and twenty three percent of your error budget.

@math items="6 h × 2000 rps × 15% = 6 480 000 failures@six hours;;budget: 5 256 000@The month allowed"
Six hours where fifteen percent of requests fail, at two thousand a second, is nearly six and a half million failures. The month allowed five point two six million.

@words text="burn = rate × duration × failed fraction"
Uptime has no severity factor. An error budget does.

@end text="Full lesson on Learn"
The full lesson, with incidents to run, is on Learn.
