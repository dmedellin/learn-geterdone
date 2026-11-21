---
format: long
lesson: rational-and-radical-expressions/complex-fractions
title: Complex fractions: two methods, and the exclusion that disappears
thumb: Every level has a say
---

@chapter Fractions inside fractions
@title text="Complex Fractions" sub="Rational and Radical Expressions" art=thumb
A complex fraction looks intimidating, but it needs nothing new. Just multiplying, dividing, adding and subtracting, in one of two orders. The second order is usually much shorter, and the two must always agree.

@art stacked-fractions
A complex fraction is a rational expression whose top, or bottom, or both, contain fractions of their own. One over x minus one third, all over x minus three, is a typical one. So is one over x plus one over y, over one over x minus one over y.

@chapter Two methods
@art two-routes
Method one treats the main bar as what it is, a division. Combine the top into a single fraction. Do the same to the bottom. Then divide the one by the other. It always works, and it's often long.

@art multiplier-both
Method two clears the small fractions before they cause trouble. Find the L C D of every small denominator anywhere in the expression, and multiply the whole top and the whole bottom by it.

@math heading="Why method 2 is legal" items="A / B = (A·M) / (B·M),   M ≠ 0@A over B"
Why is that allowed? For any non zero M, A over B equals A M over B M. Choose M to be the L C D of the small denominators, and both A M and B M come out free of fractions, because every small denominator divides M.

@chapter One expression, both ways
@math heading="(1/x − 1/3) / (x − 3)" items="Method 1:  top = (3 − x)/(3x)@method one;;(3 − x)/(3x) ÷ (x − 3) = (3 − x)/(3x(x − 3))@divided by;;Method 2:  × 3x top and bottom  →  (3 − x)/(3x(x − 3))@method two"
Take one over x minus one third, all over x minus three. With method one, the top becomes three minus x, over three x. Divided by x minus three, that's three minus x, over three x times x minus three. With method two, multiply top and bottom by three x, and you get the same thing directly. One step fewer.

@art small-bars-vanish
Look at the top with method two. Three x times one over x is three, and three x times one third is x. The small fractions are gone. Then the finish is a sign observation: three minus x is minus, x minus three.

@math items="= −(x − 3) / (3x(x − 3))@minus x minus three;;= −1/(3x)@reduces to;;x = 1:  (2/3)/(−2) = −1/3  and  −1/3  ✓@check at one"
So the quotient is minus x minus three, over three x times x minus three, which reduces to minus one over three x. Check at one. The original is two thirds over minus two, which is minus one third, and minus one over three is minus one third too.

@chapter Where the exclusions come from
@art three-levels
That answer is startlingly simple, and that's where domain discipline pays. Minus one over three x looks as if it only excludes zero. The original excluded zero, because of one over x. And it excluded three, because the main denominator, x minus three, was zero there. Both belong to the answer.

@math heading="(1/x + 1/y) / (1/x − 1/y)" items="LCD = xy@x y;;= (y + x) / (y − x)@multiplying;;x ≠ 0,   y ≠ 0,   x ≠ y@valid when"
Now two variables. One over x plus one over y, over one over x minus one over y. The L C D of the small denominators is x y. Multiplying top and bottom by it gives y plus x, over y minus x. It's valid when x isn't zero, y isn't zero, and x isn't y.

@art empty-divisor
That third condition deserves a pause. It doesn't come from any denominator. It comes from the bottom half itself: one over x minus one over y is zero when x equals y. In a complex fraction, the divisor is an expression, so you have to ask when it vanishes.

@chapter Where people slip
@list heading="Common slips" items="Multiplying only part of the top by the LCD@The first|Losing the main denominator's exclusion@The second|Forgetting the lower half can be zero@the third"
The first slip is multiplying only part of the top by the L C D. Three x times the bracket is three minus x, not three minus one third. The second is losing the main denominator's exclusion, three in our example. And the third is forgetting that the lower half can be zero without any denominator being zero.

@chapter Try it
@words text="(1/x + 1/2) / (1/x − 1/2)" sub="LCD of the small denominators: 2x"
Your turn. Simplify one over x plus one half, over one over x minus one half. The L C D of the small denominators is two x. First multiply the whole top and bottom by it. Then start again, combine each half, and divide. Both routes should agree. And ask when the lower half is zero.

@end text="Two methods, one answer"
You can work complex fractions both ways and compare on Learn. That's learn dot get er done dot I O.
