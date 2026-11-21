---
format: long
lesson: linear-equations-and-inequalities/linear-inequalities
title: Linear inequalities and the one rule that flips the sign
thumb: Negative? Flip the sign
---

@chapter Same moves, one exception
@title text="Linear Inequalities" sub="Linear Equations and Inequalities" art=thumb
You solve an inequality with the same moves as an equation, with exactly one exception. And the answer isn't a single number any more. It's a whole set of them.

@art number-line-ray
A linear inequality looks like a x plus b is less than c, or the same with another relation. Its solution set is every number that makes it true. Three x minus four is less than eleven holds at zero, at four, and at every number below five. So the answer is x less than five.

@art filled-hollow
Less than is strict, and less than or equal to is not. That's not decoration: x less than or equal to five contains five, and x less than five doesn't. On a number line, it's a filled endpoint or a hollow one.

@chapter What you may do
@list heading="Both sides" items="Add or subtract anything: unchanged@add or subtract|Multiply or divide by a positive: unchanged@by a positive number|Multiply or divide by a negative: REVERSED@by a negative number|Multiply or divide by anything with x: not allowed@anything containing x"
Here are the rules for both sides. Add or subtract any number, or any expression in x, and the relation stays the same. Multiply or divide by a positive number: same. Multiply or divide by a negative number, and the relation reverses. And multiplying or dividing by anything containing x isn't allowed at all, because you don't know its sign.

@chapter Why a negative flips it
@art flip-negative
Three is less than five. That's true. Multiply both sides by minus one and you get minus three and minus five. On the number line, minus three sits to the right of minus five. So minus three is greater than minus five. The relation had to turn round, or the statement would have become false.

@words text="If a < b and c < 0, then ac > bc" sub="a theorem, not a convention"
And it's a theorem, not a convention. If a is less than b, then b minus a is positive. If c is negative, minus c is positive. Their product is positive, and expanding it gives a c minus b c is positive. That says exactly that a c is greater than b c.

@chapter Never divide by x
@math heading="3x > 5x" items="÷ x:  3 > 5   so no solutions?   WRONG@divide by x;;− 3x:  0 > 2x@subtract three x;;0 > x,  so x < 0@divide by two;;x = −1:  −3 > −5  ✓@at minus one"
Try three x is greater than five x. Divide by x, and you get three is greater than five. False, so no solutions? Wrong. Instead, subtract three x: zero is greater than two x. Divide by two: x is less than zero. Check at minus one: minus three is greater than minus five. True.

@art no-divide-x
So whenever a step would divide by something with the variable in it, collect terms instead. You never know the sign of x, so you can never divide by it.

@chapter Choosing the side
@math heading="5 − 3x ≥ 2x + 15, route A" items="5 ≥ 5x + 15@add three x;;−10 ≥ 5x@subtract fifteen;;−2 ≥ x,  that is x ≤ −2@divide by five"
Here's five minus three x is at least two x plus fifteen. Route A: add three x, and five is at least five x plus fifteen. Subtract fifteen: minus ten is at least five x. Divide by five, a positive number: minus two is at least x. Which means x is at most minus two.

@math heading="Route B" items="5 − 5x ≥ 15@subtract two x;;−5x ≥ 10@subtract five;;x ≤ −2   sign REVERSED@divide by minus five"
Route B: subtract two x instead, and five minus five x is at least fifteen. Subtract five: minus five x is at least ten. Now divide by minus five, and the sign reverses: x is at most minus two. Same answer.

@art two-routes
Check it: at minus two both sides are eleven, and eleven is at least eleven. At zero, five is at least fifteen is false. Route A avoided the reversal by collecting x where its coefficient was larger. But it asks you to read minus two is at least x correctly, because turning a statement round reverses the relation too.

@chapter When x disappears
@art all-or-nothing
Sometimes x cancels. Two x plus one is greater than two x reduces to one is greater than zero, true whatever x is, so every real number is a solution. Two x plus one is less than two x reduces to one is less than zero, which is false, so no number works.

@list heading="Common slips" items="Reversing because a minus sign appeared@The first|Dividing by something containing x@The second|Swapping sides without reversing@The third"
Three slips. The first is reversing because a minus sign appeared. x plus five is less than two gives x less than minus three, and nothing reverses, because you only subtracted. The second is dividing by x. The third is turning a statement round without turning the relation round.

@chapter Try it
@words text="3x − 4 < 11" sub="solve it, then test x = 0 and x = 5"
For practice, solve three x minus four is less than eleven. Then test zero, which should pass, and five, which should fail. The answer is a set. Writing x equals five would report a number that fails.

@end text="Watch the sign flip"
You can solve inequalities step by step and test values on Learn. That's learn dot get er done dot I O. See you in the next one.
