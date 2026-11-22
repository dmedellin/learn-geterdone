---
format: short
lesson: backtesting-and-trading-systems/walk-forward-testing
title: How many walk-forward folds fit in 350 bars?
---

@art rolling-windows
Three hundred and fifty bars, train on eighty, test on thirty. How many folds?

@math items="(350 − 80 − 30) ÷ 30 = 8@two hundred and forty;;8 + 1 = 9@plus one"
Three hundred and fifty minus eighty minus thirty is two hundred and forty. Divided by thirty, eight. Plus one for the first fold: nine forward windows.

@words text="9 × 30 = 270 = every bar after training"
Nine times thirty covers every bar after the first training window, exactly once.

@end text="Full lesson on Learn"
Slide the windows in the full lesson on Learn.
