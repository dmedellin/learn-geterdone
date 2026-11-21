---
format: long
lesson: number-theory-and-cryptography/chinese-remainder-theorem
title: The Chinese remainder theorem, built term by term
thumb: Many remainders, one answer
---

@chapter An old riddle
@title text="The Chinese Remainder Theorem" sub="Number Theory and Cryptography" art=thumb
Here's a puzzle from a Chinese text of the third century. Its solution is a theorem that still makes every RSA implementation faster today.

@quote text="There are things whose number is unknown. Divided by 3 the remainder is 2; by 5 the remainder is 3; by 7 the remainder is 2." cite="Sun Tzu's problem, third century"
There are things whose number is unknown. Divided by three the remainder is two. By five the remainder is three. By seven the remainder is two. How many things are there?

@art riddle-pile
You could try numbers one at a time until one fits. But there's a way to build the answer directly, for any remainders you like.

@chapter The theorem
@words text="x ≡ aᵢ (mod mᵢ),  mᵢ pairwise coprime" sub="exactly one solution modulo M = m₁m₂⋯mₖ"
The Chinese remainder theorem says this. If the moduli are pairwise coprime, so no two share a factor, then for any choice of remainders there's exactly one solution modulo their product.

@art separate-dials
Think of each modulus as its own dial. You can set every dial independently, and there's exactly one number, up to the product, that shows all those settings at once.

@chapter The construction
@math heading="Build the solution" items="M = m₁m₂⋯mₖ,  Mᵢ = M / mᵢ@let M be;;yᵢ = Mᵢ⁻¹ mod mᵢ@since the moduli;;x = Σ aᵢ Mᵢ yᵢ@then x is"
The proof builds the answer. Let M be the product of the moduli, and M i be M divided by the i th modulus. Since the moduli are pairwise coprime, M i has an inverse, y i, modulo the i th modulus. Then x is the sum of a i times M i times y i.

@art invisible-terms
Here's why it works. Every M i is divisible by every modulus except its own. So each term vanishes modulo all the other moduli, and modulo its own it contributes exactly a i. The terms don't interfere.

@chapter Solving the riddle
@math heading="M = 3 · 5 · 7 = 105" items="M₁ = 35 ≡ 2 (mod 3),  y₁ = 2  →  2 · 35 · 2 = 140@thirty five;;M₂ = 21 ≡ 1 (mod 5),  y₂ = 1  →  3 · 21 · 1 = 63@twenty one;;M₃ = 15 ≡ 1 (mod 7),  y₃ = 1  →  2 · 15 · 1 = 30@fifteen;;x = 140 + 63 + 30 = 233 ≡ 23 (mod 105)@add them"
Back to the riddle. M is three times five times seven, a hundred and five. M one is thirty five, which is two mod three, and its inverse is two, giving a term of a hundred and forty. M two is twenty one, which is one mod five, giving sixty three. M three is fifteen, one mod seven, giving thirty. Add them: two hundred and thirty three, which is twenty three, mod a hundred and five.

@words text="23 = 7·3 + 2 = 4·5 + 3 = 3·7 + 2" sub="23, 128, 233, −82: the same answer mod 105"
Check it. Twenty three leaves two on division by three, three on division by five, and two on division by seven. And since the answer is unique mod a hundred and five, twenty three, a hundred and twenty eight, two hundred and thirty three and even minus eighty two are all the same answer.

@art unique-meeting
Why unique? If two numbers both solve the system, every modulus divides their difference. Because the moduli are pairwise coprime, their product divides it too. So the two are congruent mod M.

@chapter Coprimality is not optional
@math heading="Moduli 4 and 6" items="x ≡ 1 (mod 4),  x ≡ 2 (mod 6):  no solution@x congruent to one;;x ≡ 1 (mod 4),  x ≡ 3 (mod 6):  x ≡ 9 (mod 12)@change the second"
Drop coprimality and things go wrong. x congruent to one mod four, and two mod six, has no solution. The first makes x odd and the second makes it even. Change the second remainder to three, and there are solutions, but they're x congruent to nine mod twelve, not mod twenty four.

@art clash
So for moduli that share a factor, the answer lives modulo the lcm, and the remainders have to agree modulo every pairwise gcd. Four and six share two, and one and two disagree mod two.

@chapter Why RSA uses it
@art split-work
RSA decryption works modulo n, which is p times q. By this theorem, that's the same as working mod p and mod q separately, then recombining. The pieces use numbers half the size, and multiplication cost grows like the square of the size. With Fermat's theorem trimming the exponents too, the overall gain is roughly a factor of four.

@chapter Where people slip
@list heading="Common slips" items="Not checking coprimality@The first|Inverting Mᵢ modulo M@The second|Forgetting to reduce the final sum@And the third"
The first slip is applying the theorem without checking coprimality. The second is inverting M i modulo the wrong thing. It's the inverse modulo its own modulus, not modulo M. Reduce M i first and the inversion is small. And the third is forgetting to reduce the final sum into the range from zero to M.

@chapter Try it
@words text="x ≡ 1 (mod 5),  x ≡ 2 (mod 7),  x ≡ 3 (mod 9)" sub="three inversions, not 315 trials"
Your turn. Solve x congruent to one mod five, two mod seven, and three mod nine, by the construction. Searching could take up to three hundred and fifteen trials. The construction takes three inversions.

@end text="Combine two moduli"
You can combine congruences, coprime or not, and watch each term vanish for the other modulus, on Learn. That's learn dot get er done dot I O.
