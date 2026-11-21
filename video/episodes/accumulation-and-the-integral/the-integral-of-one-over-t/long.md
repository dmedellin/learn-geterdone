---
format: long
lesson: accumulation-and-the-integral/the-integral-of-one-over-t
title: The integral of 1/t, where the power rule breaks
thumb: Where ln 2 comes from
---

@chapter Where the shortcut fails
@title text="The Integral of 1/t" sub="Accumulation and the Integral" art=thumb
Every integral so far had an antiderivative from the reversed power rule: raise the power, then divide by the new one. Now try it on one over t.

@math heading="1/t = t⁻¹" items="t⁻¹  →  t⁰/0  ✗@divide by zero"
One over t is t to the minus one. Raise the power and you get t to the zero. Divide by the new power, and you're asked to divide by zero. That's no antiderivative. And no polynomial has derivative one over t, because a polynomial's derivative never has a term in t to the minus one.

@art hyperbola-strip
But nothing is wrong with the rate itself. One over t is a perfectly good falling rate from one to two. What fails is the shortcut. The sums still work, unchanged.

@chapter The sums, from one to two
@math heading="1/t on [1, 2],  n = 4,  h = 1/4" items="rates:  1,  4/5,  2/3,  4/7@the rates;;L₄ = 319/420 ≈ 0.759524@The left sum;;R₄ = 533/840 ≈ 0.634524@The right sum;;T₄ = 1171/1680 ≈ 0.697024@the trapezoid"
With four pieces, the rates at the left ends are one, four fifths, two thirds and four sevenths. The left sum is three hundred and nineteen over four hundred and twenty, about zero point seven six. The right sum is about zero point six three, and the trapezoid, about zero point six nine seven.

@art bracket-falling
The rate falls, so the total lies between the right sum and the left sum, in a window an eighth wide. And the lab's exact total tile prints about zero point six nine three one four seven, labelled rounded.

@words text="≈ 0.693147   (ln 2, rounded)" sub="the sums are exact; the total is not"
That label matters. The sums are exact fractions. The total isn't a fraction at all, so the lab can only print it as a rounded decimal.

@chapter No fraction at the end
@art converging-decimals
Refine the pieces, and the left sum drops. Eight pieces give about zero point seven two five. Sixteen give about zero point seven zero nine. Each is a different exact fraction, and each is above the target by about half as much as the last.

@words text="ln 2 is not a fraction" sub="a known fact, not proved here"
The target is not a fraction. That's a known fact of mathematics, and it isn't proved here. What the lab shows is that no sum it can print equals the target. A list of fractions can close in on a number that is none of them.

@chapter The natural logarithm
@math heading="The integral of 1/t" items="∫₁ˣ dt/t = ln x@from one to x"
Here's the claim. For x greater than one, the sums of one over t from one to x approach a number written l n x, the natural logarithm: the power you raise e to, to get x. That accumulating one over t produces it is the claim, and the sums support it.

@chapter Scaling leaves the sums alone
@art doubled-piece
Here's a fact you can prove. Double an interval, from a to b, to two a to two b. Each piece's left end doubles, so its rate halves. But its width doubles. So rate times width stays exactly the same, piece by piece.

@math heading="1/t on [2, 4],  n = 4" items="rates:  1/2,  2/5,  1/3,  2/7@the rates;;(1/2)·(1/2 + 2/5 + 1/3 + 2/7) = 319/420@the sum"
So on the scaled preset, from two to four, the rates are a half, two fifths, a third and two sevenths, the width is a half, and the sum is three hundred and nineteen over four hundred and twenty. Exactly the sum from one to two.

@art scaled-regions
The region from two to four is lower and wider than the region from one to two, and for every number of pieces, its sum comes out the same.

@art two-halves
So the total from two to four equals the total from one to two, and by additivity, the total from one to four is twice it. The l n four preset agrees: about one point three eight six, which is two times l n two. That's the addition rule of logarithms, as an exact equality of fractions.

@chapter Where people slip
@list heading="Common slips" items="Writing t⁰/0@The first|Quoting the rounded total as exact@The second|Concluding the total is a fraction@the third"
The first slip is applying the power rule anyway, and writing t to the zero over zero. That names no function. The second is quoting the rounded total as if it were exact. Keep the approximately sign. And the third is concluding the total is a fraction, because every sum is.

@chapter Try it
@words text="1/t on [1, 3],  n = 4" sub="left ends: 1, 3/2, 2, 5/2"
Your turn, on the l n three preset, from one to three. The left ends are one, three halves, two and five halves. You should find a left sum of seventy seven sixtieths and a right sum of nineteen twentieths, around l n three, about one point zero nine eight six.

@end text="Sum it, bracket it, name it"
You can bracket the integral of one over t for any upper limit, on Learn. That's learn dot get er done dot I O.
