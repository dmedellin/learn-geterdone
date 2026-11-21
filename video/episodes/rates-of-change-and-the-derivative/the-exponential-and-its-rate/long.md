---
format: long
lesson: rates-of-change-and-the-derivative/the-exponential-and-its-rate
title: The exponential and its rate: why e is special
thumb: A rate proportional to itself
---

@chapter Something new
@title text="The Exponential and Its Rate" sub="Rates of Change and the Derivative" art=thumb
Every function so far, apart from one over t, has been a polynomial, with quotients that come out as exact fractions. Exponentials are different. For the first time, some of the numbers will be rounded.

@art exponential-curve
An exponential like two to the t has its variable in the exponent. As t grows, the curve climbs faster and faster. So what's its rate?

@chapter The quotient factors
@math heading="b^(a + h) − b^a" items="= b^a·b^h − b^a@b to the a times b to the h;;= b^a·(b^h − 1)@So the difference;;quotient:  b^a·(b^h − 1)/h@Divide by h"
Start with the law of exponents. B to the a plus h is b to the a times b to the h. So the difference is b to the a, times b to the h minus one. Divide by h, and the quotient is b to the a, times b to the h minus one, over h.

@words text="(b^h − 1)/h" sub="no a in it at all"
That's exact algebra. Nothing is dropped. And look at that second factor. It contains the base and the step, but nothing about the place. So one column of numbers serves every place.

@chapter The column for two
@math heading="b = 2,  a = 0:  (2^h − 1)/h" items="h = 1:  1    exact@a step of one;;h = 1/2:  2(√2 − 1) ≈ 0.828427@With a half;;h = 1/4:  ≈ 0.756828@A quarter;;h = 1/64:  ≈ 0.696914@one sixty fourth"
Take base two. With a step of one, the factor is two minus one, over one, exactly one. With a half, it's two times root two minus one, which has no finite decimal: about zero point eight two eight four. A quarter gives about zero point seven five six eight. And by one sixty fourth, it's about zero point six nine six nine.

@art sinking-column
From the second row on, every figure is rounded, and the lab marks it with an approximately sign. The column keeps sinking, toward about zero point six nine three one four seven.

@chapter The rate of an exponential
@math heading="The exponential's rate" items="(b^h − 1)/h → ln b@heads for;;(bᵗ)′ = ln b · bᵗ@So the rate;;b = 2:  ln 2 ≈ 0.693147@For two"
For each positive base, the column heads for a number written l n b, the natural log of b. So the rate of b to the t, at every t, is l n b times b to the t. For two, that constant is about zero point six nine three one four seven.

@words text="stated, not proved" sub="the factoring is proved; the constant is claimed"
Be clear about what's proved. The factoring is. That the rounded column settles on one number is what the table suggests, and the lesson states it without proof. No table of seven rows establishes it for every step.

@chapter Other bases, and e
@art three-bases
For base three, the first quotient is exactly two, and the column heads for about one point zero nine eight six. For base e, every quotient is rounded, since e isn't a fraction. The first is e minus one, about one point seven one eight, and the column heads for one.

@words text="(eᵗ)′ = eᵗ" sub="e ≈ 2.71828"
That's what makes e special. Of all the bases, e, about two point seven one eight two eight, is the one whose rate is the exponential itself.

@chapter Another place
@art scaled-column
Now move to three, with base two. A step of one gives sixteen minus eight, which is eight: exactly two cubed times the first entry at zero. Every row is eight times the matching row. So the rate of two to the t at three is eight times l n two, about five point five four five.

@art rate-equals-height
That's the whole story. An exponential's rate is proportional to the function itself: the taller the curve, the steeper it climbs. A rate that's a constant times the quantity is exactly what the equation y prime equals k y says, and that equation comes back later.

@chapter Where people slip
@art power-rule-flat
The big slip is applying the power rule to two to the t. That would give t times two to the t minus one, which is zero at zero. But the quotients at zero head for about zero point six nine three. The power rule is for a variable base and a fixed exponent.

@list heading="Two more slips" items="Quoting a rounded figure as exact@a rounded figure|Expecting the constant to change with the place@change with the place"
Two more. Don't quote a rounded figure as if it were exact. Write approximately whenever it was rounded. And don't expect the constant to change with the place. The place only comes in through the factor b to the a.

@chapter Try it
@words text="b = 3,  a = 0" sub="first entry 2 · heads for ≈ 1.09861"
Your turn. Take base three at zero. The first entry should be two, and the column should head for about one point zero nine eight six one, which is l n three.

@end text="One column, every place"
You can watch the column sink toward l n b for any base, on Learn. That's learn dot get er done dot I O.
