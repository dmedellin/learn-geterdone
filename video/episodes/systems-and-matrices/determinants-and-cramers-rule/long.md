---
format: long
lesson: systems-and-matrices/determinants-and-cramers-rule
title: Determinants and Cramer's rule: one number that decides uniqueness
thumb: Is D zero?
---

@chapter The question
@title text="Determinants and Cramer's Rule" sub="Systems and Matrices" art=thumb
Row reduction tells you how many solutions a system has, but only at the end. The determinant answers that in advance, from the coefficients alone, in a single number.

@math heading="2 × 2 determinant" items="det [ a  b ; c  d ]  =  ad − bc@a d minus b c"
For a two by two matrix with rows a, b and c, d, the determinant is a d minus b c: the product down the main diagonal, minus the product up the other one.

@art cross-diagonals
It's written det A, or with vertical bars around the entries. Brackets hold an array, and bars produce a number. Only square matrices have a determinant.

@math heading="Two examples" items="| 3  5 ; 1  4 |  =  (3)(4) − (5)(1)  =  7@three times four;;| 2  6 ; 1  3 |  =  6 − 6  =  0@six minus six"
Rows three, five and one, four: three times four, minus five times one, is seven. Rows two, six and one, three: six minus six, which is zero.

@art proportional-rows
That second matrix has a second row that's half the first. A determinant of zero is what that always produces.

@chapter Three by three
@math heading="Expand along the first row" items="| 2  1  3 ; 0  4  −1 ; 5  2  0 |@two, one, three;;= 2·| 4  −1 ; 2  0 |  −  1·| 0  −1 ; 5  0 |  +  3·| 0  4 ; 5  2 |@cross out"
Take the rows two, one, three; zero, four, minus one; and five, two, zero. Take each entry of the first row, cross out its row and column, and multiply the entry by the determinant of what's left. Then combine with alternating signs: plus, minus, plus.

@art cofactor-cross
For the first entry, two, crossing out leaves four, minus one, two, zero. For the one, it leaves zero, minus one, five, zero. And for the three, zero, four, five, two.

@math heading="Work it out" items="= 2(0 − (−2))  −  1(0 − (−5))  +  3(0 − 20)@two times zero;;= 2(2) − 1(5) + 3(−20)@two times two;;= 4 − 5 − 60  =  −61@minus sixty one"
That's two times zero minus minus two, minus one times zero minus minus five, plus three times zero minus twenty. So two times two, minus five, plus three times minus twenty. Four minus five minus sixty is minus sixty one.

@art sign-pattern
Those signs aren't optional. Add the middle term instead, and you get minus fifty one, a wrong answer with no visible symptom. And a row with a zero in it is the smart one to expand along, because that term vanishes.

@chapter What D decides
@words text="D ≠ 0  ⟺  exactly one solution" sub="n equations in n unknowns"
Here's what the number is for. A system of n equations in n unknowns has exactly one solution if and only if D, the determinant of its coefficient matrix, isn't zero. When D is zero, there's either no solution or infinitely many.

@math heading="Same D, two outcomes" items="x + y = 1,    2x + 2y = 5:    D = 0,  no solution@equals five;;x + y = 1,    2x + 2y = 2:    D = 0,  infinitely many@equals two"
x plus y equals one, with two x plus two y equals five, has D equal to zero and no solution. x plus y equals one, with two x plus two y equals two, also has D zero, but it's one equation written twice, with infinitely many solutions.

@art fork-zero
One determinant, two different outcomes. D equals zero rules out uniqueness and says nothing else. To tell which case you're holding, go back to elimination.

@chapter Cramer's rule
@math heading="Cramer's rule" items="x = Dx / D,      y = Dy / D      (D ≠ 0)@x equals D x over D"
If D isn't zero, Cramer's rule writes the solution as a ratio of determinants. x equals D x over D, and y equals D y over D.

@art column-replace
D x is D with the x column replaced by the constants. D y is D with the y column replaced. For three unknowns, you'd need four three by three determinants.

@math heading="2x + 3y = 7,    5x − y = 3" items="D = (2)(−1) − (3)(5) = −17@minus seventeen;;Dx = | 7  3 ; 3  −1 | = −7 − 9 = −16@minus sixteen;;Dy = | 2  7 ; 5  3 | = 6 − 35 = −29@minus twenty nine;;x = 16/17,     y = 29/17@sixteen seventeenths"
Take two x plus three y equals seven, and five x minus y equals three. Minus y contributes minus one. D is minus two minus fifteen, minus seventeen. D x is minus seven minus nine, minus sixteen. D y is six minus thirty five, minus twenty nine. So x is sixteen seventeenths, and y is twenty nine seventeenths.

@math heading="Check exactly" items="2(16/17) + 3(29/17) = 119/17 = 7 ✓@one hundred nineteen;;5(16/17) − 29/17 = 51/17 = 3 ✓@fifty one"
Check: thirty two plus eighty seven is one hundred nineteen seventeenths, which is seven. And eighty minus twenty nine is fifty one seventeenths, which is three. Exact fractions check exactly. Decimals don't.

@chapter Where people slip
@list heading="Common slips" items="Reading a row before standard form@The first|Adding all three terms@The second|Calling D = 0 infinitely many@the third"
The first slip is reading coefficients before standard form: three y plus two x equals seven gives the row two, three, not three, two. The second is adding all three terms of a three by three expansion. And the third is announcing infinitely many solutions because D is zero. That conclusion needs the reduction.

@chapter Try it
@words text="3x + 2y = 4      x − y = 5" sub="is Cramer's rule legal here?"
Your turn. For three x plus two y equals four, and x minus y equals five, write the coefficient determinant and decide whether Cramer's rule is legal here. Then build D x and D y, keep the quotients exact, and check the pair in both equations.

@end text="Compute D first"
You can compute determinants and try Cramer's rule on your own systems, on Learn. That's learn dot get er done dot I O.
