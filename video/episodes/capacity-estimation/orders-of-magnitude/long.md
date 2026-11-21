---
format: long
lesson: capacity-estimation/orders-of-magnitude
title: Orders of magnitude: why an estimate is an interval
thumb: Half-widths multiply
---

@chapter The question
@title text="Orders of Magnitude" sub="Capacity Estimation" art=thumb
How much data does a service write in a day? You multiply users by actions by bytes and get one number. That number looks precise. It isn't, and this video is about how imprecise it really is.

@art single-dot
Nobody knows that a service has exactly ten million daily users. What you actually know is something like five to twenty million, and ten million is the middle. Every factor you put into an estimate is a range like that.

@chapter Ranged factors
@math heading="Known to within a factor of k" items="[c/k, c·k]@the interval;;width = hi/lo = k²@its width;;k = 1  →  known exactly@k equals one"
A quantity known to within a factor of k, with central value c, is the interval from c over k to c times k. We call k its half-width. Its width, the ratio of the two ends, is k squared. And k equals one means you measured it.

@words text="±2× is not ±50%" sub="÷2 is −50% · ×2 is +100%"
Notice the half-width is a factor, not a percentage. A factor of two down is minus fifty percent, but a factor of two up is plus one hundred percent. So known to within a factor of two means one multiplicative step either side.

@chapter Intervals multiply
@art interval-product
Now multiply two positive intervals. The smallest product comes from the two smallest ends, and the largest from the two largest ends. Nothing in between needs checking, and both ends really can happen.

@math heading="Two ranged factors" items="[c/k, ck] · [d/m, dm]@multiply;;= [cd/(km), cd·km]@you get;;half-width km@half-widths multiply"
Multiply c over k to c k by d over m to d m, and you get c d over k m, up to c d times k m. That's a ranged factor again, with central value c d and half-width k m. The half-widths multiply.

@chapter A worked example
@art three-ranges
Take ten million users, a hundred actions each, and a kilobyte per action, each known to within a factor of two.

@math heading="Bytes per day" items="10⁷ users · 10² actions · 10³ bytes@the centres;;centre = 10¹² bytes@a terabyte;;low = 1.25·10¹¹@the low end;;high = 8·10¹²@the high end;;half-width 2 · 2 · 2 = 8@two times two times two"
The centres multiply to ten to the twelve bytes, a terabyte. The low end is one point two five times ten to the eleven. The high end is eight times ten to the twelve. And the half-width is two times two times two, which is eight.

@words text="125 GB … 8 TB a day" sub="centred on 1 TB"
So the honest report is between a hundred and twenty five gigabytes and eight terabytes a day, centred on a terabyte. That's one sentence, and it says far more than one terabyte does.

@chapter Reporting the width
@art range-funnel
Three narrow factors went in, and one wide range came out. So how do you say how wide it is?

@math heading="Two ways to say how wide" items="half-width  ÷8 … ×8@carry into;;width  8 · 8 = 64×@end to end;;10¹ ≤ 64 < 10²@between ten and a hundred"
There are two numbers here. Divide by eight up to times eight is the half-width, and that's what you carry into the next multiplication. Sixty four times is the width end to end, and it tells you whether the answer is worth acting on. It sits between ten and a hundred, so this answer is good to within two orders of magnitude.

@chapter Where the middle is
@art lopsided-average
Here's the surprise. The plain average of the two ends is four point zero six two five times ten to the twelve. That's sixty five sixteenths of the estimate, about four times it. The high end is sixty four times the low end, so it drags any average towards itself.

@math heading="The centre of a product range" items="(lo + hi)/2 = 4.0625·10¹²@plain average;;√(lo · hi) = √(10²⁴) = 10¹²@the geometric mean"
Compare the plain average, four point zero six two five times ten to the twelve, with the geometric mean, the square root of low times high. That's the square root of ten to the twenty four, which is ten to the twelve exactly. Right where the estimate started.

@art widest-factor
And the range gives you direction. With three factors at a factor of two, they all contribute equally. Make one of them a factor of ten and the half-width becomes forty, and that one factor is the only thing worth measuring. The widest factor is the work item.

@chapter Where people slip
@list heading="Common slips" items="Averaging the two ends@The first|Adding the half-widths@The second|Calling the high end conservative@The third"
The first slip is averaging the two ends, which lands you four times too high. The second is adding the half-widths, so three factors of two become six instead of eight, and the answer looks narrower than it is. The third is taking the high end of every factor and calling it conservative. That's just one end of a range you've already computed.

@chapter Try it
@words text="bytes per action: ±10×" sub="half-width 2 · 2 · 10 = 40"
Your turn. Keep the same three factors, but make bytes per action known only to a factor of ten. The half-width is now two times two times ten, forty. Work out the new low and high ends, the width, and which decade it falls in. Then say which factor you'd go and measure.

@end text="Drag the factors, watch the range"
You can move every factor and its half-width and watch the whole interval redraw, on Learn. That's learn dot get er done dot I O.
