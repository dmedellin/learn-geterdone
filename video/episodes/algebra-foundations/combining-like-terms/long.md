---
format: long
lesson: algebra-foundations/combining-like-terms
title: Combining like terms: what makes two terms alike
thumb: Same letters, same exponents
---

@chapter The question
@title text="Combining Like Terms" sub="Algebra Foundations" art=thumb
When can two terms be added into one? Exactly when their variable parts match. The rule is short. The work is in seeing which terms qualify, and keeping the signs attached while you collect.

@art sorting-bins
Two terms are like terms when their variable parts are identical: the same letters, each raised to the same exponent. Five x squared y and minus two x squared y are like terms. Constants are all alike, since none of them has any letters.

@art letters-reorder
The order of the letters doesn't matter, because multiplication is commutative. Three x y and two y x have the same variable part, written two ways. Sorting the letters alphabetically inside every term is a cheap habit that makes this visible.

@chapter Why it works
@art common-factor
Why are you allowed to combine them? For any numbers a and b and any variable part v, a v plus b v is a plus b, times v. That's the distributive law, read from right to left. No new rule is needed.

@math heading="3x + 4y − x + 2y" items="x terms:   3x + (−x) = (3 − 1)x = 2x@the x terms;;y terms:   4y + 2y = (4 + 2)y = 6y@the y terms;;answer:   2x + 6y@two x plus six y"
Here's one. The x terms are three x and minus x, so three minus one gives two x. The y terms are four y and two y, which make six y. So the answer is two x plus six y.

@words text="−x contributes −1"
Notice that minus x contributes minus one. Not zero, and not plus one. That's the invisible coefficient doing real work. Treat minus x as nothing, and you'd get three x instead of two.

@chapter When terms aren't alike
@list heading="Not alike" items="x² and x³@different exponent|4x and 4y@different letters|5x²y and 2xy²@swapped|3x + 2(x + 1)@inside a bracket"
There are four ways two terms fail to be alike. A different exponent on the same letter, like x squared and x cubed. Different letters, like four x and four y. The same letters with the exponents swapped. And one term still inside a bracket that hasn't been expanded.

@art swapped-exponents
The swapped case is sneaky. Five x squared y and two x y squared look close. But at x equals two and y equals three, the first is sixty and the second is thirty six. They aren't even nearly interchangeable.

@art expand-first
The bracket case gives you the order for the whole subject: expand, then collect. Three x plus two times, x plus one, becomes three x plus two x plus two. Now there are like terms to combine.

@words text="3√2 + 5√2 = 8√2" sub="but √2 + √3 stays as it is"
This isn't only about letters. Three root two plus five root two is eight root two, for exactly the same reason. And root two plus root three can't be combined, for the same reason x plus y can't.

@chapter A full collection
@math heading="4a − 3b + 2a − b + 7" items="4a + (−3b) + 2a + (−b) + 7@attach every sign;;a terms:   (4 + 2)a = 6a@the a terms;;b terms:   (−3 − 1)b = −4b@the b terms;;answer:   6a − 4b + 7@seven has nothing"
Here's the worked example. First, attach every sign. The a terms give four plus two, which is six a. The b terms give minus three minus one, which is minus four b. The seven has nothing to join. So it's six a minus four b plus seven.

@words text="at a = 1, b = 1:   9 and 9"
Check at a equals one and b equals one. The original gives nine, and so does the answer. That catches a dropped term or a wrong sign, though it isn't a proof.

@art vanishing-group
Sometimes a whole group disappears. In two x plus three minus five minus two x, the x terms give two minus two, which is zero, so they vanish. Three minus five is minus two, and that's all that's left.

@chapter Where people slip
@list heading="Common slips" items="3x² + 5x² is 8x², not 8x⁴@adding the exponents|3x + 4y is not 7xy@seven x y|Dropping a subtracted term's sign@dropping the sign"
Three slips. Adding the exponents: three x squared plus five x squared is eight x squared, because the exponent never changes. Writing three x plus four y as seven x y. And dropping the sign of a subtracted term before you group.

@words text="x = 2, y = 1:   10 against 14" sub="3x + 4y  against  7xy"
That second one is worth testing. At x and y both equal to one, both sides are seven, which proves nothing. At x equals two and y equals one, it's ten against fourteen.

@chapter Try it
@words text="6a²b − a²b + 3ab²" sub="mark the groups first"
Try six a squared b, minus a squared b, plus three a b squared. Mark the groups before you touch any coefficients. Only the first two terms join, so you get five a squared b plus three a b squared. If you combined all three, the swapped exponents fooled you.

@end text="Group the terms yourself"
You can watch terms get sorted into groups by their variable parts, on Learn. That's learn dot get er done dot I O.
