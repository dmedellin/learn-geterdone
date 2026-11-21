---
format: short
lesson: gof-structural/adapter
title: Three adapters, or one?
---

@art plug-mismatch
Your code wants one interface. The library you can't change speaks another.

@art adapter-between
Put a small class between them. It implements your interface, and calls the library. That's Adapter.

@art class-adapter-each
Inherit from the vendor's class, and you need one adapter per class. Three printers, three adapters. But you can override its behaviour in one line.

@art object-adapter-family
Hold the vendor's object instead, and one adapter serves the whole family.

@end text="Full lesson on Learn"
The full lesson, with a lab to count both designs, is on Learn.
