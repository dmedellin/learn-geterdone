---
format: short
lesson: enterprise-patterns-data-source/row-data-gateway-and-finders
title: Why one big query beats fifty small ones
---

@art many-trips
Fifty small queries can be ten times slower than one big one.

@math items="50 keyed finds: 255 ms@Fifty keyed finds;;one query, 200 rows: 25 ms@one query"
At five milliseconds a statement and a tenth a row, fifty keyed finds take two hundred and fifty five milliseconds. One query returning two hundred rows takes twenty five. Every statement pays the wait.

@words text="Unless the wait is short"
But put the database on the same machine, and the advice reverses. So measure.

@end text="Full lesson on Learn"
The full lesson, with a lab for the timings, is on Learn.
