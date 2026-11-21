---
format: long
lesson: number-theory-and-cryptography/the-euclidean-algorithm
title: The Euclidean algorithm: a gcd in a handful of divisions
thumb: Divide, keep the remainder, repeat
---

@chapter One identity
@title text="The Euclidean Algorithm" sub="Number Theory and Cryptography" art=thumb
How do you find the greatest common divisor of two numbers a thousand digits long, in milliseconds? With one of the oldest algorithms still in daily use, built on a single identity.

@words text="gcd(a, b) = gcd(b, a mod b)" sub="for b > 0"
Here it is. For b bigger than zero, the gcd of a and b equals the gcd of b and a mod b. Replace the pair by the smaller number and the remainder, and the answer doesn't change.

@art same-divisors
Why is that true? Write a as q b plus r. Anything that divides a and b also divides a minus q b, which is r. And anything that divides b and r divides q b plus r, which is a. So the two pairs have exactly the same common divisors. Same set, same greatest member.

@chapter The algorithm
@list heading="GCD(a, b)" items="while b ≠ 0@while b is not zero|(a, b) = (b, a mod b)@replace the pair|return a@return a"
So the whole algorithm is a loop. While b is not zero, replace the pair a, b with b, a mod b. When b hits zero, return a.

@art pair-shrinks
It's correct because the gcd never changes from one step to the next. That's a loop invariant. And it stops because b strictly shrinks and can't go below zero. At the end, the gcd of a and zero is just a.

@chapter A worked example
@math heading="gcd(1071, 462)" items="1071 = 2 · 462 + 147@one thousand and seventy one;;462 = 3 · 147 + 21@four hundred and sixty two;;147 = 7 · 21 + 0@a hundred and forty seven;;gcd = 21@so the gcd"
Let's run it. One thousand and seventy one is two times four hundred and sixty two, plus a hundred and forty seven. Four hundred and sixty two is three times a hundred and forty seven, plus twenty one. A hundred and forty seven is seven times twenty one, plus nothing. So the gcd is twenty one.

@words text="1071 = 21 · 51    462 = 21 · 22" sub="gcd(51, 22) = 1"
Check it. One thousand and seventy one is twenty one times fifty one, and four hundred and sixty two is twenty one times twenty two. Fifty one and twenty two share no factor, so twenty one really is the greatest. Three divisions, and nothing was factored.

@art last-nonzero
Notice where the answer sits. The gcd is the last remainder that isn't zero. Returning the zero is the classic off by one.

@chapter How fast
@art halving-steps
Here's the speed guarantee. In two steps, the first number at least halves. If b is at most half of a, the remainder is already below half. If b is more than half, the remainder is a minus b, which is below half. So the number of steps is logarithmic.

@words text="Lamé: steps ≤ 5 × digits of the smaller input" sub="worst case: consecutive Fibonacci numbers"
Lame's theorem sharpens that. The number of division steps is at most five times the number of decimal digits in the smaller input. And the worst case happens exactly for consecutive Fibonacci numbers.

@math heading="gcd(89, 55)" items="89 = 1 · 55 + 34@eighty nine;;55 = 1 · 34 + 21@fifty five;;34 = 1 · 21 + 13@and so on;;⋮;;2 = 2 · 1 + 0   gcd = 1,  9 steps@nine divisions"
Try eighty nine and fifty five. Eighty nine is one times fifty five, plus thirty four. Fifty five is one times thirty four, plus twenty one. And so on down the Fibonacci numbers, every quotient one, the slowest possible progress. It takes nine divisions to reach a gcd of one.

@art fibonacci-squares
So size isn't what decides the step count. One thousand and seventy one and four hundred and sixty two took three steps. Eighty nine and fifty five took nine. The pattern of quotients decides, not the size of the numbers.

@art scaled-copy
Here's a nice way to see it. Scale both inputs by ten, to eight hundred and ninety and five hundred and fifty. You get the same nine rows, because scaling both numbers leaves every quotient unchanged.

@chapter In practice
@words text="RSA · fractions · computer algebra" sub="thousand-digit gcds in milliseconds"
That's why Euclid's algorithm is everywhere. It computes gcds of thousand digit numbers in milliseconds, inside every implementation of RSA, in reducing fractions, and in computer algebra. For the general case, nobody has beaten it asymptotically.

@chapter Where people slip
@list heading="Common slips" items="Stopping at the wrong point@The first|Requiring a > b to start@The second|Assuming big numbers mean many steps@And the third"
The first slip is stopping at the wrong point. The answer is the last nonzero remainder. The second is thinking a must be bigger than b to start. If it isn't, the first division just swaps them. And the third is assuming bigger numbers mean more steps.

@chapter Try it
@words text="gcd(144, 89)" sub="144 = F₁₂,  89 = F₁₁"
Your turn. Run the algorithm on a hundred and forty four and eighty nine. They're consecutive Fibonacci numbers, so before you start, predict how many divisions it will take. Then count them.

@end text="Watch every division"
You can watch every division, and try the Fibonacci worst case, on Learn. That's learn dot get er done dot I O.
