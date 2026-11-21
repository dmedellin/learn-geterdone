---
format: long
lesson: logic-and-proof/contraposition-and-contradiction
title: Proof by contraposition vs proof by contradiction
thumb: Two ways round a dead end
---

@chapter The question
@title text="Contraposition and Contradiction" sub="Logic and Proof" art=thumb
Sometimes a direct proof just stalls. You assume p, and there's nowhere useful to go. Two indirect techniques get you round that. They're often confused, but they aren't the same technique, and knowing which one fits is half the work.

@chapter Contraposition
@art back-door
To prove p implies q by contraposition, prove not q implies not p instead. It's a different theorem with the same meaning. The two are logically equivalent, so a proof of either is a proof of both.

@math heading="If n² is even, then n is even" items="contrapositive: if n is odd, then n² is odd@We prove;;n = 2k + 1@Let n be odd;;n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1@n squared is;;2k² + 2k is an integer, so n² is odd  ∎@That's odd"
Take: if n squared is even, then n is even. We prove the contrapositive: if n is odd, then n squared is odd. Let n be odd, so n is two k plus one. Then n squared is four k squared plus four k plus one, which is two times, two k squared plus two k, plus one. That's odd.

@art detour-sign
Compare the direct attempt. Assuming n squared is even gives n squared equals two m, and there's nowhere to go. Getting from n squared back to n needs unique factorisation, from Number Theory. The contrapositive hands you n itself, in a form you can compute with. That's the whole reason to choose it.

@math heading="If 3n + 2 is odd, then n is odd" items="contrapositive: n even ⟹ 3n + 2 even@if n is even;;n = 2k@so n is two k;;3n + 2 = 6k + 2 = 2(3k + 1)  ∎@six k plus two"
Another. If three n plus two is odd, then n is odd. The contrapositive: if n is even, then three n plus two is even. Let n be even, so n is two k. Then three n plus two is six k plus two, which is two times, three k plus one. Even. Two lines.

@chapter Contradiction
@art collision
Proof by contradiction is different. To prove s, assume not s, and derive something known to be false. A false conclusion can't follow from a true assumption, so not s must be false, and s holds.

@math heading="√2 is irrational" items="suppose √2 = a/b, in lowest terms@Suppose;;2 = a²/b²  ⟹  a² = 2b²@Squaring;;a² even  ⟹  a even, a = 2c@a is even"
Suppose the square root of two is rational, a over b, in lowest terms. Squaring, a squared is two b squared. So a squared is even, and by the theorem we just proved, a is even. Write a as two c.

@math heading="√2 is irrational" items="4c² = 2b²  ⟹  b² = 2c²@Substituting;;b² even  ⟹  b even@b is even too;;a and b both even: not lowest terms  ✗@both divisible by two"
Substituting gives four c squared equals two b squared, so b squared equals two c squared, and b is even too. But then a and b are both divisible by two. They weren't in lowest terms after all. The assumption is false, and the square root of two is irrational.

@art halved-bars
Notice what was contradicted. Not a law of arithmetic, but a condition we imposed ourselves: lowest terms. Imposing it was the move that made the proof possible. And a good proof names it: this contradicts the assumption that the fraction was in lowest terms.

@chapter Choosing between them
@art fork-sign
So how do you choose? Try the direct proof first, and notice where it stalls. The stall is diagnostic. Unable to use p? Try contraposition. Nothing to grab hold of at all? Try contradiction.

@list heading="Which technique?" items="Conditional, ¬q concrete: contraposition@concrete|Non-existence or impossibility: contradiction@impossibility|Assumed p ∧ ¬q, derived ¬p: that's contraposition@you're doing contraposition"
If the claim is a conditional and not q is concrete, use contraposition. If it asserts non existence or impossibility, use contradiction, because assuming the thing exists gives you something to hold. And if you assumed p and not q, then derived not p, you're doing contraposition. Say so.

@art extra-bead
Euclid's proof that there are infinitely many primes is often told as a contradiction. But look at how it actually runs.

@words text="N = p₁p₂⋯pₙ + 1" sub="a prime factor of N is not on the list"
Take any finite list of primes, multiply them, and add one. That number has a prime factor, and no prime on the list divides it, since that prime would divide one. So, given any list, it builds a prime that isn't on it. As written, it's direct and constructive, and stronger.

@chapter Where people slip
@list heading="Common slips" items="Proving the inverse instead@The first|Calling every indirect proof a contradiction@The second|Not naming what is contradicted@the third"
The first slip is proving the inverse, not p implies not q, instead of the contrapositive. The contrapositive negates and swaps. The second is calling every indirect proof a contradiction. And the third is ending with contradiction, without saying what was contradicted.

@chapter Try it
@words text="If n is an integer and n² + 5 is odd, then n is even." sub="pick the technique before you start"
Your turn. Prove: if n is an integer and n squared plus five is odd, then n is even. Before you start, say which technique you'll use, and why the other one would be harder.

@end text="See why contraposition is legitimate"
You can check that a conditional and its contrapositive agree in every row, on Learn. That's learn dot get er done dot I O.
