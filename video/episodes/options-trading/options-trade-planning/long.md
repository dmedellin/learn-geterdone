---
format: long
lesson: options-trading/options-trade-planning
title: Options trade planning: thesis, structure, contract, risk, exit
thumb: Thesis first, every time
---

@chapter The question
@title text="Options Trade Planning" sub="Options Trading" art=thumb
You've learned contracts, premiums, the Greeks and a handful of strategies. Now, how do you put them together into one trade you'd actually be willing to place? The answer is an order of operations, and it's the same every time.

@words text="Thesis → structure → contract → risk → exit"
Thesis, structure, contract, risk, exit. In that order, every time. Use the same sequence for every candidate, so weak plans get rejected before entry, not after.

@chapter The thesis comes first
@art thesis-first
The option is the instrument you use to express a market thesis. It doesn't replace the thesis. So start with the underlying, not the option chain. If you start with the chain, the contracts that happen to be available end up creating the idea.

@list heading="Define the thesis" items="Direction@direction|Target@target|Invalidation@invalidation|Expected duration@expected duration|No-trade conditions@no trade"
State the thesis in full. The direction. The target. The invalidation, the price that says you're wrong. The expected duration. And the no trade conditions, the situations where you simply stay out.

@chapter Choose the structure
@art structure-fit
Next, choose the strategy. Match its directional and volatility exposure to the thesis. Direction, target, timing, implied volatility, strike geometry and liquidity all have to be consistent with each other. A strategy that fits the direction but fights the timing isn't a fit.

@chapter Select the contract
@art contract-check
Then select executable contracts. Verify the expiration against the thesis duration, the strikes against the target, the bid ask spread, the quantity, and any event before expiration. Everything from the chain and liquidity lesson applies here.

@chapter Approve the risk
@art risk-scale
Now the risk. Confirm the maximum loss, the account risk, the target payoff, any assignment exposure, and the exit rules. Maximum position risk, invalidation, event handling and exit conditions must all be written before entry.

@words text="Share-backed: the loss if invalidation is hit"
For a share backed position, the drill asks which figure the risk budget compares. It's the one Trade Setup and Execution defined: the loss if the invalidation is hit. That's the number your maximum risk percent of account equity has to cover.

@chapter Write the exit
@art exit-rules
And last, the exit. Write it down before you enter, as rules rather than intentions. The stock price that invalidates the thesis. The profit objective. A time stop, because an option's extrinsic value runs out. And what you'll do about any event before expiration, and about assignment if the position is short.

@words text="An exit rule is part of the plan" sub="not something you decide later"
The rule is the same as for risk: it's written before entry. Decide the exit once the trade is already moving, and it stops being part of the plan and becomes a reaction to whatever the price just did.

@chapter Score the plan
@art ten-checks
The lesson's lab turns this into a plan you can score. You fill in direction, strategy, stock price, target, invalidation, duration, expiration, strikes, premium, the displayed bid and ask, quantity, account equity, maximum risk percent, implied volatility context, events, and an exit rule. Then it evaluates the plan against ten checks.

@words text="Start with the bullish preset" sub="every check prints its own arithmetic"
Evaluate the bullish preset first. It's the worked example, and every check prints its own arithmetic, so you can see exactly why each one passes or fails. Then build your own and export the result.

@chapter Where people slip
@list heading="Common mistakes" items="Starting with the chain, not a thesis@The first|Optimizing one metric@The second|Changing risk after entry@The third"
The first mistake is starting with an option chain instead of a thesis. The second is optimizing one metric. High delta, low premium, or high probability alone can't validate the full plan. And the third is changing risk after entry. Risk limits and invalidation lose their value when they're adjusted only to avoid realizing a loss.

@chapter Try it
@words text="A plan the ten checks approve" sub="or the check that fails, and the fix"
Your turn. Take a thesis written the way Trade Setup and Execution taught. Choose the structure, and produce a plan the ten checks approve. Or, if one fails, name the check that fails and what would fix it. The lab's values come from a simplified model, so treat them as a reference.

@end text="Score a full options plan"
You can load a preset, fill in a plan and score it against ten checks, on Learn. That's learn dot get er done dot I O.
