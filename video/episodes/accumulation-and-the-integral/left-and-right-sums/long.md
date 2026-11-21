---
format: long
lesson: accumulation-and-the-integral/left-and-right-sums
title: Left and right sums, and the total trapped between them
thumb: The gap you know in advance
---

@chapter Two ways to freeze
@title text="Left and Right Sums" sub="Accumulation and the Integral" art=thumb
Last time, every piece was frozen at its left end. But the right end is just as reasonable. The two give different numbers, and the gap between them is something you can write down before you compute either.

@art left-vs-right
The right sum uses the same pieces and the same widths, but reads the rate at the right end of each piece. On a rising rate, the left rectangles sit below the curve, and the right ones poke above it.

@chapter The square, both ways
@math heading="t² on [0, 1],  n = 4,  h = 1/4" items="L₄ = (1/4)·(0 + 1/16 + 4/16 + 9/16) = 7/32@The left sum;;R₄ = (1/4)·(1/16 + 4/16 + 9/16 + 16/16) = 15/32@The right sum;;R₄ − L₄ = 8/32 = 1/4@the gap"
Take t squared from zero to one, in four pieces of width a quarter. The left sum uses zero, one sixteenth, four sixteenths and nine sixteenths, and comes to seven thirty seconds. The right sum drops the zero and adds sixteen sixteenths, giving fifteen thirty seconds. So the gap is eight thirty seconds, a quarter.

@chapter The gap formula
@math heading="The gap" items="Rₙ − Lₙ = h·(f(b) − f(a))@h times;;t²:  (1/4)·(1 − 0) = 1/4@For the square"
Here's the claim. For any rate, the right sum minus the left sum is h times f of b minus f of a. For the square, that's a quarter times one minus zero: a quarter. It matches.

@art telescoping
Why? The two sums use almost the same list of rates. Every rate in the middle appears in both, so it cancels. The left sum keeps f of a, the right sum keeps f of b, and that's all that survives. Nothing was assumed about the rate.

@art gap-column
Slide all the little differences into one column, and you can see it: one column, h wide, as tall as the whole change in the rate.

@chapter The bracket
@words text="rising rate:  Lₙ ≤ total ≤ Rₙ" sub="falling rate: the other way round"
Now suppose the rate only rises. On each piece, the rate is at least its left end value and at most its right end value. Add over the pieces, and the total is trapped between the left sum and the right sum. For a falling rate, everything reverses.

@math heading="t² on [0, 1]" items="7/32 ≤ 1/3 ≤ 15/32@seven thirty seconds;;window width:  1/4@a window"
For the square, the total is a third, and it lies between seven thirty seconds and fifteen thirty seconds, a window a quarter wide. That's a statement the page can prove by arithmetic, not just assert.

@art narrowing-window
Double the pieces, and h halves, so the window halves too. The total gets pinned down more and more tightly.

@chapter Which sum is larger
@art falling-sums
The right sum isn't always the big one. Take four minus t, from zero to two, in four pieces. The left sum is thirteen halves, and the right sum is eleven halves. The gap is minus one, which is a half times two minus four: the same formula. And the total, six, sits between them.

@chapter A rate that turns around
@art hump-rate
The bracket needs the rate to move one way only. Type t minus t squared, from zero to one, with one piece. The rate is zero at both ends, so both sums are zero. But the lab's exact total is a sixth, outside the pair. The gap formula still holds, and gives zero.

@chapter Where people slip
@list heading="Common slips" items="Believing the right sum always overestimates@The first|Bracketing a rate that turns around@The second|Taking the average as the total@the third"
The first slip is believing the right sum is always the overestimate. Which is larger follows the rate, not the name. The second is using the bracket on a rate that turns around. And the third is taking the average of the two sums as the total.

@math heading="The average, for t²" items="(7/32 + 15/32)/2 = 11/32@the average;;total:  1/3@a third"
For the square, the average of the two sums is eleven thirty seconds, and the total is a third. The average is a better estimate than either end, but it's still an estimate.

@chapter Try it
@words text="4 − t on [0, 2],  n = 4" sub="the rate drops by 2 across the interval"
Your turn. Take the falling preset. The rate drops by two across the interval. Predict the gap from that, then check it against the lab, and say which sum is the larger, and why. Then double the pieces, and watch the gap halve.

@end text="Left, right, and the total between"
You can compute both sums for any rate and see the total trapped between them, on Learn. That's learn dot get er done dot I O.
