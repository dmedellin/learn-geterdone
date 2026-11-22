---
format: long
lesson: trade-setup-execution/position-sizing
title: Position sizing: quantity is an output, not a choice
thumb: Risk first, quantity last
---

@chapter The question
@title text="Position Sizing" sub="Trade Setup & Execution" art=thumb
How many shares should you buy? Lots of people answer from conviction. A big position when they feel sure, a small one when they don't. This lesson takes that choice away from feelings entirely.

@words text="Quantity is an output"
The position quantity is an output of your risk rules, not an input chosen from conviction. You set the risk budget first, and the quantity falls out of it. Widen the stop and watch the quantity fall.

@words text="Process and measurement" sub="no live data, no recommendations, no signals"
As with the rest of this course, it teaches process and measurement. It doesn't give live market data, personal recommendations, or trade signals.

@chapter Three ideas
@art budget-first
First, the risk budget. Choose the maximum account loss for this trade before you calculate anything. It can be a predefined percentage of equity, or a fixed dollar amount. Either way, what matters is that the number is decided before you ever look at the quantity it produces.

@art per-unit
Second, per unit risk. For each share or contract, include the loss from entry to stop, plus reasonable trading costs. Slippage and fees belong in the number.

@art round-down
And third, round down. Use whole tradable units, without ever going over the risk budget. Never round up past it. Rounding up by even one unit means the loss at your stop would be bigger than the budget you chose, and the budget stops meaning anything.

@chapter Shares
@math heading="Shares" items="account risk = equity × risk %@equity times;;shares = floor(account risk ÷ (|entry − stop| + cost per share))@entry to stop"
For shares, the account risk is equity times your risk percentage. Divide it by the per share risk, the distance from entry to stop plus the estimated slippage and fees per share, and round down. Floor just means round down to a whole number.

@art stop-widens
This is why a wider stop means fewer shares. The budget stays fixed. The per share risk grows. So the quantity shrinks. You never tighten the stop to make the number bigger. The stop comes from structure, as the stop placement lesson showed, and the size simply follows.

@chapter Long options
@math heading="Long options" items="contracts = floor(account risk ÷ planned loss per contract)@planned premium loss"
For a long option, the per unit loss is the planned premium loss, from the premium you paid to your planned premium exit, plus the round trip costs per contract. Divide the account risk by that planned loss per contract, and round down.

@art option-path
But there's a limitation. An underlying price stop doesn't map to one guaranteed option price. Delta, gamma, implied volatility, time decay, the spread, and gaps can all change the premium you actually exit at.

@chapter Check before you trade
@art concentration
The last step is a sanity check. Check concentration and liquidity. A trade sized correctly for risk can still be too concentrated in one position, or too difficult to execute.

@words text="Notional ÷ account" sub="what fraction of the account is in this position?"
So the lesson asks one more question: what fraction of the account is the position's notional? Risk tells you what you can lose at the stop. Notional tells you how much of the account is exposed.

@chapter Where people slip
@list heading="Common mistakes" items="Choosing quantity before the stop@The first|Ignoring gaps and slippage@The second|Treating option premium as one-to-one@The third|Using maximum buying power as size@And the fourth"
The first mistake is choosing the quantity before the stop. The second is ignoring gaps and slippage. Actual losses can exceed the planned stop distance, especially around events or in illiquid instruments. The third is treating option premium and underlying movement as one to one. And the fourth is using maximum buying power as the position size. Available leverage isn't acceptable loss.

@words text="The plan can be exceeded" sub="gaps · events · illiquid instruments"
That second one is a reminder that the stop is a plan, not a promise. Price can gap past it. So the budget is the loss you plan for, and the real loss can occasionally be larger.

@chapter Try it
@words text="Equity · risk % · entry · stop · costs → quantity"
Here's the lesson's standard. Turn equity, a risk percentage, an entry, a stop and costs into a rounded down quantity, of shares or of contracts. Never rounded up past the budget. And say what fraction of the account the position's notional is.

@end text="Size a position yourself"
You can set a budget, move the stop, and watch the quantity change, on Learn. That's learn dot get er done dot I O.
