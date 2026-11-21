---
format: short
lesson: enterprise-patterns-data-source/gateways
title: Rename one column, edit four classes
---

@art sql-everywhere
Rename one column, and you're editing four classes.

@math items="SQL in every class: edit 4@each hold;;one gateway: edit 1@one gateway"
When cart, checkout, report and admin each hold their own SQL against the price table, a rename is edited in all four. Put the SQL in one gateway, and the rename is edited in one.

@words text="All the SQL, easy to find"
That's Fowler's promise: the rest of the application knows nothing about SQL.

@end text="Full lesson on Learn"
The full lesson, with a lab that traces it, is on Learn.
