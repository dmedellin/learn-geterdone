---
format: short
lesson: enterprise-patterns-objects-and-tables/identity-map
title: The bug from loading one row twice
---

@art two-watches
Two watches, and you never know the time. Neither does your app.

@art two-copies
Load the same row into two objects and change both. Whichever is written last decides what the database holds.

@words text="Look in the map first"
An Identity Map keeps every loaded object by its key. Look there before every load, and one row is always one object. Saving the query is just a bonus.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts duplicates, is on Learn.
