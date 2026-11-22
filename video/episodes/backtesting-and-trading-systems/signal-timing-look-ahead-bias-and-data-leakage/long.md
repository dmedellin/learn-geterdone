---
format: long
lesson: backtesting-and-trading-systems/signal-timing-look-ahead-bias-and-data-leakage
title: Look-ahead bias: when your backtest reads tomorrow's newspaper
thumb: Known before you trade
---

@chapter The problem
@title text="Signal Timing, Look-Ahead Bias, and Data Leakage" sub="Backtesting and Trading Systems" art=thumb
Here's a backtest that looks perfect. Every time the close breaks out, it buys at that close. The problem is that the breakout isn't known until the close has printed. By then, that price has gone.

@words text="Every input must be available before the decision"
The lesson's rule is strict. Every input must have been available before the simulated decision and fill. Future information can make a weak rule look precise, and it rarely announces itself. The result just looks a little too good, and it's tempting to believe it.

@chapter Three ways the future leaks in
@art future-peek
The first is look ahead bias. The test uses a value that only became known after the simulated decision. Buying at the close that generated the signal is the classic case.

@art full-sample-mean
The second is data leakage. Training or preprocessing exposes information from validation or future periods. For example, normalising every period with a mean computed over the full sample. Now future observations affect the past transformed values.

@words text="No single price is out of place"
Leakage is subtle, because no single price is out of place. You can inspect every row and find nothing wrong. The mean just carries a little of the future into every period it touches, and the fix is to fit it on the training period alone.

@art publication-lag
The third is publication lag. Fundamental and macro data must enter the test on the date they were released, not the period they describe. On a quarter's end date, the report doesn't exist yet. And revised figures aren't the numbers that were originally released. Fundamental data enters on the date it became available to the market.

@chapter A causal sequence
@list heading="Build a causal event sequence" items="Observe: complete the bar or receive the event@Observe|Calculate: update indicators and conditions@calculate|Execute: an eligible order at a later price@execute"
The fix is a causal sequence of events. Observe: complete the bar, or receive the event. Calculate: update the indicators and evaluate the conditions. Execute: submit an eligible order at a later executable price. And for every field, record when it became knowable.

@art observe-calc-execute
Each step happens strictly after the one before. If a step ever uses something from later in the sequence, the test has broken causality, however small the gap.

@chapter Bar 40
@math heading="Breakout confirmed by bar 40's close" items="signal: close of bar 40@close of bar forty;;order: next opportunity@next opportunity;;fill: bar 41's open@forty one"
Here's the lesson's example. A breakout is confirmed by bar forty's close. So the signal exists at the close of bar forty. The order goes in at the next opportunity. And the earliest fill is at the open of bar forty one.

@art next-bar-open
Bar forty's close is the value the rule needed to see. It can't be both read and traded at. And bar thirty nine is worse: nothing on bar thirty nine knew what bar forty would close at. The lab counts every fill that breaks this order as an invalid assumption.

@art causal-arrow
Notice that none of these mistakes need bad intentions. A single line of code that reads the current bar's close a moment too early is enough. That's why the lesson asks you to timestamp signals, orders and fills separately. If all three share one timestamp, you can't even check the order they happened in.

@chapter Where people slip
@list heading="Common mistakes" items="Buying at the close that made the signal@The first|Revised data used as originally released@The second|Centering the full dataset before splitting@And the third"
The first mistake is buying at the close that generated the signal. The second is using revised economic data as if it were the originally released data. And the third is centering the full dataset before splitting it into training and validation.

@list heading="Practical rules" items="Timestamp signals, orders and fills separately@Timestamp|Lag data by actual availability@Lag data|Fit transformations on training data only@fit any transformation"
The practical rules follow. Timestamp signals, orders and fills separately, so you can check their order. Lag data by its actual availability, not its reporting period. And fit any transformation on training data only.

@chapter Try it
@words text="Same-period fills vs next-period fills"
In the lesson's lab, which runs on deterministic synthetic educational data, you can switch between valid next period execution and impossible same period fills, and then add future leakage. Watch how much the result inflates. That gap is how much of the performance was never available.

@end text="Switch on the leak, watch it inflate"
You can add leakage and watch the result inflate, on Learn. That's learn dot get er done dot I O.
