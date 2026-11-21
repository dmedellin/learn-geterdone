---
format: short
lesson: ddd-building-blocks/layered-architecture
title: The fix that adds arrows
---

@words text="8 arrows → 10 arrows" sub="and it's better"
The fix added two more dependencies, and the design got better.

@code block=1 lines=6-9 label=Java focus="8@tells the screen"
A library's Loan object, when it falls overdue, tells the screen directly. The domain now depends on the user interface. That arrow points up.

@art callback-up
Evans's fix: the domain declares a listener, and the screen implements it. One more interface, one more arrow, and none pointing up.

@end text="Full lesson on Learn"
Count a library's arrows in the full lesson on Learn.
