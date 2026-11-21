---
format: long
lesson: randomised-algorithms/witnesses-liars-and-one-sided-error
title: Miller–Rabin: witnesses, liars and the number 561
thumb: A witness is a proof
---

@chapter Proof or silence
@title text="Witnesses, Liars, and One-Sided Error" sub="Randomised Algorithms" art=thumb
Here's a primality test that can prove a number is composite, and can never prove it's prime. Each base either hands you a certificate, or says nothing at all.

@math heading="The strong test on base a" items="n − 1 = d·2ˢ,  d odd@n minus one;;x₀ = aᵈ mod n,  then square, s − 1 times@a to the d;;x₀ = 1  or some xᵢ = n − 1  ⟹  inconclusive@inconclusive;;otherwise a is a witness: n is composite@a witness"
Write n minus one as d times two to the s, with d odd. Start at a to the d, mod n, then keep squaring. If the chain starts at one, or hits n minus one, the base is inconclusive. Otherwise a is a witness, and n is composite.

@chapter Why a witness is a proof
@art square-root-one
If n is prime, Fermat says the chain ends at one. Look at the first one in the chain. If it isn't the very first term, the term before it is a square root of one. And modulo a prime, the only square roots of one are one and minus one. So it hit n minus one, and the base is inconclusive.

@words text="no base is ever a witness for a prime"
So a prime never has a witness, which means a witness proves compositeness. At ninety seven, all ninety four usable bases are inconclusive. That's not evidence ninety seven is prime. It's a consequence of it being prime.

@chapter The certificate
@art witness-chain
So there are two ways to run the chain. One reaches one or minus one where a prime would. The other never does, and that one is a proof.

@math heading="n = 341,  a = 2" items="d = 85,  s = 2@eighty five;;2⁸⁵ mod 341 = 32@thirty two;;32² = 1024 = 3·341 + 1@squaring gives one;;gcd(31, 341) = 31@a factor"
Take three forty one with base two. d is eighty five, s is two. Two to the eighty five, mod three forty one, is thirty two. Then squaring gives one. So thirty two is a square root of one that isn't plus or minus one, and the greatest common divisor of thirty one and three forty one, thirty one, is a factor.

@art factor-split
That's why repeating the test only builds evidence one way. A thousand silent bases never add up to a proof of primality.

@chapter Carmichael numbers
@art fermat-blind
The Fermat test just checks whether a to the n minus one is one. A Carmichael number passes that for every base coprime to it. The smallest is five sixty one, three times eleven times seventeen.

@math heading="n = 561, every base" items="strong test:  550 of 558 witnesses = 275/279@five hundred and fifty;;Fermat:  240 of 558, all sharing a factor@two hundred and forty;;Fermat on coprime bases:  0 of 318@catches zero"
Five sixty one has five hundred and fifty eight usable bases. The strong test finds five hundred and fifty witnesses. The Fermat test catches two hundred and forty, but every one of those shares a factor with five sixty one. On the three hundred and eighteen coprime bases, it catches zero.

@list heading="The eight liars for 561" items="50, 101, 103, 256@fifty|305, 458, 460, 511@three oh five"
The eight bases that say nothing are fifty, one oh one, one oh three, two fifty six, three oh five, four fifty eight, four sixty, and five eleven. Base fifty starts the chain at five sixty, which is n minus one, so it's inconclusive at the first step.

@chapter The error after t bases
@art liar-fraction
Because the error is one sided, t random bases are wrong about a composite only if all t are liars. If q is the liar fraction, that's q to the t.

@art repeated-bases
The theorem that at least three quarters of bases are witnesses is stated here, not proved, and it gives at most one quarter to the t. The panel checks it on the number on screen, which is a test, not a proof.

@math heading="561,  q = 4/279" items="t = 5:  1024/1690522737399 ≈ 6.1 × 10⁻¹⁰@t equals five;;bound:  (1/4)⁵ = 1/1024@the bound"
At t equals five on five sixty one, the exact error is about one in one point six five billion. The bound allows one in a thousand and twenty four. That gap is what at least three quarters costs: it has to cover the worst composite.

@words text="2047 = 23 · 89" sub="240 of 2044 bases are liars · base 2 is one"
The worst of the lab's examples is two thousand and forty seven, where two hundred and forty of its bases are liars, including base two, the one everybody tries first. A fixed base isn't a randomised test. It's a deterministic one, with a known counterexample.

@chapter Where people slip
@list heading="Common slips" items="Reading silence as evidence of primality@The first|Quoting Fermat's catch rate on a Carmichael number@The second|Using one fixed base@And the third"
The first slip is reading an inconclusive run as evidence of primality. The second is quoting the Fermat test's overall catch rate on a Carmichael number. Forty out of ninety three sounds half working, and it's all common factors. And the third is using one fixed base. Draw bases at random, and say how many.

@end text="A witness is a proof"
Try every base on five sixty one and see the liars, on Learn. That's learn dot get er done dot I O.
