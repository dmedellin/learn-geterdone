---
format: short
lesson: gof-document-editor/window-systems
title: When you can't change the vendor's classes
---

@art no-common-base
Four window systems, four vendors, no common base class. How does one editor run on all of them?

@art window-windowimp
Give every window an implementation object behind an interface you define. The window asks it to draw. Each platform's subclass does the work its own way.

@words text="Two hierarchies, one reference"
Kinds of window grow on one side, platforms on the other, and neither touches the other. That's Bridge.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the classes, is on Learn.
