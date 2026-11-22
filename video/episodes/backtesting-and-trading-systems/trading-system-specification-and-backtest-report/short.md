---
format: short
lesson: backtesting-and-trading-systems/trading-system-specification-and-backtest-report
title: The risk cap that can never work
---

@art contradiction-block
Risk per trade, three point five percent. Maximum open risk, three percent. Spot the problem?

@math items="first trade: 3.5% open risk@first position;;3.5% > 3% cap@more than"
The first position alone carries three point five percent, more than the cap. The cap is broken by the very first trade.

@words text="Block it, don't warn"
So it can never constrain anything. A good specification builder blocks it before export.

@end text="Full lesson on Learn"
Build and validate a spec in the full lesson on Learn.
