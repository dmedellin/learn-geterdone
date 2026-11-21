---
format: long
lesson: accumulation-and-the-integral/refining-the-partition
title: Refining the partition: does doubling the pieces halve the error?
thumb: Close to two, not two
---

@chapter More pieces
@title text="Refining the Partition" sub="Accumulation and the Integral" art=thumb
Cut the interval into more pieces, and the window around the total shrinks. So keep doubling the pieces, and watch what the sums do. The table tells a clear story. But it isn't a proof, and this lesson keeps those two apart.

@art doubling-pieces
Doubling the pieces halves the width, and every old left end is still a left end of the new partition. Each term now reads the rate closer to where it's actually being added.

@chapter The square, refined
@math heading="t² on [0, 1],  left sums" items="n = 4:  7/32@four pieces;;n = 8:  35/128@With eight;;n = 16:  155/512@With sixteen;;total:  1/3@a third"
Take t squared from zero to one. With four pieces, the left sum is seven thirty seconds. With eight, thirty five over one hundred and twenty eight. With sixteen, one hundred and fifty five over five hundred and twelve. The exact total is a third. Each sum is below it, and each is closer than the last.

@art error-slivers
What each sum misses is the thin slivers between the rectangles and the curve. Every doubling shaves them thinner.

@math heading="sum minus total" items="n = 4:  −11/96@minus eleven;;n = 8:  −23/384@minus twenty three;;n = 16:  −47/1536@minus forty seven"
The lab prints the error as the sum minus the total, so these errors are negative: minus eleven ninety sixths, minus twenty three over three hundred and eighty four, and minus forty seven over one thousand five hundred and thirty six.

@chapter The error ratio
@math heading="error(n) / error(2n)" items="4 → 8:  44/23 ≈ 1.91304@forty four;;8 → 16:  92/47 ≈ 1.95745@ninety two"
Now divide each error by the next one. From four pieces to eight, the ratio is forty four twenty thirds, about one point nine one three. From eight to sixteen, it's ninety two forty sevenths, about one point nine five seven. The signs cancel, so the ratio is positive.

@art creeping-toward
So each doubling cuts the error to a little more than half. The ratios are below two, and creeping toward it. Here's the core of why. The error is about half of the gap between the left and right sums, and that gap halves exactly.

@chapter Exactly two
@art straight-ramp
There's one kind of rate where the ratio is exactly two: a straight line. For the ramp two t from zero to two, the total is exactly the average of the left and right sums. So the left sum falls short by exactly half the gap, which is two h.

@math heading="ramp 2t on [0, 2]:  error = −2h" items="n = 4,  h = 1/2:  −1@minus one;;n = 8,  h = 1/4:  −1/2@minus a half;;ratio:  exactly 2@exactly two"
At four pieces, the error is minus one. At eight, it's minus a half. The ratio is exactly two, every time.

@chapter Claim and evidence
@words text="The left sums approach the total" sub="a claim, demonstrated and not proved"
Here's the claim. For a polynomial rate on a fixed interval, the left sums approach a single number, and that number is the exact total. For the ramp, the error two h proves it, because two h goes to zero. For t squared there's no such formula in sight, and the table is evidence at three values of n.

@art bendy-cubic
A cubic shows how the ratio depends on the rate. For t cubed from zero to two, four pieces give nine quarters, against a total of four. Eight pieces give forty nine sixteenths. The ratio is twenty eight fifteenths, about one point eight six seven, further from two. A rate that bends more needs thinner pieces.

@chapter Where people slip
@list heading="Common slips" items="Assuming doubling always halves the error@The first|Reading the ratio as correctness@The second|Calling a table a proof@the third"
The first slip is assuming that doubling halves the error exactly, for every rate. The second is reading the ratio as a verdict on correctness. Every sum is exact. The error belongs to the method. And the third is calling a table a proof.

@art halving-errors
Treat two as a law for t squared, and you'd predict the error at eight pieces as eleven over one hundred and ninety two. The lab prints twenty three over three hundred and eighty four. Near half is not half.

@chapter Try it
@words text="t² on [0, 1],  n = 16" sub="left rates: 0, 1, 4, …, 225, all over 256"
Your turn. Repeat the computation at sixteen pieces. The sixteen left rates are zero, one, four, and so on up to two hundred and twenty five, all over two hundred and fifty six. You should land on one hundred and fifty five over five hundred and twelve, and a ratio of ninety two forty sevenths.

@end text="Double the pieces, measure the error"
You can double the pieces yourself and watch the error ratio, as an exact fraction, on Learn. That's learn dot get er done dot I O.
