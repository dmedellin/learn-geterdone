---
format: long
lesson: rational-and-radical-expressions/solving-radical-equations
title: Solving radical equations: squaring adds a solution you don't want
thumb: Squaring can lie
---

@chapter Isolate, raise, check
@title text="Solving Radical Equations" sub="Rational and Radical Expressions" art=thumb
To solve a radical equation, isolate the radical and raise both sides to the index. The step is legal, and it isn't reversible. So it can produce numbers that solve the new equation and not the original. The check isn't proofreading. It's the last step of the method.

@words text="√(x + 7) = x − 5   is a radical equation" sub="√7 · x = 5 is not: the variable is outside"
A radical equation has the variable under a radical sign. The square root of x plus seven equals x minus five is one. Root seven times x equals five is not, because the variable is outside the root.

@art isolate
You met this in Solving Rational Equations, where clearing denominators could create a root. Here it comes from a different direction, and the cure is identical: substitute into the original.

@chapter Why squaring adds answers
@math heading="Raising both sides" items="a = b  ⟹  aⁿ = bⁿ@if a equals b;;n odd:  aⁿ = bⁿ  ⟹  a = b@for odd n;;n even:  aⁿ = bⁿ  ⟹  a = ±b@for even n"
If a equals b, then a to the n equals b to the n, for every positive whole number n. Going back works for odd n. But for even n, a to the n equals b to the n only tells you a is plus or minus b.

@art merged-equations
So squaring solves a equals b and a equals minus b at the same time, and the two solution sets come back mixed together. The extraneous root isn't a mistake. It's the correct consequence of a legal step.

@chapter The key example
@math heading="√(x + 7) = x − 5" items="x + 7 = x² − 10x + 25@squares to;;x² − 11x + 18 = 0@rearranges;;(x − 2)(x − 9) = 0@factors;;candidates: 2 and 9@the candidates"
Follow it through. The square root of x plus seven equals x minus five squares to x plus seven equals x squared minus ten x plus twenty five. That rearranges to x squared minus eleven x plus eighteen equals zero, which factors as x minus two times x minus nine. The candidates are two and nine.

@math heading="Check in the original" items="x = 9:  √16 = 4   and   9 − 5 = 4   ✓@at nine;;x = 2:  √9 = 3   and   2 − 5 = −3   ✗@at two;;solution set: {9}@solution set"
At nine, the left side is root sixteen, four, and the right side is four. It works. At two, the left side is root nine, three, but the right side is minus three. It fails. The solution set is just nine.

@art one-crossing
Two isn't random, though. It solves the square root of x plus seven equals minus, x minus five, the other equation that squaring quietly included. There's also a shortcut: a principal root is never negative, so x minus five must be at least zero, and x at least five. That alone rules out two.

@chapter Seen without algebra
@art never-negative
Here's a quick one. The square root of x plus one equals minus three. No work is needed. A principal square root is never negative, so there's no solution.

@math items="√(x + 1) = −3@minus three;;x + 1 = 9  →  x = 8@squaring;;x = 8:  √9 = 3 ≠ −3  ✗@check eight"
But squaring produces x plus one equals nine, and the confident answer, x equals eight. Check eight: root nine is three, not minus three. Entirely extraneous. The equation had no solution before the first step.

@chapter Two radicals
@math heading="√(x + 5) − √x = 1" items="√(x + 5) = 1 + √x@move root x;;x + 5 = 1 + 2√x + x@squaring gives;;4 = 2√x,   √x = 2@so four;;x = 4@x equals four"
With two radicals, isolate one before squaring. Here, move root x across, to get root x plus five equals one plus root x. Squaring gives x plus five equals one plus two root x plus x. Keep that middle term. So four equals two root x, root x is two, and x equals four.

@art candidate-check
Check it in the original. Root nine minus root four is three minus two, which is one. It works. Two squarings, one surviving solution.

@art two-way-arrow
For an odd index, there's no extraneous root problem, because cubing is reversible. A cubed equals b cubed forces a equals b for real numbers. The check is still good insurance for arithmetic, but it's no longer part of the logic.

@chapter Where people slip
@list heading="Common slips" items="Squaring term by term@The first|Squaring before isolating@The second|Treating the check as optional@the third"
The first slip is squaring term by term. x minus five squared is x squared minus ten x plus twenty five, not x squared minus twenty five. The second is squaring before isolating, which leaves a cross term with a root still in it. And the third is treating the check as optional. Without it, you'd answer two and nine.

@chapter Try it
@words text="√(2x + 3) = x" sub="the right side can't be negative, so x ≥ 0"
Your turn. Solve the square root of two x plus three equals x. A principal square root can't equal a negative number, so x is at least zero. Square, factor the quadratic, and check both candidates in the original.

@end text="Isolate, square, check"
You can practise spotting extraneous roots on Learn. That's learn dot get er done dot I O.
