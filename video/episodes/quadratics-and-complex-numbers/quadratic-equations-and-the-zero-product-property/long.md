---
format: long
lesson: quadratics-and-complex-numbers/quadratic-equations-and-the-zero-product-property
title: The zero product property: why the zero has to be there
thumb: Only zero splits a product
---

@chapter The shape
@title text="Quadratic Equations and the Zero Product Property" sub="Quadratics and Complex Numbers" art=thumb
Every method in this course ends in the same place: a product equal to zero. So before any of them, it's worth knowing exactly why that place is special.

@math heading="Standard form" items="ax² + bx + c = 0@a x squared;;a ≠ 0@as long as a"
A quadratic equation in x is one you can write as a x squared, plus b x, plus c, equals zero, as long as a isn't zero. That's called standard form. If a were zero, the x squared term would vanish, and you'd be back to a linear equation.

@words text="x² − 9 = 0    x² + 3x = 0" sub="b = 0          c = 0"
b or c can be zero, and often are. x squared minus nine equals zero has no x term. x squared plus three x equals zero has no constant. Both are still quadratic.

@art parabola-crossings
A quadratic usually has two solutions. So an answer with one number in it is usually half an answer. And the check hasn't changed since linear equations: substitute, and see.

@chapter The property
@math heading="Zero product property" items="ab = 0  ⟺  a = 0 or b = 0@a times b"
Here's the rule. For real numbers, a times b equals zero exactly when a is zero or b is zero. The or is inclusive, so both can be zero. It only rules out the case where neither is.

@art three-switches
Think of a row of switches wired one after another. If any single switch is off, nothing gets through. A product with a zero factor is zero, and the property says the reverse too: a zero product must have a zero factor.

@math heading="Why it's true" items="ab = 0,  a ≠ 0@suppose;;(1/a)(ab) = (1/a) · 0@one over a;;((1/a) · a)b = 1 · b = b@regroup;;so b = 0@So b"
Suppose a times b is zero and a isn't zero. Then a has a reciprocal, one over a, so multiply both sides by it. The right side is zero. Regroup the left, and one over a times a is one, leaving just b. So b is zero.

@art clock-face
That proof needed every non-zero number to have a reciprocal. Without that, the rule can fail. On a twelve hour clock, three times four is twelve, which is zero on that clock, and neither three nor four is zero there. So this is a fact about the real numbers, not about algebra in general.

@chapter Only zero
@art equal-rectangles
Zero is the only number that works this way. If a times b is twelve, that tells you nothing. Three times four, two times six, and twenty four times one half all give twelve. A product can't land on zero unless a factor is already zero.

@math heading="(x − 3)(x + 5) = 9" items="x − 3 = 9 → x = 12  ✗@twelve;;(12 − 3)(12 + 5) = 9 · 17 = 153@a hundred and fifty three;;x² + 2x − 24 = 0@x squared plus two x"
So look at x minus three, times x plus five, equals nine. Setting x minus three to nine gives twelve, but twelve minus three times twelve plus five is nine times seventeen, which is a hundred and fifty three, not nine. The fix is to expand and move everything to one side: x squared plus two x minus twenty four equals zero.

@chapter More factors
@math heading="x(x − 2)(x + 7) = 0" items="x = 0@three solutions;;x − 2 = 0 → x = 2@two, and;;x + 7 = 0 → x = −7@and minus seven"
The property extends to any number of factors, by applying it again and again. x, times x minus two, times x plus seven, equals zero has three solutions: zero, two, and minus seven, one bracket at a time.

@chapter Don't divide
@art lost-solution
Now x squared equals five x. It's tempting to divide both sides by x and get five. But zero works too, because zero squared is five times zero. Dividing by x quietly assumed x wasn't zero, and that step threw the zero away.

@math heading="x² = 5x" items="x² − 5x = 0@move everything;;x(x − 5) = 0@factor;;x = 0 or x = 5@so x is zero"
Move everything to one side instead. x squared minus five x equals zero. Factor, x times x minus five. So x is zero or x is five. Nothing is lost, and it's one line longer.

@chapter Worked example
@math heading="(2x − 1)(x + 4) = 0" items="2x − 1 = 0  or  x + 4 = 0@the property gives;;x = 1/2  or  x = −4@one half"
Take two x minus one, times x plus four, equals zero. The property gives two linear equations: two x minus one equals zero, or x plus four equals zero. The first gives one half, the second minus four.

@art split-paths
And those are the only solutions. Any other x makes both brackets non-zero, and two non-zero real numbers can't multiply to zero. So nothing has been missed.

@chapter Where people slip
@list heading="Common slips" items="Splitting a product that isn't zero@The first|Dividing both sides by a variable@The second|Copying the bracket with the sign flipped@The third"
The first slip is splitting a product that isn't equal to zero. The second is dividing both sides by a variable, which loses a solution. The third is reading answers off the brackets by reflex. x minus four, times x plus two, equals zero gives four and minus two, not minus four and two. Each bracket is a small equation to solve.

@end text="Zero on one side, then split"
Try splitting products yourself, and see which ones you're allowed to split, on Learn. That's learn dot get er done dot I O.
