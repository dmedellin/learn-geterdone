---
format: short
lesson: storage-engines-and-indexes/hash-vs-tree-for-ranges
title: The hash index that does 167 times the work
---

@art full-scan
A hash index is faster than a tree. Until you ask it for a range.

@math items="hash:  900 + 100 × 5 000 = 500 900 /s@five hundred thousand;;tree:  900 × 3 + 100 × 3 = 3 000 /s@three thousand"
With no order, every range becomes a full scan, five thousand page reads. On nine hundred lookups and a hundred ranges a second, that's five hundred thousand nine hundred reads, against the tree's three thousand.

@words text="Faster at what?"
Always name the operation.

@end text="Full lesson on Learn"
The full lesson, with the crossover worked out, is on Learn.
