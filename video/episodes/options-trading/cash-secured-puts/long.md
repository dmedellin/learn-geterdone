---
format: long
lesson: options-trading/cash-secured-puts
title: Cash-secured puts: getting paid to agree to buy
thumb: Paid to agree to buy
---

@chapter The question
@title text="Cash-Secured Puts" sub="Options Trading" art=thumb
What if someone paid you today for agreeing to buy a stock later, at a price you choose? That's a cash secured put. The premium is real. So is the promise you've made in return.

@words text="Short put + cash set aside"
A cash secured put is a short put with the purchase cash set aside. You take a premium now for agreeing to buy the shares at the strike, and you reserve enough cash to actually do it.

@chapter The structure
@art cash-reserve
The cash is the security. Set aside enough to buy the shares the short puts represent, at the strike. For a standard contract that's the strike times one hundred, times the number of contracts. Real planning also uses the exact deliverable and your broker's requirements.

@art agree-to-buy
And only sell the put when assignment at the strike is financially and strategically acceptable. If the stock falls below the strike, you can be required to make the full purchase at the strike, even after a large decline. The strike you choose is the price you're promising to pay, so choose it as a purchase price, not as a premium number.

@chapter Four numbers
@math heading="From strike and premium" items="Cash reserved = strike × 100 × contracts@cash reserved;;Effective purchase price = strike − premium@effective purchase price;;Max profit = premium × 100@maximum profit;;Stock-to-zero loss = (strike − premium) × 100@goes to zero"
Every cash secured put comes down to four numbers. The cash reserved is the strike times one hundred, times the contracts. The effective purchase price is the strike minus the premium. The maximum profit is the premium, times one hundred. And if the stock goes to zero, the loss is the strike minus the premium, times one hundred.

@words text="Effective price = breakeven = basis if assigned"
That effective purchase price does two jobs. It's the expiration breakeven, and it's your net share basis if you're assigned. Fees come off it too, in real planning.

@chapter Worked with the course's numbers
@math heading="Short 100 put at $4.00, one contract" items="Cash reserved: 100 × 100 = $10,000@ten thousand;;Effective price: 100 − 4 = $96@ninety six;;Max profit: $4.00 × 100 = $400@four hundred;;Stock to zero: (100 − 4) × 100 = $9,600@ninety six hundred"
Take the short put from the Calls and Puts lesson: a one hundred strike at four dollars, one contract. The cash reserved is ten thousand dollars. The effective purchase price is ninety six. The maximum profit is four hundred. And the stock to zero loss is ninety six hundred dollars.

@art payoff-short-put
On a chart, it's flat at the full premium at or above the strike. Below the strike, it slopes down, dollar for dollar, crossing zero at the effective price. The loss is bounded, by the effective purchase price, because a stock can't fall below zero. But it's substantial.

@art reward-vs-risk
Limited reward, substantial risk. The most you can make is the premium. The most you can lose is close to the whole cash reserve. Keep both numbers in front of you, not just the first one.

@chapter Plan it
@art put-plan
Write the plan down before you sell anything. Four checks, every time, in the same order.

@list heading="Plan a cash-secured put" items="Confirm willingness to own shares@Confirm|Reserve sufficient cash@reserve|Calculate effective basis@calculate|Plan assignment and exit@plan"
So the plan goes in order. Confirm you're willing to own the shares. Reserve sufficient cash, using the deliverable, the strike, the quantity and your broker's requirements. Calculate the effective basis. And plan assignment and the exit: decide whether you'll close, roll, accept the shares, or avoid expiration, before you enter.

@chapter Where people slip
@list heading="Common mistakes" items="Treating premium as free income@The first|Choosing a strike for high premium@The second|Using cash needed elsewhere@The third"
The first mistake is treating the premium as free income. It's compensation for accepting downside and assignment risk. The second is choosing a strike just for a high premium. Higher premium often comes with a greater chance, and severity, of assignment. And the third is using cash you need elsewhere.

@art cash-locked
That last one bites at the worst time. Assignment can consume the reserved capital during a market decline, exactly when you might want that cash for something else.

@chapter Try it
@words text="Cash · effective price · max profit · stock-to-zero loss"
Your turn. From strike and premium alone, state the cash a cash secured put reserves, its effective purchase price, its maximum profit, and its stock to zero loss. Then say what the loss is bounded by. Do all four without the chart, and only then drag the expiration price to check.

@end text="Drag the expiration price"
You can set strike and premium and drag the expiration price, on Learn. That's learn dot get er done dot I O.
