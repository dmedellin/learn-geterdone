---
format: long
lesson: number-theory-and-cryptography/modular-exponentiation
title: Modular exponentiation: square and multiply
thumb: Huge powers, small numbers
---

@chapter The problem
@title text="Modular Exponentiation" sub="Number Theory and Cryptography" art=thumb
RSA encrypts by raising a number to a power with hundreds of digits. Written out, that power wouldn't fit in the universe. Yet your computer does it in an instant. Here's how.

@art giant-number
The goal is a to the b, mod m, without ever forming a to the b. The naive way multiplies by a, b times over. For a two thousand bit exponent, that's hopeless. We need two ideas, and both are essential.

@chapter Square, don't multiply
@art doubling-ladder
The first idea is squaring. a to the two k is a to the k, squared. So each squaring doubles the exponent you've reached. Square seven times, and you've gone from a to a to the hundred and twenty eight.

@art binary-switches
For exponents that aren't powers of two, read b in binary. Each set bit says which power of a to multiply in. Since b is a sum of powers of two, the product of those selected powers is a to the b.

@list heading="MODPOW(a, b, m)" items="result = 1,  base = a mod m@start with|if b is odd: result = result · base mod m@if b is odd|base = base · base mod m@square the base|b = b div 2@halve b"
Here's the loop. Start with result one and base equal to a mod m. While b is above zero: if b is odd, multiply the result by the base. Then square the base, and halve b, rounding down. Reduce mod m after every multiplication.

@chapter Seven to the 128, mod 13
@math heading="7¹²⁸ mod 13" items="7² = 49 ≡ 10@seven squared;;10² = 100 ≡ 9@ten squared;;9² = 81 ≡ 3@nine squared;;3² = 9,  9² ≡ 3,  3² = 9,  9² ≡ 3@then nine;;7¹²⁸ ≡ 3  (mod 13)@seven squarings"
Here's a pure power of two. Seven squared is forty nine, which is ten, mod thirteen. Ten squared is a hundred, which is nine. Nine squared is eighty one, which is three. Then nine, three, nine, three. Since a hundred and twenty eight is two to the seventh, seven squarings give the answer: three.

@art bounded-box
And look at the sizes. No number above a hundred and forty four ever appeared. That's the second idea: reduce at every step. Each intermediate is a product of two numbers below m, so it's below m squared.

@chapter Three to the 200, mod 50
@math heading="Square, mod 50" items="3⁴ ≡ 31,  3⁸ ≡ 11@three to the fourth;;3¹⁶ ≡ 21,  3³² ≡ 41@three to the sixteenth;;3⁶⁴ ≡ 31,  3¹²⁸ ≡ 11@three to the sixty fourth"
Now a mixed exponent. Square repeatedly, mod fifty. Three to the fourth is thirty one, and three to the eighth is eleven. Three to the sixteenth is twenty one, and to the thirty second, forty one. Three to the sixty fourth is thirty one, and to the hundred and twenty eighth, eleven.

@math heading="200 = 11001000₂" items="200 = 128 + 64 + 8@two hundred is;;3²⁰⁰ ≡ 11 · 31 · 11@so multiply;;341 ≡ 41,  41 · 11 = 451 ≡ 1@eleven times thirty one"
Two hundred is a hundred and twenty eight plus sixty four plus eight, so multiply eleven, thirty one and eleven. Eleven times thirty one is three forty one, which is forty one. Times eleven is four fifty one, which is one. So the answer is one.

@art square-chain
That's seven squarings and three multiplications, against a hundred and ninety nine the naive way.

@chapter What it costs
@math heading="Naive vs square and multiply" items="b = 128:  128  vs  8 squarings@a hundred and twenty eight;;b = 10⁶:  a million  vs  about 20@a million;;b = 2¹⁰²⁴:  impossible  vs  about 1024@two to the"
The loop runs once per bit of b, so the cost is at most about two times log base two of b multiplications. For an exponent of a hundred and twenty eight, that's eight squarings instead of a hundred and twenty eight multiplications. For a million, about twenty. For two to the thousand and twenty four, about a thousand and twenty four squarings, where the naive way is impossible.

@words text="2048-bit modulus → 4096-bit intermediates" sub="a^b itself: about 2¹⁰²⁴ bits"
And thanks to reduction, a two thousand and forty eight bit modulus means intermediates of four thousand and ninety six bits. Entirely routine. Without reduction, a to the b would have about two to the thousand and twenty four bits.

@chapter Where it's used
@art one-way
This is inside RSA, where encryption and decryption are each one modular exponentiation. It's inside Diffie Hellman key exchange, and inside primality tests like Fermat and Miller Rabin. And notice the asymmetry. Computing a to the b, mod m, is fast. Recovering b from the answer, the discrete logarithm, is believed hard. A lot of cryptography lives in that gap.

@chapter Where people slip
@list heading="Common slips" items="Reducing the exponent modulo m@The first|Computing aᵇ before reducing@The second|Multiplying in the wrong powers@And the third"
The first slip is reducing the exponent modulo m. Exponents reduce modulo phi of m, and only for a base coprime to m. The second is computing a to the b before reducing. Reducing at every step is the whole point. And the third is multiplying in the wrong powers. Write b in binary first, and it's mechanical.

@chapter Try it
@words text="5¹¹⁷ mod 19" sub="117 = 1110101₂"
Your turn. Compute five to the hundred and seventeen, mod nineteen, by square and multiply. Write a hundred and seventeen in binary first. It has five set bits. No intermediate should ever exceed three hundred and sixty one.

@end text="Trace every squaring"
You can trace every squaring and every multiplication, bit by bit, on Learn. That's learn dot get er done dot I O.
