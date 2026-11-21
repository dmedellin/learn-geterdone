---
format: short
lesson: gof-creational/abstract-factory
title: The design pattern that makes one change easy and one hard
---

@art growth-edits
Abstract Factory makes one kind of change free, and another expensive.

@math items="new style: +4 classes, 0 edited@a new style;;new kind: +5 classes, 5 edited@a new kind"
In the lesson's map viewer, a new style adds four classes and edits nothing. A new kind of part adds five, and edits every factory, because the factory's interface lists the kinds.

@words text="Families vary, kinds stay put"
So use it where families vary and the kinds stay put.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the classes, is on Learn.
