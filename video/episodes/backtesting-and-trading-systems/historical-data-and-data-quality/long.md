---
format: long
lesson: backtesting-and-trading-systems/historical-data-and-data-quality
title: Bad data makes fake signals: checking history before a backtest
thumb: One bad bar, many wrong numbers
---

@chapter The problem
@title text="Historical Data and Data Quality" sub="Backtesting and Trading Systems" art=thumb
A backtest can only be as reliable as the historical data its rules read. That sounds obvious. What's less obvious is how small a defect it takes to change the answer.

@art spike-breakout
A single bad price spike can look exactly like a breakout. A missing bar can change an indicator. And a stale value, a price that stopped updating, can create a fill that could never have happened.

@chapter Three checks
@list heading="What to understand" items="Completeness@Completeness|Consistency@Consistency|Plausibility@Plausibility"
The lesson sorts the checks into three groups. Completeness: are the expected instruments, timestamps, fields and sessions all there? Consistency: are there duplicates, are records in order, are the units and timezone right, and do the prices relate to each other properly? Plausibility: are there stale bars, extreme jumps, negative values, or impossible records?

@art missing-and-duplicate
Completeness and consistency are the structural problems. A gap where a bar should be. The same bar twice. Bars out of order, or stamped in a different timezone from the rest.

@art impossible-candle
Plausibility is about values that can't be true. A negative price. A candle whose high is below its close. A price that sits unchanged for far too long. Each of these loads into a file without complaint, and that's the trap. Loading isn't validation.

@chapter Why timestamps matter
@art timestamp-shift
Timestamps deserve their own mention. Signals depend on event order and session boundaries. If a timestamp is wrong, events get reordered. A signal can end up computed on a bar that hadn't closed yet, which is a leak of future information, not just a wrong label.

@words text="Vendors don't all share a timezone"
And don't assume all vendor files use the same timezone. Mixing them can create wrong bars or expose future data without any obvious error.

@chapter One missing bar
@words text="Close above the highest close of the previous 12 bars"
Here's the lesson's worked question. A rule counts closes above the highest close of the previous twelve bars. One bar in the file is missing. How many bars can the rule not score because of it?

@math heading="One hole, twelve-bar window" items="1 missing bar@the missing bar;;each of the next 12 windows contains the hole@each of the next twelve;;12 bars can't be scored@twelve bars"
You might think just one, the missing bar itself. But each of the next twelve bars has that hole inside its twelve bar window, and you can't compute a highest of twelve across a hole. So twelve bars can't be scored on the raw series.

@art lookback-window
And skipping the hole isn't a fix. That turns the window into eleven bars, which is a different rule. The lab's validated series repairs the bar instead, and says that it did.

@chapter Validate before calculating
@list heading="Validate before calculating" items="Profile missing, duplicate, stale, extreme@Profile|Repair or exclude, documented@repair or exclude|Recalculate on the validated data@recalculate"
So the workflow is fixed. Profile: measure the missing, duplicate, stale and extreme records. Then repair or exclude, with a documented treatment that doesn't invent unknown prices. Then recalculate, and confirm that indicators and signals use the validated dataset.

@words text="Flag it · document the treatment" sub="never copy a future price into a past bar"
A missing bar should be flagged and handled with a documented, instrument appropriate rule. Never silently invent a price. And never just copy the next close into it, because that puts a future price into a past bar, which is look ahead by construction.

@art validate-pipeline
Run this validation automatically, before every backtest, not once when the file first arrives. Data gets updated, vendors change formats, and a check you ran last month says nothing about today's file. The validated dataset is the only one the rules should ever see.

@chapter Where people slip
@list heading="Common mistakes" items="Correcting data by hand with no audit trail@The first|Assuming one timezone for every vendor@The second|Ignoring delisted or halted instruments@the third"
The first mistake is correcting data by hand without an audit trail. The second is assuming every vendor file uses the same timezone. And the third is ignoring instruments that were delisted or temporarily halted. Keep the raw data, record every change, and treat suspicious records as defects until they're verified.

@chapter Try it
@words text="Inject one defect · watch the signals move"
In the lesson's lab, which uses deterministic synthetic educational data, you can inject common defects and then clean them. Try adding one bad record and watch how far it travels into the signals and the performance.

@end text="Break the data, then clean it"
You can inject and clean data defects yourself, on Learn. That's learn dot get er done dot I O.
