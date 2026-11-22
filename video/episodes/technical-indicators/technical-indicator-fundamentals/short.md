---
format: short
lesson: technical-indicators/technical-indicator-fundamentals
title: An indicator can't see the next bar
---

@art lookback-window
Every indicator value comes from bars that have already closed.

@math items="SMA = (C₁ + … + Cₙ) ÷ n@add up"
Take a simple moving average. Add up the last n closes and divide by n. Nothing in that calculation comes from the future.

@words text="A summary, not a forecast"
An indicator summarizes history. Before you trust one, know its input, its formula, and the bars inside its window.

@end text="Full lesson on Learn"
The full lesson, with a window you can move, is on Learn.
