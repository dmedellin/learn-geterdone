---
format: short
lesson: capacity-estimation/orders-of-magnitude
title: Why the middle of your estimate is not the average
---

@art lopsided-average
Your estimate's range is a hundred and twenty five gigabytes to eight terabytes. Where's the middle?

@math items="(lo + hi)/2 = 4.0625·10¹²@average the ends;;√(lo · hi) = 10¹²@the square root"
If you average the ends, you get about four times the estimate you started with. Take the square root of low times high instead, and you get ten to the twelve, one terabyte, exactly.

@words text="Ranges built by multiplying: use √(lo · hi)"
A range built by multiplying has its centre at the geometric mean, not the average.

@end text="Full lesson on Learn"
The full lesson, with every factor on a slider, is on Learn.
