---
format: short
lesson: enterprise-patterns-layers-and-performance/capacity-and-scalability
title: The slower system that scales better
---

@art two-lines-cross
The system that's twice as fast on one server can still lose.

@math items="Swordfish: 20 tps, +15 a server@Swordfish does twenty;;Camel: 40 tps, +10 a server@Camel does forty;;5 servers: both 80@five servers"
In Fowler's illustration, Swordfish does twenty transactions a second, and gains fifteen with each extra server. Camel does forty, but gains only ten. At five servers, both reach eighty.

@words text="Capacity ≠ scalability"
Capacity says what one server does. Scalability says what the next server adds.

@end text="Full lesson on Learn"
The full lesson, with a lab that projects both, is on Learn.
