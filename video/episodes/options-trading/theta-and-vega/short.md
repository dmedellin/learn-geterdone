---
format: short
lesson: options-trading/theta-and-vega
title: The vega mistake that's off by a factor of a hundred
---

@art iv-dial-vega
Implied volatility falls ten points. Do you multiply vega by ten, or by zero point one?

@math items="Vega = 0.139 per IV point@zero point one three nine;;0.139 × (−10) × 100 = −$139@minus ten"
Vega is quoted per one percentage point. So a vega of zero point one three nine, times minus ten points, times one hundred, is minus one hundred and thirty nine dollars.

@words text="Points, not decimals"
Use zero point one, and you'd get a dollar thirty nine. Match the units.

@end text="Full lesson on Learn"
The full lesson, with a time and volatility shock, is on Learn.
