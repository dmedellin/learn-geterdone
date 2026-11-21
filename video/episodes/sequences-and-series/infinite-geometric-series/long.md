---
format: long
lesson: sequences-and-series/infinite-geometric-series
title: Infinite geometric series: what an endless sum really means
thumb: The number it approaches
---

@chapter Nobody adds for ever
@title text="Infinite Geometric Series" sub="Sequences and Series" art=thumb
Four plus two plus one plus a half, and on for ever. Does that have a sum? Nobody can add infinitely many numbers, so the answer has to be a definition, not a longer addition.

@art approach-line
Here's the definition. Form the partial sums, S one, S two, S three. If there's a number they get as close to as you like, and stay that close, the series converges, and that number is its sum. Otherwise it diverges, and has no sum at all.

@words text="2 + 6 + 18 + …     a₁/(1 − r) = −1" sub="a number, but not a sum"
Writing down a formula doesn't create a sum. For two plus six plus eighteen, the expression a one over one minus r returns minus one. But the partial sums run away, so minus one isn't a sum. The formula was used without a licence.

@chapter Why the ratio decides
@math heading="Split the finite sum" items="Sₙ = a₁/(1 − r)  −  [a₁/(1 − r)] · rⁿ@split the numerator"
Take the finite sum formula and split the numerator. The first piece is a constant. The second is that same constant times r to the n. So everything depends on r to the n.

@math heading="How fast rⁿ shrinks" items="(1/2)¹⁰ = 1/1024@a half to the tenth;;(9/10)¹⁰⁰  <  1/37000@nine tenths"
When the size of r is below one, it shrinks fast. A half to the tenth is one over a thousand and twenty four. Nine tenths to the hundredth is smaller than one over thirty seven thousand.

@math heading="The geometric series, settled" items="a₁ ≠ 0:   converges ⇔ |r| < 1@converges exactly;;S∞ = a₁/(1 − r)@a one over one minus r;;a₁ = 0:   S∞ = 0@every term is zero"
So, for a nonzero first term, the series converges exactly when the size of r is less than one, and then its sum is a one over one minus r. If a one is zero, every term is zero, and the sum is zero, whatever r is.

@art zigzag-approach
A negative ratio converges too, but from both sides. For a half minus a quarter plus an eighth, the sum is a third. S one is a half, too big. S two is a quarter, too small. The partial sums close in on a third, alternating around it.

@chapter When it fails
@art runaway
If the size of r is bigger than one, the terms grow without bound. The gap between consecutive partial sums is a term, so the sums move further and further apart. They can't be settling on anything. And when r is one, the sum is n times a one, which runs away too.

@art two-values
When r is minus one, the partial sums visit a one, zero, a one, zero, for ever, and approach neither. Those three cases cover every r whose size is at least one.

@chapter How close, after how many terms
@math heading="4 + 2 + 1 + 1/2 + …" items="S∞ = 4/(1 − 1/2) = 8@so the sum is eight;;8 − Sₙ = 8(1/2)ⁿ@the gap;;n = 12:   gap 1/512@twelve terms;;n = 13:   gap 1/1024  <  1/1000@thirteen"
Back to four plus two plus one. a one is four, r is a half, so the sum is eight. The gap after n terms is exactly eight times a half to the n. After twelve terms the gap is one over five hundred and twelve. After thirteen it's one over a thousand and twenty four, finally below a thousandth.

@art halving-bar
That gap is never zero. No partial sum ever equals eight. The sum is eight anyway, because sum means the number approached, not a number reached. That's why zero point nine nine nine recurring equals one stops being surprising.

@chapter Three wrong answers
@math heading="1 − 1 + 1 − 1 + …" items="(1 − 1) + (1 − 1) + …  →  0@suggests zero;;1 − (1 − 1) − (1 − 1) − …  →  1@suggests one;;a₁/(1 − r)  →  1/2@returns a half"
One minus one plus one minus one has r equal to minus one, so it has no sum. Bracket it in pairs and it suggests zero. Bracket it the other way and it suggests one. The formula returns a half. Three answers, and none is licensed. Moving brackets is allowed in a finite sum, and this isn't one.

@chapter Shrinking isn't enough
@art harmonic-groups
If a series converges, its terms must shrink to zero. But the reverse is false. In one plus a half plus a third plus a quarter, the terms shrink. Group them in blocks of one, two, four, eight, and each block is more than a half. So the partial sums pass every bound.

@list heading="Common slips" items="“The terms are shrinking, so it has a sum”@First|Reading S∞ as a total eventually reached@Second|Regrouping a divergent series@Third"
So, three slips. First, deciding there's a sum because the terms are getting smaller. Second, reading the sum as a total you eventually reach. Third, regrouping the terms of a divergent series.

@chapter Try it
@words text="3 − 1 + 1/3 − 1/9 + …" sub="r = −1/3 ·  find S∞, S₄ and the gap"
Your turn. Take three minus one plus a third minus a ninth. The ratio is minus one third, so a sum exists. Find it, add the first four terms, and work out the exact signed gap between them from the closed form. Then check its sign matches which side of the limit S four sits on.

@end text="How close, after how many terms"
You can pick a distance and see exactly how many terms it takes, on Learn. That's learn dot get er done dot I O.
