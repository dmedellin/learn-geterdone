---
format: long
lesson: accumulation-and-the-integral/total-change-from-a-rate
title: Total change from a rate: freeze it, then add the pieces
thumb: An exact estimate
---

@chapter The question
@title text="Total Change from a Rate" sub="Accumulation and the Integral" art=thumb
A rate tells you how fast something is changing right now. But what does it add up to over an interval? That's the total change, and the honest answer comes in two parts: a number, and how far to trust it.

@art constant-rate
When the rate holds still, it's easy. Distance is speed times time. A tank filling at a steady three litres per minute gains three times four, twelve litres, in four minutes.

@words text="change = rate × time" sub="provided the rate does not change"
The catch is the proviso. Rate times time is the total only if the rate doesn't change. And most rates worth asking about do move.

@chapter Freeze it in pieces
@math heading="The left sum" items="h = (b − a)/n@of width h;;Lₙ = h·(f(a) + f(a + h) + … + f(b − h))@the left sum"
So cut the interval from a to b into n pieces of width h, which is b minus a, over n. Inside each piece, pretend the rate is what it was at the left end. Each piece gives rate times width, and the left sum adds them up.

@chapter A tap that opens slowly
@math heading="rate 2t on [0, 2],  n = 4,  h = 1/2" items="left ends:  0,  1/2,  1,  3/2@The left ends;;rates:  0,  1,  2,  3@the rates there;;L₄ = (1/2)·(0 + 1 + 2 + 3) = 3@times a half"
Take a tap that opens slowly: t minutes after it opens, it delivers two t litres per minute. Over two minutes, in four pieces, the width is a half. The left ends are zero, a half, one and three halves, and the rates there are zero, one, two and three. Add them, times a half, and you get three.

@art left-rectangles
Each piece is a rectangle, as tall as the rate at its left end and as wide as the step. The left sum is their total area.

@chapter What the sum assumes
@words text="L₄ = 3    exact total = 4"
But the lab's exact total is four, not three. And that gap isn't rounding. The tap is still opening during every piece, and each piece was charged at the smallest rate it contains.

@art missed-triangles
On the piece from one to three halves, the rate climbs from two to three, but the sum charged it all at two. What's missing from each piece is a little triangle, a half wide and one tall, with an area of a quarter. Four of them make the missing one.

@words text="a rising rate + a left sum → too low"
So the error has a direction. A rising rate with a left sum comes out too low. Where the four comes from is a later lesson. For now, it's what the sums get compared with.

@chapter A tempting shortcut
@art end-rate-box
Here's a tempting shortcut: the rate at the end, four, times the time, two. That gives eight, twice the total. It treats the rate as four for the whole two minutes, but it was four only at the last instant, and zero at the first.

@chapter A steeper rate
@art steep-rate
A steeper rate makes the same point bigger. Take t squared plus one, from zero to three, in three pieces of width one. The rates at the left ends are one, two and five, so the left sum is eight. The exact total is twelve. Three pieces are far too few for a rate that climbs from one to ten.

@art more-pieces
More pieces help. For the ramp, eight pieces give seven halves, and sixteen give fifteen quarters. Both are closer, both are exact fractions, and both are still below four.

@chapter Where people slip
@list heading="Common slips" items="End rate × elapsed time@The first|Adding the rates, forgetting the width@The second|Reading the sum as the total@the third"
The first slip is the end rate times the elapsed time, which you've just seen. The second is adding the rates and forgetting the width. The ramp's rates add to six, but six isn't litres. Six times a half is. And the third is reading the sum as the total. Exact arithmetic on an estimate gives an exact estimate.

@chapter Try it
@words text="t² + 1 on [0, 3],  n = 3" sub="rates at the left ends: 1, 2, 5"
Your turn. Use the speed preset, t squared plus one from zero to three, and write out the three left ends and rates yourself. The rates are one, two and five. Add them, multiply by the width, one, and say in one sentence why the answer is below twelve.

@end text="Freeze the rate, add the pieces"
You can cut a rate into pieces and see the sum beside the exact total, on Learn. That's learn dot get er done dot I O.
