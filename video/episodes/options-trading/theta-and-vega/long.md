---
format: long
lesson: options-trading/theta-and-vega
title: Theta and vega: what a day and an IV point cost your option
thumb: Points, not decimals
---

@chapter The question
@title text="Theta and Vega" sub="Options Trading" art=thumb
The stock doesn't move at all. Five days pass, and implied volatility drops. How much has your call lost, and which of those two things took it? Theta and vega let you split the loss line by line.

@words text="Theta prices a day · Vega prices an IV point"
Here's the idea in one line. Theta prices a day. Vega prices an implied volatility point. And both are local to the current state, so they describe the option as it is right now.

@chapter Theta
@art clock-drain
Theta estimates the option price change for one day passing, with the other inputs unchanged. It's quoted per share, so the contract figure is times one hundred. For a long option it's negative. Waiting costs money, even on a day when nothing else happens.

@chapter Vega
@art iv-dial-vega
Vega estimates the option price change for a one percentage point change in implied volatility. One point. So if implied volatility goes from thirty five percent to twenty five percent, that's a change of ten points, and you multiply vega by ten.

@art two-drains
A long option gains when implied volatility rises and loses when it falls, all else equal. So a holder has two quiet costs running at once: the calendar, and any fall in volatility. This example has both.

@chapter The worked example
@words text="100 call · 45 DTE · IV 35% · stock held at $100" sub="5 days pass · IV −10 points"
The lesson's worked example is the lab's default state. A one hundred call, forty five days to expiration, implied volatility thirty five percent, with the stock held at one hundred. Five days pass, and implied volatility falls ten points.

@math heading="Time contribution" items="Theta = −0.060 per share per day@minus zero point zero six;;−0.060 × 5 days × 100 = −$30@thirty dollars"
Theta is minus zero point zero six zero per share per day. Times five days, times one hundred, is minus thirty dollars. That's the time contribution.

@math heading="Volatility contribution" items="Vega = 0.139 per IV point@zero point one three nine;;0.139 × (−10) × 100 = −$139@minus ten;;Ten points, not 0.10@not zero point one"
Vega is zero point one three nine per point. Times minus ten, times one hundred, is minus one hundred and thirty nine dollars. Ten points, not zero point one. That's the unit trap the drill is built around.

@chapter Estimate versus repricing
@math heading="Add them, then reprice" items="Linear: −$30 − $139 = −$169@one hundred and sixty nine;;Full: $5.17 → $3.54 = −$162@five seventeen;;Residual: +$7@seven dollars"
Add them, and the linear estimate is minus one hundred and sixty nine dollars. Now reprice in full: five seventeen to three fifty four, a loss of one hundred and sixty two. The difference, plus seven dollars, is the residual.

@art moving-greeks
Where does the seven dollars come from? The Greeks themselves changed as the state changed. Theta and vega at forty days and twenty five percent are not what they were at forty five days and thirty five percent. The estimate used the starting values the whole way.

@art long-short-mirror
In this example, both signs are against the holder. The writer's attribution is the mirror image. Time passing and implied volatility falling both transfer value from the long side to the short side.

@chapter Use them together
@art stress-grid
A long option can be right on direction and still lose value when time and volatility move against it. So read current theta to estimate the cost of waiting, read vega for the sensitivity to an implied volatility point, and stress several combinations of time and volatility, not just the one you expect. Then reprice the full position.

@chapter Where people slip
@list heading="Common mistakes" items="Multiplying theta indefinitely@The first|IV change as a decimal@The second|Greek estimates as exact P and L@The third"
The first mistake is multiplying theta indefinitely. Theta isn't constant, and it changes as expiration approaches. The second is using the implied volatility change as a decimal with a quoted vega. The units have to match. And the third is adding Greek estimates as if they were exact profit and loss. Cross effects and changing sensitivities create differences.

@chapter Try it
@words text="Theta × days · vega × IV points"
Your turn. Using the lesson's defaults, attribute the premium change to theta times days and vega times implied volatility points, in the right units. Then say why the sum is an estimate, rather than the P and L. And watch the units: points, not decimals.

@end text="Apply a time and IV shock"
You can apply days passed and an implied volatility change, and compare the estimate with the repricing, on Learn. That's learn dot get er done dot I O.
