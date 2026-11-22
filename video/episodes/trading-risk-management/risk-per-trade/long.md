---
format: long
lesson: trading-risk-management/risk-per-trade
title: Risk per trade: why the percentage decides how deep you fall
thumb: Small losses, slow decay
---

@chapter The question
@title text="Risk Per Trade" sub="Trading Risk Management" art=thumb
How much of your account should one trade be allowed to lose? It sounds like a small decision. But it decides how deep you fall in a bad stretch, and how hard it is to climb back.

@words text="Losing streaks happen even when the method is valid"
Losing streaks occur even when the trading method is valid. Oversized risk turns normal variance into severe drawdown. Smaller fixed percentage risk slows account decay after each loss.

@chapter Risk as a percentage
@art shrinking-steps
Risk percentage is the planned dollar loss divided by current account equity. And that word current is doing a lot of work. With fixed percentage risk, what happens after a loss? Dollar risk decreases with equity. The same percentage applied to lower equity produces a smaller dollar amount.

@art fixed-vs-percent
That's compounding down. Fixed percentage sizing automatically reduces dollar risk as equity falls. If you kept risking the original dollar amount, that would be fixed dollar sizing, and each loss would take a bigger share of what's left.

@art compound
With a fixed percentage, the account still falls in a streak, but each drop is smaller than the last, so the decline slows as it goes.

@chapter Three losses in a row
@math heading="Three losses at 2% of current equity" items="0.98 × 0.98 × 0.98 = 0.9412@point nine eight;;account at 94.1% of start@ninety four point one;;drawdown = 5.9%@five point nine"
Here's the lesson's example. Three consecutive losses, at a fixed two percent of current equity. Each loss leaves ninety eight percent of the balance. So multiply point nine eight by itself three times. That's point nine four one two. The account is at ninety four point one percent of its start, a five point nine percent drawdown.

@words text="5.9%, not 6%" sub="each loss is taken from a smaller balance"
That's slightly less than three times two percent, because each loss is taken from a smaller balance. Six percent is the fixed dollar answer: three losses of the same thousand dollars on a fifty thousand dollar account.

@math heading="Recovery needed" items="1 ÷ 0.9412 − 1 = 6.2%@six point two"
And to recover, you need one divided by point nine four one two, minus one. That's a gain of six point two percent. Already, the climb back is a little bigger than the fall.

@chapter Recovery asymmetry
@art recovery
That gap is called recovery asymmetry. A percentage loss requires a larger percentage gain to return to the prior peak. Small losses hide it. Big losses make it impossible to ignore.

@math heading="After a 50% loss" items="remaining = ½ of the start@half;;✗  +50% → ¾ of the start@a quarter;;✗  +75% → 87.5% of the start@eighty seven and a half;;+100% → back to the start@doubling"
After a fifty percent loss, what gain gets you back? Half the account remains. A fifty percent gain on that half is only a quarter of the original, so you're at three quarters. Seventy five percent brings you to eighty seven and a half percent of the peak. Only doubling, a hundred percent, gets back to it.

@words text="Measure recovery, not only drawdown"
So the lesson's advice is to use the recovery percentage, not only the drawdown percentage. The recovery number is the one you actually have to earn.

@chapter What makes a streak hurt
@art streak
What makes a losing streak most damaging? Large risk per trade. Large per trade risk compounds the drawdown much faster. Low trade frequency doesn't change the depth of a streak of a given length. And a written stop is the control, not the damage. It bounds each loss.

@words text="Stress-test at least 10 losses in a row"
That's why the lesson says to stress test at least ten consecutive losses. Choose a percentage that remains acceptable through a realistic losing streak, not just through one bad trade.

@chapter Where people slip
@list heading="Common mistakes" items="Fixed dollars while equity falls@The first|Increasing risk to recover faster@The second|Judging risk from one trade@the third"
Three mistakes. The first is using a fixed dollar amount while equity falls. The second is increasing risk to recover faster. That's the escalation the lesson warns against. And the third is evaluating risk from one trade, instead of a sequence.

@art one-vs-sequence
That last one is the root of the others. One trade at a big percentage can look harmless. It's the sequence that does the damage.

@list heading="Practical rules" items="Risk a % of current equity@a percentage|Stress-test 10 losses@stress test|Lower risk after drawdown@lower risk"
So express risk as a percentage of current equity. Stress test at least ten losses in a row. And lower risk after drawdown, rather than increasing it.

@chapter Try it
@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. Its steps are: select a survivable percentage, recalculate from current equity after each loss, and measure recovery.

@words text="Ten losses at your %: drawdown? recovery?"
For practice, pick a risk percentage and run ten losses in a row in the lab. Before it shows you, estimate the drawdown, then the gain you'd need to recover. Then try half the percentage.

@end text="Survive the streak first"
You can stress test your own risk percentage in the lab, on Learn. That's learn dot get er done dot I O.
