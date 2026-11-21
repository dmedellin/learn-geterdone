---
format: short
lesson: enterprise-patterns-data-source/data-mapper
title: A Data Mapper doesn't remove dependencies
---

@art dependency-arrows
A Data Mapper doesn't remove a dependency. It turns one around, and adds one.

@math items="jdbc changes: reaches 2, no domain class@database library;;account changes: reaches 4, mapper included@domain class"
Change the database library, and it now stops at the mapper and main. But change the domain class, and the mapper depends on it too, so it reaches four classes.

@words text="Its price: one more layer"
That's why Fowler pairs it with a rich Domain Model, and not with a simple one.

@end text="Full lesson on Learn"
The full lesson, with a lab that traces it, is on Learn.
