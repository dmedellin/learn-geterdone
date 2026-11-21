---
format: short
lesson: enterprise-patterns-objects-and-tables/class-and-concrete-table-inheritance
title: The inheritance mapping that's fast until you search
---

@art concrete-tables
One table per concrete class means no joins. So why not always use it?

@math items="load a manager: 1 table@one table;;find every person: 3 tables@find every person;;add a field to person: 3 tables@add a field"
Loading a manager reads one table. But find every person, and you search all three. Add a field to person, and you alter all three.

@words text="Class table: joins to load, alters one"
Class Table Inheritance is the opposite trade. It joins to load, but alters just one table.

@end text="Full lesson on Learn"
The full lesson, with a lab for all three mappings, is on Learn.
