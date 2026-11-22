---
format: long
lesson: options-trading/option-premium
title: Option premium: intrinsic value plus everything else
thumb: Intrinsic plus extrinsic
---

@chapter The question
@title text="Option Premium" sub="Options Trading" art=thumb
You see a call quoted at nine dollars twenty. What are you actually paying for? Part of that number is easy to explain. The rest is what the whole options course is really about.

@words text="Premium = intrinsic + extrinsic"
A premium is intrinsic value plus everything else. Split it into those two parts, and you can say which part the stock decides, and which part time and volatility decide.

@chapter The pieces
@art premium-bar
The premium is the market price the buyer pays and the seller receives, quoted per share. Intrinsic value is the amount the option is in the money, and it can't be negative. Extrinsic value is whatever the premium has on top of that.

@art two-drivers
Extrinsic value is priced chiefly by two things. The time remaining until expiration, and implied volatility, which is the model's assumption about how much the stock might move. Each gets its own lesson later in the course.

@chapter A worked example
@words text="100 call · stock $108 · 30 days · IV 30%"
Here's the lesson's worked example. A one hundred call, with the stock at one hundred and eight, thirty days left, and implied volatility at thirty percent, priced by the model the page uses.

@math heading="Split the premium" items="Intrinsic = max(108 − 100, 0) = $8.00@Intrinsic value;;Model premium = $9.20@the model;;Extrinsic = 9.20 − 8.00 = $1.20@extrinsic"
Intrinsic value is the larger of one hundred and eight minus one hundred, and zero: eight dollars. That part is the same whatever the time or volatility. The model premium is nine dollars twenty. So extrinsic is nine twenty minus eight: one dollar twenty.

@art split-bars
That one dollar twenty is what thirty days of possible further movement is priced at. A real quote would differ from the model's number, but the split works the same way: premium minus intrinsic is extrinsic.

@chapter At expiration
@art expiry-line
Now let time run out with the stock still at one hundred and eight. The option is worth eight dollars, just its intrinsic value. The one dollar twenty is what the clock removes. On the lesson's chart, the purple line is that expiration value at every stock price.

@art iv-dial
And in the lab, move the implied volatility slider. Only the extrinsic part changes. Raise implied volatility and the extrinsic part grows. Lower it and the extrinsic part shrinks. The eight dollars of intrinsic value doesn't move.

@art all-extrinsic
The same split works the other way round. An out of the money option has no intrinsic value, so its whole premium is extrinsic. And at expiration, with no time left, all of it is gone. That's the second case the drill asks you to handle.

@chapter Decompose any premium
@list heading="Four steps" items="Calculate intrinsic value@calculate intrinsic|Read the full premium@read the full premium|Subtract intrinsic@subtract|Identify the drivers@the drivers"
So for any quote: calculate intrinsic value from the stock and strike. Read the full premium, and when you're trading, use an executable quote, because a theoretical value is only a reference. Subtract intrinsic to get extrinsic. Then identify the drivers: time, implied volatility, rates, dividends, and market supply and demand.

@chapter Where people slip
@list heading="Common mistakes" items="Calling all premium time value@The first|Theoretical value as a fill price@The second|Forgetting the multiplier@And the third"
The first mistake is calling all premium time value. An in the money option can contain both intrinsic and extrinsic value, like this call. The second is assuming a theoretical value is a fill price. A model doesn't guarantee a bid, an ask, or an execution. And the third is forgetting the multiplier.

@math heading="Per contract" items="$9.20 × 100 = $920@nine twenty;;$1.20 × 100 = $120 of extrinsic@one hundred and twenty"
Premium per share normally gets multiplied by one hundred for a standard contract. So nine twenty is nine hundred and twenty dollars a contract, and one hundred and twenty dollars of that is extrinsic.

@chapter Try it
@words text="Split it both ways round"
Your turn. Split a quoted premium into intrinsic and extrinsic value, from the stock and the strike alone. Do it for an option with intrinsic value, and for one without. Then say which part is left at expiration. The model here is simplified: European Black Scholes, a fixed four point five percent rate, and no dividends.

@end text="Watch the premium split"
You can change the stock, strike, time and volatility, and watch the premium split, on Learn. That's learn dot get er done dot I O.
