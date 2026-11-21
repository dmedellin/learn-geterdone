---
format: short
lesson: enterprise-patterns-objects-and-tables/unit-of-work
title: Six database writes that should be two
---

@art scattered-writes
Your save writes six times. It only needed two.

@math items="at once: 6 writes@six writes;;at commit: INSERT line1; UPDATE order7@insert line one"
Change an order twice, add two lines, delete one, and change the other. Written as you go, that's six writes. A Unit of Work commits two: insert line one, and update the order once.

@art created-deleted
The line that was added and deleted never reaches the database at all.

@end text="Full lesson on Learn"
The full lesson, with a lab for your own script, is on Learn.
