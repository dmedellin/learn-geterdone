---
format: long
lesson: number-theory-and-cryptography/greatest-common-divisor
title: Greatest common divisor, and why you don't find it by factoring
thumb: Largest shared divisor
---

@chapter The question
@title text="Greatest Common Divisor" sub="Number Theory and Cryptography" art=thumb
What's the largest number that divides both of two numbers? There's a formula for it that's completely correct, and almost useless in practice. Let's see why.

@art common-measure
For integers a and b, not both zero, the greatest common divisor is the largest positive integer dividing both. And the gcd of a and zero is the size of a. That last fact matters more than it looks.

@art lcm-meeting
Its partner is the least common multiple. For nonzero a and b, it's the smallest positive integer that both divide. Picture two hoppers with different stride lengths. The lcm is the first place they land together.

@chapter From the factorisations
@math heading="48 and 180" items="48 = 2⁴ · 3@forty eight is;;180 = 2² · 3² · 5@one hundred and eighty is;;gcd = 2² · 3 = 12@the gcd takes;;lcm = 2⁴ · 3² · 5 = 720@the lcm takes"
If you know the prime factorisations, it's easy. Forty eight is two to the fourth times three. One hundred and eighty is two squared, times three squared, times five. The gcd takes the smaller exponent of each prime: two squared times three, twelve. The lcm takes the larger: two to the fourth, times three squared, times five, which is seven hundred and twenty.

@art min-max-bars
Why the smaller exponent? A common divisor can use each prime only as often as both numbers allow, and taking exactly that many gives the largest one. The lcm is the mirror image, with the larger exponents.

@chapter The product identity
@words text="gcd(a, b) · lcm(a, b) = |a · b|" sub="12 · 720 = 8640 = 48 · 180"
Put them together and you get an exact identity. The gcd times the lcm equals the product of the two numbers. Check it: twelve times seven hundred and twenty is eight thousand six hundred and forty, and so is forty eight times a hundred and eighty.

@math heading="At each prime" items="min(aᵢ, bᵢ) + max(aᵢ, bᵢ) = aᵢ + bᵢ@the smaller exponent plus"
The proof is one line. At each prime, the smaller exponent plus the larger one is just the two exponents added together. Multiply over all the primes, and you're done.

@words text="lcm(a, b) = |ab| / gcd(a, b)" sub="gcd 4, lcm 60  ⟹  ab = 240"
That identity is the practical way to get an lcm. Find the gcd, then divide. And it pins down the product: if the gcd is four and the lcm is sixty, a times b is two hundred and forty. Four and sixty fit, and so do twelve and twenty.

@chapter Why not factor?
@art easy-hard
Here's the catch with the formula. It needs both factorisations, and factoring is hard. For two numbers a hundred digits long, no known method factors them in reasonable time. Yet Euclid's algorithm finds their gcd in a few hundred divisions.

@math heading="84 and 264, by Euclid" items="264 = 3 · 84 + 12@two hundred and sixty four;;84 = 7 · 12 + 0  ⟹  gcd = 12@eighty four is;;lcm = 84 · 264 / 12 = 1848@so the lcm"
Here's a preview. Two hundred and sixty four is three times eighty four, plus twelve. Eighty four is seven times twelve, plus nothing. So the gcd is twelve, in two divisions, without factoring anything. So the lcm is eighty four times two hundred and sixty four, over twelve, which is eighteen hundred and forty eight.

@chapter Coprime
@art coprime-gears
Two numbers are coprime when their gcd is one. They share no prime factor. Neither needs to be prime. Eight and nine are both composite, and they're coprime. It's a property of the pair.

@math heading="Neighbours are coprime" items="d ∣ n  and  d ∣ (n + 1)@divides n and;;⟹  d ∣ (n + 1) − n = 1@so it divides;;gcd(n, n + 1) = 1@consecutive"
Here's a neat one. Any number that divides n and n plus one also divides their difference, so it divides one. So consecutive integers are always coprime.

@art neighbours
Keep that one in mind. Neighbours never share a factor, and that's a fact the Chinese remainder theorem will lean on later in the course.

@chapter Where people slip
@list heading="Common slips" items="Computing gcds by factoring@The first|Extending the identity to three numbers@The second|Forgetting the base case gcd(a, 0)@And the third"
The first slip is computing gcds by factoring. Correct, and impractical. The second is extending the product identity to three numbers. The gcd of two, four and eight is two, the lcm is eight, and their product is sixteen, not sixty four. And the third is forgetting that the gcd of a and zero is a. That's the base case of Euclid's algorithm.

@chapter Try it
@words text="gcd(1071, 462)  and  lcm(1071, 462)" sub="without factoring either number"
Your turn. Find the gcd and the lcm of one thousand and seventy one and four hundred and sixty two, without factoring either one. The gcd takes three divisions, and the lcm follows from the identity.

@end text="Find a gcd without factoring"
You can run the divisions yourself and watch the gcd appear without any factoring, on Learn. That's learn dot get er done dot I O.
