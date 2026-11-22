---
format: short
lesson: backtesting-and-trading-systems/historical-data-and-data-quality
title: One missing bar breaks twelve
---

@art lookback-window
One missing bar in your data. How many bars does it break?

@words text="Close above the highest of the previous 12"
Take a rule that compares each close with the highest close of the previous twelve bars.

@math items="each of the next 12 windows holds the hole@each of the next twelve;;12 bars can't be scored@twelve bars"
Each of the next twelve bars has the hole inside its window. So twelve bars can't be scored, not just one.

@end text="Full lesson on Learn"
Inject and clean data defects in the full lesson on Learn.
