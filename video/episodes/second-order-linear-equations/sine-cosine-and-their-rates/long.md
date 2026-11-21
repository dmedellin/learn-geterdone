---
format: long
lesson: second-order-linear-equations/sine-cosine-and-their-rates
title: Why the rate of sine is cosine, and the rate of cosine is minus sine
thumb: Two rates, one sign flip
---

@chapter The question
@title text="Sine, Cosine and Their Rates" sub="Second-Order Linear Equations" art=thumb
The first second-order equation in this course is solved by two functions you already know, sine and cosine. The reason comes down to one fact about their rates.

@art sine-cosine-waves
Every rate you've worked out so far came out as a fraction, because the functions were polynomials. Sine and cosine aren't polynomials. At almost every place their values are irrational, so there's no neat column of fractions to read.

@words text="≈ 0.841471" sub="rounded to six significant figures"
So the lab works in ordinary floating point. It rounds each quotient to six significant figures, puts an approximately equals sign in front of it, and shows the number the column heads for.

@chapter The claim
@math heading="For t in radians" items="sin′ t = cos t@the rate of sine;;cos′ t = −sin t@the rate of cosine"
Here's the claim. For t measured in radians, the rate of sine at every t is cosine of t, and the rate of cosine at every t is minus sine of t.

@art secant-shrinking
Be clear about its status. A table of quotients that settle toward a number shows the pattern at the places you try. It can't show that the pattern continues for every smaller step, and no table can. So the course uses this as a claim, and says so once.

@chapter The column at zero
@math heading="sin at a = 0" items="h = 1:  ≈ 0.841471@h equals one;;h = 1/2:  ≈ 0.958851@Halve it;;h = 1/4:  ≈ 0.989616@zero point nine eight nine;;h = 1/8:  ≈ 0.997398@then zero point nine nine seven"
Start with sine at zero and a step of h equals one. The quotient is just sine of one, about zero point eight four one four seven one. Halve it and you get about zero point nine five eight eight five one, then zero point nine eight nine six one six, then zero point nine nine seven three nine eight.

@words text="→ 1 = cos 0" sub="the gap shrinks to about a quarter each halving"
The numbers climb toward one, which is cosine of zero. And the gap to one is cut to about a quarter each time you halve h. That's because the usual leading error depends on the second rate of sine at zero, and that's zero, so a smaller term is what's left.

@chapter The hidden sign
@art hilltop-tangent
Now cosine at zero. Its quotients start at about minus zero point four five nine six nine eight and shrink toward zero. Cosine is at the top of its hill there, not yet falling. But zero has no sign, so this column can't tell you the sign of the rate.

@art falling-tangent
The column at one can. Cosine is falling at one, so every quotient there is negative.

@math heading="cos at a = 1" items="h = 1:  cos 2 − cos 1 ≈ −0.956449@cosine of two minus cosine of one;;h = 1/64:  ≈ −0.845658@at h equals one over sixty four;;limit:  −sin 1 ≈ −0.841471@minus sine of one"
The first quotient is cosine of two minus cosine of one, about minus zero point nine five six four four nine. The last of seven, at h equals one over sixty four, is about minus zero point eight four five six five eight. They're heading for minus sine of one, about minus zero point eight four one four seven one.

@chapter Where people slip
@list heading="Common slips" items="The rate of cos is sin@The first|The last quotient is the rate@The second|Measuring in degrees@The third"
The first slip is taking the rate of cosine to be sine, because it's the other one. The second is reading the last quotient as the rate itself. For sine at one, it's about zero point five three three seven zero six, while cosine of one is about zero point five four zero three zero two. The third is measuring in degrees.

@art radians-vs-degrees
A degree is pi over one hundred and eighty of a radian. In degrees, the quotients of sine at zero would head for about zero point zero one seven four five three three, not one, and the two rates would no longer be each other's.

@chapter Twice flips the sign
@math heading="Take the rate twice" items="cos″ = (−sin)′ = −(sin′)@the rate of minus sine;;= −cos@which is minus cosine;;sin″ = (cos)′ = −sin@The same steps"
Now take a rate twice. The rate of cosine is minus sine, so the rate of the rate of cosine is the rate of minus sine, which is minus cosine. The same steps give sine double prime equals minus sine.

@art double-rate-flip
Each function is the negative of its own second rate. Written as an equation for an unknown y, that's y double prime equals minus y, or y double prime plus y equals zero. And that proof is only as firm as the two claims it uses.

@chapter Try it
@words text="sin at a = 1" sub="do the quotients head for cos 1 ≈ 0.540302?"
Your turn. Run the sine preset at one in the lab. Watch the quotients settle, note how far the last row still is from cosine of one, and ask yourself which way the gap is shrinking.

@end text="Halve h, watch the rate settle"
You can halve the step and watch sine and cosine trade rates, on Learn. That's learn dot get er done dot I O.
