---
format: short
lesson: sorting-and-selection/what-a-sort-must-promise
title: Sort by the less important key first
---

@art two-passes
To sort by department, then by name, you sort by name first.

@words text="1. name (stable) · 2. department (stable)"
The last pass is the one whose order survives across the whole list. And because it's stable, it leaves ties alone, so the name order from the first pass survives inside each department.

@words text="Major first → sorted by name"
Do it the other way, and you've sorted by name, with department as the tie break.

@end text="Full lesson on Learn"
The full lesson, with both orders run side by side, is on Learn.
