---
format: long
lesson: accumulation-and-the-integral/the-antiderivative-and-the-fundamental-theorem
title: The antiderivative and the fundamental theorem: a total in one subtraction
thumb: No pieces to add
---

@chapter Where the total comes from
@title text="The Antiderivative and the Fundamental Theorem" sub="Accumulation and the Integral" art=thumb
For three lessons, every sum was compared with an exact total printed beside it. Where did that total come from? Not from adding pieces. It came from running the derivative backwards.

@art backwards-arrow
Given a rate f, look for a function F whose rate of change is f. That's called an antiderivative. If you can find one, the total change can be read straight off its two ends.

@chapter Reverse the power rule
@math heading="Antiderivative:  F′ = f" items="c·tⁿ  →  c·tⁿ⁺¹/(n + 1)@c t to the n;;c  →  c·t@a constant c"
For a polynomial, you find it term by term. A term c t to the n becomes c t to the n plus one, over n plus one: one power higher, divided by the new power. And a constant c becomes c t. It's the power rule, read from right to left.

@math heading="f(t) = t²" items="raise the power:  t³@Raise the power;;divide by the new power:  t³/3@Divide by the new power;;check:  (t³/3)′ = 3t²/3 = t²  ✓@check"
Take t squared. Raise the power to get t cubed. Divide by the new power to get t cubed over three. And check: the derivative of t cubed over three is three t squared over three, which is t squared. It passes.

@chapter The total, in one subtraction
@math heading="t² on [0, 1]" items="F(1) − F(0) = 1/3 − 0 = 1/3@F of one minus F of zero;;left sums:  7/32,  35/128,  155/512@the left sums"
So F of one minus F of zero is a third minus zero: a third. And the left sums from before were seven thirty seconds, thirty five over one hundred and twenty eight, and one hundred and fifty five over five hundred and twelve, each a little nearer a third, and none of them equal to it.

@art pincer
The right sums close in from above: fifteen thirty seconds, fifty one over one hundred and twenty eight, one hundred and eighty seven over five hundred and twelve. A third sits between every pair.

@art area-under-parabola
One subtraction gives exactly the number the sums were closing in on. The antiderivative isn't an estimate of the total. It is the total.

@chapter Why it's plausible
@art telescoping-steps
Cut the interval into pieces. The changes of F across the pieces add up to F of b minus F of a, exactly, because every value in the middle is added once and subtracted once. For the ramp two t, with F equal to t squared, the four piece changes are a quarter, three quarters, five quarters and seven quarters. They add to four.

@art flat-guess
The left sum charges those same pieces zero, a half, one and three halves, adding to three. Each is a flat guess at the change in F, and a good one, because F prime is f. Over a short piece, F changes by about its rate times the width, and shorter pieces make each guess better.

@chapter The fundamental theorem
@words text="If F′ = f:  total change = F(b) − F(a)" sub="the sums approach it: stated, not proved"
That's the fundamental theorem, as the lab demonstrates it. If F prime is f, the left and right sums approach F of b minus F of a, and that's the total change. The telescoping is exact algebra. That the sums approach it is what the tables show, and a first analysis course proves.

@art shifted-antiderivatives
A constant added to F changes nothing. If G is F plus five, the five is added at both ends and subtracted once. So the total doesn't depend on which antiderivative you chose.

@chapter A rate with three terms
@math heading="3t² − 4t + 1 on [1, 3]" items="F = t³ − 2t² + t@Term by term;;F(3) = 27 − 18 + 3 = 12@F of three;;F(1) = 1 − 2 + 1 = 0@F of one;;total:  12 − 0 = 12@twelve minus zero"
Take three t squared minus four t plus one, from one to three. Term by term, F is t cubed minus two t squared plus t. F of three is twenty seven minus eighteen plus three, twelve. F of one is one minus two plus one, zero. So the total is twelve minus zero, twelve, however many pieces you'd choose, because none were used.

@chapter Where people slip
@list heading="Common slips" items="Raising the power, forgetting to divide@The first|Thinking the constant changes the total@The second|Taking the demonstration for a proof@the third"
The first slip is raising the power and forgetting to divide. Write t cubed for t squared, and its derivative is three t squared, three times too much. The slip hides on two t, where two t squared over two is just t squared. The second is thinking the constant changes the total. And the third is taking the demonstration for a proof.

@chapter Try it
@words text="3t² − 4t + 1" sub="the terms become t³, −2t² and t"
Your turn. On the mixed preset, the three terms become t cubed, minus two t squared, and t. Differentiate your result to see three t squared minus four t plus one come back. Then evaluate at three and at one, and subtract.

@end text="Run the derivative backwards"
You can compare every sum with the antiderivative's exact total, on Learn. That's learn dot get er done dot I O.
