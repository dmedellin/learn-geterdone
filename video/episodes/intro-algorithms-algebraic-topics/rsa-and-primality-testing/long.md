---
format: long
lesson: intro-algorithms-algebraic-topics/rsa-and-primality-testing
title: RSA and the Miller-Rabin primality test
thumb: Easy to find, hard to factor
---

@chapter The gap RSA lives in
@title text="RSA and Primality Testing" sub="Introduction to Algorithms, Sections 31.7–31.8" art=thumb
Two sections of chapter thirty one build a cryptosystem out of the last lesson's arithmetic.

@quote text="The RSA public-key cryptosystem relies on the dramatic difference between the ease of finding large prime numbers and the difficulty of factoring the product of two large prime numbers." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 31.7"
The RSA public key cryptosystem relies on the dramatic difference between the ease of finding large prime numbers and the difficulty of factoring the product of two large prime numbers.

@art public-secret
Each participant publishes one key and keeps the other, and the two undo each other. To send Alice a message, Bob applies her public key, and only she can undo it. To sign, Alice applies her secret key, and anyone can check with her public one.

@chapter RSA in five steps
@list heading="Making a key" items="choose primes p, q · n = pq@two large primes|φ(n) = (p − 1)(q − 1)@phi of n|small odd e, coprime to φ(n)@small odd e|d = e⁻¹ mod φ(n)@the inverse|C = Mᵉ mod n · M = Cᵈ mod n@encrypt"
Choose two large primes p and q, and let n be their product. Phi of n is p minus one times q minus one. Choose a small odd e coprime to phi of n, and let d be the inverse of e mod phi of n. Publish e and n, and keep d. To encrypt, raise to the e. To decrypt, raise to the d.

@math heading="p = 43, q = 67" items="n = 2881 · φ(n) = 42·66 = 2772@twenty eight eighty one;;e = 5 · 5·1109 − 2·2772 = 1 → d = 1109@d is eleven oh nine;;1000⁵ mod 2881 = 962@encrypts to;;962¹¹⁰⁹ mod 2881 = 1000@decrypts"
Here's a key small enough to check. Forty three times sixty seven is twenty eight eighty one, and phi is twenty seven seventy two. With e equal to five, d is eleven oh nine. The message one thousand encrypts to nine sixty two, and nine sixty two to the eleven oh nine decrypts back to one thousand.

@art two-moduli
Why does it work? Check modulo p and modulo q separately. M to the e d is M times a power of M to the p minus one, which is one by Fermat's theorem. The same holds mod q, and the Chinese remainder theorem joins the two.

@chapter Finding primes
@art prime-search
Now the easy half: finding the primes. A random number near n is prime with probability about one over the natural log of n. So for ten twenty four bit numbers, it takes about seven hundred ten tries, half that using only odd numbers. You just need a fast test.

@art fermat-fooled
Fermat's theorem nearly gives one. If n is prime, a to the n minus one is one, mod n. But some composites pass at base two, twenty two of them below ten thousand. And Carmichael numbers pass for every base that shares no factor with them.

@chapter Miller-Rabin
@art square-root-chain
Miller Rabin adds a second check. Write n minus one as two to the t times an odd u. Compute a to the u, then square it t times. If a square is one while the value before it was neither one nor n minus one, that's a nontrivial square root of one, and n is composite.

@art witness-count
For any odd composite, at least half the bases are witnesses. So after s random bases, the test wrongly says prime with probability at most two to the minus s. If n is prime, it always says prime.

@math heading="2047 = 23 · 89" items="2¹¹ = 2048 ≡ 1 ⇒ 2¹⁰²³ ≡ 1@two to the eleven;;base 2: no testimony@base two;;3¹⁰²³ ≡ 1565 · 1565² ≡ 1013 ≠ 1@Base three;;1,804 witnesses of 2,044 bases@witnesses"
The lesson's number is two thousand forty seven, twenty three times eighty nine. Two to the eleven is twenty forty eight, which is one, so base two gives no testimony. Base three is a witness. The lab counts one thousand eight hundred four witnesses among two thousand forty four bases.

@chapter Where people slip
@list heading="Common slips" items="A pass proves primality@The first|More bases fix Fermat@The second|d modulo n, not φ(n)@the third"
The first slip is reading a passed test as proof of primality. Composite is a proof. Prime is only the absence of one. The second is trusting Fermat's test with more bases. Carmichael numbers defeat it. And the third is computing d modulo n instead of modulo phi of n.

@chapter Try it
@words text="n = 1387 · 1386 = 2·693" sub="trace base 2"
Your turn. Compute two to the six ninety three, mod thirteen eighty seven, by repeated squaring, and square it once. Is Fermat's test fooled at base two? Is the strong test?

@end text="Count the witnesses"
You can count the witnesses for any odd number up to two thousand forty seven, on Learn. That's learn dot get er done dot I O.
