---
format: short
lesson: measuring-systems/coordinated-omission
title: Your load test reported 2 ms through a one second outage
---

@art stall-gap
A one second stall in your load test. The p ninety nine says two milliseconds.

@math items="as recorded:  p99 = 2 ms@two milliseconds;;with the 99 missed requests:  p99 = 990 ms@nine hundred and ninety"
As recorded, that's two milliseconds. The generator waits for each reply before sending the next, so during the stall it sent nothing. Put back the ninety nine requests its own schedule called for, each waiting from when it was due, and the p ninety nine is nine hundred and ninety.

@words text="Generate on a clock, not on replies"
That's four hundred and ninety five times worse.

@end text="Full lesson on Learn"
The full lesson, with the correction worked out, is on Learn.
