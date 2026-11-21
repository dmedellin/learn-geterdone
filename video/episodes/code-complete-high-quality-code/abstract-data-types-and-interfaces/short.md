---
format: short
lesson: code-complete-high-quality-code/abstract-data-types-and-interfaces
title: Six public methods, three classes hiding inside
---

@art mixed-drawer
How many classes are hiding inside this one?

@code block=3 lines=12-17 label=Java focus="12-13@tickets|14-15@forecast|16-17@audit log"
Read the method names. Two are about tickets. Two are about a weather forecast. And two run an audit log.

@words text="One class, one abstraction"
Steve McConnell's rule: each class should implement one abstract data type, and its public routines should belong together.

@art grouped-routines
By the names alone, that's three classes sharing one name.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts what a class exposes, is on Learn.
