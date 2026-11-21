---
format: long
lesson: number-theory-and-cryptography/the-sieve-of-eratosthenes
title: The Sieve of Eratosthenes: find primes by crossing out
thumb: Cross out the multiples
---

@chapter The idea
@title text="The Sieve of Eratosthenes" sub="Number Theory and Cryptography" art=thumb
Here's the oldest algorithm still in use. It finds every prime up to some number n, and it never tests a single number for primality. It just crosses things out.

@art number-grid
Write down every number from two up to n. Now remove multiples. Whatever survives is prime. That's the whole idea, and it costs far less than checking each number separately.

@list heading="Running the sieve" items="List 2 to n@list the candidates|Take the smallest uncrossed number: it is prime@take the smallest|Cross out its multiples from p²@cross out its multiples|Stop when p² > n@stop when p squared"
Here are the steps. First, list the candidates, two through n. One is left out from the start. Then take the smallest number not yet crossed out. It's prime, because nothing smaller divides it. Next, cross out its multiples, starting from p squared. And stop when p squared is bigger than n.

@chapter Sieving to thirty
@math heading="n = 30,  √30 ≈ 5.5" items="p = 2:  cross 4, 6, 8, …, 30@two crosses out;;p = 3:  cross 9, 15, 21, 27@three crosses out;;p = 5:  cross 25@five crosses out;;p = 7:  7² = 49 > 30,  stop@seven squared"
Let's sieve to thirty. The square root of thirty is about five and a half, so only two, three and five need passes. Two crosses out four, six, eight and every even number up to thirty. Three crosses out nine, fifteen, twenty one and twenty seven. The others were already gone. Five crosses out just twenty five. And seven squared is forty nine, past thirty, so we stop.

@words text="2 3 5 7 11 13 17 19 23 29" sub="10 primes"
What's left is two, three, five, seven, eleven, thirteen, seventeen, nineteen, twenty three and twenty nine. Ten primes.

@art crossing-pass
Notice the pass for five crossed out exactly one number. That's typical. Nearly all the work happens at the smallest primes.

@chapter Two shortcuts
@art start-at-square
Why start each pass at p squared? Any smaller multiple of p, k times p with k less than p, has a smaller prime factor, and an earlier pass already removed it. Three's pass starts at nine, not six, because six went with the twos. Starting at two p still works. It's just wasteful.

@art stop-early
And why stop at the square root of n? Because a composite number always has a prime factor no bigger than its own square root. So after sieving with every prime up to the square root of n, anything still standing has no small factor, and it's prime.

@words text="Sieving to 100: passes for 2, 3, 5, 7" sub="97 survives without a pass of its own"
So to sieve to a hundred, you need passes only for two, three, five and seven. Ninety seven, the largest prime below a hundred, survives without a pass of its own.

@chapter What it costs
@art work-shrinks
The pass for a prime p does about n over p operations. Add those up and the total grows like n times log log n. That's very nearly linear. Log log n is under five for any n anyone will ever run.

@words text="n = 10⁶" sub="sieve: a few million · trial division: about a hundred million"
Compare that with testing each number by trial division. At a million, the sieve does a few million operations. Trial division does roughly a hundred million.

@math heading="Primes below n" items="10 → 4@below ten;;100 → 25@below a hundred;;1 000 → 168@below a thousand;;1 000 000 → 78 498@below a million;;n / ln n predicts 72 382@predicts"
And here's what it finds. Four primes below ten, twenty five below a hundred, a hundred and sixty eight below a thousand, and seventy eight thousand four hundred and ninety eight below a million. The prime number theorem's estimate, n over the natural log of n, predicts seventy two thousand three hundred and eighty two. The approximation improves only slowly.

@chapter Its limits
@art too-big
The sieve needs memory in proportion to n, and that's its limit. RSA needs primes about a thousand and twenty four bits long. Sieving at that size is hopeless. There are more candidates than atoms in the universe.

@words text="Large primes: probabilistic tests" sub="such as Miller–Rabin"
So those primes are found a different way. You pick random numbers and test them with probabilistic tests such as Miller Rabin, which decide primality without ever producing a factor.

@chapter Where people slip
@list heading="Common slips" items="Sieving past √n@The first|Starting the inner loop at 2p@The second|Expecting it to scale to cryptographic sizes@And the third"
The first slip is sieving past the square root. Those passes remove nothing new. The second is starting the inner loop at two p, which is correct but wasteful. And the third is expecting the sieve to scale to cryptographic sizes. It doesn't.

@chapter Try it
@words text="Sieve to 200" sub="predict the passes first"
Your turn. Before you sieve to two hundred, say which primes need passes, and roughly how many numbers each will cross out. Then run it and compare. The prediction is the understanding.

@end text="Sieve, and see who crossed out what"
You can run the sieve and see which prime removed every number, on Learn. That's learn dot get er done dot I O.
