---
format: short
lesson: gof-document-editor/document-structure
title: One call, every part of the tree
---

@art glyph-tree
A line can hold a letter, or a whole diagram. Should the line care which?

@art composite-roles
The Gang of Four say no. Give a single part and a group of parts one interface. A group answers by asking each of its parts.

@math items="10 nodes → 10 calls@ten nodes;;total: 345 minutes@three hundred"
In the lesson's recipe book, ten nodes means ten calls, and one question returns three hundred and forty five minutes.

@words text="That's Composite"
The client asks once, and never needs to know what's inside.

@end text="Full lesson on Learn"
The full lesson, with a tree to count, is on Learn.
