---
format: long
lesson: accumulation-and-the-integral/the-constant-of-integration
title: The constant of integration: a family, and one value to pick
thumb: One value is exactly enough
---

@chapter The question
@title text="The Constant of Integration" sub="Accumulation and the Integral" art=thumb
Ask which function has a given rate, and you don't get one answer. You get a whole family. To pick out the one you want, you need exactly one more fact.

@art tank-levels
Picture a tank that gains water at two t litres per minute. The rate tells you how much arrives. It doesn't tell you how much was there to begin with. A tank that held four litres and one that held a hundred gain water identically.

@chapter A family
@art family-curves
T squared, t squared plus four, and t squared minus seven all have derivative two t. Their graphs are the same curve, moved up or down. So the antiderivatives of a rate form a family, F plus C, one for each constant C.

@math heading="Two antiderivatives differ by a constant" items="D = F − G,   D′ = 0@their difference;;D = c₀ + c₁t + … + c_k·tᵏ@Write D;;c₁ = 2c₂ = … = k·c_k = 0@every coefficient;;D = c₀@the constant term survives"
Does the family leave anything out? No. If F and G have the same derivative, their difference D has derivative zero. Write D out as a polynomial. Its derivative is zero only if every coefficient is zero, so only the constant term survives.

@art flat-derivative
A polynomial whose derivative is zero is flat: a constant. That proof is for polynomials, the only rates the lab accepts. For other functions the statement is true too, but it isn't proved here.

@chapter One value picks the member
@math heading="y′ = 2t,  y(1) = 5" items="y = t² + C@The family;;1² + C = 5@one squared;;C = 4,   y = t² + 4@So C"
Take y prime equals two t, with y of one equal to five. The family is t squared plus C. The given value says one squared plus C is five. So C is four, and y is t squared plus four. Notice that the tank's amount at zero was never given. It came out of the formula, as four.

@words text="y′ = f(t),   y(t₀) = y₀" sub="the simplest differential equation"
That pair, a rule for the rate and one value to start from, is the simplest differential equation there is. The rest of the subject is that same sentence, with harder rules.

@art second-value-clash
And one value is exactly enough. A second value either repeats the first, or contradicts it. T squared plus four already gives y of two equal to eight. Ask for y of two equal to nine as well, and you'd need C to be five and four at once.

@chapter The value isn't the constant
@art height-vs-constant
Take y prime equals three t squared, with y of two equal to zero. The family is t cubed plus C. Two cubed plus C is zero, so C is minus eight, and y is t cubed minus eight. The zero is a height on the curve, not the constant.

@math heading="C = y₀ − F(t₀)" items="y(1) = 5,  F(1) = 1:   C = 4@Five minus one;;y(2) = 0,  F(2) = 8:   C = −8@Zero minus eight"
In general, C is the given value minus F at that place. Five minus one is four. Zero minus eight is minus eight.

@chapter When C is the start
@art start-at-zero
The cubic preset is t cubed minus t, with y of zero equal to a half. Here F is t to the fourth over four, minus t squared over two, and F of zero is zero. So C is just a half. Start at zero, and C equals the starting value, which is why people come to think C is simply the start.

@chapter Where people slip
@list heading="Common slips" items="Taking C to be zero@The first|Copying the given value into C@The second|Dropping C because the total didn't need it@the third"
The first slip is taking C to be zero unless told otherwise. The second is copying the given value into C. From y of one equal to five, writing t squared plus five gives six at one. And the third is dropping C because the total didn't need it.

@art tank-levels
The tank shows why that matters. With C equal to four, it holds thirteen litres at three. With C equal to zero, nine. The rate fixes how the quantity changes. Only a value fixes where it is.

@chapter Try it
@words text="y′ = 3t²,  y(2) = 0" sub="start from F = t³"
Your turn, with the through zero preset. Start from F equals t cubed. Put two into t cubed plus C equals zero, and solve. Then check that your y has derivative three t squared, and value zero at two.

@end text="A family, and one value"
You can see the whole family of antiderivatives, and the one member through your point, on Learn. That's learn dot get er done dot I O.
