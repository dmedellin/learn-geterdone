---
format: short
lesson: availability-and-failure/shuffle-sharding
title: How shuffle sharding turns outages into degradations
---

@art one-left
Sixteen nodes, two per tenant, picked at random. One bad tenant poisons its nodes.

@math items="share one node:  7/30  →  degraded@Seven in thirty;;share both:  1/120  →  down@shares both"
Seven in thirty tenants share one of those nodes. They lose half their capacity and keep working. Only one in a hundred and twenty shares both, and goes down.

@words text="Overlap is not collision"
Overlap isn't collision. Random shards make a full outage rare.

@end text="Full lesson on Learn"
The full lesson, with the overlaps counted, is on Learn.
