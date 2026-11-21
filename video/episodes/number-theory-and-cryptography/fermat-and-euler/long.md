---
format: long
lesson: number-theory-and-cryptography/fermat-and-euler
title: Fermat's little theorem and Euler's theorem: shrinking huge exponents
thumb: Exponents reduce mod φ(m)
---

@chapter A huge exponent
@title text="Fermat's Little Theorem and Euler's Theorem" sub="Number Theory and Cryptography" art=thumb
What are the last two digits of three to the power one million two hundred and thirty four thousand five hundred and sixty seven? That number has over half a million digits. By the end of this video you'll find them in a few lines.

@words text="a^φ(m) ≡ 1 (mod m)" sub="when gcd(a, m) = 1"
The tool is Euler's theorem. When a and m are coprime, a to the phi of m is congruent to one, mod m. To use it, we first need phi.

@chapter Euler's totient
@art coprime-count
Phi of m is the number of integers from one to m that are coprime to m. Those are exactly the invertible elements, the units, mod m.

@math heading="Computing φ" items="φ(7) = 6@phi of seven;;φ(9) = 9 − 3 = 6@phi of nine;;φ(12) = 4:  1, 5, 7, 11@phi of twelve;;φ(35) = φ(5)φ(7) = 4 · 6 = 24@phi of thirty five;;φ(3120) = 8 · 2 · 4 · 12 = 768@three thousand one hundred and twenty"
For a prime p, phi of p is p minus one, so phi of seven is six. For a prime power, subtract the multiples of the prime: phi of nine is nine minus three, six. Phi of twelve is four: one, five, seven and eleven. And phi is multiplicative on coprime factors, so phi of thirty five is four times six, twenty four. Phi of three thousand one hundred and twenty is seven hundred and sixty eight.

@chapter Why Euler's theorem holds
@art shuffle-units
Here's the proof. List the units mod m. Multiply each one by a. You get units again, and they're all different, because a is invertible. So it's the same set, just shuffled.

@math heading="Same set, same product" items="a^φ · (u₁⋯u_φ) ≡ u₁⋯u_φ  (mod m)@so the products;;a^φ(m) ≡ 1  (mod m)@cancel it"
So the products agree. a to the phi, times the product of the units, is congruent to the product of the units. That product is itself a unit, so you can cancel it, and a to the phi of m is one.

@words text="a^(p−1) ≡ 1 (mod p)" sub="Fermat: p prime, p ∤ a  ·  equivalently aᵖ ≡ a"
Fermat's little theorem is the prime case. Phi of p is p minus one, so if p doesn't divide a, a to the p minus one is one, mod p. Equivalently, a to the p is congruent to a, for every a.

@chapter Reducing exponents
@words text="aᵏ ≡ a^(k mod φ(m))  (mod m)" sub="when gcd(a, m) = 1"
Here's the practical rule. When a is coprime to m, you can reduce the exponent modulo phi of m.

@math heading="7¹⁰⁰⁰ mod 13" items="φ(13) = 12@phi of thirteen;;1000 = 83 · 12 + 4@a thousand is;;7¹⁰⁰⁰ ≡ 7⁴@so seven to the;;7² = 49 ≡ 10,  7⁴ ≡ 100 ≡ 9@seven squared"
Take seven to the thousand, mod thirteen. Phi of thirteen is twelve. A thousand is eighty three twelves plus four, so seven to the thousand is seven to the fourth. Seven squared is forty nine, which is ten, and ten squared is a hundred, which is nine. The answer is nine, from two multiplications.

@art exponent-wheel
The powers of seven come back to one after twelve steps, so the exponent just goes round and round a cycle of twelve.

@chapter The opening question
@math heading="3^1234567 mod 100" items="gcd(3, 100) = 1@three and a hundred;;φ(100) = 2 · 20 = 40@phi of a hundred;;1234567 mod 40 = 7@seven;;3⁷ = 2187 ≡ 87@three to the seventh"
Now the opening question. Three and a hundred are coprime, so the theorem applies. Phi of a hundred is two times twenty, forty. The exponent, divided by forty, leaves seven. So we need three to the seventh, which is two thousand one hundred and eighty seven. The last two digits are eighty seven.

@art tower-shrinks
Two facts made that possible. Euler shrank the exponent from over a million down to seven, and reducing mod a hundred kept every number small. Either one alone wouldn't have been enough.

@chapter Testing for primes
@art impostor
Fermat's theorem gives a primality test. If a to the n minus one isn't one mod n, for some a coprime to n, then n is definitely composite. But the converse fails. Carmichael numbers like five hundred and sixty one pass for every coprime base, and five sixty one is three times eleven times seventeen.

@art many-tries
That's why the Miller Rabin refinement is used in practice. And it's how RSA keys get made. Random thousand and twenty four bit numbers are tested until one passes, and about one in seven hundred does. Nothing gets factored.

@chapter Where people slip
@list heading="Common slips" items="Reducing the exponent modulo m@The first|Using a non-coprime base@The second|Treating a pass as proof of primality@And the third"
The first slip is reducing the exponent modulo m. The second is using a base that isn't coprime: two to the phi of four is zero mod four, not one. And the third is treating a pass of Fermat's test as proof. It proves compositeness when it fails, and nothing when it passes.

@math heading="2¹⁰ mod 7" items="✗  10 mod 7 = 3:  2³ = 8 ≡ 1@exponent mod seven;;✓  10 mod 6 = 4:  2⁴ = 16 ≡ 2@reduce mod six;;1024 = 146 · 7 + 2@and a thousand"
Here's the first slip in action. Take two to the ten, mod seven. Reduce the exponent mod seven and you get two cubed, which is one. Reduce mod six, which is phi of seven, and you get two to the fourth, which is two. And a thousand and twenty four is a hundred and forty six sevens plus two, so two is right.

@chapter Try it
@words text="2^1000000 mod 77" sub="φ(77) = 60"
Your turn. Find two to the million, mod seventy seven. Phi of seventy seven is sixty, so reduce the exponent first, then finish with square and multiply.

@end text="Watch the powers return to 1"
You can watch the powers of any number cycle back to one, on Learn. That's learn dot get er done dot I O.
