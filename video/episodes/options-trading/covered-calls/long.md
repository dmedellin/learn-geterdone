---
format: long
lesson: options-trading/covered-calls
title: Covered calls: income now, upside capped, downside kept
thumb: The premium isn't protection
---

@chapter The question
@title text="Covered Calls" sub="Options Trading" art=thumb
You own shares, and you sell a call against them. Someone pays you a premium today. What did you actually give up for it, and what didn't you give up? The answer to the second part is where people get caught.

@words text="Long shares + short call"
A covered call is long shares plus a short call. You take a premium now, and in exchange you hand over the upside above the strike. That's the whole trade in one sentence.

@chapter The structure
@art shares-plus-call
The call is covered because you own the shares it represents. A standard contract covers one hundred shares, so one call needs one hundred deliverable shares. Own the correct number of shares for the calls you sell. That's the first check.

@art strike-as-sale
And the strike isn't just a premium selection input. It's a potential sale price. If the call is assigned, your shares go at the strike. So the strategy is appropriate only when selling the shares at the strike is acceptable to you.

@chapter Breakeven and basis
@math heading="Adjusted basis" items="Breakeven = stock basis − premium@basis minus;;Premium lowers breakeven by the premium amount@lowers"
The premium you receive lowers your expiration breakeven by exactly the premium amount. So the breakeven is your stock cost basis, minus the call premium you received. Subtract premium from basis, and that's your adjusted basis.

@chapter The capped upside
@art capped-payoff
Now look at the payoff at expiration. Below the strike, the position rises and falls with the shares, shifted up by the premium. Above the strike, further stock gains are offset by the short call. The line goes flat.

@math heading="Maximum profit" items="Max profit = (strike − basis + premium) × 100@strike minus your basis;;Reached at or above the strike@at or above"
So the maximum profit is capped. It's the strike, minus your basis, plus the premium, times one hundred per contract. You reach it at or above the strike, and nothing more can be earned after that, however far the stock climbs.

@art versus-shares
Put the shares alone on the same chart and compare. Below the strike, the covered call sits above the shares by the premium. Above the strike, the shares keep climbing while the covered call stays flat. Somewhere above the strike, the shares alone pull ahead.

@chapter The downside you keep
@art downside-kept
And the downside? It stays with you. The shares still own every dollar of a fall. The premium offsets only a limited amount of stock loss, the premium itself, and nothing more.

@math heading="A $20 fall at expiration" items="Shares: −$20 per share@twenty dollars;;Call premium kept: + premium@keep;;P/L = (premium − 20) × 100@times one hundred"
That's the drill. Say the stock finishes twenty dollars below your basis, under the strike. The shares lose twenty dollars a share. The call expires worthless, and you keep the premium. So the result is the premium minus twenty, times one hundred. The fall is still almost all yours.

@words text="Not downside protection"
That's why a covered call isn't downside protection. It's a trade of upside for income, with the stock's downside left in place.

@chapter Assignment and exit
@art assignment-handoff
Plan assignment before you enter. If the stock is above the strike, the call can be assigned and the shares leave your account at the strike. Know how dividends, early assignment and expiration can affect the stock position.

@list heading="Plan a covered call" items="Confirm share coverage@confirm|Choose an acceptable strike@acceptable strike|Calculate adjusted basis@calculate|Plan assignment and exit@plan"
So the plan has four steps, in order. First, confirm share coverage, the right number of deliverable shares for the calls you sell. Second, choose an acceptable strike, a price you'd genuinely be willing to sell at. Third, calculate the adjusted basis. And fourth, plan assignment and the exit, before the trade is on rather than after.

@chapter Where people slip
@list heading="Common mistakes" items="Selling calls on shares that must not be sold@The first|Calling it downside protection@The second|Ignoring tax and account consequences@The third"
The first mistake is selling calls on shares that must not be sold, because assignment can remove them at the strike. The second is calling the strategy downside protection. And the third is ignoring tax and account consequences. Assignment and share disposition can have account specific effects that need professional review.

@chapter Try it
@words text="Breakeven · max profit · loss on a fall"
Your turn. Compute a covered call's breakeven, its capped maximum profit, and its loss on a fall. Then say, in your own words, why the premium is not downside protection.

@end text="Compare it with the shares alone"
You can set basis, strike and premium, and compare the position with the shares alone, on Learn. That's learn dot get er done dot I O.
