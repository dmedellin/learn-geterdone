---
format: short
lesson: enterprise-patterns-objects-and-tables/embedded-value-and-serialized-lob
title: Nine queries or one? Storing a tree in a column
---

@art node-by-node
A thread of eight posts takes nine queries to read. Or one.

@math items="post by post: 9 queries@post by post;;level by level: 5@level by level;;one column: 1@one column"
Read it post by post, and that's nine queries. Level by level, five. Serialize the whole thread into one column, and it's one.

@art one-column
The catch: SQL can't see inside that column. Use it too much, Fowler warns, and your database becomes a transactional file system.

@end text="Full lesson on Learn"
The full lesson, with a lab for any tree, is on Learn.
