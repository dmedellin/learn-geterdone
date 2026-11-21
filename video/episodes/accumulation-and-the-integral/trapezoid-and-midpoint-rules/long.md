---
format: long
lesson: accumulation-and-the-integral/trapezoid-and-midpoint-rules
title: The trapezoid and midpoint rules, and the factor of four
thumb: Halve the width, quarter the error
---

@chapter Better than the ends
@title text="The Trapezoid and Midpoint Rules" sub="Accumulation and the Integral" art=thumb
The left and right sums freeze the rate at an end, and their errors halve as the pieces double. There are two simple ways to do much better. On a quadratic, their errors fall by exactly four.

@art trapezoid-piece
The first is the trapezoid rule. Replace the flat top of each piece with the straight line from the rate at the left end to the rate at the right. The area is the average of the two end rates, times the width.

@math heading="Two rules" items="Tₙ = (Lₙ + Rₙ)/2@the trapezoid sum;;Mₙ = h·(f(m₁) + … + f(mₙ))@the midpoint sum"
So the trapezoid sum is just the average of the left and right sums. The second rule, the midpoint sum, freezes each piece at the rate in the middle of the piece instead.

@art midpoint-piece
Reading the middle helps, because the overshoot on one half of the piece largely cancels the undershoot on the other.

@chapter The square, both ways
@math heading="t² on [0, 1],  n = 4" items="T₄ = (7/32 + 15/32)/2 = 11/32@The average;;11/32 − 1/3 = 1/96@high by"
Take t squared from zero to one, in four pieces. The left sum was seven thirty seconds and the right sum fifteen thirty seconds. The average is eleven thirty seconds. Against the total of a third, it's high by one ninety sixth.

@art chord-above
It's high because the rate curves upward, and the straight chord across each piece lies above the curve.

@math heading="Midpoints" items="1/8,  3/8,  5/8,  7/8@one eighth;;squares:  1, 9, 25, 49  over 64@Their squares;;M₄ = (1/4)·(84/64) = 21/64@twenty one sixty fourths;;error:  −1/192@low"
The midpoints are one eighth, three eighths, five eighths and seven eighths. Their squares are one, nine, twenty five and forty nine, over sixty four. A quarter of their total is twenty one sixty fourths, and that's low, by one over one hundred and ninety two.

@art opposite-errors
So the midpoint sum is low by half as much as the trapezoid sum is high. The two errors have opposite signs.

@chapter Doubling divides by four
@math heading="t² on [0, 1]" items="T₄:  1/96     T₈:  1/384@trapezoid error;;M₄:  −1/192     M₈:  −1/768@midpoint error;;ratio:  exactly 4@exactly four"
Now double to eight pieces. The trapezoid error drops from one ninety sixth to one over three hundred and eighty four. The midpoint error drops from minus one over one hundred and ninety two to minus one over seven hundred and sixty eight. The ratio is exactly four.

@art quarter-shrink
Why four? For t squared, the trapezoid error is exactly h squared over six, and the midpoint error is minus h squared over twelve. Halve h, and h squared drops to a quarter.

@chapter Why h squared
@math heading="One piece, from x to x + h" items="total:  h·(x² + xh + h²/3)@the total;;trapezoid:  h·(x² + xh + h²/2)@The trapezoid;;midpoint:  h·(x² + xh + h²/4)@the midpoint"
On one piece from x to x plus h, the total is h times x squared plus x h plus h squared over three. The trapezoid has h squared over two in that last place, and the midpoint has h squared over four. So the trapezoid is over by h cubed over six, and the midpoint short by h cubed over twelve.

@words text="n·h³/6 = h²/6" sub="because n·h = 1"
Neither excess depends on x. Add them over n pieces, and since n times h is one, you get h squared over six, and minus h squared over twelve. That proof is for the square only.

@chapter Exact only for lines
@art line-exact
Because the trapezoid uses both ends, it's tempting to think it's exact whenever it has enough information. It's exact for every straight line. On a curve, it's exact only by accident.

@math heading="Other powers, trapezoid errors" items="t³:  1/64,  1/256,  1/1024    ratio exactly 4@t cubed;;t⁴:  53/2560,  213/40960    ratio 848/213 ≈ 3.98122@t to the fourth"
A cubic is kind. On t cubed from zero to one, the trapezoid errors are one sixty fourth, one over two hundred and fifty six, and one over one thousand and twenty four: a ratio of exactly four. But t to the fourth gives eight hundred and forty eight over two hundred and thirteen, about three point nine eight. Near four, and not four.

@chapter Where people slip
@list heading="Common slips" items="Thinking the trapezoid rule is exact for polynomials@The first|Expecting the same sign from both rules@The second|Taking a ratio of 4 as a law@the third"
The first slip is thinking the trapezoid rule is exact for every polynomial. The second is expecting both rules to err in the same direction. And the third is taking a ratio of four as a law for every smooth rate. It's exactly four for t squared and t cubed, and not for t to the fourth.

@chapter Try it
@words text="midpoints,  n = 8" sub="1/16,  3/16,  …,  15/16"
Your turn. Switch the lab's rule to midpoints, and set the pieces to eight. The midpoints are one sixteenth, three sixteenths, and so on up to fifteen sixteenths. You should find eighty five over two hundred and fifty six, an error of minus one over seven hundred and sixty eight, and a ratio of four again.

@end text="Ends, middles, and a factor of four"
You can switch between left, right, trapezoid and midpoint rules and compare their errors, on Learn. That's learn dot get er done dot I O.
