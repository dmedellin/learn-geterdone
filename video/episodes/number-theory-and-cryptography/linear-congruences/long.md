---
format: long
lesson: number-theory-and-cryptography/linear-congruences
title: Linear congruences: none, one, or exactly gcd many
thumb: Check the gcd first
---

@chapter The question
@title text="Linear Congruences" sub="Number Theory and Cryptography" art=thumb
Over the real numbers, a x equals b has exactly one solution whenever a isn't zero. Modulo m, the same kind of equation can have no solutions, one, or several. And one gcd tells you which, before you do any work.

@words text="ax ≡ b (mod m)" sub="g = gcd(a, m)"
Here's the theorem. Let g be the gcd of a and m. Then a x congruent to b, mod m, has a solution exactly when g divides b. And when it does, there are exactly g solutions modulo m.

@art three-outcomes
So there are really only two cases. Either g fails to divide b, and there's nothing to find. Or it does, and you get exactly g answers, spaced evenly around the modulus.

@chapter Why the gcd decides
@art multiples-only
A x congruent to b means a x minus m y equals b, for some integer y. By Bezout, the values of a x minus m y are exactly the multiples of g. So there's a solution exactly when b is one of those multiples.

@art divide-all
When it is, divide everything by g: a, b and the modulus. Now the new coefficient and the new modulus are coprime, so there's exactly one solution modulo m over g.

@art lift-up
Now lift it back. Each class modulo m over g splits into g classes modulo m. So one solution downstairs becomes g solutions upstairs. That's why the count is the gcd, not one, and not m.

@chapter Three examples
@math heading="6x ≡ 7 (mod 15)" items="gcd(6, 15) = 3@the gcd of six;;3 ∤ 7  ⟹  no solution@three doesn't divide"
First, six x congruent to seven, mod fifteen. The gcd of six and fifteen is three, and three doesn't divide seven. So there's no solution at all. Decided in one line.

@math heading="6x ≡ 9 (mod 15)" items="gcd = 3,  3 ∣ 9  ⟹  3 solutions@three divides nine;;2x ≡ 3 (mod 5)@divide through;;2⁻¹ ≡ 3  ⟹  x ≡ 9 ≡ 4 (mod 5)@the inverse of two;;x ≡ 4, 9, 14 (mod 15)@lifting back"
Change the seven to nine. Three divides nine, so there are three solutions. Divide through: two x is congruent to three, mod five. The inverse of two, mod five, is three, so x is nine, which is four, mod five. Lifting back to fifteen: four, nine and fourteen.

@art spaced-solutions
Check them. Six times four is twenty four, six times nine is fifty four, and six times fourteen is eighty four. All three are nine, mod fifteen. And notice they're spaced five apart, which is fifteen over three.

@math heading="7x ≡ 3 (mod 26)" items="gcd(7, 26) = 1  ⟹  one solution@the gcd is one;;7 · 15 = 105 = 4 · 26 + 1  ⟹  7⁻¹ ≡ 15@seven times fifteen;;x ≡ 15 · 3 = 45 ≡ 19 (mod 26)@so x"
Third, seven x congruent to three, mod twenty six. Here the gcd is one, so exactly one solution. Seven times fifteen is a hundred and five, one more than four times twenty six, so the inverse of seven is fifteen. So x is fifteen times three, forty five, which is nineteen.

@chapter A worked example
@math heading="14x ≡ 30 (mod 100)" items="g = gcd(14, 100) = 2,  2 ∣ 30@g is two;;7x ≡ 15 (mod 50)@divide by two;;7 · 43 = 301 ≡ 1  ⟹  7⁻¹ ≡ 43@seven times forty three;;x ≡ 43 · 15 = 645 ≡ 45 (mod 50)@so x is;;x ≡ 45, 95 (mod 100)@lift to"
Now fourteen x congruent to thirty, mod a hundred. g is two, and two divides thirty, so two solutions. Divide by two: seven x is fifteen, mod fifty. Seven times forty three is three hundred and one, which is one, so the inverse of seven is forty three. So x is forty three times fifteen, six hundred and forty five, which is forty five, mod fifty. Lift to a hundred: forty five and ninety five.

@words text="14 · 45 = 630    14 · 95 = 1330" sub="both ≡ 30 (mod 100)"
Both check: six hundred and thirty and thirteen hundred and thirty each leave thirty. Reporting only forty five would be half an answer.

@chapter Why it differs from ordinary equations
@art field-vs-not
The real numbers are a field, so every nonzero a can be divided out. The integers mod m are a field only when m is prime. Modulo a composite, some coefficients can't be divided out, and the gcd measures that failure exactly.

@chapter Where people slip
@list heading="Common slips" items="Reporting one solution when there are g@The first|Solving before checking the gcd@The second|Dividing only the coefficient by g@And the third"
The first slip is reporting one solution when there are g. Stopping at the reduced congruence gives a correct statement about the wrong modulus. The second is trying to solve before checking the gcd. And the third is dividing only the coefficient by g. Divide all three.

@chapter Try it
@words text="15x ≡ 25 (mod 35)" sub="state the number of solutions first"
Your turn. Solve fifteen x congruent to twenty five, mod thirty five. But before you find any solution, say how many there are, and how far apart they'll be.

@end text="Solve, or prove unsolvable"
You can solve any linear congruence, or watch the gcd prove there's no solution, on Learn. That's learn dot get er done dot I O.
