---
format: long
lesson: combinatorics-and-counting/the-binomial-theorem
title: The binomial theorem: why expanding a power is counting choices
thumb: Expanding is choosing
---

@chapter Two facts, one fact
@title text="The Binomial Theorem" sub="Combinatorics and Counting" art=thumb
The numbers C of n, k count subsets. They're also the coefficients you get when you expand x plus y to a power. That isn't a coincidence, or even an analogy. It's the same fact.

@math heading="The binomial theorem" items="(x + y)ⁿ = Σ C(n, k) xⁿ⁻ᵏ yᵏ@x plus y to the n;;sum over k = 0, 1, …, n@for k from zero"
Here's the theorem. x plus y to the n equals the sum, for k from zero to n, of C of n, k, times x to the n minus k, times y to the k.

@chapter Expanding is choosing
@art factor-row
x plus y to the n is a product of n identical factors, each one x plus y. Expanding it, without collecting terms, means picking either x or y from every factor.

@art expansion-tree
That gives one term for each way of choosing, so two to the n terms in all. Every factor doubles the count.

@art choice-picks
A term equals x to the n minus k, times y to the k, exactly when y was chosen from k of the factors. And the number of ways to choose those k factors is C of n, k.

@art collect-terms
So when you collect equal terms, the coefficient on x to the n minus k, y to the k, is C of n, k. The coefficients count subsets, because expanding is choosing.

@math heading="(x + y)⁴" items="x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴@x to the fourth;;1, 4, 6, 4, 1 = row 4@The coefficients"
For example, x plus y to the fourth is x to the fourth, plus four x cubed y, plus six x squared y squared, plus four x y cubed, plus y to the fourth. The coefficients one, four, six, four, one are row four of Pascal's triangle.

@chapter Identities by substitution
@art substitution-dials
Because the theorem holds for any x and y, you can substitute numbers, and it turns into facts about a whole row of the triangle.

@math heading="Substitute" items="x = y = 1:  Σ C(n, k) = 2ⁿ@both to one;;x = 1, y = −1:  Σ (−1)ᵏ C(n, k) = 0, n ≥ 1@minus one;;x = 1, y = 2:  Σ 2ᵏ C(n, k) = 3ⁿ@y to two"
Set both to one, and the row sum is two to the n. Set x to one and y to minus one, and the alternating sum is zero, for n at least one. Set x to one and y to two, and the sum of two to the k times C of n, k is three to the n.

@chapter Extracting a coefficient
@math heading="x⁵y³ in (2x − 3y)⁸" items="general term: C(8, k)(2x)⁸⁻ᵏ(−3y)ᵏ@general term;;k = 3: C(8, 3) · 2⁵ · (−3)³@Take k equals three;;= 56 · 32 · (−27) = −48384@fifty six times"
What's the coefficient of x to the fifth y cubed, in two x minus three y, to the eighth? The general term is C of eight, k, times two x to the eight minus k, times minus three y to the k. Take k equals three. That's fifty six times thirty two times minus twenty seven: minus forty eight thousand three hundred and eighty four.

@words text="(2x)⁵ = 32x⁵ · (−y)³ = −y³" sub="constants and signs get the powers too"
Two places to be careful. The constants inside the brackets are raised to the powers too. And a minus sign survives an odd power. Both get dropped often enough to be worth naming.

@math heading="x²y⁶ in (x + 2y)⁸" items="want y⁶ ⟹ k = 6@so k equals six;;check: x⁸⁻⁶ = x²  ✓@check;;C(8, 6) · 2⁶ = 28 · 64 = 1792@twenty eight times"
One more: x squared y to the sixth, in x plus two y, to the eighth. We want y to the sixth, so k equals six. Then check that x gets the right power: eight minus six is two. The coefficient is twenty eight times sixty four, one thousand seven hundred and ninety two.

@chapter More than two terms
@art three-term
With more than two terms, the same idea gives the multinomial theorem. A coefficient counts the ways to assign the n factors to the terms, and it's n factorial over the factorials of the exponents.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the constants inside the brackets@The first|Losing a sign on an odd power@The second|Reading k as the first term's exponent@And the third"
The first slip is forgetting the constants inside the brackets. The second is losing a sign on an odd power, which is half of all extraction errors. And the third is confusing the index with the exponent. In this form, k is the exponent of the second term.

@chapter Try it
@words text="x⁴y⁵ in (2x − 3y)⁹" sub="then set x = y = 1: (2 − 3)⁹ = −1"
Your turn. Find the coefficient of x to the fourth, y to the fifth, in two x minus three y, to the ninth. Check the sign and both constants. Then set x and y to one in the same expansion, and confirm the total is two minus three, to the ninth, which is minus one.

@end text="See each expansion beside its row"
You can see each expansion printed next to its row of the triangle, on Learn. That's learn dot get er done dot I O.
