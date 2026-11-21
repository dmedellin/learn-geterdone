---
format: long
lesson: polynomials-and-factoring/the-factor-theorem-and-rational-roots
title: The factor theorem and rational roots: factoring a cubic by search
thumb: A root hands you a factor
---

@chapter The question
@title text="The Factor Theorem and Rational Roots" sub="Polynomials and Factoring" art=thumb
How do you factor a cubic? Grouping might work, or it might not. What you want is a method that always finishes, even when the answer is that there's nothing to find. Two theorems give you exactly that.

@chapter The factor theorem
@math heading="The factor theorem" items="f(c) = 0  ⟺  (x − c) is a factor of f@if and only if"
For a polynomial f and a number c, x minus c is a factor of f if and only if f of c is zero.

@math heading="Why" items="f(x) = (x − c)q(x) + f(c)@remainder theorem;;f(c) = 0  →  f(x) = (x − c)q(x)@if f of c is zero"
By the remainder theorem, f of x equals x minus c, times q of x, plus f of c. So if f of c is zero, that reads f of x equals x minus c times q of x. And x minus c is a factor. The other direction is just as short: substitute x equals c into the factored form.

@art root-and-factor
So a root and a factor are the same information. A root you've found hands you a factor, and lets you divide the degree down by one. A factor you've found tells you a root, for free.

@chapter Where to look
@math heading="The rational root theorem" items="root p/q in lowest terms@lowest terms;;p divides a₀@the constant term;;q divides aₙ@the leading coefficient"
Now, where do you look? For a polynomial with integer coefficients, if p over q in lowest terms is a root, then p divides the constant term, and q divides the leading coefficient.

@art candidate-net
Read the direction carefully. It doesn't say every candidate is a root. Most aren't. It says any rational root must be on the list, so checking the list is a complete search.

@chapter A worked example
@math heading="2x³ − 3x² − 8x − 3" items="p: ±1, ±3@the divisors of minus three;;q: ±1, ±2@the divisors of two;;±1, ±3, ±1/2, ±3/2@eight numbers"
Take two x cubed minus three x squared minus eight x minus three. The divisors of minus three are plus or minus one and three. The divisors of two are plus or minus one and two. So the candidates are plus or minus one, three, one half and three halves. Eight numbers.

@art search-list
Then test them one at a time, ideally by synthetic division, so that a hit hands you the quotient straight away.

@math heading="Test" items="f(1) = 2 − 3 − 8 − 3 = −12@f of one;;f(−1) = −2 − 3 + 8 − 3 = 0@f of minus one;;(x + 1) is a factor@x plus one"
f of one is two minus three minus eight minus three, minus twelve. Not a root. f of minus one is minus two minus three plus eight minus three, which is zero. So x plus one is a factor.

@math heading="Divide it out" items="−1 │ 2  −3  −8  −3  →  2  −5  −3  0@synthetic division;;2x² − 5x − 3 = (2x + 1)(x − 3)@the AC method;;(x + 1)(2x + 1)(x − 3)@so the cubic"
Synthetic division by x plus one gives two, minus five, minus three, and a remainder of zero. The quotient two x squared minus five x minus three factors by the AC method, as two x plus one times x minus three. So the cubic is x plus one, times two x plus one, times x minus three.

@art degree-drops
The roots are minus one, minus a half, and three, all on the original list. And notice where the search stopped. Once the problem became a quadratic, the candidate list had done its job.

@chapter When the search is empty
@math heading="x³ − 2" items="candidates: 1, −1, 2, −2@the candidates;;f(1) = −1 · f(−1) = −3@f of one;;f(2) = 6 · f(−2) = −10@f of two"
Now x cubed minus two. The candidates are one, minus one, two and minus two. f of one is minus one, f of minus one is minus three, f of two is six, and f of minus two is minus ten. None is zero.

@art irrational-root
So x cubed minus two has no rational root and no rational linear factor. It does have a real root, the cube root of two. That root is irrational, and this theorem is exactly what proves it can't be written as a fraction.

@art three-roots
One more fact. A polynomial of degree n has at most n roots. Each root gives a factor, and the degrees of the factors can't add up to more than n.

@chapter Where people slip
@list heading="Common slips" items="Reading candidates as promised roots@The first|Getting p and q the wrong way round@The second|Testing on after the degree drops to two@The third"
The first slip is reading the candidates as promised roots. The second is getting p and q the wrong way round. Swap them here, and you'd miss the root minus a half entirely. The third is testing on after the degree drops to two. Use the pair or AC method instead.

@chapter Try it
@words text="2x³ − 3x² − 5x + 6" sub="f(1) = 0"
Your turn. Two x cubed minus three x squared minus five x plus six. Build the candidate list. The first hit is given: f of one is zero. Divide by x minus one, then factor the quotient with the AC method.

@math items="(x − 1)(2x + 3)(x − 2)@x minus one"
The complete answer is x minus one, times two x plus three, times x minus two. If your quotient came out as two x squared plus x minus six, check the sign under the minus three.

@end text="Test the whole list"
You can build the full candidate list for any polynomial and test it exactly, on Learn. That's learn dot get er done dot I O.
