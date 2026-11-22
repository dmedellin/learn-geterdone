---
format: long
lesson: backtesting-and-trading-systems/survivorship-selection-and-corporate-actions
title: Survivorship bias and stock splits: the backtest that only remembers winners
thumb: Test what existed then
---

@chapter The problem
@title text="Survivorship, Selection, and Corporate Actions" sub="Backtesting and Trading Systems" art=thumb
Say you want to test a stock strategy over ten years. You download today's index members and run the rule. It looks great. The trouble is in that first step.

@art survivors-only
Today's members are the survivors. The companies that failed, got delisted, or went bankrupt along the way aren't in the list. They were investable at the time, but your test never sees them. So the test quietly removes the failures.

@words text="What was actually available, at each point in time"
The lesson's principle is this. A historical universe must contain what was actually available at each point in time. Keep only today's survivors and you remove failures. Select assets after seeing their returns, and the test knows the future.

@chapter Two biases
@art failures-included
Survivorship bias is the first one. Exclude failed instruments and historical performance usually looks stronger, because the worst outcomes have been cut out before the test began.

@art cherry-pick
Selection bias is the second. Choosing markets or periods after reviewing the results changes the question being tested. You're no longer asking whether the rule works. You're asking whether it works on the places you already know it worked.

@chapter The point-in-time universe
@list heading="Reconstruct the investable set" items="Date membership@Date membership|Include failures@include failures|Adjust correctly@adjust correctly"
The fix is to treat universe membership as data, not a static list. Date membership: record when each instrument entered and left the universe. Include failures: keep delistings, bankruptcies and unavailable periods. And adjust correctly, which brings us to corporate actions.

@art membership-timeline
With point in time membership, the system on any historical date only knows the constituents available on that date. It can't use future knowledge of who joined, who left, or who survived. And for a name that was delisted while you held it, include the delisting return, or a documented conservative treatment, rather than letting the position silently vanish.

@chapter Splits
@art split-cliff
Corporate actions are splits, dividends, mergers and delistings, and they must be handled consistently with the strategy. Take a two for one split. An unadjusted price series suddenly halves. To a backtest, that looks like a fifty percent loss that nobody actually took.

@math heading="SPLT splits two-for-one" items="quoted 111.33  →  55.66@one hundred and eleven point three three;;55.66 × 2 ÷ 111.33 − 1 ≈ 0%@times two;;unadjusted: −50%@Unadjusted"
Here's the lesson's example. A name called SPLT is quoted at one hundred and eleven point three three and splits two for one to fifty five point six six. Adjusted, the return is fifty five point six six, times two, divided by one hundred and eleven point three three, minus one. That's zero. Unadjusted, it's minus fifty percent.

@math heading="In an equal-weight portfolio of 8" items="−50% ÷ 8 = −6.25 points@divided by eight"
And it doesn't stay in one name. In the lab's equal weight portfolio, that false minus fifty percent, divided by eight, knocks six point two five points off the whole portfolio's step.

@art split-shares
Nothing about the value changed. A holder of one share at a hundred and ten dollars holds two at fifty five after the split. Doubling the share count without halving the price is just as wrong, in the other direction.

@words text="Price adjustment ≠ cash distributions"
Dividends need the same care. An adjusted price series folds past distributions into the price history, but a strategy that actually held the shares received cash on a particular day. Keep the two apart, and check whether your vendor prices are raw or adjusted before you trust either.

@chapter Where people slip
@list heading="Common mistakes" items="Today's index members for a ten-year test@The first|Removing bankrupt symbols as bad data@The second|Adjusted prices with unadjusted cash flows@And the third"
The first mistake is downloading today's index members for a ten year test. The second is removing bankrupt symbols as bad data, when they're the most important records you have. And the third is mixing adjusted prices with unadjusted cash flows. Keep price adjustment separate from real cash distributions and from trade execution.

@chapter Try it
@words text="Is your vendor's data raw or adjusted?"
For practice, check whether your price data is raw or adjusted, and how it treats delisting returns. Then, in the lab, which runs on deterministic synthetic educational data, toggle point in time membership, delisted symbols and split adjustment, and compare the honest portfolio with the biased one.

@end text="Compare the honest and biased portfolios"
You can toggle the universe and the split adjustment yourself, on Learn. That's learn dot get er done dot I O.
