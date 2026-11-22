---
format: long
lesson: options-trading/long-calls-and-long-puts
title: Long calls and long puts: planning a defined-risk directional trade
thumb: Risk the premium, plan the exit
---

@chapter The question
@title text="Long Calls and Long Puts" sub="Options Trading" art=thumb
You think a stock is going to move, and you want to express that with an option. A long call for up, a long put for down. The risk is simple to state. What the option is worth along the way is not.

@words text="A long option risks its premium"
The lesson puts it in one sentence. A long option risks its premium, and what it's worth before expiration is a separate question. Keep those two apart and most of the planning follows.

@chapter Long call
@art call-payoff-long
A long call seeks upside participation. The premium you paid is at risk, and at expiration there's no fixed maximum profit. The higher the stock finishes above the breakeven, the more it makes.

@math heading="Long call at expiration" items="Breakeven = strike + premium@strike plus the premium;;Max loss = premium × 100 × contracts@premium times;;Max profit: no fixed cap@no fixed"
At expiration, the breakeven is the strike plus the premium. The maximum loss is the premium, times one hundred, times the number of contracts. And there's no fixed cap on the profit.

@chapter Long put
@art put-payoff-long
A long put seeks downside participation, again with the premium at risk. Its maximum profit is substantial, but limited, because a stock can only fall as far as zero.

@math heading="Long put at expiration" items="Breakeven = strike − premium@strike minus the premium;;Max loss = premium × 100 × contracts@premium;;Max profit = (strike − premium) × 100@stock goes to zero"
Its breakeven is the strike minus the premium. The maximum loss is again the premium paid. And the maximum profit is the strike minus the premium, times one hundred, reached if the stock goes to zero.

@chapter Before expiration
@art curve-over-kink
Now the part that a payoff chart hides. Before expiration, the option's value can differ a lot from its intrinsic value, because time and implied volatility remain. On a chart, the value today is a smooth curve that sits above the bent expiration line.

@words text="Below breakeven, weeks before expiry" sub="Not necessarily losing"
So here's the drill's question. A position is below its breakeven, weeks before expiry. Is it necessarily losing? No. The expiration breakeven only applies at expiration. Weeks earlier, remaining time and volatility can leave the option worth more, or less, than that line suggests.

@art exit-model
That's why the lab models an exit separately. You set an entry, then choose an exit stock price, an exit date, and an exit implied volatility, and compare the modeled value with the expiration line. A planned early exit is priced by time and volatility, not by the breakeven.

@chapter Build the plan
@list heading="Plan a long option" items="State the directional thesis@State|Choose strike and expiration@choose the strike|Set maximum premium risk@set the maximum|Define exit conditions@define"
A direction forecast is not enough. State the directional thesis: a call for bullish exposure, a put for bearish. Then choose the strike and expiration, matching delta, premium and days to expiration to the move you expect and its timing. Then set the maximum premium risk. And define the exit conditions.

@art risk-budget
Size the position from the debit that can be lost, not from the profit you hope for. The premium is the most you can lose, so it's the number your risk budget has to approve.

@art exit-signs
Then write the exits down before you enter. A stock price that invalidates the idea. A profit objective. A time stop, because a long option loses value as days pass. And a decision about any event before expiration, since implied volatility can move sharply around it.

@chapter Where people slip
@list heading="Common mistakes" items="Buying far OTM because it's cheap@The first|Only the expiration breakeven for an early exit@The second|Risking the entire premium by default@The third"
The first mistake is buying far out of the money just because it's cheap. Low delta and limited time can need an unusually large and fast move. The second is using only the expiration breakeven to plan an early exit. The third is risking the entire premium by default. You can exit before a full premium loss when the thesis is invalidated.

@chapter Try it
@words text="Breakeven · max loss · why an early exit is different"
Your turn. From strike and premium, state a long option's expiration breakeven and its maximum loss. Then explain why an exit before expiration is priced by time and volatility, rather than by that breakeven. The lab's model is simplified, so treat its values as a reference, not a quote.

@end text="Model an early exit"
You can set an entry, model an exit, and compare it with the expiration line, on Learn. That's learn dot get er done dot I O.
