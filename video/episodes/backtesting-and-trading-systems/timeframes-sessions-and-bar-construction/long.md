---
format: long
lesson: backtesting-and-trading-systems/timeframes-sessions-and-bar-construction
title: Bars, sessions and timeframes: what your chart is hiding
thumb: The bar hides the order
---

@chapter The problem
@title text="Timeframes, Sessions, and Bar Construction" sub="Backtesting and Trading Systems" art=thumb
Switching from five minute bars to hourly bars feels like zooming out on a chart. Same market, different view. The lesson says that's wrong, and it matters.

@words text="A timeframe changes the information available"
A timeframe doesn't merely change the chart view. It changes the information available to the system. And so it changes the indicators, the signals and the fills.

@art twelve-into-one
Here's why. A sixty minute bar hides the sequence inside twelve five minute bars. You get one open, one high, one low and one close. The path in between, the order things happened in, is gone. Volume isn't lost, because aggregation sums it. It's the sequence that disappears.

@chapter The missing sequence
@art which-came-first
That's how an hourly test can miss an intrabar stop. The bar shows the range, but not whether the high or the low came first. If your stop and your target are both inside that range, the bar can't tell you which one was hit.

@words text="Use data granular enough for the fill model"
So choose a source frequency granular enough for your execution assumptions. Lower frequency bars are fine only when their information supports the fill model you're using. And never use daily bars to infer an exact intraday sequence.

@chapter Sessions
@art sessions-band
Next, sessions. Regular, extended, overnight and exchange specific sessions all produce different datasets. Extended hours prints are real prices. Include them and you change the gaps, the highest high a breakout reads, the volume, and the bars a rule can be filled in.

@words text="Extended-hours signals · regular-hours fills?"
That's why mixing extended hours signals with regular hours fills, without clear rules, is one of the lesson's named mistakes. Include only the times the system is allowed to observe and trade.

@chapter The decision clock
@list heading="Define the market clock" items="Bar interval@bar interval|Session rule@session rule|Decision clock@decision clock"
The lesson pulls this together into three definitions. The bar interval: open, high, low, close and volume all depend on the aggregation window. The session rule: which hours count. And the decision clock: the exact timestamp when indicators update and orders become eligible.

@art boundary-rule
Bar boundaries should come from a documented exchange and timezone rule. Not the most profitable alignment, which is fitting the clock to the answer. And not whatever local time the machine happens to use, which gives a different dataset on every run. Use one timezone, one calendar and one boundary rule.

@art time-grid
The decision clock is the one people forget to write down. When exactly does the indicator update: at the close of the bar, or as each trade arrives? And when does an order become eligible? If you don't fix that moment before testing, two runs of the same rule can quietly disagree.

@chapter Count the bars
@math heading="Regular session: 390 minutes" items="390 ÷ 60 = 6.5@six point five;;6 full bars + 1 partial bar@six full bars;;the 7th bar covers 30 minutes@thirty minutes"
Here's a quick one from the lesson. A regular session runs three hundred and ninety minutes. Aggregate it into sixty minute bars. Three hundred and ninety divided by sixty is six point five. So you get six full bars, and a seventh partial bar covering the last thirty minutes.

@art partial-bar
Not six bars, because six times sixty only covers three hundred and sixty minutes. And not six and a half, because a bar is a whole record. A rule needs to know that the seventh bar is shorter, and not comparable to the others.

@chapter Where people slip
@list heading="Common mistakes" items="Assuming all daily bars close at the same time@The first|Extended-hours signals with regular-hours fills@The second|Inferring intraday order from daily OHLC@And the third"
The first mistake is assuming all daily bars close at the same time. The second is mixing extended hours signals with regular hours fills without rules. And the third is using daily open, high, low and close to infer an exact intraday sequence. Store timestamps in one clear canonical timezone.

@chapter Try it
@words text="Same minutes · different bars · different signals"
In the lesson's lab, which uses deterministic synthetic educational data, you can aggregate one intraday sequence into different bars and sessions. Try it. Build five minute bars, then sixty minute bars, then switch the extended session on and off. Watch where the signals move, and ask which version your fill model can honestly support.

@end text="Build bars from the same minutes"
You can aggregate the same sequence into different bars and sessions, on Learn. That's learn dot get er done dot I O.
