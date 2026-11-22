---
format: short
lesson: backtesting-and-trading-systems/signal-timing-look-ahead-bias-and-data-leakage
title: You can't buy at the close that made the signal
---

@art future-peek
Your backtest buys at the close. But it only knew to buy after the close.

@math items="signal: bar 40's close@bar forty's close;;earliest fill: bar 41's open@forty one"
If a breakout is confirmed by bar forty's close, the earliest fill is the open of bar forty one.

@words text="Read it, then trade later"
Bar forty's close can't be both the thing you read and the price you trade. Fill there, and your test is quietly using the future.

@end text="Full lesson on Learn"
See the leak inflate a result in the full lesson on Learn.
