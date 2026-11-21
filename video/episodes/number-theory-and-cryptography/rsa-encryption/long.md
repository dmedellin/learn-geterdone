---
format: long
lesson: number-theory-and-cryptography/rsa-encryption
title: RSA encryption, built from the number theory you know
thumb: Easy to multiply, hard to factor
---

@chapter No shared secret
@title text="RSA Encryption" sub="Number Theory and Cryptography" art=thumb
Classical ciphers all need both sides to share a key in advance. RSA doesn't. You publish a key to the whole world, and only you can read what's sent with it. Every step is a theorem from this course.

@art public-padlock
Think of a padlock you hand out freely. Anyone can snap it shut on a message. Only you have the key that opens it.

@chapter Making a key
@list heading="Key generation" items="Choose distinct primes p, q@two large distinct|n = pq@multiply them|φ(n) = (p − 1)(q − 1)@phi of n|e coprime to φ(n)@choose e|d = e⁻¹ mod φ(n)@compute d"
To make a key, choose two large distinct primes, p and q. Multiply them to get n. Then phi of n is p minus one, times q minus one. Choose e between one and phi of n, coprime to it. And compute d, the inverse of e mod phi of n, with the extended Euclidean algorithm.

@art two-keys
The public key is n and e. The private key is n and d. And p, q and phi of n must stay secret.

@words text="c = mᵉ mod n      m = cᵈ mod n" sub="0 ≤ m < n"
To encrypt a message, written as a number m below n, compute m to the e, mod n. To decrypt, raise the ciphertext to the d, mod n. Each is a single modular exponentiation, done by square and multiply.

@chapter Why decryption works
@math heading="(mᵉ)ᵈ ≡ m (mod n)" items="ed = 1 + kφ(n)@e d is;;m^(ed) = m · (m^φ(n))ᵏ@so m to the;;≡ m · 1ᵏ = m  (mod n)@Euler's theorem"
Why does decryption work? Since e d is congruent to one mod phi of n, e d is one plus k times phi of n. So m to the e d is m, times m to the phi of n, to the k. And by Euler's theorem, when m is coprime to n, m to the phi of n is one. So you get m.

@words text="gcd(m, n) ≠ 1?" sub="work mod p and mod q, then the Chinese remainder theorem"
If m happens to share a factor with n, it still works. Mod p, either p divides m and both sides are zero, or Fermat applies. The same goes mod q, and the Chinese remainder theorem joins the two.

@chapter The textbook key
@math heading="The standard example" items="p = 61,  q = 53,  n = 3233@sixty one;;φ(n) = 60 · 52 = 3120@phi of n;;e = 17,  d = 2753@e is seventeen;;65¹⁷ mod 3233 = 2790@encrypt;;2790²⁷⁵³ mod 3233 = 65  ✓@and decrypting"
Here's the standard example. p is sixty one and q is fifty three, so n is three thousand two hundred and thirty three. Phi of n is sixty times fifty two, three thousand one hundred and twenty. e is seventeen, and d is two thousand seven hundred and fifty three, the inverse Bezout gave us. Encrypt sixty five, and you get two thousand seven hundred and ninety. And decrypting gives sixty five back.

@art message-loop
So the message makes a round trip. The public key locks it, and only the private exponent unlocks it.

@chapter A key by hand
@math heading="p = 11, q = 13" items="n = 143,  φ(n) = 10 · 12 = 120@n is a hundred;;e = 7:  120 = 17 · 7 + 1  ⟹  d ≡ −17 ≡ 103@take e;;7 · 103 = 721 = 6 · 120 + 1  ✓@check"
Now a key small enough for paper. Take p eleven and q thirteen, so n is a hundred and forty three and phi of n is a hundred and twenty. Take e equal to seven. A hundred and twenty is seventeen sevens plus one, so d is minus seventeen, which is a hundred and three. Check: seven times a hundred and three is seven hundred and twenty one, one more than six times a hundred and twenty.

@math heading="Encrypt m = 9" items="9² = 81,  9⁴ = 6561 ≡ 126@nine squared;;9⁷ ≡ 126 · 81 · 9@nine to the seventh;;126 · 81 = 10206 ≡ 53,  53 · 9 = 477 ≡ 48@the first product;;48¹⁰³ mod 143 = 9  ✓@decrypting"
Encrypt nine. Nine squared is eighty one, and nine to the fourth reduces to a hundred and twenty six. Nine to the seventh is a hundred and twenty six, times eighty one, times nine. The first product reduces to fifty three, and fifty three times nine reduces to forty eight. So the ciphertext is forty eight, and decrypting gives nine again.

@chapter What security rests on
@art multiply-easy
An attacker sees n and e. To find d, they need phi of n. But knowing phi of n is as good as knowing the factors, because p plus q is n minus phi of n plus one, and with p times q equal to n, that's a quadratic. So RSA is secure only if factoring is hard.

@art split-hard
And that's believed, not proved. The best known general method, the number field sieve, isn't polynomial. The largest RSA modulus factored publicly is eight hundred and twenty nine bits. Nobody has proved breaking RSA needs factoring, and Shor's algorithm would factor quickly on a large enough quantum computer.

@art same-ciphertext
Textbook RSA also isn't safe to deploy. It's deterministic, so identical messages give identical ciphertexts and an attacker can test guesses. Real systems add randomised padding, called OAEP.

@chapter Where people slip
@list heading="Common slips" items="Leaking φ(n)@The first|Using equal or close primes@The second|Deploying textbook RSA@And the third"
The first slip is publishing or leaking phi of n. With n, it gives away the factorisation. The second is using equal or close primes, which makes n easy to factor. And the third is deploying textbook RSA.

@chapter Try it
@words text="p = 17,  q = 23,  e = 3" sub="build the key, then break it"
Your turn. Build a key from seventeen and twenty three, with e equal to three. Find n, phi of n and d. Encrypt and decrypt a small message. Then factor n and recover d yourself.

@end text="Generate, use, break"
You can generate a key, encrypt with it, and watch the page break it again, on Learn. That's learn dot get er done dot I O.
