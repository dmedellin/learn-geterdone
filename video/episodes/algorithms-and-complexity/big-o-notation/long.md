---
format: long
lesson: algorithms-and-complexity/big-o-notation
title: Big-O, Omega and Theta: the proof is two numbers
thumb: Find C, find k
---

@chapter The question
@title text="Big-O, Big-Omega and Big-Theta" sub="Algorithms and Complexity" art=thumb
People say an algorithm is big O of n squared all the time. But what does that sentence actually claim? It's a precise statement, and proving it comes down to finding two numbers.

@chapter The definition
@math heading="Big-O" items="f(n) = O(g(n))@f of n is big O;;⟺  |f(n)| ≤ C·|g(n)|  for all n ≥ k@positive constant C;;(C, k) is a witness@a witness"
f of n is big O of g of n when there's a positive constant C and a threshold k, so that f is at most C times g for every n from k onwards. The pair C and k is called a witness.

@art ceiling-curve
In a picture, past some point, f stays under a fixed multiple of g, forever. What happens before k doesn't matter at all. Proving a big O claim means producing C and k. That's the entire content of the definition.

@art floor-curve
Big Omega flips it round. f is at least C times g from k onwards, so it's a lower bound.

@art sandwich
And big Theta means both at once. f is trapped between two multiples of g, so f and g grow at the same rate.

@chapter Proving a bound
@math heading="3n² + 5n + 100 = O(n²)" items="for n ≥ 1:  n ≤ n²  and  1 ≤ n²@for n at least one;;3n² + 5n + 100 ≤ 3n² + 5n² + 100n²@So three n squared"
Let's prove one. For n at least one, n is at most n squared, and one is at most n squared. So three n squared plus five n plus a hundred is at most three n squared plus five n squared plus a hundred n squared.

@math heading="3n² + 5n + 100 = O(n²)" items="3n² + 5n² + 100n² = 108n²@a hundred and eight;;C = 108,  k = 1@The witnesses"
Add those up and you get a hundred and eight n squared. The witnesses are C equals a hundred and eight, and k equals one. That's a complete proof.

@words text="n ≥ 10:  C = 5 works too" sub="any valid pair proves it"
That's not the sharpest choice. From n equals ten on, C equals five works. But it doesn't matter. Any pair that works proves the claim.

@chapter A disproof
@math heading="n² ≠ O(n)" items="suppose n² ≤ C·n  for all n ≥ k@Suppose;;divide by n:  n ≤ C  for all n ≥ k@Divide by n;;false for n > max(C, k)@false"
Now the other way. Is n squared big O of n? Suppose it were, so n squared is at most C n from k onwards. Divide by n, and you get n at most C, for every n from k on. That's false as soon as n is bigger than both C and k. So no witnesses exist.

@art escaping-line
That's the shape of every disproof. Assume the witnesses exist, then derive a contradiction.

@chapter Useful properties
@list heading="Rules" items="Transitive: f = O(g), g = O(h) ⟹ f = O(h)@chains|Sum: f₁ + f₂ = O(max(g₁, g₂))@the sum rule|Product: f₁·f₂ = O(g₁·g₂)@products multiply|Polynomials: degree k gives Θ(nᵏ)@a polynomial"
A few rules do most of the work. Big O chains, so it's transitive. By the sum rule, adding two costs gives big O of the larger one. Products multiply. And a polynomial of degree k is Theta of n to the k.

@art log-bases
One more. Log base two of n and log base ten of n differ by a constant factor, so they're in the same class. That's why nobody writes the base of a logarithm inside a big O.

@art set-bucket
And notice that the equals sign is misleading. Big O of g is a set, the functions bounded above by a multiple of g. So read f equals big O of g as f is in big O of g. It isn't symmetric.

@chapter Where people slip
@list heading="Common slips" items="Claiming O where Θ is meant@The first|Not saying which case is bounded@The second|Writing “at least O(n)”@The third"
The first slip is claiming big O where Theta is meant. n is big O of n squared is true, and says almost nothing. The second is not saying which case is bounded. And the third is saying at least big O of n. Big O is already an upper bound, so the word you want is Omega.

@words text="“Quicksort is O(n log n)” ✗" sub="worst case Θ(n²) · average case Θ(n log n)"
The second one is everywhere. Quicksort is big O of n log n is a false statement, because quicksort's worst case is Theta of n squared. What's true is that its average case is Theta of n log n. Worst, average and best case are different functions.

@chapter Try it
@words text="Find C and k" sub="for 3n² + 5n + 100 ≤ 5n²,  start at n = 10"
Try it. Check for yourself that C equals five works from n equals ten. Then try to find a pair with a smaller k, and see how C has to grow.

@end text="The proof is the pair (C, k)"
The full lesson on big O, Omega and Theta is on Learn. That's learn dot get er done dot I O.
