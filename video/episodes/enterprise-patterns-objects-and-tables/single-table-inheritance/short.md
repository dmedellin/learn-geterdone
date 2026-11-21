---
format: short
lesson: enterprise-patterns-objects-and-tables/single-table-inheritance
title: Store a whole class hierarchy in one table
---

@art one-table
Four classes, one table, and no joins. What's the catch?

@words text="Columns for every class"
Single Table Inheritance puts every class in one table, with a type column. Every row has columns for every class's fields, and uses only its own.

@math items="manager: 7 fields used, 2 of 9 empty@two of the nine"
In the lesson's staff hierarchy, a manager's row leaves two of the nine field columns empty. That's the price of one place for everything.

@end text="Full lesson on Learn"
The full lesson, with a lab for all three mappings, is on Learn.
