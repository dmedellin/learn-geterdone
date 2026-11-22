---
format: long
lesson: trade-setup-execution/entry-confirmation
title: Entry confirmation: the first candle that meets your rule
thumb: The first candle that qualifies
---

@chapter The question
@title text="Entry Confirmation" sub="Trade Setup & Execution" art=thumb
You've found a setup, at the right place, in the right direction. Now which candle do you actually enter on? If you can't answer that before it happens, you'll end up picking whichever candle looks best afterwards.

@words text="The first candle that satisfies the written rule"
This lesson's answer is precise. The entry is the first candle that satisfies the model you wrote down, not the candle that later looks best.

@words text="Process and measurement" sub="no live data, no recommendations, no signals"
As with the rest of this course, it teaches process and measurement. It doesn't give live market data, personal recommendations, or trade signals.

@chapter Three ideas
@list heading="Core concepts" items="An exact entry rule@exact event|A timing trade-off@trade off"
First, the entry rule is an exact event, such as a close, a structure shift, acceptance, or a successful retest. Second, there's a timing trade off. Earlier entries improve price but use less evidence, and later entries do the opposite.

@words text="Same rule in replay, backtest and live"
Third, consistency. Apply the same confirmation definition in replay, in backtesting, and live. If your replay uses one definition and your live trading uses another, your test results describe a strategy you aren't actually trading. One definition, written once, used everywhere.

@chapter Three models
@art decision-area
The lab compares three models, written as rules, around a decision area. On the same chart, each one picks out a different candle, at a different moment.

@art reaction-close
The reaction close is the first close back in the trade's direction off the decision area. It's the earliest of the three, so it gets the best price, and it's also the one most often caught by a pullback that hasn't really finished.

@art shift-close
The structure shift is the first close beyond the last minor high the pullback made. On the breakout tab, it's the first close beyond the break candle's close, which is acceptance.

@art retest-close
And retest confirmation waits for price to return to the level, then takes the first close away from it again. It's the latest of the three. By then there's the most evidence, but price may already have moved away.

@chapter The trade-offs
@list heading="Confirmation trade-offs" items="Reaction close · earlier · low–medium evidence@Reaction close|Structure shift · middle · medium–high evidence@Structure shift|Retest · later · high evidence@Retest"
Here's the lesson's table. Reaction close: earlier, with low to medium evidence. Better price, more false starts. Structure shift: in the middle, with medium to high evidence, balancing price and confirmation. Retest: later, with high evidence, but a possible missed trade, or a worse price.

@art timing-line
None of these is right in general. They're three points on the same line, from early and cheap to late and well supported. The point is to choose one before the setup, and stick to it.

@chapter The process
@list heading="Entry confirmation process" items="Choose the model@Choose the model|Mark the trigger level@Mark the trigger level|Wait for completion@Wait for completion|Verify the trade still works@Verify the trade"
Choose the model before the setup. Mark the trigger level, with the price and timeframe you'll judge it on. Wait for completion. And verify the trade still works.

@art wick-not-close
Waiting for completion means just that. If the rule says a close, an intrabar wick through the trigger doesn't count. Then, once it's confirmed, recalculate the invalidation distance and the room to the target. A confirmed setup can still be a no trade if the entry is now too late.

@chapter Where people slip
@list heading="Common mistakes" items="Any favorable candle as confirmation@The first|Switching from retest to breakout@The second|Entering after confirmation destroys reward@The third|Assuming more confirmation guarantees success@And the fourth"
The first mistake is treating any favorable candle as confirmation. It has to satisfy the specific rule. The second is changing from retest to breakout after a missed trade, which makes historical results impossible to compare honestly. The third is entering after confirmation has destroyed the reward. And the fourth is assuming more confirmation guarantees success. It changes evidence and timing, not certainty.

@chapter Try it
@words text="For each model, the first qualifying candle" sub="on every tab"
Here's the lesson's standard. For each model, pick the first candle that satisfies its written rule, on every tab. That includes the losing entry the reaction model takes on the failed tab. And it includes no valid entry at all, for the two models that tab never completes.

@end text="Find the entry candle"
You can pick the entry candle for each model on four practice tabs, on Learn. That's learn dot get er done dot I O.
