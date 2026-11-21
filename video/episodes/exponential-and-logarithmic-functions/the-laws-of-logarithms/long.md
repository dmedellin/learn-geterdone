---
format: long
lesson: exponential-and-logarithmic-functions/the-laws-of-logarithms
title: The laws of logarithms, and the two that aren't laws
thumb: Products become sums
---

@chapter Three laws, one idea
@title text="The Laws of Logarithms" sub="Exponential and Logarithmic Functions" art=thumb
Three laws turn a product into a sum, a quotient into a difference, and a power into a multiple. Each one is an exponent law you already know, written in the other notation. And two rules that look like laws are not.

@words text="M = bᵐ,    N = bⁿ" sub="m = log_b M,    n = log_b N"
Take positive numbers M and N, and call their logarithms m and n. By the definition, M is b to the m, and N is b to the n. Then one exponent law finishes the job.

@chapter The product law
@math heading="Product law" items="M·N = bᵐ·bⁿ = b^(m+n)@M times N;;log_b(M·N) = m + n@So m plus n;;log_b(M·N) = log_b M + log_b N@In other words"
M times N is b to the m times b to the n, which is b to the m plus n. So m plus n is the exponent that produces M times N, and that's exactly what its logarithm means. In other words, the log of a product is the sum of the logs.

@art product-sum
Multiplying powers of the same base adds the exponents. A logarithm is an exponent. So the logarithm of a product is the sum of the logarithms. It's the same statement, written twice.

@chapter Quotients and powers
@math heading="Quotient law" items="M/N = bᵐ/bⁿ = b^(m−n)@M over N;;log_b(M/N) = log_b M − log_b N@the log of a quotient"
Division works the same way. M over N is b to the m minus n, so the log of a quotient is the log of the top minus the log of the bottom.

@art quotient-difference
The subtraction is where signs get lost, and the order matters. The log of N over M is the negative of the log of M over N.

@math heading="Power law" items="Mᵖ = (bᵐ)ᵖ = b^(mp)@M to the p;;log_b(Mᵖ) = p·log_b M@So the log"
For powers, M to the p is b to the m, to the p, which is b to the m p. So the log of M to the p is p times the log of M. Here p can be anything, negative or a fraction, which is how a root comes out as a coefficient.

@art power-stack
Picture M cubed as M times M times M. Each factor contributes one log of M, so the three of them contribute three.

@art number-check
A number check catches a misremembered law fast. Log base two of eight times four is log base two of thirty two, which is five. And log base two of eight, plus log base two of four, is three plus two. Also five.

@chapter Two invented laws
@math heading="Not laws" items="log₂(8 + 8) = log₂(16) = 4@sixteen, which is four;;log₂(8) + log₂(8) = 3 + 3 = 6@three plus three;;log₂(8/4) = log₂(2) = 1@eight over four;;log₂(8) / log₂(4) = 3/2@divided by"
Now the fakes, in base two. The log of eight plus eight is the log of sixteen, which is four. But log eight plus log eight is three plus three, six. And the log of eight over four is the log of two, one. But log eight divided by log four is three over two.

@art broken-sum
There's no law at all for a sum inside a logarithm. The ratio is more interesting. Log eight over log four, in base two, equals log base four of eight, which really is three over two. A ratio of logs is a change of base, not the log of a ratio.

@chapter Expanding, with a check
@math heading="log_b( x³·√y / z² )" items="log_b(x³·√y) − log_b(z²)@quotient law;;log_b(x³) + log_b(√y) − log_b(z²)@product law;;log_b(x³) + log_b(y^(1/2)) − log_b(z²)@as a power;;3·log_b x + ½·log_b y − 2·log_b z@power law"
Here's an expansion: the log of x cubed root y, over z squared. The quotient law splits off the bottom. The product law splits the top. Write the root as a power, one half. Then the power law brings every exponent down: three log x, plus a half log y, minus two log z.

@math heading="check:   b = 2,   x = 8,   y = 16,   z = 4" items="8³·√16 / 4² = 512·4 / 16 = 128@five hundred and twelve;;log₂(128) = 7@its log;;3·3 + ½·4 − 2·2 = 9 + 2 − 4 = 7@nine plus two"
Check it with base two, x eight, y sixteen and z four. Inside, five hundred and twelve times four, over sixteen, is a hundred and twenty eight, and its log is seven. On the right, nine plus two minus four. Also seven.

@chapter A domain that shrinks
@art domain-shrink
Log of x squared equals two log x is true for positive x, and false for negative x. At minus five, the left side is log of twenty five, a perfectly good number. The right side is two log of minus five, which isn't defined.

@words text="log_b(x²) = 2·log_b|x|" sub="for every x ≠ 0"
The identity that holds everywhere except zero uses the absolute value: two log of the absolute value of x. Expanding a logarithm can shrink its domain, and your answer should say so.

@chapter Where people slip
@list heading="Common slips" items="Splitting the log of a sum@The first|A quotient of logs as the log of a quotient@The second|Bringing down an exponent that isn't on everything@The third"
The first is splitting the log of a sum: log of x plus three is not log x plus log three. The second is turning a quotient of logs into the log of a quotient. The third is bringing down an exponent that isn't on the whole argument.

@chapter Try it
@words text="log_b( √(x⁵·y) / z³ )" sub="first line:   the quotient-law split"
Your turn. Expand the log of the square root of x to the fifth times y, all over z cubed. Start with the quotient law split, write the root as a power, finish, then condense it back. Check that every exponent lands on the whole factor it came from.

@end text="Each law, checked on your numbers"
You can enter your own numbers and watch the three laws hold and the two fakes fail, on Learn. That's learn dot get er done dot I O.
