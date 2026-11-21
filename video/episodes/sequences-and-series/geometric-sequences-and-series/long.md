---
format: long
lesson: sequences-and-series/geometric-sequences-and-series
title: Geometric sequences and series: the same multiplier every time
thumb: Multiply, shift, subtract
---

@chapter The same multiplier
@title text="Geometric Sequences and Series" sub="Sequences and Series" art=thumb
An arithmetic sequence adds the same number at every step. A geometric sequence multiplies by the same number instead. That small change gives you exponential growth, decay, and a sum formula that comes out of one line of cancelling.

@art growth-curve
A geometric sequence has a first term a one and a constant multiplier r, called the common ratio. Each term is r times the one before.

@math heading="Common ratios" items="3, 6, 12, 24, …   r = 2@equal to two;;81, 27, 9, 3, …   r = 1/3@one third;;5, −10, 20, −40, …   r = −2@minus two;;7, 0, 0, …   r = 0@seven, zero"
Three, six, twelve, twenty four has r equal to two. Eighty one, twenty seven, nine, three has r equal to one third, and shrinks. Five, minus ten, twenty, minus forty has r equal to minus two, and a negative ratio makes the signs alternate. And seven, zero, zero has r equal to zero.

@chapter Divide, don't subtract
@words text="3, 6, 12, 24" sub="differences 3, 6, 12 · ratios 2, 2, 2"
To find r, divide a term by the one before. Subtracting is the habit left over from arithmetic sequences. Three, six, twelve, twenty four has differences three, six, twelve, but ratios two, two, two. Only the ratios are constant.

@words text="2, 4, 6   vs   2, 4, 8" sub="the third term decides"
And check at least two ratios. Two, four, six and two, four, eight both start with a difference of two and a ratio of two. The third term decides which is which. If a term is zero, check the multiplication directly instead.

@chapter The n-th term
@math heading="The n-th term" items="aₙ = a₁rⁿ⁻¹@a n equals"
Getting from a one to a n takes n minus one multiplications by r, just as an arithmetic sequence takes n minus one additions of d. So a n equals a one times r to the n minus one.

@art shrinking-squares
If the size of r is bigger than one, the terms grow. If it's between zero and one, they decay, like eighty one, twenty seven, nine, three.

@art alternating-bars
For a positive r, the terms sit on an exponential curve. For a negative r, the sizes behave the same way, but the signs alternate.

@math heading="3, 6, 12, 24, …" items="a₁₀ = 3 · 2⁹ = 3(512) = 1536@three times two;;not  3 · 2¹⁰ = 3072@not three"
For three, six, twelve, the tenth term is three times two to the ninth, three times five hundred and twelve, which is fifteen hundred and thirty six. Not three times two to the tenth. That's the next term.

@chapter The sum
@art shift-cancel
Now the sum. Write S n, the first n terms. Multiply the whole line by r, and the terms all slide one place along. Subtract, and everything cancels except the first term of one line and the last term of the other.

@math heading="Multiply by r, subtract" items="Sₙ − rSₙ = a₁ − a₁rⁿ@all but two cancel;;Sₙ(1 − r) = a₁(1 − rⁿ)@factor both sides;;Sₙ = a₁(1 − rⁿ) / (1 − r),   r ≠ 1@divide by one minus r"
So all but two cancel: S n minus r S n is a one minus a one r to the n. Factor both sides. Then divide by one minus r, which you can only do when r isn't one. That gives the finite sum formula.

@math heading="S₁₀ of 3, 6, 12, …" items="S₁₀ = 3(1 − 1024) / (1 − 2) = 3(1023) = 3069@three times one minus;;3 + 6 + 12 + … + 1536 = 3069  ✓@adding the ten terms"
For three, six, twelve, the sum of ten terms is three times one minus a thousand and twenty four, over one minus two. That's three times a thousand and twenty three, three thousand and sixty nine. Adding the ten terms by hand gives the same.

@chapter The edge cases
@art flat-row
When r is one, every term is a one, so the sum is just n times a one. Put r equals one into the formula and you get zero over zero. That isn't a sign the sum is undefined. It's the trace of the division you weren't allowed to do.

@art one-then-zeros
When r is zero, the sequence is a one, then zeros. The formula gives a one, matching a one plus zero plus zero, so it needs no special case. And a finite sum doesn't need the terms to shrink. Growing or alternating is fine, as long as r isn't one.

@chapter Common slips
@list heading="Common slips" items="a₁rⁿ for the n-th term@First|Finding r by subtracting@Second|Putting r = 1 into the formula@Third"
First, writing a one r to the n, which is one term too far. At n equals one your formula must give a one. Second, finding r by subtracting. Third, putting r equals one into a formula that divides by one minus r.

@chapter Try it
@words text="81, −27, 9, −3, …" sub="r = −1/3 ·  find a₈ and S₈"
Your turn. Take eighty one, minus twenty seven, nine, minus three. The ratio is minus one third. Find the eighth term and the sum of the first eight from the formulas. Settle the sign of each power first, then add the eight terms directly to check.

@end text="Terms and finite sums, twice"
You can set a first term and a ratio, and compare every sum with the formula, on Learn. That's learn dot get er done dot I O.
