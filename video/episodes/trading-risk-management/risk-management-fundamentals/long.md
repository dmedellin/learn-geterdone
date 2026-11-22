---
format: long
lesson: trading-risk-management/risk-management-fundamentals
title: Risk management fundamentals: what you control, and what you don't
thumb: Exposure is the dial you set
---

@chapter The question
@title text="Risk Management Fundamentals" sub="Trading Risk Management" art=thumb
You've found a setup you really like. Everything lines up. And it still loses. Was the setup wrong? Not necessarily. That single fact is where risk management starts.

@words text="The outcome is uncertain" sub="your exposure is the controlled variable"
The market outcome is uncertain. Your exposure is the controlled variable. A valid setup can still lose. Risk management limits the account damage when price doesn't follow the thesis.

@chapter Two kinds of variable
@art control-split
Every trade has two kinds of variable. The ones you set, and the ones you absorb. You can control position size, your planned exit, your total exposure, and whether a trade is taken at all.

@art paths
What you can't control is the next price move, gaps, news, or the order in which wins and losses arrive. Those are the market's.

@words text="Position size" sub="set before entry"
So which variable is directly controlled before entry? Position size. Not the next candle, because nothing you do before entry changes what it prints. And not market volatility. Volatility is a property of the market you're entering, not a setting you choose.

@chapter A strong setup loses
@art fan
Now, a strong setup loses. What does that prove? That losses can occur within a valid process. A setup is a probability, not a promise. One loss is a single draw from its distribution, and says almost nothing about its validity.

@words text="Losses are part of the distribution"
And it doesn't prove that risk rules are unnecessary. It's the opposite. Because a valid setup still loses, each loss has to be sized so that it's survivable. That's what the rules are for.

@chapter Survival first
@art survival
So what's the first objective of risk management? Not to maximise every winner. Winners are the uncontrolled side. And not to avoid all losing trades, because no process does that. The objective is to keep losses survivable.

@words text="Keep losses survivable"
A strategy can only produce long term results if normal losses don't remove the ability to continue. Risk management keeps individual and accumulated losses within planned limits.

@chapter In dollars, before entry
@list heading="Apply it in order" items="Define the invalidation@define the invalidation|Convert it to dollars@convert it to dollars|Check total exposure@check total exposure"
Risk calculations should happen before the order is submitted, in three steps. First, define the invalidation, the price condition that proves the thesis wrong. Then convert it to dollars: the distance from entry to invalidation, times position size. Then check total exposure, including open positions, correlation, leverage, and execution risk.

@art exposure-stack
That last step matters because a trade never lands on an empty account. Whatever is already open is part of the risk, and the new position adds to it. Later lessons in the course work through each of those pieces.

@math heading="Equity $40,000 · risk 1.25%" items="$40,000 × 1.25%@forty thousand times one;;= $40,000 × 0.0125@point zero one two five;;= $500@five hundred dollars"
Here's the lesson's example. Equity is forty thousand dollars, and risk per trade is one and a quarter percent. Forty thousand times one and a quarter percent is forty thousand times point zero one two five. That's five hundred dollars.

@math heading="Not these" items="✗  $400 = 1%@four hundred;;✗  $5,000 = 12.5%@five thousand"
Four hundred would be one percent. One and a quarter percent is a quarter more than that. And five thousand reads the percentage as twelve and a half, not one and a quarter. Move the decimal. That five hundred dollar figure is set before entry. The outcome isn't.

@chapter Where people slip
@list heading="Common mistakes" items="Letting confidence increase size@The first|Moving the stop because it's losing@The second|Measuring risk after the position is open@the third"
Three mistakes. The first is assuming confidence should increase position size. The second is moving the stop because the trade is losing. And the third is measuring risk only after the position is open.

@art entry-stop
The rules that guard against them are simple. Define maximum loss before entry. Calculate position size from the stop distance. And treat unexpected gaps and slippage as additional risk, on top of the plan.

@chapter Try it
@words text="Synthetic educational data" sub="no live market connection"
The lesson's lab uses simplified synthetic examples, with no live market connection. Adjust the controls, then read the market behaviour and the account impact after each change.

@words text="Your equity × your risk % = ?"
For practice, take your own account size, or a made up one, and pick a risk percentage. Work out the planned loss in dollars, by hand, before you go any further. That's the number you'd set before any entry.

@end text="Set the loss before the trade"
You can change the risk conditions and watch the account impact, on Learn. That's learn dot get er done dot I O.
