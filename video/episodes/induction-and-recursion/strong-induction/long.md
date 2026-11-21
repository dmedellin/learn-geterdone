---
format: long
lesson: induction-and-recursion/strong-induction
title: Strong induction: assume every earlier case
thumb: Count how far back you reach
---

@chapter When one case back isn't enough
@title text="Strong Induction" sub="Induction and Recursion" art=thumb
Ordinary induction gives you one fact to work with: P of k. But some proofs of P of k plus one need a case further back, and you don't always know which one.

@art reach-back
Strong induction fixes that. Instead of assuming just the previous case, you assume every case from the start up to k. Then you prove P of k plus one, using whichever of them you need.

@math heading="Strong induction" items="P(n₀) holds@P of n nought;;P(n₀), …, P(k) together imply P(k+1),  every k ≥ n₀@together imply;;then P(n) for all n ≥ n₀@for all n"
Formally: if P of n nought holds, and for every k, the truth of P of n nought through P of k together imply P of k plus one, then P of n holds for all n from n nought on.

@words text="Q(n):  P(m) for all n₀ ≤ m ≤ n" sub="ordinary induction on Q = strong induction on P"
Is it stronger? No. Define Q of n to mean P holds for every m from n nought up to n. Ordinary induction on Q gives you exactly strong induction for P. Nothing is gained in power. What you gain is a hypothesis that matches the shape of the argument.

@chapter Products of primes
@art factor-tree
Here's an argument that needs it. Claim: every integer from two on is a product of one or more primes. Base: two is prime, so it's a product of one prime.

@math items="assume every m with 2 ≤ m ≤ k is a product of primes@assume every;;k+1 prime:  done@If k plus one is prime;;else k+1 = ab with 2 ≤ a, b ≤ k@Otherwise;;a, b products of primes, so ab is too@both a and b"
Now assume every integer from two to k is a product of primes. If k plus one is prime, you're done. Otherwise k plus one is a times b, with both between two and k. By the strong hypothesis, both a and b are products of primes, so their product is too.

@words text="a and b could be anywhere below k+1"
Ordinary induction is useless here. Knowing that k factors tells you nothing about k plus one, because a and b could be anywhere below it. The hypothesis has to cover them all.

@chapter Postage stamps
@art stamps
Next, postage. Claim: every amount from eight cents on can be made from three cent and five cent stamps.

@math heading="n = 3a + 5b,  n ≥ 8" items="8 = 3 + 5@eight is;;9 = 3 + 3 + 3@nine is;;10 = 5 + 5@ten is;;k ≥ 10:  k − 2 ≥ 8, add one 3¢ stamp@add one"
The bases: eight is three plus five, nine is three threes, and ten is two fives. For the step, take k at least ten, and assume every amount from eight to k works. Then k minus two is at least eight, so it can be made. Add one three cent stamp, and you've made k plus one.

@chapter Counting base cases
@art three-pillars
Why three bases? Because the step reaches back three places. With only eight as a base, the step at nine and ten would lean on six and seven, which are outside the claim. And in fact seven can't be made at all. Counting the base cases correctly is the whole difficulty in this style of proof.

@art halving-split
Strong induction is the natural partner of a recursion whose calls aren't on n minus one. Merge sort splits at n over two. Binary search halves. Fibonacci reaches back two, so a proof about it needs two base cases. Each correctness proof needs every smaller value.

@chapter Where people slip
@list heading="Common slips" items="One base case when the step reaches back several@one base case|Using a case outside n₀ … k@outside the range|Strong induction by default@by default"
Three slips. Supplying one base case when the step reaches back several. That's the most common error of all. Using a case outside the range from n nought to k. And reaching for strong induction by default. If the step uses only P of k, say so. A stronger hypothesis than you need hides what the proof depends on.

@chapter Try it
@words text="every n ≥ 12 is 4a + 5b" sub="12 = 4+4+4 · 13 = 4+4+5 · 14 = 4+5+5 · 15 = 5+5+5"
Your turn. Show every amount from twelve on is four a plus five b. The step will reach back four, so you need four base cases: twelve, thirteen, fourteen and fifteen. Check each one.

@art fib-branch
Then, for k at least fifteen, k plus one minus four is k minus three, which is at least twelve. Add a four, and you're done. And here's why it starts at twelve: eleven is the largest amount you can't make from fours and fives.

@end text="A claim that survives five checks"
On Learn, you can watch a claim pass five checks in a row and then fail, which is why proofs matter. That's learn dot get er done dot I O.
