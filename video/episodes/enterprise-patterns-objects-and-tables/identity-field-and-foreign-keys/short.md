---
format: short
lesson: enterprise-patterns-objects-and-tables/identity-field-and-foreign-keys
title: Why the order of your inserts matters
---

@art parents-first
Insert a line before its order, and the database refuses.

@code block=1 lines=1-9 label=Java focus="4@parent row|7@each line"
A line row holds its order's key. So against a database that checks every statement, insert the parent row first, then each line.

@words text="Or defer the checks to commit"
Fowler's first advice, though: if the database can defer its checks to commit, do that, and the order stops mattering.

@end text="Full lesson on Learn"
The full lesson, with a lab that sorts the writes, is on Learn.
