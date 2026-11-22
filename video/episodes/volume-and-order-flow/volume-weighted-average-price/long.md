---
format: long
lesson: volume-and-order-flow/volume-weighted-average-price
title: VWAP: the session's average price, weighted by volume
thumb: Where is value today?
---

@chapter The question
@title text="Volume-Weighted Average Price" sub="Volume and Order Flow" art=thumb
During a session, price wanders all over. So where has most of the trading actually happened? A plain average of prices can't tell you, because it treats a quiet bar the same as a busy one. VWAP fixes that.

@art vwap-line
VWAP, the volume weighted average price, is a single line that follows the session. Price above it or below it describes where current trading sits relative to the session's average value.

@chapter The formula
@math heading="VWAP" items="VWAP = Σ(price × volume) ÷ Σ volume@price times volume;;both sums start at the session open@from the start"
VWAP is cumulative price times volume, divided by cumulative volume. You add up price times volume for every bar, and divide by all the volume traded, both from the start of the session.

@art weighting
That means each bar's typical price is weighted by how much traded there. A busy bar pulls the average toward its price. A quiet bar barely moves it.

@chapter Worked example
@words text="Bar 1: 100 on 100 · Bar 2: 102 on 300"
Here's the lesson's example. The first bar has a typical price of one hundred on one hundred contracts. The second has one oh two on three hundred contracts.

@math heading="Two bars" items="100 × 100 = 10,000@one hundred times one hundred;;102 × 300 = 30,600@times three hundred;;10,000 + 30,600 = 40,600@forty thousand six hundred;;40,600 ÷ 400 = 101.50@one oh one point five"
One hundred times one hundred is ten thousand. One oh two times three hundred is thirty thousand six hundred. Together that's forty thousand six hundred. Divide by the four hundred contracts, and VWAP is one oh one point five.

@math heading="Not these" items="✗  101.00: the plain average@the plain average;;✗  102.00: the last bar alone@the last"
One oh one would be the plain average of the two prices. But three times the volume traded at one oh two, so VWAP sits closer to it. And one oh two is just the last bar's price. VWAP is cumulative, so the first bar's hundred contracts still pull it down.

@words text="Not close-only · not one bar"
So VWAP isn't calculated from closing prices only, which would ignore how much traded at each price. And it isn't the highest volume bar alone. That's a different idea, a profile's point of control. VWAP averages every bar.

@words text="VWAP is built from volume"
One more thing follows from the formula. With no participation, there'd be no line at all. So whenever you see VWAP, it's a summary of real trading, weighted by where that trading was heaviest.

@chapter Reading control
@art above-rising
Now read it. Price that stays above a rising VWAP shows buyers accepting prices above the session's volume weighted average. Trade is being done higher than average, and the average itself is climbing. Sellers are supplying in those trades, but it's buyers who are paying up.

@art below-falling
The mirror image is price below a falling VWAP. Sellers are accepting lower prices, below the session average.

@art flat-crossing
And when price crosses a flat VWAP again and again? That suggests two way balance around session value. Neither side is maintaining progress away from the average. It's not clear trend control, and it's not a guaranteed breakout either.

@words text="Slope + sustained location > one cross"
The lesson puts it as slope and acceptance. A rising or falling VWAP, plus sustained price location on one side, is stronger evidence than a single cross.

@chapter Where people slip
@list heading="Common mistakes" items="Mixing session VWAP with multi-day data@The first|Buying every VWAP reclaim@The second|Ignoring the opening auction and events@the third"
Three mistakes. The first is mixing session VWAP with multi day data without defining reset rules. The second is buying every VWAP reclaim. And the third is ignoring the opening auction and event driven volume.

@art session-reset
So reset session VWAP at the session boundary. Use slope and acceptance, not one touch. And remember VWAP is a reference, not automatic support or resistance.

@chapter Try it
@list heading="Reading steps" items="Check VWAP slope@check the slope|Check price location@check price location|State control@state control"
The lab's steps are short. First, check the slope. Rising, falling, or flat? Second, check price location. Is price consistently above, below, or crossing it? Third, state control. Describe who is accepting prices away from the session average.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection. For practice, rework the two bar example with the volumes swapped, three hundred at one hundred and one hundred at one oh two, and see which way VWAP moves.

@end text="Slope, location, then control"
You can watch VWAP build through a session in the lab, on Learn. That's learn dot get er done dot I O.
