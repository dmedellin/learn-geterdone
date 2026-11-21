---
format: long
lesson: capacity-estimation/from-request-cost-to-machine-count
title: From a request's cost to a machine count
thumb: 167, not 100
---

@chapter The question
@title text="From a Request's Cost to a Machine Count" sub="Capacity Estimation" art=thumb
You know your peak rate, and you know what one request costs. How many machines do you need? It looks like one division. Two things make it more than that: machines are whole numbers, and the utilisation you divide by is a decision.

@art core-time
Capacity is one over what a request costs, in whatever resource is scarce. If one request occupies a core for forty milliseconds, and a machine has eight cores, then each second the machine can serve eight times a thousand over forty requests.

@math heading="Capacity and target" items="capacity = 8 · 1000 ms/s ÷ 40 ms = 200 req/s@two hundred;;usable = 200 · 0.6 = 120 req/s@sixty percent;;N = ⌈peak / (capacity · ρ)⌉@the machine count"
That's two hundred requests a second per machine. Now pick a target utilisation, rho, the fraction of capacity you're willing to use. At sixty percent, usable capacity is a hundred and twenty. And the machine count N is the ceiling of the peak over the usable capacity.

@chapter A worked example
@math heading="A checkout API at 20 000 req/s" items="20 000 / 120 = 500/3 = 166.67@five hundred over three;;N = ⌈500/3⌉ = 167@a hundred and sixty seven;;fleet: 167 · 200 = 33 400 req/s@thirty three thousand four hundred;;peak sits at 100/167 = 59.88%@fifty nine point eight eight"
At a peak of twenty thousand requests a second, you need twenty thousand over a hundred and twenty machines. That's five hundred over three, one hundred and sixty six point six seven. Round up: a hundred and sixty seven. The fleet has thirty three thousand four hundred of raw capacity, and the peak sits at a hundred over a hundred and sixty seven, fifty nine point eight eight percent.

@art server-rack
So that's a hundred and sixty seven machines, each a little under sixty percent full at the peak, with thirteen thousand four hundred requests a second of capacity deliberately unused.

@art staircase-ceiling
Fifty nine point eight eight, not sixty, is the ceiling showing up. Rounding up bought two thirds of a machine nobody asked for. That's the safe direction for this error. Round down for tidiness, and you're short at exactly the moment the peak arrives.

@chapter What the headroom buys
@math heading="At 100% instead" items="⌈20 000 / 200⌉ = 100@a hundred machines;;167 − 100 = 67 machines@sixty seven"
Size the same peak at a hundred percent and you get a hundred machines. The sixty seven machines between those answers are the headroom, priced. They aren't waste. They're the latency the design asked for.

@art queue-knee
Because target utilisation is a queueing decision. As utilisation approaches one, waiting time rises without bound. Sixty percent is a point on that curve, chosen so response time stays tolerable and you can lose a machine without the rest going over the knee.

@art two-questions
And it's not insurance against a wrong estimate. That's a separate question. If the peak and the cost are each known to a factor of two, the fleet sits somewhere across a divide by four to times four interval. The headroom doesn't begin to cover that. The two compose by multiplying.

@chapter An integer is not precise
@math heading="Same peak, same target" items="20 ms per request → N = 84@twenty milliseconds;;40 ms per request → N = 167@forty;;80 ms per request → N = 334@eighty"
A hundred and sixty seven looks like a hard number, but it's only as hard as its inputs. Halve the cost to twenty milliseconds and you get eighty four. Keep forty and it's a hundred and sixty seven. Double it to eighty and you get three hundred and thirty four. The ceiling removes the fraction, not the range.

@art second-constraint
This is the one constraint version. Real fleets are often held up by a second constraint too, a data volume, a connection count, a write rate. Then the answer is the larger of the two ceilings. The trap is always to compute one ceiling and stop.

@chapter Where people slip
@list heading="Common slips" items="Sizing at 100%@The first|Treating headroom as an error bar@The second|Reading the integer as precise@The third"
The first slip is sizing the fleet at a hundred percent, with no room for a deploy or a failed machine. The second is treating the headroom as cover for a wrong estimate. And the third is reading the integer as a precise answer. Name the assumption that moves it most, here the cost of a request.

@chapter Try it
@words text="500 000 req/s · 2 ms · 4 cores · 80% target" sub="capacity = 4 · 1000/2 = 2 000 req/s"
Your turn. An edge cache at five hundred thousand requests a second, two milliseconds a request, four cores, eighty percent target. The capacity is four times a thousand over two, two thousand a second per machine. Work out the usable capacity, the exact count and N. Then predict N at sixty percent.

@end text="Price your headroom"
You can move the cost, the cores and the target and watch the staircase of machines, on Learn. That's learn dot get er done dot I O.
