---
format: long
lesson: number-theory-and-cryptography/primes-and-factorisation
title: Primes and unique factorisation: the atoms of arithmetic
thumb: One way to build every number
---

@chapter The atoms
@title text="Primes and Unique Factorisation" sub="Number Theory and Cryptography" art=thumb
Every whole number above one can be broken into primes, and there's only one way to do it. That's the fundamental theorem of arithmetic, and almost every later argument in number theory leans on it.

@art prime-atoms
Think of primes as the atoms of multiplication. An integer p bigger than one is prime if its only positive divisors are one and p. A number above one that isn't prime is composite.

@words text="1 is neither prime nor composite" sub="by decision"
And one is neither. That isn't an accident or a technicality. It's a decision, made to keep the main theorem clean.

@math heading="If 1 were prime" items="6 = 2 · 3@six would be two;;6 = 1 · 2 · 3@one times two;;6 = 1 · 1 · 2 · 3@one times one"
Here's why. If one counted as prime, six would be two times three, but also one times two times three, and one times one times two times three, and so on forever. Uniqueness would need an awkward exception.

@chapter The fundamental theorem
@words text="Every n > 1 is a product of primes" sub="unique up to the order of the factors"
The theorem says every integer above one is a product of primes, and that factorisation is unique, apart from the order you write the factors in.

@art factor-tree
Existence is strong induction. If n is prime, you're done. Otherwise n is a times b, with both smaller than n, so each already factors into primes. Put the two lists together.

@words text="p ∣ ab  ⟹  p ∣ a  or  p ∣ b" sub="Euclid's lemma"
Uniqueness is the hard half. It needs Euclid's lemma: if a prime divides a product, it divides one of the factors. Take two factorisations of n. A prime from the first divides the second product, so it equals one of its primes. Cancel, and repeat.

@math heading="Not every number system has it" items="6 = 2 · 3@six is two times three;;6 = (1 + √−5)(1 − √−5)@and also"
And uniqueness isn't universal. In numbers of the form a plus b times the square root of minus five, six is two times three, and also one plus root minus five, times one minus root minus five, with all four factors unbreakable. Unique factorisation is a property of the integers.

@chapter Infinitely many primes
@art plus-one
Euclid showed the primes never run out. Take any finite list of primes. Multiply them all together and add one. Call that N.

@math heading="Euclid's argument" items="N = p₁p₂⋯pₖ + 1@N is bigger;;q ∣ N,  q prime@has a prime factor q;;q = pᵢ  ⟹  q ∣ 1  ✗@If that prime;;2·3·5·7·11·13 + 1 = 30031 = 59 · 509@thirty thousand and thirty one"
N is bigger than one, so N has a prime factor q. If that prime were on the list, it would divide both the product and N, and so their difference, which is one. Impossible. But careful: N itself needn't be prime. Two times three times five times seven times eleven times thirteen, plus one, is thirty thousand and thirty one, which is fifty nine times five hundred and nine.

@chapter Stop at the square root
@art square-root-bound
Here's a shortcut for testing. If n is composite, it has a prime factor no bigger than the square root of n. Write n as a times b, with a the smaller. If both were bigger than the square root, their product would be bigger than n.

@words text="101:  try 2, 3, 5, 7" sub="none divides, so 101 is prime"
So to test one hundred and one, you only need the primes up to ten: two, three, five and seven. None divides it, so it's prime. That's four divisions instead of ninety nine.

@chapter A worked example
@math heading="Factor 360" items="360 ÷ 2 ÷ 2 ÷ 2 = 45@divide by two;;45 ÷ 3 ÷ 3 = 5@forty five;;360 = 2³ · 3² · 5@so three hundred;;(3+1)(2+1)(1+1) = 4 · 3 · 2 = 24 divisors@add one to each"
Factor three hundred and sixty. Divide by two three times, to reach forty five. Divide by three twice, to reach five, which is prime. So three hundred and sixty is two cubed, times three squared, times five. To count its divisors, add one to each exponent and multiply: four times three times two is twenty four.

@art divisor-grid
Why does that work? A divisor is just a choice of exponent for each prime, from zero up to its exponent in n, chosen independently. And uniqueness of factorisation guarantees each choice gives a different divisor.

@chapter How the primes thin out
@art thinning-dots
There are twenty five primes below a hundred, a hundred and sixty eight below a thousand, and seventy eight thousand four hundred and ninety eight below a million. They thin out slowly. Near ten to the hundred, roughly one number in two hundred and thirty is prime. That density is what makes RSA key generation practical.

@chapter Where people slip
@list heading="Common slips" items="Calling 1 prime@The first|Believing Euclid's N is always prime@The second|Trial dividing past √n@And the third"
The first slip is calling one prime. The second is believing Euclid's N is always prime. It has a prime factor outside the list, and that's all the proof claims. And the third is trial dividing past the square root, which is wasted work.

@chapter Try it
@words text="Factor 2520" sub="predict the divisor count from the exponents"
Your turn. Factor two thousand five hundred and twenty completely. Then predict how many divisors it has from the exponents alone, before you list a single one.

@end text="Factor a number, count its divisors"
You can factor any number step by step and watch the divisor count come from the exponents, on Learn. That's learn dot get er done dot I O.
