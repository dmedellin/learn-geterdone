---
format: long
lesson: exponential-and-logarithmic-functions/change-of-base
title: Change of base: any logarithm from the two keys you have
thumb: Argument on top, base below
---

@chapter Two keys, infinitely many bases
@title text="Change of Base" sub="Exponential and Logarithmic Functions" art=thumb
A calculator offers two bases, and there are infinitely many. Log base two of ten is a perfectly definite number. It's the exponent that turns two into ten, and it's between three and four. But there's no key for it.

@art missing-key
One identity closes the gap. It takes two lines to derive, and the derivation is worth knowing, because it's what keeps the top and bottom the right way up.

@chapter The identity
@math heading="Change of base" items="log_b(x) = log_c(x) / log_c(b)@log base b of x equals;;b, c > 0,   b ≠ 1,   c ≠ 1,   x > 0@as long as"
Here it is. Log base b of x equals log base c of x, over log base c of b, for any base c you can compute, as long as both bases are positive and not one, and x is positive.

@math heading="Why it's true" items="y = log_b(x)    ⟺    bʸ = x@Let y be;;log_c(bʸ) = log_c(x)@apply log base c;;y·log_c(b) = log_c(x)@The power law;;y = log_c(x) / log_c(b)@Divide"
Let y be log base b of x, which means b to the y equals x. Equal numbers have equal logarithms, so apply log base c to both sides. The power law brings the y down in front. Divide by log base c of b, which is allowed, because it's zero only when b is one.

@art fraction-stack
So the argument goes on top, and the base of the answer goes underneath. Log base two of ten is ln ten over ln two.

@chapter Log base two of ten
@math heading="log₂(10)" items="log 10 / log 2 = 1.000000 / 0.301030 ≈ 3.321928@log ten over log two;;ln 10 / ln 2 = 2.302585 / 0.693147 ≈ 3.321928@ln ten over ln two;;check:   2³ = 8 < 10 < 16 = 2⁴@the check"
With common logs, log ten over log two is one over point three zero one zero three, about three point three two one nine. With natural logs, ln ten over ln two gives the same value. And the check: two cubed is eight and two to the fourth is sixteen, so it must be between three and four.

@art upside-down
Flip the fraction and you get ln two over ln ten, about point three zero one. The calculator returns it without complaint. But it's log base ten of two, the reciprocal. Only the bracket, or the derivation, tells you it's wrong.

@chapter Two corollaries
@words text="log_b(x) = 1 / log_x(b)" sub="log₂(8) = 3        log₈(2) = 1/3"
Put c equal to x, and the identity collapses: log base b of x is one over log base x of b. Log base two of eight is three, and log base eight of two is one third.

@art stretched-logs
Put c equal to e, and log base b of x is one over ln b, times ln x. So every logarithm is a fixed multiple of the natural one. For base two, the multiple is about one point four four. For base ten, about point four three four. Bases differ by a scale, never by a shape.

@chapter An exact answer stays exact
@math heading="log₈(32)" items="log₈(32) = log₂(32) / log₂(8) = 5/3@change to base two;;check:   8^(5/3) = (2³)^(5/3) = 2⁵ = 32@To check"
Changing base doesn't force a decimal. Take log base eight of thirty two. Both numbers are powers of two, so change to base two, and you get five over three. To check, eight to the five thirds is two cubed to the five thirds, which is two to the fifth, thirty two.

@chapter The trap, on numbers
@math heading="log₅(40)" items="log 40 / log 5 = 1.602060 / 0.698970 ≈ 2.292030@The identity;;✗   log(40/5) = log 8 ≈ 0.903090@log of forty over five;;✗   log 40 − log 5 = log 8@log forty minus log five"
Take log base five of forty. The identity gives log forty over log five, about two point two nine two. It gets confused with log of forty over five, which is log eight, about point nine zero three, and with log forty minus log five, which is the same log eight.

@art bracket-check
A bracket rejects both without any arithmetic. Five squared is twenty five and five cubed is a hundred and twenty five, so the answer must lie between two and three. Log eight doesn't.

@art three-routes
The helper base also gives you a free check. Any legal helper works, so three different ones must give quotients that look nothing alike, yet agree to every digit. Base ten, base e and base two all give two point two nine two zero three.

@chapter Where people slip
@list heading="Common slips" items="Putting the base on top@The first|Turning the quotient into a difference@The second|A decimal where a fraction was available@The third"
The first is putting the base on top, which gives the reciprocal. The second is turning the quotient into a difference. For forty and five in base e, those are about two point two nine two and two point oh seven nine: close enough to look right. The third is giving a decimal where a fraction was available.

@chapter Try it
@words text="log₉(50)" sub="bracket:   9¹ < 50 < 9²"
Your turn. Find log base nine of fifty. The bracket is given: nine is less than fifty, which is less than eighty one, so the answer is between one and two. Complete ln fifty over the right thing, round only at the end, and use the bracket to reject the reversed fraction.

@end text="Three helper bases, one value"
You can compute the same logarithm through three helper bases and watch them agree, on Learn. That's learn dot get er done dot I O.
