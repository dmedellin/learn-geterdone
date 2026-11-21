---
format: long
lesson: scaling-laws-and-cost/autoscaling-lag
title: Autoscaling lag: over a million requests with nowhere to go
thumb: Always r times tau behind
---

@chapter Capacity arrives late
@title text="Autoscaling Lag" sub="Scaling Laws and Cost" art=thumb
Autoscaling handles spikes. That's the belief. It handles growth, with a fixed lag. During a ramp, the fleet is always one boot window behind demand.

@art booting-instances
Demand rises at r requests a second, every second, for a ramp of length D. And tau is the time between ordering an instance and it serving traffic. Capacity responds to the demand of tau seconds ago, because that's when the instances arriving now were ordered.

@art lagging-lines
So for the first tau seconds, capacity doesn't move at all, and the gap grows from zero to r times tau. After that, capacity rises at the same rate as demand, but tau seconds late. So the gap stays at r times tau, constantly. It isn't a transient that closes.

@chapter The shortfall is an area
@art triangle-rectangle
The requests demanded and not served are the area between the two lines. A triangle while the boot and the ramp overlap, then a rectangle for the rest.

@math heading="r = 50 rps/s,  τ = 90 s,  D = 300 s" items="gap r·τ = 50 × 90 = 4 500 rps@four thousand five hundred;;triangle ½·r·τ² = 202 500@two hundred and two thousand;;rectangle r·τ·(D − τ) = 4 500 × 210 = 945 000@nine hundred and forty five thousand;;total = 1 147 500 requests@one million one hundred"
Take a ramp of fifty requests a second per second, a ninety second boot, and a three hundred second ramp. The gap is four thousand five hundred requests a second. The triangle is a half times fifty times ninety squared, two hundred and two thousand five hundred. The rectangle is four thousand five hundred times two hundred and ten, nine hundred and forty five thousand. Together, one million one hundred and forty seven thousand five hundred.

@math heading="Check" items="r·τ·(D − τ/2) = 4 500 × 255 = 1 147 500  ✓@two hundred and fifty five"
The closed form gives the same integer. r times tau, times D minus half of tau, is four thousand five hundred times two hundred and fifty five. Two routes to one figure is how you catch using D where you meant D minus tau.

@chapter Above one
@words text="t = 90 s:  λ = 9 500,  μ = 5 000,  ρ = 19/10"
At the worst instant, ninety seconds in, demand is nine thousand five hundred and capacity in service is still the base of five thousand. Utilisation is nineteen tenths. And mu has to be capacity in service, not capacity ordered. That difference is the whole lesson.

@art overflow-backlog
Above one, there's no steady state. The backlog grows at lambda minus mu, four thousand five hundred requests a second. So the shortfall isn't requests that were slow. It's demand that arrived with no capacity for it.

@chapter It never drains
@art level-end
When the ramp ends at three hundred seconds, demand is twenty thousand and capacity is fifteen thousand five hundred. At three hundred and ninety seconds, they meet, level at twenty thousand. Level means nothing spare. So the backlog never drains on its own. It's a permanent loss of over a million requests, not a slow period.

@chapter The warm reserve
@art warm-reserve
What removes it is capacity that's already warm. Hold r times tau, four thousand five hundred requests a second, in reserve, and the shortfall is exactly zero. The reserve absorbs the gap for the first tau seconds, and by then the first new instances are serving. A smaller reserve only reduces it.

@words text="Halve τ:  half the gap, a quarter of the triangle"
A reserve is idle capacity, bought on purpose, so it's instance hours against requests. Two knobs shrink r times tau without one. Halve the boot time, and you halve the gap and quarter the triangle. Or scale on a leading signal, so the boot starts earlier.

@chapter Where people slip
@list heading="Common slips" items="Believing autoscaling handles spikes@The first|Taking ρ against capacity ordered@The second|Reporting the shortfall as latency@the third"
The first slip is believing autoscaling handles spikes. The second is taking utilisation against the capacity ordered, which hides the whole effect. And the third is reporting the shortfall as latency, when there's no surplus to work it off.

@chapter Try it
@words text="τ = 45 s" sub="same r, same D"
Your turn. Halve the boot window to forty five seconds and keep the rest. Predict what happens to the triangle and to the total. One falls by a factor of four and the other doesn't. Then check, and say what the warm reserve would need to be.

@end text="Buy the boot window warm"
You can move the boot time and the reserve and watch the shortfall, on Learn. That's learn dot get er done dot I O.
