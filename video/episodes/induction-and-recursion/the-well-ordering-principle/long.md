---
format: long
lesson: induction-and-recursion/the-well-ordering-principle
title: The well-ordering principle: why induction works
thumb: There's always a smallest one
---

@chapter What induction stands on
@title text="The Well-Ordering Principle" sub="Induction and Recursion" art=thumb
Induction is the main tool of this whole course. You prove a first case, and a step from each case to the next.

@art dominoes
But a proof technique has to stand on something, and induction stands on one plain fact about the natural numbers.

@art first-in-line
Here it is. Take any collection of natural numbers, as long as it isn't empty. It always has a smallest member. That's the well-ordering principle.

@math heading="Well-ordering" items="S ⊆ ℕ,  S ≠ ∅@any subset;;there is m ∈ S with m ≤ s for every s ∈ S@there's a member"
In symbols: take any subset S of the naturals that isn't empty. Then there's a member m of S that's less than or equal to every member of S.

@chapter A property of ℕ
@art endless-descent
It sounds too obvious to say out loud. But it's a property of the naturals specifically, and it fails elsewhere. In the integers, the negative numbers form a nonempty set with no least element. Whatever candidate you pick, there's a smaller one below it.

@art halving-gap
The positive rationals fail too. Name any positive rational q, and q over two is smaller and still positive. The reals fail in the same way: the open interval from zero to one has no first number in it.

@list heading="No least element" items="ℤ: the negative integers@negative integers|ℚ⁺: the positive rationals@positive rationals|ℝ: the open interval (0, 1)@open interval"
So that's three nonempty sets with no least element: the negative integers, the positive rationals, and the open interval. For the naturals, the principle has to be assumed, or derived from an equivalent assumption.

@chapter Induction, from well-ordering
@words text="P(0)  and  P(k) → P(k+1)" sub="then P(n) for every n ∈ ℕ"
Now the payoff. Suppose P of zero is true, and P of k implies P of k plus one for every natural k. Well-ordering is enough to prove that P of n holds for every n.

@math heading="Suppose some P(n) fails" items="S = { n ∈ ℕ : P(n) is false } ≠ ∅@Collect every;;m = the least element of S@smallest member;;m ≠ 0, so m − 1 ∈ ℕ@can't be zero"
Collect every n where P is false into a set S, and suppose S isn't empty. Well-ordering hands you its smallest member, m. And m can't be zero, because P of zero holds, so m minus one is a natural number.

@math items="m − 1 < m, so m − 1 ∉ S@smaller than m;;so P(m − 1) is true@is true;;P(m − 1) → P(m): P(m) is true@the step gives;;contradiction, so S = ∅@contradicts"
Since m minus one is smaller than m, it isn't in S, so P of m minus one is true. Then the step gives you P of m. That contradicts m being in S, so S is empty, and P holds everywhere.

@art smallest-counterexample
That proof is worth reading twice. The base case rules out m equals zero. The step rules out every other m. And well-ordering guarantees that if any counterexample existed, there'd be a smallest one to rule out.

@chapter Minimal counterexample
@list heading="Minimal counterexample" items="Assume the claim fails somewhere@Assume the claim|Take the least n where it fails@Take the least|Derive a contradiction@derive a contradiction|Conclude there are no failures@Conclude"
The proof is also a template you can reuse. Assume the claim fails somewhere. Take the least n where it fails. Then derive a contradiction, usually by producing an even smaller counterexample. Conclude that there are no failures at all. This is sometimes called infinite descent.

@chapter An example: prime factors
@art factor-split
Here's the template at work. The claim: every integer greater than one has a prime factor. Suppose not, and let S be the set of integers greater than one with no prime factor.

@math items="m = the least element of S@smallest member;;m is not prime, so m = ab with 1 < a < m@isn't prime;;a ∉ S, so a has a prime factor p@isn't in S;;p | a and a | m, so p | m@divides m"
If S isn't empty, it has a smallest member, m. m isn't prime, because a prime divides itself. So m is a times b, with a between one and m. Since a is smaller than m, a isn't in S, so a has a prime factor p. And p divides a, which divides m, so p divides m. Contradiction.

@words text="Minimality is what licenses the claim about a"
Notice what did the work. Minimality of m is what let you say something about a. Without well-ordering there'd be no smallest counterexample, and the argument would have nothing to grip.

@chapter Where people slip
@list heading="Common slips" items="Assuming it holds for ℤ or ℚ@The first|Not showing the set is nonempty@The second|Using a set that isn't a subset of ℕ@the third"
Three slips. The first is assuming well-ordering holds for the integers or the rationals. It doesn't, so a minimal counterexample there needs a lower bound first. The second is forgetting to show the set is nonempty. And the third is taking the least element of a set that isn't a subset of the naturals.

@chapter Try it
@words text="a = dq + r,  0 ≤ r < d" sub="S = { a − dq : q ∈ ℤ,  a − dq ≥ 0 }"
To practise, prove the division algorithm. For any integer a and any d greater than zero, there are q and r with a equals d q plus r, and r at least zero and less than d. Start from the set of all values of a minus d q that are non-negative.

@art first-in-line zoom=in
That set sits inside the naturals, and it's nonempty: take q very negative. So it has a least element, r. Now suppose r is at least d, and look at r minus d. That's your contradiction.

@end text="Find the first false case"
You can hunt for the first false case of a statement, and see the least element the proof talks about, on Learn. That's learn dot get er done dot I O.
