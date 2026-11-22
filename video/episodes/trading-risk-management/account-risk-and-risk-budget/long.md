---
format: long
lesson: trading-risk-management/account-risk-and-risk-budget
title: Account risk and the risk budget: when valid trades add up
thumb: Risks add up
---

@chapter The question
@title text="Account Risk and Risk Budget" sub="Trading Risk Management" art=thumb
Three charts, three good setups, all at once. Each one, on its own, risks a sensible amount. So why can taking all three still break your plan?

@words text="Several setups can be valid at once" sub="but their risks accumulate"
Because several setups can be valid at the same time, but their risks accumulate. The market may offer multiple entries. The account experiences the combined open and realised risk, not each chart in isolation.

@chapter Three layers of risk
@art one-stop
Start with trade risk. That's the planned loss on one position, if its invalidation is reached.

@art open-stops
Next is open risk. That's the sum of the planned losses to every active stop. In other words, the loss to current planned stops, if every one of them were hit.

@words text="Open risk ≠ market value" sub="$50,000 position · stop 1% away → $500 open risk"
Open risk isn't the maximum profit on your trades, and it isn't total market value. Market value is exposure. A fifty thousand dollar position with a stop one percent away carries five hundred dollars of open risk.

@art gate
And then there are loss limits. Daily and weekly limits stop new risk after a defined amount of damage.

@chapter Why three trades can be too many
@art three-blocks
So why can three trades exceed your intended budget? Because their planned losses add together. Each one contributes to total account risk.

@words text="Different tickers ≠ independent"
It isn't because they use different tickers. Different tickers don't make risks independent, and even independent stops still add. The correlation lesson later in this course adds the adjustment for positions that share a driver. Here, they simply add.

@chapter Does it fit?
@art budget-bar
Here's the lesson's example. The daily limit is one thousand dollars. Realised loss so far today is three hundred. Open risk to current stops is four hundred. The next setup needs a planned loss of three hundred and fifty. Does it fit?

@math heading="Daily limit $1,000" items="$1,000 − $300 realised@three hundred realised;;− $400 open@four hundred open;;= $300 available@three hundred available;;$350 > $300 → doesn't fit@doesn't fit"
One thousand, minus three hundred realised, minus four hundred open, leaves three hundred available. A planned loss of three hundred and fifty doesn't fit. Reduce its size until the full planned loss is three hundred or less, or pass.

@math heading="Not these" items="✗  $700 is under $1,000@seven hundred;;✗  fits if it has a 2R target@target"
The tempting wrong answer says seven hundred is under one thousand. But seven hundred is what's already committed. The question is whether seven hundred plus three fifty, ten fifty, stays under one thousand, and it doesn't. And a target doesn't change what a trade can cost. The budget is spent by planned losses.

@chapter When the budget is spent
@words text="Stop adding new risk"
You've used the full daily risk budget. What's the direct action? Stop adding new risk. That's the whole purpose of a limit: to prevent additional exposure after the budget is consumed.

@list heading="Not these" items="Increase size to recover@increase size|Remove all stops@remove all stops"
Two wrong answers are worth naming. Increase size to recover is the escalation the limit exists to prevent. And remove all stops converts bounded open risk into unbounded risk. It makes the day's damage larger, not smaller.

@chapter Where people slip
@list heading="Common mistakes" items="Treating buying power as risk budget@The first|Ignoring exposure already open@The second|Resetting the daily limit after one win@the third"
Three mistakes. The first is treating available buying power as risk budget. The second is ignoring exposure that's already open. And the third is resetting the daily limit after one winning trade.

@list heading="Practical rules" items="Set trade, open, daily and weekly limits separately@set trade|Count realised loss and open stop risk together@count realised|Leave reserve for slippage and gaps@leave reserve"
So set trade, open, daily, and weekly limits separately. Count realised losses and active stop risk together. And leave reserve for slippage and gaps.

@chapter Try it
@list heading="Apply it in order" items="Start with account equity@start with account equity|Reserve the budget@reserve the budget|Reduce shared exposure@reduce shared exposure"
The lab's order is this. Start with account equity, your current usable equity, not an old peak balance. Then reserve the budget, subtracting realised loss and open risk before adding another position. Then reduce shared exposure, since correlated positions can consume more budget than their count suggests.

@art peak-vs-current
That first step trips people after a drawdown. If the account has fallen from its peak, the limits come from where it is now. Basing them on the old peak would let you risk money you no longer have.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. Pick a daily limit, add a realised loss and some open risk, and work out how much room is left before you look.

@end text="Count what's already committed"
You can test your own risk budget in the lab, on Learn. That's learn dot get er done dot I O.
