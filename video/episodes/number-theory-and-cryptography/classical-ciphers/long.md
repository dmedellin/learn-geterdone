---
format: long
lesson: number-theory-and-cryptography/classical-ciphers
title: Classical ciphers: shift, affine, Vigenère, and how each one falls
thumb: Why every old cipher broke
---

@chapter Why study broken ciphers
@title text="Classical Ciphers" sub="Number Theory and Cryptography" art=thumb
Here are three ciphers built from modular arithmetic, and each one is broken by a different attack. They're worth studying anyway, because the reasons they fail are exactly the requirements a real cipher has to meet.

@chapter The shift cipher
@words text="E(x) = (x + k) mod 26" sub="letters as 0 … 25 · Caesar: k = 3"
Number the letters zero to twenty five. The shift cipher adds a key k, mod twenty six, and decryption subtracts it. Caesar's cipher is k equals three.

@art cipher-wheel
There are only twenty five useful keys, so an attacker just tries them all and reads the output. That takes seconds by hand. The first lesson: the key space must be far too large to search. Modern ciphers use two to the hundred and twenty eight keys or more.

@chapter The affine cipher
@words text="E(x) = (ax + b) mod 26,  gcd(a, 26) = 1" sub="D(y) = a⁻¹(y − b) mod 26"
The affine cipher multiplies too: a x plus b, mod twenty six. To decrypt, you need the inverse of a, so a must be coprime to twenty six. That leaves twelve valid multipliers, and twelve times twenty six is three hundred and twelve keys.

@math heading="a = 5, b = 8" items="H = 7:  5 · 7 + 8 = 43 ≡ 17 = R@the letter H;;5 · 21 = 105 = 4 · 26 + 1  ⟹  5⁻¹ ≡ 21@to decrypt;;21 · (17 − 8) = 189 ≡ 7 = H  ✓@twenty one times"
Take a five and b eight. The letter H is seven. Five times seven plus eight is forty three, which is seventeen, the letter R. To decrypt, the inverse of five is twenty one, since five times twenty one is a hundred and five, one more than four twenty sixes. Twenty one times seventeen minus eight is a hundred and eighty nine, which is seven. Back to H.

@art two-outputs
Break the rule and use a equal to thirteen, and every letter lands on one of just two outputs. There's nothing to decrypt.

@chapter Breaking it with frequencies
@art letter-bars
Three hundred and twelve keys is still easy to search, but there's a worse problem. Each letter always maps to the same letter, so frequencies survive. E is the commonest letter in English, at about twelve percent, and whatever it maps to will be the commonest ciphertext letter.

@math heading="Guess E → R and T → I" items="4a + b ≡ 17,  19a + b ≡ 8  (mod 26)@four a plus b;;15a ≡ −9 ≡ 17@subtract;;15⁻¹ ≡ 7  ⟹  a ≡ 7 · 17 = 119 ≡ 15@the inverse of fifteen;;b ≡ 17 − 60 = −43 ≡ 9@and b"
Say the commonest ciphertext letters are R and I, and guess they're E and T. That gives four a plus b congruent to seventeen, and nineteen a plus b congruent to eight. Subtract: fifteen a is minus nine, which is seventeen. The inverse of fifteen is seven, so a is seven times seventeen, a hundred and nineteen, which is fifteen. And b is seventeen minus sixty, minus forty three, which is nine. The key is fifteen, nine.

@chapter The Vigenère cipher
@art repeating-key
Vigenere fixes that by using a keyword: a repeating sequence of shifts. The same plaintext letter encrypts differently depending on its position, so simple frequency counts fail. It was called the indecipherable cipher for three centuries.

@list heading="Breaking Vigenère" items="Find the key length@first|Split into columns@then split|Break each column as a shift cipher@each column"
It falls in two stages. First, find the key length. Repeated fragments of plaintext that line up with the same key position give repeated ciphertext, and the distances between them are multiples of the length. That's Kasiski's method. Then split the ciphertext into that many columns. Each column is a single shift cipher, broken by frequency.

@chapter The one-time pad
@words text="Random · as long as the message · never reused" sub="Shannon: perfect secrecy"
Now the cipher that can't be broken. If the key is uniformly random, at least as long as the message, and never reused, the ciphertext tells an attacker nothing. That's Shannon's theorem. But the key is as long as the message, and has to be shared in advance, which is the problem encryption was meant to solve.

@art pad-reuse
And reuse destroys it completely. Two messages under the same key combine to cancel the key out, and both plaintexts can usually be recovered. That's the failure that broke the Soviet VENONA traffic.

@art padlock-pair
Notice that every cipher here needs both sides to share the key in advance. RSA answers that problem a different way: no shared secret is needed at all.

@chapter Where people slip
@list heading="Common slips" items="An affine multiplier sharing a factor with 26@The first|Believing a large key space is enough@The second|Reusing a one-time pad@And the third"
The first slip is choosing an affine multiplier that shares a factor with twenty six, like thirteen or any even number. The second is believing a large key space is enough. Even with millions of keys, the affine cipher would fall to frequencies. And the third is reusing a one-time pad.

@chapter Try it
@words text="Commonest letters: K and D" sub="assume E → K and T → D"
Your turn. Suppose the two commonest ciphertext letters are K and D. Assume they come from E and T, set up the two congruences, and solve for a and b.

@end text="Encrypt, and break it"
You can try any affine key and see which ones can't be decrypted, on Learn. That's learn dot get er done dot I O.
