---
format: long
lesson: trading-risk-management/position-sizing
title: Position sizing: turning a stop distance into a share count
thumb: Wider stop, smaller size
---

@chapter The question
@title text="Position Sizing" sub="Trading Risk Management" art=thumb
You know where your stop goes. You know how much you're willing to lose. So how many shares, or contracts, do you buy? That's position sizing, and it's three short calculations.

@words text="Wider move → smaller position" sub="same dollar risk"
The idea underneath is this. A wider market move requires a smaller position for the same dollar risk. The chart determines the stop distance. Position size converts that distance into a loss the account can tolerate.

@chapter Three quantities
@art budget
First, dollar risk. That's account equity multiplied by the risk percentage you've selected. It's your risk budget for the trade, in dollars.

@art unit-risk
Second, unit risk. That's the distance from entry to stop, multiplied by the instrument's value per point. For shares, one point is one dollar a share. For a futures contract, you need its multiplier.

@math heading="Position size" items="dollar risk = equity × risk %@equity times;;unit risk = |entry − stop| × value per point@distance from entry to stop;;quantity = dollar risk ÷ unit risk, rounded down@divided by unit risk"
And third, quantity. Dollar risk divided by unit risk, rounded down to a tradable amount. So dollar risk equals equity times risk percent. Unit risk is the distance from entry to stop, times the value per point. Quantity is dollar risk divided by unit risk, rounded down.

@chapter Costs belong in the unit
@art reserve
What else should go in with the stop distance? Estimated costs and slippage. Fees and slippage increase the effective loss per unit. Slippage is the distance between the stop price and the fill you actually receive. So you add a reserve per share for it.

@words text="Not the target · not past profits"
The target doesn't belong in this calculation. It's on the other side of the entry. And past profits don't change what this trade can cost.

@chapter Worked example
@math heading="Equity $40,000 · risk 1% · entry 52.00 · stop 50.00 · reserve 0.10" items="budget = $40,000 × 1% = $400@four hundred dollars;;per share = (52.00 − 50.00) + 0.10 = $2.10@two dollars ten;;$400 ÷ $2.10 = 190.5@one ninety point five;;round down → 190 shares@one hundred and ninety shares"
Here's the lesson's example. Equity forty thousand dollars, risk one percent, so the budget is four hundred dollars. Entry fifty two, stop fifty, plus a ten cent slippage reserve, so risk per share is two dollars ten. Four hundred divided by two ten is one ninety point five. Round down, to one hundred and ninety shares.

@math heading="Check" items="190 × $2.10 = $399@three hundred and ninety nine;;✗  200: divides by the bare $2.00@two hundred;;✗  191 × $2.10 = $401.10@over the budget"
One ninety shares risks three hundred and ninety nine dollars. Two hundred shares divides by the bare two dollar distance, and would risk four hundred and twenty. And one ninety one rounds up, putting four hundred and one dollars ten at risk, over the budget.

@chapter Why round down
@art round-down
So why round down? To preserve the maximum risk limit. Rounding down keeps planned risk at or below the budget. It doesn't improve win rate, because quantity has no effect on whether the trade works. And it doesn't remove slippage. The reserve handles that.

@chapter Double the stop
@art double-stop
Now, what happens to position size when the stop distance doubles? It usually halves. For the same dollar risk, doubling unit risk roughly halves quantity.

@words text="Double size × double distance = 4× loss"
The wrong instinct is to keep the size. Unchanged size with twice the distance is twice the dollar loss. And doubling the size when the stop doubles quadruples the loss: twice the shares, each losing twice as much.

@chapter Where people slip
@list heading="Common mistakes" items="Sizing from buying power@The first|Same share count for every setup@The second|Ignoring gaps, spread and commissions@the third"
Three mistakes. The first is sizing from buying power. The second is using the same share count for every setup, whatever the stop distance. And the third is ignoring gaps, spread, and commissions.

@art same-count
That second one is common. A fixed share count means a fixed risk only if every stop is the same distance away, and they never are.

@list heading="Practical rules" items="Stop distance before quantity@stop distance|Use the right multiplier@multiplier|Round down, then recalculate@round down"
So determine stop distance before quantity. Use the correct contract multiplier, or option premium multiplier. And round down, then recalculate your actual risk.

@chapter Try it
@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. It runs the same three steps: calculate the risk budget, calculate risk per unit, and round down.

@words text="Stop 48.00 instead of 50.00?"
For practice, keep the worked example's account, risk and entry, but move the stop down to forty eight. Work out the new risk per share with the same reserve, then the share count, then check it against the budget.

@end text="Budget, unit risk, round down"
You can size positions for your own examples in the lab, on Learn. That's learn dot get er done dot I O.
