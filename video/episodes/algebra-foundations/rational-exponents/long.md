---
format: long
lesson: algebra-foundations/rational-exponents
title: Rational exponents: why x to the 1/2 has to be a square root
thumb: The laws decide what it means
---

@chapter The gap
@title text="Rational Exponents" sub="Algebra Foundations" art=thumb
What does x to the one half mean? Nothing so far tells you. You could invent a meaning. Instead, ask which meaning keeps the exponent laws true. There's only one, and everything else follows from it.

@art gap-fill
You've seen this move before. x to the zero is one, because x to the n times x to the zero has to be x to the n. A negative exponent was settled the same way. x to the one half is the next gap, and it's filled in the same way.

@chapter What the laws force
@art halves-make-whole
Take x to the one over n, and multiply it by itself n times. The product law says add the exponents. That's one over n, added n times, which is one. So the product is x to the one, which is just x.

@art three-thirds
With n equal to three, that's three copies of x to the one third. A third, plus a third, plus a third, is one whole.

@math items="(x^(1/n))ⁿ = x^(n · 1/n) = x¹ = x@x to the one over n;;so x^(1/n) is an n-th root of x@an n th root"
So x to the one over n is a number whose n th power is x. That's exactly an n th root of x. The notation wasn't chosen to be memorable. It was forced.

@words text="x^(1/n) ≥ 0" sub="the only arbitrary part"
One thing is still open. When n is even and x is positive, there are two candidates. Two and minus two, raised to the fourth, both give sixteen. So a convention picks the root that isn't negative, just like the radical sign. That's the only arbitrary part.

@chapter Root and power
@math heading="x^(p/q), for x ≥ 0" items="= (q-th root of x)^p@the q th root of x;;= q-th root of (x^p)@of x to the p"
For x at least zero, x to the p over q means the q th root of x, raised to the power p. By the power of a power law, it's also the q th root of x to the p. Both name the same number, so take whichever is easier.

@math heading="8^(2/3)" items="root first:   ∛8 = 2,   2² = 4@root first;;power first:   8² = 64,   ∛64 = 4@power first"
Eight to the two thirds. Root first: the cube root of eight is two, and two squared is four. Power first: eight squared is sixty four, and the cube root of sixty four is four. They agree.

@art root-first
Both routes are legal, but take the root first anyway. Twenty seven to the four thirds, root first, is three to the fourth, which is eighty one. Power first, you'd need the cube root of five hundred thirty one thousand, four hundred forty one. Same answer, far bigger numbers.

@chapter Negative exponents
@art reciprocal-flip
A negative exponent works exactly as before. x to the minus p over q is one over x to the p over q. The minus sign makes a reciprocal, never a negative number.

@math items="16^(−3/4) = 1 / 16^(3/4)@sixteen to the minus three quarters;;⁴√16 = 2,   2³ = 8@fourth root of sixteen;;= 1/8@one eighth"
So sixteen to the minus three quarters is one over sixteen to the three quarters. The fourth root of sixteen is two, and two cubed is eight. The answer is one eighth.

@chapter Why the base can't be negative
@math heading="(−8)^(2/6)" items="root first:   6th root of −8, not real@root first;;power first:   (−8)² = 64,   6th root = 2@power first;;but 2/6 = 1/3,   and (−8)^(1/3) = −2@but two sixths"
Now allow a negative base, and try minus eight to the two sixths. Root first, the sixth root of minus eight isn't a real number. Power first, minus eight squared is sixty four, and its sixth root is two. But two sixths is one third, and minus eight to the one third is minus two.

@art three-readings
Three readings of one symbol: no value, two, and minus two. Requiring the base to be at least zero removes the problem at the source, and it costs nothing. When you want the cube root of minus eight, write it as a root, where it's clearly minus two.

@chapter The laws, unchanged
@math items="x^(1/2) · x^(1/3) = x^(5/6)@a half plus a third;;(x⁶)^(1/3) = x²@x to the sixth;;(8x⁶)^(2/3) = 4x⁴@eight x to the sixth"
And the payoff: every exponent law now works with fractions, with no new cases. x to the half times x to the third is x to the five sixths, because a half plus a third is five sixths. x to the sixth, to the one third, is x squared. And eight x to the sixth, to the two thirds, is four x to the fourth.

@chapter Where people slip
@list heading="Common slips" items="Reading the exponent as a multiplier@as a multiplier|Expecting a negative answer from a negative exponent@a negative answer|Using a negative base@a negative base"
Three slips. Reading the exponent as a multiplier: eight to the two thirds isn't eight times two thirds. Thinking a negative exponent gives a negative answer: nine to the minus one half is one third. And applying rational exponents to a negative base.

@chapter Try it
@words text="27^(2/3)" sub="cube root first"
Try twenty seven to the two thirds. Take the cube root first, then finish. The root is three, and squaring gives nine. If you got six, you treated the exponent as multiplication.

@end text="One power, computed both ways"
You can compute any rational power by both routes, and see when they disagree, on Learn. That's learn dot get er done dot I O.
