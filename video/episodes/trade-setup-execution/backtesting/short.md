---
format: short
lesson: trade-setup-execution/backtesting
title: Why your backtest win rate isn't the real one
---

@art regime-bands
You set a base win rate. The backtest reports a different one. Why?

@words text="Each trade draws a regime" sub="trend · range · volatile"
In the lesson's synthetic lab, every trade draws a regime, and the win probability is nudged by setup and regime.

@math items="breakout in a range: −0.08@breakout in a range;;pullback in a trend: +0.07@pullback in a trend"
A breakout in a range loses zero point zero eight. A pullback in a trend gains zero point zero seven. The base rate is just an average over conditions the rule can't choose.

@end text="Full lesson on Learn"
Run a synthetic backtest in the full lesson on Learn.
