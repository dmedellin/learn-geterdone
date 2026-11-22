---
format: long
lesson: options-trading/delta-and-gamma
title: Delta and gamma: the slope, and how fast the slope changes
thumb: Delta is a slope
---

@chapter The question
@title text="Delta and Gamma" sub="Options Trading" art=thumb
The stock moves five dollars. How much does your call move? Delta gives you a fast first answer. Gamma tells you why that first answer comes out too small on a big move.

@words text="Delta is a slope" sub="Gamma is how fast the slope changes"
That's the whole lesson in one line. Delta is a slope. Gamma is how fast the slope changes. Put the two together and you can estimate a move, and know which way your estimate is off.

@chapter Delta
@art price-curve
Picture the option's value plotted against the stock price. It's a curve. Delta estimates the option price change for a small change in the underlying, with the other inputs held constant. In other words, it's the slope of that curve where the stock is right now.

@art position-shares
Multiply delta by the contract multiplier and by the quantity, and you get position delta. That's your share equivalent directional exposure: roughly how many shares of stock your options behave like at this moment.

@chapter The worked example
@words text="100 call · 30 DTE · IV 30% · one contract" sub="stock $100 → $105"
The lesson's worked example is the lab's default state. A one hundred call, thirty days to expiration, implied volatility at thirty percent, one contract. The stock moves from one hundred to one hundred and five.

@math heading="Delta only" items="Delta = 0.534@zero point five three four;;0.534 × $5 × 100 = +$267@two hundred and sixty seven"
Delta now is zero point five three four. So the first order estimate is zero point five three four, times five dollars, times one hundred: plus two hundred and sixty seven dollars. That estimate assumes the slope holds for the whole five dollars.

@chapter Gamma
@art tangent-gap
But it doesn't. The curve bends upward, so the straight tangent line falls below it as the stock moves away. Gamma estimates how much delta changes for a one dollar move in the underlying. It's the correction for the slope changing along the way.

@art slope-steepens
Over the five dollars, delta climbs step by step, so each dollar of the move is worth a little more than the one before it.

@math heading="Delta plus gamma" items="Gamma = 0.0462@zero point zero four six two;;½ × 0.0462 × 5² × 100 = +$58@one half;;267 + 58 = +$325@three hundred and twenty five"
Gamma is zero point zero four six two, so delta rises about zero point zero four six per dollar. Add one half, times zero point zero four six two, times five squared, times one hundred. That's fifty eight dollars, giving plus three hundred and twenty five.

@chapter Full repricing
@math heading="Reprice the option" items="$3.61 → $6.83: +$322@three sixty one;;Delta after the move: 0.743@zero point seven four three;;Delta only: undershot by $55@undershot"
Now reprice the option in full. It goes from three sixty one to six eighty three, a gain of three hundred and twenty two dollars. Delta after the move is zero point seven four three. The linear estimate used zero point five three four the whole way, and undershot by fifty five dollars.

@art three-estimates
The gamma estimate overshoots slightly, by three dollars, because gamma itself changes as well. So you have three numbers: two sixty seven, three twenty five, and the full repricing, three twenty two. Estimates are for intuition. The full model is the better approximation.

@chapter Position delta
@math heading="Share equivalents" items="0.534 × 100 = 53 for one contract@one contract;;0.534 × 100 × 3 = 160 for three@three contracts"
Back to position delta. Zero point five three four times one hundred is fifty three share equivalents for one contract. Three contracts are one hundred and sixty. That's what the position gains per dollar of stock, right now, and it will be different after the move.

@art gamma-peak
Gamma is often greatest near the strike, close to expiration. Higher gamma means delta can change more quickly as the stock moves. So stock, time, and volatility changes can make the original Greeks stale, and you recalculate after any material change.

@chapter Where people slip
@list heading="Common mistakes" items="Treating delta as constant@The first|Ignoring the multiplier@The second|Probability language as certainty@The third"
The first mistake is treating delta as constant. It changes with stock price, time, volatility and other inputs. The second is ignoring the multiplier. A zero point five delta standard contract is roughly fifty share deltas, not half a share. The third is using probability language as certainty. Delta based probability readings are model dependent approximations.

@chapter Try it
@words text="Dollar estimate · share equivalents · why it undershoots"
Your turn. Turn a delta into a first order dollar estimate. Convert it to share equivalent exposure with the multiplier and the quantity. And explain why the estimate undershoots on a large move.

@end text="Compare the three estimates"
You can set a move and compare all three estimates, on Learn. That's learn dot get er done dot I O.
