---
format: short
lesson: backtesting-and-trading-systems/timeframes-sessions-and-bar-construction
title: A 390-minute session makes 7 hourly bars, not 6
---

@art partial-bar
A trading session is three hundred and ninety minutes. How many hourly bars?

@math items="390 ÷ 60 = 6.5@six point five;;6 full bars + a 30-minute 7th@seventh"
Three hundred and ninety over sixty is six point five. That's six full bars, and a seventh bar covering just thirty minutes.

@words text="The short bar isn't comparable"
A bar is a whole record, so your rule has to know the last one is shorter than the rest.

@end text="Full lesson on Learn"
Build bars yourself in the full lesson on Learn.
