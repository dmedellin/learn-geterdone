---
format: long
lesson: options-trading/calls-and-puts
title: Calls and puts: four positions from one strike
thumb: Four positions, one strike
---

@chapter The question
@title text="Calls and Puts" sub="Options Trading" art=thumb
There are two contract types, calls and puts, and each one has two sides, long and short. That's four positions. Take one strike and one premium through all four, and you'll see exactly where each one makes money, where it loses, and which one has no limit on its loss.

@art four-payoffs
Start with the definitions. A call gives its holder the right to buy the underlying at the strike. A put gives its holder the right to sell the underlying at the strike. Long positions pay premium for those rights. Short positions receive premium and accept the obligations.

@words text="100 strike · $4.00 premium · one contract"
The lesson's worked example uses a strike of one hundred, a premium of four dollars, and one contract. Same numbers, four positions, so the arithmetic is done once in the open.

@chapter Long call
@art long-call-payoff
The long call first. You paid the premium for the right to buy at one hundred. Below the strike the call expires worthless and you lose what you paid. Above it, every dollar the stock rises adds to the payoff.

@math heading="Long call" items="Breakeven = 100 + 4 = $104@strike plus premium;;Max loss = $4.00 × 100 = $400@cannot exceed;;At $110: (10 − 4) × 100 = +$600@at one hundred and ten;;Max profit: uncapped@uncapped"
Breakeven is strike plus premium, one hundred and four. The loss cannot exceed the four dollars times one hundred you paid, so four hundred dollars. At one hundred and ten, the P and L is ten minus four, times one hundred: plus six hundred. And the maximum profit is uncapped.

@chapter Long put
@art long-put-payoff
The long put is the mirror. It gains as the stock falls. But a stock can only fall to zero, so its profit has a ceiling.

@math heading="Long put" items="Breakeven = 100 − 4 = $96@strike minus premium;;Max profit = (100 − 4) × 100 = $9,600@goes to zero;;At $110: expires worthless, −$400@expires worthless"
Breakeven is strike minus premium, ninety six. The most it can make is one hundred minus four, times one hundred, ninety six hundred dollars, if the stock goes to zero. Maximum loss is the four hundred paid. At one hundred and ten the put expires worthless, and you're down four hundred.

@chapter The short side
@art short-call-cliff
Now the writers. The short call has the same breakeven as the long call, one hundred and four, because the holder's breakeven is the writer's. Its maximum profit is the four hundred dollar premium. But above one hundred and four, every dollar is the writer's loss, with no ceiling.

@math heading="Short call and short put" items="Short call at $110: (4 − 10) × 100 = −$600@four minus ten;;Short put: breakeven $96, max profit $400@short put;;Short put max loss: $9,600@ninety six hundred"
At one hundred and ten, the short call is four minus ten, times one hundred: minus six hundred. The short put has a breakeven of ninety six and a maximum profit of four hundred. Its maximum loss is ninety six hundred dollars.

@art short-put-floor
The short put writer keeps the premium at or above the strike. Below it, the writer buys the stock at one hundred. At one hundred and ten, the put expires worthless, and the writer keeps the full four hundred.

@chapter Where people slip
@list heading="Common mistakes" items="Calls are always bullish@The first|Ignoring premium in breakeven@The second|Expiration payoff at every moment@And the third"
The first mistake is treating calls as bullish in every case. A long call is bullish, but a short call is neutral to bearish, and it carries very different risk. The second is ignoring premium in breakeven. And the third is using the expiration payoff for every moment.

@art breakeven-gap
Take the second one. Anywhere between one hundred and one hundred and four, the long call is in the money, but it hasn't yet covered the four dollars you paid, so the position is still losing. Being in the money doesn't necessarily mean the position is profitable.

@words text="Before expiration: time value and IV"
And the third. These straight lines are the payoff at expiration. Before expiration, time value and implied volatility also affect the option's price, so what a position is worth today sits off the expiration line. Later lessons take those two apart.

@chapter Try it
@words text="Breakeven and max loss, all four" sub="Which one has no cap?"
Here's the test. From strike and premium alone, give the breakeven and the maximum loss of each of the four positions, and name the one whose loss has no cap. Then work out a short put's P and L at a price, before you open the chart.

@end text="Drag the expiration price"
You can choose a position and drag the expiration price, on Learn. That's learn dot get er done dot I O.
