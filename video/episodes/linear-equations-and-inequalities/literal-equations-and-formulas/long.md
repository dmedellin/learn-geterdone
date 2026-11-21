---
format: long
lesson: linear-equations-and-inequalities/literal-equations-and-formulas
title: Rearranging formulas: solving for one letter among many
thumb: Solve for the letter you need
---

@chapter Why rearrange
@title text="Literal Equations and Formulas" sub="Linear Equations and Inequalities" art=thumb
A formula is just an equation with several letters in it. You rearrange it with the same four moves you already know. Only two things are new, and both are about what the answer looks like.

@art formula-letters
An equation with more than one letter is called a literal equation. To solve it for a named letter means to get that letter alone on one side, and absent from the other. Formulas are the usual example.

@art rearrange-once
Why bother? Say you need to convert twenty temperatures from Fahrenheit to Celsius. Solving the formula twenty times is twenty problems. Rearranging it once gives you a formula you just evaluate twenty times.

@chapter Fahrenheit to Celsius
@math heading="F = (9/5)C + 32, solve for C" items="F − 32 = (9/5)C@subtract thirty two;;(5/9)(F − 32) = C@five ninths;;C = (5/9)(F − 32)@five ninths of F minus thirty two"
Start from F equals nine fifths C plus thirty two. Subtract thirty two from both sides: F minus thirty two equals nine fifths C. Multiply both sides by five ninths. And there it is: C equals five ninths of F minus thirty two.

@math heading="Check with C = 100" items="F = (9/5)(100) + 32 = 180 + 32 = 212@two hundred and twelve;;(5/9)(212 − 32) = (5/9)(180) = 100@back to one hundred"
Check it. A hundred degrees Celsius gives nine fifths of a hundred, plus thirty two, which is a hundred and eighty plus thirty two, or two hundred and twelve. And five ninths of two hundred and twelve minus thirty two is five ninths of a hundred and eighty, back to one hundred.

@chapter When the letter appears twice
@math heading="S = C + rC, solve for C" items="S = C(1 + r)@factor;;C = S/(1 + r)@divide by one plus r;;provided 1 + r ≠ 0@as long as"
Undoing one operation at a time can't isolate a letter that appears twice. So gather its terms, and factor. S equals C plus r C. Factor out C: S equals C times one plus r. Then divide by one plus r, so C equals S over one plus r, as long as one plus r isn't zero.

@art factor-out
Watch the one. C on its own is one times C. Forget that, and you'd write S equals C times r, which is a different formula. And C equals S minus r C isn't an answer either, because C is still on the right.

@chapter When it's on both sides
@math heading="ax + b = cx + d, solve for x" items="ax − cx + b = d@subtract c x;;ax − cx = d − b@subtract b;;(a − c)x = d − b@factor x;;x = (d − b)/(a − c)@divide by a minus c"
If the target letter starts on both sides, collect it first, exactly as with numbers. a x plus b equals c x plus d. Subtract c x, then subtract b: a x minus c x equals d minus b. Factor x out, then divide by a minus c. So x equals d minus b, over a minus c.

@art collect-target
That's valid only when a minus c isn't zero. If it is zero, you can't divide, and the equation is read the other way: if b equals d, every x works, and if not, none does. The condition marks a real change in the answer.

@chapter The condition on the division
@art forbidden-divisor
Every division by a letter carries a condition. Solve a equals one half b h for h, and you get h equals two a over b, valid when b isn't zero. Sometimes the forbidden value hides. In C equals S over one plus r, it's r equals minus one, not r equals zero. Read the divisor, not the letter.

@chapter Where people slip
@list heading="Common slips" items="Cancelling a term, not a factor@The first|Stopping with the target on both sides@The second|Dividing without stating the condition@The third"
Three slips. The first is cancelling a letter that's a term rather than a factor. The second is stopping while the target letter is still on both sides. And the third is dividing by a letter without saying when it's nonzero.

@math heading="(A − P)/(Pt) at A = 230, P = 200, t = 3" items="cancel P wrongly: (A − 1)/t = 229/3@cross out the P;;true value: 1/20@true value;;legal: (A/P − 1)/t = 1/20@divide the whole numerator"
That first slip, in numbers. A minus P, over P t, at A two hundred and thirty, P two hundred, t three. Cross out the P and you get two hundred and twenty nine thirds. The true value is one twentieth. Divide the whole numerator by P instead, and A over P minus one, over t, gives one twentieth.

@chapter Try it
@art square-two-roots
One formula this method can't rearrange is a equals s squared. Undoing a square needs a square root, which gives two answers, and that's for a later course. For practice, take S equals C plus r C, solve it for r instead of C, and write down your condition when you divide.

@end text="Solve for any letter"
You can rearrange formulas and check them with numbers on Learn. That's learn dot get er done dot I O. See you in the next one.
