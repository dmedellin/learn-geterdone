---
format: short
lesson: enterprise-patterns-domain-logic/value-object
title: The bug where changing one booking changes another
---

@art shared-range
Extend one booking, and a second booking quietly extends too.

@words text="Two bookings, one DateRange"
Both bookings share one DateRange object, because they cover the same week. One calls setEnd on it. Now the other booking's range has changed, though nothing touched it.

@words text="Make values immutable"
Fowler's advice: make value objects immutable. To change a date, replace the object with a new one, and sharing is safe.

@end text="Full lesson on Learn"
The full lesson, with a lab that checks a class, is on Learn.
