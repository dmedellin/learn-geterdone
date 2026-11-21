---
format: short
lesson: code-complete-high-quality-code/assertions-and-error-handling
title: The range check that never fires
---

@art month-range
This month check looks right, and lets every bad month through.

@words text="month < 1 && month > 12"
Month less than one, and month greater than twelve. But no integer is below one and above twelve at the same time. So the check is never true. You wanted or.

@art boundary-ticks
So test both ends of the range, just inside and just outside. Zero and thirteen expose it at once.

@end text="Full lesson on Learn"
The full lesson, with a lab to test your own checks, is on Learn.
