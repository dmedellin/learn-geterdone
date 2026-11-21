---
format: long
lesson: latency-and-the-tail/the-speed-of-light-floor
title: The speed of light floor: the latency no engineering removes
thumb: 3d over c, and nothing less
---

@chapter The question
@title text="The Speed-of-Light Floor" sub="Latency and the Tail" art=thumb
A round trip from New York to London takes seventy six milliseconds. How much of that can you actually fix? Less than you'd hope, and you can work it out with one division.

@art fibre-route
Signals in fibre travel at about two thirds of the speed of light. A round trip covers the distance twice. So over a great circle distance d, no round trip can take less than two d divided by two thirds c.

@math heading="The light-speed floor" items="RTT_min = 2d ÷ (⅔c)@two d divided by;;= 3d/c@three d over c"
Two d divided by two thirds of c simplifies to three d over c. It assumes a perfectly straight cable and zero processing. So it's a bound nothing beats, not a prediction.

@chapter New York to London
@math heading="d = 5585 km" items="3 × 5 585 000 / 299 792 458 s@three times;;= 55.889 ms@fifty five point eight eight nine"
New York to London is five thousand five hundred and eighty five kilometres. Three times that, in metres, over two hundred and ninety nine million, seven hundred and ninety two thousand, four hundred and fifty eight metres a second, is fifty five point eight eight nine milliseconds. The speed of light is exact by definition, so this floor is an exact fraction.

@math heading="Measured: 76 ms" items="76 / 55.889 = 1.360@one point three six;;remainder 76 − 55.889 = 20.111 ms@twenty point one one one"
Now set the measurement to seventy six milliseconds. That's one point three six times the floor. The remainder is twenty point one one one milliseconds. That remainder is the number to take into a meeting.

@chapter The remainder
@art floor-and-remainder
What's left above the floor is queueing at each hop, the time to clock bits onto each link, middleboxes, and your own software. It's the only part anyone can fix. Here it's about a quarter of the measurement, so even removing all of it would be about a twenty six percent improvement.

@math heading="Halve the remainder" items="55.889 + 10.056 = 65.945 ms@halving it;;saves 10.055 ms = 13.2%@thirteen point two"
And halving it, which would be an extremely good quarter of work, takes the route from seventy six to sixty five point nine four five milliseconds. That saves ten point zero five five milliseconds, thirteen point two percent.

@list heading="Floors" items="New York → San Francisco: 41.419 ms@San Francisco|Mumbai → London: 72.050 ms@Mumbai|Frankfurt → Singapore: 102.701 ms@Frankfurt|London → Sydney: 170.048 ms@Sydney"
A few more floors. New York to San Francisco is forty one point four one nine milliseconds. Mumbai to London is seventy two point zero five. Frankfurt to Singapore is a hundred and two point seven zero one. And London to Sydney is a hundred and seventy point zero four eight.

@chapter What a CDN buys
@art nearby-copy
That hundred and seventy millisecond floor is why a service with one region has a bad day in the other hemisphere. The fix is a second copy of the data, not a faster anything. A content network doesn't accelerate a packet. It shortens the route.

@art write-to-origin
But a reader in Sydney who posts a comment has to reach the one place that owns the data. That write's floor is a hundred and seventy point zero four eight again. No cache configuration changes it.

@art below-floor
And if a measurement comes out below the floor, that's not a fast network. It's a wrong distance, usually because you measured to a nearby edge node while thinking it was the origin.

@art coastline-cable
Two cautions on the model. Two thirds of c is a convention, since real fibre runs at roughly zero point six six to zero point six nine of c, so the floor is good to a few percent. And real cables follow coastlines and ducts, not great circles. So the true floor is somewhat higher than this one.

@chapter Where people slip
@list heading="Common slips" items="Quoting one-way as a round trip@The first|Using c instead of ⅔c@The second|Offering a cache for a write@The third"
The first slip is quoting a one way figure as a round trip. New York to London one way is twenty seven point nine four four. The second is using c instead of two thirds c, which gives thirty seven point two five nine. The third is offering a cache for a request that must reach the origin.

@chapter Try it
@words text="Frankfurt → Singapore · 10 263 km · measured 165 ms" sub="floor: 102.701 ms"
Your turn. Frankfurt to Singapore, ten thousand two hundred and sixty three kilometres, measured at a hundred and sixty five milliseconds. The floor is a hundred and two point seven zero one. Compute the ratio and the remainder. Then say whether a hundred and twenty millisecond target is reachable from Frankfurt at all.

@end text="Know the floor before the work"
You can pick a route, enter a measurement and see the floor and the remainder, on Learn. That's learn dot get er done dot I O.
