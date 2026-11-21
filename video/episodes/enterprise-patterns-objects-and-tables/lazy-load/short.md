---
format: short
lesson: enterprise-patterns-objects-and-tables/lazy-load
title: Why your list page sends fifty queries
---

@art ripple
One query for the list, then one more for every row. That's ripple loading.

@words text="A collection of lazy objects"
Each lazy object, looked at one by one, makes its own trip to the database, where one trip could have fetched them all.

@art lazy-collection
Fowler's cure: make the collection itself lazy, and load all of it the first time it's touched.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the queries, is on Learn.
