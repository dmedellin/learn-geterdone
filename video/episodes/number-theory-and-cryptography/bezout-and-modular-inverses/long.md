---
format: long
lesson: number-theory-and-cryptography/bezout-and-modular-inverses
title: Bézout's identity: how modular inverses are found
thumb: Run Euclid backwards
---

@chapter The gcd as a combination
@title text="Bézout's Identity and Modular Inverses" sub="Number Theory and Cryptography" art=thumb
You can build the greatest common divisor out of the two numbers themselves. That one fact is where every modular inverse in cryptography comes from, including RSA's private key.

@words text="gcd(a, b) = ax + by" sub="for some integers x, y"
Here's Bezout's identity. For integers a and b, not both zero, there are integers x and y with a x plus b y equal to the gcd of a and b. And the gcd is the smallest positive number you can make that way.

@art combine-rods
Picture rods of two lengths. Lay some forward, some backward, and the smallest positive length you can measure out is exactly the gcd.

@art smallest-combination
The proof uses well-ordering. Take the smallest positive combination, call it d. Divide a by d. The remainder is another combination, smaller than d, so it must be zero. So d divides a, and likewise b. And any common divisor of a and b divides d. So d is the gcd.

@chapter Run Euclid backwards
@math heading="gcd(1071, 462)" items="1071 = 2 · 462 + 147  ⟹  147 = 1071 − 2 · 462@one thousand and seventy one;;462 = 3 · 147 + 21  ⟹  21 = 462 − 3 · 147@four hundred and sixty two"
The proof says x and y exist. The extended Euclidean algorithm finds them. Run Euclid forward, and rearrange each line to give the remainder. One thousand and seventy one is two times four hundred and sixty two, plus a hundred and forty seven. Four hundred and sixty two is three times a hundred and forty seven, plus twenty one.

@math heading="Back-substitute" items="21 = 462 − 3 · 147@start from;;= 462 − 3(1071 − 2 · 462)@replace the hundred;;= 7 · 462 − 3 · 1071@collect"
Now go upward. Start from twenty one as four hundred and sixty two minus three times a hundred and forty seven. Replace the hundred and forty seven using the line above. Collect the terms, and twenty one comes out as seven times four hundred and sixty two, minus three times one thousand and seventy one.

@art run-backwards
So x is minus three and y is seven. In practice the algorithm keeps the coefficients as it goes, with every row of its table still true, so there's no back substitution at all.

@chapter Modular inverses
@words text="ax ≡ 1 (mod m)  ⟺  gcd(a, m) = 1" sub="and the inverse is unique mod m"
Now the payoff. a has an inverse modulo m, a number x with a x congruent to one, mod m, exactly when the gcd of a and m is one. And that inverse is unique, mod m.

@math heading="Why" items="gcd(a, m) = 1  ⟹  ax + my = 1@Bezout gives;;ax ≡ 1 (mod m)@reduce modulo m"
If the gcd is one, Bezout gives a x plus m y equals one. Reduce modulo m, the m y term vanishes, and a x is congruent to one. The coefficient of a is the inverse.

@chapter The inverse of 17 mod 3120
@math heading="Forward" items="3120 = 183 · 17 + 9@three thousand one hundred and twenty;;17 = 1 · 9 + 8@seventeen is;;9 = 1 · 8 + 1@nine is;;gcd = 1@so the gcd"
Here's the calculation RSA needs. Three thousand one hundred and twenty is a hundred and eighty three times seventeen, plus nine. Seventeen is one times nine, plus eight. Nine is one times eight, plus one. So the gcd is one, and an inverse exists.

@math heading="Backward" items="1 = 9 − 1 · 8@one is nine;;= 2 · 9 − 1 · 17@two nines;;= 2 · 3120 − 367 · 17@two times;;−367 + 3120 = 2753@add the modulus"
Now backwards. One is nine minus eight. Substitute for eight, and it's two nines minus seventeen. Substitute for nine, and it's two times three thousand one hundred and twenty, minus three hundred and sixty seven times seventeen. So the inverse is minus three hundred and sixty seven. Add the modulus to get two thousand seven hundred and fifty three.

@words text="17 · 2753 = 46 801 = 15 · 3120 + 1  ✓"
Now check it. seventeen times that is forty six thousand eight hundred and one, one more than fifteen times three thousand one hundred and twenty.

@art round-trip
That number, two thousand seven hundred and fifty three, is the private exponent of the standard textbook RSA key. This one calculation is the whole of RSA key generation.

@chapter Euclid's lemma
@words text="p ∣ ab  ⟹  p ∣ a  or  p ∣ b" sub="Euclid's lemma"
Bezout also proves Euclid's lemma. If a prime p divides a b, and p doesn't divide a, then the gcd of p and a is one. So p x plus a y equals one. Multiply by b. Both terms on the left are multiples of p, so p divides b.

@art dependency-stack
And Euclid's lemma is what makes prime factorisation unique. So the most familiar fact in the course has the deepest justification. It rests on Bezout, which rests on well-ordering.

@chapter Where people slip
@list heading="Common slips" items="Leaving a negative inverse unreduced@The first|Looking for an inverse when the gcd isn't 1@The second|A sign error in back-substitution@And the third"
The first slip is leaving a negative inverse unreduced. The negative one is correct, but the representative from zero up is conventional. The second is looking for an inverse when the gcd isn't one. And the third is a sign error in back substitution.

@art no-inverse
When the gcd isn't one, there's no inverse to find. Two has no inverse modulo four. And for sign errors, always check that a x plus b y really equals the gcd. It's one multiplication, and it catches the error every time.

@chapter Try it
@words text="7⁻¹ (mod 26)" sub="extended Euclid, then verify"
Your turn. Find the inverse of seven modulo twenty six by the extended algorithm, and verify it. It's the decryption key for the affine cipher later in the course.

@end text="Compute the coefficients"
You can run the extended algorithm row by row, with the identity checked on every line, on Learn. That's learn dot get er done dot I O.
